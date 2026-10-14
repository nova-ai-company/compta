# Corrigé E14-10 — Location longue durée de véhicules (VP et VU) et relevé de carte carburant : quelle TVA récupérer ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-10](../exercices/E14-10_lld-vehicules-vp-vu-carte-carburant.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Le principe
La TVA grevant les **véhicules conçus pour transporter des personnes ou à usage mixte** (véhicules de tourisme, M1) est **exclue du droit à déduction**, ainsi que celle des **services portant sur ces véhicules** (location, entretien, réparation). Les véhicules **utilitaires** (N1 « CTTE ») ouvrent droit à déduction dans les conditions normales. Pour les **carburants**, des règles propres : gazole et essence → **80 %** pour les VP, **100 %** pour les VU ; l'**électricité** utilisée pour recharger un véhicule n'est pas un produit pétrolier et relève du droit commun (déduction admise, y compris pour un VP — *à vérifier au BOFiP en vigueur*).

### Ventilation (question 1)

| Ligne | Compte | TVA récupérable | Justification |
|---|---|---|---|
| VP1 loyer 420,00 + 84,00 | 6135 : **504,00** TTC | 0 | Location d'un VP : exclusion |
| VP1 entretien 45,00 + 9,00 | 6155 : **54,00** TTC | 0 | Service sur un VP : exclusion |
| VP2 loyer 390,00 + 78,00 | 6135 : **468,00** TTC | 0 | VP, même électrique : exclusion |
| VP2 entretien 30,00 + 6,00 | 6155 : **36,00** TTC | 0 | Service sur un VP |
| VU loyers 930,00 | 6135 : 930,00 HT | **186,00** | VU : droit commun |
| VU entretien 120,00 | 6155 : 120,00 HT | **24,00** | VU : droit commun |
| Assurance 190,00 | 616 : 190,00 | — | Exonérée (pas de TVA) |
| Essence VP1 342,00 (TVA 57,00) | 6061 : 296,40 | **45,60** (80 %) | Essence d'un VP : 80 % |
| Recharge VP2 64,80 (TVA 10,80) | 6061 : 54,00 | **10,80** | Électricité : droit commun (*à vérifier*) |
| Gazole VU 1 020,00 (TVA 170,00) | 6061 : 850,00 | **170,00** | Gazole d'un VU : 100 % |
| Péages VU1 84,00 (TVA 14,00) | 6251 : 70,00 | **14,00** | Dépense professionnelle d'un VU |
| Lavage VP1 18,00 (TVA 3,00) | 6155 : 18,00 TTC | 0 | Service portant sur un VP : exclusion |
| Boutique 7,20 | 425 : 7,20 | 0 | Dépense personnelle, à retenir sur paie |

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| TVA récupérable – loyers | 186,00 + 24,00 | 210,00 € |
| TVA récupérable – carburants & péages | 45,60 + 10,80 + 170,00 + 14,00 | 240,40 € |
| **TVA récupérable du mois** | 210,00 + 240,40 | **450,40 €** |
| TVA non récupérable – loyers VP | 84,00 + 9,00 + 78,00 + 6,00 | 177,00 € |
| TVA non récupérable – essence (20 %) et lavage | 57,00 × 20 % = 11,40 + 3,00 | 14,40 € |
| **Surcoût de TVA non récupérable** | 177,00 + 14,40 | **191,40 €** |
| Ancien process (tout récupéré) : TVA déduite | 387,00 + 57,00 + 10,80 + 170,00 + 14,00 + 3,00 | 641,80 € |
| Déduction à tort évitée | 641,80 − 450,40 | 191,40 € / mois |

Sur un an et pour deux VP, le « tout en 44566 » représentait environ 2 300 € de TVA déduite à tort, pour cette seule filiale — c'est le genre de chiffre qu'un contrôle fiscal retrouve en une heure.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/09/2026 | AC | 6135 | Locations mobilières | ALF ALF-2026-09-5521 loyers VP1+VP2 TTC (TVA non déd.) | 972,00 | |
| 01/09/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | ALF ALF-2026-09-5521 entretien VP1+VP2 TTC | 90,00 | |
| 01/09/2026 | AC | 6135 | Locations mobilières | ALF ALF-2026-09-5521 loyers VU1-VU3 | 930,00 | |
| 01/09/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | ALF ALF-2026-09-5521 entretien VU1-VU3 | 120,00 | |
| 01/09/2026 | AC | 616 | Primes d'assurances | ALF ALF-2026-09-5521 assurance 5 véhicules | 190,00 | |
| 01/09/2026 | AC | 44566 | TVA déductible sur ABS | ALF ALF-2026-09-5521 TVA VU | 210,00 | |
| 01/09/2026 | AC | 401ALF | Fournisseur AutoLease France | ALF ALF-2026-09-5521 loyers 09/2026 | | 2 512,00 |
| 30/09/2026 | AC | 6061 | Fournitures non stockables (énergie, carburants) | ALF-CC-2026-09 essence VP1 (TVA 80 %) | 296,40 | |
| 30/09/2026 | AC | 6061 | Fournitures non stockables (énergie, carburants) | ALF-CC-2026-09 recharge VP2 | 54,00 | |
| 30/09/2026 | AC | 6061 | Fournitures non stockables (énergie, carburants) | ALF-CC-2026-09 gazole VU1-VU3 | 850,00 | |
| 30/09/2026 | AC | 6251 | Voyages et déplacements | ALF-CC-2026-09 péages VU1 | 70,00 | |
| 30/09/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | ALF-CC-2026-09 lavage VP1 TTC | 18,00 | |
| 30/09/2026 | AC | 425 | Personnel – avances et acomptes | ALF-CC-2026-09 achat boutique Y. Morel à retenir | 7,20 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | ALF-CC-2026-09 TVA récupérable | 240,40 | |
| 30/09/2026 | AC | 401ALF | Fournisseur AutoLease France | ALF-CC-2026-09 carte carburant 09/2026 | | 1 536,00 |
| | | | | **Totaux** | **4 048,00** | **4 048,00** |

> En analytique, chaque ligne est affectée à l'établissement utilisateur (VP1 : Nice ; VP2 : Antibes ; VU : établissement de rattachement de chaque véhicule) — la flotte est un coût de l'établissement, pas du siège.

## 4. Points d'attention / pièges

- **« Électrique » ne veut pas dire « TVA récupérable »** sur le loyer : l'exclusion vise la catégorie du véhicule (tourisme), pas son énergie. Seule l'électricité de recharge suit le droit commun.
- **Le lavage, l'entretien, les pneus d'un VP** : TVA non récupérable (services portant sur un bien exclu) ; l'erreur classique est de les traiter comme le carburant (80 %).
- **Assurance** : exonérée, aucune TVA à chercher ; vérifier que le TTC de la facture n'en contient pas.
- **La retenue de 7,20 €** sur la paie de Y. Morel suppose une information préalable et le respect des règles de retenue sur salaire ; la politique flotte doit être signée par les titulaires de carte. Si la retenue n'est pas faite, la somme devient un avantage à déclarer ou une charge non justifiée.
- **Qualification VU** : on se fie à la carte grise (genre « CTTE », catégorie N1) et au nombre de places ; une camionnette aménagée avec banquette arrière peut perdre sa qualité d'utilitaire.
- **Option pour les débits** sur la facture AutoLease : la TVA des VU est déductible dès la facture.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Note à Sophie Garnier (question 4)** :
> 1) VP1 et VP2 entrent dans le calcul des **taxes annuelles sur l'affectation des véhicules de tourisme** à des fins économiques (taxe CO2 et taxe polluants ; VP2 électrique en principe exonéré — *barèmes et exonérations à vérifier*) : charge **non déductible** du résultat fiscal, à réintégrer sur la 2058-A. 2) Pour les VP en LLD, la fraction du loyer correspondant à l'amortissement pratiqué par le loueur au-delà du plafond fiscal (art. 39-4 CGI, plafond fonction des émissions de CO2) est **non déductible** : à réintégrer à partir du montant communiqué chaque année par AutoLease.

**Réponse au chef d'établissement de Nice (question 5)** :
> « Passer en électrique ne rend pas la TVA du loyer récupérable : un VP reste un VP. Le gain de TVA porte seulement sur l'énergie (électricité récupérable contre 80 % pour l'essence). En revanche, l'électrique a d'autres avantages fiscaux pour le groupe : exonération probable des taxes annuelles sur les VP, plafond de déductibilité des loyers plus élevé, avantage en nature souvent minoré pour vous en paie (*à vérifier*). La décision relève de la politique flotte du groupe ; je peux chiffrer les deux options si vous le souhaitez. »

**Contrôles** : fichier flotte (immatriculation, catégorie M1/N1, genre carte grise, énergie, établissement, titulaire de carte) servant de table de paramétrage des codes TVA dans l'ERP ; revue mensuelle des achats « boutique » et des pleins hors jours ouvrés ; rapprochement carte carburant / kilométrage.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI annexe II art. 206-IV-2-6° : exclusion des véhicules conçus pour transporter des personnes et des services s'y rapportant.
- CGI art. 298-4-1° : déductibilité de la TVA sur les carburants (80 % / 100 %).
- BOFiP, TVA – Droits à déduction – exclusions (véhicules) et carburants (*références précises et règles pour l'électricité à vérifier*).
- CGI art. 261 C : exonération des opérations d'assurance.
- CGI art. 39-4 : limitation de la déductibilité de l'amortissement des VP (et des loyers correspondants).
- CIBS (Code des impositions sur les biens et services) : taxes annuelles sur l'affectation des véhicules de tourisme (*articles à vérifier*).
