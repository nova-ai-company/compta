"""Génère les examens blancs complets (sujet + corrigé) à partir de la banque de QCM du module M14."""
import os, re

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "formation", "modules", "M14_preparation_entretien_GSF")
qtxt = open(os.path.join(D, "QCM_questions.md"), encoding="utf-8").read()
rtxt = open(os.path.join(D, "QCM_reponses.md"), encoding="utf-8").read()

# Questions : bloc "### Qnnn ★" jusqu'au titre suivant
questions = {}
for m in re.finditer(r"^### (Q\d{3}) (★+)\s*\n(.*?)(?=^#{2,3} )", qtxt, re.S | re.M):
    questions[m.group(1)] = (m.group(2), re.sub(r"(\n\s*-{3,}\s*)+$", "", m.group(3).strip()))

# Explications : "**Qnnn — Réponse X** (...)" + paragraphe
expl = {}
for m in re.finditer(r"^\*\*(Q\d{3}) — Réponse ([A-D])\*\*(.*?)(?=^\*\*Q\d{3} — |^## |\Z)", rtxt, re.S | re.M):
    expl[m.group(1)] = (m.group(2), m.group(3).strip())

# Composition des examens (tableaux de la fin de QCM_questions.md)
exams = []
for m in re.finditer(r"### Examen blanc n° (\d) — 20 minutes\s*\n\n\|.*?\n\|.*?\n((?:\|.*\n)+)", qtxt):
    rows = re.findall(r"\|\s*\d+\s*\|\s*(Q\d{3})\s*\|\s*(\w)\s*\|", m.group(2))
    exams.append((m.group(1), [r[0] for r in rows]))

THEMES = {"A": "Fondamentaux et PCG", "B": "Fournisseurs / achats", "C": "Clients / ventes", "D": "TVA",
          "E": "Trésorerie", "F": "Paie et social", "G": "Immobilisations et clôture",
          "H": "Fiscalité et liasse", "I": "Excel et outils", "J": "Culture GSF"}

for num, qids in exams:
    assert len(qids) == 15, (num, qids)
    answers = [expl[q][0] for q in qids]
    s = [f"# Examen blanc n° {num} — QCM d'entretien GSF (15 questions, 20 minutes)", "",
         "**Conditions réelles :** 20 minutes, sans document, calculatrice simple tolérée, **une seule bonne réponse** par question.",
         "1 point par bonne réponse → note sur 15. Gérez votre temps : environ 80 secondes par question, gardez les calculs pour la fin.", "",
         f"👉 **Sur le site : touchez (ou cliquez) la réponse de votre choix** — elle s’entoure en bleu ; vous pouvez changer d’avis. Quand les 15 questions sont faites, descendez en bas de page et appuyez sur **« Corriger mon examen »**. Sur papier : notez vos réponses dans la grille en bas de page, puis ouvrez le [corrigé](Examen_blanc_{num}_corrige.md).", "",
         "---", ""]
    for i, q in enumerate(qids, 1):
        stars, body = questions[q]
        s += [f"### Question {i} {stars}", "", body, ""]
    s += ["---", "", "## Ma grille de réponses", "",
          "| " + " | ".join(str(i) for i in range(1, 16)) + " |",
          "|" + "---|" * 15,
          "| " + " | ".join(" " for _ in range(15)) + " |", "",
          f'<div class="qcm-exam" data-answers="{",".join(answers)}" data-corrige="../Examen_blanc_{num}_corrige/"></div>', ""]
    open(os.path.join(D, "examens_blancs", f"Examen_blanc_{num}.md"), "w", encoding="utf-8").write("\n".join(s))

    c = [f"# Corrigé de l'examen blanc n° {num}", "",
         f"Sujet : [Examen blanc n° {num}](Examen_blanc_{num}.md)", "",
         "## Grille des réponses", "",
         "| Question | " + " | ".join(str(i) for i in range(1, 16)) + " |",
         "|---|" + "---|" * 15,
         "| Réponse | " + " | ".join(f"**{a}**" for a in answers) + " |", "",
         "## Explications", ""]
    for i, q in enumerate(qids, 1):
        stars, body = questions[q]
        a, e = expl[q]
        theme = THEMES[re.search(r"\|\s*" + q + r"\s*\|\s*(\w)", qtxt).group(1)]
        c += [f"### Question {i} — réponse **{a}** · {theme} {stars}", "",
              "??? note \"Rappel de la question\"", ""] + ["    " + l for l in body.splitlines()] + ["", f"**Réponse {a}** {e}", ""]
    c += ["## Interpréter votre score", "",
          "| Score | Lecture |", "|---|---|",
          "| 14-15 | Excellent : vous êtes prête pour le QCM réel. |",
          "| 11-13 | Bon niveau : relisez les explications des questions manquées. |",
          "| 8-10 | Correct mais fragile : retravaillez les thèmes concernés dans le cours et le recueil d'écritures. |",
          "| 0-7 | Insuffisant : reprenez le cours M14 et la banque de QCM par thème avant de repasser un examen. |", ""]
    open(os.path.join(D, "examens_blancs", f"Examen_blanc_{num}_corrige.md"), "w", encoding="utf-8").write("\n".join(c))
    print("Examen", num, "OK —", "".join(answers))
