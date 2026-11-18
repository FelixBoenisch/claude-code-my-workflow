# Lens 2 — Introduction Structure

**Manuscript:** Accountability and Algorithmic Delegation: Experimental Evidence

**Reviewed:** 2026-09-07; current working tree, including uncommitted edits, at HEAD `d4f48b6`

**Sources:** `manuscript/introduction.tex`, checked against `abstract.tex`, `literature.tex`, `design.tex`, `results.tex`, `conclusion.tex`, and `main.tex`

**Framework:** Cochrane / Varian; local `.claude/skills/seven-pass-review/SKILL.md`

**Scope:** Introduction structure and fidelity to the current paper. Commented source is distinguished from published prose. Citation verification and detailed identification checks belong to the other lenses.

## Current assessment

| Severity | Count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 3 |
| MINOR | 4 |

**Score: 7 / 10.** The two contributions and main treatment contrast are clear. The headline magnitudes now agree across sections: punishment reduces delegation from 60.8% to 42.5%, a difference of 18.3 percentage points. The main remaining problems concern claims of no protection from punishment, treatment-specific selection by performance, and a causal explanation of the contrast with Feier et al. Opening and ordering preferences are editorial issues and are downgraded from their earlier MAJOR ratings.

## Rubric scorecard

| Item | Current verdict |
|---|---|
| Opens with the research question | Partial: both questions appear in the opening paragraph, after scene-setting and citations (`introduction.tex:5`). |
| Hook → context → contribution → roadmap; literature after hook | Partial: economics context follows the question, but normative citations precede it; contribution follows an extended mechanism paragraph (`:7`, `:16`, `:20`). |
| Contribution counted and enumerated | Pass: “Our contribution is twofold. First…” and “Second…” remain explicit (`:20`, `:22`). |
| Findings previewed with magnitudes | Partial: delegation effect fully and consistently quantified; punishment comparison has neither its estimated gap nor uncertainty (`:11`). |
| Roadmap matches manuscript | Pass: literature, design, results/mechanisms, conclusion match `main.tex:100`, `:102`, `:104`, `:106`. Preregistration appendix already linked at `introduction.tex:9`. |
| Preview faithful to evidence | Partial: pooled performance description at `:16` improves on earlier version, but three substantive claims still exceed the evidence. |

## MAJOR findings

### I-M1 — Cross-study comparison still claims a channel explanation the design does not identify

**Evidence:** `manuscript/introduction.tex:22`; `literature.tex:35` and `:37`.

The revised paragraph more clearly explains the different treatment contrasts, the reward-versus-punishment distinction, and the separation of roles. It nevertheless ends: “Once both channels are closed, the differential disappears, and punishment tracks the realized outcome instead.”

This presents the absence of a statistically detectable differential as the consequence of removing two channels. Neither channel is varied experimentally within this study. The current literature section describes differences in evaluation instrument, calibration, role assignment, and punishment manipulation; it does not establish which explains the contrasting results. Even granting the intended role of calibration, that cross-study attribution does not follow. The earlier report's reliance on a live three-item paragraph in `design.tex` is stale: that paragraph is now commented out at `design.tex:131` and is not a published contradiction.

**Revision direction:** separate the design contrast from the observation. For example: “In our design, with separate roles and individual-level calibration, we detect no significant punishment reduction from delegation. The comparison does not identify which design difference accounts for the contrast with their findings.” Do not describe the differential as having been experimentally made to disappear.

### I-M2 — “Offers no protection” turns a nonsignificant estimate into an established absence

**Evidence:** `manuscript/introduction.tex:11` and `:16`; `results.tex:49` and `:52`; also `abstract.tex:2` and `conclusion.tex:6`.

The preview says delegation “offers no protection against punishment,” and the mechanism paragraph starts from “no differential punishment.” Current numbered Result 2 is appropriately narrower: delegation does not reduce punishment **significantly** after a low-payoff outcome. The body reports £0.48 for delegated versus £0.55 for own decisions after bad outcomes, with paired-test `p = 0.13`. The estimate is in the hypothesized protection direction; failure to reject zero does not establish equivalence or rule out protection.

The review's independent numerical check gives a delegated-minus-own estimate of −£0.07125 (80 recipients; paired-test `p = 0.1308`), consistent with those levels. This finding does not depend on requiring a significance test in the introduction: the issue is the strength of the verbal conclusion. Its recurrence elsewhere does not make the preview accurate.

**Revision direction:** use “We find no statistically significant reduction in punishment from delegation,” optionally followed by the bad-outcome levels or gap. This also addresses the earlier request to quantify the second contribution. An equivalence claim would require an explicit substantively meaningful bound and supporting precision analysis.

### I-M3 — Contribution still asserts selective treatment effects after the body narrowed the selection result

**Evidence:** `manuscript/introduction.tex:20`; contrast with `introduction.tex:16`, `results.tex:109`, `:113`, and `:132`.

The contribution says punishment discourages delegation “selectively among the decision-makers most likely to succeed.” This links the randomized punishment effect to ability and reads as established treatment heterogeneity. The body now explicitly states that the performance–delegation relationships do not differ statistically between conditions (`results.tex:109`, `:132`), and Result 4 has been narrowed to “Better-performing Player~As are less likely to delegate” (`:113`). The introduction's mechanism paragraph already uses this pooled formulation (`:16`).

The descriptive slope difference and the comparison of delegators' mean scores across conditions (`results.tex:110`) do not establish that the treatment effect concentrates among stronger performers. This is a substantive inconsistency, not merely an issue with “most likely to succeed.” The old objection that relative wording was inappropriate because absolute success rates were low was too strong: relative rankings remain meaningful at low success probabilities.

**Revision direction:** conclude the first contribution with the average treatment effect. If selection remains here, state it separately: “Across conditions, better-performing decision-makers are less likely to delegate.” Label any treatment difference in this relationship descriptive, with the lack of statistical evidence for heterogeneity clear.

## MINOR findings

### I-m1 — Opening delays the behavioral question

**Evidence:** `manuscript/introduction.tex:5`.

The first three sentences establish widespread algorithm use and give examples; the fourth introduces the normative citations; the sixth asks the first behavioral question. The opening has been compressed since the previous review, but the question still follows broad scene-setting. Moving the behavioral tension to the first or second sentence would sharpen the hook. This is an editorial improvement, not a major defect: both questions are clear within the opening paragraph, and the economics literature follows them at `:7`.

### I-m2 — Extended mechanism preview separates findings from contribution

**Evidence:** `manuscript/introduction.tex:16`, followed by contributions at `:20` and `:22`.

The live mechanism paragraph is approximately 293 whitespace-delimited words, down from the earlier version. It still takes the reader through anticipated punishment, effort, signaling, and performance selection before the counted contribution arrives. Its admission that mechanisms remain unresolved is appropriate. Consider placing the contributions immediately after the findings, then compressing or repositioning the mechanism discussion. The issue is reading order, not a requirement to remove qualifications or substantive material.

### I-m3 — Opening questions and subsequent presentation use opposite orders

**Evidence:** `manuscript/introduction.tex:5` versus `:11`, `:20`, `:22`; `design.tex:99` and `:109`; `results.tex:7` and `:33`; `conclusion.tex:4`.

The introduction asks attribution first and delegation second, whereas findings, contributions, hypotheses, results, and conclusion present delegation first. Swapping the opening questions would give readers a consistent mapping. The earlier MAJOR rating overstated the cost of this minor organizational mismatch.

### I-m4 — Stale alternatives remain in the introduction source

**Evidence:** `manuscript/introduction.tex:3`, `:13`, `:14`, `:18`, `:26`, and `:28`.

The file retains an old opening, multiple mechanism versions, a superseded design-contribution paragraph, and an obsolete three-strand contribution paragraph. These comments do not appear in the compiled paper and are not counted as live claim inconsistencies. They can still confuse source-level collaboration, and the local single-source-of-truth rule asks for stale comments to be removed before sharing. Archive useful alternatives outside the manuscript when preparing a clean draft.

## Disposition of every previous finding

Previous IDs refer to the replaced report, whose own date was 2026-08-20. Current findings use the `I-` prefix to make the mapping unambiguous. Counts above include only current findings.

| Previous ID | Status | Current disposition |
|---|---|---|
| MAJOR-1 — buried question / citations | Partial | Opening compressed; question still delayed. Downgraded to I-m1. |
| MAJOR-2 — causal cross-study attribution | Open | I-M1. Comparison paragraph clearer, but “Once both channels are closed…” remains. Old live-design-paragraph evidence retired because it is now commented out. |
| MAJOR-3 — mechanism paragraph before contribution | Partial | Paragraph revised and shorter; ordering remains. Downgraded to I-m2. |
| MAJOR-4 — question order | Open | I-m3; downgraded to MINOR. |
| MINOR-1 — only one previewed result quantified | Partial | Delegation magnitude current and correct; punishment unquantified. Subsumed under I-M2 because inferential wording is the material issue. Quantifying exploratory selection is optional, not a separate defect. |
| MINOR-2 — 16.8 versus roughly 17 points | Resolved | `introduction.tex:11`, `abstract.tex:2`, and `results.tex:9` consistently give 18.3 points, using 60.8% versus 42.5%. |
| MINOR-3 — beliefs “match” actual levels | Resolved | `introduction.tex:16` now says “actual punishment pattern,” following the specific claim about differential punishment. This distinguishes the pattern from level overestimation in `results.tex:76`. |
| MINOR-4 — recruitment total presented as sample | Superseded | 322 accurately describes recruitment; `results.tex:3` explains roles and two Player A exclusions. Main Player A sample is 159, not the old review's 161. Role-specific analytic Ns could be added, but recruitment N in this introductory overview is not itself misleading. |
| MINOR-5 — conflicting counts of design differences | Resolved | `literature.tex:37` says “various respects”; `introduction.tex:22` distinguishes comparison dimensions; old design enumeration commented out at `design.tex:131`. Remaining causal language is I-M1, not an enumeration inconsistency. |
| MINOR-6 — “most likely to succeed” | Superseded | I-M3 identifies unsupported treatment-specific selection. Low absolute success rates alone do not invalidate a relative performance description. |
| MINOR-7 — stale comments | Open | I-m4, with current locations; comments are not treated as published prose. |
| MINOR-8 — roadmap omits appendix | Superseded | No requirement to enumerate all appendix material. Roadmap accurately covers main sections; `introduction.tex:9` already directs readers to the preregistration appendix. |

## Revision priority

1. Align the contribution and headline preview with the identified average effect and uncertainty in punishment and heterogeneity results (I-M2, I-M3).
2. Remove causal channel attribution from the cross-study comparison (I-M1).
3. Adjust the hook and ordering if helpful, then archive stale alternatives (I-m1–I-m4).

Preserve the counted contributions, clear randomized treatment contrast, matching headline magnitudes, explicit unresolved-mechanism conclusion, and accurate main-text roadmap. The findings call for targeted revisions, not a wholesale introduction rewrite.
