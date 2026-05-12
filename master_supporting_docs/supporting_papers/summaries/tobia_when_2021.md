---
title: "When Does Physician Use of AI Increase Liability?"
authors: Kevin Tobia, Aileen Nielsen, Alexander Stremitzer
venue: Journal of Nuclear Medicine
year: 2021
volume: 62(1)
pages: 17–21
doi: 10.2967/jnumed.120.256032
bibtex_handle: tobia_when_2021
pdf: ../tobia_when_2021.pdf
relevance_to_manuscript: high — links algorithmic delegation to legal liability; cited in lit.tex ¶25
---

# Tobia, Nielsen & Stremitzer (2021) — *When Does Physician Use of AI Increase Liability?*

## Research question

When physicians use AI to inform medical decisions, **under what conditions does their liability for harm change?** Legal scholars have argued that tort law privileges "standard care," so a physician who accepts an AI recommendation for *nonstandard* care faces higher liability risk. This paper tests that prediction empirically using lay juror judgments.

## Methods

- **Online vignette experiment** through Lucid, March 2020. **Nationally representative US sample**, *n* = 2,000 (pre-registered).
- **2 × 2 between-subject design**:
  - **AI Recommendation**: standard care vs nonstandard care.
  - **Physician's Decision**: accept the recommendation vs reject it.
- Scenarios closely follow Price et al. (legal scholarship on AI in medicine), describing a physician treating an ovarian cancer patient where an AI ("Oncology-AI") provides a chemotherapy dosage recommendation. In all conditions, the resulting treatment causes harm.
- Subjects evaluate whether the physician's decision was "reasonable" under tort law standards.

## Key results

- **When AI recommends standard care**, the physician *reduces* liability risk by **accepting** rather than rejecting that advice. Following standard-care AI advice is liability-protective.
- **When AI recommends nonstandard care**, **no analogous shielding effect** exists. Rejecting the AI's nonstandard recommendation (to provide standard care instead) does *not* protect the physician.
- **Implication**: tort law is unlikely to undermine the use of AI precision medicine, contrary to legal-scholarship predictions. AI use can in some cases reduce liability.

## Main takeaways

1. **AI advice has an asymmetric liability effect**: protective when accepted for standard care; not protective when rejected to provide standard care.
2. **Lay juror judgments differ from legal scholars' predictions.** The "standard care anchor" legal scholars worry about is weaker than expected.
3. **AI use may be incentivised in medicine** rather than discouraged, on net.
4. **The asymmetry suggests AI is being used as a blame shield by jurors** — accepting AI advice transfers some responsibility to the AI, while rejecting it leaves responsibility fully with the physician.
5. **Policy implication**: contrary to fears, tort law may encourage rather than impede medical AI adoption.

## Relation to "Algorithms and Responsibility" (this manuscript)

Tobia et al. is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 25: "they extend the discussion to liability law and find experimentally that physicians who follow standard-care AI recommendations face reduced legal exposure; they argue that this could constitute an incentive to follow such recommendations specifically because doing so shields physicians from blame."

**Why this paper matters for the manuscript:**

**(1) Links algorithmic delegation to the legal/policy domain.** Most of the manuscript's literature review is on lab experiments. Tobia et al. shows the same blame-shifting logic operating in the *legal* context — accepting AI advice can reduce a physician's liability. This is the legal analogue of the manuscript's research question, and a useful policy-section anchor.

**(2) The "shielding when accepted, no protection when rejected" asymmetry parallels the manuscript's design contrast.** In Tobia, *accepting AI* is a kind of delegation — the physician hands over part of the decision to the AI. In the manuscript, Player A's delegation similarly hands the decision to the algorithm. Tobia finds shielding in this direction. The manuscript finds *no shielding* (H2 null). One possible explanation: Tobia's setting has a clear "moral high ground" (the AI's recommendation is the safer default), while the manuscript's setting has no equivalent — neither delegation nor self-decision has any moral pre-rating attached to it.

**(3) The vignette-vs-lab gap again.** Tobia is vignette-based; the manuscript is incentivised lab. Both designs measure third-party attributions of responsibility/liability, but in different ways. Tobia gets clean shielding effects in vignettes; the manuscript does not in lab.

**(4) Policy framing is useful.** Tobia argues tort law incentivises AI use. The manuscript finds that the prospect of punishment *reduces* algorithmic delegation. These two findings can be reconciled: when AI use is the established standard of care, the *legal* incentive favours AI; when accountability is acute and the actor experiences it personally, the *psychological* response favours direct engagement. Both can be true simultaneously, operating on different decision margins.

**Where in literature.tex:**

- Paragraph 25 cites it correctly with the right framing (liability protection + incentive interpretation).

**Worth borrowing for the policy section:** Tobia et al.'s argument that AI provides incentive-aligned blame shielding is exactly the worry that motivates the manuscript's question. The manuscript could engage with Tobia more directly in the conclusion: "Tobia et al. (2021) document that lay judges of physician liability extend partial blame-shielding when physicians follow AI recommendations. Our results suggest that this third-party effect, even if real, may be moderated by the *principal's* own preference for retaining accountability when stakes are salient — a tension that AI governance frameworks will need to address."

**Limitation:** Different domain (medicine), different methodology (vignette), different DV (legal-style judgments). The Tobia result is qualitative support for the manuscript's framing, not a direct competitor.
