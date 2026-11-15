# M18 — Corrigé de la banque de QCM (saisie comptable selon les règles de Trisomie 21 France)

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CB** | Carte bancaire. Paiement par carte. Les encaissements CB arrivent en banque nets de commission. |
    | **CCA** | Charges constatées d'avance — ou compte courant d'associé. Deux sens selon le contexte : (1) clôture : charge payée en N mais qui concerne N+1 (compte 486) ; (2) financement : argent prêté par un associé à sa société (compte 455). |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
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
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 1068522** | Res invest - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve d'investissement : excédent d'un ESSMS mis de côté, sur décision du financeur, pour financer un investissement. |
    | **Compte 1068552** | Res tréso - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve de trésorerie : excédent affecté pour renforcer la trésorerie du service. |
    | **Compte 1068562** | Res compens déficits- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des déficits : couvre un futur déficit. Le document T21 indique qu'elle doit atteindre au moins 5 % de la dotation annuelle. |
    | **Compte 1068572** | Res compens amort- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des charges d'amortissement : couvre les surcoûts d'amortissement d'un investissement. |
    | **Compte 1648000** | Intérêts courus sur emprunts auprès des Ets de crédit (plan T21). Intérêts courus non échus (ICNE) : intérêts de l'exercice qui seront payés l'an prochain. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 2183000** | Matériel de bureau et matériel informatique (plan T21). Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4110000** | Clients (comptes de tiers CL…) (plan T21). Centralisation des clients. On saisit dans les comptes CL… |
    | **Compte 4210000** | Personnel - Rémunérations dues (plan T21). Salaires nets à payer. Crédité par la paie, débité au virement des salaires. |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4250000** | Personnel - Avances et acomptes (plan T21). Avance ou acompte versé à un salarié, récupéré sur la paie. |
    | **Compte 4270000** | Personnel - Oppositions (plan T21). Sommes retenues sur salaire pour un tiers (saisie sur salaire, avis à tiers détenteur). |
    | **Compte 4282000** | Dettes provisionnées pour congés à payer (plan T21). Congés payés acquis et non pris à la clôture (dette envers les salariés). |
    | **Compte 4382000** | Charges sociales sur congés à payer (plan T21). Charges sociales sur les congés payés provisionnés. |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4860000** | Charges constatées d’avance (plan T21). Charge constatée d'avance : facturée en N mais concernant N+1 (ex. : assurance avril N – mars N+1). |
    | **Compte 4878000** | Produits constatés d’avance - Subventions (plan T21). Subvention reçue en N pour une période de N+1 (ex. : année scolaire). |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6062500** | Fournitures scolaires, éducatives et de loisirs (plan T21). Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. |
    | **Compte 6062800** | Autres fournitures non stockées (plan T21). Autres petites fournitures. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 (plan T21). Remboursements de la prévoyance pour les arrêts longs : au crédit, en banque. Ancien compte 6492000. |
    | **Compte 6556000** | Frais de siège social du gestionnaire (plan T21). Frais de siège facturés par le siège à la structure (taux autorisé par le financeur). |
    | **Compte 6618000** | Autres charges d'intérêt - intérêts courus (plan T21). Intérêts courus à la clôture (ICNE). |
    | **Compte 6892200** | Report en fonds dédiés à l'exploitation (plan T21). Mise en fonds dédiés de la part non dépensée d'une subvention d'exploitation affectée. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
    | **Compte 7584100** | Remboursements sur frais de formation ancien compte 6498000 (plan T21). Remboursement de frais de formation (OPCO). Ancien compte 6498000. |
    | **Compte 7892200** | Fonds dédiés - Exploitation (plan T21). Utilisation, l'année suivante, des fonds dédiés d'exploitation (quand on dépense enfin la subvention). |
    | **FOEDF** | Compte fournisseur EDF. FO = fournisseur. Compte de tiers du fournisseur d'électricité (exemple du document T21), regroupé dans 4010000. |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **produit à recevoir** | Recette acquise mais pas encore reçue. Ex. : solde d'une subvention AGEFIPH dû au 31/12, versé en mars. |
<!-- /glossaire-page -->

*Fichier de correction : à n'ouvrir qu'après avoir répondu aux questions de `QCM_questions.md`. Sources : documents internes Trisomie 21 France (30/04/2026), plan comptable T21 France (MAJ 13/10/2025) et [fiche du dossier](fiche_dossier_5_structures.md) (hypothèses pédagogiques : structures, comptes de liaison et de banque, clés, montants).*

## Grille rapide des réponses

- **A** : Q001 C · Q002 B · Q003 C · Q004 D · Q005 A · Q006 B · Q007 D · Q008 B
- **B** : Q009 C · Q010 A · Q011 D · Q012 B · Q013 C · Q014 A · Q015 D · Q016 B
- **C** : Q017 A · Q018 C · Q019 D · Q020 B · Q021 A · Q022 C · Q023 D
- **D** : Q024 B · Q025 A · Q026 C · Q027 D · Q028 B · Q029 A · Q030 C · Q031 D
- **E** : Q032 A · Q033 C · Q034 D · Q035 B · Q036 A · Q037 C · Q038 D · Q039 B · Q040 A · Q041 C
- **F** : Q042 D · Q043 A · Q044 B · Q045 C · Q046 D · Q047 A · Q048 B · Q049 C · Q050 D

---

## A. Les documents et le plan comptable T21

**Q001 — Réponse C** (7 chiffres)  
Tous les comptes du plan T21 ont 7 chiffres (6061200, 4081000, 7312130…). Le document « Les journaux comptables » cite parfois des numéros courts (60612, 6251) : ce sont les mêmes comptes, abrégés.

**Q002 — Réponse B** (plan des ESSMS relevant du I de l'article L. 312-1 du CASF)  
C'est ce qu'indique l'introduction du document « La comptabilité chez Trisomie 21 France », qui renvoie à l'arrêté du 19 décembre 2025 applicable au 1er janvier 2026. Ce plan ajoute notamment les comptes de liaison (18) et de fonds dédiés ou reportés (19).

**Q003 — Réponse C** (pas de TVA : factures saisies TTC)  
Les activités des structures ne sont pas soumises à la TVA ; la TVA payée fait partie du coût. Créer un compte 4456600 (réponse A) est une erreur classique, repérée en révision (E18-10).

**Q004 — Réponse D** (achats non stockés 606xxxx)  
Le document T21 le dit pour la classe 60 : « il n'y a pas de notion de stocks, les comptes utilisés sont les 606 ». Pas de 601/602, pas de variation de stocks.

**Q005 — Réponse A** (demander la mise à jour et vérifier avant la clôture)  
Le plan est antérieur à l'arrêté qu'il applique. Un senior ne crée pas de comptes de sa propre initiative (réponse C) : il pose la question à la Fédération et à l'expert-comptable, puis vérifie les comptes concernés avant la clôture 2026.

**Q006 — Réponse B** (excédents d'un côté, déficits de l'autre, gestion contrôlée)  
L'autorité de tarification suit séparément les excédents et les déficits antérieurs, car leur affectation (reprise, réserve, couverture) fait l'objet de décisions distinctes. On ne les compense pas dans un seul compte.

**Q007 — Réponse D** (4)  
1068522 investissement, 1068552 trésorerie, 1068562 compensation des déficits et 1068572 compensation des charges d'amortissement. Le quatrième n'est pas décrit dans le document : c'est une des incohérences à signaler (E18-12).

**Q008 — Réponse B** (45 000,00 €)  
900 000,00 × 5 % = 45 000,00 €. Prudence de langage : le document parle de « norme » sans citer de texte ; on présente ce chiffre comme le **repère** de la Fédération, à vérifier avec l'expert-comptable.

---

## B. Les journaux

**Q009 — Réponse C** (Fédération uniquement, EIG Gestion commerciale)  
Le journal des ventes est un journal automatique ; aucune écriture manuelle. Les dotations passent par la banque (731), les notes de frais par les achats.

**Q010 — Réponse A** (aucune écriture manuelle, déversement EIG RH)  
Le journal de paie est automatique. L'agent comptable **contrôle** le déversement (net à payer = virements, ratio de charges, lignes inhabituelles) mais n'y écrit jamais.

**Q011 — Réponse D** (FOEDF au débit ; banque créditée automatiquement)  
Dans un journal à contrepartie automatique, on saisit seulement la ligne de contrepartie. « Débit pour les dépenses » s'applique à cette ligne (FOEDF débité, dette éteinte) ; la banque, elle, est créditée par le logiciel.

**Q012 — Réponse B** (passage par 5800000 dans les deux journaux)  
Le document T21 (classe 58) interdit d'écrire directement banque contre caisse : la sortie et l'entrée passent par 5800000, qui revient à zéro quand les deux moitiés sont saisies.

**Q013 — Réponse C** (journal IM, EIG IMMOS)  
Le journal des immobilisations est automatique : dotations et sorties d'actif viennent d'EIG IMMOS. D'où l'importance de garder les fiches d'immobilisations à jour.

**Q014 — Réponse A** (régénérable tant que N-1 n'est pas clos)  
Les à-nouveaux provisoires reprennent le bilan de clôture provisoire de N-1 ; à la clôture définitive, le journal de reprise des à-nouveaux les écrase. Les comptes de charges et produits (classes 6 et 7) n'y figurent pas.

**Q015 — Réponse D** (journal des achats, tiers SA)  
Le document « Les journaux comptables » range les notes de frais dans le journal des achats : compte SA crédité, charges débitées.

**Q016 — Réponse B** (6419100 au crédit)  
Les remboursements de prévoyance pour les arrêts de longue durée vont en 6419100 (« 64191 » dans le document), au crédit, comme les IJSS en 6419000.

---

## C. Les comptes de tiers FO, LI, SA, CL

**Q017 — Réponse A** (interdit)  
4010000, 4011000, 4248000 et 4110000 sont des comptes de centralisation : le document T21 rend obligatoire la saisie sur le compte de tiers et interdit la saisie directe. Une saisie sans tiers crée des comptes FO faussement débiteurs (E18-10).

**Q018 — Réponse C** (LIMARTINEZ)  
Libéral conventionné = préfixe LI, nom en majuscules, sans espace ni accent. FO est réservé aux fournisseurs, SA aux salariés.

**Q019 — Réponse D** (D LIDUPONT / C 6223221)  
Un avoir s'écrit « à l'envers » de la facture (document « Les journaux comptables », NB sur les avoirs) : le libéral est débité, la charge créditée.

**Q020 — Réponse B** (centralisation des SA)  
4248000 regroupe les comptes SA des salariés pour leurs notes de frais. Les salaires nets sont en 4210000, les acomptes en 4250000, les oppositions en 4270000.

**Q021 — Réponse A** (chercher avant de créer)  
Un fournisseur créé deux fois disperse les factures et les paiements : impossible de lettrer et de repérer un doublon. Les réponses C et D sont interdites ou à éviter.

**Q022 — Réponse C** (payée deux fois ou avoir non lettré)  
Un compte fournisseur est normalement créditeur (dette). Débiteur, il signifie que l'on a plus payé (ou reçu en avoir) que facturé. Autre cause possible à vérifier : une facture saisie sur 4010000 sans tiers.

**Q023 — Réponse D** (débités à la facture, crédités au règlement ; Fédération uniquement)  
Les clients doivent de l'argent : leur compte est débité à la facture. Seule la Fédération facture, via EIG Gestion commerciale.

---

## D. Les 5 structures et les inter-structures

**Q024 — Réponse B** (une association, cinq comptabilités)  
Une seule personne morale, mais cinq structures (SIE, SES, SAV, EMP, ASS), chacune avec sa balance, parce que chaque financeur veut les comptes de son service. L'analytique (réponse D) ne suffit pas : il faut des bilans séparés.

**Q025 — Réponse A** (1840000 Liaison Siège)  
Chaque structure regarde vers l'autre : chez le SESSAD, la liaison s'appelle « Liaison Siège » ; c'est au siège que l'on trouve le 1849100 « Liaison SESSAD » (numéros fictifs de la fiche).

**Q026 — Réponse C** (créditeur de 20 389,20 €)  
Le solde du 184x au siège est l'exact opposé du 1840000 de la structure. Tout écart a une cause précise (IS sans miroir, virement mal imputé…).

**Q027 — Réponse D** (300,00 €)  
Clé m² du SAVS : 25 %. 1 200,00 × 25 % = 300,00 €. (120,00 = EMP 10 % ; 180,00 = SIE 15 % ; 540,00 = SES 45 %.)

**Q028 — Réponse B** (1840000 Liaison Siège)  
Un mouvement de trésorerie entre deux structures passe toujours par les comptes de liaison. Le 5800000 est réservé aux mouvements entre comptes de trésorerie d'une **même** structure.

**Q029 — Réponse A** (6556000 / 1840000 au SAVS ; 1849200 / 7556000 au siège)  
Les frais de siège sont une charge pour le service (6556000 « Frais de siège social du gestionnaire ») et un produit pour le siège (7556000 « Siège social du gestionnaire »), reliés par les comptes de liaison.

**Q030 — Réponse C** (174,00 €)  
Clé ETP de l'Emploi accompagné : 12 %. 1 450,00 × 12 % = 174,00 €. (130,50 = siège 9 % ; 391,50 = SAVS 27 %.)

**Q031 — Réponse D** (solde nul)  
Document T21, classe 18 : « dans les comptes consolidés de l'organisme gestionnaire, les comptes de classe 18 doivent avoir un solde nul ». Ce que l'un doit, l'autre le possède.

---

## E. Cas de saisie

**Q032 — Réponse A** (directement en banque, 6062100)  
Document « Les journaux comptables » : une dépense par carte avec ticket de caisse et ticket CB, mais sans facture, se saisit directement en banque avec le compte de charge (« 60621 » dans le document = 6062100).

**Q033 — Réponse C** (1 089,00 € TTC en 2183000 + fiche EIG IMMOS)  
TVA non récupérable : l'immobilisation est inscrite TTC. 1 089,00 € > 500,00 € : immobilisation. La fiche EIG IMMOS permettra au journal IM de calculer les amortissements.

**Q034 — Réponse D** (reclasser en charge et supprimer la fiche EIG IMMOS)  
350,00 € TTC est sous le seuil de 500,00 € : c'est une charge (par exemple 6062800). Sans suppression de la fiche, EIG IMMOS générerait une dotation à la clôture.

**Q035 — Réponse B** (7312130 au crédit)  
Dotation de l'autorité de tarification = classe 73, au crédit, dans le journal de banque. 7312130 vise les ESSMS du 2° du I de l'article L. 312-1 du CASF, dont le SESSAD.

**Q036 — Réponse A** (écart de 3 720,00 €)  
La banque aurait dû être débitée de 1 860,00 € ; elle a été créditée de 1 860,00 €. Différence : 2 × 1 860,00 = 3 720,00 €, banque comptable trop basse. Un écart égal au double d'une opération signale presque toujours une erreur de sens.

**Q037 — Réponse C** (6251000 et 6062400 au débit, SADURAND au crédit)  
C'est l'exemple même du document « Les journaux comptables » : indemnités kilométriques en « voyages et déplacements », stylos et carnets en « fournitures administratives », salarié crédité du total.

**Q038 — Réponse D** (486,90 € TTC en 6062500)  
Pas de TVA récupérable : la charge est le TTC. Sous le seuil d'immobilisation, c'est une charge, au compte des fournitures éducatives.

**Q039 — Réponse B** (dans ASS, 40-HABITAT)  
La première question est « quelle structure porte la dépense ? ». La dépense est celle de l'habitat inclusif (structure ASS), même si le salarié est payé par le SAVS.

**Q040 — Réponse A** (ne pas la saisir, traiter la relance)  
Un duplicata n'est pas une nouvelle facture. Le saisir créerait un doublon et un risque de double paiement.

**Q041 — Réponse C** (signaler, sans écrire dans PA)  
Le journal PA est automatique : on ne le modifie pas à la main. On garde un seul circuit pour l'IJSS (la banque, selon la procédure T21) et on demande la correction du paramétrage de la paie. Une OD supplémentaire (réponse B) aggraverait le doublon.

---

## F. Fin d'exercice

**Q042 — Réponse D** (D 6223221 / C 4081000)  
La charge est au débit, le 4081000 (dette) au **crédit**. Attention : le document T21 écrit l'inverse (« débité en N ») ; c'est une erreur de rédaction (E18-09, E18-12).

**Q043 — Réponse A** (1 800,00 € au débit du 4860000)  
Janvier à mars 2027 = 3 mois : 7 200,00 × 3/12 = 1 800,00 €. La CCA est un actif (débit 4860000), la charge est créditée. C'est l'exemple du document T21.

**Q044 — Réponse B** (D 6618000 292,00 / C 1648000 292,00)  
Novembre et décembre = 2 mois sur 3 : 438,00 × 2/3 = 292,00 €. Intérêts courus au crédit du 1648000 (document T21, classe 16), charge en 6618000.

**Q045 — Réponse C** (fonds dédiés)  
La subvention finance un **projet** non encore entièrement réalisé : la part non utilisée est reportée en fonds dédiés (6892200 au débit, compte 19 au crédit), puis reprise en 7892200 quand les dépenses sont faites.

**Q046 — Réponse D** (produit constaté d'avance)  
La convention finance une **période** : 6 mois sur 12 concernent 2027. 24 000,00 × 6/12 = 12 000,00 € en 4878000 « Produits constatés d'avance – Subventions ».

**Q047 — Réponse A** (47 et 58)  
Document T21 : les comptes 47 « doivent être soldés à chaque fin d'exercice » et les comptes 58 « doivent présenter un solde nul ». Les comptes 18 ne sont nuls qu'**additionnés** pour toute l'association, pas un par un.

**Q048 — Réponse B** (crédité)  
L'extourne est l'inverse exact de l'écriture du 31/12 : D 4081000 / C 6061200. C'est l'« exception » citée par le document T21 pour la classe 6.

**Q049 — Réponse C** (calcul EIG RH, OD si non déversé, 4282000 / 4382000)  
L'agent comptable contrôle l'état de la paie mais ne recalcule pas tout. C'est une **dette** (classe 4), pas une provision de classe 15 ; elle se passe par structure, jamais dans le journal PA.

**Q050 — Réponse D** (D 4676000 / C 7584100)  
Le remboursement est acquis en 2026 (formation suivie, accord obtenu) : produit à recevoir. 7584100 « Remboursements sur frais de formation » ; 4676000 car l'OPCO n'est pas une collectivité publique.

---

## Grille d'interprétation du score (sur 50, barème 1 point par bonne réponse)

| Score | Interprétation | Que faire ensuite |
|---|---|---|
| 45 – 50 | Excellent : vous maîtrisez les règles T21 et la saisie multi-structures. | Entraînez-vous sur le cas de synthèse E18-11 en temps limité. |
| 35 – 44 | Bon niveau : quelques automatismes à consolider. | Relisez les explications des questions manquées et refaites les exercices du thème le plus faible. |
| 0 – 34 | À revoir : certaines bases manquent encore. | Relisez la fiche du dossier et le cours M18, puis refaites E18-09 à E18-12 avant de repasser le QCM. |

---

[Retour aux questions](QCM_questions.md)
