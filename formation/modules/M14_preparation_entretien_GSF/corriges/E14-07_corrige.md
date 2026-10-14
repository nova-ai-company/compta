# Corrigé E14-07 — Autolaveuse, accessoires, petit matériel et contrat de maintenance : immobiliser ou passer en charge ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-07](../exercices/E14-07_autolaveuse-immobilisation-maintenance.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Ventilation ligne à ligne
Le **coût d'acquisition** d'une immobilisation comprend le prix d'achat et **tous les coûts directement attribuables** engagés pour mettre le bien en place et en état de fonctionner (PCG art. 213-8). En sont exclus notamment les frais de **formation** du personnel.

| Ligne | HT | Traitement | Justification |
|---|---|---|---|
| Autolaveuse AL-55 | 2 800,00 | **Immobilisation 2154** | Bien durable, utilisé plus d'un exercice, > 500 € HT |
| Batterie lithium supplémentaire | 420,00 | **Immobilisation 2154** (coût de l'autolaveuse) | Accessoire spécifique acquis avec la machine, nécessaire à son usage en continu (rotation des batteries) ; inutilisable sans elle |
| Livraison | 60,00 | **Immobilisation** | Coût directement attribuable (mise en place) |
| Mise en service et réglages | 90,00 | **Immobilisation** | Coût directement attribuable (mise en état de fonctionner) |
| Formation des agents | 120,00 | **Charge 6228** | Exclue du coût d'acquisition (PCG art. 213-8) |
| Kit brosses et disques | 145,00 | **Charge 6063** | Consommables à usure rapide, remplacés régulièrement |
| Éco-participation DEEE | 12,50 | **Immobilisation** | Fait partie du prix d'achat du bien |
| Aspirateur dorsal | 289,00 | **Charge 6063** | Bien de faible valeur (≤ 500 € HT) : tolérance de passage en charge |
| Contrat de maintenance 12 mois | 540,00 | **Charge 6156**, étalée : **CCA** | Service rendu d'octobre 2026 à septembre 2027 |

### Question 2 — Plan d'amortissement
Base amortissable : 3 382,50 € HT (la TVA est récupérable, elle n'entre pas dans le coût). Linéaire 5 ans → 676,50 €/an, 56,375 €/mois. Départ : **mise en service le 21/09** (et non la date de facture du 14/09). En jours (360) : du 21 au 30/09 = **10 jours** ; du 21/09 au 31/12 = 10 + 90 = **100 jours**.

### Question 4 — Dix aspirateurs
La tolérance s'apprécie **par unité** : dix aspirateurs à 289,00 € (2 890,00 € au total) restent en principe en charge, chaque bien étant autonome. **Mais** l'administration exclut la tolérance lorsque les biens constituent un **ensemble** ou un **premier équipement** (par exemple l'équipement initial d'un nouvel établissement ou d'un nouveau marché) : dans ce cas, on immobilise. Et la politique du groupe peut imposer un seuil plus bas ou des règles propres (suivi des actifs par établissement) : on l'applique.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Coût d'entrée 2154 | 2 800,00 + 420,00 + 60,00 + 90,00 + 12,50 | **3 382,50 €** |
| TVA sur immobilisation (44562) | 3 382,50 × 20 % | 676,50 € |
| Charges (6228 + 6063 + 6156) | 120,00 + 145,00 + 289,00 + 540,00 | 1 094,00 € |
| TVA sur ABS (44566) | 1 094,00 × 20 % | 218,80 € |
| Total TVA | 676,50 + 218,80 | 895,30 € ✓ |
| Dette 404MNE (immo) | 3 382,50 + 676,50 | 4 059,00 € |
| Dette 401MNE (charges) | 1 094,00 + 218,80 | 1 312,80 € |
| Total facture | 4 059,00 + 1 312,80 | 5 371,80 € ✓ |
| Annuité | 3 382,50 / 5 | 676,50 € |
| Dotation septembre | 676,50 × 10 / 360 | **18,79 €** |
| Dotation mensuelle (oct., nov.) | 676,50 / 12 | **56,38 €** |
| Dotation 2026 | 676,50 × 100 / 360 | **187,92 €** |
| Dotation décembre (ajustement d'arrondi) | 187,92 − 18,79 − 56,38 − 56,38 | 56,37 € |
| CCA maintenance au 30/09 | 540,00 × 12/12 (rien de consommé) | 540,00 € |
| CCA au 31/10 | 540,00 × 11/12 | 495,00 € |

**Début du plan :**

| Période | Base | Dotation | Cumul | VNC |
|---|---|---|---|---|
| 2026 (21/09-31/12) | 3 382,50 | 187,92 | 187,92 | 3 194,58 |
| 2027 à 2030 | 3 382,50 | 676,50 / an | … | … |
| 2031 (01/01-20/09) | 3 382,50 | 488,58 | 3 382,50 | 0,00 |

(Contrôle : 187,92 + 4 × 676,50 + 488,58 = 3 382,50 ✓.)

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 14/09/2026 | AC | 2154 | Matériel industriel | MNE MN-4377 autolaveuse AL-55 n° AL55-26-01937 (ANT) | 3 382,50 | |
| 14/09/2026 | AC | 44562 | TVA déductible sur immobilisations | MNE MN-4377 TVA immo | 676,50 | |
| 14/09/2026 | AC | 404MNE | Fournisseur d'immobilisations Machines Nett' | MNE MN-4377 part immobilisation | | 4 059,00 |
| 14/09/2026 | AC | 6228 | Divers – formation externe | MNE MN-4377 formation 4 agents | 120,00 | |
| 14/09/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | MNE MN-4377 brosses + aspirateur dorsal | 434,00 | |
| 14/09/2026 | AC | 6156 | Maintenance | MNE MN-4377 contrat maintenance 10/2026-09/2027 | 540,00 | |
| 14/09/2026 | AC | 44566 | TVA déductible sur ABS | MNE MN-4377 TVA ABS | 218,80 | |
| 14/09/2026 | AC | 401MNE | Fournisseur Machines Nett' | MNE MN-4377 part charges | | 1 312,80 |
| 30/09/2026 | OD | 486 | Charges constatées d'avance | CCA maintenance AL-55 12/12 | 540,00 | |
| 30/09/2026 | OD | 6156 | Maintenance | CCA maintenance AL-55 12/12 | | 540,00 |
| 30/09/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotation 09/2026 AL-55 (10 j) | 18,79 | |
| 30/09/2026 | OD | 28154 | Amortissements du matériel industriel | Dotation 09/2026 AL-55 (10 j) | | 18,79 |
| 01/10/2026 | OD | 6156 | Maintenance | Extourne CCA maintenance AL-55 | 540,00 | |
| 01/10/2026 | OD | 486 | Charges constatées d'avance | Extourne CCA maintenance AL-55 | | 540,00 |
| 31/10/2026 | OD | 486 | Charges constatées d'avance | CCA maintenance AL-55 11/12 | 495,00 | |
| 31/10/2026 | OD | 6156 | Maintenance | CCA maintenance AL-55 11/12 | | 495,00 |
| 31/10/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotation 10/2026 AL-55 | 56,38 | |
| 31/10/2026 | OD | 28154 | Amortissements du matériel industriel | Dotation 10/2026 AL-55 | | 56,38 |
| | | | | **Totaux** | **7 021,97** | **7 021,97** |

> Une seule écriture fournisseur (tout en 404 ou tout en 401) est aussi admise par beaucoup d'ERP ; l'important est que la **ligne d'immobilisation** alimente le fichier des immobilisations (fiche : n° de série, établissement d'Antibes, date de mise en service, durée, méthode).

## 4. Points d'attention / pièges

- **Date de départ** : mise en service (21/09), pas la date de facture ni la date de paiement.
- **Formation** : erreur fréquente que de l'immobiliser parce qu'elle figure sur la même facture.
- **Contrat de maintenance** : la facture de septembre ne concerne pas septembre. En clôture mensuelle, sans CCA, septembre porterait 540,00 € de charge à tort, et les onze mois suivants zéro.
- **TVA** : 44562 pour la partie immobilisée (elle se déclare sur la ligne « biens constituant des immobilisations » de la CA3), 44566 pour le reste.
- **Fiscalement**, le matériel industriel neuf de plus de 3 ans peut être amorti en **dégressif** (coefficient 1,75 pour 5 ans, taux 35 %, départ au premier jour du mois d'acquisition : 3 382,50 × 35 % × 4/12 = 394,63 € pour 2026). La méthode est fixée par le groupe ; l'aide-comptable applique la politique, elle ne choisit pas machine par machine.
- **Composants** : pour une machine de ce prix, pas d'approche par composants (la batterie supplémentaire suit la durée de la machine). Pour une batterie de remplacement achetée dans trois ans, la question se reposerait (charge d'entretien ou composant).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse d'entretien (question 5), environ une minute :**
> « Je pose trois questions. Un : est-ce un bien que l'entreprise va utiliser plus d'un an et qu'elle contrôle ? Si c'est un consommable, des brosses, des disques, c'est une charge. Deux : quelle est sa valeur unitaire ? En dessous de 500 € HT, on peut le passer en charge, sauf s'il fait partie d'un ensemble ou d'un premier équipement, et sauf règle plus stricte du groupe. Trois : qu'est-ce qui entre dans le coût ? Le prix, la livraison, l'installation, la mise en service, l'éco-participation ; pas la formation ni la maintenance, qui est une charge étalée sur la durée du contrat. Puis je crée la fiche d'immobilisation avec la date de mise en service, et je vérifie que la dotation part bien dans la clôture mensuelle. »

**Message à l'établissement d'Antibes :** « La facture MN-4377 a été ventilée : l'autolaveuse (avec batterie, livraison, mise en service) est immobilisée et amortie sur 5 ans à compter du 21/09 ; brosses et aspirateur en charges ; la maintenance est étalée sur 12 mois. Merci de nous envoyer systématiquement le PV de mise en service des machines et de reporter le n° de série dans le BR. »

**Contrôle mensuel** : rapprochement fichier des immobilisations / balance (2154, 28154) ; revue des comptes 6063 et 6156 au-dessus de 500 € par ligne pour détecter des immobilisations passées en charge.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG art. 211-1 (définition des actifs), 212-1 et suivants, 213-8 (coût d'acquisition, frais exclus), 214-13 (amortissement à partir de la mise en service).
- CGI art. 39-1-2° (amortissements) et 39 A (amortissement dégressif) ; BOFiP BOI-BIC-CHG-20-30-10 : tolérance pour les biens de faible valeur (*référence et seuil à vérifier*).
- PCG : comptes 2154, 28154, 404, 44562, 486, 6156, 6811.
