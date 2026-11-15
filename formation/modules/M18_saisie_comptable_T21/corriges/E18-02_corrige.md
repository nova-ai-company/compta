# Corrigé E18-02 — Dix factures fournisseurs à contrôler et à saisir

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **CCA** | Charges constatées d'avance — ou compte courant d'associé. Deux sens selon le contexte : (1) clôture : charge payée en N mais qui concerne N+1 (compte 486) ; (2) financement : argent prêté par un associé à sa société (compte 455). |
    | **CGI** | Code général des impôts. Le code qui contient toutes les règles fiscales (TVA, IS, IR…). « art. 39 CGI » = article 39 de ce code. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **EPRD** | État des prévisions de recettes et de dépenses. Budget prévisionnel des gestionnaires sous CPOM. Il part de la ressource notifiée par le financeur (« budget par la recette »). Dépôt en général au 30 avril (à vérifier chaque année). |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **RIB** | Relevé d'identité bancaire. Document qui donne les coordonnées bancaires (IBAN, BIC) d'un compte. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **SIREN** | Numéro d'identification de l'entreprise (9 chiffres). Identifiant unique de chaque entreprise en France. Mention obligatoire sur les factures, y compris celui du client depuis la facturation électronique. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 486** | Charges constatées d'avance (CCA). Dépense payée cette année qui concerne l'année suivante (assurance, loyer d'avance). |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 2050000** | Concessions et droits similaires, brevets, licences (plan T21). Logiciel ou licence achetés (propriété durable). Un abonnement mensuel n'est pas une immobilisation. |
    | **Compte 2182000** | Matériel de transport (plan T21). Véhicule acheté (exemple du document T21 : véhicule acheté au garage Martin). |
    | **Compte 2183000** | Matériel de bureau et matériel informatique (plan T21). Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4860000** | Charges constatées d’avance (plan T21). Charge constatée d'avance : facturée en N mais concernant N+1 (ex. : assurance avril N – mars N+1). |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6062500** | Fournitures scolaires, éducatives et de loisirs (plan T21). Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. |
    | **Compte 6068000** | Autres achats non stockés de matières et fournitures (plan T21). Autres petits achats non stockés. |
    | **Compte 6155800** | Entretien et réparations des autres matériel et outillages (plan T21). Entretien et réparation des véhicules et du matériel. |
    | **Compte 6156100** | Maintenance informatique (plan T21). Maintenance informatique, abonnements logiciels. |
    | **Compte 6161000** | Assurance Multirisques (plan T21). Assurance multirisque des locaux. |
    | **Compte 6354000** | Droits d’enregistrement et de timbre (plan T21). Droits d'enregistrement et de timbre. |
    | **FOBUREAU26** | Compte fournisseur fournitures de bureau (dossier M18). Fournitures administratives (6062400). |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **FOGARAGEMARTIN** | Compte fournisseur Garage Martin (dossier M18). Garage de Valence : entretien et achat des véhicules. Regroupé dans 4010000. |
    | **FOINFORHONE** | Compte fournisseur informatique (dossier M18). Maintenance informatique (6156100) et matériel (2183000 si immobilisé). |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOMAAF** | Compte fournisseur assurances (dossier M18). Mutuelle d'assurance : multirisque, flotte automobile, responsabilité civile. |
    | **bon à payer** | Accord écrit de la direction pour payer. Sans bon à payer de la directrice, la facture ne part pas en paiement. |
    | **charges constatées d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **Extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-02](../exercices/E18-02_factures-fournisseurs-saisie.md)

!!! abstract "En clair"
    Neuf pièces sur dix se saisissent. La dixième (Info Rhône, n° INF-2026-0917) **ne se saisit pas** : c'est un doublon d'une facture déjà payée, mal adressée, fausse dans ses calculs et sans bon à payer. Pour les neuf autres, on saisit toujours le **TTC**, dans la **bonne structure**. Deux factures communes (EDF, assurance des locaux) sont saisies au siège et réparties entre les cinq structures. Trois achats deviennent des **immobilisations** : l'ordinateur de l'emploi accompagné, la licence du logiciel de planning et le Partner du SESSAD.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### La grille de contrôle d'un senior, avant toute saisie

| N° | Contrôle | Ce que l'on regarde |
|---|---|---|
| 1 | **Destinataire** | Nom exact « Association Cap Horizons 21 », adresse « 14 rue des Alpes 26000 Valence », SIREN client 999 210 021. Une facture au nom d'un salarié ou d'une autre entité n'est pas une pièce de l'association |
| 2 | **Mentions** | Numéro unique, date, identité et SIREN du fournisseur, n° de TVA, désignation précise, quantités, prix, période ou date de livraison, échéance, pénalités de retard, indemnité forfaitaire de 40 €. Mentions de la facturation électronique : SIREN du client, adresse de livraison si elle diffère, nature de l'opération |
| 3 | **Calculs** | Quantité × prix unitaire, total HT, TVA par taux, TTC. On refait le calcul, on ne fait pas confiance au total |
| 4 | **Doublon** | Le numéro de facture n'existe pas déjà dans le compte du tiers (et pas sous un autre tiers en double) |
| 5 | **Réalité** | Conforme au bon de commande, au devis, au bon de livraison signé, au contrat. Livré et en bon état |
| 6 | **Bon à payer** | Tampon ou visa de la directrice. Aucune facture saisie pour paiement sans bon à payer (règle de l'association) |
| 7 | **Imputation** | Quelle structure ? Quel compte ? Charge ou immobilisation ? Quelle période (une partie sur l'exercice suivant) ? Quel code analytique ? |

### Le résultat du contrôle, pièce par pièce (question 1)

| N° | Fournisseur | Conclusion | Commentaire |
|---|---|---|---|
| 1 | EDF | **À saisir** | Tout est conforme. Facture **commune** aux locaux de Valence : siège + IS selon les m² |
| 2 | Bureau Vallée 26 | **À saisir** | Calculs justes, bon de commande et bon de livraison du SAVS |
| 3 | Ludik Éducation | **À saisir**, puis avoir n° 9 | Un jeu retourné à la livraison : l'avoir n° 9 le corrige. On ne « corrige » pas la facture soi-même |
| 4 | Info Rhône Services | **À saisir** | Ordinateur 899,00 € TTC : **immobilisation** ; souris 24,90 € TTC : charge |
| 5 | Logiplanning | **À saisir**, nouveau tiers **FOLOGIPLAN** à créer | Licence perpétuelle : **immobilisation** 2050000. Maintenance : charge, dont 10 mois sur 2027 |
| 6 | Garage Martin (réparation) | **À saisir** | Entretien du véhicule du SAVS : charge |
| 7 | Garage Martin (véhicule) | **À saisir**, contrôles renforcés avant paiement | Achat de véhicule : **immobilisation** 2182000 |
| 8 | MAAF | **À saisir** | Facture **commune** (locaux) : siège + IS. Période à cheval sur 2027 |
| 9 | Ludik Éducation (avoir) | **À saisir** | Écriture « à l'envers » de la facture |
| 10 | Info Rhône Services | **En attente, ne pas saisir** | Doublon, nom et adresse faux, SIREN client absent, erreur de calcul, pas de bon à payer |

### Immobilisation ou charge ? (question 2)

| Bien | Montant TTC | Décision | Raison |
|---|---|---|---|
| Tablette sensorielle (n° 3) | 388,80 | Charge 6062500 | Bien durable, mais **sous le seuil** de 500 € TTC fixé par l'association |
| Ordinateur portable (n° 4) | 899,00 | **Immobilisation 2183000** | Bien durable, utilisé plusieurs années, plus de 500 € TTC |
| Souris (n° 4) | 24,90 | Charge 6068000 | Utilisable seule, faible valeur. Elle n'est pas un élément de l'ordinateur |
| Licence Logiplanning (n° 5) | 1 440,00 | **Immobilisation 2050000** | Droit d'utilisation **perpétuel** acheté : c'est un actif incorporel (document T21, classe 20) |
| Maintenance Logiplanning (n° 5) | 432,00 | Charge 6156100 | Service rendu mois après mois pendant 12 mois : ce n'est pas un bien |
| Réparation de la Clio (n° 6) | 494,28 | Charge 6155800 | Elle **maintient** le véhicule en état, sans prolonger sa durée de vie de façon notable ni l'améliorer |
| Peugeot Partner (n° 7) | 15 186,76 | **Immobilisation 2182000** | Bien durable. Le certificat d'immatriculation (286,76 €) est inclus dans le coût d'entrée : il est indispensable pour mettre le véhicule en circulation *(certaines associations le passent en charge, en 6354000 : suivez la procédure de l'association et restez constant)* |

> 💡 Réflexe senior : le seuil de 500 € s'apprécie **par bien** utilisable seul, pas par facture. Une facture de 1 200 € pour dix chaises à 120 € reste en charge ; une facture de 899 € pour un seul ordinateur est une immobilisation.

### Pourquoi saisir le TTC ? (question 4)

Une entreprise soumise à la TVA récupère la TVA payée à ses fournisseurs : pour elle, le vrai coût est le HT, et la TVA va dans un compte 445 « TVA déductible ». Les services de Cap Horizons 21 (SESSAD, SAVS, emploi accompagné) ne sont pas soumis à la TVA ; l'association **ne peut donc pas** la récupérer. Les 348,98 € de TVA de la facture EDF sont **définitivement payés** : ils font partie du coût de l'électricité. C'est pourquoi le plan comptable T21 ne contient **aucun compte 445**, et que la charge est de **2 093,87 €**.

## 2. Calculs (détaillés, chaque montant justifié)

**Recalcul des factures** : tous les totaux des pièces n° 1 à 9 sont justes. Exemples : Bureau Vallée 4 × 24,90 = 99,60 ; 20 × 2,95 = 59,00 ; 3 × 31,50 = 94,50 ; 6 × 8,40 = 50,40 ; total 303,50 HT ; TVA 60,70 ; TTC 364,20. Ludik : base 20 % = 69,80 + 89,00 + 324,00 + 12,50 = 495,30, TVA 99,06 ; base 5,5 % = 56,88, TVA 3,13 ; TTC = 495,30 + 99,06 + 56,88 + 3,13 = 654,37.

**Répartition EDF (2 093,87 € TTC, clé m²)**

| Structure | Clé | Calcul | Part |
|---|---|---|---|
| SIE | 15 % | 2 093,87 × 15 % | 314,08 |
| SES | 45 % | 2 093,87 × 45 % | 942,24 |
| SAV | 25 % | 2 093,87 × 25 % | 523,47 |
| EMP | 10 % | 2 093,87 × 10 % | 209,39 |
| ASS | 5 % | 2 093,87 × 5 % | 104,69 |
| **Total** | 100 % | | **2 093,87** |

**Répartition MAAF (2 883,50 €, clé m²)**

| Structure | Clé | Calcul arrondi | Part retenue |
|---|---|---|---|
| SES | 45 % | 1 297,575 | 1 297,58 |
| SAV | 25 % | 720,875 | 720,88 |
| EMP | 10 % | 288,35 | 288,35 |
| ASS | 5 % | 144,175 | 144,18 |
| SIE | 15 % | 432,525 → 432,53, **moins 0,02 d'écart d'arrondi** | 432,51 |
| **Total** | | | **2 883,50** |

Les arrondis au centime donnent 2 883,52 : on met l'écart (− 0,02) sur le siège, qui porte la facture. Règle simple, à appliquer toujours de la même façon.

**Part de 2027 (question 5)** — à **noter** pour la clôture, sans passer l'écriture aujourd'hui :

- Maintenance Logiplanning : 432,00 € pour 12 mois (01/11/2026 – 31/10/2027). 2026 = 2 mois ; 2027 = 10 mois. Part 2027 : 432,00 × 10/12 = **360,00 €** (SESSAD).
- Assurance MAAF : 2 883,50 € pour 12 mois (01/11/2026 – 31/10/2027). Part 2027 : 10/12 de la part de chaque structure.

| Structure | Charge de l'année | Part 2027 (10/12) |
|---|---|---|
| SIE | 432,51 | 360,43 |
| SES | 1 297,58 | 1 081,32 |
| SAV | 720,88 | 600,73 |
| EMP | 288,35 | 240,29 |
| ASS | 144,18 | 120,15 |
| **Total** | **2 883,50** | **2 402,92** |

Au 31/12/2026, ces montants seront passés en **charges constatées d'avance** (CCA) : compte **4860000** au débit, la charge au crédit, en OD, **dans chaque structure** pour sa part (la charge de chaque structure est déjà chez elle grâce à l'IS). Extourne au 01/01/2027.

## 3. Écritures comptables

*Comptes de banque et tiers : voir la fiche du dossier. Les montants sont TTC. Les lignes « miroir » sont générées automatiquement par EIG quand on renseigne le compte IS ; sinon, on les saisit en OD dans chaque structure.*

### Facture n° 1 — EDF, saisie au siège avec IS (02/11/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SIE | AC | 6061200 Énergie, électricité | | EDF – électricité Valence – 10284556712 – 09-10/2026 – part siège 15 % | 01-SIEGE | 314,08 | |
| SIE | AC | 1849100 Liaison SESSAD | | EDF – électricité Valence – 10284556712 – IS SESSAD 45 % | | 942,24 | |
| SIE | AC | 1849200 Liaison SAVS | | EDF – électricité Valence – 10284556712 – IS SAVS 25 % | | 523,47 | |
| SIE | AC | 1849300 Liaison Emploi | | EDF – électricité Valence – 10284556712 – IS Emploi 10 % | | 209,39 | |
| SIE | AC | 1849400 Liaison Association | | EDF – électricité Valence – 10284556712 – IS Asso 5 % | | 104,69 | |
| SIE | AC | 4010000 Fournisseurs | FOEDF | EDF – électricité Valence – 10284556712 – 09-10/2026 | | | 2 093,87 |
| SES | OD | 6061200 Énergie, électricité | | EDF 09-10/2026 – IS reçue du siège | 10-SESSAD | 942,24 | |
| SES | OD | 1840000 Liaison Siège | | EDF 09-10/2026 – IS reçue du siège | | | 942,24 |
| SAV | OD | 6061200 Énergie, électricité | | EDF 09-10/2026 – IS reçue du siège | 20-SAVS | 523,47 | |
| SAV | OD | 1840000 Liaison Siège | | EDF 09-10/2026 – IS reçue du siège | | | 523,47 |
| EMP | OD | 6061200 Énergie, électricité | | EDF 09-10/2026 – IS reçue du siège | 30-EMPLOI | 209,39 | |
| EMP | OD | 1840000 Liaison Siège | | EDF 09-10/2026 – IS reçue du siège | | | 209,39 |
| ASS | OD | 6061200 Énergie, électricité | | EDF 09-10/2026 – IS reçue du siège | 90-ASSO | 104,69 | |
| ASS | OD | 1840000 Liaison Siège | | EDF 09-10/2026 – IS reçue du siège | | | 104,69 |

*Code analytique de l'ASS : 90-ASSO, car la salle commune sert aux événements de l'association (hypothèse de la fiche).*

### Facture n° 2 — Bureau Vallée 26, SAVS (27/10/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SAV | AC | 6062400 Fournitures administratives | | Bureau Vallée – fournitures SAVS – BV26-F-118204 – 10/2026 | 20-SAVS | 364,20 | |
| SAV | AC | 4010000 Fournisseurs | FOBUREAU26 | Bureau Vallée – fournitures SAVS – BV26-F-118204 – 10/2026 | | | 364,20 |

### Facture n° 3 — Ludik Éducation, SESSAD (29/10/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 6062500 Fournitures scolaires, éducatives et de loisirs | | Ludik – matériel éducatif SESSAD – LE-2026-04417 – 10/2026 | 10-SESSAD | 654,37 | |
| SES | AC | 4010000 Fournisseurs | FOLUDIK | Ludik – matériel éducatif SESSAD – LE-2026-04417 – 10/2026 | | | 654,37 |

### Facture n° 4 — Info Rhône Services, emploi accompagné (05/11/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| EMP | AC | 2183000 Matériel de bureau et matériel informatique | | Info Rhône – PC portable n° série PF4K2Z8M – INF-2026-1102 | 30-EMPLOI | 899,00 | |
| EMP | AC | 6068000 Autres achats non stockés de matières et fournitures | | Info Rhône – souris sans fil – INF-2026-1102 | 30-EMPLOI | 24,90 | |
| EMP | AC | 4010000 Fournisseurs | FOINFORHONE | Info Rhône – PC portable et souris Emploi – INF-2026-1102 | | | 923,90 |

### Facture n° 5 — Logiplanning, SESSAD (02/11/2026) — créer d'abord le tiers FOLOGIPLAN

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 2050000 Concessions et droits similaires, brevets, licences | | Logiplanning – licence perpétuelle 5 postes – LP-26-00731 | 10-SESSAD | 1 440,00 | |
| SES | AC | 6156100 Maintenance informatique | | Logiplanning – maintenance 11/2026-10/2027 – LP-26-00731 | 10-SESSAD | 432,00 | |
| SES | AC | 4010000 Fournisseurs | FOLOGIPLAN | Logiplanning – licence et maintenance – LP-26-00731 | | | 1 872,00 |

### Facture n° 6 — Garage Martin, réparation du véhicule du SAVS (28/10/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SAV | AC | 6155800 Entretien et réparations des autres matériels et outillages | | Garage Martin – entretien Clio GE-482-KL – GM-2026-1877 | 20-SAVS | 494,28 | |
| SAV | AC | 4010000 Fournisseurs | FOGARAGEMARTIN | Garage Martin – entretien Clio GE-482-KL – GM-2026-1877 | | | 494,28 |

### Facture n° 7 — Garage Martin, achat du Peugeot Partner du SESSAD (30/10/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 2182000 Matériel de transport | | Garage Martin – Peugeot Partner GT-915-RB (véhicule 14 900,00 + carte grise 286,76) – GM-2026-1890 | 10-SESSAD | 15 186,76 | |
| SES | AC | 4010000 Fournisseurs | FOGARAGEMARTIN | Garage Martin – Peugeot Partner GT-915-RB – GM-2026-1890 | | | 15 186,76 |

### Facture n° 8 — MAAF, assurance multirisque des locaux, saisie au siège avec IS (20/10/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SIE | AC | 6161000 Assurance multirisques | | MAAF – multirisque locaux – MA-2026-558120 – 11/2026-10/2027 – part siège | 01-SIEGE | 432,51 | |
| SIE | AC | 1849100 Liaison SESSAD | | MAAF – multirisque locaux – MA-2026-558120 – IS SESSAD 45 % | | 1 297,58 | |
| SIE | AC | 1849200 Liaison SAVS | | MAAF – multirisque locaux – MA-2026-558120 – IS SAVS 25 % | | 720,88 | |
| SIE | AC | 1849300 Liaison Emploi | | MAAF – multirisque locaux – MA-2026-558120 – IS Emploi 10 % | | 288,35 | |
| SIE | AC | 1849400 Liaison Association | | MAAF – multirisque locaux – MA-2026-558120 – IS Asso 5 % | | 144,18 | |
| SIE | AC | 4010000 Fournisseurs | FOMAAF | MAAF – multirisque locaux – MA-2026-558120 – 11/2026-10/2027 | | | 2 883,50 |
| SES | OD | 6161000 Assurance multirisques | | MAAF 11/2026-10/2027 – IS reçue du siège | 10-SESSAD | 1 297,58 | |
| SES | OD | 1840000 Liaison Siège | | MAAF 11/2026-10/2027 – IS reçue du siège | | | 1 297,58 |
| SAV | OD | 6161000 Assurance multirisques | | MAAF 11/2026-10/2027 – IS reçue du siège | 20-SAVS | 720,88 | |
| SAV | OD | 1840000 Liaison Siège | | MAAF 11/2026-10/2027 – IS reçue du siège | | | 720,88 |
| EMP | OD | 6161000 Assurance multirisques | | MAAF 11/2026-10/2027 – IS reçue du siège | 30-EMPLOI | 288,35 | |
| EMP | OD | 1840000 Liaison Siège | | MAAF 11/2026-10/2027 – IS reçue du siège | | | 288,35 |
| ASS | OD | 6161000 Assurance multirisques | | MAAF 11/2026-10/2027 – IS reçue du siège | 90-ASSO | 144,18 | |
| ASS | OD | 1840000 Liaison Siège | | MAAF 11/2026-10/2027 – IS reçue du siège | | | 144,18 |

### Facture n° 9 — Avoir Ludik Éducation, SESSAD (09/11/2026)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 4010000 Fournisseurs | FOLUDIK | Ludik – avoir jeu endommagé – AV-2026-0087 sur LE-2026-04417 | | 41,88 | |
| SES | AC | 6062500 Fournitures scolaires, éducatives et de loisirs | | Ludik – avoir jeu endommagé – AV-2026-0087 sur LE-2026-04417 | 10-SESSAD | | 41,88 |

Après l'avoir, le compte FOLUDIK présente un solde créditeur de 654,37 − 41,88 = **612,49 €** : c'est le montant à virer le 20/11. Au paiement, on **lettre** ensemble la facture, l'avoir et le virement (654,37 = 41,88 + 612,49).

### Facture n° 10 — Info Rhône Services : aucune écriture

## 4. Points d'attention / pièges

**Facture n° 10 : les anomalies (question 6)**

1. **Doublon** : le numéro INF-2026-0917 a déjà été saisi le 18/09/2026 et **payé** le 15/10/2026 (lettrage A dans le compte FOINFORHONE). La payer reviendrait à payer deux fois la même prestation.
2. **Montant différent** de la facture d'origine (309,60 € au lieu de 342,00 €) : ce n'est donc même pas une simple copie. Soit c'est une réédition erronée, soit le fournisseur a réutilisé un numéro, ce qui est interdit (la numérotation doit être unique et continue).
3. **Erreur de calcul** : 3 × 95,00 = **285,00**, et non 258,00 (chiffres inversés).
4. **Destinataire faux** : « Cap Horizon » sans « s », « **41** rue des Alpes » au lieu de 14, **SIREN client absent**.
5. **Pas de bon à payer**.

Décision : **on ne saisit pas**, on classe la pièce dans une chemise « litiges / en attente » avec une note, et on écrit au fournisseur :

> Objet : votre facture n° INF-2026-0917 reçue le 12/11/2026
>
> Bonjour,
>
> Nous avons reçu par courrier une facture n° INF-2026-0917 datée du 15/09/2026, d'un montant de 309,60 € TTC. Or, une facture portant ce même numéro, de 342,00 € TTC, pour la maintenance du troisième trimestre 2026, a déjà été enregistrée et réglée par virement le 15/10/2026.
>
> Par ailleurs, ce document présente une erreur de calcul (3 × 95,00 € = 285,00 € HT et non 258,00 €) et une adresse erronée (14 rue des Alpes, et non 41 ; « Association Cap Horizons 21 », SIREN 999 210 021).
>
> Pouvez-vous nous confirmer qu'il s'agit d'un envoi par erreur, ou nous préciser à quelle prestation ce document correspond ? Nous ne procéderons à aucun règlement d'ici là.
>
> Bien cordialement,
> L'agent comptable – Association Cap Horizons 21

**Autres pièges**

- **Saisir le HT** parce que la facture l'affiche en gros : faux. Sans compte 445, la TVA « disparaîtrait » et l'écriture serait déséquilibrée, ou la charge sous-évaluée.
- **Facture n° 3** : ne pas saisir 654,37 − 41,88 directement « pour simplifier ». On saisit la facture **telle qu'elle est** et l'avoir **tel qu'il est** : deux pièces, deux écritures, un lettrage.
- **Facture n° 5** : tout passer en charge (« c'est du logiciel ») ou tout immobiliser. Le contrat sépare un **droit perpétuel** (actif) et un **service de 12 mois** (charge). Un abonnement en ligne sans licence (logiciel « en SaaS », payé tant qu'on l'utilise) resterait entièrement en charge.
- **Facture n° 6 contre n° 7** : même fournisseur, même compte de tiers, mais l'une est une charge (réparation), l'autre une immobilisation (achat). Le compte de charge ou d'immobilisation dépend de **la nature** de la dépense, pas du fournisseur.
- **Facture n° 8** : saisir 100 % de la prime au siège sans IS. Le SESSAD, le SAVS… occupent les locaux : leurs financeurs doivent porter leur part, sinon les comptes du siège sont gonflés et ceux des services sous-évalués.
- **Nouveau tiers** : chercher « LOGI », « PLANNING » dans la liste avant de créer FOLOGIPLAN, pour ne pas créer un doublon.

## 5. Ce qu'un senior ferait en plus

**Fiches à créer dans EIG IMMOS (question 7)**

| Bien | Structure | Compte | Valeur d'entrée TTC | Date de mise en service | Informations à saisir |
|---|---|---|---|---|---|
| Ordinateur portable | EMP | 2183000 | 899,00 | 06/11/2026 | N° de série PF4K2Z8M, fournisseur, n° de facture, durée d'amortissement selon la procédure (souvent 3 ans pour le matériel informatique), localisation, utilisateur |
| Licence Logiplanning Pro | SES | 2050000 | 1 440,00 | 03/11/2026 | 5 postes, n° de facture, durée d'utilisation prévue |
| Peugeot Partner | SES | 2182000 | 15 186,76 | 05/11/2026 | Immatriculation GT-915-RB, date de 1re mise en circulation, kilométrage, durée selon la procédure (véhicule d'occasion : durée d'utilisation restante) |

Les dotations aux amortissements seront ensuite calculées et déversées par EIG IMMOS dans le journal IM : **aucune** OD manuelle.

**Contrôles avant le virement du Partner (question 8)**

- L'achat est-il bien prévu au **plan d'investissement** du SESSAD validé par l'ARS (EPRD 2026) ? Un investissement non prévu peut entraîner des amortissements refusés dans l'ERRD.
- Le montant dépasse 1 500 € : virement **signé par la directrice et la trésorière** (Odile Marchand).
- Vérifier le **RIB** du Garage Martin avec celui déjà connu (ne jamais utiliser un RIB reçu par simple mail : risque de fraude au faux fournisseur).
- Vérifier la **trésorerie** du SESSAD au 20/11 (15 186,76 € d'un coup) et, si un financement spécifique existe (subvention d'investissement), la date de son versement.
- Classer avec la facture : le bon de commande signé, le certificat d'immatriculation, le procès-verbal de livraison. Ce sont les pièces que le commissaire aux comptes demandera.

**Bonnes pratiques générales**

- Saisir la pièce **avec son numéro** dans le libellé : c'est ce qui permet la recherche de doublons par le logiciel.
- Tenir une **liste de clôture** dès novembre (CCA Logiplanning et MAAF, factures EDF de novembre–décembre à provisionner, etc.) : on n'a plus rien à chercher le 31/12.
- Pour les factures communes, vérifier une fois par mois que **chaque** IS a bien son miroir dans la structure (le solde 1849100 chez le siège est l'opposé exact du 1840000 du SESSAD).

**Le raisonnement d'analyse**

- L'ordre des contrôles a une logique : on écarte d'abord ce qui n'est **pas une dette** de l'association (mauvais destinataire, doublon), puis ce qui est **faux** (calculs), puis ce qui n'est **pas autorisé** (bon à payer). On ne réfléchit au compte qu'ensuite.
- Le choix charge / immobilisation change le résultat de **chaque** structure, donc ce que le financeur accepte : une immobilisation coûte au budget par ses amortissements sur plusieurs années, une charge pèse en une fois. Le seuil de l'association doit être écrit dans une procédure et appliqué sans exception.

## 6. Références

- Documents internes Trisomie 21 France : « Les journaux comptables » (journal des achats, comptes FO, avoirs « à l'envers »), « La comptabilité chez T21 France » (classes 20 et 21, compte 486 pour les charges constatées d'avance, classe 18), plan comptable T21 (13/10/2025).
- PCG (règlement ANC n° 2014-03 modifié) : définition des actifs, coût d'acquisition des immobilisations, charges constatées d'avance.
- Code de commerce et CGI : mentions obligatoires des factures, pénalités de retard et indemnité forfaitaire pour frais de recouvrement de 40 €.
