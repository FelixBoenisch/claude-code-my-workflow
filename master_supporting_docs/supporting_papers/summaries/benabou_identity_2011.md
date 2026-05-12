---
title: "Identity, Morals, and Taboos: Beliefs as Assets"
authors: Roland Bénabou, Jean Tirole
venue: Quarterly Journal of Economics
year: 2011
volume: 126(2)
pages: 805–855
doi: 10.1093/qje/qjr002
bibtex_handle: benabou_identity_2011
pdf: ../benabou_identity_2011.pdf
relevance_to_manuscript: high — theoretical foundation for M3; cited in lit.tex ¶33
---

# Bénabou & Tirole (2011) — *Identity, Morals, and Taboos: Beliefs as Assets*

## Research question

Standard models of social preferences (inequity aversion, reciprocity, altruism) struggle to explain several puzzling features of moral behaviour:
- Why the same people behave morally and immorally depending on context, framing, and "thin veils" of plausible deniability.
- Why people sometimes turn on those who behave too well (resentment of moral exemplars).
- Why "taboo trade-offs" exist — people refuse to even *contemplate* certain choices.

Bénabou & Tirole develop a **third-generation theory of moral behaviour** based on **identity management**. People care about "who they are," infer their values from their past choices, and treat *beliefs about themselves* as assets that can be invested in or threatened.

## Methods

Theoretical paper. Develops a formal cognitive model of identity:

- **Self-signaling**: Because people have better access to the *record* of their conduct than to the *underlying motivations*, they judge themselves by what they do.
- **Self-reputation**: identity-enhancing behaviors are more likely when objective info about deep preferences is scarce.
- **Non-monotonic responses**: identity investments are hill-shaped in prior confidence — weakly held identities yield to conformity, strongly held ones produce counter-reactions.
- **Taboo trade-offs**: agents refuse to engage even in mere contemplation of decisions that would threaten precious self-views.
- **Social norms**: depending on perceived correlations of values, the same agents can act prosocially (shun free riders) or selfishly (shun moral exemplars).

The model unifies and extends prior work on cognitive dissonance, self-perception (Festinger, Bem), self-signaling (Bodner & Prelec; Bénabou & Tirole 2004, 2006), and self-handicapping.

## Key results (theoretical)

1. **Identity acts as an asset** that responds non-monotonically to acts and threats.
2. **Asymmetric responses to good vs bad acts**: identity investments protect a *positive* self-concept; bad acts threaten this asset and may produce avoidance behaviour ("moral wiggle room").
3. **Information avoidance is rational** under this framework — people prefer not to know things that would threaten identity.
4. **Social norms emerge** as identity-management strategies at the group level; mavericks (whether deviant or excellent) get shunned for the same identity-protection reason.
5. **History dependence** — behaviour is path-dependent; once a person has committed to an identity, future choices align to protect it.

## Main takeaways

1. **People are not just outcome-maximisers; they manage identity assets.** Behavior is governed by anticipated effects on self-view.
2. **Moral wiggle room makes sense** under identity management — a thin veil of plausible deniability lets the agent maintain a positive self-view while behaving selfishly.
3. **Asymmetric salience of credit and blame**: identity is *more* threatened by bad acts than enhanced by good ones (consistent with Steffel et al. 2016).
4. **Theoretical foundation for "process ownership"**: caring about being the locus of moral judgment, not just the outcome, follows naturally from identity management.
5. The paper is the standard economic-theory reference for identity-based explanations of moral behaviour.

## Relation to "Algorithms and Responsibility" (this manuscript)

Bénabou & Tirole is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 33: "the identity / moral self-image literature in economics, anchored by Bénabou (2011), models people as caring about 'who they are' and inferring their own values from past choices. Identity functions as an asset that responds non-monotonically to acts and threats, producing asymmetric reactions to good versus bad outcomes that map naturally onto the credit-blame asymmetry documented by Steffel et al. (2016). The intersection of these two literatures with our setting is largely unexplored: no formal model directly links the identity framework to algorithm-mediated decisions."

**Why this paper matters for the manuscript:**

**(1) The theoretical foundation for M3.** The manuscript's preferred mechanism (M3 — process ownership / identity / accountability salience) is explicitly framed as drawing on Bénabou & Tirole. The identity framework predicts:
- Under low accountability salience (no punishment), the moral content of the prediction is low; identity is not threatened; delegating is fine.
- Under high accountability salience (punishment possible), the moral content is salient; identity is at stake; the principal would rather *be the agent of the moral act* than offload it, because acting morally is identity-protective.

This is the H1 reversal interpreted through the Bénabou-Tirole framework.

**(2) Non-monotonic identity response explains the H1 reversal.** Under standard responsibility-shifting models, more accountability → more delegation (avoid blame). Under Bénabou-Tirole, more accountability → more *engagement* (protect identity by being the actor). The two predictions diverge exactly at the H1 manipulation, and the manuscript's data lines up with Bénabou-Tirole.

**(3) "Asymmetric reactions to good vs bad outcomes" map to Steffel et al.** Bénabou-Tirole provides the formal mechanism for why the credit-blame asymmetry exists: identity threats from bad acts are *more salient* than identity-enhancement from good acts because the asset (positive self-view) is what's at stake. The manuscript builds on this to justify the focus on punishment over reward.

**(4) "No formal model links identity to algorithm-mediated decisions" — the manuscript fills this gap.** The Bénabou-Tirole framework has not previously been applied to algorithmic delegation specifically. The manuscript is positioned to make a theoretical contribution by being the first to do so, even if only informally.

**Where in literature.tex:**

- Paragraph 33: correctly cited as the theoretical anchor for the identity / moral self-image framework. Worth strengthening by being explicit that M3 is operationalising Bénabou-Tirole for algorithm delegation.

**Worth borrowing more from Bénabou-Tirole:**

- The "taboo trade-off" framing is rhetorically powerful. The manuscript could note: "Under Bénabou & Tirole (2011), engaging with morally consequential decisions through an algorithm risks treating them as a 'taboo trade-off' — a category of choice that subjects refuse to even contemplate via certain channels. The H1 reversal we observe is consistent with subjects refusing to route morally salient decisions through an impersonal algorithm when the moral content is made vivid by the punishment possibility."

- The "self-signaling" framing is more general than "identity" — the manuscript could use this term to clarify why the H1 reversal makes sense: in the punishment condition, delegation signals to oneself (and potentially to others) that one is the type of person who routes morally costly decisions through machines rather than engaging directly. Subjects prefer to signal otherwise.

- The "non-monotonic response to identity threats" is precisely the pattern in the H1 data: under no threat (no punishment), delegation is high; under threat (punishment), delegation drops. Subjects with weakly-held moral identity might conform; those with strongly-held moral identity counter-react. The manuscript could check for heterogeneity along this dimension — e.g., by SVO or by the Holt-Laury risk measures.

**Limitation:** Bénabou-Tirole is theoretical; the manuscript's empirical evidence is suggestive of identity-based explanations but doesn't directly test the identity model's mechanisms (e.g., self-inference from past actions, taboo formation, social norm emergence). The manuscript should be careful not to overclaim — M3 is a *candidate* explanation grounded in Bénabou-Tirole, not a directly-tested one.
