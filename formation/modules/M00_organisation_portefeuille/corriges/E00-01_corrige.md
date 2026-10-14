# Corrigé E00-01 — Construire son planning d'octobre à décembre 2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E00-01](../exercices/E00-01_planning-T4-2026.md)

## 1. Analyse

Un planning de senior se construit en quatre temps :
1. **La capacité réelle**, et non théorique : jours ouvrés, moins les fériés et les congés, puis seulement 80 % de ce temps, puisque le reste part en imprévus.
2. **Les contraintes dures** : échéances légales (liasses, solde d'IS, OSS, acomptes, CFE, AG) et événements qui ne se déplacent pas (rendez-vous bancaire de la Menuiserie le 16/11, formation des 3 et 4/11, congés).
3. **L'écart charge / capacité.** S'il existe, on le règle **avant** de commencer, par des reports qui ne compromettent aucune échéance légale et par des délégations à des personnes compétentes pour la tâche.
4. **Le séquencement.** On fait d'abord ce qui a l'échéance la plus proche, puis on vérifie semaine par semaine que la somme ne dépasse pas la capacité.

Deux pièges dans l'énoncé :
- **Hôtel Belle Vue (C16)** : la clôture est au 31/10/2026, mais la liasse n'est due qu'au **31/01/2027**. On peut donc reporter une partie des travaux sans risque légal, à condition que l'inventaire du 31/10 soit **bien réalisé et récupéré à la date** (ce qui ne se rattrape pas).
- **Studio Pixel (C25)** : la **lettre de mission non signée** est un risque pour le cabinet, à traiter **tout de suite** (2 h). La « situation intermédiaire » demandée avant Noël, elle, a peu d'intérêt à quelques semaines de la clôture du premier exercice (31/12/2026). On propose aux associés de faire directement le bilan en janvier.

## 2. Calculs

### 2.1 Capacité

| Élément | Calcul | Résultat |
|---|---|---|
| Jours ouvrés du 12/10 au 31/12/2026 (lundi au vendredi) | 12 semaines — dernière semaine du 28 au 31/12 = 4 jours | 59 jours |
| − Jours fériés tombant en semaine | 11/11 (mercredi) ; le 25/12 est compris dans les congés | − 1 |
| − Congés (21 au 25/12 inclus) | 5 jours | − 5 |
| **Jours travaillés** | 59 − 1 − 5 | **53 jours** |
| Heures de présence | 53 × 7 h | **371 h** |
| **Capacité productive** (80 %) | 371 × 0,80 | **296,8 h** |

### 2.2 Charge

Total des 17 lignes : 38 + 30 + 30 + 14 + 42 + 5 + 105 + 3 + 6 + 14 + 8 + 5 + 3 + 12 + 6 + 7 + 4 = **332 h**.

**Écart : 332 − 296,8 = 35,2 h de surcharge** (≈ 12 % de la capacité). Il faut arbitrer.

### 2.3 Arbitrages chiffrés

| Arbitrage | Heures | Justification | Échéance légale préservée ? |
|---|---|---|---|
| C16 Hôtel : n'effectuer en décembre que 20 h (cut-off, stocks, révision des cycles), reporter 22 h (finalisation, annexe, liasse) à la **semaine du 4/01/2027** | − 22 | Liasse au 31/01/2027 | Oui. L'inventaire du 31/10 est réalisé par le client, et Lucie récupère et contrôle les feuilles de comptage début novembre |
| C25 Studio Pixel : faire la **lettre de mission** (2 h) tout de suite, reporter la situation intermédiaire (6 h) et la remplacer par le **bilan du 1er exercice** en janvier | − 6 | Premier exercice clos le 31/12/2026, à 3 semaines près | Oui (liasse en mai 2027) |
| C12 Pharmacie : déléguer à **Lucie** le contrôle du fichier d'inventaire (périmés, quantités négatives, rapprochement des quantités et des prix) | − 8 | Travail de pointage, sans révision : conforme à son mail | Oui |
| Contrôle des avis de CFE (télécharger, comparer à N-1, alerter si l'écart dépasse 10 %) délégué à Lucie | − 3 | Tâche de pointage | Oui (15/12) |
| **Total** | **− 39** | | |

Charge après arbitrage : 332 − 39 = **293 h**, pour une capacité de 296,8 h, soit **3,8 h de marge** en plus de la réserve de 20 %. Lucie utilise 11 h sur les 20 h qu'elle propose (10 h par mois en novembre et en décembre). Il lui reste 9 h pour un imprévu.

> On **ne reporte pas** le prévisionnel de la Menuiserie (C24). Ce n'est pas une échéance légale, mais l'enjeu pour le client est vital : un financement à négocier avec la banque et un risque pour la continuité de l'exploitation. On ne reporte pas non plus les rendez-vous de pré-bilan, parce que les décisions doivent être prises **avant** le 31/12 (investissements, rémunération).

### 2.4 Classement urgence / importance

| | Urgent (≤ 4 semaines ou date fixe proche) | Pas urgent |
|---|---|---|
| **Important — légal** | 8 OSS T3 (31/10) ; 4 FitClub (liasse 30/11) ; 12 acomptes IS (15/12) ; 13 CFE (15/12) ; 7 CA3 mensuelles | 1, 2, 3 liasses 30/09 (31/12) ; 6 AG Petit Zinc (31/12) ; 5 Hôtel (31/01) |
| **Important — client / cabinet** | 10 prévisionnel C24 (banque le 16/11) ; 9 Paul Durand (TVA due depuis le dépassement) ; 11 lettre de mission C25 (risque pour le cabinet) ; 16 formation (date fixe, PA) | 14 pré-bilans ; 15 lettres de pièces ; 17 revues |
| **Moins important** | — | 11 situation intermédiaire C25 (reportée) |

## 3. Écritures comptables

Sans objet : il s'agit d'un exercice d'organisation. Le livrable est le planning ci-dessous.

### Planning semaine par semaine (heures productives)

| Semaine | Capacité | Échéances légales de la semaine (portefeuille) | Tenue + CA3 | Autres travaux | Total |
|---|---|---|---|---|---|
| S42 — 12-16/10 | 28 | DSN 15/10 (pôle social) ; **solde IS C04 15/10** (vérifier le paiement) ; début des CA3 de septembre | 10 | C21 FitClub 10 ; C03 Garage 8 | 28 |
| S43 — 19-23/10 | 28 | **CA3 de septembre** (15-24/10) | 10 | **C09 OSS T3** 3 ; C21 4 ; C03 11 | 28 |
| S44 — 26-30/10 | 28 | **OSS T3 le 31/10** ; URSSAF T3 C17 (31/10) ; inventaire C16 (31/10, fait par le client) | 10 | C03 11 ; **C17 Paul** 6 ; revue C21 1 | 28 |
| S45 — 02-06/11 | 28 | — | 10 | **Formation PA** 7 ; C24 prévisionnel 11 | 28 |
| S46 — 09-13/11 (férié le 11) | 22,4 | DSN 15/11 (dimanche, à anticiper) | 7 | C24 3 (finalisation avant le 16/11) ; C03 8 (fin) ; revue C03 1 ; **lettre de mission C25** 2 | 21 (marge 1,4) |
| S47 — 16-20/11 | 28 | **CA3 d'octobre** ; RDV banque C24 le 16/11 | 10 | C12 Pharmacie 14 ; C04 AG (rapport de gestion, convocations) 4 | 28 |
| S48 — 23-27/11 | 28 | **Liasse C21 au 30/11** (télétransmise en S44, vérifier l'accusé de réception) | 10 | C12 8 (fin) ; revue C12 1 ; C13 Atelier 9 | 28 |
| S49 — 30/11-04/12 | 28 | — | 10 | C13 14 ; lettres de pièces 31/12 : 4 | 28 |
| S50 — 07-11/12 | 28 | Préparation des **acomptes IS du 15/12**, de la **CFE du 15/12**, de l'**acompte CA12** (C01, C20) | 10 | C13 7 (fin) ; revue C13 1 ; lettres de pièces 2 ; acomptes IS 5 ; pré-bilans 3 | 28 |
| S51 — 14-18/12 | 28 | **15/12** : acomptes IS, CFE, **solde IS C21** ; DSN ; **CA3 de novembre** ; télétransmission des liasses **C03, C12, C13** | 10 | pré-bilans 9 ; AG C04 (PV) 1 ; C16 Hôtel 8 | 28 |
| S52 — 21-25/12 | 0 | Congés. Tout ce qui est dû avant le 31/12 est **déposé en S51** | — | — | 0 |
| S53 — 28-31/12 | 22,4 | **Date limite des liasses 30/09 et de l'AG C04 : déjà faites** | 8 | C16 Hôtel 12 | 20 (marge 2,4) |
| **Total** | **296,8** | | **105** | **188** | **293** |

## 4. Points d'attention / pièges

- **Ne jamais caler une échéance légale la dernière semaine avant des congés** : les liasses C03, C12 et C13 sont télétransmises en S51, et non le 31/12.
- **Le 15/11/2026 tombe un dimanche** : la DSN est à transmettre le vendredi précédent (le pôle social en est responsable, mais vérifiez les variables de paie transmises).
- Le report de l'Hôtel suppose que l'**inventaire physique au 31/10** soit fait et documenté. C'est le seul point non rattrapable de ce dossier.
- Ne pas planifier à 100 % : la capacité est déjà réduite à 80 %, et il reste en plus 3,8 h de marge et 9 h de Lucie.
- **La délégation a des limites** : Lucie fait du pointage, pas de la révision (pièce 3). La conclusion sur la dépréciation des périmés de la Pharmacie reste la vôtre.
- Paul Durand (C17) n'a pas d'échéance légale « affichée », mais la TVA est due **depuis le jour du dépassement** du seuil. Chaque mois de retard aggrave les intérêts et la régularisation, d'où son traitement en S44.

## 5. Ce qu'un senior ferait en plus

**Mail à Hélène (≤ 10 lignes)** :

> Objet : Planning T4 2026 — arbitrages à valider
>
> Hélène, ma capacité jusqu'au 31/12 est de 297 h productives (53 jours × 7 h × 80 %), pour 332 h de travaux recensés.
> Je propose : (1) Hôtel Belle Vue : 20 h en décembre, finalisation et liasse la semaine du 4/01 (échéance 31/01) ; (2) Studio Pixel : lettre de mission signée en novembre, pas de situation intermédiaire, bilan du 1er exercice en janvier ; (3) Lucie (11 h) : contrôle du fichier d'inventaire de la Pharmacie et des avis de CFE.
> Toutes les échéances légales sont tenues : liasses C03, C12 et C13 télétransmises avant mes congés (S51), OSS au 31/10, acomptes IS et CFE au 15/12.
> Marge restante : 3,8 h. Le prévisionnel de la Menuiserie est prioritaire (banque le 16/11).
> Pouvez-vous valider, et prévenir les associés de Studio Pixel ?

Autres réflexes :
- Saisir le planning dans l'**outil de suivi** du cabinet, avec des alertes à J-5 sur chaque échéance légale.
- Faire un **point du lundi** (15 min) : le prévu de la semaine passée contre le réalisé, puis l'ajustement des semaines suivantes.
- Prévoir dès maintenant la **semaine du 4 janvier** (C16, CA3 de décembre avec les taxes sur véhicules, soldes d'IS au 15/01 pour C03, C12 et C13).

## 6. Références
- CGI, art. 1668 (acomptes et solde d'IS) ; calendrier fiscal DGFiP 2026-2027 (**dates à vérifier chaque année**).
- Code de commerce : approbation des comptes dans les 6 mois de la clôture (C04 : clôture 30/06/2026 → AG au plus tard le 31/12/2026).
- Cours M00, § 5 (calendrier), § 6 (saison fiscale) et § 8 (priorisation).
