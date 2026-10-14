# E02-03 — Acompte versé à un bureau d'études, puis facture finale à cheval sur la clôture
**Client :** C13 — Atelier Ligne | **Difficulté :** ★★☆ | **Durée estimée :** 35 min | **Thèmes :** acompte versé (4091), facture d'acompte, imputation sur la facture définitive, TVA sur prestations de services (déduction au paiement), option pour les débits, clôture

**Corner case :** oui — facture finale reçue avant la clôture du 30/09 mais payée après : charge de l'exercice, TVA déductible de l'exercice suivant

## La mise en situation

Clôture d'Atelier Ligne au **30/09/2026**. En révisant le compte 4091, vous trouvez un acompte de 3 600,00 € versé en juin au bureau d'études structure BET Structura, qui n'a jamais été soldé. Nicolas Brun, cogérant :

> « Ah oui, Structura ! Ils ont rendu leur note de calcul le 18 septembre, j'ai reçu la facture finale, je la paierai à l'échéance le 20 octobre. Pour l'acompte, j'ai mis la TVA en déductible en juin, c'est bon ? Et la TVA de la facture finale, je peux la mettre dans la déclaration de septembre ? »

Hélène Ferrand : « Reprenez le dossier Structura depuis le début, avec la TVA mois par mois. C'est un cas d'école sur l'exigibilité des services. »

Rappels : Atelier Ligne est au réel normal (CA3 mensuelle). Plan du dossier : 604 Achats d'études et prestations de services (études incorporées aux missions) ; 4091 Fournisseurs – avances et acomptes versés ; 44566 TVA déductible ; **445669 TVA déductible en attente de paiement** (sous-compte du dossier, pour les services non encore payés).

## Les pièces

**Pièce 1 — Facture d'acompte**
```
BET STRUCTURA SAS — Bureau d'études techniques structure béton et bois
22 rue de la Villette, 69003 Lyon
SAS au capital de 40 000 € — RCS Lyon 503 412 776 — TVA FR41 503412776

FACTURE D'ACOMPTE N° BS-2026-0614                   Date : 15/06/2026
Client : ATELIER LIGNE SARL — SIREN 839 222 017
         17 rue Duguesclin, 69006 Lyon
Nature de l'opération : prestation de services
Objet : étude structure — opération « Les Terrasses de Saône » — devis signé DV-26-077
        (montant total 12 000,00 € HT)

Acompte de 30 % à la commande                        HT      3 600,00 €
                                                 TVA 20 %       720,00 €
                                                 TTC         4 320,00 €
Échéance : à réception. Pénalités : 3 x taux d'intérêt légal — Indemnité forfaitaire : 40 €.
```

**Pièce 2 — Relevé bancaire** : 22/06/2026, virement émis « BET STRUCTURA ACPTE BS-2026-0614 » : 4 320,00 €.

**Pièce 3 — Facture finale**
```
BET STRUCTURA SAS — [en-tête identique]

FACTURE N° BS-2026-0931                              Date : 20/09/2026
Client : ATELIER LIGNE SARL — SIREN 839 222 017 — 17 rue Duguesclin, 69006 Lyon
Nature de l'opération : prestation de services
Objet : étude structure « Les Terrasses de Saône » — note de calcul et plans
        remis le 18/09/2026 — devis DV-26-077

Étude structure (prix forfaitaire)                   HT     12 000,00 €
                                                 TVA 20 %     2 400,00 €
                                                 TTC        14 400,00 €
À déduire : facture d'acompte BS-2026-0614 du 15/06/2026
            HT 3 600,00 € — TVA 720,00 € — TTC              - 4 320,00 €
                                         NET À PAYER        10 080,00 €
Échéance : 20/10/2026. Pas d'escompte. Pénalités : 3 x taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

**Pièce 4 — Saisie de juin passée par le cabinet**

| Date | Compte | Libellé | Débit | Crédit |
|---|---|---|---|---|
| 22/06/2026 | 4091 | Structura acompte | 3 600,00 | |
| 22/06/2026 | 44566 | Structura acompte | 720,00 | |
| 22/06/2026 | 512 | Structura acompte | | 4 320,00 |

## Travail à faire

1. Expliquez à quel moment Atelier Ligne peut déduire la TVA de chacune des deux factures, et pourquoi. La saisie de juin est-elle correcte sur le plan de la TVA ?
2. Passez les écritures complètes du dossier Structura selon la méthode du dossier (réception de la facture, paiement, transfert de TVA), de juin à octobre 2026.
3. Présentez les soldes des comptes 4091, 401STRU, 445669 et 604 au 30/09/2026 et commentez.
4. Que changerait la présence, sur les factures de Structura, de la mention « Option pour le paiement de la TVA d'après les débits » ?
5. Répondez à Nicolas Brun.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E02-03_corrige.md)
