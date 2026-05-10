"""Robustness: every key analysis run twice — full sample vs pass_att2-pass-only.

For each analysis the script reports the same statistics on:
  - full sample           (no attention-check exclusion)
  - attention-pass sample (pass_att2 == 1; A excluded on belief screen,
                           B excluded on punishment screen — preregistered rule)

Outputs:
  scripts/python/_outputs/attention_check_comparison.json
  scripts/python/_outputs/attention_check_comparison.md
"""
from __future__ import annotations

import json
import math

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

from lib.io import load_delegator, load_evaluator
from lib.paths import OUTPUTS

CONTROLS = ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]

PUNISH_CELLS = [
    ("punish_del_good", 1, 0),
    ("punish_del_bad", 1, 1),
    ("punish_nodel_good", 0, 0),
    ("punish_nodel_bad", 0, 1),
]


def filter_a(d: pd.DataFrame, on: bool) -> pd.DataFrame:
    return d[d["pass_att2"] == 1].copy() if on else d.copy()


def filter_b(e: pd.DataFrame, on: bool) -> pd.DataFrame:
    return e[e["pass_att2"] == 1].copy() if on else e.copy()


# ------- analyses (return dict of scalars) -------

def sample_sizes(d, e, on):
    da = filter_a(d, on)
    eb = filter_b(e, on)
    return {
        "n_a_total": int(len(da)),
        "n_a_pun": int((da["treat"] == 0).sum()),
        "n_a_nopun": int((da["treat"] == 1).sum()),
        "n_b_total": int(len(eb)),
        "n_b_pun": int((eb["treat"] == 0).sum()),
        "n_b_nopun": int((eb["treat"] == 1).sum()),
    }


def balance(df, on):
    sub = df[df["pass_att2"] == 1].copy() if on else df.copy()
    g0, g1 = sub[sub["treat"] == 0], sub[sub["treat"] == 1]
    out = {}
    for col, kind in [
        ("age", "c"), ("female", "b"), ("socio_status", "c"),
        ("went_to_uni", "b"), ("technology_score", "c"), ("leader", "b"),
    ]:
        m0, m1 = float(g0[col].mean()), float(g1[col].mean())
        if kind == "c":
            _, p = stats.ttest_ind(g0[col].dropna(), g1[col].dropna(), equal_var=False)
        else:
            tab = pd.crosstab(sub["treat"], sub[col])
            _, p, _, _ = stats.chi2_contingency(tab)
        out[col] = {"mean_pun": round(m0, 3), "mean_nopun": round(m1, 3),
                    "p": round(float(p), 4)}
    return out


def h1(d, on):
    df = filter_a(d, on)
    by = df.groupby("treat")["delegation"]
    counts = by.sum().astype(int).to_dict()
    n = by.count().astype(int).to_dict()
    rates = {k: counts[k] / n[k] for k in counts}
    table = np.array([[counts[0], n[0] - counts[0]], [counts[1], n[1] - counts[1]]])
    chi2, p_chi2, _, _ = stats.chi2_contingency(table, correction=False)
    _, p_fisher = stats.fisher_exact(table, alternative="two-sided")
    return {
        "rate_pun_pct": round(100 * rates[0], 1),
        "rate_nopun_pct": round(100 * rates[1], 1),
        "gap_pp": round(100 * (rates[1] - rates[0]), 1),
        "n_pun": int(n[0]),
        "n_nopun": int(n[1]),
        "p_chi2": round(float(p_chi2), 4),
        "p_fisher": round(float(p_fisher), 4),
    }


def _logit(y, X):
    X = sm.add_constant(X.astype(float), has_constant="add")
    return sm.Logit(y.astype(float), X).fit(disp=False, cov_type="HC1")


def logit_col1(d, on):
    df = filter_a(d, on)
    sub = df[["delegation", "treat"]].dropna()
    m = _logit(sub["delegation"], sub[["treat"]])
    return {"n": int(len(sub)), "treat_coef": round(float(m.params["treat"]), 4),
            "treat_se": round(float(m.bse["treat"]), 4),
            "treat_p": round(float(m.pvalues["treat"]), 4),
            "pseudo_r2": round(float(m.prsquared), 4)}


def logit_col2(d, on):
    df = filter_a(d, on)
    cols = ["delegation", "treat", "overall_score"] + CONTROLS
    sub = df[cols].dropna()
    m = _logit(sub["delegation"], sub[["treat", "overall_score"] + CONTROLS])
    return {"n": int(len(sub)), "treat_coef": round(float(m.params["treat"]), 4),
            "treat_se": round(float(m.bse["treat"]), 4),
            "treat_p": round(float(m.pvalues["treat"]), 4),
            "pseudo_r2": round(float(m.prsquared), 4)}


def logit_col3(d, on):
    df = filter_a(d, on)
    sub = df[df["treat"] == 0].copy()
    sub["bel_diff_bad"] = sub["nodel_del_bad"]
    sub["bel_diff_good"] = sub["nodel_del_good"]
    cols = ["delegation", "bel_diff_bad", "bel_diff_good", "overall_score"] + CONTROLS
    sub = sub[cols].dropna()
    m = _logit(sub["delegation"],
               sub[["bel_diff_bad", "bel_diff_good", "overall_score"] + CONTROLS])
    return {
        "n": int(len(sub)),
        "bel_good_coef": round(float(m.params["bel_diff_good"]), 4),
        "bel_good_p": round(float(m.pvalues["bel_diff_good"]), 4),
        "bel_bad_coef": round(float(m.params["bel_diff_bad"]), 4),
        "bel_bad_p": round(float(m.pvalues["bel_diff_bad"]), 4),
        "score_coef": round(float(m.params["overall_score"]), 4),
        "score_p": round(float(m.pvalues["overall_score"]), 4),
        "pseudo_r2": round(float(m.prsquared), 4),
    }


def h2(e, on):
    eb = filter_b(e, on)
    pun = eb[eb["treat"] == 0].copy()
    n = len(pun)
    diff_bad = pun["punish_nodel_bad"] - pun["punish_del_bad"]
    diff_good = pun["punish_nodel_good"] - pun["punish_del_good"]

    _, p_bad_t = stats.ttest_rel(pun["punish_nodel_bad"], pun["punish_del_bad"])
    try:
        _, p_bad_w = stats.wilcoxon(pun["punish_nodel_bad"], pun["punish_del_bad"],
                                    zero_method="wilcox")
    except ValueError:
        p_bad_w = float("nan")
    _, p_good_t = stats.ttest_rel(pun["punish_nodel_good"], pun["punish_del_good"])
    try:
        _, p_good_w = stats.wilcoxon(pun["punish_nodel_good"], pun["punish_del_good"],
                                     zero_method="wilcox")
    except ValueError:
        p_good_w = float("nan")

    sd_bad = float(diff_bad.std(ddof=1))
    sd_good = float(diff_good.std(ddof=1))
    mde_bad = 2.8 * sd_bad / math.sqrt(n) if n > 0 else float("nan")
    mde_good = 2.8 * sd_good / math.sqrt(n) if n > 0 else float("nan")

    n_never = int((pun.set_index("code")[
        ["punish_del_good", "punish_del_bad", "punish_nodel_good", "punish_nodel_bad"]
    ] == 0).all(axis=1).sum())

    return {
        "n": int(n),
        "punish_del_good_mean": round(float(pun["punish_del_good"].mean()), 4),
        "punish_del_bad_mean": round(float(pun["punish_del_bad"].mean()), 4),
        "punish_nodel_good_mean": round(float(pun["punish_nodel_good"].mean()), 4),
        "punish_nodel_bad_mean": round(float(pun["punish_nodel_bad"].mean()), 4),
        "diff_bad_mean": round(float(diff_bad.mean()), 4),
        "diff_good_mean": round(float(diff_good.mean()), 4),
        "p_bad_t": round(float(p_bad_t), 4),
        "p_bad_w": None if math.isnan(p_bad_w) else round(float(p_bad_w), 4),
        "p_good_t": round(float(p_good_t), 4),
        "p_good_w": None if math.isnan(p_good_w) else round(float(p_good_w), 4),
        "mde_bad": round(mde_bad, 4),
        "mde_good": round(mde_good, 4),
        "n_never_punish": n_never,
        "pct_never_punish": round(100 * n_never / n, 1) if n > 0 else None,
    }


def punishment_reg(e, on):
    eb = filter_b(e, on)
    pun = eb[eb["treat"] == 0].copy()
    rows = []
    for col, deleg, bad in PUNISH_CELLS:
        sub = pun[["code", col] + CONTROLS].copy()
        sub = sub.rename(columns={col: "punish"})
        sub["delegated"] = deleg
        sub["bad_outcome"] = bad
        rows.append(sub)
    long = pd.concat(rows, ignore_index=True).dropna()
    long["interaction"] = long["delegated"] * long["bad_outcome"]
    X = sm.add_constant(
        long[["delegated", "bad_outcome", "interaction"] + CONTROLS].astype(float),
        has_constant="add",
    )
    m = sm.OLS(long["punish"].astype(float), X).fit(
        cov_type="cluster", cov_kwds={"groups": long["code"].astype(str)}
    )
    return {
        "n_obs": int(len(long)),
        "delegated_coef": round(float(m.params["delegated"]), 4),
        "delegated_p": round(float(m.pvalues["delegated"]), 4),
        "bad_coef": round(float(m.params["bad_outcome"]), 4),
        "bad_p": round(float(m.pvalues["bad_outcome"]), 4),
        "interaction_coef": round(float(m.params["interaction"]), 4),
        "interaction_p": round(float(m.pvalues["interaction"]), 4),
        "adj_r2": round(float(m.rsquared_adj), 4),
    }


def perf_corr(d, on):
    df = filter_a(d, on)
    sub = df[df["treat"] == 0][["overall_score", "delegation"]].dropna()
    r, p = stats.pearsonr(sub["overall_score"], sub["delegation"])
    return {"n": int(len(sub)), "r": round(float(r), 3), "p": round(float(p), 4)}


def mechanism(d, on):
    df = filter_a(d, on)
    nondeleg = df[df["delegation"] == 0]
    rates = nondeleg.groupby("treat")["success_last"].agg(["mean", "count"]).to_dict("index")
    pun = nondeleg[nondeleg["treat"] == 0]["success_last"].dropna()
    nopun = nondeleg[nondeleg["treat"] == 1]["success_last"].dropna()
    _, p_succ = stats.ttest_ind(nopun, pun, equal_var=False) if len(pun) > 0 and len(nopun) > 0 else (None, float("nan"))
    pun_perf = nondeleg[nondeleg["treat"] == 0]["overall_score"]
    nopun_perf = nondeleg[nondeleg["treat"] == 1]["overall_score"]
    _, p_perf = stats.ttest_ind(nopun_perf, pun_perf, equal_var=False)
    return {
        "n_pun": int(rates[0]["count"]),
        "n_nopun": int(rates[1]["count"]),
        "succ_pun_pct": round(100 * float(rates[0]["mean"]), 1),
        "succ_nopun_pct": round(100 * float(rates[1]["mean"]), 1),
        "succ_p": round(float(p_succ), 4) if not math.isnan(p_succ) else None,
        "score_pun": round(float(pun_perf.mean()), 2),
        "score_nopun": round(float(nopun_perf.mean()), 2),
        "score_p": round(float(p_perf), 4),
    }


def hypo(d, on):
    df = filter_a(d, on)
    nopun = df[df["treat"] == 1]
    sub = nopun[["delegation", "delegation_hypo"]].dropna()
    diffs = sub["delegation"] - sub["delegation_hypo"]
    n_changed = int((diffs != 0).sum())
    n_drop = int((diffs > 0).sum())
    n_rise = int((diffs < 0).sum())
    if n_changed > 0:
        from scipy.stats import chi2 as chi2_dist
        stat = (n_drop - n_rise) ** 2 / max(n_changed, 1)
        p_mc = float(1 - chi2_dist.cdf(stat, df=1))
    else:
        p_mc = float("nan")
    return {
        "n_pairs": int(len(sub)),
        "actual_pct": round(100 * float(sub["delegation"].mean()), 1) if len(sub) else None,
        "hypo_pct": round(100 * float(sub["delegation_hypo"].mean()), 1) if len(sub) else None,
        "n_drop": n_drop,
        "n_rise": n_rise,
        "p_mcnemar": None if math.isnan(p_mc) else round(p_mc, 4),
    }


def order_eff(d, on):
    df = filter_a(d, on)
    sub = df[["delegation", "treat", "random_order_del"]].dropna()
    sub["treat_x_order"] = sub["treat"] * sub["random_order_del"]
    X = sm.add_constant(
        sub[["treat", "random_order_del", "treat_x_order"]].astype(float),
        has_constant="add",
    )
    m = sm.Logit(sub["delegation"].astype(float), X).fit(disp=False, cov_type="HC1")
    pun = df[df["treat"] == 0]
    nopun = df[df["treat"] == 1]
    pun_table = pd.crosstab(pun["random_order_del"], pun["delegation"]).values
    nopun_table = pd.crosstab(nopun["random_order_del"], nopun["delegation"]).values
    _, p_pun, _, _ = stats.chi2_contingency(pun_table, correction=False)
    _, p_nopun, _, _ = stats.chi2_contingency(nopun_table, correction=False)
    return {
        "interaction_coef": round(float(m.params["treat_x_order"]), 4),
        "interaction_p": round(float(m.pvalues["treat_x_order"]), 4),
        "pun_chi2_p": round(float(p_pun), 4),
        "nopun_chi2_p": round(float(p_nopun), 4),
    }


def belief_dist(d, on):
    df = filter_a(d, on)
    pun = df[df["treat"] == 0]
    out = {}
    for col in ["belief_del_good", "belief_nodel_good", "belief_del_bad", "belief_nodel_bad"]:
        deleg = pun.loc[pun["delegation"] == 1, col].dropna()
        nodel = pun.loc[pun["delegation"] == 0, col].dropna()
        if len(deleg) >= 2 and len(nodel) >= 2:
            _, p_t = stats.ttest_ind(deleg, nodel, equal_var=False)
        else:
            p_t = float("nan")
        out[col] = {
            "deleg_mean": round(float(deleg.mean()), 3) if len(deleg) else None,
            "nodel_mean": round(float(nodel.mean()), 3) if len(nodel) else None,
            "diff_pp": (round(float(deleg.mean() - nodel.mean()), 3)
                       if len(deleg) and len(nodel) else None),
            "p_t": None if math.isnan(p_t) else round(float(p_t), 4),
            "n_deleg": int(len(deleg)),
            "n_nodel": int(len(nodel)),
        }
    return out


def b_overestimation(d, e, on):
    da = filter_a(d, on)
    eb = filter_b(e, on)
    true_mean = float(da["overall_score"].mean())
    a_belief = float(da["wa_confidence"].mean())
    b_belief = float(eb["wa_difficulty"].mean())
    return {
        "true_score_mean": round(true_mean, 3),
        "a_wa_confidence_mean": round(a_belief, 3),
        "b_wa_difficulty_mean": round(b_belief, 3),
        "a_overestimation": round(a_belief - true_mean, 3),
        "b_overestimation": round(b_belief - true_mean, 3),
    }


def b_likert(e, on):
    eb = filter_b(e, on)
    pun = eb[eb["treat"] == 0]
    out = {}
    for likert in ["responsibility", "trust", "perception"]:
        sub = pun[[likert, "nodel_del_bad", "nodel_del_good"]].dropna(subset=[likert])
        n = int(len(sub))
        out[likert] = {"n": n, "mean": round(float(sub[likert].mean()), 3) if n else None}
        for diff in ["nodel_del_bad", "nodel_del_good"]:
            ss = sub[[likert, diff]].dropna()
            if len(ss) >= 3 and ss[likert].std() > 0 and ss[diff].std() > 0:
                r, p = stats.pearsonr(ss[likert], ss[diff])
                out[likert][f"r_x_{diff}"] = round(float(r), 3)
                out[likert][f"p_x_{diff}"] = round(float(p), 4)
            else:
                out[likert][f"r_x_{diff}"] = None
                out[likert][f"p_x_{diff}"] = None
    return out


# ------- formatting -------

def _fmt(v):
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.4f}".rstrip("0").rstrip(".") if v != int(v) else f"{int(v)}"
    return str(v)


def _delta(a, b):
    if a is None or b is None:
        return ""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return ""
    d = b - a
    if abs(d) < 1e-6:
        return "≈0"
    return f"{d:+.4f}".rstrip("0").rstrip(".")


def render_section(title, rows):
    """rows: list of (label, full_value, att_value)"""
    lines = [f"\n## {title}\n",
             "| Metric | Full sample | Attention-pass | Δ |",
             "|---|---:|---:|---:|"]
    for label, full_v, att_v in rows:
        lines.append(f"| {label} | {_fmt(full_v)} | {_fmt(att_v)} | {_delta(full_v, att_v)} |")
    return "\n".join(lines) + "\n"


def render_report(F, A):
    parts = ["# Attention-check robustness comparison\n",
             "Each analysis below is run twice:\n",
             "- **Full sample** — no attention-check exclusion.\n",
             "- **Attention-pass** — `pass_att2 == 1` (Player A excluded on belief-elicitation screen; Player B excluded on punishment-elicitation screen).\n",
             "\n"]

    s, sa = F["sample_sizes"], A["sample_sizes"]
    parts.append(render_section("Sample sizes", [
        ("N Player A total", s["n_a_total"], sa["n_a_total"]),
        ("  Punishment", s["n_a_pun"], sa["n_a_pun"]),
        ("  No-Punishment", s["n_a_nopun"], sa["n_a_nopun"]),
        ("N Player B total", s["n_b_total"], sa["n_b_total"]),
        ("  Punishment", s["n_b_pun"], sa["n_b_pun"]),
        ("  No-Punishment", s["n_b_nopun"], sa["n_b_nopun"]),
    ]))

    for role, key in [("Player A", "balance_player_a"), ("Player B", "balance_player_b")]:
        ba, bb = F[key], A[key]
        rows = []
        for col in ["age", "female", "socio_status", "went_to_uni", "technology_score", "leader"]:
            rows.append((f"{col} mean Pun", ba[col]["mean_pun"], bb[col]["mean_pun"]))
            rows.append((f"{col} mean No-Pun", ba[col]["mean_nopun"], bb[col]["mean_nopun"]))
            rows.append((f"{col} p (treat balance)", ba[col]["p"], bb[col]["p"]))
        parts.append(render_section(f"Balance — {role}", rows))

    h, ha = F["h1_chi_fisher"], A["h1_chi_fisher"]
    parts.append(render_section("H1 — delegation rate by condition", [
        ("delegation rate Punishment %", h["rate_pun_pct"], ha["rate_pun_pct"]),
        ("delegation rate No-Pun %", h["rate_nopun_pct"], ha["rate_nopun_pct"]),
        ("gap (pp)", h["gap_pp"], ha["gap_pp"]),
        ("N Punishment", h["n_pun"], ha["n_pun"]),
        ("N No-Punishment", h["n_nopun"], ha["n_nopun"]),
        ("p (Pearson chi²)", h["p_chi2"], ha["p_chi2"]),
        ("p (Fisher exact)", h["p_fisher"], ha["p_fisher"]),
    ]))

    for col_label, key in [("Logit Col 1 (treat only, full sample)", "logit_col1"),
                            ("Logit Col 2 (treat + score + controls, full sample)", "logit_col2")]:
        c, ca = F[key], A[key]
        parts.append(render_section(col_label, [
            ("N", c["n"], ca["n"]),
            ("treat coef", c["treat_coef"], ca["treat_coef"]),
            ("treat SE", c["treat_se"], ca["treat_se"]),
            ("treat p", c["treat_p"], ca["treat_p"]),
            ("Pseudo R²", c["pseudo_r2"], ca["pseudo_r2"]),
        ]))

    c3, c3a = F["logit_col3"], A["logit_col3"]
    parts.append(render_section("Logit Col 3 (Punishment-only, belief differences + score + controls)", [
        ("N", c3["n"], c3a["n"]),
        ("bel diff (good) coef", c3["bel_good_coef"], c3a["bel_good_coef"]),
        ("bel diff (good) p", c3["bel_good_p"], c3a["bel_good_p"]),
        ("bel diff (bad) coef", c3["bel_bad_coef"], c3a["bel_bad_coef"]),
        ("bel diff (bad) p", c3["bel_bad_p"], c3a["bel_bad_p"]),
        ("overall_score coef", c3["score_coef"], c3a["score_coef"]),
        ("overall_score p", c3["score_p"], c3a["score_p"]),
        ("Pseudo R²", c3["pseudo_r2"], c3a["pseudo_r2"]),
    ]))

    h2_, h2a = F["h2_paired"], A["h2_paired"]
    parts.append(render_section("H2 — Player B punishment cells, paired tests", [
        ("N Player B (Punishment cond.)", h2_["n"], h2a["n"]),
        ("punish_del_good £", h2_["punish_del_good_mean"], h2a["punish_del_good_mean"]),
        ("punish_nodel_good £", h2_["punish_nodel_good_mean"], h2a["punish_nodel_good_mean"]),
        ("punish_del_bad £", h2_["punish_del_bad_mean"], h2a["punish_del_bad_mean"]),
        ("punish_nodel_bad £", h2_["punish_nodel_bad_mean"], h2a["punish_nodel_bad_mean"]),
        ("diff bad (nodel-del) £", h2_["diff_bad_mean"], h2a["diff_bad_mean"]),
        ("diff good (nodel-del) £", h2_["diff_good_mean"], h2a["diff_good_mean"]),
        ("paired-t p (bad)", h2_["p_bad_t"], h2a["p_bad_t"]),
        ("Wilcoxon p (bad)", h2_["p_bad_w"], h2a["p_bad_w"]),
        ("paired-t p (good)", h2_["p_good_t"], h2a["p_good_t"]),
        ("Wilcoxon p (good)", h2_["p_good_w"], h2a["p_good_w"]),
        ("MDE bad (£, 80% power)", h2_["mde_bad"], h2a["mde_bad"]),
        ("MDE good (£, 80% power)", h2_["mde_good"], h2a["mde_good"]),
        ("never punishes (n)", h2_["n_never_punish"], h2a["n_never_punish"]),
        ("never punishes (%)", h2_["pct_never_punish"], h2a["pct_never_punish"]),
    ]))

    pr, pra = F["punish_reg"], A["punish_reg"]
    parts.append(render_section("Punishment regression — pooled OLS, clustered SE", [
        ("N (subject-by-cell)", pr["n_obs"], pra["n_obs"]),
        ("delegated coef", pr["delegated_coef"], pra["delegated_coef"]),
        ("delegated p", pr["delegated_p"], pra["delegated_p"]),
        ("bad_outcome coef", pr["bad_coef"], pra["bad_coef"]),
        ("bad_outcome p", pr["bad_p"], pra["bad_p"]),
        ("interaction coef", pr["interaction_coef"], pra["interaction_coef"]),
        ("interaction p", pr["interaction_p"], pra["interaction_p"]),
        ("adj R²", pr["adj_r2"], pra["adj_r2"]),
    ]))

    pc, pca = F["perf_corr_pun"], A["perf_corr_pun"]
    parts.append(render_section("Performance × delegation correlation (Punishment cond. only)", [
        ("N", pc["n"], pca["n"]),
        ("Pearson r", pc["r"], pca["r"]),
        ("p", pc["p"], pca["p"]),
    ]))

    me, mea = F["mechanism_effort"], A["mechanism_effort"]
    parts.append(render_section("Mechanism / effort — non-delegators", [
        ("n non-delegators Punishment", me["n_pun"], mea["n_pun"]),
        ("n non-delegators No-Pun", me["n_nopun"], mea["n_nopun"]),
        ("success rate Punishment %", me["succ_pun_pct"], mea["succ_pun_pct"]),
        ("success rate No-Pun %", me["succ_nopun_pct"], mea["succ_nopun_pct"]),
        ("p (success rate diff)", me["succ_p"], mea["succ_p"]),
        ("mean overall_score Pun", me["score_pun"], mea["score_pun"]),
        ("mean overall_score No-Pun", me["score_nopun"], mea["score_nopun"]),
        ("p (score diff)", me["score_p"], mea["score_p"]),
    ]))

    hp, hpa = F["hypo_delegation"], A["hypo_delegation"]
    parts.append(render_section("Hypothetical delegation (No-Pun within-subject)", [
        ("n pairs", hp["n_pairs"], hpa["n_pairs"]),
        ("actual delegation %", hp["actual_pct"], hpa["actual_pct"]),
        ("hypothetical delegation %", hp["hypo_pct"], hpa["hypo_pct"]),
        ("n switched: would-stop", hp["n_drop"], hpa["n_drop"]),
        ("n switched: would-start", hp["n_rise"], hpa["n_rise"]),
        ("McNemar p", hp["p_mcnemar"], hpa["p_mcnemar"]),
    ]))

    oe, oea = F["order_effects"], A["order_effects"]
    parts.append(render_section("Order effects (random_order_del)", [
        ("treat × order coef", oe["interaction_coef"], oea["interaction_coef"]),
        ("treat × order p", oe["interaction_p"], oea["interaction_p"]),
        ("p (order in Punishment)", oe["pun_chi2_p"], oea["pun_chi2_p"]),
        ("p (order in No-Pun)", oe["nopun_chi2_p"], oea["nopun_chi2_p"]),
    ]))

    bd, bda = F["belief_dist"], A["belief_dist"]
    rows = []
    for col in ["belief_del_good", "belief_nodel_good", "belief_del_bad", "belief_nodel_bad"]:
        rows.append((f"{col} delegators £", bd[col]["deleg_mean"], bda[col]["deleg_mean"]))
        rows.append((f"{col} non-delegators £", bd[col]["nodel_mean"], bda[col]["nodel_mean"]))
        rows.append((f"{col} diff (del-nodel)", bd[col]["diff_pp"], bda[col]["diff_pp"]))
        rows.append((f"{col} t-test p", bd[col]["p_t"], bda[col]["p_t"]))
        rows.append((f"{col} n delegators", bd[col]["n_deleg"], bda[col]["n_deleg"]))
        rows.append((f"{col} n non-delegators", bd[col]["n_nodel"], bda[col]["n_nodel"]))
    parts.append(render_section("Belief distributions — delegators vs non-delegators (Punishment cond.)", rows))

    bo, boa = F["b_overestimation"], A["b_overestimation"]
    parts.append(render_section("Player B beliefs about Player A performance", [
        ("true score mean (Player A)", bo["true_score_mean"], boa["true_score_mean"]),
        ("Player A wa_confidence mean", bo["a_wa_confidence_mean"], boa["a_wa_confidence_mean"]),
        ("Player B wa_difficulty mean", bo["b_wa_difficulty_mean"], boa["b_wa_difficulty_mean"]),
        ("A overestimation (pts)", bo["a_overestimation"], boa["a_overestimation"]),
        ("B overestimation (pts)", bo["b_overestimation"], boa["b_overestimation"]),
    ]))

    bl, bla = F["b_likert"], A["b_likert"]
    rows = []
    for likert in ["responsibility", "trust", "perception"]:
        rows.append((f"{likert} n", bl[likert]["n"], bla[likert]["n"]))
        rows.append((f"{likert} mean", bl[likert]["mean"], bla[likert]["mean"]))
        rows.append((f"{likert} × nodel_del_bad r", bl[likert]["r_x_nodel_del_bad"], bla[likert]["r_x_nodel_del_bad"]))
        rows.append((f"{likert} × nodel_del_bad p", bl[likert]["p_x_nodel_del_bad"], bla[likert]["p_x_nodel_del_bad"]))
        rows.append((f"{likert} × nodel_del_good r", bl[likert]["r_x_nodel_del_good"], bla[likert]["r_x_nodel_del_good"]))
        rows.append((f"{likert} × nodel_del_good p", bl[likert]["p_x_nodel_del_good"], bla[likert]["p_x_nodel_del_good"]))
    parts.append(render_section("Player B Likert × punishment correlations", rows))

    return "".join(parts)


def main() -> None:
    d = load_delegator()
    e = load_evaluator()

    results = {}
    for label, on in [("full_sample", False), ("attention_pass", True)]:
        print(f"\n----- running {label} -----")
        bag = {}
        bag["sample_sizes"] = sample_sizes(d, e, on)
        bag["balance_player_a"] = balance(d, on)
        bag["balance_player_b"] = balance(e, on)
        bag["h1_chi_fisher"] = h1(d, on)
        bag["logit_col1"] = logit_col1(d, on)
        bag["logit_col2"] = logit_col2(d, on)
        bag["logit_col3"] = logit_col3(d, on)
        bag["h2_paired"] = h2(e, on)
        bag["punish_reg"] = punishment_reg(e, on)
        bag["perf_corr_pun"] = perf_corr(d, on)
        bag["mechanism_effort"] = mechanism(d, on)
        bag["hypo_delegation"] = hypo(d, on)
        bag["order_effects"] = order_eff(d, on)
        bag["belief_dist"] = belief_dist(d, on)
        bag["b_overestimation"] = b_overestimation(d, e, on)
        bag["b_likert"] = b_likert(e, on)
        results[label] = bag

    json_path = OUTPUTS / "attention_check_comparison.json"
    md_path = OUTPUTS / "attention_check_comparison.md"
    json_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    md_path.write_text(render_report(results["full_sample"], results["attention_pass"]),
                       encoding="utf-8")
    print(f"\nWrote: {json_path}")
    print(f"Wrote: {md_path}")


if __name__ == "__main__":
    main()
