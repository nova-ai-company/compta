# Corrigé E16-03 — Un salarié pour deux services : ventiler les salaires au temps passé

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **ERRD** | État réalisé des recettes et des dépenses. Le compte rendu de l'EPRD après la clôture : réalisé, écarts, proposition d'affectation du résultat. Dépôt en général au 30 avril N+1 (à vérifier). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **FIPHFP** | Fonds pour l'insertion des personnes handicapées dans la fonction publique. Finance l'emploi des personnes handicapées dans le secteur public (l'équivalent de l'AGEFIPH pour le public). |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **Compte 645** | Charges de sécurité sociale et de prévoyance. Cotisations patronales. |
    | **Compte 6411** | Salaires, appointements. Salaire brut de base. Les IJSS reçues en subrogation viennent en diminution. |
    | **comptabilité analytique** | Ranger les charges et produits par service ou projet. La comptabilité générale dit « quoi » (du carburant), l'analytique dit « pour qui » (pour le SAVS). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **groupe II** | Dépenses de personnel. Salaires, charges sociales, intérim, formation. |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **section analytique** | Une « case » de la comptabilité analytique. Un service ou un projet (ex. : 20-SAVS) dans lequel on range les charges et les produits qui le concernent. |
    | **subventions affectées** | Subvention donnée pour un projet précis. Elle ne peut servir qu'à ce projet ; ce qui n'est pas dépensé va en fonds dédiés ou est remboursé. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-03](../exercices/E16-03_ventiler-salaires-temps-passe.md)

!!! abstract "En clair"
    - **Salaire chargé** = salaire brut + charges patronales. C'est ce que le salarié **coûte** à l'association.
    - **Pourcentage de temps** = heures passées pour un service ÷ total des heures de la feuille de temps.
    - **Part du service** = salaire chargé × pourcentage.
    - L'écriture ne change **pas** les comptes 6411 et 645 : elle déplace seulement le coût d'une **section analytique** à une autre (OD analytique de reclassement).

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Pourquoi le temps passé, et pas « le budget » ?

Les salaires représentent la plus grosse partie des charges d'un service médico-social (souvent 70 à 80 %). Si la psychologue reste à 100 % sur le SESSAD alors qu'elle passe 40 % de son temps au SAVS :
- le SESSAD présente des charges **trop élevées** à l'ARS (agence régionale de santé) dans son ERRD (état réalisé des recettes et des dépenses) ;
- le SAVS présente des charges **trop faibles** au Département dans son compte administratif ;
- et si un jour le SAVS est en déficit, on ne pourra pas prouver qu'il manquait des moyens.

La seule clé acceptée pour un salarié partagé, c'est le **temps réellement passé**, prouvé par une **feuille de temps signée**. Le budget dit ce qu'on **prévoyait** ; la feuille de temps dit ce qui **s'est passé**.

### Le cas d'Inès Moulin : pourquoi on ne « bascule » pas

Inès Moulin a **réellement** travaillé pour le projet Pairs de janvier à mai (les feuilles d'émargement des 9 séances le montrent). Le problème n'est pas la réalité du travail, c'est la **preuve** exigée par la convention.

Mettre ces cinq mois sur l'emploi accompagné reviendrait à déclarer à l'ARS, à l'AGEFIPH et au FIPHFP qu'Inès a travaillé pour eux alors que c'est faux. C'est une **fausse déclaration** dans un compte rendu financier : le financeur peut demander le **remboursement**, et la confiance est perdue pour les conventions suivantes. La comptabilité analytique doit refléter la **réalité**, pas l'endroit où il reste du budget.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 1 — Salaire chargé mensuel (taux de 42 %, *valeur à vérifier chaque année*)

| Salarié | Brut | Charges patronales (brut × 42 %) | Salaire chargé |
|---|---|---|---|
| Claire Vidal | 3 250,00 € | 1 365,00 € | **4 615,00 €** |
| Julien Pereira | 1 920,00 € | 806,40 € | **2 726,40 €** |
| Inès Moulin | 2 450,00 € | 1 029,00 € | **3 479,00 €** |

### Question 2 — Ventilation d'octobre 2026

**Pourcentages de temps :**
- Claire Vidal : SESSAD 92,40 / 154,00 = **60 %** ; SAVS 61,60 / 154,00 = **40 %**.
- Julien Pereira : SESSAD 61,60 / 123,20 = **50 %** ; SAVS 36,96 / 123,20 = **30 %** ; Emploi 24,64 / 123,20 = **20 %**.
- Inès Moulin : Emploi 123,20 / 154,00 = **80 %** ; Pairs 30,80 / 154,00 = **20 %** (= les 0,2 ETP prévus au budget du projet).

**Ventilation :**

| Salarié | Section | % | Brut (6411) | Charges (645) | Chargé |
|---|---|---|---|---|---|
| Claire Vidal | 10-SESSAD | 60 % | 1 950,00 | 819,00 | 2 769,00 |
| Claire Vidal | 20-SAVS | 40 % | 1 300,00 | 546,00 | 1 846,00 |
| Julien Pereira | 10-SESSAD | 50 % | 960,00 | 403,20 | 1 363,20 |
| Julien Pereira | 20-SAVS | 30 % | 576,00 | 241,92 | 817,92 |
| Julien Pereira | 30-EMPLOI | 20 % | 384,00 | 161,28 | 545,28 |
| Inès Moulin | 30-EMPLOI | 80 % | 1 960,00 | 823,20 | 2 783,20 |
| Inès Moulin | 50-PAIRS | 20 % | 490,00 | 205,80 | 695,80 |
| **Total** | | | **7 620,00** | **3 200,40** | **10 820,40** |

Contrôle : 4 615,00 + 2 726,40 + 3 479,00 = **10 820,40 €** ✓.

**Ce qu'il faut déplacer** (la paie a tout mis sur la section du contrat) :
- de 10-SESSAD vers 20-SAVS : 1 300,00 + 546,00 (C. Vidal) et 576,00 + 241,92 (J. Pereira) ;
- de 10-SESSAD vers 30-EMPLOI : 384,00 + 161,28 (J. Pereira) ;
- de 30-EMPLOI vers 50-PAIRS : 490,00 + 205,80 (I. Moulin).

### Question 4 — Régularisation de janvier à septembre (Claire Vidal et Julien Pereira)

**Claire Vidal** — 9 mois : brut 9 × 3 250,00 = 29 250,00 € ; charges 29 250,00 × 42 % = 12 285,00 € ; chargé 41 535,00 €.
Temps : SESSAD 806 / 1 240 = **65 %** ; SAVS 434 / 1 240 = **35 %**.

| Section | Brut | Charges | Chargé |
|---|---|---|---|
| 10-SESSAD (65 %) | 19 012,50 | 7 985,25 | 26 997,75 |
| 20-SAVS (35 %) | 10 237,50 | 4 299,75 | 14 537,25 |

**Julien Pereira** — 9 mois : brut 9 × 1 920,00 = 17 280,00 € ; charges 17 280,00 × 42 % = 7 257,60 € ; chargé 24 537,60 €.
Temps : SESSAD 520 / 1 000 = **52 %** ; SAVS 300 / 1 000 = **30 %** ; Emploi 180 / 1 000 = **18 %**.

| Section | Brut | Charges | Chargé |
|---|---|---|---|
| 10-SESSAD (52 %) | 8 985,60 | 3 773,95 | 12 759,55 |
| 20-SAVS (30 %) | 5 184,00 | 2 177,28 | 7 361,28 |
| 30-EMPLOI (18 %) | 3 110,40 | 1 306,37 | 4 416,77 |

*(Charges Emploi : 7 257,60 × 18 % = 1 306,368 → 1 306,37 € ; charges SESSAD = 7 257,60 − 2 177,28 − 1 306,37 = 3 773,95 €.)*

Remarquez : la psychologue était à **65 %** SESSAD de janvier à septembre, mais à **60 %** en octobre. C'est normal (vacances scolaires, nouveaux enfants…) et c'est précisément pourquoi on ventile **chaque mois** sur les feuilles réelles, et pas avec un pourcentage fixe.

**Effet total sur 10 mois (janvier à octobre)** :

| Section | Effet |
|---|---|
| 10-SESSAD | − 29 524,50 € (charges qui n'étaient pas les siennes) |
| 20-SAVS | + 24 562,45 € (14 537,25 + 1 846,00 + 7 361,28 + 817,92) |
| 30-EMPLOI | + 4 962,05 € (4 416,77 + 545,28) |

Contrôle : 24 562,45 + 4 962,05 = 29 524,50 ✓. Sans ce travail, l'ERRD du SESSAD aurait été surévalué de près de 30 000 €, et le compte administratif du SAVS sous-évalué d'autant.

### Question 5 — Le montant contesté par la Fondation Lumen

Janvier à mai = 5 mois × 20 % × 3 479,00 € = 5 × 695,80 € = **3 479,00 €** (dont brut 5 × 490,00 = 2 450,00 € et charges 5 × 205,80 = 1 029,00 €).
*(Coïncidence : cela fait exactement un mois de salaire chargé, puisque 5 × 20 % = 100 %.)*

## 3. Écritures comptables

### Question 3 — OD analytique de reclassement d'octobre

| Date | Journal | Compte | Intitulé du compte | Libellé | Section | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6411 | Salaires | Reclassement 10/2026 C. Vidal 40 % SAVS | 20-SAVS | 1 300,00 | |
| 31/10/2026 | OD | 6411 | Salaires | Reclassement 10/2026 C. Vidal 40 % SAVS | 10-SESSAD | | 1 300,00 |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reclassement 10/2026 C. Vidal 40 % SAVS | 20-SAVS | 546,00 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reclassement 10/2026 C. Vidal 40 % SAVS | 10-SESSAD | | 546,00 |
| 31/10/2026 | OD | 6411 | Salaires | Reclassement 10/2026 J. Pereira 30 % SAVS | 20-SAVS | 576,00 | |
| 31/10/2026 | OD | 6411 | Salaires | Reclassement 10/2026 J. Pereira 20 % Emploi | 30-EMPLOI | 384,00 | |
| 31/10/2026 | OD | 6411 | Salaires | Reclassement 10/2026 J. Pereira | 10-SESSAD | | 960,00 |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reclassement 10/2026 J. Pereira 30 % SAVS | 20-SAVS | 241,92 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reclassement 10/2026 J. Pereira 20 % Emploi | 30-EMPLOI | 161,28 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reclassement 10/2026 J. Pereira | 10-SESSAD | | 403,20 |
| 31/10/2026 | OD | 6411 | Salaires | Reclassement 10/2026 I. Moulin 20 % Pairs (feuille de temps signée) | 50-PAIRS | 490,00 | |
| 31/10/2026 | OD | 6411 | Salaires | Reclassement 10/2026 I. Moulin 20 % Pairs | 30-EMPLOI | | 490,00 |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reclassement 10/2026 I. Moulin 20 % Pairs (feuille de temps signée) | 50-PAIRS | 205,80 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reclassement 10/2026 I. Moulin 20 % Pairs | 30-EMPLOI | | 205,80 |
| | | | | **Totaux** | | **3 905,00** | **3 905,00** |

### Question 4 — OD analytique de régularisation janvier à septembre

| Date | Journal | Compte | Intitulé du compte | Libellé | Section | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6411 | Salaires | Régul. 01–09/2026 C. Vidal 35 % SAVS (feuilles de temps) | 20-SAVS | 10 237,50 | |
| 31/10/2026 | OD | 6411 | Salaires | Régul. 01–09/2026 C. Vidal | 10-SESSAD | | 10 237,50 |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Régul. 01–09/2026 C. Vidal 35 % SAVS | 20-SAVS | 4 299,75 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Régul. 01–09/2026 C. Vidal | 10-SESSAD | | 4 299,75 |
| 31/10/2026 | OD | 6411 | Salaires | Régul. 01–09/2026 J. Pereira 30 % SAVS | 20-SAVS | 5 184,00 | |
| 31/10/2026 | OD | 6411 | Salaires | Régul. 01–09/2026 J. Pereira 18 % Emploi | 30-EMPLOI | 3 110,40 | |
| 31/10/2026 | OD | 6411 | Salaires | Régul. 01–09/2026 J. Pereira | 10-SESSAD | | 8 294,40 |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Régul. 01–09/2026 J. Pereira 30 % SAVS | 20-SAVS | 2 177,28 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Régul. 01–09/2026 J. Pereira 18 % Emploi | 30-EMPLOI | 1 306,37 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Régul. 01–09/2026 J. Pereira | 10-SESSAD | | 3 483,65 |
| | | | | **Totaux** | | **26 315,30** | **26 315,30** |

Contrôles : 5 184,00 + 3 110,40 = 8 294,40 ✓ ; 2 177,28 + 1 306,37 = 3 483,65 ✓.

**Pourquoi ces sens ?** Le service qui **reçoit** une charge est **débité** (sa charge augmente) ; le service qui la **cède** est **crédité** (sa charge diminue). Les comptes 6411 et 645 sont débités et crédités du même montant : le total des salaires de l'association ne change pas d'un centime.

**Pas d'écriture pour Inès Moulin (janvier à mai)** : le travail a bien été fait pour Pairs, l'imputation analytique sur 50-PAIRS est donc **juste**. Ce qui change, c'est le **compte rendu** à la Fondation (dépenses éligibles), pas la comptabilité.

## 4. Points d'attention / pièges

### Réponse à Sophie Laurent

« Je comprends, mais on ne peut pas : Inès a travaillé pour Pairs, pas pour l'emploi accompagné. Si on met ces heures sur la convention emploi, on déclare à l'ARS, à l'AGEFIPH et au FIPHFP un travail qui n'a pas été fait pour eux. En cas de contrôle, c'est un remboursement, et c'est notre crédibilité pour les prochains appels à projets. Je vous propose plutôt d'essayer de justifier ces heures auprès de la Fondation. »

### Ce que l'on propose à la directrice

1. **Constituer un dossier de preuves** pour janvier à mai : extraits de l'agenda, les 9 feuilles d'émargement des séances animées par Inès, les comptes rendus des séances, et une **attestation** signée par la directrice et la cheffe de service récapitulant les heures mois par mois.
2. **Le présenter honnêtement** à la Fondation comme un **état reconstitué** (daté du jour où il est établi), en demandant s'il peut être accepté à titre exceptionnel.
3. **Si la Fondation refuse** : les 3 479,00 € restent sur 50-PAIRS en comptabilité (c'est la réalité), mais ils sont **retirés des dépenses éligibles** du compte rendu. Ils seront financés par les **ressources propres** de l'association (vie associative, réserves). La directrice et la trésorière doivent le savoir **avant** la clôture.

> ⚠️ Erreur classique : fabriquer aujourd'hui des « feuilles de temps » de janvier à mai et les dater de l'époque. C'est un **faux document**. Un état reconstitué doit dire qu'il est reconstitué.

### Autres pièges

- **Ventiler seulement le brut** et oublier les charges patronales (645) : la section qui reçoit le salarié paraît moins chère qu'elle ne l'est.
- **Utiliser le pourcentage du budget** (0,2 ETP « prévu ») au lieu du temps réel : c'est exactement ce que la Fondation a refusé.
- **Oublier la régularisation** : corriger seulement octobre laisse 9 mois faux dans l'ERRD et le compte administratif.
- **Arrondis** : calculez la dernière section par **différence** (total − autres parts) pour que la somme tombe juste.

## 5. Ce qu'un senior ferait en plus

### Question 6 — Demande au service paie

« Bonjour, à partir de novembre, pouvez-vous paramétrer une **ventilation analytique mensuelle** dans le logiciel de paie pour trois salariés : Claire Vidal (SESSAD / SAVS), Julien Pereira (SESSAD / SAVS / Emploi), Inès Moulin (Emploi / Pairs) ? Je vous enverrai les pourcentages de chaque mois **avec les variables de paie**, à partir des feuilles de temps signées. L'OD de paie arrivera ainsi déjà ventilée, et je n'aurai plus d'OD de reclassement à passer. Merci ! »

### Et aussi

- **Ajouter la feuille de temps à la liste des variables mensuelles** : pas de feuille signée, pas d'imputation au projet. Prévenir les chefs de service de la date limite (par exemple le 20 du mois).
- **Relire toutes les conventions** de financement (emploi accompagné, habitat, Pairs) pour lister les **justificatifs exigés** : feuilles de temps, émargements, factures acquittées… et les demander **dès le premier mois**, pas au moment du contrôle.
- **Vérifier la cohérence avec les ETP** de la fiche : 0,6 + 0,4 pour la psychologue, 0,2 ETP sur Pairs pour Inès Moulin. Un écart durable entre le temps réel et le budget doit être signalé : il faudra peut-être revoir le budget de 2027.
- **Mettre à jour les ventilations des provisions** à la clôture (congés payés, taxe sur les salaires) avec les **mêmes** pourcentages : elles suivent le salaire.

## 6. Références

- Plan comptable des ESSMS et cadre budgétaire du Code de l'action sociale et des familles : charges de personnel en groupe II, affectation des charges à chaque établissement ou service — *textes à vérifier dans leur version en vigueur*.
- PCG : comptes 6411 (salaires), 645 (charges de sécurité sociale et de prévoyance).
- Règlement ANC n° 2018-06 : subventions affectées et fonds dédiés (une dépense non éligible ne peut pas consommer la subvention).
- Convention de financement de la Fondation Lumen (fictive) : clause de justification des frais de personnel. *En pratique, lisez toujours la convention : ce sont ses clauses qui fixent les justificatifs exigés.*
