# Corrigé E02-02 — Un avoir pour retour et rabais… un peu trop généreux

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-02](../exercices/E02-02_avoir-retour-mode-co.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Contrôle de la facture** : 200 × 18,50 = 3 700,00 ; 150 × 22,00 = 3 300,00 ; 100 × 26,40 = 2 640,00 ; brut 9 640,00 ; remise 5 % = 482,00 ; net 9 158,00 ; TVA 1 831,60 ; TTC 10 989,60 € ✓. Mentions complètes (adresse de livraison différente indiquée, n° de commande, nature de l'opération, SIREN client).

**Contrôle de l'avoir** — un avoir doit remettre l'acheteur dans la situation **exacte** où il serait si l'opération n'avait pas eu lieu (retour) ou si le prix avait été réduit (rabais) :
- **Rabais pantalons** : 10 % de la base **nette** 3 135,00 € (3 300,00 × 95 %) = 313,50 € ✓.
- **Retour des robes** : les robes ont été facturées **26,40 € brut, moins 5 % de remise**, soit 25,08 € net pièce. L'avoir les reprend à **26,40 €** : il oublie la remise. Retour correct : 20 × 25,08 = **501,60 € HT**, et non 528,00 €.

L'erreur est de **26,40 € HT** (+ 5,28 € de TVA = **31,68 € TTC**), **en faveur de Mode & Co**. Elle n'est pas « gratuite » : la TVA déductible serait minorée de 5,28 € de trop chez Mode & Co et la TVA collectée minorée d'autant chez le fournisseur ; le compte fournisseur de Mode & Co ne correspondrait pas au compte client chez Textiles Lumière… et le fournisseur s'en apercevra tôt ou tard (contrôle de marge, audit). La bonne pratique professionnelle est de le signaler.

**Pourquoi deux comptes différents (question 2) ?**
- Le **retour** annule une partie de l'**achat** lui-même : les robes ne font plus partie des achats → **crédit 607**.
- Le **rabais** est une **réduction de prix** sur des marchandises conservées → **6097 « RRR obtenus sur achats de marchandises »**. Cela permet de suivre les réductions obtenues (outil de négociation fournisseur) et de calculer un coût d'achat net cohérent.

## 2. Calculs (détaillés, chaque montant justifié)

| | HT | TVA 20 % | TTC |
|---|---|---|---|
| Retour selon l'avoir : 20 × 26,40 | 528,00 € | | |
| Retour correct : 20 × 26,40 × 95 % | 501,60 € | | |
| Rabais : 3 300,00 × 95 % × 10 % | 313,50 € | | |
| **Avoir reçu** | 841,50 € | 168,30 € | 1 009,80 € |
| **Avoir correct** | 815,10 € | 163,02 € | 978,12 € |
| **Écart (en faveur de Mode & Co)** | **26,40 €** | **5,28 €** | **31,68 €** |

**Montant à payer le 02/10 (question 5)** : 10 989,60 – 1 009,80 + 31,68 = **10 011,48 €**.
Contrôle : 10 989,60 – 978,12 (avoir correct) = 10 011,48 € ✓.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 18/09/2026 | AC | 401TEXL | Fournisseur Textiles Lumière | Textiles Lumière AV AV-26-0087 s/ FA-26-0912 | 1 009,80 | |
| 18/09/2026 | AC | 607 | Achats de marchandises | AV-26-0087 retour 20 robes défaut couture | | 528,00 |
| 18/09/2026 | AC | 6097 | RRR obtenus sur achats de marchandises | AV-26-0087 rabais 10 % retard chinos | | 313,50 |
| 18/09/2026 | AC | 44566 | TVA déductible sur ABS | AV-26-0087 TVA | | 168,30 |
| 25/09/2026 | AC | 607 | Achats de marchandises | Textiles Lumière F rectif. compl. AV-26-0087 (remise 5 % robes) | 26,40 | |
| 25/09/2026 | AC | 44566 | TVA déductible sur ABS | Textiles Lumière F rectif. compl. AV-26-0087 | 5,28 | |
| 25/09/2026 | AC | 401TEXL | Fournisseur Textiles Lumière | Textiles Lumière F rectif. compl. AV-26-0087 | | 31,68 |
| 02/10/2026 | BQ | 401TEXL | Fournisseur Textiles Lumière | Vir. Textiles Lumière FA-26-0912 – AV-26-0087 + rectif. | 10 011,48 | |
| 02/10/2026 | BQ | 512 | Banque | Vir. Textiles Lumière FA-26-0912 – AV-26-0087 + rectif. | | 10 011,48 |
| | | | | **Totaux** | **11 052,96** | **11 052,96** |

**Compte 401TEXL lettré**

| Date | Pièce | Débit | Crédit | Let. |
|---|---|---|---|---|
| 02/09 | FA-26-0912 | | 10 989,60 | A |
| 18/09 | AV-26-0087 | 1 009,80 | | A |
| 25/09 | Rectificative compl. | | 31,68 | A |
| 02/10 | Virement | 10 011,48 | | A |
| | **Totaux** | **11 021,28** | **11 021,28** | Solde 0 |

Effet net sur les achats : 607 = 9 158,00 – 528,00 + 26,40 = **8 656,40 €** (soit 9 158,00 – 501,60) ; 6097 = 313,50 € ; coût net des marchandises conservées = **8 342,90 €**.

## 4. Points d'attention / pièges

- **Un avoir se contrôle comme une facture** : quantités (= bon de retour), prix (= prix **net** facturé à l'origine), taux de TVA (= taux de la facture d'origine), référence à la facture.
- **Retour = crédit du compte d'achat** ; **rabais/remise/ristourne hors facture = 609x**. Ne pas tout mettre en 609.
- **TVA** : l'avoir oblige Mode & Co à **reverser** la TVA déduite (168,30 €, puis 163,02 € net après rectification) sur la CA3 de septembre (mois de réception de l'avoir).
- **Question 6 — avoir reçu après paiement** : le compte 401 devient **débiteur** (le fournisseur nous doit de l'argent). On impute l'avoir sur le prochain règlement, ou on demande un remboursement. À la clôture, un 401 débiteur ne peut pas rester en dettes fournisseurs (principe de **non-compensation**) : on le reclasse à l'actif en **4097 « Fournisseurs – autres avoirs »** (ou 409 selon la nomenclature du dossier), puis on extourne à l'ouverture. Si l'avoir est seulement **promis** et pas encore reçu à la clôture : avoir à recevoir 4098 / 607 ou 6097 / 44586.
- **Ne pas déduire l'avoir « à la louche »** sur le paiement sans document : le compte ne se lettrerait pas.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 7 — conséquences sur le stock** :
- **sortir les 20 robes** du stock dans le back-office (quantités) à la date du retour — sinon l'inventaire du 31/12 sera faux et le CMUP aussi ;
- les robes retournées sortent **à leur coût d'entrée** (25,08 € net), pas au CMUP de la référence ;
- le **rabais** sur les chinos diminue leur **coût d'achat** : il doit être intégré au calcul du CMUP (3 135,00 – 313,50 = 2 821,50 € pour 150 pièces, soit 18,81 € pièce au lieu de 20,90 €) ;
- vérifier que les 20 robes n'avaient pas été mises en ligne et vendues entre-temps (sinon : litige qualité côté client final, retours, provision).

**Message à Inès Moreau :**

> Bonjour Inès,
>
> L'avoir de Textiles Lumière contient une petite erreur en votre faveur : les robes ont été reprises au prix brut (26,40 €) alors que vous les aviez payées avec 5 % de remise. L'écart est de 31,68 € TTC. Je vous propose de le leur signaler — ils vous enverront une facture complémentaire — pour garder un compte propre avec votre principal grossiste. Le montant à payer le 2 octobre est alors de **10 011,48 €**.
>
> Pensez aussi à sortir les 20 robes du stock dans Shopify à la date du retour, et à mettre à jour le coût des chinos (rabais de 10 %).

**Documentation** : conserver le bon de retour (20 robes) avec l'avoir — c'est la pièce qui justifie la quantité ; noter dans la fiche fournisseur : « remise quantitative 5 % — à vérifier sur chaque avoir ».

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 607 « Achats de marchandises », 6097 « RRR obtenus sur achats de marchandises », 4097 / 4098 ; principe de non-compensation.
- CGI art. 272-1 : réduction de la TVA en cas de réduction de prix ou de résiliation (avoir).
- CGI, annexe II, art. 242 nonies A : l'avoir fait référence à la facture initiale.
- PCG : coût d'acquisition des stocks (net des rabais, remises et ristournes).
