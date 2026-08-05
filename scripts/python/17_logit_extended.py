"""Extended Logit specifications for the delegation decision.

Adds:
  Col 4: baseline + overconfidence + wa_confidence (full sample, with controls)
  Col 5: baseline (no attention exclusion) — robustness for §sec:result1
  Col 6: Punishment-only with belief differences AND no attention exclusion — robustness for Col (3)
"""
from __future__ import annotations

import statsmodels.api as sm

from lib.io import load_delegator
from lib.paths import TABLES
from lib.fmt import num
from lib.regtable import render_two_block_table
from lib import manifest

CONTROLS = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]


def fit_logit(y, X):
    X = sm.add_constant(X, has_constant="add")
    return sm.Logit(y.astype(float), X.astype(float)).fit(disp=False, cov_type="HC1")


def col_overconf(df):
    """Full sample, punish + overall_score + overconfidence + controls.
    Note: wa_confidence is omitted because overconfidence = wa_confidence - overall_score
    by construction (collinear with overall_score + overconfidence)."""
    cols = ["delegation", "punish", "overall_score", "overconfidence"] + CONTROLS
    sub = df[cols].dropna()
    return fit_logit(sub["delegation"],
                     sub[["punish", "overall_score", "overconfidence"] + CONTROLS]), len(sub)


def col_full_no_excl(df):
    """Col (1) without attention-check exclusion (it has none anyway, since main delegation
    decision predates the attention check). Trivially identical to existing Col (1).
    Included for completeness of the robustness panel."""
    sub = df[["delegation", "punish"]].dropna()
    return fit_logit(sub["delegation"], sub[["punish"]]), len(sub)


def col_pun_no_att_excl(df):
    """Col (3)-equivalent: Punishment only, with belief differences, but
    NOT excluding the attention-check failers (preregistered exclusion lifted).
    """
    sub = df[df["treat"] == 0].copy()
    sub["bel_diff_bad"] = sub["nodel_del_bad"]
    sub["bel_diff_good"] = sub["nodel_del_good"]
    cols = ["delegation", "bel_diff_bad", "bel_diff_good", "overall_score"] + CONTROLS
    sub = sub[cols].dropna()
    return fit_logit(sub["delegation"],
                     sub[["bel_diff_bad", "bel_diff_good", "overall_score"] + CONTROLS]), len(sub)


def main() -> None:
    d = load_delegator()
    d["punish"] = 1 - d["treat"]  # Punishment indicator (1 = Punishment condition)
    m_oc, n_oc = col_overconf(d)
    m_full, n_full = col_full_no_excl(d)
    m_pun_full, n_pun_full = col_pun_no_att_excl(d)

    # Robustness table: shows H1 effect persists with overconfidence added,
    # and the Punishment-only Col (3) result holds without attention-check exclusion.
    rows = [
        ("Punishment indicator", "punish"),
        ("Task performance", "overall_score"),
        ("Overconfidence", "overconfidence"),
        ("Punishment beliefs: bad outcome (no del.~$-$~del.)", "bel_diff_bad"),
        ("Punishment beliefs: good outcome (no del.~$-$~del.)", "bel_diff_good"),
    ]
    extra = [
        ("Controls", ["yes", "no", "yes"]),
        ("Attention-check excl.", ["yes (Player A)", "n/a", "no"]),
        ("Sample", ["Full", "Full", "Punishment"]),
        ("N", [f"${n_oc}$", f"${n_full}$", f"${n_pun_full}$"]),
        ("Pseudo $R^2$", [f"${num(m_oc.prsquared, 3)}$", f"${num(m_full.prsquared, 3)}$",
                          f"${num(m_pun_full.prsquared, 3)}$"]),
    ]

    p_overconf = float(m_oc.pvalues.get("overconfidence", float("nan")))
    p_treat_oc = float(m_oc.pvalues["punish"])
    p_treat_full = float(m_full.pvalues["punish"])
    p_perf_pun_full = float(m_pun_full.pvalues["overall_score"])
    p_bel_good_pun_full = float(m_pun_full.pvalues["bel_diff_good"])

    note = (
        "Robustness specifications for the delegation logit. "
        "Column (1) adds \\textit{overconfidence} (defined as the weighted-average belief about own "
        "performance minus actual performance) to the main full-sample specification. The treatment "
        f"effect remains: \\textit{{Punishment indicator}} $p={num(p_treat_oc, 3)}$. "
        f"\\textit{{Overconfidence}} is not significantly associated with delegation $p={num(p_overconf, 3)}$. "
        "Column (2) reproduces the unconditional treatment effect for completeness "
        f"($p={num(p_treat_full, 3)}$; identical to the main Col (1)). "
        "Column (3) restricts to the \\textit{Punishment} condition and includes the within-subject "
        "belief differences but \\textit{does not} exclude subjects who failed the belief-screen "
        "attention check; the heterogeneity result is preserved: "
        f"\\textit{{Task performance}} $p={num(p_perf_pun_full, 3)}$; "
        f"\\textit{{Punishment beliefs: good outcome}} $p={num(p_bel_good_pun_full, 3)}$. "
        "Robust HC1 standard errors in parentheses. Following AEA editorial policy, "
        "significance stars are not reported in the table."
    )

    (TABLES / "reg_delegation_robustness.tex").write_text(
        render_two_block_table(
            caption="Determinants of the delegation decision --- robustness",
            label="tab:reg_delegation_robustness",
            col_headers=[r"\multicolumn{2}{c}{\textit{Full sample}}", r"\textit{Punishment} (no excl.)"],
            block_label="Delegation",
            rows=rows,
            models=[m_oc, m_full, m_pun_full],
            extra_rows=extra,
            note=note,
        ),
        encoding="utf-8",
    )

    out = {
        "robust_overconf_punish_coef": round(float(m_oc.params["punish"]), 4),
        "robust_overconf_punish_p": round(p_treat_oc, 4),
        "robust_overconf_overconfidence_coef": round(float(m_oc.params["overconfidence"]), 4),
        "robust_overconf_overconfidence_p": round(p_overconf, 4),
        "robust_overconf_n": n_oc,
        "robust_pun_no_excl_n": n_pun_full,
        "robust_pun_no_excl_perf_coef": round(float(m_pun_full.params["overall_score"]), 4),
        "robust_pun_no_excl_perf_p": round(p_perf_pun_full, 4),
        "robust_pun_no_excl_bel_good_coef": round(float(m_pun_full.params["bel_diff_good"]), 4),
        "robust_pun_no_excl_bel_good_p": round(p_bel_good_pun_full, 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
