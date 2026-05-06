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


if __name__ == "__main__":
    main()
