# Lens 3 — Methods / identification

**Review updated:** 2026-09-07

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence*

**Snapshot:** current working-tree manuscript, including uncommitted edits, on HEAD `d4f48b6`; supersedes the 2026-08-21 review.

**Verdict:** REVISE-MAJOR — **0 CRITICAL, 8 MAJOR, 8 MINOR; 6/10.**

The revised manuscript more clearly separates the two hypotheses, acknowledges that the performance gradients do not differ significantly across treatments, and treats the mechanism as unresolved. The two-person exclusion changes the main delegation difference from 16.8 to 18.3 percentage points; the negative treatment difference remains significant with either sample. The remaining problems concern what the design identifies, the strength of the punishment-null interpretation, selected-sample effort comparisons, and insufficient documentation of assignment and analysis choices. They do not establish that the main treatment comparison is invalid.

## Scope and verification

I reread the active source in `manuscript/design.tex`, `results.tex`, `appendix.tex`, `abstract.tex`, `conclusion.tex`, and the input structure in `main.tex`; inspected the relevant generated tables, current Python sources, and `scripts/python/_outputs/numbers.json`; and read the preregistration text extracted from the same embedded PDF in `quality_reports/bibliography_audit_2026-09-05/build/main.txt:1576` onward. That earlier PDF extraction is used only for the preregistration, not as the current manuscript.

For this update I also ran **fresh, read-only calculations** with `paper/.venv/Scripts/python.exe -B`, reading `data/clean/delegator_cleaned.xlsx` and `evaluator_cleaned.xlsx` directly. These checked sample counts, H1 with/without the two exclusions, H2 paired effects/confidence intervals/TOST/MDE, attention pass rates, order heterogeneity, the pooled performance coefficient, and performance interactions. These are checks of cleaned data, **not** a fresh reconstruction from raw experimental records or a run of the full generating pipeline. No manuscript, data, tables, figures, or manifest was changed.

All source locations below are relative to `paper/`. Commented LaTeX and unreferenced tables are not treated as findings reported to readers. In particular, `results.tex:174` and `:176` contain commented order/power material; the interaction p-values at `results.tex:109` are in a commented footnote, although the active sentence now acknowledges nonsignificance.

The old report also overstated several concerns. Covariate imbalance alone is not evidence of failed randomization or intentional suppression; a minimum detectable effect is not a confidence bound; and strategy-method elicitation does not mechanically imply attenuation toward zero. Those claims are withdrawn below. The old headline said seven minor findings, but its body contained **eight**.

## MAJOR findings

### L3-M1. The punishment null still becomes a claim of no protection

**Evidence:** `results.tex:49` says Player B punishes the choices “no differently”; `:57` says Player A “cannot escape punishment” and “pays no punishment premium.” `abstract.tex:2` says “Delegation, in turn, offers no protection.” `conclusion.tex:6` says recipients punish the choices “alike.” Result 2 itself (`results.tex:52`) correctly says “does not punish … significantly less.”

Fresh calculations for the **full Punishment sample, n=80**, with difference defined as delegated minus own punishment, give:

| Comparison | Mean difference | 95% paired-t CI | Two-sided p |
|---|---:|---:|---:|
| Bad outcome | −£0.07125 | [−£0.16414, £0.02164] | 0.13081 |
| Good outcome | £0.03188 | [−£0.06988, £0.13363] | 0.53474 |

Thus the bad-outcome data remain compatible with a discount of about £0.16, approximately 30% of the own-decision bad-outcome mean. An exploratory TOST supports equivalence at **±£0.20** (p=0.00360), but not at **±£0.10** (p=0.26981). A meaningful equivalence margin requires substantive justification; it must not be presented as preregistered merely because a legacy table mentions it.

**Revision:** report the effect and interval beside Result 2 and use “no statistically detectable reduction” consistently. If equivalence is retained, state the justified margin and its exploratory status. Do not reuse the former review's assertion that a £0.125 MDE “rules out” discounts above that amount. The freshly calculated full-sample paired MDE is about **£0.132** at 80% power; it answers a different question from the confidence interval. Existing generic `h2_*` manifest entries often describe the **67 attention passers**, not the full-sample headline.

### L3-M2. The appendix still connects the interaction coefficient to the wrong H2 estimand

**Evidence:** `design.tex:109` defines H2 conditional on a low-payoff outcome. `appendix.tex:17` correctly says the interaction measures how the delegation difference changes after a bad outcome, then adds “and thus any insulation from punishment after bad outcomes” and foregrounds −0.103, p=0.077. `tables/reg_punishment.tex:13` and `:17` report Delegated and Delegated × Bad outcome. The same interpretation remains in the source docstring, `scripts/python/06_logit_punishment.py:6`.

For the reported specification,

```
H2 bad-outcome effect = beta_Delegated + beta_Delegated×Bad
                     ≈ 0.032 − 0.103 = −£0.071.
```

The interaction alone is a difference between the bad- and good-outcome delegation effects. Its p-value is not the p-value for H2. Moving the passage from the main text to the appendix has not fully corrected this.

**Revision:** report the linear combination with its own clustered uncertainty, or parameterize the model with bad outcomes as the reference category. Keep the interaction as a secondary comparison across outcome states. The paired test already measures the relevant bad-outcome contrast; its p=0.13081 should not be replaced with the interaction's p=0.077.

### L3-M3. Result 5 still treats an endogenous subgroup comparison as an effort effect

**Evidence:** `results.tex:146` states “The prospect of punishment does not induce additional effort.” The actual evidence at `:143` compares only non-delegators. `design.tex:75` says delegators skip the final-prediction screen, and `scripts/python/08_mechanism_effort.py:28` explicitly restricts to `delegation == 0`.

Punishment changes delegation, so non-delegators in the two arms are treatment-selected groups. Similar initial errors (p=0.857) or nonsignificantly different initial scores (p=0.316) do not make those groups exchangeable in latent motivation, effort responsiveness, or final-image ability. Comparing each subject's final error with initial error does not remove that selection. Holding images fixed addresses image differences across arms, not this problem.

The new error-improvement statistics and explicit proxy caveat are useful, but the caveat discusses measurement error and pressure; it does not acknowledge the selected-sample estimand. The categorical Result 5 conflicts even with the active statement that the channel cannot be ruled out conclusively.

**Revision:** state the finding descriptively: among those who chose to retain the prediction, performance improved less under punishment. Explain that the design observes neither final-prediction effort nor its treatment effect for all Player As. Carry that limit into the signaling and concluding discussion. Current Result 4 (“Better-performing Player As are less likely to delegate,” `:113`) is already a more defensible descriptive statement; no monotonicity decomposition is necessary unless making claims about the identities of marginal delegators.

### L3-M4. Punishment changes material exposure as well as social judgment, and the payoff description remains misleading

**Evidence:** `design.tex:67` says the final prediction “would not affect her own payoff”; `:85` says A's payoff “depended solely on her performance in the initial ten rounds.” Yet `:73` makes punishment contingent on delegation and the realized outcome, and `results.tex:65` repeats “Neither option affects Player A's own monetary payoff.”

These descriptions can apply to **pre-punishment earnings**, but not generally to final earnings. Punishment introduces both exposure to a recipient's judgment and possible outcome-dependent losses. Accordingly, random assignment identifies the total effect of introducing this punishment regime, not a separate social-judgment mechanism.

The new discussion explicitly allows that relinquishing control becomes troubling when the outcome has indirect consequences for A (`results.tex:132`) and calls the mechanism unresolved (`:155`), a material improvement. Nevertheless, `conclusion.tex:11` attributes the determinant to “what delegating may convey about the person who chooses it.” That specific channel is not isolated.

**Revision:** distinguish base pay from punishment-adjusted pay throughout; describe the identified effect as the effect of the punishment opportunity. State that its monetary and social components are not separated. A new treatment is not needed to report the current total effect; it would be needed to identify these components separately. This is an interpretation limit, not evidence that H1's estimate is confounded by a preexisting treatment-group difference.

### L3-M5. Past-performance calibration does not establish equality of final-prediction success probabilities or beliefs

**Evidence:** `design.tex:69` accurately specifies a Bernoulli draw calibrated to initial empirical accuracy. `:71` upgrades this to “neutralizes this motive” and common-knowledge parity. `results.tex:127` states “performance is equalized between the algorithm and each individual subject” and uses this to interpret away beliefs about relative ability. `results.tex:140` itself permits greater effort on the final prediction to outperform the algorithm.

The implemented equality is between the algorithm's success probability and **observed accuracy over ten earlier images**. Extending it to a subject's prospective success on the single final image requires assumptions about learning, effort, image difficulty and subjects' understanding. Likewise, common knowledge of the calibration statement does not prove that subjects believe their own next prediction has that same probability. A finite historical accuracy rate is also a noisy measure of underlying ability.

The aggregate delegation shares are not a validation test: `results.tex:10` infers credibility and lack of systematic preferences from shares “around 50%,” although opposing individual preferences could yield the same aggregate.

**Revision:** consistently describe equality with measured initial accuracy and identify prospective parity as an assumption. Treat calibration as a design feature intended to reduce relative-performance concerns, with remaining belief/effort channels explicitly open. Withdraw the behavioral “validation” based on aggregate choice shares. Any use of perceived initial score as a probability of final success should state the corresponding extrapolation.

### L3-M6. Assignment, pilot inclusion, attrition and the new exclusion need an integrated sample account

**Evidence:** `design.tex:67` describes random pairing, but `:102` gives a causal identification claim without specifying the treatment-assignment unit or mechanism. `results.tex:3` gives 322 recruits, re-matching after attrition, and the exclusion of two No-Punishment Player As. `appendix.tex:114` dates preregistration after the pilot; `:116` folds the zero-prediction exclusion into its first deviation. The preregistration's Q6 permits attention exclusions but does not specify this zero-prediction rule; Q8 says a pilot with 25 Punishment observations had already been run and was planned for inclusion (`quality_reports/bibliography_audit_2026-09-05/build/main.txt:1608` onward).

**Fresh checks:** the two excluded participants are both No-Punishment non-delegators and both attention passers. With the exclusion H1 is 34/80 versus 48/79 (χ² p=0.02125; Fisher p=0.02644); without it H1 is 34/80 versus 48/81 (χ² p=0.03343; Fisher p=0.04073). The conclusion therefore survives. However, the pooled background-adjusted performance coefficient moves from −0.1191 (n=159, p=0.13059) to −0.1598 (n=157, p=0.04741), changing the significance of the descriptive mechanism finding.

**Revision:** give assignment unit, timing, procedure, role allocation, matching/re-matching rules, and starts/completions/exclusions by arm and role. Explicitly distinguish pre-preregistration pilot observations from later observations and explain which enter each analysis. Label the new zero-prediction rule as an additional analysis decision, explain when it was chosen, and show the unrestricted sensitivity for H1 and performance selection. Its objective rationale is credible; its observed effect on a secondary finding should nevertheless be transparent. The current sources do not establish that attrition or exclusion biased H1, nor do balance tests establish that assignment was valid.

### L3-M7. Belief findings remain sensitive to post-decision measurement and attention selection

**Evidence:** `design.tex:77` places punishment-belief elicitation and its attention check after delegation. `results.tex:97` now correctly says differential punishment “does not predict delegation in the full sample” before emphasizing passers; `:100` acknowledges unincentivized reports and post-hoc rationalization. `tables/reg_belief_specs.tex:38`–`:46` gives AMEs of 1.3–1.4 pp in the full sample (p=0.388/0.370) versus 4.7–5.5 pp among passers (p=0.011/0.006, n=60).

The caveats and exploratory label are improvements. However, later summaries again say those expecting a larger penalty are more likely to delegate without preserving the passers restriction (`results.tex:155`). Passing a check after treatment and delegation is not a baseline characteristic. Fresh counts are **61/80 (76.3%)** versus **68/79 (86.1%)** for A (χ² p=0.11334); complete-case regression Ns are smaller, so table Ns must not be used as attention-pass denominators.

A near-zero average reported penalty also does not establish zero aggregate behavioral effect when beliefs, responsiveness, success probabilities and choice thresholds differ across subjects. The asymmetry footnote at `results.tex:100` is a useful diagnostic, not identification of that counterfactual.

**Revision:** retain “among attention-check passers” in every summary, report the pass rates and sample flow, and interpret the association as exploratory and noncausal. Frame the mean-belief finding as lack of positive evidence for an aggregate penalty, not exclusion of anticipated punishment as a mechanism. The first unincentivized-elicitation rationale in `design.tex:77` should also be qualified: all four contingent B choices are recorded (`:87`), so counterfactual cells are in principle scoreable; hedging and complexity are design tradeoffs, not impossibility.

### L3-M8. The randomized option-order results remain absent and have changed with the sample

**Evidence:** `design.tex:73` reports randomized option order. The old reassuring order-control footnote at `results.tex:28` and the detailed discussion at `:174` are now comments, not manuscript evidence. `scripts/python/12_order_effects.py:21`–`:44` computes the relevant comparisons.

Fresh current-sample results are:

| Option displayed first | Punishment delegation | No-Punishment delegation | Punishment minus No-Punishment |
|---|---:|---:|---:|
| Own decision | 13/40 = 32.5% | 27/42 = 64.3% | −31.8 pp |
| Algorithm | 21/40 = 52.5% | 21/37 = 56.8% | −4.3 pp |

The specified robust Logit treatment × order coefficient is 1.1468, p=0.07962; the former p=0.115 is stale. This exploratory interaction does not establish order-specific treatment effects, but the visible concentration is relevant to how general the pooled H1 estimate is.

**Revision:** report the four cells and interaction estimate/uncertainty in the appendix, clearly marked exploratory. Give the pooled treatment effect with order adjustment and avoid equating an imprecise interaction with absence of heterogeneity. Randomized order does not by itself invalidate the pooled effect.

## MINOR findings

### L3-m1. The general standard-error statement omits clustering

`results.tex:5`: “Regressions report robust (HC1) standard errors.” The punishment table instead correctly uses Player-B-clustered errors (`tables/reg_punishment.tex:43`; also the extensive-margin table). Specify HC1 for individual-level Probit analyses and clustering for stacked B analyses. The old claim that HC1 necessarily “under-covers badly” at n=60 was unsupported; sample size alone does not demonstrate this. Small-sample stability checks for the exploratory belief association may be useful without treating an unrun check as a demonstrated failure.

### L3-m2. The hypothetical-switching significance label depends on an asymptotic McNemar test

`results.tex:10` reports 12 versus 5 discordant pairs and p=0.090, calling the shift weakly significant. A fresh exact binomial McNemar calculation gives **p=0.14346**. Report the exact test and call the pattern directionally consistent rather than statistically corroborating at 10%. This does not affect between-condition H1.

### L3-m3. Exploratory status is now explicit, but multiplicity is not

`results.tex:5` now correctly labels Results 3–5 exploratory. It does not state whether their p-values are adjusted, define inferential families, or qualify the accumulation of marginal tests. State that exploratory p-values are unadjusted and avoid treating the number of nominally significant checks as cumulative confirmation. A declared family and adjusted results would be useful if these tests remain central; correction is not automatically required for every descriptive diagnostic.

### L3-m4. State the scope of the punishment measure more explicitly

`design.tex:87` describes contingent strategy-method choices and a **flat £0.10 cost of any positive punishment**. Thus mean punishment combines a costly participation decision with intensity choices having no additional monetary marginal cost. The extensive-margin analysis is already included, and `design.tex:73` now explicitly says A learned punishment was costly.

In `design.tex:125` qualify the estimand as punishment elicited contingently using this strategy method and technology. Do not generalize without qualification to spontaneous punishment after a personally experienced outcome or to proportional-cost punishment systems. The earlier report's assertions that the strategy method must attenuate the delegation effect, or that the flat fee necessarily inflates its variance, were not established and are withdrawn.

### L3-m5. Ancillary elicitations and the population-share payment benchmark need closure

`design.tex:79` motivates a population-relative ability measure and says a randomly selected score was rewarded against “the realized population share.” `:81` and `:87` describe risk elicitation for both roles, without corresponding results in the active analysis. State which measures are unused/exploratory and where their definitions or results can be found. Collecting a measure does not require a significant result or justify an accusation of selective suppression.

Also define the population benchmark and when it was available, given the same-day-payment statement at `design.tex:89`. The available text is insufficient to establish an actual payment inconsistency. Preserve the accurate disclosure that the own-score incentive is not a proper scoring rule (`:79`).

### L3-m6. Limit the balance claim and distinguish within-arm from cross-arm evidence

`results.tex:3` refers broadly to balanced treatment groups but cites only Player A; `appendix.tex:13` explicitly explains why it omits B's table. The unused `tables/balance_player_b.tex:7` and `:10` report age and education differences. These do **not** invalidate B's within-person H2 comparisons, including the within-person hypothetical comparison in the No-Punishment arm, and do not establish failed randomization or concealment.

Specify “Player A's reported background characteristics.” Including B's summary table would improve transparency. If the real-versus-hypothetical difference itself is interpreted causally across arms, report and qualify that comparison rather than treating two within-arm patterns as a treatment-effect test.

### L3-m7. The manuscript does not yet provide complete study documentation

The active `main.tex` input chain and appendix contain no study-level ethics approval/exemption statement, full participant instructions, or data/code availability statement. `design.tex:62` and `:85` document informed consent; photo consent is separately noted. Add the applicable approval/exemption and supporting-materials information, without implying that absent manuscript reporting means approval was absent. The acknowledgments placeholder at `main.tex:80` is only minor front-matter polish.

### L3-m8. Do not restore the dormant power outputs without correcting their calculation and sample labels

`scripts/python/16_power.py:33` returns `abs(p2 - p1) * 2` after already converting Cohen's h into a probability difference. This doubles the stated H1 minimum detectable difference: the stored **42.9 pp** (`scripts/python/_outputs/numbers.json:245`) should be approximately **21.4 pp** under that calculation's n=80-per-arm and p0=0.50 assumptions. The separate unused `tables/power_mde.tex` reports approximately 21.5 pp using another routine.

The numbered script's H2 power/TOST calculation uses 67 passers, whereas the headline uses 80 Bs. Neither that table nor the commented power paragraph is currently part of the article. Fix the generator and reconcile assumptions before presenting power evidence; do not copy an unused output as if it validated the current headline.

## Disposition of every prior finding

Statuses refer to the old finding as written, not to whether all nearby text is now perfect. “Superseded” means the earlier diagnosis was materially overstated or replaced by a more accurate one.

| Prior ID | Status | Current disposition |
|---|---|---|
| C1 | Superseded | Imbalance/suppression accusation withdrawn; limited reporting issue L3-m6. Within-arm paired tests do not require cross-arm balance. |
| C2 | Open | Null-as-equivalence persists: L3-M1. Old numerical confidence-bound interpretation corrected. |
| C3 | Partial | Removed from main-text coefficient discussion, but misleading connection persists in appendix and source: L3-M2. |
| C4 | Partial | Indirect payoff mechanism now acknowledged and mechanism unresolved; payoff descriptions and specific concluding attribution remain: L3-M4. |
| C5 | Resolved | Pooled interactions now implemented (`07_performance.py:123`), freshly verified p=0.54791/0.48666. Active text explicitly states nonsignificance (`results.tex:109`, `:132`). Displaying the p-values would improve auditability but “never tested” is no longer true. |
| C6 | Partial | Current Result 4 is descriptive; causal effort Result 5 remains unsupported by selected non-delegators: L3-M3. Old monotonicity prescription is not required. |
| M1 | Open | Assignment, attrition, pilot and analysis flow remain incomplete: L3-M6. |
| M2 | Open | Initial accuracy calibration still overextended to future ability/beliefs: L3-M5. |
| M3 | Open | Base earnings and final earnings still conflated: L3-M4. |
| M4 | Partial | Measurement limitations acknowledged; scoreability rationale remains weak: L3-M7. Do not claim incentivization would have been costless or uniformly simpler. |
| M5 | Partial | Full-sample null, timing caveat and exploratory status clearer; selection and summary overreach remain: L3-M7. Corrected attention counts replace old reconstructions. |
| M6 | Partial | Explicit exploratory label resolves part; unadjusted/multiplicity qualification absent: L3-m3. |
| M7 | Resolved | Current `results.tex:29` and `:109` agree with current table and fresh filtered-sample p=0.04741. New sensitivity to exclusions belongs in L3-M6. |
| M8 | Partial | A's knowledge of costly punishment is explicit and extensive margin reported; technology scope remains: L3-m4. Unproven variance/revealed-preference claims withdrawn. |
| M9 | Open | Active order reporting remains absent; current interaction p=0.07962 replaces old p=0.115: L3-M8. |
| M10 | Partial | Within-person estimand is clearer; strategy-method generalization needs qualification: L3-m4. Automatic attenuation claim withdrawn. |
| M11 | Open | Unused measures still not reconciled with their motivation: L3-m5, downgraded to minor; no inference of suppressed nulls. |
| m1 | Resolved | The old “misunderstanding should arise alike” defense is now commented out at `results.tex:127`. Broader parity concern remains L3-M5. |
| m2 | Open | General SE statement still inconsistent with clustering: L3-m1. |
| m3 | Superseded | No evidence demonstrated HC1 failure merely from n=60; optional sensitivity discussed under L3-m1, not a separate established defect. |
| m4 | Open | Exact McNemar p=0.14346, not weak significance: L3-m2. |
| m5 | Not verified | Session/population descriptions remain at `design.tex:71` and `results.tex:127`; this methods update did not independently re-audit Feier's original calibration. The words alone do not establish a substantive contradiction. |
| m6 | Open | Population-share reference set and payment timing unclear: L3-m5. |
| m7 | Open | Aggregate shares do not validate individual parity beliefs: L3-M5. |
| m8 | Open | Study documentation absent from active manuscript: L3-m7. No inference of absent ethical approval. |

## What now works, and recommended order

The individual calibration mechanism is transparent, the H2 comparison is explicitly low-outcome-specific, Player-B clustering and paired tests respect the repeated observations, the full-sample belief null is disclosed, and the new performance interaction prevents an untested activation story from carrying the mechanism conclusion. H1's sign and significance survive the new exclusion sensitivity.

Prioritize (1) H2 intervals and the correct regression contrast; (2) descriptive effort language and the limits of prospective parity; (3) assignment/pilot/exclusion documentation; and (4) passers and order sensitivity. These changes can substantially improve the defensibility of the existing study without pretending the current data identify a unique mechanism.
