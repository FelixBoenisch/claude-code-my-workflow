# Lens 2 — Introduction Structure

**Manuscript:** Accountability and Algorithmic Delegation: Experimental Evidence
**File under review:** `manuscript/introduction.tex` (checked against `abstract.tex`, `literature.tex`, `design.tex`, `results.tex`, `conclusion.tex`, `main.tex`)
**Framework:** Cochrane / Varian
**Date:** 2026-08-20

---

## Summary of counts

| Severity | Count |
|---|---|
| CRITICAL | 0 |
| MAJOR | 4 |
| MINOR | 8 |

**Score: 7 / 10**

Rubric items 3 (enumerated contribution) and 5 (roadmap accuracy) pass cleanly. Item 4 passes for the headline result only. Items 1, 2, and 6 carry the four MAJOR findings.

---

## Rubric scorecard

| # | Item | Verdict |
|---|---|---|
| 1 | Opens with the research question, not AI throat-clearing | **Partial** — question arrives at sentence 7 of 9 (MAJOR-1) |
| 2 | hook → context → contribution → roadmap; literature after the hook | **Partial** — economics literature is correctly placed after the hook, but a normative-debate citation block precedes it (MAJOR-1); contribution is buried behind the mechanism paragraph (MAJOR-3) |
| 3 | Contribution explicitly counted and enumerated | **Pass** — "Our contribution is twofold. First… Second…" |
| 4 | Findings previewed with magnitudes | **Partial** — delegation result carries numbers; punishment and selection results do not (MINOR-1) |
| 5 | Roadmap matches `main.tex` `\input` order | **Pass** — literature → design → results → conclusion, exactly as inputted |
| 6 | Intro framing consistent with what the body delivers | **Fail on two counts** (MAJOR-2, MAJOR-4) |

---

## MAJOR findings

### MAJOR-1 — The question is buried four sentences deep behind an AI-ubiquity opening and a normative-debate citation cluster
`manuscript/introduction.tex:3`

> "Algorithms take part in a growing share of consequential decisions. Many of these decisions carry consequences that fall, at least in part, on others. Physicians rely on diagnostic systems, firms let screening software rank job applicants, and financial advisors draw on algorithmic tools. In each of these settings, a human decides whether to put the algorithm in charge. Who bears responsibility when an algorithm's decision causes harm is the subject of a lively legal \citep{lemley_remedies_2019, buiten_law_2023}, ethical \citep{matthias_responsibility_2004, santoni_de_sio_four_2021}, and policy \citep{european_commission_liability_2019,european_union_ai_act_2024} debate."

Four sentences of scene-setting, then a six-citation drop, and only then the tension ("While the debate concerns where responsibility should lie, behavior is another matter") and the two questions. Cochrane's rule is that the first paragraph earns its keep by posing the question; here the first four sentences are interchangeable with the opening of any AI paper and none of them is specific to delegation-plus-accountability. The citation block is also literature placed *before* the hook — the rubric's item 2 failure mode — even though it is normative literature rather than the economics strand.

The material worth keeping is sentence 4 ("a human decides whether to put the algorithm in charge") and the tension sentence. The three worked examples and the citation cluster can move down into paragraph 2 or into `literature.tex`, which already covers the policy strand.

**Fix direction:** open on the tension. Something in the shape of "When an algorithm makes a decision that harms someone, a human chose to put it in charge. Whether that choice changes who answers for the harm, and whether the prospect of answering for it changes the choice, are behavioral questions that the legal and ethical debate over algorithmic responsibility does not settle." Examples and normative citations follow.

---

### MAJOR-2 — The intro asserts a causal cross-study attribution that the body explicitly declines to make
`manuscript/introduction.tex:18`

> "However, the same subject both delegates and evaluates, and the delegation decision is strongly determined by beliefs about relative ability, inviting punishment of overconfidence rather than of delegation itself. **Once both channels are closed, the differential disappears, and punishment tracks the realized outcome instead.**"

This sentence tells the reader that closing two specific design channels is *what caused* Feier et al.'s punishment differential to vanish in this paper. The body never establishes that, and in two places says the opposite:

- `manuscript/design.tex:102` lists **three** differences from Feier et al. and puts the task first: "Our study differs from theirs in three respects. **First, the task differs.** Second, the roles of Player~A and Player~B are separated across disjoint subject pools. Third, their design does not control for relative performance at the individual level." The task difference is a live third channel that the intro sentence silently drops.
- `manuscript/results.tex:70` concedes that the whole class of design departures "may explain the absence of the predicted effect, not its reversal."
- The now-commented passage at `manuscript/results.tex:171` states the point flatly: "the question of which design feature is causally responsible for the sign reversal cannot be resolved without an experiment that varies relative-performance calibration directly, which we do not do here." That caution was correct and the intro contradicts it.

At AER/QJE, a two-study comparison presented as a channel-shutdown experiment is exactly the sentence a referee circles. The design difference set is not orthogonal, the samples differ, and Feier et al. measure reward while this paper measures punishment.

**Fix direction:** state the co-occurrence, not the mechanism. E.g. "In our design, where neither channel is present, no such differential appears. Punishment tracks the realized outcome instead." That keeps the contrast and drops the causal claim. (Note it also requires reconciling the enumeration — see MINOR-5.)

---

### MAJOR-3 — The contribution is buried behind a 330-word inconclusive mechanism paragraph
`manuscript/introduction.tex:14`, contribution at `:16`

The intro's longest paragraph runs through four candidate mechanisms (anticipated punishment, punishment-induced effort, selection on performance, signaling) and lands on:

> "Thus, while the drop in delegation under punishment is robust, which motive produces it is a question we narrow rather than settle."

The reader then meets "Our contribution is twofold" at line 16. The structural consequence is that the last thing a skimming reader absorbs before the contribution statement is the paper's weakest material — a list of things the data cannot distinguish. This is a Varian ordering failure independent of length: the contribution should be adjacent to the findings, with mechanism narrowing either compressed or moved after it.

I am reading this against the mid-draft verbosity tolerance and still flagging it, because the damage is ordering, not word count. Two options, either acceptable:

1. Compress to roughly four sentences that name the candidates and state the verdict, keeping the position.
2. Keep the length but move it *after* the two contribution paragraphs, so the intro reads findings → contribution → what we could not pin down → roadmap.

Option 2 is the safer edit at this stage since it preserves all the content (consistent with the standing preference for keeping material at mid-draft).

---

### MAJOR-4 — The two headline questions are stated in the opposite order from every other part of the paper
`manuscript/introduction.tex:3`

> "**Does delegating a decision to an algorithm change the responsibility that those affected assign to the delegator?** And does the prospect of being held responsible move the delegation decision itself?"

Attribution first, delegation second. Everything downstream runs the other way:

| Location | Order |
|---|---|
| `abstract.tex:1` | delegation reversal first, then "Delegation offers no protection in return" |
| `introduction.tex:9` (findings) | delegation first |
| `introduction.tex:16` / `:18` (contribution) | delegation is First, attribution is Second |
| `design.tex:93` / `:99` | Hypothesis 1 = delegation, Hypothesis 2 = punishment |
| `results.tex:7` / `:33` | Player A delegation, then Player B punishment |
| `conclusion.tex:4` | "whether the prospect of being held responsible shapes the decision to put an algorithm in charge, **and** whether putting an algorithm in charge shapes the responsibility assignment" — delegation first |

The intro is the single outlier, and it is the place where the reader forms the mapping. It forces a re-index at the findings paragraph six lines later. Swapping the two questions is a one-line fix with no downstream consequences, and it makes the conclusion's opening a clean echo of the intro's.

---

## MINOR findings

### MINOR-1 — Magnitudes are given for one of three previewed results
`manuscript/introduction.tex:9`, `:14`

The delegation result is fully quantified ("$42.5$ percent", "$59.3$ percent", "roughly $17$~percentage points"). The other two previewed results are qualitative only:

- Punishment (`:9`): "Player~B punishes delegated and self-made decisions alike" — no numbers, though `results.tex:48` has them ($\pounds 0.48$ vs $\pounds 0.55$ after bad outcomes; $\pounds 0.33$ vs $\pounds 0.30$ after good).
- Selection (`:14`): "it is disproportionately the better-performing Player~As who keep the decision" — no numbers, though `results.tex:112` has $2.47$ vs $3.06$ correct predictions among delegators across conditions.

Since the punishment null is the paper's *second enumerated contribution*, giving it a magnitude in the intro strengthens it. A null with numbers reads as a measurement; a null without reads as a failure to find. Adding levels is not statistical hedging and does not touch the lean-intro rule.

### MINOR-2 — Effect size rounds inconsistently against the abstract
`manuscript/introduction.tex:9` says "roughly $17$~percentage points"; `abstract.tex:1` says "$16.8$ percentage points"; `results.tex:9` says "$16.8$~percentage points". `results.tex:104` also uses "$17$~percentage-point". Pick one. The abstract and Result 1 both use 16.8, so the intro should match.

### MINOR-3 — "match how Player~B actually punishes" overstates belief accuracy
`manuscript/introduction.tex:14`

> "Her elicited beliefs show no such expectation, and instead match how Player~B actually punishes."

`results.tex:81` reports two patterns, and the first one contradicts a plain reading of "match": "Player~As, on average, substantially overestimate punishment in every scenario." Beliefs match the *absence of a delegation penalty*, not the level of punishment, and Figure~\ref{fig:realized_vs_anticipated} makes the level gap visually obvious. The sentence is defensible in context but a referee comparing it to the figure will read it as a misstatement.

**Fix direction:** "and instead reproduce the absence of any delegation penalty in Player~B's actual punishment."

### MINOR-4 — "322 participants" names the recruitment total, not the unit of either test
`manuscript/introduction.tex:7`

The delegation comparison rests on 161 Player As, and the punishment elicitation on the Player Bs in the *Punishment* condition. "322 participants" is accurate as a recruitment figure but flatters the design in the sentence that introduces it. A purely descriptive fix carries no statistical hedging: "with $161$ decision-makers and $161$ matched recipients."

### MINOR-5 — Three different enumerations of "how we differ" circulate, and two of them disagree
- `introduction.tex:16` — departs from the human-intermediary canon "in three respects": algorithmic intermediary, genuine uncertainty, consequences fall entirely on the recipient. This matches `literature.tex:11` exactly. **Consistent, good.**
- `introduction.tex:18` — departs from Feier et al. via **two** channels: dual delegator/evaluator role, and relative-ability signalling.
- `literature.tex:34` — departs from Feier et al. in **three** respects: individual-level calibration, separated roles, varied punishment regime.
- `design.tex:102` — departs from Feier et al. in **three** respects: **the task differs**, separated roles, relative performance not controlled.

`literature.tex:34` and `design.tex:102` name different third items, and the intro names only two. A reader who reads all three sections cannot tell how many differences there are. The intro should state the same count as `literature.tex`, or state two and say plainly that it is naming the two that bear on the punishment result. (This is entangled with MAJOR-2 — fixing that sentence is the natural moment to fix the count.)

### MINOR-6 — "the decision-makers most likely to succeed" overreaches for this sample
`manuscript/introduction.tex:16`

> "Accountability disciplines algorithm use rather than fueling it, and it does so selectively among the decision-makers most likely to succeed."

Mean performance is $2.76$ and $3.09$ correct out of ten (`results.tex:110`), and the delegator contrast driving Result 3 is $2.47$ vs $3.06$ (`results.tex:112`). "Most likely to succeed" describes subjects whose success probability is roughly $25$–$30$ percent. `results.tex:133` even notes that better performance moves subjects *toward* maximal outcome uncertainty in this sample. "the better-performing decision-makers" is both accurate and no weaker rhetorically.

### MINOR-7 — Dead commented-out prose inside the section body
`manuscript/introduction.tex:11-12` holds a `%old` near-duplicate of the live mechanism paragraph; `:24-26` holds two long stale blocks, one of which frames the paper as contributing to "three strands of literature" and asserts a regulatory-lever claim that the current conclusion no longer makes. The repo's own single-source-of-truth rule asks for no commented-out stale content before a draft is shared, and the `:26` block will actively mislead a co-author skimming the source. Move both to `quality_reports/section_diffs/` or delete.

### MINOR-8 — Roadmap omits the appendix
`manuscript/introduction.tex:20` covers Sections 2–5 accurately but not `appendix.tex`, which `main.tex:110` inputs and which carries the preregistration, balance table, and several referenced figures (`appendix:prereg`, `appendix:sum_stats`, `fig:punishment_passers`, `fig:punishment_hypothetical`). One trailing clause noting that the appendix contains the preregistration and supplementary analyses is standard at the target journals.

---

## What the introduction does well

- **Contribution is counted and enumerated.** "Our contribution is twofold. First… Second…" is exactly what the rubric asks for, and each contribution is a distinct claim rather than a restatement of the other.
- **The headline finding is previewed with real numbers** and with the direction stated against the prediction it overturns ("reverses the canonical prediction"), which is the strongest sentence in the intro.
- **The roadmap is accurate.** Section order and content descriptions match `main.tex` and the section files line for line, including the fact that mechanisms live inside Results rather than in a separate section.
- **The economics literature is correctly placed after the hook** (paragraph 2, `:5`), and it is used to set up a prediction the paper then overturns rather than as a survey.
- **Design description at `:7` is faithful to `design.tex`** on every checkable detail: ten rounds for own payoff, one consequential prediction, individual-level calibration, between-subject punishment manipulation, strategy-method elicitation over all four (delegation, outcome) cells.
- **Departures paragraph stays on the human-intermediary strand**, as it should.

---

## Priority order for revision

1. MAJOR-2 (causal cross-study claim) — highest referee risk, smallest edit.
2. MAJOR-4 (question order) — one-line swap, removes a needless reader stumble.
3. MAJOR-3 (contribution buried) — reorder rather than cut.
4. MAJOR-1 (opening) — largest rewrite, but the intro is publishable without it and unignorable with it.
5. MINOR-1, -3, -5 — substantive accuracy.
6. MINOR-2, -4, -6, -7, -8 — housekeeping.
