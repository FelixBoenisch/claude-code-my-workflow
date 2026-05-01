"""Punishment regression: Player B chosen punishment ~ delegation + outcome + interaction + controls.

Produces tables/reg_punishment.tex.
"""
from __future__ import annotations

import pandas as pd
import statsmodels.api as sm

from lib.io import load_evaluator
from lib.paths import TABLES
from lib.fmt import num
from lib.regtable import render_two_block_table
from lib import manifest

CELLS = [
    ("punish_del_good", 1, 0),
    ("punish_del_bad", 1, 1),
    ("punish_nodel_good", 0, 0),
    ("punish_nodel_bad", 0, 1),
]
CONTROLS = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]


def reshape_long(e: pd.DataFrame) -> pd.DataFrame:
    pun = e[(e["treat"] == 0) & (e["pass_att2"] == 1)].copy()
    rows = []
    for col, deleg, bad in CELLS:
        sub = pun[["code", col] + CONTROLS].copy()
        sub = sub.rename(columns={col: "punish"})
        sub["delegated"] = deleg
        sub["bad_outcome"] = bad
        rows.append(sub)
    return pd.concat(rows, ignore_index=True)


def main() -> None:
    e = load_evaluator()
    long = reshape_long(e).dropna()

    long["interaction"] = long["delegated"] * long["bad_outcome"]
    X = sm.add_constant(
        long[["delegated", "bad_outcome", "interaction"] + CONTROLS].astype(float),
        has_constant="add",
    )
    y = long["punish"].astype(float)
    model = sm.OLS(y, X).fit(cov_type="cluster", cov_kwds={"groups": long["code"].astype(str)})

    rows = [
        ("Delegated", "delegated"),
        ("Bad outcome", "bad_outcome"),
        ("Delegated $\\times$ Bad outcome", "interaction"),
        ("Age", "age"),
        ("Female", "female"),
        ("Socio-economic status", "socio_status"),
        ("Went to uni", "went_to_uni"),
        ("Technology score", "technology_score"),
        ("Leadership position", "leader"),
        ("Constant", "const"),
    ]
    extra = [
        ("N (subject-by-cell)", [f"${len(long)}$"]),
        ("Adj.\\ $R^2$", [f"${num(model.rsquared_adj, 3)}$"]),
    ]
    note = (
        "OLS estimates of Player~B's chosen punishment on a delegation indicator, a bad-outcome "
        "indicator, their interaction, and socio-demographic controls. Standard errors clustered "
        "at the Player~B level (in parentheses). Sample: Player~B subjects in the \\textit{Punishment} "
        "condition who passed the punishment-elicitation attention check, expanded over the four "
        "(delegation, outcome) cells of the strategy method. "
        f"Two-sided $p$-values: \\textit{{Delegated}} $p={num(model.pvalues['delegated'], 3)}$; "
        f"\\textit{{Bad outcome}} $p={num(model.pvalues['bad_outcome'], 3)}$; "
        f"\\textit{{Delegated $\\times$ Bad outcome}} $p={num(model.pvalues['interaction'], 3)}$. "
        "Following AEA editorial policy, significance stars are not reported."
    )
    (TABLES / "reg_punishment.tex").write_text(
        render_two_block_table(
            caption="Determinants of Player~B's chosen punishment",
            label="tab:reg_punishment",
            col_headers=[r"\textit{Punishment} (\pounds)"],
            block_label="Punishment",
            rows=rows,
            models=[model],
            extra_rows=extra,
            note=note,
            column_spec="lc",
        ),
        encoding="utf-8",
    )

    out = {
        "punish_reg_n": int(len(long)),
        "punish_reg_delegated_coef": round(float(model.params["delegated"]), 4),
        "punish_reg_delegated_p": round(float(model.pvalues["delegated"]), 4),
        "punish_reg_bad_outcome_coef": round(float(model.params["bad_outcome"]), 4),
        "punish_reg_bad_outcome_p": round(float(model.pvalues["bad_outcome"]), 4),
        "punish_reg_interaction_coef": round(float(model.params["interaction"]), 4),
        "punish_reg_interaction_p": round(float(model.pvalues["interaction"]), 4),
        "punish_reg_adj_r2": round(float(model.rsquared_adj), 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
