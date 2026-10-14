# E15-01 — Test de saisie : un lot de 8 pièces d'achats et de ventes
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Nice (ETB061) | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** test technique d'entretien, saisie au journal d'achats et de ventes, remise, frais de port, avoir, escompte, facture d'acompte, achat intracommunautaire autoliquidé, immobilisation ou charge, contrôle arithmétique d'une facture

**Corner case :** oui — une facture reçue comporte une erreur de calcul du TTC : on ne la saisit pas telle quelle

> *Cadre de formation : sociétés, documents et personnes fictifs. GSF Riviera SAS (SIREN fictif 999 100 206) n'existe pas.*

## La mise en situation

Mercredi 14/10/2026, 10 h. Entretien pour le poste d'assistante comptable au service comptable de GSF Riviera. Après l'échange oral, Laurent Vidal, chef comptable (personnage fictif), vous installe dans un bureau avec une calculatrice et un plan de comptes :

> « Voici un petit test technique, 45 minutes. Huit pièces de début octobre. Pour chacune : le journal, les comptes, l'écriture. Si une pièce ne doit pas être saisie, dites-le et dites pourquoi. Je regarde surtout votre raisonnement, pas la vitesse. »

Informations données avec le test :
- Journaux : **AC** (achats), **VT** (ventes), **BQ** (banque).
- GSF Riviera vend des **prestations de services** (nettoyage, vitrerie) et **n'a pas opté** pour le paiement de la TVA d'après les débits : la TVA sur ses factures de prestations est enregistrée en **44574 TVA collectée en attente d'encaissement**, puis virée en 44571 lors de l'encaissement.
- Seuil interne d'immobilisation (procédure fictive du groupe) : **500,00 € HT** par bien ; en dessous, charge.
- Plan de comptes utile : 2154 Matériel industriel ; 404 Fournisseurs d'immobilisations ; 401 Fournisseurs (un sous-compte par tiers) ; 411 Clients ; 4191 Clients – avances et acomptes reçus ; 4452 TVA due intracommunautaire ; 44562 TVA déductible sur immobilisations ; 44566 TVA déductible sur autres biens et services ; 445662 TVA déductible intracommunautaire ; 44571 TVA collectée ; 44574 TVA collectée en attente d'encaissement ; 512 Banque ; 6063 Fournitures d'entretien et de petit équipement ; 6241 Transports sur achats ; 665 Escomptes accordés ; 706 Prestations de services.

## Les pièces

**Pièce 1 — Facture d'achat reçue via la plateforme agréée (PA)**

```
AZUR HYGIÈNE DISTRIBUTION SAS — 12 avenue de la Lanterne, 06200 Nice
SIREN 999 401 117 — TVA FR 27 999401117
FACTURE N° F26-1214 du 01/10/2026
Client : GSF Riviera SAS, SIREN 999 100 206 — livraison : établissement de Nice
Nature de l'opération : livraison de biens

Produits d'entretien (détail joint)           1 250,00
Remise 5 %                                     - 62,50
Net commercial                                1 187,50
Frais de port                                    45,00
Total HT                                      1 232,50
TVA 20 %                                        246,50
Total TTC                                     1 479,00
Échéance : 45 jours fin de mois. Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

**Pièce 2 — Avoir reçu via la PA**

```
AZUR HYGIÈNE DISTRIBUTION SAS — SIREN 999 401 117
AVOIR N° AV-0431 du 05/10/2026 — sur facture F26-1214
Retour de 10 bidons de détergent abîmés à la livraison
Total HT 120,00 — TVA 20 % 24,00 — Total TTC 144,00
```

**Pièce 3 — Facture de vente émise par GSF Riviera**

```
GSF RIVIERA SAS — SIREN 999 100 206 — TVA FR 61 999100206
FACTURE N° FV-2026-1003 du 07/10/2026
Client : Clinique des Oliviers SAS, SIREN 999 410 233, 45 bd de Cimiez, 06000 Nice
Nature de l'opération : prestation de services
Nettoyage des locaux — septembre 2026 (contrat CT-0610)   8 400,00
Escompte 2 % pour règlement sous 10 jours                - 168,00
Net financier HT                                         8 232,00
TVA 20 %                                                 1 646,40
Total TTC                                                9 878,40
```

**Pièce 4 — Facture d'acompte émise par GSF Riviera et avis de crédit de la banque**

```
GSF RIVIERA SAS — FACTURE D'ACOMPTE N° FA-2026-0017 du 08/10/2026
Client : Cabinet Azur Syndic SARL, SIREN 999 420 377 — Résidence Les Mimosas
Nature de l'opération : prestation de services
Remise en état après travaux (devis D-2026-0288 de 5 000,00 € HT, prestation prévue en novembre)
Acompte 30 % : HT 1 500,00 — TVA 20 % 300,00 — TTC 1 800,00

Avis de crédit banque du 08/10/2026 : VIR CABINET AZUR SYNDIC REF FA-2026-0017 ... 1 800,00
```

**Pièce 5 — Facture d'un fournisseur allemand**

```
REINIGUNGSTECHNIK MÜLLER GMBH — Industriestraße 4, 70173 Stuttgart (Allemagne)
USt-IdNr. DE 999 123 456
RECHNUNG / FACTURE N° 2026-4471 du 06/10/2026
Client : GSF Riviera SAS — TVA FR 61 999100206
200 disques de lustrage + 50 brosses de récurage        2 000,00 EUR
TVA : 0,00 — Exonération, article 138 directive 2006/112/CE — Autoliquidation par le preneur
Total à payer : 2 000,00 EUR
```

**Pièce 6 — Facture d'achat de matériel**

```
ÉQUIP'PRO RIVIERA SARL — 3 chemin des Presses, 06800 Cagnes-sur-Mer
SIREN 999 430 581 — TVA FR 09 999430581
FACTURE N° EP-0977 du 09/10/2026 — Client : GSF Riviera SAS, SIREN 999 100 206
Nature de l'opération : livraison de biens
1 autolaveuse autoportée AL-75 (durée d'utilisation prévue 5 ans)   4 800,00
6 kits seaux + balais de lavage (6 × 30,00)                          180,00
Total HT 4 980,00 — TVA 20 % 996,00 — Total TTC 5 976,00
```

**Pièce 7 — Facture reçue via la PA**

```
LAVERIE INDUSTRIELLE AZUR SAS — SIREN 999 440 662
FACTURE N° LIA-5520 du 09/10/2026 — Client : GSF Riviera SAS, SIREN 999 100 206
Nature de l'opération : prestation de services
Blanchissage des tenues de travail — septembre 2026 (établissement de Nice)
Total HT 640,00 — TVA 20 % 128,00 — Total TTC 786,00
```

**Pièce 8 — Projet de facture de vente préparé par l'établissement (à émettre)**

```
GSF RIVIERA SAS — FACTURE N° FV-2026-1009 du 12/10/2026
Client : Syndic Promenade Gestion SAS — 210 promenade des Anglais, 06200 Nice
Nettoyage de vitrerie — halls A et B           1 200,00
Remise 10 % (geste commercial accordé)         - 120,00
Total HT 1 080,00 — TVA 20 % 216,00 — Total TTC 1 296,00
```

## Travail à faire

1. Pour chaque pièce, indiquez s'il faut la saisir et dans quel journal.
2. Pièce 1 : expliquez le traitement de la **remise** et des **frais de port**.
3. Pièce 3 : expliquez pourquoi l'escompte apparaît en charge et pourquoi la TVA est calculée sur 8 232,00 €.
4. Pièce 5 : expliquez le mécanisme de l'**autoliquidation** et passez l'écriture.
5. Pièce 6 : séparez ce qui est **immobilisation** et ce qui est **charge** ; justifiez.
6. Pièces 7 et 8 : relevez les anomalies et dites ce que vous faites.
7. Présentez toutes les écritures dans un tableau unique (date, journal, compte, intitulé, libellé, débit, crédit) et vérifiez l'équilibre.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-01_corrige.md)
