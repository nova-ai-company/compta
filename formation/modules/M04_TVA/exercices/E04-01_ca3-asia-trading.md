# E04-01 — La CA3 de septembre d'Asia Trading
**Client :** C19 — Asia Trading SARL | **Difficulté :** ★★★ | **Durée estimée :** 1 h 15 | **Thèmes :** CA3 complète, importation et autoliquidation, base de la TVA à l'importation, livraison intracommunautaire, carburants, cadeaux, écriture de liquidation de TVA

**Corner case :** oui — base d'importation calculée sur la facture FOB du fournisseur au lieu du DAU, et facture de LIC sans mention d'exonération

## La mise en situation

Kevin Nguyen, gérant d'Asia Trading, vous envoie le 9 octobre 2026 les pièces de septembre et son brouillon :

> Bonjour, voilà le dossier de septembre. J'ai essayé de pré-remplir la TVA pour vous faire gagner du temps : pour l'import, j'ai pris la facture du fournisseur chinois (62 300 $ × 0,9165 = 57 097,95 €), TVA 20 % = 11 419,59 €. Et j'ai tout mis en déductible, même les coffrets cadeaux de fin de saison pour nos clients, c'est bien pour le business non ? La déclaration est à déposer au plus tard le 19/10. Kevin

Asia Trading est au réel normal (CA3 mensuelle). Aucun crédit de TVA n'a été reporté de la déclaration d'août.

## Les pièces

### Pièce 1 — Journal des ventes de septembre 2026 (récapitulatif)

| Catégorie | Clients | HT | TVA | TTC |
|---|---|---|---|---|
| Ventes France (magasins de décoration) | 47 factures | 186 400,00 | 37 280,00 | 223 680,00 |
| Ventes Belgique | 1 facture (ci-dessous) | 42 600,00 | 0,00 | 42 600,00 |

### Pièce 2 — Facture de vente en Belgique

```
ASIA TRADING SARL – 60 avenue Berthelot – 69007 Lyon – SIREN 838 900 101 – TVA FR 34 838900101
FACTURE N° AT-2026-0918 du 22/09/2026 – Nature : livraison de biens
Client : LUMIÈRE & MAISON SRL – Rue Neuve 88 – 1000 Bruxelles – TVA BE 0712.554.390
Livraison : entrepôt du client à Bruxelles – transport par Transports Leroy (CMR n° 26-04471), livré le 24/09/2026
480 suspensions « Lotus » × 62,50 €          30 000,00
210 lampadaires « Bambou » × 60,00 €         12 600,00
Total HT                                     42 600,00
TVA 0 %                                           0,00
Total                                        42 600,00     Paiement à 45 jours fin de mois
```
Consultation VIES du 21/09/2026 : numéro BE 0712.554.390 **valide**, capture archivée.

### Pièce 3 — Déclaration d'importation (DAU) — extrait

```
DAU n° 26FR6900IM0447213 – date d'acceptation 08/09/2026 – Bureau de Lyon
Importateur : ASIA TRADING SARL – EORI FR838900101 – n° TVA FR 34 838900101
Marchandises : luminaires (position 9405) – origine Chine – fournisseur Shenzhen Brightway Lighting Co.
Valeur facture : 62 300,00 USD (FOB Shenzhen)
Valeur en douane (CIF Fos-sur-Mer, taux de change douane du mois) : 62 000,00 EUR
Droits de douane 4,7 %                                      2 914,00 EUR
TVA : AUTOLIQUIDATION (art. 1695 II du CGI) – base et montant à déclarer sur la CA3
```

### Pièce 4 — Facture du transitaire

```
RHÔNE TRANSIT SAS – SIREN 519 004 881 – facture n° RT-26-3390 du 10/09/2026
Fret maritime Shenzhen → Fos (inclus dans la valeur CIF) – transport international      4 900,00  (exonéré)
Honoraires de dédouanement                                       HT 380,00 – TVA 20 %   76,00
Débours : droits de douane acquittés pour votre compte (DAU 26FR6900IM0447213)        2 914,00
Total TTC à payer                                                                     8 270,00
```

### Pièce 5 — Achats et frais de septembre (factures au nom d'Asia Trading, toutes conformes)

| Nature | HT | TVA |
|---|---|---|
| Emballages, cartons | 3 200,00 | 640,00 |
| Loyer de l'entrepôt (bailleur ayant opté pour la TVA) | 6 000,00 | 1 200,00 |
| Énergie, télécom | 1 400,00 | 280,00 |
| Honoraires (avocat, expert-comptable) | 2 600,00 | 520,00 |
| Marketing (salon professionnel à Lyon) | 1 600,00 | 320,00 |
| Gazole — fourgon utilitaire (carte grise CTTE) | 600,00 | 120,00 |
| Essence (SP95) — véhicule de tourisme du gérant | 250,00 | 50,00 |
| Coffrets cadeaux clients : 30 coffrets à 90,00 € TTC | 2 250,00 | 450,00 |
| Rayonnages de stockage (immobilisation, facture du 15/09) | 9 500,00 | 1 900,00 |

## Travail à faire

1. Relevez les erreurs du raisonnement de Kevin et les anomalies des pièces.
2. Calculez la base et le montant de la TVA à l'importation. Comment cette TVA est-elle déclarée et payée ?
3. Déterminez la TVA déductible du mois, ligne par ligne.
4. Remplissez la CA3 de septembre 2026 (lignes A1, A4, F2, 08, 16, 19, 20, 23, 24, 28 et 32, plus toute autre ligne utile).
5. Passez l'écriture de constatation de la TVA à l'importation et l'écriture de liquidation de la TVA au 30/09/2026.
6. Quelles autres obligations déclaratives découlent de la vente en Belgique ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E04-01_corrige.md)
