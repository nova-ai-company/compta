# E09-07 — Asia Trading : dettes et créances en dollars au 31/12/2026
**Client :** C19 — Asia Trading SARL | **Difficulté :** ★★★ | **Durée estimée :** 1 h 15 | **Thèmes :** conversion des créances et dettes en devises, écarts de conversion actif/passif (476/477), provision pour perte de change (1515), position globale de change, compte bancaire en devises, marchandises en transit (FOB), retraitements fiscaux, dénouement en N+1

**Corner case :** oui — les marchandises en transit ne sont pas dans l'inventaire physique, et le stock ne se réévalue jamais au cours de clôture.

## La mise en situation

*Mise en situation projetée : nous sommes le 12 janvier 2027, en début de saison de clôture.*

Kevin Nguyen, gérant, vous appelle :

> « Le dollar a pris presque 3 % en décembre. Mes dettes chinoises ont gonflé, il faut que je montre une grosse perte ? Par contre, ma créance sur Dubaï a augmenté aussi : je peux compter le gain ? Et pour le stock, mon magasinier a compté l'entrepôt le 31 au soir, je vous envoie le fichier. »

Hélène Ferrand vous rappelle qu'Asia Trading n'a **aucune couverture de change** (pas d'achat à terme, pas d'option) au 31/12/2026, et que la pratique constante de la société est de raisonner en **position globale de change** lorsque les échéances sont voisines (moins de 2 mois d'écart).

**Cours de référence BCE (valeurs fictives retenues pour l'exercice) — 1 € = x USD :**

| Date | Cours |
|---|---|
| 15/11/2026 | 1,0900 |
| 02/12/2026 | 1,0750 |
| 10/12/2026 | 1,0820 |
| 31/12/2026 | 1,0600 |
| 15/01/2027 | 1,0650 |

## Les pièces

**Pièce 1 — Facture fournisseur**
```
SHENZHEN BRIGHT LIGHTING CO., LTD — Invoice n° SBL-2026-1147 — Date: 15/11/2026
Buyer: ASIA TRADING SARL — 60 avenue Berthelot, 69007 Lyon — FR 18 838 900 101
2 400 LED pendant lamps model SBL-P40 — Incoterm FOB Shenzhen — Loaded on board 15/11/2026
Total amount: USD 84,000.00 — Payment: T/T 60 days from B/L date (due 14/01/2027)
```
*Comptabilisée le 15/11/2026 : 84 000 / 1,0900 = 77 064,22 €. Marchandises arrivées, dédouanées et en stock le 20/12/2026.*

**Pièce 2 — Facture fournisseur**
```
NINGBO HOMELIGHT MANUFACTURING CO. — Invoice n° NH-26-0988 — Date: 02/12/2026
1 100 table lamps model NH-T12 — Incoterm FOB Ningbo — Bill of lading dated 02/12/2026
Vessel ETA Fos-sur-Mer: 12/01/2027
Total amount: USD 36,500.00 — Payment: T/T 60 days from B/L date (due 31/01/2027)
```
*Comptabilisée le 02/12/2026 : 36 500 / 1,0750 = 33 953,49 €.*

**Pièce 3 — Facture de vente**
```
ASIA TRADING SARL — Facture n° 2026-0612 du 10/12/2026
Client : LUMIÈRE EMIRATES LLC — Dubai, UAE
Livraison de 900 appliques — Incoterm EXW Lyon — enlevées le 10/12/2026
Exportation — exonération de TVA, art. 262 I du CGI
Montant : USD 52,000.00 — Paiement à 60 jours (10/02/2027)
```
*Comptabilisée le 10/12/2026 : 52 000 / 1,0820 = 48 059,15 €.*

**Pièce 4 — Relevé du compte bancaire en dollars**
```
BANQUE COMMERCIALE DU RHÔNE — Compte devises USD n° 40021-USD — Solde au 31/12/2026 : USD 15,000.00
```
*Solde comptable du compte 5124 « Banque USD » au 31/12/2026 : 13 950,00 € (cours historiques des mouvements).*

**Pièce 5 — Inventaire physique de l'entrepôt au 31/12/2026**
```
Total valorisé au coût d'achat (CMUP, droits de douane et frais d'approche inclus) : 412 600,00 €
NB : les lampes NH-T12 ne sont pas encore arrivées.
```

## Travail à faire
1. Expliquez à Kevin le principe de conversion à la clôture et répondez à ses deux questions.
2. Calculez, pour chaque élément monétaire, la valeur au cours de clôture et l'écart de conversion.
3. Déterminez la provision pour perte de change : (a) élément par élément ; (b) en position globale. Laquelle retenir ?
4. Traitez le compte bancaire en dollars et le stock (pièces 4 et 5).
5. Passez les écritures au 31/12/2026, puis celles du 01/01/2027.
6. Indiquez les retraitements fiscaux sur la 2058-A et montrez que le résultat fiscal n'est pas affecté par la provision.
7. La dette Shenzhen est payée le 15/01/2027 (cours 1,0650). Passez l'écriture de règlement.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E09-07_corrige.md)
