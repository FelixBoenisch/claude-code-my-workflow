# Lens 4 — Results and tables, updated

**Date:** 2026-09-07. **Previous review:** 2026-08-21.
**Snapshot:** `d4f48b6` plus uncommitted manuscript edits, branch `restructure/results-section`.
**Verdict:** REVISE-MAJOR. **Score:** 6.5/10.
**Active findings:** 0 CRITICAL, 8 MAJOR, 10 MINOR. Resolved findings are excluded; active findings overlap with other lenses.

Paths below are relative to `paper/`. Scope: active sources included by `manuscript/main.tex`, their five included tables and referenced figures. Comments and orphan section drafts are excluded.

## Improvements and numerical reconciliation

- The two Player A exclusions change the No-Punishment denominator from 81 to 79, leaving its 48 delegators unchanged. The headline is now **42.5% versus 60.8%, a reduction of 18.3 pp** (Pearson p=0.021; Fisher p=0.026). Abstract, results, table and figure agree. Table 1 AMEs range from −18.3 to −21.8 pp; Ns are 159, 157, 157, 157 and 128. The all-completer result remains significant at 16.8 pp (Pearson p=0.033; Fisher p=0.041).
- The effort comparison is now quantified at `manuscript/results.tex:143`: **0.51 versus 8.11 lbs** improvement, Welch p=0.027 and Mann–Whitney p=0.014. Initial absolute errors are **22.47 versus 22.69 lbs**, Welch p=0.857. Fresh read-only calculations reproduce the means and Welch tests. The old 10.94 lbs and baseline-outlier criticism describe the superseded sample.
- Pooled performance coefficients are now significant in `tables/reg_delegation.tex:15`. Result 4 at `manuscript/results.tex:113` describes the pooled association. Lines 109 and 132 acknowledge the nonsignificant difference between treatment gradients. The old “no interaction estimated” finding is obsolete.
- Perceived-score levels are correctly labelled at `manuscript/results.tex:107`; the old overconfidence units error is substantially fixed.
- H2 is unchanged: bad-outcome delegated minus own punishment is −£0.07125, paired p=0.1308. Rounded means reconcile with the figure and OLS table. Belief AMEs reconcile with their table: 1.3/1.4 pp in the full Punishment sample and 4.7/5.5 pp among passers, per £0.10.

## Active MAJOR findings

### L4-M1. Punishment conclusions still turn a nonsignificant contrast into equivalence

**Evidence:** `manuscript/results.tex:49,55,57`; `manuscript/appendix.tex:23`; `manuscript/abstract.tex:2`; `manuscript/conclusion.tex:6,11`.

Result 2 correctly says punishment is not significantly lower. “No differently,” “essentially zero” and “cannot escape punishment” are stronger. The full Punishment sample of 80 Player Bs gives a bad-outcome **95% CI [−£0.1641, £0.0216]** for delegated minus own punishment. A nontrivial reduction remains compatible with the data. The old review mixed this full-sample estimate with power/TOST results for 67 passers.

**Revision:** Report the contrast and CI and use consistent language about lack of statistically significant evidence. If equivalence matters, justify the bound and name the sample. Fresh full-sample TOST gives p=0.270 at ±£0.10 and p=0.0036 at ±£0.20. The wider bound permits effects comparable to the outcome effect; it does not establish literal equality. No power/TOST table is currently included. Lens 5 documents a separate numerical provenance issue in unused H1 power output.

### L4-M2. The H2 interaction explanation remains misleading in the appendix

**Evidence:** `manuscript/appendix.tex:17`; `tables/reg_punishment.tex:13–18`.

The appendix correctly defines the interaction as the change in the delegation difference after a bad outcome, then adds “and thus any insulation from punishment after bad outcomes.” The latter clause remains incorrect. The full-sample bad-outcome contrast is **0.032−0.103=−0.071**, not −0.103; the passer contrast is approximately **0.001−0.078=−0.077**. Interaction p=0.077 and paired bad-outcome p=0.131 test different quantities.

**Revision:** Remove the conflating clause and report outcome-specific contrasts with uncertainty. The old main-text six-line contradiction is gone, but the interpretation is only partly repaired.

### L4-M3. Result 5 exceeds the qualified evidence preceding it

**Evidence:** `manuscript/results.tex:140–146,150,155`.

The numbered statement now says **“The prospect of punishment does not induce additional effort.”** The preceding paragraph acknowledges that effort is unobserved, proxies are imperfect, and the channel cannot conclusively be ruled out. Final outcomes and screen times are observed only for 46 versus 31 non-delegators, a group selected by treatment. Baseline balance on two measures does not make their effort comparison randomized.

**Revision:** State the descriptive result about smaller prediction-error improvements and screen-time increases among non-delegators under punishment. Preserve the selection/proxy limits in the numbered statement and later references. The new statistics resolve an old reporting gap; they do not identify a causal null on latent effort.

### L4-M4. The cross-condition belief footnote still implies treatment invariance

**Evidence:** `manuscript/results.tex:77`; `manuscript/appendix.tex:84–93`.

Current read-only calculations after exclusions:

| Expected punishment | Punishment | No-Punishment | Unadjusted Welch p |
|---|---:|---:|---:|
| Delegated, good | £0.6225 | £0.5272 | 0.362 |
| Own, good | £0.6044 | £0.4044 | 0.046 |
| Delegated, bad | £0.9225 | £0.8949 | 0.787 |
| Own, bad | £0.9794 | £0.8576 | 0.199 |

The text says the manipulation “appears not to have changed participants' punishment expectations.” These comparisons do not establish that claim. **Correction to the previous review:** one p=0.046 among four unadjusted comparisons is not decisive evidence of a treatment effect either; it does not survive a four-comparison Bonferroni adjustment. Noisy sign changes in mean differences also do not establish a mechanism. The old p=0.038 belongs to the prior sample.

**Revision:** Describe the broadly similar pattern and observable differences without concluding invariance; provide a joint comparison or CIs if this matters to the argument.

### L4-M5. The claimed behavioral-asymmetry test has no identifiable reported specification

**Evidence:** `manuscript/results.tex:100` footnote (“We find no such asymmetry”) and line 150.

This concerns unequal **behavioral responses** to expected penalties for delegating versus deciding oneself. The commented analysis at `manuscript/appendix.tex:32` instead compares mean belief differences across good and bad outcomes. These are different hypotheses. The old review incorrectly treated that statistic as support for the current behavioral claim. No specification, coefficient or p-value is reported for that claim.

**Revision:** Identify and report the actual sign/piecewise response test, if conducted, or remove the assertion. Mean expected penalty zero alone does not imply zero aggregate response with nonlinear or heterogeneous reactions. This is a reporting finding, not proof that no analysis exists elsewhere.

### L4-M6. The general standard-error statement remains false for punishment regressions

**Evidence:** `manuscript/results.tex:5`; notes to `tables/reg_punishment.tex` and `tables/reg_punishment_extensive.tex`.

The general footnote says regressions report HC1 standard errors; the two punishment tables correctly specify clustering by Player B over four scenarios. Extensive-margin AME p-values also use a subject bootstrap. Scope HC1 to delegation models and describe the punishment inference separately. This is a reporting inconsistency: the reviewed punishment code does cluster.

### L4-M7. Central table notes remain insufficiently self-contained

**Evidence:** notes to `tables/reg_delegation.tex`, `tables/reg_belief_specs.tex`, and `tables/reg_punishment.tex`.

The delegation note omits explicit Player A/pooled-condition sample definitions, delegation=1 and Punishment indicator=1 coding. The belief and OLS punishment notes omit star legends. Performance-score units and several covariate definitions are left to scattered prose or the balance note.

**Revision:** Define sample, coding, score units and symbols in each table; add concise covariate glosses or an explicit definitions reference. Harmonize star usage. An unverified journal-specific star rule is not treated as a scientific defect.

### L4-M8. Attention-sample flow and scope of the belief finding remain unclear

**Evidence:** `manuscript/results.tex:28,97,100`; `manuscript/appendix.tex:78,116`; Ns and notes in the delegation/belief tables.

The text now explicitly acknowledges the full-sample belief null. However, later statements about “Player As who expect…” still need the passer qualifier. Current Player A passers are **61/80 versus 68/79**; the complete-case pooled passer regression has N=128, and the Punishment belief regression has N=60. Only one of the two missing-background observations is a passer, so Table 1's note that “two subjects are dropped in Columns (2)–(5)” is inaccurate for Column (5). Figure n=61 versus table n=60 is an explainable missing-covariate difference.

**Revision:** Add sample flow by role/condition and explain missing-covariate losses. The attention-rate difference itself is not significant (Pearson p=0.113); do not characterize it as proven differential attrition or failed randomization.

## Active MINOR findings

1. **L4-m1 — Performance gradients.** At `manuscript/results.tex:109`, interaction p=0.548/0.487 appears only in a comment. Report estimate/uncertainty if central; keep line 110's “particularly when punishment is possible” descriptive.
2. **L4-m2 — Final-outcome test.** At `manuscript/results.tex:143`, 48.4% versus 21.7% is 15/31 versus 10/46; fresh Fisher p=0.0245. Report a test, while retaining the selected-sample limitation.
3. **L4-m3 — Hypothetical switching.** At `manuscript/results.tex:10`, 12 versus 5 discordant choices gives asymptotic uncorrected McNemar p≈0.090 but exact two-sided p=0.143. Name the variant, preferably report exact inference for 17 discordant pairs. The hypothetical 41/79=51.9% is correct.
4. **L4-m4 — Figure notation.** The current performance figure shows r=−0.19* and r=−0.09, not the old −0.02. Its note at `manuscript/results.tex:123` should define the individual-level Pearson/point-biserial correlation and star. The punishment figure still displays +£0.20*** without a star legend in the note at line 45.
5. **L4-m5 — Balance table.** `tables/balance_player_a.tex:5–16` gives means/p-values without per-variable Ns or SDs. Ns can vary with missing data. The old explanation confused condition Ns with complete-case drops and is withdrawn.
6. **L4-m6 — Magnitude context.** At `manuscript/results.tex:35`, £0.30–£0.55 is roughly 15%–28% of the £2 cap; anchoring “substantial” would help.
7. **L4-m7 — Perceived-score definition.** `manuscript/design.tex:79` describes elicitation and `manuscript/results.tex:107` names the weighted mean. Define the sum of score times reported probability. Clarify that the footnote's remaining “This overconfidence” means perceived minus actual score.
8. **L4-m8 — Header.** `tables/reg_belief_specs.tex:10`: “Full Punishment” should read “Punishment, full sample.”
9. **L4-m9 — Bootstrap disclosure.** The extensive-margin note specifies 400 subject resamples. `scripts/python/25_punishment_extensive.py:78–92` uses their SD for normal-approximation p-values and skips failed fits. Name that method and successful-resample count; assess numerical stability if keeping three decimals. The old assertion that 2,000 is a universal floor is withdrawn.
10. **L4-m10 — Conditional extensive margin.** The extensive-table AME averages over outcomes, while `manuscript/results.tex:55` says “for each outcome.” Fresh exact paired binary tests give p=1.000 after good outcomes (2 versus 2 discordant) and p=0.453 after bad outcomes (2 versus 5). Report conditional contrasts/tests and qualify “indistinguishable.”

## Disposition of all previous findings

Historical IDs refer to the 2026-08-21 version in Git. Superseded includes corrections to earlier reviewer reasoning.

| Old ID | Status | Current disposition |
|---|---|---|
| C1 | PARTIAL / CORRECTED | Belief-invariance claim persists; old values and categorical rejection withdrawn; M4. |
| C2 | PARTIAL | Main-text contradiction gone; appendix conflation persists; M2. |
| C3 | RESOLVED | Levels now correctly labelled; minor definition residue in m7. |
| M1 | RESOLVED | Improvement statistics now reported; new causal overclaim is M3. |
| M2 | OPEN, downgraded | Correct updated outcome rates still lack a test; m2. |
| M3 | RESOLVED | Baseline metric/test supplied, old outliers excluded. Selection is M3. |
| M4 | OPEN | Missing star legends grouped in M7. |
| M5 | OPEN | HC1 versus clustering, M6. |
| M6 | SUPERSEDED | Notation consistency retained in M7/m4; unverified policy/unused-file objections withdrawn. |
| M7 | PARTIAL | Interaction exists and null acknowledged; remaining reporting/wording is m1. |
| M8 | PARTIAL, downgraded | Figure now has Ns, but correlation/star definition missing; m4. |
| M9 | RESOLVED | Current pooled coefficients significant; Result 4 narrowed. |
| M10 | PARTIAL | Full-sample null explicit; flow/scope remain M8. |
| M11 | OPEN | Standalone notes, M7. |
| M12 | PARTIAL / CORRECTED | Active power absent; distinguish full sample/passers and unused outputs; M1/Lens 5. |
| MINOR-1 | SUPERSEDED | Unreferenced exploratory figures are not compiled-manuscript defects. |
| MINOR-2 | PARTIAL / CORRECTED | Several claims removed; response asymmetry requires a different test, M5. |
| MINOR-3 | OPEN | 61 versus 60 needs missing-covariate explanation; M8. |
| MINOR-4 | RESOLVED | Performance difference and p=0.059 now at results:107. |
| MINOR-5 | OPEN / CORRECTED | Ns/SDs still absent; erroneous denominator rationale withdrawn; m5. |
| MINOR-6 | OPEN | Economic context, m6. |
| MINOR-7 | PARTIAL / CORRECTED | Extensive-table reference present; pooled AME is not conditional test, m10. |
| MINOR-8 | OPEN | Figure symbols, m4. |
| MINOR-9 | PARTIAL | Elicitation/summary described; formal summary/gloss, m7. |
| MINOR-10 | OPEN | “Full Punishment,” m8. |
| MINOR-11 | PARTIAL / CORRECTED | Bootstrap disclosure, m9; universal resample floor withdrawn. |
| MINOR-12 | RESOLVED FOR SOURCE CHANGE | Figure widths now 0.75/0.93 linewidth; old 0.65-width allegation withdrawn. |

## Verification limits

Fresh read-only checks used cleaned XLSX files and the current exclusions; raw-data cleaning was not reproduced. H1/H2 uncertainty also independently reproduced in Lenses 3 and 5. Other regression values were reconciled to current tables, generator definitions and the manifest. No full pipeline rerun is claimed.

An isolated copy compiled with pdflatex, BibTeX and two further pdflatex passes. The final log includes five tables, no undefined references/citations, and one 1.299 pt overfull box. The title page and native performance, punishment and hypothetical-punishment PNGs were visually inspected; this is not a claim of inspecting every PDF page. The acknowledgment placeholder belongs to Lens 6. Manuscript sources, data, bibliography, production exhibits and the author's existing PDF were preserved.
