# E12-03 — Contrôles de cohérence sur la balance de Transports Leroy
**Client :** C11 — Transports Leroy SAS | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 30 | **Thèmes :** contrôles de cohérence, comptes de tiers, TVA, capitaux propres, immobilisations, emprunts, nomenclature PCG 2025

**Corner case :** oui — anomalies cachées dans une balance « propre » en apparence, dont des comptes supprimés par le PCG 2025.

## La mise en situation

Mardi 6 octobre 2026. Bruno Leroy veut renouveler quatre tracteurs ; sa banque demande une **situation intermédiaire au 30/09/2026** « pour la semaine prochaine ». Hélène Ferrand vous confie le dossier :

> « La saisie est à jour au 30/09 (c'est Kevin, notre alternant, qui l'a faite cette année). Avant de calculer les amortissements et les régularisations de la situation, faites-moi les **contrôles de cohérence** sur la balance, sans exception. Je veux une liste d'anomalies chiffrées, les corrections, et ce qu'il faut demander à Bruno. Ne passez rien sans pièce. »

Bruno au téléphone : « La balance est bonne, Kevin a tout passé, c'est juste pour la banque, faites simple ! »

## Les pièces

### Pièce 1 — Balance générale au 30/09/2026 (exercice du 01/01 au 31/12/2026 — avant travaux de situation)

> Les dotations aux amortissements et les régularisations de la situation ne sont **pas encore passées** (281 = cumul au 31/12/2025). Les comptes auxiliaires « F-TOTAL » et « C-CARREF » sont présentés séparément parce que leur solde est de sens contraire à celui du collectif.

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 101 | Capital social |  | 80 000,00 |
| 1061 | Réserve légale |  | 8 000,00 |
| 1068 | Autres réserves |  | 310 000,00 |
| 110 | Report à nouveau |  | 21 500,00 |
| 120 | Résultat de l'exercice 2025 (bénéfice) |  | 142 000,00 |
| 1641 | Emprunts auprès des établissements de crédit |  | 640 000,00 |
| 2154 | Matériel industriel (atelier) | 86 000,00 |  |
| 2182 | Matériel de transport (tracteurs, semi-remorques) | 2 330 000,00 |  |
| 2183 | Matériel de bureau et informatique | 24 000,00 |  |
| 281 | Amortissements des immobilisations corporelles |  | 1 395 000,00 |
| 275 | Dépôts et cautionnements versés | 18 000,00 |  |
| 3221 | Stock de gazole (cuve) | 21 000,00 |  |
| 401 | Fournisseurs – autres comptes (soldes créditeurs) |  | 286 000,00 |
| 401 F-TOTAL | Fournisseur TotalEnergies Marketing France (compte auxiliaire) | 2 980,00 |  |
| 4091 | Fournisseurs – avances et acomptes versés |  |  |
| 411 | Clients – autres comptes (soldes débiteurs) | 520 000,00 |  |
| 411 C-CARREF | Client Carrefour Supply Chain (compte auxiliaire) |  | 4 560,00 |
| 421 | Personnel – rémunérations dues |  | 3 850,00 |
| 431 | URSSAF |  | 58 400,00 |
| 437 | Autres organismes sociaux |  | 21 300,00 |
| 4421 | Prélèvement à la source |  | 6 900,00 |
| 44566 | TVA déductible sur ABS | 31 200,00 |  |
| 44571 | TVA collectée |  | 49 400,00 |
| 44583 | Remboursement de TVA demandé |  |  |
| 4487 | TICPE à recevoir (remboursement partiel) | 19 400,00 |  |
| 455 | Associé – compte courant Bruno Leroy | 6 200,00 |  |
| 471 | Compte d'attente | 12 400,00 |  |
| 512 | Banque | 38 870,00 |  |
| 530 | Caisse |  | 640,00 |
| 6061 | Carburant (gazole) | 520 000,00 |  |
| 6122 | Redevances de crédit-bail mobilier | 126 000,00 |  |
| 6135 | Locations mobilières | 36 000,00 |  |
| 615 | Entretien et réparations | 110 000,00 |  |
| 616 | Assurances | 64 000,00 |  |
| 6226 | Honoraires | 21 000,00 |  |
| 6251 | Voyages et déplacements | 48 600,00 |  |
| 6256 | Missions (frais de route chauffeurs) | 72 000,00 |  |
| 6257 | Réceptions | 3 100,00 |  |
| 626 | Télécommunications | 9 800,00 |  |
| 6281 | Péages | 86 000,00 |  |
| 6355 | Taxe annuelle sur les véhicules lourds (ex-taxe à l'essieu) | 7 200,00 |  |
| 6411 | Salaires | 560 000,00 |  |
| 645 | Charges sociales | 190 000,00 |  |
| 6611 | Intérêts des emprunts | 44 600,00 |  |
| 6712 | Pénalités, amendes fiscales et pénales | 3 400,00 |  |
| 7061 | Prestations de transport |  | 1 980 000,00 |
| 758 | Produits divers |  | 1 800,00 |
| 791 | Transferts de charges d'exploitation (IJSS) |  | 2 400,00 |
| | **Totaux** | **5 011 750,00** | **5 011 750,00** |

### Pièce 2 — Extrait Kbis du 22/06/2026
```
TRANSPORTS LEROY — SAS au capital de 120 000,00 €
SIREN 803 909 101 RCS Lyon — 2 rue du Port 69200 Vénissieux
Président : M. Bruno LEROY
Mention du 18/06/2026 : augmentation du capital de 80 000 € à 120 000 € par incorporation de réserves (assemblée générale extraordinaire du 15/06/2026)
```

### Pièce 3 — Procès-verbal des assemblées générales ordinaire et extraordinaire du 15/06/2026 (extrait)
- 1re résolution (AGO) : approbation des comptes 2025, bénéfice de **142 000 €**.
- 2e résolution (AGO) : affectation — dividendes **60 000 €** (mis en paiement au plus tard le 31/12/2026, non versés au 30/09), solde **82 000 €** en « autres réserves ».
- 1re résolution (AGE) : augmentation de capital de **40 000 €** par incorporation d'une somme prélevée sur les « autres réserves ».

### Pièce 4 — Rapprochement CA comptable / CA3 déposées (préparé par Kevin)

| Mois 2026 | CA comptable HT (7061) | Base HT déclarée sur la CA3 (20 %) |
|---|---:|---:|
| Janvier | 205 000 | 205 000 |
| Février | 208 000 | 208 000 |
| Mars | 222 000 | 222 000 |
| Avril | 219 000 | 219 000 |
| Mai | 221 000 | 194 000 |
| Juin | 226 000 | 226 000 |
| Juillet | 231 000 | 231 000 |
| Août | 228 000 | 228 000 |
| Septembre | 220 000 | (CA3 à déposer en octobre) |
| **Total** | **1 980 000** | |

Note de Kevin : « Petit écart en mai, je n'ai pas trouvé, mais ça doit se compenser ailleurs. »

### Pièce 5 — Extraits de grands livres

```
421 PERSONNEL – RÉMUNÉRATIONS DUES — septembre 2026
30/09  OD PAIE   Salaires nets septembre              crédit 41 200,00
30/09  BQ        VIR SALAIRES SEPT (lot 23 salariés)  débit  37 350,00
Solde au 30/09 : 3 850,00 C

6251 VOYAGES ET DÉPLACEMENTS — septembre 2026 (extrait)
30/09  BQ        VIR DIALLO MAMADOU SAL SEPT          débit   3 850,00

471 COMPTE D'ATTENTE
28/09  BQ        PRLV DKV EURO SERVICE RELEVE 09-2026 débit  12 400,00

401 F-TOTAL — TotalEnergies Marketing France
14/08  AC        Facture n° TMF-0826-4471 (gazole cuve)            crédit 2 980,00
14/08  BQ        VIR TOTALENERGIES TMF-0826-4471                    débit  2 980,00
21/08  BQ        VIR TOTALENERGIES TMF-0826-4471                    débit  2 980,00

411 C-CARREF — Carrefour Supply Chain
31/07  VT        Facture 2026-0731                                   débit  4 560,00
28/08  BQ        VIR CARREFOUR SUPPLY FACT 2026-0731                 crédit 4 560,00
02/09  BQ        VIR CARREFOUR SUPPLY FACT 2026-0731                 crédit 4 560,00

530 CAISSE
21/09  CA        Achat ampoules et balais d'essuie-glace (ticket Norauto) crédit 640,00
Solde au 30/09 : 640,00 C (aucun mouvement de caisse depuis le 01/01, caisse vide)

455 BRUNO LEROY
03/07  BQ        CB SOCIÉTÉ — LOCATION VILLA SÉTE 12-26/07          débit  6 200,00
```

### Pièce 6 — Fichier des immobilisations (total par compte au 30/09/2026)

| Compte | Fichier | Balance |
|---|---:|---:|
| 2154 | 86 000 | 86 000 |
| 2182 | 2 258 000 | 2 330 000 |
| 2183 | 24 000 | 24 000 |

Facture Krone France n° KF-26-1187 du 08/07/2026 : semi-remorque frigorifique, **72 000 € HT**, comptabilisée en 2182.

### Pièce 7 — Attestation bancaire (Banque Populaire Rhône)
Capital restant dû au 30/09/2026 sur l'ensemble des prêts : **612 400 €** (échéances mensuelles ; capital remboursé en juillet, août et septembre : 9 200 € par mois).
Kevin : « Les échéances de juillet à septembre, je les ai passées en 6611 en entier, le tableau d'amortissement n'était pas arrivé. »

### Pièce 8 — Divers
- Le compte 6712 contient trois avis de contravention (excès de vitesse, surcharge), dont l'entreprise a désigné les conducteurs pour deux d'entre eux mais a payé les trois.
- Le compte 791 contient les IJSS reçues en subrogation pour un chauffeur en arrêt maladie (salaire maintenu).
- Taux de charges sociales patronales apparent de 2025 : 33,5 %.

## Travail à faire

1. Réalisez **tous les contrôles de cohérence** du cours (§ 5) sur cette balance, sous la forme d'un tableau : contrôle / résultat / anomalie (oui-non) / montant.
2. Pour chaque anomalie, expliquez la **cause** et proposez l'**écriture de correction** (ou le traitement si aucune écriture n'est possible sans réponse du client).
3. Calculez l'**impact** des corrections sur le résultat provisoire.
4. Rédigez le mail à Bruno Leroy listant les points à régulariser (avec le ton approprié sur le compte courant).
5. Bruno vous demande d'envoyer la situation à la banque « sans tout ça, ça ne change rien au fond ». Que répondez-vous ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E12-03_corrige.md)
