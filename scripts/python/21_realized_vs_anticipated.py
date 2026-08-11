"""Realized vs anticipated punishment per scenario (Punishment condition).

House style (adopted 2026-08-10): scenarios grouped by outcome as in
20_punishment_figure.py, Player B's realized punishment (moss green, first bar)
next to Player A's anticipated punishment (terracotta, second bar), values
printed at the bar base, +-1 SE whiskers. The y-scale matches fig:punishment
in pounds per inch (same width, height scaled by the ylim ratio), so realized
bars print at the same height in both figures when included at the same width.

Outputs:
  figures/realized_vs_anticipated.png          -- full sample (body)
  figures/realized_vs_anticipated_passers.png  -- attention-check passers (appendix)
plus manifest entries. Player A's No-Punishment beliefs are shown in the
hypothetical-punishment appendix figure (20_punishment_figure.py).
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lib.io import load_delegator, load_evaluator
from lib.paths import FIGURES
from lib import manifest

KEYS = ["del_good", "nodel_good", "del_bad", "nodel_bad"]
TICKS = ["Delegated", "Self-decided", "Delegated", "Self-decided"]
TERRA = "#bb7843"   # Player A anticipated punishment
GREEN = "#5b7553"   # Player B realized punishment (matches fig:punishment)
X = [0, 1.0, 2.6, 3.6]
W = 0.345
YMAX = 1.15
HEIGHT = 4.2 * YMAX / 0.8  # same pounds-per-inch as fig:punishment


def draw(dg, ev, save_to):
    bel_m = {c: dg[f"belief_{c}"].mean() for c in KEYS}
    bel_s = {c: dg[f"belief_{c}"].sem() for c in KEYS}
    pun_m = {c: ev[f"punish_{c}"].mean() for c in KEYS}
    pun_s = {c: ev[f"punish_{c}"].sem() for c in KEYS}

    fig, ax = plt.subplots(figsize=(6.8, HEIGHT))
    for x, c in zip(X, KEYS):
        first = x == 0
        ax.bar(x - 0.5 * W, pun_m[c], width=W, yerr=pun_s[c], capsize=3,
               color=GREEN, error_kw=dict(lw=1.1),
               label="Player B realized punishment ($n=%d$)" % len(ev)
               if first else None)
        ax.bar(x + 0.5 * W, bel_m[c], width=W, yerr=bel_s[c], capsize=3,
               color=TERRA, error_kw=dict(lw=1.1),
               label="Player A anticipated punishment ($n=%d$)" % len(dg)
               if first else None)
        ax.text(x - 0.5 * W, 0.03, f"{pun_m[c]:.2f}", ha="center",
                color="white", fontsize=8, fontweight="bold")
        ax.text(x + 0.5 * W, 0.03, f"{bel_m[c]:.2f}", ha="center",
                color="white", fontsize=8, fontweight="bold")
    ax.set_ylabel("Average punishment (£)")
    ax.set_ylim(0, YMAX)
    ax.set_xticks(X)
    ax.set_xticklabels(TICKS, fontsize=9)
    y_grp = -0.122 * 4.2 / HEIGHT  # constant label distance despite taller axes
    ax.text((X[0] + X[1]) / 2, y_grp, "Good outcome", ha="center",
            transform=ax.get_xaxis_transform(), fontsize=10)
    ax.text((X[2] + X[3]) / 2, y_grp, "Bad outcome", ha="center",
            transform=ax.get_xaxis_transform(), fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    fig.tight_layout()
    fig.savefig(save_to, bbox_inches="tight", dpi=200)
    plt.close(fig)
    return bel_m, pun_m


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    dg_full = d[d["treat"] == 0]
    ev_full = e[e["treat"] == 0]
    dg_pass = dg_full[dg_full["pass_att2"] == 1]
    ev_pass = ev_full[ev_full["pass_att2"] == 1]

    bel_f, pun_f = draw(dg_full, ev_full, FIGURES / "realized_vs_anticipated.png")
    bel_p, pun_p = draw(dg_pass, ev_pass,
                        FIGURES / "realized_vs_anticipated_passers.png")

    out = {}
    for key in KEYS:
        out[f"fig_rva_belief_pun_{key}_mean"] = round(float(bel_f[key]), 4)
        out[f"fig_rva_realized_{key}_mean"] = round(float(pun_f[key]), 4)
        out[f"fig_rva_belief_pun_{key}_mean_passers"] = round(float(bel_p[key]), 4)
        out[f"fig_rva_realized_{key}_mean_passers"] = round(float(pun_p[key]), 4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
