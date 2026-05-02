# Data layout & dictionary

This directory holds the experiment's raw, intermediate, and analysis-ready
files. **All `*.xlsx`, `*.csv`, and `*.parquet` content is gitignored** because
the raw exports include Prolific Participant IDs (PII). Code that operates on
the data is tracked.

## Layout

```
data/
├── raw/             # oTree session exports + Prolific exports (gitignored)
│   ├── pre_pilot/
│   ├── pilot/
│   ├── main/
│   │   ├── delegator/
│   │   ├── delegator_no_punish/
│   │   ├── delegator_no_punish_2/
│   │   ├── evaluator_1/ ... evaluator_4/
│   │   └── evaluator_no_punish_1/ ... evaluator_no_punish_5/
│   └── Test/        # pre-experiment dev artefacts
├── interim/         # pipeline intermediates (gitignored)
│   ├── 01_cleaned/  # per-wave cleaned + Prolific demographic merges
│   ├── 02_appended/ # waves concatenated
│   └── 03_pagetimes/# joined with page-timing data
├── clean/           # analysis-ready (gitignored)
│   ├── delegator_cleaned.xlsx   # 161 rows, 136 columns — Player A
│   └── evaluator_cleaned.xlsx   # 161 rows,  82 columns — Player B
└── code_legacy/     # canonical raw -> clean pipeline (Jupyter; not yet ported to Python)
```

The pipeline `raw/ -> interim/ -> clean/` is implemented by the notebooks in
[`code_legacy/`](code_legacy/). The pipeline from `clean/` to manuscript
artefacts is implemented in [`../scripts/python/`](../scripts/python/).

---

# Data dictionary

## `clean/delegator_cleaned.xlsx` — Player A (decision-maker), n = 161

### Identifiers

| Column | Type | Description |
|---|---|---|
| `code` | str | oTree participant code (8-char). Joins to Prolific export via `delegator_match*.xlsx` in `raw/`. |
| `session_code` | str | oTree session code (one per recruitment batch). |
| `pilot` | int | 1 if subject is from the pilot wave; 0 if main wave. |

### Treatment & design

| Column | Type | Description |
|---|---|---|
| `treat` | int | **0 = Punishment** condition (Player B can punish). **1 = No-Punishment** (no punishment possible). |
| `random_order_del` | int | 0/1: which delegation option appeared first on screen (randomised). |

### Prediction task — first 10 rounds (incentivised)

| Column | Type | Description |
|---|---|---|
| `guess_r1`..`guess_r10` | int | Player A's weight prediction in pounds for round 1..10. |
| `truth_r1`..`truth_r10` | int | True weight for round 1..10 (constant across subjects in a session). |
| `success_r1`..`success_r10` | 0/1 | 1 if `|guess − truth| ≤ 10` lbs. |
| `overall_score` | int | Sum of `success_r1..success_r10` (0–10). Used as Player A's "performance" measure throughout the paper. |
| `true_performance` | int | Continuous performance measure (sum of `|guess − truth|` errors, scaled). |
| `test_slider` | int | Calibration slider value collected before the task (familiarisation check). |

### 11th prediction (the payoff-relevant decision)

| Column | Type | Description |
|---|---|---|
| `delegation` | 0/1 | **1 if Player A delegated the 11th prediction to the algorithm.** Headline outcome of H1. |
| `guess_last` | float | Player A's 11th prediction (NA if delegated). |
| `truth_last` | float | True weight on the 11th prediction (constant across subjects). |
| `success_last` | float | 1 if `|guess_last − truth_last| ≤ 10` lbs (NA if delegated). |
| `confidence_last` | float | Player A's stated confidence in earning the high payoff for Player B (only if she predicted herself). |
| `delegation_hypo` | float | (No-Punishment only) hypothetical: would she have delegated if punishment were possible? |

### Beliefs about own performance (probability mass on each possible score)

| Column | Type | Description |
|---|---|---|
| `confidence0`..`confidence10` | int | Probability mass (in %) Player A placed on the corresponding score (0..10). Should sum to 100. |
| `wa_confidence` | float | Weighted-average confidence: $\sum_{k} k \cdot \text{confidence}_k / 100$. |
| `highest_confidence` | float | Mode score: the value of $k$ at which `confidence_k` is largest. |
| `error_confidence` | int | **Number of failed submission attempts** on the confidence-elicitation screen (the oTree form rejects the submission when the percentages over `confidence0..10` don't sum to 100). A UI / data-quality counter, not a belief-accuracy measure. |
| `overconfidence` | float | `wa_confidence − overall_score`. Positive = overconfident in own performance. |
| `overconfidence_to_others` | float | Subject's own predicted score minus the mean of her predicted distribution over others. |

### Beliefs about population distribution

| Column | Type | Description |
|---|---|---|
| `difficulty0`..`difficulty10` | int | Player A's estimate of the population share (in %) at each score. Should sum to ≈100. |
| `wa_difficulty` | float | Weighted-average estimate. |
| `error_difficulty` | int | **Number of failed submission attempts** on the population-distribution screen (oTree rejects when `difficulty0..10` don't sum to 100). A UI / data-quality counter, not a belief-accuracy measure. |

### Beliefs about Player B's punishment (the 4 strategy-method cells)

| Column | Type | Description |
|---|---|---|
| `belief_del_good` | float | £ Player A expects Player B to deduct after **delegated decision + good outcome**. Range £0–£2. |
| `belief_del_bad` | float | £ … after **delegated decision + bad outcome**. |
| `belief_nodel_good` | float | £ … after **self decision + good outcome**. |
| `belief_nodel_bad` | float | £ … after **self decision + bad outcome**. |
| `belief_*_binary` | int | 1 if the corresponding belief is strictly positive. |
| `bad_good_del` | float | `belief_del_bad − belief_del_good` (within-subject outcome effect under delegation). |
| `bad_good_nodel` | float | `belief_nodel_bad − belief_nodel_good` (under self decision). |
| `nodel_del_good` | float | `belief_nodel_good − belief_del_good` (within-subject delegation effect for good outcome). Used in Col (3) of Table 1. |
| `nodel_del_bad` | float | `belief_nodel_bad − belief_del_bad` (delegation effect for bad outcome). Used in Col (3). |
| `nodel_del_good_x_treat` | float | `nodel_del_good × treat` interaction. |
| `nodel_del_bad_x_treat` | float | `nodel_del_bad × treat` interaction. |

### Risk preferences

| Column | Type | Description |
|---|---|---|
| `switching_point` | int | Switching point in the Holt & Laury-style multiple price list (higher = more risk-averse). |

### Free-text responses

| Column | Type | Description |
|---|---|---|
| `del_reason` | str | Why Player A delegated / didn't (open-ended). |
| `research_about` | str | What Player A thinks the research is about. |
| `unclear` | str | Aspects of the experiment Player A found unclear. |
| `explain_punish_bad` | str | Player A's open-ended reasoning about expected punishment after a bad outcome. |
| `explain_punish_good` | str | Same, for a good outcome. |

### Attention checks & timing

| Column | Type | Description |
|---|---|---|
| `pass_att1` | 0/1 | 1 if subject passed the **first** attention check. |
| `pass_att2` | 0/1 | 1 if subject passed the **belief-elicitation** screen attention check. **This is the preregistered exclusion criterion for Player A.** |
| `attention` | float | Raw attention-check response. |
| `time_taken` | float | Total time on the experiment in seconds. Mean ≈ 746 s = 12.4 min. |
| `punish_bel_time` | int | Time on the punishment-belief screen in seconds. |
| `total_approvals` | float | Prolific approval rate of the subject (eligibility was ≥95%). |

### Demographics

| Column | Type | Description |
|---|---|---|
| `age` | float | Self-reported age in years. |
| `female` | float | 1 if `sex == "Female"`. |
| `sex`, `gender`, `ethnicity`, `ethnicity_simple`, `white` | str/int | Demographic identifiers. |
| `country_birth`, `nationality`, `language`, `languages`, `abroad` | str | Migration / language. |
| `education`, `went_to_uni`, `student_status` | str/int | Education. `went_to_uni` = 1 if has university degree. |
| `employ_status`, `employ_sector`, `leadership`, `management_exp`, `leader` | str/int | Employment. `leader` = 1 if reports management or supervisory experience. |
| `income`, `socio_status` | str/float | Income; `socio_status` is self-reported on a 1–10 scale. |
| `religion`, `religious` | str/int | Religion; `religious` = 1 if any religious affiliation. |
| `body_weight` | str | Self-reported body weight category (used for sensitivity analyses since the task involves weight). |
| `dating_apps`, `hobbies` | str | Lifestyle indicators. |

### Technology affinity (used in the `technology_score` composite)

| Column | Type | Description |
|---|---|---|
| `device_usage` | str | Weekly device usage. |
| `internet_products` | str | Use of internet products. |
| `programming` | str | Programming experience. |
| `tech_at_work` | str | Technology use at work. |
| `tech_use_at_work_often` | int | Binarisation of `tech_at_work` (≈daily). |
| `nft`, `crypto` | str | Familiarity with NFT / crypto. |
| `technology_score` | int | Composite (0–N). Used in the balance table and as a control. |

### Constructed regressors

| Column | Type | Description |
|---|---|---|
| `treat_x_overall_score` | int | `treat × overall_score` interaction. |
| `overall_score_x_treat` | int | Same (alias). |

---

## `clean/evaluator_cleaned.xlsx` — Player B (third party who can punish), n = 161

### Identifiers

Same as Player A: `code`, `session_code`, `pilot`.

### Treatment

| Column | Type | Description |
|---|---|---|
| `treat` | int | **0 = Punishment** condition (Player B's choices implemented). **1 = No-Punishment** (Player B's choices hypothetical). |

### Punishment decisions (the 4 strategy-method cells)

| Column | Type | Description |
|---|---|---|
| `punish_del_good` | float | £ Player B chose to deduct from Player A in **delegated + good outcome** scenario. Range £0–£2 in £0.10 increments. |
| `punish_del_bad` | float | £ … in **delegated + bad outcome**. |
| `punish_nodel_good` | float | £ … in **self decision + good outcome**. |
| `punish_nodel_bad` | float | £ … in **self decision + bad outcome**. |
| `punish_*_binary` | int | 1 if corresponding punishment is strictly positive. |
| `never_punish` | int | 1 if all four cells are zero. ($\sim 42\%$ of attention-check passers.) |
| `bad_good_del` | float | Within-subject `punish_del_bad − punish_del_good`. |
| `bad_good_nodel` | float | Within-subject `punish_nodel_bad − punish_nodel_good`. |
| `nodel_del_good` | float | `punish_nodel_good − punish_del_good`. |
| `nodel_del_bad` | float | `punish_nodel_bad − punish_del_bad`. The H2 test variable in the bad-outcome cell. |
| `punish_time` | int | Time on the punishment-elicitation screen in seconds. |

### Beliefs about population distribution

Same as Player A: `difficulty0..difficulty10`, `wa_difficulty`, `med_difficulty`, `error_difficulty` (failed-submission counter, see Player A note).

### Post-experiment Likert items (Player B only)

| Column | Type | Description |
|---|---|---|
| `perception` | float | Perception of task difficulty. |
| `responsibility` | float | Likert: how responsible should Player A feel? |
| `trust` | float | Likert: trust in the algorithm. |
| `accountability` | str | Free-text: who should be accountable for a bad outcome? |
| `why_punish` | str | Free-text: rationale for punishment. |
| `why_punish_del_less` | str | Free-text: why might one punish less under delegation? |
| `why_punish_bad`, `why_punish_good` | float/str | Specific scenario justifications. |

### Risk preferences

| Column | Type | Description |
|---|---|---|
| `switching_point` | int | Same MPL as Player A. |

### Attention checks & timing

| Column | Type | Description |
|---|---|---|
| `pass_att2` | 0/1 | Pass on the **punishment-elicitation screen** attention check. **Preregistered exclusion criterion for Player B.** 135/161 = 83.9% pass. |
| `attention` | float | Raw attention response. |
| `time_taken` | float | Total time on experiment in seconds. Mean ≈ 474 s = 7.9 min. |
| `total_approvals` | float | Prolific approval rate. |

### Free-text responses

| Column | Type | Description |
|---|---|---|
| `research_about` | str | Player B's guess at the research question. |
| `unclear` | str | What was unclear. |

### Demographics & technology affinity

Same set of columns as Player A (`age`, `female`, `sex`, `ethnicity`, `socio_status`, `went_to_uni`, `technology_score`, `leader`, …). All used in the balance check (Appendix Table A1b).

---

## Conventions across both files

- **Booleans are stored as int 0/1** (sometimes float when there's NA in the column), not Python booleans.
- **Currency values are in £.**
- **Probabilities/percentages in `confidence_*` and `difficulty_*` are in `%` (0–100), not 0–1.**
- **Time values in `*_time` and `time_taken` are in seconds.**
- **Missing values:** `success_last` / `guess_last` / `confidence_last` are NA when Player A delegated; `delegation_hypo` is NA outside the No-Punishment hypothetical question.

## Provenance

Both files are produced by [`data/code_legacy/04 delegator/00_delegator cleaning.ipynb`](code_legacy/04%20delegator/00_delegator%20cleaning.ipynb)
and [`data/code_legacy/05 evaluator/00_evaluator_cleaning.ipynb`](code_legacy/05%20evaluator/00_evaluator_cleaning.ipynb), which read from
`data/interim/03_pagetimes/*_full_merged.xlsx`. The earlier interim files are
themselves produced by [`data/code_legacy/01 raw data treatment/`](code_legacy/01%20raw%20data%20treatment/) and
[`data/code_legacy/02 merge pagetimes/`](code_legacy/02%20merge%20pagetimes/).

The full dependency graph (raw exports → cleaning → analysis → manuscript) is
in [`scripts/python/README.md`](../scripts/python/README.md).
