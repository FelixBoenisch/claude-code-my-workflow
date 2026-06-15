---
title: Critical review of literature.tex — content, accuracy, structure, flow
date: 2026-06-12
scope: manuscript/literature.tex (current version, 61 lines); cross-checked against introduction.tex, design.tex, results.tex, conclusion.tex, ProjectAlgorithm.bib, the local paper library (master_supporting_docs/supporting_papers/), and targeted web searches
status: PROPOSALS ONLY — no manuscript file has been edited
constraints honoured: standalone section at current scale · full reference sweep · NEUTRAL SETUP (no pre-positioning of H1-reversal-interpretive literature) · every inline [Comment:] adjudicated
---

# Review of `literature.tex`

**How to read this file.** Part 1 is the priority list. Part 2 goes through the section paragraph by paragraph; this is where all paste-ready LaTeX lives, in document order, so you can apply it top-to-bottom. Part 3 maps each of your inline `[Comment:]` blocks to its resolution. Part 4 lists cross-section consistency problems (changes in *other* files, not literature.tex). Part 5 is small mechanics. Part 6 is the BibTeX block for `ProjectAlgorithm.bib`. Part 7 documents what was verified against what, so you can audit any claim I make below.

Line numbers refer to the current `literature.tex`. Snippets use only existing bib keys plus the new keys defined in Part 6.

---

# Part 1 — Executive summary (what matters most)

| # | Priority | Issue | Where | Fix |
|---|---|---|---|---|
| 1 | **P0 — factual** | Köbis et al. (2025) is misdescribed: the paper explicitly reports **no evidence** that people request more cheating from machines than from humans ("there was no evidence that people requested more cheating from machines…", their study 3). Their findings are (i) vague delegation *interfaces* increase dishonest requests and (ii) machine agents *comply* far more than human agents. | line 48 | §2.10, snippet S-10 |
| 2 | **P0 — factual** | "Algorithmic outrage asymmetry" is misattributed to `bigman_people_2018`. That paper documents *ex-ante* aversion to machine moral decision-makers (and the aversion persists for *positive* outcomes). The outrage-asymmetry result is Bigman, Wilson, Arnestad, Waytz & Gray (2023, *JEP: General*) — which also happens to be the post-2020 workplace/hiring reference you asked for. | line 42 | §2.8, snippet S-8 |
| 3 | **P0 — citation integrity** | `stein_dont_2020` is flagged `[NOT FOUND]` in ProjectAlgorithm.bib ("may be partially fabricated by an earlier session"). It is still cited at line 28 for the complexity-aversion claim. Drop the clause or replace with a verified reference before anything is circulated. | line 28 | §2.6, snippet S-6 |
| 4 | **P1 — content gap (the big one)** | Bartling & Fischbacher's **punishment-on/off delegation comparison is missing**: delegation rises from **17% (D&noP) to 56% (D&P)**, "more than three times higher" (Fisher p < 0.01) — their words: "avoiding punishment is an important motive for the decision whether or not to delegate." This is the single most relevant prior result for H1 and the human-delegation benchmark for your whole design, and the section never states it. It also forces a re-scoping of the paper's novelty claim (see #5). | line 11 | §2.3, snippet S-3 |
| 5 | **P1 — novelty claim** | Because BF2012 *did* run the punishment-on/off test for human delegation, the claim (intro ¶9, design.tex ¶72 context, lit ¶52/54) that such a test "is not feasible in designs where punishment is always possible" is true of the *algorithmic* literature only. Scope the claim: *first to vary the punishment possibility for delegation to an algorithm* (and in a setting with inherent uncertainty + individual-level calibration). | lines 52–54 + intro | §2.12–2.13, snippets S-12/S-13; Part 4 |
| 6 | **P1 — factual nuance** | Chevrier & Teixeira: delegation rates do **not** rise under AI in their data (17/17/23%, n.s.); the wiggle room is exploited by *programmers* (60% inegalitarian choices), and recipients punish less *often* but more *severely*. So the ¶48 wrap-up "the direction of the effect on delegation is uniformly positive" is wrong for at least one of the four papers. | line 48 | §2.10, snippet S-10 |
| 7 | **P1 — content gap** | Strand 2 reviews advice-weighting but not **ceding decision control** — the margin your Player A actually faces. The bib already holds the needed entries unused: `ivanova_stenzel_measuring_2024`, `ivanova_stenzel_delegating_2025`, `dargnies_aversion_2026`, `kormylo_till_2025`; add Candrian & Scherer 2022, Germann & Merkle 2023, Holzmeister et al. 2023 (BibTeX in Part 6). Strand 2 also has **no closing bridge** stating what your design adds to it. | lines 27–35 | §2.6, snippets S-6/S-6b/S-6c |
| 8 | **P1 — content gap** | Gogoll & Uhl's **observer-side result** is missing: their observers reward machine-delegators significantly less than human-delegators *in both outcome states* (success: 17.77 vs 12.52 ECU; failure: 4.42 vs 0.49). This is the cleanest incentivised antecedent for your punishment stage and currently invisible (G&U appears only as a one-clause aversion cite). | lines 38, 44 | §2.7/§2.9, snippets S-7/S-9 |
| 9 | **P2 — accuracy** | Smaller misdescriptions: Kirchkamp & Strobel selfishness direction (increase is relative to *deciding alone*, similar for human and computer partners); Maasland & Weißmüller (they *do* find a conditional tendency to delegate dismissals; aversion dominates overall); Oexl/BF random-device phrasing ("shifts punishment **to the device**" — nothing is shifted to it; the principal's punishment simply falls); Feier role structure ("third parties" punish — in fact the *affected participants* evaluate, in a dual role, on a reward–punishment scale). | lines 11, 44, 50 | §2.3/§2.9/§2.11 |
| 10 | **P2 — flow** | Strand 3 lacks a red line (your own diagnosis). Proposed arc: moral-domain aversion (entry) → do observers actually judge algorithm-mediated decisions differently? (vignettes, post-2020 domains) → incentivised evidence (G&U observers, Kirchkamp, Maasland) → recent "moral cover" strand → Feier → extensions. Snippets implement this without moving subsection boundaries. | lines 37–54 | §2.7–§2.13 |

Also notable: the bare `[Comment: …]` blocks (lines 19–21, 32–35, 46, 56–58, plus inline ones) are **plain text and compile into the PDF** — unlike design.tex, which uses `\todo[inline]`. See Part 5.

---

# Part 2 — Paragraph-by-paragraph review with snippets

## 2.1 Section opening (lines 3–5, currently commented out)

**Your comment:** "Is this first paragraph really necessary? Is it perhaps better placed in a conclusionary paragraph … perhaps introducing the summary of the contribution … (e.g. in the intro)?"

**Recommendation: drop the three-strand enumeration here; it already lives in the intro.** Introduction ¶15 *is* the "contributes to three strands" paragraph, so reinstating the enumeration here would duplicate it almost verbatim. Independent evidence that the enumeration is not the norm: the audit of your own 65-paper library (`master_supporting_docs/literature_section_audit.md`) found only 13/65 papers with a separate lit section and only 3/65 opening it with a strand-enumerating bridge. The pattern in the strong econ exemplars (Freer et al. 2024; Coffman's "V. Related Literature") is a short *functional* opener instead.

The section currently starts cold with a subsection heading. A two-sentence functional opener fixes that without duplicating the intro:

```latex
Our study connects an established experimental literature on responsibility
avoidance through delegation between humans with a younger literature on
algorithm use in decision-making. We review the two in turn, and then turn to
the small set of studies --- closest to ours --- that examines responsibility
attributions when the delegate is an algorithm.
```

Then delete the commented-out lines 3–5 (at polish stage; no rush).

## 2.2 Strand 1 opening paragraph (line 9)

Three problems. (i) The strategic-motives sentence is a ~90-word run-on whose "i.e."-clause restates the responsibility-shifting definition twice. (ii) Four references exist only as plain text — "(Fershtman and Gneezy, 2001)", "(Aghion and Tirole, 1997)" — and your comment asks for Bolton & Dewatripont and the Schelling-plus-applications footnote from Bartling & Fischbacher. None of these keys existed in the bib; all are provided in Part 6. (iii) Per Bartling & Fischbacher's own framing, the commitment-device citation should be Schelling (1960), with Fershtman & Gneezy as *experimental* evidence in the footnote.

**Replacement for line 9:**

```latex
Delegation has long been studied as an efficiency-enhancing institutional
arrangement: principals delegate to agents who have better information, lower
opportunity costs, or specialised skills \citep[see][for an overview of the
principal--agent literature]{bolton_contract_2005}. Alongside these efficiency
motives, the literature has identified strategic motives for delegation:
delegation can serve as a commitment device that alters equilibrium play
\citep{schelling_strategy_1960},\footnote{Applications include output and
pricing decisions in oligopolistic markets \citep{vickers_delegation_1985},
inflation targeting \citep{rogoff_optimal_1985}, and bargaining
\citep{jones_have_1989}. \citet{huck_strategic_2004} provide experimental
evidence on strategic delegation in oligopolistic markets,
\citet{schotter_bargaining_2000} and \citet{fershtman_gneezy_2001} in
bargaining settings.} or as a means of motivating the agent's initiative
\citep{aghion_formal_1997}. This paper concerns a third, distinct motive:
principals may delegate not because the agent is more competent or cheaper,
but because delegation shifts responsibility for the resulting outcome away
from themselves --- both in their own eyes (felt responsibility) and in the
eyes of others (attributed blame). The political-science and public-choice
literatures have long recognized delegation as a blame-shifting strategy
\citep{weaver_politics_1986, fiorina_legislator_1986}. Experimental economics
has established the same motive in incentivised settings, primarily using
modified dictator games.
```

## 2.3 Canonical evidence paragraph (line 11)

**The biggest content gap in the section sits here.** Bartling & Fischbacher ran a clean 2×2: delegation possible × punishment possible. Verified directly from the published text in your library: *"In treatment D&noP, 17% of As delegated the decision right. In treatment D&P, the share of delegated decisions rises to 56%, which is significantly higher (Fisher exact test, p < 0.01). This finding demonstrates that avoiding punishment is an important motive for the decision whether or not to delegate a decision right."* This is (a) the precise human-intermediary benchmark for your H1 manipulation, (b) the strongest possible motivation for your design, and (c) the reason your novelty claim must be scoped to *algorithmic* delegation (see §2.12–2.13). The current text gestures at the motive ("the prospect of avoiding punishment constitutes a strong motive") without telling the reader that BF identified it with exactly the on/off comparison you transpose.

Smaller fixes folded in: the punishers in BF are the *affected receivers* (one randomly selected), not third parties; the Coffman sentences are accurate but their logical order is muddled ("This holds even when…" has an ambiguous antecedent); the random-device sentence says the principal "shifts some punishment **to the device**", but in both papers nothing is shifted *to* anything — the principal's punishment falls (and in Oexl's random treatment the intermediary absorbs none: $0.64 → $0.72, n.s.); and the closing synthesis ("Across the two papers…") leans on Coffman's mechanism while naming only BF and Oexl.

**Replacement for line 11 (two paragraphs):**

```latex
\citet{bartling_shifting_2012} provide the canonical experimental evidence. In
their design, a dictator may either choose between a fair and an unfair
allocation of an endowment or delegate this choice to another person whose
monetary incentives are aligned with the dictator's; a receiver, who is
adversely affected by the unfair allocation, may then assign costly punishment
to the dictator and the delegee. Two results anchor the literature. First,
responsibility is delegated along with the decision right: when the delegee
chooses the unfair allocation, punishment falls largely on the delegee, while
the dictator is almost spared. Second --- and most directly relevant for our
design --- the prospect of punishment is itself a motive for delegating.
Comparing otherwise identical treatments with and without a punishment stage,
the share of dictators who delegate more than triples, from 17\% to 56\%, when
punishment is possible.

Two follow-up studies dissect the mechanism. \citet{coffman_intermediation_2011}
shows that third-party punishment of a selfish first mover falls when an
intermediary is placed between her and the affected party, even when the
intermediary is completely passive; yet the reduction disappears in a treatment
in which the first mover still transacts directly with the affected party
despite the intermediary's presence. What protects the principal is thus the
absence of direct interaction with the affected party, rather than any
transfer of blame to a deciding intermediary. \citet{oexl_shifting_2013}
sharpen the complementary point about the intermediary. In their design,
delegation necessarily eliminates the fair option; the principal nevertheless
escapes punishment, and the intermediary --- despite being powerless to
restore fairness --- absorbs blame, but only when she actively chooses between
the two unfair allocations. When she merely triggers a random draw between
them, she absorbs none. Relatedly, both papers include treatments that replace
the deciding human with a randomization device (a die roll in
\citealp{bartling_shifting_2012}; the intermediary-triggered random draw in
\citealp{oexl_shifting_2013}). In both, the principal's punishment still falls
relative to deciding directly, but by less than under delegation to a deciding
human. Consistent with this, in \citet{bartling_shifting_2012} fewer dictators
delegate to the die than delegate to a human delegee in the corresponding
treatment (39\% vs.\ 56\%). Two components of responsibility shifting
thus emerge: the absence of direct interaction with the affected party drives
the reduction in the principal's punishment, while the act of choosing ---
rather than any contribution to outcome unfairness --- is what transfers blame
onto an intermediary.
```

*Note on numbers:* 17%/56%/39% and "more than three times higher" are quoted from the published ReStud text (`_extracted_text/bartling_shifting_2012.txt`, results section); Oexl's $0.64→$0.72 (n.s.) from the paper summary. The snippet only hard-codes the three delegation shares; spot-check them against the PDF pages when pasting.

## 2.4 Hamman paragraph (line 13)

Two small things: "settings with third-party punishment" mislabels the canonical set (BF/Oexl punishers are affected recipients; only Coffman's is a genuine third party), and there is a double space after "punishment." The content itself is accurate.

**Replacement for line 13:**

```latex
The motive does not depend on the presence of a punishment stage.
\citet{hamman_self-interest_2010} show that principals' transfers to
recipients fall sharply when allocation decisions are made by hired agents, in
a setting with no punishment opportunity at all --- indicating that
responsibility shifting can operate through felt responsibility or moral
wiggle room rather than through the avoidance of sanctions. Self-reported
responsibility and recipient-side blame attributions are consistent with this
reading: dictators feel less responsible when they delegate, and recipients
place less blame on principals than on the agents who chose on their behalf.
```

## 2.5 Domains paragraph (line 17) + Argenton (line 15) + Steffel (line 23)

This paragraph is structurally fine (one domain per sentence) but three of the five sentences undersell the very findings that serve your design, and your comments ask for additions. Recommendations:

- **Fershtman & Gneezy** — add the mechanism (responders won't reject because that would also punish the delegate; rejections fell from 13% to 5% despite worse offers). "Extract larger surpluses" alone reads like a bargaining-power story.
- **Erat** — add the harm gradient (delegation of the lie rises with the harm it inflicts: 25% → 34%), which is what makes it a responsibility-shifting result.
- **Hill** — add the load-bearing nuance: the blame discount survives *full information* about who did what. This pre-empts the "it's just an information story" objection and the delegate-is-powerless clause you already have echoes Oexl nicely.
- **Deception cluster (your comment):** include Gawn & Innes 2019 (delegation reduces lying aversion) and Gawn & Innes 2021 (the "Machiavelli" pattern: retain generous decisions, delegate selfish ones — directly relevant to a paper about *who keeps the decision*), with Kandul & Kirchkamp 2018 as a see-also. **Garofalo & Rott 2018** I would include *only* with its actual (boundary) finding: delegating merely the *communication* of an unfair decision does not shift blame and even backfires — a useful contrast that clarifies what must be transferred (the decision right) for shifting to work. **Charness/Maximiano** (workplace): optional one-liner, fits the "domains" logic.
- **Argenton (line 15):** **reinstate.** One sentence buys the credit-side mirror, it is strand-1 canon (not H1-interpretive, so no tension with your neutral-setup choice), and EER 2023 is exactly the recency the section needs.
- **Steffel (line 23): keep it out**, as you suspected. Its load-bearing content for this paper (blame-avoidance > credit-seeking) is interpretive ammunition for the results section, where results.tex already cites it twice. Under your neutral-setup decision it should not be planted here. (If you ever want the design-motivation half only — people delegate choices made *on behalf of others* more readily — a single clause could be added, but I'd leave it.)
- **Barber & Odean (your comment, line 20):** **do not add.** B&O (2001 QJE) is about gender, overconfidence, and trading frequency; it contains no delegation-to-advisor result. The claim in the quoted sentence cannot be supported by that citation.

**Replacement for lines 15–23 (core version; the two clearly marked sentences are the optional add-ons):**

```latex
Beyond the canonical dictator-game setting, the responsibility-shifting motive
--- and the strategic use of delegation it gives rise to --- has been
documented across a range of domains. In incentivised ultimatum bargaining,
proposers who use a delegate secure larger surpluses: responders are less
willing to reject a tough offer when doing so would also punish the
intermediary, so offers that would be rejected coming from the proposer
herself are accepted from her agent \citep{fershtman_gneezy_2001}. In
sequential voting, non-pivotal voters are punished less than pivotal ones for
the same group outcome, and a substantial share of voters strategically vote
against their preferred allocation to avoid being pivotal
\citep{bartling_fischbacher_schudy_2015}. For acts of deception, principals
pay agents to lie on their behalf, and do so more often the more the lie harms
its victim \citep{erat_avoiding_2013}; delegation itself reduces lying
aversion \citep{gawn_lying_2019}, and decision rights are retained for
generous decisions but delegated for selfish ones \citep{gawn_machiavelli_2021}
(on delegated lies, see also \citealp{kandul_do_2018}).
% OPTIONAL (workplace domain):
In gift-exchange labor settings, workers punish a low wage with low effort
when the employer chooses it intentionally, but far less when the wage is
delegated to an agent or a random device
\citep{charness_attribution_2004,maximiano_gift_2013}.
% (end optional)
In policy-making, observers rate delegating legislatures as less blameworthy
than legislatures who decide directly --- even when the delegate is powerless
to change the outcome, and even when observers are fully informed about each
actor's contribution, so the discount is not an artefact of incomplete
information \citep{hill_does_2015}. \citet{freer_friedman_weidenholzer_2024}
isolate the motive in financial decision-making, finding that a substantial
fraction of investors delegate even purely luck-based lottery choices, where
alternative motives --- decision costs, performance-chasing, or risk tolerance
--- cannot rationalize the choice. The mirror image holds on the credit side:
principals who take a fair decision themselves receive more credit than
principals who delegate it, so responsibility attribution cuts both ways
\citep{argenton_potters_yang_2023}.
% OPTIONAL (boundary result):
The motive has limits, however: delegating merely the \textit{communication}
of an unfair decision, rather than the decision right itself, does not shift
blame --- if anything, it invites more punishment for both parties
\citep{garofalo_shifting_2018}.
% (end optional)
```

## 2.6 Strand-1 bridge (line 25)

Good paragraph; keep its job. Three upgrades: (i) terminology — your Player B is the *affected recipient who punishes*, so "the outcome falls entirely on a third party" should become "on a passive recipient" (you reserve "third party" for unaffected observers elsewhere, and Feier's structure differs on exactly this point); (ii) the bridge can now lean on the sharpened canon: blame transfers only to a delegate who *decides*, and devices absorb punishment only partially — which positions the algorithm as the open case between deciding human and die; (iii) add the punishment-motive clause so the bridge mirrors the BF result you now report.

**Replacement for line 25:**

```latex
In sum, in settings with self-interested choice, delegation to another human
reduces both the principal's punishment and her felt responsibility, and the
prospect of punishment is itself a quantitatively important motive for
delegating. The canonical results also mark the boundaries of the effect:
blame transfers onto an intermediary only if the intermediary genuinely
decides, and a randomization device shields the principal only partially. An
algorithmic delegate is neither a deciding human nor a mere randomization
device, and where it falls between the two is not obvious ex ante. Our setting
further departs from the canonical design along three dimensions: the
intermediary is algorithmic rather than human, the outcome falls entirely on a
passive recipient rather than partly on the principal herself, and the
underlying decision involves genuine predictive uncertainty rather than a
known fair--unfair choice. Whether the responsibility-shifting motive retains
its force under these conditions is the question we take up.
```

## 2.7 Strand 2: "Delegation to algorithms" (lines 27–35)

Four issues.

1. **"beginning with \citet{dietvorst_algorithm_2015}"** is historically wrong — the clinical-vs-statistical-prediction literature goes back to Meehl (1954) and Dawes (1979), as Burton et al.'s review (which you cite) dates the field from 1950. One footnote fixes it and signals to referees that you know the lineage.
2. **The moderator mega-sentence** (8 `\citep`s in one sentence) should be split and grouped: algorithm-side, task-side, control-side. While splitting: **drop `stein_dont_2020`** (flagged `[NOT FOUND]`/possibly fabricated in the bib — do not cite it anywhere), and **move `bogert_humans_2021` out of the "subjective tasks" clause** — its actual finding is that reliance on algorithms *increases* with task difficulty, which currently sits under the wrong sign.
3. **Recency** (your comment): `qin_ai_2025` is already in; the natural further adds are `kormylo_till_2025` (betrayal aversion is asymmetric between human and algorithmic advisers — MS 2025) and `dargnies_aversion_2026` (hiring algorithms; what transparency does and does not buy — MS 2026, the "Dargnies/Hakimov/Kübler" you asked about; note the spelling is **Dargnies**).
4. **The missing sub-strand: ceding decision control.** Your design is full delegation, not advice-taking. The bib already holds both Ivanova-Stenzel & Tolksdorf papers unused; add Candrian & Scherer 2022, Germann & Merkle 2023, Holzmeister et al. 2023 (Part 6). This paragraph also absorbs the AI-vs-human delegation contrast from your line-21 comment — via Candrian (prefers-AI, especially under losses) and Ivanova-Stenzel & Tolksdorf 2025 (prefer AI to human, but under-delegate to both: a *decision-autonomy* preference). I'd skip Leyer & Schneider 2019 (conference proceedings; Candrian covers the point in a better venue).

**S-6 — Replacement for line 28:**

```latex
A large and rapidly growing empirical literature studies when and why people
are willing to use algorithmic decision aids. Its modern experimental phase
begins with \citet{dietvorst_algorithm_2015}, who introduce the term
\textit{algorithm aversion} for the finding that people prefer their own (or
other humans') judgement over algorithmic predictions, even after observing
that the algorithm outperforms the human.\footnote{The underlying comparison
is much older: a long literature following \citet{meehl_clinical_1954} and
\citet{dawes_robust_1979} documents that simple statistical rules outperform
clinical judgement --- and that decision-makers resist them nonetheless.} In
contrast, \citet{logg_algorithm_2019} document conditions under which subjects
weight algorithmic advice \textit{more} heavily than human advice; the picture
that emerges is one of substantial heterogeneity in algorithm preferences
across tasks, contexts, and elicitation methods. \citet{burton_systematic_2020},
\citet{mahmud_what_2022}, \citet{chugunova_we_2022}, and the meta-analysis of
\citet{qin_ai_2025} review this literature and document a large array of
moderators. On the algorithm side, aversion is stronger when the algorithm
cannot be observed to learn from its mistakes \citep{berger_watch_2021} and
when its reasoning is opaque \citep{litterscheidt_financial_2020,
sharan_dont_2020}; trust also responds asymmetrically to violations ---
a small breach depresses willingness to follow a human expert's advice but
leaves reliance on algorithmic advice unaffected \citep{kormylo_till_2025}.
On the task side, aversion rises with the degree of irreducible uncertainty
\citep{dietvorst_people_2020}, with the perceived subjectivity of the task
\citep{castelo_task-dependent_2019}, and with loss framing of the decision
\citep{bockstedt_humans_2025}, while reliance on algorithmic advice increases
with task difficulty \citep{bogert_humans_2021}. On the control side, people
use imperfect algorithms far more readily when they retain even a minimal
ability to modify the output \citep{dietvorst_overcoming_2018}, and aversion
to algorithmic evaluation in hiring depends on what exactly is disclosed about
the algorithm \citep{dargnies_aversion_2026}.
```

**S-6b — New paragraph after S-6 (ceding control; uses your line-30 and line-21 material):**

```latex
Closest to our setting is the smaller subset of this literature in which
subjects do not merely weight algorithmic advice but cede the decision itself.
\citet{ivanova_stenzel_measuring_2024} develop a menu-based design to measure
the willingness to cede control to an algorithm and document substantial
heterogeneity in it; comparing delegation to an algorithm and to another human
within subject, they further find that people under-delegate to both even when
delegation is payoff-superior --- though less so to the algorithm ---
consistent with a general preference for decision autonomy rather than
algorithm-specific distrust \citep{ivanova_stenzel_delegating_2025}.
\citet{candrian_rise_2022} likewise find that subjects cede decisions
\textit{more} willingly to an autonomous AI than to a human agent, especially
for decisions framed as losses, and similar delegation margins have been
studied in incentivised financial settings \citep{germann_algorithm_2023,
holzmeister_delegation_2023}.
```

**S-6c — Closing bridge for strand 2 (new; replaces the comment block at lines 30–35):**

```latex
Two features of our design speak to this literature. First, by calibrating the
algorithm to each subject's own measured performance and making this common
knowledge, we shut down the relative-competence considerations that drive much
of the heterogeneity above. Second, the institutional environment in which the
delegation choice is embedded --- in particular, whether the human remains
exposed to sanctions for the algorithm's output --- has to our knowledge not
been varied in this literature. Our punishment manipulation isolates exactly
this margin.
```

*Optional, your call:* `normann_delegate_2025` (delegation of pricing to a collusive algorithm) widens the scope beyond the moral domain — the 2026-05-12 lit review recommended it only if you want that breadth; I'd leave it out to keep the strand tight. `sunstein_anatomy_2024` and `bonnefon_moral_2024` are placed in §2.8's footnote instead.

## 2.8 Strand 3 opening: moral domain (lines 37–40)

Three fixes: (i) "The consensus is" is too strong now that the recent strand (¶48) documents the opposite pattern — "much of this work concludes" keeps the arc honest without spoiling ¶48's reveal; (ii) the Gogoll & Uhl description should say what they actually did on the use side (forced choice between human and machine delegate of *equal calibrated performance*; only ~26% choose the machine) — that "must delegate" feature is also what makes their observer result so clean later; (iii) the orphan one-sentence paragraph at line 40 gets absorbed as the topic sentence of the attribution paragraph (§2.9 below). Optionally, anchor the subsection's recency with the two recent surveys in a footnote.

**S-7 — Replacement for lines 38–40:**

```latex
Within this body of work, a smaller subset studies algorithm use in settings
whose consequences fall partly or wholly on someone other than the
decision-maker, sometimes called the \textit{moral domain}
\citep{gogoll_rage_2018}. Much of this work concludes that aversion to
algorithms is amplified once third-party welfare is at stake.
\citet{gogoll_rage_2018} document this in an incentivised task in which
subjects must delegate to either a human or a machine of equal, calibrated
performance: only about a quarter choose the machine. \citet{bigman_people_2018}
document the same preference in vignettes across high-stakes moral domains
(driving, legal, medical, military), and \citet{jauernig_people_2022} identify
\textit{moral discretion} as the human capacity that people specifically value
in such settings.\footnote{For recent surveys of this area see
\citet{bonnefon_moral_2024} and, with a legal-policy focus,
\citet{sunstein_anatomy_2024}.}
```

## 2.9 Observer attributions, vignette strand (line 42) and incentivised strand (line 44)

**Line 42.** Fixes: (a) the dangling "document the same pattern" (same as *what*? — nothing has been asserted yet); (b) the **Bigman misattribution** (Priority #2): the outrage asymmetry is Bigman et al. 2023, which simultaneously supplies your post-2020 *workplace/hiring* reference; (c) **Kurtzberg**: drop it — it is pre-2020 (your stated rule for domain references), and the bib note records that the real authors/title are Naquin & Kurtzberg, "Human reactions to technological failure…", so the citation would render under a different name than the prose implies anyway; (d) add `awad_drivers_2020` (NHB) for the driving domain — post-2020, top venue; (e) Pezzo is pre-2020 but functions as the *early evidence* anchor rather than a domain representative, so I'd keep it labelled as such (strict variant: delete the Pezzo clause and let Tobia carry the medical domain).

**S-8 — Replacement for lines 40–42 (the line-40 orphan is absorbed as the opening):**

```latex
Once decisions affect third parties, the responsibility-shifting motive
established for human delegation becomes relevant for algorithmic delegation
as well --- and with it the question of how observers apportion blame when an
algorithm is involved in the decision. A first strand of evidence,
predominantly vignette-based and unincentivised, finds that they generally do
so to the human's advantage. Early evidence comes from the medical domain, where a physician who follows a (bad)
recommendation from a computerised decision aid is faulted less than one who
errs unaided \citep{pezzo_pezzo_physician_2006}; \citet{tobia_when_2021}
extend the point to liability, showing that physicians who follow
standard-of-care AI recommendations face reduced legal exposure --- an
incentive, the authors argue, to follow such recommendations precisely because
doing so shields the physician from blame. In hiring, algorithmic
discrimination triggers less moral outrage than identical human
discrimination, and the responsible organization is judged less harshly
\citep{bigman_algorithmic_2023}. In automated driving, blame is apportioned
asymmetrically between the two actor types: when a human and a machine driver
of a shared-control vehicle both err, observers assign the machine the smaller
share of the blame \citep{awad_drivers_2020}. \citet{shank_attributions_2019}
examine moral
violations produced by human--algorithm pairs and find that the precise
division of authority matters: humans who monitor algorithms are blamed less
than humans acting alone or humans receiving algorithmic recommendations.
```

*(On Awad, the safest claim is the title's: drivers are blamed more than their automated cars in dual-error crashes. If you prefer the simpler reading "the machine's involvement reduces total blame on the human relative to a fully human benchmark", check the paper's Study 1 framing first — the snippet above stays within what the abstract supports.)*

**Line 44.** Your comment: "It's hard to follow…there is no real red line… Does it not tie into Shank attributions 2019?" Yes — the tie is *division of authority*: Shank gives the observer-side vignette evidence, Kirchkamp & Strobel the incentivised self-side counterpart on *shared* decisions; Maasland then moves to delegation proper; and Gogoll & Uhl's observer result (currently missing entirely, Priority #8) is the cleanest incentivised antecedent of your punishment stage. Direction fixes: Kirchkamp's selfishness increase is relative to *deciding alone* and similar for human and computer partners (the current "more selfish … with humans" is not what the paper's highlights state); Maasland *do* find a (conditional) tendency to delegate dismissals more than promotions — aversion dominates overall, but the current "does not overcome" erases their nuance.

**S-9 — Replacement for line 44:**

```latex
Evidence from incentivised experiments is younger, smaller, and more mixed.
The observer-side result of \citet{gogoll_rage_2018} is the closest antecedent
of our punishment stage: their observers evaluate subjects who delegated to a
machine less favourably than subjects who delegated to a human --- for
successful and failed outcomes alike. On the decision-maker side,
\citet{kirchkamp_sharing_2019} provide the incentivised counterpart to
\citet{shank_attributions_2019}'s division-of-authority evidence: in a
dictator game in which the decision is shared with either another human or a
computer, selfish choices become more frequent relative to deciding alone, but
to a similar extent for both partner types, and dictators report no lower felt
responsibility when the partner is a machine. Moving from shared decisions to
full delegation, \citet{maasland_blame_2022} find in a computer-aided HR
setting that respondents show some tendency to hand unpleasant dismissal
decisions (rather than promotions) to an algorithm, but the effect is fragile
and algorithm aversion dominates blame avoidance overall.
```

## 2.10 The recent "moral cover" strand (line 48)

This paragraph contains the two clearest factual errors in the section (Priorities #1 and #6):

- **Köbis:** the paper *explicitly* reports "no evidence that people requested more cheating from machines than from humans when using natural language" (their study 3). What they show: delegation interfaces that permit vague goal-setting sharply increase dishonest requests (plausible deniability — the framing your sentence already has), and machine agents *comply* with unethical instructions far more often than human agents (~79–98% vs ~25–40%).
- **Chevrier:** delegation rates do **not** differ across their treatments (17% human / 17% rule-based / 23% AI, n.s.); recipients punish AI-mediated inequality less *often* but more *severely*; the AI *programmer* is punished less than the rule-based programmer; and it is the *programmers* who exploit the wiggle room (60% choose the inegalitarian option vs 30% of human intermediaries).
- Therefore the wrap-up "the direction of the effect on delegation is uniformly positive" is unsupportable; only Hueholt & Szech show a higher delegation rate to AI.
- **Tontrup:** worth adding their sharpest fact — *prosocial* subjects are the most likely to involve the AI, which is what makes the moral-cost reading bite.
- Hueholt & Szech is accurately described (verified against the paper: incentivised trolley-style charitable choice; delegation to AI > human across both studies).

**S-10 — Replacement for line 48:**

```latex
A more recent strand documents the opposite pattern: algorithmic
intermediaries serving as moral cover. \citet{chevrier_algorithm_2024} extend
the blame chain to the programmer behind the algorithm: recipients punish
inegalitarian AI-mediated allocations less often, the programmer of an
autonomous AI is punished less severely than the programmer of a fully
controlled one --- and programmers respond by choosing the inegalitarian
option more often, exploiting the moral wiggle room that the AI's autonomy
creates, while delegation rates themselves do not differ across intermediary
types. \citet{kobis_delegation_2025} show in large preregistered die-roll and
tax experiments that delegation interfaces permitting vague goal-setting
sharply increase dishonesty --- principals can induce cheating without ever
stating it --- and that machine agents comply with unethical instructions far
more often than human agents do. \citet{tontrup_strategic_2025} let allocators
involve ChatGPT in a dictator-game allocation: those who do transfer less to
the recipient, and prosocial subjects are the most likely to involve the AI,
consistent with delegation lowering the moral cost of selfish choices.
Finally, \citet{hueholt_trusting_2026} use an incentivised trolley-style
choice between two real charitable allocations and find that subjects delegate
the moral decision to an AI significantly more often than to a human delegate.
The common motif across these settings is that the algorithm provides moral
cover; on which margin it operates differs --- only in
\citet{hueholt_trusting_2026} does it appear as a higher delegation rate ---
and it stands in contrast to \citet{maasland_blame_2022}, where aversion
dominates the blame-shifting motive in the same broad domain.
```

*(Optional recency add for this paragraph or a footnote: `jolly_not_2025` — autonomy-restricting workplace algorithms facilitate unethical behavior via displacement of responsibility; J. Business Ethics. It is in the bib, unused. Fits the motif; include if you want a workplace data point here.)*

## 2.11 Feier paragraph (line 50)

Accuracy fixes, all verified against the paper text in your library: (i) the evaluators are not "third parties" — the *affected participants themselves* evaluate, in a dual role, the decision-maker whose choice determined their own payoff (this matters because your own design shares the recipient-as-punisher structure while *separating* the roles, which is exactly your second extension); (ii) the elicitation is a single reward–punishment scale (−40 to +40 ECU), so "punishment is only reduced significantly" is better stated as evaluations being significantly more favourable; (iii) your comment's point (a) — the gap is not specifically outcome-conditional — goes in as a footnote with your reanalysis numbers; (iv) double space after "treatment,".

**S-11 — Replacement for line 50:**

```latex
The most closely related study is \citet{feier_hiding_2022}, who study
delegation to an algorithm in an incentivised laboratory experiment. Subjects
choose whether their own performance in a Raven-style logic task or the
performance of a delegate --- another participant or, depending on the
treatment, an algorithm calibrated to the session-level distribution of human
performance --- determines another participant's payoff; the subject's own
payoff is unaffected by this choice. Evaluation lies with the affected
participants themselves: in a dual role, each subject may reward or punish the
decision-maker whose choice determined her own payoff, on a single
reward--punishment scale elicited via the strategy method. The headline
finding is that decision-makers are evaluated significantly more favourably
when a bad outcome was produced by the algorithm than when they produced it
themselves, while no such gap arises for bad outcomes produced by a human
delegate. Thus algorithm delegation, but not human delegation, shields the
principal from blame for bad outcomes.\footnote{The shield is not specific to
bad outcomes: in their data, the evaluation gap between self-made and
algorithm-delegated decisions is of similar magnitude after good outcomes,
where it likewise favours delegation (a within-treatment interaction test on
their published data yields $p=0.67$; own computations). This is consistent
with evaluators rewarding the use of the algorithm as such, rather than
specifically excusing its failures.}
```

*(The footnote uses the numbers from `replication_materials/feier_hiding_2022/reanalysis_03_alternative_stories.py`, which the 2026-05-22 report verified against script output. If you prefer not to introduce own computations in the lit section, cut everything after "where it likewise favours delegation".)*

## 2.12 Extension paragraph (line 52)

This is the paragraph your two trickiest comments attach to. Decisions implemented below:

- **Dimension 1 + your "Careful: applies to both delegating to the algorithm and delegating to another human."** Correct, and the same point appears in results.tex line 240. Resolution: state the signal-extraction concern as bearing on Feier's *delegated-vs-self* comparisons (which is where their significant result lives), and acknowledge in a footnote that, since the session-level calibration applies to both delegate types, the channel does not by itself explain their algorithm–human differential. This keeps the critique honest and referee-proof. The optional Weitzner cite formalizes ability-signalling through algorithm use; it is *design-side* motivation (why individual calibration matters), so it does not violate your neutral-setup decision — but it is genuinely optional and easily dropped.
- **Dimension 2 + your "Maybe leave out the second point… Otherwise include a footnote that shows empirically that the punishment decisions are linked…"** Recommendation: **keep the dimension, add the footnote.** You have the empirical support already computed (in Feier's machine treatment, the evaluator's own delegation decision correlates with her good-outcome evaluation gap, r = −0.34, but not the bad-outcome gap, r = 0.02). That framing — "the concern is empirically visible but does not drive their headline result" — extends Feier rather than undermining them, and it also resolves your second bullet at lines 56–58. Note the intro currently advertises only *two* design departures; see Part 4.
- **Dimension 3** is garbled in the current text ("delegation rates between the two treatments may be different not because of…" — whose treatments?). Rewrite states the identification point plainly and anchors it to BF2012's on/off comparison, which is what makes your manipulation a *transposition* of the canonical test rather than an invention from nowhere.

**S-12 — Replacement for line 52:**

```latex
Our design extends \citet{feier_hiding_2022} along three dimensions. First,
their algorithm is calibrated at the session level, so the delegation decision
carries a signal about the subject's beliefs concerning her ability relative
to the pool --- indeed, their own analysis shows that the propensity to
delegate is driven primarily by self-assessed errors in the logic task, not by
the type of delegate. Punishment of a non-delegator may then partly sanction
perceived overconfidence rather than responsibility-taking per
se.\footnote{Because the session-level calibration applies to their
human-delegate treatment as well, this signal-extraction channel bears on the
comparison between delegated and self-made decisions within each treatment; it
does not by itself explain why the evaluation gap emerges only for the
algorithmic delegate. See \citet{weitzner_reputational_2024} for a
formalization of ability-signalling through algorithm use.} We instead
calibrate the algorithm to each subject's own measured performance and make
this common knowledge between the players, removing the relative-performance
signal of delegation by construction. Second, in their design the same subject
acts as both delegator and evaluator, which may import self-justification
motives into the evaluation decision;\footnote{In their data, the evaluator's
own delegation decision is significantly correlated with her evaluation gap
after good outcomes ($r=-0.34$ in the machine treatment) but not after bad
outcomes ($r=0.02$; own computations from their published data) --- the
dual-role concern is thus empirically visible, though it does not drive their
headline bad-outcome result.} we separate the delegator and evaluator roles
across disjoint subject pools. Third, punishment is always possible in their
design --- as in nearly all of the algorithmic literature reviewed above ---
so the motivational question of whether the prospect of punishment itself
drives delegation is not identified. We add a condition in which punishment is
ruled out by construction, transposing to algorithmic delegation the
punishment-on/off comparison through which \citet{bartling_shifting_2012}
established the motive for human delegation.
```

## 2.13 Closing claim (line 54)

Current text has the duplicated "to our knowledge", a missing "for", a missing comma — and, more importantly, after §2.3 the novelty must be scoped to algorithmic delegation (BF2012 ran the on/off test for human delegation). The two halves of the contribution also deserve one sentence each rather than headline + afterthought.

**S-13 — Replacement for line 54 (and delete the comment block at lines 56–58, now absorbed into §2.11/§2.12 footnotes):**

```latex
Our experiment is, to our knowledge, the first to provide a clean test of
blame shifting onto an algorithm in a setting with inherent outcome
uncertainty, controlling for relative-performance concerns by construction. It
is also the first to vary the punishment possibility itself for an algorithmic
delegate, and hence to test whether, in such a setting, the prospect of
punishment motivates the delegation decision.
```

---

# Part 3 — Your inline [Comment:] blocks, adjudicated

| # | Location | Comment (gist) | Recommendation | Snippet |
|---|---|---|---|---|
| 1 | lines 3–5 | Roadmap paragraph necessary? Better in intro? | Drop the enumeration (it duplicates intro ¶15); replace with a 2-sentence functional opener. Library audit: only 3/65 papers open with a strand-enumerating bridge. | §2.1 |
| 2 | line 9 | Add Bolton & Dewatripont; Schelling + applications footnote | Yes to all; keys and BibTeX provided. | §2.2 |
| 3 | line 15 | Argenton commented out | **Reinstate** — one sentence, strand-1 canon, EER 2023 recency; no tension with neutral setup. | §2.5 (last core sentence) |
| 4 | line 17 | Add Kandul/Kirchkamp; Gawn/Innes; Garofalo & Rott; Charness; Maximiano | Deception cluster: **yes** (Gawn & Innes 2019 + 2021, Kandul & Kirchkamp as see-also). Garofalo & Rott: **only with its true boundary framing** (delegating communication backfires — Management Science 2018). Charness/Maximiano: optional one-liner, included as marked optional. | §2.5 |
| 5 | lines 19–21 | Barber & Odean; AI-vs-human delegation refs (Dietvorst, Leyer & Schneider, Logg, Candrian, Germann, Holzmeister) | **Barber & Odean: do not add** — the quoted claim is not in that paper (it is about overconfidence and trading volume, not delegation to advisors). The AI-vs-human delegation contrast lives in the new ceding-control paragraph via Candrian 2022 + Ivanova-Stenzel & Tolksdorf 2025; Germann & Merkle and Holzmeister et al. added as the financial-delegation cluster; Leyer & Schneider skipped (conference paper; Candrian covers the point in a better venue). | §2.7, S-6b |
| 6 | line 23 | Steffel: leave out because it returns in results? | **Yes, leave out** — consistent with your neutral-setup decision; results.tex already cites it where it earns its keep. Optional design-motivation clause provided if you ever want it. | §2.5 |
| 7 | lines 32–35 | Reviews old-ish; add recent refs; include Dargnies/Hakimov/Kübler; place the two Ivanova-Stenzel papers | Recency: `qin_ai_2025` (in), add `kormylo_till_2025` + `dargnies_aversion_2026` (both already in bib, MS 72(1) special issue), surveys `bonnefon_moral_2024`/`sunstein_anatomy_2024` as a footnote in strand 3. Both Ivanova-Stenzel papers anchor the new ceding-control paragraph. Note: it's **Dargnies** (not "Dargies"). | §2.7, §2.8 |
| 8 | line 42 | Kurtzberg too old; post-2020 only for domains | Drop Kurtzberg (also: bib note says the true authors/title are Naquin & Kurtzberg 2004, so the rendered citation wouldn't match the prose anyway). Post-2020 domain set: hiring → `bigman_algorithmic_2023`; driving → `awad_drivers_2020`; medical → `tobia_when_2021` already qualifies; Pezzo kept as labelled *early evidence* (strict variant: cut it). | §2.9, S-8 |
| 9 | line 46 | Kirchkamp "no red line"; ties into Shank? | Yes: division-of-authority is the thread. Shank (observer-side vignettes) → Kirchkamp (incentivised self-side, shared decisions) → Maasland (delegation proper) → G&U observer result added as the punishment-stage antecedent. | §2.9, S-9 |
| 10 | line 52, comment 1 | "Careful, this applies to both delegating to the algorithm and to another human" | Agreed (same point as results.tex line 240). Handled in the dimension-1 footnote: signal applies to both delegate types in Feier → it bears on delegated-vs-self margins and does not alone explain their algorithm–human differential. | §2.12 |
| 11 | line 52, comment 2 | "Maybe leave out the second point… or footnote with empirical link" | **Keep point, add footnote** with your computed correlations (r = −0.34 good / 0.02 bad). Empirically grounded, extends rather than attacks Feier. Requires harmonizing the intro's "two design features" — see Part 4. | §2.12 |
| 12 | lines 56–58 | Two Feier reanalysis findings to include somewhere | Bullet (a) → footnote in the Feier paragraph (§2.11). Bullet (b) → footnote on dimension 2 (§2.12). Both with "own computations" attribution. | §2.11, §2.12 |

---

# Part 4 — Cross-section consistency (changes in *other* files)

These are not literature.tex edits, but the lit section cannot be finalized coherently without them.

1. **introduction.tex ¶15: broken promise.** "We argue in Section~\ref{literature} that the two findings are reconcilable…" — the reconciliation argument lives in *results.tex* ("Reconciling our findings with Feier et al."), and under your neutral-setup decision it should stay there. Fix the intro pointer, e.g.:
   ```latex
   We argue in Section~\ref{results} that the two findings are reconcilable: ...
   ```
   (or reference the specific subsection label once results.tex stabilizes).
2. **introduction.tex ¶9 vs lit ¶52: two vs three departures from Feier.** If you keep dimension 2 (recommended), the intro should either say "three design features" or explicitly frame it as "two identification-critical features, plus a separation of delegator and evaluator roles that removes self-justification motives from the punishment data." Pick one and make them match.
3. **introduction.tex ¶9: "a test that is not feasible in designs where punishment is always possible."** Overbroad — BF2012's D&noP vs D&P is exactly that test for human delegation. Suggested scoping:
   ```latex
   ... allowing us to identify the effect of anticipated punishment on the
   delegation decision itself --- a test that none of the existing
   algorithmic-delegation designs permits.
   ```
4. **design.tex H1 grounding (¶72).** The hypothesis section says BF "also show that subjects are more likely to delegate morally consequential decisions even to a die roll" — loose on two counts (39% delegate to the die *vs 56% to a human*, and the comparison benchmark is unstated). More importantly, H1's true anchor is BF's 17%→56% on/off result, which design.tex never states. Suggest adding one sentence there:
   ```latex
   In the canonical human-delegate setting, removing the punishment possibility
   collapses the delegation rate from 56\% to 17\% \citep{bartling_shifting_2012};
   H1 transposes this comparison to an algorithmic delegate.
   ```
5. **results.tex line 240** (the "[Consideration for literature review]" about the Feier signal applying to both treatments) is resolved by the §2.12 dimension-1 footnote — you can delete that note once S-12 is in.

---

# Part 5 — Mechanics (quick fixes, no judgment calls)

| Line | Issue | Fix |
|---|---|---|
| 19–21, 32–35, 46, 56–58 + inline at 9, 17, 42, 52 | Bare `[Comment: …]` text **compiles into the PDF** (design.tex uses `\todo[inline]` for the same purpose) | Wrap in `\todo[inline,color=yellow!50]{…}` or `%` — or apply the snippets above, which absorb/remove them |
| 13 | Double space: `punishment.  \citet{hamman` | fixed in S-4 |
| 50 | Double space: `treatment,  delegate` | fixed in S-11 |
| 54 | "first to our knowledge to" (duplicate); "controlling relative-performance concerns" (missing "for"); "whether, in such a setting the prospect" (missing comma) | fixed in S-13 |
| 38 | Mixed series punctuation: "…, \citet{bigman…} in vignettes…; and \citet{jauernig…}" | fixed in S-7 |
| 9 | "e.g. as a commitment device" — AER style prefers "e.g.," or restructuring | fixed in S-2 |
| 15, 23, 30 | Dead commented-out lines once their content is resolved | delete at polish stage (per your draft-inclusiveness preference, not now) |
| 7, 27, 37 | `\subsection*` (unnumbered) — AER-style papers typically number subsections (A., B., …) | style call; flag only |

---

# Part 6 — BibTeX to append to `ProjectAlgorithm.bib`

All entries verified against publisher pages / IDEAS / the paper PDFs this session except where a `VERIFY` note says otherwise (kept consistent with the file's existing convention). Run `/validate-bib` after pasting.

```bibtex
%%% =====================================================================
%%% Additions from literature.tex review, 2026-06-12.
%%% Classic strand-1 references (Bartling-Fischbacher framing apparatus)
%%% =====================================================================

@book{bolton_contract_2005,
    title = {Contract Theory},
    author = {Bolton, Patrick and Dewatripont, Mathias},
    publisher = {MIT Press},
    address = {Cambridge, MA},
    year = {2005}
}

@book{schelling_strategy_1960,
    title = {The Strategy of Conflict},
    author = {Schelling, Thomas C.},
    publisher = {Harvard University Press},
    address = {Cambridge, MA},
    year = {1960}
}

@article{aghion_formal_1997,
    title = {Formal and Real Authority in Organizations},
    author = {Aghion, Philippe and Tirole, Jean},
    journal = {Journal of Political Economy},
    volume = {105},
    number = {1},
    pages = {1--29},
    year = {1997},
    doi = {10.1086/262063}
}

@article{vickers_delegation_1985,
    title = {Delegation and the Theory of the Firm},
    author = {Vickers, John},
    journal = {The Economic Journal},
    volume = {95},
    number = {Supplement},
    pages = {138--147},
    year = {1985},
    doi = {10.2307/2232877}
}

@article{rogoff_optimal_1985,
    title = {The Optimal Degree of Commitment to an Intermediate Monetary Target},
    author = {Rogoff, Kenneth},
    journal = {The Quarterly Journal of Economics},
    volume = {100},
    number = {4},
    pages = {1169--1189},
    year = {1985},
    doi = {10.2307/1885679}
}

@article{jones_have_1989,
    title = {Have Your Lawyer Call My Lawyer: Bilateral Delegation in Bargaining Situations},
    author = {Jones, Stephen R. G.},
    journal = {Journal of Economic Behavior \& Organization},
    volume = {11},
    number = {2},
    pages = {159--174},
    year = {1989},
    note = {VERIFY page range before submission}
}

@article{schotter_bargaining_2000,
    title = {Bargaining Through Agents: An Experimental Study of Delegation and Commitment},
    author = {Schotter, Andrew and Zheng, Wei and Snyder, Blaine},
    journal = {Games and Economic Behavior},
    volume = {30},
    number = {2},
    pages = {248--292},
    year = {2000},
    doi = {10.1006/game.1999.0728},
    note = {VERIFY doi}
}

@article{huck_strategic_2004,
    title = {Strategic Delegation in Experimental Markets},
    author = {Huck, Steffen and M{\"u}ller, Wieland and Normann, Hans-Theo},
    journal = {International Journal of Industrial Organization},
    volume = {22},
    number = {4},
    pages = {561--574},
    year = {2004},
    doi = {10.1016/j.ijindorg.2003.11.001},
    note = {VERIFY doi}
}

%%% Deception / domains cluster (strand 1, line 17)

@article{gawn_lying_2019,
    title = {Lying Through Others: Does Delegation Promote Deception?},
    author = {Gawn, Glynis and Innes, Robert},
    journal = {Journal of Economic Psychology},
    volume = {71},
    pages = {59--73},
    year = {2019}
}

@article{gawn_machiavelli_2021,
    title = {Machiavelli Preferences Without Blame: Delegating Selfish vs.\ Generous Decisions in Dictator Games},
    author = {Gawn, Glynis and Innes, Robert},
    journal = {Journal of Behavioral and Experimental Economics},
    volume = {90},
    year = {2021},
    note = {VERIFY article number/pages}
}

@article{kandul_do_2018,
    title = {Do {I} Care If Others Lie? {Current} and Future Effects When Lies Can Be Delegated},
    author = {Kandul, Serhiy and Kirchkamp, Oliver},
    journal = {Journal of Behavioral and Experimental Economics},
    volume = {74},
    pages = {70--78},
    year = {2018}
}

@article{garofalo_shifting_2018,
    title = {Shifting Blame? {Experimental} Evidence of Delegating Communication},
    author = {Garofalo, Orsola and Rott, Christina},
    journal = {Management Science},
    volume = {64},
    number = {8},
    pages = {3911--3925},
    year = {2018},
    doi = {10.1287/mnsc.2017.2782}
}

@article{charness_attribution_2004,
    title = {Attribution and Reciprocity in an Experimental Labor Market},
    author = {Charness, Gary},
    journal = {Journal of Labor Economics},
    volume = {22},
    number = {3},
    pages = {665--688},
    year = {2004},
    doi = {10.1086/383111}
}

@article{maximiano_gift_2013,
    title = {Gift Exchange and the Separation of Ownership and Control},
    author = {Maximiano, Sandra and Sloof, Randolph and Sonnemans, Joep},
    journal = {Games and Economic Behavior},
    volume = {77},
    number = {1},
    pages = {41--60},
    year = {2013}
}

%%% Ceding-control / delegation-to-AI cluster (strand 2)

@article{candrian_rise_2022,
    title = {Rise of the Machines: Delegating Decisions to Autonomous {AI}},
    author = {Candrian, Cindy and Scherer, Anne},
    journal = {Computers in Human Behavior},
    volume = {134},
    pages = {107308},
    year = {2022},
    doi = {10.1016/j.chb.2022.107308},
    note = {VERIFY author first names against the journal page}
}

@article{germann_algorithm_2023,
    title = {Algorithm Aversion in Delegated Investing},
    author = {Germann, Maximilian and Merkle, Christoph},
    journal = {Journal of Business Economics},
    volume = {93},
    number = {9},
    pages = {1691--1727},
    year = {2023},
    doi = {10.1007/s11573-022-01121-9}
}

@article{holzmeister_delegation_2023,
    title = {Delegation Decisions in Finance},
    author = {Holzmeister, Felix and Holm{\'e}n, Martin and Kirchler, Michael and Stefan, Matthias and Wengstr{\"o}m, Erik},
    journal = {Management Science},
    volume = {69},
    number = {8},
    pages = {4828--4844},
    year = {2023},
    doi = {10.1287/mnsc.2022.4555}
}

%%% Post-2020 domain references (strand 3, line 42)

@article{bigman_algorithmic_2023,
    title = {Algorithmic Discrimination Causes Less Moral Outrage Than Human Discrimination},
    author = {Bigman, Yochanan E. and Wilson, Desman and Arnestad, Mads N. and Waytz, Adam and Gray, Kurt},
    journal = {Journal of Experimental Psychology: General},
    volume = {152},
    number = {1},
    pages = {4--27},
    year = {2023},
    doi = {10.1037/xge0001250},
    note = {VERIFY middle author spellings against the APA page}
}

@article{awad_drivers_2020,
    title = {Drivers Are Blamed More Than Their Automated Cars When Both Make Mistakes},
    author = {Awad, Edmond and Levine, Sydney and Kleiman-Weiner, Max and Dsouza, Sohan and Tenenbaum, Joshua B. and Shariff, Azim and Bonnefon, Jean-Fran{\c c}ois and Rahwan, Iyad},
    journal = {Nature Human Behaviour},
    volume = {4},
    number = {2},
    pages = {134--143},
    year = {2020},
    doi = {10.1038/s41562-019-0762-8}
}

%%% Optional: precursors footnote (strand 2)

@book{meehl_clinical_1954,
    title = {Clinical versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence},
    author = {Meehl, Paul E.},
    publisher = {University of Minnesota Press},
    address = {Minneapolis},
    year = {1954}
}

@article{dawes_robust_1979,
    title = {The Robust Beauty of Improper Linear Models in Decision Making},
    author = {Dawes, Robyn M.},
    journal = {American Psychologist},
    volume = {34},
    number = {7},
    pages = {571--582},
    year = {1979}
}

%%% Optional: recent surveys footnote (strand 3) — sunstein PDF is already in
%%% master_supporting_docs/supporting_papers/

@article{sunstein_anatomy_2024,
    title = {An Anatomy of Algorithm Aversion},
    author = {Sunstein, Cass R. and Gaffe, Jared H.},
    journal = {Columbia Science and Technology Law Review},
    volume = {26},
    pages = {290--319},
    year = {2024},
    note = {VERIFY volume/pages against the published issue}
}
```

(`bonnefon_moral_2024`, `kormylo_till_2025`, `dargnies_aversion_2026`, `ivanova_stenzel_measuring_2024`, `ivanova_stenzel_delegating_2025`, `weitzner_reputational_2024`, `jolly_not_2025` already exist in the bib — no new entries needed for those.)

---

# Part 7 — Verification notes

**Verified against the actual paper text in your library (`_extracted_text/`):**
- BF2012 treatment structure and delegation rates (17% / 56% / 39%, Fisher p<0.01) — read directly from the published text; also their statement that punishers are the receivers, and that A/B payoffs are perfectly aligned.
- Köbis et al.: "there was no evidence that people requested more cheating from machines than from humans when using natural language"; "cheating requests by principals were not always higher for machine agents"; compliance figures 79–98% (Llama/Claude).
- Kirchkamp & Strobel treatments (SDT/MDT/CDT) and highlights ("when the decision is shared with a computer the number of selfish choices increases"; "humans behave quite similar when deciding with a computer [as] with another human").
- Feier et al. role structure (evaluators are the participants whose own payoff was affected; dual role).

**Verified against the per-paper summaries in `supporting_papers/summaries/` (generated from the PDFs):** Coffman treatment logic (passive intermediary; Allow-Taking), Oexl Choice/Random results ($2.58→$1.92; $2.01→$1.59; intermediary $0.64→$0.72 n.s.), Gogoll & Uhl design and observer rewards (17.77/12.52; 4.42/0.49; 26.5% machine choice), Feier evaluation scale (−40..+40 ECU) and results (machine bad-outcome gap p=0.041; human n.s.; delegation 46.1% vs 56.2% n.s.), Hueholt & Szech (N=5,639; AI>human delegation in both studies), Chevrier (delegation 17/17/23 n.s.; extensive/intensive punishment margins; programmers 60% inegalitarian), Bigman & Gray 2018 (ex-ante aversion, persists for positive outcomes; outrage asymmetry NOT in this paper), Pezzo (attenuation in both directions; agreeing protective), Shank (monitoring protective, recommendations not).

**Verified via prior project reports:** Feier reanalysis numbers (interaction p=0.672; r=−0.337/+0.022) from `quality_reports/lit_subsection3_comment_responses.md`, which states it checked them against the `reanalysis_0*.py` outputs.

**Verified via web this session (publisher/IDEAS pages):** Bigman et al. 2023 (JEP:G 152(1):4–27, doi 10.1037/xge0001250); Awad et al. 2020 (NHB 4(2):134–143); Gawn & Innes 2019 (JoEP 71:59–73) and 2021 (JBEE 90); Kandul & Kirchkamp 2018 (JBEE 74:70–78); Garofalo & Rott 2018 (MS 64(8):3911–3925); Huck/Müller/Normann 2004 (IJIO 22(4):561–574); Holzmeister et al. 2023 (MS 69(8):4828–4844); Candrian & Scherer 2022 (CHB 134:107308); Germann & Merkle 2023 (JBE 93(9):1691–1727); Charness 2004 (JLE 22(3):665–688); Maximiano et al. 2013 (GEB 77(1):41–60).

**Known weak spots (flagged in place):** Jones 1989 page range; Schotter et al. and Huck et al. DOIs; Gawn & Innes 2021 article number; Sunstein & Gaffe volume/pages; Bigman 2023 middle-author spellings. All carry `VERIFY` notes in the BibTeX, matching your file's convention; `/validate-bib --semantic` will catch them.

**What I deliberately did not suggest:** pre-positioning Steffel, Weitzner-as-interpretation, or any reversal-anticipating strand in the lit section (your neutral-setup decision — Weitzner appears only as an optional design-side footnote cite in S-12); any framing that elevates process ownership (M3) over the other candidate mechanisms; Barber & Odean (claim not supported by the paper); Leyer & Schneider 2019 (weak venue, point covered by Candrian 2022); `normann_delegate_2025` in the main text (scope widening — flagged as optional only).
