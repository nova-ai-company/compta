# Corrigé E06-03 — Le nouveau four à sole et la reprise de l'ancien

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-03](../exercices/E06-03_four-reprise-boulangerie-dupain.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — Décomposer la facture (question 1).** Une facture d'équipement mélange presque toujours le bien, ses frais accessoires et des services qui n'ont rien à faire dans le coût.

| Ligne | Traitement | Compte | Raison |
|---|---|---|---|
| Four 41 500 | Immobilisation | 2154 | Bien principal |
| Chambre de pousse 6 200 | Immobilisation **distincte** | 2154 | Équipement séparable, durée propre (8 ans) |
| Livraison 650 | Coût du four | 2154 | Frais directement attribuables (mise en place) |
| Installation, raccordement, hotte 1 400 | Coût du four | 2154 | Mise en état de fonctionnement |
| Démontage de l'ancien four 750 | **Charge** | 6155 | Se rattache à la **sortie** de l'ancien bien |
| Formation 480 | **Charge** | 618 (subdivision selon la nomenclature 2025 du PCG) | La formation est exclue du coût |
| Extension de garantie 1 140 | **Charge**, étalée | 6156 + 486 | Service rendu sur 3 ans (01/10/2026 → 30/09/2029) |

Coût d'entrée : **four = 41 500 + 650 + 1 400 = 43 550 €** ; **chambre de pousse = 6 200 €**. (On affecte la livraison et l'installation au four, qui les a générées ; une répartition au prorata serait aussi défendable, si elle est documentée.)

**Étape 2 — La reprise (question 2).** Juridiquement, il y a **deux ventes** : Thermo-Fournil vend un four neuf à la boulangerie (52 120 € HT), et **la boulangerie vend son vieux four** à Thermo-Fournil (2 400 € HT). Les deux dettes se compensent ensuite. Conséquences :
- la cession d'un bien meuble d'investissement dont la TVA a été déduite est **taxable à 20 %** : la boulangerie **collecte** 480 € de TVA ;
- elle doit **émettre une facture** de cession (ou Thermo-Fournil l'émet en son nom et pour son compte dans le cadre d'un **mandat d'autofacturation** écrit) ;
- comptablement, on ne déduit **jamais** la reprise du coût du nouveau bien : le nouveau four est inscrit pour son coût complet et l'ancien sort avec un prix de cession en 775.

La facture de Thermo-Fournil, en calculant la TVA sur le net (49 720 €), aboutit au même montant net de TVA (10 424 – 480 = 9 944), mais elle **masque** une TVA collectée et une cession : la déclaration de TVA et les comptes seraient faux dans leurs composantes. On demande la facture de cession (pièce manquante).

**Étape 3 — L'acompte.** Il porte sur une **livraison de biens** : la TVA n'est exigible qu'à la livraison, d'où l'absence de facture d'acompte avec TVA — c'est normal. En revanche, l'acompte sur une immobilisation se comptabilise en **238 Avances et acomptes versés sur commandes d'immobilisations corporelles**, et non au débit du 401 (qui mélangerait dettes d'exploitation et d'investissement).

**Étape 4 — Dates.** Livraison (transfert de propriété) : 28/09 ; mise en service : **01/10/2026**. En linéaire, l'amortissement part de la mise en service (3 mois sur 2026). En dégressif, il partirait du 1er jour du mois d'acquisition (septembre → 4 mois).

**Étape 5 — Facture électronique.** Depuis le 01/09/2026, la boulangerie doit être en mesure de **recevoir** des factures électroniques via sa plateforme agréée. Thermo-Fournil, si c'est une PME, n'est tenue d'**émettre** en format électronique qu'à compter du 01/09/2027 : le PDF reçu par e-mail reste acceptable en septembre 2026. À vérifier : la taille de Thermo-Fournil (si c'était une ETI/GE, la facture aurait dû transiter par une PA).

## 2. Calculs (détaillés, chaque montant justifié)

**Ancien four (question 3)**

| Élément | Calcul | Montant |
|---|---|---:|
| Annuité | 32 000 / 10 | 3 200,00 |
| Cumul au 31/12/2025 | 6,5 ans × 3 200 | 20 800,00 |
| Dotation 2026 jusqu'au 30/09 | 3 200 × 9/12 | **2 400,00** |
| Cumul à la sortie | | 23 200,00 |
| **VNC** | 32 000 – 23 200 | **8 800,00** |
| Prix de cession | | 2 400,00 |
| **Moins-value** | 2 400 – 8 800 | **– 6 400,00** |

**Nouveaux biens — linéaire**

| Bien | Coût | Durée | Annuité | Dotation 2026 (01/10 → 31/12, 90/360) |
|---|---:|---:|---:|---:|
| Four | 43 550,00 | 10 ans | 4 355,00 | **1 088,75** |
| Chambre de pousse | 6 200,00 | 8 ans | 775,00 | **193,75** |
| **Total** | | | | **1 282,50** |

**TVA**
- Déductible sur immobilisations (44562) : (43 550 + 6 200) × 20 % = **9 950,00**
- Déductible sur ABS (44566) : (750 + 480 + 1 140) × 20 % = 2 370 × 20 % = **474,00**
- Total déductible : 10 424,00 ; collectée sur la cession : **480,00** ; net = 9 944,00 = TVA de la facture ✓.

**Règlements** : TTC brut 52 120 × 1,20 = 62 544,00 – cession TTC 2 880,00 – acompte 15 000,00 = **44 664,00** = net à payer ✓.

**Extension de garantie** : 1 140 / 36 mois = 31,67 €/mois ; charge 2026 = 1 140 × 3/36 = **95,00** ; **CCA** = 1 140 × 33/36 = **1 045,00**.

**Option dégressif (question 5)** — le four et la chambre de pousse sont des **matériels industriels neufs** de durée ≥ 3 ans : éligibles.
- Four : 10 ans → taux 10 % × 2,25 = 22,5 % ; 2026 : 43 550 × 22,5 % × 4/12 = **3 266,25**
- Chambre de pousse : 8 ans → 12,5 % × 2,25 = 28,125 % ; 2026 : 6 200 × 28,125 % × 4/12 = **581,25**
- Total dégressif 2026 : **3 847,50** contre 1 282,50 en linéaire, soit **2 565,00 €** de déduction supplémentaire en 2026 → économie d'IS au taux de 15 % : **384,75 €** (un **décalage**, pas une économie définitive).

## 3. Écritures comptables

La proposition du stagiaire est **rejetée** ; on saisit directement les bonnes écritures (et on reclasse l'acompte).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 13/06/2026 | BQ | 238 | Avances et acomptes versés sur immobilisations corporelles | Acompte BC-0614 Thermo-Fournil (reclassé du 401) | 15 000,00 | |
| 13/06/2026 | BQ | 512 | Banque | Acompte BC-0614 | | 15 000,00 |
| 28/09/2026 | AC | 2154 | Matériel industriel – four à sole 5 étages | TF-26-1187 four + livraison + installation | 43 550,00 | |
| 28/09/2026 | AC | 2154 | Matériel industriel – chambre de pousse | TF-26-1187 chambre de pousse | 6 200,00 | |
| 28/09/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | TF-26-1187 démontage ancien four | 750,00 | |
| 28/09/2026 | AC | 618 | Divers – formation du personnel (subdivision nomenclature 2025) | TF-26-1187 formation | 480,00 | |
| 28/09/2026 | AC | 6156 | Maintenance | TF-26-1187 extension garantie 3 ans | 1 140,00 | |
| 28/09/2026 | AC | 44562 | TVA sur immobilisations | TF-26-1187 | 9 950,00 | |
| 28/09/2026 | AC | 44566 | TVA sur autres biens et services | TF-26-1187 | 474,00 | |
| 28/09/2026 | AC | 404 | Fournisseurs d'immobilisations – Thermo-Fournil | TF-26-1187 (brut, avant reprise) | | 62 544,00 |
| 30/09/2026 | VT | 462 | Créances sur cessions d'immobilisations | Cession ancien four à Thermo-Fournil | 2 880,00 | |
| 30/09/2026 | VT | 775 | Produits des cessions d'éléments d'actif | Cession ancien four | | 2 400,00 |
| 30/09/2026 | VT | 44571 | TVA collectée | Cession ancien four 20 % | | 480,00 |
| 30/09/2026 | OD | 404 | Fournisseurs d'immobilisations – Thermo-Fournil | Compensation reprise | 2 880,00 | |
| 30/09/2026 | OD | 462 | Créances sur cessions d'immobilisations | Compensation reprise | | 2 880,00 |
| 30/09/2026 | OD | 404 | Fournisseurs d'immobilisations – Thermo-Fournil | Imputation acompte du 13/06 | 15 000,00 | |
| 30/09/2026 | OD | 238 | Avances et acomptes versés sur immobilisations corporelles | Imputation acompte | | 15 000,00 |
| 30/09/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Ancien four : 9 mois 2026 | 2 400,00 | |
| 30/09/2026 | OD | 28154 | Amortissements du matériel industriel | Ancien four | | 2 400,00 |
| 30/09/2026 | OD | 28154 | Amortissements du matériel industriel | Sortie ancien four | 23 200,00 | |
| 30/09/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie ancien four (VNC) | 8 800,00 | |
| 30/09/2026 | OD | 2154 | Matériel industriel | Sortie ancien four | | 32 000,00 |
| 15/10/2026 | BQ | 404 | Fournisseurs d'immobilisations – Thermo-Fournil | Règlement solde TF-26-1187 | 44 664,00 | |
| 15/10/2026 | BQ | 512 | Banque | Règlement solde TF-26-1187 | | 44 664,00 |
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Four + chambre de pousse (3 mois) | 1 282,50 | |
| 31/12/2026 | OD | 28154 | Amortissements du matériel industriel | Four 1 088,75 + chambre 193,75 | | 1 282,50 |
| 31/12/2026 | OD | 486 | Charges constatées d'avance | Garantie 33/36 | 1 045,00 | |
| 31/12/2026 | OD | 6156 | Maintenance | Garantie 33/36 | | 1 045,00 |
| | | | | **Totaux** | **179 695,50** | **179 695,50** |

Le 404 Thermo-Fournil est soldé : 62 544 – 2 880 – 15 000 – 44 664 = 0 ✓. Le 238 est soldé ✓. Le 401 Thermo-Fournil, débité à tort en juin, doit être soldé par le reclassement de l'acompte (D 238 / C 401 si la saisie initiale est conservée).

**Impact sur le résultat 2026** : 750 + 480 + 95 + 2 400 + 8 800 – 2 400 + 1 282,50 = **11 407,50 €** de charges nettes.

## 4. Points d'attention / pièges

**Erreurs du stagiaire (question 6)**
1. Coût du four **minoré de la reprise** (2 400 €) : on ne compense pas un achat et une vente.
2. Démontage, formation et garantie (2 370 €) **immobilisés** : ce sont des charges (garantie étalée).
3. Un seul bien au lieu de deux (four 10 ans / chambre de pousse 8 ans).
4. Ancien four **non sorti** : « amorti à 65 % » n'est pas une raison de le garder ; il n'existe plus. VNC de 8 800 € restée à l'actif, et le fichier aurait continué à l'amortir (3 200 €/an).
5. Point de départ au 28/09 (livraison) au lieu du **01/10** (mise en service) en linéaire.
6. Acompte resté au **401** au lieu du **238**, et non imputé.
7. TVA collectée sur la cession absente de la CA12 (et TVA déductible minorée d'autant) : sans effet sur le net, mais déclaration fausse dans ses lignes.

**Autres pièges**
- Régime simplifié : la TVA sur immobilisations s'impute sur la **CA12 annuelle** ; si le crédit est important, une demande de remboursement en cours d'année est possible sous conditions (*seuils et formulaire à vérifier*).
- **Dégressif** : c'est un choix **fiscal** (art. 39 A) qui peut être pratiqué en comptabilité si le rythme de consommation le justifie, ou via des **amortissements dérogatoires** si le plan comptable reste linéaire (cf. E06-10). Pour une boulangerie au taux de 15 %, l'enjeu est faible (≈ 385 € de décalage en 2026) ; il ne justifie pas à lui seul la complexité.
- Le **contrat de crédit-bail** du four ventilé n'a rien à voir avec ce four : ne pas le mélanger dans le fichier des immobilisations.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Message à Marc Dupain (à envoyer l'après-midi)**

> Bonjour Marc,
>
> Le nouveau four est bien enregistré. Une précision : la reprise de l'ancien four est, fiscalement, une vente faite par la boulangerie. Il nous faut une facture de cession de 2 400 € HT + 480 € de TVA, au nom de Thermo-Fournil. Le plus simple : demandez à Thermo-Fournil s'ils peuvent l'établir pour votre compte (autofacturation) ou nous vous préparons le modèle.
>
> La formation et l'extension de garantie sont des charges, pas des investissements. Enfin, vous pouvez amortir plus vite le four (dégressif), mais le gain d'impôt 2026 serait d'environ 385 € et il sera « repris » les années suivantes : nous vous conseillons de rester en linéaire, sauf si vous préférez anticiper.

**Contrôles et documentation**
- Vérifier le **numéro de série** (26-4471) dans le fichier des immobilisations : c'est ce qui permettra de rapprocher le bien en cas de contrôle ou de sinistre.
- Mettre à jour l'**attestation d'assurance** multirisque (valeur du nouveau matériel).
- Conserver le bon de commande (BC-0614) avec la preuve de l'acompte.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : coût d'acquisition (éléments inclus et exclus), sortie des immobilisations, compte 238.
- CGI, art. 256 et 266 : cession d'un bien meuble d'investissement soumise à la TVA ; art. 269-2-a : exigibilité à la livraison pour les livraisons de biens.
- CGI, art. 289 et annexe II : facturation, autofacturation sur mandat ; calendrier de la facturation électronique (réception 01/09/2026, émission PME 01/09/2027).
- CGI, art. 39 A : amortissement dégressif (coefficients 1,25 / 1,75 / 2,25) ; BOFiP, BIC – Amortissements – dégressif.
