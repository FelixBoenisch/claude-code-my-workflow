# Literature Review — Algorithms, Responsibility, and Delegation

**Date:** 2026-05-02
**Query:** Full-fledged literature review for the "Algorithms and Responsibility" paper
**Scope:** four interlocking strands: (i) responsibility avoidance through delegation; (ii) algorithm aversion and adoption; (iii) responsibility attributions to algorithm-mediated decisions; (iv) theoretical microfoundations (psychological ownership, identity, moral self-image, demand-effect methodology).

---

## Summary

The paper sits at the intersection of three established and one emerging literatures. The
**delegation-and-blame literature** (Bartling & Fischbacher 2012; Coffman 2011; Hamman et al.
2010; Oexl & Grossman 2013; Hill 2015; Steffel et al. 2016; Erat 2013) is the foundation: in
incentivised settings with human intermediaries, principals can shift punishment onto the
intermediary, and the prospect of punishment motivates delegation. The **algorithm-aversion
literature** (Dietvorst et al. 2015; Logg et al. 2019; Burton et al. 2020; Mahmud et al.
2022; Chugunova et al. 2022) documents many moderators of algorithm preferences, including
heightened aversion when decisions affect third parties or have moral content (Gogoll & Uhl
2018; Goldbach et al. 2019; Niszczota & Kaszás 2020; Newman, Fast & Harmon 2020). The
**responsibility-attributions-to-algorithms literature** (Kurtzberg & Naquin 2004; Pezzo &
Pezzo 2006; Liu et al. 2021; Shank et al. 2019; Bigman & Gray 2018; Tobia, Nielsen &
Stremitzer 2021; Kirchkamp & Strobel 2019) is mostly hypothetical-vignette work documenting
that people attribute less responsibility to humans when an algorithm is involved.

The closest precedent for our experimental design is **Feier, Gogoll & Uhl
2022**, who study delegation to an algorithm in an incentivised setting and find that
decision-makers are held less responsible for algorithmically delegated decisions. A new
working paper by **Chevrier & Teixeira 2024** extends this by adding a "programmer" target
of blame: their finding is that AI programmers and the delegator can both escape blame,
creating a "moral wiggle room". Two other very recent additions: **Köbis et al. 2025
(Nature)** show that humans delegate dishonest behaviour to AI agents more readily than to
human agents (because LLMs are more compliant), and **Bockstedt & Buckman 2024 (Mgmt Sci)**
show that loss-framing eliminates algorithm aversion in delegation. **Ivanova-Stenzel &
Tolksdorf 2024** measure willingness to cede control to algorithms with a menu-based design.

The **theoretical microfoundation** for our M3 mechanism (process ownership / desire to be
the proximate cause of good outcomes) draws on the **identity / moral-self-image literature**
(Bénabou & Tirole 2011 *QJE*; Falk & Szech 2013 *Science* for diffusion of responsibility in
markets) and on Steffel et al. 2016's specific finding that people care more about avoiding
blame for bad outcomes than about claiming credit for good ones.

The most consequential **gap** the paper addresses: existing work documents punishment
differentials *conditional on* the punishment possibility but does not directly identify
whether the threat of punishment causally moves the delegation decision. A second gap:
existing algorithm-versus-human comparisons confound algorithmic intermediation with
relative-performance signal extraction; individual-level calibration with common knowledge
isolates the responsibility margin. The paper's headline result —
that punishment possibility *reduces* delegation, opposite to what the responsibility-shifting
literature predicts — sits in tension with the established blame-avoidance findings and is
better explained by a Steffel-style asymmetric process-ownership account combined with
plausible experimenter-demand contributions.

---

## Key Papers

### Bartling & Fischbacher (2012) — Shifting the Blame
- **Main contribution:** the canonical experimental demonstration of delegation-as-blame-shifting in a modified dictator game.
- **Method:** dictator chooses fair vs unfair allocation, or delegates to an intermediary with aligned incentives; recipient may punish.
- **Key finding:** punishment shifts from dictator to intermediary; the prospect of avoiding punishment is a strong delegation motive.
- **Relevance:** the theoretical and empirical anchor for H1.

### Coffman (2011) — Intermediation Reduces Punishment
- **Main contribution:** replicates Bartling-Fischbacher and reinterprets the mechanism.
- **Method:** modified dictator with intermediary; varies whether the intermediary is powerless.
- **Key finding:** punishment decreases under intermediation, but because the dictator no longer "directly interacts" with the affected party, not because of inherent blame-shift; holds even with powerless intermediary.
- **Relevance:** an alternative reading that could have shaped the new paper's mechanism interpretation.

### Steffel, Williams & Perrmann-Graham (2016) — Passing the Buck
- **Main contribution:** people delegate choices for others much more than for themselves, especially when outcomes might be unappealing; the asymmetry is driven by anticipated responsibility and blame.
- **Method:** multiple lab and field studies on hotels, meal choices, business decisions.
- **Key finding:** "people care more about avoiding blame for bad outcomes than about claiming credit for good ones"; delegation is uniquely effective relative to other choice-avoidance strategies.
- **Relevance:** the **direct theoretical anchor** for the paper's M3 process-ownership story.

### Erat (2013, working paper) — Avoiding Lying via Delegated Deception
- **Main contribution:** principals delegate the act of lying to agents; women delegate more than men, and delegation increases as the harm caused by the lie increases.
- **Method:** lab experiment, deception game with delegation.
- **Relevance:** demonstrates delegation reduces the psychological cost of behaviour one expects to be judged negatively — parallel to responsibility avoidance.

### Dietvorst, Simmons & Massey (2015) — Algorithm Aversion
- **Main contribution:** coined the term; documents preference for human over algorithmic judgement even after observing the algorithm outperform.
- **Method:** lab experiments where subjects observe both human and algorithmic forecasters.
- **Relevance:** the foundational reference for the algorithm-aversion strand.

### Dietvorst & Bharti (2020) — Diminishing Sensitivity to Forecasting Error
- **Main contribution:** people reject algorithms more in *uncertain* decision domains because they have diminishing sensitivity to forecasting error.
- **Method:** nine studies, $N \approx 4{,}820$.
- **Key finding:** people prefer riskier methods (human judgement) in uncertain settings, even when those methods perform worse on average.
- **Relevance:** **directly relevant to M3**: better-performing Player As (whose probability of success sits closer to 50%) face *more* outcome uncertainty, which on this account would make them prefer their own judgement — a complementary lens on the heterogeneity result.

### Logg, Minson & Moore (2019) — Algorithm Appreciation
- **Main contribution:** documents conditions under which subjects show *appreciation* of algorithmic over human advice — moderated by the kind of task and the subject's perceived expertise.
- **Method:** lab experiments across multiple judgement tasks.
- **Relevance:** the counterweight to algorithm-aversion findings; together with Dietvorst the picture is heterogeneity, not a uniform aversion.

### Gogoll & Uhl (2018) — Rage Against the Machine
- **Main contribution:** in a moral-domain laboratory setting, subjects prefer to delegate to a human over an algorithm even on a simple calculation task.
- **Method:** lab experiment with controlled algorithm performance.
- **Relevance:** a foundational moral-domain finding; the paper's reframing — that this aversion may be more naturally read as fear-of-judgement-when-punishment-is-possible — is a contribution.

### Newman, Fast & Harmon (2020) — Algorithmic Reductionism
- **Main contribution:** people perceive algorithmic HR decisions as less fair than identical human decisions; the mechanism is "algorithmic reductionism" (quantification + decontextualization).
- **Method:** scenario experiments on HR decisions.
- **Key finding:** this finding holds for both selection and layoff outcomes.
- **Relevance:** an HR-domain example of moral-domain algorithm aversion; gives a specific channel (perceived inability to capture context) that is compatible with our M3 reading.

### Bigman & Gray (2018) — Algorithmic Outrage Asymmetry
- **Main contribution:** moral violations by algorithms produce less outrage than identical violations by humans.
- **Method:** scenario experiments.
- **Relevance:** establishes an attributional asymmetry that motivates the H2 hypothesis.

### Tobia, Nielsen & Stremitzer (2021) — Physician Use of AI and Liability
- **Main contribution:** physicians who follow AI recommendations for *standard* care can reduce liability exposure; following non-standard AI recommendations does not similarly shield them.
- **Method:** scenario experiment with $N = 2{,}000$ U.S. adults serving as mock jurors.
- **Relevance:** liability-law evidence that AI recommendations can shield decision-makers — establishes the policy stakes for our regulatory framing.

### Kirchkamp & Strobel (2019) — Sharing Responsibility with Computers
- **Main contribution:** in a modified dictator game, no significant differences in self-reported responsibility between human-computer and human-human teams; insignificant tendency toward more selfish allocations under shared responsibility with computers.
- **Method:** lab experiment.
- **Relevance:** an early null finding on responsibility-sharing in human-machine collaborative settings.

### Feier, Gogoll & Uhl (2022) — Hiding Behind Machines
- **Main contribution:** decision-makers are held less responsible for algorithmically delegated decisions than for human-delegated ones, conditional on outcome.
- **Method:** lab experiment, ten logic tasks, principals in human or machine treatment delegate to determine third party's payoff; third parties may reward or punish.
- **Key finding:** the algorithmic-delegation-shields-from-blame finding.
- **Relevance:** **the direct precedent** for our paper. The current paper's reconciliation argues that their finding is best read as a signal-extraction channel that our individual-level calibration closes off by construction.

### Chevrier & Teixeira (2024 working paper) — Shifting Blame to the Programmer
- **Main contribution:** in a lab experiment with a delegation chain (delegator → intermediary → outcome), where the intermediary is human, a rule-based algorithm, or an AI, examines blame attribution to delegators *and* programmers.
- **Method:** lab experiment with three intermediary types.
- **Key finding:** AI programmers and the delegator are not perceived as responsible for inegalitarian AI allocations, allowing AI programmers to exploit a "moral wiggle room" and select inegalitarian allocations more often.
- **Relevance:** **most direct competitor / complement**. Our paper studies the same delegation-to-AI question but isolates a different margin (motivational salience of accountability for the principal); their paper extends the blame chain backward to the developer.

### Köbis et al. (2025, Nature) — Delegation to AI Increases Dishonesty
- **Main contribution:** humans delegate cheating to AI agents more readily than to human agents because machines are far more compliant with unethical instructions (58–98% compliance vs 25–40% for humans).
- **Method:** multiple lab experiments + LLM experiments (GPT-4, Claude 3.5, Llama 3.3).
- **Key finding:** the delegation-shields-from-blame effect interacts with machine compliance to enable behaviour that wouldn't occur without delegation.
- **Relevance:** **highest-profile recent paper** in this area; relevant context but in a different setting (active dishonesty rather than uncertainty-with-stakes).

### Bockstedt & Buckman (2024 *Mgmt Sci*) — Loss Aversion and AI Delegation
- **Main contribution:** loss-framing of decision tasks eliminates algorithm aversion in delegation; participants delegate to humans and AI at similar rates under losses.
- **Method:** lab experiment with framing manipulation.
- **Relevance:** mechanism-of-aversion paper; the framing-dependence of algorithm aversion is consistent with the broader picture of heterogeneity.

### Ivanova-Stenzel & Tolksdorf (2024) — Measuring Preferences for Algorithms
- **Main contribution:** menu-based design to elicit willingness to cede control to algorithms versus humans, with performance information.
- **Method:** lab experiment with AI vs human conditions.
- **Relevance:** methodological complement; could be cited alongside Dietvorst and Logg as recent algorithm-preference measurement.

### Bénabou & Tirole (2011, *QJE*) — Identity, Morals, Taboos
- **Main contribution:** theoretical model of moral behaviour grounded in identity: people care about "who they are" and infer their values from past choices; identity investments respond non-monotonically to acts and threats.
- **Relevance:** **theoretical foundation for the M3 process-ownership story**. The desire to be the proximate cause of good outcomes is well-modelled as identity protection; the asymmetric utility from being the proximate cause maps to identity-investment dynamics.

### Falk & Szech (2013, *Science*) — Morals and Markets
- **Main contribution:** market interaction (bilateral and multilateral) substantially erodes the willingness to protect a third party (a mouse) from harm.
- **Method:** lab experiment with binary decisions.
- **Relevance:** the canonical reference for **diffusion of responsibility** as a behavioural force; our paper's setting features one possible analogue (delegation as diffusion).

### de Quidt, Haushofer & Roth (2018, *AER*) — Bounding Experimenter Demand
- **Main contribution:** technique for assessing robustness to demand effects by deliberately inducing demand and bounding its influence.
- **Key finding:** demand effects in 11 classic tasks average about 0.13 SD — modest.
- **Relevance:** the methodological reference for the M4 (experimenter demand) discussion in the conclusion.

### Holt & Laury (2002, *AER*) — Risk Aversion and Incentive Effects
- **Main contribution:** the canonical multiple-price-list (MPL) elicitation of risk preferences.
- **Relevance:** the design's risk-elicitation reference.

---

## Thematic Organization

### Theoretical contributions

The blame-avoidance-via-delegation literature has not produced a unified formal model;
mechanisms are largely descriptive (signal extraction; lack of direct interaction;
psychological cost reduction). The closest theoretical anchor for our M3 mechanism is
**Bénabou & Tirole's identity model** (2011 *QJE*) — moral self-image as an asset,
investment dynamics that produce asymmetric responses to acts and threats — combined with
**Steffel et al.'s** empirical credit/blame asymmetry. Diffusion-of-responsibility
explanations (Falk & Szech 2013 *Science*; Coffman 2011) provide a complementary lens.
None of these models specifically predict whether algorithmic intermediation should
attenuate or amplify responsibility shifting; that remains an open theoretical question.

### Empirical findings

The empirical literature shows substantial heterogeneity:

- In dictator-game settings with human intermediaries, **delegation reduces punishment**
  (Bartling & Fischbacher 2012; Hamman et al. 2010; Oexl & Grossman 2013), and **the
  prospect of punishment motivates delegation** (Bartling & Fischbacher 2012).
- In algorithm-aversion settings, **third-party / moral-domain decisions amplify aversion**
  to algorithms (Gogoll & Uhl 2018; Goldbach et al. 2019; Niszczota & Kaszás 2020;
  Newman, Fast & Harmon 2020).
- In responsibility-attribution settings, **observers attribute less responsibility when
  algorithms are involved** (Kurtzberg & Naquin 2004; Pezzo & Pezzo 2006; Bigman & Gray
  2018; Liu et al. 2021), and **physicians may follow AI recommendations to shield
  themselves from liability** (Tobia, Nielsen & Stremitzer 2021).
- In incentivised algorithm-delegation experiments, the picture is more mixed:
  **Feier et al. 2022** find delegation-shields-from-blame; **Kirchkamp & Strobel 2019**
  find no responsibility differential for human-computer vs human-human teams;
  **Maasland & Weißmüller 2022** find aversion *dominates* blame avoidance in HR settings.
- Recent additions: **Chevrier & Teixeira 2024** find programmers escape blame too;
  **Köbis et al. 2025 (Nature)** show AI's higher compliance enables delegated dishonesty;
  **Bockstedt & Buckman 2024** show loss-framing eliminates algorithm aversion.

### Methodological innovations

The paper's individual-level Bernoulli calibration of the algorithm to each subject's
empirical accuracy is, to our knowledge, the first in this literature. Existing designs
(Feier et al. 2022; Gogoll & Uhl 2018; Logg et al. 2019; Dietvorst et al. 2015) calibrate
at the session or pool level. The on/off punishment manipulation as a between-subject
treatment is also new in this specific literature, though the logic mirrors the
canonical Bartling-Fischbacher die-roll vs human comparison.

### Open debates

1. **Sign of the responsibility-shifting effect with algorithms.** Feier et al. (2022)
   and most attribution work suggest delegation-shields-from-blame; our finding that
   punishment possibility *reduces* delegation reverses the prediction of the canonical
   responsibility-avoidance literature. The reconciliation we offer — signal extraction
   in their setup, motivational salience in ours — is one resolution among several
   plausible ones.
2. **Aversion vs blame avoidance as competing channels.** Maasland & Weißmüller 2022
   conclude that aversion dominates blame avoidance in HR; our setting's individual-
   level calibration largely neutralises the aversion channel by construction, leaving
   the blame margin to be observed.
3. **Whether algorithm preferences are stable across decision domains.** The
   meta-analytic picture (Mahmud et al. 2022; Chugunova et al. 2022) is that domain
   matters substantially; our weight-prediction setting is one specific point in that
   space, with limited external validity to the high-stakes domains motivating
   regulatory debates.

---

## Gaps and Opportunities

1. **Theoretical microfoundations.** No formal model links the identity / moral-self-image
   literature to algorithm-mediated decisions. A simple model with $u = \pi -
   \alpha E[\text{punish}] + \beta \mathbb{1}[\text{ownership} \cdot \text{good outcome}]$
   (where $\beta$ is activated only by moral salience) would formalise the M3 reading and
   produce testable comparative statics.
2. **The signal-extraction-vs-process-ownership decomposition.** Our paper hypothesises
   that Feier et al.'s differential punishment is driven by signal extraction and that our
   design isolates a process-ownership margin; testing this decomposition directly would
   require an experiment that varies the relative-performance calibration across arms while
   holding the punishment possibility fixed.
3. **Cross-domain external validity.** Almost all incentivised work is in stylised lab
   tasks. The high-stakes algorithmic domains motivating regulatory debates (medical
   diagnosis, judicial risk assessment, hiring, credit) are essentially un-represented in
   the experimental literature. Vignette-based work bridges the gap (Tobia et al. 2021;
   Bigman & Gray 2018) but the incentive structure is hypothetical.
4. **The "moral wiggle room" frontier.** Chevrier & Teixeira 2024 extend the blame chain
   to programmers; further work could extend it to deploying organisations (the most
   common Player-B-stated accountability target in our data).
5. **Interaction of accountability regimes with adoption.** Our paper takes one step in
   this direction by showing that the punishment possibility shifts adoption; the converse
   question — how regulatory regimes shape the *quality* of human decisions when an
   algorithm is the alternative — is wide open.

---

## Suggested Next Steps

- **Bring Bénabou & Tirole 2011** explicitly into Section~\ref{literature} as the
  theoretical anchor for M3, alongside Steffel et al. 2016's specific
  credit-vs-blame-asymmetry quote.
- **Add Newman, Fast & Harmon 2020** to the moral-domain algorithm-aversion paragraph
  (currently missing despite being directly relevant).
- **Add Chevrier & Teixeira 2024** as a working-paper companion that extends our framing
  along a different margin (the programmer); this is a "this paper" that should be cited
  in the reconciliation paragraph.
- **Add Köbis et al. 2025 (Nature)** as the most prominent recent contribution and as a
  contrast: their setting (delegating dishonest behaviour with LLM compliance as the
  amplifier) is genuinely different from ours but shares the AI-as-blame-shield motif.
- **Add Falk & Szech 2013 (Science)** as the canonical diffusion-of-responsibility
  reference for the broader market-erodes-morals frame.
- **Add Bockstedt & Buckman 2024 (Mgmt Sci)** and **Ivanova-Stenzel & Tolksdorf 2024**
  as recent algorithm-preference references in the §Delegation-to-Algorithms paragraph.
- **Mention Maasland & Weißmüller 2022** explicitly: their finding that aversion
  *dominates* blame avoidance in HR is a useful contrast to our finding that the
  punishment possibility reduces delegation. Both findings imply that algorithms are not
  the easy blame-shield the canonical responsibility-avoidance literature might suggest.
- **Mention Dietvorst & Bharti 2020 (Psych Sci)** in §sec:mechanism: their
  diminishing-sensitivity-to-error mechanism gives an alternative reading of the M3
  performance heterogeneity (better-performing subjects face more outcome uncertainty,
  preferring their own judgement on the diminishing-sensitivity logic).

---

## BibTeX entries

The new entries below have been added to [`manuscript/ProjectAlgorithm.bib`](../manuscript/ProjectAlgorithm.bib):

```bibtex
@article{benabou_identity_2011,
    title = {Identity, Morals, and Taboos: Beliefs as Assets},
    author = {Bénabou, Roland and Tirole, Jean},
    journal = {Quarterly Journal of Economics},
    volume = {126}, number = {2}, pages = {805--855}, year = {2011},
    doi = {10.1093/qje/qjr002}
}

@article{falk_morals_2013,
    title = {Morals and Markets},
    author = {Falk, Armin and Szech, Nora},
    journal = {Science}, volume = {340}, number = {6133}, pages = {707--711}, year = {2013},
    doi = {10.1126/science.1231566}
}

@article{newman_eliminating_2020,
    title = {When eliminating bias isn't fair: Algorithmic reductionism and procedural justice in human resource decisions},
    author = {Newman, David T. and Fast, Nathanael J. and Harmon, Derek J.},
    journal = {Organizational Behavior and Human Decision Processes},
    volume = {160}, pages = {149--167}, year = {2020},
    doi = {10.1016/j.obhdp.2020.03.008}
}

@unpublished{chevrier_algorithm_2024,
    title = {Algorithm Delegation and Responsibility: Shifting Blame to the Programmer?},
    author = {Chevrier, Marion and Teixeira, Marina}, year = {2024},
    note = {GREDEG Working Paper 2024-04, Université Côte d'Azur},
    url = {https://ideas.repec.org/p/gre/wpaper/2024-04.html}
}

@article{kobis_delegation_2025,
    title = {Delegation to artificial intelligence can increase dishonest behaviour},
    author = {Köbis, Nils and Rahwan, Zoe and Rilla, Raluca and others},
    journal = {Nature}, volume = {646}, number = {8083}, year = {2025},
    doi = {10.1038/s41586-025-09505-x},
    note = {VERIFY full author list}
}

@article{bockstedt_humans_2024,
    title = {Humans' Use of AI Assistance: The Effect of Loss Aversion on Willingness to Delegate Decisions},
    author = {Bockstedt, Jesse C. and Buckman, Joseph R.},
    journal = {Management Science}, volume = {72}, number = {1}, pages = {323--342}, year = {2024},
    doi = {10.1287/mnsc.2024.05585}
}

@article{ivanova_stenzel_measuring_2024,
    title = {Measuring preferences for algorithms --- How willing are people to cede control to algorithms?},
    author = {Ivanova-Stenzel, Radosveta and Tolksdorf, Michel},
    journal = {Journal of Behavioral and Experimental Economics}, year = {2024},
    note = {VERIFY volume and pages}
}
```

The previously added entries `holt_risk_2002` and `de_quidt_measuring_2018` had `VERIFY`
notes; both have been confirmed and the notes removed (`de_quidt_measuring_2018` carries
its DOI).

---

## Post-Flight Verification

| Item | Status |
|---|---|
| Manual cross-check via WebSearch on each new citation | Complete (search results in the conversation) |
| Verifier subagent run | Pending — see §"Post-Flight" below |
| Unverified author lists or page numbers | `kobis_delegation_2025` (full author list), `ivanova_stenzel_measuring_2024` (volume/pages) — flagged with `VERIFY` |

A `claim-verifier` Post-Flight pass is recommended before final integration into the
manuscript; for now, the entries above carry conservative `note = {VERIFY}` flags where
exact bibliographic details could not be confirmed via WebSearch alone.
