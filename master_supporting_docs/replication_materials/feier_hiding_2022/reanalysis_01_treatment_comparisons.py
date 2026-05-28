"""
Treatment comparisons for Feier et al. (2022) data.

Compares the Human and Machine treatments on:
  1. Errors            -- actual count of mistakes on the logic task (0-10).
  2. Self-assessment   -- subjects' estimate of how many mistakes they made.
  3. Overconfidence    -- Error - Self_Assessment.

Self-assessment definition from the paper (p. 9):
  "participants were asked to assess their own performance by estimating
   how many mistakes they had made during the logic task."

So lower Self_Assessment = subject thinks they made few mistakes (= confident).
  Overconfidence = Error - Self_Assessment
    > 0  -> subject UNDER-estimated own errors  (overconfident)
    < 0  -> subject OVER-estimated own errors   (underconfident)
    = 0  -> perfectly calibrated.

Run:  python reanalysis_01_treatment_comparisons.py
"""

import os
import pandas as pd
from scipy import stats

# ---------------------------------------------------------------------------
# Load data (path relative to this script, so it runs from anywhere)
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(HERE, "data.csv"))

# Compute overconfidence: actual errors - self-assessed errors.
df["Overconfidence"] = df["Error"] - df["Self_Assessment"]

# Split by treatment.  Machine == 0 -> Human treatment, 1 -> Machine treatment.
human = df[df["Machine"] == 0]
machine = df[df["Machine"] == 1]

print(f"Sample: {len(df)} subjects "
      f"({len(human)} Human treatment, {len(machine)} Machine treatment)")
print("=" * 72)


def compare(varname, h_vals, m_vals):
    """Print summary statistics + parametric (t) and non-parametric (Mann-Whitney) tests."""
    h_mean, h_sd = h_vals.mean(), h_vals.std()
    m_mean, m_sd = m_vals.mean(), m_vals.std()
    t, p_t = stats.ttest_ind(h_vals, m_vals)
    u, p_u = stats.mannwhitneyu(h_vals, m_vals, alternative="two-sided")
    print(f"\n[{varname}]")
    print(f"  Human   : mean = {h_mean:6.3f}   SD = {h_sd:.3f}   n = {len(h_vals)}")
    print(f"  Machine : mean = {m_mean:6.3f}   SD = {m_sd:.3f}   n = {len(m_vals)}")
    print(f"  Difference (Machine - Human): {m_mean - h_mean:+6.3f}")
    print(f"  Independent-samples t-test  : t = {t:6.3f}   p = {p_t:.4f}")
    print(f"  Mann-Whitney U (two-sided)  : U = {u:6.0f}   p = {p_u:.4f}")


compare("1. Errors (actual count, 0-10)",
        human["Error"], machine["Error"])

compare("2. Self-assessment (estimated own errors, 0-10)",
        human["Self_Assessment"], machine["Self_Assessment"])

compare("3. Overconfidence (Error - Self_Assessment)",
        human["Overconfidence"], machine["Overconfidence"])

# ---------------------------------------------------------------------------
# Compact summary table at the end
# ---------------------------------------------------------------------------
print("\n" + "=" * 72)
print("Summary table")
print("=" * 72)


def t_str(h_vals, m_vals):
    t, p = stats.ttest_ind(h_vals, m_vals)
    return f"{t:+.3f} (p = {p:.3f})"


summary = pd.DataFrame({
    "Human (mean)":   [human["Error"].mean(),
                       human["Self_Assessment"].mean(),
                       human["Overconfidence"].mean()],
    "Machine (mean)": [machine["Error"].mean(),
                       machine["Self_Assessment"].mean(),
                       machine["Overconfidence"].mean()],
    "Difference":     [machine["Error"].mean() - human["Error"].mean(),
                       machine["Self_Assessment"].mean() - human["Self_Assessment"].mean(),
                       machine["Overconfidence"].mean() - human["Overconfidence"].mean()],
    "t-test (p)":     [t_str(human["Error"], machine["Error"]),
                       t_str(human["Self_Assessment"], machine["Self_Assessment"]),
                       t_str(human["Overconfidence"], machine["Overconfidence"])],
}, index=["Errors", "Self-assessment", "Overconfidence"]).round(3)

print(summary.to_string())
print()
