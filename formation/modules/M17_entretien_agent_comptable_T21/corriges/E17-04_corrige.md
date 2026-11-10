# Corrigé E17-04 — Journal de paie, charges sociales par salarié et paiement des salaires

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E17-04](../exercices/E17-04_journal-paie-charges-sociales-paiement-salaires.md)

!!! abstract "En clair"
    Les totaux du journal de paie peuvent être **justes** alors qu'**une ligne** est fausse. C'est pour cela qu'on contrôle **salarié par salarié** : une cotisation divisée par le brut doit redonner le taux. Ici, Rachid Haddad a une cotisation URSSAF patronale calculée sur un brut erroné. On le signale **avant** l'envoi de la DSN, on comptabilise le journal **corrigé**, puis on ventile tout par service.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Le contrôle salarié par salarié

**La méthode.** Pour chaque salarié et chaque cotisation : **brut × taux**, arrondi au centime, puis comparaison avec le journal. Ensuite : brut − total salarial = net avant PAS ; net imposable × taux PAS = PAS ; net avant PAS − PAS − acompte = net à payer.

**Part salariale et net : tout est juste.** Exemple pour Thomas Girard :
- URSSAF : 2 712,40 × 16,80 % = 455,68 ✓ ; retraite : 2 712,40 × 4,01 % = 108,77 ✓ ; prévoyance : 2 712,40 × 0,80 % = 21,70 ✓ ; mutuelle 35,00 ✓.
- Total salarial : 455,68 + 108,77 + 21,70 + 35,00 = 621,15 ✓.
- Net avant PAS : 2 712,40 − 621,15 = 2 091,25 ✓ ; PAS : 2 203,53 × 4,1 % = 90,34 ✓ ; net : 2 091,25 − 90,34 = 2 000,91 ✓.

Le même calcul pour les cinq autres salariés retombe sur le journal (détail au § 2).

**Part patronale : une anomalie.**

| Salarié | URSSAF patronale dans le journal | Brut × 28,00 % | Écart |
|---|---|---|---|
| Thomas Girard | 759,47 | 2 712,40 × 28 % = 759,47 | 0,00 ✓ |
| Claire Dumas | 696,08 | 2 486,00 × 28 % = 696,08 | 0,00 ✓ |
| Inès Roche | 581,11 | 2 075,39 × 28 % = 581,11 | 0,00 ✓ |
| **Rachid Haddad** | **657,50** | 2 438,20 × 28 % = **682,70** | **− 25,20** ✗ |
| Julie Marchetti | 725,20 | 2 590,00 × 28 % = 725,20 | 0,00 ✓ |
| Malik Benoît | 547,51 | 1 955,40 × 28 % = 547,51 | 0,00 ✓ |

657,50 / 28 % = 2 348,21 : la cotisation a été calculée sur **2 348,20 €** au lieu de **2 438,20 €**. C'est une **inversion de chiffres** dans la base (48 / 84). Les autres cotisations de Rachid sont bien calculées sur 2 438,20 € : l'erreur ne touche que la ligne URSSAF patronale.

Conséquences :
- Le **net** de Rachid **n'est pas touché** (c'est une cotisation patronale) : son salaire a été payé juste le 28/10.
- Sans correction, la DSN déclarerait **25,20 € de moins** à l'URSSAF. Cela entraînerait une régularisation, voire une majoration.
- Les totaux corrigés : URSSAF patronale 3 966,87 + 25,20 = **3 992,07 €** ; total patronal 5 212,61 + 25,20 = **5 237,81 €**.

**Ce que l'on fait** : on **ne corrige pas soi-même** le journal. On écrit **tout de suite** au service paie, avant l'envoi de la DSN, avec le calcul. Le service paie corrige son paramétrage et renvoie un journal corrigé. On comptabilise ensuite les montants **corrigés**, qui seront ceux de la DSN.

**Deux « fausses anomalies »** à savoir expliquer :
- **Julie Marchetti n'a pas de mutuelle** : c'est normal. Elle a une **dispense valable** (demande écrite et justificatif reçus le 12/01/2026). Pas de part salariale, **pas de part patronale** non plus. À vérifier une fois par an : le justificatif doit rester valable.
- **Inès Roche a un taux PAS de 0,0 %** : c'est le taux **transmis par l'administration fiscale** (foyer non imposable, par exemple). Le service paie l'a reçu dans le **compte rendu** de la DSN. On ne le change pas. Si un salarié n'a **pas** de taux transmis, la paie applique un **taux non personnalisé** (grille), et non 0 %.

> 💡 Réflexe senior : le contrôle « cotisation ÷ brut = taux » prend dix minutes avec un tableur. C'est la meilleure façon de trouver une erreur de paramétrage **avant** la DSN, quand elle est encore facile à corriger.

### Question 2 — Le coût employeur par service

Les charges de personnel suivent **le service où travaille le salarié**. Rachid Haddad est partagé : 70 % de **chacune** de ses charges va au SAVS, 30 % à l'habitat inclusif (selon son planning, clé « temps passé » de la fiche de l'association).

| Service | Salariés | Brut | URSSAF patronale | Retraite patronale | Prévoyance + mutuelle patronales | **Coût employeur** |
|---|---|---|---|---|---|---|
| 01-SIEGE | Malik Benoît | 1 955,40 | 547,51 | 117,52 | 64,33 | **2 684,76** |
| 10-SESSAD | Thomas Girard, Claire Dumas | 5 198,40 | 1 455,55 | 312,43 | 147,98 | **7 114,36** |
| 20-SAVS | Inès Roche, Rachid Haddad (70 %) | 3 782,13 | 1 059,00 | 227,31 | 116,23 | **5 184,67** |
| 30-EMPLOI | Julie Marchetti | 2 590,00 | 725,20 | 155,66 | 38,85 | **3 509,71** |
| 40-HABITAT | Rachid Haddad (30 %) | 731,46 | 204,81 | 43,96 | 21,47 | **1 001,70** |
| **Total** | | **14 257,39** | **3 992,07** | **856,88** | **388,86** | **19 495,20** |

Contrôle : 14 257,39 + 5 237,81 = 19 495,20 ✓.

Après l'encaissement des IJSS de Claire Dumas (343,17 €), le coût net du SESSAD pour octobre sera de 7 114,36 − 343,17 = **6 771,19 €**.

### Question 5 — Les IJSS en subrogation

- Arrêt du 05/10 au 16/10 : **12 jours**. Les **3 premiers jours** sont des jours de **carence** (pas d'IJSS).
- IJSS versées : 12 − 3 = **9 jours** × 38,13 € = **343,17 €**.

**Pourquoi en diminution du compte 6411 ?** Avec la méthode retenue, le salaire de Claire a été **maintenu en entier** dans le brut (charge 6411). Quand la CPAM rembourse une partie de ce salaire, la charge réelle de l'association **baisse**. Depuis le PCG applicable aux exercices ouverts à compter du **01/01/2025** (règlement ANC n° 2022-06), les comptes de **transfert de charges (791) sont supprimés**. Le remboursement vient donc **au crédit du compte de charge** concerné, avec le **même code analytique** (10-SESSAD).

**Et si les IJSS ne sont pas arrivées au 31/12 ?** Il faut alors constater un **produit à recevoir** : débit 4387 Organismes sociaux – produits à recevoir, crédit 6411 (10-SESSAD). Sinon, la charge du SESSAD est surévaluée dans l'ERRD (état réalisé des recettes et des dépenses). L'écriture est ensuite soldée à l'encaissement : débit 512, crédit 4387.

> ⚠️ Erreur classique : suivre la méthode de l'ancienne comptable, « 512 au débit, 791 Transferts de charges au crédit ». Le compte 791 **n'existe plus** depuis 2025. Et un transfert de charges faisait apparaître une charge et un produit, au lieu d'une charge nette plus faible.

**À savoir :** dans la pratique, beaucoup de logiciels de paie **déduisent** les IJSS du brut le mois suivant. Ils ajoutent alors les IJSS nettes au net à payer. Dans ce cas, les IJSS en attente sont une **créance sur la CPAM** (compte 4387) passée dans l'écriture de paie (voir le module M15, exercice E15-07). Demandez toujours au service paie **quelle méthode** il applique : l'écriture comptable en dépend.

## 2. Calculs (détaillés, chaque montant justifié)

**Recalcul des cotisations salariales**

| Salarié | Brut | URSSAF 16,80 % | Retraite 4,01 % | Prévoyance 0,80 % | Mutuelle | Total salarial |
|---|---|---|---|---|---|---|
| Thomas Girard | 2 712,40 | 455,68 | 108,77 | 21,70 | 35,00 | 621,15 ✓ |
| Claire Dumas | 2 486,00 | 417,65 | 99,69 | 19,89 | 35,00 | 572,23 ✓ |
| Inès Roche | 2 075,39 | 348,67 | 83,22 | 16,60 | 35,00 | 483,49 ✓ |
| Rachid Haddad | 2 438,20 | 409,62 | 97,77 | 19,51 | 35,00 | 561,90 ✓ |
| Julie Marchetti | 2 590,00 | 435,12 | 103,86 | 20,72 | 0,00 (dispense) | 559,70 ✓ |
| Malik Benoît | 1 955,40 | 328,51 | 78,41 | 15,64 | 35,00 | 457,56 ✓ |
| **Total** | **14 257,39** | **2 395,25** | **571,72** | **114,06** | **175,00** | **3 256,03** |

**Recalcul des cotisations patronales (montants corrigés)**

| Salarié | URSSAF 28,00 % | Retraite 6,01 % | Prévoyance 1,50 % | Mutuelle | Total patronal |
|---|---|---|---|---|---|
| Thomas Girard | 759,47 | 163,02 | 40,69 | 35,00 | 998,18 ✓ |
| Claire Dumas | 696,08 | 149,41 | 37,29 | 35,00 | 917,78 ✓ |
| Inès Roche | 581,11 | 124,73 | 31,13 | 35,00 | 771,97 ✓ |
| Rachid Haddad | **682,70** | 146,54 | 36,57 | 35,00 | **900,81** (journal : 875,61) |
| Julie Marchetti | 725,20 | 155,66 | 38,85 | 0,00 | 919,71 ✓ |
| Malik Benoît | 547,51 | 117,52 | 29,33 | 35,00 | 729,36 ✓ |
| **Total corrigé** | **3 992,07** | **856,88** | **213,86** | **175,00** | **5 237,81** |

**Recalcul du PAS et du net**

| Salarié | Net avant PAS | Net imposable × taux | PAS | Acompte | Net à payer |
|---|---|---|---|---|---|
| Thomas Girard | 2 091,25 | 2 203,53 × 4,1 % | 90,34 | 0,00 | 2 000,91 ✓ |
| Claire Dumas | 1 913,77 | 2 019,60 × 2,3 % | 46,45 | 0,00 | 1 867,32 ✓ |
| Inès Roche | 1 591,90 | 1 686,03 × 0,0 % | 0,00 | 0,00 | 1 591,90 ✓ |
| Rachid Haddad | 1 876,30 | 1 980,77 × 3,6 % | 71,31 | 0,00 | 1 804,99 ✓ |
| Julie Marchetti | 2 030,30 | 2 104,10 × 5,2 % | 109,41 | 0,00 | 1 920,89 ✓ |
| Malik Benoît | 1 497,84 | 1 588,55 × 1,5 % | 23,83 | 400,00 | 1 074,01 ✓ |
| **Total** | **11 001,36** | | **341,34** | **400,00** | **10 260,02** |

**Ventilation de Rachid Haddad (70 % / 30 %)**

| Élément | Total | 20-SAVS (70 %) | 40-HABITAT (30 %, par différence) |
|---|---|---|---|
| Brut | 2 438,20 | 1 706,74 | 731,46 |
| URSSAF patronale | 682,70 | 477,89 | 204,81 |
| Retraite patronale | 146,54 | 102,58 | 43,96 |
| Prévoyance + mutuelle patronales | 36,57 + 35,00 = 71,57 | 50,10 | 21,47 |

Le second service est calculé **par différence** : la somme des deux parts redonne toujours exactement le total.

**Sommes dues aux organismes (prélevées le 16/11)**

| Organisme | Part salariale | Part patronale | Total |
|---|---|---|---|
| URSSAF (431) | 2 395,25 | 3 992,07 | **6 387,32** |
| AGIRC-ARRCO (437ARR) | 571,72 | 856,88 | **1 428,60** |
| Prévoyance + mutuelle (437PRV) | 114,06 + 175,00 = 289,06 | 213,86 + 175,00 = 388,86 | **677,92** |
| DGFiP – PAS (4421) | 341,34 | — | **341,34** |
| **Total prélevé** | | | **8 835,18** |

**Contrôle de l'écriture de paie** : 2 395,25 + 571,72 + 289,06 + 341,34 + 400,00 + 10 260,02 = **14 257,39** = brut ✓.

## 3. Écritures comptables

L'acompte du 15/10 (débit 425 / crédit 512 : 400,00 €) a déjà été passé (E17-03). Il n'est pas repris ici.

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 28/10/2026 | PA | 6411 | Salaires, appointements | Paie 10/2026 – brut | 01-SIEGE | 1 955,40 |  |
| 28/10/2026 | PA | 6411 | Salaires, appointements | Paie 10/2026 – brut | 10-SESSAD | 5 198,40 |  |
| 28/10/2026 | PA | 6411 | Salaires, appointements | Paie 10/2026 – brut | 20-SAVS | 3 782,13 |  |
| 28/10/2026 | PA | 6411 | Salaires, appointements | Paie 10/2026 – brut | 30-EMPLOI | 2 590,00 |  |
| 28/10/2026 | PA | 6411 | Salaires, appointements | Paie 10/2026 – brut | 40-HABITAT | 731,46 |  |
| 28/10/2026 | PA | 431 | Sécurité sociale | Paie 10/2026 – URSSAF salariale | — |  | 2 395,25 |
| 28/10/2026 | PA | 437ARR | Caisse de retraite AGIRC-ARRCO | Paie 10/2026 – retraite salariale | — |  | 571,72 |
| 28/10/2026 | PA | 437PRV | Organisme de prévoyance et mutuelle | Paie 10/2026 – prévoyance + mutuelle salariales | — |  | 289,06 |
| 28/10/2026 | PA | 4421 | Prélèvements à la source | Paie 10/2026 – PAS | — |  | 341,34 |
| 28/10/2026 | PA | 425 | Personnel – avances et acomptes | Paie 10/2026 – reprise acompte M. Benoît | — |  | 400,00 |
| 28/10/2026 | PA | 421 | Personnel – rémunérations dues | Paie 10/2026 – nets à payer | — |  | 10 260,02 |
| 28/10/2026 | PA | 6451 | Cotisations à l'URSSAF | Paie 10/2026 – URSSAF patronale | 01-SIEGE | 547,51 |  |
| 28/10/2026 | PA | 6451 | Cotisations à l'URSSAF | Paie 10/2026 – URSSAF patronale | 10-SESSAD | 1 455,55 |  |
| 28/10/2026 | PA | 6451 | Cotisations à l'URSSAF | Paie 10/2026 – URSSAF patronale | 20-SAVS | 1 059,00 |  |
| 28/10/2026 | PA | 6451 | Cotisations à l'URSSAF | Paie 10/2026 – URSSAF patronale | 30-EMPLOI | 725,20 |  |
| 28/10/2026 | PA | 6451 | Cotisations à l'URSSAF | Paie 10/2026 – URSSAF patronale | 40-HABITAT | 204,81 |  |
| 28/10/2026 | PA | 6453 | Cotisations aux caisses de retraite | Paie 10/2026 – retraite patronale | 01-SIEGE | 117,52 |  |
| 28/10/2026 | PA | 6453 | Cotisations aux caisses de retraite | Paie 10/2026 – retraite patronale | 10-SESSAD | 312,43 |  |
| 28/10/2026 | PA | 6453 | Cotisations aux caisses de retraite | Paie 10/2026 – retraite patronale | 20-SAVS | 227,31 |  |
| 28/10/2026 | PA | 6453 | Cotisations aux caisses de retraite | Paie 10/2026 – retraite patronale | 30-EMPLOI | 155,66 |  |
| 28/10/2026 | PA | 6453 | Cotisations aux caisses de retraite | Paie 10/2026 – retraite patronale | 40-HABITAT | 43,96 |  |
| 28/10/2026 | PA | 6452 | Cotisations aux mutuelles et à la prévoyance | Paie 10/2026 – prévoyance + mutuelle patronales | 01-SIEGE | 64,33 |  |
| 28/10/2026 | PA | 6452 | Cotisations aux mutuelles et à la prévoyance | Paie 10/2026 – prévoyance + mutuelle patronales | 10-SESSAD | 147,98 |  |
| 28/10/2026 | PA | 6452 | Cotisations aux mutuelles et à la prévoyance | Paie 10/2026 – prévoyance + mutuelle patronales | 20-SAVS | 116,23 |  |
| 28/10/2026 | PA | 6452 | Cotisations aux mutuelles et à la prévoyance | Paie 10/2026 – prévoyance + mutuelle patronales | 30-EMPLOI | 38,85 |  |
| 28/10/2026 | PA | 6452 | Cotisations aux mutuelles et à la prévoyance | Paie 10/2026 – prévoyance + mutuelle patronales | 40-HABITAT | 21,47 |  |
| 28/10/2026 | PA | 431 | Sécurité sociale | Paie 10/2026 – URSSAF patronale | — |  | 3 992,07 |
| 28/10/2026 | PA | 437ARR | Caisse de retraite AGIRC-ARRCO | Paie 10/2026 – retraite patronale | — |  | 856,88 |
| 28/10/2026 | PA | 437PRV | Organisme de prévoyance et mutuelle | Paie 10/2026 – prévoyance + mutuelle patronales | — |  | 388,86 |
| 28/10/2026 | BQ | 421 | Personnel – rémunérations dues | Virement salaires nets 10/2026 | — | 10 260,02 |  |
| 28/10/2026 | BQ | 512 | Banque | Virement salaires nets 10/2026 | — |  | 10 260,02 |
| 16/11/2026 | BQ | 431 | Sécurité sociale | DSN 10/2026 – URSSAF | — | 6 387,32 |  |
| 16/11/2026 | BQ | 437ARR | Caisse de retraite AGIRC-ARRCO | DSN 10/2026 – AGIRC-ARRCO | — | 1 428,60 |  |
| 16/11/2026 | BQ | 437PRV | Organisme de prévoyance et mutuelle | DSN 10/2026 – prévoyance et mutuelle | — | 677,92 |  |
| 16/11/2026 | BQ | 4421 | Prélèvements à la source | DSN 10/2026 – PAS reversé à la DGFiP | — | 341,34 |  |
| 16/11/2026 | BQ | 512 | Banque | DSN 10/2026 – prélèvements | — |  | 8 835,18 |
| 18/11/2026 | BQ | 512 | Banque | CPAM – IJSS subrogation C. Dumas (9 j × 38,13) | — | 343,17 |  |
| 18/11/2026 | BQ | 6411 | Salaires, appointements | IJSS C. Dumas – diminution des salaires | 10-SESSAD |  | 343,17 |
| | | | | **Totaux** | | **38 933,57** | **38 933,57** |

**Question 6 — Contrôle des comptes de tiers**

| Compte | Débits | Crédits | Solde |
|---|---|---|---|
| 421 | 10 260,02 (virement du 28/10) | 10 260,02 (paie) | 0,00 ✓ |
| 425 | 400,00 (acompte du 15/10, E17-03) | 400,00 (paie) | 0,00 ✓ |
| 431 | 6 387,32 (DSN) | 2 395,25 + 3 992,07 = 6 387,32 | 0,00 ✓ |
| 437ARR | 1 428,60 (DSN) | 571,72 + 856,88 = 1 428,60 | 0,00 ✓ |
| 437PRV | 677,92 (DSN) | 289,06 + 388,86 = 677,92 | 0,00 ✓ |
| 4421 | 341,34 (DSN) | 341,34 (paie) | 0,00 ✓ |

Solde du compte 6411 après les IJSS : 14 257,39 − 343,17 = **13 914,22 €** (débiteur).

## 4. Points d'attention / pièges

- **Saisir le journal tel quel** : on comptabiliserait 25,20 € de charges URSSAF en moins, et l'écart apparaîtrait le jour où l'URSSAF régularise.
- **Corriger soi-même la ligne fausse** sans prévenir le service paie : la comptabilité ne correspondrait plus à la DSN. Les deux doivent toujours dire la même chose.
- **Mettre toutes les charges sociales du salarié partagé dans un seul service** : le SAVS paierait l'animation de l'habitat inclusif, alors que l'habitat a son propre financement (aide à la vie partagée du Département). Les deux comptes rendus seraient faux.
- **Oublier de ventiler les charges patronales** : on ventile souvent le brut et on oublie le reste. Le coût d'un service, c'est **brut + charges patronales**.
- **Les IJSS en 791** : compte supprimé depuis 2025.
- **Les IJSS sans code analytique** : la baisse de charge doit aller au **même service** que le salaire maintenu (10-SESSAD). Sinon, le SESSAD garde une charge qu'il n'a pas eue.
- **Le PAS** : ce n'est pas une cotisation sociale, c'est l'impôt du salarié. L'association le collecte et le reverse à la DGFiP (direction générale des finances publiques) via la DSN. Ce n'est pas une charge de l'association.
- **Croire qu'une association ne paie que des charges sociales** : elle paie aussi la **taxe sur les salaires** (voir E17-02 et E17-06), calculée séparément par le cabinet.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail au service paie (le 02/11, avant la DSN) :**

> Objet : Journal de paie octobre — URSSAF patronale de Rachid Haddad
>
> Bonjour Hélène,
>
> En contrôlant le journal d'octobre, je trouve pour Rachid Haddad une URSSAF patronale de 657,50 €, soit 28 % de 2 348,20 €. Son brut est de 2 438,20 € : la cotisation devrait être de **682,70 €** (écart de 25,20 €). Les autres cotisations de Rachid sont bien calculées sur 2 438,20 €. Le net n'est pas touché.
>
> Pouvez-vous corriger avant l'envoi de la DSN et me renvoyer le journal corrigé ? Je comptabiliserai la version corrigée.
>
> Merci, bonne journée,
> [Prénom Nom], agent comptable

**Contrôles mensuels à présenter en entretien :**
1. Journal de paie = DSN = écritures comptables (même total par organisme).
2. Comptes 421, 425, 431, 437, 4421 **soldés** chaque mois.
3. Total du virement des salaires = total des nets du journal (et nombre de virements = nombre de salariés payés).
4. Suivi des IJSS attendues par salarié (date de l'arrêt, montant attendu, date de réception). Relance de la CPAM au-delà d'un mois.
5. Coût de la paie **par service** comparé au **budget** (EPRD pour le SESSAD, budget prévisionnel pour le SAVS, conventions pour les autres) : c'est la base du **suivi budgétaire** demandé par la directrice.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG, règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06 : suppression des comptes de transfert de charges (791, 796, 797) pour les exercices ouverts à compter du 01/01/2025.
- PCG : comptes 421, 425, 431, 437, 438, 4421, 641, 645 ; règlement ANC n° 2018-06 pour les associations.
- Code de la sécurité sociale : indemnités journalières, délai de carence et subrogation de l'employeur (*références à vérifier*).
- CGI : prélèvement à la source de l'impôt sur le revenu, collecté par l'employeur et reversé via la DSN.
- Fiche de l'association Cap Horizons 21 : § 3.5 (clé « temps passé » pour un salarié partagé entre deux services).
