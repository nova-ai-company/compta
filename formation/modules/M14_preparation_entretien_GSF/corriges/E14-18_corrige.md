# Corrigé E14-18 — Préparer la CA3 mensuelle de GSF Riviera à partir de la balance des comptes de TVA

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-18](../exercices/E14-18_ca3-mensuelle-gsf-riviera.md)

*Numérotation des lignes du 3310-CA3 donnée à titre indicatif — à vérifier sur le formulaire en vigueur.*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Compte par compte

| Compte | Dans la CA3 de septembre ? | Ligne (indicative) |
|---|---|---|
| 44571 (312 486,40) | **Oui** : TVA exigible sur les encaissements du mois | Base 1 562 432,00 en A1 (01) « ventes, prestations de services » ; taux normal ligne 08 |
| 44574 (248 902,16) | **Non** : TVA non encore exigible | — (à rapprocher des créances clients ouvertes) |
| 445711 (630,00) | **Oui** : autoliquidation sous-traitance BTP, exigible au paiement | Base 3 150,00 en ligne 02 « autres opérations imposables » ; ligne 08 |
| 4452 – CloudLedger (314,53) | **Oui** : service d'un prestataire non établi en France, autoliquidé par GSF Riviera | Base 1 572,65 en A3 « achats de prestations de services réalisés auprès d'un assujetti non établi en France » ; ligne 08 |
| 4452 – pièces Allemagne (476,00) | **Oui** : acquisition intracommunautaire de biens | Base 2 380,00 en B2 « acquisitions intracommunautaires » ; ligne 08 ; rappel ligne 17 |
| 44562 (4 218,40) | **Oui** | Ligne 19 « biens constituant des immobilisations » |
| 44566 (96 412,18) | **Oui, après correction** des cadeaux (− 180,00) | Ligne 20 « autres biens et services » |
| 445661 / 445662 (630,00 / 790,53) | **Oui** : déduction de la TVA autoliquidée | Ligne 20 |
| 44586 (3 412,00) | **Non** : pas de facture → pas de droit à déduction | — |
| 44587 (5 240,00) | **Non** : pas de facture, pas d'encaissement | — |
| Facture Bâti Azur (9 800,00, autoliquidée par le client) | **Oui, sans TVA** : opération non imposable chez GSF Riviera | E2 « autres opérations non imposables » |

**44586 — réponse au collègue** : non. La TVA ne se déduit que sur la base d'une **facture** (et, pour les services, quand elle est exigible chez le prestataire). Une FNP est une estimation comptable : sa TVA attend la facture.

**Boutique Mistral — réponse au collègue** : non plus. Sous le régime des **encaissements**, la TVA de cette facture **n'a jamais été exigible ni déclarée** (elle est restée en 44574). Il n'y a donc **rien à « récupérer »** : une imputation en régularisation ferait déduire 360,00 € qui n'ont jamais été versés au Trésor. On solde simplement la créance : perte sur créance irrécouvrable **HT** (654 : 1 800,00 €) et annulation de la TVA en attente (44574 : 360,00 €). (Sous le régime des débits, la TVA aurait été déclarée à la facture, et sa récupération aurait supposé une facture rectificative / un avoir après constat de l'irrécouvrabilité définitive.)

**Cadeaux** : la TVA sur les cadeaux n'est déductible que pour les biens de **très faible valeur** (≤ 73 € TTC par bénéficiaire et par an, *à vérifier*). Chaque coffret vaut 120,00 € TTC > 73 € → TVA **non déductible** : 9 × 20,00 = **180,00 €** à réintégrer en charge.

## 2. Calculs (détaillés, chaque montant justifié)

**Brouillon de CA3 — septembre 2026**

| Ligne (indicative) | Libellé | Base HT | TVA |
|---|---|---|---|
| A1 (01) | Ventes, prestations de services (encaissements) | 1 562 432,00 | |
| A3 | Achats de prestations de services auprès d'un assujetti non établi en France | 1 572,65 | |
| B2 | Acquisitions intracommunautaires | 2 380,00 | |
| 02 | Autres opérations imposables (autoliquidation sous-traitance BTP) | 3 150,00 | |
| E2 | Autres opérations non imposables (facture Bâti Azur autoliquidée) | 9 800,00 | |
| 08 | Taux normal 20 % : 1 562 432,00 + 1 572,65 + 2 380,00 + 3 150,00 | **1 569 534,65** | **313 906,93** |
| 16 | Total de la TVA brute due | | **313 906,93** |
| 17 | dont TVA sur acquisitions intracommunautaires | | 476,00 |
| 19 | TVA déductible – biens constituant des immobilisations | | **4 218,40** |
| 20 | TVA déductible – autres biens et services : 96 412,18 − 180,00 + 630,00 + 790,53 | | **97 652,71** |
| 22 | Report du crédit de la déclaration précédente | | 0,00 |
| 23 | Total TVA déductible | | **101 871,11** |
| 28 | **TVA nette due** (16 − 23) | | **212 035,82** |
| 32 | Total à payer | | **212 035,82** |

Contrôle : TVA brute = 312 486,40 + 630,00 + 314,53 + 476,00 = 313 906,93 € = 1 569 534,65 × 20 % ✓.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6234 | Cadeaux | TVA non déductible coffrets clients > 73 € TTC (9 × 20,00) | 180,00 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur ABS | TVA non déductible coffrets clients | | 180,00 |
| 30/09/2026 | OD | 654 | Pertes sur créances irrécouvrables | Boutique Mistral F FR-2026-03-0144 – LJ clôturée 25/09 | 1 800,00 | |
| 30/09/2026 | OD | 44574 | TVA collectée en attente d'encaissement | Boutique Mistral – TVA jamais exigible, annulée | 360,00 | |
| 30/09/2026 | OD | 411BMIS | Client Boutique Mistral | Boutique Mistral – créance irrécouvrable | | 2 160,00 |
| 30/09/2026 | OD | 44571 | TVA collectée | Liquidation CA3 09/2026 | 312 486,40 | |
| 30/09/2026 | OD | 445711 | TVA due autoliquidée – sous-traitance BTP | Liquidation CA3 09/2026 | 630,00 | |
| 30/09/2026 | OD | 4452 | TVA due intracommunautaire / autoliquidée | Liquidation CA3 09/2026 | 790,53 | |
| 30/09/2026 | OD | 44562 | TVA déductible sur immobilisations | Liquidation CA3 09/2026 | | 4 218,40 |
| 30/09/2026 | OD | 44566 | TVA déductible sur ABS | Liquidation CA3 09/2026 | | 96 232,18 |
| 30/09/2026 | OD | 445661 | TVA déductible autoliquidée – sous-traitance BTP | Liquidation CA3 09/2026 | | 630,00 |
| 30/09/2026 | OD | 445662 | TVA déductible intracommunautaire / autoliquidée | Liquidation CA3 09/2026 | | 790,53 |
| 30/09/2026 | OD | 44551 | TVA à décaisser | Liquidation CA3 09/2026 | | 212 035,82 |
| 19/10/2026 | BQ | 44551 | TVA à décaisser | Télérèglement CA3 09/2026 | 212 035,82 | |
| 19/10/2026 | BQ | 512 | Banque | Télérèglement CA3 09/2026 | | 212 035,82 |
| | | | | **Totaux** | **528 282,75** | **528 282,75** |

Après liquidation, restent seulement en balance : 44574 (248 902,16 − 360,00 = 248 542,16 C), 44586 (3 412,00 D) et 44587 (5 240,00 C), qui ne sont pas des comptes déclaratifs du mois.

## 4. Points d'attention / pièges

- **Déclarer le 44574** (TVA facturée non encaissée) : erreur coûteuse en trésorerie (on avancerait près de 249 k€ au Trésor).
- **Oublier les autoliquidations** : elles sont neutres en trésorerie (due = déductible), mais leur omission est sanctionnée (amende spécifique) et fausse les recoupements (déclaration d'échanges de services / données douanières pour les acquisitions intracommunautaires).
- **Facture autoliquidée émise par GSF Riviera** (Bâti Azur) : base en « non imposable » (E2), sans TVA ; ne pas l'oublier, l'administration rapproche le chiffre d'affaires déclaré du chiffre d'affaires comptable.
- **Taux de conversion** des factures en devises (CloudLedger) : celui retenu par la comptabilité doit être cohérent avec les règles applicables (*taux à vérifier*), et la TVA autoliquidée est calculée sur la base en euros.
- **Créance irrécouvrable** : HT en 654 (la TVA en attente n'a jamais été une charge ni une dette réelle envers le Trésor).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Contrôles avant transmission (question 4)** :
1. **44571 = 20 % des encaissements HT du mois** (journal de banque × 20/120) : 1 562 432,00 × 20 % = 312 486,40 ✓.
2. **44574 = TVA contenue dans la balance âgée clients** (créances TTC × 20/120), après la sortie de Boutique Mistral.
3. **Autoliquidations : comptes « due » = comptes « déductible »** (630,00 / 630,00 ; 790,53 / 790,53) ✓.
4. **Chiffre d'affaires déclaré vs comptable** : CA comptable du mois (706) vs encaissements déclarés : l'écart doit s'expliquer par la variation des créances clients (et les opérations non imposables).
5. Revue des **TVA non déductibles** classiques : cadeaux > seuil, véhicules de tourisme (E14-10), dépenses de logement / restaurant du personnel, factures non conformes.
6. Comparaison avec les **trois derniers mois** (TVA nette due / CA) et explication des variations.
7. Dossier de déclaration : brouillon, balance des comptes de TVA, états de rapprochement, justificatifs des autoliquidations, validation par la responsable avant télédéclaration.

**Message à Sophie Garnier** : « CA3 de septembre : TVA nette due **212 035,82 €** (TVA brute 313 906,93 € dont 1 420,53 € d'autoliquidations ; TVA déductible 101 871,11 €). Corrections avant déclaration : TVA sur cadeaux clients non déductible (180,00 €), créance Boutique Mistral passée en perte HT sans régularisation de TVA (TVA jamais exigible sur les encaissements). Les 44586 / 44587 ne sont pas déclarés. Échéance de paiement retenue : 19/10. »

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 269-2-c (encaissements), 271 (déduction : facture et exigibilité), 283-1, 283-2 et 283-2 nonies (autoliquidations), 256 bis (acquisitions intracommunautaires), 272 (régularisations, créances irrécouvrables).
- CGI annexe II art. 206-IV-2-3° et art. 28-00 A de l'annexe IV : exclusion des cadeaux sauf biens de très faible valeur (seuil à vérifier).
- CGI art. 287 et annexe II (obligations déclaratives, CA3 mensuelle) ; formulaire n° 3310-CA3 et sa notice (*numérotation à vérifier*).
- PCG : comptes 4452, 44551, 44562, 44566, 44571, 44574, 654.
