# Desk Review: Algorithms and Responsibility

**Calibrated to:** American Economic Review (AER)
**Date:** 2026-05-01
**Paper:** manuscript/main.tex
**Novelty check:** ON (Post-Flight verification: SKIPPED — flagged for manual cross-check)

## Verdict

**SEND OUT — with reservations**

Borderline desk-reject on three vectors (Phase-0 reproducibility, statistical fragility of the headline test, unresolved placeholders), but the design is genuinely original (individual-level algorithm calibration, punishment-off treatment) and the contradicted-H1 finding is the kind of signal that AER readers want to see if it survives scrutiny. I'm sending out, but the editorial decision will lean hard on the methods referee's judgment about whether $n = 161$ Player As supporting a $p = 0.049$ headline is enough for an AER lead.

## One-paragraph contribution statement (my understanding)

The authors run a preregistered online experiment ($N = 322$, UK Prolific) in which a decision-maker (Player A) makes a payoff-relevant prediction for a second party (Player B) and may delegate to an algorithm calibrated, at the individual level, to her own performance. Between subjects, they switch off Player B's ability to punish. Two findings: (i) introducing the punishment possibility *reduces* delegation by 17 pp — the opposite of what the responsibility-avoidance literature predicts; (ii) punishment is essentially outcome-based, with no significant differential between delegated and self-made decisions. The contribution is therefore both a reversal of an established prediction in a new (algorithm-mediated) setting and a behavioural microfoundation for accountability-based AI regulation (EU AI Act).

## Desk-reject analysis (considered, not invoked)

I considered desk-rejecting on the following grounds and declined for the reasons stated:

- **Reproducibility FAIL (Phase 0).** No analysis pipeline exists. Per AER's Data and Code Availability Policy this would block acceptance. **Why I didn't desk-reject:** the issue is fixable in a 1–2 week pre-submission sprint, and the paper's intellectual content is independent of pipeline existence. Flagged in the editorial decision as a MUST-fix before resubmission.
- **Below the bar (statistical power).** The headline H1 test is $\chi^2$ $p = 0.049$ on $n = 161$. **Why I didn't desk-reject:** the *direction* of the result is the contribution, not the precision. AER does publish reversal-of-prediction papers, and a follow-up wave to tighten the estimate is a reasonable Major Revision ask.
- **Unresolved placeholders.** `[ZZ]`, `[CITE]`, `[VERIFY]`, `[Future analysis …]` markers throughout main text. **Why I didn't desk-reject:** these are mechanical and indicate a working draft, not a submission. I'm reviewing as if this were a pre-submission consultation, which is what the author has asked for.

## Novelty probes

Novelty check skipped per Post-Flight verification rule (cannot run WebSearch in this orchestration environment without claim-verifier). Editor's prior on novelty of the specific design:

| Probe | Query (would have run) | Editor's prior |
|---|---|---|
| 1 | "algorithm delegation responsibility experiment 2024" | Likely overlap with Feier et al. 2022 (cited & differentiated) and possibly Maasland & Weißmüller 2022 (in bib but lightly engaged) |
| 2 | "punishment delegation algorithm Prolific" | Authors should verify no near-cousin in *Mgmt Sci*, *JESA*, or *Exp Econ* 2023–2025 |
| 3 | "individual-level algorithm calibration responsibility" | The individual-level calibration is the authors' design innovation; should be safe |

**Recommended manual cross-check:** *Management Science* 2023–2025 issues; ESA / WEAI 2024 conference programs; SSRN working papers tagged "algorithm aversion".

## AER style violations flagged

- **Significance stars in Tables 1 and A2.** AEA policy since 2018 (per CLAUDE.md, since 2023 per journal profile — both pre-current). Strip and report exact $p$-values in notes.
- **`\bibliographystyle{chicago}`.** Use `aer.bst` for AER submission.
- **Figures are PNG.** AEA Production prefers PDF/EPS. Production-stage issue.

## Send-out plan

Proceeding to Phase 1b (referee selection) and Phase 2 (parallel referees, blind to each other).

---

## Referee Selection

Drawing from AER referee-pool weights (CREDIBILITY 0.30, POLICY 0.25, STRUCTURAL 0.15, MEASUREMENT 0.15, SKEPTIC 0.10, THEORY 0.05).

**Draw 1 (without replacement):** CREDIBILITY (top of pool).
**Draw 2 (re-normalized, CREDIBILITY removed):** POLICY (0.25/0.70 = 0.357, top of remainder).

Cognitive diversity check: PASS — CREDIBILITY pushes on whether $p = 0.049$ on $n = 161$ is identification-enough; POLICY pushes on whether the EU AI Act framing actually generalises beyond UK Prolific subjects. These are orthogonal lenses.

| Referee | Disposition | Critical peeve | Constructive peeve |
|---|---|---|---|
| Referee A (domain) | POLICY | "External validity: would this replicate in a different country / time / population?" | "Rewards unit-economics discussions (what does this translate to in policy terms?)" |
| Referee B (methods) | CREDIBILITY | "Power calculations required for null results." | "Gives credit for explicit pre-registration when relevant." |

**Paper type for methods referee:** Survey-experiment (per `methods-referee.md` taxonomy added in v1.8.0).
