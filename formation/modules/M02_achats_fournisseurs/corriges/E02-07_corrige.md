# Corrigé E02-07 — Le relevé mensuel des cartes carburant

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-07](../exercices/E02-07_releve-carte-carburant-leroy.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 : classer les véhicules** d'après la carte grise, pas d'après l'usage déclaré.
- **Poids lourds** (tracteurs) et **camionnettes « CTTE »** (Master, Kangoo Van) : véhicules conçus pour le transport de marchandises → **hors exclusion**, TVA déductible à 100 % sur tout (carburant, entretien, lavage).
- **Peugeot 508 et Clio « VP »** : véhicules conçus pour le transport de personnes → **véhicules exclus** du droit à déduction (achat, location, entretien, services afférents), avec un régime particulier pour les **carburants**.

**Étape 2 : appliquer les règles par dépense (question 1)**

| Dépense | Tracteurs, Master, Kangoo (VU / PL) | 508, Clio (VP) |
|---|---|---|
| Gazole | 100 % | **80 %** |
| Essence (SP95, SP95-E10) | 100 % | **80 %** (alignement sur le gazole achevé en 2022) |
| AdBlue | 100 % (fourniture, pas un carburant) | — |
| Péages autoroutiers | 100 % | Position généralement admise : déductible (dépense de déplacement, distincte des services afférents au véhicule) — **à confirmer** dans le BOFiP en vigueur ; enjeu ici : 17,00 € |
| Lavage | 100 % | **0 %** (service afférent à un véhicule exclu) |

**Étape 3 : la facture.** Une facture récapitulative mensuelle d'un émetteur de cartes est une facture valable dès lors qu'elle détaille les produits, quantités et TVA par taux. Les **péages** sont « refacturés » : les factures détaillées des sociétés d'autoroute sont disponibles sur l'espace client — à télécharger et conserver, elles justifient la déduction.

## 2. Calculs (détaillés, chaque montant justifié)

| Ligne | HT | TVA facturée | Taux de déduction | TVA déductible | TVA non déductible | Compte |
|---|---|---|---|---|---|---|
| Gazole tracteurs (21 450 × 1,4250) | 30 566,25 | 6 113,25 | 100 % | 6 113,25 | 0,00 | 6061 |
| Gazole Master (380 × 1,4400) | 547,20 | 109,44 | 100 % | 109,44 | 0,00 | 6061 |
| Gazole 508 (210 × 1,4600) | 306,60 | 61,32 | 80 % | 49,06 | 12,26 | 6061 |
| SP95-E10 Clio (160 × 1,4900) | 238,40 | 47,68 | 80 % | 38,14 | 9,54 | 6061 |
| SP95 Kangoo (95 × 1,5100) | 143,45 | 28,69 | 100 % | 28,69 | 0,00 | 6061 |
| AdBlue (1 200 × 0,5500) | 660,00 | 132,00 | 100 % | 132,00 | 0,00 | 6068 |
| Péages PL | 2 755,00 | 551,00 | 100 % | 551,00 | 0,00 | 6251 |
| Péages 508 | 85,00 | 17,00 | 100 % (à confirmer) | 17,00 | 0,00 | 6251 |
| Lavage PL (12 × 35,00) | 420,00 | 84,00 | 100 % | 84,00 | 0,00 | 6155 |
| Lavage 508 | 25,00 | 5,00 | 0 % | 0,00 | 5,00 | 6155 |
| **Total (hors boutique)** | **35 746,90** | **7 149,38** | | **7 122,58** | **26,80** | |

Détail des 80 % : 61,32 × 80 % = 49,056 → 49,06 € ; 47,68 × 80 % = 38,144 → 38,14 €.

**Imputation des charges (TVA non déductible incluse dans la charge)** :
- 6061 Carburants : 30 566,25 + 547,20 + 306,60 + 238,40 + 143,45 = 31 801,90 € + TVA non déductible 12,26 + 9,54 = **31 823,70 €** ;
- 6068 AdBlue : **660,00 €** ;
- 6251 Péages : 2 755,00 + 85,00 = **2 840,00 €** ;
- 6155 Lavage : 420,00 + 25,00 + 5,00 = **450,00 €** ;
- Boutique : **41,58 €** TTC, en attente (voir question 4).

Contrôle : 31 823,70 + 660,00 + 2 840,00 + 450,00 + 7 122,58 + 41,58 = **42 937,86 €** = total prélevé ✓.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 6061 | Fournitures non stockables – carburants | CarbuPro CP-2026-09-018834 carburants 09/2026 (dont TVA non déd. VP 21,80) | 31 823,70 | |
| 30/09/2026 | AC | 6068 | Autres matières et fournitures (AdBlue) | CarbuPro CP-2026-09-018834 AdBlue | 660,00 | |
| 30/09/2026 | AC | 6251 | Voyages et déplacements (péages) | CarbuPro CP-2026-09-018834 péages | 2 840,00 | |
| 30/09/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | CarbuPro CP-2026-09-018834 lavages (dont TVA non déd. 508) | 450,00 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | CarbuPro CP-2026-09-018834 TVA déductible | 7 122,58 | |
| 30/09/2026 | AC | 471 | Compte d'attente | CarbuPro CP-2026-09-018834 boutique carte PL 09 – justif. demandé | 41,58 | |
| 30/09/2026 | AC | 401CARB | Fournisseur CarbuPro Services | CarbuPro CP-2026-09-018834 | | 42 937,86 |
| 10/10/2026 | BQ | 401CARB | Fournisseur CarbuPro Services | Prlv CarbuPro CP-2026-09-018834 | 42 937,86 | |
| 10/10/2026 | BQ | 512 | Banque | Prlv CarbuPro CP-2026-09-018834 | | 42 937,86 |
| | | | | **Totaux** | **85 875,72** | **85 875,72** |

> Pour le suivi analytique (coût de revient par véhicule, nécessaire au calcul des prix de transport), ventilez 6061 par sous-comptes ou axes : « PL », « VU », « VP direction », « VP commercial ».

## 4. Points d'attention / pièges

- **Question 4 — la ligne « Boutique »** : 41,58 € sans détail, sur la carte d'un tracteur. Une carte carburant n'a pas vocation à payer des achats de boutique (snacks, boissons, cigarettes…). Sans facture détaillée : **aucune TVA déductible**, et la nature de la dépense n'est pas justifiée. On l'isole en 471, on demande le ticket au chauffeur ; s'il s'agit d'un achat personnel → **retenue sur salaire** (avec son accord, et dans le respect des règles de retenue) ou remboursement ; s'il s'agit d'un achat pour le camion (ampoule, liquide lave-glace) → reclassement avec TVA sur présentation du ticket détaillé. Recommander au client de **bloquer** les achats boutique sur les cartes PL (paramétrage chez l'émetteur).
- **Question 5 — l'erreur des mois précédents** : saisie en bloc, toute la TVA déduite. TVA déduite à tort en septembre si l'on avait fait pareil : **26,80 €** (12,26 + 9,54 + 5,00), soit environ **320 € par an** (26,80 × 12 = 321,60 €) depuis l'arrivée des deux VP. Montant faible, mais **systématique** et facile à repérer en contrôle ; régularisation à prévoir sur une prochaine CA3 pour les mois de 2026 concernés.
- **La TVA non déductible n'est pas perdue fiscalement** : elle s'ajoute à la charge (déductible du résultat).
- **Essence des VU** : 100 % depuis 2022 — ne pas appliquer 80 % au Kangoo par habitude.
- **Véhicules de tourisme** : penser aussi aux autres conséquences fiscales (amortissements non déductibles au-delà des plafonds, taxes annuelles sur les véhicules de tourisme affectés à des fins économiques) — renvoi au module fiscalité.
- **Avantage en nature** : si Bruno Leroy utilise la 508 à titre privé, l'avantage (y compris carburant) doit être évalué et soumis à cotisations (module paie).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — TICPE.** Volume éligible : 21 450 litres de gazole des tracteurs = **214,50 hl**. Remboursement estimé : 214,50 × 15,25 = **3 271,13 €** (*taux à vérifier chaque année*). Le remboursement est **demandé** à l'administration pour chaque période de dépôt prévue (semestrielle ou selon les modalités en vigueur), sur la base des factures de carburant et de la liste des véhicules éligibles. Comptablement :
- au fil de l'eau, rien (le droit n'est constaté que si les conditions sont remplies) ;
- **à la clôture du 31/12**, le remboursement acquis au titre des consommations de l'exercice et non encore encaissé est constaté en **produit à recevoir** (compte de l'État, 4487) ;
- contrepartie : depuis la suppression des comptes de transfert de charges (règlement ANC 2022-06), on le présente **en diminution de la charge de carburant** (sous-compte de 6061 « remboursement TICPE ») ou en produit d'exploitation (74) selon la position retenue par le cabinet — **à valider avec Hélène Ferrand** et à appliquer de façon permanente.

**Message à Bruno Leroy :**

> Bonjour Monsieur Leroy,
>
> Nous avons repris la saisie des cartes carburant par véhicule. Pour la 508 et la Clio (véhicules de tourisme), la TVA n'est récupérable qu'à 80 % sur le carburant et pas du tout sur l'entretien et le lavage : cela représente environ 27 € par mois que nous ne pouvons plus déduire. Nous régulariserons les mois précédents de 2026.
>
> Par ailleurs, la carte du tracteur EH-409 a servi à un achat « boutique » de 41,58 € sans détail : pouvez-vous interroger le chauffeur ? Nous vous suggérons de demander à CarbuPro de bloquer les achats boutique sur les cartes poids lourds.
>
> Enfin, pensez à déposer la demande de remboursement partiel de TICPE : pour septembre, elle représente environ 3 270 €.

**Contrôles** : rapprochement des immatriculations du relevé avec le fichier des immobilisations et des contrats de crédit-bail / LLD (un véhicule inconnu = carte non désactivée ou véhicule personnel) ; ratio litres / 100 km par tracteur (détection d'anomalies) ; conservation des factures détaillées de péages.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 298-4-1° : coefficients d'admission des carburants (gazole et essence : 80 % pour les véhicules exclus, 100 % pour les autres).
- CGI, annexe II, art. 206-IV-2-6° : exclusion des véhicules conçus pour le transport de personnes et des services afférents.
- BOFiP, TVA – Droits à déduction – exclusions et restrictions (véhicules, carburants, péages).
- Code des douanes (dispositions relatives au remboursement partiel de TICPE pour le transport routier de marchandises) — taux et modalités à vérifier chaque année.
- PCG : suppression des comptes de transfert de charges (règlement ANC 2022-06).
