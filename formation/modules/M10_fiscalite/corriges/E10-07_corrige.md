# Corrigé E10-07 — Régime mère-fille chez Delta Invest : QPFC à 5 % ou à 1 % ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-07](../exercices/E10-07_mere-fille-delta-invest.md)

## 1. Analyse

Le régime mère-fille (art. 145 et 216 CGI) permet à la société mère de **déduire** les dividendes reçus, sous réserve de **réintégrer une quote-part de frais et charges** (QPFC). Pour chaque dividende, le senior se pose quatre questions :

1. La distributrice est-elle soumise à l'IS ? (Une SCI à l'IR ne verse pas de dividendes mais une quote-part de résultat.)
2. ≥ 5 % du capital, titres nominatifs, conservés ≥ 2 ans ?
3. La distributrice est-elle **membre du même groupe intégré** → QPFC à 1 % ?
4. Le produit est-il bien un dividende (et non des intérêts) ?

| Produit | Mère-fille ? | QPFC | Motif |
|---|---|---|---|
| Dividende Bâtisseurs du Sud 150 000 € | **Oui** | **1 %** | 100 %, nominatif depuis 2017, membre du groupe intégré depuis 2019 (le dividende provient du résultat 2025, exercice d'appartenance au groupe) |
| Dividende SCI Horizon Pro 32 000 € | **Oui** | **5 %** | SCI ayant **opté pour l'IS**, 40 % depuis 2018, mais **hors** groupe (< 95 %) |
| Dividendes actions cotées 2 400 € | **Non** | — | 0,02 % < 5 % : produit imposable au taux normal |
| Intérêts compte courant Menuiserie 4 500 € | **Non** | — | Ce sont des intérêts, imposables (le traitement au niveau du groupe relève de M13) |

## 2. Calculs

- Dividendes déduits : 150 000 + 32 000 = **182 000 €**
- QPFC : 150 000 × 1 % = 1 500 € ; 32 000 × 5 % = 1 600 € → **3 100 €**

**2058-A individuel 2026**

| Ligne | Réintégrations | Déductions |
|---|---|---|
| Résultat comptable (bénéfice avant IS) | 168 300,00 | |
| Quote-part de frais et charges (1 % et 5 %) | 3 100,00 | |
| Produits nets de participations (régime mère-fille) | | 182 000,00 |
| **Totaux** | **171 400,00** | **182 000,00** |
| **Résultat fiscal individuel** | | **Déficit 10 600,00** |

Le déficit individuel de Delta Invest n'est **pas** reporté par Delta : il est transmis au **résultat d'ensemble** du groupe (M13), où il s'impute sur les bénéfices des autres membres.

**Comparaison avec le calcul du stagiaire (5 % sur tout)**

| | Calcul correct | « 5 % sur tout » |
|---|---|---|
| QPFC | 3 100 € | 5 % × 184 400 = 9 220 € |
| Dividendes déduits | 182 000 € | 184 400 € (actions cotées déduites à tort) |
| Résultat fiscal individuel | – 10 600 € | 168 300 + 9 220 – 184 400 = – 6 880 € |

Écart de base : – 6 880 – (– 10 600) = **3 720 €** de base en trop chez le stagiaire, qui cumule deux erreurs :
- QPFC à 5 % sur Bâtisseurs au lieu de 1 % : + 6 000 € de base (surtaxe) ;
- déduction des dividendes des actions cotées non éligibles : – 2 400 € de base, plus 120 € de QPFC (sous-taxe).
Effet net sur l'IS du groupe à 25 % : 3 720 × 25 % = **930 €** payés en trop — mais avec une erreur dans les deux sens, ce qui serait redressable pour la partie actions cotées.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 28/05/2026 | BQ | 512000 | Banque | Dividende Bâtisseurs du Sud — exercice 2025 | 150 000,00 | |
| 28/05/2026 | BQ | 761100 | Revenus des titres de participation | Dividende Bâtisseurs du Sud — exercice 2025 | | 150 000,00 |
| 30/06/2026 | BQ | 512000 | Banque | Dividende SCI Horizon Pro — exercice 2025 | 32 000,00 | |
| 30/06/2026 | BQ | 761100 | Revenus des titres de participation | Dividende SCI Horizon Pro — exercice 2025 | | 32 000,00 |
| | | | | **Totaux** | **182 000,00** | **182 000,00** |

Rappel : le produit se rattache à la date de la **décision de distribution** (AG), pas à la date de clôture de la filiale. Aucune écriture pour la QPFC (retraitement extra-comptable).

## 4. Points d'attention / pièges

- **1 % uniquement intra-groupe intégré** : la SCI Horizon Pro (40 %) reste à 5 %.
- **SCI à l'IS ≠ SCI à l'IR** : si Horizon Pro était à l'IR, Delta imposerait sa quote-part de résultat (pas de mère-fille).
- **Seuil de 5 %** : les dividendes d'un portefeuille de placement sont imposables en totalité.
- **Intérêts ≠ dividendes**.
- Le régime mère-fille est **optionnel** et s'exerce en portant les montants sur la liasse : un oubli coûte cher.
- **Clauses anti-abus** : exclusion si le dividende est déductible chez la distributrice (dispositifs hybrides) ou si le montage est artificiel.
- **TVA** : les dividendes sont hors champ mais entrent dans le calcul du **coefficient de déduction** de la holding (M04) et peuvent rendre Delta redevable de la **taxe sur les salaires**.

## 5. Ce qu'un senior ferait en plus

- **Mail type à Jean Delmas** :

> « Bonjour Monsieur Delmas, les dividendes reçus de vos filiales sont effectivement quasi exonérés grâce au régime mère-fille : on les déduit et on ne réintègre qu'une quote-part de frais de 1 % pour Bâtisseurs du Sud (filiale intégrée) et de 5 % pour la SCI Horizon Pro. En revanche, les 2 400 € de dividendes de votre portefeuille d'actions cotées sont imposables normalement (participation inférieure à 5 %). Le calcul de l'an dernier appliquait 5 % partout : nous vérifions s'il y a lieu de déposer une réclamation pour 2025 (délai : jusqu'au 31/12/2027). Bien à vous. »

- **Vérifier 2025** : si la QPFC de 5 % a été appliquée à tort sur des dividendes intra-groupe, **réclamation** (délai : 31/12 de la 2e année suivant la mise en recouvrement — *à vérifier*).
- Tenir à jour dans le dossier permanent le **registre des participations** (date d'acquisition, %, forme des titres, appartenance au groupe).
- Annexe 2059-F/G (composition du capital, filiales et participations) à cohérer.

## 6. Références

- CGI : art. 145 (conditions du régime mère-fille), art. 216 (déduction, QPFC 5 % / 1 %), art. 223 A et s. (intégration fiscale), art. 206 (SCI ayant opté pour l'IS).
- PCG : compte 761 (produits de participations), rattachement à la date de la décision de distribution.
- BOFiP : séries IS-BASE (régime des sociétés mères), IS-GPE (intégration).
