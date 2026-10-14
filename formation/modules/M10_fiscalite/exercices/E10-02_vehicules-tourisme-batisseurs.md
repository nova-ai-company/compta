# E10-02 — Le SUV du président : amortissement excédentaire et taxes annuelles
**Client :** C02 — Bâtisseurs du Sud SAS | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** véhicule de tourisme, plafond art. 39-4, taxe annuelle CO₂, taxe polluants, prorata, conseil achat de fin d'année

**Corner case :** oui — un pick-up double cabine 5 places que la société considère comme « utilitaire ».

## La mise en situation

Mardi 13 octobre 2026. Karim Benali appelle, ravi :

> « J'ai pris le SUV en juillet comme je vous avais dit. Nadia a fait des calculs bizarres de "taxe CO₂", elle dit que ça ne se déduit même pas ! Et je voudrais racheter une voiture pour mon conducteur de travaux en décembre, une électrique ou le même SUV, pour payer moins d'impôt cette année. Vous me dites quoi ? Ah, et le pick-up Ranger, c'est un utilitaire, hein, on n'a rien à payer dessus ? »

Hélène Ferrand vous demande de **contrôler les calculs de Nadia** (qui ont été repris dans le fichier « trucs fiscaux » de l'exercice E10-01) et de préparer une réponse chiffrée pour Karim.

## Les pièces

**Pièce 1 — Facture d'achat du SUV**

```
AUTO DISTRIBUTION RHÔNE SAS — 140 route de Grenoble, 69800 Saint-Priest
SIREN 734 221 908 — TVA FR 52 734 221 908
FACTURE N° VN-2026-0718                          Date : 01/07/2026
Client : BÂTISSEURS DU SUD SAS, ZA des Plaines, 69800 Saint-Priest — SIREN 812 450 776
Livraison : idem — Nature de l'opération : livraison de biens

Désignation                                         Qté      PU HT        Total HT
SUV 4x4 2.0 diesel 180 ch — boîte auto              1     43 650,00      43 650,00
  Genre national : VP — carrosserie CI — 5 places
  CO2 (WLTP) : 158 g/km — Puissance fiscale : 10 CV — Crit'Air 2
Frais de mise à la route                             1        350,00         350,00
                                                         TOTAL HT       44 000,00
                                                         TVA 20 %        8 800,00
                                                         TOTAL TTC      52 800,00
Carte grise et taxe à l'immatriculation : facturées séparément (débours)
Règlement : virement à la livraison. Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

**Pièce 2 — Fiche d'immobilisation saisie par Nadia**

```
Immobilisation : SUV 4x4 diesel — Compte 2182 — Mise en service 01/07/2026
Valeur d'origine : 52 800,00 € TTC (TVA non récupérable)
Mode : linéaire 5 ans — Dotation 2026 : 5 280,00 €
Utilisateur : Karim Benali (usage professionnel et privé — avantage en nature déclaré en paie)
Note Nadia : "non déductible = 5 280 × (52 800 – 9 900) / 52 800 = 4 290 €"
             "taxes 2026 = 813 + 252 = 1 065 € (charge à payer, déclaration CA3 de janvier 2027)"
```

**Pièce 3 — Carte grise du pick-up (extrait)**

```
Véhicule : pick-up double cabine 2.0 diesel — mis en service le 15/03/2024
J.1 Genre national : CTTE (camionnette) — J.2 Carrosserie : BE (pick-up)
S.1 Nombre de places assises : 5 — V.7 CO2 (WLTP) : 236 g/km
Affecté toute l'année 2026 aux chantiers (transport du chef d'équipe, de 2 compagnons et du petit matériel)
Acquis 38 400 € HT, TVA déduite, amorti sur 5 ans sans plafonnement
```

**Pièce 4 — Paramètres retenus pour l'exercice 2026 (valeurs à vérifier chaque année)**

| Plafond d'amortissement (véhicules WLTP, immatriculés depuis 2021) | |
|---|---|
| CO₂ < 20 g/km | 30 000 € |
| 20 à 49 g/km | 20 300 € |
| 50 à 160 g/km | 18 300 € |
| > 160 g/km | 9 900 € |

*Note : l'ancien seuil de 130 g/km concernait les véhicules mesurés en norme NEDC ; les seuils ci-dessus sont ceux de la norme WLTP (véhicules immatriculés depuis 2021).*

Barème de la **taxe annuelle sur les émissions de CO₂** retenu (tarif marginal par gramme, WLTP) :

| Fraction des émissions (g/km) | Tarif par gramme |
|---|---|
| jusqu'à 14 | 0 € |
| de 15 à 55 | 1 € |
| de 56 à 63 | 2 € |
| de 64 à 95 | 3 € |
| de 96 à 115 | 4 € |
| de 116 à 135 | 10 € |
| de 136 à 155 | 50 € |
| de 156 à 175 | 60 € |
| au-delà de 175 | 65 € |

**Taxe annuelle polluants** retenue : électrique/hydrogène 0 € ; essence, gaz, hybrides (catégorie « 1 ») 100 € ; véhicules les plus polluants (dont diesel) 500 €.
Prorata : nombre de jours d'affectation / 365. Montants arrondis à l'euro le plus proche.

## Travail à faire

1. Vérifiez le calcul de l'amortissement non déductible du SUV pour 2026 et donnez le montant pour une année pleine (2027).
2. Recalculez les deux taxes annuelles 2026 du SUV, précisez leur traitement comptable et fiscal et leur date de déclaration.
3. Passez l'écriture de charge à payer des taxes au 31/12/2026.
4. Le pick-up est-il un « utilitaire » ? Analysez et, si nécessaire, chiffrez le risque pour 2026.
5. Répondez à Karim sur son projet d'achat en décembre (électrique à 45 000 € TTC, CO₂ 0 g, ou même SUV diesel, livraison le 14/12/2026) : comparez l'effet fiscal 2026 des deux options.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E10-02_corrige.md)
