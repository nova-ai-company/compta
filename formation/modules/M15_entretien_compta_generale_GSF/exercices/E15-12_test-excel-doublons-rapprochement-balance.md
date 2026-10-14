# E15-12 — Test Excel : doublons, totaux par établissement et rapprochement avec la balance fournisseurs
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissements de Nice, Antibes et Cannes | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** export de factures fournisseurs, détection de doublons (NB.SI / NB.SI.ENS), totaux par établissement (SOMME.SI.ENS), rapprochement avec la balance (RECHERCHEX / RECHERCHEV), tableau croisé dynamique, écritures de correction

**Corner case :** oui — un doublon « déguisé » (même facture, numéro saisi sans tirets) échappe à la formule NB.SI ; et des factures de même montant ne sont pas forcément des doublons

> *Cadre de formation : le groupe GSF est réel, mais **GSF Riviera SAS, les fournisseurs, les personnes et tous les montants sont fictifs**.*

## La mise en situation

Deuxième partie de votre entretien. Laurent Vidal, chef comptable (personnage fictif), ouvre un fichier Excel sur l'ordinateur de la salle :

> « Ici, on vit dans Excel. Voici l'export de l'outil de dématérialisation : les 25 factures fournisseurs reçues en octobre par les trois établissements. Et à côté, la balance des fournisseurs sortie de la compta. Vous avez 40 minutes. Je veux les **formules exactes** que vous tapez, pas seulement les résultats. Excel est en français, séparateur point-virgule. »

Le fichier contient deux onglets :
- **Export** : en-têtes en ligne 1, données en lignes 2 à 26 (colonnes A à H).
- **Balance** : en-têtes en ligne 1, données en lignes 2 à 6 (colonne A = code tiers, B = nom, C = total des crédits d'octobre, c'est-à-dire les factures saisies en comptabilité ce mois-ci).

On suppose qu'**aucune** de ces factures n'a été payée en octobre et que la balance ne contient **que** les factures d'octobre.

## Les pièces

**Pièce 1 — Onglet « Export » (factures reçues en octobre 2026, montants en €)**

| Ligne Excel | A — Établissement | B — Fournisseur | C — Code tiers | D — N° facture | E — Date | F — HT | G — TVA | H — TTC |
|---|---|---|---|---|---|---|---|---|
| 2 | Nice | Hygiène Pro Méditerranée | 401HPM | HPM-26-10398 | 02/10/2026 | 1 840,00 | 368,00 | 2 208,00 |
| 3 | Antibes | Azur Consommables Sanitaires | 401ACS | ACS-7712 | 02/10/2026 | 965,50 | 193,10 | 1 158,60 |
| 4 | Cannes | Intérim Riviera | 401IRV | IR-2026-1104 | 05/10/2026 | 3 420,00 | 684,00 | 4 104,00 |
| 5 | Nice | Textiles Pro Sud | 401TPS | TPS-0926-118 | 05/10/2026 | 612,00 | 122,40 | 734,40 |
| 6 | Nice | Hygiène Pro Méditerranée | 401HPM | HPM-26-10412 | 06/10/2026 | 2 275,00 | 455,00 | 2 730,00 |
| 7 | Antibes | Maintenance Nettoyage Côte | 401MNC | MNC-3381 | 07/10/2026 | 1 180,00 | 236,00 | 1 416,00 |
| 8 | Cannes | Azur Consommables Sanitaires | 401ACS | ACS-7740 | 08/10/2026 | 742,30 | 148,46 | 890,76 |
| 9 | Nice | Intérim Riviera | 401IRV | IR-2026-1121 | 09/10/2026 | 5 130,00 | 1 026,00 | 6 156,00 |
| 10 | Antibes | Hygiène Pro Méditerranée | 401HPM | HPM-26-10455 | 09/10/2026 | 1 490,00 | 298,00 | 1 788,00 |
| 11 | Antibes | Azur Consommables Sanitaires | 401ACS | ACS-7712 | 09/10/2026 | 965,50 | 193,10 | 1 158,60 |
| 12 | Cannes | Textiles Pro Sud | 401TPS | TPS-1026-131 | 12/10/2026 | 612,00 | 122,40 | 734,40 |
| 13 | Nice | Maintenance Nettoyage Côte | 401MNC | MNC-3402 | 13/10/2026 | 845,00 | 169,00 | 1 014,00 |
| 14 | Antibes | Intérim Riviera | 401IRV | IR-2026-1139 | 14/10/2026 | 2 565,00 | 513,00 | 3 078,00 |
| 15 | Nice | Hygiène Pro Méditerranée | 401HPM | HPM2610412 | 15/10/2026 | 2 275,00 | 455,00 | 2 730,00 |
| 16 | Cannes | Hygiène Pro Méditerranée | 401HPM | HPM-26-10501 | 16/10/2026 | 980,00 | 196,00 | 1 176,00 |
| 17 | Nice | Sacs et Emballages du Var | 401SEV | SEV-26-0457 | 16/10/2026 | 436,80 | 87,36 | 524,16 |
| 18 | Antibes | Textiles Pro Sud | 401TPS | TPS-1026-140 | 19/10/2026 | 612,00 | 122,40 | 734,40 |
| 19 | Nice | Azur Consommables Sanitaires | 401ACS | ACS-7795 | 20/10/2026 | 1 310,00 | 262,00 | 1 572,00 |
| 20 | Cannes | Intérim Riviera | 401IRV | IR-2026-1150 | 21/10/2026 | 2 850,00 | 570,00 | 3 420,00 |
| 21 | Nice | Textiles Pro Sud | 401TPS | TPS-1026-152 | 22/10/2026 | 612,00 | 122,40 | 734,40 |
| 22 | Antibes | Maintenance Nettoyage Côte | 401MNC | MNC-3430 | 23/10/2026 | 1 625,00 | 325,00 | 1 950,00 |
| 23 | Nice | Intérim Riviera | 401IRV | IR-2026-1163 | 26/10/2026 | 4 275,00 | 855,00 | 5 130,00 |
| 24 | Cannes | Azur Consommables Sanitaires | 401ACS | ACS-7811 | 27/10/2026 | 588,40 | 117,68 | 706,08 |
| 25 | Antibes | Hygiène Pro Méditerranée | 401HPM | HPM-26-10577 | 28/10/2026 | 2 010,00 | 402,00 | 2 412,00 |
| 26 | Nice | Maintenance Nettoyage Côte | 401MNC | MNC-3447 | 29/10/2026 | 920,00 | 184,00 | 1 104,00 |

**Pièce 2 — Onglet « Balance » (comptes 401, total des crédits d'octobre 2026)**

| Ligne Excel | A — Code tiers | B — Nom | C — Crédits octobre |
|---|---|---|---|
| 2 | 401ACS | Azur Consommables Sanitaires | 5 486,04 |
| 3 | 401HPM | Hygiène Pro Méditerranée | 10 314,00 |
| 4 | 401IRV | Intérim Riviera | 21 888,00 |
| 5 | 401MNC | Maintenance Nettoyage Côte | 5 484,00 |
| 6 | 401TPS | Textiles Pro Sud | 2 937,60 |
| | | **Total** | **46 109,64** |

**Pièce 3 — Informations données oralement par le chef comptable**
- Textiles Pro Sud facture une location mensuelle de vêtements de travail de 612,00 € HT **par établissement**.
- « Sacs et Emballages du Var » est un nouveau fournisseur de l'établissement de Nice, référencé en octobre.
- Les achats de consommables, emballages et produits se comptabilisent en 6068 (Autres matières et fournitures) ; TVA déductible en 44566.

## Travail à faire

1. **Doublons** : ajoutez en colonne I une formule qui compte, pour chaque ligne, combien de fois le couple « code tiers + n° de facture » apparaît. Donnez la formule de la cellule I2 et les lignes signalées.
2. **Doublon déguisé** : la formule de la question 1 ne voit pas tout. Proposez une deuxième formule (colonne J) qui repère les factures d'un même fournisseur ayant le **même montant TTC**. Analysez chaque ligne signalée : vrai doublon ou non ?
3. **Totaux par établissement** : donnez la formule SOMME.SI.ENS du total TTC de Nice, puis les totaux TTC de Nice, Antibes et Cannes **avant** et **après** élimination des vrais doublons (ajoutez pour cela une colonne K « Doublon ? » remplie à la main avec « Oui » / « Non »).
4. **Rapprochement avec la balance** : dans un onglet « Rappro », listez les codes tiers en colonne A (y compris 401SEV). Donnez les formules : total export hors doublons par tiers (colonne B), montant de la balance avec **RECHERCHEX** (colonne C), puis la même recherche avec **RECHERCHEV** pour une version d'Excel plus ancienne, et l'écart (colonne D). Présentez le tableau chiffré et expliquez chaque écart.
5. **Écritures** : passez les écritures de correction au 31/10/2026 qui découlent de vos écarts.
6. **TCD** : expliquez en quatre lignes comment vous construiriez un tableau croisé dynamique « total TTC par établissement et par fournisseur », et ce qu'il faut faire avant de le construire.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-12_corrige.md)
