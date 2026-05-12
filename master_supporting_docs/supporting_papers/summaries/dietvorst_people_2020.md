---
title: "People Reject Algorithms in Uncertain Decision Domains Because They Have Diminishing Sensitivity to Forecasting Error"
authors: Berkeley J. Dietvorst, Soaham Bharti
venue: Psychological Science
year: 2020
volume: 31(10)
pages: 1302–1314
doi: 10.1177/0956797620948841
bibtex_handle: dietvorst_people_2020
pdf: ../dietvorst_people_2020.pdf
relevance_to_manuscript: medium-high — uncertainty amplifies algorithm aversion; cited in lit.tex ¶19
---

# Dietvorst & Bharti (2020) — *People Reject Algorithms in Uncertain Decision Domains*

## Research question

**Why** do people reject algorithms in uncertain decision domains (medicine, investing, self-driving cars) even when algorithms outperform humans? The paper proposes that **diminishing sensitivity to forecasting error** drives the rejection: people care a lot about small errors but increasingly less about large ones, leading them to prefer "risky" methods (humans) that offer the chance of near-perfect outcomes over methods (algorithms) that offer consistent moderate performance.

## Methods

Nine studies, *N* = 4,820. Pre-registered. Forecasting tasks with varying levels of inherent uncertainty (e.g., investment returns, medical outcomes). Subjects choose between algorithmic and human forecasters and decision-making methods.

## Key results

- **People have diminishing sensitivity to forecasting error**: each marginal unit of error generates less subjective disutility than the previous one.
- **Algorithm rejection rises with task uncertainty**: in domains where outcomes are more unpredictable, subjects use algorithms less.
- **Subjects choose methods by perceived likelihood of near-perfect answers**, not by average performance.
- **Higher variance methods are preferred** when average performance is held fixed.

## Main takeaways

1. **Algorithm aversion is amplified in uncertain domains** precisely because subjects prefer "shots at perfection" over consistent moderate performance.
2. **The mechanism is concave subjective penalty for error** — diminishing sensitivity rather than risk preferences in the traditional sense.
3. **Policy implication**: in genuinely uncertain domains (medicine, finance, self-driving), algorithm uptake will be lower than performance metrics suggest is optimal, because the variance-of-outcomes pattern favors humans.
4. The result helps explain why algorithm aversion is so persistent even when algorithms clearly outperform on average.

## Relation to "Algorithms and Responsibility" (this manuscript)

Dietvorst & Bharti is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19.

**Why this paper matters for the manuscript:**

**(1) The manuscript's task is *highly uncertain*.** Player A predicts weight from a face photograph — genuinely uncertain. By Dietvorst & Bharti's logic, this design would amplify algorithm aversion. The manuscript's relatively high delegation rate (~50%) is therefore somewhat surprising. Possible explanations:
- The individual-level Bernoulli calibration removes performance ambiguity — there's no perceived variance difference between A and the algorithm, so the Dietvorst & Bharti mechanism can't bite.
- Player A's "control" over the prediction is also illusory (she can't reliably do better than her own empirical accuracy), so the "shot at perfection" intuition is weak.
- Algorithm aversion is moderated by the moral salience of the decision, which Player B's matched-payoff design partly captures.

**(2) Useful framing point for the discussion.** The manuscript could note: "Dietvorst & Bharti (2020) document that algorithm aversion is amplified in uncertain decision domains via diminishing sensitivity to error. Our design's individual-level Bernoulli calibration removes the perceived variance gap between human and algorithmic methods, which closes off this channel and likely explains the relatively balanced delegation rates we observe."

**(3) Connects to the manuscript's design choice of the visual prediction task.** Predicting weight from a face is precisely the kind of "inherently uncertain" task Dietvorst & Bharti focus on. The manuscript's external validity arguments for choosing such a task (financial forecasting, medical diagnosis, fraud detection) parallel Dietvorst & Bharti's motivating examples.

**Where in literature.tex:**

- Paragraph 19 cites it correctly.

**Worth borrowing:** The Dietvorst & Bharti framing — that uncertainty itself drives algorithm aversion — strengthens the manuscript's argument that prediction tasks in real-world applications (medical, financial, judicial) face uphill battles for algorithmic adoption. This is a useful policy point for the conclusion.
