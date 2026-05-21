---
title: "AI as the Phantom Limb: The Asymmetry of Attribution in Human vs. AI Delegation"
authors: Yu-Sheng Chen, Yoyo Tsung-Yu Hou, Yu-Hsuan Lin, Joshua Mu-En Liu, WeiRong Chen, Yihsiu Chen
venue: CHI '26 — Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems
year: 2026
doi: 10.1145/3772318.3791075
affiliations: National Chengchi University, Taipei
bibtex_handle: chen_ai_2026
pdf: ../chen_AI_2026.pdf
relevance_to_manuscript: moderate (Tier 3) — HCI experiment on attribution asymmetry in human vs AI delegation. Conceptually useful for the responsibility-vs-accountability distinction but methodologically removed from econ tradition.
---

# Chen et al. (2026, CHI) — *AI as the Phantom Limb*

## Research question

When a delegator's AI assistant receives external feedback (positive or negative) on a delegated task, how is that feedback internalised by the delegator — and does it differ from how feedback to a human delegate is internalised?

Sub-questions: Do people trust, perceive interpersonal distance, attribute responsibility, or internalise feedback differently when delegating to an AI vs a human? Does the delegate's competence or the valence of feedback moderate these dynamics?

## Methods

Pre-registered between-participants 2 × 2 × 2 vignette/scenario experiment. Recruited 355 participants on Prolific.

- **Setting**: Participants imagine delegating a scheduling task to an assistant (human vs AI), who completes the task. A supervisor then provides feedback (positive vs negative) on the assistant's performance.
- **Treatments**: 2 (Agent: Human vs AI) × 2 (Competence: High vs Low) × 2 (Feedback valence: Positive vs Negative).
- **Outcome measures**:
  - Multidimensional trust (ability, benevolence, perceived risk, reciprocity).
  - Psychological distance (3-item Likert).
  - Responsibility attribution to self vs assistant.
  - **Feedback internalisation**: extent to which feedback directed at the assistant was perceived as directed at the participant themselves.

## Key results

**Result 1 — Baseline trust is higher for human assistants.** Across competence and feedback conditions, participants reported higher trust in human than AI assistants. H1-1 supported.

**Result 2 — AI Phantom Limb effect.** When the AI assistant received *negative* feedback, participants internalised the criticism as self-directed significantly more than when the *human* assistant received the same negative feedback. The asymmetry did **not** appear for positive feedback: participants did not internalise positive feedback to AI as self-credit any more than positive feedback to a human.

**Result 3 — The pattern reverses on responsibility attribution.** When the AI failed, participants attributed *more* responsibility to themselves (and less to the AI) than when the human failed. Conversely, they attributed more responsibility to a human assistant for the task outcome.

**Result 4 — Competence moderates feedback effects.** Low-competence AI receiving negative feedback produced the strongest self-internalisation effect.

The authors interpret the pattern as: AI assistants are perceived as *unaccountable* in social/normative terms (the audience cannot meaningfully blame the AI), so the negative externality flows back to the human delegator. With human delegates, the audience can blame the human delegate, so the negative feedback stays with the delegate rather than rebounding.

## Main takeaways

1. **Human-AI delegation blurs the self–other boundary** in a way that human–human delegation does not.
2. **The blurring is asymmetric**: negative feedback to AI gets internalised by the delegator; positive feedback does not get transferred symmetrically.
3. **Responsibility and accountability decouple**: people may believe the AI is *responsible* (internally) for a failure but recognise that an external audience cannot hold it *accountable* — so the accountability burden flows back to the delegator.
4. **Design implication**: AI delegation that obscures the human-in-the-loop may inadvertently increase the human's social-psychological burden under failure.
5. The "AI Phantom Limb" framing is a memorable handle for this attribution asymmetry.

## Relation to "Algorithms and Responsibility" (this manuscript)

**Why this paper matters for the manuscript:**

**(1) Sharpens the responsibility-vs-accountability distinction.**
The paper makes an explicit *internal-responsibility* vs *external-accountability* distinction that maps directly onto the manuscript's framing question: why does delegation to AI not absorb blame from third parties even though it might absorb self-felt responsibility? Chen et al.'s answer — *because the audience does not see AI as accountable, the social-blame burden returns to the delegator* — is a microfoundation for the manuscript's H2 null result.

**(2) Conceptually adjacent to the manuscript's H1 reversal.**
If delegating to AI loads the *accountability* burden back onto the delegator (Chen et al.'s mechanism), then under high accountability salience (the manuscript's punishment-on treatment) delegation to AI should become *less* attractive, not more — exactly the H1 reversal the manuscript documents. Worth citing as a non-economics articulation of the same intuition.

**(3) Methodological caveat — HCI tradition, not incentivised economics.**
Vignette-based, hypothetical scenarios, Likert-scale outcome measures. The paper is in the HCI tradition (CHI 2026 proceedings) rather than incentivised economics. Useful for *conceptual* framing but should not be over-leaned-on for empirical claims; econ referees will discount Likert-scale evidence.

**(4) Useful counterpoint to Hueholt & Szech (2026).**
Hueholt & Szech (2026, EER) finds that delegation to AI absorbs *internal* moral burden via belief adaptation. Chen et al. finds that delegation to AI *fails* to absorb *external* social-blame burden, which rebounds to the delegator. The two findings together support a clean two-channel account: AI is a good shield against internal moral burden but a poor shield against external accountability. This is exactly the framing the manuscript's H1 reversal can sit inside.

**Where to cite in literature.tex:**

- **Subsection 3 ¶32 (responsibility perceptions)**: a useful addition to the post-Shank 2019 / Bigman 2018 / Tobia 2021 list. Cite for the responsibility-accountability decoupling specifically.
- **Possibly in the "Where this paper fits" discussion**: the AI-Phantom-Limb framing can be a rhetorical anchor for the manuscript's central claim that AI absorbs *some* but not *all* of the blame burden.

**Caveat — proceedings publication.**
This is a conference proceedings paper (ACM CHI), not a journal article. For a top-5 econ submission, treat it as a working-paper-level reference: useful for ideas but not for citation legitimacy. Cite the published-version DOI when available; the work itself may also appear as a journal article in 2026–2027.
