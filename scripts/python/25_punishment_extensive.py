"""Extensive-margin probit: P(any punishment) by delegation and outcome.

Produces tables/reg_punishment_extensive.tex (appendix). DV = 1{punishment > 0}
in a cell, stacked over the four (delegation, outcome) cells (4 obs per Player B),
probit with SE clustered at the Player-B level. Two columns: full sample and
attention-check passers.

The Delegated x Bad interaction means the interpretable quantities are the
discrete average marginal effects (AME) of delegation and of the bad outcome,
computed by counterfactual prediction; their p-values come from a seeded
subject-cluster bootstrap (deterministic).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import norm

from lib.io import load_evaluator
from lib.paths import TABLES
from lib.fmt import num
from lib.regtable import render_two_block_table, stars_for
from lib import manifest

CELLS = [("punish_del_good", 1, 0), ("punish_del_bad", 1, 1),
         ("punish_nodel_good", 0, 0), ("punish_nodel_bad", 0, 1)]
SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
REGS = ["delegated", "bad_outcome", "interaction", "wa_difficulty"] + SES
BOOT_REPS = 400
SEED = 0


def long_panel(df):
    rows = []
    for col, deleg, bad in CELLS:
        s = df[["code", col, "wa_difficulty"] + SES].copy().rename(columns={col: "pun"})
        s["punish_bin"] = (s["pun"] > 0).astype(float)
        s["delegated"], s["bad_outcome"] = deleg, bad
        rows.append(s)
    p = pd.concat(rows, ignore_index=True)
    p["interaction"] = p["delegated"] * p["bad_outcome"]
    return p[["code", "punish_bin"] + REGS].dropna()


def fit(panel, cluster=True):
    X = sm.add_constant(panel[REGS].astype(float), has_constant="add")
    kw = dict(cov_type="cluster", cov_kwds={"groups": panel["code"].astype(str)}) if cluster else {}
    return sm.Probit(panel["punish_bin"].astype(float), X).fit(disp=False, **kw)


def discrete_ames(res, panel):
    X = sm.add_constant(panel[REGS].astype(float), has_constant="add")
    x1, x0 = X.copy(), X.copy()
    x1["delegated"], x1["interaction"] = 1.0, panel["bad_outcome"].values
    x0["delegated"], x0["interaction"] = 0.0, 0.0
    ame_del = float((res.predict(x1) - res.predict(x0)).mean())
    xb1, xb0 = X.copy(), X.copy()
    xb1["bad_outcome"], xb1["interaction"] = 1.0, panel["delegated"].values
    xb0["bad_outcome"], xb0["interaction"] = 0.0, 0.0
    ame_bad = float((res.predict(xb1) - res.predict(xb0)).mean())
    return ame_del, ame_bad


def ame_with_p(panel):
    res = fit(panel)
    ad, ab = discrete_ames(res, panel)
    rng = np.random.RandomState(SEED)
    codes = panel["code"].unique()
    by = {c: panel[panel["code"] == c] for c in codes}
    bd, bb = [], []
    for _ in range(BOOT_REPS):
        draw = rng.choice(codes, size=len(codes), replace=True)
        bs = pd.concat([by[c] for c in draw], ignore_index=True)
        try:
            r = fit(bs, cluster=False)
            d, b = discrete_ames(r, bs)
            bd.append(d); bb.append(b)
        except Exception:
            continue
    p_del = 2 * norm.cdf(-abs(ad / np.std(bd, ddof=1)))
    p_bad = 2 * norm.cdf(-abs(ab / np.std(bb, ddof=1)))
    return res, (ad, p_del), (ab, p_bad), int(panel["code"].nunique()), len(panel)


def ame_cells(ame_p_full, ame_p_pass):
    coefs, ps = [], []
    for (a, p) in (ame_p_full, ame_p_pass):
        star = stars_for(p)
        coefs.append(f"${num(100 * a, 1)}^{{{star}}}$" if star else f"${num(100 * a, 1)}$")
        ps.append("$(p<0.001)$" if p < 0.001 else f"$(p={num(p, 3)})$")
    return coefs, ps


def main() -> None:
    e = load_evaluator()
    pun = e[e["treat"] == 0]
    full = long_panel(pun)
    passers = long_panel(pun[pun["pass_att2"] == 1])

    rf, adf, abf, nsf, nf = ame_with_p(full)
    rp, adp, abp, nsp, npn = ame_with_p(passers)

    rows = [
        ("Delegated", "delegated"),
        ("Bad outcome", "bad_outcome"),
        ("Delegated $\\times$ Bad outcome", "interaction"),
        ("Player B belief about Player A perf.", "wa_difficulty"),
        ("Age", "age"), ("Female", "female"), ("Socio-economic status", "socio_status"),
        ("Went to uni", "went_to_uni"), ("Technology score", "technology_score"),
        ("Leadership position", "leader"), ("Constant", "const"),
    ]
    del_coefs, del_ps = ame_cells(adf, adp)
    bad_coefs, bad_ps = ame_cells(abf, abp)
    extra = [
        ("AME of Delegated (pp)", del_coefs),
        ("", del_ps),
        ("AME of Bad outcome (pp)", bad_coefs),
        ("", bad_ps),
        ("Observations", [f"${nf}$", f"${npn}$"]),
        ("Subjects", [f"${nsf}$", f"${nsp}$"]),
        ("Pseudo $R^2$", [f"${num(rf.prsquared, 3)}$", f"${num(rp.prsquared, 3)}$"]),
    ]
    note = (
        "Probit regression of an indicator for non-zero punishment. The sample is stacked over "
        "the four (delegation, outcome) cells of the strategy method (4 observations per Player~B). "
        "Column~(1) uses the full Punishment-condition sample; Column~(2) restricts to attention-check "
        "passers. Standard errors clustered at the Player~B level. The \\textit{AME} rows report "
        "discrete average marginal effects on the probability of imposing any punishment, in "
        "percentage points. AME p-values use a $400$-replication subject-cluster bootstrap. "
        "Significance: $^{*}\\,p<0.10$; $^{**}\\,p<0.05$; $^{***}\\,p<0.01$."
    )
    table = render_two_block_table(
        caption="Extensive margin of punishment --- Probit",
        label="tab:reg_punishment_extensive",
        col_headers=[r"\textit{Full sample}", r"\textit{Passers}"],
        block_label="Any punishment",
        rows=rows,
        models=[rf, rp],
        extra_rows=extra,
        note=note,
        column_spec=(
            "@{\\extracolsep{5pt}}l"
            "*{2}{>{\\centering\\arraybackslash}p{2.0cm}}"
        ),
        stars=True,
        separate_note=True,
    )
    (TABLES / "reg_punishment_extensive.tex").write_text(table, encoding="utf-8")

    out = {
        "ext_ame_del_full_pp": round(100 * adf[0], 2), "ext_ame_del_full_p": round(adf[1], 4),
        "ext_ame_del_pass_pp": round(100 * adp[0], 2), "ext_ame_del_pass_p": round(adp[1], 4),
        "ext_ame_bad_full_pp": round(100 * abf[0], 2), "ext_ame_bad_full_p": round(abf[1], 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
