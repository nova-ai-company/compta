# Corrigé E08-01 — Inventaire des matières premières de la Boulangerie Dupain et variation de stock

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-01](../exercices/E08-01_inventaire-matieres-boulangerie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Une fiche d'inventaire n'est pas une pièce que l'on « saisit » : c'est une pièce que l'on **contrôle**. Quatre questions pour chaque ligne :
1. **Le bien existe-t-il et appartient-il à l'entreprise ?** (comptage, propriété)
2. **A-t-il encore une valeur ?** (périmé, abîmé, invendable)
3. **Le prix unitaire est-il le bon ?** (coût d'acquisition **HT**, conforme à la méthode — ici le dernier prix d'achat HT)
4. **Le calcul est-il juste et la ligne dans le bon compte ?** (31 matières, 326 emballages, 35 produits finis)

### Question 1 — Les anomalies de la fiche

| # | Ligne | Anomalie | Traitement correct |
|---|---|---|---|
| 1 | Chocolat de couverture | **Erreur de calcul** : 12 × 62,90 = **754,80 €**, et non 7 548,00 € (virgule décalée, facteur 10) | 754,80 € |
| 2 | Beurre AOP lot DLC 20/12/2026 | **Produit périmé** au 31/12, non repris par le fournisseur, jeté le 4 janvier (pièce 5) : **valeur nulle** | Exclu de l'inventaire (0 €) ; conserver la note de Julie et, idéalement, une trace de la destruction (photo datée, registre d'hygiène) |
| 3 | Boîtes pâtisserie | Valorisées au **prix TTC** (64,80 €) au lieu du **prix HT** (54,00 €, pièce 2). La TVA est récupérable : elle ne fait pas partie du coût | 9 × 54,00 = **486,00 €** |
| 4 | Pains et viennoiseries invendus | **Produits finis**, valorisés (85 €) sans méthode, alors qu'ils ont été **donnés** le soir même (pièce 4) : ils ne sont plus dans le patrimoine au 31/12 à minuit | Exclus (0 €) — de toute façon, un produit fini se valorise au **coût de production**, jamais au prix de vente |
| 5 | Emballages | Mélangés aux matières premières dans un total unique | Isolés en **326 Emballages** (variation **6032**) |

Point à vérifier, sans anomalie : la **livraison du 31/12 au matin** (20 sacs de T65) a bien été comptée — le stock de 48 sacs l'inclut (Marc le confirme). Le stock est juste, mais l'**achat** n'est pas comptabilisé : il faut une **facture non parvenue**.

Méthode : le « dernier prix d'achat HT » est ici acceptable, car les matières tournent en moins de deux semaines (approximation du FIFO) et la méthode est appliquée de façon permanente. On ne la change pas.

### Question 3 — La livraison du 31/12

Les 20 sacs sont **physiquement dans le stock compté** au 31/12. Si l'achat n'est pas enregistré, on aurait un stock final sans l'achat correspondant : résultat surévalué de 396,00 €. → **FNP** au 31/12/2026, TVA à 5,5 % (farine, produit alimentaire).

## 2. Calculs (détaillés, chaque montant justifié)

### Inventaire corrigé des matières premières (compte 31)

| Article | Qté | PU HT | Valeur |
|---|---|---|---|
| Farine T65 tradition (dont 20 sacs livrés le 31/12) | 48 | 19,80 € | 950,40 € |
| Farine T45 pâtisserie | 22 | 23,50 € | 517,00 € |
| Farine de seigle | 8 | 31,20 € | 249,60 € |
| Beurre AOP (lots non périmés) | 60 | 21,40 € | 1 284,00 € |
| Beurre AOP lot périmé | 10 | — | 0,00 € |
| Sucre semoule | 14 | 24,60 € | 344,40 € |
| Chocolat de couverture | 12 | 62,90 € | **754,80 €** |
| Œufs frais | 40 | 7,20 € | 288,00 € |
| Levure fraîche | 15 | 4,10 € | 61,50 € |
| Poudre d'amandes | 6 | 98,50 € | 591,00 € |
| **Total matières premières (31)** | | | **5 040,70 €** |

### Inventaire corrigé des emballages (compte 326)

| Article | Qté | PU HT | Valeur |
|---|---|---|---|
| Sacs papier kraft | 12 | 38,00 € | 456,00 € |
| Boîtes pâtisserie | 9 | **54,00 €** (64,80 / 1,20) | 486,00 € |
| **Total emballages (326)** | | | **942,00 €** |

### Rapprochement avec la fiche de Marc

| | Montant |
|---|---|
| Total de la fiche | 13 172,10 € |
| – Erreur de calcul chocolat (7 548,00 – 754,80) | – 6 793,20 € |
| – Beurre périmé | – 214,00 € |
| – Boîtes valorisées TTC (583,20 – 486,00) | – 97,20 € |
| – Invendus donnés | – 85,00 € |
| **= Stock corrigé (5 040,70 + 942,00)** | **5 982,70 €** |

Contrôle : 13 172,10 – 6 793,20 – 214,00 – 97,20 – 85,00 = 5 982,70 € ✔

### Variations de stock

| | Stock initial (01/01/2026) | Stock final (31/12/2026) | Variation = SI – SF |
|---|---|---|---|
| Matières premières (6031) | 5 860,00 € | 5 040,70 € | **+ 819,30 €** (solde débiteur) |
| Emballages (6032) | 1 120,00 € | 942,00 € | **+ 178,00 €** (solde débiteur) |

### FNP Moulins du Lyonnais

20 sacs × 19,80 € = **396,00 € HT** ; TVA 5,5 % = 396,00 × 5,5 % = **21,78 €** ; TTC **417,78 €**.

### Question 5 — Incidence sur le résultat et contrôle de cohérence

**Incidence des corrections** par rapport à la fiche de Marc (qui aurait conduit à un stock final de 13 172,10 € et à l'oubli de la FNP) :
- stock final inférieur de 13 172,10 – 5 982,70 = 7 189,40 € → charges (603) supérieures de 7 189,40 € ;
- achat supplémentaire (FNP) : 396,00 € ;
- **résultat avant IS inférieur de 7 585,40 €** à celui qu'aurait donné la fiche brute.

**Ratio consommation de matières / CA** :

| | 2026 corrigé | 2026 « version Marc » | 2025 |
|---|---|---|---|
| Consommation = SI + achats – SF | 5 860,00 + 148 600,00 + 396,00 – 5 040,70 = **149 815,30 €** | (5 860,00 + 1 120,00) + 148 600,00 – 13 172,10 = 142 407,90 € | 146 900,00 € |
| CA HT | 712 400,00 € | 712 400,00 € | 690 000,00 € |
| **Ratio** | **21,03 %** | 19,99 % | **21,29 %** |

Le ratio corrigé (21,03 %) est cohérent avec 2025 (21,29 %) — légère amélioration plausible (prix de vente revalorisés). La version de Marc faisait apparaître une baisse d'1,3 point **sans explication économique** : c'est exactement le signal qui aurait dû alerter, même sans voir l'erreur sur le chocolat.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6031 | Variation des stocks de matières premières | Annulation stock initial MP au 31/12/2025 | 5 860,00 | |
| 31/12/2026 | OD | 31 | Matières premières | Annulation stock initial MP au 31/12/2025 | | 5 860,00 |
| 31/12/2026 | OD | 31 | Matières premières | Stock final MP — inventaire corrigé du 31/12/2026 | 5 040,70 | |
| 31/12/2026 | OD | 6031 | Variation des stocks de matières premières | Stock final MP — inventaire corrigé du 31/12/2026 | | 5 040,70 |
| 31/12/2026 | OD | 6032 | Variation des stocks des autres approvisionnements | Annulation stock initial emballages | 1 120,00 | |
| 31/12/2026 | OD | 326 | Emballages | Annulation stock initial emballages | | 1 120,00 |
| 31/12/2026 | OD | 326 | Emballages | Stock final emballages au 31/12/2026 | 942,00 | |
| 31/12/2026 | OD | 6032 | Variation des stocks des autres approvisionnements | Stock final emballages au 31/12/2026 | | 942,00 |
| 31/12/2026 | OD | 601 | Achats stockés – matières premières | FNP Moulins du Lyonnais BL-26-12-3381 (20 sacs T65) | 396,00 | |
| 31/12/2026 | OD | 44586 | TVA sur factures non parvenues | FNP Moulins du Lyonnais — TVA 5,5 % | 21,78 | |
| 31/12/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Moulins du Lyonnais BL-26-12-3381 | | 417,78 |
| | | | | **Totaux** | **13 380,48** | **13 380,48** |

Le 01/01/2027 : **extourne** de la FNP (D 408 417,78 / C 601 396,00 ; C 44586 21,78), puis saisie normale de la facture mensuelle de janvier.

**Sens des soldes (question 4).**
- **6031 : solde débiteur de 819,30 €** (5 860,00 – 5 040,70). Le stock de matières a **baissé** : la boulangerie a consommé, en 2026, 819,30 € de matières **de plus** qu'elle n'en a acheté. Cette consommation de stock est une **charge** supplémentaire, qui s'ajoute aux 148 996,00 € d'achats (148 600,00 + 396,00).
- **6032 : solde débiteur de 178,00 €** (1 120,00 – 942,00), même logique pour les emballages.
- Si le stock avait augmenté, le 603 aurait été **créditeur** : il serait resté dans les charges, en diminution (il ne devient jamais un produit).

## 4. Points d'attention / pièges

- **L'erreur « ×10 » sur le chocolat** à elle seule représentait 6 793,20 € de résultat fictif — près de 4,5 % de la consommation annuelle. Un contrôle de vraisemblance (« 12 cartons de chocolat, 7 500 € ? ») suffit à la voir : recalculez **toujours** les lignes à forte valeur.
- **Prix HT** : la boulangerie récupère la TVA ; valoriser au TTC surévalue le stock de 20 % (ou 5,5 %) sur la ligne concernée.
- **Périmé = 0** : un produit alimentaire périmé non repris n'a aucune valeur, même s'il est encore dans la chambre froide au 31/12.
- **Produits finis** : les invendus donnés le soir même ne sont plus là. Si un jour la boulangerie gardait un stock de produits finis significatif (bûches de Noël congelées, par exemple), il se valoriserait au **coût de production** en 35 (variation 7135), jamais au prix de vente.
- **La livraison du 31/12** : stock compté ⇒ achat obligatoirement enregistré. C'est le contrôle de cut-off le plus simple et le plus oublié.
- **« Ça fera plaisir au banquier »** : un stock gonflé améliore le résultat N, mais il **se retourne en N+1** (stock initial surévalué = charge 2027 surévaluée). Et c'est une inexactitude des comptes.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Message à Marc (à envoyer après 14 h) :**

> Bonjour Marc,
>
> Merci pour l'inventaire. En le reprenant ligne par ligne, nous avons trouvé quelques corrections :
> - le chocolat : 12 cartons à 62,90 € font **754,80 €**, pas 7 548 € (une virgule a glissé) ;
> - les 10 plaques de beurre périmées que Julie a mises de côté n'ont plus de valeur ;
> - les boîtes pâtisserie se comptent au prix **HT** (54 €), puisque vous récupérez la TVA ;
> - les invendus du 31 ont été donnés le soir même : ils ne font plus partie du stock.
>
> Votre stock réel au 31/12 est donc de **5 982,70 €** (5 040,70 € de matières et 942,00 € d'emballages). C'est cohérent avec votre activité : vos matières représentent 21 % de votre chiffre d'affaires, comme en 2025.
>
> Un stock plus élevé aurait affiché un meilleur résultat cette année, mais il se serait retourné contre vous l'an prochain — et votre banquier préfère des comptes justes. Nous avons aussi enregistré la livraison de farine du 31 au matin ; pensez à nous transmettre la facture des Moulins du Lyonnais dès réception.
>
> Pour le prochain inventaire, je vous propose un modèle de fiche pré-remplie (articles, unités, derniers prix HT) : vous n'aurez plus qu'à compter.
>
> Bien cordialement,

**Contrôles et documentation :**
- conserver la fiche manuscrite **signée** + la fiche corrigée + le rapprochement (pièce justificative de l'inventaire, Code de commerce art. L. 123-12) ;
- vérifier le prix unitaire des trois lignes les plus importantes sur les dernières factures (fait pour le chocolat et les boîtes) ;
- préparer pour le 31/12/2027 une **fiche d'inventaire pré-remplie** avec les prix HT des dernières factures et une colonne « DLC » ;
- noter dans le dossier permanent : « stock de produits finis non inscrit — invendus donnés chaque soir (bons de collecte) ». Les dons d'invendus alimentaires peuvent ouvrir droit à la **réduction d'impôt mécénat** (CGI art. 238 bis), sur la base du **coût de revient**, si l'association est éligible et délivre un reçu : à proposer à Marc (sous réserve de chiffrer le coût de revient et de respecter les conditions et plafonds en vigueur, *à vérifier chaque année*).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce art. L. 123-12 (inventaire au moins une fois tous les 12 mois) et art. L. 123-14 (image fidèle).
- PCG (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06) : coût d'acquisition des stocks (hors taxes récupérables) ; règles d'évaluation des biens fongibles ; comptes 31, 326, 601, 6031, 6032, 408, 44586.
- CGI art. 38-3 (évaluation des stocks au prix de revient ou au cours du jour s'il est inférieur) ; BOFiP, série BIC – produits et stocks (BOI-BIC-PDSTK).
- CGI art. 278-0 bis (taux réduit de 5,5 % sur les produits alimentaires) ; CGI art. 238 bis (réduction d'impôt mécénat).
