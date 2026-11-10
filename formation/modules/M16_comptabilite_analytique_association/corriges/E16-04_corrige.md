# Corrigé E16-04 — Calculer et répartir les frais de siège

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-04](../exercices/E16-04_calculer-repartir-frais-siege.md)

!!! abstract "En clair"
    1. Les **ESSMS** (SESSAD, SAVS) paient le taux **autorisé** : 4,5 % de leurs charges **hors frais de siège**. Pas un euro de plus.
    2. Le **reste** du siège se répartit sur les autres services avec une clé (charges directes)…
    3. … mais chaque financeur a un **plafond**. Ce qui dépasse n'est payé par personne.
    4. Ce « trou » doit être financé par les **ressources propres** de l'association, ou réduit.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — L'erreur de Mme Roux

Elle a appliqué 4,5 % au **budget total** du SESSAD (1 180 000 €). Deux erreurs dans une seule ligne :
- **Le budget total contient déjà les frais de siège.** Calculer 4,5 % sur un montant qui inclut les frais de siège, c'est calculer des frais de siège sur des frais de siège. La règle dit : **hors frais de siège**.
- **On calcule sur le réalisé, pas sur le budget** : au moment de l'ERRD (état réalisé des recettes et des dépenses), ce sont les charges réelles de l'année qui comptent.

Conséquence : 53 100 € facturés au lieu de 50 776,84 €, soit **2 323,16 €** de trop. L'ARS (agence régionale de santé) les aurait retirés des charges acceptées au moment de l'ERRD.

### La logique d'ensemble

Le siège coûte **160 000,00 €** (y compris sa part des charges communes, restée sur 01-SIEGE dans l'exercice E16-02). On cherche qui le paie :

```
160 000,00 € de siège
  ├─ SESSAD et SAVS : taux autorisé 4,5 %   → montant fixé par la règle
  ├─ Emploi, habitat, Pairs : le reste, au prorata des charges directes
  │     └─ mais plafonné par chaque convention
  └─ Ce qui reste = non couvert → ressources propres de l'association
```

## 2. Calculs (détaillés, chaque montant justifié)

### Question 1 — Frais de siège des ESSMS

| Service | Charges brutes hors frais de siège | Taux | Frais de siège |
|---|---|---|---|
| 10-SESSAD | 1 128 374,19 € | 4,5 % | **50 776,84 €** |
| 20-SAVS | 612 150,69 € | 4,5 % | **27 546,78 €** |
| **Total ESSMS** | **1 740 524,88 €** | | **78 323,62 €** |

Calculs : 1 128 374,19 × 0,045 = 50 776,838… → 50 776,84 € ; 612 150,69 × 0,045 = 27 546,781… → 27 546,78 €.

Le SESSAD supporte donc au total 1 128 374,19 + 50 776,84 = **1 179 151,03 €** (proche du budget de la fiche, 1 180 000 €), et le SAVS 612 150,69 + 27 546,78 = **639 697,47 €** (budget : 640 000 €). Les ordres de grandeur sont cohérents.

### Question 2 — Le reste, réparti mécaniquement

Reste à financer : 160 000,00 − 78 323,62 = **81 676,38 €**.

Charges directes des trois services hors ESSMS : 255 600,00 + 81 300,00 + 47 400,00 = **384 300,00 €**.

| Service | Charges directes | Calcul | Quote-part mécanique |
|---|---|---|---|
| 30-EMPLOI | 255 600,00 € | 81 676,38 × 255 600 / 384 300 | 54 323,40 € |
| 40-HABITAT | 81 300,00 € | 81 676,38 × 81 300 / 384 300 | 17 278,92 € |
| 50-PAIRS | 47 400,00 € | 81 676,38 × 47 400 / 384 300 | 10 074,06 € |
| **Total** | **384 300,00 €** | | **81 676,38 €** |

Taux implicite : 81 676,38 / 384 300,00 = **21,25 %** des charges directes. C'est près de **cinq fois** le taux des ESSMS. Aucun financeur n'acceptera cela.

### Question 3 — Ce que les financeurs acceptent

| Service | Plafond | Calcul | Quote-part acceptée | Quote-part mécanique | Non financé |
|---|---|---|---|---|---|
| 30-EMPLOI | 10 % | 255 600,00 × 10 % | **25 560,00 €** | 54 323,40 € | 28 763,40 € |
| 40-HABITAT | 8 % | 81 300,00 × 8 % | **6 504,00 €** | 17 278,92 € | 10 774,92 € |
| 50-PAIRS | 10 % | 47 400,00 × 10 % | **4 740,00 €** | 10 074,06 € | 5 334,06 € |
| **Total** | | | **36 804,00 €** | **81 676,38 €** | **44 872,38 €** |

### Question 4 — Couverture du siège

| | Montant |
|---|---|
| Coût du siège | 160 000,00 € |
| Frais de siège des ESSMS (4,5 %) | − 78 323,62 € |
| Quotes-parts acceptées hors ESSMS | − 36 804,00 € |
| **Siège non couvert** | **44 872,38 €** |
| Taux de couverture | 115 127,62 / 160 000,00 = **71,95 %** |
| Excédent de la vie associative | − 16 000,00 € |
| **Reste à financer sur les réserves** | **28 872,38 €** |

**Réponse à la directrice : non, le siège n'est pas entièrement couvert.** Près de 28 % de son coût (44 872,38 €) n'est payé par aucun financeur. L'excédent de la vie associative (dons, cotisations) en absorbe 16 000,00 € ; il reste **28 872,38 €** de déficit, qui sera pris sur les **fonds propres** de l'association si rien ne change.

> 💡 Réflexe senior : un siège non couvert ne se voit pas dans les comptes **d'un** service ; il se voit dans le résultat de **l'association**. C'est pourquoi la trésorière pose la question : c'est l'argent des dons qui paie la comptabilité.

**Pistes à présenter (sans promettre de résultat) :**
1. **Négocier le taux** lors du prochain CPOM (contrat pluriannuel d'objectifs et de moyens) avec l'ARS et avec le Département. Repère : passer de 4,5 % à 5,5 % rapporterait 1 740 524,88 × 1 % = **17 405,25 €** par an. Une demande de frais de siège se prépare avec un dossier (missions du siège, coûts, comparaison) — *procédure et pièces à vérifier auprès des autorités*.
2. **Mettre les frais de structure au plafond** dans **chaque** nouveau budget d'appel à projets ou de convention, et les justifier (c'est la partie financière des dossiers de subvention).
3. **Imputer en direct** ce qui est vraiment direct pour les projets **hors ESSMS** : par exemple, les heures du siège consacrées au compte rendu de Pairs, si la convention accepte ce temps en coût direct et qu'il est prouvé par des **feuilles de temps**. Attention : pour le SESSAD et le SAVS, ce serait des frais de siège **déguisés**, refusés.
4. **Regarder les coûts du siège** lui-même (contrats, honoraires, logiciels) : 1 € économisé au siège est 1 € de trou en moins.

## 3. Écritures comptables

### Question 5 — Compte de liaison 181 ou OD analytique ?

**Le compte de liaison 181** sert quand **chaque service tient une comptabilité séparée** (un « établissement » avec sa propre balance). Le siège « facture » le service :
- chez le service : une charge (quote-part de frais de siège) et une dette envers le siège (181) ;
- chez le siège : une créance sur le service (181) et un produit.

À la fin, on **additionne** toutes les comptabilités : les comptes 181 se compensent (dette du service = créance du siège) et la charge et le produit internes s'éliminent. C'est lourd, mais indispensable quand chaque établissement doit présenter son **propre bilan**.

Exemple pour le SESSAD seulement (à titre d'illustration) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD (compta SESSAD) | 655 | Quote-part de frais de siège | Frais de siège 2026 – 4,5 % | 50 776,84 | |
| 31/12/2026 | OD (compta SESSAD) | 181 | Compte de liaison – Siège | Frais de siège 2026 – 4,5 % | | 50 776,84 |
| 31/12/2026 | OD (compta siège) | 181 | Compte de liaison – SESSAD | Frais de siège 2026 facturés au SESSAD | 50 776,84 | |
| 31/12/2026 | OD (compta siège) | 7xx | Produit : quote-part de frais de siège | Frais de siège 2026 facturés au SESSAD | | 50 776,84 |
| | | | | **Totaux** | **101 553,68** | **101 553,68** |

**L'OD analytique** sert quand l'association tient **une seule comptabilité générale** avec un **axe analytique** « service » — c'est le cas de Cap Horizons 21 (fiche, § 1). On ne crée ni dette, ni créance, ni produit interne : on **déplace** le coût du siège vers les sections des services, comme pour les charges communes.

**Choix pour Cap Horizons 21 : l'OD analytique.** Une seule comptabilité, un axe « service » : c'est plus simple, et le total des charges de l'association ne change pas (une refacturation interne n'est pas une charge de plus).

*Numéros : 655 « quote-part de frais de siège » et le produit « 7xx » du siège sont des intitulés à adapter : utilisez la subdivision prévue par le plan comptable des ESSMS et le plan de comptes de l'association.*

### Question 6 — OD analytique de répartition des frais de siège au 31/12/2026

On débite le compte 655 sur la section de chaque service (sa charge augmente) et on le crédite sur la section 01-SIEGE (le coût du siège diminue d'autant). En comptabilité générale, le compte 655 est soldé : effet nul sur le résultat.

| Date | Journal | Compte | Intitulé du compte | Libellé | Section | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 655 | Quote-part de frais de siège | Frais de siège 2026 – 4,5 % autorisé | 10-SESSAD | 50 776,84 | |
| 31/12/2026 | OD | 655 | Quote-part de frais de siège | Frais de siège 2026 – 4,5 % autorisé | 20-SAVS | 27 546,78 | |
| 31/12/2026 | OD | 655 | Quote-part de frais de siège | Frais de structure 2026 – 10 % convention | 30-EMPLOI | 25 560,00 | |
| 31/12/2026 | OD | 655 | Quote-part de frais de siège | Frais de gestion 2026 – 8 % convention AVP | 40-HABITAT | 6 504,00 | |
| 31/12/2026 | OD | 655 | Quote-part de frais de siège | Frais indirects 2026 – 10 % convention | 50-PAIRS | 4 740,00 | |
| 31/12/2026 | OD | 655 | Quote-part de frais de siège | Frais de siège 2026 répartis sur les services | 01-SIEGE | | 115 127,62 |
| | | | | **Totaux** | | **115 127,62** | **115 127,62** |

**Pourquoi on répartit le montant accepté, et pas le montant mécanique ?** Le compte rendu de chaque convention reprend les charges de la section. Si l'on mettait 54 323,40 € sur l'emploi accompagné, la section afficherait un déficit que le financeur ne couvrira jamais, et le compte rendu montrerait des frais de structure hors convention. Il est plus clair de laisser le **non couvert** (44 872,38 €) **visible sur 01-SIEGE** : c'est exactement le chiffre que la directrice doit présenter au bureau.

Après l'OD, la section 01-SIEGE présente : 160 000,00 − 115 127,62 = **44 872,38 €** de charges nettes non couvertes ✓.

## 4. Points d'attention / pièges

- **Base de calcul** : charges **hors frais de siège** (sinon calcul circulaire) et **réalisées** (pas le budget).
- **Plafond des ESSMS** : 4,5 % est un **maximum autorisé**. Ajouter au SESSAD une part du loyer du siège ou du salaire de la directrice, c'est dépasser ce taux par la porte de derrière.
- **Lire chaque convention** : la base du plafond change (charges directes, dépenses éligibles, budget total…). Un plafond de 10 % « des dépenses directes » ne s'applique pas sur le même montant qu'un plafond de 10 % « du budget total ».
- **Ne pas additionner** les charges du siège et les frais de siège des services pour faire le total de l'association : c'est le même argent compté deux fois (refacturation interne).
- **Arrondis** : 4,5 % donne des millièmes ; arrondissez chaque montant au centime, puis faites la somme de contrôle.

## 5. Ce qu'un senior ferait en plus

- **Une note d'une page pour le bureau**, avec le tableau de couverture de la question 4 et les pistes. Exemple :

> « Le siège coûte 160 000 € en 2026. Les financeurs en paient 115 128 € (72 %) : 78 324 € par le taux autorisé de 4,5 % sur le SESSAD et le SAVS, 36 804 € par les plafonds des conventions emploi, habitat et Pairs. Il reste 44 872 € non couverts. L'excédent de la vie associative (16 000 €) n'en couvre qu'une partie : le déficit prévisible est de 28 872 €, pris sur les fonds propres. Je propose de préparer une demande de révision du taux de frais de siège pour le prochain CPOM (+ 1 point = + 17 405 € par an) et d'inscrire systématiquement les frais de structure au plafond dans les nouveaux dossiers de financement. »

- **Vérifier la décision d'autorisation** des frais de siège (taux, durée, services concernés) et la classer dans le dossier permanent : le commissaire aux comptes la demandera.
- **Préparer l'EPRD 2027** avec le bon calcul (hors frais de siège), pour ne pas reproduire l'erreur de 2025.
- **Calculer le « coût économique »** de chaque service avec la répartition mécanique (exercice E16-05) : c'est le vrai coût d'un service, utile pour répondre à un appel à projets sans sous-estimer ses frais.

## 6. Références

- Code de l'action sociale et des familles : frais de siège social des organismes gestionnaires d'ESSMS (autorisation, quote-part imputée aux budgets des établissements) — *articles et procédure à vérifier dans leur version en vigueur*.
- Plan comptable des ESSMS : compte de quote-part de frais de siège (groupe III) et comptes de liaison 18x — *subdivisions à vérifier*.
- Règlement ANC n° 2018-06 (comptes annuels des associations).
- Conventions de financement (emploi accompagné, aide à la vie partagée, Fondation Lumen) : clauses sur les frais de structure — *fictives dans cet exercice*.
