"""Redesigned punishment figure for the Player-B subsection.

Two panels:
  Panel A: Combined view per (delegation, outcome) cell —
           average punishment (left y-axis, £) and share punishing zero (right
           y-axis, %), with full Punishment-condition sample (full opacity)
           overlaid by attention-check passers (lower opacity).
  Panel B: HYPOTHETICAL punishment per cell, No-Punishment condition (where
           Player Bs answered the same questions but could not impose punishment
           in practice) — average (left y-axis, £) and share zero (right y-axis,
           %), full sample overlaid by attention-check passers (lower opacity).

No Player A belief overlay. (That was on the previous figure; it now belongs
to the punishment-beliefs paragraph downstream.)
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from lib.io import load_evaluator
from lib.paths import FIGURES
from lib import manifest

CELLS = [
    ("punish_del_good", "Delegated\nGood"),
    ("punish_del_bad", "Delegated\nBad"),
    ("punish_nodel_good", "Self-decided\nGood"),
    ("punish_nodel_bad", "Self-decided\nBad"),
]
COLOR_AVG = "#4F6EC4"   # blue, for avg punishment
COLOR_ZERO = "#C4A54F"  # gold, for zero-share
COLOR_HYPOT = "#888888" # grey, for hypothetical bars


def _cell_arrays(df, cols):
    means = np.array([df[c].mean() for c in cols])
    sems = np.array([df[c].sem() for c in cols])
    zero_share = np.array([(df[c] == 0).mean() for c in cols])
    return means, sems, zero_share


def main() -> None:
    e = load_evaluator()
    pun_full = e[e["treat"] == 0]                                # actual Punishment, n=80
    pun_pass = pun_full[pun_full["pass_att2"] == 1]              # actual passers, n=67
    hypo_full = e[e["treat"] == 1]                               # hypothetical No-Punishment, n=81
    hypo_pass = hypo_full[hypo_full["pass_att2"] == 1]           # hypothetical passers

    cols = [c for c, _ in CELLS]
    labels = [lab for _, lab in CELLS]
    x = np.arange(len(CELLS))

    full_means, full_sems, full_zero = _cell_arrays(pun_full, cols)
    pass_means, pass_sems, pass_zero = _cell_arrays(pun_pass, cols)
    hypo_full_means, hypo_full_sems, hypo_full_zero = _cell_arrays(hypo_full, cols)
    hypo_pass_means, hypo_pass_sems, hypo_pass_zero = _cell_arrays(hypo_pass, cols)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
    fs = 10
    w = 0.18

    # ------------------------------------------------------------------ Panel A
    ax = axes[0]
    ax2 = ax.twinx()

    # Average punishment bars (left axis)
    ax.bar(x - 1.5 * w, full_means, width=w, yerr=full_sems, capsize=3,
           color=COLOR_AVG, alpha=1.0,
           label=f"Avg punishment, full ($n={len(pun_full)}$)")
    ax.bar(x - 0.5 * w, pass_means, width=w, yerr=pass_sems, capsize=3,
           color=COLOR_AVG, alpha=0.4,
           label=f"Avg punishment, passers ($n={len(pun_pass)}$)")

    # Zero-punishment shares (right axis)
    ax2.bar(x + 0.5 * w, 100 * full_zero, width=w,
            color=COLOR_ZERO, alpha=1.0,
            label=f"Share zero, full ($n={len(pun_full)}$)")
    ax2.bar(x + 1.5 * w, 100 * pass_zero, width=w,
            color=COLOR_ZERO, alpha=0.4,
            label=f"Share zero, passers ($n={len(pun_pass)}$)")

    ax.set_title("(A) Average punishment and share punishing zero", fontsize=fs)
    ax.set_ylabel("Average punishment (£)", color=COLOR_AVG)
    ax.tick_params(axis="y", labelcolor=COLOR_AVG)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=fs - 1)
    ax.set_ylim(0, max(0.75, max((full_means + full_sems).max(),
                                 (pass_means + pass_sems).max()) * 1.20))
    ax.spines["top"].set_visible(False)

    ax2.set_ylabel("Share punishing zero (%)", color=COLOR_ZERO)
    ax2.tick_params(axis="y", labelcolor=COLOR_ZERO)
    ax2.set_ylim(0, 100)
    ax2.spines["top"].set_visible(False)

    # Combined legend
    handles_left, labels_left = ax.get_legend_handles_labels()
    handles_right, labels_right = ax2.get_legend_handles_labels()
    ax.legend(handles_left + handles_right, labels_left + labels_right,
              fontsize=fs - 2, loc="upper left", frameon=False, ncol=1)

    # ------------------------------------------------------------------ Panel B
    ax = axes[1]
    ax2b = ax.twinx()

    ax.bar(x - 1.5 * w, hypo_full_means, width=w, yerr=hypo_full_sems, capsize=3,
           color=COLOR_AVG, alpha=1.0,
           label=f"Avg punishment, full ($n={len(hypo_full)}$)")
    ax.bar(x - 0.5 * w, hypo_pass_means, width=w, yerr=hypo_pass_sems, capsize=3,
           color=COLOR_AVG, alpha=0.4,
           label=f"Avg punishment, passers ($n={len(hypo_pass)}$)")

    ax2b.bar(x + 0.5 * w, 100 * hypo_full_zero, width=w,
             color=COLOR_ZERO, alpha=1.0,
             label=f"Share zero, full ($n={len(hypo_full)}$)")
    ax2b.bar(x + 1.5 * w, 100 * hypo_pass_zero, width=w,
             color=COLOR_ZERO, alpha=0.4,
             label=f"Share zero, passers ($n={len(hypo_pass)}$)")

    ax.set_title("(B) Hypothetical punishment (No-Punishment condition)", fontsize=fs)
    ax.set_ylabel("Average punishment (£)", color=COLOR_AVG)
    ax.tick_params(axis="y", labelcolor=COLOR_AVG)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=fs - 1)
    # Match Panel A's left-axis range for visual comparability
    ax.set_ylim(0, max(0.75, max((full_means + full_sems).max(),
                                 (pass_means + pass_sems).max(),
                                 (hypo_full_means + hypo_full_sems).max(),
                                 (hypo_pass_means + hypo_pass_sems).max()) * 1.20))
    ax.spines["top"].set_visible(False)

    ax2b.set_ylabel("Share punishing zero (%)", color=COLOR_ZERO)
    ax2b.tick_params(axis="y", labelcolor=COLOR_ZERO)
    ax2b.set_ylim(0, 100)
    ax2b.spines["top"].set_visible(False)

    handles_left, labels_left = ax.get_legend_handles_labels()
    handles_right, labels_right = ax2b.get_legend_handles_labels()
    ax.legend(handles_left + handles_right, labels_left + labels_right,
              fontsize=fs - 2, loc="upper left", frameon=False, ncol=1)

    # Re-sync Panel A's left-axis range with Panel B for direct comparability
    axes[0].set_ylim(ax.get_ylim())

    fig.tight_layout()
    fig.savefig(FIGURES / "punishment.png", bbox_inches="tight", dpi=200)
    plt.close(fig)

    # Manifest
    out = {}
    for col, mean, zero, sem in zip(cols, full_means, full_zero, full_sems):
        out[f"fig_pun_actual_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_actual_{col}_sem"] = round(float(sem), 4)
        out[f"fig_pun_actual_{col}_zero_share"] = round(float(zero), 4)
    for col, mean, zero in zip(cols, pass_means, pass_zero):
        out[f"fig_pun_passers_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_passers_{col}_zero_share"] = round(float(zero), 4)
    for col, mean, zero, sem in zip(cols, hypo_full_means, hypo_full_zero, hypo_full_sems):
        out[f"fig_pun_hypothetical_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_hypothetical_{col}_sem"] = round(float(sem), 4)
        out[f"fig_pun_hypothetical_{col}_zero_share"] = round(float(zero), 4)
    for col, mean, zero in zip(cols, hypo_pass_means, hypo_pass_zero):
        out[f"fig_pun_hypothetical_passers_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_hypothetical_passers_{col}_zero_share"] = round(float(zero), 4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
