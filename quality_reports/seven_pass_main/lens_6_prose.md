# Lens 6 — Prose quality: updated review

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence*

**Review date:** 2026-09-07

**Snapshot:** Current working tree at HEAD `d4f48b6`, including uncommitted manuscript changes. Line references below are to this working tree, not the August review.

**Scope:** The seven section files included by `manuscript/main.tex`, plus its title-page text. Superseded section drafts and commented-out prose are excluded from the assessment of what readers see.

**Method:** Re-read the included source and reassessed every finding in the 2026-08-21 report under the local seven-pass-review skill. This pass does not independently rerun analyses or validate external sources. Numerical uncertainty and the build observations identified below were shared by the other passes.

**Current findings:** **0 CRITICAL · 5 MAJOR · 6 MINOR**, counting the issue clusters below once each. **Score: 7.5/10.**

## Assessment

Several genuine defects have been repaired. The malformed results sentence about losing the value of intermediation now reads cleanly; the conclusion's signaling sentence has a grammatical verb phrase; the comma splice in the final results paragraph is gone. The introduction now identifies both research questions, explains both comparisons, and numbers its mechanism discussion coherently. Result 4 now states the overall performance association without asserting a treatment interaction. Main-text figure notes use consistent whisker wording, and the old significance-star legend is gone.

The main remaining prose problem is uneven qualification. Numbered results, introduction, and conclusion sometimes turn imprecise estimates or exploratory associations into claims of absence, impossibility, or an identified mechanism. The body supplies qualifications that these prominent sentences omit. Repairing those statements matters more than enforcing short sentences or replacing valid passive constructions.

The previous report's headline count was incorrect: its body contained **100 IDs (C1–C3, M1–M19, m1–m78)**, not 58. All 100 are dispositioned below. Its CRITICAL classification of copyediting defects was disproportionate. Its assertions that shared infinitives, singular “their,” certain comparative constructions, or sentences over 30 words are necessarily ungrammatical are not retained. The reviewed local instructions do not establish a blanket ban on colons or em-dashes. Counts and scores therefore are not directly comparable with the old headline totals.

## Current MAJOR findings

### P6-M1 — Replace categorical absence of protection with the estimated evidence

**Locations:** `abstract.tex:2`; `introduction.tex:11,16`; `results.tex:49,55,57`; `conclusion.tex:6,11`; `appendix.tex:23`.

> “Delegation, in turn, offers no protection.” — `abstract.tex:2`
>
> “the effect of delegation is essentially zero” — `results.tex:55`
>
> “delegation cannot shift blame” — `conclusion.tex:11`

Result 2 itself is now appropriately limited to a failure to detect significantly lower punishment. The surrounding prose remains stronger. After a bad outcome, mean punishment is £0.48 for delegation versus £0.55 for own predictions (`results.tex:49`). The results pass reports a paired 95% confidence interval of approximately **[−£0.164, £0.0216]** for the delegated-minus-own difference. The negative interaction reported at `appendix.tex:17` is also inconsistent with describing all delegation effects as zero. Non-rejection is not an equivalence result, and punishment is a behavioral measure of attributed responsibility rather than a direct measure of all blame.

**Proposed headline wording:** “We find no statistically significant reduction in punishment after bad outcomes when the prediction is delegated.” In the results, give the point estimate and interval before interpreting its precision. In the conclusion, use “Our experiment does not establish that delegation protects the decision-maker from punishment.” Revise the extensive-margin summary on the same principle. These edits preserve the principal delegation finding without claiming that protection is impossible.

**Historical links:** C3, M1, m4, m57.

### P6-M2 — Result 5 excludes an unobserved mechanism

**Location:** `results.tex:146`, supported and qualified at `results.tex:140–143`; related wording at `introduction.tex:16` and `conclusion.tex:9`.

> “The prospect of punishment does not induce additional effort.”

The immediately preceding paragraph says effort is unobserved and that the channel cannot be ruled out conclusively. Outcomes and screen times are proxies, and the comparisons concern non-delegators whose selection may itself respond to treatment. The numbered result therefore cannot state a causal absence of additional effort.

**Proposed replacement:** “Among non-delegators, the observed performance and screen-time measures provide no evidence of greater effort under punishment.” Follow with the limitation that these comparisons do not identify treatment effects on effort. Keep the same evidentiary scope when previewing this mechanism in the introduction and conclusion.

**Historical link:** M14, still open.

### P6-M3 — The contribution preview still promotes a descriptive interaction to a finding

**Locations:** `introduction.tex:20`; `results.tex:110,143`.

> “it does so selectively among the decision-makers most likely to succeed” — `introduction.tex:20`
>
> “It is precisely the better performers who retain control of the decision, particularly when punishment is possible.” — `results.tex:110`

The revised `results.tex:109,132` explicitly says the treatment-specific relationships do not differ statistically. The commented diagnostic at line 109 reports interaction p-values of 0.548 and 0.487. That qualification is consistent with the restrained Result 4, but not with the contribution preview's assertion of selective treatment effects. The explanatory footnote at line 143 likewise presents stronger positive selection under punishment as established.

**Proposed introduction replacement:** “The prospect of punishment discourages delegation. Across participants, better performers are also less likely to delegate.” In the results, label the difference between treatment-specific relationships descriptive and avoid “precisely” and “particularly” as inferential emphasis. Do not infer which individuals changed their decisions from these group comparisons.

**Historical link:** m66's old sentence-level defect is resolved; this is the remaining substantive qualification problem.

### P6-M4 — Design intentions and a cross-study contrast are written as established channel closure

**Locations:** `introduction.tex:22`; `design.tex:64,71`; `literature.tex:37`; `results.tex:127`.

> “Once both channels are closed, the differential disappears” — `introduction.tex:22`
>
> “removes the relative-performance signal from the delegation decision by construction” — `literature.tex:37`
>
> “The negative relationship between performance and delegation therefore points to something other than beliefs about relative ability.” — `results.tex:127`

Individual calibration matches the algorithm to measured initial accuracy. It does not establish that subjects believe their prospective final accuracy is identical to that algorithm's success probability. Nor does comparing this experiment with another study identify the causal effect of closing either proposed channel: multiple design features differ. The softened phrase “is designed to remove” at the beginning of `results.tex:127` is an improvement, but the subsequent exclusion remains too strong and the earlier caveat about incomplete understanding is now commented out.

**Proposed contrast:** “Our design separates the roles and calibrates the algorithm to individual initial performance, reducing two possible sources of ambiguity. In this setting, we do not detect a significant punishment advantage from delegation after bad outcomes.” For the performance discussion: “Individual calibration reduces the scope for this explanation, although beliefs about prospective relative performance may still matter.” Restore a concise limitation in live prose.

**Historical links:** M8, M15, M17.

### P6-M5 — A zero mean in elicited beliefs does not by itself imply no aggregate behavioral response

**Locations:** `results.tex:100,150,155`; related summary at `introduction.tex:16`.

> “a mean expected penalty of zero implies no aggregate push toward less delegation” — `results.tex:150`, footnote

Line 100 explicitly concedes that a zero average penalty need not rule out an aggregate effect if behavioral responses are asymmetric. Line 150 then states the unconditional implication anyway. Elicitation timing and measurement error add reasons to avoid “cannot explain” in the line 155 summary. The line 100 statement that no asymmetry was found should be accompanied by its diagnostic in the analysis report, but this prose pass does not treat that undocumented test as proof of a general mathematical implication.

**Proposed replacement:** “The mean elicited penalty does not point toward less delegation, although heterogeneous responses and measurement error prevent us from excluding this channel.” At line 155, replace “cannot explain the reversal” with “does not provide a clear explanation for the reversal.” Retain the individual-level association as a separate descriptive finding.

## Current MINOR findings

### P6-m1 — Repair the remaining awkward or incomplete constructions

| Current location and quotation | Proposed repair |
|---|---|
| `design.tex:3`: “eligibility followed Prolific's standard quality screens, a prior approval rate of at least…” | “Eligibility required a prior approval rate of at least 95% and fluency in English.” Retain any additional screening requirement only if it actually applied. |
| `design.tex:71`: “should limit Player~B from reading delegation…” | “should reduce the scope for Player~B to read delegation…”; this also avoids asserting that the inference is eliminated. |
| `design.tex:85`: “Player~B learned that he had been randomly matched with a Player~A, and introduced to the task…” | “We told Player~B that he had been randomly matched with a Player~A and introduced him to the task she had completed.” |
| `literature.tex:37`: “outweighing any downstream punishment as a measure of responsibility shifting” | “making punishment an ambiguous measure of responsibility shifting.” |
| `results.tex:61`: “does not merely fail to support Hypothesis …, but the effect is statistically significant…” | “Result 1 does not merely fail to support Hypothesis 1. The effect is statistically significant in the opposite direction.” |

These are local clarity defects, not submission-blocking failures to parse the manuscript as a whole.

### P6-m2 — Clarify the sequence and the mechanism summary

At `results.tex:140`, **“Finally”** introduces effort even though signaling follows at line 150. Use “The prospect of punishment could also motivate…” or omit the transition.

At `conclusion.tex:9`, **“whereby the decision-maker would retain control”** and **“leaving only a non-monetary value in which”** obscure the links between effort, signaling, monetary incentives, and social judgment. The paragraph is more intelligible than before but still moves through all four before introducing the measurement limits. Prefer: “Decision-makers might retain control to try to outperform the algorithm. They might also retain control to signal that they intend to try hard. Our measured beliefs provide little evidence of a punishment advantage from this signal, but participants may care about the recipient's judgment independently of monetary sanctions.” Then begin a new paragraph with the limitations. This is a clarity suggestion, not a requirement to shorten every sentence.

The scoring-rule footnote at `design.tex:79` also benefits from separating **“While this linear scoring rule is not proper as…”** into the rule's incentive property and the observed reporting behavior. Preserve both substantive points. The long literature paragraph at `literature.tex:7–9` now has a useful bridge from political science to experiments; an optional paragraph break before the intermediary's blame would further help navigation.

### P6-m3 — Remove the printed acknowledgment placeholder before submission

**Location:** `main.tex:80`.

> `\hl{[To do: Add acknowledgments]}`

The title-page inspection from this review confirms that the placeholder still prints. Replace it with the actual acknowledgment or remove the placeholder when preparing the submission version. This is **MINOR**, not the old MAJOR/CRITICAL-level blocker. The old categorical claim that colored links are unacceptable at all listed journals is withdrawn; apply the chosen journal's actual submission requirements when relevant.

### P6-m4 — Anchor the abstract's calibration comparison

**Location:** `abstract.tex:2`.

> “an algorithm, calibrated to perform equally well”

The comparator is implicit and the phrase can suggest equality of prospective ability rather than matching the empirical score used by the algorithm. Prefer **“an algorithm calibrated to match her accuracy over ten initial prediction rounds.”** The current “chooses to make … or delegate” shares an infinitival “to” grammatically; changing it to “either makes … or delegates” is optional rather than correction of an error.

### P6-m5 — Finish a small, consistent copyediting pass

| Location | Current wording or formatting | Suggested edit |
|---|---|---|
| `design.tex:3` | Bare `https://www.prolific.com` | Use `\url{https://www.prolific.com}`. |
| `literature.tex:5` | “literature see, e.g.,” | “literature, see, for example,”. |
| `literature.tex:17` | “moderators for when and why algorithms are used” | “moderators of algorithm use”. |
| `literature.tex:35` | “after good outcomes delegated…” | “after good outcomes, delegated…”. |
| `design.tex:93` | “have coined the \textit{moral} domain” | “call the \textit{moral domain}”. |
| `results.tex:55` | “no striking relationship” | “no clear relationship”; keep any statistical claim tied to the corresponding analysis. |
| `results.tex:69` | “view … relatively critically” | “are relatively critical of delegating …”. |
| `results.tex:123` | “by treatment” followed by “by condition” | Use “by condition” in both sentences. |
| `results.tex:5,23`; `appendix.tex:116` | “Chi-squared” versus “chi-squared”; “Mann-Whitney” and “Kolmogorov-Smirnov” | Use lowercase “chi-squared” and surname en-dashes (`Mann--Whitney`, `Kolmogorov--Smirnov`) consistently. |

Serial commas, present tense for stable features of the experimental design, ordinary methods passives, and a numeral at the beginning of a quantitative sentence are not treated as errors. Repeated spaces and commented drafts do not alter the rendered prose.

### P6-m6 — Keep the priority claim qualified consistently

**Location:** `conclusion.tex:11`, compared with `introduction.tex:20` and `literature.tex:37`.

> “providing the first direct test”

Use the same **“to our knowledge”** qualification as in the introduction and literature section, pending the citation pass's assessment of the precisely defined novelty claim. The earlier report's separate assertion that “we contribute by providing … and show” is grammatically impossible is withdrawn: “contribute” and “show” can be parallel predicates. A simpler sentence would still read better: “We provide, to our knowledge, the first direct test of whether the prospect of punishment motivates delegation to an algorithm.”

## Disposition of every historical finding

**Resolved** means the cited defect is absent from the current included prose. **Partial** means the passage improved but a related issue remains. **Open** means the underlying concern remains, possibly at a lower severity. **Superseded** means the old recommendation is withdrawn as an unsupported rule, misdiagnosis, or inconsequential source-format preference. **Not verified** is reserved for a claim that could not be checked; none of the 100 source-level dispositions below requires that status. Historical IDs do not add to the current counts.

**Disposition totals:** 49 resolved, 11 partial, 17 open, 23 superseded, 0 not verified.

### Historical CRITICAL and MAJOR IDs

| Old ID | Status | Current evidence and disposition |
|---|---|---|
| C1 | Resolved | `results.tex:65` now says “may lose its force, along with the value”. |
| C2 | Resolved | `conclusion.tex:9` now has “signaling a willingness” and “but it would affect”. |
| C3 | Partial | No-protection and priority claims remain at `conclusion.tex:11` (P6-M1, P6-m6); the old parallelism and “no better or worse” diagnoses are withdrawn. |
| M1 | Partial | Old colon/dash sentence replaced; `appendix.tex:23` still asserts no reduction in frequency or harshness (P6-M1). |
| M2 | Superseded | `design.tex:62` uses a colon to introduce an enumeration; no verified ban makes this a major defect. |
| M3 | Resolved | `design.tex:85` now uses proper LaTeX en-dashes. Sentence length alone is not an error. |
| M4 | Superseded | `appendix.tex:7` heading remains; dash choice and a nonbreaking space are optional uniformity edits. |
| M5 | Partial | Belief owner clarified at `design.tex:71`; “limit … from” remains (P6-m1). |
| M6 | Resolved | `results.tex:157–158` splits the comma splice into two sentences. |
| M7 | Partial | Desktop restriction separated at `design.tex:3`; screening apposition still awkward (P6-m1). |
| M8 | Partial | Past tense fixed at `design.tex:85`; the strength of “common knowledge” remains substantive (P6-M4), not a demonstrated dangling modifier. |
| M9 | Open | “Lastly” became “Finally” at `results.tex:140`, but signaling still follows (P6-m2). |
| M10 | Open | Correlative remains at `results.tex:61`; downgrade to local clarity repair (P6-m1). |
| M11 | Open | “outweighing … punishment as a measure” remains at `literature.tex:37` (P6-m1). |
| M12 | Resolved | Costless-delegation discussion rewritten at `design.tex:73`; faulty “Thus” removed. |
| M13 | Open | “whereby” / “value in which” remain in `conclusion.tex:9` (P6-m2). |
| M14 | Open | Result 5 still excludes induced effort at `results.tex:146` (P6-M2). |
| M15 | Partial | “must therefore” softened at `results.tex:127`, but exclusion remains and caveat is commented (P6-M4). |
| M16 | Resolved | `results.tex:3` reports observed balance without claiming that it demonstrates effective randomization. |
| M17 | Open | “Once both channels are closed, the differential disappears” remains at `introduction.tex:22` (P6-M4). |
| M18 | Resolved | Live Result statements no longer contain the inconsistent condition-name markup; relevant passages were removed or commented. |
| M19 | Open | Printed placeholder remains at `main.tex:80`; downgrade to MINOR (P6-m3). Unsupported blanket link-color rule withdrawn. |

### Historical MINOR IDs

| Old ID | Status | Current evidence and disposition |
|---|---|---|
| m1 | Superseded | `abstract.tex:2` shares “to” across coordinated infinitives; valid grammar (P6-m4 offers optional simplification). |
| m2 | Open | Abstract comparator remains implicit at `abstract.tex:2` (P6-m4). |
| m3 | Resolved | Both endpoints now carry percent signs at `abstract.tex:2`. |
| m4 | Partial | “in return” removed; no-protection claim remains at `abstract.tex:2` (P6-M1). |
| m5 | Superseded | Serial comma at `introduction.tex:7` is a house-style option, not a necessary grammatical repair. |
| m6 | Resolved | `introduction.tex:9` now uses “can either make … or delegate”. |
| m7 | Resolved | Transition restructured at `introduction.tex:9`. |
| m8 | Superseded | Spelling out “percent” in introduction prose while using symbols elsewhere is acceptable. |
| m9 | Resolved | “to merely convey” no longer appears in the mechanism preview (`introduction.tex:16`). |
| m10 | Resolved | Preview now uses first, second, third, finally (`introduction.tex:16`). |
| m11 | Resolved | Current contribution paragraph identifies the decision and its consequences coherently (`introduction.tex:20`). |
| m12 | Superseded | Commented introduction drafts do not print and need not be purged for a prose review. |
| m13 | Open | Overview footnote still needs the clarifying comma at `literature.tex:5` (P6-m5). |
| m14 | Resolved | `literature.tex:7` now repeats “and that” and clarifies the attributed finding. |
| m15 | Partial | `literature.tex:7–9` now bridges explicitly to experimental economics; paragraph remains long (optional split, P6-m2). |
| m16 | Superseded | Serial comma in the review-citation list at `literature.tex:17` is optional. |
| m17 | Open | “moderators for when and why” remains at `literature.tex:17` (P6-m5). |
| m18 | Resolved | Old moderators topic sentence is no longer included prose. |
| m19 | Resolved | Old multi-study authority sentence is no longer included prose. |
| m20 | Resolved | Old “Yet,” transition replaced in the revised `literature.tex:17`. |
| m21 | Superseded | `literature.tex:26` can coordinate an elliptical second clause with a distinct third finding; forcing “do so” risks altering the claim. |
| m22 | Superseded | `literature.tex:28` legitimately shares “than physicians who reject them” across two comparative predicates. Optional splitting only. |
| m23 | Resolved | Autonomous-driving sentence rewritten at `literature.tex:28`. |
| m24 | Resolved | Current investment-study summary explicitly names agents at `literature.tex:33`. |
| m25 | Open | Add comma after “good outcomes” at `literature.tex:35` (P6-m5). |
| m26 | Resolved | `literature.tex:37` now specifies “in their design”. |
| m27 | Superseded | Nominal “responsibility shifting” and attributive “responsibility-shifting” can properly coexist; no blanket replacement warranted. |
| m28 | Open | Bare Prolific URL remains at `design.tex:3` (P6-m5). |
| m29 | Resolved | Extraneous comma before “or delegate” removed at `design.tex:5`. |
| m30 | Superseded | Methods passives at `design.tex:62` have clear agents and are conventional. |
| m31 | Superseded | Double source space at `design.tex:62` collapses in LaTeX and is not a printed prose defect. |
| m32 | Partial | Tenses fixed at `design.tex:69`; “For example … thus” remains harmless optional tightening. |
| m33 | Superseded | Repeated modals at `design.tex:71` are grammatical and need no required edit. |
| m34 | Open | Scoring-rule footnote remains overloaded at `design.tex:79` (P6-m2). |
| m35 | Superseded | Double source space at `design.tex:79` does not affect the rendered prose. |
| m36 | Resolved | `design.tex:87` now distinguishes elicitation and questionnaire administration. |
| m37 | Open | “have coined the moral domain” remains at `design.tex:93` (P6-m5). |
| m38 | Superseded | A question introduced by “whether” can be explored; `design.tex:102` is intelligible. |
| m39 | Resolved | Old “differs … differs” passage removed from the revised hypothesis discussion. |
| m40 | Resolved | Old “as overconfidence … for assuming responsibility” passage removed. |
| m41 | Superseded | Citation ties versus ordinary spaces are contextual line-breaking choices, not a required uniformity correction. |
| m42 | Resolved | `results.tex:3` now says “We recruited”. |
| m43 | Superseded | Present tense for a design property and past tense for observed actions at `results.tex:9` are compatible. |
| m44 | Resolved | `results.tex:10` now says “contrary to the direction”. |
| m45 | Resolved | Hypothetical-switching footnote split and clarified at `results.tex:10`. |
| m46 | Resolved | Footnote now uses “toward” (`results.tex:10`). |
| m47 | Resolved | “a systematic preference for their own predictions” at `results.tex:10`. |
| m48 | Resolved | Figure note at `results.tex:23` now gives the exact p-value without a star legend. |
| m49 | Resolved | Main figure notes at `results.tex:23,45,86` all use “Whiskers indicate ±1 standard error of the mean”. |
| m50 | Resolved | Repeated treatment-difference clause removed from live text at `results.tex:27–28`. |
| m51 | Resolved | Attention-check footnote at `results.tex:28` now says “taking the delegation decision seriously”. |
| m52 | Resolved | `results.tex:29` now uses the natural “when discussing the mechanisms”. |
| m53 | Resolved | Figure note now refers to “Player A's own predictions” (`results.tex:45`). |
| m54 | Resolved | Bad-outcome statement is a full sentence with clear corresponding averages (`results.tex:49`). |
| m55 | Resolved | Old p=0.08 sentence removed; current appendix reports p=0.077 (`appendix.tex:17`). No universal three-decimal rule imposed. |
| m56 | Partial | Singular “their” is grammatical, so that subclaim is withdrawn; “no striking relationship” remains (`results.tex:55`, P6-m5). |
| m57 | Resolved | Word order corrected to “therefore cannot” at `results.tex:57`; substantive overclaim is P6-M1. |
| m58 | Resolved | `results.tex:57` now has a comma followed by “since”. |
| m59 | Open | “relatively critically” remains at `results.tex:69` (P6-m5). |
| m60 | Resolved | `results.tex:77` now says “anticipated punishment as a mechanism behind”. |
| m61 | Superseded | Commented editorial note at `results.tex:97` does not print. |
| m62 | Resolved | `results.tex:100` now uses “hypothetical nature …, since”. |
| m63 | Superseded | Trailing source whitespace does not affect prose. |
| m64 | Resolved | Sample-composition argument rewritten into separate sentences (`results.tex:107`). |
| m65 | Resolved | Current live results prose uses “versus”; “vs.” is reserved for relevant figure captions. |
| m66 | Resolved | Old doubled connective/comma defect fixed at `results.tex:110`; interaction interpretation remains separately in P6-M3. |
| m67 | Open | “by treatment” / “by condition” still alternate in `results.tex:123` (P6-m5). |
| m68 | Superseded | Beginning a quantitative sentence with a percentage at `results.tex:143` is acceptable. |
| m69 | Partial | Main results now use `Mann--Whitney`; appendix test names remain hyphenated at `appendix.tex:116` (P6-m5). |
| m70 | Open | “Chi-squared” versus “chi-squared” remains (`results.tex:5,23`; `appendix.tex:116`, P6-m5). |
| m71 | Superseded | Blank lines after the final results paragraph have no prose effect. |
| m72 | Superseded | Commented conclusion note is nonprinting; substantive calibration question covered by P6-M4. |
| m73 | Resolved | Responsibility-assignment sentence rewritten clearly at `conclusion.tex:4`. |
| m74 | Resolved | `conclusion.tex:4` now says “We address both questions”. |
| m75 | Resolved | `conclusion.tex:6` now says “does not explain the reversal”. |
| m76 | Resolved | `conclusion.tex:9` explicitly names “both the belief and effort measures”. |
| m77 | Resolved | Both appendix section headings now use title case (`appendix.tex:5,55`). |
| m78 | Superseded | Math-mode versus text numerals and prose “percent” versus symbols do not automatically constitute errors; enforce only an adopted style. |

## Verification and limits

The current isolated build reported by the coordinating review completed successfully, with no undefined citations or references. Its final log identifies one small 1.29903 pt overfull box at `conclusion.tex:8–10`, alongside geometry/layout package warnings. This pass does not repeat old figure-overflow assertions after the figure-width changes. The live title-page placeholder was visually confirmed by the coordinating review. No manuscript text was changed by this pass.
