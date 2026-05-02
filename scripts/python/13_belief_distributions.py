"""Belief distributions: figures + delegators-vs-non heterogeneity in Punishment.

Player A's belief_del_good / belief_del_bad / belief_nodel_good / belief_nodel_bad
distributions in the Punishment condition, separately for those who delegated
vs those who didn't.

Produces figures/belief_distributions.png + manifest entries.
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from lib.io import load_delegator
from lib.paths import FIGURES
from lib import manifest

CELLS = [
    ("belief_del_good", "Delegated +\nhigh payoff"),
    ("belief_nodel_good", "Self +\nhigh payoff"),
    ("belief_del_bad", "Delegated +\nlow payoff"),
    ("belief_nodel_bad", "Self +\nlow payoff"),
]
COLOR_DELEG = "#3b6ea8"
COLOR_NODEL = "#c97a3c"


def main() -> None:
    d = load_delegator()
    pun = d[(d["treat"] == 0) & (d["pass_att2"] == 1)].copy()

    fig, axes = plt.subplots(2, 2, figsize=(9, 6.5), sharex=True)
    axes = axes.flatten()

    out = {}
    for ax, (col, label) in zip(axes, CELLS):
        deleg = pun.loc[pun["delegation"] == 1, col].dropna()
        nodel = pun.loc[pun["delegation"] == 0, col].dropna()
        bins = np.arange(0, 2.21, 0.2)
        ax.hist([deleg.values, nodel.values], bins=bins, density=True,
                color=[COLOR_DELEG, COLOR_NODEL],
                label=["Delegators", "Non-delegators"], edgecolor="black", linewidth=0.4)
        ax.set_title(label, fontsize=10)
        ax.set_xlim(0, 2.0)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # Tests
        t, p_t = stats.ttest_ind(deleg, nodel, equal_var=False)
        u, p_u = stats.mannwhitneyu(deleg, nodel, alternative="two-sided")

        out[f"belief_dist_{col}_deleg_mean"] = round(float(deleg.mean()), 4)
        out[f"belief_dist_{col}_nodel_mean"] = round(float(nodel.mean()), 4)
        out[f"belief_dist_{col}_diff_mean"] = round(float(deleg.mean() - nodel.mean()), 4)
        out[f"belief_dist_{col}_t_p"] = round(float(p_t), 4)
        out[f"belief_dist_{col}_mwu_p"] = round(float(p_u), 4)
        out[f"belief_dist_{col}_n_deleg"] = int(len(deleg))
        out[f"belief_dist_{col}_n_nodel"] = int(len(nodel))

    axes[0].legend(loc="upper right", fontsize=9, frameon=False)
    for ax in axes[2:]:
        ax.set_xlabel("Expected punishment (\\pounds)")
    for ax in axes[::2]:
        ax.set_ylabel("Density")
    plt.suptitle("Player A beliefs about Player B punishment, by delegation choice", fontsize=11)
    plt.tight_layout()
    fig.savefig(FIGURES / "belief_distributions.png", dpi=200, bbox_inches="tight")
    plt.close(fig)

    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
