"""Ajoute en haut de chaque page un encadré « Les mots et codes de cette page ».

L'encadré liste, avec leur explication simple, tous les sigles, codes analytiques,
comptes et mots du métier présents dans la page (dictionnaire : assets/lexique.js,
généré par gen_lexique.py — lancer gen_lexique.py AVANT ce script).
Lisible sur le site (encadré repliable) ET dans l'éditeur (Markdown brut).
Relançable sans risque : l'encadré existant est remplacé.

Usage : python3 outils/glossaire_pages.py [M16 M17 ...]   (par défaut : M16 M17)
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "formation")
DEB, FIN = "<!-- glossaire-page -->", "<!-- /glossaire-page -->"
EXCLUS_CAT = {"client", "module", "exercice"}
EXCLUS_CLE = {"N", "M", "T1", "T2", "T3", "T4"}
ORDRE = {"compte": 2, "terme": 3}

src = open(os.path.join(DOCS, "assets", "lexique.js"), encoding="utf-8").read()
LEX = json.loads(re.search(r"window\.LEXIQUE = (\{.*\});", src).group(1))
keys = sorted((k for k, v in LEX.items() if v["c"] not in EXCLUS_CAT and k not in EXCLUS_CLE), key=len, reverse=True)
RE = re.compile(r"(^|[^A-Za-z0-9À-ÿ_\-/.°+'’])(" + "|".join(map(re.escape, keys)) + r")(?=$|[^A-Za-z0-9À-ÿ_\-/+°])", re.M)
YEAR_CTX = re.compile(r"(?:^|\s)(en|au|de|du|à|depuis|avant|après|fin|début|exercice|année|→|–|-)\s*$", re.I)
SP = "[\\s  ]"


def faux_positif(code, text, start):
    """Mêmes garde-fous que bulles.js : années et montants ne sont pas des comptes."""
    if re.fullmatch(r"\d{4}", code) and YEAR_CTX.search(text[max(0, start - 14):start]):
        return True
    if re.fullmatch(r"\d{3,6}x?", code):
        bef, aft = text[max(0, start - 2):start], text[start + len(code):start + len(code) + 12]
        if re.search(r"\d" + SP + "$", bef) or re.match(r"(,\d|\.\d|" + SP + "?[€%])", aft):
            return True
        if len(code) == 3 and (re.match(SP + r"\d{3}([,\s  ]|$)", aft)
                               or re.match(SP + r"?(km|h\b|m²|m2|an|jour|place|heure|personne|salarié|mois|enfant|adulte|habitant|dossier|facture|ligne|question|%)", aft, re.I)
                               or re.search(r"[×x*+=−\-/:]" + SP + "?$", bef)):
            return True
    return False


def entrees(text):
    trouves, vus = {}, set()
    for m in RE.finditer(text):
        code = m.group(2)
        if faux_positif(code, text, m.start(2)):
            continue
        e = LEX[code]
        sig = (e["t"].split(" — ", 1)[-1], e["d"])
        if sig in vus:  # variantes d'un même mot (pluriel, majuscule)
            continue
        vus.add(sig)
        trouves[code] = e
    def tri(item):
        k, e = item
        o = ORDRE.get(e["c"], 1)
        return (o, int(re.sub(r"\D", "", k) or 0) if o == 2 else 0, k.lower())
    return sorted(trouves.items(), key=tri)


def encadre(items):
    out = [DEB,
           '??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"',
           "    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.",
           "",
           "    | Mot / code | Ce que ça veut dire |",
           "    |---|---|"]
    for k, e in items:
        titre = e["t"].split(" — ", 1)[-1]
        d = e["d"]
        txt = titre if d.lower().startswith(titre.lower()) else f"{titre}. {d}" if not titre.endswith(".") else f"{titre} {d}"
        if e["c"] == "compte":
            k = f"Compte {k}"
        out.append(f"    | **{k}** | {txt.replace('|', '/')} |")
    out.append(FIN)
    return "\n".join(out)


def traiter(path):
    txt = open(path, encoding="utf-8").read()
    txt = re.sub(r"\n?" + re.escape(DEB) + r".*?" + re.escape(FIN) + r"\n?", "\n", txt, flags=re.S)
    items = entrees(txt)
    lines = txt.split("\n")
    # Position : après le titre H1 et les lignes d'en-tête qui le suivent immédiatement.
    i = next((n for n, l in enumerate(lines) if l.startswith("# ")), -1) + 1
    while i < len(lines) and lines[i].strip():
        i += 1
    # Les exercices ont une ligne « **Corner case :** » juste après l'en-tête : l'encadré va dessous.
    j = i
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j < len(lines) and lines[j].startswith("**Corner case"):
        i = j
        while i < len(lines) and lines[i].strip():
            i += 1
    if items:
        lines[i:i] = ["", encadre(items)]
    new = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    if new != open(path, encoding="utf-8").read():
        open(path, "w", encoding="utf-8").write(new)
    return len(items)


mods = sys.argv[1:] or ["M16", "M17"]
n = 0
for mod in mods:
    for f in sorted(glob.glob(os.path.join(DOCS, "modules", mod + "_*", "**", "*.md"), recursive=True)):
        if os.path.basename(f).startswith("_"):
            continue
        k = traiter(f)
        n += 1
print(f"Encadrés « mots et codes » mis à jour sur {n} pages ({', '.join(mods)})")
