# Corrigé E06-02 — La rénovation des chambres 101 à 110 : remplacement de composants

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-02](../exercices/E06-02_renovation-chambres-hotel-belle-vue.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — Reconnaître un remplacement de composant.** Les agencements des chambres (AG-12) et le mobilier (MO-07) sont suivis **séparément** dans le fichier : ce sont des composants / biens distincts. Leur remplacement complet entraîne deux mouvements **indissociables** : entrée des nouveaux biens **et sortie des anciens**. M. Garnier n'a fait que le premier.

**Étape 2 — Qualifier chaque facture (question 1)**

| Facture | Nature | Traitement | Compte | Justification |
|---|---|---|---|---|
| F1 Dépose / évacuation 8 500 | Coût lié à la **sortie** des anciens agencements | **Charge** | 6152 Entretien et réparations sur biens immobiliers | Le démontage d'un bien que l'entreprise utilisait ne fait pas partie du coût du nouveau bien : il se rattache à la sortie de l'ancien (cf. cours § 2.1) |
| F2 Travaux 215 000 | Nouveaux agencements | **Immobilisation** | 2135 | Composant de remplacement |
| F3 Architecte d'intérieur 18 000 | Honoraires directement attribuables | **Immobilisation** | 2135 | Coût de conception et de suivi du nouveau composant |
| F4 Peinture des couloirs 6 800 | **Entretien** de parties communes, sans lien avec le composant chambres | **Charge** | 6152 | Remise en état, ni nouvel actif ni prolongation de durée |
| F5 Mobilier 52 000 | Nouveau mobilier | **Immobilisation** | 2184 | |
| F6 Téléviseurs 10 × 450 | Équipement des chambres | **Immobilisation** | 2188 (autres immobilisations corporelles — équipements audiovisuels) | Valeur unitaire < 500 € HT, **mais** la tolérance fiscale de faible valeur est une faculté et la doctrine l'écarte pour un **équipement d'ensemble** (renouvellement complet de l'équipement de 10 chambres). Comptablement, 4 500 € d'équipements durables d'une rénovation globale ne sont pas « non significatifs ». Position du cabinet : **immobiliser** |

**Étape 3 — Les anomalies (question 2)**
- **F1 à 10 %** : le taux réduit de 10 % vise les travaux dans des **locaux d'habitation** achevés depuis plus de 2 ans. Un **hôtel** n'est pas un local d'habitation : le taux applicable est **20 %**. La TVA déductible est limitée à celle **légalement due et correctement facturée** : demander à Démolition Express une facture rectificative (avoir + nouvelle facture à 20 %, soit 1 700 € de TVA, TTC 10 200 €). En attendant, on ne déduit que les 850 € facturés ; les 850 € complémentaires seront déduits et payés à réception de la facture rectificative.
- **F2 : retenue de garantie** de 5 % du TTC = 258 000 × 5 % = **12 900 €** à payer en avril 2027 (après la réception sans réserve). C'est une **dette fournisseur d'immobilisation** à isoler (sous-compte), pas une réduction du coût. La facture porte la mention « **TVA acquittée d'après les débits** » : pour des travaux immobiliers (prestations de services), la TVA est normalement exigible chez le prestataire à l'encaissement ; grâce à l'option pour les débits, l'hôtel peut déduire **toute** la TVA dès la facture, y compris celle afférente à la retenue de garantie. Sans cette option, la TVA de la retenue ne serait déductible qu'au paiement.
- **Pièce 3** : la facture de cession du mobilier usagé est correcte (TVA 20 % sur un bien meuble dont la TVA avait été déduite). La créance n'est pas encaissée : 462, relance à suivre.

**Étape 4 — Date de sortie.** Les anciens biens sont amortis **jusqu'au 04/01/2026 inclus** (dépose à partir du 05/01) : du 01/11/2025 au 04/01/2026 = 30 + 30 + 4 = **64 jours**.

## 2. Calculs (détaillés, chaque montant justifié)

**Anciens biens (question 3)**

| | AG-12 Agencements | MO-07 Mobilier |
|---|---:|---:|
| Valeur brute | 180 000,00 | 45 000,00 |
| Annuité | 180 000 / 15 = 12 000,00 | 45 000 / 10 = 4 500,00 |
| Cumul au 31/10/2025 | 108 000,00 | 27 000,00 |
| Dotation complémentaire (64/360) | 12 000 × 64/360 = **2 133,33** | 4 500 × 64/360 = **800,00** |
| Cumul à la sortie | 110 133,33 | 27 800,00 |
| **VNC sortie (675)** | **69 866,67** | **17 200,00** |

Résultat de sortie : 1 500,00 (775) – (69 866,67 + 17 200,00) (675) = **– 85 566,67 €**.
(Le prix du brocanteur porte sur une partie du mobilier ; le reste a été mis à la déchetterie : tout le bien MO-07 sort en une fois.)

**Nouveaux biens (question 4)** — mise en service 01/04/2026 → 7 mois jusqu'au 31/10/2026 (210/360).

| Bien | Coût | Durée | Annuité | Dotation 2025/2026 (7/12) |
|---|---:|---:|---:|---:|
| Agencements chambres 101-110 (F2 + F3) | 233 000,00 | 12 ans | 19 416,67 | **11 326,39** |
| Mobilier chambres (F5) | 52 000,00 | 8 ans | 6 500,00 | **3 791,67** |
| Téléviseurs (F6) | 4 500,00 | 5 ans | 900,00 | **525,00** |
| **Total** | **289 500,00** | | | **15 643,06** |

Charges d'entretien à reclasser : F1 8 500 + F4 6 800 = **15 300,00 €**.

## 3. Écritures comptables

Les factures F1 à F6 ont déjà été saisies par M. Garnier (TVA comprise, correctement ventilée 44562/44566 sous réserve de F1). On passe les écritures de **correction**, puis les sorties et les dotations.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/01/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotation compl. AG-12 et MO-07 au 04/01/2026 | 2 933,33 | |
| 05/01/2026 | OD | 28135 | Amortissements des agencements des constructions | Dotation compl. AG-12 (64 j) | | 2 133,33 |
| 05/01/2026 | OD | 28184 | Amortissements du mobilier | Dotation compl. MO-07 (64 j) | | 800,00 |
| 05/01/2026 | OD | 28135 | Amortissements des agencements des constructions | Sortie AG-12 | 110 133,33 | |
| 05/01/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie AG-12 (remplacement composant) | 69 866,67 | |
| 05/01/2026 | OD | 2135 | Agencements des constructions | Sortie AG-12 | | 180 000,00 |
| 05/01/2026 | OD | 28184 | Amortissements du mobilier | Sortie MO-07 | 27 800,00 | |
| 05/01/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie MO-07 (cession + rebut) | 17 200,00 | |
| 05/01/2026 | OD | 2184 | Mobilier | Sortie MO-07 | | 45 000,00 |
| 08/01/2026 | VT | 462 | Créances sur cessions d'immobilisations | Fact. HBV-DIV-2026-002 Brocante des Pentes | 1 800,00 | |
| 08/01/2026 | VT | 775 | Produits des cessions d'éléments d'actif | Cession mobilier usagé | | 1 500,00 |
| 08/01/2026 | VT | 44571 | TVA collectée | Cession mobilier usagé 20 % | | 300,00 |
| 31/03/2026 | OD | 6152 | Entretien et réparations sur biens immobiliers | Reclass. F1 dépose + F4 peinture couloirs | 15 300,00 | |
| 31/03/2026 | OD | 2135 | Agencements des constructions | Reclass. F1 + F4 (charges) | | 15 300,00 |
| 31/03/2026 | OD | 2188 | Autres immobilisations corporelles – TV | Reclass. F6 téléviseurs (équipement d'ensemble) | 4 500,00 | |
| 31/03/2026 | OD | 6063 | Fournitures d'entretien et de petit équipement | Reclass. F6 | | 4 500,00 |
| 31/03/2026 | OD | 404RHL | Fournisseur d'immo. Rénov'Habitat Lyonnais | Isolement retenue de garantie 5 % F2 | 12 900,00 | |
| 31/03/2026 | OD | 404RG | Fournisseurs d'immo. – retenues de garantie | RG F2 libérable 04/2027 | | 12 900,00 |
| 31/10/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Dotations nouveaux biens ch. 101-110 (7 mois) | 15 643,06 | |
| 31/10/2026 | OD | 28135 | Amortissements des agencements des constructions | Agencements ch. 101-110 | | 11 326,39 |
| 31/10/2026 | OD | 28184 | Amortissements du mobilier | Mobilier ch. 101-110 | | 3 791,67 |
| 31/10/2026 | OD | 28188 | Amortissements des autres immo. corporelles | Téléviseurs | | 525,00 |
| | | | | **Totaux** | **278 076,39** | **278 076,39** |

À réception de la facture rectificative de Démolition Express (TVA 20 %) : D 44566 850,00 / C 401 850,00 (complément de TVA, la charge HT reste 8 500 €).

Les dotations de l'exercice pour les **anciens** biens se limitent aux 2 933,33 € ci-dessus : vérifier que le logiciel d'immobilisations ne calcule pas une annuité complète (12 000 + 4 500) sur des biens sortis.

## 4. Points d'attention / pièges

**Question 6 — si l'on avait suivi la saisie de M. Garnier**

| Poste (exercice clos le 31/10/2026) | Saisie Garnier | Correct |
|---|---:|---:|
| Charges d'entretien (F1 + F4) | 0,00 (immobilisées) | 15 300,00 |
| Téléviseurs en charge | 4 500,00 | 0,00 |
| Dotations anciens biens (non sortis : annuités complètes) | 16 500,00 | 2 933,33 |
| Dotations nouveaux agencements (248 300 / 12 × 7/12) | 12 070,14 | 11 326,39 |
| Dotations mobilier et TV | 3 791,67 | 4 316,67 |
| VNC des biens sortis (675) | 0,00 | 87 066,67 |
| Produit de cession (775) | – 1 500,00 | – 1 500,00 |
| **Total des charges nettes** | **35 361,81** | **119 443,06** |

→ Résultat **surévalué de 84 081,25 €** avec la saisie du président, et un actif gonflé : les anciens agencements et l'ancien mobilier (VNC 87 066,67 €) continueraient de figurer au bilan alors qu'ils sont à la déchetterie.

**Autres pièges**
- Ne pas confondre **remplacement** (sortie + entrée) et **dépense ultérieure** sur un bien existant (une salle de bains ajoutée dans une chambre qui n'en avait pas : on immobilise sans sortie).
- Si le composant remplacé **n'avait pas été identifié** à l'origine (agencements noyés dans « Constructions »), il faut **estimer** sa valeur brute et ses amortissements (par exemple en partant du coût actuel déflaté) pour le sortir.
- Les **pertes d'exploitation** pendant la fermeture (chambres non louées, salaires du personnel) ne sont jamais incorporées au coût.
- Travaux à cheval sur une clôture : passer par **231 Immobilisations corporelles en cours** (non amorties) jusqu'à la mise en service.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à Olivier Garnier**

> Bonjour Monsieur Garnier,
>
> Merci pour la saisie des factures de rénovation. Nous avons fait trois corrections : la dépose des anciens agencements et la peinture des couloirs sont des charges d'entretien (15 300 €) ; les téléviseurs, qui font partie du renouvellement complet des chambres, sont immobilisés ; enfin, les anciens agencements et l'ancien mobilier doivent sortir du bilan pour leur valeur résiduelle (87 067 €). Le résultat de l'exercice sera donc inférieur d'environ 84 000 € à ce que la saisie laissait apparaître.
>
> Deux actions de votre côté : demandez à Démolition Express une facture rectificative au taux de 20 % (un hôtel n'est pas un logement, le taux de 10 % ne s'applique pas) ; relancez la Brocante des Pentes pour les 1 800 € TTC.
>
> Enfin, la retenue de garantie de 12 900 € due à Rénov'Habitat sera à payer après le 31/03/2027 si aucune réserve n'est levée : pensez à nous signaler d'éventuelles malfaçons avant cette date.

**Contrôles et documentation**
- Mettre à jour le fichier : clôturer AG-12 et MO-07 (date de sortie 05/01/2026) ; créer 3 fiches (agencements 233 000 €, mobilier 52 000 €, TV 4 500 €).
- Rapprocher 675 et 775 du fichier (sorties de l'exercice) et préparer le tableau de variation des immobilisations (2054).
- Programmer dans le dossier permanent un **plan pluriannuel** de rénovation des 28 chambres : il permettra d'anticiper les sorties de composants des étages suivants.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : approche par composants, remplacement d'un composant et sortie de l'élément remplacé ; dépenses ultérieures ; coût d'acquisition (éléments exclus).
- CGI, art. 279-0 bis : taux de 10 % pour les travaux dans les **locaux d'habitation** achevés depuis plus de deux ans (non applicable à un hôtel).
- CGI, art. 269-2-c : exigibilité de la TVA sur les prestations de services à l'encaissement ; option pour le paiement d'après les débits.
- BOFiP, BIC – Charges – immobilisations de faible valeur (tolérance de 500 € HT).
- Loi n° 71-584 du 16 juillet 1971 : retenue de garantie sur marchés de travaux.
