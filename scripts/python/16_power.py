"""Power calculations: H1 ex-ante MDE; H2 paired-t MDE; TOST equivalence.

H1 (between-subject chi-squared): given n=80/cell, what is the minimum
detectable difference in delegation rates at 80% power and alpha=0.05?

H2 (within-subject paired-t on bad-outcome cell): given n=67 attention-pass
Player Bs and the observed within-subject SD of (punish_nodel_bad -
punish_del_bad), what is the minimum detectable mean difference?

TOST: two one-sided tests for equivalence, with bound +/- chosen as the
practical-significance threshold. We use 0.20 (£0.20 = 10% of the £2 max
punishment) as the bound.
"""
from __future__ import annotations

import numpy as np
from scipy import stats
from statsmodels.stats.power import NormalIndPower, TTestPower

from lib.io import load_delegator, load_evaluator
from lib import manifest


def h1_mde(n_per_cell: int = 80, alpha: float = 0.05, power: float = 0.80,
           baseline_rate: float = 0.50) -> float:
    """Approximate MDE in proportion difference for two-sample chi-squared."""
    pwr = NormalIndPower()
    cohens_h = pwr.solve_power(effect_size=None, nobs1=n_per_cell, alpha=alpha,
                                power=power, ratio=1.0, alternative="two-sided")
    p1 = baseline_rate
    h = cohens_h
    p2 = (np.sin(np.arcsin(np.sqrt(p1)) + h / 2) ** 2)
    return abs(p2 - p1) * 2


def h2_mde_paired(sd_diff: float, n: int, alpha: float = 0.05, power: float = 0.80) -> float:
    pwr = TTestPower()
    es = pwr.solve_power(effect_size=None, nobs=n, alpha=alpha, power=power, alternative="two-sided")
    return float(es * sd_diff)


def tost(diffs, low: float, high: float, alpha: float = 0.05) -> tuple[float, float, bool]:
    """Two one-sided tests for equivalence of mean(diffs) within [low, high]."""
    n = len(diffs)
    mean = float(np.mean(diffs))
    sd = float(np.std(diffs, ddof=1))
    se = sd / np.sqrt(n)
    t_low = (mean - low) / se
    t_high = (mean - high) / se
    p_low = 1 - stats.t.cdf(t_low, df=n - 1)
    p_high = stats.t.cdf(t_high, df=n - 1)
    p_max = max(p_low, p_high)
    is_equivalent = p_max < alpha
    return float(p_low), float(p_high), is_equivalent


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    # H1 MDE
    h1_actual_diff = float(d.loc[d["treat"] == 1, "delegation"].mean() -
                            d.loc[d["treat"] == 0, "delegation"].mean())
    h1_mde_pp = h1_mde(n_per_cell=80, baseline_rate=0.50)

    # H2 MDE on bad-outcome cell
    pun = e[(e["treat"] == 0) & (e["pass_att2"] == 1)].copy()
    diff_bad = (pun["punish_nodel_bad"] - pun["punish_del_bad"]).dropna()
    diff_good = (pun["punish_nodel_good"] - pun["punish_del_good"]).dropna()

    sd_bad = float(diff_bad.std(ddof=1))
    sd_good = float(diff_good.std(ddof=1))
    n_pun = len(pun)

    h2_mde_bad = h2_mde_paired(sd_bad, n_pun)
    h2_mde_good = h2_mde_paired(sd_good, n_pun)

    # TOST with bound +/- 0.20 (10% of max punishment)
    p_low_bad, p_high_bad, eq_bad = tost(diff_bad.values, low=-0.20, high=0.20)
    p_low_good, p_high_good, eq_good = tost(diff_good.values, low=-0.20, high=0.20)

    # Tighter TOST bound: +/- 0.10
    p_low_bad_10, p_high_bad_10, eq_bad_10 = tost(diff_bad.values, low=-0.10, high=0.10)

    out = {
        "h1_actual_diff_pp": round(100 * h1_actual_diff, 1),
        "h1_mde_pp_at_80pct_power": round(100 * h1_mde_pp, 1),
        "h2_n": n_pun,
        "h2_diff_bad_mean": round(float(diff_bad.mean()), 4),
        "h2_diff_bad_sd": round(sd_bad, 4),
        "h2_mde_bad_at_80pct_power": round(h2_mde_bad, 4),
        "h2_diff_good_mean": round(float(diff_good.mean()), 4),
        "h2_diff_good_sd": round(sd_good, 4),
        "h2_mde_good_at_80pct_power": round(h2_mde_good, 4),
        "tost_bad_bound_0p20_p": round(max(p_low_bad, p_high_bad), 4),
        "tost_bad_bound_0p20_equivalent": bool(eq_bad),
        "tost_good_bound_0p20_p": round(max(p_low_good, p_high_good), 4),
        "tost_good_bound_0p20_equivalent": bool(eq_good),
        "tost_bad_bound_0p10_p": round(max(p_low_bad_10, p_high_bad_10), 4),
        "tost_bad_bound_0p10_equivalent": bool(eq_bad_10),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
