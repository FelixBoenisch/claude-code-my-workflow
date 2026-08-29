# Lens 3 — Methods / Identification

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence* (Felix Bönisch, WZB Berlin)
**Files reviewed (compiled only):** `manuscript/abstract.tex`, `introduction.tex`, `literature.tex`, `design.tex`, `results.tex`, `conclusion.tex`, `appendix.tex`, plus every `tables/*.tex` reachable from them and `manuscript/prereg_aspredicted_133980.pdf`.
**Reviewer stance:** AER/QJE/JPE referee, experimental economics. Substantive correctness only.

**Verdict summary:** 6 CRITICAL, 11 MAJOR, 7 MINOR. The two headline results are computed correctly and the numbers in the text reconcile internally (I checked). The problems are (a) a suppressed balance failure on the Player B side, (b) a null result asserted as equivalence with no power analysis in a paper that *has* the MDE table sitting unused in `tables/`, (c) a misread regression coefficient, and (d) a set of mechanism claims that condition on post-treatment variables or are never tested at all.

---

## CRITICAL

### C1. A Player B balance table exists, shows two significant imbalances, and is suppressed with a justification that does not cover the comparisons the paper actually makes

`appendix.tex:13`:

> "We do not separately report a balance table for Player~B. Player~B's punishment behavior is identified within-subject across the four (delegation, outcome) scenarios of the strategy method, so balance across conditions is not strictly required for the punishment analysis."

But `tables/balance_player_b.tex` exists, is fully formatted, and reports:

| Variable | Punishment | No-Punishment | p |
|---|---|---|---|
| Age | 37.087 | 42.356 | **0.011** |
| Went to uni | 0.688 | 0.481 | **0.013** |

Two of six characteristics are imbalanced at the 5% level — a 5.3-year age gap and a 21-percentage-point education gap. Under successful randomization the probability of two or more of six independent tests rejecting at 5% is about 3.3%. Three problems follow.

1. **The stated justification is incomplete.** Balance is not required for the *within-subject* H2 comparison — correct. But the paper makes at least two *between-condition* Player B comparisons that do require it: `results.tex:62` fn ("Hypothetical punishment choices elicited from Player~Bs in the \textit{No-Punishment} condition corroborate this conclusion") and the whole of `appendix.tex:78`, which compares No-Punishment hypothetical punishment (£0.53 vs £0.43, p=0.069) against the Punishment-condition realized pattern. Those comparisons are contaminated by exactly the two imbalanced covariates, and age is a well-documented predictor of punishment behavior.
2. **The blanket claim in the body is not supported.** `results.tex:3`: *"Treatment randomization was effective, as demonstrated by the balance across observable characteristics (Appendix~\ref{appendix:sum_stats}, Table~\ref{tab:treatment_balance})."* `tab:treatment_balance` is the Player A table only. A referee who finds `balance_player_b.tex` in the replication package will read this as selective reporting.
3. **It raises a question about the randomization mechanism itself** (see M1). If A and B were assigned as pairs, an imbalance this large on the B side and none on the A side is odd and needs explanation.

**Fix:** print the Player B table, report the joint test for B as you do for A (`appendix.tex:11`), and either drop the cross-condition hypothetical-vs-realized comparisons or run them with age and education controls.

### C2. A null result is stated as equivalence with no power analysis anywhere — and the MDE table has been written and then dropped

The abstract (`abstract.tex`) asserts: *"Recipients punish delegated and self-made predictions alike."* The conclusion (`conclusion.tex:6`): *"Delegation, in turn, offers no protection against punishment."* Result 2 (`results.tex:51`) is correctly phrased as a failure to reject, but the abstract, intro and conclusion all convert it into an affirmative claim of no effect.

There is no power analysis, no MDE, and no equivalence test anywhere in the compiled paper. `results.tex:169` is a commented-out `\todo`. Meanwhile `tables/power_mde.tex` exists, is auto-generated, and its own note says:

> "$\delta_a = \pounds 0.20$ (the equivalence bound **used in Result~2 in the body of the paper**, equal to $10\%$ of the maximum punishment of $\pounds 2$)"

So an equivalence test was in the body at some point and has been removed, leaving the equivalence *language* without the equivalence *test*.

I reconstructed the relevant power figures from the reported statistics and they are unfavourable:

- **H2.** Reported bad-outcome difference £0.07, paired-t p=0.13, n=80 ⇒ t≈1.53 ⇒ SE≈£0.0457 ⇒ σ_d ≈ £0.409 ≈ 2δ_a. Row 3 of `power_mde.tex` then applies: **MDE = £0.125** at 80% power. The study cannot distinguish "no insulation" from a **£0.125 delegation discount, i.e. 23% of the £0.55 self-decided bad-outcome mean.** That is a large effect to leave undetectable, and it is roughly the size of effects reported in this literature.
- **H1.** `power_mde.tex` gives MDE = 21.5 pp at p₀=0.50. The realised effect is 16.8 pp. Power at the observed effect (p₀=0.593, p₁=0.425, n=80 per arm) is Φ(0.168/0.0779 − 1.96) ≈ **0.58**. A headline effect detected at 58% power carries a real Type-M exaggeration risk that the paper never acknowledges.

**Fix:** include `power_mde.tex`, restore the TOST against the £0.20 bound, and downgrade "punish alike" to "we can rule out a delegation discount larger than £0.125 (23% of the bad-outcome mean); smaller discounts are not detectable at this sample size."

### C3. The `Delegated × Bad outcome` coefficient is misread — it is a difference-in-differences, not the bad-outcome insulation effect

`results.tex:54`:

> "The \textit{Delegated}~$\times$~\textit{Bad outcome} interaction, **which captures any insulation from punishment after bad outcomes**, amounts to $-0.103$ and is weakly significant ($p=0.08$)."

This is wrong. In `tables/reg_punishment.tex` the model is an OLS on the stacked 4-cell design with main effects for `Delegated` and `Bad outcome`. The interaction is the *difference between* the delegation effect in bad outcomes and the delegation effect in good outcomes. I verified this against the cell means in `results.tex:48`:

- `Delegated` = 0.032 ≈ 0.33 − 0.30 (good-outcome delegation effect) ✓
- `Bad outcome` = 0.256 ≈ 0.55 − 0.30 (self-decided outcome effect) ✓
- `Delegated × Bad` = −0.103 ≈ (0.48 − 0.55) − (0.33 − 0.30) = −0.07 − 0.03 ✓

**The quantity H2 is about is the linear combination** `Delegated + Delegated×Bad` = 0.032 − 0.103 = **−0.071, which is exactly the paired-t estimate with p=0.13** — not p=0.08. The regression does not "confirm" a weakly significant insulation effect; it reports no such coefficient. The paper never tests the linear combination.

This matters twice over. First, `results.tex:54` presents a marginal p-value for the H2 estimand that the table does not contain. Second, it creates an **inference double standard**: p=0.08 here is read as suggestive support, while `appendix.tex:78`'s p=0.069 in the *opposite* direction (No-Punishment Player Bs would punish delegation *more*, £0.53 vs £0.43) is read as "corroborating" the same conclusion, and `results.tex:10`'s p=0.090 and `results.tex:139` fn's p=0.058 are treated as evidence. Two weakly significant effects with opposite signs cannot both corroborate "no delegation differential."

**Fix:** report the linear combination with its own SE, restate the sentence, and treat all marginal p-values symmetrically.

### C4. The manipulation confounds social accountability with Player A having a material stake in the outcome — the conclusion's headline interpretation is not licensed

`design.tex:96` claims the design "exploits the punishment manipulation as the only between-subject difference and holds fixed every other feature of the decision environment." Literally true at the level of instructions, but the punishment manipulation changes **two** things about Player A's problem simultaneously:

1. Player B can now form and act on a judgment of her (the social/accountability channel the paper wants);
2. **Player A's own payoff now depends on the realised outcome of the final prediction**, which in the No-Punishment condition it does not at all.

Every "activation" story the paper offers is stated in social terms — `results.tex:135` ("being punished for a decision one gave away may feel different"), `results.tex:147` ("the natural focus of any judgment he forms"), `conclusion.tex:10` ("what delegating may convey about the person who chooses it"). But a purely non-social mechanism fits the same data: once her own money rides on the outcome, a preference for control / ambiguity aversion over a machine's realisation becomes payoff-relevant where before it was free. Nothing in the design separates "Player B is judging me" from "I now have £2 riding on this."

The paper's own framing acknowledges the second channel exists and then never uses it: `design.tex:66` fn says incentives are aligned "As long as a better outcome for Player~B weakly reduces Player~A's expected punishment" — i.e. A's payoff *is* outcome-contingent under Punishment.

This is decisive for the conclusion: *"accountability disciplines algorithm use rather than fueling it"* (`conclusion.tex:10`) is one of two observationally equivalent readings. The separating condition is cheap to describe — a third arm where A's payoff is reduced by a stochastic, non-social, outcome-contingent deduction of the same expected magnitude — and its absence should be stated as a limitation rather than the interpretation asserted.

### C5. The central mechanism claim — that the performance/delegation relationship is stronger under punishment — is never tested

This claim appears three times and carries the whole "activation" argument:

- `results.tex:112`: "this relationship is considerably stronger in the \textit{Punishment} condition (Table~\ref{tab:reg_belief_specs}) than in the \textit{No-Punishment} condition (Figure~\ref{fig:performance_overview})"
- `results.tex:135`: "Consistent with such activation, the relationship between performance and delegation is markedly stronger under punishment than without it."
- `results.tex:149`: "It is the better-performing Player~As who retain the decision when punishment is possible"

The cited evidence is **a regression coefficient in one condition compared by eye to a figure in the other condition**. That is not a test. The relevant object is the `Punishment × Task performance` interaction in the pooled sample, and it appears in no table in the paper (`reg_delegation.tex`, `reg_delegation_full.tex`, `reg_delegation_robustness.tex`, `reg_belief_specs.tex` — none contains it).

Worse, the Punishment-side coefficient being cited (`reg_belief_specs.tex`, Cols 3–5, Task performance −0.362 to −0.381) comes from a **probit on N=60 with 9 regressors, restricted to attention-check passers**, while the No-Punishment side has no estimate at all. Comparing a subsample-restricted, heavily-conditioned coefficient in one arm to an unconditional picture in the other is not a like-for-like contrast even informally.

**Fix:** run the pooled interaction, report it, and let its p-value discipline the language. If it is insignificant — which at these sample sizes is likely — the "activation" narrative in `results.tex:135`, `results.tex:149` and `conclusion.tex:8` has to be softened considerably.

### C6. Results 3 and 4 condition on delegation, a post-treatment outcome

Both mechanism Results are built on comparisons *within* treatment-selected subgroups.

**Result 4 (`results.tex:142`)** — "The prospect of punishment does not induce additional effort. Non-delegators improve on their performance less in the \textit{Punishment} condition than in the \textit{No-Punishment} condition." — rests entirely on `results.tex:139`: 45.5% vs 21.7% high-payoff rates among non-delegators. Non-delegation is caused by the treatment (that is Result 1). Comparing non-delegators across conditions is a comparison of two differently-selected populations, and the paper says so itself in the very same paragraph's footnote:

> "Non-delegators in the \textit{Punishment} condition are drawn from a slightly weaker pool but are more strongly positively selected within it, so the two forces offset, whereas among delegators they compound."

That sentence is an assertion, not a test, and it is internally in tension with Result 3: if better performers select into non-delegation under Punishment, the Punishment non-delegator pool should be *better* on initial performance, not statistically identical (3.12 vs 2.98, p=0.66). Balance on the *observed* score does not deliver balance on unobserved effort propensity, which is precisely the variable in question. Result 4 is stated unconditionally and is not identified.

Note also that no test is reported for the 45.5% vs 21.7% comparison itself, despite it being the load-bearing number (n=33 and n=46; χ² p≈0.024 by my calculation — worth reporting rather than leaving to the reader).

**Result 3 (`results.tex:115`)** — "The additional delegation in the No-Punishment condition comes disproportionately from better performers" — is inferred from delegators' mean scores across conditions (2.47 vs 3.06, p=0.039), again a post-treatment subgroup. This one is *rescuable*, and I verified the fix: **under a monotonicity assumption** (punishment never *induces* delegation — no defiers), the No-Punishment delegator pool decomposes into always-delegators (share 0.425, mean 2.47, identified from the Punishment arm) and compliers (share 0.168). Solving

0.593 × 3.06 = 0.425 × 2.47 + 0.168 × m

gives **m ≈ 4.55** — the marginal delegators score 4.55/10 against an overall mean of ~2.9. That is a *stronger* and cleaner statement than the one the paper makes, but it requires monotonicity to be stated explicitly. Report it that way, or drop the causal phrasing.

**Fix:** restate Results 3 and 4 as descriptive facts about selected subsamples, add the monotonicity decomposition for Result 3, and for Result 4 acknowledge that the effort channel is unidentified because the design only observes final-prediction effort for non-delegators. (See M2 for the design change that would have fixed this.)

---

## MAJOR

### M1. The randomization procedure is described nowhere; `design.tex` has no sample, assignment, matching, or power subsection

`design.tex` runs 102 lines and never states: how many subjects, how many per condition, the unit of randomization (individual? pair? session?), the method (oTree `session.config`? separate Prolific listings?), the timing (were both roles randomized at entry, or was B assigned to match A's condition?), whether assignment was stratified or blocked, and how sample size was chosen. All sample information appears only in `results.tex:3`.

`results.tex:3` — *"Treatment randomization was effective, as demonstrated by the balance"* — substitutes a balance check for a description of the mechanism. A referee cannot verify that the analysis unit matches the randomization unit because the randomization unit is never stated. This matters concretely here: the delegation analysis is at the Player A level and the punishment analysis at the Player B level, but A and B are matched into pairs and (per `results.tex:3` fn) pairs were **re-matched** after attrition. The re-matching protocol is not described at all, and re-matching after the fact can break the assignment-to-analysis correspondence.

Relatedly, the paper contains **no attrition reporting**: no starts-vs-completes counts, no differential attrition test by condition, no CONSORT-style flow. The only mention is the single clause "Due to attrition and subsequent re-matching" (`results.tex:3` fn). For a top-5 experimental submission this is not sufficient.

### M2. "Equal performance" is communicated as a claim about the past, is calibrated off a different incentive regime, and applies to a single fixed final image

The individual-level calibration is the paper's best design idea (see Right #1), but three gaps sit between what was implemented and what the paper claims.

1. **Tense.** `design.tex:66`: "She was also told that, based on her first ten predictions, the algorithm **would have performed** equally well." That is a statement about the *past ten rounds*. What A needs for the delegation decision is a claim about the *next* prediction. `design.tex:70` then upgrades this to "making this performance parity common knowledge," and `results.tex:129` to "this equality of performance is common knowledge. The pattern in the \textit{Punishment} condition **must** therefore reflect something other than beliefs about relative ability." The "must" is doing more work than the instructions license. Note the instructions to B (`design.tex:82`) use the present tense — "an algorithm that **performs** as well as Player~A had performed in the earlier rounds" — so the two roles were told subtly different things.
2. **Incentive regime differs across phases.** Rounds 1–10 paid £4/£2 on one randomly selected round; the final prediction pays £5/£1 to B and, under Punishment, exposes A to £2 of punishment. Standard effort models predict higher effort on the final prediction, so the algorithm's calibrated probability is a *downward*-biased estimate of A's own next-round accuracy. The paper's own effort section (`results.tex:137`) recognises the mechanism but never notes that it undermines the parity claim.
3. **Single-image difficulty.** The final prediction is one fixed image (`results.tex:139`: "all Player~As faced the same images in the first ten rounds and on the final prediction"). The algorithm's p is A's *average* accuracy over ten different images; her own p is her accuracy on *that one*. Parity therefore requires image 11 to be of average difficulty — an unstated assumption. Pooled non-delegator success (≈31.6%, reconstructed from `results.tex:139`) versus the pooled initial rate (≈29.3%) is reassuringly close, but that comparison is itself on a selected sample, so it does not settle the question.

**Design suggestion worth stating:** having *every* Player A make the final prediction and *then* implementing either her prediction or the algorithm's draw would have (i) made parity verifiable, (ii) made effort observable for delegators too, fixing C6/Result 4, at the cost of nothing the paper needs.

### M3. The paper tells Player A (and Player B) that the final prediction is payoff-irrelevant for A — which is false in the Punishment condition

`design.tex:66`: "We informed Player~A that her final prediction would not affect her own payoff but would almost entirely determine Player~B's."
`design.tex:82` (instructions to B): "while Player~A's payoff **depended solely on her performance in the initial ten rounds**."

Both statements are true in No-Punishment and false in Punishment, where B conditions punishment on the outcome and therefore A's payoff *does* depend on the final prediction. Either (a) the manuscript is mis-describing condition-specific instructions as if they were common, or (b) subjects were actually told something inaccurate. Either way it needs fixing, because it bears directly on the "no self-serving motive / incentives aligned" argument at `design.tex:64` and `design.tex:66` fn, and on C4.

### M4. The claim that the belief elicitation could not be incentivized is contradicted by the design's own strategy method

`design.tex:74` gives three reasons for not incentivizing punishment beliefs. The first is factually wrong given the design:

> "First, only two of the four scenarios remain payoff-relevant after the delegation decision, making the others purely hypothetical."

But Player B's punishment is elicited by the strategy method **for all four cells** (`design.tex:84`). Every one of A's four beliefs is therefore *verifiable against a real, recorded decision by her matched B*. Payoff-relevance for B is irrelevant to whether A's belief about B's stated choice can be scored. A binarized scoring rule (Hossain–Okui) on one randomly drawn cell would have been both incentive-compatible and simpler than the 11-bin own-performance elicitation the paper *did* run on the very next screen — which also undercuts reason three ("would have substantially increased task complexity").

This matters because the unincentivized, post-decision beliefs are the sole evidence for Result 3 (`results.tex:107`) and thereby for ruling out the most natural mechanism. `results.tex:104` and `conclusion.tex:8` both flag the limitation honestly, but the justification for creating it does not hold up.

### M5. Attention-check exclusion is post-treatment, its pass rate is never reported by condition, and the belief result exists only in the excluded sample

The headline belief-heterogeneity finding is null in the full sample and significant only among passers:

`tables/reg_belief_specs.tex`: full Punishment sample AME = 1.3 pp (p=0.388) and 1.4 pp (p=0.370); passers-only AME = 4.7 pp (p=0.011) and 5.5 pp (p=0.006). `results.tex:104` describes this as "the relationship **sharpens**," which reads as a gradual strengthening rather than what it is — a sign-preserving but null-to-significant flip on dropping 25% of the sample.

Three problems:

1. **The exclusion is post-treatment.** Player A's attention check sits on the belief-elicitation screen, i.e. after the delegation decision and after treatment exposure. `results.tex:29` fn even notes it "may still correlate with who took the delegation decision seriously" — which is the definition of a bad conditioning variable.
2. **Pass rates by condition are never reported.** Reconstructing from `reg_delegation.tex` (passers N=130 of 159) and `reg_belief_specs.tex` (Punishment passers N=60 of 78), the pass rate is roughly **77% in Punishment vs 86% in No-Punishment** — a 9.5 pp gap (two-proportion z ≈ 1.55, p ≈ 0.12 by my calculation). Not significant, but not negligible either, and it is exactly the check a referee will ask for before accepting a passers-only result.
3. **The prereg left it open.** `appendix.tex:110` states this accurately ("the preregistration left open whether participants who failed the attention checks would be excluded"), consistent with the prereg's "I **may** exclude participants that failed the attention checks." That honesty is good — but it means the passers restriction is a researcher-degrees-of-freedom choice, and the result that depends on it should be labelled exploratory rather than "sharpened."

### M6. Multiple hypothesis testing is never addressed

Two preregistered comparisons, then roughly fifteen further tests in the mechanism section, several landing at 0.03–0.09 and all interpreted as evidence: p=0.033 (H1), p=0.090 (McNemar), p=0.011/0.006 (belief AMEs), p=0.039 (delegator scores), p=0.068 (task performance), p=0.019 and p=0.058 (screen times), p=0.069 (hypothetical punishment), p=0.08 (interaction), p=0.024 (unreported, outcome rates). No correction, no family definition, no mention of the issue anywhere in the compiled text. At minimum the mechanism section needs an explicit "these are exploratory and unadjusted" statement and preferably a Romano–Wolf or sharpened-q adjustment for the main exploratory family.

### M7. The `results.tex` claim about task performance contradicts itself between §Result 1 and §Mechanisms

`results.tex:29`:
> "**Neither actual nor perceived performance is significantly associated with delegation in the pooled sample**, although actual performance enters negatively and is weakly significant under the attention restriction ($p=0.068$)."

`results.tex:112`:
> "**Task performance is negatively associated with the decision to delegate across conditions** (Table~\ref{tab:del_decision_determinants}, Column~(5))."

These assert opposite things about the same relationship, 80 lines apart. Line 112 cites Column (5) — the passers-only column at p=0.068 — while the full-sample Column (3) coefficient is −0.119 (SE 0.079, t=1.51, p≈0.13). A referee will read line 112 as citing the column that says what the mechanism section needs. Pick one characterisation and use it in both places.

### M8. Punishment is costly only on the extensive margin, which changes what the primary outcome measures

`design.tex:84`:
> "Player~B could choose to reduce Player~A's payoff by up to $\pounds 2$ in $\pounds 0.10$ increments... Imposing strictly positive punishment required Player~B to forgo $\pounds 0.10$ of his own earnings, ensuring that punishment was costly to the punisher."

This is a **flat entry fee**, not a price. Once B pays £0.10, the marginal cost of raising punishment from £0.10 to £2.00 is **zero**. Implications the paper never discusses:

- "Costly punishment" is accurate only for the decision to punish at all. The intensity choice is uncosted and therefore not a revealed-preference measure in the sense the literature (Fehr–Gächter, Bartling–Fischbacher, all of which use proportional 1:k technologies) assumes.
- The primary H2 outcome — mean punishment in £ — mixes one costly binary decision with a costless intensity choice, which inflates σ_d and directly worsens the power problem in C2.
- A material-payoff-maximising spiteful B should choose £2 conditional on entry. Observed means are £0.30–£0.55 with 55% punishing at all (`results.tex:60`), so intensity is being driven by something other than the incentive structure — which is fine, but it needs saying, especially since the paper's own comparability argument to Bartling & Fischbacher and Coffman rests on the punishment technologies being alike.
- It is also never stated whether **Player A was told that punishment is costly to B**. This matters for Figure `fig:realized_vs_anticipated`, where A substantially overestimates punishment in every scenario — an obvious candidate explanation is that A did not know B had to pay to punish.

### M9. The randomized option-order manipulation is under-reported, and the suppressed numbers are material

`design.tex:72`: "The two delegation options (own decision / algorithm) appeared in **random order** across subjects." This is a second randomized factor, and the compiled paper reports only a footnote (`results.tex:29`) saying the treatment coefficient survives an order control.

The commented-out text at `results.tex:167` contains what a referee would want:

> "presenting the algorithm option first roughly doubles delegation ($52.5\%$ vs $32.5\%$ when the own-decision option is first; $\chi^2$ $p=0.070$), while the \textit{No-Punishment} condition shows no order effect ($p=0.674$); the treatment $\times$ order interaction is not significant ($p=0.115$)"

Taken at face value, the treatment effect is ≈6.8 pp in the algorithm-first arm (52.5 vs 59.3) and ≈26.8 pp in the own-first arm (32.5 vs 59.3). The interaction is insignificant at n=40 per cell — as it must be — but "not significant at p=0.115" is not the same as "not there," and the pattern means the headline effect may be concentrated in one arm of a second randomization. This belongs in the appendix with the numbers, not in a commented block. Omitting it while retaining the reassuring footnote is the kind of asymmetry referees penalise heavily.

### M10. Strategy-method elicitation is never validated or caveated, yet the null in Result 2 depends on it

Every punishment number in the paper is a cold, contingent strategy-method choice; only one of the four cells is implemented per Player B (`design.tex:84`). The paper never mentions the strategy-method/direct-response distinction, never cites the evidence that the strategy method attenuates punishment (Brandts & Charness 2011 is the standard reference), and never notes that attenuation biases *toward* the null it reports.

Combined with C2's MDE of £0.125, this compounds: Result 2 may be a null because the elicitation is cold, because the sample is small, or because there is genuinely no effect, and the paper cannot distinguish these. The prereg does specify the strategy method, so this is a caveat to state rather than a deviation — but it must be stated, because it is the main threat to the paper's second headline claim.

`design.tex:102` also overstates what the method delivers: "Hypothesis~2 is identified by the within-subject comparison across the four (delegation, outcome) scenarios of Player~B's strategy-method punishment, **which isolates the effect of delegation on punishment**." It isolates the effect of delegation on *stated contingent* punishment. That is a different estimand and the sentence should say so.

### M11. Elicitations described and motivated in `design.tex` never appear in `results.tex`

Design-to-analysis alignment gaps, all in `design.tex`:

- **Population score distribution / relative-ability measure** (`design.tex:76`): motivated at length — "Combined with her belief about her own score, this locates where she places herself in the distribution and yields a measure of perceived ability relative to other participants" — and then never used anywhere in `results.tex` or the appendix. This is odd given that the entire relative-ability argument (`design.tex:70`, `results.tex:129`) is the paper's identification claim, and this variable is the direct test of whether subjects internalised the parity claim (see also M12).
- **Risk preferences, both roles** (`design.tex:78`, `design.tex:84`): incentivized Holt–Laury lists for A and B, analysed nowhere. The author's own commented note at `results.tex:184` records that Feier et al. found risk-averse subjects delegate more — so the analysis was contemplated and dropped.
- Player B's task-difficulty perception *is* used (`reg_punishment.tex`, "Player B belief about Player A perf."), and technology affinity *is* used, so the gap is specific to the two items above.

A referee reads a described-but-unanalysed incentivized elicitation as a dropped null. Either report them (a line each in an appendix table suffices) or delete them from `design.tex`.

---

## MINOR

### m1. Circularity in the footnote defending the parity assumption
`results.tex:129` fn: "under this alternative, delegation should decline with **perceived** own performance... In the data, perceived performance is statistically indistinguishable between delegators and non-delegators." But `design.tex:76` states that perceived performance was elicited *after* A was told the algorithm performs equally well, and `results.tex:110` fn concedes "This overconfidence may partly reflect the information that the algorithm performs equally well." Using a post-information belief to test whether the information was internalised is circular. The population-distribution measure (M11) would be the non-circular test, if it is contaminated less.

### m2. Stated SE method contradicts the tables
`results.tex:5`: "Regressions report robust (HC1) standard errors." But `reg_punishment.tex` and `reg_punishment_extensive.tex` both note "Standard errors clustered at the Player~B level" — which is the correct choice and should be what the text says.

### m3. HC1 at N=60
`reg_belief_specs.tex` Cols (3)–(5) use HC1 on N=60 with 9 regressors (pseudo-R²=0.25). HC1 under-covers badly in samples this small; HC3 or a wild bootstrap would be the defensible choice for the paper's most-cited exploratory coefficient.

### m4. The McNemar "weakly significant" claim depends on the least conservative variant
`results.tex:10` fn reports the No-Punishment hypothetical-switching test as "within-subject McNemar's test $p=0.090$". With 12 and 5 discordant pairs, I get: uncorrected χ² = 49/17 = 2.882 → **p = 0.0896** ✓ (matches); continuity-corrected = 36/17 = 2.118 → **p = 0.146**; exact binomial 2·P(X≥12 | n=17, p=0.5) = 2 × 9402/131072 → **p = 0.144**. So the "weakly significant" label survives only under the uncorrected asymptotic version, at n=17 discordant pairs where the asymptotic approximation is least trustworthy. Given that this is offered as the within-subject corroboration of the headline result, report the exact test.

### m5. Feier et al.'s calibration is described two different ways
`design.tex:70`: "under the **session-level** calibration of \citet{feier_hiding_2022}". `results.tex:129`: "the algorithm's performance distribution is matched to the distribution of human performance at the **population level**." These are different claims about the design feature the paper's entire contribution is defined against. Pick one and verify it.

### m6. The population-share incentive may not be implementable as described
`design.tex:76`: "One score was drawn at random at the end of the experiment, and Player~A earned $\pounds 0.30$ if her estimate for it fell within five percentage points of **the realized population share**." The population is undefined (the 161 Player As? the session?), and `design.tex:86` says "we... paid all participants **on the day of participation**" — so for early participants the population share did not yet exist. Clarify how this was resolved.

### m7. Over-reading the 50% delegation rate
`results.tex:10`: "Delegation shares around $50\%$ are consistent with subjects, on average, finding the claim of equal relative performance credible. Their behavior reflects neither systematic preference for one's own prediction nor systematic deference to the algorithm." A ~50% aggregate share is equally consistent with indifference, with random choice, and with heterogeneous strong preferences that cancel. It is weak evidence for the credibility claim, which the paper elsewhere leans on heavily (`design.tex:70`, `results.tex:129`).

### m8. Missing standard front-matter for an experimental submission
No IRB/ethics approval statement, no instructions or screenshots appendix (the appendix contains only tables, figures and the prereg PDF), no data/code availability statement. AER requires the first and effectively requires the second for experimental work. `design.tex:62` fn covers image consent, which is good, but is not an ethics approval statement.

---

## What the paper gets right

1. **The individual-level algorithm calibration is a genuine methodological advance, and the "no feedback between rounds" choice makes it work.** Fixing the algorithm's success probability to each subject's own accuracy (`design.tex:68`) neutralises relative-ability beliefs subject-by-subject rather than on average, and because "No feedback was provided between rounds" (`design.tex:62`), Player A cannot back out the algorithm's realised probability and behave strategically against it. The reasoning at `design.tex:70` for why this matters — that relative-ability beliefs would otherwise dominate the delegation decision and mask the motive of interest — is correct and well argued. This is the paper's strongest design idea and it is properly motivated.

2. **The within-subject strategy method for H2, with correctly clustered standard errors.** Eliciting punishment for all four (delegation, outcome) cells means H2 is estimated free of between-subject heterogeneity in punishment proclivity, and `reg_punishment.tex` clusters at the Player B level over the 4 stacked observations per subject — the right choice, and one that many papers get wrong. The complementary extensive-margin probit (`appendix.tex:17`) is the right robustness check for a censored-at-zero outcome with 45% zeros.

3. **The preregistration-deviation appendix is honest and the statistical reasoning in it is correct.** `appendix.tex:110` discloses all three deviations, and the argument for replacing the preregistered Mann–Whitney/Kolmogorov–Smirnov tests is exactly right: "Both are tests for independent samples, whereas punishment is elicited within-subject via the strategy method." Substituting the Wilcoxon signed-rank test is the correct fix, not a convenient one, and the paper reports both parametric and non-parametric results throughout even where they disagree (e.g. `results.tex:48`, t p=0.13 vs Wilcoxon p=0.54). The same honesty appears at `design.tex:76` fn, which volunteers that its own scoring rule "is not proper," and at `results.tex:104`, which volunteers the two main weaknesses of the belief measure.

4. **The reported numbers reconcile.** I checked the subgroup means against the aggregates and they are internally exact: Punishment (34 delegators at 2.47, 46 non-delegators at 2.98) → 2.76 ✓; No-Punishment (48 at 3.06, 33 at 3.12) → 3.09 ✓. The regression cell decomposition in `reg_punishment.tex` reproduces the raw cell means in `results.tex:48` to the reported precision ✓. Whatever else is wrong, the arithmetic is not.

---

## Score

**5 / 10.**

The design has one genuinely good idea (individual-level calibration) and the analysis is arithmetically sound, but the identification claims outrun the design in four places that a top-five referee will find on the first read: a suppressed balance failure, an equivalence claim with no power analysis in a paper that already generated the MDE table, a misread interaction coefficient underpinning the H2 discussion, and a headline interpretation ("accountability disciplines algorithm use") that the manipulation cannot separate from a plain own-stake effect. The mechanism section, which is where the paper spends most of its pages, rests on comparisons within post-treatment subgroups and on one central claim that is never tested at all. Most of this is fixable with re-analysis of existing data and more careful language rather than new data collection — C1, C3, C5 and M9 in particular are a day's work — which is why the score is 5 and not lower.
