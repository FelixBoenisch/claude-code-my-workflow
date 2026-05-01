"""Result 2: paired tests on punishment cells; MDE; figures (original notebook styling).

Produces:
  figures/punishment.png
  figures/punishment_shares.png
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from lib.io import load_delegator, load_evaluator
from lib.paths import FIGURES
from lib import manifest

COLORS = ["#5DB692", "#B65D81"]
CELL_ORDER = [
    ("punish_del_good", "belief_del_good", "Delegation +\n high payoff"),
    ("punish_nodel_good", "belief_nodel_good", "No delegation +\n high payoff"),
    ("punish_del_bad", "belief_del_bad", "Delegation +\n low payoff"),
    ("punish_nodel_bad", "belief_nodel_bad", "No delegation +\n low payoff"),
]
BINARY_CELL_ORDER = [
    ("punish_del_good_binary", "belief_del_good_binary", "Delegation +\n high payoff"),
    ("punish_nodel_good_binary", "belief_nodel_good_binary", "No delegation +\n high payoff"),
    ("punish_del_bad_binary", "belief_del_bad_binary", "Delegation +\n low payoff"),
    ("punish_nodel_bad_binary", "belief_nodel_bad_binary", "No delegation +\n low payoff"),
]


def grouped_bar(ev2: pd.DataFrame, dg2: pd.DataFrame, cells, ylabel: str, ylim: float,
                pun_label: str, bel_label: str, save_to) -> None:
    ev_means = [ev2[c[0]].mean() for c in cells]
    ev_sems = [ev2[c[0]].sem() for c in cells]
    dg_means = [dg2[c[1]].mean() for c in cells]
    dg_sems = [dg2[c[1]].sem() for c in cells]

    x = list(range(len(cells)))
    width = 0.3

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.bar([p + width for p in x], dg_means, width, yerr=dg_sems, capsize=5,
           label=bel_label, color=COLORS[0])
    ax.bar(x, ev_means, width, yerr=ev_sems, capsize=5,
           label=pun_label, color=COLORS[1])
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, ylim)
    ax.set_xticks([p + width / 2 for p in x])
    ax.set_xticklabels([c[2] for c in cells])
    ax.legend(loc="upper left", frameon=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    fig.savefig(save_to, bbox_inches="tight", dpi=200)
    plt.close(fig)


def main() -> None:
    e = load_evaluator()
    d = load_delegator()

    pun = e[(e["treat"] == 0) & (e["pass_att2"] == 1)].copy()
    pun_d = d[(d["treat"] == 0) & (d["pass_att2"] == 1)].copy()
    n_pun = len(pun)

    means = {c[0]: float(pun[c[0]].mean()) for c in CELL_ORDER}

    diff_bad = pun["punish_nodel_bad"] - pun["punish_del_bad"]
    diff_good = pun["punish_nodel_good"] - pun["punish_del_good"]

    _, p_bad_t = stats.ttest_rel(pun["punish_nodel_bad"], pun["punish_del_bad"])
    _, p_bad_w = stats.wilcoxon(pun["punish_nodel_bad"], pun["punish_del_bad"], zero_method="wilcox")
    _, p_good_t = stats.ttest_rel(pun["punish_nodel_good"], pun["punish_del_good"])
    try:
        _, p_good_w = stats.wilcoxon(pun["punish_nodel_good"], pun["punish_del_good"], zero_method="wilcox")
    except ValueError:
        p_good_w = float("nan")

    sd_diff_bad = float(diff_bad.std(ddof=1))
    sd_diff_good = float(diff_good.std(ddof=1))
    mde_bad = 2.8 * sd_diff_bad / np.sqrt(n_pun)
    mde_good = 2.8 * sd_diff_good / np.sqrt(n_pun)

    n_never = int((pun.set_index("code")[
        ["punish_del_good", "punish_del_bad", "punish_nodel_good", "punish_nodel_bad"]
    ] == 0).all(axis=1).sum())
    pct_never = round(100 * n_never / n_pun, 1)
    pun_full = e[e["treat"] == 0]
    n_never_full = int(pun_full["never_punish"].sum())
    pct_never_full = round(100 * n_never_full / len(pun_full), 1)

    out = {
        "h2_n_punishment": n_pun,
        "punish_del_bad_mean": round(means["punish_del_bad"], 4),
        "punish_nodel_bad_mean": round(means["punish_nodel_bad"], 4),
        "punish_del_good_mean": round(means["punish_del_good"], 4),
        "punish_nodel_good_mean": round(means["punish_nodel_good"], 4),
        "h2_paired_t_bad_p": round(float(p_bad_t), 4),
        "h2_wilcoxon_bad_p": round(float(p_bad_w), 4),
        "h2_paired_t_good_p": round(float(p_good_t), 4),
        "h2_wilcoxon_good_p": round(float(p_good_w), 4) if not np.isnan(p_good_w) else None,
        "h2_diff_bad_mean": round(float(diff_bad.mean()), 4),
        "h2_diff_good_mean": round(float(diff_good.mean()), 4),
        "h2_mde_bad_at_80pct_power": round(mde_bad, 4),
        "h2_mde_good_at_80pct_power": round(mde_good, 4),
        "n_never_punish_attention_pass": n_never,
        "pct_never_punish_attention_pass": pct_never,
        "n_never_punish_full": n_never_full,
        "pct_never_punish_full": pct_never_full,
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")

    grouped_bar(
        pun, pun_d, CELL_ORDER,
        ylabel="Punishment in \\pounds",
        ylim=1.1,
        pun_label="Player B - Actual Punishment",
        bel_label="Player A - Beliefs",
        save_to=FIGURES / "punishment.png",
    )
    grouped_bar(
        pun, pun_d, BINARY_CELL_ORDER,
        ylabel="Share of positive punishment",
        ylim=1.1,
        pun_label="Player B - Actual Punishment",
        bel_label="Player A - Beliefs",
        save_to=FIGURES / "punishment_shares.png",
    )


if __name__ == "__main__":
    main()
