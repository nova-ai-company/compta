# E14-02 — Prestation ponctuelle et révision de prix rétroactive par indice : facture complémentaire (Aéroport Côte d'Azur Services)
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Nice | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** formule de révision de prix, rattachement à l'exercice / au mois, factures à établir (FAE), extourne, facture complémentaire, travaux supplémentaires sans bon de commande

**Corner case :** oui — l'indice de révision est publié après la période qu'il concerne : trois mois de rappel sont dus mais pas encore facturés à la clôture

> *Cadre de formation : société, clients, indices et personnes fictifs. Les indices utilisés ne sont pas des indices publiés : ils servent uniquement au calcul.*

## La mise en situation

Lundi 05/10/2026, clôture mensuelle de septembre (J+3). Thomas Vidal, contrôleur de gestion de l'établissement de Nice (personnage fictif), vous écrit :

> « Deux sujets pour Aéroport Côte d'Azur Services. 1) La révision annuelle au 1er juillet n'a pas été appliquée : l'indice de juin est sorti le 25 septembre seulement. On a facturé juillet, août et septembre à l'ancien prix. 2) Pour le nettoyage exceptionnel du terminal après le salon du 19 septembre, l'équipe a fait 6 heures de plus que le devis, à la demande du responsable d'exploitation de l'aéroport. Leur service achats nous a envoyé vendredi un bon de commande complémentaire. Est-ce que tout ça peut rentrer dans le chiffre d'affaires de septembre ? Je dois remonter le reporting au groupe jeudi. »

Informations : TVA exigible sur les encaissements (pas d'option pour les débits) ; comptes 411ACAS, 706, 4181 Clients – factures à établir, 44587 Taxes sur le chiffre d'affaires sur factures à établir, 44574 TVA collectée en attente d'encaissement. Les écritures de FAE sont **extournées le 1er jour du mois suivant**.

## Les pièces

**Pièce 1 — Contrat AC-2023-004 (extraits)**
```
Article 5 – Prix : forfait mensuel de 32 600,00 € HT (valeur au 01/07/2025),
établi sur la base de l'indice de référence I0 = 118,4 (indice de juin 2025).
Article 6 – Révision : le prix est révisé chaque 1er juillet selon la formule
   P = P0 × (0,125 + 0,875 × I / I0)
   I = valeur de l'indice du mois de juin de l'année de révision.
   Le coefficient est arrondi à 4 décimales. Le prix révisé s'applique aux
   prestations exécutées à compter du 1er juillet, y compris si l'indice est
   publié postérieurement ; le rappel fait alors l'objet d'une facture
   complémentaire.
Article 7 – Clause de sauvegarde : si la hausse du prix dépasse 5 % sur un an,
   les parties se rencontrent avant toute facturation.
Article 9 – Prestations ponctuelles : sur devis accepté et bon de commande.
   Toute facture doit rappeler le numéro du bon de commande, faute de quoi elle
   est rejetée par le service comptable du client.
```

**Pièce 2 — Publication de l'indice (note interne du siège, 25/09/2026)**
```
Indice de révision « coût propreté » (fictif) – valeur de juin 2026 : 122,7
(juin 2025 : 118,4)
```

**Pièce 3 — Devis D-NIC-2026-118 du 02/09/2026 accepté, bon de commande BC-ACAS-26-0912**
```
Nettoyage exceptionnel du hall d'exposition après le salon du 19/09/2026
Forfait 4 850,00 € HT – TVA 20 % 970,00 € – TTC 5 820,00 €
Bon de commande client : BC-ACAS-26-0912 du 08/09/2026 – 4 850,00 € HT
```

**Pièce 4 — Facture émise le 30/09/2026**
```
GSF RIVIERA SAS – SIREN 999 100 206 – TVA FR48999100206
FACTURE N° FR-2026-09-0471 – 30/09/2026
Client : AÉROPORT CÔTE D'AZUR SERVICES SAS – SIREN 999 200 428 – TVA FR14999200428
Nature : prestation de services – Lieu : hall d'exposition, zone aéroportuaire (adresse fictive), Nice
Réf. commande : BC-ACAS-26-0912
Nettoyage exceptionnel après salon du 19/09/2026   HT 4 850,00   TVA 970,00   TTC 5 820,00
Échéance 30/10/2026 – pénalités 3 x taux légal – indemnité forfaitaire 40 €
```

**Pièce 5 — Feuille d'heures du chef d'équipe (19-20/09/2026) et bon de commande complémentaire**
```
Heures prévues au devis : 120 h — heures réalisées : 126 h
Heures supplémentaires demandées par M. Olivier Bianchi (fictif), responsable d'exploitation ACAS (oral)
Taux horaire contractuel prestations ponctuelles : 38,00 € HT
Bon de commande complémentaire BC-ACAS-26-0987 du 02/10/2026 : 228,00 € HT
« Heures complémentaires nettoyage salon du 19/09 »
```

**Pièce 6 — Factures mensuelles déjà émises (forfait au prix non révisé)**

| Facture | Date | Période | HT | TVA | TTC |
|---|---|---|---|---|---|
| FR-2026-07-0388 | 31/07/2026 | juillet | 32 600,00 | 6 520,00 | 39 120,00 |
| FR-2026-08-0405 | 31/08/2026 | août | 32 600,00 | 6 520,00 | 39 120,00 |
| FR-2026-09-0466 | 30/09/2026 | septembre | 32 600,00 | 6 520,00 | 39 120,00 |

## Travail à faire

1. Calculez le coefficient de révision, le nouveau prix mensuel et le rappel dû pour juillet, août et septembre. La clause de sauvegarde joue-t-elle ?
2. Répondez à Thomas Vidal : le rappel et les heures complémentaires relèvent-ils du chiffre d'affaires de septembre ? Justifiez (principe d'indépendance des exercices, appliqué ici aux clôtures mensuelles).
3. Passez les écritures du 30/09 (y compris la facture FR-2026-09-0471 déjà émise), les extournes du 01/10 et les factures complémentaires émises le 08/10/2026.
4. Rédigez les mentions spécifiques de la facture complémentaire de révision.
5. Que se serait-il passé, comptablement et commercialement, si le bon de commande complémentaire n'avait pas été obtenu ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-02_corrige.md)
