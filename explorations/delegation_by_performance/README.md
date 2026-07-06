# Delegation by performance — discussion-section checks

**Goal:** Support the restructured "Discussion of results" (results.tex) with checks on how the delegation decision relates to first-ten-rounds performance across conditions.

**Status:** Active (2026-07-06). Candidates for graduation into `scripts/python/` once Felix finalizes which numbers enter the manuscript.

## Scripts (run from `scripts/python/` or with it on `sys.path`)

- `scripts/tercile_check.py` — delegation rates by performance bin (0–2 / 3 / 4+, plus finer splits) × condition, full sample and `pass_att2` passers; Fisher tests per bin; treat × score Logit interaction.
- `scripts/balance_means.py` — per-condition means of `overall_score` and balance tests (t-test, Mann-Whitney).
- `scripts/scatter_full_vs_passers.py` — side-by-side version of `fig:performance_delegation_scatter` (full sample vs passers) with per-condition Pearson r/p annotated → `output/perf_delegation_scatter_full_vs_passers.png`.

## Key findings

1. **Treatment gap widens with performance** (full sample): −11.0 pp (scores 0–2), −15.6 pp (3), −26.8 pp (4+, Fisher p=0.059). Passers: −12.1 / −16.2 / −28.9 pp (p=0.065). Low performers do NOT delegate more under Punishment → failure-avoidance variant of process ownership unsupported.
2. **Treat × score interaction not significant** (Logit p=0.29 full, 0.34 passers) — pattern is descriptive.
3. **Manifest/figure mismatch in `07_performance.py`:** the scatter plots passers only (`pass_att2==1`), but `perf_corr_punishment_r/p` (−0.189/0.092) is computed on the FULL sample. Passers values: r=−0.224, p=0.083. The manuscript currently cites the full-sample statistic as "among attention-check passers".
4. Per-condition performance: Punishment 2.76 vs No-Punishment 3.09 (t-test p=0.121); confidence 4.65 vs 4.87 (p=0.466). Direction of the (insignificant) performance gap is conservative for Result 1.
