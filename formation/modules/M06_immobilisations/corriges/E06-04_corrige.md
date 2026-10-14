# Corrigé E06-04 — Cession d'un porteur frigorifique et d'une semi-remorque

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-04](../exercices/E06-04_cession-porteur-transports-leroy.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — La TVA (question 1).** Le **régime de la marge** (CGI, art. 297 A) est réservé aux **assujettis-revendeurs** qui achètent des biens d'occasion **sans avoir pu récupérer de TVA** (par exemple auprès d'un particulier) pour les revendre — c'est le cas du Garage Martin pour ses VO achetés à des particuliers. Transports Leroy n'est pas un revendeur : elle cède ses **propres immobilisations**, dont elle a **déduit la TVA** à l'achat. La cession est donc **taxable au taux normal de 20 % sur le prix total**.

Erreurs du projet de facture :
1. Régime de la marge à tort → TVA 20 % sur 81 000 € = 16 200 € ; TTC 97 200 €.
2. Prix global : il faut **ventiler par bien** (immatriculation, kilométrage) — c'est indispensable pour calculer chaque résultat de cession et justifier la sortie de chaque fiche.
3. Mentions manquantes : SIREN et n° de TVA intracommunautaire du client, **nature de l'opération** (livraison de biens), adresse de livraison si différente, date et conditions de paiement, pénalités de retard et **indemnité forfaitaire de 40 €** (vente entre professionnels).

Facture rectifiée (corps) :

```
Nature de l'opération : livraison de biens — Livraison au dépôt de Vénissieux le 31/05/2026
Porteur 19 t frigorifique FL-219-TR, 412 000 km, vendu en l'état     HT  41 000,00
Semi-remorque frigorifique GA-554-KR, vendue en l'état               HT  40 000,00
                                                              Total HT    81 000,00
                                                              TVA 20 %    16 200,00
                                                              Total TTC   97 200,00
Paiement par virement au plus tard le 30/06/2026. Pénalités de retard : 3 × taux d'intérêt légal ;
indemnité forfaitaire pour frais de recouvrement : 40 €.
```

**Étape 2 — La séquence comptable.** (1) dotation complémentaire jusqu'à la date de cession, (2) sortie (brut, amortissements, VNC en 675), (3) produit de cession en 775 contre une créance sur cession (462), (4) encaissement. Le 675 et le 775 sont des comptes de **résultat exceptionnel**, maintenus pour les cessions par le PCG 2025.

**Étape 3 — L'imposition (question 4).** Transports Leroy est une **société à l'IS** : il n'y a **pas** de régime court terme / long terme pour le matériel. Le résultat de cession (plus-value ou moins-value) est **inclus dans le résultat imposable** et taxé au taux de droit commun. Le « long terme » dont parlait l'ancien comptable concerne les entreprises **à l'IR**… et même pour elles, il ne joue que sur la fraction du prix qui **dépasse le coût d'origine** (cf. question 6).

## 2. Calculs (détaillés, chaque montant justifié)

**Question 2 — Résultat de cession par véhicule** (cession le 31/05/2026 → 5 mois en 2026)

| | Porteur FL-219-TR | Semi-remorque GA-554-KR |
|---|---:|---:|
| Valeur brute | 96 000,00 | 52 000,00 |
| Annuité | 96 000 / 6 = 16 000,00 | 52 000 / 8 = 6 500,00 |
| Cumul au 31/12/2025 | 62 666,67 (2022 : 11/12 = 14 666,67 + 3 × 16 000) | 5 416,67 (2025 : 10/12) |
| **Dotation 2026** (5/12) | **6 666,67** | **2 708,33** |
| Cumul à la cession | 69 333,34 | 8 125,00 |
| **VNC** | **26 666,66** | **43 875,00** |
| Prix de cession HT | 41 000,00 | 40 000,00 |
| **Résultat de cession** | **+ 14 333,34** | **– 3 875,00** |

Résultat net de cession : 14 333,34 – 3 875,00 = **+ 10 458,34 €** (contrôle : 775 = 81 000,00 ; 675 = 26 666,66 + 43 875,00 = 70 541,66 ; 81 000,00 – 70 541,66 = 10 458,34 ✓).

**Question 4 — IS chez Transports Leroy** : 10 458,34 € inclus dans le résultat fiscal, au taux marginal de 25 % → **≈ 2 614,59 € d'IS**. (Les dotations 2026 de 9 375,00 € sont, elles, déductibles.)

**Question 5 — Cas « entreprise individuelle à l'IR »**

| Bien | Durée de détention | Nature du bien | Résultat | Qualification |
|---|---|---|---:|---|
| Porteur | 01/02/2022 → 31/05/2026 : **≥ 2 ans** | Amortissable | + 14 333,34 | Plus-value **à court terme** à hauteur des amortissements déduits (69 333,34) ; la plus-value (14 333,34) leur étant inférieure → **100 % court terme**, **0 € de long terme** |
| Semi-remorque | 01/03/2025 → 31/05/2026 : **< 2 ans** | Amortissable | – 3 875,00 | Moins-value **à court terme** (bien amortissable : toujours CT, et de toute façon < 2 ans) |
| **Plus-value nette à court terme** | | | **+ 10 458,34** | |

Imposition : la plus-value nette à court terme s'ajoute au **bénéfice BIC** et suit le barème progressif (et, en principe, l'assiette des cotisations sociales de l'exploitant — *à vérifier selon le régime social*). Sur option, elle peut être **étalée sur 3 ans** : 3 486,11 € en 2026, 3 486,11 € en 2027, 3 486,12 € en 2028.

**Question 6 — Variante : porteur vendu 101 000 € HT (entreprise à l'IR)**

| Élément | Calcul | Montant |
|---|---|---:|
| Plus-value totale | 101 000,00 – 26 666,66 | 74 333,34 |
| dont **court terme** (= amortissements déduits) | | **69 333,34** |
| dont **long terme** (= prix – coût d'origine) | 101 000,00 – 96 000,00 | **5 000,00** |
| Contrôle | 69 333,34 + 5 000,00 | 74 333,34 ✓ |
| Impôt sur le long terme | 5 000 × 12,8 % | 640,00 |
| Prélèvements sociaux | 5 000 × 17,2 % | 860,00 |
| **Total sur le long terme** | | **1 500,00** |

La logique : la fraction de la plus-value qui ne fait que « reprendre » des amortissements déduits au taux marginal est taxée comme eux (court terme) ; seul le **gain réel au-delà du prix d'achat** bénéficie du taux proportionnel.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/05/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotation 2026 FL-219-TR (5 mois) + GA-554-KR (5 mois) | 9 375,00 | |
| 31/05/2026 | OD | 28182 | Amortissements du matériel de transport | FL-219-TR 6 666,67 + GA-554-KR 2 708,33 | | 9 375,00 |
| 31/05/2026 | OD | 28182 | Amortissements du matériel de transport | Sortie FL-219-TR | 69 333,34 | |
| 31/05/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie FL-219-TR | 26 666,66 | |
| 31/05/2026 | OD | 2182 | Matériel de transport | Sortie FL-219-TR | | 96 000,00 |
| 31/05/2026 | OD | 28182 | Amortissements du matériel de transport | Sortie GA-554-KR | 8 125,00 | |
| 31/05/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie GA-554-KR | 43 875,00 | |
| 31/05/2026 | OD | 2182 | Matériel de transport | Sortie GA-554-KR | | 52 000,00 |
| 31/05/2026 | VT | 462 | Créances sur cessions d'immobilisations | Fact. 2026-VI-002 Frigo Transports Auvergne | 97 200,00 | |
| 31/05/2026 | VT | 775 | Produits des cessions d'éléments d'actif | Cession FL-219-TR 41 000 + GA-554-KR 40 000 | | 81 000,00 |
| 31/05/2026 | VT | 44571 | TVA collectée | Cession véhicules 20 % | | 16 200,00 |
| 30/06/2026 | BQ | 512 | Banque | Vir. Frigo Transports Auvergne | 97 200,00 | |
| 30/06/2026 | BQ | 462 | Créances sur cessions d'immobilisations | Règlement fact. 2026-VI-002 | | 97 200,00 |
| | | | | **Totaux** | **351 775,00** | **351 775,00** |

Pourquoi **462** et non 411 ? La créance née d'une cession d'immobilisation n'est pas une créance d'exploitation : la distinguer permet une présentation correcte du bilan (autres créances) et du tableau des flux (flux d'investissement).

## 4. Points d'attention / pièges

- **Oublier la dotation de l'exercice de cession** : la VNC serait surévaluée de 9 375 € et la plus-value sous-évaluée d'autant — le résultat total est identique, mais le **classement** (6811 d'exploitation vs 675 exceptionnel) et l'EBE/résultat d'exploitation sont faussés.
- **Créditer 2182 du prix de vente** : erreur classique de saisie « au plus simple » ; le compte 2182 ne contient que des valeurs d'origine.
- **TVA** : la TVA collectée sur les cessions d'immobilisations figure sur la CA3 du mois (mai 2026) ; aucune régularisation de TVA déduite n'est due puisque la cession est taxée.
- **Si un véhicule avait fait l'objet d'amortissements dérogatoires**, le solde du 145 serait repris en 7872 à la cession (cf. E06-10) et la plus-value **fiscale** serait calculée sur la VNC fiscale.
- **IS** : pas de « remploi » permettant d'exonérer la plus-value en rachetant un véhicule ; seuls des régimes spécifiques et ciblés existent. La plus-value est taxée l'année de la cession.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Formalités annexes (question 7)**
- **Déclaration de cession** et certificat de situation administrative remis à l'acheteur ; barrer et signer les certificats d'immatriculation.
- **Résilier ou modifier l'assurance** flotte ; **désactiver les cartes carburant** et badges de télépéage des deux véhicules.
- **Taxe à l'essieu** (véhicules ≥ 12 t) : mettre à jour la déclaration (fin d'assujettissement à la date de cession) — *modalités à vérifier*.
- **Remboursement partiel de TICPE** : retirer les véhicules de la liste déclarée pour la période suivante.
- Mettre à jour le **fichier des immobilisations** (date de sortie, prix) et vérifier qu'aucun **contrat de maintenance** du groupe froid ne continue d'être facturé.

**Mail à Bruno Leroy**

> Bonjour Monsieur Leroy,
>
> La facture de vente doit être émise avec une TVA de 20 % (16 200 €) : le régime de la marge ne s'applique pas à une entreprise qui vend son propre matériel. Votre acheteur la récupérera, cela ne lui coûte rien.
>
> Sur le plan fiscal, la vente dégage un gain net de 10 458 € (plus-value de 14 333 € sur le porteur, moins-value de 3 875 € sur la semi-remorque). Votre société étant à l'impôt sur les sociétés, ce gain est imposé comme le reste du bénéfice, soit environ 2 600 € d'IS. La notion de « long terme » ne concerne pas le matériel d'une société à l'IS.
>
> Pensez enfin à résilier l'assurance et à désactiver les cartes carburant des deux véhicules.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : sortie des immobilisations ; comptes 462, 675, 775 (maintenus par le règlement ANC n° 2022-06).
- CGI, art. 297 A : régime de la marge (assujettis-revendeurs) ; art. 256 et 266 : cession taxable d'un bien d'investissement.
- CGI, art. 242 nonies A, annexe II : mentions obligatoires des factures ; Code de commerce, art. L. 441-9 et L. 441-10 : pénalités et indemnité forfaitaire.
- CGI, art. 39 duodecies et s. (régime CT/LT des entreprises à l'IR), art. 39 quaterdecies (étalement de la plus-value nette à court terme) ; art. 219 (taux de l'IS).
