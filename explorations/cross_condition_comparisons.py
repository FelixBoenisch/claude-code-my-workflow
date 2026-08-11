"""Cross-condition comparisons: A's beliefs and B's punishment (preview only)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "python"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats

from lib.io import load_delegator, load_evaluator

KEYS = ["del_good", "nodel_good", "del_bad", "nodel_bad"]
TICKS = ["Delegated", "Self-decided", "Delegated", "Self-decided"]
BLUE = {0: "#3b6ea8", 1: "#8aacd1"}   # dark = Punishment, light = No-Punishment
X = [0, 1.0, 2.6, 3.6]
W = 0.345
OUT = r"c:\Users\USER\Documents\Test environment\paper\explorations\figs"


def draw(df, prefix, labels, ymax, save_to):
    g = {t: df[df["treat"] == t] for t in (0, 1)}
    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    for x, c in zip(X, KEYS):
        col = f"{prefix}_{c}"
        first = x == 0
        for t in (0, 1):
            m, s = g[t][col].mean(), g[t][col].sem()
            ax.bar(x + (t - 0.5) * W, m, width=W, yerr=s, capsize=3,
                   color=BLUE[t], error_kw=dict(lw=1.1),
                   label=f"{labels[t]} ($n={len(g[t])}$)" if first else None)
            ax.text(x + (t - 0.5) * W, 0.02 * ymax, f"{m:.2f}", ha="center",
                    color="white", fontsize=8, fontweight="bold")
    ax.set_ylabel("Average punishment (£)")
    ax.set_ylim(0, ymax)
    ax.set_xticks(X)
    ax.set_xticklabels(TICKS, fontsize=9)
    ax.text(0.5, -0.122, "Good outcome", ha="center",
            transform=ax.get_xaxis_transform(), fontsize=10)
    ax.text(3.1, -0.122, "Bad outcome", ha="center",
            transform=ax.get_xaxis_transform(), fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    fig.tight_layout()
    fig.savefig(save_to, bbox_inches="tight", dpi=200)
    plt.close(fig)


def tests(df, prefix, label):
    print(f"--- {label}")
    for c in KEYS + ["avg"]:
        if c == "avg":
            a = df[df["treat"] == 0][[f"{prefix}_{k}" for k in KEYS]].mean(axis=1)
            b = df[df["treat"] == 1][[f"{prefix}_{k}" for k in KEYS]].mean(axis=1)
        else:
            a = df[df["treat"] == 0][f"{prefix}_{c}"]
            b = df[df["treat"] == 1][f"{prefix}_{c}"]
        t, p = stats.ttest_ind(a, b)
        u = stats.mannwhitneyu(a, b, alternative="two-sided")
        print(f"{c:12s} P {a.mean():.3f}  NP {b.mean():.3f}  "
              f"t p={p:.3f}  MWU p={u.pvalue:.3f}")


d = load_delegator()
e = load_evaluator()
draw(d, "belief", {0: "Punishment", 1: "No-Punishment (hypothetical)"}, 1.15,
     OUT + r"\comp_beliefs_conditions.png")
draw(e, "punish", {0: "Punishment (actual)", 1: "No-Punishment (hypothetical)"}, 0.8,
     OUT + r"\comp_punishment_conditions.png")
tests(d, "belief", "Player A beliefs, full")
tests(d[d["pass_att2"] == 1], "belief", "Player A beliefs, passers")
tests(e, "punish", "Player B punishment, full")
tests(e[e["pass_att2"] == 1], "punish", "Player B punishment, passers")
