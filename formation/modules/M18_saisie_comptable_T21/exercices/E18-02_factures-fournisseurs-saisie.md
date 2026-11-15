# E18-02 — Dix factures fournisseurs à contrôler et à saisir

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CTA** | Centrale de traitement d'air (ou écart de conversion). En immobilisations : équipement de ventilation ; en IFRS : écart de conversion (currency translation adjustment). |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **FALC** | Facile à lire et à comprendre. Méthode d'écriture simple, illustrée, pensée pour les personnes avec une déficience intellectuelle. Très utilisée dans le réseau Trisomie 21. |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **RCS** | Registre du commerce et des sociétés. Registre tenu par le greffe où sont immatriculées les sociétés commerciales. |
    | **SARL** | Société à responsabilité limitée. Société classique des PME ; le gérant majoritaire est TNS. Ex. : C01 Boulangerie Dupain. |
    | **SAS** | Société par actions simplifiée. Société très souple ; le président est assimilé salarié. Ex. : C02 Bâtisseurs du Sud, C08 TechNova. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **SIREN** | Numéro d'identification de l'entreprise (9 chiffres). Identifiant unique de chaque entreprise en France. Mention obligatoire sur les factures, y compris celui du client depuis la facturation électronique. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 2050000** | Concessions et droits similaires, brevets, licences (plan T21). Logiciel ou licence achetés (propriété durable). Un abonnement mensuel n'est pas une immobilisation. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **FOBUREAU26** | Compte fournisseur fournitures de bureau (dossier M18). Fournitures administratives (6062400). |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **FOFERRAND** | Compte fournisseur expert-comptable (dossier M18). Honoraires de comptabilité et de paie (6226010), répartis en IS. |
    | **FOFONCIA** | Compte fournisseur bailleur (dossier M18). Foncière Rhodanienne : loyer et charges des locaux de Valence, répartis en IS selon les m². |
    | **FOGARAGEMARTIN** | Compte fournisseur Garage Martin (dossier M18). Garage de Valence : entretien et achat des véhicules. Regroupé dans 4010000. |
    | **FOINFORHONE** | Compte fournisseur informatique (dossier M18). Maintenance informatique (6156100) et matériel (2183000 si immobilisé). |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOMAAF** | Compte fournisseur assurances (dossier M18). Mutuelle d'assurance : multirisque, flotte automobile, responsabilité civile. |
    | **FOORANGE** | Compte fournisseur télécom (dossier M18). Contrat unique de téléphonie et internet facturé au siège, réparti en IS selon les ETP. |
    | **FOTOTALCARTE** | Compte fournisseur carte carburant (dossier M18). Relevé mensuel des cartes carburant des véhicules de service (6062100). |
    | **bon à payer** | Accord écrit de la direction pour payer. Sans bon à payer de la directrice, la facture ne part pas en paiement. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **Lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 30 | **Thèmes :** contrôle des factures (mentions, calculs, doublon, bon à payer), TVA non récupérable et saisie TTC, facture commune répartie en inter-structures (IS), immobilisation ou charge (seuil de 500 € TTC), licence de logiciel (2050000) et maintenance, réparation ou achat de véhicule, prime d'assurance à cheval sur deux exercices, avoir, création d'un compte de tiers

**Corner case :** oui — une facture porte le numéro d'une facture déjà saisie et payée, avec un mauvais nom, une mauvaise adresse, une erreur de calcul et sans bon à payer ; une autre mélange une licence (immobilisation) et un contrat de maintenance (charge, en partie sur 2027).

> *Cadre de formation : association, personnes et documents fictifs. Les factures sont **reconstituées** : noms de fournisseurs repris de la fiche du dossier, SIREN, numéros de TVA et montants inventés.*

!!! abstract "En clair"
    Une facture n'est pas « à saisir » dès qu'elle arrive : elle est d'abord **à contrôler**. Est-elle bien adressée à l'association ? Les calculs sont-ils justes ? L'a-t-on déjà reçue ? La directrice a-t-elle donné son **bon à payer** (son accord écrit pour payer) ? Ensuite seulement, on choisit la structure, le compte et le tiers. Et comme l'association ne récupère pas la TVA, on saisit le montant **TTC** (toutes taxes comprises), pas le HT (hors taxes).

## La mise en situation

Lundi 16 novembre 2026. Le courrier et la boîte mail « factures » de la semaine ont été triés par l'assistante de direction. Dix pièces vous attendent. Nathalie Berthier, la directrice, a tamponné celles qu'elle a validées (« BON À PAYER »). Elle vous laisse un mot :

> « Bonjour, voici les factures de la semaine. Saisissez tout ce qui peut l'être avant mercredi : la campagne de virements est le **20/11**. Pour celles qui posent problème, mettez-les de côté et dites-moi quoi faire. Attention à l'achat du Partner pour le SESSAD, c'est la grosse dépense de l'année. Merci ! N. B. »

**Rappels de la fiche du dossier**

- L'association **ne récupère pas la TVA** : charges et immobilisations sont saisies **TTC**.
- Pas de stocks : les achats vont en **606xxxx**.
- Un bien durable de **plus de 500 € TTC** est immobilisé (classe 2) ; les **licences** de logiciel achetées vont en **2050000** ; les abonnements et la maintenance restent en charge.
- Les factures **communes** (locaux de Valence, assurance des locaux) sont saisies **au siège** (SIE) et réparties par IS selon les **m²** : SIE 15 %, SES 45 %, SAV 25 %, EMP 10 %, ASS 5 %. Comptes de liaison chez le siège : 1849100 SESSAD, 1849200 SAVS, 1849300 Emploi, 1849400 Association ; dans chaque structure : 1840000 Liaison Siège.
- Les fournisseurs sont des comptes de tiers **FO** (centralisés en 4010000, où l'on ne saisit jamais directement).

**Extrait de la liste des comptes de tiers fournisseurs existants** : FOBUREAU26, FOEDF, FOFERRAND, FOFONCIA, FOGARAGEMARTIN, FOINFORHONE, FOLUDIK, FOMAAF, FOORANGE, FOTOTALCARTE.

**Extrait du compte FOINFORHONE (livres du siège), au 16/11/2026**

| Date | Journal | Pièce | Libellé | Débit | Crédit | Lettrage |
|---|---|---|---|---|---|---|
| 18/09/2026 | AC | INF-2026-0917 | Info Rhône – maintenance parc T3 2026 | | 342,00 | A |
| 15/10/2026 | BQSIE | VIR-1015 | Virement Info Rhône INF-2026-0917 | 342,00 | | A |

## Les pièces

### Facture n° 1 — EDF (électricité des locaux communs)

```text
EDF – Électricité de France – Direction Commerce Entreprises Auvergne-Rhône-Alpes
SIREN 998 412 306 – TVA intracommunautaire FR23998412306

FACTURE N° 10 284 556 712                      Date d'émission : 02/11/2026
Nature de l'opération : livraison de biens (fourniture d'électricité)

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021            Compte client : 4 001 236 587
Site de consommation : 14 rue des Alpes 26000 Valence (locaux, 620 m²)
Point de livraison : 14 25 8 63 0 77 41 21

Période facturée : du 01/09/2026 au 31/10/2026 (index réels)

Désignation                                        Montant HT
Abonnement (2 mois)                                    164,60
Consommation heures pleines   6 820 kWh x 0,1385       944,57
Consommation heures creuses   3 140 kWh x 0,1102       346,03
Accise sur l'électricité      9 960 kWh                261,25
Contribution tarifaire d'acheminement (CTA)             28,44
                                                   ----------
Total HT                                             1 744,89
TVA 20 %                                               348,98
TOTAL TTC                                            2 093,87 €

Échéance : 23/11/2026 – paiement par virement
Pas d'escompte pour paiement anticipé.
Tout retard de paiement entraîne des pénalités égales à trois fois le taux
d'intérêt légal et une indemnité forfaitaire pour frais de recouvrement de 40 €.
```

*Tampon : « BON À PAYER – N. Berthier – 09/11/2026 – Commun Valence ».*

### Facture n° 2 — Bureau Vallée 26 (fournitures du SAVS)

```text
BUREAU VALLÉE 26 – SARL Papeteries de la Drôme
Zone commerciale des Couleures – 26000 Valence
SIREN 998 530 147 – RCS Romans – TVA FR78998530147

FACTURE N° BV26-F-118204                       Date : 27/10/2026
Nature de l'opération : livraison de biens
Votre commande : BC-SAV-2026-031 du 20/10/2026 (S. Laurent)

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021
Adresse de livraison : Cap Horizons 21 – SAVS – 14 rue des Alpes, 1er étage

Réf.      Désignation                        Qté   P.U. HT   Total HT
PAP480    Ramettes A4 80 g (carton de 5)       4     24,90      99,60
CLA080    Classeurs à levier dos 80 mm        20      2,95      59,00
HP305XL   Cartouches encre HP 305 XL noir      3     31,50      94,50
AGE27S    Agendas 2027 semainier               6      8,40      50,40
                                                            ---------
Total HT                                                       303,50
TVA 20 %                                                        60,70
TOTAL TTC                                                      364,20 €

Échéance : 30 jours date de facture, soit le 26/11/2026
Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €. Pas d'escompte.
```

*Tampon : « BON À PAYER – N. Berthier – 09/11/2026 – SAVS ». Bon de livraison signé par S. Laurent le 27/10/2026, conforme.*

### Facture n° 3 — Ludik Éducation (matériel éducatif du SESSAD)

```text
LUDIK ÉDUCATION SAS – 8 allée des Tisserands 69007 Lyon
SIREN 998 761 204 – TVA FR87998761204 – Capital 40 000 €

FACTURE N° LE-2026-04417                       Date : 29/10/2026
Nature de l'opération : livraison de biens

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021
Adresse de livraison : Cap Horizons 21 – SESSAD – 14 rue des Alpes, rez-de-chaussée

Désignation                                       Qté   P.U. HT   Total HT   TVA
Jeu « Émotions en images »                          2     34,90      69,80   20 %
Coffret pictogrammes communication (300 cartes)     1     89,00      89,00   20 %
Tablette sensorielle lumineuse 60 x 45 cm           1    324,00     324,00   20 %
Livre « Je lis avec les gestes » (FALC)             4     14,22      56,88   5,5 %
Frais de port                                       1     12,50      12,50   20 %

                         Base HT        TVA
TVA 20 %                  495,30      99,06
TVA 5,5 %                  56,88       3,13
Total HT                                          552,18
Total TVA                                         102,19
TOTAL TTC                                         654,37 €

Échéance : 28/11/2026. Pénalités : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

*Tampon : « BON À PAYER – N. Berthier – 09/11/2026 – SESSAD ». Bon de livraison du 03/11/2026 : « 1 jeu Émotions en images – boîte écrasée, retourné au transporteur ».*

### Facture n° 4 — Info Rhône Services (ordinateur du service emploi accompagné)

```text
INFO RHÔNE SERVICES SARL – 22 avenue Victor-Hugo 26000 Valence
SIREN 998 204 519 – TVA FR81998204519

FACTURE N° INF-2026-1102                       Date : 05/11/2026
Nature de l'opération : livraison de biens

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021
Adresse de livraison : Cap Horizons 21 – Emploi accompagné – 14 rue des Alpes, 2e étage
Devis accepté : DV-2026-0388 du 15/10/2026

Désignation                                         Qté   P.U. HT   Total HT
Ordinateur portable 14" – i5 – 16 Go – SSD 512 Go     1    749,17     749,17
  N° de série : PF4K2Z8M – garantie constructeur 2 ans
Souris sans fil                                       1     20,75      20,75
                                                               ---------
Total HT                                                         769,92
TVA 20 %                                                         153,98
TOTAL TTC                                                        923,90 €
  dont ordinateur 899,00 € TTC – souris 24,90 € TTC

Échéance : 05/12/2026. Pénalités : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

*Tampon : « BON À PAYER – N. Berthier – 10/11/2026 – Emploi accompagné ». Mise en service le 06/11/2026 (mail de Julie Marchetti).*

### Facture n° 5 — Logiplanning (logiciel de planning du SESSAD)

```text
LOGIPLANNING SAS – 5 rue de la République 38000 Grenoble
SIREN 998 377 150 – TVA FR91998377150

FACTURE N° LP-26-00731                         Date : 02/11/2026
Nature de l'opération : prestation de services et cession de licence

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021      Site utilisateur : SESSAD – 14 rue des Alpes
Bon de commande : BC-SES-2026-014 du 12/10/2026

Désignation                                                       Total HT
Licence perpétuelle « Logiplanning Pro » – 5 postes                1 200,00
  (droit d'utilisation sans limite de durée)
Contrat de maintenance et mises à jour – 12 mois                     360,00
  du 01/11/2026 au 31/10/2027
                                                                 ---------
Total HT                                                           1 560,00
TVA 20 %                                                             312,00
TOTAL TTC                                                          1 872,00 €

Échéance : 02/12/2026 – virement. Pénalités : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

*Tampon : « BON À PAYER – N. Berthier – 10/11/2026 – SESSAD ». Le logiciel est installé et utilisé depuis le 03/11/2026.*

### Facture n° 6 — Garage Martin (réparation du véhicule du SAVS)

```text
GARAGE MARTIN SARL – 140 route de Montélimar 26000 Valence
SIREN 998 640 832 – TVA FR05998640832 – Agent Renault

FACTURE N° GM-2026-1877                        Date : 28/10/2026
Nature de l'opération : prestation de services et livraison de pièces

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021
Véhicule : Renault Clio – GE-482-KL – 84 312 km (véhicule de service SAVS)

Désignation                                       Qté   P.U. HT   Total HT
Vidange + filtre à huile                            1     89,00      89,00
Plaquettes de frein avant (pièces)                  1     64,50      64,50
Main-d'œuvre freinage 1,2 h x 62,00                 1     74,40      74,40
Pneus 185/65 R15 posés et équilibrés                2     92,00     184,00
                                                               ---------
Total HT                                                         411,90
TVA 20 %                                                          82,38
TOTAL TTC                                                        494,28 €

Échéance : à réception. Pénalités : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

*Tampon : « BON À PAYER – N. Berthier – 09/11/2026 – SAVS ».*

### Facture n° 7 — Garage Martin (achat d'un véhicule pour le SESSAD)

```text
GARAGE MARTIN SARL – 140 route de Montélimar 26000 Valence
SIREN 998 640 832 – TVA FR05998640832

FACTURE N° GM-2026-1890                        Date : 30/10/2026
Nature de l'opération : livraison de biens

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021
Bon de commande signé le 06/10/2026 par N. Berthier (SESSAD)

Véhicule d'occasion : Peugeot Partner 1.5 BlueHDi – 5 places
Immatriculation : GT-915-RB – 1re mise en circulation 03/2023 – 38 400 km
Livraison : 05/11/2026

Désignation                                                       Montant
Véhicule (prix HT)                                               12 416,67
TVA 20 %                                                          2 483,33
Prix TTC du véhicule                                             14 900,00
Certificat d'immatriculation (taxe, hors champ de la TVA)           286,76
                                                                ---------
NET À PAYER                                                      15 186,76 €

Échéance : 30/11/2026. Pénalités : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

*Tampon : « BON À PAYER – N. Berthier – 10/11/2026 – SESSAD – investissement prévu à l'EPRD 2026 ». Le véhicule a été livré au SESSAD le 05/11/2026.*

### Facture n° 8 — MAAF (assurance multirisque des locaux)

```text
MAAF – Mutuelle d'assurance – Agence Valence Entreprises
SIREN 998 915 273 – Entreprise régie par le Code des assurances

AVIS D'ÉCHÉANCE ET FACTURE N° MA-2026-558120     Date : 20/10/2026
Contrat Multirisque Professionnels n° 7 412 559 K
Souscripteur : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN : 999 210 021
Risque assuré : locaux du 14 rue des Alpes 26000 Valence (620 m²)

Période de garantie : du 01/11/2026 au 31/10/2027

Prime nette annuelle                                               2 640,00
Taxe sur les conventions d'assurance (9 %)                           237,60
Contribution attentats et actes de terrorisme                          5,90
                                                                 ---------
TOTAL À PAYER                                                      2 883,50 €

Opération d'assurance exonérée de TVA.
À régler avant le 30/11/2026. À défaut de paiement, les garanties peuvent être
suspendues dans les conditions prévues par le Code des assurances.
```

*Tampon : « BON À PAYER – N. Berthier – 09/11/2026 – Commun Valence ».*

### Facture n° 9 — Ludik Éducation (avoir)

```text
LUDIK ÉDUCATION SAS – 8 allée des Tisserands 69007 Lyon
SIREN 998 761 204 – TVA FR87998761204

AVOIR N° AV-2026-0087                          Date : 09/11/2026
Sur facture n° LE-2026-04417 du 29/10/2026
Motif : article endommagé à la livraison, retourné le 03/11/2026

Client : Association Cap Horizons 21 – 14 rue des Alpes 26000 Valence
SIREN client : 999 210 021

Désignation                         Qté   P.U. HT   Total HT
Jeu « Émotions en images »            1     34,90      34,90
TVA 20 %                                                6,98
TOTAL AVOIR TTC                                        41,88 €

Montant à déduire de votre prochain règlement.
```

### Facture n° 10 — Info Rhône Services (reçue par courrier le 12/11/2026)

```text
INFO RHÔNE SERVICES SARL – 22 avenue Victor-Hugo 26000 Valence
SIREN 998 204 519 – TVA FR81998204519

FACTURE N° INF-2026-0917                       Date : 15/09/2026
Nature de l'opération : prestation de services

Client : Association Cap Horizon 21 – 41 rue des Alpes 26000 Valence

Désignation                                         Qté   P.U. HT   Total HT
Maintenance trimestrielle parc informatique         3     95,00     258,00
  (juillet, août, septembre 2026)
                                                               ---------
Total HT                                                         258,00
TVA 20 %                                                          51,60
TOTAL TTC                                                        309,60 €

Échéance : 15/10/2026. Pénalités : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

*Aucun tampon.*

## Travail à faire

1. Pour **chaque** pièce, faites le contrôle avant saisie : destinataire, mentions, calculs, doublon, conformité à la commande ou à la livraison, bon à payer. Concluez : **à saisir**, ou **à mettre en attente** (et pourquoi).
2. Pour chaque pièce à saisir, indiquez la **structure**, le **compte** (charge ou immobilisation), le **tiers** et le **code analytique**. Justifiez chaque choix « immobilisation ou charge ».
3. Passez les écritures au journal des achats (AC), avec, pour les factures communes, les **écritures miroirs** dans chaque structure. Vérifiez que chaque écriture est équilibrée.
4. Expliquez pourquoi on saisit **2 093,87 €** et non 1 744,89 € pour la facture EDF.
5. Factures n° 5 et n° 8 : quelle part concernera 2027 ? Calculez-la par structure, sans passer l'écriture (elle sera passée à la clôture), et notez-la dans votre liste de clôture.
6. Facture n° 10 : listez les anomalies et rédigez le message au fournisseur.
7. Quelles fiches faut-il créer dans **EIG IMMOS** (l'outil de suivi des immobilisations) ? Avec quelles informations ?
8. Facture n° 7 : quels contrôles supplémentaires faites-vous avant le virement du 20/11, vu le montant ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-02_corrige.md)
