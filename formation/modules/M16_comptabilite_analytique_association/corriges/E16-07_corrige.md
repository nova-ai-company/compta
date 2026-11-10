# Corrigé E16-07 — Le projet expérimental « Pairs et voix » : subvention affectée et fonds dédiés

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **15059** | Cerfa n° 15059 — compte rendu financier. Le formulaire pour rendre compte de l'utilisation d'une subvention : budget prévu, dépenses réelles, écarts expliqués. |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **BQ** | Journal de banque. Journal qui reprend les mouvements du relevé bancaire. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **Cerfa** | Formulaire administratif officiel. Formulaire numéroté de l'administration (ex. : Cerfa 12156 pour demander une subvention). |
    | **FALC** | Facile à lire et à comprendre. Méthode d'écriture simple, illustrée, pensée pour les personnes avec une déficience intellectuelle. Très utilisée dans le réseau Trisomie 21. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **Compte 194** | Fonds dédiés sur subventions. Subvention reçue pour un projet précis, pas encore dépensée à la clôture (numéro à vérifier dans le plan de l'association). |
    | **Compte 487** | Produits constatés d'avance (PCA). Recette reçue cette année qui concerne l'année suivante. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 689** | Reports en fonds dédiés. On « met de côté » à la clôture la part d'une subvention affectée non encore dépensée. |
    | **Compte 789** | Utilisation des fonds dédiés. L'année où la subvention mise de côté est dépensée, on la « reprend » en produit. |
    | **Compte 6894** | Reports en fonds dédiés sur subventions (sous-compte du 689, à vérifier). |
    | **Compte 7894** | Utilisation des fonds dédiés sur subventions (sous-compte du 789, à vérifier). |
    | **charges directes** | Charge qui concerne un seul service. On sait tout de suite à quel service l'imputer (ex. : le matériel pédagogique du SESSAD). |
    | **compte rendu financier** | Rendre compte de l'usage d'une subvention. Budget prévu, dépenses réelles, écarts expliqués (Cerfa 15059). |
    | **coût complet** | Ce que coûte vraiment un service. Charges directes + part des charges communes + frais de siège. |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **Quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **section analytique** | Une « case » de la comptabilité analytique. Un service ou un projet (ex. : 20-SAVS) dans lequel on range les charges et les produits qui le concernent. |
    | **subvention affectée** | Subvention donnée pour un projet précis. Elle ne peut servir qu'à ce projet ; ce qui n'est pas dépensé va en fonds dédiés ou est remboursé. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E16-07](../exercices/E16-07_projet-pairs-et-voix-fonds-dedies.md)

*Rappel : association, fondation, personnes et chiffres fictifs.*

!!! abstract "En clair"
    1. Fonds dédiés = la partie d'une subvention **affectée** qui n'a **pas encore été dépensée** pour son objet à la clôture.
    2. Report : charge **689** au débit, fonds dédiés **19x** au crédit. Utilisation l'année suivante : **19x** au débit, produit **789** au crédit.
    3. Seules les dépenses **éligibles** selon la convention consomment la subvention. Ici, les frais de siège sont plafonnés à **3 %** : le reste (1,5 %) est payé par l'association elle-même.
    4. Une subvention de **l'année suivante** versée en avance n'est **pas** un fonds dédié : c'est un **produit constaté d'avance** (compte 487).

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Pourquoi des fonds dédiés ?

En 2025, l'association a reçu 50 000 € de la Fondation Lumen mais n'en a consommé que 25 020 €. Sans fonds dédiés, le projet afficherait un « bénéfice » de près de 25 000 € en 2025… puis un « déficit » équivalent en 2026, quand l'argent est dépensé. C'est faux : l'argent **appartient au projet**, l'association s'est engagée à le dépenser pour cet objet (sinon elle doit le rendre, article 6 de la convention). Les fonds dédiés corrigent ce décalage dans le temps.

### Dans quel ordre consommer les financements ?

C'est le point qui fait les erreurs. L'énoncé fixe trois règles :

1. La **Région** passe en premier : sa subvention est annuelle et ne peut pas être reportée. Si on la laissait « de côté », on devrait la rendre.
2. La **Fondation Lumen** finance **le reste des dépenses éligibles**.
3. Côté Lumen, on consomme d'abord **les fonds les plus anciens** (le report de 2025), puis la tranche 2026.

### Les frais de siège : ce que l'association impute ≠ ce que le financeur accepte

L'association applique sa clé (4,5 % des charges directes) pour connaître le **coût complet** de chaque section. Mais la convention Lumen (article 4) n'accepte que **3 %**. Conséquence : seuls 3 % peuvent être financés par Lumen. Les 1,5 % restants sont une vraie charge du projet, mais ils ne sont **financés par personne** : ils restent à la charge des **ressources propres** de l'association (adhésions, dons : section 90-ASSO). C'est pour cela que la section 50-PAIRS sera légèrement **déficitaire**, et c'est normal.

> 💡 Réflexe senior : avant tout calcul de fonds dédiés, relisez la **convention** et surlignez trois choses : les **dépenses éligibles**, le **plafond des frais de structure**, la **clause de reversement**. Les fonds dédiés se calculent sur ce que **le financeur** accepte, pas sur ce que l'association aimerait lui imputer.

### La tranche 2027 versée en décembre 2026

L'argent arrive en 2026, mais la convention l'attribue **au titre de 2027**. Ce n'est pas une ressource de 2026 : on ne l'enregistre pas en produit 2026 (et donc on ne la met pas non plus en fonds dédiés). C'est un **produit constaté d'avance** (487), repris en produit le 01/01/2027.

> ⚠️ Erreur classique : passer la tranche 2027 en 74 en 2026, puis la « neutraliser » par un 689. Le résultat est le même, mais le bilan et l'annexe sont faux : les fonds dédiés représentent des ressources **de l'exercice** non encore utilisées, pas des ressources d'un exercice futur.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 1 — Contrôle des fonds dédiés au 31/12/2025

| Élément 2025 | Calcul | Montant |
|---|---|---|
| Charges directes | donné | 34 000,00 |
| Frais de structure éligibles (3 %) | 34 000 × 3 % | 1 020,00 |
| **Dépenses éligibles** | 34 000 + 1 020 | **35 020,00** |
| − Région 2025 (en priorité) | | − 10 000,00 |
| **À financer par Lumen** | 35 020 − 10 000 | **25 020,00** |
| Tranche Lumen 2025 | | 50 000,00 |
| **Fonds dédiés au 31/12/2025** | 50 000 − 25 020 | **24 980,00** ✓ |

Le montant du bilan 2025 est juste.

### Question 2 — Frais de siège 2026

| Élément | Calcul | Montant |
|---|---|---|
| Quote-part imputée par l'association | 49 760 × 4,5 % | 2 239,20 |
| Part éligible Lumen | 49 760 × 3 % | 1 492,80 |
| **Part non financée (à la charge de l'association)** | 2 239,20 − 1 492,80 = 49 760 × 1,5 % | **746,40** |

### Question 3 — Utilisation et report 2026

| Étape | Calcul | Montant |
|---|---|---|
| Dépenses éligibles 2026 | 49 760 + 1 492,80 | 51 252,80 |
| − Région 2026 | | − 12 000,00 |
| **À financer par Lumen en 2026** | 51 252,80 − 12 000 | **39 252,80** |
| 1) Utilisation des fonds dédiés 2025 (789) | tout le report, car 24 980 < 39 252,80 | **24 980,00** |
| 2) Utilisation de la tranche 2026 | 39 252,80 − 24 980 | 14 272,80 |
| Tranche 2026 | | 40 000,00 |
| **Report au 31/12/2026 (689)** | 40 000 − 14 272,80 | **25 727,20** |

Contrôle global : fonds Lumen disponibles en 2026 = 24 980 + 40 000 = 64 980 ; consommés 39 252,80 ; reste 64 980 − 39 252,80 = **25 727,20** ✓.

Suivi par tranche :

| Tranche Lumen | Montant | Utilisé en 2025 | Utilisé en 2026 | Reste au 31/12/2026 |
|---|---|---|---|---|
| 2025 | 50 000,00 | 25 020,00 | 24 980,00 | 0,00 |
| 2026 | 40 000,00 | — | 14 272,80 | 25 727,20 |
| **Total** | **90 000,00** | **25 020,00** | **39 252,80** | **25 727,20** |

### Question 5 — Compte de résultat analytique 2026 de la section 50-PAIRS

| Charges | Montant | Produits | Montant |
|---|---|---|---|
| Charges directes | 49 760,00 | 74 Fondation Lumen – tranche 2026 | 40 000,00 |
| Quote-part frais de siège (4,5 %) | 2 239,20 | 74 Région 2026 | 12 000,00 |
| 6894 Report en fonds dédiés | 25 727,20 | 7894 Utilisation des fonds dédiés | 24 980,00 |
| **Total charges** | **77 726,40** | **Total produits** | **76 980,00** |
| | | **Résultat** | **− 746,40** |

Explication : le déficit de **746,40 €** est exactement la part des frais de siège **non acceptée** par la Fondation (1,5 % × 49 760). Tout le reste est financé. C'est un résultat **normal et expliqué** : il est absorbé par les ressources propres de l'association. Si le résultat de la section avait été différent de − 746,40 €, il y aurait eu une erreur dans le calcul des fonds dédiés.

Même contrôle en 2025 : 50 000 + 10 000 − (34 000 + 1 530 + 24 980) = **− 510,00 €** = 1,5 % × 34 000 ✓.

### Question 6 — Tableau de suivi des fonds dédiés — annexe 2026

*Présentation inspirée du modèle de l'annexe du règlement ANC n° 2018-06 (variation des fonds dédiés par nature de ressource) ; adaptez les intitulés au modèle utilisé par le cabinet.*

| Fonds dédiés issus de… | À l'ouverture (01/01/2026) | Reports de l'exercice (689) | Utilisations de l'exercice (789) | Transferts | À la clôture (31/12/2026) | dont fonds sans dépense au cours des deux derniers exercices |
|---|---|---|---|---|---|---|
| Subventions d'exploitation : Fondation Lumen – « Pairs et voix » | 24 980,00 | 25 727,20 | 24 980,00 | 0,00 | 25 727,20 | 0,00 |
| Subventions d'exploitation : Région – « Pairs et voix » | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **Total** | **24 980,00** | **25 727,20** | **24 980,00** | **0,00** | **25 727,20** | **0,00** |

Contrôle : 24 980 + 25 727,20 − 24 980 = 25 727,20 ✓ (= solde du 194 au bilan).

À joindre en commentaire dans l'annexe : nature du projet, durée de la convention (2025-2027), règle d'utilisation (Région d'abord, puis Lumen, fonds anciens d'abord), et mention de la **tranche 2027 reçue d'avance** (30 000 € en produits constatés d'avance).

### Question 7 — Projection 2027

| Élément 2027 | Calcul | Montant |
|---|---|---|
| Charges directes prévues | mail de la directrice | 50 000,00 |
| Frais de structure éligibles | 50 000 × 3 % | 1 500,00 |
| Dépenses éligibles | | 51 500,00 |
| − Région 2027 | | − 12 000,00 |
| À financer par Lumen en 2027 | | 39 500,00 |
| Fonds Lumen disponibles | 25 727,20 (fonds dédiés) + 30 000 (tranche 2027) | 55 727,20 |
| **Non utilisé au 31/12/2027** | 55 727,20 − 39 500 | **16 227,20** |

Au rythme actuel, **16 227,20 €** resteraient non dépensés à la fin du programme et devraient être **reversés à la Fondation** (article 6). Contrôle : sur 120 000 €, la Fondation aura financé 25 020 + 39 252,80 + 39 500 = 103 772,80 €, soit 16 227,20 € de moins ✓.

**Ce qu'il faut conseiller à la directrice, dès maintenant (pas en décembre 2027) :**

1. **Ajuster le programme 2027** (plus de sessions, de nouveaux supports FALC…) en accord écrit avec la Fondation ; ou
2. **Demander un avenant de prolongation** (par exemple jusqu'au 30/06/2028), à signer **avant le 31/12/2027** ; ou
3. Accepter de reverser le solde : il faudra alors prévoir la dette envers la Fondation à la clôture 2027 (et non plus des fonds dédiés).

## 3. Écritures comptables

### Rappel — écriture passée au 31/12/2025

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2025 | OD | 6894 | Reports en fonds dédiés sur subventions d'exploitation | Lumen – Pairs et voix – report 2025 | 24 980,00 | |
| 31/12/2025 | OD | 194 | Fonds dédiés sur subventions d'exploitation | Lumen – Pairs et voix – report 2025 | | 24 980,00 |
| | | | | **Totaux** | **24 980,00** | **24 980,00** |

### Question 4 — Écritures 2026 (section analytique 50-PAIRS)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 20/03/2026 | BQ | 512 | Banque | Fondation Lumen – conv. FL-2025-031 – tranche 2026 | 40 000,00 | |
| 20/03/2026 | BQ | 74 | Subventions d'exploitation – Fondation Lumen | Fondation Lumen – conv. FL-2025-031 – tranche 2026 | | 40 000,00 |
| 30/06/2026 | BQ | 512 | Banque | Région – subvention 2026 Pairs et voix | 12 000,00 | |
| 30/06/2026 | BQ | 74 | Subventions d'exploitation – Région | Région – subvention 2026 Pairs et voix | | 12 000,00 |
| 15/12/2026 | BQ | 512 | Banque | Fondation Lumen – tranche 2027 versée en avance | 30 000,00 | |
| 15/12/2026 | BQ | 487 | Produits constatés d'avance | Fondation Lumen – tranche 2027 versée en avance | | 30 000,00 |
| 31/12/2026 | OD | 194 | Fonds dédiés sur subventions d'exploitation | Lumen – Pairs et voix – utilisation du report 2025 | 24 980,00 | |
| 31/12/2026 | OD | 7894 | Utilisations des fonds dédiés sur subventions d'exploitation | Lumen – Pairs et voix – utilisation du report 2025 | | 24 980,00 |
| 31/12/2026 | OD | 6894 | Reports en fonds dédiés sur subventions d'exploitation | Lumen – Pairs et voix – report tranche 2026 non utilisée | 25 727,20 | |
| 31/12/2026 | OD | 194 | Fonds dédiés sur subventions d'exploitation | Lumen – Pairs et voix – report tranche 2026 non utilisée | | 25 727,20 |
| | | | | **Totaux** | **132 707,20** | **132 707,20** |

*Subdivisions des comptes 74 (par financeur), 194, 6894 et 7894 selon le plan de comptes de l'association.*

Le 01/01/2027, on extourne le produit constaté d'avance : débit 487 / crédit 74 pour 30 000,00 €.

**Pourquoi deux écritures au 31/12 et pas une seule « nette » ?** On pourrait être tenté de ne passer que la variation (25 727,20 − 24 980 = 747,20 € de report net). C'est **interdit en pratique** : l'annexe doit montrer séparément les **reports** et les **utilisations** de l'année, et le CAC contrôle chaque mouvement. On passe donc les deux écritures, en brut.

## 4. Points d'attention / pièges

- **Mettre la subvention Région en fonds dédiés** : non, elle doit être utilisée dans l'année ; elle finance en priorité les dépenses 2026.
- **Calculer les fonds dédiés sur 4,5 % de frais de siège** : le report serait sous-évalué de 746,40 € et la Fondation financerait des frais qu'elle refuse. Le CAC le verrait en comparant le compte rendu financier à la convention.
- **Oublier la reprise du report 2025** : le compte 194 gonflerait chaque année (24 980 + 25 727,20 = 50 707,20) alors que l'argent de 2025 a été dépensé.
- **Passer une seule écriture nette** : l'annexe et le contrôle deviennent impossibles.
- **Tranche 2027 en fonds dédiés** : non, c'est un produit constaté d'avance (ressource d'un exercice futur).
- **Le compte rendu financier à la Fondation** ne présente que les dépenses **éligibles** (51 252,80 € en 2026), pas le coût complet analytique (51 999,20 €).

## 5. Ce qu'un senior ferait en plus

- **Un tableau de suivi pluriannuel** par convention (onglet Excel) : tranches, dépenses éligibles par année, utilisation, reste à engager, date limite. Mis à jour à chaque clôture et à chaque compte rendu.
- **Vérifier la nature du financeur avec le CAC** : une fondation privée n'est pas une autorité publique. Selon le règlement ANC n° 2018-06, son versement peut relever des « contributions financières d'autres organismes » plutôt que des subventions d'exploitation, avec des comptes de produits et de fonds dédiés distincts. Ici, on suit le plan de comptes de l'association (compte 74, fiche de l'association) ; faites valider ce classement chaque année.
- **Mail type à Hélène Ferrand** :

```
Objet : Pairs et voix — fonds dédiés 2026

Bonjour Hélène,
- Report 2025 contrôlé : 24 980,00 € (OK).
- 2026 : dépenses éligibles 51 252,80 € (frais de structure plafonnés à 3 %
  selon l'art. 4) ; Région 12 000 € ; Lumen 39 252,80 €.
- Écritures au 31/12 : utilisation 789 = 24 980,00 € ; report 689 = 25 727,20 €.
- Tranche 2027 reçue le 15/12 : 30 000 € en 487.
- Résultat analytique 50-PAIRS : − 746,40 € (frais de siège non éligibles).
- Alerte : au rythme prévu, 16 227,20 € resteraient non utilisés fin 2027.
  Je propose d'en parler à N. Berthier pour un avenant.
Les justificatifs sont dans le dossier « Clôture 2026 / Fonds dédiés ».
```

## 6. Références

- Règlement ANC n° 2018-06 relatif aux comptes annuels des personnes morales de droit privé à but non lucratif : fonds dédiés (comptes 19x, 689, 789), contributions financières, modèle d'annexe (tableau de variation des fonds dédiés).
- PCG (règlement ANC n° 2014-03 modifié) : produits constatés d'avance (487).
- Compte rendu financier de subvention : Cerfa n° 15059 (pour les financeurs publics ; la Fondation peut avoir son propre modèle).
- Fiche de l'association Cap Horizons 21 : section 50-PAIRS, frais de siège 4,5 %.
