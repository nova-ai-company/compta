# E05-01 — Rapprochement bancaire de septembre et écart introuvable
**Client :** C01 — Boulangerie Dupain SARL | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** rapprochement bancaire, suspens, commissions titres-restaurant, recherche d'écart

**Corner case :** oui — après traitement de tous les suspens, il reste un écart « inexpliqué » de quelques centaines d'euros.

## La mise en situation

Lundi 5 octobre 2026, Marc Dupain a déposé au cabinet sa boîte à chaussures de septembre. Votre collègue a importé le relevé bancaire et saisi les pièces ; elle est partie en congé en vous laissant ce post-it :

> « Rappro de septembre Dupain pas fini. Il me reste un écart que je ne trouve pas, j'ai pensé le mettre en 471 en attendant. Tu valides ? — Inès »

Hélène Ferrand passe derrière vous : « Pas de 471 pour boucler un rapprochement, on cherche. Et vérifiez que les suspens d'août sont bien sortis. »

## Les pièces

### Pièce 1 — État de rapprochement au 31/08/2026 (archivé au dossier)

| Relevé Banque Populaire Auvergne Rhône Alpes | Montant | Compte 512 BPAURA | Montant |
|---|---|---|---|
| Solde créditeur du relevé au 31/08/2026 | 18 245,37 | Solde débiteur du 512 au 31/08/2026 | 18 725,37 |
| – Chèque n° 4402 du 28/08 (Grands Moulins du Rhône) non débité | – 1 860,00 | | |
| + Remise espèces du 31/08 (bordereau 0831) non créditée | + 2 340,00 | | |
| **Solde rectifié** | **18 725,37** | **Solde rectifié** | **18 725,37** |

*Établi par : Inès M. — Visé : H. Ferrand*

### Pièce 2 — Relevé de compte

```
BANQUE POPULAIRE AUVERGNE RHÔNE ALPES — Agence Lyon Cordeliers
Relevé de compte courant professionnel n° 09/2026 — du 01/09/2026 au 30/09/2026
Titulaire : SARL BOULANGERIE DUPAIN — 12 rue de la Charité 69002 LYON
IBAN : FR76 1680 7000 3412 3456 7890 112 — BIC CCBPFRPPGRE
Autorisation de découvert : 5 000,00 EUR
```

| Date | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|
| 01/09 | **SOLDE CRÉDITEUR AU 31/08/2026** | | | 18 245,37 |
| 01/09 | REMISE ESPECES 31/08 BORD. 0831 |  | 2 340,00 | 20 585,37 |
| 02/09 | PRLV SEPA URSSAF RHONE-ALPES | 1 912,00 |  | 18 673,37 |
| 03/09 | CHEQUE N° 4402 | 1 860,00 |  | 16 813,37 |
| 04/09 | REMISE CB TPE 0012 DU 01-03/09 |  | 4 215,60 | 21 028,97 |
| 05/09 | PRLV SEPA SCI CHARITE LOYER SEPT | 2 400,00 |  | 18 628,97 |
| 08/09 | REMISE ESPECES BORD. 0907 |  | 3 180,00 | 21 808,97 |
| 10/09 | VIR SEPA EDENRED FRANCE REMB TR 2026-08 |  | 1 128,40 | 22 937,37 |
| 12/09 | CHEQUE N° 4403 | 642,30 |  | 22 295,07 |
| 15/09 | PRLV SEPA EDF ENTREPRISES | 786,45 |  | 21 508,62 |
| 15/09 | VIR SEPA SALAIRES AOUT 2026 (6 bénéf.) | 8 925,60 |  | 12 583,02 |
| 18/09 | REMISE CB TPE 0012 DU 04-17/09 |  | 6 512,80 | 19 095,82 |
| 20/09 | ECHEANCE PRET N° 4471 0098 | 1 245,18 |  | 17 850,64 |
| 22/09 | CHEQUE N° 4405 | 1 524,00 |  | 16 326,64 |
| 25/09 | REMISE ESPECES BORD. 0924 |  | 2 960,00 | 19 286,64 |
| 28/09 | FRAIS TENUE DE COMPTE PRO | 38,50 |  | 19 248,14 |
| 28/09 | COMMISSIONS ENCAISSEMENT CB 09/2026 | 96,42 |  | 19 151,72 |
| 29/09 | COTISATION CARTE BUSINESS | 12,00 |  | 19 139,72 |
| 30/09 | PRLV SEPA ORANGE PRO | 54,99 |  | 19 084,73 |
| 30/09 | **SOLDE CRÉDITEUR AU 30/09/2026** | **19 497,44** | **20 336,80** | **19 084,73** |

*Frais de tenue de compte et cotisation carte : opérations exonérées de TVA. Commissions CB : exonérées de TVA.*

### Pièce 3 — Extrait du grand livre, compte 512 BPAURA (septembre 2026, ordre de saisie)

| Date | Jnl | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|---|
| 01/09 | | **Report solde débiteur au 31/08** | | | 18 725,37 |
| 02/09 | BQ | URSSAF août |  | 1 912,00 | 16 813,37 |
| 05/09 | BQ | Loyer septembre SCI Charité |  | 2 400,00 | 14 413,37 |
| 04/09 | BQ | Remise CB 01-03/09 | 4 215,60 |  | 18 628,97 |
| 07/09 | BQ | Remise espèces bord. 0907 | 3 180,00 |  | 21 808,97 |
| 10/09 | BQ | Edenred remb. TR août (bordereau 1 175,00) | 1 175,00 |  | 22 983,97 |
| 10/09 | BQ | Ch. 4403 Metro |  | 642,30 | 22 341,67 |
| 15/09 | BQ | EDF |  | 786,45 | 21 555,22 |
| 15/09 | BQ | Salaires août |  | 8 925,60 | 12 629,62 |
| 16/09 | BQ | Ch. 4404 Emballages Lyonnais |  | 412,80 | 12 216,82 |
| 18/09 | BQ | Remise CB 04-17/09 | 6 512,80 |  | 18 729,62 |
| 20/09 | BQ | Échéance prêt 4471 |  | 1 245,18 | 17 484,44 |
| 19/09 | BQ | Ch. 4405 Grands Moulins du Rhône |  | 1 254,00 | 16 230,44 |
| 24/09 | BQ | Remise espèces bord. 0924 | 2 960,00 |  | 19 190,44 |
| 29/09 | BQ | Ch. 4406 Pâtisserie Supply |  | 834,00 | 18 356,44 |
| 30/09 | BQ | Remise espèces bord. 0930 | 2 115,00 |  | 20 471,44 |
| 30/09 | BQ | Remise CB 18-30/09 | 1 887,40 |  | 22 358,84 |
| | | **Total septembre / solde débiteur au 30/09** | **22 045,80** | **18 412,33** | **22 358,84** |

### Pièce 4 — Bordereau de remboursement Edenred (extrait)

```
EDENRED FRANCE — Remboursement de titres-restaurant
Affilié : BOULANGERIE DUPAIN — n° affilié 6900 4412
Période : titres déposés en août 2026 — Date de virement : 10/09/2026
Valeur faciale des titres remboursés ..................... 1 175,00 EUR
Commission de remboursement HT (3,30 %) ...................   38,78 EUR
Frais de traitement HT ...................................     0,05 EUR
TVA 20 % sur commission et frais ..........................     7,77 EUR
Total commission TTC ......................................    46,60 EUR
NET VIRÉ ................................................. 1 128,40 EUR
```

### Pièce 5 — Facture Orange (extrait)
```
Orange Business — Facture n° FO-2026-09-7781 du 22/09/2026 — Client : SARL Boulangerie Dupain
Forfait Pro Fibre + mobile — période du 01/10 au 31/10/2026
Total HT : 45,83 EUR — TVA 20 % : 9,16 EUR — Total TTC : 54,99 EUR — prélevé le 30/09/2026
```

### Pièce 6 — Talon du chéquier (extrait)
```
N° 4405 — 19/09/2026 — Ordre : Grands Moulins du Rhône — Montant : 1 524,00 € — Objet : fact. GM-26-0877 farine T65
N° 4406 — 29/09/2026 — Ordre : Pâtisserie Supply — Montant : 834,00 €
```

## Travail à faire
1. Vérifiez le dénouement des suspens de l'état au 31/08/2026.
2. Pointez le relevé et le compte 512 ; listez les opérations non pointées de chaque côté.
3. Établissez l'état de rapprochement au 30/09/2026 et chiffrez l'écart résiduel.
4. Trouvez l'origine de l'écart résiduel en expliquant votre méthode de recherche.
5. Passez les écritures nécessaires au 30/09/2026 et présentez l'état de rapprochement définitif.
6. Répondez à Inès sur sa proposition d'utiliser le 471.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E05-01_corrige.md)
