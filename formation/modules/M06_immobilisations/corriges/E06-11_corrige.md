# Corrigé E06-11 — Balayage des comptes 6063 / 615 et fichier des immobilisations qui ne colle pas

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-11](../exercices/E06-11_requalification-fichier-immos-atelier-ligne.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — La grille de requalification (question 1).** Pour chaque facture : (a) est-ce un **bien durable** contrôlé, ou un **service** / une **remise en état** ? (b) si c'est un bien, sa **valeur unitaire** dépasse-t-elle 500 € HT ? (c) fait-il partie d'un **ensemble** ?

| N° | Objet | Décision | Compte | Durée | Justification |
|---|---|---|---|---|---|
| 1 | Station CAO 2 850 | **Immobilisation** | 2183 | 3 ans | Bien durable > 500 € HT |
| 2 | Écran 420 | Charge (maintenue) | 6063 | — | Valeur unitaire < 500 € HT : tolérance ; facture distincte, bien autonome |
| 3 | Licence perpétuelle ArchiPlan 4 200 | **Immobilisation incorporelle** | 205 | 3 ans | Logiciel **acquis**, droit d'usage illimité dans le temps et contrôlé |
| 4 | Abonnement BIM 3 600 | Charge **étalée** | 651 (reclass.) + 486 | — | **SaaS** : service, pas de contrôle du logiciel ; période à cheval → CCA 9/12 |
| 5 | Tête d'impression traceur 680 | Charge (maintenue) | 615 | — | Réparation : remet en état, ne prolonge pas significativement la durée |
| 6 | Climatisation gainable 6 900 | **Immobilisation** | 2181 | 10 ans | Agencement nouveau dans un local loué ; durée ≤ bail (12 ans jusqu'au 30/09/2036) |
| 7 | Peinture des bureaux 3 200 | Charge (maintenue) | 615 | — | Entretien |
| 8 | 6 chaises à 380 | Charge (maintenue) | 6063 | — | Unités < 500 € HT, remplacement ponctuel (pas un renouvellement complet du mobilier) |
| 9 | Imprimante 3D 1 450 | **Immobilisation** | 2183 | 3 ans | Bien durable > 500 € HT |
| 10 | Maintenance copieur 960 | Charge **étalée** | 615 + 486 | — | Service sur 12 mois → CCA 11/12 |
| 11 | 3 smartphones à 520 | **Immobilisation** | 2183 | 3 ans | Chaque unité > 500 € HT (le seuil est par bien) |
| 12 | MacBook Pro 1 990 | **Immobilisation** | 2183 | 3 ans | Bien durable payé par la société et utilisé par elle ; **anomalie** de facture |

**Anomalie — facture n° 12** : établie au nom de Mme Fabre, elle ne permet pas à la SARL de **déduire la TVA** (le droit à déduction suppose une facture au nom de l'assujetti). Elle fragilise aussi la preuve de propriété. Action : demander à l'Apple Store une **facture rectificative au nom d'Atelier Ligne SARL** (SIREN 839 222 017) ; en attendant, la TVA de 398 € est sortie du 44566 et isolée en compte d'attente (471). Si la facture rectificative n'était pas obtenue, la TVA deviendrait un élément du coût (et l'on s'interrogerait sur un usage privé du bien).

Remarque CA3 : les biens immobilisés relèvent de la ligne « TVA sur immobilisations » (44562) ; le reclassement n'a pas d'incidence sur le montant déductible, mais il rend la déclaration exacte.

**Étape 2 — Le rapprochement (question 4).** On compare fichier (pièce 2) et balance (pièce 3) **compte par compte** :

| Compte | Fichier | Balance | Écart (balance – fichier) | Explication | Correction |
|---|---:|---:|---:|---|---|
| 205 / 2805 | 12 400 / 9 300 | 12 400 / 9 300 | 0 / 0 | — | — |
| 2181 / 28181 | 38 000 / 22 800 | 38 000 / 22 800 | 0 / 0 | — | — |
| 2183 brut | 41 650,00 | 44 150,00 | **+ 2 500,00** | Portable Dell (15/03/2026) comptabilisé mais **absent du fichier** | **Fichier** : créer la fiche ; **comptabilité** : passer la dotation manquante (le fichier ne l'a pas calculée) |
| 28183 | 27 940,00 | 29 790,00 | **+ 1 850,00** | Dotation estimée de la situation au 31/03 **jamais contre-passée** → doublon avec la dotation du fichier | **Comptabilité** : contre-passer 1 850 € |
| 2184 brut | 18 200,00 | 15 950,00 | **– 2 250,00** | Table de réunion donnée en janvier : sortie passée en comptabilité, **pas dans le fichier** | **Fichier** : saisir la sortie |
| 28184 | 11 060,00 | 8 810,00 | **– 2 250,00** | Idem (amortissements de la table) | **Fichier** |

Principe : on corrige **là où est l'erreur**. La balance a raison pour le portable et la table (pièces comptables existantes) → c'est le fichier qu'on corrige ; la balance a tort pour la dotation estimée → écriture comptable.

## 2. Calculs (détaillés, chaque montant justifié)

**Dotations de l'exercice (prorata au jour, 360 jours)**

| Bien | Coût | Durée | Jours (date → 30/09/2026) | Calcul | Dotation |
|---|---:|---:|---|---|---:|
| 1 Station CAO | 2 850,00 | 3 ans | 12/11 : 19 j + 10 mois = 319 | 2 850 / 3 × 319/360 | 841,81 |
| 3 Licence ArchiPlan | 4 200,00 | 3 ans | 05/01 : 26 j + 8 mois = 266 | 4 200 / 3 × 266/360 | 1 034,44 |
| 6 Climatisation | 6 900,00 | 10 ans | 20/04 : 11 j + 5 mois = 161 | 6 900 / 10 × 161/360 | 308,58 |
| 9 Imprimante 3D | 1 450,00 | 3 ans | 03/06 : 28 j + 3 mois = 118 | 1 450 / 3 × 118/360 | 158,43 |
| 11 Smartphones | 1 560,00 | 3 ans | 02/09 : 29 j | 1 560 / 3 × 29/360 | 41,89 |
| 12 MacBook Pro | 1 990,00 | 3 ans | 22/07 : 9 j + 2 mois = 69 | 1 990 / 3 × 69/360 | 127,14 |
| **Sous-total requalifiés** | **18 950,00** | | | | **2 512,29** |
| Portable Dell (écart fichier) | 2 500,00 | 3 ans | 15/03 : 16 j + 6 mois = 196 | 2 500 / 3 × 196/360 | 453,70 |
| **Total dotations complémentaires** | | | | | **2 965,99** |

Répartition : 2805 = 1 034,44 ; 28181 = 308,58 ; 28183 = 841,81 + 158,43 + 41,89 + 127,14 + 453,70 = **1 622,97**.

**Charges constatées d'avance**
- Abonnement BIM : 3 600 × 9/12 = **2 700,00** (01/10/2026 → 30/06/2027).
- Maintenance copieur : 960 × 11/12 = **880,00** (01/10/2026 → 31/08/2027).
- Total : **3 580,00**.

**Reclassements**
- Vers immobilisations : 2183 = 2 850 + 1 450 + 1 560 + 1 990 = **7 850,00** ; 205 = **4 200,00** ; 2181 = **6 900,00** ; total **18 950,00** (dont 12 050,00 sortis du 6063 et 6 900,00 du 615).
- TVA : 18 950 × 20 % = 3 790,00 à sortir du 44566, dont 3 392,00 vers 44562 et 398,00 (MacBook) vers 471.

**Question 3 — Option fiscale pour la licence ArchiPlan** : les logiciels **acquis** peuvent faire l'objet d'un **amortissement exceptionnel sur 12 mois** (CGI, art. 236-II). Sur l'exercice : 4 200 × 266/360 = 3 103,33 € déductibles, contre 1 034,44 € d'amortissement comptable → **amortissement dérogatoire de 2 068,89 €** (D 6872 / C 145), puis le solde (1 096,67 €) l'exercice suivant, avec reprises ultérieures. Gain : un décalage d'IS de l'ordre de 2 068,89 × 15 % ≈ 310 € (taux réduit, à confirmer selon le résultat). À proposer aux gérants : faible enjeu, mais gratuit — décision à prendre avant l'arrêté des comptes, l'option n'étant valable que si elle est comptabilisée.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 2183 | Matériel de bureau et informatique | Requalif. fact. 1, 9, 11, 12 | 7 850,00 | |
| 30/09/2026 | OD | 205 | Concessions, logiciels, licences | Requalif. fact. 3 licence ArchiPlan | 4 200,00 | |
| 30/09/2026 | OD | 2181 | Installations générales, agencements divers | Requalif. fact. 6 climatisation | 6 900,00 | |
| 30/09/2026 | OD | 6063 | Fournitures d'entretien et de petit équipement | Requalif. fact. 1, 3, 9, 11, 12 | | 12 050,00 |
| 30/09/2026 | OD | 615 | Entretien et réparations | Requalif. fact. 6 | | 6 900,00 |
| 30/09/2026 | OD | 44562 | TVA sur immobilisations | Reclass. TVA immobilisations (hors fact. 12) | 3 392,00 | |
| 30/09/2026 | OD | 471 | Compte d'attente – TVA MacBook (facture au nom de C. Fabre) | Dans l'attente de la facture rectificative | 398,00 | |
| 30/09/2026 | OD | 44566 | TVA sur autres biens et services | Reclass. TVA requalifiée | | 3 790,00 |
| 30/09/2026 | OD | 651 | Redevances pour logiciels (abonnements) | Reclass. abonnement BIM | 3 600,00 | |
| 30/09/2026 | OD | 6063 | Fournitures d'entretien et de petit équipement | Reclass. abonnement BIM | | 3 600,00 |
| 30/09/2026 | OD | 486 | Charges constatées d'avance | BIM 9/12 + maintenance copieur 11/12 | 3 580,00 | |
| 30/09/2026 | OD | 651 | Redevances pour logiciels (abonnements) | CCA BIM 9/12 | | 2 700,00 |
| 30/09/2026 | OD | 615 | Entretien et réparations | CCA maintenance copieur 11/12 | | 880,00 |
| 30/09/2026 | OD | 28183 | Amortissements du matériel informatique | Contre-passation dotation estimée situation 31/03 | 1 850,00 | |
| 30/09/2026 | OD | 6811 | Dotations aux amortissements des immobilisations | Contre-passation dotation estimée | | 1 850,00 |
| 30/09/2026 | OD | 6811 | Dotations aux amortissements des immobilisations | Biens requalifiés + portable Dell | 2 965,99 | |
| 30/09/2026 | OD | 2805 | Amortissements des logiciels | Licence ArchiPlan | | 1 034,44 |
| 30/09/2026 | OD | 28181 | Amortissements des agencements | Climatisation | | 308,58 |
| 30/09/2026 | OD | 28183 | Amortissements du matériel informatique | Station, imprimante 3D, smartphones, MacBook, Dell | | 1 622,97 |
| | | | | **Totaux** | **34 735,99** | **34 735,99** |

**Dans le fichier des immobilisations** (pas d'écriture) : créer les 7 fiches (6 biens requalifiés + portable Dell) avec leurs dates de mise en service ; saisir la sortie de la table de réunion (janvier 2026, VNC nulle).

## 4. Points d'attention / pièges

**Question 6 — Rapprochement après corrections**

| Compte | Fichier corrigé | Balance corrigée | Écart |
|---|---:|---:|---:|
| 205 | 12 400 + 4 200 = 16 600,00 | 16 600,00 | 0 |
| 2805 | 9 300 + 1 034,44 = 10 334,44 | 10 334,44 | 0 |
| 2181 | 38 000 + 6 900 = 44 900,00 | 44 900,00 | 0 |
| 28181 | 22 800 + 308,58 = 23 108,58 | 23 108,58 | 0 |
| 2183 | 41 650 + 2 500 + 7 850 = 52 000,00 | 44 150 + 7 850 = 52 000,00 | 0 |
| 28183 | 27 940 + 1 622,97 = 29 562,97 | 29 790 – 1 850 + 1 622,97 = 29 562,97 | 0 |
| 2184 | 18 200 – 2 250 = 15 950,00 | 15 950,00 | 0 |
| 28184 | 11 060 – 2 250 = 8 810,00 | 8 810,00 | 0 |

**Impact sur le résultat de l'exercice** : + 18 950,00 (requalifications) + 3 580,00 (CCA) + 1 850,00 (contre-passation) – 2 965,99 (dotations) = **+ 21 414,01 €**.

**Pièges**
- Le seuil de 500 € s'apprécie **par unité** : 3 smartphones à 520 € = 3 immobilisations, 6 chaises à 380 € = 6 charges.
- **Licence perpétuelle ≠ abonnement** : le premier est un actif (205), le second un service (charge, CCA).
- **Climatisation** dans un local loué : 2181 et durée limitée par le bail (ici 10 ans < bail restant) ; un simple entretien de la clim existante resterait en 615.
- **Dotation de situation intermédiaire** : toute écriture d'estimation passée pour une situation doit être **contre-passée** ou remplacée à la clôture ; sinon, doublon.
- Ne **jamais** « forcer » le rapprochement par une écriture d'écart globale.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à Camille Fabre et Nicolas Brun**

> Bonjour Camille, bonjour Nicolas,
>
> En révisant les comptes au 30/09/2026, nous avons reclassé en immobilisations 18 950 € de dépenses passées en « petit matériel » ou « entretien » (station CAO, licence ArchiPlan, climatisation, imprimante 3D, smartphones, MacBook). Elles seront amorties sur 3 à 10 ans. Le résultat de l'exercice augmente d'environ 21 400 € après ces corrections.
>
> Règle simple pour la suite : tout bien durable de plus de 500 € HT l'unité est un investissement ; les abonnements logiciels et contrats de maintenance restent des charges.
>
> Camille : merci de demander à l'Apple Store une facture au nom d'Atelier Ligne SARL pour le MacBook du 22/07, sans laquelle la TVA (398 €) ne peut pas être récupérée.
>
> Nicolas : pour les situations intermédiaires, prévenez-nous, nous passerons les dotations estimées et les contre-passerons à l'ouverture de la période suivante.
>
> Enfin, l'option d'amortissement sur 12 mois de la licence ArchiPlan permettrait de déduire 2 069 € de plus cette année : souhaitez-vous l'exercer ?

**Contrôles et documentation**
- Feuille de travail « rapprochement fichier / balance » signée, avec renvoi aux pièces (factures, mail de Nicolas, attestation de don de la table).
- Vérifier le **reçu** ou l'attestation de l'association bénéficiaire de la table (don d'un bien totalement amorti : pas de réduction d'impôt sans reçu, et valeur nulle en comptabilité).
- Paramétrer dans le logiciel de tenue une **alerte** sur les comptes 6063/615 au-delà de 500 € HT.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : définition d'un actif, logiciels acquis, dépenses ultérieures, agencements dans des locaux loués, charges constatées d'avance.
- BOFiP, BIC – Charges – tolérance des biens de faible valeur (500 € HT par unité).
- CGI, art. 236-II : amortissement exceptionnel des logiciels acquis sur 12 mois ; art. 39 B (connexion).
- CGI, art. 271-II : droit à déduction de la TVA subordonné à la détention d'une facture conforme au nom de l'assujetti.
