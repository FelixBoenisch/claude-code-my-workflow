"""Realized vs anticipated punishment per scenario.

Three series per (delegation, outcome) cell, attention-check passers only:
  - Player A beliefs in the Punishment condition (anticipated)
  - Player B realized punishment in the Punishment condition (realized)
  - Player A beliefs in the No-Punishment condition (hypothetical)

Layout follows the legacy `data/code_legacy/05 evaluator/01_evaluator
analysis.ipynb` (cell 27): grouped bars per scenario with SEM error bars.

Output: figures/realized_vs_anticipated.png + manifest entries.
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
COLOR_BELIEF_NOPUN = "#7A8FBF"  # blue-grey — Player A beliefs, No-Punishment


def _stats(df, cols):
    means = np.array([df[c].mean() for c in cols])
    sems = np.array([df[c].sem() for c in cols])
    return means, sems


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    dg_pun  = d[(d["treat"] == 0) & (d["pass_att2"] == 1)]
    dg_nop  = d[(d["treat"] == 1) & (d["pass_att2"] == 1)]
    ev_pun  = e[(e["treat"] == 0) & (e["pass_att2"] == 1)]

    bel_cols = [f"belief_{key}" for key, _ in CELLS]
    pun_cols = [f"punish_{key}" for key, _ in CELLS]

    bel_pun_m, bel_pun_s = _stats(dg_pun, bel_cols)
    bel_nop_m, bel_nop_s = _stats(dg_nop, bel_cols)
    pun_m, pun_s         = _stats(ev_pun, pun_cols)

    x = np.arange(len(CELLS))
    w = 0.27

    fig, ax = plt.subplots(figsize=(8, 5.2))

    ax.bar(x - w, bel_pun_m, width=w, yerr=bel_pun_s, capsize=4,
           color=COLOR_BELIEF_PUN,
           label=f"Player A beliefs — Punishment ($n={len(dg_pun)}$)")
    ax.bar(x,      pun_m,    width=w, yerr=pun_s,    capsize=4,
           color=COLOR_REALIZED,
           label=f"Player B realized punishment — Punishment ($n={len(ev_pun)}$)")
    ax.bar(x + w,  bel_nop_m, width=w, yerr=bel_nop_s, capsize=4,
           color=COLOR_BELIEF_NOPUN,
           label=f"Player A beliefs — No-Punishment, hypothetical ($n={len(dg_nop)}$)")

    ax.set_ylabel("Punishment in £")
    ax.set_xticks(x)
    ax.set_xticklabels([lab for _, lab in CELLS], fontsize=9)
    ax.set_ylim(0, max(1.25,
                       1.15 * max((bel_pun_m + bel_pun_s).max(),
                                  (bel_nop_m + bel_nop_s).max(),
                                  (pun_m + pun_s).max())))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper left", fontsize=9, frameon=False)

    fig.tight_layout()
    fig.savefig(FIGURES / "realized_vs_anticipated.png",
                bbox_inches="tight", dpi=200)
    plt.close(fig)

    out = {}
    for (key, _), b_p, b_n, r in zip(CELLS, bel_pun_m, bel_nop_m, pun_m):
        out[f"fig_rva_belief_pun_{key}_mean"]   = round(float(b_p), 4)
        out[f"fig_rva_belief_nopun_{key}_mean"] = round(float(b_n), 4)
        out[f"fig_rva_realized_{key}_mean"]     = round(float(r),   4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
