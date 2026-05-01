"""Logit regressions of delegation on condition + controls.

Produces:
  tables/reg_delegation.tex      (Table 1 — main, Cols 1/2/3)
  tables/reg_delegation_full.tex (Table A2 — full controls)
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


def col1(df):
    sub = df[["delegation", "treat"]].dropna()
    return fit_logit(sub["delegation"], sub[["treat"]]), len(sub)


def col2(df):
    cols = ["delegation", "treat", "overall_score"] + CONTROLS
    sub = df[cols].dropna()
    return fit_logit(sub["delegation"], sub[["treat", "overall_score"] + CONTROLS]), len(sub)


def col3(df):
    sub = df[df["treat"] == 0].copy()
    sub = sub[sub["pass_att2"] == 1]
    sub["bel_diff_bad"] = sub["nodel_del_bad"]
    sub["bel_diff_good"] = sub["nodel_del_good"]
    cols = ["delegation", "bel_diff_bad", "bel_diff_good", "overall_score"] + CONTROLS
    sub = sub[cols].dropna()
    return fit_logit(
        sub["delegation"],
        sub[["bel_diff_bad", "bel_diff_good", "overall_score"] + CONTROLS],
    ), len(sub)


def main() -> None:
    d = load_delegator()
    m1, n1 = col1(d)
    m2, n2 = col2(d)
    m3, n3 = col3(d)
    models = [m1, m2, m3]

    main_rows = [
        ("No-Punishment indicator", "treat"),
        ("Punishment beliefs: bad outcome (no del.~$-$~del.)", "bel_diff_bad"),
        ("Punishment beliefs: good outcome (no del.~$-$~del.)", "bel_diff_good"),
        ("Task performance", "overall_score"),
    ]
    extra_main = [
        ("Controls", ["no", "yes", "yes"]),
        ("N", [f"${n1}$", f"${n2}$", f"${n3}$"]),
        ("Pseudo $R^2$", [f"${num(m.prsquared, 3)}$" for m in models]),
    ]
    pvals = []
    for label, mod, name in [
        ("\\textit{No-Punishment indicator} Col~(1)", m1, "treat"),
        ("Col~(2)", m2, "treat"),
        ("\\textit{Task performance} Col~(3)", m3, "overall_score"),
        ("\\textit{Punishment beliefs: good outcome} Col~(3)", m3, "bel_diff_good"),
    ]:
        if mod is not None and name in mod.params.index:
            pvals.append(f"{label} $p={num(mod.pvalues[name], 3)}$")
    note_main = (
        "Coefficients from a Logit regression of the delegation decision on the condition indicator, "
        "task performance, and socio-demographic controls. Robust (HC1) standard errors in parentheses. "
        "Two-sided $p$-values for the headline coefficients: " + "; ".join(pvals) + ". "
        "Controls in Columns (2) and (3) include age, gender, self-reported socio-economic status, "
        "university education, technology affinity, and leadership experience; full results in "
        "Appendix Table~\\ref{tab:reg_delegation}. "
        "Two subjects are dropped in Column~(2) due to missing socio-demographic data. "
        "Column~(3) restricts to the \\textit{Punishment} condition and includes within-subject "
        "differences in expected punishment between non-delegated and delegated decisions for each "
        "outcome; subjects who failed the belief-screen attention check are excluded, as preregistered. "
        "Following AEA editorial policy, significance stars are not reported in the table; "
        "exact $p$-values are stated in this note."
    )
    (TABLES / "reg_delegation.tex").write_text(
        render_two_block_table(
            caption="Determinants of the delegation decision",
            label="tab:del_decision_determinants",
            col_headers=[r"\multicolumn{2}{c}{\textit{Full sample}}", r"\textit{Punishment only}"],
            block_label="Delegation",
            rows=main_rows,
            models=models,
            extra_rows=extra_main,
            note=note_main,
        ),
        encoding="utf-8",
    )

    full_rows = [
        ("No-Punishment indicator", "treat"),
        ("Punishment beliefs: bad outcome", "bel_diff_bad"),
        ("Punishment beliefs: good outcome", "bel_diff_good"),
        ("Task performance", "overall_score"),
        ("Age", "age"),
        ("Female", "female"),
        ("Socio-economic status", "socio_status"),
        ("Went to uni", "went_to_uni"),
        ("Technology score", "technology_score"),
        ("Leadership position", "leader"),
        ("Constant", "const"),
    ]
    extra_full = [
        ("N", [f"${n1}$", f"${n2}$", f"${n3}$"]),
        ("Pseudo $R^2$", [f"${num(m.prsquared, 3)}$" for m in models]),
    ]
    note_full = (
        "Logit estimates with robust (HC1) standard errors in parentheses. "
        "Two subjects in Column~(2) are dropped due to missing socio-demographic data. "
        "Column~(3) restricts to the \\textit{Punishment} condition and excludes subjects who "
        "failed the attention check on the belief-elicitation screen, as preregistered. "
        "The belief variables in Column~(3) are within-subject differences in expected punishment "
        "between non-delegated and delegated decisions for each outcome. "
        "Following AEA editorial policy, significance stars are not reported in the table."
    )
    (TABLES / "reg_delegation_full.tex").write_text(
        render_two_block_table(
            caption="Determinants of the delegation decision --- full controls",
            label="tab:reg_delegation",
            col_headers=[r"\multicolumn{2}{c}{\textit{Full sample}}", r"\textit{Punishment only}"],
            block_label="Delegation",
            rows=full_rows,
            models=models,
            extra_rows=extra_full,
            note=note_full,
        ),
        encoding="utf-8",
    )

    out = {
        "logit_col1_treat_coef": round(float(m1.params["treat"]), 4),
        "logit_col1_treat_se": round(float(m1.bse["treat"]), 4),
        "logit_col1_treat_p": round(float(m1.pvalues["treat"]), 4),
        "logit_col1_n": n1,
        "logit_col1_pseudo_r2": round(float(m1.prsquared), 4),
        "logit_col2_treat_coef": round(float(m2.params["treat"]), 4),
        "logit_col2_treat_se": round(float(m2.bse["treat"]), 4),
        "logit_col2_treat_p": round(float(m2.pvalues["treat"]), 4),
        "logit_col2_n": n2,
        "logit_col2_pseudo_r2": round(float(m2.prsquared), 4),
        "logit_col3_overall_score_coef": round(float(m3.params["overall_score"]), 4),
        "logit_col3_overall_score_p": round(float(m3.pvalues["overall_score"]), 4),
        "logit_col3_bel_good_coef": round(float(m3.params["bel_diff_good"]), 4),
        "logit_col3_bel_good_p": round(float(m3.pvalues["bel_diff_good"]), 4),
        "logit_col3_bel_bad_coef": round(float(m3.params["bel_diff_bad"]), 4),
        "logit_col3_bel_bad_p": round(float(m3.pvalues["bel_diff_bad"]), 4),
        "logit_col3_n": n3,
        "logit_col3_pseudo_r2": round(float(m3.prsquared), 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
