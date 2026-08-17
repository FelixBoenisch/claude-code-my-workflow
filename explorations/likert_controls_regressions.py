"""Exploration: add Player B's post-experiment Likert items (responsibility,
trust, perception) to the punishment regressions, individually and jointly.

Baseline replicates scripts/python/06_logit_punishment.py, Column (2)
(Punishment condition, attention-check passers, preregistered sample):

  Panel A (levels, 4 obs/subject):
    punish ~ delegated + bad_outcome + delegated*bad + wa_difficulty + SES
  Panel B (differences, 2 obs/subject; DV = punish_nodel - punish_del):
    diff ~ bad_outcome + wa_difficulty + SES

The Likert items are subject-level constants, so in Panel A they can only
shift punishment LEVELS (the within-subject delegated/bad/interaction
coefficients are identified within subject and are orthogonal to any
between-subject regressor up to sample composition). In Panel B a Likert
coefficient measures whether the attitude predicts the SIZE of the
within-subject delegation effect, i.e. the moderation question.

Output: explorations/likert_controls_regressions.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "python"))

from lib.io import load_evaluator  # noqa: E402

OUT_MD = Path(__file__).with_suffix(".md")

CELLS = [
    ("punish_del_good", 1, 0),
    ("punish_del_bad", 1, 1),
    ("punish_nodel_good", 0, 0),
    ("punish_nodel_bad", 0, 1),
]
SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
LIKERTS = ["responsibility", "trust", "perception"]

MODELS = [
    ("Baseline", []),
    ("+ Responsibility", ["responsibility"]),
    ("+ Trust", ["trust"]),
    ("+ Perception", ["perception"]),
    ("+ All three", LIKERTS),
]

ROW_LABELS = {
    "delegated": "Delegated",
    "bad_outcome": "Bad outcome",
    "interaction": "Delegated x Bad outcome",
    "wa_difficulty": "B's belief about A's performance",
    "responsibility": "Responsibility (Likert 1-5)",
    "trust": "Trust in algorithm (Likert 1-5)",
    "perception": "Task difficulty perception (Likert 1-5)",
    "age": "Age",
    "female": "Female",
    "socio_status": "Socio-economic status",
    "went_to_uni": "Went to uni",
    "technology_score": "Technology score",
    "leader": "Leadership position",
    "const": "Constant",
}


def reshape_levels(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for col, deleg, bad in CELLS:
        sub = df[["code", col, "wa_difficulty"] + SES + LIKERTS].copy()
        sub = sub.rename(columns={col: "punish"})
        sub["delegated"] = deleg
        sub["bad_outcome"] = bad
        rows.append(sub)
    long = pd.concat(rows, ignore_index=True)
    long["interaction"] = long["delegated"] * long["bad_outcome"]
    return long


def reshape_diffs(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for outcome, c_del, c_self in [("good", "punish_del_good", "punish_nodel_good"),
                                   ("bad", "punish_del_bad", "punish_nodel_bad")]:
        sub = df[["code", c_del, c_self, "wa_difficulty"] + SES + LIKERTS].copy()
        sub["diff"] = sub[c_self] - sub[c_del]
        sub["bad_outcome"] = int(outcome == "bad")
        rows.append(sub[["code", "diff", "bad_outcome", "wa_difficulty"] + SES + LIKERTS])
    return pd.concat(rows, ignore_index=True)


def fit(long: pd.DataFrame, dv: str, xvars: list[str]):
    est = long.dropna(subset=[dv] + xvars).copy()
    X = sm.add_constant(est[xvars].astype(float), has_constant="add")
    m = sm.OLS(est[dv].astype(float), X).fit(
        cov_type="cluster", cov_kwds={"groups": est["code"].astype(str)}
    )
    return m, est


def cell(m, var: str) -> str:
    if var not in m.params.index:
        return "--"
    return f"{m.params[var]:.3f} ({m.bse[var]:.3f}) [{m.pvalues[var]:.3f}]"


def panel_table(long: pd.DataFrame, dv: str, base_x: list[str]) -> tuple[str, dict]:
    fits = {}
    for label, extra in MODELS:
        m, est = fit(long, dv, base_x + extra)
        fits[label] = (m, est)

    # Baseline refit on the joint-model estimation sample (stability check)
    joint_est = fits["+ All three"][1]
    m_base_joint, _ = fit(joint_est, dv, base_x)
    fits["Baseline, joint sample"] = (m_base_joint, joint_est)

    order = [v for v in ["delegated", "bad_outcome", "interaction", "wa_difficulty"]
             if v in base_x] + LIKERTS + SES + ["const"]
    cols = [label for label, _ in MODELS] + ["Baseline, joint sample"]

    lines = ["| | " + " | ".join(f"({i+1}) {c}" for i, c in enumerate(cols)) + " |",
             "|---" * (len(cols) + 1) + "|"]
    for var in order:
        row = [ROW_LABELS.get(var, var)]
        for c in cols:
            row.append(cell(fits[c][0], var))
        lines.append("| " + " | ".join(row) + " |")
    lines.append("| Observations | " + " | ".join(str(int(fits[c][0].nobs)) for c in cols) + " |")
    lines.append("| Subjects | " + " | ".join(str(fits[c][1]["code"].nunique()) for c in cols) + " |")
    lines.append("| Adj. R2 | " + " | ".join(f"{fits[c][0].rsquared_adj:.3f}" for c in cols) + " |")
    return "\n".join(lines), fits


def main() -> None:
    e = load_evaluator()
    pun = e[(e["treat"] == 0) & (e["pass_att2"] == 1)].copy()
    n_subj = len(pun)

    # --- Likert summary stats on the analysis sample -------------------------
    summ = ["| Item | N non-missing | Mean | SD | Min | Max |", "|---|---|---|---|---|---|"]
    for lk in LIKERTS:
        s = pun[lk].dropna()
        summ.append(f"| {ROW_LABELS[lk]} | {len(s)} | {s.mean():.2f} | {s.std():.2f} "
                    f"| {s.min():.0f} | {s.max():.0f} |")
    summary_table = "\n".join(summ)

    corr = pun[LIKERTS].corr()
    corr_lines = ["| | responsibility | trust | perception |", "|---|---|---|---|"]
    for lk in LIKERTS:
        corr_lines.append(f"| {lk} | " + " | ".join(f"{corr.loc[lk, c]:.3f}" for c in LIKERTS) + " |")
    corr_table = "\n".join(corr_lines)

    # --- Panels --------------------------------------------------------------
    levels = reshape_levels(pun)
    base_a = ["delegated", "bad_outcome", "interaction", "wa_difficulty"] + SES
    table_a, fits_a = panel_table(levels, "punish", base_a)

    diffs = reshape_diffs(pun)
    base_b = ["bad_outcome", "wa_difficulty"] + SES
    table_b, fits_b = panel_table(diffs, "diff", base_b)

    md = f"""# Likert attitudes as controls in the punishment regressions

**Exploration, not a manuscript artefact.** Generated by
`explorations/likert_controls_regressions.py`. Question: what happens to the
punishment regressions when Player B's three post-experiment Likert items
(`responsibility`, `trust`, `perception`) enter individually and jointly?

**Sample.** Punishment condition (`treat == 0`), attention-check passers
(`pass_att2 == 1`), the preregistered sample of the main punishment table
(Column 2 of `tables/reg_punishment.tex`): n = {n_subj} Player Bs. Standard
errors clustered at the Player B level. Cells report coefficient (SE) [p].
No significance stars, per AEA convention.

**Caveat on timing.** The Likert items were elicited *after* the punishment
decisions. They are post-treatment measurements of attitudes, not exogenous
controls, so these regressions describe associations and cannot support a
causal reading.

## Likert items on the analysis sample

{summary_table}

Pairwise correlations:

{corr_table}

## Panel A -- Punishment levels (4 obs per subject)

DV: chosen punishment in GBP, stacked over the four strategy-method cells.
Baseline spec = main table: `punish ~ delegated + bad_outcome +
delegated x bad + wa_difficulty + SES`, cluster by subject.

{table_a}

Because the Likert items are constant within subject while `delegated`,
`bad_outcome`, and the interaction vary within subject, the design
coefficients can move across columns only through sample composition
(Likert missingness). Column (6) refits the baseline on the column-(5)
estimation sample to isolate that channel.

## Panel B -- Within-subject delegation effect (2 obs per subject)

DV: `punish_nodel - punish_del` per outcome (positive = self-made decisions
punished more than delegated ones). Here a Likert coefficient answers the
moderation question: do attitudes predict the *size* of the delegation
effect in punishment?

{table_b}

## Reading

(Interpretation added after inspection of the numbers.)
"""
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"written: {OUT_MD}")

    # Console: key coefficients for quick reading
    for panel, fits, keys in [
        ("A", fits_a, ["delegated", "interaction"] + LIKERTS),
        ("B", fits_b, ["bad_outcome"] + LIKERTS),
    ]:
        print(f"\n=== Panel {panel} ===")
        for label in [m[0] for m in MODELS] + ["Baseline, joint sample"]:
            m = fits[label][0]
            parts = [f"{k}={cell(m, k)}" for k in keys if k in m.params.index]
            print(f"  {label}: N={int(m.nobs)}  " + "  ".join(parts))


if __name__ == "__main__":
    main()
