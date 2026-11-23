import re, json, sys
src = sys.argv[1]
lines = open(src, encoding="utf-8").read().split("\n")
sections, cur, q = [], None, None
def flush():
    global q
    if q and cur is not None:
        cur["questions"].append(q)
    q = None
for ln in lines:
    m = re.match(r"^## ([A-Z])\. (.+)$", ln)
    if m:
        flush(); cur = {"id": m.group(1), "title": m.group(2), "questions": []}; sections.append(cur); continue
    if ln.startswith("### "):
        flush(); cur = None; continue
    m = re.match(r"^\*\*(M\d+)\. (.*?)\*\*(.*)$", ln)
    if m and cur is not None:
        flush()
        rest = m.group(3)
        tag = "sart" if "BAŞLAMADAN" in rest else "sonra"
        extra = re.sub(r"\[.*?\]|🔗\s*X\d+", "", rest).strip()
        q = {"id": m.group(1), "text": m.group(2).strip(), "extra": extra, "tag": tag,
             "notes": [], "options": [], "why": ""}
        continue
    if q is None: continue
    s = ln.strip()
    if s.startswith("> Neden önemli:"):
        q["why"] = s.split(":", 1)[1].strip(); continue
    if not s: continue
    if re.match(r"^[A-F]\) ", s):
        parts = re.split(r"\s{2,}(?=[A-F]\) )", s)
        for p in parts:
            p = re.sub(r"^[A-F]\)\s*", "", p).strip()
            mm = re.match(r"^(.*?)\s+—\s+(.*)$", p)
            if mm and "Süre" in mm.group(2):
                q["options"].append(mm.group(1).strip()); q["notes"].append(mm.group(2).strip())
            else:
                q["options"].append(p)
        continue
    q["notes"].append(s)
flush()
for sec in sections:
    for qq in sec["questions"]:
        blob = qq["text"] + " " + qq["extra"] + " " + " ".join(qq["notes"])
        qq["multi"] = bool(re.search(r"Seçilebilir|Birden fazla seçebilirsin", blob))
        # drop "Başka: ____" style options; free-text box is always present
        qq["options"] = [o for o in qq["options"] if "____" not in o]
        # option with trailing "— Süre" handled; "Bilmiyorum" stays
json.dump(sections, sys.stdout, ensure_ascii=False, indent=1)
