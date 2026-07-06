"""Side-by-side version of fig:performance_delegation_scatter:
full sample (left) vs attention-check passers (right), same styling as
07_performance.py, with per-condition Pearson r/p annotated on each panel.
"""
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st

sys.path.insert(0, r"c:\Users\USER\Documents\Test environment\paper\scripts\python")
from lib.io import load_delegator

OUT = r"c:\Users\USER\Documents\Test environment\paper\explorations\perf_delegation_scatter_full_vs_passers.png"

COLORS = ["#5DB692", "#B65D81"]
TREAT_LABEL = {0: "Punishment", 1: "No-Punishment"}

dg = load_delegator()

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

for ax, (title, df) in zip(
    axes,
    [(f"Full sample ($n={len(dg)}$)", dg),
     (f"Attention-check passers ($n={(dg['pass_att2'] == 1).sum()}$)",
      dg[dg["pass_att2"] == 1])],
):
    lines = []
    for treat, color in [(0, COLORS[0]), (1, COLORS[1])]:
        sub = df[df["treat"] == treat]
        agg = sub.groupby("overall_score")["delegation"].agg(["mean", "count"]).reset_index()
        ax.scatter(
            agg["overall_score"], agg["mean"],
            s=10 + 12 * agg["count"], color=color, alpha=0.7,
            edgecolor="black", linewidth=0.4, label=TREAT_LABEL[treat],
        )
        ax.plot(agg["overall_score"], agg["mean"], color=color, linewidth=1.4)
        r, p = st.pearsonr(sub["overall_score"], sub["delegation"])
        lines.append(f"{TREAT_LABEL[treat]}: $r={r:.3f}$, $p={p:.3f}$")
    ax.text(0.02, 0.02, "\n".join(lines), transform=ax.transAxes,
            fontsize=9, va="bottom")
    ax.set_title(title, fontsize=11)
    ax.set_xlabel("Score in first 10 rounds")
    ax.set_xticks(np.arange(0, 11))
    ax.set_ylim(0, 1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

axes[0].set_ylabel("Share delegating")
axes[1].legend(frameon=False, title="Condition")
fig.suptitle("Delegation share by performance and condition (dot size proportional to subject count)",
             fontsize=11)
plt.tight_layout()
fig.savefig(OUT, bbox_inches="tight", dpi=200)
print("saved", OUT)
