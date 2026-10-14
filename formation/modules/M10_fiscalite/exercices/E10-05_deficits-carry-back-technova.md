# E10-05 — TechNova : imputation plafonnée des déficits et option pour le carry-back
**Client :** C08 — TechNova SAS | **Difficulté :** ★★★ | **Durée estimée :** 1 h | **Thèmes :** report en avant (1 M€ + 50 %), suivi 2058-B, carry-back, interaction avec le CIR, acomptes

**Corner case :** oui — le carry-back est sans effet lorsque l'IS de l'exercice d'imputation a été payé par du CIR.

## La mise en situation

Jeudi 4 février 2027, visio avec Yanis Haddad (président) et Émilie Roux (DAF à temps partagé).

> **Yanis :** « Enfin rentables ! 1,64 M€ de résultat fiscal grâce au contrat grand compte. Avec nos 2,3 M€ de déficits, on ne paie rien, non ? »
> **Émilie :** « Attention, il y a un plafond je crois. Autre question : on va recruter 8 ingénieurs en 2027, on prévoit une perte fiscale d'environ 180 000 €. Il paraît qu'on peut "récupérer" l'IS payé en 2026 avec le carry-back. Vous pouvez nous chiffrer ça ? »

Hélène Ferrand : « Faites le calcul complet. Le CIR 2026 est calculé dans le dossier (exercice E10-06 : 89 534 €) — tenez-en compte. »

## Les pièces

**Pièce 1 — Suivi des déficits reportables (2058-B de l'exercice 2025, extrait)**

| Exercice d'origine | Déficit d'origine | Imputé antérieurement | Restant au 01/01/2026 |
|---|---|---|---|
| 2020 | 410 000 € | 140 000 € (sur le bénéfice 2025) | 270 000 € |
| 2021 | 620 000 € | 0 € | 620 000 € |
| 2022 | 540 000 € | 0 € | 540 000 € |
| 2023 | 480 000 € | 0 € | 480 000 € |
| 2024 | 390 000 € | 0 € | 390 000 € |
| **Total** | **2 440 000 €** | **140 000 €** | **2 300 000 €** |

**Pièce 2 — Projet de 2058-A 2026 (préparé par Émilie)**

```
Résultat comptable 2026 (avant IS)                                   1 652 300
+ Réintégrations diverses                                               18 400
– Déductions diverses (dont CIR comptabilisé en produit : à neutraliser)  30 700
Résultat fiscal avant imputation des déficits                        1 640 000
– Déficits antérieurs imputés (Émilie : "tout")                    – 1 640 000
Résultat imposable                                                           0
```

**Pièce 3 — Informations**

```
- Capital : 54 000 € entièrement libéré ; détenu par Yanis Haddad (62 %), deux cofondateurs
  (18 %), des business angels personnes physiques (12 %) et un FCPI (8 %).
- CA HT 2026 : 3 920 000 €. PME au sens communautaire.
- Aucun dividende n'a jamais été distribué ; aucun n'est prévu.
- Aucun acompte d'IS versé en 2026 (exercice 2025 sans IS du fait des déficits).
- Aucun changement d'activité depuis la création.
- Plafonds retenus (valeurs à vérifier chaque année) :
  report en avant : 1 000 000 € + 50 % du bénéfice excédant 1 000 000 € ;
  carry-back : imputation sur le bénéfice de l'exercice précédent, dans la limite du plus faible
  de ce bénéfice et de 1 000 000 € ; créance = déficit reporté × taux normal de l'IS (25 %).
- Taux d'IS : 15 % jusqu'à 42 500 €, 25 % au-delà.
```

## Travail à faire

1. Corrigez le projet d'Émilie : déficit imputable en 2026, résultat imposable, IS brut 2026.
2. Mettez à jour le suivi des déficits (2058-B) au 31/12/2026, en imputant les déficits les plus anciens en premier.
3. Compte tenu du CIR 2026 (89 534 €), quel est l'IS à payer et que devient l'excédent de CIR ?
4. Si l'exercice 2027 dégage un déficit fiscal de 180 000 €, l'option pour le carry-back est-elle intéressante ? Chiffrez.
5. Variante : même question si TechNova n'avait **pas** eu de CIR en 2026. Chiffrez la créance et donnez son écriture et son traitement fiscal.
6. Établissez l'échéancier des acomptes d'IS 2027.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E10-05_corrige.md)
