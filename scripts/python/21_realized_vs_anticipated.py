"""Realized vs anticipated punishment per scenario (Punishment condition).

Two series per (delegation, outcome) cell:
  - Player A beliefs in the Punishment condition (anticipated)
  - Player B realized punishment in the Punishment condition (realized)

Outputs:
  figures/realized_vs_anticipated.png          -- full sample (body)
  figures/realized_vs_anticipated_passers.png  -- attention-check passers (appendix)
plus manifest entries. Player A's No-Punishment beliefs are shown in the
hypothetical-punishment appendix figure (20_punishment_figure.py).

Layout follows the legacy `data/code_legacy/05 evaluator/01_evaluator
analysis.ipynb` (cell 27): grouped bars per scenario with SEM error bars.
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from lib.io import load_delegator, load_evaluator
from lib.paths import FIGURES
from lib import manifest

CELLS = [
    ("del_good",   "Delegation +\nhigh payoff"),
    ("nodel_good", "No delegation +\nhigh payoff"),
    ("del_bad",    "Delegation +\nlow payoff"),
    ("nodel_bad",  "No delegation +\nlow payoff"),
]

COLOR_BELIEF_PUN  = "#5DB692"   # green   — Player A beliefs, Punishment
COLOR_REALIZED    = "#B65D81"   # magenta — Player B punishment, Punishment

YMAX = 1.25  # shared across both variants for visual comparability


def _stats(df, cols):
    means = np.array([df[c].mean() for c in cols])
    sems = np.array([df[c].sem() for c in cols])
    return means, sems


def _draw(bel, pun, n_bel, n_pun, save_to):
    bel_m, bel_s = bel
    pun_m, pun_s = pun
    x = np.arange(len(CELLS))
    w = 0.32

    fig, ax = plt.subplots(figsize=(8, 5.2))
    ax.bar(x - 0.5 * w, bel_m, width=w, yerr=bel_s, capsize=4,
           color=COLOR_BELIEF_PUN,
           label=f"Player A anticipated punishment ($n={n_bel}$)")
    ax.bar(x + 0.5 * w, pun_m, width=w, yerr=pun_s, capsize=4,
           color=COLOR_REALIZED,
           label=f"Player B realized punishment ($n={n_pun}$)")

    ax.set_ylabel("Punishment in £")
    ax.set_xticks(x)
    ax.set_xticklabels([lab for _, lab in CELLS], fontsize=9)
    ax.set_ylim(0, max(YMAX, 1.15 * max((bel_m + bel_s).max(),
                                        (pun_m + pun_s).max())))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper left", fontsize=9, frameon=False)

    fig.tight_layout()
    fig.savefig(save_to, bbox_inches="tight", dpi=200)
    plt.close(fig)


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    dg_full = d[d["treat"] == 0]
    ev_full = e[e["treat"] == 0]
    dg_pass = dg_full[dg_full["pass_att2"] == 1]
    ev_pass = ev_full[ev_full["pass_att2"] == 1]

    bel_cols = [f"belief_{key}" for key, _ in CELLS]
    pun_cols = [f"punish_{key}" for key, _ in CELLS]

    bel_f = _stats(dg_full, bel_cols)
    pun_f = _stats(ev_full, pun_cols)
    bel_p = _stats(dg_pass, bel_cols)
    pun_p = _stats(ev_pass, pun_cols)

    _draw(bel_f, pun_f, len(dg_full), len(ev_full),
          FIGURES / "realized_vs_anticipated.png")
    _draw(bel_p, pun_p, len(dg_pass), len(ev_pass),
          FIGURES / "realized_vs_anticipated_passers.png")

    out = {}
    for (key, _), b_f, r_f, b_p, r_p in zip(CELLS, bel_f[0], pun_f[0],
                                            bel_p[0], pun_p[0]):
        out[f"fig_rva_belief_pun_{key}_mean"]         = round(float(b_f), 4)
        out[f"fig_rva_realized_{key}_mean"]           = round(float(r_f), 4)
        out[f"fig_rva_belief_pun_{key}_mean_passers"] = round(float(b_p), 4)
        out[f"fig_rva_realized_{key}_mean_passers"]   = round(float(r_p), 4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
