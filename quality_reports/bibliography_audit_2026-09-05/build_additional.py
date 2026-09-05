import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
inventory = json.loads((OUT / 'inventory.json').read_text(encoding='utf-8-sig'))
entries = {e['key']: e for e in inventory['entries']}
rows = []

def add(key, citation, sources, changes=(), limitations='', notes=''):
    e = entries[key]
    cs = []
    for field, new, reason in changes:
        cs.append({'field': field, 'old': e['fields'].get(field), 'new': new, 'reason': reason})
    status = 'verified_no_change'
    if cs:
        status = 'verified_completion_or_cleanup'
    if any(c['reason'].startswith('Correction:') for c in cs):
        status = 'verified_correction'
    rows.append({'key':key, 'cited':e['cited'], 'status':status, 'verified_citation':citation,
                 'changes':cs, 'sources':[{'title':t,'url':u} for t,u in sources],
                 'limitations':limitations, 'notes':notes,
                 'verification_scope':'Author identities/order, title, publication type, final publication year, venue, volume, issue where applicable, page range/article number, and DOI where present or proposed; source-access limitations stated separately.'})

add('jones_have_1989', 'Jones, Stephen R. G. (1989). Have your lawyer call my lawyer: Bilateral delegation in bargaining situations. Journal of Economic Behavior & Organization, 11(2), 159–174. DOI: 10.1016/0167-2681(89)90011-5.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/pii/0167268189900115'),('McMaster author publication record','https://experts.mcmaster.ca/scholarly-works/1440916')],
    [('doi','10.1016/0167-2681(89)90011-5','Optional completion: publisher identifies this DOI.'),('annote',None,'Cleanup: page range is confirmed; remove completed VERIFY reminder.')],
    notes='Publisher issue date is March 1989; McMaster uses a January 1 placeholder. Existing year is correct.')

add('schotter_bargaining_2000','Schotter, Andrew; Zheng, Wei; Snyder, Blaine (2000). Bargaining Through Agents: An Experimental Study of Delegation and Commitment. Games and Economic Behavior, 30(2), 248–292. DOI: 10.1006/game.1999.0728.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/pii/S0899825699907285')],
    [('annote',None,'Cleanup: DOI is confirmed by publisher; remove completed VERIFY reminder.')],notes='Final issue February 2000. The 1999 portion of the DOI does not change the citation year.')

add('huck_strategic_2004','Huck, Steffen; Müller, Wieland; Normann, Hans-Theo (2004). Strategic delegation in experimental markets. International Journal of Industrial Organization, 22(4), 561–574. DOI: 10.1016/j.ijindorg.2003.10.005.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/abs/pii/S0167718704000025'),('Tilburg publication record','https://research.tilburguniversity.edu/en/publications/strategic-delegation-in-experimental-markets/'),('Published article in Tilburg repository','https://pure.uvt.nl/ws/files/608080/Strategic.pdf')],
    [('doi','10.1016/j.ijindorg.2003.10.005','Correction: publisher and institutional record give this DOI; existing DOI is wrong.'),('annote',None,'Cleanup: replace VERIFY reminder with the verified DOI.')],notes='Final issue April 2004; publication details besides DOI match.')

add('gawn_lying_2019','Gawn, Glynis; Innes, Robert (2019). Lying through others: Does delegation promote deception? Journal of Economic Psychology, 71, 59–73. DOI: 10.1016/j.joep.2018.08.005.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/abs/pii/S0167487017305949'),('Robert Innes author publication list','https://robinnes.weebly.com/')],
    [('doi','10.1016/j.joep.2018.08.005','Optional completion: add DOI confirmed by the publisher.')],notes='Final issue March 2019; no issue number is displayed by publisher.')

add('gawn_machiavelli_2021','Gawn, Glynis; Innes, Robert (2021). Machiavelli Preferences Without Blame: Delegating Selfish vs. Generous Decisions in Dictator Games. Journal of Behavioral and Experimental Economics, 90, article 101615. DOI: 10.1016/j.socec.2020.101615.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/abs/pii/S2214804320302639')],notes='Final issue February 2021. Retain 2021 despite the 2020 DOI component. 101615 is an article number, not a page range.')

add('kandul_do_2018','Kandul, Serhiy; Kirchkamp, Oliver (2018). Do I care if others lie? Current and future effects when lies can be delegated. Journal of Behavioral and Experimental Economics, 74, 70–78. DOI: 10.1016/j.socec.2018.03.006.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/abs/pii/S2214804318301332'),('Author working-paper history','https://www.kirchkamp.de/research/delegation.html')],
    [('doi','10.1016/j.socec.2018.03.006','Optional completion: add publisher DOI.')],notes='Final issue June 2018. Existing title matches the final article; do not replace it with the different working-paper subtitle on the author website.')

add('garofalo_shifting_2018','Garofalo, Orsola; Rott, Christina (2018). Shifting Blame? Experimental Evidence of Delegating Communication. Management Science, 64(8), 3911–3925. DOI: 10.1287/mnsc.2017.2782.',
    [('Maastricht author publication record','https://cris.maastrichtuniversity.nl/en/publications/shifting-blame-experimental-evidence-of-delegating-communication/'),('Published article in VU repository','https://research.vu.nl/ws/portalfiles/portal/119346007/Shifting_blame_Experimental_evidence_of_delegating_communication.pdf')],notes='Early online 2017; final issue August 2018. The existing 2018 year is correct.')

add('charness_attribution_2004','Charness, Gary (2004). Attribution and Reciprocity in an Experimental Labor Market. Journal of Labor Economics, 22(3), 665–688. DOI: 10.1086/383111.',
    [('University of Chicago Press article','https://www.journals.uchicago.edu/doi/10.1086/383111'),('Journal issue contents','https://www.journals.uchicago.edu/toc/jole/2004/22/3')],notes='Final issue July 2004; all supplied citation fields match.')

add('maximiano_gift_2013','Maximiano, Sandra; Sloof, Randolph; Sonnemans, Joep (2013). Gift exchange and the separation of ownership and control. Games and Economic Behavior, 77(1), 41–60. DOI: 10.1016/j.geb.2012.07.004.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/pii/S089982561200098X')],
    [('doi','10.1016/j.geb.2012.07.004','Optional completion: add publisher DOI.')],notes='Final issue January 2013; retain 2013 despite the 2012 DOI component.')

add('candrian_rise_2022','Candrian, Cindy; Scherer, Anne (2022). Rise of the machines: Delegating decisions to autonomous AI. Computers in Human Behavior, 134, article 107308. DOI: 10.1016/j.chb.2022.107308.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/pii/S0747563222001303')],notes='Final issue September 2022; all supplied citation fields match. 107308 is an article number.')

add('germann_algorithm_2023','Germann, Maximilian; Merkle, Christoph (2023). Algorithm aversion in delegated investing. Journal of Business Economics, 93(9), 1691–1727. DOI: 10.1007/s11573-022-01121-9.',
    [('Springer article','https://link.springer.com/article/10.1007/s11573-022-01121-9'),('Final article in Aarhus repository','https://pure.au.dk/ws/files/384484032/s11573-022-01121-9.pdf'),('Publisher-supplied RePEc issue record','https://ideas.repec.org/a/spr/jbecon/v93y2023i9d10.1007_s11573-022-01121-9.html')],notes='Online 17 November 2022; final issue November 2023. Existing 2023 year is correct.')

add('holzmeister_delegation_2023','Holzmeister, Felix; Holmén, Martin; Kirchler, Michael; Stefan, Matthias; Wengström, Erik (2023). Delegation Decisions in Finance. Management Science, 69(8), 4828–4844. DOI: 10.1287/mnsc.2022.4555.',
    [('INFORMS article','https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4555'),('INFORMS final PDF','https://pubsonline.informs.org/doi/pdf/10.1287/mnsc.2022.4555')],notes='Online 4 October 2022; final PDF says Vol. 69, No. 8, August 2023, pp. 4828–4844. Retain 2023 even though web cite-as uses online year 2022.')

add('filiz_reducing_2021','Filiz, Ibrahim; Judek, Jan René; Lorenz, Marco; Spiwoks, Markus (2021). Reducing algorithm aversion through experience. Journal of Behavioral and Experimental Finance, 31, article 100524. DOI: 10.1016/j.jbef.2021.100524.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/pii/S221463502100068X')],notes='Final issue September 2021; all supplied citation fields match. 100524 is an article number.')

add('jung_towards_2021','Jung, Markus; Seiter, Mischa (2021). Towards a better understanding on mitigating algorithm aversion in forecasting: an experimental study. Journal of Management Control, 32(4), 495–516. DOI: 10.1007/s00187-021-00326-3.',
    [('Springer article','https://link.springer.com/article/10.1007/s00187-021-00326-3'),('Springer issue contents','https://link.springer.com/journal/187/volumes-and-issues/32-4'),('Author CV at Ulm','https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.125/documents/staff/CV_Seiter.pdf')],
    [('number','4','Optional completion: issue 4 is confirmed by Springer issue contents.')],notes='Online 28 September 2021; final issue December 2021.')

add('bigman_algorithmic_2023','Bigman, Yochanan E.; Wilson, Desman; Arnestad, Mads N.; Waytz, Adam; Gray, Kurt (2023). Algorithmic discrimination causes less moral outrage than human discrimination. Journal of Experimental Psychology: General, 152(1), 4–27. DOI: 10.1037/xge0001250.',
    [('APA article PDF (search-indexed)','https://www.apa.org/pubs/journals/releases/xge-xge0001250.pdf'),('PubMed APA-supplied bibliographic record','https://pubmed.ncbi.nlm.nih.gov/35758989/')],
    [('annote',None,'Cleanup: author spellings/order verified, including Desman Wilson; remove completed VERIFY reminder.')],
    limitations='APA direct access was blocked/challenged. Full citation and author spellings are supported by the APA-supplied PubMed record; APA PDF was available through search indexing.',
    notes='Early online 27 June 2022; final issue January 2023. Existing 2023 year and Desman spelling are correct.')

add('awad_drivers_2020','Awad, Edmond; Levine, Sydney; Kleiman-Weiner, Max; Dsouza, Sohan; Tenenbaum, Joshua B.; Shariff, Azim; Bonnefon, Jean-François; Rahwan, Iyad (2020). Drivers are blamed more than their automated cars when both make mistakes. Nature Human Behaviour, 4(2), 134–143. DOI: 10.1038/s41562-019-0762-8.',
    [('Nature article','https://www.nature.com/articles/s41562-019-0762-8'),('Nature issue contents','https://www.nature.com/nathumbehav/volumes/4/issues/2'),('Final article at author institution','https://compminds.uw.edu/pdfs/awad-2020drivers.pdf')],notes='Online 28 October 2019; final issue February 2020. Retain 2020; Dsouza is spelled correctly as published.')

add('meehl_clinical_1954','Meehl, Paul E. (1954). Clinical versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence. Minneapolis: University of Minnesota Press.',
    [('University of Minnesota author bibliography','https://meehl.umn.edu/lane-practice'),('1954 edition library catalog','https://openlibrary.org/books/OL6157448M/Clinical_versus_statistical_prediction')],
    limitations='University author bibliography confirms title, author, original publisher and year; Minneapolis is corroborated by the library catalog. No edition-specific DOI proposed.',
    notes='The 1996 Jason Aronson and 2013 Echo Point reprints do not require changing a citation to the original 1954 edition.')

add('dawes_robust_1979','Dawes, Robyn M. (1979). The Robust Beauty of Improper Linear Models in Decision Making. American Psychologist, 34(7), 571–582. DOI: 10.1037/0003-066X.34.7.571.',
    [('Published paper in Stanford repository','https://stanford.edu/~knutson/jdm/dawes79.pdf'),('Published paper in research lab repository','https://worthylab.org/wp-content/uploads/2020/12/dawes_1979_robustbeautylinearmodels.pdf'),('Crossref-derived record at Japan National Institute of Informatics','https://cir.nii.ac.jp/crid/1361981468461775488')],
    [('doi','10.1037/0003-066X.34.7.571','Optional completion: DOI identified in Crossref-derived NII record; article metadata matches the published paper.')],
    limitations='APA and PsycNet were robots-blocked. Original article PDF verifies existing metadata; DOI is corroborated by Crossref-derived NII metadata rather than direct APA access.',notes='Final issue July 1979; existing supplied citation fields are correct.')

add('ariely_large_2009','Ariely, Dan; Gneezy, Uri; Loewenstein, George; Mazar, Nina (2009). Large Stakes and Big Mistakes. The Review of Economic Studies, 76(2), 451–469. DOI: 10.1111/j.1467-937X.2009.00534.x.',
    [('Oxford University Press article','https://academic.oup.com/restud/article-abstract/76/2/451/1594205')],notes='Published 1 April 2009; all supplied citation fields match.')

add('dohmen_professionals_2008','Dohmen, Thomas J. (2008). Do professionals choke under pressure? Journal of Economic Behavior & Organization, 65(3–4), 636–653. DOI: 10.1016/j.jebo.2005.12.004.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/abs/pii/S016726810600196X'),('Elsevier author profile and publication listing','https://www.sciencedirect.com/author/7801649494/thomas-j-dohmen')],notes='Final combined issue March 2008; existing year is correct despite older DOI component. All supplied citation fields match.')

add('blunden_downside_2023','Blunden, Hayley; Steffel, Mary (2023). The downside of decision delegation: When transferring decision responsibility incurs interpersonal costs. Organizational Behavior and Human Decision Processes, 176, article 104251. DOI: 10.1016/j.obhdp.2023.104251.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/abs/pii/S0749597823000262')],
    [('pages','104251','Completion: add missing final article number; this is not a page range.'),('doi','10.1016/j.obhdp.2023.104251','Optional completion: add publisher DOI.')],notes='Final issue May 2023; existing title/authors/venue/volume/year match.')

add('arnestad_manual_2024','Arnestad, Mads N.; Meyers, Samuel; Gray, Kurt; Bigman, Yochanan E. (2024). The existence of manual mode increases human blame for AI mistakes. Cognition, 252, article 105931. DOI: 10.1016/j.cognition.2024.105931.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/pii/S0010027724002178'),('Hebrew University publication record','https://cris.huji.ac.il/en/publications/the-existence-of-manual-mode-increases-human-blame-for-ai-mistake-2/'),('PubMed publisher-supplied record','https://pubmed.ncbi.nlm.nih.gov/39208639/')],
    [('pages','105931','Completion: add missing final article number; this is not a page range.'),('doi','10.1016/j.cognition.2024.105931','Optional completion: add publisher DOI.')],notes='Online 28 August 2024; final issue November 2024. Existing title/authors/venue/volume/year match.')

add('allen_algorithm_2022','Allen, Ryan T.; Choudhury, Prithwiraj (Raj) (2022). Algorithm-Augmented Work and Domain Experience: The Countervailing Forces of Ability and Aversion. Organization Science, 33(1), 149–169. DOI: 10.1287/orsc.2021.1554.',
    [('INFORMS article','https://pubsonline.informs.org/doi/10.1287/orsc.2021.1554'),('INFORMS issue contents','https://pubsonline.informs.org/toc/orsc/33/1')],
    [('author','Allen, Ryan T. and Choudhury, Prithwiraj (Raj)','Optional author-name completion: match the fuller names printed by publisher; existing abbreviated forms identify the same authors.'),('doi','10.1287/orsc.2021.1554','Optional completion: add publisher DOI.')],notes='Online 3 December 2021; final issue January–February 2022. Retain 2022 despite web cite-as using online year 2021.')

add('beckers_drivers_2022','Beckers, Niek; Siebert, Luciano Cavalcante; Bruijnes, Merijn; Jonker, Catholijn; Abbink, David (2022). Drivers of partially automated vehicles are blamed for crashes that they cannot reasonably avoid. Scientific Reports, 12(1), article 16193. DOI: 10.1038/s41598-022-19876-0.',
    [('Nature article and citation','https://www.nature.com/articles/s41598-022-19876-0'),('TU Delft citation export','https://research.tudelft.nl/en/publications/drivers-of-partially-automated-vehicles-are-blamed-for-crashes-th/'),('Publisher Crossmark authors','https://crossmark.crossref.org/dialog/?doi=10.1038%2Fs41598-022-19876-0'),('PubMed publisher-supplied record','https://pubmed.ncbi.nlm.nih.gov/36171437/')],
    [('author','Beckers, Niek and Siebert, Luciano Cavalcante and Bruijnes, Merijn and Jonker, Catholijn and Abbink, David','Correction: publisher citation, Crossmark, and university export treat Siebert as the family name and Luciano Cavalcante as given names; current BibTeX comma incorrectly makes Cavalcante part of the surname.'),('number','1','Optional completion: issue 1 is recorded by publisher-supplied PubMed metadata and TU Delft.')],notes='Published 28 September 2022. Other supplied fields match; 16193 is an article number.')

add('gill_blame_2020','Gill, Tripat (2020). Blame It on the Self-Driving Car: How Autonomous Vehicles Can Alter Consumer Morality. Journal of Consumer Research, 47(2), 272–291. DOI: 10.1093/jcr/ucaa018.',
    [('Oxford University Press article','https://academic.oup.com/jcr/article-abstract/47/2/272/5819144'),('Journal issue contents','https://academic.oup.com/jcr/issue/47/2')],notes='Online 11 April 2020; final issue August 2020. All supplied citation fields match.')

add('ismagilova_aint_2025','Ismagilova, Zilia; Ploner, Matteo (2025). Ain’t blaming you: Delegation of financial decisions to humans and algorithms. Computers in Human Behavior: Artificial Humans, 4, article 100147. DOI: 10.1016/j.chbah.2025.100147.',
    [('Elsevier article','https://www.sciencedirect.com/science/article/pii/S2949882125000313'),('Publisher article with linked correction notice','https://doi.org/10.1016/j.chbah.2025.100147'),('University of Trento publication record','https://iris.unitn.it/handle/11572/450551')],
    limitations='Publisher links a May 2026 multi-article erratum concerning ethical approval/informed consent (volume 8, article 100317). Its full text was not independently retrieved; the original article now displays an Ethical Statement. No evidence of altered bibliographic metadata.',
    notes='Final issue May 2025. All supplied bibliographic fields match. Record the correction notice in the audit; no automatic extra bibliography entry or change to the original citation is proposed.')

add('matthias_responsibility_2004','Matthias, Andreas (2004). The responsibility gap: Ascribing responsibility for the actions of learning automata. Ethics and Information Technology, 6(3), 175–183. DOI: 10.1007/s10676-004-3422-1.',
    [('Springer article','https://link.springer.com/article/10.1007/s10676-004-3422-1'),('Springer issue contents','https://link.springer.com/journal/10676/volumes-and-issues/6-3')],notes='Final issue September 2004; all supplied citation fields match.')

add('santoni_de_sio_four_2021','Santoni de Sio, Filippo; Mecacci, Giulio (2021). Four Responsibility Gaps with Artificial Intelligence: Why they Matter and How to Address them. Philosophy & Technology, 34(4), 1057–1084. DOI: 10.1007/s13347-021-00450-x.',
    [('Springer article','https://link.springer.com/article/10.1007/s13347-021-00450-x'),('Springer issue contents','https://link.springer.com/journal/13347/volumes-and-issues/34-4')],
    [('number','4','Optional completion: add issue confirmed by publisher contents.')],notes='Online 14 May 2021; final issue December 2021. Existing title capitalization is a style difference; no title correction needed.')

assert set(r['key'] for r in rows) == set(inventory['assignments']['additional'])
(OUT / 'additional.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
md = ['# Additional bibliography audit — 5 September 2026', '',
      'Proposal only. No bibliography or manuscript file was changed. All 28 assigned entries were reviewed individually. Existing final-year citations were retained where they differ from online-first dates. Capitalization differences are treated as style, and article identifiers stored in `pages` are not treated as page ranges. DOI, issue, and fuller-author-name additions are marked separately from corrections.', '',
      '## Planned substantive corrections and missing locators', '',
      '- `beckers_drivers_2022` (cited): change second author from `Cavalcante Siebert, Luciano` to `Siebert, Luciano Cavalcante` to match the publisher’s family-name parsing.',
      '- `huck_strategic_2004` (uncited): replace incorrect DOI `10.1016/j.ijindorg.2003.11.001` with `10.1016/j.ijindorg.2003.10.005`.',
      '- `blunden_downside_2023` (uncited): add article number `104251` and optionally DOI.',
      '- `arnestad_manual_2024` (uncited): add article number `105931` and optionally DOI.', '',
      'Optional DOI/issue/author-name completions and resolved VERIFY reminders are enumerated below. All assigned entries already describe published articles or a published book; no working-paper-to-journal conversion is required in this group.', '',
      '## Individual evidence ledger', '']
for r in sorted(rows,key=lambda x:(not x['cited'], inventory['assignments']['additional'].index(x['key']))):
    md += [f"### `{r['key']}` — {'cited' if r['cited'] else 'uncited'}; {r['status']}", '',r['verified_citation'],'']
    if r['changes']:
        for c in r['changes']:
            old = '(absent)' if c['old'] is None else c['old']
            new = '(remove field)' if c['new'] is None else c['new']
            md.append(f"- `{c['field']}`: `{old}` → `{new}`. {c['reason']}")
    else:
        md.append('No bibliographic change proposed.')
    md += ['',r['notes'],'']
    if r['limitations']:
        md += ['Access/verification limitation: '+r['limitations'],'']
    md += ['Evidence: '+ '; '.join(f"[{s['title']}]({s['url']})" for s in r['sources']) + '.', '']
(OUT / 'additional.md').write_text('\n'.join(md),encoding='utf-8')
print(json.dumps({'entries':len(rows),'cited':sum(r['cited'] for r in rows),'with_proposals':sum(bool(r['changes']) for r in rows)},indent=2))
