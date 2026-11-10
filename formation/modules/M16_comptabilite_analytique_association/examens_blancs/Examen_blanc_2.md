# Examen blanc n° 2 — QCM agent comptable en association (15 questions, 20 minutes)

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **15059** | Cerfa n° 15059 — compte rendu financier. Le formulaire pour rendre compte de l'utilisation d'une subvention : budget prévu, dépenses réelles, écarts expliqués. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **98-COMMUN** | Section des charges communes à répartir. Même rôle que 00-COMMUN : section de passage vidée chaque mois vers les services. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **Cerfa** | Formulaire administratif officiel. Formulaire numéroté de l'administration (ex. : Cerfa 12156 pour demander une subvention). |
    | **CONCATENER** | Fonction Excel qui assemble des textes. Colle plusieurs cellules en un seul texte (ex. : fournisseur + numéro de facture pour repérer les doublons). |
    | **CPOM** | Contrat pluriannuel d'objectifs et de moyens. Contrat de 5 ans entre une association et l'ARS et/ou le Département : objectifs, moyens, et budget présenté en EPRD. |
    | **CRC** | Comité de la réglementation comptable. Ancien organisme de normalisation comptable, remplacé par l'ANC. Le règlement CRC 99-01 (comptes des associations) a été remplacé par le règlement ANC 2018-06. |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **NB.SI** | Fonction Excel de comptage avec condition. Compte les cellules qui respectent un critère ; NB.SI(...)>1 repère les doublons (ex. : un numéro de facture saisi deux fois). |
    | **QCM** | Questionnaire à choix multiples. Test avec plusieurs réponses proposées. |
    | **RECHERCHEX** | Fonction Excel de recherche moderne. Remplace RECHERCHEV : cherche une valeur dans une colonne et renvoie celle d'une autre colonne, à gauche ou à droite, en correspondance exacte par défaut. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SOMME.SI.ENS** | Fonction Excel de somme avec conditions. Additionne les montants qui respectent un ou plusieurs critères (ex. : total des factures de l'établissement de Nice en septembre). |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 401** | Fournisseurs. Ce que l'association doit à ses fournisseurs (factures reçues, pas encore payées). |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6132** | Locations immobilières. Loyer des locaux, location de salle. |
    | **Compte 6211** | Personnel intérimaire. Remplacement d'un salarié absent par une agence d'intérim (groupe II). |
    | **Compte 6226** | Honoraires. Expert-comptable, commissaire aux comptes, avocat. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 6411** | Salaires, appointements. Salaire brut de base. Les IJSS reçues en subrogation viennent en diminution. |
    | **Compte 10682** | Excédents affectés à l'investissement. Excédent d'un service mis de côté pour financer un investissement (véhicule, travaux). Plan des ESSMS. |
    | **Compte 10686** | Réserve de compensation des déficits. Excédent mis de côté pour couvrir un déficit futur du même service. Plan des ESSMS. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **contributions volontaires** | Aide gratuite reçue par l'association. Bénévolat, salle prêtée, dons en nature : on peut les valoriser en classe 8 (comptes 86 / 87). |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **groupe I** | Dépenses d'exploitation courante. Carburant, fournitures, alimentation, petit matériel. |
    | **groupe II** | Dépenses de personnel. Salaires, charges sociales, intérim, formation. |
    | **groupe III** | Dépenses de structure. Loyers, assurances, entretien, amortissements, frais de siège, intérêts. |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **Réserve de compensation** | Excédent mis de côté pour un futur déficit. Compte 10686 : si le service est en déficit plus tard, on puise dans cette réserve. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

**Conditions réelles :** 20 minutes, sans document, calculatrice simple tolérée, **une seule bonne réponse** par question.
1 point par bonne réponse → note sur 15. Gérez votre temps : environ 80 secondes par question, gardez les calculs pour la fin. Rappel : l'association fictive Cap Horizons 21 **ne récupère pas la TVA**.

👉 **Sur le site : touchez (ou cliquez) la réponse de votre choix** — elle s’entoure en bleu ; vous pouvez changer d’avis. Quand les 15 questions sont faites, descendez en bas de page et appuyez sur **« Corriger mon examen »**. Sur papier : notez vos réponses dans la grille en bas de page, puis ouvrez le [corrigé](Examen_blanc_2_corrige.md).

---

### Question 1 ★

Facture de carburant saisie : D 6061 186,40 / C 401 186,40. Sur quelle(s) ligne(s) saisit-on le code analytique ?

- **A)** Sur la ligne 401 uniquement
- **B)** Sur les deux lignes, 6061 et 401
- **C)** Sur aucune : l'analytique se tient dans un tableur à part
- **D)** Sur la ligne 6061 uniquement

### Question 2 ★★

En fin de mois, une OD analytique « vide » la section 98-COMMUN (loyer de 74 400,00 €, compte 6132) vers les sections des services, sur le même compte 6132. Effet sur le solde du compte 6132 en comptabilité générale :

- **A)** il augmente de 74 400,00 €
- **B)** il ne change pas : seule l'étiquette analytique change
- **C)** il diminue de 74 400,00 €
- **D)** il double, puis on extourne l'écriture en fin d'année

### Question 3 ★

Facture d'une agence d'intérim pour remplacer une orthophoniste du SESSAD en arrêt maladie. Codification :

- **A)** 6226 « Honoraires », groupe III, 10-SESSAD
- **B)** 6211 « Personnel intérimaire », groupe II, 10-SESSAD
- **C)** 6211 « Personnel intérimaire », groupe I, 01-SIEGE
- **D)** 6411 « Salaires, appointements », groupe II, 10-SESSAD

### Question 4 ★★★

Facture de carte carburant du véhicule 3, utilisé par le SESSAD et le SAVS : 620,00 € TTC pour le mois. Carnet de bord : 1 240 km pour le SESSAD, 310 km pour le SAVS. Imputation :

- **A)** 6061 : 310,00 € sur 10-SESSAD et 310,00 € sur 20-SAVS
- **B)** 6061 : 620,00 € sur 10-SESSAD (service du conducteur habituel)
- **C)** 6251 : 496,00 € sur 10-SESSAD et 124,00 € sur 20-SAVS
- **D)** 6061 : 496,00 € sur 10-SESSAD et 124,00 € sur 20-SAVS

### Question 5 ★

Pour répartir la téléphonie, l'informatique et le logiciel métier entre les services, Cap Horizons 21 retient :

- **A)** les m²
- **B)** les ETP
- **C)** les places autorisées
- **D)** le montant des dotations

### Question 6 ★★

Téléphonie : 8 820,00 € TTC par an, répartie selon la clé ETP. Effectif total : 29,4 ETP, dont SAVS 7,8 ETP. Part du SAVS :

- **A)** 2 340,00 €
- **B)** 1 260,00 €
- **C)** 2 205,00 €
- **D)** 2 520,00 €

### Question 7 ★

Dans le budget d'un ESSMS (SESSAD, SAVS), les frais de siège figurent dans :

- **A)** le groupe I — exploitation courante
- **B)** le groupe II — personnel
- **C)** le groupe III — structure
- **D)** aucun groupe : ils sont inscrits en classe 8

### Question 8 ★★

SESSAD : charges du groupe II (personnel) 924 000,00 € ; total des charges 1 180 000,00 €. Poids du personnel :

- **A)** 78,31 %
- **B)** 127,71 %
- **C)** 21,69 %
- **D)** 92,40 %

### Question 9 ★★

Groupe I du SESSAD : budget annuel 96 000,00 €. Réalisé au 30/09 : 70 100,00 €. Écart par rapport au budget au prorata (9/12) :

- **A)** − 25 900,00 €
- **B)** + 1 900,00 €, défavorable
- **C)** − 1 900,00 €, favorable
- **D)** − 1 900,00 €, défavorable

### Question 10 ★★★

Groupe II du SESSAD, réalisé au 30/09 : 712 400,00 €. Pour les 3 derniers mois, on retient un rythme de 76 255,56 € par mois hors intérim, plus 2 900,00 € d'intérim en octobre seulement (retour de l'orthophoniste le 1er novembre). Projection au 31/12 :

- **A)** 949 866,68 €
- **B)** 924 000,00 €
- **C)** 944 066,68 €
- **D)** 941 166,68 €

### Question 11 ★

Quel texte fixe les règles des comptes annuels des associations (fonds propres, fonds dédiés, contributions volontaires en nature) ?

- **A)** Le règlement ANC n° 2018-06
- **B)** Le règlement CRC n° 99-01, toujours applicable
- **C)** Le Code général des impôts
- **D)** L'instruction budgétaire M14 des communes

### Question 12 ★

Pour un gestionnaire qui a signé un CPOM avec l'ARS, le document budgétaire prévisionnel est :

- **A)** l'EPRD (état des prévisions de recettes et de dépenses)
- **B)** le compte administratif
- **C)** le Cerfa n° 15059
- **D)** le bilan

### Question 13 ★★

L'ERRD du SESSAD fait apparaître un excédent. La direction propose de le mettre de côté pour couvrir un éventuel déficit futur. Compte concerné (*subdivision selon le plan des ESSMS*) :

- **A)** 10682 « Excédents affectés à l'investissement »
- **B)** 10686 « Réserve de compensation des déficits »
- **C)** 19x « Fonds dédiés »
- **D)** 789 « Utilisation des fonds dédiés »

### Question 14 ★

Pourquoi Cap Horizons 21 paie-t-elle la taxe sur les salaires ?

- **A)** Parce qu'elle emploie plus de 11 salariés
- **B)** Parce qu'elle est financée par l'ARS
- **C)** Parce que la taxe remplace les cotisations patronales de sécurité sociale
- **D)** Parce qu'elle n'est pas soumise à la TVA sur l'essentiel de ses recettes

### Question 15 ★★

À partir d'un export du grand livre (colonnes : compte, code analytique, montant), quelle fonction Excel donne le total du compte 6061 pour le seul code 20-SAVS ?

- **A)** RECHERCHEX
- **B)** NB.SI
- **C)** CONCATENER
- **D)** SOMME.SI.ENS

---

## Ma grille de réponses

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

<div class="qcm-exam" data-answers="D,B,B,D,B,A,C,A,C,C,A,A,B,D,D" data-corrige="../Examen_blanc_2_corrige/"></div>
