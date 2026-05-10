"""Belief-difference specifications for the punishment-beliefs paragraph.

Five columns, all restricted to the Punishment condition:

  (1) Simple-average belief difference, full Punishment, no controls
  (2) Simple-average belief difference, full Punishment, with controls
  (3) Simple-average belief difference, passers only, with controls
  (4) Weighted (by P(good)) belief difference, passers only, with controls
  (5) Two-difference decomposition (good + bad), passers only, with controls

Outputs tables/reg_belief_specs.tex (label: tab:reg_belief_specs).
"""
from __future__ import annotations

import statsmodels.api as sm

from lib.io import load_delegator
from lib.paths import TABLES
from lib.fmt import num
from lib.regtable import render_two_block_table, stars_for
from lib import manifest

SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
CTRLS = ["overall_score"] + SES


def fit_logit(y, X):
    X = sm.add_constant(X, has_constant="add")
    return sm.Logit(y.astype(float), X.astype(float)).fit(disp=False, cov_type="HC1")


def fit_spec(df, regs):
    sub = df[["delegation"] + regs].dropna()
    return fit_logit(sub["delegation"], sub[regs]), len(sub)


def main() -> None:
    d = load_delegator()
    sub = d[d["treat"] == 0].copy()
    sub["bel_diff_good"] = sub["nodel_del_good"]
    sub["bel_diff_bad"]  = sub["nodel_del_bad"]
    sub["bel_diff_avg"]  = 0.5 * (sub["bel_diff_good"] + sub["bel_diff_bad"])
    sub["p_success"]     = sub["wa_confidence"] / 10.0
    sub["bel_diff_weighted"] = (sub["p_success"] * sub["bel_diff_good"]
                                + (1 - sub["p_success"]) * sub["bel_diff_bad"])
    pas = sub[sub["pass_att2"] == 1].copy()

    m1, n1 = fit_spec(sub, ["bel_diff_avg"])
    m2, n2 = fit_spec(sub, ["bel_diff_avg"] + CTRLS)
    m3, n3 = fit_spec(pas, ["bel_diff_avg"] + CTRLS)
    m4, n4 = fit_spec(pas, ["bel_diff_weighted"] + CTRLS)
    m5, n5 = fit_spec(pas, ["bel_diff_bad", "bel_diff_good"] + CTRLS)
    models = [m1, m2, m3, m4, m5]
    ns = [n1, n2, n3, n4, n5]

    rows = [
        (r"Punishment beliefs: simple average ($\overline{\Delta}$)",     "bel_diff_avg"),
        (r"Punishment beliefs: weighted by $\Pr(\text{good})$",           "bel_diff_weighted"),
        (r"Punishment beliefs: bad outcome (no del.~$-$~del.)",           "bel_diff_bad"),
        (r"Punishment beliefs: good outcome (no del.~$-$~del.)",          "bel_diff_good"),
        ("Task performance",       "overall_score"),
        ("Age",                    "age"),
        ("Female",                 "female"),
        ("Socio-economic status",  "socio_status"),
        ("Went to uni",            "went_to_uni"),
        ("Technology score",       "technology_score"),
        ("Leadership position",    "leader"),
        ("Constant",               "const"),
    ]
    extra = [
        ("Controls", ["No", "Yes", "Yes", "Yes", "Yes"]),
        ("Sample",   [r"\textit{Punishment}",
                      r"\textit{Punishment}",
                      r"Passers",
                      r"Passers",
                      r"Passers"]),
        ("N",            [f"${n}$" for n in ns]),
        (r"Pseudo $R^2$", [f"${num(m.prsquared, 3)}$" for m in models]),
    ]
    note = (
        "Logit estimates with robust (HC1) standard errors in parentheses. "
        "Significance: $^{*}\\,p<0.10$; $^{**}\\,p<0.05$; $^{***}\\,p<0.01$ (two-sided). "
        "Sample restricted to the \\textit{Punishment} condition throughout, "
        "since beliefs about a counterfactual that cannot materialise do not "
        "enter Player~A's decision rule in the \\textit{No-Punishment} arm. "
        "Belief differences are within-subject \\textit{(no delegation)}~$-$~\\textit{(delegation)} "
        "in expected punishment, so positive coefficients indicate that subjects who expect "
        "to be punished more harshly for not delegating (relative to delegating) are more "
        "likely to delegate. Column~(1) uses the simple average of the two outcome-conditional "
        "belief differences without controls; Column~(2) adds task performance and "
        "socio-demographic controls; Column~(3) restricts to subjects who passed the "
        "attention check on the belief-elicitation screen, as preregistered; "
        "Column~(4) replaces the simple average with a weighted average using "
        "Player~A's elicited probability of producing the high payoff "
        "($\\Pr(\\text{good})=$ \\textit{wa\\_confidence}$/10$); "
        "Column~(5) replaces the single belief regressor with the two outcome-conditional "
        "belief differences entered separately."
    )
    table = render_two_block_table(
        caption="Delegation and punishment beliefs",
        label="tab:reg_belief_specs",
        col_headers=[r"\multicolumn{2}{c}{\textit{Full Punishment}}",
                     r"\multicolumn{3}{c}{\textit{Punishment, passers}}"],
        block_label="Delegation",
        rows=rows,
        models=models,
        extra_rows=extra,
        note=note,
        column_spec="@{\\extracolsep{5pt}}lcc|ccc",
        stars=True,
    )
    (TABLES / "reg_belief_specs.tex").write_text(table, encoding="utf-8")

    out = {}
    for i, (m, n) in enumerate(zip(models, ns), start=1):
        out[f"belspec_col{i}_n"] = n
        out[f"belspec_col{i}_pseudo_r2"] = round(float(m.prsquared), 4)
        for v in ["bel_diff_avg", "bel_diff_weighted", "bel_diff_bad", "bel_diff_good"]:
            if v in m.params.index:
                out[f"belspec_col{i}_{v}_coef"] = round(float(m.params[v]), 4)
                out[f"belspec_col{i}_{v}_se"]   = round(float(m.bse[v]), 4)
                out[f"belspec_col{i}_{v}_p"]    = round(float(m.pvalues[v]), 4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
