# Corrigé E18-04 — Quatre notes de frais : contrôler, saisir, rembourser

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CV** | Chevaux fiscaux (puissance fiscale). Puissance administrative d'une voiture, inscrite sur la carte grise. Le barème kilométrique dépend du nombre de CV. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 467** | Autres comptes débiteurs ou créditeurs. Compte de tiers « divers » (ex. : frais à rembourser à un salarié, subvention à reverser). |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6256000** | Missions (plan T21). Repas et hébergement en mission. |
    | **Compte 6256700** | Missions - Journées Fédérales (plan T21). Déplacements pour les journées fédérales. |
    | **SABERTHIER** | Compte salarié : Nathalie Berthier (dossier M18). Notes de frais de la directrice : visées par le président ou la trésorière. |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **SAGIRARD** | Compte salarié : Thomas Girard (dossier M18). Notes de frais d'un éducateur du SESSAD. |
    | **SAHADDAD** | Compte salarié : Rachid Haddad (dossier M18). Notes de frais d'un CESF (SAVS et habitat inclusif). |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **habitat inclusif** | Logement partagé en milieu ordinaire. Des personnes handicapées vivent ensemble chez elles, avec un projet de vie partagé animé par l'association. |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-04](../exercices/E18-04_notes-de-frais.md)

!!! abstract "En clair"
    Trois notes sont remboursées le 20/11/2026 : Nathalie Durand **205,60 €**, Thomas Girard **366,73 €** (un forfait repas refusé : le repas était offert), Rachid Haddad **252,99 €**, **en deux parties** (173,74 € par le SAVS et 79,25 € par l'association pour l'habitat inclusif). La note de la directrice est **mise en attente** : elle doit être visée par le président ou la trésorière, et deux dépenses sont refusées (le bar de l'hôtel et le déjeuner offert). Après visa, on lui remboursera **362,28 €** au lieu des 400,18 € demandés.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Pour chaque ligne d'une note de frais, trois questions :

1. **Est-ce réel ?** Justificatif (ticket, facture, e-billet) ou, pour les kilomètres, tableau des trajets signé.
2. **Est-ce professionnel ?** Le planning ou le programme confirment le déplacement ; rien de personnel.
3. **Est-ce déjà payé ?** Repas fourni, dépense déjà réglée par une carte de l'association.

Puis, pour la note entière : **qui l'a visée ?** Et **pour quelle structure** sont les dépenses ?

### Question 1 — Ligne par ligne

**Note n° 1 — Nathalie Durand (SESSAD) : tout est accepté.** C'est exactement l'exemple du document T21 : des indemnités kilométriques en 6251000 et des fournitures en 6062400. L'achat a été autorisé par le chef de service (mention sur le visa).

**Note n° 2 — Thomas Girard (SESSAD) : un forfait refusé.**

| Ligne | Décision | Pourquoi |
|---|---|---|
| 412 km | Acceptée | Tableau signé et visé |
| Parkings 7,70 € | Acceptée | Deux tickets |
| 5 forfaits repas | Acceptée | Planning conforme |
| Forfait du 22/10 | **Refusé** | Réunion de synthèse au service, **repas offert** : pas de dépense pour le salarié |

**Note n° 3 — Rachid Haddad (SAVS et habitat inclusif) : tout est accepté, mais à répartir.**

| Ligne | Décision | Structure / code |
|---|---|---|
| 196 km | Acceptée | SAV / 20-SAVS |
| 90 km | Acceptée | **ASS / 40-HABITAT** |
| Péage 4,60 € | Acceptée | SAV / 20-SAVS (rendez-vous d'une personne accompagnée par le SAVS) |
| 2 forfaits (08/10, 15/10) | Acceptée | SAV / 20-SAVS |
| 1 forfait (21/10) | Acceptée | **ASS / 40-HABITAT** |

**Note n° 4 — Nathalie Berthier (siège) : en attente de visa, deux refus.**

| Ligne | Décision | Pourquoi |
|---|---|---|
| 22 km | Acceptée (après visa) | Trajet siège – gare, professionnel |
| Parking 24,00 € | Acceptée (après visa) | Ticket |
| Train 148,00 € | Acceptée (après visa) | E-billet |
| Métro 10,00 € | Acceptée (après visa) | Reçu |
| Hôtel : chambre, petit-déjeuner, taxe de séjour = 146,25 € | Acceptée (après visa) | Facture de l'hôtel au nom de la directrice **et** de l'association |
| Hôtel : bar 18,50 € | **Refusée** | **Dépense personnelle** (consommation au bar à 22 h 40). Elle reste à la charge de la directrice |
| Forfait dîner du 05/11 | Acceptée (après visa) | « Soirée libre » au programme : elle a dû dîner à ses frais |
| Forfait déjeuner du 06/11 | **Refusé** | « Déjeuner offert par la Fédération » |

### Question 3 — Une note, deux structures

Les dépenses de Rachid concernent **deux financeurs** : le Département pour le SAVS, et les financeurs de l'habitat inclusif (aide à la vie partagée, rattachée à la structure ASS). Tout saisir au SAVS ferait payer au Département des frais de l'habitat inclusif : ses comptes seraient faux, et le compte rendu financier de l'habitat inclusif aussi.

**Solution la plus simple** : traiter la note comme **deux notes**, une par structure.

- Dans les livres du **SAV** : saisie de la partie SAVS (173,74 €), compte de tiers SAHADDAD, remboursement par la banque du SAVS (BQSAV).
- Dans les livres de l'**ASS** : saisie de la partie habitat (79,25 €), compte de tiers SAHADDAD, remboursement par la banque de l'association (BQASS).

Rachid reçoit deux virements le même jour. Pour les mois suivants, on lui demande de remplir **deux notes** (ou une note en deux parties, avec un total par structure).

*Autre solution, plus lourde : tout saisir au SAVS puis faire une inter-structure. Mais les comptes de liaison du dossier relient chaque structure **au siège** : il faudrait passer par le siège (SAV → SIE → ASS), soit trois écritures pour 79,25 €. On la réserve aux cas où une seule structure peut payer.*

### Question 4 — La note de la directrice

- **Qui vise ?** La directrice n'a pas de supérieur salarié : sa note est visée par un **membre du bureau**, le **président** (Jean-Marc Lefort) ou la **trésorière** (Odile Marchand). Personne ne valide ses propres dépenses : c'est la base du contrôle interne, et les frais des dirigeants sont un point que le commissaire aux comptes regarde systématiquement.
- **En attendant** : on ne la saisit pas pour paiement (règle de l'association : rien n'est saisi pour paiement sans validation). On la met dans la chemise « en attente », avec une note : montant accepté 362,28 €, refus du bar (18,50 €) et du déjeuner offert (19,40 €). On la présente à la trésorière, **avec** ces deux refus déjà indiqués : la trésorière vise un montant clair, et la directrice voit pourquoi il diffère de sa demande.
- **Quel compte ?** Le plan T21 contient un compte **6256700 Missions – Journées fédérales**. C'est exactement l'objet du déplacement : on l'utilise pour l'hôtel et le repas. Il permet de suivre le coût de la participation aux journées du réseau. Le train, le métro, le parking et les kilomètres restent en **6251000** Voyages et déplacements. *(Si la procédure de l'association préfère le compte général 6256000 Missions, on l'applique : l'important est d'être constant d'un déplacement à l'autre.)*

## 2. Calculs (détaillés, chaque montant justifié)

| Salarié | Détail | 6251000 | 6256000 / 6256700 | 6062400 | Total remboursé |
|---|---|---|---|---|---|
| N. Durand | 286 × 0,636 = 181,896 → 181,90 ; fournitures 23,70 | 181,90 | | 23,70 | **205,60** |
| T. Girard | 412 × 0,636 = 262,032 → 262,03 ; parkings 3,50 + 4,20 = 7,70 ; repas 5 × 19,40 = 97,00 | 269,73 | 97,00 | | **366,73** |
| R. Haddad – SAVS | 196 × 0,665 = 130,34 ; péage 4,60 ; repas 2 × 19,40 = 38,80 | 134,94 | 38,80 | | **173,74** |
| R. Haddad – habitat | 90 × 0,665 = 59,85 ; repas 1 × 19,40 = 19,40 | 59,85 | 19,40 | | **79,25** |
| N. Berthier (après visa) | 22 × 0,665 = 14,63 ; parking 24,00 ; train 148,00 ; métro 10,00 → 196,63. Hôtel 129,00 + 14,00 + 3,25 = 146,25 ; repas 19,40 → 165,65 (6256700) | 196,63 | 165,65 | | **362,28** |

**Contrôle des demandes**

| Salarié | Demandé | Accepté | Écart | Motif |
|---|---|---|---|---|
| N. Durand | 205,60 | 205,60 | 0,00 | — |
| T. Girard | 262,03 + 7,70 + 6 × 19,40 = 386,13 | 366,73 | 19,40 | Repas offert le 22/10 |
| R. Haddad | 252,99 | 252,99 | 0,00 | — (réparti sur deux structures) |
| N. Berthier | 14,63 + 24,00 + 148,00 + 10,00 + 164,75 + 2 × 19,40 = 400,18 | 362,28 | 37,90 | Bar 18,50 (personnel) + déjeuner offert 19,40 |

Pas de TVA à isoler : l'association ne la récupère pas, et les indemnités kilométriques et forfaits n'en contiennent pas.

**Campagne du 20/11/2026** : BQSES 205,60 + 366,73 = **572,33 €** ; BQSAV **173,74 €** ; BQASS **79,25 €**. Note de la directrice : remboursement par BQSIE à la campagne suivante, après visa.

## 3. Écritures comptables

*Dans le journal des achats (AC), on saisit débits et crédits. Dans le journal de banque, on saisit seulement la ligne du salarié (SA au débit) ; la ligne 512 est ajoutée par le logiciel. Le compte 4248000 Salariés – NDF est alimenté automatiquement par le compte de tiers SA : on ne saisit jamais directement dans 4248000.*

### Note n° 1 — Nathalie Durand

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 6251000 Voyages et déplacements | | NDF Durand – 286 km 5 CV – 10/2026 | 10-SESSAD | 181,90 | |
| SES | AC | 6062400 Fournitures administratives | | NDF Durand – stylos et carnets – 14/10/2026 | 10-SESSAD | 23,70 | |
| SES | AC | 4248000 Salariés – NDF | SADURAND | NDF Durand – 10/2026 | | | 205,60 |
| SES | BQSES | 4248000 Salariés – NDF | SADURAND | Virement NDF Durand 10/2026 – 20/11/2026 | | 205,60 | |
| SES | BQSES | 5122000 Crédit Mutuel – SESSAD *(ligne automatique)* | | Virement NDF Durand 10/2026 | | | 205,60 |

### Note n° 2 — Thomas Girard

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 6251000 Voyages et déplacements | | NDF Girard – 412 km 5 CV + 2 parkings – 10/2026 | 10-SESSAD | 269,73 | |
| SES | AC | 6256000 Missions | | NDF Girard – 5 forfaits repas – 10/2026 | 10-SESSAD | 97,00 | |
| SES | AC | 4248000 Salariés – NDF | SAGIRARD | NDF Girard – 10/2026 | | | 366,73 |
| SES | BQSES | 4248000 Salariés – NDF | SAGIRARD | Virement NDF Girard 10/2026 – 20/11/2026 | | 366,73 | |
| SES | BQSES | 5122000 Crédit Mutuel – SESSAD *(ligne automatique)* | | Virement NDF Girard 10/2026 | | | 366,73 |

### Note n° 3 — Rachid Haddad, en deux structures

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SAV | AC | 6251000 Voyages et déplacements | | NDF Haddad – 196 km 6 CV + péage A7 15/10 – 10/2026 – part SAVS | 20-SAVS | 134,94 | |
| SAV | AC | 6256000 Missions | | NDF Haddad – 2 forfaits repas – 10/2026 – part SAVS | 20-SAVS | 38,80 | |
| SAV | AC | 4248000 Salariés – NDF | SAHADDAD | NDF Haddad – 10/2026 – part SAVS | | | 173,74 |
| SAV | BQSAV | 4248000 Salariés – NDF | SAHADDAD | Virement NDF Haddad 10/2026 part SAVS – 20/11/2026 | | 173,74 | |
| SAV | BQSAV | 5123000 Crédit Mutuel – SAVS *(ligne automatique)* | | Virement NDF Haddad 10/2026 part SAVS | | | 173,74 |
| ASS | AC | 6251000 Voyages et déplacements | | NDF Haddad – 90 km 6 CV – 10/2026 – Maison partagée | 40-HABITAT | 59,85 | |
| ASS | AC | 6256000 Missions | | NDF Haddad – 1 forfait repas 21/10 – Maison partagée | 40-HABITAT | 19,40 | |
| ASS | AC | 4248000 Salariés – NDF | SAHADDAD | NDF Haddad – 10/2026 – part habitat inclusif | | | 79,25 |
| ASS | BQASS | 4248000 Salariés – NDF | SAHADDAD | Virement NDF Haddad 10/2026 part habitat – 20/11/2026 | | 79,25 | |
| ASS | BQASS | 5125000 Crédit Mutuel – Association *(ligne automatique)* | | Virement NDF Haddad 10/2026 part habitat | | | 79,25 |

### Note n° 4 — Nathalie Berthier, **après** le visa de la trésorière (ou du président)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SIE | AC | 6251000 Voyages et déplacements | | NDF Berthier – journées fédérales Paris 05-06/11/2026 – train, métro, parking, 22 km | 01-SIEGE | 196,63 | |
| SIE | AC | 6256700 Missions – Journées fédérales | | NDF Berthier – journées fédérales – hôtel H-26-11-0412 (hors bar) + 1 repas | 01-SIEGE | 165,65 | |
| SIE | AC | 4248000 Salariés – NDF | SABERTHIER | NDF Berthier – journées fédérales 05-06/11/2026 – visa trésorière | | | 362,28 |
| SIE | BQSIE | 4248000 Salariés – NDF | SABERTHIER | Virement NDF Berthier 11/2026 | | 362,28 | |
| SIE | BQSIE | 5121000 Crédit Mutuel – Siège *(ligne automatique)* | | Virement NDF Berthier 11/2026 | | | 362,28 |

### Question 6 — Le lettrage

| Compte SADURAND | Débit | Crédit | Lettrage |
|---|---|---|---|
| AC – NDF Durand 10/2026 | | 205,60 | A |
| BQSES – virement du 20/11/2026 | 205,60 | | A |
| **Solde** | | **0,00** | |

La note (crédit : l'association doit 205,60 € à Nathalie Durand) et le virement (débit : la dette est payée) portent la même lettre A : le compte est **soldé**. Chaque compte SA doit être à zéro après chaque campagne de remboursement.

Un **solde non lettré** en fin de mois signifie :

- **solde créditeur** : une note saisie mais **pas encore payée** (normal pour une note en attente, comme celle de la directrice si on l'avait saisie ; anormal si elle traîne) ;
- **solde débiteur** : un virement **sans note** saisie (oubli de saisie, ou remboursement fait par erreur) : l'association a payé sans pièce, à régulariser immédiatement.

## 4. Points d'attention / pièges

- **Saisir une note au journal de banque directement** (charge au débit, banque au crédit) : c'est plus court, mais contraire à la règle T21 (les notes vont au journal des achats, avec un compte SA). On perdrait la trace de la dette envers le salarié entre la note et le paiement, et le lettrage.
- **Créditer 4248000 sans tiers** : interdit, c'est un compte de centralisation.
- **Tout saisir au SAVS pour Rachid** parce qu'il a écrit « SAVS » en haut de sa note : le tableau des trajets montre deux services. C'est le **tableau** qui commande l'imputation, pas l'en-tête.
- **Payer la directrice « parce que c'est la directrice »** : sans visa d'un membre du bureau, on ne paie pas. C'est la même règle que pour un chef de service qui viserait sa propre note (voir E17-05).
- **Rembourser le bar** « parce que c'est sur la facture de l'hôtel » : une facture n'est pas une preuve de dépense professionnelle. On rembourse la chambre, le petit-déjeuner et la taxe de séjour, pas la consommation personnelle.
- **Arrondis** : 286 × 0,636 = 181,896 → 181,90 € ; on arrondit chaque ligne au centime, comme le dit la règle interne. Un calcul arrondi au total peut différer d'un centime ; ce qui compte est d'appliquer la même règle à tous.

### Question 7 — Pourquoi pas un compte 467 et une OD, comme en E17-05 ?

En E17-05, l'hypothèse de travail était une association qui suit les frais dans un compte **467** par salarié, en OD : c'est une méthode qui existe. Ici, on applique la **règle réelle** de Trisomie 21 France : les notes de frais vont au **journal des achats**, sur un compte de tiers **SA** centralisé en **4248000** Salariés – NDF. Le principe est le même (une dette envers le salarié, créditée à la note, débitée au paiement, lettrée), seul le compte change. Réflexe senior : **en arrivant dans une structure, on applique sa procédure**, pas celle de son poste précédent.

## 5. Ce qu'un senior ferait en plus

**Bonnes pratiques**

- Tenir le **cumul annuel des kilomètres** par salarié : au-delà de 5 000 km dans l'année, le barème change de tranche (*valeurs à vérifier chaque année*).
- Rapprocher chaque mois les notes de frais du **relevé de la carte carburant** et du **carnet de bord** des véhicules de service : un salarié ne peut pas demander des kilomètres pour un jour où il avait un véhicule de l'association.
- Rédiger un **message court** à chaque salarié dont la note est réduite (ici : Thomas Girard et la directrice), avec le motif, avant le virement. Un remboursement inférieur sans explication crée des tensions inutiles.
- Proposer à la directrice une **note de frais en deux colonnes** pour les salariés qui travaillent pour plusieurs structures (SAVS / habitat inclusif, SESSAD / emploi accompagné).
- Pour les frais de la directrice et des membres du bureau, garder dans le dossier la **trace du visa** (signature, date) : c'est la première pièce que le commissaire aux comptes demande sur ce poste.
- Rembourser **régulièrement** (une campagne par mois) : les salariés avancent leur propre argent.

**Le raisonnement d'analyse**

- Le schéma « note au journal des achats, puis paiement en banque » sépare deux moments : celui où l'association **reconnaît** devoir l'argent (après contrôle et visa) et celui où elle **paie**. Entre les deux, le compte SA montre exactement ce qui reste dû à chacun.
- L'imputation par structure n'est pas un détail : les frais de déplacement sont souvent examinés ligne par ligne par les financeurs (Département pour le SAVS, financeurs de l'habitat inclusif). Une note mal répartie se voit dans les comptes rendus.

## 6. Références

- Document interne « Les journaux comptables chez Trisomie 21 France » : enregistrement d'une note de frais (compte SA crédité ; 6251 et 60624 débités) ; journal de banque (paiements avec les comptes SA).
- Document interne « La comptabilité chez Trisomie 21 France » : compte 4248 Salariés – NDF, compte de centralisation.
- Plan comptable T21 : 6251000, 6256000, 6256700, 6062400, 4248000.
- Barème kilométrique fiscal publié chaque année par l'administration fiscale ; limites d'exonération des allocations forfaitaires de repas fixées par l'URSSAF (*valeurs à vérifier chaque année*).
