# E05-02 — La caisse du Petit Zinc est créditrice
**Client :** C04 — Le Petit Zinc SAS | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** caisse, Z de caisse, virements internes 580, plafond des paiements en espèces, écarts de caisse

**Corner case :** oui — le solde de caisse passe créditeur plusieurs jours dans le mois, ce qui est physiquement impossible.

## La mise en situation

Le Petit Zinc (clôture au 30/06) a ouvert son exercice 2026-2027 le 1er juillet. Le cabinet tient la comptabilité mensuellement. En revoyant le mois de septembre 2026, le logiciel affiche une alerte rouge : **« Solde de caisse créditeur au 15/09/2026 »**.

Clara Rossi vous a envoyé les pièces par WhatsApp, comme d'habitude. Message vocal retranscrit :

> « Bonjour ! Pour la caisse je ne comprends pas, on n'a jamais été à découvert en caisse, ça n'existe pas ! Hugo a fait le comptage ce soir, il y a 3 687 € dans le coffre, fond de caisse compris. Ah et pour la Cave des Canuts on a payé en liquide, ils nous font 3 % de remise. Bisous. »

Hélène Ferrand : « Une caisse créditrice, c'est la première chose qu'un vérificateur imprime. Trouvez-moi toutes les causes, et on prévient Clara pour la Cave des Canuts. »

## Les pièces

### Pièce 1 — Grand livre du compte 530 Caisse, septembre 2026 (tel que saisi)

| Date | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|
| 01/09 | Report au 31/08 | | | 1 240,00 D |
| 01/09 | Z n° 2431 — espèces | 412,50 |  | 1 652,50 D |
| 01/09 | Ticket marché Saint-Antoine (herbes, fruits) |  | 86,40 | 1 566,10 D |
| 02/09 | Z n° 2432 — espèces | 388,00 |  | 1 954,10 D |
| 03/09 | Z n° 2433 — espèces | 455,20 |  | 2 409,30 D |
| 04/09 | Z n° 2434 — espèces | 521,70 |  | 2 931,00 D |
| 04/09 | Remise en banque bord. 0904 |  | 1 500,00 | 1 431,00 D |
| 05/09 | Z n° 2435 — espèces | 612,80 |  | 2 043,80 D |
| 05/09 | Cave des Canuts fact. CV-2611 (vins) |  | 1 450,00 | 593,80 D |
| 08/09 | Z n° 2436 — espèces | 302,10 |  | 895,90 D |
| 08/09 | Metro fact. 0189-4456 (produits d'entretien) |  | 342,18 | 553,72 D |
| 09/09 | Z n° 2437 — espèces | 366,90 |  | 920,62 D |
| 10/09 | Z n° 2438 — espèces | 401,30 |  | 1 321,92 D |
| 11/09 | Z n° 2439 — espèces | 588,60 |  | 1 910,52 D |
| 11/09 | Remise en banque bord. 0911 |  | 1 200,00 | 710,52 D |
| 11/09 | Avance extra M. Diallo |  | 200,00 | 510,52 D |
| 15/09 | Z n° 2441 — espèces | 344,80 |  | 855,32 D |
| 15/09 | Remise en banque bord. 0915 |  | 1 500,00 | 644,68 **C** |
| 15/09 | Remise espèces 15/09 (import relevé) |  | 1 500,00 | 2 144,68 **C** |
| 16/09 | Z n° 2442 — espèces | 397,50 |  | 1 747,18 **C** |
| 17/09 | Z n° 2443 — espèces | 433,10 |  | 1 314,08 **C** |
| 18/09 | Z n° 2444 — espèces | 569,90 |  | 744,18 **C** |
| 19/09 | Z n° 2445 — espèces | 702,30 |  | 41,88 **C** |
| 19/09 | Ticket marché Saint-Antoine |  | 64,20 | 106,08 **C** |
| 22/09 | Z n° 2446 — espèces | 318,40 |  | 212,32 D |
| 23/09 | Z n° 2447 — espèces | 377,60 |  | 589,92 D |
| 24/09 | Z n° 2448 — espèces | 420,00 |  | 1 009,92 D |
| 25/09 | Z n° 2449 — espèces | 611,20 |  | 1 621,12 D |
| 25/09 | Remise en banque bord. 0925 |  | 1 800,00 | 178,88 **C** |
| 26/09 | Z n° 2450 — espèces | 689,50 |  | 510,62 D |
| 29/09 | Z n° 2451 — espèces | 295,40 |  | 806,02 D |
| 30/09 | Z n° 2452 — espèces | 352,80 |  | 1 158,82 D |
| | **Totaux septembre** | **9 561,60** | **9 642,78** | **1 158,82 D** |

*Le restaurant est ouvert du mardi au samedi. Les remises d'espèces sont saisies dans le journal de caisse (contrepartie 580) à partir des bordereaux ; les relevés bancaires sont importés automatiquement.*

### Pièce 2 — Extrait du journal de banque importé (septembre 2026)

| Date | Libellé relevé | Compte débité | Compte crédité | Montant |
|---|---|---|---|---|
| 07/09 | VERSEMENT ESPECES BORD. 0904 | 512 | 580 | 1 500,00 |
| 09/09 | CB METRO LYON GERLAND | 401METRO | 512 | 342,18 |
| 14/09 | VERSEMENT ESPECES BORD. 0911 | 512 | 580 | 1 200,00 |
| 16/09 | VERSEMENT ESPECES BORD. 0915 | 512 | 530 | 1 500,00 |
| 28/09 | VERSEMENT ESPECES BORD. 0925 | 512 | 580 | 1 800,00 |

*(L'import du 16/09 a été affecté manuellement par un stagiaire.)*

### Pièce 3 — Photo WhatsApp : Z de caisse n° 2440

```
LE PETIT ZINC — 8 place Sathonay 69001 LYON — SIRET 834 567 210 00019
Logiciel de caisse certifié NF525 — Caisse 01
RAPPORT Z n° 2440 — Clôture du samedi 12/09/2026 à 23:41
--------------------------------------------------------
Couverts : 96
CA TTC TVA 10 % ............................ 2 214,30
CA TTC TVA 20 % ............................   632,00
TOTAL TTC .................................. 2 846,30
  dont TVA 10 % : 201,30 — TVA 20 % : 105,33
Règlements :
  Espèces .................................... 698,40
  Carte bancaire ........................... 1 973,90
  Titres-restaurant .......................... 174,00
Grand total perpétuel : 1 284 556,92
Signature : 7F3A-91C2-...
```

### Pièce 4 — Facture Cave des Canuts (extrait)

```
CAVE DES CANUTS SARL — 14 rue d'Austerlitz 69004 Lyon — SIREN 512 908 334 — TVA FR42 512 908 334
FACTURE CV-2611 du 03/09/2026 — Client : SAS Le Petit Zinc, 8 place Sathonay 69001 Lyon — SIREN 834 567 210
Livraison de biens — Vins AOC (détail joint, 24 cartons)
Total HT 1 237,61 € — Remise 3 % paiement comptant – 37,13 € — Net HT 1 200,48 €
TVA 20 % 240,10 € — Net à payer TTC 1 440,58 €
Réglé en espèces le 05/09/2026 : 1 450,00 € (monnaie rendue 9,42 €)
Pénalités de retard : 3 fois le taux d'intérêt légal — Indemnité forfaitaire pour frais de recouvrement : 40 €
```

### Pièce 5 — Ticket CB Metro du 08/09/2026
```
METRO LYON GERLAND — 08/09/2026 14:12 — CB VISA **** 4471 — SAS LE PETIT ZINC
Montant : 342,18 EUR — Facture 0189-4456 éditée
```

### Pièce 6 — Comptage physique (billetage) du 30/09/2026 au soir, signé Hugo Lemoine
Total billets et pièces : **3 687,00 €** (dont fond de caisse 300,00 €).

## Travail à faire
1. Expliquez pourquoi un solde de caisse créditeur est impossible et quelles en sont les conséquences en cas de contrôle fiscal.
2. Identifiez **toutes** les anomalies du compte 530 de septembre (aidez-vous des pièces 2 à 5).
3. Passez les écritures de correction et recalculez le solde corrigé au 30/09/2026 ; vérifiez que le solde corrigé n'est jamais créditeur.
4. Comparez le solde corrigé au comptage physique et traitez l'écart éventuel.
5. Analysez le paiement de la Cave des Canuts au regard de la réglementation des paiements en espèces, et rédigez le message à Clara.
6. Que pensez-vous de l'« avance extra M. Diallo » ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E05-02_corrige.md)
