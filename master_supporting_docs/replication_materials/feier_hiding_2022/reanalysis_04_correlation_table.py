"""
Reanalysis 04: Correlation table for the dual-role analysis.

Variables included:
  Error           - actual number of mistakes on the logic task (0-10).
  Self_Assess     - subject's estimate of own mistakes (0-10).
  Del             - subject's OWN delegation choice (0 = no, 1 = yes).
  R(Del,good)     - evaluation given to delegated GOOD outcome  (range -40..+40).
  R(Self,good)    - evaluation given to self-made GOOD outcome.
  R(Del,bad)      - evaluation given to delegated BAD outcome.
  R(Self,bad)     - evaluation given to self-made BAD outcome.
  Diff_good       - R(Self,good) - R(Del,good)  (within-subject good-outcome diff).
  Diff_bad        - R(Self,bad)  - R(Del,bad)   (within-subject bad-outcome diff).

Pearson correlations with two-sided p-values.  Significance stars:
  *** p < 0.01
  **  p < 0.05
  *   p < 0.10

Sign convention: higher Error / Self_Assess = worse / lower self-perceived
performance.  Higher R(.,.) = more reward (less punishment).
"""

import os
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(HERE, "data.csv"))

df["Diff_good"] = df["Self_good"] - df["Del_good"]
df["Diff_bad"]  = df["Self_bad"]  - df["Del_bad"]

# Display labels (kept short so the table fits a terminal)
LABELS = {
    "Error":           "Error",
    "Self_Assessment": "SelfAss",
    "Del":             "Del",
    "Del_good":        "R(D,g)",
    "Self_good":       "R(S,g)",
    "Del_bad":         "R(D,b)",
    "Self_bad":        "R(S,b)",
    "Diff_good":       "Diff_g",
    "Diff_bad":        "Diff_b",
}
VARS = list(LABELS.keys())


def star(p):
    if p < 0.01:
        return "***"
    if p < 0.05:
        return "** "
    if p < 0.10:
        return "*  "
    return "   "


def corr_table(sub, label):
    print(f"\n=== {label}  (n = {len(sub)}) ===\n")
    rows = []
    for i, vi in enumerate(VARS):
        row = []
        for j, vj in enumerate(VARS):
            if j > i:
                row.append("")
            elif i == j:
                row.append("  1.000   ")
            else:
                r, p = stats.pearsonr(sub[vi], sub[vj])
                row.append(f"{r:+.3f}{star(p)}")
        rows.append(row)
    out = pd.DataFrame(rows,
                       columns=[LABELS[v] for v in VARS],
                       index=[LABELS[v] for v in VARS])
    print(out.to_string())


print("Pearson correlations.  Significance: *** p<0.01, ** p<0.05, * p<0.10")
print()
print("Variable key:")
print("  Error    = actual errors on logic task (0-10; higher = worse)")
print("  SelfAss  = self-assessed errors (0-10; higher = thinks did worse)")
print("  Del      = subject's own delegation choice (0 = no, 1 = yes)")
print("  R(D,g)   = reward to delegated good outcome")
print("  R(S,g)   = reward to self-made good outcome")
print("  R(D,b)   = reward to delegated bad outcome")
print("  R(S,b)   = reward to self-made bad outcome")
print("  Diff_g   = R(S,g) - R(D,g)  (positive = favors self-made for good)")
print("  Diff_b   = R(S,b) - R(D,b)  (negative = blame-shielding direction)")

corr_table(df,                          "FULL SAMPLE")
corr_table(df[df["Machine"] == 0],      "HUMAN treatment")
corr_table(df[df["Machine"] == 1],      "MACHINE treatment")
