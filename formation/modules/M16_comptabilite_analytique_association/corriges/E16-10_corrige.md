# Corrigé E16-10 — Construire le tableau de bord mensuel de la direction

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CDD** | Contrat à durée déterminée. Contrat de travail avec une date de fin ; donne souvent droit à une indemnité de fin de contrat. |
    | **CNR** | Crédits non reconductibles. Financement ponctuel accordé par l'ARS pour une dépense exceptionnelle (remplacement, véhicule). Il n'est pas renouvelé l'année suivante. |
    | **CPOM** | Contrat pluriannuel d'objectifs et de moyens. Contrat de 5 ans entre une association et l'ARS et/ou le Département : objectifs, moyens, et budget présenté en EPRD. |
    | **EPRD** | État des prévisions de recettes et de dépenses. Budget prévisionnel des gestionnaires sous CPOM. Il part de la ressource notifiée par le financeur (« budget par la recette »). Dépôt en général au 30 avril (à vérifier chaque année). |
    | **ERRD** | État réalisé des recettes et des dépenses. Le compte rendu de l'EPRD après la clôture : réalisé, écarts, proposition d'affectation du résultat. Dépôt en général au 30 avril N+1 (à vérifier). |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **FIN.MOIS** | Fonction Excel « fin du mois ». Renvoie le dernier jour du mois d'une date (ex. : FIN.MOIS(A2;0) donne le 31/10 pour le 12/10). Utile pour les échéances. |
    | **GI** | Groupe I (groupe fonctionnel). Dans le budget d'un ESSMS : les dépenses d'exploitation courante (carburant, fournitures, alimentation…). |
    | **GII** | Groupe II (groupe fonctionnel). Dans le budget d'un ESSMS : les dépenses de personnel (salaires, charges sociales, intérim). |
    | **GIII** | Groupe III (groupe fonctionnel). Dans le budget d'un ESSMS : les dépenses de structure (loyers, assurances, amortissements, frais de siège). |
    | **RECHERCHEV** | Fonction Excel de recherche verticale. Cherche une valeur dans la 1re colonne d'un tableau et renvoie l'info d'une autre colonne. Toujours finir par FAUX (correspondance exacte), sinon le résultat peut être faux. |
    | **RECHERCHEX** | Fonction Excel de recherche moderne. Remplace RECHERCHEV : cherche une valeur dans une colonne et renvoie celle d'une autre colonne, à gauche ou à droite, en correspondance exacte par défaut. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SI** | Stock initial. Stock au début de l'exercice (= stock final de l'exercice précédent). |
    | **SOMME.SI.ENS** | Fonction Excel de somme avec conditions. Additionne les montants qui respectent un ou plusieurs critères (ex. : total des factures de l'établissement de Nice en septembre). |
    | **TCD** | Tableau croisé dynamique. Outil d'Excel qui regroupe et totalise des données (très utile en révision). |
    | **TDB** | Tableau de bord. Une page de quelques indicateurs suivis chaque mois par la direction (activité, coût, budget, trésorerie). |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **Compte 401** | Fournisseurs. Ce que l'association doit à ses fournisseurs (factures reçues, pas encore payées). |
    | **comptabilité analytique** | Ranger les charges et produits par service ou projet. La comptabilité générale dit « quoi » (du carburant), l'analytique dit « pour qui » (pour le SAVS). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **double signature** | Deux personnes valident le paiement. Au-dessus d'un seuil, la directrice ET la trésorière signent le virement : c'est un contrôle anti-fraude. |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **Groupe I** | Dépenses d'exploitation courante. Carburant, fournitures, alimentation, petit matériel. |
    | **groupe II** | Dépenses de personnel. Salaires, charges sociales, intérim, formation. |
    | **Groupe III** | Dépenses de structure. Loyers, assurances, entretien, amortissements, frais de siège, intérêts. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **Taux d'activité** | Activité réalisée / activité prévue. Ex. : heures d'accompagnement faites ÷ heures prévues. Les financeurs surveillent la sous-activité. |
    | **Taux d'occupation** | Places occupées / places autorisées. Ex. : 42 enfants accompagnés pour 45 places = 93,3 %. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-10](../exercices/E16-10_tableau-de-bord-mensuel-direction.md)

*Rappel : association, personnes et chiffres fictifs. Excel en français : séparateur « ; ».*

!!! abstract "En clair"
    1. Avant de calculer un indicateur de coût, on **retraite** : on ajoute ce qui manque dans la comptabilité du mois (amortissements, frais de siège trimestriels).
    2. Sans retraitement, le SESSAD semble avoir 34 323 € d'avance sur son budget (− 3,49 %). Après retraitement, l'avance n'est plus que de 8 422 € (− 0,86 %).
    3. Les points orange d'octobre : **activité** du SESSAD et du SAVS en dessous de l'objectif, **budget** du SAVS dépassé, **délai fournisseurs** passé de 28 à 37 jours.
    4. Le fichier Excel se met à jour en changeant **une seule cellule** : la date d'arrêté.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Un bon indicateur = une définition + une source + une cible

Un tableau de bord ne sert à rien si la directrice doit se demander « comment ce chiffre est-il calculé ? ». Pour chaque indicateur, on fixe une fois pour toutes :

| Indicateur | Formule | Source | Pourquoi la directrice le regarde |
|---|---|---|---|
| Taux d'occupation | personnes accompagnées ÷ places autorisées | dossier des usagers | Les financeurs paient des places : des places vides sont un risque sur la dotation |
| Taux d'activité | activité réalisée ÷ activité prévue (cumul) | logiciel de suivi des interventions | Une place occupée mais peu accompagnée n'est pas un service rendu |
| Coût annualisé par place | charges retraitées × 12/10 ÷ places | comptabilité analytique | Comparable d'un service à l'autre et d'une année à l'autre (l'ARS compare les SESSAD entre eux) |
| Poids du personnel | groupe II ÷ total des charges retraitées | comptabilité analytique | Dans le médico-social, le personnel fait environ 80 % des charges : une dérive de 1 point = plusieurs milliers d'euros |
| Écart budgétaire cumulé | charges retraitées − budget × mois/12 | comptabilité + budget | Prévenir un déficit |
| Jours de trésorerie | trésorerie ÷ (charges décaissables annuelles ÷ 365) | banque | Combien de jours l'association peut payer sans nouvelle recette |
| Délai moyen de paiement fournisseurs | solde 401 ÷ achats TTC des 3 derniers mois × nombre de jours | comptabilité fournisseurs | Respect des délais légaux, relations avec les fournisseurs |

### Pourquoi retraiter ?

La comptabilité d'octobre est **juste**, mais **incomplète** pour un pilotage mensuel :

- les **amortissements** ne sont passés qu'au 31/12 → il manque 10/12 de la dotation annuelle ;
- la **quote-part de frais de siège** est facturée par trimestre → au 31/10, octobre n'est pas encore facturé ;
- les **CNR** du SESSAD sont encaissés mais pas encore dépensés → la trésorerie paraît plus confortable qu'elle ne l'est.

> ⚠️ Erreur classique : afficher un feu **vert** sur le budget du SESSAD (− 3,49 %) alors que l'écart vient surtout d'écritures pas encore passées. La directrice croit avoir de la marge… et l'ERRD sort en déficit.

> 💡 Réflexe senior : la vraie solution est en amont : passer chaque mois un « abonnement » des amortissements et des frais de siège (1/12 du budget). Le retraitement dans le tableau de bord n'est qu'une rustine en attendant.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 1 — Charges cumulées et écart budgétaire

**Cumul au 31/10 = cumul au 30/09 + octobre**

| Service | Groupe I | Groupe II | Groupe III | Total cumulé brut |
|---|---|---|---|---|
| 10-SESSAD | 63 600 + 7 100 = 70 700,00 | 690 300 + 77 900 = 768 200,00 | 102 910 + 7 200 = 110 110,00 | **949 010,00** |
| 20-SAVS | 38 100 + 4 300 = 42 400,00 | 384 900 + 42 300 = 427 200,00 | 59 820 + 4 283,33 = 64 103,33 | **533 703,33** |
| 30-EMPLOI | 17 300 + 1 900 = 19 200,00 | 192 400 + 21 600 = 214 000,00 | 16 600 + 1 800 = 18 400,00 | **251 600,00** |

**Retraitements**

| Service | Amortissements (annuel × 10/12) | Frais de siège d'octobre (annuel ÷ 12) | Total charges retraitées |
|---|---|---|---|
| 10-SESSAD | 26 000 × 10/12 = 21 666,67 | 50 813 / 12 = 4 234,42 | 949 010,00 + 21 666,67 + 4 234,42 = **974 911,09** |
| 20-SAVS | 5 000 × 10/12 = 4 166,67 | 27 560 / 12 = 2 296,67 | 533 703,33 + 4 166,67 + 2 296,67 = **540 166,67** |
| 30-EMPLOI | — | — (déjà imputés) | **251 600,00** |

**Écarts (budget proratisé = budget annuel × 10/12)**

| Service | Budget proratisé | Écart brut (€) | Écart brut (%) | Écart retraité (€) | Écart retraité (%) |
|---|---|---|---|---|---|
| 10-SESSAD | 1 180 000 × 10/12 = 983 333,33 | − 34 323,33 | − 3,49 % | − 8 422,24 | − 0,86 % |
| 20-SAVS | 640 000 × 10/12 = 533 333,33 | + 370,00 | + 0,07 % | + 6 833,34 | + 1,28 % |
| 30-EMPLOI | 300 000 × 10/12 = 250 000,00 | + 1 600,00 | + 0,64 % | + 1 600,00 | + 0,64 % |

**Commentaire SESSAD** : l'écart brut de − 34 323,33 € est composé à 75 % d'écritures manquantes (21 666,67 + 4 234,42 = 25 901,09 €). Il reste − 8 422,24 €, qui s'explique surtout par le poste d'éducatrice non remplacé de juin à septembre (groupe II : 768 200 − 780 000 = − 11 800 €). Ce n'est pas une marge durable : le CDD coûte 3 900 € par mois depuis octobre, et les 25 000 € d'achats financés par les CNR arrivent en novembre.

**Commentaire SAVS** : brut, le SAVS semble « dans les clous » (+ 0,07 %). Retraité, il dépasse de 1,28 %, ce qui est cohérent avec la projection de déficit d'environ 11 660 € faite au 30/09 (exercice E16-06) : annualisées, les charges retraitées donnent 540 166,67 × 12/10 = 648 200 €, très proche des 648 060 € projetés.

### Question 2 — Indicateurs d'activité et de coût

| Indicateur | 10-SESSAD | 20-SAVS | 30-EMPLOI |
|---|---|---|---|
| Taux d'occupation | 43 / 45 = **95,6 %** | 58 / 60 = **96,7 %** | 37 / 40 = **92,5 %** |
| Taux d'activité | 7 640 / 8 250 = **92,6 %** | 11 350 / 12 500 = **90,8 %** | 3 820 / 4 000 = **95,5 %** |
| Charges retraitées annualisées (× 12/10) | 1 169 893,31 | 648 200,00 | 301 920,00 |
| **Coût annualisé par place** | 1 169 893,31 / 45 = **25 997,63** | 648 200,00 / 60 = **10 803,33** | 301 920,00 / 40 = **7 548,00** |
| Coût budgété par place | 1 180 000 / 45 = 26 222,22 | 640 000 / 60 = 10 666,67 | 300 000 / 40 = 7 500,00 |
| Écart du coût par place | − 0,86 % | + 1,28 % | + 0,64 % |
| **Poids du personnel** (groupe II / charges retraitées) | 768 200 / 974 911,09 = **78,80 %** | 427 200 / 540 166,67 = **79,09 %** | 214 000 / 251 600 = **85,06 %** |
| Poids du personnel au budget | 936 000 / 1 180 000 = 79,32 % | 505 000 / 640 000 = 78,91 % | 252 000 / 300 000 = 84,00 % |
| Écart (points) | − 0,52 pt | + 0,18 pt | + 1,06 pt |

Remarques :

- L'écart du coût par place est, par construction, égal à l'écart budgétaire en % (les deux comparent des charges annualisées au budget). L'intérêt du coût par place est ailleurs : **comparer** avec les autres SESSAD et SAVS (données des financeurs, indicateurs du réseau) et suivre l'évolution d'une année sur l'autre.
- Le taux d'activité du SESSAD (92,6 %) est plus bas que son taux d'occupation (95,6 %) : les enfants sont là, mais ils ont eu **moins d'interventions** que prévu pendant l'absence non remplacée de Mme Perrin. Sous CPOM, les objectifs d'activité comptent : à expliquer à l'ARS.

### Question 3 — Trésorerie et fournisseurs

**Jours de trésorerie** : charges décaissables par jour = 2 300 000 / 365 = 6 301,37 €.

| | Trésorerie | Jours |
|---|---|---|
| Au 31/10, brut | 412 000 | 412 000 / 6 301,37 = **65,4 jours** |
| Au 31/10, hors CNR à dépenser | 412 000 − 25 000 = 387 000 | 387 000 / 6 301,37 = **61,4 jours** |
| Pour comparaison, au 31/01 | 468 000 | 74,3 jours |

Lecture : la trésorerie a baissé de 56 000 € depuis janvier, et une fois les CNR dépensés en novembre, l'association sera à **environ 61 jours**, juste au-dessus du seuil de vigilance de 60 jours. Elle reste confortable, mais la tendance est à surveiller (déficit du SAVS, achats de fin d'année).

**Délai moyen de paiement des fournisseurs** (méthode simple : solde 401 ÷ achats TTC des 3 derniers mois × nombre de jours de ces 3 mois) :

| | Calcul | Résultat |
|---|---|---|
| Au 30/09 | 58 900 / 197 000 × 92 jours (juil. 31 + août 31 + sept. 30) | **27,5 jours** |
| Au 31/10 | 86 400 / 214 000 × 92 jours (août 31 + sept. 30 + oct. 31) | **37,1 jours** |

Lecture : le délai s'est allongé de près de **10 jours** en un mois. Cause probable (note de la pièce 5) : la directrice était en congé du 12 au 23/10 et **aucune délégation** de signature des bons à payer n'avait été prévue. Le délai reste sous le plafond légal (le Code de commerce fixe un délai maximal entre professionnels, en principe **60 jours** à compter de la date de la facture, ou 45 jours fin de mois si les parties en conviennent — *à vérifier dans le texte en vigueur*), mais des retards répétés exposent à des **pénalités de retard** et à l'**indemnité forfaitaire de 40 €** par facture, et abîment la relation avec les fournisseurs locaux.

## 3. Tableau de bord, seuils et formules Excel

*Pas d'écriture comptable dans cet exercice : le tableau de bord exploite la comptabilité, il ne la modifie pas.*

### Question 4 — Seuils proposés

| Indicateur | 🟢 Vert | 🟠 Orange | 🔴 Rouge |
|---|---|---|---|
| Taux d'occupation | ≥ 95 % | 90 % à 95 % | < 90 % |
| Taux d'activité | ≥ 95 % | 90 % à 95 % | < 90 % |
| Écart budgétaire cumulé (charges retraitées) | ≤ + 1 % | + 1 % à + 3 % | > + 3 % |
| Coût par place / budget | ≤ budget | jusqu'à + 2 % | > + 2 % |
| Poids du personnel / budget | ≤ + 1 point | + 1 à + 2 points | > + 2 points |
| Jours de trésorerie | ≥ 60 jours | 30 à 60 jours | < 30 jours |
| Délai moyen fournisseurs | ≤ 30 jours | 30 à 45 jours | > 45 jours |

Règle complémentaire : un écart budgétaire **inférieur à − 5 %** n'est pas « super vert » : il est marqué **« à expliquer »** (écriture manquante ? poste vacant ? activité en baisse ?).

Ces seuils sont des **propositions** : ils se fixent avec la directrice, puis ne changent plus en cours d'année.

### Le tableau de bord commenté — octobre 2026

```
CAP HORIZONS 21 — TABLEAU DE BORD DE LA DIRECTION — Arrêté au 31/10/2026 (10 mois)

                               SESSAD            SAVS              EMPLOI ACC.
Taux d'occupation              95,6 %  🟢        96,7 %  🟢        92,5 %  🟠
Taux d'activité                92,6 %  🟠        90,8 %  🟠        95,5 %  🟢
Écart budgétaire (retraité)    − 0,86 % 🟢       + 1,28 % 🟠       + 0,64 % 🟢
Coût annualisé par place       25 998 € 🟢       10 803 € 🟠        7 548 € 🟠
  (budget)                     (26 222 €)        (10 667 €)        (7 500 €)
Poids du personnel             78,8 %  🟢        79,1 %  🟢        85,1 %  🟠
  (budget)                     (79,3 %)          (78,9 %)          (84,0 %)

ASSOCIATION
Jours de trésorerie            65 j (61 j hors CNR)  🟢 — en baisse depuis janvier (74 j)
Délai moyen fournisseurs       37 j  🟠 — 28 j en septembre

COMMENTAIRES
1. SESSAD : budget tenu, mais l'avance vient du poste non remplacé de juin à
   septembre. Activité à 92,6 % : rattrapage attendu avec le CDD depuis le 01/10.
   À expliquer dans l'ERRD si l'objectif annuel n'est pas atteint.
2. SAVS : dépassement de 1,28 % (≈ 6 800 €) ; projection de fin d'année :
   déficit d'environ 11 700 € (note du 19/10). Activité à 90,8 % : en limite
   du seuil rouge, à analyser avec Sophie Laurent (absences, liste d'attente ?).
3. Emploi accompagné : 3 places disponibles (37/40) ; personnel un peu au-dessus
   du budget (+ 1 point). Vérifier les admissions prévues d'ici décembre.
4. Fournisseurs : + 10 jours en octobre à cause des bons à payer bloqués
   pendant les congés. Proposition : délégation de signature écrite pendant
   les absences de la directrice.
5. Trésorerie : confortable, mais à 61 jours une fois les CNR dépensés.

Retraitements appliqués : amortissements 10/12 et frais de siège d'octobre
(SESSAD, SAVS). Sources : balance analytique, logiciel de suivi d'activité, banque.
```

### Question 5 — Les formules Excel

**Onglet TDB — mise en page** : B1 = date d'arrêté (31/10/2026) ; B2 = nombre de mois écoulés ; services en A5:A7 (10-SESSAD, 20-SAVS, 30-EMPLOI) ; groupes en B4:D4 (GI, GII, GIII).

```
B2  (mois écoulés)          =MOIS($B$1)
```

**Réalisé cumulé** d'un service et d'un groupe, du 1er janvier à la date d'arrêté (cellule B5, à recopier vers la droite et vers le bas) :

```
=SOMME.SI.ENS(Donnees!$F:$F;Donnees!$B:$B;$A5;Donnees!$C:$C;B$4;
              Donnees!$A:$A;">="&DATE(ANNEE($B$1);1;1);Donnees!$A:$A;"<="&$B$1)
```

Les `$` sont placés pour que la colonne A (service) et la ligne 4 (groupe) restent fixes quand on recopie. Le critère de date utilise `"<="&$B$1` : on concatène l'opérateur et la date.

**Budget annuel** (onglet Budget, colonne A = clé `Service|Groupe`, par exemple `10-SESSAD|GII`, construite par `=B2&"|"&C2`) :

```
Avec RECHERCHEV :  =RECHERCHEV($A5&"|"&B$4;Budget!$A:$D;4;FAUX)
Avec RECHERCHEX :  =RECHERCHEX($A5&"|"&B$4;Budget!$A:$A;Budget!$D:$D;"absent")
```

RECHERCHEV cherche toujours dans la **première colonne** de la plage (d'où la clé en colonne A) et a besoin de `FAUX` pour une correspondance exacte. RECHERCHEX est plus souple (colonne de recherche et colonne de résultat séparées, valeur par défaut si absent), mais n'existe que dans les versions récentes d'Excel.

**Budget proratisé, écart, écart %** (exemple sur le total d'un service, en ligne 5) :

```
Budget proratisé   G5  =F5*$B$2/12                (F5 = budget annuel du service)
Retraitements      H5  =Amort_annuel*$B$2/12 + FS_annuel/12   (0 pour l'emploi accompagné)
Charges retraitées I5  =E5+H5                     (E5 = total réalisé cumulé)
Écart €            J5  =I5-G5
Écart %            K5  =SIERREUR(J5/G5;0)
```

**Feu tricolore** sur l'écart budgétaire :

```
L5  =SI(K5<-5%;"À expliquer";SI(K5<=1%;"Vert";SI(K5<=3%;"Orange";"Rouge")))
```

Taux d'activité et feu :

```
Taux d'activité  =SOMME.SI.ENS(Activite!$F:$F;Activite!$B:$B;$A5;Activite!$A:$A;"<="&$B$1)
                 /SOMME.SI.ENS(Activite!$E:$E;Activite!$B:$B;$A5;Activite!$A:$A;"<="&$B$1)
Feu              =SI(M5>=95%;"Vert";SI(M5>=90%;"Orange";"Rouge"))
```

(Si l'onglet Activite contient des cumuls mensuels plutôt que des montants du mois, on ne prend que la ligne de la date d'arrêté : critère `Activite!$A:$A;$B$1` au lieu de `"<="&$B$1`.)

**Jours de trésorerie** (B20 = trésorerie au 31/10 ; B21 = charges décaissables annuelles) :

```
=B20/(B21/365)
```

**Délai moyen fournisseurs** (B25 = solde 401 ; B26:B28 = achats TTC des 3 derniers mois) :

```
=B25/SOMME(B26:B28)*($B$1-FIN.MOIS($B$1;-3))
```

`FIN.MOIS($B$1;-3)` renvoie le dernier jour du mois situé 3 mois avant la date d'arrêté (31/07/2026) : 31/10 − 31/07 = **92 jours**. La formule reste juste quel que soit le mois.

**Le tableau croisé dynamique (TCD)** — pour vérifier les SOMME.SI.ENS et voir la répartition par groupe :

1. Cliquez dans la table tData → **Insertion > Tableau croisé dynamique** → nouvelle feuille.
2. **Lignes** : Service ; **Colonnes** : Groupe ; **Valeurs** : Somme de Montant.
3. **Filtre** : Date ≤ 31/10/2026 (ou un **segment chronologique** : Insertion > Chronologie).
4. Pour le poids du personnel : clic droit sur une valeur → **Afficher les valeurs > % du total de la ligne** : la colonne GII donne directement le poids du personnel (brut, avant retraitement).
5. Après chaque import du mois : **Données > Actualiser tout**.

Le TCD sert de **contrôle** : son total général doit être égal à la somme des SOMME.SI.ENS du tableau de bord et au total des charges de la balance analytique.

**Les feux avec la mise en forme conditionnelle** :

- Sur une cellule texte (« Vert », « Orange », « Rouge ») : **Accueil > Mise en forme conditionnelle > Règles de mise en surbrillance des cellules > Texte qui contient** « Rouge » → remplissage rouge clair, etc.
- Ou directement sur la valeur numérique : **Mise en forme conditionnelle > Jeux d'icônes > 3 feux de signalisation**, puis **Gérer les règles > Modifier** : type **Nombre** (et non Pourcentage, qui serait un centile de la plage), valeurs seuils 0,95 et 0,90 pour le taux d'activité. Pour un indicateur où « plus petit = mieux » (délai fournisseurs, écart budgétaire), cliquez sur **Inverser l'ordre des icônes**.

## 4. Points d'attention / pièges

- **Indicateurs non retraités** : amortissements passés au 31/12, frais de siège trimestriels, CNR encaissés non dépensés faussent les feux.
- **Cumul ≠ mois** : un taux d'activité calculé sur le seul mois d'octobre peut être très différent du cumul (vacances, absences). Affichez le **cumul**, et le mois en complément si utile.
- **Pourcentage dans les jeux d'icônes** : par défaut, Excel calcule les seuils en « Pourcentage » **de la plage** (et non de la valeur) : il faut choisir le type **Nombre**.
- **Plages entières (F:F)** dans SOMME.SI.ENS : pratiques, mais à éviter si l'onglet contient des totaux en bas de colonne (double compte). Préférez une **table Excel** (tData[Montant]).
- **Trésorerie « brute »** : ne pas oublier l'argent déjà promis (CNR, fonds dédiés des projets, tranche versée d'avance) : il est en banque, mais il n'est pas disponible.
- **Seuils** : fixés avec la directrice, stables dans l'année, écrits en bas du tableau.

## 5. Ce qu'un senior ferait en plus

- **Une page, toujours la même** : même ordre, mêmes seuils, même date d'envoi (par exemple le 10 du mois suivant). La régularité vaut plus que la sophistication.
- **Ajouter une projection de fin d'année** par service (méthode de l'exercice E16-06) : la directrice veut savoir où l'on **va**, pas seulement où l'on est.
- **Graphique de tendance** de la trésorerie sur 12 mois glissants (courbe) : la baisse progressive depuis janvier se voit mieux qu'un chiffre isolé.
- **Fiche de définition** de chaque indicateur (formule, source, responsable, seuils) en annexe du fichier : utile pour la trésorière, le CAC et votre remplaçante pendant vos congés.
- **Proposer la délégation de signature** pour les bons à payer pendant les absences de la directrice, avec un plafond, et la double signature au-delà de 1 500 € (règle interne de la fiche).
- **Protéger le fichier** : cellules de formules verrouillées, seule la cellule B1 (date d'arrêté) et l'onglet Donnees modifiables.

**Mail d'accompagnement à Nathalie Berthier** :

```
Objet : Tableau de bord d'octobre 2026

Madame la Directrice,
Voici le tableau de bord d'octobre (une page). En résumé :
- SESSAD et emploi accompagné : budget tenu ; activité du SESSAD à 92,6 %,
  en rattrapage depuis l'arrivée du CDD.
- SAVS : dépassement de 1,28 % à fin octobre, cohérent avec le déficit
  d'environ 11 700 € prévu au 31/12.
- Délai de paiement des fournisseurs passé de 28 à 37 jours pendant vos
  congés : je vous propose une délégation de signature pour les prochaines absences.
Le fichier se met à jour en changeant la date en cellule B1 ; je vous
enverrai celui de novembre le 10/12.
L'agent comptable
```

## 6. Références

- Code de l'action sociale et des familles : cadre budgétaire des ESSMS (EPRD, ERRD, budget prévisionnel, compte administratif), objectifs d'activité fixés dans le CPOM — *textes à consulter dans leur version en vigueur*.
- Code de commerce : délais de paiement entre professionnels, pénalités de retard et indemnité forfaitaire pour frais de recouvrement de 40 € — *articles et plafonds à vérifier dans le texte en vigueur*.
- Fiche de l'association Cap Horizons 21 : places, budgets, frais de siège, règle de double signature.
- Excel : aide en ligne de Microsoft pour SOMME.SI.ENS, RECHERCHEV, RECHERCHEX, FIN.MOIS, tableaux croisés dynamiques et mise en forme conditionnelle.
