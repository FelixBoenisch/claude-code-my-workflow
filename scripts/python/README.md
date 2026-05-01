# Python analysis pipeline

End-to-end pipeline from `data/clean/{delegator,evaluator}_cleaned.xlsx` to the
manuscript's tables, figures, and inline numbers.

## Quick start

```bash
# from repo root
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe scripts/python/run_all.py
```

Outputs land in:

- `manuscript/figures/` — PNGs the manuscript references
- `tables/` — `.tex` fragments that the manuscript `\input{}`s
- `scripts/python/_outputs/numbers.json` — every numeric claim in the manuscript

## Pipeline

| Step | Script | Produces |
|---|---|---|
| 1 | `01_sample_summary.py`  | sample sizes, time-on-task, attention pass rates, mean performance (manifest only) |
| 2 | `02_balance.py`         | `tables/balance_player_a.tex`, `tables/balance_player_b.tex` |
| 3 | `03_h1_delegation.py`   | `figures/delegation_shares.png`; H1 chi² + Fisher tests |
| 4 | `04_logit_delegation.py`| `tables/reg_delegation.tex`, `tables/reg_delegation_full.tex` (Tables 1 + A2) |
| 5 | `05_h2_punishment.py`   | `figures/punishment.png`, `figures/punishment_shares.png`; paired-t / Wilcoxon; MDE |
| 6 | `06_logit_punishment.py`| `tables/reg_punishment.tex` (Appendix punishment regression) |
| 7 | `07_performance.py`     | `figures/performance.png`, `figures/performance_delegation_scatter.png` |
| 8 | `08_mechanism_effort.py`| Mechanism (M2) numbers (manifest only) |

## Layout

```
scripts/python/
├── run_all.py              # orchestrator: imports each step and runs main()
├── lib/
│   ├── paths.py            # all project paths (single source of truth)
│   ├── io.py               # data loaders (xlsx → parquet cache)
│   ├── manifest.py         # _outputs/numbers.json: every claim the paper makes
│   ├── fmt.py              # AEA-style number formatters (no significance stars)
│   └── regtable.py         # multi-column regression-table builder
├── _outputs/
│   └── numbers.json        # source of truth for /audit-reproducibility
└── 0X_*.py                 # the eight pipeline scripts
```

## Conventions

- **Treat-condition coding.** `treat == 0` is the **Punishment** condition
  (the "real-world default" — punishment possible). `treat == 1` is the
  **No-Punishment** condition (punishment switched off). Coefficients on the
  `treat` regressor are therefore the effect of moving from Punishment to
  No-Punishment; positive means more delegation under No-Punishment, which is
  what the data show.
- **AEA style.** No significance stars in any table. Standard errors in
  parentheses; exact two-sided p-values reported in table notes.
- **Robust standard errors.** Logits use HC1; the punishment regression
  clusters at the Player B level.
- **Manifest discipline.** Every numeric claim that appears in the manuscript
  body must also appear in `_outputs/numbers.json` with a key whose name reflects
  what it measures, so `/audit-reproducibility` can verify them mechanically.

## Cleaning pipeline (not yet ported)

The notebooks under `data/code_legacy/` produce the cleaned files this pipeline
consumes. They have not yet been ported to Python — see
[`data/code_legacy/README.md`](../../data/code_legacy/README.md).
