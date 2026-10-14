# Corrigé E03-10 — Balance âgée et dépréciation des créances : fin de la méthode statistique

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-10](../exercices/E03-10_balance-agee-depreciation.md)

## 1. Analyse

**a) Pourquoi abandonner la grille ?**
- **Comptablement** : une dépréciation traduit une perte probable sur une créance identifiée (règles d'évaluation des actifs du PCG). L'ancienneté est un **indice**, pas une preuve : un client qui paie selon un échéancier ou une créance déjà payée mais mal lettrée n'a pas à être dépréciée, tandis qu'un client en liquidation non couvert l'est à 100 % même s'il n'a que 60 jours de retard.
- La grille s'applique **sur le TTC** : erreur supplémentaire, car la TVA est récupérable en cas de perte (ici, option débits : TVA déjà reversée → récupérable).
- **Fiscalement** (art. 39-1-5° CGI) : la dépréciation n'est déductible que si la perte est **nettement précisée** et **probable**, à raison d'**événements en cours** à la clôture, **créance par créance**. Une dépréciation **forfaitaire** est **non déductible** (réintégration sur le tableau 2058-A). La jurisprudence n'admet une approche statistique qu'exceptionnellement, pour des créances nombreuses de faible montant et sur la base d'une expérience passée précise — ce n'est pas le cas d'un transporteur qui a une quarantaine de clients professionnels.

**b) Analyse client par client**

| Client | Constat | Conclusion |
|---|---|---|
| Rhône Agri, Autres | Créances récentes (< 60 j), pas d'incident | Saines |
| **Béton Express** | Redressement judiciaire ; plan envisagé à 30 % | Douteux → 416. Dépréciation de la part probablement perdue : **70 % du HT**. Pas de TVA récupérable en redressement (créance non définitivement irrécouvrable) |
| **Meubles Durand** | 6 600 € payés le 06/10 (après la situation, avant son établissement : confirme le caractère sain) ; facture de 3 000 € contestée, dommage reconnu | Facture contestée → 416, dépréciation **100 % du HT** (2 500 €). La TVA ne sera récupérée que si une réduction de prix (avoir) ou une irrécouvrabilité est constatée |
| **Garden Center** | Paiement reçu le 14/03/2025, laissé en 471 | **Erreur de lettrage** : aucune dépréciation ; solder le 471 contre le 411 |
| **Logistique Vallée** | Échéancier signé et respecté | **Aucune dépréciation** (perte non probable) ; surveiller |
| **Agro Sud Export** | Liquidation judiciaire ; assurance-crédit 85 % du HT, sinistre accepté | 416 ; **TVA récupérable** (liquidation, option débits → TVA reversée) ; dépréciation de la **part non couverte** : 15 % du HT |
| **Transalp Négoce** | Société radiée, PV de carence | Créance **irrécouvrable hors procédure** (preuve : PV de carence) → **perte 654** + **TVA récupérée** (facture rectificative au dernier domicile connu) |

**c) Garden Center : pourquoi c'est le point le plus important.** Une créance « de plus d'un an » chez un client qui paie toujours doit faire penser à un **paiement non lettré**. Le 471 doit être **vide** à chaque situation : un virement de 6 000 € qui y dort depuis 18 mois révèle un défaut de contrôle (et, avec la grille, aurait été déprécié à 100 % alors qu'il était payé).

**d) Assurance-crédit.** La perte probable est la part **non indemnisée** : 15 % du HT. L'accord écrit de l'assureur (12/08/2026) rend l'indemnisation suffisamment certaine pour limiter la dépréciation à la part non couverte. (Variante plus prudente : déprécier 100 % du HT et constater l'indemnité en produit à son encaissement — à éviter ici puisque l'accord est obtenu, la dépréciation à 100 % surestimerait la perte.) À l'encaissement de l'indemnité (15 300 €), on soldera le 416 et la perte de 2 700 € sera constatée en 654 avec reprise de la dépréciation.

## 2. Calculs

**Grille de l'ancien collaborateur (sur TTC)**

| Tranche | Base TTC | Taux | Dépréciation |
|---|---|---|---|
| 91-180 j | 14 400,00 | 25 % | 3 600,00 |
| > 180 j | 39 840,00 | 50 % | 19 920,00 |
| > 1 an | 9 600,00 | 100 % | 9 600,00 |
| **Total** | | | **33 120,00** |

**Analyse individuelle**

| Client | Créance TTC | HT | TVA récupérable à ce stade | Taux retenu | Dépréciation | Perte |
|---|---|---|---|---|---|---|
| Béton Express | 18 240,00 | 15 200,00 | 0 (redressement) | 70 % | **10 640,00** | — |
| Durand (facture contestée) | 3 000,00 | 2 500,00 | 0 (litige) | 100 % | **2 500,00** | — |
| Garden Center | 6 000,00 | — | — | 0 % (payé) | 0,00 | — |
| Logistique Vallée | 14 400,00 | 12 000,00 | — | 0 % | 0,00 | — |
| Agro Sud Export | 21 600,00 | 18 000,00 | **3 600,00** (liquidation) | 15 % non couvert | **2 700,00** | — |
| Transalp Négoce | 3 600,00 | 3 000,00 | **600,00** | — | — | **3 000,00** |
| **Total** | | | **4 200,00** | | **15 840,00** | **3 000,00** |

**Comparaison** : grille 33 120 € vs analyse 15 840 € de dépréciation + 3 000 € de perte = 18 840 € d'impact résultat. La grille **surévaluait** le risque de 14 280 € (33 120 – 18 840), tout en ignorant la TVA récupérable.

**Mouvement net du 491** : solde 21 400 € (grille 2025, devenu sans objet) → reprise totale ; nouvelle dépréciation 15 840 €. Solde au 30/09/2026 : **15 840 €**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 471 | Compte d'attente | Lettrage virement Garden Center du 14/03/2025 | 6 000,00 | |
| 30/09/2026 | OD | 411GAR | Client Garden Center Lyon Est | Lettrage fact. 25-0214 | | 6 000,00 |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Béton Express (RJ) | 18 240,00 | |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Durand – facture contestée | 3 000,00 | |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Agro Sud Export (LJ) | 21 600,00 | |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Transalp Négoce (PV de carence) | 3 600,00 | |
| 30/09/2026 | OD | 411 | Clients (comptes individuels) | Reclassement en douteux | | 46 440,00 |
| 30/09/2026 | OD | 44571 | TVA collectée (régularisation – ligne 21 CA3) | Avoir de TVA Agro Sud Export – LJ du 08/07/2026 | 3 600,00 | |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Avoir de TVA Agro Sud Export | | 3 600,00 |
| 30/09/2026 | OD | 654 | Pertes sur créances irrécouvrables (*subdivision selon la nomenclature 2025*) | Transalp Négoce – PV de carence 18/03/2026 | 3 000,00 | |
| 30/09/2026 | OD | 44571 | TVA collectée (régularisation – ligne 21 CA3) | Transalp – TVA sur créance irrécouvrable | 600,00 | |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Transalp – solde | | 3 600,00 |
| 30/09/2026 | OD | 491 | Dépréciation des comptes clients | Reprise dépréciation forfaitaire 2025 | 21 400,00 | |
| 30/09/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise dépréciation forfaitaire 2025 | | 21 400,00 |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Béton 10 640 + Durand 2 500 + Agro 2 700 | 15 840,00 | |
| 30/09/2026 | OD | 491 | Dépréciation des comptes clients | Dépréciations individuelles au 30/09/2026 | | 15 840,00 |
| | | | | **Totaux** | **96 880,00** | **96 880,00** |

Solde du 416 après écritures : 46 440 – 3 600 – 3 600 = **39 240 €** (Béton 18 240 + Durand 3 000 + Agro 18 000 HT). Dépréciation : 15 840 €. Valeur nette : **23 400 €**, qui se décompose ainsi :
- Agro Sud Export : 18 000 – 2 700 = 15 300 € (indemnité attendue de l'assureur) ;
- Béton Express : 18 240 – 10 640 = 7 600 € (dividende estimé de 30 % du HT, soit 4 560 €, + TVA de 3 040 € qui sera récupérable sur la part abandonnée ou incluse dans les versements du plan) ;
- Durand : 3 000 – 2 500 = 500 € (TVA de la facture contestée, non dépréciée car récupérable en cas d'avoir ou de perte).

## 4. Points d'attention / pièges

- **Récupération de TVA** : possible ici parce que Transports Leroy a **opté pour les débits** (la TVA a été reversée à la facturation). Sans option, pour des prestations de transport, la TVA d'une facture impayée n'aurait jamais été exigible : rien à récupérer (voir E03-07). Chaque récupération exige une **facture rectificative** adressée au client (au liquidateur pour Agro Sud Export).
- **Béton Express** : pas de TVA récupérable tant que le plan n'est pas arrêté ; si le plan prévoit un abandon partiel, la TVA afférente à la part abandonnée deviendra récupérable.
- **Fiscalité de la reprise** : la reprise de 21 400 € est un produit imposable en 2026. Mais la dotation forfaitaire de 2025 n'aurait jamais dû être déduite : le résultat fiscal 2025 est **minoré de 21 400 €** (moins la part qui aurait été justifiée par une analyse individuelle). En cas de contrôle, l'administration peut réintégrer la dotation sur 2025 (exercice non prescrit) ; la reprise 2026 serait alors non imposable (correction symétrique des bilans). **Recommandation** : documenter la position, et envisager avec Hélène une **régularisation spontanée** (déclaration rectificative 2025 avec réduction de l'intérêt de retard) plutôt que de laisser la reprise « corriger » l'erreur un an plus tard.
- **Ne pas déprécier Logistique Vallée** au seul motif de l'ancienneté de la tranche 91-180 j : l'échéancier respecté est un élément probant. À surveiller à chaque mois.
- **Le 471 doit être soldé** à chaque situation.

## 5. Ce qu'un senior ferait en plus

**Note au dossier de travail (synthèse)** :
> Poste clients au 30/09/2026 : 260 040 € TTC. Abandon de la méthode forfaitaire (non conforme à l'art. 39-1-5° CGI et appliquée sur le TTC) au profit d'une analyse individuelle conduite avec M. Leroy le 09/10/2026. Créances à risque : Béton Express (RJ, plan envisagé à 30 %) dépréciée à 70 % du HT ; facture Durand contestée (dommage reconnu) dépréciée à 100 % du HT ; Agro Sud Export (LJ) : TVA récupérée, dépréciation limitée à la part non couverte par l'assurance-crédit (15 % du HT, accord assureur du 12/08/2026) ; Transalp Négoce passée en perte (PV de carence du 18/03/2026), TVA récupérée. Garden Center : créance soldée par lettrage d'un virement de 2025 resté en 471. Dépréciation totale : 15 840 € ; reprise de la dépréciation forfaitaire 2025 : 21 400 €. Point fiscal 2025 à trancher avec H. Ferrand.

**Pièces justificatives à obtenir / classer** : courriel du mandataire de Béton Express (projet de plan) ; déclaration de créance et accusé de réception ; constat de dommage et courriel de reconnaissance (Durand) ; échéancier signé et preuves des versements (Vallée) ; jugement de liquidation, déclaration de sinistre et accord de l'assureur (Agro) ; PV de carence et extrait Kbis de radiation (Transalp) ; factures rectificatives de TVA.

**Conseil à Bruno Leroy** : mettre en place une revue mensuelle de la balance âgée avec le service recouvrement, une veille BODACC sur les 20 premiers clients, et un rapprochement mensuel du compte d'attente 471.

## 6. Références

- CGI : art. 39-1-5° (dépréciations), art. 272-1 (TVA sur créances irrécouvrables), art. 269-2-c et option pour les débits.
- BOFiP : BIC-PROV (conditions de déductibilité des dépréciations de créances) ; TVA-DED (régularisations en cas d'impayé).
- Code de commerce : art. L. 622-24 (déclaration de créance), art. L. 626-1 et suivants (plan de sauvegarde / redressement).
- PCG : comptes 416, 471, 491, 654, 6817, 7817.
- CGI : art. 38-4 bis (intangibilité du bilan d'ouverture et correction symétrique des bilans) ; art. 1727 (intérêt de retard et réduction en cas de régularisation spontanée).
