# E14-05 — Rapprochement commande / réception / facture (3-way match) : six factures fournisseurs à traiter
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Nice | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** 3-way match, tolérances d'écart, bon à payer, blocage, factures électroniques reçues via plateforme agréée (PA), statuts du cycle de vie, doublon PA + PDF, facture sans commande, taux de TVA erroné

**Corner case :** oui — la même facture arrive deux fois (flux électronique via la PA et PDF transféré par mail) ; une facture sans commande concerne une dépense réelle et nécessaire

> *Cadre de formation : sociétés, documents et personnes fictifs.*

## La mise en situation

Lundi 05/10/2026, 8 h 45. Le poste « factures fournisseurs » du siège compte six documents en attente pour l'établissement de Nice. Nathalie Ferri, acheteuse au service Achats (personnage fictif), passe la tête dans le bureau :

> « Le run de paiement part jeudi. Je veux la liste de ce qui est bon à payer et de ce qui est bloqué, avec le motif, avant midi. Et pas de saisie en double, on a eu le cas le mois dernier. »

Règles du groupe (procédure interne fictive) :
- Toute facture de marchandises doit être rapprochée d'un **bon de commande (BC)** validé et d'un **bon de réception (BR)** saisi par l'établissement. Pour les services sous contrat, le contrat tient lieu de commande et la période facturée tient lieu de réception.
- **Tolérance automatique** : écart ≤ 1 % du HT de la ligne **et** ≤ 20,00 € HT par facture. Au-delà : blocage et litige ouvert.
- Depuis le 01/09/2026, **seule la facture reçue via la PA** fait foi ; les PDF reçus par mail sont des copies.
- Toutes les factures reçues et recevables sont **comptabilisées** à réception (même bloquées au paiement) ; une facture **refusée** via la PA n'est pas comptabilisée.
- Comptes : 6063 Fournitures d'entretien et de petit équipement ; 6156 Maintenance ; 44566 TVA déductible sur ABS ; 401HPD Hygiène Pro Distribution ; 401MNE Machines Nett'.

## Les pièces

**Pièce 1 — Bons de commande validés (extraits ERP)**

| BC | Fournisseur | Article | Qté | PU HT |
|---|---|---|---|---|
| BC-2026-0911 | Hygiène Pro Distribution | Sacs 110 L (carton de 200) | 40 | 18,50 |
| BC-2026-0911 | Hygiène Pro Distribution | Détergent neutre 5 L | 30 | 12,40 |
| BC-2026-0915 | Hygiène Pro Distribution | Essuie-mains rouleau | 100 | 4,20 |
| BC-2026-0915 | Hygiène Pro Distribution | Gants nitrile (boîte de 100) | 50 | 6,90 |
| BC-2026-0920 | Hygiène Pro Distribution | Désinfectant surfaces 5 L | 20 | 9,80 |
| Contrat MN-2025-07 | Machines Nett' | Maintenance préventive autolaveuse, par machine et par trimestre | 3 | 165,00 |

**Pièce 2 — Bons de réception saisis par l'établissement de Nice**

| BR | BC | Date | Article | Qté reçue |
|---|---|---|---|---|
| BR-NIC-2026-0612 | BC-2026-0911 | 22/09 | Sacs 110 L | 40 |
| BR-NIC-2026-0612 | BC-2026-0911 | 22/09 | Détergent neutre 5 L | 30 |
| BR-NIC-2026-0618 | BC-2026-0915 | 25/09 | Essuie-mains rouleau | 100 |
| BR-NIC-2026-0618 | BC-2026-0915 | 25/09 | Gants nitrile | 40 (*« reliquat 10 boîtes – rupture fournisseur »*) |
| BR-NIC-2026-0623 | BC-2026-0920 | 28/09 | Désinfectant surfaces 5 L | 20 |
| BR-NIC-2026-0627 | — | 29/09 | 2 brosses de lavage + 1 bavette d'aspiration (BL Machines Nett' n° BL-8812, signé par le chef d'équipe) | 1 lot |

**Pièce 3 — Les six documents reçus**

| N° | Canal | Fournisseur (SIREN) | Facture | Date | Contenu | HT | TVA | TTC |
|---|---|---|---|---|---|---|---|---|
| A | PA | Hygiène Pro Distribution (999 300 119) | F26-7781 | 23/09/2026 | BC-2026-0911 : 40 × 18,50 ; 30 × 12,40 | 1 112,00 | 222,40 (20 %) | 1 334,40 |
| B | PA | Hygiène Pro Distribution | F26-7795 | 26/09/2026 | BC-2026-0915 : 100 × 4,20 ; 50 × 6,90 | 765,00 | 153,00 (20 %) | 918,00 |
| C | PA | Hygiène Pro Distribution | F26-7802 | 29/09/2026 | BC-2026-0920 : 20 × 10,60 | 212,00 | 42,40 (20 %) | 254,40 |
| D | PA | Machines Nett' (999 300 226) | MN-4410 | 30/09/2026 | « Pièces détachées autolaveuse — commande téléphonique du 28/09 », sans référence de BC | 236,00 | 47,20 (20 %) | 283,20 |
| E | PA | Machines Nett' | MN-4402 | 01/10/2026 | Contrat MN-2025-07, maintenance T4 2026 (oct.-déc.) : 3 × 165,00 | 495,00 | 49,50 (10 %) | 544,50 |
| F | Mail (PDF) | Hygiène Pro Distribution | F26-7781 | 23/09/2026 | PDF transféré par l'assistante de l'établissement : « Facture à payer svp ! » | 1 112,00 | 222,40 | 1 334,40 |

Toutes les factures portent les mentions obligatoires usuelles (SIREN de GSF Riviera, nature de l'opération, échéance à 45 jours fin de mois, pénalités, 40 €) — sauf indication contraire ci-dessus.

## Travail à faire

1. Réalisez le 3-way match de chaque document (tableau : BC / BR / facture / écart / décision / statut à renvoyer via la PA / action).
2. Pour chaque blocage, indiquez qui doit lever le blocage et ce qu'on attend (avoir, BC de régularisation, facture rectifiée, livraison du reliquat…).
3. Passez les écritures d'achat à comptabiliser au 05/10/2026.
4. La facture E concerne le trimestre octobre-décembre. Quel traitement à la clôture mensuelle d'octobre, une fois la facture rectifiée reçue ?
5. Préparez la liste « bon à payer / bloqué » demandée par Nathalie Ferri.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-05_corrige.md)
