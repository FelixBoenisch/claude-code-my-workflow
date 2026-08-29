"""Mechanism analysis (M2 / effort) among non-delegating Player As.

The default Player-A loader applies the manuscript sample restriction. This
script produces the outcome, prediction-error, and screen-time statistics used
in the effort discussion.
"""
import numpy as np
import pandas as pd
from scipy import stats

from lib.io import load_delegator
from lib import manifest
from lib.paths import DELEGATOR_PAGETIMES


def _welch_p(x: pd.Series, y: pd.Series) -> float:
    """Two-sided Welch unequal-variance t-test."""
    return float(stats.ttest_ind(x.dropna(), y.dropna(), equal_var=False).pvalue)


def _mwu_p(x: pd.Series, y: pd.Series) -> float:
    """Two-sided Mann-Whitney rank-sum test."""
    return float(stats.mannwhitneyu(x.dropna(), y.dropna(), alternative="two-sided").pvalue)


def main() -> None:
    d = load_delegator()
    nondeleg = d[d["delegation"] == 0].copy()

    # Positive values mean that absolute prediction error fell on the final
    # prediction relative to the subject's mean error in rounds 1--10.
    initial_errors = pd.concat(
        [
            (nondeleg[f"guess_r{r}"] - nondeleg[f"truth_r{r}"]).abs()
            for r in range(1, 11)
        ],
        axis=1,
    )
    nondeleg["initial_abs_error"] = initial_errors.mean(axis=1)
    nondeleg["final_abs_error"] = (nondeleg["guess_last"] - nondeleg["truth_last"]).abs()
    nondeleg["abs_error_improvement"] = (
        nondeleg["initial_abs_error"] - nondeleg["final_abs_error"]
    )

    # Page timestamps are Unix seconds. Retaining only the timestamp fields and
    # merging the cleaned analysis sample ensures the same exclusion and the
    # same treatment/delegation definitions are used for the time measures.
    time_columns = [
        "participant.code",
        "ExplainTask",
        *[f"Round{r}" for r in range(1, 11)],
        "Del",
        "Del_hypo",
        "OneDecision",
    ]
    page_times = pd.read_excel(DELEGATOR_PAGETIMES, usecols=time_columns)
    page_times = page_times.merge(
        d[["code", "treat", "delegation"]],
        left_on="participant.code",
        right_on="code",
        how="inner",
        validate="one_to_one",
    )
    page_times = page_times[page_times["delegation"] == 0].copy()
    page_times["final_prediction_time"] = np.where(
        page_times["treat"] == 0,
        page_times["OneDecision"] - page_times["Del"],
        page_times["OneDecision"] - page_times["Del_hypo"],
    )
    initial_durations = pd.concat(
        [page_times["Round1"] - page_times["ExplainTask"]]
        + [
            page_times[f"Round{r}"] - page_times[f"Round{r - 1}"]
            for r in range(2, 11)
        ],
        axis=1,
    )
    page_times["initial_prediction_time_mean"] = initial_durations.mean(axis=1)
    page_times["prediction_time_increase"] = (
        page_times["final_prediction_time"]
        - page_times["initial_prediction_time_mean"]
    )

    rates = nondeleg.groupby("treat")["success_last"].agg(["mean", "count"]).to_dict("index")
    perf_means = nondeleg.groupby("treat")["overall_score"].mean().to_dict()

    pun = nondeleg[nondeleg["treat"] == 0]["success_last"]
    nopun = nondeleg[nondeleg["treat"] == 1]["success_last"]
    p_succ = _welch_p(nopun, pun)

    pun_perf = nondeleg[nondeleg["treat"] == 0]["overall_score"]
    nopun_perf = nondeleg[nondeleg["treat"] == 1]["overall_score"]
    p_perf = _welch_p(nopun_perf, pun_perf)

    pun_error = nondeleg[nondeleg["treat"] == 0]["initial_abs_error"]
    nopun_error = nondeleg[nondeleg["treat"] == 1]["initial_abs_error"]
    pun_improvement = nondeleg[nondeleg["treat"] == 0]["abs_error_improvement"]
    nopun_improvement = nondeleg[nondeleg["treat"] == 1]["abs_error_improvement"]

    pun_times = page_times[page_times["treat"] == 0]
    nopun_times = page_times[page_times["treat"] == 1]
    pun_final_time = pun_times["final_prediction_time"]
    nopun_final_time = nopun_times["final_prediction_time"]
    pun_time_increase = pun_times["prediction_time_increase"]
    nopun_time_increase = nopun_times["prediction_time_increase"]

    out = {
        "nondeleg_punishment_n": int(rates[0]["count"]),
        "nondeleg_no_punishment_n": int(rates[1]["count"]),
        "nondeleg_punishment_success_rate_pct": round(100 * float(rates[0]["mean"]), 1),
        "nondeleg_no_punishment_success_rate_pct": round(100 * float(rates[1]["mean"]), 1),
        "nondeleg_success_p": round(p_succ, 4),
        "nondeleg_punishment_overall_score_mean": round(float(perf_means[0]), 2),
        "nondeleg_no_punishment_overall_score_mean": round(float(perf_means[1]), 2),
        "nondeleg_overall_score_p": round(p_perf, 4),
        "effort_initial_abs_error_punishment_mean": round(float(pun_error.mean()), 2),
        "effort_initial_abs_error_no_punishment_mean": round(float(nopun_error.mean()), 2),
        "effort_initial_abs_error_welch_p": round(_welch_p(nopun_error, pun_error), 4),
        "effort_initial_abs_error_mwu_p": round(_mwu_p(nopun_error, pun_error), 4),
        "effort_abs_error_improvement_punishment_mean": round(float(pun_improvement.mean()), 2),
        "effort_abs_error_improvement_no_punishment_mean": round(float(nopun_improvement.mean()), 2),
        "effort_abs_error_improvement_punishment_median": round(float(pun_improvement.median()), 2),
        "effort_abs_error_improvement_no_punishment_median": round(float(nopun_improvement.median()), 2),
        "effort_abs_error_improvement_welch_p": round(
            _welch_p(nopun_improvement, pun_improvement), 4
        ),
        "effort_abs_error_improvement_mwu_p": round(
            _mwu_p(nopun_improvement, pun_improvement), 4
        ),
        "effort_abs_error_improvement_punishment_onesample_p": round(
            float(stats.ttest_1samp(pun_improvement.dropna(), popmean=0).pvalue), 4
        ),
        "effort_abs_error_improvement_no_punishment_onesample_p": round(
            float(stats.ttest_1samp(nopun_improvement.dropna(), popmean=0).pvalue), 4
        ),
        "effort_abs_error_improvement_punishment_wilcoxon_p": round(
            float(stats.wilcoxon(pun_improvement.dropna()).pvalue), 4
        ),
        "effort_abs_error_improvement_no_punishment_wilcoxon_p": round(
            float(stats.wilcoxon(nopun_improvement.dropna()).pvalue), 4
        ),
        "effort_screen_time_punishment_n": int(pun_final_time.notna().sum()),
        "effort_screen_time_no_punishment_n": int(nopun_final_time.notna().sum()),
        "effort_final_screen_time_punishment_median": round(float(pun_final_time.median()), 1),
        "effort_final_screen_time_no_punishment_median": round(float(nopun_final_time.median()), 1),
        "effort_final_screen_time_mwu_p": round(_mwu_p(nopun_final_time, pun_final_time), 4),
        "effort_screen_time_increase_punishment_mean": round(float(pun_time_increase.mean()), 1),
        "effort_screen_time_increase_no_punishment_mean": round(float(nopun_time_increase.mean()), 1),
        "effort_screen_time_increase_punishment_median": round(float(pun_time_increase.median()), 1),
        "effort_screen_time_increase_no_punishment_median": round(float(nopun_time_increase.median()), 1),
        "effort_screen_time_increase_mwu_p": round(
            _mwu_p(nopun_time_increase, pun_time_increase), 4
        ),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
