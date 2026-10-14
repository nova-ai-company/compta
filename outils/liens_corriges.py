"""Ajoute (ou met à jour) les liens énoncé ↔ corrigé dans tous les modules. Relançable sans risque."""
import glob, os, re

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "formation", "modules")
TAG_EX = "<!-- lien-corrige -->"
TAG_CO = "<!-- lien-enonce -->"
n_ex = n_co = 0

for ex in sorted(glob.glob(os.path.join(ROOT, "M*", "exercices", "*.md"))):
    mod = os.path.dirname(os.path.dirname(ex))
    num = os.path.basename(ex).split("_")[0]
    cors = sorted(glob.glob(os.path.join(mod, "corriges", num + "*_corrige.md")) +
                  glob.glob(os.path.join(mod, "corriges", num + "[a-z]_corrige.md")))
    cors = sorted(set(cors))
    if not cors:
        continue
    links = []
    for c in cors:
        suffix = os.path.basename(c)[len(num):].replace("_corrige.md", "")
        label = "Voir le corrigé" + (f" (partie {suffix})" if suffix else "")
        links.append(f"[{label} →](../corriges/{os.path.basename(c)})")
    block = f"\n\n---\n\n{TAG_EX}\n> ✅ **Exercice terminé ?** " + " · ".join(links) + "\n"
    txt = open(ex, encoding="utf-8").read()
    txt = re.sub(r"\n*---\n\n" + re.escape(TAG_EX) + r"\n.*\n?$", "", txt, flags=re.S).rstrip()
    open(ex, "w", encoding="utf-8").write(txt + block)
    n_ex += 1
    for c in cors:
        t = open(c, encoding="utf-8").read()
        t = re.sub(re.escape(TAG_CO) + r"\n.*?\n\n", "", t, flags=re.S)
        lines = t.split("\n", 1)
        back = f"{TAG_CO}\n> ↩️ [Revenir à l'énoncé de l'exercice {num}](../exercices/{os.path.basename(ex)})\n\n"
        t = lines[0] + "\n\n" + back + (lines[1].lstrip("\n") if len(lines) > 1 else "")
        open(c, "w", encoding="utf-8").write(t)
        n_co += 1

print(f"{n_ex} énoncés et {n_co} corrigés reliés")
