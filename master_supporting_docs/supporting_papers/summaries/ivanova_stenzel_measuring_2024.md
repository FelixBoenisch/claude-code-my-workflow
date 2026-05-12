---
title: "Measuring preferences for algorithms — How willing are people to cede control to algorithms?"
authors: Radosveta Ivanova-Stenzel, Michel Tolksdorf
venue: Journal of Behavioral and Experimental Economics
year: 2024
volume: 112
article: 102270
doi: 10.1016/j.socec.2024.102270
bibtex_handle: ivanova_stenzel_measuring_2024
pdf: ../ivanova_stenzel_measuring_2024.pdf
relevance_to_manuscript: high — methodological precedent for measuring algorithm preferences; cited in lit.tex ¶19
---

# Ivanova-Stenzel & Tolksdorf (2024) — *Measuring preferences for algorithms*

## Research question

Existing studies of algorithm aversion use a binary outcome ("do you choose your own forecast or the algorithm's?"), missing **the intensity of preferences for or against algorithms**. The paper introduces a **menu-based elicitation method** that varies the monetary cost of using the algorithm, capturing both extensive and intensive margins.

The applied question: **how much money are subjects willing to give up to avoid the algorithm?** And does providing information about the algorithm's performance change this?

## Methods

- **Lab experiment**, TU Berlin, *n* = 212 (106 per condition). Pre-registered AsPredicted #112129.
- **Forecasting task**: predict the rank of a US state by departing air passengers, based on five informational cues. 10 unincentivised rounds with feedback. 11th round is payoff-relevant.
- **Between-subjects condition**: "Human" (only own performance feedback) vs "Human-Algorithm" (both own and algorithm performance feedback).
- **Menu-based elicitation**: 9 choice problems in the payoff-relevant round. Each problem varies the penalty rate τ_alg for inaccurate algorithm forecasts. The own penalty rate τ_own is constant. The 5th choice problem is the standard binary choice in prior literature (equal penalties).
- One of the 9 choice problems is randomly implemented for payment. This allows measuring willingness-to-pay to use (or avoid) the algorithm.
- Standard risk and ambiguity questionnaires follow.

## Key results

- **Subjects exhibit strong but heterogeneous preferences for algorithms** along the intensive margin.
- **Algorithms are underused** relative to performance-based optima — subjects don't use the algorithm even when doing so would maximise expected payoff.
- **Information about algorithm performance increases use** when the algorithm is more costly to use — but not when the costs are equal.
- **Belief patterns explain choices**: subjects' beliefs about their own performance and the algorithm's performance drive their choices.
- **The menu-based measure detects effects that the binary measure misses** — the binary choice would have shown no effect of performance feedback in this data; the menu reveals it.

## Main takeaways

1. **Algorithm preferences have a meaningful intensive margin** that prior binary measures missed.
2. **People are willing to pay to avoid algorithms** — algorithm aversion has real opportunity cost.
3. **Performance feedback about the algorithm helps**, but only at moderate cost margins.
4. **The menu-based method is methodologically valuable** for future work studying algorithm preferences.
5. The result challenges the common interpretation that 40–60% delegation rates in prior studies represent indifference; intensive-margin measurement reveals stronger preferences.

## Relation to "Algorithms and Responsibility" (this manuscript)

Ivanova-Stenzel & Tolksdorf (2024) is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19 as part of the algorithm-aversion literature.

**Why this paper matters for the manuscript:**

**(1) Methodological pedigree.** Ivanova-Stenzel & Tolksdorf develop the **menu-based elicitation** approach, which is a methodological cousin of the manuscript's design choice to make delegation *costless*. The manuscript could have used a menu varying the cost of delegation as a robustness check. As it stands, the manuscript's costless design is consistent with the IVT-2024 approach in that it removes price effects from the delegation decision.

**(2) Heterogeneity in algorithm preferences is large.** IVT-2024 documents that some subjects are willing to pay substantially to use or avoid algorithms, while others are essentially indifferent. The manuscript's delegation rate of ~50% in the No-Punishment condition is consistent with this heterogeneity — half delegate, half don't, with substantial within-person preference intensity that the binary measure can't detect.

**(3) The forecasting task is similar to the manuscript's prediction task.** Both papers use a numerical forecasting / prediction task as the substantive domain. This makes comparison easier. IVT-2024 finds underutilisation of algorithms in forecasting; the manuscript finds similar delegation rates around 50%. The convergence suggests these results are stable across slight variations in forecasting task design.

**(4) IVT-2024 doesn't have a moral-domain version.** The forecasting task in IVT-2024 affects only the subject's own payoff; there is no third party. The manuscript's contribution is precisely to take the IVT-style design into the moral domain (where Player B is affected by Player A's prediction) and add the punishment manipulation. This positions IVT-2024 as a methodological / measurement precedent that the manuscript extends into responsibility-attribution territory.

**Where in literature.tex:**

- Paragraph 19 cites it correctly as part of the algorithm-aversion literature.

**Worth borrowing:** The menu-based design is a robustness lever the manuscript could mention as future work: "Future work could combine the menu-based elicitation of Ivanova-Stenzel & Tolksdorf (2024) with the punishment-on/off manipulation introduced here, to measure not just whether subjects delegate but *how much they would pay* to (avoid) delegate(ing) under different accountability regimes."

**Worth noting:** The paper's bib entry is now joined by a follow-up working paper (`ivanova_stenzel_delegating_2025`), which is the direct AI-vs-human extension of this earlier work. The two should be cited together when discussing the IVT line of work.
