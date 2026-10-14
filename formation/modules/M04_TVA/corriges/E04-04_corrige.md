# Corrigé E04-04 — Le coefficient de déduction de la holding

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-04](../exercices/E04-04_coefficient-deduction-holding.md)

## 1. Analyse

**a) Le mécanisme (art. 205 et 206 ann. II CGI).** La TVA d'une dépense est déductible à hauteur du **coefficient de déduction**, produit de trois coefficients, **déterminés dépense par dépense** (ou par catégorie homogène) :
- **assujettissement** : proportion d'utilisation de la dépense pour des opérations **dans le champ** de la TVA ;
- **taxation** : proportion des opérations **ouvrant droit à déduction** parmi les opérations dans le champ (ratio de chiffre d'affaires, calculé au niveau de l'entreprise ou par secteur) ;
- **admission** : 0 pour les dépenses exclues (véhicules de tourisme…), 1 sinon.
Chaque coefficient est **arrondi par excès** au centième ; le produit aussi.

**b) Classement des produits 2025**

| Produit | Qualification | Effet |
|---|---|---|
| Management fees 240 000 € | **Taxable** (prestations de services) | Numérateur et dénominateur du coefficient de taxation |
| Intérêts des comptes courants 28 000 € | **Exonérés** (opérations de crédit, art. 261 C-1° CGI ; pas d'option) | Dénominateur seulement. Ils ne sont pas « accessoires » : prêter aux filiales est une activité habituelle de cette holding de financement de groupe |
| Dividendes 450 000 € | **Hors champ** (détention de titres, pas une activité économique) | **Exclus** du coefficient de taxation ; pris en compte via l'**assujettissement** |
| Cession du VP 12 000 € | Cession de bien d'investissement | **Exclue** du coefficient de taxation |

**c) Dépense par dépense**

| Dépense | Assujettissement | Taxation | Admission | Déduction |
|---|---|---|---|---|
| Exclusivement liées aux management fees | 1 | 1 (affectée à une opération taxable) | 1 | **1** |
| Conseil M&A pour **céder une participation** (gestion patrimoniale, hors champ) | **0** | — | — | **0** |
| Frais généraux mixtes | 0,75 (clé de temps documentée) | 0,90 | 1 | **0,68** |
| LLD véhicule de tourisme | — | — | **0** | **0** |
| Serveur et postes (mixtes) | 0,75 | 0,90 | 1 | **0,68** |

Les honoraires de cession d'une participation sont rattachés à une opération **hors champ** (cession de titres d'une participation non animée, dans le cadre de la gestion du portefeuille) : la TVA n'est **pas déductible du tout**. L'ancien collaborateur a appliqué le coefficient général (0,75) : erreur d'**affectation**. (À distinguer des frais d'acquisition de titres d'une filiale à laquelle la holding fournira des prestations taxables, dont la TVA peut être déductible selon la jurisprudence européenne — analyse au cas par cas.)

**d) Calendrier.** En cours d'année N, on applique des coefficients **provisoires** (sur la base de N-1 ou d'estimations). Les coefficients **définitifs** sont arrêtés **au plus tard le 25 avril N+1**, et la régularisation est portée sur la déclaration déposée avant cette date (pour une CA3 mensuelle : celle de mars N+1, déposée en avril). Ici, la régularisation 2025 aurait dû figurer sur la **CA3 de mars 2026**. Elle n'a pas été faite → on la porte maintenant sur la prochaine CA3 (celle de septembre 2026, déposée en octobre), en **ligne 15 « TVA antérieurement déduite à reverser »**, avec un **intérêt de retard** (art. 1727 CGI, 0,20 % par mois), réduit en cas de régularisation spontanée (*réduction à vérifier*).

## 2. Calculs

**Coefficients définitifs 2025**

| Coefficient | Calcul | Résultat brut | Arrondi par excès |
|---|---|---|---|
| Assujettissement (frais mixtes) | Clé de temps | 0,75 | 0,75 |
| Taxation | 240 000 / (240 000 + 28 000) | 0,8955 | **0,90** |
| Admission | — | 1 | 1 |
| **Déduction** | 0,75 × 0,90 × 1 | 0,675 | **0,68** |

**TVA déductible définitive 2025 et régularisation**

| Dépense | TVA facturée | Déduite (provisoire) | Définitive | À reverser |
|---|---|---|---|---|
| Exclusives management fees | 3 200,00 | 3 200,00 | 3 200,00 | 0,00 |
| Conseil cession de participation | 4 000,00 | 3 000,00 | 0,00 | **3 000,00** |
| Frais généraux mixtes | 9 000,00 | 6 750,00 | 6 120,00 (× 0,68) | **630,00** |
| LLD véhicule de tourisme | 1 440,00 | 0,00 | 0,00 | 0,00 |
| Serveur et postes | 2 000,00 | 1 500,00 | 1 360,00 (× 0,68) | **140,00** |
| **Total** | **19 640,00** | **14 450,00** | **10 680,00** | **3 770,00** |

**Intérêt de retard (décompte indicatif)**

| Rappel | Échéance normale | Point de départ | Nombre de mois (jusqu'à octobre 2026 inclus) | Intérêt (0,20 %/mois) |
|---|---|---|---|---|
| 3 000,00 (CA3 de juin 2025, payée en juillet 2025) | juillet 2025 | 1er août 2025 | 15 | 90,00 |
| 770,00 (régularisation de la CA3 de mars 2026, avril 2026) | avril 2026 | 1er mai 2026 | 6 | 9,24 |
| **Total** | | | | **99,24** |

*Décompte à affiner selon les dates exactes de dépôt ; l'intérêt est calculé du premier jour du mois suivant l'échéance au dernier jour du mois du paiement.*

**Simulation 2026**

| | Calcul | Résultat |
|---|---|---|
| Coefficient **provisoire** 2026 (frais mixtes) | = définitif 2025 | **0,68** |
| Taxation prévisionnelle 2026 | 260 000 / (260 000 + 60 000) = 0,8125 | 0,82 |
| Assujettissement prévisionnel | clé de temps | 0,68 |
| **Déduction définitive prévisionnelle 2026** | 0,68 × 0,82 = 0,5576 | **0,56** |
| Variation pour le serveur (coefficient d'origine 0,68) | 0,68 – 0,56 = 0,12 > 0,10 | régularisation annuelle |
| Reversement en avril 2027 au titre du serveur | 2 000 × 0,12 / 5 | **48,00** |

Les frais mixtes de 2026, déduits provisoirement à 0,68, seront également régularisés (reversement de 0,12 × TVA de l'année) en avril 2027. Si l'écart avait été inférieur ou égal à 10 points, aucune régularisation annuelle n'aurait été due pour le serveur.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6226 | Honoraires | TVA non déductible – conseil cession participation 2025 | 3 000,00 | |
| 30/09/2026 | OD | 6xx | Charges externes par nature (loyer, informatique, honoraires — ventilées) | Régularisation coefficient définitif 2025 – frais mixtes | 630,00 | |
| 30/09/2026 | OD | 6xx | Charges externes (TVA non récupérable sur immobilisation – régularisation) | Régularisation coefficient définitif 2025 – serveur | 140,00 | |
| 30/09/2026 | OD | 4458 | TVA à régulariser (ligne 15 CA3) | Reversement TVA 2025 – coefficients définitifs | | 3 770,00 |
| 30/09/2026 | OD | 658 | Charges diverses de gestion courante – intérêts de retard (*subdivision selon la nomenclature 2025 du PCG*) | Intérêt de retard TVA (régularisation spontanée) | 99,24 | |
| 30/09/2026 | OD | 4458 | TVA à régulariser | Intérêt de retard à payer avec la CA3 | | 99,24 |
| 30/09/2026 | OD | 4458 | TVA à régulariser | Report sur CA3 09/2026 | 3 869,24 | |
| 30/09/2026 | OD | 44551 | TVA à décaisser | CA3 09/2026 – ligne 15 + intérêt de retard | | 3 869,24 |
| | | | | **Totaux** | **7 738,48** | **7 738,48** |

Remarques :
- Les comptes 2025 étant clos, la régularisation passe en **charges 2026**. Pour la TVA non récupérable sur le serveur, l'alternative consiste à l'ajouter au coût de l'immobilisation (et à ajuster les amortissements) ; en pratique, pour 140 €, la charge est admise (principe d'importance relative).
- Fiscalement, l'intérêt de retard afférent à une taxe déductible n'est pas une sanction : il est en principe **déductible** du résultat imposable (*à vérifier selon la doctrine en vigueur*).

## 4. Points d'attention / pièges

- **Dividendes ≠ opération exonérée** : ils sont **hors champ** ; on ne les met pas au dénominateur du coefficient de taxation. Leur effet passe par le coefficient d'**assujettissement** des frais mixtes.
- **Clé d'assujettissement** : elle doit refléter l'utilisation réelle (temps, surfaces, effectifs…), être **documentée** et cohérente d'une année sur l'autre ; un ratio de chiffre d'affaires incluant les dividendes est une approche souvent contestée.
- **Arrondis** : par excès au centième (0,8955 → 0,90 ; 0,675 → 0,68).
- **Coefficient provisoire de l'année N** = coefficient définitif de N-1 (ou estimation si changement important).
- **Régularisation d'avril** : à inscrire au planning du cabinet pour chaque client assujetti partiel (holdings, sociétés mixtes, SCI partiellement optantes).
- **Intégration fiscale** : sans incidence sur la TVA (le groupe TVA « assujetti unique » est un dispositif distinct, optionnel).

## 5. Ce qu'un senior ferait en plus

- **Note de méthode** au dossier permanent : liste des dépenses et de leur affectation (taxable / mixte / patrimoniale / exclue), clé d'assujettissement, calcul annuel des coefficients, date de régularisation.
- **Paramétrage comptable** : codes TVA distincts par catégorie (déduction 100 %, coefficient mixte, 0 %), pour sortir automatiquement les montants.
- **Conseil à Jean Delmas** : l'opération d'acquisition prévue en 2026 génère des frais importants (audit, avocats, conseil) dont la déductibilité dépend de la destination des titres : si Delta Invest **animera** la cible et lui facturera des prestations taxables, la TVA des frais d'acquisition peut être déductible (au moins partiellement) ; l'anticiper **avant** la signature des lettres de mission.
- **Option pour la taxation des intérêts** (art. 260 B CGI) : à étudier — elle augmenterait le coefficient de taxation (intérêts taxés et facturés avec TVA aux filiales, qui récupèrent cette TVA si elles sont pleinement redevables).
- **Mail à Hélène** : synthèse chiffrée (3 770 € + 99,24 €), proposition de dépôt sur la CA3 de septembre, et information du client (erreur antérieure au cabinet actuel ?).

## 6. Références

- Annexe II au CGI : art. 205 (principe), art. 206 (coefficients d'assujettissement, de taxation, d'admission, arrondis, exclusions des cessions de biens d'investissement et opérations accessoires), art. 207 (régularisations, seuil de 10 points, 1/5 et 1/20).
- CGI : art. 261 C-1° (exonération des opérations de crédit), art. 260 B (option), art. 271 (droit à déduction), art. 1727 (intérêt de retard).
- BOFiP : TVA-DED-20 (coefficient de déduction) ; TVA-DED-60 (régularisations).
- Jurisprudence européenne sur les holdings (immixtion dans la gestion des filiales et droit à déduction) — à consulter en cas d'opération d'acquisition.
