# Bibliography audit: implemented changes

Completed **5 September 2026**, following the author's review and instructions. 

Updated **38 existing records** (16 currently cited), deleted **`stein_dont_2020`**, and rebuilt the manuscript. The bibliography now contains **105 entries**; all **54 cited keys** resolve. The manuscript's `.tex` source files were preserved.

## Author decisions implemented

- **Sunstein and Gaffe:** use **2025**, January, *Science and Technology Law Review*, **26(1): 290-317**, DOI **10.52214/stlr.v26i1.13339**, following the [journal website](https://journals.library.columbia.edu/index.php/stlr/article/view/13339). The existing citation key `sunstein_anatomy_2024` is retained so source citations continue to work.
- **Stein:** deleted `stein_dont_2020`. The original entry remains available in the audit and the bibliography backup.
- **Goldbach, Kurtzberg, and Liu:** confirmed uncited and preserved byte-for-byte; no action is needed on their identity annotations for the current manuscript.
- **Issue years:** applied the agreed final-issue convention, including **2026** for Bockstedt/Buckman and Kormylo et al., **2025** for Freisinger/Schneider, and the published **2026** Freer/Friedman/Weidenholzer article.
- Applied the reviewed corrections, metadata completions, optional enrichments, and removal of resolved verification notes.

## Ismagilova erratum retrieved

The complete notice was found appended to the existing supporting article PDF and extracted as [ismagilova_ethics_erratum_2026.pdf](ismagilova_ethics_erratum_2026.pdf). All three pages were rendered and visually inspected. The source PDF was preserved.

**Item 7**, across erratum pages **1-2**, adds the omitted ethics and informed-consent statement for Ismagilova and Ploner. It says formal ethics approval was not required under the University of Trento guidelines for anonymous adult participants facing no identifiable risk; Prolific participation was voluntary, study information was provided before participants opted in, and withdrawal was permitted. It lists no revisions to their results, data, or analyses. The current supporting article already includes this statement on printed page 9.

The notice is *Computers in Human Behavior: Artificial Humans*, **8 (2026), 100317**, DOI [10.1016/j.chbah.2026.100317](https://doi.org/10.1016/j.chbah.2026.100317). The original article remains **2025, volume 4, article 100147**, with its original DOI. No erratum entry was added to the manuscript bibliography because it is not cited.

[Full statement, source links, and retrieval evidence](ISMAGILOVA_ERRATUM_RETRIEVAL.md).

## Rendering adjustments

Three small BibTeX adaptations preserve the verified metadata in the existing `aer` bibliography style:

- Heaton's article locator is stored as `note = {Article No. 11.}` because the style does not support an `articleno` field.
- The compound surname is protected as `{{Santoni de Sio}, Filippo and Mecacci, Giulio}`. Without the inner braces, BibTeX printed "de Sio, Filippo Santoni" and sorted the reference under D. The protected form follows the [publisher citation](https://link.springer.com/article/10.1007/s13347-021-00450-x).
- The EU Act's `howpublished` ends in `12 July`; the retained `year = {2024}` supplies the year once in the rendered locator. This avoids printing "12 July 2024 2024" while preserving the complete date.

The existing style does not print DOI, URL, or ISBN fields; those enrichments are retained in the bibliography file.

## Verification

- Independent comparison against the reviewed audit, the user's decisions, and the original bibliography: **passed**.
- BibTeX syntax, unique entry keys, revised field values, and all 54 cited keys: **passed**.
- `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`: **all successful**, with no BibTeX warnings or undefined citations.
- Final reference pages 27-31 were visually checked; names, ordering, dates, and page layout are correct.
- Two pre-existing non-bibliographic LaTeX warnings remain: marginal-note geometry and the layouts package scale setting.

[Independent QA](implementation_qa.md) | [Build evidence](build_verification.json) | [Machine-readable change ledger](implemented_changes.json).

## Implemented field changes

The table gives the final stored values. Citation keys were preserved except for the approved Stein deletion. The [original review report](REPORT.before-implementation.md) retains the verification evidence for every one of the original 106 entries.

| Citation key | Cited | Field | Before | Implemented |
|---|---|---|---|---|
| `allen_algorithm_2022` | No | `author` | Allen, Ryan and Choudhury, Prithwiraj | Allen, Ryan T. and Choudhury, Prithwiraj (Raj) |
| `allen_algorithm_2022` | No | `doi` | (absent / removed) | 10.1287/orsc.2021.1554 |
| `arnestad_manual_2024` | No | `pages` | (absent / removed) | 105931 |
| `arnestad_manual_2024` | No | `doi` | (absent / removed) | 10.1016/j.cognition.2024.105931 |
| `bartling_shifting_2012` | Yes | `author` | Bartling, B. and Fischbacher, U. | Bartling, Bj{\"o}rn and Fischbacher, Urs |
| `beckers_drivers_2022` | Yes | `author` | Beckers, Niek and Cavalcante Siebert, Luciano and Bruijnes, Merijn and Jonker, Catholijn and Abbink, David | Beckers, Niek and Siebert, Luciano Cavalcante and Bruijnes, Merijn and Jonker, Catholijn and Abbink, David |
| `beckers_drivers_2022` | Yes | `number` | (absent / removed) | 1 |
| `benabou_identity_2011` | No | `journal` | Quarterly Journal of Economics | The Quarterly Journal of Economics |
| `bigman_algorithmic_2023` | Yes | `annote` | VERIFY middle author spellings against the APA page | (absent / removed) |
| `blunden_downside_2023` | No | `pages` | (absent / removed) | 104251 |
| `blunden_downside_2023` | No | `doi` | (absent / removed) | 10.1016/j.obhdp.2023.104251 |
| `bockstedt_humans_2025` | No | `year` | 2025 | 2026 |
| `bogert_humans_2021` | No | `number` | (absent / removed) | 1 |
| `buiten_law_2023` | Yes | `doi` | (absent / removed) | 10.1016/j.clsr.2023.105794 |
| `buiten_law_2023` | Yes | `note` | CONFIRM volume and article number before adoption | (absent / removed) |
| `dawes_robust_1979` | Yes | `doi` | (absent / removed) | 10.1037/0003-066X.34.7.571 |
| `european_commission_liability_2019` | Yes | `author` | {European Commission} | {European Commission, Directorate-General for Justice and Consumers} |
| `european_commission_liability_2019` | Yes | `isbn` | (absent / removed) | 978-92-76-12959-2 |
| `european_union_ai_act_2024` | Yes | `howpublished` | Official Journal of the European Union | Official Journal of the European Union, L, 2024/1689, 12 July |
| `european_union_ai_act_2024` | Yes | `url` | (absent / removed) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng |
| `european_union_ai_act_2024` | Yes | `annote` | VERIFY citation form | (absent / removed) |
| `fiorina_legislator_1986` | Yes | `doi` | (absent / removed) | 10.1093/oxfordjournals.jleo.a036905 |
| `freer_friedman_weidenholzer_2024` | Yes | `entry_type` | unpublished | article |
| `freer_friedman_weidenholzer_2024` | Yes | `year` | 2024 | 2026 |
| `freer_friedman_weidenholzer_2024` | Yes | `month` | apr | sep |
| `freer_friedman_weidenholzer_2024` | Yes | `journal` | (absent / removed) | Games and Economic Behavior |
| `freer_friedman_weidenholzer_2024` | Yes | `volume` | (absent / removed) | 159 |
| `freer_friedman_weidenholzer_2024` | Yes | `pages` | (absent / removed) | 56--70 |
| `freer_friedman_weidenholzer_2024` | Yes | `doi` | (absent / removed) | 10.1016/j.geb.2026.05.012 |
| `freer_friedman_weidenholzer_2024` | Yes | `url` | https://arxiv.org/abs/2309.03419 | https://doi.org/10.1016/j.geb.2026.05.012 |
| `freer_friedman_weidenholzer_2024` | Yes | `note` | arXiv:2309.03419 [econ.GN], v3 15 April 2024. University of Essex / UCSC. | (absent / removed) |
| `freisinger_decoding_2024` | No | `year` | 2024 | 2025 |
| `freisinger_decoding_2024` | No | `volume` | (absent / removed) | 43 |
| `freisinger_decoding_2024` | No | `number` | (absent / removed) | 6 |
| `freisinger_decoding_2024` | No | `pages` | (absent / removed) | 958--969 |
| `freisinger_decoding_2024` | No | `doi` | 10.1016/j.emj.2024.102087 | 10.1016/j.emj.2024.10.004 |
| `freisinger_decoding_2024` | No | `url` | https://doi.org/10.1016/j.emj.2024.102087 | https://doi.org/10.1016/j.emj.2024.10.004 |
| `freisinger_decoding_2024` | No | `note` | Accepted 18 October 2024; article {102087} | (absent / removed) |
| `gawn_lying_2019` | Yes | `doi` | (absent / removed) | 10.1016/j.joep.2018.08.005 |
| `heaton_social_2023` | No | `note` | (absent / removed) | Article No. 11. |
| `huck_strategic_2004` | No | `doi` | 10.1016/j.ijindorg.2003.11.001 | 10.1016/j.ijindorg.2003.10.005 |
| `huck_strategic_2004` | No | `annote` | VERIFY doi | (absent / removed) |
| `jolly_not_2025` | No | `number` | (absent / removed) | 2 |
| `jones_have_1989` | No | `doi` | (absent / removed) | 10.1016/0167-2681(89)90011-5 |
| `jones_have_1989` | No | `annote` | VERIFY page range before submission | (absent / removed) |
| `jung_towards_2021` | No | `number` | (absent / removed) | 4 |
| `kandul_do_2018` | Yes | `doi` | (absent / removed) | 10.1016/j.socec.2018.03.006 |
| `killoran_learn_2026` | No | `annote` | VERIFY: author list extracted from web-search summary; PNAS page not directly fetched. Confirm before citing. | (absent / removed) |
| `kormylo_till_2025` | No | `year` | 2025 | 2026 |
| `kormylo_till_2025` | No | `author` | Kormylo, Cameron and Adjerid, Idris and Ball, Sheryl B. and Dogan, Can | Kormylo, Cameron and Adjerid, Idris and Ball, Sheryl and Dogan, Can |
| `lemley_remedies_2019` | Yes | `note` | CONFIRM page range against the journal listing before adoption. SSRN 3223621 | (absent / removed) |
| `lemley_remedies_2019` | Yes | `url` | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3223621 | https://lawreview.uchicago.edu/print-archive/remedies-robots |
| `litterscheidt_financial_2020` | No | `author` | Litterscheidt, Roman and Streich, David J. | Litterscheidt, Rouven and Streich, David J. |
| `maximiano_gift_2013` | No | `doi` | (absent / removed) | 10.1016/j.geb.2012.07.004 |
| `normann_delegate_2025` | No | `doi` | (absent / removed) | 10.48550/arXiv.2510.27636 |
| `pezzo_pezzo_physician_2006` | No | `annote` | VERIFY | (absent / removed) |
| `salatino_influence_2025` | No | `volume` | (absent / removed) | 15 |
| `salatino_influence_2025` | No | `pages` | (absent / removed) | 12329 |
| `santoni_de_sio_four_2021` | Yes | `number` | (absent / removed) | 4 |
| `santoni_de_sio_four_2021` | Yes | `author` | Santoni de Sio, Filippo and Mecacci, Giulio | {Santoni de Sio}, Filippo and Mecacci, Giulio |
| `schotter_bargaining_2000` | No | `annote` | VERIFY doi | (absent / removed) |
| `stein_dont_2020` | No | `entry` | Complete original record | Deleted |
| `sunstein_anatomy_2024` | Yes | `pages` | 290--319 | 290--317 |
| `sunstein_anatomy_2024` | Yes | `number` | (absent / removed) | 1 |
| `sunstein_anatomy_2024` | Yes | `doi` | (absent / removed) | 10.52214/stlr.v26i1.13339 |
| `sunstein_anatomy_2024` | Yes | `url` | (absent / removed) | https://journals.library.columbia.edu/index.php/stlr/article/view/13339 |
| `sunstein_anatomy_2024` | Yes | `journal` | Columbia Science and Technology Law Review | Science and Technology Law Review |
| `sunstein_anatomy_2024` | Yes | `annote` | VERIFY volume/pages against the published issue | (absent / removed) |
| `sunstein_anatomy_2024` | Yes | `year` | 2024 | 2025 |
| `sunstein_anatomy_2024` | Yes | `month` | (absent / removed) | jan |
| `tacconelli_how_2026` | Yes | `note` | (absent / removed) | Published online 4 June 2026; ahead of print. |
| `tacconelli_how_2026` | Yes | `annote` | Early online 4 June 2026 (ahead of print); add volume/pages at proof stage. Randomized vignette experiment, N=3,808 (US and German lay evaluators + 248 German physicians): physicians accepting standard-care AI recommendations judged significantly more reasonable than those rejecting them; equivalence for nonstandard recommendations. | Published online 4 June 2026; ahead of print as checked 5 September 2026. Analyzed N=2,808: 248 German physicians, 1,202 US adults, and 1,358 German adults. |
| `tontrup_strategic_2025` | Yes | `note` | SSRN Working Paper No.\ 5696827, posted 6 October 2025. | SSRN Working Paper No.\ 5696827. Written 6 October 2025; posted 13 November 2025; revised 27 June 2026. |
| `tontrup_strategic_2025` | Yes | `doi` | (absent / removed) | 10.2139/ssrn.5696827 |
| `tsumura_effects_2026` | No | `volume` | (absent / removed) | 16 |
| `tsumura_effects_2026` | No | `pages` | (absent / removed) | 2670 |
| `weitzner_reputational_2024` | No | `note` | arXiv:2402.15418 [econ.GN], v3 31 July 2024. McGill University. Presented at AEA 2025. | arXiv:2402.15418 [econ.TH], v3 31 July 2024. McGill University. Presented at AEA 2025. |
| `weitzner_reputational_2024` | No | `doi` | (absent / removed) | 10.48550/arXiv.2402.15418 |

## Preserved originals

- [Original bibliography snapshot](ProjectAlgorithm.bib.before-approved-changes).
- [Review report before implementation](REPORT.before-implementation.md).
- The pre-build manuscript PDF is preserved at `build/main.before-bibliography-update.pdf`.

Original bibliography SHA-256: `45446173e385d351df0168be5ef45dd99968fcc582f68936577e38c66c5b4471`.  
Final bibliography SHA-256: `50bc741e30a9ddedc77fed6c4c90730a332cad61c7c6d7e44446b34f77a889a5`.
