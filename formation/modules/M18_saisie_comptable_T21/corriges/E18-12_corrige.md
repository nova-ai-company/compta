# Corrigé E18-12 — Lire et critiquer les documents comptables de Trisomie 21 France

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CAT** | Compte à terme. Placement bloqué pour une durée fixée, avec intérêts. Comptes 5081XXX dans le plan T21. |
    | **CFF** | Structure « CFF » de la Fédération. Code interne d'une structure de Trisomie 21 France (compte de liaison 1841200). Signification à demander. |
    | **CGI** | Code général des impôts. Le code qui contient toutes les règles fiscales (TVA, IS, IR…). « art. 39 CGI » = article 39 de ce code. |
    | **CME** | Crédit Mutuel (abréviation du plan T21). Banque coopérative : pour ouvrir un compte, on souscrit des parts sociales. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **CPOM** | Contrat pluriannuel d'objectifs et de moyens. Contrat de 5 ans entre une association et l'ARS et/ou le Département : objectifs, moyens, et budget présenté en EPRD. |
    | **DK** | Abréviation d'un lieu dans le plan T21. « SESSAD DK », « SAVS DK » : vraisemblablement Dunkerque. À faire confirmer. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ESMS** | Établissement ou service médico-social. Autre façon d'écrire ESSMS : une structure autorisée et financée par l'ARS et/ou le Département. |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **FIPHFP** | Fonds pour l'insertion des personnes handicapées dans la fonction publique. Finance l'emploi des personnes handicapées dans le secteur public (l'équivalent de l'AGEFIPH pour le public). |
    | **FNP** | Factures non parvenues. À la clôture : charges de l'année dont la facture n'est pas encore arrivée. On les enregistre quand même (compte 408) pour que l'année supporte ses vraies charges. |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N+1** | L'exercice suivant. L'année comptable d'après (ex. : si N = 2026, N+1 = 2027). Une charge « de N+1 » ne doit pas peser sur le résultat de N. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **PLSIE** | Journal de banque « placement » du siège. Un journal par placement : versements, retraits, intérêts du compte à terme 5081100. |
    | **PSB** | Parts sociales (abréviation du plan T21). Dans « PSB CME T21 France (parts sociales) », compte 5040000 : parts sociales détenues au Crédit Mutuel. |
    | **RAN** | Report à nouveau. Résultat d'un exercice pas encore affecté (comptes 115xxxx créditeurs, 1159xxx débiteurs dans le plan T21). |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIA** | Structure « SIA » de la Fédération. Code interne d'une structure de Trisomie 21 France (compte de liaison 1841100). Signification à demander. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **URSSAF** | Organisme de recouvrement des cotisations sociales. Collecte les cotisations sociales (maladie, famille, CSG…) des salariés et des indépendants. |
    | **Compte 641x** | Rémunérations du personnel (sous-comptes). Salaires, congés payés, indemnités. |
    | **Compte 754** | Dons manuels (ou collectes). Dons des particuliers (numéro selon la nomenclature ANC 2018-06). |
    | **Compte 791** | Transferts de charges. Compte SUPPRIMÉ depuis le PCG 2025 : ne plus l'utiliser. |
    | **Compte 4671XXX** | Comptes débiteurs et produits à recevoir (plan T21). Créances diverses et produits à recevoir (un sous-compte par débiteur). Libellé identique à 4676000 : à clarifier. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 1032000** | Fonds propres sattutaires avec droits de reprise (plan T21). Fonds propres de départ qu'un financeur peut reprendre si le service ferme. Le plan écrit « sattutaires » (coquille pour « statutaires »). |
    | **Compte 1068522** | Res invest - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve d'investissement : excédent d'un ESSMS mis de côté, sur décision du financeur, pour financer un investissement. |
    | **Compte 1068552** | Res tréso - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve de trésorerie : excédent affecté pour renforcer la trésorerie du service. |
    | **Compte 1068562** | Res compens déficits- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des déficits : couvre un futur déficit. Le document T21 indique qu'elle doit atteindre au moins 5 % de la dotation annuelle. |
    | **Compte 1068572** | Res compens amort- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des charges d'amortissement : couvre les surcoûts d'amortissement d'un investissement. |
    | **Compte 1150120** | RAN ESMS sous gestion contrôlée (créditeur) (plan T21). Report à nouveau excédentaire d'un ESSMS financé par une autorité de tarification (« gestion contrôlée ») : excédent pas encore affecté. |
    | **Compte 1159020** | RAN ESMS sous gestion contrôlée (débiteur) (plan T21). Report à nouveau déficitaire d'un ESSMS sous gestion contrôlée : déficit en attente de reprise. |
    | **Compte 1159220** | Dépenses pour congés payés (plan T21). Congés payés acquis non financés lors du passage à la provision (écriture de transition). À voir avec l'expert-comptable. |
    | **Compte 1159230** | Autres droits acquis par les salariés non provisionnés (plan T21). Autres droits des salariés (ex. : indemnités de départ) non provisionnés, constatés en report à nouveau. |
    | **Compte 1195000** | RAN des activités ESSMS hors gestion ctlée (débiteur) (plan T21). Report à nouveau déficitaire d'activités hors gestion contrôlée (non tarifées). |
    | **Compte 1202000** | Excédent de l'exercice ESMS sous gestion non contrôlée (plan T21). Excédent de l'exercice d'une activité non tarifée (ex. : vie associative). |
    | **Compte 1205000** | Excédent de l'exercice ESMS sous gestion contrôlée (plan T21). Excédent de l'exercice d'un ESSMS tarifé (SESSAD, SAVS), en attente de décision d'affectation. |
    | **Compte 1292000** | Déficit de l'exercice ESMS sous gestion non contrôlée (plan T21). Déficit de l'exercice d'une activité non tarifée. |
    | **Compte 1295000** | Déficit de l'exercice ESMS sous gestion contrôlée (plan T21). Déficit de l'exercice d'un ESSMS tarifé. |
    | **Compte 1841100** | SIA - Compte liaison exploit° courante BFR (plan T21). Liaison avec la structure « SIA » de la Fédération (code interne : à faire préciser). |
    | **Compte 1844050** | Compte de liaison des établissements (plan T21). Liaison des établissements (compte générique). |
    | **Compte 1848000** | 91 - Compte liaison exploit° courante BFR (plan T21). Liaison avec la structure « 91 » (Essonne ; à faire confirmer). |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 1940000** | Fonds dédiés sur subventions d'exploitation (plan T21). Subvention d'exploitation affectée à un projet et non dépensée au 31/12 (ex. : fondation pour le projet Pairs). |
    | **Compte 1950000** | Fonds dédiés sur contribution financières d'autres organismes (plan T21). Contributions financières d'autres organismes (ex. : fondation d'entreprise) non utilisées. |
    | **Compte 1960000** | Fonds dédiés sur ressources liées à la générosité du public (plan T21). Dons du public affectés à un projet et non utilisés. |
    | **Compte 2710000** | Titres immobilisés (droit de propriété) (plan T21). Titres détenus durablement (le document T21 y range les parts sociales du Crédit Mutuel ; le plan, lui, a aussi 5040000 : à clarifier). |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4310000** | Sécurité sociale (plan T21). URSSAF : cotisations à payer. Crédité par la paie, débité au paiement. |
    | **Compte 4372000** | Mutuelles (plan T21). Cotisations mutuelle à payer. |
    | **Compte 4373100** | Caisse de retraite (plan T21). Cotisations retraite complémentaire à payer. |
    | **Compte 4373200** | Caisse de prévoyance (plan T21). Cotisations prévoyance à payer. |
    | **Compte 4421000** | Prélèvements à la source (Impôt sur le revenu) (plan T21). Prélèvement à la source de l'impôt sur le revenu retenu sur les salaires, à reverser. |
    | **Compte 4471100** | Taxe sur les salaires (plan T21). Taxe sur les salaires à payer (les associations non soumises à la TVA la paient). |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4730000** | Comptes d’attente (plan T21). Second compte d'attente (même libellé que 4710000 : à clarifier). Même règle : soldé au 31/12. |
    | **Compte 5040000** | PSB CME T21 France (parts sociales) (plan T21). Parts sociales du Crédit Mutuel détenues par T21 France (« PSB CME »). Le document range les parts sociales en 27 : à clarifier. |
    | **Compte 5081100** | Compte à terme du siège (dossier M18, fictif). Placement du siège, sous-compte du 5081XXX du plan T21 ; journal PLSIE. |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 5188000** | Intérêts courus à recevoir (plan T21). Intérêts des placements acquis au 31/12 mais versés plus tard. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6223222** | Honoraires Psycho-motriciens (plan T21). Honoraires de psychomotriciens. |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6311000** | Taxe sur les salaires (plan T21). Taxe sur les salaires (calculée par la paie). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 (plan T21). Remboursements de la prévoyance pour les arrêts longs : au crédit, en banque. Ancien compte 6492000. |
    | **Compte 6479000** | Remboursement aur autres charges sociales (plan T21). Remboursements d'autres charges sociales (le plan écrit « aur » pour « aux »). |
    | **Compte 6611000** | Intêrets des emprunts (plan T21). Intérêts des emprunts (exemple du document T21 : prélevés par la banque). |
    | **Compte 6892200** | Report en fonds dédiés à l'exploitation (plan T21). Mise en fonds dédiés de la part non dépensée d'une subvention d'exploitation affectée. |
    | **Compte 7068300** | Prestations de services exterieures (plan T21). Autres prestations de services. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7312170** | Dotation du SAVS (dossier M18, numéro fictif). Le plan T21 ne prévoit que 7312130 (services pour enfants). Pour le SAVS, une autre subdivision 7312xxx est nécessaire : à vérifier dans le plan de l'association. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7541100** | Dons T21 France (plan T21). Dons à T21 France. |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
    | **Compte 7557000** | Siège social interassociatif (plan T21). Frais de siège interassociatif reçus. |
    | **Compte 7584100** | Remboursements sur frais de formation ancien compte 6498000 (plan T21). Remboursement de frais de formation (OPCO). Ancien compte 6498000. |
    | **Compte 7640000** | Revenus des valeurs mobilières de placement (plan T21). Intérêts des placements (comptes à terme, livrets). |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **FOMARTIN** | Compte fournisseur Garage Martin (document T21). Exemple du document T21 : achat d'un véhicule, FOMARTIN au crédit, 2182000 au débit. |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIMOREAUPSY** | Compte libéral : psychomotricien (dossier M18). Séances de psychomotricité du SESSAD (6223222). |
    | **autorité de tarification** | Le financeur qui fixe le budget d'un ESSMS. L'ARS (pour le SESSAD) ou le Conseil départemental (pour le SAVS). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **Extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **Fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **habitat inclusif** | Logement partagé en milieu ordinaire. Des personnes handicapées vivent ensemble chez elles, avec un projet de vie partagé animé par l'association. |
    | **produits à recevoir** | Recette acquise mais pas encore reçue. Ex. : solde d'une subvention AGEFIPH dû au 31/12, versé en mars. |
    | **report à nouveau** | Résultat gardé en attente. Excédent (110) ou déficit (119) reporté sur un budget suivant. |
    | **réserve de compensation** | Excédent mis de côté pour un futur déficit. Compte 10686 : si le service est en déficit plus tard, on puise dans cette réserve. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-12](../exercices/E18-12_lire-et-critiquer-les-documents-t21.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

!!! abstract "En clair"
    Une procédure interne est un **outil**, pas un texte sacré. On l'applique, et on la **vérifie** avec trois tests simples : (1) **le sens** : une dette est au crédit, une créance au débit, une charge au débit, un produit au crédit ; (2) **la cohérence** : le document et le plan comptable disent-ils la même chose ? (3) **la date** : le document est-il à jour de la réglementation qu'il cite ? Quand on trouve une erreur, on **ne corrige pas seul** : on applique la bonne règle, on le **documente** et on le **signale** avec tact.

### Partie A — « Dans quel compte et à quel sens ? »

| N° | Opération | Compte(s) du plan T21 et sens | Journal | Appui dans les documents |
|---|---|---|---|---|
| 1 | IJSS reçues de la CPAM | **6419000 au crédit** (le logiciel débite 5122000) | BQSES | Doc. 2, journal de banque ; doc. 1, classe 6 (exception) |
| 2 | Facture de psychomotricien de décembre non arrivée | **6223222 au débit**, **4081000 au crédit** | OD | Doc. 1, classe 40 — **en corrigeant le sens** (voir B) |
| 3 | Avoir EDF de 54,00 € | **FOEDF (4010000) au débit**, **6061200 au crédit** | AC | Doc. 2, « NB : en cas d'avoir… l'écriture est à l'envers » |
| 4 | Affectation de 20 000,00 € d'excédent en réserve de compensation des déficits | **1068562 au crédit** ; au débit, le compte où se trouve l'excédent à affecter (**1205000** si c'est le résultat de l'exercice précédent, ou **1150120** s'il avait été mis en report à nouveau) | OD | Doc. 1, classe 10 : « les affectations en réserves viennent créditer les comptes » |
| 5 | Intérêts acquis au 31/12 sur le compte à terme, versés en N+1 | **5188000 au débit**, **7640000 au crédit** | OD | Doc. 1, classe 51 : « en compte 5188, les intérêts courus non échus des placements » |
| 6 | Subvention affectée non utilisée au 31/12 | **6892200 au débit**, **1940000** au crédit (1950000 si le financeur est un organisme privé, 1960000 pour des dons) | OD | Doc. 1, classes 19 et 68 |
| 7 | Placement de 50 000,00 € sur le compte à terme | **PLSIE** : 5081100 au débit / 5800000 au crédit ; **BQSIE** : 5800000 au débit / 5121000 au crédit | PLSIE et BQSIE | Doc. 1, classe 58 : tout mouvement entre comptes de classe 5 transite par le 58 |
| 8 | Extourne au 01/01/2027 d'une FNP d'électricité | **4081000 au débit**, **6061200 au crédit** | OD | Doc. 1, classe 6 : « lors des extournes… leur saisie est au crédit » |

**Le placement, à l'aller et au retour** (et la preuve que l'extrait 2 se trompe) :

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 02/03/2026 | SIE | BQSIE | 5800000 | Virements internes | Versement sur CAT – virement du 02/03 | 50 000,00 | |
| 02/03/2026 | SIE | BQSIE | 5121000 | Crédit Mutuel – Siège | (ligne automatique) | | 50 000,00 |
| 02/03/2026 | SIE | PLSIE | 5081100 | CAT détaillés | Souscription CAT 12 mois | 50 000,00 | |
| 02/03/2026 | SIE | PLSIE | 5800000 | Virements internes | Souscription CAT 12 mois | | 50 000,00 |
| 02/03/2027 | SIE | PLSIE | 5800000 | Virements internes | Libération CAT à l'échéance | 50 000,00 | |
| 02/03/2027 | SIE | PLSIE | 5081100 | CAT détaillés | Libération CAT à l'échéance | | 50 000,00 |
| 02/03/2027 | SIE | BQSIE | 5121000 | Crédit Mutuel – Siège | (ligne automatique) | 50 000,00 | |
| 02/03/2027 | SIE | BQSIE | 5800000 | Virements internes | Retour des fonds du CAT | | 50 000,00 |
| | | | | | **Total** | **200 000,00** | **200 000,00** |

À la libération, le compte de placement 5081100 est **crédité** : il sort 50 000,00 € du placement. S'il était « débité » comme le dit le document, le placement doublerait dans les comptes alors que l'argent est revenu en banque. *Les intérêts reçus à l'échéance iraient en 7640000 au crédit (en soldant d'abord le 5188000 s'il y a eu des intérêts courus au 31/12/2026).*

### Partie B — Question 9 : les incohérences, erreurs et coquilles

**a) Erreurs qui peuvent fausser une écriture** (à signaler en priorité)

| N° | Où | Ce qui est écrit | Ce qu'il faut comprendre | Risque |
|---|---|---|---|---|
| 1 | Doc. 1, classe 40 | 4081000 « débité en N, crédité en N+1 » | **Crédité en N** (dette, il remplace le FO ou le LI qui sont crédités), **débité en N+1** par l'extourne | Une FNP passée « au débit du 4081000 » ferait une **créance** au lieu d'une dette, et une charge… créditée |
| 2 | Doc. 1, classe 50 | « souscription : débité ; libération : débité » | Souscription : **débité** ; libération : **crédité** | Placement jamais soldé, trésorerie surévaluée |
| 3 | Doc. 1, classe 43 | Charges sociales « à reverser à **l'État** » | À reverser aux **organismes sociaux** : URSSAF (4310000), mutuelles (4372000), caisses de retraite (4373100) et de prévoyance (4373200). L'**État**, c'est la classe **44** (prélèvement à la source 4421000, taxe sur les salaires 4471100) | Confusion entre classe 43 et classe 44 dans les lettrages et les déclarations |
| 4 | Doc. 1, classe 27 / plan | Parts sociales du Crédit Mutuel en **classe 27** | Le plan les met en **5040000** « PSB CME T21 France (parts sociales) » (classe 5), alors qu'il contient aussi un 2710000 « Titres immobilisés » | Même opération, deux comptes possibles selon le document lu. Les parts sociales d'une banque mutualiste, détenues durablement (souvent une condition pour avoir un compte ou un prêt), relèvent en général des **immobilisations financières** : à trancher avec l'expert-comptable |

**b) Incohérences entre documents ou avec la réglementation**

| N° | Constat | Commentaire |
|---|---|---|
| 5 | Plan « MAJ le 13/10/2025 – **Applicable au 1/01/2025** », alors que le document 1 renvoie à l'**arrêté du 19/12/2025 applicable au 01/01/2026** | Le plan est **antérieur** à l'arrêté qu'il est censé appliquer. Demander s'il a été revu (comptes créés, supprimés ou renumérotés) avant la clôture 2026 |
| 6 | Réserves : le document décrit **3 types** (investissement, compensation des déficits, trésorerie), le plan contient **4 comptes** | Le **1068572** « Res compens amort » (compensation des charges d'amortissement) n'est pas expliqué |
| 7 | **4710000** et **4730000** ont le **même intitulé** « Comptes d'attente » | Lequel utiliser, et pour quoi ? Sans règle, les sommes en attente se dispersent. Proposer par exemple 4710000 pour les **recettes** à identifier et 4730000 pour les **dépenses** (à décider par la Fédération) |
| 8 | **4671XXX** et **4676000** ont le **même intitulé** « Comptes débiteurs et produits à recevoir » | Même problème ; le 4671XXX semble prévu pour des comptes détaillés (« XXX ») : à préciser |
| 9 | **7556000 / 7557000** sont placés **entre 7488000 et 7541100** | L'ordre numérique n'est pas respecté (755 après 754) : on les cherche au mauvais endroit et on risque de croire qu'ils n'existent pas |
| 10 | Le plan ne prévoit que **7312130** (ESSMS du **2°** du I de l'article L. 312-1 du CASF : services pour enfants et jeunes handicapés) | Un **SAVS** relève d'une autre catégorie (en principe le **7°**, services pour adultes handicapés : à vérifier) ; il faut une autre subdivision 7312xxx (la fiche utilise **7312170**, numéro fictif) |
| 11 | Le document 2 utilise des numéros **courts** (60612, 2182, 6251, 60624, 60621, 627, 6611, 64191) et l'exemple « FOMARTIN », alors que le plan est à **7 chiffres** | Sans gravité si l'on sait que 60612 = 6061200, mais déroutant pour une débutante ; le compte « 627 » correspond à **6270000** |
| 12 | Doc. 1, classe 12 : « l'excédent ou le déficit de l'**exercice précédent** » | Imprécis : la classe 12 reçoit le résultat de l'exercice **qui vient d'être clos** ; il n'est « précédent » que dans le bilan d'ouverture, en attendant son affectation |

**c) Simples coquilles** (à corriger à la prochaine mise à jour, sans urgence)

- 1032000 « Fonds propres **sattutaires** » → statutaires.
- 6479000 « Remboursement **aur** autres charges sociales » → sur.
- 6611000 « **Intêrets** des emprunts » → Intérêts.
- 1950000 « Fonds dédiés sur **contribution** financières » → contributions.
- 7068300 « Prestations de services **exterieures** » → extérieures.
- 1068562 / 1068572 « … relevant **art** L.312-1 » : il manque « du I de l'».

### Question 10 — Pourquoi aucun compte 445 ?

Les comptes 445 servent à suivre la **TVA** (collectée sur les ventes, déductible sur les achats). Le plan T21 n'en contient aucun parce que les activités des structures (accompagnement médico-social financé par l'ARS et le Département, vie associative) ne sont **pas soumises à la TVA** : le CGI prévoit des **exonérations** pour ce type d'organismes et d'activités (à vérifier activité par activité, en particulier pour les ventes de la Fédération : formations, documentation, goodies).

**Conséquences pour la saisie** : la TVA payée aux fournisseurs **n'est pas récupérable**, elle fait partie du coût. On saisit les factures **TTC** en charge (ou en immobilisation, TTC aussi) ; une TVA séparée sur un compte 445 est une **erreur** (voir E18-10).

**L'indice dans le plan** : les comptes **6311000** « Taxe sur les salaires » et **4471100**. La taxe sur les salaires est due, en principe, par les employeurs qui ne sont **pas** soumis à la TVA (ou qui ne le sont que sur une petite partie de leurs recettes). Sa présence confirme que les structures sont **hors TVA**.

### Question 11 — Pourquoi 6419000 fonctionne au crédit

Quand un salarié est en arrêt maladie, l'association continue souvent de le payer (**maintien de salaire**) et reçoit les **IJSS** de la CPAM à sa place (**subrogation**). La charge de salaire est enregistrée en totalité en 641x ; les IJSS viennent **réduire** ce coût. Plutôt qu'un compte de produit, le plan utilise un compte de **charge** qui fonctionne « à l'envers », au **crédit** : 6419000 « Remboursements sur rémunération du personnel – IJSS ». Résultat : les **charges de personnel** apparaissent **nettes** des remboursements, ce qui est le coût réel pour le service et ce que regarde le financeur. Même logique pour la prévoyance (**6419100**).

« **Ancien compte 6491000** » : le plan signale que ces remboursements étaient auparavant enregistrés dans un autre compte (6491000, et 6492000 pour la prévoyance ; de même 7584100 remplace 6498000). C'est utile pour **comparer avec N-1** et pour reprendre d'anciens tableaux. Cette logique rejoint aussi le PCG 2025, qui a **supprimé les comptes de transfert de charges** (791) : on n'« transfère » plus, on enregistre le remboursement là où il a un sens.

### Question 12 — 1150120, 1159020 et 1159220

- **1150120** « RAN ESMS sous gestion contrôlée (**créditeur**) » : les **excédents** passés d'un service tarifé, pas encore affectés (ou affectés en report à nouveau).
- **1159020** « RAN ESMS sous gestion contrôlée (**débiteur**) » : les **déficits** passés, pas encore couverts.

**Pourquoi deux comptes ?** Parce que l'**autorité de tarification** suit séparément ce qui est « en plus » et ce qui est « en moins ». Le document T21 le dit : l'affectation est **décidée par le financeur** (compte administratif) ou **proposée** par le gestionnaire (CPOM). Un excédent peut être repris en diminution des tarifs futurs ou mis en réserve ; un déficit peut être couvert par une reprise de réserve ou repris sur les exercices suivants. Si l'on compensait tout dans un seul compte, on ne pourrait plus retrouver **chaque décision d'affectation** ni justifier les montants dans l'ERRD ou le compte administratif.

**1159220** « Dépenses pour congés payés » (et 1159230 « Autres droits acquis par les salariés non provisionnés ») : un report à nouveau **débiteur** lié aux congés payés. Dans les ESSMS, il sert en principe de contrepartie à la **première** constatation des dettes de congés payés quand elles n'avaient pas été financées par les tarifs, pour ne pas faire apparaître un déficit d'un seul coup. *Vérifiez dans l'historique de l'association (dossiers de clôture, décisions des financeurs) l'origine du solde avant d'y toucher.*

### Question 13 — Les réserves 10685xx et la « norme » des 5 %

- Le document décrit **3** types de réserves ; le plan en contient **4** : investissement (**1068522**), trésorerie (**1068552**), compensation des déficits (**1068562**) et compensation des charges d'amortissement (**1068572**), cette dernière n'étant pas expliquée.
- **Application** : 5 % × 1 296 000,00 = **64 800,00 €**. Le solde du 1068562 du SESSAD est de **41 300,00 €** : il manque **23 500,00 €** pour atteindre le niveau indiqué.

| Élément | Montant |
|---|---|
| Dotation 2026 du SESSAD | 1 296 000,00 € |
| Niveau indiqué par le document (5 %) | 64 800,00 € |
| Réserve de compensation des déficits (1068562) | 41 300,00 € |
| **Écart** | **− 23 500,00 €** |

**Précautions de langage** : le document parle de « norme » sans citer de texte. Dites « selon le **repère** indiqué par la Fédération » et non « la loi impose ». Vérifiez la base réglementaire (règles d'affectation des résultats du CASF, CPOM, position de l'ARS) avec l'expert-comptable. Enfin, l'agent comptable **ne décide pas** l'affectation : il **prépare** une proposition chiffrée (par exemple, affecter une partie d'un futur excédent à cette réserve) pour la direction, le conseil d'administration et le financeur.

### Question 14 — Gestion contrôlée et gestion non contrôlée

Explication simple, à confirmer avec l'expert-comptable :

- **Sous gestion contrôlée** : activités dont les **ressources sont fixées par une autorité de tarification** (ARS, Département) et dont le **résultat est soumis à son contrôle** : elle examine les comptes, peut rejeter des charges, décide (ou valide) l'affectation des excédents et déficits. Le résultat n’« appartient » donc pas librement à l'association.
- **Sous gestion non contrôlée** : activités financées **autrement** (cotisations, dons, ventes, subventions sur projet) : le résultat reste à la disposition de l'association, dans le respect des conventions de chaque financeur.

Dans le plan, la distinction se voit dans les comptes de résultat (**1205000 / 1295000** gestion contrôlée, **1202000 / 1292000** non contrôlée) et de report à nouveau (**1150120 / 1159020** contrôlée, **1195000** hors gestion contrôlée).

| Structure | Classement proposé | Prudence |
|---|---|---|
| SES (SESSAD, dotation ARS, CPOM) | **Contrôlée** | Clair |
| SAV (SAVS, dotation du Département) | **Contrôlée** | Clair |
| EMP (Emploi accompagné, ARS + AGEFIPH + FIPHFP par convention) | **À vérifier** | Dépend du statut du dispositif et des conventions : à valider avec l'expert-comptable et l'ARS |
| ASS (vie associative, dons, habitat inclusif, projets) | **Non contrôlée** | L'aide à la vie partagée de l'habitat inclusif passe par une convention, pas par une tarification : à confirmer |
| SIE (siège) | Cas particulier | Ses coûts sont couverts par les **frais de siège** autorisés, eux-mêmes pris en charge par les services contrôlés : le traitement de son résultat est à voir avec l'autorité qui a autorisé les frais de siège |

### Question 15 — 7312130 suffit-il ?

Non. 7312130 vise les ESSMS du **2°** du I de l'article L. 312-1 du CASF (le **SESSAD**). Le **SAVS** relève d'une autre catégorie (en principe le **7°**, à vérifier) : il faut une subdivision **7312xxx** propre, à créer **par la Fédération** dans le plan commun (et non « à la volée » dans le logiciel), pour que les dotations de chaque catégorie restent identifiables dans les comptes de l'association et dans les états de synthèse. En attendant, les exercices du module utilisent **7312170** (fictif). Pour l'Emploi accompagné, le compte (731 ou 74) dépend de la nature du financement : à vérifier.

### Question 16 — Ce que révèlent les comptes 1841100 à 1848000

Ces intitulés (« SIA », « CFF », « AF », « SESSAD DK », « SAVS DK », « SESSAD Lille », « 56 », « 28 », « 93 », « 91 ») montrent que le plan est un **plan commun au réseau**, construit à partir des structures de **plusieurs entités** (vraisemblablement des sites et des associations départementales désignées par leur ville ou leur numéro de département). Conséquences :

1. Les comptes de liaison **réels** de Cap Horizons 21 sont à lire dans **son** plan, pas dans ce document : la fiche du module utilise 1849100 à 1849400 comme **hypothèse**.
2. Ne jamais utiliser un compte nommé « SESSAD DK » pour le SAVS de Cap Horizons 21 sans l'avoir **renommé** : le CAC et l'expert-comptable liraient un intitulé faux.
3. Le compte **1844050** « Compte de liaison des établissements » mérite aussi une question : à quoi sert-il par rapport aux autres ?

## 2. Calculs (détaillés, chaque montant justifié)

| Calcul | Détail | Résultat |
|---|---|---|
| Réserve de compensation des déficits attendue | 1 296 000,00 × 5 % | 64 800,00 € |
| Écart avec le solde du 1068562 | 41 300,00 − 64 800,00 | − 23 500,00 € |
| IJSS (A1) | montant reçu | 642,18 € au crédit du 6419000 |
| Extourne FNP électricité (A8) | inverse exact de l'écriture du 31/12 | 1 860,00 € |

## 3. Écritures comptables

L'écriture du placement est présentée au § 1 (partie A). Voici la FNP de la question A2 et son extourne, au **bon** sens, avec un montant d'exemple (16 séances × 38,00 € = 608,00 €) :

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/12/2026 | SES | OD | 6223222 | Honoraires Psycho-motriciens | FNP LIMOREAUPSY – 16 séances – 12/2026 | 608,00 | |
| 31/12/2026 | SES | OD | 4081000 | Fournisseurs factures non parvenues | FNP LIMOREAUPSY – 16 séances – 12/2026 | | 608,00 |
| 01/01/2027 | SES | OD | 4081000 | Fournisseurs factures non parvenues | Extourne FNP LIMOREAUPSY – 12/2026 | 608,00 | |
| 01/01/2027 | SES | OD | 6223222 | Honoraires Psycho-motriciens | Extourne FNP LIMOREAUPSY – 12/2026 | | 608,00 |
| | | | | | **Total** | **1 216,00** | **1 216,00** |

Et l'avoir EDF (A3), saisi au siège :

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 15/11/2026 | SIE | AC | 4010000 | Fournisseurs FO (tiers FOEDF) | FOEDF – avoir régularisation – AV-2026-0912 | 54,00 | |
| 15/11/2026 | SIE | AC | 6061200 | Energie, électricité | FOEDF – avoir régularisation – AV-2026-0912 | | 54,00 |
| | | | | | **Total** | **54,00** | **54,00** |

*Si la facture d'origine avait été répartie en IS, l'avoir doit l'être aussi, avec la même clé (sinon le siège garde tout l'avoir et les structures toute la charge).*

## 4. Points d'attention / pièges

- **Recopier une procédure sans la vérifier** : l'erreur sur le 4081000 se transmet de comptable en comptable. Le test du sens (dette = crédit) suffit à la repérer.
- **Corriger seule le document de la Fédération** : non. On applique la bonne règle, on **documente** (note dans le dossier de clôture) et on **propose** une correction par la voie hiérarchique.
- **Créer des comptes « qui manquent »** (7312xxx, 445…) directement dans le logiciel : non. La création passe par la Fédération (plan commun) et l'expert-comptable.
- **Affirmer une règle sans source** (« la loi impose 5 % ») : dites « le document de la Fédération indique » et faites vérifier.
- **Confondre gestion contrôlée et « contrôle de gestion »** : il ne s'agit pas d'un outil de pilotage, mais du **régime** du résultat (qui décide de son affectation).
- **Ton du mail** : un mail qui « liste les fautes » braque. Un mail qui explique **l'impact pratique** et **propose** une solution est lu et suivi.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

### Question 17 — Le mail à Mme Berthier

> **Objet : Documents comptables de la Fédération – quelques points à clarifier**
>
> Bonjour Madame Berthier,
>
> Merci pour les trois documents de la Fédération, très utiles pour harmoniser nos pratiques. En les appliquant, j'ai noté quelques points ; je vous les présente par ordre d'importance pour la saisie.
>
> **1. Deux phrases à corriger, car elles conduiraient à une écriture fausse** (je saisis déjà selon la règle habituelle, Mme Ferrand pourra le confirmer) :
> - le compte 4081000 (factures non parvenues) est **crédité** en fin d'exercice et débité l'année suivante, et non l'inverse ;
> - le compte de placement est **crédité** lors de la libération des fonds (le document indique « débité » deux fois).
>
> **2. Trois points à faire préciser par la Fédération** : où classer les parts sociales du Crédit Mutuel (classe 27 dans le document, compte 5040000 dans le plan) ; la différence entre les comptes 4710000 et 4730000, qui portent le même intitulé ; et l'ajout d'un compte de dotation pour le SAVS, car le plan ne prévoit que celui des services pour enfants (7312130).
>
> **3. Une question de calendrier** : le plan est daté du 13/10/2025, avant l'arrêté du 19/12/2025 applicable en 2026. Savez-vous si une mise à jour est prévue avant notre clôture 2026 ?
>
> **4. Quelques coquilles** sans incidence (liste jointe), à transmettre si la Fédération met à jour ses documents.
>
> Si vous le souhaitez, je peux préparer une note courte et neutre que vous pourriez transmettre à la Fédération. Je reste bien sûr disponible pour en parler de vive voix.
>
> Bien cordialement,
> [Prénom Nom], agent comptable

**Pourquoi ce mail fonctionne** : il remercie, il classe (urgent / à préciser / sans urgence), il dit ce que vous faites **déjà** (vous ne bloquez pas le travail), il propose une **solution** (une note) et laisse la directrice décider de la suite.

**Documentation** : gardez dans le dossier permanent une « **note de lecture des procédures T21** » (date, point, règle appliquée, validation de l'expert-comptable). Le CAC y verra que les écarts entre la procédure et la pratique sont **voulus et justifiés**.

## 6. Références

- Documents internes Trisomie 21 France : « La comptabilité chez Trisomie 21 France » et « Les journaux comptables chez Trisomie 21 France » (30/04/2026) ; « Plan comptable général T21 France » (MAJ 13/10/2025).
- Arrêté du 19 décembre 2025 relatif au plan comptable applicable aux ESSMS privés relevant du I de l'article L. 312-1 du CASF (applicable au 01/01/2026) : à lire dans sa version publiée pour vérifier les comptes du plan T21.
- Code de l'action sociale et des familles : article L. 312-1, I (catégories d'ESSMS) ; règles réglementaires d'affectation des résultats des ESSMS (à consulter avec l'expert-comptable).
- Code général des impôts : exonérations de TVA des organismes sans but lucratif et du secteur médico-social ; taxe sur les salaires (textes à consulter selon l'activité).
- Plan comptable général (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06) : suppression des comptes de transfert de charges.
