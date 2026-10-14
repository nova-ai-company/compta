# E07-01 — Journal de paie mensuel et contrôle de la DSN
**Client :** C01 — Boulangerie Dupain SARL | **Difficulté :** ★★☆ | **Durée estimée :** 60 min | **Thèmes :** écriture de paie, 421/425/427/431/437/4421, heures supplémentaires, réduction générale, rapprochement paie / DSN, rémunération du gérant TNS

**Corner case :** oui — DSN déposée à partir d'une version provisoire de la paie (heures supplémentaires manquantes) + virement « salaire » du gérant majoritaire mélangé à la paie

## La mise en situation

Jeudi 9 octobre 2026, 9 h 10. Note d'Hélène Ferrand sur votre bureau :

> « Bonjour, Yasmine (gestionnaire paie) est en congé jusqu'au 19. La paie de septembre de la Boulangerie Dupain est faite et payée, la DSN est partie le 5. Pouvez-vous passer l'écriture de paie, l'écriture de règlement, et faire le contrôle paie / DSN avant l'échéance du 15 ? Marc a aussi déposé son relevé de septembre : il a écrit "salaire Marc" sur un virement, à traiter. Merci — H. F. »

Dans le dossier partagé, vous trouvez un post-it de Yasmine daté du 30/09 : *« Kévin : Marc m'a appelée ce matin, 4 h sup/semaine en septembre (17,33 h à 25 %). Bulletin refait et payé ce soir. »*

## Les pièces

### Pièce 1 — Paramètres de paie retenus par le logiciel (septembre 2026)

> Taux **simplifiés** pour l'exercice, regroupés par organisme — *valeurs à vérifier chaque année*. SMIC mensuel 35 h : 1 823,03 € ; PASS mensuel : 4 005 € (tous les salaires sont sous le plafond).

| Cotisation | Assiette | Part salariale | Part patronale | Organisme |
|---|---|---|---|---|
| Sécurité sociale vieillesse (plafonnée + déplafonnée) | Brut | 7,30 % | — | URSSAF |
| Maladie, vieillesse, allocations familiales, AT/MP (2,40 %), CSA, FNAL, dialogue social, chômage, AGS, **formation professionnelle 0,55 %**, **taxe d'apprentissage 0,59 %** | Brut | — | 37,026 % (au total) | URSSAF |
| Retraite complémentaire AGIRC-ARRCO T1 + CEG | Brut | 4,01 % | 6,01 % | AGIRC-ARRCO (caisse Pro BTP Alimentaire — fictive) |
| CSG déductible | 98,25 % du brut + part patronale mutuelle | 6,80 % | — | URSSAF |
| CSG non déductible + CRDS | idem | 2,90 % | — | URSSAF |
| Complémentaire santé (forfait mensuel 60 €) | Forfait | 25,00 € | 35,00 € | Mutuelle Rhône Santé (fictive) |
| Réduction de cotisations salariales sur HS | Rémunération des HS | − 11,31 % | — | URSSAF |
| Déduction forfaitaire patronale HS (< 20 salariés) | Par heure sup. | — | − 1,50 €/h | URSSAF |
| Réduction générale (calcul logiciel) | — | — | voir journal | URSSAF / AGIRC-ARRCO |

### Pièce 2 — Bulletin de paie de Kévin Morel (version définitive)

```
BOULANGERIE DUPAIN SARL — 12 rue de la Charité, 69002 Lyon
SIRET 912 345 001 00018 — APE 1071C — URSSAF Rhône-Alpes
Convention collective : Boulangerie-pâtisserie (entreprises artisanales) IDCC 843

BULLETIN DE PAIE — Période du 01/09/2026 au 30/09/2026 — Paiement le 30/09/2026 par virement
Salarié : Kévin MOREL — Ouvrier boulanger, niveau II coeff. 185 — Entrée 03/02/2022
N° SS : 1 95 04 69 ••• ••• •• — Contrat CDI temps plein 35 h

Rubrique                                   Base        Taux       Montant salarié  |  Montant / taux patronal
-------------------------------------------------------------------------------------------------------------
Salaire de base                            151,67 h    13,5162    2 050,00
Heures supplémentaires 25 %                 17,33 h    16,8952      292,79
SALAIRE BRUT                                                      2 342,79
Sécurité sociale vieillesse                2 342,79    7,30 %       171,02
Cotisations patronales URSSAF              2 342,79                          |  37,026 %       867,44
Retraite compl. AGIRC-ARRCO T1 + CEG       2 342,79    4,01 %        93,95   |   6,01 %        140,80
Complémentaire santé                                                 25,00   |                  35,00
Réduction salariale heures sup.              292,79   -11,31 %      -33,11
Réduction générale des cotisations                                           |                -483,18
Déduction forfaitaire patronale HS          17,33 h   1,50 €                 |                 -26,00
CSG déductible                             2 336,79    6,80 %       158,90
CSG non déductible + CRDS                  2 336,79    2,90 %        67,77
TOTAL COTISATIONS                                                   483,53   |                 534,06
NET À PAYER AVANT IMPÔT SUR LE REVENU                             1 859,26
  dont heures supplémentaires exonérées d'IR : 273,23
Net imposable                                                     1 688,80
Impôt sur le revenu prélevé à la source    1 688,80    2,10 %        35,46   (taux personnalisé)
NET PAYÉ                                                          1 823,80
Montant net social : 1 894,26
Coût total employeur : 2 876,85
Cumul brut annuel : 20 870,63   Cumul HS exonérées : 273,23
Dans votre intérêt et pour vous aider à faire valoir vos droits, conservez ce bulletin sans limitation de durée.
```

### Pièce 3 — Journal de paie récapitulatif de septembre 2026 (édition définitive du 30/09/2026, 17 h 42)

| Salarié | Brut | Cot. salariales | Net avant IR | Net imposable | Taux PAS | PAS | Acompte | Opposition | Net payé | Patronal URSSAF (net) | Patronal retraite (net) | Patronal mutuelle |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Julie DUPAIN — vendeuse resp. | 2 100,00 | 466,04 | 1 633,96 | 1 729,81 | 4,5 % | 77,84 | — | — | 1 556,12 | 283,54 | 38,35 | 35,00 |
| Kévin MOREL — boulanger | 2 342,79 | 483,53 | 1 859,26 | 1 688,80 | 2,1 % | 35,46 | — | — | 1 823,80 | 431,22 | 67,84 | 35,00 |
| Antoine RIVA — boulanger | 1 950,00 | 434,79 | 1 515,21 | 1 606,79 | 0,0 % | 0,00 | — | 120,00 | 1 395,21 | 165,97 | 18,31 | 35,00 |
| Léa FONTAINE — pâtissière | 2 000,00 | 445,20 | 1 554,80 | 1 647,80 | 3,2 % | 52,73 | — | — | 1 502,07 | 206,16 | 25,16 | 35,00 |
| Sonia MERCIER — vendeuse | 1 823,03 | 408,32 | 1 414,71 | 1 502,67 | 0,0 % | 0,00 | 300,00 | — | 1 114,71 | 58,81 | 0,00 | 35,00 |
| Inès BARBIER — vendeuse 24 h | 1 250,08 | 288,92 | 961,16 | 1 032,79 | 0,0 % | 0,00 | — | — | 961,16 | 40,35 | 0,00 | 35,00 |
| **TOTAL** | **11 465,90** | **2 526,80** | **8 939,10** | **9 208,66** | | **166,03** | **300,00** | **120,00** | **8 353,07** | **1 186,05** | **149,66** | **210,00** |

Ventilation complémentaire fournie par le logiciel :
- cotisations salariales : URSSAF 1 917,01 € (dont réduction HS − 33,11 €) ; AGIRC-ARRCO 459,79 € ; mutuelle 150,00 € ;
- réduction générale : 3 572,76 € (imputée 3 033,32 € sur l'URSSAF, 539,44 € sur l'AGIRC-ARRCO) ;
- dans le patronal URSSAF net : contribution formation professionnelle 63,06 € ; taxe d'apprentissage (part principale) 67,65 €.

### Pièce 4 — Accusé de dépôt et état récapitulatif de la DSN de septembre 2026

```
net-entreprises.fr — DSN mensuelle — Accusé de réception de dépôt
SIRET 912 345 001 00018 — Période 09/2026 — Nature : DSN mensuelle (01) — Type : normale
Date de dépôt : 05/10/2026 08:57 — Statut : CONFORME — Version paie source : « SIMUL_2026-09_v2 » du 28/09/2026

Effectif déclaré : 6 salariés            Total rémunérations brutes déclarées : 11 173,11
Prélèvement à la source (DGFiP) ............................. 166,03   prélèvement le 25/10 (*)
URSSAF (bordereau) — cotisations dues ...................... 2 901,00   paiement le 15/10/2026 (SEPA)
AGIRC-ARRCO — cotisations dues .............................   561,71   paiement le 15/10/2026 (SEPA)
Mutuelle Rhône Santé — cotisations dues ....................   360,00   paiement le 15/10/2026
(*) date indicative
```

### Pièce 5 — Extrait du relevé bancaire Crédit Lyonnais Rhône (fictif) — compte 512100

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 15/09/2026 | VIR ACOMPTE MERCIER S. | 300,00 | |
| 15/09/2026 | PRLV URSSAF RHONE-ALPES DSN 08/2026 | 2 875,40 | |
| 30/09/2026 | VIR SALAIRES 09/2026 (6 bénéficiaires) | 8 353,07 | |
| 30/09/2026 | VIR « SALAIRE MARC » | 2 200,00 | |

Annotation manuscrite de Marc Dupain sur le relevé : *« Mon salaire comme d'hab, à mettre avec la paie des gars ! »*

Extrait du procès-verbal d'AG du 12/06/2026 conservé au dossier juridique : *« L'assemblée fixe la rémunération mensuelle du gérant, M. Marc Dupain, à 2 200 € nets à compter du 1er juillet 2026, ses cotisations sociales personnelles étant prises en charge par la société. »*

## Travail à faire

1. Vérifiez sur le bulletin de Kévin Morel le passage du brut au net payé (cotisations salariales, net imposable, PAS). Expliquez pourquoi son net imposable est identique à celui qu'il aurait eu sans heures supplémentaires.
2. Passez au 30/09/2026 l'écriture de paie de septembre (journal OD de paie) à partir du journal définitif, en isolant la formation professionnelle et la taxe d'apprentissage.
3. Passez l'écriture de règlement des salaires du 30/09 et rappelez l'écriture de l'acompte du 15/09.
4. Rapprochez la DSN déposée du journal de paie. Chiffrez les écarts par organisme, expliquez leur origine et indiquez ce qu'il faut faire **avant le 15/10/2026**.
5. Traitez le virement « salaire Marc ». Marc a-t-il raison de vouloir l'intégrer à la paie ?
6. Rédigez le mail à Marc (5 à 8 lignes).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E07-01_corrige.md)
