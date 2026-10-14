# Corrigé E06-10 — La presse numérique : plan dégressif fiscal et amortissements dérogatoires

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-10](../exercices/E06-10_degressif-derogatoire-imprimerie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — Base amortissable (question 1).** Coût = presse 342 000 + transport 4 500 + installation et mise au point 13 500 = **360 000,00 €**. La **formation** (5 800 €) est exclue du coût (charge). Valeur résiduelle : non significative.

**Étape 2 — Pourquoi un plan comptable linéaire.** Le plan d'amortissement comptable doit refléter le **rythme de consommation** des avantages économiques. La presse produira un volume **régulier** sur 8 ans : le mode **linéaire** s'impose en comptabilité. Le dégressif est un **avantage fiscal** (CGI, art. 39 A) ; pour en bénéficier sans fausser le résultat comptable, on comptabilise l'écart en **amortissements dérogatoires** — provision réglementée inscrite en capitaux propres (145). Le CAC a raison.

**Étape 3 — Deux points de départ.**
- **Linéaire (comptable)** : date de **mise en service** = 01/07/2026 → 6 mois en 2026 ; fin le 30/06/2034.
- **Dégressif (fiscal)** : **premier jour du mois d'acquisition** = 01/05/2026 (livraison et transfert de propriété le 12/05) → 8 mois en 2026 ; fin le 30/04/2034.
Sabine a pris la mise en service pour le dégressif : erreur, elle s'est privée de 2 mois de dégressif.

**Étape 4 — Taux dégressif.** Durée 8 ans → taux linéaire 12,5 % ; coefficient **2,25** (durée > 6 ans) → **28,125 %**. Passage au linéaire dès que VNC × 28,125 % < VNC / durée restante, c'est-à-dire quand la durée restante devient inférieure à 1 / 0,28125 ≈ 3,56 ans.

## 2. Calculs (détaillés, chaque montant justifié)

**Plan comptable (question 2)** : 360 000 / 8 = 45 000 €/an.

| Exercice | Dotation linéaire | Cumul | VNC comptable |
|---|---:|---:|---:|
| 2026 (6 mois) | 22 500,00 | 22 500,00 | 337 500,00 |
| 2027 à 2033 (par an) | 45 000,00 | 67 500 → 337 500 | 292 500 → 22 500 |
| 2034 (6 mois) | 22 500,00 | 360 000,00 | 0,00 |

**Plan fiscal dégressif (question 3)** — durée restante comptée à partir du 01/05/2026 (8 ans).

| Exercice | Durée restante au 1er janvier | Annuité dégressive (VNC × 28,125 %) | Annuité linéaire sur durée restante | **Annuité retenue** | VNC fiscale fin |
|---|---:|---:|---:|---:|---:|
| 2026 (8 mois) | 8,00 | 360 000 × 28,125 % × 8/12 | — | **67 500,00** | 292 500,00 |
| 2027 | 7,33 | 82 265,63 | 39 886,36 | **82 265,63** | 210 234,37 |
| 2028 | 6,33 | 59 128,42 | 33 194,90 | **59 128,42** | 151 105,95 |
| 2029 | 5,33 | 42 498,55 | 28 332,37 | **42 498,55** | 108 607,40 |
| 2030 | 4,33 | 30 545,83 | 25 063,25 | **30 545,83** | 78 061,57 |
| 2031 | 3,33 | 21 954,82 | **23 418,47** | **23 418,47** (passage au linéaire) | 54 643,10 |
| 2032 | 2,33 | — | 23 418,47 | **23 418,47** | 31 224,63 |
| 2033 | 1,33 | — | 23 418,47 | **23 418,47** | 7 806,16 |
| 2034 (4 mois) | 0,33 | — | 23 418,47 × 4/12 | **7 806,16** | 0,00 |
| **Total** | | | | **360 000,00** | |

(Passage au linéaire en 2031 : 54 643,10 + 23 418,47 = 78 061,57 ÷ 3,333 = 23 418,47 > 21 954,82.)

**Amortissements dérogatoires (question 4)**

| Exercice | Fiscal | Comptable | Dotation 6872 | Reprise 7872 | Solde 145 fin |
|---|---:|---:|---:|---:|---:|
| 2026 | 67 500,00 | 22 500,00 | **45 000,00** | | 45 000,00 |
| 2027 | 82 265,63 | 45 000,00 | 37 265,63 | | 82 265,63 |
| 2028 | 59 128,42 | 45 000,00 | 14 128,42 | | 96 394,05 |
| 2029 | 42 498,55 | 45 000,00 | | 2 501,45 | 93 892,60 |
| 2030 | 30 545,83 | 45 000,00 | | 14 454,17 | 79 438,43 |
| 2031 | 23 418,47 | 45 000,00 | | 21 581,53 | 57 856,90 |
| 2032 | 23 418,47 | 45 000,00 | | 21 581,53 | 36 275,37 |
| 2033 | 23 418,47 | 45 000,00 | | 21 581,53 | 14 693,84 |
| 2034 | 7 806,16 | 22 500,00 | | 14 693,84 | 0,00 |
| **Total** | **360 000,00** | **360 000,00** | **96 394,05** | **96 394,05** | |

Contrôle de l'**amortissement minimal** (CGI, art. 39 B) : le cumul fiscal (comptable + dérogatoires) reste chaque année ≥ au cumul linéaire (ex. fin 2033 : 352 193,84 ≥ 337 500,00) ✓.

**Question 6 — IS 2026** : déduction fiscale 2026 = 22 500 + 45 000 = 67 500 € (contre 51 440,63 € dans la version de Sabine). Le dérogatoire de 45 000 € réduit l'IS 2026 de 45 000 × 25 % = **11 250 €**. Mais dès 2029, les reprises (7872) sont **imposables** : sur la durée totale, la déduction fiscale est exactement de 360 000 €, comme en linéaire. C'est un **décalage d'impôt** (gain de trésorerie, financement gratuit par l'État), non une économie définitive — sauf si le taux d'IS baisse entre-temps ou si l'entreprise est déficitaire au moment des reprises.

**Participation** : la réserve spéciale de participation se calcule à partir du **bénéfice fiscal** (B) ; les dérogatoires, en réduisant B en 2026-2028, **réduisent la participation** de ces exercices (et l'augmentent lors des reprises). À expliquer au CSE si la question est posée.

## 3. Écritures comptables

Écritures de correction au 31/12/2026 (la facture a été saisie par Sabine pour 365 800 € en 2154 avec 73 160 € en 44562) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 618 | Divers – formation du personnel (subdivision selon la nomenclature 2025 du PCG) | DPE-26-00418 reclass. formation opérateurs | 5 800,00 | |
| 31/12/2026 | OD | 2154 | Matériel industriel | Reclass. formation hors coût presse | | 5 800,00 |
| 31/12/2026 | OD | 44566 | TVA sur autres biens et services | Reclass. TVA formation | 1 160,00 | |
| 31/12/2026 | OD | 44562 | TVA sur immobilisations | Reclass. TVA formation | | 1 160,00 |
| 31/12/2026 | OD | 28154 | Amortissements du matériel industriel | Annulation excédent dotation dégressive (51 440,63 – 22 500,00) | 28 940,63 | |
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Ramené au linéaire 6 mois | | 28 940,63 |
| 31/12/2026 | OD | 6872 | Dotations aux provisions réglementées (immobilisations) | Dérogatoire presse DP-B2-26-1187 | 45 000,00 | |
| 31/12/2026 | OD | 145 | Amortissements dérogatoires | Dérogatoire presse 2026 | | 45 000,00 |
| | | | | **Totaux** | **80 900,63** | **80 900,63** |

Situation après correction : 2154 = 360 000,00 ; 28154 (presse) = 22 500,00 ; 145 = 45 000,00 ; charges 2026 liées à la presse = 22 500 (6811) + 45 000 (6872) + 5 800 (formation) = 73 300,00 €.

## 4. Points d'attention / pièges

- **Prorata dégressif** : au mois d'**acquisition** (pas à la mise en service, pas au jour près).
- **Coefficient** : 2,25 au-delà de 6 ans — vérifier chaque année qu'aucun coefficient majoré temporaire n'est applicable (il y en a eu par le passé).
- **Dégressif en comptabilité** : possible seulement si le rythme de consommation est réellement décroissant (obsolescence technologique rapide, usage intensif en début de vie) — à justifier. Ici, le CAC refuse à juste titre.
- **Le dérogatoire suppose un plan fiscal ≥ plan comptable en début de vie** ; on ne peut pas passer un dérogatoire « pour optimiser » une année puis l'oublier : il faut le **suivre jusqu'au bout** (reprises) — d'où la nécessité de paramétrer le fichier des immobilisations avec les **deux plans**.
- **Présentation** : 145 est en **capitaux propres** (provisions réglementées) ; 6872 / 7872 en résultat exceptionnel ; la liasse reprend les dérogatoires sur les tableaux des amortissements et des provisions (2055 / 2056).
- **Question 7 — vente le 30/06/2029** : (1) amortissement comptable jusqu'au 30/06/2029 (6 mois : 22 500 €) ; (2) pas d'annuité dégressive fiscale au titre de l'exercice de cession selon la doctrine (*règle à vérifier dans le BOFiP*) ; en pratique, on solde le 145 en **reprise intégrale** (7872) à la date de cession, ce qui réintègre dans le résultat l'avance fiscale obtenue ; (3) sortie du bien (675 / 775) ; (4) la plus-value **fiscale** = prix – VNC fiscale ; le résultat comptable de cession plus la reprise du dérogatoire en donnent l'équivalent.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à Sabine Morel**

> Bonjour Sabine,
>
> Comme le suggère Audit Rhône-Alpes, nous ramenons la presse au linéaire en comptabilité (22 500 € en 2026, mise en production au 01/07) et nous constatons l'avantage fiscal en amortissement dérogatoire. Bonne nouvelle : le point de départ fiscal du dégressif est le mois d'acquisition (mai), et non la mise en production : la déduction fiscale 2026 atteint 67 500 €, contre 51 441 € dans votre calcul, soit environ 4 000 € d'IS en moins par rapport à votre version.
>
> La formation des opérateurs (5 800 €) sort du coût de la presse : c'est une charge.
>
> Le plan complet ci-joint montre que les dérogatoires seront repris à partir de 2029 : merci de paramétrer les deux plans (comptable et fiscal) dans votre logiciel d'immobilisations pour que les dotations et reprises soient calculées automatiquement.

**Contrôles et documentation**
- Rapprocher le 145 du fichier (total des dérogatoires par bien) chaque année.
- Préparer pour le CAC la feuille de travail : facture, PV de réception, plan comptable, plan fiscal, tableau des dérogatoires.
- Vérifier le traitement de l'**acompte de 30 %** versé à la commande (238, imputé à la facture) et le respect des délais de paiement (45 jours).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI, art. 39 A et annexe II (biens éligibles, coefficients, point de départ au premier jour du mois d'acquisition) ; BOFiP, BIC – Amortissements – amortissement dégressif.
- CGI, art. 39 B : amortissement minimal ; connexion fiscalo-comptable des amortissements dérogatoires.
- PCG : plan d'amortissement reflétant la consommation des avantages ; provisions réglementées (145, 6872, 7872).
- Code du travail, art. L. 3324-1 : calcul de la réserve spéciale de participation (bénéfice fiscal).
