# Results-section revision — exploratory sandbox

Ad-hoc analyses supporting the paragraph-by-paragraph revision of `manuscript/results.tex`.

## How it's used

- `explore.py` is a single running script, sectioned by paragraph (`### P01`, `### P02`, …) following the continuous numbering of the planning files in `quality_reports/results_revision/`.
- Each paragraph's section runs whatever ad-hoc checks the revision needs (means, contrasts, robustness slices, sample counts, etc.).
- Outputs land in `output/` and are then summarised into the corresponding `quality_reports/results_revision/NN_<slug>.md` planning file.
- This is a 60/100-threshold sandbox per `.claude/rules/exploration-fast-track.md` — code does not need to be production-grade.

## Data sources

Cleaned data loaded via the production helpers (`scripts/python/lib/io.py`):

- `load_delegator()` → `data/clean/delegator_cleaned.xlsx` (Player A / decision-makers)
- `load_evaluator()` → `data/clean/evaluator_cleaned.xlsx` (Player B / recipients)

Both functions cache to `.parquet` siblings on first read.

## Running

From the repo root:

```bash
python explorations/results-revision/explore.py
```

Or interactively, run a single paragraph block in your editor.
