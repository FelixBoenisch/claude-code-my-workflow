# Seven-Pass Review: Accountability and Algorithmic Delegation

**Updated:** 2026-09-07. **Previous synthesis:** 2026-08-21.
**Manuscript:** `manuscript/main.tex`, on `restructure/results-section`.
**Snapshot:** HEAD `d4f48b6` plus the uncommitted manuscript edits present during this review.
**Scope:** the seven included sections (`abstract`, `introduction`, `literature`, `design`, `results`, `conclusion`, `appendix`), their currently included exhibits, and the actual bibliography `manuscript/ProjectAlgorithm.bib`. Commented passages and the two orphan section drafts are excluded from active claims.

## Executive verdict

**Overall state: REVISE-MAJOR.** The manuscript has improved materially, particularly in bibliography accuracy, reporting of the effort comparison, and qualification of the performance-gradient comparison. The headline delegation result reconciles across the current manuscript and exhibits and survives inclusion of the two excluded participants.

The principal remaining work concerns **interpretation and transparent reporting**: the paper still presents a nonsignificant punishment contrast as no protection; its numbered effort result exceeds the evidence from selected non-delegators and imperfect proxies; and its introduction claims selective treatment effects and a causal explanation of cross-study differences that the design does not establish.

**No current finding is classified CRITICAL.** Consequential inferential and reporting issues are classified MAJOR; this does not mean the manuscript is ready for submission. The old claims of fabricated references shipping in the bibliography, suppressed Player B balance failures, and a missing performance interaction should not remain on the revision checklist. Some were resolved by revisions; others were overstatements by the previous review.

The old headline of “173 findings” is not a reliable denominator: several lens totals did not match their enumerated findings, and citation IDs were duplicated. Current per-lens counts below are newly enumerated, overlap across lenses, and must not be read as a deduplicated measure of scientific defects or a mechanical improvement score.

## What changed since the previous review

| Area | Current assessment |
|---|---|
| Headline delegation result | Two No-Punishment Player As are excluded for entering zero in at least eight initial predictions. The current comparison is **34/80 versus 48/79**, or **42.5% versus 60.8%**, a reduction of **18.3 pp** (Pearson p=0.0212; Fisher p=0.0264). Current abstract, results, table and figure agree. |
| Sensitivity to those exclusions | All 161 Player As give **16.8 pp**, Pearson p=0.0334 and Fisher p=0.0407. Exclusions do not create H1 significance. This sensitivity is not yet shown in the active manuscript. The descriptive pooled performance association is more sensitive to the exclusions. |
| Effort comparison | The paper now reports **8.11 versus 0.51 lbs** error reduction, Welch p=0.027 and Mann–Whitney p=0.014, with initial absolute errors **22.69 versus 22.47 lbs**, p=0.857. The old “no magnitudes/tests” criticism is resolved. The new causal wording of Result 5 remains problematic. |
| Performance selection | A pooled treatment × performance test now exists, and the body explicitly acknowledges its nonsignificance. P-values 0.548/0.487 are only in a source comment. Result 4 now states the pooled association. The introduction's “selectively” claim has not caught up. |
| Perceived performance | The former 4.65/4.87-as-overconfidence units error is substantially corrected: the current text calls 4.65/4.89 perceived-performance levels. A residual footnote and formal definition could be clearer. |
| Punishment regression | The appendix discusses both full and attention-passer samples and correctly begins by defining the interaction as a change across outcomes. A subsequent clause still conflates it with the entire bad-outcome delegation contrast. |
| Beliefs and mechanisms | Full-sample null versus passer association, exploratory status, post-decision belief measurement, and proxy limitations are now clearer. Some summaries and numbered statements still outrun those qualifications. |
| Bibliography | The September audit repaired cited metadata/verification flags, removed Stein, and supplied full Bartling author names. Current checks find **54 live cited keys, zero missing keys, and no unresolved cited verification flags**. Stronger full-text checks also overturn some old semantic accusations. |
| Build | The current source compiles in an isolated copy: **37 pages**, no undefined references/citations or BibTeX warnings. One small 1.299 pt overfull box remains in the conclusion; the title-page acknowledgment placeholder still renders. |

## Prioritized substantive findings

All findings here are MAJOR. The list is deduplicated by revision task; lens totals count their own overlapping perspectives. Paths are relative to `paper/` and refer to the reviewed snapshot.

| Priority | Evidence and issue | Recommended revision |
|---|---|---|
| **1. Punishment uncertainty and estimand** | `manuscript/abstract.tex:2`, `introduction.tex:11`, `results.tex:49,55,57`, `appendix.tex:17,23`, `conclusion.tex:6,11`. “No protection,” “alike,” and “cannot shift blame” exceed non-rejection. For 80 Player Bs, delegated minus own bad-outcome punishment is **−£0.0713**, paired p=0.1308, **95% CI [−£0.1641, £0.0216]**. The −0.103 interaction is the change in the delegation contrast across outcomes, not the bad-outcome contrast itself. | Use consistent qualified language, report the gap/CI, and show the linear combination of delegation and interaction coefficients with its own uncertainty. Report an equivalence analysis only with a justified bound and explicit sample. |
| **2. Effort and mechanism limits** | `manuscript/results.tex:100,143,146,150,155`. “Does not induce additional effort” conflicts with the paragraph's proxy caveat; final effort proxies are observed only for **46 versus 31 selected non-delegators**. A zero mean reported belief penalty also does not establish a zero aggregate behavioral response. The behavioral-asymmetry footnote lacks a reported model/test. | State the observable selected-sample pattern, preserve selection and measurement limitations, and remove causal exclusion of the channel. Identify/report the response-asymmetry analysis or remove its empirical assertion. |
| **3. Introduction/body alignment and cross-study inference** | `manuscript/introduction.tex:20,22` versus `results.tex:109,113,132`. “Selectively among … most likely to succeed” implies established treatment heterogeneity; “Once both channels are closed, the differential disappears” implies an identified cross-study explanation. Neither follows from the current evidence. | State the average treatment effect and pooled performance association separately. Present design differences as possible explanations, with the inability to distinguish their causal roles explicit. |
| **4. Exclusions, pilot, assignment and order** | `manuscript/results.tex:3,28,174`; `appendix.tex:114–116`; `design.tex:73`. The new exclusion is disclosed but its decision timing/status and unrestricted sensitivity are missing. Assignment, pilot and recruitment flow need fuller documentation. Order results are commented out and their old p-values are stale. | Show the all-completer sensitivity and affected performance findings; distinguish preregistered choices from subsequent decisions; document assignment/re-matching and pilot inclusion. Report order cells and interaction uncertainty as exploratory robustness. |
| **5. Belief scope and sample flow** | `manuscript/results.tex:77,97,100,155`; current belief table. The full-sample association is null (p=0.388/0.370), while passer AMEs are 4.7/5.5 pp per £0.10 (p=0.011/0.006; N=60). Later summaries omit that restriction. The treatment-invariance footnote lacks adequate support. | Keep the passer qualifier, report role/arm sample flow and missing-covariate losses, and describe beliefs as exploratory post-decision associations. State how unadjusted exploratory p-values are interpreted; avoid a blanket multiplicity rule for every printed test. |
| **6. Calibration and material incentives** | `manuscript/design.tex:67,69,71,85`; `results.tex:10,65,127`. Calibration matches **past measured accuracy**. It does not establish subjective parity or equal accuracy on a future prediction with different effort. Statements that the final choice cannot affect A's payoff ignore punishment-adjusted earnings. | Distinguish design calibration from subjects' beliefs and prospective performance. Distinguish base earnings from final earnings. Attribute H1 to the prospect of punishment, whose monetary and social components are not separately randomized. |
| **7. Inference reporting and dormant power output** | `manuscript/results.tex:5`; table notes; `scripts/python/16_power.py:33`; `scripts/python/_outputs/numbers.json:245`. HC1 wording conflicts with Player-B clustering; central notes omit coding/definitions/legends. The unused numbered power routine doubles an already back-transformed H1 probability difference, storing **42.9 pp** instead of approximately **21.4 pp** under its assumptions. | Correct reporting and provide headline uncertainty. Before using dormant power material, fix/reconcile its generator and sample labels; the separate unused table says about 21.5 pp. An off-paper power error does not change the current H1 estimate. |
| **8. Remaining citation precision** | `manuscript/design.tex:87,93,102`; `literature.tex:9,32`. Steffel does not operationalize blame through monetary punishment. Bartling's die treatment has no matched no-punishment die comparator. Chevrier distinguishes AI from a rule-based algorithm. | Remove/reframe Steffel in the punishment-measure citation group; separate observed die use from a causal punishment effect; attribute Chevrier's distinctive punishment pattern specifically to its AI treatment. See [Lens 7](lens_7_citations.md) for primary-text evidence. |

## Numerical details that should not be copied from the old review

**Punishment equivalence:** the old synthesis quoted passer TOST results beside the full-sample gap. Fresh tests give:

| Own minus delegated punishment after bad outcomes | Full Punishment sample | Attention passers |
|---|---:|---:|
| N | 80 | 67 |
| Mean insulation | £0.0713 | £0.0769 |
| Paired-t 95% CI | [−£0.0216, £0.1641] | [−£0.0292, £0.1829] |
| TOST at ±£0.10 | p=0.2698 | p=0.3323 |
| TOST at ±£0.20 | p=0.0036 | p=0.0118 |

A ±£0.20 test is a valid equivalence test at that bound; the old review was wrong to dismiss it as no equivalence test at all. Its economic informativeness remains a separate question. An MDE is not a confidence bound, and an observed effect below an 80%-power MDE is not itself invalid.

**Order:** in the current sample, own-decision-first delegation is 13/40 versus 27/42 (**32.5% versus 64.3%**); algorithm-first is 21/40 versus 21/37 (**52.5% versus 56.8%**). The specified logit interaction has p=**0.0796**, replacing 0.115. These descriptive differences warrant reporting; they do not prove an order artifact or invalidate the pooled randomized comparison.

**Beliefs and attention:** the own/good expected-punishment comparison is £0.604 versus £0.404, unadjusted Welch p=**0.046**, replacing 0.038. One nominal result among four comparisons is not decisive evidence of a treatment effect; the comparisons also do not establish invariance. Player A passers are **61/80 versus 68/79**, with attention-rate comparison p=0.113. Do not use complete-case regression Ns as pass-rate denominators.

**Hypothetical switching:** 12 versus 5 discordant pairs produces asymptotic uncorrected McNemar p≈0.090 but exact two-sided p=**0.143**. This changes the strength of the supplementary footnote, not H1.

## Disposition of the previous synthesis

Every lens also maps its individual historical findings. These tables cover every old cross-lens priority ID, so the former checklist can be retired safely.

| Old critical ID | Disposition |
|---|---|
| **C1 — equivalence** | **OPEN, reclassified MAJOR.** Categorical claims persist; corrected full-sample/passers evidence above. |
| **C2 — dropped tables as root cause** | **PARTIAL / REFRAMED.** Five tables are currently included. Power, Player B balance and separate robustness tables remain off-paper, but their omission is not a single proven root cause or an obligation to restore every file. Report the needed evidence and fix stale auxiliary output first. |
| **C3 — H2 interaction** | **PARTIAL.** Main-text contradiction removed; appendix still conflates the interaction with bad-outcome insulation. |
| **C4 — hidden Player B imbalance** | **SUPERSEDED.** Omission is explicit. Both actual and hypothetical within-arm paired contrasts remain valid without between-arm demographic balance. A B table is useful transparency; the old suppression/failure accusation was unsupported. |
| **C5 — untested mechanism / overconfidence** | **LARGELY RESOLVED.** Interaction implemented and nonsignificance acknowledged; levels relabelled. Intro heterogeneity wording and exact interaction reporting remain. |
| **C6 — causal cross-study claim** | **OPEN, reclassified MAJOR.** Current intro:22 still overattributes the contrast. The old three-difference design paragraph is now commented out. |
| **C7 — bibliography** | **RESOLVED for manuscript.** Stein removed, cited flags repaired, actual citation resolution clean. Root bibliography instructions still need maintenance, but do not make the compiled references invalid. |
| **C8 — acknowledgment placeholder** | **OPEN, reclassified MINOR.** Still visible on page 1 at `manuscript/main.tex:80`; remove before circulation. |

| Old major ID | Disposition |
|---|---|
| **M1 — selective belief sample** | **PARTIAL.** Full-sample null and exploratory status now explicit; sample flow and generalized summaries remain. |
| **M2 — order** | **OPEN; updated values.** Current interaction p=0.0796; no proven order artifact. |
| **M3 — multiple testing** | **PARTIAL / REFRAMED.** Exploratory label added; test-family/status interpretation still needed. Blanket adjustment of 34 p-values withdrawn. |
| **M4 — abstract contribution** | **OPEN, MINOR.** The reversal conveys novelty; closing contribution sentence could be sharper. |
| **M5 — selection absent from abstract** | **SUPERSEDED.** Do not add the former unsupported treatment-specific claim. Omission of an exploratory pooled association is not a major defect. |
| **M6 — question order** | **OPEN, MINOR.** Intro still attribution-first, remainder delegation-first. |
| **M7 — long mechanism preview** | **PARTIAL, MINOR.** Revised/shorter; placement remains an editorial choice. |
| **M8 — unchanged punishment beliefs** | **OPEN / CORRECTED.** Invariance unsupported; old claim of decisive contradiction from one p-value withdrawn. |
| **M9 — unquantified effort** | **RESOLVED.** Current magnitudes/tests included. New Result 5 overclaim is separate. |
| **M10 — unused elicited measures** | **OPEN, MINOR / REFRAMED.** Explain their use or omission. Relative rank among humans is not a direct algorithm-parity manipulation check. |
| **M11 — accountability versus money** | **OPEN / NARROWED.** H1 identifies punishment availability; monetary exposure and social judgment are not isolated. This does not invalidate H1. |
| **M12 — Steffel** | **OPEN.** Measure citation and boundary condition need correction; Steffel does not itself establish the current negative treatment effect. |
| **M13 — Litterscheidt/Dargnies** | **RESOLVED for the active manuscript.** The paragraph is now wholly commented out at `manuscript/literature.tex:19`; the old live-text tension is absent. |
| **M14 — HC1 claim** | **OPEN.** Distinguish HC1 delegation models and clustered punishment models. |
| **M15 — stars without legends** | **OPEN.** Missing legends remain; unverified journal-policy assertions withdrawn. |
| **M16 — two malformed sentences** | **RESOLVED.** Results mechanism sentence and conclusion signaling sentence rewritten. Other current prose issues are assessed in Lens 6. |
| **M17 — omitted competing works** | **MINOR / REFRAMED.** Targeted engagement would help; absence does not disprove the narrow novelty claim. |
| **M18 — long sentences / terminology** | **PARTIAL / REFRAMED.** Assess actual ambiguity and redundancy, not a mechanical 30-word violation count. |

## Minor polish

Remove the acknowledgment placeholder; define figure stars/correlations; add Ns/dispersion to the balance table; clarify the belief-table header and missing-covariate counts; label exact versus asymptotic supplementary tests; address the small conclusion overflow. Consider a sharper abstract ending, adding “accountability” to keywords, and a shorter mechanism preview. JEL choices, sentence length and punctuation preferences are not independent major defects without a relevant target-journal or house requirement.

Study documentation should also identify the applicable ethics approval/exemption, supporting instructions and data/code availability. Missing reporting is not evidence that approval or consent was absent; consent is described in the manuscript.

## Per-lens scorecard

Scores are qualitative editorial judgments, not a validated grading scale. Counts include only each lens's current numbered findings and are not deduplicated across lenses.

| Lens | Critical | Major | Minor | Score/10 |
|---|---:|---:|---:|---:|
| [1. Abstract](lens_1_abstract.md) | 0 | 1 | 4 | 7.0 |
| [2. Introduction](lens_2_intro.md) | 0 | 3 | 4 | 7.0 |
| [3. Methods](lens_3_methods.md) | 0 | 8 | 8 | 6.0 |
| [4. Results](lens_4_results.md) | 0 | 8 | 10 | 6.5 |
| [5. Robustness](lens_5_robustness.md) | 0 | 7 | 3 | 5.0 |
| [6. Prose](lens_6_prose.md) | 0 | 5 | 6 | 7.5 |
| [7. Citations](lens_7_citations.md) | 0 | 3 | 8 | 8.0 |
| **Total lens findings / mean score** | **0** | **35** | **43** | **6.7** |

## Reconciliation between lenses

- **Severity:** The recurring punishment overclaim is consistently MAJOR. It is consequential and needs correction, but does not establish invalid estimates. Front-matter placeholders are MINOR. This replaces the older inflated CRITICAL classification.
- **Performance:** The body has repaired the old untested-gradient problem; the introduction still overstates selective treatment effects. Both findings can be true. A significant coefficient in one condition and not another is not itself a significant difference between coefficients.
- **Effort:** Added statistics resolve the reporting omission. They do not resolve selected-sample identification or measurement limitations; the new numbered statement must reflect that distinction.
- **Balance:** B's omission is a transparency choice, not proof of failed H2 identification. Any causal comparison of real versus hypothetical punishment across arms needs its own justification.
- **Belief asymmetry:** The old commented test of good-versus-bad mean penalties is not the behavioral sign-response test now asserted in a footnote. Do not reinstate it as if it answered that question.
- **Citations:** Full-paper checks overrule unsupported adverse claims based on abstracts. Tontrup has an observer condition and treatment comparisons; Chevrier reports the decomposition, with treatment specificity still needing correction. Root bibliography-tool instructions are separated from actual manuscript reference validity.

## Verification and limits

Seven reviewer agents covered the seven lenses in waves within the concurrency limit; the coordinator drafted Results and synthesized the reports, with an independent Results check. No runtime/token estimate is claimed.

Read-only recomputations from the cleaned XLSX files verified selected H1/H2 tests, CIs/TOST, exclusions, order cells, attention counts, belief means and effort statistics. Regression values were also checked against current tables, code and the manifest. This was **not** a full raw-data-to-paper replication or a rerun of the entire analysis pipeline.

An isolated source copy passed pdflatex → BibTeX → pdflatex → pdflatex. The current build includes exactly `reg_delegation`, `reg_belief_specs`, `balance_player_a`, `reg_punishment` and `reg_punishment_extensive`. The final log has no undefined references/citations or BibTeX warnings, one 1.299 pt overfull box in `conclusion.tex:8–10`, and geometry/layout package warnings. The title page and selected native figures were visually inspected; no claim is made to exhaustive page-by-page visual QA. Build evidence is in the workspace's `tmp/seven_pass_2026-09-07/`.

Citation work combined supplied full papers, the completed 5 September metadata audit and targeted primary-source web checks. Blocked endpoints and unverified suggestions are identified in Lens 7; the update is not a fresh online audit of all 105 bibliography entries or an exhaustive literature search.

The author's manuscript sources, bibliography, data, production exhibits and existing PDF were preserved. The updated review covers the working tree, not merely committed HEAD. Historical reports remain available in Git; each lens contains its own old-to-current finding map.
