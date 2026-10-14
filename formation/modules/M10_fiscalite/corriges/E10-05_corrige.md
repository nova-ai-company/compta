# Corrigé E10-05 — TechNova : imputation plafonnée des déficits et option pour le carry-back

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-05](../exercices/E10-05_deficits-carry-back-technova.md)

## 1. Analyse

- **Report en avant** : imputation plafonnée à 1 000 000 € + 50 % de l'excédent de bénéfice au-delà de 1 000 000 €. Émilie a imputé « tout » : erreur classique, le résultat imposable n'est pas nul.
- Les déficits restent reportables **sans limite de durée** ; le changement d'actionnariat (business angels, FCPI) n'a pas d'effet, en l'absence de changement d'activité.
- **Carry-back** : le déficit 2027 ne peut remonter que sur le bénéfice 2026, **diminué de la fraction ayant donné lieu à un IS payé au moyen de crédits d'impôt**. Or l'IS 2026 est entièrement payé par le CIR → aucun bénéfice d'imputation → **carry-back sans effet**. C'est logique : on ne peut pas « rembourser » un impôt qui n'a pas été payé en argent.

## 2. Calculs

**1) Imputation 2026**

- Bénéfice avant imputation : 1 640 000 €
- Plafond d'imputation : 1 000 000 + 50 % × (1 640 000 – 1 000 000) = 1 000 000 + 320 000 = **1 320 000 €**
- Déficits disponibles : 2 300 000 € → imputation retenue : **1 320 000 €**
- **Résultat imposable 2026 : 320 000 €**
- Taux réduit : CA < 10 M€, capital libéré, personnes physiques 92 % (≥ 75 %) → applicable.
- IS brut : 42 500 × 15 % + (320 000 – 42 500) × 25 % = 6 375 + 69 375 = **75 750 €**

**2) Suivi 2058-B au 31/12/2026**

| Origine | Restant au 01/01/2026 | Imputé en 2026 | Restant au 31/12/2026 |
|---|---|---|---|
| 2020 | 270 000 | 270 000 | 0 |
| 2021 | 620 000 | 620 000 | 0 |
| 2022 | 540 000 | 430 000 | 110 000 |
| 2023 | 480 000 | 0 | 480 000 |
| 2024 | 390 000 | 0 | 390 000 |
| **Total** | **2 300 000** | **1 320 000** | **980 000** |

**3) IS 2026 et CIR**

- IS brut 75 750 € – CIR 89 534 € → **IS à payer : 0 €**
- Excédent de CIR : 89 534 – 75 750 = **13 784 €** → **remboursement immédiat** (PME au sens communautaire), demandé avec le relevé de solde 2572 et la 2069-A.

**4) Carry-back du déficit 2027 (180 000 €)**

| Élément | Montant |
|---|---|
| Bénéfice imposable 2026 | 320 000 € |
| – Fraction distribuée | 0 € |
| – Fraction ayant donné lieu à un IS payé par crédits d'impôt (IS 75 750 € entièrement payé par le CIR) | – 320 000 € |
| **Bénéfice d'imputation** | **0 €** |
| Carry-back possible | **0 €** |

→ L'option est **sans intérêt**. Le déficit 2027 de 180 000 € viendra s'ajouter au stock reportable en avant : 980 000 + 180 000 = **1 160 000 €**.

**5) Variante sans CIR**

| Élément | Montant |
|---|---|
| Bénéfice d'imputation 2026 | 320 000 € |
| Plafond légal retenu | 1 000 000 € |
| Limite = min (320 000 ; 1 000 000) | 320 000 € |
| Déficit 2027 reporté en arrière = min (180 000 ; 320 000) | **180 000 €** |
| **Créance de carry-back** = 180 000 × 25 % | **45 000 €** |

> Le plafond légal n'est pas limitant ici (180 000 € est inférieur à la fois à 200 000 € et à 1 000 000 €), ce qui rend le résultat insensible à la version du texte en vigueur — mais vérifiez toujours le plafond de l'année.

- La créance (constatée à la clôture 2027) est **non imposable**, imputable sur l'IS des 5 exercices suivants (2028 → 2032), remboursable à l'issue ; mobilisable auprès d'un établissement de crédit.
- L'option se fait avec la liasse 2027 (imprimé 2039).
- Remarque : la créance (45 000 €) est inférieure à l'IS effectivement payé en 2026 dans cette hypothèse (75 750 €), mais la **règle de calcul** est fixée par le texte (déficit × taux normal).

**6) Acomptes 2027**

- 15/03/2027 : base exercice 2025 (IS nul) → **0 €**
- IS de référence 2026 (**avant** imputation du CIR) : 75 750 € ; ¼ = 18 937,50 €
- 15/06/2027 : 2 × 18 937,50 – 0 = **37 875,00 €**
- 15/09/2027 : **18 937,50 €** ; 15/12/2027 : **18 937,50 €**
- Total : **75 750 €**, alors que l'IS 2026 a été entièrement couvert par le CIR ! TechNova peut **moduler** ses acomptes si elle estime, sous sa responsabilité, que les versements dépasseraient l'impôt finalement dû en 2027 (en tenant compte de sa perte prévue) ; une erreur de plus de 10 % est sanctionnée (majoration et intérêt de retard — *conditions à vérifier*). Avec un déficit 2027 prévu, la modulation à **zéro** est justifiée et documentée.

## 3. Écritures comptables

**Au 31/12/2026 (IS de l'exercice — le CIR est traité dans E10-06)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 695000 | Impôt sur les bénéfices | IS 2026 (après imputation plafonnée des déficits) | 75 750,00 | |
| 31/12/2026 | OD | 444000 | État — impôt sur les bénéfices | IS 2026 (après imputation plafonnée des déficits) | | 75 750,00 |
| | | | | **Totaux** | **75 750,00** | **75 750,00** |

**Variante sans CIR — au 31/12/2027 (option carry-back)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2027 | OD | 444100 | État — créance de carry-back | Report en arrière du déficit 2027 (180 000 × 25 %) | 45 000,00 | |
| 31/12/2027 | OD | 699000 | Produits — Reports en arrière des déficits | Report en arrière du déficit 2027 | | 45 000,00 |
| | | | | **Totaux** | **45 000,00** | **45 000,00** |

Sur le 2058-A 2027 : **déduction** de 45 000 € (produit non imposable). Le déficit 2027 reportable en avant est diminué des 180 000 € reportés en arrière.

## 4. Points d'attention / pièges

- **« On ne paie rien, on a des déficits »** : faux dès que le bénéfice dépasse 1 M€.
- L'ordre : déficits imputés **avant** l'application du taux réduit.
- **Carry-back + CIR** : le bénéfice ayant supporté un IS payé par crédits d'impôt est exclu. Une start-up avec un gros CIR n'a souvent **rien** à remonter.
- **Acomptes** : calculés sur l'IS **avant** crédits d'impôt → décalage de trésorerie important si on ne module pas.
- Ne pas oublier la **2069-A** et le dossier justificatif du CIR, sans quoi le remboursement de 13 784 € sera bloqué.
- Le plafond légal du carry-back doit être vérifié chaque année (il a déjà été modifié par le passé).

## 5. Ce qu'un senior ferait en plus

- **Mail type à Yanis et Émilie** :

> « Bonjour, 1) sur 2026 vous ne pouvez imputer que 1 320 000 € de déficits (plafond de 1 M€ + 50 % de l'excédent) : le résultat imposable est de 320 000 €, soit un IS de 75 750 €. Bonne nouvelle : votre CIR (89 534 €) le couvre entièrement, et le surplus de 13 784 € vous sera remboursé. Il vous restera 980 000 € de déficits pour l'avenir. 2) Le carry-back ne vous rapportera rien sur la perte 2027 : l'IS 2026 ayant été payé par le CIR, il n'y a pas d'impôt à "récupérer". La perte 2027 s'ajoutera simplement à vos déficits reportables. 3) Les acomptes 2027 seraient de 75 750 € au total : compte tenu de la perte prévue, nous vous proposons de les moduler à zéro en documentant le prévisionnel. »

- Mettre à jour le **tableau de suivi pluriannuel** des déficits (par année d'origine) dans le dossier permanent.
- Archiver le prévisionnel 2027 justifiant la modulation des acomptes.

## 6. Références

- CGI : art. 209 I (report en avant, plafond 1 M€ + 50 %), art. 220 quinquies (carry-back : limite, exclusion du bénéfice payé par crédits d'impôt, créance), art. 221-5 (changement d'activité), art. 219 (taux), art. 1668 (acomptes et modulation), art. 1731 A (insuffisance d'acomptes), art. 244 quater B et 199 ter B (CIR, remboursement immédiat).
- PCG : compte 699 « Produits — Reports en arrière des déficits ».
- BOFiP : série IS-DEF (déficits).
