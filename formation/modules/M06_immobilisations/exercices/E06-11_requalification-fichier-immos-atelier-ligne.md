# E06-11 — Balayage des comptes 6063 / 615 et fichier des immobilisations qui ne colle pas
**Client :** C13 — Atelier Ligne SARL | **Difficulté :** ★★★ | **Durée estimée :** 1 h 30 | **Thèmes :** charge ou immobilisation, seuil de 500 € HT, logiciels acquis vs abonnements SaaS, agencements dans un local loué, facture au nom du gérant, prorata au jour, charges constatées d'avance, rapprochement fichier des immobilisations / balance

**Corner case :** oui — 12 factures à requalifier et un fichier des immobilisations qui diverge de la balance sur trois comptes.

## La mise en situation

Vendredi 9 octobre 2026. Atelier Ligne a clôturé le **30/09/2026** (exercice du 01/10/2025 au 30/09/2026). Vous faites la révision du cycle immobilisations ; Hélène Ferrand vous a laissé ce mot :

> « Deux sujets. Un : balayez le 6063 et le 615 au-dessus de 400 € — Camille et Nicolas passent tout en "petit matériel". Deux : le fichier des immos ne colle pas avec la balance, je veux un rapprochement ligne à ligne, pas une écriture d'ajustement. Le bail du cabinet a été renouvelé le 01/10/2024 pour 12 ans. Convention : 360 jours. »

## Les pièces

**Pièce 1 — Factures de plus de 400 € HT relevées dans les comptes 6063 et 615** (TVA à 20 % déduite en 44566 pour toutes)

| N° | Date | Fournisseur | Objet | HT | Compte utilisé |
|---|---|---|---|---:|---|
| 1 | 12/11/2025 | Lyon Informatique Pro | Station de travail CAO HP Z4 (processeur, 64 Go, carte graphique pro) | 2 850,00 | 6063 |
| 2 | 20/11/2025 | Lyon Informatique Pro | Écran 27" 4K | 420,00 | 6063 |
| 3 | 05/01/2026 | ArchiSoft France | Licence **perpétuelle** ArchiPlan Pro (1 poste), maintenance non incluse | 4 200,00 | 6063 |
| 4 | 01/07/2026 | BIMCloud SAS | Abonnement annuel plateforme BIM collaborative (01/07/2026 – 30/06/2027) | 3 600,00 | 6063 |
| 5 | 14/02/2026 | Graphitec Services | Remplacement de la tête d'impression du traceur A0 | 680,00 | 615 |
| 6 | 20/04/2026 | Clim Confort 69 | Fourniture et pose d'une climatisation réversible gainable dans les bureaux | 6 900,00 | 615 |
| 7 | 15/08/2026 | Peintures Duguesclin | Peinture des bureaux (rafraîchissement) | 3 200,00 | 615 |
| 8 | 03/03/2026 | Bureau Ergo | 6 chaises de bureau ergonomiques à 380,00 € HT (remplacement de chaises cassées) | 2 280,00 | 6063 |
| 9 | 03/06/2026 | Maker Store Lyon | Imprimante 3D pour maquettes | 1 450,00 | 6063 |
| 10 | 01/09/2026 | Copie Rhône | Contrat de maintenance annuel du copieur (01/09/2026 – 31/08/2027) | 960,00 | 615 |
| 11 | 02/09/2026 | Opérateur Mobile Pro | 3 smartphones à 520,00 € HT | 1 560,00 | 6063 |
| 12 | 22/07/2026 | Apple Store Part-Dieu | MacBook Pro 14" — facture établie au nom de **Mme Camille Fabre**, payée par la carte bancaire de la société | 1 990,00 | 6063 |

Mise en service : à la date de la facture pour tous les biens. Durées d'utilisation retenues par le cabinet : matériel informatique et téléphonie 3 ans ; logiciels 3 ans ; climatisation 10 ans.

**Pièce 2 — Fichier des immobilisations au 30/09/2026 (édition du logiciel, dotations de l'exercice incluses)**

| Compte | Valeur brute | Amortissements cumulés | VNC |
|---|---:|---:|---:|
| 205 Logiciels | 12 400,00 | 9 300,00 | 3 100,00 |
| 2181 Agencements | 38 000,00 | 22 800,00 | 15 200,00 |
| 2183 Matériel informatique | 41 650,00 | 27 940,00 | 13 710,00 |
| 2184 Mobilier | 18 200,00 | 11 060,00 | 7 140,00 |
| **Total** | **110 250,00** | **71 100,00** | **39 150,00** |

**Pièce 3 — Balance au 30/09/2026 (avant révision)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Logiciels | 12 400,00 | |
| 2805 Amortissements logiciels | | 9 300,00 |
| 2181 Agencements | 38 000,00 | |
| 28181 Amortissements agencements | | 22 800,00 |
| 2183 Matériel informatique | 44 150,00 | |
| 28183 Amortissements matériel informatique | | 29 790,00 |
| 2184 Mobilier | 15 950,00 | |
| 28184 Amortissements mobilier | | 8 810,00 |

**Pièce 4 — Éléments recueillis auprès de Nicolas Brun (cogérant)**

```
- "Le portable Dell Latitude de Lucie (2 500 € HT, acheté le 15/03/2026), je l'ai passé en 2183
  avec le fournisseur d'immobilisations, mais je n'ai pas su le créer dans le logiciel d'immos."
- "En mars, la banque voulait une situation au 31/03 : j'ai passé une dotation estimée de 1 850 €
  sur le matériel informatique. À la clôture, j'ai passé la dotation du logiciel d'immos."
- "La grande table de réunion (2 250 € HT, achetée en 2014, totalement amortie) a été donnée à une
  association en janvier : j'ai passé l'écriture de sortie, mais elle est encore dans le logiciel."
```

## Travail à faire

1. Pour chacune des 12 factures, indiquez : charge ou immobilisation, compte correct, durée, justification. Signalez les anomalies de pièces.
2. Calculez les dotations de l'exercice des biens requalifiés (prorata au jour) et les charges constatées d'avance nécessaires.
3. Licence ArchiPlan : présentez l'option fiscale d'amortissement exceptionnel et chiffrez-la (sans la comptabiliser à ce stade).
4. Établissez le rapprochement fichier / balance avant corrections : écarts par compte, explication, correction (en comptabilité ou dans le fichier ?).
5. Passez toutes les écritures de correction au 30/09/2026.
6. Présentez le rapprochement **après** corrections (il doit être nul) et l'impact total sur le résultat.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E06-11_corrige.md)
