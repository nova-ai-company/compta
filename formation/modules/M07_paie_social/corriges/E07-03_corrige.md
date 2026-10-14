# Corrigé E07-03 — Arrêt maladie avec subrogation et IJSS

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-03](../exercices/E07-03_arret-maladie-subrogation-leroy.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **Trois acteurs, trois flux** : la CPAM verse des IJSS (revenu de remplacement, **pas un salaire**) ; l'employeur verse un **complément** (qui, lui, est un salaire soumis à cotisations) ; en **subrogation**, l'employeur avance les IJSS au salarié avec la paie et les récupère auprès de la CPAM.
2. **Sur le bulletin** : on retient l'absence (14 jours), on ajoute le complément employeur (salaire des jours 4 à 14 − IJSS brutes), puis, sous le net, on ajoute les **IJSS nettes** (déjà diminuées de la CSG/CRDS précomptée par la CPAM). Les IJSS maladie sont **imposables** : elles entrent dans le net imposable et supportent le PAS (en subrogation, c'est l'employeur qui le prélève).
3. **En comptabilité** : les IJSS avancées ne sont pas une charge de l'entreprise. La façon la plus directe de le traduire est de débiter une **créance sur la CPAM** (4387) dans l'écriture de paie : seul le brut soumis (salaire des jours travaillés + complément) passe en 6411. **Le compte 791 « Transferts de charges » est supprimé depuis les exercices ouverts au 01/01/2025** (règlement ANC n° 2022-06) : on ne l'utilise plus, ni pour la maladie, ni pour l'AT.
4. **Variante** : débiter 6411 du salaire intégralement maintenu, puis, à réception des IJSS, créditer un compte de charges de personnel (641, *subdivision selon la nomenclature 2025 du PCG* — remboursements d'IJSS) — c'est ce qu'il faut faire pour corriger l'été.

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 IJSS

| Élément | Calcul | Montant |
|---|---|---|
| SJB | (2 400,00 × 3) / 91,25 | 78,90 € |
| IJ brute journalière | 78,90 × 50 % | 39,45 € |
| Jours d'arrêt | du 08/09 au 21/09 | 14 jours |
| Carence | 08, 09, 10/09 | 3 jours |
| Jours indemnisés | 11/09 → 21/09 | 11 jours |
| **IJSS brutes** | 39,45 × 11 | **433,95 €** |
| CSG/CRDS 6,70 % | 433,95 × 6,70 % | 29,07 € |
| **IJSS nettes** | 433,95 − 29,07 | **404,88 €** ✔ (= virement CPAM) |
| Part imposable des IJSS | 433,95 − CSG déductible (433,95 × 3,80 % = 16,49) | 417,46 € |

### 2.2 Bulletin de septembre

| Rubrique | Calcul | Salarié | Patronal |
|---|---|---|---|
| Salaire de base | | 2 400,00 | |
| Absence maladie 14 jours | 2 400 / 30 × 14 | − 1 120,00 | |
| Complément employeur (jours 4 à 14) | 2 400 / 30 × 11 = 880,00 − IJSS brutes 433,95 | + 446,05 | |
| **Brut soumis** | 2 400 − 1 120 + 446,05 | **1 726,05** | |
| Sécu vieillesse 7,30 % | | 126,00 | |
| URSSAF patronal 36,50 % | | | 630,01 |
| AGIRC-ARRCO 4,01 % / 6,01 % | | 69,21 | 103,74 |
| Mutuelle | | 30,00 | 30,00 |
| Réduction générale | | | − 332,89 |
| CSG déductible 6,80 % | base 1 726,05 × 98,25 % + 30,00 = 1 725,84 | 117,36 | |
| CSG non déd. + CRDS 2,90 % | 1 725,84 × 2,90 % | 50,05 | |
| **Total cotisations** | | **392,62** | **430,86** |
| Net avant IJSS | 1 726,05 − 392,62 | 1 333,43 | |
| IJSS nettes (subrogation) | | + 404,88 | |
| **Net à payer avant IR** | | **1 738,31** | |
| Net imposable | 1 726,05 − (126,00 + 69,21 + 30,00 + 117,36) + 30,00 + 417,46 | 1 830,94 | |
| PAS 3,8 % | 1 830,94 × 3,8 % | − 69,58 | |
| **Net payé** | | **1 668,73** | |

Vérification du maintien : Benoît perçoit, pour les jours 4 à 14, 446,05 € de complément + 433,95 € d'IJSS brutes = 880,00 € = le salaire brut de ces 11 jours ✔. Les 3 jours de carence (240,00 €) sont perdus.

Patronal ventilé : URSSAF 630,01 − 282,62 = **347,39 €** ; retraite 103,74 − 50,27 = **53,47 €** ; mutuelle **30,00 €**. Total 430,86 €.

Organismes : 431 = salarial (126,00 + 117,36 + 50,05 = 293,41) + patronal 347,39 = **640,80 €** ; 4371 = 69,21 + 53,47 = **122,68 €** ; 4372 = **60,00 €**.

### 2.3 Été : AT de J. Petit
Les IJSS AT (1 186,50 €) ont remboursé une partie d'un salaire **intégralement maintenu et passé en 6411** en juillet. Il faut les porter **en diminution de la charge de personnel**, pas en produit.

## 3. Écritures comptables

**Paie de septembre de Benoît Garcia**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD-PAIE | 6411 | Salaires, appointements | Paie 09/2026 B. Garcia – brut soumis | 1 726,05 | |
| 30/09/2026 | OD-PAIE | 4387 | Organismes sociaux – produits à recevoir (IJSS subrogation) | IJSS nettes avancées 11/09–21/09 | 404,88 | |
| 30/09/2026 | OD-PAIE | 6451 | Cotisations à l'URSSAF | Patronal URSSAF net | 347,39 | |
| 30/09/2026 | OD-PAIE | 6453 | Cotisations aux caisses de retraite | Patronal AGIRC-ARRCO net | 53,47 | |
| 30/09/2026 | OD-PAIE | 6452 | Cotisations aux mutuelles | Mutuelle patronale | 30,00 | |
| 30/09/2026 | OD-PAIE | 431 | Sécurité sociale (URSSAF) | Sal. + pat. | | 640,80 |
| 30/09/2026 | OD-PAIE | 4371 | AGIRC-ARRCO | Sal. + pat. | | 122,68 |
| 30/09/2026 | OD-PAIE | 4372 | Mutuelle | Sal. + pat. | | 60,00 |
| 30/09/2026 | OD-PAIE | 4421 | État – prélèvement à la source | PAS (y compris sur IJSS) | | 69,58 |
| 30/09/2026 | OD-PAIE | 421 | Personnel – rémunérations dues | Net payé B. Garcia | | 1 668,73 |
| | | | | **Totaux** | **2 561,79** | **2 561,79** |

**Encaissement des IJSS**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/10/2026 | BQ | 512 | Banque BNP Paribas | CPAM IJ B. Garcia subrogation | 404,88 | |
| 02/10/2026 | BQ | 4387 | Organismes sociaux – produits à recevoir (IJSS subrogation) | CPAM IJ B. Garcia subrogation | | 404,88 |
| | | | | **Totaux** | **404,88** | **404,88** |

**Correction des IJSS AT de l'été**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 791 | Transferts de charges (compte supprimé) | Annulation imputation IJ AT J. Petit | 1 186,50 | |
| 30/09/2026 | OD | 641 | Rémunérations du personnel – remboursements IJSS (*subdivision selon la nomenclature 2025 du PCG*) | IJ AT J. Petit 07/2026 en diminution de charge | | 1 186,50 |
| | | | | **Totaux** | **1 186,50** | **1 186,50** |

> Si le paramétrage du logiciel le permet, l'idéal est de reprendre l'écriture du 21/08 elle-même (même exercice, pas encore clôturé) plutôt que de passer une OD : il ne doit **plus exister** de compte 791 dans le plan de comptes du dossier — supprimez-le ou bloquez-le.

## 4. Points d'attention / pièges

- **Ne jamais utiliser le 791** (ni 796 ni 797) : supprimés par le règlement ANC n° 2022-06 pour les exercices ouverts à compter du 01/01/2025. Un compte 791 mouvementé dans une balance 2026 = anomalie de révision.
- **Pas de produit exceptionnel** non plus : un arrêt maladie n'a rien de « majeur et inhabituel ».
- Le **complément employeur** est un salaire : il est soumis à cotisations et entre dans la réduction générale. Les **IJSS** ne le sont pas (sauf CSG/CRDS précomptée).
- Le **PAS** s'applique aux IJSS subrogées : l'oublier crée un écart avec la DSN (bloc « revenus de remplacement »).
- La CPAM verse sur la base de l'**attestation de salaire** transmise via la DSN (signalement d'arrêt de travail sous 5 jours) : si le signalement est tardif ou erroné, l'IJSS reçue diffère de l'IJSS avancée → l'écart reste à la charge de l'employeur (6411) ou à recalculer.
- **Délai de carence** : en AT, pas de carence ; en maladie, 3 jours (sauf accord plus favorable) ; le maintien légal ne démarre qu'au 8e jour.
- Le délai d'envoi de l'arrêt (48 h) conditionne le versement intégral des IJSS en cas de récidive : contrôler la date de réception.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- **Révision au 31/12/2026** : justifier le solde du 4387 salarié par salarié (état des arrêts en subrogation, IJSS avancées, IJSS reçues). Un solde ancien (> 3 mois) = signalement DSN manquant, IJSS refusée ou contrôle médical : relancer la CPAM via net-entreprises et, si l'IJSS est définitivement perdue, constater la charge (6411) — ou demander le remboursement au salarié si l'IJSS avancée n'était pas due (dans la limite des règles de compensation).
- **Contrôle de cohérence annuel** : brut 641 nets des remboursements IJSS ↔ brut DSN.
- Paramétrer dans le logiciel un compte unique « IJSS subrogation » et **désactiver** le 791.
- **Mail à Bruno Leroy** :

> Bonjour Monsieur Leroy,
> Le bulletin de septembre de Benoît Garcia est établi : les trois jours de carence ne sont pas payés, puis son salaire est intégralement maintenu par le complément que vous versez et par les indemnités de la CPAM, que vous avez bien reçues le 2 octobre (404,88 €).
> Votre interlocuteur a raison : depuis 2025, le compte « transfert de charges » n'existe plus. Les indemnités journalières de l'accident de Jordan Petit ont été reclassées en diminution des salaires ; cela ne change pas votre résultat.
> Pensez à nous transmettre chaque arrêt dès réception pour que la déclaration à la CPAM parte dans les 5 jours.
> Bien cordialement,

## 6. Références

- Code de la sécurité sociale : articles L. 321-1 et L. 323-1 et suivants (IJSS maladie), R. 323-1 et suivants (délai de carence, calcul du gain journalier) ; article R. 323-11 (subrogation) — *paramètres de calcul à vérifier*.
- Code du travail : articles L. 1226-1 et D. 1226-1 et suivants (maintien légal de salaire).
- CGI, article 80 quinquies (imposition des indemnités journalières).
- Règlement ANC n° 2022-06 modifiant le règlement ANC n° 2014-03 : suppression des comptes de transferts de charges ; PCG, comptes 641, 4387, 431, 437, 4421, 421.
