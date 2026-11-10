# E16-10 — Construire le tableau de bord mensuel de la direction
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★☆ | **Durée estimée :** 60 min | **Thèmes :** tableau de bord, indicateurs de pilotage, taux d'occupation, taux d'activité, coût par place, poids des charges de personnel, écart budgétaire cumulé, retraitements avant calcul, jours de trésorerie, délai moyen de paiement des fournisseurs, Excel (SOMME.SI.ENS, RECHERCHEV, RECHERCHEX, FIN.MOIS, tableau croisé dynamique, mise en forme conditionnelle), seuils d'alerte (feux tricolores)

**Corner case :** oui — les indicateurs calculés « brut » sur la comptabilité d'octobre sont faussés (amortissements passés seulement au 31/12, frais de siège facturés par trimestre, crédits non reconductibles encaissés mais pas encore dépensés) : il faut retraiter avant d'afficher un feu vert

> *Cadre de formation : association, personnes et chiffres fictifs. Cet exercice reprend les chiffres de [E16-06](E16-06_suivi-budgetaire-30-septembre.md) au 30/09 et y ajoute le mois d'octobre. Excel en français : séparateur « ; », fonctions en français.*

!!! abstract "En clair"
    Un **tableau de bord**, c'est une page qui permet à la directrice de voir **en deux minutes** si chaque service va bien : activité, coûts, budget, trésorerie, fournisseurs. Chaque indicateur a une **formule**, une **valeur cible** et un **feu** (vert, orange, rouge). Votre travail : des chiffres **justes** (retraités), des formules **automatiques** (le mois prochain, on change seulement la date) et un **commentaire** court qui dit quoi faire.

## La mise en situation

Mardi 10/11/2026. Nathalie Berthier, directrice générale :

> « Mme Roux me faisait un tableau à la main, différent chaque mois. Je voudrais un vrai tableau de bord mensuel, toujours le même, une page, avec des feux. Pour chaque service : est-ce qu'on fait l'activité prévue, est-ce qu'on tient le budget, combien coûte une place. Et pour l'association : combien de jours on tient avec notre trésorerie, et est-ce qu'on paie nos fournisseurs à l'heure. Vous me faites celui d'octobre, et vous me montrez comment il se met à jour tout seul ? »

Hypothèses retenues (à valider avec la directrice) :

- Le tableau porte sur les trois services financés par des fonds publics à l'activité : **SESSAD** (10), **SAVS** (20) et **emploi accompagné** (30).
- **Retraitements** avant calcul des indicateurs de coût (SESSAD et SAVS) : ajouter les **amortissements** de l'année au prorata des mois écoulés (ils ne sont passés qu'au 31/12), et la **quote-part de frais de siège d'octobre** (facturée seulement le 31/12 avec le 4e trimestre). Pour l'emploi accompagné, les frais de siège sont imputés chaque mois et il n'y a pas d'immobilisation : aucun retraitement.
- Charges décaissables annuelles de l'association (hors amortissements, hors frais de siège internes, qui ne sortent pas de la banque) : **2 300 000 €**.

## Les pièces

**Pièce 1 — Charges réalisées par service et par groupe fonctionnel (balance analytique)**

| Service | Groupe | Cumul au 30/09/2026 | Mois d'octobre 2026 |
|---|---|---|---|
| 10-SESSAD | I – Exploitation courante | 63 600,00 | 7 100,00 |
| 10-SESSAD | II – Personnel | 690 300,00 | 77 900,00 |
| 10-SESSAD | III – Structure | 102 910,00 | 7 200,00 |
| 20-SAVS | I – Exploitation courante | 38 100,00 | 4 300,00 |
| 20-SAVS | II – Personnel | 384 900,00 | 42 300,00 |
| 20-SAVS | III – Structure | 59 820,00 | 4 283,33 |
| 30-EMPLOI | I – Exploitation courante | 17 300,00 | 1 900,00 |
| 30-EMPLOI | II – Personnel | 192 400,00 | 21 600,00 |
| 30-EMPLOI | III – Structure | 16 600,00 | 1 800,00 |

**Pièce 2 — Budgets 2026 des charges**

| Service | Groupe I | Groupe II | Groupe III | Total | Amortissements prévus 2026 | Frais de siège 2026 |
|---|---|---|---|---|---|---|
| 10-SESSAD | 82 000,00 | 936 000,00 | 162 000,00 | 1 180 000,00 | 26 000,00 | 50 813,00 |
| 20-SAVS | 48 000,00 | 505 000,00 | 87 000,00 | 640 000,00 | 5 000,00 *(véhicule neuf reporté)* | 27 560,00 |
| 30-EMPLOI | 24 000,00 | 252 000,00 | 24 000,00 | 300 000,00 | — | imputés chaque mois |

**Pièce 3 — Activité (cumul de janvier à octobre 2026)**

| Service | Places autorisées / objectif | Personnes accompagnées au 31/10 | Unité d'activité | Prévu (cumul 10 mois) | Réalisé (cumul 10 mois) |
|---|---|---|---|---|---|
| 10-SESSAD | 45 | 43 | actes (interventions directes) | 8 250 | 7 640 |
| 20-SAVS | 60 | 58 | heures d'accompagnement | 12 500 | 11 350 |
| 30-EMPLOI | 40 | 37 | heures d'accompagnement | 4 000 | 3 820 |

**Pièce 4 — Trésorerie de l'association en fin de mois (comptes 512 + livret)**

| Mois | Jan. | Fév. | Mars | Avr. | Mai | Juin | Juil. | Août | Sept. | Oct. |
|---|---|---|---|---|---|---|---|---|---|---|
| Solde (k€) | 468 | 451 | 437 | 402 | 389 | 371 | 352 | 384 | 395 | 412 |

*Le solde d'octobre comprend les CNR (crédits non reconductibles) de 25 000 € du SESSAD, reçus le 20/10 et à dépenser en novembre.*

**Pièce 5 — Fournisseurs**

| Élément | Au 30/09/2026 | Au 31/10/2026 |
|---|---|---|
| Solde créditeur du compte 401 (factures reçues non payées) | 58 900,00 | 86 400,00 |
| Achats TTC des 3 derniers mois (factures reçues) | juil. 61 500 + août 61 200 + sept. 74 300 = 197 000,00 | août 61 200 + sept. 74 300 + oct. 78 500 = 214 000,00 |

```
Note de l'agent comptable : Nathalie Berthier était en congé du 12 au 23/10.
Aucune délégation de signature des bons à payer n'avait été prévue.
```

**Pièce 6 — Organisation du fichier Excel souhaitée**

```
Onglet « Donnees »  : une ligne par écriture analytique (table Excel nommée tData)
  A Date (fin de mois) | B Service | C Groupe (GI, GII, GIII) | D Compte | E Libellé | F Montant
Onglet « Budget »   : A Cle (= Service|Groupe) | B Service | C Groupe | D Budget annuel
Onglet « Activite » : A Date | B Service | C Places | D Personnes accompagnées | E Prévu | F Réalisé
Onglet « TDB »      : B1 = date d'arrêté (31/10/2026) ; le reste se calcule
```

## Travail à faire

1. Calculez, pour chaque service, les charges **cumulées au 31/10**, le **budget proratisé** (10/12), l'écart en € et en %, **avant** puis **après** retraitements. Commentez la différence pour le SESSAD.
2. Calculez pour chaque service le **taux d'occupation**, le **taux d'activité**, le **coût annualisé par place** (charges retraitées × 12/10 ÷ places) comparé au coût budgété, et le **poids du personnel** (groupe II ÷ total des charges retraitées) comparé au budget.
3. Calculez les **jours de trésorerie** au 31/10 (avec et sans les CNR) et le **délai moyen de paiement des fournisseurs** au 30/09 et au 31/10. Commentez.
4. Proposez des **seuils** (vert, orange, rouge) pour chaque indicateur et présentez le **tableau de bord commenté** d'octobre.
5. Donnez les **formules Excel** : réalisé cumulé (SOMME.SI.ENS), budget (RECHERCHEV puis RECHERCHEX), écart, feu tricolore (SI), jours de trésorerie, délai fournisseurs (avec FIN.MOIS). Expliquez comment obtenir la répartition par groupe avec un **tableau croisé dynamique** (TCD) et comment afficher les feux avec la **mise en forme conditionnelle**.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E16-10_corrige.md)
