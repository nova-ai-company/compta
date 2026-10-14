# Corrigé E08-03 — Marchandises en transit au 31/12 : FOB, DAP, EXW chez Asia Trading

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-03](../exercices/E08-03_transit-incoterms-asia-trading.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

L'inventaire physique répond à la question « qu'y a-t-il dans l'entrepôt ? ». Le bilan répond à une autre question : « **qu'est-ce qui appartient à Asia Trading** (et dont elle supporte les risques) au 31/12 à minuit ? ». Entre les deux : les marchandises **en mer**, **sur la route**, **chez des tiers**.

Méthode du senior, dossier par dossier :
1. **Lire le contrat** (conditions générales d'achat / de vente) : y a-t-il une clause de transfert de propriété ?
2. **Lire l'Incoterm** : où passent les **risques** ? (Les Incoterms ne règlent pas, à eux seuls, la propriété : s'il n'y a pas de clause, on retient le transfert des risques comme indice du transfert du contrôle, et on le documente.)
3. **Vérifier les dates réelles** (B/L « shipped on board », CMR, preuve de livraison) — pas la date de la facture.
4. En déduire : stock oui / non ; achat ou vente à comptabiliser ou à neutraliser.

### Question 1 — Les quatre dossiers

| Dossier | Contrat / Incoterm | Date du fait générateur | Propriétaire au 31/12 | Dans le stock d'Asia Trading ? | Comptabilité actuelle | Régularisation |
|---|---|---|---|---|---|---|
| **A** — 2 000 ORBIT (achat) | FOB Ningbo + clause : propriété et risques à la mise à bord | Mise à bord le **12/12/2026** | **Asia Trading** | **Oui** (en transit, non compté) | Facture non comptabilisée ; fret en 6241 | **FNP** + **ajout au stock** (en transit) |
| **B** — 1 500 ARC (achat) | DAP Lyon + clause : propriété à la livraison au lieu convenu | Livraison le **08/01/2027** | **Le fournisseur** | **Non** | Achat comptabilisé en 607 le 05/12 | **CCA** (achat facturé, non livré) |
| **C** — 400 ZEN (vente) | EXW Lyon : risques transférés à la mise à disposition ; enlèvement par le transporteur du client | Prise en charge le **29/12/2026** | **Le client belge** | **Non** (sorties le 29/12, non comptées : correct) | Vente non comptabilisée | **Facture à établir** (livraison intracommunautaire exonérée) |
| **D** — 300 NOVA (vente) | DAP magasin du client : risques transférés à la livraison à Grenoble | Livraison le **04/01/2027** | **Asia Trading** (la réserve de propriété ne joue pas ici : c'est la livraison qui n'a pas eu lieu) | **Oui** (en cours de livraison, non comptées) | Vente comptabilisée le 30/12 | **PCA** sur la vente + **ajout au stock** |

Remarques :
- **Dossier A** : au 31/12, les lampes sont sur un navire entre Ningbo et Le Havre, mais elles sont **à Asia Trading** depuis le 12/12 (clause expresse, cohérente avec le FOB). Si le navire coule, c'est Asia Trading (ou son assureur) qui supporte la perte. → Achat de 2026 et stock au 31/12.
- **Dossier B** : la facture est datée du 05/12 et a été saisie, mais jusqu'au 08/01/2027 les lampadaires sont aux risques du vendeur et lui appartiennent. → Pas d'achat consommé en 2026 ni de stock ; on neutralise la charge par une **charge constatée d'avance** (achat facturé non livré). La dette fournisseur, elle, existe (facture reçue, échéance à 60 jours) : on la conserve.
- **Dossier C** : EXW = la vente est réalisée dès la prise en charge par le transporteur du client, le 29/12. La facture du 04/01/2027 se rattache à 2026 : **facture à établir**. Pour l'exonération de livraison intracommunautaire, il faut conserver les preuves du transport (CMR signée, attestation de réception du client) et le n° de TVA du client.
- **Dossier D** : la facture du 30/12 ne fait pas la vente. En DAP, le transfert des risques a lieu à la livraison au magasin, le 04/01/2027. Au 31/12, les 300 NOVA sont dans un camion, aux risques d'Asia Trading. → Le chiffre d'affaires est neutralisé (**PCA**) et les NOVA sont **réintégrées au stock**. *La clause de réserve de propriété n'est pas l'élément décisif : même livrées, des marchandises vendues avec réserve de propriété sortent du stock du vendeur à la livraison.*

## 2. Calculs (détaillés, chaque montant justifié)

### Question 2 — Valeur des marchandises à ajouter au stock

**Dossier A — 2 000 ORBIT en transit**

| Composant | Calcul | Montant |
|---|---|---|
| Prix d'achat | 19 200 USD / 1,0600 (cours du jour de l'opération : mise à bord le 12/12) | 18 113,21 € |
| Fret maritime (FOB : à la charge de l'acheteur, déjà engagé) | facture transitaire du 14/12 | 1 480,00 € |
| Droits de douane, transitaire, transport Le Havre → Lyon | **non encore engagés** au 31/12 (dédouanement en janvier) | 0,00 € |
| **Coût du stock en transit** | | **19 593,21 €** |

Le stock en transit est valorisé au cours **historique** (1,0600) : un stock est un élément non monétaire, il n'est **pas** réévalué au cours de clôture.

**Dossier D — 300 NOVA en cours de livraison** : 300 × 15,85 € = **4 755,00 €** (coût CMUP, pas le prix de vente de 9 600 €).

### Question 4 — Dettes en dollars au 31/12/2026

Une dette en devises (y compris une FNP) est convertie au **cours de clôture** ; l'écart avec le montant comptabilisé va en **écart de conversion** (476 si perte latente, 477 si gain latent) ; une perte latente non couverte donne lieu à une **provision pour perte de change**.

| Dette | Montant USD | Comptabilisée | Au cours de clôture (1,0400) | Écart (perte latente) |
|---|---|---|---|---|
| A — Ningbo Starlight (408, FNP) | 19 200,00 | 19 200 / 1,0600 = 18 113,21 € | 19 200 / 1,0400 = 18 461,54 € | **348,33 €** |
| B — Foshan Modern Lights (401) | 16 800,00 | 16 800 / 1,0700 = 15 700,93 € | 16 800 / 1,0400 = 16 153,85 € | **452,92 €** |
| **Total** | | | | **801,25 €** |

Le dollar s'est apprécié (moins de dollars pour 1 €) : il faudra plus d'euros pour payer → **perte latente** de 801,25 € → 476 et provision 1515 de 801,25 € (aucune couverture).

### Question 5 — Incidence sur le résultat et stock final

| Écriture | Incidence sur le résultat 2026 |
|---|---|
| FNP Ningbo (achat 607) | – 18 113,21 € |
| Stock en transit ORBIT (6037 créditeur) | + 19 593,21 € |
| CCA sur achat ARC | + 15 700,93 € |
| Provision pour perte de change | – 801,25 € |
| Facture à établir Lumière & Maison | + 9 800,00 € |
| PCA vente Maison Déco Grenoble | – 9 600,00 € |
| Stock NOVA en cours de livraison (6037 créditeur) | + 4 755,00 € |
| **Total** | **+ 21 334,68 €** |

Lecture : l'écart vient surtout du dossier B (un achat de 15 700,93 € était passé en charges sans marchandise en contrepartie) et du fret du dossier A déjà en charges (1 480,00 €) qui « suit » désormais le stock.

**Stock de marchandises au bilan au 31/12/2026** : 190 976,27 (entrepôt) + 19 593,21 (ORBIT en transit) + 4 755,00 (NOVA en cours de livraison) = **215 324,48 €**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 607 | Achats de marchandises | FNP Ningbo Starlight NS-26-2290 — 19 200 USD à 1,0600 | 18 113,21 | |
| 31/12/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Ningbo Starlight NS-26-2290 (dette USD) | | 18 113,21 |
| 31/12/2026 | OD | 38 | Stocks en voie d'acheminement | 2 000 ORBIT en mer (FOB, à bord le 12/12) — prix + fret | 19 593,21 | |
| 31/12/2026 | OD | 6037 | Variation des stocks de marchandises | Stock en transit ORBIT au 31/12/2026 | | 19 593,21 |
| 31/12/2026 | OD | 486 | Charges constatées d'avance | Achat ARC Foshan FML-1205-26 — DAP, livré le 08/01/2027 | 15 700,93 | |
| 31/12/2026 | OD | 607 | Achats de marchandises | Achat ARC Foshan FML-1205-26 non livré au 31/12 | | 15 700,93 |
| 31/12/2026 | OD | 476 | Différences de conversion – Actif | Réévaluation dettes USD au cours de 1,0400 | 801,25 | |
| 31/12/2026 | OD | 408 | Fournisseurs – factures non parvenues | Écart de conversion FNP Ningbo (18 461,54 – 18 113,21) | | 348,33 |
| 31/12/2026 | OD | 401 | Fournisseurs | Écart de conversion Foshan (16 153,85 – 15 700,93) | | 452,92 |
| 31/12/2026 | OD | 6865 | Dotations aux provisions financières | Provision pour perte de change au 31/12/2026 | 801,25 | |
| 31/12/2026 | OD | 1515 | Provisions pour pertes de change | Provision pour perte de change au 31/12/2026 | | 801,25 |
| 31/12/2026 | OD | 4181 | Clients – factures à établir | Lumière & Maison — 400 ZEN, EXW, enlevés le 29/12 | 9 800,00 | |
| 31/12/2026 | OD | 707 | Ventes de marchandises | LIC exonérée (art. 262 ter I CGI) — 400 ZEN | | 9 800,00 |
| 31/12/2026 | OD | 707 | Ventes de marchandises | Maison Déco Grenoble FA-2026-1219 — livrée le 04/01/2027 | 9 600,00 | |
| 31/12/2026 | OD | 487 | Produits constatés d'avance | Vente NOVA non livrée au 31/12 (DAP Grenoble) | | 9 600,00 |
| 31/12/2026 | OD | 38 | Stocks en voie d'acheminement | 300 NOVA en cours de livraison (300 × 15,85) | 4 755,00 | |
| 31/12/2026 | OD | 6037 | Variation des stocks de marchandises | Stock NOVA en cours de livraison au 31/12/2026 | | 4 755,00 |
| | | | | **Totaux** | **79 164,85** | **79 164,85** |

Le compte **38** est prévu par le PCG pour les stocks en voie d'acheminement, mis en dépôt ou donnés en consignation ; un sous-compte du 37 (« marchandises en transit ») est également acceptable. Au bilan, il figure dans le poste « marchandises ».

**Au 01/01/2027** : extourne de la FNP, de la CCA, de la facture à établir, du PCA et des deux lignes de stock en transit (la variation de stock 2027 repartira du stock total de 215 324,48 €) ; extourne des écarts de conversion (476 / 408 / 401). La provision pour perte de change sera reprise au 31/12/2027 (ou lors du règlement). Les ORBIT entreront dans la fiche CMUP à leur arrivée, à leur coût complet (prix + fret + droits + transitaire + transport), toujours au cours historique de 1,0600.

**TVA** : la facture FA-2026-1219 mentionne la TVA ; elle a été déclarée sur la CA3 de décembre et reste due (TVA facturée) : on ne neutralise que le **HT** en 487. La TVA à l'importation des ORBIT sera autoliquidée en janvier 2027, au dédouanement.

## 4. Points d'attention / pièges

- **FOB / CIF : les risques passent au chargement**. Que le fret soit payé par l'acheteur (FOB) ou par le vendeur (CIF), la marchandise est aux risques de l'acheteur dès qu'elle est à bord. La seule différence pour le stock : en CIF, le fret est inclus dans le prix du fournisseur.
- **Groupe D (DAP, DPU, DDP)** : le vendeur garde les risques jusqu'à destination ; une facture reçue (ou émise) avant n'y change rien.
- **Ne pas réévaluer le stock** au cours de clôture : seules les **dettes** en devises le sont.
- **Une FNP en devises est une dette en devises** : elle se réévalue comme un 401.
- **Provision pour perte de change** : non déductible fiscalement (la perte latente est déjà prise en compte par le régime fiscal des écarts de conversion, CGI art. 38-4) → réintégration extra-comptable (voir M09).
- **Vente intracommunautaire** : la facture doit être émise au plus tard le 15 du mois suivant la livraison et mentionner l'exonération ; l'état récapitulatif des clients doit inclure l'opération dans la période de **livraison** (décembre 2026).
- **Double comptage** : vérifier que les NOVA ne figurent pas aussi dans le stock compté (elles étaient parties : pas de doublon) et que les ORBIT ne seront pas comptées deux fois en janvier (extourne du 38).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — Explication à Kevin Nguyen :**

> Bonjour Kevin,
>
> Pour vos lampes en mer au 31/12, c'est le **contrat** (et l'Incoterm) qui décide, pas la date de la facture :
> - les **ORBIT** (FOB Ningbo) vous appartiennent depuis leur chargement le 12/12 : elles sont à vous, à vos risques, et figurent donc dans votre stock au 31/12, même si elles n'arriveront qu'en janvier. Avec un **CIF**, la réponse aurait été la même : le fournisseur aurait payé le fret et l'assurance, mais les risques vous auraient été transférés au chargement, exactement comme en FOB ;
> - les **ARC** (DAP Lyon) restent au fournisseur jusqu'à leur livraison chez vous le 08/01 : en DAP, c'est le vendeur qui porte le risque pendant le voyage. Ils ne sont donc ni dans vos achats consommés, ni dans votre stock 2026 ;
> - à l'inverse, côté ventes : les **ZEN** enlevés le 29/12 par le transporteur de votre client belge sont vendus en 2026 (EXW), alors que les **NOVA** facturées le 30/12 mais livrées à Grenoble le 04/01 sont une vente de 2027 (DAP).
>
> Ces ajustements augmentent votre résultat 2026 d'environ 21 300 € avant impôt, principalement parce que l'achat des ARC était déjà passé en charges.
>
> Pour l'an prochain : pourriez-vous nous transmettre, avec l'inventaire, la liste des conteneurs en mer au 31/12 (n° de B/L, date de chargement, Incoterm) et les livraisons clients en cours ?
>
> Bien cordialement,

**Contrôles et documentation :**
- feuille de cut-off « transit » : liste de tous les B/L de décembre, avec l'Incoterm, la date de mise à bord et la date d'arrivée ; rapprochement avec les factures et l'inventaire ;
- conserver les clauses contractuelles de transfert de propriété (CGA / CGV) dans le dossier permanent ;
- pour les livraisons intracommunautaires en EXW : vérifier que la preuve du transport est conservée (le transport est organisé par le client : attestation de réception indispensable) ;
- proposer à Kevin une réflexion sur la **couverture de change** (achats à terme) : 801,25 € de perte latente sur deux factures seulement.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié) : comptes 38 « Stocks en voie d'acheminement, mis en dépôt ou donnés en consignation », 486, 487, 4181, 476, 1515 ; conversion des opérations en devises (cours du jour de l'opération ; dettes au cours de clôture ; provision pour perte latente non couverte).
- Code civil art. 1196 et 1583 (transfert de propriété dans la vente, sauf clause contraire) ; règles Incoterms® 2020 de la Chambre de commerce internationale (transfert des risques et répartition des frais).
- Code de commerce art. L. 624-16 (clause de réserve de propriété).
- CGI art. 38-4 (régime fiscal des écarts de conversion) ; art. 262 ter I (exonération des livraisons intracommunautaires) ; art. 289 (délai d'émission des factures) ; règlement d'exécution (UE) n° 282/2011, art. 45 bis (preuve du transport intracommunautaire).
