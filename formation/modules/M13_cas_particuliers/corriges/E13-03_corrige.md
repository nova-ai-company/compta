# Corrigé E13-03 — Groupe Delta Invest : résultat d'ensemble, neutralisations et IS chez chacune

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E13-03](../exercices/E13-03_integration-fiscale-delta-invest.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — Chaque société calcule son résultat « comme si elle était seule ».** C'est la règle de base de l'intégration (CGI art. 223 B) : on ne neutralise rien à ce stade, chaque société applique ses propres règles (réintégrations, déductions, régime mère-fille).

Chez **Delta Invest** :
- L'**abandon de créance à caractère financier** n'est **pas déductible** chez la société qui le consent (CGI art. 39, 13), sauf s'il est consenti dans le cadre d'une procédure de sauvegarde, de redressement, de liquidation ou d'un accord de conciliation homologué — ce n'est pas le cas (pièce 1) → **réintégration de 120 000 €**.
- **Dividendes de Bâtisseurs du Sud** : régime mère-fille (≥ 5 % du capital, détention ≥ 2 ans) → déduction de 150 000 € et réintégration d'une **quote-part de frais et charges**. Comme la filiale distributrice est **membre du groupe intégré**, la quote-part est de **1 %** et non de 5 % (CGI art. 216, I).

Chez **la Menuiserie**, le produit d'abandon (120 000 €) est **imposable** individuellement : il est déjà dans son résultat fiscal de − 60 000 € (sans lui, la perte fiscale serait de − 180 000 €).

**Étape 2 — La mère fait la somme et rectifie.** Les opérations internes au groupe ne doivent pas créer d'impôt : l'abandon de créance entre sociétés du groupe est **neutralisé** pour le résultat d'ensemble (art. 223 B). Concrètement :
- chez Delta, la charge n'a pas été déduite (elle a été réintégrée) → rien à corriger de ce côté ;
- chez la Menuiserie, le produit a été imposé → on **déduit 120 000 €** du résultat d'ensemble.

Les dividendes ne donnent plus lieu à une neutralisation distincte : l'avantage du groupe est désormais intégré dans la quote-part réduite à 1 %.

**Étape 3 — L'IS du groupe** est calculé par la mère sur le résultat d'ensemble, avec **un seul** plafond de 42 500 € au taux de 15 %.

**Étape 4 — La convention répartit la charge.** Convention de **neutralité** : Bâtisseurs du Sud paie à Delta l'IS qu'elle aurait payé seule ; la Menuiserie, déficitaire, ne paie rien et ne reçoit rien ; l'économie reste chez la mère. Chez les filiales, la dette d'impôt est une dette envers la **mère** (451), pas envers l'État (444).

## 2. Calculs (détaillés, chaque montant justifié)

**Résultat fiscal individuel de Delta Invest**

| Élément | Montant |
|---|---|
| Résultat comptable avant IS (240 000 + 150 000 − 205 000 − 120 000) | 65 000,00 € |
| + Réintégration abandon de créance à caractère financier | + 120 000,00 € |
| − Déduction des dividendes (régime mère-fille) | − 150 000,00 € |
| + Quote-part de frais et charges 1 % × 150 000 | + 1 500,00 € |
| **Résultat fiscal individuel** | **36 500,00 €** |

**Résultat d'ensemble**

| Société | Résultat fiscal |
|---|---|
| Delta Invest | 36 500,00 € |
| Bâtisseurs du Sud (302 600 + 7 400) | 310 000,00 € |
| Menuiserie (− 62 000 + 2 000) | − 60 000,00 € |
| **Somme des résultats** | **286 500,00 €** |
| Neutralisation de l'abandon de créance intra-groupe (déduction du produit taxé chez la Menuiserie) | − 120 000,00 € |
| **Résultat d'ensemble** | **166 500,00 €** |

**IS du groupe** : 42 500 × 15 % + (166 500 − 42 500) × 25 % = 6 375,00 + 31 000,00 = **37 375,00 €**.

**IS individuels (en l'absence d'intégration)**

| Société | Calcul | IS |
|---|---|---|
| Delta Invest | 36 500 × 15 % | 5 475,00 € |
| Bâtisseurs du Sud | 42 500 × 15 % + 267 500 × 25 % = 6 375 + 66 875 | 73 250,00 € |
| Menuiserie | déficit | 0,00 € |
| **Total** | | **78 725,00 €** |

**Économie d'intégration** : 78 725,00 − 37 375,00 = **41 350,00 €**, qui se décompose ainsi :

| Origine | Calcul | Montant |
|---|---|---|
| Neutralisation de l'abandon (charge non déductible chez Delta, absorbée au niveau du groupe) | 120 000 × 25 % | 30 000,00 € |
| Imputation du déficit propre de la Menuiserie | 60 000 × 25 % | 15 000,00 € |
| Perte d'un plafond à 15 % (un seul plafond pour le groupe au lieu de deux) | 36 500 × (25 % − 15 %) | − 3 650,00 € |
| **Total** | | **41 350,00 €** ✓ |

**Soldes**
- Delta / SIE : acomptes 40 000,00 − IS du groupe 37 375,00 = **excédent de 2 625,00 €** (remboursable ou imputable, relevé de solde 2572 du groupe).
- Bâtisseurs du Sud / Delta : 73 250,00 − 68 000,00 = **5 250,00 € à verser à Delta**.
- Charge nette d'IS chez Delta : 37 375,00 − 73 250,00 = **− 35 875,00 €** (produit net d'intégration).

**Résultats nets 2026**

| | Résultat avant IS | IS (charge) / produit d'intégration | Résultat net |
|---|---|---|---|
| Delta Invest | 65 000,00 € | − 37 375,00 + 73 250,00 | **100 875,00 €** |
| Bâtisseurs du Sud | 302 600,00 € | − 73 250,00 | **229 350,00 €** |
| Menuiserie | − 62 000,00 € | 0,00 | **− 62 000,00 €** |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| *Chez Bâtisseurs du Sud* | | | | | | |
| 31/12/2026 | OD | 695 | Impôts sur les bénéfices | IS 2026 dû à la mère (convention d'intégration) | 73 250,00 | |
| 31/12/2026 | OD | 451DELTA | Groupe – compte courant Delta Invest | IS 2026 dû à la mère (convention d'intégration) | | 73 250,00 |
| *Chez Delta Invest* | | | | | | |
| 31/12/2026 | OD | 695 | Impôts sur les bénéfices | IS du groupe intégré 2026 | 37 375,00 | |
| 31/12/2026 | OD | 444 | État – impôts sur les bénéfices | IS du groupe intégré 2026 | | 37 375,00 |
| 31/12/2026 | OD | 451BDS | Groupe – compte courant Bâtisseurs du Sud | Contribution IS 2026 de Bâtisseurs du Sud | 73 250,00 | |
| 31/12/2026 | OD | 6989 | Intégration fiscale – produits | Contribution IS 2026 de Bâtisseurs du Sud | | 73 250,00 |
| *Chez la Menuiserie* | | | | | | |
| — | — | — | — | Aucune écriture d'IS (déficit, convention de neutralité) | — | — |
| | | | | **Totaux** | **183 875,00** | **183 875,00** |

*Compte 698 « Intégration fiscale » (6981 charges / 6989 produits) : subdivision selon la nomenclature 2025 du PCG ; certains dossiers créditent directement le 695 — présentation à garder constante.*

**Pour mémoire (déjà comptabilisées en cours d'année)** : chez Delta, acomptes D 444 / C 512 (40 000) et encaissements des contributions de Bâtisseurs du Sud D 512 / C 451BDS (68 000) ; chez Bâtisseurs du Sud, D 451DELTA / C 512 (68 000). L'abandon de créance : chez Delta, D 668 Autres charges financières (*subdivision selon la nomenclature 2025*) / C 4551 Compte courant Menuiserie 120 000 ; chez la Menuiserie, D 4551 Delta / C 768 120 000.

**Après ces écritures** : 444 chez Delta débiteur de 2 625 € (créance sur l'État) ; 451 Bâtisseurs du Sud débiteur de 5 250 € chez Delta ; 451 Delta créditeur de 5 250 € chez Bâtisseurs du Sud (réciprocité à contrôler).

## 4. Points d'attention / pièges

- **Ne pas neutraliser deux fois** : l'abandon étant déjà non déductible chez Delta, seule la déduction du produit chez la Menuiserie est à opérer au niveau du groupe. Si l'abandon avait été **déductible** chez Delta (abandon commercial, ou dans une procédure), il aurait fallu, en plus, réintégrer la charge.
- **Quote-part de 1 %, pas de 5 %**, pour des dividendes reçus d'une filiale intégrée — et pas de neutralisation supplémentaire.
- **Un seul plafond à 15 %** pour le groupe : l'économie est rognée de 3 650 €. Une convention mal rédigée qui ferait payer aux filiales un IS « au taux du groupe » créerait des transferts entre sociétés.
- **Chez la filiale, jamais de 444** : sa dette d'IS est envers la mère.
- **Réciprocité** des comptes courants 451 entre sociétés du groupe : à rapprocher à chaque clôture.
- **Dépréciation des titres de la Menuiserie** chez Delta : si elle était dotée, elle relèverait du régime des plus ou moins-values à long terme sur titres de participation (non déductible en pratique) — retraitement à prévoir sur la 2058-A, sans effet de neutralisation spécifique.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 5 — Provision pour restitution ?** L'avis du Comité d'urgence du CNC n° 2005-G admet que l'économie liée aux déficits d'une filiale est un **gain immédiat** de la mère, mais impose une **provision** lorsque la mère aura l'obligation probable de la **réallouer** à la filiale (restitution en trésorerie, indemnisation à la sortie). Ici, la convention exclut toute indemnité (art. 3 et 6) → **pas de provision**. En revanche, la situation de la Menuiserie (capitaux propres négatifs, prévisionnel tendu) rend une **sortie du groupe** possible : à décrire dans l'**annexe** de Delta (engagements et risques liés à l'intégration). À réexaminer à chaque clôture.

**Question 6 — Note à Jean Delmas :**

> Bonjour Jean,
>
> Votre banquier a en partie raison. Pris isolément, l'abandon de 120 000 € n'est pas déductible chez Delta Invest. Mais grâce à l'intégration, le groupe ne paie pas d'impôt sur ce flux interne : l'IS du groupe 2026 est estimé à **37 375 €** au lieu de **78 725 €** si chaque société était imposée seule (économie de **41 350 €**, dont 30 000 € liés à l'abandon et 15 000 € au déficit de la Menuiserie).
>
> En revanche, l'abandon **coûte** bien 120 000 € à Delta en trésorerie et en patrimoine : c'est une créance à laquelle vous renoncez. La clause de retour à meilleure fortune vous permettra de la récupérer en partie si la Menuiserie redevient bénéficiaire (la somme alors remboursée sera un produit imposable chez Delta et une charge chez la Menuiserie, à neutraliser de nouveau tant que les deux sont dans le groupe).
>
> Trois points d'attention :
> 1. **Antoine Girard** détient 5 % de la Menuiserie : l'abandon enrichit aussi sa participation ; prévoyez une justification de l'intérêt de Delta dans le procès-verbal (sauvegarde de la filiale, de son fonds et des emplois).
> 2. **Capitaux propres de la Menuiserie** : même après l'abandon, ils resteraient négatifs (environ − 18 000 € pour un capital de 50 000 €) ; une AGE devra statuer sur la poursuite de l'activité dans les 4 mois de l'approbation des comptes (C. com. art. L. 223-42). Un abandon plus important ou une augmentation de capital peut être nécessaire.
> 3. Si Delta descendait sous **95 %** de la Menuiserie (par exemple en cas d'augmentation de capital souscrite par un tiers), la Menuiserie sortirait du groupe.
>
> Bâtisseurs du Sud devra verser à Delta 5 250 € de solde d'IS ; Delta récupérera 2 625 € d'excédent d'acomptes auprès du SIE.

**Contrôles et documentation** : convention d'intégration signée et à jour au dossier juridique ; liste des sociétés du groupe et pourcentages au 31/12 ; tableaux 2058-ER / 2058-ES / 2058-RG ; rapprochement des 451 réciproques ; suivi pluriannuel des déficits propres de la Menuiserie (pour l'application de l'article 2 de la convention) ; engagement de retour à meilleure fortune mentionné dans l'annexe de la Menuiserie (engagement hors bilan) et de Delta ; vérification de la **convention réglementée** (abandon consenti à une société ayant un dirigeant ou associé commun) et de son approbation.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 223 A à 223 U (intégration fiscale), notamment art. 223 B (résultat d'ensemble, neutralisation des abandons de créances et subventions intra-groupe) et art. 223 F (cessions d'immobilisations).
- CGI art. 145 et 216 (régime mère-fille, quote-part de frais et charges de 5 % / 1 %).
- CGI art. 39, 13 (déductibilité des aides et abandons de créances) ; art. 219 (taux d'IS).
- Avis du Comité d'urgence du CNC n° 2005-G (comptabilisation de l'IS dans les groupes intégrés).
- Code de commerce art. L. 223-42 (capitaux propres inférieurs à la moitié du capital, SARL) ; art. L. 223-19 / L. 227-10 (conventions réglementées).
- BOFiP : BOI-IS-GPE (régime de groupe).
