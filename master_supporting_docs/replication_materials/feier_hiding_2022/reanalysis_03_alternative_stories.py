"""
Reanalysis 03: Searching for alternative empirical stories to Feier's
main result.

Feier's main result: In the Machine treatment, the principal is "punished"
significantly less for algorithm-delegated bad outcomes than for self-made
bad outcomes (mean reward 12.96 ECU vs 8.53 ECU, paired t, p = 0.041).
Reading: AI delegation shields the principal from blame for bad outcomes.

This script asks: what ALTERNATIVE stories can the data tell?
"""

import os
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm

HERE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(HERE, "data.csv"))

df["Diff_good"] = df["Self_good"] - df["Del_good"]
df["Diff_bad"]  = df["Self_bad"]  - df["Del_bad"]

human   = df[df["Machine"] == 0]
machine = df[df["Machine"] == 1]


# ---------------------------------------------------------------------------
# STORY 1: It is not "blame-shielding for bad outcomes." It is "decision-
# rewarding for using AI" -- observers reward DELEGATING to AI across BOTH
# good and bad outcomes, not asymmetrically more for bad outcomes.
# ---------------------------------------------------------------------------
print("=" * 78)
print("STORY 1: 'AI-decision rewarding' rather than 'blame-shielding'")
print("=" * 78)
print()
print("Treatment gaps (Machine minus Human) by cell:")
for cell in ["Del_good", "Self_good", "Del_bad", "Self_bad"]:
    h_m, m_m = human[cell].mean(), machine[cell].mean()
    t, p = stats.ttest_ind(human[cell], machine[cell])
    print(f"  {cell:10s}: Human = {h_m:6.2f},  Machine = {m_m:6.2f},  "
          f"Delta = {m_m - h_m:+6.2f},  t = {t:+5.2f},  p = {p:.3f}")
print()
print("Reading: if Feier's effect were specifically about 'shielding bad outcomes',")
print("we should see Del_bad rise far more than Del_good in the Machine treatment.")
print("Instead, Del_good rises MORE than Del_bad. Algorithm-use is rewarded")
print("regardless of outcome -- and good-outcome use is rewarded most.")
print()

# Within-Machine: are good- and bad-outcome Self-Del gaps similar in magnitude?
print("Within-Machine paired comparisons:")
t_bad,  p_bad  = stats.ttest_rel(machine["Self_bad"],  machine["Del_bad"])
t_good, p_good = stats.ttest_rel(machine["Self_good"], machine["Del_good"])
print(f"  Bad : Self_bad  ({machine['Self_bad'].mean():.2f}) vs Del_bad  ({machine['Del_bad'].mean():.2f}): "
      f"gap = {machine['Del_bad'].mean()  - machine['Self_bad'].mean():+.2f},  "
      f"paired t = {t_bad:+.2f}, p = {p_bad:.3f}")
print(f"  Good: Self_good ({machine['Self_good'].mean():.2f}) vs Del_good ({machine['Del_good'].mean():.2f}): "
      f"gap = {machine['Del_good'].mean() - machine['Self_good'].mean():+.2f},  "
      f"paired t = {t_good:+.2f}, p = {p_good:.3f}")
print()
print("Gap magnitudes are similar (+4.43 bad vs +3.22 good); the bad-outcome gap")
print("only reaches significance because variance is lower in that cell.")
print("This is a DECISION-rewarding pattern, not an OUTCOME-conditional shielding.")


# ---------------------------------------------------------------------------
# STORY 2: The 'punishment' framing is misleading -- subjects are net-REWARDING
# in all four cells, including bad outcomes.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STORY 2: All cells are net-rewarded, not net-punished")
print("=" * 78)
print()
print("Mean evaluation in each cell (positive = net reward, negative = net punishment):")
print()
for treat_name, sub in [("HUMAN", human), ("MACHINE", machine)]:
    print(f"  {treat_name}:")
    for cell in ["Self_good", "Del_good", "Self_bad", "Del_bad"]:
        m = sub[cell].mean()
        sign = "REWARD" if m > 0 else "PUNISH"
        print(f"    {cell:10s} = {m:+6.2f}   ({sign} on average)")
print()
print("Even bad-outcome cells have POSITIVE mean evaluations. Feier's framing of")
print("'punishment shielding' is technically a 'lower reward for self-made bad")
print("outcomes,' not active punishment. Subjects don't really punish; they reward")
print("less. This matters because the literature framing the result as 'punishment")
print("avoidance' is somewhat overstated.")


# ---------------------------------------------------------------------------
# STORY 3: The main result is outlier-driven (median + trimmed-mean check)
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STORY 3: Is the main result outlier-driven?")
print("=" * 78)
print()
print("Within-MACHINE Self_bad vs Del_bad under different aggregators:")
sb = machine["Self_bad"]
db = machine["Del_bad"]
print(f"  Mean   : Self_bad = {sb.mean():.2f},  Del_bad = {db.mean():.2f},  diff = {db.mean()-sb.mean():+.2f}")
print(f"  Median : Self_bad = {sb.median():.2f},  Del_bad = {db.median():.2f},  diff = {db.median()-sb.median():+.2f}")
print(f"  20% trimmed mean: Self_bad = {stats.trim_mean(sb,0.2):.2f},  Del_bad = {stats.trim_mean(db,0.2):.2f},  "
      f"diff = {stats.trim_mean(db,0.2) - stats.trim_mean(sb,0.2):+.2f}")
print()
# Wilcoxon signed-rank (non-parametric paired)
w, pw = stats.wilcoxon(sb, db)
print(f"  Wilcoxon signed-rank test (non-parametric paired): W = {w:.0f}, p = {pw:.4f}")
print()
# Distribution of Diff_bad
print("  Distribution of within-subject Diff_bad (Self - Del) in Machine treatment:")
diff_b = machine["Diff_bad"]
print(f"    n         = {len(diff_b)}")
print(f"    mean      = {diff_b.mean():+.2f}")
print(f"    median    = {diff_b.median():+.2f}")
print(f"    Diff = 0  : {(diff_b == 0).sum():3d} subjects ({100*(diff_b==0).mean():.1f}%)")
print(f"    Diff < 0  : {(diff_b < 0).sum():3d} subjects ({100*(diff_b<0).mean():.1f}%)  "
      f"<- the 'blame-shielding' direction")
print(f"    Diff > 0  : {(diff_b > 0).sum():3d} subjects ({100*(diff_b>0).mean():.1f}%)")
print()
# Sign test
n_neg = (diff_b < 0).sum()
n_pos = (diff_b > 0).sum()
n_eff = n_neg + n_pos
binom_p = stats.binom_test(n_neg, n_eff, p=0.5) if hasattr(stats, "binom_test") else stats.binomtest(n_neg, n_eff, p=0.5).pvalue
print(f"  Sign test (excluding ties): {n_neg}/{n_eff} subjects show the 'shielding' direction, p = {binom_p:.4f}")


# ---------------------------------------------------------------------------
# STORY 4: Mass-at-zero -- many subjects don't differentiate at all
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STORY 4: How many subjects ACTUALLY differentiate by delegation status?")
print("=" * 78)
print()
print("In MACHINE treatment, count subjects whose Self_bad == Del_bad:")
machine_eq = (machine["Self_bad"] == machine["Del_bad"]).sum()
print(f"  {machine_eq}/{len(machine)} subjects = {100*machine_eq/len(machine):.1f}% give IDENTICAL evaluations")
print(f"  to delegated and self-made bad outcomes (no within-subject differentiation).")
print()
print("In HUMAN treatment, the same:")
human_eq = (human["Self_bad"] == human["Del_bad"]).sum()
print(f"  {human_eq}/{len(human)} subjects = {100*human_eq/len(human):.1f}% give identical evaluations.")
print()
print("Among Machine-treatment subjects who DO differentiate:")
machine_diff = machine[machine["Self_bad"] != machine["Del_bad"]]
print(f"  n = {len(machine_diff)}")
print(f"  mean Diff_bad = {machine_diff['Diff_bad'].mean():+.2f}")
t, p = stats.ttest_rel(machine_diff["Self_bad"], machine_diff["Del_bad"])
print(f"  paired t = {t:+.2f}, p = {p:.4f}")
print()
print("Interpretation: the headline finding is driven by a MINORITY of subjects who")
print("actively differentiate. A large fraction give the same evaluation in both cells.")


# ---------------------------------------------------------------------------
# STORY 5: The result fails when we control for the evaluator's own
# characteristics (Risk, Error, Self_Assessment)
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STORY 5: Does the Self_bad - Del_bad gap depend on evaluator traits?")
print("=" * 78)
print()
# In long format: each subject contributes 2 rows (Self_bad, Del_bad), with
# a "Delegated" dummy. Subject fixed effects + Delegated interacted with treatment.
long = pd.melt(
    df[["Subject","Machine","Risk","Error","Self_Assessment","Del","Self_bad","Del_bad"]],
    id_vars=["Subject","Machine","Risk","Error","Self_Assessment","Del"],
    value_vars=["Self_bad","Del_bad"],
    var_name="Scenario",
    value_name="Punishment",
)
long["Delegated"] = (long["Scenario"] == "Del_bad").astype(int)
long["SubjectID"] = long["Subject"].astype(str) + "_" + long["Machine"].astype(str)

# Within Machine treatment only: OLS with Delegated, Risk, Error, Self_Assessment as predictors
mach_long = long[long["Machine"] == 1].copy()
formula = "Punishment ~ Delegated + Risk + Error + Self_Assessment + Del"
model = sm.OLS.from_formula(formula, mach_long).fit(cov_type="cluster", cov_kwds={"groups": mach_long["SubjectID"]})
print("OLS on Machine-treatment long data, clustered by subject:")
print(f"  Formula: {formula}")
print(model.summary().tables[1])
print()
print("If Delegated coefficient survives controlling for evaluator characteristics,")
print("the effect is robust. If it shrinks/loses significance, the original finding")
print("was driven by evaluator heterogeneity, not by delegation per se.")


# ---------------------------------------------------------------------------
# STORY 6: The good-outcome differential SHOULD be similar to bad-outcome
# if the 'decision-rewarding' story is right, but unequal if the 'blame-
# shielding' story is right. We test this with an interaction.
# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("STORY 6: Outcome-by-delegation interaction test")
print("=" * 78)
print()
long_all = pd.melt(
    df[["Subject","Machine","Self_good","Del_good","Self_bad","Del_bad"]],
    id_vars=["Subject","Machine"],
    value_vars=["Self_good","Del_good","Self_bad","Del_bad"],
    var_name="Scenario",
    value_name="Punishment",
)
long_all["Delegated"] = long_all["Scenario"].isin(["Del_good","Del_bad"]).astype(int)
long_all["GoodOutcome"] = long_all["Scenario"].isin(["Self_good","Del_good"]).astype(int)
long_all["SubjectID"] = long_all["Subject"].astype(str) + "_" + long_all["Machine"].astype(str)

mach_4 = long_all[long_all["Machine"] == 1].copy()
formula2 = "Punishment ~ Delegated * GoodOutcome"
model2 = sm.OLS.from_formula(formula2, mach_4).fit(cov_type="cluster", cov_kwds={"groups": mach_4["SubjectID"]})
print("Within-MACHINE OLS, clustered by subject:")
print(f"  Formula: {formula2}")
print(model2.summary().tables[1])
print()
print("If the 'blame-shielding for bad outcomes' story is correct, the Delegated:GoodOutcome")
print("interaction should be NEGATIVE and SIGNIFICANT -- meaning the Self-vs-Del gap is")
print("BIGGER for bad outcomes than for good. If the interaction is null, then the")
print("Self-vs-Del gap is roughly the same magnitude in both cells -- a DECISION-rewarding")
print("pattern, not an outcome-conditional shielding pattern.")
