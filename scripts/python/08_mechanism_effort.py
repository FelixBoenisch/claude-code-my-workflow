"""Mechanism analysis (M2 / effort): non-delegators in No-Punishment vs Punishment.

Records the headline numbers for §sec:mechanism (45.5% vs 21.7% etc.).
"""
import numpy as np
from scipy import stats

from lib.io import load_delegator
from lib import manifest


def main() -> None:
    d = load_delegator()
    nondeleg = d[d["delegation"] == 0].copy()

    rates = nondeleg.groupby("treat")["success_last"].agg(["mean", "count"]).to_dict("index")
    perf_means = nondeleg.groupby("treat")["overall_score"].mean().to_dict()

    pun = nondeleg[nondeleg["treat"] == 0]["success_last"]
    nopun = nondeleg[nondeleg["treat"] == 1]["success_last"]
    _, p_succ = stats.ttest_ind(nopun.dropna(), pun.dropna(), equal_var=False)

    pun_perf = nondeleg[nondeleg["treat"] == 0]["overall_score"]
    nopun_perf = nondeleg[nondeleg["treat"] == 1]["overall_score"]
    _, p_perf = stats.ttest_ind(nopun_perf, pun_perf, equal_var=False)

    out = {
        "nondeleg_punishment_n": int(rates[0]["count"]),
        "nondeleg_no_punishment_n": int(rates[1]["count"]),
        "nondeleg_punishment_success_rate_pct": round(100 * float(rates[0]["mean"]), 1),
        "nondeleg_no_punishment_success_rate_pct": round(100 * float(rates[1]["mean"]), 1),
        "nondeleg_success_p": round(float(p_succ), 4),
        "nondeleg_punishment_overall_score_mean": round(float(perf_means[0]), 2),
        "nondeleg_no_punishment_overall_score_mean": round(float(perf_means[1]), 2),
        "nondeleg_overall_score_p": round(float(p_perf), 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
