# Corrigé E03-03 — Honoraires d'architecte par phases, acompte et en-cours

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-03](../exercices/E03-03_honoraires-architecte-phases.md)

## 1. Analyse

**a) Le fait générateur des honoraires** est l'achèvement de chaque élément de mission (le contrat prévoit une facturation à l'achèvement). La phase APD est achevée le 22/09/2026 : le produit appartient bien à l'exercice clos le 30/09/2026, et la date de facture du 30/09 est correcte (une facture établie en octobre aurait imposé un 4181 « facture à établir »).

**b) L'acompte de janvier** a été comptabilisé en 4191 (avance reçue, dette envers le client) avec TVA, exigible dès son encaissement (prestation de services, TVA sur encaissements). Il s'impute **en HT** sur la phase APD : on facture 6 300 € HT, on déduit 4 200 € HT d'acompte déjà facturé, la TVA de la facture ne porte que sur le **solde non encore soumis**.

Présenter « TTC de la phase – acompte TTC » donne ici le même net à payer (même taux), mais **c'est une mauvaise pratique** : la facture doit faire apparaître clairement la base HT restant due et la TVA correspondante, et rappeler la référence de la facture d'acompte (n° 2026-004).

**c) La reprographie n'est pas un débours.** Atelier Ligne commande les tirages **en son nom**, pour exécuter **sa propre mission** (la facture de Copy'Lyon est à son nom et elle a déduit la TVA de 36 €). Les conditions de l'art. 267-II-2° CGI (mandat, compte de passage, refacturation au nom du client) ne sont pas réunies : c'est un **frais accessoire** de la prestation, soumis à la TVA à 20 % et comptabilisé en produit.

**d) Client particulier.** L'indemnité forfaitaire de 40 € et les mentions de pénalités issues de l'art. L. 441-10 C. com. ne concernent que les **professionnels**. Face à des particuliers, la mention de l'indemnité de 40 € est **inappropriée** (et inopposable). Pas de SIREN client ; pas de facturation électronique (en B2C, Atelier Ligne fera de l'**e-reporting** des données de transaction et de paiement à compter du 01/09/2027).

**e) La phase PRO commencée.** Prestation partiellement exécutée, non facturable (facturation à l'achèvement de la phase) : c'est un **en-cours de production de services** (compte 345), évalué **au coût de production**, jamais au prix de vente (pas de marge anticipée), et dans la limite de la valeur de réalisation.

**Anomalies du projet de facture :**
1. Déduction de l'acompte en TTC au lieu du HT, sans référence à la facture d'acompte n° 2026-004.
2. Reprographie présentée comme débours non soumis à TVA (il manque 36 € de TVA).
3. Indemnité de 40 € mentionnée face à des particuliers.
4. Nature de l'opération (prestation de services) et date d'achèvement de la phase non mentionnées.
5. Pas de mention de la date d'échéance (le « 30 jours » doit se traduire par une date : 30/10/2026).

## 2. Calculs

| Élément | Calcul | Montant |
|---|---|---|
| Honoraires totaux | 420 000 × 10 % | 42 000,00 |
| ESQ + APS | 42 000 × 15 % | 6 300,00 |
| APD | 42 000 × 15 % | 6 300,00 |
| Acompte imputé (HT) | 42 000 × 10 % | 4 200,00 |
| Solde APD HT | 6 300 – 4 200 | 2 100,00 |
| Reprographie HT | coût réel | 180,00 |
| Base HT de la facture 2026-118 | 2 100 + 180 | **2 280,00** |
| TVA 20 % | | **456,00** |
| Net à payer TTC | | **2 736,00** |

Contrôle : le projet de l'assistante (2 700 €) sous-facturait 36 € (TVA sur reprographie).

**En-cours PRO** : 62 h × 48 €/h = **2 976,00 €**. Valeur de réalisation : 40 % × 10 500 € (honoraires PRO/DCE = 42 000 × 25 %) = 4 200 € > 2 976 € → pas de dépréciation.

**Récapitulatif du contrat au 30/09/2026** : facturé HT cumulé = 4 200 (acompte) + 6 300 + 2 100 (+ 180 de frais) = 12 600 € d'honoraires = ESQ + APS + APD (30 % de 42 000). ✔

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 12/01/2026 | VT | 411ROCH | Client Roche | Facture d'acompte 2026-004 | 5 040,00 | |
| 12/01/2026 | VT | 4191 | Clients – avances et acomptes reçus | Facture d'acompte 2026-004 | | 4 200,00 |
| 12/01/2026 | VT | 44574 | TVA collectée en attente | Facture d'acompte 2026-004 | | 840,00 |
| 15/01/2026 | BQ | 512 | Banque | Encaissement 2026-004 | 5 040,00 | |
| 15/01/2026 | BQ | 411ROCH | Client Roche | Encaissement 2026-004 | | 5 040,00 |
| 15/01/2026 | OD | 44574 | TVA collectée en attente | TVA exigible – encaissement | 840,00 | |
| 15/01/2026 | OD | 44571 | TVA collectée | TVA exigible – encaissement | | 840,00 |
| 10/04/2026 | VT | 411ROCH | Client Roche | Facture 2026-031 ESQ+APS | 7 560,00 | |
| 10/04/2026 | VT | 706 | Prestations de services | Facture 2026-031 ESQ+APS | | 6 300,00 |
| 10/04/2026 | VT | 44574 | TVA collectée en attente | Facture 2026-031 | | 1 260,00 |
| 28/04/2026 | BQ | 512 | Banque | Encaissement 2026-031 | 7 560,00 | |
| 28/04/2026 | BQ | 411ROCH | Client Roche | Encaissement 2026-031 | | 7 560,00 |
| 28/04/2026 | OD | 44574 | TVA collectée en attente | TVA exigible – encaissement | 1 260,00 | |
| 28/04/2026 | OD | 44571 | TVA collectée | TVA exigible – encaissement | | 1 260,00 |
| 30/09/2026 | VT | 411ROCH | Client Roche | Facture 2026-118 APD | 2 736,00 | |
| 30/09/2026 | VT | 4191 | Clients – avances et acomptes reçus | Imputation acompte 2026-004 | 4 200,00 | |
| 30/09/2026 | VT | 706 | Prestations de services | Phase APD | | 6 300,00 |
| 30/09/2026 | VT | 7088 | Autres produits d'activités annexes (frais refacturés) | Reprographie APD | | 180,00 |
| 30/09/2026 | VT | 44574 | TVA collectée en attente | Facture 2026-118 | | 456,00 |
| 30/09/2026 | OD | 345 | En-cours de production de services | En-cours phase PRO Roche (62 h × 48 €) | 2 976,00 | |
| 30/09/2026 | OD | 7134 | Variation des en-cours de production de services | En-cours phase PRO Roche | | 2 976,00 |
| | | | | **Totaux** | **37 212,00** | **37 212,00** |

(La refacturation de reprographie peut aussi être enregistrée en 706 si le cabinet préfère un seul compte d'honoraires ; l'essentiel est qu'elle soit en produit, avec TVA.)

Au 01/10/2026 (exercice suivant), l'en-cours sera extourné (345 / 7134 inversés) et un nouvel en-cours sera constaté à la clôture suivante.

## 4. Points d'attention / pièges

- **TVA de septembre 2026** sur ce dossier : **0 €**. La facture 2026-118 n'est pas encaissée au 30/09 ; ses 456 € restent en 44574 et seront déclarés le mois du paiement (octobre ou novembre). L'acompte et la facture d'avril ont été déclarés en janvier et en avril.
- **4191 soldé** : après imputation, le compte d'acompte du client Roche doit être à zéro. Un 4191 résiduel à la clôture d'Atelier Ligne doit être justifié contrat par contrat.
- **En-cours au coût, pas au prix** : valoriser 40 % de 10 500 € (4 200 €) serait anticiper une marge non acquise. Le coût horaire ne comprend ni les frais commerciaux ni les frais administratifs généraux.
- **Ne pas facturer la phase PRO à 40 %** pour « gonfler » l'exercice : contraire au contrat, et la TVA deviendrait exigible au premier encaissement.
- **Débours** : la qualification dépend du **nom sous lequel la dépense est engagée** et du mandat, pas de la volonté de « refacturer au coût ».

## 5. Ce qu'un senior ferait en plus

**Corps de la facture correcte à transmettre à Camille :**

```
FACTURE N° 2026-118 – Date : 30/09/2026 – Nature : prestation de services (maîtrise d'œuvre)
Client : M. et Mme ROCHE – 8 chemin de la Sauvegarde – 69130 Écully
Contrat du 12/01/2026 – Maison individuelle Écully
Élément de mission APD – achevé le 22/09/2026 (15 % × 42 000 € HT)        6 300,00
Déduction de l'acompte facturé le 12/01/2026 (facture n° 2026-004), HT   – 4 200,00
Solde honoraires APD HT                                                    2 100,00
Frais de reprographie dossier APD (au coût réel)                            180,00
Total HT                                                                   2 280,00
TVA 20 %                                                                     456,00
TOTAL TTC À PAYER                                                          2 736,00
Échéance : 30/10/2026 – Règlement par virement (IBAN …)
```

**Conseil au client :** profiter de cette facture pour paramétrer le logiciel de facturation (modèle « facture de phase avec imputation d'acompte HT »), distinguer clients particuliers et professionnels (mentions LME, SIREN du client), et préparer l'e-reporting des encaissements (prestations de services) de 2027.

**Dossier de révision :** documenter le calcul du coût horaire (feuille de temps, masse salariale de production / heures productives) et faire **signer par la gérance l'état des en-cours** au 30/09 (relevé phase par phase, client par client).

## 6. Références

- PCG : comptes 4191, 345, 7134 ; règles d'évaluation des stocks et en-cours au coût de production (art. 213-1 et suivants du PCG — dispositions sur le coût d'entrée).
- CGI : art. 267-II-2° (débours), art. 269-2-c (exigibilité à l'encaissement), art. 289 et 242 nonies A ann. II (mentions des factures).
- Code de commerce : art. L. 441-9 et L. 441-10 (mentions et pénalités entre professionnels uniquement).
- Loi n° 77-2 du 3 janvier 1977 sur l'architecture (contrat écrit obligatoire).
