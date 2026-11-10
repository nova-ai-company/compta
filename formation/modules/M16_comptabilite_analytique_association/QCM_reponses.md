# M16 — Corrigé de la banque de QCM (analytique, budgets et gestion en association)

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **12156** | Cerfa n° 12156 — demande de subvention. Le formulaire officiel pour demander une subvention à l'État, une collectivité ou un organisme public. Il contient le budget prévisionnel du projet. |
    | **15059** | Cerfa n° 15059 — compte rendu financier. Le formulaire pour rendre compte de l'utilisation d'une subvention : budget prévu, dépenses réelles, écarts expliqués. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **98-COMMUN** | Section des charges communes à répartir. Même rôle que 00-COMMUN : section de passage vidée chaque mois vers les services. |
    | **AAP** | Appel à projets. Le financeur décrit un besoin ; les associations répondent avec un projet et un budget. L'agent comptable chiffre la partie financière. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **BP** | Budget prévisionnel. Dans le médico-social : le budget qu'un service hors CPOM (ex. : le SAVS) présente à son financeur avant le 31 octobre de l'année précédente (à vérifier chaque année). |
    | **CA** | Chiffre d'affaires (ou journal de caisse, ou compte administratif). Le plus souvent : le total des ventes HT de l'année. Dans une liste de journaux, « CA » peut désigner le journal de caisse. Dans le médico-social (M16, M17), CA = compte administratif : le compte rendu annuel d'un service hors CPOM (ex. : le SAVS) remis au Département. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **Cerfa** | Formulaire administratif officiel. Formulaire numéroté de l'administration (ex. : Cerfa 12156 pour demander une subvention). |
    | **CNSA** | Caisse nationale de solidarité pour l'autonomie. Finance l'aide à l'autonomie (personnes âgées, handicap). L'EPRD et l'ERRD sont déposés sur sa plateforme. |
    | **CPOM** | Contrat pluriannuel d'objectifs et de moyens. Contrat de 5 ans entre une association et l'ARS et/ou le Département : objectifs, moyens, et budget présenté en EPRD. |
    | **CRC** | Comité de la réglementation comptable. Ancien organisme de normalisation comptable, remplacé par l'ANC. Le règlement CRC 99-01 (comptes des associations) a été remplacé par le règlement ANC 2018-06. |
    | **EPRD** | État des prévisions de recettes et de dépenses. Budget prévisionnel des gestionnaires sous CPOM. Il part de la ressource notifiée par le financeur (« budget par la recette »). Dépôt en général au 30 avril (à vérifier chaque année). |
    | **ERRD** | État réalisé des recettes et des dépenses. Le compte rendu de l'EPRD après la clôture : réalisé, écarts, proposition d'affectation du résultat. Dépôt en général au 30 avril N+1 (à vérifier). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **N+1** | L'exercice suivant. L'année comptable d'après (ex. : si N = 2026, N+1 = 2027). Une charge « de N+1 » ne doit pas peser sur le résultat de N. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
    | **NB.SI** | Fonction Excel de comptage avec condition. Compte les cellules qui respectent un critère ; NB.SI(...)>1 repère les doublons (ex. : un numéro de facture saisi deux fois). |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **QCM** | Questionnaire à choix multiples. Test avec plusieurs réponses proposées. |
    | **RECHERCHEX** | Fonction Excel de recherche moderne. Remplace RECHERCHEV : cherche une valeur dans une colonne et renvoie celle d'une autre colonne, à gauche ou à droite, en correspondance exacte par défaut. |
    | **RIB** | Relevé d'identité bancaire. Document qui donne les coordonnées bancaires (IBAN, BIC) d'un compte. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SOMME.SI.ENS** | Fonction Excel de somme avec conditions. Additionne les montants qui respectent un ou plusieurs critères (ex. : total des factures de l'établissement de Nice en septembre). |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 401** | Fournisseurs. Ce que l'association doit à ses fournisseurs (factures reçues, pas encore payées). |
    | **Compte 404** | Fournisseurs d'immobilisations. Dettes envers un fournisseur pour un bien durable (véhicule, ordinateur). |
    | **Compte 408** | Fournisseurs. Factures non parvenues (FNP) : charge de l'année dont la facture n'est pas encore arrivée. |
    | **Compte 411** | Clients / usagers. Ce que l'on doit à l'association. |
    | **Compte 487** | Produits constatés d'avance (PCA). Recette reçue cette année qui concerne l'année suivante. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 616** | Primes d'assurances. Assurance des locaux, des véhicules, responsabilité civile. Pas de TVA. |
    | **Compte 641x** | Rémunérations du personnel (sous-comptes). Salaires, congés payés, indemnités. |
    | **Compte 689** | Reports en fonds dédiés. On « met de côté » à la clôture la part d'une subvention affectée non encore dépensée. |
    | **Compte 789** | Utilisation des fonds dédiés. L'année où la subvention mise de côté est dépensée, on la « reprend » en produit. |
    | **Compte 2183** | Matériel de bureau et informatique. Ordinateurs, imprimantes : un bien durable, amorti sur plusieurs années. |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6064** | Fournitures administratives. Papier, stylos, cartouches. |
    | **Compte 6132** | Locations immobilières. Loyer des locaux, location de salle. |
    | **Compte 6211** | Personnel intérimaire. Remplacement d'un salarié absent par une agence d'intérim (groupe II). |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 6311** | Taxe sur les salaires. Impôt payé par les employeurs non soumis à la TVA, comme l'association. |
    | **Compte 6411** | Salaires, appointements. Salaire brut de base. Les IJSS reçues en subrogation viennent en diminution. |
    | **Compte 6811** | Dotations aux amortissements. L'usure annuelle des biens durables (véhicules, ordinateurs). |
    | **Compte 7351** | Produits de la tarification. Dotation globale versée par l'ARS ou le Département (numéro selon le plan des ESSMS). |
    | **Compte 10682** | Excédents affectés à l'investissement. Excédent d'un service mis de côté pour financer un investissement (véhicule, travaux). Plan des ESSMS. |
    | **Compte 10686** | Réserve de compensation des déficits. Excédent mis de côté pour couvrir un déficit futur du même service. Plan des ESSMS. |
    | **Compte 44566** | TVA déductible sur autres biens et services. Sans objet pour l'association : chez elle, la TVA est une charge. |
    | **charge commune** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **charge directe** | Charge qui concerne un seul service. On sait tout de suite à quel service l'imputer (ex. : le matériel pédagogique du SESSAD). |
    | **Clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **contributions volontaires** | Aide gratuite reçue par l'association. Bénévolat, salle prêtée, dons en nature : on peut les valoriser en classe 8 (comptes 86 / 87). |
    | **Coût complet** | Ce que coûte vraiment un service. Charges directes + part des charges communes + frais de siège. |
    | **crédits non reconductibles** | Financement ponctuel (CNR). Somme accordée une seule fois par l'ARS pour une dépense exceptionnelle ; elle n'est pas renouvelée l'année suivante. |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **groupe I** | Dépenses d'exploitation courante. Carburant, fournitures, alimentation, petit matériel. |
    | **groupe II** | Dépenses de personnel. Salaires, charges sociales, intérim, formation. |
    | **groupe III** | Dépenses de structure. Loyers, assurances, entretien, amortissements, frais de siège, intérêts. |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **plan de trésorerie** | Prévoir l'argent en banque mois par mois. Solde de début + encaissements − décaissements = solde de fin, sur 6 à 12 mois. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **Réserve de compensation** | Excédent mis de côté pour un futur déficit. Compte 10686 : si le service est en déficit plus tard, on puise dans cette réserve. |
    | **section d'attente** | Section analytique provisoire. Pour les charges dont on ne connaît pas encore le service. Elle doit être vide à la clôture. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

*Fichier de correction : à n'ouvrir qu'après avoir répondu aux questions de `QCM_questions.md`. Référentiel : exercice 2026, PCG 2025 et règlement ANC 2018-06. Association fictive : Cap Horizons 21. Les valeurs signalées « à vérifier » évoluent chaque année.*

## Grille rapide des réponses

- **A** : Q001 B · Q002 D · Q003 A · Q004 C · Q005 B · Q006 D
- **B** : Q007 C · Q008 B · Q009 D · Q010 C · Q011 A · Q012 B · Q013 D
- **C** : Q014 C · Q015 B · Q016 D · Q017 A · Q018 C · Q019 B · Q020 A
- **D** : Q021 C · Q022 B · Q023 D · Q024 C · Q025 A
- **E** : Q026 A · Q027 B · Q028 C · Q029 A · Q030 D · Q031 A
- **F** : Q032 B · Q033 C · Q034 D · Q035 A · Q036 C · Q037 B
- **G** : Q038 A · Q039 D · Q040 B · Q041 A · Q042 C · Q043 D
- **H** : Q044 D · Q045 A · Q046 D · Q047 C · Q048 B · Q049 A · Q050 C
- **I** : Q051 D · Q052 B · Q053 A · Q054 C · Q055 B
- **J** : Q056 A · Q057 D · Q058 C · Q059 B · Q060 D

---

## A. Analytique : principes et vocabulaire

**Q001 — Réponse B** (« Pour quel service, dispositif ou projet cette dépense a-t-elle été faite ? »)  
La comptabilité générale dit « **quoi** » (le compte : 6061 carburant, 6132 loyer…) ; l'analytique dit « **pour qui** » (10-SESSAD, 20-SAVS, 50-PAIRS…). L'échéance relève du suivi fournisseurs, et l'association ne récupère pas la TVA.

**Q002 — Réponse D** (Sur la ligne 6061 uniquement)  
Le code analytique se met sur les comptes de **charges et de produits** (classes 6 et 7). Les comptes de tiers (401, 411) et la banque n'en portent pas : un fournisseur n'« appartient » pas à un service, c'est la dépense qui lui appartient.

**Q003 — Réponse A** (une charge directe du SESSAD (10-SESSAD))  
On sait tout de suite à quel service la dépense appartient : c'est une **charge directe**. On ne répartit avec une clé que les charges **communes** (loyer, téléphonie, véhicules partagés…).

**Q004 — Réponse C** (Retrouver chaque pièce, l'imputer sur le bon service ou la répartir avec la bonne clé, pour que la section soit vide)  
La section d'attente doit être **vide** à la clôture. Une répartition « forfaitaire » ou un transfert au siège ferait payer à un financeur des charges qui ne le concernent peut-être pas (risque de charges refusées). Le bon réflexe est de la vider **chaque mois**, quand on se souvient encore de chaque pièce.

**Q005 — Réponse B** (il ne change pas : seule l'étiquette analytique change)  
L'OD analytique débite et crédite **le même compte** 6132 : le solde général est inchangé. Seule la répartition entre sections bouge (crédit sur 98-COMMUN, débits sur 10-SESSAD, 20-SAVS, 30-EMPLOI et 01-SIEGE).

**Q006 — Réponse D** (égal au total des charges de la comptabilité générale)  
L'analytique est une **étiquette** posée sur les lignes de charges : son total doit être égal au total des comptes de classe 6. Les frais de siège répartis par OD analytique débitent les services et créditent la section siège : ils ne changent pas le total. Un écart signale une ligne sans code ou une OD déséquilibrée.

---

## B. Codifier une facture

**Q007 — Réponse C** (D 6064 180,00 / C 401 180,00)  
L'association ne récupère pas la TVA : la TVA payée est une **charge**, on saisit la charge **TTC** (180,00 €). Le compte 44566 est le réflexe d'une entreprise commerciale : c'est le piège n° 1. La dette envers le fournisseur est toujours le TTC.

**Q008 — Réponse B** (6211 « Personnel intérimaire », groupe II, 10-SESSAD)  
Le personnel extérieur (intérim) se comptabilise en **6211** et relève du **groupe II** (charges afférentes au personnel), sur le service qui en bénéficie. Le 6411 est réservé aux salaires des salariés de l'association ; ce n'est pas un honoraire.

**Q009 — Réponse D** (D 2183 1 100,00 / C 404 1 100,00)  
Un matériel durable au-dessus du seuil est une **immobilisation** (2183, fournisseur d'immobilisations 404). Le coût d'acquisition comprend les taxes **non récupérables** : chez un non-assujetti, on immobilise le **TTC**. La charge annuelle passera par l'amortissement (6811, groupe III), sur le code 20-SAVS.

**Q010 — Réponse C** (Groupe III — structure)  
Le **groupe III** regroupe les charges de **structure** : loyers, entretien, assurances, amortissements, frais de siège, frais financiers. Rappel : il n'y a pas de TVA sur une prime d'assurance (compte 616), et la charge commune se répartit selon la clé m².

**Q011 — Réponse A** (Ne pas la saisir comme facture de l'association : la traiter en note de frais de l'éducatrice (justificatif, liste des participants, visa du chef de service), ou demander une facture au nom de l'association)  
Une facture au nom d'une salariée n'est pas une facture de l'association. Si la dépense est bien liée au service, on la rembourse **en note de frais**, avec le ticket, la liste des participants et le visa du chef de service. Refuser de rembourser une dépense de service faite de bonne foi n'est pas la bonne réponse.

**Q012 — Réponse B** (D 408 1 240,00 / C 401 1 240,00)  
La charge est déjà dans l'exercice 2025 (via le 408). À réception de la facture, on **solde le 408** et on crée la dette fournisseur. Passer à nouveau un 6061 compterait la charge deux fois (une fois en 2025, une fois en 2026). Si la charge à payer avait été extournée au 01/01, on passerait D 6061 / C 401.

**Q013 — Réponse D** (6061 : 496,00 € sur 10-SESSAD et 124,00 € sur 20-SAVS)  
Clé kilomètres : total 1 550 km. SESSAD 1 240 / 1 550 = 80 % → 620,00 × 80 % = 496,00 € ; SAVS 20 % → 124,00 €. Le carburant est un achat non stocké (6061, groupe I) ; le 6251 sert aux voyages et déplacements (indemnités kilométriques, billets…).

---

## C. Clés de répartition

**Q014 — Réponse C** (Les m² occupés par chaque service)  
Le loyer dépend de la **surface** : clé **m²**. Une bonne clé est juste (elle suit ce qui fait varier la charge), simple (calculable chaque mois) et justifiable (on peut la montrer au financeur).

**Q015 — Réponse B** (les ETP)  
Un poste de travail = un utilisateur : la clé **ETP** suit le nombre de personnes qui travaillent. Les m² servent pour les locaux, les kilomètres pour les véhicules, le temps passé pour les salariés partagés.

**Q016 — Réponse D** (20 176,27 €)  
74 400,00 × 160 / 590 = 20 176,27 €. 19 200,00 € correspond à une division par 620 m² (salle commune oubliée dans la répartition) ; 18 600,00 € à un partage égal entre 4 services ; 11 349,16 € est la part du siège (90 m²).

**Q017 — Réponse A** (2 340,00 €)  
8 820,00 / 29,4 = 300,00 € par ETP ; × 7,8 = 2 340,00 €. 1 260,00 € = partage égal entre 7 sections ; 2 205,00 € = partage égal entre 4 services.

**Q018 — Réponse C** (Le planning ou le relevé d'heures signé qui montre le temps passé dans chaque service)  
Pour un salarié partagé, la clé est le **temps passé**, et la preuve est un **planning** ou un **relevé d'heures** signé (ou un avenant au contrat). Ici : SESSAD 34 800,00 €, SAVS 23 200,00 €. Si la répartition réelle change, on met la clé à jour.

**Q019 — Réponse B** (11 000,00 €)  
Total : 1 600 heures. Emploi : 400 / 1 600 = 25 % → 44 000,00 × 25 % = 11 000,00 €. Le piège : 400 / 1 200 (diviser par les heures de l'autre service, 14 666,67 €). 33 000,00 € est la part du SAVS ; 22 000,00 € un partage 50/50 sans fondement.

**Q020 — Réponse A** (Les services paient deux fois le loyer du siège)  
Double imputation : la part du siège est déjà dans le coût du siège, financé par les frais de siège. La répartir une seconde fois sur les services gonfle leurs charges, et l'autorité de tarification peut refuser l'excédent.

---

## D. Frais de siège

**Q021 — Réponse C** (le groupe III — structure)  
Les frais de siège sont des charges de **structure** (groupe III), comme les loyers, les assurances et les amortissements. La classe 8 sert aux contributions volontaires en nature.

**Q022 — Réponse B** (50 850,00 €)  
1 130 000,00 × 4,5 % = 50 850,00 €. 53 100,00 € applique le taux à 1 180 000,00 €, c'est-à-dire à une base qui contient déjà les frais de siège (le siège se facturerait sur lui-même). 45 200,00 € = taux de 4 % ; 5 085,00 € = erreur de virgule.

**Q023 — Réponse D** (81 610,00 €)  
Frais de siège ESSMS : 50 850,00 + 27 540,00 = 78 390,00 €. Reste : 160 000,00 − 78 390,00 = 81 610,00 €, à couvrir par les quotes-parts acceptées par les conventions des autres dispositifs et par les ressources propres. Un siège en déficit chronique doit être signalé à la direction.

**Q024 — Réponse C** (Oui, si le financeur l'accepte dans le budget de la convention ; sinon ce coût reste à la charge des ressources propres de l'association)  
L'autorisation de frais de siège vaut pour les **ESSMS**. Pour un projet ou un dispositif financé par convention, c'est le **financeur** qui décide : il faut prévoir la ligne (frais de structure ou de gestion) dans le budget présenté, et le justifier.

**Q025 — Réponse A** (L'autorité de tarification (ARS, Département), selon la procédure prévue par le Code de l'action sociale et des familles)  
Les frais de siège des ESSMS doivent être **autorisés** par l'autorité de tarification, en général pour 5 ans, avec un taux ou un montant. Le CAC certifie les comptes ; il n'autorise pas de financement.

---

## E. Coût complet et indicateurs

**Q026 — Réponse A** (ses charges directes + sa part des charges communes + sa quote-part de frais de siège)  
Construction en cascade : charges **directes** → + charges **communes** réparties = coût de production (base des frais de siège) → + **frais de siège** = **coût complet**. Charges moins produits, c'est le résultat, pas un coût.

**Q027 — Réponse B** (10 666,67 €)  
640 000,00 / 60 = 10 666,67 € par place. 8 888,89 € est le coût par **personne accompagnée** (640 000,00 / 72) ; 10 200,00 € oublie les frais de siège (612 000,00 / 60). Annoncez toujours ce que contient votre coût.

**Q028 — Réponse C** (65,31 €)  
640 000,00 / 9 800 = 65,31 €. 62,45 € est calculé sur 612 000,00 € (sans les frais de siège). Ce type d'indicateur sert à chiffrer une réponse à un appel à projets.

**Q029 — Réponse A** (78,31 %)  
924 000,00 / 1 180 000,00 = 78,31 %, dans la fourchette habituelle (75 à 85 %) d'un service d'accompagnement. 127,71 % est le rapport inversé ; 21,69 % est le poids des groupes I et III.

**Q030 — Réponse D** (91,11 %)  
Places occupées / places autorisées : 41 / 45 = 91,11 %. 109,76 % est le rapport inversé ; 8,89 % est le taux d'inoccupation. L'ARS surveille la sous-activité : un taux faible durable peut conduire à revoir la dotation.

**Q031 — Réponse A** (47 jours)  
Charges décaissables par jour : 2 350 000,00 / 365 = 6 438,36 €. Jours de trésorerie : 300 000,00 / 6 438,36 = 46,6, soit environ **47 jours** : l'association tient un mois et demi sans aucune recette. 8 jours vient du rapport inversé 2 350 000 / 300 000 (7,8).

---

## F. Suivi budgétaire et écarts

**Q032 — Réponse B** (défavorable : on a dépensé plus que prévu)  
Sur une charge, réalisé > budget = **dépassement** = écart défavorable. Sur un produit, c'est l'inverse (plus de recettes que prévu = favorable). Un écart n'est pas une erreur : il faut l'**expliquer**.

**Q033 — Réponse C** (− 1 900,00 €, favorable)  
Budget au prorata : 96 000,00 × 9/12 = 72 000,00 €. Écart : 70 100,00 − 72 000,00 = − 1 900,00 € (− 2,6 %) : on a dépensé moins que prévu, écart **favorable** sur une charge. − 25 900,00 € compare le réalisé de 9 mois au budget de 12 mois.

**Q034 — Réponse D** (+ 2,80 %)  
Budget au prorata : 924 000,00 × 9/12 = 693 000,00 €. Écart : 712 400,00 − 693 000,00 = + 19 400,00 €, soit 19 400 / 693 000 = + 2,80 % (défavorable). + 2,10 % rapporte l'écart au budget annuel au lieu du budget au prorata.

**Q035 — Réponse A** (Parce que certaines dépenses ne sont pas régulières (congés d'été, prime versée en décembre, assurance payée en janvier) : un budget mensualisé est plus fiable)  
Le prorata suppose des dépenses régulières. Une assurance payée en janvier fait paraître le groupe III en dépassement en début d'année ; une prime de décembre fait paraître le groupe II sous-consommé au 30/09. Quand c'est possible, on compare à un **budget mensualisé**.

**Q036 — Réponse C** (944 066,68 €)  
712 400,00 + 3 × 76 255,56 + 2 900,00 = 944 066,68 €, soit environ 20 000 € au-dessus du budget de 924 000,00 €. 949 866,68 € prolonge l'intérim sur 3 mois ; 941 166,68 € l'oublie en octobre ; 924 000,00 € suppose que le reste du budget sera exactement consommé, ce qui n'est pas une projection.

**Q037 — Réponse B** (Une page : un chiffre, une cause, une piste d'action)  
La directrice doit pouvoir décider vite : **un chiffre** (l'écart et la projection), **une cause** (l'intérim de remplacement), **une piste** (demander des crédits non reconductibles, reporter un achat). Attendre la clôture, c'est prévenir trop tard.

---

## G. Subventions, fonds dédiés et contributions volontaires

**Q038 — Réponse A** (Le règlement ANC n° 2018-06)  
Le **règlement ANC n° 2018-06** s'applique aux personnes morales de droit privé à but non lucratif ; il a remplacé l'ancien règlement CRC 99-01. Pour les ESSMS, il se combine avec le plan comptable et le cadre budgétaire des ESSMS (CASF).

**Q039 — Réponse D** (D 689 8 000,00 / C 19x 8 000,00)  
La part non utilisée d'une subvention **affectée** est mise en **fonds dédiés** : charge 689 « Reports en fonds dédiés » au débit, passif 19x au crédit, code 50-PAIRS. Le produit constaté d'avance (487) concerne une subvention relative à une période future, pas la partie non consommée d'un projet en cours. Le 789 sert l'année où les fonds sont utilisés.

**Q040 — Réponse B** (11 000,00 €)  
Dépenses réelles du projet : 30 000,00 + 45 000,00 × 20 % = 30 000,00 + 9 000,00 = 39 000,00 €. Fonds dédiés : 50 000,00 − 39 000,00 = 11 000,00 €. Oublier la quote-part de salaire donne 20 000,00 € : le projet paraît sous-consommé et on reporte trop. D'où l'importance d'une analytique juste, salaires compris.

**Q041 — Réponse A** (D 19x 8 000,00 / C 789 8 000,00)  
Quand les fonds sont utilisés, on solde le passif (19x au débit) et on constate un produit **789 « Utilisation des fonds dédiés »** qui équilibre les charges de l'année. Les dépenses elles-mêmes ont été payées normalement (401 / 512) : le fonds dédié ne se paie pas.

**Q042 — Réponse C** (En contributions volontaires en nature, classe 8 (86 emplois / 87 contributions), en pied du compte de résultat)  
Le bénévolat valorisé figure en **classe 8** (comptes 86 / 87, qui s'équilibrent), en pied de compte de résultat, si l'association dispose d'une méthode fiable (heures relevées, taux justifié). Il ne passe ni en charges de personnel ni au bilan. C'est un bon argument auprès des financeurs : leur euro produit plus qu'un euro d'action.

**Q043 — Réponse D** (Une contribution volontaire en nature (mise à disposition gratuite), valorisée en classe 8 si la valorisation est fiable, et décrite dans l'annexe)  
Une mise à disposition gratuite est une **contribution volontaire en nature** : comptes 86 / 87 en pied de compte de résultat (ou information en annexe si la valorisation n'est pas fiable). Elle a sa ligne dans le budget du Cerfa n° 12156 et le compte rendu du Cerfa n° 15059.

---

## H. Secteur médico-social

**Q044 — Réponse D** (L'ARS (Agence régionale de santé))  
Le SESSAD (enfants, soins et éducation spécialisée) relève de l'**ARS**, par une dotation globale sous **CPOM**. Le SAVS (adultes, vie sociale) relève du **Conseil départemental**.

**Q045 — Réponse A** (l'EPRD (état des prévisions de recettes et de dépenses))  
Sous CPOM : **EPRD** (prévisionnel), puis **ERRD** (réalisé). Hors CPOM : budget prévisionnel (BP) puis **compte administratif** (CA). Le Cerfa n° 15059 est le compte rendu financier d'une subvention.

**Q046 — Réponse D** (le 31 octobre de l'année N-1)  
Le **budget prévisionnel** d'un ESSMS hors CPOM se dépose avant le **31 octobre N-1** (pour l'année N). Le compte administratif, lui, se dépose au plus tard le 30 avril N+1. L'EPRD : 30 avril N (ou 30 jours après la notification de la dotation).

**Q047 — Réponse C** (que l'autorité fixe d'abord la ressource (la dotation) et que le gestionnaire présente des dépenses compatibles avec cette ressource)  
Dans l'ancien système (BP), le gestionnaire proposait des dépenses que l'autorité acceptait ou refusait. Avec l'EPRD, la ressource est **notifiée d'abord** ; le gestionnaire **ajuste** ses dépenses, avec un plan de financement et un tableau de trésorerie.

**Q048 — Réponse B** (10686 « Réserve de compensation des déficits »)  
La **réserve de compensation des déficits** (10686) sert à absorber un déficit ultérieur. Le 10682 finance des investissements. Les fonds dédiés concernent des ressources affectées par un tiers, pas l'affectation du résultat.

**Q049 — Réponse A** (que l'autorité de tarification refuse de la prendre en compte dans le financement du service)  
Une charge **non opposable** est une charge que l'autorité de tarification ne finance pas (non prévue, non justifiée, ou ne relevant pas du service). Elle reste à la charge de l'association, d'où l'importance d'une analytique juste et justifiable.

**Q050 — Réponse C** (96 785,71 €)  
Versé de janvier à mai : 5 × 92 500,00 = 462 500,00 €. Reste : 1 140 000,00 − 462 500,00 = 677 500,00 €, sur 7 mois : 96 785,71 €. 95 000,00 € (1 140 000 / 12) oublie le rattrapage des 5 premiers mois. À intégrer dans le plan de trésorerie.

---

## I. Paie, charges sociales et frais

**Q051 — Réponse D** (Parce qu'elle n'est pas soumise à la TVA sur l'essentiel de ses recettes)  
La taxe sur les salaires est due par les employeurs **non soumis à la TVA** (ou soumis sur moins de 90 % de leur chiffre d'affaires). Compte **6311**, groupe II. Les associations bénéficient d'un abattement annuel. *Barème, seuils et abattement : valeurs à vérifier chaque année.*

**Q052 — Réponse B** (D 512 1 150,00 / C 641x 1 150,00, code 20-SAVS)  
Depuis le PCG 2025 (règlement ANC 2022-06), les comptes de transfert de charges (79x) sont supprimés : les IJSS reçues en subrogation **diminuent la charge de salaires** (crédit d'un compte 641x, subdivision selon le plan de comptes), sur le service de la salariée. Le 7351 est réservé à la dotation de l'autorité de tarification.

**Q053 — Réponse A** (164,80 € en 6251 « Voyages et déplacements »)  
412 × 0,40 = 164,80 €. Les indemnités kilométriques sont des frais de déplacement (6251), sur le code du service (10-SESSAD), après signature du salarié et visa du chef de service. Le 6061 concerne le carburant payé directement (carte carburant).

**Q054 — Réponse C** (Vous ne remboursez pas ces kilomètres sans explication : vous en parlez au salarié et au chef de service (double prise en charge possible))  
Indemnités kilométriques et véhicule de service le même jour = **double prise en charge** probable. Il peut y avoir une explication (véhicule en panne, deux trajets) : on demande, on documente, et on ne paie qu'après visa. Le contrôle se fait sans accusation.

**Q055 — Réponse B** (Vérifier que le total des nets à payer du journal est égal au total du fichier de virement)  
Le total des **nets à payer** du journal doit être égal au total du **fichier de virement** (et le nombre de bulletins à l'effectif du mois, entrées et sorties comprises). Brut et net ne sont jamais égaux (cotisations salariales, prélèvement à la source).

---

## J. Trésorerie, contrôle interne, AAP et Excel

**Q056 — Réponse A** (145 000,00 €)  
180 000,00 + 210 000,00 − 245 000,00 = 145 000,00 €. − 35 000,00 € est le **flux net** du mois (encaissements − décaissements) : il faut l'ajouter au solde de départ.

**Q057 — Réponse D** (Vous appelez le fournisseur au numéro habituel (pas celui du mail), puis vous faites valider la modification par la direction avant tout paiement)  
Fraude au faux RIB : un mail se falsifie, et répondre au mail, c'est répondre au fraudeur. On **appelle** au numéro connu, on conserve la trace, et la modification est validée par une deuxième personne.

**Q058 — Réponse C** (12156 : demande de subvention (avec budget prévisionnel) ; 15059 : compte rendu financier de la subvention)  
Le **Cerfa n° 12156** est le dossier de demande de subvention des associations (avec le budget du projet) ; le **Cerfa n° 15059** est le compte rendu financier, à produire après l'exercice (budget / réalisé, écarts, utilisation de la subvention). L'EPRD et l'ERRD se déposent sur la plateforme de la CNSA.

**Q059 — Réponse B** (64 268,40 €)  
Année 1 : 42 000,00 × 0,5 = 21 000,00 € ; année 2 : 21 000,00 × 1,02 = 21 420,00 € ; année 3 : 21 420,00 × 1,02 = 21 848,40 €. Total : 64 268,40 €. 64 260,00 € applique 2 % une seule fois au total ; 63 000,00 € oublie la hausse ; 126 000,00 € oublie le mi-temps.

**Q060 — Réponse D** (SOMME.SI.ENS)  
SOMME.SI.ENS(montants ; comptes ; "6061" ; codes ; "20-SAVS") additionne selon **plusieurs critères**. RECHERCHEX renvoie une valeur trouvée (un libellé), NB.SI compte des lignes. Un tableau croisé dynamique (comptes en lignes, codes en colonnes) donne le même résultat pour tous les comptes à la fois.

---

## Corrigé des examens blancs

### Examen blanc n° 1

| N° | Question | Bonne réponse | Thème |
|---|---|---|---|
| 1 | Q001 | **B** | Analytique : principes et vocabulaire |
| 2 | Q003 | **A** | Analytique : principes et vocabulaire |
| 3 | Q007 | **C** | Codifier une facture |
| 4 | Q010 | **C** | Codifier une facture |
| 5 | Q014 | **C** | Clés de répartition |
| 6 | Q016 | **D** | Clés de répartition |
| 7 | Q022 | **B** | Frais de siège |
| 8 | Q026 | **A** | Coût complet et indicateurs |
| 9 | Q027 | **B** | Coût complet et indicateurs |
| 10 | Q032 | **B** | Suivi budgétaire et écarts |
| 11 | Q039 | **D** | Subventions, fonds dédiés et contributions volontaires |
| 12 | Q044 | **D** | Secteur médico-social |
| 13 | Q046 | **D** | Secteur médico-social |
| 14 | Q053 | **A** | Paie, charges sociales et frais |
| 15 | Q057 | **D** | Trésorerie, contrôle interne, AAP et Excel |

### Examen blanc n° 2

| N° | Question | Bonne réponse | Thème |
|---|---|---|---|
| 1 | Q002 | **D** | Analytique : principes et vocabulaire |
| 2 | Q005 | **B** | Analytique : principes et vocabulaire |
| 3 | Q008 | **B** | Codifier une facture |
| 4 | Q013 | **D** | Codifier une facture |
| 5 | Q015 | **B** | Clés de répartition |
| 6 | Q017 | **A** | Clés de répartition |
| 7 | Q021 | **C** | Frais de siège |
| 8 | Q029 | **A** | Coût complet et indicateurs |
| 9 | Q033 | **C** | Suivi budgétaire et écarts |
| 10 | Q036 | **C** | Suivi budgétaire et écarts |
| 11 | Q038 | **A** | Subventions, fonds dédiés et contributions volontaires |
| 12 | Q045 | **A** | Secteur médico-social |
| 13 | Q048 | **B** | Secteur médico-social |
| 14 | Q051 | **D** | Paie, charges sociales et frais |
| 15 | Q060 | **D** | Trésorerie, contrôle interne, AAP et Excel |

### Examen blanc n° 3

| N° | Question | Bonne réponse | Thème |
|---|---|---|---|
| 1 | Q004 | **C** | Analytique : principes et vocabulaire |
| 2 | Q009 | **D** | Codifier une facture |
| 3 | Q011 | **A** | Codifier une facture |
| 4 | Q019 | **B** | Clés de répartition |
| 5 | Q020 | **A** | Clés de répartition |
| 6 | Q023 | **D** | Frais de siège |
| 7 | Q024 | **C** | Frais de siège |
| 8 | Q028 | **C** | Coût complet et indicateurs |
| 9 | Q034 | **D** | Suivi budgétaire et écarts |
| 10 | Q040 | **B** | Subventions, fonds dédiés et contributions volontaires |
| 11 | Q043 | **D** | Subventions, fonds dédiés et contributions volontaires |
| 12 | Q047 | **C** | Secteur médico-social |
| 13 | Q049 | **A** | Secteur médico-social |
| 14 | Q055 | **B** | Paie, charges sociales et frais |
| 15 | Q058 | **C** | Trésorerie, contrôle interne, AAP et Excel |

## Grille d'interprétation du score (sur 15, barème 1 point par bonne réponse)

| Score | Interprétation | Que faire avant l'entretien |
|---|---|---|
| 14 – 15 | Excellent : vous maîtrisez l'analytique et les règles du secteur. | Entretenir : refaire un examen blanc la veille de l'entretien. |
| 11 – 13 | Bon niveau : vous passerez très probablement le cap du test écrit. | Relire les explications des questions manquées et retravailler le thème le plus faible. |
| 0 – 10 | À revoir : quelques bases manquent encore. | Reprendre le cours M16 (clés, frais de siège, suivi budgétaire) et le cours M17 (EPRD, paie, trésorerie), puis la banque de QCM thème par thème, et repasser un examen blanc 48 h après. |
