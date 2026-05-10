# Results Section — Working Canvas

> Crystallisation workspace for re-doing the results section of *Algorithms and Responsibility*.
> Plan: [`quality_reports/plans/ok-we-need-to-crystalline-comet.md`](plans/ok-we-need-to-crystalline-comet.md)
>
> **How this works**: Felix pastes a chunk → Claude proposes a row diff (ID, tags, position, verbatim quote) → Felix accepts/edits/rejects → on accept, the row appears in the table below and a detail block is appended further down. Cells only tag and index; the full prose lives verbatim in the detail block. Nothing is paraphrased into a cell.

---

## Schema reference

**Row ID format**: `<Player>-<Kind><n>` — e.g. `A-R1`, `B-M2`. IDs are stable and append-only; table order is independent of ID order.

**Type colour tags**:

- 🟦 **argument** — a claim being made
- 🟨 **analysis** — an empirical operation (regression, test, plot)
- 🟩 **interpretation** — what the analysis means / how it should be read
- 🟥 **open question** — unresolved, needs decision
- 🟪 **supporting evidence** — auxiliary check, robustness, descriptive

**Players**: `A` | `B` | `—` (use `—` for design-level / sample-level material that isn't player-specific).

**Kind**: `Result` | `Mechanism` | `Preamble` (intro, manipulation checks, balance, attrition, sample descriptives).

**Analysis**: short label for the empirical operation (e.g. "main reg on confidence", "het by trust", "robustness: drop top decile"). Leave **empty** for any row that isn't itself an analysis (🟦 argument, 🟩 interpretation, 🟥 question, 🟪 supporting evidence, descriptive/preamble rows). Use it for 🟨 analysis rows, and optionally as a *grouping* tag — multiple rows can share the same Analysis label to cluster all rows tied to the same operation (the analysis itself, its interpretation, its robustness check).

**Source** (presence indicator, one slot per known draft layer): `N` = notes filled · `O` = old draft filled · `C` = current draft filled · `_` = empty. Format: `N · O · C` (e.g. `N · _ · _` = only notes so far; `N · O · C` = all three).

**Status**: `draft` | `confirmed` | `parking` | `cut` — applies to the topic, not to any individual draft version.

**Parent** (table column): row ID this row attaches to as its primary structural parent. Empty for headline rows. Mechanisms exploring a result point to that result's row; analyses supporting a mechanism point to that mechanism's row. Captures the *primary* structural attachment only — richer relations (tension with, supersedes, depends on multiple) live in the detail-block Cross-refs.

**Detail-block convention**: when a row has prose from multiple sources (notes, old draft, current draft), each source goes under its own labelled subheading inside the detail block, verbatim. The row stays single; the dossier stacks. Split into separate rows only if the old vs. new prose argue *different things* (not just rephrasing) — link with a `supersedes` or `tension with` cross-ref.

---

## Overview table

| ID | Player | Kind | Analysis | Type | Handle | Source | Parent | Status |
|----|--------|------|------|------|------|------|------|------|
| P1 | — | Preamble | | | Results intro: sample, time spent, earnings | N · O · C | | draft |
| P2 | — | Preamble | | | Power analysis (ex-post, à la Feier et al.) | _ · O · _ | | parking |
| A-R1 | A | Result | | 🟦 argument | Punishment possibility reduces likelihood to delegate | N · _ · _ | | draft |
| A-R2 | A | Result | delegation share by condition | 🟨 analysis | Delegation rates: 42.5% Baseline vs 59.3% Treatment | N · _ · _ | A-R1 | draft |
| A-M1 | A | Mechanism | | 🟦 argument | Lit task differs: aligned incentives + certainty weaken the punishment-avoidance motive | N · _ · _ | A-R1 | draft |
| A-M2 | A | Mechanism | | 🟦 argument | Implication: weaker punishment motive should show in punishment beliefs | N · _ · _ | A-M1 | draft |
| A-M3 | A | Mechanism | | 🟦 argument | A-M1 explains null result, not reversal | N · _ · _ | A-M1 | draft |
| A-M4 | A | Mechanism | | 🟦 argument | Player A may expect higher punishment when delegating | N · _ · _ | A-R1 | draft |
| A-M5 | A | Mechanism | | 🟦 argument | Lit consistency: moral decisions viewed critically | N · _ · _ | A-M4 | draft |
| A-M6 | A | Mechanism | | 🟦 argument | Shirking motive is punished | N · _ · _ | A-M4 | draft |
| A-M7 | A | Mechanism | | 🟦 argument | Player A exerts more effort under punishment to outperform algorithm; not delegating becomes optimal | N · _ · _ | A-R1 | draft |
| A-R3 | A | Result | performance: delegators by condition | 🟨 analysis | Performance of delegators: Treatment > Baseline (later rounds), equal in first 10 | N · _ · _ | A-M7 | draft |
| A-R4 | A | Result | performance: non-delegators by condition | 🟨 analysis | Performance of non-delegators improved in Treatment, not in Baseline | N · _ · _ | A-M7 | draft |
| A-M8 | A | Mechanism | | 🟦 argument | Performance differences not driven by task difference (task was same) | N · _ · _ | A-M7 | draft |
| A-R6 | A | Result | main delegation regression | 🟨 analysis | Regression confirms A-R1 | N · _ · _ | A-R1 | draft |
| A-R7 | A | Result | main delegation regression | 🟨 analysis | Baseline only: delegation decreases with performance in first 10 rounds | N · _ · _ | A-R1 | draft |
| A-M9 | A | Mechanism | | 🟩 interpretation | Interp I: causal-attribution preference — only emerges under punishment motive | N · _ · _ | A-R7 | draft |
| A-M10 | A | Mechanism | | 🟩 interpretation | Interp II umbrella: Beliefs | N · _ · _ | A-R7 | draft |
| A-M13 | A | Mechanism | | 🟩 interpretation | Belief sub-claim 1: A expects higher punishment for delegated decisions the worse the outcome | N · _ · _ | A-M10 | draft |
| A-M14 | A | Mechanism | | 🟩 interpretation | Belief sub-claim 2 (alternative): better-performing Player As just hold different beliefs (null in data) | N · _ · _ | A-M10 | draft |
| A-M11 | A | Mechanism | | 🟩 interpretation | Interp III: lit says more uncertainty → less delegation; alignment depends on perf↔uncertainty direction | N · _ · _ | A-R7 | draft |
| A-M12 | A | Mechanism | | 🟦 argument | Uncertainty interpretation can't explain treatment differences (would hold equally in both conditions) | N · _ · _ | A-M11 | draft |
| A-M15 | A | Mechanism | | 🟩 interpretation | Delegation shares around 50% indicate subjects perceive equal performance credibly | N · _ · _ | A-R2 | draft |
| A-R8 | A | Result | | 🟨 analysis | Performance is equal between treatments | N · _ · _ | A-M7 | draft |
| A-M16 | A | Mechanism | | 🟦 argument | Equal performance rules out ex-ante differences and effort-for-B as drivers of treatment differences | N · _ · _ | A-R8 | draft |
| A-R9 | A | Result | | 🟨 analysis | Significant overconfidence, equal across treatments | N · _ · _ | A-M7 | draft |
| A-M17 | A | Mechanism | | 🟩 interpretation | Overconfidence could stem from the info that algorithm performs equally well | N · _ · _ | A-R9 | draft |
| A-M18 | A | Mechanism | | 🟦 argument | Methodological restriction: analyze punishment beliefs only in Baseline (Treatment beliefs are hypothetical) | N · _ · _ | A-M10 | draft |
| A-R10 | A | Result | punishment beliefs across scenarios | 🟨 analysis | Punishment beliefs positive in all 4 scenarios (surprisingly for good outcomes) | N · _ · _ | A-M10 | draft |
| A-R11 | A | Result | punishment beliefs by delegation × outcome | 🟨 analysis | No difference in punishment beliefs between delegated and non-delegated decisions for either outcome | N · _ · _ | A-M13 | draft |

---

## Detail blocks

<!-- One block per row, in ID order. Each block holds the verbatim prose from Felix and any commentary or cross-refs. -->

### P1 — Results intro: sample, time spent, earnings
**Tags**: Player — · Preamble · status: draft

**Notes** (Felix):
> Results introduction paragraph (details on sample, time spent, earnings, etc.)

**Old draft**:
> Data collection took place between February and June 2023 through the British online platform Prolific, with all participants recruited from the United Kingdom.\footnote{EXCLUSION CRITERIA} The experiment was programmed in oTree [reference]. A total of 322 subjects were recruited (161 assigned to Player A, 161 to Player B). \footnote{We preregistered the collection of data from 320 participants (80 subjects per role per treatment). Due to attrition and subsequent re-matching we recruited an extra pair in the treatment condition.} On average, Player A spent 12 minutes completing the experiment and earned YZ, while Player B spent approximately 8 minutes and earned YZ. Treatment randomization was effective, as demonstrated by the balance across observable characteristics (Appendix \ref{appendix:sum_stats}, Table \ref{tab:treatment_balance}). [Balance is only important for Player A, because there we do comparisons across treatments, for Player B it is about a within-subject decision. Balance across observables is only given for Player A.]
>
> [for external validity concerns: only people at pc, no phone or tablet]

**Current draft**:
> Data collection took place between February and June 2023 through the British online platform Prolific, with all participants recruited from the United Kingdom.\footnote{EXCLUSION CRITERIA: leave a comment for Felix to insert later} A total of $322$ subjects were recruited ($161$ assigned to Player~A, $161$ to Player~B).\footnote{We preregistered the collection of data from $320$ participants ($80$ subjects per role per treatment). Due to attrition and subsequent re-matching we recruited an extra pair in the \textit{Punishment} condition.} On average, Player~A spent $12$ minutes completing the experiment and earned an average bonus of $\pounds 2.49$ on top of the Prolific show-up fee, while Player~B spent approximately $8$ minutes and earned an average bonus of $\pounds 2.30$. Treatment randomization was effective, as demonstrated by the balance across observable characteristics (Appendix~\ref{appendix:sum_stats}, Table~\ref{tab:treatment_balance}). A flow diagram showing recruitment, attrition, attention-check exclusion, and the analysis sample, broken down by condition and role, appears in Appendix~\ref{appendix:attrition}; in particular, attrition rates do not differ meaningfully across the \textit{Punishment} and \textit{No-Punishment} conditions.

**Felix's commentary**: —

**Cross-refs**: —

### P2 — Power analysis (ex-post, à la Feier et al.)
**Tags**: Player — · Preamble · status: parking

**Notes**: _(awaiting paste)_

**Old draft**:
> [Do ex-post power analysis and describe as in Feier et al.: "The key dependent variable in our study is the relative reward (or punishment) for delegating the task versus using one's own work in case of success and in case of failure. Because we elicit these relative rewards via the strategy method, we compare paired differences. After running a pilot, we performed an ad-hoc power analysis to determine the appropriate sample size per treatment. We calculated with an expected mean of the paired differences of 5.00 ECU, an expected standard deviation of the paired differences of 15.00, an error probability of α = 0.05 and a power of 1 − β = 0.8. These parameters determined a required sample size of 73 subjects for each of the two treatments."]

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: —

### A-R1 — Punishment possibility reduces likelihood to delegate
**Tags**: Player A · Result · 🟦 argument · status: draft

**Notes** (Felix):
> Player A - Main result: punishment possibility reduces likelihood to delegate

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: —

### A-R2 — Delegation rates: 42.5% Baseline vs 59.3% Treatment
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> 42.5% of decisions delegated in Baseline condition (punishment possible), 59.3% of decisions delegated in Treatment condition (punishment not possible)

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: supports A-R1

### A-M1 — Lit task differs: aligned incentives + certainty weaken the punishment-avoidance motive
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Task different in literature: decision intent not obvious, because  (i) incentives aligned, and (ii) implemented with certainty → punishment motive not no strong (no intention/selfishness) → delegation motive to avoid punishment not so strong

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: explains divergence of A-R1 from literature

### A-M2 — Implication: weaker punishment motive should show in punishment beliefs
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Weaker punishment motive would be reflected in punishment beliefs

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: testable implication of A-M1 — points to a punishment-beliefs analysis

### A-M3 — A-M1 explains null result, not reversal
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Weaker punishment motive would not explain reversal, just lack of treatment difference

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: limitation of A-M1 — A-M1 alone cannot account for the direction of A-R2

### A-M4 — Player A may expect higher punishment when delegating
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Mechanism for A-R1: Player A may expect higher punishment when delegating

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: alternative mechanism for A-R1 (parallel to A-M1)

### A-M5 — Lit consistency: moral decisions viewed critically
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Would be consistent with parts of prior work: moral decisions viewed critically

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: literature support for A-M4

### A-M6 — Shirking motive is punished
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Shirking motive is punished

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: supporting consideration for A-M4

### A-M7 — Player A exerts more effort under punishment to outperform algorithm; not delegating becomes optimal
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Mechanism relating to A-R1:
> Player A can exert more effort when punishment is possible to outperform algorithm, so that not delegating is actually optimal

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: alternative mechanism for A-R1 (parallel to A-M1, A-M4)

### A-R3 — Performance of delegators: Treatment > Baseline (later rounds), equal in first 10
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> Among Player As that delegated, those in the Treatment condition (punishment not possible and delegation share higher) outperformed those in the Baseline condition (punishment possible and delegation share low), whereas performance in first 10 rounds is equal between both.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: relates to A-M7

### A-R4 — Performance of non-delegators improved in Treatment, not in Baseline
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> Performance among players that did not delegate improved in Treatment condition, and not in Baseline condition.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: relates to A-M7

### A-M8 — Performance differences not driven by task difference (task was same)
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Can't be due to differences in task, because task was the same.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: rules out task-difference confound for A-R3 and A-R4

### A-R6 — Regression confirms A-R1
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> Result that extends the simple comparison of A-R1: Regression confirms finding.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: confirms A-R1 via regression; same regression as A-R7

### A-R7 — Baseline only: delegation decreases with performance in first 10 rounds
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> Result stemming from the same regression: In Baseline condition, likelihood to delegate decreases with performance in first 10 rounds.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: same regression as A-R6

### A-M9 — Interp I: causal-attribution preference — only emerges under punishment motive
**Tags**: Player A · Mechanism · 🟩 interpretation · status: draft

**Notes** (Felix):
> Potential Interpretation I: The higher the likelihood of securing a high payoff for Player B, the more inclined Player A is to have directly brought about the outcome. Because we do only observe this relationship in the Baseline condition, this can't be inherent, but could instead be motivated by the punishment motive.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: interprets A-R7

### A-M10 — Interp II umbrella: Beliefs
**Tags**: Player A · Mechanism · 🟩 interpretation · status: draft

**Notes** (Felix):
> Potential interpretation II: Beliefs

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: alternative interpretation of A-R7; refines into sub-claims A-M13 and A-M14

### A-M13 — Belief sub-claim 1: A expects higher punishment for delegated decisions the worse the outcome
**Tags**: Player A · Mechanism · 🟩 interpretation · status: draft

**Notes** (Felix):
> Punishment motive - Player A must expect higher punishment for delegated decisions the worse the outcome.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: sub-claim under A-M10; alternative reading: A-M14

### A-M14 — Belief sub-claim 2 (alternative): better-performing Player As just hold different beliefs (null in data)
**Tags**: Player A · Mechanism · 🟩 interpretation · status: draft

**Notes** (Felix):
> Better-performing Player As could hold systematically different punishment beliefs than worse-performing Player As - We do not see this in the data

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: sub-claim under A-M10 (alternative reading to A-M13); empirical null embedded

### A-M11 — Interp III: lit says more uncertainty → less delegation; alignment depends on perf↔uncertainty direction
**Tags**: Player A · Mechanism · 🟩 interpretation · status: draft

**Notes** (Felix):
> Potential interpretation III: Literature shows that with more inherent uncertainty in a decision, delegation declines. Question to answer: Does uncertainty increase or decrease with performance? Depending on answer, our finding is in line with literature or not.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: alternative interpretation of A-R7; limited by A-M12

### A-M12 — Uncertainty interpretation can't explain treatment differences (would hold equally in both conditions)
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Anyways, this should hold equally in both conditions and cannot explain the treatment differences.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: limitation of A-M11

### A-M15 — Delegation shares around 50% indicate subjects perceive equal performance credibly
**Tags**: Player A · Mechanism · 🟩 interpretation · status: draft

**Notes** (Felix):
> Related to A-R1: Delegation shares around 50% -> Subjects perceive equal performance credibly.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: interprets A-R2 (the underlying delegation rates)

### A-R8 — Performance is equal between treatments
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> Result: Performance is equal between treatments

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: in A-M7 cluster; basis for A-M16

### A-M16 — Equal performance rules out ex-ante differences and effort-for-B as drivers of treatment differences
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Treatment differences do not stem from ex-ante performance differences, nor (as seen before) from increase effort for the decision of Player B.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: implication of A-R8; references earlier finding on effort-for-B (A-R3 / A-R4 in the A-M7 cluster)

### A-R9 — Significant overconfidence, equal across treatments
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> Subjects exhibit significant overconfidence (could stem from the info that algorithm performs equally well), which does also not differ between treatments.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: in A-M7 cluster (per Felix: "yet another flavor of performance"); interpreted by A-M17

### A-M17 — Overconfidence could stem from the info that algorithm performs equally well
**Tags**: Player A · Mechanism · 🟩 interpretation · status: draft

**Notes** (Felix):
> (could stem from the info that algorithm performs equally well)

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: interpretation of A-R9 (parenthetical extracted from A-R9's verbatim)

### A-M18 — Methodological restriction: analyze punishment beliefs only in Baseline (Treatment beliefs are hypothetical)
**Tags**: Player A · Mechanism · 🟦 argument · status: draft

**Notes** (Felix):
> Player A - Beliefs - Result: Only look at punishment beliefs of people in Baseline condition, because beliefs in treatment condition are purely hypothetical.

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: scope condition for A-R10 and A-R11

### A-R10 — Punishment beliefs positive in all 4 scenarios (surprisingly for good outcomes)
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> Punishment positive in all 4 scenarios (surprisingly for good outcomes)

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: scope: Baseline only (per A-M18); in A-M10 belief cluster

### A-R11 — No difference in punishment beliefs between delegated and non-delegated decisions for either outcome
**Tags**: Player A · Result · 🟨 analysis · status: draft

**Notes** (Felix):
> no difference between delegated and non delegated decisions for neither outcome

**Old draft**: _(awaiting paste)_

**Current draft**: _(awaiting paste)_

**Felix's commentary**: —

**Cross-refs**: scope: Baseline only (per A-M18); tests A-M13 (no delegation-vs-non-delegation difference cuts against A-M13)

---

## Phase 2 placeholder: DAG view

<!-- Once the table feels saturated, a Mermaid graph rendering cross-refs as edges goes here. Not built upfront. -->
