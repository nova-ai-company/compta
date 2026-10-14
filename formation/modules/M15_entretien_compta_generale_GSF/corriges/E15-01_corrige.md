# Corrigé E15-01 — Test de saisie : un lot de 8 pièces d'achats et de ventes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-01](../exercices/E15-01_test-saisie-huit-pieces.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Pour chaque pièce, posez-vous toujours les mêmes quatre questions, dans cet ordre :

1. **Qui émet la pièce ?** Un fournisseur (→ achat, journal AC) ou GSF Riviera (→ vente, journal VT) ? Un mouvement d'argent déjà réalisé (→ BQ) ?
2. **La pièce est-elle correcte ?** Mentions, calculs (HT × taux = TVA ; HT + TVA = TTC). Une pièce fausse ne se saisit pas.
3. **Quelle nature de dépense ou de recette ?** C'est elle qui donne le compte de classe 6, 7 ou 2.
4. **Quelle TVA ?** Déductible (achat), collectée (vente), autoliquidée (achat à l'étranger), et à quel compte.

### Question 1 — Tableau de décision

| Pièce | Saisir ? | Journal | Pourquoi |
|---|---|---|---|
| 1 — Facture Azur Hygiène | Oui | AC | Achat de fournitures, facture conforme |
| 2 — Avoir Azur Hygiène | Oui | AC | Un avoir reçu est un « achat négatif » : il se saisit dans le même journal que la facture |
| 3 — Facture Clinique des Oliviers | Oui | VT | Vente de prestation émise par GSF Riviera |
| 4 — Facture d'acompte Cabinet Azur Syndic | Oui | BQ | L'acompte est encaissé le jour même : on enregistre l'encaissement (voir ci-dessous) |
| 5 — Facture Müller GmbH | Oui | AC | Achat intracommunautaire : TVA autoliquidée |
| 6 — Facture Équip'Pro | Oui | AC | Une ligne en immobilisation, une ligne en charge |
| 7 — Facture Laverie Industrielle Azur | **Non** | — | Erreur de calcul : 640,00 + 128,00 = 768,00 €, pas 786,00 € |
| 8 — Projet de facture Syndic Promenade | **Pas encore** | (VT après correction) | Mentions obligatoires manquantes ; on corrige avant émission, puis on saisit |

### Question 2 — Pièce 1 : remise et frais de port

- **La remise de 5 %** est une réduction commerciale accordée **sur la facture elle-même**. On ne l'enregistre pas à part : on comptabilise directement le **net commercial** (1 187,50 €). Le compte 609 (rabais, remises et ristournes obtenus) ne sert que lorsque la réduction arrive **plus tard**, sur un avoir séparé.
- **Les frais de port** sont un coût accessoire d'achat. On peut les mettre en **6241 Transports sur achats** (choix retenu ici, plus lisible) ou les ajouter au 6063 avec les produits. Les deux sont acceptés ; l'important est d'appliquer **la règle du plan de comptes de l'entreprise** — au test, dites-le.
- La TVA (246,50 €) va en **44566** : c'est de la TVA déductible sur un achat de biens courants.

### Pièce 2 — Avoir

L'avoir **annule une partie de la facture** : on passe l'écriture **inverse** de la facture. Le fournisseur 401 est débité (on lui doit moins), la charge 6063 est créditée (on a moins consommé), la TVA déductible 44566 est créditée (on récupère moins de TVA).

### Question 3 — Pièce 3 : l'escompte

- L'**escompte** est une réduction **financière** accordée au client pour un paiement rapide. Pour GSF Riviera, c'est un **coût financier** : on l'enregistre au débit du **665 Escomptes accordés**, et on garde le chiffre d'affaires **brut** (8 400,00 €) au crédit du 706.
- La **TVA se calcule sur le net financier** (8 232,00 €), car c'est le prix réellement payé par le client : 8 232,00 × 20 % = 1 646,40 €.
- Comme il s'agit d'une **prestation de services** sans option pour les débits, la TVA n'est due qu'à l'encaissement : on la met en **44574** (en attente), pas en 44571.

### Pièce 4 — Facture d'acompte

L'acompte est versé **avant** la prestation (prévue en novembre). Ce n'est pas encore un chiffre d'affaires : on crédite **4191 Clients – avances et acomptes reçus** (une dette envers le client tant que la prestation n'est pas faite). Pour une **prestation de services**, la TVA devient exigible **à l'encaissement** de l'acompte : comme le virement est reçu le 08/10, la TVA (300,00 €) va directement en **44571**. Lors de la facture finale de novembre, on soldera le 4191.

### Question 4 — Pièce 5 : l'autoliquidation

Le fournisseur allemand facture **hors taxe** : c'est **GSF Riviera, l'acheteur**, qui doit calculer et déclarer la TVA française (on dit qu'elle « s'autoliquide »). Elle passe deux fois dans la même écriture :
- au **crédit du 4452** TVA due intracommunautaire (GSF Riviera la doit au Trésor) ;
- au **débit du 445662** TVA déductible intracommunautaire (GSF Riviera la récupère aussitôt).

Résultat : **aucun coût de TVA**, mais l'opération doit apparaître sur la CA3 (base 2 000,00 € en acquisitions intracommunautaires). Le fournisseur est crédité du montant **réellement à payer** : 2 000,00 €.

### Question 5 — Pièce 6 : immobilisation ou charge

| Ligne | Montant HT | Seuil 500 € HT | Durée > 1 an | Traitement |
|---|---|---|---|---|
| Autolaveuse AL-75 | 4 800,00 | au-dessus | oui (5 ans) | **Immobilisation** 2154, TVA en 44562 |
| 6 kits seaux + balais | 6 × 30,00 = 180,00 (30,00 par bien) | en dessous | — | **Charge** 6063, TVA en 44566 |

Le seuil s'apprécie **par bien** (30,00 € par kit), pas sur le total de la ligne. Comme la facture porte sur une immobilisation, le fournisseur va en **404 Fournisseurs d'immobilisations** (certains plans de comptes gardent le 401 : suivez la règle interne).

### Question 6 — Anomalies des pièces 7 et 8

- **Pièce 7** : 640,00 × 20 % = 128,00 € (juste) mais 640,00 + 128,00 = **768,00 €** et non 786,00 € (chiffres inversés). On **ne saisit pas** : on refuse la facture via la PA (motif : erreur de montant TTC) et on demande au fournisseur une facture corrigée. On ne « corrige » jamais soi-même une facture fournisseur.
- **Pièce 8** : le projet de facture n'indique ni le **SIREN du client** ni la **nature de l'opération** (prestation de services), deux mentions de la réforme de la facturation électronique (*date d'application à l'émetteur à vérifier selon sa taille*). Il manque aussi le n° de TVA intracommunautaire du client et la date ou la période de la prestation, l'échéance, les pénalités de retard et l'indemnité de 40 €. On fait **corriger le projet avant émission**. La remise de 10 % est accordée sur la facture : on comptabilise le **net** (1 080,00 €). Une fois la facture corrigée et émise le 12/10, on la saisit (écriture ci-dessous).

## 2. Calculs (détaillés, chaque montant justifié)

| Pièce | Calcul | Résultat |
|---|---|---|
| 1 | 1 250,00 × 95 % = 1 187,50 ; + 45,00 = 1 232,50 HT ; × 20 % = 246,50 ; TTC 1 479,00 | conforme |
| 2 | 120,00 × 20 % = 24,00 ; TTC 144,00 | conforme |
| 3 | 8 400,00 × 2 % = 168,00 ; net 8 232,00 ; × 20 % = 1 646,40 ; TTC 9 878,40 | conforme |
| 4 | 5 000,00 × 30 % = 1 500,00 ; × 20 % = 300,00 ; TTC 1 800,00 | conforme |
| 5 | TVA autoliquidée : 2 000,00 × 20 % = 400,00 | à calculer par GSF Riviera |
| 6 | Immobilisation : 4 800,00 × 20 % = 960,00 ; charge : 180,00 × 20 % = 36,00 ; total TVA 996,00 ; TTC 5 976,00 | conforme |
| 7 | 640,00 + 128,00 = 768,00 ≠ 786,00 | **erreur → non saisie** |
| 8 | 1 200,00 × 90 % = 1 080,00 ; × 20 % = 216,00 ; TTC 1 296,00 | calculs justes, mentions manquantes |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | Azur Hygiène F26-1214 produits (net de remise) | 1 187,50 | |
| 01/10/2026 | AC | 6241 | Transports sur achats | Azur Hygiène F26-1214 frais de port | 45,00 | |
| 01/10/2026 | AC | 44566 | TVA déductible sur autres biens et services | Azur Hygiène F26-1214 TVA 20 % | 246,50 | |
| 01/10/2026 | AC | 401AZH | Fournisseur Azur Hygiène Distribution | Azur Hygiène F26-1214 | | 1 479,00 |
| 05/10/2026 | AC | 401AZH | Fournisseur Azur Hygiène Distribution | Azur Hygiène avoir AV-0431 sur F26-1214 | 144,00 | |
| 05/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | Azur Hygiène AV-0431 retour 10 bidons | | 120,00 |
| 05/10/2026 | AC | 44566 | TVA déductible sur autres biens et services | Azur Hygiène AV-0431 TVA 20 % | | 24,00 |
| 06/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | Müller GmbH 2026-4471 disques et brosses | 2 000,00 | |
| 06/10/2026 | AC | 445662 | TVA déductible intracommunautaire | Müller GmbH 2026-4471 TVA autoliquidée 20 % | 400,00 | |
| 06/10/2026 | AC | 4452 | TVA due intracommunautaire | Müller GmbH 2026-4471 TVA autoliquidée 20 % | | 400,00 |
| 06/10/2026 | AC | 401MUL | Fournisseur Reinigungstechnik Müller | Müller GmbH 2026-4471 | | 2 000,00 |
| 07/10/2026 | VT | 411CLO | Client Clinique des Oliviers | Clinique des Oliviers FV-2026-1003 | 9 878,40 | |
| 07/10/2026 | VT | 665 | Escomptes accordés | Clinique des Oliviers FV-2026-1003 escompte 2 % | 168,00 | |
| 07/10/2026 | VT | 706 | Prestations de services | Clinique des Oliviers FV-2026-1003 nettoyage 09/2026 | | 8 400,00 |
| 07/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | Clinique des Oliviers FV-2026-1003 TVA 20 % | | 1 646,40 |
| 08/10/2026 | BQ | 512 | Banque | Cabinet Azur Syndic acompte FA-2026-0017 | 1 800,00 | |
| 08/10/2026 | BQ | 4191 | Clients – avances et acomptes reçus | Cabinet Azur Syndic acompte 30 % devis D-2026-0288 | | 1 500,00 |
| 08/10/2026 | BQ | 44571 | TVA collectée | Cabinet Azur Syndic acompte TVA 20 % encaissée | | 300,00 |
| 09/10/2026 | AC | 2154 | Matériel industriel | Équip'Pro EP-0977 autolaveuse AL-75 | 4 800,00 | |
| 09/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | Équip'Pro EP-0977 6 kits seaux et balais | 180,00 | |
| 09/10/2026 | AC | 44562 | TVA déductible sur immobilisations | Équip'Pro EP-0977 TVA sur autolaveuse | 960,00 | |
| 09/10/2026 | AC | 44566 | TVA déductible sur autres biens et services | Équip'Pro EP-0977 TVA sur kits | 36,00 | |
| 09/10/2026 | AC | 404EQP | Fournisseur d'immobilisations Équip'Pro Riviera | Équip'Pro EP-0977 | | 5 976,00 |
| 12/10/2026 | VT | 411SPG | Client Syndic Promenade Gestion | Syndic Promenade FV-2026-1009 (après correction) | 1 296,00 | |
| 12/10/2026 | VT | 706 | Prestations de services | Syndic Promenade FV-2026-1009 vitrerie (net de remise) | | 1 080,00 |
| 12/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | Syndic Promenade FV-2026-1009 TVA 20 % | | 216,00 |
| | | | | **Totaux** | **23 141,40** | **23 141,40** |

**Pourquoi débit / crédit ?** Repère simple : ce que l'entreprise **reçoit** ou **consomme** (charge, immobilisation, TVA récupérable, argent sur le compte) va au **débit** ; ce qu'elle **doit** ou **gagne** (dette fournisseur, TVA due, chiffre d'affaires) va au **crédit**. Le client 411 est au débit : il doit de l'argent à GSF Riviera.

## 4. Points d'attention / pièges

- **Remise sur facture ≠ avoir ultérieur** : on ne passe pas de 609 quand la remise figure déjà sur la facture.
- **Escompte** : chiffre d'affaires **brut** au 706, escompte en **665**, TVA sur le **net**. Erreur fréquente : calculer la TVA sur 8 400,00 €.
- **Autoliquidation** : la TVA n'est **pas** ajoutée à la dette fournisseur (le fournisseur allemand ne réclame que 2 000,00 €).
- **Acompte** : jamais en 706 tant que la prestation n'est pas réalisée.
- **Seuil d'immobilisation** : apprécié **bien par bien**, sur le HT.
- **Facture fausse** (pièce 7) : on ne la modifie pas, on la refuse et on en demande une autre.
- **TVA des prestations** : en 44574 à la facturation (régime des encaissements), pas en 44571.

## 5. Ce que le recruteur attend / ce qu'un senior ferait en plus

- **Annoncer sa méthode** à voix haute (« je contrôle d'abord les calculs, ensuite je choisis les comptes ») : c'est ce que le chef comptable veut entendre.
- Signaler que la pièce 6 déclenche une **fiche d'immobilisation** (date de mise en service, durée de 5 ans, amortissement linéaire) et que la pièce 4 sera **soldée** à la facture finale de novembre (411 crédité de l'acompte TTC, 4191 débité).
- Proposer un **message au fournisseur** de la pièce 7 : « Bonjour, votre facture LIA-5520 du 09/10/2026 présente un total TTC de 786,00 € alors que HT 640,00 € + TVA 128,00 € = 768,00 €. Nous l'avons refusée sur la plateforme ; merci de nous transmettre une facture corrigée. Cordialement. »
- Pour la pièce 8, prévenir l'établissement : utiliser le **modèle de facture** de l'ERP, qui reprend automatiquement les mentions obligatoires.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 2154, 404, 401, 411, 4191, 4452, 44562, 44566, 445662, 44571, 44574, 6063, 6241, 609, 665, 706 ; règles de comptabilisation des réductions sur achats et ventes.
- CGI art. 256 bis (acquisitions intracommunautaires), art. 269 (exigibilité de la TVA : encaissement pour les prestations de services, y compris les acomptes), art. 271 (droit à déduction).
- Code de commerce art. L. 441-9 (mentions obligatoires des factures).
- CGI art. 289 et 289 bis (facturation électronique) — *calendrier et mentions à vérifier selon les textes en vigueur*.
