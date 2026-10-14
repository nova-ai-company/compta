# Corrigé E05-08 — Prélèvements et dépenses personnelles : EURL à l'IR contre SARL à l'IS

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-08](../exercices/E05-08_prelevements-perso-ir-vs-is.md)

## 1. Analyse

### 1.1 Le principe commun
Une dépense n'est une **charge** de l'entreprise que si elle est engagée **dans l'intérêt de l'exploitation** (art. 39-1 CGI). Une dépense personnelle du dirigeant n'est **jamais** une charge, quelle que soit la forme de l'entreprise. Ce qui change selon la forme et le régime, c'est **où on l'enregistre** et **ce que cela déclenche**.

### 1.2 Style & Vous (EURL à l'IR)
- Le bénéfice de l'EURL est imposé **au nom de Nadia** dans la catégorie des BIC. Sa rémunération de gérante n'est pas déductible : elle fait partie de son bénéfice. Les sommes qu'elle prélève ne sont donc pas des charges : la pratique du dossier les enregistre en **108** (compte de l'exploitant), comme en entreprise individuelle. Une méthode plus rigoureuse, puisque l'EURL est une personne morale, consiste à décider une rémunération par décision de l'associée unique, à la comptabiliser en **644** puis à la réintégrer extra-comptablement : le résultat fiscal est identique. On suit ici la pratique du dossier (permanence des méthodes), en recommandant une décision formelle de l'associée unique.
- **Le 455 n'est pas le bon compte** pour des prélèvements réguliers : il ferait apparaître un compte courant **débiteur** de 25 200 € — interdit aussi dans une EURL dont l'associée unique est une personne physique (art. L. 223-21 C. com.).

| Ligne | Analyse | Traitement |
|---|---|---|
| Virements « Nadia perso » | Prélèvements / rémunération de la gérante | 108 (pratique du dossier) |
| PAS IR | Impôt **personnel** de Nadia sur l'ensemble de ses revenus | 108 — jamais en 635 |
| Cotisations SSI | Cotisations sociales obligatoires de la gérante : **déductibles** du BIC (art. 154 bis CGI) | 646 — correct |
| Madelin prévoyance | Déductible dans les limites de l'art. 154 bis CGI (plafond à vérifier) | 646 — correct, contrôle du plafond à la clôture |
| Courses Carrefour | Personnel | 108 |
| Airbnb Corse | Vacances personnelles | 108 |

### 1.3 Boulangerie Dupain (SARL à l'IS)
La SARL est un **contribuable distinct**. Toute dépense personnelle du gérant payée par la société est soit une **rémunération** (si elle est décidée et déclarée comme telle), soit une **créance** de la société sur lui (il doit rembourser), soit, à défaut, un **avantage occulte** taxé comme revenu distribué.

| Ligne | Analyse | Traitement |
|---|---|---|
| Rémunération de gérance (AG) | Rémunération décidée, déductible de l'IS, soumise aux cotisations TNS | 641 — correct |
| Retraits DAB sans justificatif | Prélèvement personnel | 455 Marc (débit) |
| Espèces prises dans la caisse | Prélèvement personnel (recettes bien déclarées via les Z, puis sorties) | 455 Marc (débit) |
| Assurance auto personnelle | Véhicule personnel, non utilisé pour l'activité | 455 Marc (débit) — pas une charge |
| Netflix | Personnel | 455 Marc (débit) |
| Scolarité du fils | Personnel | 455 Marc (débit) |

## 2. Calculs

### 2.1 Style & Vous

| Reclassement vers 108 | Montant |
|---|---|
| Virements Nadia (depuis 455) | 25 200,00 |
| PAS IR (depuis 635) | 3 690,00 |
| Courses (depuis 6063) | 186,40 |
| Airbnb (depuis 6256) | 1 240,00 |
| **Total 108 au 30/09/2026** | **30 316,40** |

**Impact sur le résultat** : les charges diminuent de 3 690,00 + 186,40 + 1 240,00 = **5 116,40 €** → le bénéfice BIC de Nadia augmente d'autant. Ce n'est donc pas « rien » :
- **IR** : 5 116,40 € de revenu supplémentaire, imposé à son taux marginal ;
- **cotisations SSI** : elles sont assises sur le bénéfice ; laisser 5 116,40 € de dépenses personnelles en charges revenait à **minorer l'assiette sociale** (de l'ordre de 40 % de cotisations sur ce montant, taux indicatif) — risque URSSAF en plus du risque fiscal ;
- **TVA** : si de la TVA avait été déduite sur les courses ou l'Airbnb, elle serait à reverser (ici, saisies TTC : pas d'impact).

### 2.2 Boulangerie Dupain — compte courant de Marc

| Mouvement | Débit | Crédit |
|---|---|---|
| Solde au 01/01/2026 | | 4 200,00 |
| Retraits DAB | 1 800,00 | |
| Espèces caisse | 2 400,00 | |
| Assurance auto personnelle | 1 128,00 | |
| Netflix | 161,91 | |
| Scolarité | 2 850,00 | |
| **Solde au 30/09/2026** | **4 139,91 débiteur** | |

Le compte courant de Marc est **débiteur de 4 139,91 €**. Effet sur le résultat de la SARL : charges réduites de 1 128,00 + 161,91 + 2 850,00 = **4 139,91 €** (IS supplémentaire au taux de 15 % : environ 621 €).

## 3. Écritures comptables

**Style & Vous :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 108 | Compte de l'exploitant (pratique du dossier) | Reclassement virements « Nadia perso » janv.-sept. | 25 200,00 |  |
| 30/09/2026 | OD | 455 | Associée — compte courant N. Belkacem | Reclassement virements « Nadia perso » |  | 25 200,00 |
| 30/09/2026 | OD | 108 | Compte de l'exploitant (pratique du dossier) | Prélèvement à la source IR personnel de N. Belkacem | 3 690,00 |  |
| 30/09/2026 | OD | 635 | Autres impôts, taxes et versements assimilés | Annulation PAS IR personnel |  | 3 690,00 |
| 30/09/2026 | OD | 108 | Compte de l'exploitant (pratique du dossier) | Courses Carrefour personnelles | 186,40 |  |
| 30/09/2026 | OD | 6063 | Fournitures d'entretien et de petit équipement | Annulation courses personnelles |  | 186,40 |
| 30/09/2026 | OD | 108 | Compte de l'exploitant (pratique du dossier) | Location vacances Airbnb personnelle | 1 240,00 |  |
| 30/09/2026 | OD | 6256 | Missions | Annulation location vacances personnelle |  | 1 240,00 |
| | | | | **Totaux** | **30 316,40** | **30 316,40** |

**Boulangerie Dupain :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 455 | Associé — compte courant M. Dupain | Assurance auto personnelle M. Dupain (contrat n° 7781-AP) | 1 128,00 |  |
| 30/09/2026 | OD | 616 | Primes d'assurance | Annulation assurance auto personnelle |  | 1 128,00 |
| 30/09/2026 | OD | 455 | Associé — compte courant M. Dupain | Abonnement Netflix personnel janv.-sept. | 161,91 |  |
| 30/09/2026 | OD | 6181 | Documentation générale | Annulation Netflix |  | 161,91 |
| 30/09/2026 | OD | 455 | Associé — compte courant M. Dupain | Frais de scolarité Institution Saint-Just (fils) | 2 850,00 |  |
| 30/09/2026 | OD | 6188 | Autres frais divers | Annulation frais de scolarité |  | 2 850,00 |
| | | | | **Totaux** | **4 139,91** | **4 139,91** |

On enregistre **la réalité** (une créance sur Marc) : il serait pire de laisser ces dépenses en charges pour « éviter » le compte débiteur.

**Régularisation recommandée — remboursement par Marc (exemple au 15/10/2026) :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | BQ | 512 | Banque | Remboursement par M. Dupain du compte courant débiteur | 4 139,91 |  |
| 15/10/2026 | BQ | 455 | Associé — compte courant M. Dupain | Remboursement compte courant débiteur |  | 4 139,91 |
| | | | | **Totaux** | **4 139,91** | **4 139,91** |

## 4. Points d'attention / pièges

### Pourquoi le compte débiteur est un problème en SARL
- **Code de commerce, art. L. 223-21** : il est interdit aux gérants et associés personnes physiques d'une SARL de contracter des emprunts auprès de la société, de se faire consentir un **découvert en compte courant** ou de faire cautionner leurs engagements personnels. Le contrat est nul.
- **Abus de biens sociaux** (art. L. 241-3, 4° C. com.) : usage des biens ou du crédit de la société, de mauvaise foi, contraire à l'intérêt social, à des fins personnelles. Payer la scolarité de son fils avec le compte de la société entre dans cette définition. Peines : jusqu'à 5 ans d'emprisonnement et 375 000 € d'amende. Julie Dupain (40 %) est associée : l'intérêt social n'est pas celui du seul Marc.
- **Fiscalement** : les sommes mises à la disposition des associés sont présumées **revenus distribués** (art. 111 a CGI) ; les dépenses personnelles laissées en charges seraient réintégrées au résultat de la société **et** imposées chez Marc comme distributions occultes (art. 109 et 111 c CGI), avec pénalité possible pour défaut de désignation des bénéficiaires (art. 1759 CGI).
- **Le solde créditeur d'ouverture ne « couvre » pas tout** : 4 200 € de crédit ont été consommés par les seuls prélèvements d'espèces ; au-delà, chaque euro est une avance interdite.

### Les solutions de régularisation (avant le 31/12/2026)

| Solution | Mécanisme | Coût pour Marc / la société | Avis |
|---|---|---|---|
| **1. Remboursement** par Marc | Virement de 4 139,91 € | Aucun coût fiscal ou social | **Recommandée** : simple, efface le débit |
| 2. Complément de **rémunération** | Décision d'AG (avec Julie), imputation au 455 | Cotisations TNS (de l'ordre de 40 % — indicatif) + IR pour Marc ; déductible de l'IS | Possible si Marc n'a pas la trésorerie ; à formaliser |
| 3. **Dividende** | Distribution votée en AG sur bénéfices distribuables, imputée au 455 | Gérant majoritaire de SARL : la fraction des dividendes > 10 % du capital + primes + comptes courants est soumise aux cotisations sociales ; ici le seuil est faible (≈ 2 000 €) → coût social élevé | Peu intéressant |
| 4. Ne rien faire | Compte débiteur au bilan | Infraction visible au bilan, risque ABS, revenus distribués | **Exclu** |

### Autres pièges
- Les **retraits d'espèces sans justificatif** sont l'angle mort de la Boulangerie (≈ 35 % d'encaissements en espèces) : un vérificateur rapprochera les recettes espèces, les remises en banque et les prélèvements du gérant.
- **Prélèvement à la source** : l'impôt personnel n'est jamais une charge, même s'il est prélevé sur le compte professionnel.
- **Style & Vous** : le 108 se solde à la clôture contre le résultat/la rémunération décidée ; un 455 débiteur ne doit pas apparaître non plus.

## 5. Tableau comparatif

| Question | Style & Vous — EURL à l'IR | Boulangerie Dupain — SARL à l'IS |
|---|---|---|
| Qui est imposé sur le bénéfice ? | Nadia (IR, BIC) | La société (IS), puis Marc sur ce qu'il perçoit |
| Rémunération de la gérante/du gérant | Non déductible (part du bénéfice) | Déductible de l'IS si décidée et non excessive |
| Prélèvements courants | 108 (pratique du dossier) ou 644 + réintégration | Uniquement la rémunération votée (641) ou dividendes votés |
| Dépense personnelle laissée en charge | Bénéfice BIC et assiette SSI minorés → rappel d'IR et de cotisations | IS éludé **et** revenu distribué occulte chez Marc (double imposition + pénalités) |
| Dépense personnelle payée par l'entreprise | 108 : neutre fiscalement si correctement classée | Créance sur Marc (455 débiteur interdit) → remboursement ou rémunération votée |
| Risque pénal | Faible si l'EURL n'est pas lésée au détriment de tiers (mais même interdiction légale du découvert en compte courant) | Abus de biens sociaux, d'autant qu'il y a une autre associée |

## 6. Ce qu'un senior ferait en plus

**Réponse à Nadia :**
> « Bonjour Nadia, vos 2 800 € mensuels ne sont pas une charge : ils sont en quelque sorte une avance sur votre bénéfice, c'est normal. En revanche, l'impôt sur le revenu, les courses et les vacances ne peuvent pas être des charges du salon : nous les avons reclassés. Cela augmente votre bénéfice de 5 116 €, donc votre impôt **et** vos cotisations sociales (qui sont calculées sur ce bénéfice). Pour l'avenir, le plus simple est de vous virer une somme fixe chaque mois et de payer toutes vos dépenses personnelles depuis votre compte personnel. Je vous propose aussi de formaliser votre rémunération par une décision d'associée unique. »

**Appel puis e-mail à Marc (rappeler après 14 h) :**
> « Bonjour Marc, suite à notre échange : votre compte courant n'a plus que 4 200 € disponibles et les dépenses personnelles le rendent **débiteur de 4 139,91 €**. En SARL, la loi interdit au gérant d'avoir un compte courant débiteur, et l'administration fiscale peut taxer ces sommes comme des revenus distribués. La solution la plus simple : un virement de votre compte personnel de 4 139,91 € avant le 31/12. À l'avenir, aucune dépense personnelle par la carte ou la caisse de la boulangerie, et plus aucun retrait d'espèces sans pièce : si vous avez besoin de plus, on augmente votre rémunération en AG avec Julie. »

**Dossier** : tracer l'alerte (date, interlocuteur, solution retenue) dans le dossier de travail ; c'est la preuve du devoir de conseil du cabinet. Si le compte restait débiteur à la clôture, Hélène Ferrand devrait apprécier les conséquences sur la mission (et, en présence d'un CAC dans un autre dossier, la révélation des faits délictueux relèverait de ce dernier).

## 7. Références
- Code de commerce, art. L. 223-21 (interdiction des emprunts et découverts en compte courant dans les SARL), art. L. 241-3 (abus de biens sociaux dans les SARL).
- CGI, art. 39-1 (charges déductibles), art. 8 (imposition de l’associé unique d’une EURL non soumise à l’IS), art. 154 bis (cotisations sociales et contrats Madelin), art. 109, 111 a et c (revenus distribués), art. 1759 (pénalité pour distributions occultes).
- CSS, art. L. 131-6 (assiette des cotisations des travailleurs indépendants, y compris fraction des dividendes > 10 % pour les gérants majoritaires de SARL).
- PCG : comptes 108, 455, 641, 644.
