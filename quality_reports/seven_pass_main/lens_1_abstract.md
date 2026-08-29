# Lens 1 — Abstract Audit

**Manuscript:** *Accountability and Algorithmic Delegation: Experimental Evidence* (Bönisch, WZB Berlin)
**Files read:** `manuscript/main.tex`, `abstract.tex`, `introduction.tex`, `literature.tex`, `design.tex`, `results.tex`, `conclusion.tex`
**Date:** 2026-08-20

---

## Summary of counts

| Severity | Count |
|---|---|
| CRITICAL | 0 |
| MAJOR | 5 |
| MINOR | 8 |

**Headline:** every number in the abstract survives the cross-check against the body. There is no numeric or sign error. The abstract's weaknesses are structural (no contribution sentence, missing the selection result) and one genuine over-claim of a null.

---

## Rubric scorecard

| # | Criterion | Verdict |
|---|---|---|
| 1 | First sentence states the research question | **Partially** — sentence 1 is background; the question arrives in sentence 2 |
| 2 | Names the method (experiment, design, sample) | **Yes** — preregistered, online, n=322, between-subject manipulation named |
| 3 | Quantifies the headline result | **Partially** — Result 1 quantified precisely; Result 2 carries no magnitudes |
| 4 | States the contribution in one sentence | **No** — closes on a hedge, not a contribution |
| 5 | Cross-check against body | **Numbers pass; two claims over-reach** |

---

## Full text under audit

`manuscript/abstract.tex:1` (single-line file, quoted in segments below):

> Experimental evidence suggests that delegation can shift responsibility for adverse outcomes onto human intermediaries. We ask whether the same responsibility-avoidance motive applies to delegation to algorithms. In a preregistered online experiment with $322$ participants, a decision-maker chooses to make a payoff-relevant prediction for a matched recipient or delegate it to an algorithm, calibrated to perform equally well. We vary between subjects whether the recipient can impose punishment. The prospect of punishment reduces delegation by $16.8$ percentage points, from $59.3$ to $42.5\%$, reversing the direction that the responsibility-shifting account predicts. Delegation offers no protection in return. Recipients punish delegated and self-made predictions alike and condition punishment on the realized outcome. We discuss several candidate mechanisms for this reversal.

---

## Cross-check table (rubric item 5 — the core of this pass)

| Abstract claim | Body location | Verdict |
|---|---|---|
| "$322$ participants" | `results.tex:3` "A total of $322$ subjects were recruited ($161$ assigned to Player~A, $161$ to Player~B)"; `introduction.tex:7` "322 participants" | **Match** (see MAJOR-3 on framing) |
| "preregistered online experiment" | `introduction.tex:7` fn (AsPredicted #133980); `design.tex:3` Prolific/oTree | **Match** |
| "algorithm, calibrated to perform equally well" | `design.tex:66,68` "based on her first ten predictions, the algorithm would have performed equally well"; Bernoulli calibration at individual level | **Match** |
| "vary between subjects whether the recipient can impose punishment" | `design.tex:5,72`; `results.tex` treatment labels | **Match** |
| "reduces delegation by $16.8$ percentage points" | `results.tex:9-10` "significantly \textit{reduces} delegation by $16.8$~percentage points (Pearson Chi-squared, $p=0.033$)" | **Match** |
| "from $59.3$ to $42.5\%$" | `results.tex:9` "$42.5\%$ ... [Punishment]"; "$59.3\%$ delegated [No-Punishment]"; arithmetic 59.3 − 42.5 = 16.8 | **Match** |
| "reversing the direction that the responsibility-shifting account predicts" | `results.tex:10` "opposing the direction posited by Hypothesis~1"; `design.tex:93` H1 states punishment *increases* delegation | **Match** |
| "Delegation offers no protection in return" | `results.tex:51,62`; `conclusion.tex:6` | **Match** |
| "Recipients punish delegated and self-made predictions alike" | `results.tex:48,54` | **Over-reaches — see MAJOR-2** |
| "condition punishment on the realized outcome" | `results.tex:35` "$\pounds 0.20$ on average (paired $t$-test, $p<0.001$)"; `results.tex:54` "Punishment loads overwhelmingly on the outcome" | **Match** |

**No abstract number is absent from the body, and none appears with a different value or sign. Zero CRITICAL findings.**

---

## MAJOR findings

### MAJOR-1 — The abstract has no contribution sentence; it closes on a hedge

`manuscript/abstract.tex:1` (final sentence):

> "We discuss several candidate mechanisms for this reversal."

This is a statement of what remains unresolved, not of what the paper delivers. Rubric item 4 fails outright. The body states the contribution twice, in publishable form, and neither version reaches the abstract:

- `introduction.tex:16`: "we provide, to our knowledge, the first direct test of whether the prospect of punishment motivates delegation to an algorithm"
- `conclusion.tex:10`: "we contribute by providing the first direct test of whether the prospect of punishment motivates delegation to an algorithm, and show that in an environment with inherent task uncertainty and no self-serving choice to police, accountability disciplines algorithm use rather than fueling it"
- `literature.tex:36`: "the first direct test of responsibility shifting onto an algorithm in a setting in which the outcome is genuinely uncertain and delegation is uninformative about relative ability. It is also the first to identify the effect of the prospect of punishment itself on the decision to delegate to an algorithm."

For AER/QJE/JPE, an abstract that ends on "we discuss several candidate mechanisms" reads as a paper that did not land. The novelty claim ("first direct test", "no existing design varies whether punishment is possible" — `introduction.tex:5`) is the strongest sentence in the paper and it is nowhere in the abstract.

**Fix:** replace or precede the closing sentence with the contribution. Something in the register of: "This is the first design to vary whether punishment is possible, and it shows that accountability disciplines algorithm use rather than fueling it."

### MAJOR-2 — "punish ... alike" asserts equivalence the compiled body does not establish

Abstract: "Recipients punish delegated and self-made predictions alike".

What the compiled body actually reports:

- `results.tex:48`: "After a bad outcome, $\pounds 0.48$ versus $\pounds 0.55$. The punishment gap for bad outcomes thus runs in the direction predicted by Hypothesis~2 but is small and statistically insignificant ($\pounds 0.07$; paired $t$-test $p=0.13$; Wilcoxon signed-rank $p=0.54$)."
- `results.tex:54`: "The \textit{Delegated}~$\times$~\textit{Bad outcome} interaction, which captures any insulation from punishment after bad outcomes, amounts to $-0.103$ and is **weakly significant** ($p=0.08$)."
- `results.tex:51` (Result 2, carefully worded): "Player~B does **not punish delegated decisions significantly less** than self-made ones."

Result 2 is a non-rejection. The abstract converts it into an affirmative equivalence claim ("alike"), and it does so despite a regression interaction that is weakly significant *in the direction Hypothesis 2 predicts*. A referee who reads `results.tex:54` after reading the abstract will flag the gap immediately.

Aggravating: the equivalence evidence that would license "alike" exists in the repo but is **not compiled**. `manuscript/results_pre_restructure_2026-05-06.tex:53` contains a TOST equivalence test ("rules out moderate insulation effects (those exceeding $\pounds 0.20$ ...) at $\alpha = 0.05$, but we cannot rule out smaller insulation effects"). That file is out of scope for the paper, so as the manuscript currently compiles, no equivalence test backs the abstract's null. Either restore an equivalence test to `results.tex` or soften the abstract to match Result 2's own wording (e.g. "Recipients punish delegated and self-made predictions no less harshly").

### MAJOR-3 — "$322$ participants" oversells the denominator of the headline result

The headline 16.8pp comparison rests on Player A only: `results.tex:3` "$161$ assigned to Player~A", split roughly 80/80 across conditions (`results.tex:3` fn: "$80$ subjects per role per treatment"). A reader of the abstract will attach n=322 to a 16.8pp effect at p=0.033, and be surprised at ~80 per cell. Nothing stated is false, but for a top-5 abstract the design is worth one clause. **Fix:** "322 participants in matched pairs" or "161 decision-makers and 161 recipients".

### MAJOR-4 — Sentence 1 mischaracterizes the canonical literature in a way the body explicitly contradicts

Abstract sentence 1: "delegation can shift responsibility **for adverse outcomes** onto human intermediaries."

The canonical studies have no outcomes in the relevant sense. `results.tex:70`: "In the modified dictator games of \citet{bartling_shifting_2012, coffman_intermediation_2011, hamman_self-interest_2010, oexl_shifting_2013}, the decision-maker chooses between a fair and an unfair allocation. Her intent is therefore transparent, **the chosen allocation is implemented with certainty**". `literature.tex:11` restates it: "the underlying decision involves genuine predictive uncertainty rather than a known fair--unfair choice".

This distinction is load-bearing. The paper's entire "departures from canonical settings" argument (`results.tex:70`, `introduction.tex:16`) rests on the canonical setting being about *deliberate self-serving choice implemented with certainty*, not about *adverse outcomes*. Writing "adverse outcomes" in the opening sentence imports the paper's own environment into the prior literature and quietly dissolves the contrast the paper needs. **Fix:** "shift responsibility for harmful decisions onto human intermediaries", or "shift blame for unfair choices".

### MAJOR-5 — The selection result is absent, though the introduction bills it as part of the main finding

`introduction.tex:16`: "Accountability disciplines algorithm use rather than fueling it, **and it does so selectively among the decision-makers most likely to succeed**. This reversal is the paper's main empirical result."

The selection finding is a numbered result (`results.tex:115`, Result 4: "In the Punishment condition, better-performing Player~As are less likely to delegate. The additional delegation in the No-Punishment condition comes disproportionately from better performers"), it is quantified (`results.tex:112`: "$2.47$ out of $10$ ... compared with $3.06$ ... $t$-test, $p=0.039$"), and it survives into the conclusion. It is the paper's only *positive* mechanism-side finding — everything else in the mechanisms section is a ruled-out channel. Omitting it leaves the abstract with one positive result and one null, which is exactly the impression the closing hedge reinforces. **Fix:** one clause, e.g. "the drop is concentrated among the better-performing decision-makers".

---

## MINOR findings

### MINOR-1 — First sentence is background, not the research question
`abstract.tex:1`: "Experimental evidence suggests that delegation can shift responsibility for adverse outcomes onto human intermediaries." The question arrives only in sentence 2 ("We ask whether the same responsibility-avoidance motive applies to delegation to algorithms."). This is a defensible AER-style hook and the delay is only one sentence, but rubric item 1 is not strictly met. If the abstract is compressed (see MINOR-4), merging these two sentences solves both problems at once.

### MINOR-2 — Result 2 carries no magnitudes
The abstract quantifies the delegation result to one decimal but gives the punishment result in words only. The body has clean numbers available: `results.tex:48` "$\pounds 0.33$ for delegated and $\pounds 0.30$ for self-made" (good outcome), "$\pounds 0.48$ versus $\pounds 0.55$" (bad outcome), and `results.tex:35` "$\pounds 0.20$ on average" for the outcome effect. The outcome effect in particular ("punishment responds to the outcome by £0.20") is the sharper number and would let the abstract show, rather than assert, that sanctions track outcomes rather than process.

### MINOR-3 — "from $59.3$ to $42.5\%$" never names the conditions
Neither *Punishment* nor *No-Punishment* is named in the abstract, so the reader must infer that 59.3 is the no-punishment baseline from the word "reduces". Also note the numbers are presented in reverse order relative to how the body introduces them (`results.tex:9` gives 42.5 first). Naming the conditions once removes the inference.

### MINOR-4 — Length: 117 words, above AER's ~100-word abstract guidance
Given AER is the stated first target and MAJOR-1 and MAJOR-5 both call for *additions*, the abstract needs compression elsewhere. Candidates: sentence 1 and sentence 2 merge cleanly; "Delegation offers no protection in return." is largely restated by the sentence that follows it.

### MINOR-5 — JEL codes: O33 is a stretch; the natural codes for this paper are missing
`main.tex:83`: "\textit{JEL Classification}: C91, D91, O33".
- **C91** (Design of Experiments: Laboratory, Individual) — fine; standard for online individual-decision experiments.
- **D91** (Role and Effects of Psychological, Emotional, Social, and Cognitive Factors on Decision Making) — good fit.
- **O33** (Technological Change: Choices and Consequences; Diffusion Processes) — weak. Nothing in the paper concerns diffusion, adoption at scale, productivity, or technological change as an economic process. It signals a growth/innovation paper to search engines and to editors triaging by field.
- **Missing and clearly warranted:** **D81** (Criteria for Decision-Making under Risk and Uncertainty) — outcome uncertainty is central to the design (`design.tex:64`) and to the contribution claim; **D83** (Search; Learning; Information and Knowledge; Belief) — the paper elicits and analyzes punishment beliefs throughout (`results.tex:81,94,104`). **D63** (Equity, Justice, Inequality, Other Normative Criteria) is a reasonable alternative for the punishment/blame side.

**Suggested set:** C91, D81, D83, D91 (drop O33, or retain it only if algorithm adoption is pitched as the framing).

### MINOR-6 — Keywords omit the title's own lead term
`main.tex:85`: "algorithms; delegation; responsibility; punishment; experiment". "Accountability" is the first word of the title (`main.tex:72`) and the framing word of the conclusion (`conclusion.tex:10`), yet it is not a keyword. "Algorithm aversion" is also absent despite the paper positioning itself against that literature (`introduction.tex:16`: "adding a determinant of algorithm use"; `conclusion.tex:10`: "the aversion literature"). Consider: accountability; algorithm aversion; blame attribution.

### MINOR-7 — "Recipients" is unqualified; hypothetical punishment runs the other way
The abstract's punishment claim is measured only in the *Punishment* condition (`results.tex:35`: "in the \textit{Punishment} condition, in which punishment was payoff-relevant"). In the *No-Punishment* condition the hypothetical elicitation points the opposite way — `results.tex:62` fn: "these Player~Bs state that they would punish a delegated decision **more** than a self-made one after a bad outcome ($\pounds 0.53$ versus $\pounds 0.43$; paired $t$-test, $p=0.069$)". The abstract's unqualified "Recipients punish ... alike" therefore describes the incentivized subsample, not all recipients in the study. This does not require a change to the abstract, but it is a live referee question and the body should not be the only place the qualifier appears.

### MINOR-8 — The abstract poses one research question; the paper poses two
`introduction.tex:3` asks both: "Does delegating a decision to an algorithm change the responsibility that those affected assign to the delegator? And does the prospect of being held responsible move the delegation decision itself?" `conclusion.tex:4` repeats the pair, and `introduction.tex:16-18` states the contribution as explicitly "twofold". The abstract collapses this into one ("whether the same responsibility-avoidance motive applies to delegation to algorithms"), then reports results on both. The reader meets the punishment result without having been told it was a question. A single "and whether delegation in turn shields the delegator" would close the loop.

---

## Title check

`main.tex:72`: "Accountability and Algorithmic Delegation: Experimental Evidence" — **good fit.** Both nouns are load-bearing: accountability is the manipulated variable, delegation the outcome. The title is honest about the design (it does not promise a mechanism the paper does not deliver, which matters given `results.tex:149` "its mechanism remains unresolved"). One observation only: the title's "Accountability" never appears in the abstract, which speaks entirely in terms of "punishment". Using the word once would tie title, abstract, and conclusion (`conclusion.tex:10`) together.

---

## Bottom line

The abstract is numerically clean — the strongest thing that can be said after a line-by-line cross-check, and it means the paper can be read without fear that the front page misreports the back. What it does not yet do is sell. It states a reversal, states a null, and then tells the reader the mechanism is open. The two things a top-5 abstract must carry, the novelty claim and the positive selection finding, are both present in the introduction and conclusion and both absent here. Fixing MAJOR-1 and MAJOR-5 is largely a copy-and-compress exercise from `introduction.tex:16` and `results.tex:112-115`.

**Score: 6/10.**
