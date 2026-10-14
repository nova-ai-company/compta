# Corrigé E02-08 — La note de frais du président d'une holding

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-08](../exercices/E02-08_note-de-frais-president-delta-invest.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Chez un **assujetti partiel**, la TVA déductible se détermine en **deux filtres successifs** :
1. **La dépense ouvre-t-elle droit à déduction ?** Facture au nom de l'entreprise, dépense nécessaire à l'exploitation, et **absence d'exclusion** légale (hébergement des dirigeants, transport de personnes, cadeaux au-delà de la limite…). Si non → 0 %.
2. **Dans quelle proportion ?** On applique le **coefficient de déduction** (produit des coefficients d'assujettissement, de taxation et d'admission). Pour Delta Invest, les frais du président servent à la fois aux management fees (taxables) et à la gestion des participations (dividendes hors champ) : dépenses mixtes → coefficient **0,90** (provisoire, régularisé au vu des données définitives de 2026).

| N° | Dépense | Filtre 1 : droit à déduction ? | TVA facturée | TVA déductible (× 0,90) | Compte |
|---|---|---|---|---|---|
| 1 | Déjeuner d'affaires | **Oui** — dépense de restauration engagée dans l'intérêt de l'entreprise, facture au nom de Delta Invest | 19,20 | 17,28 | 6257 Réceptions |
| 2 | Coffret de vins au banquier | **Oui** — cadeau ≤ 73 € TTC au bénéficiaire sur l'année (68,40 € ; registre vérifié) | 11,40 | 10,26 | 6234 Cadeaux |
| 3 | Champagne à K. Benali | **Non** — 145,20 € TTC > 73 € par bénéficiaire | 24,20 | 0,00 | 6234 Cadeaux |
| 4 | 4 coffrets de chocolats | **Oui** — 30,00 € TTC par bénéficiaire, 4 bénéficiaires distincts | 20,00 | 18,00 | 6234 Cadeaux |
| 5 | Train | **Non** — transport de personnes exclu | (16,91 incluse) | 0,00 | 6251 Voyages et déplacements |
| 6 | Hôtel | **Non** — logement des dirigeants exclu (petit-déjeuner inclus dans le prix de la chambre) | 33,00 | 0,00 | 6251 |
| 7 | Taxi | **Non** — transport de personnes exclu ; de plus, un reçu n'est pas une facture | (3,50 incluse) | 0,00 | 6251 |
| 8 | Dîner seul en déplacement | **Oui** — repas pris en déplacement professionnel, facture au nom de la société | 3,00 | 2,70 | 6256 Missions |
| 9 | Ticket FNAC « cadeau » | **Non** — aucune facture, nature et bénéficiaire inconnus | ? | 0,00 | — (voir ci-dessous) |

**Dépense n° 9 (question 2).** Un ticket de carte bancaire ne prouve ni la nature de l'achat, ni le bénéficiaire, ni l'intérêt de l'entreprise. On **ne rembourse pas** en l'état : on demande à Jean Delmas la **facture** (au nom de Delta Invest) et le **nom du bénéficiaire**. Si elle est fournie : charge 6234, TVA déductible si ≤ 73 € TTC et facture conforme. Sinon : dépense personnelle, non remboursée. Montant remboursé le 12/10 : 1 226,79 – 79,99 = **1 146,80 €**.

**Les cadeaux et la limite de 73 € TTC** : la limite s'apprécie **par bénéficiaire et par an**, TTC. C'est pourquoi le **registre des cadeaux** (bénéficiaire, date, montant) est indispensable : un deuxième cadeau au même banquier dans l'année ferait dépasser le seuil.

## 2. Calculs (détaillés, chaque montant justifié)

**TVA déductible**

| N° | TVA facturée | × 0,90 | Déductible | Non déductible (→ charge) |
|---|---|---|---|---|
| 1 | 14,20 + 5,00 = 19,20 | 17,28 | 17,28 | 1,92 |
| 2 | 11,40 | 10,26 | 10,26 | 1,14 |
| 4 | 20,00 | 18,00 | 18,00 | 2,00 |
| 8 | 3,00 | 2,70 | 2,70 | 0,30 |
| **Total** | **53,60** | | **48,24** | **5,36** |

**Charges (TVA non déductible incluse)**

| Compte | Détail | Montant |
|---|---|---|
| 6257 Réceptions | n° 1 : 167,00 HT + 1,92 | **168,92 €** |
| 6234 Cadeaux à la clientèle | n° 2 : 57,00 + 1,14 = 58,14 ; n° 3 : 145,20 (TTC) ; n° 4 : 100,00 + 2,00 = 102,00 | **305,34 €** |
| 6251 Voyages et déplacements | n° 5 : 186,00 ; n° 6 : 369,50 ; n° 7 : 38,50 (TTC, TVA non déductible) | **594,00 €** |
| 6256 Missions | n° 8 : 30,00 + 0,30 | **30,30 €** |
| **Total charges** | | **1 098,56 €** |

Contrôle : 1 098,56 + 48,24 = **1 146,80 €** = montant remboursé ✓.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6257 | Réceptions | NDF J. Delmas 09/2026 – déj. Négociants 15/09 (Girard, Royer) | 168,92 | |
| 30/09/2026 | OD | 6234 | Cadeaux à la clientèle | NDF J. Delmas 09/2026 – cadeaux Royer, Benali, 4 assistantes | 305,34 | |
| 30/09/2026 | OD | 6251 | Voyages et déplacements | NDF J. Delmas 09/2026 – train, hôtel, taxi Paris 22-24/09 | 594,00 | |
| 30/09/2026 | OD | 6256 | Missions | NDF J. Delmas 09/2026 – dîner Paris 23/09 | 30,30 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur ABS | NDF J. Delmas 09/2026 – TVA déductible (coef. 0,90) | 48,24 | |
| 30/09/2026 | OD | 4671 | J. Delmas – notes de frais | NDF J. Delmas 09/2026 (hors ticket FNAC) | | 1 146,80 |
| 12/10/2026 | BQ | 4671 | J. Delmas – notes de frais | Vir. remboursement NDF 09/2026 | 1 146,80 | |
| 12/10/2026 | BQ | 512 | Banque | Vir. remboursement NDF 09/2026 | | 1 146,80 |
| | | | | **Totaux** | **2 293,60** | **2 293,60** |

> La TVA est déduite sur la CA3 de **septembre** si les factures sont détenues à la date de dépôt (factures de biens : exigibilité à la livraison ; restauration et hôtellerie : prestations dont la TVA est exigible à l'encaissement — payées par Jean Delmas en septembre). La part non déductible (5,36 €) est incorporée aux charges. Les coefficients définitifs 2026 entraîneront une **régularisation** globale avant le 25 avril 2027 (délai à vérifier) si le coefficient définitif diffère de 0,90 de plus de la tolérance prévue.

## 4. Points d'attention / pièges

- **« C'est pour le groupe, donc tout est récupérable »** : non. L'intérêt de l'entreprise est une condition **nécessaire** mais **pas suffisante** ; les exclusions légales (logement, transport de personnes, cadeaux au-delà du seuil) s'appliquent quelle que soit la finalité. Puis le coefficient réduit encore la déduction.
- **Petit-déjeuner** inclus dans le prix de la chambre : il suit le régime de l'hébergement (exclu). Facturé séparément, il serait une prestation de restauration — analyse à faire au cas par cas.
- **Seuil des cadeaux en TTC** et **par an** : un cadeau à 68,40 € passe, un second de 10 € au même bénéficiaire dans l'année ferait tomber la déduction.
- **Reçu de taxi, ticket CB** : ce ne sont pas des factures — pas de déduction possible, quel que soit le régime.
- **Gift au président d'une filiale** (n° 3) : relation d'affaires intra-groupe ; la dépense reste fiscalement déductible si elle est dans l'intérêt de Delta Invest et non excessive — mais sans TVA récupérable.
- **Assujetti partiel** : ne jamais appliquer le coefficient sur une dépense **exclue** (0 × 0,90 = 0) ni oublier de l'appliquer sur une dépense mixte.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse à Jean Delmas (question 4) :**

> Bonjour Monsieur Delmas,
>
> Votre note de septembre est traitée ; vous serez remboursé de **1 146,80 €** le 12/10. Sur la récupération de la TVA, trois règles s'appliquent successivement :
> 1. **Exclusions légales** (CGI, annexe II, art. 206-IV) : la TVA sur l'hébergement des dirigeants et sur le transport de personnes (train, taxi) n'est jamais déductible, même pour un déplacement strictement professionnel. Les cadeaux ne le sont que s'ils n'excèdent pas 73 € TTC par bénéficiaire et par an (CGI, annexe IV, art. 28-00 A) : la caisse de champagne offerte à Karim Benali (145,20 €) est donc exclue.
> 2. **Justificatif** : seule une facture au nom de Delta Invest ouvre droit à déduction (CGI art. 271-II). Le ticket FNAC de 79,99 € ne peut pas être pris en charge en l'état : merci de nous transmettre la facture et le nom du bénéficiaire.
> 3. **Coefficient de déduction** (CGI, annexe II, art. 205 et suivants) : Delta Invest percevant des dividendes hors champ, la TVA de ses frais généraux n'est déductible qu'à 90 % (coefficient provisoire 2026).
>
> Résultat : sur 131,21 € de TVA figurant dans vos justificatifs, 48,24 € sont récupérables.

Calcul de la TVA figurant dans les justificatifs : 19,20 + 11,40 + 24,20 + 20,00 + 33,00 + 3,00 (TVA détaillée sur les factures) + 16,91 (train : 186,00 × 10 / 110) + 3,50 (taxi : 38,50 × 10 / 110) = **131,21 €**.

**Points de vigilance (question 5)** :
- **IS** : les frais de réception et cadeaux sont déductibles s'ils sont engagés dans l'intérêt de l'entreprise et justifiés (identité des bénéficiaires). Au-delà de certains montants, ils doivent figurer sur le **relevé détaillé des frais généraux** (seuils à vérifier chaque année) ; les cadeaux d'une valeur unitaire significative font l'objet d'un suivi spécifique.
- **Refacturation** : les frais de Jean liés à la Menuiserie (renégociation du PGE) pourraient être **refacturés** dans le cadre de la convention d'animation (management fees) — à vérifier dans la convention.
- **Contrôle interne** : la note de frais du président doit être **visée** par une autre personne (DG, ou associé) ; politique de frais écrite (plafonds hôtel, classe de transport, cadeaux) ; registre des cadeaux tenu par Lucie et rapproché du compte 6234 en fin d'année.
- **Conventions réglementées** : un remboursement de frais normal n'en relève pas, mais des avantages excessifs pourraient être qualifiés de rémunération (et donc d'avantage à déclarer).

**Documentation** : copie des justificatifs dans la GED, registre des cadeaux mis à jour (Royer : 68,40 € ; Benali : 145,20 € ; 4 assistantes : 30,00 € chacune), relance de Jean pour le ticket FNAC dans la liste des points en suspens.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 271 : droit à déduction (facture conforme au nom de l'assujetti).
- CGI, annexe II, art. 206-IV-2 : exclusions (logement des dirigeants et du personnel, transport de personnes, biens cédés sans rémunération au-delà d'une très faible valeur).
- CGI, annexe IV, art. 28-00 A : seuil des biens de très faible valeur (73 € TTC par bénéficiaire et par an — à vérifier).
- CGI, annexe II, art. 205 à 207 : coefficient de déduction (assujettissement, taxation, admission) et régularisations.
- CGI art. 39-1-1° et art. 39-5 / 54 quater : déductibilité des frais généraux et relevé détaillé.
- BOFiP, TVA – Droits à déduction – dépenses de restauration, d'hébergement, cadeaux.
- PCG : comptes 6234, 6251, 6256, 6257.
