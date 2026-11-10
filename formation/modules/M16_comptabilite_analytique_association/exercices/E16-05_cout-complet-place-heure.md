# E16-05 — Combien coûte un accompagnement ? Coût complet par place et par heure
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** coût complet, charges directes, charges communes, frais de siège, coût par place, coût par personne, coût horaire, taux d'occupation, comparaison avec la dotation, note de synthèse

**Corner case :** oui — le SESSAD a 45 places autorisées mais 42 enfants accompagnés en moyenne ; et le coût de l'emploi accompagné change selon que l'on compte le siège « financé » ou le siège réel

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **FIPHFP** | Fonds pour l'insertion des personnes handicapées dans la fonction publique. Finance l'emploi des personnes handicapées dans le secteur public (l'équivalent de l'AGEFIPH pour le public). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **charges communes** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **charges directes** | Charge qui concerne un seul service. On sait tout de suite à quel service l'imputer (ex. : le matériel pédagogique du SESSAD). |
    | **Coût complet** | Ce que coûte vraiment un service. Charges directes + part des charges communes + frais de siège. |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **taux d'occupation** | Places occupées / places autorisées. Ex. : 42 enfants accompagnés pour 45 places = 93,3 %. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes et chiffres fictifs.*

!!! abstract "En clair"
    Le **coût complet** d'un service, c'est tout ce qu'il coûte vraiment : ses **charges directes** (ses salaires, ses fournitures), sa part des **charges communes** (loyer, véhicules, téléphone…) et sa part du **siège**. En le divisant par le nombre de places ou d'heures, on obtient un chiffre parlant : « une place de SESSAD coûte X € par an ». C'est ce chiffre que l'on compare à ce que le financeur verse.

## La mise en situation

Mardi 10/11/2026, 16 h. Nathalie Berthier, directrice générale, prépare un rendez-vous avec l'ARS (agence régionale de santé) et la réponse à un appel à projets du Département. Elle vous écrit :

> « Bonjour, on me demande souvent "combien coûte une place chez vous ?". Je n'ai jamais de chiffre solide. Pouvez-vous me calculer, pour le SESSAD, le SAVS et l'emploi accompagné, le coût complet 2026, le coût par place (ou par personne) et le coût par heure d'intervention, et me dire si les financements couvrent ? Une note de **10 lignes maximum**, s'il vous plaît : je la lirai entre deux réunions. »

## Les pièces

**Pièce 1 — Coûts 2026 par service (estimation de clôture ; résultats des exercices E16-02 et E16-04)**

| Service | Charges directes | Charges communes réparties | Frais de siège (taux autorisé ou plafond de la convention) |
|---|---|---|---|
| 10-SESSAD | 1 014 500,00 € | 113 874,19 € | 50 776,84 € |
| 20-SAVS | 552 300,00 € | 59 850,69 € | 27 546,78 € |
| 30-EMPLOI | 255 600,00 € | 26 666,73 € | 25 560,00 € |

Pour mémoire (E16-04) : si l'on répartissait **tout** le coût du siège, la quote-part de l'emploi accompagné serait de **54 323,40 €** au lieu de 25 560,00 €.

**Pièce 2 — Activité 2026 (tableaux de bord des chefs de service)**

| Service | Capacité | Personnes accompagnées (moyenne de l'année) | Heures d'intervention directe* | ETP |
|---|---|---|---|---|
| 10-SESSAD | 45 places | 42 enfants | 12 600 h | 14,2 |
| 20-SAVS | 60 places | 60 adultes | 7 800 h | 7,8 |
| 30-EMPLOI | 40 personnes (convention) | 40 personnes | 3 400 h | 3,6 |

\* Heures passées **auprès** de la personne, de sa famille, de l'école ou de l'employeur (hors trajets, réunions internes et écrits).

**Pièce 3 — Financements 2026**

| Service | Financeur | Montant |
|---|---|---|
| 10-SESSAD | ARS – dotation globale | 1 165 000,00 € |
| 20-SAVS | Département de la Drôme – dotation globale | 628 000,00 € |
| 30-EMPLOI | ARS 170 000,00 € + AGEFIPH 85 000,00 € + FIPHFP 25 000,00 € | 280 000,00 € |

*(On ne tient compte d'aucun autre produit dans cet exercice.)*

## Travail à faire

1. Calculez le **coût complet** 2026 de chaque service et la part (en %) des charges directes, des charges communes et des frais de siège.
2. Calculez le **coût par place et par an** (SESSAD, SAVS) et le **coût par personne accompagnée** (emploi). Pour le SESSAD, calculez aussi le coût par **enfant réellement accompagné** et le taux d'occupation.
3. Calculez le **coût par heure d'intervention directe** de chaque service.
4. Comparez avec les financements : écart en euros et en %, financement par place et par heure.
5. Emploi accompagné : recalculez le coût par personne avec le **siège réel** (quote-part de 54 323,40 €). Qu'en concluez-vous ?
6. Rédigez la **note de 10 lignes** à la directrice.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E16-05_corrige.md)
