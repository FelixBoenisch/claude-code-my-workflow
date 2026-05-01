# Cross-Artifact Reproducibility — Algorithms and Responsibility

**Date:** 2026-05-01
**Manuscript:** manuscript/main.tex
**Outputs dir:** scripts/python/_outputs/ — DOES NOT EXIST
**Status:** CANNOT VERIFY (no scripts, no outputs)

## Finding

The manuscript reports specific numeric claims (delegation shares, regression coefficients, punishment amounts, balance test p-values, performance averages) but the repository contains **no analysis scripts** that produce them:

- `scripts/python/` contains only `.gitkeep`
- `scripts/python/_outputs/` does not exist
- `tables/` is empty (Tables 1, A1, A2 are hand-coded LaTeX in `manuscript/*.tex`)
- `manuscript/figures/` contains four PNGs (`delegation_shares.png`, `performance.png`, `punishment.png`, `punishment_shares.png`) with no provenance: no parent script, no input data trail

## Implications for the editor

Per `.claude/rules/cross-artifact-review.md` Step 5 and the AER profile (Replication 5→10), this is **desk-reject-adjacent** in `--peer AER` mode. AER's Data and Code Availability Policy is enforced strictly at acceptance, and increasingly probed during review. The Data Editor will require a complete pipeline.

This is a *pre-submission readiness* failure rather than an evidence of fraud — the numbers may all be correct. But the editor cannot evaluate any reproducibility claim, and every numeric value in the manuscript is currently un-auditable.

## Numeric claims that need a producing script

(Selection — list is not exhaustive.)

| Claim | Section | Required script |
|---|---|---|
| 42.5% Baseline delegation, 59.3% Treatment delegation | results.tex §5.2 | `03_delegation.py` |
| χ²(1) p = 0.049, Fisher p = 0.041 | results.tex §5.2 | same |
| Logit coefficients 0.677/0.757/-0.609 etc. | Tables 1, A2 | `03_delegation.py` |
| Punishment averages £0.310/0.311/0.494/0.571 | results.tex §5.3 | `04_punishment.py` |
| Paired-t p = 0.153, Wilcoxon p = 0.533 | results.tex §5.3 | same |
| Mean performance 3.05; Treatment 3.12, Baseline 2.97 | results.tex §5.2, §5.5 | `02_performance.py` |
| Balance table p-values (Table A1) | appendix.tex §A.1 | `02_balance.py` |
| Attention-check pass rates (135/161 = 83.9%) | results.tex §5.1 | `01_clean.py` |

## Recommendation

Build the pipeline before any external review. Suggest invoking `/data-analysis` with the raw Prolific export to scaffold `01_clean.py` → `04_punishment.py`, with each numeric output written as a `.tex` fragment under `tables/` or as a CSV the manuscript can `\input{}` via siunitx.
