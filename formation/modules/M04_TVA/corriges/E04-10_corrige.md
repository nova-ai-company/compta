# Corrigé E04-10 — Rapprochement CA comptable / CA déclaré : expliquer l'écart

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-10](../exercices/E04-10_coherence-ca-tva.md)

## 1. Analyse

**a) La méthode.** On part du **chiffre d'affaires comptable** de l'exercice (ventilé par taux) et on le transforme, élément par élément, en **base imposable théorique** de la période, que l'on compare au **cumul des bases déclarées** sur les CA3 de la même période. Pour une entreprise de services à la TVA sur les encaissements, les principaux éléments de passage sont :

| Élément | Sens | Pourquoi |
|---|---|---|
| Variation des **PCA** (clôture – ouverture) | + | Abonnements encaissés (donc taxés) mais dont le produit est reporté |
| Variation des **créances sur prestations** (HT) | – | Prestations comptabilisées en produit mais pas encore encaissées (TVA non exigible) |
| **Cessions d'immobilisations** avec TVA | + | Taxables mais comptabilisées en 775, hors CA |
| **Bons à usage unique** vendus non utilisés | + | TVA exigible à la vente du bon, produit différé (4191) |
| Avoirs, ventes exonérées, autoliquidées… | ± | Selon les cas |

Le **résidu** doit être nul ou expliqué ; tout résidu inexpliqué est soit une erreur déclarative, soit une erreur comptable.

**b) Les éléments du dossier**
- **PCA** : passent de 39 900 € à 46 500 € → + 6 600 € de prestations encaissées et taxées dans l'exercice mais non comptabilisées en produit. **Justifié.**
- **Créances adhérents** : 6 000 € → 8 400 € TTC, soit + 2 400 € TTC (+ 2 000 € HT) de prestations comptabilisées mais non encaissées. **Justifié** (TVA en attente — à vérifier : ces sommes devraient figurer en 44574).
- **Cession des appareils** : 6 000 € HT taxés à 20 % en mars, en 775. **Justifié** (ligne A2 « autres opérations imposables » sur la CA3, ou A1 selon la pratique).
- **Bons cadeaux « 3 mois d'abonnement »** : le lieu (FitClub Villeurbanne), la nature (abonnement) et donc le taux (20 %) sont connus dès l'émission → **bons à usage unique** : TVA exigible **à la vente du bon** (4 150 € HT), le produit étant différé jusqu'à l'utilisation. **Justifié** — le traitement du logiciel est correct.
- **Résidu : 1 250 € HT** = l'**avoir** de juillet, comptabilisé (706100 net) mais **non pris en compte** sur la CA3 de juillet. **Erreur déclarative** : la TVA de 250 € a été déclarée et payée en trop.

**c) Le solde débiteur de 250 € du 44571.** Les écritures de liquidation de TVA ont été passées à partir des montants des CA3 : le 44571 a été soldé pour le montant **déclaré** (qui ignorait l'avoir), alors que la comptabilité avait déjà débité le 44571 de 250 € lors de la saisie de l'avoir. Il reste donc un débit de 250 € : c'est une **créance sur l'État** (TVA payée en trop), cohérente avec le résidu du rapprochement. Les deux contrôles se confirment mutuellement.

## 2. Calculs

**Tableau de passage — taux de 20 %**

| Élément | Montant HT |
|---|---|
| Abonnements (706100, net de l'avoir) | 612 400,00 |
| Frais d'inscription (706200) | 18 600,00 |
| Coaching (706300) | 41 200,00 |
| Accessoires et textiles (707200) | 25 200,00 |
| **CA comptable à 20 %** | **697 400,00** |
| + Variation des PCA (46 500 – 39 900) | + 6 600,00 |
| – Variation des créances adhérents HT ((8 400 – 6 000) / 1,2) | – 2 000,00 |
| + Cession d'immobilisations taxée (775) | + 6 000,00 |
| + Bons à usage unique vendus non utilisés (4191) | + 4 150,00 |
| **= Base taxable théorique à 20 %** | **712 150,00** |
| Base déclarée (cumul des 12 CA3) | 713 400,00 |
| **Écart (déclaré – théorique)** | **+ 1 250,00** |
| Explication : avoir du 12/07/2026 non déclaré | 1 250,00 |
| **Résidu inexpliqué** | **0,00** |

TVA : théorique 712 150 × 20 % = 142 430,00 € ; déclarée 142 680,00 € → **250,00 € payés en trop**.

**Taux de 5,5 %** : CA comptable 9 600 € (ventes de biens, TVA exigible à la livraison, sans PCA ni bons) = base déclarée 9 600 € ; TVA 528 € = 9 600 × 5,5 % ✔. **Aucun écart.**

**Contrôle du 44571** : solde débiteur de 250 € = TVA de l'avoir non déclarée ✔.

## 3. Écritures comptables

La correction est **déclarative** (récupérer 250 € sur la prochaine CA3) ; en comptabilité, on reclasse le solde anormal du 44571 dans un compte de TVA à régulariser, soldé lors de la liquidation de la CA3 de septembre 2026.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/08/2026 | OD | 4458 | TVA à régulariser – à récupérer (ligne 21 CA3) | Avoir adhérent 12/07/2026 non déclaré sur CA3 07/2026 | 250,00 | |
| 31/08/2026 | OD | 44571 | TVA collectée | Reclassement du solde débiteur | | 250,00 |
| 30/09/2026 | OD | 44551 | TVA à décaisser | CA3 09/2026 – imputation ligne 21 | 250,00 | |
| 30/09/2026 | OD | 4458 | TVA à régulariser – à récupérer | CA3 09/2026 – imputation ligne 21 | | 250,00 |
| | | | | **Totaux** | **500,00** | **500,00** |

Au bilan du 31/08/2026, les 250 € figurent en **créance sur l'État** (autres créances), et le 44571 est soldé.

## 4. Points d'attention / pièges

- **Correction** : porter 250 € en ligne **21 « Autre TVA à déduire »** de la CA3 de septembre 2026 (déposée en octobre), en précisant dans la zone de commentaire qu'il s'agit de la régularisation de l'avoir du 12/07/2026 — ou, si l'on préfère, minorer la base de la période. Délai : une régularisation en faveur de l'entreprise est possible jusqu'au 31/12 de la 2e année suivant celle du versement. Pas d'intérêt de retard : l'erreur est **en faveur de l'État**.
- **Ne pas confondre** les éléments de passage justifiés (PCA, créances, cession, bons) avec des erreurs : ils doivent être **documentés** (balance N et N-1, détail des PCA, liste des bons non utilisés, facture de cession).
- **Créances adhérents** : la TVA correspondante (8 400 / 6 = 1 400 €) devrait apparaître en **44574** (TVA en attente). Vérifier ce compte : s'il n'existe pas, le logiciel déclare peut-être la TVA à la facturation (ce qui expliquerait un autre type d'écart) — ici le rapprochement montre que la TVA a bien été déclarée à l'encaissement.
- **Bons cadeaux** : un bon utilisable sur toute la gamme (abonnements à 20 % **et** compléments à 5,5 %) serait un bon **à usages multiples** : pas de TVA à la vente, TVA à l'utilisation. La qualification change le rapprochement.
- **Cession d'immobilisation** : vérifier la ligne utilisée sur la CA3 (A2 ou A1 selon la pratique) ; la base de 6 000 € doit apparaître quelque part.

## 5. Ce qu'un senior ferait en plus

**Conclusion de la feuille de travail** :
> Rapprochement CA / TVA de l'exercice clos le 31/08/2026 : CA comptable à 20 % de 697 400 € ; base théorique de 712 150 € après prise en compte de la variation des PCA (+ 6 600 €), des créances adhérents (– 2 000 € HT), de la cession d'appareils (+ 6 000 €) et des bons à usage unique non utilisés (+ 4 150 €). Base déclarée : 713 400 €. Écart de 1 250 € intégralement expliqué par l'avoir du 12/07/2026 non repris dans la CA3 de juillet : TVA payée en trop de 250 €, régularisée sur la CA3 de septembre 2026 (ligne 21). Taux de 5,5 % : concordance. Solde débiteur du 44571 (250 €) expliqué et reclassé. Aucun risque fiscal identifié ; amélioration du processus recommandée.

**Réponse à Romain Faure** :
> Le logiciel calcule correctement la TVA de ce qu'il connaît ; mais l'avoir de juillet, saisi en comptabilité, ne figurait pas dans l'état utilisé pour la déclaration : vous avez payé 250 € de trop, que nous récupérons sur la déclaration de septembre. Pour éviter que cela se reproduise, nous vous proposons de préparer les CA3 à partir de la comptabilité, après un contrôle mensuel entre l'état du logiciel et les comptes de TVA.

**Mise en place** : rapprochement **mensuel** 44571 / 44574 / état du logiciel avant chaque dépôt ; tableau de passage annuel archivé dans le dossier de révision (pièce maîtresse en cas de contrôle).

## 6. Références

- CGI : art. 269-2-c (exigibilité des prestations de services), art. 271 et 272-1 (régularisations en cas de réduction de prix), règles relatives aux bons (transposition de la directive (UE) 2016/1065, applicable depuis le 01/01/2019).
- LPF : art. L. 190 et R. 196-1 (réclamations).
- PCG : comptes 487, 4191, 4458, 44571, 44574, 775.
- BOFiP : TVA-BASE (bons à usage unique et à usages multiples), TVA-DECLA (régularisations sur déclaration ultérieure).
