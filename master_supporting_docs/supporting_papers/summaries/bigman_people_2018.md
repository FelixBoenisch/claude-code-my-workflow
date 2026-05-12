---
title: "People are averse to machines making moral decisions"
authors: Yochanan E. Bigman, Kurt Gray
venue: Cognition
year: 2018
volume: 181
pages: 21–34
doi: 10.1016/j.cognition.2018.08.003
bibtex_handle: bigman_people_2018
pdf: ../bigman_people_2018.pdf
relevance_to_manuscript: high — moral-domain machine aversion; cited in lit.tex ¶19, 25 (algorithmic outrage asymmetry)
---

# Bigman & Gray (2018) — *People are averse to machines making moral decisions*

## Research question

**Do people want autonomous machines making moral decisions?** And if not, why?

The paper proposes the answer is rooted in **mind perception**: machines are seen as lacking the full mind (agency *and* experience) required for moral decision-making. Three further questions:
1. Does the aversion exist even when machine decisions are *positive*?
2. Can the aversion be reduced by limiting machines to an advisory role, increasing their perceived experience, or increasing their perceived expertise?

## Methods

**Nine vignette studies** across four moral domains (driving, legal, medical, military). Subjects evaluate scenarios in which an autonomous machine or a human makes a moral decision.

- **Studies 1–6**: documenting and characterising the aversion. Subjects report whether they would prefer a human or a machine making the decision; mind-perception ratings of the machine (agency + experience) are mediators.
- **Studies 7–9**: testing routes to reduce the aversion:
  - Advisory role (Study 7)
  - Increased experiential mind (Study 8) — describing the machine as feeling, suffering, etc.
  - Increased expertise (Study 9) — describing the machine as more competent

## Key results

- **Strong aversion across all four moral domains.** People consistently prefer human decision-makers, even when the machine has identical decision-making rules.
- **Mediation by mind perception**: the aversion is partly explained by perceiving machines as lacking a complete mind (both the agency to reason and the experience to feel).
- **Aversion persists for positive outcomes** (Studies 5–6). Not just a fear of bad outcomes; people don't want machines making moral calls regardless of valence.
- **Reducing routes are limited**:
  - Advisory role *moderately* helps but doesn't eliminate aversion.
  - Increased experience (perceived mind) helps, but unevenly.
  - Increased expertise does *not* significantly help — people don't accept machines just because they're more accurate.

## Main takeaways

1. **Aversion to machine moral decisions is robust and large** across multiple domains.
2. **Mind perception is the central mechanism** — specifically, the perceived absence of feeling / experience.
3. **The aversion is not about outcomes.** It survives both good and bad outcomes, and competence improvements.
4. **Hard to eliminate** with conventional design interventions.
5. **Policy implication**: putting AI in moral domains may face deep resistance grounded in lay metaphysics about minds.

## Relation to "Algorithms and Responsibility" (this manuscript)

Bigman & Gray is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19 (algorithm aversion strongest in moral content), and paragraph 25 invokes their **"algorithmic outrage asymmetry"** finding (moral violations by algorithms produce less outrage than identical violations by humans).

**Why this paper matters for the manuscript:**

**(1) Mind-perception mechanism is *orthogonal* to your M3.** Bigman & Gray's mechanism is observer-side and about *the algorithm's perceived capability for moral judgment*. The manuscript's M3 is principal-side and about *the principal's experience of process ownership*. These are not competing — they could both be operating, in different proportions, depending on design. In the manuscript's design (Bernoulli draw, no anthropomorphisation), the mind-perception channel is muted because the algorithm is so obviously rule-based; the M3 channel is the residual.

**(2) "Algorithmic outrage asymmetry" is the *opposite-direction* result to the manuscript's H2 null.** Bigman & Gray (2020 working paper cited in Feier et al.) find that moral violations by algorithms produce *less* outrage than violations by humans — which would suggest H2 should hold (less punishment for algorithmic delegation). The manuscript finds *no* significant punishment differential. The two results aren't directly comparable (Bigman uses vignettes and outrage ratings; the manuscript uses incentivised costly punishment), but the contrast is informative: incentivised behavioural measures may attenuate the outrage asymmetry that vignette studies pick up.

**(3) The vignette-vs-lab gap is methodologically important.** Bigman & Gray is the high-water mark of the vignette literature on moral machine aversion. The manuscript belongs to the incentivised-lab subset (Feier, Chevrier, Kirchkamp, Maasland, Tontrup). Vignette studies tend to find stronger and more robust effects; lab studies find more mixed evidence. The manuscript's null on H2 is in line with the lab-study pattern. This is worth a sentence in the discussion: "Bigman & Gray (2018) identify a strong moral-machine aversion in vignette settings; the corresponding effect in incentivised lab paradigms is more variable (see Kirchkamp & Strobel 2019 and our H2 result)."

**(4) Advisory framing partly reduces aversion** — relevant for policy. Bigman & Gray's finding that advisory framings help is consistent with the broader literature on human-in-the-loop AI design. The manuscript's design is closer to "full delegation" than "advisory" — Player A either makes the prediction herself or hands it entirely to the algorithm. This is the harder version of the question.

**Where in literature.tex:**

- Paragraph 19: correct citation as moral-domain aversion paper.
- Paragraph 25: correct citation for the algorithmic outrage asymmetry.

**Worth adding:** A sentence in section 4 / mechanism discussion noting that the manuscript's algorithm is deliberately designed to be transparent and rule-based (Bernoulli draw at known probability), which should *minimise* the Bigman & Gray mind-perception channel. The residual delegation aversion observed under the punishment condition is therefore unlikely to be driven by mind perception in your data — supporting the M3 reading.
