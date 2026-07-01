"""One-off: extensive-margin probit for Player B punishment.

DV = 1{punishment > 0} in a cell, stacked over the four (delegation, outcome)
cells (4 obs per Player B), clustered SE at the Player-B level. Two columns:
full sample and attention-check passers.

Reports probit coefficients and the *discrete* average marginal effects (AME) of
delegation and of the bad outcome, computed by counterfactual prediction so the
Delegated x Bad interaction is handled correctly. AME p-values come from a
cluster (subject) bootstrap.

Output: quality_reports/extensive_margin_probit.md   (not in run_all.py)
"""
from __future__ import annotations
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PARQUET = os.path.join(ROOT, "data", "clean", "evaluator_cleaned.parquet")
OUT = os.path.join(ROOT, "quality_reports", "extensive_margin_probit.md")

CELLS = [("punish_del_good", 1, 0), ("punish_del_bad", 1, 1),
         ("punish_nodel_good", 0, 0), ("punish_nodel_bad", 0, 1)]
SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
REGS = ["delegated", "bad_outcome", "interaction", "wa_difficulty"] + SES
ROWS = [
    ("Delegated", "delegated"),
    ("Bad outcome", "bad_outcome"),
    ("Delegated $\\times$ Bad outcome", "interaction"),
    ("Player B belief about Player A perf.", "wa_difficulty"),
    ("Age", "age"), ("Female", "female"), ("Socio-economic status", "socio_status"),
    ("Went to uni", "went_to_uni"), ("Technology score", "technology_score"),
    ("Leadership position", "leader"), ("Constant", "const"),
]


def stars(p):
    return "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.10 else ""


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
    # AME of delegation: del 0->1 with interaction = bad_outcome
    x1, x0 = X.copy(), X.copy()
    x1["delegated"], x1["interaction"] = 1.0, panel["bad_outcome"].values
    x0["delegated"], x0["interaction"] = 0.0, 0.0
    ame_del = (res.predict(x1) - res.predict(x0)).mean()
    # AME of bad outcome: bad 0->1 with interaction = delegated
    xb1, xb0 = X.copy(), X.copy()
    xb1["bad_outcome"], xb1["interaction"] = 1.0, panel["delegated"].values
    xb0["bad_outcome"], xb0["interaction"] = 0.0, 0.0
    ame_bad = (res.predict(xb1) - res.predict(xb0)).mean()
    return ame_del, ame_bad


def boot_p(panel, reps=400, seed=0):
    rng = np.random.RandomState(seed)
    codes = panel["code"].unique()
    by = {c: panel[panel["code"] == c] for c in codes}
    dels, bads = [], []
    for _ in range(reps):
        draw = rng.choice(codes, size=len(codes), replace=True)
        bs = pd.concat([by[c] for c in draw], ignore_index=True)
        try:
            r = fit(bs, cluster=False)
            ad, ab = discrete_ames(r, bs)
            dels.append(ad); bads.append(ab)
        except Exception:
            continue
    def p(arr, pt):
        se = np.std(arr, ddof=1)
        from scipy.stats import norm
        return 2 * norm.cdf(-abs(pt / se)) if se > 0 else np.nan
    return dels, bads


def column(panel):
    res = fit(panel)
    ad, ab = discrete_ames(res, panel)
    dels, bads = boot_p(panel)
    from scipy.stats import norm
    p_del = 2 * norm.cdf(-abs(ad / np.std(dels, ddof=1)))
    p_bad = 2 * norm.cdf(-abs(ab / np.std(bads, ddof=1)))
    return res, (ad, p_del), (ab, p_bad), panel["code"].nunique(), len(panel)


def cell(res, key):
    if key not in res.params.index:
        return ""
    b, se, p = res.params[key], res.bse[key], res.pvalues[key]
    return f"{b:.3f}{stars(p)} ({se:.3f})"


def main():
    e = pd.read_parquet(PARQUET)
    pun = e[e["treat"] == 0]
    full = long_panel(pun)
    passers = long_panel(pun[pun["pass_att2"] == 1])

    rf, adf, abf, nsf, nf = column(full)
    rp, adp, abp, nsp, npn = column(passers)

    md = ["# Extensive-margin probit: P(any punishment)\n",
          "DV = $1\\{\\text{punishment} > 0\\}$ in a cell, stacked over the four "
          "(delegation, outcome) cells (4 obs per Player~B). Probit; SE clustered at the "
          "Player~B level, in parentheses. Stars: * p<0.10, ** p<0.05, *** p<0.01.\n",
          "| Variable | Full sample | Passers |", "|---|---|---|"]
    for label, key in ROWS:
        md.append(f"| {label} | {cell(rf, key)} | {cell(rp, key)} |")
    md.append(f"| **AME of Delegated (pp)** | {100*adf[0]:.1f} (p={adf[1]:.3f}) | {100*adp[0]:.1f} (p={adp[1]:.3f}) |")
    md.append(f"| **AME of Bad outcome (pp)** | {100*abf[0]:.1f} (p={abf[1]:.3f}) | {100*abp[0]:.1f} (p={abp[1]:.3f}) |")
    md.append(f"| Observations | {nf} | {npn} |")
    md.append(f"| Subjects | {nsf} | {nsp} |")
    md.append(f"| Pseudo R2 | {rf.prsquared:.3f} | {rp.prsquared:.3f} |")
    md.append("\n**Note.** The AME rows are *discrete* average marginal effects on the "
              "probability of imposing any punishment, in percentage points: for Delegated, the "
              "average change from setting delegated $0\\to1$ (with the interaction moved "
              "consistently); for Bad outcome, the change from setting bad $0\\to1$. They are "
              "computed by counterfactual prediction (not naive margins, which mishandle the "
              "interaction), with p-values from a 400-rep subject-cluster bootstrap. The probit "
              "interaction *coefficient* is not itself the marginal interaction effect "
              "(Ai \\& Norton 2003); read the AME rows for interpretation.\n")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
