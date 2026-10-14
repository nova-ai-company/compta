# Corrigé E14-17 — Intra-groupe : management fees, convention de trésorerie (cash pooling) et rapprochement des comptes réciproques

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-17](../exercices/E14-17_intragroupe-management-fees-cash-pooling-reciproques.md)

*Rappel : conventions, taux et montants fictifs ; pas de groupe TVA (hypothèse).*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Recalcul
- **Management fees T3** : 4 812 000,00 × 2,5 % = **120 300,00 € HT** ; TVA 20 % = 24 060,00 € ; TTC **144 360,00 €** ✓ (le siège a correctement facturé).
- **Intérêts T3** : la convention impose la base **exact/365** : 1 850 000,00 × 3,10 % × 92/365 = **14 455,34 €**. Le siège a calculé en base 360 (14 656,11 €) : **le siège a tort**, de 200,77 €. Un écart de cette nature (rapport 365/360, soit + 1,39 %) est la signature d'une erreur de base de calcul.

### Question 2 — Les écarts

| Écart | Montant | Nature | Origine | Qui corrige |
|---|---|---|---|---|
| Facture management fees | 144 360,00 | **Temporel / omission** | Facture datée du 30/09, reçue le 05/10, non saisie par Riviera | **GSF Riviera** : saisie en septembre (date de facture, période ouverte jusqu'à J+5) |
| Remontée de trésorerie | 45 000,00 | **Temporel / erreur de date** | Opération du 28/09 enregistrée le 01/10 par Riviera | **GSF Riviera** : enregistrement au 28/09 et annulation de la saisie du 01/10 |
| Intérêts | 200,77 | **Erreur de calcul** | Base 360 au lieu de 365 | **Siège** |

Principe : **chaque société corrige ses propres erreurs** ; on ne « force » jamais l'égalité chez l'une pour masquer l'erreur de l'autre, et on n'ajuste pas l'écart en consolidation sans écriture dans les comptes individuels.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Management fees HT | 4 812 000,00 × 2,5 % | 120 300,00 € |
| TVA | 120 300,00 × 20 % | 24 060,00 € |
| TTC | | 144 360,00 € |
| Intérêts convention (365) | 1 850 000,00 × 3,10 % × 92/365 | 14 455,34 € |
| Intérêts siège (360) | 1 850 000,00 × 3,10 % × 92/360 | 14 656,11 € |
| Écart d'intérêts | 14 656,11 − 14 455,34 | 200,77 € |
| Écart total compte courant | 45 000,00 + 200,77 | 45 200,77 € ✓ |

**Après corrections (question 4)** :

| Compte | Avant | Correction | Après |
|---|---|---|---|
| Siège 451GSFR (créditeur) | 1 927 106,11 | − 200,77 | **1 926 905,34** |
| Riviera 451GSF (débiteur) | 1 881 905,34 | + 45 000,00 | **1 926 905,34** ✓ |
| Siège 411GSFR (débiteur) | 144 360,00 | — | **144 360,00** |
| Riviera 401GSF (créditeur) | 0,00 | + 144 360,00 | **144 360,00** ✓ |

Et en résultat : charge d'intérêts du siège 14 455,34 € = produit d'intérêts de Riviera 14 455,34 € ✓ ; produit de management fees du siège 120 300,00 € = charge de Riviera 120 300,00 € ✓ (éliminés en consolidation).

## 3. Écritures comptables

**Chez GSF Riviera**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 6228 | Rémunérations d'intermédiaires et honoraires – frais de siège | GSF F GSF-MF-2026-T3-021 management fees T3 | 120 300,00 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | GSF F GSF-MF-2026-T3-021 TVA 20 % | 24 060,00 | |
| 30/09/2026 | AC | 401GSF | Fournisseur groupe – GSF | GSF F GSF-MF-2026-T3-021 | | 144 360,00 |
| 28/09/2026 | BQ | 451GSF | Groupe – compte courant de trésorerie (siège) | Remontée cash pooling 28/09 | 45 000,00 | |
| 28/09/2026 | BQ | 512 | Banque | Remontée cash pooling 28/09 | | 45 000,00 |
| 01/10/2026 | BQ | 512 | Banque | Annulation saisie 01/10 remontée du 28/09 (doublon) | 45 000,00 | |
| 01/10/2026 | BQ | 451GSF | Groupe – compte courant de trésorerie (siège) | Annulation saisie 01/10 remontée du 28/09 (doublon) | | 45 000,00 |
| | | | | **Totaux** | **234 360,00** | **234 360,00** |

**Au siège**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 451GSFR | Groupe – compte courant GSF Riviera | Correction intérêts cash pooling T3 base 365 | 200,77 | |
| 30/09/2026 | OD | 6615 | Intérêts des comptes courants et des dépôts créditeurs | Correction intérêts cash pooling T3 base 365 | | 200,77 |
| | | | | **Totaux** | **200,77** | **200,77** |

> Pour mémoire, l'écriture d'intérêts correcte chez Riviera (déjà passée) : D 451GSF 14 455,34 / C 763 14 455,34 ; au siège, après correction : charge 6615 nette de 14 455,34 €.
> Si la période de septembre de GSF Riviera était déjà clôturée, la remontée resterait au 01/10 et l'écart de 45 000,00 € serait documenté comme **écart temporel** (« cash in transit ») dans l'outil de consolidation ; ici, la période étant ouverte jusqu'à J+5, on corrige à la bonne date.

## 4. Points d'attention / pièges

- **Ne pas saisir une facture intra-groupe à sa date de réception** quand la convention de clôture du groupe veut qu'elle soit dans le même mois chez l'émetteur et le récepteur : c'est la première cause d'écarts réciproques.
- **TVA** : hors groupe TVA, les management fees sont des prestations de services taxables (TVA collectée par le siège, déductible chez Riviera). **Avec un groupe TVA** (assujetti unique, possible depuis 2023), les opérations entre membres sont **hors champ** : facture sans TVA, et le paramétrage ERP doit en tenir compte (*appartenance au groupe TVA à vérifier*).
- **Intérêts** : pas de TVA (opérations financières exonérées, sauf option). Le compte courant de trésorerie se présente en « autres créances / autres dettes » (ou disponibilités selon l'analyse retenue par le groupe — à vérifier dans le manuel comptable du groupe).
- **Base de calcul** : exact/365, exact/360, 30/360… se lit dans la convention ; c'est un contrôle simple à faire à chaque trimestre.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Vigilance fiscale et juridique (question 5)** :
- **Management fees** : déductibles chez la filiale seulement s'ils rémunèrent des **services réels**, utiles à la filiale, à un **prix de pleine concurrence** ; documentation des prix de transfert (clé de répartition, coûts du siège, marge) ; une clé « % du chiffre d'affaires » doit pouvoir être justifiée par les coûts réels du siège. Sinon : risque de requalification (acte anormal de gestion, distribution).
- **Intérêts de compte courant** : chez le débiteur (ici le siège), déductibilité limitée au taux fixé par l'article 39-1-3° du CGI (ou à un taux de pleine concurrence justifié), et règles de limitation des charges financières nettes (art. 212 bis) ; chez le prêteur, produit imposable.
- **Conventions réglementées** : selon la forme et la gouvernance (SAS), les conventions entre sociétés ayant des dirigeants communs peuvent relever de la procédure des conventions réglementées (exceptions pour les conventions courantes conclues à des conditions normales et pour les filiales détenues à 100 % — *à vérifier*).
- **Intégration fiscale** (probable dans le groupe, *à vérifier*) : n'efface ni la TVA, ni la nécessité de documenter les prix.

**Mail au service consolidation (07/10)** :
> Comptes réciproques GSF Riviera / GSF au 30/09 : (1) facture de management fees T3 (144 360,00 €) saisie chez Riviera au 30/09 ; (2) remontée de trésorerie du 28/09 (45 000,00 €) enregistrée à sa date réelle chez Riviera ; (3) intérêts de cash pooling T3 : erreur de base au siège (360 au lieu de 365, 200,77 €), corrigée par le siège. Après corrections, comptes courants à 1 926 905,34 € et créance/dette de management fees à 144 360,00 € des deux côtés.

**Contrôle préventif** : calendrier intra-groupe (factures intra-groupe émises au plus tard J-2 de la fin du mois, « cut-off » commun), tableau de rapprochement mensuel automatique, calcul des intérêts par un outil unique pour les deux côtés.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 39-1-1° et 57 (déductibilité, prix de transfert), 39-1-3° et 212 bis (intérêts), 256 C (groupe TVA — assujetti unique).
- CGI art. 261 C : exonération des opérations financières (intérêts).
- Code de commerce art. L. 227-10 (conventions réglementées en SAS) (*à vérifier*).
- PCG : comptes 451, 6615, 763 ; règlement ANC relatif aux comptes consolidés (élimination des opérations réciproques) (*référence à vérifier*).
