# E02-07 — Le relevé mensuel des cartes carburant
**Client :** C11 — Transports Leroy | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** TVA sur carburants (gazole / essence, VP / VU), services afférents aux véhicules, péages, facture récapitulative, dépense non justifiée, TICPE (aperçu)

**Corner case :** oui — un achat « boutique » sans détail sur une carte carburant et le lavage de la berline du président

## La mise en situation

Transports Leroy reçoit chaque mois de son émetteur de cartes carburant une facture récapitulative, prélevée le 10 du mois suivant. Jusqu'ici, la saisie était faite « en bloc » : tout en 6061, toute la TVA en 44566. Hélène Ferrand vous confie le dossier :

> « Le relevé de septembre est arrivé. Je veux une saisie ventilée, avec la bonne TVA par véhicule. Bruno Leroy a deux voitures de société dans le parc depuis cette année, je ne suis pas sûre qu'on ait fait attention. Et regardez la ligne boutique. »

Rappels : SAS, réel normal, CA3 mensuelle. Parc : 16 tracteurs routiers (poids lourds ≥ 7,5 t), 1 Renault Master (camionnette, carte grise « CTTE »), 1 Renault Kangoo Van (camionnette « CTTE »), 1 Peugeot 508 (berline, carte grise « VP ») utilisée par Bruno Leroy, 1 Renault Clio (« VP ») utilisée par le commercial.

## Les pièces

```
CARBUPRO SERVICES SAS — Solutions de paiement carburant pour professionnels
Tour Lumière, 40 avenue Jean Jaurès, 69007 Lyon
SAS au capital de 2 500 000 € — RCS Lyon 401 778 652 — TVA FR00 401778652

FACTURE RÉCAPITULATIVE N° CP-2026-09-018834              Date : 30/09/2026
Période : 01/09/2026 – 30/09/2026 — Compte client 77-1043
Client : TRANSPORTS LEROY SAS — SIREN 803 909 101 — 2 rue du Port, 69200 Vénissieux
Nature de l'opération : livraisons de biens et prestations de services
Prélèvement SEPA le 10/10/2026

Carte / véhicule                 Produit          Quantité     PU HT      HT          TVA 20 %     TTC
Cartes PL (16 tracteurs)         Gazole           21 450 l    1,4250   30 566,25    6 113,25   36 679,50
GG-123-AB Renault Master         Gazole              380 l    1,4400      547,20      109,44      656,64
FR-508-LB Peugeot 508            Gazole              210 l    1,4600      306,60       61,32      367,92
EK-771-CL Renault Clio           SP95-E10            160 l    1,4900      238,40       47,68      286,08
FT-225-KG Renault Kangoo Van     SP95                 95 l    1,5100      143,45       28,69      172,14
Cartes PL (16 tracteurs)         AdBlue            1 200 l    0,5500      660,00      132,00      792,00
Cartes PL                        Péages autoroutes                       2 755,00      551,00    3 306,00
FR-508-LB Peugeot 508            Péages autoroutes                          85,00       17,00      102,00
Cartes PL                        Lavage poids lourd   12 x               420,00       84,00      504,00
FR-508-LB Peugeot 508            Lavage auto           1 x                25,00        5,00       30,00
Carte PL n° 09 (tracteur EH-409) Boutique (divers) — détail non disponible                            41,58
                                                               ------------------------------------------
                                                    TOTAL HT  35 746,90  (hors boutique)
                                                    TOTAL TVA  7 149,38  (hors boutique)
                                                    TOTAL TTC À PRÉLEVER                     42 937,86
Les péages sont refacturés pour le compte des sociétés d'autoroute (factures détaillées
disponibles sur l'espace client). Pénalités : 3 x taux légal — Indemnité forfaitaire : 40 €.
```

## Travail à faire

1. Rappelez les règles de déduction de la TVA applicables à chaque type de dépense du relevé, selon la catégorie du véhicule.
2. Établissez le tableau de ventilation : HT, TVA facturée, TVA déductible, TVA non déductible, compte de charge, pour chaque ligne.
3. Passez l'écriture de la facture récapitulative et celle du prélèvement.
4. Que faites-vous de la ligne « Boutique » ?
5. Quelle a été l'erreur des mois précédents ? Estimez l'enjeu annuel sur la base de ce mois.
6. Les 21 450 litres de gazole des tracteurs ouvrent droit au remboursement partiel de TICPE. On retient un taux de remboursement de **15,25 € par hectolitre** (*valeur à vérifier chaque année et selon la région*). Calculez le montant correspondant et dites quand et comment il sera comptabilisé.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E02-07_corrige.md)
