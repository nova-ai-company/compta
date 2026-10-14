# Corrigé E02-04 — Acquisition intracommunautaire : la collection d'hiver arrive d'Italie

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-04](../exercices/E02-04_achat-intracom-mode-co.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Question 1 — Pourquoi pas de TVA ?** Une vente de biens entre deux assujettis de deux États membres, avec **transport effectif** de l'Italie vers la France, se décompose en :
- une **livraison intracommunautaire exonérée** en Italie (le fournisseur l'indique : art. 41 D.L. 331/1993, art. 138 de la directive) ;
- une **acquisition intracommunautaire imposable en France** (CGI art. 256 bis), dont la TVA est due par **l'acquéreur**, Mode & Co.

Mode & Co **autoliquide** : elle déclare la TVA due (4452) et, ayant des droits à déduction complets, la déduit simultanément (445662). Montant : 15 278,20 × 20 % = **3 055,64 €**. Opération **neutre** en trésorerie, mais **obligatoirement déclarée** : l'absence de déclaration est sanctionnée (CGI art. 1788 A), même sans perte pour le Trésor.

**Question 2 — Fait générateur et exigibilité.** Le fait générateur est la **livraison** (enlèvement le 25/09/2026, transport vers la France). La TVA est exigible **le 15 du mois suivant** le fait générateur (15/10/2026), **ou à la date de la facture si elle est émise avant** (CGI art. 269-2-d). La facture est datée du **25/09/2026** → TVA exigible en **septembre** → **CA3 de septembre 2026**, celle que l'on prépare.

**Question 3 — Le transporteur facture de la TVA.** Le transport intracommunautaire de biens est une **prestation de services** ; entre assujettis, elle est imposable au lieu d'établissement du **preneur** (CGI art. 259). Le preneur (Mode & Co) est en France, le prestataire (Transalp) aussi → TVA française classique, facturée par le transporteur, déductible par Mode & Co. Si le transporteur avait été italien, Mode & Co aurait autoliquidé la TVA sur le transport (service UE).

**Question 4 — L'anomalie : le n° de TVA de Mode & Co.** La facture indique **FR02** 851777890 ; le bon numéro est **FR20** 851777890 (clé inversée).
- **Pour le fournisseur italien** : l'exonération de sa livraison intracommunautaire suppose notamment que l'acquéreur dispose d'un numéro de TVA valide **et le lui ait communiqué** ; un numéro erroné expose Tessitura Ferrari à une remise en cause de l'exonération (et à facturer la TVA italienne).
- **Pour Mode & Co** : l'acquisition reste imposable en France et l'autoliquidation est due quoi qu'il arrive. Mais la facture est irrégulière (mention erronée), et l'incohérence apparaîtra dans les échanges d'informations entre administrations (état récapitulatif du fournisseur italien déclaré sous un numéro inexistant).
- **Action** : demander à Tessitura Ferrari une **facture rectificative** (ou une note de correction) portant FR20 851777890, et vérifier dans la fiche fournisseur que le bon numéro leur a été communiqué. Vérifier aussi **leur** numéro sur le système VIES de la Commission européenne et conserver la preuve de la consultation.

## 2. Calculs (détaillés, chaque montant justifié)

| Ligne | Calcul | Montant |
|---|---|---|
| Chemises | 300 × 19,80 | 5 940,00 € |
| Vestes | 200 × 38,50 | 7 700,00 € |
| Jupes | 120 × 16,25 | 1 950,00 € |
| Total brut | | 15 590,00 € ✓ |
| Remise 2 % | 15 590,00 × 2 % | – 311,80 € ✓ |
| **Base imposable** | | **15 278,20 €** ✓ |
| **TVA autoliquidée 20 %** | 15 278,20 × 20 % | **3 055,64 €** |
| Transport HT / TVA / TTC | | 420,00 € / 84,00 € / 504,00 € ✓ |

**Question 6 — coût d'entrée d'une veste** (transport réparti au prorata des valeurs nettes) :
- prix net d'une veste : 38,50 × 98 % = **37,73 €** ;
- valeur nette des vestes : 7 700,00 × 98 % = 7 546,00 € ; quote-part de transport : 420,00 × 7 546,00 / 15 278,20 = 207,44 € ; par veste : 207,44 / 200 = **1,04 €** ;
- **coût d'entrée ≈ 38,77 €** par veste (hors TVA, récupérable).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 25/09/2026 | AC | 607 | Achats de marchandises | Tessitura Ferrari F 2026/FV/0388 collection hiver | 15 278,20 | |
| 25/09/2026 | AC | 445662 | TVA déductible intracommunautaire | Tessitura Ferrari F 2026/FV/0388 autoliquidation | 3 055,64 | |
| 25/09/2026 | AC | 4452 | TVA due intracommunautaire | Tessitura Ferrari F 2026/FV/0388 autoliquidation | | 3 055,64 |
| 25/09/2026 | AC | 401FERR | Fournisseur Tessitura Ferrari | Tessitura Ferrari F 2026/FV/0388 | | 15 278,20 |
| 30/09/2026 | AC | 6241 | Transports sur achats | Transalp F TL-26-09-4471 transport Prato-Vénissieux | 420,00 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | Transalp F TL-26-09-4471 | 84,00 | |
| 30/09/2026 | AC | 401TRAN | Fournisseur Transalp Logistique | Transalp F TL-26-09-4471 | | 504,00 |
| | | | | **Totaux** | **18 837,84** | **18 837,84** |

**Sur la CA3 de septembre 2026** : 15 278,20 € en base sur la ligne des **acquisitions intracommunautaires** (TVA due 3 055,64 €) ; 3 055,64 € en TVA déductible « autres biens et services » ; la TVA de 84,00 € du transporteur n'est déductible qu'au **paiement** (prestation de services, sauf option du transporteur pour les débits) → CA3 d'octobre si la facture est payée le 30/10.

## 4. Points d'attention / pièges

- **« Pas de TVA sur la facture = rien à déclarer »** : c'est l'erreur la plus fréquente sur les achats intracommunautaires. Toute facture d'un fournisseur UE sans TVA déclenche l'autoliquidation.
- **Date d'exigibilité** : ce n'est ni la date de réception (29/09) ni la date de paiement (24/11) ; c'est le 15 du mois suivant la livraison, **ou la date de facture si elle est antérieure**.
- **Si le fournisseur italien avait facturé de la TVA italienne** (22 %) par erreur : non récupérable en France via la CA3 ; il faudrait exiger une facture rectificative (ou, à défaut, une procédure de remboursement auprès de l'Italie, longue et incertaine).
- **Incoterm EXW** : le transfert des risques a lieu à l'enlèvement à Prato (25/09). Si la clôture avait été le 30/09 et la marchandise encore en transit, elle aurait dû figurer **dans le stock** de Mode & Co.
- **Écarts de change** : aucun ici (facture en euros).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 7 — autres obligations** :
- **EMEBI** (enquête statistique sur les échanges de biens intra-UE) : obligatoire pour les acquisitions seulement au-delà d'un seuil annuel (à vérifier chaque année) ; Mode & Co est en dessous → rien à faire, mais à **surveiller** si les volumes italiens augmentent ;
- **e-reporting** : à partir du **01/09/2027** (PME), les acquisitions auprès de fournisseurs non établis en France devront être transmises à l'administration via la PA de Mode & Co (e-reporting des opérations internationales) ;
- **conservation** de la preuve du transport (CMR du transporteur, bon de réception) : elle sert au fournisseur italien pour justifier son exonération, et à Mode & Co pour justifier la date d'entrée en stock.

**Message à Inès Moreau :**

> Bonjour Inès,
>
> La logique est simple : quand vous achetez des marchandises à un fournisseur d'un autre pays de l'UE, c'est **vous** qui déclarez la TVA française à sa place (3 055,64 € sur cette facture), et vous la récupérez sur la même déclaration. Ça ne vous coûte rien, mais il faut absolument la déclarer — c'est fait sur la CA3 de septembre.
>
> Le transporteur, lui, est français et vous facture un service en France : TVA normale, que vous récupérez quand vous le payez.
>
> Un point à régler : Tessitura Ferrari a mal recopié votre numéro de TVA (FR02 au lieu de FR20). Pouvez-vous leur demander une facture corrigée ? C'est surtout important pour eux, mais cela évite des questions lors des recoupements entre administrations.

**Documentation** : copie de la consultation VIES du numéro de Tessitura Ferrari, CMR, bon de réception ; fiche fournisseur avec le bon numéro de TVA de Mode & Co à transmettre à tous les fournisseurs UE.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 256 bis : acquisitions intracommunautaires de biens.
- CGI art. 262 ter I : exonération des livraisons intracommunautaires (côté vendeur français) ; directive 2006/112/CE art. 138 (côté vendeur UE).
- CGI art. 269-2-d : exigibilité de la TVA sur les acquisitions intracommunautaires.
- CGI art. 259 : lieu des prestations de services entre assujettis (transport).
- CGI art. 1788 A : sanctions des manquements liés à l'autoliquidation.
- CGI art. 289 bis et 290 : facturation électronique et e-reporting (PME : 01/09/2027).
- PCG : comptes 607, 4452, 445662, 6241 ; coût d'acquisition des stocks.
