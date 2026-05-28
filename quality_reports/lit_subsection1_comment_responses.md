---
title: Responses to inline comments — *Responsibility avoidance through delegation*
date: 2026-05-13
scope: literature.tex lines 5–18 (the "Responsibility avoidance through delegation" subsection)
status: DRAFT — proposals only; literature.tex not yet edited
---

# Comments addressed

Four inline `[Comment: ...]` markers in the subsection (lines 7, 15 × 2, 16). For each, this file provides:
- The comment verbatim
- A proposed revision (1–2 options)
- Brief rationale + tradeoffs

The order below matches the order of the comments in the file.

---

## Comment 1 (line 7) — Broaden the opening before the blame-shifting framing

**Comment:**
> [Comment: start even broader: "there are many reasons for why delegation emerges, such as differences in information, cost, ability, etc. Moreover, research suggests that delegation may serve other strategic goals, such as avoiding punishment."]

**Current opening of the subsection (line 9):**
> The political-science and public-choice literatures have long recognized that delegation can serve as a strategy for shifting blame onto an intermediary~\citep{weaver_politics_1986, fiorina_legislator_1986}. Experimental economics has established the same point in incentivised settings, primarily using modified dictator games.

**Issue.** The current opening jumps straight to blame-shifting as a motive without first acknowledging that delegation has well-established efficiency rationales (information, cost, skill). The reader is dropped into the responsibility-shifting subliterature without context.

### Option A — single broadening sentence prepended

Insert *before* the existing line 9, as the new opening of the subsection:

> Delegation has long been studied as an efficiency-enhancing institutional arrangement: principals delegate to agents who have better information, lower opportunity costs, or specialised skills. Alongside these efficiency motives, however, a separate literature has identified a strategic responsibility-shifting motive --- principals may delegate not because the agent is more competent or cheaper, but because doing so shifts moral responsibility for the resulting outcome away from the principal. The political-science and public-choice literatures have long recognized this strategic use of delegation~\citep{weaver_politics_1986, fiorina_legislator_1986}, and experimental economics has established the same point in incentivised settings, primarily using modified dictator games.

### Option B — two-sentence broadening

Slightly tighter, splits the "alongside" claim into two sentences and gives the responsibility-shifting motive its own framing:

> Delegation has long been studied as an efficiency-enhancing institutional arrangement: principals delegate to agents who have better information, lower opportunity costs, or specialised skills. A separate strategic motive, less developed in the classical principal-agent literature, is responsibility shifting: by interposing an agent between herself and the outcome, the principal may diffuse or evade blame for unpopular or harmful decisions. The political-science and public-choice literatures have long recognized this~\citep{weaver_politics_1986, fiorina_legislator_1986}, and experimental economics has established the same point in incentivised settings...

### Recommendation
**Option A.** Slightly shorter, more direct. Preserves the existing transition sentence into Weaver/Fiorina without needing further surgery.

### Citations
- No new bib entries strictly required. If you want a citation for the efficiency-rationale claim, the standard references are Aghion & Tirole 1997 (formal vs real authority) and Bolton & Dewatripont 2005 (textbook). Neither is currently in your bib; adding them is optional — the claim is canonical enough not to require a citation.

---

## Comment 2 (line 15) — Reframe Hill 2015 around his actual contribution

**Comment:**
> [Comment: focus more on contribution, i.e. not punishment as measure of blame, but survey questions]

**Current sentence:**
> \citet{hill_does_2015} provides a vignette-based corroboration in a legislative-delegation context. Subjects directly evaluate blame in unincentivised hypothetical scenarios; the resulting attributions track the patterns observed in incentivised experiments, suggesting that punishment captures more qualitative blame attributions reliably.

**Issue.** The current text frames Hill as primarily *validating the punishment-as-blame interpretation* of the canonical literature. But Hill's actual contribution is methodological: he addresses a real gap — prior work measured "blameworthiness" indirectly via punishment, and never tested whether subjects actually *perceive* the underlying behavior as blameworthy. Hill provides direct survey-based blame measurement.

### Proposed revision

> \citet{hill_does_2015} addresses a methodological concern about the canonical literature: punishment is an indirect proxy for blame, and prior experiments never tested whether participants actually perceive inequitable dictator-game allocations as blameworthy. Using vignettes in a legislative-delegation context, he elicits direct survey-based blame ratings and finds the same pattern as the experimental literature --- principals are judged less blameworthy than intermediaries, even when the intermediary is powerless.

**Rationale.** This (a) makes Hill's *gap-identification* contribution explicit, (b) makes his *direct-measurement methodology* the lead, (c) keeps the convergent-finding point (which is the substantive payoff for your manuscript) intact, (d) drops the "punishment captures blame reliably" framing that wasn't quite what Hill demonstrates.

### Shorter alternative

If you want it tighter (one sentence):

> \citet{hill_does_2015} addresses the concern that punishment is an indirect proxy for blame and shows, with direct survey-based blame ratings in a legislative-delegation context, that principals are judged less blameworthy than intermediaries even when the intermediary is powerless.

---

## Comment 3 (line 15) — Reframe Erat 2013 around his actual contribution

**Comment:**
> [Comment: focus on distribution: they think that the immorality of decisions in the dictator game is questionable, and they do a similar setup in which deception (in their eyes a more plausibly immoral act) can either be done oneself or delegated.]

(Reading "distribution" as a typo for "distinction" or "contribution".)

**Current sentence:**
> \citet{erat_avoiding_2013} provides a related demonstration that people are willing to pay to delegate the act of lying, consistent with delegation reducing the psychological cost of behavior that one expects to be judged negatively.

**Issue.** The current text frames Erat as just another delegation paper that confirms responsibility-shifting. The actual contribution is sharper: Erat *challenges* the dictator-game tradition's assumption that inequitable allocations are themselves blameworthy, and constructs a setup using *deception* — which has clearer moral content — to test the same responsibility-shifting logic.

### Proposed revision

> \citet{erat_avoiding_2013} questions a foundational assumption of the dictator-game tradition --- namely, that inequitable allocations are themselves clearly immoral --- and constructs a setup in which the principal can lie directly to a third party or pay an agent to lie on her behalf. A significant fraction of principals pay to delegate the lie, confirming the responsibility-shifting motive in a domain where the moral content of the underlying act is more clearly established.

**Rationale.** Makes explicit that Erat is *critiquing* the dictator-game framing as much as extending it. The "deception is a less ambiguous form of moral cost" framing is the substantive point Hill alluded to (and Felix's comment names directly).

### Shorter alternative

> \citet{erat_avoiding_2013} questions whether inequitable dictator-game allocations are themselves clearly immoral, and instead studies delegation of deception --- a domain with less ambiguous moral content. A significant fraction of principals pay an agent to lie on their behalf, confirming the responsibility-shifting motive for this clearer case.

---

## Comment 4 (line 16) — List of settings instead of detailed prose?

**Comment:**
> [Comment: maybe we can have a list of examples/specific settings in which blame is avoided through delegation, instead of going into lots of detail in each study? Also would this then better be placed in the first paragraph of this subsection? We can keep Steffel separate if it is that important.]

**My take.** Two parts of the comment to address.

### (a) On compressing to a list

The Comments 2 and 3 revisions above already compress Hill and Erat to one sentence each, focused on their *specific contributions*. With those revisions applied, the paragraph is already substantially tighter than the current version while keeping each paper's distinctive point. **I'd argue against further compression to a list**, because:

- Hill's contribution is *methodological* (direct vs indirect blame measurement). A list entry like "legislative delegation via direct survey blame ratings (Hill 2015)" reads as breadth and loses the methodological warrant for your design.
- Erat's contribution is *critical of the dictator-game tradition* (questioning whether inequity is even blameworthy). A list entry loses this critical-stance framing.
- Steffel's contribution is *load-bearing* (the credit-blame asymmetry that motivates your punishment-only design). Already a separate paragraph if you keep it.

So with Comments 2 + 3 applied, the result is naturally three tight sentences (Hill, Erat) plus the load-bearing Steffel block. No further compression needed.

### (b) On moving to the first paragraph

I'd advise against this. The first paragraph (lines 7–9, including Option A revision above) is setting up the *broad framing* of the subsection: efficiency motives vs strategic responsibility-shifting motives. Inserting Hill/Erat/Steffel there would clutter that framing.

The cleaner structure preserves what's already there:
- **¶1** (lines 7–9 + your broadening from Comment 1): efficiency vs strategic motives, public-choice introduction.
- **¶2 (B&F + Hamman)**: canonical experimental demonstration.
- **¶3 (Coffman + Oexl + randomization-device sentence)**: mechanism reinterpretation + closest precedent to algorithmic delegation.
- **¶4 (Hill + Steffel + Erat)**: methodological corroboration (Hill) + load-bearing asymmetry (Steffel) + critical extension to clearer moral content (Erat).
- **¶5 (summary)**: what's common across canonical setting, what's different in algorithmic setting.

### Recommended path

1. Apply Comments 2 and 3 (the Hill and Erat revisions).
2. Leave the paragraph as four sentences (Hill — Steffel — Steffel asymmetry — Erat).
3. **Don't** restructure to a list or move to the first paragraph.

### Alternative if you really want the list

If, after seeing the revised Hill/Erat sentences, you still prefer the list format, here is one option. Replace lines 15 (the current ¶15) with:

> Beyond the canonical dictator-game setting, the responsibility-shifting motive has been documented across several settings: legislative delegation~\citep{hill_does_2015}, where direct survey-based blame ratings replicate the punishment-based pattern; delegated deception~\citep{erat_avoiding_2013}, where the moral content of the underlying act is less ambiguous than dictator-game inequity; and decisions made on behalf of others~\citep{steffel_passing_2016}, where the credit-blame asymmetry --- \textit{people care more about avoiding blame for bad outcomes than about claiming credit for good ones} --- is established as a distinct driver of delegation.

This is a single-paragraph list that compresses all three papers without losing the substantive points each contributes. Tradeoff: it's denser and loses the rhetorical emphasis on Steffel's italicised asymmetry.

---

## Summary of changes proposed

| Comment | Location | Type of edit |
|---|---|---|
| 1 | Before line 9 (new opening sentence) | Insert broadening paragraph (Option A recommended) |
| 2 | Line 15, first sentence | Replace Hill sentence with proposed revision |
| 3 | Line 15, last sentence (Erat) | Replace Erat sentence with proposed revision |
| 4 | Line 15 paragraph structure | Recommended: keep paragraph structure as-is after applying Comments 2 & 3; do not move to first paragraph or convert to list (unless you prefer the list option above) |

No literature.tex changes have been made. Apply selectively when ready.
