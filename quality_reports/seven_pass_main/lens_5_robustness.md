# Lens 5 — Robustness, Power, and Unreported Analysis

Seven-pass adversarial review of *Accountability and Algorithmic Delegation: Experimental Evidence*.
Reviewer stance: sharp, skeptical AER/QJE referee.
Scope: `manuscript/{abstract,introduction,literature,design,results,conclusion,appendix}.tex` as compiled by `main.tex`, plus `scripts/` and `quality_reports/` as evidence of analyses run.

**Verdict: 3 / 10.** The prose is disciplined and the mechanism section is unusually honest about what it cannot settle. But the paper's *statistical* self-defense is close to absent. There is no confidence interval anywhere in the manuscript, no power calculation, no equivalence test, no multiple-testing acknowledgment, and no order-effect discussion — and the repository shows that all four were computed. Two headline claims (the reversal, and the punishment null) are each weaker than the text states, and the supporting numbers proving so are sitting in `scripts/python/_outputs/numbers.json` and `tables/power_mde.tex`.

**Counts: 3 CRITICAL, 8 MAJOR, 4 MINOR.**

---

## CRITICAL

### C1. The headline effect is smaller than the study's own minimum detectable effect, and the paper reports neither

`manuscript/results.tex:9-10`:

> "The introduction of potential punishment thus significantly \textit{reduces} delegation by $16.8$~percentage points (Pearson Chi-squared, $p=0.033$)"

`manuscript/results.tex:149`:

> "The reversal in Result~\ref{res:delegation} is robust"

`manuscript/introduction.tex:14`:

> "while the drop in delegation under punishment is robust, which motive produces it is a question we narrow rather than settle."

The repository contains the ex-ante power calculation. `tables/power_mde.tex:7`:

> `H1 (delegation, two-proportion test) & Baseline $p_0=0.50$ & $\Delta = 0.215$ (21.5 pp)`

At n = 80 per cell, α = 0.05 two-sided, power = 0.80, the study's MDE is **21.5 pp**. The realized effect is **16.8 pp** — 78% of the MDE. Post-hoc power at the observed effect is **58%**, and the 95% CI on the delegation gap is **[1.6 pp, 32.0 pp]** (my computation from the reported cell shares, n = 80/81). A referee will compute this in ninety seconds and conclude that the paper's central contribution is a coin-flip-powered p = 0.031 whose interval nearly touches zero, described three times as "robust."

Two aggravating facts:

1. **The word "power" appears nowhere in the compiled manuscript.** The only hit is a commented-out to-do at `manuscript/results.tex:169`:
   > `%\paragraph{Power.} \todo[inline]{Add an ex-post (or, preferably, the original ex-ante) power analysis here, framed as in \cite{feier_hiding_2022}.}`

   The to-do was deleted rather than executed, even though `scripts/python/_outputs/power_calc.py` was written and `tables/power_mde.tex` generated. `tables/power_mde.tex` is **never `\input`** by any compiled file (verified: the only table inputs are `reg_delegation`, `reg_punishment`, `reg_belief_specs`, `balance_player_a`, `reg_punishment_extensive`).

2. **A prior referee explicitly demanded exactly this and it was not delivered.** `quality_reports/peer_review_algorithms_and_responsibility/referee_methods.md:45`:
   > "No ex-ante power calculation reported anywhere I can find. n=161 Player As (≈80 per arm) is small for a between-subject behavioural test where the headline difference is 17 percentage points... This is the load-bearing weakness."

   The scripts were then written. The results were not put in the paper.

There is also no sample-size justification. `manuscript/results.tex:3` states only that "We preregistered the collection of data from $320$ participants ($80$ subjects per role per treatment)" — the 80 is asserted, never justified by a power target.

**Ask:** report the 95% CI on the delegation gap in the body; state the ex-ante MDE and the sample-size justification in the design section; add randomization-inference or bootstrap p-values for a binary outcome at this n; and strike "robust" or qualify it.

*Note on the settled-decisions list: this is not a request for a wave robustness check. The pooled n = 161/role is taken as given. The objection is that the paper does not tell the reader what that n can and cannot detect.*

---

### C2. Result 2 is a null presented as equivalence; the equivalence test was run, fails at the tighter bound, and is unreported

`manuscript/abstract.tex:1`:

> "Delegation offers no protection in return. Recipients punish delegated and self-made predictions alike"

`manuscript/conclusion.tex:6`:

> "Delegation, in turn, offers no protection against punishment. Recipients punish delegated and self-made predictions alike"

These are assertions of absence. The supporting evidence, from `manuscript/results.tex:48`, is:

> "The punishment gap for bad outcomes thus runs in the direction predicted by Hypothesis~2 but is small and statistically insignificant ($\pounds 0.07$; paired $t$-test $p=0.13$; Wilcoxon signed-rank $p=0.54$)."

What the repository knows and the paper does not say:

| Quantity | Value | Source |
|---|---|---|
| Bad-cell insulation, passers | £0.077 | `numbers.json: h2_diff_bad_mean` |
| SD of the within-subject difference | £0.435 | `numbers.json: h2_diff_bad_sd` |
| **95% CI on insulation** | **[−£0.027, +£0.181]** | my computation, n = 67 |
| MDE at 80% power | £0.149 | `numbers.json: h2_mde_bad_at_80pct_power` |
| TOST at ±£0.20 | equivalent, p = 0.012 | `numbers.json: tost_bad_bound_0p20_*` |
| **TOST at ±£0.10** | **NOT equivalent, p = 0.332** | `numbers.json: tost_bad_bound_0p10_*` |

Three problems, each independently disqualifying at AER:

1. **The interval admits a large effect in H2's predicted direction.** The upper bound, £0.181, is **32% of the self-made bad-outcome punishment level (£0.571)**. "Punish delegated and self-made predictions alike" is not something these data establish; a one-third reduction in punishment for delegating is fully inside the interval, and that would be a headline result in the other direction.
2. **The observed insulation is half the MDE.** £0.077 vs £0.149. The test was never capable of resolving the effect it reports as absent.
3. **The equivalence bound that "works" is as large as the paper's own largest punishment effect.** The TOST passes only at ±£0.20. But `manuscript/results.tex:35` reports the outcome effect — the paper's strongest punishment finding — as exactly "$\pounds 0.20$ on average." An equivalence region as wide as the biggest effect in the data is not an equivalence result. And at the tighter ±£0.10 bound the test fails outright (p = 0.33). The paper reports neither.

Compounding this, the regression evidence actually leans *toward* H2 and the abstract does not admit it. `manuscript/results.tex:54`:

> "The \textit{Delegated}~$\times$~\textit{Bad outcome} interaction, which captures any insulation from punishment after bad outcomes, amounts to $-0.103$ and is weakly significant ($p=0.08$)."

A p = 0.08 point estimate in the hypothesized direction, in an underpowered test, becomes "punish delegated and self-made predictions alike" in the abstract and conclusion. That is the single largest overstatement in the manuscript.

**Ask:** replace the flat null with CI framing in the abstract, body, and conclusion ("we can rule out insulation larger than £0.18, or ~32% of baseline punishment"); report the TOST at both bounds, including the failing one; report the MDE.

---

### C3. A 20-pp order effect concentrated in the Punishment condition was computed, drafted into the results section, and then commented out

`scripts/python/12_order_effects.py` computes it. `numbers.json`:

```
order_pun_diff_pp    = 20.0     order_pun_chi2_p    = 0.0704
order_nopun_diff_pp  = -4.6     order_nopun_chi2_p  = 0.6742
order_logit_interaction_coef = 1.0217   order_logit_interaction_p = 0.115
```

The finding was written up. `manuscript/results.tex:167`, **commented out**:

> `%\paragraph{Order effects.} ... Order effects are localised to the \textit{Punishment} condition: presenting the algorithm option first roughly doubles delegation ($52.5\%$ vs $32.5\%$ when the own-decision option is first; $\chi^2$ $p=0.070$), while the \textit{No-Punishment} condition shows no order effect ($p=0.674$)`

What survives into the compiled paper is a single footnote at `manuscript/results.tex:29`:

> "Including a control for the random order in which the two delegation options appeared on screen leaves the treatment coefficient essentially unchanged (Punishment coefficient $-0.48$ ($p=0.019$), with the ``algorithm first'' order indicator at 0.27 ($p=0.21$), starting from the specification in Column~(3))."

This footnote is true and misleading. Adding an order *main effect* to a randomized design cannot move the treatment coefficient much — that is not the threat. The threat is the *interaction*, and the interaction is where the action is. Working from the reported cell shares:

- Own-decision-first arm: Punishment 32.5% vs No-Punishment ≈ 61.6% → gap ≈ **29 pp**
- Algorithm-first arm: Punishment 52.5% vs No-Punishment ≈ 57.0% → gap ≈ **5 pp**

**The headline reversal is essentially confined to one order arm.** The order effect *within* the Punishment condition (20.0 pp) is larger than the treatment effect itself (16.8 pp). The interaction is p = 0.115 — not significant, but at n = 40 per order-by-condition cell it is not remotely powered either, so "not significant" is not reassurance. Suppressing this while retaining a footnote that implies the issue was checked and cleared is the kind of selective reporting a referee treats as a credibility event, not a robustness gap.

**Ask:** restore the order-effects paragraph, report the interaction and the cell-level shares, and state plainly that the design cannot resolve whether the reversal is order-dependent.

---

## MAJOR

### M1. No multiple-testing correction, and no acknowledgment that one might be warranted

`manuscript/results.tex` contains **34 reported p-values**. The words "multiple", "Bonferroni", "family-wise", "false discovery", "Holm", "Romano", and "Westfall" appear **zero times** in any compiled file. The preregistration specifies two hypotheses; the paper reports outcomes across delegation, punishment (intensive and extensive), beliefs (four cells plus two differences plus three aggregation schemes), performance, improvement, screen time, and a hypothetical delegation question.

The only gesture is `manuscript/results.tex:5`:

> "The subsequent analyses serve to understand the mechanism behind these results. They are exploratory in nature, though several of them were outlined as secondary analyses in the preregistration."

"Several of them" does no work. A referee will demand the explicit mapping: which analyses were preregistered as secondary, which are post hoc, and — for the results the paper leans on (Result 3, Result 4, and the belief-heterogeneity finding) — what survives even a crude correction. The belief-heterogeneity p-values (0.011, 0.006, 0.010) are the paper's most-quoted mechanism numbers; against 34 tests, none of them clears a family-wise threshold.

### M2. The belief–delegation relationship exists only in the attention-passer subsample, and the specification where it fails sits unused in `tables/`

`manuscript/results.tex:101`:

> "Expected differential punishment does not predict delegation in the full sample (Columns~(1)--(2)). Among subjects who passed the attention check on the belief-elicitation screen, the relationship **sharpens**. A $\pounds 0.10$ larger expected punishment penalty for deciding herself is associated with a $4.7$~percentage-point higher probability of delegation (Column~(3), $p=0.011$)"

"Sharpens" is doing a great deal of euphemistic work. From `tables/reg_belief_specs.tex:38-46`:

| Sample | N | AME | p |
|---|---|---|---|
| Full Punishment (1) | 80 | 1.3 pp | 0.388 |
| Full Punishment + controls (2) | 78 | 1.4 pp | 0.370 |
| **Passers (3)** | **60** | **4.7 pp** | **0.011** |
| **Passers, weighted (4)** | **60** | **5.5 pp** | **0.006** |

The effect more than triples and goes from null to p = 0.011 when 20 of 80 observations are dropped. That is not sharpening; that is a subgroup result. And `tables/reg_delegation_robustness.tex:21-22, 31` — **generated but never `\input`** — reports the same specification without the exclusion:

> "Column (3) restricts to the \textit{Punishment} condition and includes the within-subject belief differences but \textit{does not} exclude subjects who failed the belief-screen attention check; the heterogeneity result is preserved: \textit{Task performance} $p=0.033$; \textit{Punishment beliefs: good outcome} $p=0.125$."

The note calls the result "preserved" at p = 0.125. It is not preserved. The uncompiled table is the one that would let a referee see this; it is the one left out.

This result is then promoted to a numbered Result at `manuscript/results.tex:107`:

> "Within the \textit{Punishment} condition, Player~As who expect a larger penalty for deciding themselves are more likely to delegate."

stated without any sample qualifier, though it holds only on 60 of 80 subjects.

### M3. Result 3 (selection) has no interaction test anywhere, and its bivariate relationship is not significant

`manuscript/results.tex:115`:

> "\textit{In the Punishment condition, better-performing Player~As are less likely to delegate. The additional delegation in the No-Punishment condition comes disproportionately from better performers.}"

`manuscript/results.tex:112`:

> "this relationship is considerably stronger in the \textit{Punishment} condition (Table~\ref{tab:reg_belief_specs}) than in the \textit{No-Punishment} condition (Figure~\ref{fig:performance_overview})"

and `manuscript/introduction.tex:16`:

> "Accountability disciplines algorithm use rather than fueling it, and it does so selectively among the decision-makers most likely to succeed."

Three problems:

1. **No treatment × performance interaction is estimated anywhere.** I searched every script and every key in `numbers.json`; the only interactions in the repository are `order_logit_interaction_*` and `punish_reg_*_interaction_*`. The claim "considerably stronger in the Punishment condition" is made by eyeballing a coefficient in a Punishment-only, passers-only table against a figure. This is the Gelman–Stern error: the difference between "significant here" and "not significant there" is not itself a test. For a claim promoted to the introduction, an interaction with its own standard error is mandatory.

2. **The underlying bivariate relationship is not significant.** `scripts/python/_outputs/attention_check_comparison.md`, "Performance × delegation correlation (Punishment cond. only)": Pearson r = −0.189, **p = 0.093** (full); r = −0.224, **p = 0.083** (passers). The relationship becomes significant only inside a multivariate probit on a restricted sample. Result 3 states it as fact.

3. **The one supporting test conditions on a post-treatment variable.** `manuscript/results.tex:112`:
   > "Player~As who delegated in the \textit{Punishment} condition scored on average $2.47$ out of $10$ ... compared with $3.06$ for delegators in the \textit{No-Punishment} condition ($t$-test, $p=0.039$)."

   Delegation is the outcome the treatment moves. Comparing delegators across conditions compares two endogenously selected subsamples, and no p-value from such a comparison has a clean interpretation. The paper is entitled to describe the composition difference; it is not entitled to attach an inferential p to it without saying what the null is.

### M4. The Player B balance table exists, shows two imbalances at p < 0.05, and is suppressed with a justification that does not cover the comparisons the paper makes

`manuscript/appendix.tex:13`:

> "We do not separately report a balance table for Player~B. Player~B's punishment behavior is identified within-subject across the four (delegation, outcome) scenarios of the strategy method, so balance across conditions is not strictly required for the punishment analysis."

`tables/balance_player_b.tex:7-10` exists and is not `\input`:

| Variable | Punishment | No-Punishment | p |
|---|---|---|---|
| Age | 37.087 | 42.356 | **0.011** |
| Went to uni | 0.688 | 0.481 | **0.013** |

The stated justification is valid **only** for the within-condition, within-subject test. The paper repeatedly makes *between-condition* Player B comparisons that the justification does not cover:

- `manuscript/appendix.tex:78`: the entire hypothetical-punishment subsection compares No-Punishment Player Bs' stated punishment to the Punishment condition's realized punishment, and draws a directional conclusion ("Player~Bs state that they would punish a delegated decision more than a self-made one... $p=0.069$").
- `manuscript/results.tex:62` footnote: "Hypothetical punishment choices elicited from Player~Bs in the \textit{No-Punishment} condition corroborate this conclusion."

A five-year age gap and a 21-pp university-education gap between the two Player B pools are exactly the sort of thing that could drive a between-condition punishment difference. Withholding a table that exists, using a rationale that does not apply to the comparisons actually drawn, reads as suppression rather than economy.

### M5. Attention-check exclusion is differential by condition, and the appendix's promise to report both samples is not kept

`manuscript/appendix.tex:110`:

> "the preregistration left open whether participants who failed the attention checks would be excluded. **We present the analysis for both samples.**"

**(a) The exclusion is not balanced.** From `numbers.json`: Player A attention-check failures are 19/80 (23.8%) in Punishment vs 11/81 (13.6%) in No-Punishment — χ² p = 0.098 (my computation). Player B is balanced (13/80 vs 13/81, p = 0.97). The Player A passer subsample is therefore **no longer a randomized sample**, and it is precisely the subsample on which the belief-heterogeneity result (M2), the performance coefficient, and the passer-restricted Column (5) all live. This is never mentioned. It is also a substantive clue in its own right: differentially higher failure under Punishment is consistent with a cognitive-load account of the reversal (see M8).

**(b) The counts are never stated.** Nowhere does the compiled text say that 30 of 161 Player As and 26 of 161 Player Bs failed. A reader must reverse-engineer it from N rows and figure notes.

**(c) The promise is not kept where it matters.** Analyses whose passer/full-sample split is computed in `scripts/python/_outputs/attention_check_comparison.md` but reported one-sidedly:

| Analysis | Full sample | Passers | Which the paper reports |
|---|---|---|---|
| H1 Fisher exact | 0.041 | **0.054** | 0.041 only (`results.tex:23`) |
| Hypothetical-delegation McNemar | 0.090 | **0.197** | 0.090 only (`results.tex:10`) |
| Order effect within Punishment | 0.070 | 0.117 | neither |
| Belief diff, delegators vs non (good, no-del) | **0.016** | 0.006 | neither |
| Punishment regression interaction | 0.076 | 0.137 | 0.08 only (`results.tex:54`) |

The Fisher-exact row directly contradicts a claim in the text. `manuscript/results.tex:5`:

> "delegation shares are tested using Pearson Chi-squared tests, **with Fisher's exact tests yielding the same conclusions throughout**."

Among attention-check passers, Fisher's exact gives p = 0.054 — the opposite conclusion at the 5% threshold the paper itself adopts two sentences earlier. "Throughout" is not accurate.

### M6. Two elicited, incentivized measures are never analyzed — including the one that directly tests the paper's central identifying claim

**Risk preferences.** `manuscript/design.tex:78`:

> "Finally, we elicited risk preferences using an incentivized multiple price list in the style of \citet{holt_risk_2002}"

Risk preferences appear in **no** results table, **no** figure, **no** appendix, and **no** analysis script (`grep` across `scripts/python/*.py` returns only `10_payoffs.py`, which uses it to compute earnings). This is not a neutral omission: the closest precedent found risk aversion predicts delegation, as the author's own commented-out note records at `manuscript/results.tex:184`:

> `%    \item Are risk attitudes related to any decisions? ... [Comment: Result in Feier et al.: risk averse subjects were also more likely to delegate.]`

Risk attitude is also a live rival for the uncertainty-aversion mechanism the paper entertains at `manuscript/results.tex:133`. A referee will ask why an incentivized, theoretically-relevant covariate was collected and never used.

**Perceived relative ability.** `manuscript/design.tex:76`:

> "We also asked Player~A to estimate the distribution of scores in the population... Combined with her belief about her own score, **this locates where she places herself in the distribution and yields a measure of perceived ability relative to other participants.**"

This measure is constructed by design and then never reported. It matters because the paper's central defense of Result 3 rests on the claim that relative-ability beliefs are neutralized. `manuscript/results.tex:129`:

> "The pattern in the \textit{Punishment} condition must therefore reflect something other than beliefs about relative ability."

and the footnote defending it uses only *own* perceived performance:

> "under this alternative, delegation should decline with perceived own performance... In the data, perceived performance is statistically indistinguishable between delegators and non-delegators."

The paper argues about *relative* ability using an *absolute* ability measure while holding a purpose-built relative-ability measure it does not report. That is the single most answerable objection in the paper and it is left open.

### M7. Result 4 (effort) conditions on a post-treatment variable, rests on one binary draw per subject, and reports no test for its own headline measure

`manuscript/results.tex:142`:

> "\textit{The prospect of punishment does not induce additional effort. Non-delegators improve on their performance less in the \textit{Punishment} condition than in the \textit{No-Punishment} condition.}"

Four issues:

1. **The improvement measure is reported with no statistic at all.** `manuscript/results.tex:139`: "By this measure, non-delegators in the \textit{No-Punishment} condition improve, whereas non-delegators in the \textit{Punishment} condition do not." No means, no SEs, no test, no n. This is the sentence that names the Result.
2. **Post-treatment conditioning.** Non-delegators are 46/80 (57.5%) under Punishment and 33/81 (40.7%) under No-Punishment. These are differently selected groups *by construction of the treatment effect being studied*. The paper's footnote asserts the forces "offset" — "Non-delegators in the \textit{Punishment} condition are drawn from a slightly weaker pool but are more strongly positively selected within it, so the two forces offset" — with no evidence and no bounding exercise.
3. **Internal tension with Result 3.** Result 3 says better performers keep the decision under Punishment. That predicts Punishment non-delegators should do *better* on the final prediction. They do dramatically worse (21.7% vs 45.5%). The paper reads this as evidence against an effort motive; it is equally readable as evidence that Result 3's selection story is wrong, or that something about the Punishment condition degrades performance. Neither alternative is raised.
4. **The supporting p-value is omitted while the balance p-value is reported.** `manuscript/results.tex:139` reports "$3.12$ vs.\ $2.98$ correct predictions; $t$-test, $p=0.66$" for the *balance* check but gives no p for the 45.5% vs 21.7% comparison that carries the argument. It exists: `attention_check_comparison.md`, "p (success rate diff) = 0.031". Reporting the reassuring p and omitting the load-bearing one is a pattern a referee will notice, especially since the comparison is 21.7% vs 45.5% on **a single binary prediction per subject** with n = 46 and n = 33 — an enormously noisy basis for a numbered Result.

### M8. Two rival explanations for the reversal are never raised, one of which the paper's own data support

The mechanisms section (`manuscript/results.tex:68-149`) canvasses: departures from canonical settings, anticipated differential punishment, sample composition, performance-based selection, process ownership, outcome-uncertainty aversion, effort, and signaling. It is genuinely even-handed among these — and it does *not* over-commit to process ownership, which it explicitly demotes at `manuscript/results.tex:135` ("we cannot test either story and offer them only to show that activation by the prospect of punishment is conceivable"). That treatment is appropriate and I do not flag it.

What is missing are two rivals that require no new theory:

**(a) Differential cognitive load / instruction complexity.** The Punishment condition adds a punishment mechanism, a punishment-conditioning explanation, and a four-scenario belief elicitation. It is strictly longer and more complex. A load account predicts a shift toward the more effortful-seeming but cognitively default option, and predicts worse comprehension. **The paper's own data show exactly the predicted comprehension gap**: 23.8% attention-check failure under Punishment vs 13.6% under No-Punishment (M5). This rival is never named, and the one piece of evidence bearing on it is never reported.

**(b) Experimenter demand / salience of the recipient.** Telling Player A that Player B can punish her makes Player B's judgment salient in a way no other feature of the design does. The signaling discussion at `manuscript/results.tex:145-147` circles this without naming demand effects, and the paper offers no demand-mitigation evidence (no post-experimental guess-the-hypothesis item, no obfuscation of the manipulation). At `manuscript/results.tex:135` the paper concedes that its preferred readings work "only if the prospect of punishment activates" them — which is also precisely the structure of a demand explanation. A referee will read "activation by the prospect of punishment" as an unlabeled demand effect and say so.

---

## MINOR

### m1. Robustness checks are thin rather than padded — but the thinness is itself the finding

On rubric 2 (motivated vs theatrical), the compiled paper passes: every reported check maps to a stated threat. Column (2) of `tables/reg_delegation.tex` addresses composition, (3)–(4) address performance confounds, (5) addresses attention, the extensive-margin appendix addresses whether delegation shifts P(punish). None is padding.

The problem is the inverse. The checks that *would* be motivated by the sharpest threats — order (C3), power/equivalence (C1, C2), differential exclusion (M5), Player B balance (M4), risk and relative-ability controls (M6) — are the ones absent. A referee reading the robustness block will not think "padding"; they will think "the author checked the easy things."

### m2. Attrition is never quantified, despite a CONSORT script

`manuscript/results.tex:3` footnote: "Due to attrition and subsequent re-matching we recruited an extra pair in the \textit{No-Punishment} condition." No rate, no pattern, no breakdown by arm or role. `scripts/python/09_consort.py` exists and `numbers.json` carries `consort_*_completed` / `consort_*_attention_excluded` keys — but only *completed* counts, so the attrition denominator was apparently never assembled. A prior referee asked for this specifically (`referee_methods.md:86`: "differential attrition is the leading internal-validity threat after randomization itself"). For an online experiment at AER, a CONSORT flow diagram is close to mandatory.

### m3. Table-note inconsistency on significance stars

The two compiled tables carry stars (`tables/reg_delegation.tex:40`: "Significance: $^{*}\,p<0.10$..."; `tables/reg_belief_specs.tex:13-43`), while the two uncompiled robustness tables carry the opposite note (`tables/reg_delegation_robustness.tex:31`: "Following AEA editorial policy, significance stars are not reported in the table."). Whatever convention is chosen, the tables should agree. Flagging only the inconsistency, not the convention itself.

### m4. `tables/reg_delegation_robustness.tex` reports logit coefficients against a probit main table

`manuscript/results.tex:27` says "Table~\ref{tab:del_decision_determinants} reports Probit estimates" and `tables/reg_delegation.tex:40` confirms probit. But `tables/reg_delegation_robustness.tex:13` carries logit coefficients (−0.771, −0.677 — roughly 1.7× the probit values), and `scripts/python/17_logit_extended.py:23` uses `sm.Logit`. If that table is ever brought into the appendix, the coefficients will not be comparable to the main table. `quality_reports/logit_vs_probit_delegation.md` shows AMEs are near-identical across the two, so this is presentational, not substantive.

---

## Rubric 1 — the objections an AER/QJE referee will raise that the paper does not address

Ordered by how quickly a referee reaches them:

1. **What is the confidence interval on 16.8 pp?** There is not one CI anywhere in the manuscript. It is [1.6, 32.0].
2. **Was the study powered for its own headline?** MDE 21.5 pp > effect 16.8 pp; post-hoc power 58%. (C1)
3. **Is Result 2 a null or an equivalence?** CI admits 32% insulation; TOST fails at ±£0.10. (C2)
4. **Order effects.** 20 pp inside the Punishment condition, suppressed. (C3)
5. **Why does every mechanism result live on the attention-passer subsample, and why is that subsample differentially selected?** (M2, M5)
6. **Multiple testing across 34 p-values with two preregistered hypotheses.** (M1)
7. **Where is the treatment × performance interaction?** Result 3 and an introduction sentence rest on a cross-subsample significance comparison. (M3)
8. **Player B imbalance** on age (p = 0.011) and education (p = 0.013), with a suppressed table. (M4)
9. **Risk preferences and perceived relative ability** were elicited, are theoretically load-bearing, and are unreported. (M6)
10. **Attrition / CONSORT.** (m2)
11. **One binary decision per subject.** The entire paper rests on a single binary choice per Player A with no within-subject replication. Nothing in the design allows a subject-level check that the delegation choice is stable; the paper never discusses this design constraint.
12. **Demand effects and differential cognitive load.** (M8)
13. **Randomization inference.** With a binary outcome and n = 80 per arm at p = 0.031, a referee will want an exact or permutation p to confirm the result is not knife-edge on asymptotic approximation. A prior referee asked for this (`referee_methods.md:70`); it was not done.

---

## Rubric 7 — unreported analyses, stated neutrally

Analyses present in `scripts/` or `quality_reports/` with no counterpart in the compiled manuscript:

| Analysis | Location | Direction relative to headline |
|---|---|---|
| Ex-ante MDE, H1 and H2 | `tables/power_mde.tex` (never `\input`), `_outputs/power_calc.py` | Against — MDE exceeds the observed H1 effect |
| TOST equivalence, both bounds | `scripts/python/16_power.py`, `numbers.json` | Mixed — passes at ±£0.20, fails at ±£0.10 |
| Order effects | `scripts/python/12_order_effects.py`; drafted at `results.tex:167`, commented out | Against — effect concentrated in one order arm |
| Player B balance table | `tables/balance_player_b.tex` (never `\input`) | Against — two imbalances at p < 0.05 |
| Full/passer split for every headline test | `_outputs/attention_check_comparison.md` | Mixed — Fisher H1 p = 0.054 and McNemar p = 0.197 among passers |
| Belief-spec without attention exclusion | `tables/reg_delegation_robustness.tex` (never `\input`) | Against — good-outcome belief p = 0.125 |
| Punishment regression with Player B difficulty beliefs | `tables/reg_punishment_robustness.tex` (never `\input`) | Neutral — coefficients stable |
| Bad-cell difference regression | `quality_reports/punishment_bad_cell_diff.md` | Neutral |
| Logit vs probit comparison | `quality_reports/logit_vs_probit_delegation.md` | Neutral — AMEs near-identical |
| Punishment distribution diagnostics | `quality_reports/punishment_distributions.md`, 4 PNGs | Not assessed |
| Player B Likert × punishment correlations | `_outputs/attention_check_comparison.md` | Potentially supportive — "should humans be held responsible for AI decisions" × bad-cell insulation, r = 0.254, p = 0.066 |
| Belief levels, delegators vs non-delegators | `_outputs/attention_check_comparison.md` | Supportive — no-delegation/good-outcome belief differs, p = 0.016 full sample |
| Risk preferences (Holt–Laury) | elicited per `design.tex:78`; analyzed nowhere | Unknown |
| Perceived relative ability | constructed per `design.tex:76`; analyzed nowhere | Unknown |

The last two are the ones I would press hardest on. The Likert `responsibility` correlation (r = 0.254, p = 0.066) is the most theoretically on-point heterogeneity in the dataset — a direct measure of whether a punisher thinks humans should answer for algorithmic decisions, correlated with how much insulation they grant — and it appears only in an auto-generated diagnostic file.

---

## Top three

1. **C1 — the headline effect is below the study's own MDE, and neither the MDE nor a CI appears in the paper.** The calculation exists in the repo; a prior referee demanded it; it was not included.
2. **C2 — "Recipients punish delegated and self-made predictions alike" overstates a null whose CI admits a 32% insulation effect**, whose equivalence test fails at the tighter bound, and whose regression interaction is p = 0.08 in H2's predicted direction.
3. **C3 — a 20-pp order effect inside the Punishment condition was computed, drafted, and commented out**, leaving a footnote that implies the threat was checked and cleared.

**Score: 3 / 10.**
