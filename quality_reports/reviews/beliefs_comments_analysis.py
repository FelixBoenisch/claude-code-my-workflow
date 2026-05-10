"""Ad-hoc analyses requested by inline comments in results.tex (lines 72-96).

Each block produces console output that is pasted verbatim into
quality_reports/reviews/beliefs_comments_thoughts.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "python"))

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

from lib.io import load_delegator, load_evaluator

CELLS = [
    ("del_good",   "Delegated + Good"),
    ("del_bad",    "Delegated + Bad"),
    ("nodel_good", "Self + Good"),
    ("nodel_bad",  "Self + Bad"),
]

def banner(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)


def fit_logit(y, X):
    X = sm.add_constant(X, has_constant="add")
    return sm.Logit(y.astype(float), X.astype(float)).fit(disp=False, cov_type="HC1")


def fmt(m, var):
    if var not in m.params.index:
        return ""
    b = m.params[var]
    se = m.bse[var]
    p = m.pvalues[var]
    return f"{var:<28s} b={b:+.3f}  SE={se:.3f}  p={p:.3f}"


# ---------------------------------------------------------------------------
def analysis_1_realized_vs_anticipated():
    """Comment on line 77: figure comparing realized vs anticipated punishment."""
    banner("ANALYSIS 1: Realized vs anticipated punishment per scenario")

    d = load_delegator()
    e = load_evaluator()

    # Realized: Player B in PUNISHMENT (treat==0).
    # Anticipated: Player A in PUNISHMENT (treat==0).
    cells_eval = [("punish_del_good","del_good"),("punish_del_bad","del_bad"),
                  ("punish_nodel_good","nodel_good"),("punish_nodel_bad","nodel_bad")]
    cells_del  = [("belief_del_good","del_good"),("belief_del_bad","del_bad"),
                  ("belief_nodel_good","nodel_good"),("belief_nodel_bad","nodel_bad")]

    for sample_name, mask_e, mask_d in [
        ("FULL Punishment-condition sample",
         e["treat"]==0, d["treat"]==0),
        ("PASSERS only (pass_att2==1, treat==0)",
         (e["treat"]==0)&(e["pass_att2"]==1), (d["treat"]==0)&(d["pass_att2"]==1)),
    ]:
        ee = e.loc[mask_e]
        dd = d.loc[mask_d]
        print(f"\n--- {sample_name} ---  (n_PlayerB={len(ee)},  n_PlayerA={len(dd)})")
        print(f"{'Cell':<22}{'Realized (B)':>14}{'Anticipated (A)':>18}{'Belief gap':>14}")
        for (col_e, key),(col_d,_) in zip(cells_eval, cells_del):
            r = ee[col_e].mean()
            a = dd[col_d].mean()
            print(f"{key:<22}{r:>14.3f}{a:>18.3f}{a-r:>+14.3f}")

        # Per-cell two-sample tests (between subject; A vs B are different participants)
        print(f"\n  Tests for (A's belief != B's realized):")
        for (col_e,_),(col_d,key) in zip(cells_eval,
                                          [("belief_del_good","del_good"),
                                           ("belief_del_bad","del_bad"),
                                           ("belief_nodel_good","nodel_good"),
                                           ("belief_nodel_bad","nodel_bad")]):
            t,p = stats.ttest_ind(dd[col_d].dropna(), ee[col_e].dropna(), equal_var=False)
            print(f"    {key:<22}t={t:+.2f}  p={p:.4f}")


# ---------------------------------------------------------------------------
def analysis_2_beliefs_vary_with_delegation():
    """Comment on line 79: do beliefs vary with delegation decision?"""
    banner("ANALYSIS 2: Belief level by delegation choice (within each treatment)")

    d = load_delegator()
    cells = ["belief_del_good","belief_del_bad","belief_nodel_good","belief_nodel_bad"]
    diff_cols = ["nodel_del_good","nodel_del_bad"]

    for tlab, tval in [("Punishment (treat=0)", 0), ("No-Punishment (treat=1, hypothetical)", 1)]:
        for pass_lab, pass_mask in [
            ("FULL", lambda x: pd.Series(True, index=x.index)),
            ("PASSERS", lambda x: x["pass_att2"]==1),
        ]:
            sub = d[(d["treat"]==tval) & pass_mask(d)]
            print(f"\n--- {tlab} | {pass_lab} (n={len(sub)}) ---")
            print(f"  {'Variable':<22}{'deleg=1 mean':>14}{'deleg=0 mean':>14}{'diff':>10}{'t':>8}{'p':>8}")
            for col in cells + diff_cols:
                a = sub.loc[sub["delegation"]==1, col].dropna()
                b = sub.loc[sub["delegation"]==0, col].dropna()
                if len(a)<3 or len(b)<3: continue
                t,p = stats.ttest_ind(a,b,equal_var=False)
                print(f"  {col:<22}{a.mean():>14.3f}{b.mean():>14.3f}{a.mean()-b.mean():>10.3f}{t:>8.2f}{p:>8.3f}")


# ---------------------------------------------------------------------------
def analysis_3_between_subject():
    """Comment on line 81 (first): between-subject belief analysis."""
    banner("ANALYSIS 3: Between-subject — belief levels by treatment")

    d = load_delegator()
    cells = ["belief_del_good","belief_del_bad","belief_nodel_good","belief_nodel_bad",
             "nodel_del_good","nodel_del_bad"]
    print(f"\n  {'Variable':<22}{'Punish mean':>14}{'NoPun mean':>14}{'diff':>10}{'t':>8}{'p':>8}")
    for col in cells:
        a = d.loc[d["treat"]==0, col].dropna()
        b = d.loc[d["treat"]==1, col].dropna()
        t,p = stats.ttest_ind(a,b,equal_var=False)
        print(f"  {col:<22}{a.mean():>14.3f}{b.mean():>14.3f}{a.mean()-b.mean():>10.3f}{t:>8.2f}{p:>8.3f}")

    print("\n  Same restricted to PASSERS:")
    sub = d[d["pass_att2"]==1]
    print(f"  {'Variable':<22}{'Punish mean':>14}{'NoPun mean':>14}{'diff':>10}{'t':>8}{'p':>8}")
    for col in cells:
        a = sub.loc[sub["treat"]==0, col].dropna()
        b = sub.loc[sub["treat"]==1, col].dropna()
        t,p = stats.ttest_ind(a,b,equal_var=False)
        print(f"  {col:<22}{a.mean():>14.3f}{b.mean():>14.3f}{a.mean()-b.mean():>10.3f}{t:>8.2f}{p:>8.3f}")


# ---------------------------------------------------------------------------
def analysis_4_three_specs():
    """Comment on line 81 (second): three specs — beliefs only / +controls / passers."""
    banner("ANALYSIS 4: Logit of delegation on belief differences — three specs")

    d = load_delegator()
    SES = ["age","female","socio_status","went_to_uni","technology_score","leader"]

    sub = d[d["treat"]==0].copy()
    sub["bel_diff_bad"]  = sub["nodel_del_bad"]
    sub["bel_diff_good"] = sub["nodel_del_good"]

    # Spec 1: beliefs only, full PUNISHMENT sample
    s1 = sub[["delegation","bel_diff_bad","bel_diff_good"]].dropna()
    m1 = fit_logit(s1["delegation"], s1[["bel_diff_bad","bel_diff_good"]])

    # Spec 2: beliefs + controls (overall_score + SES), full PUNISHMENT sample
    cols2 = ["delegation","bel_diff_bad","bel_diff_good","overall_score"]+SES
    s2 = sub[cols2].dropna()
    m2 = fit_logit(s2["delegation"], s2[["bel_diff_bad","bel_diff_good","overall_score"]+SES])

    # Spec 3: same as 2 but PASSERS only
    s3 = sub[sub["pass_att2"]==1][cols2].dropna()
    m3 = fit_logit(s3["delegation"], s3[["bel_diff_bad","bel_diff_good","overall_score"]+SES])

    for label, m, n in [("Spec 1: beliefs only — full Punishment", m1, len(s1)),
                        ("Spec 2: beliefs + controls — full Punishment", m2, len(s2)),
                        ("Spec 3: beliefs + controls — PASSERS only", m3, len(s3))]:
        print(f"\n--- {label}  (N={n}, pseudo-R^2={m.prsquared:.3f}) ---")
        for v in ["bel_diff_bad","bel_diff_good"]:
            print("  " + fmt(m,v))


# ---------------------------------------------------------------------------
def analysis_5_weighted_and_average():
    """Comment on line 81 (fourth): weight by P(success), or take simple average."""
    banner("ANALYSIS 5: Weighted / averaged belief difference as single regressor")

    d = load_delegator()
    SES = ["age","female","socio_status","went_to_uni","technology_score","leader"]

    sub = d[d["treat"]==0].copy()
    # P(good) proxy: weighted-average self-confidence over 0..10 → /10
    sub["p_success"] = sub["wa_confidence"] / 10.0
    sub["bel_diff_bad"]  = sub["nodel_del_bad"]
    sub["bel_diff_good"] = sub["nodel_del_good"]

    sub["bel_diff_weighted"] = (sub["p_success"]*sub["bel_diff_good"]
                                + (1-sub["p_success"])*sub["bel_diff_bad"])
    sub["bel_diff_avg"] = 0.5*(sub["bel_diff_good"] + sub["bel_diff_bad"])

    print(f"\n  Distribution of single-regressor belief diffs (Punishment, full):")
    print(sub[["bel_diff_weighted","bel_diff_avg","p_success"]].describe().round(3))

    for sample_lab, sample_mask in [("Full Punishment", sub["treat"].notna()),
                                    ("Passers only", sub["pass_att2"]==1)]:
        s = sub.loc[sample_mask].copy()

        for reg_lab, reg in [("WEIGHTED (by P(good))", "bel_diff_weighted"),
                              ("AVERAGE (simple mean)", "bel_diff_avg")]:
            for ctrl_lab, ctrl in [("no controls", []),
                                    ("with controls", ["overall_score"]+SES)]:
                cols = ["delegation", reg] + ctrl
                ss = s[cols].dropna()
                if len(ss) < 15: continue
                m = fit_logit(ss["delegation"], ss[[reg]+ctrl])
                print(f"\n  --- {sample_lab} | {reg_lab} | {ctrl_lab}  (N={len(ss)}, pR2={m.prsquared:.3f}) ---")
                print("    " + fmt(m, reg))


# ---------------------------------------------------------------------------
def analysis_6_correlation():
    """Comment on line 81 (fifth): correlation between the two diff regressors."""
    banner("ANALYSIS 6: Are bel_diff_good and bel_diff_bad collinear?")

    d = load_delegator()
    sub = d[d["treat"]==0].copy()
    full = sub[["nodel_del_good","nodel_del_bad"]].dropna()
    pas  = sub.loc[sub["pass_att2"]==1, ["nodel_del_good","nodel_del_bad"]].dropna()

    for lab, x in [("Full Punishment", full),("Passers only", pas)]:
        r = x.corr().iloc[0,1]
        print(f"\n  {lab} (n={len(x)}): corr(bel_diff_good, bel_diff_bad) = {r:.3f}")
        # VIF: 1/(1-R^2)
        vif = 1/(1-r*r)
        print(f"    Implied VIF = {vif:.2f}  (>10 typically a concern)")


# ---------------------------------------------------------------------------
def analysis_7_pool_treatments():
    """Comment on line 85: use beliefs from BOTH treatments."""
    banner("ANALYSIS 7: Pool both treatments — beliefs interact with treatment?")

    d = load_delegator()
    SES = ["age","female","socio_status","went_to_uni","technology_score","leader"]

    df = d.copy()
    df["bel_diff_bad"]  = df["nodel_del_bad"]
    df["bel_diff_good"] = df["nodel_del_good"]
    df["bel_diff_avg"]  = 0.5*(df["bel_diff_good"] + df["bel_diff_bad"])
    df["pun"] = (df["treat"]==0).astype(int)
    df["bel_avg_x_pun"] = df["bel_diff_avg"]*df["pun"]
    df["bel_good_x_pun"] = df["bel_diff_good"]*df["pun"]
    df["bel_bad_x_pun"]  = df["bel_diff_bad"] *df["pun"]

    # Spec A: pooled, single avg regressor + treatment + interaction
    cols_a = ["delegation","pun","bel_diff_avg","bel_avg_x_pun","overall_score"]+SES
    sa = df[cols_a].dropna()
    ma = fit_logit(sa["delegation"], sa[["pun","bel_diff_avg","bel_avg_x_pun","overall_score"]+SES])

    # Spec B: pooled, both regressors + treatment + interactions
    cols_b = ["delegation","pun","bel_diff_bad","bel_diff_good",
              "bel_bad_x_pun","bel_good_x_pun","overall_score"]+SES
    sb = df[cols_b].dropna()
    mb = fit_logit(sb["delegation"],
                   sb[["pun","bel_diff_bad","bel_diff_good",
                       "bel_bad_x_pun","bel_good_x_pun","overall_score"]+SES])

    # Spec C: same as A but PASSERS only
    sc = df.loc[df["pass_att2"]==1, cols_a].dropna()
    mc = fit_logit(sc["delegation"], sc[["pun","bel_diff_avg","bel_avg_x_pun","overall_score"]+SES])

    for lab, m, n in [("Spec A: pooled, AVG diff x treat", ma, len(sa)),
                       ("Spec B: pooled, BOTH diffs x treat", mb, len(sb)),
                       ("Spec C: Spec A, PASSERS only", mc, len(sc))]:
        print(f"\n--- {lab}  (N={n}, pseudo-R^2={m.prsquared:.3f}) ---")
        for v in ["pun","bel_diff_avg","bel_avg_x_pun",
                  "bel_diff_bad","bel_diff_good","bel_bad_x_pun","bel_good_x_pun"]:
            line = fmt(m,v)
            if line: print("  " + line)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    analysis_1_realized_vs_anticipated()
    analysis_2_beliefs_vary_with_delegation()
    analysis_3_between_subject()
    analysis_4_three_specs()
    analysis_5_weighted_and_average()
    analysis_6_correlation()
    analysis_7_pool_treatments()
