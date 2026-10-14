# Corrigé E15-05 — Note de frais d'un chef d'équipe et petite caisse de l'établissement

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-05](../exercices/E15-05_notes-de-frais-petite-caisse.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Ce qu'est une note de frais

Le salarié a **avancé de l'argent pour l'entreprise**. La société lui doit donc ce montant : c'est une **dette envers le salarié** (421 au crédit), et en face, des **charges** de la société (classe 6) et de la TVA récupérable (44566) au débit. Si une **avance** a été versée avant, le salarié doit cette avance à la société (425 au débit au moment du versement) : on la **déduit** du remboursement.

### Question 1 — Ligne par ligne

| N° | Remboursée ? | Compte | TVA récupérable | Pourquoi |
|---|---|---|---|---|
| 1 | Oui | 6257 Réceptions | 7,90 | Repas d'affaires avec un client identifié (nom et société notés) : c'est une réception |
| 2 | Oui | 6256 Missions | 1,68 | Repas du salarié en déplacement professionnel |
| 3 | Oui | 6251 Voyages et déplacements | 0,00 | Péage avec le véhicule personnel : règle interne → TTC en charge |
| 4 | Oui | 6251 Voyages et déplacements | — | Indemnités kilométriques : pas de facture, donc **pas de TVA** |
| 5 | Oui | 6234 Cadeaux | 7,50 | 45,00 € TTC ≤ 73 € TTC et premier cadeau de l'année à ce bénéficiaire |
| 6 | **Non** | — | — | Pas de justificatif → pas de remboursement (règle interne) |

**Pourquoi refuser 12,00 € ?** Sans justificatif, la société ne peut pas prouver que la dépense est professionnelle : la charge ne serait pas déductible fiscalement, et un remboursement sans justificatif pourrait être requalifié en **rémunération** soumise à cotisations. Pour 12,00 €, la règle est la même que pour 1 200,00 €.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 2 — Indemnités kilométriques

420 km × 0,636 €/km = **267,12 €** (barème 5 CV, tranche jusqu'à 5 000 km — *valeur à vérifier chaque année*).

### HT des lignes avec TVA

| N° | TTC | TVA | HT (TTC − TVA) |
|---|---|---|---|
| 1 | 86,90 | 7,90 | 79,00 (contrôle : 79,00 × 10 % = 7,90 ✓) |
| 2 | 18,50 | 1,68 | 16,82 (contrôle : 18,50 / 1,10 = 16,82 ✓) |
| 5 | 45,00 | 7,50 | 37,50 (contrôle : 37,50 × 20 % = 7,50 ✓) |

### Question 3 — Montant à verser

| Élément | Montant |
|---|---|
| Ligne 1 | 86,90 |
| Ligne 2 | 18,50 |
| Ligne 3 | 23,40 |
| Ligne 4 | 267,12 |
| Ligne 5 | 45,00 |
| **Total accepté** | **440,92** |
| − Avance du 01/09 | − 150,00 |
| **Reste à verser à Karim Benali** | **290,92** |

(Ligne 6 refusée : 12,00 €. La note déposée totalisait donc 452,92 € ; on en accepte 440,92 €.)

### Question 5 — Petite caisse

- Caisse théorique au 30/09 : 300,00 − 25,60 − 34,80 = **239,60 €**.
- Caisse comptée : 229,60 €.
- **Écart : 10,00 € manquants** (perte de caisse).
- Réapprovisionnement pour revenir à 300,00 € : 300,00 − 229,60 = **70,40 €** (= 25,60 + 34,80 + 10,00).
- Produits d'entretien : 34,80 − 5,80 = 29,00 € HT (contrôle : 29,00 × 20 % = 5,80 ✓).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/09/2026 | BQ | 425 | Personnel – avances et acomptes | Avance sur frais K. Benali – septembre | 150,00 | |
| 01/09/2026 | BQ | 512 | Banque | Avance sur frais K. Benali – septembre | | 150,00 |
| 30/09/2026 | OD | 6257 | Réceptions | NDF Benali 09/2026 – déjeuner client Clinique des Oliviers | 79,00 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur autres biens et services | NDF Benali – TVA 10 % déjeuner client | 7,90 | |
| 30/09/2026 | OD | 6256 | Missions | NDF Benali – repas déplacement Toulon | 16,82 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur autres biens et services | NDF Benali – TVA 10 % repas Toulon | 1,68 | |
| 30/09/2026 | OD | 6251 | Voyages et déplacements | NDF Benali – indemnités kilométriques 420 km × 0,636 | 267,12 | |
| 30/09/2026 | OD | 6251 | Voyages et déplacements | NDF Benali – péages A8 (TTC) | 23,40 | |
| 30/09/2026 | OD | 6234 | Cadeaux | NDF Benali – coffret de vin client Clinique des Oliviers | 37,50 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur autres biens et services | NDF Benali – TVA 20 % cadeau ≤ 73 € TTC | 7,50 | |
| 30/09/2026 | OD | 425 | Personnel – avances et acomptes | NDF Benali – imputation avance du 01/09 | | 150,00 |
| 30/09/2026 | OD | 421 | Personnel – rémunérations dues (notes de frais) | NDF Benali 09/2026 – net à rembourser | | 290,92 |
| 05/10/2026 | BQ | 421 | Personnel – rémunérations dues (notes de frais) | Remboursement NDF Benali 09/2026 | 290,92 | |
| 05/10/2026 | BQ | 512 | Banque | Remboursement NDF Benali 09/2026 | | 290,92 |
| 08/09/2026 | CA | 626 | Frais postaux et de télécommunications | Caisse Nice – timbres recommandés | 25,60 | |
| 08/09/2026 | CA | 530 | Caisse | Caisse Nice – timbres recommandés | | 25,60 |
| 15/09/2026 | CA | 6063 | Fournitures d'entretien et de petit équipement | Caisse Nice – produits d'entretien | 29,00 | |
| 15/09/2026 | CA | 44566 | TVA déductible sur autres biens et services | Caisse Nice – TVA 20 % produits d'entretien | 5,80 | |
| 15/09/2026 | CA | 530 | Caisse | Caisse Nice – produits d'entretien | | 34,80 |
| 30/09/2026 | CA | 658 | Charges diverses de gestion courante | Caisse Nice – écart de caisse (manquant) | 10,00 | |
| 30/09/2026 | CA | 530 | Caisse | Caisse Nice – écart de caisse (manquant) | | 10,00 |
| 30/09/2026 | BQ | 530 | Caisse | Réapprovisionnement caisse Nice | 70,40 | |
| 30/09/2026 | BQ | 512 | Banque | Retrait pour réapprovisionnement caisse Nice | | 70,40 |
| | | | | **Totaux** | **1 022,64** | **1 022,64** |

*Compte 658 : subdivision selon la nomenclature 2025 du PCG.*

**Pourquoi ces sens ?**
- **Avance** : la société prête de l'argent au salarié → créance sur le salarié (425 au **débit**), l'argent sort de la banque (512 au **crédit**).
- **Note de frais** : charges et TVA au **débit** ; la société doit le total au salarié, mais une partie est déjà payée par l'avance → on **solde le 425** (crédit 150,00) et le reste est une dette (421 au **crédit** 290,92).
- **Caisse** : chaque dépense fait **sortir** de l'argent de la caisse → 530 au **crédit**. Le réapprovisionnement fait **entrer** de l'argent dans la caisse (530 au débit) et sortir de la banque (512 au crédit).

Contrôle : après ces écritures, le 530 vaut 300,00 − 25,60 − 34,80 − 10,00 + 70,40 = **300,00 €** = fonds fixe ✓ ; le 425 et le 421 de Karim Benali sont soldés.

## 4. Points d'attention / pièges

- **Oublier l'avance** : on rembourserait 440,92 € au lieu de 290,92 €, et le 425 resterait débiteur indéfiniment.
- **TVA sur les indemnités kilométriques** : il n'y en a pas (pas de facture, c'est un barème).
- **Repas d'affaires (6257) ≠ repas du salarié en mission (6256)** : la distinction sert au contrôle des frais de réception.
- **Cadeau** : vérifier le seuil **par bénéficiaire et par an** (si M. Roux reçoit un deuxième cadeau dans l'année, le cumul compte).
- **Écart de caisse** : on ne « bricole » pas un ticket pour faire tomber la caisse juste ; on constate l'écart, on le signale, et un écart répété doit être expliqué par la responsable d'agence.
- **Caisse créditrice** : un compte 530 ne peut jamais être créditeur (on ne peut pas avoir moins de 0 € en caisse) : si c'est le cas, une recette a été oubliée ou une dépense saisie deux fois.

## 5. Ce que le recruteur attend / ce qu'un senior ferait en plus

**Question 6 — Points de contrôle d'une note de frais :**
1. **Signature** du salarié et **validation** du manager (le chef d'agence).
2. **Un justificatif original par ligne**, lisible, au nom de la société quand c'est possible.
3. **Caractère professionnel** : motif, lieu, et pour un repas d'affaires, **nom et société des invités**.
4. **Cohérence des dates** : pas de repas en déplacement à Toulon le même jour qu'un repas à Nice, dates dans la période.
5. **Kilomètres** : trajets plausibles (Nice – Toulon ≈ 150 km aller), **carte grise** au nom du salarié (ou de son conjoint) et puissance fiscale conforme au barème utilisé.
6. **Pas de double remboursement** : même ticket déjà présenté, ou dépense déjà payée par carte société.
7. **Plafonds internes** respectés (montant d'un repas, d'un cadeau).
8. **Avances** en cours déduites.
9. **TVA** : récupérée seulement quand elle figure sur le justificatif et que la dépense ouvre droit à déduction.

**Message au chef d'équipe (ligne 6)** : « Bonjour Karim, votre note de septembre est validée pour 440,92 €, soit 290,92 € après déduction de l'avance de 150,00 €. Le parking du 25/09 (12,00 €) n'a pas pu être remboursé faute de ticket ; pensez à photographier vos tickets dès le paiement. »

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 421, 425, 44566, 512, 530, 6063, 6234, 6251, 6256, 6257, 626, 658.
- CGI art. 39 (charges déductibles : dépenses engagées dans l'intérêt de l'entreprise et justifiées) ; barème kilométrique publié chaque année par l'administration fiscale (*valeurs à vérifier*).
- CGI art. 271 et annexe II art. 206 (déduction de la TVA ; exclusion des cadeaux sauf biens de très faible valeur — *seuil à vérifier*).
- Réglementation sociale des frais professionnels (remboursement de frais réels justifiés non soumis à cotisations) — *textes à vérifier*.
