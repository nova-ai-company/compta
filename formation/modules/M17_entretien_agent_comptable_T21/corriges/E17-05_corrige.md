# Corrigé E17-05 — Les frais du mois des professionnels : contrôler et payer

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **BOFiP** | Bulletin officiel des finances publiques. La doctrine officielle de l'administration fiscale : elle explique comment l'administration applique la loi. |
    | **BOSS** | Bulletin officiel de la sécurité sociale. La doctrine officielle de l'URSSAF sur les cotisations (équivalent social du BOFiP). |
    | **BQ** | Journal de banque. Journal qui reprend les mouvements du relevé bancaire. |
    | **CCN** | Convention collective nationale. Accord de branche qui complète le Code du travail (salaires minimaux, primes, congés…). |
    | **CGI** | Code général des impôts. Le code qui contient toutes les règles fiscales (TVA, IS, IR…). « art. 39 CGI » = article 39 de ce code. |
    | **CV** | Chevaux fiscaux (puissance fiscale). Puissance administrative d'une voiture, inscrite sur la carte grise. Le barème kilométrique dépend du nombre de CV. |
    | **EPRD** | État des prévisions de recettes et de dépenses. Budget prévisionnel des gestionnaires sous CPOM. Il part de la ressource notifiée par le financeur (« budget par la recette »). Dépôt en général au 30 avril (à vérifier chaque année). |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **URSSAF** | Organisme de recouvrement des cotisations sociales. Collecte les cotisations sociales (maladie, famille, CSG…) des salariés et des indépendants. |
    | **Compte 120** | Résultat de l'exercice (excédent). Le bénéfice de l'année, avant sa répartition (affectation). |
    | **Compte 421** | Personnel. Rémunérations dues : les salaires nets à verser. |
    | **Compte 425** | Personnel. Avances et acomptes : argent avancé à un salarié avant la paie. |
    | **Compte 467** | Autres comptes débiteurs ou créditeurs. Compte de tiers « divers » (ex. : frais à rembourser à un salarié, subvention à reverser). |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 4286** | Personnel. Autres charges à payer (ex. : frais à rembourser à la clôture). |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 6256** | Missions. Repas et frais des salariés en déplacement. |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **habitat inclusif** | Logement partagé en milieu ordinaire. Des personnes handicapées vivent ensemble chez elles, avec un projet de vie partagé animé par l'association. |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E17-05](../exercices/E17-05_frais-professionnels-controler-payer.md)

!!! abstract "En clair"
    Sur 1 627,03 € demandés, on rembourse **1 365,46 €**. Les 261,57 € restants ne sont pas une « punition » : ce sont des frais **sans justificatif**, **personnels**, **déjà payés** par la carte carburant, ou **en contradiction avec le planning**. Chaque refus s'explique en une phrase au salarié.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Les trois questions à poser pour chaque ligne

1. **Est-ce réel ?** Il faut un justificatif (ticket, relevé de badge) ou, pour les kilomètres, un tableau des trajets signé.
2. **Est-ce professionnel ?** Le planning, le programme ou le carnet de bord doivent confirmer le déplacement.
3. **Est-ce déjà payé ?** Par la carte carburant, par un repas fourni, par un autre état de frais.

Et une question pour l'état entier : **qui l'a validé ?** Personne ne valide ses propres frais.

### Question 1 — Ligne par ligne

**État n° 1 — Thomas Girard (SESSAD) : tout est accepté.**

| Ligne | Décision | Pourquoi |
|---|---|---|
| 412 km | Accepté | Tableau signé, visé par le chef de service. Cumul 3 980 + 412 = 4 392 km : on reste dans la tranche « jusqu'à 5 000 km » |
| Parkings 7,70 € | Accepté | Deux tickets |
| 6 forfaits repas | Accepté | Planning conforme |

**État n° 2 — Inès Roche (SAVS) : une journée en contradiction avec le planning.**

| Ligne | Décision | Pourquoi |
|---|---|---|
| 474 km (538 − 64) | Accepté | Tableau signé et visé |
| 64 km du 14/10 | **Suspendu** | Le 14/10, Inès était **en formation au siège** de 9 h à 17 h. A-t-elle fait des visites avant ou après ? Erreur de date ? On lui demande, sans l'accuser. Si c'est justifié, paiement le mois prochain |
| 8 forfaits repas | Accepté | Planning conforme |
| Forfait du 14/10 | **Refusé** | Le déjeuner était **fourni** par l'association |

**État n° 3 — Rachid Haddad (SAVS et habitat inclusif) : deux frais sans justificatif.**

| Ligne | Décision | Pourquoi |
|---|---|---|
| 196 km SAVS | Accepté | Code **20-SAVS** |
| 90 km habitat | Accepté | Code **40-HABITAT** : l'habitat inclusif a son propre financement, il doit porter ses propres frais |
| Péage aller 4,60 € | Accepté | Ticket |
| Péage retour 4,60 € | **Suspendu** | Pas de ticket. Le retour a sans doute eu lieu, mais la règle est la même pour tous. Si Rachid a un badge télépéage, le **relevé** suffit |
| Parking 9,00 € | **Suspendu** | Pas de ticket |
| 3 forfaits repas | Accepté | 2 SAVS + 1 habitat |

**État n° 4 — Julie Marchetti (emploi accompagné) : une double demande.**

| Ligne | Décision | Pourquoi |
|---|---|---|
| 60 km du 06/10 | Accepté | Véhicule personnel, rien au carnet de bord ce jour-là |
| 55 km du 13/10 et 65 km du 20/10 | **Refusé** | Le **carnet de bord** montre que Julie avait le **véhicule de service VS-03** ces jours-là. Elle n'a pas utilisé sa voiture |
| Parking 5,00 € | Accepté | Ticket |
| Carburant 62,30 € | **Refusé** | Le relevé de la **carte carburant** montre la même dépense, même jour, même station, même montant. Le plein est **déjà payé** par l'association. Le ticket de caisse est celui imprimé lors du paiement par carte |
| 2 forfaits repas | Accepté | Le forfait repas ne dépend pas du véhicule utilisé |

**État n° 5 — Karim Belkacem (SESSAD) : une dépense personnelle et un visa irrégulier.**

| Ligne | Décision | Pourquoi |
|---|---|---|
| 214 km | Accepté (après visa de la directrice) | Journée du réseau : déplacement professionnel. Cumul 1 920 + 214 = 2 134 km |
| Péages 21,80 € | Accepté | Deux tickets |
| Parking 18,00 € | Accepté | Ticket |
| Forfait repas du midi | Accepté | « Déjeuner libre » au programme |
| Dîner 64,00 € | **Refusé** | **Dépense personnelle** : la journée finissait à 17 h, Karim est resté à Lyon pour le week-end, avec son épouse. Rien de professionnel |

### Question 3 — Le visa de Karim Belkacem

Karim a **visé son propre état**. Personne ne valide ses propres dépenses : c'est la base du **contrôle interne**. Pour un chef de service, le visa revient à la **directrice**. On présente donc l'état (corrigé du dîner) à Nathalie Berthier lors de la séance de signature du 12/11, **avant** le paiement du 13/11. Pour les frais de la directrice elle-même, le visa revient à la **trésorière** (ou au président).

> ⚠️ Erreur classique : rembourser un chef de service « parce que c'est le chef ». Le commissaire aux comptes regarde justement les frais des cadres et des dirigeants. C'est un point classique de son contrôle.

### Question 5 — Pourquoi un compte 467 par salarié ?

Le salarié a avancé de l'argent pour l'association. L'association lui doit cette somme : c'est une **dette envers lui**, à enregistrer au **crédit** d'un compte de tiers, puis à solder au remboursement.

| Compte | Quand l'utiliser | Avantages / limites |
|---|---|---|
| **467xxx** (un sous-compte par salarié) — **choix de Cap Horizons 21** | Remboursement **hors paie**, par virement séparé | Les frais sont **séparés des salaires** : le compte 421 reste réservé à la paie et se contrôle facilement contre le journal de paie. Le lettrage état de frais / virement est simple, salarié par salarié |
| 421 (sous-compte « frais ») | Remboursement **avec le salaire**, sur le bulletin | Logique si la paie rembourse les frais. Mais risque de mélange : un 421 non soldé ne dit plus si c'est la paie ou les frais |
| 4286 Personnel – autres charges à payer | **À la clôture** seulement : frais de décembre connus mais pas encore traités au 31/12 | Ce n'est pas un compte de gestion courante |
| 425 Personnel – avances et acomptes | Quand l'association **avance** de l'argent **avant** la dépense (avance pour un séjour, par exemple) | Le salarié doit l'argent à l'association ; on impute ensuite l'état de frais sur l'avance |

Le plus important : **une seule méthode**, écrite dans la procédure, appliquée tous les mois, et un compte **soldé** après chaque remboursement.

## 2. Calculs (détaillés, chaque montant justifié)

| Salarié | Détail du calcul | Accepté | Demandé |
|---|---|---|---|
| Thomas Girard | 412 × 0,636 = 262,03 ; parkings 7,70 ; 6 × 19,40 = 116,40 | **386,13** | 386,13 |
| Inès Roche | 474 × 0,606 = 287,24 ; 8 × 19,40 = 155,20 | **442,44** | 538 × 0,606 = 326,03 + 9 × 19,40 = 174,60 → 500,63 |
| Rachid Haddad | SAVS : 196 × 0,665 = 130,34 + péage 4,60 + 2 × 19,40 = 38,80 → 173,74 ; habitat : 90 × 0,665 = 59,85 + 19,40 → 79,25 | **252,99** | 252,99 + 4,60 + 9,00 = 266,59 |
| Julie Marchetti | 60 × 0,529 = 31,74 ; parking 5,00 ; 2 × 19,40 = 38,80 | **75,54** | 180 × 0,529 = 95,22 + 62,30 + 5,00 + 38,80 → 201,32 |
| Karim Belkacem | 214 × 0,697 = 149,16 ; péages 21,80 ; parking 18,00 ; 19,40 | **208,36** | 208,36 + 64,00 = 272,36 |
| **Total** | | **1 365,46** | **1 627,03** |

**Ce qui n'est pas payé : 1 627,03 − 1 365,46 = 261,57 €**

| Salarié | Montant | Statut |
|---|---|---|
| Inès Roche | 64 × 0,606 = 38,79 (suspendu) + 19,40 (refusé) = 58,19 | 38,79 payable plus tard si justifié |
| Rachid Haddad | 4,60 + 9,00 = 13,60 | Suspendu (justificatif) |
| Julie Marchetti | 120 × 0,529 = 63,48 + 62,30 = 125,78 | Refusé (véhicule de service + carte carburant) |
| Karim Belkacem | 64,00 | Refusé (dépense personnelle) |
| **Total** | **261,57** | ✓ |

**Répartition par compte et par service**

| Service | 6251 Voyages et déplacements | 6256 Missions | Total |
|---|---|---|---|
| 10-SESSAD (Thomas + Karim) | 269,73 + 188,96 = 458,69 | 116,40 + 19,40 = 135,80 | 594,49 |
| 20-SAVS (Inès + Rachid SAVS) | 287,24 + 134,94 = 422,18 | 155,20 + 38,80 = 194,00 | 616,18 |
| 30-EMPLOI (Julie) | 36,74 | 38,80 | 75,54 |
| 40-HABITAT (Rachid habitat) | 59,85 | 19,40 | 79,25 |
| **Total** | **977,46** | **388,00** | **1 365,46** |

Pas de TVA à isoler : l'association ne la récupère pas, et les indemnités kilométriques et forfaits repas n'en comportent pas.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6251 | Voyages et déplacements | Frais 10/2026 T. Girard – 412 km 5 CV + parkings | 10-SESSAD | 269,73 | |
| 31/10/2026 | OD | 6256 | Missions | Frais 10/2026 T. Girard – 6 forfaits repas | 10-SESSAD | 116,40 | |
| 31/10/2026 | OD | 467GIR | Frais à rembourser – T. Girard | Frais 10/2026 T. Girard | — | | 386,13 |
| 31/10/2026 | OD | 6251 | Voyages et déplacements | Frais 10/2026 I. Roche – 474 km 4 CV | 20-SAVS | 287,24 | |
| 31/10/2026 | OD | 6256 | Missions | Frais 10/2026 I. Roche – 8 forfaits repas | 20-SAVS | 155,20 | |
| 31/10/2026 | OD | 467ROC | Frais à rembourser – I. Roche | Frais 10/2026 I. Roche | — | | 442,44 |
| 31/10/2026 | OD | 6251 | Voyages et déplacements | Frais 10/2026 R. Haddad – 196 km 6 CV + péage | 20-SAVS | 134,94 | |
| 31/10/2026 | OD | 6251 | Voyages et déplacements | Frais 10/2026 R. Haddad – 90 km 6 CV | 40-HABITAT | 59,85 | |
| 31/10/2026 | OD | 6256 | Missions | Frais 10/2026 R. Haddad – 2 forfaits repas | 20-SAVS | 38,80 | |
| 31/10/2026 | OD | 6256 | Missions | Frais 10/2026 R. Haddad – 1 forfait repas | 40-HABITAT | 19,40 | |
| 31/10/2026 | OD | 467HAD | Frais à rembourser – R. Haddad | Frais 10/2026 R. Haddad | — | | 252,99 |
| 31/10/2026 | OD | 6251 | Voyages et déplacements | Frais 10/2026 J. Marchetti – 60 km 3 CV + parking | 30-EMPLOI | 36,74 | |
| 31/10/2026 | OD | 6256 | Missions | Frais 10/2026 J. Marchetti – 2 forfaits repas | 30-EMPLOI | 38,80 | |
| 31/10/2026 | OD | 467MAR | Frais à rembourser – J. Marchetti | Frais 10/2026 J. Marchetti | — | | 75,54 |
| 31/10/2026 | OD | 6251 | Voyages et déplacements | Frais 10/2026 K. Belkacem – Lyon 214 km 7 CV, péages, parking | 10-SESSAD | 188,96 | |
| 31/10/2026 | OD | 6256 | Missions | Frais 10/2026 K. Belkacem – 1 forfait repas | 10-SESSAD | 19,40 | |
| 31/10/2026 | OD | 467BEL | Frais à rembourser – K. Belkacem | Frais 10/2026 K. Belkacem | — | | 208,36 |
| 13/11/2026 | BQ | 467GIR | Frais à rembourser – T. Girard | Virement frais 10/2026 | — | 386,13 | |
| 13/11/2026 | BQ | 467ROC | Frais à rembourser – I. Roche | Virement frais 10/2026 | — | 442,44 | |
| 13/11/2026 | BQ | 467HAD | Frais à rembourser – R. Haddad | Virement frais 10/2026 | — | 252,99 | |
| 13/11/2026 | BQ | 467MAR | Frais à rembourser – J. Marchetti | Virement frais 10/2026 | — | 75,54 | |
| 13/11/2026 | BQ | 467BEL | Frais à rembourser – K. Belkacem | Virement frais 10/2026 | — | 208,36 | |
| 13/11/2026 | BQ | 512 | Banque | Remise frais professionnels 10/2026 | — | | 1 365,46 |
| | | | | **Totaux** | | **2 730,92** | **2 730,92** |

Après le virement, chaque compte 467 est **soldé** : on lettre l'état de frais avec le virement.

Les écritures sont datées du **31/10** : les frais appartiennent au mois d'**octobre**, même s'ils sont payés en novembre. C'est important pour le **suivi budgétaire mensuel** de chaque service. Cela compte aussi en décembre : les frais de décembre payés en janvier sont des **charges de l'exercice** qui se termine.

Les sommes suspendues (38,79 € pour Inès, 13,60 € pour Rachid) ne sont **pas** comptabilisées : elles le seront le mois où le justificatif arrivera.

## 4. Points d'attention / pièges

- **Rembourser le carburant d'un véhicule de service** : l'association paie **deux fois** le même plein. Le contrôle croisé « état de frais / carnet de bord / relevé de carte carburant » est indispensable.
- **Payer des kilomètres un jour où le planning dit autre chose** : le planning est la preuve du caractère professionnel du trajet. En cas de doute, on **suspend** et on pose la question.
- **Le forfait repas quand le repas est fourni** : on paie un repas qui n'a rien coûté au salarié.
- **Les frais sans justificatif** : un remboursement sans justificatif peut être **requalifié en salaire** par l'URSSAF, avec des cotisations à payer.
- **Les frais dépassant les limites d'exonération** : les indemnités kilométriques au barème fiscal et un forfait repas dans les limites admises ne sont pas soumis à cotisations. Au-delà, l'**excédent** entre dans l'assiette des cotisations *(limites URSSAF à vérifier chaque année)*.
- **Tout imputer au service principal du salarié** : les 90 km de Rachid pour l'habitat inclusif seraient payés par le SAVS, dont le financeur (le Département) ne finance pas l'habitat.
- **Oublier le cumul annuel** : au-delà de **5 000 km** dans l'année, le barème fiscal change de formule. Il faut suivre le cumul de chaque salarié (Thomas Girard en est à 4 392 km : il dépassera sans doute 5 000 km en décembre).
- **Payer un état visé par le demandeur lui-même** : faute de contrôle interne, même si le montant est juste.

> 💡 Réflexe senior : un refus se fait **par écrit**, ligne par ligne, avec la règle appliquée, et **sans jugement**. Dans 9 cas sur 10, c'est une erreur de bonne foi (mauvaise date, mélange entre deux véhicules). Si les erreurs se répètent chez la même personne, on en parle à la directrice.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Message à Julie Marchetti (question 6) :**

> Bonjour Julie,
>
> J'ai traité votre état de frais d'octobre. Je vous rembourse **75,54 €** le 13/11 : 60 km du 06/10, le parking du 06/10 et vos 2 forfaits repas.
>
> Je n'ai pas pu reprendre deux éléments. Les **13/10 et 20/10**, le carnet de bord indique que vous aviez le **véhicule de service VS-03** : les kilomètres de ces deux jours ne sont donc pas remboursables en indemnités kilométriques. Et le **plein du 20/10 (62,30 €)** a été payé avec la **carte carburant** du VS-03 (il apparaît sur le relevé de la carte) : il est déjà réglé par l'association.
>
> Si je me trompe, par exemple si vous avez utilisé votre voiture pour une partie du trajet, dites-le-moi et nous regarderons ensemble.
>
> Bonne journée,
> [Prénom Nom], agent comptable

**Question 7 — Trois contrôles mensuels :**
1. **Rapprochement des cartes carburant** avec les carnets de bord des 8 véhicules de service : litres et kilomètres cohérents, aucun plein un jour où le véhicule n'a pas roulé, aucun plein sur un véhicule pendant qu'un salarié demande des kilomètres pour le même trajet.
2. **Suivi du cumul kilométrique** de chaque salarié (seuil de 5 000 km du barème) et des **montants par service** comparés au budget (les frais de déplacement pèsent lourd au SESSAD et au SAVS).
3. **Comptes 467 soldés** après chaque remise. Un solde ancien signifie un état oublié ou un virement en erreur.

**Pour aller plus loin :**
- Conseiller un **outil de notes de frais** avec photo du justificatif et circuit de validation : moins de papier, et le visa par le bon supérieur est imposé par l'outil.
- Si les kilomètres en véhicule personnel deviennent très importants dans un service, faire comparer par la directrice le coût des indemnités et celui d'un véhicule de service de plus : c'est une donnée utile pour l'**EPRD** et pour le prochain budget.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 6251 « Voyages et déplacements », 6256 « Missions », 421, 425, 4286, 467 ; règlement ANC n° 2018-06 pour les associations.
- Barème kilométrique fiscal publié chaque année par l'administration fiscale (*valeurs à vérifier chaque année*).
- Réglementation URSSAF sur les frais professionnels : allocations forfaitaires, indemnités kilométriques, indemnités de repas et leurs limites d'exonération (*valeurs à vérifier chaque année ; doctrine dans le BOSS, bulletin officiel de la sécurité sociale*).
- CCN du 15 mars 1966 : remboursement des frais de déplacement et de repas (*hypothèse de l'association ; dispositions à vérifier dans la convention*).
- Fiche de l'association Cap Horizons 21 : § 3.6 (frais des professionnels).
