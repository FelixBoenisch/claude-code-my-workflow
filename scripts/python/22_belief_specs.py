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


def ame_pp10(model, var):
    """AME of `var` on P(delegation), in percentage points per GBP 0.10.

    get_margeff returns effects per GBP 1 of belief difference; x100 gives
    percentage points, /10 rescales to the GBP 0.10 elicitation increment.
    """
    me = model.get_margeff(at="overall", method="dydx")
    names = [n for n in model.model.exog_names if n != "const"]
    i = names.index(var)
    return 10.0 * float(me.margeff[i]), float(me.pvalues[i])


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
    def ame_cells(specs):
        """One (coef, p) cell pair per column; each spec is (model, var) or None."""
        coef_cells, p_cells = [], []
        for spec in specs:
            if spec is None:
                coef_cells.append("")
                p_cells.append("")
                continue
            m, var = spec
            a, ap = ame_pp10(m, var)
            star = stars_for(ap)
            coef_cells.append(f"${num(a, 1)}^{{{star}}}$" if star else f"${num(a, 1)}$")
            p_cells.append(f"$(p={num(ap, 3)})$")
        return coef_cells, p_cells

    ame_main, ame_main_p = ame_cells([
        (m1, "bel_diff_avg"),
        (m2, "bel_diff_avg"),
        (m3, "bel_diff_avg"),
        (m4, "bel_diff_weighted"),
        None,
    ])
    ame_good, ame_good_p = ame_cells([None, None, None, None, (m5, "bel_diff_good")])
    ame_bad, ame_bad_p = ame_cells([None, None, None, None, (m5, "bel_diff_bad")])

    YES, NO = r"\checkmark", r"$\times$"
    extra = [
        (r"AME of belief measure (pp per \pounds 0.10)", ame_main),
        ("", ame_main_p),
        (r"AME: good-outcome difference (pp per \pounds 0.10)", ame_good),
        ("", ame_good_p),
        (r"AME: bad-outcome difference (pp per \pounds 0.10)", ame_bad),
        ("", ame_bad_p),
        ("Controls",     [NO, YES, YES, YES, YES]),
        ("Passers only", [NO, NO, YES, YES, YES]),
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
        "belief differences entered separately. "
        "The \\textit{AME} rows report the average marginal effect of the belief measure "
        "entered in the respective column on the probability of delegation, in percentage "
        "points per \\pounds 0.10 increase in the corresponding belief difference."
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
                a, ap = ame_pp10(m, v)
                out[f"belspec_col{i}_{v}_ame_pp10"] = round(a, 2)
                out[f"belspec_col{i}_{v}_ame_p"]    = round(ap, 4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
