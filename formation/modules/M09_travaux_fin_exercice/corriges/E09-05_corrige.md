# Corrigé E09-05 — Atelier Ligne : honoraires par phases, FNP et FAE au 30/09/2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-05](../exercices/E09-05_fnp-fae-atelier-ligne.md)

## 1. Analyse

| Pièce | Fait générateur | Traitement au 30/09/2026 |
|---|---|---|
| 1 — APD Dubreuil | Phase **achevée** (dossier remis le 25/09) et **validée** le 28/09. Le droit à facturer est acquis | **FAE** 15 % × 48 000 € |
| 1 — PRO Dubreuil | Phase **commencée, non achevée** : le contrat ne permet de la facturer qu'à son achèvement | **En-cours de production de services** (345), valorisé **au coût** de production. Ce n'est **pas** une FAE |
| 2 — DET Lumen septembre | Avancement de septembre, facturable mensuellement → droit acquis au 30/09 | **FAE** 3 900 € HT |
| 3 — DCE Lumen | Facturée le 20/09, phase non commencée | **PCA** 4 800 € |
| 4 — BET Calcul+ | Note de calcul livrée le 21/09 (service fait) | **FNP** 4 500 € HT |
| 5 — Assurance | Cotisation assise sur les honoraires de l'exercice clos : la charge appartient à l'exercice | **FNP** (charge à payer) 1 850 €, sans TVA |
| 6 — Note de frais | Déplacements de septembre | **Charge à payer** 312 € (TVA non récupérable) |
| 7 — Licence CAO | Période 01/10/2026 – 30/09/2027 | **Rien** (exercice suivant) |
| 8 — Brotteaux | Créance née sur l'exercice, contestée, perte probable de 50 % | **Créance douteuse + dépréciation** (ou avoir à établir, voir ci-dessous) |

**Réponse à la proposition de Camille (le PRO) :** enregistrer 40 % du PRO en FAE reviendrait à constater un **produit non acquis**. Le contrat ne donne droit à facturation qu'à l'achèvement de la phase, et le client n'a rien validé. Le travail déjà réalisé a pourtant une valeur : on le constate en **en-cours de production**, **au coût de revient** (heures × coût horaire de production), sans marge, et non au prix de vente. Deux réserves sur les chiffres de Camille :
- un avancement de 40 % en 1 jour (PRO commencé le 29/09) n'est crédible que parce que la phase a été préparée en parallèle de l'APD. On retient les **62 heures réellement pointées**, qui sont objectives, plutôt que le pourcentage déclaré ;
- test de valeur : le coût de l'en-cours ne doit pas dépasser ce qui sera facturé. Le PRO vaut 20 % × 48 000 = 9 600 € HT ; à 40 %, cela représente 3 840 € HT, supérieur au coût de 3 596 €. Aucune dépréciation n'est nécessaire.

**TVA sur encaissements :**
- **FAE** : la TVA n'est ni exigible ni facturée. Elle est portée en 44587 *TVA sur factures à établir*. Quand la facture sera émise mais non payée, elle passera en TVA collectée **en attente d'encaissement** (sous-compte 4457x), et ne deviendra exigible qu'au paiement.
- **FNP** du BET (prestataire sur encaissements) : 44586, puis TVA déductible **lors du paiement** au fournisseur.

**Brotteaux — dépréciation ou avoir à établir ?**
- Si la remise est **décidée ou acceptée avant la clôture**, ou si elle constitue une **obligation**, c'est une **réduction de prix** : **avoir à établir** de 3 000 € HT + 600 € de TVA.
- Ici, à la clôture, rien n'est décidé : la remise est une **hypothèse de négociation** (« probablement »). La créance existe en totalité, mais son recouvrement est **incertain pour moitié**. On reclasse donc la créance en **clients douteux (416)** et on la **déprécie à 50 % du HT** (la TVA ne sera reversée que sur ce qui sera encaissé, puisque l'entreprise est sur encaissements).
- Si la remise est formalisée **après la clôture mais avant l'arrêté**, en conséquence du litige né avant la clôture, l'événement est **ajustant** : on peut alors passer directement l'avoir à établir.

## 2. Calculs

| Élément | Calcul | HT | TVA | TTC |
|---|---|---|---|---|
| FAE APD Dubreuil | 48 000 × 15 % | 7 200,00 € | 1 440,00 € | 8 640,00 € |
| FAE DET Lumen | situation n° 7 | 3 900,00 € | 780,00 € | 4 680,00 € |
| **Total FAE** | | **11 100,00 €** | **2 220,00 €** | **13 320,00 €** |
| En-cours PRO | 62 h × 58 € | 3 596,00 € | — | — |
| PCA DCE Lumen | 100 % | 4 800,00 € | — | — |
| FNP BET | | 4 500,00 € | 900,00 € | 5 400,00 € |
| FNP assurance | | 1 850,00 € | — | 1 850,00 € |
| Note de frais | | 312,00 € | — | 312,00 € |
| Dépréciation Brotteaux | 6 000 × 50 % | 3 000,00 € | — | — |

**Impact sur le résultat :**
+ 11 100 (FAE) + 3 596 (en-cours) – 4 800 (PCA) – 4 500 (BET) – 1 850 (assurance) – 312 (frais) – 3 000 (dépréciation) = **+ 234,00 €**.

Avec la proposition de Camille (PRO en FAE au prix de vente : 3 840 € au lieu de 3 596 € en en-cours), le résultat aurait été surévalué de 244 € seulement. L'écart est faible, mais le principe est essentiel : avec plusieurs projets, l'erreur se démultiplie, et une FAE sans droit à facturer est une **créance fictive**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 4181 | Clients – factures à établir | FAE APD Dubreuil 15 % | 8 640,00 | |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | FAE DET Lumen sept. | 4 680,00 | |
| 30/09/2026 | OD | 706 | Prestations de services | FAE APD Dubreuil + DET Lumen | | 11 100,00 |
| 30/09/2026 | OD | 44587 | TVA sur factures à établir | FAE APD Dubreuil + DET Lumen | | 2 220,00 |
| 30/09/2026 | OD | 345 | En-cours de production de services | En-cours PRO Dubreuil 62 h × 58 € | 3 596,00 | |
| 30/09/2026 | OD | 7134 | Variation des en-cours de production de services | En-cours PRO Dubreuil | | 3 596,00 |
| 30/09/2026 | OD | 706 | Prestations de services | PCA DCE Lumen (non commencée) | 4 800,00 | |
| 30/09/2026 | OD | 487 | Produits constatés d'avance | PCA DCE Lumen | | 4 800,00 |
| 30/09/2026 | OD | 604 | Achats d'études et prestations de services | FNP BET Calcul+ Dubreuil | 4 500,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP BET Calcul+ | 900,00 | |
| 30/09/2026 | OD | 4081 | Fournisseurs – factures non parvenues | FNP BET Calcul+ | | 5 400,00 |
| 30/09/2026 | OD | 616 | Primes d'assurance | Régularisation RC décennale 2025-26 | 1 850,00 | |
| 30/09/2026 | OD | 4081 | Fournisseurs – factures non parvenues | Régularisation RC décennale | | 1 850,00 |
| 30/09/2026 | OD | 6251 | Voyages et déplacements | Note de frais C. Fabre septembre | 312,00 | |
| 30/09/2026 | OD | 4686 | Divers – charges à payer | Note de frais C. Fabre | | 312,00 |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Reclassement SCI des Brotteaux | 7 200,00 | |
| 30/09/2026 | OD | 411 | Clients | Reclassement SCI des Brotteaux | | 7 200,00 |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation Brotteaux 50 % HT | 3 000,00 | |
| 30/09/2026 | OD | 491 | Dépréciations des comptes de clients | Dépréciation Brotteaux | | 3 000,00 |
| | | | | **Totaux** | **39 478,00** | **39 478,00** |

**Au 01/10/2026** : extourne des FAE, du PCA, des FNP et de la note de frais (ou solde du 4686 au remboursement). L'**en-cours** n'est pas extourné ligne à ligne : il sera soldé par la variation d'en-cours de l'exercice suivant (stock initial).

## 4. Points d'attention / pièges

- **FAE = droit à facturer acquis à la clôture.** Une phase non achevée n'est pas une FAE ; c'est un en-cours **au coût**, sans marge et hors frais commerciaux et administratifs généraux.
- **Facturer d'avance n'acquiert pas le produit** : la note DCE émise pour « le budget du client » est neutralisée en PCA. Avec la TVA sur encaissements, si le client la paie avant la réalisation, la TVA est due à l'encaissement, même si le produit reste en PCA.
- **FNP assurance** : pas de TVA (opération d'assurance exonérée), mais une taxe sur les conventions incluse dans le coût.
- **Note de frais** : pas de récupération de la TVA sur le transport de voyageurs (exclusion du droit à déduction).
- **Licence CAO** : rien au 30/09. Attention, elle sera **autoliquidée** sur la CA3 d'octobre (fournisseur hors de France).
- **Ne pas déprécier le TTC** : avec la TVA sur encaissements, la TVA de la créance Brotteaux n'a même pas encore été reversée.
- **Dépréciation fiscalement déductible** si la perte est probable et chiffrée à partir d'éléments précis (lettre de contestation, analyse des cogérants documentée).

## 5. Ce qu'un senior ferait en plus

- **Tableau de suivi des missions** (projet, honoraires, phases, % facturé, % réalisé, heures, coût) à tenir par Atelier Ligne et à joindre au dossier chaque année. Il sert à la fois aux FAE, aux en-cours, aux PCA et au pilotage de la rentabilité par projet.
- **Contrôle d'achèvement** : exiger une preuve de remise et de validation de chaque phase comptée en FAE (courriel du client, PV, visa).
- **Pertes à terminaison** : vérifier pour chaque projet que le coût total estimé ne dépasse pas les honoraires (sinon, provision 1517).
- **Conseil** : proposer une **clause de facturation intermédiaire** (acomptes mensuels par phase) dans les futurs contrats. Elle réduit le BFR et sécurise le chiffre d'affaires de fin d'exercice.

**Réponse à Camille :**
> « Bonjour Camille, l'APD Dubreuil (7 200 € HT) et la situation DET Lumen de septembre (3 900 € HT) sont bien rattachés à l'exercice en "factures à établir". Pour le PRO, le contrat ne vous permet de facturer qu'à l'achèvement : nous valorisons donc les 62 heures déjà passées au coût (3 596 €) en "travaux en cours". Le résultat en tient compte, sans anticiper une facture que le client n'a pas encore validée. Pour la SCI des Brotteaux, nous déprécions 50 % de la note ; si vous formalisez la remise avant l'arrêté des comptes, nous la passerons en avoir. »

## 6. Références

- CGI, art. 38, 2 bis (prestations de services : rattachement à l'achèvement, ou au fur et à mesure pour les prestations continues ou discontinues à échéances successives) ; art. 269, 2-c (TVA à l'encaissement) ; art. 39, 1-5° (dépréciations).
- PCG : comptes 345 « En-cours de production de services », 7134, 4181, 487, 416, 491 ; coût de production des en-cours (charges directes et indirectes de production, hors frais administratifs généraux et commerciaux).
- Code de commerce, art. L. 123-21.
