---
title: "Receiving credit: On delegation and responsibility"
authors: Cédric Argenton, Jan Potters, Yadi Yang
venue: European Economic Review
year: 2023
volume: 158
article: 104522
doi: 10.1016/j.euroecorev.2023.104522
bibtex_handle: argenton_potters_yang_2023
pdf: ../argenton_potters_yang_2023.pdf
relevance_to_manuscript: high — credit-side counterpart of responsibility-shifting; added for subsection 1 breadth
---

# Argenton, Potters & Yang (2023) — *Receiving credit: On delegation and responsibility*

## Research question

The literature on blame-shifting through delegation is well established. Argenton, Potters & Yang ask the **mirror-image question**: does one receive **credit** for taking a *good* decision personally, as compared to delegating it to someone else?

Machiavelli (1532) provided the conjecture: "Princes ought to keep affairs of grace in their own hands" — i.e., favourable decisions should *not* be delegated. The paper tests this empirically.

A secondary contribution: does the responsibility-attribution model that B&F (2012) developed for punishment extend symmetrically to rewards?

## Methods

- **Lab experiment** using a four-player delegated dictator game (adapted from Bartling & Fischbacher 2012).
- **Players**: Dictator (D), Delegate (B), two Recipients.
- **Decision**: D chooses between
  - **Fair** allocation: equal split among all four.
  - **Unfair** allocation: D and B get more; recipients get less.
  - **Delegate** to B, who then chooses between fair and unfair.
- **Key difference from B&F**: instead of allowing recipients to *punish* D or B, recipients can *reward* D or B (or both) when a fair allocation is realised.
- **Theoretical extension**: the authors show that B&F's responsibility-attribution model extends to rewards under symmetric assumptions — if "responsibility" is attributed in proportion to a player's contribution to the probability of the outcome, then rewards should mirror punishments.

## Key results

**Result 1 — Credit-taking is symmetric to blame-shifting.**
The dictator receives a higher reward when she chooses the fair allocation directly than when she delegates and the delegate chooses fair. Conversely, when the dictator delegates, the delegate receives a higher reward than the dictator.

**Result 2 — Direct fair choice vs delegation-to-random-device that produces fair.**
The dictator receives the same reward when she chooses fair directly as when she delegates to a random device that happens to produce a fair outcome. Random devices do not absorb credit — consistent with the B&F assumption that "only people, not nature" can be held responsible.

**Result 3 — Machiavelli's prescription is empirically supported.**
The Machiavellian advice ("keep favourable decisions in your own hands") is borne out: dictators who want credit for fair allocations should *not* delegate.

**Result 4 — Asymmetry note (literature comparison).**
Prior work suggests reward responses to good behaviour are weaker than punishment responses to bad behaviour (Offerman 2002; Sefton et al. 2007). The authors flag that responsibility attribution itself might be asymmetric — but their experiment doesn't directly resolve this. Their main message is that the *structural pattern* of responsibility attribution (dictator vs delegate vs random device) is symmetric across rewards and punishments.

## Main takeaways

1. **Responsibility attribution is a two-sided sword.** Delegation reduces both blame for bad outcomes *and* credit for good outcomes.
2. **The B&F responsibility-attribution model extends to rewards** with the same structural predictions.
3. **Random devices don't absorb credit** — consistent with the asymmetric framing that people are responsibility-bearing actors while devices are not.
4. **The Machiavellian prescription is rational** under the responsibility-attribution model: keep favourable decisions personal, delegate unfavourable ones.
5. **Open question on overall magnitude**: although the structural pattern is symmetric, the *strength* of credit-giving may be smaller than blame-imposing (negativity bias).

## Relation to "Algorithms and Responsibility" (this manuscript)

Argenton, Potters & Yang is **not yet cited** in literature.tex but should be added to subsection 1 per the recent restructuring discussion. It's the credit-side complement to the B&F tradition.

**Why this paper matters for the manuscript:**

**(1) Directly relevant to the credit-blame asymmetry that anchors Steffel et al.**
The manuscript leans on Steffel et al. (2016) for the claim that "people care more about avoiding blame for bad outcomes than about claiming credit for good ones." Argenton, Potters & Yang provide the cleanest *experimental* foundation for the credit-side half of that asymmetry: they show that the same structural pattern of responsibility attribution holds for credit as for blame, in the same B&F design family. This strengthens the citation chain for the credit-blame framing.

**(2) Confirms that random devices don't absorb credit.**
Highly relevant for the manuscript's design rationale. The algorithm in the manuscript is structurally close to a random device (Bernoulli draw at A's empirical accuracy). Argenton et al. show that random devices don't absorb credit — by symmetry with the B&F-style responsibility-attribution model, this suggests random-device-like algorithms also shouldn't absorb blame much. This is consistent with the manuscript's H2 null and provides a defensible theoretical anchor.

**(3) Cite alongside B&F for the bidirectional responsibility-shifting claim.**
When the manuscript discusses responsibility-shifting in subsection 1, it naturally cites B&F for the blame side. Argenton et al. is the corresponding credit-side anchor. Citing both gives the manuscript a more complete framing.

**(4) The Tilburg / Nanjing affiliations matter for the lit-review legitimacy.**
A peer-reviewed EER 2023 paper by Argenton (Tilburg) and colleagues is exactly the kind of citation a top-econ submission needs to validate the breadth of the responsibility-shifting tradition.

**Where to cite in literature.tex:**

- Paragraph 15 (subsection 1 breadth-list): cite as the credit-side complement to the punishment-based literature. Drafted earlier:
  > "...The mirror image holds on the credit side: delegators receive less credit for good outcomes they delegate \citep{argenton_potters_yang_2023}..."
- Possibly also in the conclusion / mechanism discussion if you discuss the credit-blame asymmetry in detail. Argenton et al. provide the structural-pattern claim; Steffel et al. provide the magnitude-asymmetry claim. Both are useful.

**Cross-references in the manuscript's existing citations:**

- Chevrier & Teixeira 2024 cite Argenton et al. 2023 as part of the responsibility-shifting literature, grouped with B&F, Coffman, Oexl.
- Tontrup & Sprigman 2025 cite Argenton et al. 2023 in their reference list.
- This recent paper is increasingly part of the standard responsibility-shifting reading list.

**Methodological note**: Argenton et al. design is a faithful B&F adaptation — same four-player structure, same fair/unfair allocation, same recipient-mediated punishment-or-reward. This makes their results directly comparable to B&F. The manuscript could note this when discussing how the recipient's behaviour generalises across blame and credit.

**Important caveat**: The Argenton et al. paper is about *human* delegation, with no algorithmic component. The credit-side symmetry result they document is specifically about delegation to other humans (or to a random device). The manuscript could speculate on whether credit also gets attenuated when delegating to an algorithm, but that's an extension beyond the Argenton et al. paper.
