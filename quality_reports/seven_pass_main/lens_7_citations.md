# Lens 7 — Citation Audit

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence* (Felix Bönisch).

**Updated:** 2026-09-07. **Previous review:** 2026-08-21.

**Snapshot:** working tree at HEAD `d4f48b6`, including uncommitted manuscript edits. Locations refer to that working tree.

**Scope:** the seven sections input by `manuscript/main.tex`: abstract, introduction, literature, design, results, conclusion, appendix; actual bibliography `manuscript/ProjectAlgorithm.bib`. Commented prose and uncompiled alternative drafts are excluded from live citation counts.

This update applies the local seven-pass citation lens and `validate-bib --semantic` workflow. It rechecks structure, citation contexts, top-cited works, and previous findings using supplied full-paper texts, the recent bibliography audit's publisher/Crossref evidence, and targeted web checks. It is not an exhaustive new literature search or a new 105-entry online metadata audit. Only this review file was edited.

## Current verdict

**The bibliography repairs materially improve this lens. No critical citation defect remains.** The fabricated-entry warning, cited verification flags, and Bartling author-name issue are resolved. Stronger primary evidence also closes two earlier adverse allegations: Tontrup and Sprigman have an observer condition and treatment-level transfer results; Chevrier and Teixeira report the extensive/intensive punishment decomposition. Those allegations must leave the revision checklist.

Outstanding substantive work concerns the evidence motivating Hypothesis 1, a Steffel miscitation, and distinguishing Chevrier's two algorithm treatments.

| Severity | Current count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 3 |
| MINOR | 8 |
| **Total** | **11** |

**Score: 8.0 / 10.** Documentation drift and unused bibliography inventory are separate from manuscript defects. The August report used `MAJOR-9` twice and its headline counts did not consistently match its items; current findings have unambiguous IDs.

## 1. Structural and metadata validation

| Check | Current result |
|---|---:|
| Bibliography entries | 105 |
| Distinct live cited keys | 54 |
| Citation commands | 75: 40 `\citet`, 35 `\citep` |
| Individual key appearances, including each key in grouped citations | 110 |
| Live keys missing from bibliography | 0 |
| Duplicate keys, exact normalized titles, or normalized DOIs | 0 |
| Entries missing author, title, or year | 0 |
| DOI fields incorrectly prefixed with an HTTP resolver URL | 0 |
| Unused entries | 51 — informational |
| Cited entries with unresolved `VERIFY`/`CONFIRM` fields | 0 |

Counts were recomputed after removing LaTeX comments; bibliography entries/fields were parsed with balanced braces. No current citation-command misuse was identified. The existing `main.blg` (2026-09-07 19:50) records 54 used entries with no BibTeX warnings. The existing `main.log` (19:51) has no undefined-citation warnings. The coordinating reviewer subsequently confirmed a successful isolated four-step build of the current manuscript with no undefined references/citations or BibTeX warnings. This citation subreview did not independently run that build.

The [5 September implementation report](../bibliography_audit_2026-09-05/REPORT.md), actual `.bib`, and [cached Crossref records](../bibliography_audit_2026-09-05/core_crossref.json) agree on the consequential repairs:

- `stein_dont_2020` is deleted. All five previously cited verification flags are cleared and their corrections are present.
- Bartling/Fischbacher have full given names. Bockstedt and Kormylo use final-issue year 2026. Arnestad's article number and the missing DOIs highlighted in August are supplied.
- Sunstein/Gaffe now uses 2025 and DOI `10.52214/stlr.v26i1.13339`, consistent with the [current journal record](https://journals.library.columbia.edu/index.php/stlr/article/view/13339). Old years embedded in stable citation keys are not metadata errors.
- Exactly three unresolved identity annotations remain: `goldbach_geht_2019`, `kurtzberg_attribution_2004`, `liu_when_2021`. All are uncited; the September implementation record documents the author's decision to retain them. They are not current reference-list defects.
- Tacconelli remains documented as ahead of print. The [authors' SSRN record](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6962005) confirms its identity, journal DOI, and analyzed samples. No final issue locator was established in this update; missing final pages are not automatically an error.

Metadata comparison reused the 5 September publisher evidence, including eight cached Crossref records for the selected top ten. Online-first/final-issue differences were reconciled rather than flagged mechanically. Fresh requests to several publisher/Crossref endpoints were blocked; those attempts are not represented as successful revalidation.

## 2. Current major findings

### L7-M1 — Steffel remains in the citation group supporting punishment as the operational measure

**Location:** `design.tex:87`. **Previous:** MAJOR-4, open.

The sentence says responsibility-attribution research predominantly operationalizes blame through punishment and cites Bartling, Coffman, and Steffel. Steffel's experiments elicit decisions and responsibility/blame ratings, without implementing a monetary punishment outcome. Discussing punishment in other papers does not make its own study evidence for that operationalization.

Remove Steffel from this group, or distinguish rating-based from punishment-based evidence. Bartling and Coffman support punishment as a measure. Correct the old review too: **Coffman's main punishment stage is costless to the punisher**, although losses are real. The current sentence says “punishment,” so Coffman remains appropriate; the old review's costly-punishment characterization was too broad.

**Primary evidence:** [Steffel full text](../../master_supporting_docs/supporting_papers/_extracted_text/steffel_passing_2016.txt), experiments 2–6; [Coffman full text](../../master_supporting_docs/supporting_papers/_extracted_text/coffman_intermediation_2011.txt), published pp. 80–81.

### L7-M2 — Distinguish observed die delegation from an identified punishment effect on die delegation

**Locations:** `design.tex:93,102`; `literature.tex:9`. **Previous:** MAJOR-5 and MAJOR-6, open, consolidated.

“More likely to delegate ... even to a die roll” still lacks a comparator. Bartling and Fischbacher establish that human delegation rises from **17% without punishment to 56% with punishment**. In their random-device treatment, **39% delegate**, compared with 56% under human delegation with punishment; that difference is nonsignificant, one-sided Fisher exact **p = .14**. There is **no matched die/no-punishment treatment**. Those data therefore do not identify punishment's effect on die delegation.

The supplied article resolves the August report's uncertainty about these percentages. State die use and partial punishment protection separately from the identified punishment effect for human delegation. `design.tex:117` already accurately describes the weaker protection supplied by the random device. At `literature.tex:9`, “less delegation” should be understood as the point estimate, not an established treatment difference.

Steffel, grouped among the hypothesis's foundations at `design.tex:93`, supplies a relevant qualification: experiment 5 finds that choosing for others increases delegation to another person without the corresponding increase in coin-flip use; anticipated blame is not relieved by the coin flip. Engage that boundary when extending the human result. It does **not** itself demonstrate this manuscript's negative punishment treatment effect, as the older review sometimes implied.

**Primary evidence:** [Bartling full text](../../master_supporting_docs/supporting_papers/_extracted_text/bartling_shifting_2012.txt), §4.2, pp. 79–80, Table 3; [Steffel full text](../../master_supporting_docs/supporting_papers/_extracted_text/steffel_passing_2016.txt), experiment 5, §§10.2–10.3.

### L7-M3 — Specify Chevrier's AI condition rather than generalizing its mechanism to all algorithms

**Location:** `literature.tex:32`. **Previous:** MAJOR-10, partial; the decomposition itself is verified.

The paragraph attributes less frequent but more severe conditional punishment to “algorithmic delegation” generally. The source distinguishes human, rule-based algorithm (RA), and partly autonomous AI treatments. The distinctive pattern belongs to **AI**, where the programmer controls the decision only half the time. RA largely resembles human intermediation.

Section 4.3 reports punishment incidence of **36% for AI**, **63% for RA**, and **58% for human delegation** after an inegalitarian outcome. Table 2 reports punishment of the delegator, conditional on punishment, of **€3.91, €2.21, and €1.77**, respectively. Section 4.3.2 explicitly computes expected punishment and confirms its reduction under AI delegation relative to directly choosing the same unfair allocation.

The old “unverified decomposition” allegation is resolved. Identify the AI treatment and its programmer-control distinction. Mentioning the programmer helps explain the difference, but omission of the paper's entire programmer analysis is not a separate citation offense. Do not replace the detailed results with the abstract's compressed responsibility-gap language.

**Primary evidence:** [Chevrier full text](../../master_supporting_docs/supporting_papers/_extracted_text/chevrier_algorithm_2024.txt), §§3.2 and 4.3, pp. 12–13 and 16–19, Table 2, Figures 2–3.

## 3. Current minor findings

| ID | Location | Finding and revision |
|---|---|---|
| **L7-m1** | `design.tex:93` | “Have coined the moral domain” attributes an origin that Gogoll/Uhl does not establish. Use the existing `literature.tex:26` wording “sometimes called the moral domain.” Old MAJOR-9 (attribution), downgraded. |
| **L7-m2** | `literature.tex:17` | “Systematic reviews” is too specific for the mixture of systematic reviews, an interdisciplinary review, Qin's meta-analysis, and Irlenbusch's survey. Use “reviews and meta-analyses.” Old MINOR-17. |
| **L7-m3** | `design.tex:64` | Feier's Raven-style pattern task is grouped under “purely mathematical tasks.” Expand to mathematical or logical tasks, or remove Feier from that parenthesis. Doubt that an algorithm can err is the author's design rationale, not an independently established result of both citations. Old MINOR-23. |
| **L7-m4** | `design.tex:102` | “Similar” delegation rates in Feier becomes an argument that intermediary type matters less. The estimates are 46.1% and 56.2%, p = .28. Use “did not differ significantly,” as `literature.tex:35` already does; nonsignificance does not establish equivalence or rank the importance of intermediary type. Old MINOR-24, partial. |
| **L7-m5** | `literature.tex:28` | Tacconelli includes both lay and physician evaluators, resolving that uncertainty. Its measured outcome is vignette-based **reasonableness**, however. Distinguish favorable evaluations and inferred liability implications from demonstrated reductions in actual legal exposure “among lay and expert evaluators alike.” The [authors' abstract](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6962005) names the outcome. Old MINOR-20, narrowed. |
| **L7-m6** | `design.tex:3` | Prolific's URL remains bare text. Use `\url{}` or the existing `prolific` entry as appropriate. This is link/line-breaking polish, not a missing scholarly reference. Old MINOR-15. |
| **L7-m7** | Literature positioning and signaling discussion | A short engagement with Maasland/Weißmüller, Kirchkamp/Strobel, and Weitzner would sharpen the competing mechanisms. Their absence does not establish that the specific punishment-manipulation novelty claim is false. Old MAJOR-8/MAJOR-9 (coverage), superseded by a narrower recommendation. |
| **L7-m8** | `results.tex:127`; `literature.tex:37`; `design.tex:71` | Feier's calibration is still called population-level in results and session-level elsewhere. Its full text specifies the human participants in the same room/session. Use session-level consistently; the underlying comparison to individual calibration remains valid. Old MINOR-18, open. |

For L7-m7, [Maasland](../../master_supporting_docs/supporting_papers/_extracted_text/maasland_blame_2022.txt) varies promotion/dismissal and algorithm pretesting, not monetary punishment availability. [Kirchkamp](../../master_supporting_docs/supporting_papers/_extracted_text/kirchkamp_sharing_2019.txt) compares **partner types** in felt responsibility; this is not the present **delegated versus own decision** contrast in punishment. [Weitzner](../../master_supporting_docs/supporting_papers/_extracted_text/weitzner_reputational_2024.txt) models ability signaling through following/overriding advice, so its mechanism cannot simply be imported into full delegation under publicly matched performance. These distinctions correct the old report's suggestion that each is essentially this paper's finding or mechanism.

[Argenton's reward-side study](../../master_supporting_docs/supporting_papers/_extracted_text/argenton_potters_yang_2023.txt) remains an optional addition; `design.tex:121` now discusses Coffman's reward result. Blunden/Steffel is a plausible interpersonal-cost comparator from the September audit, but its full argument was not independently reverified here, so it is not a mandatory addition. Older unnumbered suggestions for entirely new references were not revalidated as the current literature frontier.

## 4. Top-ten cite–claim verification ledger

All seven works cited at least three times are included. At the two-citation cutoff, Tontrup, Köbis, and Hill are selected in first-occurrence order. Other tied works, including Steffel and Qin, were checked where relevant to old findings. Counts are **live key appearances**. Primary texts reside in `master_supporting_docs/supporting_papers/_extracted_text/` under the corresponding key.

| Work/key | Count | Current claim direction and primary evidence | Verdict |
|---|---:|---|---|
| `bartling_shifting_2012` | 14 | Human delegation reduces punishment and increases with punishment availability; random devices supply weaker cover. Published §4.2/Table 3 establish 17%, 56%, and 39%. | Core direction correct; die comparator/inference requires L7-M2. |
| `feier_hiding_2022` | 11 | Bad outcomes following machine delegation receive more favorable evaluations; good-outcome contrasts are nonsignificant. Full text pp. 11–14 confirms session calibration, dual roles, and the performance-belief association. | Core facts correct; L7-m3/m4 qualify task and null wording. |
| `coffman_intermediation_2011` | 10 | Directness affects punishment; intermediation also reduces charitable-action rewards. Published pp. 77–81, 95–99, 102. | Direction correct. Main punishment is costless to the punisher; the old review's gloss was wrong. |
| `oexl_shifting_2013` | 6 | A deciding but powerless intermediary absorbs blame; merely initiating random selection does not yield the same intermediary-blame pattern. Abstract and pp. 306–312. | Correct direction. |
| `gogoll_rage_2018` | 6 | People hesitate to delegate consequential tasks to machines; observers judge delegation critically. Abstract and experimental design. | Direction correct; coinage attribution is L7-m1. |
| `hamman_self-interest_2010` | 5 | Delegation lowers recipient transfers and principals' felt responsibility. Published §III.B, pp. 1840–1841 explicitly reports questionnaire results. | Verified, including the previously uncertain felt-responsibility measure. Do not imply this design itself has punishment. |
| `logg_algorithm_2019` | 3 | Algorithm appreciation depends on context/comparator; estimating body weight from photographs is an actual task. Abstract and experiment 1A. | Correct direction and task attribution. |
| `tontrup_strategic_2025` | 2 | AI transfer execution, lower transfers, and responsibility shared by allocators and observers. Supplied full manuscript §III.B, pp. 18–21; §III.C.2, pp. 23–24. | Verified at the level used. Withdraw the old observer and treatment-effect allegations. |
| `kobis_delegation_2025` | 2 | Delegation can facilitate dishonesty when interfaces permit indirect specification of dishonest goals; requests and agent compliance are different outcomes. Supplied text and [Nature article](https://www.nature.com/articles/s41586-025-09505-x). | Direction correct; preserve the interface-dependent scope. |
| `hill_does_2015` | 2 | Observers blame delegating legislatures less, including with agencies lacking substantive discretion. Full text pp. 311–314 and vignettes. | Verified. “Legislatures” is the actual stimulus domain. |

Hüholt/Szech's full text (§§2.2, 3.2) measures desired/felt responsibility and moral obligation after choice and supports the current associative wording at `literature.tex:33`. Chevrier's full results verify its decomposition, as described in L7-M3.

Feier supports the cited **design differences**, but does not identify overconfidence punishment or dual-role self-justification as causes of its evaluation differential. At `introduction.tex:22`, the differential disappearing “once both channels are closed” is a cross-study explanatory inference, not an identified result of that citation. The methods/introduction lenses should assess this interpretation; it is not double-counted here as a citation defect.

**Tontrup source limitation:** its supplied full text contains both observer attribution and treatment-level comparisons. The short [NYU author publication abstract](https://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=37891) omits those details. Absence from that abstract cannot support the old adverse findings. Direct SSRN retrieval was blocked; the revision identity beyond the repository's recorded June 2026 revision was not independently downloaded again.

## 5. Repository documentation/artifacts — outside manuscript counts

1. **Bibliography instructions drift remains.** `CLAUDE.md:31,129` and the default in `.claude/skills/validate-bib/SKILL.md` point at the root `Bibliography_base.bib` template, while `main.tex` reads `ProjectAlgorithm`. Repoint documentation when maintaining the repository. This is operational drift, not a critical failure of the bibliography actually compiled. The old claim that the template necessarily ships as the submission bibliography was unsupported.
2. **Stale labels and output remain.** `ProjectAlgorithm.bib:305` labels later entries as unverified placeholders despite the completed audit. `bibtex.stdout` still contains July warnings for now-existing keys. Prefer dated build evidence for current diagnosis.
3. **Source-only polish is separate.** Commented prose/citations and Burton's U+2010 hyphen remain. They may be cleaned for readability/portability, but the inspected build reports no error from that hyphen. Unused references are inventory, not citation defects.

## 6. Disposition of all previous findings

Resolved means current files or stronger primary evidence close the concern. Superseded means the old framing/severity is replaced. Not verified means an older suggestion was not independently established here. Old IDs are retained only for traceability.

| Previous ID | Status | Current disposition |
|---|---|---|
| CRITICAL-1 | **Superseded** | Documentation mismatch remains; actual citation resolution is clean. Repository item 1. |
| CRITICAL-2 | **Resolved** | Stein deleted; cited flags resolved. Three uncited identity annotations intentionally retained. |
| MAJOR-3 | **Resolved** | The Litterscheidt/Dargnies paragraph is wholly commented out at `literature.tex:19`; no live transparency contradiction. |
| MAJOR-4 | **Open** | Steffel punishment-measure citation remains; L7-M1. |
| MAJOR-5 | **Open** | Steffel's nonhuman boundary remains unengaged; L7-M2. It does not establish the current reversal. |
| MAJOR-6 | **Open** | Die comparator/inference remains; L7-M2. Previously unavailable percentages now verified. |
| MAJOR-7 | **Resolved** | Full Tontrup text has observer attribution and treatment-level transfer differences. Withdraw both allegations. |
| MAJOR-8 | **Superseded** | Kirchkamp remains uncited and its source TODO remains, but its null is a different comparison; L7-m7. |
| MAJOR-9 (attribution) | **Open** | “Coined” remains; downgraded to L7-m1. |
| MAJOR-9 (coverage) | **Superseded** | Qualified comparison replaces mandatory insertion; L7-m7. Blunden's substantive fit not independently reverified. |
| MAJOR-10 | **Partial** | Decomposition verified; AI-treatment specificity remains as L7-M3. Programmer discussion not separately counted. |
| MAJOR-11 | **Resolved** | Bartling/Fischbacher full names corrected. |
| MINOR-12 | **Superseded** | 51 unused entries are informational, as the validation skill specifies. |
| MINOR-13 | **Resolved** | Bockstedt/Kormylo/Dargnies all use final-issue year 2026. |
| MINOR-14 | **Resolved** | Listed missing locators/DOIs completed; Tacconelli ahead-of-print status documented; Feier's 19 is a valid article number. |
| MINOR-15 | **Open** | Bare Prolific URL; L7-m6. |
| MINOR-16 | **Superseded** | U+2010 remains without observed citation/build failure; portability housekeeping. |
| MINOR-17 | **Open** | “Systematic reviews” remains; L7-m2. |
| MINOR-18 | **Open** | Results still says population-level at line 127 while literature/design say session-level; L7-m8. |
| MINOR-19 | **Superseded** | Commented blocks remain but are not live citation defects; repository item 3. |
| MINOR-20 | **Partial** | Old report mentioned this ID without a standalone item. Expert evaluators verified; clarify reasonableness versus legal exposure, L7-m5. |
| MINOR-21 | **Superseded** | Zero appendix citations is not inherently defective. The appendix includes the preregistration directly; methodological citations require a concrete claim. |
| MINOR-22 | **Open** | July `bibtex.stdout` still stale; repository item 2, outside manuscript counts. |
| MINOR-23 | **Open** | Feier under “purely mathematical”; L7-m3. |
| MINOR-24 | **Partial** | Literature now uses nonsignificance language; design still says “similar” and infers more; L7-m4. |
| Unnumbered new-literature suggestions | **Not verified** | No exhaustive current search establishing those omissions; not mandatory revisions. |

## 7. Recommended revision order

1. Repair Steffel's punishment citation and the human-to-nonhuman inference supporting Hypothesis 1.
2. Specify Chevrier's AI condition and programmer-control distinction.
3. Correct local attribution/evidence-strength wording in L7-m1–m5 and calibration wording in L7-m8; selectively engage competing mechanisms in L7-m7.
4. Complete URL polish and maintain bibliography documentation separately. Do not reopen resolved fabrication/metadata allegations or delete the now-verified Tontrup findings.
