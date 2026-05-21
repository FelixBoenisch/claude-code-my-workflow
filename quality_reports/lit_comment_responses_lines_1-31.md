# Responses to inline comments in literature.tex (lines 1–31)

Generated 2026-05-18. One response per inline `[Comment: …]` marker, plus the orphaned quoted-string strings in ¶22 and ¶24. Each entry: (i) what the comment is asking, (ii) my response, (iii) a concrete text suggestion you can copy if appropriate.

A typo to flag separately, not from a comment: **line 1** reads `\label{literaturCe}` — should be `\label{literature}`. Internal `\ref` calls will break otherwise.

---

## ¶7 — Comment 1: "What is moral responsibility? Is it about feeling responsible or being made responsible? Should we explicitly mention both here?"

**Response.** Yes, this distinction is load-bearing later in the paper (it's exactly the distinction we discussed in connection with Steffel's two mediators, and the one that lets you separate the H1 reversal from the Hueholt & Szech result). The current term "moral responsibility" elides two distinct things — self-felt responsibility and externally-attributed blame — that the rest of subsection 1 treats separately (Hamman's qualitative responsibility ratings vs B&F's punishment-shifting). Worth making it explicit on first use.

**Suggested replacement for the relevant clause in ¶7:**
> "…because doing so shifts the responsibility for the resulting outcome away from the principal --- both in the principal's own eyes (her felt responsibility for the outcome) and in the eyes of others (the blame that third parties attribute to her). These two dimensions tend to co-move in the canonical settings we discuss next, but we will see below that they can decouple."

The closing clause ("can decouple") foreshadows your H1 reversal narrative without committing to it yet.

---

## ¶11 — Comment 2: "Please give a table overview of whether punishment was costly in Bartling and Fischbacher, Hamman et al., and Coffman."

**Response.** Table below. Important up-front note: **Hamman et al. 2010 does not have third-party punishment as a design feature at all.** Hamman measures generosity under delegation vs direct choice plus qualitative responsibility ratings; there is no recipient-side costly punishment phase. So the "costly punishment" dimension separates {B&F, Coffman, Oexl} from {Hamman}, not B&F from Hamman.

| Paper | Punishment phase? | Costly to punisher? | Intermediary punishable? | Intermediary's discretion | Random-device variant? |
|---|---|---|---|---|---|
| Bartling & Fischbacher (2012) | Yes | Yes (1 cost / 3 reduction) | Yes | Full (fair vs unfair) | Yes — die roll |
| Hamman et al. (2010) | No (qualitative ratings instead) | n/a | n/a | Full | No |
| Coffman (2011) | Yes | Yes | No (passive intermediary in headline treatment) | None (passive) | Yes — random outcome |
| Oexl & Grossman (2013) | Yes | Yes | Yes | Varied: full, restricted, or none ("powerless") | Yes — random draw |

The table makes clear that Oexl's contribution is *not* "punishment is costly + aligned incentives + punishable intermediary" — those features are shared with B&F. Oexl's distinguishing contribution is varying the *intermediary's discretion*, including a "powerless" treatment where the intermediary cannot affect the outcome at all. This is the actual contrast that addresses Comments 3, 4, 5.

I would not put this table in the manuscript itself (the comparison is too granular for a top-econ lit review), but you might keep it in an appendix or just use it to inform the prose rewrite below.

---

## ¶11 — Comments 3, 4, 5: "I thought [aligned incentives / punishable intermediary] was also the case in the other experiments." + "Were these three dimensions only mentioned to distinguish from Coffman, or also from B&F and Hamman?"

**Response.** Comments 3 and 4 are correct: B&F also has aligned incentives and a punishable intermediary. The current ¶11 wording misframes Oexl's contribution by listing features that aren't actually distinguishing. The real contribution is Oexl's variation of *intermediary discretion*, including the powerless-intermediary treatment.

**Suggested rewrite of the second half of ¶11** (replacing the current "...in a setting where punishment is costly, the intermediary's incentives are aligned with the dictator's, and the intermediary can also be punished" through the "Together, the two studies suggest..." sentence):

> "\citet{oexl_shifting_2013} extend the design by systematically varying the *intermediary's discretion* --- from full choice to fully constrained --- and find that punishment shifting persists even when the intermediary has no genuine choice at all (the ``powerless intermediary'' treatment). Their result is striking because it rules out the natural interpretation that the principal escapes blame because some of it has migrated to a responsible deciding intermediary: in Oexl's powerless treatment, the intermediary cannot meaningfully be held responsible for the outcome, yet the principal still escapes punishment. Taken together with Coffman's passive-intermediary result, the two studies suggest that the lack of direct interaction between dictator and recipient is a key channel through which delegation reduces punishment, independent of any actual transfer of blame to the intermediary."

This (i) names Oexl's actual contribution precisely (varying discretion), (ii) explains *why* the powerless result matters (rules out an alternative interpretation), and (iii) preserves your existing "lack of direct interaction" conclusion.

---

## ¶22 + ¶24 — Comment 6: "Suggest an introductory sentence/paragraph based on these two quotes, that links well with what comes next."

**Response.** The two quoted strings are competing draft openers. The ¶22 string is duplicative of the transition already ending ¶19, so it can be deleted. The ¶24 string is a positioning sentence for the subsection; it can be expanded into a short opening paragraph that signals (a) what this subsection covers, and (b) the moral-domain subset that ¶28 will focus on.

**Suggested opening paragraph for subsection 2** (replacing both quoted strings):

> "Because our intermediary is an algorithm rather than another human, our work also connects to the rapidly growing literature on algorithmic decision use. This literature primarily asks when and why people are willing to rely on algorithms, largely abstracting from the responsibility-shifting motive that drove the discussion above. We summarise the main findings, with particular attention to the smaller subset of studies in which the decision being delegated has consequences for someone other than the decision-maker --- the configuration closest to our setting."

Drops both quoted lines, gives the reader a roadmap, and foreshadows the structure of the subsection.

---

## ¶26 — Comment 7: "I would put the Logg reference after the general Dietvorst reference on algorithm aversion."

**Response.** Agreed. Currently Logg sits mid-paragraph as a counter to a long list of aversion moderators, which makes the contrast feel buried. Moving Logg adjacent to Dietvorst sets up the heterogeneity framing earlier and lets the moderator list flow without interruption.

**Suggested reordering for the opening of ¶26** (replacing the first two sentences of the current ¶26):

> "The literature on people's willingness to use algorithmic decision aids has grown rapidly since \citet{dietvorst_algorithm_2015}, who introduced the term \textit{algorithm aversion} for the finding that people prefer their own (or other humans') judgement over algorithmic predictions, even after observing that algorithms outperform human decision-makers. The phenomenon is far from universal, however: \citet{logg_algorithm_2019} documents conditions under which subjects show \textit{appreciation} of algorithmic advice over human advice, and the picture that has since emerged is one of substantial heterogeneity across tasks, contexts, and elicitation methods. \citet{burton_systematic_2020}, \citet{mahmud_what_2022}, \citet{chugunova_we_2022}, and the recent meta-analysis of \citet{qin_ai_2025} provide systematic reviews and document a large array of moderators determining when and why algorithms are used in decision-making. For example..."

Then the existing moderator list (Berger / Litterscheidt / Sharan / Stein / Dietvorst 2020 / Dietvorst 2018 / Castelo / Bogert) follows unchanged.

---

## ¶26 — Comment 8: "the literature reviews and references in general are old-ish...ideally we can include more recent references."

**Response.** Two concrete additions emerged from the recent lit search:

1. **Qin et al. (2025), *Psychological Bulletin*** — quantitative meta-analysis of 442 effect sizes from 163 studies (N=82,078). Most up-to-date numeric anchor for the aversion-vs-appreciation literature. Adds the "capability × personalization" framework. Already woven into the rewrite above as `\citet{qin_ai_2025}`.

2. **Bonnefon, Rahwan & Shariff (2024), *Annual Review of Psychology*** — narrative review of the moral psychology of AI, explicitly organised around moral agents / moral patients / **moral proxies (delegates)**. The moral-proxy framing is directly relevant to your manuscript. Best added in ¶28 as the lead citation for the moral-domain subset (see Comment 9 below).

Bib entries to add (if not yet present):

```bibtex
@article{qin_ai_2025,
    title = {{AI} aversion or appreciation? A capability-personalization framework and a meta-analytic review},
    author = {Qin, X. and Zhou, M. and Chen, S. and Wu, J. and Zhou, Z. and Dong, Y. and Cao, J. and Lu, J. G.},
    journal = {Psychological Bulletin},
    volume = {151},
    number = {5},
    pages = {580--599},
    year = {2025},
    doi = {10.1037/bul0000477}
}

@article{bonnefon_moral_2024,
    title = {The Moral Psychology of Artificial Intelligence},
    author = {Bonnefon, Jean-Fran\c{c}ois and Rahwan, Iyad and Shariff, Azim},
    journal = {Annual Review of Psychology},
    volume = {75},
    pages = {653--675},
    year = {2024},
    doi = {10.1146/annurev-psych-030123-113559}
}
```

Three optional further additions, if you want to refresh the moderator list with 2024–2026 work:

- `bockstedt_humans_2025` (already cited)
- `ivanova_stenzel_measuring_2024` (already cited)
- `dargnies_aversion_2026` (already in your bib; consider adding to the moderator list for the algorithmic-HR aversion finding)

---

## ¶28 — Comment 9: "We mention these three references and then only cover in more detail the Gogoll reference. What could we say about the other two?"

**Response.** Right — Bigman and Jauernig are co-cited at the anchor but never discussed. Both can earn a sentence each. Bigman is the canonical "people are averse to machines making moral decisions" demonstration across multiple domains; Jauernig is the closer-in study identifying *moral discretion* as what people want to preserve.

**Suggested additions in ¶28**, immediately after the moral-domain anchor sentence:

> "\citet{bigman_people_2018} document a robust pattern of aversion to machines making moral decisions across multiple domains (driving, legal, medical, military): people prefer humans to algorithms for moral judgments even when the algorithm performs as well or better. \citet{jauernig_people_2022} show that this preference reflects a desire for *moral discretion* --- people prefer human decision-makers specifically because humans can exercise contextual judgment rather than apply rigid rules."

Note: Bigman is also currently cited in subsection 3 ¶34 for the "algorithmic outrage asymmetry" finding. This is fine — Bigman 2018 documents both phenomena (moral-domain aversion ex ante; reduced outrage ex post). You're using the paper for two distinct claims in two distinct subsections, which is legitimate.

---

## ¶28 — Comment 10: "How [Gogoll] is discussed does not mean that it was about a decision for someone else."

**Response.** Correct. Gogoll & Uhl's setting has the algorithm's output determine *both* the subject's *and* a partner's payoff — joint impact, not "for someone else." Currently the paragraph frames the subset as "decisions made on behalf of someone else", which fits Steffel-style other-only configurations but not Gogoll's joint-impact setting. Two options to fix:

**Option A — broaden the framing of the subset.** Change "for someone other than the decision-maker" to "with consequences for third parties" or "with third-party stakes." This accommodates Gogoll (joint impact), Goldbach (joint impact), and your own setting (purely other-affecting) under one heading.

> "Within this body of work, a smaller subset focuses on settings in which the decision being delegated *has consequences for third parties*, sometimes called the \textit{moral domain}…"

**Option B — keep the "for someone else" framing and adjust the Gogoll sentence.** Less clean.

Option A is cleaner. I'd recommend it.

For the Gogoll sentence itself, also clarify the joint-impact structure:

> "\citet{gogoll_rage_2018} find that subjects preferred to delegate a calculation task to another participant rather than to an algorithm even when the task was a straightforward arithmetic exercise where algorithmic advantage should have been salient; the algorithm's output determined both the subject's *and* a partner's payoff, so the moral content arose through joint impact rather than through deciding purely on someone else's behalf. Inference about pure preferences is further complicated, however, by the fact that subjects had observed the algorithm fail in $80\%$ of cases."

---

## ¶28 — Comment 11: "Check again whether [the consensus statement] holds after updating the list of papers we refer to."

**Response.** The current consensus statement is *"aversion to algorithms is amplified when third-party welfare is at stake"*. After incorporating the recent 2024–2026 work, this consensus is no longer cleanly true. **Hueholt & Szech (2026, EER)** and **Tontrup & Sprigman (2025)** both find that subjects facing a real-stakes moral decision *prefer* to delegate to AI rather than to another human — the opposite direction. The literature is now genuinely split.

**Suggested replacement for the consensus sentence:**

> "Earlier work in this subset converged on the conclusion that aversion to algorithms is amplified when third-party welfare is at stake. More recent work, however, has documented the opposite pattern in some settings: \citet{hueholt_trusting_2026} and \citet{tontrup_strategic_2025} both find that subjects facing real-stakes moral decisions prefer to delegate to AI rather than to another human, consistent with the responsibility-shifting motive dominating aversion in some moral contexts. The empirical picture is therefore unsettled, and our manuscript contributes a sharper test by manipulating the salience of third-party punishment directly."

This (i) acknowledges the older consensus, (ii) flags the new counter-evidence, (iii) motivates your manuscript's contribution as resolving the tension. Useful narrative move.

---

## ¶28 — Comment 12: "Do the first two mechanisms not hold when deciding to employ an algorithm for oneself? This paragraph is specific to making decisions for others."

**Response.** Correct. Lack of trust and loss of perceived control are general drivers of algorithm aversion — they apply to any algorithm-use decision, self-affecting or third-party-affecting. The only mechanism *specific* to the moral-domain subset is "anticipated reputational or moral costs", which by construction requires third-party stakes.

**Suggested rewrite of the mechanism sentences:**

> "The mechanism behind this amplified moral-domain aversion remains unsettled. Two of the most commonly proposed drivers --- \textit{lack of trust in the algorithm} and \textit{loss of perceived control} --- are general explanations for algorithm aversion that apply equally to self-affecting decisions; they do not by themselves explain why aversion is amplified specifically when third parties are affected. The driver that is distinctively moral-domain is \textit{anticipated reputational or moral cost} --- the principal's expectation that she will be judged for using an algorithm in a setting with moral stakes. Existing designs typically cannot separate this third channel from the first two."

This sharpens the manuscript's contribution: by manipulating the *external punishment* margin directly (your H1), you're isolating the moral-domain-specific channel that the prior literature cannot.

---

## Line 30 — Comment 13: "Are there any other papers that fit into this literature strand and particularly choosing to delegate to algorithms for others? Delegation to algorithms, but not yet about responsibility?"

**Response.** Yes, several. Most are already in your bib but not currently cited in ¶26 or ¶28. Candidates:

- **Freisinger & Schneider (2024)** — cited by Hueholt & Szech as documenting role-dependent preferences in a layoff-decision delegation context: individuals deciding on their own behalf prefer delegating to AI, while affected individuals favour human decision-makers. Directly relevant. *Verify the citation exists and add to bib.*
- **Ivanova-Stenzel & Tolksdorf (2025)** [`ivanova_stenzel_delegating_2025`] — already in bib. Autonomy-preference vs decision-cost trade-offs in AI delegation. Could be cited in ¶26 or as a transition to ¶28.
- **Dargnies, Hakimov & Kübler (2026)** [`dargnies_aversion_2026`] — already in bib. Aversion to algorithmic delegation in hiring decisions (third-party stakes; HR context).
- **Newman, Fast & Harmon (2020)** [`newman_eliminating_2020`] — algorithmic HR decisions perceived as less fair; already cited in your earlier draft of ¶28 (which has been removed in the current version — worth restoring).
- **Kobis et al. (2025)** [`kobis_delegation_2025`] — currently cited in subsection 3. Could also be cited in ¶28 as evidence that delegation to AI is empirically observable in morally consequential settings.

**Suggested addition near the end of ¶28** (after the mechanisms sentence):

> "Other recent contributions document related patterns: \citet{ivanova_stenzel_delegating_2025} highlight the trade-off between decision-autonomy preferences and the cost-reduction benefits of delegation; \citet{dargnies_aversion_2026} document aversion to algorithmic hiring decisions; and \citet{newman_eliminating_2020} attribute moral-domain aversion in HR to \textit{algorithmic reductionism} --- the perception that algorithms decontextualise the qualitative features of performance."

This addresses Comment 13, restores Newman (which was useful and currently missing), and pulls Ivanova-Stenzel and Dargnies into the right subsection.

---

## Cross-cutting observations

1. **The "responsibility vs accountability" distinction (Comment 1) is load-bearing across the subsection.** Making it explicit in ¶7 sets up cleaner framings later, including for the H1 reversal discussion in §3 of subsection 3.

2. **Comment 11's "consensus is no longer clean" point is important.** It directly motivates your manuscript: you're not just adding another data point to a settled literature, you're contributing to an active disagreement. Worth playing up in the abstract/intro too.

3. **Comments 3–5 on Oexl reveal a small but real misstatement of the canonical literature.** Fix this early — referees who know the B&F/Coffman/Oexl chain will spot the misframing immediately.

4. **The Logg-reordering in Comment 7 is a small structural improvement.** Independent of content, it makes the paragraph read more decisively (heterogeneity framing up front, moderators in a clean list).

5. **The Bonnefon and Qin additions (Comment 8) buy you two things at once:** freshens the literature reviews and lets you ground the moral-proxy framing in a *Nature*-adjacent venue.
