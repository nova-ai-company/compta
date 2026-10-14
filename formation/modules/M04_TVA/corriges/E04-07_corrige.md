# Corrigé E04-07 — TVA sur les encaissements : le cabinet d'architectes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-07](../exercices/E04-07_tva-encaissements-architecte.md)

## 1. Analyse

**a) L'erreur de la stagiaire.** Pour les **prestations de services**, la TVA est exigible **lors de l'encaissement** du prix, des acomptes ou du solde (art. 269-2-c CGI), sauf option pour les débits. La TVA à déclarer en septembre est donc celle **contenue dans les encaissements de septembre**, quelle que soit la date des factures. La stagiaire a déclaré la TVA des **factures émises** (méthode « débits ») : elle a déclaré trop sur certaines factures (F-110 et F-118, non payées) et pas assez sur d'autres (paiements de factures antérieures).

**b) L'acompte sans facture.** L'encaissement d'un acompte sur une prestation de services rend la TVA **exigible immédiatement** : 2 400 × 20/120 = 400 € à déclarer en septembre, **facture ou pas**. Entre professionnels, une **facture d'acompte** est obligatoire dès l'encaissement (art. 289 CGI) : elle doit être émise maintenant (et non avec la facture de phase). Comptablement : 4191 (avance reçue) pour le HT et 44571 pour la TVA.

**c) Le contrôle du 44574.** Dans un système « encaissements », le compte de TVA en attente doit toujours correspondre à la **TVA incluse dans les créances clients non encaissées** (411, hors acomptes et hors clients exonérés). Ce rapprochement mensuel détecte les erreurs de saisie — ici, un **avoir comptabilisé TTC en 706**, sans extourner la TVA en attente : le 706 est trop diminué de 400 € et le 44574 surévalué de 400 €. Si l'erreur n'est pas corrigée, la TVA de 400 € sera un jour « libérée » et déclarée alors qu'elle n'est pas due.

## 2. Calculs

**TVA collectée exigible en septembre (encaissements)**

| Date | Encaissement | TTC | TVA (× 20/120) |
|---|---|---|---|
| 05/09 | F-2026-101 (50 %) | 6 000,00 | 1 000,00 |
| 14/09 | F-2026-074 | 9 600,00 | 1 600,00 |
| 22/09 | F-2026-105 | 7 200,00 | 1 200,00 |
| 25/09 | Acompte Clinique vétérinaire | 2 400,00 | 400,00 |
| 28/09 | F-2026-112 | 18 000,00 | 3 000,00 |
| **Total** | | **43 200,00** | **7 200,00** |

Base HT : 36 000 €. **TVA exigible : 7 200 €** (et non 4 256 € : 25 536 € TTC de factures émises × 20/120).

**Reconstitution du 411 au 30/09/2026**

| Facture | Montant dû TTC | TVA incluse |
|---|---|---|
| F-2026-101 (solde 50 %) | 6 000,00 | 1 000,00 |
| F-2026-089 (6 000 – avoir 2 400) | 3 600,00 | 600,00 |
| F-2026-110 | 4 800,00 | 800,00 |
| F-2026-118 | 2 736,00 | 456,00 |
| **Total** | **17 136,00** | **2 856,00** |

Contrôle par les mouvements : 34 800 + 4 800 + 18 000 + 2 736 – 2 400 – 40 800 (encaissements sur factures) = 17 136 € ✔.

**Rapprochement du 44574**

| | Montant |
|---|---|
| Solde au 31/08 (= 34 800 / 6) | 5 800,00 |
| + TVA des factures de septembre (800 + 3 000 + 456) | 4 256,00 |
| – TVA libérée sur encaissements de factures (40 800 / 6) | – 6 800,00 |
| **= Solde comptable au 30/09 (avant correction)** | **3 256,00** |
| TVA théorique en attente (créances au 30/09) | 2 856,00 |
| **Écart** | **400,00** = TVA de l'avoir AV-2026-006 (2 400 / 6) |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/09/2026 | VT | 411PHC | Client Pharma Concept | F-2026-110 | 4 800,00 | |
| 02/09/2026 | VT | 706 | Prestations de services | F-2026-110 | | 4 000,00 |
| 02/09/2026 | VT | 44574 | TVA collectée en attente | F-2026-110 | | 800,00 |
| 10/09/2026 | VT | 411PRS | Client Promo Saône | F-2026-112 | 18 000,00 | |
| 10/09/2026 | VT | 706 | Prestations de services | F-2026-112 | | 15 000,00 |
| 10/09/2026 | VT | 44574 | TVA collectée en attente | F-2026-112 | | 3 000,00 |
| 09/2026 | BQ | 512 | Banque | Encaissements clients de septembre | 43 200,00 | |
| 09/2026 | BQ | 411 | Clients (F-101, F-074, F-105, F-112) | Encaissements de factures | | 40 800,00 |
| 25/09/2026 | BQ | 4191 | Clients – avances et acomptes reçus | Acompte Clinique vétérinaire du Parc (facture d'acompte à émettre) | | 2 000,00 |
| 25/09/2026 | BQ | 44571 | TVA collectée | TVA exigible sur acompte | | 400,00 |
| 30/09/2026 | OD | 44574 | TVA collectée en attente | TVA exigible sur encaissements de septembre (40 800 / 6) | 6 800,00 | |
| 30/09/2026 | OD | 44571 | TVA collectée | TVA exigible sur encaissements de septembre | | 6 800,00 |
| 30/09/2026 | OD | 44574 | TVA collectée en attente | Correction avoir AV-2026-006 comptabilisé TTC | 400,00 | |
| 30/09/2026 | OD | 706 | Prestations de services | Correction avoir AV-2026-006 | | 400,00 |
| | | | | **Totaux** | **73 200,00** | **73 200,00** |

Après correction : 44574 = 3 256 – 400 = **2 856 €** = TVA théorique ✔. 44571 du mois = 400 + 6 800 = **7 200 €** ✔.

**CA3 de septembre — partie TVA collectée**

| Ligne | Montant |
|---|---|
| A1 — Ventes, prestations de services (base HT encaissée) | 36 000 |
| 08 — Taux normal 20 % : base / taxe | 36 000 / 7 200,00 |
| 16 — Total TVA brute | 7 200,00 |

## 4. Points d'attention / pièges

- **Clôture du 30/09** : au bilan, le 44574 (2 856 €) figure en dettes fiscales (TVA due dès l'encaissement des créances). Il ne faut pas le solder.
- **Avoirs** sur prestations non encaissées : ils diminuent le 44574 (pas le 44571), puisque la TVA n'avait pas été déclarée.
- **Avoir sur une facture partiellement payée** : vérifier si la TVA de la partie payée a déjà été déclarée (et, si l'avoir porte sur la part payée, régulariser le 44571).
- **Client public (Chorus Pro)** : le paiement arrive de la DRFiP, pas de la commune : bien identifier la facture pour le lettrage.
- **Facture d'acompte** obligatoire entre professionnels dès l'encaissement, avec les mentions habituelles.
- **E-reporting 2027** : pour les prestations de services, Atelier Ligne devra transmettre les **données de paiement** (date, montant encaissé) : le relevé des encaissements devient une obligation déclarative.

## 5. Ce qu'un senior ferait en plus

**Avis sur l'option pour les débits (pour Nicolas Brun et Camille Fabre) :**

| | TVA sur les encaissements (actuel) | Option pour les débits |
|---|---|---|
| Fait déclencheur | Encaissement | Facturation |
| Trésorerie | La TVA n'est reversée qu'une fois encaissée | La TVA est avancée à l'État avant d'être encaissée (délais de paiement des clients : 30 à 60 jours, voire plus pour les collectivités) |
| Gestion | Suivi des encaissements et du 44574 ; relevé mensuel des encaissements | Plus simple : TVA = journal des ventes |
| Impayés | Pas de TVA à récupérer (jamais versée) | TVA à récupérer, avec formalités (facture rectificative, irrécouvrabilité) |
| Clients | Les clients professionnels déduisent la TVA au paiement de la facture | Les clients peuvent déduire la TVA dès réception de la facture (avantage pour eux) |
| Formalités | — | Option à formuler auprès du SIE ; **mention obligatoire « Option pour le paiement de la taxe d'après les débits »** sur les factures |

**Recommandation** : pour un cabinet d'architectes qui facture par phases, avec des clients publics et privés aux délais de paiement longs et des honoraires parfois contestés, **le maintien de la TVA sur les encaissements est préférable** (trésorerie, impayés). La simplification attendue sera obtenue autrement : rapprochement mensuel automatisé encaissements / 44574 et lettrage systématique (indispensable de toute façon pour l'e-reporting 2027).

**Mail à Hélène** : « CA3 de septembre corrigée : TVA collectée 7 200 € au lieu de 4 256 €, écart de 2 944 € qui aurait été déclaré en moins ; avoir mal comptabilisé corrigé (400 €) ; facture d'acompte à émettre pour la Clinique vétérinaire. Avis sur l'option débits joint. »

## 6. Références

- CGI : art. 269-2-c (exigibilité des prestations de services, option pour les débits), art. 289 (factures et factures d'acompte), art. 242 nonies A ann. II (mention de l'option pour les débits).
- BOFiP : TVA-BASE-20 (fait générateur et exigibilité).
- PCG : comptes 4191, 44571, 44574 (subdivision usuelle pour la TVA en attente).
