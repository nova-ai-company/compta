# Corrigé E15-14 — Du compte de résultat à l'IS : EBE, résultat fiscal et écritures d'impôt

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-14](../exercices/E15-14_resultat-comptable-sig-is.md)

*Rappel : société et montants fictifs.*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Résultat comptable avant IS
4 885 000 − 4 475 000 = **410 000 €** (bénéfice).

### Question 2 — Les SIG, en partant du haut
Chaque solde « enlève » une famille de charges de plus :
- **Valeur ajoutée** = ce que l'entreprise produit − ce qu'elle achète à l'extérieur. Pour une entreprise de propreté, elle est très élevée car le cœur du métier, c'est le **personnel**.
- **EBE** (excédent brut d'exploitation) = valeur ajoutée − impôts et taxes − charges de personnel (+ subventions d'exploitation, ici aucune). C'est la ressource dégagée par l'activité **avant** amortissements, financement et impôt : l'indicateur que regardent le plus les directions opérationnelles.
- **Résultat d'exploitation** = EBE + reprises + autres produits − dotations − autres charges. **Les amendes (dans les autres charges de gestion courante) sont ici** : depuis le règlement ANC n° 2022-06, elles ne vont plus en exceptionnel.
- **Résultat financier** = produits financiers − charges financières.
- **Résultat courant avant impôts** = exploitation + financier.
- **Résultat exceptionnel** : la **cession d'immobilisation** (775 − 675) y reste.

### Question 3 — Réintégrations
Le résultat fiscal part du résultat comptable, puis on **ajoute** (réintègre) les charges que le fisc refuse :
- **Amendes** : 4 200 € — une amende sanctionne une infraction, la loi interdit de la déduire.
- **Voiture de tourisme** : l'amortissement n'est déductible que sur la base du plafond (18 300 €). La part de l'amortissement calculée sur la fraction du prix au-dessus du plafond est réintégrée.

Il n'y a pas d'IS à réintégrer ici, car le résultat de 410 000 € est **avant** IS (voir question 6).

### Question 4 — IS et solde
Tout le résultat fiscal est taxé à 25 % (pas de taux réduit pour une filiale de grand groupe). Les acomptes déjà versés (98 000 €) viennent en déduction : il reste un **solde à payer**.

### Question 6 — L'IS n'est pas déductible
L'IS est calculé **sur** le bénéfice : s'il était déductible de ce bénéfice, on tournerait en rond (l'impôt réduirait la base de l'impôt). La loi prévoit donc qu'il n'est pas déductible. Si une charge d'IS figurait déjà dans le résultat comptable (compte 695), il faudrait la **réintégrer** pour revenir au résultat avant impôt, puis calculer l'impôt. Dans notre cas, le résultat fourni est avant IS : on n'a rien à réintégrer à ce titre.

## 2. Calculs (détaillés, chaque montant justifié)

**SIG (question 2)**

| Solde | Calcul | Montant (€) |
|---|---|---|
| Production de l'exercice | Prestations vendues | 4 850 000 |
| Consommation en provenance des tiers | 312 000 + 618 000 | 930 000 |
| **Valeur ajoutée** | 4 850 000 − 930 000 | **3 920 000** |
| Charges de personnel | 2 520 000 + 760 000 | 3 280 000 |
| **EBE** | 3 920 000 − 96 000 − 3 280 000 | **544 000** |
| **Résultat d'exploitation** | 544 000 + 15 000 + 6 000 − 118 000 − 22 000 − 8 000 | **417 000** |
| Résultat financier | 2 000 − 14 000 | − 12 000 |
| **Résultat courant avant impôts** | 417 000 − 12 000 | **405 000** |
| Résultat exceptionnel | 12 000 − 7 000 | 5 000 |
| **Résultat avant IS** | 405 000 + 5 000 | **410 000** ✓ |

Ratio utile à commenter : EBE / chiffre d'affaires = 544 000 / 4 850 000 = **11,2 %**.

**Résultat fiscal et IS (questions 3 et 4)**

| Élément | Calcul | Montant (€) |
|---|---|---|
| Amortissement comptable de la voiture | 42 000 / 5 | 8 400 |
| Amortissement fiscalement déductible | 18 300 / 5 | 3 660 |
| **Réintégration voiture** | 8 400 − 3 660 (= (42 000 − 18 300) / 5) | **4 740** |
| Réintégration amendes | | 4 200 |
| **Résultat fiscal** | 410 000 + 4 200 + 4 740 | **418 940** |
| **IS 2025** | 418 940 × 25 % | **104 735** |
| Acomptes versés en 2025 | 98 000 / 4 = 24 500 × 4 | 98 000 |
| **Solde à payer le 15/05/2026** | 104 735 − 98 000 | **6 735** |
| **Résultat net comptable** | 410 000 − 104 735 | **305 265** |

**Question bonus (PME éligible)** : 42 500 × 15 % = 6 375 ; (418 940 − 42 500) × 25 % = 376 440 × 25 % = 94 110 ; IS = 6 375 + 94 110 = **100 485 €** (soit 4 250 € d'économie, = 42 500 × 10 %).

## 3. Écritures comptables

**Pourquoi ces comptes** : un acompte d'IS n'est pas encore une charge, c'est une **avance** versée à l'État → on débite le compte d'État **444** (et on crédite la banque). Au 31/12, on constate la **charge** d'impôt de l'année (débit **695**) en contrepartie du 444. Le 444 devient alors **créditeur** de 6 735 € : c'est la dette d'IS restant à payer, soldée le 15/05/2026.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/03/2025 | BQ | 444 | État – impôt sur les bénéfices | 1er acompte IS 2025 | 24 500,00 | |
| 15/03/2025 | BQ | 512 | Banque | 1er acompte IS 2025 | | 24 500,00 |
| 15/06/2025 | BQ | 444 | État – impôt sur les bénéfices | 2e acompte IS 2025 | 24 500,00 | |
| 15/06/2025 | BQ | 512 | Banque | 2e acompte IS 2025 | | 24 500,00 |
| 15/09/2025 | BQ | 444 | État – impôt sur les bénéfices | 3e acompte IS 2025 | 24 500,00 | |
| 15/09/2025 | BQ | 512 | Banque | 3e acompte IS 2025 | | 24 500,00 |
| 15/12/2025 | BQ | 444 | État – impôt sur les bénéfices | 4e acompte IS 2025 | 24 500,00 | |
| 15/12/2025 | BQ | 512 | Banque | 4e acompte IS 2025 | | 24 500,00 |
| 31/12/2025 | OD | 695 | Impôts sur les bénéfices | IS exercice 2025 (418 940 × 25 %) | 104 735,00 | |
| 31/12/2025 | OD | 444 | État – impôt sur les bénéfices | IS exercice 2025 | | 104 735,00 |
| 15/05/2026 | BQ | 444 | État – impôt sur les bénéfices | Solde IS 2025 | 6 735,00 | |
| 15/05/2026 | BQ | 512 | Banque | Solde IS 2025 | | 6 735,00 |
| | | | | **Totaux** | **209 470,00** | **209 470,00** |

Contrôle du 444 au 31/12/2025 : débits 98 000 − crédit 104 735 = **6 735 € créditeur** (dette) ✓ ; soldé à zéro le 15/05/2026 ✓.

## 4. Points d'attention / pièges

- **Confondre EBE et résultat d'exploitation** : l'EBE est **avant** dotations aux amortissements et provisions.
- **Mettre les amendes en exceptionnel** : plus depuis le règlement ANC n° 2022-06 (charges d'exploitation, 658 — *subdivision selon la nomenclature 2025 du PCG*). Mais elles restent **non déductibles** fiscalement : classement comptable et traitement fiscal sont deux questions différentes.
- **Cession** : elle reste en exceptionnel (675 / 775) ; ce n'est pas une contradiction avec la règle précédente, c'est une exception prévue par le nouveau PCG.
- **Voiture** : réintégrer tout l'amortissement (8 400) est faux ; seule la part au-delà du plafond est réintégrée (4 740).
- **Acomptes en 695** : passer les acomptes directement en charge fausse le résultat en cours d'année ; ils vont en 444.
- **Signe du 444** : débiteur = l'État nous doit (trop d'acomptes, à se faire rembourser) ; créditeur = on doit un solde.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Ce que le recruteur attend** : des SIG dans le bon ordre avec un **contrôle** (on retombe sur 410 000), deux réintégrations justifiées en une phrase chacune, un IS juste et une explication claire du 444. Savoir dire « l'EBE de 11,2 % du chiffre d'affaires est cohérent pour un métier de main-d'œuvre » montre que vous lisez les chiffres, pas seulement que vous les calculez.

**En pratique** : le calcul est reporté sur le tableau de détermination du résultat fiscal de la liasse (réintégrations), et le solde est payé avec le relevé de solde d'IS ; on garde dans le dossier le détail du plafond retenu pour la voiture (carte grise, taux d'émission).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : soldes intermédiaires de gestion ; comptes 444, 695, 675, 775 ; règlement ANC n° 2022-06 (résultat exceptionnel restreint).
- CGI art. 39-2 (amendes non déductibles) ; art. 39-4 (plafond d'amortissement des véhicules de tourisme) ; art. 213 (IS non déductible) ; art. 219 (taux de l'IS et taux réduit PME) ; art. 1668 (acomptes et solde de l'IS) (*à vérifier*).
- BOFiP-IS : liquidation et paiement de l'IS.
