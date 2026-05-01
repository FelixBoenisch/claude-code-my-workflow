"""Compute mean bonus earnings for Player A and Player B from cleaned data.

The original payoff_calc*.ipynb notebooks compute exact realized payoffs from
raw oTree exports. The cleaned files don't carry all the inputs (which round
was randomly drawn for payment, the MPL outcome, the matched Player B for each
Player A), so this script computes payoff under the experimental rules with the
following treatment of the stochastic pieces:

  - Random-round task payoff: expectation over uniform draws from rounds 1-10.
        E[task] = £4 * mean(success_r1..r10) + £2 * (1 - mean) = £2 + £2*p
  - Belief-about-own-performance payoff: each subject placed probability mass
        confidence0..confidence10 on each possible score; the bonus is £0.30 *
        the mass placed on the actual realized score. Deterministic.
  - Belief-about-distribution payoff: a random score 0-10 is drawn and the
        estimate must be within 5pp of the true population share at that score.
        We take expectation over the uniform draw. Deterministic given the data.
  - Risk MPL payoff: not in cleaned data. We do not include it; report the
        bonus excluding risk and note this in the manifest.
  - Player A punishment: matched at the (delegation, outcome) cell to a specific
        Player B's strategy-method choice. We don't have the matching, so use
        the per-cell mean across Player Bs in the same condition as expectation.

The resulting figure is the *mean bonus excluding the Prolific show-up fee and
the MPL outcome*. Felix should add the Prolific base fee + a small risk-MPL
adjustment when reporting total earnings in the manuscript.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from lib.io import load_delegator, load_evaluator
from lib import manifest

GOOD_DEL = 4.0   # Player A: payoff for correct random round
BAD_DEL = 2.0    # Player A: payoff for incorrect random round
GOOD_EVA = 5.0   # Player B: payoff if 11th prediction was correct
BAD_EVA = 1.0    # Player B: payoff if 11th prediction was incorrect
BELIEF_PAYMENT_CONFIDENCE = 0.30
BELIEF_PAYMENT_DIFFICULTY = 0.30
PUNISHMENT_COST = 0.10  # Player B: cost per non-zero strategy-method cell


def confidence_payoff_per_subject(d: pd.DataFrame) -> pd.Series:
    """Player A: mass placed on the realized overall_score, x £0.30."""
    out = []
    for _, row in d.iterrows():
        score = int(row["overall_score"])
        mass = float(row[f"confidence{score}"]) / 100.0  # confidence is in %
        out.append(BELIEF_PAYMENT_CONFIDENCE * mass)
    return pd.Series(out, index=d.index, name="confidence_payoff")


def difficulty_payoff_per_subject(d: pd.DataFrame, true_shares: np.ndarray) -> pd.Series:
    """E[belief-about-distribution payoff] under uniform draw of which score
    will be checked. Pays £0.30 if within 5pp."""
    out = []
    for _, row in d.iterrows():
        within = []
        for k in range(11):
            est = float(row[f"difficulty{k}"])  # in %
            true = true_shares[k]               # in %
            within.append(1.0 if abs(est - true) <= 5 else 0.0)
        prob = sum(within) / 11.0
        out.append(BELIEF_PAYMENT_DIFFICULTY * prob)
    return pd.Series(out, index=d.index, name="difficulty_payoff")


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    true_shares = (
        d["overall_score"].value_counts(normalize=True).reindex(range(11), fill_value=0).sort_index() * 100
    ).values

    # ---------- Player A ----------
    p_success = (
        d[[f"success_r{i}" for i in range(1, 11)]].mean(axis=1)
    )
    d_task = BAD_DEL + (GOOD_DEL - BAD_DEL) * p_success
    d_conf = confidence_payoff_per_subject(d)
    d_diff = difficulty_payoff_per_subject(d, true_shares)

    pun_cell_means = {
        "punish_del_good":   float(e.loc[(e["treat"] == 0) & (e["pass_att2"] == 1), "punish_del_good"].mean()),
        "punish_del_bad":    float(e.loc[(e["treat"] == 0) & (e["pass_att2"] == 1), "punish_del_bad"].mean()),
        "punish_nodel_good": float(e.loc[(e["treat"] == 0) & (e["pass_att2"] == 1), "punish_nodel_good"].mean()),
        "punish_nodel_bad":  float(e.loc[(e["treat"] == 0) & (e["pass_att2"] == 1), "punish_nodel_bad"].mean()),
    }

    def expected_punishment(row):
        if row["treat"] == 1:
            return 0.0
        # Use success_last when delegated=0; for delegated, the algo draws
        # Bernoulli(p_success) — we take expectation.
        deleg = int(row["delegation"])
        if deleg == 1:
            p_good = float(np.mean([row[f"success_r{i}"] for i in range(1, 11)]))
            return p_good * pun_cell_means["punish_del_good"] + (1 - p_good) * pun_cell_means["punish_del_bad"]
        else:
            outc = int(row["success_last"]) if pd.notna(row["success_last"]) else int(round(np.mean([row[f"success_r{i}"] for i in range(1, 11)])))
            return pun_cell_means["punish_nodel_good"] if outc == 1 else pun_cell_means["punish_nodel_bad"]

    d_pun = d.apply(expected_punishment, axis=1)

    d["bonus_excl_risk"] = d_task + d_conf + d_diff - d_pun

    # ---------- Player B ----------
    # Task payoff conditional on the matched Player A's 11th-prediction outcome.
    # We don't have per-pair matches in the cleaned data, so we use the overall
    # success rate of Player A's actual 11th predictions as the expected outcome.
    p_match_good = float(d.loc[d["delegation"] == 0, "success_last"].mean())
    e_task_expected = p_match_good * GOOD_EVA + (1 - p_match_good) * BAD_EVA

    e_diff = difficulty_payoff_per_subject(e, true_shares)

    # Punishment cost: £0.10 per cell where Player B chose strictly positive punishment.
    cells = ["punish_del_good", "punish_del_bad", "punish_nodel_good", "punish_nodel_bad"]
    e_pun_cost = (e[cells] > 0).sum(axis=1).astype(float) * PUNISHMENT_COST
    # In No-Punishment, no cost is incurred (responses hypothetical).
    e_pun_cost = e_pun_cost.where(e["treat"] == 0, 0.0)

    e["bonus_excl_risk"] = e_task_expected + e_diff - e_pun_cost

    out = {
        # Player A
        "player_a_mean_task_payoff": round(float(d_task.mean()), 2),
        "player_a_mean_confidence_payoff": round(float(d_conf.mean()), 2),
        "player_a_mean_difficulty_payoff": round(float(d_diff.mean()), 2),
        "player_a_mean_expected_punishment": round(float(d_pun.mean()), 2),
        "player_a_mean_expected_punishment_pun_only": round(
            float(d.loc[d["treat"] == 0].apply(expected_punishment, axis=1).mean()), 2
        ),
        "player_a_mean_bonus_excl_risk": round(float(d["bonus_excl_risk"].mean()), 2),
        # Player B
        "player_b_mean_task_payoff_expected": round(float(e_task_expected), 2),
        "player_b_mean_difficulty_payoff": round(float(e_diff.mean()), 2),
        "player_b_mean_punishment_cost": round(float(e_pun_cost.mean()), 2),
        "player_b_mean_bonus_excl_risk": round(float(e["bonus_excl_risk"].mean()), 2),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
