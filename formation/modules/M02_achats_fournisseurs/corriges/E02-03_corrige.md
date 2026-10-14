# Corrigé E02-03 — Acompte versé à un bureau d'études, puis facture finale à cheval sur la clôture

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-03](../exercices/E02-03_acompte-verse-atelier-ligne.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Règle clé : le droit à déduction naît lorsque la TVA devient exigible chez le fournisseur** (CGI art. 271-I-2).
- Structura réalise une **prestation de services** ; ses factures ne portent **pas** la mention de l'option pour les débits. Sa TVA est donc exigible **à l'encaissement** (CGI art. 269-2-c).
- Conséquence chez Atelier Ligne : la TVA n'est déductible **qu'au moment du paiement** (et à condition de détenir la facture).

| Facture | Paiement | TVA déductible | CA3 |
|---|---|---|---|
| Acompte BS-2026-0614 : 720,00 € | 22/06/2026 | 720,00 € | **Juin 2026** |
| Finale BS-2026-0931 : 2 400,00 € de TVA totale, dont 720,00 € déjà déduits → **1 680,00 €** restant | 20/10/2026 | 1 680,00 € | **Octobre 2026** (exercice suivant) |

**La saisie de juin** : le résultat est juste (TVA de 720,00 € déduite en juin, le mois du paiement), mais la méthode court-circuite le compte fournisseur (la facture d'acompte n'apparaît pas en 401). Elle est acceptable pour un acompte payé immédiatement ; la méthode du dossier (réception → 401 avec TVA en attente → paiement → transfert) est plus rigoureuse et identique pour toutes les factures de services. Pour la suite de l'exercice, on la reprend selon la méthode du dossier.

**Charge et TVA n'ont pas le même calendrier** : la **charge** de 12 000,00 € HT appartient à l'exercice clos le 30/09/2026 (prestation achevée le 18/09, facture reçue le 20/09) ; la **TVA** de la facture finale ne sera déductible qu'en octobre 2026. Nicolas ne peut donc pas l'inscrire sur la CA3 de septembre.

**Compte retenu** : 604 « Achats d'études et prestations de services », car l'étude structure est **incorporée** à la mission d'architecture vendue au client (le compte 611 « Sous-traitance générale » est aussi rencontré dans la pratique ; l'essentiel est la constance).

## 2. Calculs (détaillés, chaque montant justifié)

| | HT | TVA 20 % | TTC |
|---|---|---|---|
| Prix total (devis DV-26-077) | 12 000,00 € | 2 400,00 € | 14 400,00 € |
| Acompte 30 % | 12 000,00 × 30 % = 3 600,00 € | 720,00 € | 4 320,00 € |
| Solde | 8 400,00 € | **1 680,00 €** | **10 080,00 €** |

Contrôle : 14 400,00 – 4 320,00 = 10 080,00 € ✓ ; 2 400,00 – 720,00 = 1 680,00 € ✓.

## 3. Écritures comptables

Écritures selon la méthode du dossier (la saisie de juin est remplacée par les trois premières lignes de juin ci-dessous — en pratique, on ne la contre-passe que si elle n'a pas été validée ; sinon on la conserve, le résultat étant identique).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/06/2026 | AC | 4091 | Fournisseurs – avances et acomptes versés | Structura F acompte BS-2026-0614 30 % | 3 600,00 | |
| 15/06/2026 | AC | 445669 | TVA déductible en attente de paiement | Structura F acompte BS-2026-0614 | 720,00 | |
| 15/06/2026 | AC | 401STRU | Fournisseur BET Structura | Structura F acompte BS-2026-0614 | | 4 320,00 |
| 22/06/2026 | BQ | 401STRU | Fournisseur BET Structura | Vir. Structura acompte BS-2026-0614 | 4 320,00 | |
| 22/06/2026 | BQ | 512 | Banque | Vir. Structura acompte BS-2026-0614 | | 4 320,00 |
| 22/06/2026 | OD | 44566 | TVA déductible sur ABS | TVA déductible au paiement BS-2026-0614 | 720,00 | |
| 22/06/2026 | OD | 445669 | TVA déductible en attente de paiement | TVA déductible au paiement BS-2026-0614 | | 720,00 |
| 20/09/2026 | AC | 604 | Achats d'études et prestations de services | Structura F BS-2026-0931 étude structure Terrasses de Saône | 12 000,00 | |
| 20/09/2026 | AC | 445669 | TVA déductible en attente de paiement | Structura F BS-2026-0931 TVA sur solde | 1 680,00 | |
| 20/09/2026 | AC | 4091 | Fournisseurs – avances et acomptes versés | Structura F BS-2026-0931 imputation acompte BS-2026-0614 | | 3 600,00 |
| 20/09/2026 | AC | 401STRU | Fournisseur BET Structura | Structura F BS-2026-0931 net à payer | | 10 080,00 |
| 20/10/2026 | BQ | 401STRU | Fournisseur BET Structura | Vir. Structura solde BS-2026-0931 | 10 080,00 | |
| 20/10/2026 | BQ | 512 | Banque | Vir. Structura solde BS-2026-0931 | | 10 080,00 |
| 20/10/2026 | OD | 44566 | TVA déductible sur ABS | TVA déductible au paiement BS-2026-0931 | 1 680,00 | |
| 20/10/2026 | OD | 445669 | TVA déductible en attente de paiement | TVA déductible au paiement BS-2026-0931 | | 1 680,00 |
| | | | | **Totaux** | **34 800,00** | **34 800,00** |

**Soldes au 30/09/2026 (question 3)**

| Compte | Solde | Commentaire |
|---|---|---|
| 4091 | 0,00 € | L'acompte est imputé sur la facture finale : un 4091 non soldé alors que la prestation est terminée est une anomalie classique de révision |
| 401STRU | 10 080,00 € créditeur | Dette réelle au 30/09 (échéance 20/10) |
| 445669 | 1 680,00 € débiteur | TVA **non encore déductible** : elle figure au bilan (créance sur l'État « en attente »), pas sur la CA3 de septembre |
| 604 | 12 000,00 € | Charge de l'exercice 2025-2026 (prestation achevée le 18/09) |

## 4. Points d'attention / pièges

- **Ne pas confondre** la date de déduction de la TVA (paiement, pour un service sans option débits) et la date de rattachement de la charge (réalisation du service).
- **L'acompte n'est pas une charge** : il reste en 4091 tant que la prestation n'est pas réalisée. Si la note de calcul n'avait été remise qu'en octobre, le 4091 de 3 600,00 € serait resté à l'actif au 30/09 et aucune charge ne serait constatée.
- **Ne pas déduire deux fois la TVA de l'acompte** : la facture finale affiche 2 400,00 € de TVA, mais 720,00 € ont déjà été déduits. Seuls 1 680,00 € restent à déduire.
- **Achats de biens** (ordinateurs, mobilier) : la TVA est déductible dès la facture (exigibilité à la livraison, ou à l'encaissement de l'acompte pour un acompte). Le raisonnement « au paiement » ne vaut que pour les **services** sans option débits.
- **Question 4 — mention de l'option pour les débits** : si Structura avait opté, sa TVA serait exigible à la **facturation** ; Atelier Ligne pourrait déduire 720,00 € dès réception de la facture d'acompte (juin) et **1 680,00 € dès la facture finale du 20/09**, donc sur la **CA3 de septembre 2026**. C'est exactement pour cela que cette mention devient obligatoire avec la réforme de la facturation électronique : le client sait, à la lecture de la facture, quand il peut déduire.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse à Nicolas Brun (question 5) :**

> Bonjour Nicolas,
>
> Pour Structura :
> - la TVA de l'acompte (720 €) a bien été déduite en juin, au moment où vous l'avez payé : c'est correct ;
> - la TVA de la facture finale (1 680 € restant à déduire) **ne peut pas** figurer sur la déclaration de septembre : Structura n'a pas opté pour les débits, sa TVA n'est due qu'à l'encaissement, et vous ne pouvez la déduire que lorsque vous payez. Elle ira sur la déclaration d'**octobre**, après votre virement du 20/10 ;
> - en revanche, la prestation (12 000 € HT) est bien une charge de l'exercice clos le 30/09, puisque l'étude a été rendue le 18/09.
>
> Bonne nouvelle pour vos propres factures : c'est la même règle pour vos clients — vous ne reversez la TVA de vos honoraires qu'à l'encaissement.

**Contrôles de révision** :
- balayage du 4091 au 30/09 : chaque acompte doit correspondre à une commande **non encore livrée** ; sinon, rechercher la facture finale ;
- balayage du 445669 : il doit correspondre exactement à la TVA des factures de services non payées (rapprochement avec la balance âgée fournisseurs) ;
- **en-cours** : l'étude Structura se rattache à la mission « Les Terrasses de Saône » ; si la phase correspondante n'est pas encore facturée au client, la charge entre dans l'évaluation des **en-cours de production de services** au 30/09 (voir module stocks et en-cours).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 269-2-c : exigibilité de la TVA sur les prestations de services à l'encaissement, sauf option pour les débits.
- CGI art. 271-I-2 : le droit à déduction prend naissance lorsque la taxe devient exigible chez le redevable.
- CGI, annexe II, art. 242 nonies A : mention de l'option pour les débits (renforcée par la réforme de la facturation électronique).
- PCG : compte 4091 « Fournisseurs – Avances et acomptes versés sur commandes » ; compte 604.
- BOFiP, TVA – Droits à déduction – naissance du droit à déduction.
