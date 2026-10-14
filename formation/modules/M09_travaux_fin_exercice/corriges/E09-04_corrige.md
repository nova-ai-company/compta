# Corrigé E09-04 — FitClub : abonnements annuels, packs de coaching et redevance au 31/08/2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-04](../exercices/E09-04_pca-fitclub.md)

## 1. Analyse

**L'état du logiciel contient deux erreurs.**
1. **Il est en TTC.** Un PCA neutralise du **produit**, et le produit est HT. La TVA a été collectée à l'encaissement et reversée ; elle ne se « constate pas d'avance ». Reprendre 60 645 € surévaluerait le PCA de la TVA (1/6 du TTC) et minorerait d'autant le résultat.
2. **Il ignore les suspensions.** Les 6 membres dont le contrat a commencé en janvier 2026 ont vu leur abonnement prolongé de 2 mois (CGV). La prestation que FitClub leur doit après le 31/08/2026 n'est donc pas de 4 mois (septembre à décembre) mais de **6 mois** (septembre 2026 à février 2027). Le produit encaissé qui couvre ces 2 mois supplémentaires n'est pas acquis.

**Le raisonnement par « génération »** (mois de début) est le bon. Un contrat débuté le mois *m* a encore *r* mois à courir après le 31/08/2026, et son PCA vaut 390 € × r/12 = 32,50 € × r. Les **préventes de septembre 2026** (30 contrats) sont payées mais le service n'a pas commencé : 100 % en PCA.

**Packs coaching :** il s'agit de **prestations discontinues**, dont le produit est acquis **à chaque séance réalisée**. Les 180 séances restantes (45 %) ne sont pas acquises → PCA. Le taux historique de non-utilisation (< 3 %) est trop faible et le pack encore valide : on ne reconnaît pas de produit sur les séances « probablement perdues ». Le produit des séances non consommées ne sera reconnu qu'à l'expiration du pack.

**Frais d'inscription :** ils rémunèrent une contrepartie **réalisée à l'inscription** (dossier, badge, bilan forme de 45 min la première semaine). Le produit est donc acquis immédiatement, et Romain a raison sur le principe. Point de vigilance : sans prestation distincte (simple « droit d'entrée »), il faudrait les étaler sur la durée de l'abonnement. Ici, le bilan forme justifie la reconnaissance immédiate. Documentez cette position et appliquez-la de façon constante.

**Redevance d'août :** la charge naît du CA d'août 2026 réalisé sur l'exercice, mais la facture est datée du 05/09 → **FNP**.

## 2. Calculs

**PCA abonnements (HT), par génération :**

| Début | Nb | r (mois restants) | Nb × r | PCA HT (32,50 € × Nb × r) |
|---|---|---|---|---|
| 10/2025 | 18 | 1 | 18 | 585,00 € |
| 11/2025 | 15 | 2 | 30 | 975,00 € |
| 12/2025 | 9 | 3 | 27 | 877,50 € |
| 01/2026 | 55 | 4 | 220 | 7 150,00 € |
| 02/2026 | 24 | 5 | 120 | 3 900,00 € |
| 03/2026 | 20 | 6 | 120 | 3 900,00 € |
| 04/2026 | 14 | 7 | 98 | 3 185,00 € |
| 05/2026 | 12 | 8 | 96 | 3 120,00 € |
| 06/2026 | 16 | 9 | 144 | 4 680,00 € |
| 07/2026 | 8 | 10 | 80 | 2 600,00 € |
| 08/2026 | 22 | 11 | 242 | 7 865,00 € |
| 09/2026 (prévente) | 30 | 12 | 360 | 11 700,00 € |
| **Sous-total (sans suspensions)** | | | **1 555** | **50 537,50 €** |
| Suspensions : 6 contrats × 2 mois supplémentaires | | | + 12 | + 390,00 € |
| **PCA abonnements** | | | **1 567** | **50 927,50 €** |

Contrôles :
- 60 645,00 € TTC / 1,20 = 50 537,50 € HT : l'état logiciel, une fois converti en HT, correspond bien au sous-total ;
- suspensions : 6 × 2 × 32,50 € = 390,00 €.

**PCA coaching :** 40 packs × 300 € HT = 12 000 € HT ; part non consommée 180/400 = 45 % → **5 400,00 €**.

**FNP redevance :** 61 400 € × 6 % = **3 684,00 € HT** ; TVA 736,80 € ; TTC 4 420,80 €.

**Écart avec le chiffre de Romain :** 60 645,00 – 50 927,50 = 9 717,50 € de PCA en trop si l'on avait repris l'état brut (soit un résultat minoré d'autant), sans compter l'oubli du coaching et de la redevance.

**Impact des écritures d'inventaire sur le résultat :** – 50 927,50 – 5 400,00 – 3 684,00 = **– 60 011,50 €** par rapport à la balance avant inventaire.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/08/2026 | OD | 7061 | Abonnements | PCA abonnements annuels (HT, suspensions incluses) | 50 927,50 | |
| 31/08/2026 | OD | 487 | Produits constatés d'avance | PCA abonnements annuels | | 50 927,50 |
| 31/08/2026 | OD | 7063 | Coaching | PCA séances non consommées 45 % | 5 400,00 | |
| 31/08/2026 | OD | 487 | Produits constatés d'avance | PCA packs coaching | | 5 400,00 |
| 31/08/2026 | OD | 651 | Redevances pour concessions, brevets, licences, marques… | FNP redevance franchise août 2026 | 3 684,00 | |
| 31/08/2026 | OD | 44586 | TVA sur factures non parvenues | FNP redevance août | 736,80 | |
| 31/08/2026 | OD | 4081 | Fournisseurs – factures non parvenues | FNP redevance août | | 4 420,80 |
| | | | | **Totaux** | **60 748,30** | **60 748,30** |

Au **01/09/2026** : extourne des trois écritures.

## 4. Points d'attention / pièges

- **Un état logiciel est une donnée à auditer, pas une vérité.** Vérifiez la base (TTC/HT), les cas non gérés (suspensions, gestes commerciaux, résiliations pour motif légitime) et le total par rapport au CA.
- **Les préventes** (contrats commençant après la clôture) sont souvent oubliées par les outils qui ne listent que les contrats « actifs ». Ici, l'état les inclut, mais vérifiez-le toujours.
- **Résiliations pour motif légitime** (déménagement, maladie longue selon les CGV) : si un remboursement est dû à la clôture, passez un **avoir à établir** plutôt qu'un PCA.
- **Coaching :** ne reconnaissez pas par anticipation le produit des séances qui ne seront « probablement » jamais consommées tant que le pack est valide. Le produit des séances non utilisées est reconnu à l'**expiration**.
- **La redevance de franchise** est une charge d'exploitation (651). Le droit d'entrée initial, lui, est une **immobilisation incorporelle** amortie sur la durée du contrat (vu en M05).
- **Frais d'inscription :** quelle que soit la position retenue, elle doit être **permanente** d'un exercice à l'autre (principe de permanence des méthodes).

## 5. Ce qu'un senior ferait en plus

- **Contrôle global de vraisemblance :** les abonnements annuels démarrés sur l'exercice représentent 255 contrats × 390 € = 99 450 € HT, auxquels s'ajoutent 30 préventes (11 700 € HT). Un PCA d'environ 51 k€ est cohérent avec le pic de janvier, les contrats d'été et les préventes de rentrée. Comparez avec le PCA au 31/08/2025.
- **Procédure pour l'an prochain :** demander à l'éditeur de FitManager un état **HT** intégrant les suspensions ; à défaut, faire tenir par l'accueil un registre des suspensions et prolongations, rapproché chaque trimestre ; documenter dans le dossier permanent la règle de reconnaissance des frais d'inscription.
- **Mail à Romain :**
> « Bonjour Romain, le chiffre du logiciel (60 645 €) ne peut pas être repris tel quel : il est en TTC et ne tient pas compte des 6 abonnements prolongés pour raisons médicales. Après correction, les abonnements payés d'avance qui relèvent de l'exercice suivant représentent 50 927,50 € HT. Les frais d'inscription restent bien en CA de l'exercice, car le badge et le bilan forme sont fournis dès l'inscription. En revanche, les séances de coaching non encore réalisées (45 % des packs, soit 5 400 € HT) seront reconnues au fur et à mesure des séances. Ce n'est pas une perte de chiffre d'affaires, c'est un décalage d'exercice. »

## 6. Références

- CGI, art. 38, 2 bis (prestations continues et discontinues à échéances successives : rattachement au fur et à mesure de l'exécution).
- Code de commerce, art. L. 123-21 ; permanence des méthodes (art. L. 123-17).
- PCG : compte 487 « Produits constatés d'avance », compte 4081 « Fournisseurs – factures non parvenues », compte 651 « Redevances pour concessions, brevets, licences, marques, procédés, logiciels… ».
- CGI, art. 269, 2-c (TVA sur prestations de services exigible à l'encaissement).
