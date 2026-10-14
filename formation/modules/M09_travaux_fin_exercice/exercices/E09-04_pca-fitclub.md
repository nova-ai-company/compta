# E09-04 — FitClub : abonnements annuels, packs de coaching et redevance au 31/08/2026
**Client :** C21 — FitClub Villeurbanne SAS | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** PCA sur abonnements (calcul par génération), état logiciel à corriger (TTC, suspensions), PCA à l'avancement (séances non consommées), frais d'inscription, FNP de redevance de franchise

**Corner case :** oui — l'état de PCA du logiciel est en TTC et ignore les suspensions d'abonnement.

## La mise en situation

Vous révisez FitClub Villeurbanne (exercice du 01/09/2025 au 31/08/2026). Romain Faure, président, vous a transféré l'état « Produits différés » exporté de son logiciel de gestion des membres, avec ce commentaire :

> « Le logiciel calcule tout seul, vous n'avez qu'à reprendre le chiffre : 60 645 €. Pour les frais d'inscription, je les mets en CA direct, c'est bon ? Et les packs coaching, c'est encaissé, donc c'est du CA, non ? »

Hélène Ferrand vous a laissé un post-it : « Ne reprenez jamais un état logiciel sans le tester. Et pensez à la redevance de franchise d'août. »

Rappels : l'abonnement annuel est vendu **468 € TTC** (TVA 20 %, soit **390 € HT**). Il est payé intégralement à la souscription et court **12 mois à compter du 1er du mois** de début. Les frais d'inscription sont de **49 € TTC** par nouveau membre. La redevance de franchise est de **6 % du CA HT mensuel**, facturée par le franchiseur le 5 du mois suivant.

## Les pièces

**Pièce 1 — État « Produits différés » du logiciel au 31/08/2026**
```
FITMANAGER v8.2 — Club : FitClub Villeurbanne — Édité le 02/09/2026
Abonnements annuels actifs — Montants encaissés non consommés (TTC)
Mois de début   Nb contrats   Mois restants au 31/08/26   Montant différé TTC
09/2025              42                0                      0,00
10/2025              18                1                    702,00
11/2025              15                2                  1 170,00
12/2025               9                3                  1 053,00
01/2026              55                4                  8 580,00
02/2026              24                5                  4 680,00
03/2026              20                6                  4 680,00
04/2026              14                7                  3 822,00
05/2026              12                8                  3 744,00
06/2026              16                9                  5 616,00
07/2026               8               10                  3 120,00
08/2026              22               11                  9 438,00
09/2026 (prévente)   30               12                 14 040,00
TOTAL                                                   60 645,00
NB : les suspensions d'abonnement ne sont pas gérées par ce rapport.
```

**Pièce 2 — Registre des suspensions (tenu sur Excel par l'accueil)**

| Membre | Contrat début | Motif | Suspension | Nouvelle date de fin |
|---|---|---|---|---|
| 6 membres (liste nominative jointe) | 01/2026 | Certificat médical (blessure) | 2 mois (avril-mai 2026) | 28/02/2027 au lieu du 31/12/2026 |

*Les CGV prévoient la prolongation de la durée de l'abonnement en cas de suspension médicale, sans remboursement.*

**Pièce 3 — Packs coaching**
```
Packs « Coaching 10 séances » — 360 € TTC (300 € HT) — validité 12 mois
Packs vendus entre le 01/09/2025 et le 31/08/2026 et encore valides : 40
Séances : 400 vendues — 220 consommées au 31/08/2026 — 180 restantes (45 %)
Historique : moins de 3 % des séances ne sont jamais consommées.
```

**Pièce 4 — Facture du franchiseur (reçue le 05/09/2026)**
```
FITNESS FRANCE FRANCHISE SAS — SIREN 501 222 908 — FR33501222908
Facture n° RD-2026-08-0412 du 05/09/2026
Redevance de franchise — août 2026 — 6 % × CA HT déclaré 61 400,00 €
HT 3 684,00 € — TVA 20 % 736,80 € — TTC 4 420,80 €
Échéance : 20/09/2026
```

**Pièce 5 — Frais d'inscription**
```
Frais d'inscription perçus sur l'exercice : 214 nouveaux membres × 49 € TTC
Contrepartie : création du dossier, badge d'accès, bilan forme initial de 45 min avec un coach
réalisé la première semaine.
```

**Pièce 6 — Extrait de la balance au 31/08/2026 (avant inventaire)**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 7061 | Abonnements | | 512 800,00 |
| 7062 | Frais d'inscription | | 8 740,00 |
| 7063 | Coaching | | 18 600,00 |
| 487 | Produits constatés d'avance (ouverture extournée le 01/09/2025) | | 0,00 |

## Travail à faire
1. Analysez l'état du logiciel : est-il exploitable tel quel ? Recalculez le PCA sur abonnements au 31/08/2026.
2. Calculez le PCA sur les packs coaching.
3. Répondez à Romain sur les frais d'inscription.
4. Traitez la redevance de franchise d'août.
5. Passez les écritures au 31/08/2026 et contrôlez l'équilibre.
6. Proposez une procédure pour fiabiliser le calcul l'an prochain.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E09-04_corrige.md)
