# `results.tex` — old vs new

## Overview

The old `results.tex` is **327 lines** with two major subsections (Delegation
behavior; Punishment behavior) plus an extensive end-of-file dump of bullet
outlines, alternative analyses considered, and many bracketed planning notes.
It has the manuscript's headline numbers correctly reported but mixed in
with a lot of self-questioning, alternative interpretations, and explicit
TODOs.

The new `results.tex` is **104 lines** with five tightly-organised
subsections (Sample/attention/balance, Result 1, Result 2, Beliefs and
consistency, Mechanism) and a more disciplined treatment of what is
preregistered vs exploratory.

## What changed in the prose

- **Subsection structure expanded**: old had two sections (Delegation; Punishment) plus a fragment "Delegation decision" subsection at the very bottom that was a presentation outline; new has five clear subsections.
- **Headline framing of Result 1** softened: from "we not only reject Hypothesis 1 but also observe an effect in the opposite direction, suggesting that the possibility of punishment discourages delegation" to a more measured presentation that explicitly notes the preregistered one-sided test fails by construction (since the realised direction is opposite) and that all subsequent mechanism analyses are exploratory.
- **Headline framing of Result 2** softened: from "Player A cannot avoid punishment by delegating" to "we cannot reject equal punishment of delegated and self-made decisions; the point estimate runs in the H2 direction but is small relative to the test's confidence interval at the achieved sample size". Explicit MDE / under-power-against-moderate-effects caveat added.
- **Mean overall_score corrected**: was 3.05 in old, actually 2.93 across all 161 subjects (3.05 was wrong).
- **Chi² p-value corrected**: was 0.049 in old (Yates' continuity-corrected), actually 0.033 uncorrected (modern econ convention; Stata default).
- **M2 overall_score for Punishment non-delegators**: 2.97 in old → 2.98 in new (rounding).
- **Tables**: Table 1 was inline in the old; now `\input{../tables/reg_delegation.tex}` from a generated artefact.
- **Significance stars stripped** from all tables (AEA editorial policy).
- **New paragraph** at the start of §sec:result2: explicit MDE framing and explicit acknowledgment that the test is well-powered against large effects but underpowered against modest ones.
- **§sec:mechanism** restructured: old had effort and beliefs interleaved with the H1 discussion; new gives mechanism its own subsection with M1, M2, M3, M4 explicitly weighed and treated as exploratory; M3 (process ownership) is the most-consistent reading but supported only by the heterogeneity sub-sample (60-subject Column 3) plus the selected non-delegator effort comparison; M4 (experimenter demand) explicitly cannot be separated.
- **Player A attention-pass rate filled**: was unstated in old; now 131/161 = 81.4%.
- **Player B punishment-pass rate**: was 135/161 = 83.9% in old (preserved).
- **CONSORT pointer** added to the §Sample paragraph.

## Dropped items

### Unrealised analyses ("Future analysis: ...")

(Most of these became the [pending] markers I subsequently filled.)

- **Binned scatter of delegation share vs overall_score by condition** — described as "produce a binned scatter plot with delegation share on the y-axis, performance score on the x-axis, dot size proportional to the number of subjects, separately by treatment". I implemented this as `figures/performance_delegation_scatter.png` via `07_performance.py` but the new manuscript doesn't currently `\includegraphics{}` it (the figure exists; it just isn't linked from the prose). **Worth bringing in** as the visual evidence for the M3 mechanism story.
- **Regression of chosen punishment on delegation, outcome, interaction, beliefs about Player A's performance, and demographics** — "Report as Appendix Table; flag the coefficient on the interaction." I implemented this as `tables/reg_punishment.tex` via `06_logit_punishment.py`; the new manuscript does include it via `\input{../tables/reg_punishment.tex}`.
- **Robustness-without-attention-check exclusion table** — "results without the attention-check exclusion (robustness)". **Not yet generated**; the new manuscript's body still says "all results are robust to including these subjects (Appendix~\ref{appendix:regs}, full robustness panel pending the analysis pipeline)".

### Self-questioning notes / alternative interpretations

- **"those are the p-values for the two-sided hypothesis, but we have a one-sided hypotheis. Should we instead have equal punishment and then reject that?; also in STATA I find other p-values"** — the author noting the one-sided/two-sided mismatch and the chi² discrepancy with Stata. Both issues are now resolved.
- **"This may be surprising, especially for good outcomes, given that punishment even was costly."** — observation that punishment > 0 even for good outcomes, with a hint of puzzlement. Currently the new manuscript notes this but does not flag it as surprising.
- **"On the one hand, ..."** — a fragmentary opening to a paragraph that was never written.
- **The bracketed `[Inequality/deservingness motive: other guy does not do anything and can earn 5 without working, like this is unfair...but delegator does not know what the evaluator had/did not have to do]`** — an alternative explanation for why Player B punishes good outcomes (a "you didn't have to work for your £5" inequality motive). **Currently not in the new manuscript.** Could be a useful candidate explanation for the puzzling baseline punishment of good outcomes.
- **`[hypothetical punishment in treat?]`** — author considering whether to discuss the No-Punishment hypothetical punishment. **Currently absent.**
- **`[interpretation: punishment is outcome-based, not delegation-based, but this is not surprising given that performance is controlled for. However, if shirking mattered we could think about observing more punishment when delegating, even for the good outcome; Hence, this can explain positive punishment at least for good outcomes when delegating]`** — a specific interpretive thread on shirking-as-explanation for positive good-outcome punishment. **Not in the new manuscript.**
- **`[More analysis: Are beliefs correlated with delegation decision? Does everyone feel the same or is there large heterogeneity? Maybe show belief distributions for the four scenarios. Compare beliefs for delegated decisions (both outcomes) between those that delegated and those that didnt in Baseline (hypothetical vs. relevant)]`** — three planned analyses on belief heterogeneity. **None implemented.** A belief-distribution figure (4 small panels) could strengthen §sec:beliefs.
- **`robustness checks with overconfidence (2 ways) and beliefs about performance`** — planned robustness on overconfidence + beliefs as additional regressors. **Not implemented.** The cleaned data has `wa_confidence`, `highest_confidence`, `overconfidence`, `overconfidence_to_others` columns ready.
- **`order effects`** — planned analysis of order effects in delegation, punishment, beliefs. The Stata file has `bys treat random_order_del: sum delegation` already coded. **Not implemented in the Python pipeline.** The `random_order_del` column is in the cleaned data.
- **`[discussion of beliefs]`** — placeholder paragraph in the middle of the H1 discussion. The new manuscript has a §Beliefs subsection that addresses this.
- **`[Bharti and Dietvorst]`** discussion — a paragraph on uncertainty-and-algorithm-aversion citing Bharti & Dietvorst 2020 ("with increasing task uncertainty, subjects' preference for algorithms over their own prediction decreases"), with the author wondering whether their finding contrasts with this paper's. **Bharti is not currently cited.** This was a real interpretive thread the author wanted to pursue: "Key question, with higher performance comes lower or higher uncertainty? Depending on the answer to this question, our finding is in contrast or in line with the literature". **Worth pursuing** for the M3 mechanism discussion.
- **Reference to overconfidence as a treatment-balanced control**: "subjects exhibit significant overconfidence, measured by the weighted average belief about their performance. While this overconfidence may also partly reflect the information that the algorithm is performing equally well, it is not statistically different between both treatments." **The overconfidence-balanced-across-treatments observation is dropped.**
- **`[include in figure the split by who ended up delegating?]`** — planned modification to `figures/performance.png` to show the score distribution split by delegate/non-delegate. **Not implemented.**

### Specific results / patterns mentioned but not in new

- **The Pearson correlation between Player A delegation and her own performance beliefs**: "Similarly, the delegation decision of Player A is negatively related to their beliefs about own performance, even though not significantly so." Footnote in the old draft. **Not in new manuscript.** Could strengthen the M3 story (better-believed-performers delegate less).
- **The interpretation of the heterogeneity-in-Baseline-only result**: "[cant be for inherent motive because no such connection in treatment] Finding this relationship in the Baseline condition only indicates that Player A does not merely avoid directly causing a bad outcome and savoring directly causing a good outcome for Player B. Instead, it suggests a connection to anticipated punishment, such that Player A expects more severe punishment for delegated decisions (relative to non-delegated ones) the worse the outcome." — a more specific interpretive claim than what the new manuscript settles on. The new manuscript treats M3 (process ownership) as the candidate; the old had a slightly different reading (anticipation-of-conditional-punishment).
- **`[Inequality/deservingness motive]`** as a Player B punishment explanation (covered above) — also dropped.

### Dump at the end of the file (lines 178–328)

A massive set of bullet outlines, presentation-style summaries, and notes:

#### Presentation-style result summary (lines 180–188)
A 4-bullet "story" version of the results clearly written for an oral presentation. Useful as an outline if the author wants to give a talk.

#### Open analysis questions (lines 195–209)
- "performance measured as distance from truth" — alternative measure (continuous, not 0/1)
- "why did the people that did not delegate also make the last guess, so there is no difference in time cost?" — design rationale that's now in §design (paragraph saying "Player A also makes the eleventh prediction whether or not she ultimately decides to delegate")
- "why did they not make the decision first and then decide to delegate?" — design alternative considered and rejected
- "do they actually try harder in 11th decision?" — partially addressed in §sec:mechanism M2 (the differential-improvement footnote)
- "explore order effects in punishment and belief about punishment" — not done
- **"Think more about this potential non-linearity, i.e. If I know it will fail, then I may want to delegate. If I know I will succeed, I want to do it myself. Hence, my preference on delegation may change depending on the chance of success. What kind of literature is here, starting with the DIetvorst papers (maybe the 2020 one)?"** — **A specific theoretical thread on conditional-on-success delegation preferences**. The M3 process-ownership story partly captures this (better-performing → less delegation in the Punishment condition). The Dietvorst 2020 connection is not in the new manuscript.
- "what about people delegating because they themselves feel responsible even though they may be aware that the other person does not feel the same?" — feel-responsible-vs-be-blamed distinction
- "there are hedging motives in the performance elicitation task" — methodological note (already addressed in design footnote)

#### "Evaluator" subsection enumeration (lines 212–222)
A planned 8-item analysis of Player B:
1. Attention (135/161 pass; spending time: 10%-60s, 20%-78s, 30%-87s) — partially in new (attention rate, but no time distribution)
2. Beliefs about performance (mean 4.32 → overestimate) — **Not in new manuscript**. Player B's beliefs about Player A performance are in the cleaned data but not analysed.
3. Punishment behavior (averages and distribution) — averages in new; distribution figure not in new
4. Punishment and Performance Beliefs — not in new
5. Punishment and Socio-Demographics — partially in new (the `06_logit_punishment.py` regression has demographic controls)
6. Hypothetical Punishment (No-Punishment hypothetical responses) — not analysed in new
7. Frequency of Punishment — in new (`figures/punishment_shares.png`)
8. Order Effects — not in new

#### "Story" enumeration (lines 226–246)
A bullet list of additional findings the author was considering:

- **"Punishment (all four individually, but also differences) is independent (Pearson and Kendall) of beliefs about performance, so this holds consistently across the whole (mostly supported between 2 and 6) distribution of performance beliefs. Hence, from a punishment perspective it doesn't matter whether you delegate when task is easy or harder."** — a result on punishment-vs-belief independence. **Not in new manuscript.** Useful to refute alternative explanations.
- "For those thinking longer about the punishment decision, there is a positive correlation between easiness of the task and punishment for a bad outcome when you don't delegate vs. when you delegate." — a heterogeneity-by-time-on-screen result. Not in new.
- "Punishment correlated with socio-demographics?" — not explicitly in new beyond the regression.
- **"Consistent with punishment: for those that state that individuals should be held responsible for AI-generated decisions responsibility avoidance is less possible (pos. correlation between 'nodel-del-bad' and 'responsibility')"** — a result tying Player B's stated views on AI responsibility to their punishment behaviour. The `responsibility` column is in the cleaned data. **Not in new.** Could be a nice connection between attitudes and behaviour for the M4 demand-rebuttal.
- "Delegators overestimate how much is being punished, but conditional on not punishing zero in all 4 cases, they are accurate." — a finer point on belief-vs-actual punishment alignment. The new manuscript reports the overestimate but not the conditioning-on-positive-punishment refinement.
- The "Ways to filter" enumeration (`pass att1`, `pass att2`, `error confidence`, `time spent on screen`) — possible alternative attention/quality filters. **Not explored in new.**

#### Substantive notes (lines 248–328)

- **"Evaluators who did not perform the task themselves but were presented with the same task overestimated the performance similarly to evaluators."** — a finding that Player B's overestimation is similar to Player A's. **Not in new.**
- **Feier et al. comparison: "risk averse were also more likely to delegate"** — a Feier finding worth comparing to in the manuscript. **Not currently checked or compared.** The cleaned data has `switching_point` (MPL).
- **Feier et al. comparison: "Here it makes sense that the worse you are, the more likely you delegate, because it increases expected success for the third party. But in my experiment this is not clear and therefore more interesting."** — a substantive contrast with Feier et al. that strengthens the M3 process-ownership story. **Not in new manuscript explicitly.**
- "Would be nice to have randomly chosen pictures, so that the extra picture also shows up among the first pictures." — design-improvement note for a follow-up.
- **A long quote from Coffman** on punishment-decreases-not-due-to-diffusion-of-responsibility-but-direct-interaction. Already in literature in compressed form.
- **A long quote from Steffel et al.** on credit-vs-blame asymmetry: "decision makers may prefer to delegate to someone else in fear of receiving the punishment or blame... people care more about avoiding blame for bad outcomes than getting credit for good outcomes." This is the **conceptual basis for the M3 process-ownership story**. The new manuscript invokes process ownership and cites Steffel briefly but doesn't ground it in this specific Steffel passage.
- **"feeling responsible versus being blamed"** — the same distinction noted above.
- **"result in lit review of chugunova and sele is algorithm aversion stronger in moral contexts (evidence Gogoll Uhl 2018) I can say that this was when punishment is possible. Without punishment possibility there seems to be algorithm appreciation. Hence it is rather the fear of judgement when employing algorithms in moral tasks and the potential consequences than the pure morality of the decision."** — **An important reframing of the existing literature**: the algorithm-aversion-in-moral-contexts result may be better understood as fear-of-judgement-when-punishment-is-possible. **Not in the new manuscript** but could substantially strengthen the contribution-positioning.
- "Delegation behavior maybe in line with gogoll uhl 2018, because algorithm use was punished more." — speculative comparison.
- **"extension of either delegate to human or algorithm not possible because has been done before (Gogoll Uhl 2018) to account for effect of loss of control."** — an explicit design-choice note about why this paper does NOT include a human-delegation arm. Useful if a referee asks.
- "use ttest_rel to compare punishments instead of ttest_ind" — methodological note (paired test for the strategy method).
- "Feier et al uses GLM logit IRLS. Is that different from the logit I am using?" — methodological question, probably resolved.
- **"results not so consistent with Maasland and Weißmüller, that bad news you delegate more, whereas good news you delegate less"** — a comparison with Maasland & Weißmüller (the loss-of-psychological-ownership theory). **Not currently engaged.** This is the theoretical framework that motivates M3 most directly.
- "during belief elicitation, they already know that two scenarios are irrelevant, so maybe look at beliefs if affected" — a planned check for belief-elicitation contamination by the realised cell.
- **"check if people that are better/more confident in last guess have different beliefs"** — heterogeneity check.
- "think about all the reasons that can impact the delegation behavior, e.g. risk aversion: oh for a single prediction I would like to delegate whereas for multiple I would have not or so, but this cannot explain treatment differences." — a risk-aversion-as-confound argument.
- "filter in Feier et al only those that punish and check whether if only punishment were possible they have the same results as I have." — re-analysis of Feier et al. data. Probably out of scope.
- **"Regarding Feier et al: If I always say that punishment in their experiment could be due to the signal value in delegation (concerns regarding relative performance), then this holds for both their treatments so should technically not explain why they find differential rewarding in the machine treatment."** — **A real critique of the new manuscript's own Feier-reconciliation argument.** The new manuscript's reading is that signal-extraction explains Feier's differential punishment; this note asks whether that signal-extraction story can also explain the human-vs-machine differential (which is what Feier observed). Worth thinking through carefully — this critique could come up from a careful referee.
- "when showing balance across observables, then be careful to use chi-squared test for categorical variables." — done in `02_balance.py`.
- "Excluding subjects that failed the attention test was pre-registered." — captured in PAP appendix.
- "Go through all variables and check which information is still there, e.g. questionnaire responses, hypothetical answers..." — review note. The data dictionary now does this.
- **"In interpretation, talk about experimenter demand effects, but unclear in which direction they may go."** — done in §conclusion.
- **"I cannot know if beliefs follow the delegation decision (motivated beliefs/hedging) or whether the delegation decision follows beliefs."** — captured in §sec:beliefs "Caveat on causal direction".
- **"What are motivated beliefs here? Only two cases can be relevant, but I can still have motivated beliefs about the other two cases to justify/not regret my delegation decision."** — a more refined version of the motivated-beliefs-vs-belief-driven-delegation question. Currently the new manuscript treats this somewhat in §sec:beliefs but not as carefully as this note hints.
- "Show that randomization worked on socio-demographics, attention checks(?), time taken, ..." — done for socio-demographics; not for attention checks or time taken.

## Why the changes (where I can infer)

- The corrections to mean overall_score (3.05 → 2.93) and chi² (0.049 → 0.033) came from re-running the analysis pipeline against the cleaned data and discovering the discrepancies.
- The H1 reframing as "rejection of the standard prediction in favour of the opposite direction" with explicit one-sided/two-sided disclosure responded to the methods referee.
- The H2 underpowered-against-moderate-effects framing responded to the methods referee's critical peeve about reporting nulls without power calcs.
- The M3 reframing as candidate hypothesis and explicit M4 (experimenter demand) discussion responded to the domain referee's concern about over-claiming the mechanism.
- The compression came from converting an active-research scratchpad into a polished section.

## High-leverage items to consider bringing back

In rough priority order, of items currently not in the manuscript:

1. **Linking M3 to the Steffel et al. credit/blame asymmetry quote** — would ground the process-ownership story in the literature.
2. **Reframing the Gogoll-Uhl algorithm-aversion-in-moral-contexts result as fear-of-judgement-when-punishment-is-possible** — substantially strengthens the contribution.
3. **Engaging with Maasland & Weißmüller's loss-of-psychological-ownership theory** — direct theoretical motivation for M3.
4. **The Feier-reconciliation critique** ("signal-extraction holds for both their treatments so shouldn't explain differential rewarding") — a referee-grade critique to think through and address proactively.
5. **The binned-scatter figure** for §sec:result1 — visual evidence for the heterogeneity that drives M3.
6. **The `delegation_hypo` analysis** for No-Punishment subjects — direct corroborating evidence for H1.
7. **The order-effects analysis** in delegation/punishment/beliefs.
8. **The Bharti & Dietvorst 2020 discussion** on uncertainty and algorithm aversion.
9. **Player B's beliefs about Player A performance** — under-exploited cleaned column.
10. **Punishment-vs-performance-beliefs independence** — refutes an alternative.
11. **Player B `responsibility` Likert correlated with their punishment** — attitudes-behaviour link.
