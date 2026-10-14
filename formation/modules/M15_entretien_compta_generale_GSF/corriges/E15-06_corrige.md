# Corrigé E15-06 — Test technique : acquisition d'une autolaveuse, plan d'amortissement et cession d'un véhicule utilitaire

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-06](../exercices/E15-06_immobilisations-acquisition-amortissement-cession.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Étape 1 — Qu'est-ce qui entre dans le coût de l'autolaveuse ? (question 1)
La règle à retenir : le coût d'une immobilisation = **prix d'achat net de remise + tous les frais nécessaires pour amener la machine sur place et la faire fonctionner**. Tout ce qui sert à autre chose (former les gens, entretenir la machine plus tard) est une **charge**.

| Ligne | HT | Traitement | Pourquoi, en une phrase |
|---|---|---|---|
| Autolaveuse AL-80 | 18 500,00 | Coût (2154) | C'est le bien lui-même. |
| Remise commerciale 5 % | −925,00 | Coût (en moins) | Le coût, c'est ce qu'on paie réellement : la remise sur facture le diminue. |
| Transport et livraison | 350,00 | Coût (2154) | Sans transport, la machine n'est pas sur le site : frais directement nécessaires. |
| Installation de la borne de charge | 480,00 | Coût (2154) | Sans borne, la machine ne peut pas fonctionner : frais de mise en état de marche. |
| Formation de 3 agents | 600,00 | **Charge (6228)** | Elle profite au personnel, pas à la machine : elle est expressément exclue du coût. |

### Étape 2 — Deux comptes de TVA déductible (question 2)
La TVA sur la partie immobilisée va en **44562** (TVA sur immobilisations) ; la TVA sur la formation, qui est une charge, va en **44566**. De même, la dette envers le fournisseur se répartit en **404** (immobilisation) et **401** (charge). Beaucoup d'entreprises acceptent une seule ligne fournisseur ; l'important est la bonne ventilation HT et TVA.

### Étape 3 — Le plan d'amortissement (question 3)
- **Base** = coût d'entrée HT (la TVA est récupérée, elle n'est pas un coût).
- **Point de départ** = la **mise en service** (01/04/2026, pièce 2), pas la date de facture (10/03).
- **Annuité pleine** = base / 5 ans.
- **2026** : du 01/04 au 31/12 = 9 mois de 30 jours = 270 jours sur 360.
- La dernière année (2031) reçoit le « reste » : du 01/01 au 31/03/2031 = 90 jours, pour arriver exactement à 5 ans d'utilisation.

### Étape 4 — L'erreur du projet de facture de cession (question 4)
Le véhicule est un **utilitaire** dont la TVA a été **déduite à l'achat** (fiche d'immobilisation). Quand on revend un bien dont on a récupéré la TVA, la vente est **soumise à la TVA** sur le prix de vente. La mention « TVA non applicable – véhicule d'occasion » est fausse (le régime de la marge concerne les négociants en biens d'occasion, pas GSF Riviera qui vend son propre matériel). Il faut ajouter la TVA à 20 %.

### Étape 5 — La cession (question 5)
Une cession se fait toujours en **3 temps** :
1. **Dotation complémentaire** : on amortit le véhicule jusqu'au jour de la vente (il a servi du 01/01 au 30/06/2026).
2. **Sortie de l'actif** : on retire le véhicule du bilan. On solde l'amortissement (28182 au débit), on solde la valeur d'origine (2182 au crédit), et la différence, la **valeur nette comptable (VNC)**, va en charge au **675**.
3. **Facture de cession** : le prix de vente HT va en produit au **775**, la TVA en 44571, la créance sur l'acheteur en **462** (on n'utilise pas 411, réservé aux clients de l'activité).

Le résultat de cession = 775 − 675. On ne le comptabilise jamais directement : il « apparaît » par différence entre les deux comptes.

## 2. Calculs (détaillés, chaque montant justifié)

**Autolaveuse**

| Élément | Calcul | Montant |
|---|---|---|
| Coût d'entrée (2154) | 18 500,00 − 925,00 + 350,00 + 480,00 | **18 405,00 €** |
| TVA sur immobilisation (44562) | 18 405,00 × 20 % | 3 681,00 € |
| Dette 404 | 18 405,00 + 3 681,00 | 22 086,00 € |
| Formation (6228) | ligne de facture | 600,00 € |
| TVA sur formation (44566) | 600,00 × 20 % | 120,00 € |
| Dette 401 | 600,00 + 120,00 | 720,00 € |
| Contrôle total TTC | 22 086,00 + 720,00 | 22 806,00 € ✓ |
| Annuité pleine | 18 405,00 / 5 | 3 681,00 € |
| Dotation 2026 | 3 681,00 × 270 / 360 | **2 760,75 €** |
| Dotation 2031 | 3 681,00 × 90 / 360 | 920,25 € |

**Plan d'amortissement de l'autolaveuse**

| Exercice | Base | Dotation | Cumul | VNC fin d'exercice |
|---|---|---|---|---|
| 2026 (01/04-31/12, 270 j) | 18 405,00 | 2 760,75 | 2 760,75 | 15 644,25 |
| 2027 | 18 405,00 | 3 681,00 | 6 441,75 | 11 963,25 |
| 2028 | 18 405,00 | 3 681,00 | 10 122,75 | 8 282,25 |
| 2029 | 18 405,00 | 3 681,00 | 13 803,75 | 4 601,25 |
| 2030 | 18 405,00 | 3 681,00 | 17 484,75 | 920,25 |
| 2031 (01/01-31/03, 90 j) | 18 405,00 | 920,25 | 18 405,00 | 0,00 |

**Véhicule utilitaire cédé**

| Élément | Calcul | Montant |
|---|---|---|
| Annuité pleine | 28 000,00 / 5 | 5 600,00 € |
| Contrôle du cumul au 31/12/2025 | 2023 : 5 600 × 90/360 = 1 400 ; 2024 : 5 600 ; 2025 : 5 600 | 12 600,00 € ✓ (= fiche) |
| Dotation complémentaire 2026 | 5 600,00 × 180 / 360 (01/01-30/06) | **2 800,00 €** |
| Amortissements cumulés au 30/06/2026 | 12 600,00 + 2 800,00 | 15 400,00 € |
| VNC au 30/06/2026 (675) | 28 000,00 − 15 400,00 | **12 600,00 €** |
| Prix de cession HT (775) | projet de facture | 13 500,00 € |
| TVA collectée sur cession | 13 500,00 × 20 % | 2 700,00 € |
| Prix TTC (462) | 13 500,00 + 2 700,00 | **16 200,00 €** |
| Résultat de cession | 13 500,00 − 12 600,00 | **+900,00 € (plus-value)** |

**Facture de cession corrigée** : HT 13 500,00 € — TVA 20 % 2 700,00 € — TTC 16 200,00 €. Comme le garage a payé le **montant de la facture émise**, la facture doit être corrigée **avant** émission ; si elle avait déjà été émise à 13 500,00 €, il faudrait une facture rectificative et réclamer 2 700,00 € au garage (sinon GSF Riviera devrait quand même reverser la TVA, prélevée sur le prix encaissé).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 10/03/2026 | AC | 2154 | Matériel industriel | PES-26-0311 autolaveuse AL-80 n° AL80-26-00452 | 18 405,00 | |
| 10/03/2026 | AC | 44562 | TVA déductible sur immobilisations | PES-26-0311 TVA immobilisation | 3 681,00 | |
| 10/03/2026 | AC | 404 | Fournisseurs d'immobilisations | PES-26-0311 Propreté Équipement Sud | | 22 086,00 |
| 10/03/2026 | AC | 6228 | Divers – formations externes | PES-26-0311 formation 3 agents | 600,00 | |
| 10/03/2026 | AC | 44566 | TVA déductible sur autres biens et services | PES-26-0311 TVA formation | 120,00 | |
| 10/03/2026 | AC | 401 | Fournisseurs | PES-26-0311 Propreté Équipement Sud | | 720,00 |
| 30/06/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotation complémentaire VU GS-457-RV (180 j) | 2 800,00 | |
| 30/06/2026 | OD | 28182 | Amortissements du matériel de transport | Dotation complémentaire VU GS-457-RV | | 2 800,00 |
| 30/06/2026 | OD | 28182 | Amortissements du matériel de transport | Sortie VU GS-457-RV – solde amortissements | 15 400,00 | |
| 30/06/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie VU GS-457-RV – VNC | 12 600,00 | |
| 30/06/2026 | OD | 2182 | Matériel de transport | Sortie VU GS-457-RV – valeur d'origine | | 28 000,00 |
| 30/06/2026 | VT | 462 | Créances sur cessions d'immobilisations | CES-2026-003 Garage des Baous | 16 200,00 | |
| 30/06/2026 | VT | 775 | Produits des cessions d'éléments d'actif | CES-2026-003 cession VU GS-457-RV | | 13 500,00 |
| 30/06/2026 | VT | 44571 | TVA collectée | CES-2026-003 TVA 20 % | | 2 700,00 |
| 15/07/2026 | BQ | 512 | Banque | Virement Garage des Baous CES-2026-003 | 16 200,00 | |
| 15/07/2026 | BQ | 462 | Créances sur cessions d'immobilisations | Règlement CES-2026-003 | | 16 200,00 |
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotation 2026 autolaveuse AL-80 (270 j) | 2 760,75 | |
| 31/12/2026 | OD | 28154 | Amortissements du matériel industriel | Dotation 2026 autolaveuse AL-80 | | 2 760,75 |
| | | | | **Totaux** | **88 766,75** | **88 766,75** |

**Pourquoi ce sens ?** (à savoir expliquer à l'oral)
- Une immobilisation achetée est un **emploi** : 2154 au **débit**. La dette fournisseur est une **ressource** : 404 au **crédit**.
- Les amortissements (28x) sont des comptes d'actif « en négatif » : ils augmentent au **crédit** et on les solde au **débit** quand le bien sort.
- 675 est une **charge** (débit), 775 un **produit** (crédit) : c'est pour cela qu'on ne « compense » pas.

## 4. Points d'attention / pièges

- **Date de départ** : le 01/04 (mise en service), pas le 10/03 (facture). Partir du 10/03 donnerait 2026 = 3 681,00 × 291 / 360 = 2 975,48 € (21 jours en mars + 270), une dotation surévaluée.
- **Formation** immobilisée « parce qu'elle est sur la même facture » : erreur la plus fréquente.
- **Oublier la dotation complémentaire** avant la sortie : la VNC serait fausse (15 400,00 € au lieu de 12 600,00 €) et le résultat de cession aussi (−1 900,00 € au lieu de +900,00 €). Le résultat global ne change pas, mais la présentation (exploitation / cessions) est faussée.
- **Ne pas passer le prix de vente en 706** ni la créance en 411 : la cession d'un bien n'est pas une prestation de nettoyage.
- **TVA sur la cession** : bien dont la TVA a été déduite → cession taxable. À l'inverse, pour une voiture de tourisme dont la TVA n'a pas été récupérée, la vente n'est pas soumise à TVA.
- **Le résultat de cession reste dans 675 / 775** même avec le PCG 2025 : la suppression concerne les comptes de transfert de charges (791, 796, 797), pas les cessions.
- **Fichier des immobilisations** : sortir la fiche n° 2182-0457 et créer la fiche de l'autolaveuse (n° de série, site, date de mise en service).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Pour aller plus loin — amortissement dégressif de la balayeuse (facultatif)**

Raisonnement : le dégressif s'applique à la **VNC** du début d'année (et non à la valeur d'origine), au taux de 5 ans × 1,75 = 20 % × 1,75 = **35 %**. 2026 compte **6 mois** (premier jour du mois d'acquisition : 01/07). Chaque année, on compare 35 % au taux linéaire « 1 / nombre d'années restantes » ; dès que le linéaire est plus fort, on passe au linéaire.

| Exercice | VNC début | Taux retenu | Dotation | VNC fin |
|---|---|---|---|---|
| 2026 (6 mois) | 24 000,00 | 35 % × 6/12 | 4 200,00 | 19 800,00 |
| 2027 | 19 800,00 | 35 % (linéaire 1/4 = 25 %) | 6 930,00 | 12 870,00 |
| 2028 | 12 870,00 | 35 % (linéaire 1/3 = 33,33 %) | 4 504,50 | 8 365,50 |
| 2029 | 8 365,50 | linéaire 1/2 = 50 % | 4 182,75 | 4 182,75 |
| 2030 | 4 182,75 | linéaire 1/1 = 100 % | 4 182,75 | 0,00 |

(Contrôle : 4 200,00 + 6 930,00 + 4 504,50 + 4 182,75 + 4 182,75 = 24 000,00 ✓.)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/07/2026 | AC | 2154 | Matériel industriel | Achat balayeuse aspiratrice | 24 000,00 | |
| 05/07/2026 | AC | 44562 | TVA déductible sur immobilisations | TVA balayeuse | 4 800,00 | |
| 05/07/2026 | AC | 404 | Fournisseurs d'immobilisations | Achat balayeuse aspiratrice | | 28 800,00 |
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotation 2026 balayeuse (dégressif 35 % × 6/12) | 4 200,00 | |
| 31/12/2026 | OD | 28154 | Amortissements du matériel industriel | Dotation 2026 balayeuse | | 4 200,00 |
| | | | | **Totaux** | **33 000,00** | **33 000,00** |

> Si le groupe amortissait ce bien en linéaire en comptabilité et en dégressif seulement pour le fiscal, l'écart serait un **amortissement dérogatoire** (145 / 6872). Ce n'est pas demandé ici, mais citer le mot en entretien montre que vous connaissez la différence.

**Réponse orale à la question 6 (30 secondes) :**
> « L'installation est nécessaire pour que la machine fonctionne : sans borne, l'autolaveuse ne roule pas, donc c'est un coût directement attribuable, on l'immobilise. La formation, elle, rend le personnel compétent, pas la machine : le plan comptable l'exclut du coût d'acquisition, c'est une charge de l'exercice. »

**Message à l'établissement de Nice :** « Le projet de facture CES-2026-003 ne peut pas partir en l'état : le fourgon GS-457-RV a eu sa TVA récupérée à l'achat, sa revente est donc soumise à TVA 20 %. Montant à facturer : 13 500,00 € HT + 2 700,00 € de TVA = 16 200,00 € TTC. Merci de prévenir le Garage des Baous avant envoi. »

**Contrôle** : après la cession, rapprocher le fichier des immobilisations avec la balance (2182 et 28182 doivent avoir baissé de 28 000,00 € et de 15 400,00 € au total des mouvements de sortie).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : définition et coût d'entrée des immobilisations corporelles (articles 211-1 et 213-8 : frais directement attribuables inclus, frais de formation exclus) ; amortissement à compter de la date de mise en service ; sortie des immobilisations (comptes 675 et 775).
- PCG, règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06 (exercices ouverts à compter du 01/01/2025) : maintien des comptes 675 / 775 pour les cessions d'immobilisations.
- CGI : article 39 A (amortissement dégressif, coefficients) ; règles de TVA applicables aux cessions de biens d'investissement ayant ouvert droit à déduction (*référence précise à vérifier dans le CGI et le BOFiP*).
- Comptes PCG : 2154, 2182, 28154, 28182, 404, 44562, 44566, 44571, 462, 675, 775, 6811.
