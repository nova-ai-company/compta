# Corrigé E10-10 — La 2072 de la SCI Les Tilleuls : travaux et déficit foncier

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-10](../exercices/E10-10_2072-sci-les-tilleuls.md)

## 1. Analyse

Une SCI à l'IR ne calcule pas un « bénéfice » comptable : elle détermine un **revenu foncier** selon les règles de l'art. 28 et suivants du CGI (encaissements / paiements, pas d'amortissement), puis le **répartit** entre ses associés, qui le reportent sur leur 2044.

Pour les travaux, le critère est simple à énoncer et délicat à appliquer :
- **Déductibles** : entretien, réparation, amélioration (locaux d'habitation) ;
- **Non déductibles** : construction, reconstruction, **agrandissement** (augmentation du volume ou de la surface habitable).

Les **provisions sur charges récupérables** versées par les locataires ne sont pas des recettes ; corrélativement, les charges récupérables ne sont pas déductibles (sauf celles non récupérées au départ d'un locataire).

## 2. Calculs

**1) Travaux**

| Travaux | Montant | Traitement | Motif |
|---|---|---|---|
| Toiture à l'identique | 21 600 | **Déductible** | Réparation/entretien, sans modification du gros œuvre |
| Ravalement (quote-part copro) | 18 400 | **Déductible** | Entretien |
| Chaudière à condensation | 6 800 | **Déductible** | Amélioration (remplacement d'un équipement existant) |
| Salle de bains | 7 300 | **Déductible** | Amélioration / réparation, même surface |
| Combles → chambre de 18 m² | 24 500 | **Non déductible** | **Agrandissement** : création de surface habitable |
| **Total déductible** | **54 100** | | |

**2) Recettes et charges**

| Rubrique | Montant |
|---|---|
| Loyers encaissés | 49 800,00 |
| Régularisation des provisions 2025 à réintégrer (4 200 – 3 560) | 640,00 |
| **Total des recettes** | **50 440,00** |
| Frais de gestion forfaitaires (4 × 20 €) | 80,00 |
| Honoraires de relocation | 650,00 |
| Assurance PNO | 1 260,00 |
| Travaux déductibles | 54 100,00 |
| Taxe foncière hors TEOM récupérée (6 900 – 1 140) | 5 760,00 |
| Provisions de copropriété non récupérables 2026 | 4 100,00 |
| Charges récupérables non récupérées (départ locataire) | 360,00 |
| **Total des charges hors intérêts** | **66 310,00** |
| Intérêts d'emprunt + assurance emprunteur (9 840 + 610) | 10 450,00 |
| **Résultat foncier de la SCI** | **– 26 320,00** |

Non retenus : capital remboursé (14 300 €), charges récupérables refacturées aux locataires (5 880 € encaissés au titre des 6 240 € appelés, et TEOM 1 140 € — ni recette ni charge ; seuls les 360 € non récupérés sont déductibles), combles (24 500 €).

**3-4) Répartition et imputation par associé**

Pour chaque associé, on vérifie la part de déficit due aux intérêts : si sa part de recettes ≥ sa part d'intérêts, tout le déficit provient des « autres charges » et est imputable sur le revenu global (dans la limite de 10 700 €).

| Associé | Quote-part | Recettes | Intérêts | Résultat | Déficit dû aux intérêts | Imputable sur le revenu global | Reportable sur revenus fonciers (10 ans) |
|---|---|---|---|---|---|---|---|
| Paul | 50 % | 25 220,00 | 5 225,00 | – 13 160,00 | 0 | **10 700,00** | **2 460,00** |
| Emma | 25 % | 12 610,00 | 2 612,50 | – 6 580,00 | 0 | **6 580,00** | 0 |
| Julien (usufruitier) | 25 % | 12 610,00 | 2 612,50 | – 6 580,00 | 0 | **6 580,00** | 0 |
| **Total** | 100 % | 50 440,00 | 10 450,00 | **– 26 320,00** | | **23 860,00** | **2 460,00** |

(Recettes 50 440 > intérêts 10 450 au niveau de chacun → aucune fraction « intérêts ».)

**5) Conditions et démembrement**

- **Maintien de la location** des biens jusqu'au **31/12/2029** (31/12 de la 3e année suivant l'imputation, ici 2026) et **conservation des parts** par les associés pendant la même période. À défaut, le déficit imputé sur le revenu global est remis en cause (réintégration l'année de la rupture).
- **Démembrement** : le résultat est attribué à l'**usufruitier** (statuts + règle fiscale), Julien conserve donc sa quote-part du déficit. Attention : la donation de la nue-propriété des parts **avant le 31/12/2029** peut être analysée comme une cession au regard de la condition de conservation des parts — *point à vérifier* (doctrine sur le démembrement des parts de sociétés ayant imputé un déficit foncier). À signaler à Paul et à Julien par écrit.

**6) Combles** : 24 500 € non déductibles des revenus fonciers ; ils s'ajouteront au **prix de revient** du bien pour le calcul de la future plus-value immobilière (travaux de construction/agrandissement), sous réserve des justificatifs.

## 3. Écritures comptables

La SCI à l'IR tient une comptabilité (recommandée par le cabinet) mais les retraitements sont **extra-comptables** (2072). Écriture d'immobilisation des combles dans la comptabilité de la SCI :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/06/2026 | AC | 213500 | Constructions — aménagements | Combles appt 4 — Bâti-Combles | 24 500,00 | |
| 30/06/2026 | AC | 401000 | Fournisseurs | Combles appt 4 — Bâti-Combles | | 24 500,00 |
| 30/06/2026 | AC | 615200 | Entretien et réparations sur biens immobiliers | Réfection toiture — Toitures Lyonnaises | 21 600,00 | |
| 30/06/2026 | AC | 401000 | Fournisseurs | Réfection toiture — Toitures Lyonnaises | | 21 600,00 |
| | | | | **Totaux** | **46 100,00** | **46 100,00** |

## 4. Points d'attention / pièges

- **Agrandissement** : dès qu'on crée de la surface habitable, la dépense sort des charges, même si elle comporte de l'isolation.
- **TEOM** : déductible seulement si elle n'est pas récupérée sur les locataires.
- **Régularisation des provisions de copropriété** : les provisions non récupérables déduites en N doivent être **ajustées** en N+1 sur les charges réelles (ici + 640 € de recettes).
- **Capital remboursé** : jamais déductible.
- **Plafond de 10 700 €** : par foyer fiscal ; si un associé a d'autres revenus fonciers, le déficit s'impute d'abord sur eux.
- Vacance d'un logement : les charges restent déductibles si le bien est **effectivement proposé à la location**.

## 5. Ce qu'un senior ferait en plus

- **Mail type à Paul Garnier** :

> « Bonjour Monsieur Garnier, la SCI dégage un déficit foncier de 26 320 € pour 2026. Votre part (13 160 €) s'impute sur votre revenu global à hauteur de 10 700 € ; le solde de 2 460 € viendra en déduction de vos revenus fonciers des 10 prochaines années. Emma et Julien imputent chacun 6 580 €. Les travaux des combles (24 500 €), qui créent une pièce supplémentaire, ne sont pas déductibles : ils augmenteront le prix de revient de l'appartement en cas de vente. Attention : pour conserver l'avantage, les appartements doivent rester loués et les parts conservées jusqu'au 31/12/2029 ; nous vérifions l'effet de la donation de Julien et revenons vers vous. Bien à vous. »

- Remettre à chaque associé le **relevé de sa quote-part** (recettes, charges, intérêts) pour sa 2044.
- Conserver toutes les factures de travaux (contrôle fréquent sur le déficit foncier) et les PV d'AG de copropriété.
- Ouvrir un **suivi pluriannuel** des déficits reportables par associé.

## 6. Références

- CGI : art. 28 à 31 (revenus fonciers, charges déductibles, travaux), art. 156 I-3° (déficit foncier, plafond de 10 700 €, condition de location sur 3 ans), art. 8 (transparence des sociétés civiles), art. 150 VB (prix de revient des immeubles pour les plus-values).
- BOFiP : série RFPI-BASE (détermination du revenu foncier, travaux), RFPI-SPEC (sociétés immobilières).
- Imprimés : 2072 (déclaration de la SCI), 2044 (associés).
