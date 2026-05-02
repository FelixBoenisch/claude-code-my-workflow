# `literature.tex` — old vs new

## Overview

The old `literature.tex` is a **343-line working draft** with three named
subsections (blame avoidance through delegation; delegation to algorithms;
responsibility perceptions of decisions involving algorithms) and a large
amount of supplementary material: long quoted passages from Maasland et al.,
Heaton et al., Bigman & Gray, Pezzo & Pezzo, Shank et al., Langer & Landers,
Coffman, Steffel et al., a structural bullet outline at the end, two long
paragraph-length quotes from a survey-style passage on machine aversion,
multiple bracketed planning notes ("[Note: I have to justify somewhere..."),
and a list of 8+ references intended for citation.

The new `literature.tex` is **37 lines, four short subsections** (responsibility
avoidance through delegation; delegation to algorithms; responsibility
perceptions of decisions involving algorithms; **plus a new "Where this paper
fits" subsection that includes a substantive engagement with the Feier et al.
discrepancy**). Each subsection is one or two well-structured paragraphs.

## What changed in the prose

The new lit review is not a verbatim trim of the old; it's a re-write that
covers the same papers (Bartling-Fischbacher, Coffman, Hamman, Oexl-Grossman,
Hill, Steffel-Williams, Erat, Dietvorst, Logg, Burton/Mahmud/Chugunova
reviews, Berger, Litterscheidt, Sharan, Stein, Bigman, Jauernig, Castelo,
Bogert, Gogoll-Uhl, Goldbach, Niszczota, Kurtzberg, Pezzo, Liu, Shank, Tobia,
Kirchkamp-Strobel, Feier) with much tighter phrasing.

The single most consequential **addition** in the new lit is the **"Reconciling
our findings with Feier et al." paragraph**, which argues that the differential
punishment in Feier et al. is most plausibly read as a signal-extraction
channel that the new design closes off by construction, while our design
isolates a different and milder margin (process ownership / motivational
salience for the principal). This paragraph did not exist in the old draft.

## Dropped items

### Planning notes / brackets

- `[consistent naming: 'delegator', 'delegee/intermediary', 'punisher/third party/evaluator...']` — naming-decision note.
- `[intro paragraph]` — placeholder for an opening intro paragraph for the section. The new lit opens with a short framing paragraph.
- `[General evidence] Bystander effect (Fischer et al 2011)` — a planned reference to the bystander-effect literature as a general parallel. **Currently absent from the new lit. Worth considering** as a one-sentence parallel since it's a nicely intuitive prior.
- `[Experimental Evidence]` and `In the political science literature the motive of blame avoidance through delegation has been discussed extensively` — two intended subsection cuts. The political-science framing survives in the new lit's first paragraph (Weaver, Fiorina citations).
- `[maybe change order: Coffman first, also because oexl explicitly extend bartling fischbacher]` — paragraph-ordering note. The new lit puts Bartling first then Coffman + Oexl together, which matches the intent.
- `[In all of these studies notions of blame and responsibility have been operationalized using punishment...]` — a planned bridge sentence on punishment-as-operationalization.
- `[Maybe distinction between die treatmnet and my experiment?; maybe move to end of subsection]` — design-choice note about contrasting with the die-roll treatment.
- `[Note: I have to justify somewhere that here, a third party is still affected, but the delegator does not choose with certainty and the incentives are actually aligned, like the evaluator can always just think ''he tried his best'', so why would punishment be different?]` — **an important self-critique**. Currently addressed in the new design section (last paragraph: "incentives of Player A and Player B are nominally aligned"). Could also be flagged in the lit if you want to surface the puzzle earlier.
- `[Is algorithm aversion only found when making decisions for oneself, because there blame avoidance may be a less strong motive than when making decisions for others?]` — open question, **dropped**.
- `[Present Findings] [Literature Review studies] [Delegation when payoff relevant for otehrs.] [Say what influences delegation and how this can be alleviated, then mention review papers last.]` — structural-outline notes for the §Delegation-to-Algorithms paragraph.
- `[do not talk about maasland weißmüller here, because they talk about blame avoidance but include no measure on it...talk about it in the results section]` — the old plan was to discuss Maasland & Weißmüller in results, not lit. The new manuscript doesn't cite them at all (the .bib still has `maasland_blame_2022` but it's not `\cite`d).

### Quoted reference material (`\textcolor{blue}{...}`)

These long quotations from other papers were never meant to remain in the
final draft, but they record specific framings the author wanted to engage:

- **Maasland & Weißmüller quote (lines 35–49)** on individuals shifting mental burden + factual responsibility through delegation; Erat (2013) on delegating lying; Steffel et al. on cost-of-feeling-responsible; Newman et al. (2020) on perceiving algorithmic HR decisions as less fair (selection or layoff). This last point — Newman et al. on HR fairness — is **not currently cited anywhere in the manuscript**. Worth noting if you want to bring an HR-domain example into the lit.
- **Mahmud quote (lines 76–78)** on the algorithm-aversion-as-deviation-from-rational framing.
- **Long quote on responsibility attributions to algorithms (lines 91–100)** from a passage that includes Kurtzberg & Naquin 2004, Pezzo & Pezzo 2006, Liu & Du 2021, Shank et al. 2019. Most of these citations make it into the new lit (4th paragraph of §3 in the new lit), but the Bigman & Gray (2018, p. 21) reference is left as a hanging citation in the old draft.
- **Langer & Landers quote (lines 105–119)** on physicians being shielded from blame by following automated recommendations; second-party uncertainty about who to blame in shared human-system decisions; the Pezzo, Tobia, Jutzi, Nolan, Longoni, Promberger references. **The Langer & Landers paper itself is not currently cited.** The Tobia (2021) physician-AI-liability point survives in the new lit.
- **Coffman extended quote (lines 258–263)** on how decreased punishment under intermediation is not due to diffusion of responsibility but to lack of direct interaction. The point survives in compressed form in the new lit; the verbatim quote is gone.
- **Steffel et al. quote on credit-vs-blame asymmetry (lines 269–283)**: "people care more about avoiding blame for bad outcomes than getting credit for good outcomes". This is **a key conceptual point that survives in the new mechanism story (process ownership / asymmetric utility from being the proximate cause of good outcomes)** — but the Steffel quote itself is not in the lit.
- **Long quote on punishment-as-blame-proxy (lines 162–181)**: makes the methodological case for using punishment as the operationalization of blame; argues that blame is most relevant when operationalized into punishment (von Grundherr et al., 2021); cites Klepper & Nagin (1989) on the deterrence effect of punishment vs blame. **The new manuscript doesn't include this defence.** Could be useful if a referee asks "why punishment as the operationalization?".
- **Long machine-aversion quote (lines 185–301)** — a near-page-length quote from another paper covering: machine aversion as a recurring phenomenon (Dzindolet et al., 2002); algorithm aversion in moral domains (Goldbach 2019, Niszczota & Kaszás 2020, Gogoll & Uhl 2018); the trust-vs-blame-shifting question (Robinette 2016); blame avoidance in political sciences (Weaver 1986); EU blame games (Heinkelmann-Wild & Zangl 2020); officials in the US (Maestas 2008); franchise networks (Hardy 2019); public choice theory (Fiorina 1986); experimental evidence (Fischbacher 2008); Hill 2015; Oexl-Grossman 2013; algorithmic outrage asymmetry (Bigman 2020); moral attributions weakened for AI (Gamez 2020); humans as "moral crumple zones" (Elish 2019); responsibility as predictor of punishment (Bolton & Ockenfels 2000, Fehr & Schmidt 1999); machine self-exculpation; closing conjecture and rationale; perceived utility definition (Dzindolet 2002); risk attitudes incorporation (O'Donoghue & Somerville 2018). **Almost none of this elaborate context survives in the new lit** — too much material for one section. But the conjecture framing ("Delegators are rewarded differently for delegating other-regarding tasks to artificial agents as compared to human agents") is the precise hypothesis that Feier et al. test, so it's implicitly in the new lit's Feier discussion.

### ChatGPT-tagged paragraph (yellow text, lines 135–141)

Chris Roth paper note: "We add to the literature by (i) comparing the effect of stories to that of statistics over time, and (ii) providing systematic, theory-guided evidence on mechanisms with a focus on the role of qualitative information." — appears to be a stylistic model the author wanted to follow, not an actual citation. Dropped.

### Final structural outline (lines 304–316)

A bullet outline summarising the entire literature section's intended structure. The new lit implements roughly this structure but in prose. Dropped.

### Reference list at the end (lines 318–344)

A bibliographic list of papers the author intended to cite or already cited:
- Bartling & Fischbacher (2011) — cited as 2012 in new
- **Chang, Solomon & Westerfield (2016)** — *Looking for someone to blame: delegation, cognitive dissonance, and the disposition effect* (Journal of Finance). **Not cited in the new manuscript.** A finance-domain example of delegation-and-blame that would fit well in §literature.
- Coffman (2011) — cited
- **Duch, Przepiorka & Stevenson (2015)** — *Responsibility attribution for collective decision makers* (AJPS). **Not cited.** A political-science complement to Hill (2015).
- **El Zein, Bahrami & Hertwig (2019)** — *Shared responsibility in collective decisions* (Nature Human Behavior). **Not cited.** A high-profile group-decision-making piece on responsibility.
- Oexl & Grossman (2013) — cited
- **Palmeira, Spassova & Keh (2015)** — *Other-serving bias in advice-taking: when advisors receive more credit than blame* (OBHDP). **Not cited.** Asymmetry of credit/blame in advice-taking — relevant to the process-ownership story.
- Steffel, Williams & Perrmann-Graham (2016) — cited
- **"Blame and praise: responsibility attribution patterns in decision chains"** — uncited, no author given.
- **"Generative AI Triggers Welfare-Reducing Decisions in Humans"** — uncited, recent generative-AI paper.
- **"Potentially cite Sveta and Dorothea papers"** — author note.
- **"Check mamud section 2 on different definitions of an algorithm"** — author note.

**Worth scanning** for any of these that you'd want to bring into the lit, especially Chang et al. (delegation-cognitive-dissonance in finance), Palmeira et al. (asymmetric credit/blame in advice-taking) and El Zein et al. (Nature paper on shared responsibility).

### Substantive notes that didn't survive

- The note about **why punishment patterns might differ even when incentives are aligned** ("the evaluator can always just think 'he tried his best'") — this nuance is implicit in the new manuscript's H2 framing but is not spelled out in the lit.
- The observation about **Feier et al. that the same delegator also plays the role of the evaluator** ("if I delegate this can either be because I think I am better than algorithm or because of other reasons. Hence when I evaluate I may judge the decision according to what I did or if I am aware that I delegated to avoid responsibility, I could also tell myself that I won't allow this for others") — this is a specific design critique of Feier et al. that *partly* survives in the new lit (the third bullet of "three features that complicate the inference" in the §Where this paper fits paragraph) but the within-subject-evaluation argument is more compressed.
- The closing **bullet logic / "logic"** outline of the section: "algorithm aversion -> algorithm use in moral domains -> reasons for delegation/not delegation -> responsibility/blame -> blame literature (non-algorithmic) -> experimental research on blame (Fischbacher...) -> algorithmic outrage asymmetry -> gap in literature and contribution + why is it important to answer the research questions (they motivate both sides of the hypothesis)". The new lit follows this logic but doesn't explicitly call out "both sides of the hypothesis" — i.e., the old plan was to motivate H1 in **both directions** (more delegation if blame can be shifted; less delegation if you're punished for the act of delegating). The new lit only motivates H1 in the original direction.

## Why the changes (where I can infer)

- The compression came from converting a planning document into prose.
- The **"Reconciling our findings with Feier et al."** paragraph is a direct response to the methods referee's concern about over-claiming the contribution and under-engaging with the discrepancy. This is one of the stronger improvements over the old draft.
- The dropping of long quoted passages reflects standard manuscript-cleanup; those quotes were source material, not draft text.
- The dropping of Newman et al., Langer & Landers, Chang et al., Palmeira et al., El Zein et al., Duch et al. is mostly because the new lit goes deep on Bartling/Coffman/Oexl/Hill/Steffel/Erat for the responsibility side and Dietvorst/Logg/Burton/Mahmud/Chugunova for the algorithm side, plus Feier/Kirchkamp directly. Adding more would dilute, but several of the dropped citations would strengthen specific sub-arguments.
