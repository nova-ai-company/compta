# Corrigé E12-01a — Garage Martin : écritures d'inventaire et balance après inventaire

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E12-01](../exercices/E12-01_cas-synthese-garage-martin.md)

> Partie 1/2 du corrigé du cas de synthèse. La partie 2 (`E12-01b_corrige.md`) traite le bilan, le compte de résultat, les SIG, la CAF, l'IS, l'annexe et la note de synthèse.
> Tous les montants ont été recalculés par script ; la balance avant inventaire, le journal d'inventaire et la balance après inventaire sont équilibrés.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Avant de passer la moindre écriture, un senior fait **trois choses** :
1. **Il contrôle la balance avant inventaire** (contrôles de cohérence du cours, § 5) : 421 soldé ✔ ; caisse débitrice (1 150 €) ✔ ; **471 non vide (850 € créditeur)** ✘ → à apurer ; capital (15 000 €) conforme aux statuts ✔ ; 120/129 à zéro → affectation N-1 passée ✔ ; emprunt : capital restant dû au 01/08/2026 = 30 000 € = solde du 1641 ✔ ; 28 cumulés au 30/09/2025 = fichier des immobilisations ✔ (51 000 / 26 700 = 22 500 + 4 200 / 42 400 = 21 600 + 20 800 / 6 000 / 3 600) ; **2182 contient encore le Master vendu** ✘ ; 6354/7088 : **débours dans le CA** ✘.
2. **Il liste les informations d'inventaire** et décide pour chacune : écriture / pas d'écriture / question au client.
3. **Il fixe l'ordre** : d'abord tout ce qui touche le résultat comptable, **l'IS en dernier** (il dépend de tout le reste).

### Point par point

| # | Information | Décision du senior |
|---|---|---|
| 1 | Fichier des immobilisations | Dotations de l'exercice à calculer pour chaque bien, **y compris le Master jusqu'à sa date de cession** et la station de géométrie **à partir du 01/02/2026**. Le fonds commercial n'est pas amorti (durée non limitée, présomption retenue par le client) : un test de dépréciation suffit — rien n'indique une perte de valeur (activité stable, rentable). |
| 2 | Cession du Master | Le prix (775) et la TVA collectée sont déjà enregistrés. Il manque la **sortie du bien** : solder 2182 et 28182, constater la VNC en 675. Les cessions d'immobilisations **restent en résultat exceptionnel** (675/775) avec le PCG 2025. |
| 3 | Stocks | Balance : stocks **initiaux** (46 000 / 98 000). On annule le stock initial et on constate le stock final (pièces 52 400 € ; VO 69 100 €). **La BMW en dépôt-vente n'appartient pas au garage → exclue** (le garage n'est que mandataire). |
| 4 | Dépréciations de stocks | Reprise intégrale de la dépréciation N-1 (VO vendus) ; nouvelle dépréciation lorsque la **valeur nette de réalisation** (prix de vente probable – frais de vente/remise en état – TVA sur la marge éventuelle) < coût. |
| 5 | Garantie VO | Obligation contractuelle → sortie de ressources probable, montant estimable statistiquement → **provision pour risques** (compte 1512). On ajuste le stock de provision : 3 540 € nécessaires – 2 900 € existants = **dotation 640 €**. |
| 6 | FNP | Travaux de carrosserie terminés le 25/09 (BL signé) et électricité consommée en septembre → charges de l'exercice → **408** + TVA en 44586. |
| 7 | FAE | Prestation achevée le 30/09, facturée le 05/10 → produit de l'exercice → **418** + TVA en 44587. |
| 8 | CCA | Assurance : 6 mois sur 12 concernent l'exercice suivant ; loyer T4 2026 : entièrement N+1. |
| 9 | ICNE | Intérêts du 01/08 au 30/09/2026 sur 30 000 € → 1688. |
| 10 | Transports Vidal | RJ ouvert → créance **douteuse** (416) ; dépréciation sur le **HT** (la TVA n'est pas une perte : elle sera récupérable en cas d'irrécouvrabilité définitive). |
| 11 | M. Roux | Certificat d'irrécouvrabilité → **perte définitive** (654) ; la TVA collectée est récupérable (régularisation sur la CA3, facture rectificative adressée au client). |
| 12 | Congés payés | La balance contient la dette N-1 : on **ajuste** à la dette N (16 200 €) et aux charges sociales (42 %). |
| 13 | Mégane VO-233 | Achetée à un **assujetti avec TVA récupérée** → le régime de la marge est **exclu** (il suppose un bien acquis sans droit à déduction). La vente est taxable sur le **prix total** : HT 9 500 €, TVA 1 900 €. TVA déjà collectée : 300 € → **complément 1 600 €** (CA3 de septembre, non encore déposée). |
| 14 | Cartes grises | Sommes payées **au nom et pour le compte du client**, refacturées à l'euro près, comptabilisées en compte de tiers : ce sont des **débours** (hors CA, hors base de TVA). On neutralise 6354 et 7088. *En N+1 : créer un compte 467 « Débours cartes grises ».* |
| 15 | Compte 471 | Encaissement identifié → lettrage du client Plomberie Rhodanienne. |
| 16 | Amende 450 € | Charge d'exploitation (658 — plus d'exceptionnel depuis le PCG 2025) ; **non déductible** fiscalement (art. 39-2 CGI) → réintégration extra-comptable, pas d'écriture. |
| 17 | IDR 11 300 € | Méthode préférentielle (provision) non retenue par la société → **pas d'écriture**, **mention en annexe** des engagements. |
| 18 | IS | Calculé en dernier sur le résultat fiscal. |

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 Amortissements de l'exercice (01/10/2025 → 30/09/2026)

| Réf. | Bien | Base | Calcul | Dotation |
|---|---|---:|---|---:|
| I-02 | Agencements | 85 000 | 85 000 / 10 | 8 500,00 |
| I-03 | Ponts élévateurs | 36 000 | 36 000 / 8 | 4 500,00 |
| I-04 | Valise diagnostic | 12 000 | 12 000 / 5 | 2 400,00 |
| I-05 | Station de géométrie | 18 000 | 18 000 / 6 × 8/12 (01/02 → 30/09) | 2 000,00 |
| I-06 | Master (cédé) | 24 000 | 24 000 / 5 × 5,5/12 (01/10/2025 → 15/03/2026) | 2 200,00 |
| I-07 | Dépanneuse | 32 000 | 32 000 / 5 | 6 400,00 |
| I-08 | Informatique | 9 000 | 9 000 / 3 (dernière annuité : bien totalement amorti au 30/09/2026) | 3 000,00 |
| I-09 | Mobilier | 6 000 | 6 000 / 10 | 600,00 |
| | **Total compte 6811** | | | **29 600,00** |

Par compte : 28135 = 8 500 ; 28154 = 4 500 + 2 400 + 2 000 = 8 900 ; 28182 = 6 400 + 2 200 = 8 600 ; 28183 = 3 000 ; 28184 = 600.

### 2.2 Cession du Master

- Amortissements cumulés à la date de cession : 21 600 + 2 200 = **23 800 €** ; VNC = 24 000 – 23 800 = **200 €**.
- Plus-value comptable = 8 000 – 200 = **7 800 €** (775 – 675).
- Fiscalement (société à l'IS) : la plus-value est imposée au taux de droit commun avec le résultat ; la distinction court terme / long terme ne joue pas ici → aucun retraitement.

### 2.3 Stocks

- Pièces : SI 46 000 → SF 52 400 ⇒ variation 60371 = **– 6 400 €** (stockage).
- VO : 9 800 + 11 500 + 8 200 + 10 900 + 6 400 + 12 600 + 9 700 = **69 100 €** (BMW DV-03 exclue). SI 98 000 ⇒ variation 60372 = **+ 28 900 €** (déstockage).
- Total variation des stocks de marchandises : 46 000 + 98 000 – 52 400 – 69 100 = **22 500 €** (débitrice).

### 2.4 Dépréciation des stocks

| Article | Coût | Valeur nette de réalisation | Dépréciation |
|---|---:|---|---:|
| Golf VO-219 (8,5 mois de stock) | 10 900 | 9 500 – 400 = 9 100 (vente à perte → pas de TVA sur marge) | 1 800,00 |
| C3 VO-207 (10,5 mois) | 6 400 | 5 200 – 500 = 4 700 (idem) | 1 700,00 |
| Pièces obsolètes | 3 200 | 800 | 2 400,00 |
| **Total dotation 6817** | | | **5 900,00** |

Contrôle des autres VO (VNR > coût → aucune dépréciation) : 208 : 12 900 – TVA sur marge (12 900 – 9 800) / 6 = 516,67 → 12 383,33 > 9 800 ; Clio : 15 990 / 1,2 = 13 325 > 11 500 ; Duster : 10 500 – 383,33 = 10 116,67 > 8 200 ; Yaris : 15 400 – 466,67 = 14 933,33 > 12 600 ; Focus : 13 200 / 1,2 = 11 000 > 9 700.
Reprise de la dépréciation N-1 : **6 000 €** (7817), les VO concernés sont sortis du stock.

### 2.5 Autres calculs

- **Provision garanties** : 236 000 × 1,5 % = **3 540 €** ; dotation 3 540 – 2 900 = **640 €**.
- **FNP** : 2 400 + 1 100 = 3 500 € HT ; TVA 700 € ; 408 = **4 200 €**.
- **FAE** : 1 800 + 1 350 = 3 150 € HT ; TVA 630 € ; 418 = **3 780 €**.
- **CCA** : assurance 9 600 × 6/12 = **4 800 €** ; loyer **10 500 €** ; total **15 300 €**.
- **ICNE** : 30 000 × 4 % × 2/12 = **200 €**. Contrôle du 6611 : intérêts payés 420 + 390 + 360 + 330 = 1 500 – extourne ICNE N-1 280 = 1 220 € = solde avant inventaire ✔ ; charge de l'exercice après ICNE : **1 420 €**.
- **Transports Vidal** : 4 000 € HT × 70 % (perte probable) = **2 800 €**.
- **M. Roux** : 300 € HT en 654, 60 € de TVA récupérée.
- **Congés payés** : 16 200 – 14 800 = **+ 1 400 €** ; charges : 16 200 × 42 % = 6 804 – 6 216 = **+ 588 €**.
- **Mégane** : prix TTC 11 400 → HT 9 500, TVA 1 900 ; déjà collecté 300 → **+ 1 600 €** de TVA ; le CA de la vente passe de 11 100 € (7072) à 9 500 € (7073), soit **– 1 600 €** de CA.
- **IS** : voir partie 2 (résultat fiscal 87 302 € → IS **17 576 €**).

## 3. Écritures comptables (journal OD d'inventaire, au 30/09/2026)

| N° | Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---:|---:|
| 1 | 30/09/2026 | OD | 6811 | Dotations aux amortissements des immobilisations | Dotations aux amortissements de l'exercice | 29 600,00 |  |
| 1 | 30/09/2026 | OD | 28135 | Amort. installations, agencements | Dotations aux amortissements de l'exercice |  | 8 500,00 |
| 1 | 30/09/2026 | OD | 28154 | Amort. matériel industriel | Dotations aux amortissements de l'exercice |  | 8 900,00 |
| 1 | 30/09/2026 | OD | 28182 | Amort. matériel de transport | Dotations aux amortissements de l'exercice |  | 8 600,00 |
| 1 | 30/09/2026 | OD | 28183 | Amort. matériel de bureau et informatique | Dotations aux amortissements de l'exercice |  | 3 000,00 |
| 1 | 30/09/2026 | OD | 28184 | Amort. mobilier | Dotations aux amortissements de l'exercice |  | 600,00 |
| 2 | 30/09/2026 | OD | 28182 | Amort. matériel de transport | Sortie de l'utilitaire Renault Master cédé le 15/03/2026 | 23 800,00 |  |
| 2 | 30/09/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie de l'utilitaire Renault Master cédé le 15/03/2026 | 200,00 |  |
| 2 | 30/09/2026 | OD | 2182 | Matériel de transport | Sortie de l'utilitaire Renault Master cédé le 15/03/2026 |  | 24 000,00 |
| 3 | 30/09/2026 | OD | 60371 | Variation des stocks de pièces détachées | Annulation du stock initial | 46 000,00 |  |
| 3 | 30/09/2026 | OD | 60372 | Variation des stocks de VO | Annulation du stock initial | 98 000,00 |  |
| 3 | 30/09/2026 | OD | 3710 | Stock de pièces détachées | Annulation du stock initial |  | 46 000,00 |
| 3 | 30/09/2026 | OD | 3720 | Stock de véhicules d'occasion | Annulation du stock initial |  | 98 000,00 |
| 4 | 30/09/2026 | OD | 3710 | Stock de pièces détachées | Constatation du stock final | 52 400,00 |  |
| 4 | 30/09/2026 | OD | 3720 | Stock de véhicules d'occasion | Constatation du stock final | 69 100,00 |  |
| 4 | 30/09/2026 | OD | 60371 | Variation des stocks de pièces détachées | Constatation du stock final |  | 52 400,00 |
| 4 | 30/09/2026 | OD | 60372 | Variation des stocks de VO | Constatation du stock final |  | 69 100,00 |
| 5 | 30/09/2026 | OD | 3972 | Dépréciation du stock de VO | Reprise de la dépréciation VO N-1 (véhicules vendus) | 6 000,00 |  |
| 5 | 30/09/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise de la dépréciation VO N-1 (véhicules vendus) |  | 6 000,00 |
| 6 | 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation des VO invendus (Golf, C3) et des pièces obsolètes | 5 900,00 |  |
| 6 | 30/09/2026 | OD | 3972 | Dépréciation du stock de VO | Dépréciation des VO invendus (Golf, C3) et des pièces obsolètes |  | 3 500,00 |
| 6 | 30/09/2026 | OD | 3971 | Dépréciation du stock de pièces | Dépréciation des VO invendus (Golf, C3) et des pièces obsolètes |  | 2 400,00 |
| 7 | 30/09/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Ajustement de la provision pour garanties | 640,00 |  |
| 7 | 30/09/2026 | OD | 1512 | Provisions pour garanties données aux clients | Ajustement de la provision pour garanties |  | 640,00 |
| 8 | 30/09/2026 | OD | 611 | Sous-traitance générale (carrosserie) | Factures non parvenues (carrosserie, électricité) | 2 400,00 |  |
| 8 | 30/09/2026 | OD | 6061 | Fournitures non stockables (eau, énergie) | Factures non parvenues (carrosserie, électricité) | 1 100,00 |  |
| 8 | 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | Factures non parvenues (carrosserie, électricité) | 700,00 |  |
| 8 | 30/09/2026 | OD | 408 | Fournisseurs – factures non parvenues | Factures non parvenues (carrosserie, électricité) |  | 4 200,00 |
| 9 | 30/09/2026 | OD | 418 | Clients – factures à établir | Facture à établir Plomberie Rhodanienne (travaux terminés le 30/09) | 3 780,00 |  |
| 9 | 30/09/2026 | OD | 7061 | Prestations atelier (main-d'œuvre) | Facture à établir Plomberie Rhodanienne (travaux terminés le 30/09) |  | 1 800,00 |
| 9 | 30/09/2026 | OD | 7071 | Ventes de pièces détachées | Facture à établir Plomberie Rhodanienne (travaux terminés le 30/09) |  | 1 350,00 |
| 9 | 30/09/2026 | OD | 44587 | TVA sur factures à établir | Facture à établir Plomberie Rhodanienne (travaux terminés le 30/09) |  | 630,00 |
| 10 | 30/09/2026 | OD | 486 | Charges constatées d'avance | Charges constatées d'avance (assurance, loyer T4 2026) | 15 300,00 |  |
| 10 | 30/09/2026 | OD | 616 | Primes d'assurances | Charges constatées d'avance (assurance, loyer T4 2026) |  | 4 800,00 |
| 10 | 30/09/2026 | OD | 6132 | Locations immobilières | Charges constatées d'avance (assurance, loyer T4 2026) |  | 10 500,00 |
| 11 | 30/09/2026 | OD | 6611 | Intérêts des emprunts | Intérêts courus non échus 01/08 – 30/09/2026 | 200,00 |  |
| 11 | 30/09/2026 | OD | 1688 | Intérêts courus sur emprunts | Intérêts courus non échus 01/08 – 30/09/2026 |  | 200,00 |
| 12 | 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Reclassement Transports Vidal en clients douteux | 4 800,00 |  |
| 12 | 30/09/2026 | OD | 411 | Clients | Reclassement Transports Vidal en clients douteux |  | 4 800,00 |
| 13 | 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation créance Transports Vidal (70 % du HT) | 2 800,00 |  |
| 13 | 30/09/2026 | OD | 491 | Dépréciation des comptes clients | Dépréciation créance Transports Vidal (70 % du HT) |  | 2 800,00 |
| 14 | 30/09/2026 | OD | 654 | Pertes sur créances irrécouvrables | Créance irrécouvrable M. Roux | 300,00 |  |
| 14 | 30/09/2026 | OD | 44571 | TVA collectée | Créance irrécouvrable M. Roux | 60,00 |  |
| 14 | 30/09/2026 | OD | 411 | Clients | Créance irrécouvrable M. Roux |  | 360,00 |
| 15 | 30/09/2026 | OD | 6412 | Congés payés | Ajustement de la dette de congés payés | 1 400,00 |  |
| 15 | 30/09/2026 | OD | 6451 | Cotisations URSSAF | Ajustement de la dette de congés payés | 588,00 |  |
| 15 | 30/09/2026 | OD | 4282 | Dettes provisionnées pour congés payés | Ajustement de la dette de congés payés |  | 1 400,00 |
| 15 | 30/09/2026 | OD | 4382 | Charges sociales sur congés à payer | Ajustement de la dette de congés payés |  | 588,00 |
| 16 | 30/09/2026 | OD | 7072 | Ventes de VO – régime de la marge | Régularisation TVA : Mégane achetée à un professionnel | 11 100,00 |  |
| 16 | 30/09/2026 | OD | 7073 | Ventes de VO – régime normal | Régularisation TVA : Mégane achetée à un professionnel |  | 9 500,00 |
| 16 | 30/09/2026 | OD | 44571 | TVA collectée | Régularisation TVA : Mégane achetée à un professionnel |  | 1 600,00 |
| 17 | 30/09/2026 | OD | 7088 | Produits des activités annexes | Reclassement des cartes grises refacturées (débours) | 2 760,00 |  |
| 17 | 30/09/2026 | OD | 6354 | Droits d'enregistrement (cartes grises) | Reclassement des cartes grises refacturées (débours) |  | 2 760,00 |
| 18 | 30/09/2026 | OD | 471 | Compte d'attente | Affectation de l'encaissement en attente (Plomberie Rhodanienne) | 850,00 |  |
| 18 | 30/09/2026 | OD | 411 | Clients | Affectation de l'encaissement en attente (Plomberie Rhodanienne) |  | 850,00 |
| 19 | 30/09/2026 | OD | 695 | Impôts sur les bénéfices | Impôt sur les sociétés de l'exercice | 17 576,00 |  |
| 19 | 30/09/2026 | OD | 444 | État – impôt sur les bénéfices (acomptes versés) | Impôt sur les sociétés de l'exercice |  | 17 576,00 |
| | | | | | **Totaux** | **397 354,00** | **397 354,00** |


### Balance après inventaire au 30/09/2026

| Compte | Intitulé | Solde avant | Écritures | Débit après | Crédit après |
|---|---|---:|---:|---:|---:|
| 101 | Capital | -15 000,00 | 0,00 |  | 15 000,00 |
| 1061 | Réserve légale | -1 500,00 | 0,00 |  | 1 500,00 |
| 1068 | Autres réserves | -196 000,00 | 0,00 |  | 196 000,00 |
| 110 | Report à nouveau (créditeur) | -4 300,00 | 0,00 |  | 4 300,00 |
| 1512 | Provisions pour garanties données aux clients | -2 900,00 | -640,00 |  | 3 540,00 |
| 1641 | Emprunts auprès des établissements de crédit | -30 000,00 | 0,00 |  | 30 000,00 |
| 1688 | Intérêts courus sur emprunts | 0,00 | -200,00 |  | 200,00 |
| 207 | Fonds commercial | 60 000,00 | 0,00 | 60 000,00 |  |
| 2135 | Installations générales, agencements | 85 000,00 | 0,00 | 85 000,00 |  |
| 2154 | Matériel industriel (outillage atelier) | 66 000,00 | 0,00 | 66 000,00 |  |
| 2182 | Matériel de transport | 56 000,00 | -24 000,00 | 32 000,00 |  |
| 2183 | Matériel de bureau et informatique | 9 000,00 | 0,00 | 9 000,00 |  |
| 2184 | Mobilier | 6 000,00 | 0,00 | 6 000,00 |  |
| 275 | Dépôts et cautionnements versés | 7 000,00 | 0,00 | 7 000,00 |  |
| 28135 | Amort. installations, agencements | -51 000,00 | -8 500,00 |  | 59 500,00 |
| 28154 | Amort. matériel industriel | -26 700,00 | -8 900,00 |  | 35 600,00 |
| 28182 | Amort. matériel de transport | -42 400,00 | 15 200,00 |  | 27 200,00 |
| 28183 | Amort. matériel de bureau et informatique | -6 000,00 | -3 000,00 |  | 9 000,00 |
| 28184 | Amort. mobilier | -3 600,00 | -600,00 |  | 4 200,00 |
| 3710 | Stock de pièces détachées | 46 000,00 | 6 400,00 | 52 400,00 |  |
| 3720 | Stock de véhicules d'occasion | 98 000,00 | -28 900,00 | 69 100,00 |  |
| 3971 | Dépréciation du stock de pièces | 0,00 | -2 400,00 |  | 2 400,00 |
| 3972 | Dépréciation du stock de VO | -6 000,00 | 2 500,00 |  | 3 500,00 |
| 401 | Fournisseurs | -68 400,00 | 0,00 |  | 68 400,00 |
| 408 | Fournisseurs – factures non parvenues | 0,00 | -4 200,00 |  | 4 200,00 |
| 411 | Clients | 52 600,00 | -6 010,00 | 46 590,00 |  |
| 416 | Clients douteux ou litigieux | 0,00 | 4 800,00 | 4 800,00 |  |
| 418 | Clients – factures à établir | 0,00 | 3 780,00 | 3 780,00 |  |
| 421 | Personnel – rémunérations dues | 0,00 | 0,00 |  |  |
| 4282 | Dettes provisionnées pour congés payés | -14 800,00 | -1 400,00 |  | 16 200,00 |
| 431 | Sécurité sociale (URSSAF) | -8 400,00 | 0,00 |  | 8 400,00 |
| 437 | Autres organismes sociaux (retraite, prévoyance) | -3 300,00 | 0,00 |  | 3 300,00 |
| 4382 | Charges sociales sur congés à payer | -6 216,00 | -588,00 |  | 6 804,00 |
| 4421 | Prélèvements à la source (IR) | -1 100,00 | 0,00 |  | 1 100,00 |
| 444 | État – impôt sur les bénéfices (acomptes versés) | 15 000,00 | -17 576,00 |  | 2 576,00 |
| 44566 | TVA déductible sur ABS | 13 800,00 | 0,00 | 13 800,00 |  |
| 44571 | TVA collectée | -17 200,00 | -1 540,00 |  | 18 740,00 |
| 44586 | TVA sur factures non parvenues | 0,00 | 700,00 | 700,00 |  |
| 44587 | TVA sur factures à établir | 0,00 | -630,00 |  | 630,00 |
| 455 | Associé – compte courant Thierry Martin | -18 000,00 | 0,00 |  | 18 000,00 |
| 471 | Compte d'attente | -850,00 | 850,00 |  |  |
| 486 | Charges constatées d'avance | 0,00 | 15 300,00 | 15 300,00 |  |
| 491 | Dépréciation des comptes clients | 0,00 | -2 800,00 |  | 2 800,00 |
| 512 | Banque | 139 746,00 | 0,00 | 139 746,00 |  |
| 530 | Caisse | 1 150,00 | 0,00 | 1 150,00 |  |
| 6022 | Fournitures consommables atelier (huiles, ingrédients) | 18 000,00 | 0,00 | 18 000,00 |  |
| 60371 | Variation des stocks de pièces détachées | 0,00 | -6 400,00 |  | 6 400,00 |
| 60372 | Variation des stocks de VO | 0,00 | 28 900,00 | 28 900,00 |  |
| 6061 | Fournitures non stockables (eau, énergie) | 14 500,00 | 1 100,00 | 15 600,00 |  |
| 6063 | Petit outillage | 6 200,00 | 0,00 | 6 200,00 |  |
| 6064 | Fournitures administratives | 1 800,00 | 0,00 | 1 800,00 |  |
| 6071 | Achats de pièces détachées | 175 000,00 | 0,00 | 175 000,00 |  |
| 6072 | Achats de véhicules d'occasion | 365 000,00 | 0,00 | 365 000,00 |  |
| 611 | Sous-traitance générale (carrosserie) | 32 000,00 | 2 400,00 | 34 400,00 |  |
| 6132 | Locations immobilières | 52 500,00 | -10 500,00 | 42 000,00 |  |
| 6135 | Locations mobilières | 3 600,00 | 0,00 | 3 600,00 |  |
| 615 | Entretien et réparations | 7 800,00 | 0,00 | 7 800,00 |  |
| 616 | Primes d'assurances | 15 900,00 | -4 800,00 | 11 100,00 |  |
| 6226 | Honoraires | 9 600,00 | 0,00 | 9 600,00 |  |
| 6231 | Annonces et insertions | 8 400,00 | 0,00 | 8 400,00 |  |
| 6251 | Voyages et déplacements | 2 100,00 | 0,00 | 2 100,00 |  |
| 626 | Frais postaux et de télécommunications | 2 700,00 | 0,00 | 2 700,00 |  |
| 627 | Services bancaires | 1 900,00 | 0,00 | 1 900,00 |  |
| 6281 | Cotisations professionnelles | 1 200,00 | 0,00 | 1 200,00 |  |
| 6312 | Taxe d'apprentissage | 1 100,00 | 0,00 | 1 100,00 |  |
| 6333 | Participation formation professionnelle continue | 900,00 | 0,00 | 900,00 |  |
| 63511 | Cotisation foncière des entreprises | 3 100,00 | 0,00 | 3 100,00 |  |
| 6354 | Droits d'enregistrement (cartes grises) | 2 760,00 | -2 760,00 |  |  |
| 6411 | Salaires | 170 000,00 | 0,00 | 170 000,00 |  |
| 6412 | Congés payés | 0,00 | 1 400,00 | 1 400,00 |  |
| 6413 | Primes et gratifications | 6 000,00 | 0,00 | 6 000,00 |  |
| 6418 | Rémunération du gérant | 48 000,00 | 0,00 | 48 000,00 |  |
| 6451 | Cotisations URSSAF | 42 100,00 | 588,00 | 42 688,00 |  |
| 6453 | Cotisations retraite complémentaire | 13 500,00 | 0,00 | 13 500,00 |  |
| 6458 | Cotisations autres organismes sociaux | 2 800,00 | 0,00 | 2 800,00 |  |
| 646 | Cotisations sociales personnelles du gérant (SSI) | 19 500,00 | 0,00 | 19 500,00 |  |
| 6475 | Médecine du travail | 900,00 | 0,00 | 900,00 |  |
| 654 | Pertes sur créances irrécouvrables | 0,00 | 300,00 | 300,00 |  |
| 658 | Pénalités et amendes (subdivision selon la nomenclature 2025 du PCG) | 450,00 | 0,00 | 450,00 |  |
| 6611 | Intérêts des emprunts | 1 220,00 | 200,00 | 1 420,00 |  |
| 675 | Valeurs comptables des éléments d'actif cédés | 0,00 | 200,00 | 200,00 |  |
| 6811 | Dotations aux amortissements des immobilisations | 0,00 | 29 600,00 | 29 600,00 |  |
| 6815 | Dotations aux provisions d'exploitation | 0,00 | 640,00 | 640,00 |  |
| 6817 | Dotations aux dépréciations des actifs circulants | 0,00 | 8 700,00 | 8 700,00 |  |
| 695 | Impôts sur les bénéfices | 0,00 | 17 576,00 | 17 576,00 |  |
| 7061 | Prestations atelier (main-d'œuvre) | -395 000,00 | -1 800,00 |  | 396 800,00 |
| 7071 | Ventes de pièces détachées | -300 000,00 | -1 350,00 |  | 301 350,00 |
| 7072 | Ventes de VO – régime de la marge | -310 000,00 | 11 100,00 |  | 298 900,00 |
| 7073 | Ventes de VO – régime normal | -140 000,00 | -9 500,00 |  | 149 500,00 |
| 7088 | Produits des activités annexes | -8 760,00 | 2 760,00 |  | 6 000,00 |
| 758 | Produits divers de gestion courante | -400,00 | 0,00 |  | 400,00 |
| 775 | Produits des cessions d'éléments d'actif | -8 000,00 | 0,00 |  | 8 000,00 |
| 7817 | Reprises sur dépréciations des actifs circulants | 0,00 | -6 000,00 |  | 6 000,00 |
| | **Totaux** | | | **1 716 440,00** | **1 716 440,00** |

**Contrôles finaux :**
- Résultat = produits (classe 7) 1 166 950,00 – charges (classe 6) 1 097 674,00 = **69 276,00 €** (bénéfice), identique au résultat du bilan (partie 2).
- 471 soldé ✔ ; 421 nul ✔ ; 444 créditeur de 2 576 € = solde d'IS à payer ✔ ; 28182 = 27 200 € = amortissements de la seule dépanneuse (20 800 + 6 400) ✔ ; 1641 + 1688 = 30 200 € ✔.

## 4. Points d'attention / pièges

- **Oublier la dotation complémentaire du bien cédé** avant de le sortir : la VNC serait fausse (2 400 au lieu de 200) et la plus-value sous-évaluée — résultat global identique, mais présentation fausse (exploitation / exceptionnel).
- **Compter le véhicule en dépôt-vente** : il gonflerait le stock de 15 750 € (prix de vente estimé) ou de son « coût », alors que le garage n'en est pas propriétaire. Le contrat de mandat le prouve.
- **Déprécier les VO au forfait** (« 10 % sur les VO de plus de 6 mois ») : la dépréciation doit être **justifiée véhicule par véhicule** (valeur de marché, cote, offres). L'ancienneté n'est qu'un **indice** qui déclenche le test.
- **Déprécier la créance douteuse sur le TTC** : erreur classique. La dépréciation porte sur le HT.
- **Régime de la marge** : il ne s'applique qu'aux biens acquis **sans TVA déductible** (particulier, assujetti lui-même au régime de la marge, etc.). Un VO acheté avec une facture mentionnant de la TVA récupérée sort du régime.
- **Débours** : les comptabiliser en charges/produits gonfle le CA et fausse les ratios (et, si la TVA a été appliquée à tort, crée un rappel). Conditions : dépense engagée au nom et pour le compte du client, en vertu d'un mandat, refacturée pour son montant exact et suivie en compte de passage.
- **Garder les provisions N-1 « en l'état »** : la provision pour garanties et la dette de CP doivent être **réestimées** à chaque clôture.
- **TVA** : les régularisations Mégane et Roux sont à **reporter sur la CA3 de septembre** (déposée en octobre). Si elle avait déjà été déposée, régularisation sur la CA3 suivante.

## 5. Ce qu'un senior ferait en plus

- **Documenter chaque écriture** dans le dossier de travail (référence de la feuille de travail en libellé, pièce justificative scannée : relevé de parc signé, inventaire pièces, attestation du mandataire, certificat d'irrécouvrabilité, BL carrosserie, tableau d'emprunt).
- **Mail au client** pour sécuriser les points sensibles :
  > « Bonjour Thierry, pour boucler le bilan, j'ai besoin de : (1) l'inventaire pièces détaillé signé (pas seulement le total), (2) une copie du contrat de dépôt-vente de la BMW de M. Faure, (3) votre confirmation écrite des prix de vente que vous estimez pour la Golf et la C3 (9 500 € et 5 200 €). Par ailleurs, la Mégane achetée chez Auto Distribution Rhône ne pouvait pas être vendue sous le régime de la marge : nous corrigeons la TVA sur la déclaration de septembre (1 600 € de TVA en plus). Pour l'avenir, vos VO achetés à des professionnels avec TVA doivent être facturés avec TVA sur le prix total. Bien cordialement. »
- **Procédure pour N+1** : un code « régime » (marge / normal) dans le logiciel de gestion VO dès l'achat ; un compte 467 pour les cartes grises ; une revue mensuelle du 471.
- **Suivi de la créance Vidal** : surveiller le plan de redressement ; si la liquidation est prononcée, passer la perte et récupérer la TVA.

## 6. Références

- PCG (règlement ANC n° 2014-03 modifié notamment par le règlement ANC n° 2022-06) : définition des actifs, amortissements (prorata temporis), dépréciation des stocks et créances, provisions (passif : obligation, sortie de ressources probable, estimation fiable), résultat exceptionnel restreint.
- CGI, art. 39-1-5° (provisions déductibles), art. 39-2 (amendes et pénalités non déductibles), art. 297 A (régime de la marge sur les biens d'occasion), art. 272 (récupération de la TVA sur créances irrécouvrables), art. 267 (exclusion des débours de la base d'imposition).
- Code de commerce, art. L. 123-12 et suivants (inventaire, comptes annuels) ; art. L. 622-24 (déclaration des créances dans une procédure collective).
