import re, subprocess, sys, os
def pdf_ids(pdf):
    t=subprocess.run(["pdftotext","-layout",pdf,"-"],capture_output=True,text=True).stdout
    return set(re.findall(r"[0-9a-f]{24}",t))
def parse(path):
    blocks=open(path,encoding="utf-8").read().strip().split("\n\n")
    rows=[]
    for b in blocks:
        L=[x.strip() for x in b.splitlines() if x.strip()]
        idm=[x for x in L if re.fullmatch(r"[0-9a-f]{24}",x)]
        dt =[x for x in L if re.search(r"\d{1,2} \w{3} \d{4}, \d{2}:\d{2}",x)]
        tt =[x for x in L if re.fullmatch(r"\d{2}:\d{2}:\d{2}",x)]
        bn =[x for x in L if x.startswith("£")]
        if not(idm and dt and tt):
            print("  !! could not parse block:",L); continue
        rows.append((idm[0], dt[0].replace(",",""), tt[0], bn[0][1:] if bn else ""))
    return rows
def main(raw,pdf):
    inv=pdf_ids(pdf); rows=parse(raw)
    ids=[r[0] for r in rows]
    print(f"parsed rows: {len(rows)}   invoice size: {len(inv)}")
    bad=[i for i in ids if i not in inv]
    dup=[i for i in set(ids) if ids.count(i)>1]
    print("ids NOT in invoice:", bad or "none")
    print("duplicate ids in paste:", dup or "none")
    missing=sorted(inv-set(ids))
    print(f"still missing from this study: {len(missing)}")
    for m in missing: print("   ",m)
if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
