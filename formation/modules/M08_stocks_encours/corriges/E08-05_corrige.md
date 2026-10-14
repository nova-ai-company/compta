# Corrigé E08-05 — Stock de véhicules d'occasion du Garage Martin au 30/09/2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-05](../exercices/E08-05_stock-vo-garage-martin.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Les erreurs de principe de la liste de Thierry

| # | Erreur | Règle |
|---|---|---|
| 1 | **Valorisation au prix de vente affiché** (TTC de surcroît) | Un stock se valorise au **coût d'entrée** (coût d'acquisition + frais de remise en état). Le prix de vente ne sert qu'à **tester** la valeur (VNR) : il ne peut que faire **baisser** la valeur, jamais la faire monter au-dessus du coût. Valoriser au prix affiché, c'est comptabiliser la marge avant la vente |
| 2 | **BMW Série 1 en dépôt-vente** incluse | Le véhicule appartient à M. Lacroix (mandat, pièce 4) : **hors stock** du garage. Le garage ne constatera qu'une **commission** (8 %) le jour de la vente |
| 3 | **3008 invendu depuis 11 mois** : « on verra l'an prochain » | Indice de perte de valeur **existant à la clôture** (décision de vente aux enchères prise le 25/09) : dépréciation **au 30/09/2026** |
| 4 | **Acompte C3** passé en vente | Au 30/09, la C3 n'est pas livrée (livraison le 05/10) : pas de vente. L'acompte est une **dette** envers la cliente (4191) |
| 5 | Pas de prise en compte de la **TVA sur la marge** ni des **coûts de vente** | La VNR est un montant **net** : prix de vente – TVA sur la marge – coûts pour achever et vendre |

### Les véhicules : biens identifiables

Un VO est un bien **identifiable** (numéro de série, immatriculation) : on retient son **coût réel individuel**, jamais un CMUP. Le coût comprend :
- le **prix d'achat** : TTC payé au particulier (pas de TVA récupérable sur un achat à un particulier) ; **HT** pour la Golf achetée à un professionnel (TVA déduite) ;
- les **frais de remise en état** : pièces au coût d'achat HT + main-d'œuvre **au coût de revient** de l'atelier (42 €/h), **jamais au taux facturé** aux clients (78 €/h), qui inclut la marge du garage.

> Le garage suit les VO en marchandises (37, variation 6037) : la main-d'œuvre interne, comptabilisée en charges de personnel, est « réintégrée » dans le stock via la variation de stock. Cette méthode doit être **permanente** d'un exercice à l'autre.

### La VNR d'un VO vendu sous le régime de la marge

Pour un VO acheté à un particulier, le garage revendra sous le **régime de la marge** (CGI art. 297 A) : il devra reverser à l'État une TVA égale à 20/120 de (prix de vente TTC – prix d'achat). Cette TVA est un **coût de la vente** : ce que le garage encaissera réellement, c'est le prix TTC **moins** cette TVA. Elle vient donc **réduire la VNR**. Si la marge est **négative**, la TVA est **nulle** (et la perte de marge ne s'impute pas sur les autres ventes).

Pour un VO vendu sous le **régime normal** (Golf), le prix de vente à retenir est le prix **HT** (la TVA de 20 % sur le prix total est entièrement reversée).

## 2. Calculs (détaillés, chaque montant justifié)

### Question 2 — Coût d'entrée

| Véhicule | Prix d'achat | Pièces | Main-d'œuvre (h × 42 €) | **Coût d'entrée** |
|---|---|---|---|---|
| Peugeot 3008 | 13 800,00 | 1 150,00 | 10 × 42 = 420,00 | **15 370,00** |
| Renault Clio V | 10 900,00 | 420,00 | 4 × 42 = 168,00 | **11 488,00** |
| Dacia Sandero | 5 200,00 | — | — | **5 200,00** |
| Peugeot 308 | 11 500,00 | 640,00 | 6 × 42 = 252,00 | **12 392,00** |
| VW Golf 8 (HT) | 14 200,00 | — | — | **14 200,00** |
| Citroën C3 | 6 900,00 | 380,00 | 3 × 42 = 126,00 | **7 406,00** |
| BMW Série 1 (dépôt-vente) | — | — | — | **exclue** |
| **Total** | | | | **66 056,00** |

### Question 3 — VNR et dépréciation

| Véhicule | Prix de vente probable | TVA à reverser | Coûts pour achever / vendre | **VNR** | Coût | **Dépréciation** |
|---|---|---|---|---|---|---|
| 3008 (enchères) | 11 200,00 TTC | marge 11 200 – 13 800 < 0 → **0,00** | frais vendeur 6 % × 11 200 = 672,00 + convoyage 150,00 = 822,00 | **10 378,00** | 15 370,00 | **4 992,00** |
| Clio V | 10 400,00 TTC | marge 10 400 – 10 900 < 0 → **0,00** | 240,00 | **10 160,00** | 11 488,00 | **1 328,00** |
| Sandero | 4 800,00 TTC | marge 4 800 – 5 200 < 0 → **0,00** | débosselage 600,00 + 240,00 = 840,00 | **3 960,00** | 5 200,00 | **1 240,00** |
| 308 | 15 400,00 TTC | (15 400 – 11 500) × 20/120 = 3 900 / 6 = **650,00** | 240,00 | **14 510,00** | 12 392,00 | 0,00 |
| Golf (régime normal) | 19 200 / 1,20 = 16 000,00 HT | incluse (prix HT) | 240,00 | **15 760,00** | 14 200,00 | 0,00 |
| C3 (vendue le 28/09) | 8 990,00 TTC | (8 990 – 6 900) × 20/120 = 2 090 / 6 = **348,33** | 240,00 | **8 401,67** | 7 406,00 | 0,00 |
| **Total** | | | | | **66 056,00** | **7 560,00** |

Valeur nette du stock VO au 30/09/2026 : 66 056,00 – 7 560,00 = **58 496,00 €**.

Remarques :
- **Frais d'enchères** : retenus HT (la TVA sur la facture de la maison d'enchères est récupérable).
- **Sandero** : le débosselage de 600 € HT est un **coût pour achever** le bien (avant la vente) : il réduit la VNR. On ne l'ajoute pas au coût d'entrée au 30/09 : il n'est pas encore engagé.
- **308** : la VNR (14 510) reste supérieure au coût (12 392) **même après** la TVA sur la marge de 650 €. Mais faites le test sans la TVA : on aurait trouvé 15 160 — l'écart peut devenir décisif sur un véhicule à faible marge.

### Question 4 — Acompte de la C3

Au 30/09/2026, la C3 est sur le parc, non livrée (livraison le 05/10) : la vente est une vente de l'exercice 2026-2027. L'acompte de 1 000 € est une **dette** : reclassement 707 → **4191 Clients – avances et acomptes reçus sur commandes**. Pour une **livraison de biens**, l'acompte ne rend pas la TVA exigible : aucune TVA à constater sur l'acompte (la TVA sur la marge sera due à la livraison du 05/10). La C3 reste **dans le stock** au 30/09 à son coût (7 406,00 €).

### Variation de stock

| | Montant |
|---|---|
| Stock initial VO (30/09/2025) | 58 700,00 € |
| Stock final VO (30/09/2026) | 66 056,00 € |
| **Variation 6037 = SI – SF** | **– 7 356,00 €** → solde **créditeur** |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6037 | Variation des stocks de marchandises | Annulation stock VO au 30/09/2025 | 58 700,00 | |
| 30/09/2026 | OD | 37 | Stocks de marchandises – VO | Annulation stock VO au 30/09/2025 | | 58 700,00 |
| 30/09/2026 | OD | 37 | Stocks de marchandises – VO | Stock VO au 30/09/2026 (6 véhicules, coût réel — BMW en dépôt exclue) | 66 056,00 | |
| 30/09/2026 | OD | 6037 | Variation des stocks de marchandises | Stock VO au 30/09/2026 | | 66 056,00 |
| 30/09/2026 | OD | 397 | Dépréciations des stocks de marchandises | Reprise dépréciation VO au 30/09/2025 (véhicules vendus) | 2 150,00 | |
| 30/09/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise dépréciation VO au 30/09/2025 | | 2 150,00 |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation VO : 3008 4 992 / Clio 1 328 / Sandero 1 240 | 7 560,00 | |
| 30/09/2026 | OD | 397 | Dépréciations des stocks de marchandises | Dépréciation VO au 30/09/2026 | | 7 560,00 |
| 30/09/2026 | OD | 707 | Ventes de marchandises – VO | Annulation acompte C3 passé en vente (BC-26-0177) | 1 000,00 | |
| 30/09/2026 | OD | 4191 | Clients – avances et acomptes reçus sur commandes | Acompte Mme Benhamou — C3 livrée le 05/10/2026 | | 1 000,00 |
| | | | | **Totaux** | **135 466,00** | **135 466,00** |

**Sens du 6037 (question 5)** : solde **créditeur** de 7 356,00 €. Le stock de VO a **augmenté** (66 056 contre 58 700) : une partie des achats de VO de l'exercice n'a pas été « consommée » (vendue). Le 6037 créditeur vient **en diminution des charges** (achats de marchandises) — il reste au compte de résultat dans la rubrique « variation de stocks de marchandises », avec un signe négatif. Ce n'est pas un produit.

**Incidence par rapport à la liste de Thierry** : sa liste (95 970 €, sans dépréciation, acompte en vente) aurait donné un résultat supérieur de (95 970,00 – 66 056,00) + (7 560,00 – 2 150,00) + 1 000,00 = 29 914,00 + 5 410,00 + 1 000,00 = **36 324,00 €**.

## 4. Points d'attention / pièges

- **Ne jamais valoriser au prix de vente** : c'est l'erreur la plus fréquente chez les négociants en VO, et la plus coûteuse en cas de contrôle (marge anticipée, IS payé trop tôt… ou stock artificiellement gonflé pour la banque).
- **Main-d'œuvre interne au coût de revient** (42 €/h) : au taux facturé (78 €/h), on stockerait la marge de l'atelier.
- **TVA sur la marge** : à déduire du prix de vente pour la VNR ; **nulle** si la marge est négative (Clio, Sandero, 3008). Ne pas calculer une TVA « négative ».
- **Golf au régime normal** : comparez des montants **HT** (coût HT / prix de vente HT).
- **Dépôt-vente** : la BMW doit être identifiée physiquement lors du comptage (étiquette « dépôt ») ; la tenue d'un registre des dépôts est recommandée. Si la vente intervient, le garage facture sa commission (TVA sur la commission) et reverse le prix au mandant.
- **Ancienneté > 6 mois** : la Clio (10 mois) et le 3008 (11 mois) sont les deux véhicules à tester en priorité ; la dépréciation ne se calcule pas au forfait (« 10 % par trimestre d'ancienneté ») mais à partir d'une VNR **documentée** (offres reçues, cote, estimation de la maison d'enchères).
- **Informations postérieures** : l'adjudication du 22/10/2026 sera connue avant l'arrêté des comptes : si le prix réel diffère sensiblement de l'estimation (11 200 €), **ajustez** la dépréciation.
- **Sinistre grêle** : sans indemnité d'assurance, la perte s'exprime dans la VNR ; s'il y avait eu une indemnité acquise à la clôture, on l'aurait constatée en produit à recevoir.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Message à Thierry :**

> Bonjour Thierry,
>
> Merci pour la liste du parc. Pour le bilan, nous devons valoriser les VO à ce qu'ils vous ont **coûté** (prix d'achat + pièces + heures d'atelier à leur coût, pas au tarif client), et non au prix affiché : la marge ne se compte qu'à la vente.
> - La **BMW** de M. Lacroix ne vous appartient pas (dépôt-vente) : elle sort de la liste.
> - Votre stock VO au 30/09 vaut **66 056 €** au coût.
> - Le **3008** ne peut pas attendre l'an prochain : vous avez décidé le 25/09 de l'envoyer aux enchères, où il devrait faire environ 11 200 €. La perte (près de 5 000 €) existait déjà au 30/09 : elle se constate dans ce bilan. Idem pour la **Clio** (offres à 10 400 €) et la **Sandero** grêlée : au total, 7 560 € de dépréciation.
> - L'acompte de 1 000 € sur la **C3** n'est pas encore une vente au 30/09 : la voiture a été livrée le 05/10. Nous l'avons reclassé en acompte client.
>
> Merci de nous transmettre le procès-verbal d'adjudication du 3008 dès la vente du 22/10 : nous ajusterons si le prix est différent.
>
> Conseil pour la suite : un VO qui ne part pas en 90 jours vous coûte de la trésorerie et de la valeur. Un tableau de bord « âge du parc » (date d'entrée, prix affiché, cote, offres) permettrait de décider plus tôt.
>
> Bien cordialement,

**Contrôles et documentation :**
- rapprocher la liste du parc du **livre de police** (tout VO acheté et non revendu doit être sur le parc, et inversement) ;
- vérifier que les ventes de VO de l'exercice ont toutes été **sorties** du livre de police et facturées (cut-off des dernières livraisons de septembre) ;
- conserver : mandat de dépôt-vente, bon de commande C3, offres sur la Clio, devis de débosselage, estimation de la maison d'enchères ;
- dans le cas de synthèse (bilan complet), reporter le stock net (58 496,00 €) et les dépréciations sur le relevé des provisions (2056).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié) : coût d'entrée des stocks (biens identifiables : coût individuel ; frais de remise en état) ; dépréciation à la clôture (valeur actuelle) ; comptes 37, 397, 4191, 6037, 6817, 7817.
- CGI art. 297 A et suivants (régime de la marge pour les biens d'occasion) ; art. 269 (fait générateur des livraisons de biens : la livraison).
- CGI art. 38-3 et 39-1-5° (évaluation des stocks, déduction des dépréciations) ; BOFiP, série BIC – produits et stocks.
- Code pénal et réglementation sur le registre des objets mobiliers (livre de police) tenu par les revendeurs de biens d'occasion.
