# E11-02 — Studio Pixel : l'appel et la libération du solde du capital
**Client :** C25 — Studio Pixel SAS | **Difficulté :** ★☆☆ | **Durée estimée :** 30 min | **Thèmes :** appel du capital non appelé, 109 / 4562 / 1012 / 1013, contrôle d'une pré-comptabilisation OCR, régularisation de TVA collectée à tort, libération par compensation, conséquences fiscales de la libération intégrale

**Corner case :** oui — un versement d'associé enregistré comme une vente (avec TVA collectée déjà déclarée).

## La mise en situation

Suite de l'exercice E11-01. Lundi 12 octobre 2026, en révisant les comptes de tiers de Studio Pixel au 30/09/2026, vous constatez que le compte **109 « Capital souscrit non appelé » présente toujours un solde débiteur de 2 000 €**, alors que Sarah Cohen vous assure que « le capital a été complété en juin ».

Léo Martin, par mail :

> « Oui, j'ai fait la décision en juin comme vous me l'aviez conseillé, et on a viré chacun 1 000 €. D'ailleurs, puisque la société me doit 2 230,80 € sur mon compte courant, je n'aurais pas pu simplement "compenser" au lieu de virer de l'argent qui va ressortir ? Et maintenant que le capital est complet, on peut mettre des intérêts sur mon compte courant ? »

## Les pièces

**Pièce 1 — Décision du président**

```
STUDIO PIXEL — SAS au capital de 10 000 € — RCS Lyon 952 777 888
DÉCISION DU PRÉSIDENT DU 02/06/2026
Le Président,
- vu l'article 7 des statuts,
- constatant que le capital social de 10 000 € n'est libéré qu'à hauteur de 8 000 €,
décide d'appeler le solde des apports en numéraire, soit 2 000 € :
   M. Léo MARTIN : 100 actions × 10 € = 1 000 €
   Mme Sarah COHEN : 100 actions × 10 € = 1 000 €
Les fonds devront être versés au plus tard le 20/06/2026 sur le compte bancaire de la société.
La présente décision est notifiée à chaque actionnaire par lettre recommandée avec AR
expédiée ce jour.
Fait à Lyon, le 02/06/2026 — Léo MARTIN, Président
```

**Pièce 2 — Relevé bancaire (extrait de juin 2026)**

```
Banque Rhodanienne — compte n° ...4471 — STUDIO PIXEL SAS
15/06/2026  VIR M LEO MARTIN  LIB: SOLDE CAPITAL PIXEL                  + 1 000,00
15/06/2026  VIR MME COHEN SARAH  LIB: PIXEL                             + 1 000,00
```

**Pièce 3 — Écritures générées par l'outil de pré-comptabilisation (validées par Sarah en juin)**

```
15/06/2026  BQ  512    Banque                          1 000,00
                4551   Compte courant L. Martin                   1 000,00
            Libellé : VIR M LEO MARTIN SOLDE CAPITAL PIXEL

15/06/2026  BQ  512    Banque                          1 000,00
                706    Prestations de services                      833,33
                44571  TVA collectée                                166,67
            Libellé : VIR MME COHEN SARAH PIXEL
            (règle automatique : « VIR … PIXEL » = encaissement client)
```

**Pièce 4 — Déclaration de TVA de juin 2026 (CA3 déposée le 21/07/2026, extrait)**

```
Ligne 0979 / base prestations de services : inclut 833,33 € (encaissement du 15/06)
TVA brute due : inclut 166,67 €
```

**Pièce 5 — Extrait de la balance au 30/09/2026 (comptes de capitaux)**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1011 | Capital souscrit – non appelé | | 2 000,00 |
| 1013 | Capital souscrit – appelé versé | | 8 000,00 |
| 109 | Actionnaires : capital souscrit non appelé | 2 000,00 | |
| 4551 | Compte courant L. Martin | | 3 230,80 |
| 4552 | Compte courant S. Cohen | | 235,20 |

## Travail à faire

1. Analysez les anomalies de la pièce 3 et leur incidence (résultat, TVA, bilan).
2. Passez les écritures de l'appel (02/06/2026) et de la libération (15/06/2026), puis les écritures de correction des enregistrements erronés (datées du 30/09/2026). Comment régularisez-vous la TVA ?
3. Présentez les comptes de capital tels qu'ils apparaîtront au 31/12/2026.
4. Répondez à Léo sur la **compensation** avec son compte courant.
5. Répondez à Léo sur les **intérêts de compte courant** et expliquez ce que change la libération intégrale du capital sur le plan fiscal.
6. Que se serait-il passé si Sarah n'avait pas versé les 1 000 € à l'échéance ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E11-02_corrige.md)
