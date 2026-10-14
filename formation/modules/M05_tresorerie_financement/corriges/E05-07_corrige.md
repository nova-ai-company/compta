# Corrigé E05-07 — Vider le compte d'attente de TechNova avant la levée de fonds

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-07](../exercices/E05-07_vider-471-technova.md)

## 1. Analyse

Le 471 n'est ni un actif ni un passif : c'est une **file d'attente**. Chaque ligne y est parce qu'on ignorait sa nature au moment de l'import. Pour le solder, on traite **ligne par ligne** : identifier la pièce, déterminer la contrepartie, vérifier si la contrepartie avait déjà été enregistrée ailleurs (dans ce cas, on **lettre**, on ne recompte pas la charge ou le produit).

### Identification ligne par ligne

| N° | Opération | Contrepartie | Justification |
|---|---|---|---|
| 1 | Solde de l'avance remboursable Bpifrance | **1674** Avances conditionnées de l'État | Remboursable en cas de succès : c'est une dette (comme la première tranche) ; ni subvention ni produit. |
| 2 | Facture AWS (cloud) | **6135** + autoliquidation (**445662 / 4452**) | Prestataire établi au Luxembourg, preneur assujetti en France : TVA autoliquidée par TechNova (art. 283-2 CGI). La facture n'avait pas été saisie. |
| 3 | Avance de 3 600 € versée au président | **4671** Débiteur divers – Y. Haddad | Voir § 4 : opération interdite. On ne la noie pas en charges. |
| 4 | Payout Stripe | **4672** Stripe – transit | Les ventes ont déjà été importées (4672 débité de 46 452 €) : le virement **solde** le transit avec les frais. |
| 4 bis | Frais Stripe 1 452 € | **627** / 4672 | Non comptabilisés ; services de paiement, en principe exonérés de TVA. |
| 5 | Dépôt de marque INPI | **6227** | Marque créée en interne : les dépenses de création d'une marque ne sont pas immobilisables (PCG, art. 212-3) ; redevance INPI non soumise à TVA. Certains cabinets immobilisent les frais de dépôt en 205 : position à documenter. |
| 6 | Règlement SoftDev | **401 SoftDev** | Facture déjà saisie : on lettre (18 000 = 15 000 HT + 3 000 TVA). Ne pas repasser une charge. |
| 7 | Paiement de la TVA de mars | **44551** | Déjà comptabilisée par la CA3 : on solde la dette. |
| 8 | Règlement de F-2026-0142 | **411 Logistik Plan** | Lettrage avec la facture 0142. |
| 9 | Second paiement, affecté à F-2026-0218 | **411 Logistik Plan** | Accord écrit du client : le paiement s'impute sur la facture de juillet. Entre mai et juillet, le 411 était créditeur (client créditeur, à reclasser en 4191/419 si l'arrêté tombait dans cette période). |
| 10 | Abonnement Apple personnel de Y. Haddad | **4671** Y. Haddad | Dépense personnelle : pas une charge ; créance sur le dirigeant à récupérer. |
| 11 | Remboursement de l'avance de la ligne 3 | **4671** Y. Haddad | Lettrage avec la ligne 3. |
| 12 | Cotisations URSSAF de juin | **431** | Déjà comptabilisées par la paie : lettrage. |
| 13 | Dépôt de garantie des bureaux de Gerland | **275** Dépôts et cautionnements versés | Somme récupérable en fin de bail : immobilisation financière, pas une charge. |
| 14 | Remboursement de la créance de CIR 2025 | **444** (créance CIR) | Créance comptabilisée au 31/12/2025 : on la solde. Pas de produit 2026. |
| 15 | Frais de virement international | **627** | Frais bancaires. |

## 2. Calculs

- AWS : TVA autoliquidée 1 249,00 × 20 % = **249,80 €** (collectée en 4452 et déductible en 445662 : neutre en trésorerie, mais à déclarer sur la CA3 de février — **à vérifier** : si elle n'a pas été déclarée, régulariser sur la prochaine CA3).
- Stripe : 46 452,00 – 1 452,00 = 45 000,00 ✔ → le 4672 est soldé pour cette période.
- SoftDev : 15 000,00 × 1,20 = 18 000,00 ✔.
- Compte Y. Haddad (4671) : + 3 600,00 – 3 600,00 + 89,90 = **89,90 € débiteur** au 30/09/2026.
- Contrôle du 471 : débits de soldage (encaissements) 12 000 + 45 000 + 8 400 + 8 400 + 3 600 + 86 420 = 163 820,00 ; crédits de soldage (décaissements) 1 249 + 3 600 + 270 + 18 000 + 2 400 + 89,90 + 4 830 + 1 200 + 36 = 31 674,90 ; net 132 145,10 débit → solde **0,00** ✔.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 471 | Compte d'attente | L1 — Bpifrance tranche 2 avance remboursable | 12 000,00 |  |
| 30/09/2026 | OD | 1674 | Avances conditionnées de l'État | L1 — Bpifrance AR-2025-0412 tranche 2 |  | 12 000,00 |
| 30/09/2026 | OD | 6135 | Locations mobilières (hébergement cloud) | L2 — AWS facture EUINFR26-118842 | 1 249,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L2 — AWS |  | 1 249,00 |
| 30/09/2026 | OD | 445662 | TVA déductible intracommunautaire (autoliquidation services) | L2 — AWS autoliquidation 20 % | 249,80 |  |
| 30/09/2026 | OD | 4452 | TVA due intracommunautaire | L2 — AWS autoliquidation 20 % |  | 249,80 |
| 30/09/2026 | OD | 4671 | Débiteur divers — Y. Haddad | L3 — avance versée au président | 3 600,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L3 |  | 3 600,00 |
| 30/09/2026 | OD | 471 | Compte d'attente | L4 — virement Stripe payout PO_1Q8x7Z | 45 000,00 |  |
| 30/09/2026 | OD | 4672 | Stripe — compte de transit | L4 — virement Stripe payout |  | 45 000,00 |
| 30/09/2026 | OD | 627 | Services bancaires et assimilés | L4 — commissions Stripe période payout | 1 452,00 |  |
| 30/09/2026 | OD | 4672 | Stripe — compte de transit | L4 — commissions Stripe |  | 1 452,00 |
| 30/09/2026 | OD | 6227 | Frais d'actes et de contentieux | L5 — INPI dépôt marque TechNova Plan | 270,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L5 |  | 270,00 |
| 30/09/2026 | OD | 401SOFT | Fournisseur SoftDev Consulting | L6 — règlement fact. SD-2026-031 | 18 000,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L6 |  | 18 000,00 |
| 30/09/2026 | OD | 44551 | TVA à décaisser | L7 — paiement CA3 mars 2026 | 2 400,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L7 |  | 2 400,00 |
| 30/09/2026 | OD | 471 | Compte d'attente | L8 — règlement F-2026-0142 | 8 400,00 |  |
| 30/09/2026 | OD | 411LOG | Client Logistik Plan GmbH | L8 — règlement F-2026-0142 |  | 8 400,00 |
| 30/09/2026 | OD | 471 | Compte d'attente | L9 — 2e paiement (affecté à F-2026-0218) | 8 400,00 |  |
| 30/09/2026 | OD | 411LOG | Client Logistik Plan GmbH | L9 — règlement anticipé F-2026-0218 |  | 8 400,00 |
| 30/09/2026 | OD | 4671 | Débiteur divers — Y. Haddad | L10 — abonnement Apple personnel payé par la société | 89,90 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L10 |  | 89,90 |
| 30/09/2026 | OD | 471 | Compte d'attente | L11 — remboursement avance Y. Haddad | 3 600,00 |  |
| 30/09/2026 | OD | 4671 | Débiteur divers — Y. Haddad | L11 — remboursement avance |  | 3 600,00 |
| 30/09/2026 | OD | 431 | Sécurité sociale | L12 — cotisations URSSAF juin 2026 | 4 830,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L12 |  | 4 830,00 |
| 30/09/2026 | OD | 275 | Dépôts et cautionnements versés | L13 — dépôt de garantie bureau annexe Gerland | 1 200,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L13 |  | 1 200,00 |
| 30/09/2026 | OD | 471 | Compte d'attente | L14 — remboursement CIR 2025 | 86 420,00 |  |
| 30/09/2026 | OD | 444 | État — impôts sur les bénéfices (créance CIR) | L14 — remboursement CIR 2025 |  | 86 420,00 |
| 30/09/2026 | OD | 627 | Services bancaires et assimilés | L15 — frais de virement international | 36,00 |  |
| 30/09/2026 | OD | 471 | Compte d'attente | L15 |  | 36,00 |
| | | | | **Totaux** | **197 196,70** | **197 196,70** |

> En production, on passerait plutôt chaque reclassement **à la date de l'opération bancaire** (ce qui place la TVA AWS sur la bonne période et facilite le lettrage). Le regroupement au 30/09 est acceptable pour une situation intermédiaire, à condition de régulariser la CA3 si besoin.

## 4. Points d'attention / pièges

### Lignes 3, 10 et 11 : l'avance au président
- **Juridiquement** : il est **interdit** à une SAS de consentir un prêt ou une avance à son président ou à ses dirigeants personnes physiques (art. L. 227-12 C. com., renvoyant aux interdictions de l'art. L. 225-43). Le contrat est nul. Le fait que Yanis ait remboursé quatre mois plus tard n'efface pas l'infraction ; s'y ajoute le risque d'**abus de biens sociaux** (art. L. 242-6 C. com.) — usage des fonds de la société dans un intérêt personnel.
- **Fiscalement** : les avances consenties aux associés sont présumées **revenus distribués** (art. 111 a CGI). Le remboursement permet de neutraliser l'imposition, mais l'opération reste visible. L'avance gratuite constitue en outre un avantage (absence d'intérêts) que l'administration peut relever.
- **Ligne 10** : 89,90 € de dépense personnelle → créance sur Yanis, à rembourser **avant la clôture** ; à défaut, rémunération ou avantage en nature à déclarer.
- **Pour la levée de fonds** : les investisseurs font une *due diligence* ; une avance au président découverte par eux est un sujet de confiance. Mieux vaut que le cabinet l'ait identifiée, documentée et que l'opération soit close.

### Autres pièges
- **Ne pas comptabiliser deux fois** : lignes 6, 7, 12 et 14 soldent des dettes ou créances **déjà enregistrées**. Passer la ligne 14 en produit doublerait le CIR ; passer la ligne 6 en charge doublerait la sous-traitance.
- **Avance remboursable ≠ subvention** : la confusion gonfle artificiellement le résultat de 12 000 €.
- **Dépôt de garantie** : 275, pas 613.
- **Autoliquidation** : une facture étrangère « reverse charge » trouvée dans une boîte mail est souvent oubliée sur la CA3.

## 5. Ce qu'un senior ferait en plus

**Liste des suites à donner :**
1. Obtenir le **remboursement de 89,90 €** par Yanis (virement) avant le 31/12/2026.
2. Vérifier la **CA3 de février** (autoliquidation AWS) et régulariser si nécessaire.
3. Classer la convention Bpifrance et la lettre de versement du solde au dossier permanent ; noter l'échéancier de remboursement.
4. Dossier du bureau de Gerland : obtenir le bail (dépôt de garantie, durée, loyers → engagements).
5. Supprimer la carte de la société des comptes personnels de Yanis (Apple, etc.).
6. Rédiger une **note interne** sur l'avance au président (dates, remboursement) et en parler à Hélène Ferrand avant toute communication à l'investisseur.

**Message à Émilie :**
> « Bonjour Émilie, merci pour vos réponses très complètes : le 471 est soldé au 30/09. Un 471 dans une situation, c'est une zone d'ombre pour le lecteur (un investisseur se demandera ce qui s'y cache) et, à la clôture, il ne peut figurer dans aucun poste du bilan. Je vous propose : (1) un point hebdomadaire de 15 minutes sur les lignes non affectées ; (2) des règles d'affectation automatique dans le logiciel pour Stripe, AWS, URSSAF, DGFIP ; (3) une boîte mail factures@ partagée pour que les factures n'arrivent plus chez Yanis. Concernant l'avance de février, Hélène Ferrand appellera Yanis. Belle journée. »

**Contrôle de cohérence** : après l'opération, vérifier les soldes de 4672 (doit correspondre aux ventes Stripe du 15 au 30/09 non encore virées), 1674 (40 000 €), 444 (zéro pour le CIR 2025), 411 Logistik (soldé).

## 6. Références
- PCG : comptes 471 (à solder), 1674, 275, 4672, 6135, 6227, 627, 444, 445662, 4452 ; PCG art. 212-3 (marques créées en interne non immobilisables).
- CGI, art. 283-2 (autoliquidation des prestations de services reçues d'un prestataire non établi en France) ; art. 111 a (avances aux associés) ; art. 244 quater B (CIR).
- Code de commerce, art. L. 227-12 et L. 225-43 (interdiction des prêts aux dirigeants de SAS), art. L. 242-6 (abus de biens sociaux dans les SA, applicable aux SAS par l'art. L. 244-1).
