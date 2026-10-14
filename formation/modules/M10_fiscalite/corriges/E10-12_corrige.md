# Corrigé E10-12 — LMNP des Bernard : amortissements par composants et ARD

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-12](../exercices/E10-12_LMNP-bernard.md)

## 1. Analyse

1. **Statut** : recettes 31 200 € > 23 000 €, mais 31 200 € < 98 000 € de salaires → **LMNP** (les deux conditions du LMP sont cumulatives).
2. **Terrain** : jamais amortissable. M. Bernard l'a exclu pour Lyon mais pas pour Annecy.
3. **Art. 39 C CGI** : en location meublée non professionnelle, l'amortissement ne peut ni **créer** ni **augmenter** un déficit. La fraction non déduite (ARD) est reportable **sans limite de durée**, sur les bénéfices futurs de la même activité.
4. Même s'il existait un déficit (venant des charges hors amortissement), un LMNP ne peut l'imputer **que sur ses revenus de location meublée non professionnelle** des 10 années suivantes — jamais sur les salaires.

## 2. Calculs

**Taux annuel moyen par composants** : 50 %/50 + 20 %/25 + 20 %/20 + 10 %/10 = 1 % + 0,8 % + 1 % + 1 % = **3,8 % du bâti**.

| Bien | Prix | Terrain | Bâti amortissable | Dotation 2026 (3,8 %) |
|---|---|---|---|---|
| Studio Lyon 7e | 140 000 | 15 % = 21 000 | 119 000 | 4 522,00 |
| Studio Lyon 3e | 165 000 | 15 % = 24 750 | 140 250 | 5 329,50 |
| Annecy | 310 000 | 20 % = 62 000 | **248 000** | **9 424,00** |
| Mobilier | | | | 2 900,00 |
| **Total** | | | | **22 175,50** |

Erreur sur Annecy : 11 780 – 9 424 = 2 356 € de trop chaque année depuis 2023 (à corriger aussi sur les exercices antérieurs : correction d'erreur, cumul des amortissements à recalculer et ARD 2023-2025 à revoir).

**Art. 39 C**

| Élément | Montant |
|---|---|
| Recettes | 31 200,00 |
| – Charges hors amortissements | – 21 970,00 |
| = Résultat avant amortissements | **9 230,00** |
| Amortissements de l'exercice | 22 175,50 |
| **Amortissement déductible** (limité au résultat avant amortissements) | **9 230,00** |
| **ARD de l'exercice** | 22 175,50 – 9 230,00 = **12 945,50** |
| ARD antérieurs (non imputables : pas de bénéfice résiduel) | 14 800,00 |
| **Stock d'ARD au 31/12/2026** | **27 745,50** |
| **Résultat fiscal 2026** | **0,00** |

(Sous réserve du recalcul des ARD antérieurs après correction du terrain d'Annecy.)

**Comparaison micro-BIC 2026**

- Recettes 31 200 € × (1 – 50 %) = **15 600 €** imposables (au barème + prélèvements sociaux).
- Réel : **0 €** imposable, et 27 745,50 € d'ARD en réserve pour les années futures.
- → Le **réel** reste nettement plus favorable.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 681120 | Dotations aux amortissements des immobilisations corporelles | Amortissement des immeubles par composants 2026 | 19 275,50 | |
| 31/12/2026 | OD | 281300 | Amortissements des constructions | Amortissement des immeubles par composants 2026 | | 19 275,50 |
| 31/12/2026 | OD | 681120 | Dotations aux amortissements des immobilisations corporelles | Amortissement du mobilier 2026 | 2 900,00 | |
| 31/12/2026 | OD | 281840 | Amortissements du mobilier | Amortissement du mobilier 2026 | | 2 900,00 |
| | | | | **Totaux** | **22 175,50** | **22 175,50** |

En comptabilité, on comptabilise **l'intégralité** de l'amortissement (le résultat comptable est une perte de 12 945,50 €). La limitation de l'art. 39 C est un **retraitement extra-comptable** (réintégration de 12 945,50 € et suivi des ARD sur la liasse).

## 4. Points d'attention / pièges

- **Terrain** : vérifier la ventilation dès l'acquisition (expertise, notaire, ratio usuel selon la localisation).
- **Ordre d'imputation** des années suivantes : charges, puis amortissements de l'exercice, puis ARD antérieurs.
- **Pas de déficit sur le revenu global** pour un LMNP.
- **Cotisation CFE** : due pour les locations meublées (sauf exonérations), déductible.
- **Statut LMP** à surveiller chaque année : si les recettes augmentent ou si un des époux arrête de travailler, le statut peut basculer (cotisations sociales, plus-values professionnelles).
- **Meublé de tourisme** : réglementation locale (enregistrement, quotas) et risque de TVA si prestations para-hôtelières (3 des 4 services).

## 5. Ce qu'un senior ferait en plus

**Réintégration des amortissements à la revente (LF 2025)** : depuis la loi de finances pour 2025, lors de la cession d'un logement loué en LMNP, les amortissements **déduits** pendant la location viennent **réduire le prix d'acquisition** retenu pour le calcul de la plus-value immobilière privée (hors exceptions, notamment certaines résidences de services — *modalités et exceptions à vérifier*). Les ARD non encore déduits ne devraient pas être concernés puisqu'ils n'ont pas été « admis en déduction » (*point à confirmer*).

Arrêter d'amortir ? **Non** : l'amortissement est obligatoire en comptabilité commerciale, et il évite aujourd'hui l'impôt sur les loyers (IR + prélèvements sociaux, ≈ 45 % au taux marginal du foyer) ; la plus-value future bénéficie, elle, des abattements pour durée de détention. Le senior propose une **simulation** à l'horizon de revente envisagé.

- **Mail type à M. Bernard** :

> « Bonjour Monsieur Bernard, votre résultat 2026 est nul : l'amortissement est limité aux loyers nets (9 230 €), et le surplus (12 945,50 €) est mis en réserve avec les 14 800 € des années précédentes, sans limite de durée. En revanche, en tant que loueur non professionnel, vous ne pouvez pas déduire de déficit de vos salaires. Nous avons corrigé l'amortissement d'Annecy, qui incluait le terrain (non amortissable). Pour la revente : les amortissements déduits seront bien réintégrés dans la plus-value, mais continuer à amortir reste intéressant ; je vous propose une simulation si un projet de vente se précise. Bien à vous. »

- Tenir un **tableau de suivi des ARD** par année d'origine dans le dossier permanent.

## 6. Références

- CGI : art. 35 (location meublée = BIC), art. 39 C II (limitation de l'amortissement et ARD), art. 155 IV (définition LMP/LMNP), art. 156 I-1° ter (imputation des déficits LMNP), art. 50-0 (micro-BIC), art. 150 VB (prix d'acquisition et réintégration des amortissements — rédaction issue de la LF 2025).
- PCG : approche par composants (art. 214-9), terrain non amortissable.
- Loi du 19/11/2024 dite « Le Meur » (régulation des meublés de tourisme, régime micro-BIC).
