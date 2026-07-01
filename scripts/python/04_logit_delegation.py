"""Logit regressions of delegation on condition + controls.

Produces:
  tables/reg_delegation.tex          (Main 5-col table for the With-Controls paragraph)
  tables/reg_delegation_full.tex     (Mirror of the main, kept for the appendix input)
  tables/reg_delegation_beliefs.tex  (Punishment-only spec with belief differences,
                                      kept for the punishment-beliefs paragraph downstream)
"""
from __future__ import annotations

import statsmodels.api as sm

from lib.io import load_delegator
from lib.paths import TABLES
from lib.fmt import num
from lib.regtable import render_two_block_table, stars_for
from lib import manifest

SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]


def fit_logit(y, X):
    X = sm.add_constant(X, has_constant="add")
    return sm.Logit(y.astype(float), X.astype(float)).fit(disp=False, cov_type="HC1")


def fit_probit(y, X):
    X = sm.add_constant(X, has_constant="add")
    return sm.Probit(y.astype(float), X.astype(float)).fit(disp=False, cov_type="HC1")


def fit_spec(df, regs, restrict_passers=False, fitter=fit_logit):
    sample = df.loc[df["pass_att2"] == 1].copy() if restrict_passers else df
    sub = sample[["delegation"] + regs].dropna()
    return fitter(sub["delegation"], sub[regs]), len(sub)


def ame_pp(model):
    me = model.get_margeff(at="overall", method="dydx")
    return float(me.margeff[0]), float(me.pvalues[0])


def main() -> None:
    d = load_delegator()

    # --- Main 5-column specifications --------------------------------------
    # The body table (tab:del_decision_determinants -> reg_delegation.tex) is
    # reported as Probit; the appendix mirror (tab:reg_delegation ->
    # reg_delegation_full.tex) and the manifest remain Logit.
    spec_defs = [
        (["treat"], False),
        (["treat"] + SES, False),
        (["treat"] + SES + ["overall_score"], False),
        (["treat"] + SES + ["wa_confidence"], False),
        (["treat"] + SES + ["overall_score"], True),
    ]
    logit_models, probit_models, ns = [], [], []
    for regs, passers in spec_defs:
        ml, n = fit_spec(d, regs, restrict_passers=passers, fitter=fit_logit)
        mp, _ = fit_spec(d, regs, restrict_passers=passers, fitter=fit_probit)
        logit_models.append(ml)
        probit_models.append(mp)
        ns.append(n)
    main_models = logit_models  # used for the appendix mirror and the manifest

    main_rows = [
        ("No-Punishment indicator", "treat"),
        ("Task performance", "overall_score"),
        ("Perceived performance", "wa_confidence"),
        ("Age", "age"),
        ("Female", "female"),
        ("Socio-economic status", "socio_status"),
        ("Went to uni", "went_to_uni"),
        ("Technology score", "technology_score"),
        ("Leadership position", "leader"),
        ("Constant", "const"),
    ]

    def build_extra(models):
        ame_coef_cells, ame_p_cells = [], []
        for m in models:
            a, ap = ame_pp(m)
            star = stars_for(ap)
            ame_coef_cells.append(
                f"${num(100 * a, 1)}^{{{star}}}$" if star else f"${num(100 * a, 1)}$"
            )
            ame_p_cells.append(f"$(p={num(ap, 3)})$")
        return [
            ("AME of No-Punishment (pp)", ame_coef_cells),
            ("", ame_p_cells),
            ("N", [f"${n}$" for n in ns]),
            ("Pseudo $R^2$", [f"${num(m.prsquared, 3)}$" for m in models]),
        ]

    note_template = (
        "Coefficients from a {model} regression of the delegation decision on the "
        "No-Punishment indicator and the controls listed in each column. "
        "Robust (HC1) standard errors in parentheses. "
        "Significance: $^{{*}}\\,p<0.10$; $^{{**}}\\,p<0.05$; $^{{***}}\\,p<0.01$ (two-sided). "
        "Two subjects are dropped in Columns~(2)--(4) due to missing socio-demographic "
        "data. The \\textit{{AME of No-Punishment}} row reports the average marginal "
        "effect of the No-Punishment indicator on the probability of delegation, in "
        "percentage points."
    )

    # --- Body table -> Probit ----------------------------------------------
    main_table = render_two_block_table(
        caption="Determinants of the delegation decision",
        label="tab:del_decision_determinants",
        col_headers=[r"\multicolumn{4}{c}{\textit{Full sample}}", r"\textit{Passers}"],
        block_label="Delegation",
        rows=main_rows,
        models=probit_models,
        extra_rows=build_extra(probit_models),
        note=note_template.format(model="Probit"),
        column_spec="@{\\extracolsep{5pt}}lcccc|c",
        stars=True,
    )
    (TABLES / "reg_delegation.tex").write_text(main_table, encoding="utf-8")

    # --- Appendix-full table: same specifications, Logit, alternative label -
    appendix_table = render_two_block_table(
        caption="Determinants of the delegation decision --- full controls",
        label="tab:reg_delegation",
        col_headers=[r"\multicolumn{4}{c}{\textit{Full sample}}", r"\textit{Passers}"],
        block_label="Delegation",
        rows=main_rows,
        models=logit_models,
        extra_rows=build_extra(logit_models),
        note=note_template.format(model="Logit"),
        column_spec="@{\\extracolsep{5pt}}lcccc|c",
        stars=True,
    )
    (TABLES / "reg_delegation_full.tex").write_text(appendix_table, encoding="utf-8")

    # --- Punishment-only spec with belief differences -----------------------
    # Kept for the punishment-beliefs paragraph downstream. Routed to its own
    # file/label so the main table is no longer responsible for it.
    sub_b = d[d["treat"] == 0].copy()
    sub_b = sub_b[sub_b["pass_att2"] == 1]
    sub_b["bel_diff_bad"] = sub_b["nodel_del_bad"]
    sub_b["bel_diff_good"] = sub_b["nodel_del_good"]
    cols_b = ["delegation", "bel_diff_bad", "bel_diff_good", "overall_score"] + SES
    sub_b = sub_b[cols_b].dropna()
    m_b = fit_logit(
        sub_b["delegation"],
        sub_b[["bel_diff_bad", "bel_diff_good", "overall_score"] + SES],
    )
    n_b = len(sub_b)

    beliefs_rows = [
        ("Punishment beliefs: bad outcome (no del.~$-$~del.)", "bel_diff_bad"),
        ("Punishment beliefs: good outcome (no del.~$-$~del.)", "bel_diff_good"),
        ("Task performance", "overall_score"),
        ("Age", "age"),
        ("Female", "female"),
        ("Socio-economic status", "socio_status"),
        ("Went to uni", "went_to_uni"),
        ("Technology score", "technology_score"),
        ("Leadership position", "leader"),
        ("Constant", "const"),
    ]
    extra_b = [
        ("N", [f"${n_b}$"]),
        ("Pseudo $R^2$", [f"${num(m_b.prsquared, 3)}$"]),
    ]
    note_b = (
        "Logit estimates with robust (HC1) standard errors in parentheses. "
        "Significance: $^{*}\\,p<0.10$; $^{**}\\,p<0.05$; $^{***}\\,p<0.01$ (two-sided). "
        "Sample restricted to the \\textit{Punishment} condition and to subjects who "
        "passed the attention check on the belief-elicitation screen, as preregistered. "
        "Belief variables are within-subject differences in expected punishment "
        "between non-delegated and delegated decisions for each outcome."
    )
    beliefs_table = render_two_block_table(
        caption="Delegation and punishment beliefs --- Punishment condition only",
        label="tab:reg_delegation_beliefs",
        col_headers=[r"\textit{Punishment, attention passers}"],
        block_label="Delegation",
        rows=beliefs_rows,
        models=[m_b],
        extra_rows=extra_b,
        note=note_b,
        column_spec="@{\\extracolsep{5pt}}l|c",
        stars=True,
    )
    (TABLES / "reg_delegation_beliefs.tex").write_text(beliefs_table, encoding="utf-8")

    # --- Manifest ----------------------------------------------------------
    out = {}
    for i, (m, n) in enumerate(zip(main_models, ns), start=1):
        out[f"logit_col{i}_treat_coef"] = round(float(m.params["treat"]), 4)
        out[f"logit_col{i}_treat_se"] = round(float(m.bse["treat"]), 4)
        out[f"logit_col{i}_treat_p"] = round(float(m.pvalues["treat"]), 4)
        a, ap = ame_pp(m)
        out[f"logit_col{i}_ame_pp"] = round(100 * a, 2)
        out[f"logit_col{i}_ame_p"] = round(ap, 4)
        out[f"logit_col{i}_n"] = n
        out[f"logit_col{i}_pseudo_r2"] = round(float(m.prsquared), 4)
    out.update({
        "logit_beliefs_overall_score_coef": round(float(m_b.params["overall_score"]), 4),
        "logit_beliefs_overall_score_p": round(float(m_b.pvalues["overall_score"]), 4),
        "logit_beliefs_bel_good_coef": round(float(m_b.params["bel_diff_good"]), 4),
        "logit_beliefs_bel_good_p": round(float(m_b.pvalues["bel_diff_good"]), 4),
        "logit_beliefs_bel_bad_coef": round(float(m_b.params["bel_diff_bad"]), 4),
        "logit_beliefs_bel_bad_p": round(float(m_b.pvalues["bel_diff_bad"]), 4),
        "logit_beliefs_n": n_b,
        "logit_beliefs_pseudo_r2": round(float(m_b.prsquared), 4),
    })
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
