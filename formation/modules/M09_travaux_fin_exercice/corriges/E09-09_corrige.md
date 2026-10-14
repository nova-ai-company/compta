# Corrigé E09-09 — Menuiserie Bois & Création : les événements de janvier-mars 2027

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-09](../exercices/E09-09_evenements-posterieurs-menuiserie.md)

## 1. Analyse

**Principe.** Les événements survenus **entre la clôture (31/12/2026) et l'arrêté des comptes (20/03/2027)** se classent en deux catégories :
- **ajustants** : ils apportent une information sur une situation **qui existait à la clôture**. On **corrige** les comptes 2026 ;
- **non ajustants** : la situation est **née après la clôture**. On ne touche pas aux comptes, mais on **informe en annexe** si l'événement est significatif. Si l'événement remet en cause la **continuité d'exploitation**, il affecte la base même d'établissement des comptes.

Antoine a tout inversé : la liquidation (2027) **doit** toucher 2026, alors que l'incendie (2027) **ne doit pas** y figurer.

| Événement | Situation à la clôture ? | Classement | Traitement |
|---|---|---|---|
| 1 — Liquidation de Saône Concept | **Oui** : le client était en redressement judiciaire depuis juin 2026, ne payait plus depuis mars, et sa situation était déjà compromise. La liquidation **confirme** que la créance était irrécouvrable au 31/12 | **Ajustant** | Dépréciation portée à **100 % du HT** |
| 2 — Incendie du 22/01/2027 | **Non** : le sinistre est survenu après la clôture (l'extracteur existait, mais le sinistre n'existait pas) | **Non ajustant** | **Rien dans les comptes 2026**, information en annexe (significatif : 85 000 € de dommages, 3 semaines d'arrêt partiel) |
| 3 — Jugement prud'homal | **Oui** : licenciement du 14/09/2026, litige né en 2026 ; le jugement **précise le montant** | **Ajustant** | Provision portée à **18 500 €** (montant certain, sans appel) |
| 4 — Vente du lot de chêne | **Oui** : les marques d'humidité étaient **constatées à l'inventaire** ; la vente de janvier donne la **valeur nette de réalisation** au 31/12 | **Ajustant** | Dépréciation du stock |
| 5 — Projet d'augmentation de capital | **Non** : décision future, conditionnelle | **Non ajustant** | Information en annexe (soutien de l'associé), élément clé pour la continuité d'exploitation |

**Continuité d'exploitation.** Plusieurs indices s'accumulent : perte de 2026 après ajustements, capitaux propres négatifs, perte d'un client majeur, PGE à rembourser, incendie. Les comptes ne peuvent être établis en continuité que si la société démontre sa capacité à poursuivre son activité **au moins 12 mois** après la clôture : prévisionnel de trésorerie, **lettre de soutien de Delta Invest**, indemnité d'assurance attendue, échéancier des dettes. La continuité est retenue si ces éléments sont crédibles, avec une **mention de l'incertitude** en annexe. Dans le cas contraire, les comptes devraient être établis en valeurs liquidatives.

## 2. Calculs

**Créance Saône Concept :**

| Élément | Montant |
|---|---|
| Créance HT | 54 000,00 € |
| Dépréciation nécessaire : 100 % du HT | 54 000,00 € |
| Dépréciation déjà prévue au projet : 30 % | 16 200,00 € |
| **Complément** | **37 800,00 €** |

La TVA (10 800 €) n'est pas dépréciée : elle sera récupérée auprès du Trésor (voir point 4).

**Litige :** 18 500 – 8 000 = **10 500,00 €** de complément.

**Stock de chêne :** valeur nette de réalisation = 19 500 – 500 = 19 000 € ; coût 26 000 € → **dépréciation 7 000,00 €**.

**Résultat 2026 après ajustements :**

| Élément | Montant |
|---|---|
| Résultat provisoire | + 18 600,00 € |
| Complément de dépréciation Saône Concept | – 37 800,00 € |
| Complément de provision prud'homale | – 10 500,00 € |
| Dépréciation du stock de chêne | – 7 000,00 € |
| **Résultat 2026** | **– 36 700,00 €** |

**Capitaux propres au 31/12/2026 :**
22 400 (au 31/12/2025) – 36 700 (résultat 2026) – 800 (subvention virée au résultat) = **– 15 100,00 €**.

Ils sont négatifs, et donc bien inférieurs à la moitié du capital (25 000 €). L'AGE de 2026 ayant décidé de ne pas dissoudre, la société doit **reconstituer ses capitaux propres** à hauteur de la moitié du capital (ou réduire son capital) au plus tard à la clôture du deuxième exercice suivant celui au cours duquel les pertes ont été constatées. Les pertes de 2025 ayant été constatées lors de l'approbation des comptes en 2026, l'échéance est la **clôture 2028** (art. L. 223-42 C. com.). L'augmentation de capital envisagée par Delta (pièce 5) va dans ce sens.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Complément dépréciation Saône Concept (LJ 10/02/2027) | 37 800,00 | |
| 31/12/2026 | OD | 491 | Dépréciations des comptes de clients | Complément dépréciation Saône Concept | | 37 800,00 |
| 31/12/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Complément provision litige R. T. (jugement 02/02/2027) | 10 500,00 | |
| 31/12/2026 | OD | 1511 | Provisions pour litiges | Complément provision litige R. T. | | 10 500,00 |
| 31/12/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation lot de chêne (VNR 19 000) | 7 000,00 | |
| 31/12/2026 | OD | 391 | Dépréciations des matières premières | Dépréciation lot de chêne | | 7 000,00 |
| | | | | **Totaux** | **55 300,00** | **55 300,00** |

*Créance déjà reclassée en 416 dans le projet de comptes (depuis l'ouverture du redressement judiciaire). Si ce n'était pas le cas : D 416 / C 411 pour 64 800 €.*

**Pour mémoire, en 2027 :**
- paiement du jugement : D 1511 18 500 / C 7815 18 500, puis D 641/645 (ou 658 selon la nature des sommes) / C 512 ;
- incendie : sortie de la VNC de la cabine détruite et des stocks, indemnité d'assurance à constater lorsqu'elle sera acquise (voir E09-11), dans les comptes 2027 ;
- vente du chêne : reprise de la dépréciation de 7 000 €.

## 4. Points d'attention / pièges

- **« C'est arrivé en 2027 » n'est pas un critère.** Le seul critère est : la situation existait-elle au 31/12 ?
- **Ne jamais intégrer un sinistre postérieur** dans les comptes de l'exercice clos pour « montrer qu'on a souffert » : ce serait une **inexactitude** des comptes.
- **TVA sur la créance irrécouvrable** : la TVA collectée sur des factures impayées peut être récupérée lorsque la créance devient **définitivement irrécouvrable** (art. 272, 1 CGI). En cas de **liquidation judiciaire**, l'imputation est admise à partir du **jugement prononçant la liquidation**, sous réserve que la créance ait été déclarée. *Les conditions précises et les justificatifs (jugement, déclaration de créance, attestation du liquidateur) sont à vérifier au BOFiP avant de récupérer la TVA.* La récupération intervient en **2027** : imputation sur la CA3 suivant le jugement, et émission d'une **facture rectificative** (ou d'un avoir) adressée au liquidateur. Elle ne se fait pas au 31/12/2026, d'où une dépréciation limitée au HT.
- **Comptabilisation de la perte définitive en 2027** : D 654 *Pertes sur créances irrécouvrables* 54 000 + D 44571 10 800 / C 416 64 800, puis reprise de la dépréciation D 491 54 000 / C 7817 54 000.
- **Jugement sans appel** : le montant devient certain. On pourrait aussi reclasser la provision en charge à payer (dette). Les deux présentations ont le même effet sur le résultat.
- **Déductibilité fiscale** : la dépréciation de la créance, la provision prud'homale et la dépréciation du stock sont déductibles (pertes probables, individualisées et chiffrées). La Menuiserie étant dans le groupe d'**intégration fiscale** de Delta Invest, son déficit est imputé sur le résultat d'ensemble.

**Mentions en annexe (à rédiger) :**
1. **Événements postérieurs** : incendie du 22/01/2027 (dommages estimés à 85 000 €, couverts par l'assurance sous déduction d'une franchise de 5 000 €, arrêt partiel de 3 semaines) ; liquidation du client Saône Concept, prise en compte dans les comptes ; jugement prud'homal, pris en compte.
2. **Continuité d'exploitation** : capitaux propres négatifs, prévisionnel de trésorerie, soutien de l'associé majoritaire (lettre de soutien et projet d'augmentation de capital de 100 000 €), incertitude significative le cas échéant.
3. **Capitaux propres < ½ capital** : rappel de la décision de non-dissolution et de l'échéance de régularisation.

## 5. Ce qu'un senior ferait en plus

- **Exiger une lettre de soutien formelle de Delta Invest**, signée de Jean Delmas, couvrant au moins 12 mois après la clôture, et un **prévisionnel de trésorerie mensuel 2027** établi par Antoine et revu par le cabinet. Sans ces pièces, on ne signe pas une plaquette en continuité d'exploitation.
- **Lettre d'affirmation** du gérant listant tous les événements postérieurs connus à la date d'arrêté.
- **Coordination avec le dossier Delta Invest** (E09-10) : la perte et les capitaux propres négatifs de la Menuiserie pèsent sur la valeur d'utilité des titres chez la holding.
- **Prévention des difficultés** : rappeler à Antoine l'intérêt d'une **procédure de conciliation ou d'un mandat ad hoc** pour négocier avec la banque (PGE) et l'URSSAF, avant que la situation ne se dégrade.
- **Assurance** : suivre la déclaration de sinistre et l'expertise, et faire chiffrer la **perte d'exploitation** garantie.

**Réponse à Antoine (à envoyer aussi à Jean Delmas) :**
> « Antoine, la liquidation de Saône Concept, même prononcée en février 2027, confirme que la créance était perdue au 31/12/2026 : elle doit être dépréciée à 100 % du HT dans les comptes 2026. La TVA (10 800 €) sera récupérée en 2027. Le jugement prud'homal et la vente à perte du lot de chêne, qui étaient déjà en germe à fin 2026, sont également pris en compte. À l'inverse, l'incendie de janvier ne peut pas être inscrit dans les comptes 2026 : il sera décrit dans l'annexe et traité en 2027 avec l'indemnité d'assurance. Le résultat 2026 s'établit à – 36 700 € et les capitaux propres à – 15 100 €. Pour que nous puissions arrêter les comptes en continuité d'exploitation, il nous faut avant le 15 mars le prévisionnel de trésorerie 2027 et une lettre de soutien de Delta Invest. »

## 6. Références

- Code de commerce, art. L. 123-20 (prudence, prise en compte des risques et pertes nés au cours de l'exercice même s'ils sont connus entre la clôture et l'établissement des comptes) ; art. L. 123-13 et R. 123-196 (informations en annexe) ; art. L. 223-42 (capitaux propres inférieurs à la moitié du capital social).
- PCG (règlement ANC n° 2014-03 modifié) : événements postérieurs à la clôture, continuité d'exploitation, dépréciation des stocks à la valeur nette de réalisation.
- CGI, art. 272, 1 (récupération de la TVA sur créances irrécouvrables) ; art. 39, 1-5° (dépréciations et provisions) ; art. 223 A et suivants (intégration fiscale).
- Code de commerce, livre VI (procédures collectives : déclaration des créances, liquidation judiciaire).
