"""One-off: exploratory views of the punishment distribution across the four cells.

Produces four PNGs + a markdown viewer in quality_reports/:
  punishment_dist_ecdf.png    -- per-cell ECDFs (independent), by outcome
  punishment_dist_hist.png    -- per-cell histograms (2x2)
  punishment_dist_diff.png    -- within-subject difference (self - delegated), by outcome
  punishment_dist_scatter.png -- paired scatter (self vs delegated), by outcome
Full Punishment-condition sample (treat == 0, n = 80).
"""
from __future__ import annotations
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
QR = os.path.join(ROOT, "quality_reports")
e = pd.read_parquet(os.path.join(ROOT, "data", "clean", "evaluator_cleaned.parquet"))
p = e[e["treat"] == 0]
dg, db = p["punish_del_good"], p["punish_del_bad"]
sg, sb = p["punish_nodel_good"], p["punish_nodel_bad"]

C_DEL, C_SELF = "#4F6EC4", "#C4A54F"


def ecdf_step(ax, data, **kw):
    x = np.sort(data.values)
    y = np.arange(1, len(x) + 1) / len(x)
    ax.step(np.concatenate([[0], x, [2]]), np.concatenate([[0], y, [1]]), where="post", lw=2, **kw)


# --- 1. ECDFs -------------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for a, (self_, del_, title) in zip(ax, [(sg, dg, "Good outcome"), (sb, db, "Bad outcome")]):
    ecdf_step(a, self_, color=C_SELF, label="Self-decided")
    ecdf_step(a, del_, color=C_DEL, label="Delegated")
    a.set_title(title); a.set_xlabel("Punishment (£)"); a.set_xlim(0, 2); a.set_ylim(0, 1)
    a.spines[["top", "right"]].set_visible(False)
ax[0].set_ylabel("Cumulative share of Player Bs")
ax[0].legend(frameon=False, loc="lower right")
fig.tight_layout(); fig.savefig(os.path.join(QR, "punishment_dist_ecdf.png"), dpi=150, bbox_inches="tight"); plt.close(fig)

# --- 2. Histograms (2x2) --------------------------------------------------
fig, ax = plt.subplots(2, 2, figsize=(10, 6.5), sharex=True, sharey=True)
bins = np.arange(-0.05, 2.15, 0.1)
for a, (d, title, c) in zip(ax.flat, [(dg, "Delegated, Good", C_DEL), (db, "Delegated, Bad", C_DEL),
                                      (sg, "Self-decided, Good", C_SELF), (sb, "Self-decided, Bad", C_SELF)]):
    a.hist(d, bins=bins, color=c, edgecolor="white", linewidth=0.3)
    a.set_title(title); a.spines[["top", "right"]].set_visible(False)
for a in ax[-1]:
    a.set_xlabel("Punishment (£)")
for a in ax[:, 0]:
    a.set_ylabel("Number of Player Bs")
fig.tight_layout(); fig.savefig(os.path.join(QR, "punishment_dist_hist.png"), dpi=150, bbox_inches="tight"); plt.close(fig)

# --- 3. Within-subject difference (self - delegated) ----------------------
fig, ax = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
bins = np.arange(-2.05, 2.15, 0.1)
for a, (self_, del_, title) in zip(ax, [(sg, dg, "Good outcome"), (sb, db, "Bad outcome")]):
    diff = (self_ - del_).dropna()
    a.hist(diff, bins=bins, color="#6E8B6E", edgecolor="white", linewidth=0.3)
    a.axvline(0, color="gray", ls="--", lw=1)
    npos, nneg, nzero = int((diff > 0).sum()), int((diff < 0).sum()), int((diff == 0).sum())
    a.set_title(f"{title}\nmean = £{diff.mean():.3f};  self>del: {npos},  self<del: {nneg},  equal: {nzero}",
                fontsize=9)
    a.set_xlabel("Self-decided $-$ Delegated punishment (£)"); a.set_xlim(-2, 2)
    a.spines[["top", "right"]].set_visible(False)
ax[0].set_ylabel("Number of Player Bs")
fig.tight_layout(); fig.savefig(os.path.join(QR, "punishment_dist_diff.png"), dpi=150, bbox_inches="tight"); plt.close(fig)

# --- 4. Paired scatter (self vs delegated) --------------------------------
rng = np.random.RandomState(0)
def jit(v):
    return v.values + rng.uniform(-0.03, 0.03, len(v))
fig, ax = plt.subplots(1, 2, figsize=(9.5, 4.7), sharex=True, sharey=True)
for a, (self_, del_, title) in zip(ax, [(sg, dg, "Good outcome"), (sb, db, "Bad outcome")]):
    a.plot([0, 2], [0, 2], color="gray", ls="--", lw=1, zorder=1)
    a.scatter(jit(self_), jit(del_), s=28, alpha=0.45, color=C_DEL, edgecolor="none", zorder=2)
    a.set_title(title); a.set_xlabel("Self-decided punishment (£)")
    a.set_xlim(-0.1, 2.1); a.set_ylim(-0.1, 2.1); a.set_aspect("equal")
    a.spines[["top", "right"]].set_visible(False)
ax[0].set_ylabel("Delegated punishment (£)")
ax[0].text(1.4, 0.15, "below line:\nself > delegated", fontsize=8, color="gray")
fig.tight_layout(); fig.savefig(os.path.join(QR, "punishment_dist_scatter.png"), dpi=150, bbox_inches="tight"); plt.close(fig)

md = """# Punishment distribution across the four scenarios (exploratory)

Full Punishment-condition sample (Player B, `treat == 0`, n = 80). Four ways to show it.

## 1. Per-cell ECDFs (treating cells as independent)
Cumulative distribution of punishment in each cell, by outcome. The height at £0 is the
share who punish nothing; curve separation shows the outcome effect; the near-overlap of
Self vs Delegated within each panel is the null.

![ECDF](punishment_dist_ecdf.png)

## 2. Per-cell histograms
The literal distribution in each of the four cells. The spike at £0 (the non-punishers)
dominates every panel.

![Histograms](punishment_dist_hist.png)

## 3. Within-subject difference, self − delegated (measured together)
Per Player B, the gap between self-made and delegated punishment, by outcome. A spike at 0
(subjects who punish identically) with roughly symmetric tails = the paired null.

![Differences](punishment_dist_diff.png)

## 4. Paired scatter, self vs delegated (measured together)
Each Player B is one point (jittered); the dashed line is equality. Points below the line
punish self-made decisions more; symmetry about the line = no insulation. The blob at the
origin is the non-punishers.

![Scatter](punishment_dist_scatter.png)
"""
with open(os.path.join(QR, "punishment_distributions.md"), "w", encoding="utf-8") as f:
    f.write(md)
print("done")
