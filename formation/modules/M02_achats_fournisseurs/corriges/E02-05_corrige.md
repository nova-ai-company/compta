# Corrigé E02-05 — Services numériques achetés en Allemagne et aux États-Unis

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-05](../exercices/E02-05_services-cloud-ue-usa-technova.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Question 1 — Pourquoi pas de TVA, et pourquoi en déclarer quand même ?**
Entre assujettis, une prestation de services est imposable **au lieu d'établissement du preneur** (CGI art. 259) : ici, la France. Le prestataire (allemand ou américain) n'étant pas établi en France, la TVA française est **due par le preneur assujetti** (CGI art. 283-2) : TechNova l'**autoliquide** (TVA due + TVA déductible simultanées). C'est neutre en trésorerie pour TechNova, qui a des droits à déduction complets, mais l'omission est sanctionnable (CGI art. 1788 A), et elle fausse le chiffre d'affaires déclaré au titre des opérations imposables.

**Différence UE / hors UE** :
- **Datenwerk (UE)** : c'est une **prestation de services intracommunautaire** ; elle se déclare sur la ligne spécifique de la CA3 consacrée aux achats de prestations de services intracommunautaires, et le prestataire allemand la déclare de son côté dans son état récapitulatif (recoupement entre administrations via les n° de TVA).
- **NimbusCloud (hors UE)** : même mécanisme d'autoliquidation, mais **ligne différente** de la CA3 (achats auprès d'un assujetti non établi, hors prestations intracommunautaires) ; pas d'état récapitulatif côté fournisseur. Vérifiez les lignes exactes sur le formulaire CA3 en vigueur.

**Question 2 — Exigibilité.** Pour une prestation de services, la TVA autoliquidée est exigible à l'**achèvement de la prestation** (ou à l'encaissement d'un acompte). Pour une prestation **continue** facturée par période, à la fin de chaque période. Ici, la période est septembre 2026 pour les deux factures → **CA3 de septembre 2026**. Le paiement d'octobre ne change rien.

**Question 3 — Compte.** L'hébergement cloud et l'outil de monitoring de la plateforme sont des prestations **incorporées directement** au service SaaS vendu aux clients : **604 « Achats d'études et prestations de services »**. C'est ce qui permet de calculer une **marge brute** du SaaS (CA – coût d'hébergement), indicateur suivi de près par les investisseurs de TechNova. Le 6228 (« Divers » des honoraires) range ces coûts dans les frais généraux et fausse l'analyse (et les ratios du dossier de levée de fonds). D'autres dossiers utilisent 6135 (locations) ou un sous-compte de 61 : l'essentiel est la **constance**, mais 604 est le plus juste pour un coût de production.

**Question 4 — Conversion.**
- **Comptabilité** : la facture est convertie au **cours du jour de l'opération** (date de facture / fin de période) : 18 640,00 / 1,1650 = **16 000,00 €**. Le montant débité sur la carte n'est pas le coût de la prestation : il inclut un **effet de change** (le cours a varié entre le 30/09 et le 03/10) et une **commission bancaire**.
- **TVA** : la base est convertie au taux de change publié par la BCE connu au jour de l'exigibilité (règle à vérifier dans le BOFiP — base d'imposition, opérations en devises). Hypothèse de l'énoncé : 1,1650 → base **16 000,00 €**, TVA **3 200,00 €**.

**Question 6 — Non payée au 31/12.** La dette de 18 640,00 USD serait **réévaluée** au cours du 31/12 : l'écart par rapport à 16 000,00 € serait inscrit en **écart de conversion** (476 si la dette augmente → perte latente, avec **provision pour perte de change** ; 477 si elle diminue → gain latent, non comptabilisé en résultat). Voir module M09.

## 2. Calculs (détaillés, chaque montant justifié)

| | Calcul | Montant |
|---|---|---|
| Datenwerk – base | | 1 250,00 € |
| Datenwerk – TVA autoliquidée | 1 250,00 × 20 % | **250,00 €** |
| NimbusCloud – contrôle du sous-total | 11 880 + 4 320 + 1 680 + 760 | 18 640,00 USD ✓ |
| NimbusCloud – conversion au 30/09 | 18 640,00 / 1,1650 | **16 000,00 €** |
| NimbusCloud – TVA autoliquidée | 16 000,00 × 20 % | **3 200,00 €** |
| Montant débité le 03/10 | 18 640,00 / 1,1580 = 16 096,7185 | 16 096,72 € |
| **Perte de change** | 16 096,72 – 16 000,00 | **96,72 €** |
| Commission 1,5 % | 16 096,72 × 1,5 % = 241,4508 | **241,45 €** |
| Total décaissé | 16 096,72 + 241,45 | 16 338,17 € |

La commission bancaire est un service financier **exonéré de TVA** : pas de TVA déductible.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 604 | Achats d'études et prestations de services | Datenwerk F DW-2026-09-1188 monitoring 09/2026 | 1 250,00 | |
| 30/09/2026 | AC | 445662 | TVA déductible autoliquidée (services UE) | Datenwerk F DW-2026-09-1188 autoliquidation | 250,00 | |
| 30/09/2026 | AC | 4452 | TVA due autoliquidée (services UE) | Datenwerk F DW-2026-09-1188 autoliquidation | | 250,00 |
| 30/09/2026 | AC | 401DATW | Fournisseur Datenwerk GmbH | Datenwerk F DW-2026-09-1188 | | 1 250,00 |
| 30/09/2026 | AC | 604 | Achats d'études et prestations de services | NimbusCloud INV-NC-2026-09-77351 USD 18 640 à 1,1650 | 16 000,00 | |
| 30/09/2026 | AC | 445662 | TVA déductible autoliquidée (services hors UE) | NimbusCloud INV-NC-2026-09-77351 autoliquidation | 3 200,00 | |
| 30/09/2026 | AC | 4452 | TVA due autoliquidée (services hors UE) | NimbusCloud INV-NC-2026-09-77351 autoliquidation | | 3 200,00 |
| 30/09/2026 | AC | 401NIMB | Fournisseur NimbusCloud Inc. | NimbusCloud INV-NC-2026-09-77351 (USD 18 640,00) | | 16 000,00 |
| 03/10/2026 | BQ | 401NIMB | Fournisseur NimbusCloud Inc. | CB NimbusCloud INV-NC-2026-09-77351 | 16 000,00 | |
| 03/10/2026 | BQ | 666 | Pertes de change | CB NimbusCloud – écart de change 1,1650 / 1,1580 | 96,72 | |
| 03/10/2026 | BQ | 627 | Services bancaires et assimilés | Commission paiement devise 1,5 % | 241,45 | |
| 03/10/2026 | BQ | 512 | Banque | CB NimbusCloud + commission | | 16 338,17 |
| 05/10/2026 | BQ | 401DATW | Fournisseur Datenwerk GmbH | Prlv SEPA Datenwerk DW-2026-09-1188 | 1 250,00 | |
| 05/10/2026 | BQ | 512 | Banque | Prlv SEPA Datenwerk DW-2026-09-1188 | | 1 250,00 |
| | | | | **Totaux** | **38 288,17** | **38 288,17** |

> Utilisez des **sous-comptes distincts** de 4452 et 445662 pour les services UE et les services hors UE (par exemple 44521 / 44522) : ils alimentent des lignes différentes de la CA3 et facilitent le rapprochement mensuel. Dans le FEC, renseignez Montantdevise (18640,00) et Idevise (USD) sur les lignes NimbusCloud.

**Sur la CA3 de septembre 2026** : bases 1 250,00 € (services UE) et 16 000,00 € (services hors UE), TVA due 3 450,00 € ; TVA déductible 3 450,00 € ; effet net nul.

## 4. Points d'attention / pièges

- **Le montant débité sur la carte n'est pas le montant de la facture** : il mélange le prix, le change et les frais. Toujours comptabiliser la facture au cours du jour, puis le règlement.
- **Ne pas autoliquider sur la commission bancaire** (service financier exonéré, rendu par une banque française).
- **Vérifier l'entité qui facture** : les grands fournisseurs de cloud facturent souvent les clients européens depuis une filiale **établie dans l'UE** (Irlande, Luxembourg) ; la facture devient alors une prestation intracommunautaire (autre ligne de la CA3). Lisez l'en-tête, pas le nom commercial.
- **Si un prestataire étranger facture de la TVA française** (parce qu'il est immatriculé en France pour d'autres opérations, B2C notamment) : en B2B avec un preneur français, c'est en principe le preneur qui doit autoliquider ; exiger une facture conforme plutôt que de déduire une TVA facturée à tort.
- **Prestations continues** : une facture annuelle payée d'avance déclenche l'exigibilité à l'**encaissement de l'acompte** (paiement), et non à la fin de la période.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Fiche « mode d'emploi » pour Émilie (question 7) :**

> 1. Facture **sans TVA** d'un fournisseur **non établi en France** → autoliquidation : 4452 au crédit + 445662 au débit, 20 % du HT en euros.
> 2. **UE** et **hors UE** : sous-comptes distincts (lignes CA3 différentes).
> 3. Mois de déclaration : celui de la **fin de la période de service** (ou du paiement d'avance), pas celui du paiement.
> 4. Facture en devise : cours **du jour de la facture** ; l'écart au paiement va en **666 / 766** ; la commission bancaire en **627**, sans TVA.
> 5. Coûts d'hébergement et outils de la plateforme : **604** (coût de production du SaaS), pas 6228.
> 6. Vérifier chaque mois l'en-tête : une filiale UE du même fournisseur change la ligne de la CA3.

**Contrôles de révision** : rapprochement mensuel 4452 / 445662 (soldes nets identiques dans les deux comptes) et lignes de la CA3 ; revue annuelle de la liste des fournisseurs étrangers ; vérification du chiffre d'affaires « autoliquidé » déclaré vs comptes 604 / 61 alimentés par des fournisseurs étrangers.

**Point CIR** : les coûts d'hébergement de l'environnement de **R&D** (distinct de la production) peuvent entrer dans l'assiette du CIR selon les règles en vigueur : demander à Émilie de séparer les comptes cloud « production » et « R&D » chez NimbusCloud.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 259 : lieu des prestations de services entre assujettis (preneur).
- CGI art. 283-2 : autoliquidation par le preneur assujetti lorsque le prestataire n'est pas établi en France.
- CGI art. 269-2-a et 269-2-c, et BOFiP TVA – exigibilité des prestations autoliquidées et des prestations continues.
- BOFiP, TVA – base d'imposition – conversion des opérations en devises (taux de change à retenir — à vérifier).
- CGI art. 1788 A : sanctions.
- PCG : comptes 604, 666, 766, 627 ; conversion des dettes en devises et écarts de conversion (476 / 477) — module M09.
