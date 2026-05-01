"""Player A and Player B balance tables (Appendix Tables A1 and A1b).

Produces:
  tables/balance_player_a.tex
  tables/balance_player_b.tex
"""
import numpy as np
import pandas as pd
from scipy import stats

from lib.io import load_delegator, load_evaluator
from lib.paths import TABLES
from lib.fmt import num

VARS = [
    ("age", "Age", "continuous"),
    ("female", "Female", "binary"),
    ("socio_status", "Socio-economic status", "continuous"),
    ("went_to_uni", "Went to uni", "binary"),
    ("technology_score", "Technology score", "continuous"),
    ("leader", "Leadership position", "binary"),
]


def balance_table(df: pd.DataFrame) -> list[tuple[str, float, float, float]]:
    rows = []
    g0 = df[df["treat"] == 0]
    g1 = df[df["treat"] == 1]
    for col, label, kind in VARS:
        m0 = float(g0[col].mean())
        m1 = float(g1[col].mean())
        if kind == "continuous":
            _, p = stats.ttest_ind(g0[col].dropna(), g1[col].dropna(), equal_var=False)
        else:
            tab = pd.crosstab(df["treat"], df[col])
            _, p, _, _ = stats.chi2_contingency(tab)
        rows.append((label, m0, m1, float(p)))
    return rows


def render_tex(rows, label: str, caption: str, table_label: str) -> str:
    lines = [
        r"\begin{table}[!htbp]",
        r"    \centering",
        f"    \\caption{{{caption}}}",
        f"    \\label{{{table_label}}}",
        r"    \begin{tabular}{l|rrr}",
        r"                  Variable &  \textit{Punishment} &  \textit{No-Punishment} &  $p$-value \\ \hline",
    ]
    for variable, m0, m1, p in rows:
        lines.append(f"        {variable:>22} &  ${num(m0,3)}$ &  ${num(m1,3)}$ &  ${num(p,3)}$ \\\\")
    lines.extend([
        r"    \end{tabular}",
        r"    \begin{minipage}{0.95\textwidth}\footnotesize",
        f"    \\textit{{Note:}} Mean values by condition for {label}, with $p$-values from two-sided $t$-tests for continuous variables and Chi-squared tests for binary variables. \\textit{{Socio-economic status}} is self-reported on a $1$--$10$ scale; \\textit{{Went to uni}} indicates a university degree; \\textit{{Technology score}} is constructed from weekly device usage, programming skills, cryptocurrency knowledge, technology use at work, and similar items; \\textit{{Leadership position}} indicates self-reported management or supervisory experience.",
        r"    \end{minipage}",
        r"\end{table}",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    rows_a = balance_table(d)
    rows_b = balance_table(e)

    (TABLES / "balance_player_a.tex").write_text(
        render_tex(rows_a, "Player~A", "Condition balance --- Player~A", "tab:treatment_balance"),
        encoding="utf-8",
    )
    (TABLES / "balance_player_b.tex").write_text(
        render_tex(rows_b, "Player~B", "Condition balance --- Player~B", "tab:treatment_balance_B"),
        encoding="utf-8",
    )
    print("Player A balance:")
    for r in rows_a: print(f"  {r}")
    print("Player B balance:")
    for r in rows_b: print(f"  {r}")


if __name__ == "__main__":
    main()
