# Legacy cleaning pipeline (raw → clean)

This directory holds the **Jupyter notebooks** that turn the raw oTree exports in
[`../raw/`](../raw/) into the cleaned analysis files in [`../clean/`](../clean/).
They predate the canonical Python analysis pipeline at
[`scripts/python/`](../../scripts/python/) and have not yet been ported.

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

## How to re-run from raw data

There is **no one-command re-run from raw**. To regenerate the cleaned files
from `data/raw/`, open Jupyter and execute the following 8 notebooks in order:

1. `01 raw data treatment/00_pre-pilot_and_pilot.ipynb`
2. `01 raw data treatment/01_main.ipynb`
3. `01 raw data treatment/02_main_no_punish.ipynb`
4. `01 raw data treatment/03_main_no_punish2.ipynb`
5. `01 raw data treatment/04_data_merging.ipynb`
6. `02 merge pagetimes/match_with_pagetimes.ipynb`
7. `04 delegator/00_delegator cleaning.ipynb`
8. `05 evaluator/00_evaluator_cleaning.ipynb`

All paths inside these notebooks have been updated to the current folder layout
(`raw/`, `interim/`, `clean/`); cells that previously referenced
`raw_data/`, `processed_data/...`, or hardcoded Dropbox paths now point at the
current locations. Each notebook runs independently against the outputs of the
preceding one.

### Pandas 3.0 caveat

The notebooks were originally written against an older pandas version. The
project's pinned environment ([`requirements.txt`](../../requirements.txt))
uses `pandas==3.0.2`, where two patterns the notebooks use no longer work:

1. `int(some_pandas_Series)` and `float(some_pandas_Series)` raise `TypeError`
   on pandas 3.0 (worked silently on 2.x). Affects the bonus-payoff cells in
   notebooks 1, 2, 3, 4 (the ones that compute Prolific bonuses alongside the
   cleaning).
2. Some `.loc` assignments may emit `FutureWarning` or fail on dtype mismatches
   that were silently coerced in older pandas.

If you re-run from raw, expect to apply small fixes (`int(s)` → `int(s.iloc[0])`,
`float(s)` → `float(s.iloc[0])`) before the bonus cells will execute. The cleaning
cells themselves are unaffected; the bugs sit in the bonus-calc tail. The
[bonus calculation has been ported separately](../../scripts/python/10_payoffs.py)
and is no longer needed from these notebooks.

### Reproducing without re-running

The cleaned files in [`../clean/`](../clean/) and intermediates in
[`../interim/`](../interim/) are gitignored due to PII content. You should
already have them locally from the original pipeline run; if you don't (e.g.,
fresh clone), restore them from your Dropbox copy of `Project Algorithm` rather
than re-running the notebooks. The Python analysis pipeline then reads from
`../clean/` directly, no notebook execution required.

## What's safe to ignore

- `00 within session calculations/` — self-labeled obsolete
- `03 old pilot analysis/` — self-labeled old; references hardcoded Dropbox paths
- `Link Evaluator and Delegator Analysis.ipynb` and `power.ipynb` (top of dir) —
  misplaced; reference unqualified filenames

## Migration TODO

A proper port would move the cleaning logic to `scripts/python/cleaning/01_..08_*.py`,
strip the bonus-calc cells (already replaced by [10_payoffs.py](../../scripts/python/10_payoffs.py)),
save intermediates as `.parquet`, and add a `run_everything.py` orchestrator
chaining cleaning → analysis → compile. Estimated effort: ~1 day. Once verified
DataFrame-equivalent (xlsx metadata + `random.randint` calls in the bonus cells
prevent strict byte-equivalence), this directory can be deleted.
