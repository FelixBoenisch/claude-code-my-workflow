---
title: "When are artificial intelligence versus human agents faulted for wrongdoing? Moral attributions after individual and joint decisions"
authors: Daniel B. Shank, Alyssa DeSanti, Timothy Maninger
venue: Information, Communication & Society
year: 2019
volume: 22(5)
pages: 648–663
doi: 10.1080/1369118X.2019.1568515
bibtex_handle: shank_attributions_2019
pdf: ../shank_attributions_2019.pdf
relevance_to_manuscript: high — direct comparison of moral fault for AI vs human, individual vs joint; cited in lit.tex ¶25
---

# Shank, DeSanti & Maninger (2019) — *When are AI versus human agents faulted for wrongdoing?*

## Research question

Two questions:
1. **Are AI agents attributed the same moral fault as human agents** when both produce identical real-world moral violations?
2. **How does moral fault distribute in human-AI joint decision-making structures** — specifically, when humans monitor AIs vs. when AIs recommend to humans?

## Methods

- **Vignette experiment**. Four real-world AI moral-violation scenarios (e.g., AI parole sentencing leniency toward whites, beauty-contest AI selecting few dark-skinned winners, recommender exposing children to violent videos, Twitter bot producing derogatory remarks).
- **Within-subject manipulation** of decision-making structure across four conditions:
  1. **Individual AI**
  2. **Individual human**
  3. **Joint — human monitoring AI** (AI acts, human supervises)
  4. **Joint — AI recommending to human** (AI advises, human decides)
- Subjects rate moral permissibility and fault for each entity in each scenario.

## Key results

- **AIs receive less moral fault than humans for the same violation.** Consistent with the broader "algorithmic outrage asymmetry" literature.
- **The decision-making structure has little effect on AI fault.** AIs are blamed about the same whether acting alone or jointly with humans.
- **But the decision-making structure matters a lot for human fault.** Specifically:
  - **Humans monitoring AIs are faulted less than humans acting alone.**
  - **Humans receiving AI recommendations are faulted about the same as humans alone.**
- **In joint structures, AIs receive more permission and less fault than the humans they're paired with.** The authors flag this as potential "strategic scapegoating" — using AIs as moral crumple zones for human moral failings.

## Main takeaways

1. **AIs are systematically faulted less than humans** for the same moral violations.
2. **Monitoring an AI is *protective*** for the human — fault is diffused.
3. **Receiving AI recommendations is *not* protective** for the human — they're still on the hook.
4. **AI can absorb meaningful moral fault** in joint structures (though less than humans).
5. **Policy implication**: strategic scapegoating of AIs for human moral failings is a real risk in joint decision structures.

## Relation to "Algorithms and Responsibility" (this manuscript)

Shank et al. is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 25: "consider moral violations produced by human-algorithm pairs and find that humans who monitor algorithms are blamed less than humans acting alone or humans receiving algorithm recommendations, suggesting that responsibility attributions are sensitive to the precise division of authority between human and machine."

**Why this paper matters for the manuscript:**

**(1) The "monitoring vs recommending" distinction is informative.** Shank et al. show that the *protection* offered by AI partnership depends on the structure: monitoring an AI protects the human, but receiving AI recommendations doesn't. In the manuscript's design, Player A either fully delegates to the algorithm (closer to "monitoring" — A doesn't intervene) or makes the decision herself. The Shank pattern would predict that delegation should shield A from blame. The manuscript's H2 null is therefore inconsistent with the Shank pattern in vignette settings.

**(2) The vignette-vs-lab gap appears again.** Shank et al. is vignette-based; the manuscript is incentivised lab. The pattern in vignettes — strong asymmetric blame attribution favouring the human in monitoring structures — does not show up in the manuscript's costly punishment data. This is consistent with the broader pattern: vignette-based moral-attribution studies find strong effects; incentivised lab studies find weaker or null effects (Kirchkamp; this manuscript).

**(3) "Strategic scapegoating" is a relevant policy framing.** Shank et al.'s concern about strategic scapegoating of AI parallels the manuscript's concern about responsibility-shifting through algorithmic delegation. Both papers argue that AI's lower-fault status creates incentives for humans to use AI to shed blame. The manuscript's H1 reversal complicates this — when accountability is salient and stakes are real, subjects don't *exploit* this shield, they actively avoid using AI. This is worth flagging in the policy discussion: the strategic-scapegoating concern documented by Shank et al. may operate primarily in *anticipated* moral judgement (vignette settings) rather than in *experienced* moral judgement (lab settings with real punishment).

**(4) The Shank finding that "AI fault is structure-invariant" is suggestive.** AIs in their data are blamed similarly across structures. This is consistent with the manuscript's design choice: the algorithm in the manuscript is structurally identical to a "Bernoulli draw" — it has no choice and no agency. If the moral-fault attribution to AI is structure-invariant, then varying delegation (the structural question in the manuscript) shouldn't change how subjects perceive the algorithm's contribution to a bad outcome. The action is on the *human* side. This is the right conceptual frame for thinking about why the manuscript's H2 is null.

**Where in literature.tex:**

- Paragraph 25 correctly summarises the central finding.

**Worth integrating:** The manuscript's discussion section could engage with Shank et al.'s "monitoring vs recommending" structure directly. The manuscript's delegation choice is essentially a *monitoring* choice (Player A monitors the algorithm's prediction by either accepting it as delegated or substituting her own). Shank et al. predict this structure shields the principal from blame. The manuscript finds no such shielding. Two candidate explanations:
1. The lab setting with costly punishment dampens the asymmetric attribution that vignettes pick up.
2. The aligned-incentive prediction task removes the moral salience of "shielding" — there's no bad action to be shielded from, just a stochastic outcome.

**Limitation:** Shank et al.'s sample size, methodology, and venue suggest this is a useful contributor to the lit-review map rather than a strong empirical anchor for any specific claim in the manuscript.
