# M18 — Banque de QCM : la saisie comptable selon les règles de Trisomie 21 France

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CB** | Carte bancaire. Paiement par carte. Les encaissements CB arrivent en banque nets de commission. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ESMS** | Établissement ou service médico-social. Autre façon d'écrire ESSMS : une structure autorisée et financée par l'ARS et/ou le Département. |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PA** | Plateforme agréée — ou, dans le M18, journal de paie. Opérateur agréé par l'État (anciennement « PDP ») qui transmet les factures électroniques entre entreprises et envoie les données à l'administration. Dans le module M18, PA est le code du journal des salaires, alimenté automatiquement par EIG RH. |
    | **QCM** | Questionnaire à choix multiples. Test avec plusieurs réponses proposées. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **SIREN** | Numéro d'identification de l'entreprise (9 chiffres). Identifiant unique de chaque entreprise en France. Mention obligatoire sur les factures, y compris celui du client depuis la facturation électronique. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **VT** | Journal des ventes. Journal où l'on enregistre les factures clients (et les Z de caisse). |
    | **Compte 1150120** | RAN ESMS sous gestion contrôlée (créditeur) (plan T21). Report à nouveau excédentaire d'un ESSMS financé par une autorité de tarification (« gestion contrôlée ») : excédent pas encore affecté. |
    | **Compte 1159020** | RAN ESMS sous gestion contrôlée (débiteur) (plan T21). Report à nouveau déficitaire d'un ESSMS sous gestion contrôlée : déficit en attente de reprise. |
    | **Compte 1640000** | Emprunts auprès des Ets de crédit (plan T21). Capital restant dû des emprunts bancaires. Crédité au déblocage, débité à chaque remboursement de capital. |
    | **Compte 1648000** | Intérêts courus sur emprunts auprès des Ets de crédit (plan T21). Intérêts courus non échus (ICNE) : intérêts de l'exercice qui seront payés l'an prochain. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1940000** | Fonds dédiés sur subventions d'exploitation (plan T21). Subvention d'exploitation affectée à un projet et non dépensée au 31/12 (ex. : fondation pour le projet Pairs). |
    | **Compte 1950000** | Fonds dédiés sur contribution financières d'autres organismes (plan T21). Contributions financières d'autres organismes (ex. : fondation d'entreprise) non utilisées. |
    | **Compte 2183000** | Matériel de bureau et matériel informatique (plan T21). Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. |
    | **Compte 2184000** | Mobilier (plan T21). Mobilier (bureaux, armoires, tables). |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4210000** | Personnel - Rémunérations dues (plan T21). Salaires nets à payer. Crédité par la paie, débité au virement des salaires. |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4282000** | Dettes provisionnées pour congés à payer (plan T21). Congés payés acquis et non pris à la clôture (dette envers les salariés). |
    | **Compte 4310000** | Sécurité sociale (plan T21). URSSAF : cotisations à payer. Crédité par la paie, débité au paiement. |
    | **Compte 4382000** | Charges sociales sur congés à payer (plan T21). Charges sociales sur les congés payés provisionnés. |
    | **Compte 4417000** | Subventions d'exploitation (plan T21). Subvention d'exploitation accordée mais pas encore reçue (créance sur le financeur). |
    | **Compte 4611000** | Transfert T21 France (plan T21). Opérations de transfert avec la Fédération T21 France. |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4686000** | Comptes créditeurs et Charges à payer (plan T21). Charge de N à payer qui n'est ni un fournisseur, ni une dette sociale ou fiscale. |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4860000** | Charges constatées d’avance (plan T21). Charge constatée d'avance : facturée en N mais concernant N+1 (ex. : assurance avril N – mars N+1). |
    | **Compte 4870000** | Produits constatés d’avance (plan T21). Produit constaté d'avance : encaissé en N mais concernant N+1. |
    | **Compte 4878000** | Produits constatés d’avance - Subventions (plan T21). Subvention reçue en N pour une période de N+1 (ex. : année scolaire). |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6062500** | Fournitures scolaires, éducatives et de loisirs (plan T21). Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. |
    | **Compte 6062800** | Autres fournitures non stockées (plan T21). Autres petites fournitures. |
    | **Compte 6156100** | Maintenance informatique (plan T21). Maintenance informatique, abonnements logiciels. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6226010** | Honoraires comptabilité (plan T21). Honoraires de l'expert-comptable (et du commissaire aux comptes, faute de compte dédié dans le plan : à vérifier). |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6411100** | Personnel titulaire et stagiaires - Rémunération principale (plan T21). Salaires bruts des salariés en CDI (« titulaires »). |
    | **Compte 6412000** | Congés payés (plan T21). Congés payés (et variation de la provision). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 (plan T21). Remboursements de la prévoyance pour les arrêts longs : au crédit, en banque. Ancien compte 6492000. |
    | **Compte 6451800** | Provision sur charges Congés Payés (plan T21). Charges sociales sur la provision pour congés payés. |
    | **Compte 6556000** | Frais de siège social du gestionnaire (plan T21). Frais de siège facturés par le siège à la structure (taux autorisé par le financeur). |
    | **Compte 6611000** | Intêrets des emprunts (plan T21). Intérêts des emprunts (exemple du document T21 : prélevés par la banque). |
    | **Compte 6618000** | Autres charges d'intérêt - intérêts courus (plan T21). Intérêts courus à la clôture (ICNE). |
    | **Compte 6892200** | Report en fonds dédiés à l'exploitation (plan T21). Mise en fonds dédiés de la part non dépensée d'une subvention d'exploitation affectée. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
    | **Compte 7584100** | Remboursements sur frais de formation ancien compte 6498000 (plan T21). Remboursement de frais de formation (OPCO). Ancien compte 6498000. |
    | **Compte 7588000** | Autres produits divers de gestion courante (plan T21). Autres produits divers (ex. : arrondis créditeurs). |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **FOGARAGEMARTIN** | Compte fournisseur Garage Martin (dossier M18). Garage de Valence : entretien et achat des véhicules. Regroupé dans 4010000. |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIBENALI** | Compte libéral : psychologue (dossier M18). Groupes de parole du SAVS (6223224). |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **SAHADDAD** | Compte salarié : Rachid Haddad (dossier M18). Notes de frais d'un CESF (SAVS et habitat inclusif). |
    | **bon à payer** | Accord écrit de la direction pour payer. Sans bon à payer de la directrice, la facture ne part pas en paiement. |
    | **charge constatée d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **codes analytiques** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **facture non parvenue** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **Frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
    | **produit à recevoir** | Recette acquise mais pas encore reçue. Ex. : solde d'une subvention AGEFIPH dû au 31/12, versé en mars. |
    | **report à nouveau** | Résultat gardé en attente. Excédent (110) ou déficit (119) reporté sur un budget suivant. |
    | **réserve de compensation** | Excédent mis de côté pour un futur déficit. Compte 10686 : si le service est en déficit plus tard, on puise dans cette réserve. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
<!-- /glossaire-page -->

*Module M18 — Saisir dans une association du réseau Trisomie 21 France. Exemples sur l'association **fictive** Cap Horizons 21 et ses 5 structures (voir la [fiche du dossier](fiche_dossier_5_structures.md)). Les règles citées viennent des trois documents internes de Trisomie 21 France (« La comptabilité chez Trisomie 21 France » et « Les journaux comptables chez Trisomie 21 France », 30/04/2026 ; « Plan comptable général T21 France », MAJ 13/10/2025). Mise à jour : 15/11/2026.*

## Mode d'emploi

- **50 questions** réparties en 6 thèmes : les documents et le plan T21, les journaux, les comptes de tiers, les 5 structures et les inter-structures (IS), les cas de saisie, la fin d'exercice.
- **Une seule bonne réponse par question.** Niveau : ★ facile · ★★ intermédiaire · ★★★ un peu plus long (calcul ou raisonnement en plusieurs étapes).
- Les réponses commentées sont dans un fichier séparé : `QCM_reponses.md`. Ne l'ouvrez qu'après avoir répondu.
- Rappels essentiels : Cap Horizons 21 **ne récupère pas la TVA** (charges et immobilisations **TTC**) ; **pas de stocks** ; comptes à **7 chiffres**. Les numéros de comptes de liaison et de banque des structures, les clés de répartition et les montants sont des **hypothèses pédagogiques** (fiche du dossier).
- Clés de répartition (ordre SIE / SES / SAV / EMP / ASS) : **m²** 15 / 45 / 25 / 10 / 5 % ; **ETP** 9 / 48 / 27 / 12 / 4 % ; **forfait** honoraires 20 / 40 / 20 / 10 / 10 %.
- Dans les écritures, « D » = débit, « C » = crédit ; montants au format français.

## Sommaire

- A. Les documents et le plan comptable T21 — Q001 à Q008 (8 questions)
- B. Les journaux — Q009 à Q016 (8 questions)
- C. Les comptes de tiers FO, LI, SA, CL — Q017 à Q023 (7 questions)
- D. Les 5 structures et les inter-structures — Q024 à Q031 (8 questions)
- E. Cas de saisie — Q032 à Q041 (10 questions)
- F. Fin d'exercice — Q042 à Q050 (9 questions)

---

## A. Les documents et le plan comptable T21

### Q001 ★

Les numéros de comptes du plan comptable T21 France comptent :

- **A)** 3 chiffres
- **B)** 6 chiffres
- **C)** 7 chiffres
- **D)** un nombre de chiffres variable selon la classe

### Q002 ★

Selon le document « La comptabilité chez Trisomie 21 France », le plan comptable à appliquer est :

- **A)** le plan comptable général des entreprises, sans adaptation
- **B)** le plan comptable des établissements et services sociaux et médico-sociaux relevant du I de l'article L. 312-1 du CASF (dernière version : arrêté du 19 décembre 2025)
- **C)** l'instruction budgétaire et comptable des communes
- **D)** le plan comptable des fondations reconnues d'utilité publique

### Q003 ★★

Le plan comptable T21 ne contient aucun compte 445. La raison et la conséquence pour la saisie sont :

- **A)** c'est un oubli : il faut créer le compte 4456600 dans le logiciel
- **B)** la TVA est enregistrée sur un compte 6xxxxxx séparé « TVA non récupérable »
- **C)** les structures ne sont pas soumises à la TVA : on saisit les factures TTC en charge (ou en immobilisation)
- **D)** la TVA est déclarée par la Fédération pour toutes les associations

### Q004 ★

Une structure achète du papier, des produits d'entretien et du carburant. Selon les documents T21 :

- **A)** on les enregistre en 601 ou 602 (achats stockés), puis on constate la variation de stock à la clôture
- **B)** on les immobilise s'ils dépassent 100 €
- **C)** on les met en 4710000 jusqu'à la fin du mois
- **D)** il n'y a pas de stocks : on les enregistre en achats non stockés 606xxxx

### Q005 ★★

Le plan T21 est « MAJ le 13/10/2025 – Applicable au 1/01/2025 » ; le document de procédure renvoie à l'arrêté du 19/12/2025 applicable au 01/01/2026. Le bon réflexe :

- **A)** demander si une mise à jour du plan est prévue et vérifier les comptes créés ou supprimés avant la clôture 2026
- **B)** ne rien faire : un plan comptable est valable dix ans
- **C)** créer soi-même dans le logiciel tous les comptes de l'arrêté
- **D)** revenir au plan comptable général des entreprises jusqu'à la mise à jour

### Q006 ★★

Quelle est la différence entre 1150120 et 1159020 ?

- **A)** Le premier est utilisé par le siège, le second par les services
- **B)** Le premier reçoit les excédents antérieurs non affectés (report à nouveau créditeur), le second les déficits antérieurs (report à nouveau débiteur), pour les ESMS sous gestion contrôlée
- **C)** Le premier concerne 2025, le second 2026
- **D)** Aucune : ce sont deux comptes en double à fusionner

### Q007 ★★

Le document T21 décrit 3 types de réserves (investissement, compensation des déficits, trésorerie). Combien de comptes de réserves 10685xx le plan T21 contient-il ?

- **A)** 2
- **B)** 3
- **C)** 5
- **D)** 4

### Q008 ★★★

Selon le document T21, « la réserve de compensation des déficits doit être d'au moins 5 % de la dotation annuelle ». Pour un service doté de 900 000,00 €, le niveau indiqué est :

- **A)** 4 500,00 €
- **B)** 45 000,00 €
- **C)** 90 000,00 €
- **D)** 450 000,00 €

---

## B. Les journaux

### Q009 ★

Le journal des ventes (VT) chez Trisomie 21 France :

- **A)** est utilisé par toutes les structures pour leurs dotations
- **B)** est un journal manuel où l'on saisit les dons
- **C)** n'est utilisé que par la Fédération ; il est alimenté automatiquement par EIG Gestion commerciale
- **D)** sert aux notes de frais des salariés

### Q010 ★

Dans le journal de paie (PA) :

- **A)** aucune écriture manuelle n'est autorisée : les écritures sont déversées par EIG RH
- **B)** on saisit à la main les écritures de paie à partir des bulletins
- **C)** on saisit les remboursements de notes de frais
- **D)** on saisit les IJSS reçues de la CPAM

### Q011 ★★

Le journal BQSIE est un journal de banque à contrepartie automatique. Vous enregistrez le paiement d'une facture EDF de 120,00 €. Que saisissez-vous ?

- **A)** 5121000 au débit 120,00 et FOEDF au crédit 120,00
- **B)** 6061200 au débit 120,00, sans tiers
- **C)** FOEDF au crédit 120,00 ; le logiciel met la banque au débit
- **D)** FOEDF au débit 120,00 ; le logiciel met lui-même la banque (5121000) au crédit

### Q012 ★★

La structure ASS retire 300,00 € au distributeur pour alimenter sa caisse. Comment l'enregistrer ?

- **A)** Banque au crédit et caisse au débit dans une seule écriture d'OD
- **B)** Dans BQASS : 5800000 au débit (banque créditée) ; dans CAASS : 5800000 au crédit (caisse débitée)
- **C)** En charge 6270000 (frais bancaires)
- **D)** Par le compte de liaison 1840000

### Q013 ★

Les dotations aux amortissements sont enregistrées :

- **A)** à la main en OD par l'agent comptable
- **B)** dans le journal des achats, avec la facture
- **C)** dans le journal des immobilisations (IM), alimenté automatiquement par EIG IMMOS
- **D)** dans le journal de paie

### Q014 ★★

Le journal des à-nouveaux provisoires (ANP) :

- **A)** peut être régénéré autant de fois que souhaité tant que l'exercice N-1 n'est pas clos
- **B)** se saisit à la main à partir du bilan de l'expert-comptable
- **C)** n'est jamais remplacé
- **D)** contient les comptes de charges et de produits de N-1

### Q015 ★

Dans quel journal saisit-on une note de frais de salarié ?

- **A)** Le journal de paie (PA)
- **B)** Le journal de banque, directement en charge
- **C)** Le journal des opérations diverses (OD) uniquement
- **D)** Le journal des achats (AC), avec le compte de tiers SA

### Q016 ★★

L'organisme de prévoyance verse 2 340,00 € pour un salarié en arrêt de longue durée. Dans le journal de banque, on saisit :

- **A)** 6419000 au débit
- **B)** 6419100 au crédit
- **C)** 7488000 au crédit
- **D)** 4310000 au crédit

---

## C. Les comptes de tiers FO, LI, SA, CL

### Q017 ★

Saisir une facture directement sur le compte 4010000 Fournisseurs (sans compte FO) est :

- **A)** interdit : 4010000 est un compte de centralisation, on saisit toujours sur le compte de tiers
- **B)** autorisé pour les petites factures
- **C)** obligatoire pour les fournisseurs occasionnels
- **D)** autorisé au journal OD seulement

### Q018 ★

L'association conventionne avec une orthophoniste libérale, Mme Lucia Martinez. Son compte de tiers sera :

- **A)** FOMARTINEZ
- **B)** SAMARTINEZ
- **C)** LIMARTINEZ
- **D)** 4011000 directement

### Q019 ★★

Claire Dupont, orthophoniste (LIDUPONT), envoie un avoir de 68,00 € (2 séances facturées à tort). L'écriture est :

- **A)** D 6223221 68,00 / C LIDUPONT 68,00
- **B)** D 4011000 68,00 / C 5122000 68,00
- **C)** D LIDUPONT 68,00 / C 7588000 68,00
- **D)** D LIDUPONT 68,00 / C 6223221 68,00

### Q020 ★★

Le compte 4248000 « Salariés – NDF » :

- **A)** enregistre les salaires nets à payer
- **B)** est le compte de centralisation des comptes de tiers SA (notes de frais des salariés)
- **C)** enregistre les acomptes sur salaire
- **D)** enregistre les oppositions sur salaire

### Q021 ★★

Vous devez saisir une facture EDF et ne trouvez pas tout de suite FOEDF. Que faites-vous ?

- **A)** Vous cherchez d'abord le compte existant (par nom, par début de code) : créer un FOEDF2 empêcherait le lettrage et la détection des doublons
- **B)** Vous créez FOEDF2, c'est plus rapide
- **C)** Vous saisissez sur 4010000 et régulariserez plus tard
- **D)** Vous saisissez sur 4710000

### Q022 ★★

Dans la balance auxiliaire du SAVS, FOGARAGEMARTIN présente un solde **débiteur** de 624,00 €. L'explication la plus probable :

- **A)** une facture non encore payée
- **B)** une facture saisie en double
- **C)** une facture payée deux fois, ou un avoir reçu mais pas lettré
- **D)** une facture non parvenue

### Q023 ★

Les comptes de tiers CL (clients) :

- **A)** sont crédités à la facture et débités au règlement
- **B)** sont utilisés par toutes les structures pour les dotations
- **C)** n'existent pas dans le plan T21
- **D)** sont débités à la facture et crédités au règlement (et ne servent qu'à la Fédération, via EIG Gestion commerciale)

---

## D. Les 5 structures et les inter-structures

### Q024 ★

Cap Horizons 21, c'est :

- **A)** cinq associations différentes
- **B)** une seule association (un SIREN) qui tient cinq comptabilités appelées structures
- **C)** une association et quatre sociétés
- **D)** une seule comptabilité avec cinq codes analytiques

### Q025 ★

Dans les livres du SESSAD, le compte de liaison avec le siège est :

- **A)** 1840000 Liaison Siège
- **B)** 1849100 Liaison SESSAD
- **C)** 5800000 Virements internes
- **D)** 4611000

### Q026 ★★

Au siège, le 1849100 Liaison SESSAD a un solde débiteur de 20 389,20 €. Dans les livres du SESSAD, le 1840000 doit présenter :

- **A)** un solde débiteur de 20 389,20 €
- **B)** un solde nul
- **C)** un solde créditeur de 20 389,20 €
- **D)** un solde créditeur égal à la moitié, soit 10 194,60 €

### Q027 ★★

Facture EDF du trimestre : 1 200,00 € TTC, saisie au siège, répartie selon la clé m². La part du SAVS est :

- **A)** 120,00 €
- **B)** 180,00 €
- **C)** 540,00 €
- **D)** 300,00 €

### Q028 ★★

Le SAVS rembourse 8 000,00 € au siège par virement bancaire. Dans les livres du SAVS, la contrepartie de la banque est :

- **A)** 5800000 Virements internes
- **B)** 1840000 Liaison Siège
- **C)** 6556000 Frais de siège
- **D)** 4010000 Fournisseurs

### Q029 ★★

Les frais de siège de novembre (2 587,50 € pour le SAVS) s'enregistrent :

- **A)** chez le SAVS : 6556000 au débit / 1840000 au crédit ; chez le siège : 1849200 au débit / 7556000 au crédit
- **B)** chez le SAVS : 7556000 au crédit ; chez le siège : 6556000 au débit
- **C)** uniquement chez le siège, en 7556000
- **D)** chez le SAVS : 6226010 au débit

### Q030 ★★★

Facture télécom de 1 450,00 € TTC saisie au siège, clé ETP. La part de l'Emploi accompagné (EMP) est :

- **A)** 130,50 €
- **B)** 145,00 €
- **C)** 174,00 €
- **D)** 391,50 €

### Q031 ★★

Dans les comptes de l'association entière (les 5 structures additionnées), les comptes de classe 18 :

- **A)** représentent la trésorerie disponible
- **B)** sont égaux au total des frais de siège
- **C)** sont toujours créditeurs
- **D)** doivent avoir un solde nul

---

## E. Cas de saisie

### Q032 ★

Un éducateur paie du carburant avec la carte bancaire du SESSAD ; il rapporte le ticket de caisse et le ticket CB, sans facture. On saisit :

- **A)** directement en banque (BQSES), au débit du 6062100, sans compte FO
- **B)** au journal des achats avec un compte FO créé pour la station
- **C)** en 4710000 en attendant une facture
- **D)** en note de frais SA

### Q033 ★★

L'Emploi accompagné achète un ordinateur portable : 907,50 € HT + TVA 181,50 € = 1 089,00 € TTC. Seuil d'immobilisation de l'association : 500,00 € TTC. On saisit :

- **A)** 907,50 € en 2183000 et 181,50 € en 4456600
- **B)** 1 089,00 € en 6062800
- **C)** 1 089,00 € en 2183000, et on crée la fiche dans EIG IMMOS
- **D)** 907,50 € en 6156100

### Q034 ★★

Un destructeur de documents de 350,00 € TTC a été enregistré en 2183000. Que faire ?

- **A)** Rien : tout matériel de bureau s'immobilise
- **B)** Le laisser et l'amortir sur un an
- **C)** Le passer en 4710000
- **D)** Le reclasser en charge (606xxxx) et supprimer sa fiche dans EIG IMMOS

### Q035 ★

L'ARS verse la dotation mensuelle du SESSAD : 108 000,00 €. Dans BQSES, on saisit :

- **A)** 7488000 au crédit
- **B)** 7312130 au crédit
- **C)** 4417000 au débit
- **D)** 1840000 au crédit

### Q036 ★★

Une IJSS de 1 860,00 € reçue a été saisie par erreur au **débit** du 6419000 dans BQSAV. Au rapprochement bancaire, on constate :

- **A)** un écart de 3 720,00 € (deux fois le montant), la banque comptable étant trop basse
- **B)** un écart de 1 860,00 €
- **C)** aucun écart, seule la charge est fausse
- **D)** un écart de 930,00 €

### Q037 ★★

Nathalie Durand présente une note de frais : indemnités kilométriques 206,00 € et stylos et carnets 23,40 €. L'écriture au journal des achats est :

- **A)** D 6411100 229,40 / C 4210000 229,40
- **B)** D 6251000 229,40 / C 5122000 229,40
- **C)** D 6251000 206,00 et D 6062400 23,40 / C SADURAND 229,40
- **D)** D SADURAND 229,40 / C 6251000 229,40

### Q038 ★★

Facture Ludik Éducation pour le SESSAD : 405,75 € HT + TVA 81,15 € = 486,90 € TTC. L'écriture correcte :

- **A)** D 6062500 405,75 / D 4456600 81,15 / C FOLUDIK 486,90
- **B)** D 2184000 486,90 / C FOLUDIK 486,90
- **C)** D 6062500 405,75 / C FOLUDIK 405,75
- **D)** D 6062500 486,90 / C FOLUDIK 486,90

### Q039 ★★

Rachid Haddad, salarié du SAVS, présente une note de frais pour des achats faits pour l'habitat inclusif (structure ASS). On la saisit :

- **A)** dans le SAVS, code 20-SAVS, puisqu'il est salarié du SAVS
- **B)** dans ASS, sur son compte SAHADDAD, code analytique 40-HABITAT
- **C)** au siège, puis on répartit selon la clé ETP
- **D)** dans le journal de paie du SAVS

### Q040 ★★

Vous recevez un « DUPLICATA » d'une facture de LIBENALI déjà saisie le mois précédent et non payée. Que faites-vous ?

- **A)** Vous ne la saisissez pas (vous vérifiez le n° dans le compte du tiers et tamponnez « déjà comptabilisé »), puis vous traitez la relance (paiement si le bon à payer est signé)
- **B)** Vous la saisissez à nouveau, puisque c'est un nouveau document
- **C)** Vous la saisissez puis passez un avoir
- **D)** Vous la mettez en 4710000

### Q041 ★★★

Le déversement de paie du SESSAD contient une ligne « 6419000 IJSS subrogation 642,18 € au crédit », et la même IJSS a été encaissée en banque (saisie en 6419000 au crédit, comme le prévoit la procédure T21). Que faites-vous ?

- **A)** Vous supprimez à la main la ligne dans le journal PA
- **B)** Vous passez une OD de 642,18 € au crédit du 6419000 pour équilibrer
- **C)** Vous signalez le doublon au service paie pour corriger le paramétrage et régénérer le déversement, sans écrire dans le journal PA
- **D)** Rien : deux crédits en 6419000 sont normaux en subrogation

---

## F. Fin d'exercice

### Q042 ★★

Au 31/12/2026, les séances d'orthophonie de décembre (612,00 €) n'ont pas encore été facturées. L'écriture d'inventaire correcte est :

- **A)** D 4081000 612,00 / C 6223221 612,00
- **B)** D 6223221 612,00 / C LIDUPONT 612,00
- **C)** D 4860000 612,00 / C 6223221 612,00
- **D)** D 6223221 612,00 / C 4081000 612,00

### Q043 ★★

Prime d'assurance annuelle de 7 200,00 € pour la période du 01/04/2026 au 31/03/2027, entièrement comptabilisée en 2026. La charge constatée d'avance au 31/12/2026 est :

- **A)** 1 800,00 € au débit du 4860000
- **B)** 5 400,00 € au débit du 4860000
- **C)** 1 800,00 € au crédit du 4860000
- **D)** 2 400,00 € au débit du 4870000

### Q044 ★★

Emprunt du SESSAD : l'échéance du 31/01/2027 comprend 438,00 € d'intérêts pour la période du 01/11/2026 au 31/01/2027. Au 31/12/2026, on enregistre :

- **A)** D 6611000 438,00 / C 1640000 438,00
- **B)** D 6618000 292,00 / C 1648000 292,00
- **C)** D 1648000 292,00 / C 6618000 292,00
- **D)** D 6618000 146,00 / C 1648000 146,00

### Q045 ★★

Subvention affectée de 40 000,00 € d'une fondation pour un projet ; 27 350,00 € dépensés en 2026, le reste le sera en 2027. Au 31/12/2026 :

- **A)** on extourne 12 650,00 € de produit au 01/01/2027
- **B)** on passe 12 650,00 € en produits constatés d'avance (4878000)
- **C)** on reporte 12 650,00 € en fonds dédiés : D 6892200 / C compte 19 (1940000 ou 1950000 selon la nature du financeur)
- **D)** on rembourse immédiatement 12 650,00 € à la fondation

### Q046 ★★

Convention AGEFIPH de 24 000,00 € pour la période du 01/07/2026 au 30/06/2027, entièrement encaissée en 2026 (crédit 7488000). Au 31/12/2026 :

- **A)** aucune écriture : la subvention est encaissée
- **B)** fonds dédiés de 12 000,00 €
- **C)** produit à recevoir de 12 000,00 €
- **D)** produit constaté d'avance de 12 000,00 € : D 7488000 / C 4878000

### Q047 ★

Selon le document T21, quels comptes doivent être soldés (à zéro) à la clôture ?

- **A)** Les comptes d'attente (classe 47) et les virements internes (classe 58)
- **B)** Les comptes de banque
- **C)** Les comptes de fonds dédiés (classe 19)
- **D)** Les comptes de liaison de chaque structure, pris un par un

### Q048 ★★

Le 01/01/2027, on extourne la facture non parvenue d'électricité de 1 860,00 €. Le compte 6061200 est alors :

- **A)** débité de 1 860,00 €
- **B)** crédité de 1 860,00 € (c'est l'« exception » des charges saisies au crédit, citée par le document T21)
- **C)** soldé par le compte 1840000
- **D)** inchangé : on n'extourne que le 4081000

### Q049 ★★

Les congés payés acquis et non pris au 31/12/2026 :

- **A)** sont calculés par l'agent comptable salarié par salarié et saisis dans le journal PA
- **B)** sont une provision de classe 15
- **C)** sont calculés par EIG RH ; si le logiciel ne déverse pas l'écriture, on la passe en OD : 6412000 / 4282000 et 6451800 / 4382000, par structure
- **D)** ne se comptabilisent pas dans un ESSMS

### Q050 ★★

L'OPCO a accordé 1 450,00 € de prise en charge pour une formation suivie en novembre 2026 par une salariée du SAVS ; le versement aura lieu en février 2027. Au 31/12/2026 :

- **A)** aucune écriture avant l'encaissement
- **B)** D 4081000 / C 7584100
- **C)** D 4686000 / C 6419000
- **D)** D 4676000 / C 7584100 (produit à recevoir)

---

[Voir les réponses commentées](QCM_reponses.md)
