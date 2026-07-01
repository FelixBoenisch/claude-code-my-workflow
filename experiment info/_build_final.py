import csv, re, subprocess, os
from collections import Counter
def pdf_ids(pdf):
    t=subprocess.run(["pdftotext","-layout",pdf,"-"],capture_output=True,text=True).stdout
    return set(re.findall(r"[0-9a-f]{24}",t))
def parse(path):
    rows=[]
    for b in open(path,encoding="utf-8").read().strip().split("\n\n"):
        L=[x.strip() for x in b.splitlines() if x.strip()]
        i=[x for x in L if re.fullmatch(r"[0-9a-f]{24}",x)][0]
        d=[x for x in L if re.search(r"\d{1,2} \w{3} \d{4}, \d{2}:\d{2}",x)][0].replace(",","")
        t=[x for x in L if re.fullmatch(r"\d{2}:\d{2}:\d{2}",x)][0]
        bn=[x for x in L if x.startswith("£")]
        rows.append({"prolific_id":i,"started":d,"time_taken":t,"bonus":bn[0][1:] if bn else ""})
    return rows

master=list(csv.DictReader(open("submissions_digitized.csv",encoding="utf-8")))
dela_ids ={r["prolific_id"] for r in master if r["png_file"]=="Main I - dela.png"}
eva1a_ids={r["prolific_id"] for r in master if r["png_file"]=="Main I - no punish - eva1a.png"}

del_rows=parse("raw_pastes/del.txt")
for r in del_rows:
    r["png_file"]="Main I - dela.png" if r["prolific_id"] in dela_ids else "Main I - delb.png"
    r["id_source"]="manual_paste"
eva1_rows=parse("raw_pastes/eva1.txt")
for r in eva1_rows:
    r["png_file"]="Main I - no punish - eva1a.png" if r["prolific_id"] in eva1a_ids else "Main I - no punish - eva1b.png"
    r["id_source"]="manual_paste"

cols=["prolific_id","started","time_taken","bonus","png_file","id_source"]
final=[]; done=set()
for r in master:
    if r["png_file"]=="Main I - dela.png":
        if "del" not in done: final+=del_rows; done.add("del")
    elif r["png_file"]=="Main I - no punish - eva1a.png":
        if "eva1" not in done: final+=eva1_rows; done.add("eva1")
    else:
        final.append(r)

with open("submissions_digitized.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for r in final: w.writerow({c:r.get(c,"") for c in cols})

# ---- validation ----
ids=[r["prolific_id"] for r in final]
print("TOTAL rows:",len(final))
print("unique ids:",len(set(ids)),"  duplicates:",[i for i,c in Counter(ids).items() if c>1] or "none")
print("id lengths:",dict(Counter(len(i) for i in ids)))
print("bad time fmt:",[r["prolific_id"] for r in final if not re.fullmatch(r'\d{2}:\d{2}:\d{2}',r["time_taken"])] or "none")
print("bad started fmt:",[r["prolific_id"] for r in final if not re.search(r'\d{1,2} \w{3} \d{4} \d{2}:\d{2}',r["started"])] or "none")
print("bad bonus fmt:",[r["bonus"] for r in final if r["bonus"] and not re.fullmatch(r'\d+\.\d{2}',r["bonus"])] or "none")
print("blank-bonus rows:",sum(1 for r in final if r["bonus"]==""))
print("id_source:",dict(Counter(r["id_source"] for r in final)))
# cross-check against full invoice universe
allinv=set()
for p in os.listdir("."):
    if p.endswith(".pdf"): allinv|=pdf_ids(p)
print("ids not in any invoice:",[i for i in set(ids) if i not in allinv] or "none")
print("invoice ids missing from csv:",len(allinv-set(ids)))
# per-study counts
print("\nrows per png_file:")
for k,v in sorted(Counter(r["png_file"] for r in final).items()): print(f"  {v:>3}  {k}")
