"""Exploratory: delegation rates by performance group x condition.

Question: do LOW performers delegate MORE under Punishment than under
No-Punishment (failure-avoidance variant of process ownership), or does the
treatment gap come from mid/high performers withholding delegation
(success-ownership variant)?
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, r"c:\Users\USER\Documents\Test environment\paper\scripts\python")
from lib.io import load_delegator

d = load_delegator()

TREAT = {0: "Punishment", 1: "No-Punishment"}


def groups(df, label):
    print(f"\n=== {label} (n={len(df)}) ===")
    print("score distribution:", df["overall_score"].value_counts().sort_index().to_dict())

    # Discrete score -> approximate terciles: 0-2 / 3 / 4-10
    # plus a robustness split at the median (<=2 vs >=3)
    for name, cut in [
        ("terciles 0-2 | 3 | 4+", [(-1, 2), (3, 3), (4, 10)]),
        ("median split <=2 | >=3", [(-1, 2), (3, 10)]),
        ("finer: 0-1 | 2 | 3 | 4+", [(-1, 1), (2, 2), (3, 3), (4, 10)]),
    ]:
        print(f"\n--- {name} ---")
        rows = []
        for lo, hi in cut:
            g = df[(df["overall_score"] >= lo) & (df["overall_score"] <= hi)]
            row = {"bin": f"[{max(lo,0)},{hi}]"}
            for tv in (0, 1):
                sub = g[g["treat"] == tv]
                row[f"n_{TREAT[tv][:5]}"] = len(sub)
                row[f"del_{TREAT[tv][:5]}"] = round(sub["delegation"].mean(), 3) if len(sub) else np.nan
            # Fisher exact within bin: Punishment vs No-Punishment
            tab = pd.crosstab(g["treat"], g["delegation"])
            if tab.shape == (2, 2):
                row["fisher_p"] = round(stats.fisher_exact(tab)[1], 3)
            rows.append(row)
        print(pd.DataFrame(rows).to_string(index=False))

    # Interaction test: logit delegation ~ treat * score
    import statsmodels.api as sm
    X = pd.DataFrame({
        "const": 1.0,
        "nopun": df["treat"],
        "score": df["overall_score"],
        "nopun_x_score": df["treat"] * df["overall_score"],
    })
    m = sm.Logit(df["delegation"], X).fit(disp=0)
    print("\nLogit delegation ~ nopun * score:")
    print(pd.DataFrame({"coef": m.params.round(3), "p": m.pvalues.round(3)}).to_string())

    # Slope within each condition (Pearson r, score vs delegation)
    for tv in (0, 1):
        sub = df[df["treat"] == tv]
        r, p = stats.pearsonr(sub["overall_score"], sub["delegation"])
        print(f"corr(score, delegation) in {TREAT[tv]}: r={r:.3f}, p={p:.3f}")


groups(d, "FULL SAMPLE")
groups(d[d["pass_att2"] == 1], "ATTENTION-CHECK PASSERS")
