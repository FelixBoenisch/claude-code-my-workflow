# Legacy cleaning pipeline (raw → clean)

This directory holds the **Jupyter notebooks** that turn the raw oTree exports in
`../raw/` into the cleaned analysis files in `../clean/`. They predate the
canonical Python analysis pipeline at [`scripts/python/`](../../scripts/python/)
and have not yet been ported to scripts.

## Pipeline

```
data/raw/                                                 (oTree CSV exports)
  ↓  01 raw data treatment/00..03_*.ipynb                 (per-wave cleaning)
data/interim/01_cleaned/*.xlsx
  ↓  01 raw data treatment/04_data_merging.ipynb          (append waves)
data/interim/02_appended/*_full.xlsx
  ↓  02 merge pagetimes/match_with_pagetimes.ipynb        (join page-timing data)
data/interim/03_pagetimes/*_full_merged.xlsx
  ↓  04 delegator/00_delegator cleaning.ipynb             (final delegator clean)
  ↓  05 evaluator/00_evaluator_cleaning.ipynb             (final evaluator clean)
data/clean/{delegator,evaluator}_cleaned.xlsx             ← canonical inputs to scripts/python/
```

## Why kept

The Python analysis pipeline (`scripts/python/`) reads `data/clean/*.xlsx`.
Those files exist and were produced by these notebooks. Until the cleaning is
ported to Python, deleting this directory would make `data/raw/` un-reproducible
to `data/clean/`.

## What's safe to ignore

- `00 within session calculations/` — self-labeled obsolete
- `03 old pilot analysis/` — self-labeled old; references hardcoded Dropbox paths
- `Link Evaluator and Delegator Analysis.ipynb` and `power.ipynb` (top of dir) —
  misplaced; reference unqualified filenames

## Migration TODO

Port to `scripts/python/cleaning/01_..09_*.py`, save intermediates as `.parquet`
under `data/interim/`, and confirm output `data/clean/` files are byte-equivalent
to the existing ones. Once verified, this directory can be deleted.
