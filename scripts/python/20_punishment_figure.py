"""Punishment figures for the Player-B subsection.

Two separate single-panel figures (shared left-axis scale for comparability):
  figures/punishment.png              -- actual punishment, Punishment condition (body)
  figures/punishment_hypothetical.png -- hypothetical punishment, No-Punishment
                                         condition (appendix)

Each shows, per (delegation, outcome) cell: average punishment (left y-axis, £) and
the share imposing non-zero punishment (right y-axis, %), full sample at full opacity
overlaid by attention-check passers at lower opacity.
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
COLOR_PUN = "#C4A54F"   # gold, for share imposing punishment


def _cell_arrays(df, cols):
    means = np.array([df[c].mean() for c in cols])
    sems = np.array([df[c].sem() for c in cols])
    punish_share = np.array([(df[c] > 0).mean() for c in cols])
    return means, sems, punish_share


def draw_panel(ax, x, labels, full, pas, n_full, n_pass, ymax, fs=10, w=0.18):
    """Draw one punishment panel on `ax`. `full`/`pas` are (means, sems, punish) tuples."""
    f_means, f_sems, f_punish = full
    p_means, p_sems, p_punish = pas
    ax2 = ax.twinx()

    ax.bar(x - 1.5 * w, f_means, width=w, yerr=f_sems, capsize=3, color=COLOR_AVG, alpha=1.0,
           label=f"Avg punishment, full ($n={n_full}$)")
    ax.bar(x - 0.5 * w, p_means, width=w, yerr=p_sems, capsize=3, color=COLOR_AVG, alpha=0.4,
           label=f"Avg punishment, passers ($n={n_pass}$)")
    ax2.bar(x + 0.5 * w, 100 * f_punish, width=w, color=COLOR_PUN, alpha=1.0,
            label=f"Share punishing, full ($n={n_full}$)")
    ax2.bar(x + 1.5 * w, 100 * p_punish, width=w, color=COLOR_PUN, alpha=0.4,
            label=f"Share punishing, passers ($n={n_pass}$)")

    ax.set_ylabel("Average punishment (£)", color=COLOR_AVG)
    ax.tick_params(axis="y", labelcolor=COLOR_AVG)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=fs - 1)
    ax.set_ylim(0, ymax)
    ax.spines["top"].set_visible(False)

    ax2.set_ylabel("Share imposing punishment (%)", color=COLOR_PUN)
    ax2.tick_params(axis="y", labelcolor=COLOR_PUN)
    ax2.set_ylim(0, 100)
    ax2.spines["top"].set_visible(False)

    hl, ll = ax.get_legend_handles_labels()
    hr, lr = ax2.get_legend_handles_labels()
    ax.legend(hl + hr, ll + lr, fontsize=fs - 2, loc="upper left", frameon=False, ncol=1)


def main() -> None:
    e = load_evaluator()
    pun_full = e[e["treat"] == 0]                                # actual Punishment, n=80
    pun_pass = pun_full[pun_full["pass_att2"] == 1]              # actual passers, n=67
    hypo_full = e[e["treat"] == 1]                               # hypothetical No-Punishment, n=81
    hypo_pass = hypo_full[hypo_full["pass_att2"] == 1]           # hypothetical passers

    cols = [c for c, _ in CELLS]
    labels = [lab for _, lab in CELLS]
    x = np.arange(len(CELLS))

    full = _cell_arrays(pun_full, cols)
    pas = _cell_arrays(pun_pass, cols)
    hfull = _cell_arrays(hypo_full, cols)
    hpas = _cell_arrays(hypo_pass, cols)

    # Common left-axis maximum across both figures, for visual comparability.
    ymax = max(0.75, 1.20 * max(
        (full[0] + full[1]).max(), (pas[0] + pas[1]).max(),
        (hfull[0] + hfull[1]).max(), (hpas[0] + hpas[1]).max(),
    ))

    # --- Body figure: actual punishment -----------------------------------
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    draw_panel(ax, x, labels, full, pas, len(pun_full), len(pun_pass), ymax)
    fig.tight_layout()
    fig.savefig(FIGURES / "punishment.png", bbox_inches="tight", dpi=200)
    plt.close(fig)

    # --- Appendix figure: hypothetical punishment -------------------------
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    draw_panel(ax, x, labels, hfull, hpas, len(hypo_full), len(hypo_pass), ymax)
    fig.tight_layout()
    fig.savefig(FIGURES / "punishment_hypothetical.png", bbox_inches="tight", dpi=200)
    plt.close(fig)

    # Manifest
    out = {}
    for col, mean, punish, sem in zip(cols, full[0], full[2], full[1]):
        out[f"fig_pun_actual_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_actual_{col}_sem"] = round(float(sem), 4)
        out[f"fig_pun_actual_{col}_punish_share"] = round(float(punish), 4)
    for col, mean, punish in zip(cols, pas[0], pas[2]):
        out[f"fig_pun_passers_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_passers_{col}_punish_share"] = round(float(punish), 4)
    for col, mean, punish, sem in zip(cols, hfull[0], hfull[2], hfull[1]):
        out[f"fig_pun_hypothetical_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_hypothetical_{col}_sem"] = round(float(sem), 4)
        out[f"fig_pun_hypothetical_{col}_punish_share"] = round(float(punish), 4)
    for col, mean, punish in zip(cols, hpas[0], hpas[2]):
        out[f"fig_pun_hypothetical_passers_{col}_mean"] = round(float(mean), 4)
        out[f"fig_pun_hypothetical_passers_{col}_punish_share"] = round(float(punish), 4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
