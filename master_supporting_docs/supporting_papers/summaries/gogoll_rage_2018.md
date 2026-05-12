---
title: "Rage Against the Machine: Automation in the Moral Domain"
authors: Jan Gogoll, Matthias Uhl
venue: Journal of Behavioral and Experimental Economics
year: 2018
volume: 74
pages: 97–103
doi: 10.1016/j.socec.2018.04.003
bibtex_handle: gogoll_rage_2018
pdf: ../gogoll_rage_2018.pdf
relevance_to_manuscript: high — defines the "moral domain" framing used in design.tex; cited in lit.tex ¶19, 21 and design.tex ¶39
---

# Gogoll & Uhl (2018) — *Rage Against the Machine*

## Research question

Do people exhibit algorithm aversion specifically in the **moral domain** — i.e., when the delegated task affects a third party — and if so, **why?** The authors test two standard candidate mechanisms: (i) perceived utility / competence and (ii) trust.

This is the paper that coined the term "moral domain" in this literature, defined as decisions imposing indirect costs or benefits on an uninvolved third party.

## Methods

- **Lab experiment**, German university, Sept 2015, z-Tree + ORSEE. *n* = 264 subjects across 12 sessions. Plus 48 subjects in two preparatory sessions for calibration.
- **Part 1 — Delegation in the moral domain.** Subjects assigned the calculation task (count specific patterns in 10 puzzles). Half are *actors*, half are *observers*. Actors play three roles consecutively:
  - As **delegator**, must choose between delegating the task to another human or to a machine. **No option to do the task themselves** — this strips out the loss-of-control confound that's normally bundled into algorithm aversion.
  - As **task-solver**, solve the task themselves (this generates the data used for matching others' delegations).
  - As **third party**, receive payoff from someone else's task solution.
- **Algorithm calibration:** machine is programmed to reproduce *exactly* the empirical error distribution of human task-solvers from preparatory sessions. Equal performance is therefore baked in.
- **Observers** reward / punish the delegator with up to 70 ECU in each of four (delegate-type × outcome) cells, strategy method.
- **Part 2 — Perception of errors.** Subjects guess number of red-marked (incorrect) exercises in 240 shown for humans vs machine. Equal error counts, but subjects' guesses tested for biased perception.
- **Part 3 — Trust game.** Standard two-player trust game with multiplier of 3; subjects play against either a human partner or a machine (programmed with reciprocation profiles from preparatory subjects).

## Key results

**Result 1 — Strong aversion to delegating to a machine.** Of 132 delegators, only 26.5% chose the machine; 73.5% chose another human. Significantly below 50% (*p* < 0.001).

**Result 2 — Observers reward machine-delegators less.** Whether the task succeeded or failed:
- Successful outcome: human-delegator rewarded 17.77 ECU vs machine-delegator 12.52 ECU (*p* < 0.001).
- Failed outcome: human-delegator rewarded 4.42 ECU vs machine-delegator 0.49 ECU (*p* = 0.002).

The aversion shows on both the principal side (don't delegate to machine) and the observer side (punish machine-delegation).

**Result 3 — Machine errors not perceived as more frequent than human errors.** Estimated error counts: machine 58.11, human 59.84 (*p* = 0.63). The aversion is **not** explained by misperceived competence.

**Result 4 — Trust in machine ≈ trust in human.** Trust-game transfers: 30.83 ECU to machine vs 33.64 to human (*p* = 0.17). The aversion is **not** explained by lower generalised trust.

**Post-experimental survey (n = 78):** Five alternative explanations tested (contempt for human effort, blame/praise attribution bias, responsibility-passing limits). None decisively supported either. The authors conclude: machine aversion in the moral domain is an "aversion per se," not reducible to standard mechanisms.

## Main takeaways

1. **Algorithm aversion is strong and observable on both sides** when third-party welfare is at stake. People don't delegate to machines in the moral domain and observers punish those who do.
2. **Perceived utility / competence does not explain it** — error rates are equal and known.
3. **Trust does not explain it.** Trust-game behaviour is equivalent toward humans and machines.
4. **The mechanism is unexplained by standard candidates**, leaving an "aversion per se" residual that the authors flag for future research.
5. The paper is widely cited as evidence that algorithm aversion *amplifies* in moral-domain settings, contrary to "neutral" tasks like forecasting where Logg et al. find appreciation.

## Relation to "Algorithms and Responsibility" (this manuscript)

Gogoll & Uhl is cited in [literature.tex](../../../manuscript/literature.tex) paragraph 19 (algorithm aversion in moral domain) and paragraph 21 (third-party welfare amplifies aversion). It's also cited in [design.tex](../../../manuscript/design.tex) paragraph 39 — but the manuscript flags an issue there ("FB CHECK: Verify that Gogoll & Uhl (2018) actually support the math-task scepticism contrast"). Reading the paper: the math-task framing is *implicit* — Gogoll & Uhl note that subjects might be sceptical that algorithms could ever fail at purely mathematical tasks, which is why they used a calculation task with deliberately reproduced error patterns. The manuscript's claim is therefore *defensible* but not explicit in the Gogoll text; the FB CHECK can probably be resolved by softening the citation to "as motivated by".

**Why this paper matters for the manuscript:**

**(1) The moral-domain framing comes from here.** The manuscript defines its task as falling within the moral domain (design.tex ¶82): "Player A's choice imposes monetary externalities on a matched recipient, and a poor decision causes real, albeit modest, monetary harm." This is essentially Gogoll & Uhl's definition. Anchoring the manuscript in this tradition is important for situating it relative to "neutral" forecasting tasks (Logg et al. 2019).

**(2) Equal-performance calibration is borrowed from here.** Gogoll & Uhl programme the machine to reproduce the empirical human error distribution at the *session* level. The manuscript improves on this by calibrating at the *individual* level (Bernoulli at each Player A's accuracy). The manuscript's design innovation is therefore a sharpening of Gogoll & Uhl's approach — and one that closes the signal-extraction channel that session-level calibration still leaves open. This is a useful design-pedigree point.

**(3) Gogoll & Uhl's "aversion per se" residual is what the manuscript's M3 mechanism tries to explain.** When the standard mechanisms (utility, trust, perceived competence) are ruled out, what's left? Gogoll & Uhl flag the question; the manuscript's M3 (process ownership / identity / accountability salience) is a candidate answer. This is worth making explicit in the discussion section: "The manuscript's M3 mechanism is offered as a candidate explanation for the 'aversion per se' residual that Gogoll & Uhl (2018) identify."

**(4) The strong machine-aversion finding here (26.5% delegate) contrasts with the manuscript's near-50% rates.** Two design differences matter:
- Gogoll & Uhl force subjects to delegate (no own-task option); manuscript allows direct decision.
- Gogoll & Uhl observers punish machine-delegators directly; the manuscript's observers (Player B) do not differentially punish (Result 2).
- The manuscript's individual-level calibration may produce stronger machine acceptance than session-level calibration in Gogoll & Uhl.

The lower delegation rates in Gogoll & Uhl are consistent with a stronger "moral domain" aversion than the manuscript identifies. This is worth flagging in the discussion: the manuscript's prediction task may be on the *edge* of the moral domain — outcomes affect a third party, but the underlying decision is uncertainty-based and well-aligned with the recipient's interests. The "moral domain" status of the task in the manuscript is therefore weaker than in Gogoll & Uhl, which probably explains the higher delegation rates.

**(5) The post-experimental survey approach (ruling out alternative mechanisms) is a methodological template.** The manuscript's mechanism section (M1/M2/M3 in section 4) does something similar — testing punishment beliefs, performance heterogeneity, etc., to rule out alternative readings of the H1 reversal. This is a defensible approach with precedent in this literature.

**Where in literature.tex:**

- Paragraph 19 introduces it correctly as evidence that moral-domain delegation is averted.
- Paragraph 21 cites it as part of the moral-domain subsection, also correctly.
- Design.tex paragraph 39 — the "math-task scepticism" framing needs slight softening; the original text supports it implicitly but doesn't state it. Suggest: "as motivated by Gogoll & Uhl (2018), who deliberately chose a calculation task in part because the math-task framing leaves room for algorithmic error."

**Worth borrowing:** Gogoll & Uhl's "aversion per se" framing is rhetorically useful. The manuscript could frame its M3 result as: "Where Gogoll & Uhl (2018) identified an unexplained residual of aversion to algorithms in the moral domain, we identify a candidate mechanism — accountability salience under process ownership — that the punishment manipulation isolates."
