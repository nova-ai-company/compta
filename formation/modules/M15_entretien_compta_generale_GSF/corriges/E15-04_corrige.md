# Corrigé E15-04 — TVA : préparer la CA3 de septembre 2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-04](../exercices/E15-04_ca3-septembre-2026.md)

*Numérotation des lignes du 3310-CA3 donnée à titre indicatif — à vérifier sur le formulaire en vigueur.*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### La logique de la CA3 en trois étapes

1. **TVA brute** : la TVA que GSF Riviera doit au Trésor pour le mois (TVA collectée exigible + TVA autoliquidée).
2. **TVA déductible** : la TVA payée aux fournisseurs que GSF Riviera a le droit de récupérer (+ le crédit du mois précédent).
3. **TVA nette** = brute − déductible. Si positive → à payer ; si négative → crédit à reporter.

### Question 1 — Compte par compte

| Compte | Dans la CA3 de septembre ? | Pourquoi |
|---|---|---|
| 44571 (58 400,00) | **Oui** | TVA des encaissements de septembre : c'est la TVA **exigible** du mois (régime des encaissements) |
| 445711 (1 200,00) | **Oui** | TVA due par GSF Riviera sur la sous-traitance autoliquidée |
| 44574 (71 250,00) | **Non** | TVA de factures **non encaissées** : elle n'est pas encore due. Elle sera déclarée le mois où le client paiera |
| 44562 (1 840,00) | **Oui** | TVA déductible sur immobilisations (ligne séparée) |
| 44566 (14 251,60) | **Oui, après correction** | Il faut d'abord retirer la TVA non déductible (150,00) |
| 445661 (1 200,00) | **Oui** | Déduction de la TVA autoliquidée (même montant que le 445711) |
| 44567 (2 300,00) | **Oui** | Crédit de la CA3 d'août, reporté en déduction |

### Question 2 — Base des encaissements

Toutes les ventes sont à 20 % : base = 58 400,00 / 20 % = **292 000,00 € HT**. C'est le montant à porter en ligne « ventes, prestations de services ».

### Question 3 — TVA non déductible

- **Entretien du véhicule de tourisme** (60,00 €) : la TVA sur les véhicules de tourisme (achat, location, **entretien, réparations**) n'est **pas déductible**, sauf exceptions (véhicules utilitaires, auto-écoles, taxis…). Un véhicule 4 places à usage mixte du directeur est un véhicule de tourisme → TVA non récupérable : elle devient une **charge**.
- **Coffrets cadeaux** (90,00 €) : la TVA sur les cadeaux n'est déductible que pour les biens de **très faible valeur** (on retient 73 € TTC par bénéficiaire et par an). Chaque coffret vaut 90,00 € TTC > 73 € → **aucune** TVA déductible sur les 6 coffrets (6 × 15,00 = 90,00 €).

Total non déductible : 60,00 + 90,00 = **150,00 €**.

Les repas (10 %) et les ouvrages (5,5 %) sont des dépenses professionnelles avec justificatifs au nom de la société : TVA **déductible**. Le taux ne change rien au droit à déduction ; il sert seulement à vérifier les montants (1 240,00 × 10 % = 124,00 ; 320,00 × 5,5 % = 17,60).

### Pourquoi l'autoliquidation de la sous-traitance ?

Dans le BTP, quand un sous-traitant travaille pour une entreprise elle-même sous-traitante ou titulaire d'un marché de travaux immobiliers, c'est le **preneur** (ici GSF Riviera) qui déclare la TVA à la place du sous-traitant. Le nettoyage de fin de chantier, rattaché aux travaux de construction, entre dans ce dispositif (*conditions d'application à vérifier au cas par cas*). GSF Riviera déclare 1 200,00 € de TVA due **et** déduit 1 200,00 € : effet nul sur le montant à payer, mais les deux lignes doivent figurer sur la déclaration.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 4 — TVA déductible

- Immobilisations (ligne 19) : **1 840,00 €** (contrôle : 9 200,00 × 20 % = 1 840,00 ✓).
- Autres biens et services (ligne 20) : 14 251,60 − 150,00 (non déductible) + 1 200,00 (autoliquidation) = **15 301,60 €**.
- Contrôle du détail 44566 : 13 960,00 + 60,00 + 90,00 + 124,00 + 17,60 = 14 251,60 ✓.

### Question 5 — Brouillon de CA3 de septembre 2026

| Ligne (indicative) | Libellé | Base HT | TVA |
|---|---|---|---|
| A1 (01) | Ventes, prestations de services (encaissements de septembre) | 292 000,00 | |
| 02 | Autres opérations imposables (sous-traitance autoliquidée) | 6 000,00 | |
| 08 | Taux normal 20 % : 292 000,00 + 6 000,00 | **298 000,00** | **59 600,00** |
| 16 | Total de la TVA brute | | **59 600,00** |
| 19 | TVA déductible sur immobilisations | | 1 840,00 |
| 20 | TVA déductible sur autres biens et services | | 15 301,60 |
| 22 | Report du crédit de la déclaration précédente | | 2 300,00 |
| 23 | Total TVA déductible | | **19 441,60** |
| 28 | **TVA nette due** (16 − 23) | | **40 158,40** |

Contrôles :
- TVA brute = 58 400,00 + 1 200,00 = 59 600,00 = 298 000,00 × 20 % ✓.
- Total déductible = 1 840,00 + 15 301,60 + 2 300,00 = 19 441,60 ✓.
- TVA nette = 59 600,00 − 19 441,60 = **40 158,40 €** à payer au plus tard le 19/10/2026.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 61551 | Entretien et réparations – matériel de transport | TVA non déductible entretien véhicule de tourisme | 60,00 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur autres biens et services | TVA non déductible entretien véhicule de tourisme | | 60,00 |
| 30/09/2026 | OD | 6234 | Cadeaux | TVA non déductible 6 coffrets > 73 € TTC | 90,00 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur autres biens et services | TVA non déductible 6 coffrets > 73 € TTC | | 90,00 |
| 30/09/2026 | OD | 44571 | TVA collectée | Liquidation CA3 09/2026 | 58 400,00 | |
| 30/09/2026 | OD | 445711 | TVA due autoliquidée – sous-traitance | Liquidation CA3 09/2026 | 1 200,00 | |
| 30/09/2026 | OD | 44562 | TVA déductible sur immobilisations | Liquidation CA3 09/2026 | | 1 840,00 |
| 30/09/2026 | OD | 44566 | TVA déductible sur autres biens et services | Liquidation CA3 09/2026 (14 251,60 − 150,00) | | 14 101,60 |
| 30/09/2026 | OD | 445661 | TVA déductible autoliquidée – sous-traitance | Liquidation CA3 09/2026 | | 1 200,00 |
| 30/09/2026 | OD | 44567 | Crédit de TVA à reporter | Liquidation CA3 09/2026 – imputation crédit d'août | | 2 300,00 |
| 30/09/2026 | OD | 44551 | TVA à décaisser | Liquidation CA3 09/2026 | | 40 158,40 |
| 19/10/2026 | BQ | 44551 | TVA à décaisser | Télérèglement CA3 09/2026 | 40 158,40 | |
| 19/10/2026 | BQ | 512 | Banque | Télérèglement CA3 09/2026 | | 40 158,40 |
| | | | | **Totaux** | **99 908,40** | **99 908,40** |

**Pourquoi ces sens ?** La liquidation **solde** chaque compte de TVA déclaré : on débite les comptes créditeurs (TVA collectée, TVA due) et on crédite les comptes débiteurs (TVA déductible, crédit antérieur). La différence est la dette envers le Trésor : **44551 au crédit**. Le paiement solde cette dette (44551 au débit, banque au crédit).

**Corrections de TVA non déductible** : la TVA « non récupérable » n'est pas perdue comptablement, elle **augmente la charge** concernée (61551 pour l'entretien, 6234 pour les cadeaux).

Après liquidation, il ne reste en balance que le **44574 (71 250,00 € créditeur)**, qui n'est pas un compte déclaratif du mois.

## 4. Points d'attention / pièges

- **Déclarer le 44574** : c'est le piège principal pour une entreprise de services. On paierait 71 250,00 € de TVA que les clients n'ont pas encore payée.
- **Oublier le crédit d'août** (ligne 22) : on paierait 2 300,00 € de trop.
- **Oublier l'autoliquidation** : sans effet sur le montant à payer, mais la déclaration est incomplète (et sanctionnable).
- **TVA non déductible** : véhicules de tourisme (achat, location, entretien) et cadeaux au-delà du seuil. Le carburant des véhicules de tourisme obéit à des règles particulières (déduction partielle) : non traité ici.
- **Le taux ne décide pas de la déduction** : une TVA à 10 % ou 5,5 % se déduit comme une TVA à 20 %, si la dépense est professionnelle et justifiée par une facture.

## 5. Ce que le recruteur attend / ce qu'un senior ferait en plus

- **Contrôle de cohérence** : TVA collectée / base = 20 % ; TVA autoliquidée due = TVA autoliquidée déductible ; TVA nette du mois comparée aux mois précédents (une variation forte doit s'expliquer).
- **Contrôle du 44574** : il doit correspondre à la TVA contenue dans les factures clients non réglées (balance âgée clients × 20/120).
- **Prévenir les acheteurs** : les cadeaux clients au-delà de 73 € TTC « coûtent » 20 % de plus que prévu ; certains groupes fixent un budget cadeau en TTC.
- **Dossier de déclaration** : brouillon de CA3, balance des comptes de TVA, détail des corrections, accusé de dépôt et de paiement, archivés avec la validation du chef comptable.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 269 (exigibilité : encaissement pour les prestations de services), art. 271 (droit à déduction), art. 283-2 nonies (autoliquidation de la sous-traitance dans le BTP), art. 287 (obligations déclaratives).
- CGI annexe II art. 206 (exclusions du droit à déduction : véhicules de tourisme, cadeaux sauf biens de très faible valeur) — *seuil à vérifier chaque année*.
- Formulaire n° 3310-CA3 et sa notice (*numérotation des lignes à vérifier*).
- PCG : comptes 44551, 44562, 44566, 445661, 44567, 44571, 445711, 44574, 6234, 61551.
