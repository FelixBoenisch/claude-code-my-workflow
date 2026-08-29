# Lens 7 — Citation Audit

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence* (Bönisch, WZB Berlin)
**Date:** 2026-08-21
**Scope:** the seven files `main.tex` actually `\input`s — `abstract.tex`, `introduction.tex`, `literature.tex`, `design.tex`, `results.tex`, `conclusion.tex`, `appendix.tex`. `literature_revised.tex` and `results_pre_restructure_2026-05-06.tex` excluded (not compiled).
**Bibliography validated against:** `manuscript/ProjectAlgorithm.bib` (106 entries).
**Build artifacts inspected:** `main.blg`, `main.log`, `main.aux`, `main.bbl`, `bibtex.stdout`.

---

## Headline counts

| Severity | Count |
|---|---|
| CRITICAL | 2 |
| MAJOR | 9 |
| MINOR | 13 |
| **Total** | **24** |

**Structural health is good.** Every citation key in the compiled manuscript resolves. `main.blg` (2026-08-20 23:20) reports 66 entries used and **zero warnings**; `main.log` (23:44) contains **no** `Citation ... undefined`, no `!` errors, and no unset-Unicode errors. The two keys that failed in the stale `bibtex.stdout` (2026-07-07) — `filiz_reducing_2021`, `jung_towards_2021` — have since been added and now resolve.

**Semantic health is better than average for a paper at this stage.** I independently verified the actual findings of 13 of the load-bearing works against primary or publisher sources. Eleven check out cleanly. The problems cluster in three places: (i) two adjacent sentences in `literature.tex` that assert opposite things about algorithm transparency, (ii) a handful of overstatements around `steffel_passing_2016`, `tontrup_strategic_2025`, `chevrier_algorithm_2024` and `gogoll_rage_2018`, and (iii) coverage gaps where the *most* on-point precedent is already sitting in the author's own `.bib` file, uncited.

---

## 1. Structural validation

### 1.1 Key resolution — clean

| Check | Result |
|---|---|
| Unique keys cited in compiled text | 66 |
| Keys unresolved in `ProjectAlgorithm.bib` | **0** |
| BibTeX warnings in `main.blg` | **0** |
| `Citation undefined` in `main.log` | **0** |
| Duplicate entries (by DOI) | **0** |
| Entries missing a `year` field | **0** |

One key, `kirchkamp_sharing_2019`, appears in a `\citet{}` in `introduction.tex:26` but that entire line is LaTeX-commented (`%`), so it never reaches the `.aux`. See MAJOR-8.

### CRITICAL-1 — The documented "single source of truth" bibliography is an empty template

`CLAUDE.md:31` documents the repo layout as:

```
├── Bibliography_base.bib        # Central bibliography (single source)
```

and `CLAUDE.md:129` documents `/validate-bib` as "Cross-reference all citations against `Bibliography_base.bib`".

`Bibliography_base.bib` (repo root) contains **two dummy entries** and nothing else:

> `@book{Example2024_book, author = {Lastname, Firstname}, title = {An Example Book Title}, ...`
> `@article{Example2025_article, author = {Lastname, Firstname and Coauthor, Name}, ...`

Meanwhile `main.tex` compiles `\bibliography{ProjectAlgorithm}` against `manuscript/ProjectAlgorithm.bib`. The two files share **zero** real entries, so there is no disagreement to adjudicate — the documented central bibliography is simply unpopulated and unused.

Consequences: (a) any `/validate-bib` run as documented would report all 66 citations as unresolved and produce a false negative or a wasted revision cycle; (b) the file that will ship in the replication package as "the bibliography" is a template; (c) a contributor following `CLAUDE.md` would add references to a file the paper does not read. Either point `CLAUDE.md` and `/validate-bib` at `manuscript/ProjectAlgorithm.bib`, or delete `Bibliography_base.bib`. `WORKFLOW.md:79`/`:198` already correctly names `ProjectAlgorithm.bib`, so the two governance documents disagree with each other.

### CRITICAL-2 — A fabrication-flagged entry and five unresolved `VERIFY` flags ship inside the submission bibliography

`ProjectAlgorithm.bib:360-366`:

```bibtex
@article{stein_dont_2020,
    title = {{[NOT FOUND]} {Don't} {Let} {Me} {Down}: {The} {Role} of {Algorithmic} {Complexity} in {Algorithm} {Aversion}},
    journal = {Working Paper},
    author = {Stein, Jens-Peter and others},
    year = {2020},
    annote = {VERIFY: claim-verifier could not locate this paper in any indexed database. Title and authors may be partially fabricated by an earlier session. ...},
}
```

The literal string `[NOT FOUND]` is inside the `title` field, and the `annote` records that the entry may be **partially fabricated by an automated session**. The key is currently uncited, so nothing prints — but one `\cite{stein_dont_2020}` would place a fabricated reference into an AER/QJE/JPE reference list. Delete it, or replace with the verified alternative the annote itself proposes (`castelo_task-dependent_2019`, already in the bib and already cited).

The bib also carries **13 entries with unresolved `VERIFY`/`CONFIRM` annotes**, of which **five are cited in the compiled paper**:

| Key | Line | Unresolved flag | Cited at |
|---|---|---|---|
| `european_union_ai_act_2024` | 537 | "VERIFY citation form" | `introduction.tex:3`, `:26` |
| `sunstein_anatomy_2024` | 1101 | "VERIFY volume/pages against the published issue" | `literature.tex:26` |
| `bigman_algorithmic_2023` | 1057 | "VERIFY middle author spellings against the APA page" | `literature.tex:28` |
| `lemley_remedies_2019` | 1236 | "CONFIRM page range against the journal listing" | `introduction.tex:3` |
| `buiten_law_2023` | 1247 | "CONFIRM volume and article number" | `introduction.tex:3` |

Uncited but flagged: `goldbach_geht_2019` (annote states the originally-listed German title could not be located and a *different* paper was substituted), `kurtzberg_attribution_2004` (author order reversed and title changed), `liu_when_2021` (co-author "Du Yu" not found in any indexed publication), `pezzo_pezzo_physician_2006`, `killoran_learn_2026` ("author list extracted from web-search summary; PNAS page not directly fetched"), `jones_have_1989`, `schotter_bargaining_2000`, `huck_strategic_2004`.

These are the residue of an automated rewrite pass (`ProjectAlgorithm.bib:302-305`: *"All entries below are placeholders --- VERIFY before submission"*). All five cited ones must be verified before submission; the uncited flagged ones should be verified or removed.

### 1.2 Unused entries — MINOR-12

40 of 106 entries are never cited. Most are harmless inventory, but several are substantive omissions rather than surplus (see §4). Full list:

`argenton_potters_yang_2023`, `ariely_large_2009`, `benabou_identity_2011`, `blunden_downside_2023`, `bockstedt_humans_2025`, `candrian_rise_2022`, `charness_attribution_2004`, `de_quidt_measuring_2018`, `dohmen_professionals_2008`, `falk_morals_2013`, `freisinger_decoding_2024`, `garofalo_shifting_2018`, `gawn_machiavelli_2021`, `germann_algorithm_2023`, `goldbach_geht_2019`, `heaton_social_2023`, `holzmeister_delegation_2023`, `huck_strategic_2004`, `jolly_not_2025`, `jones_have_1989`, `killoran_learn_2026`, `kirchkamp_sharing_2019`, `kormylo_till_2025`, `kurtzberg_attribution_2004`, `liu_when_2021`, `maasland_blame_2022`, `maximiano_gift_2013`, `newman_eliminating_2020`, `niszczota_robo-investors_2020`, `pezzo_pezzo_physician_2006`, `prolific`, `rogoff_optimal_1985`, `salatino_influence_2025`, `schotter_bargaining_2000`, `sharan_dont_2020`, `stein_dont_2020`, `trunk_current_2020`, `tsumura_effects_2026`, `vickers_delegation_1985`, `weitzner_reputational_2024`.

### MAJOR-11 — `bartling_shifting_2012` prints with initials while every other entry prints full first names

`ProjectAlgorithm.bib:33`:

```bibtex
author = {Bartling, B. and Fischbacher, U.},
```

`main.bbl:32` therefore renders:

> **Bartling, B. and U.~Fischbacher**, "Shifting the {Blame}: {On} {Delegation} and {Responsibility},"

against, three entries later, `main.bbl:38`:

> **Bartling, Bj\"orn, Urs Fischbacher, and Simeon Schudy**, "Pivotality and responsibility attribution in sequential voting,"

This is the paper's **second most-cited work** (14 citation instances) and the anchor of the whole responsibility-shifting strand. It is the only entry in the bibliography formatted with initials. Fix to `{Bartling, Bj\"orn and Fischbacher, Urs}`.

### 1.3 Field completeness — MINOR-14

Cited entries with incomplete metadata:

- `arnestad_manual_2024` (line 1145) — no `pages`, no `doi`. *Cognition* 252 has an article number.
- `allen_algorithm_2022` (line 1153) — no `doi`.
- `gawn_lying_2019` (line 921), `kandul_do_2018` (line 940), `maximiano_gift_2013`, `dawes_robust_1979` — no `doi`.
- `tacconelli_how_2026` (line 1163) — no `volume`/`pages`; annote correctly notes "add volume/pages at proof stage".
- `feier_hiding_2022` — `pages = {19}` (article number). `main.bbl:184` renders this as `{\it 28} (2), 19.`, which reads like a single-page article. Acceptable for *Sci Eng Ethics* but worth a look at proof stage.

### MINOR-16 — Non-ASCII hyphen inside a printed author name

`ProjectAlgorithm.bib:173`: `author = {Burton, Jason W. and Stein, Mari‐Klara and Jensen, Tina Blegind}` — "Mari‐Klara" uses U+2010 HYPHEN, not ASCII `-`. It survives compilation under MiKTeX's `inputenc` and prints into `main.bbl:92`, but it is a portability hazard on other TeX distributions and should be normalised. Several `abstract` fields (unused by `aer.bst`) also carry U+2010, U+2014, U+2019 and `×`.

---

## 2. Semantic / cite-claim direction

I selected the 13 most load-bearing works by citation count and by the weight of the claim they carry, and checked each against a primary or publisher source. **Verification status is stated explicitly for each.**

### 2.1 Verified accurate — no action needed

**`feier_hiding_2022` (21 citation instances — the paper's anchor).** Verified in full against the *Science and Engineering Ethics* text (PMC8979930) and the arXiv working-paper version. Every substantive characterisation in the manuscript is correct:

| Manuscript claim | Location | Source | Verdict |
|---|---|---|---|
| "her own performance in a Raven-style logic task" | `literature.tex:32` | Ten pattern-sequence puzzles in 5 min; missing fourth pattern from four alternatives | ✅ |
| "after good outcomes delegated and self-made decisions are rewarded alike in both treatments" | `literature.tex:32` | No human/machine difference for good outcomes | ✅ |
| "After bad outcomes, decisions delegated to the algorithm, but not ... to another human, are rewarded more generously than self-made ones" | `literature.tex:32` | Machine: 8.53 (non-deleg.) vs 12.96 (deleg.), *p*=0.041. Human: 7.29 vs 8.26, n.s. | ✅ |
| "their algorithm is calibrated at the session level" | `literature.tex:34` | "The algorithm was programmed to mirror the performance of the human participants in the room" | ✅ |
| "the same subject acts as both delegator and evaluator" | `literature.tex:34` | Confirmed; strategy method over four scenarios | ✅ |
| "the propensity to delegate is driven primarily by beliefs about task performance, not by the type of delegate" (fn.) | `literature.tex:34` | Self-assessed errors *p*<0.001; agent type *p*=0.376 | ✅ |
| "delegation rates are similar for human and algorithmic intermediaries" | `design.tex:96` | 46.1% vs 56.2%, χ² *p*=0.28 | ✅ (but see MINOR-24) |
| "decision-makers are rewarded less when a negative outcome is directly attributable to their own action" | `design.tex:102` | ✅ | ✅ |

I also confirm that **Feier et al. contains no self-serving motive** — the delegate's outcome affects the third party's payment, not the delegator's own earnings. The manuscript nowhere frames it as the canonical unfair-choice-with-machines paper, and `results.tex:70` and `design.tex:64` explicitly and correctly place the "no self-serving choice to police" feature as a *departure* of this paper from the dictator-game strand. **No finding raised** (per settled decision).

**`oexl_shifting_2013`** — `literature.tex:7`: *"Punishment lands on the intermediary even when delegation itself has eliminated the fair option, leaving him only the choice between two unfair allocations."* Verified: the published finding is that an intermediary given the choice between two unfair outcomes is punished *more* than when the dictator chooses one directly, despite being powerless. ✅

**`coffman_intermediation_2011`** — `literature.tex:7`: *"The principal escapes punishment even when the intermediary remains completely passive, but not when the principal continues to interact with the recipient directly."* Verified against the AEJ:Micro abstract and secondary sources: punishment falls for completely passive intermediaries, and the driver is that "moral decision making is ... predicted by the fairness of the consequences that follow directly." ✅

**`gawn_lying_2019`** — `literature.tex:9`: *"Principals pay agents to lie on their behalf and deceive more readily through a delegate than directly."* Verified: the paper's stated main finding is "subjects are more willing to lie through a delegate than to lie directly." ✅ (The interrogative title invites the opposite reading; the manuscript gets the direction right.)

**`freer_friedman_weidenholzer_2024`** — `literature.tex:9`: *"a substantial fraction of investors delegate even purely luck-based lottery choices, in which alternative motives such as decision costs, performance-chasing, or risk tolerance cannot rationalize the choice."* Verified against the arXiv abstract: "a surprisingly large fraction of investors delegate even trivial choice tasks, suggesting a major role for the blame shifting motive"; decision costs and performance-chasing operate on *other* margins; the risk-acceptability motive is explicitly ruled out. ✅ Precise and well-framed.

**`shank_attributions_2019`** — `literature.tex:28`: *"humans who merely monitor an algorithm blamed less than humans who decide alone."* Verified: "humans who monitor AIs are faulted less than solo humans and humans receiving recommendations." ✅

**`normann_delegate_2025`** — `literature.tex:17`: *"experimental firms likewise delegate pricing more often when they can override the algorithm."* Verified against the arXiv abstract: "Participants delegate more when they can override the algorithm's decisions." ✅

**`dargnies_aversion_2026`** — `literature.tex:17`: *"explanations of how the algorithm works leave acceptance unchanged."* Verified: "Providing details on how the algorithm works does not increase the preference for the algorithm for workers or for managers." ✅

**`jung_towards_2021`** — `literature.tex:17`: *"reliance on algorithms increases ... under time pressure."* Verified: the mitigation of aversion "is based on forecasters' loss of confidence in their own forecast when they are under time pressure." ✅

**`gogoll_rage_2018` (7 instances) — the factual claims.** `literature.tex:26`: *"document this in an incentivized calculation task with performance uncertainty."* Verified: the task is a purely mathematical implementation, and subjects were shown past performances of 24 subjects from a preparatory session alongside the algorithm's, so performance uncertainty is present and calibration is population-level. ✅ `results.tex:74`'s claim that *"observers view the delegation of morally consequential decisions to machines relatively critically"* is directly supported by the abstract: "observers judge such delegations in relatively critical light." ✅

**`litterscheidt_financial_2020`** — `literature.tex:17`: *"aversion is stronger when the algorithm ... remains a black box to its users."* Individually accurate: the paper finds investors delegate more when given detailed information on the robo-advisor's underlying investment principles. ✅ — but see MAJOR-3.

### MAJOR-3 — `literature.tex:17` asserts two directly opposite things about algorithm transparency, two sentences apart

> "aversion is stronger when the algorithm cannot be observed to learn from its mistakes \citep{berger_watch_2021} or **remains a black box to its users** \citep{litterscheidt_financial_2020}. Evidence about relative performance gathered through experience and feedback reduces aversion \citep{filiz_reducing_2021}, whereas **explanations of how the algorithm works leave acceptance unchanged** \citep{dargnies_aversion_2026}."

Both citations are individually faithful, and that is exactly the problem. Litterscheidt & Streich find that *explaining the algorithm's investment principles raises delegation*; Dargnies, Hakimov & Kübler find that *providing details on how the algorithm works does not raise preference for it*. Placed one sentence apart with a bare "whereas", the passage reads as if the second finding refines the first, when the two are in genuine empirical tension. A referee who knows either paper will stop here. Either (a) mark the tension explicitly and note the domain difference (retail investing vs. hiring), or (b) drop the `litterscheidt_financial_2020` clause, since the black-box framing is not needed for the paragraph's argument.

### MAJOR-4 — `steffel_passing_2016` miscited as an instance of blame operationalised through costly punishment

`design.tex:84`:

> "We focus on punishment rather than reward because the responsibility-attribution literature has predominantly operationalized blame through punishment~\citep{bartling_shifting_2012,coffman_intermediation_2011,steffel_passing_2016}."

Verified: Steffel, Williams & Perrmann-Graham (2016, *OBHDP*) run hypothetical-scenario studies (business decisions, hotel reservations, meal orders) with rating-scale measures of responsibility and blame. There is **no costly-punishment stage anywhere in the paper**. It cannot support the sentence it is attached to. Bartling & Fischbacher and Coffman do, and are sufficient. Drop `steffel_passing_2016` from this list.

### MAJOR-5 — `steffel_passing_2016`'s actual finding anticipates this paper's headline reversal and goes unmentioned

Steffel et al. also report that people **delegate to other people but not to inanimate objects or chance**. The manuscript cites the paper three times (`introduction.tex:26` [commented], `design.tex:84`, `design.tex:90`) and lists it among the works grounding Hypothesis 1 — the hypothesis that the paper then *rejects with a significant reversal*.

This is the highest-value substantive gap in the whole citation set. A paper already in the citation list contains a prior finding pointing in the direction of the paper's own result, and the manuscript treats it as supporting the opposite prediction. The `design.tex:88-96` hypothesis-development passage should engage it: Steffel et al. supply an existing reason to expect that a non-intentional delegate does *not* attract responsibility-motivated delegation, which strengthens rather than weakens the paper's contribution.

### MAJOR-6 — Ambiguous, possibly reversed characterisation of the Bartling & Fischbacher randomisation-device result

Two live statements about the same result:

`literature.tex:7`:
> "randomization devices provide the principal weaker cover than deciding humans \citep{bartling_shifting_2012, oexl_shifting_2013} and **attract correspondingly less delegation** \citep{bartling_shifting_2012}."

`design.tex:96`:
> "\citet{bartling_shifting_2012} also show that subjects are **more likely to delegate** morally consequential decisions **even to a die roll**, an early form of delegation to a non-intentional agent, suggesting that responsibility avoidance persists when the agent lacks intentionality."

I verified the design: Bartling & Fischbacher run a four-player dictator variant (one A, one B, two Cs; fair = 5/5/5/5, unfair = 9/9/1/1) and include a "treatment random" in which A can delegate to a computerised random device (die) that selects the unfair allocation with probability 0.4, and cannot delegate to B. I could **not** retrieve the treatment-level delegation percentages — the working-paper PDFs at TWI Kreuzlingen, KOPS Konstanz and ZORA all returned unparseable binary or an access-denied page. **Stated explicitly: the numerical comparison is unverified.**

Regardless of the numbers, the two sentences as written pull in opposite directions and `design.tex:96` has no comparator ("more likely" than *what*?). Because `design.tex:96` sits inside the passage that motivates Hypothesis 1 — the hypothesis the paper rejects — this is load-bearing. Rewrite `design.tex:96` with an explicit comparator ("delegate to the random device at non-trivial rates, though less often than to a human intermediary") so it cannot be read as contradicting `literature.tex:7`.

### MAJOR-7 — `tontrup_strategic_2025`: "outside observers" claim unsupported, and the transfer result is a within-delegator comparison

`literature.tex:30`:

> "In a similar setting, \citet{tontrup_strategic_2025} let dictators hand the execution of their transfer to a large language model. **Transfers fall when this option is available**, and dictators **as well as outside observers** attribute part of the responsibility to the machine."

Verified against the NYU Engelberg output page for the paper (SSRN itself returns 403). The design is confirmed: a $10 dictator game where treated Allocators can involve ChatGPT at a time cost, against a "non-agentive computer program" control; about 35% involve the AI. Two problems:

1. The reported result is **"Allocators who involved the AI transferred significantly less money to the Recipient"** — a comparison *between delegators and non-delegators within the treatment*, not a treatment-level fall in mean transfers when the option is available. Prosocial individuals were *more* likely to involve the AI, so the composition matters. "Transfers fall when this option is available" overstates it.
2. I found **no evidence of an outside-observer / third-party attribution measure** in this paper. The reported attribution result is that "Allocators who attributed more responsibility to the AI were also more likely to involve the AI" — the Allocator's own attribution, correlational. **Stated explicitly: I could not verify any outside-observer measure and believe the clause is incorrect.** Either verify it against the SSRN PDF or delete "as well as outside observers".

### MAJOR-10 — `chevrier_algorithm_2024` mischaracterised: the paper's subject is the programmer, and there are two distinct algorithm types

`literature.tex:30`:

> "\citet{chevrier_algorithm_2024} extend the canonical dictator game of \citet{bartling_shifting_2012} with an algorithmic intermediary. As with a human intermediary, the dictator who delegates an inegalitarian allocation faces lower expected punishment than the dictator who chooses it herself. **Delegation to the algorithm makes recipients less likely to punish at all, although the delegator is punished more harshly than under a human intermediary when punishment does occur.** Delegation rates in their design nevertheless do not differ between human and algorithmic intermediaries."

Verified abstract: *"The intermediary can be a human, a rule-based algorithm (RA), or an artificial intelligence algorithm (AI) ... Behind these algorithms, a programmer fully controls the decisions of the RA and partially controls the decisions of the AI. We find that participants delegate regardless of the type of intermediary. While human intermediaries and RA programmers are perceived as more responsible for inegalitarian decisions, the delegator is perceived as less responsible. AI programmers and the delegator are not perceived as responsible for the inegalitarian allocations made by the AI. This allows AI programmers to exploit the moral wiggle room and select inegalitarian allocations more frequently."*

Three issues:
- The manuscript collapses **two distinct algorithmic intermediaries** (rule-based vs. AI) into one, and the abstract's central contrast is precisely between them: for RA the *programmer* absorbs responsibility, for AI responsibility lands on *nobody*.
- The paper's headline — that the responsibility travels to the **programmer**, and that AI programmers exploit the resulting wiggle room — is omitted entirely from the live text. (It appears only in the commented-out `results.tex:175`, which correctly identifies "the programr [sic] behind the algorithm" as the paper's margin.) That headline is directly relevant to the regulatory framing in `introduction.tex:3`.
- **Stated explicitly: I could not verify the extensive/intensive-margin decomposition** ("less likely to punish at all ... punished more harshly ... when punishment does occur"). It is not in the abstract, and the GREDEG PDF server refused the connection. Given that the manuscript's own `results.tex:60` reports an extensive-margin analysis, this attributed decomposition is doing comparative work and must be checked against the working paper.

### MAJOR-9 (attribution) — "coined the *moral* domain"

`design.tex:90`:

> "These strands of the literature mostly focus on what \citet{gogoll_rage_2018} have **coined** the \textit{moral} domain."

Gogoll & Uhl's title is "Automation in the moral domain" and they use the term, but "the moral domain" is long-standing vocabulary in moral psychology and did not originate with them. The manuscript's own `literature.tex:26` gets this right — "sometimes called the \textit{moral domain} \citep{gogoll_rage_2018}" — so the two passages are also internally inconsistent. Change `design.tex:90` to match `literature.tex:26`.

### 2.2 Verified with minor caveats

**`hamman_self-interest_2010` (6 instances)** — `literature.tex:7`: *"principals' transfers to recipients fall sharply under delegation even without any punishment opportunity, and that principals report feeling less responsible for the resulting allocations."* The first clause is confirmed by the AER abstract ("recipients receive significantly less, and in many cases close to nothing, when allocation decisions are made by agents"). The felt-responsibility clause is consistent with how the paper is universally cited and with the secondary literature ("perceived responsibility as well as blame and punishment are reliably diminished"), but I did not open the paper's questionnaire section. **Stated explicitly: partially verified.**

**`hill_does_2015`** — `literature.tex:9`: *"Observers rate delegating legislatures as less blameworthy, and do so even when the delegate is powerless to change the outcome."* The "powerless intermediary" half is confirmed verbatim by the JELS abstract. **Stated explicitly: I could not verify the "legislatures" detail of the vignette** from the abstract or available secondary sources. Confirm the stimulus domain before submission.

**`tobia_when_2021` + `tacconelli_how_2026`** — `literature.tex:28` attributes to the pair: *"judged less harshly, and face lower legal exposure ... among lay and expert evaluators alike."* The expert-evaluator component comes only from Tacconelli et al. (248 German physicians, per the bib annote); Tobia, Nielsen & Stremitzer (2021) use lay mock-juror samples. The joint "alike" is defensible only because Tacconelli covers both. MINOR-20 below.

**`kobis_delegation_2025`** — `introduction.tex:5` (*"makes dishonesty easier by obscuring intent"*) and `literature.tex:30` (*"delegation to algorithms increases dishonest behaviour"*). The second is the paper's title. The first is a reasonable gloss of the interface-ambiguity mechanism. ✅

**`hueholt_trusting_2026`** — `literature.tex:30`: *"in an incentivized donation choice with real moral stakes ... subjects delegate to an AI more often than to a human counterpart and feel less responsible when they do."* The first half is confirmed (two experiments, N=5,639; individuals facing a real-life moral decision delegate significantly more often to AI than to a human). The "feel less responsible" half is consistent with the paper's framing ("responsibility shifting ... extends to AI delegates") but **stated explicitly: not directly verified** as a measured outcome.

---

## 3. Style consistency

**`\citet` vs `\citep` — clean.** I checked all 66 live citation instances. Textual `\citet` is used wherever the author is the grammatical subject (`\citet{bartling_shifting_2012} provide the canonical experimental evidence`; `\citet{feier_hiding_2022} report that...`), parenthetical `\citep` wherever the citation is an aside or a list (`\citep{bartling_shifting_2012, hamman_self-interest_2010, ...}`). `\citep[e.g.,][]{...}` is used correctly at `conclusion.tex:6` and `results.tex:74`. **No misuse found.**

**Duplicate entries under different keys — none found.** No duplicate DOIs. The apparently duplicated titles in a naive scan (`shifting the blame`, `hiding behind`, `blame the machine`) are prefix collisions between genuinely distinct works.

### MINOR-13 — Same journal issue, three different years

`bockstedt_humans_2025` (MS **72(1)**, 323–342, `year = {2025}`), `kormylo_till_2025` (MS **72(1)**, 343–367, `year = {2025}`) and `dargnies_aversion_2026` (MS **72(1)**, 285–301, `year = {2026}`) are all in the same *Management Science* Special Issue on the Human-Algorithm Connection. I verified that issue is dated **January 2026**, so `dargnies_aversion_2026` is the correct one and the other two are misdated. Only `dargnies` is cited, so nothing prints wrong today — but the inconsistency will bite if the others are ever cited.

### MINOR-15 — Prolific cited as a bare inline URL while a `prolific` bib entry sits unused

`design.tex:3`:
> "We ran an online experiment via the British platform Prolific (https://www.prolific.com) with UK participants."

The URL is neither `\url{}`-wrapped (so it will not line-break and is not hyperlinked despite `hyperref` being loaded) nor routed through the `prolific` entry that already exists at `ProjectAlgorithm.bib:1107` with Prolific's own recommended citation form. Use `\citep{prolific}` or at minimum `\url{}`.

### MINOR-17 — "systematic reviews" applied to a meta-analysis and a narrative survey

`literature.tex:15`:
> "\citet{burton_systematic_2020}, \citet{mahmud_what_2022}, \citet{chugunova_we_2022}, \citet{qin_ai_2025} and \citet{irlenbusch_human_2026} provide **systematic reviews** of this literature."

`burton_systematic_2020` and `mahmud_what_2022` are systematic reviews. `chugunova_we_2022` self-describes as an "interdisciplinary review"; `qin_ai_2025` is a **meta-analytic** review (*Psych Bulletin*); `irlenbusch_human_2026` is an ECONtribute discussion-paper survey. "Reviews and meta-analyses" would be accurate.

### MINOR-18 — Feier's calibration described two ways

`literature.tex:34` says "calibrated at the **session** level"; `results.tex:129` says "matched to the distribution of human performance at the **population** level". Both gloss the same fact ("mirror the performance of the human participants in the room"), but a referee reading both will pause. Pick one term.

### MINOR-19 — Large commented-out blocks carrying citations

`introduction.tex` lines 11–12, 24 and 26, and `results.tex` lines 165–203, are dead prose containing ~20 citation instances plus a `\todo[inline]`, unresolved `\hl{}` queries (`conclusion.tex:2`, `literature.tex:23-24`, `results.tex:76`, `results.tex:101`), and a to-do list with 17 open analysis items. `introduction.tex:26` in particular is a complete alternative contribution paragraph. `results.tex:169` still contains `\cite{feier_hiding_2022}` inside an un-run `\todo` for a power analysis. None of this compiles, but all of it ships in the source and the replication package. Strip before submission.

### MINOR-21 — Appendix has zero citations

`appendix.tex` reports preregistration deviations, sample construction, a CONSORT diagram and regression specifications with no citation anywhere — not for the preregistration platform, not for the estimator choices, not for the attention-check or attrition conventions. `quality_reports/logit_vs_probit_delegation.md` and `extensive_margin_probit.md` exist in the repo, suggesting the methodological choices were deliberated; the appendix should cite the standards it follows.

### MINOR-22 — Stale `bibtex.stdout`

`manuscript/bibtex.stdout` (2026-07-07) still records the two now-resolved missing keys. Harmless, but it is the artifact a reader would check first; it should be regenerated or gitignored alongside the other build products.

### MINOR-23 — Feier's task is not "purely mathematical"

`design.tex:64`:
> "In contrast, subjects may be skeptical that an algorithm could ever fail in purely mathematical tasks~\citep{gogoll_rage_2018,feier_hiding_2022}."

Gogoll & Uhl's task is a purely mathematical implementation ✅. Feier et al.'s is a **Raven-style pattern/logic puzzle** — which the manuscript itself correctly describes at `literature.tex:32`. Drop `feier_hiding_2022` from this parenthesis, or widen the phrase to "purely mathematical or logical tasks".

### MINOR-24 — "similar" delegation rates understates a 10 pp difference

`design.tex:96`: *"\citet{feier_hiding_2022} report that delegation rates are similar for human and algorithmic intermediaries."* The actual figures are 46.1% (35/76) vs 56.2% (41/73), *p*=0.28 — a 10 pp point difference in the direction of *more* algorithmic delegation, statistically indistinguishable in a 149-subject sample. "Statistically indistinguishable" is more honest than "similar" and costs nothing, especially since the manuscript's own contribution rests on a 16.8 pp difference in a 322-subject sample.

---

## 4. Coverage

The striking pattern here is that the most important missing engagements are **already in `ProjectAlgorithm.bib`, uncited**. These were evidently gathered during the lit-review passes (`quality_reports/lit_review_recent_algorithm_responsibility.md`, `lit_review_algorithms_responsibility.md`) and then not carried into the compiled draft.

### MAJOR-8 — Kirchkamp & Strobel (2019) is flagged as a TODO in the live source and still absent

`literature.tex:24` contains a live, un-actioned comment:

> `%\hl{We should cite Kirchkamp and Strobel, even though it is not about delegation}`

`kirchkamp_sharing_2019` is in the bib (line 249), is cited in the non-compiled `literature_revised.tex:41`, and appears in the commented-out contribution paragraph at `introduction.tex:26` — where the paper's contribution is framed as *"we build on \citet{feier_hiding_2022} and \citet{kirchkamp_sharing_2019}"*. It appears **nowhere in the compiled paper**.

This matters more than a housekeeping oversight. Kirchkamp & Strobel, "Sharing responsibility with a machine" (*JBEE* 80, 2019), finds **no significant difference in felt responsibility between human–computer and human–human teams** — a null that runs parallel to this paper's Result 2 (recipients punish delegated and self-made predictions alike). It is the closest prior null in the literature and it *supports* the manuscript. Section 3 (`literature.tex:28-30`) currently presents the incentivized strand as uniformly finding that "algorithmic intermediaries can serve as moral cover", with only `ismagilova_aint_2025` on the other side. Kirchkamp & Strobel belongs beside it.

### MAJOR-9 (coverage) — Four further in-bib, uncited works that each bear on a specific live claim

| Missing work | Bib key (uncited) | The claim it bears on |
|---|---|---|
| **Maasland & Weißmüller (2022), *Front. Psych.*, "Blame the Machine?"** | `maasland_blame_2022` | Their stated conclusion — *"Respondents' aversion to algorithms dominates blame avoidance by delegation"* — is qualitatively **this paper's headline result** in an HR-decision setting. The manuscript claims (`introduction.tex:16`, `literature.tex:36`) to provide "the first direct test" and to be "the first to identify the effect of the prospect of punishment itself." The novelty claim probably survives (Maasland & Weißmüller vary the *unpleasantness of the HR decision*, not the *possibility of punishment*), but it cannot survive **unstated**. A referee who knows this paper will read the novelty claim as overreach. |
| **Blunden & Steffel (2023), *OBHDP*, "The downside of decision delegation: When transferring decision responsibility incurs interpersonal costs"** | `blunden_downside_2023` | This is the direct precedent for `results.tex:145` ("The signaling value of not delegating") and for the conclusion's framing at `conclusion.tex:10` ("what delegating may convey about the person who chooses it"). The paper argues delegation carries interpersonal costs — precisely the mechanism the manuscript proposes and cannot currently anchor in prior work. Its absence makes the mechanism section look speculative when it has a literature. |
| **Argenton, Potters & Yang (2023), *EER*, "Receiving credit: On delegation and responsibility"** | `argenton_potters_yang_2023` | The reward-side companion to Bartling & Fischbacher. `design.tex:84` explicitly justifies *"focus[ing] on punishment rather than reward"* — that sentence needs this citation, and currently supports the choice with `steffel_passing_2016`, which does not use punishment at all (MAJOR-4). Also relevant to Result 2's finding of positive punishment after *good* outcomes under delegation. |
| **Weitzner (2024), "Reputational Algorithm Aversion" (arXiv 2402.15418)** | `weitzner_reputational_2024` | A theory of agents avoiding algorithms for **reputational/signalling** reasons — the exact mechanism at `results.tex:145-147` and `conclusion.tex:8`. The manuscript presents its signalling channel as an ad hoc conjecture ("we cannot test either story and offer them only to show that activation ... is conceivable"). Weitzner gives it a model. |

Lower priority, also in-bib and uncited: `garofalo_shifting_2018` (delegated communication and blame, *Man. Sci.*), `gawn_machiavelli_2021` (delegating selfish vs. generous decisions), `jolly_not_2025` (autonomy-restricting algorithms and displacement of responsibility), `de_quidt_measuring_2018` (relevant to a between-subject manipulation of whether punishment is possible — the manuscript nowhere discusses experimenter demand, which is a natural referee question given that the *No-Punishment* condition still elicits hypothetical punishment beliefs).

### MINOR — Works not in the bib at all worth considering

- **Longoni, Bonezzi & Morewedge (2019), *JCR*, "Resistance to Medical Artificial Intelligence"** — the canonical high-stakes algorithm-aversion paper. `introduction.tex:3` opens with physicians and diagnostic systems and cites nothing empirical for that setting.
- **Dykstra, Exley, Niederle & Wong (2025), "When Decisions Require Consideration, People Give Up Control"** — directly on giving up decision control, relevant to the process-ownership reading at `results.tex:131`.
- **"Blame and praise: responsibility attribution patterns in decision chains" (*Experimental Economics*, 2024)** — responsibility attribution along delegation chains.
- **"Multi-step delegation and the frequency of immoral decisions: Theory and experiment" (*EER*, 2025)** — recent and squarely in the strand-1 literature.

---

## 5. Prioritised fix list

**Before anything else (CRITICAL)**
1. Resolve the `Bibliography_base.bib` / `ProjectAlgorithm.bib` split: repoint `CLAUDE.md:31`, `CLAUDE.md:129` and `/validate-bib` at `manuscript/ProjectAlgorithm.bib`, or delete the empty template.
2. Delete `stein_dont_2020` (fabrication-flagged). Verify the five **cited** `VERIFY`-annoted entries: `european_union_ai_act_2024`, `sunstein_anatomy_2024`, `bigman_algorithmic_2023`, `lemley_remedies_2019`, `buiten_law_2023`.

**Before circulating (MAJOR)**
3. Fix or acknowledge the Litterscheidt/Dargnies contradiction at `literature.tex:17`.
4. Remove `steffel_passing_2016` from the punishment-operationalisation list at `design.tex:84`; add `argenton_potters_yang_2023`.
5. Engage Steffel et al.'s "no delegation to inanimate objects or chance" finding in `design.tex:88-96` — it partly anticipates the paper's reversal.
6. Rewrite `design.tex:96` with an explicit comparator so it stops contradicting `literature.tex:7` on the Bartling die-roll result; retrieve the actual delegation percentages.
7. Delete or verify "as well as outside observers" and soften "transfers fall when this option is available" at `literature.tex:30` (Tontrup & Sprigman).
8. Rework the Chevrier & Teixeira paragraph: distinguish rule-based from AI intermediaries, add the programmer result, and verify the extensive/intensive decomposition against the working paper.
9. Fix `bartling_shifting_2012`'s author field to full first names.
10. Cite `kirchkamp_sharing_2019` (and clear the `literature.tex:24` TODO), `maasland_blame_2022`, `blunden_downside_2023`, `weitzner_reputational_2024`.
11. Change "coined" to "sometimes called" at `design.tex:90`.

**At polish (MINOR)**
12. Items 12–24 above: unused entries, year inconsistency, missing pages/DOIs, the Prolific URL, the U+2010 hyphen, "systematic reviews", session-vs-population wording, commented-out blocks, appendix citations, stale `bibtex.stdout`, the Feier "mathematical task" parenthesis, and "similar" → "statistically indistinguishable".

---

## Verification ledger

**Independently verified against primary/publisher sources (11):** `feier_hiding_2022` (full — PMC + arXiv), `oexl_shifting_2013`, `coffman_intermediation_2011`, `gawn_lying_2019`, `freer_friedman_weidenholzer_2024`, `shank_attributions_2019`, `normann_delegate_2025`, `dargnies_aversion_2026`, `jung_towards_2021`, `gogoll_rage_2018`, `litterscheidt_financial_2020`, `steffel_passing_2016`, `chevrier_algorithm_2024` (abstract only), `tontrup_strategic_2025` (institutional summary only), `hueholt_trusting_2026` (partial).

**Could not verify — stated explicitly:**
- Bartling & Fischbacher treatment-level delegation percentages for the random-device treatment (three PDF hosts returned binary or access-denied).
- Chevrier & Teixeira's extensive/intensive punishment decomposition (GREDEG server refused connection; not in the abstract).
- Tontrup & Sprigman's "outside observers" measure (SSRN 403; absent from the institutional summary — I believe this clause is **incorrect**, not merely unverified).
- Hamman et al.'s felt-responsibility questionnaire result (consistent with universal secondary citation; primary section not opened).
- Hill (2015)'s vignette domain ("legislatures").
- Hüholt & Szech's "feel less responsible" measure.

---

## Score

**6.5 / 10**

The structural layer is genuinely clean — zero unresolved keys, zero BibTeX warnings, zero LaTeX errors, no duplicate entries, correct and consistent `\citet`/`\citep` discipline throughout. That is better than most manuscripts arrive at this stage. The semantic layer is also mostly sound: on the paper's anchor citation, `feier_hiding_2022`, every one of eight distinct characterisations checked out against the published text, including the subtle calibration and dual-role details on which the paper's identification argument rests. That is careful work.

What holds the score down is not sloppiness but incompleteness at exactly the points a top-five referee inspects. Two adjacent sentences in the literature review assert opposite things about algorithm transparency. A paper cited three times to *ground* Hypothesis 1 in fact contains a finding that *anticipates the hypothesis failing*. The bibliography still carries an entry whose title says `[NOT FOUND]` and whose annote admits possible fabrication, alongside five cited entries with unresolved verification flags — in a repository whose own documentation points the validation tool at an empty template file. And the four works that would most strengthen the mechanism section and most sharpen the novelty claim are already sitting in the author's `.bib`, gathered and then never carried into the draft.

None of this is hard to fix, and the fixes mostly make the paper's contribution *stronger* rather than weaker — Kirchkamp & Strobel supports Result 2, Steffel et al. supports the reversal, Blunden & Steffel and Weitzner give the signalling channel a literature it currently lacks. But as it stands, the citation apparatus would not survive a careful referee at AER, QJE or JPE.
