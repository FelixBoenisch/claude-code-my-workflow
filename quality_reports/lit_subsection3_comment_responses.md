# Responses to inline comments in literature.tex (current pass)

Generated 2026-05-22 (second update of the day). After Felix's substantial restructuring pass, many earlier open items are now resolved. This document covers (i) which earlier items are resolved, (ii) which earlier items remain open, (iii) new comments from this pass, and (iv) **new issues I noticed reading the current text that you have not flagged but should**.

---

## Newly resolved in this pass

- **Open 7 (Köbis plausible-deniability framing)** — line 42 now reads "exploiting AI as a plausible-deniability device". The compliance-mechanism framing you ruled out has been dropped. Resolved.
- **Open 8 (move Feier to the end)** — structurally executed. The current order is: (a) moral-domain stylised fact ¶32; (b) vignette/observer strand ¶36; (c) Kirchkamp + Maasland ¶38; (d) four recent papers ¶42; (e) Feier as immediate precedent ¶44; (f) Feier-extension framing ¶46. Resolved.
- **Open 9 (relative-performance transition)** — folded into ¶46 as: "Their own analysis shows that the propensity to delegate is driven primarily by self-assessed errors in the logic task, not by the agent type." Resolved.
- **Open 11 (N12: missing Feier topic sentence)** — restored at ¶44: "The most closely related study is \citet{feier_hiding_2022}, who study delegation to an algorithm in an incentivised laboratory experiment." Resolved.
- **Open 12 (N13: "which other reasons?")** — ¶46 now says delegation-rate differences "may be different not because of differences in anticipated punishment, but more generally by preferences for algorithms" and names self-assessed errors as the driver. Resolved.
- **Open 13 (N14: "too critical" reframe)** — ¶46 now opens with "Our design extends \citet{feier_hiding_2022} along three dimensions." This is the constructive framing suggested. Resolved.

Also: you commented out the Argenton sentence (line 15) and the Steffel sentence (line 19). Both items I had previously discussed as deferrable; the lines remain in the source as `%` comments and can be deleted entirely whenever.

---

## Still open

### Open 1 — N1: Kurtzberg too old (line 36 comment)

Unchanged. My recommendation: drop Kurtzberg and the workplace-domain sentence. If you want to keep the workplace domain, run a verified post-2020 web search; I have not done this. (Bigman 2018 and Shank 2019 are also pre-2020 but cover multi-domain, so they're not strictly post-2020 either — flag if you want strict consistency.)

### Open 2 — N2 (line 40 comment): Kirchkamp / "no red line" / tie to Shank

Unchanged from the previous pass. My suggestion: keep Kirchkamp as the *self-side* complement to Shank's observer-side findings (Shank documents observer-side asymmetries across human-algorithm configurations; Kirchkamp's null says the corresponding self-felt-responsibility effect does not exist). A small rewrite of the Kirchkamp sentence can make this explicit:

```latex
On the self-side, \citet{kirchkamp_sharing_2019} compare a modified dictator game in which the dictator either acts alone or makes the decision jointly with a computer; they find no significant difference in the dictator's self-felt responsibility between human-computer and human-human teams.
```

### Open 4 / N10 (now at line 46): "Careful, this applies to both delegating to the algorithm and delegating to another human"

You have moved this concern into a new inline comment at line 46, attached to the first "extension" clause of the Feier-extension paragraph. The concern is the same as before: the signal-extraction reading attributes the asymmetric finding to algorithm-delegation specifically, but mechanically the signal-extraction logic is available in both treatments.

Suggested addition right after the first extension clause:

```latex
... we calibrate the algorithm at the individual level, removing the relative-performance signal of delegation by construction. The same signal-extraction channel operates in their human-delegate condition as well; our individual-level calibration removes it across both delegate types.
```

This is short and acknowledges the symmetry directly. Alternatively, you could fold the concern into a footnote.

---

## New comments in this revision

### N15 (line 5): "Is this first paragraph really necessary? Better in a conclusionary paragraph?"

Reasonable structural question. The opening paragraph names the three strands the manuscript bridges. Three options:

1. **Keep it as the intro to the literature section.** Standard top-econ practice — open by signposting the three strands the lit review covers. Reader benefit: knows what's coming.
2. **Move it to a closing paragraph of the literature section** that summarises the manuscript's position relative to the three strands. Less standard but defensible.
3. **Move it to the introduction of the paper** as part of the contribution claim. Most common in AER-style intros.

My recommendation: **keep it where it is**, possibly trim it to one sentence. Top-econ lit-review subsections are easier to follow when the reader has a roadmap. A reader who has just finished the introduction wants to know what they're about to read.

### N16 (line 9): "Are there any examples of ancient philosophers?"

Honest answer: yes, but I don't have a verified scholarly reference in your supporting papers folder that documents historical-philosophical examples of responsibility-shifting via delegation. Candidates worth flagging if you decide to pursue:

- **Aristotle**, *Nicomachean Ethics* Book III, on voluntariness and responsibility when one acts through agents.
- **Aquinas** on the doctrine of "indirect intention" (related to double-effect reasoning).
- The Talmudic concept of *shaliach* (an agent acting on behalf of a principal carries the principal's responsibility, with exceptions).

**Caution**: citing these is appropriate only if you actually engage with them substantively. A bare-name citation in passing reads as pretension to a top-econ audience and may invite reviewer scepticism. If you want to use one, the cleanest move is to cite a modern scholarly source that discusses the historical philosophy (e.g., a *Stanford Encyclopedia of Philosophy* article on agency or delegation), not the primary text. If you'd like a verified pointer, I can run a targeted search.

**Conservative recommendation**: skip the ancient-philosophy hook. It doesn't strengthen the paper.

### N17 (line 50): "Check feier data. Does performance differ between treatments?"

**Answer (already in our analyses):** No, not significantly. From `reanalysis_01_treatment_comparisons.py`:

- Human treatment: mean errors = 3.908, SD = 2.362, *n* = 76
- Machine treatment: mean errors = 4.507, SD = 2.274, *n* = 73
- Independent t-test: *t* = −1.576, **p = 0.117**
- Mann-Whitney U: *p* = 0.089

So performance is descriptively slightly worse in the Machine treatment but not significantly different by either parametric or non-parametric tests. This replicates Feier's Errors.ipynb output exactly.

**Implication for the manuscript**: this means the slight delegation-rate gap (46.1% Human vs 56.2% Machine) is NOT cleanly attributable to genuine performance differences — it's more likely driven by *perceived* performance (the Self_Assessment variable, which DOES differ significantly between treatments, *p* = 0.021). Worth noting in the Feier-extension paragraph if you want to make this explicit:

```latex
The descriptive delegation-rate difference between their treatments is small and not significant; nor does it reflect genuine performance differences (errors do not significantly differ, $p = 0.117$).
```

### N18 (lines 52–54): Two findings to incorporate from our reanalyses

You've flagged two findings from our reanalyses to add. Both are worth including:

**(a) The punishment gap is not specifically outcome-conditional.**

From `reanalysis_03_alternative_stories.py`: the within-Machine-treatment OLS interaction `Delegated × GoodOutcome` is null (β = −1.21, *p* = 0.672). The Self-vs-Del gap is approximately the same size for good outcomes (+3.22) and bad outcomes (+4.42); only the bad-outcome cell crosses significance because variance is lower.

Suggested addition (in the Feier-extension paragraph or in a discussion section):

```latex
Indeed, the punishment gap in their data is not specifically outcome-conditional: a within-treatment interaction test shows that the Self-vs-Del gap is statistically the same size for good and bad outcomes ($p = 0.67$ on the interaction), consistent with observers rewarding the use of AI as a decision rather than specifically shielding the principal from blame for bad outcomes.
```

**(b) Delegation correlates with the within-subject Diff_good but NOT Diff_bad.**

From `reanalysis_04_correlation_table.py`: in the Machine treatment, `Del ↔ Diff_g = −0.337*** ` (significant), but `Del ↔ Diff_b = +0.022` (n.s.). The self-justification signature is on good outcomes, not bad. So the dual-role concern is real but does not drive the headline bad-outcome finding.

Suggested addition (in the second extension clause about delegator/evaluator separation):

```latex
... we separate the delegator and evaluator roles across distinct subject pools. Notably, in their data the subject's own delegation decision is significantly correlated with the within-subject differential for good outcomes ($r = -0.34$ in the Machine treatment, $p < 0.01$) but not for bad outcomes ($r = 0.02$, $p > 0.8$), suggesting the dual-role concern is empirically visible but does not drive their headline bad-outcome finding.
```

The asymmetry between Diff_g and Diff_b is informative both ways: it shows the dual-role concern is real (Diff_g) AND that it doesn't compromise Feier's headline (Diff_b). The framing is therefore "we extend by addressing a real concern" rather than "we extend because Feier is broken."

---

## Issues I noticed that you have NOT flagged but should consider

Reading through the current text, I noticed several small but real problems:

### Issue A — Line 21 missing comma

```latex
In sum, the canonical literature documents that in settings with self-interested choice delegation reduces principal punishment and her felt responsibility, ...
```

There's a missing comma after "self-interested choice". As written, it parses as "self-interested choice delegation" (a noun phrase) rather than "[in settings with self-interested choice], delegation reduces...". Fix:

```latex
... documents that in settings with self-interested choice, delegation reduces principal punishment and her felt responsibility, ...
```

### Issue B — Line 24 grammar with "introducing"

```latex
... beginning with \citet{dietvorst_algorithm_2015} introducing the term \textit{algorithm aversion} ---
```

"introducing" reads awkwardly as a dangling participle. Cleaner:

```latex
... beginning with \citet{dietvorst_algorithm_2015}, who introduced the term \textit{algorithm aversion} ---
```

### Issue C — Line 38 stray em-dashes

```latex
Evidence using incentivised laboratory experiments --- is younger and smaller.
```

The em-dashes wrap nothing — there's no interjected clause. Either remove them entirely:

```latex
Evidence using incentivised laboratory experiments is younger and smaller.
```

Or fill in what was intended to be interjected (perhaps an example or a clarifying phrase).

### Issue D — Line 46 punctuation after semicolon

```latex
... preferences for algorithms; Their own analysis shows that ...
```

Capital "T" after a semicolon is non-standard. Either lowercase "their" or replace the semicolon with a period.

### Issue E — Line 48 multiple problems

```latex
Our experiment is the first to our knowledge to provide a clean test of blame-shifting in a setting with inherent uncertainty, while controlling for concerns about reltive performance, whether in such a setting anticipated punishment is a motive in the delegation decision itself.
```

Three problems:
1. **Typo**: "reltive" → "relative".
2. **Grammar**: "to provide a clean test of blame-shifting … whether in such a setting anticipated punishment is a motive" is broken — the second "whether" clause hangs without a verb to attach to.
3. **Substance**: the sentence tries to say two things (clean test of blame-shifting AND test of whether anticipated punishment motivates delegation). They should be in separate clauses.

Suggested rewrite:

```latex
Our experiment is, to our knowledge, the first to provide a clean test of blame-shifting in a setting with inherent uncertainty, controlling for relative-performance concerns. It also tests whether, in such a setting, the prospect of punishment itself motivates the delegation decision.
```

### Issue F — Subsection 3 title vs ¶32–34 content

The subsection is titled "Responsibility perceptions of decisions involving algorithms." But ¶32 ("smaller subset focuses on algorithm-use preferences") and ¶34 ("the moral domain introduces the responsibility-shifting motive") are positioning paragraphs that bridge from the prior subsection (algorithm use) to the responsibility-perceptions subsection. The first paragraph of subsection 3 is therefore not yet about responsibility perceptions — it's about *which subset of the algorithm-use literature* is relevant to the manuscript.

Two ways to fix:

1. **Move ¶32 and ¶34 to the end of the previous subsection** ("Delegation to algorithms") as the closing paragraphs. The moral-domain stylised fact then sits within the algorithm-use literature; subsection 3 then opens cleanly with the responsibility-perceptions question.

2. **Keep ¶32 and ¶34 where they are**, but reframe them as a setup paragraph rather than as parts of the subsection's central content. A small structural sentence at the top of ¶32 like "Before turning to responsibility perceptions specifically, we note one feature of the algorithm-use literature relevant to our setting..." would tell the reader these paragraphs are scaffolding, not the main content.

My recommendation: **Option 1** (move). It restores the cleaner narrative arc where each subsection has one job.

### Issue G — Line 34 awkward phrasing

```latex
With the decisions affecting others, the \textit{moral domain} in delegating to algorithms also introduces the responsibility-shifting motive that characterizes setting of delegation to humans.
```

"the moral domain in delegating to algorithms also introduces the responsibility-shifting motive" — the moral domain doesn't *introduce* anything; it's the setting in which RS becomes relevant. Also "setting" should be plural or have an article.

Suggested:

```latex
Once decisions affect a third party, the responsibility-shifting motive established for human delegation (Section~1) becomes relevant for algorithmic delegation as well.
```

This is cleaner and connects subsections 1 and 3 explicitly.

---

## Big-picture observation

The current text is in a much better state than the previous pass. The Feier-extension paragraph (¶46) reads particularly well now — the "we extend along three dimensions" framing is constructive and clear. The four recent papers paragraph (¶42) is also clean.

The two main remaining structural concerns are:
- **¶32–34 placement** (Issue F): these paragraphs straddle two subsections; cleaner to move them.
- **Open 4/N10 in ¶46**: the signal-extraction-applies-to-both-treatments concern needs a one-clause acknowledgment, as discussed above.

The smaller textual issues (B, C, D, E, G) are quick fixes — well under five minutes to apply.

---

## Self-review

I verified:
- Each "newly resolved" item against the current literature.tex. Each is confirmed in the file.
- The Feier performance-difference numbers (3.908 vs 4.507, *p* = 0.117) from `reanalysis_01_treatment_comparisons.py`'s output, not from memory.
- The Delegated × GoodOutcome interaction null (*p* = 0.67) from `reanalysis_03_alternative_stories.py` output.
- The Del ↔ Diff_g and Del ↔ Diff_b correlations (-0.34 and +0.02 in Machine treatment) from `reanalysis_04_correlation_table.py` output.
- That the Argenton and Steffel sentences are commented out (lines 15 and 19) with `%`.

What I did NOT verify in this pass:
- The post-2020 substitute for Kurtzberg (Open 1) — still pending if you want.
- The ancient-philosopher reference (N16) — not pursued.
- Whether the proposed Issue F restructure (moving ¶32–34) is the right move given subsection-2 length constraints. Worth a second look if you implement.
