# Corrigé E03-06 — Vente d'un véhicule d'occasion et carte grise en débours

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-06](../exercices/E03-06_vente-vo-cartes-grises.md)

## 1. Analyse

**a) Régime de la marge (art. 297 A CGI).** Il s'applique aux livraisons de biens d'occasion par un **assujetti-revendeur** lorsque le bien a été acquis **sans possibilité de déduire la TVA** : auprès d'un particulier, d'un assujetti qui n'a pas pu déduire la TVA, d'un autre revendeur ayant lui-même appliqué le régime de la marge. Ici, le SUV a été acheté à **M. Lacroix, particulier**, sans TVA : régime de la marge **obligatoire**. La TVA est due sur la **marge** = prix de vente TTC – prix d'achat, et se calcule « en dedans » (marge × 20/120).

Le véhicule n'est pas un « moyen de transport neuf » (plus de 6 mois et plus de 6 000 km) : aucune règle particulière.

**b) Mentions de facture** sous ce régime :
- mention **« Régime particulier – Biens d'occasion »** (art. 242 nonies A ann. II CGI, en référence à l'art. 297 A) ;
- **aucune TVA ne doit apparaître** sur la facture pour la vente du véhicule (art. 297 E CGI) : l'acheteur ne peut pas la déduire. Faire figurer « dont TVA 3 150 € » est une faute : la TVA mentionnée à tort est due du seul fait de sa facturation (art. 283-3 CGI) tant que la facture n'est pas rectifiée.

**c) Les frais de remise en état** (pièces de 620 € HT) **n'entrent pas** dans le prix d'achat pour le calcul de la marge : la marge est la différence entre le prix de vente et le **prix d'achat** du bien. En contrepartie, la TVA sur ces pièces (124 €) est **déductible** normalement.

**d) Les frais de mise à la route** (préparation, contrôle, plein) facturés à l'acheteur sont l'**accessoire** de la livraison du véhicule : ils suivent le régime du principal et **s'ajoutent au prix de vente** pour le calcul de la marge. On ne les taxe pas séparément à 20 % sur leur montant total.

**e) Taxes de carte grise : débours.** Les trois conditions de l'art. 267-II-2° CGI sont réunies :
1. **mandat** : mandat d'immatriculation signé par M. Faure ;
2. **compte de passage** : à condition de les enregistrer en **467** (pas en charges / produits) ;
3. **reddition de comptes** : refacturation au **montant exact** (314,76 €) avec le récapitulatif ANTS.

Elles sont donc **hors base de TVA**. Les **frais de démarche** (36 € TTC), eux, rémunèrent un service rendu par le garage : TVA 20 %, compte 706.

## 2. Calculs

| Élément | Montant |
|---|---|
| Prix de vente du véhicule TTC | 18 900,00 |
| + Frais de mise à la route (accessoires) | 290,00 |
| **= Prix de vente total (régime de la marge)** | **19 190,00** |
| – Prix d'achat (M. Lacroix) | – 14 500,00 |
| **= Marge TTC** | **4 690,00** |
| **TVA sur la marge** : 4 690 × 20/120 | **781,67** |
| Marge HT | 3 908,33 |
| Produit de la vente (707) : 19 190,00 – 781,67 | **18 408,33** |
| Frais de démarche : HT 30,00 + TVA 6,00 | 36,00 |
| Débours carte grise (Y6) | 314,76 |
| **Total à payer par le client** (inchangé) | **19 540,76** |

**Incidence sur la TVA de septembre**

| | TVA comptabilisée (pièce 5) | TVA due |
|---|---|---|
| Véhicule + accessoires | 3 150,00 + 48,33 | 781,67 |
| Carte grise | 52,46 | 0,00 |
| Démarche | 6,00 | 6,00 |
| **Total** | **3 256,79** | **787,67** |

La TVA collectée est **surévaluée de 2 469,12 €**. Tant que la facture n'est pas rectifiée, cette TVA reste due (art. 283-3). Une fois l'avoir et la nouvelle facture émis (en septembre si possible, sinon à la date de rectification), seule la TVA sur marge est due.

**Marge économique de l'opération** : 18 408,33 – 14 500,00 – 620,00 = **3 288,33 € HT**.

## 3. Écritures comptables

**a) Écritures de l'opération**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/07/2026 | AC | 607 | Achats de marchandises (VO) | VO-26-041 Lacroix – sans TVA | 14 500,00 | |
| 02/07/2026 | AC | 512 | Banque | Paiement VO-26-041 | | 14 500,00 |
| 28/07/2026 | AC | 607 | Achats de marchandises (pièces) | AP-77810 remise en état FG-218-KL | 620,00 | |
| 28/07/2026 | AC | 44566 | TVA déductible sur ABS | AP-77810 | 124,00 | |
| 28/07/2026 | AC | 401APR | Fournisseur Auto-Pièces Rhône | AP-77810 | | 744,00 |
| 16/09/2026 | BQ | 467 | Débours clients – cartes grises | ANTS Faure FG-218-KL | 314,76 | |
| 16/09/2026 | BQ | 512 | Banque (CB pro) | ANTS Faure | | 314,76 |
| 18/09/2026 | VT | 411FAU | Client Faure | Facture V-2026-0094 (rectificative) | 19 540,76 | |
| 18/09/2026 | VT | 7071 | Ventes de VO – régime de la marge | VO FG-218-KL + mise à la route | | 18 408,33 |
| 18/09/2026 | VT | 445712 | TVA collectée sur marge | TVA marge 4 690 × 20/120 | | 781,67 |
| 18/09/2026 | VT | 706 | Prestations de services | Frais de démarche carte grise | | 30,00 |
| 18/09/2026 | VT | 44571 | TVA collectée 20 % | Frais de démarche | | 6,00 |
| 18/09/2026 | VT | 467 | Débours clients – cartes grises | Refacturation ANTS Faure | | 314,76 |
| 18/09/2026 | BQ | 512 | Banque | Virement Faure | 19 540,76 | |
| 18/09/2026 | BQ | 411FAU | Client Faure | Virement Faure | | 19 540,76 |
| | | | | **Totaux** | **54 640,28** | **54 640,28** |

**b) Écriture de correction de la pièce 5** (à passer à la place de l'annulation pure et simple, si l'écriture erronée est déjà validée) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 18/09/2026 | VT | 707 | Ventes de marchandises | Avoir AV-2026-0011 annulant V-2026-0093 | 16 283,97 | |
| 18/09/2026 | VT | 44571 | TVA collectée | Avoir AV-2026-0011 | 3 256,79 | |
| 18/09/2026 | VT | 411FAU | Client Faure | Avoir AV-2026-0011 | | 19 540,76 |
| | | | | **Totaux** | **19 540,76** | **19 540,76** |

Le compte 467 « débours cartes grises » est soldé (314,76 au débit et au crédit) ✔. Le client est soldé ✔.

## 4. Points d'attention / pièges

- **Régime global ou cas par cas ?** Pour les véhicules, c'est toujours **pièce par pièce** : le régime de la marge globale est réservé aux biens dont le prix d'achat unitaire n'excède pas 300 € (voir M04, E04-03). Une vente à perte ne génère pas de TVA mais ne s'impute pas sur la marge d'un autre véhicule.
- **Ne jamais faire apparaître de TVA** sur la ligne du véhicule vendu sous le régime de la marge.
- **Pièces de remise en état** : TVA déductible, et coût à intégrer à la valeur du VO **en stock** si le véhicule n'est pas vendu à la clôture (coût nécessaire pour mettre le bien en état d'être vendu).
- **Débours** : le paiement par la carte pro du garage n'empêche pas la qualification de débours, dès lors que le mandat existe et que la dépense est passée en 467. Le compte 467 doit être **soldé** dossier par dossier : un solde débiteur ancien = carte grise payée non refacturée.
- **Dernier mois de l'exercice** : la rectification doit intervenir rapidement — la TVA de septembre est déclarée sur la CA3 déposée en octobre, et c'est aussi le mois de clôture (le CA de l'exercice est en jeu : 707 corrigé à 18 408,33 €).

## 5. Ce qu'un senior ferait en plus

**Procédure de remplacement de la facture** : émettre un **avoir** n° AV-2026-0011 annulant intégralement V-2026-0093 (avec la référence de la facture annulée), puis une **nouvelle facture** V-2026-0094 du même jour, transmise au client avec un mot d'explication. Le total payé par M. Faure ne change pas : aucune incidence pour lui.

**Corps de la facture correcte :**
```
FACTURE N° V-2026-0094 – 18/09/2026 – Nature : livraison de bien (+ prestation de démarche)
Annule et remplace la facture V-2026-0093 (avoir AV-2026-0011)
Véhicule d'occasion SUV diesel FG-218-KL – 1re MEC 03/2021 – 68 400 km
  y compris préparation et mise à la route                                     19 190,00
  « Régime particulier – Biens d'occasion » (art. 297 A du CGI) – TVA non récupérable
Frais de démarche d'immatriculation           HT 30,00 – TVA 20 % 6,00 – TTC      36,00
Débours : taxes d'immatriculation acquittées pour votre compte
  (mandat du 18/09/2026 – récapitulatif ANTS joint, Y6)                          314,76
TOTAL À PAYER                                                                  19 540,76
Réglé par virement le 18/09/2026
```

**Contrôles à étendre** : relire **toutes les factures VO** de l'exercice (le stagiaire a utilisé le modèle atelier) ; rapprocher le livre de police des factures d'achat et de vente ; vérifier le solde du 467 au 30/09 ; paramétrer dans le logiciel un modèle « VO régime de la marge » sans TVA apparente.

## 6. Références

- CGI : art. 297 A (régime de la marge), art. 297 E (interdiction de faire apparaître la TVA), art. 267-II-2° (débours), art. 283-3 (TVA facturée à tort), art. 242 nonies A ann. II (mentions).
- BOFiP : TVA-SECT (biens d'occasion — assujettis-revendeurs) ; TVA-BASE (débours).
- PCG : comptes 607, 7071, 467, 4457x.
- Code pénal : art. 321-7 (tenue du registre de police pour les revendeurs d'objets mobiliers).
