# Corrigé E13-12 — TechNova : une licence payée en ether par un client américain

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E13-12](../exercices/E13-12_technova-cryptoactifs-recus-en-paiement.md)

> **Avertissement de méthode.** Les jetons sont une matière récente, dont les textes comptables, fiscaux et réglementaires (MiCA) évoluent. Ce corrigé distingue :
> - ✅ **établi** : ce qui découle des principes généraux et ne fait pas débat ;
> - 🔎 **à vérifier** : numéros de comptes de la nomenclature, rédaction exacte des textes fiscaux, statut du prestataire.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Question 1 — Le chiffre d'affaires.** ✅ La vente est une **prestation de services** (licence SaaS) facturée **en euros** : le chiffre d'affaires est de **18 000 €**, comme pour n'importe quel client. Le paiement en ether est une **modalité de règlement**, comparable à un paiement en devise : il n'affecte ni le montant du produit ni sa nature.
- La licence couvre la période du 01/09/2026 au 31/08/2027 : au 31/12/2026, 8 mois sur 12 se rapportent à 2027 → **produit constaté d'avance** de 12 000 € (c'est le corner case récurrent de TechNova).
- ✅ **TVA** : prestation de services à un preneur assujetti établi hors UE → **hors champ** de la TVA française (CGI art. 259-1°) ; la mention de la facture est correcte. Le mode de paiement ne change rien.
- Ici le client a envoyé une quantité d'ETH égale exactement à 18 000 € au cours du jour : pas d'écart de règlement. (S'il y en avait eu un, il se traiterait par analogie avec un écart de change sur règlement — 🔎 comptes à confirmer.)

**Question 2 — Classement des ETH.** Le règlement ANC n° 2018-07 (intégré au PCG) distingue, chez le **détenteur** de jetons qu'il n'a pas émis :
- les jetons détenus **durablement** pour l'usage des services qu'ils donnent (droits d'usage) → immobilisations incorporelles ;
- les **autres jetons détenus**, notamment à titre de placement ou de moyen de paiement → **actif circulant**, compte **522 « Jetons détenus »** (🔎 numéro à confirmer dans le plan de comptes du logiciel).
TechNova a reçu l'ether en règlement et compte le convertir en euros : actif circulant, 522. Entrée pour sa **valeur à la date de réception** : 18 000 €.

**Question 3 — Cession.** ✅ La différence entre le prix de cession (9 450 €) et la valeur d'entrée des jetons cédés (3 × 3 000 = 9 000 €) est un **résultat de cession** : + 450 €. Les frais de la plateforme (47,25 €) sont une charge de services bancaires et assimilés. 🔎 Présentation : le règlement 2018-07 prévoit des comptes de produits et charges dédiés aux cessions de jetons ; à défaut de certitude sur la subdivision, on utilise un sous-compte de **767 / 667** (produits / charges nets sur cessions de valeurs mobilières de placement, par analogie) — *subdivision selon la nomenclature 2025 du PCG*.
✅ **TVA** : l'échange de cryptoactifs contre des euros est une opération sur moyen de paiement **exonérée** (CJUE, 22/10/2015, *Hedqvist*, aff. C-264/14). Opération financière **accessoire** pour TechNova → elle ne devrait pas affecter son droit à déduction (exclusion des opérations financières accessoires du calcul du coefficient de taxation — 🔎 à vérifier si les opérations se multipliaient).

**Question 4 — Évaluation à la clôture.** Selon le règlement 2018-07, les jetons détenus inscrits en actif circulant sont évalués à la clôture à leur **valeur actuelle** (cours sur un marché actif à la date de clôture). L'approche retenue ici, **prudente** et cohérente avec la logique des écarts de conversion :
- la différence entre la valeur actuelle et la valeur d'entrée est inscrite au bilan dans un compte de **différences d'évaluation** (actif si moins-value, passif si plus-value) ;
- la **moins-value latente** est couverte par une **provision pour risques** (charge financière) ;
- la **plus-value latente** n'est **pas** comptabilisée en résultat.
🔎 Mécanique et numéros de comptes (474x « Différences d'évaluation de jetons », provision) à confirmer dans le texte du règlement et la nomenclature du logiciel avant passation ; **la conclusion (moins-value constatée en charge, plus-value non constatée) est, elle, conforme au principe de prudence.**

Au cours hypothétique de 2 700 € : 3 ETH valent 8 100 € pour une valeur d'entrée de 9 000 € → moins-value latente de **900 €** → différence d'évaluation actif 900 € et provision 900 €.
Si le cours était de **3 300 €** : plus-value latente de 900 € → D 522 / C différence d'évaluation passif (474x) 900 € ; **aucun produit** en résultat comptable.

**Question 5 — IS.** 🔎 La loi de finances pour 2019 a introduit une règle propre aux jetons détenus par les entreprises soumises à l'IS (codifiée à l'article 38 du CGI) : à la clôture, les jetons non immobilisés sont évalués à leur **valeur à cette date** et l'**écart d'évaluation** est compris dans le **résultat imposable**. Conséquences pratiques, à vérifier dans la rédaction en vigueur et au BOFiP :
- en cas de **moins-value latente** : la perte de 900 € est déductible ; avec la mécanique comptable ci-dessus, on réintègre la **provision** (900) et on déduit la **différence d'évaluation actif** (900) → effet net nul par rapport au résultat comptable, mais deux lignes au tableau 2058-A ;
- en cas de **plus-value latente** : elle serait **imposable** alors qu'elle n'est pas comptabilisée → **réintégration extra-comptable** de 900 €.
✅ Le résultat de cession (+ 450 €) et les frais (− 47,25 €) suivent le résultat comptable. Le produit de 18 000 € (6 000 € en 2026 après PCA) est imposé normalement.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Valeur d'entrée des 6 ETH | 6 × 3 000,00 | 18 000,00 € |
| CA 2026 | 18 000,00 × 4/12 | 6 000,00 € |
| PCA au 31/12/2026 | 18 000,00 × 8/12 | 12 000,00 € |
| Prix de cession brut (3 ETH) | 3 × 3 150,00 | 9 450,00 € |
| Valeur d'entrée des 3 ETH cédés | 3 × 3 000,00 | 9 000,00 € |
| Résultat de cession | 9 450,00 − 9 000,00 | + 450,00 € |
| Frais de transaction | 9 450,00 × 0,50 % | 47,25 € |
| Net viré en banque | 9 450,00 − 47,25 | 9 402,75 € |
| Valeur actuelle des 3 ETH au 31/12 | 3 × 2 700,00 | 8 100,00 € |
| Moins-value latente | 9 000,00 − 8 100,00 | **900,00 €** |
| (Variante : cours 3 300 €) | 3 × 3 300,00 − 9 000,00 | plus-value latente 900,00 € |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 28/08/2026 | VT | 411BRIG | Client Brightline Logistics | F TN-2026-0918 licence 09/2026-08/2027 | 18 000,00 | |
| 28/08/2026 | VT | 706 | Prestations de services – licences SaaS | F TN-2026-0918 – hors champ art. 259-1° | | 18 000,00 |
| 04/09/2026 | OD | 522 | Jetons détenus (ETH) | Règlement Brightline 6 ETH au cours de 3 000 € | 18 000,00 | |
| 04/09/2026 | OD | 411BRIG | Client Brightline Logistics | Règlement Brightline 6 ETH | | 18 000,00 |
| 20/10/2026 | BQ | 512 | Banque | Cession 3 ETH à 3 150 € – net viré | 9 402,75 | |
| 20/10/2026 | BQ | 627 | Services bancaires et assimilés | Frais de transaction EuroCrypto 0,50 % | 47,25 | |
| 20/10/2026 | BQ | 522 | Jetons détenus (ETH) | Sortie 3 ETH à la valeur d'entrée | | 9 000,00 |
| 20/10/2026 | BQ | 767 | Produits nets sur cessions (jetons) | Résultat de cession 3 ETH | | 450,00 |
| 31/12/2026 | OD | 706 | Prestations de services – licences SaaS | PCA licence Brightline (8/12) | 12 000,00 | |
| 31/12/2026 | OD | 487 | Produits constatés d'avance | PCA licence Brightline (8/12) | | 12 000,00 |
| 31/12/2026 | OD | 474A | Différences d'évaluation de jetons – actif | 3 ETH : valeur actuelle 8 100 < 9 000 | 900,00 | |
| 31/12/2026 | OD | 522 | Jetons détenus (ETH) | 3 ETH : valeur actuelle 8 100 < 9 000 | | 900,00 |
| 31/12/2026 | OD | 6865 | Dotations aux provisions pour risques et charges financiers | Moins-value latente sur jetons | 900,00 | |
| 31/12/2026 | OD | 151J | Provision pour pertes sur jetons | Moins-value latente sur jetons | | 900,00 |
| | | | | **Totaux** | **59 250,00** | **59 250,00** |

*🔎 Comptes 522, 474A, 151J et 767 (sous-compte « jetons ») : subdivisions selon la nomenclature 2025 du PCG et le règlement ANC 2018-07, à confirmer avant passation. Les écritures de différence d'évaluation sont extournées à l'ouverture de l'exercice suivant (comme les écarts de conversion), la provision étant reprise ou ajustée à chaque clôture.*

**Annexe** : méthode comptable des jetons (classement, source du cours retenu, heure de référence), quantité détenue, valeur d'entrée, valeur actuelle, différences d'évaluation, provision, et — compte tenu de la volatilité — information sur l'évolution du cours après la clôture si elle est significative.

## 4. Points d'attention / pièges

- **Ne pas réévaluer le chiffre d'affaires** au gré du cours de l'ETH : le produit est figé à 18 000 € (date de l'opération) ; les variations ultérieures concernent l'actif « jetons ».
- **Ne pas oublier le PCA** : le mode de paiement exotique fait oublier la règle de base des abonnements annuels.
- **Plus-value latente** : jamais en produit comptable, mais potentiellement imposable (🔎) → retraitement extra-comptable.
- **Source du cours** : choisir une source unique, fiable (plateforme de référence ou indice), et une heure de référence, et s'y tenir (permanence des méthodes).
- **Stablecoins** : si le client avait payé en jeton adossé à une monnaie officielle, la qualification (jeton de monnaie électronique au sens de MiCA, donc monnaie électronique ?) serait à analyser : le traitement pourrait se rapprocher de la trésorerie / des devises.
- **Frais** : à comptabiliser séparément (pas de « net » qui masque le résultat de cession).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — Justificatifs et vigilance :**
1. Relevés de la plateforme (réception, cession, solde au 31/12) **signés ou exportés** avec horodatage, et attestation de solde au 31/12 ; capture de l'explorateur de blockchain pour la transaction d'entrée (hash) ; cours de référence au 31/12 (source et heure).
2. **Contrat** autorisant le paiement en ETH et désignant l'adresse du portefeuille du client : rapprochement adresse émettrice / adresse contractuelle.
3. **LCB-FT** : identité du payeur = client (KYC), cohérence du montant ; la plateforme applique les règles de traçabilité des transferts de cryptoactifs (règlement européen sur les informations accompagnant les transferts) ; le cabinet, assujetti à la LCB-FT, documente son analyse de l'opération (pas de soupçon ici : client identifié, contrat, montant cohérent).
4. **Statut du prestataire** : 🔎 vérifier qu'EuroCrypto Exchange est **agréé comme prestataire de services sur cryptoactifs (CASP) au titre de MiCA** — l'enregistrement PSAN ne suffit plus après la fin de la période transitoire française (🔎 date à vérifier). Sinon, risque de blocage des fonds : transférer vers un prestataire agréé.
5. **Politique de trésorerie** : décision écrite du président (montant maximal détenu, délai de conversion, signataires) ; conversion rapide recommandée — TechNova n'a pas vocation à spéculer.
6. **Contrôle interne** : accès au compte de la plateforme (double authentification, deux personnes), conservation des clés si portefeuille auto-hébergé (à éviter).

**Question 7 — Réponse à Émilie :**

> Bonjour Émilie,
>
> **Ce qui est certain** : le chiffre d'affaires est de 18 000 € (facture en euros), dont 12 000 € seront reportés sur 2027 (licence jusqu'en août 2027) ; pas de TVA (client hors UE). Les 6 ETH entrent au bilan pour 18 000 € dans un compte de « jetons détenus ». La revente de 3 ETH dégagera un gain d'environ 450 € (avant 47 € de frais), sans TVA.
>
> **Ce que nous validons encore** : la mécanique exacte d'évaluation au 31/12 et son traitement fiscal. À titre d'exemple, si l'ETH valait 2 700 € au 31/12, nous constaterions une provision de 900 € ; s'il valait 3 300 €, aucun gain ne serait comptabilisé, mais il pourrait être imposable.
>
> **Ce dont nous avons besoin** : les relevés de la plateforme (réception, vente, solde au 31/12), le contrat avec Brightline, et la confirmation qu'EuroCrypto Exchange dispose bien de l'agrément européen MiCA. Je vous suggère aussi une décision écrite de Yanis sur la conversion des cryptos reçues (par exemple sous 48 h).

**Documentation** : note technique datée (sources consultées, points 🔎 et leur résolution), validée par Hélène ; pièces listées ci-dessus ; tableau de suivi des jetons (quantité, valeur d'entrée, cessions, valeur actuelle).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Règlement ANC n° 2018-07 relatif à la comptabilisation des jetons (intégré au PCG) : détenteurs de jetons, classement, évaluation à la clôture, informations en annexe.
- PCG : produits constatés d'avance, écarts de conversion (analogie), provisions pour risques.
- CGI art. 259-1° (lieu des prestations de services B2B) ; art. 261 C (exonération des opérations portant sur les moyens de paiement) ; CJUE 22/10/2015, *Hedqvist*, aff. C-264/14.
- CGI art. 38 (régime des jetons détenus par les entreprises — disposition issue de la loi de finances pour 2019, rédaction en vigueur à vérifier) ; BOFiP correspondant.
- Règlement (UE) 2023/1114 (MiCA) ; règlement (UE) 2023/1113 (informations accompagnant les transferts de fonds et de cryptoactifs) ; Code monétaire et financier (PSAN, LCB-FT).
