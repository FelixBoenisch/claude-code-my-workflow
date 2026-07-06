---
title: "Proposal: structure and narrative for the 'Discussion of results' subsection"
date: "2026-07-02"
scope: "manuscript/results.tex, subsection 'Discussion of results' (\\label{sec:mechanism}, lines 61–204) + material to absorb from subsection 'Other' (lines 206–216)"
status: "PROPOSAL — no manuscript edits made; drafting to proceed theme by theme after sign-off"
---

# 0. What this document is

A structural and narrative proposal for the "Discussion of results" subsection, based on a full read of the manuscript (introduction, literature, design, results, conclusion, appendix — treating abstract/intro/conclusion and the current discussion draft as outdated), the May reviews (`mechanism_section_review.md`, `mechanism_followup.md`, `beliefs_comments_thoughts.md`), and the restructure plan. Section 1 states the subsection's job; Section 2 the narrative arc; Section 3 the block-by-block structure with content decisions; Section 4 cross-cutting decisions and consistency flags; Section 5 the proposed step-by-step drafting sequence; Section 6 the decision points needing Felix's call.

---

# 1. The job of the subsection

After Result 1 (punishment possibility *reduces* delegation, 42.5% vs. 59.3%) and Result 2 (conditional on outcome, no detectable punishment differential between delegated and self-made decisions), the subsection must do four things, in this order of importance:

1. **Confront the reversal.** H1 predicted the opposite sign. The reader needs a disciplined answer to "why?", not a definitive one — the section's credibility rests on systematic elimination, honest verdicts, and explicit epistemic status (exploratory; two analyses pre-stated as secondary in the preregistration).
2. **State the puzzle sharply.** The two results are individually interpretable but *jointly* puzzling: the prospect of punishment changes Player A's delegation behavior even though neither realized punishment (Result 2) nor Player A's beliefs about punishment attach any *delegation-specific* penalty. Punishment matters without a punishment-contingent reason attached to delegation as such. This is the hook the whole subsection hangs on.
3. **Weigh candidate mechanisms without overclaiming.** Process ownership should come out as *the only candidate not contradicted by the data* — explicitly not as an established mechanism. (Consistent with Felix's standing position: process ownership is one candidate, not the preferred one; experimenter demand cannot be excluded by design.)
4. **Reconcile with the closest precedent.** The apparent tension with feier_hiding_2022 must be dissolved here (not in "Other"), and the two-channel synthesis (internal felt responsibility vs. external accountability) is the intellectual payoff that positions the paper in the recent algorithmic-delegation literature.

**What the subsection is NOT for:** re-reviewing the literature (that is Section 2's job — discussion references should interpret *our* results against it), re-reporting Results 1–2, or housing robustness material that belongs with the results themselves (order effects, power).

---

# 2. The narrative arc (one paragraph)

> The canonical responsibility-shifting force was imported from settings whose features — transparent selfish intent, certainty, misaligned incentives — our design deliberately lacks; its absence can rationalize a *null*, but the observed *reversal* requires a countervailing force that actively discourages delegation when punishment is possible. We evaluate candidates systematically: the reversal is not a composition artifact (performance and confidence are balanced across arms); it is not driven by anticipated differential punishment (beliefs show no delegation-specific asymmetry on average — correctly so, given Player B's behavior — even though belief *heterogeneity* does predict delegation at the margin among attentive subjects); and it is not an effort response (improvement on the final prediction is concentrated in the *No-Punishment* arm, the opposite of what an outperform-the-algorithm story implies). What survives is a preference over *who produces the outcome*: better performers refuse to delegate specifically when punishment is possible, a gradient that expected utility rules out by construction (individual-level calibration), that is not mediated by beliefs, and that runs on actual rather than perceived performance. We read this as suggestive of stake-conditional process ownership — the desire to personally deliver the good outcome when the recipient can hold you to account — while being explicit that the evidence is an exploratory heterogeneity pattern and that an experimenter-demand account is observationally similar. Finally, our findings and feier_hiding_2022's are not in tension but complementary: their design identifies a signal-extraction channel that ours closes by construction, and the two studies jointly suggest that algorithms shield the principal's internal moral burden far better than her external accountability.

---

# 3. Proposed structure, block by block

Current order: Departures → Anticipated punishment → Beliefs (caveats, figure, table, decomposition, summary) → Heterogeneity → **Process ownership** → belief-mediation checks → Uncertainty → **Balance (M3)** → **Effort (M4)** → In sum → Two channels. Problems: the survivor (process ownership) is buried mid-section; the artifact check arrives *after* the reader has been asked to interpret heterogeneity; "Inherent uncertainty" dangles as an undispatched candidate; the Feier reconciliation sits in "Other"; experimenter demand is missing from the weighing.

Proposed order — dispatch the mechanical explanation first, then the two instrumental channels (anticipation, effort), and let the preference-based account close as the survivor:

### Block 1 — Opening frame (2 short paragraphs, no header)

- **Para 1:** Result 1 does not merely fail to support H1; it reverses it. Then the puzzle sentence (job #2 above): punishment changes behavior although neither realized punishment nor beliefs attach a differential penalty to delegating as such.
- **Para 2 (epistemic status + roadmap):** Because the effect reverses the preregistered direction, all analyses in this subsection are interpretive/exploratory; two were pre-stated as secondary analyses in the preregistration (the role of own performance and beliefs about it; the consistency of punishment beliefs with delegation) — cite Appendix `appendix:preregistration`. One roadmap sentence naming the candidates in the order they appear.
- Replaces the current unfinished opening sentence (line 63).

### Block 2 — `\paragraph{Departures from canonical settings.}`

- **Role:** explain why H1's imported force may be weak here → *this rationalizes a null, not a reversal* → pivot sentence: "The remainder of this section therefore asks what actively discourages delegation when punishment is possible."
- Keep: dictator-game contrast (transparent intent, self-interest, certainty) vs. our task (uncertainty, aligned incentives, effortful prediction); the "prediction under uncertainty is precisely the algorithmic domain" defense. This also redeems the design section's promise ("implications … are taken up in Section 5") — make that link explicit.
- **Change (per Felix's inline comment):** drop the dependence on beliefs ("it would be reflected in punishment beliefs") — the story stands on design differences alone; the flat realized punishment (Result 2) is corroborating, not load-bearing.
- **FB comment "recent literature on responsibility avoidance via delegation to algorithms?"** — recommendation: do *not* import tontrup/chevrier/hueholt here; they belong in Block 8 where they sharpen and then resolve the puzzle (Hueholt et al. find *more* AI delegation when moral stakes become real — the internal channel). A single forward-pointing clause here suffices ("we return to the recent algorithmic-delegation evidence below").
- Fix typo "obsrvation" (line 69) when drafting.

### Block 3 — `\paragraph{No composition artifact.}` (short)

- **Role:** quick kill of the mechanical explanation before behavioral channels. Absorbs current "(M3) Performance differences and overconfidence across conditions."
- Content: performance in rounds 1–10 balanced (mean 2.93/10, indistinguishable across arms); overconfidence present but balanced; treatment effect robust to performance and confidence controls (Table `tab:del_decision_determinants`, cols. 3–4 — already established in the Result 1 part, so one pointer sentence, not a re-argument).
- Figure decision (see §4.3): `fig:performance` can move to the appendix if `fig:performance_by_delegation` stays in the body.

### Block 4 — `\paragraph{Anticipated differential punishment.}` + `\paragraph{Punishment beliefs.}` (keep two headers; this is the longest block)

- **Statement of the channel:** the natural reading — A expects harsher punishment for delegated decisions (anchor: gogoll_rage_2018, bigman_people_2018, jauernig_people_2022, bonnefon_moral_2024) — plus the shirking variant (extra punishment for outsourcing the effort). Optional one-sentence third variant: A caters to B's *procedural* preference for a human decision, which punishment makes enforceable — observationally it collapses into the same belief asymmetry, so it is testable with the same data. (Decision point D5.)
- **A useful identification sentence to add:** because the algorithm reproduces A's own success probability (and this is common knowledge), outcome-contingent punishment affects both options symmetrically; *only a delegation-contingent asymmetry in expected punishment could tilt the choice*. This justifies why the belief *difference* is the operative statistic and why overestimated *levels* (which apply to both options) cannot drive Result 1.
- **Caveats paragraph (line 77):** keep essentially as is — it is honest and structurally motivated (unincentivized, post-decision, hedging/rationalization, hypotheticality, Punishment-condition restriction, "suggestive not mediation"). It is also the version already reviewed and settled in May (`beliefs_comments_thoughts.md`); don't reopen.
- **Evidence, in this order:**
  1. Levels: A overestimates punishment in every cell (fig `realized_vs_anticipated`) — but by the identification sentence, levels cancel across options.
  2. Relative pattern: no delegation-specific asymmetry on average (diff-of-diffs +0.08, p>0.32; appendix pointer) — and this matches Player B's actual behavior (Result 2). *This is the load-bearing null.*
  3. Within-subject heterogeneity (Table `tab:reg_belief_specs`): among attention-check passers, subjects who expect a larger penalty for *not* delegating delegate more (simple avg 2.71, p=0.035; weighted 3.33, p=0.030; good-outcome difference carries it: 1.58, p=0.033). Honest framing: the channel is *alive at the margin* among attentive subjects, unconditionally weak — and a margin with a zero mean cannot generate a 17-point treatment-level gap.
- **Verdict sentence (sample):** "Anticipated differential punishment is thus at most a margin along which subjects differ, not a force that could reverse the average delegation decision: the asymmetry it requires is absent from beliefs on average, absent from Player B's realized punishment — whose point estimate, if anything, runs in the opposite direction — and therefore unavailable to push delegation down in the aggregate."
- **Cuts/demotions within this block:**
  - "Interpretation of the two-difference decomposition" paragraph (line 100) → footnote, as Felix already flagged. Agreed.
  - Commented-out `belief_distributions` figure + paragraph (lines 103–116) → leave out entirely. The regression table carries the same information; the single-significant-cell story is fragile and invites over-reading.
  - Blue bars (hypothetical No-Punishment beliefs) in `fig:realized_vs_anticipated`: **recommend KEEP, with a repurposed one-sentence role** — see decision point D2.

### Block 5 — `\paragraph{Effort to outperform the algorithm.}` (short)

- Keep the current logic and evidence; tighten. The channel's punishment link, stated crisply: if A believes effort on the final prediction can lift her success probability above the calibrated algorithm's, punishing outcomes makes self-deciding strictly better in expected-punishment terms.
- Evidence: improvement from rounds 1–10 to round 11 is concentrated among *No-Punishment* non-delegators; 45.5% vs. 21.7% high payoff among non-delegators; same final image across arms; ex-ante scores of non-delegators balanced (3.12 vs. 2.98, p=0.66).
- Add one hedging clause: cross-arm comparisons among non-delegators condition on an endogenous choice, so equal ex-ante scores are reassuring but do not fully rule out selection on unobservables. (Referee-proofing; one clause, not a paragraph.)
- The delegator-composition footnote currently here (2.47 vs. 3.06, p=0.039; passers 2.38 vs. 2.98, p=0.080) **moves to Block 6**, where it is evidence *for* the selection story rather than an aside.

### Block 6 — `\paragraph{Selection on performance and process ownership.}` (the survivor; merges current "Heterogeneity by performance" + "(M2) Process ownership" + the belief-mediation checks + "Inherent uncertainty")

Internal order — evidence first, interpretation second, alternatives third:

1. **The gradient (descriptive, hedged):** within *Punishment*, better performers delegate less (Pearson r=−0.19, p=0.092, passers — describe as "modest" / "marginally significant"; never "strong"); no comparable gradient in *No-Punishment*. Figure(s): see §4.3.
2. **The composition fact (moved from Block 5's footnote into text):** delegators under Punishment score 2.47/10 vs. 3.06/10 under No-Punishment — the extra ~17 points of delegation in *No-Punishment* come disproportionately from mid/upper performers, i.e., exactly the subjects who refuse to delegate when punishment is possible.
3. **Why the gradient is informative (Feier contrast, keep current paragraph):** population-level calibration in feier_hiding_2022 makes a performance→delegation gradient expected-utility-rational; individual-level, common-knowledge calibration makes EU predict *no* gradient — so the observed one reflects preferences (or misperception), not rational relative-ability updating.
4. **Not belief-mediated (keep, with appendix footnote):** no good/bad asymmetry in the expected delegation penalty (p≈0.38); punishment beliefs uncorrelated with performance (|r|≤0.21, none significant) → the gradient cannot be re-routed through the anticipation channel.
5. **Not (mis)perceived ability:** perceived performance does not discriminate delegators from non-delegators under Punishment (4.69 vs. 4.71) while actual performance does (2.38 vs. 3.00) — delegators are not subjects who *believe* they are worse; they are subjects who *are* worse. (Currently only in the `performance_by_delegation` caption — promote one sentence to the text; it is one of the strongest facts for the preference reading.)
6. **Interpretation:** stake-conditional process ownership — the value of being the proximate cause of the good outcome, behaviorally consequential only when B holds an enforcement role. Keep the current careful formulation ("does not require anticipating differential punishment; the elicited beliefs show no such asymmetry").
7. **Alternative reading of the gradient — inherent uncertainty (dietvorst_people_2020):** demote from standalone `\paragraph` to 2–3 sentences here (or a footnote): higher own success probability ⇒ outcome uncertainty closer to its maximum ⇒ Dietvorst-style aversion predicts less delegation — but the preference is condition-invariant and thus explains neither Result 1 nor the *arm-specificity* of the gradient. Framing it as "fails the same arm-specificity test" makes it a dispatch, not a dangling candidate. (Decision point D4.)
8. **Demand caveat (1–2 sentences + pointer):** the punishment screen could itself cue direct engagement; the design cannot separate this from process ownership; full treatment (direction ambiguity, de_quidt_measuring_2018 probe) stays in the Conclusion. This restores the missing fifth candidate (May review, F6) without duplicating the Conclusion.

**Citation re-anchoring (important — see §4.4):** steffel_passing_2016 is currently the anchor for "utility from being the proximate cause of a good outcome." Steffel et al.'s own asymmetry runs the other way (blame-avoidance > credit-seeking; delegation *increases* for potentially blameworthy choices). Keep Steffel for the two-mediator decomposition in Block 8 (that use is accurate); re-anchor the process-ownership preference here to the decision-rights/control literature — candidates to verify and add to the bib: Bartling, Fehr & Herz (2014, *Econometrica*, intrinsic value of decision rights), Owens, Grossman & Fackler (2014, *AEJ: Micro*, control premium); optionally benabou_identity_2011 (already in the bib) for the self-image side. **Verify before citing** (e.g., `/verify-claims`); none of the first two is currently in `ProjectAlgorithm.bib`.

### Block 7 — `\paragraph{Taking stock.}` (replaces "In sum")

- Systematic verdict list using **descriptive names, not M-numbers** (see §4.1): composition artifact — contradicted (balance); punishment anticipation — the required average asymmetry is absent from beliefs and from realized punishment; effort — the round-11 pattern runs opposite; process ownership — the only candidate not contradicted, supported by the arm-specific gradient and delegator composition; experimenter demand — not separately identifiable from process ownership with this design.
- **Tone (this is where Felix's skepticism must bind):** "the most consistent reading of the data we have, not a confirmed mechanism"; evidence = one exploratory heterogeneity pattern in a ~60-subject subsample plus a delegator-composition comparison. Avoid "the data support M2" phrasing; prefer "not contradicted / most consistent among the candidates we can evaluate."
- Optional connective sentence (decision point D6): the good-outcome belief difference is the one that predicts delegation (Table `tab:reg_belief_specs`, col. 5) — consistent with the good-outcome state being the locus of the decision, as the process-ownership reading independently implies. Suggestive glue; flag as such or omit.

### Block 8 — `\paragraph{Relation to prior evidence.}` (moved from "Other"; merges "Reconciling with feier_hiding_2022" + "Two channels of responsibility-shifting")

1. **Feier reconciliation (trimmed from the current Other version):** the two contrasts are not contradictions. (i) Their punishment differential is plausibly signal extraction (delegation reveals self-perceived relative ability under session-level calibration); our individual-level, common-knowledge calibration closes that channel by construction, so the disappearance of the differential is consistent with — not a refutation of — their result. (ii) Their design compares delegate types with punishment always available; ours compares punishment regimes — different treatments, so the "natural prediction" from their findings was never directly tested by them (this is Felix's own inline comment; make it one clean sentence). Keep the honest closer: which design feature causes the sign reversal cannot be resolved without varying calibration directly.
   - Handle Felix's second inline comment ("relative-performance concern applies to both treatments") — in our design it applies to *neither* arm (closed by construction in both), so it cannot generate a between-arm delegation difference; it explains why our *levels* and Feier's are hard to compare, not a within-paper confound. State this in a footnote if at all.
2. **Two-channel synthesis (keep — this is the payoff paragraph):** Steffel's decomposition (felt responsibility vs. anticipated blame); hueholt_trusting_2026 shows the internal channel (more AI delegation when moral consequences become real); our Results 1–2 speak to the external channel (delegation falls when third-party punishment is possible; punishment tracks outcomes, not delegation). Closing line: AI is a strong shield against the principal's internal moral burden but a weak shield against external accountability — channels conflated with human delegates, separable with algorithmic ones.
3. **Compress** the "expanding map" material (chevrier_algorithm_2024, kobis_delegation_2025, unified-design future work) to one or two sentences with a pointer to the Conclusion — the current two-paragraph version in "Other" overlaps the literature section.

---

# 4. Cross-cutting decisions and consistency flags

### 4.1 Drop the M-numbering (recommended)

The M-labels have drifted across files and are now mutually inconsistent:
- `results.tex` In-sum: M1 anticipation, M2 process ownership, M3 performance differences, M4 effort.
- `conclusion.tex` (outdated): "upper bound on the contribution of M4" where M4 = *demand*.
- `appendix.tex` preregistration table (outdated): "M2/M3" for the secondary analyses and "M1 (process ownership) and M4 (experimenter demand)" — three different schemes in one repo.
- Felix's own memory/feedback refers to process ownership as "M3" from an earlier numbering.

Recommendation: use descriptive names in prose ("punishment anticipation", "effort", "process ownership", "composition artifact", "experimenter demand") and reserve enumeration for the Taking-stock paragraph if needed. Whatever is chosen must be propagated to intro/conclusion/appendix in the later sync pass (they are outdated anyway; add to the sync checklist).

### 4.2 Epistemic status, stated once

One sentence in Block 1 (exploratory; two pre-stated secondary analyses), rather than repeated hedging in every block. The preregistration appendix table must then be brought in line (its current M-labels misattribute which analyses were pre-stated).

### 4.3 Figures — three performance figures is too many

Currently in/near the subsection: `fig:performance` (balance), `fig:performance_delegation_scatter` (gradient), `fig:performance_by_delegation` (distributions by arm × delegation + confidence). Recommendation (decision point D3):
- Body keeps **`fig:performance_by_delegation`** — it carries the gradient's composition story *and* the perceived-vs-actual dissociation, the two facts Block 6 leans on.
- `fig:performance` → appendix (balance is also documented by the regression controls and the appendix balance table).
- `fig:performance_delegation_scatter` → appendix (the r=−0.19/p=0.092 gradient is honestly weak as a visual; report it in text, keep the scatter available for referees).
- `fig:realized_vs_anticipated` and `tab:reg_belief_specs` stay in the body (Block 4).

### 4.4 Steffel re-anchoring (Block 6) — flagged above; verify-then-add

Felix's inline comment already questions the Steffel fit. Concrete proposal: (i) keep steffel_passing_2016 only for the Block-8 decomposition; (ii) verify and add Bartling–Fehr–Herz 2014 and/or Owens–Grossman–Fackler 2014 as the preference anchor in Block 6; (iii) if verification does not pan out, fall back to Felix's own suggested hedge ("consistent with the broader psychological-ownership literature, in which the intensity of caring tracks the size of the stake").

### 4.5 Consistency flags to fix while drafting (not blocking)

- **p-value discrepancy:** bad-outcome punishment gap paired t-test is p=0.13 in `results.tex` (line 45) but p=0.153 in `appendix.tex`/`conclusion.tex` — likely full vs. passers samples; make the sample explicit wherever cited.
- **Result 2 tone:** the discussion must say "we cannot reject equal punishment" (intro/abstract framing, MDE appendix), never "there is no difference." The Feier block inherits this.
- **"borderline significant (p=0.08)"** for the Delegated×Bad interaction: fine in the Results part, but the discussion should not lean on it in one direction while dismissing p=0.09 elsewhere — apply one standard for "marginal."
- Spelling/style: "obsrvation" (line 69); unify "unincentivised/unincentivized" (BE/AE mixed); "Player~As" pluralization used consistently.
- Line 49 comment (determinants of punishment per cell / belief-independence of punishment) is Result-2-section business, not Discussion — park it there.
- Order effects + power paragraphs (in "Other"): move to Result 1 robustness footnote / appendix respectively; after Block 8 absorbs the Feier material, subsection "Other" can be dissolved.
- Per Felix's earlier note: do **not** discuss the deservingness/inequality motive.

---

# 5. Proposed drafting sequence (one theme per step)

| Step | Block | Deliverable |
|------|-------|-------------|
| 1 | Blocks 1+2 | Opening frame (puzzle + epistemic status + roadmap) and Departures rewrite |
| 2 | Block 3 | No-composition-artifact paragraph |
| 3 | Block 4 | Anticipation + beliefs (largest step: identification sentence, evidence order, verdict, footnote demotion) |
| 4 | Block 5 | Effort paragraph |
| 5 | Block 6 | Selection-on-performance & process ownership (incl. citation re-anchoring, uncertainty demotion, demand caveat) |
| 6 | Block 7 | Taking stock |
| 7 | Block 8 | Relation to prior evidence (Feier + two channels; dissolve "Other") |
| 8 | — | Consistency pass: labels, figure moves, cross-refs, §4.5 flags; sync checklist for intro/abstract/conclusion/appendix |

Each step: I draft the block in full LaTeX (respecting the caveats above), Felix reviews, we iterate, then he pastes/approves the edit.

---

# 6. Decision points for Felix (recommendation first)

- **D1 — Block order.** Recommended: artifact → anticipation → effort → process ownership (survivor last). Alternative: current order (process ownership mid-section). Recommendation rests on the eliminate-then-survive arc and on the artifact check preceding any heterogeneity interpretation.
- **D2 — Blue bars (hypothetical No-Punishment beliefs) in `fig:realized_vs_anticipated`.** Felix's comment leans toward dropping. Recommend **keep**, with a repurposed one-sentence role: beliefs about the punishment *schedule* are nearly identical across arms, so the manipulation changed whether punishment is real, not what subjects think it would look like — direct support for a non-belief-mediated mechanism (and thus for Block 6). If dropped, that argument is lost.
- **D3 — Figure allocation** (§4.3): keep `performance_by_delegation` in body; `performance` and the scatter to appendix.
- **D4 — Inherent uncertainty:** fold into Block 6 as a 2–3 sentence dispatched alternative (recommended) vs. footnote vs. keep as own paragraph.
- **D5 — Procedural-preference variant** (B wants a human decision; punishment makes that enforceable): add as one sentence inside Block 4's channel statement (recommended — it preempts a likely referee comment and is dispatched by the same belief evidence) or omit.
- **D6 — Connective sentence in Taking stock** (good-outcome belief difference ↔ good-outcome focus of process ownership): include flagged as suggestive, or omit.
- **D7 — M-numbering:** drop in favor of descriptive names (recommended) or renumber consistently everywhere.
