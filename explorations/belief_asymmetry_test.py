"""C1 open flank: is Player A's delegation response to expected punishment
differentials ASYMMETRIC around zero?

Motivation (mechanisms logic map, C1 "aggregation subtlety"): a mean-zero
expected differential does not imply a zero behavioural effect if the response
is asymmetric. If Player As who expect a DELEGATION penalty react more strongly
than those who expect a KEEPING penalty, a mean-zero belief distribution still
shifts aggregate delegation down, and R3's "no aggregate push" reading is too
quick.

SIGN CONVENTION. This script uses the convention of the proposed test:

    d_i = E[punishment | delegate] - E[punishment | keep]

so d_i > 0 means Player A expects to be punished MORE for delegating (a
delegation penalty, which should push her toward keeping the decision), and
d_i < 0 means she expects to be punished more for keeping.

This is the NEGATIVE of the manuscript's variable. `22_belief_specs.py` and
Table reg_belief_specs use bel_diff = (no delegation) - (delegation), i.e.
bel_diff = -d. Coefficients here therefore carry the opposite sign to the
table; the AMEs are identical up to that flip.

Three differentials, following the paper's construction:
    d_bad      = belief_del_bad  - belief_nodel_bad          (= -nodel_del_bad)
    d_good     = belief_del_good - belief_nodel_good         (= -nodel_del_good)
    d_weighted = p*d_good + (1-p)*d_bad,  p = wa_confidence/10
    d_avg      = 0.5*(d_good + d_bad)

Four specifications, all within the Punishment condition:
    (1) Spline at zero      delegation ~ d + d*1[d>0]
    (2) Sign split          delegation ~ 1[d>0] + 1[d<0] + |d|*1[d>0] + |d|*1[d<0]
    (3) Nonparametric       binned delegation rate against d
    (4) Counterfactual      E[g(d_i)] - g(0), the delegation the asymmetry moves

Output: explorations/belief_asymmetry_test.md
        explorations/figs/belief_asymmetry_binned.png
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "python"))

from lib.io import load_delegator  # noqa: E402

OUT_MD = Path(__file__).with_suffix(".md")
FIGDIR = Path(__file__).parent / "figs"
FIGDIR.mkdir(exist_ok=True)

SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
CTRLS = ["overall_score"] + SES
MEASURES = ["d_bad", "d_weighted", "d_avg"]
LABEL = {
    "d_bad": "Bad-outcome differential",
    "d_weighted": "Probability-weighted differential",
    "d_avg": "Simple-average differential",
}
RNG = np.random.default_rng(20260820)


def build(d: pd.DataFrame) -> pd.DataFrame:
    s = d[d["treat"] == 0].copy()
    # Negative of the manuscript's bel_diff: d = delegate - keep.
    s["d_good"] = -s["nodel_del_good"]
    s["d_bad"] = -s["nodel_del_bad"]
    s["d_avg"] = 0.5 * (s["d_good"] + s["d_bad"])
    p = s["wa_confidence"] / 10.0
    s["d_weighted"] = p * s["d_good"] + (1 - p) * s["d_bad"]
    return s


def add_spline_terms(df: pd.DataFrame, m: str) -> pd.DataFrame:
    x = df[m]
    df = df.copy()
    df["d"] = x
    df["d_pos_slope"] = x * (x > 0)          # extra slope above zero
    df["pos"] = (x > 0).astype(float)
    df["neg"] = (x < 0).astype(float)
    df["mag_pos"] = x.where(x > 0, 0.0)      # magnitude on the delegation-penalty side
    df["mag_neg"] = (-x).where(x < 0, 0.0)   # magnitude on the keeping-penalty side
    return df


def fit(y, X, kind="probit"):
    X = sm.add_constant(X.astype(float), has_constant="add")
    if kind == "probit":
        return sm.Probit(y.astype(float), X).fit(disp=False, cov_type="HC1")
    return sm.OLS(y.astype(float), X).fit(cov_type="HC1")


def fmt(m, var):
    if var not in m.params.index:
        return "--"
    return f"{m.params[var]:+.3f} ({m.bse[var]:.3f}) [{m.pvalues[var]:.3f}]"


def ame_pp10(model, var):
    """AME on P(delegate) in percentage points per GBP 0.10."""
    me = model.get_margeff(at="overall", method="dydx")
    names = [n for n in model.model.exog_names if n != "const"]
    i = names.index(var)
    return 10.0 * 100.0 * float(me.margeff[i]) / 100.0, float(me.pvalues[i])


ZERO_COLS = ["d", "d_pos_slope", "pos", "neg", "mag_pos", "mag_neg"]


def _gap(mod, est, regs, zero_cols):
    Xo = sm.add_constant(est[regs].astype(float), has_constant="add")
    z = est.copy()
    for c in zero_cols:
        if c in z.columns:
            z[c] = 0.0
    Xz = sm.add_constant(z[regs].astype(float), has_constant="add")
    return float(mod.predict(Xo).mean() - mod.predict(Xz).mean())


def counterfactual(df, regs, kind="probit", B=2000, zero_cols=None):
    """E[g(d_i)] - g(0): mean predicted delegation at observed d minus at d=0.

    Bootstrap uses the LPM regardless of `kind`: probit separates on a
    non-trivial share of resamples at these cell sizes, which silently
    truncated the CI in the first version of this script.
    """
    zero_cols = zero_cols or ZERO_COLS
    est = df[["delegation"] + regs].dropna()
    if len(est) < 15:
        return None
    mod = fit(est["delegation"], est[regs], kind)
    gap = _gap(mod, est, regs, zero_cols)
    mod_l = fit(est["delegation"], est[regs], "ols")
    gap_lpm = _gap(mod_l, est, regs, zero_cols)

    boot, fails = [], 0
    for _ in range(B):
        idx = RNG.integers(0, len(est), len(est))
        bs = est.iloc[idx]
        try:
            bm = fit(bs["delegation"], bs[regs], "ols")
            boot.append(_gap(bm, bs, regs, zero_cols))
        except Exception:
            fails += 1
    lo, hi = (np.percentile(boot, [2.5, 97.5]) if len(boot) > 100 else (np.nan, np.nan))
    return dict(gap=gap, gap_lpm=gap_lpm, lo=lo, hi=hi, n=len(est),
                nboot=len(boot), fails=fails)


def main() -> None:
    d = load_delegator()
    full = build(d)
    pas = full[full["pass_att2"] == 1].copy()
    samples = [("Full Punishment", full), ("Punishment, passers", pas)]

    md = ["# Asymmetric belief response test (C1 aggregation subtlety)", "",
          "**Exploration, not a manuscript artefact.** Generated by",
          "`explorations/belief_asymmetry_test.py`.", "",
          "## Sign convention (read this first)", "",
          "This report uses the convention of the proposed test:", "",
          "```", "d_i = E[punishment | delegate] - E[punishment | keep]", "```", "",
          "`d > 0` means Player A expects a **delegation penalty** (punished more for",
          "delegating), which should push her toward keeping the decision.",
          "`d < 0` means she expects a **keeping penalty**.", "",
          "This is the **negative** of the manuscript's `bel_diff` variable in Table",
          "`reg_belief_specs`, which is defined as *(no delegation) - (delegation)*.",
          "Coefficient signs here are therefore flipped relative to that table.", "",
          "The asymmetry hypothesis: if the response to `d > 0` is steeper than the",
          "response to `d < 0`, a mean-zero belief distribution still depresses",
          "aggregate delegation, and R3's \"no aggregate push\" reading would be too",
          "quick.", ""]

    # ---------------- distribution of d ------------------------------------
    md += ["## 0. Distribution of the differential", "",
           "| Sample | Measure | N | Mean | SE | t-test mean=0 (p) | Median | Share d<0 | Share d=0 | Share d>0 |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    from scipy import stats as st
    for sname, s in samples:
        for m in MEASURES:
            x = s[m].dropna()
            t = st.ttest_1samp(x, 0)
            md.append(f"| {sname} | {LABEL[m]} | {len(x)} | {x.mean():+.4f} | {x.sem():.4f} "
                      f"| {t.pvalue:.3f} | {x.median():+.3f} | {(x<0).mean():.3f} "
                      f"| {(x==0).mean():.3f} | {(x>0).mean():.3f} |")
    md += ["", "A mean indistinguishable from zero is the premise of R3. The mass at",
           "exactly zero is large, which is what limits the power of every test below.", ""]

    # ---------------- Spec 1: spline at zero --------------------------------
    md += ["## 1. Spline at zero", "",
           "`delegation ~ d + d*1[d>0]` (+ controls). Continuous at zero with a kink.",
           "Slope below zero is the `d` coefficient; slope above zero is",
           "`d + d*1[d>0]`. **The interaction is the asymmetry.** A negative",
           "interaction means the delegation-penalty side is steeper.", "",
           "Probit coefficients, HC1 SEs: coef (SE) [p].", "",
           "| Sample | Measure | Controls | N | d | d x 1[d>0] (asymmetry) | Slope above 0 | Wald p (asym) |",
           "|---|---|---|---|---|---|---|---|"]
    for sname, s in samples:
        for m in MEASURES:
            for ctrl_lab, ctrl in [("no", []), ("yes", CTRLS)]:
                df = add_spline_terms(s, m)
                regs = ["d", "d_pos_slope"] + ctrl
                est = df[["delegation"] + regs].dropna()
                if len(est) < 20:
                    continue
                try:
                    mod = fit(est["delegation"], est[regs])
                except Exception:
                    continue
                above = mod.params["d"] + mod.params["d_pos_slope"]
                try:
                    w = mod.f_test("d_pos_slope = 0").pvalue
                except Exception:
                    w = np.nan
                md.append(f"| {sname} | {LABEL[m]} | {ctrl_lab} | {len(est)} | {fmt(mod,'d')} "
                          f"| {fmt(mod,'d_pos_slope')} | {above:+.3f} | {float(w):.3f} |")
    md.append("")

    # ---------------- Spec 2: sign split ------------------------------------
    md += ["## 2. Sign split", "",
           "`delegation ~ 1[d>0] + 1[d<0] + |d|*1[d>0] + |d|*1[d<0]` (+ controls),",
           "with `d = 0` as the reference group. Separate intercept shifts and",
           "separate magnitude slopes on each side. The comparison of interest is",
           "the two magnitude slopes: `|d| x 1[d>0]` (delegation-penalty side,",
           "expected negative) versus `|d| x 1[d<0]` (keeping-penalty side,",
           "expected positive).", "",
           "| Sample | Measure | Ctrl | N | 1[d>0] | 1[d<0] | \\|d\\| x 1[d>0] | \\|d\\| x 1[d<0] | Wald p (slopes equal in magnitude) |",
           "|---|---|---|---|---|---|---|---|---|"]
    for sname, s in samples:
        for m in MEASURES:
            for ctrl_lab, ctrl in [("no", []), ("yes", CTRLS)]:
                df = add_spline_terms(s, m)
                regs = ["pos", "neg", "mag_pos", "mag_neg"] + ctrl
                est = df[["delegation"] + regs].dropna()
                if len(est) < 20:
                    continue
                try:
                    mod = fit(est["delegation"], est[regs])
                except Exception:
                    continue
                # symmetric response => slope_pos = -slope_neg => sum = 0
                try:
                    w = mod.f_test("mag_pos + mag_neg = 0").pvalue
                except Exception:
                    w = np.nan
                md.append(f"| {sname} | {LABEL[m]} | {ctrl_lab} | {len(est)} | {fmt(mod,'pos')} "
                          f"| {fmt(mod,'neg')} | {fmt(mod,'mag_pos')} | {fmt(mod,'mag_neg')} "
                          f"| {float(w):.3f} |")
    md += ["", "Under a symmetric response the two magnitude slopes are equal and",
           "opposite, so their sum is zero. The Wald test in the last column tests",
           "exactly that restriction.", ""]

    # ---------------- Spec 3: nonparametric ---------------------------------
    md += ["## 3. Nonparametric binned response", "",
           "Delegation rate by bin of `d`. Bins are the natural GBP grid of the",
           "elicitation; cells with fewer than three subjects are shown but should",
           "not be read.", ""]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
    for ax, (sname, s) in zip(axes, samples):
        m = "d_bad"
        x = s[["delegation", m]].dropna()
        bins = [-np.inf, -0.50, -0.20, -0.001, 0.001, 0.20, 0.50, np.inf]
        labs = ["<= -0.50", "(-0.50,-0.20]", "(-0.20,0)", "= 0",
                "(0,0.20)", "[0.20,0.50)", ">= 0.50"]
        x["bin"] = pd.cut(x[m], bins=bins, labels=labs)
        g = x.groupby("bin", observed=False)["delegation"].agg(["mean", "count"])
        md.append(f"**{sname}**, bad-outcome differential:")
        md.append("")
        md.append("| Bin of d | N | Delegation rate |")
        md.append("|---|---|---|")
        for b, r in g.iterrows():
            rate = "--" if r["count"] == 0 else f"{r['mean']:.3f}"
            md.append(f"| {b} | {int(r['count'])} | {rate} |")
        md.append("")
        ok = g[g["count"] >= 1]
        ax.plot(range(len(ok)), ok["mean"], "o-", color="#3b6ea8")
        for i, (b, r) in enumerate(ok.iterrows()):
            ax.annotate(f"n={int(r['count'])}", (i, r["mean"]), textcoords="offset points",
                        xytext=(0, 8), ha="center", fontsize=7.5, color="#555")
        ax.set_xticks(range(len(ok)))
        ax.set_xticklabels(ok.index, rotation=45, ha="right", fontsize=8)
        ax.axvline(list(ok.index).index("= 0"), color="#999", ls=":", lw=1)
        ax.set_title(sname, fontsize=10)
        ax.set_ylim(0, 1)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Delegation rate")
    fig.suptitle("Delegation rate by expected punishment differential d (delegate - keep)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(FIGDIR / "belief_asymmetry_binned.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    md += ["Figure: `explorations/figs/belief_asymmetry_binned.png`.", ""]

    # ---------------- Spec 4: counterfactual --------------------------------
    md += ["## 4. Counterfactual: how much delegation does the asymmetry move?", "",
           "Integrate the fitted response over the observed `d` distribution and",
           "compare with the same subjects evaluated at `d = 0`:", "",
           "```", "gap = mean_i[ g(d_i, X_i) ] - mean_i[ g(0, X_i) ]", "```", "",
           "Under a symmetric (linear) response with mean-zero `d`, the gap is zero",
           "by construction. A non-zero gap is the aggregate delegation shift that",
           "the asymmetry produces. **Benchmark: the treatment effect to be",
           "explained is 16.8 pp.** Point estimates from probit and LPM; 95% CI from",
           "2000 LPM bootstrap draws (probit separates on a non-trivial share of",
           "resamples at these cell sizes).", "",
           "The **spline** row is the one to read for the asymmetry question: the",
           "spline is continuous at zero, so its gap reflects only curvature of the",
           "response. The **sign-split** row additionally absorbs the two intercept",
           "dummies, so it also contains a pure \"holds any non-zero belief\" level",
           "effect that has nothing to do with asymmetry. The last row per block",
           "isolates that by zeroing only the magnitude slopes.", "",
           "| Sample | Measure | Spec | N | Gap probit (pp) | Gap LPM (pp) | 95% CI (pp) | Share of 16.8 pp |",
           "|---|---|---|---|---|---|---|---|"]
    for sname, s in samples:
        for m in MEASURES:
            specs = [
                ("spline", ["d", "d_pos_slope"], None),
                ("sign split (total)", ["pos", "neg", "mag_pos", "mag_neg"], None),
                ("sign split (slopes only)", ["pos", "neg", "mag_pos", "mag_neg"],
                 ["mag_pos", "mag_neg"]),
            ]
            for spec_lab, regs, zc in specs:
                df = add_spline_terms(s, m)
                r = counterfactual(df, regs, "probit", zero_cols=zc)
                if r is None:
                    continue
                share = 100 * r["gap"] / 0.168
                ci = ("--" if np.isnan(r["lo"])
                      else f"[{100*r['lo']:+.2f}, {100*r['hi']:+.2f}]")
                md.append(f"| {sname} | {LABEL[m]} | {spec_lab} | {r['n']} "
                          f"| {100*r['gap']:+.2f} | {100*r['gap_lpm']:+.2f} | {ci} "
                          f"| {share:+.1f}% |")
    md += ["", "## Reading", "",
           "**1. The asymmetry hypothesis is not supported, and the one hint of an",
           "asymmetry runs the wrong way.**", "",
           "The map's conjecture was that subjects expecting a *delegation* penalty",
           "(`d > 0`) react more strongly than those expecting a *keeping* penalty",
           "(`d < 0`), so that a mean-zero belief distribution would still depress",
           "aggregate delegation and rescue C1. The data point the other way. In the",
           "only cell where anything reaches conventional significance (passers,",
           "probability-weighted, with controls), the response is concentrated",
           "entirely on the keeping-penalty side:", "",
           "| Side | Sign-split slope | p |",
           "|---|---|---|",
           "| Delegation penalty, `\\|d\\| x 1[d>0]` | -0.03 | 0.976 |",
           "| Keeping penalty, `\\|d\\| x 1[d<0]` | +3.65 | 0.017 |", "",
           "Wald test of symmetry (slopes equal and opposite): p = 0.059. The spline",
           "tells the same story: slope -3.20 below zero (p = 0.005), essentially flat",
           "above it (-0.48), interaction p = 0.097.", "",
           "Subjects who expect to be punished more for keeping the decision do",
           "delegate more, and steeply. Subjects who expect to be punished more for",
           "delegating do not visibly hold back. If that is real, the belief",
           "distribution pushes delegation *up* under Punishment, not down, which",
           "makes Result 1 harder to explain rather than easier.", "",
           "**2. Do not lean on it: this is one cell in twelve.**", "",
           "Twelve specification cells were run (2 samples x 3 measures x 2 control",
           "sets). Exactly one clears p < 0.10 on the symmetry test. That is",
           "approximately what twelve independent draws would produce by chance, and",
           "the cell that does clear is the smallest one (n = 60) with the most",
           "parameters (11). Every uncontrolled specification, and every",
           "specification on the bad-outcome differential, returns a flat null",
           "(p between 0.20 and 0.99).", "",
           "**3. The counterfactual is small and its sign is unstable.**", "",
           "Reading the spline row, which is the one that isolates curvature, the gap",
           "between the observed belief distribution and a `d = 0` world ranges from",
           "-1.3 pp to +3.6 pp across measures and samples. Every bootstrap CI covers",
           "zero and spans roughly +/-10 pp. Against the 16.8 pp to be explained, the",
           "channel is somewhere between negligible and modest, and the point",
           "estimates change sign depending on the belief measure.", "",
           "**4. A separate pattern worth noticing (not asymmetry).**", "",
           "In the sign-split specifications both intercept dummies are positive and",
           "similar in size (around +0.5 to +0.65 in the uncontrolled full sample),",
           "meaning subjects holding *any* non-zero differential delegate more than",
           "the 30-36% who report exactly zero, regardless of which way their",
           "differential points. This is what drives the large +9 pp \"sign split",
           "(total)\" gaps, and it is a level effect, not an asymmetry. It is also",
           "not individually significant (p > 0.15). Most plausibly it reflects",
           "engagement: subjects who thought about the punishment cells at all differ",
           "from those who reported a flat zero. Worth a sentence if you ever use",
           "this material, but it is not evidence for C1.", "",
           "**Bottom line.** The aggregation subtlety does not save anticipated",
           "differential punishment. R3's \"no aggregate push\" reading survives this",
           "test. The flank the map flagged as \"unexplored\" can now be marked",
           "explored and closed, with the caveat that power is genuinely poor and the",
           "one directional hint present runs against C1 rather than for it.", "",
           "## Caveats (state with any result)", "",
           "1. **Within-Punishment.** This explains the delegation *level* under",
           "   Punishment relative to a `d = 0` benchmark. Treating No-Punishment",
           "   delegation as that benchmark is an assumption, not a measurement.",
           "2. **Post-decision, unincentivized beliefs.** Reverse causality is live:",
           "   subjects may rationalize the choice they already made. The test is",
           "   suggestive, not identifying.",
           "3. **Power.** The Punishment sample is 80 subjects (61 passers), and a",
           "   large share sit at exactly `d = 0`, so each side of the split is thin.",
           "   Absence of a detected asymmetry is weak evidence of its absence.", ""]

    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print("written:", OUT_MD)


if __name__ == "__main__":
    main()
