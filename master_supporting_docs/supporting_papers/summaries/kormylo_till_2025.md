---
title: "Till Tech Do Us Part: Betrayal Aversion and Its Role in Algorithm Use"
authors: Cameron Kormylo, Idris Adjerid, Sheryl B. Ball, Can Dogan
venue: Management Science
year: 2025
volume: 72(1)
pages: 343–367
doi: 10.1287/mnsc.2022.03510
note: Special Issue on the Human-Algorithm Connection
bibtex_handle: kormylo_till_2025
pdf: ../kormylo_till_2025.pdf
relevance_to_manuscript: high — algorithm-vs-human asymmetric mechanism; added in recent lit-review pass
---

# Kormylo, Adjerid, Ball & Dogan (2025) — *Till Tech Do Us Part*

## Research question

People often refuse expert financial advice. One reason is **betrayal aversion** — the strong dislike for the violation of trust norms in a relationship. The paper asks: **does substituting an algorithmic advisor for a human advisor attenuate betrayal aversion**, and does this lead to higher uptake of expert advice?

The intuition: algorithms don't have intentions, so violating trust by them feels less like a betrayal. But prior work (Koehler & Gershoff 2003) shows people feel betrayed by inanimate products like airbags and vaccines, so the answer isn't ex-ante obvious.

## Methods

- **Two lab experiments** (one on MTurk via video-sharing platform; one with undergraduates).
- **Setting**: 40-round financial market trading game with a simulated structure and a real financial trading algorithm.
- **2 × 3 between-subjects design**:
  - **Factor 1**: Expert presented as human or algorithm (underlying algorithm identical).
  - **Factor 2**: Three conditions:
    - **Control** (no disclaimer)
    - **Betrayal risk** (informed there's a slight chance the expert will make a self-interested decision)
    - **Error risk** (informed there's a slight chance of an accidental error — controls for monetary-return concerns without intentionality)
- **n = 275** in the main MTurk experiment; smaller sample in the undergraduate replication.

## Key results

**Result 1 — Human-expert betrayal aversion**: Informing participants of betrayal risk reduced uptake of human-expert advice by ~16% (β = −0.159, *p* = 0.024). Error-risk had no effect (β = 0.007, *p* = 0.924), establishing that the effect is *psychological betrayal* rather than expected-return concerns.

**Result 2 — Algorithm-expert betrayal aversion is absent**: The same betrayal-risk disclaimer did *not* reduce algorithmic-expert uptake (*p* = 0.431). Algorithms apparently can't betray in the same way humans can.

**Result 3 — Economic consequences are real**: Betrayal aversion toward human experts costs participants ~$2.15 (~20% of overall returns, *p* = 0.072).

**Result 4 — Subjective measures align**: Participants in the human-advisor betrayal condition report feeling misled, having trust violated, and feeling betrayed; participants in the algorithm condition do *not* report these feelings.

**Result 5 — Replicated** in a second experiment with undergraduate students and a different human advisor.

## Main takeaways

1. **Betrayal aversion is human-specific.** It strongly reduces uptake of human expert advice but doesn't apply to algorithmic experts.
2. **The mechanism is psychological, not monetary**: error-risk disclaimers don't have the same effect.
3. **Algorithmic experts have an under-appreciated advantage**: substituting an algorithm can attenuate barriers to expert advice acceptance.
4. **Real economic consequences**: ~20% earnings loss from refusing human advice due to betrayal aversion.
5. **Reframes algorithm-vs-human comparison**: the older "algorithm aversion" framing assumes algorithms are at a disadvantage, but algorithms are *advantaged* in domains where betrayal aversion is a barrier to human-expert uptake.

## Relation to "Algorithms and Responsibility" (this manuscript)

Kormylo et al. is **not yet cited** in literature.tex but was added to the bib in the recent lit-review pass.

**Why this paper matters for the manuscript:**

**(1) Asymmetric human-vs-algorithm psychological mechanism.** Kormylo et al. identifies a specific channel (betrayal aversion) that's *only* triggered by humans, not algorithms. The manuscript's M3 reading is related: process ownership / accountability salience is what subjects experience when they delegate — and this experience may also be human-specific in some sense. The manuscript could engage with Kormylo et al. as a useful counterpoint: where Kormylo et al. show algorithms *win* in a human-disadvantage domain, the manuscript shows algorithms *lose* in a context where principals want to retain accountability.

**(2) Direct relevance to the manuscript's algorithm aversion subsection.** Kormylo et al. is the most relevant 2025 Management Science paper on algorithm preferences. Cite it alongside Dargnies et al. 2026 in literature.tex paragraph 19. Suggested addition: "Kormylo et al. (2025) document an asymmetry in betrayal aversion across human and algorithmic experts: humans are subject to it, algorithms are not, with measurable consequences for advice uptake."

**(3) The "human-specific psychological cost" finding is methodologically informative.** Both Kormylo et al. and the manuscript design experiments that hold technical performance equal across human and algorithm conditions, isolating psychological mechanisms. The convergence of finding *real, behaviour-moving psychological asymmetries* across the two papers supports the broader claim that human-vs-algorithm comparisons activate something other than just "expected return" reasoning.

**(4) Pre-registered, published Management Science Special Issue.** This is a high-quality recent reference with a clean methodological pedigree — useful as a citation for the algorithm-vs-human literature.

**Where to cite in literature.tex:**

- Paragraph 19 (algorithm aversion subsection), alongside Dargnies et al. 2026.
- Possibly also in the discussion section as a counter-example: in some domains (financial advice), algorithms have *advantages* via reduced betrayal aversion; in other domains (moral-domain delegation with accountability salience), they have disadvantages via accountability-displacement concerns.

**Limitation:** Kormylo et al.'s setting is *aligned with the principal's interest* (advisor advice for the participant's own financial gain), not a third-party-affecting moral domain. So the betrayal-aversion mechanism is not directly transferable to the manuscript's setting. But it's a useful example of the kind of human-algorithm asymmetric mechanism the manuscript is also documenting (in a different domain).
