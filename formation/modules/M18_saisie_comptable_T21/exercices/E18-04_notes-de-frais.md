# E18-04 — Quatre notes de frais : contrôler, saisir, rembourser

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **CESF** | Conseiller (ou conseillère) en économie sociale et familiale. Travailleur social qui aide les personnes à gérer leur budget, leur logement, leur vie quotidienne. Métier fréquent dans un SAVS. |
    | **CV** | Chevaux fiscaux (puissance fiscale). Puissance administrative d'une voiture, inscrite sur la carte grise. Le barème kilométrique dépend du nombre de CV. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIRET** | Numéro d'établissement (14 chiffres). SIREN + 5 chiffres (NIC) qui identifient un établissement précis (un magasin, une usine). |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **Compte 467** | Autres comptes débiteurs ou créditeurs. Compte de tiers « divers » (ex. : frais à rembourser à un salarié, subvention à reverser). |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6251000** | Voyages et déplacements (plan T21). Indemnités kilométriques, train, péages, parkings (notes de frais). |
    | **Compte 6256000** | Missions (plan T21). Repas et hébergement en mission. |
    | **Compte 6256700** | Missions - Journées Fédérales (plan T21). Déplacements pour les journées fédérales. |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **habitat inclusif** | Logement partagé en milieu ordinaire. Des personnes handicapées vivent ensemble chez elles, avec un projet de vie partagé animé par l'association. |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 15 | **Thèmes :** notes de frais (NDF), comptes de tiers SA (centralisés en 4248000), journal des achats, indemnités kilométriques et barème, forfait repas, péages, parkings, train, hôtel, comptes 6251000 / 6256000 / 6256700 / 6062400, frais partagés entre deux structures, dépense personnelle, validation des frais de la directrice, paiement en banque et lettrage

**Corner case :** oui — un salarié travaille pour deux structures et a tout mis sur une seule note ; la directrice a rempli sa propre note, avec une dépense personnelle, et personne ne l'a visée.

> *Cadre de formation : association, personnes, montants et documents fictifs. Le schéma d'écriture des notes de frais (compte SA crédité, 6251 et 60624 débités) est celui du document interne « Les journaux comptables chez Trisomie 21 France ».*

!!! abstract "En clair"
    Une **note de frais** (NDF) est le formulaire par lequel un salarié demande le remboursement de ce qu'il a payé de sa poche pour l'association : kilomètres faits avec sa voiture, parking, train, repas en déplacement, petites fournitures. Chez Trisomie 21 France, la note se saisit au **journal des achats**, comme une facture : le salarié est un « fournisseur » d'un genre particulier, avec un compte de tiers **SA** (par exemple **SADURAND** pour Nathalie Durand). Puis on le rembourse par virement, au journal de **banque**.

## La mise en situation

Lundi 16 novembre 2026. Les notes de frais d'octobre et une note de début novembre sont dans la bannette « NDF ». Elles seront remboursées avec la **campagne de virements du 20/11/2026**.

**Règles internes de Cap Horizons 21 pour les frais** (note de la directrice du 02/01/2026, hypothèses de l'exercice)

1. **Indemnités kilométriques** (véhicule personnel) : barème fiscal, tranche « jusqu'à 5 000 km par an ». On retient (*valeurs à vérifier chaque année*) :

    | Puissance fiscale | 3 CV | 4 CV | 5 CV | 6 CV | 7 CV et plus |
    |---|---|---|---|---|---|
    | € par km | 0,529 | 0,606 | 0,636 | 0,665 | 0,697 |

    Chaque note est accompagnée d'un **tableau des trajets** (date, trajet, motif, km). Les montants sont arrondis au centime **par ligne**.
2. **Repas en déplacement** : **forfait de 19,40 € par repas** (*valeur à vérifier chaque année*, montant conventionnel retenu par l'association) quand le salarié est en déplacement à l'heure du repas, selon le planning. **Pas de forfait si le repas est fourni** (par l'association ou par l'organisateur).
3. **Péages, parkings, train, transports en commun, hôtel** : au réel, **sur justificatif**.
4. **Petites fournitures** achetées pour le service : remboursées sur ticket, si l'achat a été autorisé par le chef de service.
5. **Dépenses personnelles** : jamais remboursées.
6. **Visa** : chaque note est signée par le salarié et **visée par son supérieur** : le chef de service pour les salariés, la directrice pour les chefs de service. **Personne ne vise sa propre note.**
7. **Imputation** : la structure et le code analytique sont ceux du **service pour lequel le déplacement a été fait**.
8. **Comptes** (plan T21) : 6251000 Voyages et déplacements (kilomètres, péages, parkings, train, métro) ; 6256000 Missions (repas, hôtel) ; 6062400 Fournitures administratives. Le plan T21 contient aussi un compte **6256700 Missions – Journées fédérales**.

## Les pièces

### Note n° 1 — Nathalie Durand, éducatrice spécialisée, SESSAD — véhicule personnel 5 CV

| Ligne | Détail | Justificatif | Demandé |
|---|---|---|---|
| 1 | Kilomètres d'octobre : domiciles des familles et écoles | Tableau des trajets signé | 286 km |
| 2 | Stylos et carnets pour le bureau du SESSAD, Papeterie du Centre, 14/10/2026 | Ticket de caisse | 23,70 € |

*Signée par N. Durand le 31/10/2026. Visa : « K. Belkacem – 03/11/2026 – achat autorisé ».*

### Note n° 2 — Thomas Girard, éducateur spécialisé, SESSAD — véhicule personnel 5 CV

| Ligne | Détail | Justificatif | Demandé |
|---|---|---|---|
| 1 | Kilomètres d'octobre : écoles et domiciles des familles | Tableau des trajets signé | 412 km |
| 2 | Parkings : hôpital de Valence 07/10 (3,50 €), centre-ville 21/10 (4,20 €) | 2 tickets | 7,70 € |
| 3 | Forfaits repas : 06/10, 13/10, 15/10, 20/10, 22/10, 27/10 | Planning | 6 forfaits |

*Signée le 31/10/2026. Visa : « K. Belkacem – 03/11/2026 ».*
*Planning du SESSAD du 22/10/2026 : « T. Girard – réunion de synthèse au SESSAD, 9 h – 16 h, repas pris en commun, offert par le service ». Les cinq autres jours : visites à l'extérieur sur le temps de midi.*

### Note n° 3 — Rachid Haddad, conseiller en économie sociale et familiale (CESF), SAVS et habitat inclusif — véhicule personnel 6 CV

Rachid travaille pour le **SAVS** (structure SAV) et anime l'**habitat inclusif** « La Maison partagée » (structure ASS, code analytique 40-HABITAT). Il a rempli **une seule note**, avec la mention « Service : SAVS » en haut.

| Ligne | Détail | Justificatif | Demandé |
|---|---|---|---|
| 1 | Kilomètres d'octobre | Tableau des trajets signé : **196 km** visites à domicile SAVS ; **90 km** courses et animation à La Maison partagée | 286 km |
| 2 | Péage A7 Valence – Montélimar, 15/10 (rendez-vous d'une personne accompagnée par le SAVS) | Ticket | 4,60 € |
| 3 | Forfaits repas : 08/10 et 15/10 (SAVS), 21/10 (Maison partagée) | Planning | 3 forfaits |

*Signée le 31/10/2026. Visa : « S. Laurent – 04/11/2026 ».*

### Note n° 4 — Nathalie Berthier, directrice, siège — véhicule personnel 6 CV

Déplacement aux **journées fédérales de Trisomie 21 France**, à Paris, les **05 et 06/11/2026**.

| Ligne | Détail | Justificatif | Demandé |
|---|---|---|---|
| 1 | Kilomètres : siège – gare de Valence TGV, aller-retour | Tableau | 22 km |
| 2 | Parking de la gare de Valence TGV, 05 au 06/11 | Ticket | 24,00 € |
| 3 | Train Valence TGV – Paris aller-retour | E-billet | 148,00 € |
| 4 | Métro, 4 tickets | Reçu de l'application | 10,00 € |
| 5 | Hôtel, nuit du 05/11 | Facture de l'hôtel (ci-dessous) | 164,75 € |
| 6 | Forfaits repas : dîner du 05/11, déjeuner du 06/11 | Programme des journées | 2 forfaits |

*Signée par N. Berthier le 09/11/2026. Case « Visa du supérieur » : **vide**.*

```text
HÔTEL DU CANAL ** – 18 quai de Jemmapes 75010 Paris
SIRET 998 671 904 00015 (fictif)

FACTURE N° H-26-11-0412               Date : 06/11/2026
Client : Mme Nathalie Berthier – Association Cap Horizons 21
Séjour : 1 nuit, du 05/11/2026 au 06/11/2026, chambre 214

Chambre single, 1 nuit                                     129,00
Petit-déjeuner                                              14,00
Taxe de séjour                                               3,25
Bar – 05/11 22 h 40                                         18,50
                                                          -------
TOTAL TTC                                                  164,75 €
Réglé par carte bancaire personnelle le 06/11/2026.
```

*Programme des journées fédérales : « 05/11 : 14 h – 18 h ateliers ; soirée libre. 06/11 : 9 h – 16 h plénière ; **déjeuner offert par la Fédération** ».*

## Travail à faire

1. Pour chaque note, ligne par ligne : **acceptée**, **refusée** ou **en attente** ? Justifiez.
2. Calculez le montant à rembourser à chaque salarié, en détaillant le calcul des indemnités kilométriques.
3. Note de Rachid Haddad : dans quelle(s) structure(s) la saisissez-vous ? Proposez la solution la plus simple et expliquez pourquoi une saisie de tout au SAVS serait une erreur.
4. Note de la directrice : qui doit la viser ? Que faites-vous en attendant ? Quel compte de charge choisissez-vous pour l'hôtel et le repas ?
5. Passez les écritures : saisie des notes au journal des achats (AC), avec le compte de tiers SA, puis remboursement au journal de banque de la structure. Vérifiez l'équilibre.
6. Expliquez le **lettrage** du compte SADURAND, et ce que signifierait un solde non lettré sur un compte SA à la fin du mois.
7. En E17-05, les frais étaient enregistrés dans un compte 467 par salarié, en OD. Pourquoi la méthode est-elle différente ici ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-04_corrige.md)
