"""Combined performance figure + performance/delegation statistics.

figures/performance_overview.png:
  Top panel:    delegation share by first-ten-rounds score, by condition
                (dot size = number of subjects at that score, dots connected
                within condition).
  Bottom strip: four horizontal boxplots on the shared x-axis — actual score
                (Punishment, No-Punishment) and perceived score (Punishment,
                No-Punishment). White line = median, white diamond = mean.

Color scheme: hue encodes the measure (blue = actual performance, magenta =
perceived performance), lightness encodes the condition (dark = Punishment,
light = No-Punishment). The scatter is actual-score-based and therefore uses
the blue pair.

Replaces the former figures/performance.png and
figures/performance_delegation_scatter.png (retired 2026-07-30, Package D
Change 4).
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from scipy import stats as st

from lib.io import load_delegator
from lib.paths import FIGURES
from lib import manifest

BLUE = {0: "#3b6ea8", 1: "#8aacd1"}       # actual performance: dark = Punishment
MAGENTA = {0: "#9c3a6a", 1: "#d191b0"}    # perceived performance: dark = Punishment
LABEL = {0: "Punishment", 1: "No-Punishment"}
SCORES = np.arange(0, 11)


def main() -> None:
    dg = load_delegator()

    fig = plt.figure(figsize=(8.5, 6.2))
    gs = fig.add_gridspec(2, 1, height_ratios=[3.1, 1.5], hspace=0.10)
    ax = fig.add_subplot(gs[0])
    axb = fig.add_subplot(gs[1], sharex=ax)

    # --- top: delegation share by score, dots connected within condition ----
    for t in (0, 1):
        sub = dg[dg["treat"] == t]
        agg = (sub.groupby("overall_score")["delegation"]
                  .agg(["mean", "count"]).reset_index())
        x = agg["overall_score"] + (t - 0.5) * 0.24
        ax.plot(x, agg["mean"], color=BLUE[t], linewidth=1.4, zorder=2)
        ax.scatter(x, agg["mean"], s=10 + 12 * agg["count"], color=BLUE[t],
                   label=LABEL[t], alpha=0.95, edgecolor="white",
                   linewidth=0.8, zorder=3)
        # correlation annotation at the right end of each line (stars per
        # house convention, p-values in the figure note)
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
    ns = {t: int((dg["treat"] == t).sum()) for t in (0, 1)}
    ax.legend(handles=[Line2D([], [], marker="o", ls="-", color=BLUE[t],
                              markersize=9,
                              label=f"{LABEL[t]} ($n={ns[t]}$)") for t in (0, 1)],
              frameon=False, fontsize=9, loc="upper right")

    # --- bottom: boxplots with mean diamonds --------------------------------
    rows = [
        (dg.loc[dg["treat"] == 0, "overall_score"], BLUE[0],    "Actual, Punishment"),
        (dg.loc[dg["treat"] == 1, "overall_score"], BLUE[1],    "Actual, No-Punishment"),
        (dg.loc[dg["treat"] == 0, "wa_confidence"], MAGENTA[0], "Perceived, Punishment"),
        (dg.loc[dg["treat"] == 1, "wa_confidence"], MAGENTA[1], "Perceived, No-Punishment"),
    ]
    positions = [3, 2, 1, 0]
    for (series, col, _), pos in zip(rows, positions):
        axb.boxplot(series.dropna(), positions=[pos], vert=False, widths=0.62,
                    patch_artist=True, showfliers=True, showmeans=True,
                    flierprops=dict(marker="o", markersize=3, markerfacecolor=col,
                                    markeredgecolor="none", alpha=0.5),
                    medianprops=dict(color="white", linewidth=1.4),
                    meanprops=dict(marker="D", markerfacecolor="white",
                                   markeredgecolor=col, markersize=5),
                    boxprops=dict(facecolor=col, edgecolor=col),
                    whiskerprops=dict(color=col), capprops=dict(color=col))
    axb.set_yticks(positions)
    axb.set_yticklabels([lab for _, _, lab in rows], fontsize=8.5)
    axb.set_xlabel("Correct predictions in the first ten rounds")
    axb.set_xticks(SCORES)
    axb.set_xlim(-0.7, 10.7)
    axb.spines["top"].set_visible(False)
    axb.spines["right"].set_visible(False)

    fig.savefig(FIGURES / "performance_overview.png", bbox_inches="tight", dpi=200)
    plt.close(fig)

    # --- statistics (unchanged) ---------------------------------------------
    pearson_pun_df = dg[dg["treat"] == 0][["overall_score", "delegation"]].dropna()
    pearson_pun_r = float(pearson_pun_df.corr().iloc[0, 1])
    pearson_pun_p = float(st.pearsonr(pearson_pun_df["overall_score"], pearson_pun_df["delegation"]).pvalue)

    pas = dg[dg["pass_att2"] == 1]
    pearson_pun_pas_df = pas[pas["treat"] == 0][["overall_score", "delegation"]].dropna()
    pearson_pun_pas = st.pearsonr(pearson_pun_pas_df["overall_score"], pearson_pun_pas_df["delegation"])
    pearson_nopun_df = dg[dg["treat"] == 1][["overall_score", "delegation"]].dropna()
    pearson_nopun = st.pearsonr(pearson_nopun_df["overall_score"], pearson_nopun_df["delegation"])

    out = {
        "perf_corr_punishment_r": round(pearson_pun_r, 3),
        "perf_corr_punishment_p": round(pearson_pun_p, 4),
        "perf_n_punishment": int(len(pearson_pun_df)),
        "perf_corr_punishment_passers_r": round(float(pearson_pun_pas.statistic), 3),
        "perf_corr_punishment_passers_p": round(float(pearson_pun_pas.pvalue), 4),
        "perf_n_punishment_passers": int(len(pearson_pun_pas_df)),
        "perf_corr_nopunishment_r": round(float(pearson_nopun.statistic), 3),
        "perf_corr_nopunishment_p": round(float(pearson_nopun.pvalue), 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
