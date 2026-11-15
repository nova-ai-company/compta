# E18-06 — Contrôler un journal des ventes automatique, puis saisir les recettes de Cap Horizons 21
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) — partie A : comptabilité de la Fédération (entité distincte) | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 15 | **Thèmes :** journal automatique (EIG Gestion commerciale), contrôle d'un déversement, comptes de tiers CL, avoir, encaissements clients, lettrage, dotation du Département, subvention d'une fondation, dons en ligne, adhésions, indemnité d'assurance, remboursement OPCO

**Corner case :** oui — le journal des ventes ne se corrige pas « à la main » ; le plan T21 n'a pas de compte pour les adhésions d'une association locale ; une fondation n'a pas encore de compte de subvention

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IME** | Institut médico-éducatif. Établissement qui accueille des enfants et adolescents avec une déficience intellectuelle. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **OGIRYS** | Abonnement facturé par la Fédération. Compte 7060002 « Abonnement annuel OGIRYS » : prestation vendue par la Fédération aux associations (nom d'outil interne). |
    | **OPCO** | Opérateur de compétences. Organisme qui finance la formation professionnelle des salariés de la branche. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SIREN** | Numéro d'identification de l'entreprise (9 chiffres). Identifiant unique de chaque entreprise en France. Mention obligatoire sur les factures, y compris celui du client depuis la facturation électronique. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **VIR** | Virement. Abréviation utilisée sur les relevés bancaires. |
    | **VT** | Journal des ventes. Journal où l'on enregistre les factures clients (et les Z de caisse). |
    | **Compte 4110000** | Clients (comptes de tiers CL…) (plan T21). Centralisation des clients. On saisit dans les comptes CL… |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5124000** | Banque de l'emploi accompagné (dossier M18, fictif). Compte bancaire de l'emploi accompagné, journal BQEMP. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 6155800** | Entretien et réparations des autres matériel et outillages (plan T21). Entretien et réparation des véhicules et du matériel. |
    | **Compte 7060002** | Abonnement annuel OGIRYS (plan T21). Abonnement annuel OGIRYS facturé (Fédération). |
    | **Compte 7060004** | Prestations de FORMATION (plan T21). Prestations de formation vendues (Fédération). |
    | **Compte 7085200** | Frais pédagogiques de formation (plan T21). Frais pédagogiques de formation facturés. |
    | **Compte 7085300** | Inscription événements (plan T21). Inscriptions à des événements. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7312170** | Dotation du SAVS (dossier M18, numéro fictif). Le plan T21 ne prévoit que 7312130 (services pour enfants). Pour le SAVS, une autre subdivision 7312xxx est nécessaire : à vérifier dans le plan de l'association. |
    | **Compte 7410002** | Subvention Fondation de France (plan T21). Subvention de la Fondation de France. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7562100** | Cotisations fédérales (plan T21). Cotisations fédérales (cotisations des associations membres à la Fédération). |
    | **FOGARAGEMARTIN** | Compte fournisseur Garage Martin (dossier M18). Garage de Valence : entretien et achat des véhicules. Regroupé dans 4010000. |
    | **FOMAAF** | Compte fournisseur assurances (dossier M18). Mutuelle d'assurance : multirisque, flotte automobile, responsabilité civile. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes, sociétés et documents fictifs. Les numéros de comptes viennent du plan comptable T21 France. Les factures de la Fédération sont inventées pour l'exercice.*

!!! abstract "En clair"
    Un journal **automatique** est rempli par un autre logiciel (ici EIG Gestion commerciale, qui fait les factures). Personne ne tape dedans. Le travail du comptable n'est donc **pas** de ressaisir les factures, mais de **vérifier** que ce qui est arrivé en comptabilité correspond exactement aux factures émises : même nombre, mêmes montants, bons comptes, bons clients. Si c'est faux, on corrige **à la source** (dans EIG), pas en bricolant le journal.

## La mise en situation

Lundi 16 novembre 2026. Dans le cadre de votre intégration, la directrice a organisé une demi-journée d'échange avec Sandrine Vidal, responsable comptable de la **Fédération Trisomie 21 France** *(personne fictive)*. Attention : la Fédération est une **autre association**, avec son propre SIREN, son propre conseil d'administration et sa **propre comptabilité**. Cap Horizons 21 en est **membre** ; elle n'est pas une de ses structures.

Le document T21 sur les journaux le dit : *« Chez Trisomie 21 France, seule la Fédération utilise ce journal [des ventes]. Les facturations sont établies depuis EIG Gestion commerciale qui déverse en automatique les écritures dans la comptabilité. Aucune écriture manuelle n'est à passer dans ce journal. »*

Sandrine Vidal vous tend deux listings :

> « Chaque semaine, je compare la liste des factures d'EIG avec le journal VT. Je ne retape jamais une facture. Cette semaine, quelque chose cloche : faites le contrôle comme si vous étiez à ma place. »

L'après-midi, de retour chez Cap Horizons 21, vous saisissez les **recettes** arrivées sur les comptes bancaires des structures.

## Les pièces

### Partie A — La Fédération (entité distincte)

**Pièce A1 — Liste des factures et avoirs émis dans EIG Gestion commerciale, du 01/11 au 13/11/2026**

| N° | Date | Client (code EIG) | Objet | Article EIG | Montant |
|---|---|---|---|---|---|
| FA-2026-0412 | 02/11/2026 | Association Cap Avenir 59 (CLCAPAVENIR59) | Formation « Accompagner l'inclusion scolaire », 2 jours, 8 stagiaires × 300,00 | FORMATION | 2 400,00 |
| FA-2026-0413 | 03/11/2026 | Association Horizons 44 (CLHORIZONS44) | Abonnement annuel au logiciel OGIRYS, **année 2027** | ABONNEMENT | 1 800,00 |
| FA-2026-0414 | 05/11/2026 | IME Les Tilleuls (CLIMETILLEULS) | Frais pédagogiques : kits et supports de la formation du 22/10 | FRAIS-PEDA | 360,00 |
| FA-2026-0415 | 06/11/2026 | Association Cap Horizons 21 (CLCAPHORIZONS21) | Inscription aux journées fédérales, 3 personnes × 150,00 | INSCRIPTION | 450,00 |
| AV-2026-0031 | 09/11/2026 | Association Cap Avenir 59 (CLCAPAVENIR59) | Avoir sur FA-2026-0412 : 1 stagiaire absent, signalé avant la formation | FORMATION | − 300,00 |
| | | | | **Total net** | **4 710,00** |

*Paramétrage des articles EIG (fiche « articles », extrait remis par Sandrine Vidal) : FORMATION → 7060004 ; ABONNEMENT → 7060002 ; FRAIS-PEDA → 7085200 ; INSCRIPTION → 7085300. Les activités facturées ne sont pas soumises à la TVA : le plan T21 ne comporte aucun compte 445 (hypothèse de l'exercice, à confirmer pour la Fédération).*

**Pièce A2 — Journal VT de la Fédération, tel qu'il apparaît dans la comptabilité au 13/11/2026**

| Lot EIG | Date | Pièce | Compte | Tiers | Débit | Crédit |
|---|---|---|---|---|---|---|
| 2611-01 | 02/11 | FA-2026-0412 | 4110000 | CLCAPAVENIR59 | 2 400,00 | |
| 2611-01 | 02/11 | FA-2026-0412 | 7060004 | | | 2 400,00 |
| 2611-01 | 03/11 | FA-2026-0413 | 4110000 | CLHORIZONS44 | 1 800,00 | |
| 2611-01 | 03/11 | FA-2026-0413 | 7060002 | | | 1 800,00 |
| 2611-02 | 03/11 | FA-2026-0413 | 4110000 | CLHORIZONS44 | 1 800,00 | |
| 2611-02 | 03/11 | FA-2026-0413 | 7060002 | | | 1 800,00 |
| 2611-02 | 05/11 | FA-2026-0414 | 4110000 | CLIMETILLEULS | 360,00 | |
| 2611-02 | 05/11 | FA-2026-0414 | 7060004 | | | 360,00 |
| 2611-02 | 06/11 | FA-2026-0415 | 4110000 | *(vide)* | 450,00 | |
| 2611-02 | 06/11 | FA-2026-0415 | 7085300 | | | 450,00 |
| 2611-03 | 09/11 | AV-2026-0031 | 7060004 | | 300,00 | |
| 2611-03 | 09/11 | AV-2026-0031 | 4110000 | CLCAPAVENIR59 | | 300,00 |
| | | | | **Total** | **7 110,00** | **7 110,00** |

*Le journal est équilibré. Sandrine Vidal : « Un journal équilibré n'est pas un journal juste. »*

**Pièce A3 — Relevé bancaire de la Fédération (extrait), journal BQFED (code hypothétique)**

| Date | Libellé banque | Crédit |
|---|---|---|
| 12/11/2026 | VIR ASSOCIATION CAP AVENIR 59 – FA-2026-0412 AV-2026-0031 | 2 100,00 |
| 13/11/2026 | VIR HORIZONS 44 – FACTURE 0413 | 1 800,00 |
| 13/11/2026 | VIR CAP HORIZONS 21 – JOURNEES FEDERALES FA-2026-0415 | 450,00 |

### Partie B — Cap Horizons 21 : les recettes arrivées en banque

**Pièce B1 — Extraits des relevés des comptes des structures, du 05/11 au 13/11/2026**

| Compte (structure) | Date | Libellé banque | Crédit |
|---|---|---|---|
| 5125000 (ASS) | 05/11 | VIR FONDATION LUMEN – CONV FL-2025-031 – PAIRS ET VOIX – TRANCHE 1/2 2026 | 15 600,00 |
| 5125000 (ASS) | 06/11 | VIR PLATEFORME DONS EN LIGNE – REVERSEMENT 10/2026 | 1 236,40 |
| 5125000 (ASS) | 09/11 | REMISE CHEQUES N° 0000187 – 13 CHEQUES | 455,00 |
| 5123000 (SAV) | 10/11 | VIR DEPARTEMENT DE LA DROME – DOTATION SAVS 11/2026 | 53 333,33 |
| 5123000 (SAV) | 12/11 | VIR MUTUELLE ASSURANCE – INDEMNITE SINISTRE 2026-S-0457 | 1 184,00 |
| 5124000 (EMP) | 13/11 | VIR OPCO – PEC FORMATION DOSSIER 26-118 | 1 680,00 |

**Pièce B2 — Les justificatifs (résumés)**

- **Fondation Lumen** *(fictive)* : convention FL-2025-031 du projet « Pairs et voix » (code analytique 50-PAIRS), subvention **affectée** de 31 200,00 € pour 2026, versée en deux tranches de 50 %. Le plan comptable T21 ne contient **aucun** compte au nom de la Fondation Lumen. Il contient 7410002 « Subvention Fondation de France » et 7488000 « Autres subventions et participations ».
- **Plateforme de dons en ligne** : récapitulatif d'octobre : 23 dons, total **brut 1 280,00 €**, commission de la plateforme **43,60 €**, versement net 1 236,40 €. La liste nominative des donateurs est jointe (reçus fiscaux à émettre).
- **Remise de chèques n° 0000187** : 11 adhésions individuelles 2026 à 30,00 €, 1 adhésion « famille » à 45,00 €, et un chèque de **80,00 €** de M. Faure accompagné d'un mot : « 30 € pour mon adhésion, le reste en don ». Le plan T21 ne contient qu'un compte de cotisations : **7562100 « Cotisations fédérales »**.
- **Département de la Drôme** : arrêté de tarification du SAVS 2026, dotation globale de 640 000,00 €, versée par douzièmes. Le plan T21 ne liste que **7312130** (services du 2° du I de l'article L. 312-1 du CASF, enfants) ; la fiche du dossier prévoit **7312170** *(numéro fictif)* pour le SAVS.
- **Mutuelle d'assurance (FOMAAF)** : lettre d'indemnisation du sinistre 2026-S-0457 (accrochage de la Clio du SAVS le 02/10) : réparation 1 334,00 € (facture FOGARAGEMARTIN déjà saisie au SAVS), franchise 150,00 €, indemnité 1 184,00 €.
- **OPCO** : accord de prise en charge de la formation « Job coaching » suivie par Julie Marchetti (emploi accompagné), coût payé par la structure EMP en septembre ; prise en charge 1 680,00 €.

## Travail à faire

**Partie A — Fédération**

1. Expliquez pourquoi, à la Fédération, le comptable ne **saisit** pas les factures de vente, et ce qu'il fait à la place.
2. Comparez la pièce A1 et la pièce A2, ligne par ligne. Trouvez **les trois anomalies** du déversement. Pour chacune, dites comment un senior la **repère**, ce qu'elle provoque si on ne la voit pas, et comment on la **corrige**.
3. Présentez le journal VT **tel qu'il doit être** après correction.
4. Si la période est verrouillée et qu'EIG ne permet plus d'annuler un lot, quelle solution de repli ? Présentez les écritures correspondantes et dites quelle anomalie **ne peut pas** se corriger par une OD.
5. Saisissez les trois encaissements de la pièce A3 dans le journal BQFED (ligne tapée + ligne de banque automatique) et **lettrez** les comptes CLCAPAVENIR59 et CLHORIZONS44. Que vous aurait montré le lettrage de CLHORIZONS44 si personne n'avait vu le doublon ?
6. La facture FA-2026-0413 porte sur l'année 2027. Qu'est-ce que cela implique à la clôture du 31/12/2026 ?

**Partie B — Cap Horizons 21**

7. Pour chaque ligne de la pièce B1, indiquez la **structure**, le **journal**, le **compte** et le **code analytique**. Signalez les comptes qui doivent être **validés** avant la saisie, et la question que vous posez.
8. Passez les écritures (ligne tapée + ligne de banque automatique).
9. Pourquoi l'indemnité d'assurance et le remboursement de l'OPCO ne viennent-ils pas en **diminution** des charges (crédit du compte 6155800 ou du compte de formation), alors que les IJSS vont au crédit d'un compte 64 ?
10. Citez deux conséquences, à la clôture de 2026, de la subvention de la Fondation Lumen.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-06_corrige.md)
