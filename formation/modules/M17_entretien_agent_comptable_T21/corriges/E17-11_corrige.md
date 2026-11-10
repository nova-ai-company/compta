# Corrigé E17-11 — Clôture au 31/12/2026 avec l'expert-comptable et le commissaire aux comptes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E17-11](../exercices/E17-11_cloture-2026-expert-comptable-cac.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

!!! abstract "En clair"
    Pour chaque information, trois questions : (1) **à quel exercice** appartient cette charge ou ce produit ? (2) existe-t-il une **dette ou un risque** à la clôture ? (3) **quel service** doit la supporter ? La troisième question est propre au secteur : une écriture juste mais dans le mauvais service fausse l'ERRD du SESSAD ou le compte administratif du SAVS.

| Info | Principe | Service (code analytique) | Écriture type |
|---|---|---|---|
| 1 | Rattachement : l'audit porte sur 2026 | Clé « charges directes » (fiche, § 3.5) | **FNP** : 6226 / 4081 (TTC) |
| 2 | Rattachement : électricité consommée en 2026 | Clé m² | **FNP** : 6061 / 4081 (TTC) |
| 3 | Rattachement : 3 mois de prime concernent 2027 | Clé m² | **CCA** : 486 / 616 |
| 4 | Rattachement : loyer de janvier 2027 | Clé m² | **CCA** : 486 / 6132 |
| 5 | Rattachement : subvention acquise en 2026 (objectif atteint) | 30-EMPLOI | **Subvention à recevoir** : 441 / 74 |
| 6 | Rattachement : congés acquis en 2026, payés en 2027 | Chaque service | 6412 / 4282 et 645 / 4382 |
| 7a | Engagement de retraite : méthode de l'association = annexe | Tous | **Pas d'écriture** ; mention en annexe |
| 7b | Départ certain au 31/12/2026 : la dette existe | 01-SIEGE | **Charge à payer** : 6414 / 4286 et 645 / 4386 |
| 8 | Amortissement + étalement de la subvention au même rythme | 10-SESSAD | 6811 / 2818 et 139 / 777 |
| 9 | Subvention affectée non utilisée | 50-PAIRS | 194 / 7894 puis 6894 / 194 |

**Pourquoi tout en TTC ?** L'association ne récupère pas la TVA (fiche, § 3.8) : la TVA est une charge. Pas de compte 44586 ici.

**Information 7 : provision, dette ou engagement ?**
- Une **dette** : on sait **qui**, **combien** et **quand**. C'est le cas de Mme Roux : elle part le 31/12/2026, le montant est calculé, il sera payé en janvier. → **écriture obligatoire** (charge à payer).
- Une **provision** : une sortie d'argent **probable**, mais dont le montant ou la date ne sont pas certains. → écriture en classe 15 / 68.
- Un **engagement mentionné en annexe** : pour les indemnités de départ à la retraite des **autres** salariés, l'entreprise ou l'association peut **soit** les provisionner (méthode dite « préférentielle »), **soit** les indiquer seulement dans l'annexe. Cap Horizons 21 a toujours choisi l'annexe. On ne change pas de méthode sans décision et sans explication. → **pas d'écriture**, mais une mention en annexe : 186 000,00 €.

*Si l'association décidait un jour de provisionner, il s'agirait d'un changement de méthode comptable, avec un traitement particulier et un impact sur les budgets des services : à étudier avec l'expert-comptable, le CAC et les autorités de tarification.*

**Information 8 : pourquoi étaler la subvention ?** Le véhicule coûte 12 500,00 € mais sa charge est répartie sur 5 ans par l'amortissement. Si on mettait les 12 500,00 € de subvention en produit dès 2026, le SESSAD afficherait un gros excédent en 2026, puis des déficits ensuite. En virant la subvention au résultat **au même rythme que l'amortissement** (compte 777), l'effet sur le résultat est **nul chaque année**.

> ⚠️ Erreur classique : croire que tous les CNR se traitent pareil. Les CNR font en principe partie des produits de la tarification ; quand ils financent un investissement, les pratiques varient (subvention d'investissement étalée, comme ici, **ou** produit de l'année puis affectation de l'excédent correspondant à l'investissement, compte 10682). **Question à poser** à Hélène Ferrand et à l'ARS : « quel traitement retenez-vous pour ces CNR d'investissement, et est-ce cohérent avec l'ERRD ? » Faites valider par le CAC. *À vérifier sur la notification et sur le cadre réglementaire en vigueur.*

## 2. Calculs (détaillés, chaque montant justifié)

| Info | Calcul | Montant |
|---|---|---|
| 1 — FNP honoraires CAC | 9 600,00 − 3 840,00 (acompte) | 5 760,00 € TTC |
| 2 — FNP électricité | estimation | 1 860,00 € TTC |
| 3 — CCA assurance | 7 200,00 × 3/12 (janvier à mars 2027) | 1 800,00 € |
| 4 — CCA loyer | loyer de janvier 2027 | 6 200,00 € |
| 5 — AGEFIPH à recevoir | 36 000,00 − 28 800,00 | 7 200,00 € |
| 7b — Indemnité Mme Roux | 7 850,00 + 3 297,00 | 11 147,00 € |
| 8 — Amortissement 2026 | 12 500,00 / 5 × 6/12 (du 01/07 au 31/12) | 1 250,00 € |
| 8 — Quote-part de subvention 2026 | même rythme que l'amortissement : 12 500,00 / 5 × 6/12 | 1 250,00 € |
| 9 — Ressources disponibles 2026 | 6 200,00 (fonds dédiés 2025) + 40 000,00 (tranche 2026) | 46 200,00 € |
| 9 — Fonds dédiés au 31/12/2026 | 46 200,00 − 31 500,00 | 14 700,00 € |

**Congés payés par service (information 6)**

| Service | Congés payés bruts | Charges 42 % | Total |
|---|---|---|---|
| 01-SIEGE | 9 800,00 € | 4 116,00 € | 13 916,00 € |
| 10-SESSAD | 58 400,00 € | 24 528,00 € | 82 928,00 € |
| 20-SAVS | 31 200,00 € | 13 104,00 € | 44 304,00 € |
| 30-EMPLOI | 12 600,00 € | 5 292,00 € | 17 892,00 € |
| 40-HABITAT | 3 800,00 € | 1 596,00 € | 5 396,00 € |
| **Total** | **115 800,00 €** | **48 636,00 €** | **164 436,00 €** |

Comme la dette 2025 (155 348,00 €) a été extournée le 01/01/2026, on enregistre la **totalité** de la dette 2026. Effet net sur le résultat 2026 : 164 436,00 − 155 348,00 = **9 088,00 €** de charge en plus.

Fonds dédiés : on considère que les dépenses 2026 consomment d'abord les fonds reportés de 2025 (6 200,00 €), puis la tranche 2026 (25 300,00 €). Il reste 40 000,00 − 25 300,00 = 14 700,00 € de la tranche 2026. ✓

## 3. Écritures comptables

**A. Factures non parvenues, charges constatées d'avance, subvention à recevoir**

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6226 | Honoraires | FNP solde honoraires CAC 2026 (TTC) | clé charges directes | 5 760,00 | |
| 31/12/2026 | OD | 4081 | Fournisseurs — factures non parvenues | FNP Audit Rhodanien 2026 | | | 5 760,00 |
| 31/12/2026 | OD | 6061 | Fournitures non stockables (eau, énergie) | FNP électricité novembre-décembre 2026 | clé m² | 1 860,00 | |
| 31/12/2026 | OD | 4081 | Fournisseurs — factures non parvenues | FNP électricité novembre-décembre 2026 | | | 1 860,00 |
| 31/12/2026 | OD | 486 | Charges constatées d'avance | CCA assurance multirisque 01/2027 à 03/2027 | | 1 800,00 | |
| 31/12/2026 | OD | 616 | Primes d'assurances | CCA assurance multirisque 01/2027 à 03/2027 | clé m² | | 1 800,00 |
| 31/12/2026 | OD | 486 | Charges constatées d'avance | CCA loyer janvier 2027 | | 6 200,00 | |
| 31/12/2026 | OD | 6132 | Locations immobilières | CCA loyer janvier 2027 | clé m² | | 6 200,00 |
| 31/12/2026 | OD | 441 | Subventions à recevoir — AGEFIPH | Solde convention AGEFIPH 2026 (objectif atteint) | | 7 200,00 | |
| 31/12/2026 | OD | 74 | Subventions d'exploitation — AGEFIPH | Solde convention AGEFIPH 2026 | 30-EMPLOI | | 7 200,00 |
| | | | | **Total** | | **22 820,00** | **22 820,00** |

*Le compte 441 est utilisé ici pour une subvention à recevoir ; selon le plan de comptes, un compte de produits à recevoir (468x) peut être utilisé pour un financeur qui n'est pas une collectivité publique. Le logiciel ventile les lignes « clé m² » et « clé charges directes » entre les services selon les clés de la fiche, § 3.5.*

**B. Congés payés (dette provisionnée par service)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6412 | Congés payés | CP acquis non pris au 31/12/2026 | 01-SIEGE | 9 800,00 | |
| 31/12/2026 | OD | 6412 | Congés payés | CP acquis non pris au 31/12/2026 | 10-SESSAD | 58 400,00 | |
| 31/12/2026 | OD | 6412 | Congés payés | CP acquis non pris au 31/12/2026 | 20-SAVS | 31 200,00 | |
| 31/12/2026 | OD | 6412 | Congés payés | CP acquis non pris au 31/12/2026 | 30-EMPLOI | 12 600,00 | |
| 31/12/2026 | OD | 6412 | Congés payés | CP acquis non pris au 31/12/2026 | 40-HABITAT | 3 800,00 | |
| 31/12/2026 | OD | 4282 | Dettes provisionnées pour congés à payer | CP acquis non pris au 31/12/2026 | | | 115 800,00 |
| 31/12/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Charges sur CP au 31/12/2026 | 01-SIEGE | 4 116,00 | |
| 31/12/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Charges sur CP au 31/12/2026 | 10-SESSAD | 24 528,00 | |
| 31/12/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Charges sur CP au 31/12/2026 | 20-SAVS | 13 104,00 | |
| 31/12/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Charges sur CP au 31/12/2026 | 30-EMPLOI | 5 292,00 | |
| 31/12/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Charges sur CP au 31/12/2026 | 40-HABITAT | 1 596,00 | |
| 31/12/2026 | OD | 4382 | Charges sociales sur congés à payer | Charges sur CP au 31/12/2026 | | | 48 636,00 |
| | | | | **Total** | | **164 436,00** | **164 436,00** |

**C. Indemnité de départ à la retraite de Mme Roux (dette certaine)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6414 | Indemnités et avantages divers | Indemnité départ retraite Mme Roux — payée 01/2027 | 01-SIEGE | 7 850,00 | |
| 31/12/2026 | OD | 4286 | Personnel — autres charges à payer | Indemnité départ retraite Mme Roux | | | 7 850,00 |
| 31/12/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Cotisations sur indemnité de départ Mme Roux | 01-SIEGE | 3 297,00 | |
| 31/12/2026 | OD | 4386 | Organismes sociaux — autres charges à payer | Cotisations sur indemnité de départ Mme Roux | | | 3 297,00 |
| | | | | **Total** | | **11 147,00** | **11 147,00** |

**D. Véhicule d'occasion du SESSAD : amortissement et quote-part de subvention**

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations | Amortissement véhicule SESSAD 01/07 au 31/12/2026 | 10-SESSAD | 1 250,00 | |
| 31/12/2026 | OD | 2818 | Amortissements des autres immobilisations corporelles | Amortissement véhicule SESSAD 2026 | | | 1 250,00 |
| 31/12/2026 | OD | 139 | Subventions d'investissement inscrites au compte de résultat | Quote-part CNR ARS véhicule 2026 | | 1 250,00 | |
| 31/12/2026 | OD | 777 | Quote-part des subventions d'investissement virée au résultat | Quote-part CNR ARS véhicule 2026 | 10-SESSAD | | 1 250,00 |
| | | | | **Total** | | **2 500,00** | **2 500,00** |

*Compte 777 : vérifiez son classement et son intitulé exacts dans la nomenclature 2025 du PCG et dans le plan de comptes des ESSMS. Dans le budget du SESSAD, il figure en groupe III des recettes (produits non encaissables). Ce véhicule explique la quote-part de 2 500,00 € par an prévue dans l'EPRD 2027 (E17-07).*

**E. Fonds dédiés du projet « Pairs et voix »**

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 194 | Fonds dédiés sur subventions de fonctionnement | Utilisation des fonds dédiés 2025 — Fondation Lumen | | 6 200,00 | |
| 31/12/2026 | OD | 7894 | Utilisation des fonds dédiés sur subventions de fonctionnement | Utilisation des fonds dédiés 2025 — Fondation Lumen | 50-PAIRS | | 6 200,00 |
| 31/12/2026 | OD | 6894 | Reports en fonds dédiés sur subventions de fonctionnement | Tranche 2026 non utilisée — Fondation Lumen | 50-PAIRS | 14 700,00 | |
| 31/12/2026 | OD | 194 | Fonds dédiés sur subventions de fonctionnement | Tranche 2026 non utilisée — Fondation Lumen | | | 14 700,00 |
| | | | | **Total** | | **20 900,00** | **20 900,00** |

Solde du compte 194 (Pairs) au 31/12/2026 : 6 200,00 − 6 200,00 + 14 700,00 = **14 700,00 €**. Résultat de la section 50-PAIRS sur cette subvention : 40 000,00 + 6 200,00 − 31 500,00 − 14 700,00 = **0,00 €** ✓.

**Information 7a — Aucune écriture.** Mention en annexe : « Engagement en matière d'indemnités de départ à la retraite au 31/12/2026 : 186 000,00 € (171 500,00 € au 31/12/2025), non provisionné, évalué par un actuaire (méthode et hypothèses principales). »

### Question 5 — Impact sur le résultat 2026

| Écriture | Effet | Montant |
|---|---|---|
| FNP honoraires CAC | charge | − 5 760,00 € |
| FNP électricité | charge | − 1 860,00 € |
| CCA assurance | charge en moins | + 1 800,00 € |
| CCA loyer | charge en moins | + 6 200,00 € |
| AGEFIPH à recevoir | produit | + 7 200,00 € |
| Congés payés 2026 | charge | − 164 436,00 € |
| Indemnité Mme Roux | charge | − 11 147,00 € |
| Amortissement véhicule | charge | − 1 250,00 € |
| Quote-part de subvention | produit | + 1 250,00 € |
| Utilisation fonds dédiés 2025 | produit | + 6 200,00 € |
| Report en fonds dédiés 2026 | charge | − 14 700,00 € |
| **Total des écritures d'inventaire** | | **− 176 503,00 €** |
| Pour mémoire : extourne des congés payés 2025 déjà passée le 01/01/2026 | produit déjà en compte | + 155 348,00 € |
| **Impact net par rapport à l'année précédente** | | **− 21 155,00 €** |

### Question 6 — Extournes au 01/01/2027

| Écriture | Extourne ? | Pourquoi |
|---|---|---|
| FNP honoraires CAC, FNP électricité | **Oui** | La vraie facture sera saisie en 2027 |
| CCA assurance, CCA loyer | **Oui** | La charge revient en 2027 |
| AGEFIPH à recevoir | **Non** en général | On lettrera le 441 lors de l'encaissement (débit 512 / crédit 441). *Selon l'habitude du dossier : à voir avec Hélène Ferrand.* |
| Congés payés | **Oui** | Méthode de l'association (extourne puis nouvelle dette à la clôture) |
| Indemnité Mme Roux | **Non** | Elle sera soldée par la paie de janvier (débit 4286 et 4386) |
| Amortissement, quote-part 777 | **Non** | Écritures définitives |
| Fonds dédiés | **Non** | Le 194 sera repris en 2027 au fur et à mesure des dépenses |

## 4. Points d'attention / pièges

- **FNP en HT** : erreur classique d'une comptable venue d'une entreprise. Ici, tout est **TTC** (TVA non récupérable).
- **Congés payés oubliés dans un service** : chaque service a son ERRD ou son compte rendu ; la ventilation analytique est **obligatoire**.
- **La « provision » pour congés payés** n'est pas une provision au sens comptable (classe 15) : c'est une **dette** (4282 / 4382), car le montant et le bénéficiaire sont connus.
- **Mme Roux** : ne pas la noyer dans l'engagement global de retraite. Son départ est **certain** au 31/12/2026 : c'est une charge à payer de 2026. Pensez aussi à vérifier que l'actuaire l'a bien **sortie** de son calcul (sinon, double compte en annexe).
- **Subvention AGEFIPH** : la méthode de Mme Roux (produit à l'encaissement) est fausse. Une subvention acquise (convention signée, conditions remplies) est un produit de l'exercice, même si elle est encaissée plus tard.
- **CNR d'investissement** : traitement à valider (voir l'analyse). Ne pas comptabiliser 12 500,00 € de produit en 2026 sans validation.
- **Fonds dédiés** : reprendre d'abord les fonds dédiés anciens avant d'en constituer de nouveaux, et respecter les dates limites des conventions.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

### Question 7 — Sommaire du dossier de travail pour Hélène Ferrand

1. **Balance générale et balance analytique** au 31/12/2026, avec le contrôle « somme des sections = résultat global ».
2. **Banque** : états de rapprochement de chaque compte (courant, livret) au 31/12/2026, avec les relevés.
3. **Tiers** : balances âgées fournisseurs et clients (financeurs), comptes lettrés, explication des soldes anciens ; comptes d'attente (471) soldés.
4. **Écritures d'inventaire** (A à E ci-dessus), une feuille par écriture avec la pièce justificative.
5. **Immobilisations** : tableau des immobilisations et des amortissements, factures des acquisitions 2026 (véhicule), sorties d'actifs.
6. **Subventions** : tableau de suivi par financeur (notifié, encaissé, à recevoir, à reverser), tableau des subventions d'investissement (131 / 139), tableau des **fonds dédiés** (194) par projet.
7. **Paie** : rapprochement paie / comptabilité (641, 645, 421, 431…), état des congés payés par service, attestation de l'actuaire (IDR), calcul de l'indemnité de Mme Roux.
8. **Fonds propres** : affectation du résultat 2025 (E17-08), tableau des réserves par service.
9. **Contrôles budgétaires** : réalisé 2026 par service comparé à l'EPRD et au budget du SAVS, avec les principaux écarts expliqués (base de l'ERRD et du compte administratif).
10. **Liste des points en suspens** (questions pour Hélène Ferrand : traitement des CNR, extourne du 441…).

### Question 8 — Justificatifs pour M. Garnier (commissaire aux comptes)

| Domaine | Justificatifs |
|---|---|
| Trésorerie | États de rapprochement bancaire au 31/12/2026 ; relevés de décembre 2026 et janvier 2027 ; liste des personnes habilitées et délégations de signature (double signature) |
| Tiers | États de rapprochement des comptes de tiers (fournisseurs, financeurs, organismes sociaux) ; balances âgées ; réponses aux **demandes de confirmation** qu'il enverra (banques, avocats, financeurs) |
| Immobilisations | Inventaire physique des immobilisations (véhicules : cartes grises), factures d'acquisition 2026 |
| Financements | **Conventions de subvention** (AGEFIPH, Fondation Lumen, Département, Ville…), **notifications et arrêtés** de l'ARS et du Département (dotations, CNR), CPOM, décisions d'affectation des résultats |
| Gouvernance | **PV du conseil d'administration et de l'AG** (approbation des comptes 2025, affectation, budget), statuts à jour, délégations de pouvoir |
| Personnel | État des congés payés par service ; attestation actuarielle IDR ; dossier de départ de Mme Roux ; rapprochement DSN / comptabilité |
| Contrats | Bail des locaux de Valence, contrats d'assurance, contrats de LLD, lettre de mission de l'expert-comptable |
| Clôture | Dossier de travail ci-dessus ; liste des événements postérieurs à la clôture ; **lettre d'affirmation** signée par la direction en fin de mission |

**Mail à Hélène Ferrand :**
> « Bonjour Madame Ferrand, je vous transmets le dossier de travail de la clôture 2026 de Cap Horizons 21 (sommaire joint). Trois points à valider ensemble le 2 février : (1) le traitement des CNR ARS du véhicule du SESSAD, que j'ai enregistrés en subvention d'investissement étalée au rythme de l'amortissement ; (2) le solde AGEFIPH de 7 200,00 € comptabilisé en subvention à recevoir, alors qu'il était jusqu'ici enregistré à l'encaissement ; (3) l'indemnité de départ de Mme Roux, comptabilisée en charge à payer de 2026, à exclure du calcul actuariel. Bien cordialement. »

**Calendrier à rappeler à la direction** *(à vérifier chaque année)* : arrêté des comptes par le conseil d'administration, rapport du CAC, approbation par l'AG dans les 6 mois, dépôt de l'ERRD et du compte administratif au 30/04/2027, publication des comptes si l'association dépasse le seuil légal de subventions publiques (*seuil à vérifier*).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Règlement ANC n° 2018-06 : subventions d'investissement, fonds dédiés (19x, 689, 789), engagements de retraite et méthode préférentielle, annexe.
- PCG (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06) : charges à payer, charges constatées d'avance, dettes provisionnées pour congés payés, amortissements, quote-part des subventions d'investissement virée au résultat.
- Code de commerce et Code de l'action sociale et des familles : mission du commissaire aux comptes dans les associations subventionnées, obligations de publication — *articles et seuils à vérifier*.
- Code de l'action sociale et des familles : ERRD et compte administratif des ESSMS — *à vérifier sur le cadre réglementaire en vigueur*.
- Fiche de l'association Cap Horizons 21, § 3.1, § 3.5 et § 3.8.
