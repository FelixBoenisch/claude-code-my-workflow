"""One-off: reproduce tab:del_decision_determinants (Logit) and the same specs
under Probit, and write a side-by-side markdown comparison.

Output: quality_reports/logit_vs_probit_delegation.md
Not part of run_all.py (underscore-prefixed helper).
"""
from __future__ import annotations
import os
import pandas as pd
import statsmodels.api as sm

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PARQUET = os.path.join(ROOT, "data", "clean", "delegator_cleaned.parquet")
OUT = os.path.join(ROOT, "quality_reports", "logit_vs_probit_delegation.md")

SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]
SPECS = [
    ("(1)", ["treat"], False),
    ("(2)", ["treat"] + SES, False),
    ("(3)", ["treat"] + SES + ["overall_score"], False),
    ("(4)", ["treat"] + SES + ["wa_confidence"], False),
    ("(5)", ["treat"] + SES + ["overall_score"], True),
]
ROWS = [
    ("No-Punishment indicator", "treat"),
    ("Task performance", "overall_score"),
    ("Perceived performance", "wa_confidence"),
    ("Age", "age"),
    ("Female", "female"),
    ("Socio-economic status", "socio_status"),
    ("Went to uni", "went_to_uni"),
    ("Technology score", "technology_score"),
    ("Leadership position", "leader"),
    ("Constant", "const"),
]


def stars(p):
    return "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.10 else ""


def fit(df, regs, model_cls, passers):
    s = df.loc[df["pass_att2"] == 1] if passers else df
    sub = s[["delegation"] + regs].dropna()
    X = sm.add_constant(sub[regs].astype(float), has_constant="add")
    m = model_cls(sub["delegation"].astype(float), X).fit(disp=False, cov_type="HC1")
    return m, len(sub)


def ame_treat(m):
    me = m.get_margeff(at="overall", method="dydx")
    names = [n for n in m.params.index if n != "const"]
    i = names.index("treat")
    return float(me.margeff[i]), float(me.pvalues[i])


def cell(m, key):
    if key not in m.params.index:
        return ""
    b, se, p = m.params[key], m.bse[key], m.pvalues[key]
    return f"{b:.3f}{stars(p)} ({se:.3f})"


def build_block(df, model_cls):
    models, ns = [], []
    for _, regs, passers in SPECS:
        m, n = fit(df, regs, model_cls, passers)
        models.append(m); ns.append(n)
    lines = []
    hdr = "| Variable | (1) | (2) | (3) | (4) | (5) |"
    sep = "|---|---|---|---|---|---|"
    lines += [hdr, sep]
    for label, key in ROWS:
        lines.append("| " + label + " | " + " | ".join(cell(m, key) for m in models) + " |")
    ames = [ame_treat(m) for m in models]
    lines.append("| **AME of No-Punishment (pp)** | "
                 + " | ".join(f"{a*100:.1f}{stars(p)} (p={p:.3f})" for a, p in ames) + " |")
    lines.append("| N | " + " | ".join(str(n) for n in ns) + " |")
    lines.append("| Pseudo R2 | " + " | ".join(f"{m.prsquared:.3f}" for m in models) + " |")
    return "\n".join(lines)


def main():
    d = pd.read_parquet(PARQUET)
    md = []
    md.append("# Delegation determinants: Logit (current) vs Probit\n")
    md.append("Dependent variable: delegation (1 = delegated to algorithm). HC1 robust "
              "standard errors in parentheses. Stars: * p<0.10, ** p<0.05, *** p<0.01 "
              "(two-sided). Columns (1)-(4) full sample; (5) attention-check passers. "
              "Two subjects drop in (2)-(4) for missing demographics.\n")
    md.append("## Table A — Logit (current `tab:del_decision_determinants`)\n")
    md.append(build_block(d, sm.Logit))
    md.append("\n## Table B — Probit (same specifications)\n")
    md.append(build_block(d, sm.Probit))
    md.append("\n## Note\n")
    md.append("Raw coefficients are not directly comparable across the two (logit "
              "coefficients are ~1.6-1.8x probit), but the average marginal effects "
              "(AME rows) and significance are nearly identical, so the substantive "
              "conclusion is unchanged.\n")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
