# Corrigé E16-08 — La balance analytique ne tombe pas juste : retrouver et corriger les erreurs d'imputation

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **99-ATTENTE** | Section d'attente. Charges dont on ne connaît pas encore le service. Elle doit être vide à la clôture. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IK** | Indemnités kilométriques. Remboursement des kilomètres faits avec sa voiture personnelle pour le travail, selon un barème (prix par km). Compte 6251. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **ODA** | Journal des opérations diverses analytiques. Journal où l'on saisit les reclassements entre services (sections analytiques) sans changer les comptes généraux. |
    | **QP** | Quote-part. La part d'un total qui revient à un service (ex. : QP de frais de siège = la part du coût du siège payée par le SESSAD). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **Compte 613** | Locations. Loyers (sous-comptes 6132 immobilier, 6135 mobilier et véhicules). |
    | **Compte 641** | Rémunérations du personnel. Salaires bruts. |
    | **Compte 645** | Charges de sécurité sociale et de prévoyance. Cotisations patronales. |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6063** | Fournitures d'entretien et de petit équipement. Petit matériel (moins de 500 € environ), produits d'entretien. |
    | **Compte 6226** | Honoraires. Expert-comptable, commissaire aux comptes, avocat. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **OD analytiques** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **section d'attente** | Section analytique provisoire. Pour les charges dont on ne connaît pas encore le service. Elle doit être vide à la clôture. |
    | **sections analytiques** | Une « case » de la comptabilité analytique. Un service ou un projet (ex. : 20-SAVS) dans lequel on range les charges et les produits qui le concernent. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-08](../exercices/E16-08_balance-analytique-erreurs-imputation.md)

*Rappel : association, personnes, fournisseurs et chiffres fictifs.*

!!! abstract "En clair"
    1. On commence **toujours** par comparer, compte par compte, le total analytique au grand livre. Ici, deux comptes ne tombent pas juste : le **loyer** (+ 7 750 €, ventilé deux fois) et les **charges sociales** (+ 180 €, chiffres inversés à la saisie).
    2. On vide ensuite la **section d'attente** (2 210 €).
    3. Enfin, on contrôle la **vraisemblance** service par service avec les pièces : c'est là qu'on trouve les erreurs invisibles dans les totaux (salaire au mauvais service, frais de siège passés deux fois…).
    4. Après correction : total analytique = **136 640,00 €** = grand livre.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Étape 1 — Rapprochement compte par compte (question 1)

| Compte | Total analytique | Grand livre | Écart | Ce que l'écart suggère |
|---|---|---|---|---|
| 6061 | 3 480,00 | 3 480,00 | 0,00 | — |
| 6063 | 2 150,00 | 2 150,00 | 0,00 | — |
| 613 | 15 500,00 | 7 750,00 | **+ 7 750,00** | L'écart est **exactement** le montant du loyer : il a été ventilé **deux fois** |
| 6226 | 1 800,00 | 1 800,00 | 0,00 | — (mais tout est en attente) |
| 6251 | 2 860,00 | 2 860,00 | 0,00 | — (mais 410 € en attente) |
| 641 | 82 400,00 | 82 400,00 | 0,00 | — |
| 645 | 36 380,00 | 36 200,00 | **+ 180,00** | 180 / 9 = 20 : un écart **divisible par 9** signale souvent une **inversion de deux chiffres** à la saisie (4 640 au lieu de 4 460) |
| Frais de siège | 0,00 | 0,00 | 0,00 | — (mais le total à zéro ne prouve rien : voir étape 3) |
| **Total** | **144 570,00** | **136 640,00** | **+ 7 930,00** | = 7 750 + 180 |

> 💡 Réflexe senior : la règle du 9. Quand deux chiffres sont inversés (46 ↔ 64), l'écart est toujours un multiple de 9. Ici 4 640 − 4 460 = 180 = 9 × 20. Cherchez dans la ventilation un montant où deux chiffres voisins diffèrent de 2 (6 − 4 = 2 → 2 × 90 = 180).

### Étape 2 — La section d'attente

99-ATTENTE contient 2 210 € : les honoraires du cabinet (1 800 €) et l'état de frais du job coach (410 €). Une section d'attente est un **outil de saisie**, pas un service : elle doit être vide avant toute édition pour la direction ou un financeur. Sinon, 2 210 € de charges ne sont supportées par **aucun** service et tous les coûts sont sous-évalués.

### Étape 3 — Vraisemblance service par service

Deux types d'erreurs ne se voient **pas** dans les totaux :

- **Le montant est dans le mauvais service** (le total du compte est juste) : la facture Ludiclasse, la carte carburant n° 5, le salaire de Mme Vidal, l'état de frais de Mme Fabre.
- **Le montant est passé deux fois dans une OD qui s'équilibre** : l'OD de frais de siège crédite le siège et débite les services pour le même montant ; passée deux fois, la ligne reste à zéro au total. Mais le SESSAD supporte 25 406,50 € de frais de siège **en un mois**, soit la moitié de son budget annuel (50 813 €) : c'est invraisemblable.

> ⚠️ Erreur classique : s'arrêter quand « le total tombe juste ». Pour un financeur, la seule chose qui compte, c'est **son** service. Un salaire de 3 140 € chargé imputé au SESSAD au lieu du SAVS fausse deux comptes administratifs, même si le total de l'association est parfait.

### Les 9 anomalies (question 2)

| N° | Anomalie | Pièce qui le prouve | Effet sur les services (avant correction) |
|---|---|---|---|
| 1 | Facture Ludiclasse (matériel pédagogique, 640,00 €) codée 20-SAVS | (a) bon de commande signé par le chef de service SESSAD | SESSAD sous-évalué de 640 € ; SAVS surévalué de 640 € |
| 2 | Honoraires du cabinet (1 800,00 €) en section d'attente | (h) | Aucun service ne les supporte ; à répartir selon le forfait |
| 3 | IK du job coach de l'emploi accompagné (410,00 €) en section d'attente | (g) | Emploi accompagné sous-évalué de 410 € |
| 4 | Loyer ventilé deux fois : 100 % au siège **et** répartition aux m² | (f) | Siège surévalué de 7 750 € ; total analytique > grand livre |
| 5 | Carte carburant n° 5 (260,00 €) codée 40-HABITAT, qui n'a pas de véhicule | (b) | Habitat surévalué de 260 € ; SAVS sous-évalué de 260 € |
| 6 | Salaire de Clara Vidal (2 180,00 € + 960,00 €) imputé au SESSAD au lieu du SAVS (mutation du 01/09 non paramétrée en paie) | (c) et (d) | SESSAD surévalué de 3 140 € ; SAVS sous-évalué de 3 140 € |
| 7 | OD de frais de siège du T3 passée deux fois (OD-0931 et OD-0937) | (e) | Chaque service supporte le double ; le siège est crédité deux fois |
| 8 | Ventilation de 645 de l'emploi accompagné saisie 4 640,00 au lieu de 4 460,00 | (c) | Emploi accompagné surévalué de 180 € ; total 645 > grand livre |
| 9 | État de frais de Mme Fabre (185,00 €) codé 50-PAIRS au lieu de 90-ASSO | (g) | Pairs surévalué de 185 € (charge présentée à tort au financeur) ; vie associative sous-évaluée |

Le 9e cas, l'état de frais de **Mme Fabre**, mérite une explication : elle participe aussi au projet Pairs, mais le stand du forum relève de la **vie associative** (sensibilisation). On impute selon **l'objet de la dépense**, pas selon la personne.

## 2. Calculs (détaillés, chaque montant justifié)

**Honoraires à répartir (forfait)** : Siège 1 800 × 10 % = 180,00 ; SESSAD × 40 % = 720,00 ; SAVS × 25 % = 450,00 ; Emploi × 15 % = 270,00 ; Habitat × 5 % = 90,00 ; Pairs × 5 % = 90,00 ; total 1 800,00 ✓.

**Loyer aux m² (contrôle de la répartition déjà passée)** : 7 750 / 590 m² = 13,1356 €/m² ; Siège 90 m² → 1 182,20 ; SESSAD 280 m² → 3 677,97 ; SAVS 160 m² → 2 101,69 ; Emploi 60 m² → 788,14 ; total 7 750,00 ✓. La répartition est juste : c'est l'imputation **initiale** de 7 750 € au siège qui est en trop.

**Frais de siège T3** : SESSAD 50 813 / 4 = 12 703,25 ✓ ; SAVS 27 560 / 4 = 6 890,00 ✓ ; Pairs 2 239,20 / 4 = 559,80 ✓. Une seule OD suffit : 24 329,05 €.

**Mme Vidal** : 2 180,00 + 960,00 = 3 140,00 € à transférer du SESSAD au SAVS.

## 3. Écritures comptables (OD analytiques de correction, question 3)

Ces écritures ne touchent **que** l'analytique (les comptes généraux ne bougent pas). Convention : **débit = on ajoute la charge à la section**, **crédit = on la retire**.

**A. Déplacements entre sections (l'OD s'équilibre)**

| Date | Journal | Compte | Section | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | ODA | 6063 | 10-SESSAD | Ludiclasse LC-26-0918 – réimputation au SESSAD | 640,00 | |
| 30/09/2026 | ODA | 6063 | 20-SAVS | Ludiclasse LC-26-0918 – réimputation au SESSAD | | 640,00 |
| 30/09/2026 | ODA | 6226 | 01-SIEGE | Honoraires cabinet 09/2026 – forfait 10 % | 180,00 | |
| 30/09/2026 | ODA | 6226 | 10-SESSAD | Honoraires cabinet 09/2026 – forfait 40 % | 720,00 | |
| 30/09/2026 | ODA | 6226 | 20-SAVS | Honoraires cabinet 09/2026 – forfait 25 % | 450,00 | |
| 30/09/2026 | ODA | 6226 | 30-EMPLOI | Honoraires cabinet 09/2026 – forfait 15 % | 270,00 | |
| 30/09/2026 | ODA | 6226 | 40-HABITAT | Honoraires cabinet 09/2026 – forfait 5 % | 90,00 | |
| 30/09/2026 | ODA | 6226 | 50-PAIRS | Honoraires cabinet 09/2026 – forfait 5 % | 90,00 | |
| 30/09/2026 | ODA | 6226 | 99-ATTENTE | Honoraires cabinet 09/2026 – sortie de l'attente | | 1 800,00 |
| 30/09/2026 | ODA | 6251 | 30-EMPLOI | IK L. Moreno 09/2026 – job coach | 410,00 | |
| 30/09/2026 | ODA | 6251 | 99-ATTENTE | IK L. Moreno 09/2026 – sortie de l'attente | | 410,00 |
| 30/09/2026 | ODA | 6061 | 20-SAVS | Carte carburant n° 5 – véhicule SAVS | 260,00 | |
| 30/09/2026 | ODA | 6061 | 40-HABITAT | Carte carburant n° 5 – véhicule SAVS | | 260,00 |
| 30/09/2026 | ODA | 641 | 20-SAVS | C. Vidal 09/2026 – mutation au SAVS au 01/09 | 2 180,00 | |
| 30/09/2026 | ODA | 641 | 10-SESSAD | C. Vidal 09/2026 – mutation au SAVS au 01/09 | | 2 180,00 |
| 30/09/2026 | ODA | 645 | 20-SAVS | C. Vidal 09/2026 – charges patronales | 960,00 | |
| 30/09/2026 | ODA | 645 | 10-SESSAD | C. Vidal 09/2026 – charges patronales | | 960,00 |
| 30/09/2026 | ODA | QP siège | 01-SIEGE | Annulation OD-2026-0937 (doublon frais de siège T3) | 24 329,05 | |
| 30/09/2026 | ODA | QP siège | 10-SESSAD | Annulation OD-2026-0937 (doublon frais de siège T3) | | 12 703,25 |
| 30/09/2026 | ODA | QP siège | 20-SAVS | Annulation OD-2026-0937 (doublon frais de siège T3) | | 6 890,00 |
| 30/09/2026 | ODA | QP siège | 30-EMPLOI | Annulation OD-2026-0937 (doublon frais de siège T3) | | 3 228,00 |
| 30/09/2026 | ODA | QP siège | 40-HABITAT | Annulation OD-2026-0937 (doublon frais de siège T3) | | 948,00 |
| 30/09/2026 | ODA | QP siège | 50-PAIRS | Annulation OD-2026-0937 (doublon frais de siège T3) | | 559,80 |
| 30/09/2026 | ODA | 6251 | 90-ASSO | IK Mme Fabre – stand forum des associations | 185,00 | |
| 30/09/2026 | ODA | 6251 | 50-PAIRS | IK Mme Fabre – stand forum des associations | | 185,00 |
| | | | | **Totaux** | **30 764,05** | **30 764,05** |

*ODA = journal des OD analytiques (nom à adapter au logiciel). « QP siège » = ligne analytique de quote-part de frais de siège.*

**B. Suppressions de lignes analytiques en trop (le total analytique diminue)**

| Compte | Section | Ligne analytique saisie | Ligne correcte | Correction | Pourquoi |
|---|---|---|---|---|---|
| 613 | 01-SIEGE | 8 932,20 | 1 182,20 | − 7 750,00 | Supprimer l'imputation initiale de 100 % au siège (la répartition aux m² la remplace) |
| 645 | 30-EMPLOI | 4 640,00 | 4 460,00 | − 180,00 | Corriger la transposition de chiffres (récapitulatif de paie) |
| | | | **Total** | **− 7 930,00** | = écart avec le grand livre ✓ |

Dans la plupart des logiciels, on ne « passe » pas ces suppressions par une OD : on **modifie la ventilation** de l'écriture d'origine (facture du bailleur, OD de paie). Si la période est clôturée, on passe une ligne analytique de correction négative, avec un libellé qui renvoie à la pièce.

### C. Balance analytique corrigée (question 4)

| Compte | 01-SIEGE | 10-SESSAD | 20-SAVS | 30-EMPLOI | 40-HABITAT | 50-PAIRS | 90-ASSO | 99-ATTENTE | **Total analytique** | Grand livre | Écart |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 6061 Carburant | — | 1 720,00 | 1 040,00 | 720,00 | — | — | — | — | **3 480,00** | 3 480,00 | 0,00 |
| 6063 Fournitures et petit matériel | 310,00 | 1 140,00 | 420,00 | 120,00 | 160,00 | — | — | — | **2 150,00** | 2 150,00 | 0,00 |
| 613 Locations (loyer de Valence) | 1 182,20 | 3 677,97 | 2 101,69 | 788,14 | — | — | — | — | **7 750,00** | 7 750,00 | 0,00 |
| 6226 Honoraires | 180,00 | 720,00 | 450,00 | 270,00 | 90,00 | 90,00 | — | — | **1 800,00** | 1 800,00 | 0,00 |
| 6251 Voyages et déplacements (IK) | — | 1 175,00 | 690,00 | 810,00 | — | — | 185,00 | — | **2 860,00** | 2 860,00 | 0,00 |
| 641 Rémunérations du personnel | 7 300,00 | 40 100,00 | 21 600,00 | 10 150,00 | 2 450,00 | 800,00 | — | — | **82 400,00** | 82 400,00 | 0,00 |
| 645 Charges de sécurité sociale | 3 200,00 | 17 650,00 | 9 480,00 | 4 460,00 | 1 060,00 | 350,00 | — | — | **36 200,00** | 36 200,00 | 0,00 |
| Quote-part frais de siège (OD interne) | − 24 329,05 | 12 703,25 | 6 890,00 | 3 228,00 | 948,00 | 559,80 | — | — | **0,00** | 0,00 | 0,00 |
| **Total** | **− 12 156,85** | **78 886,22** | **42 671,69** | **20 546,14** | **4 708,00** | **1 799,80** | **185,00** | — | **136 640,00** | **136 640,00** | **0,00** |

Contrôle : total analytique **136 640,00 €** = grand livre **136 640,00 €** ✓ ; section 99-ATTENTE à zéro ✓ ; ligne de frais de siège à zéro au total ✓.

Effet des corrections par service :

| Section | Avant | Après | Variation |
|---|---|---|---|
| 01-SIEGE | − 28 915,90 | − 12 156,85 | + 16 759,05 |
| 10-SESSAD | 93 369,47 | 78 886,22 | − 14 483,25 |
| 20-SAVS | 46 351,69 | 42 671,69 | − 3 680,00 |
| 30-EMPLOI | 23 274,14 | 20 546,14 | − 2 728,00 |
| 40-HABITAT | 5 826,00 | 4 708,00 | − 1 118,00 |
| 50-PAIRS | 2 454,60 | 1 799,80 | − 654,80 |
| 90-ASSO | 0,00 | 185,00 | + 185,00 |
| 99-ATTENTE | 2 210,00 | 0,00 | − 2 210,00 |
| **Total** | **144 570,00** | **136 640,00** | **− 7 930,00** |

### D. Question 5 — Pourquoi le siège reste négatif en septembre ?

Ce n'est **pas** une anomalie. L'OD de frais de siège est **trimestrielle** : elle refacture en septembre trois mois de frais de siège (juillet, août, septembre), alors que la balance de septembre ne contient que les charges du siège de **septembre**. Le contrôle pertinent se fait sur le **trimestre** (balance analytique de juillet à septembre) ou sur l'année. Sur une balance mensuelle, un siège négatif le mois de l'OD trimestrielle est normal ; un siège **deux fois** plus négatif que d'habitude (− 28 915,90 € avant correction) est un signal d'alerte.

## 4. Points d'attention / pièges

- **Corriger au hasard** pour faire tomber le total : on risque de créer de nouvelles erreurs. Méthode : compte par compte → section d'attente → vraisemblance par service.
- **Un total juste ne prouve rien** : 7 des 9 anomalies ne changent pas le total analytique (seuls le loyer ventilé deux fois et la transposition le modifient).
- **Imputer selon la personne** et non selon l'objet de la dépense (Mme Fabre) : c'est l'objet qui compte.
- **Mutation de salarié** : la paie suit le contrat, mais le paramétrage analytique n'est pas toujours mis à jour. À chaque entrée, sortie, mutation ou temps partagé : mise à jour du paramétrage **le mois même**.
- **Répartition « en plus » au lieu de « à la place »** : une OD de répartition doit **retirer** la charge de la section d'origine (crédit) quand elle la ventile ailleurs.
- **Ressaisie manuelle** d'une ventilation : source d'erreurs de frappe. Préférez l'import du fichier analytique de la paie.

## 5. Ce qu'un senior ferait en plus

**Cinq contrôles mensuels (question 6)** :

1. **Rapprochement analytique / générale par compte** : écart = 0 pour chaque compte de charges et de produits (un tableau Excel avec une colonne « Écart » et une mise en forme rouge si ≠ 0).
2. **Section d'attente à zéro** avant toute édition.
3. **Revue de vraisemblance** : carburant uniquement sur les sections qui ont des véhicules ; frais de siège = budget / 4 une fois par trimestre ; masse salariale de chaque service comparée au mois précédent (variation > 5 % à expliquer).
4. **Rapprochement paie / analytique** : récapitulatif analytique de paie = ventilation de l'OD de paie ; liste des mouvements de personnel du mois transmise au service paie.
5. **Journal des OD analytiques relu** (pas de doublon de numéro, de montant ou de date) et validé par la cheffe de mission ou la directrice.

Et aussi : rendre le **code analytique obligatoire** à la saisie (blocage dans le logiciel) ; documenter les clés de répartition dans une **procédure** datée (le CAC la demandera) ; garder une **piste d'audit** de chaque OD analytique (pièce, auteur, validation).

**Mail à Hélène Ferrand** :

```
Objet : Balance analytique septembre — 9 anomalies corrigées

Bonjour Hélène,
Écart initial analytique / générale : + 7 930 € (loyer ventilé deux fois
7 750 € ; transposition 4 640 / 4 460 sur le 645 Emploi : 180 €).
Section d'attente vidée (honoraires 1 800 € au forfait ; IK job coach 410 €).
Réimputations : Ludiclasse 640 € SAVS → SESSAD ; carte carburant n° 5
260 € Habitat → SAVS ; C. Vidal 3 140 € SESSAD → SAVS (mutation du 01/09,
paramétrage paie à corriger dès octobre) ; IK Mme Fabre 185 € Pairs → Asso ;
doublon OD frais de siège T3 annulé (24 329,05 €).
Balance corrigée = grand livre = 136 640,00 €. La liste des OD est jointe pour
relecture avant validation.
```

## 6. Références

- Règlement ANC n° 2018-06 et plan comptable des ESSMS : obligation de présenter des comptes **par établissement / service** pour chaque financeur.
- Code de l'action sociale et des familles (dispositions budgétaires et comptables des ESSMS) : chaque service autorisé a son propre budget et son propre compte de résultat — *textes à consulter dans leur version en vigueur*.
- Fiche de l'association Cap Horizons 21 : sections analytiques, clés de répartition (m², km, ETP, temps passé, forfait).
