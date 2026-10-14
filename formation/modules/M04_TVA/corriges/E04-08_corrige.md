# Corrigé E04-08 — Quatre taux de TVA à l'officine

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-08](../exercices/E04-08_pharmacie-quatre-taux.md)

## 1. Analyse

**a) Les taux à l'officine**

| Taux | Produits |
|---|---|
| **2,1 %** | Médicaments **remboursables** par la sécurité sociale (et produits sanguins, certains médicaments soumis à autorisation) |
| **5,5 %** | Appareillages et équipements pour personnes handicapées, protections hygiéniques féminines, produits alimentaires (laits infantiles, compléments selon leur nature), masques et gels dans les conditions fixées par la loi |
| **10 %** | Médicaments **non remboursables** (vendus sans ordonnance ou déremboursés) |
| **20 %** | Parapharmacie, cosmétiques, hygiène, matériel non spécifique, **prestations de services** de la pharmacie (coopération commerciale, location de matériel selon le cas) |

**b) Le déremboursement change le taux.** Un médicament déremboursé n'est plus « remboursable » : il passe de 2,1 % à **10 %** à la date d'effet du déremboursement (01/09/2026). La TVA légalement due est celle du **taux applicable**, même si le ticket et le LGO affichent 2,1 % : la pharmacie doit reverser la différence (elle ne peut pas la récupérer auprès des clients). D'où l'importance de la **mise à jour de la base de données** du LGO.

**c) L'avoir du laboratoire est une ristourne** (remise de fin d'année calculée sur le CA réalisé) : c'est une **réduction du prix d'achat** des marchandises. Pour la pharmacie, elle se comptabilise en **609 (6097) « RRR obtenus sur achats de marchandises »** et **diminue la TVA déductible** à hauteur de la TVA incluse dans le prix initial. La TVA d'une réduction de prix suit le **taux des produits auxquels elle se rapporte** : 2,1 % pour la part relative aux produits remboursables, 10 % pour les non remboursables. **Il faut ventiler** : la TVA correcte est de 63 € + 84 € = **147 €**, pas 768 €.
Si la pharmacie comptabilisait l'avoir tel quel, elle réduirait sa TVA déductible de 768 € au lieu de 147 € : elle **perdrait 621 €** ; inversement, le laboratoire augmenterait indûment sa TVA déductible… et le contrôle de l'un révélerait l'incohérence chez l'autre. **Il faut demander au laboratoire un avoir rectificatif.** (En attendant, la pharmacie ne peut retenir que la TVA réellement afférente à la réduction : 147 €.)

**d) La coopération commerciale est un service rendu par la pharmacie** (mise en avant en vitrine) au laboratoire, distinct de l'achat de marchandises : la pharmacie **facture** ce service avec **TVA à 20 %** et l'enregistre en **produit** (706 ou 708). Ce n'est pas une remise. La frontière est surveillée (et encadrée par le droit de la concurrence) : un service fictif masquant une remise serait requalifié — un contrat écrit et des preuves de réalisation (photos de la vitrine, dates) sont indispensables.

## 2. Calculs

**Ventes de septembre — ventilation corrigée**

| Taux | TTC LGO | Correction DOLORYX | TTC corrigé | HT | TVA |
|---|---|---|---|---|---|
| 2,1 % | 142 380,00 | – 1 230,00 | 141 150,00 | 138 246,82 | 2 903,18 |
| 5,5 % | 9 917,00 | | 9 917,00 | 9 400,00 | 517,00 |
| 10 % | 21 120,00 | + 1 230,00 | 22 350,00 | 20 318,18 | 2 031,82 |
| 20 % | 26 280,00 | | 26 280,00 | 21 900,00 | 4 380,00 |
| **Total** | **199 697,00** | | **199 697,00** | **189 865,00** | **9 832,00** |

**Incidence DOLORYX** : à 2,1 %, 1 230 € TTC → TVA 25,30 € ; à 10 % → TVA 111,82 €. **TVA supplémentaire : 86,52 €** pour septembre, à la charge de la pharmacie (marge réduite). À vérifier : le prix de vente a-t-il été adapté au nouveau statut ?

**TVA collectée totale** : 9 832,00 (ventes) + 300,00 (coopération commerciale) = **10 132,00 €**.

**TVA déductible**

| Élément | TVA |
|---|---|
| Achats 2,1 % | 2 129,40 |
| Achats 5,5 % | 335,50 |
| Achats 10 % | 1 130,00 |
| Achats 20 % | 2 560,00 |
| Frais généraux 20 % | 1 120,00 |
| Sous-total | 7 274,90 |
| – Ristourne Alpin Santé (3 000 × 2,1 % + 840 × 10 %) | – 147,00 |
| **TVA déductible nette (ligne 20)** | **7 127,90** |

**TVA nette due** : 10 132,00 – 7 127,90 = **3 004,10 €**.

**CA3 de septembre (extrait)**

| Ligne | Base HT | TVA |
|---|---|---|
| A1 — Ventes, prestations de services | 191 365 (189 865 + 1 500) | |
| 08 — 20 % | 23 400 (21 900 + 1 500) | 4 680,00 |
| 9B — 10 % | 20 318 | 2 031,82 |
| 09 — 5,5 % | 9 400 | 517,00 |
| Ligne dédiée au taux de 2,1 % (France métropolitaine) | 138 247 | 2 903,18 |
| 16 — Total TVA brute | | 10 132,00 |
| 20 — Autres biens et services | | 7 127,90 |
| 23 — Total TVA déductible | | 7 127,90 |
| **28 — TVA nette due** | | **3 004,10** |
*Numérotation à contrôler sur le formulaire millésimé ; bases arrondies à l'euro.*

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | VT | 4111 | Clients – organismes de tiers payant | Ventes 09/2026 – part tiers payant | 118 400,00 | |
| 30/09/2026 | VT | 5115 | Cartes bancaires à encaisser | Ventes 09/2026 – CB | 70 297,00 | |
| 30/09/2026 | VT | 531 | Caisse | Ventes 09/2026 – espèces | 11 000,00 | |
| 30/09/2026 | VT | 70711 | Ventes médicaments remboursables 2,1 % | Ventes 09/2026 (DOLORYX reclassé) | | 138 246,82 |
| 30/09/2026 | VT | 70712 | Ventes 5,5 % | Ventes 09/2026 | | 9 400,00 |
| 30/09/2026 | VT | 70713 | Ventes médicaments non remboursables 10 % | Ventes 09/2026 (dont DOLORYX) | | 20 318,18 |
| 30/09/2026 | VT | 70714 | Ventes parapharmacie 20 % | Ventes 09/2026 | | 21 900,00 |
| 30/09/2026 | VT | 44571 | TVA collectée (2,1 / 5,5 / 10 / 20 %) | 2 903,18 + 517,00 + 2 031,82 + 4 380,00 | | 9 832,00 |
| 30/09/2026 | VT | 411ALP | Client Laboratoires Alpin Santé | PC-2026-031 coopération commerciale | 1 800,00 | |
| 30/09/2026 | VT | 706 | Prestations de services | PC-2026-031 coopération commerciale | | 1 500,00 |
| 30/09/2026 | VT | 44571 | TVA collectée 20 % | PC-2026-031 | | 300,00 |
| 15/09/2026 | AC | 401ALP | Fournisseur Laboratoires Alpin Santé | AS-RFA-2026-0412 (TVA ventilée, avoir rectificatif demandé) | 3 987,00 | |
| 15/09/2026 | AC | 6097 | RRR obtenus sur achats de marchandises | Ristourne 2026 Alpin Santé | | 3 840,00 |
| 15/09/2026 | AC | 44566 | TVA déductible sur ABS | TVA sur ristourne : 3 000 × 2,1 % + 840 × 10 % | | 147,00 |
| | | | | **Totaux** | **205 484,00** | **205 484,00** |

## 4. Points d'attention / pièges

- **Remises arrière de fin d'année** : à la clôture du 30/09, estimer les **ristournes acquises** sur l'exercice et non encore reçues (avoirs à recevoir : 4098 + TVA en 44567/44587 selon le plan du cabinet), en fonction des contrats et du CA réalisé avec chaque laboratoire et grossiste.
- **Ventilation par taux** : toujours exiger des fournisseurs des avoirs ventilés par taux (un avoir « global à 20 % » sur des produits à 2,1 % est faux pour les deux parties).
- **Base de données du LGO** : contrôler les changements de statut (déremboursements, nouvelles spécialités) chaque mois — l'enjeu peut être important sur un produit très vendu.
- **Tiers payant** : rapprocher le 4111 des retours NOEMIE (paiements et rejets) ; un rejet non suivi devient une créance douteuse.
- **Coopération commerciale** : contrat écrit, service réel et distinct, prix proportionné ; sinon requalification en remise (TVA au taux des produits, pas 20 %).

## 5. Ce qu'un senior ferait en plus

- **Courrier au laboratoire** demandant l'avoir rectificatif ventilé (2,1 % / 10 %).
- **Message au Dr Petit** : « Le LGO a laissé DOLORYX à 2,1 % alors qu'il est à 10 % depuis son déremboursement au 1er septembre : nous corrigeons la TVA de septembre (+ 86,52 €) ; pouvez-vous faire mettre à jour la base produits et vérifier votre prix de vente ? L'avoir Alpin Santé est une réduction de vos achats, la facture vitrine est un chiffre d'affaires de services à 20 %. »
- **Contrôle de cohérence annuel** : marge brute par taux (ventes HT / achats HT par taux, après stocks) comparée aux années précédentes et aux ratios de la profession ; un taux de marge anormal sur le 2,1 % ou le 10 % peut révéler des erreurs de taux.

## 6. Références

- CGI : art. 278 à 281 octies (taux de TVA ; le taux de 2,1 % des médicaments remboursables figure à l'art. 281 octies) — vérifier la rédaction en vigueur pour chaque catégorie de produits.
- CGI : art. 267-I et 271 (base et déduction : réductions de prix), art. 272-1 (régularisation de la TVA en cas de réduction de prix).
- Code de commerce : art. L. 441-3 et suivants (conventions écrites, coopération commerciale) ; Code de la santé publique (encadrement des remises sur les médicaments remboursables).
- PCG : comptes 6097, 706, 4111, 44566, 44571.
