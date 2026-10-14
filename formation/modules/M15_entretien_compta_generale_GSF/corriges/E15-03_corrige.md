# Corrigé E15-03 — Lettrage et justification d'un compte fournisseur et d'un compte client

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-03](../exercices/E15-03_lettrage-justification-fournisseur-client.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Rappel : à quoi sert le lettrage ?

Le lettrage permet de savoir, à tout moment, **quelles factures restent ouvertes**. Un compte de tiers bien lettré se justifie en une ligne : « le solde = la liste des pièces non lettrées ». C'est ce que le chef comptable vérifie.

Sens normal des soldes :
- un **fournisseur (401)** est normalement **créditeur** : GSF Riviera lui doit de l'argent ;
- un **client (411)** est normalement **débiteur** : il doit de l'argent à GSF Riviera.

Un solde dans l'autre sens est dit **anormal** : il cache presque toujours une erreur (doublon, mauvais compte) ou une situation à régler (trop-perçu, avoir non utilisé).

### Question 1 — Lettrage du compte 401AZH

| Date | Pièce | Libellé | Débit | Crédit | Lettre | Commentaire |
|---|---|---|---|---|---|---|
| 02/09 | AC-0905 | F26-1101 | | 1 479,00 | A | |
| 30/09 | BQ-0929 | VIR règlement F26-1101 | 1 479,00 | | A | lettrage **total** (1 479,00 − 1 479,00 = 0) |
| 09/09 | AC-0912 | F26-1130 | | 2 160,00 | b | |
| 02/10 | AC-1002 | Avoir AV-0412 | 144,00 | | b | |
| 05/10 | BQ-1003 | VIR règlement partiel | 1 000,00 | | b | lettrage **partiel** : reste 1 016,00 |
| 11/09 | AC-0918 | F26-1130 (2ᵉ saisie) | | 2 160,00 | — | **doublon** → à annuler, puis lettrer avec l'écriture d'annulation (C) |
| 06/10 | AC-1006 | F26-1188 | | 864,00 | — | ouverte, non échue |

(Convention fréquente : majuscule = lettrage total, minuscule = lettrage partiel. Suivez le paramétrage du logiciel.)

### Question 2 — Écart de 2 160,00 € avec le fournisseur

Écart : 4 040,00 − 1 880,00 = **2 160,00 €**, soit exactement le montant de F26-1130. Le fournisseur n'a émis F26-1130 **qu'une fois** ; chez nous, elle apparaît **deux fois** (pièces AC-0912 du 09/09 et AC-0918 du 11/09, même numéro, même montant). C'est un **doublon de saisie** : la facture est arrivée deux fois (par exemple par la plateforme et par mail) et a été saisie deux fois.

Conséquences du doublon :
- la dette fournisseur est surévaluée de 2 160,00 € ;
- la charge 6063 est surévaluée de 1 800,00 € ;
- la **TVA déductible** est surévaluée de 360,00 € — et si la CA3 de septembre a déjà été déposée, GSF Riviera a **déduit 360,00 € de trop**. L'annulation en octobre réduit la TVA déductible d'octobre : la correction se fait ainsi sur la CA3 suivante.

**Justification du solde exact (après correction) :**

| Facture | Montant TTC | Déjà réglé / imputé | Reste dû |
|---|---|---|---|
| F26-1130 | 2 160,00 | avoir 144,00 + virement 1 000,00 | 1 016,00 |
| F26-1188 | 864,00 | — | 864,00 |
| **Total** | | | **1 880,00** |

1 880,00 € = solde du relevé fournisseur ✓. L'avoir AV-0412 est enregistré chez nous mais **pas encore imputé** sur un paiement : il faut l'utiliser au prochain règlement de F26-1130 (payer 1 016,00 € et non 1 160,00 €).

### Question 3 — Compte client 411HBR

| Date | Pièce | Libellé | Débit | Crédit | Lettre |
|---|---|---|---|---|---|
| 31/08 | VT-0831 | FV-2026-0815 | 3 600,00 | | A |
| 12/09 | BQ-0909 | VIR Hôtel Bellevue | | 3 600,00 | A (total) |
| 30/09 | VT-0930 | FV-2026-0921 | 3 600,00 | | b |
| 12/10 | BQ-1008 | VIR réf. FV-2026-0921 | | 3 600,00 | b |
| 05/10 | VT-1001 | Avoir AV-V-0031 | | 360,00 | non lettré |

Le client a payé FV-2026-0921 pour son montant **total** (3 600,00 €) **sans déduire l'avoir** de 360,00 € qu'on lui avait accordé. Résultat : GSF Riviera **doit 360,00 €** au client : le compte client est **créditeur**. Ce n'est pas une erreur comptable (les écritures sont justes), c'est une **situation à régler** avec le client :
- **solution simple** (la plus courante) : avec l'accord du client, **déduire l'avoir de la prochaine facture** (octobre) → aucune écriture supplémentaire, on lettrera l'avoir avec la facture d'octobre ;
- ou **rembourser** 360,00 € par virement (411HBR au débit, 512 au crédit), si le client le demande.

À la clôture de l'exercice, un client créditeur ne doit pas être laissé en diminution des créances : il est présenté au passif (clients créditeurs — compte 419) ; *le reclassement est fait par l'équipe de clôture*.

### Question 4 — Comptes 401MNE et 401MNT

Les deux comptes portent **le même SIREN** (999 300 226) : c'est le même fournisseur, créé **deux fois** dans le fichier des tiers (le 29/09, quelqu'un a créé « Machines Nett SARL » au lieu de rechercher « Machines Nett' »). La facture MN-4410 a été saisie sur le nouveau compte, le paiement sur l'ancien : chaque compte est faux, mais **l'ensemble est juste** (283,20 − 283,20 = 0). L'anomalie se voit au **solde débiteur** du 401MNE : on aurait « payé d'avance » un fournisseur, ce qui n'est pas le cas.

Correction : on **transfère** le solde d'un compte vers l'autre, puis on lettre facture et paiement dans le bon compte (401MNE, le compte historique), et on demande la **désactivation** du compte 401MNT.

## 2. Calculs (détaillés, chaque montant justifié)

- Solde 401AZH avant correction : crédits 1 479,00 + 2 160,00 + 2 160,00 + 864,00 = 6 663,00 ; débits 1 479,00 + 144,00 + 1 000,00 = 2 623,00 ; solde créditeur 6 663,00 − 2 623,00 = **4 040,00**.
- Doublon F26-1130 : HT 1 800,00 ; TVA 1 800,00 × 20 % = 360,00 ; TTC 2 160,00.
- Solde après correction : 4 040,00 − 2 160,00 = **1 880,00** ✓ (= relevé fournisseur).
- Reste dû sur F26-1130 : 2 160,00 − 144,00 − 1 000,00 = **1 016,00**.
- Client 411HBR : débits 3 600,00 + 3 600,00 = 7 200,00 ; crédits 3 600,00 + 360,00 + 3 600,00 = 7 560,00 ; solde créditeur **360,00**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 13/10/2026 | AC | 401AZH | Fournisseur Azur Hygiène Distribution | Annulation doublon F26-1130 (pièce AC-0918) | 2 160,00 | |
| 13/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | Annulation doublon F26-1130 (pièce AC-0918) | | 1 800,00 |
| 13/10/2026 | AC | 44566 | TVA déductible sur autres biens et services | Annulation doublon F26-1130 – TVA | | 360,00 |
| 13/10/2026 | OD | 401MNT | Fournisseur Machines Nett SARL (compte créé en double) | Transfert MN-4410 vers 401MNE – tiers en double | 283,20 | |
| 13/10/2026 | OD | 401MNE | Fournisseur Machines Nett' | Transfert MN-4410 depuis 401MNT – tiers en double | | 283,20 |
| | | | | **Totaux** | **2 443,20** | **2 443,20** |

**Pourquoi ces sens ?**
- L'annulation d'une facture d'achat est l'**inverse** de la facture : le fournisseur (crédité à la facture) est **débité**, la charge et la TVA (débitées à la facture) sont **créditées**.
- Pour le transfert, on « vide » 401MNT (créditeur → on le **débite**) et on porte la facture au 401MNE (→ **crédit**). Le 401MNE est alors soldé : 283,20 au débit (paiement) et 283,20 au crédit (facture) → lettrage total.

Après correction : 401AZH créditeur de 1 880,00 € ; 401MNE et 401MNT soldés ; 411HBR créditeur de 360,00 € (à régler avec le client, pas d'écriture).

## 4. Points d'attention / pièges

- **Doublon** : on ne supprime pas la ligne en double, on l'**annule par une écriture** (traçabilité). Contrôle préventif : même fournisseur + même numéro de facture = blocage dans le logiciel.
- **TVA du doublon** : penser à la CA3 ; la TVA déduite deux fois doit être reversée (ici, automatiquement via la CA3 d'octobre).
- **Paiement partiel** : lettrage **partiel**, jamais de lettrage forcé avec un écart.
- **Avoir non imputé** (fournisseur comme client) : il doit être suivi, sinon on paie trop (fournisseur) ou le client attend son argent (client).
- **Solde anormal** : toujours l'expliquer. Un 401 débiteur peut aussi être un acompte versé (normal, mais alors en 4091) ou un paiement en double (à réclamer au fournisseur).

## 5. Ce que le recruteur attend / ce qu'un senior ferait en plus

**Question 6 — Mail au fournisseur :**

> Objet : Relevé de compte au 13/10/2026 — GSF Riviera SAS (Nice)
>
> Bonjour,
>
> Merci pour votre relevé. Après rapprochement, nous trouvons comme vous un solde de **1 880,00 €** :
> - F26-1130 (2 160,00 €) : nous avons réglé 1 000,00 € le 05/10 dans l'attente de votre avoir pour les produits non conformes. Votre avoir AV-0412 (144,00 €) étant reçu, le solde de **1 016,00 €** sera réglé lors de notre prochain règlement fournisseurs ;
> - F26-1188 (864,00 €) : réglée à son échéance contractuelle.
>
> Pour faciliter nos échanges, merci de nous adresser vos factures uniquement via la plateforme de facturation électronique.
>
> Cordialement,
> Service comptabilité fournisseurs — GSF Riviera SAS

(On n'explique pas au fournisseur notre doublon interne : c'est une correction chez nous seulement.)

**Autres réflexes attendus :**
- Prévenir la personne chargée du **fichier tiers** : rechercher un fournisseur **par SIREN** avant toute création ; désactiver 401MNT.
- Prévenir le commercial ou l'établissement pour l'**Hôtel Bellevue** : « l'avoir de 360,00 € sera déduit de la facture d'octobre, merci de le confirmer au client ».
- Mettre en place un **rapprochement régulier** des relevés fournisseurs (au moins pour les principaux fournisseurs) : c'est ainsi qu'on détecte les doublons et les factures non reçues.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 401, 4091, 411, 419, 44566, 6063 ; correction des erreurs par écriture (pas d'effacement d'une écriture validée).
- Code de commerce art. L. 123-14 (comptes réguliers et sincères) et art. L. 441-10 (délais de paiement).
- CGI art. 271 (déduction de la TVA ; une même facture ne donne droit qu'à une seule déduction).
