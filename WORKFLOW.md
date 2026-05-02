# Project workflow — Algorithms and Responsibility

Single source of truth for the full pipeline: from raw oTree exports to the final
manuscript PDF. This document describes every code file, its inputs/outputs, the
variables it reads or produces, and the conventions that hold across the repo.

For deeper documentation of specific layers see:

- [`data/README.md`](data/README.md) — full variable dictionary (218 columns)
- [`data/code_legacy/README.md`](data/code_legacy/README.md) — cleaning notebooks
- [`scripts/python/README.md`](scripts/python/README.md) — analysis pipeline
- [`notebooks/exploration/README.md`](notebooks/exploration/README.md) — exploration shelf
- [`master_supporting_docs/payments/README.md`](master_supporting_docs/payments/README.md) — pilot bonuses

---

## 1 · End-to-end pipeline

```
                                    ┌──────────────────────────┐
                                    │  data/raw/  (gitignored) │
                                    │  oTree CSV exports per   │
                                    │  session, Prolific demo. │
                                    └────────────┬─────────────┘
                                                 │  Step 1 — cleaning (Jupyter)
                                                 │  data/code_legacy/   (8 notebooks)
                                                 ▼
                                    ┌──────────────────────────┐
                                    │  data/interim/           │
                                    │  01_cleaned/  (per-wave) │
                                    │  02_appended/ (concat)   │
                                    │  03_pagetimes/ (joined)  │
                                    └────────────┬─────────────┘
                                                 │
                                                 ▼
                                    ┌──────────────────────────┐
                                    │  data/clean/             │
                                    │  delegator_cleaned.xlsx  │
                                    │  evaluator_cleaned.xlsx  │
                                    └────────────┬─────────────┘
                                                 │  Step 2 — analysis (Python)
                                                 │  scripts/python/    (10 scripts)
                                                 │  python scripts/python/run_all.py
                                                 ▼
                       ┌─────────────────────────────────────────────────┐
                       │                                                 │
            tables/*.tex                       manuscript/figures/*.png         scripts/python/_outputs/
            (5 LaTeX fragments)                (5 PNGs)                         numbers.json (manifest)
                       │                                                 │
                       └────────────────┬────────────────────────────────┘
                                        │  Step 3 — typeset (LaTeX)
                                        │  pdflatex; bibtex; pdflatex; pdflatex
                                        ▼
                                    ┌──────────────────────────┐
                                    │  manuscript/main.pdf     │
                                    │  (36 pages)              │
                                    └──────────────────────────┘
```

There is no one-command runner from raw to PDF. The three steps above are
executed independently. See §6 (How to reproduce) for the commands.

---

## 2 · Repository layout

```
paper/
├── WORKFLOW.md                      ← this file
├── README.md                        (template README — outdated; project repurposed)
├── CLAUDE.md / MEMORY.md            (Claude-Code workflow conventions)
├── requirements.txt                 (Python env: 8 analysis packages)
├── .venv/                           (gitignored)
│
├── manuscript/                      ← LaTeX paper
│   ├── main.tex
│   ├── introduction.tex / literature.tex / design.tex / results.tex /
│   │   conclusion.tex / appendix.tex
│   ├── ProjectAlgorithm.bib
│   ├── figures/                     ← 5 generated PNGs (\includegraphics targets)
│   └── main.pdf                     ← compiled output
│
├── tables/                          ← 5 generated .tex fragments (\input targets)
│
├── scripts/python/                  ← canonical analysis pipeline
│   ├── 01..10_*.py                  (numbered scripts, one per analysis step)
│   ├── lib/                         (shared utilities)
│   ├── _outputs/numbers.json        (manifest of every numeric paper claim)
│   ├── run_all.py                   (orchestrator)
│   └── README.md
│
├── data/
│   ├── raw/                         ← oTree + Prolific exports (gitignored, PII)
│   ├── interim/                     ← cleaning intermediates (gitignored)
│   ├── clean/                       ← analysis-ready (gitignored)
│   ├── code_legacy/                 ← cleaning Jupyter notebooks (raw → clean)
│   └── README.md                    ← full variable dictionary
│
├── notebooks/exploration/           ← 12 exploratory notebooks + README
│
├── master_supporting_docs/
│   ├── payments/                    (pilot bonus list — pilot_bonuses.txt is gitignored)
│   ├── screenshots/                 (oTree screen captures by player role)
│   └── supporting_papers/ + supporting_slides/
│
└── quality_reports/
    ├── peer_review_algorithms_and_responsibility/   (5-report --peer AER review)
    └── cross_artifact_algorithms_and_responsibility/(reproducibility audit)
```

---

## 3 · Step 1 — Cleaning (Jupyter notebooks)

Located in [`data/code_legacy/`](data/code_legacy/). Run **in this order**:

| # | Notebook | Reads | Writes | Purpose |
|---|---|---|---|---|
| 1 | `01 raw data treatment/00_pre-pilot_and_pilot.ipynb` | `data/raw/{pre_pilot,pilot}/{delegator,evaluator}/all_apps_wide-*.csv` + `prolific_export_*.csv` | `data/interim/01_cleaned/{delegator,evaluator}_pilot.xlsx` | Concatenate pre-pilot + pilot waves; rename oTree columns; merge demographic data from Prolific |
| 2 | `01 raw data treatment/01_main.ipynb` | `data/raw/main/{delegator,evaluator_1..4}/all_apps_wide-*.csv` + Prolific exports | `data/interim/01_cleaned/{delegator,evaluator}_main.xlsx` | Same for the **Punishment** wave (June 19, 2023) |
| 3 | `01 raw data treatment/02_main_no_punish.ipynb` | `data/raw/main/{delegator_no_punish,evaluator_no_punish_1..3}/...` | `data/interim/01_cleaned/{delegator,evaluator}_main_no_punish.xlsx` | First **No-Punishment** wave (June 19–20, 2023) |
| 4 | `01 raw data treatment/03_main_no_punish2.ipynb` | `data/raw/main/{delegator_no_punish_2,evaluator_no_punish_4..5}/...` | `data/interim/01_cleaned/{delegator,evaluator}_main_no_punish2.xlsx` | Second No-Punishment wave (June 21, 2023) |
| 5 | `01 raw data treatment/04_data_merging.ipynb` | All four `01_cleaned/*` files above | `data/interim/02_appended/{delegator,evaluator}_full.xlsx` | Append all waves into single delegator + evaluator DataFrames |
| 6 | `02 merge pagetimes/match_with_pagetimes.ipynb` | `02_appended/*_full.xlsx` + all `data/raw/**/PageTimes-*.csv` | `data/interim/03_pagetimes/{delegator,evaluator}_full_merged.xlsx` | Join page-by-page timing data so per-screen time is available |
| 7 | `04 delegator/00_delegator cleaning.ipynb` | `03_pagetimes/delegator_full_merged.xlsx` | `data/clean/delegator_cleaned.xlsx` | Final Player A clean: construct derived variables (treat, female, technology_score, attention-check passes, belief differences, …) |
| 8 | `05 evaluator/00_evaluator_cleaning.ipynb` | `03_pagetimes/evaluator_full_merged.xlsx` | `data/clean/evaluator_cleaned.xlsx` | Final Player B clean: same construction |

### Notebooks not in the canonical pipeline

| Notebook | Status |
|---|---|
| `00 within session calculations/Delegator_after Session.ipynb` | Operational (computes during-session payments to send to Prolific). Not analytical. |
| `03 old pilot analysis/*` | Self-labelled "old"; pilot-only analyses superseded by main waves |
| `04 delegator/01_delegator analysis.ipynb` | Old analysis notebook; figure-producing cells now in `scripts/python/` |
| `05 evaluator/01_evaluator analysis.ipynb` | Same |
| `Link Evaluator and Delegator Analysis.ipynb` | Cross-side exploratory analysis |
| `power.ipynb` | Power calculation sketch |

For exploratory equivalents kept live, see [`notebooks/exploration/`](notebooks/exploration/).

### Pandas 3.0 compatibility note

These notebooks were written against an older pandas. The pinned environment
uses `pandas==3.0.2`, where `int(some_pandas_Series)` and
`float(some_pandas_Series)` raise `TypeError`. The bonus-payoff cells inside
notebooks 1–4 use those idioms. The cleaning cells themselves are unaffected;
only the bonus tail crashes. Bonus computation has been ported separately to
[`scripts/python/10_payoffs.py`](scripts/python/10_payoffs.py).

---

## 4 · Step 2 — Analysis (Python scripts)

Located in [`scripts/python/`](scripts/python/). Run via `python scripts/python/run_all.py`.

### Library code (`scripts/python/lib/`)

| File | Purpose |
|---|---|
| `paths.py` | Single source of truth for all project paths (RAW, INTERIM, CLEAN, MANUSCRIPT, FIGURES, TABLES, OUTPUTS). |
| `io.py` | Data loaders. Caches `xlsx` → `parquet` on first call for ~10× faster subsequent reads. |
| `manifest.py` | Append-only JSON manifest of every numeric claim the paper makes; written to `_outputs/numbers.json` for `/audit-reproducibility`. |
| `fmt.py` | AEA-style number formatters (no significance stars). |
| `regtable.py` | Multi-column regression-table builder; emits `\input{}`-able LaTeX. |

### Pipeline scripts

| # | Script | Reads | Writes | Computes |
|---|---|---|---|---|
| 1 | `01_sample_summary.py` | `data/clean/*` | `_outputs/numbers.json` | N per role, time-on-task, attention pass rates (Player A 81.4%, Player B 83.9%), mean overall_score (2.93) |
| 2 | `02_balance.py` | `data/clean/*` | `tables/balance_player_a.tex`, `tables/balance_player_b.tex` | Two-sided t-tests + chi-squared on age, female, SES, university, tech score, leadership across condition |
| 3 | `03_h1_delegation.py` | `data/clean/delegator_cleaned.xlsx` | `manuscript/figures/delegation_shares.png` + manifest | H1 chi² (p=0.033 uncorrected) and Fisher exact (p=0.041); delegation shares 42.5% Punishment vs 59.3% No-Punishment |
| 4 | `04_logit_delegation.py` | `data/clean/delegator_cleaned.xlsx` | `tables/reg_delegation.tex` (Table 1), `tables/reg_delegation_full.tex` (Table A2) | 3-column logit: Col 1 unconditional, Col 2 with controls, Col 3 Punishment-only with belief differences. Robust HC1 SEs |
| 5 | `05_h2_punishment.py` | `data/clean/{delegator,evaluator}_cleaned.xlsx` | `manuscript/figures/{punishment,punishment_shares}.png` + manifest | Paired-t (p=0.153) and Wilcoxon (p=0.533) on bad-outcome cell; cell means; minimum detectable effect at 80% power; share never-punishing (41.8%) |
| 6 | `06_logit_punishment.py` | `data/clean/evaluator_cleaned.xlsx` | `tables/reg_punishment.tex` | OLS of Player B punishment on (delegated, bad_outcome, interaction, demographics); SEs clustered at Player B level |
| 7 | `07_performance.py` | `data/clean/delegator_cleaned.xlsx` | `manuscript/figures/{performance,performance_delegation_scatter}.png` + manifest | Score distribution + KDE of confidence beliefs; Pearson correlation (r=−0.19, p=0.092) of performance with delegation in Punishment cond |
| 8 | `08_mechanism_effort.py` | `data/clean/delegator_cleaned.xlsx` | `_outputs/numbers.json` | M2 (effort) numbers: 45.5% non-delegator success in No-Punishment vs 21.7% in Punishment; ex-ante performance balance |
| 9 | `09_consort.py` | `data/clean/*` | `_outputs/numbers.json` | CONSORT counts by condition × role: completed, attention-excluded, analysis sample |
| 10 | `10_payoffs.py` | `data/clean/*` | `_outputs/numbers.json` | Mean bonus £2.49 Player A, £2.30 Player B (excluding Prolific show-up fee + MPL outcome) |

`run_all.py` imports each module and calls its `main()`. Total runtime ~4 seconds.

---

## 5 · Step 3 — Typeset (LaTeX)

Located in [`manuscript/`](manuscript/). Composed of:

| File | Section |
|---|---|
| `main.tex` | Document class, packages, abstract, `\input{}` of all section files, bibliography |
| `introduction.tex` | §1 |
| `literature.tex` | §2 (with subsection on reconciling Feier et al.) |
| `design.tex` | §3 (Conditions overview figure, sample, procedure for each player, hypotheses, identification) |
| `results.tex` | §4 (sample/balance, H1, H2, beliefs, mechanism) — `\input{../tables/reg_delegation.tex}` |
| `conclusion.tex` | §5 (mechanism, implications, limitations, future research) |
| `appendix.tex` | A1 condition balance, A1b same for Player B, A2 full regression, A.regpunishment, PAP deviations table, CONSORT diagram, experimental timelines, punishment frequencies |
| `ProjectAlgorithm.bib` | Bibliography (50+ entries, including Holt & Laury 2002, de Quidt et al. 2018) |

### Compile

```bash
cd manuscript
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Produces `main.pdf` (36 pages, builds cleanly with `aer.bst` + `utf8` inputenc).

---

## 6 · How to reproduce (from a fresh clone, with raw data restored)

```bash
# 0. Set up Python environment
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt   # Windows
# .venv/bin/python  -m pip install -r requirements.txt        # Mac/Linux

# 1. Cleaning (notebooks) — only needed if data/clean/*.xlsx missing
#    Open Jupyter and execute the 8 notebooks in order (see §3).
#    Or restore data/clean/* from your local Dropbox copy.
jupyter notebook data/code_legacy/

# 2. Analysis (Python pipeline)
.venv/Scripts/python.exe scripts/python/run_all.py

# 3. Typeset
cd manuscript
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## 7 · Variables — quick reference

The full data dictionary lives in [`data/README.md`](data/README.md) (266 lines,
organised by purpose). Quick reference here for the variables that appear most
often in the manuscript and analysis scripts.

### Identifiers

| Variable | Type | Where | Description |
|---|---|---|---|
| `code` | str | both | oTree participant code (8-char). Joins to Prolific via `delegator_match*.xlsx` in raw/ |
| `session_code` | str | both | oTree session (one per recruitment batch) |
| `pilot` | int | both | 1 = pilot wave, 0 = main wave |
| `treat` | int | both | **0 = Punishment**, **1 = No-Punishment** |

### Player A — main outcome variables

| Variable | Type | Description |
|---|---|---|
| `delegation` | 0/1 | **Headline H1 outcome.** 1 = Player A delegated the 11th prediction to the algorithm |
| `overall_score` | int 0-10 | Sum of `success_r1..success_r10`; Player A's performance on the first 10 rounds |
| `success_last` | float | 1 if Player A's 11th prediction was within 10 lbs (NA if delegated) |
| `pass_att2` | 0/1 | Belief-screen attention-check pass. **Preregistered exclusion criterion for Player A.** 131/161 pass |

### Player A — beliefs about Player B's punishment (the strategy method)

| Variable | Description |
|---|---|
| `belief_del_good` / `belief_del_bad` | £ Player A expects Player B to deduct after delegated decision + good/bad outcome |
| `belief_nodel_good` / `belief_nodel_bad` | Same, after self decision |
| `nodel_del_good` / `nodel_del_bad` | Within-subject differences (no-del minus del). Used in Col (3) of Table 1 |

### Player A — beliefs about own performance / population

| Variable | Description |
|---|---|
| `confidence0`..`confidence10` | Probability mass (%) Player A places on each possible score 0..10 |
| `wa_confidence` | Weighted average confidence ($\sum_k k \cdot \text{confidence}_k / 100$) |
| `difficulty0`..`difficulty10` | Estimated population share (%) at each score |
| `error_confidence`, `error_difficulty` | **Failed-submission counters** (oTree rejected the form because percentages didn't sum to 100). UI / data-quality measures, not belief-accuracy measures. |

### Player B — main outcome variables

| Variable | Description |
|---|---|
| `punish_del_good` / `punish_del_bad` | £ Player B chose to deduct after delegated decision + good/bad outcome (range £0–£2 in £0.10 steps) |
| `punish_nodel_good` / `punish_nodel_bad` | Same, after self decision. **`nodel_del_bad` (within-subject difference) is the H2 test variable in the bad-outcome cell.** |
| `never_punish` | 1 if all four cells are zero (~42% of attention-pass Bs) |
| `pass_att2` | Punishment-screen attention check. **Preregistered exclusion for Player B.** 135/161 pass |

### Demographics & technology (used in balance + controls)

`age`, `female`, `socio_status` (1–10 self-reported), `went_to_uni`, `technology_score` (composite of programming / device usage / crypto / etc.), `leader` (1 if reports management/supervisory experience).

### Conventions

- Booleans stored as int 0/1 (sometimes float when NA present).
- Currency in £.
- Probabilities in `confidence_*` and `difficulty_*` are **percent** (0–100), not 0–1.
- Time in seconds.
- Missing values in `success_last` / `guess_last` / `confidence_last` indicate Player A delegated.

---

## 8 · Outputs produced

### Tables ([`tables/`](tables/))

| File | Inputs to manuscript |
|---|---|
| `balance_player_a.tex` | Appendix Table A1 |
| `balance_player_b.tex` | Appendix Table A1b |
| `reg_delegation.tex` | Body Table 1 |
| `reg_delegation_full.tex` | Appendix Table A2 |
| `reg_punishment.tex` | Appendix Table for Player B punishment regression |

### Figures ([`manuscript/figures/`](manuscript/figures/))

| File | Used in |
|---|---|
| `delegation_shares.png` | Body §4.2 (H1 result) |
| `performance.png` | Body §4.2 (calibration) |
| `performance_delegation_scatter.png` | Body §4.2 (heterogeneity) |
| `punishment.png` | Body §4.3 (H2 result, with Player A beliefs overlaid) |
| `punishment_shares.png` | Appendix (frequencies) |

### Numbers manifest

[`scripts/python/_outputs/numbers.json`](scripts/python/_outputs/numbers.json) records every numeric
claim the manuscript makes (delegation rates, p-values, regression coefficients, MDE,
sample sizes, etc.). This file is the contract between the analysis pipeline and
the manuscript prose, and the ground truth for `/audit-reproducibility`.

---

## 9 · What's still pending

| Item | Status | Action |
|---|---|---|
| Cleaning notebooks ported to Python scripts | not done | ~1 day port; preserves DataFrame-equivalent (not byte-identical due to `random.randint` in bonus cells + xlsx metadata) |
| One-command raw → PDF orchestrator | not done | trivial once cleaning is ported |
| PAP registry link + ID | placeholder in `appendix.tex` | only Felix can supply |
| CONSORT recruitment-funnel counts (invited / consented) | placeholder in `appendix.tex` | needs Prolific audit log |
| Random-seed discipline | not enforced | not currently load-bearing (no bootstraps); add when introducing TOST or randomization-inference |
| `/audit-reproducibility` wired into pre-commit / CI | not done | ~2 hours; catches manuscript ↔ data drift |

See [`scripts/python/README.md`](scripts/python/README.md) §"Cleaning pipeline (not yet ported)" and [`data/code_legacy/README.md`](data/code_legacy/README.md) §"Migration TODO" for porting notes.

---

## 10 · Cross-references

- [`scripts/python/README.md`](scripts/python/README.md) — analysis pipeline detail
- [`data/README.md`](data/README.md) — full variable dictionary (218 columns)
- [`data/code_legacy/README.md`](data/code_legacy/README.md) — cleaning notebook detail + pandas 3 caveat
- [`notebooks/exploration/README.md`](notebooks/exploration/README.md) — exploratory notebook inventory
- [`quality_reports/peer_review_algorithms_and_responsibility/`](quality_reports/peer_review_algorithms_and_responsibility/) — `/review-paper --peer AER` reports
