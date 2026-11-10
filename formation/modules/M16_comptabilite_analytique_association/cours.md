# M16 — Comptabilité analytique et suivi budgétaire en association médico-sociale

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **12156** | Cerfa n° 12156 — demande de subvention. Le formulaire officiel pour demander une subvention à l'État, une collectivité ou un organisme public. Il contient le budget prévisionnel du projet. |
    | **15059** | Cerfa n° 15059 — compte rendu financier. Le formulaire pour rendre compte de l'utilisation d'une subvention : budget prévu, dépenses réelles, écarts expliqués. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **98-COMMUN** | Section des charges communes à répartir. Même rôle que 00-COMMUN : section de passage vidée chaque mois vers les services. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **Cerfa** | Formulaire administratif officiel. Formulaire numéroté de l'administration (ex. : Cerfa 12156 pour demander une subvention). |
    | **ERRD** | État réalisé des recettes et des dépenses. Le compte rendu de l'EPRD après la clôture : réalisé, écarts, proposition d'affectation du résultat. Dépôt en général au 30 avril N+1 (à vérifier). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **FIPHFP** | Fonds pour l'insertion des personnes handicapées dans la fonction publique. Finance l'emploi des personnes handicapées dans le secteur public (l'équivalent de l'AGEFIPH pour le public). |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **OPCO** | Opérateur de compétences. Organisme qui finance la formation professionnelle des salariés de la branche. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **QCM** | Questionnaire à choix multiples. Test avec plusieurs réponses proposées. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 181** | Compte de liaison siège / établissements. Enregistre les échanges entre le siège et chaque service quand chacun a sa propre comptabilité. |
    | **Compte 401** | Fournisseurs. Ce que l'association doit à ses fournisseurs (factures reçues, pas encore payées). |
    | **Compte 408** | Fournisseurs. Factures non parvenues (FNP) : charge de l'année dont la facture n'est pas encore arrivée. |
    | **Compte 411** | Clients / usagers. Ce que l'on doit à l'association. |
    | **Compte 616** | Primes d'assurances. Assurance des locaux, des véhicules, responsabilité civile. Pas de TVA. |
    | **Compte 626** | Frais postaux et de télécommunications. Téléphone, internet, timbres. |
    | **Compte 689** | Reports en fonds dédiés. On « met de côté » à la clôture la part d'une subvention affectée non encore dépensée. |
    | **Compte 2183** | Matériel de bureau et informatique. Ordinateurs, imprimantes : un bien durable, amorti sur plusieurs années. |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6064** | Fournitures administratives. Papier, stylos, cartouches. |
    | **Compte 6068** | Autres matières et fournitures. Matériel pédagogique, jeux, fournitures d'activités. |
    | **Compte 6132** | Locations immobilières. Loyer des locaux, location de salle. |
    | **Compte 6211** | Personnel intérimaire. Remplacement d'un salarié absent par une agence d'intérim (groupe II). |
    | **Compte 6226** | Honoraires. Expert-comptable, commissaire aux comptes, avocat. |
    | **Compte 6811** | Dotations aux amortissements. L'usure annuelle des biens durables (véhicules, ordinateurs). |
    | **Compte 44566** | TVA déductible sur autres biens et services. Sans objet pour l'association : chez elle, la TVA est une charge. |
    | **charge commune** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **charge constatée d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **charge non opposable** | Dépense refusée par le financeur. Le financeur estime qu'elle ne relève pas du service (ex. : une amende) : elle reste à la charge de l'association. |
    | **Charges directes** | Charge qui concerne un seul service. On sait tout de suite à quel service l'imputer (ex. : le matériel pédagogique du SESSAD). |
    | **Clé de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **Code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **Comptabilité analytique** | Ranger les charges et produits par service ou projet. La comptabilité générale dit « quoi » (du carburant), l'analytique dit « pour qui » (pour le SAVS). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **compte de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **contributions volontaires** | Aide gratuite reçue par l'association. Bénévolat, salle prêtée, dons en nature : on peut les valoriser en classe 8 (comptes 86 / 87). |
    | **coût complet** | Ce que coûte vraiment un service. Charges directes + part des charges communes + frais de siège. |
    | **crédits non reconductibles** | Financement ponctuel (CNR). Somme accordée une seule fois par l'ARS pour une dépense exceptionnelle ; elle n'est pas renouvelée l'année suivante. |
    | **Dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **file active** | Nombre de personnes accompagnées sur l'année. Elle peut dépasser le nombre de places (des personnes sortent, d'autres entrent). |
    | **Fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **Groupe II** | Dépenses de personnel. Salaires, charges sociales, intérim, formation. |
    | **groupe III** | Dépenses de structure. Loyers, assurances, entretien, amortissements, frais de siège, intérêts. |
    | **Groupes fonctionnels** | Les 3 familles de dépenses d'un ESSMS. Groupe I : exploitation courante. Groupe II : personnel. Groupe III : structure (loyers, amortissements, frais de siège). |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **Section analytique** | Une « case » de la comptabilité analytique. Un service ou un projet (ex. : 20-SAVS) dans lequel on range les charges et les produits qui le concernent. |
    | **section d'attente** | Section analytique provisoire. Pour les charges dont on ne connaît pas encore le service. Elle doit être vide à la clôture. |
    | **Taux d'activité** | Activité réalisée / activité prévue. Ex. : heures d'accompagnement faites ÷ heures prévues. Les financeurs surveillent la sous-activité. |
<!-- /glossaire-page -->

*Module de préparation au poste d'**agent comptable** dans une association du réseau Trisomie 21 France (débutant accepté). Il s'appuie sur l'association **fictive** Cap Horizons 21 : lisez d'abord la [fiche de l'association](fiche_association_Cap_Horizons_21.md). Référentiel au 10/11/2026.*

**Objectif du module.** À la fin, vous savez répondre à trois questions que l'on vous posera dès la première semaine :

1. « Cette facture, elle va sur **quel service** ? » (codifier)
2. « Combien nous **coûte** vraiment le SAVS, ou le projet Pairs ? » (répartir et calculer un coût complet)
3. « Est-ce qu'on va **tenir le budget** cette année ? » (suivre le budget et expliquer les écarts)

!!! abstract "En clair — ce module en 5 idées"
    1. **La comptabilité générale dit « quoi »** (du carburant, des salaires), **la comptabilité analytique dit « pour qui »** (pour le SESSAD, pour le SAVS, pour le projet Pairs).
    2. **Dans une association, chaque service a son financeur.** L'ARS paie le SESSAD, le Département paie le SAVS. Chacun ne veut payer que **ses** charges. L'analytique sert à le prouver.
    3. **Une charge est soit directe, soit commune.** Directe : on sait tout de suite à quel service elle appartient. Commune : on la répartit avec une **clé** (m², ETP, kilomètres, temps passé).
    4. **Le siège coûte de l'argent et doit être financé.** On le répartit sur les services sous forme de **frais de siège**, au taux autorisé par le financeur.
    5. **Le budget ne sert à rien si on ne le suit pas.** Chaque mois : budget, réalisé, **écart**, explication, et une projection de fin d'année.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple chez Cap Horizons 21 |
    |---|---|---|
    | Comptabilité analytique | Ranger chaque charge et chaque produit par **service**, projet ou activité | Le carburant de la voiture 3 va sur le SESSAD |
    | Section analytique | Une « case » de l'analytique : un service, un projet | 10-SESSAD, 20-SAVS, 50-PAIRS |
    | Code analytique | Le code saisi sur chaque ligne d'écriture | « 20 » = SAVS |
    | Charge directe | Charge qui concerne un seul service | Fournitures pédagogiques du SESSAD |
    | Charge commune (indirecte) | Charge partagée entre plusieurs services | Le loyer des locaux de Valence |
    | Clé de répartition | La règle de partage d'une charge commune | Les m², les ETP, les kilomètres |
    | ETP | Équivalent temps plein : 1 salarié à mi-temps = 0,5 ETP | Le SAVS a 7,8 ETP |
    | ESSMS | Établissement ou service social et médico-social, autorisé par l'ARS ou le Département | Le SESSAD et le SAVS |
    | SESSAD | Service d'éducation spéciale et de soins à domicile (enfants) | 45 places, financé par l'ARS |
    | SAVS | Service d'accompagnement à la vie sociale (adultes) | 60 places, financé par le Département |
    | ARS | Agence régionale de santé : finance le soin et le médico-social | Verse la dotation du SESSAD |
    | Dotation globale | Somme annuelle versée par le financeur, souvent par douzièmes | 1/12 de la dotation chaque mois |
    | Groupes fonctionnels | Les 3 grandes familles de dépenses (et de recettes) d'un ESSMS | Groupe II = personnel |
    | Frais de siège | La part du coût du siège payée par chaque service | 4,5 % des charges du SESSAD |
    | Coût complet | Charges directes + part des charges communes + frais de siège | Ce que coûte vraiment une place de SAVS |
    | Fonds dédiés | Subvention reçue pour un projet précis, pas encore dépensée à la clôture | Reste de la subvention de la Fondation Lumen |
    | Écart budgétaire | Réalisé − budget | + 12 000 € de remplacements au SESSAD |

---

## Partie 1 — Pourquoi l'analytique est indispensable dans une association

> 🟢 **En clair :** dans une entreprise, l'analytique aide à décider (quel produit est rentable ?). Dans une association médico-sociale, elle sert d'abord à **rendre des comptes** : chaque financeur doit voir que son argent a payé son service, et rien d'autre.

### 1.1 Plusieurs financeurs, plusieurs « comptes de résultat »

Chez Cap Horizons 21, une seule comptabilité générale, mais **sept sections** :

| Section | Qui paie ? | Qui contrôle le compte rendu ? |
|---|---|---|
| 10-SESSAD | ARS | ARS, via l'**ERRD** |
| 20-SAVS | Conseil départemental | Département, via le **compte administratif** |
| 30-EMPLOI | ARS + AGEFIPH + FIPHFP | Chaque financeur, via un **compte rendu financier** |
| 40-HABITAT | Département (aide à la vie partagée) | Département, via un compte rendu |
| 50-PAIRS | Fondation Lumen + Région | Fondation, via un compte rendu annuel |
| 90-ASSO | Adhérents, donateurs | Le conseil d'administration, l'assemblée générale |
| 01-SIEGE | Les autres services (frais de siège) | ARS / Département (autorisation des frais de siège) |

Si une charge du SAVS est imputée par erreur au SESSAD :

- le SESSAD paraît plus cher → l'ARS peut **refuser** cette charge (« charge non opposable ») ;
- le SAVS paraît moins cher → son résultat est faux, et le Département peut **reprendre** un excédent qui n'existe pas.

> 💡 Réflexe senior : à chaque saisie, posez-vous la question « **si le financeur de ce service me demande la pièce, est-ce que je peux justifier que cette dépense le concerne ?** » Si la réponse est non, la charge n'est pas sur le bon service, ou elle doit être répartie.

### 1.2 Comptabilité générale et analytique : deux étiquettes sur la même ligne

Une écriture analytique n'est pas une deuxième écriture. C'est **une étiquette en plus** sur la ligne de charge.

| Compte | Libellé | Code analytique | Débit | Crédit |
|---|---|---|---|---|
| 6061 Fournitures non stockables (carburant) | Carte carburant véhicule 3 – octobre | **10-SESSAD** | 186,40 | |
| 401 Fournisseurs | Station Total Valence | — | | 186,40 |

Règles de base :

- On met un code analytique sur les **classes 6 et 7** (charges et produits). Pas sur les comptes de tiers (401, 411) ni la banque.
- Une ligne peut être **ventilée** sur plusieurs codes (ex. : 60 % SESSAD, 40 % SAVS).
- Le total de l'analytique doit être **égal** au total des charges de la comptabilité générale. Une ligne sans code va dans une **section d'attente** (souvent « 99 ») qui doit être **vide** à la clôture.

> ⚠️ Erreur classique : laisser des charges dans la section d'attente « pour plus tard ». À la clôture, il y en a 40 000 €, et plus personne ne se souvient à quel service elles appartiennent.

### 1.3 Rappel indispensable : la TVA est une charge

L'association n'est pas assujettie à la TVA (activités non lucratives, exonérées). Elle **ne récupère pas** la TVA de ses achats. La charge comptabilisée est donc le montant **TTC**.

| Facture | En entreprise commerciale | Chez Cap Horizons 21 |
|---|---|---|
| Fournitures 100 € HT + 20 € TVA | 6064 : 100 / 44566 : 20 / 401 : 120 | **6064 : 120** / 401 : 120 |

Conséquence pour l'analytique et les budgets : **tous les budgets sont en TTC**. Un devis de véhicule à 20 000 € HT coûte 24 000 € à l'association.

---

## Partie 2 — Codifier une facture (le geste de tous les jours)

> 🟢 **En clair :** « codifier », c'est écrire sur la facture (ou dans le logiciel) les trois informations qui permettent de la saisir sans hésiter : **le compte**, **le service**, **le groupe fonctionnel**.

### 2.1 La méthode en 4 questions

1. **Quoi ?** Un bien consommé, un service, un salaire, un investissement ? → le **compte** (6xxx ou 2xxx).
2. **Pour qui ?** Un seul service (charge directe) ou plusieurs (charge commune) ? → le **code analytique**, ou la **clé**.
3. **Dans quel groupe ?** I (exploitation courante), II (personnel) ou III (structure) ? → indispensable pour le budget des ESSMS.
4. **Quelle période ?** La facture concerne-t-elle bien l'exercice en cours ? Sinon : charge constatée d'avance, charge à payer, ou exercice précédent.

### 2.2 Le tableau de codification type

| Facture | Compte | Groupe | Code analytique | Remarque |
|---|---|---|---|---|
| Jeux et matériel pédagogique pour les séances du SESSAD | 6068 | I | 10-SESSAD | Directe |
| Carburant (carte de la voiture 5, affectée au SAVS) | 6061 | I | 20-SAVS | Directe : la carte est liée au véhicule |
| Repas d'une sortie collective du SAVS | 6257 ou 6068 *(selon plan)* | I | 20-SAVS | Joindre la liste des participants |
| Loyer des locaux de Valence | 6132 | III | **Commune** : clé m² | Voir partie 3 |
| Assurance multirisque | 616 | III | **Commune** : clé m² | Pas de TVA sur l'assurance |
| Téléphonie mobile (34 lignes) | 626 | I | **Commune** : clé ETP, ou ligne par ligne | |
| Honoraires du commissaire aux comptes | 6226 | III | **Commune** : clé charges directes | |
| Ordinateur portable 1 100 € TTC | **2183** | III (via l'amortissement 6811) | Service utilisateur | Immobilisation, pas une charge |
| Formation d'une éducatrice (organisme de formation) | 6228 ou 631/633 *(selon le financement OPCO)* | II | Service de l'éducatrice | |
| Intérim pour remplacer une orthophoniste en arrêt | 6211 | II | 10-SESSAD | Personnel extérieur = groupe II |
| Location d'une salle pour une journée « Pairs et voix » | 6132 | I ou III *(hors ESSMS : sans objet)* | 50-PAIRS | Le projet n'est pas un ESSMS : seul le budget de la convention compte |

> 💡 Réflexe senior : écrivez le code **sur la facture** (ou dans le commentaire de la pièce numérique) **avant** de la faire valider par le chef de service. S'il n'est pas d'accord, il le corrige au moment de la validation, pas trois mois plus tard.

### 2.3 Les pièges de codification

| Situation | Le piège | La bonne pratique |
|---|---|---|
| Une facture d'imprimante pour tout le bâtiment | La mettre « au SESSAD parce que c'est le plus gros » | Charge commune → clé ETP |
| Une facture adressée au nom d'une salariée | La saisir comme une facture de l'association | Bloquer : soit refaire la facture au nom de l'association, soit passer en note de frais |
| Une facture de décembre 2025 reçue en février 2026 | La passer en charge 2026 | Si une charge à payer avait été constatée en 2025 : solder le 408. Sinon : charge sur exercice antérieur, à signaler |
| Le carburant d'une voiture qui sert à deux services | Tout mettre sur le service du conducteur habituel | Clé kilomètres (carnet de bord) |
| Un salarié qui travaille pour deux services | Laisser tout son salaire sur un seul service | Ventiler au **temps passé**, avec un planning signé |

---

## Partie 3 — Répartir les charges communes

> 🟢 **En clair :** une clé de répartition, c'est une règle de partage **juste, simple et justifiable**. Juste : elle suit ce qui fait varier la charge. Simple : on peut la calculer tous les mois. Justifiable : on peut la montrer au financeur.

### 3.1 Choisir la bonne clé

| La charge varie avec… | Clé | Exemples |
|---|---|---|
| La surface | **m²** | Loyer, charges locatives, ménage, électricité, assurance des locaux |
| Le nombre de personnes qui travaillent | **ETP** | Téléphonie, informatique, logiciels, fournitures de bureau, médecine du travail |
| L'usage des véhicules | **kilomètres** | Carburant, entretien, assurance flotte (ou véhicules affectés) |
| Le temps de travail | **temps passé** (heures) | Psychologue, secrétaire ou chef de service partagés |
| Rien de mesurable | **charges directes** (ou forfait) | Honoraires du CAC, frais bancaires |

### 3.2 Exemple chiffré : le loyer

Loyer et charges des locaux de Valence : **74 400 €** TTC par an. Surfaces : SESSAD 280 m², SAVS 160 m², Emploi 60 m², Siège 90 m², salle commune 30 m² (total 620 m²).

**Étape 1 — On répartit la salle commune** comme le reste (au prorata des 590 m² occupés) : on raisonne donc directement sur 590 m².

| Service | m² | % (sur 590) | Loyer |
|---|---|---|---|
| 10-SESSAD | 280 | 47,46 % | 35 308,47 € |
| 20-SAVS | 160 | 27,12 % | 20 176,27 € |
| 30-EMPLOI | 60 | 10,17 % | 7 566,10 € |
| 01-SIEGE | 90 | 15,25 % | 11 349,16 € |
| **Total** | **590** | **100 %** | **74 400,00 €** |

*Calcul : 74 400 × 280 / 590 = 35 308,47 €, et ainsi de suite. Le dernier montant est calculé par différence pour que le total tombe juste.*

**Étape 2 — La part du siège** (11 349,16 €) n'est pas « perdue » : elle fait partie du coût du siège, qui sera refacturé aux services par les **frais de siège** (partie 4).

> ⚠️ Erreur classique : répartir le loyer du siège une deuxième fois sur les services avec la clé m², **puis** facturer les frais de siège. Le loyer du siège est alors payé deux fois par les services.

### 3.3 Le temps passé : le cas des salariés partagés

La psychologue (1 ETP) travaille 60 % pour le SESSAD et 40 % pour le SAVS selon son planning. Coût chargé annuel : 58 000 €.

| Service | % temps | Charge |
|---|---|---|
| 10-SESSAD | 60 % | 34 800,00 € |
| 20-SAVS | 40 % | 23 200,00 € |

Il faut un **document qui prouve** la répartition : planning, relevé d'heures mensuel signé, ou avenant au contrat. C'est la première pièce que demande un financeur.

> 💡 Réflexe senior : si la répartition réelle change (la psychologue passe plus de temps au SAVS cet automne), on **met à jour la clé** et on le dit au chef de service. Une clé figée depuis cinq ans est une clé fausse.

### 3.4 Deux façons techniques de répartir

| Méthode | Comment | Avantage | Inconvénient |
|---|---|---|---|
| **À la saisie** | Ventilation de la ligne de facture sur plusieurs codes (grille de ventilation dans le logiciel) | Le réalisé par service est juste en temps réel | Il faut tenir les grilles à jour |
| **Par OD analytique** (opération diverse) en fin de mois | On saisit sur une section « commune », puis on la vide vers les services | Plus simple à la saisie | Les chiffres par service sont faux avant l'OD |

Exemple d'OD analytique de répartition (on « vide » la section commune) :

| Compte | Code analytique | Débit | Crédit |
|---|---|---|---|
| 6132 Locations immobilières | 10-SESSAD | 35 308,47 | |
| 6132 Locations immobilières | 20-SAVS | 20 176,27 | |
| 6132 Locations immobilières | 30-EMPLOI | 7 566,10 | |
| 6132 Locations immobilières | 01-SIEGE | 11 349,16 | |
| 6132 Locations immobilières | 98-COMMUN | | 74 400,00 |

*Le compte général ne bouge pas (débit et crédit sur le même compte 6132) : seule l'étiquette analytique change.*

---

## Partie 4 — Les frais de siège

> 🟢 **En clair :** le siège (direction générale, comptabilité, RH) ne reçoit pas de dotation à lui. Ce sont les services qui le financent, chacun pour sa part, sous forme de **frais de siège** inscrits dans leur budget (groupe III).

### 4.1 Le principe

- Pour les **ESSMS** (SESSAD, SAVS), les frais de siège doivent être **autorisés** par l'autorité de tarification (procédure prévue par le Code de l'action sociale et des familles). L'autorisation fixe un **taux** ou un **montant**, en général pour 5 ans. Chez Cap Horizons 21 : **4,5 %** des charges brutes des ESSMS, hors frais de siège.
- Pour les **autres activités** (emploi accompagné, habitat, projet Pairs), une quote-part n'est possible que si le **financeur l'accepte** dans le budget de la convention. Sinon, ce coût reste à la charge des fonds propres de l'association.

### 4.2 Exemple de calcul

Charges brutes 2026, hors frais de siège : SESSAD 1 130 000 € ; SAVS 612 000 €.

| Service | Base | Taux | Frais de siège |
|---|---|---|---|
| 10-SESSAD | 1 130 000 € | 4,5 % | 50 850,00 € |
| 20-SAVS | 612 000 € | 4,5 % | 27 540,00 € |
| **Total ESSMS** | | | **78 390,00 €** |

Le siège coûte 160 000 €. Il reste **81 610 €** à financer : part acceptée par les conventions des autres dispositifs, plus la part du loyer et des fonctions du siège qui sont déjà **refacturées directement**, et le reste sur les ressources propres. *(Les chiffres complets sont travaillés dans l'exercice E16-04.)*

> 💡 Réflexe senior : vérifiez chaque année que **le total des frais de siège facturés ne dépasse pas** ce qui a été autorisé, et que le siège est bien **équilibré**. Un siège en déficit chronique doit être signalé à la direction : soit on demande une révision du taux, soit on réduit ses charges.

### 4.3 Comment on l'enregistre

Deux pratiques, selon l'organisation de l'association :

1. **Une seule comptabilité, analytique par service** (cas de Cap Horizons 21) : une **OD analytique** transfère le coût du siège vers les sections des services. Pas d'écriture entre comptes de tiers.
2. **Une comptabilité par établissement** (grandes associations) : le siège « facture » les services par un **compte de liaison** (181). Charge dans le service (groupe III), produit dans le siège ; les comptes de liaison s'annulent quand on combine les comptes.

---

## Partie 5 — Le coût complet d'un accompagnement

> 🟢 **En clair :** le coût complet répond à la question « **combien coûte une place, une personne accompagnée, une heure d'intervention** ? ». On en a besoin pour discuter avec le financeur, et pour chiffrer une réponse à un appel à projets.

### 5.1 La construction en cascade

| Étape | Ce qu'on ajoute | SAVS (exemple) |
|---|---|---|
| 1 | Charges **directes** (salaires de l'équipe, carburant, activités) | 547 540 € |
| 2 | + Part des charges **communes** (loyer, téléphonie, véhicules, psychologue) | 64 460 € |
| 3 | = Coût de production du service (base des frais de siège) | 612 000 € |
| 4 | + **Frais de siège** | 27 540 € |
| 5 | = **Coût complet** | **640 000 €** |
| 6 | ÷ nombre de places (60) | **10 666,67 € par place et par an** |

Autres unités utiles :

- **par personne accompagnée** (file active : 72 personnes accompagnées sur l'année pour 60 places) : 640 000 / 72 = 8 888,89 € ;
- **par heure d'intervention directe** (ex. : 9 800 heures auprès des personnes) : 640 000 / 9 800 = 65,31 €.

> ⚠️ Erreur classique : comparer le coût d'une place du SAVS avec celui d'une autre association **sans vérifier ce qui est dedans** (frais de siège inclus ou non, transport inclus ou non). Annoncez toujours ce que contient votre coût.

### 5.2 Le vrai coût d'un projet : les contributions volontaires

Un projet comme « Pairs et voix » repose aussi sur des **bénévoles** (pairs, parents) et sur une salle **prêtée gratuitement** par la mairie. Ce n'est pas une dépense, mais c'est une ressource.

- On peut les **valoriser** en classe 8 (comptes **86** emplois / **87** contributions), en pied de compte de résultat, si l'association dispose d'une méthode fiable (heures relevées, taux horaire justifié).
- Le compte rendu financier (Cerfa n° 15059) et le budget prévisionnel (Cerfa n° 12156) ont des lignes prévues pour cela.

> 💡 Réflexe senior : un financeur apprécie de voir la valorisation du bénévolat : elle montre que **son euro produit plus qu'un euro** d'action. C'est un argument fort dans une réponse à un appel à projets.

---

## Partie 6 — Le suivi budgétaire

> 🟢 **En clair :** suivre un budget, c'est comparer chaque mois **ce qu'on avait prévu** et **ce qui s'est passé**, comprendre l'écart, et **prévenir** la direction assez tôt pour agir.

### 6.1 Le tableau de suivi type (SESSAD, au 30/09)

| Groupe | Budget annuel | Budget au prorata 9/12 | Réalisé au 30/09 | Écart (€) | Écart (%) | Commentaire |
|---|---|---|---|---|---|---|
| I — Exploitation courante | 96 000 | 72 000 | 70 100 | − 1 900 | − 2,6 % | Normal |
| II — Personnel | 924 000 | 693 000 | 712 400 | **+ 19 400** | **+ 2,8 %** | Intérim pour remplacer une orthophoniste en arrêt |
| III — Structure | 160 000 | 120 000 | 113 500 | − 6 500 | − 5,4 % | Achat de véhicule reporté (amortissement non commencé) |
| **Total charges** | **1 180 000** | **885 000** | **896 000** | **+ 11 000** | **+ 1,2 %** | |

*Lecture : un écart **positif sur une charge** est **défavorable** (on a dépensé plus que prévu).*

### 6.2 Les 4 réflexes d'analyse

1. **Prorata ou saisonnalité ?** Le prorata 9/12 suppose des dépenses régulières. Ce n'est pas vrai pour tout : les congés payés d'été, une prime versée en décembre, une assurance payée en janvier. Utilisez un **budget mensualisé** quand c'est possible.
2. **Écart ponctuel ou durable ?** L'intérim de l'orthophoniste s'arrête quand elle revient ; une augmentation de loyer, non.
3. **Projection de fin d'année** : réalisé à date + reste à dépenser **réaliste** (pas simplement le reste du budget). Exemple, groupe II : le rythme réel est de 712 400 / 9 = 79 155,56 € par mois. Mais l'intérim (environ 2 900 € par mois) s'arrête au retour de l'orthophoniste, prévu le 1er novembre. Projection : 712 400 + 3 × 76 255,56 + 2 900 (octobre) ≈ 944 067 €, soit environ **20 000 €** de plus que le budget de 924 000 €.
4. **Remboursements et produits en face** : les indemnités journalières (IJSS) versées pour l'orthophoniste en arrêt **réduisent** la charge de personnel (depuis le PCG 2025, plus de compte de transfert de charges 79). Vérifiez qu'elles sont bien encaissées et imputées au SESSAD.

### 6.3 Prévenir la direction : la note de suivi

Une bonne note tient en une page :

```
Objet : suivi budgétaire SESSAD au 30/09/2026

Madame la Directrice,
Au 30 septembre, les charges du SESSAD s'élèvent à 896 000 €, soit 11 000 € (+1,2 %)
de plus que le budget au prorata.
- Principal écart : personnel (+19 400 €), dû à l'intérim de remplacement de
  l'orthophoniste en arrêt depuis mai. Les IJSS reçues (6 200 €) sont déjà déduites.
- Écart favorable : structure (−6 500 €), achat du véhicule reporté à 2027.
Projection au 31/12 : déficit estimé de 8 000 à 12 000 € si l'arrêt se prolonge.
Pistes : demander à l'ARS des crédits non reconductibles pour le remplacement ;
reporter l'achat de mobilier prévu en novembre.
Je reste à votre disposition pour en parler.
```

> 💡 Réflexe senior : **un chiffre, une cause, une piste**. La directrice n'a pas besoin du grand livre ; elle a besoin de savoir s'il faut agir, et comment.

### 6.4 Le tableau de bord mensuel

Quelques indicateurs simples, suivis chaque mois pour chaque service :

| Indicateur | Calcul | Pourquoi |
|---|---|---|
| Taux d'activité | Places occupées / places autorisées (ou heures réalisées / heures prévues) | L'ARS et le Département surveillent la sous-activité |
| Poids du personnel | Groupe II / total des charges | En général 75 à 85 % dans un service d'accompagnement |
| Écart budgétaire cumulé | Réalisé − budget au prorata | Alerte précoce |
| Coût par place | Charges cumulées / places, ramené à l'année | Comparaison dans le temps |
| Jours de trésorerie | Trésorerie / (charges annuelles décaissables / 365) | Combien de jours on tient sans recette |

---

## Partie 7 — Subventions affectées et fonds dédiés (lien avec l'analytique)

> 🟢 **En clair :** quand un financeur donne de l'argent **pour un projet précis** et que tout n'est pas dépensé au 31/12, on ne le garde pas en résultat : on le met de côté en **fonds dédiés**, pour le dépenser l'année suivante sur ce même projet.

Exemple : Fondation Lumen, convention 2025-2027, 150 000 € au total. En 2026, l'association reçoit 50 000 € mais ne dépense que 42 000 € sur le projet.

| Date | Compte | Libellé | Débit | Crédit |
|---|---|---|---|---|
| 31/12/2026 | 689 Reports en fonds dédiés | Part non utilisée de la subvention Fondation Lumen 2026 | 8 000,00 | |
| 31/12/2026 | 19x Fonds dédiés sur subventions | Projet Pairs et voix | | 8 000,00 |

En 2027, quand ces 8 000 € seront dépensés : D 19x / C **789** Utilisation des fonds dédiés. Les deux lignes portent le code **50-PAIRS**.

Ce mécanisme ne marche que si **l'analytique est juste** : c'est elle qui donne le montant réellement dépensé sur le projet.

> ⚠️ Erreur classique : calculer les fonds dédiés à partir des seuls achats du projet, en oubliant la **quote-part des salaires** de l'éducatrice qui y travaille 20 % de son temps. Le projet paraît sous-consommé, on reporte trop, et le financeur croit que le projet n'avance pas.

---

## Checklist de fin de module

- [ ] Je sais expliquer la différence entre comptabilité générale et analytique en une phrase.
- [ ] Je codifie une facture en 4 questions : quoi, pour qui, quel groupe, quelle période.
- [ ] Je sais que la TVA est une charge pour l'association (saisie TTC).
- [ ] Je choisis une clé de répartition et je sais la justifier (m², ETP, km, temps passé).
- [ ] Je ne fais pas payer deux fois le loyer du siège (clé + frais de siège).
- [ ] Je calcule des frais de siège au taux autorisé et je vérifie l'équilibre du siège.
- [ ] Je construis un coût complet par place, par personne et par heure.
- [ ] Je fais un tableau budget / réalisé / écart, et une projection de fin d'année réaliste.
- [ ] J'écris une note de suivi d'une page : un chiffre, une cause, une piste.
- [ ] Je calcule des fonds dédiés à partir du réalisé analytique, salaires compris.

**Exercices du module :** E16-01 à E16-10, puis la banque de QCM. Le module **M17** met tout cela en pratique dans les missions du poste (factures, paie, EPRD/ERRD, appels à projets, trésorerie).
