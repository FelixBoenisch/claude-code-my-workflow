"""
Reanalysis 02: Delegator-evaluator dual-role link in Feier et al. (2022).

Each subject acts as both delegator (their own Del choice) and evaluator
(strategy-method punishment/reward for the four (delegation, outcome) cells).
This raises the concern that evaluator-role behaviour is biased by the
subject's own delegation choice -- e.g. via self-justification ("I delegated,
so I should not punish other delegators") or hypocrisy aversion ("if I would
not have delegated, I should punish delegators").

This script tests:
  (1) Do delegators give different evaluations in each of the four scenarios?
  (2) Do delegators show different within-subject differentials Self - Del?
  (3) Do the patterns differ by treatment (Human vs Machine)?

Sign convention: punishment/reward range is -40 to 40 in the strategy method.
  Positive  = reward
  Negative  = punishment

For the within-subject differential Diff_bad = Self_bad - Del_bad:
  > 0  -> subject treats SELF-made bad outcomes more GENEROUSLY than delegated
  < 0  -> subject punishes SELF-made bad outcomes MORE than delegated
  = 0  -> no within-subject differentiation
The Feier headline (in the Machine treatment) is that the AVERAGE Diff_bad < 0.

Run:  python reanalysis_02_delegator_evaluator_link.py
"""

import os
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(HERE, "data.csv"))

# Within-subject differentials (Self minus Del)
df["Diff_good"] = df["Self_good"] - df["Del_good"]
df["Diff_bad"] = df["Self_bad"] - df["Del_bad"]

n_del = (df["Del"] == 1).sum()
n_nodel = (df["Del"] == 0).sum()
print(f"Sample: {len(df)} subjects ({n_nodel} non-delegators, {n_del} delegators)")
print("=" * 78)


def cmp(label, var, sub=df):
    """Print mean of `var` by Del status, with t-test and Mann-Whitney."""
    d = sub[sub["Del"] == 1][var]
    n = sub[sub["Del"] == 0][var]
    if len(d) < 2 or len(n) < 2:
        print(f"  [{label}] -- skipped (too few obs in one group)")
        return
    t, pt = stats.ttest_ind(d, n)
    u, pu = stats.mannwhitneyu(d, n, alternative="two-sided")
    print(f"\n[{label}]")
    print(f"  Delegators   (Del=1) : mean = {d.mean():+7.3f}   n = {len(d)}")
    print(f"  Non-delegators (Del=0): mean = {n.mean():+7.3f}   n = {len(n)}")
    print(f"  Diff (Del=1 - Del=0)  : {d.mean() - n.mean():+7.3f}")
    print(f"  t-test  : t = {t:+.3f}   p = {pt:.4f}")
    print(f"  M-W U   : U = {u:.0f}     p = {pu:.4f}")


# ---------------------------------------------------------------------------
# Pooled (all 149 subjects)
# ---------------------------------------------------------------------------
print("\nPOOLED (all 149 subjects)")
print("-" * 78)
print("\n--- Raw evaluations in the four scenarios ---")
cmp("Del_good  -- reward for delegated good outcome",  "Del_good")
cmp("Self_good -- reward for self-made good outcome",  "Self_good")
cmp("Del_bad   -- reward/punishment for delegated bad outcome",  "Del_bad")
cmp("Self_bad  -- reward/punishment for self-made bad outcome",  "Self_bad")

print("\n--- Within-subject differentials Self - Del ---")
cmp("Diff_good = Self_good - Del_good",  "Diff_good")
cmp("Diff_bad  = Self_bad - Del_bad",    "Diff_bad")


# ---------------------------------------------------------------------------
# By treatment
# ---------------------------------------------------------------------------
for treat_val, treat_name in [(0, "HUMAN"), (1, "MACHINE")]:
    sub = df[df["Machine"] == treat_val]
    sub_d = (sub["Del"] == 1).sum()
    sub_n = (sub["Del"] == 0).sum()
    print("\n" + "=" * 78)
    print(f"{treat_name} TREATMENT  (n = {len(sub)}: {sub_n} non-delegators, {sub_d} delegators)")
    print("=" * 78)
    print("\n--- Raw evaluations ---")
    cmp("Del_good",  "Del_good",  sub=sub)
    cmp("Self_good", "Self_good", sub=sub)
    cmp("Del_bad",   "Del_bad",   sub=sub)
    cmp("Self_bad",  "Self_bad",  sub=sub)
    print("\n--- Within-subject differentials ---")
    cmp("Diff_good", "Diff_good", sub=sub)
    cmp("Diff_bad",  "Diff_bad",  sub=sub)


# ---------------------------------------------------------------------------
# Compact summary table
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("Summary table -- means by delegator status, pooled and by treatment")
print("=" * 78)


def row(label, sub):
    d_evs = sub[sub["Del"] == 1]
    n_evs = sub[sub["Del"] == 0]
    return {
        "n (del / nodel)": f"{len(d_evs)}/{len(n_evs)}",
        "Del_good":  f"{d_evs['Del_good'].mean():+.2f} / {n_evs['Del_good'].mean():+.2f}",
        "Self_good": f"{d_evs['Self_good'].mean():+.2f} / {n_evs['Self_good'].mean():+.2f}",
        "Del_bad":   f"{d_evs['Del_bad'].mean():+.2f} / {n_evs['Del_bad'].mean():+.2f}",
        "Self_bad":  f"{d_evs['Self_bad'].mean():+.2f} / {n_evs['Self_bad'].mean():+.2f}",
        "Diff_bad":  f"{d_evs['Diff_bad'].mean():+.2f} / {n_evs['Diff_bad'].mean():+.2f}",
    }


tbl = pd.DataFrame({
    "Pooled":  row("pooled",  df),
    "Human":   row("Human",   df[df["Machine"] == 0]),
    "Machine": row("Machine", df[df["Machine"] == 1]),
}).T
print(tbl.to_string())
print()
print("Each cell: delegators-mean / non-delegators-mean.")
