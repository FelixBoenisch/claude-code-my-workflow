# Seven-Pass Review: Accountability and Algorithmic Delegation

**Date:** 2026-08-21
**Path:** `manuscript/main.tex`
**Branch:** `restructure/results-section`
**Scope:** the seven files `main.tex` compiles (`abstract`, `introduction`, `literature`, `design`, `results`, `conclusion`, `appendix`). The orphans `literature_revised.tex` and `results_pre_restructure_2026-05-06.tex` were excluded.

## Executive verdict

**Overall state: REVISE-MAJOR**

173 findings (17 CRITICAL, 68 MAJOR, 88 MINOR). The paper is numerically sound at its core. Every headline number in the abstract reconciles against the body, delegation shares and Ns tie out across prose, tables, figures, and conclusion, and the anchor citation (`feier_hiding_2022`, 21 uses) was verified correct on all eight distinct characterizations.

The problem is not the data. It is that **the results restructure on this branch dropped supporting tables from the build while the claims that depended on them stayed in the text.** Four lenses found this independently, from four different directions. Everything in the CRITICAL table below is verified against source files or `scripts/python/_outputs/numbers.json`, not taken on a reviewer agent's word.

Nothing here requires new data collection. The two most severe items are fixed by re-analysis and re-wording.

## Cross-lens CRITICAL issues

| # | Lens(es) | Issue | Recommendation |
|---|---|---|---|
| C1 | 1, 3, 4, 5, 6 | **Equivalence asserted without an equivalence test.** The abstract says recipients "punish delegated and self-made predictions alike"; `conclusion.tex:10` says "delegation cannot shift blame". No power, MDE, or TOST appears anywhere in the compiled paper. The TOST was run: it **fails** at ±£0.10 (p=0.332) and passes only at ±£0.20 (p=0.012) — a bound as large as the paper's own headline effect. Observed £0.077 against an MDE of £0.149. | Either report the TOST with its bound stated honestly, or retreat to Result 2's own wording ("does not punish significantly less"). Do not keep "alike" / "cannot". |
| C2 | 1, 3, 4, 5 | **Three tables were dropped from the build and the claims resting on them were not.** Current `main.log` loads five tables. The July logs (`pass1.stdout`) additionally loaded `power_mde.tex` and `reg_delegation_robustness.tex`; `balance_player_b.tex` has never been referenced. `power_mde.tex`'s own note refers to "the equivalence bound used in Result 2 in the body" — a bound no longer present. | Decide per table: re-`\input` it, or remove the claim it supported. C1, C3, and C4 are all downstream of this one. |
| C3 | 3, 4 | **The H2 interaction is mislabelled and carries the wrong p-value.** `results.tex:54` calls the `Delegated × Bad outcome` coefficient (−0.103, p=0.08) the one "which captures any insulation from punishment after bad outcomes". It is the difference-in-differences. Insulation is the linear combination 0.032 − 0.103 = −0.071, i.e. the £0.07 at p=0.13 already reported at `results.tex:48`. The paper therefore calls the same quantity "statistically insignificant" at line 48 and "weakly significant" at line 54. | Report the linear combination with its own SE. Relabel the interaction as the DiD. Resolve the six-line self-contradiction. |
| C4 | 3, 5 | **A Player B balance table exists, fails on two of six covariates, and is not reported.** `tables/balance_player_b.tex` shows age 37.1 vs 42.4 (p=0.011) and university degree 68.8% vs 48.1% (p=0.013). `appendix.tex:13` declines to report it because punishment "is identified within-subject, so balance across conditions is not strictly required". That is correct for the within-subject H2 test and false for the between-condition Player B comparisons the appendix itself runs. | Report the table. Narrow the justification to the within-subject analysis, and address imbalance where between-condition comparisons are actually made. |
| C5 | 3, 4 | **The mechanism section's central claim is never tested.** "The performance/delegation relationship is stronger under punishment" carries the mechanism argument, but no treatment × performance interaction appears in any table. Separately, `results.tex:110` reports perceived-performance *levels* (4.65 vs 4.87) as "similar overconfidence", while overconfidence is 1.89 vs 1.78 and `reg_delegation_robustness.tex` defines the construct correctly. Manuscript and table code disagree. | Run and report the interaction. Fix the overconfidence figures to match the code's definition. |
| C6 | 1, 2 | **The intro asserts a causal cross-study attribution the body explicitly disclaims.** `introduction.tex:18`: "Once both channels are closed, the differential disappears". `results.tex:70` concedes the departures "may explain the absence of the predicted effect, not its reversal", and a commented passage at `results.tex:171` says which feature is responsible "cannot be resolved without an experiment that varies relative-performance calibration directly, which we do not do here". `design.tex:102` also names a third difference (the task) that the intro drops. | Downgrade to association. Smallest edit on this list, highest referee risk. |
| C7 | 7 | **The bibliography has never been validated, and a fabrication-flagged entry ships in it.** `stein_dont_2020` has `{[NOT FOUND]}` in its title field and an `annote` recording that it "may be partially fabricated by an earlier session". 13 `VERIFY` flags remain, 5 on cited entries. Root cause: `CLAUDE.md:31` names `Bibliography_base.bib` as the single-source bibliography and points `/validate-bib` at it, but that file holds **two dummy entries** (`Example2024_book`, `Example2025_article`). The real 106-entry `ProjectAlgorithm.bib` has never been checked by the repo's own tooling. | Delete `stein_dont_2020`. Resolve the 5 cited `VERIFY` flags. Repoint `/validate-bib` and `CLAUDE.md` at `ProjectAlgorithm.bib`. |
| C8 | 6 | **A placeholder renders in every compiled PDF.** `main.tex:73` carries an uncommented `\hl{[To do: Add acknowledgments]}` in the author footnote, highlighted on page 1 of the current `main.pdf`. | One-line fix. Do before any circulation. |

## MAJOR issues (second-round)

| # | Lens(es) | Issue |
|---|---|---|
| M1 | 4, 5 | Mechanism results run on attention-check passers only, where pass rates are differential by condition for Player A (23.8% vs 13.6%) — a no-longer-randomized subsample. Belief–delegation is null in the full sample (p=0.388), significant among 60 passers (p=0.011), p=0.125 in the uncompiled robustness table. Pass rates are never reported. |
| M2 | 3, 5 | A 20.0 pp order effect within *Punishment* (p=0.070) versus −4.6 pp under *No-Punishment* (p=0.674) was drafted and commented out at `results.tex:167`. See the contradictions section — this is unreported, not fatal. |
| M3 | 5 | Zero multiple-testing acknowledgment against 34 p-values in `results.tex`. |
| M4 | 1 | The abstract has no contribution sentence. It closes on "We discuss several candidate mechanisms for this reversal." The novelty claim exists in publishable form at `introduction.tex:16`, `conclusion.tex:10`, and `literature.tex:36`, and reaches the abstract in none of them. |
| M5 | 1 | Result 4 (better performers keep the decision under punishment) is absent from the abstract though `introduction.tex:16` bills it as part of the main result. It is the only positive mechanism-side finding. |
| M6 | 2 | The intro's two headline questions are ordered attribution-first; the abstract, H1/H2, results order, and conclusion all run delegation-first. The intro is the sole outlier. |
| M7 | 2 | The contribution sits behind a 330-word inconclusive mechanism paragraph ending on "a question we narrow rather than settle". |
| M8 | 4 | `results.tex:81` claims the treatment did not change punishment beliefs; Appendix Figure A3 shows £0.60 vs £0.40 (Welch p=0.038) on the exact variable Result 3 says "carries the relationship". |
| M9 | 4 | Result 5 (effort channel) has no magnitude, test, table, or figure. Reconstructed: +0.51 lbs vs +10.94 lbs, between-condition p=0.007. The claim is correct and simply unreported. |
| M10 | 5 | Incentivized Holt–Laury risk preferences and a purpose-built perceived-*relative*-ability measure are elicited (`design.tex:76,78`) and analyzed nowhere. The latter is the direct test of the paper's central identifying claim, currently defended with an absolute-ability measure. |
| M11 | 3 | The manipulation confounds social accountability with Player A having money at stake, which undercuts the conclusion's headline reading. |
| M12 | 7 | `steffel_passing_2016` is miscited at `design.tex:84` (it has no punishment stage) and its real finding — people delegate to other people but not to inanimate objects — anticipates this paper's own reversal while being listed as grounding the rejected H1. |
| M13 | 7 | `literature.tex:17` presents genuine empirical tension between `litterscheidt_financial_2020` and `dargnies_aversion_2026` as refinement via a bare "whereas". Both citations are individually faithful. |
| M14 | 4 | `results.tex:5` claims all regressions use HC1; the two punishment tables cluster at Player B level. |
| M15 | 4 | `reg_punishment.tex` and `reg_belief_specs.tex` print significance stars with no legend (and AEA style omits stars entirely). |
| M16 | 6 | Two sentences do not parse: `results.tex:70` ("and with it does the value") and `conclusion.tex:8` ("Merely signaling to exert additional effort… but move"). |
| M17 | 7 | Four in-bib, uncited works bear on the novelty claim — `kirchkamp_sharing_2019` (with a live TODO at `literature.tex:24`, and its null on felt responsibility *supports* Result 2), `maasland_blame_2022`, `blunden_downside_2023`, `weitzner_reputational_2024`. |
| M18 | 6 | 88 sentences exceed 30 words; terminology drifts ("self-decided"/"self-made", "condition"/"treatment"); number formatting is inconsistent. |

## MINOR polish

- JEL codes: O33 is a weak fit (no diffusion content); D81 (uncertainty) and D83 (belief elicitation) are missing. Suggested set C91, D81, D83, D91.
- Keywords omit "accountability", the title's own lead term.
- Condition names render three different ways inside the four numbered Result statements (nested `\textit` renders upright at lines 107 and 142; no markup at 115).
- `results.tex:137` labels a paragraph "Lastly" with two mechanism paragraphs following; the intro uses "Lastly" for a different mechanism.
- Five colon / em-dash house-style violations: `appendix.tex:17`, `design.tex:62`, `design.tex:82` (single hyphens as parenthetical dashes will look like a typesetting error).
- `bartling_shifting_2012`, the second most-cited work, has an initials-only author field while all 65 other entries print full first names.
- Figure notes at `appendix.tex:87` (62 words) and `literature.tex:17` (57 words) are the longest sentences in the paper.
- Intro opens with four sentences of AI-ubiquity setup plus a six-citation normative block before the question appears.

## Per-lens scorecard

| Lens | Critical | Major | Minor | Score/10 |
|---|---|---|---|---|
| 1. Abstract | 0 | 5 | 8 | 6.0 |
| 2. Intro | 0 | 4 | 8 | 7.0 |
| 3. Methods | 6 | 11 | 7 | 5.0 |
| 4. Results | 3 | 12 | 12 | 6.0 |
| 5. Robustness | 3 | 8 | 4 | 3.0 |
| 6. Prose | 3 | 19 | 36 | 7.5 |
| 7. Citations | 2 | 9 | 13 | 6.5 |
| **Overall** | **17** | **68** | **88** | **5.5** |

## Revision plan (in recommended order)

1. **Reinstate or retire the dropped tables (C2).** This is the root cause and it gates C1, C3, C4, C5. For each of `power_mde.tex`, `balance_player_b.tex`, `reg_delegation_robustness.tex`, decide: back into the build, or the dependent claim comes out.
2. **Fix the equivalence claim (C1).** Report the TOST with its ±£0.20 bound stated plainly, or drop "alike" and "cannot shift blame" for Result 2's own wording. This is the sentence a referee will quote.
3. **Correct the H2 interaction (C3).** Report the linear combination, relabel the DiD, resolve the line-48 / line-54 contradiction.
4. **Report Player B balance and narrow the justification (C4).**
5. **Test the mechanism claim (C5)** — treatment × performance interaction — and fix the overconfidence numbers to match the code definition.
6. **Downgrade the causal cross-study language in the intro (C6).** Smallest edit, high referee risk.
7. **Clean the bibliography (C7)** and repoint `/validate-bib` at the file the manuscript actually uses. Delete `stein_dont_2020`.
8. **Remove the `\hl` placeholder (C8)**, then the prose MAJORs (M16, M18) and the abstract's missing contribution and selection result (M4, M5).

## Contradictions between lenses

- **Lens 5 vs the author's own analysis on order effects.** Lens 5 characterized the commented-out order effect as showing "the reversal is largely confined to one order arm", derived by back-calculating cell shares. The commented paragraph itself reports the treatment × order interaction at p=0.115, non-significant, which `numbers.json` confirms (`order_logit_interaction_p = 0.115`). The defensible finding is that a real order effect went unreported, **not** that the headline result is an order artifact. Recorded here so the stronger claim does not propagate.
- **Lens 3 vs Lens 6 on how much work remains.** Lens 6 judges that fixing its criticals reaches ~9/10 "without touching substance"; Lens 3 finds the identification claims outrun the design. Both are right within scope. The prose is in better shape than the inference.
- **Lens 2 vs Lens 1 on the mechanism paragraph.** Lens 2 wants it moved after the contributions, not cut; Lens 1 wants a contribution sentence added to the abstract. These are compatible.
- **No M3 over-commitment found.** Lens 5 examined the mechanisms section specifically and reports it is even-handed and explicitly demotes process ownership. The existing skepticism about M3 appears already reflected in the draft.

## Notes on this run

- `domain-reviewer.md` still carries its `AUTO-DETECT-TEMPLATE-MARKER` and is written for lecture slides. Lens 3 used an experimental-economics adaptation, not the shipped template. Customizing that agent would make future runs of this skill and `/review-paper --peer` materially better.
- `proofreader.md` is likewise slide-oriented; Lens 6 used an adapted manuscript version.
- Scholar Gateway and Consensus connectors were unauthorized in this session, so Lens 7 verified via general web search and flagged what it could not confirm.
- All CRITICAL findings in this synthesis were independently verified against source files or `numbers.json` before being recorded.
