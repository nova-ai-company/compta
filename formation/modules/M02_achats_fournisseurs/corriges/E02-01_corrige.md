# Corrigé E02-01 — La facture de la minoterie : remise, escompte, port et palettes consignées

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-01](../exercices/E02-01_minoterie-remise-escompte-port.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

On lit la facture **de haut en bas**, en séparant ce qui est commercial, ce qui est financier, ce qui est accessoire et ce qui n'est pas un achat.

| Élément | Nature | Traitement comptable | TVA |
|---|---|---|---|
| Remise fidélité 3 % | Réduction **commerciale** sur facture | **Non comptabilisée** : on enregistre le net commercial (1 941,94 €) | Réduit la base |
| Escompte 1 % | Réduction **financière** (paiement anticipé) | **Produit financier 765 Escomptes obtenus** | Réduit la base (la facture calcule la TVA sur le net financier) |
| Frais de livraison facturés par le vendeur | **Frais accessoire** de la livraison | 6241 Transports sur achats (méthode du dossier) ou incorporation au 601 | **Même taux que la marchandise livrée** : 5,5 % |
| Consignation de palettes | **Créance** sur le fournisseur (on récupère la somme au retour) | 4096 | Hors champ tant que les palettes sont rendues |

**L'anomalie** : la minoterie applique **20 %** sur les frais de livraison. Or les frais accessoires facturés par le vendeur (transport, emballage…) font partie de la base imposable de la livraison principale (CGI art. 267) et suivent **son taux**, ici **5,5 %** (farine, produit alimentaire). La TVA facturée en trop n'est **pas déductible** par la boulangerie (elle est due par la minoterie qui l'a facturée — CGI art. 283-3). Montant de l'erreur : 45,00 × (20 % – 5,5 %) = **6,52 €** (9,00 € facturés au lieu de 2,48 €).

Petit montant, mais **récurrent** (chaque livraison) : sur un an, plusieurs dizaines d'euros de TVA non déductible et, surtout, un défaut à signaler à un fournisseur important. D'où l'appel et la demande d'avoir.

**Montant à payer le 12/10 (question 3)** : 2 112,26 – 6,52 = **2 105,74 €**, en indiquant la référence de la facture et le motif de la différence (« TVA port 5,5 % – avoir à recevoir »). Le paiement intervient avant le 13/10 : l'escompte est acquis.

## 2. Calculs (détaillés, chaque montant justifié)

| Ligne | Calcul | Montant |
|---|---|---|
| Farine T65 | 60 × 21,40 | 1 284,00 € |
| Farine T45 | 20 × 24,90 | 498,00 € |
| Seigle | 8 × 27,50 | 220,00 € |
| **Brut HT** | | **2 002,00 €** ✓ |
| Remise 3 % | 2 002,00 × 3 % = 60,06 | – 60,06 € ✓ |
| **Net commercial** | | **1 941,94 €** ✓ |
| Escompte 1 % | 1 941,94 × 1 % = 19,4194 | – 19,42 € ✓ |
| **Net financier** | | **1 922,52 €** ✓ |
| TVA 5,5 % sur le net financier | 1 922,52 × 5,5 % = 105,7386 | 105,74 € ✓ |
| Port | | 45,00 € |
| TVA facturée sur le port (20 %) | 45,00 × 20 % | 9,00 € ✗ |
| TVA due sur le port (5,5 %) | 45,00 × 5,5 % = 2,475 | **2,48 €** |
| Consignation | 2 × 15,00 | 30,00 € |
| **TTC facturé** | 1 922,52 + 45,00 + 105,74 + 9,00 + 30,00 | **2 112,26 €** ✓ (arithmétiquement juste) |
| **TTC dû** | 2 112,26 – (9,00 – 2,48) | **2 105,74 €** |

Contrôle de l'avoir : 9,00 – 2,48 = **6,52 €**.

**Question 5 — paiement le 20/10 (hors délai d'escompte)** : la minoterie refacture l'escompte et la TVA correspondante :
- escompte : 19,42 € ;
- TVA à 5,5 % : 19,42 × 5,5 % = 1,0681 → **1,07 €** ;
- total facture complémentaire : **20,49 €**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/10/2026 | AC | 601 | Achats de matières premières | Minoterie MMO-26-2207 farines (net commercial) | 1 941,94 | |
| 05/10/2026 | AC | 6241 | Transports sur achats | Minoterie MMO-26-2207 frais de livraison | 45,00 | |
| 05/10/2026 | AC | 4096 | Fournisseurs – emballages à rendre | Minoterie MMO-26-2207 consignation 2 palettes | 30,00 | |
| 05/10/2026 | AC | 44566 | TVA déductible sur ABS | Minoterie MMO-26-2207 (105,74 + 9,00) | 114,74 | |
| 05/10/2026 | AC | 765 | Escomptes obtenus | Minoterie MMO-26-2207 escompte 1 % | | 19,42 |
| 05/10/2026 | AC | 401MINO | Fournisseur Minoterie des Monts d'Or | Minoterie MMO-26-2207 | | 2 112,26 |
| 12/10/2026 | BQ | 401MINO | Fournisseur Minoterie des Monts d'Or | Vir. Minoterie MMO-26-2207 (moins TVA port) | 2 105,74 | |
| 12/10/2026 | BQ | 512 | Banque | Vir. Minoterie MMO-26-2207 | | 2 105,74 |
| 14/10/2026 | AC | 401MINO | Fournisseur Minoterie des Monts d'Or | Minoterie AV rectif. TVA port s/ MMO-26-2207 | 6,52 | |
| 14/10/2026 | AC | 44566 | TVA déductible sur ABS | Minoterie AV rectif. TVA port s/ MMO-26-2207 | | 6,52 |
| 19/10/2026 | AC | 401MINO | Fournisseur Minoterie des Monts d'Or | Déconsignation 2 palettes MMO-26-2207 | 30,00 | |
| 19/10/2026 | AC | 4096 | Fournisseurs – emballages à rendre | Déconsignation 2 palettes MMO-26-2207 | | 30,00 |
| | | | | **Totaux** | **4 273,94** | **4 273,94** |

Après ces écritures : 401MINO = 2 112,26 – 2 105,74 – 6,52 = 0 pour la facture (lettrable), puis 30,00 € débiteur (déconsignation), qui s'imputera sur la facture suivante ; 4096 soldé ; TVA déductible nette = 114,74 – 6,52 = **108,22 €** (105,74 + 2,48).

**Variante (question 5) — paiement le 20/10, facture complémentaire d'escompte :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 20/10/2026 | AC | 765 | Escomptes obtenus | Minoterie F compl. escompte non acquis s/ MMO-26-2207 | 19,42 | |
| 20/10/2026 | AC | 44566 | TVA déductible sur ABS | Minoterie F compl. escompte non acquis | 1,07 | |
| 20/10/2026 | AC | 401MINO | Fournisseur Minoterie des Monts d'Or | Minoterie F compl. escompte non acquis | | 20,49 |
| | | | | **Totaux** | **20,49** | **20,49** |

(Au sein du même exercice, on annule le produit 765 ; certains dossiers imputent au compte d'achat — l'important est la cohérence.)

## 4. Points d'attention / pièges

- **Remise sur facture = rien à comptabiliser** : ne pas créer de ligne 609 de 60,06 €.
- **L'escompte n'est pas une remise** : c'est un **produit financier** (765). Il apparaît dans le résultat financier, pas dans la marge.
- **TVA de l'escompte** : la facture calcule la TVA sur le net financier → la TVA déductible est 105,74 € (et non 1 941,94 × 5,5 % = 106,81 €). Si la boulangerie perd l'escompte, la TVA « remonte » via la facture complémentaire.
- **Taux des frais accessoires** : ils suivent le taux de la livraison principale (5,5 %), qu'ils soient facturés par le vendeur pour une livraison de farine, de pain ou de matériel. Un transporteur **indépendant** facturerait, lui, 20 %.
- **La consignation n'est pas une charge** : 4096. Si une palette n'était pas rendue, elle deviendrait un achat d'emballage (6026) avec TVA.
- **Question 6 — stock au 31/12** : le coût d'acquisition des stocks comprend le prix d'achat **après déduction des remises, rabais et escomptes de règlement**, majoré des **frais accessoires** (transport). Même si le port est comptabilisé en 6241 et l'escompte en 765 dans les comptes de gestion, la valorisation du stock de farine au 31/12 doit se faire au **coût net** (net financier + quote-part de port). Exemple, en répartissant le port au prorata des valeurs : coût d'un sac de T65 = 21,40 × 0,97 × 0,99 = 20,55 € + quote-part de port (45,00 × 1 284,00 / 2 002,00) / 60 = 0,48 €, soit **≈ 21,03 €** — méthode à fixer et à appliquer de façon permanente (voir module stocks).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Message à Marc Dupain :**

> Bonjour Marc,
>
> Pour la facture MMO-26-2207 : payez **2 105,74 €** avant le **13/10** (vous gardez l'escompte de 1 %, soit 19,42 €). La minoterie s'est trompée de TVA sur les frais de port (20 % au lieu de 5,5 %) : nous avons retenu la différence de 6,52 € et ils vont vous envoyer un avoir. Les 30 € de palettes vous seront remboursés quand vous les rendrez.
>
> Un conseil : l'escompte de 1 % pour payer 3 semaines plus tôt équivaut à un rendement annuel d'environ 17 % — c'est toujours intéressant de le prendre si la trésorerie le permet.

(1 % gagné pour 22 jours d'avance environ (paiement le 12/10 au lieu du 04/11) : 1 % × 365 / 22 ≈ 16,6 % par an.)

**Contrôles** :
- vérifier les factures de la minoterie depuis son changement de logiciel (les mois précédents ont-ils la même erreur ?) ;
- suivre le compte 4096 : le nombre de palettes consignées et rendues doit concorder ; un solde ancien = palettes perdues à passer en charges ;
- noter au dossier permanent : « Minoterie : escompte 1 % à 8 jours — paiement à surveiller ; port au taux de la farine ».

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 765 « Escomptes obtenus », 4096 « Fournisseurs – créances pour emballages et matériel à rendre », 6241, 609 ; coût d'acquisition des stocks et des immobilisations (prix d'achat net des remises, rabais et escomptes de règlement, majoré des frais accessoires).
- CGI art. 267-I-2° : frais accessoires compris dans la base imposable de l'opération principale ; art. 267-II-1° : escomptes et remises exclus de la base.
- CGI art. 278-0 bis : taux de 5,5 % sur les produits alimentaires.
- CGI art. 283-3 : TVA facturée à tort due par l'émetteur de la facture, non déductible par le client.
- Code de commerce art. L. 441-9 : conditions d'escompte, pénalités, indemnité forfaitaire.
