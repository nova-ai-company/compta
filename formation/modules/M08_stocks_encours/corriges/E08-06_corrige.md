# Corrigé E08-06 — Inventaire de la Pharmacie Centrale au 30/09 : démarque, périmés et péremption courte

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-06](../exercices/E08-06_perimes-pharmacie-centrale.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Quelle valeur retenir ?

| Valeur | Ce que c'est | Retenue ? |
|---|---|---|
| 412 380 € | Stock **théorique** valorisé au **prix public TTC** | **Non** : un stock se valorise au **coût d'acquisition HT** (la TVA est récupérable, et le prix de vente inclut la marge non encore réalisée). L'utiliser surévaluerait le stock d'environ 136 000 € |
| 281 640 € | Stock **théorique** au PAMP HT (prix d'achat moyen pondéré net des remises sur facture = un CMUP) | **Non** : c'est ce que le logiciel *croit* qu'il y a en stock |
| **279 120 €** | Stock **physique** compté et valorisé au PAMP HT | **Oui**, c'est le point de départ : l'inventaire physique fait foi. Le logiciel est un outil de gestion ; l'inventaire au sens du Code de commerce est le **comptage** |

Le « logiciel plus précis » du Dr Petit est en réalité **moins fiable** que le comptage : il ignore les vols, la casse, les erreurs de délivrance et de réception.

### Question 2 — La démarque

Écart physique / théorique : 279 120,00 – 281 640,00 = **– 2 520,00 €** (– 0,89 %).

- **Comptablement** : aucune écriture spécifique. En inventaire intermittent comptable, retenir le stock physique suffit : la démarque est automatiquement incluse dans la variation de stock (le coût d'achat des marchandises vendues l'absorbe). Le logiciel, lui, doit être recalé sur le physique.
- **Diligences** : une démarque inférieure à 1 % du stock est courante en officine (petits vols en parapharmacie, erreurs de saisie). On la **compare** à celle des exercices précédents et on demande une **analyse par famille** : une démarque concentrée sur les médicaments remboursables (erreurs de délivrance, de facturation tiers payant) n'a pas le même sens qu'une démarque en dermocosmétique (vol à l'étalage).
- **Stupéfiants** : l'écart est **nul** et rapproché du registre — c'est le point de contrôle réglementaire qui compte. Un écart sur les stupéfiants n'est pas une question comptable mais une obligation de déclaration aux autorités : à signaler immédiatement à la titulaire.

### Question 3 — Les périmés : sortie ou dépréciation ?

- **Médicaments périmés non repris** (2 140 + 860 = **3 000,00 €**) : ils n'ont **aucune valeur** et ont été enlevés pour destruction le 07/10 (bordereau DO-26-4471). Ils sont **exclus** du stock (valeur nulle). Une dépréciation à 100 % aboutirait au même résultat, mais l'exclusion est plus lisible pour des produits **destinés à la destruction** ; l'essentiel est la **preuve de destruction**, que le vérificateur demandera.
- **Dermocosmétique Alpina périmée** (1 520,00 €) : elle a encore une valeur — la reprise par le laboratoire à **50 %** du prix d'achat. On la maintient au stock brut et on la **déprécie de 50 %** (760,00 €). À la réception de l'avoir Alpina (fin octobre), le produit sortira du stock et l'avoir sera comptabilisé.

### Question 4 — La liste B : péremption courte et références arrêtées

Pour chaque produit, VNR = ce que l'officine encaissera réellement (net) :
- **Lait 1er âge** : sur l'historique de l'officine, 40 % du lot sera vendu avant péremption, 60 % sera périmé (valeur nulle) → dépréciation de 60 %. On utilise une **statistique propre à l'officine**, pas un forfait arbitraire.
- **Solaires « formule 2026 »** : vente certaine mais à **50 % du prix de vente HT habituel**. Prix habituel HT = 1,75 × PAMP → prix soldé = 0,875 × PAMP, inférieur au coût → dépréciation de 12,5 % (les coûts de vente en officine sont négligeables ici).
- **Tests antigéniques** : 5 mois de vente avant péremption (octobre à février) × 10 boîtes = 50 boîtes vendues ; 130 boîtes seront périmées → dépréciation de 130 boîtes.

## 2. Calculs (détaillés, chaque montant justifié)

### Stock final brut

| | Montant |
|---|---|
| Stock physique compté (PAMP HT) | 279 120,00 € |
| – Médicaments remboursables périmés (détruits) | – 2 140,00 € |
| – Médicaments non remboursables périmés (détruits) | – 860,00 € |
| **Stock final brut (37)** | **276 120,00 €** |

### Dépréciation au 30/09/2026

| Produit | Base (PAMP HT) | Calcul | Dépréciation |
|---|---|---|---|
| Dermocosmétique Alpina périmée | 1 520,00 € | VNR = 50 % × 1 520,00 = 760,00 → 1 520,00 – 760,00 | **760,00 €** |
| Lait infantile 1er âge | 640,00 € | 60 % non vendu × 640,00 | **384,00 €** |
| Solaires formule arrêtée | 1 150,00 € | VNR = 1 150,00 × 1,75 × 50 % = 1 006,25 → 1 150,00 – 1 006,25 | **143,75 €** |
| Tests antigéniques | 342,00 € | (180 – 5 × 10) = 130 boîtes × 1,90 | **247,00 €** |
| **Total** | | | **1 534,75 €** |

Stock net au bilan : 276 120,00 – 1 534,75 = **274 585,25 €**.

### Variation de stock et dépréciation

| | Montant |
|---|---|
| Stock initial (30/09/2025) | 268 450,00 € |
| Stock final brut (30/09/2026) | 276 120,00 € |
| **Variation 6037 = SI – SF** | **– 7 670,00 €** (créditrice : le stock a augmenté) |
| Reprise dépréciation 2025 (7817) | 3 900,00 € |
| Dotation 2026 (6817) | 1 534,75 € |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6037 | Variation des stocks de marchandises | Annulation stock initial au 30/09/2025 | 268 450,00 | |
| 30/09/2026 | OD | 37 | Stocks de marchandises | Annulation stock initial au 30/09/2025 | | 268 450,00 |
| 30/09/2026 | OD | 37 | Stocks de marchandises | Stock final au 30/09/2026 (inventaire physique PAMP HT, hors périmés détruits) | 276 120,00 | |
| 30/09/2026 | OD | 6037 | Variation des stocks de marchandises | Stock final au 30/09/2026 | | 276 120,00 |
| 30/09/2026 | OD | 397 | Dépréciations des stocks de marchandises | Reprise dépréciation au 30/09/2025 | 3 900,00 | |
| 30/09/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise dépréciation au 30/09/2025 | | 3 900,00 |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation stocks au 30/09/2026 (Alpina, lait 1er âge, solaires, tests) | 1 534,75 | |
| 30/09/2026 | OD | 397 | Dépréciations des stocks de marchandises | Dépréciation stocks au 30/09/2026 | | 1 534,75 |
| | | | | **Totaux** | **550 004,75** | **550 004,75** |

Le 6037 est **créditeur** de 7 670,00 € : le stock a augmenté de 7 670,00 € sur l'exercice ; une partie des achats n'a pas été vendue, ce qui **diminue** le coût d'achat des marchandises vendues (et augmente la marge).

## 4. Points d'attention / pièges

- **Prix public TTC** : piège n° 1 en officine. Le logiciel affiche les deux colonnes ; seule la valeur **au prix d'achat HT net** est une valeur de stock. Écart ici : 412 380,00 – 276 120,00 = **136 260,00 €** de stock (et donc de résultat) fictif.
- **PAMP « net des remises sur facture »** : les remises **arrière** (ristournes de fin d'année, voir E02-09) réduisent aussi le coût d'acquisition des produits encore en stock. Si elles sont significatives sur les familles concernées (génériques), le stock doit être minoré en conséquence — point de méthode à documenter et à appliquer de façon permanente.
- **Périmés détruits** : exclus du stock **avec preuve** (bordereau d'enlèvement) ; sans preuve, l'administration peut considérer qu'il s'agit d'une minoration de stock.
- **Pas de dépréciation forfaitaire** (« 2 % du stock pour les périmés futurs ») : chaque ligne repose sur un fait (péremption, arrêt de référence, historique de ventes de l'officine).
- **Reprise et dotation** : la dépréciation 2025 (3 900,00 €) concernait des produits vendus ou détruits : elle est **reprise en totalité** ; la nouvelle dépréciation est calculée sur les produits présents au 30/09/2026.
- **Démarque et TVA** : les produits volés ou perdus ont fait l'objet d'une TVA déduite à l'achat ; les vols dûment justifiés (plainte) ne donnent en principe pas lieu à régularisation, les disparitions inexpliquées peuvent en entraîner une — sujet à garder en tête si la démarque augmente.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse au Dr Petit :**

> Bonjour Docteur,
>
> Merci pour les documents. Trois précisions :
> - le montant de **412 380 €** est votre stock au **prix public TTC** : pour le bilan, nous devons retenir le **prix d'achat HT**, et le **comptage** de la société d'inventaire (et non le stock théorique du logiciel). Votre stock au 30/09 est de **276 120 €** au coût d'achat, après sortie des médicaments périmés détruits ;
> - l'écart de 2 520 € entre le logiciel et le comptage (0,9 %) est dans la norme ; pourriez-vous nous dire sur quelles familles il se concentre ? Le résultat sur les stupéfiants (écart nul) est parfait ;
> - les périmés et produits à risque ne sont pas des « broutilles » au sens comptable : 3 000 € de produits détruits et 1 534,75 € de dépréciation. Ils sont **déductibles**, à condition de pouvoir les justifier.
>
> Merci de conserver le bordereau d'enlèvement des périmés du 07/10, l'accord de reprise Alpina et l'avoir correspondant, et de nous transmettre l'édition du logiciel par famille de l'écart d'inventaire.
>
> Bien cordialement,

**Justificatifs à conserver (dossier de travail « stocks ») :**
- rapport de la société d'inventaire signé ; édition du stock théorique ; tableau de rapprochement physique / théorique ;
- liste des périmés détaillée par produit (code, quantité, PAMP) + **bordereau d'enlèvement** ;
- accord de reprise Alpina et avoir ;
- justification de chaque dépréciation (historique de vente du lait 1er âge, courrier d'arrêt de la formule solaire, statistique de vente des tests) ;
- comparaison de la démarque et du taux de marge avec les deux exercices précédents.

**Conseil** : proposer à la titulaire une **revue trimestrielle des péremptions à 6 mois** via le logiciel (retours aux grossistes et laboratoires tant qu'ils sont possibles) : la meilleure dépréciation est celle qu'on évite.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce art. L. 123-12 (inventaire physique) et L. 123-18 (évaluation au coût).
- PCG (règlement ANC n° 2014-03 modifié) : coût d'acquisition des stocks (hors TVA récupérable, net des remises) ; biens fongibles valorisés au coût moyen pondéré ; dépréciation (comptes 397, 6817, 7817).
- CGI art. 38-3 et 39-1-5° (évaluation des stocks ; déduction des dépréciations justifiées) ; BOFiP, série BIC – produits et stocks.
- Code de la santé publique (réglementation des stupéfiants : registre, déclaration des écarts) et réglementation de l'élimination des médicaments non utilisés et périmés de l'officine.
