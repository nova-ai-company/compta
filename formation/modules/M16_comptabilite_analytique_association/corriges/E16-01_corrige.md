# Corrigé E16-01 — Codifier douze factures : compte de charge, code analytique, groupe fonctionnel

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-01](../exercices/E16-01_codifier-douze-factures.md)

!!! abstract "En clair"
    Pour chaque facture, posez-vous trois questions, toujours dans le même ordre :
    1. **Quoi ?** → le compte (la nature de la dépense).
    2. **Pour qui ?** → le code analytique (le service qui a **utilisé** la dépense, pas celui dont le nom est sur la facture).
    3. **Dans quelle case du budget ?** → le groupe fonctionnel (I exploitation courante, II personnel, III structure). Il découle du compte.

    Et une règle qui ne change jamais chez Cap Horizons 21 : **la charge, c'est le TTC**.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 2 — Pourquoi enregistrer les charges TTC ?

Les activités de l'association sont **non lucratives** et exonérées ou hors champ de TVA. Elle ne collecte pas de TVA, donc elle **ne peut pas déduire** la TVA qu'elle paie : cette TVA est un **coût définitif**, comme le prix lui-même. Elle va donc **dans la charge** (et, pour un bien immobilisé, **dans le coût de l'immobilisation**). Il n'y a **pas** de compte 44566 dans ce dossier.

> ⚠️ Erreur classique : venir d'un cabinet qui tient des sociétés commerciales et saisir « 6068 HT + 44566 TVA ». Le compte de TVA déductible gonfle, rien ne viendra jamais le solder, et les charges des services sont sous-évaluées de 20 %.

### Question 3 — Les trois pièges

**Piège 1 — La facture au nom d'une salariée (pièce 11).** Ce n'est **pas** une facture fournisseur de l'association : Léa Fontaine a payé avec sa carte personnelle et demande à être remboursée. On ne la saisit donc **pas** au crédit d'un compte 401 : c'est une **note de frais**, que l'on enregistre au crédit du compte **421** (dette envers la salariée). La dépense est acceptable parce que :
- elle est professionnelle (jeux pour des séances à l'école) et cohérente avec son poste ;
- la note est **signée** par la salariée et **validée** par son chef de service ;
- le justificatif original est joint.

Le nom de la salariée sur le ticket ne rend pas la dépense personnelle ; ce qui compte, c'est l'objet et la validation. En revanche, on lui rappellera de passer par un **bon de commande** au nom de l'association (comme la pièce 1) pour les prochains achats.

**Piège 2 — La facture de 2025 (pièce 12).** La révision a eu lieu le **15/12/2025** : la charge appartient à **l'exercice 2025**. Mme Roux l'avait bien prévue : une **FNP** de 384,00 € figure au compte 4081 au 31/12/2025. Quand la facture arrive, on **solde la FNP** : débit 4081, crédit 401. **Aucune charge en 2026, donc aucun code analytique** (le coût a déjà été réparti en 2025).

> ⚠️ Erreur classique : saisir la facture en 6155 comme une facture normale. La charge serait comptée **deux fois** (une fois en 2025 par la FNP, une fois en 2026), et le compte 4081 garderait pour toujours son solde créditeur de 384,00 €.

*Autre méthode, courante dans les cabinets* : l'**extourne** des FNP au 01/01/2026 (débit 4081, crédit 6155). Dans ce cas, on saisit la facture normalement en charge (débit 6155, crédit 401) et les deux écritures s'annulent dans le résultat 2026. Ici, Mme Roux n'extourne pas : on solde donc directement le 4081.

*Si aucune FNP n'avait été passée*, la charge serait enregistrée en 2026 (charge d'exploitation, **pas** en exceptionnel), avec un libellé « exercice 2025 », et on le signalerait à Hélène Ferrand et au commissaire aux comptes si le montant était significatif.

**Piège 3 — La facture commune adressée à un seul service (pièce 3).** L'avis d'échéance est adressé au « SESSAD » uniquement parce que le bail a été signé par le SESSAD en 2009. Mais il couvre le **plateau complet de 620 m²**, occupé par le SESSAD, le SAVS, l'emploi accompagné, le siège et la salle commune. Le coder 10-SESSAD ferait payer **tout** le loyer par l'ARS (agence régionale de santé). On le code **00-COMMUN** et on le répartira au m² (exercice E16-02).

### Les autres pièces, une par une

- **Pièce 1** : fournitures pédagogiques commandées par le SESSAD → 6068, 10-SESSAD. Deux taux de TVA (20 % et 5,5 % sur les livres) : sans importance pour nous, on prend le **TTC total**.
- **Pièce 2** : le relevé détaille les véhicules, et on pourrait être tenté d'imputer chaque ligne au service du véhicule. Mais la règle de la maison est claire : **tous** les frais de véhicules sont répartis **au kilomètre**. → 6061, 00-COMMUN.
- **Pièce 4** : assurance de la Maison partagée → 616, 40-HABITAT. Elle couvre 2 mois de 2026 et 10 mois de 2027 (voir question 5).
- **Pièce 5** : le CAC (commissaire aux comptes) certifie les comptes de **toute** l'association → 6226, 00-COMMUN (clé « charges directes » de la fiche).
- **Pièce 6** : un ordinateur coûte 790,00 × 1,20 = **948,00 € TTC** > 500 € → **immobilisation** (2183), au **TTC**, car la TVA non récupérable fait partie du coût. Fournisseur d'immobilisations : compte **404**. Les souris (19,90 × 1,20 = 23,88 € TTC l'unité) restent en **charge** (6063). Une seule facture, deux traitements.
- **Pièce 7** : sortie éducative du SAVS (apprendre à gérer un budget au restaurant) → 6288, 20-SAVS. Ce n'est **pas** une « réception » : c'est une activité avec les personnes accompagnées.
- **Pièce 8** : une seule facture, mais **trois stagiaires de trois services**. Pas besoin de clé : on impute **au réel**, 420,00 € par stagiaire, sur le service de chacun.
- **Pièce 9** : location de salle pour le projet « Pairs et voix » → 6132, 50-PAIRS. Le projet est financé par une **subvention affectée** : gardez une copie de la facture pour le compte rendu financier à la Fondation Lumen.
- **Pièce 10** : un seul compte opérateur pour toute l'association → 626, 00-COMMUN (clé ETP — équivalents temps plein).

## 2. Calculs (détaillés, chaque montant justifié)

### Question 1 — Tableau de codification

| Pièce | Compte | Montant TTC | Code analytique | Groupe | Remarque |
|---|---|---|---|---|---|
| 1 Éveil & Apprendre | 6068 | 403,52 € | 10-SESSAD | I | 344,00 HT + 56,00 + 3,52 de TVA, tout en charge |
| 2 Carbu'Pro | 6061 | 1 248,00 € | 00-COMMUN | I | À répartir au km, ne pas imputer véhicule par véhicule |
| 3 SCI Les Terrasses (loyer) | 6132 | 6 200,00 € | 00-COMMUN | III | **Piège** : adressée au SESSAD, mais couvre les 620 m² → clé m² |
| 3 SCI Les Terrasses (charges) | 614 | 1 000,00 € | 00-COMMUN | III | Idem |
| 4 Mutuelle Alpine | 616 | 1 140,00 € | 40-HABITAT | III *(pour info, hors ESSMS)* | Période 01/11/2026–31/10/2027 → CCA de 950,00 € au 31/12/2026 |
| 5 Audit Rhodanien | 6226 | 5 760,00 € | 00-COMMUN | III | Certification de toute l'association → clé charges directes |
| 6 Rhône Bureautique (ordinateurs) | 2183 | 1 896,00 € | 20-SAVS | — | 948,00 € TTC l'unité > 500 € → immobilisation (amortissement en groupe III) |
| 6 Rhône Bureautique (souris) | 6063 | 47,76 € | 20-SAVS | I | 23,88 € TTC l'unité → charge |
| 7 La Table du Parc | 6288 | 148,00 € | 20-SAVS | I | Sortie éducative, pas une réception |
| 8 IFHRA (L. Fontaine) | 6185 | 420,00 € | 10-SESSAD | II | Imputation au réel par stagiaire |
| 8 IFHRA (M. Rivière) | 6185 | 420,00 € | 20-SAVS | II | Idem |
| 8 IFHRA (I. Moulin) | 6185 | 420,00 € | 30-EMPLOI | II *(pour info, hors ESSMS)* | Idem |
| 9 Espace Rencontres | 6132 | 225,00 € | 50-PAIRS | III *(pour info, hors ESSMS)* | Pièce à garder pour le compte rendu de la subvention |
| 10 Teleo Pro | 626 | 974,88 € | 00-COMMUN | I | Compte unique → clé ETP |
| 11 La Boîte à Jeux | 6068 | 86,40 € | 10-SESSAD | I | **Piège** : note de frais → crédit 421, pas 401 |
| 12 Rhône Auto Services | 4081 | 384,00 € | — | — | **Piège** : charge 2025 déjà prévue en FNP → on solde la FNP |

**Contrôles de calcul :**
- Pièce 1 : 192,00 + 88,00 = 280,00 × 20 % = 56,00 ; 64,00 × 5,5 % = 3,52 ; 344,00 + 56,00 + 3,52 = **403,52 €** ✓.
- Pièce 6 : 1 580,00 × 1,20 = **1 896,00 €** ; 39,80 × 1,20 = **47,76 €** ; 1 896,00 + 47,76 = 1 943,76 € ✓.
- Pièce 8 : 3 × 420,00 = 1 260,00 € ✓.
- Total du tableau (hors pièce 12) : **21 723,56 − 384,00 − 950,00 = 20 389,56 €** de dépenses 2026 codifiées, dont **15 182,88 €** sur 00-COMMUN (1 248,00 + 6 200,00 + 1 000,00 + 5 760,00 + 974,88) — soit près des trois quarts (74,5 %) : la répartition des charges communes (E16-02) n'est pas un détail.

### Question 5 — Charge constatée d'avance sur l'assurance

Période couverte : 12 mois, dont **2 mois en 2026** (novembre, décembre) et **10 mois en 2027**.
Part 2027 : 1 140,00 × 10 / 12 = **950,00 €** → charge constatée d'avance (CCA) au 31/12/2026, sur le même code analytique 40-HABITAT.
Charge 2026 restante : 1 140,00 − 950,00 = **190,00 €**.

### Question 6 — Double signature (paiement > 1 500 €)

| Pièce | Montant à payer | Double signature ? |
|---|---|---|
| 3 Loyer de novembre | 7 200,00 € | **Oui** |
| 5 Audit Rhodanien | 5 760,00 € | **Oui** |
| 6 Rhône Bureautique | 1 943,76 € | **Oui** |
| Toutes les autres | ≤ 1 500 € | Non (signature de la directrice) |

Le prélèvement de l'assurance (1 140,00 €) et celui de Teleo Pro (974,88 €) sont sous le seuil ; mais un prélèvement se **contrôle** quand même à réception du relevé.

## 3. Écritures comptables

### Question 4 — Saisie des pièces (et écriture de clôture de la question 5)

| Date | Journal | Compte | Intitulé du compte | Libellé | Code analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 15/10/2026 | HA | 6068 | Autres fournitures (matériel éducatif) | Éveil & Apprendre EA-26-1187 – kits et livres | 10-SESSAD | 403,52 | |
| 15/10/2026 | HA | 401 | Fournisseurs – Éveil & Apprendre | Éveil & Apprendre EA-26-1187 | | | 403,52 |
| 31/10/2026 | HA | 6061 | Fournitures non stockables (carburant) | Carbu'Pro relevé 10/2026 | 00-COMMUN | 1 248,00 | |
| 31/10/2026 | HA | 401 | Fournisseurs – Carbu'Pro Services | Carbu'Pro relevé 10/2026 | | | 1 248,00 |
| 01/11/2026 | HA | 6132 | Locations immobilières | SCI Terrasses du Rhône – loyer 11/2026 | 00-COMMUN | 6 200,00 | |
| 01/11/2026 | HA | 614 | Charges locatives | SCI Terrasses du Rhône – provision charges 11/2026 | 00-COMMUN | 1 000,00 | |
| 01/11/2026 | HA | 401 | Fournisseurs – SCI Les Terrasses du Rhône | SCI Terrasses du Rhône – échéance 11/2026 | | | 7 200,00 |
| 20/10/2026 | HA | 616 | Primes d'assurance | Mutuelle Alpine – Maison partagée 11/2026–10/2027 | 40-HABITAT | 1 140,00 | |
| 20/10/2026 | HA | 401 | Fournisseurs – Mutuelle Alpine des Associations | Mutuelle Alpine – Maison partagée | | | 1 140,00 |
| 30/10/2026 | HA | 6226 | Honoraires | Audit Rhodanien AR-2026-317 – acompte 1/2 CAC 2026 | 00-COMMUN | 5 760,00 | |
| 30/10/2026 | HA | 401 | Fournisseurs – Audit Rhodanien | Audit Rhodanien AR-2026-317 | | | 5 760,00 |
| 28/10/2026 | HA | 2183 | Matériel de bureau et informatique | Rhône Bureautique RB-77812 – 2 portables SAVS | 20-SAVS | 1 896,00 | |
| 28/10/2026 | HA | 6063 | Fournitures de petit équipement | Rhône Bureautique RB-77812 – 2 souris | 20-SAVS | 47,76 | |
| 28/10/2026 | HA | 404 | Fournisseurs d'immobilisations – Rhône Bureautique | Rhône Bureautique RB-77812 | | | 1 943,76 |
| 17/10/2026 | HA | 6288 | Activités et sorties des personnes accompagnées | La Table du Parc 2026-1042 – sortie SAVS | 20-SAVS | 148,00 | |
| 17/10/2026 | HA | 401 | Fournisseurs – La Table du Parc | La Table du Parc 2026-1042 | | | 148,00 |
| 23/10/2026 | HA | 6185 | Frais de formation du personnel | IFHRA F-26-0904 – L. Fontaine | 10-SESSAD | 420,00 | |
| 23/10/2026 | HA | 6185 | Frais de formation du personnel | IFHRA F-26-0904 – M. Rivière | 20-SAVS | 420,00 | |
| 23/10/2026 | HA | 6185 | Frais de formation du personnel | IFHRA F-26-0904 – I. Moulin | 30-EMPLOI | 420,00 | |
| 23/10/2026 | HA | 401 | Fournisseurs – IFHRA | IFHRA F-26-0904 | | | 1 260,00 |
| 05/11/2026 | HA | 6132 | Locations immobilières | Espace Rencontres 26-118 – salle Pairs et voix | 50-PAIRS | 225,00 | |
| 05/11/2026 | HA | 401 | Fournisseurs – Espace Rencontres du Plateau | Espace Rencontres 26-118 | | | 225,00 |
| 31/10/2026 | HA | 626 | Frais postaux et de télécommunications | Teleo Pro TP-1026-55841 – 10/2026 | 00-COMMUN | 974,88 | |
| 31/10/2026 | HA | 401 | Fournisseurs – Teleo Pro | Teleo Pro TP-1026-55841 | | | 974,88 |
| 31/10/2026 | OD | 6068 | Autres fournitures (matériel éducatif) | NDF 10/2026 L. Fontaine – jeux école Jean-Moulin | 10-SESSAD | 86,40 | |
| 31/10/2026 | OD | 421 | Personnel – notes de frais (L. Fontaine) | NDF 10/2026 L. Fontaine | | | 86,40 |
| 03/11/2026 | HA | 4081 | Fournisseurs – factures non parvenues | Rhône Auto RAS-11-0093 – solde FNP 2025 | | 384,00 | |
| 03/11/2026 | HA | 401 | Fournisseurs – Rhône Auto Services | Rhône Auto RAS-11-0093 (révision 15/12/2025) | | | 384,00 |
| 31/12/2026 | OD | 486 | Charges constatées d'avance | CCA assurance Maison partagée 01–10/2027 (10/12) | | 950,00 | |
| 31/12/2026 | OD | 616 | Primes d'assurance | CCA assurance Maison partagée 01–10/2027 (10/12) | 40-HABITAT | | 950,00 |
| | | | | **Totaux** | | **21 723,56** | **21 723,56** |

**Pourquoi ces sens ?**
- Une facture fournisseur crée une **dette** (401 ou 404 au **crédit**) et une **charge** ou une **immobilisation** au **débit**.
- La note de frais crée une dette envers la **salariée** (421 au crédit).
- La FNP de 2025 était une dette **estimée** (4081 au crédit en 2025). La vraie facture arrive : on remplace la dette estimée par la dette réelle (4081 au débit, 401 au crédit).
- La CCA retire de 2026 une charge qui concerne 2027 (616 au crédit) ; elle sera « extournée » (passée en sens inverse) le 01/01/2027.

Rappel : l'écriture de CCA du 31/12 se passe **à la clôture**, pas aujourd'hui. Notez-la dans votre dossier de clôture.

## 4. Points d'attention / pièges

- **TVA** : aucun compte 44566 dans ce dossier. Toujours le TTC.
- **Le nom sur la facture ne donne pas le code analytique.** C'est **l'utilisation** qui compte (pièce 3 adressée au SESSAD, mais commune).
- **Une facture peut porter plusieurs codes** (pièce 8) ou plusieurs comptes (pièce 6). Faites une ligne par morceau.
- **Immobilisation** : on compare le seuil à la **valeur unitaire** (948,00 € par ordinateur), pas au total de la facture. Et on immobilise au **TTC**.
- **Le groupe fonctionnel** ne sert au budget que pour les **ESSMS** (SESSAD et SAVS). Pour l'emploi accompagné, l'habitat et Pairs, on suit les rubriques du budget de la **convention** ou du **dossier de subvention**. Le noter quand même ne coûte rien et facilite les tableaux.
- **Facture d'un exercice antérieur** : toujours chercher d'abord dans le 4081 avant de saisir en charge.
- **Validation** : toutes les pièces ont le bon à payer de la directrice. Une pièce sans validation ne se paie pas, même « urgente ».

## 5. Ce qu'un senior ferait en plus

- **Contrôler le seuil des 500 €** pour les ordinateurs avec le **plan d'investissement** du SAVS : pour un ESSMS, les amortissements entrent dans le groupe III et le Département regarde si l'achat était prévu au budget.
- **Ouvrir une fiche d'immobilisation** (date de mise en service, durée d'amortissement, code analytique 20-SAVS).
- **Prévenir Mme Fontaine** par un message simple : « Bonjour Léa, votre note de frais de 86,40 € est validée et sera remboursée avec les notes du mois. Pour les prochains achats, pouvez-vous passer par un bon de commande au nom de l'association ? Cela évite d'avancer de l'argent. »
- **Prévenir Rhône Auto Services** : demander que la facture soit émise **dans le mois** de l'intervention, pour que la clôture ne repose pas sur des estimations.
- **Vérifier la formation** (pièce 8) : est-elle dans le **plan de développement des compétences** ? Une prise en charge par l'OPCO (opérateur de compétences) est-elle possible ? Si oui, le remboursement viendra **en produit**, pas en diminution du compte 6185.
- **Tenir un tableau de suivi de la section 00-COMMUN** : elle doit revenir à zéro à chaque répartition. Un solde qui traîne = une répartition oubliée.

## 6. Références

- PCG (règlement ANC n° 2014-03 modifié) : comptes 2183, 401, 404, 4081, 421, 486, 60, 61, 62 ; principe d'indépendance des exercices (charges constatées d'avance, factures non parvenues).
- Règlement ANC n° 2018-06 (comptes annuels des associations).
- Plan comptable des ESSMS et cadre budgétaire du Code de l'action sociale et des familles (groupes fonctionnels) — *numéros de subdivision à vérifier sur le plan de comptes de l'association*.
- CGI : exonération de TVA de la formation professionnelle continue (article 261 du CGI) ; règles d'exonération des organismes sans but lucratif — *à vérifier selon la situation*.
