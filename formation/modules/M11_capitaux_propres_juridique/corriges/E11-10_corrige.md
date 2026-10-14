# Corrigé E11-10 — Garage Martin : le juridique annuel d'une EURL

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-10](../exercices/E11-10_juridique-annuel-garage-martin.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**L'urgence d'abord : les intérêts de compte courant.** L'**inscription** des intérêts au crédit du compte courant de Thierry, le 30/09/2026, vaut **paiement** (mise à disposition des sommes). À cette date, la société devait :
- opérer le **PFNL de 12,8 %** (acompte d'IR) et les **prélèvements sociaux** sur les intérêts versés à un associé personne physique ;
- les **déclarer et payer** avec l'imprimé **2777** au plus tard le **15 du mois suivant**, soit le **15/10/2026** — dans six jours.

**La déductibilité** : les intérêts versés aux associés sont déductibles si le capital est entièrement libéré (✓) et dans la limite du **taux maximum** (5,10 % retenu). Au-delà, la fraction excédentaire est **réintégrée** (et peut être regardée comme un revenu distribué chez Thierry).

**L'approbation des comptes dans une EURL dont l'associé unique personne physique est gérant** : le **dépôt au greffe**, dans les **6 mois** de la clôture, de l'inventaire et des comptes annuels **dûment signés vaut approbation** (art. L. 223-31 C. com.). Il n'y a ni assemblée ni rapport du gérant à « s'adresser à lui-même ». Mais :
- la **décision d'affectation** du résultat doit être prise et **répertoriée dans le registre** des décisions, puis déposée avec les comptes ;
- la **mention au registre** des conventions conclues avec l'associé unique reste obligatoire.

Thierry a raison sur la forme (« je signe et vous déposez »), mais oublie que le registre n'a rien d'une formalité vide : sans mention, pas de preuve de la décision d'affectation ni de la convention.

## 2. Calculs (détaillés, chaque montant justifié)

**Intérêts de compte courant**

| Élément | Calcul | Montant |
|---|---|---|
| Intérêts comptabilisés | 40 000 × 6 % | 2 400,00 |
| Intérêts déductibles | 40 000 × 5,10 % | 2 040,00 |
| **Réintégration fiscale** (2058-A) | 2 400 – 2 040 | **360,00** |
| PFNL 12,8 % sur les intérêts bruts | 2 400 × 12,8 % | 307,20 |
| Prélèvements sociaux 18,6 % | 2 400 × 18,6 % | 446,40 |
| **Total à déclarer sur la 2777 (15/10/2026)** | | **753,60** |
| Compte courant après retenues | 42 400 – 753,60 | 41 646,40 |

**Affectation du résultat**

| Élément | Calcul | Montant |
|---|---|---|
| Réserve légale | 5 % × 48 900 = 2 445 ; plafond 10 % × 15 000 = 1 500 ; déjà 1 100 → manquant 400 | **400,00** |
| Bénéfice distribuable | 48 900 – 400 + 4 300 | 52 800,00 |
| Dividendes | souhait de Thierry (≤ 52 800 ✓) | 20 000,00 |
| Autres réserves | | 20 000,00 |
| Report à nouveau (affecté) | 48 900 – 400 – 20 000 – 20 000 | 8 500,00 |
| Report à nouveau après affectation | 4 300 + 8 500 | 12 800,00 |

**Dividende de 20 000 € (paiement le 15/04/2027)**
- Seuil des 10 % (gérant associé unique, travailleur indépendant) : 10 % × (capital 15 000 + primes 0 + compte courant 40 000) = **5 500,00 €** (*compte courant retenu pour son solde de l'exercice, 40 000 € ; modalité d'appréciation — solde ou moyenne — à vérifier*).
- Fraction soumise aux prélèvements sociaux : 5 500 € ; fraction soumise aux cotisations TNS : **14 500 €**.
- PFNL : 20 000 × 12,8 % = **2 560,00 €** ; prélèvements sociaux : 5 500 × 18,6 % = **1 023,00 €**.
- **Net versé : 20 000 – 2 560 – 1 023 = 16 417,00 €**.
- Cotisations TNS à prévoir (déclaration de revenus d'indépendant) : 14 500 × 40 % ≈ **5 800,00 €** (estimation).
- 2777 : au plus tard le **15/05/2027** pour 3 583,00 €.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 4551 | Compte courant T. Martin | Retenues à la source sur intérêts CC 2025-2026 (2 400 €) | 753,60 | |
| 30/09/2026 | OD | 4422 | Prélèvements forfaitaires non libératoires | PFNL 12,8 % intérêts CC T. Martin | | 307,20 |
| 30/09/2026 | OD | 4423 | Retenues et prélèvements sur distributions | Prélèvements sociaux 18,6 % intérêts CC T. Martin | | 446,40 |
| 15/10/2026 | BQ | 4422 | Prélèvements forfaitaires non libératoires | 2777 – septembre 2026 | 307,20 | |
| 15/10/2026 | BQ | 4423 | Retenues et prélèvements sur distributions | 2777 – septembre 2026 | 446,40 | |
| 15/10/2026 | BQ | 512 | Banque | Télérèglement 2777 – septembre 2026 | | 753,60 |
| 31/03/2027 | OD | 120 | Résultat de l'exercice (bénéfice) | Affectation résultat 30/09/2026 – décision de l'associé unique | 48 900,00 | |
| 31/03/2027 | OD | 1061 | Réserve légale | Dotation (plafond 10 % du capital atteint) | | 400,00 |
| 31/03/2027 | OD | 1068 | Autres réserves | Dotation | | 20 000,00 |
| 31/03/2027 | OD | 457 | Associés – dividendes à payer | Dividende T. Martin (13,333 €/part) | | 20 000,00 |
| 31/03/2027 | OD | 110 | Report à nouveau (solde créditeur) | Solde du bénéfice | | 8 500,00 |
| 15/04/2027 | BQ | 457 | Associés – dividendes à payer | Paiement dividende | 20 000,00 | |
| 15/04/2027 | BQ | 4422 | Prélèvements forfaitaires non libératoires | PFNL 12,8 % | | 2 560,00 |
| 15/04/2027 | BQ | 4423 | Retenues et prélèvements sur distributions | Prélèvements sociaux 18,6 % sur 5 500 € | | 1 023,00 |
| 15/04/2027 | BQ | 512 | Banque | Vir. dividende net T. Martin | | 16 417,00 |
| 15/05/2027 | BQ | 4422 | Prélèvements forfaitaires non libératoires | 2777 – avril 2027 | 2 560,00 | |
| 15/05/2027 | BQ | 4423 | Retenues et prélèvements sur distributions | 2777 – avril 2027 | 1 023,00 | |
| 15/05/2027 | BQ | 512 | Banque | Télérèglement 2777 – avril 2027 | | 3 583,00 |
| | | | | **Totaux** | **73 990,20** | **73 990,20** |

> La retenue est imputée sur le compte courant (la société a « payé » 2 400 € brut en inscrivant cette somme ; elle reverse 753,60 € à l'État pour le compte de Thierry). L'écriture est datée du 30/09/2026 (exercice clos) : elle est passée **avant l'arrêté des comptes**. La réintégration de 360 € est extra-comptable (2058-A). Le dividende de 20 000 € pour 1 500 parts représente 13,333 € par part (montant non arrondi admis ; on peut aussi retenir 13,30 € × 1 500 = 19 950 €).

## 4. Points d'attention / pièges

- **Inscription en compte courant = paiement** : intérêts (et dividendes) portés au crédit d'un compte courant déclenchent immédiatement les retenues et la 2777. Oubli très fréquent chez les dirigeants qui « passent leurs intérêts » eux-mêmes en fin d'exercice. Le retard expose à l'intérêt de retard et aux majorations (*à chiffrer si l'échéance est manquée*).
- **Taux maximum** : à vérifier pour **chaque exercice** selon sa date de clôture ; l'excédent est réintégré et la rémunération devrait être ramenée au taux maximum pour l'avenir.
- **Réserve légale plafonnée** : 400 € et non 2 445 €.
- **Gérant associé unique d'EURL à l'IS** = gérant majoritaire → règle des 10 % : son compte courant **relève** le seuil (40 000 € → + 4 000 €).
- **Dépôt valant approbation** : dans les **6 mois** de la clôture, soit au plus tard le **31/03/2027**. Un dépôt en avril ferait perdre l'effet d'approbation et placerait la société hors délai.
- **Amortissements dérogatoires** (6 800 €) : provisions réglementées, partie intégrante des capitaux propres ; ils varient au compte de résultat, pas par l'affectation.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 2 — Calendrier**

| Échéance | Action |
|---|---|
| **15/10/2026** | **2777** des intérêts de compte courant (753,60 €) |
| Décembre 2026 | Liasse IS (exercice clos le 30/09/2026) ; réintégration de 360 € |
| Avant le **31/03/2027** | Comptes signés par Thierry ; décision d'affectation inscrite au registre ; **dépôt au greffe** (comptes + décision d'affectation + déclaration de confidentialité) — le dépôt **vaut approbation** |
| 15/04/2027 | Paiement du dividende (délai légal : 9 mois après la clôture, soit le 30/06/2027) |
| **15/05/2027** | **2777** du dividende (3 583,00 €) |
| Avant le 15/02/2027 et le 15/02/2028 | **IFU** 2026 (intérêts de compte courant) et IFU 2027 (dividende) |

**Question 3 — Décision de l'associé unique (registre)**

> **Décision de l'associé unique du 31 mars 2027.** M. Thierry Martin, associé unique et gérant de la société Garage Martin, EURL au capital de 15 000 €, après avoir arrêté et signé l'inventaire et les comptes annuels de l'exercice clos le 30 septembre 2026, faisant apparaître un bénéfice de 48 900,00 €, et dont le dépôt au greffe vaut approbation, décide d'affecter ce bénéfice de la manière suivante : réserve légale 400,00 €, portant celle-ci à 1 500,00 €, soit le dixième du capital ; autres réserves 20 000,00 € ; dividende 20 000,00 €, mis en paiement le 15 avril 2027 ; report à nouveau 8 500,00 €, portant celui-ci à 12 800,00 €. Il est rappelé que les dividendes distribués au titre des trois exercices précédents se sont élevés à : [*à compléter d'après le registre — art. 243 bis CGI*].
>
> **Conventions (art. L. 223-19 C. com.)** : il est fait mention au présent registre des conventions suivantes conclues entre la société et son associé unique : (1) bail commercial du local 45 avenue Jean Jaurès consenti par M. Thierry Martin, loyer de 3 000 € HT par mois après indexation pour l'exercice ; (2) rémunération de son compte courant d'associé au taux de 6 % pour l'exercice clos le 30/09/2026, ramené au taux maximum fiscalement déductible à compter du 01/10/2026 [*si décidé*].
>
> *Signature : Thierry Martin, associé unique et gérant.*

**Question 5 — Conventions** : dans une EURL dont l'associé unique est gérant, les conventions entre la société et lui ne font pas l'objet d'un rapport ni d'un vote : il en est **seulement fait mention au registre des décisions** (art. L. 223-19, al. 3). Le bail (convention continuant à produire effet) et la rémunération du compte courant (jamais formalisée) doivent être mentionnés **chaque année**. Au-delà du formalisme :
- vérifier que le **loyer** reste conforme au **marché** (un loyer excessif = acte anormal de gestion, excédent non déductible et revenu distribué) — demander une estimation de valeur locative ;
- **formaliser** la rémunération du compte courant par une décision écrite fixant le taux (au plus le taux maximum, pour éviter les réintégrations).

**Question 6 — Dépôt et confidentialité** :
- Micro-entreprise ? Critères : bilan 640 000 € > 450 000 € (dépassé) ; CA 1 150 000 € > 900 000 € (dépassé) ; effectif 5 ≤ 10 (non dépassé) → un seul critère non dépassé : **pas micro**.
- **Petite entreprise** : aucun seuil approché → elle peut demander que le **compte de résultat ne soit pas rendu public** (déclaration de confidentialité jointe au dépôt). Le **bilan** restera public. Thierry ne peut donc pas tout cacher, mais ses **marges** (compte de résultat) seront protégées (*seuils relevés en 2024, à vérifier*).
- **Rapport de gestion** : la SARL qui est une **petite entreprise** en est **dispensée** (art. L. 232-1 IV C. com.) ; de toute façon, dans l'EURL à associé unique gérant, le dépôt des comptes vaut approbation.

**Question 7 — Tableau de variation des capitaux propres**

| Poste | 30/09/2026 avant affectation | Affectation | Distribution | Après affectation |
|---|---|---|---|---|
| Capital | 15 000,00 | | | 15 000,00 |
| Réserve légale | 1 100,00 | + 400,00 | | 1 500,00 |
| Autres réserves | 22 000,00 | + 20 000,00 | | 42 000,00 |
| Report à nouveau | 4 300,00 | + 8 500,00 | | 12 800,00 |
| Résultat 2025-2026 | 48 900,00 | – 48 900,00 | | 0,00 |
| Dividendes | | + 20 000,00 | – 20 000,00 | 0,00 |
| Provisions réglementées (amort. dérogatoires) | 6 800,00 | | | 6 800,00 (avant mouvements de l'exercice suivant) |
| **Total capitaux propres** | **98 100,00** | **0,00** | **– 20 000,00** | **78 100,00** |

**Mail à Thierry (extrait)**

> Bonjour Thierry,
> 1. **Urgent** : les 2 400 € d'intérêts inscrits sur votre compte courant au 30/09 sont considérés comme payés à cette date. La société doit retenir 753,60 € (acompte d'impôt et prélèvements sociaux) et les déclarer avant le **15 octobre**. Nous nous en occupons ; votre compte courant sera réduit d'autant. Par ailleurs, au-delà de 5,10 %, les intérêts ne sont pas déductibles (360 € réintégrés) : nous vous proposons de fixer le taux par écrit à ce niveau pour l'avenir.
> 2. **Comptes** : signature et dépôt avant le **31 mars 2027** (le dépôt vaut approbation). Nous joindrons une déclaration de confidentialité : votre compte de résultat ne sera pas public.
> 3. **Dividende de 20 000 €** : possible. Vous recevrez 16 417 € net le 15 avril ; environ 14 500 € seront soumis à vos cotisations de travailleur indépendant (≈ 5 800 € à prévoir). Comparons avant mars avec une rémunération complémentaire.
> 4. **Bail et compte courant** : rien de compliqué, mais il faut les mentionner chaque année dans le registre ; nous préparons la page.

**Documentation** : registre à jour (décision d'affectation, conventions), accusé de dépôt et déclaration de confidentialité, accusés 2777, calcul du taux maximum archivé, estimation de la valeur locative à demander.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. **L. 223-31** (EURL : dépôt valant approbation, registre des décisions), art. **L. 223-19** al. 3 (conventions avec l'associé unique : mention au registre), art. L. 232-1 IV (dispense de rapport de gestion pour les petites entreprises), art. L. 232-10, L. 232-11, L. 232-13 (réserve légale, bénéfice distribuable, paiement dans les 9 mois), art. L. 232-22 et L. 232-25 (dépôt et option de confidentialité), art. L. 123-16 et L. 123-16-1 (seuils petites et micro-entreprises).
- CGI : art. 39-1-3° et 212 (intérêts des comptes courants, taux maximum), art. 125 A et 117 quater (PFNL), art. 200 A (PFU), art. 242 ter (IFU), art. 243 bis.
- Code de la sécurité sociale : art. L. 131-6 (règle des 10 %).
- PCG : comptes 1061, 1068, 110, 120, 145, 455, 457, 442 ; tableau de variation des capitaux propres en annexe.
