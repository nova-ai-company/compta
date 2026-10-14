# Corrigé E09-06 — Garage Martin : litige prud'homal, garanties VO et autres « provisions » au 30/09/2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-06](../exercices/E09-06_provisions-garage-martin.md)

## 1. Analyse

On vérifie, pour chaque sujet, les trois conditions : **(1)** une obligation envers un tiers née d'un événement passé, **(2)** une sortie de ressources probable sans contrepartie, **(3)** une estimation fiable.

| Sujet | (1) Obligation / événement passé | (2) Sortie probable | (3) Estimation fiable | Conclusion |
|---|---|---|---|---|
| Litige Yohan B. | Oui : licenciement du 12/06/2026 et saisine du CPH le 02/09/2026 | Oui : requalification probable à 70 % selon l'avocat | Oui : montants chiffrés | **Provision 1511**, à la **meilleure estimation**, et **pas** à la réclamation totale |
| Garanties VO | Oui : ventes réalisées sous garantie contractuelle de 12 mois | Oui : statistiquement, des interventions auront lieu | Oui : 3 ans d'historique stable | **Provision 1512**, recalculée chaque année |
| Amende DGCCRF | Oui : manquements constatés le 08/07/2026 ; procédure engagée | Oui : lettre préalable sans observations en réponse | Oui : 3 000 € | **Provision 1516** (non déductible) |
| Pont élévateur | **Non** : aucune obligation envers un tiers ; c'est une décision de gestion future | — | — | **Aucune provision**. Le remplacement sera une **immobilisation**. On vérifie en revanche la **VNC de l'ancien pont** (dépréciation ou révision du plan d'amortissement si sa durée d'utilisation se raccourcit) |

**Litige — pourquoi pas 38 400 € ?** La provision se mesure à la **meilleure estimation** de la sortie de ressources, c'est-à-dire au **scénario le plus probable** pour une obligation unique (ici, la requalification en cause réelle et sérieuse, évaluée à 70 %). Les dommages et intérêts de 27 160 € relèvent d'un scénario jugé peu probable (20 %) : on ne les provisionne pas, mais on les mentionne en annexe comme **passif éventuel** s'ils sont significatifs. Provisionner 38 400 € serait une **surévaluation volontaire** du passif, contraire à l'image fidèle et non déductible pour la fraction excessive.

Il faut aussi ajouter les **charges patronales** sur le préavis et les congés payés afférents, qui sont des salaires. L'indemnité légale de licenciement est exonérée de cotisations dans les limites légales : on n'en ajoute pas.

**Garanties — pourquoi pas 9 800 € « comme l'an dernier » ?** Une provision se **réestime à chaque clôture** à partir des données de l'exercice. On ne la « garde » pas. L'ancienne provision est reprise et une nouvelle est dotée (ou on ne passe que le complément). Le détail reprise/dotation est plus lisible dans le tableau des provisions.

## 2. Calculs

**Provision litige :**

| Élément | Montant |
|---|---|
| Indemnité légale de licenciement | 4 200,00 € |
| Indemnité compensatrice de préavis | 6 400,00 € |
| Congés payés sur préavis | 640,00 € |
| Charges patronales sur (6 400 + 640) × 42 % = 7 040 × 42 % | 2 956,80 € |
| **Provision 1511** | **14 196,80 €** |

**Provision garanties :** un véhicule vendu au mois *m* reste couvert pendant les mois qui suivent le 30/09/2026. Le coût résiduel par véhicule est de 310 € × mois restants / 12.

| Mois de vente | Nb | Mois de garantie restant après le 30/09/2026 | Calcul | Provision |
|---|---|---|---|---|
| oct-25 | 8 | 0 | — | 0,00 € |
| nov-25 | 7 | 1 | 7 × 310 × 1/12 | 180,83 € |
| déc-25 | 9 | 2 | 9 × 310 × 2/12 | 465,00 € |
| janv-26 | 5 | 3 | 5 × 310 × 3/12 | 387,50 € |
| févr-26 | 6 | 4 | 6 × 310 × 4/12 | 620,00 € |
| mars-26 | 9 | 5 | 9 × 310 × 5/12 | 1 162,50 € |
| avr-26 | 10 | 6 | 10 × 310 × 6/12 | 1 550,00 € |
| mai-26 | 8 | 7 | 8 × 310 × 7/12 | 1 446,67 € |
| juin-26 | 7 | 8 | 7 × 310 × 8/12 | 1 446,67 € |
| juil-26 | 6 | 9 | 6 × 310 × 9/12 | 1 395,00 € |
| août-26 | 4 | 10 | 4 × 310 × 10/12 | 1 033,33 € |
| sept-26 | 9 | 11 | 9 × 310 × 11/12 | 2 557,50 € |
| **Total** | **88** | | | **12 245,00 €** |

*Convention retenue : la garantie démarre le mois de la vente (un véhicule vendu en octobre 2025 est couvert jusqu'en septembre 2026). Si l'on retenait la date exacte de vente, il faudrait calculer en jours ; l'écart serait faible.*

**Amende :** 3 000,00 €.

**Impact sur le résultat comptable :** – 14 196,80 (litige) + 9 800,00 (reprise garanties) – 12 245,00 (dotation garanties) – 3 000,00 (amende) = **– 19 641,80 €**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Litige prud'homal Yohan B. | 14 196,80 | |
| 30/09/2026 | OD | 1511 | Provisions pour litiges | Litige prud'homal Yohan B. | | 14 196,80 |
| 30/09/2026 | OD | 1512 | Provisions pour garanties données aux clients | Reprise provision garanties 30/09/2025 | 9 800,00 | |
| 30/09/2026 | OD | 7815 | Reprises sur provisions d'exploitation | Reprise provision garanties 30/09/2025 | | 9 800,00 |
| 30/09/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Provision garanties VO au 30/09/2026 | 12 245,00 | |
| 30/09/2026 | OD | 1512 | Provisions pour garanties données aux clients | Provision garanties VO au 30/09/2026 | | 12 245,00 |
| 30/09/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Amende administrative DGCCRF | 3 000,00 | |
| 30/09/2026 | OD | 1516 | Provisions pour amendes et pénalités | Amende administrative DGCCRF | | 3 000,00 |
| | | | | **Totaux** | **39 241,80** | **39 241,80** |

*Variante admise pour les garanties : une seule dotation complémentaire de 12 245 – 9 800 = 2 445,00 €.*

## 4. Points d'attention / pièges

**Traitement fiscal (art. 39, 1-5° CGI) :**

| Provision | Déductible ? | Retraitement 2058-A |
|---|---|---|
| Litige prud'homal (14 196,80 €) | **Oui** : charge future déductible, litige nettement précisé et probable | — |
| Garanties (12 245 €) et reprise (9 800 €) | **Oui**, car la méthode statistique repose sur des données propres à l'entreprise. La reprise est imposable, puisque la dotation avait été déduite | — |
| Amende administrative (3 000 €) | **Non** : les sanctions pécuniaires mises à la charge des contrevenants ne sont pas déductibles (art. 39, 2 CGI), et la provision qui les anticipe non plus | **Réintégration 3 000,00 €** en 2025-2026. L'année du paiement : la reprise de provision (produit de 3 000 €) est **déduite** extra-comptablement, puisqu'elle avait été réintégrée, et la charge d'amende (3 000 €) est **réintégrée**. L'effet net est nul et l'amende n'est jamais déduite |

- **Relevé des provisions** (tableau 2056 de la liasse) : toutes les provisions doivent y figurer, faute de quoi la déduction peut être remise en cause.
- **Meilleure estimation ≠ montant réclamé ≠ fourchette haute.** Pour une obligation unique, on retient le scénario le plus probable ; pour une population (garanties), la valeur attendue statistique.
- **Les honoraires futurs de l'avocat** ne sont pas provisionnés : la prestation n'est pas encore rendue. Les honoraires déjà engagés et non facturés au 30/09 sont une **FNP**.
- **Ne jamais provisionner un investissement** : le pont élévateur sera immobilisé en 2027. La provision « pour renouvellement des immobilisations » n'existe pas en PCG (hors concessions).
- **Absence de réponse à la DGCCRF** : elle rend l'amende plus probable encore. La provision est justifiée même si la décision n'est pas notifiée.
- **Classement** : depuis le PCG 2025, l'amende payée sera une charge d'exploitation (658, *subdivision selon la nomenclature 2025 du PCG*), et non une charge exceptionnelle.

## 5. Ce qu'un senior ferait en plus

- **Ancien pont élévateur :** demander sa VNC. S'il doit être remplacé début 2027, revoir sa durée d'utilisation restante (changement d'estimation : amortissement accéléré sur la durée résiduelle) ou le déprécier si sa valeur d'usage est inférieure à la VNC.
- **Annexe :** mentionner le passif éventuel (dommages et intérêts réclamés de 27 160 €, risque jugé faible par l'avocat) si c'est significatif, sans chiffrer ce qui pourrait nuire à la défense.
- **Procédure DGCCRF :** recommander à Thierry de mettre l'atelier en conformité (affichage des prix, ordres de réparation signés) et de répondre, même tardivement. Cela peut réduire l'amende.
- **Dossier :** conserver la lettre de l'avocat, l'extraction statistique du logiciel d'atelier et la lettre de la DDPP.

**Réponse à Thierry :**
> « Bonjour Thierry, nous avons revu les quatre sujets. (1) Pour Yohan, nous provisionnons 14 196,80 € : c'est le scénario jugé le plus probable par Me Laurent (indemnités + préavis + charges). Provisionner les 38 400 € réclamés serait considéré comme une surévaluation et ne serait pas déductible. (2) La provision pour garanties est recalculée chaque année sur vos ventes : elle passe à 12 245 €. (3) L'amende DGCCRF probable (3 000 €) est provisionnée, mais elle n'est pas déductible fiscalement ; je vous conseille de répondre au courrier et de régulariser l'affichage des prix. (4) Le pont élévateur n'est pas une provision : c'est un investissement qui sera amorti à partir de son achat. Nous allons en revanche revoir l'amortissement de l'ancien pont. »

## 6. Références

- PCG (règlement ANC n° 2014-03 modifié), titre III : définition des passifs et des provisions, évaluation à la meilleure estimation.
- CGI, art. 39, 1-5° (conditions de déductibilité des provisions, relevé des provisions) ; art. 39, 2 (non-déductibilité des sanctions pécuniaires).
- Code du travail : indemnité légale de licenciement, préavis, barème d'indemnisation du licenciement sans cause réelle et sérieuse (art. L. 1235-3).
- Code de la consommation : pouvoirs de sanction administrative de la DGCCRF (procédure contradictoire préalable).
