# Corrigé E02-06 — Sous-traitance BTP : autoliquidation, retenue de garantie et TVA facturée à tort

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-06](../exercices/E02-06_sous-traitance-btp-autoliquidation.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Pourquoi « ce n'est pas pareil » (question 1)

Pour les **travaux de construction** (y compris réparation, nettoyage, entretien, transformation, démolition) réalisés par un **sous-traitant** pour le compte d'un **preneur assujetti** qui est lui-même entrepreneur (principal ou sous-traitant de rang supérieur), la TVA est **due par le preneur** (CGI art. 283-2 nonies) : c'est l'**autoliquidation**. Les conditions sont réunies ici : contrat de sous-traitance, travaux immobiliers, Bâtisseurs du Sud entrepreneur principal assujetti.

Conséquences de la facture avec TVA :
- **Le sous-traitant** qui facture de la TVA à tort en devient **redevable du seul fait de sa facturation** (CGI art. 283-3).
- **Bâtisseurs du Sud** ne peut **pas déduire** une TVA qui n'était pas légalement due au titre de l'opération (la déduction est réservée à la TVA légalement exigible) ; et elle reste **redevable de la TVA autoliquidée**. En cas de contrôle : rappel de la TVA déduite à tort (3 740,00 €) + intérêts de retard + éventuelle amende pour défaut d'autoliquidation (CGI art. 1788 A).
- En trésorerie, si Nadia paie 21 318,00 € au lieu de 17 765,00 €, Bâtisseurs du Sud avance au sous-traitant une TVA qu'elle ne pourra pas récupérer de manière sûre.

« Ça revient au même » est faux juridiquement **et** financièrement : le risque est de payer deux fois la même TVA (une fois au sous-traitant, une fois au Trésor lors du rappel).

### La retenue de garantie (question 2)

La retenue de garantie est plafonnée à **5 % du montant des travaux** (loi du 16 juillet 1971) ; le contrat la fixe à 5 % de chaque situation.
- **Situation initiale** : 5 % calculés sur le **TTC** (22 440,00 × 5 % = 1 122,00 €) — base contestable dès lors que la TVA n'était pas due.
- **Facture rectifiée** : 5 % de **18 700,00 €** (montant HT = montant dû, puisque aucune TVA n'est facturée) = **935,00 €** ✓.

### Rythme d'avancement
Avancement cumulé 62 % × 85 000,00 = 52 700,00 € ; moins 34 000,00 € déjà facturés = **18 700,00 €** ✓ (situation n° 3). Ce contrôle est indispensable : le cumul facturé par le sous-traitant doit correspondre à l'avancement constaté **contradictoirement** (PV d'avancement signé par le conducteur de travaux de Bâtisseurs du Sud).

## 2. Calculs (détaillés, chaque montant justifié)

| | Situation initiale (erronée) | Facture rectifiée |
|---|---|---|
| Montant HT | 18 700,00 € | 18 700,00 € |
| TVA facturée | 3 740,00 € | 0,00 € (autoliquidation) |
| TTC / montant facturé | 22 440,00 € | 18 700,00 € |
| Retenue de garantie 5 % | 1 122,00 € | **935,00 €** |
| Net à payer | 21 318,00 € | **17 765,00 €** |

TVA autoliquidée par Bâtisseurs du Sud : construction **neuve** de logements → **20 %** : 18 700,00 × 20 % = **3 740,00 €**, due (445711) et déductible (445661).
Économie de trésorerie par rapport à un paiement de la situation erronée : 21 318,00 – 17 765,00 = **3 553,00 €** (3 740,00 de TVA – 187,00 d'écart de retenue).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 09/10/2026 | AC | 401RIBE | Fournisseur Maçonnerie Ribeiro | Ribeiro AV MR-AV-2026-0011 annul. MR-2026-0905 | 22 440,00 | |
| 09/10/2026 | AC | 611 | Sous-traitance | Ribeiro AV MR-AV-2026-0011 annul. MR-2026-0905 | | 18 700,00 |
| 09/10/2026 | AC | 44566 | TVA déductible sur ABS | Ribeiro AV MR-AV-2026-0011 annul. TVA facturée à tort | | 3 740,00 |
| 09/10/2026 | AC | 611 | Sous-traitance | Ribeiro F MR-2026-1009 sit. 3 Acacias (annule et remplace) | 18 700,00 | |
| 09/10/2026 | AC | 445661 | TVA déductible autoliquidée – sous-traitance BTP | Ribeiro F MR-2026-1009 autoliquidation 20 % | 3 740,00 | |
| 09/10/2026 | AC | 445711 | TVA due autoliquidée – sous-traitance BTP | Ribeiro F MR-2026-1009 autoliquidation 20 % | | 3 740,00 |
| 09/10/2026 | AC | 401RIBE | Fournisseur Maçonnerie Ribeiro | Ribeiro F MR-2026-1009 net à payer | | 17 765,00 |
| 09/10/2026 | AC | 4017 | Fournisseurs – retenues de garantie | Ribeiro F MR-2026-1009 RG 5 % chantier Acacias | | 935,00 |
| 12/10/2026 | BQ | 401RIBE | Fournisseur Maçonnerie Ribeiro | Vir. Ribeiro MR-2026-1009 | 17 765,00 | |
| 12/10/2026 | BQ | 512 | Banque | Vir. Ribeiro MR-2026-1009 | | 17 765,00 |
| | | | | **Totaux** | **62 645,00** | **62 645,00** |

> Si la saisie de Nadia n'est pas encore **validée** (période non clôturée), on peut la supprimer et ne passer que la facture rectifiée. Si elle est validée, l'enregistrement de l'avoir du sous-traitant (ci-dessus) fait office de contre-passation et conserve la piste d'audit. Le paiement du 12/10 est **conditionné** à la régularisation de l'attestation de vigilance (question 6).

**Question 5 — libération de la retenue de garantie** (un an après la réception, sans réserves non levées) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| (réception + 1 an) | BQ | 4017 | Fournisseurs – retenues de garantie | Libération RG Ribeiro chantier Acacias | 935,00 | |
| (réception + 1 an) | BQ | 512 | Banque | Libération RG Ribeiro chantier Acacias | | 935,00 |
| | | | | **Totaux** | **935,00** | **935,00** |

(En pratique, la RG est souvent remplacée par une **caution bancaire** fournie par le sous-traitant : dans ce cas, pas de retenue, pas de 4017.)

## 4. Points d'attention / pièges

- **CA3 de septembre (question 4)** : la facture erronée du 05/09 ne doit **pas** être déduite. Comme la CA3 de septembre n'est pas encore déposée, on la dépose **sans** les 3 740,00 € de TVA déductible de Nadia. L'autoliquidation de la situation n° 3 : la TVA autoliquidée est exigible selon les règles des **travaux immobiliers** (prestations de services → à l'**encaissement** par le sous-traitant, c'est-à-dire au paiement par Bâtisseurs du Sud, sauf option pour les débits). Paiement le 12/10/2026 → **CA3 d'octobre** : 18 700,00 € sur la ligne dédiée à l'autoliquidation (TVA due 3 740,00 €), et 3 740,00 € en TVA déductible. Le moment d'exigibilité de l'autoliquidation en sous-traitance BTP est un point à vérifier dans le BOFiP en vigueur.
- **La retenue de garantie ne réduit pas la charge** : la charge de sous-traitance est de 18 700,00 € ; la RG est une **dette** différée (4017), pas un rabais.
- **Taux de l'autoliquidation** : celui des travaux. En **rénovation** de logements de plus de 2 ans, le taux pourrait être de 10 % (ou 5,5 % pour certains travaux de rénovation énergétique), selon les conditions et attestations.
- **Une facture « annule et remplace »** n'existe pas juridiquement sans **avoir** : l'avoir MR-AV-2026-0011 est indispensable pour annuler la facture MR-2026-0905 dans la comptabilité du sous-traitant (sinon il reste redevable des 3 740,00 € facturés).
- **Fin d'exercice** : les situations de sous-traitance des chantiers en cours au 31/12 entrent dans le calcul du **résultat à l'avancement** (ou des en-cours) — cohérence à vérifier avec le module chantiers.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — obligation de vigilance.** Pour tout contrat d'au moins **5 000 € HT**, le donneur d'ordre doit obtenir de son cocontractant, **lors de la conclusion du contrat puis tous les six mois jusqu'à la fin de son exécution**, une **attestation de vigilance** URSSAF (et un extrait Kbis / carte d'identification). L'attestation de Ribeiro date du **12/02/2026** : elle a **plus de six mois** au 09/10/2026. À défaut, Bâtisseurs du Sud peut être tenue **solidairement** au paiement des cotisations, pénalités et majorations dues par le sous-traitant en cas de travail dissimulé (Code du travail, art. L. 8222-1 et suivants ; Code de la sécurité sociale, art. L. 243-15). **Avant de payer** : obtenir une attestation à jour (vérifiable en ligne via son code de sécurité). C'est aussi le bon moment pour vérifier l'attestation d'assurance décennale de l'année en cours et, pour un chantier avec maître d'ouvrage, l'acceptation du sous-traitant et l'agrément de ses conditions de paiement.

**Message à Nadia et Karim Benali :**

> Bonjour Nadia, bonjour Karim,
>
> Pour Maçonnerie Ribeiro (situation n° 3) :
> - la TVA facturée par Ribeiro n'est pas déductible pour nous : en sous-traitance BTP, c'est **nous** qui déclarons la TVA (autoliquidation). Garder la première facture nous exposait à un rappel de 3 740 € en cas de contrôle, plus pénalités. Ribeiro a émis un avoir et une facture rectifiée : c'est corrigé ;
> - le montant à payer est **17 765 €** (et non 21 318 €) ; 935 € de retenue de garantie seront payés un an après la réception ;
> - **avant le virement**, il nous faut l'attestation de vigilance URSSAF à jour de Ribeiro (la dernière date de février, elle n'est plus valable). Sans elle, nous pourrions être solidaires de ses dettes sociales. Pouvez-vous la lui demander aujourd'hui ?
> - la CA3 de septembre sera déposée sans la TVA de cette facture ; l'autoliquidation figurera sur celle d'octobre.

**Contrôles** : tableau de suivi des sous-traitants (contrat, montant, situations cumulées, RG, dates des attestations de vigilance, décennale) ; rapprochement mensuel 445661 / 445711 ; revue de **toutes** les factures de sous-traitants depuis le 01/01/2026 pour s'assurer qu'aucune autre ne comporte de TVA.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 283-2 nonies : autoliquidation de la TVA dans la sous-traitance de travaux de construction.
- CGI art. 283-3 : TVA facturée à tort due par celui qui la facture.
- CGI, annexe II, art. 242 nonies A : mention « Autoliquidation » sur la facture.
- CGI art. 1788 A : sanctions liées à l'autoliquidation.
- BOFiP, TVA – Redevable – autoliquidation dans le secteur du BTP (exigibilité, taux).
- Loi n° 75-1334 du 31 décembre 1975 relative à la sous-traitance (acceptation du sous-traitant, garanties de paiement).
- Loi n° 71-584 du 16 juillet 1971 : retenue de garantie (5 % maximum, substitution par caution).
- Code du travail art. L. 8222-1 et suivants ; Code de la sécurité sociale art. L. 243-15 : obligation de vigilance et solidarité financière.
