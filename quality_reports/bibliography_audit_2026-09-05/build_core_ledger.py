import json
from pathlib import Path
from html import unescape

base = Path(__file__).parent
inv = json.loads((base/'inventory.json').read_text(encoding='utf-8-sig'))
entries = {e['key']: e for e in inv['entries']}
metadata = {e['key']: e['metadata'] for e in json.loads((base/'core_crossref.json').read_text(encoding='utf-8-sig')) if e.get('metadata')}

sources = {
 'feier_hiding_2022': [('Springer article and citation metadata','https://link.springer.com/article/10.1007/s11948-022-00372-7')],
 'bartling_shifting_2012': [('Published article in institutional archive','https://doc.rero.ch/record/290015/files/rdr023.pdf'),('Author institutional publication list','https://www.econ.uzh.ch/en/people/faculty/bartling/research.html')],
 'coffman_intermediation_2011': [('American Economic Association article','https://www.aeaweb.org/articles?id=10.1257/mic.3.4.77')],
 'hamman_self-interest_2010': [('American Economic Association article','https://www.aeaweb.org/articles?id=10.1257/aer.100.4.1826')],
 'oexl_shifting_2013': [('Original Springer article and issue date','https://link.springer.com/article/10.1007/s10683-012-9335-7')],
 'steffel_passing_2016': [('Elsevier article metadata','https://www.sciencedirect.com/science/article/pii/S0749597815300108')],
 'hill_does_2015': [('Wiley article metadata','https://onlinelibrary.wiley.com/doi/10.1111/jels.12074')],
 'dietvorst_algorithm_2015': [('Author institutional manuscript','https://repository.upenn.edu/server/api/core/bitstreams/4d24c079-228b-47bd-ba8c-166eeddee8de/content')],
 'logg_algorithm_2019': [('Published article, author-hosted copy','https://coral-beige-dbda.squarespace.com/s/Algorithm-Appreciation-People-prefer-algorithmic-to-human-judgment.pdf')],
 'burton_systematic_2020': [('Wiley article metadata and publication dates','https://onlinelibrary.wiley.com/doi/10.1002/bdm.2155')],
 'chugunova_we_2022': [('ETH record documenting earlier working paper and link to later version','https://www.research-collection.ethz.ch/handle/20.500.11850/442053?locale-attribute=en')],
 'mahmud_what_2022': [('Elsevier article','https://doi.org/10.1016/j.techfore.2021.121390'),('Author dissertation containing published article','https://lutpub.lut.fi/bitstream/handle/10024/168356/Hasan%20Mahmud_A4.pdf?isAllowed=y&sequence=1')],
 'trunk_current_2020': [('Springer article metadata','https://link.springer.com/article/10.1007/s40685-020-00133-x')],
 'gogoll_rage_2018': [('Author dissertation containing published article','https://mediatum.ub.tum.de/doc/1449095/document.pdf')],
 'kirchkamp_sharing_2019': [('Author publication list','https://www.kirchkamp.de/'),('Author article status page','https://www.kirchkamp.de/research/shareMachine.html')],
 'maasland_blame_2022': [('Frontiers published article','https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.779028/full')],
 'heaton_social_2023': [('ACM article metadata','https://doi.org/10.1145/3597512.3599706'),('Author institutional publication record','https://highlights.cdt.horizon.ac.uk/students/psxdh7-1'),('Institutional record for same proceedings ISBN and venue','https://research.aber.ac.uk/en/publications/a-practical-taxonomy-of-tas-related-usecase-scenarios/')],
 'weaver_politics_1986': [],
 'fiorina_legislator_1986': [('Oxford University Press article metadata','https://academic.oup.com/jleo/article-abstract/2/1/33/873292')],
 'berger_watch_2021': [('Springer article and issue date','https://link.springer.com/article/10.1007/s12599-020-00678-5')],
 'litterscheidt_financial_2020': [('Elsevier published article metadata','https://www.sciencedirect.com/science/article/abs/pii/S2214804319304367'),('Authors original replication data','https://data.mendeley.com/datasets/zhbzv9jtww/1')],
 'sharan_dont_2020': [('NLM PubMed article record','https://pubmed.ncbi.nlm.nih.gov/32923706/')],
 'bigman_people_2018': [('Author institutional research record','https://cris.iucc.ac.il/en/publications/people-are-averse-to-machines-making-moral-decisions/')],
 'jauernig_people_2022': [('Springer article metadata','https://link.springer.com/article/10.1007/s13347-021-00495-y')],
 'dietvorst_people_2020': [('SAGE article metadata','https://journals.sagepub.com/doi/10.1177/0956797620948841')],
 'dietvorst_overcoming_2018': [('Published article on author university website','https://faculty.wharton.upenn.edu/wp-content/uploads/2016/08/Dietvorst-Simmons-Massey-2018.pdf')],
 'castelo_task-dependent_2019': [],
 'bogert_humans_2021': [('Nature published article metadata','https://www.nature.com/articles/s41598-021-87480-9')],
 'goldbach_geht_2019': [],
 'niszczota_robo-investors_2020': [('PLOS published article and citation','https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0239277')],
}

notes = {
 'feier_hiding_2022': 'Published 4 April 2022; 19 is the article number, not a single-page citation. Issue 2 confirmed in publisher-deposited Crossref metadata.',
 'bartling_shifting_2012': 'Online 8 August 2011; final issue January 2012. Keep year 2012. Publisher metadata uses initials; published PDF supplies full given names.',
 'coffman_intermediation_2011': 'November 2011 issue. The missing period after middle initial C is typographic normalization only.',
 'hamman_self-interest_2010': 'September 2010 issue. Publisher abbreviates final page as 46; 1826–1846 is the same correct range. Periods after middle initials are optional typography.',
 'oexl_shifting_2013': 'Original Springer page: online 26 July 2012, issue September 2013. Keep 2013. Crossref online date 14 March 2025 is inconsistent with original publication history and should not replace the original date; it appears associated with later platform hosting.',
 'steffel_passing_2016': 'July 2016 volume; no issue number in Elsevier/Crossref citation metadata.',
 'hill_does_2015': 'Online 28 April 2015; June 2015 issue. Both subtitle and all core citation fields confirmed.',
 'dietvorst_algorithm_2015': 'Final 2015 volume 144(1), 114–126 confirmed in APA-deposited Crossref metadata. Institutional early manuscript shows provisional 2014/143/000 metadata, which must not replace final publication details. APA article page blocked direct retrieval.',
 'logg_algorithm_2019': 'Available online 5 February 2019; March 2019 volume. DOI contains 2018 but citation year 2019 is correct.',
 'burton_systematic_2020': 'Online 23 October 2019; April 2020 issue. Keep year 2020. Mari‐Klara uses a valid Unicode hyphen in the file; this is not a corrupted author name.',
 'chugunova_we_2022': 'Earlier working paper exists, but entry already cites final journal article: August 2022, volume 99, article 101897. Final title/authors/DOI/locator independently confirmed in Elsevier-deposited Crossref metadata; direct Elsevier page blocked.',
 'mahmud_what_2022': 'February 2022 volume. DOI/copyright contain 2021, but final citation year 2022 is correct. Article number 121390.',
 'trunk_current_2020': 'Online 20 November 2020; November 2020 issue 3. Core fields and ISSNs match.',
 'gogoll_rage_2018': 'June 2018 volume; core fields verified from Elsevier-deposited Crossref and the published article reproduced in the author dissertation.',
 'kirchkamp_sharing_2019': 'Accepted February 2019 according to author; final June 2019 publication already correctly recorded, 80:25–33.',
 'maasland_blame_2022': 'Published 25 May 2022. 779028 is an article number; authors, title, volume and DOI match.',
 'heaton_social_2023': 'Published proceedings paper, 11 July 2023; ACM Article No. 11, pages 1–11. ISBN 9798400707346 and Edinburgh conference venue confirmed for these proceedings. Crossref distinguishes publisher location New York, NY, USA from event location Edinburgh United Kingdom. Existing address is the true conference venue; publisher-address normalization is optional.',
 'weaver_politics_1986': 'Original issue October–December 1986 (Crossref print month October). Later online hosting date 28 November 2008 must not replace 1986. All core fields verified in CUP-deposited Crossref metadata; direct publisher page blocked.',
 'fiorina_legislator_1986': 'OUP confirms spring 1986, 2(1), 33–51, full author and title. Journal ampersand versus “and” is an accepted name/style variation; no correction needed.',
 'berger_watch_2021': 'Online 4 December 2020; February 2021 issue. Keep 2021. Existing TeX umlaut in Rühr and em-dash title separator correctly represent publisher spelling.',
 'litterscheidt_financial_2020': 'August 2020 volume 87, article 101573. First author is Rouven, not Roman; verified independently by Elsevier page, publisher-deposited Crossref metadata and authors replication data. Other core fields match.',
 'sharan_dont_2020': 'Published 28 August 2020; 6(8), e04572. Both full author names and order match NLM/Elsevier metadata. Citation key does not need to match the final title.',
 'bigman_people_2018': 'Final December 2018 volume 181, 21–34, confirmed by Elsevier-deposited metadata and author institutional record.',
 'jauernig_people_2022': 'Published online 26 January 2022; March 2022 issue 1. The DOI includes 2021 but citation year 2022 is correct. 2 is the article number.',
 'dietvorst_people_2020': 'Online 11 September 2020; October 2020 issue. Full title, authors and order, 31(10), 1302–1314 and DOI match SAGE.',
 'dietvorst_overcoming_2018': 'Online in Articles in Advance 4 November 2016; final March 2018 issue 64(3), 1155–1170. Keep 2018.',
 'castelo_task-dependent_2019': 'Online 15 July 2019; October 2019 issue. All core fields verified in SAGE-deposited Crossref metadata; direct SAGE retrieval blocked.',
 'bogert_humans_2021': 'Published 13 April 2021. Article 8028, not page 8028. Crossref supplies issue 1, although Nature recommended citation omits issue; adding it is optional.',
 'goldbach_geht_2019': 'Elsevier-deposited Crossref metadata verifies the current English title, all four authors, year, volume, page range and DOI. The existing annotation records a separate unresolved question about whether this paper was the author’s intended source for an earlier German title; bibliographic identity is verified but author intent cannot be inferred. Preserve that intent question until resolved.',
 'niszczota_robo-investors_2020': 'Published 17 September 2020. Authors Paweł Niszczota and Dániel Kaszás, 15(9), e0239277 and DOI match. PLoS ONE versus PLOS ONE is capitalization only.',
}

rows=[]
for key in inv['assignments']['core']:
    e=entries[key]; f=e['fields']; m=metadata.get(key)
    if m:
        author='; '.join(a['given']+' '+a['family'] for a in m['author'])
        title=unescape(m['title'][0]); venue=unescape(m['container-title'][0])
        vol=m.get('volume',''); issue=m.get('issue',''); loc=m.get('article-number') or m.get('page','')
        locator=('Article '+loc) if m.get('article-number') else loc.replace('-', '–')
        suffix=(vol+('('+issue+')' if issue else '')+(': '+locator if locator else '')).strip(': ')
        if key=='heaton_social_2023': suffix='ACM, Article 11, pp. 1–11'
        citation=f'{author} ({f["year"]}). {title.rstrip(".")}. {venue}, {suffix}. DOI: {m["DOI"]}.'
    else:
        citation='Morris P. Fiorina (1986). Legislator Uncertainty, Legislative Control, and the Delegation of Legislative Power. The Journal of Law, Economics, and Organization, 2(1): 33–51. DOI: 10.1093/oxfordjournals.jleo.a036905.'
    src=[{'title':t,'url':u} for t,u in sources[key]]
    if m: src.append({'title':'Publisher-deposited Crossref metadata (retrieved 2026-09-05)','url':'https://api.crossref.org/works/'+m['DOI']})
    changes=[]; status='verified_no_change'
    if key=='litterscheidt_financial_2020':
        status='correction_required'
        changes=[{'field':'author','old':f['author'],'new':'Litterscheidt, Rouven and Streich, David J.','reason':'Necessary correction: first author’s given name is Rouven, not Roman.'}]
    if key=='bartling_shifting_2012':
        status='verified_optional_enrichment'
        changes=[{'field':'author','old':f['author'],'new':'Bartling, Bj{\\"o}rn and Fischbacher, Urs','reason':'Optional consistency only: expand correct initials using published PDF. No author identity/order error.'}]
    if key=='fiorina_legislator_1986':
        status='verified_optional_enrichment'
        changes=[{'field':'doi','old':None,'new':'10.1093/oxfordjournals.jleo.a036905','reason':'Optional missing persistent identifier, verified on OUP article page.'}]
    if key=='heaton_social_2023':
        status='verified_optional_enrichment'
        changes=[{'field':'articleno','old':None,'new':'11','reason':'Optional ACM proceedings locator completion; existing 1–11 page range is correct. Use only a field supported by bibliography style.'}]
    if key=='bogert_humans_2021':
        status='verified_optional_enrichment'
        changes=[{'field':'number','old':None,'new':'1','reason':'Optional issue completion from publisher-deposited Crossref; Nature recommended citation uses volume and article number without issue.'}]
    limits=[]
    if key in ('dietvorst_algorithm_2015','chugunova_we_2022','weaver_politics_1986','castelo_task-dependent_2019','goldbach_geht_2019'):
        limits.append('Core fields verified from publisher-deposited DOI metadata; direct publisher article retrieval unavailable. This is metadata verification, not an assessment of research claims.')
    if key=='goldbach_geht_2019': limits.append('Intended-source question in existing annote remains unresolved; no bibliography replacement or annotation removal proposed.')
    rows.append({'key':key,'cited':e['cited'],'status':status,'verified_citation':citation,'changes':changes,'sources':src,'limitations':limits,'verification_notes':notes[key]})

(base/'core.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
out=['# Bibliography audit — core assignment','', 'As of 2026-09-05. Proposal only; bibliography and manuscript files were not edited.','',
     f'Coverage: {len(rows)} entries, {sum(r["cited"] for r in rows)} currently cited. All 30 are already recorded as published journal/proceedings papers and their publication status is confirmed; no working-paper-to-journal conversion is needed in this assignment. One factual correction (uncited), four optional enrichments.','',
     'Verification compared author identity/order and spelling, full title, journal/proceedings, final year, volume, issue when applicable, page range/article number, DOI, entry type, and existing month/ISSN where present. Publisher-deposited DOI metadata was fetched individually for 29 entries; the remaining Fiorina entry was verified on OUP. Raw evidence: `core_crossref.json`. Earlier online years were distinguished from final issue years. Bibliographic title capitalization, valid TeX accents, DOI capitalization, and article-number storage in `pages` are not treated as factual errors. Local Zotero file links, historical access dates, abstract text and research-claim annotations are outside metadata verification.','',
     '## Planned changes for review','',
     '| Entry | Cited? | Planned change | Priority |','|---|---|---|---|']
for r in rows:
    for c in r['changes']:
        out.append(f'| `{r["key"]}` | {"Yes" if r["cited"] else "No"} | `{c["field"]}`: {c["old"] or "missing"} → {c["new"]}. {c["reason"]} | {"Correction" if r["status"]=="correction_required" else "Optional"} |')
out += ['', 'No automatic title/key substitutions are proposed. The existing Goldbach annotation about the intended source should remain pending author clarification. For Heaton, Edinburgh is the verified conference venue; New York is ACM’s publisher location. Changing the address convention would be optional and is not included among the proposed field changes.','', '## Individual verification ledger','']
for r in rows:
    out += [f'### `{r["key"]}` — {"cited" if r["cited"] else "uncited"}', '', r['verified_citation'],'',r['verification_notes'],'',f'Outcome: **{r["status"]}**.']
    if r['changes']:
        out += ['', *[f'- {c["reason"]} `{c["field"]}`: `{c["old"] or "missing"}` → `{c["new"]}`.' for c in r['changes']]]
    out += ['', 'Evidence: '+ '; '.join(f'[{s["title"]}]({s["url"]})' for s in r['sources'])+'.']
    if r['limitations']: out += ['', 'Limitations: '+' '.join(r['limitations'])]
    out += ['']
(base/'core.md').write_text('\n'.join(out),encoding='utf-8')
print(json.dumps({'count':len(rows),'cited':sum(r['cited'] for r in rows),'changed_entries':[r['key'] for r in rows if r['changes']],'outputs':['core.json','core.md']},indent=2))
