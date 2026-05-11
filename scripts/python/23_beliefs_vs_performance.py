"""Appendix figure: punishment beliefs are independent of task performance.

Shows Player~A's four cell-level punishment beliefs and the two outcome-conditional
belief differences (no-delegation minus delegation) against `overall_score`, in the
Punishment condition and restricted to attention-check passers.

Each panel annotates the Pearson correlation and its p-value, with an OLS fit line.

Output: figures/beliefs_vs_performance.png + manifest entries.
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

PANELS = [
    [("belief_del_good",   "Belief: delegation + high payoff"),
     ("belief_nodel_good", "Belief: self decision + high payoff"),
     ("nodel_del_good",    "Belief difference (high payoff)\n(self − delegation)")],
    [("belief_del_bad",    "Belief: delegation + low payoff"),
     ("belief_nodel_bad",  "Belief: self decision + low payoff"),
     ("nodel_del_bad",     "Belief difference (low payoff)\n(self − delegation)")],
]
COLOR_PUN = "#5DB692"


def _annot(ax, x, y, *, title):
    mask = x.notna() & y.notna()
    x, y = x[mask], y[mask]
    if len(x) < 3:
        return None
    r, p = stats.pearsonr(x, y)
    ax.scatter(x + np.random.RandomState(0).uniform(-0.12, 0.12, len(x)),
               y, s=18, color=COLOR_PUN, alpha=0.55, edgecolor="black",
               linewidth=0.3)
    b1, b0 = np.polyfit(x, y, 1)
    xs = np.array([x.min(), x.max()])
    ax.plot(xs, b0 + b1 * xs, color="#222", linewidth=1.1)
    ax.set_title(title, fontsize=10)
    ax.text(0.04, 0.95, f"$r={r:+.3f}$\n$p={p:.3f}$",
            transform=ax.transAxes, va="top", ha="left", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="0.7", alpha=0.85))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    return r, p


def main() -> None:
    d = load_delegator()
    sub = d[(d["treat"] == 0) & (d["pass_att2"] == 1)]

    fig, axes = plt.subplots(2, 3, figsize=(11, 6.4), sharex=True)
    out = {"belvp_n_passers": int(len(sub))}

    for row in (0, 1):
        for col in (0, 1, 2):
            var, title = PANELS[row][col]
            r, p = _annot(axes[row, col], sub["overall_score"], sub[var], title=title)
            out[f"belvp_{var}_r"] = round(float(r), 4)
            out[f"belvp_{var}_p"] = round(float(p), 4)

    for ax in axes[1, :]:
        ax.set_xlabel("Task performance (correct of 10)")
    for ax in axes[:, 0]:
        ax.set_ylabel("Expected punishment (£)")
    for ax in axes[:, 2]:
        ax.set_ylabel("Belief difference (£)")

    for ax in axes.ravel():
        ax.set_xticks(np.arange(0, 11))

    fig.suptitle("Player A punishment beliefs vs. task performance "
                 "(Punishment condition, attention-check passers)",
                 fontsize=11, y=1.00)
    fig.tight_layout()
    fig.savefig(FIGURES / "beliefs_vs_performance.png", dpi=200, bbox_inches="tight")
    plt.close(fig)

    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
