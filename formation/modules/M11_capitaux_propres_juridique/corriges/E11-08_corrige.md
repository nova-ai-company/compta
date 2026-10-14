# Corrigé E11-08 — Delta Invest : l'acompte sur dividendes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-08](../exercices/E11-08_acompte-dividendes-delta-invest.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Pourquoi un acompte est encadré** : distribuer avant l'approbation des comptes, c'est distribuer un bénéfice qui n'est pas encore définitivement constaté. La loi (art. L. 232-12 C. com.) exige donc :
1. un **bilan établi au cours ou à la fin de l'exercice**, **certifié par un commissaire aux comptes** ;
2. qu'il fasse apparaître un **bénéfice**, calculé **après amortissements et provisions**, **déduction faite des pertes antérieures et des sommes à porter en réserve** (légale et **statutaire**), **augmenté du report bénéficiaire** ;
3. un acompte **au plus égal** à ce bénéfice ;
4. une décision de l'organe compétent, **postérieure à la certification**.

**Vérification (question 1)**

| Condition | Constat | OK ? |
|---|---|---|
| Bilan intermédiaire au 30/06/2026 | Établi | ✓ |
| Certifié par le CAC | Attestation du 28/09/2026 | ✓ |
| Décision postérieure à la certification | Décision prévue le 15/10/2026 | ✓ |
| Organe compétent | Président (art. 25 des statuts) | ✓ |
| Montant ≤ bénéfice tel que défini par la loi | 460 000 € > plafond (voir calcul) | ✗ |

**Erreurs du projet de Lucie (question 2)** :
1. Elle part du **résultat avant impôt** (438 000 €) : le bénéfice s'entend **net**, après l'IS estimé (412 000 €).
2. Elle oublie la **réserve statutaire** de 10 % prévue par l'article 24 (qui doit être déduite comme les réserves légales).
3. La **réserve légale** est déjà au dixième du capital (80 000 € = 10 % × 800 000 €) : aucune dotation — ce point est correct par omission, mais doit être écrit dans la décision.
4. Elle n'indique pas que les **retenues fiscales** s'appliquent dès le paiement.

## 2. Calculs (détaillés, chaque montant justifié)

**Plafond de l'acompte**

| Élément | Calcul | Montant |
|---|---|---|
| Résultat net de la période (après IS estimé) | | 412 000,00 |
| – Pertes antérieures | aucune | 0,00 |
| – Réserve légale | déjà à 10 % du capital | 0,00 |
| – Réserve statutaire (10 %) | 412 000 × 10 % | – 41 200,00 |
| + Report à nouveau bénéficiaire | | + 35 000,00 |
| **= Montant maximum de l'acompte** | | **405 800,00** |

Le projet (460 000 €) dépasse le plafond de **54 200 €** : l'excédent serait un **dividende fictif** (répétition possible auprès des actionnaires, art. L. 232-17 ; responsabilité pénale du président). Les « autres réserves » (1 250 000 €) **ne peuvent pas** servir à un acompte : leur distribution suppose une décision de l'**assemblée**.

**Montant proposé** : 405 800 / 8 000 = 50,725 € par action → arrondi **50,00 € par action = 400 000 €**.

**Retenues par actionnaire (acompte de 400 000 €)**

| Actionnaire | Brut | PFNL 12,8 % | Prélèvements sociaux 18,6 % | Net versé |
|---|---|---|---|---|
| Jean Delmas (5 600 actions) | 280 000,00 | 35 840,00 | 52 080,00 | 192 080,00 |
| Catherine Delmas (1 600) | 80 000,00 | 10 240,00 | 14 880,00 | 54 880,00 |
| Hugo Delmas (800) — dispensé de PFNL | 40 000,00 | 0,00 | 7 440,00 | 32 560,00 |
| **Total** | **400 000,00** | **46 080,00** | **74 400,00** | **279 520,00** |

Contrôle : 400 000 – 46 080 – 74 400 = 279 520 ✓. La dispense d'Hugo (attestation du 20/11/2025, avant le 30/11/2025) vaut pour les revenus versés en **2026** ✓ ; elle ne couvre pas les prélèvements sociaux.

Jean Delmas étant **président de SAS** (assimilé salarié), la règle des 10 % des gérants majoritaires de SARL ne s'applique pas : ses dividendes supportent PFNL et prélèvements sociaux sur la totalité.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | OD | 4578 | Associés – acomptes sur dividendes (subdivision interne) | Acompte s/dividende 2026 – 50 €/action – décision du Président | 400 000,00 | |
| 15/10/2026 | OD | 457 | Associés – dividendes à payer | Acompte s/dividende 2026 (J. 280 000 / C. 80 000 / H. 40 000) | | 400 000,00 |
| 30/10/2026 | BQ | 457 | Associés – dividendes à payer | Paiement acompte s/dividende | 400 000,00 | |
| 30/10/2026 | BQ | 4422 | Prélèvements forfaitaires non libératoires | PFNL 12,8 % (J. et C. Delmas ; H. Delmas dispensé) | | 46 080,00 |
| 30/10/2026 | BQ | 4423 | Retenues et prélèvements sur distributions | Prélèvements sociaux 18,6 % | | 74 400,00 |
| 30/10/2026 | BQ | 512 | Banque | Vir. acompte net (192 080 / 54 880 / 32 560) | | 279 520,00 |
| 16/11/2026 | BQ | 4422 | Prélèvements forfaitaires non libératoires | 2777 – octobre 2026 | 46 080,00 | |
| 16/11/2026 | BQ | 4423 | Retenues et prélèvements sur distributions | 2777 – octobre 2026 | 74 400,00 | |
| 16/11/2026 | BQ | 512 | Banque | Télérèglement 2777 – octobre 2026 | | 120 480,00 |
| | | | | **Totaux (exercice 2026)** | **920 480,00** | **920 480,00** |

**À l'AGO 2027 (approbation des comptes 2026) — hypothèse : dividende total voté = 400 000 €**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| AGO 2027 | OD | 120 | Résultat de l'exercice | Affectation résultat 2026 – dividende total (dont acompte 400 000) | 400 000,00 | |
| AGO 2027 | OD | 457 | Associés – dividendes à payer | Dividende 2026 voté | | 400 000,00 |
| AGO 2027 | OD | 457 | Associés – dividendes à payer | Imputation de l'acompte versé le 30/10/2026 | 400 000,00 | |
| AGO 2027 | OD | 4578 | Associés – acomptes sur dividendes | Imputation de l'acompte | | 400 000,00 |
| | | | | **Totaux** | **800 000,00** | **800 000,00** |

(Les autres lignes de l'affectation — réserve statutaire, autres réserves, report à nouveau — sont passées dans la même écriture selon la résolution votée. Si le dividende total voté excède l'acompte, seul le **complément** donne lieu à paiement et à une nouvelle 2777.)

**Bilan au 31/12/2026** : le compte 4578 (400 000 € débiteur) est présenté en **autres créances** à l'actif (présentation usuelle en comptes individuels), le résultat 2026 restant intégralement en capitaux propres « avant répartition » ; l'**annexe** mentionne l'acompte versé et sa date. Certains cabinets présentent l'acompte en déduction des capitaux propres pour l'information financière : quelle que soit la présentation retenue, elle doit être expliquée en annexe et constante.

## 4. Points d'attention / pièges

- **Résultat net** (après IS estimé), **pas avant impôt**.
- **Réserves statutaires** : à déduire comme la réserve légale — lisez les statuts.
- **Les réserves antérieures ne financent pas un acompte** : seule l'assemblée peut les distribuer.
- **Ordre chronologique** : certification **avant** décision ; une décision antérieure à l'attestation du CAC rendrait l'acompte irrégulier.
- **Retenues dès le paiement** : PFNL, prélèvements sociaux et **2777 dans le mois suivant**, comme pour un dividende ordinaire ; l'acompte figure sur l'**IFU 2026**.
- **2777** : échéance légale le 15 du mois suivant le paiement, soit le **15/11/2026, qui est un dimanche** → en pratique, report au **premier jour ouvré suivant (lundi 16/11/2026)** — *règle de report à vérifier pour la télédéclaration ; par prudence, télédéclarer et télépayer le vendredi 13/11/2026*.
- **Hauts revenus** : pour Jean et Catherine Delmas, la contribution exceptionnelle sur les hauts revenus et la contribution différentielle instituée par la loi de finances pour 2025 peuvent trouver à s'appliquer — *à vérifier avec leur conseil patrimonial* ; un acompte complémentaire de contribution peut être exigé.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — Effet du second semestre et de l'abandon de créance**
- L'acompte est apprécié au vu de la situation **certifiée au 30/06/2026** : s'il est régulier à sa date, il ne devient pas fictif du seul fait d'une dégradation ultérieure.
- Mais à l'AGO 2027, le dividende de l'exercice devra être couvert par le **bénéfice distribuable de l'exercice entier**. L'abandon de créance de décembre (charge financière de 130 000 €, non déductible) et un éventuel second semestre moins favorable réduiront le résultat 2026. Si le bénéfice distribuable 2026 devenait inférieur à 400 000 €, l'AGO devrait **prélever expressément le complément sur les réserves distribuables** (Delta dispose de 1 250 000 € d'autres réserves) pour « couvrir » l'acompte ; à défaut, se poserait la question de la restitution par les actionnaires.
- **Simulation à faire en décembre** : résultat S1 412 000 – abandon 130 000 + résultat S2 estimé → bénéfice 2026 ; dotation statutaire de 10 % sur le bénéfice **annuel** ; comparer au 400 000 €.

**Mail à Lucie (extrait)**

> Bonjour Lucie,
> Le projet doit être corrigé avant signature : (1) le plafond se calcule sur le résultat **après impôt** (412 000 €) ; (2) les statuts imposent une **réserve statutaire de 10 %** (41 200 €) ; (3) avec le report à nouveau (35 000 €), l'acompte maximum est de **405 800 €**. Nous proposons **50 € par action, soit 400 000 €**. Nous vous adressons une décision corrigée.
> Ensuite : paiement le 30/10 des montants **nets** (Jean 192 080 €, Catherine 54 880 €, Hugo 32 560 €) ; nous déclarerons et paierons **120 480 €** de prélèvements sur la 2777 au plus tard le 13/11 (l'échéance du 15 tombe un dimanche). L'acompte figurera sur l'IFU 2026.

**Décision corrigée (dispositif)**

> Le Président, vu l'article L. 232-12 du Code de commerce et l'article 25 des statuts, vu la situation intermédiaire au 30 juin 2026 certifiée par le commissaire aux comptes le 28 septembre 2026, constate que le bénéfice net de la période s'élève à 412 000 € ; qu'après dotation de la réserve statutaire de 10 % (41 200 €), aucune dotation à la réserve légale n'étant requise (celle-ci atteignant le dixième du capital), et compte tenu du report à nouveau bénéficiaire de 35 000 €, le bénéfice susceptible de faire l'objet d'un acompte s'élève à 405 800 € ; décide de verser un acompte sur dividende de l'exercice 2026 de 400 000 €, soit 50 € par action, mis en paiement le 30 octobre 2026.

**Documentation** : attestation du CAC, situation intermédiaire, décision signée, calcul du plafond, attestation de dispense d'Hugo (valable pour 2026 — rappeler qu'il doit la renouveler avant le 30/11/2026 pour 2027), accusé de dépôt de la 2777.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. **L. 232-12** (acomptes sur dividendes), art. L. 232-10 et L. 232-11 (réserves et bénéfice distribuable), art. L. 232-17 (répétition des dividendes), art. L. 242-6 (dividendes fictifs, SA, applicable aux dirigeants de SAS — *éléments constitutifs à vérifier*).
- CGI : art. 117 quater (PFNL et dispense), art. 200 A (PFU), art. 223 sexies (contribution exceptionnelle sur les hauts revenus), dispositions de la loi de finances pour 2025 relatives à la contribution différentielle sur les hauts revenus (*à vérifier*), art. 242 ter (IFU).
- PCG : comptes 457, 442 ; information en annexe sur les acomptes sur dividendes.
- BOFiP : RPPM – Revenus de capitaux mobiliers – modalités du prélèvement forfaitaire non libératoire et des prélèvements sociaux.
