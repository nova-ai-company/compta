# E15-10 — Test technique : trouver les huit erreurs d'une balance de fin de mois
**Client :** GSF Riviera SAS (filiale régionale **fictive**, siège à Nice) — clôture mensuelle d'octobre 2026 | **Difficulté :** ★★☆ | **Durée estimée :** 45 min (test chronométré) | **Thèmes :** lecture d'une balance, sens normal des soldes, balance déséquilibrée, compte d'attente, TVA non déductible sur véhicule de tourisme, doublon de facture, immobilisation passée en charges, fournisseur débiteur, client créditeur (acompte reçu et TVA sur encaissement)

**Corner case :** oui — la balance a été ressaisie dans un tableur (d'où le déséquilibre), et certaines erreurs ne se voient que dans les comptes auxiliaires

> *Cadre de formation : sociétés, documents et personnes fictifs.*

## La mise en situation

C'est le grand classique des entretiens d'assistante comptable. Laurent Vidal, chef comptable de GSF Riviera SAS (personnage fictif), vous donne une balance et quelques extraits de grand livre : « Cette balance au 31/10/2026 a été préparée par un intérimaire, qui a recopié les soldes du logiciel dans un tableur pour me l'envoyer. Il y a **huit anomalies**. Trouvez-les, expliquez-les simplement, et proposez l'écriture de correction quand il en faut une. Vous avez **45 minutes**. Commencez par regarder les totaux. »

Rappels (fictifs) : TVA sur les prestations de services de GSF Riviera exigible **à l'encaissement** ; déclaration de TVA (CA3) d'octobre non encore déposée ; matériel de nettoyage motorisé amorti en linéaire sur 5 ans, prorata en jours (année de 360 jours) depuis la mise en service, dotations mensuelles ; biens de valeur unitaire **≤ 500 € HT** passés en charges (*seuil de tolérance à vérifier*).

## Les pièces

**Pièce 1 — Balance générale au 31/10/2026 (cumul depuis le 01/01/2026), telle que transmise**

| Compte | Intitulé | Solde débiteur | Solde créditeur |
|---|---|---|---|
| 101 | Capital | | 500 000,00 |
| 106 | Réserves | | 69 750,00 |
| 164 | Emprunts auprès des établissements de crédit | | 284 600,00 |
| 2154 | Matériel industriel | 846 300,00 | |
| 2182 | Matériel de transport | 392 800,00 | |
| 28154 | Amortissements du matériel industriel | | 412 650,00 |
| 28182 | Amortissements du matériel de transport | | 188 420,00 |
| 322 | Stocks de fournitures consommables | 21 340,00 | |
| 401 | Fournisseurs | | 318 760,00 |
| 411 | Clients | 1 486 220,00 | |
| 421 | Personnel – rémunérations dues | | 412 380,00 |
| 431 | Sécurité sociale | | 186 540,00 |
| 437 | Autres organismes sociaux | | 61 230,00 |
| 4421 | Prélèvements à la source | | 14 870,00 |
| 44562 | TVA déductible sur immobilisations | 2 140,00 | |
| 44566 | TVA déductible sur autres biens et services | 38 460,00 | |
| 44571 | TVA collectée | | 97 860,00 |
| 471 | Compte d'attente | 3 150,00 | |
| 512 | Banque | | 12 480,00 |
| 6022 | Fournitures consommables (produits d'entretien) | 214 600,00 | |
| 6063 | Fournitures d'entretien et de petit équipement | 38 950,00 | |
| 6064 | Fournitures administratives | | 620,00 |
| 611 | Sous-traitance générale | 286 400,00 | |
| 6135 | Locations mobilières | 74 300,00 | |
| 616 | Primes d'assurances | 41 200,00 | |
| 6411 | Salaires, appointements | 2 780 500,00 | |
| 6451 | Cotisations à l'URSSAF | 1 012 300,00 | |
| 6611 | Intérêts des emprunts et dettes | 8 940,00 | |
| 6811 | Dotations aux amortissements | 147 600,00 | |
| 706 | Prestations de services | | 4 860 000,00 |
| | **Totaux** | **7 395 200,00** | **7 420 160,00** |

**Pièce 2 — Relevé bancaire Banque du Comté au 31/10/2026 (extrait)**
```
Compte courant GSF RIVIERA SAS
Solde au 31/10/2026 : CRÉDITEUR 12 480,00 €
(aucune opération en suspens au rapprochement bancaire d'octobre)
```

**Pièce 3 — Extraits du grand livre d'octobre 2026**
```
6064 Fournitures administratives
  Solde au 30/09/2026                                         470,00 D
  08/10  AC  Papeterie Niçoise PN-4471                          150,00 D
  21/10  AC  Bureau Riviera FBR-26-0977                       1 240,00 C
  Solde au 31/10/2026                                         620,00 C
  (Facture FBR-26-0977 du 19/10/2026 : fournitures et cartouches, 1 240,00 HT
   + TVA 248,00 = 1 488,00 TTC ; écriture saisie : 401 D 1 488,00 / 6064 C 1 240,00
   / 44566 C 248,00)

471 Compte d'attente
  14/10  BQ  PRLV SEPA PREVOYANCE AZUR ECH 09/2026            3 150,00 D
  (avis d'échéance Prévoyance Azur : cotisations prévoyance de septembre 2026,
   parts salariale et patronale, comptabilisées en 437 lors de la paie de septembre)

44566 TVA déductible sur autres biens et services (extrait)
  Janvier à octobre : 10 lignes « Riviera Location Longue Durée – loyer berline
  du directeur d'agence (véhicule de tourisme) » : 640,00 HT + 128,00 TVA par mois
  → 1 280,00 de TVA portés en 44566 ; loyers HT en 6135

6022 Fournitures consommables (extrait)
  06/10  AC  Hygiène Pro HP-26-1188 (flux plateforme agréée)  4 050,00 D
  22/10  AC  Hygiène Pro HP-26-1188 (PDF reçu par e-mail)     4 050,00 D
  (TVA 810,00 et TTC 4 860,00 à chaque saisie)

6063 Fournitures d'entretien et de petit équipement (extrait)
  15/10  AC  Nett'Équip NE-26-0712 injecteur-extracteur IE-30
             n° série IE30-26-1145                            3 900,00 D
  (TVA 780,00 en 44566 ; PV de mise en service du 12/10/2026, établissement d'Antibes)
```

**Pièce 4 — Extraits des balances auxiliaires**
```
FOURNISSEURS
401DSP Distri-Sacs Provence (SIREN 999 274 905, fictif)
  28/09  AC  Facture DSP-552                                  1 980,00 C
  12/10  BQ  Virement règlement DSP-552                       1 980,00 D
  20/10  BQ  Virement « DISTRI-H. FACTURE DH-3307 »           2 340,00 D
  Solde                                                       2 340,00 D
401DHY Distri-Hygiène (SIREN 999 461 702, fictif)
  30/09  AC  Facture DH-3307                                  2 340,00 C
  Solde                                                       2 340,00 C

CLIENTS
411MER Copropriété Le Méridien (syndic fictif)
  16/10  BQ  VIR COPRO LE MERIDIEN ACOMPTE DEVIS D-26-318     1 800,00 C
  Solde                                                       1 800,00 C
  (Devis D-26-318 accepté : remise en état des parties communes prévue en
   novembre 2026, 3 750,00 € HT ; acompte de 40 % TTC demandé à la commande ;
   aucune facture émise)
```

## Travail à faire

1. La balance est-elle équilibrée ? Calculez l'écart et utilisez-le pour trouver **la première anomalie**. Pourquoi une balance sortie directement d'un logiciel est-elle toujours équilibrée ?
2. Pour chacune des **huit anomalies** : dites où vous la voyez (balance, grand livre ou auxiliaire), expliquez **en une ou deux phrases** pourquoi c'est anormal, et donnez la correction (écriture datée du 31/10/2026 quand il en faut une).
3. Présentez la **balance corrigée** au 31/10/2026.
4. Question orale : « Quand vous recevez une balance, quels sont les cinq premiers contrôles que vous faites ? »

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-10_corrige.md)
