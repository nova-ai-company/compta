# Corrigé E11-05 — Pharmacie Centrale : dividendes d'une gérante majoritaire de SELARL

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-05](../exercices/E11-05_affectation-pharmacie-selarl.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Trois filtres successifs avant de valider un montant de dividendes :
1. **Droit des sociétés** : le montant ≤ bénéfice distribuable (+ réserves disponibles si l'AGO le décide expressément).
2. **Contrats** : les **covenants bancaires** (clauses de limitation des distributions, ratios) — leur violation ne rend pas la distribution illégale, mais elle peut rendre **le prêt exigible** immédiatement. Pour une pharmacie qui doit encore 612 000 €, c'est le risque majeur.
3. **Fiscal et social chez l'associé** : pour une **gérante majoritaire de SEL**, la fraction des dividendes qui dépasse **10 % du capital, des primes et des comptes courants qu'elle détient** est soumise aux **cotisations sociales des indépendants** (art. L. 131-6 CSS). Les dividendes ne sont donc **pas** « 30 % et c'est tout ».

**Statut de Luc** : il est **salarié** (pharmacien adjoint sous contrat de travail) et minoritaire. Il n'est pas travailleur indépendant : la règle des 10 % ne s'applique pas à lui ; ses dividendes supportent PFNL + prélèvements sociaux sur la totalité (*à vérifier si son statut évoluait : un associé exerçant en SEL sous statut de travailleur indépendant serait lui aussi concerné*).

## 2. Calculs (détaillés, chaque montant justifié)

**Question 1 — Plafonds**

| Élément | Calcul | Montant |
|---|---|---|
| Réserve légale | Déjà à 16 000 = 10 % × 160 000 → **dotation 0** | 0,00 |
| Bénéfice distribuable | 212 600 – 0 + 18 400 | **231 000,00** |
| Maximum avec réserves | 231 000 + 240 000 | 471 000,00 |
| **Plafond du covenant** (art. 9.3) | 60 % × 212 600 | **127 560,00** |

La proposition de 150 000 € est **légale** (≤ 231 000 €) mais **viole le covenant** (150 000 > 127 560) : sans accord écrit préalable de la banque, elle constitue un cas d'exigibilité anticipée du prêt. Deux options : demander une **dérogation écrite** à la banque avant l'AGO, ou limiter la distribution à **127 560 € au plus** → montant arrondi proposé : **125 000 €** (7,8125 € par part).

**Question 2 — Affectation**

| Affectation | Montant |
|---|---|
| Réserve légale | 0,00 (déjà complète) |
| Dividendes | 125 000,00 |
| Autres réserves | 70 000,00 |
| Report à nouveau | 212 600 – 125 000 – 70 000 = **17 600,00** |
| **Total** | **212 600,00** |

Report à nouveau après affectation : 18 400 + 17 600 = **36 000,00 €**.

**Question 3 — Par associé**

Seuil des 10 % d'Anne = 10 % × (capital détenu 12 800 × 10 € = 128 000 + primes 0 + compte courant 45 000) = 10 % × 173 000 = **17 300,00 €**.

| | Anne Petit (80 %) | Luc Vidal (20 %) | Total |
|---|---|---|---|
| Dividende brut | 100 000,00 | 25 000,00 | 125 000,00 |
| Fraction ≤ 10 % (prélèvements sociaux) | 17 300,00 | 25 000,00 (totalité) | |
| Fraction > 10 % (cotisations TNS) | 82 700,00 | — | |
| PFNL 12,8 % sur le brut | 12 800,00 | 3 200,00 | 16 000,00 |
| Prélèvements sociaux 18,6 % | 17 300 × 18,6 % = 3 217,80 | 25 000 × 18,6 % = 4 650,00 | 7 867,80 |
| **Net versé par la société** | **83 982,20** | **17 150,00** | **101 132,20** |
| Cotisations TNS estimées (40 % × 82 700) — payées par Anne via sa déclaration de revenus d'indépendant | 33 080,00 | — | |
| **Net « en poche » estimé avant complément d'IR** | **50 902,20** | **17 150,00** | |

(Le PFNL de 12,8 % est un acompte : si Anne reste au PFU, l'IR définitif est égal à 12,8 % du brut ; en cas d'option globale pour le barème, la fraction soumise aux cotisations bénéficie de l'abattement de 40 %. La CSG déductible n'est pas prise en compte dans cette estimation.)

Contrôle : 125 000 – 16 000 – 7 867,80 = 101 132,20 ✓.

Pour mémoire, avec 150 000 € : Anne 120 000 € → cotisations estimées 40 % × (120 000 – 17 300) = 41 080 €, PFNL 15 360 € : le supplément de 20 000 € brut ne lui rapporterait qu'environ 20 000 × (1 – 0,40 – 0,128) = 9 440 € net — et ferait courir un risque d'exigibilité sur 612 000 € de prêt.

**Question 5 — Rémunération ou dividendes, sur la fraction de 82 700 €**

Base : même **coût avant IS** pour la société. Pour distribuer 82 700 € de dividendes, la SELARL doit dégager 82 700 / (1 – 25 %) = **110 266,67 €** de bénéfice avant IS.

| | Dividendes (fraction > 10 %) | Rémunération complémentaire |
|---|---|---|
| Coût avant IS pour la société | 110 266,67 | 110 266,67 (charge déductible) |
| IS (25 %) | 27 566,67 | 0,00 |
| Montant versé à Anne | 82 700,00 | 110 266,67 / 1,40 = 78 761,90 |
| Cotisations sociales | 82 700 × 40 % = 33 080,00 | 110 266,67 – 78 761,90 = 31 504,76 |
| IR | 82 700 × 12,8 % = 10 585,60 | 78 761,90 × 90 % × 41 % = 29 063,14 |
| **Net pour Anne** | **39 034,40** | **49 698,76** |

Avec ces hypothèses, la **rémunération** laisse environ **10 664 € de plus** à Anne et lui ouvre des droits à la retraite (CAVP) proportionnés. La **fraction ≤ 10 %** (17 300 €) reste, elle, plus efficace en dividendes (pas de cotisations, PFU). Conclusion type : **dividendes jusqu'au seuil des 10 %**, au-delà **rémunération** — à confirmer par une simulation complète (TMI réelle du foyer, plafonds de cotisations, CSG déductible, contrats Madelin, retraite).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/03/2027 | OD | 120 | Résultat de l'exercice (bénéfice) | Affectation résultat 30/09/2026 – AGO 15/03/2027 | 212 600,00 | |
| 15/03/2027 | OD | 457 | Associés – dividendes à payer | Dividendes 7,8125 €/part (A. Petit 100 000 / L. Vidal 25 000) | | 125 000,00 |
| 15/03/2027 | OD | 1068 | Autres réserves | Dotation | | 70 000,00 |
| 15/03/2027 | OD | 110 | Report à nouveau (solde créditeur) | Solde du bénéfice | | 17 600,00 |
| 31/03/2027 | BQ | 457 | Associés – dividendes à payer | Paiement dividendes | 125 000,00 | |
| 31/03/2027 | BQ | 4422 | Prélèvements forfaitaires non libératoires | PFNL 12,8 % (A. Petit 12 800 / L. Vidal 3 200) | | 16 000,00 |
| 31/03/2027 | BQ | 4423 | Retenues et prélèvements sur distributions | Prélèvements sociaux (A. Petit 3 217,80 / L. Vidal 4 650,00) | | 7 867,80 |
| 31/03/2027 | BQ | 512 | Banque | Vir. dividendes nets (A. Petit 83 982,20 / L. Vidal 17 150,00) | | 101 132,20 |
| 15/04/2027 | BQ | 4422 | Prélèvements forfaitaires non libératoires | 2777 – mars 2027 | 16 000,00 | |
| 15/04/2027 | BQ | 4423 | Retenues et prélèvements sur distributions | 2777 – mars 2027 | 7 867,80 | |
| 15/04/2027 | BQ | 512 | Banque | Télérèglement 2777 – mars 2027 | | 23 867,80 |
| | | | | **Totaux** | **361 467,80** | **361 467,80** |

**2777** : au plus tard le **15/04/2027** (15 du mois suivant le paiement). **IFU** avant le 15/02/2028.

> Variante : si Anne demande que son dividende soit **porté au crédit de son compte courant** (pour laisser la trésorerie dans la pharmacie), l'inscription en compte vaut paiement : les retenues sont dues de la même façon et la 2777 suit le même calendrier (D 457 / C 4551 pour le net, C 4422 / 4423 pour les retenues). Son compte courant augmenterait — et avec lui le seuil des 10 % des distributions suivantes.

## 4. Points d'attention / pièges

- **Covenant** : toujours lire le contrat de prêt (ou le tableau des covenants du dossier permanent) **avant** de rédiger une résolution de distribution.
- **Seuil des 10 %** : base = **capital détenu + primes + comptes courants** de la gérante (et de son conjoint, partenaire de PACS, enfants mineurs). Le compte courant de 45 000 € augmente le seuil de 4 500 € (*modalité de prise en compte du compte courant — solde ou moyenne — à vérifier dans la doctrine sociale*).
- **SEL** : la règle vise les travailleurs indépendants exerçant dans la SEL (ici Anne). Ne pas l'étendre automatiquement à un associé salarié (Luc), mais vérifier son statut.
- **Ne pas retenir les prélèvements sociaux sur la fraction > 10 %** : ce serait faire supporter deux fois les prélèvements sociaux à Anne.
- **Délais** (clôture 30/09/2026) : AGO au plus tard le **31/03/2027** ; dividendes payés au plus tard le **30/06/2027** (9 mois).
- **Taux PFU / prélèvements sociaux 2026** : 31,4 % (12,8 % + 18,6 %) selon nos informations — *à vérifier avant d'annoncer un chiffre au client*.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Note à Anne (extrait)**

> Docteur,
>
> 1. **Montant** : la société peut juridiquement distribuer 150 000 €, mais votre prêt d'acquisition (article 9.3) limite les dividendes à 60 % du résultat, soit 127 560 €. Au-delà, la banque pourrait exiger le remboursement immédiat des 612 000 € restants. Nous vous proposons **125 000 €**, ou bien de solliciter dès maintenant l'accord écrit de la banque.
> 2. **Ce que vous toucherez** : sur vos 100 000 €, la pharmacie retiendra 12 800 € d'acompte d'impôt et 3 217,80 € de prélèvements sociaux ; vous recevrez **83 982,20 €**. Mais, en tant que gérante majoritaire de SEL, les dividendes dépassant 17 300 € (10 % de votre capital et de votre compte courant) sont soumis à vos **cotisations URSSAF / CAVP** : environ **33 000 €** à prévoir en 2028 (estimation). Net estimé : **environ 51 000 €**.
> 3. **Optimisation** : au-delà de 17 300 €, une **rémunération** complémentaire vous laisserait davantage (≈ 49 700 € contre ≈ 39 000 € pour la même enveloppe de 82 700 € de dividendes) et améliorerait votre retraite. Nous vous proposons d'en parler avant l'AG : la rémunération de la gérance doit être fixée par décision des associés.

**Question 6 — Autres points juridiques**
- **Rémunération de la gérante** : décision collective des associés (statuts) ; vérifier qu'elle a été votée pour l'exercice en cours ; elle n'est pas une convention réglementée si elle est fixée par l'assemblée selon les statuts.
- **Compte courant d'Anne** : non rémunéré → pas de convention réglementée à rapporter ; s'il devenait rémunéré, convention de l'art. L. 223-19 (rapport du gérant à l'AGO, Anne ne prenant pas part au vote) et limite de déductibilité des intérêts.
- **Luc salarié et associé** : contrat de travail réel (subordination, fonctions techniques distinctes) ; ses dividendes ne modifient pas son statut.
- **Règles propres aux SEL de pharmaciens** : détention du capital et des droits de vote par des pharmaciens exerçant — à vérifier en cas d'entrée d'un nouvel associé.
- **Dépôt des comptes** : la SELARL est probablement une **petite entreprise** → option de confidentialité du compte de résultat à proposer à Anne (concurrence locale).
- **Calendrier** : convocation de l'AGO 15 jours avant (au plus tard le 28/02/2027), avec comptes, rapport de gestion (dispense possible pour une petite entreprise — à vérifier selon la composition de l'associé), texte des résolutions.

**Documentation** : copie de l'article 9.3 du prêt et de la réponse de la banque au dossier permanent ; feuille de calcul du seuil des 10 % (capital, primes, compte courant) archivée avec le PV ; échéance 2777 au 15/04/2027 dans le planning.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. L. 232-10 et L. 232-11 (réserve légale, bénéfice distribuable), art. L. 232-13 (paiement dans les 9 mois), art. L. 223-26 (approbation dans les 6 mois), art. L. 223-19 (conventions réglementées de SARL, applicables aux SELARL).
- Code de la sécurité sociale : art. L. 131-6 (dividendes des travailleurs indépendants en SARL et en SEL : fraction > 10 % du capital, des primes et des comptes courants).
- CGI : art. 62 (rémunération des gérants majoritaires), art. 117 quater (PFNL), art. 200 A (PFU), art. 158-3-2° (abattement de 40 % sur option), art. 242 ter (IFU).
- Loi n° 90-1258 du 31 décembre 1990 (sociétés d'exercice libéral) — règles de détention du capital.
- PCG : comptes 1061, 1068, 110, 120, 457, 442, 455.
