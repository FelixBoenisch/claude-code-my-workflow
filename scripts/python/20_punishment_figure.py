"""Punishment figures for the Player-B subsection (W9 design, adopted 2026-08-06).

Layout: cells grouped by outcome (good pair left, bad pair right), each cell
showing average punishment (moss green, left axis, +-1 SE whiskers) and the
share imposing punishment (gold, right axis), values printed on the bars.
The main figure adds n.s. brackets over each within-outcome pair and the
good-vs-bad difference in average punishment as a green arrow connecting
dashed group-mean lines.

Outputs:
  figures/punishment.png              -- Punishment condition, full sample (body)
  figures/punishment_passers.png      -- attention-check passers (appendix)
  figures/punishment_hypothetical.png -- No-Punishment condition, full sample,
                                         incl. Player A's anticipated punishment
                                         (appendix)
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from lib.io import load_delegator, load_evaluator
from lib.paths import FIGURES
from lib import manifest

KEYS = ["punish_del_good", "punish_nodel_good", "punish_del_bad", "punish_nodel_bad"]
TICKS = ["Delegated", "Self-decided", "Delegated", "Self-decided"]
GREEN = "#5b7553"   # average punishment
GOLD = "#C4A54F"    # share imposing punishment
TERRA = "#bb7843"   # Player A anticipated punishment (matches fig:realized_vs_anticipated)
X = [0, 1.0, 2.6, 3.6]
W = 0.345


def paired_wilcoxon(a, b) -> float:
    """Wilcoxon signed-rank p-value, the within-subject non-parametric
    counterpart to the paired t-test. The preregistration specified MWU and
    Kolmogorov-Smirnov, both independent-sample tests, which do not apply to
    strategy-method data. Returns NaN when all differences are zero."""
    try:
        return float(stats.wilcoxon(a, b, zero_method="wilcox")[1])
    except ValueError:
        return float("nan")


def draw_figure(df, save_to, annotate=False, beliefs=None, n_bel=None,
                passers=None):
    """One punishment panel in the W9 design. `beliefs` adds Player A's
    anticipated-punishment bars and `passers` faded full-vs-passers overlays
    (hypothetical appendix figure)."""
    m = {c: df[c].mean() for c in KEYS}
    s = {c: df[c].sem() for c in KEYS}
    sh = {c: (df[c] > 0).mean() for c in KEYS}
    sh_sem = {c: (df[c] > 0).sem() for c in KEYS}
    n = len(df)

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    ax2 = ax.twinx()
    if beliefs is None:
        w, xs = W, X
        offs = {"avg": -0.5 * W, "share": 0.5 * W}
    else:
        w = 0.24
        xs = [0, 1.65, 4.0, 5.65]
        offs = {"bel": -2 * w, "avg": -w, "avg_p": 0, "share": w, "share_p": 2 * w}
    for x, c in zip(xs, KEYS):
        first = x == 0
        if beliefs is not None:
            ax.bar(x + offs["bel"], beliefs[c.replace("punish", "belief")].mean(),
                   width=w, yerr=beliefs[c.replace("punish", "belief")].sem(),
                   capsize=3, color=TERRA, error_kw=dict(lw=1.0),
                   label="Player A anticipated ($n=%d$)" % n_bel if first else None)
        ax.bar(x + offs["avg"], m[c], width=w, yerr=s[c], capsize=3, color=GREEN,
               error_kw=dict(lw=1.1),
               label=("Avg punishment, full ($n=%d$)" if passers is not None
                      else "Avg punishment ($n=%d$)") % n if first else None)
        ax2.bar(x + offs["share"], 100 * sh[c], width=w, yerr=100 * sh_sem[c],
                capsize=3, color=GOLD, error_kw=dict(lw=1.1),
                label=("Share punishing, full ($n=%d$)" if passers is not None
                       else "Share punishing ($n=%d$)") % n if first else None)
        if passers is not None:
            ax.bar(x + offs["avg_p"], passers[c].mean(), width=w,
                   yerr=passers[c].sem(), capsize=3, color=GREEN, alpha=0.4,
                   error_kw=dict(lw=1.0),
                   label="Avg punishment, passers ($n=%d$)" % len(passers)
                   if first else None)
            ax2.bar(x + offs["share_p"], 100 * (passers[c] > 0).mean(), width=w,
                    yerr=100 * (passers[c] > 0).sem(), capsize=3,
                    color=GOLD, alpha=0.4, error_kw=dict(lw=1.0),
                    label="Share punishing, passers ($n=%d$)" % len(passers)
                    if first else None)
        if beliefs is None:
            ax.text(x + offs["avg"], 0.022, f"{m[c]:.2f}", ha="center",
                    color="white", fontsize=8, fontweight="bold")
            ax2.text(x + offs["share"], 3.0, f"{sh[c]:.0%}", ha="center",
                     color="white", fontsize=8, fontweight="bold")
    ax.set_ylabel("Average punishment (£)", color=GREEN)
    ax.tick_params(axis="y", labelcolor=GREEN)
    ax.set_ylim(0, 1.0 if beliefs is not None else 0.8)
    ax2.set_ylabel("Share imposing punishment (%)", color=GOLD)
    ax2.tick_params(axis="y", labelcolor=GOLD)
    ax2.set_ylim(0, 100)
    ax.set_xticks(xs)
    ax.set_xticklabels(TICKS, fontsize=9)
    ax.text((xs[0] + xs[1]) / 2, -0.122, "Good outcome", ha="center",
            transform=ax.get_xaxis_transform(), fontsize=10)
    ax.text((xs[2] + xs[3]) / 2, -0.122, "Bad outcome", ha="center",
            transform=ax.get_xaxis_transform(), fontsize=10)
    ax.spines["top"].set_visible(False)
    ax2.spines["top"].set_visible(False)

    if annotate:
        for x1, x2, y in [(0, 1.0, 0.46), (2.6, 3.6, 0.70)]:
            ax.plot([x1, x1, x2, x2], [y, y + 0.02, y + 0.02, y],
                    color="black", lw=0.9)
            ax.text((x1 + x2) / 2, y + 0.028, "n.s.", ha="center", fontsize=8.5)
        g_avg = (m["punish_del_good"] + m["punish_nodel_good"]) / 2
        b_avg = (m["punish_del_bad"] + m["punish_nodel_bad"]) / 2
        # zorder 0.5 puts the group-mean lines behind the bars
        ax.plot([-0.38, 1.8], [g_avg, g_avg], color=GREEN, lw=1.2,
                ls=(0, (4, 2)), zorder=0.5)
        ax.plot([1.8, 3.98], [b_avg, b_avg], color=GREEN, lw=1.2,
                ls=(0, (4, 2)), zorder=0.5)
        ax.annotate("", xy=(1.8, b_avg), xytext=(1.8, g_avg),
                    arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.4))
        ax.text(1.73, (g_avg + b_avg) / 2, f"+£{b_avg - g_avg:.2f}***",
                ha="right", va="center", fontsize=9, color=GREEN)

    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=8.5, loc="upper left", frameon=False)
    fig.tight_layout()
    fig.savefig(save_to, bbox_inches="tight", dpi=200)
    plt.close(fig)
    return m, sh


def main() -> None:
    e = load_evaluator()
    d = load_delegator()
    pun_full = e[e["treat"] == 0]
    pun_pass = pun_full[pun_full["pass_att2"] == 1]
    hypo_full = e[e["treat"] == 1]
    hypo_pass = hypo_full[hypo_full["pass_att2"] == 1]
    dg_nop = d[d["treat"] == 1]

    m, sh = draw_figure(pun_full, FIGURES / "punishment.png", annotate=True)
    draw_figure(pun_pass, FIGURES / "punishment_passers.png", annotate=False)
    draw_figure(hypo_full, FIGURES / "punishment_hypothetical.png",
                annotate=False, beliefs=dg_nop, n_bel=len(dg_nop),
                passers=hypo_pass)

    # Outcome-difference statistics (paired, subject level)
    amt_good = (pun_full["punish_del_good"] + pun_full["punish_nodel_good"]) / 2
    amt_bad = (pun_full["punish_del_bad"] + pun_full["punish_nodel_bad"]) / 2
    _, p_outcome = stats.ttest_rel(amt_bad, amt_good)
    _, p_good_pair = stats.ttest_rel(pun_full["punish_del_good"],
                                     pun_full["punish_nodel_good"])
    _, p_bad_pair = stats.ttest_rel(pun_full["punish_del_bad"],
                                    pun_full["punish_nodel_bad"])
    # Hypothetical punishment (No-Punishment condition): same pair tests
    _, p_hypo_good = stats.ttest_rel(hypo_full["punish_del_good"],
                                     hypo_full["punish_nodel_good"])
    _, p_hypo_bad = stats.ttest_rel(hypo_full["punish_del_bad"],
                                    hypo_full["punish_nodel_bad"])

    # Non-parametric counterparts for every paired comparison above
    p_outcome_w = paired_wilcoxon(amt_bad, amt_good)
    p_good_pair_w = paired_wilcoxon(pun_full["punish_del_good"],
                                    pun_full["punish_nodel_good"])
    p_bad_pair_w = paired_wilcoxon(pun_full["punish_del_bad"],
                                   pun_full["punish_nodel_bad"])
    p_hypo_good_w = paired_wilcoxon(hypo_full["punish_del_good"],
                                    hypo_full["punish_nodel_good"])
    p_hypo_bad_w = paired_wilcoxon(hypo_full["punish_del_bad"],
                                   hypo_full["punish_nodel_bad"])

    out = {}
    for c in KEYS:
        out[f"fig_pun_actual_{c}_mean"] = round(float(m[c]), 4)
        out[f"fig_pun_actual_{c}_punish_share"] = round(float(sh[c]), 4)
    out.update({
        "fig_pun_good_outcome_avg": round(float(amt_good.mean()), 4),
        "fig_pun_bad_outcome_avg": round(float(amt_bad.mean()), 4),
        "fig_pun_outcome_diff": round(float(amt_bad.mean() - amt_good.mean()), 4),
        "fig_pun_outcome_diff_paired_p": round(float(p_outcome), 5),
        "fig_pun_good_pair_paired_p": round(float(p_good_pair), 4),
        "fig_pun_bad_pair_paired_p": round(float(p_bad_pair), 4),
        "fig_pun_outcome_diff_wilcoxon_p": round(p_outcome_w, 5),
        "fig_pun_good_pair_wilcoxon_p": round(p_good_pair_w, 4),
        "fig_pun_bad_pair_wilcoxon_p": round(p_bad_pair_w, 4),
    })
    for c in KEYS:
        out[f"fig_pun_hypo_{c}_mean"] = round(float(hypo_full[c].mean()), 4)
    out.update({
        "fig_pun_hypo_good_pair_paired_p": round(float(p_hypo_good), 4),
        "fig_pun_hypo_bad_pair_paired_p": round(float(p_hypo_bad), 4),
        "fig_pun_hypo_good_pair_wilcoxon_p": round(p_hypo_good_w, 4),
        "fig_pun_hypo_bad_pair_wilcoxon_p": round(p_hypo_bad_w, 4),
    })
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
