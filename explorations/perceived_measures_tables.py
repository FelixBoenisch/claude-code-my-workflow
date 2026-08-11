"""Exploration: Table 1 and Table 3 variants with mean / median / mode of
perceived performance. Production scripts and tables/ stay untouched; results
are summarized in perceived_measures_tables.md.

Run from scripts/python (for lib imports):
  ../../.venv/Scripts/python.exe ../../explorations/perceived_measures_tables.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "python"))

import numpy as np
import statsmodels.api as sm

from lib.io import load_delegator

SES = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]


def probit(df, regs):
    sub = df[["delegation"] + regs].dropna()
    X = sm.add_constant(sub[regs].astype(float), has_constant="add")
    m = sm.Probit(sub["delegation"].astype(float), X).fit(disp=False, cov_type="HC1")
    return m, len(sub)


def ame(m, var, dummy=False):
    me = m.get_margeff(at="overall", method="dydx", dummy=dummy)
    names = [n for n in m.model.exog_names if n != "const"]
    i = names.index(var)
    return float(me.margeff[i]), float(me.pvalues[i])


def cell(m, v):
    return f"{m.params[v]:+.3f} (p={m.pvalues[v]:.3f})"


def main():
    d = load_delegator()
    conf = d[[f"confidence{k}" for k in range(11)]].to_numpy(float)
    probs = conf / conf.sum(axis=1, keepdims=True)
    ks = np.arange(11)
    d["pp_mean"] = probs @ ks          # identical to wa_confidence
    d["pp_median"] = (probs.cumsum(axis=1) < 0.5).sum(axis=1)
    d["pp_mode"] = probs.argmax(axis=1)
    d["punish"] = 1 - d["treat"]

    print("=== Table 1 analog: Column (4) with each perceived measure ===")
    print("(full sample, Punishment indicator + SES + measure, Probit)")
    for meas in ["pp_mean", "pp_median", "pp_mode"]:
        m, n = probit(d, ["punish"] + SES + [meas])
        a, ap = ame(m, "punish", dummy=True)
        print(f"{meas:10s} | Punish {cell(m, 'punish')} | AME {100*a:+.1f}pp "
              f"(p={ap:.3f}) | {meas} {cell(m, meas)} | N={n} "
              f"| pseudoR2={m.prsquared:.3f}")

    print()
    print("=== Table 3 analog: belief specs with each perceived measure as control ===")
    sub = d[d["treat"] == 0].copy()
    sub["bel_diff_good"] = sub["nodel_del_good"]
    sub["bel_diff_bad"] = sub["nodel_del_bad"]
    sub["bel_diff_avg"] = 0.5 * (sub["bel_diff_good"] + sub["bel_diff_bad"])
    sub["p_success"] = sub["wa_confidence"] / 10.0
    sub["bel_diff_weighted"] = (sub["p_success"] * sub["bel_diff_good"]
                                + (1 - sub["p_success"]) * sub["bel_diff_bad"])
    pas = sub[sub["pass_att2"] == 1]
    specs = [
        ("(2) full + controls",      sub, "bel_diff_avg"),
        ("(3) passers + controls",   pas, "bel_diff_avg"),
        ("(4) weighted, passers",    pas, "bel_diff_weighted"),
        ("(5) decomposition, pass.", pas, None),
    ]
    for meas in ["pp_mean", "pp_median", "pp_mode"]:
        print(f"--- measure: {meas}")
        for name, df, bel in specs:
            regs = ([bel] if bel else ["bel_diff_good", "bel_diff_bad"]) + [meas] + SES
            m, n = probit(df, regs)
            if bel:
                a, ap = ame(m, bel)
                belcell = f"{bel} {cell(m, bel)} | AME {10*a:+.2f}pp/£0.10 (p={ap:.3f})"
            else:
                belcell = (f"good {cell(m, 'bel_diff_good')} | "
                           f"bad {cell(m, 'bel_diff_bad')}")
            print(f"{name:26s} | {belcell} | {meas} {cell(m, meas)} | N={n}")


if __name__ == "__main__":
    main()
