# Methods Referee Report

**Calibrated to:** American Economic Review (AER)
**Disposition:** CREDIBILITY ("is the design clever or a fishing expedition? Is randomization working? Are the stars doing too much work? Is statistical power adequate to the claim?")
**Paper type:** Survey-experiment (online randomized experiment with respondent-level randomization)
**Critical peeve:** Power calculations required for null results.
**Constructive peeve:** Gives credit for explicit pre-registration when relevant.
**Date:** 2026-05-01

## Executive verdict

**Score:** 64 / 100
**Recommendation:** Major Revision (bordering on Reject; the disposition is recoverable but the paper as it stands is too thin on power, preregistration documentation, and reproducibility for AER)
**Headline:** The randomization is mechanical and the design is clever in important ways, but the headline n=161 between-subject test is fragile, the H2 null is reported without a power calculation, and the preregistration vs. reported tests issue is unresolved on the page — three things AER's methods bar will not let pass.

### Note on rubric choice

I keep the survey-experiment rubric (Design 25 / Sample 25 / Measurement 20 / Attrition+Balance 20 / Replication 10) because the unit of randomization is the respondent, the identification is mechanical via random assignment, and the live threats are exactly the survey-experiment threats: imbalance, manipulation comprehension, attrition, sampling-frame validity, and PAP adherence. The Reduced-form rubric is the wrong fit — there is no DiD/IV/RD machinery to grade. I then apply AER's `Replication 5 → 10` adjustment by lifting Replication to 15% and re-normalizing the others (Design 24 / Sample 24 / Measurement 19 / Attrition+Balance 18 / Replication 15). AER's `Identification 35 → 40` adjustment is for reduced-form papers and does not apply here; identification by randomization is essentially binary.

## Pre-scoring sanity checks

| Check | PASS / FAIL | Evidence |
|---|---|---|
| Balance (pre-treatment covariates across arms — Player A) | **PASS** | Appendix Table `tab:treatment_balance`: age, female, SES, university, technology, leadership all p > 0.30. Player B balance asserted in `results.tex:9` footnote ("results available on request") — should be in the appendix, but not a fail. |
| Manipulation-check pass rate | **PARTIAL PASS** | The "manipulation" here is the punishment-possibility framing; there is no separate manipulation check on whether subjects internalised that distinction. Two attention checks exist (belief-elicitation screen for Player A; punishment-elicitation screen for Player B). Player B pass rate = 83.9% (135/161) reported; Player A pass rate is `[ZZ%]` placeholder (`results.tex:11`). The missing Player A pass rate is a manuscript-completeness fail in waiting; I do not flag as outright FAIL only because the placeholder is explicit. |
| Attrition asymmetry | **CANNOT VERIFY** | `design.tex:31` mentions "attrition and subsequent re-matching" raised the planned 320 to 322 actually recruited. No table reports differential attrition rates by arm, and no analysis of attrition-by-treatment is provided. For an online survey-experiment, this is the standard table that must be in the appendix. |
| Sampling-frame validity | **PASS (qualified)** | UK Prolific, desktop-only restriction, Feb–Jun 2023. Prolific is acceptable for a stylised behavioural test of this kind in 2023; the limitations section acknowledges external validity to broader populations is bounded. AER will read this as "fine for a behavioural mechanism paper, weak for a policy claim" — and the paper sells itself partly on a regulatory implication, so this matters. Quality screens are gestured at via `[CITE/SPECIFY]` placeholder in `results.tex:7`. |
| Preregistration adherence (PAP) | **FAIL** | `results.tex:15` footnote: "pre-registration specifies one-sided tests in the H1 direction" but two-sided tests are reported, with the issue flagged as a `[CHECK]` placeholder for review. This is precisely the sort of unresolved deviation that AER's Data Editor and a credibility-disposed referee will not tolerate. The PAP itself is not reproduced or linked in the manuscript. The H1 *result reverses the predicted direction* of the one-sided pre-registered test, which makes the choice of two-sided here doubly load-bearing — a one-sided test in the predicted direction would not even reject. |

**Result: One FAIL (preregistration adherence) and one CANNOT VERIFY (attrition). Composite score is therefore CAPPED at 70.** The score I assign (64) sits below that cap on substance, not because of the cap.

## Dimension scores

| # | Dimension | Weight (renorm.) | Score (0–100) | Weighted |
|---|---|---|---|---|
| 1 | Design (treatment construction, control adequacy) | 24% | 80 | 19.2 |
| 2 | Sample (recruitment, eligibility, representativeness, power) | 24% | 50 | 12.0 |
| 3 | Measurement (DV validity, manipulation comprehension, beliefs) | 19% | 65 | 12.4 |
| 4 | Attrition + balance | 18% | 60 | 10.8 |
| 5 | Replication / preregistration adherence | 15% | 65 | 9.8 |
| | **Composite** | **100%** | | **64.2 → 64** |

Brief justifications:
- **Design (80).** Individual-level algorithm calibration to neutralise relative-performance signalling is genuinely clever and the right answer to the Feier et al. (2022) critique. Switching off punishment in the *Treatment* arm to identify the motivational margin is also right. The strategy method for Player B is standard. Loses 20 points for one design choice that bites later: incentive-aligned principal/recipient (`design.tex:76`) means H2 is a low-power test by construction, and the paper acknowledges this in passing.
- **Sample (50).** No ex-ante power calculation reported anywhere I can find. n=161 Player As (≈80 per arm) is small for a between-subject behavioural test where the headline difference is 17 percentage points; n≈67 Player Bs after attention-check exclusion is small for declaring a null on H2. This is the load-bearing weakness.
- **Measurement (65).** Belief elicitation is unincentivised by the authors' choice (defensible reasoning given), but this limits how much the H1 mechanism story can lean on the elicited beliefs — and the paper does lean on them in `sec:beliefs`. The Player A attention-check pass rate is a placeholder.
- **Attrition + balance (60).** Balance is documented and clean for Player A; attrition by arm is not. "Re-matching" without a transparent rule is a flag for an AEA Data Editor.
- **Replication / preregistration (65).** Preregistration exists and is referenced. But (a) the PAP is not linked in the manuscript, (b) the one-sided→two-sided deviation is unresolved on the page, (c) cross-artifact reproducibility audit cannot run because no analysis scripts exist (per `quality_reports/cross_artifact_algorithms_and_responsibility/reproducibility.md`). Per Rule #9, an `/audit-reproducibility` FAIL is FATAL — but the audit was *unable to run*, not a confirmed FAIL, so I treat as a serious MAJOR rather than fatal. The AEA Data and Code Availability Policy requires a complete replication package at acceptance, and "we have no scripts in the repo" cannot survive that.

## Major concerns (each with "What would change my mind")

### Concern 1: H2 null reported with no power calculation

**Dimension:** Sample (#2)
**Severity:** MAJOR
**Description:** The headline test for H2 is paired-t p=0.153 / Wilcoxon p=0.533 on the bad-outcome cell of the strategy method, evaluated on roughly 67 Player Bs (135 attention-check passes — but the within-subject test on the low-payoff cells uses only those Bs; the effective n is small). The paper concludes "punishment is essentially outcome-based" (`results.tex:88`) on the strength of this null. There is no ex-ante power calculation, no minimum detectable effect, and no post-hoc bound on what the test could have detected at conventional power. The Conclusion (`conclusion.tex:17`) explicitly acknowledges that "scaling the experiment to a larger sample would tighten the precision of Result~2's null" — which is the right thing to say but does not substitute for actually quantifying how underpowered the test is.

**Why this matters:** A null result without a power calculation is not evidence of absence; at the AER bar, the paper has to be transparent about what effect sizes the test could have ruled out. The paper's *interpretive* claim — that delegation does not insulate from punishment in this setting — is treated as one of two co-equal headline findings. If the test only had power to detect, say, a 50%+ difference in punishment under delegation, the framing should be much more cautious. This is exactly the kind of credibility move AER referees ask for.

**What would change my mind:** A power calculation in the design or appendix that (i) states the MDE for the H2 paired test at the sample size achieved, given the observed within-subject SD of punishment, at conventional power (80%) and significance (5%); (ii) reports a frequentist equivalence test (e.g., TOST) against a pre-specified bound on what counts as "no meaningful insulation"; or (iii) replaces the unconditional null statement with a confidence-interval framing (e.g., "the 95% CI on the delegation effect on punishment in the bad-outcome cell rules out reductions larger than £X"). Any of the three would resolve the concern; (i) plus (iii) is the strongest pairing.

### Concern 2: H1 sample-size justification absent; headline p is borderline

**Dimension:** Sample (#2)
**Severity:** MAJOR
**Description:** H1 reports Chi-squared p=0.049 / Fisher exact p=0.041 on n=161 Player As (`results.tex:15`). The paper does not state a target sample-size justification ex-ante (the design says "we targeted a balanced design of 80 participants per role per treatment, for a planned sample of 320 subjects" without showing the underlying power calculation that produced the 80-per-cell number). The headline test is at the conventional 0.05 threshold; with such a borderline p, the lack of an ex-ante justification matters. Compounding this: the *direction* of the H1 finding reverses the preregistered prediction. Reporting a two-sided p when the PAP specified one-sided tests is a defensible deviation *only if explicitly justified* — and right now the manuscript flags it as a `[CHECK]` placeholder.

**Why this matters:** A borderline-significant headline that reverses the predicted direction, reported with the wrong-tailed test relative to the PAP and without an ex-ante power calculation, is the canonical fragile finding that AER's CREDIBILITY-disposed referees flag. This is not a fatal issue; but the framing as the paper's "main empirical contribution" demands a tighter statistical story than the manuscript currently delivers.

**What would change my mind:** (i) State the ex-ante power calculation that justified n=80 per cell (target effect size, baseline rate, alpha, beta); (ii) explicitly justify the deviation from the preregistered one-sided test, in-text rather than in a `[CHECK]` placeholder, and report both the one-sided and the two-sided p-value transparently (the one-sided p in the predicted direction is non-significant by construction — say so); (iii) report a robustness-block check showing the H1 result survives with a logit specification with controls (already done in Table 1 col 2 — incorporate into the headline framing rather than a robustness paragraph); (iv) ideally, a small bootstrap or randomization-inference p-value to confirm the test is not knife-edge.

### Concern 3: Preregistration deviation unresolved on the page

**Dimension:** Replication / preregistration (#5)
**Severity:** MAJOR
**Description:** `results.tex:15` footnote: "Two-sided tests reported here. [CHECK: pre-registration specifies one-sided tests in the H1 direction; report as a footnote or move to one-sided depending on the registry text. -- placeholder for review]". This is a known unresolved deviation between PAP and reported analysis, marked for review and not yet resolved. The PAP itself is not reproduced, linked, or cited by registry ID anywhere in the manuscript I read. The constructive part of my peeve is to give explicit credit for preregistration when it is well-handled — but here the preregistration is invoked as a credibility signal without being made auditable, and the deviation is left as a TODO.

**Why this matters:** AER reads PAP adherence very strictly. A deviation flagged as `[CHECK]` in the manuscript text is a desk-level red flag for the methods referee and for the Data Editor. The H1 finding *reverses* the PAP-predicted direction, which makes the choice of test (one-sided vs two-sided) directly outcome-determinative.

**What would change my mind:** (i) Resolve the placeholder: state in-text whether the PAP specified one-sided or two-sided, give the registry ID and link, and report the analysis as preregistered (with an explicit second analysis as exploratory if a deviation is needed); (ii) add a "deviations from PAP" table or paragraph in the appendix listing every analysis change relative to the PAP and the rationale; (iii) link the PAP in a footnote at the start of `results.tex`. Standard practice and uncostly.

### Concern 4: Attrition by arm is not reported

**Dimension:** Attrition + balance (#4)
**Severity:** MAJOR
**Description:** `design.tex:31` notes "Due to attrition and subsequent re-matching, we ultimately recruited 322 participants" but does not report the rate or pattern of attrition, broken down by arm and role. For an online experiment, differential attrition is the leading internal-validity threat after randomization itself, and the standard expectation is a CONSORT-style flow diagram or equivalent table.

**Why this matters:** Without the breakdown, the reader cannot rule out that the 17pp delegation difference reflects differential drop-out between Baseline and Treatment Player As (e.g., subjects in one arm find the task more aversive and drop). The post-randomization re-matching is also unexplained — was matching done after attrition, and if so, what is the rule?

**What would change my mind:** A CONSORT-style flow diagram or an appendix table showing for each arm and each role: number invited / consented / completed-screener / completed-task / passed-attention-check / included-in-analysis. Plus a one-sentence statement of the re-matching rule. Plus, ideally, a Lee-bounds robustness analysis on H1 if attrition rates differ across arms by more than ~5 percentage points.

### Concern 5: Replication package does not exist

**Dimension:** Replication / preregistration (#5)
**Severity:** MAJOR
**Description:** The cross-artifact reproducibility audit at `quality_reports/cross_artifact_algorithms_and_responsibility/reproducibility.md` reports CANNOT VERIFY because there are no analysis scripts in the repository. Per Rule #9 of the methods-referee protocol, an `/audit-reproducibility` FAIL is FATAL — but the audit was unable to run rather than confirmed FAIL, so I treat as a serious MAJOR rather than fatal. AER's Data and Code Availability Policy requires a complete replication archive at acceptance.

**Why this matters:** The numeric claims in the manuscript (42.5% / 59.3% delegation rates, p=0.049 / p=0.041, the regression table, the 21.7% / 45.5% non-delegator success rates) are not currently audit-able from scripts. The AEA Data Editor will not accept the paper without the full pipeline. More importantly for *this* review: as a referee I cannot verify any of these numbers; I am evaluating reported point estimates on trust. For a borderline-p headline, that trust gap should be closed.

**What would change my mind:** A complete `scripts/python/` or `scripts/R/` pipeline producing every numeric claim and table in the manuscript, with `_outputs/` referenced by `\input{}` in the .tex files (per the SSOT rule the project itself adopts). Then a re-run of `/audit-reproducibility` returning PASS. This is non-negotiable for an AER submission and is the single highest-leverage thing the author can do before the next round.

## Minor suggestions

1. **Player B balance.** Move "results available on request" (`results.tex:9` footnote) to an appendix table. It costs one table and removes a referee question.
2. **Manipulation comprehension.** Add a one-item check that subjects in the Treatment arm understood that punishment was off the table. The paper relies on this distinction being internalised; one Likert item or one comprehension question would close the loop.
3. **"Two of the four belief scenarios are hypothetical."** Acknowledged in the conclusion. Consider reporting H2 patterns separately for the two payoff-relevant cells vs. the two hypothetical cells, to demonstrate the patterns are not driven by the hypothetical scenarios.
4. **Calibration disclosure.** The Bernoulli-replication implementation of the algorithm (`design.tex:41` footnote) is clean and clever — promote it from a footnote to the main text. It is the design's strongest selling point relative to Feier et al. (2022).
5. **Currency placeholders.** `[ZZ]` placeholders for earnings and Player A attention-check pass rate appear in both `design.tex:31` and `results.tex:7,11`. These should be filled before resubmission; in their current form they would not pass desk review.
6. **MPL citation.** `[CITE: which MPL? --- placeholder]` in `design.tex:49` needs to be resolved; the choice of MPL matters for risk-preference comparability.
7. **Strategy-method robustness.** A direct-method companion sample, even small, would strengthen Result 2 considerably (already noted as future work — fine, but state the stakes).
8. **Stars in tables.** The current tables use `* p<0.1; ** p<0.05; *** p<0.01` notation. AEA policy since 2023 prohibits significance stars. Re-format Tables 1 and A2 with point estimates and SEs only; report p-values in notes if needed.

## Positive observations

1. **Individual-level algorithm calibration.** The Bernoulli replication of each subject's empirical accuracy rate is the right design choice and is genuinely innovative relative to Feier et al. (2022). It substantively closes the relative-performance confound that contaminates the prior literature.
2. **Punishment-off treatment arm.** The between-subject manipulation that switches off punishment entirely is exactly the right way to identify the motivational margin of H1, and is, as far as I can tell, novel in this literature.
3. **Strategy method across all four cells.** Eliciting punishment for all four (delegation × outcome) cells is the right answer for testing H2 and is well-implemented.
4. **Preregistration exists.** The fact that the paper has a PAP at all puts it ahead of much of the historical literature in this area; the constructive part of my peeve credits the author for this. The execution of the PAP-to-paper translation is what needs work, not the existence of the PAP.
5. **Honest mechanism analysis.** Section 4.5 (`sec:mechanism`) systematically considers four mechanisms (M1–M4) and is candid that M2 is incompatible with one reading of the data and M4 cannot be ruled out. This kind of honest mechanism enumeration is rare and is methodologically the right move.
6. **Acknowledgement of the design's null-power problem.** The Conclusion (`conclusion.tex:17`) explicitly notes that scaling the sample would tighten Result 2's null. The author already understands the issue — they just need to operationalise it as a power calculation rather than a future-work bullet.
7. **Clean separation of delegator and evaluator subject pools.** Distinct Player A and Player B samples, no double-hatting — an improvement over Feier et al. (2022), where the same subject acts as both delegator and evaluator.
