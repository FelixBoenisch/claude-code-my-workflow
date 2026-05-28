# Literature-section audit across supporting papers

For each paper in `master_supporting_docs/supporting_papers/_extracted_text/`, this report records: (i) whether a Literature / Related Work section exists as a separate section from the Introduction, and (ii) whether the first paragraph of that section is an explicit framing/bridging paragraph similar to line 3 of `manuscript/literature.tex` (`'This paper bridges three strands of literature: (i) ..., (ii) ..., and (iii) ...'`).

## Summary

- **Papers scanned:** 65
- **Papers with a separate Literature / Related Work section:** 13 / 65 (20%)
- **Papers with a bridging framing paragraph (overall):** 3 / 65 (5%)
- **Of papers with a separate lit section: framing paragraph at its start:** 3 / 13 (23%)

## Detection rules

- A **separate Literature section** is recognised when a short standalone line (≤ 80 chars) matches a known heading: *Related Literature*, *Related Work*, *Literature [Review]*, *Background*, *Theoretical Background*, *Prior / Previous Literature*, *Related Research*, *Theoretical / Conceptual Framework*, *Theory and Hypotheses / Literature / Background*, *Related Studies*. Numbering / Roman numerals are allowed as prefixes.
- A **bridging paragraph** is flagged when the first ~1,500 chars of the lit section contain *either* (a) explicit enumeration of strands — `(i) ... (ii)`, `1) ... 2)`, or `first ... second ...` — *or* (b) a phrase like `'N strands / streams / bodies of literature'`. A bridge verb alone (e.g., `'contributes to two literatures'`) without enumeration or 'strands' wording does NOT trigger the flag, to keep the precision high.

## Per-paper table

| Paper | Separate lit section? | Heading found | Bridging paragraph? | Evidence |
|---|:---:|---|:---:|---|
| `argenton_potters_yang_2023` | — |  | — |  |
| `bartling_fischbacher_schudy_2015` | — |  | — |  |
| `bartling_shifting_2012` | — |  | — |  |
| `benabou_identity_2011` | — |  | — |  |
| `berger_watch_2021` | ✅ | 2 Theoretical Foundations | — |  |
| `bigman_people_2018` | — |  | — |  |
| `bogert_humans_2021` | — |  | — |  |
| `bonnefon_the_2024` | — |  | — |  |
| `burton_systematic_2020` | — |  | — |  |
| `castelo_task-dependent_2019` | — |  | — |  |
| `chen_AI_2026` | ✅ | 2 Related Work | — |  |
| `chen_otree_2016` | — |  | — |  |
| `chevrier_algorithm_2024` | ✅ | 2 Related literature and conjectures | ✅ | bridge/review verb + literature + 'and' (list of strands) |
| `chugunova_we_2022` | — |  | — |  |
| `coffman_intermediation_2011` | ✅ | V. Related Literature | — |  |
| `dargnies_aversion_2026` | — |  | — |  |
| `de_quidt_measuring_2018` | — |  | — |  |
| `dietvorst_algorithm_2015` | — |  | — |  |
| `dietvorst_overcoming_2018` | — |  | — |  |
| `dietvorst_people_2020` | — |  | — |  |
| `erat_avoiding_2013` | — |  | — |  |
| `european_union_ai_act_2024` | — |  | — |  |
| `falk_morals_2013` | — |  | — |  |
| `feier_hiding_2022` | — |  | — |  |
| `fershtman_gneezy_2001` | — |  | — |  |
| `fiorina_legislator_1986` | — |  | — |  |
| `freer_friedman_weidenholzer_2024` | ✅ | 2 Literature | ✅ | enumeration ((i)/(ii), 1)/2), or first/second) |
| `gogoll_rage_2018` | — |  | — |  |
| `goldbach_geht_2019` | — |  | — |  |
| `hamman_self-interest_2010` | ✅ | B. Related Literature | — |  |
| `heaton_social_2023` | — |  | — |  |
| `hill_does_2015` | — |  | — |  |
| `holt_risk_2002` | — |  | — |  |
| `hueholt_trusting_2026` | — |  | — |  |
| `ivanova_stenzel_delegating_2025` | — |  | — |  |
| `ivanova_stenzel_measuring_2024` | — |  | — |  |
| `jauernig_people_2022` | — |  | — |  |
| `jolly_not_2025` | ✅ | Theoretical Framework and Hypothesis | — |  |
| `killoran_learn_2026` | — |  | — |  |
| `kirchkamp_sharing_2019` | ✅ | 4. Theoretical framework and behavioral hypotheses | — |  |
| `kobis_delegation_2025` | — |  | — |  |
| `kormylo_till_2025` | ✅ | 2. Conceptual Background: Algorithms and Betrayal | ✅ | enumeration ((i)/(ii), 1)/2), or first/second); 'N (primary/main) strands/streams/bodies of literature'; bridge/review verb + literature + 'and' (list of strands) |
| `kurtzberg_attribution_2004` | — |  | — |  |
| `litterscheidt_financial_2020` | ✅ | 2. Background and related literature | — |  |
| `liu_when_2021` | ✅ | Literature review | — |  |
| `logg_algorithm_2019` | — |  | — |  |
| `maasland_blame_2022` | — |  | — |  |
| `mahmud_what_2022` | ✅ | 6.2. Theoretical framework and measurement | — |  |
| `newman_eliminating_2020` | — |  | — |  |
| `niszczota_robo-investors_2020` | — |  | — |  |
| `normann_delegate_2025` | — |  | — |  |
| `oexl_shifting_2013` | — |  | — |  |
| `pezzo_pezzo_physician_2006` | — |  | — |  |
| `qin_ai_2025` | — |  | — |  |
| `salatino_influence_2025` | — |  | — |  |
| `shank_attributions_2019` | — |  | — |  |
| `sharan_dont_2020` | — |  | — |  |
| `steffel_passing_2016` | — |  | — |  |
| `sunstein_anatomy_2024` | — |  | — |  |
| `tobia_when_2021` | — |  | — |  |
| `tontrup_strategic_2025` | — |  | — |  |
| `trunk_current_2020` | — |  | — |  |
| `tsumura_effects_2026` | ✅ | Related work | — |  |
| `weaver_politics_1986` | — |  | — |  |
| `weitzner_reputational_2024` | — |  | — |  |

## First paragraphs of detected literature sections (for spot-checking)

_Below is the first paragraph found after each detected literature heading (truncated at 1,200 chars). Use this to verify the detection and to compare framing styles across papers._


### `chevrier_algorithm_2024` — heading: *2 Related literature and conjectures* (bridging frame)

> 2.1 Related literature  To investigate whether participants decide to delegate an allocation decision to an RA or an AI, and to provide evidence of differences between these algorithms and a human intermediary, we review the relevant literature on algorithmic delegation, perceived re- sponsibility, and moral wiggle room. We use this literature review and logical reasoning to formulate behavioral conjectures in the second part.  2.1.1 Algorithmic appreciation Although algorithms often outperform humans in many tasks, people tend to prefer to delegate tasks to humans rather than algorithms (Meehl, 1954; Dawes, 2008; Sanders and Manrodt, 2003; Fildes and Goodwin, 2007; Dietvorst et al., 2015; Jung and Seiter, 2021; Dargnies et al., 2024). However, a preference for algorithmic delegation may emerge depending on whether the algorithm acts as an advisor (Logg et al., 2019; You et al., 2022; Daschner and Obermaier, 2022), the objectivity of the task (Castelo et al., 2019; Hertz and Wiese, 2019) and the perceived complexity of the algorithm (Lehmann et al., 2022; Chevrier et al., 2024). These findings underscore the growing importance of algorithms  4  in a variety of areas in economics.4 


### `freer_friedman_weidenholzer_2024` — heading: *2 Literature* (bridging frame)

> We first discuss literature that is closest to the present paper, and then review literature that proposes motives for delegation.  2.1 Nearest neighbors  Our work is closely related to recent work on delegation in financial decision mak- ing. Apesteguia et al. (2020), like the present paper, report an experiment where investors may decide to delegate financial decisions to their peers. They show that a substantial fraction of investors does so by either directly copying previously successful investors by the click of a button or manually implementing investment strategies which are similar to those of the most successful peers. Since success is mainly driven by luck and since investors who previously took on a lot of risk appear on top of the earning rankings, Apesteguia et al. (2020) find that copy trading may lead to a substantial increase in risk taking.  The present study extends the design of Apesteguia et al. (2020) by varying the complexity of the underlying task and the information investors receive about the experts. When our investors do not have access to information on experts' decision quality, we confirm that a substantial fraction of subjects chooses to delegate to 


### `kormylo_till_2025` — heading: *2. Conceptual Background: Algorithms and Betrayal* (bridging frame)

> Our work examines two primary areas of the literature. First, we look to previous work on algorithm adoption and aversion that focuses on specific drivers of use and disuse to better understand predictors of algorithmic acceptance. Then, we explore the betrayal aversion literature in economics and introduce it as a previously unexamined factor in algorithm uptake. In the section that follows, we contextualize our work to financial technology and examine the theoretical expectations of the effect of betrayal aversion on the use of trading algorithms.  2.1 Algorithm Adoption and Aversion  Prior work considering the use and adoption of information technology has strived to consider user's social and emotional beliefs (Benbasat and Wang 2005; Qiu and Benbasat 2005; Venkatesh and Davis 2000). This has led to the perception of IT artifacts as "social actors" (Al-Natour and Benbasat 2009; Reeves and Nass 1996). In the Computers are Social Actors (CASA) paradigm, humans have the same social rules and expectations of technology that they have of other humans (Nass et al. 1994). This paradigm now has renewed importance as digital ecosystems built on powerful algorithms are influencing the da


### `berger_watch_2021` — heading: *2 Theoretical Foundations*

> (Castelo et al. 2019; Longoni et al. 2019; Logg et al. 2019). 2.1 Algorithm Aversion what algorithm aversion is: unwillingness to rely on an The literature on algorithm aversion is rooted in the con- troversy over the merits of clinical (i.e., based on deliberate  resistance to algorithmic judgement. Our study aims at human thought) and actuarial (i.e., based on statistic models) judgement in different domains, such as medical diagnosis and treatment (Meehl 1954; Dawes 1979; Dawes et al. 1989; Grove et al. 2000). Overall, this research concludes that actuarial data interpretation is superior to clinical analysis but that humans nevertheless show a ten- dency to resist purely actuarial judgement. This resistance extends to the use of algorithmic decision support when compared to human advice (Promberger and Baron 2006; Alvarado-Valencia and Barrero 2014). Evidence from IS research supports these findings: For instance, Lim and O'Connor (1996) demonstrate that people underutilize information from DSS when making decisions. Elkins et al. (2013) find that expert system users feel threatened by system recommendations contradicting their expertise and thus tend to ignore these recommenda


### `chen_AI_2026` — heading: *2 Related Work*

> 2.1 Delegation in Human-AI interaction  Delegation in Human�AI interaction refers to the process in which humans transfer task execution authority and, to some extent, out- come responsibility to AI agents [36, 66, 83]. This process enables humans to leverage AI's computational efficiency while managing their own cognitive resources and decision-making load, particu- larly in complex or high-stakes tasks [19, 79, 91, 104]. For example, studies on Human�AI collaboration in decision-making contexts  large amounts of data processing or cognitively taxing choices, when they trust the AI's competence [103].  Principal-agent theory provides a foundational framework to analyze delegation by highlighting the structural dynamics of au- thority, accountability, and information asymmetry between dele- gators and delegates [35]. Within this framework, delegation shifts authority and accountability, influencing human perceptions of control, risk, and task retention decisions [12, 29, 94]. Building on this, the task delegability framework further specifies that dele- gation decisions are contingent on both task- and agent-specific characteristics. Task attributes such as complexity, uncertainty,


### `coffman_intermediation_2011` — heading: *V. Related Literature*

> A. The Economics Literature: Punishment and Fairness  The literature has shown punishment can effectively regulate individuals (Fehr and Fischbacher 2004; Fehr and G�chter 2000) as well as companies (Alexander  32This elicits their belief of the midpoint of the $10 interval containing the most Survey 1 donors in their distribution of beliefs. Beliefs were elicited this way in order to keep it simple and understandable for the subject.  33The DG decision in Survey 1 may very well not be independent. There might be wealth effects, though wealth is only in expectation. Additionally, often after performing a good act, we feel licensed to be less moral in the next period (e.g., Cain, Loewenstein, and Moore 2005). Whether subjects predict such inter-question dependencies, or others, is unknown to the author. In any case, this result should only be regarded with these considerations.  Vol. 3 No. 4  coffman: intermediation reduces punishment (and reward)  99  Dyck and Luigi Zingales 2002; Kenneth J. Martin and Randall S. Thomas 2005). Theoretically, punishment increases pro-social behavior, which means that punish- ment can lead to greater social welfare for the group (Robert Axelrod 1986)


### `hamman_self-interest_2010` — heading: *B. Related Literature*

> Extensive research in economics suggests that people not only maximize their own payoffs, narrowly construed, but also display a preference for social outcomes such as fairness or equal- ity (Daniel Kahneman, Jack L. Knetsch, and Richard H. Thaler 1986; and see Colin F. Camerer, 2003 for a review). Research on the dictator game shows that even under conditions of complete anonymity dictators share significant amounts of money with unknown recipients (Elizabeth Hoffman et al. 1994). Such results have led to the development of several theoretical models that assume people derive utility from behaving generously, or disutility from unequal outcomes (Loewenstein, Leigh Thompson and Max H. Bazerman 1989; Matthew Rabin 1993; Ernst Fehr and Klaus M. Schmidt 1999; Gary E. Bolton and Axel Ockenfels 2000; James Andreoni and John Miller 2002).  More recent work suggests that instead of valuing equitable outcomes, people may value the perception that their behavior is generous. For example, Jason Dana, Weber, and Jason Xi Kuang (2007) used a binary dictator game and varied the extent to which dictators were directly, uniquely, and knowingly responsible for outcomes. Experimental manipulations 


### `jolly_not_2025` — heading: *Theoretical Framework and Hypothesis*

> Algorithms are frequently used to improve the efficiency of decision making. By processing relevant data available to the algorithm and using those data to quickly present employees     A. A. Jolly et al.  (JCM; Hackman & Oldham, 1976). The JCM posits that employees who experience sufficient levels of positive work characteristics will subsequently experience criti-  for the employee and organization (e.g., job satisfaction and performance). Within the JCM, job autonomy fosters the psychological state of personal responsibility for the outcomes or consequences of one's work (here onwards we refer to this state as `personal responsibility'). In other words, individuals will recognize that outcomes of the job "depend increasingly on the individual's own efforts, initiatives, and decisions rather than on the adequacy of instructions from the boss or on a manual of job proce- dures," leading to "strong personal responsibility for the success and failures that occur on the job" (Hackman & Oldham, 1976, p. 258). This greater personal responsibility and sense of ownership of outcomes means that individu- als are likely to think more widely about any repercussions of their action, and, in 


### `kirchkamp_sharing_2019` — heading: *4. Theoretical framework and behavioral hypotheses*

> A purely sel sh participant would take into account neither the welfare of others nor situa- tional circumstances. In particular, for a sel sh participant it should not ma er whether the decision was made alone, with another person or with a computer. Similarly, for a partici- pant with xed social preferences the type of interaction partner, human or computer, should not ma er. However, we know that social preferences depend on the salience of the link be- tween actions and consequences. Chen and Schonger (2016) as well as Haisley and Weber (2010) show that certainty or ambiguity of the outcome ma ers. Grossman and van der Weele (2016), Grossman (2014) and Ma hey and Regner (2011) argue that social preferences are a ected by the availability of excuses which allow individuals to justify a sel sh behav- ior. ese ndings can be supported with the help of models of social image concerns (e.g., Andreoni and Bernheim, 2009; Be�nabou and Tirole, 2006; Ellingsen and Johannesson, 2008; Grossman, 2015) and models on self-perception maintenance (e.g., Aronson, 2009; Beauvois and Joule, 1996; Bodner and Prelec, 2003; Konow, 2000; Mazar et al., 2008; Murnighan et al., 2001; Rabin, 1995). Accord


### `litterscheidt_financial_2020` — heading: *2. Background and related literature*

> Retail investor behavior and financial literacy  Retail investors tend to be subject to several costly investment mistakes. For instance, few investors are invested in the stock market despite the evidence of a substantial equity premium (Guiso et al., 2002). If they are invested, they are often under-diversified, exhibit an excessive preference for local equity (Goetzmann and Kumar, 2008), or insufficiently adjust their portfolios to general market movements (Calvet et al., 2009). Overconfident investors tend to trade excessively, which compromises their returns through transaction costs (Barber and  4  Litterscheidt & Streich  Odean, 2000; Glaser and Weber, 2007). Investors further tend to prefer to realize stock price gains rather than losses, thereby diluting investment performance (the so-called disposition effect, Shefrin and Statman, 1985). Surveys have shown that a large share of retail investors lacks understanding of basic financial concepts (Inderst and Ottaviani, 2012; Lusardi and Mitchell, 2011), which is associated with inefficient financial behavior (Agarwal et al., 2017). Although the established relationship is likely endogenous and thus overstated in magnitude (Ha


### `liu_when_2021` — heading: *Literature review*

> Uncertainty reduction and trust in human�machine interaction Concepts of trust and uncertainty reduction were initially studied in the context of human�human (H�H) interaction but later were also found applicable to human�machine (H�M) interaction (Jian,  Journal of Computer-Mediated Communication 26 (2021) 384�402  385  Effects of Agency Locus and Transparency  B. Liu  Bisantz, & Drury, 2000). In both contexts, trust denotes "the attitude that an agent will help achieve      Downloaded from https://academic.oup.com/jcmc/article/26/6/384/6367958 by guest on 12 May 2026 an individual's goals in a situation characterized by uncertainty and vulnerability" (Lee & See, 2004, p. 51). For users to comply with AI-made decisions or to accept an AI system making decisions on be- half of them, they first need to trust it. Given that machines are typically considered as lacking inten- tionality (Dennett, 1988), this study focuses on the competence dimension of individuals' trust in decision-making AI systems (Lee & Moray, 1992).  How does trust develop? Research suggests that uncertainty reduction facilitates goal achieve- ment, and therefore, is fundamental to trust development in both H�H an


### `mahmud_what_2022` — heading: *6.2. Theoretical framework and measurement*

> employee-AI trust, AI strategy, and compatibility influence the use of AI Our review signals a lack of a unified theoretical framework of al gorithm aversion explaining its nature, antecedents, moderators, me diators, and outcomes. Absence of a theoretical framework makes it harder to obtain a holistic overview of algorithm aversion. The theo retical framework is necessary for understanding different concepts associated with it and guiding research (Duan et al., 2019). In our reviewed studies, we find that scholars mainly focused on merely one or few concepts related to algorithm aversion in their studies, for example, integration of people's opinions in algorithm design is explicated in Kawaguchi (2021), people's sensitivity to error in Dietvorst and Bharti (2020), and moral decisions in Niszczota and Kasza�s (2020). Surpris ingly, however, we do not have any comprehensive framework encompassing all related concepts. rule-based AI system and ML-based AI system on algorithmic decisions? Furthermore, extant literature does not suggest any scale for the al gorithm aversion construct. Therefore, a unified scale of algorithm aversion is required. Such a scale will allow for statistical


### `tsumura_effects_2026` — heading: *Related work*

> Responsibility attribution in human-agent interaction has been studied across disciplines including psychology, law, and human-robot interaction (HRI). Across these domains, prior work has highlighted factors such as causal structure, system autonomy, and moral intuition as central to blame judgments. In the context of automated vehicles (AVs), Stojilovi et al13. found that people attribute greater responsibility when AVs are involved in accidents, compared with scenarios with human drivers. Franklin et al14. proposed a comprehensive framework comprising nine factors�such as causality, knowledge, autonomy, and intention�that influence responsibility judgments. They also introduced serious games as tools to explore responsibility in causal cognition.  Medical and legal contexts provide further insight into responsibility attribution. Naik et al29. reviewed how responsibility is assigned when AI is used in clinical decision-making, while Parlangeli et al30. explored how delegating legal decisions to AI alters moral judgments. Scheutz and Malle31 examined moral evaluations of agents making life-or-death decisions and found that such decisions are judged through human moral lenses. Kne


## Papers with no separate Literature section detected

- `argenton_potters_yang_2023`
- `bartling_fischbacher_schudy_2015`
- `bartling_shifting_2012`
- `benabou_identity_2011`
- `bigman_people_2018`
- `bogert_humans_2021`
- `bonnefon_the_2024`
- `burton_systematic_2020`
- `castelo_task-dependent_2019`
- `chen_otree_2016`
- `chugunova_we_2022`
- `dargnies_aversion_2026`
- `de_quidt_measuring_2018`
- `dietvorst_algorithm_2015`
- `dietvorst_overcoming_2018`
- `dietvorst_people_2020`
- `erat_avoiding_2013`
- `european_union_ai_act_2024`
- `falk_morals_2013`
- `feier_hiding_2022`
- `fershtman_gneezy_2001`
- `fiorina_legislator_1986`
- `gogoll_rage_2018`
- `goldbach_geht_2019`
- `heaton_social_2023`
- `hill_does_2015`
- `holt_risk_2002`
- `hueholt_trusting_2026`
- `ivanova_stenzel_delegating_2025`
- `ivanova_stenzel_measuring_2024`
- `jauernig_people_2022`
- `killoran_learn_2026`
- `kobis_delegation_2025`
- `kurtzberg_attribution_2004`
- `logg_algorithm_2019`
- `maasland_blame_2022`
- `newman_eliminating_2020`
- `niszczota_robo-investors_2020`
- `normann_delegate_2025`
- `oexl_shifting_2013`
- `pezzo_pezzo_physician_2006`
- `qin_ai_2025`
- `salatino_influence_2025`
- `shank_attributions_2019`
- `sharan_dont_2020`
- `steffel_passing_2016`
- `sunstein_anatomy_2024`
- `tobia_when_2021`
- `tontrup_strategic_2025`
- `trunk_current_2020`
- `weaver_politics_1986`
- `weitzner_reputational_2024`

