# Corrigé E04-09 — Option pour la TVA sur les loyers et refacturation de la taxe foncière

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-09](../exercices/E04-09_option-tva-loyers-sci.md)

## 1. Analyse

**a) Le régime des locations de locaux professionnels nus.** Par principe, les locations d'immeubles nus sont **exonérées** de TVA (art. 261 D-2° CGI). Le bailleur peut **opter** pour la taxation des loyers de locaux nus à usage professionnel (art. 260-2° CGI) :
- lorsque le preneur est un **assujetti** qui utilise les locaux pour les besoins de son activité taxable ;
- ou, si le **bail fait mention de l'option** par le bailleur, lorsque le preneur est **non assujetti** (ou exerce une activité exonérée).
L'option permet au bailleur de **déduire la TVA** sur l'acquisition, la construction et les travaux. Elle se gère local par local (bail par bail) selon les modalités prévues par l'art. 260-2° et l'annexe II ; sa remise en cause entraîne des **régularisations** de la TVA déduite sur l'immeuble (période de 20 ans).

**b) Lot 2 (orthodontiste).** Le preneur exerce une activité **exonérée** (soins), donc il ne récupère pas la TVA. Mais le bail **mentionne expressément l'option** : l'option est **valable** et la TVA est due sur le loyer. **Réponse au cabinet** : « La SCI a opté pour la TVA sur ses loyers, comme le prévoit votre bail ; cette option est permise pour un preneur non assujetti dès lors que le bail la mentionne. Elle permet à la SCI de récupérer la TVA sur les travaux de l'immeuble. La TVA est donc due sur votre loyer et ses accessoires. » (Toute renégociation éventuelle relève d'une discussion commerciale sur le loyer HT.)

**c) La taxe foncière refacturée n'est pas un débours.** Les débours (art. 267-II-2° CGI) supposent que l'intermédiaire paie une dépense **au nom et pour le compte** de son client. Or le **redevable légal** de la taxe foncière est le **propriétaire** (la SCI) : elle paie **sa propre dette**. La refacturation au locataire, prévue par le bail, est un **complément de loyer** (accessoire de la location) : elle suit le régime du loyer, donc **TVA à 20 %** puisque la SCI a opté. Il en va de même de la TEOM.

**d) La quote-part de vacance (lot 4, janvier-juin)** n'est refacturable à personne : elle reste une **charge** de la SCI.

**e) Exigibilité.** La location est une **prestation de services** : la TVA sur les loyers et leurs accessoires est exigible **à l'encaissement** (pas d'option débits). À la facturation, la TVA va en 44574 ; elle sera déclarée le mois du paiement par chaque locataire.

**f) Les travaux de façade** portent sur l'immeuble entièrement donné en location avec option : la TVA est **entièrement déductible**. La vacance temporaire du lot 4 ne remet pas en cause la déduction, dès lors que le local était **destiné à être loué avec option** (intention démontrée : recherche de locataire, bail signé au 01/07). Les travaux de ravalement avec isolation peuvent constituer un **composant** (immobilisation) plutôt qu'une charge d'entretien (analyse M05/M09) ; la TVA est portée en ligne 19 si immobilisation.

**g) Comptes.** Depuis la suppression des comptes de transfert de charges (règlement ANC n° 2022-06), la refacturation est un **produit** : **708** (produits des activités annexes — refacturation de taxes et charges) ; la taxe foncière reste en charge (**63512**). On ne compense pas charge et produit.

## 2. Calculs

| Lot | Quote-part | Prorata temporis | Base refacturée HT | TVA 20 % | TTC |
|---|---|---|---|---|---|
| 1 — Kinetic Conseil | 30 % | 12/12 | 11 520,00 | 2 304,00 | 13 824,00 |
| 2 — Cabinet d'orthodontie | 25 % | 12/12 | 9 600,00 | 1 920,00 | 11 520,00 |
| 3 — Archipel Études | 20 % | 12/12 | 7 680,00 | 1 536,00 | 9 216,00 |
| 4 — NovaDigital | 25 % | 6/12 | 4 800,00 | 960,00 | 5 760,00 |
| **Total refacturé** | | | **33 600,00** | **6 720,00** | **40 320,00** |
| Charge restant à la SCI (lot 4 vacant 6 mois) | | | 4 800,00 | | |

Contrôle : 33 600 + 4 800 = 38 400 € = avis de taxe foncière ✔.

Montant refacturé sur la base de l'avis total (taxe foncière + TEOM). La refacturation porte sur le montant de l'impôt ; elle est soumise à la TVA comme le loyer : 38 400 × 87,5 % = 33 600 € HT refacturés.

**TVA déductible sur travaux** : 16 000 € (100 %), CA3 de septembre 2026 (facture reçue et payée — pour une prestation de travaux, la TVA est déductible lorsqu'elle est exigible chez le prestataire, c'est-à-dire au paiement, soit le 30/09/2026).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/08/2026 | AC | 2135 | Installations générales, agencements, aménagements des constructions (composant façade — à confirmer) | FL-26-208 ravalement et isolation | 80 000,00 | |
| 31/08/2026 | AC | 44562 | TVA déductible sur immobilisations | FL-26-208 | 16 000,00 | |
| 31/08/2026 | AC | 404 | Fournisseurs d'immobilisations | FL-26-208 | | 96 000,00 |
| 09/10/2026 | VT | 411 | Clients – locataires (4 comptes) | Refacturation taxe foncière + TEOM 2026 | 40 320,00 | |
| 09/10/2026 | VT | 708 | Produits des activités annexes – refacturation taxes | Refacturation TF 2026 (lots 1 à 4) | | 33 600,00 |
| 09/10/2026 | VT | 44574 | TVA collectée en attente (encaissements) | Refacturation TF 2026 | | 6 720,00 |
| 15/10/2026 | BQ | 63512 | Taxes foncières | Avis TF + TEOM 2026 | 38 400,00 | |
| 15/10/2026 | BQ | 512 | Banque | Avis TF + TEOM 2026 | | 38 400,00 |
| | | | | **Totaux** | **174 720,00** | **174 720,00** |

(Le paiement de la facture de travaux le 30/09 — 404 / 512 — n'est pas repris. À l'encaissement de chaque refacturation : 512 / 411, puis 44574 / 44571 pour la TVA correspondante.)

## 4. Points d'attention / pièges

- **Refacturation de taxes ≠ débours** : le critère est le **redevable légal**. Taxe foncière → propriétaire → complément de loyer taxable. À l'inverse, un syndic qui paie une facture au nom de la copropriété agit en débours.
- **Cohérence** : si la SCI n'avait **pas** opté, loyers et refacturations seraient exonérés (et la TVA sur les travaux non déductible).
- **Mention de l'option dans le bail** pour les preneurs non assujettis : à vérifier dans chaque nouveau bail ; sans elle, l'option n'est pas valable pour ce local (et la TVA facturée serait due du seul fait de sa facturation, sans droit à déduction correspondant pour la SCI).
- **Loi Pinel (baux commerciaux)** : la taxe foncière peut être mise à la charge du preneur si le bail le prévoit (inventaire précis des charges) ; vérifier que les baux le stipulent — ici c'est le cas.
- **Franchise de loyer du lot 4** (si elle existe) : pas de TVA sur les mois gratuits ; comptablement, étalement possible du loyer sur la durée ferme du bail.
- **Lot vacant** : la quote-part de taxe foncière non refacturable reste une charge ; si la vacance devenait durable et que le local était affecté à un usage non taxable, des régularisations de TVA seraient à examiner.

## 5. Ce qu'un senior ferait en plus

**Réponse au gestionnaire :**
> Bonjour, la taxe foncière refacturée n'est pas un débours : la SCI en est le redevable, et le bail prévoit son remboursement par les locataires, ce qui en fait un complément de loyer. Comme la SCI a opté pour la TVA, il faut facturer la TVA à 20 %. Les locataires assujettis la récupèrent ; pour le cabinet d'orthodontie, l'option est mentionnée dans son bail, la TVA est donc bien due. Je vous joins le tableau des montants par lot (total 33 600 € HT + 6 720 € de TVA) ; la part du lot 4 pendant la vacance (4 800 €) reste à la charge de la SCI.

**Contrôles annuels** : rapprochement loyers facturés / état locatif / baux (indexation, option, charges récupérables) ; suivi du 44574 (loyers non encaissés) ; locataires en retard (un locataire en difficulté → créance douteuse et analyse du dépôt de garantie, compte 165).

## 6. Références

- CGI : art. 261 D-2° (exonération des locations de locaux nus), art. 260-2° (option pour les locations de locaux nus à usage professionnel ; mention de l'option dans le bail pour un preneur non assujetti), art. 267-II-2° (débours), art. 269-2-c (exigibilité des services), art. 271 (déduction).
- Annexe II au CGI : art. 193 et suivants (modalités de l'option), art. 207 (régularisations sur immeubles, période de 20 ans).
- Code de commerce : art. L. 145-40-2 et R. 145-35 (inventaire des charges et impôts récupérables — loi Pinel).
- PCG (règlement ANC n° 2022-06) : suppression des comptes de transfert de charges ; comptes 63512, 708.
- BOFiP : TVA-IMM (locations immobilières et option).
