# Corrigé E07-02 — Bulletin d'un serveur : heures supplémentaires HCR, avantage nourriture et pourboires

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-02](../exercices/E07-02_bulletin-serveur-petit-zinc.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **Majoration des HS** : la convention HCR prévoit une majoration de **10 %** pour les heures de la 36e à la 39e (plus favorable au salarié dans les autres tranches selon la convention ; le Code du travail permet à un accord de branche de fixer un taux d'au moins 10 %). L'outil a appliqué le taux légal supplétif de 25 % : erreur en faveur du salarié, mais qui fausse le coût et les déclarations.
2. **Avantage en nature nourriture** : en HCR, le repas fourni est évalué à **1 minimum garanti** par repas. L'AN **s'ajoute au brut** (il est soumis à cotisations et à l'impôt) puis **se retranche du net** (Mehdi l'a déjà « perçu » en nature). L'outil l'a ajouté sans le retirer : le salarié est payé deux fois.
3. **Pourboires** : remis volontairement par les clients (y compris par CB) et reversés au personnel en contact avec la clientèle, ils sont **exonérés de cotisations, de CSG/CRDS et d'IR** si la rémunération du salarié n'excède pas **1,6 SMIC** (dispositif temporaire — *date d'échéance à vérifier*). Ils ne font donc **pas partie du brut** : ils figurent en bas du bulletin, ajoutés au net payé. L'outil les a mis dans le brut (cotisations indues).
4. **Comptabilité** : les pourboires encaissés par CB appartiennent aux salariés. Ce ne sont **ni du chiffre d'affaires, ni une opération soumise à TVA** : c'est une **dette** envers le personnel jusqu'à leur reversement.

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 Erreurs du bulletin brouillon

| Erreur | Brouillon | Correct |
|---|---|---|
| Majoration HS | 25 % → 17,33 × 15,50 = 268,62 € | 10 % → 17,33 × 13,64 = 236,38 € |
| Pourboires | dans le brut (cotisés, imposés) | hors brut, exonérés, ajoutés au net payé |
| AN nourriture | ajouté au brut mais **pas retranché** du net | ajouté au brut **et** retranché du net |
| Réduction HS / exonération IR | non visibles | à faire apparaître (obligation de lisibilité) |

### 2.2 Bulletin correct

| Rubrique | Base | Taux | Salarié | Patronal |
|---|---|---|---|---|
| Salaire de base | 151,67 h | 12,40 | 1 880,71 | |
| HS 10 % (36e–39e h) | 17,33 h | 13,64 | 236,38 | |
| Avantage en nature nourriture | 22 repas | 4,25 | 93,50 | |
| **Salaire brut** | | | **2 210,59** | |
| Sécurité sociale vieillesse | 2 210,59 | 7,30 % | 161,37 | |
| Cotisations patronales URSSAF | 2 210,59 | 36,80 % | | 813,50 |
| AGIRC-ARRCO T1 + CEG | 2 210,59 | 4,01 % / 6,01 % | 88,64 | 132,86 |
| Complémentaire santé HCR | | | 15,00 | 15,00 |
| Réduction salariale HS | 236,38 | − 11,31 % | − 26,73 | |
| Réduction générale | | | | − 534,22 |
| Déduction forfaitaire HS | 17,33 h | 1,50 € | | − 26,00 |
| CSG déductible | 2 186,90 | 6,80 % | 148,71 | |
| CSG non déductible + CRDS | 2 186,90 | 2,90 % | 63,42 | |
| **Total cotisations** | | | **450,41** | **401,14** |
| Déduction avantage en nature | | | − 93,50 | |
| **Net à payer avant IR** | | | **1 666,68** | |
| PAS | 1 618,01 | 1,6 % | − 25,89 | |
| Pourboires (exonérés) | | | + 210,00 | |
| **Net payé** | | | **1 850,79** | |

Détail des calculs :
- assiette CSG/CRDS : 2 210,59 × 98,25 % = 2 171,90 + 15,00 (part patronale santé) = **2 186,90 €** ;
- cotisations salariales : 161,37 + 88,64 + 15,00 − 26,73 + 148,71 + 63,42 = **450,41 €** ;
- net avant IR : 2 210,59 − 450,41 − 93,50 = **1 666,68 €** ;
- net imposable : 2 210,59 − (161,37 + 88,64 + 15,00 − 26,73 + 148,71 = 386,99) + 15,00 − HS exonérées (236,38 − CSG déductible sur HS 236,38 × 98,25 % × 6,80 % = 15,79 → 220,59) = **1 618,01 €** ;
- PAS : 1 618,01 × 1,6 % = **25,89 €** ;
- patronal : 813,50 + 132,86 + 15,00 − 534,22 − 26,00 = **401,14 €** ; ventilation : URSSAF 813,50 − 453,55 − 26,00 = **333,95 €** ; retraite 132,86 − 80,67 = **52,19 €** ; santé 15,00 € ;
- **coût employeur** : 2 210,59 + 401,14 = **2 611,73 €** (hors pourboires, qui ne sont pas une charge de l'entreprise). Le brouillon annonçait 3 046,90 € : 435 € de trop par mois.

### 2.3 Conditions de l'exonération des pourboires
- Sommes remises **volontairement** par les clients (pas le « service compris » imposé, qui est du salaire soumis) ;
- remises directement au salarié ou centralisées par l'employeur (CB) puis **reversées intégralement** au personnel en contact avec la clientèle ;
- salarié dont la **rémunération** (hors pourboires) n'excède pas **1,6 SMIC** : 1,6 × 1 823,03 = 2 916,85 € ; Mehdi : 2 210,59 € (même en proratisant pour 169 h, on reste en dessous) ✔ ;
- dispositif applicable à la date du versement : **à vérifier impérativement** (prorogations successives).

### 2.4 Correction de la pièce 5
Le total TPE (48 620,00 €) inclut 1 240,00 € de pourboires. CA TTC réel : 47 380,00 € → HT 43 072,73 € ; TVA 4 307,27 €. Écart : HT 44 200,00 − 43 072,73 = **1 127,27 €** ; TVA 4 420,00 − 4 307,27 = **112,73 €** ; total 1 240,00 €.

## 3. Écritures comptables

**Correction de l'enregistrement des remises CB**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 706100 | Ventes de repas TVA 10 % | Extourne pourboires CB 09/2026 | 1 127,27 | |
| 30/09/2026 | OD | 445711 | TVA collectée 10 % | Extourne pourboires CB 09/2026 | 112,73 | |
| 30/09/2026 | OD | 467100 | Pourboires clients à reverser au personnel | Pourboires CB 09/2026 | | 1 240,00 |
| | | | | **Totaux** | **1 240,00** | **1 240,00** |

**Paie de Mehdi Bensaïd (septembre 2026)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD-PAIE | 6411 | Salaires, appointements | Base + HS 09/2026 | 2 117,09 | |
| 30/09/2026 | OD-PAIE | 6414 | Indemnités et avantages divers | AN nourriture 22 repas | 93,50 | |
| 30/09/2026 | OD-PAIE | 601 | Achats stockés – matières premières | Reclassement repas personnel en AN (*subdivision selon la nomenclature 2025 du PCG*) | | 93,50 |
| 30/09/2026 | OD-PAIE | 6451 | Cotisations à l'URSSAF | Patronal URSSAF net | 333,95 | |
| 30/09/2026 | OD-PAIE | 6453 | Cotisations aux caisses de retraite | Patronal AGIRC-ARRCO net | 52,19 | |
| 30/09/2026 | OD-PAIE | 6452 | Cotisations aux mutuelles | Santé HCR patronal | 15,00 | |
| 30/09/2026 | OD-PAIE | 431 | Sécurité sociale (URSSAF) | Sal. 346,77 + pat. 333,95 | | 680,72 |
| 30/09/2026 | OD-PAIE | 4371 | AGIRC-ARRCO | Sal. 88,64 + pat. 52,19 | | 140,83 |
| 30/09/2026 | OD-PAIE | 4372 | Organisme complémentaire santé HCR | Sal. 15,00 + pat. 15,00 | | 30,00 |
| 30/09/2026 | OD-PAIE | 4421 | État – prélèvement à la source | PAS 09/2026 | | 25,89 |
| 30/09/2026 | OD-PAIE | 467100 | Pourboires clients à reverser au personnel | Pourboires reversés à M. Bensaïd | 210,00 | |
| 30/09/2026 | OD-PAIE | 421 | Personnel – rémunérations dues | Net payé M. Bensaïd | | 1 850,79 |
| | | | | **Totaux** | **2 821,73** | **2 821,73** |

Contrôle URSSAF salarial : 161,37 + 148,71 + 63,42 − 26,73 = 346,77 €.

> Variante acceptée : ne pas faire transiter l'AN par 6414 / 601 et débiter 6411 du seul brut « monétaire » (2 117,09 €) — l'écriture reste équilibrée car l'AN est ajouté puis retranché. La variante présentée a l'avantage de faire coïncider le 641 avec le brut déclaré en DSN (contrôle URSSAF « salaires déclarés / salaires comptabilisés »). Le compte 791 n'est plus utilisable depuis 2025.

## 4. Points d'attention / pièges

- **Ne jamais mettre les pourboires en CA** : on gonfle le CA, on paie de la TVA indue (112,73 € ce mois-ci), on fausse les redevances indexées sur le CA et l'assiette de certaines taxes.
- Le compte 467100 doit être **soldé** chaque mois : son solde = pourboires encaissés non encore reversés. Un solde qui grossit = pourboires conservés par l'employeur (illicite).
- **Commissions CB** : la commission monétique sur la part pourboire est en principe supportée par l'employeur (les pourboires doivent être reversés intégralement) — *à apprécier selon la position administrative en vigueur*.
- **Seuil de 1,6 SMIC** : à apprécier salarié par salarié ; pour un salarié au-dessus, les pourboires sont soumis à cotisations et à l'IR.
- **AN nourriture et 1,6 SMIC** : l'AN fait partie de la rémunération pour apprécier le seuil.
- En HCR, si le salarié ne prend pas son repas alors qu'il est présent au moment du service, il a droit à une **indemnité compensatrice de nourriture** (soumise à cotisations).
- Les **extras** du week-end (CDD d'usage) suivent les mêmes règles AN / pourboires ; vérifier leurs DPAE et la contribution spécifique éventuelle sur les CDD d'usage.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- Vérifier les **9 bulletins** de septembre : si la même erreur de majoration (25 %) a été appliquée à tous, recalculer et régulariser via la DSN.
- Demander à Clara d'**arrêter l'outil en ligne** non paramétré HCR : la paie reste au cabinet (mission confiée).
- Mettre en place un **tableau mensuel des pourboires** (encaissés CB / espèces, clé de répartition, reversés) — pièce justificative en cas de contrôle URSSAF.
- Paramétrer l'outil d'OCR / l'import TPE pour isoler automatiquement la ligne « TIP ».
- **Réponse à Clara** :

> Bonjour Clara,
> Vous aviez raison, le net du brouillon était trop élevé : l'outil avait majoré les heures de 36 à 39 à 25 % au lieu de 10 % (convention HCR), oublié de déduire les repas pris sur place, et soumis les pourboires à cotisations. Le bon bulletin donne un net payé de 1 850,79 €, dont 210 € de pourboires exonérés.
> Les pourboires payés par carte ne sont pas votre chiffre d'affaires : ils appartiennent aux serveurs. Nous avons corrigé la comptabilité de septembre (112,73 € de TVA en moins à payer).
> Merci de continuer à nous transmettre le relevé mensuel du terminal avec la ligne « pourboires » et votre clé de répartition.
> Bien cordialement,

## 6. Références

- Convention collective nationale des hôtels, cafés, restaurants (IDCC 1979) : majorations des heures supplémentaires, avantage nourriture (1 MG par repas), indemnité compensatrice de nourriture.
- Code du travail, articles L. 3121-33 (taux de majoration fixé par accord, au moins 10 %) et L. 3244-1 et suivants (pourboires).
- Loi n° 2022-1158 du 16 août 2022 portant mesures d'urgence pour la protection du pouvoir d'achat (exonération des pourboires) et textes de prorogation ultérieurs — *échéance à vérifier*.
- Arrêté du 10 décembre 2002 relatif à l'évaluation des avantages en nature ; BOSS, rubrique « Avantages en nature ».
- CGI, article 81 quater (HS) ; Code de la sécurité sociale, articles L. 241-13, L. 241-17, L. 241-18.
- PCG : comptes 6411, 6414, 645x, 431, 437, 4421, 421, 467 ; suppression des comptes de transferts de charges (règlement ANC n° 2022-06).
