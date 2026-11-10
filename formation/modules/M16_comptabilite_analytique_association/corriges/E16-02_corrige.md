# Corrigé E16-02 — Répartir les charges communes avec des clés de répartition

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-02](../exercices/E16-02_repartir-charges-communes.md)

!!! abstract "En clair"
    La méthode tient en trois gestes, répétés pour chaque rubrique :
    1. **Total des unités** de la clé (m², km, ETP, euros de charges directes).
    2. **Coût d'une unité** = montant à répartir ÷ total des unités.
    3. **Part d'une section** = ses unités × coût d'une unité.

    À la fin, **la somme des parts doit redonner exactement le montant de départ** et la section 00-COMMUN doit revenir à **zéro**.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Pourquoi c'est important

Le SESSAD est payé par l'ARS (agence régionale de santé), le SAVS (service d'accompagnement à la vie sociale) par le Département, l'emploi accompagné par l'ARS, l'AGEFIPH et le FIPHFP. Chacun de ces financeurs ne paie que **son** service. Si le SESSAD supporte une partie du loyer du SAVS, l'ARS finance en réalité le Département : c'est une **erreur d'affectation** que le commissaire aux comptes et les autorités de tarification peuvent relever.

### La salle commune : le piège du dénominateur

La salle commune (30 m²) n'a pas d'occupant propre. La fiche dit de la répartir « comme le reste », c'est-à-dire **au prorata des surfaces privatives** (590 m²). Deux façons de faire, même résultat :
- répartir les 30 m² au prorata des 590 m², puis ajouter ces m² à chaque section ;
- ou, plus court, diviser directement le montant par **590 m²** (et non par 620).

> ⚠️ Erreur classique : diviser par 620 m². On obtient 91 360,00 / 620 = 147,35 €/m², et après répartition des 590 m² privatifs il reste **4 420,65 €** sur la section 00-COMMUN, que personne ne paie.

### Le véhicule « pool »

Ses kilomètres sont déjà découpés par section dans le carnet de bord : on les **ajoute** aux kilomètres des véhicules affectés. Pour l'assurance flotte, on attribue 900,00 € par véhicule affecté, et les 900,00 € du véhicule pool sont découpés selon **ses** kilomètres (9 000 km).

### Les honoraires CAC et expert-comptable

Il n'y a pas de lien physique (ni m², ni km). La fiche prévoit la clé **charges directes** : un service qui dépense plus génère plus de pièces à contrôler. Le siège et la vie associative sont **exclus** par décision du bureau.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 1 — Locaux (91 360,00 €, clé m²)

| Section | m² privatifs | Part de la salle commune (30 × m² / 590) | Surface attribuée | Pourcentage | Montant |
|---|---|---|---|---|---|
| 01-SIEGE | 90 | 4,58 | 94,58 | 15,25 % | 13 936,27 € |
| 10-SESSAD | 280 | 14,24 | 294,24 | 47,46 % | 43 357,29 € |
| 20-SAVS | 160 | 8,14 | 168,14 | 27,12 % | 24 775,59 € |
| 30-EMPLOI | 60 | 3,05 | 63,05 | 10,17 % | 9 290,85 € |
| **Total** | **590** | **30,00** | **620,00** | **100 %** | **91 360,00 €** |

Coût du m² privatif : 91 360,00 / 590 = **154,85 €** (valeur arrondie ; les montants sont calculés sans arrondir le coût unitaire).
Exemple : SESSAD = 91 360,00 × 280 / 590 = 43 357,29 €.
*(La colonne « surface attribuée » est arrondie : 94,58 + 294,24 + 168,14 + 63,05 = 620,01 ; c'est un simple écart d'affichage.)*

### Question 2 — Véhicules (53 000,00 €, clé km) et assurance flotte (7 200,00 €)

**Kilomètres par section :**

| Section | Véhicules affectés | Véhicule pool | Total km |
|---|---|---|---|
| 10-SESSAD | 72 000 | 3 000 | 75 000 |
| 20-SAVS | 31 000 | 2 000 | 33 000 |
| 30-EMPLOI | 15 000 | 2 500 | 17 500 |
| 50-PAIRS | — | 1 000 | 1 000 |
| 01-SIEGE | — | 500 | 500 |
| **Total** | **118 000** | **9 000** | **127 000** |

Coût moyen du kilomètre : 53 000,00 / 127 000 = **0,4173 €/km** (environ 42 centimes).

| Section | km | Calcul | Véhicules | Assurance flotte | Calcul assurance |
|---|---|---|---|---|---|
| 10-SESSAD | 75 000 | 53 000 × 75 000 / 127 000 | 31 299,22 € | 3 900,00 € | 4 × 900 + 900 × 3 000 / 9 000 = 3 600 + 300 |
| 20-SAVS | 33 000 | 53 000 × 33 000 / 127 000 | 13 771,65 € | 2 000,00 € | 2 × 900 + 200 |
| 30-EMPLOI | 17 500 | 53 000 × 17 500 / 127 000 | 7 303,15 € | 1 150,00 € | 1 × 900 + 250 |
| 50-PAIRS | 1 000 | 53 000 × 1 000 / 127 000 | 417,32 € | 100,00 € | 900 × 1 000 / 9 000 |
| 01-SIEGE | 500 | 53 000 × 500 / 127 000 | 208,66 € | 50,00 € | 900 × 500 / 9 000 |
| **Total** | **127 000** | | **53 000,00 €** | **7 200,00 €** | |

Arrondi : le calcul brut du SESSAD donne 31 299,21 € ; l'écart de 0,01 € est mis sur le SESSAD (plus grosse part) pour que le total tombe juste.

### Question 3 — Téléphonie et informatique (32 300,00 €, clé ETP)

Coût d'un ETP : 32 300,00 / 29,4 = **1 098,64 €** (arrondi).

| Section | ETP | Calcul | Montant |
|---|---|---|---|
| 01-SIEGE | 2,6 | 32 300 × 2,6 / 29,4 | 2 856,46 € |
| 10-SESSAD | 14,2 | 32 300 × 14,2 / 29,4 | 15 600,68 € |
| 20-SAVS | 7,8 | 32 300 × 7,8 / 29,4 | 8 569,39 € |
| 30-EMPLOI | 3,6 | 32 300 × 3,6 / 29,4 | 3 955,10 € |
| 40-HABITAT | 1,0 | 32 300 × 1,0 / 29,4 | 1 098,64 € |
| 50-PAIRS | 0,2 | 32 300 × 0,2 / 29,4 | 219,73 € |
| **Total** | **29,4** | | **32 300,00 €** |

### Question 4 — CAC et expert-comptable (37 920,00 €, clé charges directes)

Taux : 37 920,00 / 1 951 100,00 = **1,94 %** des charges directes.

| Section | Charges directes | Part | Montant |
|---|---|---|---|
| 10-SESSAD | 1 014 500,00 € | 52,00 % | 19 717,00 € |
| 20-SAVS | 552 300,00 € | 28,31 % | 10 734,06 € |
| 30-EMPLOI | 255 600,00 € | 13,10 % | 4 967,63 € |
| 40-HABITAT | 81 300,00 € | 4,17 % | 1 580,08 € |
| 50-PAIRS | 47 400,00 € | 2,43 % | 921,23 € |
| **Total** | **1 951 100,00 €** | **100 %** | **37 920,00 €** |

### Question 5 — Tableau récapitulatif

| Rubrique | 01-SIEGE | 10-SESSAD | 20-SAVS | 30-EMPLOI | 40-HABITAT | 50-PAIRS | Total |
|---|---|---|---|---|---|---|---|
| Locaux (m²) | 13 936,27 | 43 357,29 | 24 775,59 | 9 290,85 | — | — | 91 360,00 |
| Véhicules (km) | 208,66 | 31 299,22 | 13 771,65 | 7 303,15 | — | 417,32 | 53 000,00 |
| Assurance flotte | 50,00 | 3 900,00 | 2 000,00 | 1 150,00 | — | 100,00 | 7 200,00 |
| Téléphonie, informatique (ETP) | 2 856,46 | 15 600,68 | 8 569,39 | 3 955,10 | 1 098,64 | 219,73 | 32 300,00 |
| CAC et expert-comptable (charges directes) | — | 19 717,00 | 10 734,06 | 4 967,63 | 1 580,08 | 921,23 | 37 920,00 |
| **Total par section** | **17 051,39** | **113 874,19** | **59 850,69** | **26 666,73** | **2 678,72** | **1 658,28** | **221 780,00** |

Contrôle : 17 051,39 + 113 874,19 + 59 850,69 + 26 666,73 + 2 678,72 + 1 658,28 = **221 780,00 €** = total de la pièce 1 → la section 00-COMMUN est **soldée** ✓.

Lecture rapide : les charges communes représentent environ **10 %** des charges du SESSAD (113 874,19 sur 1 128 374,19), du SAVS et de l'emploi accompagné, mais seulement 3 % pour l'habitat et Pairs, qui n'ont pas de bureaux à Valence.

## 3. Écritures comptables

### Question 6 — OD analytique de répartition au 31/12/2026

En comptabilité **générale**, rien ne change : les comptes 6132, 6061, 626… gardent les mêmes montants. Seule l'**affectation analytique** bouge : on **crédite** la section 00-COMMUN et on **débite** les sections qui reçoivent la charge. Dans le logiciel, la grille de clés s'applique à chaque compte de la rubrique ; le tableau ci-dessous présente les totaux par rubrique.

| Date | Journal | Comptes | Rubrique | Section analytique | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6132, 614, 616 | Locaux de Valence – clé m² | 01-SIEGE | 13 936,27 | |
| 31/12/2026 | OD | 6132, 614, 616 | Locaux de Valence – clé m² | 10-SESSAD | 43 357,29 | |
| 31/12/2026 | OD | 6132, 614, 616 | Locaux de Valence – clé m² | 20-SAVS | 24 775,59 | |
| 31/12/2026 | OD | 6132, 614, 616 | Locaux de Valence – clé m² | 30-EMPLOI | 9 290,85 | |
| 31/12/2026 | OD | 6132, 614, 616 | Locaux de Valence – clé m² | 00-COMMUN | | 91 360,00 |
| 31/12/2026 | OD | 6135, 6061, 6155, 6251 | Véhicules – clé km | 01-SIEGE | 208,66 | |
| 31/12/2026 | OD | 6135, 6061, 6155, 6251 | Véhicules – clé km | 10-SESSAD | 31 299,22 | |
| 31/12/2026 | OD | 6135, 6061, 6155, 6251 | Véhicules – clé km | 20-SAVS | 13 771,65 | |
| 31/12/2026 | OD | 6135, 6061, 6155, 6251 | Véhicules – clé km | 30-EMPLOI | 7 303,15 | |
| 31/12/2026 | OD | 6135, 6061, 6155, 6251 | Véhicules – clé km | 50-PAIRS | 417,32 | |
| 31/12/2026 | OD | 6135, 6061, 6155, 6251 | Véhicules – clé km | 00-COMMUN | | 53 000,00 |
| 31/12/2026 | OD | 616 | Assurance flotte – véhicules affectés | 01-SIEGE | 50,00 | |
| 31/12/2026 | OD | 616 | Assurance flotte – véhicules affectés | 10-SESSAD | 3 900,00 | |
| 31/12/2026 | OD | 616 | Assurance flotte – véhicules affectés | 20-SAVS | 2 000,00 | |
| 31/12/2026 | OD | 616 | Assurance flotte – véhicules affectés | 30-EMPLOI | 1 150,00 | |
| 31/12/2026 | OD | 616 | Assurance flotte – véhicules affectés | 50-PAIRS | 100,00 | |
| 31/12/2026 | OD | 616 | Assurance flotte – véhicules affectés | 00-COMMUN | | 7 200,00 |
| 31/12/2026 | OD | 626, 6156 | Téléphonie, informatique – clé ETP | 01-SIEGE | 2 856,46 | |
| 31/12/2026 | OD | 626, 6156 | Téléphonie, informatique – clé ETP | 10-SESSAD | 15 600,68 | |
| 31/12/2026 | OD | 626, 6156 | Téléphonie, informatique – clé ETP | 20-SAVS | 8 569,39 | |
| 31/12/2026 | OD | 626, 6156 | Téléphonie, informatique – clé ETP | 30-EMPLOI | 3 955,10 | |
| 31/12/2026 | OD | 626, 6156 | Téléphonie, informatique – clé ETP | 40-HABITAT | 1 098,64 | |
| 31/12/2026 | OD | 626, 6156 | Téléphonie, informatique – clé ETP | 50-PAIRS | 219,73 | |
| 31/12/2026 | OD | 626, 6156 | Téléphonie, informatique – clé ETP | 00-COMMUN | | 32 300,00 |
| 31/12/2026 | OD | 6226 | CAC et expert-comptable – clé charges directes | 10-SESSAD | 19 717,00 | |
| 31/12/2026 | OD | 6226 | CAC et expert-comptable – clé charges directes | 20-SAVS | 10 734,06 | |
| 31/12/2026 | OD | 6226 | CAC et expert-comptable – clé charges directes | 30-EMPLOI | 4 967,63 | |
| 31/12/2026 | OD | 6226 | CAC et expert-comptable – clé charges directes | 40-HABITAT | 1 580,08 | |
| 31/12/2026 | OD | 6226 | CAC et expert-comptable – clé charges directes | 50-PAIRS | 921,23 | |
| 31/12/2026 | OD | 6226 | CAC et expert-comptable – clé charges directes | 00-COMMUN | | 37 920,00 |
| | | | | **Totaux** | **221 780,00** | **221 780,00** |

*Les numéros 6155 (entretien du matériel de transport) et 6156 (maintenance) suivent le PCG ; vérifiez-les sur le plan de comptes de l'association.*

## 4. Points d'attention / pièges

### Question 7 — Réponse à Karim Belkacem

Sa remarque est **légitime**, mais la règle actuelle est celle de la fiche, validée par la direction : on l'applique pour 2026. Pour la suite, on peut proposer une clé plus fine, **si elle est mesurable** :
- tenir un **planning de réservation** de la salle (heures par service) pendant quelques mois ;
- si l'usage est très différent des surfaces (par exemple 50 % Pairs et SAVS le soir), proposer à la directrice une **clé « heures d'occupation »** pour les 30 m² de la salle commune, à partir de 2027.

Attention : si Pairs prend une part de la salle, le coût entre dans le budget du projet. Il faut que la Fondation Lumen **accepte** cette charge dans le budget de la subvention, sinon elle restera non financée.

Réponse possible : « Bonjour Karim, vous avez raison de poser la question. Pour 2026, j'applique la clé validée (au m²) : le SESSAD porte 14,24 m² de la salle, soit environ 2 205 €. Je vous propose de noter les réservations de la salle jusqu'en mars ; si l'usage est très différent, je proposerai à Nathalie Berthier une clé au temps d'occupation pour 2027. »

*(Calcul : 91 360,00 × 14,24 / 590 ≈ 2 205 € ; plus précisément 30 × 280 / 590 m² × 154,85 €/m².)*

### Question 8 — La méthode de Mme Roux sur la part du siège

La part du siège (**17 051,39 €** : ses 94,58 m², ses 500 km, ses 2,6 ETP…) est une vraie charge **du siège**. Elle s'ajoute à ses autres charges et fait partie des **160 000 €** que coûte le siège.

Or le siège est déjà financé par les **frais de siège** : 4,5 % des charges des ESSMS (SESSAD, SAVS) et une quote-part pour les autres services (exercice E16-04). Si l'on répartit **en plus** la part du siège entre les services, on la fait payer **deux fois** :
- une fois par la répartition de Mme Roux ;
- une fois dans les frais de siège.

Et pour le SESSAD et le SAVS, ce serait des **frais de siège déguisés**, au-delà du taux autorisé de 4,5 % : l'autorité de tarification peut les **rejeter** (les retirer des charges acceptées).

**Bonne méthode :** la part du siège **reste sur 01-SIEGE**. Elle sera « récupérée » une seule fois, par le calcul des frais de siège.

### Autres pièges

- **Oublier une section** : Pairs n'a pas de bureau, mais il utilise le véhicule pool et a 0,2 ETP. Il porte donc une petite part des véhicules, de la flotte et de la téléphonie.
- **Arrondis** : faites toujours la somme de contrôle. Un écart de 0,01 € se met sur la plus grosse part, et on l'écrit.
- **Mélanger les clés** : l'assurance des **locaux** suit les m², l'assurance de la **flotte** suit les véhicules. Ce sont deux rubriques différentes, même si elles sont sur le même compte 616.
- **Clés de l'année** : les ETP, les m² et les kilomètres changent. Mettez à jour les clés **chaque année** (et pour les km, à partir des **carnets de bord réels**, pas du budget).

## 5. Ce qu'un senior ferait en plus

- **Faire valider les clés par écrit** par la directrice, avec une **fiche de procédure** (une page : rubrique, clé, source de la clé, date de mise à jour). Le commissaire aux comptes la demandera, et les financeurs veulent des clés **stables** d'une année sur l'autre : changer de clé, c'est déplacer de l'argent entre financeurs.
- **Garder les justificatifs des clés** : plan des locaux avec surfaces, synthèse des carnets de bord signée, tableau des ETP au 31/12.
- **Comparer avec le budget** : la répartition du budget (EPRD du SESSAD, budget prévisionnel du SAVS) utilisait-elle les mêmes clés ? Un écart de clé entre budget et réalisé est une source classique d'écart à expliquer.
- **Proposer de réduire les charges communes** : les véhicules affectés à un seul service pourraient être imputés **en direct** (le relevé carburant détaille déjà chaque véhicule). La clé km ne resterait alors que pour le véhicule pool. C'est plus juste et plus simple à expliquer.
- **Préparer un mail à Hélène Ferrand** : « Bonjour Hélène, voici la répartition 2026 des charges communes sur la base des estimations annuelles (221 780,00 €). La section 00-COMMUN est soldée. Deux points à valider : la demande du SESSAD sur la salle commune (proposition de clé au temps d'occupation pour 2027) et le maintien de la part du siège (17 051,39 €) sur 01-SIEGE, financée par les frais de siège. »

## 6. Références

- Plan comptable des ESSMS et cadre budgétaire du Code de l'action sociale et des familles : affectation des charges par établissement ou service, groupes fonctionnels, frais de siège autorisés — *textes à vérifier dans leur version en vigueur*.
- Règlement ANC n° 2018-06 (associations) et PCG (comptes 6132, 614, 616, 6135, 6061, 6155, 6251, 626, 6156, 6226).
- Fiche de l'association Cap Horizons 21, § 3.4 (frais de siège) et § 3.5 (clés de répartition).
