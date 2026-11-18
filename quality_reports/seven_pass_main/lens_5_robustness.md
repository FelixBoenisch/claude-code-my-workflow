# Lens 5 — Robustness, power, and analysis coverage

**Updated:** 2026-09-07. **Baseline:** review dated 2026-08-21. **Snapshot:** `d4f48b6` plus the current uncommitted manuscript edits. Paths below are relative to `paper/`; line references describe this snapshot.

**Verdict: REVISE-MAJOR. Score: 5/10. Active findings: 0 CRITICAL, 7 MAJOR, 3 MINOR.**

The delegation result survives the new exclusions and both Pearson and Fisher tests. The revised paper acknowledges the insignificant treatment-by-performance interaction, reports the punishment regression in both samples, and now supplies the absolute-error improvement statistics. Those are material improvements. The principal remaining weaknesses are the categorical punishment-null claim, unreported order sensitivity, incomplete uncertainty reporting, and mechanism statements that exceed evidence from selected samples. The previous report overstated several objections; those corrections are explicit below.

## Scope and verification

Reviewed the current source reached through `manuscript/main.tex:98–117`, its included tables, the analysis scripts and numerical manifest, and the exclusion exhibit package. Comments in the sources, old compilation stdout files, and standalone exhibits are not treated as active paper content. I did not rerun the pipeline or compile the manuscript. I independently recomputed the small checks tabulated below, read-only, from `data/clean/delegator_cleaned.xlsx` and `data/clean/evaluator_cleaned.xlsx` using pandas/SciPy, applying the two IDs in `scripts/python/lib/io.py:9`. These checks do not verify raw-data cleaning or the full regression pipeline.

The currently included robustness evidence needs to be distinguished from files merely present in the repository:

| Evidence | Current active status |
|---|---|
| Delegation controls and attention-passer specification | Included at `manuscript/results.tex:31`. |
| Full-sample and attention-passer punishment regressions, including Player B performance beliefs | Included at `manuscript/appendix.tex:19`; both samples and interaction p-values discussed at line 17. |
| Extensive-margin punishment regression | Included at `manuscript/appendix.tex:25`. |
| Player A balance and joint balance tests | Included/discussed at `manuscript/appendix.tex:9–11`. |
| Player B balance table | Still explicitly omitted at `manuscript/appendix.tex:13`. |
| Separate delegation/punishment robustness tables and `tables/power_mde.tex` | Exist but are not inputs in the current source. Older `pass4.stdout` records are not evidence of present inclusion. |
| TOST, order-effects paragraph, power paragraph | TOST exists in the scripts; no active manuscript report. Order/power text at `manuscript/results.tex:174–176` is commented out. |
| Treatment-by-performance interaction | Computed; the null finding is acknowledged in active prose at `manuscript/results.tex:109,132`. The exact p-values at line 109 are commented out. |

## Active findings

### L5-M7 — MAJOR: “No protection” still asserts more than the punishment estimates establish

Severity harmonized across lenses: this is a consequential interpretation error requiring revision, not evidence that the underlying estimates or H1 are invalid. The remaining active IDs are retained for traceability.

**Evidence:** `manuscript/abstract.tex:2`, `manuscript/introduction.tex:11`, `manuscript/results.tex:49,55`, `manuscript/appendix.tex:23`, and `manuscript/conclusion.tex:6,11`. The numbered Result at `manuscript/results.tex:52` appropriately says “does not punish … significantly less.” The surrounding prose instead says “no protection,” “no differently,” and “cannot shift blame.”

The primary comparison now uses the full Punishment sample, not the attention-passer sample emphasized by the old review. Read-only recomputation gives:

| Bad-outcome insulation: own minus delegated punishment | Full sample | Attention passers |
|---|---:|---:|
| Subjects | 80 | 67 |
| Mean | £0.0713 | £0.0769 |
| Paired-t 95% confidence interval | [−£0.0216, £0.1641] | [−£0.0292, £0.1829] |
| TOST, ±£0.10 | p=0.2698; no equivalence | p=0.3323; no equivalence |
| TOST, ±£0.20 | p=0.0036; equivalence | p=0.0118; equivalence |

The upper full-sample confidence limit is about 30% of mean own-decision punishment after a bad outcome (£0.5531). Thus modest insulation remains compatible with the data. The repository TOST in `scripts/python/16_power.py:67–83` uses passers; it must not be silently presented as a full-sample result. Manifest counterparts are at `scripts/python/_outputs/numbers.json:250–268,511–516`.

The regression interaction is now transparently reported for both samples at `manuscript/appendix.tex:17`; this resolves the old omission. However, the bad-outcome delegation contrast is the sum of the delegation main effect and its interaction: about £0.032−£0.103=−£0.071 in `tables/reg_punishment.tex:13–18`. The interaction alone is the change in that contrast across outcomes, not the entire bad-outcome insulation effect.

**Revision:** use the numbered Result's non-rejection wording consistently; add the estimated bad-outcome contrast and its CI. If making an equivalence claim, justify a practically meaningful bound independently of whether it passes, report both displayed bounds and samples, and describe its scope. A ±£0.20 result is a valid statistical equivalence result at that bound; the old report was wrong to call it “not an equivalence result” merely because the bound is broad.

### L5-M1 — MAJOR: Headline precision remains unavailable to readers, and the two power implementations disagree

**Evidence:** `manuscript/results.tex:9,23,28,155` reports an 18.3 pp reduction and calls it robust across specifications, but provides no CI for the treatment contrast. Figure whiskers are ±1 SE of separate group means (`results.tex:23`), which is different information. The power table is not currently included, and `results.tex:176` is only a commented to-do.

The current contrast is 48/79−34/80=18.259 pp. An approximate, unpooled Wald 95% CI is **[2.99, 33.53] pp**, recomputed for this review. This documents substantial imprecision while preserving evidence of a reduction. Fisher's exact p=0.0264 corroborates Pearson p=0.0212; the earlier request for an exact test as though none existed is withdrawn.

`tables/power_mde.tex:7,16` supplies a planning-style MDE of 21.5 pp under baseline 0.50, n=80 per cell, two-sided alpha=.05 and 80% power. Its existence does not establish that it justified recruitment before data collection. Furthermore, `scripts/python/16_power.py:28–33` back-transforms Cohen's h into a difference in proportions and then multiplies that difference by two. The manifest therefore says **42.9 pp** at `scripts/python/_outputs/numbers.json:245`, inconsistent with the separate table-generating implementation at `_outputs/power_calc.py:47–62`.

**Revision:** report the treatment CI and a clearly labeled sample-size/sensitivity calculation; reconcile the two implementations before using their outputs. Do not call a calculation an original ex-ante justification without contemporaneous evidence. An observed effect smaller than an 80%-power MDE is not itself a validity failure, and observed-effect post-hoc power adds no useful independent evidence. The old review's “coin-flip-powered” characterization and CRITICAL rating are withdrawn.

### L5-M2 — MAJOR: Order sensitivity is still unreported and is stronger in the current analysis sample

**Evidence:** delegation options are randomized in order at `manuscript/design.tex:73`. All results on that order are inactive: both the control footnote at `results.tex:28` and paragraph at line 174 are comments. The latter also contains obsolete pre-exclusion p-values.

Read-only grouping of the current analysis sample yields:

| Delegation option order | Punishment | No-Punishment | No-Punishment minus Punishment |
|---|---:|---:|---:|
| Own decision first | 13/40 = 32.5% | 27/42 = 64.3% | 31.8 pp |
| Algorithm first | 21/40 = 52.5% | 21/37 = 56.8% | 4.3 pp |

`12_order_effects.py:26–56` estimates the logit interaction; the current manifest records p=0.0796 (`numbers.json:343–352`), with within-condition order differences of +20.0 pp and −7.5 pp. These replace the old interaction p=.115 and No-Punishment difference −4.6 pp.

**Revision:** report all four cells and interaction uncertainty, ideally also an interaction on the probability scale; keep the average treatment effect distinct from the unresolved heterogeneity. These cells do not establish that order caused an artifact, and a logit interaction is not itself the probability-scale difference in differences. The old report's claim that this invalidates the reversal, and its suggestion of deliberate suppression, were too strong. It remains an obvious, motivated robustness disclosure.

### L5-M3 — MAJOR: The new exclusion rule is disclosed, but an all-completer sensitivity should accompany the new primary analysis

**Evidence:** `manuscript/results.tex:3` and `manuscript/appendix.tex:116` now explain the exclusion of two No-Punishment Player As with at least eight zero predictions. `scripts/python/lib/io.py:20–28` makes this exclusion the default for every Player A analysis. The historical exhibit package documents both as non-delegators and describes the credible-guess distribution (`quality_reports/exhibits_excl_incredible_guessers/exhibits_excl_incredible_guessers.tex:14–28`). This is a behavior-based rationale, not evidence that cases were selected for their effects on results.

A concise sensitivity comparison is already feasible:

| Sample | Player A N | Delegation gap | Pearson p | Fisher p |
|---|---:|---:|---:|---:|
| All completers | 161 | 16.76 pp | .0334 | .0407 |
| Current primary exclusion rule | 159 | 18.26 pp | .0212 | .0264 |
| Current rule plus attention passers | 129 | 19.48 pp | .0272 | .0345 |

These are independent read-only recomputations. They show that excluding the two cases does **not** create H1 significance. Nevertheless, the paper now reports only the strengthened primary estimate. The appendix describes “three respects” of preregistration deviation while embedding the new exclusion in the recruitment deviation (`appendix.tex:116`); this leaves the timing and status of the exclusion decision unclear.

**Revision:** explicitly identify whether the rule was preregistered and when it was adopted, give role-by-condition included/excluded counts, and report the all-completer sensitivity for the headline and affected performance/effort analyses. A short appendix comparison would resolve this without changing the justified primary rule. Do not label an attention-passer comparison an all-completer sensitivity: it retains the new exclusions.

### L5-M4 — MAJOR: Belief heterogeneity is transparently shown as sample-sensitive, then generalized beyond that sample

**Evidence:** `tables/reg_belief_specs.tex:38–46` shows full-sample AMEs of 1.3 and 1.4 pp per £0.10 (p=.388/.370; N=80/78), compared with 4.7 and 5.5 pp among passers (p=.011/.006; N=60). `manuscript/results.tex:97` acknowledges this split. The heterogeneity clause has also been removed from the numbered Result at line 103; this is real progress.

The statements at `results.tex:100,155`, however, still say generally that subjects expecting a larger own-decision penalty are more likely to delegate. The positive significant result should retain its attention-passer qualifier every time it supports the mechanism account. The existing full-sample columns already expose the weak full-sample relationship; an omitted auxiliary logit table is not necessary to establish that disclosure.

Attention failures are 19/80 (23.8%) versus 11/79 (13.9%); the current difference has Pearson p=.1133, recomputed for this review. Conditioning on a check administered after delegation can alter sample composition, but this difference does not establish a treatment-induced comprehension deficit. The old claim that H1 Fisher becomes insignificant among passers is now false: current p=.0345, also reported in `_outputs/attention_check_comparison.md:61–74`.

**Revision:** label the result as an exploratory association among belief-screen passers, report exclusion counts and sampling limits, and provide matching full-sample versions of weighted/decomposed specifications if relying on them. Do not interpret a change in significance between samples as proof that the slopes differ.

### L5-M5 — MAJOR: Effort statistics have been added, but the numbered causal conclusion still exceeds the evidence

**Evidence:** `manuscript/results.tex:143` now reports absolute-error improvement of 8.11 versus 0.51 lbs, Welch p=.027 and Mann–Whitney p=.014, alongside initial-error balance. It also acknowledges that effort is unobserved and explicitly allows performance pressure to mask additional effort. The old “no statistics for improvement” criticism is resolved.

Despite that, Result 5 at `results.tex:146` still says the prospect of punishment “does not induce additional effort.” Observed final predictions exist only for selected non-delegators: N=31 without punishment and N=46 with punishment (`numbers.json:335–341`). Punishment itself changes entry into these groups. Similar observed initial error cannot establish that their counterfactual effort responses are comparable. The active offsetting-selection footnote at `results.tex:143` does not resolve this identification problem. One final prediction and screen duration are noisy proxies; now that continuous-error results are reported, the old description of the entire effort analysis as merely a binary draw is obsolete.

**Revision:** make the numbered statement descriptive: the observed performance and time proxies provide no evidence of greater effort under punishment among non-delegators. State the selection limitation explicitly alongside the proxy limitation. Retain the new statistics and the alternative pressure explanation; they improve the analysis without identifying an average causal effect on effort.

### L5-M6 — MAJOR: The exploratory test family and evidence for the asymmetry claim remain unclear

**Evidence:** `manuscript/results.tex:5` identifies Results 3–5 as exploratory but says only that “several” secondary analyses were preregistered. The mapping is not supplied at `manuscript/appendix.tex:114–116`. The belief analyses span alternative aggregations, outcome-specific differences and attention restrictions (`results.tex:90–100`; `tables/reg_belief_specs.tex:10–46`). No multiplicity interpretation accompanies the selected p-values.

A new footnote at `results.tex:100` says “We find no such asymmetry” when discussing different responses to positive versus negative expected delegation penalties, but supplies no model, N, estimate, interval or test. The included regressions do not estimate that sign-dependent response. I found no corresponding piecewise/sign interaction in the inspected numbered Python scripts; this is an unverified claim, not proof the analysis was never conducted elsewhere.

**Revision:** give a compact preregistered-secondary/post-hoc mapping, define inferential families for claims that depend on statistical significance, and report adjusted evidence or explicitly treat those findings as tentative exploratory patterns. Provide the asymmetry specification and uncertainty or remove its empirical assertion. Do not mechanically Bonferroni-correct every p-value printed anywhere in the paper: multiple representations of the same contrast are not automatically separate scientific hypotheses. The old review's blanket “34 tests” threshold is withdrawn.

### L5-m1 — MINOR: Residual performance wording outpaces the interaction qualification

`manuscript/results.tex:109,132` now explicitly says that treatment-specific performance gradients do not differ significantly. `07_performance.py:124–164` implements the tests and `numbers.json:372–377` reports p=.548 without controls and .487 with controls. Result 4 at `results.tex:113` has been narrowed to a pooled association. These resolve the core of old M3.

At `results.tex:110`, however, “It is precisely the better performers who retain control … particularly when punishment is possible” still invites a stronger heterogeneity interpretation. Keep this descriptive and show the interaction estimate/CI in the appendix. The p=.039 comparison between delegators across conditions describes composition of selected groups; it does not substitute for the treatment-by-performance test.

### L5-m2 — MINOR: Recruitment attrition remains unquantified

`manuscript/results.tex:3` and `manuscript/appendix.tex:116` describe rematching and an extra pair, but no started/randomized/dropout denominators. `scripts/python/09_consort.py:1–5` explicitly says the recruitment funnel requires the Prolific audit log; the available manifest counts begin with completers (`numbers.json:151–166`). Report a short role/arm flow if the log is available, or explicitly state what cannot be recovered. A formal CONSORT diagram is not inherently mandatory for this study, contrary to the old report's categorical claim.

### L5-m3 — MINOR: Clarify the scope of collected measures and off-paper analyses

`manuscript/design.tex:79–81` still describes population-relative performance beliefs and risk preferences without reporting their substantive use. The current mechanism discussion explicitly entertains uncertainty preferences (`results.tex:129–132`). A brief analysis inventory or explanation of omitted measures would clarify scope; any new heterogeneity analysis should be marked exploratory. These measures are not automatically required controls, and a relative rank among humans is **not** a direct measure of belief in own-versus-algorithm performance. The old review overstated that identification argument.

Before any auxiliary tables are restored, reconcile their notes: `tables/power_mde.tex:16` refers to a TOST “used in Result 2” that is currently absent, and `tables/reg_delegation_robustness.tex:31` calls a good-outcome belief association “preserved” at p=.125. Those are repository-artifact issues, not claims currently made through included tables. Different logit and probit coefficient scales are expected; reporting both links is a legitimate sensitivity check when labeled and compared through probabilities/AMEs.

## Disposition of every baseline finding

Statuses concern the old claim, not just whether a similarly titled concern remains. Only the active findings above count toward severity totals.

| Old ID | Status | Current disposition |
|---|---|---|
| C1 | PARTIAL / downgraded | H1 is stronger after exclusions and exact inference corroborates it. CI/power reporting still missing; numerical power inconsistency identified. Old below-MDE invalidity/post-hoc-power framing withdrawn. See L5-M1. |
| C2 | PARTIAL | Numbered Result is cautious and both punishment regression samples are reported, but categorical summaries and absent equivalence/CI reporting remain. Use current full-sample numbers. See L5-M7. |
| C3 | OPEN / downgraded | Order analysis remains outside the paper; current interaction p=.0796. No inference of deliberate suppression or a proven order artifact. See L5-M2. |
| M1 | OPEN / reframed | Exploratory status is stated, but mapping/multiplicity interpretation remains unclear. Blanket 34-test correction withdrawn. See L5-M6. |
| M2 | PARTIAL | Full/passer evidence is visible and the numbered Result drops the subgroup clause. Remaining summary generalization needs qualification. See L5-M4. |
| M3 | PARTIAL / downgraded | Interaction is now computed and insignificance acknowledged; narrowed numbered Result. Residual prose issue only. See L5-m1. |
| M4 | SUPERSEDED | Player B table remains omitted, but both actual and hypothetical within-condition comparisons are paired; their validity does not depend on between-condition demographic balance. Publishing the table is a reasonable transparency option, not proof of suppression. Do not infer a treatment effect from differences between actual and hypothetical punishment profiles. |
| M5 | PARTIAL | H1 Fisher discrepancy resolved under current exclusions; both punishment regression samples reported. Attention counts/limitations and the new exclusion sensitivity remain useful. See L5-M3/M4. |
| M6 | PARTIAL / downgraded | Measures still not substantively used in the inspected analysis, but neither is a mandatory covariate or direct parity manipulation check. See L5-m3. |
| M7 | PARTIAL | Improvement means/tests and pressure/proxy caveats added. Selected-sample causal effort claim remains. See L5-M5. |
| M8 | SUPERSEDED | Current design explicitly matches hypothetical belief flow across conditions (`design.tex:77`); salience and performance pressure are discussed (`results.tex:132,143,152–153`). Attention differences do not demonstrate cognitive load. Demand/load remain possible unisolated alternatives, not established explanations or separate submission-blocking findings. |
| m1 | SUPERSEDED | The “thin checks” judgment is not an independent defect. Concrete current gaps are counted above; included checks have substantive purposes. |
| m2 | OPEN | Recruitment denominator still unavailable in inspected outputs. See L5-m2. |
| m3 | SUPERSEDED | The alleged opposite significance-star conventions concern inactive auxiliary tables, not a present disagreement between included robustness tables. No current robustness finding on journal policy. |
| m4 | SUPERSEDED | Logit versus probit is legitimate when labeled; unequal raw coefficients are expected. Artifact wording and AME comparability belong to L5-m3. |

**Priority:** align punishment claims with the interval evidence; disclose current order sensitivity; add compact uncertainty and sample-sensitivity reporting; then qualify the mechanism results and document the exploratory tests. No new experiment is implied by this review.
