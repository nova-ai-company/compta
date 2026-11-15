# E18-11 — Cas de synthèse : tout le mois de novembre 2026 dans les 5 structures
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★★ | **Durée estimée :** 3 h | **Thèmes :** saisie complète d'un mois, journaux AC, BQxxx, CAASS et OD, tiers FO / LI / SA, factures communes et IS, frais de siège, dotations, IJSS, subvention, dons, notes de frais, immobilisation, virement entre structures, contrôle (sans saisie) du déversement de paie, check-list mensuelle, balance des comptes de liaison
**Corner case :** oui — une pièce est un **duplicata** déjà saisi, un salarié du SAVS présente une note de frais qui relève de la structure **ASS**, et le déversement de paie contient une ligne qui ferait **doublon** avec la banque

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQEMP** | Journal de banque de l'emploi accompagné. Contrepartie automatique 5124000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CESF** | Conseiller (ou conseillère) en économie sociale et familiale. Travailleur social qui aide les personnes à gérer leur budget, leur logement, leur vie quotidienne. Métier fréquent dans un SAVS. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **DAB** | Distributeur automatique de billets. Retrait d'espèces : à justifier (alimentation de la caisse ou prélèvement de l'exploitant). |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PA** | Plateforme agréée — ou, dans le M18, journal de paie. Opérateur agréé par l'État (anciennement « PDP ») qui transmet les factures électroniques entre entreprises et envoie les données à l'administration. Dans le module M18, PA est le code du journal des salaires, alimenté automatiquement par EIG RH. |
    | **PRLV** | Prélèvement. Abréviation utilisée sur les relevés bancaires. |
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
    | **VIR** | Virement. Abréviation utilisée sur les relevés bancaires. |
    | **Compte 641x** | Rémunérations du personnel (sous-comptes). Salaires, congés payés, indemnités. |
    | **Compte 645x** | Charges sociales patronales (sous-comptes). |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 4210000** | Personnel - Rémunérations dues (plan T21). Salaires nets à payer. Crédité par la paie, débité au virement des salaires. |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7541200** | Dons Autres projets (plan T21). Dons pour d'autres projets. |
    | **FOFERRAND** | Compte fournisseur expert-comptable (dossier M18). Honoraires de comptabilité et de paie (6226010), répartis en IS. |
    | **FOFONCIA** | Compte fournisseur bailleur (dossier M18). Foncière Rhodanienne : loyer et charges des locaux de Valence, répartis en IS selon les m². |
    | **FOINFORHONE** | Compte fournisseur informatique (dossier M18). Maintenance informatique (6156100) et matériel (2183000 si immobilisé). |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOORANGE** | Compte fournisseur télécom (dossier M18). Contrat unique de téléphonie et internet facturé au siège, réparti en IS selon les ETP. |
    | **FOTOTALCARTE** | Compte fournisseur carte carburant (dossier M18). Relevé mensuel des cartes carburant des véhicules de service (6062100). |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIBENALI** | Compte libéral : psychologue (dossier M18). Groupes de parole du SAVS (6223224). |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **LIMOREAUPSY** | Compte libéral : psychomotricien (dossier M18). Séances de psychomotricité du SESSAD (6223222). |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **SAHADDAD** | Compte salarié : Rachid Haddad (dossier M18). Notes de frais d'un CESF (SAVS et habitat inclusif). |
    | **SAMARCHETTI** | Compte salarié : Julie Marchetti (dossier M18). Notes de frais d'une chargée d'insertion (emploi accompagné). |
    | **Bon à payer** | Accord écrit de la direction pour payer. Sans bon à payer de la directrice, la facture ne part pas en paiement. |
    | **codes analytiques** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **Indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
<!-- /glossaire-page -->

*Fiche de référence : [les 5 structures et les règles de saisie](../fiche_dossier_5_structures.md). Gardez-la ouverte : vous aurez besoin des comptes de banque, des comptes de liaison et des clés.*

## La mise en situation

Mardi **1er décembre 2026**. Mme Berthier dépose sur votre bureau la bannette de novembre :

> « Voici tout novembre, toutes structures mélangées, comme d'habitude. Les bons à payer sont signés. La paie de novembre a été déversée hier par EIG RH : merci de la **contrôler** (pas de la saisir, bien sûr). Les virements des salaires du 27/11 sont déjà saisis en banque par Sophie. Je voudrais pour vendredi la check-list de fin de mois et l'état des comptes de liaison, car le SAVS doit encore rembourser le siège. »

Rappels de la fiche : pas de TVA récupérable (tout en **TTC**), pas de stocks (comptes **606xxxx**), seuil d'immobilisation **500,00 € TTC** (hypothèse), IJSS en **6419000** au crédit, dotations en **731xxxx**, frais de siège **4,5 %** (fictif). Clés : **m²** 15 / 45 / 25 / 10 / 5 % ; **ETP** 9 / 48 / 27 / 12 / 4 % ; **forfait** honoraires 20 / 40 / 20 / 10 / 10 % (ordre : SIE / SES / SAV / EMP / ASS). Barème kilométrique de l'association : **0,50 €/km** (*valeur fictive, à vérifier chaque année*).

Soldes des comptes de liaison au **31/10/2026** (chiffres propres à cet exercice) : au siège, 1849100 Liaison SESSAD **24 380,00 D** ; 1849200 Liaison SAVS **9 875,40 D** ; 1849300 Liaison Emploi **4 110,00 D** ; 1849400 Liaison Association **1 120,00 C**. Chaque structure a l'exact opposé dans son 1840000.

## Les pièces

**P1 — Foncière Rhodanienne (FOFONCIA), facture n° FR-26-1102 du 02/11/2026**
```
Locaux 12 rue des Alpes, Valence – novembre 2026
Loyer ................................ 5 400,00 €
Provision sur charges locatives .......  800,00 €
Total à payer (prélèvement le 05/11) . 6 200,00 €
Bon à payer : N. Berthier
```

**P2 — Opérateur télécom (FOORANGE), facture n° 26-11-778412 du 06/11/2026** — flotte mobile et internet, novembre 2026 : **1 450,00 € TTC** (dont TVA 241,67 €).

**P3 — Cabinet Hélène Ferrand (FOFERRAND), facture n° HF-2026-311 du 10/11/2026** — honoraires de comptabilité et de paie, novembre 2026 : **2 160,00 € TTC**.

**P4 — Relevé BQSIE (siège)**
```
05/11  PRLV FONCIERE RHODANIENNE FR-26-1102 ......... - 6 200,00
24/11  VIR RECU CAP HORIZONS 21 SAVS REMB IS ......... + 8 000,00
```

**P5 — Note de la directrice : frais de siège de novembre 2026**
```
SESSAD : 5 175,00 € · SAVS : 2 587,50 € · Emploi accompagné : 1 350,00 €
(L'autorisation de frais de siège porte sur ces trois services ; la structure
« Association et projets » n'en supporte pas.)
```

**P6 — Claire Dupont, orthophoniste (LIDUPONT), facture n° CD-2026-11 du 30/11/2026** — 22 séances × 34,00 € = **748,00 €**, enfants du SESSAD.

**P7 — Julien Moreau, psychomotricien (LIMOREAUPSY), facture n° JM-112026 du 30/11/2026** — 16 séances × 38,00 € = **608,00 €**, enfants du SESSAD.

**P8 — Ludik Éducation (FOLUDIK), facture n° LE-2026-1244 du 13/11/2026** — jeux de manipulation et matériel sensoriel pour le SESSAD : 405,75 € HT + TVA 20 % 81,15 € = **486,90 € TTC**.

**P9 — Note de frais de Nathalie Durand, éducatrice spécialisée au SESSAD (SADURAND), novembre 2026**
```
Indemnités kilométriques : 412 km × 0,50 € ........... 206,00 €
Parking hôpital (ticket) ..............................   8,60 €
Repas en déplacement (ticket du 19/11) ................  18,90 €
Feutres, carnets pour les séances (ticket) ............  23,40 €
Total ................................................. 256,90 €
Validée par le chef de service le 30/11/2026
```

**P10 — Relevé BQSES (SESSAD)**
```
06/11  VIR ARS AUVERGNE-RHONE-ALPES DOTATION 11/2026 ... + 108 000,00
20/11  VIR CPAM DROME IJSS SUBROGATION M. ......... ...  +     642,18
```

**P11 — Samira Benali, psychologue (LIBENALI)**
```
a) Facture n° SB-2026-11 du 30/11/2026 : 4 groupes de parole × 240,00 € = 960,00 €
   (adultes du SAVS)
b) Document « DUPLICATA » de la facture n° SB-2026-10 du 31/10/2026 : 960,00 €,
   envoyé « suite à votre relance ».
   Extrait du compte LIBENALI (SAVS) : SB-2026-10 saisie le 04/11/2026, 960,00 €, non payée.
```

**P12 — Carte carburant (FOTOTALCARTE), relevé n° TC-2611-0457 du 30/11/2026** — véhicules du SAVS : **1 214,70 € TTC**, prélèvement le 10/12/2026.

**P13 — Relevé BQSAV (SAVS)**
```
05/11  VIR DEPARTEMENT DE LA DROME DOTATION SAVS 11/2026 ... + 57 500,00
24/11  VIR EMIS VERS CAP HORIZONS 21 SIEGE REMB IS .......... -  8 000,00
```

**P14 — Note de frais de Rachid Haddad, CESF salarié du SAVS (SAHADDAD), novembre 2026**
```
Mission pour l'habitat inclusif « La Maison partagée » (structure Association) :
Produits d'entretien pour la salle commune (ticket) ....  38,60 €
Indemnités kilométriques : 96 km × 0,50 € .............  48,00 €
Total .................................................  86,60 €
```

**P15 — Note de frais de Julie Marchetti, chargée d'insertion (SAMARCHETTI), novembre 2026**
```
Train Valence – Lyon aller-retour (forum emploi) : 2 × 24,50 € ... 49,00 €
Repas (ticket du 17/11) ........................................ 17,80 €
Total .......................................................... 66,80 €
```

**P16 — Relevé BQEMP (Emploi accompagné)**
```
16/11  VIR AGEFIPH CONV 2026-EA-26-117 2E VERSEMENT ........ + 12 000,00
```
*(Convention de 24 000,00 € du 01/07/2026 au 30/06/2027 ; les versements sont crédités au compte 7488000.)*

**P17 — Info Rhône Services (FOINFORHONE), facture n° F-IRS-1119 du 19/11/2026**
```
1 ordinateur portable 14" + sacoche, pour la chargée d'insertion (Emploi accompagné)
Total HT 907,50 € · TVA 20 % 181,50 € · Total TTC 1 089,00 €
Garantie 3 ans. Paiement à 30 jours.
```

**P18 — Relevé BQASS (Association et projets)**
```
09/11  VIR DONS EN LIGNE OCTOBRE (campagne « Pairs et voix ») ... + 1 350,00
27/11  RETRAIT DAB VALENCE ...................................... -   300,00
```
*Le retrait alimente la caisse du marché de Noël (carnet de caisse : entrée de 300,00 € le 27/11). Les dons vont au compte 7541200 Dons Autres projets (subdivision retenue par l'association, à confirmer).*

**P19 — Récapitulatif du déversement de la paie de novembre 2026 (journal PA, EIG RH) — à CONTRÔLER, pas à saisir**

| Structure | Salaires bruts (641x) | Charges patronales (645x) | Net à payer (4210000) | Autres lignes déversées | Virement des salaires du 27/11 (déjà saisi) |
|---|---|---|---|---|---|
| SIE | 18 640,00 € | 5 778,40 € | 14 539,20 € | — | 14 539,20 € |
| SES | 101 860,00 € | 31 576,60 € | 79 450,80 € | 6419000 IJSS subrogation : **642,18 € au crédit** | 79 450,80 € |
| SAV | 29 140,00 € | 9 033,40 € | 22 729,20 € | — | 22 729,20 € |
| EMP | 12 070,00 € | 3 741,70 € | 9 414,60 € | — | 9 414,60 € |
| ASS | 3 120,00 € | 0,00 € | 2 433,60 € | — | 2 433,60 € |

## Travail à faire

1. Pour chaque pièce, indiquez la **structure**, le **journal** et les **comptes** (tableau de tri). Signalez les pièces à **ne pas saisir** et pourquoi.
2. Passez **toutes les écritures** de novembre, **structure par structure** (SIE, SES, SAV, EMP, ASS), avec les **IS** et leurs **miroirs**, les codes analytiques et des libellés au format de la fiche (`Tiers – objet – n° de pièce – période`).
3. **P17** : quelle conséquence dans **EIG IMMOS** ? Quelle écriture passera le journal **IM** et quand ?
4. **P19** : contrôlez le déversement de paie. Quelles anomalies voyez-vous ? Que faites-vous (et que ne faites-vous surtout pas) ?
5. Établissez la **balance des comptes de liaison au 30/11/2026** (siège et structures) et vérifiez que leur total fait zéro.
6. Rédigez la **check-list de fin de mois** que vous appliquerez désormais chaque mois.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-11_corrige.md)
