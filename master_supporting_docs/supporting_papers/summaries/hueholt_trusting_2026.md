---
title: "Trusting machines with morality — Delegating moral decisions to AI"
authors: Nicola Hueholt, Nora Szech
venue: European Economic Review
year: 2026
volume: 184
article: 105255
doi: 10.1016/j.euroecorev.2025.105255
affiliations: Karlsruhe Institute of Technology
bibtex_handle: hueholt_trusting_2026
pdf: ../hueholt_trusting_2026.pdf
relevance_to_manuscript: very high (Tier 1) — direct empirical test of moral-decision delegation to AI in an econ venue. Most current published competitor to the manuscript's design family.
---

# Hueholt & Szech (2026, EER) — *Trusting Machines with Morality — Delegating Moral Decisions to AI*

## Research question

Two questions, mapped 1:1 onto the manuscript's own scope:

1. **Delegation demand**: Is delegating a moral decision to AI more attractive than delegating it to another human?
2. **Mechanism**: Do (a) responsibility shifting and (b) belief adaptation contribute to individuals' willingness to delegate a moral decision to AI?

Theoretical premise: algorithm aversion in moral domains (Bigman & Gray 2018; Gogoll & Uhl 2018) and responsibility-shifting via delegation (Bartling & Fischbacher 2012) make opposing predictions when the delegate is an AI. Hueholt & Szech ask which dominates in a real-stakes moral-decision setting, and whether AI's intrinsic opacity *facilitates* responsibility shifting via motivated belief revision (moral wiggle room à la Dana, Weber & Kuang 2007).

## Methods

Two online incentivised experiments, total N = 5,639.

- **Decision task**: charitable donation choice with structural features of the trolley dilemma — choose between (Default Option A) a $5 donation to the Against Malaria Foundation providing one mosquito net for one child, or (Option B) a $25 donation to Helen Keller International providing vitamin A supplementation for ~25 children. Both options reduce under-5 mortality, so the choice is genuinely moral (helping fewer vs more beneficiaries) with no universally correct answer. The default + action-omission structure mirrors trolley framing.
- **Study 1**: 2×2 between-subjects: delegate type (Human vs AI) × framing (Gain vs Loss, where loss-frame reframes the decision as "destroying" one of the donation options). N = 800 students from a technical university.
- **Study 2**: 2×2 between-subjects in a representative German + US sample: delegate type (Human vs AI) × decision impact (RealCons: 1-in-10 donation actually paid vs HypoCons: never paid). N = 4,839.
- **Outcome measures**: delegation rate; perceived responsibility (wanted, felt, and moral duty, 5-point Likert); rated AI capability for moral decision-making; mind perception scales (agency, experience).
- **Identification**: random assignment to delegate type isolates the AI-vs-human comparison; decision-impact manipulation in Study 2 varies the burden of responsibility while holding the task constant.

## Key results

**Result 1 — Delegation to AI > delegation to humans in moral decisions.** Across both studies and both samples (students and representative population), participants delegate the moral decision *significantly more often* when the delegate is AI than when it is a human. Study 2 representative sample: 22.78%–23.30% delegation overall, with the AI advantage robust across age, gender, education. **This directly contradicts the standard moral-domain algorithm-aversion prediction.**

**Result 2 — Framing (gain vs loss) does not move delegation rates.** Contra Steffel et al. (2016)'s prediction that negative-valence decisions are delegated more, neither gain-vs-loss framing of the donation decision shifts the AI vs human delegation gap.

**Result 3 — Decision impact has *opposing* effects on AI vs human delegation.** When the donation is paid for real (RealCons), AI delegation **rises** (25.92% → 29.74%); human delegation **falls** (20.67% → 15.93%). The interaction (Decision Impact × Delegate) is highly significant (p < 0.001). When the moral stakes get real, participants pull *toward* AI and *away from* humans.

**Result 4 — Belief adaptation drives the AI-delegation appeal.** Real-consequence treatments produce *higher AI capability ratings* than hypothetical-consequence treatments — but only in AI treatments, not human ones. The pattern is consistent with motivated belief revision: facing a real moral burden, participants inflate their belief in AI's moral capability to justify delegating to it.

**Result 5 — Reduced perceived responsibility, especially for AI.** Delegation reduces self-reported responsibility ratings overall (by 0.76 on a 5-point scale, p < 0.001), and this reduction is *stronger* when delegating to AI than to a human (by an additional 0.24 units, p < 0.001).

## Main takeaways

1. **Responsibility shifting via delegation generalises to AI delegates.** The Bartling-Fischbacher tradition's central result (delegation reduces felt responsibility and motivates delegation) holds when the delegate is an algorithm.
2. **AI is a *more effective* moral-decision blame-shield than another human in this setting.** This reverses the standard algorithm-aversion-in-moral-domain prediction.
3. **The mechanism includes belief adaptation.** Participants don't just delegate — they revise their beliefs about AI's competence upwards under moral burden, which is moral wiggle room operating through opacity-enabled self-justification.
4. **Framing valence (gain vs loss) is not load-bearing.** What matters is the *reality* of consequences, not the negative-vs-positive framing.
5. **Methodological contribution**: a real-stakes trolley-style donation task that puts subjects in the decision-maker role with genuine moral content — a credible incentivised moral-domain delegation paradigm that may become a benchmark.

## Relation to "Algorithms and Responsibility" (this manuscript)

Hueholt & Szech is **the most current empirical competitor** to the manuscript's design family and should be treated as a Tier 1 reference, on par with Feier et al. 2022, Chevrier 2024, and Tontrup & Sprigman 2025.

**(1) Direct head-to-head precedent in a top econ venue.**
Published in *European Economic Review* (2026). Same research stream: AI delegation, moral decisions, responsibility shifting, incentivised online experiment. Failure to engage with this paper will be a referee-flagged omission at any top journal submission.

**(2) Opposite-direction finding on the central manipulation.**
The most consequential contrast: Hueholt & Szech vary *reality of moral consequences* (RealCons vs HypoCons) and find delegation to AI *rises* with reality — i.e., responsibility-shifting motive works for AI. The manuscript varies *punishment possibility* (on vs off) and finds delegation to AI *falls* when punishment is on — i.e., the responsibility-shifting motive *appears to fail* for AI on this margin.

These two findings can be reconciled rather than treated as contradictions, and the reconciliation is genuinely informative for the manuscript:

- Hueholt & Szech's manipulation operates on the **internal moral burden** of the decision — making the moral weight feel real rather than hypothetical.
- The manuscript's manipulation operates on the **external accountability** — making third-party judgement and punishment present rather than absent.
- The two channels can pull in opposite directions: AI is good for absorbing *internal* moral burden (because of belief malleability / wiggle room), but bad for absorbing *external* punishment (because it cannot bear accountability — see the Steffel framing).

This is potentially the cleanest framing for the manuscript's H1 reversal: AI is a *moral-burden* blame-shield but not an *accountability* blame-shield. The two manipulations isolate different mechanisms, and Hueholt & Szech provides the empirical anchor for the moral-burden leg.

**(3) Belief-adaptation mechanism is a genuine alternative to M3 (process ownership).**
Hueholt & Szech offer an explicit mechanism for *why* AI is a stronger moral-burden delegate than humans: people can flexibly revise their beliefs about AI's capability (motivated belief, moral wiggle room) in a way they cannot revise beliefs about a human delegate. The manuscript's M3 (process ownership / identity) is one candidate mechanism; belief adaptation is another. Felix should consider this seriously — both mechanisms predict delegation patterns but via different psychological routes, and Hueholt & Szech provides direct evidence for the belief-adaptation route.

**(4) Methodological complement.**
Hueholt & Szech use a one-shot moral-domain task (donation choice) with non-self-interested decision-makers (the chooser does not personally gain from either option). This is structurally close to the manuscript's design (Player A's prediction affects only Player B). The two designs are independently developed but converge on a similar configuration — useful triangulation.

**(5) Where to cite in literature.tex:**

- **Subsection 3 ("Responsibility perceptions of decisions involving algorithms")** ¶34, alongside Feier 2022, Chevrier 2024, Kobis 2025, Tontrup 2025. It belongs in the "most closely related study" tier, possibly as the second-closest precedent after Feier.
- **Discussion of the H1 reversal** in the "Where this paper fits" subsection: cite as the parallel finding on the moral-burden channel that the manuscript's punishment-channel manipulation complements.

**(6) Where to discuss in the manuscript's reconciliation section:**
The current literature.tex §3 ¶43 ("scope for the two studies to be parts of a single picture: Feier identifies the signal-extraction channel… we identify a process-ownership channel") should likely be expanded into a three-channel map: signal extraction (Feier), moral-burden / belief adaptation (Hueholt & Szech), and accountability / process ownership (this manuscript). Hueholt & Szech is the cleanest new node in that map.

**Important caveat — venue, recency, and replication risk**: Hueholt & Szech is just out (2026, accepted Dec 2025). Replication risk is non-trivial for a brand-new finding, particularly the "AI > human delegate" reversal of the standard moral-domain prediction. The manuscript should cite it as the closest current evidence but not over-anchor on it.
