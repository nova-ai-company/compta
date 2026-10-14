# Corrigé E14-01 — Facture mensuelle forfaitaire multi-sites (Riviera Mall) : TVA sur les encaissements ou option pour les débits ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-01](../exercices/E14-01_facture-forfait-multisites-riviera-mall.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Contrôle du brouillon
**Calculs.** Total HT = 18 450,00 + 1 240,00 + 12 300,00 + 9 870,00 = **41 860,00 €** ✓ (et la vitrerie est bien due : septembre est un mois de passage trimestriel). TVA 20 % = 41 860,00 × 20 % = **8 372,00 €** et non 8 327,00 € (inversion de chiffres) ; TTC = **50 232,00 €** et non 50 187,00 €. Une erreur de 45,00 € sur la TVA ne se corrige pas à la main : il faut comprendre d'où elle vient (montant saisi en dur dans le modèle ? arrondi par ligne mal paramétré ?) et régénérer la facture.

**Mentions.** Sont présentes : numéro unique et chronologique, date d'émission, identité complète du vendeur (dénomination, forme, capital, adresse, RCS, SIREN, n° TVA), identité du client et son **SIREN** (mention 2026), son n° de TVA, **nature de l'opération** (« prestation de services », mention 2026), désignation, quantités, PU HT, taux et montant de TVA, date d'échéance, pénalités de retard, indemnité forfaitaire de 40 €, conditions d'escompte.
À corriger ou compléter :
- **Adresse de réalisation de la prestation** : la facture est adressée au siège administratif de Riviera Mall, mais les prestations sont réalisées dans trois centres. Depuis 2026, l'**adresse de livraison / de réalisation**, lorsqu'elle diffère de l'adresse du client, est une mention obligatoire : le libellé « Riviera Mall Nice-Ouest » ne suffit pas, il faut l'adresse postale complète de chaque site.
- **Mention « TVA acquittée d'après les débits »** : à **supprimer**, puisqu'aucune option n'a été formulée (question 2).
- **Montant de TVA et TTC** : à recalculer.
- Bonne pratique (et souvent exigé par les grands clients) : la référence du bon de commande ou du contrat (présente : RM-2024-017).

### Question 2 — Exigibilité de la TVA
Les prestations de nettoyage sont des **prestations de services** : la TVA devient exigible lors de l'**encaissement** du prix (acomptes compris), sauf si le prestataire a **opté pour le paiement de la TVA d'après les débits** (CGI art. 269-2-c). Tant qu'aucune option n'existe, GSF Riviera déclare la TVA **au fur et à mesure des encaissements** : la TVA facturée attend dans un compte de TVA collectée « en attente » (44574) et n'est virée en 44571 qu'à l'encaissement.

Si la mention « TVA acquittée d'après les débits » est maintenue sans option réelle :
- **chez le client**, Riviera Mall est fondé à déduire la TVA dès la réception de la facture (la mention lui indique que la TVA est exigible chez le prestataire dès la facturation) ;
- **chez GSF Riviera**, l'incohérence entre la facture et le régime déclaré expose à un rappel : l'administration peut considérer que la TVA mentionnée est due dès la facturation. On crée un décalage de trésorerie et un risque de redressement pour rien.
- en **e-reporting** 2026, les prestations de services dont la TVA est exigible à l'encaissement obligent le prestataire à transmettre les **données de paiement** (encaissements) ; une mention erronée rend les flux incohérents.

Conclusion : l'ERP doit être paramétré **société par société** (certaines filiales du groupe peuvent avoir opté, d'autres non) ; on corrige le modèle de facture et on vérifie les factures déjà émises depuis le 01/09/2026 avec ce modèle.

### Question 3 — Écritures
- Facture de septembre : TVA en **44574** (en attente).
- Encaissement de la facture d'août le 22/09 : la TVA d'août (8 124,00 €) devient exigible → virement 44574 → 44571 **en septembre**.
- Encaissement partiel du 15/10 : 25 000,00 € TTC, dont TVA 25 000,00 × 20/120 = 4 166,67 € exigible **en octobre**.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| HT septembre | 18 450,00 + 1 240,00 + 12 300,00 + 9 870,00 | 41 860,00 € |
| dont Nice (NIC) | 18 450,00 + 1 240,00 | 19 690,00 € |
| TVA septembre | 41 860,00 × 20 % | 8 372,00 € |
| TTC septembre | 41 860,00 + 8 372,00 | 50 232,00 € |
| Erreur du brouillon | 8 372,00 − 8 327,00 | 45,00 € |
| TVA d'août exigible en septembre | 48 744,00 × 20/120 | 8 124,00 € |
| Encaissement du 15/10 : HT | 25 000,00 / 1,20 | 20 833,33 € |
| Encaissement du 15/10 : TVA | 25 000,00 − 20 833,33 | 4 166,67 € |
| Solde client après le 15/10 | 50 232,00 − 25 000,00 | 25 232,00 € |
| Solde 44574 (facture sept.) après le 15/10 | 8 372,00 − 4 166,67 | 4 205,33 € |

**CA3 de septembre (question 4)** — pour ce client : ligne des opérations imposables au taux normal 20 % (ligne « 08 » du 3310-CA3, *numérotation à vérifier sur le formulaire en vigueur*) : base **40 620,00 €**, TVA **8 124,00 €** (encaissement du 22/09 de la facture d'août). La facture de septembre n'y figure pas.
**CA3 d'octobre** : base **20 833,33 €**, TVA **4 166,67 €**.

**Avec option pour les débits (question 5)** : la TVA de la facture de septembre (8 372,00 €) serait exigible dès la facture → déclarée sur la CA3 de **septembre** : base 41 860,00 €, TVA 8 372,00 €. La facture d'août aurait été déclarée sur la CA3 d'**août**. Les encaissements ne génèreraient plus aucune écriture de TVA.

## 3. Écritures comptables

**Régime applicable (sans option) — septembre et octobre**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 22/09/2026 | BQ | 512 | Banque | Vir. Riviera Mall F FR-2026-08-0412 | 48 744,00 | |
| 22/09/2026 | BQ | 411RIVM | Client Riviera Mall | Vir. Riviera Mall F FR-2026-08-0412 | | 48 744,00 |
| 22/09/2026 | OD | 44574 | TVA collectée en attente d'encaissement | TVA exigible encaiss. F FR-2026-08-0412 | 8 124,00 | |
| 22/09/2026 | OD | 44571 | TVA collectée | TVA exigible encaiss. F FR-2026-08-0412 | | 8 124,00 |
| 30/09/2026 | VT | 411RIVM | Client Riviera Mall | F FR-2026-09-0457 Riviera Mall sept. | 50 232,00 | |
| 30/09/2026 | VT | 706 | Prestations de services (NIC) | F FR-2026-09-0457 forfait + vitrerie Nice-Ouest | | 19 690,00 |
| 30/09/2026 | VT | 706 | Prestations de services (ANT) | F FR-2026-09-0457 forfait Antibes-Les Pins | | 12 300,00 |
| 30/09/2026 | VT | 706 | Prestations de services (CAN) | F FR-2026-09-0457 forfait Cannes-La Bocca | | 9 870,00 |
| 30/09/2026 | VT | 44574 | TVA collectée en attente d'encaissement | F FR-2026-09-0457 TVA 20 % | | 8 372,00 |
| 15/10/2026 | BQ | 512 | Banque | Vir. Riviera Mall acompte F FR-2026-09-0457 | 25 000,00 | |
| 15/10/2026 | BQ | 411RIVM | Client Riviera Mall | Vir. Riviera Mall acompte F FR-2026-09-0457 | | 25 000,00 |
| 15/10/2026 | OD | 44574 | TVA collectée en attente d'encaissement | TVA exigible encaiss. partiel F FR-2026-09-0457 | 4 166,67 | |
| 15/10/2026 | OD | 44571 | TVA collectée | TVA exigible encaiss. partiel F FR-2026-09-0457 | | 4 166,67 |
| | | | | **Totaux** | **136 266,67** | **136 266,67** |

> En pratique, l'ERP génère automatiquement l'écriture 44574 → 44571 au lettrage de l'encaissement : votre contrôle consiste à vérifier, à chaque clôture, que **le solde de 44574 = TVA contenue dans les factures non encaissées** (balance âgée clients × 20/120).

**Hypothèse de l'option pour les débits (question 5) — facture de septembre**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | VT | 411RIVM | Client Riviera Mall | F FR-2026-09-0457 Riviera Mall sept. | 50 232,00 | |
| 30/09/2026 | VT | 706 | Prestations de services | F FR-2026-09-0457 (3 sites) | | 41 860,00 |
| 30/09/2026 | VT | 44571 | TVA collectée | F FR-2026-09-0457 TVA 20 % (option débits) | | 8 372,00 |
| | | | | **Totaux** | **50 232,00** | **50 232,00** |

## 4. Points d'attention / pièges

- **Un encaissement partiel non affecté** (« acompte sur facture septembre ») rend exigible la TVA **au prorata** de la somme encaissée : on ne l'ignore pas sous prétexte que la facture n'est pas soldée.
- **Le 44574 n'est pas un compte « fourre-tout »** : un solde qui ne correspond pas aux créances ouvertes signale des encaissements non lettrés, des avoirs mal imputés ou des factures soldées sans virement de TVA.
- **Le régime se choisit par société** : dans un groupe de 29 filiales, une filiale peut avoir opté et l'autre non. Le paramétrage ERP doit suivre le SIREN émetteur.
- **L'option pour les débits** est une décision de gestion (elle avance l'exigibilité donc la trésorerie de TVA) prise par la direction financière : l'aide-comptable signale l'incohérence, elle ne « choisit » pas le régime.
- **Mentions 2026** : une facture électronique incomplète peut être rejetée par la PA ; la sanction de l'omission d'une mention est une amende par mention manquante (CGI art. 1737, *montants à vérifier*).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à Sophie Garnier :**
> Bonjour Sophie,
> Le brouillon FR-2026-09-0457 Riviera Mall est bloqué avant envoi PA : (1) TVA erronée (8 327,00 au lieu de 8 372,00 € ; TTC 50 232,00 €) ; (2) adresses complètes des trois sites à ajouter (mention adresse de livraison 2026) ; (3) mention « TVA d'après les débits » à retirer, GSF Riviera n'ayant pas opté. Je propose de faire corriger le modèle par l'équipe ERP pour toutes les filiales concernées et de lister les factures émises depuis le 01/09 avec cette mention : si certaines sont déjà parties, il faudra émettre un avoir et une facture rectificative. Pour la CA3 de septembre, Riviera Mall représente 40 620,00 € HT / 8 124,00 € de TVA collectée (encaissement d'août).

**Réponse d'entretien (question 6)**, en 4 phrases : « Pour une prestation de services, la TVA est due à l'encaissement, sauf option pour les débits, auquel cas elle est due dès la facture. En propreté, presque tout le chiffre d'affaires est de la prestation de services, donc l'impact trésorerie est important : sur les encaissements, on ne reverse la TVA qu'une fois payés, ce qui protège des retards de paiement, notamment des clients publics. Comptablement, cela implique un compte de TVA collectée en attente, à rapprocher chaque mois des créances ouvertes. Et depuis 2026, ce choix a aussi un impact sur la facture électronique : la mention de l'option est obligatoire et, sans option, il faut transmettre les données d'encaissement en e-reporting. »

**Contrôle de clôture** : tableau « 44574 vs balance âgée clients » par société, signé chaque mois.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 269-2-c : exigibilité de la TVA à l'encaissement pour les prestations de services ; option pour les débits.
- CGI art. 242 nonies A de l'annexe II et CGI art. 289 : mentions obligatoires des factures ; réforme de la facturation électronique (nouvelles mentions applicables en 2026).
- CGI art. 1737 : amende pour omission ou inexactitude de mentions sur facture.
- Code de commerce art. L. 441-9 et L. 441-10 : mentions de la facture, pénalités de retard et indemnité forfaitaire de 40 €.
- BOFiP : TVA – Base d'imposition et exigibilité des prestations de services (BOI-TVA-BASE-20, *référence à vérifier*).
