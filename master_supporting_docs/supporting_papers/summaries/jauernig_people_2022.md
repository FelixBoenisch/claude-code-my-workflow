---
title: "People Prefer Moral Discretion to Algorithms: Algorithm Aversion Beyond Intransparency"
authors: Johanna Jauernig, Matthias Uhl, Gari Walkowitz
venue: Philosophy & Technology
year: 2022
volume: 35(1)
article: 2
doi: 10.1007/s13347-021-00495-y
bibtex_handle: jauernig_people_2022
pdf: ../jauernig_people_2022.pdf
relevance_to_manuscript: high — cited in lit.tex ¶19 and ¶27 (the M1 list); tests algorithm aversion beyond competence/trust
---

# Jauernig, Uhl & Walkowitz (2022) — *People Prefer Moral Discretion to Algorithms*

## Research question

Why do people resist algorithmic moral decisions even when the algorithms are transparent and competent? The standard answers (opacity, fear of bias) are not enough. The paper proposes that **people specifically value the human capacity for *moral discretion*** — the ability to transcend rules in light of specific circumstances.

Two specific questions:
1. **Do people prefer humans with discretion to algorithms that rigidly apply human-created fairness principles?** (Study 1)
2. **Is the preference for humans about "humanness per se" or specifically about the capacity for moral autonomy?** (Study 2)

## Methods

- Two **incentivised lab experiments**.
- **Setting**: two-person work teams generate a joint budget through a real-effort task; a "decider" then allocates the budget between the workers. Distribution conflict between workers.
- **Study 1**:
  - Workers know the decider can be either a human or an algorithm.
  - Algorithm is *rule-bound*: it deterministically applies a fairness principle (proportional to effort or equal split) that was *chosen by a human* — so the algorithm is fully transparent and rule-following.
  - Workers express a preference for human or algorithmic decider, with monetary costs/benefits to the choice.
- **Study 2**:
  - Same setting but the algorithm is given decision *autonomy* (can deviate from any fairness rule, like a human can).
  - Tests whether the preference is for human-ness or specifically for moral autonomy.

## Key results

**Study 1**: People strongly prefer humans with discretion over rule-bound algorithms. The preference is robust to monetary penalty for choosing the human.

**Study 2**: When the algorithm has moral autonomy, the preference for humans largely *disappears*. People don't dislike algorithms because they aren't human — they dislike algorithms because they're rule-bound. **The valued quality is moral discretion / autonomy, not biological humanness.**

## Main takeaways

1. **Algorithm aversion in the moral domain is partly about a desire for moral discretion** — the ability to transcend rules. Transparent rule-following doesn't satisfy this.
2. **Humanness per se is not the issue.** When algorithms are granted autonomy (within the experimental frame), much of the aversion disappears.
3. **Transparency advocates may be solving the wrong problem.** Making algorithms more transparent and more rule-bound may not address the underlying objection.
4. The paper sharpens what's specifically "human" about moral decision-making — it's not the substrate but the *flexibility* to apply principles to cases.

## Relation to "Algorithms and Responsibility" (this manuscript)

Jauernig et al. is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19 as evidence that moral domain decisions amplify algorithm aversion, and in paragraph 21 in the list of mechanism candidates ("anticipated reputational or moral costs"). The 2022 paper is part of the wave of recent work on the algorithm-aversion-in-moral-domain question.

**Why this paper matters for the manuscript:**

**(1) The "moral discretion" framing is a candidate mechanism *adjacent* to your M3.** Jauernig et al. argue that what people value about human moral decision-making is the *autonomy* to transcend rules. The manuscript's M3 (process ownership / identity / accountability salience) is a *principal-side* counterpart: what Player A values about doing the prediction herself is the autonomy to apply judgment, rather than offloading to a rule (Bernoulli draw). Both frameworks identify "autonomy in the moral act" as the central thing — Jauernig on the receiver/observer side, the manuscript on the principal side.

**(2) The manuscript's algorithm is *exactly* the kind Jauernig & co subjects dislike.** A Bernoulli draw at A's empirical accuracy is the rule-bound, transparent, non-autonomous algorithm Jauernig's subjects rejected in Study 1. The manuscript's relatively high delegation rates (42–59%) might be lower than they would be in a more general population — selection into Prolific participation, and the abstract framing of "calibrated Bernoulli" rather than vivid "robot deciding your loan," may reduce the aversion. This is a useful framing for thinking about external validity.

**(3) Jauernig's null on humanness-per-se is consistent with the manuscript's design choice.** The manuscript deliberately avoids anthropomorphising the algorithm (it's described as a calibrated Bernoulli draw, not as an AI agent with personality). Jauernig's finding that *human-ness isn't the issue* — *discretion is* — supports this design choice. The manuscript's algorithm is rule-bound and transparent, so it should be the prototypical "averted" algorithm in Jauernig's framework. The fact that ~50% of subjects still delegate suggests the prediction task may be on the *edge* of the moral domain, or that the equal-performance calibration overcomes some of the discretion-related aversion.

**(4) Jauernig provides a useful contrast for the manuscript's M3.** Jauernig: people value moral discretion *in the decider* (the algorithm is averted because it has no discretion). Manuscript M3: principals value *being* the moral decider themselves (they prefer to engage directly when accountability is salient). These are not the same mechanism but they share a common philosophical premise — moral decisions are valuable as *exercises of autonomy*, not just as outcomes.

**Where in literature.tex:**

- Paragraph 19: correctly cited as a moral-domain aversion paper.
- Paragraph 21: correctly cited as part of the mechanism-candidates list.

**Worth borrowing:** The "moral discretion" framing is more philosophically grounded than the manuscript's current M3 framing ("process ownership / identity / accountability salience"). The manuscript's discussion section could engage with Jauernig's finding directly: "Jauernig et al. (2022) show that observers value moral discretion in deciders; our manuscript shows that principals value being the locus of that discretion themselves. The two findings are complementary — both reveal that moral decisions are not just about outcomes, but about who exercises judgment."

**Methodological note:** Jauernig's design — workers choose between human and algorithmic deciders for the *outcome* that affects them — is the *flip side* of the manuscript's design (where Player A chooses whether to be the decider herself or to delegate). The combination of these two designs sketches the supply-and-demand side of algorithmic delegation in moral domains: subjects don't want to delegate moral decisions to algorithms (manuscript H1 reversal), and subjects don't want algorithms to be the moral decider for them (Jauernig Study 1).

**Limitation worth flagging:** Jauernig's setting has a clear fairness norm (proportional to effort), making the "discretion" question concrete. The manuscript's prediction task has no analogous fairness norm — there's nothing for an algorithm to be *too rule-bound about*. So the Jauernig mechanism may not apply directly. The manuscript's M3 reading should not lean too heavily on Jauernig's framework, since the moral content of your task is different in kind.
