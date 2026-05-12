---
title: "Critical review of results.tex (lines 1–191)"
date: "2026-05-11"
scope: "Preamble + §1 Result 1 + §2 Result 2 + §3 Discussion of results, up to the In-sum paragraph"
---

# 1. Top-level take

The section is structurally sound and the headline numbers are internally consistent. The main weaknesses are (i) one substantive logical tension at the M1 → M2 boundary that the prose currently glosses over rather than confronts, (ii) several paragraphs that try to carry too many independent points at once, and (iii) one orphan paragraph ("Inherent uncertainty") that has no analytical role in its current position. The recommendations below are ordered by how much they would strengthen the section if acted on; a punch list sits at the bottom.

---

# 2. Internal consistency

### 2.1 Numbers — all checks pass

Headline numbers ([results.tex:7](../../manuscript/results.tex#L7)) and downstream references reconcile:

- Delegation share gap: $59.3\% - 42.5\% = 16.8$pp falls inside the
  "16.4 to 19.1pp" AME range claimed at line 24.
- Hypothetical-question footnote at line 7: with 48 No-Punishment
  delegators and 33 non-delegators, $12/48 = 25\%$ and $5/33 = 15.2\%$
  reproduce; new rate $(48-12+5)/81 = 50.6\%$ reproduces.
- Result 2 cell means at line 34 average to a within-subject bad-good
  difference of $(0.5175 - 0.313) = 0.205 \approx \pounds 0.21$ (line 32).
- Diff-in-diff at line 36: $(0.553-0.482) - (0.297-0.329) = 0.103 \approx \pounds 0.10$.
- M4 / line 185: 44 non-delegators ($55\% \times 80$) reproduces; "$45.5\%$ vs $21.7\%$" earns-high in No-Pun vs Pun among non-delegators is consistent with $46$ Pun and $33$ No-Pun non-delegators in the full sample.

### 2.2 Substantive tension: the M1 verdict is more equivocal than the prose admits

This is the most important consistency issue. Two claims sit in the same section without being reconciled:

- **Line 75 (means-level reading):** "Player~As correctly anticipate the relative pattern of punishment in that they expect no significant difference in punishment between delegated and non-delegated decisions… It is this relative-pattern finding---on punishment beliefs alone---that provide no support for a punishment anticipation mechanism for Result~1."
- **Line 94 (within-subject reading):** "Restricting to attention-check passers (Column~(3)) sharpens the relationship substantially: the simple-average belief coefficient is~$2.71$ ($p=0.035$)… The weighted-difference specification (Column~(4)) yields a similar conclusion with a slightly larger coefficient ($3.33$, $p=0.030$), supporting the expected-utility interpretation."
- **Line 114 (verdict):** "Anticipated differential punishment as the driver of delegation is therefore inconsistent with both the elicited beliefs and the realized punishment."

The verdict on line 114 ignores the line-94 regression evidence. Within the Punishment-passers sample, *individual heterogeneity* in belief differences predicts delegation in the direction M1 implies; what fails is the *between-treatment* test (mean belief differences are similar across arms, so beliefs cannot mediate Result 1's treatment gap).

The caveat paragraph at line 73 already makes this distinction ("suggestive evidence on whether the channel is alive among those exposed to it, not as a mediation analysis of the treatment-level delegation gap"). Line 114 should either echo it explicitly or be softened. As written, a careful reader will notice the contradiction and lose trust.

**Suggested rewrite of line 114:**
> "Taken together, the belief evidence is mixed: within the *Punishment* sample, individual heterogeneity in belief differences does predict delegation in the direction M1 predicts (Table~\ref{tab:reg_belief_specs}, Cols.\ 3--4), but this within-arm signal cannot account for the treatment-level gap (Result~1) — mean belief differences are statistically indistinguishable from zero in both arms (Appendix~\ref{appendix:beliefs_vs_performance}), and Player~B does not deliver the asymmetric punishment that would justify the belief asymmetry on which the channel rests (Result~2). M1 is therefore not a viable mechanism for Result~1."

### 2.3 The "Inherent uncertainty" paragraph self-disqualifies

[results.tex:139](../../manuscript/results.tex#L139) ends with: "However, this reasoning would apply to treatment and baseline equally." Since the mechanism it describes cannot, by the paragraph's own admission, explain a treatment difference, the paragraph cannot be a candidate mechanism for Result 1. Two consistent options:

- (a) Demote to a footnote attached to the heterogeneity paragraph at line 116 or to the M2 paragraph at line 120, framed as "a related but orthogonal observation from the literature."
- (b) Cut entirely; the Dietvorst reference can be folded into M2's lead-in if useful.

Currently it disrupts the M1 → M2 → M3 → M4 progression by occupying a paragraph slot without doing analytical work.

### 2.4 Line 135's logical chain is muddled

> "Finding this relationship in the *Punishment* condition only indicates that Player A does not merely avoid directly causing a bad outcome and savoring directly causing a good outcome for Player B. **Instead, it suggests a connection to anticipated punishment**, such that either (i) … or (ii) …. However, neither do we find evidence that … nor do Player~A's punishment beliefs do vary systematically with Player~A's performance."

The paragraph says "it suggests a connection to anticipated punishment" and then immediately rules out the only two ways such a connection could operate. The reader is left wondering whether the "suggestion" is being endorsed or rejected. The intent, I think, is "the asymmetry might look like an anticipated-punishment story, but on closer inspection it isn't, so M2 (process ownership) is the better reading."

**Suggested replacement:**
> "Finding this relationship in the *Punishment* condition only could in principle reflect an anticipated-punishment channel rather than process ownership — specifically, if (i) Player~A expects more severe punishment for delegated decisions when the outcome is good than when it is bad, or (ii) better-performing Player~As hold systematically different punishment beliefs than worse-performing ones. We rule out both: there is no asymmetry in the expected delegation penalty across outcomes ($\Delta^{\text{good}} = \Delta^{\text{bad}}$, $p=0.376$ in the passers sample), and punishment beliefs are uncorrelated with task performance ($|r| \leq 0.21$, none significant; see Appendix~\ref{appendix:beliefs_vs_performance}). The heterogeneity therefore reflects preferences over who acts, not over how Player~A is punished."

---

# 3. Evidence backing

### 3.1 Claims with weak or missing evidential support

- **Line 7 footnote ("Yates correction" question):** an unresolved methodological choice on the headline test. Worth nailing down before submission — the difference between Yates and no-correction is small at $n \approx 160$ but the reviewer will check.
- **Line 7 ("one-sided vs two-sided" question):** unresolved. The preregistration framing should drive this; if the preregistration is non-directional, the two-sided test is correct and the prose at line 63 ("the observed effect points in the opposite direction") becomes a reportable but not directional finding.
- **Line 65 ("Most notably, our task departs…")**: the argument that prior-literature settings differ from ours is plausible but cites four papers without saying what specifically transfers and what doesn't. Worth one sentence sharpening which feature of dictator games (full information, certain mapping from action to allocation, etc.) is being contrasted against our prediction task.
- **Line 75 (overestimation pattern)**: described as one of "two patterns" but plays *no analytical role* in any downstream argument; the M1 verdict rests entirely on the *relative*-pattern claim, not on the levels. The author's own inline comment ("Let's consider to just leave out the hypothetical punishment beliefs. We do not do anything with them") points the same way. Either give the levels finding an analytical purpose (e.g., it's evidence about subjects' calibration of punishment magnitudes, distinct from M1) or downgrade it to a sentence in the figure caption.
- **Line 88 ("Player~A's elicited probability of producing the high payoff as the weight"):** `wa_confidence` is the expected score in the *first ten rounds*, on a 0–10 scale. Dividing by 10 gives the expected fraction correct, which is only the probability of producing the high payoff on the *final prediction* under the assumption that final-round difficulty matches average rounds-1–10 difficulty. Worth a short clarifying footnote or rephrasing.
- **Line 120 ("process ownership being behaviourally consequential only when Player~B's payoff is at meaningful third-party stake"):** Steffel (2016) is cited, but Steffel's setting is about delegating *decisions* through agents — whether her finding specifically supports "stake-conditional activation" of process ownership is worth verifying. If it doesn't, weaken to "consistent with the broader psychological-ownership literature, in which intensity of caring tracks the size of the stake."
- **Line 122:** repeats line 120's claim. As I flagged in the C3 round, this paragraph should add a *new* point (blame avoidance would predict the opposite gradient) or be cut.
- **Line 185 (effort analysis):** the round-11 evidence is presented as a single integrated paragraph but actually contains *two* independent pieces of evidence — (a) within-subject improvement is concentrated in No-Pun, not Pun; (b) cross-section non-delegator round-11 success is higher in No-Pun. These are mutually reinforcing but distinct. Splitting helps readability.

### 3.2 Claims with appropriate backing

- Result 1 (line 7): three concordant tests + a within-subject corroborator.
- Result 2 (line 32–36): one-sample tests, paired test, regression, robustness on passers, ruling out belief-about-performance as confound.
- Line 116 heterogeneity claim: Table 1 + scatter figure + appendix correlations.
- Line 141 (M3): figure + claim about balance is supported by appendix table.
- Line 187 conclusion / line 191 In-sum: the M3 and M4 verdicts are well-supported. M1's verdict is the weak link (§2.2 above).

---

# 4. Section-level flow

### 4.1 Preamble → Result 1 → Result 2 → Discussion

This top-level arc is clean: present each main finding, then discuss mechanisms.

The Result 2 closing line at 51 ("This non-result also bears on Result 1: Any treatment difference in delegation frequencies motivated by punishment avoidance would not be consistent with actual punishment behavior of Player~B") explicitly bridges Result 2 → Discussion. Good.

One issue: the bridge sentence pre-empts the M1 ruling-out exercise (lines 69–114). By the time we reach M1 in the discussion, the reader has already been told the answer. Two ways to handle:

- (a) Keep the bridge sentence but soften: "We return to this point below when discussing whether punishment anticipation can rationalise Result~1."
- (b) Cut the bridge sentence and let the M1 paragraph open the discussion of the connection.

(a) is the lighter touch.

### 4.2 Within the Discussion: mechanism order

Current sequence:
1. Preamble (line 63)
2. Departures from prior settings (line 65) — orphan, not an M
3. **(M1) Anticipated differential punishment** (line 69) — ruled out
4. **Heterogeneity by performance** (line 116) — empirical setup for M2
5. Feier contrast (line 118)
6. **(M2) Process ownership** (line 120) — surviving
7. Belief-mediated alternatives ruled out (line 135) — defending M2
8. Inherent uncertainty (line 139) — orphan
9. **(M3) Performance differences** (line 141) — ruled out as artefact
10. **(M4) Effort exertion** (line 181) — ruled out
11. **In sum** (line 191)

Three structural recommendations:

**(a) Re-home "Departures from prior settings".** The paragraph (line 65) explains *why* prior-literature settings might predict different things from our setting. It currently sits between the preamble and M1 without an M label. Two cleaner homes:

- Move it to the end of Result 2 / start of the Discussion as the *transition* paragraph, framed as "before turning to candidate mechanisms, we note that our setting departs from the prior literature in ways that complicate a direct comparison." This makes it explicitly preliminary and removes the "non-M paragraph in the M sequence" issue.
- Or fold it into M1 as a paragraph explaining why M1 might be muted in our setting relative to dictator-game studies.

**(b) Merge Heterogeneity + Feier + M2 + line-135 ruling-out into a single M2 sub-section.** Right now M2 is split across four paragraphs (116, 118, 120, 135) with a figure (124–133) in the middle and an unlabelled paragraph (122) that repeats line 120. Reorganised:
- **(M2) Process ownership.** Open with the heterogeneity finding (current line 116). Add the Feier contrast (current line 118) as a sentence or footnote — it's a comparator, not a new paragraph. Move into the process-ownership interpretation (current line 120). Add the "blame avoidance gives the opposite gradient" disambiguation (per the C3 suggestion in mechanism_followup.md). Close with the belief-mediated alternatives being ruled out (current line 135), making explicit that this is defensive work for M2.

**(c) Demote or cut "Inherent uncertainty"** (line 139), as flagged in §2.3.

After these moves, the discussion would read:
1. Transition (with Departures paragraph or a one-paragraph framing): we consider four candidate mechanisms.
2. **(M1) Anticipated differential punishment** — ruled out (with the line-114 fix in §2.2).
3. **(M2) Process ownership of the outcome** — supported (merged paragraphs).
4. **(M3) Performance differences across conditions** — ruled out (artefact check).
5. **(M4) Effort exertion** — ruled out.
6. **In sum.**

### 4.3 Two figures for the same content (line 143 vs line 156)

[results.tex:143](../../manuscript/results.tex#L143) shows the simple `figures/performance.png` (performance balance). [results.tex:156](../../manuscript/results.tex#L156) shows the augmented `figures/performance_by_delegation.png`. The author's inline comment at 154 ("Alternative figure") suggests this is intentional in-flight. The recommendation: keep `performance_by_delegation.png` because it carries M2's headline evidence, and either (i) drop `performance.png` entirely (the balance claim can be stated in text with two means and a p-value), or (ii) keep both with `performance.png` moved to the appendix as the formal balance-test figure. Two adjacent figures saying overlapping things is the worse option.

---

# 5. Paragraph-to-paragraph flow

Going through transitions:

| Lines | Transition | Issue |
|-------|------------|-------|
| 3 → 5 | Preamble → Result 1 | Clean, no transition needed |
| 7 → 24 | Headline → With controls | "Next, we examine the robustness…" — good |
| 24 → 30 | Result 1 close → Result 2 open | "Next, we turn to Player~B's punishment behavior…" — good but minimal |
| 30 → 32 | Result 2 setup → first analytical claim | Bridge sentence at line 30 reads as a header more than a paragraph; consider folding into line 32 |
| 32 → 34 | "punishment is positive and bad>good" → "conditional on outcome, no asymmetry" | Strong — "Conditional on the outcome, however…" |
| 36 → 51 | Diff-in-diff → bridge to Discussion | Sentence at 51 is good; but as flagged in §4.1, it pre-empts M1 |
| 51 → 61 | Result 2 close → Discussion opens | The §3 header at 61 + preamble at 63 do the work; good |
| 63 → 65 | Discussion preamble → Departures from prior settings | Unclear why Departures comes here; see §4.2(a) |
| 65 → 67 → 69 | Departures → consistency-but-not-reversal aside → M1 | The aside at 67 is a two-sentence bridge; would read better merged into 65 or 69 |
| 69 → 71 | M1 header → Punishment beliefs sub-section | "After making the delegation decision but before learning the outcome, we elicited…" — fine |
| 71 → 73 → 75 | Setup → caveats → results | The caveat paragraph at 73 is good but is heavy machinery for one regression; consider compressing |
| 75 → 88 | Belief patterns → regression intro | "Even though the belief measure was not incentivized…" — good logical bridge |
| 88 → 94 → 96 → 114 | Table → interpretation → decomposition footnote → M1 verdict | Two-difference-decomposition paragraph (96–97) should become a footnote per the inline comment; the M1 verdict at 114 needs the §2.2 fix |
| 114 → 116 | M1 verdict → Heterogeneity | "The regression framework also lets us explore which other factors influence…" — abrupt; reader has just been told M1 is dead and now jumps to a new exhibit. A sentence like "We now turn to a second feature of the delegation decision that motivates a different mechanism" would help |
| 116 → 118 → 120 | Heterogeneity → Feier → M2 | Acceptable but argues for the §4.2(b) merge |
| 120 → 122 → 135 | M2 → restatement → ruling-out | 122 is redundant; 135's logic chain is muddled (§2.4) |
| 135 → 139 → 141 | Ruling-out → Inherent uncertainty → M3 | Two transitions broken: Inherent uncertainty doesn't follow from 135, and M3 doesn't follow from Inherent uncertainty. Cutting 139 fixes both |
| 141 → 181 | M3 → M4 | Two figures (performance, performance_by_delegation) sit between; transition is implicit. A sentence at 181 like "A separate concern is that punishment may motivate Player~A not to delegate but to exert greater effort herself…" would soften the jump |
| 187 → 191 | M4 close → In sum | "\medskip" alone; consider adding a sentence "Taken together…" before the In-sum paragraph, or letting the section header guide the reader |

---

# 6. Intra-paragraph structure (worst offenders)

### 6.1 Headline paragraph (line 7) — 5+ topics in one paragraph

Currently mixes (i) the headline shares, (ii) the figure reference, (iii) statistical tests, (iv) a long footnote about a hypothetical within-subject test, (v) two inline methodological queries, (vi) the "$50\%$ delegation suggests subjects find the design credible" claim. Suggested split:

- Paragraph 1 (Headline): shares + figure + Pearson/Fisher tests + within-subject footnote.
- Paragraph 2 (Calibration): "Delegation shares around $50\%$ also suggest that subjects, on average, find the equal relative performance information conveyed by the design credible…". This claim is about design credibility, not about Result 1, and is currently buried.

### 6.2 Two-patterns paragraph (line 75) — first pattern is decorative

The "First, … overestimate the level of punishment" finding (current line 75 first half) does no analytical work downstream. Either:

- Cut it and lead directly with the relative-pattern finding, or
- Move it to a one-sentence figure caption note, or
- Give it an analytical role (e.g., evidence that subjects calibrate punishment levels poorly, which is informative about the experimental setting but not M1).

### 6.3 Regression interpretation paragraph (line 94) — last sentence sits awkwardly

The closing sentence — "If taken at face value this would mean that the delegation decision is primarily made by thinking about punishment consequences after a good outcome, rather than a bad outcome." — sits at the *end* of the regression interpretation but reads as a stand-alone interpretive claim that contradicts the M1 verdict to come at line 114. Either it belongs in the M1 verdict paragraph (as a hedge: "if anything, the M1 story is strongest in the good-outcome cell") or it should be cut and the same point made in §2.2's suggested rewrite.

### 6.4 Belief-mediated-alternatives paragraph (line 135) — one long sentence, muddled logic

See §2.4 above. The fix is structural, not just stylistic.

### 6.5 Effort-exertion analytical paragraph (line 185) — two distinct findings packed together

Current contents in one paragraph:
1. The differential round-1–10 → round-11 improvement (No-Pun improves, Pun doesn't).
2. The cross-section non-delegator round-11 success rate ($45.5\%$ vs $21.7\%$).
3. The reassurance that (2) isn't driven by ex-ante differences ($3.12$ vs $2.98$, $p=0.66$).
4. A footnote on delegator-side performance.

These are mutually reinforcing but conceptually distinct. A two-paragraph version reads more easily:

- Para A: improvement-from-rounds-1–10 evidence (within-subject).
- Para B: non-delegator success rate evidence (cross-section).

---

# 7. Minor issues (typos, prose)

- **Line 67:** "obsrvation" → "observation".
- **Line 75:** "It is this relative-pattern finding … that provide no support" → "that provides no support" (subject "finding" is singular).
- **Line 75:** "Two patterns emerge. First, … Second, however," — the "however" implies the two patterns are in tension, but they're independent observations on different objects (levels vs. relative). Drop "however".
- **Line 135:** "nor do Player~A's punishment beliefs do vary" → double "do"; should read "nor do Player~A's punishment beliefs vary".
- **Line 24:** "Including a control for the random order in which the two delegation options appeared on the screen in leaves the treatment coefficient essentially unchanged" — extra "in" before "leaves".
- **Line 51:** trailing `\\` at end of line — gratuitous, can be removed.
- **Line 70 → 71 transition:** the M1 paragraph (line 69) ends "In either case, delegation behavior should be consistent with observed beliefs about punishment." The next paragraph (line 71) opens with "After making the delegation decision but before learning the outcome, we elicited…". The transition flows but the *Punishment beliefs* heading interrupts and creates the impression of a new section rather than M1's empirical test. Consider removing the heading at line 71 and letting the prose continue inside the M1 \paragraph.
- **Line 92:** inline `[Comment: Maybe for consistency, include also here the marginal effect at the bottom, even thou now it would be for different variables.]` — the marginal effect for the simple-average belief difference would be in *probability per pound* units, comparable in spirit to the main table's AME; if the table is the prominent one for the M1 verdict, the AME row would help the reader. Worth doing.

---

# 8. Punch list (priority order)

1. **Fix the M1 verdict on line 114** to acknowledge the within-Punishment regression evidence (§2.2 suggested rewrite). Highest priority — currently the only place in the section where the prose contradicts its own evidence.
2. **Cut or relocate "Inherent uncertainty"** (line 139) (§2.3).
3. **Rewrite the muddled paragraph at line 135** along the lines of §2.4.
4. **Reorganise the M2 sub-section** (lines 116, 118, 120, 122, 135) into a single sequence with one clear thesis paragraph + supporting evidence + defensive ruling-out (§4.2(b)).
5. **Re-home or fold "Departures from prior settings"** (line 65) — either at the section transition or inside M1 (§4.2(a)).
6. **Split the headline paragraph** (line 7) into Headline + Calibration (§6.1).
7. **Split the effort paragraph** (line 185) into within-subject improvement + cross-section non-delegator success (§6.5).
8. **Cut the redundant restatement at line 122** and replace with the blame-avoidance disambiguation (already covered in mechanism_followup.md C3).
9. **Decide on `performance.png` vs `performance_by_delegation.png`** — one in body, one in appendix, or just the augmented one (§4.3).
10. **Resolve the methodological queries on line 7** (Yates correction; one-sided vs two-sided).
11. **Decide the fate of the line-75 levels-finding** (decorative or analytical) (§6.2).
12. **Demote the two-difference decomposition paragraph (line 96–97) to a footnote** (already noted in the inline comment).
13. **Cosmetic typos** (§7).
