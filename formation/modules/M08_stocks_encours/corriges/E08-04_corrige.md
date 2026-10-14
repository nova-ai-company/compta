# Corrigé E08-04 — Dépréciation des collections démodées de Mode & Co

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-04](../exercices/E08-04_depreciation-collections-mode-co.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — La règle

À la clôture, chaque élément du stock est comparé à sa **valeur actuelle**. Pour un stock destiné à être vendu, la valeur actuelle est la **valeur nette de réalisation (VNR)** :

> **VNR = prix de vente estimé – coûts estimés nécessaires pour réaliser la vente** (ici : frais de paiement, préparation, emballage, port non refacturé)

Si **VNR < coût (CMUP)**, on déprécie la différence ; sinon, rien. La comparaison se fait **article par article** ou par **groupe homogène** (ici, la collection : mêmes saisons, mêmes canaux de vente, mêmes prix). Une dépréciation n'est jamais « forfaitaire » ni « par prudence » au-delà de la perte probable.

**Informations postérieures à la clôture** : les prix des soldes de janvier 2027 et l'offre du soldeur (datée du 15/12/2026, acceptée le 20/01/2027) **précisent la valeur** qu'avaient les collections au 31/12/2026. Ce sont des événements postérieurs **qui confirment une situation existant à la clôture** : on **doit** les utiliser. C'est même la meilleure preuve de la VNR qui soit.

### Analyse collection par collection

| Collection | Source du prix de vente | Coûts de vente | Conclusion attendue |
|---|---|---|---|
| Été 2026 | Ventes privées d'avril-mai : historique 14,50 € (2025) et 14,60 € (2026) → on retient le plus bas, **14,50 €** (prudence raisonnable) | 3 % + 2,10 € | À tester |
| AH26 | Soldes de janvier : **27,30 €** (prix le plus bas de la saison ; le reste sera vendu à un prix au moins égal) | 3 % + 2,10 € | À tester |
| AH26 défectueux | **Aucun** prix de vente (recyclage sans contrepartie) | — | **VNR = 0** |
| Été 2025 | Offre ferme du soldeur, acceptée : **3,80 €**, enlèvement à ses frais | **0** | À tester |
| AH25 | Rayon outlet en janvier : **15,90 €** | 3 % + 2,10 € | À tester |
| Fins de séries 2024 | **Don** à une association : aucun prix | — | **VNR = 0** |
| Accessoires | Prix stable **12,90 €**, rotation 4 mois | 3 % + 2,10 € | À tester |

## 2. Calculs (détaillés, chaque montant justifié)

### Question 2 — VNR et dépréciation

Frais de paiement par pièce = 3 % du prix HT, arrondi au centime.

| Collection | Qté | CMUP | Valeur brute | Prix de vente HT | Frais 3 % | Logistique | **VNR unitaire** | Écart unitaire (CMUP – VNR) | **Dépréciation** |
|---|---|---|---|---|---|---|---|---|---|
| Été 2026 | 1 850 | 11,40 | 21 090,00 | 14,50 | 0,44 | 2,10 | **11,96** | VNR > coût | **0,00** |
| AH26 | 4 200 | 16,80 | 70 560,00 | 27,30 | 0,82 | 2,10 | **24,38** | VNR > coût | **0,00** |
| AH26 défectueux | 85 | 16,80 | 1 428,00 | — | — | — | **0,00** | 16,80 | **1 428,00** |
| Été 2025 | 960 | 9,70 | 9 312,00 | 3,80 | — | — | **3,80** | 5,90 | **5 664,00** |
| AH25 | 1 340 | 14,20 | 19 028,00 | 15,90 | 0,48 | 2,10 | **13,32** | 0,88 | **1 179,20** |
| Fins de séries 2024 | 610 | 8,90 | 5 429,00 | — | — | — | **0,00** | 8,90 | **5 429,00** |
| Accessoires | 2 300 | 4,60 | 10 580,00 | 12,90 | 0,39 | 2,10 | **10,41** | VNR > coût | **0,00** |
| **Total** | **11 345** | | **137 427,00** | | | | | | **13 700,20** |

Détail des calculs :
- Été 2026 : 14,50 × 3 % = 0,435 → 0,44 ; 14,50 – 0,44 – 2,10 = 11,96 > 11,40 → pas de dépréciation (marge nette faible : 0,56 € par pièce — à surveiller) ;
- AH26 : 27,30 × 3 % = 0,819 → 0,82 ; 27,30 – 0,82 – 2,10 = 24,38 > 16,80 ;
- Été 2025 : (9,70 – 3,80) × 960 = 5,90 × 960 = 5 664,00 € ;
- AH25 : 15,90 × 3 % = 0,477 → 0,48 ; 15,90 – 0,48 – 2,10 = 13,32 ; (14,20 – 13,32) × 1 340 = 0,88 × 1 340 = 1 179,20 € ;
- Accessoires : 12,90 × 3 % = 0,387 → 0,39 ; 12,90 – 0,39 – 2,10 = 10,41 > 4,60 ;
- AH26 défectueux : 85 × 16,80 = 1 428,00 € ; fins de séries : 610 × 8,90 = 5 429,00 €.

**Dépréciation totale au 31/12/2026 : 13 700,20 €** ; valeur nette du stock : 137 427,00 – 13 700,20 = **123 726,80 €**.

### Variation de stock et mouvement de la dépréciation

| | Montant |
|---|---|
| Stock initial 37 | 168 900,00 € |
| Stock final 37 (brut) | 137 427,00 € |
| **Variation 6037 = SI – SF** | **31 473,00 €** (débitrice : le stock a baissé) |
| Reprise de la dépréciation 2025 (7817) | 6 800,00 € |
| Dotation 2026 (6817) | 13 700,20 € |
| **Charge nette de dépréciation** | **6 900,20 €** |

### Question 4 — La proposition d'Inès

| Élément | Calcul | Montant |
|---|---|---|
| 30 % sur AH26 | 70 560,00 × 30 % | 21 168,00 € |
| 50 % sur les collections de plus d'un an (Été 2025, AH25, fins de séries 2024) | (9 312,00 + 19 028,00 + 5 429,00) × 50 % = 33 769,00 × 50 % | 16 884,50 € |
| **Total proposé** | | **38 052,50 €** |
| Dépréciation justifiée | | 13 700,20 € |
| **Excédent non justifié** | | **24 352,30 €** |

L'IS « économisé » serait de 24 352,30 × 15 % = 3 652,85 € à 24 352,30 × 25 % = 6 088,08 € selon la tranche — en apparence seulement :
- **comptablement** : la collection AH26 se vend 27,30 € en plein soldes pour un coût de 16,80 € : elle n'a **perdu aucune valeur**. La déprécier, c'est créer une **provision occulte** qui fausse l'image fidèle (art. L. 123-14 C. com.) — et sous-déprécier les fins de séries (50 % au lieu de 100 %) est tout aussi faux dans l'autre sens ;
- **fiscalement** : une dépréciation n'est déductible que si elle correspond à une **perte de valeur probable, nettement précisée** et justifiée (CGI art. 39-1-5°). Un forfait non justifié par des données propres à l'entreprise est **réintégré** en cas de contrôle, avec intérêts de retard, voire majoration pour manquement délibéré ;
- **économiquement** : même admise, elle serait **reprise** l'an prochain quand la collection sera vendue : simple décalage d'impôt, au prix d'un risque fiscal réel.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6037 | Variation des stocks de marchandises | Annulation stock initial au 31/12/2025 | 168 900,00 | |
| 31/12/2026 | OD | 37 | Stocks de marchandises | Annulation stock initial au 31/12/2025 | | 168 900,00 |
| 31/12/2026 | OD | 37 | Stocks de marchandises | Stock final au 31/12/2026 (CMUP, inventaire signé) | 137 427,00 | |
| 31/12/2026 | OD | 6037 | Variation des stocks de marchandises | Stock final au 31/12/2026 | | 137 427,00 |
| 31/12/2026 | OD | 397 | Dépréciations des stocks de marchandises | Reprise dépréciation au 31/12/2025 | 6 800,00 | |
| 31/12/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise dépréciation au 31/12/2025 | | 6 800,00 |
| 31/12/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation stocks au 31/12/2026 (état détaillé par collection) | 13 700,20 | |
| 31/12/2026 | OD | 397 | Dépréciations des stocks de marchandises | Dépréciation stocks au 31/12/2026 | | 13 700,20 |
| | | | | **Totaux** | **326 827,20** | **326 827,20** |

Après écritures : 37 = 137 427,00 € ; 397 = 13 700,20 € ; stock net au bilan = 123 726,80 €.

## 4. Points d'attention / pièges

- **VNR « nette »** : oublier les coûts de vente (3 % + 2,10 €) conduit, sur l'AH25, à conclure qu'il n'y a pas de dépréciation (15,90 > 14,20) alors qu'il en faut une.
- **Pas de compensation entre collections** : la plus-value latente de l'AH26 ne compense pas la moins-value de l'Été 2025. On déprécie par groupe homogène.
- **Été 2026** : pas de dépréciation, mais la marge nette attendue est de 0,56 € par pièce. Si les ventes privées d'avril 2027 se faisaient en dessous de 13,92 € environ (0,97 × prix – 2,10 < 11,40), une dépréciation aurait été nécessaire : la donnée se surveille, elle ne s'invente pas.
- **Retours défectueux** : ils sont **dans le stock** (inventaire physique) mais ne valent rien : 100 % de dépréciation (ou sortie de l'inventaire si l'on préfère, la preuve du recyclage étant conservée).
- **Reprise + dotation** : présentation qui permet de suivre le relevé des provisions (tableau 2056) ; le solde net (6 900,20 €) est le même que si l'on avait passé seulement la différence.
- **Fiscalement**, la dépréciation de 13 700,20 € est déductible (justifiée collection par collection, documentée par des prix réels) ; elle figure sur le relevé des provisions.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

### Question 5 — Loi AGEC et don

- La loi « anti-gaspillage pour une économie circulaire » (AGEC) **interdit en principe la destruction des invendus non alimentaires neufs**, dont les vêtements : ils doivent être **réemployés** (don, vente à un soldeur) ou **recyclés**. Les deux voies choisies par Inès (recyclage textile pour les pièces défectueuses, don pour les fins de séries) sont conformes. Pas de mise à la benne !
- Le **don** des 610 fins de séries à une association reconnue d'utilité publique ouvre droit à la **réduction d'impôt mécénat** (CGI art. 238 bis) : 60 % de la valeur du don, retenue au **coût de revient** des biens (ici, au plus 5 429,00 € → réduction de l'ordre de 3 257,40 €), dans la limite du plafond en vigueur (*plafond et taux à vérifier chaque année*). Le don devra être sorti du stock en mars 2027 et justifié par le **reçu** de l'association.
- **TVA** : un don de biens dont la TVA a été déduite entraîne en principe une régularisation ; un dispositif de **dispense** existe pour certains dons d'invendus à des associations éligibles — conditions à vérifier (CGI et BOFiP TVA) avant mars.

### Question 6 — Arguments pour l'appel à Inès

1. « Une partie de votre stock a réellement perdu de la valeur : l'Été 2025 (offre du soldeur à 3,80 €), l'AH25 (outlet), les pièces défectueuses et les fins de séries. Nous dépréciions **13 700 €**, contre 6 800 € l'an dernier : c'est justifié, documenté et déductible. »
2. « En revanche, l'AH26 s'est vendue à 27,30 € en plein soldes pour un coût de 16,80 € : elle n'a pas perdu de valeur. La déprécier serait inexact, et l'administration la réintégrerait. »
3. « Une dépréciation est un **décalage** : ce que vous déduisez cette année, vous le reprenez l'an prochain quand vous vendez. Le gain d'IS est temporaire, le risque de redressement ne l'est pas. »
4. « Le vrai levier fiscal, c'est le **don** des fins de séries : une réduction d'impôt d'environ 3 200 € (sous réserve des plafonds), en plus de l'image solidaire de la marque. »
5. « Pour l'avenir : suivez le **taux d'écoulement** de chaque collection à 6 et 12 mois, et prévoyez les déstockages plus tôt — chaque mois de retard coûte de la valeur. »

**Documentation du dossier** : état de stock signé ; export Shopify des soldes ; offre et acceptation du soldeur ; note sur les coûts de vente ; courriel sur les retours et le don ; tableau de calcul de la dépréciation ; note de synthèse sur la position refusée (forfait), datée et validée par Hélène Ferrand.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié) : évaluation des stocks à la clôture (comparaison du coût et de la valeur actuelle) ; dépréciations des actifs circulants (comptes 397, 6817, 7817) ; événements postérieurs à la clôture.
- Code de commerce art. L. 123-14 (image fidèle) et L. 123-20 (prudence : dépréciations constatées même en cas d'absence ou d'insuffisance de bénéfice).
- CGI art. 38-3 (stocks au coût ou au cours du jour s'il est inférieur) ; art. 39-1-5° (conditions de déduction des provisions et dépréciations) ; art. 238 bis (mécénat).
- Loi n° 2020-105 du 10 février 2020 relative à la lutte contre le gaspillage et à l'économie circulaire (AGEC) — interdiction de l'élimination des invendus non alimentaires neufs (Code de l'environnement).
