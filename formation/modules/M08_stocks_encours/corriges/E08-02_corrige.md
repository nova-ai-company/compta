# Corrigé E08-02 — Coût d'acquisition des importations et CMUP des luminaires d'Asia Trading

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-02](../exercices/E08-02_cmup-luminaires-asia-trading.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Qu'est-ce qui entre dans le coût d'acquisition ?

Le coût d'acquisition d'un stock comprend le **prix d'achat** et tous les **coûts directement attribuables** pour amener la marchandise **dans l'entrepôt**, en état d'être vendue. Le critère est simple : *ce coût aurait-il été engagé si l'on n'avait pas acheté cette marchandise, et est-il engagé **avant** son arrivée dans l'entrepôt ?*

| Élément | Retenu ? | Justification |
|---|---|---|
| Prix FOB converti au cours du jour de l'opération | **Oui** | Prix d'achat. Le cours retenu est celui de la date de l'opération (15/10/2026) ; il n'est **jamais** modifié ensuite |
| Commission de l'agent d'achat (3 %) | **Oui** (Kevin l'avait écartée) | Coût **directement attribuable** à l'achat. Le fait qu'elle soit exclue de la **valeur en douane** n'a rien à voir avec le coût comptable |
| Fret maritime + assurance | **Oui** | Transport jusqu'à l'entrepôt ; en FOB, il est à la charge de l'acheteur |
| Droits de douane | **Oui** | Taxe **non récupérable** liée à l'acquisition |
| Honoraires de dédouanement du transitaire | **Oui** (Kevin les avait écartés) | Coût directement attribuable à l'importation. « Ce n'est pas de la marchandise » n'est pas un critère : le fret non plus n'est pas de la marchandise |
| Transport Le Havre → Lyon | **Oui** | Transport jusqu'au lieu de stockage |
| Stockage de l'entrepôt d'Asia Trading | **Non** | Coût **postérieur** à l'arrivée en stock, non nécessaire au processus (pas de vieillissement, pas de transformation). Charge de la période (loyer 613) |
| Intérêts et commission du crédit documentaire | **Non** | **Frais financiers** (mode de paiement), exclus du coût d'acquisition des marchandises (661 / 627) |
| Perte de change au paiement | **Non** | Elle naît de la **dette** en devises, pas de la marchandise : **666 Pertes de change**. Le stock reste au coût historique au cours du jour de l'opération |
| TVA à l'importation (autoliquidée) | **Non** | TVA récupérable (non mentionnée par Kevin, mais erreur fréquente) |

> Peu importe que la comptabilité générale enregistre ces frais **par nature** (6241 Transports sur achats, 6222 Commissions et courtages sur achats, droits de douane en 607 ou 608 selon le paramétrage du dossier) : **la valorisation du stock les inclut**. C'est la fiche de stock qui doit être juste.

### Question 3 — Le CMUP après chaque entrée

Après chaque **entrée**, on recalcule : CMUP = (valeur du stock avant l'entrée + coût de l'entrée) ÷ (quantité avant + quantité entrée). Les **sorties** suivantes sont valorisées à ce CMUP jusqu'à la prochaine entrée. Les sorties ne modifient pas le CMUP. Le stock final est la valeur **résiduelle** de la fiche (ce qui évite de « perdre » des centimes d'arrondi).

## 2. Calculs (détaillés, chaque montant justifié)

### Question 2 — Coût des imports

| Composant | Import n° 1 (1 200 u) | Import n° 2 (1 000 u) |
|---|---|---|
| Prix FOB | 16 800 USD / 1,0800 = **15 555,56 €** | 14 500 USD / 1,0500 = **13 809,52 €** |
| Commission d'achat 3 % | 15 555,56 × 3 % = **466,67 €** | 13 809,52 × 3 % = **414,29 €** |
| Fret maritime + assurance | 1 850,00 € | 1 620,00 € |
| Valeur en douane CIF (prix + fret/assurance) | 17 405,56 € | 15 429,52 € |
| Droits de douane 4,7 % de la valeur CIF | 17 405,56 × 4,7 % = **818,06 €** | 15 429,52 × 4,7 % = **725,19 €** |
| Honoraires du transitaire | 280,00 € | 280,00 € |
| Transport Le Havre → Lyon | 640,00 € | 590,00 € |
| **Coût d'acquisition total** | **19 610,29 €** | **17 439,00 €** |
| **Coût unitaire** | 19 610,29 / 1 200 = **16,3419 €** | 17 439,00 / 1 000 = **17,4390 €** |

Détail import n° 1 : 15 555,56 + 466,67 + 1 850,00 + 818,06 + 280,00 + 640,00 = 19 610,29 €.
Détail import n° 2 : 13 809,52 + 414,29 + 1 620,00 + 725,19 + 280,00 + 590,00 = 17 439,00 €.

**Écart avec Kevin (import n° 1)** : 20 592,71 – 19 610,29 = **982,42 €** de trop, soit :
+ 1 200,00 (stockage) + 310,00 (crédit documentaire) + 219,09 (perte de change) – 466,67 (commission oubliée) – 280,00 (transitaire oublié) = 982,42 € ✔

Vérification de la perte de change : paiement à 16 800 / 1,0650 = 15 774,65 € ; 15 774,65 – 15 555,56 = 219,09 € → **666**.

### Question 3 — Fiche de stock au CMUP après chaque entrée

| Date | Opération | Qté entrée | Qté sortie | Coût unitaire | Valeur mouvement | Stock qté | Stock valeur | CMUP |
|---|---|---|---|---|---|---|---|---|
| 01/10 | Stock initial | | | 18,4000 | | 400 | 7 360,00 | 18,4000 |
| 22/11 | Import n° 1 | 1 200 | | 16,3419 | 19 610,29 | 1 600 | 26 970,29 | **16,8564** |
| 26/11 | Vente BL 2611 | | 500 | 16,8564 | 8 428,20 | 1 100 | 18 542,09 | 16,8564 |
| 03/12 | Vente BL 0312 | | 700 | 16,8564 | 11 799,48 | 400 | 6 742,61 | 16,8564 |
| 18/12 | Import n° 2 | 1 000 | | 17,4390 | 17 439,00 | 1 400 | 24 181,61 | **17,2726** |
| 21/12 | Vente BL 2112 | | 900 | 17,2726 | 15 545,34 | 500 | **8 636,27** | 17,2726 |

Calculs :
- CMUP au 22/11 : 26 970,29 / 1 600 = 16,856431… → **16,8564 €** ;
- sorties : 500 × 16,8564 = 8 428,20 € ; 700 × 16,8564 = 11 799,48 € ;
- CMUP au 18/12 : (6 742,61 + 17 439,00) / 1 400 = 24 181,61 / 1 400 = 17,272578… → **17,2726 €** ;
- sortie : 900 × 17,2726 = 15 545,34 € ;
- **stock final = 24 181,61 – 15 545,34 = 8 636,27 €** (500 × 17,2726 = 8 636,30 € : l'écart de 0,03 € est un arrondi ; on retient la valeur résiduelle de la fiche).

Contrôle : coût des sorties du trimestre = 8 428,20 + 11 799,48 + 15 545,34 = 35 773,02 € ; SI + entrées – sorties = 7 360,00 + 19 610,29 + 17 439,00 – 35 773,02 = 8 636,27 € ✔

### Question 4 — Comparaison des méthodes

| Méthode | Calcul | Stock final LOTUS |
|---|---|---|
| **CMUP après chaque entrée** (méthode de l'entreprise) | voir fiche | **8 636,27 €** |
| CMUP du trimestre | (7 360,00 + 19 610,29 + 17 439,00) / (400 + 1 200 + 1 000) = 44 409,29 / 2 600 = 17,0805 € ; 500 × 17,0805 | 8 540,25 € |
| FIFO (PEPS) | les 500 unités restantes proviennent de l'import n° 2 (le plus récent) : 500 × 17,4390 | 8 719,50 € |

Commentaire : en période de **hausse** du coût de revient (17,44 € pour le dernier import contre 16,34 € pour le précédent), le **FIFO** donne le stock le plus élevé (il valorise le stock aux derniers coûts) ; le CMUP de période lisse sur l'ensemble du trimestre (y compris le stock initial ancien à 18,40 €, d'où un résultat proche) ; le CMUP après chaque entrée se situe entre les deux. L'écart entre méthodes est ici faible (179,25 € au maximum) car le stock tourne vite. Asia Trading a choisi le CMUP après chaque entrée : **permanence des méthodes**, on n'en change pas.

### Stock de marchandises au 31/12/2026

| | Montant |
|---|---|
| Autres références (CMUP) | 182 340,00 € |
| LOTUS (CMUP après chaque entrée) | 8 636,27 € |
| **Stock final 37** | **190 976,27 €** |
| Stock initial 37 (31/12/2025) | 205 600,00 € |
| **Variation 6037 = SI – SF** | **14 623,73 €** (débitrice : le stock a baissé) |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6037 | Variation des stocks de marchandises | Annulation stock initial au 31/12/2025 | 205 600,00 | |
| 31/12/2026 | OD | 37 | Stocks de marchandises | Annulation stock initial au 31/12/2025 | | 205 600,00 |
| 31/12/2026 | OD | 37 | Stocks de marchandises | Stock final au 31/12/2026 (CMUP) — dont LOTUS 8 636,27 | 190 976,27 | |
| 31/12/2026 | OD | 6037 | Variation des stocks de marchandises | Stock final au 31/12/2026 (CMUP) | | 190 976,27 |
| | | | | **Totaux** | **396 576,27** | **396 576,27** |

Solde du 6037 : débiteur de 14 623,73 € — le stock a diminué, la consommation de marchandises de l'exercice (achats + 14 623,73 €) dépasse les achats.

Pour mémoire (déjà comptabilisé en cours d'exercice ou à vérifier dans la révision) : perte de change de 219,09 € au paiement du 30/11 en **666** ; intérêts et commissions du crédit documentaire en **661 / 627** ; stockage en **613**.

## 4. Points d'attention / pièges

- **Valeur en douane ≠ coût comptable** : la valeur en douane (CIF) exclut la commission d'achat, le transport après l'entrée dans l'UE et les honoraires de dédouanement ; le coût comptable les inclut. Ne recopiez pas la case 46 du DAU dans la fiche de stock.
- **Le cours de change** : celui du **jour de l'opération**, définitif pour le stock. Les écarts ultérieurs (paiement, clôture) concernent la **dette** (666 / 766, 476 / 477), jamais le stock.
- **Frais financiers** : exclus du coût d'acquisition des marchandises. L'option d'incorporation des coûts d'emprunt ne vise que les actifs nécessitant une longue période de préparation (stocks à cycle de production long), pas un achat de négoce.
- **Arrondis** : fixez une règle (CMUP à 4 décimales, valeurs au centime) et tenez-vous-y ; le stock final est la **valeur résiduelle** de la fiche.
- **Débours** : les droits de douane avancés par le transitaire sont des débours (hors TVA) ; ils sont bien un coût d'acquisition pour Asia Trading.
- **Contrôle des quantités** : la fiche de Kevin indique 500 LOTUS, l'inventaire physique aussi. En cas d'écart, c'est le **physique** qui fait foi ; l'écart (casse, erreur de livraison) s'analyse.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse à Kevin :**

> Bonjour Kevin,
>
> Merci pour la fiche LOTUS. Quelques ajustements sur le coût de l'import d'octobre :
> - la **commission de l'agent** et les **honoraires du transitaire** font bien partie du coût de vos lampes : sans eux, elles ne seraient pas dans votre entrepôt ;
> - en revanche, le **stockage** dans votre entrepôt, les **frais du crédit documentaire** et la **perte de change** ne s'ajoutent pas au stock : ce sont des charges de l'exercice (loyer, frais financiers, perte de change).
>
> Le coût réel de l'import d'octobre est de 16,34 € par lampe (et non 17,16 €), celui de novembre de 17,44 €. Au CMUP, vos 500 LOTUS valent **8 636,27 €** au 31/12.
>
> Sur le **LIFO** : cette méthode (« dernier entré, premier sorti ») est **interdite en France**, en comptabilité comme en fiscalité. En période de hausse des prix, elle réduirait artificiellement la valeur du stock et donc le résultat imposable — c'est précisément pour cela qu'elle n'est pas admise. Seuls le CMUP (votre méthode) et le FIFO sont autorisés, et on ne change pas de méthode pour optimiser un résultat.
>
> Bien cordialement,

**Contrôles et documentation :**
- dossier de travail « stocks » : pour chaque import du dernier trimestre, rapprochement facture fournisseur / DAU / facture transitaire / note de l'agent, et calcul du coût unitaire ;
- vérifier que les **autres références** ont été valorisées avec les mêmes composants (commission, honoraires) — l'erreur de Kevin est sans doute systématique ;
- proposer à Kevin un **modèle de fiche de coût d'import** (colonnes figées) à remplir à chaque arrivage ;
- vérifier la cohérence du **taux de marge** par famille de produits avec l'exercice précédent.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié) : coût d'acquisition des stocks (prix d'achat, droits de douane et taxes non récupérables, frais de transport, de manutention et autres coûts directement attribuables) ; évaluation des biens fongibles (CMUP ou FIFO) ; conversion des opérations en devises au cours du jour ; comptes 37, 6037, 666, 661.
- Code de commerce art. L. 123-17 (permanence des méthodes) et L. 123-18 (évaluation au coût d'acquisition).
- CGI art. 38-3 (évaluation des stocks) ; BOFiP, série BIC – produits et stocks (BOI-BIC-PDSTK) : la méthode LIFO n'est pas admise.
- Code des douanes de l'Union (valeur en douane, exclusion des commissions d'achat) ; tarif TARIC pour le taux de droits (à vérifier par nomenclature).
- CGI art. 1695 (autoliquidation de la TVA à l'importation) — voir module M04.
