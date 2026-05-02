"""Player B's beliefs about Player A's performance and their relation to punishment.

Player B's wa_difficulty = weighted average of their estimated population score
distribution. Compares Player A vs Player B overestimation. Tests independence
between Player B's punishment cells and their beliefs about Player A performance.
"""
from __future__ import annotations

from scipy import stats

from lib.io import load_delegator, load_evaluator
from lib import manifest

CELLS = ["punish_del_good", "punish_del_bad", "punish_nodel_good", "punish_nodel_bad"]


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    true_mean = float(d["overall_score"].mean())
    a_belief_mean = float(d["wa_confidence"].mean())
    b_belief_mean = float(e["wa_difficulty"].mean())

    a_overestimation = a_belief_mean - true_mean
    b_overestimation = b_belief_mean - true_mean

    pun = e[(e["treat"] == 0) & (e["pass_att2"] == 1)].copy()

    # Pearson + Kendall correlations between Player B's wa_difficulty and each punishment cell
    out = {
        "true_overall_score_mean": round(true_mean, 3),
        "a_wa_confidence_mean": round(a_belief_mean, 3),
        "b_wa_difficulty_mean": round(b_belief_mean, 3),
        "a_overestimation_score_pts": round(a_overestimation, 3),
        "b_overestimation_score_pts": round(b_overestimation, 3),
    }
    for cell in CELLS:
        sub = pun[[cell, "wa_difficulty"]].dropna()
        r_p, p_p = stats.pearsonr(sub[cell], sub["wa_difficulty"])
        r_k, p_k = stats.kendalltau(sub[cell], sub["wa_difficulty"])
        out[f"b_belief_pun_{cell}_pearson_r"] = round(float(r_p), 3)
        out[f"b_belief_pun_{cell}_pearson_p"] = round(float(p_p), 4)
        out[f"b_belief_pun_{cell}_kendall_tau"] = round(float(r_k), 3)
        out[f"b_belief_pun_{cell}_kendall_p"] = round(float(p_k), 4)

    # Within-subject differences
    for diff in ["nodel_del_good", "nodel_del_bad"]:
        sub = pun[[diff, "wa_difficulty"]].dropna()
        r_p, p_p = stats.pearsonr(sub[diff], sub["wa_difficulty"])
        out[f"b_belief_diff_{diff}_pearson_r"] = round(float(r_p), 3)
        out[f"b_belief_diff_{diff}_pearson_p"] = round(float(p_p), 4)

    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
