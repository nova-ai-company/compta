# Corrigé E04-06 — Ventes à distance dans l'UE : le seuil de 10 000 € et le guichet OSS

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-06](../exercices/E04-06_ventes-distance-oss.md)

## 1. Analyse

**a) Le principe** (art. 258 A et 259 D CGI). Les ventes à distance intracommunautaires de biens (biens expédiés par le vendeur à des **non-assujettis** d'un autre État membre) sont taxables **dans l'État d'arrivée**. Par exception, elles restent taxables **en France** si le montant total de ces ventes (et des services électroniques/télécoms B2C rendus à des clients UE) n'a pas dépassé **10 000 € HT** au cours de l'**année civile précédente** ni de l'**année en cours**. Le seuil est **communautaire** (tous pays confondus), pas par pays.

**b) Application.** 2025 : 8 700 € ≤ 10 000 € → taxation en France au début de 2026. Cumul 2026 :

| Date | Commande | HT | Cumul | |
|---|---|---|---|---|
| 30/06 | (S1) | 9 400,00 | 9 400,00 | |
| 02/07 | #10412 Espagne | 450,00 | 9 850,00 | sous le seuil → **TVA française** |
| 08/07 | #10437 Belgique | 300,00 | **10 150,00** | **franchissement** → **TVA belge** dès cette commande |

Le lieu de taxation bascule **à compter de la livraison qui fait dépasser le seuil** (cette livraison incluse) : la commande #10437 et toutes les ventes à distance suivantes sont taxables dans le pays de destination, pour le reste de 2026 **et pour toute l'année 2027** (le seuil de 2026 étant dépassé).

**c) Le guichet unique OSS** (régime de l'Union, art. 298 sexdecies F et suivants CGI) permet de déclarer et payer en France la TVA due dans les autres États membres, sans s'y immatriculer :
- inscription via l'espace professionnel ; lorsque la première vente à distance taxable à destination intervient **avant** l'inscription, l'inscription doit être faite **au plus tard le 10 du mois suivant** cette vente pour produire effet dès celle-ci : vente du 08/07 → limite le **10/08/2026** ; inscription le 06/08 ✔ ;
- **déclaration trimestrielle** en euros, par État membre et par taux, déposée et payée **au plus tard le dernier jour du mois suivant le trimestre** (Q3 2026 : **31/10/2026**) — une déclaration « néant » est due si aucune vente ;
- conservation des registres pendant **10 ans** ;
- corrections des trimestres antérieurs : sur une déclaration OSS ultérieure (rubrique de correction de la période concernée).

**d) Sur la CA3 française**, ces ventes figurent, pour information, en ligne **E3** « Ventes à distance taxables dans un autre État membre au profit des personnes non assujetties » (base HT), sans TVA française.

**e) Le retour allemand** (septembre, commande d'août) se déduit des ventes allemandes du trimestre (même trimestre de déclaration OSS). S'il avait concerné une vente d'un trimestre **déjà déclaré**, il aurait fallu le traiter en correction de ce trimestre sur une déclaration OSS ultérieure.

**f) Vestali.** Les ventes belges de juillet-août (après le 08/07) ont été taxées à 20 % en France : la TVA française n'était **pas due**, la TVA belge l'est. Correction : (1) déclarer la TVA belge sur l'OSS du T3 ; (2) récupérer la TVA française versée à tort via la CA3 suivante (ligne 21 « autre TVA à déduire », avec une note explicative, ou par réclamation).

## 2. Calculs

**Ventes du site (08/07 – 30/09) — ventilation HT/TVA au taux de destination**

| Pays | Taux | TTC | HT | TVA |
|---|---|---|---|---|
| Belgique | 21 % | 6 050,00 | 5 000,00 | 1 050,00 |
| Allemagne (brut) | 19 % | 4 760,00 | 4 000,00 | 760,00 |
| Allemagne — retour | 19 % | – 476,00 | – 400,00 | – 76,00 |
| Espagne | 21 % | 1 815,00 | 1 500,00 | 315,00 |
| Italie | 22 % | 1 220,00 | 1 000,00 | 220,00 |
| Pays-Bas | 21 % | 968,00 | 800,00 | 168,00 |

**Vestali — Belgique**

| Période | TTC | HT (21 %) | TVA BE | TVA FR déclarée à tort |
|---|---|---|---|---|
| Juillet–août | 2 420,00 | 2 000,00 | 420,00 | 403,33 (HT FR 2 016,67) |
| Septembre (corrigé en E03-04) | 1 320,00 | 1 090,91 | 229,09 | — |

**Déclaration OSS — 3e trimestre 2026**

| État de consommation | Taux | Base HT | TVA due |
|---|---|---|---|
| Belgique | 21 % | 8 090,91 (5 000,00 + 2 000,00 + 1 090,91) | 1 699,09 |
| Allemagne | 19 % | 3 600,00 | 684,00 |
| Espagne | 21 % | 1 500,00 | 315,00 |
| Italie | 22 % | 1 000,00 | 220,00 |
| Pays-Bas | 21 % | 800,00 | 168,00 |
| **Total** | | **14 990,91** | **3 086,09** |

À déposer et payer au plus tard le **31/10/2026**.

**CA3 françaises** : ligne E3 = bases HT des ventes à distance taxables à destination, mois par mois (total T3 : 14 990,91 €). Régularisation Vestali : **403,33 €** à récupérer (ligne 21 de la CA3 de septembre ou d'octobre, avec mention de la période d'origine). La commande #10412 (02/07) reste taxée en France : 450 € HT, 90 € de TVA, ligne A1 / 08 de juillet.

## 3. Écritures comptables

Comptes : 4671 « Shopify Payments / Stripe » (encaissements du site) ; 7071 ventes France ; 7072 ventes à distance UE ; 445711 à 445715 « TVA collectée OSS » par pays (BE, DE, ES, IT, NL).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/07/2026 | VT | 4671 | Shopify Payments | Commande #10412 Espagne (sous le seuil) | 540,00 | |
| 02/07/2026 | VT | 7071 | Ventes de marchandises France | Commande #10412 | | 450,00 |
| 02/07/2026 | VT | 44571 | TVA collectée 20 % | Commande #10412 | | 90,00 |
| 30/09/2026 | VT | 4671 | Shopify Payments | Ventes UE OSS T3 (récapitulatif) | 14 813,00 | |
| 30/09/2026 | VT | 7072 | Ventes à distance UE (OSS) | Ventes UE OSS T3 | | 12 300,00 |
| 30/09/2026 | VT | 445711 à 445715 | TVA collectée OSS (BE 1 050 ; DE 760 ; ES 315 ; IT 220 ; NL 168) | Ventes UE OSS T3 | | 2 513,00 |
| 30/09/2026 | VT | 7072 | Ventes à distance UE (OSS) | Retour Allemagne | 400,00 | |
| 30/09/2026 | VT | 445712 | TVA collectée OSS – Allemagne | Retour Allemagne | 76,00 | |
| 30/09/2026 | VT | 4671 | Shopify Payments | Remboursement retour Allemagne | | 476,00 |
| 30/09/2026 | OD | 7071 | Ventes de marchandises France | Reclassement Vestali BE juillet-août | 2 016,67 | |
| 30/09/2026 | OD | 44571 | TVA collectée 20 % | TVA FR non due – Vestali BE juil.-août (ligne 21) | 403,33 | |
| 30/09/2026 | OD | 7072 | Ventes à distance UE (OSS) | Vestali BE juillet-août | | 2 000,00 |
| 30/09/2026 | OD | 445711 | TVA collectée OSS – Belgique | Vestali BE juillet-août 21 % | | 420,00 |
| 31/10/2026 | BQ | 445711 à 445715 | TVA collectée OSS (BE 1 699,09 ; DE 684 ; ES 315 ; IT 220 ; NL 168) | Paiement déclaration OSS T3 2026 | 3 086,09 | |
| 31/10/2026 | BQ | 512 | Banque | Paiement déclaration OSS T3 2026 | | 3 086,09 |
| | | | | **Totaux** | **21 335,09** | **21 335,09** |

Contrôle des comptes OSS après paiement : BE : 1 050,00 + 420,00 + 229,09 (E03-04) – 1 699,09 = 0 ✔ ; DE : 760 – 76 – 684 = 0 ✔ ; ES, IT, NL soldés ✔.

## 4. Points d'attention / pièges

- **Seuil communautaire** : on additionne tous les pays ; ne pas raisonner « 10 000 € par pays ».
- **Date de bascule** : la vente qui fait franchir le seuil est déjà taxable à destination.
- **Année suivante** : le dépassement en 2026 impose la taxation à destination pour toute l'année 2027.
- **Option** : Mode & Co aurait pu opter pour la taxation à destination dès le premier euro (option valable deux années civiles) — utile pour simplifier quand on est proche du seuil.
- **OSS ≠ stocks à l'étranger** : si Mode & Co stockait des marchandises dans un entrepôt allemand (ou via un programme logistique de marketplace), elle devrait s'immatriculer en Allemagne pour les ventes au départ de ce stock et déclarer des transferts de stocks.
- **Ventes B2B** : un client professionnel UE avec numéro valide → livraison intracommunautaire exonérée (F2), hors OSS.
- **Frais de port** facturés : même taux et même pays que les biens.
- **Taux** : vérifier les taux de chaque État à chaque déclaration (certains pays ont des taux réduits pour certains vêtements d'enfants, etc.).

## 5. Ce qu'un senior ferait en plus

**Réponse à Inès sur les prix :**
> Avec un prix TTC unique dans toute l'UE, votre marge HT varie selon le pays : pour un article à 60 € TTC, vous encaissez 50,00 € HT en France (20 %), 50,42 € en Allemagne (19 %), 49,59 € en Belgique (21 %) et 49,18 € en Italie (22 %). L'écart est faible (moins de 2 %). Vous pouvez garder un prix unique (plus simple pour vos clients) ou ajuster vos prix par pays dans Shopify. En revanche, il faut absolument activer la TVA du pays de destination sur Vestali.

**Contrôles mis en place** : tableau mensuel des ventes UE par pays (site + marketplaces) rapproché des comptes 7072 et 4457x OSS ; échéancier OSS (31/01, 30/04, 31/07, 31/10) dans l'outil de suivi du cabinet ; vérification trimestrielle des paramétrages fiscaux des plateformes.

## 6. Références

- CGI : art. 258 A (ventes à distance intracommunautaires), art. 259 D (seuil de 10 000 €), art. 298 sexdecies F et suivants (guichet unique — régime de l'Union).
- Directive 2006/112/CE : art. 33 et 59 quater ; règlement d'exécution (UE) n° 282/2011 (modalités OSS).
- BOFiP : TVA-CHAMP (ventes à distance) ; TVA-DECLA (guichet unique OSS).
- Notice de la déclaration 3310-CA3 (ligne E3).
