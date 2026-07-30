# Redraft: literature.tex lines 39–46 (moderators of algorithm aversion)

Replaces lines 39–46. The old paragraph at line 37 duplicates this material and should be deleted when this block is adopted.

```latex
For example, on the algorithm side, algorithm aversion is stronger when the
algorithm cannot be observed to learn from its mistakes \citep{berger_watch_2021}
and when the algorithm remains a black box to its users
\citep{litterscheidt_financial_2020}. More information about the algorithm is,
however, no remedy by itself: what reduces aversion is evidence about relative
performance, gathered through experience and feedback \citep{filiz_reducing_2021},
rather than explanations of how the algorithm works, which leave acceptance
unchanged \citep{dargnies_aversion_2026}.

On the task side, algorithm aversion rises with the degree of irreducible
uncertainty \citep{dietvorst_people_2020} and with the perceived subjectivity of
the task \citep{castelo_task-dependent_2019}, while reliance on algorithms
increases with task difficulty \citep{bogert_humans_2021}, under time pressure,
which lowers decision-makers' confidence in their own judgement
\citep{jung_towards_2021}, and when the decision is framed in terms of losses
rather than gains, which removes the otherwise strong preference for human
assistance \citep{bockstedt_humans_2025}.

On the control side, people use imperfect algorithms far more readily when they
retain even a minimal ability to modify the output \citep{dietvorst_overcoming_2018};
likewise, experimental firms delegate pricing to an algorithm more often when they
can override its decisions \citep{normann_delegate_2025}. Part of algorithm
aversion may thus reflect a reluctance to relinquish decision authority as such
rather than distrust of algorithms: people underuse superior agents whether these
are human or algorithmic \citep{ivanova_stenzel_delegating_2025}, and performance
feedback raises reliance on algorithms without eliminating the desire for personal
control \citep{ivanova_stenzel_measuring_2024}.

Control, in turn, interacts with responsibility: merely retaining a manual
override increases the blame humans receive when the machine errs
\citep{arnestad_manual_2024}, experienced professionals resist algorithmic advice
precisely because they feel accountable for mistakes of a system they do not
control \citep{allen_algorithm_2022}, and passing a decision on carries
interpersonal costs of its own, as those asked to decide penalise delegators for
transferring decision responsibility \citep{blunden_downside_2023}. Reviewing
this evidence, \citet{irlenbusch_human_2026} concludes that algorithm use is
governed less by a stable pro- or anti-algorithm attitude than by whether the
informational and institutional environment allows decision-makers to calibrate
their reliance to what the algorithm can actually do --- and to the
responsibility they bear for its decisions.
```

## New bibliography entries required (append to ProjectAlgorithm.bib)

```bibtex
@article{filiz_reducing_2021,
    title = {Reducing Algorithm Aversion Through Experience},
    author = {Filiz, Ibrahim and Judek, Jan Ren{\'e} and Lorenz, Marco and Spiwoks, Markus},
    journal = {Journal of Behavioral and Experimental Finance},
    volume = {31},
    pages = {100524},
    year = {2021},
    doi = {10.1016/j.jbef.2021.100524}
}

@article{jung_towards_2021,
    title = {Towards a Better Understanding on Mitigating Algorithm Aversion in Forecasting: An Experimental Study},
    author = {Jung, Markus and Seiter, Mischa},
    journal = {Journal of Management Control},
    volume = {32},
    pages = {495--516},
    year = {2021},
    doi = {10.1007/s00187-021-00326-3}
}

@article{allen_algorithm_2022,
    title = {Algorithm-Augmented Work and Domain Experience: The Countervailing Forces of Ability and Aversion},
    author = {Allen, Ryan T. and Choudhury, Prithwiraj},
    journal = {Organization Science},
    volume = {33},
    number = {1},
    pages = {149--169},
    year = {2022},
    doi = {10.1287/orsc.2021.1554}
}

@article{arnestad_manual_2024,
    title = {The Existence of Manual Mode Increases Human Blame for {AI} Mistakes},
    author = {Arnestad, Mads N. and Meyers, Samuel and Gray, Kurt and Bigman, Yochanan E.},
    journal = {Cognition},
    volume = {252},
    pages = {105931},
    year = {2024},
    doi = {10.1016/j.cognition.2024.105931}
}

@article{blunden_downside_2023,
    title = {The Downside of Decision Delegation: When Transferring Decision Responsibility Incurs Interpersonal Costs},
    author = {Blunden, Hayley and Steffel, Mary},
    journal = {Organizational Behavior and Human Decision Processes},
    volume = {176},
    pages = {104251},
    year = {2023},
    doi = {10.1016/j.obhdp.2023.104251}
}
```
