"""CONSORT-style flow counts.

Computes everything derivable from the cleaned files. Recruitment-funnel
counts (invited, consented, randomised pre-attrition) require the Prolific
audit log and remain pending.
"""
from lib.io import load_delegator, load_evaluator
from lib import manifest


def main() -> None:
    d_completed = load_delegator(include_unrealistic=True)
    d = load_delegator()
    e = load_evaluator()

    a_pun_completed = int((d_completed["treat"] == 0).sum())
    a_nopun_completed = int((d_completed["treat"] == 1).sum())
    a_pun = int((d["treat"] == 0).sum())
    a_nopun = int((d["treat"] == 1).sum())
    b_pun = int((e["treat"] == 0).sum())
    b_nopun = int((e["treat"] == 1).sum())

    a_pun_attpass = int(((d["treat"] == 0) & (d["pass_att2"] == 1)).sum())
    a_nopun_attpass = int(((d["treat"] == 1) & (d["pass_att2"] == 1)).sum())
    b_pun_attpass = int(((e["treat"] == 0) & (e["pass_att2"] == 1)).sum())
    b_nopun_attpass = int(((e["treat"] == 1) & (e["pass_att2"] == 1)).sum())

    out = {
        "consort_a_pun_completed": a_pun_completed,
        "consort_a_nopun_completed": a_nopun_completed,
        "consort_b_pun_completed": b_pun,
        "consort_b_nopun_completed": b_nopun,
        "consort_a_pun_unrealistic_excluded": a_pun_completed - a_pun,
        "consort_a_nopun_unrealistic_excluded": a_nopun_completed - a_nopun,
        "consort_a_pun_full_analysis_sample": a_pun,
        "consort_a_nopun_full_analysis_sample": a_nopun,
        "consort_a_pun_attention_excluded": a_pun - a_pun_attpass,
        "consort_a_nopun_attention_excluded": a_nopun - a_nopun_attpass,
        "consort_b_pun_attention_excluded": b_pun - b_pun_attpass,
        "consort_b_nopun_attention_excluded": b_nopun - b_nopun_attpass,
        "consort_a_pun_analysis_sample": a_pun_attpass,
        "consort_a_nopun_analysis_sample": a_nopun_attpass,
        "consort_b_pun_analysis_sample": b_pun_attpass,
        "consort_b_nopun_analysis_sample": b_nopun_attpass,
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
