---
title: "Delegate Pricing Decisions to an Algorithm? Experimental Evidence"
authors: Hans-Theo Normann, Nina Rulié, Olaf Stypa, Tobias Werner
venue: VfS Annual Conference 2025 (Cologne) paper; arXiv 2510.27636
year: 2025
date: 2025-11-05
preregistered: osf.io/fh89u
bibtex_handle: normann_delegate_2025
pdf: ../normann_delegate_2025.pdf
relevance_to_manuscript: medium — algorithmic pricing delegation in IO; added in recent lit-review pass
---

# Normann, Rulié, Stypa & Werner (2025 WP) — *Delegate Pricing Decisions to an Algorithm?*

## Research question

In a repeated Bertrand pricing game (an IO setting where pricing algorithms have been associated with collusive outcomes), **do firm-participants delegate pricing decisions to a Q-learning algorithm**, and how do prices compare across delegation regimes?

The applied motivation is antitrust: pricing algorithms are increasingly used in real markets (gas stations, supermarkets, rental platforms), and the question of whether human-in-the-loop oversight prevents algorithmic collusion is policy-salient.

## Methods

- **Bertrand pricing experiment**, pre-registered (osf.io/fh89u). Ethical approval from GfeW (German Association for Experimental Economic Research).
- **Three treatments**:
  - **Baseline**: human participants set prices themselves.
  - **Full delegation**: at the start of each supergame, participants can delegate pricing to a self-learning (Q-learning) algorithm.
  - **Algorithmic recommendation with override**: the algorithm proposes prices; participants can override.
- DICE (Düsseldorf Institute for Competition Economics), Heinrich-Heine-Universität Düsseldorf.

## Key results

- **Delegation rates 45–86%** across conditions.
- **Higher delegation when participants can override** the algorithm's decisions (consistent with Dietvorst 2018: modifiability reduces algorithm aversion).
- **Prices are *lower* in algorithmic treatments than in baseline.** In both algorithmic treatments, prices are below the human-baseline level.
- The conclusion: "self-learning pricing algorithms can be collusive, [but] they can foster competition rather than collusion with humans-in-the-loop."

## Main takeaways

1. **High delegation rates (45–86%) to a pricing algorithm** in this Bertrand setting.
2. **Override possibility increases delegation** — consistent with Dietvorst 2018 modifiability finding.
3. **Human oversight prevents algorithmic collusion**: algorithms left alone might collude; algorithms with humans-in-the-loop foster competition.
4. **Policy implication**: human-in-the-loop oversight is a critical antitrust safeguard for algorithmic pricing.

## Relation to "Algorithms and Responsibility" (this manuscript)

Normann et al. is **not yet cited** in literature.tex but was added to the bib in the recent lit-review pass.

**Why this paper matters for the manuscript:**

**(1) Tangentially related, but a useful recent econ-experimental delegation paper.** Normann et al. is the most polished recent economics-experimental delegation paper (VfS Annual Conference 2025; pre-registered; DICE; arXiv econ.GN). It's not a moral-domain paper — the pricing decision is competitive, not redistributive — but it's the closest contemporary econ-experimental delegation study.

**(2) Modifiability finding parallels Dietvorst 2018.** Normann et al. find that "override" raises delegation from 45% to 86%. This is consistent with the manuscript's design choice to make delegation a binary (delegate vs not). Adding a "modify" option would likely raise delegation rates further per Normann et al.

**(3) High delegation rates (45–86%) are in line with the manuscript's ~50%.** Cross-design convergence on roughly half-or-more delegation in objective forecasting/pricing tasks. Suggests the moderate-delegation pattern is robust across designs.

**(4) Policy framing relevant for the manuscript's conclusion.** Both papers argue that *human-in-the-loop oversight* matters for AI deployment policy. Normann et al. about preventing algorithmic collusion; the manuscript about preserving moral accountability. Together they suggest that *enabling rather than removing human agency* is a robust policy recommendation across AI domains.

**Where to cite in literature.tex:**

- Optional addition at literature.tex paragraph 19 or 21. The paper is *tangential* to the manuscript's moral-domain focus, so could be cited briefly to widen the scope or omitted to keep the review tight.
- Most natural placement: a sentence in the conclusion's policy discussion noting that human-in-the-loop oversight is a robust policy recommendation across delegation contexts — citing Normann et al. for pricing/competition and Köbis et al. for unethical-instruction compliance.

**Limitation:** The pricing/competition domain is far from the manuscript's moral-domain prediction setting. Direct quantitative comparison is not apt. The paper is most useful as a methodological reference (recent econ-experimental delegation design) and as a policy-discussion citation.
