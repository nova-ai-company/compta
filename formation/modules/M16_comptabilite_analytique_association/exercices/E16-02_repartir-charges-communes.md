# E16-02 — Répartir les charges communes avec des clés de répartition
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** charges communes, clés de répartition, m², kilomètres, ETP, charges directes, salle commune, OD analytique, part du siège, frais de siège

**Corner case :** oui — la salle commune n'appartient à personne, un véhicule « pool » sert à cinq sections, et la part du siège ne doit pas être répartie une deuxième fois

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **00-COMMUN** | Section des charges communes à répartir. Section « de passage » : on y saisit les charges partagées (loyer, téléphone…), puis on la vide vers les services avec une clé. Elle doit revenir à zéro. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **LLD** | Location longue durée. Location d'un bien (souvent un véhicule) sur plusieurs années, sans option d'achat : loyers en charge. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **Compte 614** | Charges locatives et de copropriété. |
    | **Compte 616** | Primes d'assurances. Assurance des locaux, des véhicules, responsabilité civile. Pas de TVA. |
    | **Compte 626** | Frais postaux et de télécommunications. Téléphone, internet, timbres. |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6132** | Locations immobilières. Loyer des locaux, location de salle. |
    | **Compte 6135** | Locations mobilières. Location de véhicules (LLD), de photocopieurs. |
    | **Compte 6155** | Entretien et réparations sur biens mobiliers. Réparation des véhicules, du matériel. |
    | **Compte 6156** | Maintenance. Contrats de maintenance (informatique, logiciel). |
    | **Compte 6226** | Honoraires. Expert-comptable, commissaire aux comptes, avocat. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **charges communes** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **charges directes** | Charge qui concerne un seul service. On sait tout de suite à quel service l'imputer (ex. : le matériel pédagogique du SESSAD). |
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes et chiffres fictifs.*

!!! abstract "En clair"
    Une **charge commune** profite à plusieurs services (le loyer des locaux partagés, les voitures, le téléphone…). On ne peut pas la mettre sur un seul service. On la **découpe** avec une **clé de répartition** : un critère mesurable qui suit l'usage (des m², des kilomètres, des ETP — équivalents temps plein). Le résultat : chaque service porte **sa** part, et chaque financeur paie **sa** part.

## La mise en situation

Mardi 10/11/2026. Hélène Ferrand, cheffe de mission au cabinet d'expertise comptable, vous appelle :

> « Bonjour ! Pour la clôture 2026, je voudrais qu'on vérifie les clés **avant** décembre. Pouvez-vous me préparer la répartition des charges communes de **l'année 2026** ? Prenez les montants annuels estimés : dix mois réels, plus novembre et décembre connus par les contrats. Toutes ces charges sont aujourd'hui sur la section **00-COMMUN**. L'OD analytique sera passée au 31/12/2026 avec les montants définitifs, mais la méthode, c'est maintenant qu'on la valide. »

Une heure plus tard, deux messages arrivent.

Karim Belkacem, chef de service du SESSAD :

> « Je découvre que le SESSAD paie une partie de la salle commune. Mais le soir, c'est surtout le groupe "Pairs et voix" et les réunions du SAVS qui l'utilisent ! Ce n'est pas juste. »

Une note retrouvée dans le classeur de Mme Roux, l'ancienne comptable :

> « Après la répartition, je répartissais aussi la part du siège (ses m², ses km, ses ETP) entre les services, au prorata de leurs charges. Comme ça le siège était à zéro. »

## Les pièces

**Pièce 1 — Charges communes 2026 sur la section 00-COMMUN (montants annuels estimés, TTC)**

| Rubrique | Comptes | Détail | Montant annuel |
|---|---|---|---|
| Locaux de Valence | 6132, 614, 616 | Loyer 12 × 6 200,00 = 74 400,00 ; charges locatives et ménage 12 × 1 000,00 = 12 000,00 ; assurance multirisque des locaux 4 960,00 | **91 360,00 €** |
| Véhicules | 6135, 6061, 6155, 6251 | Location longue durée (LLD) 8 × 350,00 × 12 = 33 600,00 ; carburant 15 800,00 ; entretien 2 600,00 ; péages et parkings 1 000,00 | **53 000,00 €** |
| Assurance flotte | 616 | 8 véhicules × 900,00 | **7 200,00 €** |
| Téléphonie et informatique | 626, 6156 | Téléphonie 11 700,00 ; maintenance et licences 14 600,00 ; logiciel métier (dossier de l'usager) 6 000,00 | **32 300,00 €** |
| Commissaire aux comptes et expert-comptable | 6226 | CAC 11 520,00 ; expert-comptable (révision et paie) 26 400,00 | **37 920,00 €** |
| **Total** | | | **221 780,00 €** |

**Pièce 2 — Surfaces des locaux de Valence (fiche de l'association)**

SESSAD 280 m² · SAVS 160 m² · Emploi accompagné 60 m² · Siège 90 m² · **Salle commune 30 m²** · Total **620 m²**.
Règle de la fiche : la salle commune est « répartie comme le reste ». L'habitat inclusif et le projet Pairs n'occupent pas de bureau à Valence.

**Pièce 3 — Synthèse des carnets de bord des 8 véhicules (01/01 au 31/12/2026, novembre-décembre estimés)**

| Véhicules | Affectation | Kilomètres |
|---|---|---|
| 4 véhicules | SESSAD | 72 000 km |
| 2 véhicules | SAVS | 31 000 km |
| 1 véhicule | Emploi accompagné | 15 000 km |
| 1 véhicule « pool » (partagé) | Réservé selon le planning | 9 000 km, dont : SESSAD 3 000 · SAVS 2 000 · Emploi 2 500 · Pairs 1 000 · Siège 500 |
| **8 véhicules** | | **127 000 km** |

Règle : véhicules répartis **au kilomètre** ; assurance flotte répartie **par véhicule affecté** (900,00 € par véhicule), le véhicule pool étant réparti selon ses propres kilomètres.

**Pièce 4 — ETP par section (fiche)**

Siège 2,6 · SESSAD 14,2 · SAVS 7,8 · Emploi 3,6 · Habitat 1,0 · Pairs 0,2 · **Total 29,4 ETP**. La vie associative (90-ASSO) n'a pas de salarié.

**Pièce 5 — Charges directes 2026 (estimation, hors charges communes et hors frais de siège)**

| Section | Charges directes |
|---|---|
| 10-SESSAD | 1 014 500,00 € |
| 20-SAVS | 552 300,00 € |
| 30-EMPLOI | 255 600,00 € |
| 40-HABITAT | 81 300,00 € |
| 50-PAIRS | 47 400,00 € |
| **Total** | **1 951 100,00 €** |

Règle validée par le bureau : les honoraires du CAC et de l'expert-comptable sont répartis **au prorata des charges directes** des cinq services ci-dessus. Le siège n'en prend pas (il est financé par les frais de siège), la vie associative non plus.

## Travail à faire

1. **Locaux** : calculez la surface attribuée à chaque section après redistribution de la salle commune, puis répartissez les 91 360,00 €.
2. **Véhicules** : calculez les kilomètres par section, le coût moyen du kilomètre, et répartissez les 53 000,00 €. Répartissez ensuite l'assurance flotte.
3. **Téléphonie et informatique** : répartissez les 32 300,00 € par ETP.
4. **CAC et expert-comptable** : répartissez les 37 920,00 € au prorata des charges directes.
5. Présentez le **tableau récapitulatif** (rubriques en lignes, sections en colonnes) et vérifiez que la section 00-COMMUN revient à zéro.
6. Passez l'**OD analytique** de répartition au 31/12/2026 (une ligne par rubrique et par section).
7. Que répondez-vous à Karim Belkacem sur la salle commune ?
8. Que pensez-vous de la méthode de Mme Roux sur la part du siège ? Que devient cette part ?

*Arrondissez au centime ; l'écart d'arrondi éventuel est mis sur la section qui reçoit la plus grosse part.*

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E16-02_corrige.md)
