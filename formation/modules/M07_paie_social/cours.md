# M07 — Paie, social et rémunération des dirigeants

> **Objectif du module.** À la fin de ce module, vous savez lire n'importe quel bulletin de paie, passer et contrôler les écritures de paie à partir d'un journal de paie, rapprocher la paie de la DSN et des comptes 43x, traiter les cas qui « cassent » la paie standard (absences, congés payés, ruptures, avantages en nature, saisonniers), et — surtout — conseiller le client sur la **rémunération de ses dirigeants** (assimilé salarié ou TNS, rémunération ou dividendes, participation et épargne salariale).
>
> **Avertissement permanent.** Les taux, plafonds et seuils sociaux changent au 1er janvier (parfois en cours d'année). Dans ce module, les valeurs chiffrées sont **toujours données dans les énoncés** avec la mention *« valeur à vérifier chaque année »*. Ne mémorisez pas les taux : mémorisez les **mécanismes** et **où vérifier** (site de l'URSSAF, de l'AGIRC-ARRCO, convention collective, *Bulletin officiel de la sécurité sociale* — BOSS).

!!! abstract "En clair — ce module en 5 idées"
    1. Un bulletin de paie se lit de haut en bas : on part du **brut**, on retire les cotisations du salarié, on obtient le **net**, puis on retire l'impôt prélevé à la source. Exemple : la fiche de paie d'un serveur de C04 Le Petit Zinc, le restaurant.
    2. Pour l'entreprise, la charge, c'est le **brut + les cotisations patronales**. Le net à payer n'est qu'une dette envers le salarié.
    3. Chaque mois, la paie, la déclaration sociale (DSN), la banque et la comptabilité doivent donner **les mêmes montants**. Votre travail, c'est de le vérifier.
    4. Certaines situations changent la paie : maladie, congés payés, heures supplémentaires, repas fournis, fin de contrat. À la clôture, les congés acquis et non pris deviennent une **dette** à enregistrer.
    5. Le dirigeant n'a pas toujours le même statut : assimilé salarié (président de SAS) ou travailleur indépendant (gérant majoritaire de SARL). Exemple : le gérant de C01 Boulangerie Dupain n'est pas traité comme le président de C08 TechNova.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Salaire brut | Le salaire avant toute retenue ; c'est la charge de salaire de l'entreprise | 2 000 € brut |
    | Cotisations salariales | Part retenue sur le salaire du salarié pour la protection sociale | Retraite, maladie |
    | Cotisations patronales | Part payée en plus par l'employeur ; elle ne touche pas le net du salarié | Environ 25 à 45 % du brut selon le cas |
    | Net à payer | Ce que le salarié reçoit vraiment sur son compte | Virement de fin de mois |
    | Net imposable | Le montant qui sert à calculer l'impôt sur le revenu du salarié | Base du prélèvement à la source |
    | PAS (prélèvement à la source) | Impôt sur le revenu retenu sur la paie et reversé à l'État | Taux personnel transmis par l'administration fiscale |
    | Journal de paie | Récapitulatif mensuel de tous les bulletins, qui sert à passer l'écriture | Édité par le logiciel de paie |
    | DSN | Déclaration mensuelle envoyée aux organismes sociaux à partir de la paie | Envoyée le 5 ou le 15 du mois suivant |
    | Avantage en nature (AN) | Quelque chose fourni au salarié à la place d'argent | Repas, logement, voiture |
    | IJSS | Indemnités versées par la Sécurité sociale pendant un arrêt maladie | Salarié malade 10 jours |
    | Subrogation | L'employeur garde le salaire normal et touche lui-même les IJSS | Maintien de salaire en arrêt |
    | Congés payés (CP) | Jours de vacances acquis en travaillant, payés par l'employeur | 2,5 jours par mois |
    | Assimilé salarié | Dirigeant traité comme un salarié pour les cotisations | Président de SAS |
    | TNS | Travailleur non salarié (indépendant) : il cotise à part, sur son revenu | Gérant majoritaire de SARL |
    | Participation | Part des bénéfices reversée aux salariés, obligatoire dès 50 salariés | C18 Imprimerie Graphique Rhône |

---

## 1. Lire un bulletin de paie : la « cascade »

> 🟢 **En clair :** un bulletin part du brut et descend jusqu'au montant viré au salarié. Si vous connaissez cet ordre, vous savez contrôler n'importe quelle fiche de paie. C'est la base de toute révision sociale.

Un bulletin se lit de haut en bas comme une cascade. Retenez cet ordre, il structure tous les contrôles.

| Étape | Contenu | Remarque de praticienne |
|---|---|---|
| **Salaire de base** | Horaire contractuel × taux horaire (ou forfait mensuel) | 35 h hebdo = **151,67 h** mensualisées (35 × 52 / 12). |
| + éléments variables | Heures supplémentaires, primes, majorations (nuit, dimanche), **avantages en nature** | Les AN s'ajoutent au brut (pour cotiser) puis se **retirent** du net (ils ont été « perçus » en nature). |
| − absences | Absences non rémunérées, maladie (puis maintien éventuel) | Méthode de retenue : heures réelles ou jours ouvrés/ouvrables du mois (jurisprudence : la retenue ne doit pas dépasser la valeur réelle des heures). |
| **= Salaire brut** | Base des cotisations (sauf exceptions : plafonnement, abattement CSG) | C'est le brut qui va au **débit du 641**. |
| − cotisations salariales | Sécurité sociale, retraite complémentaire, prévoyance/mutuelle (part salariale), CSG/CRDS | La part salariale est une **retenue** sur le brut : elle va au **crédit des 43x**, pas en charge. |
| = **Net à payer avant impôt** | | Le « net social » (montant net social, obligatoire sur le bulletin depuis 2024) sert aux prestations (prime d'activité, RSA). |
| **Net imposable** | Brut − cotisations salariales **déductibles** (dont CSG déductible) + part patronale de complémentaire santé + CSG/CRDS non déductibles réintégrées | Sert d'assiette au **prélèvement à la source (PAS)**. Les heures supplémentaires exonérées d'IR (dans la limite annuelle) en sont **exclues**. |
| − PAS | Net imposable × taux transmis par la DGFiP (via le compte rendu métier DSN) | Collecté pour l'État → **compte 4421**. |
| − acomptes, oppositions | Acompte versé en cours de mois (425), saisie sur rémunération (427) | |
| + remboursements de frais | Transport (prise en charge 50 % abonnement), frais professionnels | Pas des salaires : ne cotisent pas (dans les limites). |
| = **Net payé** | Ce qui part en virement → crédit 421 soldé par 512 | |

Les **cotisations patronales** figurent sur le bulletin à titre informatif : elles ne touchent pas le net mais constituent une **charge** (645x) et une **dette** (43x).

> 💡 **Réflexe senior :** pour contrôler un bulletin en 2 minutes, faites trois ratios : cotisations salariales / brut (≈ 21–23 % pour un non-cadre sous le plafond), net à payer avant impôt / brut (≈ 77–79 %), coût total employeur / brut (≈ 1,25 à 1,45 selon la réduction générale). Tout écart notable doit avoir une explication (HS exonérées, apprenti, temps partiel, AN, absence).

> ⚠️ **Erreur classique :** passer le **net à payer** en charge. La charge, c'est le **brut** (641) + les **cotisations patronales** (645). Le net n'est qu'une dette envers le salarié (421).

---

## 2. Les écritures de paie

> 🟢 **En clair :** chaque mois, on passe une seule écriture à partir du journal de paie. Les charges vont en 64x, les dettes envers le salarié, l'URSSAF, les caisses et l'État vont en 42x, 43x et 4421. Ensuite, vous vérifiez que tout concorde avec la DSN et la banque.

### 2.1 Les comptes à connaître

| Compte | Intitulé | Usage |
|---|---|---|
| 6411 | Salaires, appointements | Brut (hors congés payés, primes et indemnités si on les sépare) |
| 6412 | Congés payés | Indemnités de CP versées / dotation à la dette provisionnée (sens selon l'option du dossier) |
| 6413 | Primes et gratifications | |
| 6414 | Indemnités et avantages divers | Indemnités de rupture, AN (si on les isole), indemnité de précarité… |
| 644 | Rémunération du travail de l'exploitant | Rémunération du gérant majoritaire TNS (pratique courante en société) |
| 6451 | Cotisations à l'URSSAF | |
| 6452 | Cotisations aux mutuelles | |
| 6453 | Cotisations aux caisses de retraite | |
| 6454 | Cotisations à France Travail (ex-Pôle emploi) | Souvent regroupé en 6451 depuis le recouvrement par l'URSSAF |
| 6458 | Cotisations aux autres organismes sociaux | Prévoyance, caisse de CP BTP… |
| 646 | Cotisations sociales personnelles de l'exploitant | Cotisations SSI du TNS |
| 647x | Autres charges sociales | 6475 médecine du travail, œuvres sociales… |
| 421 | Personnel – rémunérations dues | Net à payer |
| 425 | Personnel – avances et acomptes | |
| 427 | Personnel – oppositions | Saisies sur rémunération, pensions alimentaires (paiement direct) |
| 428x | Personnel – charges à payer | **4282** dettes provisionnées pour congés à payer, 4286 autres charges à payer |
| 431 | Sécurité sociale (URSSAF) | |
| 437 | Autres organismes sociaux | Retraite complémentaire, prévoyance, mutuelle (subdivisez : 4371, 4372…) |
| 438x | Organismes sociaux – charges à payer / produits à recevoir | **4382** charges sociales sur congés à payer, 4386 autres charges à payer, 4387 produits à recevoir |
| **4421** | État – prélèvements à la source (impôt sur le revenu) | PAS retenu sur les salaires |
| 63x | Impôts sur rémunérations | 6312 taxe d'apprentissage, 6313 formation professionnelle continue, 6333 participation formation |

> Selon l'organisation du dossier, la taxe d'apprentissage et la contribution à la formation, recouvrées mensuellement par l'URSSAF via la DSN, sont comptabilisées en 631x/633x (charges fiscales sur rémunérations) avec en contrepartie le compte 431 (organisme collecteur). Soyez **constante** d'un exercice à l'autre.

### 2.2 Schéma type (journal de paie mensuel)

| Compte | Débit | Crédit |
|---|---|---|
| 6411 Salaires (brut) | X | |
| 6451 / 6453 / 6452 / 6458 Charges patronales (nettes des réductions) | X | |
| 431 URSSAF (salariales + patronales URSSAF) | | X |
| 437x Retraite, mutuelle, prévoyance (salariales + patronales) | | X |
| 4421 PAS | | X |
| 425 Acomptes (remboursement de l'acompte versé) | | X |
| 427 Oppositions | | X |
| 421 Net à payer | | X |

Puis : règlement des salaires (421 / 512), versement des cotisations à l'échéance DSN (431, 437x, 4421 / 512).

> 💡 **Réflexe senior :** à chaque révision, le solde des comptes **421, 431, 437, 4421** à la clôture doit correspondre exactement à la paie du dernier mois (et aux échéances non encore payées). Un 431 qui « traîne » un solde ancien = cotisation non payée, majorations de retard à provisionner, ou erreur d'imputation à corriger.

### 2.3 Contrôle paie / comptabilité / DSN

La **DSN** (déclaration sociale nominative) est mensuelle et remplace la quasi-totalité des déclarations sociales. Échéances (à vérifier) : le **5 du mois M+1** pour les employeurs d'au moins 50 salariés, le **15 du mois M+1** pour les autres. Elle porte les cotisations URSSAF, retraite complémentaire, prévoyance/mutuelle, le PAS (reversé à la DGFiP par prélèvement le mois suivant) et les événements (arrêts, fins de contrat).

Contrôles à faire :
1. **Journal de paie ↔ comptabilité** : brut, charges, net, PAS identiques.
2. **Journal de paie ↔ DSN** : totaux par organisme, PAS, nombre de salariés.
3. **DSN ↔ banque** : prélèvements URSSAF, AGIRC-ARRCO, DGFiP-PAS.
4. **Annuel** : brut cumulé du journal = brut DSN annuel = 641 en comptabilité (tableau de concordance « salaires déclarés / salaires comptabilisés » — classique en contrôle URSSAF).

Une DSN déposée peut être **annulée et remplacée** jusqu'à la date d'échéance. Au-delà, l'erreur se corrige en **régularisation** dans une DSN ultérieure (bloc de régularisation de cotisations / rappel de salaire rattaché à la période d'origine).

---

## 3. Dispositifs qui modifient la paie

> 🟢 **En clair :** la paie « standard » est souvent modifiée : allègements de cotisations, heures supplémentaires, repas, maladie, congés, fin de contrat. Pour chacun, vous devez savoir ce qui change sur le bulletin et dans les comptes. Exemple : les repas fournis au personnel de C04 Le Petit Zinc.

### 3.1 Réduction générale des cotisations patronales
Allègement dégressif des cotisations patronales sur les rémunérations proches du SMIC. **Depuis le 1er janvier 2026, la réduction générale a été refondue** (réduction générale dite « dégressive unique », point de sortie relevé et paramètres modifiés — *à vérifier dans les textes en vigueur*). Le mécanisme reste : un **coefficient** fonction du rapport SMIC / rémunération, appliqué à la rémunération annuelle brute, calculé de façon annualisée et régularisé mois par mois. Il s'impute sur les cotisations URSSAF **et** sur les cotisations de retraite complémentaire.

> 🟢 **En clair :** plus un salaire est proche du SMIC, moins l'employeur paie de cotisations. Le logiciel de paie calcule cette réduction ; vous, vous vérifiez qu'elle est logique (forte au SMIC, nulle pour les hauts salaires).

En cabinet, on ne recalcule pas la réduction à la main : on **vérifie sa cohérence** (elle doit être maximale au SMIC, nulle au-delà du point de sortie, et absente pour les rémunérations qui n'y ouvrent pas droit) et on contrôle qu'elle a bien été **déclarée en DSN** (code type de personnel spécifique). Dans les exercices, son montant est **donné**.

### 3.2 Heures supplémentaires
- Majoration légale : 25 % de la 36e à la 43e heure, 50 % au-delà (sauf accord collectif, minimum 10 %).
- **Réduction de cotisations salariales** : égale au taux des cotisations d'assurance vieillesse salariales (base + complémentaire), dans la limite d'un plafond (11,31 % — *valeur à vérifier*).
- **Exonération d'impôt sur le revenu** dans la limite annuelle de 7 500 € nets (*à vérifier*) : les HS exonérées sortent du **net imposable** (donc pas de PAS dessus).
- **Déduction forfaitaire de cotisations patronales** par heure supplémentaire dans les petites entreprises (1,50 €/h pour moins de 20 salariés ; dispositif étendu selon l'effectif par les lois récentes — *vérifier montant et seuils en vigueur*).

### 3.3 Avantages en nature (AN)
Principe : l'AN est **ajouté au brut** (il cotise et entre dans le net imposable), puis **déduit du net** (il a été perçu en nature). Évaluation forfaitaire ou réelle.

| AN | Évaluation | Particularités |
|---|---|---|
| **Repas** (cas général) | Forfait URSSAF par repas (≈ 5,50 € — *à vérifier*) | Si le salarié paie une participation, l'AN est diminué d'autant. |
| **Repas HCR** (hôtels-cafés-restaurants) | 1 **minimum garanti** (MG) par repas (≈ 4,25 € — *à vérifier*) | La convention HCR impose de nourrir le personnel ou de verser une **indemnité compensatrice de nourriture** (soumise à cotisations). |
| **Logement** | Barème forfaitaire mensuel selon la **rémunération** et le **nombre de pièces**, ou valeur locative réelle | Option employeur. Abattement possible pour logement « nécessaire » à l'emploi dans certains cas. |
| **Véhicule** | Forfait (% du coût d'achat ou de location annuelle, majoré si carburant payé) ou réel | Abattement temporaire pour véhicules 100 % électriques (*à vérifier*). |
| **Outils NTIC** | Exonéré si usage privé raisonnable | |

### 3.4 Titres-restaurant
Contribution patronale **exonérée** si elle est comprise entre **50 % et 60 %** de la valeur du titre et ne dépasse pas une limite par titre (≈ 7,30 € — *à vérifier*). Comptabilisation : achat des titres (compte d'attente ou 6476/ 6478 « autres charges sociales »), la part salariale étant **retenue sur le net** (crédit d'un compte de tiers ou diminution de la charge). Côté **commerçant qui accepte** les titres (boulangerie, restaurant), le remboursement par l'émetteur se fait **sous déduction d'une commission** (charge 627 / 622) : il ne faut pas enregistrer le net en CA.

> 🟢 **En clair :** il y a deux situations. L'employeur qui **donne** des titres-restaurant paie une partie du titre (charge sociale) et retient l'autre sur le salaire. Le commerçant qui **reçoit** des titres en paiement, comme C01 Boulangerie Dupain, enregistre la vente au prix plein et la commission de l'émetteur en charge.

### 3.5 Pourboires
Les pourboires versés volontairement par les clients (y compris par carte bancaire) et reversés aux salariés en contact avec la clientèle bénéficient d'une **exonération de cotisations et d'impôt sur le revenu** pour les salariés dont la rémunération n'excède pas **1,6 SMIC**. Ce dispositif temporaire a été prorogé à plusieurs reprises : **vérifiez systématiquement sa date d'échéance** avant de l'appliquer. Comptablement : les pourboires collectés par CB sont une **dette envers les salariés** (compte de tiers 4286 ou 467 dédié), **jamais du chiffre d'affaires**, et ils ne sont pas soumis à TVA.

> 🟢 **En clair :** les pourboires appartiennent aux salariés. Quand un client de C04 Le Petit Zinc laisse un pourboire par carte, l'argent arrive sur le compte du restaurant, mais c'est une dette envers le personnel, pas une vente.

### 3.6 Absences maladie, IJSS et subrogation
- Le salarié malade perçoit des **indemnités journalières de sécurité sociale (IJSS)** après un délai de carence (3 jours en maladie ordinaire), et éventuellement un **complément employeur** (maintien de salaire légal après 1 an d'ancienneté et carence de 7 jours, ou conventionnel plus favorable).
- **Subrogation** : l'employeur maintient le salaire et **perçoit lui-même les IJSS** de la CPAM.
- **Comptablement depuis 2025 : le compte 791 « Transferts de charges » est supprimé.** Les IJSS perçues en subrogation viennent **en diminution de la charge de personnel** (compte 641, *subdivision selon la nomenclature 2025 du PCG*), avec en contrepartie un compte de tiers (4387 « Organismes sociaux – produits à recevoir », puis 512 à l'encaissement).
- Sur le bulletin : retenue pour absence, ajout du maintien (complément), et en cas de subrogation ajout des IJSS **brutes** (puis déduction en « IJSS nettes » versées par la CPAM à l'employeur) — les IJSS ne sont pas soumises aux cotisations sociales mais à la CSG/CRDS (6,2 % + 0,5 % — *à vérifier*), précomptée par la CPAM.

> ⚠️ **Erreur classique :** créditer 791 (n'existe plus) ou constater les IJSS en produit exceptionnel. Autre erreur : comptabiliser les IJSS à l'encaissement plusieurs mois après, alors que le salaire a été maintenu : à la clôture, les **IJSS à recevoir** doivent être constatées.

### 3.7 Congés payés (CP)
**Acquisition** : 2,5 jours ouvrables par mois de travail effectif (30 jours/an). **Depuis la loi n° 2024-364 du 22 avril 2024** :
- arrêt **maladie non professionnelle** : le salarié acquiert **2 jours ouvrables par mois**, dans la limite de **24 jours** par période de référence ;
- arrêt **AT/MP** : 2,5 jours par mois, **sans limite d'un an** ;
- un **report de 15 mois** s'applique aux CP non pris du fait de la maladie (l'employeur doit informer le salarié au retour) ;
- application **rétroactive** (avec des délais de forclusion) : un risque de rappels existe pour les dossiers anciens.

**Indemnisation** : la plus favorable entre la méthode du **1/10e** (10 % de la rémunération brute de la période de référence) et le **maintien de salaire**.

**Clôture : dette provisionnée pour congés à payer.** On constate à la clôture les droits acquis et non pris (y compris les jours « en cours d'acquisition »), valorisés au salaire de chaque salarié, **plus les charges sociales patronales** correspondantes :

| Compte | Débit | Crédit |
|---|---|---|
| 6412 Congés payés | Variation de la dette | |
| 4282 Dettes provisionnées pour congés à payer | | Dette CP à la clôture |
| 645x Charges sociales sur congés payés | Variation | |
| 4382 Charges sociales sur congés à payer | | Charges sociales sur la dette |

Deux méthodes : **extourne** de la dette N-1 au 1er jour de N et constatation de la nouvelle dette, ou **ajustement** de la variation. Le résultat est identique ; l'extourne est plus lisible.

> 💡 **Réflexe senior :** le taux de charges sociales appliqué à la dette CP doit être un **taux réel moyen** (net de la réduction générale), pas le taux « facial ». Pour une entreprise de salariés au SMIC, appliquer 45 % surévalue fortement la dette.

**BTP — caisse de congés payés** : dans le BTP (Bâtisseurs du Sud, C02), les CP sont versés par la **caisse de congés payés** à laquelle l'employeur cotise (cotisation ≈ 20 % des salaires — *taux propre à chaque caisse, à vérifier*). L'entreprise **ne paie pas** les CP et **ne provisionne pas de dette de CP** envers les salariés : sa charge est la cotisation à la caisse (6458 / 437x). Seules des cotisations dues non encore appelées sont à rattacher à l'exercice.

### 3.8 Contrats particuliers
- **Apprentis** : rémunération en % du SMIC selon âge et année ; exonérations de cotisations salariales **partielles** (seuil abaissé à 50 % du SMIC depuis 2025 — *à vérifier*) ; aide à l'embauche (subvention d'exploitation 74, dont le montant et les conditions changent souvent).
- **CDD d'usage** (HCR, spectacle, sondages…) : pas d'indemnité de précarité ; contribution patronale forfaitaire spécifique par contrat dans certains secteurs (*à vérifier*).
- **CDD saisonnier** : pas d'indemnité de fin de contrat (sauf convention), mais **indemnité compensatrice de CP** (10 %) à la fin du contrat.
- **CDD classique** : indemnité de fin de contrat de 10 % (6414 ou 6411).

### 3.9 Rupture du contrat
- **Rupture conventionnelle individuelle** : convention signée, délai de rétractation de **15 jours calendaires**, homologation par la DREETS (délai d'instruction de **15 jours ouvrables**, silence = homologation). Indemnité **au moins égale à l'indemnité légale de licenciement** : 1/4 de mois de salaire par année d'ancienneté jusqu'à 10 ans, 1/3 de mois au-delà (article R. 1234-2 du Code du travail), salaire de référence = le plus favorable entre la moyenne des 12 derniers mois et celle des 3 derniers mois (primes annuelles proratisées). Régime social : exonération de cotisations dans certaines limites (plafond exprimé en PASS) et **contribution patronale spécifique** sur la part exonérée (taux relevé à plusieurs reprises — *à vérifier*).
- **Solde de tout compte** : salaire du dernier mois, indemnité compensatrice de CP, indemnité de rupture, préavis éventuel ; remise du reçu, du certificat de travail et de l'attestation France Travail ; **DSN de fin de contrat** sous 5 jours.
- Clôture : si la rupture est **signée avant la clôture** et versée après, l'indemnité est une **charge à payer** (4286 / 4386) ; si elle n'est qu'envisagée, rien (au mieux une information) — sauf plan de licenciement décidé et annoncé (provision).

### 3.10 Charges sociales « annexes »
- **Mutuelle (frais de santé)** : obligatoire, part patronale ≥ 50 % ; la part patronale est soumise à CSG/CRDS, au forfait social de 8 % (≥ 11 salariés) et entre dans le net imposable.
- **Prévoyance** : obligatoire pour les cadres (1,50 % TA), souvent conventionnelle pour les non-cadres.
- **Médecine du travail** : cotisation au service de prévention et de santé au travail → 6475.
- **Formation professionnelle** : contribution 0,55 % (< 11 salariés) ou 1 % (≥ 11), + 1 % CPF-CDD sur les CDD — recouvrées par l'URSSAF.
- **Taxe d'apprentissage** : part principale recouvrée mensuellement, **solde** recouvré une fois par an (DSN d'avril/mai N+1) — pensez à la **charge à payer** du solde à la clôture.

---

## 4. Rémunération des dirigeants

> 🟢 **En clair :** le statut du dirigeant décide de tout : ses cotisations, le compte utilisé, et même si sa rémunération est une charge. Vérifiez toujours d'abord qui détient les parts et qui est gérant. Exemple : à C13 Atelier Ligne, deux cogérants à 50/50 sont ensemble majoritaires.

### 4.1 Tableau de synthèse

| Statut | Exemples du portefeuille | Régime social | Rémunération en compta | Cotisations en compta |
|---|---|---|---|---|
| **Président / DG de SAS** rémunéré | Bâtisseurs du Sud (C02), TechNova (C08), Hôtel Belle Vue (C16) | **Assimilé salarié** (régime général, sans assurance chômage) | 6411 (ou 6414 « mandataires ») | 645x |
| **Gérant minoritaire ou égalitaire de SARL** (seul gérant) | Menuiserie (C24, 5 %) | Assimilé salarié | 6411 | 645x |
| ⚠️ **Collège de gérance** : les parts des cogérants s'additionnent | Atelier Ligne (C13) : 2 cogérants à 50/50 = 100 % → **gérance majoritaire** | TNS (SSI) | 6411 / 644 | 646 |
| **Gérant majoritaire de SARL/SELARL** (> 50 %, parts du conjoint/partenaire de PACS et enfants mineurs comprises, et en cumulant les gérants si collège) | Boulangerie (C01), Pharmacie (C12), ImmoPlus (C22) | **TNS** — Sécurité sociale des indépendants (SSI, recouvrement URSSAF) | **644** (ou 6411 selon usage du cabinet — restez constante) | **646** |
| **EI / EURL à l'IR** | Style & Vous (C20), Dr Lambert (C05) | TNS | **Pas une charge** : prélèvements au **108** | **646** (déductibles, sauf CSG non déductible et CRDS) |
| **Président de SAS non rémunéré** | Studio Pixel (C25) | Aucune affiliation, aucune cotisation | — | — |

### 4.2 Le TNS : cotisations provisionnelles et régularisation
- L'année N, le TNS paie des **cotisations provisionnelles** calculées sur le revenu N-2 (puis N-1 dès qu'il est déclaré), avec possibilité de **modulation** sur la base d'un revenu estimé.
- En N+1, après la **déclaration de revenus professionnels** (déclaration unique avec la 2042), l'URSSAF **régularise** : complément à payer ou remboursement.
- Une **réforme de l'assiette** des cotisations des indépendants (assiette « brute » avec abattement forfaitaire, et non plus revenu net de cotisations) s'applique aux **revenus 2025 régularisés en 2026** — *paramètres à vérifier* ; dans les exercices, l'assiette est **donnée**.
- **À la clôture** : la régularisation à payer sur le revenu de l'exercice est une **charge à payer** (4386) ; un trop-versé est un **produit à recevoir** (diminution du 646, contrepartie 4387).

> ⚠️ **Erreur classique :** dans une EURL à l'IR, passer la « rémunération » de la gérante en 641 ou 644. Elle n'est **pas déductible** : c'est un prélèvement sur le résultat (108 « Compte de l'exploitant »). Seules les cotisations sociales obligatoires sont en charges (646).

### 4.3 Dividendes et TNS : la fraction > 10 %
Pour le gérant majoritaire de SARL / SELARL (et l'EI à l'IS, l'EURL à l'IS dont l'associé unique est gérant), la part des dividendes perçus par lui, son conjoint/partenaire et ses enfants mineurs **qui excède 10 % du capital social, des primes d'émission et des sommes versées en compte courant d'associé** (montant moyen) est soumise aux **cotisations sociales TNS** (article L. 131-6 du Code de la sécurité sociale) et non aux prélèvements sociaux sur revenus du capital. La fraction ≤ 10 % suit le régime des revenus de capitaux mobiliers (prélèvement forfaitaire non libératoire d'IR + prélèvements sociaux retenus à la source par la société).

> 🟢 **En clair :** un gérant majoritaire ne peut pas se verser librement des dividendes pour éviter les cotisations. La part des dividendes qui dépasse 10 % de ce qu'il a apporté à la société (capital, primes, compte courant) est soumise aux cotisations, comme un revenu d'activité.

> 💡 **Réflexe senior :** l'arbitrage rémunération / dividendes d'un gérant majoritaire se fait **en intégrant** la règle des 10 % : au-delà, le dividende « coûte » des cotisations sociales tout en n'étant pas déductible de l'IS. Faites toujours une simulation chiffrée.

### 4.4 Président de SAS
Assimilé salarié : bulletin de paie, cotisations du régime général **hors assurance chômage et AGS**, pas de réduction générale ni de nombreuses aides liées au contrat de travail. **Sans rémunération** : pas d'affiliation, pas de cotisations, pas de droits (retraite, indemnités journalières). Les dividendes de SAS ne subissent jamais de cotisations sociales (prélèvements sociaux uniquement).

### 4.5 ACRE
Exonération partielle et dégressive de cotisations la première année d'activité, **conditionnée** (depuis 2020 : publics ciblés — demandeurs d'emploi indemnisés, jeunes, bénéficiaires de minima sociaux… — conditions et taux à vérifier). Elle porte sur les **revenus d'activité** : un dirigeant non rémunéré n'en tire **aucun avantage**.

---

## 5. Épargne salariale

> 🟢 **En clair :** ce sont des sommes versées aux salariés en plus du salaire, liées aux résultats. La participation est obligatoire dès 50 salariés et se calcule avec une formule légale. Exemple : C18 Imprimerie Graphique Rhône et ses 52 salariés.

### 5.1 Participation
Obligatoire à partir de **50 salariés** (seuil apprécié selon les règles du Code de la sécurité sociale, franchi pendant 5 années civiles consécutives). Formule légale de la **réserve spéciale de participation (RSP)** (article L. 3324-1 du Code du travail) :

**RSP = ½ × (B − 5 % C) × S / VA**

- **B** : bénéfice net fiscal, diminué de l'impôt sur les sociétés correspondant ;
- **C** : capitaux propres (capital, primes, réserves, report à nouveau, provisions réglementées…) ;
- **S** : salaires (au sens de l'assiette des cotisations de sécurité sociale) ;
- **VA** : valeur ajoutée (charges de personnel + impôts et taxes hors taxes sur le CA + charges financières + dotations aux amortissements et provisions + résultat courant avant impôt).

Comptabilisation **dans l'exercice au titre duquel elle est due** :

| Compte | Débit | Crédit |
|---|---|---|
| 691 Participation des salariés aux résultats | RSP | |
| 4246 Réserve spéciale de participation (*intitulé selon nomenclature*) | | RSP |
| 645x / 647x Forfait social sur participation | Forfait social | |
| 4386 Organismes sociaux – charges à payer | | Forfait social |

Fiscalement, la participation est **déductible de l'exercice au cours duquel les sommes sont portées à la réserve spéciale**, c'est-à-dire N+1 : on **réintègre** la RSP dotée en N et on la **déduit** en N+1 (article 237 bis A du CGI ; même logique pour le forfait social associé). Attention : le résultat courant retenu dans la VA s'entend **avant** participation et avant IS (la participation ne se calcule pas sur elle-même).

> 🟢 **En clair :** en comptabilité, la participation est une charge de l'année où elle est gagnée (N). Pour l'impôt, elle ne compte que l'année suivante (N+1). On l'ajoute donc au résultat fiscal en N, puis on la retire en N+1.

Forfait social : 0 % pour les entreprises de moins de 50 salariés (participation volontaire), taux normal (20 % — *à vérifier*) au-delà, taux réduits possibles selon le support de placement.

### 5.2 Intéressement et PEE
- **Intéressement** : facultatif, accord d'au moins 3 ans, formule aléatoire liée aux résultats ou aux performances ; charge de l'exercice au titre duquel il est dû (6414 ou compte dédié), dette au 4284/428x. Exonéré de forfait social dans les entreprises de moins de 250 salariés (*à vérifier*).
- **PEE** : plan d'épargne d'entreprise ; l'**abondement** de l'employeur est une charge de personnel (6414/647x), soumise au forfait social et à la CSG/CRDS.
- CSG/CRDS sur participation et intéressement : précomptées sur 100 % du montant (pas d'abattement de 1,75 %).

---

## 6. Corner cases à reconnaître

> 🟢 **En clair :** ces situations ne se voient pas dans les chiffres, mais elles peuvent coûter très cher au client en cas de contrôle. Votre rôle : les repérer et prévenir le client par écrit.

| Situation | Risque | Réflexe |
|---|---|---|
| **Coach / formateur « indépendant »** travaillant aux horaires du club, avec planning imposé et matériel de l'entreprise (FitClub, C21) | **Requalification** en salariat (lien de subordination) : rappel de cotisations sur 3 ans + majorations, travail dissimulé possible | Analyser les indices (horaires, consignes, sanctions, clientèle propre, pluralité de donneurs d'ordre) ; alerter le client par écrit. |
| **Erreur de paie découverte après plusieurs mois** | Cotisations et PAS mal déclarés | Rappel (ou trop-perçu) en paie, **régularisation DSN rattachée à la période d'origine**, écriture rectificative ; aucune retenue sur salaire au-delà de la quotité saisissable pour un trop-perçu. |
| **Salarié qui est aussi associé** (Julie Dupain, C01) | Remise en cause du contrat de travail si pas de lien de subordination réel | Vérifier fonctions techniques distinctes et subordination au gérant. |
| **Dirigeant sans rémunération** (Studio Pixel, C25) | Aucune protection sociale ; « paiements » personnels de la société = rémunération de fait | Pas de 644/6411 ; vérifier qu'il n'y a pas d'AN déguisé (véhicule, loyer). |
| **Conjoint qui aide sans statut** | Travail dissimulé | Statut obligatoire : conjoint collaborateur, salarié ou associé. |

---

## 7. Checklist de fin de module

- [ ] Je sais reconstituer la cascade brut → net à payer → net imposable → PAS → net payé.
- [ ] Je passe une écriture de paie équilibrée à partir d'un journal de paie, en séparant 431 / 437x / 4421 / 425 / 427 / 421.
- [ ] Je rapproche paie, DSN, banque et comptabilité, et je sais quand une DSN peut être annulée-remplacée ou doit être régularisée.
- [ ] Je n'utilise **jamais** le compte 791 : les IJSS diminuent la charge de personnel.
- [ ] Je calcule une dette de CP (y compris jours acquis pendant un arrêt maladie depuis 2024) et ses charges sociales au taux réel.
- [ ] Je calcule l'indemnité légale de rupture et je sais où trouver le régime social applicable.
- [ ] Je distingue assimilé salarié / TNS / EI à l'IR et j'utilise les bons comptes (6411, 644, 646, 108).
- [ ] J'applique la règle des 10 % aux dividendes du gérant majoritaire.
- [ ] Je calcule une RSP et je traite son décalage fiscal.
- [ ] Je vérifie **chaque année** les taux, plafonds et dates de fin des dispositifs temporaires (pourboires, HS, réduction générale).

---

## À retenir en 30 secondes

- Le bulletin se lit de haut en bas : brut, cotisations, net, impôt, net payé.
- La charge de l'entreprise = brut (641) + cotisations patronales (645) ; le net n'est qu'une dette (421).
- Paie, DSN, banque et comptabilité doivent donner les mêmes chiffres, chaque mois et sur l'année.
- Le compte 791 n'existe plus : les IJSS diminuent la charge de personnel.
- À la clôture, enregistrez les congés acquis et non pris, avec leurs charges sociales au taux réel.
- Le statut du dirigeant (assimilé salarié, TNS, EI à l'IR) décide des comptes à utiliser.
- Les taux et plafonds changent chaque année : ne les apprenez pas par cœur, vérifiez-les.
