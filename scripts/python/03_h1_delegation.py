"""Result 1: chi-squared and Fisher exact on delegation rates by condition.

Also produces figures/delegation_shares.png in the original notebook styling.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
from scipy import stats

from lib.io import load_delegator
from lib.paths import FIGURES
from lib import manifest


def main() -> None:
    d = load_delegator()
    by = d.groupby("treat")["delegation"]

    counts = by.sum().astype(int)
    n = by.count().astype(int)
    rates = (counts / n).to_dict()
    n = n.to_dict()
    counts = counts.to_dict()

    rate_pun = rates[0]
    rate_nopun = rates[1]
    gap_pp = (rate_nopun - rate_pun) * 100

    table = np.array([[counts[0], n[0] - counts[0]], [counts[1], n[1] - counts[1]]])
    chi2, p_chi2, _, _ = stats.chi2_contingency(table, correction=False)
    _, p_fisher = stats.fisher_exact(table, alternative="two-sided")

    out = {
        "delegation_rate_punishment": round(rate_pun, 4),
        "delegation_rate_no_punishment": round(rate_nopun, 4),
        "delegation_rate_punishment_pct": round(100 * rate_pun, 1),
        "delegation_rate_no_punishment_pct": round(100 * rate_nopun, 1),
        "delegation_gap_pp": round(gap_pp, 1),
        "h1_chi2": round(float(chi2), 4),
        "h1_p_chi2_two_sided": round(float(p_chi2), 4),
        "h1_p_fisher_two_sided": round(float(p_fisher), 4),
        "h1_n_punishment": int(n[0]),
        "h1_n_no_punishment": int(n[1]),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")

    group_stats = d.groupby("treat")["delegation"].agg(["mean", "sem"]).reset_index()

    fig, ax = plt.subplots(figsize=(3.5, 5))

    x_positions = [1, 1.05]
    colors = ["#C4A54F", "#4F6EC4"]
    ax.bar(
        x_positions,
        group_stats["mean"],
        yerr=group_stats["sem"],
        capsize=5,
        width=0.03,
        color=colors,
    )
    fs = 10
    ax.annotate(
        "**",
        xy=(0.5, 0.8),
        xytext=(0.5, 0.85),
        xycoords="axes fraction",
        fontsize=fs * 1.5,
        ha="center",
        va="bottom",
        arrowprops=dict(arrowstyle="-[, widthB=3, lengthB=1", lw=1.0, color="k"),
    )
    ax.set_ylabel("Delegation share")
    ax.set_ylim(0, 1)
    ax.set_xlim(0.97, 1.08)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(["Punishment", "No-Punishment"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    fig.savefig(FIGURES / "delegation_shares.png", bbox_inches="tight", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main()
