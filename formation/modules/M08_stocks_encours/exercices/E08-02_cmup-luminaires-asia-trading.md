# E08-02 — Coût d'acquisition des importations et CMUP des luminaires d'Asia Trading
**Client :** C19 — Asia Trading | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** coût d'acquisition (prix en USD, commission d'achat, fret, droits de douane, transitaire, transport), frais exclus du coût (stockage, frais financiers, écart de change), fiche de stock au CMUP après chaque entrée, comparaison CMUP de période / FIFO, LIFO interdit, variation de stock 6037

**Corner case :** non

## La mise en situation

Asia Trading SARL importe des luminaires fabriqués en Chine et les revend à des magasins de décoration en France et en Belgique (clôture au 31/12, réel normal, IS). Le stock est tenu en **inventaire intermittent** en comptabilité ; le gérant, Kevin Nguyen, suit les quantités sur un tableur. La méthode de valorisation mentionnée dans l'annexe depuis la création est le **CMUP après chaque entrée**.

Mail de Kevin Nguyen, reçu le 11/01/2027 :

> « Bonjour, je vous envoie ma fiche de stock de la suspension LOTUS, notre best-seller du dernier trimestre. J'ai calculé un coût unitaire de 17,16 € pour l'import d'octobre parce que j'ai tout mis dedans : le stockage, les intérêts du crédit documentaire et même la perte de change. Par contre j'ai enlevé la commission de l'agent et les honoraires du transitaire, ce ne sont pas des marchandises. Au fait, mon ancien comptable en Belgique me parlait du LIFO, ce ne serait pas mieux avec la hausse des prix chinois ? Kevin »

Hélène Ferrand : « Reprenez le coût des deux imports de la LOTUS, refaites la fiche de stock au CMUP et donnez-moi le stock final au 31/12. Je veux aussi, pour la culture de Kevin, la comparaison avec le FIFO et le CMUP trimestriel. L'inventaire physique du 31/12 a été fait : 500 LOTUS en stock, ce qui correspond aux quantités du tableur. »

Informations complémentaires :
- toutes les autres références (hors LOTUS) ont été valorisées par vos soins au CMUP : **182 340,00 €** au 31/12/2026 ;
- le compte **37 Stocks de marchandises** présente un solde de **205 600,00 €** (stock au 31/12/2025) ;
- les factures en USD sont converties au cours du jour de l'opération (date de la facture du fournisseur, qui correspond à la mise à bord) ;
- taux des droits de douane applicable aux luminaires : **on retient 4,7 %** de la valeur en douane (*taux TARIC à vérifier pour chaque nomenclature*) ;
- la valeur en douane est la valeur **CIF** (prix + fret et assurance jusqu'à l'entrée dans l'Union) ; les commissions d'achat n'y sont pas incluses ;
- la TVA à l'importation est autoliquidée sur la CA3 (opération neutre, traitée au module M04).

## Les pièces

**Pièce 1 — Facture du fabricant (import n° 1)**
```
ZHONGSHAN BRIGHT LIGHTING CO., LTD — Guzhen Town, Zhongshan, Guangdong, China
COMMERCIAL INVOICE No. ZBL-2026-1047 — Date: 15/10/2026
Buyer: ASIA TRADING SARL, 60 avenue Berthelot, 69007 Lyon, France — VAT FR 41 838900101
Terms: FOB Shenzhen (Incoterms 2020) — Payment: 100 % by L/C at 45 days B/L
Item LOTUS pendant lamp, ref. LT-450 — 1,200 pcs x USD 14.00 = USD 16,800.00
Vessel: CMA CGM TAGE — B/L dated 15/10/2026 — Port of discharge: Le Havre
```
Cours retenu le 15/10/2026 : 1 EUR = **1,0800 USD**.

**Pièce 2 — Note de commission de l'agent d'achat**
```
SOURCING PARTNERS SHENZHEN LTD — Debit note SP-26-311 — 18/10/2026
Buying commission 3 % on invoice ZBL-2026-1047 (USD 16,800.00)
Amount: EUR 466,67 (converted at 1.0800) — Payment: bank transfer 30 days
```

**Pièce 3 — Facture du transitaire (import n° 1)**
```
RHÔNE TRANSIT LOGISTIQUE SAS — 14 rue de l'Industrie, 69200 Vénissieux — SIREN 444 718 223
FACTURE n° RTL-26-10-0982 du 20/11/2026 — Client : Asia Trading SARL
Dossier : import ZBL-2026-1047 — 1 200 suspensions LOTUS
                                                         HT        TVA
Fret maritime Shenzhen → Le Havre + assurance        1 850,00 €    exonéré (transport international)
Débours : droits de douane (DAU 26FR000LH0458712)      818,06 €    —  (débours)
Honoraires de dédouanement et frais de dossier         280,00 €    56,00 €
Transport routier Le Havre → Lyon (entrepôt client)    640,00 €    exonéré (transport lié à une importation*)
TOTAL                                                3 588,06 €    56,00 €     TTC 3 644,06 €
* sous réserve que les frais soient inclus dans la base de la TVA à l'importation.
Paiement à 30 jours — pénalités de retard : 3 fois le taux d'intérêt légal — indemnité forfaitaire de recouvrement : 40 €
```

**Pièce 4 — Extrait du DAU (import n° 1)**
```
DAU n° 26FR000LH0458712 — date d'acceptation 18/11/2026 — Bureau Le Havre Port
Case 46 Valeur statistique : 17 406 €   |   Case 47 Calcul des taxes :
  A00 Droits de douane — base 17 405,56 € — taux 4,7 % — montant 818,06 €
  B00 TVA import — autoliquidation (mention : « TVA autoliquidée » — n° TVA FR 41 838900101)
```

**Pièce 5 — Import n° 2 (synthèse des documents)**
```
Facture ZBL-2026-1182 du 12/11/2026 — FOB Shenzhen — 1 000 LOTUS x USD 14.50 = USD 14,500.00
Cours retenu le 12/11/2026 : 1 EUR = 1,0500 USD
Commission d'achat Sourcing Partners : 3 % — EUR 414,29
Transitaire Rhône Transit : fret + assurance 1 620,00 € ; droits de douane (DAU, base CIF 15 429,52 €,
taux 4,7 %) 725,19 € ; honoraires dédouanement 280,00 € HT ; transport Le Havre → Lyon 590,00 €
```

**Pièce 6 — Fiche de stock LOTUS du tableur de Kevin (4e trimestre 2026)**
```
Date        Mouvement                           Entrées   Sorties    Stock (qté)
01/10/2026  Stock initial (coût unitaire 18,40 €)                         400
22/11/2026  Réception import n° 1                 1 200                  1 600
26/11/2026  Ventes Maison & Lumière (BL 2611)                 500         1 100
03/12/2026  Ventes Déco Rhône (BL 0312)                       700           400
18/12/2026  Réception import n° 2                 1 000                  1 400
21/12/2026  Ventes Bazar Chic Bruxelles (BL 2112)             900           500

Calcul de Kevin pour l'import n° 1 :
  Prix FOB (16 800 USD / 1,08)                        15 555,56
  Fret + assurance                                     1 850,00
  Droits de douane                                       818,06
  Transport Le Havre → Lyon                              640,00
  Stockage entrepôt oct.-déc. (quote-part LOTUS)       1 200,00
  Intérêts et commission du crédit documentaire          310,00
  Perte de change au paiement du 30/11 (cours 1,0650)    219,09
  TOTAL                                               20 592,71  → 17,16 €/u
```

## Travail à faire

1. Pour chaque élément du calcul de Kevin et pour les éléments qu'il a écartés, indiquez s'il fait partie du coût d'acquisition du stock, et pourquoi.
2. Calculez le coût d'acquisition total et unitaire des imports n° 1 et n° 2.
3. Établissez la fiche de stock de la LOTUS au **CMUP après chaque entrée** (coût unitaire arrondi à 4 décimales, valeurs au centime) et déterminez le stock final au 31/12/2026.
4. Calculez, pour comparaison, le stock final selon le **CMUP du trimestre** et selon le **FIFO**. Commentez.
5. Répondez à Kevin sur le LIFO.
6. Passez l'écriture de variation des stocks de marchandises au 31/12/2026.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E08-02_corrige.md)
