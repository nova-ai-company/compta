# Corrigé E15-07 — Test technique : du journal de paie aux écritures de salaires et de charges sociales

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-07](../exercices/E15-07_journal-de-paie-ecritures-controle.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Étape 1 — Toujours refaire les totaux avant de saisir (question 1)
Le logiciel de paie est fiable… sauf quand un récapitulatif a été retouché ou mal paramétré. On refait donc trois additions :
- **Brut** : 89 420,00 + 3 860,00 + 2 150,00 + 1 640,00 + 1 690,00 = **98 760,00 €** ✓
- **Cotisations salariales** : 13 450,20 + 3 950,40 + 1 205,30 = **18 605,90 €** ✓
- **Cotisations patronales** : 22 870,15 + 5 925,60 + 1 807,95 = **30 603,70 €** ✗ — le journal affiche **30 630,70 €** (écart de 27,00 €, typique d'une inversion de chiffres : 30 603 / 30 630). On comptabilise **le détail** (les montants par organisme, qui sont ceux de la DSN), pas le total erroné, et on signale l'écart au service paie.
- **Net avant impôt** : 98 760,00 − 18 605,90 = 80 154,10 € ✓
- **Net à payer** : 80 154,10 − 2 318,47 − 1 500,00 − 420,00 − 1 296,00 + 1 284,60 = **75 904,23 €** ✓

### Étape 2 — La logique de l'écriture de paie (question 2)
Une écriture de paie se lit comme le bulletin :
- **Le brut est une charge** pour l'entreprise → **6411 au débit** (98 760,00 €).
- Tout ce qui est **retenu** sur le brut est de l'argent que l'entreprise doit reverser à quelqu'un d'autre que le salarié → **crédit** du compte de ce tiers : URSSAF (431), caisses (437…), DGFiP pour le prélèvement à la source (4421), commissaire de justice pour la saisie (427), fournisseur des titres pour la part salariale (467TR).
- **L'acompte** a déjà été versé le 15/10 : il avait été mis au débit de 425 (créance sur les salariés). On le **crédite** maintenant pour solder ce compte : le salarié « rembourse » l'acompte par déduction sur son salaire.
- **Les IJSS en subrogation** : l'employeur les avance au salarié (elles augmentent le net) et va les récupérer auprès de la CPAM. C'est donc une **créance sur la CPAM** → **4387 au débit**, et une dette de plus envers le salarié → crédit de 421. Elles ne passent pas en charge (elles ne sont pas dans le brut) et ne passent pas en produit.
- Ce qui reste, **le net à payer**, est la dette envers les salariés → **421 au crédit**.

Les **charges patronales** sont une seconde charge (comptes 645x, 647 au débit) et une dette envers les mêmes organismes (crédit 431, 437…).

### Étape 3 — Les titres-restaurant (question 3)
GSF Riviera achète 360 titres à 9,00 € = 3 240,00 € : c'est une **avance** pour le compte des salariés et de l'entreprise, on la met en 467TR (débit). Ensuite la paie répartit ce montant : 40 % retenus sur les salariés (1 296,00 €) et 60 % à la charge de l'employeur (1 944,00 €, compte 647). Les deux crédits de 467TR (1 296,00 + 1 944,00 = 3 240,00 €) soldent le compte. S'il ne l'est pas, c'est que le nombre de titres commandés ne correspond pas au nombre de titres retenus en paie.

### Étape 4 — Les règlements (question 4)
Chaque dette créée par la paie est soldée par un débit du compte de tiers et un crédit de 512 ; l'IJSS est l'inverse (on encaisse : 512 au débit, 4387 au crédit).

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Dû à l'URSSAF (431) | 13 450,20 + 22 870,15 | **36 320,35 €** |
| Dû à l'AGIRC-ARRCO (437ARR) | 3 950,40 + 5 925,60 | **9 876,00 €** |
| Dû à la prévoyance (437PRV) | 1 205,30 + 1 807,95 | **3 013,25 €** |
| Dû à la DGFiP (4421) | prélèvement à la source | 2 318,47 € |
| Titres-restaurant part salariale | 360 × 9,00 × 40 % = 360 × 3,60 | 1 296,00 € |
| Titres-restaurant part patronale | 360 × 9,00 × 60 % = 360 × 5,40 | 1 944,00 € |
| Contrôle titres | 1 296,00 + 1 944,00 | 3 240,00 € = facture ✓ |
| Total cotisations patronales (corrigé) | 22 870,15 + 5 925,60 + 1 807,95 | 30 603,70 € |
| **Coût total employeur** (question 7) | 98 760,00 + 30 603,70 + 1 944,00 | **131 307,70 €** |

Le coût employeur ne comprend **pas** les IJSS (récupérées auprès de la CPAM) ni le prélèvement à la source, l'acompte ou la saisie (qui sont pris sur le salaire du salarié, déjà compté dans le brut).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | BQ | 425 | Personnel – avances et acomptes | Rappel : acomptes octobre 2026 (2 salariés) | 1 500,00 | |
| 15/10/2026 | BQ | 512 | Banque | Rappel : acomptes octobre 2026 | | 1 500,00 |
| 20/10/2026 | AC | 467TR | Titres-restaurant | Titres Azur TA-26-10-0457 – 360 titres | 3 240,00 | |
| 20/10/2026 | AC | 401TRA | Fournisseur Titres Azur | Titres Azur TA-26-10-0457 | | 3 240,00 |
| 20/10/2026 | BQ | 401TRA | Fournisseur Titres Azur | Prélèvement TA-26-10-0457 | 3 240,00 | |
| 20/10/2026 | BQ | 512 | Banque | Prélèvement TA-26-10-0457 | | 3 240,00 |
| 30/10/2026 | PA | 6411 | Salaires, appointements | Paie 10/2026 Nice – brut | 98 760,00 | |
| 30/10/2026 | PA | 4387 | Organismes sociaux – produits à recevoir | Paie 10/2026 – IJSS subrogées à recevoir CPAM | 1 284,60 | |
| 30/10/2026 | PA | 431 | Sécurité sociale (URSSAF) | Paie 10/2026 – cotisations salariales URSSAF | | 13 450,20 |
| 30/10/2026 | PA | 437ARR | Caisse de retraite AGIRC-ARRCO | Paie 10/2026 – retraite salariale | | 3 950,40 |
| 30/10/2026 | PA | 437PRV | Organisme de prévoyance et mutuelle | Paie 10/2026 – prévoyance salariale | | 1 205,30 |
| 30/10/2026 | PA | 4421 | Prélèvements à la source | Paie 10/2026 – PAS | | 2 318,47 |
| 30/10/2026 | PA | 425 | Personnel – avances et acomptes | Paie 10/2026 – reprise acomptes du 15/10 | | 1 500,00 |
| 30/10/2026 | PA | 427 | Personnel – oppositions | Paie 10/2026 – saisie sur salaire | | 420,00 |
| 30/10/2026 | PA | 467TR | Titres-restaurant | Paie 10/2026 – titres part salariale | | 1 296,00 |
| 30/10/2026 | PA | 421 | Personnel – rémunérations dues | Paie 10/2026 – net à payer | | 75 904,23 |
| 30/10/2026 | PA | 6451 | Cotisations à l'URSSAF | Paie 10/2026 – URSSAF patronale | 22 870,15 | |
| 30/10/2026 | PA | 6453 | Cotisations aux caisses de retraite | Paie 10/2026 – retraite patronale | 5 925,60 | |
| 30/10/2026 | PA | 6452 | Cotisations aux mutuelles et à la prévoyance | Paie 10/2026 – prévoyance patronale | 1 807,95 | |
| 30/10/2026 | PA | 647 | Autres charges sociales | Paie 10/2026 – titres part patronale | 1 944,00 | |
| 30/10/2026 | PA | 431 | Sécurité sociale (URSSAF) | Paie 10/2026 – URSSAF patronale | | 22 870,15 |
| 30/10/2026 | PA | 437ARR | Caisse de retraite AGIRC-ARRCO | Paie 10/2026 – retraite patronale | | 5 925,60 |
| 30/10/2026 | PA | 437PRV | Organisme de prévoyance et mutuelle | Paie 10/2026 – prévoyance patronale | | 1 807,95 |
| 30/10/2026 | PA | 467TR | Titres-restaurant | Paie 10/2026 – titres part patronale | | 1 944,00 |
| 30/10/2026 | BQ | 421 | Personnel – rémunérations dues | Virement salaires nets 10/2026 | 75 904,23 | |
| 30/10/2026 | BQ | 512 | Banque | Virement salaires nets 10/2026 | | 75 904,23 |
| 05/11/2026 | BQ | 431 | Sécurité sociale (URSSAF) | DSN 10/2026 – URSSAF | 36 320,35 | |
| 05/11/2026 | BQ | 437ARR | Caisse de retraite AGIRC-ARRCO | DSN 10/2026 – AGIRC-ARRCO | 9 876,00 | |
| 05/11/2026 | BQ | 437PRV | Organisme de prévoyance et mutuelle | DSN 10/2026 – prévoyance | 3 013,25 | |
| 05/11/2026 | BQ | 4421 | Prélèvements à la source | DSN 10/2026 – PAS reversé DGFiP | 2 318,47 | |
| 05/11/2026 | BQ | 512 | Banque | DSN 10/2026 – règlements | | 51 528,07 |
| 10/11/2026 | BQ | 427 | Personnel – oppositions | Saisie sur salaire 10/2026 – commissaire de justice | 420,00 | |
| 10/11/2026 | BQ | 512 | Banque | Saisie sur salaire 10/2026 | | 420,00 |
| 18/11/2026 | BQ | 512 | Banque | CPAM – IJSS subrogation 10/2026 | 1 284,60 | |
| 18/11/2026 | BQ | 4387 | Organismes sociaux – produits à recevoir | CPAM – IJSS subrogation 10/2026 | | 1 284,60 |
| | | | | **Totaux** | **269 709,20** | **269 709,20** |

**Tableau de contrôle des comptes de tiers (question 5)**

| Compte | Débits | Crédits | Solde |
|---|---|---|---|
| 421 | 75 904,23 | 75 904,23 | 0,00 ✓ |
| 425 | 1 500,00 | 1 500,00 | 0,00 ✓ |
| 427 | 420,00 | 420,00 | 0,00 ✓ |
| 431 | 36 320,35 | 13 450,20 + 22 870,15 = 36 320,35 | 0,00 ✓ |
| 437ARR | 9 876,00 | 3 950,40 + 5 925,60 = 9 876,00 | 0,00 ✓ |
| 437PRV | 3 013,25 | 1 205,30 + 1 807,95 = 3 013,25 | 0,00 ✓ |
| 4387 | 1 284,60 | 1 284,60 | 0,00 ✓ |
| 4421 | 2 318,47 | 2 318,47 | 0,00 ✓ |
| 467TR | 3 240,00 | 1 296,00 + 1 944,00 = 3 240,00 | 0,00 ✓ |

> Dans la vraie vie, le contrôle se fait aussi **avec un document externe** : le montant de 431 doit égaler le montant URSSAF de la DSN, celui de 4421 le montant de PAS de la DSN, celui de 421 le total du fichier de virement des salaires. Un compte social qui ne se solde pas chaque mois est un signal d'alerte (erreur de paramétrage, régularisation URSSAF, paiement oublié).

## 4. Points d'attention / pièges

- **Total patronal faux** (30 630,70 € au lieu de 30 603,70 €) : si on saisit le total, l'écriture est déséquilibrée de 27,00 € ou, pire, on « force » l'équilibre sur un compte. On saisit le détail par organisme et on prévient la paie.
- **Acompte** : ne pas le déduire une seconde fois par la banque. Il a été payé le 15/10 (425 / 512) ; à la paie on crédite seulement 425.
- **Saisie sur salaire** : l'argent n'appartient ni à l'entreprise ni au salarié ; c'est une dette envers le commissaire de justice → 427, pas 421 ni 6411.
- **IJSS** : la note de l'ancienne assistante (pièce 3, question 6) est **doublement fausse** :
  1. le compte **791 Transferts de charges n'existe plus** depuis le PCG applicable aux exercices ouverts à compter du 01/01/2025 (règlement ANC n° 2022-06) ;
  2. ici, les IJSS ne sont **pas dans le brut** : elles ne sont ni une charge ni un produit, seulement une avance faite pour le compte de la CPAM → créance 4387, soldée à l'encaissement.
  Si le logiciel de paie avait **maintenu tout le salaire en brut** (méthode différente), le remboursement de la CPAM viendrait **en diminution de la charge de salaires (6411)**, jamais en 791.
- **Titres-restaurant** : la part salariale n'est pas une cotisation ; elle diminue le net et rembourse une partie des titres achetés.
- **Coût employeur** : brut + charges patronales + part patronale des titres. Ne pas y ajouter le PAS (il est déjà dans le brut, c'est l'impôt du salarié).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse orale à la question 6 :**
> « Je ne passerais pas en 791 : ce compte a été supprimé avec le nouveau plan comptable 2025. Et ici, les IJSS ne sont pas dans le brut : l'employeur les avance au salarié, donc j'enregistre une créance sur la CPAM au moment de la paie, que je solde quand la CPAM paie. Si le brut incluait tout le salaire maintenu, le remboursement viendrait en moins des salaires. »

**Mail au service paie :**
> « Bonjour, sur le journal de paie d'octobre de Nice, le total des cotisations patronales affiché est 30 630,70 € alors que la somme des lignes donne 30 603,70 € (URSSAF 22 870,15 + AGIRC-ARRCO 5 925,60 + prévoyance 1 807,95). J'ai comptabilisé le détail, qui correspond à la DSN. Pouvez-vous vérifier le paramétrage de l'état récapitulatif ? Merci. »

**Contrôles mensuels à présenter en entretien** : rapprochement journal de paie / DSN / balance (6411, 645x) ; suivi des IJSS en attente (4387) par salarié, avec relance de la CPAM au-delà d'un mois ; contrôle du nombre de titres commandés / titres retenus.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG, règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06 : suppression des comptes de transfert de charges (791, 796, 797) pour les exercices ouverts à compter du 01/01/2025.
- PCG : comptes 421, 425, 427, 431, 437, 438, 4421, 641, 645, 647.
- Code du travail : règles de la saisie des rémunérations et de l'acompte sur salaire (*articles à citer selon le texte en vigueur*).
- Code de la sécurité sociale : indemnités journalières et subrogation de l'employeur (*références à vérifier*).
- CGI : prélèvement à la source de l'impôt sur le revenu, reversé par l'employeur collecteur via la DSN.
