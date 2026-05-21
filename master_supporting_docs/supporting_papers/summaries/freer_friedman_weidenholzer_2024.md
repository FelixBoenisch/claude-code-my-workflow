---
title: "Motives for Delegating Financial Decisions"
authors: Mikhail Freer, Daniel Friedman, Simon Weidenholzer
venue: arXiv working paper
year: 2024
arxiv_id: 2309.03419
version: v3 (15 April 2024)
affiliations: University of Essex / UCSC
bibtex_handle: freer_friedman_weidenholzer_2024
pdf: ../freer_friedman_weidenholzer_2024.pdf
relevance_to_manuscript: high — applied test of blame-shifting motive in financial decisions; added for subsection 1 breadth
---

# Freer, Friedman & Weidenholzer (2024 WP) — *Motives for Delegating Financial Decisions*

## Research question

In financial decision-making, why do investors delegate to "experts" (other investors)? The paper aims to **disentangle four candidate motives**:

1. **Chasing past performance** — investors believe high-earning experts will continue to perform well (belief distortion).
2. **Blame-shifting** — investors want somebody else to blame if things go wrong (responsibility avoidance).
3. **Reducing decision costs** — complex environments make personal decisions costly; delegation is a rational shortcut.
4. **Increasing risk tolerance** — trust in the expert reduces the subjective utility cost of taking risk.

The motivating empirical context: the rise of copy-trading platforms (eToro, ZuluTrade) where investors can copy the trades of other investors at low cost.

## Methods

- **Online lab experiment**, ~600 participants from Prolific.
- **Investment task**: a sequence of three blocks, each with five investment decisions. The fifth decision in each block can be delegated to a chosen "expert" from a panel of five experts (pre-selected from preliminary sessions).
- **Three levels of task complexity**:
  - **Trivial task**: choice between two binary lotteries with identical expected payoff and variance — pure luck, no role for skill.
  - **Simple task**: choice among six lotteries differing in expected payoff and variance (some dominated).
  - **Complex task**: portfolio allocation over the five simple lotteries (multi-dimensional).
- **Information treatments** (vary what investors see about experts):
  - **AllInfo**: payoff, quality rating (Afriat's CCEI-based), risk rating.
  - **NoPay**: quality + risk only (eliminates past-performance signal).
  - **NoQual**: payoff + risk only.
- **Cost treatments**: delegation costs 10 pence (low) or 100 pence (high).

The design lets the authors isolate motives:
- Delegation in the trivial task under NoPay reveals **blame-shifting** (no other motive can apply).
- Delegation rising in the complex task reveals **decision costs**.
- Choice of high-earning expert under AllInfo reveals **performance-chasing**.
- Investors choosing risk-tolerant experts reveals **risk acceptance**.

## Key results

**Result 1 — A surprisingly large fraction delegate the trivial task.**
This is the central finding for the blame-shifting motive. Even when delegation has no informational advantage (the task is pure luck, no skill involved, and the past-payoff signal is hidden in NoPay), a substantial share of investors still delegate. **The blame-shifting motive is therefore a primary driver.**

**Result 2 — Complex tasks see higher delegation rates.**
Consistent with the decision-cost motive: complex tasks are cognitively demanding, and investors hire experts to reduce the decision burden.

**Result 3 — Some investors chase past performance.**
When earnings information is available (AllInfo), some investors disproportionately select experts with high realised payoffs, even though earnings are a noisy signal of expertise. This is the performance-chasing belief distortion documented elsewhere (Apesteguia et al. 2020).

**Result 4 — No evidence of the risk-tolerance motive.**
Delegating to high-risk-tolerance experts does not increase delegation; the increasing-risk-tolerance hypothesis is not supported in this design.

**Result 5 — Robustness**: results hold across delegation costs, although high cost reduces delegation overall.

## Main takeaways

1. **Blame-shifting is a primary motive for financial delegation** — and it operates even when no other rational basis for delegation exists. The trivial-task delegation rate is the cleanest existing evidence for this in financial decisions specifically.
2. **Multiple motives operate simultaneously.** The paper provides a methodology for disentangling them via careful treatment design rather than just measuring overall delegation.
3. **Performance-chasing is real but moderate** — investors do chase past returns, but only when information is available.
4. **Risk tolerance does not drive delegation** in this design — challenges the increasing-risk-tolerance hypothesis (Gennaioli et al. 2015) at least in this experimental setting.
5. **Methodological contribution**: provides a template for testing multiple competing motives for delegation in a single experimental paradigm.

## Relation to "Algorithms and Responsibility" (this manuscript)

Freer, Friedman & Weidenholzer is **not yet cited** in literature.tex but should be added to subsection 1 per the recent restructuring discussion. It's the most direct applied test of blame-shifting in the financial decisions domain.

**Why this paper matters for the manuscript:**

**(1) Cleanest domain-applied test of the blame-shifting motive.**
Most of the responsibility-shifting literature (B&F, Hamman, Coffman, Oexl) uses dictator games. Freer et al. apply the same conceptual framework to a more practical domain (financial decisions / lottery investment) and confirm blame-shifting as a primary motive. This is exactly the kind of "domain breadth" you flagged when you sent the arXiv link.

**(2) Multi-motive framework.**
Freer et al. explicitly disentangle blame-shifting from other motives (decision costs, performance-chasing, risk tolerance). This is methodologically important: it shows that blame-shifting isn't just the "residual" or "default" reason people delegate when there's no other explanation — it operates *additionally* to those other motives. The manuscript's H1 is a binary punishment-vs-no-punishment manipulation, which doesn't disentangle these motives as cleanly. Freer et al. is the cleanest "yes, blame-shifting is a real motive separate from other reasons" demonstration.

**(3) Trivial-task delegation rate is the most striking finding.**
The fact that a "surprisingly large fraction" delegate even when there's *literally no skill involved* (binary lottery with identical EV and variance) is the cleanest possible evidence that blame-shifting is doing work independent of any rational decision-making advantage. The manuscript can cite this for the strong empirical case that the blame-shifting motive exists outside dictator-game allocation tasks.

**(4) Aligned with the example you flagged.**
This is the paper you flagged in your earlier message (arXiv:2309.03419) as the kind of "domain breadth" you want for subsection 1. Worth citing prominently.

**Where to cite in literature.tex:**

- Paragraph 15 (subsection 1 breadth-list): cite as the financial-decisions domain test of blame-shifting. Drafted earlier:
  > "...the responsibility-shifting motive has been documented across a range of practical domains: ... financial decisions and copy trading \citep{freer_friedman_weidenholzer_2024, apesteguia_copy_2020}..."

**Cross-references in the manuscript's existing citations:**
- The paper appears in my earlier citation-graph search across recent (2024+) literature citing B&F, Coffman, Hamman, Oexl.
- Heavily cites the manuscript's literature.tex anchor set (B&F 2012, Bartling-Fischbacher-Schudy 2015, plus Erat 2013 for delegated deception).

**Important caveats**:
- This is a working paper (arXiv 2024 v3), not yet published in a journal. Cite with `@unpublished{...}` as in the bib entry. May get a journal publication soon, in which case update the entry.
- The methodology is online (Prolific) rather than in-person lab — relevant for thinking about the manuscript's own Prolific design. Confirms that lab-quality results are achievable on Prolific in the responsibility-shifting paradigm.
- The four-motive disentanglement methodology could be borrowed for future work — extending the manuscript's H1 to disentangle blame-shifting from other motives for algorithmic delegation.

**Worth borrowing for the manuscript's introduction**:
- The "copy-trading platforms" motivation Freer et al. open with is a vivid real-world example of delegation that complements the AI/algorithm motivation in your introduction. The two narratives (financial advisor delegation + AI delegation) together build a stronger applied-relevance case for the manuscript.
