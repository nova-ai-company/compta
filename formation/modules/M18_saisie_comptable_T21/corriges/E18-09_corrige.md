# Corrigé E18-09 — Les travaux de fin d'exercice au 31/12/2026, structure par structure

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
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **CA** | Chiffre d'affaires (ou journal de caisse, ou compte administratif). Le plus souvent : le total des ventes HT de l'année. Dans une liste de journaux, « CA » peut désigner le journal de caisse. Dans le médico-social (M16, M17), CA = compte administratif : le compte rendu annuel d'un service hors CPOM (ex. : le SAVS) remis au Département. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CCA** | Charges constatées d'avance — ou compte courant d'associé. Deux sens selon le contexte : (1) clôture : charge payée en N mais qui concerne N+1 (compte 486) ; (2) financement : argent prêté par un associé à sa société (compte 455). |
    | **CP** | Congés payés. Jours de vacances payés acquis par les salariés. À la clôture, on provisionne les CP acquis et non pris (dette de l'employeur). |
    | **DAB** | Distributeur automatique de billets. Retrait d'espèces : à justifier (alimentation de la caisse ou prélèvement de l'exploitant). |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ERRD** | État réalisé des recettes et des dépenses. Le compte rendu de l'EPRD après la clôture : réalisé, écarts, proposition d'affectation du résultat. Dépôt en général au 30 avril N+1 (à vérifier). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **FNP** | Factures non parvenues. À la clôture : charges de l'année dont la facture n'est pas encore arrivée. On les enregistre quand même (compte 408) pour que l'année supporte ses vraies charges. |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **ICNE** | Intérêts courus non échus. À la clôture : intérêts d'emprunt qui concernent l'année mais qui seront payés à la prochaine échéance. On les enregistre en charge de N. |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N+1** | L'exercice suivant. L'année comptable d'après (ex. : si N = 2026, N+1 = 2027). Une charge « de N+1 » ne doit pas peser sur le résultat de N. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **OPCO** | Opérateur de compétences. Organisme qui finance la formation professionnelle des salariés de la branche. |
    | **PA** | Plateforme agréée — ou, dans le M18, journal de paie. Opérateur agréé par l'État (anciennement « PDP ») qui transmet les factures électroniques entre entreprises et envoie les données à l'administration. Dans le module M18, PA est le code du journal des salaires, alimenté automatiquement par EIG RH. |
    | **PCA** | Produits constatés d'avance. À la clôture : produit facturé en N mais qui concerne N+1 (compte 487). On le retire du chiffre d'affaires de N. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **Compte 1640000** | Emprunts auprès des Ets de crédit (plan T21). Capital restant dû des emprunts bancaires. Crédité au déblocage, débité à chaque remboursement de capital. |
    | **Compte 1648000** | Intérêts courus sur emprunts auprès des Ets de crédit (plan T21). Intérêts courus non échus (ICNE) : intérêts de l'exercice qui seront payés l'an prochain. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 1940000** | Fonds dédiés sur subventions d'exploitation (plan T21). Subvention d'exploitation affectée à un projet et non dépensée au 31/12 (ex. : fondation pour le projet Pairs). |
    | **Compte 1950000** | Fonds dédiés sur contribution financières d'autres organismes (plan T21). Contributions financières d'autres organismes (ex. : fondation d'entreprise) non utilisées. |
    | **Compte 1960000** | Fonds dédiés sur ressources liées à la générosité du public (plan T21). Dons du public affectés à un projet et non utilisés. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4282000** | Dettes provisionnées pour congés à payer (plan T21). Congés payés acquis et non pris à la clôture (dette envers les salariés). |
    | **Compte 4382000** | Charges sociales sur congés à payer (plan T21). Charges sociales sur les congés payés provisionnés. |
    | **Compte 4417000** | Subventions d'exploitation (plan T21). Subvention d'exploitation accordée mais pas encore reçue (créance sur le financeur). |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4686000** | Comptes créditeurs et Charges à payer (plan T21). Charge de N à payer qui n'est ni un fournisseur, ni une dette sociale ou fiscale. |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4730000** | Comptes d’attente (plan T21). Second compte d'attente (même libellé que 4710000 : à clarifier). Même règle : soldé au 31/12. |
    | **Compte 4860000** | Charges constatées d’avance (plan T21). Charge constatée d'avance : facturée en N mais concernant N+1 (ex. : assurance avril N – mars N+1). |
    | **Compte 4878000** | Produits constatés d’avance - Subventions (plan T21). Subvention reçue en N pour une période de N+1 (ex. : année scolaire). |
    | **Compte 5300000** | Caisse (plan T21). Caisse (espèces). Le solde doit être égal au comptage physique. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6061200** | Energie, électricité (plan T21). Facture d'électricité (exemple du document T21 : EDF). |
    | **Compte 6161000** | Assurance Multirisques (plan T21). Assurance multirisque des locaux. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6226010** | Honoraires comptabilité (plan T21). Honoraires de l'expert-comptable (et du commissaire aux comptes, faute de compte dédié dans le plan : à vérifier). |
    | **Compte 6256100** | Frais Conseil d'Administration, Bénévoles, Mission CA/Représ (plan T21). Frais des administrateurs bénévoles (conseil d'administration, représentation). |
    | **Compte 6262000** | Frais de télécommunication (plan T21). Téléphone, internet. |
    | **Compte 6412000** | Congés payés (plan T21). Congés payés (et variation de la provision). |
    | **Compte 6451800** | Provision sur charges Congés Payés (plan T21). Charges sociales sur la provision pour congés payés. |
    | **Compte 6618000** | Autres charges d'intérêt - intérêts courus (plan T21). Intérêts courus à la clôture (ICNE). |
    | **Compte 6892200** | Report en fonds dédiés à l'exploitation (plan T21). Mise en fonds dédiés de la part non dépensée d'une subvention d'exploitation affectée. |
    | **Compte 7410002** | Subvention Fondation de France (plan T21). Subvention de la Fondation de France. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7584100** | Remboursements sur frais de formation ancien compte 6498000 (plan T21). Remboursement de frais de formation (OPCO). Ancien compte 6498000. |
    | **Compte 7892200** | Fonds dédiés - Exploitation (plan T21). Utilisation, l'année suivante, des fonds dédiés d'exploitation (quand on dépense enfin la subvention). |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOORANGE** | Compte fournisseur télécom (dossier M18). Contrat unique de téléphonie et internet facturé au siège, réparti en IS selon les ETP. |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **charges constatées d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
    | **produit à recevoir** | Recette acquise mais pas encore reçue. Ex. : solde d'une subvention AGEFIPH dû au 31/12, versé en mars. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-09](../exercices/E18-09_travaux-fin-exercice-t21.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

!!! abstract "En clair"
    À la clôture, on se pose trois questions pour chaque information : **(1) à quelle année appartient cette charge ou ce produit ?** (2) **dans quels livres** (quelle structure) l'écriture doit-elle aller ? (3) l'écriture devra-t-elle être **annulée (extournée)** le 01/01/2027 ? Dans un organisme à plusieurs structures, la deuxième question est aussi importante que la première : une charge juste mais dans la mauvaise structure fausse le compte rendu d'un financeur.

### Question 1 — Le sens du compte 4081000 dans le document T21

La phrase du document est **inversée**. Raisonnons simplement :

- Au 31/12/2026, la prestation a eu lieu (Claire Dupont a fait ses 18 séances en décembre), mais **la facture n'est pas arrivée**. On doit quand même enregistrer la **charge** en 2026 : la charge est au **débit** (6223221).
- Il faut une contrepartie : c'est une **dette** envers une personne qui n'a pas encore facturé. Une dette est au **crédit**. Le 4081000 « remplace » le compte LI ou FO, qui serait lui aussi **crédité** à la réception d'une facture.
- Donc **en N, le 4081000 est crédité**. En N+1, on **extourne** (le 4081000 est débité, la charge créditée), puis on saisit la vraie facture normalement (charge au débit, LI ou FO au crédit).

Le document a sans doute voulu dire « le **compte de charge** est débité en N ». À signaler à la Fédération avec tact (voir § 5).

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2026 | SES | OD | 6223221 | Honoraires Orthophonistes | FNP Dupont – 18 séances – 12/2026 | 10-SESSAD | 612,00 | |
| 31/12/2026 | SES | OD | 4081000 | Fournisseurs factures non parvenues | FNP Dupont – 18 séances – 12/2026 | | | 612,00 |
| 01/01/2027 | SES | OD | 4081000 | Fournisseurs factures non parvenues | Extourne FNP Dupont – 12/2026 | | 612,00 | |
| 01/01/2027 | SES | OD | 6223221 | Honoraires Orthophonistes | Extourne FNP Dupont – 12/2026 | 10-SESSAD | | 612,00 |
| 11/01/2027 | SES | AC | 4011000 | Libéraux (tiers LIDUPONT) | LIDUPONT – orthophonie – F2026-12 – 12/2026 | | | 612,00 |
| 11/01/2027 | SES | AC | 6223221 | Honoraires Orthophonistes | LIDUPONT – orthophonie – F2026-12 – 12/2026 | 10-SESSAD | 612,00 | |
| | | | | | **Total** | | **1 836,00** | **1 836,00** |

Bilan de l'opération : 612,00 € de charge en **2026** (l'année des séances), **0,00 €** en 2027 (extourne − 612 puis facture + 612). C'est exactement le but.

### Question 2 — Tableau de synthèse

| Info | Structure(s) | Principe | Comptes | Montant |
|---|---|---|---|---|
| 1 | SIE, avec IS vers SES, SAV, EMP, ASS | Électricité consommée en 2026, facture en 2027 → **FNP** | 6061200 / 4081000, et 184x / 1840000 pour les IS | 1 860,00 € |
| 2 | SIE, avec IS (clé forfait) | Travaux de décembre 2026 → **FNP** | 6226010 / 4081000 | 2 280,00 € |
| 3 | SES | Séances de décembre → **FNP** | 6223221 / 4081000 | 612,00 € |
| 4 | **Les 5 structures**, chacune sur sa part | 3 mois de prime (janvier-mars 2027) → **CCA** | 4860000 / 6161000 | 1 800,00 € |
| 5 | SES | Intérêts de novembre-décembre 2026 payés en 2027 → **intérêts courus** | 6618000 / 1648000 | 292,00 € |
| 6 | EMP | Subvention pour une période à cheval → **produit constaté d'avance** | 7488000 / 4878000 | 12 000,00 € |
| 7 | SAV | Remboursement acquis en 2026, encaissé en 2027 → **produit à recevoir** | 4676000 / 7584100 | 1 450,00 € |
| 8 | ASS | Frais de décembre, état remis en 2027 → **charge à payer** | 6256100 / 4686000 | 386,40 € |
| 9 | ASS (50-PAIRS) | Ressource affectée non utilisée → **fonds dédiés** | 6892200 / 1950000 | 12 650,00 € |
| 10 | Les 5 structures | Congés acquis en 2026, pris en 2027 → **dette de congés payés** | 6412000 / 4282000 et 6451800 / 4382000 | 172 246,00 € |

**Pourquoi des comptes différents pour des « dettes de fin d'année » ?** Le plan T21 a un compte par famille : **4081000** quand on attend une **facture** d'un fournisseur ou d'un libéral ; **4686000** « Comptes créditeurs et charges à payer » pour les autres créanciers (ici des bénévoles, qui n'ont ni compte FO ni compte SA) ; **4282000 / 4382000** pour le personnel et les organismes sociaux ; **1648000** pour les intérêts d'un emprunt.

### Question 4 — Pourquoi la CCA d'assurance se passe dans chaque structure

En avril 2026, le siège a saisi la prime de 7 200,00 € et a **renvoyé** à chaque structure sa part (clé m²) par les comptes de liaison. Résultat : chaque structure porte déjà **sa** charge d'assurance dans **son** compte 6161000 (le SESSAD : 7 200,00 × 45 % = 3 240,00 €). Le trop de charge (les 3 mois de 2027) est donc **dans chaque structure**. Si on ne passait la CCA qu'au siège pour 1 800,00 €, le siège aurait une charge **négative** de 1 530,00 € sur sa part, et le SESSAD garderait 810,00 € de charge de 2027 dans son ERRD. On régularise **là où est la charge**.

### Question 5 — Produit constaté d'avance ou fonds dédiés ?

- **Produit constaté d'avance (AGEFIPH, info 6)** : la convention finance une **période** (01/07/2026 – 30/06/2027). Six mois sur douze appartiennent à **2027**. Même si l'argent est encaissé, la moitié du produit n'est **pas encore gagnée** en 2026 : 24 000,00 × 6/12 = **12 000,00 €** en **4878000** « Produits constatés d'avance – Subventions ». C'est une question de **calendrier**.
- **Fonds dédiés (Fondation Lumen, info 9)** : la subvention finance un **projet** précis (« Pairs et voix »), pas une période. À la clôture, une partie n'a **pas encore été dépensée** pour le projet : 40 000,00 − 27 350,00 = **12 650,00 €**. On ne la laisse pas dans le résultat 2026 (sinon ASS afficherait un excédent qui ne lui appartient pas : l'argent est **dû au projet**, voire à restituer). On la « met de côté » par la charge **6892200** « Report en fonds dédiés à l'exploitation » au débit et un compte **19** au crédit. C'est une question d'**emploi des fonds**.

**1940000 ou 1950000 ?** Le plan T21 propose :

- **1940000** « Fonds dédiés sur **subventions d'exploitation** » ;
- **1950000** « Fonds dédiés sur **contributions financières d'autres organismes** » ;
- 1960000 « … sur ressources liées à la générosité du public » (dons : ne convient pas).

La Fondation Lumen est une **fondation privée**, pas une autorité publique. Dans la réglementation comptable des associations, le mot « subvention » vise les financements des **autorités administratives** ; l'argent d'une fondation privée est une « **contribution financière d'un autre organisme** ». L'intitulé du **1950000** décrit donc exactement la ressource : c'est le choix retenu ici.

Contre-argument à connaître : le plan T21 enregistre les dons de fondations en « Subvention Fondation de France » (**7410002**), et le dossier a crédité **7488000** « Autres subventions et participations ». Certaines associations utilisent donc **1940000** par cohérence avec le compte de produit. Les deux se défendent ; l'important est de **valider le choix avec Hélène Ferrand** et de garder **la même méthode chaque année** (le tableau des fonds dédiés de l'annexe est présenté par nature de ressource).

### Question 6 — Qui calcule les congés payés ?

- **Le calcul** (jours acquis, jours pris, valorisation au salaire) est fait par le **logiciel de paie EIG RH**, à partir des compteurs de congés de chaque salarié. Ce n'est **pas** à l'agent comptable de recalculer salarié par salarié : il **contrôle** l'état.
- **L'écriture** : le journal de paie **PA** est automatique et **aucune écriture manuelle n'y est autorisée** (document « Les journaux comptables »). Comme EIG RH ne déverse pas la provision (hypothèse de l'énoncé), on la passe en **OD**. *Si un jour EIG RH la déverse lui-même, ne surtout pas la repasser en OD (doublon).*
- **À vérifier avant de saisir** : (1) que l'état est bien arrêté au **31/12/2026** et ventilé **par structure** (et par code analytique pour ASS : 40-HABITAT) ; (2) la vraisemblance par rapport au 31/12/2025 (variation des effectifs, départs) ; (3) que l'**extourne** de l'écriture 2025 a bien été passée le 01/01/2026 (sinon la dette serait comptée deux fois) ; (4) le **taux de charges** retenu (42 %, *à vérifier chaque année*) avec le service paie.

Les comptes : **6412000** « Congés payés » / **4282000** « Dettes provisionnées pour congés à payer » pour le brut ; **6451800** « Provision sur charges Congés Payés » / **4382000** « Charges sociales sur congés à payer » pour les charges patronales. Malgré les mots « provision » et « provisionnées », c'est une **dette** (classe 4), pas une provision de classe 15 : on connaît les salariés et le montant.

## 2. Calculs (détaillés, chaque montant justifié)

**Répartitions IS (informations 1, 2 et 4)**

| Charge | Total | SIE | SES | SAV | EMP | ASS |
|---|---|---|---|---|---|---|
| FNP EDF (clé m² 15/45/25/10/5) | 1 860,00 € | 279,00 € | 837,00 € | 465,00 € | 186,00 € | 93,00 € |
| FNP Ferrand (forfait 20/40/20/10/10) | 2 280,00 € | 456,00 € | 912,00 € | 456,00 € | 228,00 € | 228,00 € |
| CCA assurance : 7 200,00 × 3/12 = 1 800,00 € (clé m²) | 1 800,00 € | 270,00 € | 810,00 € | 450,00 € | 180,00 € | 90,00 € |

**Autres calculs**

| Info | Calcul | Montant |
|---|---|---|
| 3 — FNP Dupont | 18 × 34,00 | 612,00 € |
| 5 — Intérêts courus | 438,00 × 2/3 (novembre et décembre sur 3 mois) | 292,00 € |
| 6 — PCA AGEFIPH | 24 000,00 × 6/12 (janvier à juin 2027) | 12 000,00 € |
| 7 — Produit à recevoir OPCO | accord de prise en charge | 1 450,00 € |
| 8 — Charge à payer bénévoles | état signé | 386,40 € |
| 9 — Fonds dédiés | 40 000,00 − 27 350,00 | 12 650,00 € |

*Le capital de l'échéance (2 912,00 €) ne donne lieu à **aucune** écriture d'inventaire : il figure déjà dans le solde du compte 1640000 (le capital restant dû). Seuls les intérêts « courent » avec le temps.*

**Congés payés (information 10)**

| Structure | Brut (6412000 / 4282000) | Charges 42 % (6451800 / 4382000) | Total |
|---|---|---|---|
| SIE | 10 250,00 € | 4 305,00 € | 14 555,00 € |
| SES | 61 300,00 € | 25 746,00 € | 87 046,00 € |
| SAV | 32 480,00 € | 13 641,60 € | 46 121,60 € |
| EMP | 13 120,00 € | 5 510,40 € | 18 630,40 € |
| ASS | 4 150,00 € | 1 743,00 € | 5 893,00 € |
| **Total** | **121 300,00 €** | **50 946,00 €** | **172 246,00 €** |

## 3. Écritures comptables

*Colonne « Livres » : la structure dans laquelle l'écriture est passée. Les comptes FO, LI, SA sont indiqués entre parenthèses derrière leur compte de centralisation.*

**A. Factures non parvenues communes, saisies au siège avec IS**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2026 | SIE | OD | 6061200 | Energie, électricité | FNP EDF – électricité Valence – 11-12/2026 – part siège 15 % | 01-SIEGE | 279,00 | |
| 31/12/2026 | SIE | OD | 1849100 | Liaison SESSAD | FNP EDF – IS SESSAD 45 % | | 837,00 | |
| 31/12/2026 | SIE | OD | 1849200 | Liaison SAVS | FNP EDF – IS SAVS 25 % | | 465,00 | |
| 31/12/2026 | SIE | OD | 1849300 | Liaison Emploi | FNP EDF – IS Emploi 10 % | | 186,00 | |
| 31/12/2026 | SIE | OD | 1849400 | Liaison Association | FNP EDF – IS Asso 5 % | | 93,00 | |
| 31/12/2026 | SIE | OD | 4081000 | Fournisseurs factures non parvenues | FNP EDF – électricité Valence – 11-12/2026 | | | 1 860,00 |
| 31/12/2026 | SIE | OD | 6226010 | Honoraires comptabilité | FNP Ferrand – paie 12/2026 et clôture – part siège 20 % | 01-SIEGE | 456,00 | |
| 31/12/2026 | SIE | OD | 1849100 | Liaison SESSAD | FNP Ferrand – IS SESSAD 40 % | | 912,00 | |
| 31/12/2026 | SIE | OD | 1849200 | Liaison SAVS | FNP Ferrand – IS SAVS 20 % | | 456,00 | |
| 31/12/2026 | SIE | OD | 1849300 | Liaison Emploi | FNP Ferrand – IS Emploi 10 % | | 228,00 | |
| 31/12/2026 | SIE | OD | 1849400 | Liaison Association | FNP Ferrand – IS Asso 10 % | | 228,00 | |
| 31/12/2026 | SIE | OD | 4081000 | Fournisseurs factures non parvenues | FNP Ferrand – paie 12/2026 et clôture | | | 2 280,00 |
| | | | | | **Total** | | **4 140,00** | **4 140,00** |

**B. Écritures « miroir » des IS dans les structures**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2026 | SES | OD | 6061200 | Energie, électricité | FNP EDF 11-12/2026 – IS reçue du siège | 10-SESSAD | 837,00 | |
| 31/12/2026 | SES | OD | 6226010 | Honoraires comptabilité | FNP Ferrand 12/2026 – IS reçue du siège | 10-SESSAD | 912,00 | |
| 31/12/2026 | SES | OD | 1840000 | Liaison Siège | FNP EDF et Ferrand – IS reçues du siège | | | 1 749,00 |
| 31/12/2026 | SAV | OD | 6061200 | Energie, électricité | FNP EDF 11-12/2026 – IS reçue du siège | 20-SAVS | 465,00 | |
| 31/12/2026 | SAV | OD | 6226010 | Honoraires comptabilité | FNP Ferrand 12/2026 – IS reçue du siège | 20-SAVS | 456,00 | |
| 31/12/2026 | SAV | OD | 1840000 | Liaison Siège | FNP EDF et Ferrand – IS reçues du siège | | | 921,00 |
| 31/12/2026 | EMP | OD | 6061200 | Energie, électricité | FNP EDF 11-12/2026 – IS reçue du siège | 30-EMPLOI | 186,00 | |
| 31/12/2026 | EMP | OD | 6226010 | Honoraires comptabilité | FNP Ferrand 12/2026 – IS reçue du siège | 30-EMPLOI | 228,00 | |
| 31/12/2026 | EMP | OD | 1840000 | Liaison Siège | FNP EDF et Ferrand – IS reçues du siège | | | 414,00 |
| 31/12/2026 | ASS | OD | 6061200 | Energie, électricité | FNP EDF 11-12/2026 – IS reçue du siège | 90-ASSO | 93,00 | |
| 31/12/2026 | ASS | OD | 6226010 | Honoraires comptabilité | FNP Ferrand 12/2026 – IS reçue du siège | 90-ASSO | 228,00 | |
| 31/12/2026 | ASS | OD | 1840000 | Liaison Siège | FNP EDF et Ferrand – IS reçues du siège | | | 321,00 |
| | | | | | **Total** | | **3 405,00** | **3 405,00** |

*Si EIG génère le miroir automatiquement quand on renseigne le compte IS (ce que décrit le document T21), ces lignes apparaissent toutes seules : contrôlez qu'elles existent, ne les doublez pas.*

**C. FNP directe, charges constatées d'avance, intérêts courus**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2026 | SES | OD | 6223221 | Honoraires Orthophonistes | FNP Dupont – 18 séances – 12/2026 | 10-SESSAD | 612,00 | |
| 31/12/2026 | SES | OD | 4081000 | Fournisseurs factures non parvenues | FNP Dupont – 18 séances – 12/2026 | | | 612,00 |
| 31/12/2026 | SIE | OD | 4860000 | Charges constatées d'avance | CCA MAAF multirisque – 01-03/2027 – part siège | | 270,00 | |
| 31/12/2026 | SIE | OD | 6161000 | Assurance Multirisques | CCA MAAF multirisque – 01-03/2027 – part siège | 01-SIEGE | | 270,00 |
| 31/12/2026 | SES | OD | 4860000 | Charges constatées d'avance | CCA MAAF multirisque – 01-03/2027 – part SESSAD | | 810,00 | |
| 31/12/2026 | SES | OD | 6161000 | Assurance Multirisques | CCA MAAF multirisque – 01-03/2027 – part SESSAD | 10-SESSAD | | 810,00 |
| 31/12/2026 | SAV | OD | 4860000 | Charges constatées d'avance | CCA MAAF multirisque – 01-03/2027 – part SAVS | | 450,00 | |
| 31/12/2026 | SAV | OD | 6161000 | Assurance Multirisques | CCA MAAF multirisque – 01-03/2027 – part SAVS | 20-SAVS | | 450,00 |
| 31/12/2026 | EMP | OD | 4860000 | Charges constatées d'avance | CCA MAAF multirisque – 01-03/2027 – part Emploi | | 180,00 | |
| 31/12/2026 | EMP | OD | 6161000 | Assurance Multirisques | CCA MAAF multirisque – 01-03/2027 – part Emploi | 30-EMPLOI | | 180,00 |
| 31/12/2026 | ASS | OD | 4860000 | Charges constatées d'avance | CCA MAAF multirisque – 01-03/2027 – part Asso | | 90,00 | |
| 31/12/2026 | ASS | OD | 6161000 | Assurance Multirisques | CCA MAAF multirisque – 01-03/2027 – part Asso | 90-ASSO | | 90,00 |
| 31/12/2026 | SES | OD | 6618000 | Autres charges d'intérêt - intérêts courus | ICNE emprunt Crédit Mutuel – 11-12/2026 | 10-SESSAD | 292,00 | |
| 31/12/2026 | SES | OD | 1648000 | Intérêts courus sur emprunts auprès des Ets de crédit | ICNE emprunt Crédit Mutuel – échéance 31/01/2027 | | | 292,00 |
| | | | | | **Total** | | **2 704,00** | **2 704,00** |

**D. Produit constaté d'avance, produit à recevoir, charge à payer, fonds dédiés**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2026 | EMP | OD | 7488000 | Autres Subventions et participations | PCA AGEFIPH conv. 2026-EA-26-117 – 01-06/2027 | 30-EMPLOI | 12 000,00 | |
| 31/12/2026 | EMP | OD | 4878000 | Produits constatés d'avance - Subventions | PCA AGEFIPH conv. 2026-EA-26-117 – 01-06/2027 | | | 12 000,00 |
| 31/12/2026 | SAV | OD | 4676000 | Comptes débiteurs et Produits à recevoir | OPCO – prise en charge formation 16-20/11/2026 | | 1 450,00 | |
| 31/12/2026 | SAV | OD | 7584100 | Remboursements sur frais de formation | OPCO – prise en charge formation 16-20/11/2026 | 20-SAVS | | 1 450,00 |
| 31/12/2026 | ASS | OD | 6256100 | Frais Conseil d'Administration, Bénévoles | Frais déplacement bénévoles – CA du 12/12/2026 | 90-ASSO | 386,40 | |
| 31/12/2026 | ASS | OD | 4686000 | Comptes créditeurs et Charges à payer | Frais déplacement bénévoles – CA du 12/12/2026 | | | 386,40 |
| 31/12/2026 | ASS | OD | 6892200 | Report en fonds dédiés à l'exploitation | Fondation Lumen – Pairs et voix – part non utilisée 2026 | 50-PAIRS | 12 650,00 | |
| 31/12/2026 | ASS | OD | 1950000 | Fonds dédiés sur contribution financières d'autres organismes | Fondation Lumen – Pairs et voix – part non utilisée 2026 | | | 12 650,00 |
| | | | | | **Total** | | **26 486,40** | **26 486,40** |

*Le remboursement OPCO va en **7584100** « Remboursements sur frais de formation » (l'intitulé du plan précise « ancien compte 6498000 ») : c'est un produit, pas une diminution du compte de formation. Une subvention **publique** à recevoir irait plutôt en **4417000** « Subventions d'exploitation » ; l'OPCO n'étant pas une collectivité publique, on utilise **4676000**.*

**E. Congés payés (état EIG RH)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2026 | SIE | OD | 6412000 | Congés payés | CP acquis non pris au 31/12/2026 – état EIG RH | 01-SIEGE | 10 250,00 | |
| 31/12/2026 | SIE | OD | 6451800 | Provision sur charges Congés Payés | Charges sur CP au 31/12/2026 (42 %) | 01-SIEGE | 4 305,00 | |
| 31/12/2026 | SIE | OD | 4282000 | Dettes provisionnées pour congés à payer | CP acquis non pris au 31/12/2026 | | | 10 250,00 |
| 31/12/2026 | SIE | OD | 4382000 | Charges sociales sur congés à payer | Charges sur CP au 31/12/2026 | | | 4 305,00 |
| 31/12/2026 | SES | OD | 6412000 | Congés payés | CP acquis non pris au 31/12/2026 – état EIG RH | 10-SESSAD | 61 300,00 | |
| 31/12/2026 | SES | OD | 6451800 | Provision sur charges Congés Payés | Charges sur CP au 31/12/2026 (42 %) | 10-SESSAD | 25 746,00 | |
| 31/12/2026 | SES | OD | 4282000 | Dettes provisionnées pour congés à payer | CP acquis non pris au 31/12/2026 | | | 61 300,00 |
| 31/12/2026 | SES | OD | 4382000 | Charges sociales sur congés à payer | Charges sur CP au 31/12/2026 | | | 25 746,00 |
| 31/12/2026 | SAV | OD | 6412000 | Congés payés | CP acquis non pris au 31/12/2026 – état EIG RH | 20-SAVS | 32 480,00 | |
| 31/12/2026 | SAV | OD | 6451800 | Provision sur charges Congés Payés | Charges sur CP au 31/12/2026 (42 %) | 20-SAVS | 13 641,60 | |
| 31/12/2026 | SAV | OD | 4282000 | Dettes provisionnées pour congés à payer | CP acquis non pris au 31/12/2026 | | | 32 480,00 |
| 31/12/2026 | SAV | OD | 4382000 | Charges sociales sur congés à payer | Charges sur CP au 31/12/2026 | | | 13 641,60 |
| 31/12/2026 | EMP | OD | 6412000 | Congés payés | CP acquis non pris au 31/12/2026 – état EIG RH | 30-EMPLOI | 13 120,00 | |
| 31/12/2026 | EMP | OD | 6451800 | Provision sur charges Congés Payés | Charges sur CP au 31/12/2026 (42 %) | 30-EMPLOI | 5 510,40 | |
| 31/12/2026 | EMP | OD | 4282000 | Dettes provisionnées pour congés à payer | CP acquis non pris au 31/12/2026 | | | 13 120,00 |
| 31/12/2026 | EMP | OD | 4382000 | Charges sociales sur congés à payer | Charges sur CP au 31/12/2026 | | | 5 510,40 |
| 31/12/2026 | ASS | OD | 6412000 | Congés payés | CP acquis non pris au 31/12/2026 – état EIG RH | 40-HABITAT | 4 150,00 | |
| 31/12/2026 | ASS | OD | 6451800 | Provision sur charges Congés Payés | Charges sur CP au 31/12/2026 (42 %) | 40-HABITAT | 1 743,00 | |
| 31/12/2026 | ASS | OD | 4282000 | Dettes provisionnées pour congés à payer | CP acquis non pris au 31/12/2026 | | | 4 150,00 |
| 31/12/2026 | ASS | OD | 4382000 | Charges sociales sur congés à payer | Charges sur CP au 31/12/2026 | | | 1 743,00 |
| | | | | | **Total** | | **172 246,00** | **172 246,00** |

**F. Question 7 — Comptes 47, 58 et 18 remis d'aplomb**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2026 | SES | OD | 4010000 | Fournisseurs (tiers FOLUDIK) | Reclassement prélèvement 18/12 – règlement LE-2026-1187 | | 214,80 | |
| 31/12/2026 | SES | OD | 4710000 | Comptes d'attente | Reclassement prélèvement 18/12 – LUDIK EDUCATION | | | 214,80 |
| 11/12/2026 | ASS | CAASS | 5300000 | Caisse | Retrait DAB 11/12 – caisse marché de Noël (ligne automatique) | | 300,00 | |
| 11/12/2026 | ASS | CAASS | 5800000 | Virements internes | Retrait DAB 11/12 – caisse marché de Noël | | | 300,00 |
| 30/12/2026 | SAV | OD | 6262000 | Frais de télécommunication | FOORANGE – flotte 12/2026 – IS reçue du siège 27 % | 20-SAVS | 432,00 | |
| 30/12/2026 | SAV | OD | 1840000 | Liaison Siège | FOORANGE – flotte 12/2026 – IS reçue du siège | | | 432,00 |
| | | | | | **Total** | | **946,80** | **946,80** |

Après lettrage, FOLUDIK est soldé (facture 214,80 au crédit, règlement 214,80 au débit). L'entrée en caisse se saisit **à sa vraie date** (11/12/2026) dans le journal **CAASS** : on tape seulement 5800000 au crédit, le logiciel met le 5300000 au débit. Le 5800000 de ASS revient à **zéro**.

**Contrôle des comptes de liaison après toutes les écritures (A, B et F)**

| Paire | Siège : compte et solde | Structure : 1840000 et solde | Écart |
|---|---|---|---|
| Siège / SESSAD | 1849100 : 18 640,20 + 837,00 + 912,00 = **20 389,20 D** | 18 640,20 + 1 749,00 = **20 389,20 C** | 0,00 € |
| Siège / SAVS | 1849200 : 9 875,40 + 465,00 + 456,00 = **10 796,40 D** | 9 443,40 + 921,00 + 432,00 = **10 796,40 C** | 0,00 € |
| Siège / Emploi | 1849300 : 3 214,60 + 186,00 + 228,00 = **3 628,60 D** | 3 214,60 + 414,00 = **3 628,60 C** | 0,00 € |
| Siège / Association | 1849400 : 1 120,00 C − 93,00 − 228,00 = **799,00 C** | 1 120,00 D − 321,00 = **799,00 D** | 0,00 € |
| **Toute l'association** | Siège : 20 389,20 + 10 796,40 + 3 628,60 − 799,00 = **34 015,20 D** | Structures : **34 015,20 C** | **0,00 €** ✓ |

Les comptes 18 additionnés de toute l'association font bien **zéro** (document T21, classe 18).

**G. Question 5 — Reprise des fonds dédiés en 2027**

Les 12 650,00 € sont dépensés pour le projet en 2027. À la clôture 2027 (ou au fil des dépenses), on « libère » les fonds mis de côté :

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 31/12/2027 | ASS | OD | 1950000 | Fonds dédiés sur contribution financières d'autres organismes | Fondation Lumen – Pairs et voix – utilisation 2027 | | 12 650,00 | |
| 31/12/2027 | ASS | OD | 7892200 | Fonds dédiés - Exploitation | Fondation Lumen – Pairs et voix – utilisation 2027 | 50-PAIRS | | 12 650,00 |
| | | | | | **Total** | | **12 650,00** | **12 650,00** |

Le produit 7892200 de 2027 « couvre » les dépenses 2027 du projet : résultat du projet = 0 en 2026 comme en 2027. Si au 30/06/2027 une partie n'était pas dépensée, elle serait **à restituer** à la fondation (dette, et non plus fonds dédiés) — à vérifier dans la convention.

**H. Question 8 — Extournes au 01/01/2027**

| Écriture du 31/12/2026 | Extourne au 01/01/2027 ? | Livres | Pourquoi |
|---|---|---|---|
| FNP EDF et Ferrand (avec leurs IS et leurs miroirs) | **Oui**, écriture entière, y compris les lignes 184x et 1840000 | SIE, SES, SAV, EMP, ASS | Les vraies factures et leurs IS seront saisies en 2027 |
| FNP Dupont | **Oui** | SES | Idem |
| CCA assurance | **Oui** | Les 5 | La charge revient en 2027 |
| Intérêts courus | **Oui** | SES | L'échéance du 31/01/2027 sera saisie en totalité (438,00 €) |
| PCA AGEFIPH | **Oui** | EMP | Le produit revient en 2027 |
| Produit à recevoir OPCO | **Oui** (méthode retenue) | SAV | Le versement de février sera saisi en 7584100 ; *autre méthode possible : lettrer le 4676000 à l'encaissement, sans extourne* |
| Charge à payer bénévoles | **Oui** | ASS | Le remboursement de janvier sera saisi en charge |
| Congés payés | **Oui** | Les 5 | Méthode de l'association : extourne, puis nouvelle dette au 31/12/2027 |
| Fonds dédiés | **Non** | ASS | Le 1950000 est repris au fil des dépenses (écriture G) |
| Corrections F (4710000, 5800000, IS Orange) | **Non** | SES, ASS, SAV | Ce sont des corrections définitives, pas des régularisations |

Exemple détaillé : les extournes du **SAVS**. Toutes les charges sont **au crédit** et tous les produits **au débit** : c'est l'« exception » que cite le document T21 (classe 6 : « lors des extournes […] les charges sont reprises et donc leur saisie est au crédit »).

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 01/01/2027 | SAV | OD | 1840000 | Liaison Siège | Extourne IS FNP EDF et Ferrand 2026 | | 921,00 | |
| 01/01/2027 | SAV | OD | 6061200 | Energie, électricité | Extourne IS FNP EDF 11-12/2026 | 20-SAVS | | 465,00 |
| 01/01/2027 | SAV | OD | 6226010 | Honoraires comptabilité | Extourne IS FNP Ferrand 12/2026 | 20-SAVS | | 456,00 |
| 01/01/2027 | SAV | OD | 6161000 | Assurance Multirisques | Extourne CCA MAAF 01-03/2027 | 20-SAVS | 450,00 | |
| 01/01/2027 | SAV | OD | 4860000 | Charges constatées d'avance | Extourne CCA MAAF 01-03/2027 | | | 450,00 |
| 01/01/2027 | SAV | OD | 7584100 | Remboursements sur frais de formation | Extourne produit à recevoir OPCO | 20-SAVS | 1 450,00 | |
| 01/01/2027 | SAV | OD | 4676000 | Comptes débiteurs et Produits à recevoir | Extourne produit à recevoir OPCO | | | 1 450,00 |
| 01/01/2027 | SAV | OD | 4282000 | Dettes provisionnées pour congés à payer | Extourne CP au 31/12/2026 | | 32 480,00 | |
| 01/01/2027 | SAV | OD | 4382000 | Charges sociales sur congés à payer | Extourne charges sur CP au 31/12/2026 | | 13 641,60 | |
| 01/01/2027 | SAV | OD | 6412000 | Congés payés | Extourne CP au 31/12/2026 | 20-SAVS | | 32 480,00 |
| 01/01/2027 | SAV | OD | 6451800 | Provision sur charges Congés Payés | Extourne charges sur CP au 31/12/2026 | 20-SAVS | | 13 641,60 |
| | | | | | **Total** | | **48 942,60** | **48 942,60** |

*Attention : la CCA s'extourne dans l'autre sens que la FNP. La CCA avait **crédité** la charge le 31/12 ; son extourne la **débite** le 01/01. Le principe est toujours le même : l'extourne est l'**inverse exact** de l'écriture du 31/12.*

**Question 9 — Impact sur le résultat 2026 de chaque structure**

| Structure | Détail (− = charge, + = produit ou charge en moins) | Impact |
|---|---|---|
| SIE | FNP EDF − 279,00 ; FNP Ferrand − 456,00 ; CCA + 270,00 ; CP − 14 555,00 | **− 15 020,00 €** |
| SES | FNP EDF − 837,00 ; FNP Ferrand − 912,00 ; FNP Dupont − 612,00 ; CCA + 810,00 ; ICNE − 292,00 ; CP − 87 046,00 | **− 88 889,00 €** |
| SAV | FNP EDF − 465,00 ; FNP Ferrand − 456,00 ; CCA + 450,00 ; OPCO + 1 450,00 ; CP − 46 121,60 ; IS Orange oubliée − 432,00 | **− 45 574,60 €** |
| EMP | FNP EDF − 186,00 ; FNP Ferrand − 228,00 ; CCA + 180,00 ; PCA − 12 000,00 ; CP − 18 630,40 | **− 30 864,40 €** |
| ASS | FNP EDF − 93,00 ; FNP Ferrand − 228,00 ; CCA + 90,00 ; bénévoles − 386,40 ; fonds dédiés − 12 650,00 ; CP − 5 893,00 | **− 19 160,40 €** |
| **Association** | | **− 199 508,40 €** |

*Les corrections du 4710000 (SES) et du 5800000 (ASS) n'ont aucun effet sur le résultat : elles déplacent des sommes entre comptes de bilan. Le gros chiffre vient des congés payés, mais n'oubliez pas que l'extourne des congés payés 2025, passée le 01/01/2026, a joué en sens inverse : l'impact net « réel » des congés payés sur 2026 est la **variation** de la dette d'une année sur l'autre.*

## 4. Points d'attention / pièges

- **Le sens du 4081000** : en N, il est **crédité** (c'est une dette). Le document T21 dit le contraire ; ne le recopiez pas dans vos procédures.
- **FNP en HT** : réflexe d'une comptable venue d'une entreprise. Ici tout est **TTC** (pas de compte 445 dans le plan T21).
- **Oublier les miroirs** : une FNP commune passée au siège sans IS (ou avec IS mais sans miroir dans les structures) laisse les comptes 18 **non concordants** et fausse le résultat des services.
- **CCA au seul siège** : la charge d'assurance est **dans chaque structure** depuis l'IS d'avril ; la CCA doit suivre.
- **Intérêts courus sur le capital** : seuls les **intérêts** courent ; le capital est déjà au 1640000.
- **PCA et fonds dédiés confondus** : le PCA répond à « **quand** ? » (période), les fonds dédiés à « **pour quoi** ? » (projet non encore réalisé). Une subvention peut d'ailleurs donner les deux.
- **Congés payés passés dans le journal de paie** : interdit (journal automatique). Et vérifier qu'EIG RH ne les déverse pas déjà.
- **4710000 et 5800000** : le document T21 exige qu'ils soient **soldés** à la clôture. Un 58 non nul signale presque toujours **une moitié d'opération oubliée** (ici, la caisse).
- **Extourner les fonds dédiés** : non ! Ils se **reprennent** au fil des dépenses (7892200), ils ne s'annulent pas au 01/01.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**1. Une feuille de travail par écriture d'inventaire**, avec la pièce : l'estimation EDF (relevé du compteur), le relevé de séances de Claire Dupont, le tableau d'amortissement de l'emprunt, la convention AGEFIPH, l'accord OPCO, l'état des frais des bénévoles, la convention et l'état analytique 50-PAIRS, l'état EIG RH des congés payés.

**2. Le tableau de suivi des fonds dédiés** par projet (pour l'annexe et le compte rendu financier à la fondation) :

| Projet | Ressource | Fonds dédiés au 01/01/2026 | Reçu 2026 | Utilisé 2026 | Reporté au 31/12/2026 | Date limite |
|---|---|---|---|---|---|---|
| Pairs et voix (50-PAIRS) | Fondation Lumen | 0,00 € | 40 000,00 € | 27 350,00 € | 12 650,00 € | 30/06/2027 |

**3. Les contrôles de clôture**, à cocher pour chaque structure : 4710000 et 4730000 à zéro ; 5800000 à zéro ; 1840000 de chaque structure = opposé du 184x du siège ; somme des 18 = 0 ; banques rapprochées ; caisse = inventaire physique ; comptes FO, LI, SA lettrés ; aucun solde sur 4010000, 4011000, 4248000 qui ne soit expliqué par les comptes de tiers.

**4. Le mail à Mme Berthier sur le document T21** (diplomatique, on propose, on ne corrige pas la Fédération à sa place) :

> « Bonjour Madame Berthier, j'ai regardé le passage sur le compte 4081000. Je pense qu'il s'agit d'une inversion d'écriture : en fin d'exercice, c'est le **compte de charge** qui est débité et le **4081000** qui est **crédité** (il remplace le compte du fournisseur, qui est lui-même crédité à la réception d'une facture). L'écriture est ensuite extournée au 1er janvier. C'est ainsi que j'ai passé les écritures 2026, et Mme Ferrand pourra le confirmer le 2 février. Si vous le jugez utile, je peux préparer une petite note pour la Fédération afin que le document soit corrigé dans sa prochaine mise à jour. Bien cordialement. »

**5. Des questions à garder pour Hélène Ferrand** : le choix 1950000 / 1940000 pour la Fondation Lumen ; la méthode d'extourne du produit à recevoir ; la vérification du taux de charges sur congés payés ; le paramétrage d'EIG (miroirs IS automatiques ou non, provision CP déversée ou non).

## 6. Références

- Documents internes Trisomie 21 France : « La comptabilité chez Trisomie 21 France » (30/04/2026), § classe 16, 18, 19, 40, 42-43, 47, 48, 58 et classe 6 (extournes) ; « Les journaux comptables chez Trisomie 21 France » (30/04/2026), journaux OD, PA, CAISSE ; « Plan comptable général T21 France » (MAJ 13/10/2025).
- Plan comptable général (règlement ANC n° 2014-03 modifié) : principe d'indépendance des exercices, comptes de régularisation (charges et produits constatés d'avance), charges à payer et produits à recevoir.
- Règlement ANC n° 2018-06 relatif aux comptes annuels des personnes morales de droit privé à but non lucratif : fonds dédiés, distinction subventions / contributions financières / ressources liées à la générosité du public.
- Arrêté du 19 décembre 2025 relatif au plan comptable des ESSMS privés relevant du I de l'article L. 312-1 du CASF (comptes de liaison 18, fonds dédiés 19) : à lire dans sa version publiée.
