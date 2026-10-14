# Corrigé E03-04 — Le relevé de reversement de la marketplace

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-04](../exercices/E03-04_releve-marketplace.md)

## 1. Analyse

**a) La marketplace est un intermédiaire d'encaissement, pas le client.** Les clients de Mode & Co sont les acheteurs finaux. Vestali encaisse le prix **pour le compte** de Mode & Co, prélève sa commission (qui est une **charge** de Mode & Co, avec TVA déductible, puisque Vestali facture une prestation de services) et reverse le solde. Le virement est donc un **net de trésorerie**, résultat de quatre flux à comptabiliser séparément :
1. les ventes brutes (CA + TVA collectée) ;
2. les remboursements (annulation de ventes) ;
3. les frais de la plateforme (charges + TVA déductible) ;
4. les mouvements de réserve (créance sur la plateforme).

Comptabiliser le net en ventes, comme le faisait l'ancien comptable, revient à **minorer le CA**, **omettre la TVA déductible** sur les commissions, et à déclarer une **TVA collectée fausse**. En outre, les marketplaces transmettent à l'administration les données de leurs vendeurs : l'écart serait immédiatement visible.

**b) Le seuil des ventes à distance est dépassé.** Depuis le 08/07/2026, les ventes de biens expédiés par Mode & Co à des **particuliers** établis dans un autre État membre sont taxables **dans l'État de destination** (art. 258 A et 259 D CGI). Les 14 commandes livrées en Belgique en septembre doivent supporter la **TVA belge à 21 %**, déclarée via le **guichet unique OSS** (voir M04, E04-06), et non la TVA française.

Vestali n'agit pas ici comme « fournisseur présumé » (ce régime ne vise que les vendeurs établis hors UE ou les importations de faible valeur) : c'est **Mode & Co** qui reste redevable de la TVA sur ses ventes.

**c) Le prix TTC payé par l'acheteur ne change pas** (prix affiché unique) : c'est la ventilation HT/TVA qui change. Avec un taux de 21 % au lieu de 20 %, le HT encaissé par Mode & Co **diminue** légèrement : la marge baisse. C'est un choix commercial à faire en connaissance de cause (prix TTC différenciés par pays ou non).

## 2. Calculs

**Ventilation des ventes**

| Flux | TTC | Taux | HT | TVA |
|---|---|---|---|---|
| Commandes France | 17 160,00 | 20 % FR | 14 300,00 | 2 860,00 |
| Commandes Belgique | 1 320,00 | **21 % BE** | 1 090,91 | 229,09 |
| Frais de port France | 672,00 | 20 % FR | 560,00 | 112,00 |
| **Total ventes** | **19 152,00** | | **15 950,91** | **3 201,09** |
| Retours France | – 2 160,00 | 20 % FR | – 1 800,00 | – 360,00 |
| **Net des retours** | **16 992,00** | | **14 150,91** | **2 841,09** |

**CA HT réel de septembre sur Vestali** : 14 300,00 + 1 090,91 + 560,00 – 1 800,00 = **14 150,91 €** (dont 13 590,91 € de marchandises — 707 — et 560,00 € de port — 7085).

**Incidence de la correction belge** : avec la TVA française, la vente belge aurait donné HT 1 100,00 € / TVA 220,00 €. Avec la TVA belge : HT 1 090,91 € / TVA 229,09 €. Coût pour Mode & Co : **9,09 €** de marge sur le mois — et surtout une TVA française de 220 € **non due** en France, et une TVA belge de 229,09 € **due** via l'OSS.

**Frais Vestali**

| Élément | HT | TVA | TTC |
|---|---|---|---|
| Commission 15 % × 19 152,00 | 2 872,80 | 574,56 | 3 447,36 |
| Remboursement de commission 15 % × 2 160,00 | – 324,00 | – 64,80 | – 388,80 |
| Abonnement Vendeur Pro | 39,00 | 7,80 | 46,80 |
| **Net des frais** | **2 587,80** | **517,56** | **3 105,36** |

**Reconstitution du versement** : 19 152,00 – 2 160,00 – 3 447,36 + 388,80 – 46,80 – 500,00 + 450,00 = **13 836,64 €** ✔ (= virement reçu).

## 3. Écritures comptables

Comptes utilisés : **4671 Vestali – compte vendeur**, **4672 Vestali – réserve de sécurité**, **445711 TVA collectée OSS – Belgique** (subdivision de 4457 dédiée à l'OSS, par pays).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | MKT | 4671 | Vestali – compte vendeur | RV-2026-09 ventes brutes | 19 152,00 | |
| 30/09/2026 | MKT | 7071 | Ventes de marchandises France | RV-2026-09 ventes FR | | 14 300,00 |
| 30/09/2026 | MKT | 7072 | Ventes à distance UE (OSS) | RV-2026-09 ventes BE | | 1 090,91 |
| 30/09/2026 | MKT | 7085 | Ports et frais accessoires facturés | RV-2026-09 port | | 560,00 |
| 30/09/2026 | MKT | 44571 | TVA collectée 20 % | RV-2026-09 (2 860 + 112) | | 2 972,00 |
| 30/09/2026 | MKT | 445711 | TVA collectée OSS – Belgique | RV-2026-09 ventes BE 21 % | | 229,09 |
| 30/09/2026 | MKT | 7071 | Ventes de marchandises France | RV-2026-09 retours | 1 800,00 | |
| 30/09/2026 | MKT | 44571 | TVA collectée 20 % | RV-2026-09 retours | 360,00 | |
| 30/09/2026 | MKT | 4671 | Vestali – compte vendeur | RV-2026-09 retours | | 2 160,00 |
| 30/09/2026 | MKT | 622 | Rémunérations d'intermédiaires (commissions) | FV-2026-09 commission | 2 872,80 | |
| 30/09/2026 | MKT | 44566 | TVA déductible sur ABS | FV-2026-09 commission | 574,56 | |
| 30/09/2026 | MKT | 4671 | Vestali – compte vendeur | FV-2026-09 commission | | 3 447,36 |
| 30/09/2026 | MKT | 4671 | Vestali – compte vendeur | FV-2026-09 remb. commission | 388,80 | |
| 30/09/2026 | MKT | 622 | Rémunérations d'intermédiaires | FV-2026-09 remb. commission | | 324,00 |
| 30/09/2026 | MKT | 44566 | TVA déductible sur ABS | FV-2026-09 remb. commission | | 64,80 |
| 30/09/2026 | MKT | 628 | Charges externes diverses (abonnement plateforme) | Abonnement Vendeur Pro 09/2026 | 39,00 | |
| 30/09/2026 | MKT | 44566 | TVA déductible sur ABS | Abonnement Vendeur Pro | 7,80 | |
| 30/09/2026 | MKT | 4671 | Vestali – compte vendeur | Abonnement Vendeur Pro | | 46,80 |
| 30/09/2026 | MKT | 4672 | Vestali – réserve de sécurité | Constitution réserve 09/2026 | 500,00 | |
| 30/09/2026 | MKT | 4671 | Vestali – compte vendeur | Constitution réserve 09/2026 | | 500,00 |
| 30/09/2026 | MKT | 4671 | Vestali – compte vendeur | Libération réserve 08/2026 | 450,00 | |
| 30/09/2026 | MKT | 4672 | Vestali – réserve de sécurité | Libération réserve 08/2026 | | 450,00 |
| 05/10/2026 | BQ | 512 | Banque | Virement Vestali RV-2026-09 | 13 836,64 | |
| 05/10/2026 | BQ | 4671 | Vestali – compte vendeur | Virement Vestali RV-2026-09 | | 13 836,64 |
| | | | | **Totaux** | **39 981,60** | **39 981,60** |

Remarques :
- Les opérations du relevé sont datées de la **période** (septembre) — en pratique, on peut comptabiliser commande par commande via un connecteur, mais le relevé mensuel suffit s'il est détaillé et archivé.
- Le compte 4671 peut être remplacé par un 411 « Vestali » pour les ventes et un 401 « Vestali » pour les commissions avec compensation : l'essentiel est le **brut** et le **rapprochement**.

## 4. Points d'attention / pièges

- **Contrôle du 4671** : mouvements débit 19 152,00 + 388,80 + 450,00 = 19 990,80 ; crédit 2 160,00 + 3 447,36 + 46,80 + 500,00 + 13 836,64 = 19 990,80 → **solde nul** après le versement ✔.
- **Compte de réserve 4672** : il augmente de 50,00 € sur le mois (500 constitués – 450 libérés). Son solde total doit être rapproché de l'espace vendeur Vestali (rubrique « réserve ») à chaque clôture : c'est une **créance** de Mode & Co.
- **Les retours** réintègrent le stock (inventaire au 31/12) ; vérifier le délai de retour pour estimer, à la clôture, une éventuelle **provision pour retours** sur les ventes de décembre.
- **Commission** : sa base est le total encaissé, frais de port compris ; c'est conforme au relevé.
- **Facture de commission** : Vestali étant une société française, sa facture FV-2026-09-77120 est une **facture électronique** à recevoir via la PA de Mode & Co depuis le 01/09/2026 : la TVA déductible de 517,56 € n'est récupérable qu'avec cette facture, pas avec le relevé.
- **TVA française déjà déclarée ?** Si la CA3 de juillet ou d'août a intégré des ventes belges à 20 % postérieures au 08/07, il faut les corriger (régularisation sur la CA3 suivante et déclaration OSS des trimestres concernés).

## 5. Ce qu'un senior ferait en plus

**Message à Inès :**
> Bonjour Inès, le virement de 13 836,64 € est ce qui reste après les remboursements, la commission et la réserve de Vestali. Votre CA HT de septembre sur Vestali est de 14 150,91 €, et vous récupérez 517,56 € de TVA sur les frais Vestali. Point urgent : depuis le 8 juillet, vos ventes aux particuliers belges doivent être taxées à la TVA belge (21 %), déclarée sur le guichet OSS. Vestali les taxe encore à 20 % français : merci d'activer l'option « TVA du pays de destination » dans votre espace vendeur aujourd'hui même (et de vérifier vos prix TTC par pays). Nous régularisons juillet à septembre.

**Contrôles mensuels à mettre en place :**
1. Rapprochement **relevé Vestali / compte 4671** (solde nul après versement) et **réserve / compte 4672**.
2. Rapprochement des **commandes** (back-office) / ventes du relevé / sorties de stock.
3. Ventilation des ventes **par pays de livraison** et suivi du compteur OSS.
4. Réception de la facture de commission (format électronique) et lettrage.
5. Taux de commission effectif (frais / ventes) comparé au contrat (15 %).
6. Cohérence annuelle : CA comptable Vestali = CA déclaré par la plateforme à l'administration.

## 6. Références

- CGI : art. 256 (opérations imposables), art. 258 A et 259 D (ventes à distance intracommunautaires, seuil de 10 000 €), art. 298 sexdecies F et suivants (guichet unique OSS), art. 271 (droit à déduction), art. 242 nonies A ann. II (mentions des factures).
- PCG : comptes 467, 622, 7071/7072, 7085, 4457x, 44566.
- BOFiP : TVA-CHAMP (ventes à distance et plateformes facilitant les ventes).
