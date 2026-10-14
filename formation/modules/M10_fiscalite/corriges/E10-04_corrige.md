# Corrigé E10-04 — La CFE de première année de Studio Pixel

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-04](../exercices/E10-04_CFE-premiere-annee-studio-pixel.md)

## 1. Analyse

Le calendrier de la CFE d'une entreprise créée en cours d'année (art. 1478 II CGI) :

| Année | Base | Particularité |
|---|---|---|
| 2025 (année de création) | — | **Pas d'imposition** (exonération de l'année de création) |
| 2026 (1re année d'imposition) | Biens dont l'entreprise dispose au **31/12/2025** | **Base réduite de moitié** |
| 2027 (2e année) | Biens au 31/12/2025 | Base pleine |
| 2028 et suivantes | Biens utilisés en N-2 | Régime de droit commun |

La déclaration 1447-C a bien été déposée avant le 31/12/2025 avec la demande de réduction. L'avis applique une base de 5 840 € **sans** la réduction de moitié : c'est une **erreur de l'administration**, à corriger par une **réclamation**.

## 2. Calculs

**1) 2025** : exonération de l'année de création → rien à payer, **aucun rappel** à craindre.

**2) CFE 2026 correcte**

| Élément | Calcul | Montant |
|---|---|---|
| Valeur locative au 31/12/2025 | | 5 840,00 € |
| Réduction création (50 %) | 5 840 × 50 % | – 2 920,00 € |
| **Base nette** | | **2 920,00 €** |
| Base minimum | 1 165 € < 2 920 € | ne s'applique pas |
| Cotisation | 2 920 × 29,48 % = 860,82 | **861 €** |
| Taxe additionnelle CCI | 2 920 × 0,85 % = 24,82 | **25 €** |
| Frais de gestion | (861 + 25) × 3 % = 26,58 | **27 €** |
| **Total dû** | | **913 €** |

Montant réclamé : 1 825 – 913 = **912 €**.

**4) CFE 2027 (estimation)** : base pleine 5 840 € → cotisation 1 722 € + CCI 50 € + frais 53 € = **1 825 €** (avant revalorisation des valeurs locatives et variation des taux). CFE 2026 (913 €) < 3 000 € → **pas d'acompte au 15/06/2027**. Paiement au 15/12/2027 (ou prélèvement mensuel sur option).

**3) Démarche**

- **Réclamation contentieuse** (art. L. 190 LPF) depuis la messagerie sécurisée de l'espace professionnel : « Demande de dégrèvement — application de la réduction de base de l'art. 1478 II CGI, déclaration 1447-C déposée le 14/12/2025 (copie jointe) ».
- **Délai** : pour les impôts locaux, jusqu'au 31/12 de l'année suivant celle de la mise en recouvrement (soit le 31/12/2027 — *délai à vérifier*). Mais on réclame **tout de suite**.
- **Paiement** : soit payer l'intégralité au 15/12/2026 puis obtenir le remboursement, soit demander le **sursis de paiement** dans la réclamation (sans garantie en dessous d'un certain montant — *seuil à vérifier*) et payer 913 €. Sans sursis expressément demandé, un paiement partiel entraîne la **majoration de 10 %** sur le solde impayé.
- Choix retenu ici (montant faible, trésorerie suffisante) : **paiement intégral** le 15/12/2026 et réclamation immédiate.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/12/2026 | BQ | 63511 | Cotisation foncière des entreprises (subdivision selon nomenclature 2025) | CFE 2026 — avis du 31/10/2026 | 1 825,00 | |
| 15/12/2026 | BQ | 512000 | Banque | CFE 2026 — avis du 31/10/2026 | | 1 825,00 |
| 31/12/2026 | OD | 4487 | État — produits à recevoir | Dégrèvement CFE 2026 demandé (art. 1478 II CGI) | 912,00 | |
| 31/12/2026 | OD | 63511 | Cotisation foncière des entreprises | Dégrèvement CFE 2026 demandé (art. 1478 II CGI) | | 912,00 |
| | | | | **Totaux** | **2 737,00** | **2 737,00** |

- Charge nette 2026 : 1 825 – 912 = **913 €**, déductible.
- Le dégrèvement est porté **en diminution de la charge** (plus de compte de transfert de charges depuis le règlement ANC 2022-06). On le comptabilise en produit à recevoir parce que le droit est certain (texte clair, déclaration déposée dans les délais) ; si le dossier était incertain, on attendrait la décision.
- Au remboursement : 512 / 4487 pour 912 €.

## 4. Points d'attention / pièges

- Croire que la CFE est due l'année de création : **non**, mais il faut déposer la **1447-C** avant le 31/12 de l'année de création. Sans déclaration, la réduction de moitié peut être perdue.
- La CFE **ne porte plus sur les équipements** (drone, ordinateurs) : seulement les biens passibles de taxe foncière (le local).
- Base minimum : vérifier la tranche de CA et la délibération locale ; exonération de la cotisation minimum si CA ≤ 5 000 €.
- L'avis ne s'envoie plus par la poste : il faut que le client (ou le cabinet mandaté) **consulte l'espace professionnel** début novembre.
- Pas de charge à payer pour la CFE 2027 au 31/12/2026 : elle se rattache à 2027.

## 5. Ce qu'un senior ferait en plus

- **Mail type à Léo** :

> « Bonjour Léo, rien n'est dû pour 2025 : l'année de création est exonérée. Pour 2026, l'administration a oublié la réduction de moitié prévue la première année : le bon montant est 913 € et non 1 825 €. Je vous propose de payer l'avis le 15 décembre pour éviter toute majoration ; nous déposons aujourd'hui la réclamation et le trop-payé de 912 € vous sera remboursé. Pour 2027, prévoyez environ 1 825 € (base pleine). Bien à vous. »

- Ajouter au **calendrier fiscal** du client : consultation de l'avis CFE début novembre, paiement 15/12 ; envisager la **mensualisation**.
- Archiver : 1447-C, avis, accusé de réception de la réclamation, décision de dégrèvement.
- Vérifier, l'an prochain, l'éligibilité au **plafonnement en fonction de la valeur ajoutée** (peu probable ici).

## 6. Références

- CGI : art. 1447 (champ de la CFE), art. 1467 (base), art. 1478 II (création : exonération l'année de création, réduction de moitié la première année d'imposition), art. 1647 D (cotisation minimum), art. 1679 quinquies (paiement, acompte), art. 1730 (majoration de 10 %).
- LPF : art. L. 190 (réclamations), R. 196-2 (délai de réclamation pour les impôts locaux), L. 277 (sursis de paiement).
- PCG : comptes 63511, 4487, 512.
