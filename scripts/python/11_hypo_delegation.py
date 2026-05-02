"""H1 within-subject corroborator: the delegation_hypo question.

In the No-Punishment condition, after the actual delegation decision was made,
Player As were asked the hypothetical "would you have delegated if punishment
had been possible?" If H1's direction is real (punishment reduces delegation),
the hypothetical answer should be lower than the actual No-Punishment delegation
rate.

Comparison:
  Punishment condition actual delegation rate (between-subject)
  No-Punishment hypothetical "if you could be punished" delegation rate (within)
  No-Punishment actual delegation rate (between-subject)
"""
from __future__ import annotations

import numpy as np
from scipy import stats

from lib.io import load_delegator
from lib import manifest


def main() -> None:
    d = load_delegator()
    pun_actual_rate = float(d.loc[d["treat"] == 0, "delegation"].mean())
    nopun_actual_rate = float(d.loc[d["treat"] == 1, "delegation"].mean())
    nopun_hypo_rate = float(d.loc[d["treat"] == 1, "delegation_hypo"].mean())
    nopun_hypo_n = int(d.loc[d["treat"] == 1, "delegation_hypo"].notna().sum())

    # Within-subject paired test on No-Punishment subjects: actual vs hypothetical
    sub = d.loc[d["treat"] == 1, ["delegation", "delegation_hypo"]].dropna()
    n_pairs = len(sub)
    diffs = sub["delegation"] - sub["delegation_hypo"]
    n_changed = int((diffs != 0).sum())
    n_actual_to_hypo_drop = int((diffs > 0).sum())  # actual=1, hypo=0 (would not delegate if punishment)
    n_actual_to_hypo_rise = int((diffs < 0).sum())  # actual=0, hypo=1 (would delegate if punishment)
    # McNemar's test on the change
    if n_changed > 0:
        mcnemar_stat = (n_actual_to_hypo_drop - n_actual_to_hypo_rise) ** 2 / max(n_changed, 1)
        from scipy.stats import chi2 as chi2_dist
        p_mcnemar = float(1 - chi2_dist.cdf(mcnemar_stat, df=1))
    else:
        mcnemar_stat = float("nan")
        p_mcnemar = float("nan")

    # Compare hypothetical rate to actual Punishment rate (between-subject)
    hypo_responses = d.loc[d["treat"] == 1, "delegation_hypo"].dropna().astype(int)
    pun_actual = d.loc[d["treat"] == 0, "delegation"].astype(int)
    table = np.array([
        [int(pun_actual.sum()), int((1 - pun_actual).sum())],
        [int(hypo_responses.sum()), int((1 - hypo_responses).sum()),],
    ])
    chi2, p_chi2_hypo, _, _ = stats.chi2_contingency(table, correction=False)

    out = {
        "hypo_pun_actual_rate_pct": round(100 * pun_actual_rate, 1),
        "hypo_nopun_hypo_rate_pct": round(100 * nopun_hypo_rate, 1),
        "hypo_nopun_actual_rate_pct": round(100 * nopun_actual_rate, 1),
        "hypo_nopun_hypo_n": nopun_hypo_n,
        "hypo_n_pairs_within": n_pairs,
        "hypo_within_n_changed": n_changed,
        "hypo_within_n_dropped": n_actual_to_hypo_drop,
        "hypo_within_n_added": n_actual_to_hypo_rise,
        "hypo_within_mcnemar_p": round(p_mcnemar, 4) if not np.isnan(p_mcnemar) else None,
        "hypo_actual_punishment_vs_nopun_hypo_chi2_p": round(float(p_chi2_hypo), 4),
        "hypo_within_actual_minus_hypo_pp": round(100 * (nopun_actual_rate - nopun_hypo_rate), 1),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
