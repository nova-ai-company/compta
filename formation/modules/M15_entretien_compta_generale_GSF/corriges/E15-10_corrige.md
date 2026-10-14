# Corrigé E15-10 — Test technique : trouver les huit erreurs d'une balance de fin de mois

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-10](../exercices/E15-10_balance-trouver-les-erreurs.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Étape 1 — Regarder les totaux (question 1)
Total des soldes débiteurs : 7 395 200,00 € ; total des soldes créditeurs : 7 420 160,00 €. **Écart : 24 960,00 €.**

Un logiciel comptable n'accepte que des écritures équilibrées (débit = crédit) : sa balance est **toujours** équilibrée. Un déséquilibre signifie donc que la balance a été **retouchée ou ressaisie** (ici, recopiée dans un tableur).

Méthode rapide pour trouver l'erreur :
- **Diviser l'écart par 2** : 24 960,00 / 2 = **12 480,00 €**. Si un solde a été mis **du mauvais côté**, l'écart vaut deux fois ce solde. On cherche donc un compte de 12 480,00 € → le **512 Banque**.
- (Si l'écart est divisible par 9, on pense à une **inversion de chiffres**, par exemple 1 470 recopié 1 740 : écart 270 = 9 × 30.)

### Étape 2 — Le sens normal des soldes
Pour repérer les autres anomalies, on parcourt la balance en se demandant pour chaque compte : « Ce solde est-il du **côté normal** ? »
- Comptes de **charges** (6) : débiteurs. Comptes de **produits** (7) : créditeurs.
- **Actif** (immobilisations, stocks, clients, TVA déductible, banque positive) : débiteur. **Passif** (capital, emprunts, fournisseurs, dettes sociales et fiscales) : créditeur. Amortissements : créditeurs.
- **Comptes d'attente** (471) : **nuls** en fin de mois.
- Et on descend dans les **auxiliaires** : un compte collectif (401, 411) peut avoir un solde « normal » tout en cachant un fournisseur débiteur ou un client créditeur.

### Étape 3 — Les huit anomalies (question 2)

| N° | Où la voir | Anomalie | Explication simple | Correction |
|---|---|---|---|---|
| 1 | Balance + relevé | **512 créditeur** alors que la banque est positive | Le relevé de la banque est présenté **du point de vue de la banque** : « créditeur » chez la banque = l'argent nous appartient = **débiteur** chez nous. L'intérimaire a recopié le sens du relevé. | Aucune écriture : le logiciel est juste ; on corrige la **présentation** (12 480,00 € au débit). La balance s'équilibre. |
| 2 | Balance (6064) + grand livre | **Compte de charge créditeur** (6064 : 620,00 € C) | La facture FBR-26-0977 a été saisie **à l'envers**, comme un avoir : la charge a été diminuée au lieu d'être augmentée. | Annuler l'écriture fausse (écriture inverse) puis passer la bonne : soit au total 2 × 1 240,00 € en 6064 et 2 × 248,00 € en 44566 au débit, 2 × 1 488,00 € en 401 au crédit. |
| 3 | Balance (471) | **Compte d'attente non soldé** (3 150,00 € D) | Le prélèvement de Prévoyance Azur n'a pas été identifié. C'est le paiement des cotisations de septembre, déjà enregistrées en dette au 437. | 437 au débit / 471 au crédit 3 150,00 €. |
| 4 | Grand livre 44566 | **TVA déduite sur un véhicule de tourisme** (1 280,00 €) | La TVA sur l'achat ou la location d'une **voiture de tourisme** n'est **pas récupérable**. Elle fait partie du coût de la location. | 6135 au débit / 44566 au crédit 1 280,00 € ; régulariser la TVA déduite à tort sur la CA3 d'octobre. |
| 5 | Grand livre 6022 | **Facture saisie deux fois** (HP-26-1188) | Même numéro, même montant, reçue deux fois (flux de la plateforme puis PDF par e-mail). La charge, la TVA et la dette sont doublées. | Annuler la seconde saisie : 401 au débit 4 860,00 / 6022 au crédit 4 050,00 / 44566 au crédit 810,00. |
| 6 | Grand livre 6063 | **Immobilisation passée en charge** (injecteur-extracteur 3 900,00 € HT) | Machine durable, avec n° de série, bien au-dessus de 500 € HT : c'est une immobilisation, pas une fourniture. | Reclasser en 2154 (et la TVA en 44562), créer la fiche d'immobilisation, passer la dotation d'octobre (41,17 €). |
| 7 | Auxiliaire 401 | **Fournisseur débiteur** (Distri-Sacs 2 340,00 € D) | Le virement de 2 340,00 € payait la facture DH-3307 de **Distri-Hygiène** (libellé du virement) mais a été imputé sur Distri-Sacs. Résultat : Distri-Sacs semble nous devoir de l'argent et Distri-Hygiène semble impayé (risque de relance, voire de double paiement). | 401DHY au débit / 401DSP au crédit 2 340,00 €, puis lettrage des deux comptes. |
| 8 | Auxiliaire 411 | **Client créditeur** (Copropriété Le Méridien 1 800,00 € C) | Ce n'est pas un règlement de facture : c'est un **acompte** reçu avant la prestation. Il doit aller en 4191. Et comme la TVA sur les **prestations de services** est due **à l'encaissement**, l'acompte encaissé rend la TVA exigible dès octobre. | 411 au débit 1 800,00 / 4191 au crédit 1 500,00 / 44571 au crédit 300,00. |

## 2. Calculs (détaillés, chaque montant justifié)

| Anomalie | Calcul | Montant |
|---|---|---|
| 1 — Écart de la balance | 7 420 160,00 − 7 395 200,00 | 24 960,00 € |
| 1 — Compte en cause | 24 960,00 / 2 | 12 480,00 € (512) |
| 2 — Facture inversée | HT 1 240,00 ; TVA 1 240,00 × 20 % = 248,00 ; TTC 1 488,00 | ×2 (annulation + bonne saisie) |
| 2 — Contrôle du 6064 corrigé | 470,00 + 150,00 + 1 240,00 | 1 860,00 € D |
| 4 — TVA VP | 10 mois × 128,00 (= 640,00 × 20 %) | 1 280,00 € |
| 5 — Doublon | HT 4 050,00 ; TVA 4 050,00 × 20 % = 810,00 ; TTC 4 860,00 | 4 860,00 € |
| 6 — TVA à reclasser | 3 900,00 × 20 % | 780,00 € |
| 6 — Annuité | 3 900,00 / 5 | 780,00 € |
| 6 — Dotation d'octobre | 780,00 × 19 / 360 (du 12/10 au 30/10, mois de 30 jours) | 41,17 € |
| 8 — Acompte HT | 1 800,00 / 1,20 | 1 500,00 € |
| 8 — TVA exigible | 1 800,00 − 1 500,00 | 300,00 € |
| 8 — Contrôle | 3 750,00 HT × 40 % = 1 500,00 HT → 1 800,00 TTC | ✓ |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6064 | Fournitures administratives | Annulation saisie inversée FBR-26-0977 | 1 240,00 | |
| 31/10/2026 | OD | 44566 | TVA déductible sur autres biens et services | Annulation saisie inversée FBR-26-0977 | 248,00 | |
| 31/10/2026 | OD | 401 | Fournisseurs (Bureau Riviera) | Annulation saisie inversée FBR-26-0977 | | 1 488,00 |
| 31/10/2026 | AC | 6064 | Fournitures administratives | Bureau Riviera FBR-26-0977 (bonne saisie) | 1 240,00 | |
| 31/10/2026 | AC | 44566 | TVA déductible sur autres biens et services | Bureau Riviera FBR-26-0977 TVA | 248,00 | |
| 31/10/2026 | AC | 401 | Fournisseurs (Bureau Riviera) | Bureau Riviera FBR-26-0977 | | 1 488,00 |
| 31/10/2026 | OD | 437 | Autres organismes sociaux (Prévoyance Azur) | Imputation prélèvement prévoyance 09/2026 | 3 150,00 | |
| 31/10/2026 | OD | 471 | Compte d'attente | Imputation prélèvement prévoyance 09/2026 | | 3 150,00 |
| 31/10/2026 | OD | 6135 | Locations mobilières | TVA non déductible LLD véhicule de tourisme 01-10/2026 | 1 280,00 | |
| 31/10/2026 | OD | 44566 | TVA déductible sur autres biens et services | TVA non déductible LLD véhicule de tourisme | | 1 280,00 |
| 31/10/2026 | OD | 401 | Fournisseurs (Hygiène Pro) | Annulation doublon HP-26-1188 du 22/10 | 4 860,00 | |
| 31/10/2026 | OD | 6022 | Fournitures consommables | Annulation doublon HP-26-1188 | | 4 050,00 |
| 31/10/2026 | OD | 44566 | TVA déductible sur autres biens et services | Annulation doublon HP-26-1188 TVA | | 810,00 |
| 31/10/2026 | OD | 2154 | Matériel industriel | Reclassement injecteur-extracteur IE-30 n° IE30-26-1145 | 3 900,00 | |
| 31/10/2026 | OD | 6063 | Fournitures d'entretien et de petit équipement | Reclassement injecteur-extracteur IE-30 | | 3 900,00 |
| 31/10/2026 | OD | 44562 | TVA déductible sur immobilisations | Reclassement TVA injecteur-extracteur | 780,00 | |
| 31/10/2026 | OD | 44566 | TVA déductible sur autres biens et services | Reclassement TVA injecteur-extracteur | | 780,00 |
| 31/10/2026 | OD | 6811 | Dotations aux amortissements | Dotation 10/2026 injecteur-extracteur (19 j) | 41,17 | |
| 31/10/2026 | OD | 28154 | Amortissements du matériel industriel | Dotation 10/2026 injecteur-extracteur | | 41,17 |
| 31/10/2026 | OD | 401DHY | Fournisseur Distri-Hygiène | Réimputation virement du 20/10 (DH-3307) | 2 340,00 | |
| 31/10/2026 | OD | 401DSP | Fournisseur Distri-Sacs Provence | Réimputation virement du 20/10 (DH-3307) | | 2 340,00 |
| 31/10/2026 | OD | 411MER | Client Copropriété Le Méridien | Reclassement acompte devis D-26-318 | 1 800,00 | |
| 31/10/2026 | OD | 4191 | Clients – avances et acomptes reçus | Acompte devis D-26-318 (HT) | | 1 500,00 |
| 31/10/2026 | OD | 44571 | TVA collectée | TVA exigible sur acompte D-26-318 | | 300,00 |
| | | | | **Totaux** | **21 127,17** | **21 127,17** |

> Pour l'anomalie 2, on peut aussi passer une seule écriture de 2 480,00 € / 496,00 € / 2 976,00 € ; deux écritures (annulation puis bonne saisie) laissent une piste d'audit plus claire.

**Pourquoi ce sens ?** (exemples à savoir expliquer)
- Anomalie 3 : payer une dette la **diminue** → 437 au **débit** ; le 471 avait été débité par la banque, on le **crédite** pour le remettre à zéro.
- Anomalie 5 : annuler une facture, c'est passer **l'écriture inverse** : la dette 401 au débit, la charge et la TVA au crédit.
- Anomalie 8 : on retire l'acompte du compte client (411 au **débit**) pour le mettre en 4191 au **crédit** (dette envers le client tant que la prestation n'est pas faite) ; la TVA collectée est une dette envers l'État → **crédit**.

**Balance corrigée au 31/10/2026 (question 3)**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 101 | Capital | | 500 000,00 |
| 106 | Réserves | | 69 750,00 |
| 164 | Emprunts auprès des établissements de crédit | | 284 600,00 |
| 2154 | Matériel industriel | 850 200,00 | |
| 2182 | Matériel de transport | 392 800,00 | |
| 28154 | Amortissements du matériel industriel | | 412 691,17 |
| 28182 | Amortissements du matériel de transport | | 188 420,00 |
| 322 | Stocks de fournitures consommables | 21 340,00 | |
| 401 | Fournisseurs | | 316 876,00 |
| 411 | Clients | 1 488 020,00 | |
| 4191 | Clients – avances et acomptes reçus | | 1 500,00 |
| 421 | Personnel – rémunérations dues | | 412 380,00 |
| 431 | Sécurité sociale | | 186 540,00 |
| 437 | Autres organismes sociaux | | 58 080,00 |
| 4421 | Prélèvements à la source | | 14 870,00 |
| 44562 | TVA déductible sur immobilisations | 2 920,00 | |
| 44566 | TVA déductible sur autres biens et services | 36 086,00 | |
| 44571 | TVA collectée | | 98 160,00 |
| 471 | Compte d'attente | 0,00 | |
| 512 | Banque | 12 480,00 | |
| 6022 | Fournitures consommables (produits d'entretien) | 210 550,00 | |
| 6063 | Fournitures d'entretien et de petit équipement | 35 050,00 | |
| 6064 | Fournitures administratives | 1 860,00 | |
| 611 | Sous-traitance générale | 286 400,00 | |
| 6135 | Locations mobilières | 75 580,00 | |
| 616 | Primes d'assurances | 41 200,00 | |
| 6411 | Salaires, appointements | 2 780 500,00 | |
| 6451 | Cotisations à l'URSSAF | 1 012 300,00 | |
| 6611 | Intérêts des emprunts et dettes | 8 940,00 | |
| 6811 | Dotations aux amortissements | 147 641,17 | |
| 706 | Prestations de services | | 4 860 000,00 |
| | **Totaux** | **7 403 867,17** | **7 403 867,17** |

Contrôles : 471 soldé ; 6064 débiteur ; 512 débiteur (= relevé) ; 401 : Distri-Sacs et Distri-Hygiène soldés ; 411 : Copropriété Le Méridien soldée, acompte en 4191.

## 4. Points d'attention / pièges

- **Relevé bancaire « créditeur »** : le sens est inversé entre la banque et l'entreprise. C'est la question piège n° 1 des entretiens.
- **Ne pas « forcer » l'équilibre** d'une balance avec un compte d'attente : on cherche la cause.
- **Doublon de facture** : avec la facture électronique (réception obligatoire depuis le 01/09/2026), le même document peut arriver par la plateforme **et** par e-mail. Le contrôle des doublons (n° de facture + fournisseur + montant) devient indispensable.
- **TVA sur véhicule de tourisme** : non déductible (achat, location, entretien) ; seul le carburant suit des règles particulières. Pour un véhicule **utilitaire**, la TVA est déductible.
- **Immobilisation en charge** : le résultat est faux (charge trop forte de 3 900,00 €, dotation manquante) et le matériel n'est pas suivi dans le fichier des immobilisations.
- **Fournisseur débiteur** : ne jamais le laisser « en l'état » ; il cache soit une erreur d'imputation (ici), soit un double paiement ou un avoir à réclamer. Et **lettrer** les comptes pour le voir tout de suite.
- **Client créditeur = souvent un acompte** : pour une prestation de services, la TVA est due à l'encaissement de l'acompte ; l'oublier, c'est sous-déclarer la TVA d'octobre.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse orale à la question 4 (une minute) :**
> « Un : je vérifie que la balance est équilibrée et que le résultat est cohérent avec le mois précédent. Deux : je regarde le sens des soldes, une charge créditrice, une banque créditrice, un compte d'amortissement débiteur. Trois : les comptes d'attente, 471 et 580, doivent être à zéro. Quatre : je rapproche la banque, les comptes sociaux avec la DSN et la TVA avec la déclaration. Cinq : je descends dans les auxiliaires, fournisseurs débiteurs et clients créditeurs, et je lettre. »

**Mail à l'intérimaire (bienveillant) :**
> « Merci pour la balance. Pour la prochaine, pouvez-vous l'exporter directement depuis le logiciel plutôt que la recopier ? La banque avait été reportée au crédit, comme sur le relevé : chez nous, un solde positif en banque est au débit du 512. »

**Message à l'établissement d'Antibes** : demander le PV de mise en service et le n° de série pour chaque machine, et rappeler la règle des 500 € HT.

**Dossier** : conserver la balance transmise, la balance corrigée et la liste des 8 corrections avec leurs justificatifs ; vérifier que la CA3 d'octobre intègre les corrections de TVA (−1 280,00 € VP, −810,00 € doublon, reclassement 780,00 € vers la ligne « immobilisations », +300,00 € TVA collectée sur acompte, +496,00 € net sur la facture inversée).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : fonctionnement des comptes (sens des soldes), comptes 401, 411, 4191, 437, 44562, 44566, 44571, 471, 2154, 6135.
- CGI : exclusion du droit à déduction de la TVA sur les véhicules conçus pour transporter des personnes (*référence précise à vérifier dans le CGI / l'annexe II*) ; exigibilité de la TVA à l'encaissement pour les prestations de services, y compris sur les acomptes.
- BOFiP : tolérance de passage en charges des biens de faible valeur (*référence et seuil à vérifier*).
- Code de commerce : obligation de tenue d'une comptabilité régulière et de conservation des pièces.
