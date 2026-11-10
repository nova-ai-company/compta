# E16-04 — Calculer et répartir les frais de siège
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★★ | **Durée estimée :** 50 min | **Thèmes :** frais de siège autorisés, ESSMS, charges brutes, quote-part des services hors ESSMS, plafond des conventions, couverture du siège, compte de liaison 181, OD analytique, ressources propres

**Corner case :** oui — la quote-part calculée pour les services hors ESSMS dépasse ce que leurs financeurs acceptent : le siège n'est pas entièrement couvert

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **AVP** | Aide à la vie partagée. Aide versée par le Département pour animer un habitat inclusif (projet de vie sociale et partagée des habitants). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **FIPHFP** | Fonds pour l'insertion des personnes handicapées dans la fonction publique. Finance l'emploi des personnes handicapées dans le secteur public (l'équivalent de l'AGEFIPH pour le public). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **Compte 181** | Compte de liaison siège / établissements. Enregistre les échanges entre le siège et chaque service quand chacun a sa propre comptabilité. |
    | **charges communes** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **Charges directes** | Charge qui concerne un seul service. On sait tout de suite à quel service l'imputer (ex. : le matériel pédagogique du SESSAD). |
    | **compte de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes, taux et chiffres fictifs.*

!!! abstract "En clair"
    Le **siège** (direction, comptabilité, ressources humaines) travaille pour tous les services, mais il n'a pas de financeur à lui. Il est payé par les services, sous forme de **frais de siège**. Pour le SESSAD et le SAVS (des ESSMS : établissements et services sociaux et médico-sociaux), l'autorité de tarification **autorise** un taux (ici 4,5 %). Pour les autres services, on utilise une **clé**, dans la limite de ce que chaque financeur accepte. La question finale est simple : **est-ce que tout le siège est payé ?**

## La mise en situation

Mardi 10/11/2026, 14 h. Nathalie Berthier, directrice générale, vous arrête dans le couloir :

> « J'ai la réunion de bureau jeudi. Odile Marchand, notre trésorière, me demande depuis des mois si le siège est vraiment financé. Pouvez-vous me calculer les frais de siège 2026 de chaque service et me dire s'il reste un trou ? Et préparez l'écriture, Hélène Ferrand la voudra pour la clôture. »

Dans le classeur de Mme Roux, vous trouvez son calcul de 2025 :

> « Frais de siège SESSAD = 4,5 % × budget total du SESSAD (1 180 000 €) = 53 100 €. »

## Les pièces

**Pièce 1 — Charges 2026 par section (estimation de clôture, après répartition des charges communes de l'exercice E16-02), hors frais de siège**

| Section | Charges directes | Charges communes réparties | Total hors frais de siège |
|---|---|---|---|
| 01-SIEGE | 142 948,61 € | 17 051,39 € | **160 000,00 €** |
| 10-SESSAD | 1 014 500,00 € | 113 874,19 € | **1 128 374,19 €** |
| 20-SAVS | 552 300,00 € | 59 850,69 € | **612 150,69 €** |
| 30-EMPLOI | 255 600,00 € | 26 666,73 € | **282 266,73 €** |
| 40-HABITAT | 81 300,00 € | 2 678,72 € | **83 978,72 €** |
| 50-PAIRS | 47 400,00 € | 1 658,28 € | **49 058,28 €** |
| 90-ASSO | 30 000,00 € | — | **30 000,00 €** |

**Pièce 2 — Règles (fiche de l'association, § 3.4)**

- Frais de siège **autorisés** pour les ESSMS (SESSAD, SAVS) : **4,5 %** des **charges brutes** du service, **hors frais de siège** (taux fictif).
- Les services non autorisés (emploi accompagné, habitat, Pairs) supportent le reste du coût du siège **au prorata de leurs charges directes**, à condition que leur financeur l'accepte.
- La vie associative (90-ASSO) ne supporte pas de frais de siège (décision du bureau).

**Pièce 3 — Ce que les conventions acceptent (extraits)**

| Service | Financeur | Clause sur les frais de structure |
|---|---|---|
| 30-EMPLOI | ARS + AGEFIPH + FIPHFP | « Frais de structure et de gestion : dans la limite de **10 %** des charges directes du dispositif. » |
| 40-HABITAT | Département (aide à la vie partagée, AVP) | « Frais de gestion : **8 %** maximum des charges directes. » |
| 50-PAIRS | Fondation Lumen + Région | « Frais de fonctionnement indirects : **10 %** maximum des dépenses directes du projet. » |

**Pièce 4 — Vie associative 2026 (estimation)**

Produits : cotisations 9 000,00 € ; dons 31 000,00 € ; événements 6 000,00 € → **46 000,00 €**. Charges : 30 000,00 €. Excédent prévu : **16 000,00 €**.

## Travail à faire

1. Qu'est-ce qui ne va pas dans le calcul de Mme Roux ? Calculez les frais de siège 2026 du SESSAD et du SAVS.
2. Calculez le coût du siège restant à financer, puis sa répartition **mécanique** entre l'emploi accompagné, l'habitat et Pairs au prorata des charges directes. Quel taux cela représente-t-il ?
3. Comparez avec les plafonds des conventions. Quel montant chaque service peut-il réellement supporter ?
4. Le siège est-il entièrement couvert ? Calculez le montant non couvert et le taux de couverture. Qui finance le reste ? Proposez des pistes.
5. Expliquez simplement les deux façons d'enregistrer les frais de siège : le **compte de liaison 181** et l'**OD analytique**. Laquelle convient à Cap Horizons 21 ?
6. Passez l'écriture de répartition des frais de siège au 31/12/2026 avec la méthode retenue.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E16-04_corrige.md)
