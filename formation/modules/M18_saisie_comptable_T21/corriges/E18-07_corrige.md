# Corrigé E18-07 — Les inter-structures d'un mois dans les cinq structures, et le contrôle croisé des liaisons

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
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQEMP** | Journal de banque de l'emploi accompagné. Contrepartie automatique 5124000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **VIR** | Virement. Abréviation utilisée sur les relevés bancaires. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5124000** | Banque de l'emploi accompagné (dossier M18, fictif). Compte bancaire de l'emploi accompagné, journal BQEMP. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6062500** | Fournitures scolaires, éducatives et de loisirs (plan T21). Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. |
    | **Compte 6132000** | Locations immobilières (plan T21). Loyer des locaux. |
    | **Compte 6140000** | Charges locatives et de copropriété (plan T21). Charges locatives et de copropriété refacturées par le bailleur. |
    | **Compte 6156100** | Maintenance informatique (plan T21). Maintenance informatique, abonnements logiciels. |
    | **Compte 6226010** | Honoraires comptabilité (plan T21). Honoraires de l'expert-comptable (et du commissaire aux comptes, faute de compte dédié dans le plan : à vérifier). |
    | **Compte 6228000** | Autres honoraires (plan T21). Autres honoraires. |
    | **Compte 6262000** | Frais de télécommunication (plan T21). Téléphone, internet. |
    | **Compte 6556000** | Frais de siège social du gestionnaire (plan T21). Frais de siège facturés par le siège à la structure (taux autorisé par le financeur). |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
    | **FOAUDITRHO** | Compte fournisseur commissaire aux comptes (dossier M18). Honoraires du CAC, répartis en IS. |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **FOFERRAND** | Compte fournisseur expert-comptable (dossier M18). Honoraires de comptabilité et de paie (6226010), répartis en IS. |
    | **FOFONCIA** | Compte fournisseur bailleur (dossier M18). Foncière Rhodanienne : loyer et charges des locaux de Valence, répartis en IS selon les m². |
    | **FOINFORHONE** | Compte fournisseur informatique (dossier M18). Maintenance informatique (6156100) et matériel (2183000 si immobilisé). |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOORANGE** | Compte fournisseur télécom (dossier M18). Contrat unique de téléphonie et internet facturé au siège, réparti en IS selon les ETP. |
    | **charge commune** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **Lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-07](../exercices/E18-07_inter-structures-5-structures.md)

> *Cadre de formation : association, personnes, sociétés et documents fictifs.*

!!! abstract "En clair"
    Pour chaque opération entre structures, il y a **deux écritures dans deux dossiers différents**, et elles doivent se répondre au centime près : quand le siège **débite** 1849200 (« le SAVS me doit »), le SAVS **crédite** 1840000 (« je dois au siège ») du même montant. Le contrôle croisé consiste simplement à mettre les deux soldes côte à côte, structure par structure, chaque mois. Leur somme doit faire **zéro**.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — La part de chaque structure

On applique la clé de la fiche à **chaque compte de charge** (le loyer et les charges locatives sont deux comptes : on les répartit séparément, pour que chaque structure ait le détail par nature). Tous les pourcentages tombent juste au centime : pas d'arrondi à gérer ce mois-ci.

| Facture | Montant | Clé | SIE | SES | SAV | EMP | ASS | Contrôle |
|---|---|---|---|---|---|---|---|---|
| FOFONCIA FR-2611-0087 – 6132000 | 7 200,00 | m² | 1 080,00 | 3 240,00 | 1 800,00 | 720,00 | 360,00 | 7 200,00 ✓ |
| FOFONCIA FR-2611-0087 – 6140000 | 1 000,00 | m² | 150,00 | 450,00 | 250,00 | 100,00 | 50,00 | 1 000,00 ✓ |
| FOEDF F2026-91544 – 6061200 | 1 386,40 | m² | 207,96 | 623,88 | 346,60 | 138,64 | 69,32 | 1 386,40 ✓ |
| FOORANGE OR-2611-0148 – 6262000 | 1 150,00 | ETP | 103,50 | 552,00 | 310,50 | 138,00 | 46,00 | 1 150,00 ✓ |
| FOFERRAND FA-26-11-4688 – 6226010 | 3 840,00 | forfait | 768,00 | 1 536,00 | 768,00 | 384,00 | 384,00 | 3 840,00 ✓ |
| FOAUDITRHO AR-26-0412 – 6228000 | 4 200,00 | forfait | 840,00 | 1 680,00 | 840,00 | 420,00 | 420,00 | 4 200,00 ✓ |
| FOINFORHONE IRS-2611-221 – 6156100 | 980,00 | ETP | 88,20 | 470,40 | 264,60 | 117,60 | 39,20 | 980,00 ✓ |
| **Total** | **19 756,40** | | **3 237,66** | **8 552,28** | **4 579,70** | **2 018,24** | **1 368,52** | **19 756,40** ✓ |

*Si une clé donnait des centimes en trop ou en moins (ex. 103,365), la règle maison serait de mettre l'arrondi sur la structure qui a la plus grosse part (le SESSAD), pour que la somme des parts soit toujours égale à la facture.*

### Question 2 et 3 — La logique des écritures

**Chez le siège**, la facture est saisie **en entier** au crédit du fournisseur (c'est le siège qui doit la payer). Au débit : la **part du siège** en charge (code 01-SIEGE) et la **part de chaque structure** en liaison. Le siège ne garde en charge que **ses** 15 % de loyer : le reste n'est pas « sa » charge, c'est une somme que les structures lui doivent.

**Dans chaque structure**, l'écriture miroir : la charge au débit (avec le code analytique de la structure), **1840000 Liaison Siège** au crédit. Il n'y a **pas** de fournisseur dans la structure : la structure ne doit rien à la Foncière Rhodanienne, elle doit au siège.

> ⚠️ Erreur classique : saisir dans la structure « FOFONCIA au crédit » pour sa part. Le fournisseur aurait alors deux dettes enregistrées (une chez le siège pour 8 200,00, une au SESSAD pour 3 690,00) et pourrait être payé deux fois.

### Question 4 — Les frais de siège

| Structure | Base | Taux | Frais de siège |
|---|---|---|---|
| SES | 96 400,00 | 4,5 % | **4 338,00** |
| SAV | 51 200,00 | 4,5 % | **2 304,00** |
| **Total** | | | **6 642,00** |

Chez la structure : **6556000 Frais de siège social du gestionnaire** au débit, 1840000 au crédit. Chez le siège : 184xxxx au débit, **7556000 Siège social du gestionnaire** au crédit. Les frais de siège sont la **ressource** du siège : c'est ainsi qu'il finance la direction, la comptabilité et les RH qui travaillent pour tous.

### Question 5 — La facture Ludik payée par le compte du siège

Ce qui ne va pas : dans les livres du **siège**, le compte FOLUDIK reçoit un débit de 642,80 € **sans facture en face** (la facture est au SESSAD). Résultat :

- au siège, FOLUDIK est **débiteur** : on dirait que Ludik doit 642,80 € au siège (une avance, un trop-payé) ;
- au SESSAD, FOLUDIK reste **créditeur** : la facture paraît impayée, et sera **payée une deuxième fois** à la prochaine campagne ;
- et personne ne voit que le SESSAD doit 642,80 € au siège.

Correction : chez le siège, on transforme la fausse « créance sur Ludik » en **créance sur le SESSAD** (1849100 au débit, FOLUDIK au crédit, ce qui solde FOLUDIK au siège). Au SESSAD, on éteint la dette envers Ludik et on constate la dette envers le siège (FOLUDIK au débit, lettré avec la facture ; 1840000 au crédit).

**Ce qu'il aurait fallu faire dès le 12/11** : au journal BQSIE, taper directement **1849100 au débit 642,80** (libellé « Ludik LE-2026-358 payée pour le SESSAD »), et passer au SESSAD l'OD FOLUDIK / 1840000. Une seule saisie juste au lieu d'une saisie fausse et d'une correction. Et, mieux encore : **payer la facture depuis le compte du SESSAD**, puisque c'est sa facture. Le paiement par le compte d'une autre structure doit rester une exception autorisée par la directrice.

### Question 6 — Les remboursements : pourquoi pas le 58 ?

Le compte **5800000 Virements internes** sert aux mouvements entre deux comptes de trésorerie **d'une même comptabilité** (exemple : retrait de la banque de l'ASS vers la caisse de l'ASS). Ici, l'argent passe du compte du **SESSAD** au compte du **siège** : ce sont **deux comptabilités différentes**. Si l'on passait par le 58, le 58 du SESSAD resterait débiteur et celui du siège créditeur, à jamais, et la dette du SESSAD envers le siège (1840000) ne diminuerait pas. Le remboursement **solde une dette de liaison** : il se saisit **en liaison**, des deux côtés.

### Question 7 — Le contrôle croisé au 16/11

| Compte | Solde au 16/11 |
|---|---|
| Siège, 1849200 Liaison SAVS | débiteur 10 729,70 |
| SAVS, 1840000 Liaison Siège | créditeur 10 383,10 |
| **Écart** | **346,60** |

On cherche une ligne de **346,60** dans un compte et pas dans l'autre : c'est l'**IS EDF du 04/11** (25 % de 1 386,40). Elle est chez le siège, pas au SAVS. L'intérimaire a passé les miroirs EDF au SESSAD, à l'Emploi et à l'ASS, mais a oublié le SAVS.

Conséquences si on ne la voit pas : la charge d'électricité du SAVS est **sous-évaluée** de 346,60 € (le compte administratif remis au Département serait faux), et l'association, en consolidé, a des comptes 18 qui ne s'annulent plus : son bilan ne tombe pas, et le CAC le verra tout de suite.

Correction : passer au SAVS l'OD manquante (6061200 au débit 346,60, code 20-SAVS ; 1840000 au crédit 346,60), datée du 04/11 si la période est ouverte.

**L'organisation d'un senior :**

1. **Contrôle croisé mensuel**, à date fixe (par exemple le 5 du mois suivant), pour les **quatre** couples de comptes, dans un tableau toujours identique (celui de la question 8), signé et classé.
2. **Lettrage des comptes de liaison** par pièce : chaque IS porte la même référence de pièce des deux côtés (n° de facture), ce qui permet de rapprocher ligne à ligne et de trouver l'écart en une minute.
3. **Saisie des miroirs juste après l'écriture du siège**, facture par facture, et non « en fin de mois pour tout le monde ».
4. Demander à l'éditeur si EIG peut **générer automatiquement** les miroirs à partir du compte IS saisi (c'est ce que décrit le document T21) : la meilleure façon d'éviter un oubli est de rendre l'oubli impossible.

## 2. Calculs (détaillés, chaque montant justifié)

| Calcul | Détail | Résultat |
|---|---|---|
| Total des factures | 8 200,00 + 1 386,40 + 1 150,00 + 3 840,00 + 4 200,00 + 980,00 | 19 756,40 |
| Total réparti (question 9) | 3 237,66 + 8 552,28 + 4 579,70 + 2 018,24 + 1 368,52 | 19 756,40 ✓ |
| IS du mois à la charge du SES | 3 240,00 + 450,00 + 623,88 + 552,00 + 1 536,00 + 1 680,00 + 470,40 | 8 552,28 |
| IS du mois à la charge du SAV | 1 800,00 + 250,00 + 346,60 + 310,50 + 768,00 + 840,00 + 264,60 | 4 579,70 |
| IS du mois à la charge de l'EMP | 720,00 + 100,00 + 138,64 + 138,00 + 384,00 + 420,00 + 117,60 | 2 018,24 |
| IS du mois à la charge de l'ASS | 360,00 + 50,00 + 69,32 + 46,00 + 384,00 + 420,00 + 39,20 | 1 368,52 |
| Frais de siège SES | 96 400,00 × 4,5 % | 4 338,00 |
| Frais de siège SAV | 51 200,00 × 4,5 % | 2 304,00 |
| Liaison SES au 30/11 | 12 400,00 + 8 552,28 + 642,80 + 4 338,00 − 18 000,00 | 7 933,08 |
| Liaison SAV au 30/11 | 6 150,00 + 4 579,70 + 2 304,00 − 9 000,00 | 4 033,70 |
| Liaison EMP au 30/11 | 2 380,00 + 2 018,24 − 3 000,00 | 1 398,24 |
| Liaison ASS au 30/11 (vu du siège) | − 1 200,00 + 1 368,52 | + 168,52 (le siège a désormais une créance sur l'ASS) |

## 3. Écritures comptables

### 3.1 Livres du siège (SIE)

*Les factures (AC), la correction Ludik (OD), les remboursements reçus (BQSIE : ligne tapée + ligne 5121000 automatique) et les frais de siège (OD). Le règlement des six fournisseurs par le siège n'est pas montré : il ne touche pas les liaisons.*

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| AC | 03/11/2026 | 6132000 Locations immobilières |  | Foncière Rhodanienne – loyer 11/2026 – part siège 15 % | 01-SIEGE | 1 080,00 |  |
| AC | 03/11/2026 | 6140000 Charges locatives et de copropriété |  | Foncière Rhodanienne – loyer 11/2026 – part siège 15 % | 01-SIEGE | 150,00 |  |
| AC | 03/11/2026 | 1849100 Liaison SESSAD |  | Foncière Rhodanienne – loyer 11/2026 – IS SES |  | 3 690,00 |  |
| AC | 03/11/2026 | 1849200 Liaison SAVS |  | Foncière Rhodanienne – loyer 11/2026 – IS SAV |  | 2 050,00 |  |
| AC | 03/11/2026 | 1849300 Liaison Emploi |  | Foncière Rhodanienne – loyer 11/2026 – IS EMP |  | 820,00 |  |
| AC | 03/11/2026 | 1849400 Liaison Association |  | Foncière Rhodanienne – loyer 11/2026 – IS ASS |  | 410,00 |  |
| AC | 03/11/2026 | 4010000 Fournisseurs | FOFONCIA | Foncière Rhodanienne – loyer 11/2026 – FR-2611-0087 |  |  | 8 200,00 |
| AC | 04/11/2026 | 6061200 Énergie, électricité |  | EDF – électricité Valence – sept.-oct. 2026 – part siège 15 % | 01-SIEGE | 207,96 |  |
| AC | 04/11/2026 | 1849100 Liaison SESSAD |  | EDF – électricité Valence – sept.-oct. 2026 – IS SES |  | 623,88 |  |
| AC | 04/11/2026 | 1849200 Liaison SAVS |  | EDF – électricité Valence – sept.-oct. 2026 – IS SAV |  | 346,60 |  |
| AC | 04/11/2026 | 1849300 Liaison Emploi |  | EDF – électricité Valence – sept.-oct. 2026 – IS EMP |  | 138,64 |  |
| AC | 04/11/2026 | 1849400 Liaison Association |  | EDF – électricité Valence – sept.-oct. 2026 – IS ASS |  | 69,32 |  |
| AC | 04/11/2026 | 4010000 Fournisseurs | FOEDF | EDF – électricité Valence – sept.-oct. 2026 – F2026-91544 |  |  | 1 386,40 |
| AC | 05/11/2026 | 6262000 Frais de télécommunication |  | Orange – flotte et internet – 11/2026 – part siège 9 % | 01-SIEGE | 103,50 |  |
| AC | 05/11/2026 | 1849100 Liaison SESSAD |  | Orange – flotte et internet – 11/2026 – IS SES |  | 552,00 |  |
| AC | 05/11/2026 | 1849200 Liaison SAVS |  | Orange – flotte et internet – 11/2026 – IS SAV |  | 310,50 |  |
| AC | 05/11/2026 | 1849300 Liaison Emploi |  | Orange – flotte et internet – 11/2026 – IS EMP |  | 138,00 |  |
| AC | 05/11/2026 | 1849400 Liaison Association |  | Orange – flotte et internet – 11/2026 – IS ASS |  | 46,00 |  |
| AC | 05/11/2026 | 4010000 Fournisseurs | FOORANGE | Orange – flotte et internet – 11/2026 – OR-2611-0148 |  |  | 1 150,00 |
| AC | 06/11/2026 | 6226010 Honoraires comptabilité |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – part siège 20 % | 01-SIEGE | 768,00 |  |
| AC | 06/11/2026 | 1849100 Liaison SESSAD |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS SES |  | 1 536,00 |  |
| AC | 06/11/2026 | 1849200 Liaison SAVS |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS SAV |  | 768,00 |  |
| AC | 06/11/2026 | 1849300 Liaison Emploi |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS EMP |  | 384,00 |  |
| AC | 06/11/2026 | 1849400 Liaison Association |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS ASS |  | 384,00 |  |
| AC | 06/11/2026 | 4010000 Fournisseurs | FOFERRAND | Cabinet Ferrand – comptabilité et paie – 11/2026 – FA-26-11-4688 |  |  | 3 840,00 |
| AC | 09/11/2026 | 6228000 Autres honoraires |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – part siège 20 % | 01-SIEGE | 840,00 |  |
| AC | 09/11/2026 | 1849100 Liaison SESSAD |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS SES |  | 1 680,00 |  |
| AC | 09/11/2026 | 1849200 Liaison SAVS |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS SAV |  | 840,00 |  |
| AC | 09/11/2026 | 1849300 Liaison Emploi |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS EMP |  | 420,00 |  |
| AC | 09/11/2026 | 1849400 Liaison Association |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS ASS |  | 420,00 |  |
| AC | 09/11/2026 | 4010000 Fournisseurs | FOAUDITRHO | Audit Rhodanien – CAC acompte 2/3 mission 2026 – AR-26-0412 |  |  | 4 200,00 |
| AC | 10/11/2026 | 6156100 Maintenance informatique |  | Info Rhône Services – maintenance informatique – 11/2026 – part siège 9 % | 01-SIEGE | 88,20 |  |
| AC | 10/11/2026 | 1849100 Liaison SESSAD |  | Info Rhône Services – maintenance informatique – 11/2026 – IS SES |  | 470,40 |  |
| AC | 10/11/2026 | 1849200 Liaison SAVS |  | Info Rhône Services – maintenance informatique – 11/2026 – IS SAV |  | 264,60 |  |
| AC | 10/11/2026 | 1849300 Liaison Emploi |  | Info Rhône Services – maintenance informatique – 11/2026 – IS EMP |  | 117,60 |  |
| AC | 10/11/2026 | 1849400 Liaison Association |  | Info Rhône Services – maintenance informatique – 11/2026 – IS ASS |  | 39,20 |  |
| AC | 10/11/2026 | 4010000 Fournisseurs | FOINFORHONE | Info Rhône Services – maintenance informatique – 11/2026 – IRS-2611-221 |  |  | 980,00 |
| OD | 16/11/2026 | 1849100 Liaison SESSAD |  | Ludik – LE-2026-358 payée par le siège pour le SESSAD le 12/11 – reclassement |  | 642,80 |  |
| OD | 16/11/2026 | 4010000 Fournisseurs | FOLUDIK | Ludik – LE-2026-358 – annule le débit saisi à tort au BQSIE le 12/11 |  |  | 642,80 |
| BQSIE | 20/11/2026 | 1849100 Liaison SESSAD |  | SES – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(tapé)* |  |  | 18 000,00 |
| BQSIE | 20/11/2026 | 5121000 Banque CM Siège |  | SES – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(auto)* |  | 18 000,00 |  |
| BQSIE | 20/11/2026 | 1849200 Liaison SAVS |  | SAV – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(tapé)* |  |  | 9 000,00 |
| BQSIE | 20/11/2026 | 5121000 Banque CM Siège |  | SAV – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(auto)* |  | 9 000,00 |  |
| BQSIE | 20/11/2026 | 1849300 Liaison Emploi |  | EMP – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(tapé)* |  |  | 3 000,00 |
| BQSIE | 20/11/2026 | 5121000 Banque CM Siège |  | EMP – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(auto)* |  | 3 000,00 |  |
| OD | 30/11/2026 | 1849100 Liaison SESSAD |  | Frais de siège 11/2026 – 4,5 % × 96 400,00 – SES |  | 4 338,00 |  |
| OD | 30/11/2026 | 7556000 Siège social du gestionnaire |  | Frais de siège 11/2026 – 4,5 % × 96 400,00 – SES | 01-SIEGE |  | 4 338,00 |
| OD | 30/11/2026 | 1849200 Liaison SAVS |  | Frais de siège 11/2026 – 4,5 % × 51 200,00 – SAV |  | 2 304,00 |  |
| OD | 30/11/2026 | 7556000 Siège social du gestionnaire |  | Frais de siège 11/2026 – 4,5 % × 51 200,00 – SAV | 01-SIEGE |  | 2 304,00 |
| | | | | | **Total** | **57 041,20** | **57 041,20** |
### 3.2 Livres du SESSAD (SES)

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 03/11/2026 | 6132000 Locations immobilières |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 45 %) | 10-SESSAD | 3 240,00 |  |
| OD | 03/11/2026 | 6140000 Charges locatives et de copropriété |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 45 %) | 10-SESSAD | 450,00 |  |
| OD | 03/11/2026 | 1840000 Liaison Siège |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège |  |  | 3 690,00 |
| OD | 04/11/2026 | 6061200 Énergie, électricité |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège (m² 45 %) | 10-SESSAD | 623,88 |  |
| OD | 04/11/2026 | 1840000 Liaison Siège |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège |  |  | 623,88 |
| OD | 05/11/2026 | 6262000 Frais de télécommunication |  | Orange – flotte et internet – 11/2026 – IS reçue du siège (ETP 48 %) | 10-SESSAD | 552,00 |  |
| OD | 05/11/2026 | 1840000 Liaison Siège |  | Orange – flotte et internet – 11/2026 – IS reçue du siège |  |  | 552,00 |
| OD | 06/11/2026 | 6226010 Honoraires comptabilité |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège (forfait 40 %) | 10-SESSAD | 1 536,00 |  |
| OD | 06/11/2026 | 1840000 Liaison Siège |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège |  |  | 1 536,00 |
| OD | 09/11/2026 | 6228000 Autres honoraires |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège (forfait 40 %) | 10-SESSAD | 1 680,00 |  |
| OD | 09/11/2026 | 1840000 Liaison Siège |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège |  |  | 1 680,00 |
| OD | 10/11/2026 | 6156100 Maintenance informatique |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège (ETP 48 %) | 10-SESSAD | 470,40 |  |
| OD | 10/11/2026 | 1840000 Liaison Siège |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège |  |  | 470,40 |
| OD | 16/11/2026 | 4010000 Fournisseurs | FOLUDIK | Ludik – LE-2026-358 – réglée par le siège le 12/11 |  | 642,80 |  |
| OD | 16/11/2026 | 1840000 Liaison Siège |  | Ludik – LE-2026-358 – réglée par le siège pour le SESSAD |  |  | 642,80 |
| BQSES | 20/11/2026 | 1840000 Liaison Siège |  | SES – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(tapé)* |  | 18 000,00 |  |
| BQSES | 20/11/2026 | 5122000 Banque CM SESSAD |  | SES – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(auto)* |  |  | 18 000,00 |
| OD | 30/11/2026 | 6556000 Frais de siège social du gestionnaire |  | Frais de siège 11/2026 – 4,5 % × 96 400,00 | 10-SESSAD | 4 338,00 |  |
| OD | 30/11/2026 | 1840000 Liaison Siège |  | Frais de siège 11/2026 – 4,5 % × 96 400,00 |  |  | 4 338,00 |
| | | | | | **Total** | **31 533,08** | **31 533,08** |
### 3.3 Livres du SAVS (SAV)

*Les deux lignes EDF du 04/11 sont celles qui manquaient (question 7).*

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 03/11/2026 | 6132000 Locations immobilières |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 25 %) | 20-SAVS | 1 800,00 |  |
| OD | 03/11/2026 | 6140000 Charges locatives et de copropriété |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 25 %) | 20-SAVS | 250,00 |  |
| OD | 03/11/2026 | 1840000 Liaison Siège |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège |  |  | 2 050,00 |
| OD | 04/11/2026 | 6061200 Énergie, électricité |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège (m² 25 %) – **manquante, passée le 16/11 après contrôle croisé** | 20-SAVS | 346,60 |  |
| OD | 04/11/2026 | 1840000 Liaison Siège |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège – **manquante, passée le 16/11** |  |  | 346,60 |
| OD | 05/11/2026 | 6262000 Frais de télécommunication |  | Orange – flotte et internet – 11/2026 – IS reçue du siège (ETP 27 %) | 20-SAVS | 310,50 |  |
| OD | 05/11/2026 | 1840000 Liaison Siège |  | Orange – flotte et internet – 11/2026 – IS reçue du siège |  |  | 310,50 |
| OD | 06/11/2026 | 6226010 Honoraires comptabilité |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège (forfait 20 %) | 20-SAVS | 768,00 |  |
| OD | 06/11/2026 | 1840000 Liaison Siège |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège |  |  | 768,00 |
| OD | 09/11/2026 | 6228000 Autres honoraires |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège (forfait 20 %) | 20-SAVS | 840,00 |  |
| OD | 09/11/2026 | 1840000 Liaison Siège |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège |  |  | 840,00 |
| OD | 10/11/2026 | 6156100 Maintenance informatique |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège (ETP 27 %) | 20-SAVS | 264,60 |  |
| OD | 10/11/2026 | 1840000 Liaison Siège |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège |  |  | 264,60 |
| BQSAV | 20/11/2026 | 1840000 Liaison Siège |  | SAV – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(tapé)* |  | 9 000,00 |  |
| BQSAV | 20/11/2026 | 5123000 Banque CM SAVS |  | SAV – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(auto)* |  |  | 9 000,00 |
| OD | 30/11/2026 | 6556000 Frais de siège social du gestionnaire |  | Frais de siège 11/2026 – 4,5 % × 51 200,00 | 20-SAVS | 2 304,00 |  |
| OD | 30/11/2026 | 1840000 Liaison Siège |  | Frais de siège 11/2026 – 4,5 % × 51 200,00 |  |  | 2 304,00 |
| | | | | | **Total** | **15 883,70** | **15 883,70** |

### 3.4 Livres de l'Emploi accompagné (EMP)

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 03/11/2026 | 6132000 Locations immobilières |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 10 %) | 30-EMPLOI | 720,00 |  |
| OD | 03/11/2026 | 6140000 Charges locatives et de copropriété |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 10 %) | 30-EMPLOI | 100,00 |  |
| OD | 03/11/2026 | 1840000 Liaison Siège |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège |  |  | 820,00 |
| OD | 04/11/2026 | 6061200 Énergie, électricité |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège (m² 10 %) | 30-EMPLOI | 138,64 |  |
| OD | 04/11/2026 | 1840000 Liaison Siège |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège |  |  | 138,64 |
| OD | 05/11/2026 | 6262000 Frais de télécommunication |  | Orange – flotte et internet – 11/2026 – IS reçue du siège (ETP 12 %) | 30-EMPLOI | 138,00 |  |
| OD | 05/11/2026 | 1840000 Liaison Siège |  | Orange – flotte et internet – 11/2026 – IS reçue du siège |  |  | 138,00 |
| OD | 06/11/2026 | 6226010 Honoraires comptabilité |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège (forfait 10 %) | 30-EMPLOI | 384,00 |  |
| OD | 06/11/2026 | 1840000 Liaison Siège |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège |  |  | 384,00 |
| OD | 09/11/2026 | 6228000 Autres honoraires |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège (forfait 10 %) | 30-EMPLOI | 420,00 |  |
| OD | 09/11/2026 | 1840000 Liaison Siège |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège |  |  | 420,00 |
| OD | 10/11/2026 | 6156100 Maintenance informatique |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège (ETP 12 %) | 30-EMPLOI | 117,60 |  |
| OD | 10/11/2026 | 1840000 Liaison Siège |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège |  |  | 117,60 |
| BQEMP | 20/11/2026 | 1840000 Liaison Siège |  | EMP – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(tapé)* |  | 3 000,00 |  |
| BQEMP | 20/11/2026 | 5124000 Banque CM Emploi |  | EMP – remboursement mensuel au siège – VIR 20/11 – 11/2026 *(auto)* |  |  | 3 000,00 |
| | | | | | **Total** | **5 018,24** | **5 018,24** |
### 3.5 Livres de l'Association (ASS)

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 03/11/2026 | 6132000 Locations immobilières |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 5 %) | 90-ASSO | 360,00 |  |
| OD | 03/11/2026 | 6140000 Charges locatives et de copropriété |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège (m² 5 %) | 90-ASSO | 50,00 |  |
| OD | 03/11/2026 | 1840000 Liaison Siège |  | Foncière Rhodanienne – loyer 11/2026 – IS reçue du siège |  |  | 410,00 |
| OD | 04/11/2026 | 6061200 Énergie, électricité |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège (m² 5 %) | 90-ASSO | 69,32 |  |
| OD | 04/11/2026 | 1840000 Liaison Siège |  | EDF – électricité Valence – sept.-oct. 2026 – IS reçue du siège |  |  | 69,32 |
| OD | 05/11/2026 | 6262000 Frais de télécommunication |  | Orange – flotte et internet – 11/2026 – IS reçue du siège (ETP 4 %) | 90-ASSO | 46,00 |  |
| OD | 05/11/2026 | 1840000 Liaison Siège |  | Orange – flotte et internet – 11/2026 – IS reçue du siège |  |  | 46,00 |
| OD | 06/11/2026 | 6226010 Honoraires comptabilité |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège (forfait 10 %) | 90-ASSO | 384,00 |  |
| OD | 06/11/2026 | 1840000 Liaison Siège |  | Cabinet Ferrand – comptabilité et paie – 11/2026 – IS reçue du siège |  |  | 384,00 |
| OD | 09/11/2026 | 6228000 Autres honoraires |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège (forfait 10 %) | 90-ASSO | 420,00 |  |
| OD | 09/11/2026 | 1840000 Liaison Siège |  | Audit Rhodanien – CAC acompte 2/3 mission 2026 – IS reçue du siège |  |  | 420,00 |
| OD | 10/11/2026 | 6156100 Maintenance informatique |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège (ETP 4 %) | 90-ASSO | 39,20 |  |
| OD | 10/11/2026 | 1840000 Liaison Siège |  | Info Rhône Services – maintenance informatique – 11/2026 – IS reçue du siège |  |  | 39,20 |
| | | | | | **Total** | **1 368,52** | **1 368,52** |
### 3.6 Le tableau des liaisons au 30/11/2026 (question 8)

**Mouvements de novembre, vus du siège** (+ = débit du compte 184xxxx chez le siège = la structure doit au siège)

| Mouvement | SES (1849100) | SAV (1849200) | EMP (1849300) | ASS (1849400) |
|---|---|---|---|---|
| Solde au 31/10 | + 12 400,00 | + 6 150,00 | + 2 380,00 | − 1 200,00 |
| IS des six factures | + 8 552,28 | + 4 579,70 | + 2 018,24 | + 1 368,52 |
| Ludik payé par le siège pour le SESSAD | + 642,80 | | | |
| Remboursements du 20/11 | − 18 000,00 | − 9 000,00 | − 3 000,00 | |
| Frais de siège | + 4 338,00 | + 2 304,00 | | |
| **Solde au 30/11** | **+ 7 933,08** | **+ 4 033,70** | **+ 1 398,24** | **+ 168,52** |

**Contrôle croisé au 30/11/2026, après correction**

| Structure | Compte chez le siège | Solde chez le siège | Compte chez la structure | Solde chez la structure | Somme |
|---|---|---|---|---|---|
| SES | 1849100 | débiteur 7 933,08 | 1840000 | créditeur 7 933,08 | 0,00 ✓ |
| SAV | 1849200 | débiteur 4 033,70 | 1840000 | créditeur 4 033,70 | 0,00 ✓ |
| EMP | 1849300 | débiteur 1 398,24 | 1840000 | créditeur 1 398,24 | 0,00 ✓ |
| ASS | 1849400 | débiteur 168,52 | 1840000 | créditeur 168,52 | 0,00 ✓ |
| **Association entière** | **Total 184xxxx** | **débiteur 13 533,54** | **Total des 1840000** | **créditeur 13 533,54** | **0,00 ✓** |

Chaque solde du siège est l'**opposé exact** de celui de la structure, et la somme de **tous** les comptes 18 de l'association est nulle, comme l'exige le document T21 (« dans les comptes consolidés de l'organisme gestionnaire, les comptes de classe 18 doivent avoir un solde nul »).

Remarque sur l'ASS : au 31/10, le siège devait 1 200,00 € à l'ASS ; après les IS de novembre (1 368,52 €), c'est l'ASS qui doit 168,52 € au siège. Le compte a **changé de sens** : c'est normal, et c'est pour cela qu'on présente toujours les soldes avec « débiteur » ou « créditeur ».

**Le même tableau sans la correction de la question 7**

| Structure | Solde chez le siège | Solde chez la structure | Somme |
|---|---|---|---|
| SAV | débiteur 4 033,70 | créditeur 3 687,10 | **débiteur 346,60 ✗** |
| **Association entière** | débiteur 13 533,54 | créditeur 13 186,94 | **débiteur 346,60 ✗** |

Le consolidé ne tombe plus : il reste 346,60 € dans les comptes 18, qui « disparaîtraient » du bilan combiné de l'association.

## 4. Points d'attention / pièges

- **Mettre la part d'une structure en charge chez le siège** « pour simplifier » : les charges du siège seraient gonflées, et les frais de siège (calculés pour couvrir le coût réel du siège) seraient faux.
- **Mettre un fournisseur dans les livres de la structure** pour sa part d'IS : risque de double paiement.
- **Inverser les sens** : chez le siège, une IS de charge est au **débit** du 184xxxx (créance) ; chez la structure, au **crédit** du 1840000 (dette). Un remboursement fait l'inverse des deux côtés.
- **Utiliser le 5800000** pour les virements entre structures.
- **Payer la facture d'une structure par le compte d'une autre** et la saisir comme une dépense ordinaire : il faut **toujours** passer par la liaison.
- **Oublier le code analytique** sur les écritures miroirs : la charge serait bien dans la bonne structure, mais introuvable dans les tableaux par service.
- **Laisser un écart de liaison « parce qu'il est petit »** : un écart de 346,60 € cache une charge manquante dans le compte administratif du SAVS, et un bilan consolidé faux.

## 5. Ce qu'un senior ferait en plus

**Bonnes pratiques :**

- **Un classeur « IS » mensuel** : pour chaque facture commune, la copie de la facture, le calcul de la répartition (le tableau de la question 1), et la référence des cinq écritures. Le CAC et les financeurs demandent souvent **comment** une charge commune a été répartie : la réponse doit être prête.
- **Les clés figées et votées** : les clés m², ETP et forfait sont décidées pour l'année (en conseil d'administration ou par la direction) et revues chaque année. On ne change pas une clé en cours d'année sans décision écrite, sinon les comparaisons budgétaires n'ont plus de sens.
- **Rembourser selon le solde réel** : le virement du 20/11 a été programmé à l'aveugle (18 000,00 € pour le SESSAD, alors que la dette réelle sera de 25 933,08 € avant remboursement). Mieux : calculer le remboursement **après** le contrôle croisé, pour solder la dette du mois précédent. Cela évite de laisser des soldes de liaison grossir, et donne aux financeurs une image juste de la trésorerie de chaque service.
- **Frais de siège** : vérifier chaque mois que le cumul de l'année ne dépasse pas le montant autorisé (4,5 % des charges brutes de l'année, ou le montant arrêté par l'autorité de tarification). Si le budget d'un service est revu, les frais de siège le sont aussi.

**Analyse :**

- Ce mois-ci, les IS représentent 16 518,74 € (19 756,40 − 3 237,66 de part siège), soit 84 % des factures communes : l'essentiel des charges communes est **supporté par les services**. C'est l'information qui intéresse l'ARS et le Département.
- Le SESSAD porte 43 % des IS (8 552,28 / 19 756,40). Si sa part de surface ou d'effectif baisse (par exemple après le déménagement d'une équipe), il faudra revoir les clés pour 2027.

**Mail type à la directrice (pour le comité de direction) :**

> « Bonjour Nathalie, le contrôle croisé des liaisons de novembre est fait. Deux corrections : l'IS EDF manquait dans les comptes du SAVS (346,60 €, passée le 16/11) ; la facture Ludik du SESSAD, payée par le compte du siège le 12/11, a été reclassée en liaison (642,80 €). Au 30/11, les quatre couples de liaisons sont égaux et opposés, le total des comptes 18 est nul (tableau joint). Je propose de calculer les prochains remboursements des structures à partir de ce tableau, après le contrôle de chaque mois. »

## 6. Références

- Document interne T21 France « La comptabilité » (30/04/2026), classe 18 : inter-structures, compte IS renseigné à la saisie, solde nul des comptes 18 dans les comptes consolidés ; classe 58 : virements internes entre comptes de classe 5.
- Document interne T21 France « Les journaux comptables » : journal des achats (FO, classes 60-62), journaux de banque à contrepartie automatique, journal des opérations diverses.
- Plan comptable T21 France (MAJ 13/10/2025) : 1840000, 4010000, 5800000, 6061200, 6062500, 6132000, 6140000, 6156100, 6226010, 6228000, 6262000, 6556000, 7556000. Les numéros 1849100 à 1849400 et 5121000 à 5125000 sont propres au dossier (fiche M18) : dans le plan T21, les 184xxxx désignent d'autres structures du réseau.
- Arrêté du 19 décembre 2025 relatif au plan comptable des ESSMS privés relevant du I de l'article L. 312-1 du CASF : comptes de liaison et frais de siège (*à relire pour les conditions d'autorisation des frais de siège, fixées par le CASF*).
