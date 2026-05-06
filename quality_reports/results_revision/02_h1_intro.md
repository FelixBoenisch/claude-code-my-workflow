# P02 — H1 introduction (Headline paragraph)

**Source:** `manuscript/results.tex` line 7 (the `\paragraph{Headline.}` block).
**Status:** Plan, awaiting feedback. *Replaces an earlier draft of this file written against a prior version of results.tex.*
**Last updated:** 2026-05-06.

---

## 1. What's actually on line 7 (current state)

The Headline paragraph now carries three embedded comments:

- (a) Inside the within-subject footnote: *"Absolute numbers of 5 and 12 do not mean much if we do not know how many subjects initially delegated/did not delegate. What are the percentages?"*
- (b) Inline: *"[Comment: Check p-values.]"*
- (c) Inline (a long bracket-comment at end): one- vs two-sided debate, design-section consistency, prereg framing, "best practice to make hypothesis rejectable", and *"STATA gives other p-values"*.

Two structural notes:

- The prereg-direction footnote that previously sat in this paragraph is gone. The equivalent language now lives only in the figure caption (line 22): *"The preregistration does not specify a test direction; the realized effect reverses the sign anticipated by the responsibility-avoidance literature on which the hypothesis was grounded."*
- Below this paragraph the document still has a **red `\textcolor` duplicate** of the Result 1 statement on line 9, with the clean version on lines 11–12. The red duplicate should be deleted.

---

## 2. Resolving the comments and questions

### 2.1 Comment (b): "Check p-values"

`scripts/python/_outputs/numbers.json`:

| Key | Value |
|---|---|
| `h1_p_chi2_two_sided` | `0.0334` → reported as **0.033** ✓ |
| `h1_p_fisher_two_sided` | `0.0407` → reported as **0.041** ✓ |
| `delegation_rate_punishment_pct` | **42.5** ✓ |
| `delegation_rate_no_punishment_pct` | **59.3** ✓ |
| `h1_n_punishment` | 80 |
| `h1_n_no_punishment` | 81 |

The numbers in the paragraph match the production script exactly. **No change needed.** Comment can be deleted.

### 2.2 Comment (a) in the McNemar footnote: percentages for 12 / 5

`scripts/python/_outputs/numbers.json` (from `11_hypo_delegation.py`):

| Key | Value |
|---|---|
| `hypo_n_pairs_within` | **81** (No-Punishment respondents) |
| `hypo_within_n_dropped` | **12** (delegate → would-not under hypothetical punishment) |
| `hypo_within_n_added` | **5** (not-delegate → would under hypothetical punishment) |
| `hypo_within_n_changed` | 17 |
| `hypo_nopun_actual_rate_pct` | 59.3 → 48 actual delegators, 33 non-delegators |
| `hypo_nopun_hypo_rate_pct` | 50.6 |
| `hypo_within_actual_minus_hypo_pp` | **8.6 pp** (drop in delegation rate under hypothetical punishment) |
| `hypo_within_mcnemar_p` | 0.0896 → **0.090** ✓ |

**Two natural ways to express percentages:**

- **As a share of each base** (more informative about asymmetric switching):
  - $12/48 = 25.0\%$ of actual delegators would have stopped delegating under hypothetical punishment.
  - $5/33 = 15.2\%$ of actual non-delegators would have started delegating under hypothetical punishment.
- **As a share of all No-Punishment respondents** (cleaner for a one-line footnote):
  - $12/81 = 14.8\%$ would switch from delegate to no-delegate.
  - $5/81 = 6.2\%$ would switch the other way.
  - Net change: $-8.6$ pp (matches the manifest).

Both are correct. I'd suggest the per-base form because it directly answers the "what fraction of each starting group switches?" question the comment asks.

### 2.3 Comment (c): one- vs two-sided, design vs prereg, "rejectable"

This is the substantive part. Three pieces.

#### (c-i) Is the hypothesis one-sided or two-sided?

| Source | Direction |
|---|---|
| `design.tex` L69 — H1 statement | **Directional**: "The introduction of potential punishment *increases* the likelihood that Player A delegates" |
| Preregistration (per `appendix.tex` L62) | **Non-directional**: "Direction not specified in the registry" |
| `results.tex` body (current) | Two-sided p-values reported |
| Figure caption (L22) | Notes: "preregistration does not specify a test direction" |

So three things are simultaneously true: (1) the *substantive prediction* in the design section is directional (literature-grounded), (2) the *registered hypothesis* is non-directional, (3) we test two-sided. There is no contradiction — but the relationship between the three needs to be visible in the body for a reader who doesn't read the appendix.

**Three ways to handle it. Recommendation revised to (C).**

- **Option A — work around it in results.tex.** Add one sentence to the Headline paragraph reconciling the directional H1 in design with the non-directional prereg and two-sided test. Pre-empts the referee question, but leaves the underlying inconsistency in place: design.tex still says H1 is directional even though the registry was not.
- **Option B — rely on the figure caption + appendix.** Keep the body terse. Same drawback as A.
- **Option C — fix it at the source: make H1 non-directional in design.tex.** *(Recommended.)*

  The prereg is the binding constraint. Aligning design.tex to the prereg (rather than building reconciling text in results.tex) is the cleaner solution: it removes the apparent inconsistency entirely instead of explaining it. The literature-grounded *expectation* of an increase is preserved as **prose around H1**, not as the formal hypothesis statement.

### What Option C looks like in design.tex

Two edits are needed; both are small.

**Edit 1 — `design.tex` L69.** Change H1 from directional to non-directional.

  Current:
  > H1 (Delegation): The introduction of potential punishment **increases** the likelihood that Player~A delegates the decision to the algorithm.

  Proposed:
  > H1 (Delegation): The introduction of potential punishment **affects** the likelihood that Player~A delegates the decision to the algorithm.

  (Or, for a cleaner null-form: *"Player~A's likelihood of delegating to the algorithm differs between the Punishment and No-Punishment conditions."* I'd use the first — preserves the punishment-introduction-causes-X framing readers expect.)

**Edit 2 — `design.tex` L72, opening clause.** Re-anchor the literature-grounded *direction* in surrounding prose so the substantive prediction is not lost.

  Current opening:
  > H1 is grounded in empirical evidence that responsibility avoidance shapes delegation decisions involving human intermediaries.

  Proposed opening:
  > The responsibility-avoidance literature predicts that the introduction of punishment will *increase* delegation: subjects in modified dictator games are more willing to delegate morally consequential choices to an intermediary when the option to do so is available, even when the intermediary is a randomization device~\citep{bartling_shifting_2012}.

  The rest of the paragraph (Feier et al., the algorithmic-delegate question) carries on unchanged.

This way: H1 is stated non-directionally (matching the registry); the directional intuition lives in the paragraph that motivates the test; and the "realized effect is opposite the prediction" framing in results / mechanism sections still works because the *prediction* is now an explicit literature claim rather than the formal hypothesis.

### Parallel question: H2

`design.tex` L77 also states H2 directionally ("punished **less**"). The prereg powering calculation in `appendix.tex` L37 used two-sided MDE for H2 as well, and the deviations table treats H2 as non-directional. So the same logic applies. **Suggest applying the parallel edit** — H2 as "Player A's punishment differs by delegation choice, conditional on outcome" — but since you asked specifically about H1, flagging here for your call rather than baking into the recommendation.

### What Option C does to results.tex L7

If H1 is non-directional in design.tex, the body text simplifies. The reconciling sentence I drafted under Option A is no longer needed. The Headline paragraph becomes just:

> "We reject the null of equal delegation rates across conditions at the $5\%$ level (Pearson Chi-squared, $p=0.033$; Fisher's exact, $p=0.041$); the realized effect points in the direction *opposite* to that anticipated by the responsibility-avoidance literature."

No extra design-vs-prereg footnote needed. The "opposite to expectation" framing is now a comparison to the literature (still accurate after the H1 rewrite), not a comparison to the formal hypothesis.

### What Option C does to appendix.tex

Minor cleanup, optional. The current deviations row reads:
> "H1: ... Direction not specified in the registry. ... The realized direction is opposite to that anticipated by the responsibility-avoidance literature on which we drew."

Once H1 is non-directional in design.tex, the "Direction not specified" half is the only direction claim made anywhere — so it can stay verbatim, or be slightly reworded to "Hypothesis stated and registered as non-directional." Either is fine.

#### (c-ii) "Should we instead have equal delegation as the hypothesis and reject that?"

The chi-squared and Fisher tests *already do exactly this*. H₀ for both is "rates are equal across conditions"; the two-sided alternative is "rates differ." The current p-values reject H₀ at 5%. So this isn't a different test — it's a different way to *describe* the test. The cleanest one-sentence framing:

> "We reject the null of equal delegation rates across conditions at the $5\%$ level (Pearson Chi-squared, $p=0.033$; Fisher's exact, $p=0.041$); the realized effect points in the direction *opposite* to the literature-grounded substantive prediction in Section~\ref{sec:design}."

This is what Option A above does. **No analytic change.**

#### (c-iii) "Best practice — make the hypothesis rejectable, or state it as the substantive prediction?"

Both serve different purposes; the convention in experimental econ is to keep them separate:

- **Substantive prediction (directional H1):** the conjecture grounded in theory or prior evidence — what you *believe* will happen. Stated in the design / theory section.
- **Statistical null (H₀):** what you *test against*. Standard form is the no-effect null (equal rates). Tested two-sided unless preregistered as one-sided.

Conflating the two ("our hypothesis is that punishment increases delegation, and we test that") forces awkward wording when the realized direction reverses, exactly as you're now experiencing. Keeping them separate ("substantive prediction: increases. Null: equal. We reject the null in the direction opposite to the prediction") is cleaner and is also the form recommended by the AEA RCT registry style. The wording in Option A above implements this separation.

#### (c-iv) "STATA gives other p-values"

Resolved in the prior P02 draft and unchanged: the production script uses `scipy.stats.chi2_contingency(table, correction=False)`, which matches STATA's `tabulate, chi2` default. The `0.049` in older versions of this paragraph came from a scipy run with `correction=True` (Yates), which STATA does not apply by default. Test:

```stata
tabulate treat delegation, chi2 exact
```

should print `Pr = 0.033` and `Fisher's exact = 0.041`. If it does, the puzzle is fully closed and the inline comment can be deleted. (One quick run, no further analysis needed.)

---

## 3. The Result 1 box duplication (lines 9 vs 11–12)

Line 9 is a `\textcolor{red}{\textbf{Result 1:} ...}\\` draft block; lines 11–12 are the clean `\textbf{Result~1.}` boxed version. The red one is superseded.

**Action:** delete line 9. Keep lines 11–12.

This will close one of the four `Paragraph ended before \@textcolor was complete` errors that are currently corrupting `main.aux`.

---

## 4. Concrete plan for results.tex around line 7

In order:

### Step A — STATA confirmation (skippable, ~30s)

Run `tabulate treat delegation, chi2 exact` in STATA on the cleaned data. Expect 0.033 / 0.041. If it prints anything else, paste the output into this file and I'll diagnose.

### Step B — Edit the Headline paragraph (line 7)

1. Add the McNemar percentages inside the within-subject footnote (replace the comment):
   *"…among the $81$ respondents, $12$ ($25\%$ of actual delegators) would have stopped delegating under hypothetical punishment while only $5$ ($15\%$ of actual non-delegators) would have started…"*
   (Or the all-respondents form; your call.)
2. Delete the *"[Comment: Check p-values.]"* marker (numbers verified).
3. Replace the long inline bracket-comment with one sentence and a footnote:

   > **One sentence in body:** "We reject the null of equal delegation rates across conditions at the $5\%$ level (Pearson Chi-squared, $p=0.033$; Fisher's exact, $p=0.041$); the realized effect points in the direction *opposite* to the literature-grounded substantive prediction in Section~\ref{sec:design}."
   >
   > **Footnote:** "The preregistration is non-directional on H1; we report two-sided tests throughout. The deviations from each preregistered test, and the rationale, appear in Appendix~\ref{appendix:preregistration}."

### Step C — Delete the duplicate Result 1 box

Remove line 9 (`\textcolor{red}{...}\\`); keep the clean version on lines 11–12.

### Step D — Recompile

Three-pass + bibtex. Expect one of the four `\textcolor` errors to disappear; references will continue to fail to resolve until we close the remaining textcolor blocks downstream.

---

## 5. Suggested revised paragraph (track-changes view)

Strawman implementing all of the above. Italicised additions; `[deleted]` markers for removals.

> \paragraph{Headline.} We begin by examining the delegation behavior of Player~A. In the *Punishment* condition, where Player~B can punish, $42.5\%$ of Player~As delegated the decision to the algorithm. In the *No-Punishment* condition, where punishment is impossible, $59.3\%$ delegated. Figure~\ref{fig:delegation_shares} illustrates the difference. *We reject the null of equal delegation rates across conditions at the $5\%$ level (Pearson Chi-squared, $p=0.033$; Fisher's exact, $p=0.041$); the realized effect points in the direction opposite to the literature-grounded substantive prediction in Section~\ref{sec:design}.*\footnote{*The preregistration is non-directional on H1; we report two-sided tests throughout. The deviations from each preregistered test and the rationale appear in Appendix~\ref{appendix:preregistration}.*}\footnote{A within-subject corroborator points the same direction. Player~As in the *No-Punishment* condition were asked, after their actual delegation decision, the hypothetical question of whether they would have delegated had punishment been possible. Among the $81$ respondents, *$12$ ($25\%$ of actual delegators)* would have stopped delegating under hypothetical punishment while only *$5$ ($15\%$ of actual non-delegators)* would have started, yielding a hypothetical delegation rate of $50.6\%$ (within-subject McNemar's test $p=0.090$). Hypothetical responses elicited after the actual decision are subject to motivated reasoning; the within-subject pattern complements rather than substitutes for the between-subject test. *[deleted: percentages comment.]*}*[deleted: "[Comment: Check p-values.]" and the long inline bracket-comment.]*

Net effect on prose:
- One new sentence in body (the H₀-rejection sentence).
- One new footnote (prereg + two-sided + appendix pointer).
- Two parenthetical percentages added in the McNemar footnote.
- Three comment markers and one inline bracket-comment removed.
- Original "The introduction of potential punishment thus significantly *reduces*…" sentence is *replaced* by the H₀-rejection sentence; if you'd rather keep the original wording too, we can use both.

---

## 6. Open questions for you

1. **Direction handling**: Option **C** (edit design.tex H1 to non-directional + minor results.tex tweak) is now the recommended approach. Confirm? — and apply the parallel edit to H2, or leave H2 as-is?
2. McNemar percentages — per-base form (25% of delegators / 15% of non-delegators) or share-of-all-respondents form (15% / 6%)?
3. Want to keep "The introduction of potential punishment thus significantly *reduces*…" alongside the new H₀-rejection sentence (somewhat redundant), or replace it (cleaner)?
4. STATA confirmation — run it, or accept §2.3 (c-iv) and move on?
