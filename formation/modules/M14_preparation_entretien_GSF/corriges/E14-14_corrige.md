# Corrigé E14-14 — Clôture mensuelle à J+5 d'un établissement : FNP, FAE, CCA, PCA et extournes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-14](../exercices/E14-14_cloture-mensuelle-j5-etablissement.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Le **cut-off** répond à une question unique : *ce produit ou cette charge concerne-t-il septembre ?* Si oui et qu'il n'est pas (encore) comptabilisé → **FNP / FAE**. S'il est comptabilisé en septembre mais concerne un mois ultérieur → **CCA / PCA**.

| N° | Décision | Justification |
|---|---|---|
| 1 | **Aucune FNP** | La facture F26-7851, datée du 30/09, est arrivée le 02/10 : la période de septembre étant ouverte jusqu'à J+5, on la **saisit en septembre** (date de facture). Une FNP en plus créerait un **doublon** (charge comptée deux fois). |
| 2 | **FNP 860,00 € HT** + TVA 172,00 € | Prestation de septembre rendue, montant contractuel certain. |
| 3 | **FNP 310,00 € HT** + TVA 62,00 € | Consommation de septembre, estimée sur relevé de compteur (estimation fiable et documentée). |
| 4 | **FAE 2 400,00 € HT** + TVA 480,00 € | Travaux réalisés en septembre, accord client (devis + bon d'intervention signé) : droit acquis. |
| 5 | **FAE 1 350,00 € HT** + TVA 270,00 € | Intervention réalisée sur BC : droit acquis. |
| 6 | **CCA 4 500,00 €** | Loyer d'octobre-décembre comptabilisé en septembre. |
| 7 | **PCA 3 600,00 €** | Prestation d'octobre-décembre facturée d'avance et comptabilisée en septembre. |

TVA : sur FNP et FAE, la TVA est « en attente » (44586, 44587) : elle ne sera déductible / exigible qu'avec la facture (et, pour les ventes de GSF Riviera, à l'encaissement). Les CCA et PCA se calculent **HT** : la TVA de la facture a suivi ses propres règles.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | HT | TVA 20 % | TTC |
|---|---|---|---|
| FNP EcoCollecte | 860,00 | 172,00 | 1 032,00 |
| FNP électricité | 310,00 | 62,00 | 372,00 |
| **Total FNP** | **1 170,00** | **234,00** | **1 404,00** |
| FAE Agrodélices | 2 400,00 | 480,00 | 2 880,00 |
| FAE Pharmabel | 1 350,00 | 270,00 | 1 620,00 |
| **Total FAE** | **3 750,00** | **750,00** | **4 500,00** |
| CCA loyer T4 | 4 500,00 | | |
| PCA désinfection T4 | 3 600,00 | | |

**Impact sur le résultat de septembre de l'établissement (question 3)** :
− 1 170,00 (FNP) + 3 750,00 (FAE) + 4 500,00 (CCA) − 3 600,00 (PCA) = **+ 3 480,00 €**.
(Sans ces écritures, le résultat de septembre aurait été faussé dans les deux sens : un trimestre de loyer en charge et un trimestre de désinfection en produit.)

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | HPD F26-7851 BR-ANT-0655 (ANT) | 2 140,00 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | HPD F26-7851 TVA 20 % | 428,00 | |
| 30/09/2026 | AC | 401HPD | Fournisseur Hygiène Pro Distribution | HPD F26-7851 | | 2 568,00 |
| 30/09/2026 | OD | 6288 | Autres services extérieurs – enlèvement des déchets | FNP EcoCollecte DIB 09/2026 (ANT) | 860,00 | |
| 30/09/2026 | OD | 6061 | Fournitures non stockables (énergie) | FNP électricité agence 09/2026 (ANT) | 310,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP 09/2026 TVA (ANT) | 234,00 | |
| 30/09/2026 | OD | 4081 | Fournisseurs – factures non parvenues | FNP 09/2026 (ANT) | | 1 404,00 |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | FAE 09/2026 Agrodélices + Pharmabel (ANT) | 4 500,00 | |
| 30/09/2026 | OD | 706 | Prestations de services (ANT) | FAE Agrodélices remise en état DV-ANT-2026-077 | | 2 400,00 |
| 30/09/2026 | OD | 706 | Prestations de services (ANT) | FAE Pharmabel vitrerie 29/09 | | 1 350,00 |
| 30/09/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | FAE 09/2026 TVA (ANT) | | 750,00 |
| 30/09/2026 | OD | 486 | Charges constatées d'avance | CCA loyer agence T4 2026 (ANT) | 4 500,00 | |
| 30/09/2026 | OD | 6132 | Locations immobilières | CCA loyer agence T4 2026 (ANT) | | 4 500,00 |
| 30/09/2026 | OD | 706 | Prestations de services (ANT) | PCA Agrodélices désinfection T4 FR-2026-09-0510 | 3 600,00 | |
| 30/09/2026 | OD | 487 | Produits constatés d'avance | PCA Agrodélices désinfection T4 | | 3 600,00 |
| 01/10/2026 | OD | 4081 | Fournisseurs – factures non parvenues | Extourne FNP 09/2026 (ANT) | 1 404,00 | |
| 01/10/2026 | OD | 6288 | Autres services extérieurs – enlèvement des déchets | Extourne FNP EcoCollecte | | 860,00 |
| 01/10/2026 | OD | 6061 | Fournitures non stockables (énergie) | Extourne FNP électricité | | 310,00 |
| 01/10/2026 | OD | 44586 | TVA sur factures non parvenues | Extourne FNP 09/2026 TVA | | 234,00 |
| 01/10/2026 | OD | 706 | Prestations de services (ANT) | Extourne FAE Agrodélices | 2 400,00 | |
| 01/10/2026 | OD | 706 | Prestations de services (ANT) | Extourne FAE Pharmabel | 1 350,00 | |
| 01/10/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | Extourne FAE 09/2026 TVA | 750,00 | |
| 01/10/2026 | OD | 4181 | Clients – factures à établir | Extourne FAE 09/2026 | | 4 500,00 |
| 01/10/2026 | OD | 6132 | Locations immobilières | Extourne CCA loyer T4 | 4 500,00 | |
| 01/10/2026 | OD | 486 | Charges constatées d'avance | Extourne CCA loyer T4 | | 4 500,00 |
| 01/10/2026 | OD | 487 | Produits constatés d'avance | Extourne PCA désinfection T4 | 3 600,00 | |
| 01/10/2026 | OD | 706 | Prestations de services (ANT) | Extourne PCA désinfection T4 | | 3 600,00 |
| | | | | **Totaux** | **30 576,00** | **30 576,00** |

## 4. Points d'attention / pièges

- **Question 4 — pourquoi extourner** : l'extourne annule au 01/10 l'écriture d'inventaire, de sorte que la vraie facture (FNP, FAE) puisse être saisie normalement en octobre sans double comptabilisation : l'effet net sur octobre est « facture réelle − estimation », c'est-à-dire l'**écart d'estimation** seulement.
- **Ligne 6 en octobre** : l'extourne remet 4 500,00 € en charge de loyer au 01/10 ; à la clôture d'octobre, on constate une CCA de **3 000,00 €** (novembre et décembre) ; résultat : 1 500,00 € de loyer en octobre. Fin novembre : CCA 1 500,00 € ; fin décembre : plus de CCA. Même logique pour la PCA (2 400,00 € fin octobre, 1 200,00 € fin novembre). Beaucoup d'ERP gèrent cet **étalement automatiquement** à partir des dates de période saisies sur la facture.
- **Doublon FNP / facture** (ligne 1) : la règle pratique est de bâtir la liste des FNP **après** avoir saisi toutes les factures datées du mois et reçues jusqu'à J+3, et de rapprocher la liste des BR non facturés (« GR/IR » dans certains ERP) plutôt qu'une liste manuelle.
- **FAE sans accord client** : une prestation réalisée « en plus » sans BC ni accord écrit ne donne pas lieu à FAE (droit incertain) — voir E14-02.
- **Taux de TVA des déchets** : pour une collecte de DIB auprès d'une entreprise, le taux normal est retenu ici ; le taux réduit concerne le service public de gestion des déchets ménagers et assimilés (*à vérifier*).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Contrôles J+4 (question 5)** :
1. Revue analytique de l'établissement : chiffre d'affaires et principales charges de septembre vs août et vs budget ; explication de tout écart > 10 % (ici le rappel de loyer neutralisé par la CCA, la désinfection neutralisée par la PCA).
2. Rapprochement **BR non facturés** / FNP ; rapprochement **interventions réalisées non facturées** (planning) / FAE.
3. Ancienneté des FAE et FNP : une FAE de plus de 2 mois doit être facturée ou annulée.
4. Contrôle que les **extournes automatiques** sont bien programmées au 01/10.
5. Cohérence 44586 / 44587 avec les soldes 4081 / 4181 (TVA = 20 % du HT ici).
6. Dossier de clôture : une ligne par écriture avec la pièce justificative (BR, devis signé, relevé de compteur, facture de loyer).

**Message à Laure Pellegrino** : « Clôture de septembre d'Antibes : 2 FNP (1 170 € HT), 2 FAE (3 750 € HT), CCA loyer T4 (4 500 €), PCA désinfection T4 Agrodélices (3 600 €) ; impact + 3 480 € sur le résultat du mois. La facture HPD du 28/09 étant arrivée le 02/10, elle est saisie directement en septembre. Pensez à facturer Agrodélices et Pharmabel dès cette semaine. »

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce art. L. 123-21 et L. 123-22 ; PCG : principe d'indépendance des exercices, comptes 4081, 4181, 44586, 44587, 486, 487.
- CGI art. 269 (exigibilité) et 271 (déduction) : la TVA des FNP / FAE n'est ni déductible ni exigible avant la facture (et l'encaissement pour les prestations de services, sauf option).
- CGI art. 279 : taux réduit de 10 % (déchets du service public — *champ à vérifier*).
