# M18 — La saisie comptable chez Trisomie 21 France (documents réels)

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BP** | Budget prévisionnel. Dans le médico-social : le budget qu'un service hors CPOM (ex. : le SAVS) présente à son financeur avant le 31 octobre de l'année précédente (à vérifier chaque année). |
    | **BQ** | Journal de banque. Journal qui reprend les mouvements du relevé bancaire. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CA** | Chiffre d'affaires (ou journal de caisse, ou compte administratif). Le plus souvent : le total des ventes HT de l'année. Dans une liste de journaux, « CA » peut désigner le journal de caisse. Dans le médico-social (M16, M17), CA = compte administratif : le compte rendu annuel d'un service hors CPOM (ex. : le SAVS) remis au Département. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CB** | Carte bancaire. Paiement par carte. Les encaissements CB arrivent en banque nets de commission. |
    | **CCA** | Charges constatées d'avance — ou compte courant d'associé. Deux sens selon le contexte : (1) clôture : charge payée en N mais qui concerne N+1 (compte 486) ; (2) financement : argent prêté par un associé à sa société (compte 455). |
    | **CME** | Crédit Mutuel (abréviation du plan T21). Banque coopérative : pour ouvrir un compte, on souscrit des parts sociales. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **CPOM** | Contrat pluriannuel d'objectifs et de moyens. Contrat de 5 ans entre une association et l'ARS et/ou le Département : objectifs, moyens, et budget présenté en EPRD. |
    | **CV** | Chevaux fiscaux (puissance fiscale). Puissance administrative d'une voiture, inscrite sur la carte grise. Le barème kilométrique dépend du nombre de CV. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **EPRD** | État des prévisions de recettes et de dépenses. Budget prévisionnel des gestionnaires sous CPOM. Il part de la ressource notifiée par le financeur (« budget par la recette »). Dépôt en général au 30 avril (à vérifier chaque année). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **FNP** | Factures non parvenues. À la clôture : charges de l'année dont la facture n'est pas encore arrivée. On les enregistre quand même (compte 408) pour que l'année supporte ses vraies charges. |
    | **ICNE** | Intérêts courus non échus. À la clôture : intérêts d'emprunt qui concernent l'année mais qui seront payés à la prochaine échéance. On les enregistre en charge de N. |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N+1** | L'exercice suivant. L'année comptable d'après (ex. : si N = 2026, N+1 = 2027). Une charge « de N+1 » ne doit pas peser sur le résultat de N. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCA** | Produits constatés d'avance. À la clôture : produit facturé en N mais qui concerne N+1 (compte 487). On le retire du chiffre d'affaires de N. |
    | **PSB** | Parts sociales (abréviation du plan T21). Dans « PSB CME T21 France (parts sociales) », compte 5040000 : parts sociales détenues au Crédit Mutuel. |
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
    | **URSSAF** | Organisme de recouvrement des cotisations sociales. Collecte les cotisations sociales (maladie, famille, CSG…) des salariés et des indépendants. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 4671XXX** | Comptes débiteurs et produits à recevoir (plan T21). Créances diverses et produits à recevoir (un sous-compte par débiteur). Libellé identique à 4676000 : à clarifier. |
    | **Compte 1068522** | Res invest - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve d'investissement : excédent d'un ESSMS mis de côté, sur décision du financeur, pour financer un investissement. |
    | **Compte 1068552** | Res tréso - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve de trésorerie : excédent affecté pour renforcer la trésorerie du service. |
    | **Compte 1068562** | Res compens déficits- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des déficits : couvre un futur déficit. Le document T21 indique qu'elle doit atteindre au moins 5 % de la dotation annuelle. |
    | **Compte 1068572** | Res compens amort- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des charges d'amortissement : couvre les surcoûts d'amortissement d'un investissement. |
    | **Compte 1202000** | Excédent de l'exercice ESMS sous gestion non contrôlée (plan T21). Excédent de l'exercice d'une activité non tarifée (ex. : vie associative). |
    | **Compte 1205000** | Excédent de l'exercice ESMS sous gestion contrôlée (plan T21). Excédent de l'exercice d'un ESSMS tarifé (SESSAD, SAVS), en attente de décision d'affectation. |
    | **Compte 1292000** | Déficit de l'exercice ESMS sous gestion non contrôlée (plan T21). Déficit de l'exercice d'une activité non tarifée. |
    | **Compte 1295000** | Déficit de l'exercice ESMS sous gestion contrôlée (plan T21). Déficit de l'exercice d'un ESSMS tarifé. |
    | **Compte 1640000** | Emprunts auprès des Ets de crédit (plan T21). Capital restant dû des emprunts bancaires. Crédité au déblocage, débité à chaque remboursement de capital. |
    | **Compte 1648000** | Intérêts courus sur emprunts auprès des Ets de crédit (plan T21). Intérêts courus non échus (ICNE) : intérêts de l'exercice qui seront payés l'an prochain. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 2182000** | Matériel de transport (plan T21). Véhicule acheté (exemple du document T21 : véhicule acheté au garage Martin). |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4110000** | Clients (comptes de tiers CL…) (plan T21). Centralisation des clients. On saisit dans les comptes CL… |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4282000** | Dettes provisionnées pour congés à payer (plan T21). Congés payés acquis et non pris à la clôture (dette envers les salariés). |
    | **Compte 4382000** | Charges sociales sur congés à payer (plan T21). Charges sociales sur les congés payés provisionnés. |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4686000** | Comptes créditeurs et Charges à payer (plan T21). Charge de N à payer qui n'est ni un fournisseur, ni une dette sociale ou fiscale. |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4730000** | Comptes d’attente (plan T21). Second compte d'attente (même libellé que 4710000 : à clarifier). Même règle : soldé au 31/12. |
    | **Compte 4860000** | Charges constatées d’avance (plan T21). Charge constatée d'avance : facturée en N mais concernant N+1 (ex. : assurance avril N – mars N+1). |
    | **Compte 4878000** | Produits constatés d’avance - Subventions (plan T21). Subvention reçue en N pour une période de N+1 (ex. : année scolaire). |
    | **Compte 5040000** | PSB CME T21 France (parts sociales) (plan T21). Parts sociales du Crédit Mutuel détenues par T21 France (« PSB CME »). Le document range les parts sociales en 27 : à clarifier. |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5188000** | Intérêts courus à recevoir (plan T21). Intérêts des placements acquis au 31/12 mais versés plus tard. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6062500** | Fournitures scolaires, éducatives et de loisirs (plan T21). Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6256000** | Missions (plan T21). Repas et hébergement en mission. |
    | **Compte 6262000** | Frais de télécommunication (plan T21). Téléphone, internet. |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6412000** | Congés payés (plan T21). Congés payés (et variation de la provision). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 (plan T21). Remboursements de la prévoyance pour les arrêts longs : au crédit, en banque. Ancien compte 6492000. |
    | **Compte 6451800** | Provision sur charges Congés Payés (plan T21). Charges sociales sur la provision pour congés payés. |
    | **Compte 6556000** | Frais de siège social du gestionnaire (plan T21). Frais de siège facturés par le siège à la structure (taux autorisé par le financeur). |
    | **Compte 6611000** | Intêrets des emprunts (plan T21). Intérêts des emprunts (exemple du document T21 : prélevés par la banque). |
    | **Compte 6618000** | Autres charges d'intérêt - intérêts courus (plan T21). Intérêts courus à la clôture (ICNE). |
    | **Compte 6892200** | Report en fonds dédiés à l'exploitation (plan T21). Mise en fonds dédiés de la part non dépensée d'une subvention d'exploitation affectée. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
    | **Compte 7640000** | Revenus des valeurs mobilières de placement (plan T21). Intérêts des placements (comptes à terme, livrets). |
    | **Compte 7892200** | Fonds dédiés - Exploitation (plan T21). Utilisation, l'année suivante, des fonds dédiés d'exploitation (quand on dépense enfin la subvention). |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **FOMARTIN** | Compte fournisseur Garage Martin (document T21). Exemple du document T21 : achat d'un véhicule, FOMARTIN au crédit, 2182000 au débit. |
    | **FOORANGE** | Compte fournisseur télécom (dossier M18). Contrat unique de téléphonie et internet facturé au siège, réparti en IS selon les ETP. |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **Bon à payer** | Accord écrit de la direction pour payer. Sans bon à payer de la directrice, la facture ne part pas en paiement. |
    | **charge constatée d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **facture non parvenue** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **Fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **Frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **Report à nouveau** | Résultat gardé en attente. Excédent (110) ou déficit (119) reporté sur un budget suivant. |
    | **Réserve de compensation** | Excédent mis de côté pour un futur déficit. Compte 10686 : si le service est en déficit plus tard, on puise dans cette réserve. |
<!-- /glossaire-page -->

**Public :** débutant(e) qui prend un poste d'agent comptable dans une association du réseau Trisomie 21 | **Durée :** 3 à 4 jours avec les exercices | **Prérequis :** M01 (fondamentaux) ; M16 et M17 conseillés

!!! abstract "En clair : ce que ce module vous apprend"
    Ce module est construit à partir de **trois documents internes réels** de Trisomie 21 France :

    - « La comptabilité chez Trisomie 21 France » ;
    - « Les journaux comptables chez Trisomie 21 France » ;
    - le « Plan comptable général T21 France ».

    À la fin, vous savez **saisir** toutes les pièces du quotidien dans le bon journal, la bonne structure, le bon compte et le bon code analytique : factures fournisseurs, factures de libéraux, notes de frais, relevés bancaires, caisse, placements, inter-structures, écritures de fin d'année. Vous savez aussi **contrôler et analyser** comme une comptable confirmée.

    L'association a **5 structures** : la comptabilité se tient donc **cinq fois**, une par structure, et elle est reliée par les comptes de liaison.

**Les pages du module**

| Page | À quoi elle sert |
|---|---|
| [Fiche du dossier : les 5 structures et les règles de saisie](fiche_dossier_5_structures.md) | Le dossier d'entraînement : structures, comptes bancaires, comptes de liaison, fournisseurs, clés de répartition, règles maison |
| [Le plan comptable T21, compte par compte](plan_comptable_T21_explique.md) | Les 268 comptes du plan T21, avec une explication simple et le journal habituel |
| Ce cours | La méthode, avec des écritures types |
| 12 exercices corrigés + [QCM](QCM_questions.md) | La pratique, du plus simple au cas de synthèse |

---

## 1. Le cadre : ce que disent les documents T21

### 1.1 Bilan et compte de résultat

Le document T21 commence par la base : toute comptabilité aboutit à **deux états**.

- Le **bilan** : comptes des classes **1 à 5**. Ce que l'association possède et ce qu'elle doit, à une date.
- Le **compte de résultat** : comptes des classes **6 et 7**. Ce qu'elle a dépensé (charges) et gagné (produits) pendant l'année.
- **Résultat = total des produits (classe 7) − total des charges (classe 6).** Positif : **excédent**. Négatif : **déficit**. Dans une association, on ne dit pas « bénéfice », on dit « excédent ».

Le plan à appliquer est celui des **établissements et services sociaux et médico-sociaux (ESSMS)** relevant du I de l'article L. 312-1 du Code de l'action sociale et des familles (CASF). Sa dernière version est l'**arrêté du 19 décembre 2025**, applicable à compter du 1er janvier 2026.

### 1.2 Le sens des comptes : le tableau à connaître par cœur

| Classe | Contenu chez T21 | Augmente au… | Diminue au… | Exemple du document T21 |
|---|---|---|---|---|
| 10 | Fonds propres et réserves (pas de capital social) | Crédit (affectation en réserve) | Débit (reprise de réserve) | Réserve de compensation des déficits ≥ 5 % de la dotation annuelle |
| 11 | Report à nouveau : résultats pas encore affectés | Crédit (excédent) | Débit (déficit) | Affectation **décidée** par le financeur (compte administratif) ou **proposée** par l'association (CPOM) |
| 12 | Résultat de l'exercice | Crédit (excédent) | Débit (déficit) | Produits − charges |
| 14 | Provisions réglementées | Crédit (dotation) | Débit (reprise) | **Jamais** sans accord de l'autorité de tarification |
| 15 | Provisions pour risques et charges | Crédit | Débit | Litige, remise en état |
| 16 | Emprunts | Crédit (déblocage) | Débit (remboursement) | + intérêts courus (ICNE) à la clôture |
| **18** | **Comptes de liaison entre structures** | — | — | Opérations **inter-structures (IS)** ; total consolidé **nul** |
| **19** | **Fonds dédiés ou reportés** | Crédit (part non utilisée au 31/12) | Débit (reprise quand on dépense) | Projet sur plusieurs années |
| 20, 21 | Immobilisations (logiciels ; bâtiments, véhicules, mobilier, informatique) | Débit (achat) | Crédit (vente, mise au rebut) | Véhicule acheté au garage Martin |
| 23 | Immobilisations en cours (travaux pas finis) | Débit | Crédit (transfert en 21) | Rénovation des locaux |
| 27 | Dépôts de garantie, parts sociales | Débit | Crédit | Caution du loyer, d'EDF |
| 28 | Amortissements | Crédit | Débit (sortie du bien) | Déversés par EIG IMMOS |
| 40 / 41 / 42 / 43 / 44 / 46 | Fournisseurs, clients, personnel, organismes sociaux, État, divers | Dettes : crédit ; créances : débit | Inverse | Tiers FO, LI, CL, SA |
| 47 | Comptes d'attente | — | — | **Soldés à chaque clôture** |
| 48 | Charges et produits constatés d'avance | — | — | Assurance d'avril N à mars N+1 |
| 49 | Dépréciations de créances | Crédit | Débit (reprise) | Client qui ne paiera pas |
| 50 / 51 / 53 / 58 | Placements, banques, caisse, virements internes | Débit (entrée d'argent) | Crédit (sortie) | 58 : **solde nul** au 31/12 |
| 6 | Charges | **Débit** | Crédit (avoir, extourne, **6419**) | Électricité, honoraires, salaires |
| 7 | Produits | **Crédit** | Débit (avoir accordé à un client) | Dotations, subventions, dons |

> 💡 Réflexe senior : le document T21 cite **deux exceptions** au « charges au débit ».
>
> 1. Les **6419000 / 6419100** (IJSS et prévoyance) sont des **charges négatives**. Ce sont des remboursements que l'on saisit **au crédit** et qui diminuent les charges de personnel.
> 2. Les **extournes** du 1er janvier : on reprend au crédit les charges rattachées à l'année précédente.
>
> Une charge au crédit, en dehors de ces cas et des avoirs, doit vous alerter.

---

## 2. Cinq structures, une association

L'association est **une seule personne morale** mais tient **une comptabilité par structure**. Dans le dossier d'entraînement :

| Structure | Code | Financeur |
|---|---|---|
| Siège | SIE | Frais de siège payés par les autres structures |
| SESSAD | SES | ARS |
| SAVS | SAV | Département |
| Emploi accompagné | EMP | ARS et AGEFIPH-FIPHFP |
| Association et projets | ASS | Adhérents, donateurs, fondations |

Le détail est dans la [fiche du dossier](fiche_dossier_5_structures.md).

**Pourquoi c'est important :**

- L'ARS ne finance que le SESSAD et veut voir **ses** comptes.
- Le Département ne finance que le SAVS.
- Une charge saisie dans la mauvaise structure fausse **deux** comptes rendus à la fois. Il faut ensuite la corriger devant le commissaire aux comptes.

### 2.1 Les inter-structures (IS) : le mécanisme

Le document T21 l'explique ainsi :

> « si une dépense a été effectuée par le siège pour un service, ou si une facture adressée au siège concerne plusieurs structures, une opération d'inter-structure est comptabilisée via le renseignement du compte IS lors de la saisie comptable de l'opération. »

**Exemple.** Le contrat télécom est unique et facturé au siège : 900,00 € TTC pour novembre. Clé de répartition : les ETP (siège 9 %, SESSAD 48 %, SAVS 27 %, Emploi 12 %, Association 4 %).

**Livres du siège (SIE)** — journal AC :

| Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|
| 6262000 Frais de télécommunication | | Télécom nov. – part siège 9 % | 01-SIEGE | 81,00 | |
| 1849100 Liaison SESSAD | | Télécom nov. – IS SESSAD 48 % | | 432,00 | |
| 1849200 Liaison SAVS | | Télécom nov. – IS SAVS 27 % | | 243,00 | |
| 1849300 Liaison Emploi | | Télécom nov. – IS Emploi 12 % | | 108,00 | |
| 1849400 Liaison Association | | Télécom nov. – IS Asso 4 % | | 36,00 | |
| 4010000 Fournisseurs | FOORANGE | Télécom nov. – facture n° T-26-11-0451 | | | 900,00 |

**Livres du SESSAD (SES)** — journal OD (écriture « miroir », automatique ou manuelle selon le paramétrage EIG) :

| Compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|
| 6262000 Frais de télécommunication | Télécom nov. – IS reçue du siège | 10-SESSAD | 432,00 | |
| 1840000 Liaison Siège | Télécom nov. – IS reçue du siège | | | 432,00 |

Même chose dans les livres du SAVS (243,00), de l'Emploi (108,00) et de l'Association (36,00).

**Le contrôle qui ne pardonne pas :**

- Chez le siège, le **1849100 Liaison SESSAD** est **débiteur de 432,00**.
- Chez le SESSAD, le **1840000 Liaison Siège** est **créditeur de 432,00**.
- Les deux soldes sont **égaux et de sens contraire**.

Chaque fin de mois, comparez les comptes de liaison deux à deux. Un écart veut dire qu'une moitié d'IS manque : la recherche porte sur quelques écritures, pas sur un mois entier. C'est le contrôle n° 1 d'un dossier multi-structures.

### 2.2 Les frais de siège

Le siège n'a pas de financeur propre. Chaque ESSMS lui verse des **frais de siège**, au taux autorisé par l'autorité de tarification. Dans le dossier, ce taux est de **4,5 %** (taux fictif, voir M16).

Exemple : la quote-part du SAVS pour novembre est de 2 295,00 €.

| Livres de | Journal | Compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|
| SAV | OD | 6556000 Frais de siège social du gestionnaire | Frais de siège nov. 2026 | 2 295,00 | |
| SAV | OD | 1840000 Liaison Siège | Frais de siège nov. 2026 | | 2 295,00 |
| SIE | OD | 1849200 Liaison SAVS | Frais de siège nov. 2026 – SAVS | 2 295,00 | |
| SIE | OD | 7556000 Siège social du gestionnaire | Frais de siège nov. 2026 – SAVS | | 2 295,00 |

### 2.3 Le remboursement du siège

Le SAVS rembourse ensuite le siège par **virement entre les deux comptes bancaires** : 2 538,00 € (la quote-part de télécom de 243,00 € et les frais de siège de 2 295,00 €).

| Livres de | Journal | Compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|
| SAV | BQSAV | 1840000 Liaison Siège | Remboursement siège nov. | 2 538,00 | |
| SAV | BQSAV | 5123000 Banque SAVS *(automatique)* | Remboursement siège nov. | | 2 538,00 |
| SIE | BQSIE | 5121000 Banque Siège *(automatique)* | Remboursement SAVS nov. | 2 538,00 | |
| SIE | BQSIE | 1849200 Liaison SAVS | Remboursement SAVS nov. | | 2 538,00 |

> ⚠️ Erreur classique : passer ce virement par le **5800000 Virements internes**. Le 58 sert aux mouvements entre deux comptes de trésorerie **de la même structure** (exemple du document T21 : banque → caisse). Entre deux structures, on passe **toujours** par les comptes de **liaison**.

---

## 3. Les journaux : ce que vous saisissez, ce que vous ne saisissez jamais

| Journal | Type | Vous saisissez… |
|---|---|---|
| **Achats** | Avec contrepartie (débits **et** crédits) | Factures FO, factures LI, notes de frais SA, achats d'immobilisations |
| **Ventes** | **Automatique** (EIG Gestion commerciale) — **Fédération seulement** | **Rien.** Vous **contrôlez** le déversement |
| **Banque compte courant** | Contrepartie **automatique** (512) | Une ligne par opération du relevé |
| **Banque placement** | Contrepartie automatique, un journal par placement | Versements, retraits, intérêts |
| **Caisse** | Comme la banque | Opérations en espèces |
| **Salaires (paie)** | **Automatique** (EIG RH) | **Rien. Aucune écriture manuelle autorisée.** Vous contrôlez |
| **À-nouveaux provisoires**, puis **reprise des à-nouveaux** | **Automatiques** | Rien. Le provisoire est régénérable tant que N-1 n'est pas clos ; la reprise l'écrase à la clôture de N-1 |
| **Immobilisations** | **Automatique** (EIG IMMOS) | Rien. Les dotations aux amortissements et les sorties viennent d'IMMOS |
| **Opérations diverses (OD)** | Avec contrepartie | Tout le reste : régularisations, IS, frais de siège, fin d'exercice, reclassements |

> 💡 Réflexe senior : **une erreur dans un journal automatique se corrige à la source.** Exemple : un salaire mal imputé se corrige dans EIG RH, puis la paie est re-déversée. Ne le corrigez **pas** par une OD dans la comptabilité, sinon la paie et la comptabilité ne concordent plus et l'écart revient chaque mois. Si une OD est vraiment indispensable (reclassement analytique demandé par l'expert-comptable), elle est **documentée** et **validée**.

!!! tip "Le piège du journal de banque à contrepartie automatique"
    Vous ne saisissez **que la contrepartie** ; le logiciel ajoute la ligne 512.

    - Paiement de LIDUPONT pour 480,00 € : vous tapez **LIDUPONT au débit 480,00**, et EIG génère **512 au crédit 480,00**.
    - Réception de la dotation ARS de 98 333,33 € : vous tapez **7312130 au crédit 98 333,33**, et EIG génère **512 au débit**.

    C'est ce que le document veut dire par « saisies au débit pour les dépenses, et au crédit pour les recettes ».

---

## 4. Les comptes de tiers et le lettrage

| Préfixe | Centralisé en | Saisie de la pièce | Règlement |
|---|---|---|---|
| **FO** (fournisseurs) | 4010000 | FO au **crédit** | FO au **débit** |
| **LI** (libéraux) | 4011000 | LI au crédit | LI au débit |
| **SA** (salariés, notes de frais) | 4248000 | SA au crédit | SA au débit |
| **CL** (clients) | 4110000 | CL au **débit** | CL au **crédit** |

**Interdit** : saisir directement dans 4010000, 4011000, 4110000 ou 4248000. Ce sont des comptes de **centralisation**, alimentés automatiquement par les comptes de tiers.

**Le lettrage** consiste à rapprocher, dans un compte de tiers, la facture (au crédit) et son règlement (au débit) en leur donnant la même lettre (A, B, C…). Un compte FO bien tenu ne contient que des **factures non lettrées = factures pas encore payées**.

> 💡 Réflexe senior : chaque mois, regardez les **comptes de tiers au solde anormal**.
>
> - Un FO **débiteur** signale un double paiement, un avoir non utilisé ou une facture pas encore saisie.
> - Un SA débiteur signale une avance non régularisée.
> - Une facture non lettrée depuis plus de 60 jours signale un litige ou un oubli.

---

## 5. La saisie pas à pas, avec les exemples du document T21

### 5.1 Facture fournisseur (journal Achats)

Exemple du document : **facture d'électricité EDF**. On crédite **FOEDF** et on débite **6061200** Énergie, électricité. Facture du SESSAD (compteur propre) : 642,18 € TTC.

| Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|
| AC | 6061200 Énergie, électricité | | EDF – SESSAD Romans – F-88123 – oct. 2026 | 10-SESSAD | 642,18 | |
| AC | 4010000 Fournisseurs | FOEDF | EDF – SESSAD Romans – F-88123 – oct. 2026 | | | 642,18 |

**Toujours TTC** : la TVA n'est pas récupérable, il n'y a pas de compte 445 dans le plan.

**Achat d'une immobilisation**, autre exemple du document : un **véhicule** acheté au garage Martin. On crédite **FOMARTIN** et on débite **2182000** Matériel de transport. Exemple : 18 600,00 € TTC pour le SAVS.

| Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|
| AC | 2182000 Matériel de transport | | Garage Martin – Peugeot 208 SAVS – F-2026-311 | 20-SAVS | 18 600,00 | |
| AC | 4010000 Fournisseurs | FOMARTIN | Garage Martin – Peugeot 208 SAVS – F-2026-311 | | | 18 600,00 |

Ensuite, le bien est créé dans **EIG IMMOS** (date de mise en service, durée), et les amortissements arriveront automatiquement par le journal Immobilisations.

**L'avoir** s'écrit « à l'envers ». Avoir EDF de 85,40 € : **FOEDF au débit**, **6061200 au crédit**.

### 5.2 Facture d'un libéral (journal Achats)

Exemple du document : prestation d'orthophonie de **Mme Dupont**. On crédite **LIDUPONT** et on débite **6223221** Honoraires orthophonistes. Exemple : 12 séances à 40,00 € en octobre.

| Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|
| AC | 6223221 Honoraires orthophonistes | | Dupont – 12 séances oct. 2026 – relevé n° 10 | 10-SESSAD | 480,00 | |
| AC | 4011000 Libéraux | LIDUPONT | Dupont – 12 séances oct. 2026 – relevé n° 10 | | | 480,00 |

> 💡 Réflexe senior : avant de saisir un relevé de libéral, **pointez chaque séance** sur le planning du SESSAD et vérifiez le **tarif de la convention**. Les erreurs classiques sont les suivantes : une séance facturée pendant que l'enfant était absent, une séance facturée deux fois, ou un enfant dont l'accompagnement est terminé. Dans les pièces, on désigne les enfants par leurs **initiales** (confidentialité).

### 5.3 Note de frais d'un salarié (journal Achats)

C'est l'exemple du document : **Nathalie Durand** présente une note avec des indemnités kilométriques et un achat de stylos et carnets.

- 182 km avec son véhicule de 5 CV, au taux retenu de 0,636 € par km (*barème indicatif, valeur à vérifier chaque année*) : 182 × 0,636 = 115,752, soit **115,75 €**.
- Stylos et carnets : **23,40 €** TTC, ticket joint.
- Total : **139,15 €**.

| Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|
| AC | 6251000 Voyages et déplacements | | NDF Durand oct. 2026 – 182 km | 10-SESSAD | 115,75 | |
| AC | 6062400 Fournitures administratives | | NDF Durand oct. 2026 – stylos, carnets | 10-SESSAD | 23,40 | |
| AC | 4248000 Salariés – NDF | SADURAND | NDF Durand oct. 2026 | | | 139,15 |

Au remboursement par virement (journal BQSES) : **SADURAND au débit 139,15**, et la banque est générée automatiquement. Lettrez ensuite le compte SADURAND.

> ⚠️ Erreur classique : rembourser une note de frais par la **paie** et **aussi** par virement. Choisissez un seul circuit. Chez T21, c'est le compte **SA** et le virement. Vérifiez aussi qu'il y a le **visa du supérieur** (pour la directrice : le président ou la trésorière), les **justificatifs**, et qu'aucun carburant n'est demandé pour un véhicule de service déjà payé par la carte carburant.

### 5.4 Le journal de banque, ligne par ligne

| Opération sur le relevé | Vous saisissez (contrepartie) | Sens de votre ligne |
|---|---|---|
| Paiement d'une facture fournisseur ou libéral | FO… ou LI… | Débit |
| Remboursement d'une note de frais | SA… | Débit |
| Achat par carte **sans facture** (ticket de caisse + ticket CB), ex. carburant | **6062100** directement | Débit |
| Frais bancaires | **6270000** | Débit |
| Intérêts d'emprunt prélevés | **6611000** (et 1640000 pour le capital) | Débit |
| Règlement d'un client | CL… | Crédit |
| Dotation de l'ARS ou du Département | **731xxxx** | Crédit |
| Subvention | **74xxxxx** | Crédit |
| Don | **7541xxx** | Crédit |
| IJSS de la CPAM | **6419000** | **Crédit** |
| Remboursement de la prévoyance (arrêt long) | **6419100** | **Crédit** |
| Virement d'une autre structure | **184xxxx** (liaison) | Crédit |
| Opération inconnue | **4710000** (attente, à solder vite) | Débit ou crédit |

### 5.5 Placements, caisse et virements internes

- **Placement** : un journal et un compte par placement (compte à terme, livret). Versement depuis le compte courant : sortie de banque vers le **5800000**, puis entrée du placement depuis le 5800000. Les intérêts vont en **7640000**.
- **Caisse** : retrait de 200,00 € pour alimenter la caisse.
  - Dans le journal BQ : **5800000 au débit 200,00** (la banque est générée au crédit).
  - Dans le journal CA : **5800000 au crédit 200,00** (la caisse est générée au débit).
  - Le 58 revient à **zéro**. Le document T21 interdit d'écrire directement 512 contre 53.
- Le solde de la caisse doit être **égal au comptage physique**. Faites un comptage à chaque fin de mois, signé par deux personnes.

---

## 6. La fin d'exercice selon les documents T21

| Situation | Écriture au 31/12/N | Au 01/01/N+1 |
|---|---|---|
| Prestation de N, facture datée de N+1 (**facture non parvenue**) | D 6xxxxxx / C **4081000** | **Extourne** : D 4081000 / C 6xxxxxx, puis saisie normale de la facture en FO ou LI |
| Assurance payée le 01/04/N pour avril N – mars N+1 (**charge constatée d'avance**) | D **4860000** / C 616xxxx pour 3/12 | Extourne |
| Subvention reçue en N pour une période de N+1 | D 74xxxxx / C **4878000** | Extourne |
| Produit acquis non reçu / charge due non facturée (hors fournisseurs, social, fiscal) | D **4676000** / C 7xxxxxx ou D 6xxxxxx / C **4686000** | Extourne |
| Intérêts d'emprunt courus non échus | D 6618000 / C **1648000** | Extourne |
| Intérêts de placement acquis non versés | D **5188000** / C 7640000 | Extourne |
| Subvention **affectée** non dépensée | D **6892200** / C **194xxxx / 195xxxx** | Reprise au rythme des dépenses : D 19xxxxx / C **7892200** |
| Congés payés acquis non pris | D 6412000 / C **4282000** + charges D 6451800 / C **4382000** | Selon la méthode retenue (ajustement annuel) |

**Les comptes qui doivent être à zéro au 31/12 :**

- **47** (attente) : document T21, « soldés à chaque fin d'exercice » ;
- **58** (virements internes) ;
- **18** (liaisons), au niveau consolidé de l'association.

!!! warning "Une phrase à lire avec attention dans le document T21"
    À propos du 4081000, le document écrit : *« Le compte 4081000 sera débité en exercice N, puis crédité en exercice N+1 »*. **C'est l'inverse.** Le 4081000 est un compte de **dette** : il est **crédité** en N, en contrepartie de la charge au débit, et **débité** en N+1 lors de l'extourne. L'idée du document est juste : la charge est bien rattachée à N. Seul le sens est inversé. Retrouvez les autres points de ce type dans l'[exercice E18-12](exercices/E18-12_lire-et-critiquer-les-documents-t21.md).

**L'affectation du résultat** (après la clôture) :

- Le résultat de l'année est en **12** : 1205000 ou 1295000 pour les ESSMS sous gestion contrôlée ; 1202000 ou 1292000 pour les activités non tarifées.
- Il passe ensuite en **report à nouveau** (115xxxx créditeur, 1159xxx débiteur) ou en **réserves** (1068522 investissement, 1068552 trésorerie, 1068562 compensation des déficits, 1068572 compensation des amortissements).
- Pour un service au **compte administratif**, c'est le **financeur qui décide**. Pour un service sous **CPOM**, l'association **propose** (voir M16 et l'exercice E17-08).

---

## 7. Comment travaille un senior

### 7.1 Les cinq contrôles d'une pièce, avant toute saisie

1. **Est-elle à notre nom et pour nous ?** Nom et adresse de l'association, site ou structure concernée, SIREN.
2. **Est-elle juste ?** Calculs, quantités, tarif de la convention ou du devis, période.
3. **Est-elle nouvelle ?** Numéro de facture déjà saisi ? Recherchez par fournisseur, numéro et montant.
4. **Est-elle validée ?** **Bon à payer** de la directrice, visa du chef de service.
5. **Où va-t-elle ?** Structure → compte → code analytique → IS éventuelle → immobilisation ou charge → période (N ou N+1).

### 7.2 Le rythme

| Fréquence | Tâche |
|---|---|
| Chaque jour ou deux | Saisie des achats validés ; banque **au fil de l'eau** (relevé de la veille) ; classement des pièces |
| Chaque semaine | Lettrage des tiers ; préparation de la campagne de paiement |
| Chaque mois | Notes de frais ; IS et frais de siège ; contrôle de la paie déversée ; **rapprochement bancaire** de chaque compte ; comptage de caisse ; **contrôle croisé des liaisons** ; 47 et 58 à zéro ; balance et suivi budgétaire |
| Chaque année | FNP, CCA, PCA, ICNE, fonds dédiés, congés payés ; extournes ; justification de chaque compte de bilan ; dossier pour l'expert-comptable et le CAC |

### 7.3 Analyser une balance : la méthode

1. **Les sens anormaux.** Un fournisseur débiteur, une banque créditrice (découvert ?), une charge créditrice hors 6419, un 58 ou un 47 non nul.
2. **Les comptes interdits.** Un solde sur un compte de centralisation sans tiers, un 445 (n'existe pas), un 601 ou un 603 (pas de stocks).
3. **N contre N-1 et contre le budget.** Une charge en hausse de 30 % : pourquoi ? Une ligne à zéro alors qu'elle existait l'an dernier : oubli ? Le budget (EPRD, BP) est la référence du financeur.
4. **Les liaisons.** Siège contre structure, deux à deux.
5. **La cohérence entre structures.** Des honoraires d'orthophonie dans le SAVS ? Des frais de siège manquants pour un mois ?
6. **Descendre dans le grand livre.** Pour chaque anomalie, retrouvez l'écriture, la pièce et la personne qui l'a saisie, puis corrigez par une OD **libellée et justifiée**.

> 💡 Réflexe senior : notez **chaque** correction dans un **fichier de révision** : date, compte, montant, raison, pièce. Au moment de la clôture, l'expert-comptable et le commissaire aux comptes vous demanderont « pourquoi cette OD ? ». La réponse doit être écrite, pas dans votre mémoire.

---

## 8. Ce qu'un senior remarque dans les trois documents

Lire un document interne avec un œil critique fait partie du métier. Voici les points relevés. L'[exercice E18-12](exercices/E18-12_lire-et-critiquer-les-documents-t21.md) les travaille en détail.

| Où | Ce qui est écrit | Ce qu'il faut comprendre |
|---|---|---|
| Document « comptabilité », classe 40 | 4081000 « débité en N, crédité en N+1 » | Sens inversé : crédité en N, débité en N+1 |
| Document « comptabilité », classe 50 | Souscription « débité », libération « débité » | À la libération, le placement est **crédité** |
| Document « comptabilité », classe 43 | Charges sociales « à reverser à l'État » | Elles se versent aux **organismes sociaux** (URSSAF, retraite, prévoyance, mutuelle) ; l'État, c'est la classe 44 |
| Document « comptabilité », classe 27, et plan | Parts sociales du Crédit Mutuel en 27 | Le plan a aussi **5040000** « PSB CME (parts sociales) » : quel compte utiliser ? |
| Plan | Mis à jour le 13/10/2025, « applicable au 1/01/2025 » | L'arrêté de référence est du 19/12/2025, applicable en 2026 : mise à jour à prévoir |
| Plan | 4710000 et 4730000 « Comptes d'attente » ; 4671XXX et 4676000, même libellé | Doublons apparents : lequel utiliser, et pour quoi ? |
| Plan | Une seule subdivision de dotation : **7312130** | Un SAVS relève d'une autre catégorie : quel compte de dotation pour lui ? |
| Plan | « sattutaires », « aur autres charges » | Coquilles sans conséquence comptable |

> 💡 Réflexe senior : on ne dit **jamais** « votre document est faux ». On écrit plutôt : *« En préparant la clôture, j'ai relevé trois points dans la procédure que je voudrais vérifier avec vous, pour être sûre d'appliquer la bonne règle »*. Le ton est constructif, chaque point est daté, et vous proposez une correction.

---

## 9. Les exercices du module

| N° | Exercice | Ce que vous apprenez |
|---|---|---|
| E18-01 | [Quel journal, quelle structure ?](exercices/E18-01_quel-journal-quelle-structure.md) | Classer 20 opérations ; manuel ou automatique |
| E18-02 | [Factures fournisseurs : saisie](exercices/E18-02_factures-fournisseurs-saisie.md) | Factures réelles, IS, immobilisation ou charge, facture à bloquer |
| E18-03 | [Factures de libéraux et avoirs](exercices/E18-03_factures-liberaux-avoirs.md) | Contrôler un relevé de séances, saisir les LI |
| E18-04 | [Notes de frais](exercices/E18-04_notes-de-frais.md) | Calculer, contrôler, saisir et rembourser les SA |
| E18-05 | [Relevé bancaire du SESSAD](exercices/E18-05_releve-bancaire-sessad.md) | Saisie en contrepartie automatique, IJSS, rapprochement |
| E18-06 | [Ventes, clients et produits](exercices/E18-06_ventes-clients-federation-et-produits.md) | Contrôler un journal automatique ; dotations, subventions, dons |
| E18-07 | [Inter-structures : les 5 structures](exercices/E18-07_inter-structures-5-structures.md) | Répartir les factures communes, frais de siège, liaisons à zéro |
| E18-08 | [Caisse, virements internes, placements](exercices/E18-08_caisse-virements-internes-placements.md) | Le compte 58, la caisse, le compte à terme |
| E18-09 | [Travaux de fin d'exercice T21](exercices/E18-09_travaux-fin-exercice-t21.md) | FNP, CCA, PCA, ICNE, fonds dédiés, extournes |
| E18-10 | [Réviser une balance comme un senior](exercices/E18-10_revision-balance-analyse-senior.md) | Trouver 10 anomalies, les corriger |
| E18-11 | [Cas de synthèse : un mois complet](exercices/E18-11_cas-synthese-mois-complet-5-structures.md) | Tout le mois de novembre, 5 structures |
| E18-12 | [Lire et critiquer les documents T21](exercices/E18-12_lire-et-critiquer-les-documents-t21.md) | Analyse critique des procédures réelles |

---

## Checklist de fin de module

- [ ] Je sais dire, pour une pièce, **la structure, le journal, le compte, le tiers, le code analytique**, dans cet ordre.
- [ ] Je ne saisis **jamais** dans 4010000, 4011000, 4110000 ou 4248000, et **jamais** dans les journaux de paie, de ventes, d'immobilisations ou d'à-nouveaux.
- [ ] Je saisis les factures **TTC** (pas de TVA récupérable, pas de 445).
- [ ] Je connais les comptes T21 du quotidien : 6061200, 6062100, 6062400, 6062500, 6223221, 6251000, 6256000, 6262000, 6270000, 6419000, 7312130, 74xxxxx, 7541xxx.
- [ ] Je sais passer une **IS** dans les livres du siège **et** dans ceux de la structure, et vérifier que les liaisons se compensent.
- [ ] Je sais pourquoi un virement entre deux structures passe par le **18** et un retrait pour la caisse par le **58**.
- [ ] Je sais passer les écritures de fin d'année (4081000, 4860000, 4878000, 1648000, 5188000, 6892200 / 19x) et leurs extournes.
- [ ] Je sais analyser une balance : sens anormaux, comptes interdits, N-1, budget, liaisons.
- [ ] Je sais signaler une incohérence dans une procédure **avec diplomatie**.
