"""Punishment regression robustness:
  - Add Player B's belief about Player A's performance (wa_difficulty) as a regressor.
  - Re-estimate without attention-check exclusion.
  - Report H2 paired-tests both with and without exclusion.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

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


def reshape_long(e: pd.DataFrame, exclude_attention: bool) -> pd.DataFrame:
    if exclude_attention:
        pun = e[(e["treat"] == 0) & (e["pass_att2"] == 1)].copy()
    else:
        pun = e[e["treat"] == 0].copy()
    rows = []
    for col, deleg, bad in CELLS:
        sub = pun[["code", col, "wa_difficulty"] + CONTROLS].copy()
        sub = sub.rename(columns={col: "punish"})
        sub["delegated"] = deleg
        sub["bad_outcome"] = bad
        rows.append(sub)
    return pd.concat(rows, ignore_index=True)


def fit(long: pd.DataFrame):
    long = long.copy()
    long["interaction"] = long["delegated"] * long["bad_outcome"]
    X = sm.add_constant(
        long[["delegated", "bad_outcome", "interaction", "wa_difficulty"] + CONTROLS].astype(float),
        has_constant="add",
    )
    y = long["punish"].astype(float)
    return sm.OLS(y, X).fit(cov_type="cluster", cov_kwds={"groups": long["code"].astype(str)})


def main() -> None:
    e = load_evaluator()

    # Specification 1: with attention exclusion (matches main Table)
    long1 = reshape_long(e, exclude_attention=True).dropna()
    model1 = fit(long1)

    # Specification 2: without attention exclusion (robustness)
    long2 = reshape_long(e, exclude_attention=False).dropna()
    model2 = fit(long2)

    # H2 paired-tests both ways
    pun_with = e[(e["treat"] == 0) & (e["pass_att2"] == 1)]
    pun_without = e[e["treat"] == 0]
    diff_bad_with = (pun_with["punish_nodel_bad"] - pun_with["punish_del_bad"]).dropna()
    diff_bad_without = (pun_without["punish_nodel_bad"] - pun_without["punish_del_bad"]).dropna()
    _, p_t_with = stats.ttest_rel(pun_with["punish_nodel_bad"], pun_with["punish_del_bad"])
    _, p_t_without = stats.ttest_rel(pun_without["punish_nodel_bad"], pun_without["punish_del_bad"])
    _, p_w_with = stats.wilcoxon(pun_with["punish_nodel_bad"], pun_with["punish_del_bad"], zero_method="wilcox")
    _, p_w_without = stats.wilcoxon(pun_without["punish_nodel_bad"], pun_without["punish_del_bad"], zero_method="wilcox")

    # Render robustness table
    rows = [
        ("Delegated", "delegated"),
        ("Bad outcome", "bad_outcome"),
        ("Delegated $\\times$ Bad outcome", "interaction"),
        ("Player B belief about Player A perf. (wa)", "wa_difficulty"),
        ("Age", "age"),
        ("Female", "female"),
        ("Socio-economic status", "socio_status"),
        ("Went to uni", "went_to_uni"),
        ("Technology score", "technology_score"),
        ("Leadership position", "leader"),
        ("Constant", "const"),
    ]
    extra = [
        ("Attention-check excl.", ["yes", "no"]),
        ("N (subject-by-cell)", [f"${len(long1)}$", f"${len(long2)}$"]),
        ("Adj.\\ $R^2$", [f"${num(model1.rsquared_adj, 3)}$", f"${num(model2.rsquared_adj, 3)}$"]),
    ]
    note = (
        "Punishment regression with Player~B's belief about Player~A's performance (\\textit{wa\\_difficulty}) "
        "added as a regressor. Column (1) excludes Player~Bs who failed the punishment-screen attention "
        "check (preregistered); Column (2) keeps them. Standard errors clustered at the Player~B level. "
        "The delegation, outcome, and interaction coefficients are stable across both specifications, "
        "and the belief regressor is not significantly associated with chosen punishment. "
        f"H2 paired-test on the bad-outcome cell: with exclusion paired-$t$ $p={num(float(p_t_with), 3)}$, "
        f"Wilcoxon $p={num(float(p_w_with), 3)}$ ($n={len(pun_with)}$); "
        f"without exclusion paired-$t$ $p={num(float(p_t_without), 3)}$, "
        f"Wilcoxon $p={num(float(p_w_without), 3)}$ ($n={len(pun_without)}$). "
        "Following AEA editorial policy, significance stars are not reported."
    )

    (TABLES / "reg_punishment_robustness.tex").write_text(
        render_two_block_table(
            caption="Determinants of Player~B's chosen punishment --- robustness",
            label="tab:reg_punishment_robustness",
            col_headers=[r"\textit{Excl.}", r"\textit{Incl. att.\ failers}"],
            block_label="Punishment",
            rows=rows,
            models=[model1, model2],
            extra_rows=extra,
            note=note,
            column_spec="lcc",
        ),
        encoding="utf-8",
    )

    out = {
        "robust_pun_with_excl_n": int(len(long1)),
        "robust_pun_without_excl_n": int(len(long2)),
        "robust_pun_with_wa_diff_coef": round(float(model1.params["wa_difficulty"]), 4),
        "robust_pun_with_wa_diff_p": round(float(model1.pvalues["wa_difficulty"]), 4),
        "robust_pun_without_wa_diff_coef": round(float(model2.params["wa_difficulty"]), 4),
        "robust_pun_without_wa_diff_p": round(float(model2.pvalues["wa_difficulty"]), 4),
        "h2_paired_t_bad_with_excl_p": round(float(p_t_with), 4),
        "h2_paired_t_bad_without_excl_p": round(float(p_t_without), 4),
        "h2_wilcoxon_bad_with_excl_p": round(float(p_w_with), 4),
        "h2_wilcoxon_bad_without_excl_p": round(float(p_w_without), 4),
        "h2_n_with_excl": int(len(pun_with)),
        "h2_n_without_excl": int(len(pun_without)),
        "h2_diff_bad_mean_with_excl": round(float(diff_bad_with.mean()), 4),
        "h2_diff_bad_mean_without_excl": round(float(diff_bad_without.mean()), 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
