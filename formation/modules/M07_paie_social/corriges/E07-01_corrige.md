# Corrigé E07-01 — Journal de paie mensuel et contrôle de la DSN

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-01](../exercices/E07-01_journal-paie-boulangerie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **On comptabilise toujours à partir du journal de paie définitif**, jamais à partir des bulletins un par un ni de la DSN. Ici, deux versions de la paie coexistent : la simulation du 28/09 (sans les heures supplémentaires de Kévin) et l'édition définitive du 30/09 à 17 h 42. Le virement de salaires du 30/09 (8 353,07 €) correspond **exactement** au net payé du journal définitif : c'est donc lui qui fait foi.
2. **La DSN a été générée à partir de la simulation** (« Version paie source : SIMUL_2026-09_v2 du 28/09/2026 », brut déclaré 11 173,11 € au lieu de 11 465,90 €). C'est l'anomalie à détecter. Elle est corrigeable sans pénalité tant que l'échéance du 15/10 n'est pas passée, par une **DSN « annule et remplace »**.
3. **Heures supplémentaires** : la réduction salariale (11,31 %) neutralise ici exactement les cotisations vieillesse salariales sur les HS ; l'exonération d'IR sort les HS (nettes de CSG déductible) du net imposable ; la déduction forfaitaire patronale de 1,50 €/h s'applique (moins de 20 salariés).
4. **Marc Dupain est gérant majoritaire (60 %)** : il est **TNS**, il n'a pas de contrat de travail, pas de bulletin, n'apparaît pas en DSN. Sa rémunération, fixée par l'AG, est une charge (compte 644) mais elle ne passe **ni** par le journal de paie, **ni** par le 421. Ses cotisations sociales (SSI) sont appelées séparément par l'URSSAF et comptabilisées en 646.
5. **Comptes de tiers** : acompte de Sonia (425, déjà versé le 15/09, à « récupérer » dans la paie), opposition sur le salaire d'Antoine (427, à reverser au commissaire de justice), PAS (4421, prélevé par la DGFiP le mois suivant).

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 Bulletin de Kévin Morel

| Élément | Calcul | Montant |
|---|---|---|
| Salaire de base | 151,67 h × 13,5162 | 2 050,00 € |
| HS 25 % | 17,33 h × (13,5162 × 1,25 = 16,8952) | 292,79 € |
| **Brut** | | **2 342,79 €** |
| Sécurité sociale vieillesse | 2 342,79 × 7,30 % | 171,02 € |
| AGIRC-ARRCO | 2 342,79 × 4,01 % | 93,95 € |
| Mutuelle (part salariale) | forfait | 25,00 € |
| Réduction salariale HS | 292,79 × 11,31 % | − 33,11 € |
| Assiette CSG/CRDS | 2 342,79 × 98,25 % + 35,00 (part patronale mutuelle) | 2 336,79 € |
| CSG déductible | 2 336,79 × 6,80 % | 158,90 € |
| CSG non déductible + CRDS | 2 336,79 × 2,90 % | 67,77 € |
| **Total cotisations salariales** | 171,02 + 93,95 + 25,00 − 33,11 + 158,90 + 67,77 | **483,53 €** |
| **Net à payer avant IR** | 2 342,79 − 483,53 | **1 859,26 €** |

**Net imposable** :
- brut − cotisations déductibles : 2 342,79 − (171,02 + 93,95 + 25,00 − 33,11 + 158,90) = 2 342,79 − 415,76 = 1 927,03 €
- \+ part patronale de complémentaire santé : + 35,00 € → 1 962,03 €
- − HS exonérées d'IR (HS brutes − CSG déductible afférente) : 292,79 − (292,79 × 98,25 % × 6,80 % = 19,56) = 273,23 €
- **= 1 688,80 €**

**PAS** : 1 688,80 × 2,10 % = **35,46 €**. **Net payé** : 1 859,26 − 35,46 = **1 823,80 €** ✔ (conforme au bulletin).

**Pourquoi le net imposable est-il inchangé avec ou sans HS ?** Sans les HS, le brut aurait été de 2 050,00 € et le net imposable de 1 688,80 € (la DSN, établie sans HS, donne d'ailleurs le même PAS total de 166,03 €). Variation du net imposable due aux HS :
- \+ 292,79 € de brut ;
- − 0,00 € de cotisations vieillesse nettes (21,37 + 11,74 de cotisations, exactement compensées par la réduction salariale de 33,11 €) ;
- − 19,56 € de CSG déductible afférente aux HS ;
- − 273,23 € de HS exonérées d'IR (292,79 − 19,56) ;
- **= 0,00 €.**

Conséquence pratique : **pas de PAS sur les HS** (dans la limite annuelle exonérée, 7 500 € — *à vérifier*). La CSG non déductible et la CRDS restent dues sur les HS (8,35 €) mais n'augmentent pas l'assiette fiscale.

**Coût employeur de Kévin** : patronal 867,44 + 140,80 + 35,00 − 483,18 (réduction générale) − 26,00 (17,33 h × 1,50 €) = 534,06 € ; coût total 2 342,79 + 534,06 = **2 876,85 €**.

### 2.2 Montants de l'écriture de paie

| Élément | Calcul | Montant |
|---|---|---|
| Brut (6411) | total journal | 11 465,90 € |
| Formation professionnelle (6333) | donné (≈ 11 465,90 × 0,55 %) | 63,06 € |
| Taxe d'apprentissage (6312) | donné (≈ 11 465,90 × 0,59 %) | 67,65 € |
| URSSAF patronal hors formation/TA (6451) | 1 186,05 − 63,06 − 67,65 | 1 055,34 € |
| Retraite patronale nette (6453) | total journal | 149,66 € |
| Mutuelle patronale (6452) | 6 × 35,00 | 210,00 € |
| **431 URSSAF** | salariales 1 917,01 + patronales 1 186,05 | **3 103,06 €** |
| **4371 AGIRC-ARRCO** | salariales 459,79 + patronales 149,66 | **609,45 €** |
| **4372 Mutuelle** | 6 × 60,00 (= 150,00 salarial + 210,00 patronal) | **360,00 €** |
| 4421 PAS | | 166,03 € |
| 425 Acompte Sonia | | 300,00 € |
| 427 Opposition Antoine | | 120,00 € |
| 421 Net payé | | 8 353,07 € |

Contrôle : 2 526,80 (cotisations salariales) = 1 917,01 + 459,79 + 150,00 ✔ ; 11 465,90 − 2 526,80 = 8 939,10 = 166,03 + 300,00 + 120,00 + 8 353,07 ✔.

### 2.3 Rapprochement journal de paie / DSN

| Organisme | Journal définitif | DSN déposée le 05/10 | Écart |
|---|---|---|---|
| Brut déclaré | 11 465,90 | 11 173,11 | **292,79** (= HS de Kévin) |
| URSSAF | 3 103,06 | 2 901,00 | **202,06** |
| AGIRC-ARRCO | 609,45 | 561,71 | **47,74** |
| Mutuelle | 360,00 | 360,00 | 0,00 |
| PAS | 166,03 | 166,03 | 0,00 |

Explication de l'écart URSSAF (202,06 €) — tout provient de Kévin :
- salariales : vieillesse 21,37 (171,02 − 149,65) + CSG déd. 19,56 (158,90 − 139,34) + CSG/CRDS 8,35 (67,77 − 59,42) − réduction HS 33,11 = **16,17 €** ;
- patronales : cotisations brutes + 108,41 (867,44 − 759,03), réduction générale **moins forte** + 103,48 (513,70 − 410,22 : le brut plus élevé fait baisser le coefficient), déduction forfaitaire HS − 26,00 = **185,89 €** ;
- total 16,17 + 185,89 = **202,06 €** ✔.

Écart AGIRC-ARRCO (47,74 €) : salariales 11,74 (93,95 − 82,21) + patronales 36,00 (140,80 − 123,21 = 17,59 de cotisations, + 18,41 de réduction générale imputée en moins : 91,37 − 72,96) ✔.

## 3. Écritures comptables

**Écriture de paie de septembre**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD-PAIE | 6411 | Salaires, appointements | Paie 09/2026 – brut | 11 465,90 | |
| 30/09/2026 | OD-PAIE | 6451 | Cotisations à l'URSSAF | Paie 09/2026 – patronal URSSAF net | 1 055,34 | |
| 30/09/2026 | OD-PAIE | 6333 | Participation des employeurs à la formation professionnelle continue | Paie 09/2026 – CFP 0,55 % | 63,06 | |
| 30/09/2026 | OD-PAIE | 6312 | Taxe d'apprentissage | Paie 09/2026 – TA part principale | 67,65 | |
| 30/09/2026 | OD-PAIE | 6453 | Cotisations aux caisses de retraite | Paie 09/2026 – AGIRC-ARRCO patronal net | 149,66 | |
| 30/09/2026 | OD-PAIE | 6452 | Cotisations aux mutuelles | Paie 09/2026 – mutuelle patronale | 210,00 | |
| 30/09/2026 | OD-PAIE | 431 | Sécurité sociale (URSSAF) | Paie 09/2026 – URSSAF sal. + pat. | | 3 103,06 |
| 30/09/2026 | OD-PAIE | 4371 | AGIRC-ARRCO | Paie 09/2026 – retraite sal. + pat. | | 609,45 |
| 30/09/2026 | OD-PAIE | 4372 | Mutuelle Rhône Santé | Paie 09/2026 – mutuelle | | 360,00 |
| 30/09/2026 | OD-PAIE | 4421 | État – prélèvement à la source (IR) | Paie 09/2026 – PAS | | 166,03 |
| 30/09/2026 | OD-PAIE | 425 | Personnel – avances et acomptes | Paie 09/2026 – acompte Mercier | | 300,00 |
| 30/09/2026 | OD-PAIE | 427 | Personnel – oppositions | Paie 09/2026 – saisie Riva | | 120,00 |
| 30/09/2026 | OD-PAIE | 421 | Personnel – rémunérations dues | Paie 09/2026 – net à payer | | 8 353,07 |
| | | | | **Totaux** | **13 011,61** | **13 011,61** |

**Acompte (rappel) et règlements**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/09/2026 | BQ | 425 | Personnel – avances et acomptes | Acompte S. Mercier | 300,00 | |
| 15/09/2026 | BQ | 512100 | Banque Crédit Lyonnais Rhône | Acompte S. Mercier | | 300,00 |
| 15/09/2026 | BQ | 431 | Sécurité sociale (URSSAF) | Prélèvement DSN 08/2026 | 2 875,40 | |
| 15/09/2026 | BQ | 512100 | Banque Crédit Lyonnais Rhône | Prélèvement DSN 08/2026 | | 2 875,40 |
| 30/09/2026 | BQ | 421 | Personnel – rémunérations dues | Virement salaires 09/2026 | 8 353,07 | |
| 30/09/2026 | BQ | 512100 | Banque Crédit Lyonnais Rhône | Virement salaires 09/2026 | | 8 353,07 |
| | | | | **Totaux** | **11 528,47** | **11 528,47** |

**Rémunération du gérant (hors paie)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | BQ | 644 | Rémunération du travail de l'exploitant | Rémunération gérant 09/2026 (AG 12/06/2026) | 2 200,00 | |
| 30/09/2026 | BQ | 512100 | Banque Crédit Lyonnais Rhône | Virement M. Dupain | | 2 200,00 |
| | | | | **Totaux** | **2 200,00** | **2 200,00** |

Le 15/10, le paiement des cotisations soldera 431 (3 103,06 € **si la DSN est corrigée**), 4371 et 4372 ; le 427 sera soldé par le virement au commissaire de justice ; le 4421 par le prélèvement de la DGFiP.

## 4. Points d'attention / pièges

- **Ne pas comptabiliser à partir de la DSN** : elle reflète ici une paie obsolète. Le juge de paix, c'est le **net viré** (8 353,07 €), qui authentifie la version définitive.
- **DSN à corriger avant le 15/10/2026** : déposer une **DSN « annule et remplace »** de la période 09/2026 avec la paie définitive (dépôt possible jusqu'à l'échéance — *heure limite à vérifier sur net-entreprises*). À défaut, l'URSSAF prélèverait 2 901,00 € au lieu de 3 103,06 € et l'AGIRC-ARRCO 561,71 € au lieu de 609,45 € ; il faudrait régulariser en DSN d'octobre, avec un risque de **majorations de retard** sur l'insuffisance de versement et une **pénalité pour erreur déclarative**. Le compte 431 ferait apparaître un reliquat de 202,06 € qu'il ne faudrait surtout pas « solder » par une OD.
- La **réduction générale baisse quand le brut augmente** : l'écart patronal (185,89 €) est bien supérieur à 37 % des HS. Un junior qui recalcule « 292,79 × taux patronal » trouve un faux écart.
- **Acompte** : le 425 est débité le 15/09 (versement) et crédité dans la paie. Si le 425 n'est pas soldé à la clôture, c'est qu'un acompte n'a pas été repris en paie.
- **Opposition (427)** : depuis la réforme de la saisie des rémunérations (2025), la procédure est conduite par un **commissaire de justice** et l'employeur lui reverse les sommes retenues (*modalités à vérifier*) ; l'employeur qui ne retient pas devient débiteur à la place du salarié.
- **Marc n'est pas salarié** : intégrer sa rémunération dans le 421 / la DSN serait une **erreur grave** (déclaration d'un TNS au régime général, cotisations indues, incohérence avec la SSI). Sa rémunération est en **644**, conforme à la décision d'AG (montant net de 2 200 € ; les cotisations SSI prises en charge par la société s'ajoutent en 646 lors des appels de l'URSSAF). Sans décision d'AG, le virement aurait été un **prélèvement en compte courant** (débit 455).
- **Julie Dupain est associée (40 %) et salariée** : contrôler que le contrat de travail est réel (fonctions distinctes, subordination au gérant) — sinon risque de requalification.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- **Action immédiate** : prévenir Hélène et déposer (ou faire déposer par le service paie) la DSN annule et remplace avant le 15/10 ; vérifier les montants SEPA générés.
- **Procédure** : demander au service paie de **verrouiller** la génération de la DSN sur la paie « clôturée » et de ne jamais la produire depuis une simulation ; ajouter un contrôle automatique « brut DSN = brut journal définitif ».
- **Contrôle mensuel** dans le dossier de travail : tableau à 4 colonnes (journal / DSN / banque / compta) par organisme.
- **Mail type à Marc** :

> Bonjour Marc,
> La paie de septembre est comptabilisée. Votre virement de 2 200 € ne peut pas être intégré à la paie des salariés : en tant que gérant majoritaire, vous êtes travailleur non salarié. Votre rémunération est bien enregistrée en charge de la société, conformément à la décision d'assemblée de juin, mais elle ne figure ni sur les bulletins ni dans la DSN ; vos cotisations sont réglées directement à l'URSSAF (régime des indépendants).
> Par ailleurs, les 4 h supplémentaires hebdomadaires de Kévin ajoutées le 30/09 n'avaient pas été reprises dans la déclaration sociale : nous la corrigeons avant le 15 octobre, aucune pénalité ne sera due.
> Pour l'avenir, merci de nous signaler les heures supplémentaires au plus tard le 25 du mois.
> Bien cordialement,

## 6. Références

- PCG (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06) : comptes 421, 425, 427, 431, 437, 4421, 6411, 644, 645x, 6312, 6333.
- Code de la sécurité sociale : réduction générale des cotisations patronales (article L. 241-13) ; réduction de cotisations salariales sur heures supplémentaires (article L. 241-17) ; déduction forfaitaire patronale (article L. 241-18) — *paramètres à vérifier chaque année*.
- CGI, article 81 quater (exonération d'IR des heures supplémentaires, plafond annuel) ; articles 204 A et suivants (prélèvement à la source).
- Code du travail : heures supplémentaires et majorations (articles L. 3121-28 et suivants) ; saisie des rémunérations (articles L. 3252-1 et suivants) ; acomptes (article L. 3242-1).
- Code de la sécurité sociale, article L. 133-5-3 (DSN) ; cahier technique DSN (annule et remplace, régularisations).
- Statut social du gérant majoritaire : article L. 311-3 du CSS (a contrario) et article 62 du CGI.
