"""One-off: bad-outcome-only difference regression.

DV = punish_nodel_bad - punish_del_bad (one obs per Player B, bad cell only),
no bad-outcome indicator. Columns: full / passers, without and with controls.
Output: quality_reports/punishment_bad_cell_diff.md
Not part of run_all.py.
"""
from __future__ import annotations
import os
import pandas as pd
import statsmodels.api as sm

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PARQUET = os.path.join(ROOT, "data", "clean", "evaluator_cleaned.parquet")
OUT = os.path.join(ROOT, "quality_reports", "punishment_bad_cell_diff.md")

SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
ROWS = [
    ("Constant (avg bad-cell insulation)", "const"),
    ("Player B belief about Player A perf.", "wa_difficulty"),
    ("Age", "age"),
    ("Female", "female"),
    ("Socio-economic status", "socio_status"),
    ("Went to uni", "went_to_uni"),
    ("Technology score", "technology_score"),
    ("Leadership position", "leader"),
]
SPECS = [("Full", False), ("Full +ctrl", True), ("Passers", False), ("Passers +ctrl", True)]


def stars(p):
    return "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.10 else ""


def fit(df, passers, ctrl):
    d = df[df["pass_att2"] == 1] if passers else df
    d = d.copy()
    d["diff_bad"] = d["punish_nodel_bad"] - d["punish_del_bad"]
    regs = (["wa_difficulty"] + SES) if ctrl else []
    sub = d[["diff_bad"] + regs].dropna()
    X = sm.add_constant(sub[regs].astype(float), has_constant="add") if regs else \
        pd.DataFrame({"const": 1.0}, index=sub.index)
    return sm.OLS(sub["diff_bad"].astype(float), X).fit(cov_type="HC1"), len(sub)


def cell(m, key):
    if key not in m.params.index:
        return ""
    b, se, p = m.params[key], m.bse[key], m.pvalues[key]
    return f"{b:.3f}{stars(p)} ({se:.3f})"


def main():
    e = pd.read_parquet(PARQUET)
    pun = e[e["treat"] == 0]
    models, ns = [], []
    for _, ctrl in SPECS:
        passers = "Passers" in _
        m, n = fit(pun, passers, ctrl)
        models.append(m); ns.append(n)
    md = ["# Bad-outcome-only difference regression\n",
          "DV = within-subject insulation in the **bad-outcome cell**, "
          "$\\text{punish\\_nodel\\_bad} - \\text{punish\\_del\\_bad}$ (one observation per "
          "Player B; no bad-outcome indicator). HC1 robust SE in parentheses. "
          "Stars: * p<0.10, ** p<0.05, *** p<0.01 (two-sided).\n",
          "| Variable | " + " | ".join(s for s, _ in SPECS) + " |",
          "|---|" + "---|" * len(SPECS)]
    for label, key in ROWS:
        md.append("| " + label + " | " + " | ".join(cell(m, key) for m in models) + " |")
    md.append("| N | " + " | ".join(str(n) for n in ns) + " |")
    md.append("| Adj. R2 | " + " | ".join(f"{m.rsquared_adj:.3f}" for m in models) + " |")
    md.append("\n**Note.** Without controls the constant is the mean within-subject insulation "
              "in the bad cell (= the paired t-test): £0.071 (full), £0.077 (passers), both n.s. "
              "With raw (uncentered) controls the constant is the fitted insulation at all "
              "controls = 0 — an extrapolation, **not** the average effect — hence the large, "
              "uninterpretable values. Mean-center the controls if an adjusted average is wanted.\n")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
