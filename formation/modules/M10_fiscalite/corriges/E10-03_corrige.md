# Corrigé E10-03 — L'IS d'un premier exercice de 16 mois

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-03](../exercices/E10-03_IS-premier-exercice-studio-pixel.md)

## 1. Analyse

Trois sujets à traiter dans l'ordre :

1. **Le résultat fiscal** : les frais de constitution comptabilisés en charges sont déductibles (option du PCG, suivie fiscalement). L'amende DGAC est une sanction légale → non déductible. La formation payée par Léo **avant** l'immatriculation n'a pas été reprise par la société : ni dans l'état annexé aux statuts, ni par une décision ultérieure des associés. Elle reste juridiquement une dépense **personnelle** de Léo → non déductible chez Studio Pixel (et son remboursement via le compte courant est contestable : à régulariser).
2. **Le taux réduit** : trois conditions, dont la **libération intégrale du capital**. Le capital n'était pas libéré au début de l'exercice ; il l'est depuis le 15/06/2026. L'administration apprécie cette condition **à la clôture de l'exercice** (doctrine à vérifier dans le BOFiP de l'année) → condition remplie au 31/12/2026.
3. **Le plafond de 42 500 €** s'entend « par période de 12 mois » : pour 16 mois, il est **proratisé**.

## 2. Calculs

**Résultat fiscal**

| Ligne | Réintégrations | Déductions |
|---|---|---|
| Résultat comptable (bénéfice, 16 mois) | 76 240,00 | |
| Amende DGAC (art. 39-2 CGI) | 750,00 | |
| Formation antérieure non reprise par la société | 1 410,00 | |
| Frais de constitution | — (déductibles) | |
| **Résultat fiscal** | **78 400,00** | |

**Conditions du taux réduit**

| Condition | Vérification | Résultat |
|---|---|---|
| CA HT < 10 M€ ramené à 12 mois | 210 000 × 12/16 = 157 500 € | ✔ |
| Capital entièrement libéré | Solde de 2 000 € versé le 15/06/2026 ; 4562 soldé au 31/12/2026 | ✔ (appréciation à la clôture — à vérifier) |
| ≥ 75 % détenu par des personnes physiques | Léo 50 % + Sarah 50 % = 100 % | ✔ |

**IS dû**

- Plafond proratisé : 42 500 × 16/12 = **56 666,67 €**
- IS à 15 % : 56 666,67 × 15 % = **8 500,00 €**
- IS à 25 % : (78 400,00 – 56 666,67) × 25 % = 21 733,33 × 25 % = **5 433,33 €**
- **IS total : 13 933,33 € → 13 933 €**

**Erreur de Sarah** : elle applique le plafond annuel non proratisé (6 375 + 25 % × 35 900 = 15 350 €) et paierait **1 417 €** de trop. Elle a aussi oublié les réintégrations (son calcul porte sur 76 240 €).

**Acomptes 2025 et 2026** : **aucun**. Les sociétés nouvelles ne versent pas d'acomptes au titre de leur premier exercice (il n'existe pas d'exercice de référence). **Pas de pénalité.**

**Solde** : IS 13 933 € payé avec le relevé de solde **2572** au plus tard le **15/05/2027** (15 du 4e mois suivant la clôture).

**Acomptes 2027 (prévisionnel)**

- Bénéfice de référence ramené à 12 mois : 78 400 × 12/16 = **58 800 €**
- IS de référence : 42 500 × 15 % + (58 800 – 42 500) × 25 % = 6 375 + 4 075 = **10 450 €** > 3 000 € → acomptes dus
- ¼ = **2 612,50 €**

| Échéance | Montant | Explication |
|---|---|---|
| 15/03/2027 | 0 € | Liasse du premier exercice non encore déposée et pas d'exercice antérieur (traitement à confirmer dans le BOFiP) |
| 15/06/2027 | **5 225,00 €** | Régularisation : 2 × 2 612,50 – 0 |
| 15/09/2027 | **2 612,50 €** | |
| 15/12/2027 | **2 612,50 €** | |
| **Total** | **10 450,00 €** | |

Sorties de trésorerie d'IS en 2027 : 13 933 + 10 450 = **24 383 €** — à anticiper dès maintenant.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 695000 | Impôt sur les bénéfices | IS premier exercice (16 mois) | 13 933,00 | |
| 31/12/2026 | OD | 444000 | État — impôt sur les bénéfices | IS premier exercice (16 mois) | | 13 933,00 |
| | | | | **Totaux** | **13 933,00** | **13 933,00** |

Résultat comptable après IS : 76 240 – 13 933 = **62 307,00 €**.

Régularisation recommandée de la formation (si les associés ne la reprennent pas) : refacturer la somme à Léo, c'est-à-dire **débiter son compte courant** (455) de 1 410 € par le crédit du compte de charge, ce qui supprime la réintégration. Si cette écriture est passée avant l'arrêté des comptes, le résultat fiscal devient 76 990 € (à recalculer).

## 4. Points d'attention / pièges

- **Prorata du plafond** : il joue dans les deux sens (exercice court → plafond réduit).
- **CA ramené à 12 mois** pour le seuil de 10 M€.
- **Capital non libéré** : si le solde n'avait pas été versé avant la clôture, la société aurait perdu le taux réduit (IS = 78 400 × 25 % = 19 600 €, soit + 5 667 €). Le senior vérifie le 4562 / 109 au bilan **avant** de calculer l'IS.
- **Frais pré-constitution** : seuls les actes repris (état annexé aux statuts, mandat, ou décision des associés après l'immatriculation) deviennent des charges de la société.
- **Pas d'exonération « entreprise nouvelle »** : le dispositif de l'art. 44 sexies est réservé à certaines zones (ZFRR…), non applicable rue Mercière.
- **Acomptes 2027** calculés sur le bénéfice **ramené à 12 mois**, pas sur l'IS de 16 mois / 4.

## 5. Ce qu'un senior ferait en plus

- **Mail type à Sarah** :

> « Bonjour Sarah, l'IS du premier exercice s'élève à 13 933 € (et non 15 350 €) : comme votre exercice dure 16 mois, la tranche à 15 % est portée à 56 667 €. Aucune pénalité : une société nouvelle ne verse pas d'acomptes pendant son premier exercice. À prévoir en 2027 : le solde de 13 933 € le 15 mai, puis environ 5 225 € le 15 juin et 2 612,50 € les 15 septembre et 15 décembre. La formation de Léo (juillet 2025) n'ayant pas été reprise par la société, elle n'est pas déductible : nous vous proposons de la refacturer à Léo ou de la faire approuver par décision des associés avant l'arrêté des comptes. Bien à vous. »

- Proposer une **décision des associés** de reprise des actes antérieurs (si la dépense est réellement dans l'intérêt de la société) avant l'approbation des comptes.
- Mettre en place un **budget d'IS mensualisé** (provision bancaire) pour une jeune société.
- Documenter : copie de l'appel de fonds, relevé bancaire du 15/06/2026, statuts et état des actes.

## 6. Références

- CGI art. 219 I b (taux réduit, plafond de 42 500 € par période de 12 mois, conditions), art. 39-2 (amendes), art. 1668 (acomptes ; dispense pour le premier exercice des sociétés nouvelles), art. 44 sexies (entreprises nouvelles en zones).
- Code de commerce : art. L. 210-6 (reprise des actes accomplis pour le compte de la société en formation), L. 227-1 et L. 225-3 (libération du capital des SAS).
- BOFiP : série IS-LIQ (taux réduit des PME, appréciation des conditions).
