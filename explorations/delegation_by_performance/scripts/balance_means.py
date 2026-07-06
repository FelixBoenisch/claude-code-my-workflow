import sys

from scipy import stats

sys.path.insert(0, r"c:\Users\USER\Documents\Test environment\paper\scripts\python")
from lib.io import load_delegator

d = load_delegator()
for label, df in [("full", d), ("passers", d[d["pass_att2"] == 1])]:
    p = df[df["treat"] == 0]["overall_score"]
    n = df[df["treat"] == 1]["overall_score"]
    _, pv = stats.ttest_ind(p, n)
    _, pu = stats.mannwhitneyu(p, n)
    print(
        f"{label}: Punishment {p.mean():.3f} (n={len(p)}) | "
        f"No-Punishment {n.mean():.3f} (n={len(n)}) | "
        f"pooled {df['overall_score'].mean():.3f} | "
        f"t-test p={pv:.3f} | Mann-Whitney p={pu:.3f}"
    )
