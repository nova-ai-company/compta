# Corrigé E18-01 — Quel journal, quelle structure ? 20 opérations à aiguiller

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **AN** | À-nouveaux — ou avantage en nature (paie). Deux sens : (1) journal des à-nouveaux, qui reprend les soldes du bilan au début de l'exercice ; (2) en paie, avantage en nature (voiture, logement…). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CB** | Carte bancaire. Paiement par carte. Les encaissements CB arrivent en banque nets de commission. |
    | **DAB** | Distributeur automatique de billets. Retrait d'espèces : à justifier (alimentation de la caisse ou prélèvement de l'exploitant). |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PA** | Plateforme agréée — ou, dans le M18, journal de paie. Opérateur agréé par l'État (anciennement « PDP ») qui transmet les factures électroniques entre entreprises et envoie les données à l'administration. Dans le module M18, PA est le code du journal des salaires, alimenté automatiquement par EIG RH. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **VT** | Journal des ventes. Journal où l'on enregistre les factures clients (et les Z de caisse). |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 754** | Dons manuels (ou collectes). Dons des particuliers (numéro selon la nomenclature ANC 2018-06). |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 2183000** | Matériel de bureau et matériel informatique (plan T21). Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. |
    | **Compte 2818300** | Amort Matériel de bureau et matériel informatique (plan T21). Amortissements cumulés du matériel informatique. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4110000** | Clients (comptes de tiers CL…) (plan T21). Centralisation des clients. On saisit dans les comptes CL… |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 5300000** | Caisse (plan T21). Caisse (espèces). Le solde doit être égal au comptage physique. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6068000** | Autres achats non stockés de matières et fournitures (plan T21). Autres petits achats non stockés. |
    | **Compte 6152100** | Maintenance et contrôle obligatoire immobilier (plan T21). Contrôles obligatoires des locaux (extincteurs, électricité, ascenseur). |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 (plan T21). Remboursements de la prévoyance pour les arrêts longs : au crédit, en banque. Ancien compte 6492000. |
    | **Compte 6811200** | Dot Amorts Immobilisations corporelles (plan T21). Amortissement de l'année des biens corporels. |
    | **Compte 7060004** | Prestations de FORMATION (plan T21). Prestations de formation vendues (Fédération). |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7410002** | Subvention Fondation de France (plan T21). Subvention de la Fondation de France. |
    | **Compte 7541200** | Dons Autres projets (plan T21). Dons pour d'autres projets. |
    | **FOBUREAU26** | Compte fournisseur fournitures de bureau (dossier M18). Fournitures administratives (6062400). |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **FOGARAGEMARTIN** | Compte fournisseur Garage Martin (dossier M18). Garage de Valence : entretien et achat des véhicules. Regroupé dans 4010000. |
    | **FOINFORHONE** | Compte fournisseur informatique (dossier M18). Maintenance informatique (6156100) et matériel (2183000 si immobilisé). |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **Extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-01](../exercices/E18-01_quel-journal-quelle-structure.md)

!!! abstract "En clair"
    Trois règles suffisent à aiguiller presque tout. **1.** Une **facture** (ou une note de frais) va au journal des **achats** (AC). **2.** Un mouvement lu sur le **relevé bancaire** sans facture à saisir (paiement, dotation, IJSS, frais, don) va au journal de **banque** de la structure. **3.** Ce qui vient d'un autre logiciel (paie, amortissements, ventes de la Fédération) arrive **tout seul** : on n'y touche pas à la main. Tout le reste (clôture, corrections, répartitions) va en **OD** (opérations diverses).

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Pour chaque pièce, un senior se pose cinq questions, **dans cet ordre** :

1. **Quelle est la pièce ?** Une facture ou une note de frais (on crée une dette), un relevé bancaire (l'argent a bougé), une demande de régularisation (clôture, correction) ?
2. **Le journal est-il automatique ?** Paie (**PA**, EIG RH), immobilisations (**IM**, EIG IMMOS), ventes (**VT**, EIG Gestion commerciale, Fédération seulement), à-nouveaux (**ANP / AN**). Si oui : **on ne saisit rien** ; on corrige à la source, dans l'outil EIG, puis on relance le déversement (le transfert automatique des écritures vers la comptabilité).
3. **Quelle structure ?** Celle qui a **consommé** ou **reçu**. Si la facture est commune (locaux, téléphone, expert-comptable), elle est saisie **au siège** et répartie par **IS** (inter-structure : la part de chaque structure lui est renvoyée par les comptes de liaison 18).
4. **Quel compte, quel tiers ?** Une dette envers quelqu'un se saisit **toujours** sur son compte de tiers (FO, LI, SA), jamais directement sur le compte de centralisation (4010000, 4011000, 4248000, 4110000).
5. **Quel sens ?** Facture : charge au **débit**, tiers au **crédit**. Avoir : l'inverse. Dans un journal de banque, vous ne tapez que la **contrepartie** : au débit pour une dépense, au crédit pour une recette ; le logiciel ajoute seul la ligne 512 en sens inverse.

## 2. Les réponses ligne par ligne

*Abréviations : D = débit, C = crédit. « Auto » = ligne ajoutée par le logiciel dans un journal de banque ou de caisse.*

| N° | Journal | Manuel / automatique | Structure | Compte général et tiers | Sens de la ligne saisie | Pourquoi |
|---|---|---|---|---|---|---|
| 1 | AC | Manuel, avec contrepartie | **SIE**, avec IS vers SES, SAV, EMP, ASS | 6061200 Énergie, électricité (part du siège) + 1849100 à 1849400 (parts des structures) ; tiers **FOEDF** sur 4010000 | 6061200 et 18xx D ; FOEDF C 2 093,87 | Facture commune : saisie au siège, répartie selon la clé des m² (15 / 45 / 25 / 10 / 5 %) |
| 2 | AC | Manuel | **SES** | 6251000 Voyages et déplacements (km) + 6062400 Fournitures administratives ; tiers **SADURAND** sur 4248000 | 6251000 D 181,90 et 6062400 D 23,70 ; SADURAND C 205,60 | Une note de frais se saisit au journal des **achats**, comme une facture (document T21) |
| 3 | BQSAV | Manuel, contrepartie auto | **SAV** | **6419000** Remboursements sur rémunérations – IJSS | 6419000 **C** 612,48 ; auto 5123000 D | Les IJSS sont une « charge négative » : elles diminuent les charges de personnel. Pas de compte de produit |
| 4 | BQSES | Manuel, contrepartie auto | **SES** | **7312130** Dotation ESSMS (2° du I de l'art. L. 312-1 du CASF) | 7312130 C 118 450,00 ; auto 5122000 D | Dotation de l'autorité de tarification : classe 731, jamais en subvention 74 |
| 5 | BQSAV | Manuel, contrepartie auto | **SAV** | **6062100** Combustibles et carburants, sans tiers | 6062100 D 58,40 ; auto 5123000 C | Dépense CB avec ticket mais **sans facture** : directement en charge, pas de compte FO |
| 6 | PA | **Automatique** (EIG RH) | EMP | Aucun : **interdit** de saisir | — | Le journal de paie n'accepte **aucune écriture manuelle**. On fait corriger le déversement dans EIG RH |
| 7 | IM | **Automatique** (EIG IMMOS) | SES | Aucun en manuel (l'écriture automatique sera 6811200 D / 2818300 C) | — | Les amortissements viennent **uniquement** d'EIG IMMOS. On vérifie la fiche de l'immobilisation et on relance le calcul |
| 8 | VT | **Automatique** (EIG Gestion commerciale) | **Pas chez nous** : livres de la Fédération | Tiers **CL**… (sur 4110000) D ; 7060004 Prestations de formation C | Fait par EIG, pas à la main | Seule la Fédération utilise le journal des ventes. Cap Horizons 21 n'a **pas** de journal VT |
| 9 | BQASS **puis** CAASS | Manuels, contrepartie auto | **ASS** | **5800000** Virements internes dans les deux journaux | BQASS : 5800000 D 150,00 (auto 5125000 C) ; CAASS : 5800000 C 150,00 (auto 5300000 D) | Mouvement entre deux comptes de trésorerie **de la même structure** : passage obligé par le 58 |
| 10 | AC | Manuel | **SAV** | 6062400 Fournitures administratives ; tiers **FOBUREAU26** | FOBUREAU26 **D** 37,80 ; 6062400 **C** 37,80 | Un avoir s'enregistre « à l'envers » de la facture (document T21) |
| 11 | OD | Manuel, avec contrepartie | **SIE** (avec IS) | 6061200 + 1849100 à 1849400 D ; **4081000** Fournisseurs – factures non parvenues C, **sans tiers FO** | Charges D ; 4081000 C 2 150,00, au **31/12/2026** | La consommation de 2026 doit être en charge en 2026 ; le 4081000 « remplace » le compte FO. Extourne (écriture inverse) au 01/01/2027 |
| 12 | AC | Manuel | **SES** | **6223221** Honoraires orthophonistes ; tiers **LIDUPONT** sur 4011000 | 6223221 D 675,00 ; LIDUPONT C 675,00 | Libéral conventionné : préfixe **LI**, pas FO. Contrôle du relevé avant saisie : voir E18-03 |
| 13 | BQSAV | Manuel, contrepartie auto | **SAV** | Tiers **FOGARAGEMARTIN** | FOGARAGEMARTIN D 494,28 ; auto 5123000 C | Paiement d'une facture déjà saisie : on solde le tiers, puis on **lettre** (on relie la facture et son paiement) |
| 14 | BQSES | Manuel, contrepartie auto | **SES** | **6270000** Services bancaires | 6270000 D 18,60 ; auto 5122000 C | Frais prélevés par la banque : directement en charge |
| 15 | BQASS | Manuel, contrepartie auto | **ASS** | **7541xxx** Dons (dans le plan T21 : 7541200 Dons autres projets, subdivision à confirmer) ; code 90-ASSO | 7541200 C 200,00 ; auto 5125000 D | Don : compte 754. Penser au **reçu fiscal** au donateur |
| 16 | BQASS | Manuel, contrepartie auto | **ASS** | **7410002** Subvention Fondation de France ; code **50-PAIRS** | 7410002 C 6 000,00 ; auto 5125000 D | Subvention privée affectée à un projet : 74xxxxx + code du projet. À la clôture, la part non utilisée ira en **fonds dédiés** |
| 17 | AC | Manuel | **EMP** | **2183000** Matériel de bureau et informatique (899,00) + 6068000 Autres achats non stockés (24,90) ; tiers **FOINFORHONE** | 2183000 D 899,00 et 6068000 D 24,90 ; FOINFORHONE C 923,90 | Bien durable de plus de 500 € TTC : **immobilisation**, saisie TTC. La souris, utilisable seule et sous le seuil, reste en charge. Créer la fiche dans **EIG IMMOS** |
| 18 | AC | Manuel | **SIE** (avec IS selon les m²) | **6152100** Maintenance et contrôle obligatoire immobilier ; tiers **à créer : FOSECURIFEU26** | 6152100 et 18xx D ; FOSECURIFEU26 C | **Interdit** de saisir sur 4010000 directement : on cherche le tiers, puis on le crée |
| 19 | BQSES **et** BQSIE | Manuels, contrepartie auto | **SES** et **SIE** | SES : **1840000** Liaison Siège. SIE : **1849100** Liaison SESSAD | SES : 1840000 D 4 800,00 (auto 5122000 C). SIE : 1849100 C 4 800,00 (auto 5121000 D) | Deux **structures** différentes : on passe par les comptes de **liaison**, jamais par le 58 |
| 20 | BQSAV | Manuel, contrepartie auto | **SAV** | **6419100** Remboursements sur rémunérations – prévoyance | 6419100 C 1 245,30 ; auto 5123000 D | Prévoyance : 6419100, à distinguer des IJSS (6419000), pour suivre chaque organisme |

## 3. Écritures comptables (les trois cas qui posent le plus de questions)

### Ligne 1 — Facture EDF commune : ce qui apparaît chez le siège et chez le SESSAD (question 3)

Répartition de 2 093,87 € selon les m² : SIE 15 % = 314,08 ; SES 45 % = 942,24 ; SAV 25 % = 523,47 ; EMP 10 % = 209,39 ; ASS 5 % = 104,69. Total : 2 093,87 €.

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SIE | AC | 6061200 Énergie, électricité | | EDF – électricité Valence – 10284556712 – 09-10/2026 – part siège 15 % | 01-SIEGE | 314,08 | |
| SIE | AC | 1849100 Liaison SESSAD | | EDF – électricité Valence – IS SESSAD 45 % | | 942,24 | |
| SIE | AC | 1849200 Liaison SAVS | | EDF – électricité Valence – IS SAVS 25 % | | 523,47 | |
| SIE | AC | 1849300 Liaison Emploi | | EDF – électricité Valence – IS Emploi 10 % | | 209,39 | |
| SIE | AC | 1849400 Liaison Association | | EDF – électricité Valence – IS Asso 5 % | | 104,69 | |
| SIE | AC | 4010000 Fournisseurs | FOEDF | EDF – électricité Valence – 10284556712 – 09-10/2026 | | | 2 093,87 |
| SES | OD | 6061200 Énergie, électricité | | EDF 09-10/2026 – IS reçue du siège | 10-SESSAD | 942,24 | |
| SES | OD | 1840000 Liaison Siège | | EDF 09-10/2026 – IS reçue du siège | | | 942,24 |

Dans les livres du SESSAD, on ne voit **ni EDF, ni FOEDF** : seulement sa part de charge (942,24 €) et la dette envers le siège (1840000 au crédit). Les écritures miroirs du SAVS, de l'emploi et de l'association sont identiques avec leurs montants (générées automatiquement si EIG est paramétré ainsi, sinon saisies en OD).

### Ligne 9 — Retrait d'espèces pour la petite caisse (question 4)

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| ASS | BQASS | 5800000 Virements internes | | Retrait DAB pour caisse marché de Noël – 10/11/2026 | | 150,00 | |
| ASS | BQASS | 5125000 Crédit Mutuel – Association *(ligne automatique)* | | Retrait DAB pour caisse marché de Noël – 10/11/2026 | | | 150,00 |
| ASS | CAASS | 5300000 Caisse *(ligne automatique)* | | Alimentation caisse par retrait DAB – 10/11/2026 | | 150,00 | |
| ASS | CAASS | 5800000 Virements internes | | Alimentation caisse par retrait DAB – 10/11/2026 | | | 150,00 |

Chaque journal de trésorerie ne connaît que **son** compte (512 pour la banque, 53 pour la caisse). On ne peut donc pas écrire « 53 au débit, 512 au crédit » dans une seule écriture. Chaque journal enregistre sa moitié, et le **58** sert de « sas » entre les deux. Contrôle : le 58 revient à **zéro** dès que les deux moitiés sont saisies ; un 58 qui ne s'annule pas signale une moitié oubliée.

### Ligne 19 — Remboursement du siège par le SESSAD

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | BQSES | 1840000 Liaison Siège | | Remboursement IS octobre 2026 au siège | | 4 800,00 | |
| SES | BQSES | 5122000 Crédit Mutuel – SESSAD *(ligne automatique)* | | Remboursement IS octobre 2026 au siège | | | 4 800,00 |
| SIE | BQSIE | 5121000 Crédit Mutuel – Siège *(ligne automatique)* | | Remboursement IS octobre 2026 par le SESSAD | | 4 800,00 | |
| SIE | BQSIE | 1849100 Liaison SESSAD | | Remboursement IS octobre 2026 par le SESSAD | | | 4 800,00 |

Après cette écriture, la dette du SESSAD envers le siège (1840000 au crédit chez le SESSAD) et la créance du siège sur le SESSAD (1849100 au débit chez le siège) diminuent **toutes les deux** de 4 800,00 €. Elles restent l'opposé l'une de l'autre.

## 4. Points d'attention / pièges

- **Ligne 6 (paie à la main)** — réponse à la cheffe de service : « Je ne peux pas : le journal de paie est automatique, aucune écriture manuelle n'y est autorisée. Je préviens la personne qui gère EIG RH pour qu'elle relance le déversement d'octobre de l'emploi accompagné, et je vérifie ensuite que le total du journal de paie correspond au journal PDF. » Une paie saisie à la main serait **en double** dès que le déversement fonctionnera, et ne correspondrait plus à EIG RH.
- **Ligne 7 (amortissement en OD)** — « Les dotations viennent uniquement d'EIG IMMOS. Si elle manque, c'est que la fiche de l'ordinateur n'est pas créée, est mal paramétrée (date de mise en service, durée, structure) ou que le calcul n'a pas été lancé. On corrige dans EIG IMMOS. » Une OD créerait un amortissement que le tableau d'EIG IMMOS ignore : au premier calcul, il serait **compté deux fois**.
- **Ligne 18 (saisir sur 4010000)** — « Le 4010000 est un compte de centralisation : il est interdit d'y saisir. Je cherche d'abord si le fournisseur existe déjà (sous un autre nom, par exemple FOSECURIFEU), sinon je crée FOSECURIFEU26. Cela prend deux minutes, et sans compte de tiers on ne peut ni lettrer, ni payer, ni détecter un doublon. »
- **Ligne 19 (58 entre deux structures)** — « Le 58 sert entre deux comptes de trésorerie de la **même** structure. Ici, l'argent passe du SESSAD au siège : ce sont deux comptabilités différentes. Le mouvement se passe par les comptes de **liaison** 1840000 / 1849100. » En 58, l'opération laisserait un 58 non soldé dans chaque structure et ne réduirait pas les comptes de liaison.
- **Ligne 3 et ligne 20** : jamais en produit (classe 7). Les IJSS et la prévoyance **diminuent** les charges de personnel (6419000 et 6419100, au crédit).
- **Ligne 4** : une dotation de l'ARS n'est pas une subvention. Le compte 731 la distingue des subventions 74, ce qu'attendent l'ARS et le Département dans les documents budgétaires.
- **Ligne 8** : piège de lecture. Le journal des ventes existe dans le modèle T21, mais **seule la Fédération** l'utilise. Si Cap Horizons 21 reçoit un jour une facture de la Fédération, elle la saisit comme **toute** facture fournisseur : au journal AC, avec un tiers FO.
- **Ligne 11** : le compte 4081000 n'a **pas** de tiers FO. C'est le compte lui-même qui porte la dette estimée. N'oubliez pas l'**extourne** au 01/01/2027, sinon la charge sera comptée deux fois quand la vraie facture sera saisie.
- **Ligne 17** : la TVA n'est pas récupérable, l'immobilisation est donc inscrite **TTC** (899,00 €), pas HT.

## 5. Ce qu'un senior ferait en plus

**Bonnes pratiques**

- Tenir à jour un **aide-mémoire d'aiguillage** d'une page (pièce → journal → compte), affiché à côté de l'écran pendant les premiers mois. Le tableau ci-dessus en est la base.
- Avant chaque saisie en banque, vérifier que l'opération n'est **pas déjà** passée (une facture déjà payée par prélèvement, une IJSS déjà lettrée).
- **Contrôles mensuels** : le compte 5800000 est à zéro dans chaque structure ; le 1849100 du siège est l'opposé exact du 1840000 du SESSAD (et de même pour chaque structure) ; aucun solde sur un compte de centralisation sans tiers ; le journal PA et le journal IM sont arrivés pour **chaque** structure et chaque mois.
- Répondre aux demandes « pour aller plus vite » **par écrit** (un mail court), en citant la règle T21. Cela protège l'agent comptable si quelqu'un insiste, et forme les collègues.

**Le raisonnement d'analyse**

- Les règles « journal automatique, aucune saisie manuelle » ne sont pas des caprices : elles garantissent que la comptabilité est **identique** aux outils de gestion (EIG RH, EIG IMMOS). Le commissaire aux comptes rapproche ces outils et la comptabilité ; une écriture manuelle casse le rapprochement.
- La question « quelle structure ? » est la plus grave, car chaque structure a son **financeur**. Une charge du SAVS saisie au SESSAD est, en pratique, payée avec l'argent de l'ARS au lieu de celui du Département. C'est ce que l'autorité de tarification peut rejeter dans le compte administratif ou l'ERRD.

## 6. Références

- Documents internes Trisomie 21 France : « Les journaux comptables chez Trisomie 21 France » et « La comptabilité chez Trisomie 21 France » (30/04/2026), « Plan comptable général T21 France » (13/10/2025).
- Arrêté du 19 décembre 2025 relatif au plan comptable applicable aux établissements et services privés sociaux et médico-sociaux relevant du I de l'article L. 312-1 du Code de l'action sociale et des familles.
- Fiche du dossier M18 : structures, journaux, tiers, clés de répartition.
