"""Player B post-experiment Likert attitudes correlated with their punishment.

responsibility (Likert 1-5): how responsible should Player A feel?
trust (Likert 1-5): trust in the algorithm.
perception (Likert 1-5): perception of task difficulty.

Tests whether attitudes about responsibility / trust correlate with the
within-subject difference (nodel - del) in punishment for bad outcomes —
i.e., whether subjects who think humans should be held responsible for
algorithmic decisions also punish delegated bad outcomes more relative to
self-made bad outcomes.
"""
from __future__ import annotations

from scipy import stats

from lib.io import load_evaluator
from lib import manifest

LIKERTS = ["responsibility", "trust", "perception"]


def main() -> None:
    e = load_evaluator()
    pun = e[(e["treat"] == 0) & (e["pass_att2"] == 1)].copy()

    out = {}
    for likert in LIKERTS:
        sub = pun[[likert, "nodel_del_bad", "nodel_del_good", "punish_del_bad", "punish_nodel_bad",
                   "punish_del_good", "punish_nodel_good"]].dropna(subset=[likert])
        out[f"b_likert_{likert}_n"] = int(len(sub))
        out[f"b_likert_{likert}_mean"] = round(float(sub[likert].mean()), 3)
        out[f"b_likert_{likert}_sd"] = round(float(sub[likert].std()), 3)

        # Correlate with punishment differences
        for diff in ["nodel_del_bad", "nodel_del_good"]:
            ss = sub[[likert, diff]].dropna()
            if len(ss) >= 5:
                r_p, p_p = stats.pearsonr(ss[likert], ss[diff])
                r_s, p_s = stats.spearmanr(ss[likert], ss[diff])
                out[f"b_likert_{likert}_x_{diff}_pearson_r"] = round(float(r_p), 3)
                out[f"b_likert_{likert}_x_{diff}_pearson_p"] = round(float(p_p), 4)
                out[f"b_likert_{likert}_x_{diff}_spearman_rho"] = round(float(r_s), 3)
                out[f"b_likert_{likert}_x_{diff}_spearman_p"] = round(float(p_s), 4)

    # Frequency table of `accountability` (string) — who should be accountable?
    acc = e.loc[(e["treat"] == 0) & (e["pass_att2"] == 1), "accountability"].dropna()
    counts = acc.value_counts()
    print("\naccountability (top responses):")
    for k, v in counts.items():
        print(f"  {v:>3}  {k}")
    out["accountability_n"] = int(len(acc))
    out["accountability_top_response"] = str(counts.index[0]) if len(counts) > 0 else None
    out["accountability_top_share_pct"] = round(100 * float(counts.iloc[0] / len(acc)), 1) if len(acc) > 0 else None

    manifest.update(out)
    for k, v in out.items():
        if not k.startswith("accountability_top_response"):  # already printed above
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
