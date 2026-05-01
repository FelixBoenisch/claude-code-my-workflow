# Editorial Decision: Algorithms and Responsibility

**Calibrated to:** American Economic Review (AER)
**Date:** 2026-05-01
**Decision:** **Major Revision** (per decision-rule table — but see editor's note below: this is closer to "Reject without prejudice" than to a routine R&R)

## One-paragraph editor's assessment

This is a well-designed single experiment with a publication-worthy headline finding (the H1 reversal) supported by a genuinely innovative design feature (individual-level Bernoulli calibration of the algorithm). Both referees, working from disjoint priors and blind to each other, converge on the same diagnosis: the design ideas are AER-quality, but the statistical execution and the empirical-base-to-claim ratio are not. The paper currently asks AER readers to update toward a new behavioural microfoundation for AI accountability regulation on the basis of one $n = 161$ between-subject test at $p = 0.049$, a mechanism inferred from a 60-subject sub-cell, and no replication package. Per the strict decision-rule table (0 FATAL, 9 ADDRESSABLE → Major Revision), I am not desk-rejecting; but I want to be transparent that the volume of work needed before AER resubmission is closer to "new wave of data + complete pipeline + paper restructure" than to a typical R&R. The author should weigh whether to invest that work for AER specifically or to redirect to a top-field venue (JEEA, JPubE, Management Science, Experimental Economics) where the paper as-revised would be a strong submission.

## Referee summary

- **Referee A (POLICY):** score 65/100. Reject (with encouragement). External-validity gap is first-order for AER's general-interest bar; policy claims are not earned by a single UK Prolific weight-prediction game.
- **Referee B (CREDIBILITY):** score 64/100. Major Revision. H2 null without power calc, borderline H1 $p$, unresolved PAP deviation, missing attrition table, missing replication package — all fixable, but cumulatively past AER's methods bar in current form.

Composite editor view: both referees land in the 64–65 range, which is the **Reject** band per their respective rubrics. The decision rule lifts to Major Revision because the concerns are all ADDRESSABLE in principle. I want the author to take that lift with eyes open about its size.

## Concern classification

### FATAL

None. No referee concern is unfixable in principle. The closest to fatal is the external-validity / generalisation gap (Domain C1), which cannot be addressed with the existing data — but the author can address it with new data or by tightening claims.

### ADDRESSABLE

| # | Concern | From | Suggested path |
|---|---|---|---|
| A1 | External validity is asserted, never tested | Domain C1 | Either (a) one out-of-sample replication (different country / domain), or (b) substantial scope reduction in abstract / conclusion; current EU AI Act framing is not earned |
| A2 | No magnitudes in policy-relevant units — the "so what" is missing | Domain C2 | Unit-economics paragraph in Discussion: calibrate 17pp shift against external benchmarks (physician AI adoption elasticity, loan-officer reluctance under audit), or vary stakes within the experiment, or back-of-envelope cost-benefit |
| A3 | Mechanism rests on 60-subject regression | Domain C3 | Either (a) direct test of process ownership (e.g., visibility-to-Player-B treatment), or (b) reframe M3 as "candidate hypothesis" rather than "most consistent reading" — adjust intro and conclusion to match |
| A4 | Contribution over-claimed vs Feier et al. | Domain C4 | Engage substantively with the sign discrepancy: which design feature drives the reversal? Ideally test by adding session-level-calibration arm; minimally, claim a tighter contribution |
| A5 | H2 null reported with no power calculation | Methods C1 | MDE for paired test at achieved $n$; TOST equivalence test; CI framing on the delegation effect |
| A6 | H1 sample-size justification absent; headline $p$ borderline | Methods C2 | Ex-ante power calc; explicit one-sided/two-sided justification; bootstrap or randomization-inference $p$; promote logit-with-controls into headline |
| A7 | Preregistration deviation unresolved on the page | Methods C3 | Resolve `[CHECK]` placeholder in `results.tex:15`; cite PAP by registry ID; appendix table of all PAP deviations and rationale |
| A8 | Attrition by arm not reported | Methods C4 | CONSORT-style flow diagram; one-sentence re-matching rule; Lee bounds if attrition differs >5pp across arms |
| A9 | Replication package does not exist | Methods C5 | Complete `scripts/python/` pipeline producing every numeric claim; `\input{}` table fragments per project SSOT rule; `/audit-reproducibility` PASS before resubmission |

### TASTE (author may push back)

None. Both referees disciplined themselves into providing concrete "What would change my mind" criteria for each major concern. There is nothing in either report that I would mark as defensible-by-rebuttal-alone.

## Where referees disagreed

### Disagreement 1: Recoverability and disposition

- **Domain (POLICY)** voted Reject because the external-validity and policy-magnitude gaps are not patchable without new data. Reading the conclusion's gesture toward an efficiency-vs-accountability trade-off as "the seed of a real policy contribution... that currently sits as a closing reflection rather than as a result."
- **Methods (CREDIBILITY)** voted Major Revision because every concern listed is operationally fixable. Reads the design ideas as AER-quality and the execution as the gap.
- **Editor's view:** Both are right. Methods is correct that no single concern is unfixable; Domain is correct that the *cumulative* size of the fix exceeds the implicit "revise" envelope. I split the difference by issuing Major Revision per the rule but flagging in the editor's note that this is closer to "Reject without prejudice" — a signal to the author that the resubmission must be near-rewrite quality, not patch-quality.

### Disagreement 2: Weight on the replication-package gap

- **Methods** flagged as MAJOR (Concern 5).
- **Domain** noted only in minor suggestions (alongside placeholders).
- **Editor's view:** Methods is right. AER's Data and Code Availability Policy is not waivable; the gap is structural and not stylistic. This is a load-bearing MUST.

### Disagreement 3: Weight on the mechanism (M3 process ownership) story

- **Domain** treats the thinness of M3's empirical support as a substantive contribution problem (Concern 3) — "we found something we can't readily explain, and process ownership fits" is a different and weaker contribution than the paper currently advertises.
- **Methods** does not push hard on M3 specifically; treats it as a downstream issue from the broader power problem.
- **Editor's view:** Domain is right that the mechanism story is currently over-sold relative to its evidence. The cleanest fix is rhetorical (re-framing in intro and conclusion); the gold-standard fix is a new treatment arm directly testing process ownership.

### Disagreement 4: Whether the AER's POLICY reading is fairly applied

- **Domain** reads the EU AI Act framing as a substantive over-reach the paper has not earned.
- **Methods** does not engage with the policy framing at all (correctly — out of scope).
- **Editor's view:** Domain is right that the framing is over-reached. The author has two paths: shrink the framing to a behavioural mechanism contribution (and accept that this changes the journal target), or do the work to earn the framing (replication, magnitude calibration). Either is honest; the current text is neither.

## Response-planning block (for the author)

**MUST address (every ADDRESSABLE concern, in order of leverage):**

1. **A9 (replication package).** Build the pipeline. Without this, no resubmission anywhere should happen. This is also the highest-leverage fix because it produces evidence against several other concerns (A5, A6) automatically.
2. **A7 (preregistration deviation).** Resolve the one-sided/two-sided issue in-text, not in a `[CHECK]` placeholder. Cite the PAP. List deviations.
3. **A5 + A6 (power and headline-$p$ rigour).** Compute MDE, TOST, ex-ante power. Re-frame H2 with CIs.
4. **A8 (attrition by arm).** CONSORT diagram. Re-matching rule. Lee bounds if needed.
5. **A1 + A4 (external validity / over-claiming).** This is the journal-fork moment. Either commit to a second wave (different country, different domain), or substantially shrink claims and redirect.
6. **A2 (policy magnitudes).** Unit-economics paragraph. The conclusion already gestures toward this; pull it forward and quantify.
7. **A3 (mechanism re-framing).** At minimum: re-write intro and conclusion to position M3 as a candidate hypothesis. Better: a new treatment arm.

**SHOULD address:**

- All `[ZZ]`, `[CITE]`, `[Future analysis…]`, `[VERIFY]` placeholders in the manuscript. Any one of these in a submitted draft would be flagged by an AER desk editor.
- AEA style: strip significance stars from Tables 1 and A2; switch `\bibliographystyle{chicago}` to `aer.bst`; convert PNG figures to vector PDF/EPS for production.
- Player B balance table moved from "available on request" into the appendix.
- Figure-1 treatment-overview ("Baseline: punishment / Treatment: no punishment") naming reconsidered — both referees noted the cognitive load of reversed Baseline/Treatment labels in passing; renaming to Punishment/No-Punishment throughout would be consistent with usual experimental conventions.

**MAY push back:**

Nothing in either referee report is purely TASTE. Both referees were disciplined about providing falsification criteria. The author can push back on individual "What would change my mind" asks (e.g., "we believe a power calculation is sufficient without TOST"), but the underlying concerns are not contestable.

## Path-forward summary

There are realistically three paths from here:

**Path 1 — AER resubmission (high investment, ~6–12 months work).** Build pipeline. Run a second wave (US Prolific or vignette study in a different domain). Add power and equivalence tests throughout. Add policy-units calibration. Re-write intro and conclusion. Re-frame mechanism. Resubmit as effectively a new paper with a stronger evidence base. Probability of acceptance conditional on doing this work: meaningful but not high — the AER bar is unforgiving and the original-finding-direction is contested by Feier et al.

**Path 2 — Top-field redirect (moderate investment, ~3–6 months work).** Build pipeline. Resolve PAP, attrition, power. Tighten policy claims to behavioural mechanism. Submit to JEEA, JPubE, Management Science, or Experimental Economics. The paper as-revised would be a strong submission to any of these. Probability of acceptance: high.

**Path 3 — Stay-as-is and submit somewhere else (low investment).** I do not recommend this; the placeholder count and the missing pipeline would draw a desk-rejection at any reputable venue.

The editor's strong recommendation is Path 2, with the option to upgrade to Path 1 if the second-wave data come in clean and the magnitudes calibrate well.

---

**Reports in this pipeline:**
- `quality_reports/cross_artifact_algorithms_and_responsibility/reproducibility.md` — Phase 0
- `quality_reports/peer_review_algorithms_and_responsibility/desk_review.md` — Phase 1 + 1b
- `quality_reports/peer_review_algorithms_and_responsibility/referee_domain.md` — Phase 2 (POLICY)
- `quality_reports/peer_review_algorithms_and_responsibility/referee_methods.md` — Phase 2 (CREDIBILITY)
- `quality_reports/peer_review_algorithms_and_responsibility/editorial_decision.md` — Phase 3 (this file)
