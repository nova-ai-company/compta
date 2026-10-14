# Corrigé E01-04 — Lettrer un compte fournisseur qui « ne tombe pas juste »

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-04](../exercices/E01-04_lettrage-fournisseur-hotel.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 : lettrer ce qui se solde évidemment.** On part des factures et on cherche les règlements et avoirs qui les soldent, **en lisant les libellés et les dates**, pas seulement les montants.

| Code | Écritures | Débit | Crédit | Solde |
|---|---|---|---|---|
| **A** | F 2026-311 (05/07) / Vir. 10/07 | 1 860,00 | 1 860,00 | 0,00 |
| **B** | F 2026-352 **AC-0803** (04/08) / Vir. 20/08 « acompte » 1 500,00 + Vir. 15/09 840,00 | 2 340,00 | 2 340,00 | 0,00 |
| **C** | F 2026-398 (03/09) / AV 2026-021 (08/09) 210,00 + Vir. 25/09 2 400,00 | 2 610,00 | 2 610,00 | 0,00 |

Les paiements partiels se comprennent : le 20/08, M. Garnier a versé 1 500,00 € sur la facture 352, puis le solde de 840,00 € le 15/09 (1 500 + 840 = 2 340). Le 25/09, il a payé la facture 398 sous déduction de l'avoir (2 610 – 210 = 2 400).

**Étape 2 : analyser ce qui reste.**
- **AC-0821 (06/08) — F 2026-352, 2 340,00 €** : même numéro de facture, même montant, même fournisseur que AC-0803 ; la pièce jointe est le scan du même document. C'est un **doublon** (OCR + saisie manuelle). Il ne se lettre pas avec un règlement : il se **contre-passe**, et on lettre l'écriture d'origine avec son extourne (code **D**).
- **F 2026-441 (02/10) — 2 280,00 €** : facture de septembre, non échue → reste due, normal.
- **F 2026-372 (17/08) — 396,00 €** : figure chez le fournisseur, **absente de notre comptabilité**. Facture de banquet (mariage du 15/08), probablement remise au service banquets et jamais transmise. Échue depuis le 16/09.

**Étape 3 : conclusion.** M. Garnier a raison sur les factures qu'il a reçues : il les a toutes payées. Mais (1) la comptabilité contient un doublon qui gonfle la dette de 2 340,00 € et — plus grave — a fait **déduire deux fois 390,00 € de TVA** ; (2) une facture de 396,00 € n'a jamais été payée ni comptabilisée.

## 2. Calculs (détaillés, chaque montant justifié)

**Rapprochement des soldes**

| | Montant |
|---|---|
| Solde comptable créditeur au 05/10/2026 | 4 620,00 € |
| – Doublon F 2026-352 (AC-0821) | – 2 340,00 € |
| + Facture 2026-372 non comptabilisée | + 396,00 € |
| **= Solde corrigé** | **2 676,00 €** |
| Solde selon relevé fournisseur | 2 676,00 € |
| Écart | **0,00 €** ✓ |

Décomposition du solde corrigé : F 2026-372 (396,00 €, échue) + F 2026-441 (2 280,00 €, non échue) = 2 676,00 € ✓.

**TVA** : TVA déduite deux fois sur la facture 352 = **390,00 €** (1 950,00 × 20 %) ; TVA déductible omise sur la facture 372 = **66,00 €** (330,00 × 20 %).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 09/10/2026 | AC | 401BLAN | Fournisseur Blanchisserie du Gourguillon | Extourne doublon F 2026-352 (AC-0821) | 2 340,00 | |
| 09/10/2026 | AC | 6155 | Entretien sur biens mobiliers – blanchissage | Extourne doublon F 2026-352 (AC-0821) | | 1 950,00 |
| 09/10/2026 | AC | 44566 | TVA déductible sur ABS | Extourne doublon F 2026-352 (AC-0821) | | 390,00 |
| 12/10/2026 | AC | 6155 | Entretien sur biens mobiliers – blanchissage | Blanchisserie F 2026-372 banquet 15/08 | 330,00 | |
| 12/10/2026 | AC | 44566 | TVA déductible sur ABS | Blanchisserie F 2026-372 banquet 15/08 | 66,00 | |
| 12/10/2026 | AC | 401BLAN | Fournisseur Blanchisserie du Gourguillon | Blanchisserie F 2026-372 banquet 15/08 | | 396,00 |
| | | | | **Totaux** | **2 736,00** | **2 736,00** |

> L'extourne est passée **au même journal** que l'écriture d'origine (AC), avec un libellé qui cite la pièce extournée : la piste d'audit reste lisible. La facture 372 est enregistrée à la date de **réception de la copie** (12/10), avec sa date de pièce du 17/08 ; dans le FEC, PieceDate = 17/08/2026.

**Compte 401BLAN après corrections et lettrage**

| Date | Pièce | Débit | Crédit | Let. |
|---|---|---|---|---|
| 05/07 | F 2026-311 | | 1 860,00 | A |
| 10/07 | Vir. | 1 860,00 | | A |
| 04/08 | F 2026-352 (AC-0803) | | 2 340,00 | B |
| 06/08 | F 2026-352 (AC-0821, doublon) | | 2 340,00 | D |
| 20/08 | Vir. acompte | 1 500,00 | | B |
| 03/09 | F 2026-398 | | 2 610,00 | C |
| 08/09 | AV 2026-021 | 210,00 | | C |
| 15/09 | Vir. | 840,00 | | B |
| 25/09 | Vir. | 2 400,00 | | C |
| 02/10 | F 2026-441 | | 2 280,00 | — |
| 09/10 | Extourne doublon | 2 340,00 | | D |
| 12/10 | F 2026-372 (pièce du 17/08) | | 396,00 | — |
| | **Solde créditeur** | | **2 676,00** | |

**Question 5 — si la copie de la facture 372 n'est pas reçue au 31/10/2026** : la prestation a été rendue (mariage du 15/08) et la dette est certaine (relevé du fournisseur). On constate une **facture non parvenue** :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6155 | Entretien sur biens mobiliers – blanchissage | FNP Blanchisserie F 2026-372 banquet | 330,00 | |
| 31/10/2026 | OD | 44586 | Taxes sur factures non parvenues | FNP Blanchisserie F 2026-372 banquet | 66,00 | |
| 31/10/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Blanchisserie F 2026-372 banquet | | 396,00 |
| | | | | **Totaux** | **396,00** | **396,00** |

Écriture extournée au 01/11/2026. La TVA en 44586 **n'est pas déductible** tant que la facture n'est pas détenue.

## 4. Points d'attention / pièges

- **La TVA (question 4).** La TVA d'août a été surévaluée de 390,00 € (doublon). On régularise sur la **CA3 d'octobre** (déposée en novembre) en diminuant la TVA déductible du mois ; la TVA de 66,00 € de la facture 372 est déductible sur la CA3 du mois au cours duquel l'hôtel **détient la facture** (octobre). Si le montant était significatif, on pourrait aussi déposer une déclaration rectificative du mois d'août — à arbitrer avec Hélène Ferrand (intérêts de retard possibles sur un rappel de TVA).
- **Ne jamais lettrer le doublon avec un paiement** pour « faire tomber » le compte : ce serait masquer une charge en double et une TVA déduite deux fois.
- **Lettrer au montant sans lire** : le virement de 840,00 € ne correspond à aucune facture isolée ; il ne se comprend qu'avec le virement « acompte » de 1 500,00 €.
- **Pénalités de retard** : la facture 372 est échue depuis le 16/09. Le fournisseur pourrait facturer des pénalités et l'indemnité de 40 € ; un appel courtois en expliquant la situation suffit généralement.
- **Clôture au 31/10** : c'est maintenant qu'il faut obtenir les relevés fournisseurs, pas en décembre.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Message à Olivier Garnier :**

> Bonjour Monsieur Garnier,
>
> Bonne nouvelle : vous avez bien réglé toutes les factures de la blanchisserie que nous avions. Deux points cependant :
> 1. la facture 2026-352 avait été enregistrée deux fois (une fois par notre outil de lecture automatique, une fois manuellement à la réception). Nous l'avons corrigé ; la TVA récupérée en trop (390 €) sera régularisée sur la déclaration d'octobre ;
> 2. la blanchisserie vous a facturé **396 €** le 17/08 pour le linge du mariage du 15/08 (facture 2026-372). Nous ne l'avons jamais reçue — sans doute est-elle restée au service banquets. Elle est échue depuis le 16/09 : pouvez-vous la faire régler et nous en transmettre une copie ?
>
> Pour éviter les doublons, merci de demander à la réception de ne plus saisir de factures manuellement : il suffit de les déposer sur la plateforme.

**Mesures (question 6) :**
- **une seule porte d'entrée** pour les factures : la plateforme de dématérialisation (et, pour les fournisseurs GE/ETI, la PA) ; suppression des droits de saisie manuelle de la réception ;
- activer dans le logiciel le **contrôle des doublons** (même tiers + même n° de facture) ;
- demander aux **10 principaux fournisseurs** un relevé de compte au 31/10 (circularisation « allégée ») ;
- remonter le circuit des factures « banquets / événements », qui échappent souvent au circuit habituel.

**Documentation** : feuille de travail « Rapprochement 401BLAN » avec le relevé fournisseur en annexe, conservée dans le dossier de révision de la clôture 31/10/2026.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce art. L. 123-14 et PCG : principes de régularité et de sincérité ; une dette doit être comptabilisée pour son montant réel.
- PCG : comptes 408 « Fournisseurs – Factures non parvenues » et 44586 « Taxes sur le chiffre d'affaires sur factures non parvenues ».
- CGI art. 271 : la TVA n'est déductible qu'une fois, sur présentation d'une facture conforme détenue par l'assujetti.
- CGI art. 1727 : intérêts de retard en cas de rappel de TVA.
- Code de commerce art. L. 441-10 : pénalités de retard et indemnité forfaitaire de 40 €.
