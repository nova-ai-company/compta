# Corrigé E16-06 — Suivi budgétaire au 30 septembre : budget, réalisé, écarts et projection

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-06](../exercices/E16-06_suivi-budgetaire-30-septembre.md)

*Rappel : association, personnes et chiffres fictifs. Tous les montants de charges sont TTC (TVA non récupérable).*

!!! abstract "En clair"
    1. On compare le réalisé au **budget proratisé** : 9 mois sur 12, donc budget × 9/12 (75 %).
    2. Un écart n'est pas « bon » ou « mauvais » en soi : il faut **l'expliquer**. Un poste à 0 € peut simplement ne pas encore être comptabilisé (amortissements).
    3. La projection de fin d'année = réalisé + ce qui reste à dépenser **compte tenu de ce que l'on sait**. La simple règle de trois (× 12/9) se trompe dès qu'il y a un événement ponctuel.
    4. Résultat : le SESSAD n'est **pas** en excédent de 35 000 € (projection linéaire), il finit **proche de l'équilibre (− 2 313 €)**. Le SAVS finit en **déficit d'environ 11 660 €**, pas 7 360 €.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Étape 1 — Choisir la bonne base de comparaison

Au 30/09, comparer le réalisé au budget **annuel** ne veut rien dire : 856 810 € réalisés sur 1 180 000 € budgétés, c'est « 72,6 % », et alors ? La bonne question est : « à cette date, aurais-je dû dépenser plus ou moins ? ». On calcule donc le **budget proratisé** :

> Budget proratisé au 30/09 = budget annuel × 9/12

Puis :

> Écart (€) = réalisé − budget proratisé · Écart (%) = écart / budget proratisé

Convention de signe utilisée ici : pour les **charges**, un écart **positif** = on a **plus dépensé** que prévu (défavorable). Pour les **produits**, un écart **négatif** = on a **moins encaissé** que prévu (défavorable).

> 💡 Réflexe senior : le prorata 9/12 suppose des dépenses **régulières**. Avant de commenter un écart, demandez-vous : « ce poste est-il régulier ? ». Loyer, salaires, dotation : oui. Amortissements passés à la clôture, frais de siège trimestriels, intérim d'été, achats ponctuels : non.

### Étape 2 — Lire les écarts au 30/09

**SESSAD**

- **Groupe I : + 2 100 € (+ 3,4 %)**, entièrement dû au **carburant** (+ 2 160 €, + 13,7 %) : hausse du prix ou plus de kilomètres. À surveiller, à demander au chef de service.
- **Groupe II : − 11 700 € (− 1,7 %)**. Ce n'est **pas** une économie durable : Mme Perrin est absente depuis le 01/06 et **n'a pas été remplacée** pendant 4 mois. Le remplacement commence le 01/10.
- **Groupe III : − 18 590 € (− 15,3 %)**. Presque tout vient du compte **681 à 0 €** (− 19 500 €) : les amortissements ne sont passés qu'au 31/12. C'est un **faux écart**.
- **Produits : − 1 650 €** sur les autres produits (remboursements de formation pas encore reçus). La dotation est conforme (douzièmes).
- **Résultat au 30/09 : + 26 540 €**… qui ne veut presque rien dire, puisqu'il manque 9 mois d'amortissements.

**SAVS**

- **Groupe I : + 2 100 € (+ 5,8 %)**, entièrement dû au **carburant** (+ 20 %) : les vieux véhicules consomment plus.
- **Groupe II : + 6 150 € (+ 1,6 %)**, dont **intérim + 3 300 €** (l'intérim d'été dépasse déjà le budget annuel de 8 000 €) et une petite dérive des salaires et charges (+ 3 750 €).
- **Groupe III : − 5 430 €**, là encore à cause du **681 à 0 €**, mais les « autres charges » (entretien des véhicules) sont **déjà au-dessus** du prorata (+ 1 695 €, + 11,9 %).
- **Produits : − 2 700 €** sur les autres produits (− 30 %).
- **Résultat au 30/09 : − 5 520 €**, **avant** amortissements : le signal d'alerte est déjà là.

### Étape 3 — Pourquoi la projection linéaire est fausse

La projection linéaire multiplie tout par 12/9. Elle fait trois erreurs ici :

| Erreur de la projection linéaire | Service | Effet |
|---|---|---|
| Elle multiplie **0 € d'amortissements** par 12/9 → 0 € | SESSAD et SAVS | Elle **oublie** 26 000 € (SESSAD) et 5 000 € (SAVS) de charges |
| Elle ignore le **CDD de remplacement** qui commence le 01/10 | SESSAD | Elle oublie 3 × 3 900 = 11 700 € |
| Elle prolonge l'**intérim d'été** sur l'automne | SAVS | Elle **ajoute** 3 100 € d'intérim qui n'aura pas lieu |
| Elle ignore les **réparations** du véhicule n° 6 | SAVS | Elle oublie 2 400 € |
| Elle ignore les **CNR** (crédits non reconductibles) | SESSAD | Sans effet sur le résultat **si** les 25 000 € sont dépensés en 2026, mais elle fausse les totaux de charges et de produits |

**La bonne méthode** : pour chaque poste, choisir la façon de projeter :

- poste **régulier** (salaires, loyer, carburant, dotation) → réalisé × 12/9 ;
- poste **fixé à l'année** (frais de siège, amortissements) → montant annuel connu ;
- poste **ponctuel déjà terminé** (intérim d'été) → réalisé, sans prolongement ;
- **événement connu** (CDD, CNR, réparation) → on l'ajoute pour son montant.

> ⚠️ Erreur classique : présenter à la direction un SESSAD « en excédent de 35 000 € ». La directrice risque d'engager des dépenses nouvelles… et l'ERRD (état réalisé des recettes et des dépenses) sortira en déficit.

### Étape 4 — Les CNR, un piège pour l'année suivante

Les **CNR** (crédits non reconductibles) de 25 000 € augmentent les produits **et** les charges de 2026 : effet nul sur le résultat **si** les achats sont faits avant le 31/12. Deux risques :

1. **Achat non réalisé en 2026** → les 25 000 € deviennent un excédent « artificiel » que l'ARS peut reprendre ou affecter : il faut suivre la livraison de novembre.
2. **Base 2027** : ces 25 000 € ne reviendront pas. Il ne faut **pas** les inclure dans les produits de référence de 2027.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 1 — Écarts au 30/09 (budget proratisé = budget × 9/12)

**SESSAD**

| Poste | Budget 2026 | Budget proratisé (× 9/12) | Réalisé 30/09 | Écart (€) | Écart (%) |
|---|---|---|---|---|---|
| dont 6061 Carburant | 21 000,00 | 15 750,00 | 17 910,00 | + 2 160,00 | + 13,7 % |
| **Groupe I** | 82 000,00 | 61 500,00 | 63 600,00 | **+ 2 100,00** | + 3,4 % |
| dont 621 Intérim | 12 000,00 | 9 000,00 | 8 400,00 | − 600,00 | − 6,7 % |
| **Groupe II** | 936 000,00 | 702 000,00 | 690 300,00 | **− 11 700,00** | − 1,7 % |
| dont 681 Amortissements | 26 000,00 | 19 500,00 | 0,00 | − 19 500,00 | − 100,0 % |
| **Groupe III** | 162 000,00 | 121 500,00 | 102 910,00 | **− 18 590,00** | − 15,3 % |
| **Total charges** | 1 180 000,00 | 885 000,00 | 856 810,00 | **− 28 190,00** | − 3,2 % |
| 7351 Dotation globale | 1 165 000,00 | 873 750,00 | 873 750,00 | 0,00 | 0,0 % |
| Autres produits | 15 000,00 | 11 250,00 | 9 600,00 | − 1 650,00 | − 14,7 % |
| **Total produits** | 1 180 000,00 | 885 000,00 | 883 350,00 | **− 1 650,00** | − 0,2 % |

Détail des sous-totaux réalisés : groupe I = 17 910 + 45 690 = 63 600 ; groupe II = 449 700 + 199 200 + 8 400 + 33 000 = 690 300 ; groupe III = 40 500 + 0 + 38 110 + 24 300 = 102 910 ; total = 63 600 + 690 300 + 102 910 = 856 810 €.

**SAVS**

| Poste | Budget 2026 | Budget proratisé (× 9/12) | Réalisé 30/09 | Écart (€) | Écart (%) |
|---|---|---|---|---|---|
| dont 6061 Carburant | 14 000,00 | 10 500,00 | 12 600,00 | + 2 100,00 | + 20,0 % |
| **Groupe I** | 48 000,00 | 36 000,00 | 38 100,00 | **+ 2 100,00** | + 5,8 % |
| dont 621 Intérim | 8 000,00 | 6 000,00 | 9 300,00 | + 3 300,00 | + 55,0 % |
| **Groupe II** | 505 000,00 | 378 750,00 | 384 900,00 | **+ 6 150,00** | + 1,6 % |
| dont 681 Amortissements | 9 500,00 | 7 125,00 | 0,00 | − 7 125,00 | − 100,0 % |
| **Groupe III** | 87 000,00 | 65 250,00 | 59 820,00 | **− 5 430,00** | − 8,3 % |
| **Total charges** | 640 000,00 | 480 000,00 | 482 820,00 | **+ 2 820,00** | + 0,6 % |
| 7351 Dotation globale | 628 000,00 | 471 000,00 | 471 000,00 | 0,00 | 0,0 % |
| Autres produits | 12 000,00 | 9 000,00 | 6 300,00 | − 2 700,00 | − 30,0 % |
| **Total produits** | 640 000,00 | 480 000,00 | 477 300,00 | **− 2 700,00** | − 0,6 % |

Sous-totaux : groupe I = 12 600 + 25 500 = 38 100 ; groupe II = 249 600 + 110 400 + 9 300 + 15 600 = 384 900 ; groupe III = 23 250 + 0 + 20 670 + 15 900 = 59 820 ; total = 482 820 €.

### Question 2 — Résultat au 30/09 et projection linéaire

| | SESSAD | SAVS |
|---|---|---|
| Produits au 30/09 | 883 350,00 | 477 300,00 |
| Charges au 30/09 | 856 810,00 | 482 820,00 |
| **Résultat au 30/09** | **+ 26 540,00** | **− 5 520,00** |
| Produits × 12/9 | 1 177 800,00 | 636 400,00 |
| Charges × 12/9 | 1 142 413,33 | 643 760,00 |
| **Résultat « linéaire » au 31/12** | **+ 35 386,67** | **− 7 360,00** |

(Contrôle : 26 540 × 12/9 = 35 386,67 ; − 5 520 × 12/9 = − 7 360,00.)

### Question 3 — Projection corrigée au 31/12

**SESSAD**

| Poste | Méthode | Projection 31/12 | Budget 2026 | Écart projection / budget |
|---|---|---|---|---|
| 6061 Carburant | 17 910 × 12/9 | 23 880,00 | 21 000,00 | + 2 880,00 |
| Autres charges groupe I | 45 690 × 12/9 = 60 920 + CNR 25 000 | 85 920,00 | 61 000,00 | + 24 920,00 |
| **Groupe I** | | **109 800,00** | 82 000,00 | **+ 27 800,00** |
| 641 Rémunérations | 449 700 × 12/9 | 599 600,00 | 610 000,00 | − 10 400,00 |
| 645 Charges sociales | 199 200 × 12/9 | 265 600,00 | 270 000,00 | − 4 400,00 |
| 621 Intérim | 8 400 × 12/9 | 11 200,00 | 12 000,00 | − 800,00 |
| 631/633 Taxes sur rémunérations | 33 000 × 12/9 | 44 000,00 | 44 000,00 | 0,00 |
| CDD de remplacement (641 + 645) | 3 × 3 900 | 11 700,00 | — | + 11 700,00 |
| **Groupe II** | | **932 100,00** | 936 000,00 | **− 3 900,00** |
| 613 Loyer | 40 500 × 12/9 | 54 000,00 | 54 000,00 | 0,00 |
| 681 Amortissements | tableau d'amortissement | 26 000,00 | 26 000,00 | 0,00 |
| Frais de siège | montant annuel | 50 813,00 | 50 813,00 | 0,00 |
| Autres charges groupe III | 24 300 × 12/9 | 32 400,00 | 31 187,00 | + 1 213,00 |
| **Groupe III** | | **163 213,00** | 162 000,00 | **+ 1 213,00** |
| **Total charges** | | **1 205 113,00** | 1 180 000,00 | **+ 25 113,00** |
| 7351 Dotation globale | annuelle | 1 165 000,00 | 1 165 000,00 | 0,00 |
| 7351 CNR 2026 | notification | 25 000,00 | — | + 25 000,00 |
| Autres produits | 9 600 × 12/9 | 12 800,00 | 15 000,00 | − 2 200,00 |
| **Total produits** | | **1 202 800,00** | 1 180 000,00 | **+ 22 800,00** |
| **Résultat projeté** | | **− 2 313,00** | 0,00 | **− 2 313,00** |

Passage de la projection linéaire à la projection corrigée (SESSAD) :

| | Montant |
|---|---|
| Résultat linéaire | + 35 386,67 |
| − Amortissements oubliés | − 26 000,00 |
| − CDD de remplacement | − 11 700,00 |
| + Frais de siège : 50 813,00 au lieu de 38 110 × 12/9 = 50 813,33 | + 0,33 |
| CNR : + 25 000 de produits et + 25 000 de charges | 0,00 |
| **Résultat corrigé** | **− 2 313,00** |

**SAVS**

| Poste | Méthode | Projection 31/12 | Budget 2026 | Écart projection / budget |
|---|---|---|---|---|
| 6061 Carburant | 12 600 × 12/9 | 16 800,00 | 14 000,00 | + 2 800,00 |
| Autres charges groupe I | 25 500 × 12/9 | 34 000,00 | 34 000,00 | 0,00 |
| **Groupe I** | | **50 800,00** | 48 000,00 | **+ 2 800,00** |
| 641 Rémunérations | 249 600 × 12/9 | 332 800,00 | 330 000,00 | + 2 800,00 |
| 645 Charges sociales | 110 400 × 12/9 | 147 200,00 | 145 000,00 | + 2 200,00 |
| 621 Intérim | terminé : réalisé | 9 300,00 | 8 000,00 | + 1 300,00 |
| 631/633 Taxes sur rémunérations | 15 600 × 12/9 | 20 800,00 | 22 000,00 | − 1 200,00 |
| **Groupe II** | | **510 100,00** | 505 000,00 | **+ 5 100,00** |
| 613 Loyer | 23 250 × 12/9 | 31 000,00 | 31 000,00 | 0,00 |
| 681 Amortissements | véhicule reporté : 5 000 seulement | 5 000,00 | 9 500,00 | − 4 500,00 |
| Frais de siège | montant annuel | 27 560,00 | 27 560,00 | 0,00 |
| Autres charges groupe III | 15 900 × 12/9 = 21 200 + garage 2 400 | 23 600,00 | 18 940,00 | + 4 660,00 |
| **Groupe III** | | **87 160,00** | 87 000,00 | **+ 160,00** |
| **Total charges** | | **648 060,00** | 640 000,00 | **+ 8 060,00** |
| 7351 Dotation globale | annuelle | 628 000,00 | 628 000,00 | 0,00 |
| Autres produits | 6 300 × 12/9 | 8 400,00 | 12 000,00 | − 3 600,00 |
| **Total produits** | | **636 400,00** | 640 000,00 | **− 3 600,00** |
| **Résultat projeté** | | **− 11 660,00** | 0,00 | **− 11 660,00** |

Passage de la projection linéaire à la projection corrigée (SAVS) :

| | Montant |
|---|---|
| Résultat linéaire | − 7 360,00 |
| − Amortissements oubliés (5 000 au lieu de 0) | − 5 000,00 |
| + Intérim non prolongé (12 400 linéaire − 9 300 réel) | + 3 100,00 |
| − Réparation du véhicule n° 6 | − 2 400,00 |
| **Résultat corrigé** | **− 11 660,00** |

### Question 4 — D'où vient le déficit du SAVS ?

| Origine (projection − budget) | Montant |
|---|---|
| Carburant (vieux véhicules, plus de km) | − 2 800,00 |
| Salaires et charges sociales (641 + 645) | − 5 000,00 |
| Intérim d'été au-delà du budget | − 1 300,00 |
| Taxes sur rémunérations (économie) | + 1 200,00 |
| Entretien des véhicules (dont garage 2 400) | − 4 660,00 |
| Amortissement du véhicule non acheté (économie) | + 4 500,00 |
| Autres produits non encaissés | − 3 600,00 |
| **Total** | **− 11 660,00** |

Lecture : le déficit vient à la fois du **personnel** (+ 5 100 € : salaires et intérim + 6 300 €, moins 1 200 € d'économie de taxes) et du **parc de véhicules vieillissant** (carburant + entretien : + 7 460 €). L'économie d'amortissement de 4 500 € est **trompeuse** : elle n'existe que parce que l'achat est reporté, et elle disparaîtra en 2027 (et l'amortissement du véhicule sera alors sur une année pleine).

**Leviers pour le 4e trimestre** (à proposer, la décision appartient à la direction) :

1. **Pas de nouvel intérim** sans accord de la directrice.
2. **Relancer les autres produits** : demandes de remboursement de formation non encore faites (écart de 3 600 €).
3. **Reporter** les achats non urgents du groupe I à 2027 (sauf sécurité).
4. **Analyser la dérive 641/645** (+ 5 000 €) : ancienneté, heures supplémentaires, remplacement ? Demander le détail par salarié au service paie du cabinet.
5. **Prévenir le Conseil départemental** dès maintenant (dialogue de gestion), plutôt qu'au moment du compte administratif.
6. Vérifier au bilan s'il existe une **réserve de compensation des déficits** (10686) propre au SAVS : sa reprise éventuelle est décidée par l'autorité de tarification, pas par l'association seule.

> ⚠️ Erreur classique : « rééquilibrer » le SAVS en imputant une partie de son carburant ou d'un salaire au SESSAD, qui a de la marge. C'est une **fausse imputation analytique** : chaque financeur paie **son** service. Le commissaire aux comptes et les financeurs contrôlent les clés de répartition.

## 3. Écritures comptables

**Réception des CNR (relevé bancaire du 20/10/2026)** — produit de la tarification, section 10-SESSAD :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 20/10/2026 | BQ | 512 | Banque | ARS – CNR 2026 matériel pédagogique SESSAD | 25 000,00 | |
| 20/10/2026 | BQ | 7351 | Produits de la tarification – dotation globale (CNR) | ARS – CNR 2026 matériel pédagogique SESSAD | | 25 000,00 |
| | | | | **Totaux** | **25 000,00** | **25 000,00** |

*Subdivision du 7351 selon le plan de comptes des ESSMS de l'association ; isolez les CNR dans un sous-compte ou un code analytique dédié pour pouvoir les suivre et les exclure de la base 2027.*

**Proposition pour 2027 : « abonnement » mensuel des amortissements.** Chaque fin de mois, on passe 1/12 de la dotation prévue, puis on régularise au 31/12 avec le tableau définitif. Exemple pour octobre, si la méthode avait été appliquée en 2026 :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Abonnement amortissements 10/2026 – SESSAD (26 000 / 12) | 2 166,67 | |
| 31/10/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Abonnement amortissements 10/2026 – SAVS (5 000 / 12) | 416,67 | |
| 31/10/2026 | OD | 2818 | Amortissements des autres immobilisations corporelles | Abonnement amortissements 10/2026 | | 2 583,34 |
| | | | | **Totaux** | **2 583,34** | **2 583,34** |

Avec cet abonnement, le compte 681 n'est jamais à 0 € en cours d'année, et le suivi budgétaire mensuel devient lisible.

## 4. Points d'attention / pièges

- **Amortissements à 0 €** : le piège principal. Un écart de − 100 % sur un poste n'est jamais une « économie » : c'est presque toujours une écriture pas encore passée.
- **Frais de siège trimestriels** : au 30/09, trois trimestres sont facturés, le prorata tombe juste. Au 31/10 ou au 30/11, il manquera un ou deux mois : même piège.
- **Absence non remplacée** : une économie de personnel liée à un poste vacant est **temporaire**. Dès que le remplacement arrive, elle disparaît.
- **CNR** : produits et charges à suivre à part ; à exclure de la base de l'année suivante ; à dépenser **dans l'année** pour l'objet notifié.
- **Écart en % sur une petite base** : + 55 % d'intérim au SAVS ne représente que 3 300 €. Commentez toujours **en euros d'abord**, en % ensuite.
- **Signe des écarts** : annoncez la convention (dépense en plus = défavorable). Une directrice ne doit pas avoir à deviner.
- **SESSAD et EPRD** : sous CPOM, l'EPRD couvre tout le gestionnaire ; un petit déficit du SESSAD n'est pas dramatique, mais il doit être **expliqué** dans l'ERRD.

## 5. Ce qu'un senior ferait en plus

**La note à Nathalie Berthier (question 6)** — une page, des chiffres ronds, des décisions à prendre :

```
Objet : Suivi budgétaire au 30/09/2026 et projection au 31/12/2026 — SESSAD et SAVS

Madame la Directrice,

1. Ce qu'il faut retenir
   - SESSAD : projection de fin d'année proche de l'équilibre (environ − 2 300 €).
     Le résultat comptable de + 26 500 € au 30/09 est trompeur : il manque les
     amortissements (26 000 €, passés au 31/12) et le CDD de remplacement de
     Mme Perrin (11 700 € d'octobre à décembre).
   - SAVS : risque de déficit d'environ − 11 700 € au compte administratif.

2. Origine du déficit du SAVS
   - Personnel : + 5 100 € (intérim d'été au-delà du budget, légère dérive des salaires).
   - Véhicules : + 7 500 € (carburant et réparations des véhicules anciens,
     dont 2 400 € de garage en novembre).
   - Autres produits : − 3 600 € (remboursements non encore obtenus).
   - Le report du véhicule neuf fait économiser 4 500 € d'amortissement en 2026,
     mais cette économie ne se reproduira pas en 2027.

3. Points de vigilance
   - CNR SESSAD (25 000 €) : les achats doivent être livrés et facturés avant le
     31/12, sinon les crédits non utilisés apparaîtront en excédent.
   - Ces 25 000 € ne doivent pas être repris dans le budget 2027.

4. Propositions (à votre décision)
   - SAVS : pas de nouvel intérim sans votre accord ; relance des remboursements
     de formation ; report des achats non urgents ; analyse de la masse salariale
     par salarié avec le service paie du cabinet.
   - Informer dès maintenant le Conseil départemental du risque de déficit.
   - Vérifier avec le cabinet l'existence d'une réserve de compensation des
     déficits pour le SAVS.
   - À partir de janvier 2027 : passer les amortissements chaque mois
     (1/12 du prévisionnel) pour un suivi plus fiable.

Je mets à jour cette projection fin octobre et fin novembre.
L'agent comptable
```

Autres réflexes :

- **Documenter les hypothèses** de projection dans un onglet « Hypothèses » du fichier (date, source : mail de Karim Belkacem, devis du garage, notification ARS). En cas de question du commissaire aux comptes ou de la trésorière, vous retrouvez l'origine de chaque chiffre.
- **Mettre à jour chaque mois** : une projection n'a de valeur que si elle est refaite (rolling forecast, « prévision glissante »).
- **Préparer l'argumentaire du compte administratif** dès maintenant : le Conseil départemental demandera pourquoi le véhicule a été reporté et pourquoi l'entretien a dépassé.
- **Prévoir le BP 2027 du SAVS** avec l'amortissement du véhicule en année pleine (24 000 € TTC sur la durée retenue par l'association).

## 6. Références

- Code de l'action sociale et des familles (CASF), partie réglementaire : dispositions budgétaires et comptables des ESSMS (groupes fonctionnels, EPRD, ERRD, budget prévisionnel, compte administratif, affectation des résultats) — *textes à consulter dans leur version en vigueur*.
- Plan comptable des ESSMS privés (adapté du PCG) : comptes 7351, 6811, 2818 — *subdivisions à vérifier sur le plan de comptes de l'association*.
- Règlement ANC n° 2018-06 (comptes annuels des personnes morales de droit privé à but non lucratif).
- Fiche de l'association Cap Horizons 21 : budgets 2026, frais de siège (4,5 %), modes de financement.
