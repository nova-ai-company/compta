# E15-03 — Lettrage et justification d'un compte fournisseur et d'un compte client
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Nice (ETB061) | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** test technique d'entretien, lettrage total et partiel, justification de solde, relevé de compte fournisseur, facture saisie en double, paiement partiel, avoir non imputé, solde anormal, compte tiers créé en double, mail au fournisseur

**Corner case :** oui — un fournisseur a été créé deux fois dans le fichier tiers : un compte est débiteur, l'autre créditeur, du même montant

> *Cadre de formation : sociétés, documents et personnes fictifs.*

## La mise en situation

Mercredi 14/10/2026, 15 h. Dernière partie du test technique. Laurent Vidal, chef comptable de GSF Riviera (personnage fictif), vous explique :

> « Azur Hygiène nous a envoyé son relevé de compte : il ne trouve pas le même solde que nous. Côté clients, l'Hôtel Bellevue a un solde bizarre. Et regardez Machines Nett', il y a quelque chose qui cloche. Lettrez, expliquez les écarts, proposez les écritures et rédigez la réponse au fournisseur. »

Informations données :
- Le lettrage consiste à **associer** une facture et le ou les règlements (ou avoirs) qui la soldent, en leur donnant une même lettre (A, B, C…). Un lettrage est **total** si la somme des montants associés est nulle, **partiel** sinon.
- Journaux : AC (achats), VT (ventes), BQ (banque), OD (opérations diverses).
- Comptes utiles : 401 et 411 (un sous-compte par tiers), 44566 TVA déductible sur autres biens et services, 6063 Fournitures d'entretien et de petit équipement.

## Les pièces

**Pièce 1 — Grand livre du compte 401AZH Azur Hygiène Distribution (SIREN 999 401 117), au 13/10/2026**

| Date | Journal | Pièce | Libellé | Débit | Crédit |
|---|---|---|---|---|---|
| 02/09 | AC | AC-0905 | Azur Hygiène F26-1101 | | 1 479,00 |
| 09/09 | AC | AC-0912 | Azur Hygiène F26-1130 | | 2 160,00 |
| 11/09 | AC | AC-0918 | Azur Hygiène F26-1130 | | 2 160,00 |
| 30/09 | BQ | BQ-0929 | VIR règlement F26-1101 | 1 479,00 | |
| 02/10 | AC | AC-1002 | Azur Hygiène avoir AV-0412 sur F26-1130 | 144,00 | |
| 05/10 | BQ | BQ-1003 | VIR règlement partiel F26-1130 | 1 000,00 | |
| 06/10 | AC | AC-1006 | Azur Hygiène F26-1188 | | 864,00 |
| | | | **Solde créditeur au 13/10/2026** | | **4 040,00** |

Note de l'établissement de Nice jointe à la pièce BQ-1003 : *« Sur F26-1130 (HT 1 800,00 + TVA 360,00), 12 cartons de produits non conformes. On paie 1 000,00 € tout de suite, le reste quand le fournisseur aura fait son avoir. »*

**Pièce 2 — Relevé de compte reçu d'Azur Hygiène Distribution (point de vue du fournisseur)**

```
AZUR HYGIÈNE DISTRIBUTION SAS — Relevé de compte client au 13/10/2026
Client : GSF Riviera SAS — établissement de Nice

Date     Document        Débit (vous nous devez)   Crédit (en votre faveur)
02/09    F26-1101               1 479,00
09/09    F26-1130               2 160,00
30/09    Règlement                                         1 479,00
02/10    Avoir AV-0412                                       144,00
05/10    Règlement                                         1 000,00
06/10    F26-1188                 864,00
         SOLDE DÛ                                          1 880,00

« Nous constatons un règlement partiel de F26-1130. Merci de nous indiquer
 la date de règlement du solde. » — Service recouvrement
```

**Pièce 3 — Grand livre du compte 411HBR Hôtel Bellevue Riviera SAS (SIREN 999 450 718), au 13/10/2026**

| Date | Journal | Pièce | Libellé | Débit | Crédit |
|---|---|---|---|---|---|
| 31/08 | VT | VT-0831 | FV-2026-0815 nettoyage août | 3 600,00 | |
| 12/09 | BQ | BQ-0909 | VIR Hôtel Bellevue | | 3 600,00 |
| 30/09 | VT | VT-0930 | FV-2026-0921 nettoyage septembre | 3 600,00 | |
| 05/10 | VT | VT-1001 | Avoir AV-V-0031 sur FV-2026-0921 (2 passages de vitrerie non réalisés) | | 360,00 |
| 12/10 | BQ | BQ-1008 | VIR Hôtel Bellevue réf. FV-2026-0921 | | 3 600,00 |
| | | | **Solde créditeur au 13/10/2026** | | **360,00** |

**Pièce 4 — Extraits des comptes 401MNE et 401MNT au 13/10/2026**

| Compte | Date | Journal | Libellé | Débit | Crédit |
|---|---|---|---|---|---|
| 401MNE Machines Nett' (SIREN 999 300 226, créé en 2024) | 05/10 | BQ | VIR règlement MN-4410 | 283,20 | |
| | | | **Solde débiteur** | **283,20** | |
| 401MNT Machines Nett SARL (SIREN 999 300 226, créé le 29/09/2026) | 01/10 | AC | Machines Nett MN-4410 pièces autolaveuse | | 283,20 |
| | | | **Solde créditeur** | | **283,20** |

## Travail à faire

1. **Compte 401AZH** : lettrez le compte (indiquez les lettres et si le lettrage est total ou partiel).
2. Comparez notre solde (4 040,00 €) avec celui du fournisseur (1 880,00 €) : expliquez l'écart et justifiez le solde exact, facture par facture.
3. **Compte 411HBR** : lettrez le compte. Pourquoi un compte client créditeur est-il « anormal » ? Que proposez-vous ?
4. **Comptes 401MNE / 401MNT** : expliquez l'anomalie et sa cause.
5. Passez les écritures de correction au 13/10/2026.
6. Rédigez le mail de réponse au service recouvrement d'Azur Hygiène Distribution.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-03_corrige.md)
