# Corrigé E07-04 — Dette provisionnée pour congés payés au 31/12 et charges sociales

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-04](../exercices/E07-04_provision-conges-payes-imprimerie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **Nature de la dette** : les jours de congés acquis et non pris à la clôture sont une **dette certaine** envers les salariés (charge à payer, pas une provision au sens du PCG), évaluée **salarié par salarié**, avec les **charges sociales patronales** qui seront dues lors du versement.
2. **Qui a droit ?** Seuls les **salariés** présents à la clôture. Un **mandataire social sans contrat de travail** (Laurent Chevalier, DG) n'acquiert pas de congés payés au sens du Code du travail (sauf stipulation statutaire ou décision du conseil, ici inexistante). Un **salarié sorti** (Hervé Guichard) a été réglé de ses droits par l'indemnité compensatrice versée au solde de tout compte : plus aucune dette.
3. **Arrêt maladie** : depuis la loi n° 2024-364 du 22/04/2024, le salarié en arrêt pour maladie non professionnelle **continue d'acquérir** des congés : 2 jours ouvrables par mois (plafond 24 jours par période de référence). Sabine a arrêté les droits de Nathalie Simon au 31/08 : c'est la règle **d'avant 2024**. En AT/MP, l'acquisition est de 2,5 jours par mois sans limite d'un an : Karim Haddad est correct.
4. **Report de 15 mois** : les 12 jours de Ludovic Marchal, reportés après sa maladie et notifiés le 02/02/2026, restent dus jusqu'à la fin de la période de report : dette à maintenir.
5. **Valorisation** : le salarié perçoit la plus favorable des deux méthodes (1/10e ou maintien). Pour un salarié avec beaucoup d'éléments variables (HS, primes de nuit), le 1/10e est souvent supérieur au maintien calculé sur le seul salaire de base : il faut le vérifier.
6. **Taux de charges** : appliquer le **taux réel** (charges patronales nettes de la réduction générale / brut), pas un taux « facial » de 45 % — c'est la remarque du CAC.

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 Nathalie Simon et Karim Haddad

| Salarié | Période | Calcul | Jours |
|---|---|---|---|
| N. Simon | 01/06 → 31/08/2026 (travail) | 3 mois × 2,5 | 7,5 |
| | 01/09 → 31/12/2026 (maladie non pro.) | 4 mois × 2 (cumul 8 j < plafond 24 j) | 8 |
| | En cours | | **15,5** |
| | Reliquat N-1 | | 10 |
| | **Total** | | **25,5** |
| K. Haddad | 01/07 → 31/12/2026 (AT) + juin travaillé | 7 mois × 2,5 | **17,5** ✔ |

Valorisation N. Simon (maintien) : 2 300,00 / 26 × 25,5 = **2 255,77 €** (au lieu de 1 548,08 €).

### 2.2 Paul Roche : 1/10e ou maintien

| Droits | Maintien (salaire / 26 × j) | 1/10e | Retenu |
|---|---|---|---|
| Reliquat N-1 : 6 j | 2 900 / 26 × 6 = 669,23 | 36 200 × 10 % = 3 620,00 pour 30 j → 3 620 / 30 × 6 = 724,00 | **724,00** |
| En cours : 17,5 j | 2 900 / 26 × 17,5 = 1 951,92 | 21 600 × 10 % = **2 160,00** (indemnité des 17,5 j acquis sur la période) | **2 160,00** |
| **Total** | 2 621,15 | 2 884,00 | **2 884,00** |

### 2.3 Dette corrigée au 31/12/2026

| Salarié | Valorisation Sabine | Valorisation corrigée | Écart | Motif |
|---|---|---|---|---|
| P. Roche | 2 621,15 | 2 884,00 | + 262,85 | 1/10e plus favorable |
| N. Simon | 1 548,08 | 2 255,77 | + 707,69 | acquisition pendant la maladie (8 j) |
| K. Haddad | 1 682,69 | 1 682,69 | 0,00 | |
| L. Marchal | 3 063,46 | 3 063,46 | 0,00 | report de 15 mois |
| L. Chevalier | 6 634,62 | 0,00 | − 6 634,62 | mandataire sans contrat de travail |
| H. Guichard | 820,00 | 0,00 | − 820,00 | sorti, indemnité versée |
| Autres (48) | 158 340,00 | 158 340,00 | 0,00 | |
| **Total** | **174 710,00** | **168 225,92** | **− 6 484,08** | |

### 2.4 Charges sociales
- Taux réel : 1 018 718 / 2 666 800 = **38,20 %**.
- Charges sur la dette : 168 225,92 × 38,20 % = **64 262,30 €** (Sabine : 78 619,50 € ; surévaluation de 14 357,20 €).

### 2.5 Variations (méthode de l'ajustement)
- 4282 : 168 225,92 − 162 500,00 = **+ 5 725,92 €** (dotation complémentaire).
- 4382 : 64 262,30 − 73 125,00 = **− 8 862,70 €** (diminution : le taux de 45 % de l'an dernier surévaluait déjà la dette).

> Remarque : la diminution du 4382 corrige en partie une surévaluation de l'exercice 2025. Il s'agit d'un **changement d'estimation** (affinement du taux), traité en résultat de l'exercice 2026, pas d'une correction d'erreur. Si le montant était significatif, le mentionner en annexe.

## 3. Écritures comptables

**Méthode de l'ajustement (retenue par le dossier)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6412 | Congés payés | Ajustement dette CP 31/12/2026 | 5 725,92 | |
| 31/12/2026 | OD | 4282 | Dettes provisionnées pour congés à payer | Ajustement dette CP 31/12/2026 | | 5 725,92 |
| 31/12/2026 | OD | 4382 | Charges sociales sur congés à payer | Ajustement charges sociales CP | 8 862,70 | |
| 31/12/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance – charges sociales sur CP (*subdivision selon la nomenclature 2025 du PCG*) | Ajustement charges sociales CP | | 8 862,70 |
| | | | | **Totaux** | **14 588,62** | **14 588,62** |

**Alternative : méthode de l'extourne**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/01/2026 | OD | 4282 | Dettes provisionnées pour congés à payer | Extourne dette CP 31/12/2025 | 162 500,00 | |
| 01/01/2026 | OD | 6412 | Congés payés | Extourne dette CP 31/12/2025 | | 162 500,00 |
| 01/01/2026 | OD | 4382 | Charges sociales sur congés à payer | Extourne charges CP 31/12/2025 | 73 125,00 | |
| 01/01/2026 | OD | 645 | Charges sociales sur CP (*subdivision selon la nomenclature 2025*) | Extourne charges CP 31/12/2025 | | 73 125,00 |
| 31/12/2026 | OD | 6412 | Congés payés | Dette CP 31/12/2026 | 168 225,92 | |
| 31/12/2026 | OD | 4282 | Dettes provisionnées pour congés à payer | Dette CP 31/12/2026 | | 168 225,92 |
| 31/12/2026 | OD | 645 | Charges sociales sur CP (*subdivision selon la nomenclature 2025*) | Charges sociales sur dette CP | 64 262,30 | |
| 31/12/2026 | OD | 4382 | Charges sociales sur congés à payer | Charges sociales sur dette CP | | 64 262,30 |
| | | | | **Totaux** | **468 113,22** | **468 113,22** |

Impact net en résultat identique : + 5 725,92 − 8 862,70 = **− 3 136,78 €** de charges (produit net de 3 136,78 €).

## 4. Points d'attention / pièges

- **Taux facial vs taux réel** : avec la réduction générale, les salariés proches du SMIC ont un taux patronal réel bien inférieur à 45 %. Pour une population hétérogène, un taux moyen global est acceptable si la structure des salaires est stable ; sinon, appliquer des taux par tranche de salaire.
- **Loi 2024** : les droits acquis pendant la maladie sont à intégrer **pour toute la période d'arrêt**, et les rappels rétroactifs (depuis 2009, sous réserve des délais de forclusion et de prescription) constituent un **risque** à apprécier : si des salariés ont réclamé ou si le risque est probable, une **provision pour risques** peut être nécessaire (distincte de la dette CP).
- **Report de 15 mois** : ne pas « purger » les jours reportés en fin de période de référence ; mais au terme du délai de report (si l'employeur a bien informé le salarié), les jours non pris sont perdus.
- **Mandataires sociaux** : pas de CP sauf contrat de travail cumulé (fonctions techniques distinctes, rémunération séparée, subordination) — vérifiez le dossier juridique.
- **Salariés sortis** : vérifier que leur indemnité compensatrice a bien été versée (sinon c'est une dette au 421, pas au 4282).
- Le CAC testera : rapprochement de l'état avec le registre du personnel, calcul sur un échantillon, cohérence du taux de charges avec la paie, traitement des absences longues.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- Demander à Sabine l'**état détaillé des 48 autres salariés** extrait du logiciel de paie (compteurs CP au 31/12) et vérifier que le logiciel a bien été mis à jour pour la loi 2024 (paramétrage des absences maladie).
- Contrôler par sondage la **comparaison 1/10e / maintien** sur les salariés à forte part variable (conducteurs de nuit).
- Documenter dans le dossier de travail le **calcul du taux réel** et le faire valider par le CAC avant le *hard close*.
- **Mail à Sabine Morel** :

> Bonjour Sabine,
> Merci pour votre état. Après revue, la dette de congés payés au 31/12/2026 s'élève à 168 225,92 € et les charges sociales associées à 64 262,30 € :
> – Laurent Chevalier, mandataire sans contrat de travail, n'acquiert pas de congés payés ; Hervé Guichard a été réglé de ses droits à sa sortie : ces deux lignes sont à retirer ;
> – depuis la loi du 22 avril 2024, Nathalie Simon continue d'acquérir 2 jours par mois pendant son arrêt maladie : 25,5 jours au total ;
> – pour Paul Roche, la méthode du dixième (primes de nuit et heures supplémentaires) est plus favorable que le maintien : 2 884,00 € ;
> – le taux de charges à retenir est le taux réel 2026, soit 38,20 %, conformément à la remarque du commissaire aux comptes.
> Pourriez-vous nous transmettre l'export des compteurs de congés des 48 autres salariés et nous confirmer la mise à jour du logiciel pour la loi de 2024 ?
> Bien cordialement,

## 6. Références

- Code du travail : articles L. 3141-3 (acquisition 2,5 jours par mois), L. 3141-5 et L. 3141-5-1 (périodes assimilées, acquisition pendant la maladie non professionnelle), L. 3141-19-1 et suivants (report de 15 mois et information du salarié), L. 3141-24 (indemnité : 1/10e ou maintien), L. 3141-28 (indemnité compensatrice) — issus ou modifiés par la loi n° 2024-364 du 22 avril 2024.
- PCG : comptes 4282 et 4382, 6412, 645 ; dettes provisionnées (charges à payer).
- Règlement ANC n° 2014-03, article 322-1 et suivants (distinction passifs / provisions) ; changements d'estimation (traitement prospectif en résultat).
