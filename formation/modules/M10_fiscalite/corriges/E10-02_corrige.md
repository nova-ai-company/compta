# Corrigé E10-02 — Le SUV du président : amortissement excédentaire et taxes annuelles

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-02](../exercices/E10-02_vehicules-tourisme-batisseurs.md)

## 1. Analyse

- Le SUV est un **véhicule de tourisme** (genre VP, carrosserie CI, 5 places). Conséquences en cascade : TVA non récupérable (immobilisé TTC), **plafond d'amortissement** fiscal (art. 39-4 CGI), **taxes annuelles** CO₂ et polluants non déductibles, avantage en nature pour Karim.
- Avec 158 g/km en norme **WLTP**, le véhicule se situe dans la tranche **50 à 160 g/km** → plafond de **18 300 €**. **Nadia s'est trompée** : elle a appliqué le plafond de 9 900 € avec l'ancien seuil de 130 g/km, qui concernait les véhicules mesurés en norme **NEDC**. Pour les véhicules WLTP (immatriculés depuis 2021), le plafond de 9 900 € ne s'applique qu'au-delà de 160 g/km.
- Les taxes annuelles sont dues pour la période d'affectation (prorata en jours) et se déclarent **l'année suivante** ; la charge de 2026 est donc une **charge à payer** au 31/12/2026.
- Le pick-up : le libellé « CTTE » sur la carte grise ne suffit pas. Le CIBS range parmi les véhicules de tourisme les **camionnettes pick-up comportant au moins 5 places assises** (hors exceptions limitées, notamment exploitation des remontées mécaniques et domaines skiables). C'est le corner case.

## 2. Calculs

**1) Amortissement non déductible du SUV**

- Dotation 2026 (01/07 → 31/12, 6 mois) : 52 800 / 5 × 6/12 = **5 280,00 €**
- Plafond applicable (WLTP, 158 g/km) : **18 300 €**
- Fraction non déductible : 5 280 × (52 800 – 18 300) / 52 800 = 5 280 × 65,34 % = **3 450,00 €**
- Fraction déductible : 5 280 – 3 450 = 1 830,00 € (= 18 300 / 5 × 6/12 ✔)
- **Le calcul de Nadia (4 290 €, avec un plafond de 9 900 €) est faux** : il surestime la réintégration de 840 €, soit 210 € d'IS payés en trop (25 %).
- Année pleine 2027 : dotation 10 560 € ; non déductible 10 560 × 34 500 / 52 800 = **6 900,00 €** ; déductible 3 660 €.

**2) Taxes annuelles du SUV 2026**

Taxe CO₂ — tarif plein pour 158 g/km :

| Tranche | Grammes | Tarif | Montant |
|---|---|---|---|
| 1 à 14 | 14 | 0 € | 0 |
| 15 à 55 | 41 | 1 € | 41 |
| 56 à 63 | 8 | 2 € | 16 |
| 64 à 95 | 32 | 3 € | 96 |
| 96 à 115 | 20 | 4 € | 80 |
| 116 à 135 | 20 | 10 € | 200 |
| 136 à 155 | 20 | 50 € | 1 000 |
| 156 à 158 | 3 | 60 € | 180 |
| **Total annuel** | 158 | | **1 613 €** |

- Période d'affectation : 01/07 → 31/12/2026 = **184 jours** / 365.
- Taxe CO₂ 2026 : 1 613 × 184 / 365 = 813,13 → **813 €**
- Taxe polluants (diesel = catégorie « les plus polluants ») : 500 × 184 / 365 = 252,05 → **252 €**
- Total : **1 065 €** → le calcul de Nadia est **juste**.
- Traitement : charge 2026 (compte 635 — subdivision selon la nomenclature 2025 du PCG), **non déductible** → réintégrée sur le 2058-A ; déclarée et payée avec la **CA3 de janvier 2027** (annexe 3310-A).
- Année pleine 2027 (barème inchangé) : 1 613 + 500 = 2 113 €.

**4) Pick-up — chiffrage du risque si la qualification « tourisme » est confirmée**

Taxe CO₂ pour 236 g/km (année pleine 2026, 365/365) : 1 613 (jusqu'à 158 g) + 17 × 60 (159 à 175) + 61 × 65 (176 à 236) = 1 613 + 1 020 + 3 965 = **6 598 €**
Taxe polluants (diesel) : **500 €** — Total : **7 098 €** non déductibles, à déclarer en janvier 2027.

Autres conséquences à examiner si la qualification est confirmée : plafonnement de l'amortissement (art. 39-4 CGI, qui renvoie à la même définition) et droit à déduction de TVA (règles TVA propres — voir M04). C'est un **dossier à part entière** : ne pas le régler au téléphone.

**5) Achat en décembre — effet 2026**

Livraison le 14/12/2026 : 17 jours d'amortissement (convention 360 jours : 14/12 → 30/12 inclus, à adapter à la méthode du cabinet).

| | Électrique 45 000 € TTC (0 g) | SUV diesel 52 800 € TTC (158 g) |
|---|---|---|
| Dotation 2026 | 45 000 / 5 × 17/360 = **425,00 €** | 52 800 / 5 × 17/360 = **498,67 €** |
| Plafond | 30 000 € | 18 300 € |
| Fraction non déductible | 425 × 15 000 / 45 000 = 141,67 € | 498,67 × 34 500 / 52 800 = 325,83 € |
| Déduction fiscale 2026 | **283,33 €** | **172,83 €** |
| Économie d'IS 2026 (25 %) | ≈ **71 €** | ≈ **43 €** |
| Taxes annuelles 2026 (18 jours : 14/12 → 31/12) | 0 € (CO₂ 0 g ; polluants 0 €) | (1 613 + 500) × 18/365 ≈ **104 €** non déductibles |

Conclusion : acheter en décembre **ne fait presque pas baisser l'IS 2026** (quelques dizaines d'euros) ; la décision doit se prendre sur le besoin réel, le coût complet sur 5 ans et la trésorerie. Sur 5 ans, l'électrique est nettement plus favorable (plafond 30 000 € contre 18 300 €, pas de taxes annuelles aux valeurs retenues, avantage en nature généralement minoré — *règles à vérifier*).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Amortissement SUV 2026 | 5 280,00 | |
| 31/12/2026 | OD | 28182 | Amortissements du matériel de transport | Amortissement SUV 2026 | | 5 280,00 |
| 31/12/2026 | OD | 635xxx | Taxes annuelles véhicules de tourisme (subdivision selon nomenclature 2025) | Taxe CO₂ SUV 2026 (184 j) | 813,00 | |
| 31/12/2026 | OD | 635xxx | Taxes annuelles véhicules de tourisme (subdivision selon nomenclature 2025) | Taxe polluants SUV 2026 (184 j) | 252,00 | |
| 31/12/2026 | OD | 4486 | État — charges à payer | Taxes annuelles VP 2026 à déclarer en janvier 2027 | | 1 065,00 |
| | | | | **Totaux** | **6 345,00** | **6 345,00** |

Le 2058-A (E10-01) porte : + 3 450 € (amortissement excédentaire, et non 4 290 € comme l'avait calculé Nadia) et + 1 065 € (taxes annuelles). Aucune écriture comptable pour ces réintégrations.

## 4. Points d'attention / pièges

- **Seuil NEDC / WLTP** : le piège de l'exercice. Le seuil de 130 g/km (plafond de 9 900 €) est celui de l'ancienne norme NEDC ; en WLTP, le plafond de 18 300 € s'applique de 50 à 160 g/km. Contrôlez la norme sur la carte grise (rubrique V.7 et mentions associées) avant de choisir le plafond.
- **Base du plafond = prix TTC** du véhicule (hors carte grise facturée séparément). Pour un véhicule électrique, la batterie louée ou facturée à part a son propre traitement.
- **Prorata en jours** pour les taxes (184/365), pas en mois.
- La taxe **n'est pas une charge 2027** parce qu'elle est payée en 2027 : elle se rattache à l'année d'utilisation.
- **« CTTE » sur la carte grise ≠ utilitaire** au sens des taxes : un pick-up 5 places est en principe un véhicule de tourisme pour le CIBS. Une **camionnette « 2 rangs de places »** affectée au transport de personnes peut aussi l'être. Vérifiez carrosserie + nombre de places + usage.
- Les **véhicules de location courte durée** (≤ 30 jours consécutifs ou 1 mois civil) sont exonérés chez l'utilisateur, à vérifier selon les contrats.
- Avantage en nature de Karim : à contrôler en paie (M07).

## 5. Ce qu'un senior ferait en plus

- Lister **tout le parc** (cartes grises + contrats de location) et produire un tableau : genre, carrosserie, places, CO₂, énergie, dates d'affectation, taxes, plafond.
- Sur le pick-up : note écrite à Hélène, puis analyse de la doctrine en vigueur ; si la qualification est confirmée, **régulariser** (déclaration rectificative si des années antérieures sont concernées) plutôt que d'attendre un contrôle.
- **Mail type à Karim** :

> « Bonjour Karim, sur le SUV, 3 450 € d'amortissement (et non 4 290 € comme calculé initialement : le plafond applicable à votre véhicule est de 18 300 €) et 1 065 € de taxes 2026 ne sont pas déductibles ; ce sera environ 6 900 € et 2 113 € en 2027. Acheter une voiture le 14 décembre ne vous ferait économiser que 43 € (diesel) à 71 € (électrique) d'IS sur 2026 : ce n'est pas un levier fiscal. Si le besoin est réel, l'électrique est bien plus intéressant sur la durée. Enfin, le pick-up Ranger 5 places pourrait être considéré comme un véhicule de tourisme pour les taxes : nous analysons le point et revenons vers vous avant la déclaration de janvier. Bien à vous. »

## 6. Références

- CGI art. 39-4 (plafond d'amortissement des véhicules de tourisme) ; non-déductibilité des taxes annuelles sur les véhicules de tourisme (CGI, art. relatif à ces taxes — à vérifier dans la codification en vigueur).
- CIBS : art. L. 421-2 (définition des véhicules de tourisme), L. 421-93 et suivants (taxes annuelles sur l'affectation des véhicules à des fins économiques).
- PCG : comptes 2182, 28182, 6811, 635, 4486.
- BOFiP : série BIC-AMT (amortissement des véhicules), série relative aux taxes sur l'affectation des véhicules.
