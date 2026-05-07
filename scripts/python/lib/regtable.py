"""Builder for multi-column regression tables.

By default, no significance stars (AEA editorial style). Pass `stars=True` to
append `*`/`**`/`***` to each coefficient at the 10%/5%/1% thresholds.
"""
from __future__ import annotations

from .fmt import num


def _coef_se(model, name, digits=3):
    if model is None or name not in model.params.index:
        return None, None
    return float(model.params[name]), float(model.bse[name])


def stars_for(p: float) -> str:
    """Return the conventional star annotation for a two-sided p-value."""
    if p is None:
        return ""
    if p < 0.01:
        return "***"
    if p < 0.05:
        return "**"
    if p < 0.10:
        return "*"
    return ""


def render_two_block_table(
    *,
    caption: str,
    label: str,
    col_headers: list[str],
    block_label: str,
    rows: list[tuple[str, str]],
    models,
    n_label: str = "N",
    extra_rows: list[tuple[str, list[str]]] | None = None,
    note: str = "",
    digits: int = 3,
    column_spec: str = "@{\\extracolsep{5pt}}lcc|c",
    stars: bool = False,
    col_subheaders: list[str] | None = None,
) -> str:
    """Render a regression table.

    Parameters
    ----------
    rows: list of (display_label, model_param_name)
    models: list of fitted statsmodels results (one per column)
    extra_rows: list of (label, [values per column]) appended at the bottom
    """
    n_cols = len(models)
    out = [
        r"\begin{table}[!htbp]",
        r"\centering",
        f"\\caption{{{caption}}}",
        f"\\label{{{label}}}",
        f"\\begin{{tabular}}{{{column_spec}}}",
        r"\\[-1.8ex]\hline",
        r"\hline \\[-1.8ex]",
        f"& \\multicolumn{{{n_cols}}}{{c}}{{Dependent variable: \\textit{{{block_label}}}}}\\\\[0.1cm]",
        "& " + " & ".join(col_headers) + r" \\",
    ]
    if col_subheaders:
        out.append("& " + " & ".join(col_subheaders) + r" \\")
    out.extend([
        r"\\[-1.8ex] & " + " & ".join(f"({i + 1})" for i in range(n_cols)) + r" \\",
        r"\hline \\[-1.8ex]",
    ])
    for label_text, name in rows:
        coef_cells, se_cells = [], []
        for m in models:
            b, se = _coef_se(m, name, digits)
            if b is None:
                coef_cells.append("")
                se_cells.append("")
            else:
                if stars and m is not None and name in m.pvalues.index:
                    star = stars_for(float(m.pvalues[name]))
                    coef_cells.append(f"${num(b, digits)}^{{{star}}}$" if star else f"${num(b, digits)}$")
                else:
                    coef_cells.append(f"${num(b, digits)}$")
                se_cells.append(f"$({num(se, digits)})$")
        out.append(f" {label_text} & " + " & ".join(coef_cells) + r" \\")
        out.append(r"  & " + " & ".join(se_cells) + r" \\[0.1cm]")
    out.append(r"\hline \\[-1.8ex]")
    if extra_rows:
        for label_text, values in extra_rows:
            out.append(f" {label_text} & " + " & ".join(values) + r" \\")
    out.extend([
        r"\hline",
        r"\hline \\[-1.8ex]",
        f"\\multicolumn{{{n_cols + 1}}}{{p{{0.85\\textwidth}}}}{{\\footnotesize \\textit{{Note:}} {note}}}",
        r"\end{tabular}",
        r"\end{table}",
    ])
    return "\n".join(out) + "\n"
