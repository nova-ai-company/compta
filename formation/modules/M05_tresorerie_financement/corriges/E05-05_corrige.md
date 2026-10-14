# Corrigé E05-05 — Le PGE de la Menuiserie : différé, remboursement et coût de la garantie

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-05](../exercices/E05-05_pge-menuiserie.md)

## 1. Analyse

### 1.1 La vie du PGE

| Période | Ce qui est payé | Garantie (barème PME du contrat) |
|---|---|---|
| 12/07/2021 → 12/07/2022 (année 1) | Rien (remboursement in fine prévu à 12 mois) | 0,25 % × 150 000 = **375,00 €** prélevés au versement |
| 12/08/2022 → 12/07/2023 (année 2, différé supplémentaire de l'avenant) | Intérêts 0,70 % + commission seuls | 0,50 % l'an |
| 12/08/2023 → 12/07/2024 (année 3) | 48 mensualités constantes commencent (n° 1 = 12/08/2023) | 0,50 % l'an |
| 12/08/2024 → 12/07/2027 (années 4 à 6) | Mensualités n° 13 à 48 | **1,00 % l'an** |

Durée totale : 6 ans (maximum autorisé pour un PGE). **En 2026, toute l'année est au barème de 1,00 %**, calculé mensuellement sur le capital restant dû avant l'échéance.

### 1.2 Traitement comptable
- Le PGE est un **emprunt bancaire** ordinaire (164), garanti par l'État : la garantie protège la **banque**, pas l'emprunteur. La société doit 100 % du capital.
- La **commission de garantie** est le prix de la garantie, refacturé par la banque : c'est une charge, comptabilisée en **627 Services bancaires et assimilés** (choix du cabinet, à appliquer de façon permanente ; certains cabinets l'intègrent en 661 lorsqu'elle est assimilée à un complément de taux).
- Erreur constatée : les commissions de janvier à septembre ont été saisies avec le capital en 164 → le 164 est **inférieur** au capital restant dû.

## 2. Calculs

### 2.1 Mensualité hors garantie
150 000 € sur 48 mois à 0,70 % / 12 = 0,05833 % par mois :
a = 150 000 × 0,0005833 / (1 – 1,0005833^–48) = **3 169,87 €** (dernière échéance ajustée à 3 169,63 €).

### 2.2 Tableau 2026 (échéances n° 30 à 41)

| N° | Date | Capital début | Intérêts 0,70 % | Capital remboursé | Échéance hors garantie | Commission de garantie 1 % | Total prélevé | Capital restant dû |
|---|---|---|---|---|---|---|---|---|
| 30 | 12/01/2026 | 59 877,40 | 34,93 | 3 134,94 | 3 169,87 | 49,90 | 3 219,77 | 56 742,46 |
| 31 | 12/02/2026 | 56 742,46 | 33,10 | 3 136,77 | 3 169,87 | 47,29 | 3 217,16 | 53 605,69 |
| 32 | 12/03/2026 | 53 605,69 | 31,27 | 3 138,60 | 3 169,87 | 44,67 | 3 214,54 | 50 467,09 |
| 33 | 12/04/2026 | 50 467,09 | 29,44 | 3 140,43 | 3 169,87 | 42,06 | 3 211,93 | 47 326,66 |
| 34 | 12/05/2026 | 47 326,66 | 27,61 | 3 142,26 | 3 169,87 | 39,44 | 3 209,31 | 44 184,40 |
| 35 | 12/06/2026 | 44 184,40 | 25,77 | 3 144,10 | 3 169,87 | 36,82 | 3 206,69 | 41 040,30 |
| 36 | 12/07/2026 | 41 040,30 | 23,94 | 3 145,93 | 3 169,87 | 34,20 | 3 204,07 | 37 894,37 |
| 37 | 12/08/2026 | 37 894,37 | 22,11 | 3 147,76 | 3 169,87 | 31,58 | 3 201,45 | 34 746,61 |
| 38 | 12/09/2026 | 34 746,61 | 20,27 | 3 149,60 | 3 169,87 | 28,96 | 3 198,83 | 31 597,01 |
| 39 | 12/10/2026 | 31 597,01 | 18,43 | 3 151,44 | 3 169,87 | 26,33 | 3 196,20 | 28 445,57 |
| 40 | 12/11/2026 | 28 445,57 | 16,59 | 3 153,28 | 3 169,87 | 23,70 | 3 193,57 | 25 292,29 |
| 41 | 12/12/2026 | 25 292,29 | 14,75 | 3 155,12 | 3 169,87 | 21,08 | 3 190,95 | **22 137,17** |
| | **Total 2026** | | **298,21** | **37 740,23** | | **426,03** | **38 464,47** | |

Exemple de calcul (n° 30) : intérêts = 59 877,40 × 0,70 % / 12 = 34,93 ; garantie = 59 877,40 × 1 % / 12 = 49,90.

Échéances restantes après le 31/12/2026 (n° 42 à 48, janvier → juillet 2027) : capital 22 137,17 €.

### 2.3 Contrôle du 164 au 30/09/2026

| | Montant |
|---|---|
| Capital restant dû après l'échéance n° 38 (tableau) | 31 597,01 |
| Solde du 164 (pièce 3) | 31 242,09 |
| **Écart** | **354,92** |
| Commissions de garantie n° 30 à 38 (49,90 + … + 28,96) | 354,92 ✔ |

Contrôle croisé : débit du 164 = 28 635,31 = capital remboursé n° 30 à 38 (59 877,40 – 31 597,01 = 28 280,39) + commissions 354,92 ✔. Intérêts n° 30 à 38 en 661 : 248,44 € ✔.

### 2.4 Courus au 31/12/2026 (12/12 → 31/12 = 19 jours, exact/360)
- Intérêts : 22 137,17 × 0,70 % × 19 / 360 = **8,18 €**
- Commission de garantie : 22 137,17 × 1,00 % × 19 / 360 = **11,68 €**

Montants non significatifs : la plupart des cabinets fixent un seuil en deçà duquel on ne les passe pas. On les comptabilise ici pour la démonstration (et parce que l'écriture est automatisable).

### 2.5 Coût du PGE en 2026

| Élément | Montant |
|---|---|
| Intérêts payés (n° 30 à 41) | 298,21 |
| Commissions de garantie payées | 426,03 |
| Courus de fin d'exercice (8,18 + 11,68), nets des courus d'ouverture* | ≈ 19,86 |
| **Coût 2026 (ordre de grandeur)** | **≈ 744 €** |

\* Les courus au 31/12/2025 (19 jours sur 59 877,40 €, soit environ 22 € intérêts + 32 € garantie) n'avaient pas été comptabilisés : ce n'est pas significatif ; on n'y revient pas, mais on le note pour la permanence (à compter de 2026, on les passe).

Rapporté au capital moyen de l'année (≈ 41 000 €), le coût global est d'environ **1,8 %** : la garantie (1 %) pèse davantage que les intérêts (0,70 %). Le PGE reste un financement bon marché — c'est un argument pour **ne pas** le mettre en défaut.

## 3. Écritures comptables

**Correction au 30/09/2026 :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 627 | Services bancaires et assimilés (commission de garantie PGE) | Reclassement commissions de garantie échéances 30 à 38 | 354,92 |  |
| 30/09/2026 | OD | 164100 | PGE Société Lyonnaise de Crédit | Reclassement commissions de garantie saisies en capital |  | 354,92 |
| | | | | **Totaux** | **354,92** | **354,92** |

**Échéance type (n° 39 du 12/10/2026) :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 12/10/2026 | BQ | 164100 | PGE Société Lyonnaise de Crédit | PGE échéance n° 39 — capital | 3 151,44 | |
| 12/10/2026 | BQ | 661 | Charges d'intérêts (6611) | PGE échéance n° 39 — intérêts | 18,43 | |
| 12/10/2026 | BQ | 627 | Services bancaires et assimilés | PGE échéance n° 39 — commission de garantie | 26,33 | |
| 12/10/2026 | BQ | 512 | Banque | PGE échéance n° 39 | | 3 196,20 |
| | | | | **Totaux** | **3 196,20** | **3 196,20** |

**Inventaire au 31/12/2026 (à extourner au 01/01/2027) :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 661 | Charges d'intérêts (6611) | PGE — intérêts courus 12/12-31/12 (19 j) | 8,18 |  |
| 31/12/2026 | OD | 1688 | Intérêts courus sur emprunts | PGE — intérêts courus 12/12-31/12 |  | 8,18 |
| 31/12/2026 | OD | 627 | Services bancaires et assimilés (commission de garantie PGE) | PGE — commission de garantie courue 12/12-31/12 (19 j) | 11,68 |  |
| 31/12/2026 | OD | 4686 | Divers — charges à payer | PGE — commission de garantie courue |  | 11,68 |
| | | | | **Totaux** | **19,86** | **19,86** |

### Présentation au bilan du 31/12/2026

| Dette | Montant | À 1 an au plus | De 1 à 5 ans | À plus de 5 ans |
|---|---|---|---|---|
| PGE — capital (164100) | 22 137,17 | 22 137,17 | 0,00 | 0,00 |
| Intérêts courus (1688) | 8,18 | 8,18 | — | — |

Tout le solde du PGE est **à moins d'un an** : à signaler dans le prévisionnel de trésorerie (7 mensualités d'environ 3 180 € jusqu'en juillet 2027).

## 4. Points d'attention / pièges

- **« L'État garantit, donc la banque ne risque rien »** : faux raisonnement. La garantie couvre **90 %** de la perte finale **de la banque**, après mise en jeu et recouvrement. Pour la Menuiserie, un impayé produit les mêmes effets qu'avec n'importe quel prêt : relances, **déchéance du terme** (exigibilité immédiate du solde), dégradation de la **cotation Banque de France**, risque de « défaut croisé » sur le prêt matériel et le découvert, puis recouvrement (Bpifrance, subrogée, peut poursuivre l'entreprise pour la part qu'elle a payée).
- **Commission de garantie** : à identifier sur chaque échéance ; ne jamais l'imputer en capital.
- **Barème de garantie** : celui du **contrat** fait foi (années 1 / 2-3 / 4-6). Le barème « usuel » cité dans le cours est à vérifier sur chaque contrat.
- **Continuité d'exploitation** : perte de 180 000 € sur un capital de 50 000 € → capitaux propres probablement inférieurs à la moitié du capital (art. L. 223-42 C. com.) ; l'annexe devra traiter la continuité d'exploitation, et le PGE s'inscrit dans ce diagnostic.

## 5. Ce qu'un senior ferait en plus

**Trame de l'appel à Antoine Girard :**
1. *Constat* : il reste 7 mensualités (≈ 22 300 € au total) après décembre, plus 3 en octobre-décembre (≈ 9 580 €). Le PGE coûte peu (≈ 1,8 % l'an) : c'est le dernier financement à mettre en défaut.
2. *Risques d'une suspension unilatérale* : exigibilité anticipée de tout le solde, inscription des incidents, défiance du Crédit Mutuel et de la banque du découvert, perte de crédibilité au moment où l'entreprise a besoin de ses banquiers.
3. *Alternatives, dans l'ordre* :
   - **demander à la banque**, *avant* le premier impayé, un report d'échéances ou un rééchelonnement (motif documenté : prévisionnel de trésorerie) ;
   - à défaut d'accord, saisir la **Médiation du crédit** (Banque de France), gratuite et confidentielle, qui peut obtenir un étalement des PGE selon le dispositif en vigueur (conditions à vérifier) ;
   - **mandat ad hoc ou conciliation** auprès du président du tribunal de commerce (tribunal des activités économiques dans les ressorts où il est expérimenté) (procédures amiables et confidentielles) si plusieurs créanciers sont concernés ;
   - **échéanciers URSSAF / SIE** pour décaler d'autres dettes ;
   - soutien de l'**actionnaire** Delta Invest : avance en compte courant (même modeste), report des management fees éventuels, ou abandon de créance — à discuter avec Jean Delmas.
4. *Prochaines étapes* : prévisionnel de trésorerie 12 mois (cours § 11) préparé par le cabinet sous 10 jours, rendez-vous banquier ensemble.

**Après l'appel**, un e-mail de synthèse (sans détailler les risques de manière alarmiste) pour tracer le conseil donné : le devoir de conseil du cabinet doit pouvoir être prouvé.

**Dossier** : classer le contrat, l'avenant et le tableau complet (demander les pages manquantes à la banque) au dossier permanent ; noter le barème de garantie applicable.

## 6. Références
- Loi n° 2020-289 du 23 mars 2020 de finances rectificative pour 2020, art. 6 (garantie de l'État sur les PGE) et arrêtés d'application (barème de la garantie) — dispositif à vérifier selon la date du prêt.
- PCG : comptes 164, 1688, 661, 627, 4686.
- Code de commerce, art. L. 611-3 et suivants (mandat ad hoc, conciliation), art. L. 223-42 (capitaux propres inférieurs à la moitié du capital).
- Médiation du crédit aux entreprises (Banque de France) — dispositif public de médiation.
