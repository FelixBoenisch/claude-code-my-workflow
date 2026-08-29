# Lens 6 — Prose Quality (Seven-Pass Adversarial Review)

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence*
**Reviewer role:** Academic proofreader / copy-editor, top-five economics journals
**Date:** 2026-08-21
**Files in scope:** `manuscript/abstract.tex`, `introduction.tex`, `literature.tex`, `design.tex`, `results.tex`, `conclusion.tex`, `appendix.tex` (plus one printing artifact in `main.tex`)
**Out of scope (not compiled, not reviewed):** `literature_revised.tex`, `results_pre_restructure_2026-05-06.tex`

**Counts:** 3 CRITICAL · 19 MAJOR · 36 MINOR (58 total)

---

## Executive assessment

The prose is in good shape for a mid-stage draft by a non-native speaker. Active voice dominates, paragraph topic sentences are mostly present and well placed, and the paper is largely free of the classic non-native slips (article errors are rare, subject-verb agreement is clean, tenses are broadly controlled). The house style is well internalised on the one rule that matters most: **the word "gradient" appears nowhere in the compiled manuscript**, and the intended plain phrasing ("the relationship between performance and delegation") is used consistently in `results.tex:112, 129, 135`. The introduction is also correctly lean on statistical caveats.

Three problems keep it from being submission-clean. First, a handful of sentences are genuinely ungrammatical and do not parse (the three CRITICALs). Second, the house ban on colons and em-dashes is violated in four live places, two of them in a single appendix sentence that stacks two em-dashes and a colon. Third, the conclusion drops hedges the results section carries, converting two null results into positive claims.

---

## CRITICAL

### C1 — Ungrammatical clause; the sentence does not parse
**`results.tex:70`**

> With little intent worth sanctioning, any intention-based punishment motive may lose its bite, and **with it does the value** to Player~A of placing an algorithm between herself and the outcome.

"and with it does the value" is not English. The intended reading is that the value of interposing an algorithm falls along with the punishment motive.

**Proposed replacement (house-style compliant):**
> With little intent worth sanctioning, any intention-based punishment motive may lose its bite, and so may the value to Player~A of placing an algorithm between herself and the outcome.

---

### C2 — Ungrammatical verb phrase plus broken parallelism
**`conclusion.tex:8`**

> **Merely signaling to exert additional effort** by retaining the decision would require no measurable effort at all, **but move** delegation only if the prospect of punishment gave the signal value.

Two faults. "Signaling to exert additional effort" is not idiomatic (one signals an *intention* to exert effort, one does not signal *to* exert it). And "would require ... but move" breaks the modal parallel; it must be "but would move".

**Proposed replacement:**
> Signaling an intention to exert additional effort by retaining the decision would require no measurable effort at all, but it would move delegation only if the prospect of punishment gave the signal value.

---

### C3 — Conclusion drops hedges the results section carries; two nulls become positive claims
**`conclusion.tex:10`**

> Nevertheless, we contribute by providing **the first direct test** of whether the prospect of punishment motivates delegation to an algorithm, **and show** that in an environment with inherent task uncertainty and no self-serving choice to police, accountability disciplines algorithm use rather than fueling it. **We also show that delegation cannot shift blame** when the algorithm performs **no better or worse** than the decision-maker ...

Four distinct problems in two sentences.
1. `introduction.tex:16` and `literature.tex:36` both hedge this priority claim ("to our knowledge, the first direct test"). The conclusion drops the hedge. Referees read the conclusion for the claim they will hold you to.
2. "we contribute by providing ... and show" is a parallelism break ("by providing" cannot govern "show").
3. "delegation **cannot** shift blame" is an overclaim from a null. `results.tex:48` reports $p=0.13$ on the bad-outcome gap, and `results.tex:54` reports a *weakly significant* interaction at $p=0.08$ **running in the direction Hypothesis 2 predicted**. A modal-impossibility claim is not supportable from that evidence.
4. "no better or worse" should be "neither better nor worse" (or "no better and no worse").

**Proposed replacement:**
> Nevertheless, we provide what is, to our knowledge, the first direct test of whether the prospect of punishment motivates delegation to an algorithm, and we show that in an environment with inherent task uncertainty and no self-serving choice to police, accountability disciplines algorithm use rather than fueling it. We also find no evidence that delegation shifts blame when the algorithm performs neither better nor worse than the decision-maker, with recipients conditioning their sanctions on the outcome rather than on how the prediction was made.

---

## MAJOR

### House style: colons and em-dashes in running prose

**M1 — `appendix.tex:17` — two em-dashes and a colon in one sentence.** The single worst house-style violation in the manuscript.

> A bad outcome sharply raises the probability of punishment**---**an average marginal effect of about $18$ percentage points ($p<0.001$)**---**whereas delegation leaves it essentially unchanged**:** the average marginal effect of delegation is $-1.8$ percentage points and statistically insignificant ($p=0.46$; $-2.9$ percentage points among attention-check passers, $p=0.29$).

**Proposed replacement:**
> A bad outcome sharply raises the probability of punishment. The average marginal effect is about $18$ percentage points ($p<0.001$). Delegation leaves it essentially unchanged. The average marginal effect of delegation is $-1.8$ percentage points and statistically insignificant ($p=0.46$; $-2.9$ percentage points among attention-check passers, $p=0.29$).

**M2 — `design.tex:62` — colon-explanation, the exact construction the house style bans.**

> These initial rounds served three purposes simultaneously**:** First, they established a stake from which any later punishment could be deducted.

(The capital "F" after the colon is separately wrong under any style.)

**Proposed replacement:**
> These initial rounds served three purposes simultaneously. First, they established a stake from which any later punishment could be deducted. Second, they familiarized Player~A with the task. Third, they generated the performance data needed to calibrate the algorithm.

**M3 — `design.tex:82` — hyphens used as parenthetical dashes (both a typographic error and a house-style violation), inside a 47-word sentence.**

> He learned that his own payoff would be determined by the outcome of Player~A's final prediction **-** $\pounds 5$ if it fell within 10~lbs of the true weight and $\pounds 1$ otherwise **-** while Player~A's payoff depended solely on her performance in the initial ten rounds.

Single hyphens render as hyphens, not dashes, so this will also look like a typesetting error in the PDF.

**Proposed replacement:**
> He learned that his own payoff would be determined by the outcome of Player~A's final prediction. The payoff was $\pounds 5$ if the prediction fell within 10~lbs of the true weight and $\pounds 1$ otherwise. Player~A's payoff depended solely on her performance in the initial ten rounds.

**M4 — `appendix.tex:7` — em-dash in a heading, inconsistent with the en-dash headings in `results.tex`.**

> `\subsection{Condition balance --- Player A}`

`results.tex:7` and `results.tex:33` use `--`: "Player~A -- Delegation behavior". Pick one. **Proposed:** `\subsection{Condition balance for Player~A}` (avoids the dash entirely and is house-style safe). Note also the missing `~` tie in "Player A" here, used everywhere else as `Player~A`.

---

### Grammar and clarity

**M5 — `design.tex:70` — "limit ... from" is ungrammatical.**

> ... and making this performance parity common knowledge should **limit Player~B from reading** delegation as a signal of **Player~A's believed relative competence**.

One "limits" a quantity; one "keeps" or "prevents" someone *from* doing something. "Player~A's believed relative competence" is also ambiguous about whose belief.

**Proposed replacement:**
> ... and making this performance parity common knowledge should keep Player~B from reading delegation as a signal of Player~A's beliefs about her own relative competence.

**M6 — `results.tex:149` — comma splice around "however".**

> The signaling value of not delegating requires no actual additional effort (Result~\ref{res:effort})**, however,** to explain the treatment effect it similarly rests on being activated by the prospect of punishment itself.

**Proposed replacement:**
> The signaling value of not delegating requires no actual additional effort (Result~\ref{res:effort}). To explain the treatment effect, however, it similarly rests on being activated by the prospect of punishment itself.

**M7 — `design.tex:3` — appositive list reads as a four-item list including its own header.**

> ... and eligibility followed Prolific's standard quality screens**,** a minimum $95\%$ prior approval rate, a fluent-English filter, and a desktop-only restriction (no mobile or tablet) that kept the screen layout consistent across subjects.

As written, "standard quality screens" parses as the first item in the list rather than as the category the list unpacks. A colon would normally fix this and is banned here, so split the sentence.

**Proposed replacement:**
> The experiment was programmed in oTree~\citep{chen_otree_2016}. Eligibility followed Prolific's standard quality screens. These comprised a minimum $95\%$ prior approval rate, a fluent-English filter, and a desktop-only restriction (no mobile or tablet) that kept the screen layout consistent across subjects.

**M8 — `design.tex:82` — dangling modifier plus tense mismatch.**

> ... an algorithm that **performs** as well as Player~A **had performed** in the earlier rounds, and that Player~A was aware of this, **making it common knowledge**.

"making it common knowledge" has no grammatical subject to attach to (the algorithm does not make it common knowledge), and "performs" (present) sits inside a past-tense report.

**Proposed replacement:**
> Crucially, we also told Player~B that Player~A had the option to delegate the final prediction to an algorithm that performed as well as Player~A had performed in the earlier rounds. We also told him that Player~A knew this, which made the algorithm's performance common knowledge.

**M9 — `results.tex:137` — "Lastly" is factually wrong; two more mechanism paragraphs follow.**

> \paragraph{Effort to outperform the algorithm.} **Lastly,** the prospect of punishment could motivate Player~A to exert additional effort ...

The mechanism paragraphs run: Departures → Anticipated differential punishment → Sample composition → Performance and delegation → **Effort** → Signaling value → Taking stock. "Lastly" here misdirects the reader about the structure of the section, and `introduction.tex:14` separately uses "Lastly" for the *signaling* story, so the two sections disagree about which mechanism is last.

**Proposed replacement:**
> The prospect of punishment could also motivate Player~A to exert additional effort when making the final prediction for Player~B.

**M10 — `results.tex:66` — broken "not merely ... but" correlative.**

> Result~\ref{res:delegation} does **not merely** fail to support Hypothesis~1, **but** the effect is statistically significant in the opposite direction.

The correlative requires parallel constituents. Two sentences read better and match the house preference for short declaratives.

**Proposed replacement:**
> Result~\ref{res:delegation} does not merely fail to support Hypothesis~1. The effect is statistically significant in the opposite direction.

**M11 — `literature.tex:34` — the clause is unrecoverable as written.**

> As a result, punishment may partly sanction perceived overconfidence, **outweighing any downstream punishment as a measure of responsibility shifting**.

Punishment cannot "outweigh punishment as a measure". The intended point is that the overconfidence channel contaminates the interpretation of punishment as evidence of responsibility shifting.

**Proposed replacement:**
> As a result, punishment may partly sanction perceived overconfidence rather than measure responsibility shifting.

**M12 — `design.tex:72` — "Thus" asserts a consequence that does not follow.**

> This brings us closer to Player~A's intrinsic preference over delegation in the \textit{No-Punishment} condition, since with any positive cost, the responsibility-shifting motive would need to outweigh a price effect. **Thus,** costless delegation is also standard in the literature~\citep{...}.

That costless delegation is standard in the literature is not a consequence of the preceding sentence; it is corroboration.

**Proposed replacement:**
> Costless delegation is also standard in the literature~\citep{bartling_shifting_2012,coffman_intermediation_2011,feier_hiding_2022}.

**M13 — `conclusion.tex:8` — "whereby" misused.**

> Prediction outcomes and screen times do not indicate punishment-induced additional effort, **whereby** the decision-maker would retain the decision in the hope of outperforming the algorithm.

"Whereby" means "by means of which". The relative here needs "under which" or "in which".

**Proposed replacement:**
> Prediction outcomes and screen times do not indicate punishment-induced additional effort, under which the decision-maker would retain the decision in the hope of outperforming the algorithm.

Same paragraph, same sentence class: "leaving only a non-monetary value **in which** the prospect of punishment makes the recipient's judgment salient in itself" → "leaving only a non-monetary value, under which the prospect of punishment makes the recipient's judgment salient in itself."

---

### Hedging

**M14 — `results.tex:142` — Result statement overclaims a null.**

> \resulthead{res:effort} \textit{**The prospect of punishment does not induce additional effort.** Non-delegators improve on their performance less in the \textit{Punishment} condition ...}

`results.tex:139` explicitly concedes "Effort itself remains unobserved ... so we cannot rule the channel out conclusively". The numbered Result, which is what readers and referees quote, states the stronger claim. Numbered Results should be no stronger than the text that supports them. (This is the results section, so hedging is appropriate here; the intro's leanness rule does not apply.)

**Proposed replacement:**
> \resulthead{res:effort} \textit{We find no evidence that the prospect of punishment induces additional effort. Non-delegators improve on their performance less in the \textit{Punishment} condition than in the \textit{No-Punishment} condition.}

**M15 — `results.tex:129` — "must therefore" is contradicted by its own footnote.**

> The pattern in the \textit{Punishment} condition **must therefore** reflect something other than beliefs about relative ability.

The footnote attached to this very sentence begins "We cannot rule out that some subjects did not fully internalize the individual-level equalization."

**Proposed replacement:**
> The pattern in the \textit{Punishment} condition therefore appears to reflect something other than beliefs about relative ability.

**M16 — `results.tex:3` — balance is evidence for, not a demonstration of, effective randomization; also passive.**

> Treatment randomization was effective, **as demonstrated by** the balance across observable characteristics (Appendix~\ref{appendix:sum_stats}, Table~\ref{tab:treatment_balance}).

**Proposed replacement:**
> Observable characteristics are balanced across conditions (Appendix~\ref{appendix:sum_stats}, Table~\ref{tab:treatment_balance}).

**M17 — `introduction.tex:18` — "the differential disappears" reports a null as a positive finding.**

> Once both channels are closed, **the differential disappears**, and punishment tracks the realized outcome instead.

Also passive and agentless ("once both channels are closed" — by whom?). The fix below does not add a statistical caveat and so respects the lean-intro rule; it simply states what was found.

**Proposed replacement:**
> Once we close both channels, we find no such differential, and punishment tracks the realized outcome instead.

---

### Terminology consistency

**M18 — Condition names are formatted three different ways inside the four numbered Result statements.**

- `results.tex:107` and `results.tex:142`: `\textit{... within the \textit{Punishment} condition ...}` — a **nested** `\textit` inside an already-italic Result, which LaTeX renders **upright**, i.e. the opposite of the emphasis used everywhere else.
- `results.tex:115`: **no markup at all** — "In the Punishment condition, better-performing Player~As ..." and "The additional delegation in the No-Punishment condition ...".
- Body text everywhere else: `\textit{Punishment}` / `\textit{No-Punishment}`.

The Result statements are the most-quoted sentences in the paper and currently render inconsistently. **Proposed fix:** use `\textup{Punishment}` inside the italic Result statements so the condition name renders upright *deliberately and uniformly*, and add the markup to `results.tex:115`, which currently has none.

**M19 — `main.tex:73` — a live `\hl{}` placeholder prints on the title page.**

> `\author{Felix B\"{o}nisch\thanks{WZB Berlin Social Science Center. Email: \texttt{boenischfelix@gmail.com}. \hl{[To do: Add acknowledgments]}}}`

This is not commented out. It renders as a yellow-highlighted "[To do: Add acknowledgments]" in the author footnote on page 1 of every compiled PDF. Strictly this file is outside the listed scope, but it prints, so it belongs in a prose-quality report. (Related, also in `main.tex:18`: `\hypersetup{citecolor=purple, urlcolor=green, linkcolor=red}` produces coloured links that no AEA/QJE/JPE submission should carry.)

---

## MINOR

### Abstract (`abstract.tex:1`)

| # | Current | Proposed |
|---|---|---|
| m1 | "a decision-maker **chooses to make** a payoff-relevant prediction for a matched recipient **or delegate** it" — faulty construction; "chooses to make X or delegate" reads as one choice, and the infinitives do not balance | "a decision-maker either makes a payoff-relevant prediction for a matched recipient or delegates it to an algorithm" |
| m2 | "an algorithm**,** calibrated to perform equally well" — the comma makes the calibration a non-restrictive aside; it is restrictive and load-bearing. Also "equally well" **as whom** is never said, and an abstract must stand alone | "an algorithm calibrated to match her own measured accuracy" |
| m3 | "from $59.3$ to $42.5\%$" — the first figure carries no percent sign | "from $59.3\%$ to $42.5\%$" |
| m4 | "Delegation offers no protection **in return**." — "in return" has no referent | "Delegation offers no protection." |

### Introduction (`introduction.tex`)

| # | Line | Current | Proposed |
|---|---|---|---|
| m5 | 5 | "lets them shed moral responsibility for self-serving choices \citep{tontrup_strategic_2025} **and** makes dishonesty easier" — no serial comma, inconsistent with line 3 ("legal, ethical, and policy") | insert comma before "and makes dishonesty easier" |
| m6 | 7 | "Player~A has the option **to either make** the consequential prediction herself **or delegate** it" | "Player~A has the option either to make the consequential prediction herself or to delegate it" |
| m7 | 7 | "**Thus,** the environment we study, a prediction under genuine uncertainty ..., resembles the settings ..." — "Thus" does not follow from the preceding sentence about the delegation option | "The environment we study, a prediction under genuine uncertainty ..., resembles the settings ..." |
| m8 | 9 | "$42.5$ **percent** of decision-makers" / "$59.3$ **percent**" — the abstract and `results.tex` use `\%` throughout | "$42.5\%$" / "$59.3\%$" |
| m9 | 14 | "Player~A may aim **to merely convey**" | "Player~A may aim merely to convey" |
| m10 | 14 | Enumeration breaks down: "The first is ..." / "The second is ..." / then no third / then "Lastly, ...". Reader loses count | either number all four, or drop the ordinals and rely on the paragraph's own sequencing |
| m11 | 16 | "The intermediary is an algorithm ... The decision involves genuine uncertainty ... **And its** immediate consequences fall entirely on the recipient" — "its" has no clear antecedent (the decision's? the environment's?), and the three items lack the First/Second/Third markers that `literature.tex:11` uses for the *same* three departures | "First, the intermediary is an algorithm rather than a person. Second, the decision involves genuine uncertainty, so a bad outcome may reflect bad luck rather than bad intent. Third, the decision's immediate consequences fall entirely on the recipient, so there is no self-serving choice to police." |
| m12 | 11–12, 22–26 | Three large commented-out blocks sit inside the live introduction (the `%old` intro paragraph and two `%`-blocked contribution paragraphs) | Keep for now per the mid-draft inclusiveness preference; flagged for the polish pass only |

### Literature (`literature.tex`)

| # | Line | Current | Proposed |
|---|---|---|---|
| m13 | 5 | "For an early overview of the principal--agent literature see, e.g., \citet{...}" — missing comma before "see" | "For an early overview of the principal--agent literature, see, for example, \citet{bolton_contract_2005}." |
| m14 | 7 | "They find that delegation effectively shifts punishment ..., **and** the prospect of avoiding punishment constitutes a strong motive" — the second "that" is elided across a subject change, so the clause reads as a new assertion by the authors of *this* paper | "They find that delegation effectively shifts punishment from the dictator to the intermediary, and that the prospect of avoiding punishment constitutes a strong motive for the delegation decision itself." |
| m15 | 7 | Single paragraph of ~300 words covering Bartling, Coffman, Oexl, randomization devices, and Hamman, with a topic sentence about political science that the paragraph then leaves behind | Split after "... rather than from a pure transfer of blame to a deciding intermediary." No content is lost |
| m16 | 15 | "\citet{chugunova_we_2022}, \citet{qin_ai_2025} **and** \citet{irlenbusch_human_2026}" — no serial comma | insert comma before "and" |
| m17 | 15 | "document a large array of **moderators for when and why** algorithms are used in decision-making" | "document a large array of moderators of algorithm use" |
| m18 | 17 | "**Some of** these moderators attach to the algorithm, to the task, and to the authority the human retains." — the paragraph then treats exactly those three, so "Some of" undercuts its own topic sentence | "These moderators attach to the algorithm, to the task, and to the authority the human retains." |
| m19 | 17 | 57-word sentence beginning "On the authority side, people use imperfect algorithms far more readily ..." — three independent findings strung on one spine | split after "\citep{normann_delegate_2025}" |
| m20 | 19 | "**Yet,** preferences for or against algorithms as such produce level effects on delegation." — the comma after a one-word conjunctive is non-standard, and the contrast "Yet" signals is not present | "Preferences for or against algorithms as such produce level effects on delegation." |
| m21 | 26 | "\citet{gogoll_rage_2018} **document** this in ..., \citet{bigman_people_2018} [document this] in vignettes ..., and \citet{jauernig_people_2022} **identify** ..." — the third item breaks the elliptical parallel | "... and \citet{jauernig_people_2022} do so for moral discretion, the human capacity people are most reluctant to hand over in such contexts." |
| m22 | 28 | "Physicians who follow standard-of-care AI recommendations are judged less harshly, and face lower legal exposure, than physicians who reject them" — "than" cannot govern both conjuncts cleanly | "Physicians who follow standard-of-care AI recommendations are judged less harshly than physicians who reject them, and they face lower legal exposure, among lay and expert evaluators alike." |
| m23 | 28 | "people judge the same harm to a pedestrian **more permissible**" — missing complementiser | "people judge the same harm to a pedestrian to be more permissible" |
| m24 | 30 | "\citet{ismagilova_aint_2025} let agents invest on behalf of principals who can then reward or punish **them**." — "them" could be the agents or the principals | "... who can then reward or punish the agents." |
| m25 | 32 | "They find that after good **outcomes delegated** and self-made decisions are rewarded alike" — missing comma creates a garden path | "They find that, after good outcomes, delegated and self-made decisions are rewarded alike in both treatments." |
| m26 | 34 | "Any difference in delegation rates may be due to general preferences for algorithm use." — in *their* design; as written it reads as a claim about this paper's data | "Any difference in delegation rates in their setting may be due to general preferences for algorithm use." |
| m27 | — | Hyphenation drift: "responsibility-shifting" (8×, e.g. `literature.tex:34`, `design.tex:70`) vs "responsibility shifting" (4×, e.g. `literature.tex:7`, `conclusion.tex:6`) | Adopt the hyphenated form when attributive ("the responsibility-shifting motive") and the open form when nominal ("responsibility shifting also operates through ..."), and apply it consistently |

### Design (`design.tex`)

| # | Line | Current | Proposed |
|---|---|---|---|
| m28 | 3 | "via the British platform Prolific **(https://www.prolific.com)**" — bare URL, whereas `introduction.tex:7` correctly uses `\url{}` | `(\url{https://www.prolific.com})` |
| m29 | 5 | "Player~A decides whether to make a payoff-relevant prediction for Player~B herself**,** or to delegate" — comma before "or" in a two-item alternative | delete the comma |
| m30 | 62 | "No feedback was provided between rounds." / "one of the ten rounds was randomly selected for payment." — agentless passives in a section that is otherwise emphatically active ("We calibrated", "We then asked", "We elicited") | "We provided no feedback between rounds." / "we randomly selected one of the ten rounds for payment" |
| m31 | 62 | Double space after the footnote: `stones-and-pounds.\footnote{...}  No feedback` | single space |
| m32 | 68 | "a subject who **scored** 3 out of 10 in the initial rounds **thus delegates** to an algorithm that **produces** the high payoff" — present tense inside a past-tense paragraph, and "For example ... thus" is redundant | "For example, a subject who scored 3 out of 10 in the initial rounds delegated to an algorithm that produced the high payoff for Player~B with $30\%$ probability." |
| m33 | 70 | Footnote stacks modals: "it **might** otherwise dominate the delegation decision and **may** obscure the responsibility-shifting motive" | "it might otherwise dominate the delegation decision and obscure the responsibility-shifting motive of interest" |
| m34 | 76 | "While this linear scoring rule is not proper **as** its payoff-maximizing report places all mass on the single most likely score, irrespective of risk attitude, in practice ..." — 35 words, three commas, no comma before "as" | "This linear scoring rule is not proper. Its payoff-maximizing report places all mass on the single most likely score, irrespective of risk attitude. In practice, most subjects spread probability mass across several scores." |
| m35 | 76 | Double space: "input for any subsequent behavior.  We also asked" | single space |
| m36 | 84 | "Player~B's perceptions of task difficulty, his risk preferences, and a short questionnaire **followed**, before we presented him with his final payoff." — a questionnaire is not something that "follows" alongside perceptions; agentless and mixed | "We then elicited Player~B's perceptions of task difficulty and his risk preferences, administered a short questionnaire, and presented him with his final payoff." |
| m37 | 90 | "what \citet{gogoll_rage_2018} **have coined** the \textit{moral} domain" — one coins a *term*, not a thing; also present-perfect where simple past or present is wanted. Note `literature.tex:26` italicises the whole phrase (`\textit{moral domain}`) while this line italicises only "moral" | "what \citet{gogoll_rage_2018} call the \textit{moral domain}" |
| m38 | 96 | "Whether the same logic extends to algorithmic delegates ... **is less explored**." — a "whether" clause is not "explored" | "How far the same logic extends to algorithmic delegates, to decisions under genuine uncertainty, and to settings in which the outcome falls entirely on the recipient is less well understood." |
| m39 | 102 | "Our study differs from theirs in three respects. First, the task **differs**." — "differs ... differs" in adjacent sentences | "First, the task is different." |
| m40 | 102 | "A failure to delegate may then be punished **as overconfidence** rather than **for assuming responsibility**" — "as X" / "for Ying" are not parallel; and "confounding inference ... with an inference" repeats the noun | "A failure to delegate may then be punished as overconfidence rather than as an assumption of responsibility, confounding responsibility shifting through pure intermediation with an inference about ability." |
| m41 | — | Citation spacing: `design.tex` uses `~\citep{...}` 8× and ` \citep{...}` 7×; `literature.tex` uses the plain space 54× and the tie once | standardise on the plain space, matching the dominant usage |

### Results (`results.tex`)

| # | Line | Current | Proposed |
|---|---|---|---|
| m42 | 3 | "A total of $322$ subjects **were recruited**" — passive opener where the very next footnote is active ("we recruited an extra pair") | "We recruited $322$ subjects ($161$ assigned to Player~A, $161$ to Player~B)." |
| m43 | 9 | "In the \textit{Punishment} condition, where Player~B **can** punish, $42.5\%$ of Player~As **delegated**" — present and past in one clause | "where Player~B could punish" |
| m44 | 10 | "opposing the direction posited by Hypothesis~1" — "opposing a direction" is not idiomatic | "reversing the direction predicted by Hypothesis~1" |
| m45 | 10 | 49-word footnote sentence: "Among the $81$ respondents, $12$ would have stopped delegating ... **constituting weakly significant switching behavior towards making the prediction oneself with punishment possible** (within-subject McNemar's test $p=0.090$), and yielding a hypothetical delegation rate of $50.6\%$." | "Among the $81$ respondents, $12$ would have stopped delegating under hypothetical punishment (25\% of delegators) while only $5$ would have started (15.2\% of non-delegators). The switching is weakly significant and runs toward making the prediction oneself (within-subject McNemar's test $p=0.090$). The implied hypothetical delegation rate is $50.6\%$." |
| m46 | 10 | "**towards**" — the only instance; "toward" is used 6× elsewhere in the same file | "toward" |
| m47 | 10 | "Their behavior reflects **neither systematic preference for one's own prediction** nor systematic deference" — pronoun shifts from "subjects/their" to "one's", and the article is missing | "Their behavior reflects neither a systematic preference for their own prediction nor a systematic deference to the algorithm." |
| m48 | 23 | Figure note carries significance stars: "$^{**}\,p<0.05$". `CLAUDE.md` records that AEA journals have not used significance stars since 2018 | delete the star legend; the note already reports the exact $p$-values |
| m49 | 23, 44, 90 | Whisker phrasing drifts across figure notes: "with whiskers denoting one standard error of the mean" (23) vs "Whiskers are $\pm 1$ standard error of the mean" (44) vs "Whiskers denote $\pm 1$ standard error of the mean" (90) | standardise on "Whiskers denote $\pm 1$ standard error of the mean." |
| m50 | 27 | "We next examine the robustness of the observed **treatment difference** in the delegation share and assess whether the **treatment difference** in delegation survives conditioning on ..." — the same phrase twice in 36 words, and the two halves say the same thing | "We next assess whether the treatment difference in delegation survives conditioning on socio-demographic characteristics and on Player~A's actual and perceived task performance." |
| m51 | 29 | "it may still correlate with **who took the delegation decision seriously**" — informal | "it may still correlate with how seriously subjects took the delegation decision" |
| m52 | 29 | "We return to this pattern **in discussing** the mechanisms." | "We return to this pattern when we discuss the mechanisms." |
| m53 | 44 | "the within-outcome comparisons of average punishment between delegated and **self-decided** predictions" — the only occurrence; "self-made" is used 8× in this file and throughout the paper | "self-made" |
| m54 | 48 | "After a bad outcome, $\pounds 0.48$ versus $\pounds 0.55$." — verbless fragment, and the reader must infer which figure is the delegated one | "After a bad outcome, average punishment is $\pounds 0.48$ for delegated and $\pounds 0.55$ for self-made decisions." |
| m55 | 54 | "$p=0.08$" — two decimals where the rest of the paper uses three ($p=0.033$, $p=0.069$, $p=0.090$) | "$p=0.080$" |
| m56 | 54 | Footnote: "the between-subject association with **Player~B's** average punishment level ... either **their** socio-demographic characteristics or **their** beliefs" — Player~B is "he/his" everywhere else. Also "no **striking** relationship" is informal | "his socio-demographic characteristics or his beliefs"; "no systematic relationship" |
| m57 | 62 | "Player~A **can therefore not** escape punishment" — Germanic word order | "Player~A therefore cannot escape punishment" |
| m58 | 62 | "This result also bears on Result~\ref{res:delegation} **as** any treatment difference ..." — missing comma before "as" | insert comma |
| m59 | 74 | "observers view the delegation of morally consequential decisions to machines **relatively critically**" | "observers are relatively critical of delegating morally consequential decisions to machines" |
| m60 | 81 | "elicited beliefs provide no support **for** a punishment anticipation mechanism **for** Result~\ref{res:delegation}" — repeated preposition; and "punishment anticipation" needs a hyphen when attributive | "elicited beliefs provide no support for a punishment-anticipation mechanism behind Result~\ref{res:delegation}" |
| m61 | 101 | A `%\hl{[Does this not only hold under risk neutrality or other symmetric motives?]}` editorial note sits *inside* the live footnote braces | commented, so harmless in the PDF; flagged for the polish pass |
| m62 | 104 | "First, **hypotheticality** may introduce noise **as** only two of the four scenarios could still materialize" — coinage plus missing comma | "First, the hypothetical framing may introduce noise, since only two of the four scenarios could still materialize ..." |
| m63 | 104, 147 | Trailing whitespace at end of line | strip |
| m64 | 110 | "To the extent this small raw difference matters" — missing "that"; also a 48-word footnote sentence | "To the extent that this small raw difference matters, it works against Result~\ref{res:delegation}. Player~A in the \textit{Punishment} condition performs slightly worse, and, as we will see, it is worse performers who tend to delegate more. Imbalance would therefore attenuate rather than generate the treatment difference." |
| m65 | 110, 139 | "vs.\" (6×) alongside "versus" (2×, lines 48 and 62; also `appendix.tex:78`) | standardise on "versus" in prose and reserve "vs." for table and figure notes |
| m66 | 112 | "Thus, actual performance separates delegators from non-delegators under the prospect of punishment **and** the delegation gap ... **therefore** widens" — missing comma before "and" joining two independent clauses, and "Thus ... therefore" doubles the connective | "Actual performance therefore separates delegators from non-delegators under the prospect of punishment, and the delegation gap between conditions widens with performance." |
| m67 | 125 | Figure note uses both vocabularies in adjacent sentences: "the delegation share of Player~A at each score, **by treatment**" then "the distributions ... **by condition**" | use "by condition" in both, matching the body text (44 uses of "condition" in this file) |
| m68 | 139 | "$45.5\%$ of non-delegators in the \textit{No-Punishment} condition earn ..." — sentence opens on a numeral | "In the \textit{No-Punishment} condition, $45.5\%$ of non-delegators earn the high payoff for Player~B, compared with $21.7\%$ in the \textit{Punishment} condition ..." |
| m69 | 139 | "**Mann-Whitney**" (2×) — hyphen between two surnames | "Mann--Whitney" (same fix for "Kolmogorov-Smirnov" at `appendix.tex:110`) |
| m70 | 35, 5 | "Pearson **Chi-squared**" (3×, capitalised) vs "Pearson **chi-squared**" (`appendix.tex:110`, lowercase) | lowercase "chi-squared" throughout |
| m71 | 151–164 | Fourteen blank lines between the "Taking stock" paragraph and the commented block | collapse; cosmetic only |

### Conclusion (`conclusion.tex`)

| # | Line | Current | Proposed |
|---|---|---|---|
| m72 | 2 | A `%\hl{[On multiple occasions, we say that delegation carries no information about relative ability ... Do we see a contradiction here?]}` note opens the section | commented, so harmless in the PDF; the substantive question it raises is for Lens 1/5, not this pass |
| m73 | 4 | "whether putting an algorithm in charge shapes the **responsibility assignment of those affected by the outcome**" — the abstract phrases the same idea far better ("the responsibility that those affected assign to the delegator") | "whether putting an algorithm in charge shapes the responsibility that those affected assign to the delegator" |
| m74 | 4 | "We **take both questions to** a preregistered online experiment" — unidiomatic | "We address both questions in a preregistered online experiment", matching `introduction.tex:7` |
| m75 | 6 | "The punishment result offers an explanation for why the canonical prediction fails, yet not for **its** reversal." — "its" points to "the canonical prediction", but the reversal is of the *direction*, not of the prediction | "yet not for the reversal we observe" |
| m76 | 8 | "However, **both measures** are imperfect." — "measures" has not been introduced; the reader must reconstruct that this means the belief elicitation and the effort proxies | "However, both the belief elicitation and the effort proxies are imperfect." |

### Appendix (`appendix.tex`)

| # | Line | Current | Proposed |
|---|---|---|---|
| m77 | 5, 49 | "\section{Additional **T**ables}" vs "\section{Additional **f**igures}" | pick one capitalisation |
| m78 | 110 | "we recruited **322** participants instead of the planned **320**" — plain numerals, whereas `results.tex:3` uses `$322$` and `$161$` in math mode | standardise number formatting across the manuscript (this is the single most pervasive formatting inconsistency: `$322$`/`322`, `$42.5\%$`/"42.5 percent", `$10$~lbs`/"10~lbs", "3 out of 10"/"$2.47$ out of $10$") |

---

## Rubric-by-rubric summary

**1. Grammar.** Three sentences do not parse (C1, C2, M5). Beyond those, the recurring non-native patterns are (a) Germanic verb-adverb order ("can therefore not escape", m57), (b) prepositional slips with "limit ... from", "whereby", "in which" (M5, M13), and (c) elided "that" across a subject change (m14). Articles and subject-verb agreement are otherwise handled well, which is above average for the register.

**2. Typos.** Very clean. No misspellings, no duplicated words, no search-and-replace artifacts, no straight quotes (the two `` `` ... '' `` pairs at `results.tex:29` and `appendix.tex:108` are correct LaTeX). The defects are typographic rather than orthographic: hyphens standing in for dashes (M3, m69), two double spaces (m31, m35), two trailing-whitespace lines (m63), and pervasive number-formatting drift (m78).

**3. Sentence length.** 88 sentences exceed 30 words. That is high, but the register tolerates it and most are well constructed. The ones that genuinely hurt are quoted above: `literature.tex:17` (57 words), `results.tex:10` (49, footnote), `conclusion.tex:8` (49), `results.tex:110` (48, footnote), `design.tex:82` (47), `results.tex:94` (46), `appendix.tex:87` (62, figure note). The figure notes at `appendix.tex:60, 87` are the worst offenders and are the easiest to split without losing anything.

**4. Voice.** Active voice is clearly dominant and is one of the manuscript's strengths, particularly in `design.tex` ("We calibrated", "We then asked", "We elicited") and in the mechanism paragraphs of `results.tex`. The exceptions are isolated and listed (M16, m30, m42, m36) — mostly agentless passives that sit oddly next to the active sentences around them.

**5. Hedging.** Proportionate in the results section, and correctly lean in the introduction per house style. The problem is directional and concentrated at the end: `conclusion.tex:10` converts two nulls into positive claims and drops the priority hedge the intro carries (C3), and two Result statements / assertions overreach (`results.tex:142`, `results.tex:129`). There is no over-hedging problem; the "we narrow rather than settle" framing in `results.tex:149` and `conclusion.tex:8` is honest and well judged.

**6. Paragraph cohesion.** Strong overall. Nearly every paragraph opens with a real topic sentence — `results.tex:66, 70, 94, 112, 139, 147, 149` are all textbook. Three exceptions: `literature.tex:7` (topic sentence about political science, then five experimental studies), `literature.tex:17` (the advice-taking versus full-delegation point arrives in the last two sentences with no signpost), and `conclusion.tex:8` (five mechanisms compressed into one paragraph, with the payoff sentence last). `results.tex:137` mislabels its position in the sequence (M9).

**7. Terminology consistency.** Role names are handled well — "Player~A" / "Player~B" in design and results, "decision-maker" / "recipient" in abstract, intro, and conclusion, "principal" / "intermediary" reserved for describing others' work. No drift there. The drift is elsewhere: "self-made" vs "self-decided" (m53), "condition" vs "treatment" within one figure note (m67), "toward" vs "towards" (m46), "responsibility-shifting" vs "responsibility shifting" (m27), "Chi-squared" vs "chi-squared" (m70), "vs." vs "versus" (m65), and — most visibly — the three-way inconsistency in how condition names are marked up inside the numbered Result statements (M18).

**8. LaTeX hygiene in prose.** `\citet` and `\citep` are used correctly throughout; no misuse found in any in-scope file. Quote marks are correct. The problems are: a live printing `\hl{}` placeholder in `main.tex:73` (M19), one bare URL (m28), inconsistent `~\citep` versus ` \citep` spacing in `design.tex` (m41), nested `\textit` that renders upright (M18), and four commented `\hl{}` / `\todo` editorial notes in live files (`literature.tex:23–24`, `results.tex:56, 76, 101`, `conclusion.tex:2`) — harmless in the PDF and appropriate to keep at this stage, but they must clear before submission.

---

## House-style compliance check

| Rule | Status |
|---|---|
| No colons in running prose | **2 violations** — `design.tex:62` (M2), `appendix.tex:17` (M1) |
| No em-dashes (`---`) in running prose | **3 violations** — `appendix.tex:17` (two, M1), `appendix.tex:7` heading (M4); plus hyphens-as-dashes at `design.tex:82` (M3) |
| Never use "gradient" | **Clean.** Zero occurrences in any compiled file. The plain phrasing "the relationship between performance and delegation" is used correctly at `results.tex:112, 129, 131, 135` |
| Introduction stays lean on statistical caveats | **Clean.** No power or borderline-$p$ hedging in `introduction.tex`. No such additions recommended here; the one intro fix proposed (M17) changes a null-as-positive claim into an accurate statement without adding a caveat |
| Mid-draft: keep content | **Respected.** No wholesale cuts recommended. The commented blocks in `introduction.tex`, `results.tex`, and `conclusion.tex` are flagged for the polish pass only. Every proposed edit either splits a sentence or repairs grammar; none removes substantive material |

---

## Score

**7.5 / 10**

Above the bar for a mid-stage draft and clearly the work of a careful writer, but not yet submission-clean. Three ungrammatical sentences and one printing placeholder are hard blockers; the conclusion's unhedged claims are the finding a referee is most likely to seize on. Fixing the 3 CRITICALs and the 19 MAJORs would put this at roughly 9/10 without touching a word of substance.
