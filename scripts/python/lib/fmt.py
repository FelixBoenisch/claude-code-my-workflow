"""LaTeX table formatting helpers. AEA-style: no significance stars."""
from __future__ import annotations


def num(x, digits: int = 3) -> str:
    if x is None:
        return ""
    if isinstance(x, (int,)) and not isinstance(x, bool):
        return f"{x:,}"
    try:
        return f"{x:.{digits}f}"
    except (TypeError, ValueError):
        return str(x)


def coef(estimate, se=None, digits: int = 3) -> str:
    """Estimate over standard error, AEA-style."""
    e = num(estimate, digits)
    if se is None:
        return f"${e}$"
    s = num(se, digits)
    return f"${e}$\\\\\n  & $({s})$"


def write_tex(path, body: str) -> None:
    """Write a self-contained \\input{}-able .tex fragment."""
    path.write_text(body, encoding="utf-8")
