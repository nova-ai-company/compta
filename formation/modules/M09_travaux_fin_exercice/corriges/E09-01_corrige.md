# Corrigé E09-01 — Le cut-off de Transports Leroy : 15 pièces de janvier à trier

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-01](../exercices/E09-01_cut-off-transports-leroy.md)

## 1. Analyse

**Méthode senior :** pour chaque pièce, on ne regarde **pas la date de la facture** mais la date du **fait générateur** : livraison, prestation réalisée, service fait, obligation née. Une pièce datée de janvier qui porte sur une prestation de décembre doit être rattachée à l'exercice 2025. Inversement, une facture datée de décembre peut porter sur une livraison de janvier : c'est le piège de la pièce 14.

| Pièce | Fait générateur | Rattachement | Régularisation au 31/12/2025 |
|---|---|---|---|
| 1 — Carburant décembre | Consommation 01–31/12/2025 | 2025 | **FNP** 18 450 € HT |
| 2 — Péages décembre | Trajets décembre 2025 | 2025 | **FNP** 2 860 € HT |
| 3 — Réparation | Intervention terminée le 29/12/2025 (service fait) | 2025 | **FNP** 4 200 € HT |
| 4 — Assurance 2026 | Période 01/01–31/12/2026 | 2026 | **Aucune** (rien n'a été payé ni comptabilisé en 2025) |
| 5 — RFA pneus 2025 | Remise acquise sur les achats 2025 | 2025 | **Avoir à recevoir** 3 100 € HT |
| 6 — Transport du 30/12 | Prestation exécutée le 30/12/2025 | 2025 | **FAE** 7 800 € HT |
| 7 — Tournées 05–09/01 | Prestations de janvier 2026 | 2026 | **Aucune** |
| 8 — Avarie du 18/12 | Dommage survenu le 18/12/2025, responsabilité reconnue le 19/12 | 2025 | **Charge à payer** 1 500 € **sans TVA** (indemnité, pas un avoir) |
| 9 — Location 15/12–14/01 | 17 jours sur 31 en 2025 | 2025 pour 17/31 | **FNP** 1 700 € HT |
| 10 — Téléphonie janvier | Abonnement de janvier 2026 | 2026 | **Aucune** |
| 11 — Prime de fin d'année | Décision écrite du 18/12/2025, condition de présence au 31/12/2025 → obligation née en 2025 | 2025 | **Charges à payer** : 6 000 € brut + 2 520 € de cotisations patronales |
| 12 — TICPE S2 2025 | Consommations du 2e semestre 2025 ; droit acquis | 2025 | **Produit à recevoir** sur l'État 9 460 € (en diminution du carburant) |
| 13 — Échéance d'emprunt | Intérêts du 15/10/2025 au 31/12/2025 | 2025 pour 77/92 | **Intérêts courus** 2 310 € |
| 14 — Tracteur Volvo | Livraison et transfert de propriété le **08/01/2026** | 2026 | **Annuler l'immobilisation**, reclasser l'acompte en 238, annuler la dotation, régulariser la TVA |
| 15 — Prud'hommes | Licenciement du 21/11/2025 (événement passé), saisine connue avant l'arrêté des comptes | 2025 | **Provision pour litige** 8 000 € |

Les points qui demandent un vrai raisonnement :

- **Pièce 8 — indemnité ou avoir ?** Le client ne demande pas une réduction du prix du transport : il demande la **réparation d'un préjudice** (marchandise brisée). Une indemnité qui répare un préjudice est **hors champ de la TVA**. On ne passe donc ni avoir à établir (4198) ni TVA : c'est une **charge à payer (4686)**. M. Leroy a reconnu sa responsabilité le 19/12/2025 : la dette est certaine dans son principe et dans son montant dès 2025. La charge se classe en **658** (*subdivision selon la nomenclature 2025 du PCG*), et non en exceptionnel : une avarie n'est ni majeure ni inhabituelle pour un transporteur. Vérifiez aussi l'assurance « marchandises transportées » : si l'assureur rembourse, il faut un produit à recevoir **s'il a donné son accord**.
- **Pièce 11 — prime :** la note de service du 18/12/2025 crée une **obligation envers les chauffeurs** présents au 31/12/2025. Le versement en janvier ne change rien : la charge (et ses cotisations) appartient à 2025.
- **Pièce 12 — TICPE :** le droit au remboursement naît de la consommation de gazole du semestre. Il est **acquis** au 31/12/2025, et son montant est déterminable (calculé par la téléprocédure). On constate donc un **produit à recevoir**. Depuis le PCG 2025, le compte 791 n'existe plus : ce remboursement **vient en diminution de la charge de carburant** (6061), puisqu'il réduit le coût du gazole.
- **Pièce 14 — le tracteur :** une immobilisation entre au bilan au **transfert de contrôle**, en pratique à la livraison. Le 31/12/2025, le tracteur était encore chez Volvo : il ne pouvait être ni immobilisé ni amorti. Seul l'**acompte versé** de 20 000 € est un actif, en **238** *Avances et acomptes versés sur commandes d'immobilisations corporelles*. Côté TVA, pour une **livraison de biens**, la TVA devient exigible à la livraison, et un acompte sur un bien ne la rend pas exigible. Elle n'était donc **pas déductible en décembre 2025**, même si la facture était datée du 28/12.
- **Pièce 15 — provision :** l'obligation vient d'un **événement passé** (le licenciement de novembre 2025). La saisine du 14/01/2026 est un **événement postérieur ajustant**, car elle précise une situation qui existait à la clôture. La sortie de ressources est probable selon l'avocat et le montant est estimé (8 000 €, meilleure estimation). Les trois conditions sont réunies.
- **Pièces 4, 7 et 10 :** ces pièces sont des **leurres**. Elles sont datées de janvier, mais elles portent sur 2026. Ne rien faire est la bonne réponse.

## 2. Calculs

**FNP (HT / TVA) :**

| Pièce | HT | TVA | TTC |
|---|---|---|---|
| 1 Carburant | 18 450,00 € | 3 690,00 € | 22 140,00 € |
| 2 Péages | 2 860,00 € | 572,00 € | 3 432,00 € |
| 3 Réparation | 4 200,00 € | 840,00 € | 5 040,00 € |
| 9 Location : 3 100 × 17/31 | 1 700,00 € | 340,00 € | 2 040,00 € |
| **Total** | **27 210,00 €** | **5 442,00 €** | **32 652,00 €** |

Location : du 15/12 au 31/12/2025 inclus, il y a 17 jours ; 3 100 € × 17 / 31 = **1 700,00 €**. La TVA correspondante est 1 700 € × 20 % = 340,00 €.

**Prime :** 12 chauffeurs × 500 € = 6 000,00 € ; cotisations patronales 6 000 € × 42 % = **2 520,00 €**.

**Intérêts courus :** du 15/10/2025 au 15/01/2026, la période compte 92 jours, dont 77 jours jusqu'au 31/12/2025 (16 jours en octobre, 30 en novembre, 31 en décembre). 2 760 € × 77 / 92 = **2 310,00 €**.

**Tracteur :** la dotation passée à tort est 98 000 € / 5 × 3/360 = **163,33 €**. Elle doit être annulée.

**Impact sur le résultat 2025 (avant IS) :**

| Élément | Impact |
|---|---|
| FNP (charges) | – 27 210,00 € |
| Avoir à recevoir | + 3 100,00 € |
| FAE | + 7 800,00 € |
| Indemnité avarie | – 1 500,00 € |
| Prime + cotisations | – 8 520,00 € |
| TICPE à recevoir | + 9 460,00 € |
| Intérêts courus | – 2 310,00 € |
| Provision prud'hommes | – 8 000,00 € |
| Annulation dotation tracteur | + 163,33 € |
| **Total** | **– 27 016,67 €** |

## 3. Écritures comptables

**Régularisations au 31/12/2025 :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2025 | OD | 6061 | Fournitures non stockables (énergie) | FNP TotalCard décembre | 18 450,00 | |
| 31/12/2025 | OD | 44586 | TVA sur factures non parvenues | FNP TotalCard décembre | 3 690,00 | |
| 31/12/2025 | OD | 4081 | Fournisseurs – factures non parvenues | FNP TotalCard décembre | | 22 140,00 |
| 31/12/2025 | OD | 6251 | Voyages et déplacements (péages) | FNP APRR décembre | 2 860,00 | |
| 31/12/2025 | OD | 44586 | TVA sur factures non parvenues | FNP APRR décembre | 572,00 | |
| 31/12/2025 | OD | 4081 | Fournisseurs – factures non parvenues | FNP APRR décembre | | 3 432,00 |
| 31/12/2025 | OD | 6155 | Entretien et réparations sur biens mobiliers | FNP PL Service OR-2512-339 | 4 200,00 | |
| 31/12/2025 | OD | 44586 | TVA sur factures non parvenues | FNP PL Service | 840,00 | |
| 31/12/2025 | OD | 4081 | Fournisseurs – factures non parvenues | FNP PL Service | | 5 040,00 |
| 31/12/2025 | OD | 6135 | Locations mobilières | FNP Loc'Remorques 17/31 j | 1 700,00 | |
| 31/12/2025 | OD | 44586 | TVA sur factures non parvenues | FNP Loc'Remorques | 340,00 | |
| 31/12/2025 | OD | 4081 | Fournisseurs – factures non parvenues | FNP Loc'Remorques | | 2 040,00 |
| 31/12/2025 | OD | 4098 | Fournisseurs – avoirs à recevoir | RFA 2025 Europneus | 3 720,00 | |
| 31/12/2025 | OD | 609 | Rabais, remises, ristournes obtenus sur achats | RFA 2025 Europneus | | 3 100,00 |
| 31/12/2025 | OD | 44586 | TVA sur factures non parvenues | RFA 2025 Europneus | | 620,00 |
| 31/12/2025 | OD | 4181 | Clients – factures à établir | FAE Logistique Bresse CMR 30/12 | 9 360,00 | |
| 31/12/2025 | OD | 706 | Prestations de services | FAE Logistique Bresse | | 7 800,00 |
| 31/12/2025 | OD | 44587 | TVA sur factures à établir | FAE Logistique Bresse | | 1 560,00 |
| 31/12/2025 | OD | 658 | Charges diverses de gestion courante (*subdivision selon nomenclature 2025*) | Indemnité avarie Verreries de Givors | 1 500,00 | |
| 31/12/2025 | OD | 4686 | Divers – charges à payer | Indemnité avarie Verreries de Givors | | 1 500,00 |
| 31/12/2025 | OD | 6413 | Primes et gratifications | Prime fin d'année 2025 | 6 000,00 | |
| 31/12/2025 | OD | 4286 | Personnel – autres charges à payer | Prime fin d'année 2025 | | 6 000,00 |
| 31/12/2025 | OD | 645 | Charges de sécurité sociale et de prévoyance | Cotisations s/ prime 42 % | 2 520,00 | |
| 31/12/2025 | OD | 4386 | Organismes sociaux – autres charges à payer | Cotisations s/ prime | | 2 520,00 |
| 31/12/2025 | OD | 4487 | État – produits à recevoir | Remboursement TICPE S2 2025 | 9 460,00 | |
| 31/12/2025 | OD | 6061 | Fournitures non stockables (énergie) | Remboursement TICPE S2 2025 | | 9 460,00 |
| 31/12/2025 | OD | 6611 | Intérêts des emprunts et dettes | ICNE prêt 0045-778 (77/92) | 2 310,00 | |
| 31/12/2025 | OD | 1688 | Intérêts courus sur emprunts | ICNE prêt 0045-778 | | 2 310,00 |
| 31/12/2025 | OD | 6815 | Dotations aux provisions d'exploitation | Litige prud'homal K. D. | 8 000,00 | |
| 31/12/2025 | OD | 1511 | Provisions pour litiges | Litige prud'homal K. D. | | 8 000,00 |
| 31/12/2025 | OD | 404 | Fournisseurs d'immobilisations | Annulation facture Volvo (livraison 08/01/2026) | 117 600,00 | |
| 31/12/2025 | OD | 2182 | Matériel de transport | Annulation facture Volvo | | 98 000,00 |
| 31/12/2025 | OD | 44562 | TVA déductible sur immobilisations | Annulation TVA déduite par anticipation | | 19 600,00 |
| 31/12/2025 | OD | 238 | Avances et acomptes versés sur commandes d'immobilisations corporelles | Reclassement acompte Volvo | 20 000,00 | |
| 31/12/2025 | OD | 404 | Fournisseurs d'immobilisations | Reclassement acompte Volvo | | 20 000,00 |
| 31/12/2025 | OD | 28182 | Amortissement du matériel de transport | Annulation dotation Volvo | 163,33 | |
| 31/12/2025 | OD | 6811 | Dotations aux amortissements | Annulation dotation Volvo | | 163,33 |
| | | | | **Totaux** | **213 285,33** | **213 285,33** |

**Écritures au 01/01/2026 :**
- **Extournes** des FNP, de l'avoir à recevoir, de la FAE, des charges de personnel à payer (4286/4386) et des intérêts courus : il suffit de passer les mêmes lignes en inversant débit et crédit. La facture réelle, l'avoir et la paie de janvier se saisissent ensuite normalement.
- **4686** (avarie) et **4487** (TICPE) : pas d'extourne nécessaire. On solde ces comptes au paiement ou à l'encaissement (D 4686 / C 512 ; D 512 / C 4487), ce qui garde la trace du suivi.
- **Provision 1511** : elle reste au bilan. On la reprend au dénouement du litige.
- **Tracteur au 08/01/2026** : D 2182 98 000,00 + D 44562 19 600,00 / C 404 117 600,00, puis D 404 20 000,00 / C 238 20 000,00. L'amortissement court à partir du 08/01/2026.

## 4. Points d'attention / pièges

- **Date de facture ≠ date de rattachement.** Les pièces 1, 2, 3, 6, 9 et 13 sont datées de 2026 mais relèvent (en tout ou partie) de 2025. La pièce 14 est datée de 2025 mais relève de 2026.
- **TVA dans les régularisations :** HT en charge ou en produit, TVA en **44586/44587**. Elle n'est jamais déduite ni collectée sur la CA3 avant la facture.
- **TVA du tracteur :** déduire 19 600 € en décembre 2025 était prématuré. En pratique, la déduction se trouve « régularisée » dans le temps, puisque la TVA devient déductible dès la livraison en janvier 2026. Il faut quand même **ne pas la déduire une seconde fois** sur la CA3 de janvier, et le signaler dans le dossier. En cas de contrôle, l'avance de déduction d'un mois peut être relevée (intérêt de retard minime).
- **Pièce 8 :** passer un avoir à établir avec 250 € de TVA (1 500 € traités comme TTC) aurait été faux, car il ne s'agit pas d'une réduction de prix.
- **Pièce 9 :** compter les jours **inclus**. Du 15/12 au 31/12, il y a 17 jours et non 16.
- **Pièce 11 :** oublier les **cotisations patronales** sur la prime revient à sous-estimer la charge de 42 %.
- **Pièce 12 :** le compte **791 n'existe plus**. Ne présentez pas le remboursement de TICPE en « transfert de charges ».
- **Pièce 15 :** la provision est **déductible** fiscalement (litige nettement précisé, probable, chiffré par l'avocat, charge future elle-même déductible). Elle doit figurer sur le relevé des provisions.
- **Pièce 4 :** si l'assurance 2026 avait été **prélevée en décembre 2025** et passée en charge en 2025, il aurait fallu une **CCA** pour la totalité de la prime. Vérifiez toujours la date de comptabilisation de la charge, pas seulement la période couverte.

## 5. Ce qu'un senior ferait en plus

**Note à Hélène (5 lignes) :**
> « Le cut-off 2025 de Transports Leroy minorait les charges et majorait le résultat : les régularisations manquantes représentent **– 27 016,67 € sur le résultat 2025** (avant IS). Il y a aussi une immobilisation de 98 000 € comptabilisée à tort et une TVA de 19 600 € déduite un mois trop tôt. Je propose : (1) de mesurer le caractère significatif de l'écart par rapport au résultat 2025 et au seuil de signification ; (2) de traiter les erreurs significatives selon les règles de correction d'erreurs dans les comptes 2026 et de déposer une réclamation sur l'IS 2025 si c'est pertinent (voir E09-11) ; (3) de mettre en place pour 2026 une **liste de contrôle de cut-off** et une demande systématique des pièces de janvier, du dernier n° de CMR et de la confirmation de l'avocat. »

**Contrôles complémentaires :**
- Rapprocher le **dernier CMR de 2025** et la dernière facture de 2025 pour s'assurer qu'aucun autre transport de fin décembre n'est resté non facturé.
- Demander à l'avocat une **lettre de confirmation** datée au plus près de l'arrêté.
- Interroger Bruno Leroy sur les **autres primes ou engagements** pris oralement en décembre.
- Vérifier la **provision pour congés payés** (4282/4382), absente des pièces mais incontournable pour 24 salariés.
- Pour la clôture 2026, demander dès le 5 janvier l'**export du journal des achats de janvier** au fil de l'eau.

**Mail type au client :**
> « Monsieur Leroy, pour préparer la clôture 2026, merci de nous transmettre avant le 20 janvier 2027 : les factures fournisseurs et clients datées de janvier 2027, le dernier numéro de CMR de décembre, toute réclamation client reçue depuis le 1er décembre, les décisions de primes et les courriers d'avocat. Ces pièces conditionnent l'exactitude de votre résultat 2026. »

## 6. Références

- Code de commerce, art. L. 123-12 à L. 123-14 (régularité, sincérité, image fidèle) et L. 123-21 (seuls les bénéfices réalisés peuvent être inscrits).
- CGI, art. 38, 2 (créances acquises / dettes certaines), art. 39, 1-5° (provisions), art. 269 (exigibilité de la TVA : livraison de biens / encaissement pour les services sauf option pour les débits), art. 271 (droit à déduction).
- PCG (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06) : définition des passifs et provisions ; entrée des immobilisations à la date de transfert du contrôle ; suppression des comptes 79.
- Code des douanes : remboursement partiel de la TICPE sur le gazole des véhicules de transport de marchandises de plus de 7,5 t — *modalités et taux à vérifier chaque année*.
