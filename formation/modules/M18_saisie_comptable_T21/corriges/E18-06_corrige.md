# Corrigé E18-06 — Contrôler un journal des ventes automatique, puis saisir les recettes de Cap Horizons 21

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQEMP** | Journal de banque de l'emploi accompagné. Contrepartie automatique 5124000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IME** | Institut médico-éducatif. Établissement qui accueille des enfants et adolescents avec une déficience intellectuelle. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **OGIRYS** | Abonnement facturé par la Fédération. Compte 7060002 « Abonnement annuel OGIRYS » : prestation vendue par la Fédération aux associations (nom d'outil interne). |
    | **OPCO** | Opérateur de compétences. Organisme qui finance la formation professionnelle des salariés de la branche. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **VIR** | Virement. Abréviation utilisée sur les relevés bancaires. |
    | **VT** | Journal des ventes. Journal où l'on enregistre les factures clients (et les Z de caisse). |
    | **Compte 411** | Clients / usagers. Ce que l'on doit à l'association. |
    | **Compte 754** | Dons manuels (ou collectes). Dons des particuliers (numéro selon la nomenclature ANC 2018-06). |
    | **Compte 756** | Cotisations. Adhésions des membres de l'association. |
    | **Compte 1940000** | Fonds dédiés sur subventions d'exploitation (plan T21). Subvention d'exploitation affectée à un projet et non dépensée au 31/12 (ex. : fondation pour le projet Pairs). |
    | **Compte 4110000** | Clients (comptes de tiers CL…) (plan T21). Centralisation des clients. On saisit dans les comptes CL… |
    | **Compte 4417000** | Subventions d'exploitation (plan T21). Subvention d'exploitation accordée mais pas encore reçue (créance sur le financeur). |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4870000** | Produits constatés d’avance (plan T21). Produit constaté d'avance : encaissé en N mais concernant N+1. |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5124000** | Banque de l'emploi accompagné (dossier M18, fictif). Compte bancaire de l'emploi accompagné, journal BQEMP. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 6155800** | Entretien et réparations des autres matériel et outillages (plan T21). Entretien et réparation des véhicules et du matériel. |
    | **Compte 6256700** | Missions - Journées Fédérales (plan T21). Déplacements pour les journées fédérales. |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 (plan T21). Remboursements de la prévoyance pour les arrêts longs : au crédit, en banque. Ancien compte 6492000. |
    | **Compte 6892200** | Report en fonds dédiés à l'exploitation (plan T21). Mise en fonds dédiés de la part non dépensée d'une subvention d'exploitation affectée. |
    | **Compte 7060002** | Abonnement annuel OGIRYS (plan T21). Abonnement annuel OGIRYS facturé (Fédération). |
    | **Compte 7060004** | Prestations de FORMATION (plan T21). Prestations de formation vendues (Fédération). |
    | **Compte 7085200** | Frais pédagogiques de formation (plan T21). Frais pédagogiques de formation facturés. |
    | **Compte 7085300** | Inscription événements (plan T21). Inscriptions à des événements. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7312170** | Dotation du SAVS (dossier M18, numéro fictif). Le plan T21 ne prévoit que 7312130 (services pour enfants). Pour le SAVS, une autre subdivision 7312xxx est nécessaire : à vérifier dans le plan de l'association. |
    | **Compte 7410002** | Subvention Fondation de France (plan T21). Subvention de la Fondation de France. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7541110** | Dons T21 France - Internet (plan T21). Dons à T21 France reçus par internet. |
    | **Compte 7541200** | Dons Autres projets (plan T21). Dons pour d'autres projets. |
    | **Compte 7562100** | Cotisations fédérales (plan T21). Cotisations fédérales (cotisations des associations membres à la Fédération). |
    | **Compte 7584100** | Remboursements sur frais de formation ancien compte 6498000 (plan T21). Remboursement de frais de formation (OPCO). Ancien compte 6498000. |
    | **Compte 7587000** | Indemnités d'assurance (plan T21). Indemnité versée par l'assurance après un sinistre. |
    | **Compte 7892200** | Fonds dédiés - Exploitation (plan T21). Utilisation, l'année suivante, des fonds dédiés d'exploitation (quand on dépense enfin la subvention). |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **Fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
    | **produit à recevoir** | Recette acquise mais pas encore reçue. Ex. : solde d'une subvention AGEFIPH dû au 31/12, versé en mars. |
    | **subventions affectées** | Subvention donnée pour un projet précis. Elle ne peut servir qu'à ce projet ; ce qui n'est pas dépensé va en fonds dédiés ou est remboursé. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-06](../exercices/E18-06_ventes-clients-federation-et-produits.md)

> *Cadre de formation : association, personnes, sociétés et documents fictifs.*

!!! abstract "En clair"
    Pour contrôler un journal automatique, on fait **trois comparaisons** : le **nombre** de pièces (une facture = une écriture, pas deux), le **montant total** (total EIG = total des comptes 7 nets des avoirs), et la **ventilation** (chaque article dans son compte, chaque facture sur un client CL). Ensuite, le **lettrage** des encaissements confirme tout : un client qui a payé ce qu'il devait doit avoir un compte soldé.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Pourquoi on ne saisit pas les ventes

Les factures sont faites dans **EIG Gestion commerciale**, qui en garde l'original, la numérotation et le suivi des règlements. EIG **déverse** (envoie automatiquement) les écritures dans la comptabilité, par **lots**. Si le comptable retapait une facture :

- elle existerait **deux fois** en comptabilité (une fois déversée, une fois tapée) ;
- la comptabilité ne correspondrait plus à EIG, et personne ne saurait laquelle croire.

Le comptable **contrôle** : il rapproche la liste des factures d'EIG et le journal VT, puis il suit les encaissements et le lettrage. Le document T21 le dit : *« Aucune écriture manuelle n'est à passer dans ce journal. »*

### Question 2 — Les trois anomalies

**Contrôle global d'abord** : total net des factures EIG = **4 710,00**. Dans le journal VT, comptes 7 au crédit (2 400,00 + 1 800,00 + 1 800,00 + 360,00 + 450,00 = 6 810,00) moins comptes 7 au débit (300,00) = **6 510,00**. Écart : **1 800,00**. Le contrôle global révèle tout de suite qu'il y a un problème, et son montant oriente la recherche.

| N° | Anomalie | Comment un senior la repère | Ce qu'elle provoque | Correction |
|---|---|---|---|---|
| 1 | **FA-2026-0413 déversée deux fois** (lots 2611-01 et 2611-02) | Écart global de 1 800,00 = montant d'une facture ; tri du journal par n° de pièce : le même numéro apparaît deux fois | Produit gonflé de 1 800,00 ; le client Horizons 44 paraît devoir 3 600,00 ; risque de **relance injustifiée** d'un adhérent | Dans EIG : annuler le lot en doublon (ou la partie doublon du lot 2611-02) ; comprendre **pourquoi** (lot relancé après une coupure ? export fait deux fois ?) |
| 2 | **FA-2026-0414 en 7060004** au lieu de **7085200** | Comparaison article / compte : l'article FRAIS-PEDA doit aller en 7085200 (pièce A1). Le total est juste : seul un contrôle **compte par compte** le voit | Produits mal classés : le chiffre « formations » est surestimé, les « frais pédagogiques » sous-estimés. Gênant pour l'analyse et pour le bilan pédagogique de l'organisme de formation | Corriger la **fiche article** ou la facture dans EIG (l'article a été mal choisi ou mal paramétré), puis annuler et redéverser |
| 3 | **FA-2026-0415 sans compte client** (4110000, tiers vide) | Contrôle « toute ligne 411 a un tiers CL » ; la balance auxiliaire clients ne tombe plus sur le compte 4110000 de la balance générale (écart de 450,00) | Impossible de lettrer le règlement de Cap Horizons 21 ; créance « orpheline » ; le compte de centralisation est mouvementé directement, ce que le document T21 interdit | Dans EIG : compléter la **fiche client** CLCAPHORIZONS21 (compte auxiliaire manquant, sans doute un client créé récemment), puis redéverser |

> ⚠️ Erreur classique : « corriger » en tapant une écriture dans le journal VT (par exemple une ligne de 1 800,00 en sens inverse). Le journal VT doit rester le **reflet exact** d'EIG. On corrige dans EIG, et EIG redéverse.

### Question 4 — La solution de repli si la période est verrouillée

Si le lot a été intégré dans une période **clôturée** (mois verrouillé) et qu'EIG ne permet plus de l'annuler, on passe une **OD** (journal des opérations diverses, où tous les comptes sont autorisés), avec l'accord de la responsable comptable et un libellé qui renvoie au lot EIG :

- **doublon** : contre-passation du doublon (produit au débit, client au crédit) ;
- **mauvais compte** : reclassement de 7060004 vers 7085200.

L'anomalie n° 3 (**client manquant**) ne se corrige **pas** par une OD : il faudrait mouvementer le compte de centralisation 4110000 sans tiers, ce qui est interdit. Elle se corrige **obligatoirement** dans EIG (fiche client, puis redéversement), ou par l'éditeur du logiciel.

Et dans tous les cas, on corrige aussi **la cause** dans EIG (fiche article, fiche client), sinon l'erreur reviendra à la prochaine facture.

### Question 6 — L'abonnement 2027 facturé en novembre 2026

L'abonnement couvre **l'année 2027** : à la clôture du 31/12/2026, le produit de 1 800,00 € doit être **retiré** de 2026 par un **produit constaté d'avance** (compte **4870000**). Le document T21 décrit ce mécanisme pour les charges ; il est symétrique pour les produits. Écriture au 31/12/2026 (OD) : 7060002 au débit 1 800,00 / 4870000 au crédit 1 800,00, extournée le 01/01/2027.

### Question 7 — Les recettes de Cap Horizons 21 : structure, journal, compte

| Ligne | Structure | Journal | Compte tapé | Analytique | À valider ? |
|---|---|---|---|---|---|
| Fondation Lumen | ASS | BQASS | **7488000** Autres subventions et participations | 50-PAIRS | **Oui** : demander la création d'une subdivision 7410xxx « Subvention Fondation Lumen », sur le modèle des autres fondations du plan |
| Dons en ligne | ASS | BQASS | **7541110** (brut) + **6270000** (commission) | 90-ASSO | **Oui** : 7541110 est libellé « Dons T21 France – Internet » (libellé de la Fédération) ; confirmer le compte de dons en ligne de l'association |
| Remise de chèques | ASS | BQASS | **7562100** (adhésions) + **7541200** (don de M. Faure) | 90-ASSO | **Oui** : 7562100 s'appelle « Cotisations **fédérales** » ; il sert sans doute aux cotisations que les associations versent à la Fédération (ou qu'elle reçoit). Pour les adhésions de **nos** adhérents, demander le compte à utiliser (une subdivision de 756 « Cotisations ») |
| Département | SAV | BQSAV | **7312170** *(fictif)* | 20-SAVS | **Oui** : vérifier dans le plan de l'association la subdivision de 7312 propre au SAVS |
| Indemnité d'assurance | SAV | BQSAV | **7587000** Indemnités d'assurance | 20-SAVS | Non |
| OPCO | EMP | BQEMP | **7584100** Remboursements sur frais de formation | 30-EMPLOI | Non |

> 💡 Réflexe senior : quand le compte « parfait » n'existe pas, on ne prend pas le compte dont le **nom** ressemble (7410002 Fondation **de France** pour la Fondation **Lumen** : faux, et le financeur ne s'y retrouverait pas). On saisit dans le compte **générique** le plus juste (7488000), avec un libellé précis, et on **demande la création** du bon compte. On reclasse ensuite en une OD.

**Les trois pièges de la partie B :**

- **Les dons en ligne au net** (1 236,40) : faux. Les dons sont de 1 280,00 € (c'est le montant des reçus fiscaux des donateurs) ; la commission de 43,60 € est une **charge**. Enregistrer au net fausse les dons et rend les reçus fiscaux incohérents avec la comptabilité.
- **Le chèque mixte de M. Faure** : 30,00 € d'adhésion + 50,00 € de **don**. Les deux n'ont pas le même compte, ni le même traitement fiscal (le don ouvre droit à un reçu). D'où 405,00 € d'adhésions (11 × 30,00 + 45,00 + 30,00) et 50,00 € de don.
- **La dotation du SAVS** : 640 000,00 / 12 = 53 333,33 € ; le douzième est arrondi au centime, le dernier versement de l'année rattrape l'arrondi (53 333,37 € en décembre). Rien à régulariser.

### Question 9 — Pourquoi pas en diminution des charges ?

- Depuis le règlement ANC n° 2022-06, les **comptes de transfert de charges** (79) sont supprimés. Les remboursements se comptabilisent « en diminution de la charge concernée **ou** en produit par nature, selon le cas ».
- Le **plan T21** a tranché pour chaque cas : il prévoit **7587000 Indemnités d'assurance** et **7584100 Remboursements sur frais de formation** (*« ancien compte 6498000 »* : ce remboursement était autrefois une charge négative, il est désormais un produit). En revanche, il garde les IJSS et la prévoyance en **charges négatives** (6419000, 6419100), comme le dit aussi le document « Les journaux comptables ».
- La règle pratique de l'agent comptable : **appliquer le plan de l'association, compte par compte**, et ne pas « améliorer » de sa propre initiative. Créditer 6155800 ferait disparaître le coût réel de la réparation (1 334,00 €) et la franchise (150,00 €) restée à charge, que l'on veut pouvoir suivre.

### Question 10 — La subvention de la Fondation Lumen à la clôture

1. **Fonds dédiés** : la subvention est **affectée** au projet « Pairs et voix ». Si, au 31/12/2026, une partie des 31 200,00 € de 2026 n'a pas été dépensée pour le projet, cette partie est reportée en **fonds dédiés** (6892200 Report en fonds dédiés à l'exploitation / **1940000** Fonds dédiés sur subventions d'exploitation), puis reprise en 2027 au fur et à mesure des dépenses (7892200).
2. **Produit à recevoir** : la seconde tranche (15 600,00 €) n'est pas encaissée. Si la convention la rend **acquise** pour 2026 (par exemple à la remise d'un rapport intermédiaire déjà remis), elle est constatée en produit à recevoir (**4417000** Subventions d'exploitation, ou 4676000 selon l'usage de l'association). Sinon, rien. C'est la convention qui décide, pas l'encaissement.
3. Et toujours : le **compte rendu financier** au financeur, construit à partir du code analytique 50-PAIRS.

## 2. Calculs (détaillés, chaque montant justifié)

| Calcul | Détail | Résultat |
|---|---|---|
| Total net EIG (pièce A1) | 2 400,00 + 1 800,00 + 360,00 + 450,00 − 300,00 | 4 710,00 |
| Produits nets dans le journal VT reçu | 6 810,00 − 300,00 | 6 510,00 |
| Écart | 6 510,00 − 4 710,00 | 1 800,00 (= doublon FA-2026-0413) |
| Journal VT corrigé (total des débits) | 2 400,00 + 1 800,00 + 360,00 + 450,00 + 300,00 | 5 310,00 |
| Encaissement Cap Avenir 59 | 2 400,00 − 300,00 | 2 100,00 |
| Dons en ligne | 1 280,00 − 43,60 | 1 236,40 (net viré) ✓ |
| Adhésions de la remise | 11 × 30,00 + 45,00 + 30,00 | 405,00 |
| Remise de chèques | 405,00 + 50,00 | 455,00 ✓ |
| Fondation Lumen, tranche 1 | 31 200,00 × 50 % | 15 600,00 ✓ |
| Douzième SAVS | 640 000,00 / 12 | 53 333,33 (décembre : 640 000,00 − 11 × 53 333,33 = 53 333,37) |
| Indemnité d'assurance | 1 334,00 − 150,00 | 1 184,00 ✓ |

## 3. Écritures comptables

### 3.1 Partie A — Journal VT de la Fédération tel qu'il doit être (question 3)

*Ces écritures ne sont pas tapées : c'est ce que le redéversement d'EIG doit produire. La Fédération n'est pas découpée en structures dans cet exercice : pas de code analytique.*

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| VT | 02/11 | 4110000 Clients | CLCAPAVENIR59 | Cap Avenir 59 – formation inclusion scolaire – FA-2026-0412 |  | 2 400,00 |  |
| VT | 02/11 | 7060004 Prestations de FORMATION |  | Cap Avenir 59 – formation inclusion scolaire – FA-2026-0412 |  |  | 2 400,00 |
| VT | 03/11 | 4110000 Clients | CLHORIZONS44 | Horizons 44 – abonnement annuel OGIRYS 2027 – FA-2026-0413 |  | 1 800,00 |  |
| VT | 03/11 | 7060002 Abonnement annuel OGIRYS |  | Horizons 44 – abonnement annuel OGIRYS 2027 – FA-2026-0413 |  |  | 1 800,00 |
| VT | 05/11 | 4110000 Clients | CLIMETILLEULS | IME Les Tilleuls – frais pédagogiques – FA-2026-0414 |  | 360,00 |  |
| VT | 05/11 | 7085200 Frais pédagogiques de formation |  | IME Les Tilleuls – frais pédagogiques – FA-2026-0414 |  |  | 360,00 |
| VT | 06/11 | 4110000 Clients | CLCAPHORIZONS21 | Cap Horizons 21 – inscription journées fédérales x3 – FA-2026-0415 |  | 450,00 |  |
| VT | 06/11 | 7085300 Inscription événements |  | Cap Horizons 21 – inscription journées fédérales x3 – FA-2026-0415 |  |  | 450,00 |
| VT | 09/11 | 7060004 Prestations de FORMATION |  | Cap Avenir 59 – avoir 1 stagiaire absent – AV-2026-0031 |  | 300,00 |  |
| VT | 09/11 | 4110000 Clients | CLCAPAVENIR59 | Cap Avenir 59 – avoir 1 stagiaire absent – AV-2026-0031 |  |  | 300,00 |
| | | | | | **Total** | **5 310,00** | **5 310,00** |
Contrôle : produits nets = 2 400,00 + 1 800,00 + 360,00 + 450,00 − 300,00 = 4 710,00 = total EIG ✓. Cinq pièces, cinq écritures ✓. Chaque ligne 4110000 porte un tiers CL ✓.

### 3.2 Partie A — Solution de repli si EIG ne permet plus d'annuler (question 4)

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 13/11 | 7060002 Abonnement annuel OGIRYS |  | Annulation doublon FA-2026-0413 (lot EIG n° 2611-02) |  | 1 800,00 |  |
| OD | 13/11 | 4110000 Clients | CLHORIZONS44 | Annulation doublon FA-2026-0413 (lot EIG n° 2611-02) |  |  | 1 800,00 |
| OD | 13/11 | 7060004 Prestations de FORMATION |  | Reclassement FA-2026-0414 – article mal paramétré dans EIG |  | 360,00 |  |
| OD | 13/11 | 7085200 Frais pédagogiques de formation |  | Reclassement FA-2026-0414 – article mal paramétré dans EIG |  |  | 360,00 |
| | | | | | **Total** | **2 160,00** | **2 160,00** |
*Le client manquant de FA-2026-0415 ne peut pas être corrigé par OD (voir question 4) : correction dans EIG uniquement.*

### 3.3 Partie A — Encaissements de la Fédération (question 5)

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| BQFED | 12/11 | 4110000 Clients | CLCAPAVENIR59 | Cap Avenir 59 – VIR – FA-2026-0412 moins AV-2026-0031 *(tapé)* |  |  | 2 100,00 |
| BQFED | 12/11 | 5121000 Banque Fédération *(n° hypothétique)* |  | Cap Avenir 59 – VIR – FA-2026-0412 moins AV-2026-0031 *(auto)* |  | 2 100,00 |  |
| BQFED | 13/11 | 4110000 Clients | CLHORIZONS44 | Horizons 44 – VIR – FA-2026-0413 *(tapé)* |  |  | 1 800,00 |
| BQFED | 13/11 | 5121000 Banque Fédération *(n° hypothétique)* |  | Horizons 44 – VIR – FA-2026-0413 *(auto)* |  | 1 800,00 |  |
| BQFED | 13/11 | 4110000 Clients | CLCAPHORIZONS21 | Cap Horizons 21 – VIR – FA-2026-0415 *(tapé)* |  |  | 450,00 |
| BQFED | 13/11 | 5121000 Banque Fédération *(n° hypothétique)* |  | Cap Horizons 21 – VIR – FA-2026-0415 *(auto)* |  | 450,00 |  |
| | | | | | **Total** | **4 350,00** | **4 350,00** |
**Lettrage après correction du journal VT**

*Compte CLCAPAVENIR59*

| Date | Journal | Pièce | Débit | Crédit | Lettre |
|---|---|---|---|---|---|
| 02/11/2026 | VT | FA-2026-0412 | 2 400,00 | | A |
| 09/11/2026 | VT | AV-2026-0031 | | 300,00 | A |
| 12/11/2026 | BQFED | Virement | | 2 100,00 | A |

Groupe A : 2 400,00 au débit = 300,00 + 2 100,00 au crédit ✓. Compte soldé.

*Compte CLHORIZONS44*

| Date | Journal | Pièce | Débit | Crédit | Lettre |
|---|---|---|---|---|---|
| 03/11/2026 | VT | FA-2026-0413 | 1 800,00 | | A |
| 13/11/2026 | BQFED | Virement | | 1 800,00 | A |

**Sans la correction**, le compte aurait montré une deuxième ligne FA-2026-0413 de 1 800,00 € au débit, **non lettrée** : un client qui « doit encore » une facture qu'il a payée, avec **le même numéro**. Deux factures portant le même numéro, c'est impossible (la numérotation des factures est unique et continue) : le lettrage est donc un deuxième filet de sécurité, au plus tard à la première relance… qu'il ne faut surtout pas envoyer.

*Compte CLCAPHORIZONS21* : après redéversement, FA-2026-0415 (450,00 au débit) et le virement du 13/11 (450,00 au crédit) sont lettrés. Tant que la fiche client n'est pas corrigée, le virement ne peut être lettré avec rien : c'est pour cela qu'on corrige **avant** de saisir l'encaissement.

*Compte CLIMETILLEULS* : 360,00 non lettré, normal (facture du 05/11, pas encore payée).

### 3.4 Partie B — Recettes de Cap Horizons 21 (question 8)

*Chaque journal de banque a son compte : BQASS → 5125000, BQSAV → 5123000, BQEMP → 5124000. Quand une pièce a deux lignes tapées, le logiciel génère (selon le paramétrage) une seule ligne de banque pour le **net**, qui correspond au relevé.*

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| BQASS | 05/11 | 7488000 Autres subventions et participations |  | Fondation Lumen – Pairs et voix – tranche 1/2 2026 – conv. FL-2025-031 *(tapé)* | 50-PAIRS |  | 15 600,00 |
| BQASS | 05/11 | 5125000 Banque CM Association |  | Fondation Lumen – Pairs et voix – tranche 1/2 *(auto)* |  | 15 600,00 |  |
| BQASS | 06/11 | 7541110 Dons T21 France – Internet |  | Plateforme dons en ligne – 23 dons bruts – reversement 10/2026 *(tapé)* | 90-ASSO |  | 1 280,00 |
| BQASS | 06/11 | 6270000 Services bancaires et assimilés |  | Plateforme dons en ligne – commission – reversement 10/2026 *(tapé)* | 90-ASSO | 43,60 |  |
| BQASS | 06/11 | 5125000 Banque CM Association |  | Plateforme dons en ligne – reversement net 10/2026 *(auto)* |  | 1 236,40 |  |
| BQASS | 09/11 | 7562100 Cotisations fédérales *(provisoire, à valider)* |  | Adhésions 2026 – 13 chèques – remise n° 0000187 *(tapé)* | 90-ASSO |  | 405,00 |
| BQASS | 09/11 | 7541200 Dons Autres projets |  | Don M. Faure (chèque mixte 80 € : 30 adhésion + 50 don) – remise 0000187 *(tapé)* | 90-ASSO |  | 50,00 |
| BQASS | 09/11 | 5125000 Banque CM Association |  | Remise de chèques n° 0000187 *(auto)* |  | 455,00 |  |
| BQSAV | 10/11 | 7312170 Dotation SAVS *(n° fictif, à vérifier)* |  | Département Drôme – dotation globale SAVS – douzième 11/2026 *(tapé)* | 20-SAVS |  | 53 333,33 |
| BQSAV | 10/11 | 5123000 Banque CM SAVS |  | Département Drôme – dotation SAVS 11/2026 *(auto)* |  | 53 333,33 |  |
| BQSAV | 12/11 | 7587000 Indemnités d'assurance |  | Mutuelle d'assurance – indemnité sinistre 2026-S-0457 – Clio SAVS *(tapé)* | 20-SAVS |  | 1 184,00 |
| BQSAV | 12/11 | 5123000 Banque CM SAVS |  | Mutuelle d'assurance – sinistre 2026-S-0457 *(auto)* |  | 1 184,00 |  |
| BQEMP | 13/11 | 7584100 Remboursements sur frais de formation |  | OPCO – prise en charge formation – dossier 26-118 – J. Marchetti *(tapé)* | 30-EMPLOI |  | 1 680,00 |
| BQEMP | 13/11 | 5124000 Banque CM Emploi |  | OPCO – dossier 26-118 *(auto)* |  | 1 680,00 |  |
| | | | | | **Total** | **73 532,33** | **73 532,33** |
Contrôle par relevé : ASS 15 600,00 + 1 236,40 + 455,00 = 17 291,40 ; SAV 53 333,33 + 1 184,00 = 54 517,33 ; EMP 1 680,00 ✓.

## 4. Points d'attention / pièges

- **Retaper une facture de vente** à la Fédération, ou « corriger » le journal VT à la main.
- **Croire qu'un journal équilibré est juste** : les trois anomalies laissent le journal parfaitement équilibré.
- **Se contenter du contrôle global** : il trouve le doublon (écart de 1 800,00), mais **pas** l'erreur de compte (total inchangé) ni le client manquant (total inchangé). Il faut les trois contrôles : nombre, total, ventilation.
- **Confondre les deux associations** : la Fédération et Cap Horizons 21 ont chacune leur comptabilité. Chez Cap Horizons 21, la facture FA-2026-0415 est un **achat** (journal AC, compte de charge 6256700 « Missions – Journées Fédérales », tiers FO de la Fédération), réparti selon les structures des trois participants.
- **Prendre 7410002 Fondation de France** pour la Fondation Lumen parce que le mot « fondation » y figure.
- **Dons au net** de la commission ; **chèque mixte** adhésion + don passé en entier en adhésions.
- **Créditer un compte de charge** (6155800, compte de formation) avec l'indemnité d'assurance ou le remboursement OPCO, alors que le plan T21 prévoit des comptes de produits.
- **Oublier l'analytique** sur les produits : c'est elle qui permettra de faire le compte rendu du projet « Pairs et voix » et le compte administratif du SAVS.

## 5. Ce qu'un senior ferait en plus

**Contrôle du journal automatique, en routine :**

- Une **fiche de contrôle hebdomadaire** du déversement, signée : nombre de pièces EIG / nombre de pièces VT, total EIG / total des 70 nets, liste des lignes 411 sans tiers (filtre « tiers vide »), contrôle compte par article. Cinq minutes par semaine, et le CAC adore ce genre de piste d'audit.
- **Balance auxiliaire clients = compte 4110000** de la balance générale, chaque fin de mois. Un écart signale presque toujours une ligne sans tiers.
- **Chercher la cause** du doublon avec l'informatique ou l'éditeur : un lot relancé deux fois peut se reproduire sur la paie (EIG RH) ou les immobilisations (EIG IMMOS), qui sont aussi des journaux automatiques.

**Chez Cap Horizons 21 :**

- Tenir une **liste des comptes à créer ou à valider** (Fondation Lumen, dons en ligne, adhésions, dotation SAVS) et la soumettre en une fois à la directrice et à l'expert-comptable, plutôt que dix mails. Une fois les comptes créés : une OD de reclassement, datée, documentée.
- **Reçus fiscaux** : rapprocher chaque mois la liste des dons encaissés (en ligne, chèques, virements) du registre des reçus émis. Le total des reçus 2026 doit être égal au total des comptes de dons 2026, au centime près, ou l'écart doit être expliqué.
- **Adhésions** : rapprocher la remise de chèques du **fichier des adhérents** (qui a payé ? combien ? pour quelle année ?). Une adhésion 2027 payée en décembre 2026 se traite en produit constaté d'avance.
- **Dotation SAVS** : tenir un tableau des douzièmes reçus par mois ; un douzième manquant ou modifié (arrêté de tarification rectificatif) doit se voir le jour même.
- **Sinistre** : classer ensemble la déclaration, la facture du garage et la lettre d'indemnisation ; vérifier que la franchise (150,00 €) correspond au contrat d'assurance.

## 6. Références

- Documents internes T21 France (30/04/2026) : « Les journaux comptables » (journal des ventes automatique, réservé à la Fédération, aucune écriture manuelle ; comptes CL et 70 ; dotations en 731, dons en 754, subventions en 74) ; « La comptabilité » (4110000 compte de centralisation, saisie obligatoire dans les comptes CL ; comptes 48 de régularisation ; fonds dédiés en classe 19).
- Plan comptable T21 France (MAJ 13/10/2025) : 4110000, 4417000, 4870000, 1940000, 6270000, 6892200, 7060002, 7060004, 7085200, 7085300, 7312130, 7410002, 7488000, 7541110, 7541200, 7562100, 7584100, 7587000, 7892200.
- Règlement ANC n° 2022-06 : suppression des comptes de transfert de charges.
- Règlement ANC n° 2018-06 (comptes annuels des personnes morales de droit privé à but non lucratif) : fonds dédiés, subventions affectées, dons.
