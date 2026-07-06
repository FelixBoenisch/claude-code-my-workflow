# Session log

## 2026-07-06
- Ran tercile/bin check of delegation × performance × condition to separate the two process-ownership variants; failure-avoidance unsupported (low performers do not delegate more under Punishment).
- Computed per-condition performance/confidence means for the "Selection into conditions" paragraph.
- Rendered fig:performance_delegation_scatter in full-sample and passers versions side by side; discovered `07_performance.py` computes the manifest correlation on the full sample while plotting passers → manuscript cites full-sample r/p as passers. Pending decision: which sample the figure + statistic should use.
- RESOLVED: Felix chose full sample for the scatter; `07_performance.py` updated (filter removed, passers + No-Punishment correlations added to manifest).
- GRADUATED: condition-level balance tests promoted to the pipeline — `01_sample_summary.py` now records overall_score/wa_confidence per condition + Welch t-tests; `24_performance_by_delegation.py` records the delegator-composition Welch test (p=0.0389). Pipeline convention is Welch (equal_var=False) throughout; manuscript's p=0.039 confirmed as Welch. Bin-share numbers (tercile_check.py) NOT promoted — currently not cited in results.tex.
