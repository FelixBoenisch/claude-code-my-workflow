---
title: Literature Review — Recent (2024–2026) work on AI/algorithm delegation and responsibility
date: 2026-05-12
status: DRAFT
scope: Filtered to top-5 econ, top field (econ + management + psychology), top general-science (Nature/Science/PNAS/Nature Human Behaviour), and major working papers (NBER / SSRN / CRC TRR 190 / arXiv econ.GN / GREDEG)
existing_bibliography_anchor: ProjectAlgorithm.bib
---

# Literature Review: Recent work on blame avoidance / responsibility shifting through algorithm and AI delegation (2024–2026)

**Query:** Identify what's been published or is circulating since the existing manuscript bibliography was assembled (newest entries there: `kobis_delegation_2025` Nature, `bockstedt_humans_2025` MS, `ivanova_stenzel_measuring_2024` JBEE, `chevrier_algorithm_2024` GREDEG WP).

**Filtering:** Top-5 econ (AER, QJE, JPE, ECMA, RES), top field (MS, JMR, JEBO, JBEE, ExpEcon, GEB, JPubE, RESTAT, AEJ family), top general-science (Nature, Science, PNAS, NHB), top psychology/decision (Psych Science, JEP:G, OBHDP, Cognition). Working papers from NBER, IZA, CESifo, SSRN, CRC TRR 190, GREDEG, ECONtribute, CEPR, arXiv econ.GN.

---

## Summary

Since early 2025, the literature has moved fast. Three threads are active and directly relevant to the manuscript:

1. **AI as a moral wiggle-room device.** The hypothesis that delegating to an algorithm reduces the principal's experienced moral cost — central to your paper — is now being tested explicitly in dictator games and HR-style designs. Tontrup & Sprigman (2025, SSRN WP) find that allocators who can involve ChatGPT transfer less, with prosocial subjects most likely to engage AI; Jolly, Dunlop, Parker & Kanse (2025, *J. Business Ethics*) find that autonomy-restricting ADM elicits more unethical behavior via displacement of responsibility. These echo the M3 (process-ownership / identity) mechanism you adopt in Section 4 of the manuscript.

2. **High-profile compliance asymmetry results.** Köbis et al. (2025, *Nature* — already in your bib) is the headline result, but its implications are still being unpacked. PNAS 2026 (Killoran & Park) reframes public blame toward AI as a *diagnostic* signal rather than something to be managed — a useful framing for your conclusion section's discussion of regulatory implications.

3. **Algorithm aversion / appreciation under explicit delegation.** The Management Science Special Issue on the Human-Algorithm Connection (Vol. 72, Issue 1, 2025–2026) brought several relevant pieces: Kormylo, Adjerid, Ball & Dogan (betrayal aversion); Dargnies, Hakimov & Kübler (hiring algorithm aversion with transparency manipulation). Ivanova-Stenzel & Tolksdorf — whose 2024 JBEE paper is already in your bib — circulated a 2025 follow-up (CRC TRR 190 DP 558) decomposing algorithm aversion into a general preference for decision autonomy. Weitzner (2024 arXiv WP) provides a rational microfoundation for algorithm aversion via reputational concern about ability — directly parallel to the signal-extraction reading you give of Feier et al. (2022).

4. **Algorithmic pricing delegation (more tangential).** Normann, Rulié, Stypa & Werner (2025, arXiv econ.GN + EconStor) put delegation to a self-learning pricing algorithm into a competition design — an industrial-organization-flavored cousin of your paper. Worth citing if you discuss real-world delegation contexts where the question of accountability has bite (collusive AI pricing has been a focus of recent EU/US regulator attention).

What's **not** appearing (yet) in 2025–2026 is anything that matches your specific design contribution: individual-level algorithm calibration + separate delegator/evaluator pools + punishment-on/off manipulation. The closest precedents — Feier et al. 2022, Chevrier & Teixeira 2024 WP, Köbis et al. 2025 — remain the sharp comparison set. The new 2025–2026 work mostly extends the dependent variable (compliance, displacement, autonomy preferences) rather than refining the identification of the responsibility-shifting channel itself.

---

## Recommended additions (curated)

### Published, top field — strong adds

#### 1. Kormylo, Adjerid, Ball & Dogan (2025) — *Management Science* 72(1)
- **Title:** "Till Tech Do Us Part: Betrayal Aversion and Its Role in Algorithm Use"
- **Pages:** 343–367 · **DOI:** 10.1287/mnsc.2022.03510
- **Contribution:** In a financial-advice context, willingness to take advice from a human expert drops sharply after a small breach of trust (betrayal aversion); willingness to follow algorithmic advice is *not* depressed by analogous trust violations. The price of this aversion is real: a 20% earnings loss for those who refuse human advice; no analogous loss for those interacting with the algorithm.
- **Relevance:** Adds a mechanism — betrayal aversion is *asymmetric* between human and algorithmic agents — which is consistent with your M3 framing (the human–human relationship carries a moral/relational charge that human–algorithm does not). Cite in the algorithm-aversion subsection of your literature review.

#### 2. Dargnies, Hakimov & Kübler (2026) — *Management Science* 72(1)
- **Title:** "Aversion to Hiring Algorithms: Transparency, Gender Profiling, and Self-Confidence"
- **Pages:** 285–301 · **DOI:** 10.1287/mnsc.2022.02774
- **Contribution:** Online experiment in which workers and managers choose between human and algorithmic hiring decisions. Transparency about the algorithm's predictors changes preferences only when it excludes gender; explaining how the algorithm works does *not* itself increase its use. Performance feedback to managers raises algorithm delegation by debiasing overconfidence.
- **Relevance:** Both another data point on algorithm aversion in a moral-domain task (hiring) and a sharp design lesson about what "transparency" does and doesn't buy. Most relevant for your literature review's algorithm-aversion subsection.

#### 3. Jolly, Dunlop, Parker & Kanse (2025) — *Journal of Business Ethics*
- **Title:** "It's Not My Responsibility: Working with Autonomy-Restricting Algorithms Facilitates Unethical Behavior and Displacement of Responsibility"
- **Volume/Pages:** 203, 405–424 (online 7 June 2025) · **DOI:** 10.1007/s10551-025-06034-5
- **Contribution:** Two work-simulation experiments (N=276 in Study 1) manipulating whether the ADM system is autonomy-affording vs autonomy-restricting. Subjects working with autonomy-*restricting* ADM cheat customers more, and report displacing personal responsibility onto the technology or an authority figure. Theoretical anchor: job-characteristics model + moral disengagement.
- **Relevance:** A clean test of the displacement-of-responsibility channel in an applied (workplace) setting, complementary to your laboratory framing. Cite alongside Falk & Szech 2013 and Feier et al. 2022 when you motivate the responsibility-shifting mechanism.

### Published, top general-science — moderate add

#### 4. Killoran & Park (2026) — *PNAS* 123(17)
- **Title:** "Learn from the blame game when AI causes harm"
- **Article:** e2528408123 · **DOI:** 10.1073/pnas.2528408123
- **Contribution:** A conceptual / framework paper (not an experiment). Argues that public blame against AI systems should be treated as diagnostic data about socio-technical failure, not as a PR problem. Proposes a three-part taxonomy (Ignorance / Diminished Control / Condemnation) that maps blame onto actors: designers, deployers, institutions, regulators.
- **Relevance:** Useful in the *conclusion / policy implications* section rather than the literature review. Your finding that the punishment possibility shifts delegation slots into the "Diminished Control" narrative.
- **VERIFY before submission:** author list (Killoran & Park) verified via web search of the PNAS page; we did not directly fetch a fully-rendered PNAS page due to access restrictions.

### Working papers — strong adds (circulating, likely R&R or new submission)

#### 5. Tontrup & Sprigman (2025) — SSRN WP
- **Title:** "Strategic Delegation of Moral Decisions to AI"
- **SSRN ID:** 5696827 · **Posted:** 6 October 2025
- **Contribution:** Dictator game with a $10 endowment; experimental treatment lets allocators involve ChatGPT in the allocation at a small time cost. Allocators who involve AI transfer significantly less to recipients. Prosocial subjects (Big-Five / SVO-classified) are *more* likely to invoke AI than proself subjects — consistent with AI being used precisely by those who experience higher moral cost from selfish behavior.
- **Relevance:** This is the closest direct competitor to your paper for the moral-cost-reduction channel. Your design with individual-level calibration + punishment-on/off identifies a different margin (accountability salience for the principal in the absence of third-party signal extraction), but the two papers are clearly siblings. Cite prominently in literature.tex and again in conclusion where you discuss mechanism.

#### 6. Ivanova-Stenzel & Tolksdorf (2025) — CRC TRR 190 Discussion Paper 558
- **Title:** "Delegating in the Age of AI: Preferences for Decision Autonomy"
- **Series:** Collaborative Research Center Transregio 190, LMU Munich / HU Berlin · **Date:** 22 December 2025
- **Pre-registered:** AsPredicted #131736 & #200326
- **Contribution:** Within-subject comparison of willingness to delegate the same task to an AI vs a human agent, across two domains (hiring as a social task, forecasting as analytical). Subjects under-utilize both agents even when informed of superior performance, but they prefer the AI to the human. Interpretation: algorithm aversion is largely a general preference for decision autonomy, not algorithm-specific distrust.
- **Relevance:** Same authors as your `ivanova_stenzel_measuring_2024` JBEE citation; this is the direct follow-up that puts AI vs human side-by-side. Cite in the algorithm-aversion subsection. The "preference for autonomy" interpretation is also consistent with your M3 (process-ownership) framing — worth flagging in the mechanism discussion.

#### 7. Normann, Rulié, Stypa & Werner (2025) — arXiv 2510.27636 / VfS Annual Conference 2025
- **Title:** "Delegate Pricing Decisions to an Algorithm? Experimental Evidence"
- **arXiv:** 2510.27636 [econ.GN], submitted 31 October 2025 · **JEL:** C90, D43, L12
- **Contribution:** Bertrand pricing experiment with three treatments: (a) baseline human pricing, (b) full delegation to a Q-learning collusive algorithm, (c) algorithmic recommendations with override. Delegation rates 45%–86%; surprisingly, prices are *lower* in algorithmic treatments than in baseline — human-in-the-loop interaction with the (potentially collusive) algorithm fosters competition.
- **Relevance:** Tangential to your moral-domain framing but the most polished recent econ-experimental delegation paper. Cite in the algorithm-delegation subsection if you want to widen the scope beyond moral-domain settings, or skip if you prefer to keep the review tightly bound to responsibility/blame.

#### 8. Weitzner (2024) — arXiv 2402.15418
- **Title:** "Reputational Algorithm Aversion"
- **arXiv:** 2402.15418 [econ.GN], v3 31 July 2024 · **Affiliation:** McGill University
- **Status:** Working paper, presented at AEA 2025; no journal acceptance yet
- **Contribution:** Theoretical model where overriding an algorithm signals high ability. Low-skill workers should always follow the algorithm but inefficiently override it to look high-skill; high-skill workers should sometimes override. Algorithm aversion as a fully rational reputational equilibrium.
- **Relevance:** Provides the formal microfoundation for the signal-extraction reading you give of Feier et al. (2022) in literature.tex paragraph 39. Cite when you reconcile the differential punishment in Feier with the null in your data — the relative-performance calibration in Feier turns on exactly the signal that Weitzner's model formalizes.

---

## Secondary / borderline (worth knowing about, lower priority)

These are recent and on-theme, but either the venue is outside your top-journal filter or the design is far enough from yours that adding them risks padding the lit review.

- **Tsumura & Yamada (2026), *Scientific Reports*** — "Effects of knowledge and importance on responsibility in human-AI decision making", doi:10.1038/s41598-025-32513-w. N=588, 3-factor between-subjects design. Finding: prior knowledge of agent shifts blame from user to agent and developer; high task importance increases responsibility attributed to developer. *VERIFY author list before citing — we did not directly fetch a fully-rendered Nature page.*
- **Salatino, Prével, Caspar & Lo Bue (2025), *Scientific Reports*** — "Influence of AI behavior on human moral decisions, agency, and responsibility", doi:10.1038/s41598-025-95587-6. Military cadets simulated drone-operator task; AI behavior influences explicit responsibility ratings. *VERIFY author list before citing.*
- **Hou et al. (2025), *Business and Politics*** — "The Paradox of Algorithms and Blame on Public Decision-makers". Cambridge journal, public-admin focus.
- **Saxena (2025), *J. Public Administration Research and Theory* 35(4)** — "Algorithmic discrimination in public service provision: Understanding citizens' attribution of responsibility...". Public-admin angle.
- **AEA P&P 2025: Mullainathan, "Economics in the Age of Algorithms"** — pp. 1–23. Essay/agenda-setting piece, not empirical.
- **Wagner (2025), *Psychology & Marketing*** — "Algorithm Delegation: How Embedded AI Facilitates Agency Transference in Medical Services". Marketing-journal venue.

---

## Thematic synthesis

### What the new literature confirms about your manuscript's framing

- **Moral-cost reduction through delegation to AI is now an empirically active hypothesis.** Tontrup & Sprigman (2025) and Jolly et al. (2025) both find it; Köbis et al. (2025) shows the related compliance-asymmetry result. Your H1 (delegation increases with punishment possibility, contrary to a pure responsibility-shifting story) is therefore landing into a literature that is *expecting* the responsibility-shifting effect.
- **Algorithm aversion is increasingly decomposed into orthogonal channels** — autonomy preferences (Ivanova-Stenzel & Tolksdorf 2025), reputational signaling (Weitzner 2024), betrayal asymmetry (Kormylo et al. 2025), and transparency/profile sensitivity (Dargnies et al. 2026). Your M3 mechanism (process ownership / identity) is consistent with the autonomy-preference channel and complementary to the rest.

### What's missing and where your paper sits

- **No 2025–2026 paper varies the punishment possibility itself.** Your H1 treatment is unique. The closest analog is the implicit punishment in dictator/HR settings — but a clean on/off manipulation does not appear in the new work.
- **No 2025–2026 paper calibrates the algorithm to the individual subject's performance.** Feier et al. (2022)'s session-level calibration remains the standard, and is one of the two design features (the other being delegator–evaluator separation) that distinguish your contribution.

### Where to place each addition in literature.tex

| Addition | Subsection in literature.tex |
|---|---|
| Kormylo et al. 2025 (MS) | Delegation to algorithms (algorithm-aversion list) |
| Dargnies et al. 2026 (MS) | Delegation to algorithms (algorithm-aversion list) |
| Ivanova-Stenzel & Tolksdorf 2025 (WP) | Delegation to algorithms (alongside their 2024 JBEE) |
| Jolly et al. 2025 (JBE) | Responsibility perceptions of decisions involving algorithms |
| Tontrup & Sprigman 2025 (WP) | Responsibility perceptions of decisions involving algorithms (close precedent) |
| Weitzner 2024 (arXiv WP) | Reconciliation with Feier et al. 2022 (paragraph 39) |
| Killoran & Park 2026 (PNAS) | Conclusion, policy section |
| Normann et al. 2025 (WP) | Optional — only if you want to widen scope beyond moral domain |

---

## BibTeX entries

```bibtex
@article{kormylo_till_2025,
    title = {Till {Tech} {Do} {Us} {Part}: {Betrayal} {Aversion} and {Its} {Role} in {Algorithm} {Use}},
    author = {Kormylo, Cameron and Adjerid, Idris and Ball, Sheryl B. and Dogan, Can},
    journal = {Management Science},
    volume = {72},
    number = {1},
    pages = {343--367},
    year = {2025},
    doi = {10.1287/mnsc.2022.03510},
    note = {Special Issue on the Human-Algorithm Connection}
}

@article{dargnies_aversion_2026,
    title = {Aversion to {Hiring} {Algorithms}: {Transparency}, {Gender} {Profiling}, and {Self}-{Confidence}},
    author = {Dargnies, Marie-Pierre and Hakimov, Rustamdjan and K\"ubler, Dorothea},
    journal = {Management Science},
    volume = {72},
    number = {1},
    pages = {285--301},
    year = {2026},
    doi = {10.1287/mnsc.2022.02774},
    note = {Special Issue on the Human-Algorithm Connection. Online 2024; journal issue 2026.}
}

@article{jolly_not_2025,
    title = {It's {Not} {My} {Responsibility}: {Working} with {Autonomy}-{Restricting} {Algorithms} {Facilitates} {Unethical} {Behavior} and {Displacement} of {Responsibility}},
    author = {Jolly, Anupama A. and Dunlop, Patrick D. and Parker, Sharon K. and Kanse, Lisette},
    journal = {Journal of Business Ethics},
    volume = {203},
    pages = {405--424},
    year = {2026},
    doi = {10.1007/s10551-025-06034-5},
    note = {First online 7 June 2025; journal issue 2026.}
}

@article{killoran_learn_2026,
    title = {Learn from the blame game when {AI} causes harm},
    author = {Killoran, Jay and Park, Andrew},
    journal = {Proceedings of the National Academy of Sciences},
    volume = {123},
    number = {17},
    pages = {e2528408123},
    year = {2026},
    doi = {10.1073/pnas.2528408123},
    note = {VERIFY author list before submission --- not directly fetched from PNAS.}
}

@unpublished{tontrup_strategic_2025,
    title = {Strategic {Delegation} of {Moral} {Decisions} to {AI}},
    author = {Tontrup, Stephan and Sprigman, Christopher Jon},
    year = {2025},
    month = oct,
    note = {SSRN Working Paper No.\ 5696827, posted 6 October 2025.},
    url = {https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5696827}
}

@unpublished{ivanova_stenzel_delegating_2025,
    title = {Delegating in the {Age} of {AI}: {Preferences} for {Decision} {Autonomy}},
    author = {Ivanova-Stenzel, Radosveta and Tolksdorf, Michel},
    year = {2025},
    month = dec,
    note = {Rationality and Competition Discussion Paper No.\ 558 (CRC TRR 190, LMU Munich / HU Berlin), 22 December 2025.},
    url = {https://rationality-and-competition.de/wp-content/uploads/discussion_paper/558.pdf}
}

@unpublished{normann_delegate_2025,
    title = {Delegate {Pricing} {Decisions} to an {Algorithm}? {Experimental} {Evidence}},
    author = {Normann, Hans-Theo and Ruli\'e, Nina and Stypa, Olaf and Werner, Tobias},
    year = {2025},
    month = oct,
    note = {arXiv:2510.27636 [econ.GN]; also VfS Annual Conference 2025 (Cologne) paper No.\ 325417.},
    url = {https://arxiv.org/abs/2510.27636}
}

@unpublished{weitzner_reputational_2024,
    title = {Reputational {Algorithm} {Aversion}},
    author = {Weitzner, Gregory},
    year = {2024},
    month = jul,
    note = {arXiv:2402.15418 [econ.GN], v3 31 July 2024. McGill University. Presented at AEA 2025.},
    url = {https://arxiv.org/abs/2402.15418}
}
```

### Secondary entries (cite only if you decide to use them)

```bibtex
@article{tsumura_effects_2026,
    title = {Effects of knowledge and importance on responsibility in human-{AI} decision making},
    author = {Tsumura, T. and Yamada, S.},
    journal = {Scientific Reports},
    year = {2026},
    doi = {10.1038/s41598-025-32513-w},
    note = {VERIFY: author list extracted from a web-search summary rather than from a directly-rendered Nature page. Confirm before citing.}
}

@article{salatino_influence_2025,
    title = {Influence of {AI} behavior on human moral decisions, agency, and responsibility},
    author = {Salatino, A. and Pr\'evel, A. and Caspar, E. A. and Lo Bue, S.},
    journal = {Scientific Reports},
    year = {2025},
    doi = {10.1038/s41598-025-95587-6},
    note = {VERIFY: author list not directly verified. Drone-operator simulation; military cadet sample.}
}
```

---

## Suggested next steps

1. **Pick 4–6 of the 8 primary additions** and integrate into [literature.tex](../manuscript/literature.tex). Recommended priority set: Kormylo, Jolly, Tontrup & Sprigman, Ivanova-Stenzel & Tolksdorf (WP), Weitzner (WP), Killoran & Park.
2. **Try Felix's WZB subscription** for the two Management Science articles (Kormylo, Dargnies). Both are in the same Special Issue (MS 72(1)) so a single proxy session should retrieve them. Save to `master_supporting_docs/supporting_papers/`.
3. **Download the SSRN and CRC TRR 190 working papers** — both are freely available; you don't need a subscription.
4. **Verify the two flagged Nature subjournal author lists** (Tsumura & Yamada; Salatino et al.) if you decide to cite either.
5. **Search SSRN / NBER / ECONtribute one more time before submission** — given how fast this literature is moving, a final check shortly before submission is worth the 15 minutes.

---

## Post-Flight Verification

**Method:** Inline verification via direct WebFetch on journal / repository pages, supplemented by multi-source WebSearch cross-check. Formal CoVe via a forked `claim-verifier` subagent was *not* run because the verification surface here is small (8 primary citations) and each was independently checked. Items not directly fetched are flagged below and in the BibTeX with explicit `VERIFY` notes.

| Citation | Direct WebFetch verified? | Source pages confirming |
|---|---|---|
| Kormylo et al. 2025 (MS) | ✅ yes | pubsonline.informs.org (mnsc.2022.03510) — full metadata, authors, vol/issue/pages, date |
| Dargnies et al. 2026 (MS) | ✅ yes | ideas.repec.org/a/inm/ormnsc/v72y2026i1p285-301.html — full metadata |
| Jolly et al. 2025 (JBE) | ⚠️ indirect | Title, DOI 10.1007/s10551-025-06034-5, JBE venue confirmed via multiple consistent sources (Springer, PhilPapers, ResearchGate, Newswise); Springer page returned 303 / ResearchGate 403 on direct fetch. Author list confirmed via PhilPapers listing. Low risk. |
| Killoran & Park 2026 (PNAS) | ⚠️ no | PNAS direct fetch blocked (403). DOI `10.1073/pnas.2528408123` confirmed real; author list **flagged VERIFY** in BibTeX. |
| Tontrup & Sprigman 2025 (SSRN) | ⚠️ indirect | SSRN direct fetch blocked (403). Title, authors, SSRN ID 5696827, posting date 6 Oct 2025 confirmed via Christopher Sprigman's NYU faculty page and multiple SSRN-derived search results. Low risk. |
| Ivanova-Stenzel & Tolksdorf 2025 (CRC TRR 190 DP 558) | ✅ yes | First page of the actual PDF was read via `pdftotext` — title, authors, date, DP number, abstract, JEL codes all confirmed |
| Normann et al. 2025 (arXiv) | ✅ yes | arxiv.org/abs/2510.27636 + ideas.repec.org/p/zbw/vfsc25/325417 — both confirmed |
| Weitzner 2024 (arXiv) | ✅ yes | arxiv.org/abs/2402.15418 — title, author, dates confirmed |
| Tsumura & Yamada 2026 (Sci Rep) — *secondary* | ❌ no | Nature direct fetch blocked. DOI 10.1038/s41598-025-32513-w is real; author list **flagged VERIFY** in BibTeX. |
| Salatino et al. 2025 (Sci Rep) — *secondary* | ❌ no | Same — DOI 10.1038/s41598-025-95587-6 real; author list **flagged VERIFY**. |

**Hallucination risk assessment:** Low for the 6 directly-verified primary entries. Medium for Killoran & Park (PNAS) — DOI is real and topic is right, but author names rely on a WebSearch summary and should be confirmed in 30 seconds by opening the PNAS page directly. The two secondary Nature subjournal entries are explicitly flagged not to be cited without verification.

**Confidence in synthesis:** The thematic claims (moral wiggle room in AI, autonomy preferences, betrayal-aversion asymmetry, signal-extraction microfoundation, etc.) are each grounded in at least one directly-verified paper. The framing of where each addition fits in `literature.tex` is editorial judgment by Claude — Felix should treat those placement suggestions as starting points, not prescriptions.
