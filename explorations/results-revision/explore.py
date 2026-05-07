"""Ad-hoc analyses for the paragraph-by-paragraph revision of results.tex.

Each section below corresponds to one paragraph in the revised results section,
numbered to match the planning files in quality_reports/results_revision/.

Run the whole script, or just the section for the paragraph you're working on.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_PYTHON = REPO_ROOT / "scripts" / "python"
if str(SCRIPTS_PYTHON) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_PYTHON))

from lib.io import load_delegator, load_evaluator  # noqa: E402

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def main() -> None:
    d = load_delegator()
    e = load_evaluator()
    print(f"delegator: {d.shape[0]} rows, {d.shape[1]} cols")
    print(f"evaluator: {e.shape[0]} rows, {e.shape[1]} cols")

    # --- P01: sample paragraph -----------------------------------------------
    # No exploratory code; numeric checks done directly against numbers.json.

    # --- P02: H1 introduction ------------------------------------------------
    # No exploratory code; numeric checks done directly against numbers.json.

    # --- P03: With Controls table — 12-column logit redesign ---------------
    p03_with_controls_table(d)
    # --- P03b: same 12 specs restricted to attention-check passers ---------
    p03_with_controls_table(d.loc[d["pass_att2"] == 1].copy(), sample_label="ATTENTION-CHECK PASSERS (pass_att2==1)")
    # --- P03c: focused 5-column table as described in results.tex L24 ------
    p03c_with_controls_focused(d)
    # --- P04: average punishment in the four cells, full vs passers --------
    p04_punishment_cells(e)
    # --- P05: extra Player B analyses for the subsection plan ---------------
    p05_punishment_subsection(d, e)


def p03c_with_controls_focused(d):
    """The five-column table described in results.tex L24 (revised column 4/5).

    (1) Unconditional:           treat
    (2) + SES:                   treat + SES
    (3) + Actual performance:    treat + SES + overall_score
    (4) + Perceived performance: treat + SES + wa_confidence       (NO overall_score)
    (5) Passers, actual perf:    treat + SES + overall_score, pass_att2 == 1
    """
    import statsmodels.api as sm

    SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]

    def fit(y, X):
        X = sm.add_constant(X, has_constant="add")
        return sm.Logit(y.astype(float), X.astype(float)).fit(disp=False, cov_type="HC1")

    specs = [
        ("(1) Unconditional",        ["treat"], False),
        ("(2) + SES",                ["treat"] + SES, False),
        ("(3) + Actual perf",        ["treat"] + SES + ["overall_score"], False),
        ("(4) + Perceived perf",     ["treat"] + SES + ["wa_confidence"], False),
        ("(5) Passers + Actual",     ["treat"] + SES + ["overall_score"], True),
    ]

    print("\n" + "=" * 70)
    print("P03c: Focused 5-column table (matching results.tex L24)")
    print("=" * 70)

    fits = []
    for name, regs, restrict in specs:
        sample = d.loc[d["pass_att2"] == 1].copy() if restrict else d
        sub = sample[["delegation"] + regs].dropna()
        m = fit(sub["delegation"], sub[regs])
        n = len(sub)
        coef = float(m.params["treat"])
        se = float(m.bse["treat"])
        p = float(m.pvalues["treat"])
        ame = float(m.get_margeff(at="overall", method="dydx").margeff[0])
        ame_p = float(m.get_margeff(at="overall", method="dydx").pvalues[0])
        r2 = float(m.prsquared)
        print(
            f"{name:<24}  N={n:>3}  coef={coef:+.4f}  SE={se:.4f}  "
            f"p={p:.4f}  AME={ame:+.4f} (p={ame_p:.4f})  pseudo-R^2={r2:.4f}"
        )
        fits.append((name, regs, m, n))

    # Markdown table — every coefficient
    print("\n--- Full 5-column table (markdown) ---")
    var_order = ["treat", "overall_score", "wa_confidence",
                 "age", "female", "socio_status", "went_to_uni",
                 "technology_score", "leader", "const"]
    headers = ["Variable"] + [name for name, _, _, _ in fits]
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---:"] * len(headers)) + "|")
    for var in var_order:
        coef_row = [var]
        se_row = [""]
        for _, _, m, _ in fits:
            if var in m.params.index:
                c = float(m.params[var])
                se = float(m.bse[var])
                p = float(m.pvalues[var])
                coef_row.append(f"${c:+.3f}$ ($p={p:.3f}$)")
                se_row.append(f"$({se:.3f})$")
            else:
                coef_row.append("")
                se_row.append("")
        print("| " + " | ".join(coef_row) + " |")
        print("| " + " | ".join(se_row) + " |")
    n_row = ["N"] + [f"${n}$" for _, _, _, n in fits]
    r2_row = ["Pseudo $R^2$"] + [f"${m.prsquared:.3f}$" for _, _, m, _ in fits]
    ame_row = ["AME on `treat` (pp)"] + [
        f"${100*float(m.get_margeff(at='overall', method='dydx').margeff[0]):+.1f}$ ($p={float(m.get_margeff(at='overall', method='dydx').pvalues[0]):.3f}$)"
        for _, _, m, _ in fits
    ]
    print("| " + " | ".join(n_row) + " |")
    print("| " + " | ".join(r2_row) + " |")
    print("| " + " | ".join(ame_row) + " |")


def p03_with_controls_table(d, sample_label="FULL SAMPLE"):
    """Logit specifications for the With-Controls paragraph (12 in total).

    (1)  Unconditional:                     treat
    (2)  + SES:                             treat + SES
    (3)  + Performance:                     treat + perf
    (4)  Full (Performance + SES):          treat + perf + SES
    (5)  Risk only:                         treat + switching_point
    (6)  Risk + Performance + SES:          treat + switching_point + perf + SES
    (7)  Order only:                        treat + random_order_del
    (8)  Order + Performance + SES:         treat + random_order_del + perf + SES
    (9)  Overconfidence only:               treat + overconfidence
    (10) Overconfidence + Performance + SES:treat + overconfidence + perf + SES
    (11) wa_confidence only:                treat + wa_confidence
    (12) wa_confidence + Performance + SES: treat + wa_confidence + perf + SES

    SES vector: age, female, socio_status, went_to_uni, technology_score, leader
    """
    import statsmodels.api as sm

    SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
    PERF = ["overall_score"]

    def fit(y, X):
        X = sm.add_constant(X, has_constant="add")
        return sm.Logit(y.astype(float), X.astype(float)).fit(disp=False, cov_type="HC1")

    specs = [
        ("(1) Unconditional",                 ["treat"]),
        ("(2) + SES",                         ["treat"] + SES),
        ("(3) + Performance",                 ["treat"] + PERF),
        ("(4) Full",                          ["treat"] + PERF + SES),
        ("(5) Risk only",                     ["treat", "switching_point"]),
        ("(6) Risk + Perf + SES",             ["treat", "switching_point"] + PERF + SES),
        ("(7) Order only",                    ["treat", "random_order_del"]),
        ("(8) Order + Perf + SES",            ["treat", "random_order_del"] + PERF + SES),
        ("(9) Overconf only",                 ["treat", "overconfidence"]),
        ("(10) Overconf + Perf + SES",        ["treat", "overconfidence"] + PERF + SES),
        ("(11) WA-conf only",                 ["treat", "wa_confidence"]),
        ("(12) WA-conf + Perf + SES",         ["treat", "wa_confidence"] + PERF + SES),
    ]

    print("\n" + "=" * 70)
    print(f"P03: With-Controls table — 12 logit specifications [{sample_label}]")
    print("=" * 70)
    fits = []
    for name, regs in specs:
        sub = d[["delegation"] + regs].dropna()
        m = fit(sub["delegation"], sub[regs])
        n = len(sub)
        coef = float(m.params["treat"])
        se = float(m.bse["treat"])
        p = float(m.pvalues["treat"])
        r2 = float(m.prsquared)
        ame = float(m.get_margeff(at="overall", method="dydx").margeff[0])
        ame_p = float(m.get_margeff(at="overall", method="dydx").pvalues[0])
        print(
            f"{name:<28}  N={n:>3}  coef={coef:+.4f}  SE={se:.4f}  "
            f"p={p:.4f}  AME={ame:+.4f} (p={ame_p:.4f})  pseudo-R^2={r2:.4f}"
        )
        fits.append((name, regs, m, n))

    # Full coefficient table — every variable, every spec — markdown
    print("\n--- Full 12-spec table (markdown) ---")
    var_order = ["treat", "overall_score", "switching_point", "random_order_del",
                 "overconfidence", "wa_confidence",
                 "age", "female", "socio_status", "went_to_uni",
                 "technology_score", "leader", "const"]

    headers = ["Variable"] + [name for name, _, _, _ in fits]
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---:"] * (len(headers))) + "|")
    for var in var_order:
        coef_row = [var]
        se_row = [""]
        for _, _, m, _ in fits:
            if var in m.params.index:
                c = float(m.params[var])
                se = float(m.bse[var])
                p = float(m.pvalues[var])
                coef_row.append(f"${c:+.3f}$ ($p={p:.3f}$)")
                se_row.append(f"$({se:.3f})$")
            else:
                coef_row.append("")
                se_row.append("")
        print("| " + " | ".join(coef_row) + " |")
        print("| " + " | ".join(se_row) + " |")
    n_row = ["N"] + [f"${n}$" for _, _, _, n in fits]
    r2_row = ["Pseudo $R^2$"] + [f"${m.prsquared:.3f}$" for _, _, m, _ in fits]
    ame_row = ["AME on `treat` (pp)"] + [
        f"${100*float(m.get_margeff(at='overall', method='dydx').margeff[0]):+.1f}$"
        for _, _, m, _ in fits
    ]
    print("| " + " | ".join(n_row) + " |")
    print("| " + " | ".join(r2_row) + " |")
    print("| " + " | ".join(ame_row) + " |")


def p04_punishment_cells(e):
    """Average punishment in the four (delegation, outcome) cells.

    Punishment-condition only (treat==0), since No-Punishment values are
    hypothetical. Reports cell means / SDs / share of zeros / N for the
    full sample and for the pass_att2==1 subsample.
    """
    import numpy as np
    from scipy import stats

    pun = e.loc[e["treat"] == 0].copy()
    pun_pass = pun.loc[pun["pass_att2"] == 1].copy()
    cells = [
        ("Delegated, good outcome",   "punish_del_good"),
        ("Delegated, bad outcome",    "punish_del_bad"),
        ("Self-decided, good outcome","punish_nodel_good"),
        ("Self-decided, bad outcome", "punish_nodel_bad"),
    ]

    def summarize(df, label):
        print("\n" + "-" * 70)
        print(f"P04: punishment cells — {label} (N = {len(df)})")
        print("-" * 70)
        print(f"{'Cell':<32}  {'Mean':>7}  {'SD':>6}  {'Median':>7}  {'%zero':>6}  {'t vs 0 p':>10}")
        rows = []
        for name, col in cells:
            x = df[col].dropna()
            mean = float(x.mean())
            sd = float(x.std())
            med = float(x.median())
            zero_share = float((x == 0).mean()) * 100
            t_stat, t_p = stats.ttest_1samp(x, 0.0)
            wilcox = stats.wilcoxon(x - 0.0) if (x != 0).any() else (None, None)
            print(f"  {name:<30}  {mean:7.3f}  {sd:6.3f}  {med:7.3f}  {zero_share:5.1f}%  {t_p:10.4g}")
            rows.append({
                "cell": name, "col": col, "mean": mean, "sd": sd, "median": med,
                "zero_share_pct": zero_share, "n": int(x.notna().sum()),
                "t_p_vs_zero": float(t_p),
            })
        return rows

    full_rows = summarize(pun, "Full sample (Punishment, treat==0)")
    pass_rows = summarize(pun_pass, "Attention-check passers (treat==0 & pass_att2==1)")

    # Within-subject comparisons (delegation effect, conditional on outcome)
    print("\n" + "-" * 70)
    print("Within-subject delegation effect, conditional on outcome (paired tests)")
    print("-" * 70)
    for label, df in [("Full (N=80)", pun), ("Passers (N=67)", pun_pass)]:
        for outcome, c_del, c_self in [
            ("good outcome", "punish_del_good",  "punish_nodel_good"),
            ("bad outcome",  "punish_del_bad",   "punish_nodel_bad"),
        ]:
            x = df[[c_del, c_self]].dropna()
            diff = x[c_self] - x[c_del]  # self minus delegated; positive => H2 (self punished more)
            t_p = stats.ttest_rel(x[c_self], x[c_del]).pvalue
            try:
                w_p = stats.wilcoxon(x[c_self], x[c_del], zero_method="wilcox").pvalue
            except ValueError:
                w_p = float("nan")
            print(f"  {label:<14}  {outcome:<12}  mean(self - del) = {diff.mean():+.4f}  "
                  f"paired t-test p={t_p:.4f}  Wilcoxon p={w_p:.4f}  N={len(x)}")

    # Markdown table
    print("\n--- Cell means (markdown) ---")
    print("| Cell | Full (N=80) | Passers (N=67) |")
    print("|---|---:|---:|")
    for f, p in zip(full_rows, pass_rows):
        print(f"| {f['cell']} | £{f['mean']:.3f} (SD {f['sd']:.3f}, {f['zero_share_pct']:.1f}% zero) "
              f"| £{p['mean']:.3f} (SD {p['sd']:.3f}, {p['zero_share_pct']:.1f}% zero) |")


def p05_punishment_subsection(d, e):
    """Extra analyses for the Player-B subsection plan (results.tex L28-65)."""
    import numpy as np
    import pandas as pd
    import statsmodels.api as sm
    from scipy import stats

    SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]

    pun_full = e.loc[e["treat"] == 0].copy()
    pun_pass = pun_full.loc[pun_full["pass_att2"] == 1].copy()

    print("\n" + "=" * 70)
    print("P05a: outcome effect (bad - good) within subject")
    print("=" * 70)
    for label, df in [("Full (N=80)", pun_full), ("Passers (N=67)", pun_pass)]:
        for delegated, c_good, c_bad in [
            ("delegated", "punish_del_good",  "punish_del_bad"),
            ("self-made", "punish_nodel_good","punish_nodel_bad"),
        ]:
            x = df[[c_good, c_bad]].dropna()
            diff = x[c_bad] - x[c_good]
            t_p = stats.ttest_rel(x[c_bad], x[c_good]).pvalue
            try:
                w_p = stats.wilcoxon(x[c_bad], x[c_good], zero_method="wilcox").pvalue
            except ValueError:
                w_p = float("nan")
            print(f"  {label:<14}  {delegated:<10}  mean(bad-good)={diff.mean():+.4f}  "
                  f"t={t_p:.4f}  Wilcoxon={w_p:.4f}  N={len(x)}")

    print("\n" + "=" * 70)
    print("P05b: never-punish breakdown")
    print("=" * 70)
    for label, df in [("Full (N=80)", pun_full), ("Passers (N=67)", pun_pass)]:
        cells = ["punish_del_good", "punish_del_bad", "punish_nodel_good", "punish_nodel_bad"]
        zeros_per_subject = (df[cells] == 0).sum(axis=1)
        n_total = len(df)
        for k in range(5):
            n_k = (zeros_per_subject == k).sum()
            print(f"  {label:<14}  exactly {k} cells punished zero: {n_k:3d}  ({100*n_k/n_total:5.1f}%)")
        any_pos = (df[cells].max(axis=1) > 0).sum()
        all_zero = (df[cells].max(axis=1) == 0).sum()
        small_max = ((df[cells].max(axis=1) > 0) & (df[cells].max(axis=1) <= 0.10)).sum()
        nonzero_min = df[cells].apply(lambda r: r[r > 0].min() if (r > 0).any() else np.nan, axis=1)
        small_min = (nonzero_min <= 0.10).sum()
        print(f"  {label:<14}  any-cell positive: {any_pos}; all-zero: {all_zero}; "
              f"max <= 0.10 across cells (forgo 10c for tiny pun.): {small_max}; "
              f"smallest non-zero <= 0.10: {small_min}")

    print("\n" + "=" * 70)
    print("P05c: difference-DV regressions (stacked panel, 2 obs per subject)")
    print("=" * 70)
    print("DV = punish_nodel_X - punish_del_X (positive = self punished more than delegated, H2)")
    for label, df in [("Full sample", pun_full), ("Passers", pun_pass)]:
        rows = []
        for outcome, c_del, c_self in [("good", "punish_del_good", "punish_nodel_good"),
                                       ("bad",  "punish_del_bad",  "punish_nodel_bad")]:
            sub = df[[c_del, c_self, "wa_difficulty", "code"] + SES].dropna()
            sub = sub.assign(diff=sub[c_self] - sub[c_del], bad_outcome=int(outcome == "bad"))
            rows.append(sub[["diff", "bad_outcome", "wa_difficulty", "code"] + SES])
        long = pd.concat(rows, ignore_index=True)
        regs_a = ["bad_outcome"]
        regs_b = ["bad_outcome", "wa_difficulty"] + SES
        for name, regs in [("(diff ~ bad_outcome)", regs_a),
                           ("(diff ~ bad_outcome + wa_difficulty + SES)", regs_b)]:
            X = sm.add_constant(long[regs].astype(float), has_constant="add")
            y = long["diff"].astype(float)
            m = sm.OLS(y, X).fit(cov_type="cluster", cov_kwds={"groups": long["code"].astype(str)})
            int_p = float(m.pvalues["const"])
            bo_p  = float(m.pvalues["bad_outcome"])
            sum_coef = float(m.params["const"] + m.params["bad_outcome"])
            # Test sum (intercept + bad_outcome) = 0
            from numpy import asarray
            R = asarray([[1.0] + [0.0] * (len(m.params) - 1)])
            R[0, list(m.params.index).index("bad_outcome")] = 1.0
            ftest = m.f_test(R)
            sum_p = float(ftest.pvalue)
            print(f"  {label:<10}  {name}")
            print(f"    intercept (= diff in good outcome)   = {float(m.params['const']):+.4f}  p={int_p:.4f}")
            print(f"    bad_outcome (extra diff in bad)       = {float(m.params['bad_outcome']):+.4f}  p={bo_p:.4f}")
            print(f"    intercept + bad_outcome (= diff bad)  = {sum_coef:+.4f}  p={sum_p:.4f}")
            if "wa_difficulty" in m.params.index:
                print(f"    wa_difficulty                          = {float(m.params['wa_difficulty']):+.4f}  p={float(m.pvalues['wa_difficulty']):.4f}")

    print("\n" + "=" * 70)
    print("P05d: inconsistency check — A delegates LESS under punishment, B does NOT differentially punish")
    print("=" * 70)
    a_pun_rate = float(d.loc[d["treat"] == 0, "delegation"].mean())
    a_nopun_rate = float(d.loc[d["treat"] == 1, "delegation"].mean())
    print(f"  Player A delegation rate, Punishment   : {a_pun_rate:.3f} ({100*a_pun_rate:.1f}%)")
    print(f"  Player A delegation rate, No-Punishment: {a_nopun_rate:.3f} ({100*a_nopun_rate:.1f}%)")
    diff_bad_pass = (pun_pass["punish_nodel_bad"] - pun_pass["punish_del_bad"]).mean()
    diff_good_pass = (pun_pass["punish_nodel_good"] - pun_pass["punish_del_good"]).mean()
    print(f"  Player B insulation (passers) — bad outcome:  £{diff_bad_pass:+.3f}")
    print(f"  Player B insulation (passers) — good outcome: £{diff_good_pass:+.3f}")
    print("  Implication: H1's responsibility-avoidance prediction (delegation should rise under "
          "punishment) does not match what Player B actually does to delegated decisions.")


if __name__ == "__main__":
    main()
