---
title: "Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them"
authors: Berkeley J. Dietvorst, Joseph P. Simmons, Cade Massey
venue: Management Science
year: 2018
volume: 64(3)
pages: 1155–1170
doi: 10.1287/mnsc.2016.2643
bibtex_handle: dietvorst_overcoming_2018
pdf: ../dietvorst_overcoming_2018.pdf
relevance_to_manuscript: medium-high — overcoming aversion via modifiable algorithms; cited in lit.tex ¶19
---

# Dietvorst, Simmons & Massey (2018) — *Overcoming Algorithm Aversion*

## Research question

Given algorithm aversion (Dietvorst 2015), **how can we reduce it?** Specifically: do people use imperfect algorithms more when they can **modify** the algorithm's output?

## Methods

Three incentivised forecasting studies. Participants choose between using their own forecast or the algorithm's. Treatment: participants can *modify* the algorithm's forecast (with varying levels of permitted modification).

## Key results

- **Subjects strongly prefer modifiable algorithms** over fixed ones.
- The preference holds **even when the permitted modifications are tiny** — slightly modifiable algorithms are nearly as attractive as fully modifiable ones.
- Allowing modifications increases satisfaction with the forecasting process, belief that the algorithm is superior, and willingness to use algorithms in future tasks.
- The result is interpreted as evidence that subjects want *some control* over the forecasting outcome — but not necessarily *more* control.

## Main takeaways

1. **Modifiability dramatically reduces algorithm aversion**, even when the modifiability is symbolic.
2. **The desire for control is qualitative, not quantitative** — having *any* role in the output is what matters.
3. **Design lever**: a small amount of empowerment / agency can overcome substantial algorithm aversion.
4. The result supports the "process ownership" or "agency" reading of algorithm aversion — what matters is whether the person feels they had a hand in the output.

## Relation to "Algorithms and Responsibility" (this manuscript)

Dietvorst 2018 is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19 as part of the algorithm-aversion literature.

**Why this paper matters for the manuscript:**

**(1) The "process ownership" connection is direct.** Dietvorst 2018's finding — even token control over an algorithm reduces aversion — is the *experimental analog* of the manuscript's M3 (process ownership) mechanism. Subjects want to feel they had a hand in the output; pure delegation (no modification, as in the manuscript) doesn't satisfy that need.

**(2) The manuscript's design has *no* modifiability.** Player A either delegates fully (Bernoulli draw at her accuracy) or makes the prediction herself. There's no intermediate. Under Dietvorst 2018's logic, the manuscript's delegation rates would be *higher* if subjects could modify the Bernoulli output even slightly. This is worth flagging as a robustness check / future-work direction: "Allowing Player A to modify the algorithm's prediction (e.g., adjusting the probability by a small amount, or seeing the Bernoulli result and choosing whether to override) would likely raise delegation rates substantially, per Dietvorst, Simmons & Massey (2018)."

**(3) Modifiability as a design choice in the broader literature.** Dietvorst 2018 has had significant influence on how subsequent algorithm-aversion studies design their tasks. The manuscript's choice of full delegation is conservative — it captures the worst-case for algorithm uptake.

**Where in literature.tex:**

- Paragraph 19 cites correctly.

**Worth borrowing:** The "even token modification helps" finding could be framed in the manuscript's discussion as a complementary policy lever: "Dietvorst, Simmons & Massey (2018) show that even token modifiability can reduce algorithm aversion; our results suggest that even when modifiability is unavailable, accountability salience further reduces algorithmic delegation. The two findings combine to suggest that AI deployment in moral domains should emphasise both meaningful human control over outputs and clear lines of accountability."
