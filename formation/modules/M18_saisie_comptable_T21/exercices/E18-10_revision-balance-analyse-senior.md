# E18-10 — Réviser la balance du SAVS au 30/11/2026 comme une senior
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★★ | **Durée estimée :** 2 h | **Thèmes :** revue analytique d'une balance, comparaison N / N-1 / budget, sens normal des comptes, balance auxiliaire et comptes de centralisation, lettrage, grand livre, rapprochement bancaire, comptes de liaison, frais de siège, seuil d'immobilisation, absence de TVA
**Corner case :** oui — deux anomalies différentes produisent **un seul** écart sur le compte de liaison, et un compte fournisseur débiteur cache une saisie interdite sur le compte de centralisation

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **AN** | À-nouveaux — ou avantage en nature (paie). Deux sens : (1) journal des à-nouveaux, qui reprend les soldes du bilan au début de l'exercice ; (2) en paie, avantage en nature (voiture, logement…). |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **ESMS** | Établissement ou service médico-social. Autre façon d'écrire ESSMS : une structure autorisée et financée par l'ARS et/ou le Département. |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **RAN** | Report à nouveau. Résultat d'un exercice pas encore affecté (comptes 115xxxx créditeurs, 1159xxx débiteurs dans le plan T21). |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 1150120** | RAN ESMS sous gestion contrôlée (créditeur) (plan T21). Report à nouveau excédentaire d'un ESSMS financé par une autorité de tarification (« gestion contrôlée ») : excédent pas encore affecté. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 2183000** | Matériel de bureau et matériel informatique (plan T21). Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. |
    | **Compte 2818300** | Amort Matériel de bureau et matériel informatique (plan T21). Amortissements cumulés du matériel informatique. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4310000** | Sécurité sociale (plan T21). URSSAF : cotisations à payer. Crédité par la paie, débité au paiement. |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6132000** | Locations immobilières (plan T21). Loyer des locaux. |
    | **Compte 6156100** | Maintenance informatique (plan T21). Maintenance informatique, abonnements logiciels. |
    | **Compte 6161000** | Assurance Multirisques (plan T21). Assurance multirisque des locaux. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6223224** | Honoraires Psychologues (plan T21). Honoraires de psychologues. |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6262000** | Frais de télécommunication (plan T21). Téléphone, internet. |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6411100** | Personnel titulaire et stagiaires - Rémunération principale (plan T21). Salaires bruts des salariés en CDI (« titulaires »). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6451100** | Cotisations à l’URSSAF (plan T21). Cotisations URSSAF (part employeur). |
    | **Compte 6556000** | Frais de siège social du gestionnaire (plan T21). Frais de siège facturés par le siège à la structure (taux autorisé par le financeur). |
    | **Compte 7312170** | Dotation du SAVS (dossier M18, numéro fictif). Le plan T21 ne prévoit que 7312130 (services pour enfants). Pour le SAVS, une autre subdivision 7312xxx est nécessaire : à vérifier dans le plan de l'association. |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
    | **FOBUREAU26** | Compte fournisseur fournitures de bureau (dossier M18). Fournitures administratives (6062400). |
    | **FOGARAGEMARTIN** | Compte fournisseur Garage Martin (dossier M18). Garage de Valence : entretien et achat des véhicules. Regroupé dans 4010000. |
    | **FOINFORHONE** | Compte fournisseur informatique (dossier M18). Maintenance informatique (6156100) et matériel (2183000 si immobilisé). |
    | **FOTOTALCARTE** | Compte fournisseur carte carburant (dossier M18). Relevé mensuel des cartes carburant des véhicules de service (6062100). |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIBENALI** | Compte libéral : psychologue (dossier M18). Groupes de parole du SAVS (6223224). |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

*Fiche de référence : [les 5 structures et les règles de saisie](../fiche_dossier_5_structures.md).*

## La mise en situation

Lundi **7 décembre 2026**. La paie de novembre est déversée, les relevés bancaires sont arrivés. Hélène Ferrand (expert-comptable) vous appelle :

> « Avant la clôture, je veux une **revue de la balance du SAVS à fin novembre**. Ne me renvoyez pas la balance telle quelle : regardez-la comme je le ferais. Comparez avec l'an dernier et avec le budget, vérifiez le sens de chaque solde, rapprochez les comptes de tiers et les liaisons avec le siège. J'ai l'impression qu'il y a pas mal de choses à reprendre. Vous me faites une liste des anomalies avec l'écriture qui corrige chacune. »

Rappel : le **SAVS** (code structure **SAV**, code analytique **20-SAVS**) est financé par le **Département** par une dotation globale de **690 000,00 €** pour 2026, versée par douzièmes de 57 500,00 € (compte **7312170**, numéro fictif, voir la fiche § 6). Les frais de siège du SAVS sont fixés à **2 587,50 € par mois** (4,5 % du budget de charges de 690 000,00 €, divisé par 12 — taux fictif). Ils arrivent du siège chaque fin de mois par une IS.

## Les pièces

**Pièce 1 — Balance générale du SAVS au 30/11/2026 (extrait : seuls 27 comptes sont reproduits, l'extrait ne s'équilibre donc pas)**

| Compte | Intitulé | Solde débiteur | Solde créditeur | Solde au 30/11/2025 (N-1) | Budget 2026 × 11/12 |
|---|---|---|---|---|---|
| 1150120 | RAN ESMS sous gestion contrôlée (créditeur) | | 12 400,00 | C 12 400,00 | — |
| 1840000 | Liaison Siège | | 41 210,30 | C 38 612,70 | — |
| 2183000 | Matériel de bureau et matériel informatique | 8 750,00 | | D 7 210,00 | — |
| 2818300 | Amort Matériel de bureau et matériel informatique | | 4 120,00 | C 2 890,00 | — |
| 4010000 | Fournisseurs FO | | 1 717,20 | C 3 940,60 | — |
| 4011000 | Libéraux LI | | 2 184,00 | C 960,00 | — |
| 4248000 | Salariés - NDF SA | | 238,60 | C 312,40 | — |
| 4310000 | Sécurité sociale | | 18 450,00 | C 17 980,00 | — |
| 4456600 | TVA déductible sur autres biens et services | 186,40 | | — | — |
| 4710000 | Comptes d'attente | 742,00 | | 0,00 | — |
| 5123000 | Crédit Mutuel – SAVS | 64 380,55 | | D 58 920,10 | — |
| 5800000 | Virements internes | 1 500,00 | | 0,00 | — |
| 6062100 | Combustibles et carburants | 12 846,30 | | D 11 920,10 | 12 375,00 |
| 6062400 | Fournitures administratives | 2 184,60 | | D 1 412,30 | 1 375,00 |
| 6132000 | Locations immobilières | 14 850,00 | | D 14 520,00 | 14 850,00 |
| 6156100 | Maintenance informatique | 3 410,00 | | D 3 190,00 | 3 300,00 |
| 6161000 | Assurance Multirisques | 1 800,00 | | D 1 740,00 | 1 800,00 |
| 6223221 | Honoraires Orthophonistes | 1 224,00 | | 0,00 | 0,00 |
| 6223224 | Honoraires Psychologues | 9 600,00 | | D 8 640,00 | 10 560,00 |
| 6251000 | Voyages et déplacements | 4 912,70 | | D 4 405,20 | 4 675,00 |
| 6262000 | Frais de télécommunication | 3 564,00 | | D 3 420,00 | 3 575,00 |
| 6270000 | Services bancaires et assimilés | 214,40 | | D 198,60 | 220,00 |
| 6411100 | Personnel titulaire et stagiaires - Rémunération principale | 318 640,00 | | D 309 815,00 | 322 300,00 |
| 6419000 | Remboursements sur rémunération du personnel - IJSS | 1 860,00 | | C 4 210,00 | C 2 750,00 |
| 6451100 | Cotisations à l'URSSAF | 98 420,00 | | D 95 640,00 | 99 900,00 |
| 6556000 | Frais de siège social du gestionnaire | 25 875,00 | | D 27 225,00 | 28 462,50 |
| 7312170 | Dotation SAVS (Département) — *numéro fictif* | | 632 500,00 | C 618 750,00 | C 632 500,00 |

*D = solde débiteur, C = solde créditeur.*

**Pièce 2 — Balance auxiliaire des fournisseurs du SAVS au 30/11/2026**

| Compte de tiers | Solde débiteur | Solde créditeur |
|---|---|---|
| FOBUREAU26 | | 412,80 |
| FOGARAGEMARTIN | 624,00 | |
| FOINFORHONE | 1 248,00 | |
| FOTOTALCARTE | | 1 928,40 |
| *(écritures sans compte de tiers)* | | 1 248,00 |
| **Total = solde du 4010000** | **1 872,00** | **3 589,20** |

**Pièce 3 — Balance auxiliaire des libéraux du SAVS au 30/11/2026**

| Compte de tiers | Solde débiteur | Solde créditeur |
|---|---|---|
| LIBENALI | | 960,00 |
| LIDUPONT | | 1 224,00 |
| **Total = solde du 4011000** | | **2 184,00** |

**Pièce 4 — Extrait de la balance du siège (SIE) au 30/11/2026**
```
1849200  Liaison SAVS ..................... solde débiteur 42 297,80
```

**Pièce 5 — État de rapprochement bancaire du SAVS au 30/11/2026 (préparé par une collègue, non terminé)**
```
Solde du relevé Crédit Mutuel au 30/11/2026 ............. 68 100,55 € créditeur
Solde du compte 5123000 en comptabilité ................. 64 380,55 € débiteur
Écart non expliqué ......................................  3 720,00 €
« Je n'ai trouvé aucun chèque ni virement en suspens. »
```

**Pièce 6 — Extraits du grand livre du SAVS** *(à consulter **après** avoir écrit vos hypothèses, comme une senior qui « descend » de la balance vers le détail)*

| Date | Journal | Compte | Libellé | Débit | Crédit (colonnes du grand livre) |
|---|---|---|---|---|---|
| 01/01/2026 | AN | 2183000 | À-nouveaux | 7 210,00 | |
| 12/03/2026 | AC | 2183000 | FOINFORHONE – PC portable – F-IRS-0311 | 1 190,00 | |
| 15/10/2026 | AC | 2183000 | FOBUREAU26 – destructeur de documents – F-BV-26-4502 | 350,00 | |
| 08/10/2026 | AC | 6062400 | FOBUREAU26 – fournitures – F-BV-26-4471 | 932,00 | |
| 08/10/2026 | AC | 4456600 | FOBUREAU26 – TVA – F-BV-26-4471 | 186,40 | |
| 08/10/2026 | AC | FOBUREAU26 | FOBUREAU26 – F-BV-26-4471 | | 1 118,40 |
| 22/09/2026 | BQSAV | 4710000 | Prélèvement TOTALENERGIES CARTE 09/2026 | 742,00 | |
| 30/09/2026 | AC | FOTOTALCARTE | Relevé carte carburant 09/2026 | | 742,00 |
| 31/10/2026 | AC | FOTOTALCARTE | Relevé carte carburant 10/2026 | | 1 186,40 |
| 05/09/2026 | AC | FOGARAGEMARTIN | Révision Kangoo SAVS – F-GM-2026-388 | | 624,00 |
| 12/09/2026 | BQSAV | FOGARAGEMARTIN | Virement F-GM-2026-388 | 624,00 | |
| 03/10/2026 | BQSAV | FOGARAGEMARTIN | Virement F-GM-2026-388 | 624,00 | |
| 18/06/2026 | AC | 4010000 | Info Rhône – maintenance logiciels – F-IRS-0612 | | 1 248,00 |
| 30/06/2026 | BQSAV | FOINFORHONE | Virement F-IRS-0612 | 1 248,00 | |
| 16/10/2026 | BQSAV | 5800000 | Virement SAVS vers siège – remboursement IS T3 | 1 500,00 | |
| 14/10/2026 | BQSAV | 6419000 | CPAM – IJSS Mme Roche – arrêt 09/2026 | 1 860,00 | |
| 28/10/2026 | AC | 6223221 | LIDUPONT – orthophonie – 36 séances – F2026-10 | 1 224,00 | |
| 31/01 au 31/10/2026 | OD | 6556000 | Frais de siège – IS reçue du siège (10 lignes de 2 587,50) | 25 875,00 | |

*Au siège, le 16/10/2026, le même virement a été saisi en BQSIE au crédit du compte 1849200 Liaison SAVS (1 500,00 €). Les frais de siège de novembre ont été saisis au siège le 30/11/2026 (7556000 au crédit, 1849200 au débit, 2 587,50 €).*

## Travail à faire

1. **Méthode.** Avant de regarder le grand livre, décrivez en 6 à 8 étapes la façon dont une senior révise une balance (dans quel ordre, avec quels outils, quelles questions).
2. **Sens normal des comptes.** Repérez dans la pièce 1 les comptes dont le solde est dans un **sens anormal** (ou qui ne devraient avoir **aucun** solde, ou qui ne devraient **pas exister**). Expliquez pour chacun pourquoi.
3. **Comparaisons.** Calculez au moins quatre écarts significatifs N / N-1 ou réalisé / budget et un **ratio** de contrôle (par exemple charges sociales / salaires). Lesquels sont normaux, lesquels sont des alertes ?
4. **Tiers.** Rapprochez la balance générale et les balances auxiliaires (pièces 2 et 3). Que révèlent les lignes FOINFORHONE, « écritures sans compte de tiers », FOGARAGEMARTIN et LIDUPONT ?
5. **Liaison.** Rapprochez le 1840000 du SAVS et le 1849200 du siège. Expliquez l'écart **au centime**.
6. **Anomalies.** Dressez la liste des **10 anomalies** (anomalie → cause probable → conséquence → écriture corrective). Toutes les écritures correctives doivent être **équilibrées** et indiquer le journal et les livres.
7. Présentez les **soldes corrigés** des comptes touchés et vérifiez le rapprochement bancaire.
8. Rédigez le **mail de synthèse** à Hélène Ferrand.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-10_corrige.md)
