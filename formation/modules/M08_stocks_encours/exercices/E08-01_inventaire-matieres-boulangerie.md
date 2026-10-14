# E08-01 — Inventaire des matières premières de la Boulangerie Dupain et variation de stock
**Client :** C01 — Boulangerie Dupain | **Difficulté :** ★☆☆ | **Durée estimée :** 35 min | **Thèmes :** inventaire physique, contrôle d'une fiche d'inventaire, valorisation HT, produits périmés, produits finis négligeables, variation de stock 6031 / 6032, cut-off (FNP)

**Corner case :** non (exercice de base, mais la fiche du client contient cinq anomalies)

## La mise en situation

Lundi 4 janvier 2027, 14 h 20. Marc Dupain, gérant de la Boulangerie Dupain SARL (clôture au 31/12, réel simplifié, IS), a déposé sa boîte à chaussures de décembre au cabinet. Sur le dessus, une feuille manuscrite agrafée et un post-it :

> « Voilà mon inventaire du 31 au soir, fait avec Julie après la fermeture. Total 13 172,10 €, c'est plus que l'an dernier, ça devrait faire plaisir au banquier ! Le 31 au matin, les Moulins du Lyonnais m'ont livré 20 sacs de T65, je n'ai pas encore la facture. Marc »

Hélène Ferrand vous transmet le dossier : « Contrôlez la fiche ligne par ligne avant de passer quoi que ce soit. Chez Marc, l'inventaire est fait avec beaucoup de bonne volonté et peu de méthode. Je veux les écritures de stock au 31/12/2026 et un contrôle de cohérence avec le ratio matières / CA. »

Informations tirées du dossier :
- balance au 31/12/2026 avant inventaire : **31 Stocks de matières premières = 5 860,00 €** (stock au 31/12/2025) ; **326 Emballages = 1 120,00 €** ; **601 Achats de matières premières = 148 600,00 €** (hors livraison du 31/12) ; CA HT 2026 = **712 400,00 €** ;
- ratio « consommation de matières / CA » de 2025 : 146 900 € / 690 000 € ;
- le stock de produits finis (pains, viennoiseries) n'a jamais été inscrit au bilan : il est négligeable, les invendus du jour étant donnés chaque soir à une association ;
- méthode de valorisation retenue depuis l'origine (et mentionnée dans l'annexe) : **dernier prix d'achat HT**, les matières tournant en moins de deux semaines.

## Les pièces

**Pièce 1 — Fiche d'inventaire manuscrite (retranscrite)**
```
BOULANGERIE DUPAIN — INVENTAIRE AU 31/12/2026 (fait le 31/12 à 20 h, par Marc et Julie)
Feuille n° 1/1

Article                                  Unité          Qté    Prix unit.    Valeur
------------------------------------------------------------------------------------
Farine T65 tradition                     sac 25 kg       48       19,80      950,40
Farine T45 pâtisserie                    sac 25 kg       22       23,50      517,00
Farine de seigle                         sac 25 kg        8       31,20      249,60
Beurre AOP Charentes-Poitou              plaque 2 kg     60       21,40    1 284,00
Beurre AOP (lot DLC 20/12/2026)          plaque 2 kg     10       21,40      214,00
Sucre semoule                            sac 25 kg       14       24,60      344,40
Chocolat de couverture 64 %              carton 5 kg     12       62,90    7 548,00
Œufs frais                               plateau 30      40        7,20      288,00
Levure fraîche                           pain 1 kg       15        4,10       61,50
Poudre d'amandes                         sac 10 kg        6       98,50      591,00
Sacs papier kraft (emballages)           carton 1000     12       38,00      456,00
Boîtes pâtisserie (emballages)           carton 100       9       64,80      583,20
Pains et viennoiseries invendus du 31    —                —         —         85,00
------------------------------------------------------------------------------------
TOTAL                                                                       13 172,10
Signature : M. Dupain
```

**Pièce 2 — Dernières factures d'achat (extraits)**
```
CACAO BARRY DISTRIBUTION — Facture FA-26-11873 du 14/12/2026
  Chocolat couverture noir 64 % — carton 5 kg — 12 cartons x 62,90 € HT = 754,80 € HT — TVA 5,5 %

EMBALL'PRO LYON SAS — SIREN 528 114 307 — Facture 26-4410 du 09/12/2026
  Boîtes pâtisserie kraft 100 u — 10 cartons — PU HT 54,00 € — PU TTC 64,80 €
  Total HT 540,00 € — TVA 20 % 108,00 € — TTC 648,00 €
```

**Pièce 3 — Bon de livraison**
```
LES MOULINS DU LYONNAIS SA — 27 route de Grenoble, 38200 Vienne — SIREN 391 552 840
BON DE LIVRAISON n° BL-26-12-3381 du 31/12/2026 — 7 h 15
Client : Boulangerie Dupain, 12 rue de la Charité, 69002 Lyon
Farine T65 Tradition française — sac 25 kg — 20 sacs
Prix contractuel 2026 : 19,80 € HT le sac — TVA 5,5 %
Facture mensuelle à suivre. Reçu conforme : M. Dupain
```

**Pièce 4 — Bon d'enlèvement de l'association**
```
RESTOS SOLIDAIRES PRESQU'ÎLE — Bon de collecte du 31/12/2026, 20 h 30
Collecte des invendus du jour (pains, viennoiseries) — Boulangerie Dupain
Signature du bénévole : J.-P. R.
```

**Pièce 5 — Note de Julie Dupain (trouvée dans la boîte)**
```
Marc, les 10 plaques de beurre du lot du 20/12 sont périmées, je les ai mises de côté
dans la chambre froide, on les jette lundi (le fournisseur ne les reprend pas). J.
```

## Travail à faire

1. Contrôlez la fiche d'inventaire ligne par ligne et listez les anomalies, en indiquant pour chacune le traitement correct.
2. Établissez l'inventaire corrigé au 31/12/2026, en distinguant les matières premières (compte 31) et les emballages (compte 326).
3. Traitez la livraison du 31/12 au matin.
4. Passez les écritures d'inventaire au 31/12/2026 et expliquez le **sens** du solde des comptes 6031 et 6032.
5. Calculez l'incidence des corrections sur le résultat par rapport à la fiche de Marc, et contrôlez la cohérence du ratio consommation de matières / CA avec celui de 2025.
6. Rédigez le message à Marc (il pensait faire plaisir au banquier).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E08-01_corrige.md)
