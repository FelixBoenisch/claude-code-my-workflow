"""Punishment regression: Player B chosen punishment ~ delegation + outcome + interaction + controls.

Produces tables/reg_punishment.tex with two columns: the punishment-level
regression for the full sample (1) and attention-check passers (2).
  punish ~ delegated + bad_outcome + interaction + wa_difficulty + SES
The within-subject delegation insulation is read off the Delegated x Bad
interaction; the difference-parameterization estimates are retained in the manifest.
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
SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]


def reshape_long_levels(df: pd.DataFrame) -> pd.DataFrame:
    """Stacked panel of 4 obs per subject (one per cell). DV: punish."""
    rows = []
    for col, deleg, bad in CELLS:
        sub = df[["code", col, "wa_difficulty"] + SES].copy()
        sub = sub.rename(columns={col: "punish"})
        sub["delegated"] = deleg
        sub["bad_outcome"] = bad
        rows.append(sub)
    return pd.concat(rows, ignore_index=True)


def reshape_long_diffs(df: pd.DataFrame) -> pd.DataFrame:
    """Stacked panel of 2 obs per subject (one per outcome).
    DV: nodel - del (positive = self punished more than delegated; H2 prediction)."""
    rows = []
    for outcome, c_del, c_self in [("good", "punish_del_good", "punish_nodel_good"),
                                   ("bad",  "punish_del_bad",  "punish_nodel_bad")]:
        sub = df[[c_del, c_self, "wa_difficulty", "code"] + SES].copy()
        sub["diff"] = sub[c_self] - sub[c_del]
        sub["bad_outcome"] = int(outcome == "bad")
        rows.append(sub[["diff", "bad_outcome", "wa_difficulty", "code"] + SES])
    return pd.concat(rows, ignore_index=True)


def cluster_ols(y, X, groups):
    return sm.OLS(y, X).fit(cov_type="cluster", cov_kwds={"groups": groups.astype(str)})


def fit_block(pun: pd.DataFrame):
    """Fit the three specifications on a given Punishment-condition subsample.

    Returns ((m_level, m_diff_ctrl), (n_level_rows, n_diff_rows, n_subjects)).
    """
    long4 = reshape_long_levels(pun).dropna()
    long4["interaction"] = long4["delegated"] * long4["bad_outcome"]
    X1 = sm.add_constant(
        long4[["delegated", "bad_outcome", "interaction", "wa_difficulty"] + SES].astype(float),
        has_constant="add",
    )
    m_level = cluster_ols(long4["punish"].astype(float), X1, long4["code"])

    long2 = reshape_long_diffs(pun).dropna()
    X3 = sm.add_constant(long2[["bad_outcome", "wa_difficulty"] + SES].astype(float), has_constant="add")
    m_diff_ctrl = cluster_ols(long2["diff"].astype(float), X3, long2["code"])

    return (m_level, m_diff_ctrl), (len(long4), len(long2), int(long4["code"].nunique()))


def main() -> None:
    e = load_evaluator()
    pun_full = e[e["treat"] == 0].copy()
    pun_pass = pun_full[pun_full["pass_att2"] == 1].copy()

    (l_full, dc_full), (n_lvl_full, n_dif_full, n_subj_full) = fit_block(pun_full)
    (l_pass, dc_pass), (n_lvl_pass, n_dif_pass, n_subj_pass) = fit_block(pun_pass)

    rows = [
        ("Delegated", "delegated"),
        ("Bad outcome", "bad_outcome"),
        ("Delegated $\\times$ Bad outcome", "interaction"),
        ("Player B belief about Player A perf.", "wa_difficulty"),
        ("Age", "age"),
        ("Female", "female"),
        ("Socio-economic status", "socio_status"),
        ("Went to uni", "went_to_uni"),
        ("Technology score", "technology_score"),
        ("Leadership position", "leader"),
        ("Constant", "const"),
    ]
    extra = [
        ("Observations", [f"${n_lvl_full}$", f"${n_lvl_pass}$"]),
        ("Subjects", [f"${n_subj_full}$", f"${n_subj_pass}$"]),
        ("Adj.\\ $R^2$",
         [f"${num(l_full.rsquared_adj, 3)}$", f"${num(l_pass.rsquared_adj, 3)}$"]),
    ]
    note = (
        "OLS regression of Player~B's chosen punishment levels. The sample is stacked over the four "
        "(delegation, outcome) scenarios of the strategy method (4 observations per Player~B). The "
        "\\textit{Delegated} $\\times$ \\textit{Bad outcome} interaction is the differential effect "
        "of delegation on punishment in the bad-outcome cell. Column~(1) uses the full "
        "Punishment-condition sample; Column~(2) restricts to Player~Bs who passed the attention "
        "check on the punishment-elicitation screen. Standard errors clustered at "
        "the Player~B level. Significance: $^{*}\\,p<0.10$; $^{**}\\,p<0.05$; $^{***}\\,p<0.01$ (two-sided)."
    )
    (TABLES / "reg_punishment.tex").write_text(
        render_two_block_table(
            caption="Determinants of Player~B's chosen punishment",
            label="tab:reg_punishment",
            col_headers=[r"\textit{Full sample}", r"\textit{Passers}"],
            block_label="Punishment (\\pounds)",
            rows=rows,
            models=[l_full, l_pass],
            extra_rows=extra,
            note=note,
            column_spec="@{\\extracolsep{5pt}}lcc",
            stars=True,
            note_width=0.55,
        ),
        encoding="utf-8",
    )

    out = {
        "punish_reg_n_levels_full": n_lvl_full,
        "punish_reg_n_diffs_full": n_dif_full,
        "punish_reg_n_subjects_full": n_subj_full,
        "punish_reg_n_levels_passers": n_lvl_pass,
        "punish_reg_n_diffs_passers": n_dif_pass,
        "punish_reg_n_subjects_passers": n_subj_pass,
    }
    for tag, m in [("col1_full_level", l_full), ("col2_pass_level", l_pass),
                   ("diff_full_ctrl", dc_full), ("diff_pass_ctrl", dc_pass)]:
        for k in m.params.index:
            out[f"punish_reg_{tag}_{k}_coef"] = round(float(m.params[k]), 4)
            out[f"punish_reg_{tag}_{k}_p"] = round(float(m.pvalues[k]), 4)
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
