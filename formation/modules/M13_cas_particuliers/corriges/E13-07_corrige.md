# Corrigé E13-07 — Mode & Co : déclaration OSS du 3e trimestre et correction d'un trimestre déjà déposé

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E13-07](../exercices/E13-07_mode-co-regularisation-oss.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Question 1 — Le principe.** Depuis le 01/07/2021, les **ventes à distance intracommunautaires de biens** à des non-assujettis sont imposables dans l'**État d'arrivée** dès que le total annuel de ces ventes dépasse **10 000 € HT** dans l'UE (CGI art. 258 A). Mode & Co dépasse ce seuil : les ventes aux particuliers belges sont imposables **en Belgique, au taux belge** (21 %), déclarées via l'**OSS** en France. La TVA française n'était pas due.

**Qui supporte le coût ?** Les prix sont **TTC identiques** dans toute l'UE : le client belge a payé ce qu'il devait payer. La base imposable se recalcule donc **en dedans** du prix TTC encaissé, au taux belge : la TVA due augmente (21 % au lieu de 20 %) et le chiffre d'affaires HT baisse d'autant. **Mode & Co supporte la différence** ; on ne refacture rien au client.

**Question 2 — Correction ou déclaration courante ?**
- **Avril-juin 2026** : période déjà déclarée (OSS T2 déposée le 28/07) → **correction** de la déclaration du T2, portée dans une **déclaration ultérieure** (celle du T3), dans la rubrique « corrections », pour l'État **BE** et la période **T2 2026**. On ne redépose pas la déclaration du T2 (corrections possibles pendant **3 ans**).
- **Juillet 2026** : le T3 n'est pas encore déclaré → les ventes belges de juillet sont simplement **déclarées dans le T3**, avec la bonne base et le bon taux. Pas de « correction » au sens OSS.
- **Avoir allemand** : la vente initiale (24/06) a été déclarée au T2 ; la réduction de base intervient au T3 (retour le 12/07). La pratique recommandée par la doctrine européenne (guide OSS de la Commission) et reprise par l'administration française est de traiter la diminution comme une **correction de la période d'origine** (DE, T2, − 38,00 €) dans la rubrique corrections de la déclaration suivante — *certains États membres admettant l'imputation sur la période courante, à vérifier au moment du dépôt ; en tout état de cause, ne pas compter l'avoir deux fois*.

**Question 4 — La TVA française.** Elle a été déclarée et payée à tort sur les CA3 d'avril à juillet (2 420,00 + 806,67 = 3 226,67 €). Elle est récupérable : par **imputation** sur une CA3 ultérieure (ligne de régularisation « autre TVA à déduire », avec mention explicative dans le cadre réservé à la correspondance) ou par **réclamation contentieuse** (délai jusqu'au 31 décembre de la 2e année suivant le versement). Pour un montant modeste et une erreur documentée, l'imputation sur la **CA3 de septembre** (à déposer en octobre) est la solution pratique, **dans le même mois** que le paiement de la TVA belge : la position de trésorerie reste neutre, et la piste d'audit est claire.

**Pas de nouvelle facture au client** : les factures de vente à distance B2C ne sont pas obligatoires dans tous les cas, mais Shopify en émet ; pour les clients qui en font la demande (comme celui-ci), émettre une **facture rectificative** mentionnant la TVA belge à 21 %.

## 2. Calculs (détaillés, chaque montant justifié)

**Correction du T2 — Belgique**

| | Calcul | Montant |
|---|---|---|
| Ventes TTC encaissées | | 14 520,00 € |
| Base HT correcte | 14 520,00 / 1,21 | 12 000,00 € |
| TVA BE due | 14 520,00 − 12 000,00 | **2 520,00 €** |
| TVA FR déclarée à tort | | 2 420,00 € |
| HT comptabilisé à tort | | 12 100,00 € (soit − 100,00 € de CA) |

**Belgique — juillet (déclaré au T3)** : 4 840,00 / 1,21 = 4 000,00 € HT ; TVA 840,00 € (au lieu de 4 033,33 € HT et 806,67 € de TVA FR comptabilisés, soit − 33,33 € de CA).

**Déclaration OSS du 3e trimestre 2026**

| État | Base HT | Taux | TVA |
|---|---|---|---|
| DE | 41 650,00 / 1,19 = 35 000,00 € | 19 % | 6 650,00 € |
| IT | 22 570,00 / 1,22 = 18 500,00 € | 22 % | 4 070,00 € |
| ES | 16 940,00 / 1,21 = 14 000,00 € | 21 % | 2 940,00 € |
| BE | (10 890,00 + 4 840,00) / 1,21 = 9 000,00 + 4 000,00 = 13 000,00 € | 21 % | 1 890,00 + 840,00 = 2 730,00 € |
| NL | 7 260,00 / 1,21 = 6 000,00 € | 21 % | 1 260,00 € |
| **Total T3** | **86 500,00 €** | | **17 650,00 €** |

**Rubrique « corrections » (périodes antérieures)**

| État | Période d'origine | Correction de TVA |
|---|---|---|
| BE | T2 2026 | + 2 520,00 € |
| DE | T2 2026 | − 38,00 € (avoir AV-2026-0412) |

**Montant à payer** : 17 650,00 + 2 520,00 − 38,00 = **20 132,00 €**, dépôt et paiement **au plus tard le 31/10/2026** (la date limite étant un samedi, anticipez : le paiement doit être *reçu* à la date limite, avec la référence de la déclaration).

**TVA française à récupérer** : 2 420,00 + 806,67 = **3 226,67 €**.
**Coût de l'erreur pour Mode & Co** : 100,00 + 33,33 = **133,33 €** de chiffre d'affaires HT en moins (la TVA payée en plus en Belgique, 2 520 + 840 = 3 360,00 €, n'est compensée qu'à hauteur de 3 226,67 € récupérés en France).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 44571 | TVA collectée France | Ventes BE avr.-juin : TVA FR à tort | 2 420,00 | |
| 30/09/2026 | OD | 7071 | Ventes de marchandises – UE B2C | Ventes BE avr.-juin : recalcul HT à 21 % | 100,00 | |
| 30/09/2026 | OD | 4457OSS-BE | TVA due OSS – Belgique | Ventes BE avr.-juin : TVA BE 21 % (correction T2) | | 2 520,00 |
| 30/09/2026 | OD | 44571 | TVA collectée France | Ventes BE juillet : TVA FR à tort | 806,67 | |
| 30/09/2026 | OD | 7071 | Ventes de marchandises – UE B2C | Ventes BE juillet : recalcul HT à 21 % | 33,33 | |
| 30/09/2026 | OD | 4457OSS-BE | TVA due OSS – Belgique | Ventes BE juillet : TVA BE 21 % | | 840,00 |
| 30/10/2026 | BQ | 4457OSS-DE | TVA due OSS – Allemagne | OSS T3 2026 (6 650,00 − correction T2 38,00) | 6 612,00 | |
| 30/10/2026 | BQ | 4457OSS-IT | TVA due OSS – Italie | OSS T3 2026 | 4 070,00 | |
| 30/10/2026 | BQ | 4457OSS-ES | TVA due OSS – Espagne | OSS T3 2026 | 2 940,00 | |
| 30/10/2026 | BQ | 4457OSS-BE | TVA due OSS – Belgique | OSS T3 2026 (2 730,00 + correction T2 2 520,00) | 5 250,00 | |
| 30/10/2026 | BQ | 4457OSS-NL | TVA due OSS – Pays-Bas | OSS T3 2026 | 1 260,00 | |
| 30/10/2026 | BQ | 512 | Banque | Paiement OSS T3 2026 – référence de la déclaration | | 20 132,00 |
| | | | | **Totaux** | **23 492,00** | **23 492,00** |

*Les ventes du T3 (août-septembre et autres pays) ont déjà été comptabilisées par l'export Shopify dans les bons comptes ; l'avoir allemand aussi (le 4457OSS-DE a été débité de 38,00 € en juillet, d'où un solde de 6 612,00 € à payer). La récupération des 3 226,67 € de TVA française ne donne pas lieu à une écriture distincte : le 44571 ayant été débité ci-dessus, la CA3 de septembre fait apparaître ce montant en régularisation (« autre TVA à déduire ») et l'écriture de liquidation de la CA3 solde les comptes comme d'habitude.*

**Sur la CA3** : les ventes OSS (86 500,00 € pour le T3, ventilées par mois) figurent dans les **opérations non imposables** en France (ligne des ventes à distance taxables dans un autre État membre) ; régularisation de 3 226,67 € sur la CA3 de septembre avec une note explicative.

## 4. Points d'attention / pièges

- **Ne jamais « modifier » une déclaration OSS déposée** : la correction passe par la déclaration suivante, rubrique dédiée, par État et période d'origine.
- **Recalcul en dedans** : le prix TTC encaissé ne change pas ; c'est la base HT qui baisse. Erreur fréquente : appliquer 21 % sur l'ancien HT (12 100 × 21 % = 2 541 €) → faux.
- **Double récupération** : la TVA française et la TVA belge portent sur les mêmes ventes ; si l'on ne récupère pas la TVA française, on paie deux fois.
- **Avoirs** : vérifier qu'un avoir n'est ni oublié ni compté deux fois (en correction du T2 **et** en diminution du T3).
- **Taux** : un taux réduit peut s'appliquer dans certains États (vêtements pour enfants dans certains pays, par exemple) ; vérifier le paramétrage par catégorie de produits et par pays.
- **Délai de paiement** : la TVA OSS est payée en une seule fois à la DGFiP, avec la référence unique de la déclaration ; un paiement tardif ou mal référencé expose à des relances de chaque État membre.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse au client belge (préparée pour Inès) :**

> Bonjour, merci de nous l'avoir signalé : une erreur de paramétrage a fait apparaître la TVA française au lieu de la TVA belge (21 %) sur votre facture. Le prix payé ne change pas ; vous trouverez ci-joint une facture rectificative. Toutes nos excuses pour ce désagrément.

**Note à Inès :**
> 1. L'erreur est corrigée sur la déclaration OSS du 3e trimestre (20 132 € à payer avant le 31/10) ; la TVA française payée à tort (3 226,67 €) est récupérée sur la CA3 de septembre. Coût net pour vous : environ 133 € de marge.
> 2. **Contrôles à mettre en place** : après toute modification du site, extraire un rapport « ventes par pays de livraison × taux appliqué » et le comparer au tableau des taux ; rapprochement trimestriel **CA UE de Shopify = base OSS déclarée** ; liste des avoirs du trimestre rapprochée des ventes d'origine ; validation par le cabinet avant chaque dépôt OSS.
> 3. **Marketplace** : vérifier si la marketplace collecte elle-même la TVA sur certaines ventes (elle ne le fait que dans les cas où elle est « fournisseur présumé », a priori pas pour vous, vendeur établi en France) ; ces ventes ne doivent pas figurer deux fois.

**Documentation** : copie des déclarations OSS T2 et T3, accusé de paiement, export Shopify par pays, preuve de la date de correction du paramétrage (ticket du prestataire), tableau de rapprochement CA / OSS / CA3, factures rectificatives émises.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 258 A et 259 D (ventes à distance intracommunautaires de biens, seuil de 10 000 €) ; art. 298 sexdecies F et suivants (régimes particuliers de guichet unique) ; art. 289 (facturation).
- Directive 2006/112/CE, art. 33 et 369 bis à 369 duodecies (régime de l'Union) ; règlement d'exécution (UE) n° 282/2011 (corrections, art. 61).
- Commission européenne : notes explicatives sur les règles de TVA applicables au commerce électronique et guide du guichet unique (OSS) — corrections et ajustements.
- CGI art. 271 et ann. II (imputation de la TVA) ; LPF art. R* 196-1 (réclamations).
- BOFiP : BOI-TVA-SECT-80 (régimes particuliers OSS / IOSS).
