"""Performance figure (5-panel barplot + boxplots) and performance/delegation scatter.

Replicates the original notebook styling: actual performance distribution +
KDE of performance beliefs, with by-condition horizontal boxplots underneath.

Produces:
  figures/performance.png
  figures/performance_delegation_scatter.png
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats as st

from lib.io import load_delegator
from lib.paths import FIGURES
from lib import manifest

COLORS = ["#5DB692", "#B65D81"]


def main() -> None:
    dg = load_delegator()

    bar_color = COLORS[0]
    boxplot_color_0 = sns.light_palette(bar_color, n_colors=3)[1]
    boxplot_color_1 = sns.light_palette(bar_color, n_colors=3)[2]
    density_color = COLORS[1]
    boxplot_conf_color_0 = sns.light_palette(density_color, n_colors=3)[1]
    boxplot_conf_color_1 = sns.light_palette(density_color, n_colors=3)[2]

    fig, ax = plt.subplots(
        5, 1, figsize=(7, 5), sharex=True,
        gridspec_kw={"height_ratios": [10, 1, 1, 1, 1], "hspace": 0},
    )

    score_counts = dg["overall_score"].value_counts(normalize=True).sort_index()
    sns.barplot(x=score_counts.index, y=score_counts.values, color=bar_color, alpha=0.8, ax=ax[0], width=0.5)
    sns.kdeplot(dg["wa_confidence"], color=density_color, linewidth=2, ax=ax[0], clip=(0, 10))

    ax[0].set_ylabel("Relative Frequency")
    for s in ("top", "right", "bottom"):
        ax[0].spines[s].set_visible(False)
    ax[0].tick_params(axis="x", which="both", bottom=False, labelbottom=False)

    sns.boxplot(x=dg.loc[dg["treat"] == 0, "overall_score"], ax=ax[1], color=boxplot_color_0, width=0.5)
    sns.boxplot(x=dg.loc[dg["treat"] == 1, "overall_score"], ax=ax[2], color=boxplot_color_1, width=0.5)
    sns.boxplot(x=dg.loc[dg["treat"] == 0, "wa_confidence"], ax=ax[3], color=boxplot_conf_color_0, width=0.5)
    sns.boxplot(x=dg.loc[dg["treat"] == 1, "wa_confidence"], ax=ax[4], color=boxplot_conf_color_1, width=0.5)

    for i in (1, 2, 3):
        for s in ("top", "right", "left", "bottom"):
            ax[i].spines[s].set_visible(False)
        ax[i].tick_params(axis="x", which="both", bottom=False, labelbottom=False)
        ax[i].tick_params(axis="y", which="both", left=False, labelleft=False)
    for s in ("top", "right", "left"):
        ax[4].spines[s].set_visible(False)
    ax[4].tick_params(axis="y", which="both", left=False, labelleft=False)
    ax[4].set_xlabel("Score (0--10)")
    ax[4].set_xticks(range(11))
    ax[4].set_xticklabels(range(11))

    f1 = plt.Line2D([0], [0], color=bar_color, lw=6, label="Actual performance")
    f2 = plt.Line2D([0], [0], color=boxplot_color_0, lw=4, linestyle="-", label="Punishment")
    f3 = plt.Line2D([0], [0], color=boxplot_color_1, lw=4, linestyle="-", label="No-Punishment")
    f4 = plt.Line2D([0], [0], color=density_color, lw=6, label="Performance beliefs")
    f5 = plt.Line2D([0], [0], color=boxplot_conf_color_0, lw=4, linestyle="-", label="Punishment")
    f6 = plt.Line2D([0], [0], color=boxplot_conf_color_1, lw=4, linestyle="-", label="No-Punishment")

    legend1 = ax[0].legend([f1], ["Actual performance"], fontsize=10, loc="upper right",
                           bbox_to_anchor=(0.98, 1), frameon=False)
    legend2 = ax[0].legend([f2, f3], ["  Punishment", "  No-Punishment"],
                           fontsize=8, loc="upper right", bbox_to_anchor=(1.01, 0.93), frameon=False)
    legend3 = ax[0].legend([f4], ["Performance beliefs"], fontsize=10, loc="upper right",
                           bbox_to_anchor=(0.98, 0.83), frameon=False)
    legend4 = ax[0].legend([f5, f6], ["  Punishment", "  No-Punishment"],
                           fontsize=8, loc="upper right", bbox_to_anchor=(1.01, 0.76), frameon=False)
    ax[0].add_artist(legend1)
    ax[0].add_artist(legend2)
    ax[0].add_artist(legend3)
    ax[0].add_artist(legend4)

    plt.tight_layout()
    fig.savefig(FIGURES / "performance.png", bbox_inches="tight", dpi=200)
    plt.close(fig)

    # Binned scatter by performance and condition
    fig, ax = plt.subplots(figsize=(7, 5))
    treat_label = {0: "Punishment", 1: "No-Punishment"}
    for treat, color in [(0, COLORS[0]), (1, COLORS[1])]:
        sub = dg[dg["treat"] == treat]
        agg = sub.groupby("overall_score")["delegation"].agg(["mean", "count"]).reset_index()
        ax.scatter(
            agg["overall_score"], agg["mean"],
            s=10 + 12 * agg["count"], color=color, alpha=0.7,
            edgecolor="black", linewidth=0.4, label=treat_label[treat],
        )
        ax.plot(agg["overall_score"], agg["mean"], color=color, linewidth=1.4)
    ax.set_xlabel("Score in first 10 rounds")
    ax.set_ylabel("Share delegating")
    ax.set_xticks(np.arange(0, 11))
    ax.set_ylim(0, 1)
    ax.legend(frameon=False, title="Condition")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title("Delegation share by performance and condition\n(dot size proportional to subject count)", fontsize=10)
    plt.tight_layout()
    fig.savefig(FIGURES / "performance_delegation_scatter.png", bbox_inches="tight", dpi=200)
    plt.close(fig)

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
