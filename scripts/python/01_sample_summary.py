"""Sample size, time-on-task, attention-check pass rates, mean performance.

Records all of these to the numbers manifest. Produces no figure or table —
the values are referenced inline by the manuscript and filled in via the manifest.
"""
from scipy import stats as st

from lib.io import load_delegator, load_evaluator
from lib import manifest


def main() -> None:
    d_recruited = load_delegator(include_unrealistic=True)
    d = load_delegator()
    e = load_evaluator()

    n_a = len(d)
    n_b = len(e)
    n_a_recruited = len(d_recruited)

    pass_a_belief = int(d["pass_att2"].sum())
    pass_a_punish = int(d["pass_att1"].sum())
    pass_b = int(e["pass_att2"].sum())

    time_a_min = float(d["time_taken"].mean()) / 60
    time_b_min = float(e["time_taken"].mean()) / 60

    overall_score_mean = float(d["overall_score"].mean())
    by_treat = d.groupby("treat")["overall_score"].mean().to_dict()
    score_ttest = st.ttest_ind(d.loc[d["treat"] == 0, "overall_score"],
                               d.loc[d["treat"] == 1, "overall_score"], equal_var=False)
    conf_by_treat = d.groupby("treat")["wa_confidence"].mean().to_dict()
    conf_ttest = st.ttest_ind(d.loc[d["treat"] == 0, "wa_confidence"],
                              d.loc[d["treat"] == 1, "wa_confidence"], equal_var=False)

    out = {
        "n_player_a_recruited": n_a_recruited,
        "n_player_b_recruited": n_b,
        "n_total_recruited": n_a_recruited + n_b,
        "n_player_a_analysis": n_a,
        "n_player_b_analysis": n_b,
        "n_total_analysis": n_a + n_b,
        # Backward-compatible aliases refer to the analytical sample.
        "n_player_a": n_a,
        "n_player_b": n_b,
        "n_total": n_a + n_b,
        "pass_a_belief_count": pass_a_belief,
        "pass_a_belief_pct": round(100 * pass_a_belief / n_a, 1),
        "pass_a_punish_count": pass_a_punish,
        "pass_b_count": pass_b,
        "pass_b_pct": round(100 * pass_b / n_b, 1),
        "time_a_min": round(time_a_min, 1),
        "time_b_min": round(time_b_min, 1),
        "overall_score_mean": round(overall_score_mean, 2),
        "overall_score_punishment": round(by_treat[0], 2),
        "overall_score_no_punishment": round(by_treat[1], 2),
        "overall_score_ttest_p": round(float(score_ttest.pvalue), 4),
        "wa_confidence_punishment": round(conf_by_treat[0], 2),
        "wa_confidence_no_punishment": round(conf_by_treat[1], 2),
        "wa_confidence_ttest_p": round(float(conf_ttest.pvalue), 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
