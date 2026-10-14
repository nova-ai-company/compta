# Corrigé E05-04 — Crédit-bail d'un tracteur routier : écritures, annexe et levée d'option

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-04](../exercices/E05-04_credit-bail-tracteur-leroy.md)

## 1. Analyse

### Pourquoi le tracteur n'est pas à l'actif
En comptes sociaux français, l'inscription à l'actif suit la **propriété juridique** pour les contrats de crédit-bail : tant que l'option d'achat n'est pas levée, le tracteur appartient à **Rhône Lease**. Transports Leroy a un **droit d'usage** contre paiement de loyers : ce sont des **charges** (6122), pas une immobilisation. (En comptes consolidés ou en IFRS 16, le contrat serait retraité : actif « droit d'utilisation » + dette ; ce n'est pas le cas ici.)

### Ce que dit le banquier
Il a raison sur le fond économique : les 51 loyers restant dus au 31/12/2026 (106 335,00 € HT) sont un **engagement ferme** de l'entreprise, comparable à une dette. C'est pourquoi le PCG impose de le donner **en annexe** (engagements de crédit-bail), et pourquoi les banquiers et analystes retraitent le crédit-bail en dette financière.

### Le premier loyer majoré
Le loyer n° 1 (19 200 €) est près de dix fois le loyer courant (2 085 €). Il ne rémunère pas l'usage du seul mois d'avril : il **finance une partie du bien** pour toute la durée du contrat. Le passer intégralement en charge en 2026 contreviendrait au principe d'indépendance des exercices. Méthode retenue au cabinet : **linéariser** le coût total des redevances sur la durée du contrat et constater en **charges constatées d'avance (486)** la fraction payée d'avance.

### La saisie en 238
Le compte 238 enregistre des acomptes versés en vue d'**acquérir** une immobilisation. Rien n'est acquis ici : le loyer n° 1 est une redevance → 6122 (puis lissage à l'inventaire). Les frais de dossier d'un financement relèvent des **services bancaires et assimilés (627)**, pas des honoraires.

## 2. Calculs

### 2.1 Coût total et lissage

| Élément | Montant HT |
|---|---|
| Loyer n° 1 majoré | 19 200,00 |
| 59 loyers × 2 085,00 | 123 015,00 |
| **Total des redevances** | **142 215,00** |
| Charge mensuelle lissée (/ 60) | **2 370,25** |

(Le prix de levée d'option, 1 280 €, n'est pas une redevance : c'est le prix d'achat du bien au terme.)

### 2.2 Exercice 2026 (01/04 → 31/12 : 9 mois)

| | Montant |
|---|---|
| Redevances facturées en 2026 : loyer n° 1 + loyers n° 2 à 9 (8 × 2 085,00) | 35 880,00 |
| Charge de l'exercice lissée : 9 × 2 370,25 | 21 332,25 |
| **Charges constatées d'avance au 31/12/2026** | **14 547,75** |

Situation intermédiaire au 30/09/2026 (6 mois), pour information : redevances facturées 19 200 + 5 × 2 085 = 29 625,00 ; charge lissée 6 × 2 370,25 = 14 221,50 ; CCA = **15 403,50 €**.

Évolution ensuite : en 2027, charge 28 443,00 (12 × 2 370,25) pour 25 020,00 facturés → la CCA diminue de 3 423,00 par an (11 124,75 fin 2027…) et s'annule le 31/03/2031.

### 2.3 Informations pour l'annexe au 31/12/2026
- Amortissement « fictif » (si le bien avait été acquis) : 128 000 / 5 ans = 25 600 €/an ; 2026 : 25 600 × 270 / 360 = **19 200,00 €** (01/04 → 31/12 = 9 mois de 30 jours).
- Redevances restant à payer : loyers n° 10 à 60 = 51 loyers.
  - à 1 an au plus : loyers n° 10 à 21 (2027) = 12 × 2 085 = **25 020,00** ;
  - de 1 à 5 ans : loyers n° 22 à 60 (01/2028 → 03/2031) = 39 × 2 085 = **81 315,00** ;
  - à plus de 5 ans : **0**.

## 3. Écritures comptables

**Correction de la saisie du loyer n° 1 (OD au 30/09/2026) :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6122 | Redevances de crédit-bail mobilier | Reclassement loyer n° 1 CB-26-4471 saisi en 238 | 19 200,00 |  |
| 30/09/2026 | OD | 238 | Avances et acomptes versés sur commandes d'immobilisations corporelles | Reclassement loyer n° 1 CB-26-4471 |  | 19 200,00 |
| 30/09/2026 | OD | 627 | Services bancaires et assimilés | Reclassement frais de dossier CB-26-4471 | 350,00 |  |
| 30/09/2026 | OD | 6226 | Honoraires | Reclassement frais de dossier CB-26-4471 |  | 350,00 |
| | | | | **Totaux** | **19 550,00** | **19 550,00** |

Pour mémoire, la saisie correcte d'origine (01/04/2026) aurait été : 6122 19 200,00 + 627 350,00 + 44566 3 910,00 / 401 Rhône Lease 23 460,00. Saisie d'un loyer courant (n° 2 à 60) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/05/2026 | AC | 6122 | Redevances de crédit-bail mobilier | Loyer n° 2 CB-26-4471 | 2 085,00 |  |
| 01/05/2026 | AC | 44566 | TVA déductible sur autres biens et services | Loyer n° 2 | 417,00 |  |
| 01/05/2026 | AC | 401LOC | Fournisseur Rhône Lease | Loyer n° 2 |  | 2 502,00 |
| | | | | **Totaux** | **2 502,00** | **2 502,00** |

**Inventaire au 31/12/2026 et extourne :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 486 | Charges constatées d'avance | Lissage redevances CB-26-4471 (premier loyer majoré) | 14 547,75 |  |
| 31/12/2026 | OD | 6122 | Redevances de crédit-bail mobilier | Lissage redevances CB-26-4471 |  | 14 547,75 |
| | | | | **Totaux** | **14 547,75** | **14 547,75** |

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/01/2027 | OD | 6122 | Redevances de crédit-bail mobilier | Extourne CCA au 31/12/2026 | 14 547,75 |  |
| 01/01/2027 | OD | 486 | Charges constatées d'avance | Extourne CCA au 31/12/2026 |  | 14 547,75 |
| | | | | **Totaux** | **14 547,75** | **14 547,75** |

(Au 31/12/2027, nouvelle CCA de 11 124,75 €, et ainsi de suite.)

Charge 6122 de l'exercice 2026 : 35 880,00 – 14 547,75 = **21 332,25 €** ✔.

**Levée d'option et amortissement (2031) :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/04/2031 | AC | 2182 | Matériel de transport | Levée d'option tracteur CB-26-4471 | 1 280,00 |  |
| 01/04/2031 | AC | 44562 | TVA déductible sur immobilisations | Levée d'option | 256,00 |  |
| 01/04/2031 | AC | 404LOC | Fournisseur d'immobilisations Rhône Lease | Levée d'option |  | 1 536,00 |
| | | | | **Totaux** | **1 536,00** | **1 536,00** |

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2031 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Amort. tracteur ex-CB (1 280 / 3 ans × 270/360) | 320,00 |  |
| 31/12/2031 | OD | 28182 | Amortissements du matériel de transport | Amort. tracteur ex-CB |  | 320,00 |
| | | | | **Totaux** | **320,00** | **320,00** |

Le tracteur entre à l'actif pour son **prix de levée** (1 280 €) et s'amortit sur la **durée d'utilisation résiduelle** (3 ans) : 426,67 €/an, soit 320,00 € en 2031 (9 mois).

### Note d'annexe au 31/12/2026 — Engagements de crédit-bail

| Poste | Valeur d'origine | Dotations théoriques de l'exercice | Dotations théoriques cumulées | VNC théorique | Redevances payées — exercice | Redevances payées — cumul | Restant à payer ≤ 1 an | Restant à payer 1 à 5 ans | Restant à payer > 5 ans | Prix d'achat résiduel |
|---|---|---|---|---|---|---|---|---|---|---|
| Matériel de transport (tracteur Volvo FH, contrat CB-26-4471) | 128 000,00 | 19 200,00 | 19 200,00 | 108 800,00 | 35 880,00 | 35 880,00 | 25 020,00 | 81 315,00 | 0,00 | 1 280,00 |

(Montants HT. Le niveau de détail exigé dépend de la taille de la société — annexe abrégée possible pour une petite entreprise ; ce tableau complet est celui que demandera le banquier.)

## 4. Points d'attention / pièges

- **Pas d'actif, pas d'amortissement, pas d'emprunt** en comptes sociaux. Ne jamais « immobiliser » un bien en crédit-bail, même si le client l'assure et l'entretient.
- **238 ≠ premier loyer** : un acompte sur immobilisation suppose une acquisition future par l'entreprise elle-même.
- **Premier loyer majoré** : à lisser. Le passer en charge immédiate surestime les charges de 2026 de 14 547,75 €.
- **Fiscalement**, la déduction immédiate du premier loyer majoré est risquée : l'administration et la jurisprudence considèrent en général qu'un loyer majoré qui rémunère l'usage sur toute la durée du contrat doit être **réparti** sur cette durée. Le traitement fiscal suit ici le traitement comptable (pas de retraitement) — position à documenter dans le dossier.
- **Tracteur routier ≠ véhicule de tourisme** : aucune réintégration de quote-part de loyers au titre de l'art. 39-4 CGI (qui ne vise que les véhicules de tourisme).
- **TVA** : la location financière est une prestation de services, TVA déductible sur les loyers (44566) ; la levée d'option est une livraison de bien d'investissement (44562).
- **Levée d'option** : ne pas oublier d'**ajouter le bien au fichier des immobilisations** avec sa durée résiduelle, et de **retirer** le contrat de la note d'engagements.

## 5. Ce qu'un senior ferait en plus

**Réponse écrite à M. Leroy :**
> « Bonjour Monsieur Leroy,
> Juridiquement, le tracteur appartient à Rhône Lease jusqu'à la levée de l'option en avril 2031 : dans vos comptes sociaux, il n'apparaît donc pas à l'actif, et vos loyers sont des charges. En revanche, nous indiquons en annexe la valeur du tracteur et les loyers restant dus (106 335 € HT au 31/12/2026) : c'est ce que votre banquier lit comme une dette, à juste titre.
> Pour le premier loyer de 19 200 € : il paie en réalité une partie du camion sur 5 ans. Nous le répartissons donc sur la durée du contrat ; seuls 21 332 € de loyers seront en charge en 2026. Le passer en totalité cette année ferait gagner de l'IS en apparence, mais l'administration le remettrait en cause en cas de contrôle, avec intérêts de retard.
> Bien cordialement. »

**Contrôles et dossier :**
- Créer un **échéancier des contrats de crédit-bail et LLD** (16 tracteurs !) dans le dossier permanent : n° de contrat, bien, durée, loyers, option, fin de contrat — base de la note d'annexe chaque année et du prévisionnel de trésorerie.
- Vérifier chaque mois que le nombre de loyers comptabilisés en 6122 correspond au nombre de contrats actifs (oubli fréquent d'une facture de loyer).
- Comparer avec un achat financé par emprunt pour les prochains renouvellements (coût total, effet sur le bilan et les ratios, TVA, souplesse) : c'est un vrai conseil à valeur ajoutée pour un transporteur.

## 6. Références
- PCG : comptes 6122, 486, 238, 627, 2182, 28182 ; information sur les engagements de crédit-bail dans l'annexe (règles relatives à l'annexe, art. 833-… du PCG — consulter la rubrique applicable selon la taille de l'entité).
- Code monétaire et financier, art. L. 313-7 (définition du crédit-bail).
- CGI, art. 39-1 (déductibilité des loyers), art. 39-4 (véhicules de tourisme, non applicable ici) ; art. 39 duodecies, 10 (plus-value en cas de cession d'un bien acquis par levée d'option) — à anticiper si le tracteur est revendu rapidement après 2031.
