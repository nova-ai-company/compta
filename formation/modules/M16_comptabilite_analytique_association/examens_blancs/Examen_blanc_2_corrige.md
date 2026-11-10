# Corrigé de l'examen blanc n° 2

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **15059** | Cerfa n° 15059 — compte rendu financier. Le formulaire pour rendre compte de l'utilisation d'une subvention : budget prévu, dépenses réelles, écarts expliqués. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **98-COMMUN** | Section des charges communes à répartir. Même rôle que 00-COMMUN : section de passage vidée chaque mois vers les services. |
    | **AAP** | Appel à projets. Le financeur décrit un besoin ; les associations répondent avec un projet et un budget. L'agent comptable chiffre la partie financière. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **BP** | Budget prévisionnel. Dans le médico-social : le budget qu'un service hors CPOM (ex. : le SAVS) présente à son financeur avant le 31 octobre de l'année précédente (à vérifier chaque année). |
    | **CA** | Chiffre d'affaires (ou journal de caisse, ou compte administratif). Le plus souvent : le total des ventes HT de l'année. Dans une liste de journaux, « CA » peut désigner le journal de caisse. Dans le médico-social (M16, M17), CA = compte administratif : le compte rendu annuel d'un service hors CPOM (ex. : le SAVS) remis au Département. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **Cerfa** | Formulaire administratif officiel. Formulaire numéroté de l'administration (ex. : Cerfa 12156 pour demander une subvention). |
    | **CONCATENER** | Fonction Excel qui assemble des textes. Colle plusieurs cellules en un seul texte (ex. : fournisseur + numéro de facture pour repérer les doublons). |
    | **CPOM** | Contrat pluriannuel d'objectifs et de moyens. Contrat de 5 ans entre une association et l'ARS et/ou le Département : objectifs, moyens, et budget présenté en EPRD. |
    | **CRC** | Comité de la réglementation comptable. Ancien organisme de normalisation comptable, remplacé par l'ANC. Le règlement CRC 99-01 (comptes des associations) a été remplacé par le règlement ANC 2018-06. |
    | **EPRD** | État des prévisions de recettes et de dépenses. Budget prévisionnel des gestionnaires sous CPOM. Il part de la ressource notifiée par le financeur (« budget par la recette »). Dépôt en général au 30 avril (à vérifier chaque année). |
    | **ERRD** | État réalisé des recettes et des dépenses. Le compte rendu de l'EPRD après la clôture : réalisé, écarts, proposition d'affectation du résultat. Dépôt en général au 30 avril N+1 (à vérifier). |
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
    | **Compte 411** | Clients / usagers. Ce que l'on doit à l'association. |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6132** | Locations immobilières. Loyer des locaux, location de salle. |
    | **Compte 6211** | Personnel intérimaire. Remplacement d'un salarié absent par une agence d'intérim (groupe II). |
    | **Compte 6226** | Honoraires. Expert-comptable, commissaire aux comptes, avocat. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 6311** | Taxe sur les salaires. Impôt payé par les employeurs non soumis à la TVA, comme l'association. |
    | **Compte 6411** | Salaires, appointements. Salaire brut de base. Les IJSS reçues en subrogation viennent en diminution. |
    | **Compte 10682** | Excédents affectés à l'investissement. Excédent d'un service mis de côté pour financer un investissement (véhicule, travaux). Plan des ESSMS. |
    | **Compte 10686** | Réserve de compensation des déficits. Excédent mis de côté pour couvrir un déficit futur du même service. Plan des ESSMS. |
    | **Clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **contributions volontaires** | Aide gratuite reçue par l'association. Bénévolat, salle prêtée, dons en nature : on peut les valoriser en classe 8 (comptes 86 / 87). |
    | **Coût complet** | Ce que coûte vraiment un service. Charges directes + part des charges communes + frais de siège. |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **Frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **groupe I** | Dépenses d'exploitation courante. Carburant, fournitures, alimentation, petit matériel. |
    | **groupe II** | Dépenses de personnel. Salaires, charges sociales, intérim, formation. |
    | **groupe III** | Dépenses de structure. Loyers, assurances, entretien, amortissements, frais de siège, intérêts. |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **Réserve de compensation** | Excédent mis de côté pour un futur déficit. Compte 10686 : si le service est en déficit plus tard, on puise dans cette réserve. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

Sujet : [Examen blanc n° 2](Examen_blanc_2.md)

## Grille des réponses

| Question | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Réponse | **D** | **B** | **B** | **D** | **B** | **A** | **C** | **A** | **C** | **C** | **A** | **A** | **B** | **D** | **D** |

## Explications

### Question 1 — réponse **D** · Analytique : principes et vocabulaire ★

??? note "Rappel de la question"

    Facture de carburant saisie : D 6061 186,40 / C 401 186,40. Sur quelle(s) ligne(s) saisit-on le code analytique ?
    
    - **A)** Sur la ligne 401 uniquement
    - **B)** Sur les deux lignes, 6061 et 401
    - **C)** Sur aucune : l'analytique se tient dans un tableur à part
    - **D)** Sur la ligne 6061 uniquement

**Réponse D** (Sur la ligne 6061 uniquement)  
Le code analytique se met sur les comptes de **charges et de produits** (classes 6 et 7). Les comptes de tiers (401, 411) et la banque n'en portent pas : un fournisseur n'« appartient » pas à un service, c'est la dépense qui lui appartient.

### Question 2 — réponse **B** · Analytique : principes et vocabulaire ★★

??? note "Rappel de la question"

    En fin de mois, une OD analytique « vide » la section 98-COMMUN (loyer de 74 400,00 €, compte 6132) vers les sections des services, sur le même compte 6132. Effet sur le solde du compte 6132 en comptabilité générale :
    
    - **A)** il augmente de 74 400,00 €
    - **B)** il ne change pas : seule l'étiquette analytique change
    - **C)** il diminue de 74 400,00 €
    - **D)** il double, puis on extourne l'écriture en fin d'année

**Réponse B** (il ne change pas : seule l'étiquette analytique change)  
L'OD analytique débite et crédite **le même compte** 6132 : le solde général est inchangé. Seule la répartition entre sections bouge (crédit sur 98-COMMUN, débits sur 10-SESSAD, 20-SAVS, 30-EMPLOI et 01-SIEGE).

### Question 3 — réponse **B** · Codifier une facture ★

??? note "Rappel de la question"

    Facture d'une agence d'intérim pour remplacer une orthophoniste du SESSAD en arrêt maladie. Codification :
    
    - **A)** 6226 « Honoraires », groupe III, 10-SESSAD
    - **B)** 6211 « Personnel intérimaire », groupe II, 10-SESSAD
    - **C)** 6211 « Personnel intérimaire », groupe I, 01-SIEGE
    - **D)** 6411 « Salaires, appointements », groupe II, 10-SESSAD

**Réponse B** (6211 « Personnel intérimaire », groupe II, 10-SESSAD)  
Le personnel extérieur (intérim) se comptabilise en **6211** et relève du **groupe II** (charges afférentes au personnel), sur le service qui en bénéficie. Le 6411 est réservé aux salaires des salariés de l'association ; ce n'est pas un honoraire.

### Question 4 — réponse **D** · Codifier une facture ★★★

??? note "Rappel de la question"

    Facture de carte carburant du véhicule 3, utilisé par le SESSAD et le SAVS : 620,00 € TTC pour le mois. Carnet de bord : 1 240 km pour le SESSAD, 310 km pour le SAVS. Imputation :
    
    - **A)** 6061 : 310,00 € sur 10-SESSAD et 310,00 € sur 20-SAVS
    - **B)** 6061 : 620,00 € sur 10-SESSAD (service du conducteur habituel)
    - **C)** 6251 : 496,00 € sur 10-SESSAD et 124,00 € sur 20-SAVS
    - **D)** 6061 : 496,00 € sur 10-SESSAD et 124,00 € sur 20-SAVS

**Réponse D** (6061 : 496,00 € sur 10-SESSAD et 124,00 € sur 20-SAVS)  
Clé kilomètres : total 1 550 km. SESSAD 1 240 / 1 550 = 80 % → 620,00 × 80 % = 496,00 € ; SAVS 20 % → 124,00 €. Le carburant est un achat non stocké (6061, groupe I) ; le 6251 sert aux voyages et déplacements (indemnités kilométriques, billets…).

### Question 5 — réponse **B** · Clés de répartition ★

??? note "Rappel de la question"

    Pour répartir la téléphonie, l'informatique et le logiciel métier entre les services, Cap Horizons 21 retient :
    
    - **A)** les m²
    - **B)** les ETP
    - **C)** les places autorisées
    - **D)** le montant des dotations

**Réponse B** (les ETP)  
Un poste de travail = un utilisateur : la clé **ETP** suit le nombre de personnes qui travaillent. Les m² servent pour les locaux, les kilomètres pour les véhicules, le temps passé pour les salariés partagés.

### Question 6 — réponse **A** · Clés de répartition ★★

??? note "Rappel de la question"

    Téléphonie : 8 820,00 € TTC par an, répartie selon la clé ETP. Effectif total : 29,4 ETP, dont SAVS 7,8 ETP. Part du SAVS :
    
    - **A)** 2 340,00 €
    - **B)** 1 260,00 €
    - **C)** 2 205,00 €
    - **D)** 2 520,00 €

**Réponse A** (2 340,00 €)  
8 820,00 / 29,4 = 300,00 € par ETP ; × 7,8 = 2 340,00 €. 1 260,00 € = partage égal entre 7 sections ; 2 205,00 € = partage égal entre 4 services.

### Question 7 — réponse **C** · Frais de siège ★

??? note "Rappel de la question"

    Dans le budget d'un ESSMS (SESSAD, SAVS), les frais de siège figurent dans :
    
    - **A)** le groupe I — exploitation courante
    - **B)** le groupe II — personnel
    - **C)** le groupe III — structure
    - **D)** aucun groupe : ils sont inscrits en classe 8

**Réponse C** (le groupe III — structure)  
Les frais de siège sont des charges de **structure** (groupe III), comme les loyers, les assurances et les amortissements. La classe 8 sert aux contributions volontaires en nature.

### Question 8 — réponse **A** · Coût complet et indicateurs ★★

??? note "Rappel de la question"

    SESSAD : charges du groupe II (personnel) 924 000,00 € ; total des charges 1 180 000,00 €. Poids du personnel :
    
    - **A)** 78,31 %
    - **B)** 127,71 %
    - **C)** 21,69 %
    - **D)** 92,40 %

**Réponse A** (78,31 %)  
924 000,00 / 1 180 000,00 = 78,31 %, dans la fourchette habituelle (75 à 85 %) d'un service d'accompagnement. 127,71 % est le rapport inversé ; 21,69 % est le poids des groupes I et III.

### Question 9 — réponse **C** · Suivi budgétaire et écarts ★★

??? note "Rappel de la question"

    Groupe I du SESSAD : budget annuel 96 000,00 €. Réalisé au 30/09 : 70 100,00 €. Écart par rapport au budget au prorata (9/12) :
    
    - **A)** − 25 900,00 €
    - **B)** + 1 900,00 €, défavorable
    - **C)** − 1 900,00 €, favorable
    - **D)** − 1 900,00 €, défavorable

**Réponse C** (− 1 900,00 €, favorable)  
Budget au prorata : 96 000,00 × 9/12 = 72 000,00 €. Écart : 70 100,00 − 72 000,00 = − 1 900,00 € (− 2,6 %) : on a dépensé moins que prévu, écart **favorable** sur une charge. − 25 900,00 € compare le réalisé de 9 mois au budget de 12 mois.

### Question 10 — réponse **C** · Suivi budgétaire et écarts ★★★

??? note "Rappel de la question"

    Groupe II du SESSAD, réalisé au 30/09 : 712 400,00 €. Pour les 3 derniers mois, on retient un rythme de 76 255,56 € par mois hors intérim, plus 2 900,00 € d'intérim en octobre seulement (retour de l'orthophoniste le 1er novembre). Projection au 31/12 :
    
    - **A)** 949 866,68 €
    - **B)** 924 000,00 €
    - **C)** 944 066,68 €
    - **D)** 941 166,68 €

**Réponse C** (944 066,68 €)  
712 400,00 + 3 × 76 255,56 + 2 900,00 = 944 066,68 €, soit environ 20 000 € au-dessus du budget de 924 000,00 €. 949 866,68 € prolonge l'intérim sur 3 mois ; 941 166,68 € l'oublie en octobre ; 924 000,00 € suppose que le reste du budget sera exactement consommé, ce qui n'est pas une projection.

### Question 11 — réponse **A** · Subventions, fonds dédiés et contributions volontaires ★

??? note "Rappel de la question"

    Quel texte fixe les règles des comptes annuels des associations (fonds propres, fonds dédiés, contributions volontaires en nature) ?
    
    - **A)** Le règlement ANC n° 2018-06
    - **B)** Le règlement CRC n° 99-01, toujours applicable
    - **C)** Le Code général des impôts
    - **D)** L'instruction budgétaire M14 des communes

**Réponse A** (Le règlement ANC n° 2018-06)  
Le **règlement ANC n° 2018-06** s'applique aux personnes morales de droit privé à but non lucratif ; il a remplacé l'ancien règlement CRC 99-01. Pour les ESSMS, il se combine avec le plan comptable et le cadre budgétaire des ESSMS (CASF).

### Question 12 — réponse **A** · Secteur médico-social ★

??? note "Rappel de la question"

    Pour un gestionnaire qui a signé un CPOM avec l'ARS, le document budgétaire prévisionnel est :
    
    - **A)** l'EPRD (état des prévisions de recettes et de dépenses)
    - **B)** le compte administratif
    - **C)** le Cerfa n° 15059
    - **D)** le bilan

**Réponse A** (l'EPRD (état des prévisions de recettes et de dépenses))  
Sous CPOM : **EPRD** (prévisionnel), puis **ERRD** (réalisé). Hors CPOM : budget prévisionnel (BP) puis **compte administratif** (CA). Le Cerfa n° 15059 est le compte rendu financier d'une subvention.

### Question 13 — réponse **B** · Secteur médico-social ★★

??? note "Rappel de la question"

    L'ERRD du SESSAD fait apparaître un excédent. La direction propose de le mettre de côté pour couvrir un éventuel déficit futur. Compte concerné (*subdivision selon le plan des ESSMS*) :
    
    - **A)** 10682 « Excédents affectés à l'investissement »
    - **B)** 10686 « Réserve de compensation des déficits »
    - **C)** 19x « Fonds dédiés »
    - **D)** 789 « Utilisation des fonds dédiés »

**Réponse B** (10686 « Réserve de compensation des déficits »)  
La **réserve de compensation des déficits** (10686) sert à absorber un déficit ultérieur. Le 10682 finance des investissements. Les fonds dédiés concernent des ressources affectées par un tiers, pas l'affectation du résultat.

### Question 14 — réponse **D** · Paie, charges sociales et frais ★

??? note "Rappel de la question"

    Pourquoi Cap Horizons 21 paie-t-elle la taxe sur les salaires ?
    
    - **A)** Parce qu'elle emploie plus de 11 salariés
    - **B)** Parce qu'elle est financée par l'ARS
    - **C)** Parce que la taxe remplace les cotisations patronales de sécurité sociale
    - **D)** Parce qu'elle n'est pas soumise à la TVA sur l'essentiel de ses recettes

**Réponse D** (Parce qu'elle n'est pas soumise à la TVA sur l'essentiel de ses recettes)  
La taxe sur les salaires est due par les employeurs **non soumis à la TVA** (ou soumis sur moins de 90 % de leur chiffre d'affaires). Compte **6311**, groupe II. Les associations bénéficient d'un abattement annuel. *Barème, seuils et abattement : valeurs à vérifier chaque année.*

### Question 15 — réponse **D** · Trésorerie, contrôle interne, AAP et Excel ★★

??? note "Rappel de la question"

    À partir d'un export du grand livre (colonnes : compte, code analytique, montant), quelle fonction Excel donne le total du compte 6061 pour le seul code 20-SAVS ?
    
    - **A)** RECHERCHEX
    - **B)** NB.SI
    - **C)** CONCATENER
    - **D)** SOMME.SI.ENS

**Réponse D** (SOMME.SI.ENS)  
SOMME.SI.ENS(montants ; comptes ; "6061" ; codes ; "20-SAVS") additionne selon **plusieurs critères**. RECHERCHEX renvoie une valeur trouvée (un libellé), NB.SI compte des lignes. Un tableau croisé dynamique (comptes en lignes, codes en colonnes) donne le même résultat pour tous les comptes à la fois.

## Barème et interprétation de votre score

1 point par bonne réponse, 0 pour une réponse fausse ou absente → note sur 15.

| Score | Lecture |
|---|---|
| 14-15 | Excellent : le test écrit ne devrait pas vous poser de difficulté. |
| 11-13 | Bon niveau : relisez les explications des questions manquées. |
| 0-10 | À revoir : reprenez la banque de QCM par thème (`QCM_reponses.md`) avant de repasser un examen blanc. |
