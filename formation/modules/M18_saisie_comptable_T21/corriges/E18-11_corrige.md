# Corrigé E18-11 — Cas de synthèse : tout le mois de novembre 2026 dans les 5 structures

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
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQEMP** | Journal de banque de l'emploi accompagné. Contrepartie automatique 5124000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **DAB** | Distributeur automatique de billets. Retrait d'espèces : à justifier (alimentation de la caisse ou prélèvement de l'exploitant). |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IK** | Indemnités kilométriques. Remboursement des kilomètres faits avec sa voiture personnelle pour le travail, selon un barème (prix par km). Compte 6251. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PA** | Plateforme agréée — ou, dans le M18, journal de paie. Opérateur agréé par l'État (anciennement « PDP ») qui transmet les factures électroniques entre entreprises et envoie les données à l'administration. Dans le module M18, PA est le code du journal des salaires, alimenté automatiquement par EIG RH. |
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
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 754** | Dons manuels (ou collectes). Dons des particuliers (numéro selon la nomenclature ANC 2018-06). |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 1960000** | Fonds dédiés sur ressources liées à la générosité du public (plan T21). Dons du public affectés à un projet et non utilisés. |
    | **Compte 2183000** | Matériel de bureau et matériel informatique (plan T21). Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. |
    | **Compte 2818300** | Amort Matériel de bureau et matériel informatique (plan T21). Amortissements cumulés du matériel informatique. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4210000** | Personnel - Rémunérations dues (plan T21). Salaires nets à payer. Crédité par la paie, débité au virement des salaires. |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4730000** | Comptes d’attente (plan T21). Second compte d'attente (même libellé que 4710000 : à clarifier). Même règle : soldé au 31/12. |
    | **Compte 5081100** | Compte à terme du siège (dossier M18, fictif). Placement du siège, sous-compte du 5081XXX du plan T21 ; journal PLSIE. |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5124000** | Banque de l'emploi accompagné (dossier M18, fictif). Compte bancaire de l'emploi accompagné, journal BQEMP. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 5300000** | Caisse (plan T21). Caisse (espèces). Le solde doit être égal au comptage physique. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6062200** | Produits d’entretien (plan T21). Produits d'entretien et d'hygiène. |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6062500** | Fournitures scolaires, éducatives et de loisirs (plan T21). Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. |
    | **Compte 6132000** | Locations immobilières (plan T21). Loyer des locaux. |
    | **Compte 6140000** | Charges locatives et de copropriété (plan T21). Charges locatives et de copropriété refacturées par le bailleur. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6223222** | Honoraires Psycho-motriciens (plan T21). Honoraires de psychomotriciens. |
    | **Compte 6223224** | Honoraires Psychologues (plan T21). Honoraires de psychologues. |
    | **Compte 6226010** | Honoraires comptabilité (plan T21). Honoraires de l'expert-comptable (et du commissaire aux comptes, faute de compte dédié dans le plan : à vérifier). |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6256000** | Missions (plan T21). Repas et hébergement en mission. |
    | **Compte 6262000** | Frais de télécommunication (plan T21). Téléphone, internet. |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6556000** | Frais de siège social du gestionnaire (plan T21). Frais de siège facturés par le siège à la structure (taux autorisé par le financeur). |
    | **Compte 6811200** | Dot Amorts Immobilisations corporelles (plan T21). Amortissement de l'année des biens corporels. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7312170** | Dotation du SAVS (dossier M18, numéro fictif). Le plan T21 ne prévoit que 7312130 (services pour enfants). Pour le SAVS, une autre subdivision 7312xxx est nécessaire : à vérifier dans le plan de l'association. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7541200** | Dons Autres projets (plan T21). Dons pour d'autres projets. |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
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
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **Frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **habitat inclusif** | Logement partagé en milieu ordinaire. Des personnes handicapées vivent ensemble chez elles, avec un projet de vie partagé animé par l'association. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-11](../exercices/E18-11_cas-synthese-mois-complet-5-structures.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

!!! abstract "En clair"
    Devant une bannette mélangée, on ne saisit pas dans l'ordre d'arrivée. On **trie** d'abord : **1. quelle structure ?** **2. quel journal ?** **3. quel compte et quel code analytique ?** On écarte les pièces qui ne doivent pas être saisies (duplicata, paie). Ensuite seulement on saisit, **structure par structure**, et on finit par les **contrôles** (banques, tiers, liaisons).

### Question 1 — Tableau de tri

| Pièce | Structure(s) | Journal | Comptes | Remarque |
|---|---|---|---|---|
| P1 Loyer FOFONCIA | SIE + IS vers les 4 autres | AC (siège), OD (miroirs) | 6132000, 6140000, 184x / 1840000 | Facture commune, clé **m²** |
| P2 Télécom FOORANGE | SIE + IS | AC, OD | 6262000 | Clé **ETP** ; montant **TTC** (la TVA indiquée n'est pas récupérable) |
| P3 Honoraires FOFERRAND | SIE + IS | AC, OD | 6226010 | Clé **forfait** |
| P4 Relevé BQSIE | SIE | BQSIE | FOFONCIA ; 1849200 | Le virement reçu du SAVS va en **liaison**, pas en 58 |
| P5 Frais de siège | SIE + SES, SAV, EMP | OD | 7556000 (siège) ; 6556000 (structures) | ASS non concernée |
| P6 LIDUPONT | SES | AC | 6223221 | |
| P7 LIMOREAUPSY | SES | AC | 6223222 | |
| P8 FOLUDIK | SES | AC | 6062500 | **486,90 € TTC** : sous le seuil, charge |
| P9 NDF SADURAND | SES | AC | 6251000, 6256000, 6062400 | Tiers **SA** |
| P10 Relevé BQSES | SES | BQSES | 7312130 ; 6419000 | IJSS au **crédit** |
| P11 a) LIBENALI SB-2026-11 | SAV | AC | 6223224 | |
| P11 b) Duplicata SB-2026-10 | — | **Ne pas saisir** | — | Déjà saisie le 04/11 : la saisir créerait un **doublon** (et un double paiement). Tamponner « DUPLICATA – déjà comptabilisé » |
| P12 FOTOTALCARTE | SAV | AC | 6062100 | Relevé avec facture → tiers FO (pas de saisie directe en banque) |
| P13 Relevé BQSAV | SAV | BQSAV | 7312170 ; 1840000 | Remboursement au siège = **liaison** |
| P14 NDF SAHADDAD | **ASS** (40-HABITAT) | AC | 6062200, 6251000 | Le salarié est payé par le SAVS, mais la **dépense** est celle de l'habitat inclusif |
| P15 NDF SAMARCHETTI | EMP | AC | 6251000, 6256000 | |
| P16 Relevé BQEMP | EMP | BQEMP | 7488000 | |
| P17 Ordinateur FOINFORHONE | EMP | AC (puis fiche EIG IMMOS) | 2183000 | **1 089,00 € TTC** > 500,00 € : immobilisation, **TTC** |
| P18 Relevé BQASS + caisse | ASS | BQASS et CAASS | 7541200 ; 5800000 | Retrait = mouvement entre 512 et 53 de la **même** structure → **58** |
| P19 Paie | Les 5 | PA (automatique) | — | **Contrôler, ne rien saisir** |

### Pourquoi P14 va dans ASS

Rachid Haddad est salarié du SAVS, mais il a acheté des produits d'entretien et roulé pour **l'habitat inclusif**, qui appartient à la structure **ASS** (code 40-HABITAT, financé par l'aide à la vie partagée du Département). Saisir sa note dans le SAVS ferait payer au budget du SAVS une dépense de l'habitat inclusif. On la saisit donc **dans ASS**, sur le compte SAHADDAD de cette structure (la fiche prévoit ce cas), et c'est la banque de ASS qui la rembourse. *Si son temps de travail pour l'habitat est régulier, son salaire devrait d'ailleurs faire l'objet d'une refacturation (IS) entre SAV et ASS : question à poser à la directrice.*

### Question 4 — Le contrôle du déversement de paie (P19)

| Contrôle | Résultat | Verdict |
|---|---|---|
| Net à payer (4210000) = virement des salaires du 27/11, par structure | Égalité dans les 5 structures | ✓ Le 4210000 est soldé |
| Charges patronales / brut | SIE 31,0 % · SES 31,0 % · SAV 31,0 % · EMP 31,0 % · **ASS 0,0 %** | **Anomalie** : aucune cotisation patronale déversée pour ASS alors qu'il y a 3 120,00 € de salaires |
| Lignes particulières | SES : 6419000 IJSS subrogation **642,18 € au crédit** dans le journal PA | **Anomalie** : la même IJSS est arrivée en banque le 20/11 et, selon le document T21, se saisit **en banque** au crédit du 6419000. Si l'on garde les deux, l'IJSS est comptée **deux fois** (1 284,36 € au lieu de 642,18 €) |

**Ce qu'on fait** : on saisit la ligne bancaire du 20/11 comme le prévoit le document T21 (6419000 au crédit) et on **signale** les deux anomalies au service paie (ou au cabinet qui gère EIG RH) par écrit : (1) paramétrage des cotisations patronales de la structure ASS (risque : cotisations calculées mais non comptabilisées, ou pire non déclarées) ; (2) suppression de la ligne 6419000 du déversement, ou, si l'association choisit que la paie constate l'IJSS à recevoir, la banque devra alors créditer le compte de tiers utilisé par la paie, et non le 6419000. Un seul circuit, pas deux.

**Ce qu'on ne fait surtout pas** : passer une écriture manuelle dans le journal **PA** (interdit : journal automatique) ou « corriger » à la main sans accord. La correction vient d'un **nouveau déversement** après correction du paramétrage ; à défaut avant la clôture du mois, une OD de correction **validée par l'expert-comptable**, documentée.

## 2. Calculs (détaillés, chaque montant justifié)

**Répartition des factures communes**

| Pièce | Total | SIE | SES | SAV | EMP | ASS |
|---|---|---|---|---|---|---|
| P1 Loyer (m²) | 5 400,00 € | 810,00 € | 2 430,00 € | 1 350,00 € | 540,00 € | 270,00 € |
| P1 Charges locatives (m²) | 800,00 € | 120,00 € | 360,00 € | 200,00 € | 80,00 € | 40,00 € |
| P2 Télécom (ETP) | 1 450,00 € | 130,50 € | 696,00 € | 391,50 € | 174,00 € | 58,00 € |
| P3 Honoraires (forfait) | 2 160,00 € | 432,00 € | 864,00 € | 432,00 € | 216,00 € | 216,00 € |
| P5 Frais de siège | 9 112,50 € | — | 5 175,00 € | 2 587,50 € | 1 350,00 € | — |
| **IS reçues par structure** | | | **9 525,00 €** | **4 961,00 €** | **2 360,00 €** | **584,00 €** |

**Autres calculs**

| Pièce | Calcul | Montant |
|---|---|---|
| P6 | 22 × 34,00 | 748,00 € |
| P7 | 16 × 38,00 | 608,00 € |
| P8 | 405,75 + 81,15 | 486,90 € TTC |
| P9 | 412 × 0,50 = 206,00 ; + parking 8,60 = 214,60 (6251000) ; repas 18,90 (6256000) ; fournitures 23,40 (6062400) | 256,90 € |
| P11 a) | 4 × 240,00 | 960,00 € |
| P14 | 96 × 0,50 = 48,00 (6251000) ; produits d'entretien 38,60 (6062200) | 86,60 € |
| P15 | 2 × 24,50 = 49,00 (6251000) ; repas 17,80 (6256000) | 66,80 € |
| P17 | 907,50 + 181,50 | 1 089,00 € TTC |
| P19 | charges / brut : 5 778,40 / 18 640,00 = 31,0 % ; 31 576,60 / 101 860,00 = 31,0 % ; 9 033,40 / 29 140,00 = 31,0 % ; 3 741,70 / 12 070,00 = 31,0 % ; 0,00 / 3 120,00 = 0 % | |

## 3. Écritures comptables

*Les comptes de tiers sont indiqués entre parenthèses derrière leur compte de centralisation. Dans les journaux de banque et de caisse (contrepartie automatique), la ligne 512xxxx ou 5300000 est générée par le logiciel : elle est reproduite pour montrer l'équilibre.*

### A. Siège (SIE)

**A1. Factures communes avec IS (journal AC)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 02/11/2026 | SIE | AC | 6132000 | Locations immobilières | FOFONCIA – loyer Valence – FR-26-1102 – 11/2026 – part siège 15 % | 01-SIEGE | 810,00 | |
| 02/11/2026 | SIE | AC | 6140000 | Charges locatives et de copropriété | FOFONCIA – charges – FR-26-1102 – 11/2026 – part siège 15 % | 01-SIEGE | 120,00 | |
| 02/11/2026 | SIE | AC | 1849100 | Liaison SESSAD | FOFONCIA – FR-26-1102 – IS SESSAD 45 % | | 2 790,00 | |
| 02/11/2026 | SIE | AC | 1849200 | Liaison SAVS | FOFONCIA – FR-26-1102 – IS SAVS 25 % | | 1 550,00 | |
| 02/11/2026 | SIE | AC | 1849300 | Liaison Emploi | FOFONCIA – FR-26-1102 – IS Emploi 10 % | | 620,00 | |
| 02/11/2026 | SIE | AC | 1849400 | Liaison Association | FOFONCIA – FR-26-1102 – IS Asso 5 % | | 310,00 | |
| 02/11/2026 | SIE | AC | 4010000 | Fournisseurs FO (tiers FOFONCIA) | FOFONCIA – loyer et charges – FR-26-1102 – 11/2026 | | | 6 200,00 |
| 06/11/2026 | SIE | AC | 6262000 | Frais de télécommunication | FOORANGE – flotte – 26-11-778412 – 11/2026 – part siège 9 % | 01-SIEGE | 130,50 | |
| 06/11/2026 | SIE | AC | 1849100 | Liaison SESSAD | FOORANGE – 26-11-778412 – IS SESSAD 48 % | | 696,00 | |
| 06/11/2026 | SIE | AC | 1849200 | Liaison SAVS | FOORANGE – 26-11-778412 – IS SAVS 27 % | | 391,50 | |
| 06/11/2026 | SIE | AC | 1849300 | Liaison Emploi | FOORANGE – 26-11-778412 – IS Emploi 12 % | | 174,00 | |
| 06/11/2026 | SIE | AC | 1849400 | Liaison Association | FOORANGE – 26-11-778412 – IS Asso 4 % | | 58,00 | |
| 06/11/2026 | SIE | AC | 4010000 | Fournisseurs FO (tiers FOORANGE) | FOORANGE – flotte – 26-11-778412 – 11/2026 | | | 1 450,00 |
| 10/11/2026 | SIE | AC | 6226010 | Honoraires comptabilité | FOFERRAND – compta et paie – HF-2026-311 – 11/2026 – part siège 20 % | 01-SIEGE | 432,00 | |
| 10/11/2026 | SIE | AC | 1849100 | Liaison SESSAD | FOFERRAND – HF-2026-311 – IS SESSAD 40 % | | 864,00 | |
| 10/11/2026 | SIE | AC | 1849200 | Liaison SAVS | FOFERRAND – HF-2026-311 – IS SAVS 20 % | | 432,00 | |
| 10/11/2026 | SIE | AC | 1849300 | Liaison Emploi | FOFERRAND – HF-2026-311 – IS Emploi 10 % | | 216,00 | |
| 10/11/2026 | SIE | AC | 1849400 | Liaison Association | FOFERRAND – HF-2026-311 – IS Asso 10 % | | 216,00 | |
| 10/11/2026 | SIE | AC | 4010000 | Fournisseurs FO (tiers FOFERRAND) | FOFERRAND – compta et paie – HF-2026-311 – 11/2026 | | | 2 160,00 |
| | | | | | **Total** | | **9 810,00** | **9 810,00** |

**A2. Frais de siège de novembre (journal OD)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SIE | OD | 1849100 | Liaison SESSAD | Frais de siège 11/2026 – SESSAD | | 5 175,00 | |
| 30/11/2026 | SIE | OD | 1849200 | Liaison SAVS | Frais de siège 11/2026 – SAVS | | 2 587,50 | |
| 30/11/2026 | SIE | OD | 1849300 | Liaison Emploi | Frais de siège 11/2026 – Emploi accompagné | | 1 350,00 | |
| 30/11/2026 | SIE | OD | 7556000 | Siège social du gestionnaire | Frais de siège 11/2026 – SES, SAV, EMP | 01-SIEGE | | 9 112,50 |
| | | | | | **Total** | | **9 112,50** | **9 112,50** |

**A3. Banque du siège (journal BQSIE)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 05/11/2026 | SIE | BQSIE | 4010000 | Fournisseurs FO (tiers FOFONCIA) | FOFONCIA – prélèvement – FR-26-1102 – 11/2026 | | 6 200,00 | |
| 05/11/2026 | SIE | BQSIE | 5121000 | Crédit Mutuel – Siège | (ligne automatique) | | | 6 200,00 |
| 24/11/2026 | SIE | BQSIE | 5121000 | Crédit Mutuel – Siège | (ligne automatique) | | 8 000,00 | |
| 24/11/2026 | SIE | BQSIE | 1849200 | Liaison SAVS | Remboursement IS par le SAVS – virement du 24/11 | | | 8 000,00 |
| | | | | | **Total** | | **14 200,00** | **14 200,00** |

### B. SESSAD (SES)

**B1. Achats, libéraux, note de frais (journal AC)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SES | AC | 6223221 | Honoraires Orthophonistes | LIDUPONT – orthophonie 22 séances – CD-2026-11 – 11/2026 | 10-SESSAD | 748,00 | |
| 30/11/2026 | SES | AC | 4011000 | Libéraux LI (tiers LIDUPONT) | LIDUPONT – orthophonie – CD-2026-11 – 11/2026 | | | 748,00 |
| 30/11/2026 | SES | AC | 6223222 | Honoraires Psycho-motriciens | LIMOREAUPSY – psychomotricité 16 séances – JM-112026 – 11/2026 | 10-SESSAD | 608,00 | |
| 30/11/2026 | SES | AC | 4011000 | Libéraux LI (tiers LIMOREAUPSY) | LIMOREAUPSY – psychomotricité – JM-112026 – 11/2026 | | | 608,00 |
| 13/11/2026 | SES | AC | 6062500 | Fournitures scolaires, éducatives et de loisirs | FOLUDIK – matériel sensoriel – LE-2026-1244 – 11/2026 | 10-SESSAD | 486,90 | |
| 13/11/2026 | SES | AC | 4010000 | Fournisseurs FO (tiers FOLUDIK) | FOLUDIK – matériel sensoriel – LE-2026-1244 – 11/2026 | | | 486,90 |
| 30/11/2026 | SES | AC | 6251000 | Voyages et déplacements | SADURAND – IK 412 km et parking – NDF 11/2026 | 10-SESSAD | 214,60 | |
| 30/11/2026 | SES | AC | 6256000 | Missions | SADURAND – repas 19/11 – NDF 11/2026 | 10-SESSAD | 18,90 | |
| 30/11/2026 | SES | AC | 6062400 | Fournitures administratives | SADURAND – feutres et carnets – NDF 11/2026 | 10-SESSAD | 23,40 | |
| 30/11/2026 | SES | AC | 4248000 | Salariés - NDF (tiers SADURAND) | SADURAND – note de frais – NDF 11/2026 | | | 256,90 |
| | | | | | **Total** | | **2 099,80** | **2 099,80** |

*Les feutres et carnets servent aux séances avec les enfants : on pourrait aussi les classer en 6062500 « Fournitures scolaires, éducatives et de loisirs ». Le document T21 donne justement l'exemple de stylos et carnets en 6062400 ; l'essentiel est d'être constant.*

**B2. Banque du SESSAD (journal BQSES)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 06/11/2026 | SES | BQSES | 5122000 | Crédit Mutuel – SESSAD | (ligne automatique) | | 108 000,00 | |
| 06/11/2026 | SES | BQSES | 7312130 | ESSMS relevant du 2° du I de l'article L. 312-1 du CASF | ARS – dotation globale – 11/2026 | 10-SESSAD | | 108 000,00 |
| 20/11/2026 | SES | BQSES | 5122000 | Crédit Mutuel – SESSAD | (ligne automatique) | | 642,18 | |
| 20/11/2026 | SES | BQSES | 6419000 | Remboursements sur rémunération du personnel - IJSS | CPAM Drôme – IJSS subrogation – 11/2026 | 10-SESSAD | | 642,18 |
| | | | | | **Total** | | **108 642,18** | **108 642,18** |

**B3. IS reçues du siège (journal OD, miroirs)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 02/11/2026 | SES | OD | 6132000 | Locations immobilières | FOFONCIA – loyer 11/2026 – IS reçue du siège | 10-SESSAD | 2 430,00 | |
| 02/11/2026 | SES | OD | 6140000 | Charges locatives et de copropriété | FOFONCIA – charges 11/2026 – IS reçue du siège | 10-SESSAD | 360,00 | |
| 06/11/2026 | SES | OD | 6262000 | Frais de télécommunication | FOORANGE – flotte 11/2026 – IS reçue du siège | 10-SESSAD | 696,00 | |
| 10/11/2026 | SES | OD | 6226010 | Honoraires comptabilité | FOFERRAND – 11/2026 – IS reçue du siège | 10-SESSAD | 864,00 | |
| 30/11/2026 | SES | OD | 6556000 | Frais de siège social du gestionnaire | Frais de siège 11/2026 – IS reçue du siège | 10-SESSAD | 5 175,00 | |
| 30/11/2026 | SES | OD | 1840000 | Liaison Siège | IS reçues du siège – 11/2026 | | | 9 525,00 |
| | | | | | **Total** | | **9 525,00** | **9 525,00** |

### C. SAVS (SAV)

**C1. Achats (journal AC)** — le duplicata SB-2026-10 n'est **pas** saisi.

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | AC | 6223224 | Honoraires Psychologues | LIBENALI – 4 groupes de parole – SB-2026-11 – 11/2026 | 20-SAVS | 960,00 | |
| 30/11/2026 | SAV | AC | 4011000 | Libéraux LI (tiers LIBENALI) | LIBENALI – groupes de parole – SB-2026-11 – 11/2026 | | | 960,00 |
| 30/11/2026 | SAV | AC | 6062100 | Combustibles et carburants | FOTOTALCARTE – carburant véhicules SAVS – TC-2611-0457 – 11/2026 | 20-SAVS | 1 214,70 | |
| 30/11/2026 | SAV | AC | 4010000 | Fournisseurs FO (tiers FOTOTALCARTE) | FOTOTALCARTE – relevé – TC-2611-0457 – 11/2026 | | | 1 214,70 |
| | | | | | **Total** | | **2 174,70** | **2 174,70** |

**C2. Banque du SAVS (journal BQSAV)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 05/11/2026 | SAV | BQSAV | 5123000 | Crédit Mutuel – SAVS | (ligne automatique) | | 57 500,00 | |
| 05/11/2026 | SAV | BQSAV | 7312170 | Dotation SAVS (numéro fictif, voir fiche § 6) | Département de la Drôme – dotation globale – 11/2026 | 20-SAVS | | 57 500,00 |
| 24/11/2026 | SAV | BQSAV | 1840000 | Liaison Siège | Remboursement IS au siège – virement du 24/11 | | 8 000,00 | |
| 24/11/2026 | SAV | BQSAV | 5123000 | Crédit Mutuel – SAVS | (ligne automatique) | | | 8 000,00 |
| | | | | | **Total** | | **65 500,00** | **65 500,00** |

**C3. IS reçues du siège (journal OD, miroirs)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 02/11/2026 | SAV | OD | 6132000 | Locations immobilières | FOFONCIA – loyer 11/2026 – IS reçue du siège | 20-SAVS | 1 350,00 | |
| 02/11/2026 | SAV | OD | 6140000 | Charges locatives et de copropriété | FOFONCIA – charges 11/2026 – IS reçue du siège | 20-SAVS | 200,00 | |
| 06/11/2026 | SAV | OD | 6262000 | Frais de télécommunication | FOORANGE – flotte 11/2026 – IS reçue du siège | 20-SAVS | 391,50 | |
| 10/11/2026 | SAV | OD | 6226010 | Honoraires comptabilité | FOFERRAND – 11/2026 – IS reçue du siège | 20-SAVS | 432,00 | |
| 30/11/2026 | SAV | OD | 6556000 | Frais de siège social du gestionnaire | Frais de siège 11/2026 – IS reçue du siège | 20-SAVS | 2 587,50 | |
| 30/11/2026 | SAV | OD | 1840000 | Liaison Siège | IS reçues du siège – 11/2026 | | | 4 961,00 |
| | | | | | **Total** | | **4 961,00** | **4 961,00** |

### D. Emploi accompagné (EMP)

**D1. Note de frais et immobilisation (journal AC)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | EMP | AC | 6251000 | Voyages et déplacements | SAMARCHETTI – train Valence-Lyon forum emploi – NDF 11/2026 | 30-EMPLOI | 49,00 | |
| 30/11/2026 | EMP | AC | 6256000 | Missions | SAMARCHETTI – repas 17/11 – NDF 11/2026 | 30-EMPLOI | 17,80 | |
| 30/11/2026 | EMP | AC | 4248000 | Salariés - NDF (tiers SAMARCHETTI) | SAMARCHETTI – note de frais – NDF 11/2026 | | | 66,80 |
| 19/11/2026 | EMP | AC | 2183000 | Matériel de bureau et matériel informatique | FOINFORHONE – ordinateur portable chargée d'insertion – F-IRS-1119 | | 1 089,00 | |
| 19/11/2026 | EMP | AC | 4010000 | Fournisseurs FO (tiers FOINFORHONE) | FOINFORHONE – ordinateur portable – F-IRS-1119 – 11/2026 | | | 1 089,00 |
| | | | | | **Total** | | **1 155,80** | **1 155,80** |

*Pas de code analytique sur un compte de classe 2 : le code se met sur la **dotation aux amortissements** (6811200), qui portera 30-EMPLOI.*

**D2. Banque de l'Emploi accompagné (journal BQEMP)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 16/11/2026 | EMP | BQEMP | 5124000 | Crédit Mutuel – Emploi | (ligne automatique) | | 12 000,00 | |
| 16/11/2026 | EMP | BQEMP | 7488000 | Autres Subventions et participations | AGEFIPH – conv. 2026-EA-26-117 – 2e versement | 30-EMPLOI | | 12 000,00 |
| | | | | | **Total** | | **12 000,00** | **12 000,00** |

**D3. IS reçues du siège (journal OD, miroirs)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 02/11/2026 | EMP | OD | 6132000 | Locations immobilières | FOFONCIA – loyer 11/2026 – IS reçue du siège | 30-EMPLOI | 540,00 | |
| 02/11/2026 | EMP | OD | 6140000 | Charges locatives et de copropriété | FOFONCIA – charges 11/2026 – IS reçue du siège | 30-EMPLOI | 80,00 | |
| 06/11/2026 | EMP | OD | 6262000 | Frais de télécommunication | FOORANGE – flotte 11/2026 – IS reçue du siège | 30-EMPLOI | 174,00 | |
| 10/11/2026 | EMP | OD | 6226010 | Honoraires comptabilité | FOFERRAND – 11/2026 – IS reçue du siège | 30-EMPLOI | 216,00 | |
| 30/11/2026 | EMP | OD | 6556000 | Frais de siège social du gestionnaire | Frais de siège 11/2026 – IS reçue du siège | 30-EMPLOI | 1 350,00 | |
| 30/11/2026 | EMP | OD | 1840000 | Liaison Siège | IS reçues du siège – 11/2026 | | | 2 360,00 |
| | | | | | **Total** | | **2 360,00** | **2 360,00** |

### E. Association et projets (ASS)

**E1. Note de frais pour l'habitat inclusif (journal AC)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | ASS | AC | 6062200 | Produits d'entretien | SAHADDAD – produits entretien salle commune – NDF 11/2026 | 40-HABITAT | 38,60 | |
| 30/11/2026 | ASS | AC | 6251000 | Voyages et déplacements | SAHADDAD – IK 96 km habitat inclusif – NDF 11/2026 | 40-HABITAT | 48,00 | |
| 30/11/2026 | ASS | AC | 4248000 | Salariés - NDF (tiers SAHADDAD) | SAHADDAD – note de frais habitat – NDF 11/2026 | | | 86,60 |
| | | | | | **Total** | | **86,60** | **86,60** |

**E2. Banque et caisse de l'association (journaux BQASS et CAASS)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 09/11/2026 | ASS | BQASS | 5125000 | Crédit Mutuel – Association | (ligne automatique) | | 1 350,00 | |
| 09/11/2026 | ASS | BQASS | 7541200 | Dons Autres projets | Dons en ligne octobre – campagne Pairs et voix | 50-PAIRS | | 1 350,00 |
| 27/11/2026 | ASS | BQASS | 5800000 | Virements internes | Retrait DAB pour caisse marché de Noël | | 300,00 | |
| 27/11/2026 | ASS | BQASS | 5125000 | Crédit Mutuel – Association | (ligne automatique) | | | 300,00 |
| 27/11/2026 | ASS | CAASS | 5300000 | Caisse | (ligne automatique) | | 300,00 | |
| 27/11/2026 | ASS | CAASS | 5800000 | Virements internes | Entrée en caisse – retrait DAB 27/11 | | | 300,00 |
| | | | | | **Total** | | **1 950,00** | **1 950,00** |

*Le 5800000 de ASS revient à zéro dès que les deux moitiés (banque et caisse) sont saisies. Les dons étant collectés pour « Pairs et voix », ce sont des ressources **affectées** : la part non utilisée à la clôture pourra devoir être reportée en fonds dédiés (1960000 « ressources liées à la générosité du public »).*

**E3. IS reçues du siège (journal OD, miroirs)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 02/11/2026 | ASS | OD | 6132000 | Locations immobilières | FOFONCIA – loyer 11/2026 – IS reçue du siège | 90-ASSO | 270,00 | |
| 02/11/2026 | ASS | OD | 6140000 | Charges locatives et de copropriété | FOFONCIA – charges 11/2026 – IS reçue du siège | 90-ASSO | 40,00 | |
| 06/11/2026 | ASS | OD | 6262000 | Frais de télécommunication | FOORANGE – flotte 11/2026 – IS reçue du siège | 90-ASSO | 58,00 | |
| 10/11/2026 | ASS | OD | 6226010 | Honoraires comptabilité | FOFERRAND – 11/2026 – IS reçue du siège | 90-ASSO | 216,00 | |
| 30/11/2026 | ASS | OD | 1840000 | Liaison Siège | IS reçues du siège – 11/2026 | | | 584,00 |
| | | | | | **Total** | | **584,00** | **584,00** |

### Question 3 — L'ordinateur dans EIG IMMOS

- Créer la **fiche** dans EIG IMMOS : structure **EMP**, compte 2183000, date de mise en service (19/11/2026, ou la date de livraison), valeur **1 089,00 € TTC**, durée d'amortissement selon la procédure de l'association (par exemple 3 ans pour le matériel informatique — *à vérifier dans la procédure*), code analytique 30-EMPLOI, n° d'inventaire collé sur l'appareil.
- Le journal **IM** (automatique) générera la **dotation** (6811200 au débit, 2818300 au crédit) au calcul des amortissements, en général à la **clôture** (ou chaque mois si l'association a choisi des dotations mensuelles). On ne saisit **jamais** cette dotation à la main.
- Contrôle mensuel : total du 2183000 de chaque structure = total des fiches EIG IMMOS du même compte.

### Question 5 — Balance des comptes de liaison au 30/11/2026

| Livres | Compte | Solde au 31/10 | Mouvements de novembre | Solde débiteur au 30/11 | Solde créditeur au 30/11 |
|---|---|---|---|---|---|
| SIE | 1849100 Liaison SESSAD | 24 380,00 D | + 9 525,00 (IS) | 33 905,00 | |
| SIE | 1849200 Liaison SAVS | 9 875,40 D | + 4 961,00 (IS) − 8 000,00 (virement) | 6 836,40 | |
| SIE | 1849300 Liaison Emploi | 4 110,00 D | + 2 360,00 (IS) | 6 470,00 | |
| SIE | 1849400 Liaison Association | 1 120,00 C | + 584,00 (IS) | | 536,00 |
| SES | 1840000 Liaison Siège | 24 380,00 C | + 9 525,00 au crédit | | 33 905,00 |
| SAV | 1840000 Liaison Siège | 9 875,40 C | + 4 961,00 au crédit − 8 000,00 au débit | | 6 836,40 |
| EMP | 1840000 Liaison Siège | 4 110,00 C | + 2 360,00 au crédit | | 6 470,00 |
| ASS | 1840000 Liaison Siège | 1 120,00 D | + 584,00 au crédit | 536,00 | |
| **Total association** | | | | **47 747,40** | **47 747,40** |

Le total des soldes débiteurs égale celui des soldes créditeurs : les comptes 18 de toute l'association font **zéro** ✓. Chaque paire est l'exact opposé l'une de l'autre ✓.

**Lecture pour la directrice** : au 30/11, le SESSAD doit 33 905,00 € au siège, le SAVS 6 836,40 € et l'Emploi accompagné 6 470,00 € ; c'est le siège qui doit 536,00 € à l'Association. Proposition de remboursements de trésorerie début décembre (par virement entre comptes bancaires, **via les comptes de liaison**), en gardant une marge pour les IS de décembre.

## 4. Points d'attention / pièges

- **Le duplicata** (P11 b) : un document de relance n'est pas une nouvelle facture. Contrôle : n° de facture déjà présent dans le compte du tiers ? La saisie en double conduirait à **payer deux fois** (voir E18-10, garage Martin).
- **La TVA affichée** sur P2, P8 et P17 : elle est **incluse** dans la charge ou dans l'immobilisation (TTC). Aucun compte 445.
- **Le seuil d'immobilisation s'apprécie en TTC** dans une structure qui ne récupère pas la TVA : 1 089,00 € TTC → immobilisation ; 486,90 € TTC → charge.
- **Les virements entre structures** (P4/P13) passent par **1840000 / 1849200**, jamais par 5800000.
- **Le retrait pour la caisse** (P18) passe, lui, par **5800000**, car les deux comptes de trésorerie sont dans la **même** structure.
- **Les frais de siège** ne concernent pas ASS dans ce dossier ; ne les répartissez pas « par habitude » sur les cinq structures.
- **La paie** : on ne saisit rien dans PA ; on **contrôle** (net = virement, ratio de charges, lignes inhabituelles) et on **signale**.
- **La note de frais d'un salarié pour une autre structure** (P14) : la structure qui **porte la dépense** n'est pas forcément celle qui **paie le salaire**.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

### Question 6 — Check-list de fin de mois (à appliquer à chaque structure)

| N° | Contrôle | Comment | Fait |
|---|---|---|---|
| 1 | Toutes les pièces du mois saisies ou listées « en attente » avec leur motif | Bannette vide, tableau des pièces en attente | ☐ |
| 2 | Banques **rapprochées** (5121000 à 5125000, placement 5081100) | État de rapprochement signé, relevé joint | ☐ |
| 3 | Caisse CAASS = comptage physique | Feuille de comptage signée | ☐ |
| 4 | **5800000 = 0** dans chaque structure | Balance | ☐ |
| 5 | **4710000 et 4730000 = 0**, ou chaque ligne expliquée et datée | Grand livre | ☐ |
| 6 | Comptes **FO, LI, SA lettrés** ; aucun tiers débiteur sans explication ; aucune saisie directe sur 4010000, 4011000, 4248000 | Balances auxiliaires = comptes de centralisation | ☐ |
| 7 | **Paie** : PA déversé ; 4210000 soldé par les virements ; ratio charges / brut cohérent par structure ; pas de ligne en doublon avec la banque (6419000) | Récapitulatif EIG RH | ☐ |
| 8 | **IS du mois** : loyer, charges, télécom, honoraires, **frais de siège** (montant × nombre de mois) passés et **miroirs** présents | Balance de chaque structure | ☐ |
| 9 | **Liaisons** : 184x du siège = opposé du 1840000 de chaque structure ; total des 18 = 0 | Tableau de la question 5 | ☐ |
| 10 | **Dotations** reçues = douzièmes notifiés (7312130 SES, 7312170 SAV) | Arrêtés de tarification | ☐ |
| 11 | **Immobilisations** : 21xxxxx et 20xxxxx = fiches EIG IMMOS | Édition EIG IMMOS | ☐ |
| 12 | Aucun compte **hors plan T21** créé dans le mois (445, comptes à 6 chiffres…) | Liste des comptes créés | ☐ |
| 13 | Revue rapide des **charges par structure** vs budget proratisé et vs N-1 | Tableau de bord mensuel | ☐ |
| 14 | Point de **trésorerie** et proposition de remboursements entre structures | Tableau des liaisons | ☐ |
| 15 | Questions et anomalies **écrites** (paie, directrice, expert-comptable) | Liste des points en suspens | ☐ |

**Mail au service paie (anomalies P19) :**

> « Bonjour, en contrôlant le déversement de la paie de novembre, je relève deux points : (1) pour la structure Association et projets, aucune cotisation patronale n'a été déversée (salaires bruts 3 120,00 €, charges 0,00 €) : pouvez-vous vérifier le paramétrage des comptes de cotisations de cette structure, et nous confirmer que les cotisations ont bien été déclarées ? (2) pour le SESSAD, une ligne 6419000 « IJSS subrogation » de 642,18 € a été déversée ; or la procédure de la Fédération prévoit d'enregistrer les IJSS à leur encaissement en banque, au compte 6419000. La même somme serait donc comptée deux fois. Pouvez-vous supprimer cette ligne du paramétrage et régénérer le déversement ? Je ne passe aucune écriture dans le journal de paie en attendant. Merci, bonne journée. »

**Documentation** : classer chaque pièce avec son n° d'écriture ; tamponner le duplicata ; joindre à la check-list le tableau des liaisons et l'état de rapprochement de chaque banque.

## 6. Références

- Documents internes Trisomie 21 France (30/04/2026) : journal des achats (tiers FO, LI, SA ; immobilisations en classe 2), journaux de banque (dotations 731, subventions 74, dons 754, IJSS 6419 au crédit), journal de caisse, journal de paie automatique, journal des immobilisations (EIG IMMOS), classe 18 (IS) et classe 58 (virements internes).
- Plan comptable T21 France (MAJ 13/10/2025) : comptes utilisés ci-dessus.
- Fiche du dossier M18 : structures, comptes de banque et de liaison, clés de répartition, frais de siège, seuil d'immobilisation (hypothèses pédagogiques).
