# E06-07 — Agencements dans un local loué et renouvellement du contrat de franchise
**Client :** C21 — FitClub Villeurbanne SAS | **Difficulté :** ★★☆ | **Durée estimée :** 1 h | **Thèmes :** agencements dans un local loué (2181), durée d'utilisation limitée par le bail 3-6-9, clause d'accession, droit d'entrée de franchise (incorporel), éléments exclus, dépôt de garantie (275), sortie d'un bien totalement amorti

**Corner case :** oui — des durées « physiques » qui dépassent la durée du bail et un droit d'entrée totalement amorti resté dans le fichier.

## La mise en situation

Mardi 6 octobre 2026. Révision de l'exercice clos le **31/08/2026** de FitClub (exercice du 01/09/2025 au 31/08/2026 ; liasse à déposer fin novembre).

Deux événements majeurs pendant l'exercice :
- le **renouvellement du contrat de franchise** avec FitNation au 01/09/2025, pour 9 ans ;
- la **prise à bail de la cellule voisine** (local de 380 m²) au 01/10/2025, pour créer un espace « cross-training » et de nouveaux vestiaires, ouvert au public le **01/12/2025**.

Romain Faure, le président, a répondu à votre questionnaire :

> « Les travaux, c'est du solide : le sol est garanti 8 ans, les vestiaires et les cloisons c'est 15-20 ans, la clim 12 ans. Le propriétaire veut vendre l'immeuble, je ne suis pas sûr qu'un nouveau propriétaire nous renouvelle le bail en 2034, on verra. Pour la franchise, tout est dans la facture FitNation. »

Le collaborateur qui a fait la tenue (parti depuis) a créé les fiches d'immobilisation avec les durées « physiques » données par Romain.

## Les pièces

**Pièce 1 — Bail commercial (extraits)**

```
BAIL COMMERCIAL — Cellule B, 152 cours Émile Zola, 69100 Villeurbanne
Bailleur : SCI ZOLA 152 (SIREN 444 870 221) — Preneur : FITCLUB VILLEURBANNE SAS (SIREN 880 300 404)
Durée : 9 années entières et consécutives du 01/10/2025 au 30/09/2034 (faculté de résiliation
triennale du preneur, art. L. 145-4 C. com.)
Loyer annuel HT : 42 000 € (TVA sur option du bailleur), payable mensuellement d'avance.
Dépôt de garantie : 3 mois de loyer HT, soit 10 500 €, non productif d'intérêts.
Article 12 — Accession : les travaux, aménagements et améliorations réalisés par le preneur
deviendront la propriété du bailleur en fin de bail, sans indemnité.
```

**Pièce 2 — Factures de travaux (synthèse) — mise en service le 01/12/2025**

| Fournisseur | Date | Objet | HT | TVA 20 % | TTC |
|---|---|---|---:|---:|---:|
| Sportbuild Rhône SAS (SIREN 829 004 117) | 25/11/2025 | Sol sportif amortissant (garantie 8 ans) | 42 000,00 | 8 400,00 | 50 400,00 |
| Sportbuild Rhône SAS | 25/11/2025 | Vestiaires, douches et sanitaires | 68 000,00 | 13 600,00 | 81 600,00 |
| Sportbuild Rhône SAS | 25/11/2025 | Cloisons, faux plafonds, éclairage | 38 000,00 | 7 600,00 | 45 600,00 |
| Clim'Air Pro SARL (SIREN 791 556 302) | 28/11/2025 | Centrale de traitement d'air et climatisation | 38 000,00 | 7 600,00 | 45 600,00 |
| **Total** | | | **186 000,00** | **37 200,00** | **223 200,00** |

**Pièce 3 — Facture du franchiseur**

```
FITNATION FRANCHISE SAS — 40 boulevard Haussmann, 75009 Paris — SIREN 512 330 908 — TVA FR 81 512 330 908
FACTURE N° FN-2025-0901-17                                         Date : 01/09/2025
Client : FITCLUB VILLEURBANNE SAS — SIREN 880 300 404
Nature de l'opération : prestations de services
Renouvellement du contrat de franchise du 01/09/2025 au 31/08/2034 (9 ans, sans tacite reconduction)
  Droit d'entrée de renouvellement (droit d'usage de la marque et du savoir-faire)    27 000,00
  Formation initiale des nouveaux coachs au concept (sessions sept. 2025)               3 500,00
  Kit marketing de relance (PLV, campagne réseaux sociaux sept.-oct. 2025)              2 800,00
  Licence annuelle du logiciel de gestion FitNation Manager (01/09/2025 - 31/08/2026)    1 800,00
                                                                         TOTAL HT     35 100,00
                                                                         TVA 20 %      7 020,00
                                                                         TOTAL TTC    42 120,00
Redevance d'exploitation : 6 % du CA HT mensuel, facturée séparément.
Échéance : 30/09/2025. Pénalités : 3 × taux d'intérêt légal ; indemnité forfaitaire 40 €.
```
Saisie actuelle : D 205 35 100,00 ; D 44562 7 020,00 ; C 404 42 120,00.

**Pièce 4 — Fichier des immobilisations (extrait avant révision)**

| N° | Désignation | Compte | Mise en service | Brut | Durée | Cumul au 31/08/2025 | Dotation 2025/26 calculée |
|---|---|---|---|---:|---|---:|---:|
| I-01 | Droit d'entrée franchise (contrat 2018-2025) | 205 | 01/09/2018 | 21 000,00 | 7 ans | 21 000,00 | 0,00 |
| I-02 | Contrat franchise 2025 (facture FN-2025-0901-17) | 205 | 01/09/2025 | 35 100,00 | 9 ans | — | 3 900,00 |
| A-11 | Sol sportif cellule B | 2181 | 01/12/2025 | 42 000,00 | 8 ans | — | 3 937,50 |
| A-12 | Vestiaires cellule B | 2181 | 01/12/2025 | 68 000,00 | 15 ans | — | 3 400,00 |
| A-13 | Cloisons, plafonds cellule B | 2181 | 01/12/2025 | 38 000,00 | 20 ans | — | 1 425,00 |
| A-14 | CVC cellule B | 2181 | 01/12/2025 | 38 000,00 | 12 ans | — | 2 375,00 |

**Pièce 5 — Grand livre 6132 (extrait)**

```
01/10/2025  BQ  PRLV SCI ZOLA 152 LOYER OCT + DÉPÔT DE GARANTIE     14 000,00   (débit 6132)
```
(3 500 € HT de loyer d'octobre — TVA traitée séparément — et 10 500 € de dépôt de garantie.)

## Travail à faire

1. Analysez la facture FitNation : qu'est-ce qui constitue une immobilisation ? Sur quelle durée l'amortir ? Fiscalement, à quelles conditions l'amortissement est-il déductible ?
2. Quelle est la durée d'amortissement des agencements de la cellule B ? Discutez l'incidence de la clause d'accession, de la résiliation triennale et du projet de vente de l'immeuble.
3. Recalculez les dotations de l'exercice 2025/2026 et chiffrez l'écart avec le fichier.
4. Passez les écritures de correction et d'inventaire au 31/08/2026 (y compris le fichier : bien I-01, dépôt de garantie).
5. Quelle serait l'incidence si, en 2028, FitClub décidait de donner congé à l'échéance triennale du 30/09/2028 ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E06-07_corrige.md)
