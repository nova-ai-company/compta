"""Génère les bulles d'aide du site :
- formation/assets/lexique.js : dictionnaire {code: {c, t, d, u}} lu par bulles.js
- formation/04_CODES_ET_SIGLES.md : page « Comprendre les codes et sigles »

Sources : sigles.py (à la main) + portefeuille clients, modules et exercices (automatique).
"""
import glob, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "formation")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigles import SIGLES  # noqa: E402

CATS = {
    "client": "Client du portefeuille",
    "module": "Module de la formation",
    "exercice": "Exercice",
    "notation": "Notation (dates et périodes)",
    "declaration": "Déclaration / formulaire",
    "journal": "Journal comptable",
    "fiscal": "Fiscalité",
    "social": "Paie et social",
    "forme": "Forme juridique",
    "organisme": "Organisme / administration",
    "texte": "Texte de référence",
    "sigle": "Sigle courant",
}


def slugify(value):
    """Même algorithme que l'extension toc de Python-Markdown (ancres des titres)."""
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


def url_of(path):
    rel = os.path.relpath(path, DOCS).replace(os.sep, "/")
    return rel[:-3] + "/" if not rel.endswith("index.md") else rel[:-8]


def first_title(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return ""


lex = {}

# --- Clients -------------------------------------------------------------
portfolio = os.path.join(DOCS, "01_PORTEFEUILLE_CLIENTS.md")
text = open(portfolio, encoding="utf-8").read()
headings = {m.group(1): m.group(0)[4:].strip() for m in re.finditer(r"^### (C\d\d) — .+$", text, re.M)}
for line in text.splitlines():
    m = re.match(r"^\| (C\d\d) \| (.+)$", line)
    if not m:
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    code, nom, forme, activite, impot, tva, cloture, ca, effectif, missions = cells[:10]
    d = (f"{forme} — {activite}. Imposition : {impot}. TVA : {tva}. "
         f"Clôture : {cloture}. CA N-1 : {ca}. Effectif : {effectif}. Missions du cabinet : {missions}.")
    anchor = slugify(headings.get(code, code))
    lex[code] = {"c": "client", "t": f"{code} — {nom}", "d": d, "u": f"01_PORTEFEUILLE_CLIENTS/#{anchor}"}
clients = {k: v["t"].split(" — ", 1)[1] for k, v in lex.items()}

# --- Modules -------------------------------------------------------------
for mdir in sorted(glob.glob(os.path.join(DOCS, "modules", "M*"))):
    code = os.path.basename(mdir)[:3]
    cours = os.path.join(mdir, "cours.md")
    if not os.path.exists(cours):
        continue
    t = re.sub(r"^M\d\d\s*[—:-]\s*", "", first_title(cours))
    nb = len(glob.glob(os.path.join(mdir, "exercices", "*.md")))
    lex[code] = {"c": "module", "t": f"Module {code} — {t}",
                 "d": f"Un des 15 modules de la formation ({nb} exercices). Cliquez sur le lien pour ouvrir le cours.",
                 "u": url_of(cours)}

# --- Exercices -----------------------------------------------------------
for f in sorted(glob.glob(os.path.join(DOCS, "modules", "M*", "exercices", "E*.md"))):
    code = os.path.basename(f).split("_")[0]
    t = re.sub(r"^E\d\d-\d\d[a-z]?\s*[—:-]\s*", "", first_title(f))
    head = open(f, encoding="utf-8").read(1500)
    cl = re.search(r"\*\*Client :\*\*\s*([^|\n]+)", head)
    diff = re.search(r"\*\*Difficulté :\*\*\s*([★☆]+)", head)
    parts = [f"Exercice n° {code[4:]} du module {code[1:3]} (M{code[1:3]})."]
    if cl:
        parts.append(f"Client : {cl.group(1).strip()}.")
    if diff:
        parts.append(f"Difficulté : {diff.group(1)}.")
    lex[code] = {"c": "exercice", "t": f"{code} — {t}", "d": " ".join(parts), "u": url_of(f)}

# --- Sigles --------------------------------------------------------------
for k, (c, t, d) in SIGLES.items():
    lex[k] = {"c": c, "t": f"{k} — {t}", "d": d}
SOUS_TABLEAUX = {
    "2033-A": "bilan simplifié", "2033-B": "compte de résultat simplifié", "2033-C": "immobilisations et amortissements",
    "2033-D": "provisions et déficits", "2033-E": "valeur ajoutée (CVAE)", "2033-F": "composition du capital",
    "2033-G": "filiales et participations", "2059-A": "plus et moins-values", "2059-B": "affectation des plus-values à court terme",
    "2059-E": "valeur ajoutée (CVAE)", "2059-F": "composition du capital", "2059-G": "filiales et participations",
}
for k, t in SOUS_TABLEAUX.items():
    if k not in lex:
        lex[k] = {"c": "declaration", "t": f"{k} — Liasse fiscale : {t}",
                  "d": f"Tableau {k} de la liasse fiscale ({'régime simplifié' if k.startswith('2033') else 'régime normal'}) : {t}."}

with open(os.path.join(DOCS, "assets", "lexique.js"), "w", encoding="utf-8") as f:
    f.write("/* Généré par outils/gen_lexique.py — ne pas modifier à la main. */\n")
    f.write("window.LEXIQUE_CATS = " + json.dumps(CATS, ensure_ascii=False) + ";\n")
    f.write("window.LEXIQUE = " + json.dumps(lex, ensure_ascii=False, separators=(",", ":")) + ";\n")

# --- Page « Comprendre les codes et sigles » ------------------------------
out = ["# Comprendre les codes et sigles",
       "",
       "> 🟢 **En clair :** la comptabilité utilise beaucoup d'abréviations. **Vous n'avez pas à les deviner.**",
       "> Partout dans la formation, les codes et sigles sont **soulignés en pointillés** : "
       "**cliquez (ou touchez) un code** pour afficher son explication. Cette page les rassemble tous.",
       "",
       "## Comment lire les codes de la formation",
       "",
       "| Code | Ce que ça veut dire | Exemple |",
       "|---|---|---|",
       "| **C** + 2 chiffres | Un **client** du portefeuille du cabinet (C01 à C25) | C09 = Mode & Co, l'e-commerçant |",
       "| **M** + 2 chiffres | Un **module** (chapitre) de la formation (M00 à M14) | M04 = le module sur la TVA |",
       "| **E** + module **-** numéro | Un **exercice** : E04-03 = exercice n° 3 du module M04 | E04-03 = TVA sur la marge des véhicules d'occasion |",
       "| **N**, **N-1**, **N+1** | L'exercice comptable en cours, le précédent, le suivant | N = 2026, N-1 = 2025 |",
       "| **M**, **M+1** | Un mois donné, le mois suivant | TVA de janvier (M) déclarée en février (M+1) |",
       "| **T1** … **T4** | Les trimestres de l'année | T4 = octobre à décembre |",
       "| **★☆☆ / ★★☆ / ★★★** | Difficulté de l'exercice | ★☆☆ = débutant |",
       "| Nombre à 3–6 chiffres (401, 44566…) | Un **compte** du plan comptable (PCG) | 401 = fournisseurs, 512 = banque |",
       "| Nombre à 4 chiffres + lettre (2058-A, 2033-B) | Un **formulaire fiscal** | 2058-A = passage du résultat comptable au résultat fiscal |",
       "",
       "## Les 25 clients du portefeuille",
       "",
       "| Code | Client | Fiche |",
       "|---|---|---|",
       ]
for k in sorted(c for c in lex if lex[c]["c"] == "client"):
    v = lex[k]
    out.append(f"| **{k}** | {clients[k]} — {v['d'].split('. Imposition')[0]} | [Voir la fiche]({v['u'].replace('/#', '.md#')}) |")
out += ["", "## Les modules", "", "| Code | Module |", "|---|---|"]
for k in sorted(c for c in lex if lex[c]["c"] == "module"):
    mdir = glob.glob(os.path.join(DOCS, "modules", k + "_*"))[0]
    out.append(f"| **{k}** | [{lex[k]['t'].split(' — ', 1)[1]}]({os.path.relpath(os.path.join(mdir, 'cours.md'), DOCS)}) |")

order = ["notation", "declaration", "fiscal", "social", "journal", "forme", "organisme", "texte", "sigle"]
for cat in order:
    items = sorted((k for k, (c, _, _) in SIGLES.items() if c == cat), key=lambda s: s.lower())
    if not items:
        continue
    out += ["", f"## {CATS[cat]}", "", "| Sigle | Signification | Explication simple |", "|---|---|---|"]
    for k in items:
        _, t, d = SIGLES[k]
        out.append(f"| **{k}** | {t} | {d.replace('|', '/')} |")
out.append("")
with open(os.path.join(DOCS, "04_CODES_ET_SIGLES.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print(f"lexique.js : {len(lex)} entrées ; page 04_CODES_ET_SIGLES.md générée")
