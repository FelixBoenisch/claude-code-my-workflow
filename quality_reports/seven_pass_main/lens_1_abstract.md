# Lens 1 — Abstract Audit (updated)

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence* (Felix Bönisch, WZB Berlin)

**Review date:** 2026-09-07

**Snapshot:** Current working tree on `restructure/results-section`, HEAD `d4f48b6`; uncommitted manuscript changes included.

**Files read:** Active text in `manuscript/main.tex`, `abstract.tex`, `introduction.tex`, `literature.tex`, `design.tex`, `results.tex`, and `conclusion.tex`; current punishment regression table. Commented passages and historical manuscript backups are excluded from the active claims.

**Baseline:** Prior Lens 1 report, internally dated 2026-08-20. All old finding IDs are mapped below. Paths and line numbers are relative to `paper/` and refer to this snapshot.

## Current assessment

The abstract correctly reports the current 18.3 percentage-point delegation difference, from 60.8% without punishment to 42.5% with punishment. Its main remaining substantive defect is the categorical statement that delegation “offers no protection.” Removing “punish ... alike” improves the wording without removing that inference: the punishment comparison does not reject equal means, but it does not establish the absence of protection.

The previous review over-weighted several editorial preferences. A background opening, an omitted exploratory result, and a contribution sentence that could be sharper are not major defects by themselves. In particular, the old recommendation to add that the treatment effect is concentrated among better performers should **not** be followed: the current results acknowledge a nonsignificant difference between performance gradients.

| Severity | Current count |
|---|---:|
| CRITICAL | 0 |
| MAJOR | 1 |
| MINOR | 4 |

**Score: 7/10.** One material inference problem plus modest clarity and presentation issues. This score is not mechanically comparable with the earlier, more severe scoring convention. Historical findings and optional observations are not added to the counts.

## Rubric scorecard

| Criterion | Current verdict |
|---|---|
| First sentence states the question | Partial: sentence 1 supplies a relevant hook and sentence 2 asks whether responsibility avoidance motivates algorithmic delegation. A two-sentence opening is acceptable, but the reciprocal punishment question remains implicit. |
| Names the method | Yes: preregistered online experiment, total participation, prediction task, matched recipient, algorithm, and between-subject punishment manipulation. The analyzed decision-maker denominator could be clearer. |
| Quantifies the headline result | Yes: the current treatment percentages and 18.3 percentage-point difference agree with the body and the numerical recheck. |
| States a one-sentence contribution | Partial: the reversal communicates a contribution implicitly, while the final sentence only promises discussion of mechanisms. |
| Matches the body and its evidence | Numbers and design description match. The abstract repeats the body's overconfident null interpretation; repetition does not validate it. |

## Current cross-check

The active abstract occupies `manuscript/abstract.tex:1`–`3`; its commented alternatives are excluded. It has approximately **124 words**, counting whitespace-separated tokens after removing comments and `\noindent`, with hyphenated terms counted as one token.

| Abstract claim | Current evidence | Assessment |
|---|---|---|
| Preregistered online experiment with 322 participants | `manuscript/introduction.tex:9`; `manuscript/results.tex:3` | Matches recruitment: 161 participants assigned to each role. The headline delegation analysis includes 159 Player As after two exclusions. |
| Prediction for a matched recipient; algorithm calibrated to perform equally well | `manuscript/design.tex:5`, `67`, `69` | Matches at abstract level. More precisely, algorithm success probability matches measured accuracy over ten initial rounds; this is not an independent guarantee of equal final-prediction accuracy. |
| Between-subject variation in whether punishment is possible | `manuscript/design.tex:5`, `73`, `87` | Matches. Conditional punishment decisions are elicited within subjects in the Punishment condition. |
| Delegation falls from 60.8% to 42.5%, a decrease of 18.3 percentage points | `manuscript/results.tex:9`, `23` | Matches. The independent rechecks documented in [Lens 3](lens_3_methods.md) and [Lens 5](lens_5_robustness.md) give 48/79 versus 34/80, a difference of 18.2595 percentage points; Pearson p ≈ .021 and Fisher p ≈ .0264. The old review's 59.3%, 16.8-point, and p = .033 figures are superseded. |
| Reverses the responsibility-shifting prediction | `manuscript/design.tex:94`, `99`; `manuscript/results.tex:13` | Matches the stated directional hypothesis in this environment. It does not identify which difference from human-intermediary studies causes the reversal. |
| Delegation “offers no protection” | `manuscript/results.tex:49`, `52`, `57` | Too strong for the reported non-rejection; see L1-MAJOR-1. |
| Punishment primarily follows the outcome | `manuscript/results.tex:35`, `49` | Supported as a relative descriptive statement: the average bad-versus-good outcome difference is about £0.20. The accompanying “not on whether ... delegated” should not imply that a delegation effect has been excluded. |
| Candidate mechanisms are discussed | `manuscript/results.tex:59`, `155`; `manuscript/conclusion.tex:9` | Matches. The conclusion now clearly recognizes the limitations of post-decision beliefs and effort proxies. |

No current abstract number has the wrong sign or differs from the main results. The recruitment/analysis sample distinction is a transparency issue, not a fabricated sample size.

## Current findings

### L1-MAJOR-1 — “Offers no protection” turns an imprecise estimate into an absence claim

**Location:** `manuscript/abstract.tex:2`. Related language: `manuscript/introduction.tex:11`, `manuscript/results.tex:57`, and `manuscript/conclusion.tex:6`, `11`.

The active abstract says: “Delegation, in turn, offers no protection.” It then says recipients condition punishment primarily on the outcome, “not on whether the prediction was delegated.” The old “punish ... alike” phrase is now commented out, but the active statement still asserts that protection is absent.

The relevant bad-outcome comparison at `manuscript/results.tex:49` is approximately £0.48 for delegated decisions versus £0.55 for own decisions, with a paired-test p-value of .13. Result 2 (`manuscript/results.tex:52`) correctly says punishment is **not significantly less** under delegation. The independent numerical rechecks in [Lens 3](lens_3_methods.md) and [Lens 5](lens_5_robustness.md), using the 80 Punishment-condition evaluators, give a delegated-minus-own difference of −£0.07125, paired 95% CI [−£0.16414, £0.02164], p = .1308. This interval is review evidence, not an interval currently printed in the manuscript. It remains compatible with a nontrivial reduction in punishment.

The regression interaction in `tables/reg_punishment.tex:17` is −0.103 (SE 0.058). It measures how the delegation difference changes between good and bad outcomes, rather than the bad-outcome delegation difference itself. It should not replace the paired H2 test, but it also does not support treating all delegation-related effects as zero. No active equivalence analysis licenses the absolute abstract claim.

**Revision:** State the inferential result directly, for example: “We find no statistically significant reduction in punishment for delegated predictions after bad outcomes; punishment responds primarily to the realized outcome.” Scope the recipient finding to the condition where punishment is possible. A quantitative version could report the estimated £0.07 reduction and its uncertainty if space permits. Do not reuse the old review's proposed “no less harshly,” which also asserts a directional absence unsupported by a non-rejection.

**Severity rationale:** This changes the interpretation of a central secondary result and its relationship to the responsibility-shifting account. It does not overturn the independently supported treatment effect on delegation, so MAJOR is proportionate.

### L1-MINOR-1 — Distinguish recruitment from the analyzed decision-maker sample

**Location:** `manuscript/abstract.tex:2`; `manuscript/results.tex:3`.

“322 participants” is correct for recruitment, and the matched-recipient design already indicates two roles. Readers can still attach that number to the headline comparison. The current body now discloses the two Player A exclusions, leaving 80 decision-makers in Punishment and 79 in No-Punishment, an improvement over the earlier sample presentation.

**Revision:** If space allows, say “322 recruited participants, including 159 analyzed decision-makers,” or identify the roles and place the analyzed denominator beside the result. The abstract need not reproduce the entire participant-flow note. The old proposed “161 decision-makers and 161 recipients” alone would still leave this distinction unresolved.

### L1-MINOR-2 — End on the bounded contribution rather than only the discussion agenda

**Location:** `manuscript/abstract.tex:3`; `manuscript/introduction.tex:20`; `manuscript/literature.tex:37`.

“We discuss several candidate mechanisms for this reversal” truthfully signals an unresolved mechanism. The reversal already conveys a contribution, so the absence of a separate novelty sentence is not a major defect. Still, closing on what the manipulation establishes would communicate the paper's value more clearly.

**Revision:** Consider a bounded contribution sentence, for example: “In this setting, the possibility of punishment discourages algorithm use even when the algorithm is calibrated to the decision-maker's past performance.” If retaining a “first direct test” claim, use only the scope supported by the literature review. Avoid adding the unestablished claim that punishment selectively discourages delegation among better performers.

### L1-MINOR-3 — Make both empirical questions explicit in the opening

**Location:** `manuscript/abstract.tex:1`; compare `manuscript/introduction.tex:5` and `manuscript/conclusion.tex:4`.

The abstract asks whether a responsibility-avoidance motive extends from human to algorithmic delegation. The paper separately asks whether punishment changes delegation and whether delegation changes punishment. Both results appear later, but framing both questions first would make the design easier to follow.

**Revision:** A compact opening could ask whether the prospect of punishment affects algorithmic delegation and whether delegation, in turn, reduces punishment. Moving the question into sentence 1 is optional; the present background hook is not intrinsically defective. This consolidates the old first-sentence and two-question comments rather than counting them twice.

### L1-MINOR-4 — Keywords omit the central framing term

**Location:** `manuscript/main.tex:79`, `92`.

The title begins with “Accountability,” while the keywords remain “algorithms; delegation; responsibility; punishment; experiment.” Adding “accountability” would align the title, framing, and discovery metadata. The title itself remains accurate and appropriately broad. Further terms such as “algorithm aversion” are optional and should depend on the final framing.

## Disposition of every prior finding

“Superseded” includes corrections to the previous review's recommendation or premise; it does not imply an author revision. Historical severities below are retained only as IDs. Current severities and counts appear above.

| Prior ID | Status | Current disposition |
|---|---|---|
| MAJOR-1: missing contribution sentence | Open, downgraded | The closing still describes discussion (`abstract.tex:3`). L1-MINOR-2 recognizes that the quantified reversal already communicates a contribution. |
| MAJOR-2: “punish ... alike” asserts equivalence | Partially resolved | “Alike” is removed from active abstract text, but “offers no protection” remains (`abstract.tex:2`). L1-MAJOR-1 also rejects the old proposed “no less harshly” wording. |
| MAJOR-3: 322 overstates headline denominator | Partially resolved, downgraded | The body now explains two exclusions (`results.tex:3`); the abstract gives recruitment alone. L1-MINOR-1 uses current analyzed N = 159 rather than old N = 161. |
| MAJOR-4: “adverse outcomes” mischaracterizes human-delegation literature | Superseded | The old assertion that deterministic allocations have “no outcomes” was too strong. Harmful allocations are adverse outcomes in ordinary usage, and the current literature covers other domains too (`literature.tex:7`, `11`). “Harmful decisions” could sharpen the contrast, but no major contradiction is established. |
| MAJOR-5: insert the selection result | Superseded | Current Result 4 is pooled (`results.tex:113`), and `results.tex:109` acknowledges a nonsignificant gradient difference. Omission is acceptable. Do not insert the old claim that the treatment-induced decline is concentrated among better performers. The stronger surviving introduction claim (`introduction.tex:20`) is a body-level issue for other lenses. |
| MINOR-1: first sentence is background | Open, consolidated | The hook remains (`abstract.tex:1`). It is an optional presentation choice, folded into L1-MINOR-3 rather than a separate defect. |
| MINOR-2: punishment result lacks magnitudes | Superseded | A short abstract need not quantify every secondary result. The material need is accurate uncertainty, covered by L1-MAJOR-1; a punishment magnitude is optional. |
| MINOR-3: percentages do not name conditions | Resolved on reassessment | `abstract.tex:2` says punishment reduces delegation from 60.8% to 42.5%; its direction and preceding manipulation sentence make the baseline clear. Both numbers now carry percentage signs. Formal treatment labels are unnecessary. |
| MINOR-4: exceeds AER's approximately 100-word guidance | Not verified as a current journal requirement | Active text is approximately 124 words, not the old 117. This update does not independently reverify current submission rules, so it does not carry forward an unverified mandatory limit or count it as a live defect. Compress for the actual submission target. |
| MINOR-5: replace JEL O33 / add D81 and D83 | Superseded | Codes are unchanged (`main.tex:90`), but the old report did not establish a wrong classification or mandatory alternative. These are editorial choices; no current code defect is counted. |
| MINOR-6: keywords omit accountability | Open | L1-MINOR-4; `main.tex:92` is unchanged. |
| MINOR-7: recipients lacks condition qualifier | Partially resolved, consolidated | “Primarily” softens the wording, and the preceding manipulation supplies context, but the null statement remains unqualified (`abstract.tex:2`). Scope is incorporated in L1-MAJOR-1. Hypothetical No-Punishment responses (`results.tex:57`, footnote) cannot be pooled into a claim about actual sanctions. |
| MINOR-8: abstract asks one question while paper asks two | Open, consolidated | L1-MINOR-3. The empirical questions remain clearer in `introduction.tex:5` than in the abstract. |

## Recommended order

1. Replace the categorical punishment-null claim with a qualified inferential statement.
2. Clarify the recruitment/analysis denominator if the target abstract length permits it.
3. Tighten the opening and closing to state the questions and bounded contribution; add “accountability” to the keywords.

Retain the corrected 60.8%, 42.5%, and 18.3 percentage-point figures. Do not import commented text, historical equivalence analyses, or an unestablished treatment-by-performance claim into the abstract.
