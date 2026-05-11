"""Performance and confidence distributions by treatment AND delegation status.

Mirrors the layout of `07_performance.py` (a tall bars+KDE panel above thin
boxplot strips), but extended along two new dimensions:

  - the figure has two columns, one per treatment, instead of one combined column;
  - within each column the distributions are further split by delegation choice
    (delegators vs.\\ non-delegators).

Visualises the puzzle/reconciliation around results.tex line 169:
Punishment delegators are concentrated in the low-performance tail (mean 2.38);
No-Punishment delegators are drawn more uniformly across the performance
distribution (mean 2.98). The wa_confidence KDE and the boxplot strips
underneath show that the delegation gradient in belief-about-own-performance
is much weaker than in actual performance.

Output: figures/performance_by_delegation.png + manifest entries.
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from lib.io import load_delegator
from lib.paths import FIGURES
from lib import manifest

# Colour scheme:
#   Actual performance: blue family (delegators darker, non-delegators lighter).
#   wa_confidence:      magenta family (same delegator/non-delegator contrast).
COLOR_DEL_PERF   = "#3b6ea8"
COLOR_NODEL_PERF = "#8aacd1"
COLOR_DEL_CONF   = "#9c3a6a"
COLOR_NODEL_CONF = "#d191b0"

SCORES = np.arange(0, 11)
W = 0.4


def _share(sub):
    n = len(sub)
    if n == 0:
        return np.zeros_like(SCORES, dtype=float)
    counts = sub["overall_score"].value_counts().reindex(SCORES, fill_value=0)
    return counts.values / n


def _set_no_x(ax):
    ax.tick_params(axis="x", which="both", bottom=False, labelbottom=False)


def _strip(ax):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    _set_no_x(ax)
    ax.tick_params(axis="y", which="both", left=False, labelleft=False)


def main() -> None:
    d = load_delegator()
    pas = d[d["pass_att2"] == 1]

    fig, axes = plt.subplots(
        5, 2, figsize=(12, 6.0), sharex="col",
        gridspec_kw={"height_ratios": [10, 1, 1, 1, 1],
                     "hspace": 0.10, "wspace": 0.08},
    )

    out = {}

    for col_idx, (treat_val, treat_label) in enumerate(
        [(0, "Punishment"), (1, "No-Punishment")]
    ):
        sub = pas[pas["treat"] == treat_val]
        deleg = sub[sub["delegation"] == 1]
        nodel = sub[sub["delegation"] == 0]

        # ---------------- Top panel: bars + KDE ----------------
        ax_top = axes[0, col_idx]
        s_d = _share(deleg)
        s_n = _share(nodel)
        ax_top.bar(SCORES - W/2, s_d, width=W,
                   color=COLOR_DEL_PERF, edgecolor="black", linewidth=0.4,
                   label=f"Delegators ($n={len(deleg)}$, mean ${deleg['overall_score'].mean():.2f}$)")
        ax_top.bar(SCORES + W/2, s_n, width=W,
                   color=COLOR_NODEL_PERF, edgecolor="black", linewidth=0.4,
                   label=f"Non-delegators ($n={len(nodel)}$, mean ${nodel['overall_score'].mean():.2f}$)")

        sns.kdeplot(deleg["wa_confidence"], ax=ax_top, color=COLOR_DEL_CONF,
                    linewidth=2.0, clip=(0, 10),
                    label=f"Conf., delegators (mean ${deleg['wa_confidence'].mean():.2f}$)")
        sns.kdeplot(nodel["wa_confidence"], ax=ax_top, color=COLOR_NODEL_CONF,
                    linewidth=2.0, clip=(0, 10), linestyle="--",
                    label=f"Conf., non-delegators (mean ${nodel['wa_confidence'].mean():.2f}$)")

        ax_top.set_title(treat_label, fontsize=11)
        for s in ("top", "right", "bottom"):
            ax_top.spines[s].set_visible(False)
        _set_no_x(ax_top)
        if col_idx == 0:
            ax_top.set_ylabel("Relative frequency / density")
        else:
            ax_top.set_ylabel("")
        ax_top.set_xlim(-0.7, 10.7)
        ax_top.legend(loc="upper right", fontsize=7.6, frameon=False,
                      handlelength=1.6, labelspacing=0.25)

        # ---------------- Boxplot strips ----------------
        sns.boxplot(x=deleg["overall_score"], ax=axes[1, col_idx],
                    color=COLOR_DEL_PERF, width=0.5)
        sns.boxplot(x=nodel["overall_score"], ax=axes[2, col_idx],
                    color=COLOR_NODEL_PERF, width=0.5)
        sns.boxplot(x=deleg["wa_confidence"], ax=axes[3, col_idx],
                    color=COLOR_DEL_CONF, width=0.5)
        sns.boxplot(x=nodel["wa_confidence"], ax=axes[4, col_idx],
                    color=COLOR_NODEL_CONF, width=0.5)

        for row in (1, 2, 3):
            _strip(axes[row, col_idx])
        # last row: keep the x-axis line and tick labels
        for s in ("top", "right", "left"):
            axes[4, col_idx].spines[s].set_visible(False)
        axes[4, col_idx].tick_params(axis="y", which="both", left=False, labelleft=False)
        axes[4, col_idx].set_xlabel("Score / weighted-average confidence (0--10)")
        axes[4, col_idx].set_xticks(range(11))
        axes[4, col_idx].set_xticklabels(range(11))

        # ---------------- Per-treatment manifest ----------------
        t = "pun" if treat_val == 0 else "nopun"
        out.update({
            f"perfdel_passers_{t}_deleg_perf_mean":   round(float(deleg["overall_score"].mean()), 4),
            f"perfdel_passers_{t}_nodel_perf_mean":   round(float(nodel["overall_score"].mean()), 4),
            f"perfdel_passers_{t}_deleg_conf_mean":   round(float(deleg["wa_confidence"].mean()), 4),
            f"perfdel_passers_{t}_nodel_conf_mean":   round(float(nodel["wa_confidence"].mean()), 4),
            f"perfdel_passers_{t}_n_deleg":           int(len(deleg)),
            f"perfdel_passers_{t}_n_nodel":           int(len(nodel)),
        })

    # Row-label hints on the left, in the strip area
    label_kwargs = dict(ha="right", va="center", fontsize=8.5,
                         transform=axes[1, 0].transAxes)
    axes[1, 0].text(-0.02, 0.5, "Perf., del.", **label_kwargs)
    axes[2, 0].text(-0.02, 0.5, "Perf., non-del.",
                    ha="right", va="center", fontsize=8.5,
                    transform=axes[2, 0].transAxes)
    axes[3, 0].text(-0.02, 0.5, "Conf., del.",
                    ha="right", va="center", fontsize=8.5,
                    transform=axes[3, 0].transAxes)
    axes[4, 0].text(-0.02, 0.5, "Conf., non-del.",
                    ha="right", va="center", fontsize=8.5,
                    transform=axes[4, 0].transAxes)

    fig.suptitle("Distribution of task performance and confidence by treatment and delegation choice\n"
                 "(attention-check passers)", fontsize=11, y=1.005)
    fig.savefig(FIGURES / "performance_by_delegation.png",
                bbox_inches="tight", dpi=200)
    plt.close(fig)

    # Full-sample delegator means for the footnote
    full = d
    out.update({
        "perfdel_full_pun_deleg_mean":   round(float(full[(full["treat"] == 0) & (full["delegation"] == 1)]["overall_score"].mean()), 4),
        "perfdel_full_nopun_deleg_mean": round(float(full[(full["treat"] == 1) & (full["delegation"] == 1)]["overall_score"].mean()), 4),
    })
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
