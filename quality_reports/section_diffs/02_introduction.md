# `introduction.tex` — old vs new

## Overview

The old `introduction.tex` is a **scratchpad**, not a draft: 209 lines of
bullet-outlines, alternative draft paragraphs (`\textcolor{red}{...}`),
ChatGPT-generated paragraphs, quoted material from Feier et al. and several
other papers (`\textcolor{blue}{...}`), planning notes for the section's
intended structure, and a long list of paper references that were intended
to be cited. There is no single "old introduction" — there are several
candidate openings stitched into the same file.

The new `introduction.tex` is a polished 6-paragraph manuscript intro:
opening (algorithms ubiquity + the navigation-app vignette), two-question
framing (viability + motivational salience), design pin-down, two design
features distinguishing from Feier et al., the two findings (with the H1
reversal hedged with the preregistered-direction note), the mechanism
(process ownership as candidate, not established), the three literatures
this contributes to, and the section roadmap.

## What changed in the prose

Approximately none of the old text is preserved verbatim. The new
introduction is essentially a fresh draft that takes the old's intent
("explain that algorithm-mediated decisions raise responsibility questions
+ describe the design + summarise findings") and writes it in proper prose.

Every concrete claim about the experimental findings (`42.5\% / 59.3\%`,
`p=0.049`, "Player B's punishment of Player A is statistically
indistinguishable") was already in the old draft as a planned summary; it
just hadn't been turned into prose yet.

## Dropped items

### Planning bullet outlines (Motivation block, lines 68–74)

- "This project joins in on the AI hype in the literature." [framing register choice — kept implicit]
- "Maybe you came here with a friend and they didn't need google maps to arrive at Hotel Grünau" [a presentation-style anecdote about the map-app vignette, more colloquial than the new "if you and a friend arrive late because she relied on a navigation app"]
- "This project does not aim to answer the normative question of who should be blamed or credited. The algorithm, the user of the algorithm, the creator of the algorithm? But it is entirely about the positive description of who is actually blamed, at least in a limited, very controlled lab experiment." [Explicit positive-vs-normative scope statement. **Worth considering bringing back** as a one-sentence scope clarifier.]

### Planning bullet outlines (Design + RQs block, lines 76–87)

- The original framing of the two RQs as **"Can you avoid punishment for bad decisions by delegating to an algorithm?"** with the explicit "since we are using punishment here instead of rewards, it makes sense to mostly focus on bad decisions, because there is not so much scope for punishment for good decisions" [a justification for the asymmetric attention to bad outcomes — currently absent from the new manuscript].
- The note that **"In principle it also makes sense to look at good outcomes, credit and blame for a decision can be treated very differently"** [an aside on credit vs blame asymmetry that was excised].
- The bullet on testing **"whether these beliefs translate into the decision to delegate"** as an explicit third RQ. The new manuscript folds this into the H1 motivation but doesn't list it as a standalone question.
- The mention that **"Bartling Fischbacher have these two treatments but instead of the algorithm the delegator can delegate to another person"** as an explicit comparison point [moved into the literature section].

### ChatGPT-generated paragraphs (red text, lines 16–21 and 89–91)

Two long ChatGPT-drafted paragraphs that proposed alternative openings:

1. **"Algorithmic decision-making is increasingly integrated into high-stakes domains such as criminal justice, hiring, healthcare, and finance..."** — a sweep through the policy frame leading into the two RQs. Closed with a structured "Our findings are threefold" preview that the new intro replaces with a 2-finding preview (matching what the data actually shows).
2. **"The integration of algorithms into decision-making processes has become increasingly prevalent across various sectors..."** — a different alternative opening focused on the responsibility-attribution problem and the use of algorithms as a "shield against potential backlash". Some of this language echoes in the new intro but is more bounded.

### Quoted Feier et al. abstract (blue text, lines 25–27, 33–65)

A long verbatim quote of the Feier et al. (2022) abstract describing their experimental design and finding ("we found no differences between judgments toward human and artificial agents in the event of good outcomes... when negative outcomes occurred, delegators fared significantly better if a machine agent caused the failure"). **Useful as a reference if you want to re-engage Feier et al. in the intro itself** rather than only in §literature.

### Quoted Mahmud et al. material (blue text, lines 120–142)

Two long quoted passages on the contexts where algorithms are used (healthcare imaging, robo-advisors, demand forecasting, hiring, marketing, customer-service chatbots) and the framing of algorithm aversion as deviation from rational behaviour. **Could be a source for an applied-domain expansion of the intro's opening sentence.**

### Quoted Heaton et al. material (blue text, lines 147–209)

Eight separate quotations from Heaton et al. on:

1. The distinction between responsibility (designed/deployed ethically) and accountability (answerable to performance and outcomes).
2. The position that responsibility for negative outcomes should be shared among all actors (developers, operators, data providers, regulators, algorithms).
3. "As decision-making algorithms become more ubiquitous, it is crucial to understand how they impact public perceptions of trust and blame."
4. The asymmetry between using algorithms for self vs others (see specifically: "you could say you use algo more if it is blamed, versus if you use it yourself you use it less. However, maybe if you use it yourself, you can still be happy that it was not your fault, but the algorithms, so you have an excuse." — **a very interesting interpretive thread that's gone**).
5. Examining how agency, responsibility and accountability impact trust/blame as a barrier to adoption.
6. USACM/EUACM principles around accountability.
7. A reference to the "responsibility gap" (Mittelstadt et al.) where neither developers nor algorithms are fully responsible.
8. The Tobia, Nielsen, Stremitzer (2021) liability paper — cited in passing now, but the full treatment of physician AI use and legal shielding is gone from the intro.

These quotations were a literature scan to motivate the intro; the new intro elects to motivate from the responsibility-avoidance / algorithm-aversion literatures specifically and leaves the broader ethics-of-AI conversation to other papers.

### Planning notes (interspersed brackets)

- `[explain clearly the punishment motives. You can be punished for making the wrong decision and making the wrong delegation decision. Can we differnetiate between these? Outcome vs. intention based.]` — a note about distinguishing outcome-based from intention-based punishment. **The new manuscript does treat punishment as essentially outcome-based but doesn't develop the outcome-vs-intention dichotomy explicitly.**
- `[Optional: The remainder of the paper is structured as follows...]` — kept (last paragraph of new intro).
- `Inspired from the ogoing ethical and legal debate...` — incomplete sentence fragment.
- The full "Paragraph on..." structural outline at lines 89–117 (introduction-to-algorithms paragraph; role-of-algorithms-shaping-accountability paragraph; ethical-and-practical-implications paragraph; research-questions paragraph; related-work paragraph; empirical-approach paragraph; practical-relevance paragraph; experimental-design paragraph; results paragraph; "any big policy pieces, such as the AI Act or so" paragraph). The new intro implements roughly this structure but more compressed.
- `Tobia, K., Nielsen, A., & Stremitzer, A. (2021). When does physician use of AI increase liability?` — explicit reference, dropped from the intro but retained in the literature section.

### One-line interpretive observations worth preserving

- **"so responsibility is desired to be shifted away from users of algorithms to algorithms itself to facilitate adoption. on the other hand creators should be held responsible so that they have a stronger incentive to design ethical algorithms."** — a nice two-sided framing that disappears in the new intro. **Worth bringing back** if you want a sharper hook for the regulatory-implications paragraph.
- The Heaton-quote-derived observation about whether you use an algorithm for yourself vs others (point 4 above). This is genuinely interesting and would fit well as a one-sentence motivator.

## Why the changes (where I can infer)

- The intro's tightened length is a direct response to the `--peer AER` editor desk review note: "consider opening with the punchline rather than the algorithm-ubiquity boilerplate". The new intro still opens with ubiquity (paragraph 1) but reaches the two RQs by paragraph 2.
- The mechanism reframing ("candidate hypothesis", "experimenter demand cannot be ruled out") came directly from the methods referee.
- The "within the bounds of the setting we study" language responded to the domain referee's policy-framing-overreach concern.
