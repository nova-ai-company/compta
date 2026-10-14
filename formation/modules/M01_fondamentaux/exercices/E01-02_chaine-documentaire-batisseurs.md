# E01-02 — Reconstituer la chaîne devis → BC → BL → facture
**Client :** C02 — Bâtisseurs du Sud | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** piste d'audit fiable, rapprochement 3 voies, avoir, remise, frais de livraison

**Corner case :** oui — facture émise avant la livraison d'une partie des marchandises, et réserves sur BL ignorées

## La mise en situation

Révision trimestrielle chez Bâtisseurs du Sud (la tenue est faite en interne par Nadia, comptable à mi-temps). En pointant le compte fournisseur Négoce BTP Lyonnais, vous trouvez une facture de 6 962,04 € saisie le 31/08/2026 et **toujours non payée** au 09/10/2026. Nadia vous explique :

> « Karim m'a dit de ne pas la payer, il trouve qu'elle est trop chère, mais il n'a pas eu le temps de regarder. J'ai tout scanné dans le dossier du chantier Les Acacias. Le fournisseur nous relance, il menace de bloquer notre compte client. »

Hélène Ferrand : « Reconstituez la chaîne complète et chiffrez exactement ce que l'on doit. Préparez la réclamation pour Karim. »

## Les pièces

**Pièce 1 — Devis**
```
NÉGOCE BTP LYONNAIS SAS — Matériaux de gros œuvre
Rue Antoine Primat, 69100 Villeurbanne
SAS au capital de 800 000 € — RCS Lyon 433 210 987 — TVA FR07 433210987

DEVIS N° D-2026-417                               Date : 12/08/2026
Client : BÂTISSEURS DU SUD SAS — ZA des Plaines, 69800 Saint-Priest
Chantier : Résidence Les Acacias, 18 rue des Acacias, 69800 Saint-Priest
Validité : 30 jours

Désignation                                   Qté       PU HT     Montant HT
Parpaing creux 20x20x50 NF                 2 400 u      1,28 €     3 072,00 €
Ciment CEM II/A 42,5 — sac 35 kg             120 sacs   8,90 €     1 068,00 €
Treillis soudé ST25C 2,40 x 6 m               60 pan.   24,50 €     1 470,00 €
                                         Sous-total matériaux      5 610,00 €
Remise client « compte pro » 4 % sur matériaux                    - 224,40 €
Livraison sur chantier camion-grue (forfait unique,
quel que soit le nombre de rotations)                             180,00 €
                                                     Total HT     5 565,60 €
                                                     TVA 20 %     1 113,12 €
                                                    Total TTC     6 678,72 €
Bon pour accord — signé K. Benali le 13/08/2026
```

**Pièce 2 — Bon de commande**
```
BÂTISSEURS DU SUD SAS — ZA des Plaines, 69800 Saint-Priest — SIREN 812 450 776
BON DE COMMANDE N° BC-ACA-0812                      Date : 14/08/2026
Fournisseur : Négoce BTP Lyonnais — réf. devis D-2026-417
Livraison : chantier Les Acacias — semaine 34
2 400 parpaings 20x20x50 — 120 sacs ciment CEM II 35 kg — 60 treillis ST25C
Conditions : selon devis (remise 4 %, livraison forfait 180 € HT)
Signature : K. Benali
```

**Pièce 3 — Bon de livraison n° 1**
```
NÉGOCE BTP LYONNAIS — BON DE LIVRAISON N° BL-77310       Date : 21/08/2026
Chantier Les Acacias — Commande client BC-ACA-0812
Parpaing creux 20x20x50 ........ 2 400 u
Ciment CEM II 35 kg ............   120 sacs
Treillis soudé ST25C ...........    40 pan. (reliquat 20 : rupture de stock)
RÉSERVES : 60 parpaings cassés au déchargement (palette renversée par
le grutier) — repris par le chauffeur.
Signature chauffeur : J.P.   Signature réception : M. Okoye (chef de chantier)
```

**Pièce 4 — Bon de livraison n° 2**
```
NÉGOCE BTP LYONNAIS — BON DE LIVRAISON N° BL-77802       Date : 02/09/2026
Chantier Les Acacias — Commande client BC-ACA-0812 — livraison du reliquat
Treillis soudé ST25C ...........    20 pan.
Signature réception : M. Okoye
```

**Pièce 5 — Facture**
```
NÉGOCE BTP LYONNAIS SAS — Rue Antoine Primat, 69100 Villeurbanne
SAS au capital de 800 000 € — RCS Lyon 433 210 987 — TVA FR07 433210987

FACTURE N° F-2026-08-2291                           Date : 31/08/2026
Client : BÂTISSEURS DU SUD SAS — SIREN 812 450 776
         ZA des Plaines, 69800 Saint-Priest
Votre commande : BC-ACA-0812 — Nature : livraison de biens

Désignation                                   Qté       PU HT     Montant HT
Parpaing creux 20x20x50 NF                 2 400 u      1,28 €     3 072,00 €
Ciment CEM II/A 42,5 — sac 35 kg             120 sacs   8,90 €     1 068,00 €
Treillis soudé ST25C 2,40 x 6 m               60 pan.   24,50 €     1 470,00 €
                                         Sous-total matériaux      5 610,00 €
Remise 3 %                                                        - 168,30 €
Livraison camion-grue 21/08                                         180,00 €
Livraison camion-grue (reliquat)                                    180,00 €
                                                     Total HT     5 801,70 €
                                                     TVA 20 %     1 160,34 €
                                                    Total TTC     6 962,04 €
Échéance : 30/09/2026 — Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €. Pas d'escompte.
```

**Pièce 6 — Saisie de Nadia (journal AC)**

| Date | Compte | Libellé | Débit | Crédit |
|---|---|---|---|---|
| 31/08/2026 | 601 | Négoce BTP F-2026-08-2291 | 5 801,70 | |
| 31/08/2026 | 44566 | Négoce BTP F-2026-08-2291 | 1 160,34 | |
| 31/08/2026 | 401NEGO | Négoce BTP F-2026-08-2291 | | 6 962,04 |

## Travail à faire

1. Présentez un tableau de rapprochement **devis / BC / BL / facture**, ligne par ligne, et listez tous les écarts.
2. Calculez le montant que Bâtisseurs du Sud doit réellement (HT, TVA, TTC) et le montant de l'avoir à réclamer, ventilé.
3. Commentez la saisie de Nadia (compte, ventilation) et dites si la facture doit rester en comptabilité en attendant l'avoir.
4. Passez l'écriture de l'avoir reçu le 08/10/2026 (montant conforme à votre calcul) et celle du règlement du solde le 12/10/2026.
5. Rédigez le message de réclamation au fournisseur (à faire signer par Karim Benali).
6. Quel est le défaut de procédure interne révélé par ce dossier ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E01-02_corrige.md)
