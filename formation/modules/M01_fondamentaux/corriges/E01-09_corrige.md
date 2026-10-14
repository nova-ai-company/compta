# Corrigé E01-09 — Six propositions de l'OCR à valider… ou pas

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-09](../exercices/E01-09_controle-ocr-hotel.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Le « taux de confiance » mesure la qualité de la **lecture** (les caractères ont-ils été bien reconnus ?), pas la justesse du **traitement comptable**. L'outil applique des règles simples : un taux de TVA, un compte mémorisé par fournisseur, une date trouvée sur la pièce. Sur ce lot, **aucune des six propositions n'est valable en l'état** (la F est juste sur les montants mais crée un tiers en doublon).

| Pièce | Erreur | Type de piège | Conséquence |
|---|---|---|---|
| **A** StayBooker | **Autoliquidation non passée.** Prestataire établi aux Pays-Bas, preneur assujetti en France : la prestation est imposable en France (CGI art. 259) et la TVA est due par le preneur (CGI art. 283-2). La mention « Reverse charge » le confirme. | Fournisseur étranger | Résultat : aucune. TVA : 684,00 € à déclarer en TVA due **et** en TVA déductible (opération neutre) ; l'omission reste une **erreur déclarative sanctionnable** (amende proportionnelle prévue au CGI art. 1788 A — taux à vérifier). |
| **B** CashPro | **Un seul taux lu** (la ligne à 5,5 %) ; l'outil a « équilibré » en mettant le reste dans le HT : 1 316,86 – 22,66 = 1 294,20 €. Tout est en 601 alors que les alcools du minibar sont revendus en l'état (607). | Multi-taux | Charges surévaluées de **127,20 €** ; TVA déductible sous-évaluée de **127,20 €** ; mauvaise ventilation 601/607 (ratios de coût matière faussés). |
| **C** Hygiène Pro | **Avoir lu comme une facture** : débit de la charge au lieu d'un crédit. | Sens inversé | Charges surévaluées de **360,00 €** (2 × 180) ; TVA déductible surévaluée de **72,00 €** (2 × 36) ; dette fournisseur surévaluée de 432,00 €. |
| **D** Chauffage Service | **Date d'échéance (30/11) prise pour la date de facture (30/09).** | Date / clôture | La charge de **1 450,00 €** bascule sur l'exercice suivant (clôture au 31/10) : résultat 2025-2026 **surévalué**. |
| **E** MarketPro | **Règle mémorisée « MarketPro → 6063 »** appliquée à 10 téléviseurs à 549 € HT pièce. | Mémorisation / seuil | 5 490,00 € passés en charges au lieu d'être **immobilisés** (valeur unitaire > 500 € HT) ; TVA en 44566 au lieu de 44562. |
| **F** Énergies du Rhône | **Doublon de tiers** : « ENERGIES DU RHONE SAS » (sans accent, en capitales) n'a pas été rapproché de 401ENRH « Énergies du Rhône ». | Fichier tiers | Aucune incidence sur le résultat ; mais deux comptes pour un même fournisseur → lettrage impossible, relevé fournisseur non rapprochable, risque de doublon de paiement. |

## 2. Calculs (détaillés, chaque montant justifié)

**Pièce A** : TVA autoliquidée = 3 420,00 × 20 % = **684,00 €**.

**Pièce B** :

| Taux | HT | TVA |
|---|---|---|
| 5,5 % | 412,00 € | 412,00 × 5,5 % = 22,66 € |
| 10 % | 238,00 € | 238,00 × 10 % = 23,80 € |
| 20 % | 517,00 € | 517,00 × 20 % = 103,40 € |
| **Total** | **1 167,00 €** | **149,86 €** |

TTC : 1 167,00 + 149,86 = 1 316,86 € ✓. Ventilation : 601 = 412,00 + 238,00 = **650,00 €** (denrées et viennoiseries pour le petit-déjeuner) ; 607 = **517,00 €** (boissons du minibar revendues en l'état).
Écart OCR : 1 294,20 – 1 167,00 = **127,20 €** = 23,80 + 103,40 (la TVA à 10 % et 20 % a été mise en charge).

**Pièce E** : 10 × 549,00 = 5 490,00 € HT ; TVA 1 098,00 €. Pour mesurer l'incidence sur le résultat, on retient une durée d'utilisation de 5 ans et un amortissement linéaire à compter du 02/10/2026 : dotation de l'exercice = 5 490,00 / 5 × 30 / 360 = **91,50 €** (hypothèse, calcul définitif en module immobilisations).

**Incidence cumulée si Julien avait tout validé (question 3)**

| Pièce | Incidence sur le résultat 2025-2026 (clos le 31/10/2026) | Incidence sur la TVA |
|---|---|---|
| A | 0,00 € | Omission de 684,00 € de TVA due et de 684,00 € de TVA déductible (net 0 €, mais déclaration inexacte) |
| B | – 127,20 € (charges en trop) | TVA déductible minorée de 127,20 € |
| C | – 360,00 € | TVA déductible majorée de 72,00 € |
| D | + 1 450,00 € (charge manquante) | Déduction de 290,00 € décalée (voir point d'attention) |
| E | – 5 490,00 € + 91,50 € = – 5 398,50 € | Aucune sur le montant (mauvais compte : 44566 au lieu de 44562) |
| F | 0,00 € | 0,00 € |
| **Total** | **Résultat sous-évalué de 4 435,70 €** | **TVA déductible nette minorée de 55,20 €** (127,20 – 72,00), hors pièce D |

Calcul : – 127,20 – 360,00 + 1 450,00 – 5 398,50 = **– 4 435,70 €**.

## 3. Écritures comptables

Écritures **correctes** à valider (à la place des propositions OCR) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 622 | Rémunérations d'intermédiaires et honoraires (commissions) | StayBooker F SB-FR-2026-0927-11834 commissions 09/2026 | 3 420,00 | |
| 30/09/2026 | AC | 445662 | TVA déductible autoliquidée (services UE) | StayBooker F SB-FR-2026-0927-11834 autoliquidation | 684,00 | |
| 30/09/2026 | AC | 4452 | TVA due intracommunautaire (autoliquidation) | StayBooker F SB-FR-2026-0927-11834 autoliquidation | | 684,00 |
| 30/09/2026 | AC | 401STAY | Fournisseur StayBooker B.V. | StayBooker F SB-FR-2026-0927-11834 | | 3 420,00 |
| 03/10/2026 | AC | 601 | Achats de matières premières (denrées) | CashPro F CP-26-114820 denrées 5,5 % et 10 % | 650,00 | |
| 03/10/2026 | AC | 607 | Achats de marchandises (minibar) | CashPro F CP-26-114820 boissons 20 % | 517,00 | |
| 03/10/2026 | AC | 44566 | TVA déductible sur ABS | CashPro F CP-26-114820 (22,66 + 23,80 + 103,40) | 149,86 | |
| 03/10/2026 | AC | 401CASH | Fournisseur CashPro Lyon | CashPro F CP-26-114820 | | 1 316,86 |
| 01/10/2026 | AC | 401HYGI | Fournisseur Hygiène Pro | Hygiène Pro AV AV-26-0071 s/ F F-26-0988 retour gel douche | 216,00 | |
| 01/10/2026 | AC | 6063 | Fournitures d'entretien et petit équipement (produits d'accueil) | Hygiène Pro AV AV-26-0071 s/ F F-26-0988 | | 180,00 |
| 01/10/2026 | AC | 44566 | TVA déductible sur ABS | Hygiène Pro AV AV-26-0071 s/ F F-26-0988 | | 36,00 |
| 30/09/2026 | AC | 6152 | Entretien et réparations sur biens immobiliers | Chauffage Service Rhône F CSR-2026-1477 entretien chaudière | 1 450,00 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | Chauffage Service Rhône F CSR-2026-1477 | 290,00 | |
| 30/09/2026 | AC | 401CHSR | Fournisseur Chauffage Service Rhône | Chauffage Service Rhône F CSR-2026-1477 | | 1 740,00 |
| 02/10/2026 | AC | 218 | Autres immobilisations corporelles (matériel hôtelier – téléviseurs) | MarketPro F MPF-26-55102 10 TV chambres | 5 490,00 | |
| 02/10/2026 | AC | 44562 | TVA déductible sur immobilisations | MarketPro F MPF-26-55102 | 1 098,00 | |
| 02/10/2026 | AC | 404MARK | Fournisseur d'immobilisations MarketPro | MarketPro F MPF-26-55102 | | 6 588,00 |
| 05/10/2026 | AC | 6061 | Fournitures non stockables (énergie) | Énergies du Rhône F EDR-0926-778120 élec. 09/2026 | 2 840,00 | |
| 05/10/2026 | AC | 44566 | TVA déductible sur ABS | Énergies du Rhône F EDR-0926-778120 | 568,00 | |
| 05/10/2026 | AC | 401ENRH | Fournisseur Énergies du Rhône | Énergies du Rhône F EDR-0926-778120 | | 3 408,00 |
| | | | | **Totaux** | **17 372,86** | **17 372,86** |

Compléments :
- **Pièce E** : le paiement par carte du 02/10 soldera le 404MARK au journal de banque ; ajouter les 10 téléviseurs au tableau des immobilisations (mise en service à la date d'installation dans les chambres).
- **Pièce F** : supprimer le tiers 401ENER créé par l'outil (aucune écriture validée dessus) et ajouter l'alias « ENERGIES DU RHONE SAS » au tiers 401ENRH.
- **Pièce D** : le libellé de l'intervention (entretien + remplacement d'un circulateur) relève de l'entretien courant ; si le circulateur était un composant identifié et significatif, on examinerait son immobilisation — ici, montant global modeste, charge.

## 4. Points d'attention / pièges

- **Pièce D et TVA** : la prestation d'entretien est un **service** ; si le prestataire n'a pas opté pour les débits, la TVA n'est déductible qu'au **paiement** (le 30/11 au plus tard). La **charge**, elle, est bien de septembre (intervention du 24/09), donc de l'exercice clos le 31/10/2026. Charge et TVA n'ont pas le même calendrier.
- **Pièce A** : l'hôtel est assujetti ; la commission de la plateforme est imposable en France par autoliquidation. Les plateformes facturent souvent depuis un autre État membre : vérifier chaque mois.
- **Pièce C** : un avoir **diminue** la charge **et** la TVA déductible. Repérer les mots « AVOIR », « CREDIT NOTE », les montants négatifs.
- **Pièce E** : la règle mémorisée est le piège le plus coûteux ; elle est « juste » 95 % du temps (petites fournitures), d'où une fausse impression de fiabilité.
- **Taux de confiance** : ne jamais l'utiliser comme critère de validation comptable.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Liste de contrôles pour Julien (question 4), avant toute validation d'un lot OCR de l'Hôtel Belle Vue :**
1. **Dates** : toute pièce datée du 01/10 au 30/11 → contrôle visuel de la date de facture (clôture au 31/10).
2. **Fournisseurs étrangers** (adresse hors France, n° TVA non FR, mentions « reverse charge ») → autoliquidation.
3. **Multi-taux** : toute facture alimentaire / cash & carry → recalcul de la TVA par taux.
4. **Avoirs** : filtre sur « AVOIR / CREDIT NOTE / montant négatif ».
5. **Seuil de 500 € HT** : alerte sur toute ligne > 500 € HT imputée en 606x / 6063 / 6064.
6. **Tiers** : refuser toute création automatique de fournisseur ; rapprocher d'abord par SIREN.
7. **Doublons** : contrôle n° de facture + tiers + montant (y compris PDF vs flux PA).

**Paramétrages à modifier dans l'outil** : supprimer la règle « MarketPro → 6063 » (remplacer par « MarketPro → à classer ») ; créer une règle « StayBooker → autoliquidation 20 % » ; activer le rapprochement des tiers par SIREN ; désactiver la création automatique de tiers ; ajouter une alerte sur les dates postérieures à la clôture.

**Documentation** : noter dans le dossier permanent de l'hôtel les règles de pré-comptabilisation spécifiques (plateformes de réservation, cash & carry multi-taux, matériel des chambres) et la date de dernière revue des règles mémorisées.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 259 et 283-2 : lieu des prestations de services entre assujettis et autoliquidation par le preneur.
- CGI art. 1788 A : sanctions des manquements en matière d'autoliquidation (montants à vérifier).
- CGI art. 269-2-c et 271 : exigibilité de la TVA sur les services et naissance du droit à déduction.
- CGI art. 272 : régularisation de la TVA déduite en cas d'avoir.
- BOFiP, BIC – Charges – immobilisations de faible valeur (seuil de 500 € HT).
- PCG : rattachement des charges à l'exercice ; comptes 601, 607, 44562, 44566, 4452, 445662.
