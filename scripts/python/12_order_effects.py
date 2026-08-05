"""Order effects via random_order_del.

random_order_del = 1 if the algorithm option was presented first; 0 if own decision was first.
Tests whether the H1 treatment effect is robust to interacting with order, and
whether order affects delegation rates within each condition.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

from lib.io import load_delegator
from lib import manifest


def main() -> None:
    d = load_delegator()

    # Delegation rates by (treat, order)
    by_cell = d.groupby(["treat", "random_order_del"])["delegation"].agg(["count", "mean"]).reset_index()
    print("Delegation rate by (treat, random_order_del):")
    print(by_cell.to_string(index=False))

    # Logit with punishment-indicator × order interaction
    sub = d[["delegation", "treat", "random_order_del"]].dropna()
    sub["punish"] = 1 - sub["treat"]
    sub["punish_x_order"] = sub["punish"] * sub["random_order_del"]
    X = sm.add_constant(sub[["punish", "random_order_del", "punish_x_order"]].astype(float), has_constant="add")
    y = sub["delegation"].astype(float)
    model = sm.Logit(y, X).fit(disp=False, cov_type="HC1")

    # Order effect within each condition
    pun = d[d["treat"] == 0]
    nopun = d[d["treat"] == 1]
    pun_order_diff = float(pun.groupby("random_order_del")["delegation"].mean().diff().iloc[-1])
    nopun_order_diff = float(nopun.groupby("random_order_del")["delegation"].mean().diff().iloc[-1])

    # Chi-squared for order effect within each condition
    pun_table = pd.crosstab(pun["random_order_del"], pun["delegation"]).values
    nopun_table = pd.crosstab(nopun["random_order_del"], nopun["delegation"]).values
    _, p_pun_order, _, _ = stats.chi2_contingency(pun_table, correction=False)
    _, p_nopun_order, _, _ = stats.chi2_contingency(nopun_table, correction=False)

    out = {
        "order_pun_diff_pp": round(100 * pun_order_diff, 1),
        "order_nopun_diff_pp": round(100 * nopun_order_diff, 1),
        "order_pun_chi2_p": round(float(p_pun_order), 4),
        "order_nopun_chi2_p": round(float(p_nopun_order), 4),
        "order_logit_punish_coef": round(float(model.params["punish"]), 4),
        "order_logit_punish_p": round(float(model.pvalues["punish"]), 4),
        "order_logit_order_coef": round(float(model.params["random_order_del"]), 4),
        "order_logit_order_p": round(float(model.pvalues["random_order_del"]), 4),
        "order_logit_interaction_coef": round(float(model.params["punish_x_order"]), 4),
        "order_logit_interaction_p": round(float(model.pvalues["punish_x_order"]), 4),
    }
    manifest.update(out)
    for k, v in out.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
