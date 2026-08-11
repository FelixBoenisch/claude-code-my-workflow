"""P5 variant: bottom-panel labels as a two-column table (preview only)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "python"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from matplotlib.lines import Line2D
import numpy as np
from scipy import stats as st

from lib.io import load_delegator

BLUE = {0: "#3b6ea8", 1: "#8aacd1"}
MAGENTA = {0: "#9c3a6a", 1: "#d191b0"}
LABEL = {0: "Punishment", 1: "No-Punishment"}
SCORES = np.arange(0, 11)
OUT = r"c:\Users\USER\Documents\Test environment\paper\explorations\figs"

dg = load_delegator()
fig = plt.figure(figsize=(8.5, 6.2))
gs = fig.add_gridspec(2, 1, height_ratios=[3.1, 1.5], hspace=0.10)
ax = fig.add_subplot(gs[0])
axb = fig.add_subplot(gs[1], sharex=ax)

ns = {t: int((dg["treat"] == t).sum()) for t in (0, 1)}
for t in (0, 1):
    sub = dg[dg["treat"] == t]
    agg = (sub.groupby("overall_score")["delegation"]
              .agg(["mean", "count"]).reset_index())
    x = agg["overall_score"] + (t - 0.5) * 0.24
    ax.plot(x, agg["mean"], color=BLUE[t], linewidth=1.4, zorder=2)
    ax.scatter(x, agg["mean"], s=10 + 12 * agg["count"], color=BLUE[t],
               alpha=0.95, edgecolor="white", linewidth=0.8, zorder=3)
    r, p = st.pearsonr(sub["overall_score"], sub["delegation"])
    star = "*" * sum(p < c for c in (0.10, 0.05, 0.01))
    ax.text(x.iloc[-1] + 0.28, agg["mean"].iloc[-1],
            f"$r = {r:.2f}^{{{star}}}$" if star else f"$r = {r:.2f}$",
            color=BLUE[t], fontsize=9, va="center")
ax.set_ylabel("Share delegating")
ax.set_ylim(-0.06, 1.06)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.setp(ax.get_xticklabels(), visible=False)
ax.legend(handles=[Line2D([], [], marker="o", ls="-", color=BLUE[t],
                          markersize=9,
                          label=f"{LABEL[t]} ($n={ns[t]}$)") for t in (0, 1)],
          frameon=False, fontsize=9, loc="upper right")

rows = [
    (dg.loc[dg["treat"] == 0, "overall_score"], BLUE[0],    "Actual",    "Punishment"),
    (dg.loc[dg["treat"] == 1, "overall_score"], BLUE[1],    "Actual",    "No-Punishment"),
    (dg.loc[dg["treat"] == 0, "wa_confidence"], MAGENTA[0], "Perceived", "Punishment"),
    (dg.loc[dg["treat"] == 1, "wa_confidence"], MAGENTA[1], "Perceived", "No-Punishment"),
]
positions = [3, 2, 1, 0]
for (series, col, _, _), pos in zip(rows, positions):
    axb.boxplot(series.dropna(), positions=[pos], vert=False, widths=0.62,
                patch_artist=True, showfliers=True, showmeans=True,
                flierprops=dict(marker="o", markersize=3, markerfacecolor=col,
                                markeredgecolor="none", alpha=0.5),
                medianprops=dict(color="white", linewidth=1.4),
                meanprops=dict(marker="D", markerfacecolor="white",
                               markeredgecolor=col, markersize=5),
                boxprops=dict(facecolor=col, edgecolor=col),
                whiskerprops=dict(color=col), capprops=dict(color=col))

# two-column table labels on the left: centered columns, header rule,
# vertical rule between the columns
trans = mtransforms.blended_transform_factory(axb.transAxes, axb.transData)
FS = 7.5
X_SCORE, X_TREAT = -0.205, -0.078   # column centers
X_DIV = -0.145                     # vertical divider
X_L, X_R = -0.255, -0.015          # table extent
axb.text(X_SCORE, 3.95, "Score", transform=trans, fontsize=FS,
         fontweight="bold", ha="center", va="center")
axb.text(X_TREAT, 3.95, "Treatment", transform=trans, fontsize=FS,
         fontweight="bold", ha="center", va="center")
for (_, _, score_lab, treat_lab), pos in zip(rows, positions):
    axb.text(X_SCORE, pos, score_lab, transform=trans, fontsize=FS,
             ha="center", va="center")
    axb.text(X_TREAT, pos, treat_lab, transform=trans, fontsize=FS,
             ha="center", va="center")
axb.plot([X_L, X_R], [3.55, 3.55], transform=trans, color="black",
         linewidth=0.8, clip_on=False)
axb.plot([X_DIV, X_DIV], [4.35, -0.5], transform=trans, color="black",
         linewidth=0.8, clip_on=False)
axb.set_yticks([])
axb.set_ylim(-0.65, 4.45)
axb.set_xlabel("Correct predictions in the first ten rounds")
axb.set_xticks(SCORES)
axb.set_xlim(-0.7, 10.7)
axb.spines["top"].set_visible(False)
axb.spines["right"].set_visible(False)

fig.savefig(OUT + r"\perf_p5.png", bbox_inches="tight", dpi=200)
plt.close(fig)
print("done")
