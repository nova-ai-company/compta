# E15-09 — Test technique : emprunt à annuités constantes, intérêts courus, crédit-bail et LCR fournisseur
**Client :** GSF Riviera SAS (filiale régionale **fictive**, siège à Nice) — service comptable | **Difficulté :** ★★☆ | **Durée estimée :** 40 min (test chronométré) | **Thèmes :** calcul d'une annuité constante, tableau d'amortissement d'emprunt, déblocage et frais de dossier, échéance (capital / intérêts), ICNE au 31/12 et extourne, dettes à moins / plus d'un an, crédit-bail (loyers en charges, engagement hors bilan), LCR fournisseur (effets à payer)

**Corner case :** oui — le brouillon de l'établissement passe toute l'échéance en charges d'intérêts et veut immobiliser le véhicule en crédit-bail

> *Cadre de formation : sociétés, documents et personnes fictifs.*

## La mise en situation

Entretien pour le poste d'assistante comptable chez GSF Riviera SAS. Laurent Vidal, chef comptable (personnage fictif), vous laisse **40 minutes** avec une calculatrice : « Le financement, c'est trois choses chez nous : des emprunts pour les machines, du crédit-bail pour les véhicules, et des LCR avec certains fournisseurs. Je veux voir si vous savez séparer le **capital** et les **intérêts**, et si vous savez qu'un véhicule en crédit-bail **ne s'immobilise pas** dans nos comptes sociaux. »

Comptes utilisés (PCG) : 164 Emprunts auprès des établissements de crédit, 1688 Intérêts courus, 6611 Intérêts des emprunts et dettes, 627 Services bancaires et assimilés (*subdivision selon la nomenclature 2025 du PCG*), 6122 Redevances de crédit-bail mobilier, 401 Fournisseurs, 403 Fournisseurs – effets à payer, 44566 TVA déductible sur autres biens et services, 6022 Fournitures consommables, 512 Banque.

## Les pièces

**Pièce 1 — Offre de prêt acceptée**
```
BANQUE DU COMTÉ (fictive) – Agence Nice Arenas
Emprunteur : GSF RIVIERA SAS – SIREN 999 100 206
Objet : financement de 4 autolaveuses
Montant : 60 000,00 €          Durée : 5 ans
Taux nominal annuel fixe : 4,00 %
Remboursement : 5 annuités constantes, payables le 30/06 de chaque année
Première échéance : 30/06/2027
Date de déblocage des fonds : 01/07/2026
Frais de dossier : 300,00 € (non soumis à TVA), prélevés sur le montant débloqué
Formule : annuité = C × i / (1 − (1 + i)^−n)
```

**Pièce 2 — Contrat de crédit-bail (extrait)**
```
AZUR LEASING SAS – SIREN 999 852 361 (fictif)
Objet : fourgon utilitaire électrique, valeur 34 500,00 € HT
Durée : 48 mois à compter du 01/10/2026
Loyers : 48 loyers mensuels de 690,00 € HT (TVA 20 %), payables le 1er de chaque mois
Option d'achat en fin de contrat : 2 000,00 € HT
```

**Pièce 3 — Facture fournisseur payable par LCR**
```
HYGIÈNE PRO MÉDITERRANÉE SAS – SIREN 999 318 427 – TVA FR53999318427 (fictif)
Facture HPM-26-2290 du 15/10/2026 – Client : GSF RIVIERA SAS – SIREN 999 100 206
Nature de l'opération : livraison de biens
Produits d'entretien (détergents, désinfectants)      HT      7 200,00
TVA 20 %                                                       1 440,00
TOTAL TTC                                                      8 640,00
Règlement : LCR magnétique à échéance du 30/11/2026
Pénalités de retard : 3 fois le taux d'intérêt légal – indemnité forfaitaire 40 €
```
Le 20/11/2026, la banque transmet le **relevé des LCR à payer** ; GSF Riviera le retourne avec un « bon à payer » le 22/11/2026. La banque débite le compte le 30/11/2026.

**Pièce 4 — Brouillon d'écritures préparé par l'établissement**
```
30/06/2027  6611 Intérêts des emprunts     13 477,63  /  512 Banque   13 477,63
01/10/2026  2182 Matériel de transport     34 500,00  /  401 Azur Leasing  34 500,00
```

## Travail à faire

1. Calculez l'**annuité constante** de l'emprunt (au centime).
2. Établissez le **tableau d'amortissement** complet (année, capital début, intérêts, amortissement du capital, annuité, capital fin). Que faites-vous de l'écart d'arrondi ?
3. Passez l'écriture de **déblocage** du 01/07/2026 (avec les frais de dossier).
4. Calculez et passez les **intérêts courus** au 31/12/2026, puis l'extourne au 01/01/2027.
5. Passez la **première échéance** du 30/06/2027 et expliquez l'erreur du brouillon (pièce 4).
6. Au bilan du 31/12/2026, quel montant de dette financière figure, et comment se répartit-il entre **moins d'un an** et **plus d'un an** ?
7. Crédit-bail : passez le loyer du 01/10/2026, expliquez pourquoi le brouillon (pièce 4) est faux, et calculez l'**engagement** à mentionner en annexe au 31/12/2026.
8. LCR : passez la facture, l'acceptation de la LCR et le paiement à l'échéance.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-09_corrige.md)
