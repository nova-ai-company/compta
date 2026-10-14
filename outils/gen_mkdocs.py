"""Génère mkdocs.yml (navigation) à partir du contenu de formation/."""
import glob, os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "formation")


def title(path, strip_code=True):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                t = line[2:].strip()
                if strip_code:
                    t = re.sub(r"^(Corrigé\s+)?E\d\d-\d\d[a-z]?\s*[—:-]\s*", "", t)
                    t = re.sub(r"^M\d\d\s*[—:-]\s*", "", t)
                return t.replace('"', "'")
    return os.path.basename(path)


def rel(p):
    return os.path.relpath(p, DOCS)


def q(s):
    return json.dumps(s, ensure_ascii=False)


nav = [
    ("Accueil", "index.md"),
    ("Mode d'emploi", "00_LISEZ-MOI.md"),
    ("Portefeuille clients", "01_PORTEFEUILLE_CLIENTS.md"),
    ("Codes et sigles expliqués", "04_CODES_ET_SIGLES.md"),
    ("Index des exercices", "02_INDEX_DES_EXERCICES.md"),
]
lines = ["nav:"]
for t, p in nav:
    lines.append(f"  - {q(t)}: {q(p)}")
lines.append(f"  - {q('Modules')}:")
for m in sorted(glob.glob(os.path.join(DOCS, "modules", "M*"))):
    code = os.path.basename(m)[:3]
    cours = os.path.join(m, "cours.md")
    mt = title(cours) if os.path.exists(cours) else os.path.basename(m)
    lines.append(f"    - {q(code + ' — ' + mt)}:")
    if os.path.exists(cours):
        lines.append(f"      - {q('Cours')}: {q(rel(cours))}")
    extras = [f for f in sorted(glob.glob(os.path.join(m, "*.md"))) if os.path.basename(f) != "cours.md"]
    for f in extras:
        lines.append(f"      - {q(title(f, False))}: {q(rel(f))}")
    for sub, label in (("examens_blancs", "Examens blancs (QCM)"), ("exercices", "Exercices"), ("corriges", "Corrigés")):
        files = sorted(glob.glob(os.path.join(m, sub, "*.md")))
        if not files:
            continue
        lines.append(f"      - {q(label)}:")
        for f in files:
            if sub == "examens_blancs":
                lines.append(f"        - {q(title(f, False).split(' — ')[0])}: {q(rel(f))}")
                continue
            num = os.path.basename(f).split("_")[0]
            lines.append(f"        - {q(num + ' · ' + title(f))}: {q(rel(f))}")
lines.append(f"  - {q('Glossaire FR ↔ EN')}: {q('99_GLOSSAIRE_FR_EN.md')}")
lines.append(f"  - {q('Points à valider')}: {q('03_POINTS_A_VALIDER.md')}")

with open(os.path.join(ROOT, "outils", "mkdocs.base.yml"), encoding="utf-8") as f:
    base = f.read()
with open(os.path.join(ROOT, "mkdocs.yml"), "w", encoding="utf-8") as f:
    f.write(base.rstrip() + "\n\n" + "\n".join(lines) + "\n")
print("mkdocs.yml généré")
