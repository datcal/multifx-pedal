"""Müzisyen soru listesinden (01-muzisyen-sorulari.md) tek dosyalık HTML form üretir.
Kullanım: python3 docs/tools/build_form.py"""
import json, subprocess, pathlib, re
here = pathlib.Path(__file__).resolve().parent
docs = here.parent
data = json.loads(subprocess.check_output(["python3", str(here/"parse_questions.py"), str(docs/"01-muzisyen-sorulari.md")]))
YN = ["Evet", "Hayır", "Emin değilim"]
QUICK = {q: YN for q in ["M10","M13","M14","M35","M37","M40","M41","M44","M47","M48","M53","M57","M39"]}
QUICK.update({
 "M8":  ["Kablolu", "Kablosuz", "İkisi de"],
 "M31": ["Koyu (siyah zemin)", "Açık renkli", "Fark etmez"],
 "M33": ["Sürekli yansın", "Belli süre sonra kararsın", "Fark etmez"],
 "M50": ["Yerde tek başına", "Pedal tahtasına sabit", "İkisi de"],
 "M54": ["Sahne için (daha az parlak)", "Oda için", "Fark etmez"],
 "M65": ["Sadece ben", "Başkaları da kullanacak", "Bilmiyorum"],
})
for s in data:
    for q in s["questions"]:
        q["notes"] = [n for n in q["notes"] if n != "---"]
        if not q["options"] and q["id"] in QUICK:
            q["options"] = QUICK[q["id"]]
tpl = (here/"form_template.html").read_text(encoding="utf-8")
out = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False))
(docs/"muzisyen-formu.html").write_text(out, encoding="utf-8")
# Artifact sürümü: <html>/<head>/<body> sarmalayıcısız parça
frag = re.sub(r'^<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*','',out)
frag = frag.replace("</head>\n<body>","").replace("</body>\n</html>","")
(docs/"muzisyen-formu.artifact.html").write_text(frag, encoding="utf-8")
(docs/"index.html").write_text(out, encoding="utf-8")
print("ok", sum(len(s["questions"]) for s in data), "soru")
