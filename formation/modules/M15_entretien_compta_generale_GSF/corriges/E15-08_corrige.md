# Corrigé E15-08 — Test technique : sept travaux de clôture au 31/12/2026 et leurs extournes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-08](../exercices/E15-08_travaux-de-cloture-31-12-2026.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Pour chaque information, posez-vous **deux questions** :
1. **À quel exercice appartient cette charge ou ce produit ?** Si c'est 2026 et que rien n'est comptabilisé → on l'ajoute (FNP, FAE, intérêts courus). Si c'est comptabilisé en 2026 mais que cela concerne 2027 → on le retire (charge constatée d'avance).
2. **Existe-t-il un risque de perte probable à la date de clôture ?** Si oui → **prudence** : provision ou dépréciation.

| Info | Situation | Principe | Écriture type |
|---|---|---|---|
| 1 | Service reçu en 2026, facture en 2027 | Rattachement : la charge est de 2026 | **FNP** : 611 + 44586 / 4081 |
| 2 | Service rendu en 2026, facture en 2027 | Rattachement : le produit est de 2026 | **FAE** : 4181 / 706 + 44587 |
| 3 | Charge payée en 2026 pour une période qui court jusqu'en 2027 | Rattachement : on retire la part 2027 | **CCA** : 486 / 616 |
| 4 | Intérêts du 01/12 au 31/12 non encore payés | Rattachement : intérêts de 2026 | **ICNE** : 6611 / 1688 |
| 5 | Condamnation probable, montant estimable | Prudence : passif probable | **Provision** : 6815 / 1511 |
| 6 | Client en redressement judiciaire | Prudence : perte probable sur une créance | Reclassement 416 + **dépréciation** 6817 / 491 |
| 7 | Stock qui a baissé pendant l'année | Les achats de 2026 doivent être corrigés de la variation | 6032 / 322 puis 322 / 6032 |

**Pourquoi 44586 et 44587 ?** La TVA ne figure pas encore sur une facture : on ne peut ni la déduire (44566) ni la déclarer (44571). Les comptes 44586 / 44587 la « mettent de côté » jusqu'à la vraie facture.

**Information 6 — erreur de l'établissement** : la TVA de 1 200,00 € n'est **pas** une perte pour GSF Riviera. Comme la TVA sur les prestations de GSF Riviera est exigible à l'**encaissement**, elle n'a pas encore été reversée au Trésor pour cette facture impayée : si le client ne paie jamais, GSF Riviera ne la reversera jamais (et, pour une TVA déjà déclarée, elle pourrait la récupérer). La perte probable porte donc seulement sur le **HT** : 6 000,00 × 60 % = **3 600,00 €**, et non 4 320,00 €. La créance TTC est d'abord **reclassée** en 416 (créance douteuse) pour être suivie à part.

**Les extournes (question 4)** : on extourne au 01/01/2027 les écritures qui **anticipent une pièce à venir** ou une **charge/produit déjà enregistrés** (FNP, FAE, CCA, ICNE). Ainsi, quand la vraie facture ou l'échéance arrivera en 2027, on la saisira normalement, sans double comptabilisation.
On n'extourne **pas** :
- la **provision pour litige** et la **dépréciation** : elles sont **réexaminées** à la prochaine clôture (reprise 7815 / 7817 si le risque disparaît ou se réalise) ;
- le **reclassement en 416** : la créance reste douteuse tant qu'elle n'est pas réglée ou perdue ;
- la **variation de stock** : le stock final 2026 devient le stock initial 2027, il sera annulé à la clôture 2027.

## 2. Calculs (détaillés, chaque montant justifié)

| Info | Calcul | Montant |
|---|---|---|
| 1 — FNP HT | attachement | 6 800,00 € |
| 1 — TVA | 6 800,00 × 20 % | 1 360,00 € |
| 1 — 4081 | 6 800,00 + 1 360,00 | 8 160,00 € |
| 2 — FAE HT | prestation réceptionnée | 4 250,00 € |
| 2 — TVA | 4 250,00 × 20 % | 850,00 € |
| 2 — 4181 | 4 250,00 + 850,00 | 5 100,00 € |
| 3 — CCA | 14 400,00 × 9/12 (janvier à septembre 2027) | 10 800,00 € |
| 4 — ICNE | 84 000,00 × 3,60 % × 1/12 (01/12 au 31/12) | 252,00 € |
| 5 — Provision | estimation de l'avocat (pas la demande de 28 000,00 €) | 12 000,00 € |
| 6 — Reclassement 416 | créance TTC | 7 200,00 € |
| 6 — Dépréciation | 6 000,00 (HT) × 60 % | **3 600,00 €** (et non 4 320,00 €) |
| 7 — Variation de stock | 23 450,00 − 19 870,00 (stock en baisse = consommation en plus) | 3 580,00 € de charge |

**Impact sur le résultat 2026 (question 5)**

| Info | Effet | Montant |
|---|---|---|
| 1 FNP | charge en plus | −6 800,00 |
| 2 FAE | produit en plus | +4 250,00 |
| 3 CCA | charge en moins | +10 800,00 |
| 4 ICNE | charge en plus | −252,00 |
| 5 Provision litige | charge en plus | −12 000,00 |
| 6 Dépréciation | charge en plus | −3 600,00 |
| 7 Variation de stock | charge en plus | −3 580,00 |
| **Total** | | **−11 182,00 €** |

Le résultat 2026 diminue de **11 182,00 €** (avant impôt). Le reclassement 411 → 416 n'a aucun effet sur le résultat.

## 3. Écritures comptables

**Écritures d'inventaire au 31/12/2026**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 611 | Sous-traitance générale | FNP Vitres Côte d'Azur – vitres Arenas 12/2026 | 6 800,00 | |
| 31/12/2026 | OD | 44586 | TVA sur factures non parvenues | FNP Vitres Côte d'Azur – TVA | 1 360,00 | |
| 31/12/2026 | OD | 4081 | Fournisseurs – factures non parvenues | FNP Vitres Côte d'Azur | | 8 160,00 |
| 31/12/2026 | OD | 4181 | Clients – factures à établir | FAE Résidence Les Oliviers – remise en état | 5 100,00 | |
| 31/12/2026 | OD | 706 | Prestations de services | FAE Résidence Les Oliviers | | 4 250,00 |
| 31/12/2026 | OD | 44587 | TVA sur factures à établir | FAE Résidence Les Oliviers – TVA | | 850,00 |
| 31/12/2026 | OD | 486 | Charges constatées d'avance | CCA assurance flotte 01-09/2027 (9/12) | 10 800,00 | |
| 31/12/2026 | OD | 616 | Primes d'assurances | CCA assurance flotte 01-09/2027 | | 10 800,00 |
| 31/12/2026 | OD | 6611 | Intérêts des emprunts et dettes | ICNE prêt matériel 01/12-31/12/2026 | 252,00 | |
| 31/12/2026 | OD | 1688 | Intérêts courus | ICNE prêt matériel | | 252,00 |
| 31/12/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Provision litige prud'homal ancien chef d'équipe | 12 000,00 | |
| 31/12/2026 | OD | 1511 | Provisions pour litiges | Provision litige prud'homal | | 12 000,00 |
| 31/12/2026 | OD | 416 | Clients douteux ou litigieux | Syndic Azur Gestion – RJ du 03/12/2026 – VT-26-1187 | 7 200,00 | |
| 31/12/2026 | OD | 411 | Clients | Syndic Azur Gestion – reclassement en douteux | | 7 200,00 |
| 31/12/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation Syndic Azur Gestion 60 % du HT | 3 600,00 | |
| 31/12/2026 | OD | 491 | Dépréciations des comptes de clients | Dépréciation Syndic Azur Gestion | | 3 600,00 |
| 31/12/2026 | OD | 6032 | Variation des stocks des autres approvisionnements | Annulation stock initial produits d'entretien | 23 450,00 | |
| 31/12/2026 | OD | 322 | Stocks de fournitures consommables | Annulation stock initial produits d'entretien | | 23 450,00 |
| 31/12/2026 | OD | 322 | Stocks de fournitures consommables | Stock final produits d'entretien au 31/12/2026 | 19 870,00 | |
| 31/12/2026 | OD | 6032 | Variation des stocks des autres approvisionnements | Stock final produits d'entretien | | 19 870,00 |
| | | | | **Totaux** | **90 432,00** | **90 432,00** |

**Écritures d'extourne au 01/01/2027** (seulement FNP, FAE, CCA, ICNE)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/01/2027 | OD | 4081 | Fournisseurs – factures non parvenues | Extourne FNP Vitres Côte d'Azur | 8 160,00 | |
| 01/01/2027 | OD | 611 | Sous-traitance générale | Extourne FNP Vitres Côte d'Azur | | 6 800,00 |
| 01/01/2027 | OD | 44586 | TVA sur factures non parvenues | Extourne FNP Vitres Côte d'Azur – TVA | | 1 360,00 |
| 01/01/2027 | OD | 706 | Prestations de services | Extourne FAE Résidence Les Oliviers | 4 250,00 | |
| 01/01/2027 | OD | 44587 | TVA sur factures à établir | Extourne FAE Résidence Les Oliviers – TVA | 850,00 | |
| 01/01/2027 | OD | 4181 | Clients – factures à établir | Extourne FAE Résidence Les Oliviers | | 5 100,00 |
| 01/01/2027 | OD | 616 | Primes d'assurances | Extourne CCA assurance flotte | 10 800,00 | |
| 01/01/2027 | OD | 486 | Charges constatées d'avance | Extourne CCA assurance flotte | | 10 800,00 |
| 01/01/2027 | OD | 1688 | Intérêts courus | Extourne ICNE prêt matériel | 252,00 | |
| 01/01/2027 | OD | 6611 | Intérêts des emprunts et dettes | Extourne ICNE prêt matériel | | 252,00 |
| | | | | **Totaux** | **24 312,00** | **24 312,00** |

**Ce que fait l'extourne, concrètement (exemple de l'information 1)** : le 12/01/2027, la facture de Vitres Côte d'Azur arrive et est saisie normalement (611 6 800,00 au débit). Avec l'extourne du 01/01 (611 6 800,00 au crédit), le compte 611 de 2027 est à zéro pour cette prestation : la charge n'est comptée **qu'une fois**, en 2026.

## 4. Points d'attention / pièges

- **Dépréciation sur le TTC** (proposition de l'établissement) : erreur classique ; on déprécie le **HT** (3 600,00 €), la TVA n'est pas une perte.
- **Provision au montant demandé** (28 000,00 €) : non, on retient la **meilleure estimation** du risque (12 000,00 €, avis de l'avocat). L'avis daté du 08/01/2027 est un **événement postérieur** qui éclaire une situation existant au 31/12 : on en tient compte.
- **Assurance** : pas de TVA sur les primes d'assurance (taxe spéciale incluse dans la prime) : la CCA porte sur le montant total.
- **ICNE** : on ne calcule les intérêts que sur la période **non encore payée** (décembre), sur le capital restant dû après la dernière échéance.
- **Stock** : ne jamais passer seulement la différence (3 580,00 €) en une ligne sans annuler le stock initial : le bilan doit montrer le stock final (19 870,00 €). Et le stock **ne s'extourne pas**.
- **Extourner une provision ou une dépréciation** : erreur fréquente des logiciels mal paramétrés (« extourne automatique de toutes les OD d'inventaire ») : vérifiez la liste des écritures extournées.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Phrase d'entretien (30 secondes) :**
> « À la clôture, je me pose deux questions : est-ce que chaque charge et chaque produit est dans le bon exercice — c'est les FNP, FAE, CCA, PCA et intérêts courus, que j'extourne au 1er janvier — et est-ce qu'il existe un risque probable de perte — c'est les provisions et dépréciations, que je n'extourne pas mais que je réexamine à chaque clôture. »

**Message à l'établissement de Nice (information 6) :**
> « Bonjour, la créance Syndic Azur Gestion est reclassée en client douteux et dépréciée à 60 % du HT, soit 3 600,00 € (la TVA ne se déprécie pas). Pensez à **déclarer la créance de 7 200,00 € au mandataire judiciaire** dans le délai légal à compter de la publication du jugement d'ouverture : sans déclaration, la créance est inopposable à la procédure. Merci de m'envoyer la copie de la déclaration pour le dossier de clôture. »

**Documentation du dossier** : une feuille par écriture d'inventaire avec la pièce justificative (attachement, avis d'échéance, lettre d'avocat, jugement, état d'inventaire signé), et une liste « extournes au 01/01 » cochée.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : principe de prudence et indépendance des exercices (règles générales des comptes annuels).
- PCG : règles sur les passifs (provisions : obligation à la clôture, sortie de ressources probable, montant estimable) ; dépréciation des créances ; comptes 408, 418, 4458, 486, 1688, 151, 416, 491, 6032, 6815, 6817.
- PCG, règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06 : nomenclature applicable aux exercices ouverts à compter du 01/01/2025.
- CGI : exigibilité de la TVA sur les prestations de services à l'encaissement ; récupération de la TVA sur créances irrécouvrables (*référence précise à vérifier*).
- Code de commerce : déclaration des créances en procédure collective (*article et délai à vérifier*).
