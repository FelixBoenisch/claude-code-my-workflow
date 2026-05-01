# Domain Referee Report

**Calibrated to:** American Economic Review (AER)
**Disposition:** POLICY
**Critical peeve:** External validity — would this replicate in a different country / time / population?
**Constructive peeve:** Rewards unit-economics discussions (what does this translate to in policy terms?)
**Date:** 2026-05-01
**Paper:** `manuscript/main.tex` ("Algorithms and Responsibility", Bönisch)

## Executive verdict

**Score:** 62 / 100
**Recommendation:** Reject (with strong encouragement to resubmit after substantial revision; not desk-reject — the question is real)
**Headline:** A genuinely interesting reversal of the standard responsibility-shifting result, but the contribution is currently sized for a field journal, not the AER: a single 322-subject UK Prolific session with no policy-relevant magnitudes, no replication, and a mechanism inferred from a 60-subject sub-cell.

## Dimension scores (with AER adjustments applied: Contribution 30→35, External validity 15→20, Fit 10→5)

| # | Dimension | Weight | Score | Weighted |
|---|---|---|---|---|
| 1 | Contribution & Novelty | 35% | 70 | 24.5 |
| 2 | Literature Positioning | 25% | 78 | 19.5 |
| 3 | Substantive Arguments | 20% | 60 | 12.0 |
| 4 | External Validity | 20% | 30 | 6.0 |
| 5 | Fit for AER | 5% | 55 | 2.75 |
| | **Composite** | 100% | | **64.75 / 100** |

Rounded composite: **65** (boundary between Reject and Major Revision under the rubric). I land on **Reject** because, for the AER specifically, the external-validity gap and the policy-units gap are first-order, not patchable in revision without new data.

## Major concerns (each with "What would change my mind")

### Concern 1: External validity is asserted, never tested

**Dimension:** 4 (External Validity)
**Severity:** MAJOR
**Description:** The entire empirical foundation is one online session of 322 UK Prolific workers run February–June 2023. The paper makes large-scope claims — about regulatory frameworks (EU AI Act), about "the design of accountability regimes governing algorithmic decision-making", about whether holding humans accountable "disciplines algorithmic adoption" — but the evidence base is a weight-from-photo prediction task in one country, one platform, one labour-market sample, one moment in time. The Limitations paragraph (conclusion.tex line 13) acknowledges UK Prolific narrowness in a single sentence and moves on. There is no replication, no robustness across populations, no comparison to a different decision domain (medical, judicial, hiring — the very domains the introduction names), and no demonstration that the effect survives outside the specific calibration story used here.

**Why this matters:** The AER's bar is "the topic must matter beyond specialists." A finding from a UK convenience sample on a single weight-prediction task does not, on its own evidence, license claims about EU regulatory design. Either the paper needs more evidence or the claims need to shrink dramatically.

**What would change my mind:** A second, independent study — different country (US Prolific, MTurk, or a CloudResearch panel are minimum viable; a representative-sample replication would be ideal), different decision domain (e.g. a medical-triage or hiring vignette), or both — that recovers the qualitative direction of Result 1 (punishment-possibility reduces delegation). Alternatively, recruiting an existing collaborator dataset or running a meta-analysis-style aggregation across the closest 3–5 published designs (Feier-Powell-Hetschko 2022, Kirchkamp & Strobel 2019, plus close cousins) and showing the sign aligns. Without one of these, the policy framing in Section "Implications" must come out.

### Concern 2: No magnitudes in policy-relevant units — the "so what" is missing

**Dimension:** 1, 4 (Contribution, External Validity)
**Severity:** MAJOR
**Description:** The paper reports a 17 percentage-point reduction in delegation (42.5% vs 59.3%) and frames it as a behavioural complement to the EU AI Act. But what does 17pp of "delegation to a weight-from-photo algorithm in a £5 stake game" translate to in any consequential setting? There is no back-of-envelope on what this would mean for, e.g., physician adoption of diagnostic algorithms under malpractice exposure, loan-officer adoption of credit-scoring under fair-lending audit, or judge use of risk-assessment tools under appellate review. The policy claim — "accountability regimes are a behavioural lever for algorithm use, not just for moral attribution" — is assertion, not inference: the magnitude of the lever is unestimated and the elasticity to stakes is untested. A POLICY referee at the AER reads "behavioural lever" and asks: how big a lever, on what margin, at what cost? The paper has none of these.

**Why this matters:** AER readers in adjacent fields (labour, health, IO, public, law-and-econ) need to be able to translate a finding into their own terms within one paragraph of reading. As written, the paper offers them no purchase. The conclusion's gesture toward a sharper-than-recognised efficiency-vs-accountability trade-off is exactly the right framing — but it is asserted as a takeaway, not produced as a result.

**What would change my mind:** A unit-economics paragraph in the Discussion that does at least one of: (a) calibrates the 17pp shift against an external benchmark — e.g. estimated elasticities of physician AI adoption to liability exposure, or surveyed physician/loan-officer reluctance under audit; (b) varies stakes within the experiment (the £5 stake is plausibly trivial — does the effect grow, shrink, or vanish at £50, or in a hypothetical scenario design?); (c) provides a back-of-envelope cost-benefit framing of "accountability deters adoption" in one named application. Without this, the paper is honest about what it found in its game but cannot earn the policy claim.

### Concern 3: The headline mechanism rests on a 60-subject regression and a single behavioural moment

**Dimension:** 3 (Substantive Arguments)
**Severity:** MAJOR
**Description:** The "process ownership" mechanism (M3) — which is the paper's substantive theoretical contribution beyond "we found a sign reversal" — leans on three pieces of evidence: (i) the heterogeneity result that better performers in Baseline delegate less (Pearson r = -0.19, p = 0.092 — a one-tailed p of marginal significance), (ii) the regression in Column (3) of Table tab:del_decision_determinants, which is identified off N=60 in the Baseline sub-sample, and (iii) the effort comparison among non-delegators (45.5% vs 21.7% high-payoff rate, with no significance test reported on this comparison in the manuscript text). This is a thin reed for what the abstract calls "the most consistent" mechanism. The paper rules out M1 (anticipated punishment) and M2 (effort to outperform algorithm) cleanly, and explicitly cannot rule out M4 (experimenter demand). M3 is then offered as the residual interpretation. "It's the one we couldn't kill" is not the same as "it's the one the data support."

**Why this matters:** A non-specialist AER reader is asked to update toward a process-ownership theory of algorithm use on the basis of a sub-cell heterogeneity pattern that approaches conventional significance only one-tailed. The substantive claim that the paper makes — that this finding refines the responsibility-avoidance literature — is only as strong as the mechanism story. If the mechanism story is "we found something we can't readily explain, and process ownership fits", that is a different and weaker contribution than the paper currently advertises.

**What would change my mind:** Either (a) a direct test of process ownership — e.g. a treatment in which Player A is told her decision will be invisible to Player B, removing the moral-spectator channel while keeping accountability nominal; or (b) honest re-framing of M3 as a candidate hypothesis rather than the modal interpretation, with the introduction and conclusion adjusted accordingly. The current text repeatedly calls process ownership "the most consistent" reading of the data; a referee skeptical about external validity also wants the mechanism claims to be calibrated to the evidence available.

### Concern 4: The contribution is over-claimed relative to closest precedents

**Dimension:** 1 (Contribution & Novelty)
**Severity:** MAJOR
**Description:** The paper positions itself against Feier, Powell-Hetschko (2022) on three margins: individual-level vs session-level calibration, separated subject pools for delegator/evaluator, and the on/off punishment manipulation. These are real design improvements. But the substantive contribution claimed in the abstract and conclusion is broader: a behavioural complement to AI Act-style regulation, evidence on responsibility-avoidance limits in algorithmic settings, and a refinement of the standard story to include process ownership. None of these broader claims have been independently established outside this single experiment, and the closest precedent (Feier et al.) is from a different country, different task, different elicitation, and reaches a partly opposed conclusion. A POLICY-disposed AER reader wants to see: under what conditions does the new finding hold, and under what conditions does the old finding hold? The paper does not answer this. The "Where this paper fits" subsection in literature.tex (line 31–33) catalogues design improvements but does not engage with the substantive question of why the sign should differ.

**Why this matters:** A general-interest journal needs to see a contribution that survives a sympathetic editor's question "what should I tell a colleague in another field about this paper?" The honest answer here is "Bönisch ran a clean preregistered design and found a sign reversal in the responsibility-avoidance literature when the intermediary is an algorithm." That is publishable — but at JEEA, JEBO, Experimental Economics, or possibly Management Science, not AER.

**What would change my mind:** A serious engagement with the discrepancy between this paper's findings and Feier et al.'s. A concrete claim about which design feature drives the sign reversal, ideally tested directly by varying that feature within the new experiment (e.g. running session-level calibration as an additional arm). Or evidence from at least one additional context that the headline finding generalises. Without one of these, "preregistered single-shot reversal in a UK Prolific weight-prediction game" is the honest size of the contribution.

## Minor suggestions

- Multiple unresolved placeholders dilute the manuscript's submission-readiness signal: `[ZZ]` for Player A and Player B earnings (design.tex line 31, results.tex line 7), `[ZZ%]` for Player A attention-check pass rate (results.tex line 11), `[CITE: which MPL?]` for risk preference elicitation (design.tex line 49), `[CITE/SPECIFY]` for Prolific quality screens (results.tex line 7), `[Future analysis: ...]` placeholders in results.tex lines 66 and 102 and appendix.tex line 70, plus unconstructed TikZ timeline figures in appendix.tex lines 80 and 87. None of these are substantive concerns on their own; collectively they signal the manuscript is not yet at submission state.
- The acknowledgements footnote on the title page is empty. AER expects this filled in at submission for declaration purposes.
- The footnote on results.tex line 15 explicitly flags an unresolved methodological choice: pre-registration specifies one-sided tests in the H1 direction, but H1 was rejected with the wrong sign — under preregistration this means a one-sided test fails to reject, and the paper currently reports two-sided p-values. This needs a clean disclosure of what was preregistered, what is reported, and why. Strictly speaking, this is methods territory; I flag it because the substantive claim ("punishment reduces delegation, p = 0.049") rests on it.
- The £5/£1 high/low payoff for Player B and £0–£2 punishment range translate to very small absolute stakes. A line in the Limitations on stake-magnitude generalisation would help.
- Sample size: 322 total, 161 Player As across two arms = ~80 per arm. This is fine for the headline test but very thin for the Baseline-only mechanism analysis (60 after exclusions). The conclusion already mentions scaling up; a sentence on the minimum-detectable-effect for the Result 2 null would discipline the "punishment is essentially outcome-based" claim.
- The introduction frames the navigation-app example beautifully but the paper's actual setting (predicting a stranger's weight from a photo to determine a stranger's £5 payoff) is a long way from any application a regulator would care about. The framing would be more honest if the introduction signposted this gap rather than gliding past it.

## Positive observations

1. **The reversal of H1 is a genuinely interesting empirical finding.** The standard reading of Bartling–Fischbacher and the responsibility-avoidance literature would have predicted exactly the opposite direction. A clean, preregistered experiment finding the opposite sign is the kind of empirical result that should not be filed away — it forces the literature to update its prior, and the author deserves credit for designing a setting in which the prior could be falsified.
2. **The individual-level algorithm calibration is a real methodological contribution to this experimental literature.** It removes the relative-performance signalling confound that has plagued previous designs (especially Feier et al.), and it does so in a way that is transparent to subjects and operationally simple. This is the right kind of design improvement: it sharpens what the data can tell us, rather than papering over the confound with controls.
3. **The constructive-peeve acknowledgement** — the conclusion's framing of an efficiency-vs-accountability trade-off — is exactly the kind of unit-economics discussion this referee rewards. The paper notices that "in domains where algorithms genuinely outperform humans, holding humans liable for outcomes may push decision-makers away from the more accurate technology." That sentence is the seed of a real policy contribution. The problem is that it currently sits as a closing reflection rather than as a result; pulling it forward and calibrating it (Concern 2) would meaningfully strengthen the paper.
4. **Honest mechanism analysis.** The author considers four candidate mechanisms, rules two out cleanly with the data, acknowledges that M4 (experimenter demand) cannot be ruled out, and arrives at M3 by elimination rather than confirmation. Many manuscripts in this space would have asserted M3 as established. The manuscript's hedging here is appropriate; my Concern 3 is about whether even the hedged reading is supported, not about the hedging itself.

---

**Bottom line for the editor.** This is a well-designed single experiment with a publication-worthy headline finding. It is not, on the evidence currently in the manuscript, an AER paper: the contribution is sized for a top-field journal. A revised version that (a) adds at least one out-of-sample replication or systematic robustness across populations/tasks, (b) calibrates the magnitude in policy-relevant units, and (c) softens the mechanism claim to match the available evidence could plausibly clear the AER bar at a future submission. As submitted, my recommendation is Reject with encouragement to resubmit after the additional evidence is collected, or to redirect to a top-field venue (JEEA / JPubE / Management Science / Experimental Economics) at the author's preference.
