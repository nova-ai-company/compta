# Corrigé E10-11 — La 2031 de Style & Vous : l'EURL à l'IR et la rémunération de la gérante

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-11](../exercices/E10-11_2031-style-et-vous.md)

## 1. Analyse

L'EURL n'a pas opté pour l'IS : fiscalement, **Nadia et l'entreprise ne font qu'un**. Le bénéfice de l'EURL est imposé **à son nom** (BIC, 2042-C-PRO) et sert d'assiette à ses cotisations SSI. Conséquences :

- Sa **rémunération**, qu'on l'appelle prélèvement, salaire ou prime, **n'est pas une charge** : c'est une affectation du bénéfice (si elle est passée en charge, elle est réintégrée sur la ligne « rémunération du travail de l'exploitant » du 2033-B / 2058-A).
- Ses **cotisations sociales personnelles** obligatoires sont déductibles, sauf **CSG non déductible et CRDS**.
- Son **impôt sur le revenu** n'est jamais une charge de l'entreprise.
- Les produits qu'elle prélève pour sa famille sont des **prélèvements en nature**, à constater (sinon les achats correspondants réduisent indûment le bénéfice).

## 2. Calculs

**Corrections comptables préalables**
- Prélèvement à la source de l'IR (4 200 €) : reclassement en 108 → résultat + 4 200 €.
- Prélèvements en nature (420 € au prix d'achat) : 108 / 607 → résultat + 420 €.
- Résultat comptable corrigé : 47 380 + 4 200 + 420 = **52 000,00 €**

**CSG non déductible et CRDS** : 6 790 × 2,9 / 9,7 = **2 030,00 €**

**Passage au résultat fiscal**

| Ligne | Réintégrations | Déductions |
|---|---|---|
| Résultat comptable corrigé | 52 000,00 | |
| Rémunération du travail de l'exploitant (prime 641100) | 6 000,00 | |
| CSG non déductible et CRDS | 2 030,00 | |
| Amende de stationnement | 135,00 | |
| **Résultat fiscal BIC** | **60 165,00** | |

Les 16 370 € restants de cotisations SSI (18 400 – 2 030) restent déduits, y compris la régularisation 2025 payée en 2026.

**PER / Madelin retraite (3 000 €)**
- 10 % × 60 165 = 6 016,50 €
- 15 % × (60 165 – 48 060) = 1 815,75 €
- Plafond = 7 832,25 € (> minimum 10 % du PASS = 4 806 €)
- 3 000 € < 7 832,25 € → **entièrement déductible** ✔ (le plafond se calcule sur le bénéfice avant déduction de la cotisation PER ; écart sans incidence ici).

**Aide à l'apprentie (6 000 €)** : subvention d'exploitation **imposable** (aucun texte ne l'exonère) → aucun retraitement.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 108000 | Compte de l'exploitant | Reclassement PAS impôt sur le revenu de la gérante | 4 200,00 | |
| 31/12/2026 | OD | 635400 | Impôts et taxes | Reclassement PAS impôt sur le revenu de la gérante | | 4 200,00 |
| 31/12/2026 | OD | 108000 | Compte de l'exploitant | Prélèvements en nature 2026 (produits capillaires, prix d'achat) | 420,00 | |
| 31/12/2026 | OD | 607000 | Achats de marchandises | Prélèvements en nature 2026 | | 420,00 |
| | | | | **Totaux** | **4 620,00** | **4 620,00** |

**Prime de 6 000 €** : deux traitements possibles, avec le même résultat fiscal :
- soit on la laisse en 641100 et on la réintègre (tableau ci-dessus) ;
- soit — **préférable** — on la reclasse en 108 (D 108 / C 641100 pour 6 000 €), ce qui supprime la réintégration et rend les comptes plus lisibles. Attention : aucune cotisation salariale ou patronale ne doit avoir été déclarée en DSN sur cette « prime » ; si c'est le cas, il faut **régulariser la DSN**.

## 4. Points d'attention / pièges

- Une gérante d'EURL à l'IR **n'est pas salariée** de son EURL : pas de bulletin de paie pour elle.
- **Cotisations SSI** : déductibles l'année de leur **paiement** (provisionnelles + régularisation payées en 2026) ; pas de charge à payer déductible pour une régularisation future.
- **CSG/CRDS** : 2,9 points sur 9,7 sont non déductibles.
- **Assiette sociale** : la réforme du calcul de l'assiette des cotisations des travailleurs indépendants (assiette unique, abattement forfaitaire) modifie le calcul des cotisations sur les revenus récents — *calendrier et modalités à vérifier*.
- Les prélèvements en nature non constatés sont un point classique de contrôle dans les commerces (coiffure, boulangerie).

## 5. Ce qu'un senior ferait en plus

**Éléments de réponse « faut-il passer à l'IS ? »**

| Critère | EURL à l'IR (actuel) | EURL à l'IS (option) |
|---|---|---|
| Imposition | Tout le bénéfice (60 165 €) au barème de l'IR, même s'il reste dans l'entreprise | IS 15 % / 25 % sur le bénéfice après rémunération ; IR seulement sur ce que Nadia se verse |
| Cotisations SSI | Sur tout le bénéfice | Sur sa rémunération + sur les **dividendes au-delà de 10 %** du capital, primes et compte courant (gérante TNS) |
| Intérêt | Faible si Nadia consomme tout son revenu | Intérêt si une partie du bénéfice peut rester dans l'entreprise (investissements, trésorerie) |
| Formalités | Plus simples | Option irrévocable après la 5e année (*à vérifier*) ; paie de la gérante, AG d'affectation |

Avec un bénéfice de 60 165 € et des prélèvements de 33 600 €, il reste ≈ 26 500 € non prélevés taxés aujourd'hui au taux marginal de Nadia : une **simulation chiffrée** est justifiée (voir la méthode de l'exercice E10-13). « Moins de cotisations » n'est vrai que si Nadia accepte des **droits sociaux** (retraite, indemnités journalières) plus faibles.

- **Mail type** :

> « Bonjour Nadia, votre prime de 6 000 € ne peut pas réduire votre bénéfice : dans une EURL à l'IR, tout ce que vous vous versez est un prélèvement sur le bénéfice, qui reste imposé à votre nom. Votre bénéfice 2026 est de 60 165 €. L'aide pour l'apprentie est imposable comme toute subvention d'exploitation. Pour le passage à l'IS, je vous propose un rendez-vous avec une simulation : c'est intéressant si vous laissez une partie du bénéfice dans le salon, mais il faut regarder l'impact sur votre retraite. Pensez aussi à noter les produits que vous prenez pour vous. Bien à vous. »

## 6. Références

- CGI : art. 34 et s. (BIC), art. 39-1 (charges), art. 39-2 (amendes), art. 154 bis (cotisations sociales et PER/Madelin des travailleurs non salariés), art. 154 quinquies (CSG déductible), art. 206-3 et 239 (option pour l'IS des EURL et sociétés de personnes).
- Code de la sécurité sociale : art. L. 131-6 (assiette des cotisations des travailleurs indépendants).
- PCG : compte 108 (compte de l'exploitant).
- Imprimés : 2031, 2033-A à G, 2042-C-PRO.
