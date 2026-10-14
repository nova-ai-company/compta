# Corrigé E14-05 — Rapprochement commande / réception / facture (3-way match) : six factures fournisseurs à traiter

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-05](../exercices/E14-05_3-way-match-six-factures.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Le 3-way match répond à trois questions : **a-t-on commandé ?** (BC), **a-t-on reçu ?** (BR / service fait), **nous facture-t-on ce qui a été commandé et reçu, au bon prix ?** (facture). On commence toujours par **éliminer les doublons**, puis on rapproche ligne à ligne.

### Doublon d'abord : le document F
Le PDF F26-7781 reçu par mail est la **copie** de la facture A reçue via la PA (même fournisseur, même numéro, même date, même montant). Depuis le 01/09/2026, la facture originale est le flux électronique reçu via la PA ; le PDF n'a aucune valeur de facture. **On ne le saisit pas** : on le classe avec la mention « copie – original reçu via PA, saisi le 05/10 » et on répond à l'assistante. Un contrôle « même SIREN fournisseur + même numéro de facture » doit être bloquant dans l'ERP.

### Rapprochement document par document

| Doc | BC | BR | Facture | Écart | Décision | Statut via PA | Action / qui lève le blocage |
|---|---|---|---|---|---|---|---|
| A | BC-2026-0911 : 1 112,00 HT | 40 + 30 reçus | 1 112,00 HT | aucun | **Bon à payer** | Approuvée (statut facultatif) | Paiement au run de jeudi si échéance atteinte |
| B | BC-2026-0915 : 765,00 HT | gants : 40 / 50 | 50 gants facturés | 10 × 6,90 = **69,00 € HT** (9,0 % de la facture ; > 20 €) | **Bloquée** | En litige (ou Suspendue) | Achats : relancer le reliquat. Si livré (BR complémentaire) → déblocage ; sinon avoir de 69,00 € HT (82,80 € TTC) |
| C | 20 × 9,80 = 196,00 HT | 20 reçus | 20 × 10,60 = 212,00 HT | prix : 0,80 × 20 = **16,00 € HT** (8,2 % > 1 %) | **Bloquée** | En litige | Acheteuse : soit le tarif BC s'applique → avoir de 16,00 € HT (19,20 € TTC), soit hausse tarifaire acceptée → BC modifié et déblocage |
| D | **aucun BC** | BL signé (BR-NIC-2026-0627) | 236,00 HT | facture sans commande | **Bloquée (suspendue)** | Suspendue | Chef d'établissement / acheteuse : créer un BC de régularisation, valider la dépense ; puis bon à payer |
| E | contrat : 3 × 165,00 = 495,00 HT | période T4 (service à venir) | TVA 10 % = 49,50 € | **taux de TVA erroné** (maintenance = 20 %, soit 99,00 €) | **Refusée** | Refusée (motif : taux de TVA erroné) | Fournisseur : émettre une nouvelle facture à 20 % (TTC 594,00 €) |
| F | — | — | copie PDF de A | doublon | **Non saisie** | — | Classement ; message à l'établissement |

**Pourquoi refuser E plutôt que la comptabiliser ?** GSF Riviera ne peut déduire que la TVA **régulièrement facturée** ; la prestation de maintenance relève du taux normal de 20 %. Laisser une facture à 10 % crée une anomalie chez les deux parties (le fournisseur collecte trop peu, et la facture rectificative ultérieure changera le TTC). La facture est fausse dans un élément essentiel : refus et demande d'une facture conforme (le fournisseur annule de son côté).

**Pourquoi comptabiliser B, C et D malgré le blocage ?** Ce sont des factures recevables portant sur des biens livrés (en tout ou partie) : la dette existe pour l'essentiel. Le blocage porte sur le **paiement**, pas sur l'enregistrement. Cela garantit l'exhaustivité des dettes à la clôture et le suivi des litiges dans la balance fournisseurs.

**D : facture sans commande.** La dépense est réelle (brosses livrées et utilisées), mais elle contourne la procédure d'engagement : on ne paie pas sans **validation a posteriori** par la personne habilitée. C'est aussi un point de vigilance « fraude » : une facture sans BC d'un fournisseur connu est banale, d'un fournisseur inconnu elle est suspecte.

## 2. Calculs (détaillés, chaque montant justifié)

| Doc | HT | TVA | TTC | Contrôle |
|---|---|---|---|---|
| A | 40 × 18,50 = 740,00 + 30 × 12,40 = 372,00 → 1 112,00 | 222,40 | 1 334,40 | conforme |
| B | 100 × 4,20 = 420,00 + 50 × 6,90 = 345,00 → 765,00 | 153,00 | 918,00 | écart 10 × 6,90 = 69,00 HT ; avoir éventuel 82,80 TTC |
| C | 20 × 10,60 = 212,00 | 42,40 | 254,40 | BC : 196,00 ; écart 16,00 HT = 8,16 % ; avoir éventuel 19,20 TTC |
| D | 236,00 | 47,20 | 283,20 | sans BC |
| E | 3 × 165,00 = 495,00 | facturé 49,50 au lieu de 99,00 | facturé 544,50 au lieu de 594,00 | refusée |

Total comptabilisé (A + B + C + D) : HT 2 325,00 € ; TVA 465,00 € ; TTC **2 790,00 €**.
Bon à payer jeudi : **1 334,40 €** (A seule, sous réserve de l'échéance : à 45 jours fin de mois, une facture du 23/09 est échue le 15/11 — le run de jeudi ne la paiera que si la politique du groupe est de payer à réception validée, ce qui est rare ; à défaut elle est « bon à payer, en attente d'échéance »).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | HPD F26-7781 BC-2026-0911 (NIC) | 1 112,00 | |
| 05/10/2026 | AC | 44566 | TVA déductible sur ABS | HPD F26-7781 TVA 20 % | 222,40 | |
| 05/10/2026 | AC | 401HPD | Fournisseur Hygiène Pro Distribution | HPD F26-7781 – BAP | | 1 334,40 |
| 05/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | HPD F26-7795 BC-2026-0915 (NIC) | 765,00 | |
| 05/10/2026 | AC | 44566 | TVA déductible sur ABS | HPD F26-7795 TVA 20 % | 153,00 | |
| 05/10/2026 | AC | 401HPD | Fournisseur Hygiène Pro Distribution | HPD F26-7795 – BLOQUÉE litige quantité gants | | 918,00 |
| 05/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | HPD F26-7802 BC-2026-0920 (NIC) | 212,00 | |
| 05/10/2026 | AC | 44566 | TVA déductible sur ABS | HPD F26-7802 TVA 20 % | 42,40 | |
| 05/10/2026 | AC | 401HPD | Fournisseur Hygiène Pro Distribution | HPD F26-7802 – BLOQUÉE litige prix | | 254,40 |
| 05/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | MNE MN-4410 brosses autolaveuse (NIC) sans BC | 236,00 | |
| 05/10/2026 | AC | 44566 | TVA déductible sur ABS | MNE MN-4410 TVA 20 % | 47,20 | |
| 05/10/2026 | AC | 401MNE | Fournisseur Machines Nett' | MNE MN-4410 – SUSPENDUE attente BC régul. | | 283,20 |
| | | | | **Totaux** | **2 790,00** | **2 790,00** |

> La date comptable retenue est celle de la facture (septembre pour A à D) si la période de septembre est encore ouverte au 05/10 (J+3) ; sinon, au minimum, les factures A à D doivent figurer dans les **charges à payer** de septembre, les biens ayant été reçus en septembre.

## 4. Points d'attention / pièges

- **Question 4 — facture E rectifiée (T4)** : enregistrée en octobre pour 495,00 € HT (6156) + 99,00 € de TVA. Elle couvre octobre à décembre : à la clôture mensuelle d'octobre, on ne garde en charge que 165,00 € et on constate **330,00 € de charges constatées d'avance** (486) ; fin novembre, 165,00 € ; fin décembre, 0. Beaucoup de groupes paramètrent un **étalement automatique** des factures périodiques dans l'ERP.
- **Avoir attendu ≠ avoir reçu** : ne jamais saisir un avoir « prévu » sans document (ou alors en avoir à recevoir 4098 en clôture, s'il est certain).
- **Paiement partiel d'une facture bloquée** (payer 849,00 € sur B) : certains groupes l'autorisent, mais cela complique le lettrage et la relation fournisseur ; la règle simple est « facture entière bloquée jusqu'à l'avoir ou au reliquat ».
- **Statuts PA** : le refus de E doit être transmis via la PA (statut « Refusée ») pour que le fournisseur et l'administration en aient la trace ; un simple mail ne suffit plus (*liste des statuts obligatoires et facultatifs à vérifier dans les spécifications en vigueur*).
- **Le doublon PA + PDF** est le doublon le plus fréquent de la période de transition : l'établissement continue à recevoir des PDF par habitude.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Liste pour Nathalie Ferri (question 5) :**

| Facture | Fournisseur | TTC | Statut | Motif / action |
|---|---|---|---|---|
| F26-7781 | Hygiène Pro Distribution | 1 334,40 | Bon à payer (à échéance) | Conforme BC/BR |
| F26-7795 | Hygiène Pro Distribution | 918,00 | Bloquée | 10 boîtes de gants non livrées (69,00 € HT) — reliquat ou avoir |
| F26-7802 | Hygiène Pro Distribution | 254,40 | Bloquée | Prix 10,60 au lieu de 9,80 (+16,00 € HT) — votre arbitrage tarif |
| MN-4410 | Machines Nett' | 283,20 | Suspendue | Pas de BC — BC de régularisation à créer par Nice |
| MN-4402 | Machines Nett' | — | Refusée via PA | TVA 10 % au lieu de 20 % — facture conforme demandée |
| (PDF F26-7781) | Hygiène Pro Distribution | — | Non saisi | Copie de la facture reçue via PA |

**Message à l'assistante de l'établissement :** « Merci pour le PDF de F26-7781 : nous l'avons déjà reçu via la plateforme le 23/09, il est saisi et validé. Inutile de nous transférer les PDF des fournisseurs : depuis septembre, seules les factures reçues via la plateforme font foi. En revanche, pensez à saisir les bons de réception le jour de la livraison et à signaler les reliquats. »

**Indicateurs** : taux de factures « first time match », âge moyen des litiges ouverts, nombre de factures sans BC par établissement (à remonter au chef d'établissement).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 271 et 230 de l'annexe II : conditions de déduction (TVA régulièrement facturée, facture conforme).
- CGI art. 289 et 289 bis : facturation électronique ; cycle de vie des factures et plateformes agréées (*textes d'application à vérifier*).
- Code de commerce art. L. 441-9 (mentions) et L. 441-10 (délais de paiement).
- PCG : comptes 6063, 6156, 44566, 401, 486 (charges constatées d'avance), 4098 (avoirs à recevoir).
