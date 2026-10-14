# Corrigé E10-13 — Paul Durand : rester micro, passer au réel ou créer une société ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-13](../exercices/E10-13_micro-reel-societe-paul-durand.md)

## 1. Analyse

**Règle de sortie** : le régime micro est perdu lorsque le CA dépasse le plafond **deux années civiles consécutives** ; la sortie intervient au **1er janvier de l'année suivant** la seconde année de dépassement.

| Année | CA | Dépassement de 83 600 € ? | Régime |
|---|---|---|---|
| 2025 | 61 000 € | Non | Micro |
| 2026 | 96 000 € | Oui (1re année) | **Reste micro** (sauf option pour le réel) |
| 2027 | ? | Si oui (2e année consécutive) | Micro en 2027 |
| 2028 | | | **Réel obligatoire** si 2026 et 2027 dépassent |

Paul **ne perd donc pas** le régime en 2026. Ce qu'il perd dès 2026, c'est la **franchise en base de TVA** (seuils propres, plus bas, avec effet immédiat en cas de dépassement du seuil majoré) — traité en M04.

La simulation compare des **ordres de grandeur** : les hypothèses de cotisations sont volontairement simplifiées et doivent être affichées.

## 2. Calculs

**a) Micro-BNC**

| Élément | Calcul | Montant |
|---|---|---|
| CA | | 96 000,00 |
| Revenu imposable | 96 000 × 66 % | 63 360,00 |
| Cotisations sociales | 96 000 × 26,1 % | 25 056,00 |
| CFP | 96 000 × 0,2 % | 192,00 |
| IR | (29 315 – 11 497) × 11 % + (63 360 – 29 315) × 30 % = 1 959,98 + 10 213,50 | 12 173,48 |
| **Disponible** | 96 000 – 9 500 – 25 056 – 192 – 12 173,48 | **49 078,52** |

**b) Entreprise individuelle au réel (2035)**

| Élément | Calcul | Montant |
|---|---|---|
| Recettes – charges réelles | 96 000 – 9 500 | 86 500,00 |
| Bénéfice B (cotisations = 45 % × B) | 86 500 / 1,45 | 59 655,17 |
| Cotisations TNS | 45 % × 59 655,17 | 26 844,83 |
| IR | 1 959,98 + (59 655,17 – 29 315) × 30 % | 11 062,03 |
| **Disponible** | 59 655,17 – 11 062,03 | **48 593,14** |

**c1) SASU — 100 % rémunération**

| Élément | Calcul | Montant |
|---|---|---|
| Disponible dans la société | 96 000 – 9 500 – 3 000 | 83 500,00 |
| Net versé | 83 500 / 1,82 | 45 879,12 |
| Net imposable | 45 879,12 × 1,03 | 47 255,49 |
| Après abattement de 10 % | 47 255,49 × 90 % | 42 529,95 |
| IR | 1 959,98 + (42 529,95 – 29 315) × 30 % | 5 924,46 |
| **Disponible** | 45 879,12 – 5 924,46 | **39 954,66** |

(Résultat de la société nul : aucun IS.)

**c2) SASU — 100 % dividendes (aucune rémunération)**

| Élément | Calcul | Montant |
|---|---|---|
| Bénéfice de la société | | 83 500,00 |
| IS | 42 500 × 15 % + 41 000 × 25 % = 6 375 + 10 250 | 16 625,00 |
| Dividende distribuable | 83 500 – 16 625 | 66 875,00 |
| PFU 31,4 % | | 20 998,75 |
| **Disponible** | 66 875 – 20 998,75 | **45 876,25** |

**Synthèse 2026**

| Option | Disponible | Écart vs micro |
|---|---|---|
| a) Micro-BNC | **49 078,52 €** | — |
| b) Réel BNC | 48 593,14 € | – 485,38 € |
| c1) SASU 100 % salaire | 39 954,66 € | – 9 123,86 € |
| c2) SASU 100 % dividendes | 45 876,25 € | – 3 202,27 € |

## 3. Écritures comptables

Sans objet pour un micro-entrepreneur (livre des recettes et registre des achats). Si l'option c) était retenue, les écritures de constitution relèvent du module M11.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| — | — | — | — | Aucune écriture (micro-entreprise) | 0,00 | 0,00 |
| | | | | **Totaux** | **0,00** | **0,00** |

## 4. Points d'attention / pièges

- **« Je perds le micro tout de suite »** : faux pour l'IR et les cotisations ; vrai (avec ses propres seuils) pour la **franchise de TVA**.
- **Micro vs réel** : le réel n'est intéressant que si les charges réelles dépassent l'abattement (34 % du CA, soit 32 640 €) — ici, 9 500 € seulement.
- **SASU 100 % dividendes** : pas de cotisations, donc **aucun droit** retraite, pas d'indemnités journalières ; et les dividendes ne valident aucun trimestre.
- **SASU 100 % salaire** : la meilleure protection sociale, mais le coût de cotisations le plus élevé.
- Le PFU retenu (31,4 %) tient compte de la hausse de CSG de la LFSS 2026 : *à vérifier*. Option possible pour le barème avec abattement de 40 % (rarement favorable à ce niveau de revenu pour un célibataire).
- La simulation ignore : la CSG non déductible au réel, la réforme de l'assiette des indépendants, les plafonds de cotisations, la création d'une société en cours d'année (coûts et calendrier), la **TVA**.

## 5. Ce qu'un senior ferait en plus

**Ce que la simulation ne montre pas** : la stabilité du CA (un contrat unique ≠ un revenu récurrent), les droits sociaux, le besoin de trésorerie (une SASU permet de laisser des bénéfices taxés à 15 %), le risque de **dépendance économique** (requalification en salariat si Logistique Saône est son unique client), et le temps administratif.

**Mail type à Paul** :

> « Bonjour Paul, rassurez-vous : vous restez micro-entrepreneur pour 2026. Vous ne sortiriez du régime qu'au 1er janvier 2028, et seulement si 2027 dépasse aussi 83 600 €. Nos simulations pour 2026 (hypothèses jointes) : micro ≈ 49 100 € disponibles, réel ≈ 48 600 €, société ≈ 40 000 à 45 900 € selon le mode de rémunération. Créer une société avant décembre ne vous ferait donc rien gagner cette année. En revanche, vous devez dès maintenant facturer la TVA depuis le dépassement du seuil de franchise : nous vous appelons lundi pour la mettre en place. Faisons un point en juin 2027 sur votre chiffre d'affaires : si le niveau se confirme, la société (avec une partie du bénéfice laissée en réserve) pourra devenir intéressante. Bien à vous. »

- Remettre la simulation **écrite** avec les hypothèses et la mention « estimation, valeurs à vérifier ».
- Programmer un rendez-vous de mi-année 2027.

## 6. Références

- CGI : art. 102 ter (micro-BNC, plafond, abattement, sortie du régime), art. 151-0 (versement libératoire), art. 293 B (franchise en base de TVA), art. 219 (IS), art. 200 A (PFU), art. 158-3 (abattement de 40 % sur option pour le barème), art. 83 (abattement de 10 % sur salaires).
- Code de la sécurité sociale : art. L. 613-7 (micro-social).
