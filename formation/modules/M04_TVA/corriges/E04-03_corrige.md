# Corrigé E04-03 — TVA sur la marge des véhicules d'occasion : globale ou au cas par cas ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-03](../exercices/E04-03_tva-marge-vo.md)

## 1. Analyse

**a) Marge globale : non applicable aux véhicules.** L'art. 297 A CGI prévoit deux modalités :
- **pièce par pièce** (règle générale) : la marge est calculée **pour chaque bien** ; une marge négative ne génère pas de TVA mais **ne se compense pas** avec la marge d'un autre bien ;
- **globale** (art. 297 A-II) : marge de la période = total des ventes – total des achats de la période, avec compensation ; **réservée aux biens dont le prix d'achat unitaire n'excède pas 300 €** (petits objets d'occasion, pièces détachées de récupération…).
Un véhicule d'occasion dépasse toujours 300 € : **pièce par pièce obligatoire**. La méthode de Thierry est irrégulière, et elle mélange en outre un véhicule relevant du régime normal (la fourgonnette).

**b) Véhicule par véhicule**

| VO | Origine | Régime | Raisonnement |
|---|---|---|---|
| 038 | Particulier | Marge | Acquis sans TVA |
| 039 | Particulier | Marge | Marge négative → TVA nulle, pas d'imputation |
| 040 | Professionnel **avec facture de TVA** (TVA déduite) | **Régime normal** | Le garage a déduit la TVA d'achat : la revente est taxée sur le **prix total** |
| 041 | Particulier | Marge | Voir E03-06 (frais de mise à la route inclus dans le prix) |
| 042 | Revendeur ayant appliqué la marge | Marge | La facture du vendeur mentionne le régime de la marge : pas de TVA déductible → marge à la revente |
| 043 | Revendeur allemand sous régime de la marge | Marge | Une livraison soumise au régime de la marge dans l'État de départ **n'est pas une acquisition intracommunautaire** taxable en France ; à la revente, régime de la marge |
| 045 | Revendeur allemand, LIC exonérée | **AIC taxable** | Voir c) |

**c) VO-26-045 : un « moyen de transport neuf ».** Un véhicule terrestre à moteur est réputé **neuf** si sa livraison intervient **moins de 6 mois** après sa première mise en service **ou** s'il a parcouru **moins de 6 000 km** (art. 298 sexies CGI). Ici : 4 mois **et** 3 200 km. Le vendeur allemand a, à juste titre, facturé une livraison intracommunautaire exonérée ; Garage Martin réalise une **acquisition intracommunautaire taxable en France** : il doit **autoliquider** la TVA française (20 % de 26 000 €) sur la CA3 de septembre (lignes B2, 08, 17) et la **déduire** (ligne 20, bien destiné à la revente). À la revente, le véhicule ne relève **pas** du régime de la marge (la TVA d'achat a été déduite) : **TVA sur le prix total**. « Pas de TVA, rien à déclarer » est faux — l'omission serait sanctionnée même si l'opération est neutre.

**d) Frais de remise en état (VO-044)** : TVA déductible (180 €) ; ils ne modifient pas le prix d'achat retenu pour le calcul de la future marge (4 200 €) mais ils **augmentent le coût du stock** (frais nécessaires pour mettre le bien en état d'être vendu).

## 2. Calculs

**TVA due par véhicule vendu**

| VO | Mois | Prix de vente TTC | Prix d'achat | Marge TTC | TVA due | Produit HT (707) |
|---|---|---|---|---|---|---|
| 038 | Juillet | 9 900,00 | 7 800,00 | 2 100,00 | **350,00** | 9 550,00 |
| 039 | Juillet | 10 500,00 | 11 200,00 | – 700,00 | **0,00** | 10 500,00 |
| 040 (normal) | Août | 12 600,00 | (8 000,00 HT) | — | **2 100,00** (12 600 × 20/120) | 10 500,00 |
| 041 | Septembre | 19 190,00 | 14 500,00 | 4 690,00 | **781,67** | 18 408,33 |
| 042 | Septembre | 17 400,00 | 15 000,00 | 2 400,00 | **400,00** | 17 000,00 |
| 043 | Septembre | 21 000,00 | 18 000,00 | 3 000,00 | **500,00** | 20 500,00 |
| **Total** | | | | | **4 131,67** | |

TVA par mois : juillet 350,00 € ; août 2 100,00 € ; septembre 1 681,67 €.

**Écart avec Thierry** : 4 131,67 – 2 415,00 = **1 716,67 € de TVA éludée** (compensation de la perte du VO-039 et taxation de la fourgonnette sur une « marge » de 3 000 € TTC au lieu du prix de vente total).

**Acquisition intracommunautaire VO-045** : base 26 000 € ; TVA autoliquidée **5 200 €**, déductible 5 200 € → net 0, mais lignes obligatoires.

**Stock de VO au 30/09/2026**

| VO | Coût d'acquisition | Frais de remise en état | Valeur en stock |
|---|---|---|---|
| 044 | 4 200,00 | 900,00 | 5 100,00 |
| 045 | 26 000,00 (HT, TVA autoliquidée déduite) | — | 26 000,00 |
| **Total** | | | **31 100,00** |
Test de dépréciation : véhicules en stock depuis moins de 6 mois ; comparer à la cote (valeur de vente probable – frais de vente). Pas d'indice de dépréciation fourni.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 03/07/2026 | AC | 607 | Achats de marchandises (VO) | VO-040 fourgonnette – PG-2026-19 | 8 000,00 | |
| 03/07/2026 | AC | 44566 | TVA déductible sur ABS | VO-040 – PG-2026-19 | 1 600,00 | |
| 03/07/2026 | AC | 401PLO | Fournisseur Plomberie des Gones | PG-2026-19 | | 9 600,00 |
| 05/07/2026 | VT | 411 | Clients | VO-038 – régime de la marge | 9 900,00 | |
| 05/07/2026 | VT | 7071 | Ventes VO – régime de la marge | VO-038 | | 9 550,00 |
| 05/07/2026 | VT | 445712 | TVA collectée sur marge | VO-038 – marge 2 100 × 20/120 | | 350,00 |
| 22/07/2026 | VT | 411 | Clients | VO-039 – régime de la marge (marge négative) | 10 500,00 | |
| 22/07/2026 | VT | 7071 | Ventes VO – régime de la marge | VO-039 | | 10 500,00 |
| 28/08/2026 | VT | 411 | Clients | VO-040 – régime normal | 12 600,00 | |
| 28/08/2026 | VT | 7070 | Ventes VO – régime normal | VO-040 | | 10 500,00 |
| 28/08/2026 | VT | 44571 | TVA collectée 20 % | VO-040 | | 2 100,00 |
| 12/09/2026 | VT | 411 | Clients | VO-042 – régime de la marge | 17 400,00 | |
| 12/09/2026 | VT | 7071 | Ventes VO – régime de la marge | VO-042 | | 17 000,00 |
| 12/09/2026 | VT | 445712 | TVA collectée sur marge | VO-042 – marge 2 400 × 20/120 | | 400,00 |
| 15/09/2026 | AC | 607 | Achats de marchandises (VO) | VO-045 – AIC AK-26-3570 | 26 000,00 | |
| 15/09/2026 | AC | 401KEL | Fournisseur Autohaus Keller | AK-26-3570 | | 26 000,00 |
| 15/09/2026 | AC | 445662 | TVA déductible intracommunautaire | VO-045 – autoliquidation AIC | 5 200,00 | |
| 15/09/2026 | AC | 4452 | TVA due intracommunautaire | VO-045 – autoliquidation AIC | | 5 200,00 |
| 25/09/2026 | VT | 411 | Clients | VO-043 – régime de la marge | 21 000,00 | |
| 25/09/2026 | VT | 7071 | Ventes VO – régime de la marge | VO-043 | | 20 500,00 |
| 25/09/2026 | VT | 445712 | TVA collectée sur marge | VO-043 – marge 3 000 × 20/120 | | 500,00 |
| | | | | **Totaux** | **112 200,00** | **112 200,00** |

(Les encaissements clients ne sont pas détaillés. Au 30/09/2026, la variation de stock de marchandises intègre les VO-044 et VO-045 pour 31 100 €.)

## 4. Points d'attention / pièges

- **Pas de compensation** entre véhicules : la perte du VO-039 est un coût commercial, pas une réduction de TVA.
- **Origine de chaque VO** : c'est le **justificatif d'achat** qui détermine le régime de revente (certificat de cession d'un particulier, facture avec TVA d'un professionnel, facture « régime de la marge » d'un revendeur). Classer ces pièces dans le dossier de chaque VO.
- **Achats dans l'UE** : trois cas — vendeur sous régime de la marge (pas d'AIC, marge à la revente) ; vendeur avec LIC exonérée d'un véhicule d'occasion (AIC taxable, régime normal à la revente) ; véhicule **neuf** au sens de l'art. 298 sexies (AIC taxable dans tous les cas, même acheté à un particulier).
- **Quitus fiscal** : pour immatriculer en France un véhicule acheté dans l'UE, il faut obtenir un certificat fiscal auprès du SIE ; pour le VO-045, il sera délivré au vu de l'autoliquidation.
- **Factures de vente** sous le régime de la marge : aucune TVA apparente ; mention « Régime particulier – Biens d'occasion ».

## 5. Ce qu'un senior ferait en plus

**Régularisation des CA3** : la CA3 de septembre n'est peut-être pas encore déposée (date limite en octobre) — si c'est le cas, la déposer avec les bons montants ; sinon, régulariser sur la CA3 suivante :
- TVA sur marge du trimestre : total dû 4 131,67 € ; Thierry a déclaré 2 415,00 € → **1 716,67 €** complémentaires à porter sur la prochaine déclaration (en signalant la période d'origine) ;
- **intérêt de retard** de 0,20 % par mois sur les sommes déclarées en retard (juillet et août), réduit en cas de régularisation spontanée ;
- AIC du VO-045 : lignes B2 / 08 / 17 et 20 sur la CA3 de septembre (ou en régularisation).

**Mail à Thierry :**
> Bonjour Thierry, la marge globale n'est permise que pour des biens achetés moins de 300 € pièce ; pour les voitures, c'est obligatoirement voiture par voiture, sans compenser les pertes. La fourgonnette, achetée avec TVA, se revend avec TVA sur le prix total. Il manque 1 716,67 € de TVA sur le trimestre, que nous régularisons tout de suite (avec un petit intérêt de retard). Pour le SUV allemand de 4 mois, c'est un véhicule « neuf » au sens de la TVA : il faut déclarer et déduire la TVA française (opération neutre) et vous le revendrez avec TVA sur le prix total. Je vous propose de reprendre la préparation des CA3 VO.

**Contrôle de fin d'exercice** : tableau de suivi des VO (achat, origine, régime, frais, vente, marge, TVA) rapproché du livre de police, des comptes 607/7071/7070 et du stock.

## 6. Références

- CGI : art. 297 A (régime de la marge, pièce par pièce et marge globale limitée aux biens ≤ 300 €), art. 297 E (pas de TVA apparente), art. 298 sexies (moyens de transport neufs), art. 256 bis (acquisitions intracommunautaires), art. 1727 (intérêt de retard).
- Directive 2006/112/CE : art. 311 à 325 (régime de la marge), art. 2 § 2 (moyens de transport neufs).
- BOFiP : TVA-SECT (biens d'occasion, véhicules d'occasion acquis dans l'UE).
