# E18-07 — Les inter-structures d'un mois dans les cinq structures, et le contrôle croisé des liaisons
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★★ | **Durée estimée :** 2 h | **Thèmes :** factures communes, clés de répartition (m², ETP, forfait), inter-structures (IS), comptes de liaison 184xxxx / 1840000, écritures miroirs, frais de siège (6556000 / 7556000), dépense payée par le mauvais compte bancaire, remboursements mensuels au siège, contrôle croisé des liaisons, solde consolidé nul

**Corner case :** oui — une écriture miroir manque dans une structure, et une facture du SESSAD a été payée par le compte du siège puis saisie comme si c'était une dépense du siège

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
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **AN** | À-nouveaux — ou avantage en nature (paie). Deux sens : (1) journal des à-nouveaux, qui reprend les soldes du bilan au début de l'exercice ; (2) en paie, avantage en nature (voiture, logement…). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQEMP** | Journal de banque de l'emploi accompagné. Contrepartie automatique 5124000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
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
    | **bon à payer** | Accord écrit de la direction pour payer. Sans bon à payer de la directrice, la facture ne part pas en paiement. |
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **Code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes, sociétés et documents fictifs. Les numéros de comptes de charges et de produits viennent du plan comptable T21 France ; les numéros de liaison et de banque sont ceux de la fiche du dossier M18.*

!!! abstract "En clair"
    Le siège reçoit les factures **communes** (un seul bail, un seul contrat EDF, un seul expert-comptable). Il les saisit, garde **sa** part, et « envoie » la part de chaque structure par un **compte de liaison**. Chaque structure enregistre la même somme **en miroir** : la charge chez elle, et une dette envers le siège. À la fin, les deux côtés doivent être **exactement opposés** : ce que le siège dit qu'on lui doit = ce que la structure dit qu'elle doit. Si ce n'est pas le cas, il manque une écriture quelque part, et c'est vous qui devez la trouver.

## La mise en situation

Lundi 16 novembre 2026. Nathalie Berthier vous confie la **clôture mensuelle de novembre** des inter-structures :

> « Mme Roux faisait le contrôle croisé des liaisons tous les mois. Depuis son départ, l'intérimaire a saisi les factures communes de novembre, mais je ne suis pas sûre que tout ait été passé partout. Reprenez tout : je veux, pour le comité de direction du 1er décembre, un tableau des liaisons au 30/11 qui tombe juste. »

Chez Cap Horizons 21, l'**écriture miroir** dans chaque structure n'est **pas** générée automatiquement par le logiciel : on la passe soi-même en **OD** dans le dossier de la structure (cas prévu par la fiche du dossier, § 5).

Rappels de la fiche :

| Structure | Banque / journal | Liaison chez le siège | Liaison chez la structure | Code analytique |
|---|---|---|---|---|
| SIE | 5121000 / BQSIE | — | — | 01-SIEGE |
| SES | 5122000 / BQSES | 1849100 Liaison SESSAD | 1840000 Liaison Siège | 10-SESSAD |
| SAV | 5123000 / BQSAV | 1849200 Liaison SAVS | 1840000 Liaison Siège | 20-SAVS |
| EMP | 5124000 / BQEMP | 1849300 Liaison Emploi | 1840000 Liaison Siège | 30-EMPLOI |
| ASS | 5125000 / BQASS | 1849400 Liaison Association | 1840000 Liaison Siège | 90-ASSO *(dans cet exercice, on ne ventile pas la part de l'ASS entre 40-HABITAT, 50-PAIRS et 90-ASSO)* |

| Clé | SIE | SES | SAV | EMP | ASS |
|---|---|---|---|---|---|
| **m²** (loyer, charges, électricité) | 15 % | 45 % | 25 % | 10 % | 5 % |
| **ETP** (télécom, informatique) | 9 % | 48 % | 27 % | 12 % | 4 % |
| **Forfait** (expert-comptable, CAC) | 20 % | 40 % | 20 % | 10 % | 10 % |

## Les pièces

**Pièce 1 — Les six factures communes de novembre, reçues et saisies au siège (journal AC de SIE), toutes avec bon à payer**

| Date | Fournisseur (tiers) | N° | Objet | Compte(s) de charge | Montant TTC |
|---|---|---|---|---|---|
| 03/11/2026 | Foncière Rhodanienne (FOFONCIA) | FR-2611-0087 | Loyer de novembre des locaux de Valence : loyer 7 200,00 + provision sur charges 1 000,00 | 6132000 Locations immobilières ; 6140000 Charges locatives et de copropriété | 8 200,00 |
| 04/11/2026 | EDF (FOEDF) | F2026-91544 | Électricité des locaux de Valence, septembre-octobre 2026 | 6061200 Énergie, électricité | 1 386,40 |
| 05/11/2026 | Orange (FOORANGE) | OR-2611-0148 | Flotte mobile et internet, novembre | 6262000 Frais de télécommunication | 1 150,00 |
| 06/11/2026 | Cabinet Ferrand (FOFERRAND) | FA-26-11-4688 | Comptabilité et paie, novembre | 6226010 Honoraires comptabilité | 3 840,00 |
| 09/11/2026 | Audit Rhodanien (FOAUDITRHO) | AR-26-0412 | Commissaire aux comptes : 2e acompte sur la mission 2026 | 6228000 Autres honoraires *(le plan T21 n'a pas de compte dédié au CAC)* | 4 200,00 |
| 10/11/2026 | Info Rhône Services (FOINFORHONE) | IRS-2611-221 | Maintenance informatique, contrat mensuel, novembre | 6156100 Maintenance informatique | 980,00 |
| | | | | **Total** | **19 756,40** |

**Pièce 2 — Frais de siège de novembre**

Taux autorisé : **4,5 %** (fictif, voir M16), appliqué chaque mois aux charges brutes du mois des deux services autorisés à les supporter, hors frais de siège eux-mêmes. Écriture passée au **30/11**.

| Structure | Base : charges brutes de novembre (hors frais de siège) |
|---|---|
| SES | 96 400,00 |
| SAV | 51 200,00 |

*L'emploi accompagné et l'association ne supportent pas de frais de siège en 2026 (hypothèse : leurs conventions ne le prévoient pas).*

**Pièce 3 — Une facture du SESSAD payée par le compte du siège**

- Le 04/11, la facture **LE-2026-358** de Ludik Éducation (FOLUDIK), 642,80 € TTC, jeux éducatifs du SESSAD, a été saisie **dans les livres du SESSAD** (AC de SES : 6062500 au débit, FOLUDIK au crédit, code 10-SESSAD).
- Le 12/11, le fournisseur ayant relancé, l'intérimaire l'a payée en urgence **depuis le compte bancaire du siège** (5121000). Il a saisi au journal **BQSIE** : *FOLUDIK au débit 642,80* (contrepartie automatique 5121000 au crédit).
- Dans les livres du siège, le compte FOLUDIK n'a **aucune facture** LE-2026-358.

**Pièce 4 — Remboursements mensuels au siège (virements programmés le 20/11/2026)**

| Du compte | Vers le compte | Montant | Libellé |
|---|---|---|---|
| 5122000 SESSAD | 5121000 Siège | 18 000,00 | Remboursement IS et frais de siège – 11/2026 |
| 5123000 SAVS | 5121000 Siège | 9 000,00 | Remboursement IS et frais de siège – 11/2026 |
| 5124000 Emploi | 5121000 Siège | 3 000,00 | Remboursement IS – 11/2026 |

*Pas de virement pour l'ASS ce mois-ci : au 31/10, c'est le siège qui lui devait de l'argent.*

**Pièce 5 — Soldes des comptes de liaison au 31/10/2026 (contrôle croisé d'octobre fait et validé par Mme Roux)**

| Structure | Chez le siège | Chez la structure (compte 1840000) |
|---|---|---|
| SES | 1849100 : débiteur 12 400,00 | créditeur 12 400,00 |
| SAV | 1849200 : débiteur 6 150,00 | créditeur 6 150,00 |
| EMP | 1849300 : débiteur 2 380,00 | créditeur 2 380,00 |
| ASS | 1849400 : **créditeur** 1 200,00 | **débiteur** 1 200,00 |

**Pièce 6 — Extraits du grand livre au 16/11/2026, avant toute correction**

*Livres du siège — compte 1849200 Liaison SAVS*

| Date | Journal | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|---|
| 01/11 | AN | Solde au 31/10 | | | D 6 150,00 |
| 03/11 | AC | Foncière Rhodanienne – loyer 11/2026 – IS SAV | 2 050,00 | | D 8 200,00 |
| 04/11 | AC | EDF – électricité sept.-oct. 2026 – IS SAV | 346,60 | | D 8 546,60 |
| 05/11 | AC | Orange – 11/2026 – IS SAV | 310,50 | | D 8 857,10 |
| 06/11 | AC | Cabinet Ferrand – 11/2026 – IS SAV | 768,00 | | D 9 625,10 |
| 09/11 | AC | Audit Rhodanien – acompte 2 – IS SAV | 840,00 | | D 10 465,10 |
| 10/11 | AC | Info Rhône – 11/2026 – IS SAV | 264,60 | | D 10 729,70 |

*Livres du SAVS — compte 1840000 Liaison Siège*

| Date | Journal | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|---|
| 01/11 | AN | Solde au 31/10 | | | C 6 150,00 |
| 03/11 | OD | Foncière Rhodanienne – loyer 11/2026 – IS reçue | | 2 050,00 | C 8 200,00 |
| 05/11 | OD | Orange – 11/2026 – IS reçue | | 310,50 | C 8 510,50 |
| 06/11 | OD | Cabinet Ferrand – 11/2026 – IS reçue | | 768,00 | C 9 278,50 |
| 09/11 | OD | Audit Rhodanien – acompte 2 – IS reçue | | 840,00 | C 10 118,50 |
| 10/11 | OD | Info Rhône – 11/2026 – IS reçue | | 264,60 | C 10 383,10 |

*Les comptes 1849100 / 1840000 SES, 1849300 / 1840000 EMP et 1849400 / 1840000 ASS sont, eux, cohérents au 16/11 (vous pouvez le vérifier avec vos propres écritures).*

## Travail à faire

1. Calculez, pour chacune des six factures, la **part de chaque structure** (tableau : facture × structure), et vérifiez que chaque ligne retombe sur le montant de la facture.
2. Passez l'écriture de chaque facture dans les livres du **siège** (journal AC de SIE : part du siège en charge, part des autres structures en liaison 184xxxx, fournisseur au crédit).
3. Passez les **écritures miroirs** dans les livres de **chaque** structure (SES, SAV, EMP, ASS).
4. Calculez et passez les **frais de siège** de novembre, chez le siège et dans les structures concernées.
5. **Pièce 3** : expliquez ce qui ne va pas dans la saisie de l'intérimaire, puis passez les écritures de correction chez le siège et au SESSAD. Comment aurait-il fallu saisir le paiement du 12/11 dès le départ ?
6. Passez les **remboursements** du 20/11 dans les livres du siège et des structures. Pourquoi ne passe-t-on **pas** par le compte 5800000 Virements internes ?
7. **Contrôle croisé au 16/11** : comparez les deux extraits de la pièce 6. Trouvez l'écart, expliquez-le, corrigez-le. Comment un senior organise-t-il ce contrôle pour qu'une telle erreur ne dure jamais plus d'un mois ?
8. Établissez le **tableau des liaisons au 30/11/2026**, après toutes les écritures et corrections : pour chaque structure, solde chez le siège, solde chez la structure, somme. Montrez que chaque solde du siège est l'**opposé** de celui de la structure, et que la **somme de tous les comptes 18** de l'association est **nulle**. Montrez aussi ce qu'aurait donné ce tableau sans la correction de la question 7.
9. Vérifiez que le total des charges réparties (parts des cinq structures) est égal au total des six factures.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-07_corrige.md)
