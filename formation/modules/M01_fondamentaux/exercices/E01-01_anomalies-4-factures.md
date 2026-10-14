# E01-01 — Quatre factures, combien d'anomalies ?
**Client :** C24 — Menuiserie Bois & Création | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** mentions obligatoires, nouvelles mentions 2026, taux de TVA, facture au nom du gérant, facturation électronique

**Corner case :** oui — une ETI qui envoie encore un PDF par e-mail après le 01/09/2026, et une facture d'outillage au nom personnel du gérant

## La mise en situation

Mercredi 7 octobre 2026, Antoine Girard, gérant de la Menuiserie, dépose sur la plateforme de dématérialisation quatre factures de septembre avec ce message :

> « Bonjour, voici les dernières factures fournisseurs de septembre. La trésorerie est tendue, je voudrais tout payer d'un coup vendredi, vous pouvez me dire si c'est bon ? Pour la scie, je l'ai payée avec ma carte perso, il faudra me la rembourser. Merci. Antoine »

Hélène Ferrand vous transmet le dossier : « Avant tout bon à payer, contrôle complet des quatre pièces. La Menuiserie est sous surveillance de la banque, je ne veux pas une seule TVA déduite à tort. Pour info, la Menuiserie a choisi sa PA de réception en juillet ; son bon de commande n° BC-2026-118 a été envoyé à MRAD le 08/09. »

Rappel : Menuiserie Bois & Création SARL, 9 chemin du Moulin, 69340 Francheville — SIREN 811 010 202 — TVA FR85 811010202 — réel normal, clôture 31/12. La Menuiserie fabrique et pose des menuiseries sur mesure (fenêtres, escaliers, agencements).

## Les pièces

**Pièce 1**
```
BOIS DU LYONNAIS SAS — Négoce de bois et panneaux
14 rue de l'Industrie, 69200 Vénissieux
SAS au capital de 300 000 € — RCS Lyon 521 384 907 — TVA FR51 521384907

FACTURE N° BL-F-2026-04417                    Date : 18/09/2026
Client : MENUISERIE BOIS & CRÉATION
         9 chemin du Moulin, 69340 Francheville
Livraison du 16/09/2026 — BL n° 88120

Désignation                                 Qté     PU HT      Montant HT
Contreplaqué chêne 2500x1220x19 mm           24      86,40 €     2 073,60 €
Chêne massif avivé 27 mm (m3)               0,85  1 980,00 €     1 683,00 €
                                                  Total HT       3 756,60 €
                                                  TVA 20 %         751,32 €
                                                  Total TTC      4 507,92 €

Échéance : 31/10/2026 — Règlement par virement
IBAN FR76 1027 8073 0000 0204 5170 128
```

**Pièce 2**
```
QUINCAILLERIE PRO SARL
5 avenue Berthelot, 69007 Lyon — SARL au capital de 20 000 €
RCS Lyon 448 902 163 — SIREN 448 902 163 — TVA FR17 448902163

FACTURE N° 2026-1187                               Lyon, le 22/09/2026
Client : SARL MENUISERIE BOIS & CRÉATION — SIREN 811 010 202
         9 chemin du Moulin, 69340 Francheville
Nature de l'opération : livraison de biens — livrés le 22/09/2026

Réf.     Désignation                         Qté     PU HT    Montant HT
CH-35    Charnières invisibles 35 mm         200     2,35 €     470,00 €
VIS-4    Vis agglo 4x40 (boîte de 500)        30     8,90 €     267,00 €
COL-D3   Colle vinylique D3 5 kg              12    14,40 €     172,80 €
POI-128  Poignées inox entraxe 128 mm         80     4,20 €     336,00 €
                                              Total HT       1 245,80 €
                                              TVA 20 %         259,16 €
                                              TOTAL TTC      1 504,96 €

Paiement à 30 jours fin de mois, soit le 31/10/2026. Pas d'escompte pour paiement anticipé.
Pénalités de retard : 3 fois le taux d'intérêt légal. Indemnité forfaitaire pour frais
de recouvrement : 40 €.
```

**Pièce 3**
```
OUTILLAGE DIRECT SAS — 112 cours Lafayette, 69003 Lyon
SAS au capital de 50 000 € — RCS Lyon 790 215 448 — TVA FR15 790215448

FACTURE N° OD-26-30951                          Date : 12/09/2026
Client : M. Antoine GIRARD
         22 rue des Farges, 69005 Lyon

Désignation                                 Qté    PU HT     Montant HT
Scie plongeante 1 400 W + coffret             1    690,00 €     690,00 €
Rail de guidage 1,4 m                         2     64,50 €     129,00 €
                                                 Total HT        819,00 €
                                                 TVA 20 %        163,80 €
                                                 Total TTC       982,80 €
Payé ce jour par carte bancaire (Visa **** 4471)
Pénalités de retard : taux BCE + 10 pts. Indemnité forfaitaire : 40 €.
```

**Pièce 4** — reçue par e-mail en PDF le 23/09/2026 (expéditeur : facturation@mrad-materiaux.fr)
```
MATÉRIAUX RHÔNE-ALPES DISTRIBUTION — MRAD SA
Groupe de distribution de matériaux — 2 300 salariés
Siège : 40 boulevard de l'Europe, 69310 Pierre-Bénite
SA au capital de 12 000 000 € — RCS Lyon 351 667 204 — TVA FR39 351667204

FACTURE N° MRAD-0926-558214                    Date : 21/09/2026
Client : MENUISERIE BOIS & CRÉATION — SIREN 811 010 202
         9 chemin du Moulin, 69340 Francheville
Livraison : chantier Résidence Les Charmes, 3 allée des Charmes, 69340 Francheville
Nature de l'opération : livraison de biens

Désignation                                 Qté     PU HT     Montant HT
Panneau MDF hydrofuge 19 mm 2800x2070         40    31,50 €    1 260,00 €
Vernis polyuréthane parquet 5 L               15    42,00 €      630,00 €
                                                  Total HT     1 890,00 €
                                TVA 10 % (travaux de rénovation)  189,00 €
                                                  Total TTC    2 079,00 €

Échéance : 21/10/2026. Pénalités de retard : 3 x taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

## Travail à faire

1. Pour chacune des quatre pièces, dressez la liste **exhaustive** des anomalies (mentions manquantes ou erronées, erreurs de calcul, taux, destinataire, forme de la facture).
2. Pour chaque anomalie, indiquez sa **gravité** : bloque-t-elle la déduction de la TVA ? le paiement ? ou est-ce une simple demande de mise en conformité ?
3. Indiquez, pour chaque pièce, l'action à mener (bon à payer, demande de facture rectificative / avoir, refus) et rédigez la réponse à Antoine Girard.
4. Passez les écritures comptables définitives, une fois les pièces régularisées (hypothèses : la scie est refacturée à la société le 09/10/2026 et Antoine Girard en sera remboursé ; Quincaillerie Pro émet un avoir de rectification de TVA ; MRAD émet via la PA un avoir total puis une nouvelle facture au bon taux).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E01-01_corrige.md)
