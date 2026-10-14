# E13-05 — ImmoPlus : rapprochement des fonds mandants et honoraires passés à tort en chiffre d'affaires
**Client :** C22 — ImmoPlus | **Difficulté :** ★★★ | **Durée estimée :** 1 h | **Thèmes :** loi Hoguet, compte séquestre, comptabilité mandants, représentation des fonds, garantie financière, honoraires de gestion et de transaction (fait générateur), TVA

**Corner case :** oui — un loyer encaissé sur le compte de l'agence a été comptabilisé en honoraires, et la garantie financière est insuffisante

## La mise en situation

La caisse de garantie d'ImmoPlus demande, comme chaque trimestre, l'**état de rapprochement des fonds mandants au 30/09/2026**. Frédéric Blanc, le gérant, transmet les pièces au cabinet le 9 octobre avec ce mot :

> « Ma gestionnaire est en congé, vous pouvez faire le rapprochement ? Normalement tout tombe juste. Au passage, septembre a été un excellent mois : regardez le CA ! »

Hélène Ferrand : « Faites le rapprochement, vérifiez le CA de septembre, et regardez si la garantie financière est suffisante. La CA3 de septembre n'est pas encore déposée (échéance dans quelques jours) : profitez-en. »

Rappels : ImmoPlus, SARL, cartes **T** (transaction) et **G** (gestion) ; environ 180 lots en gestion. La comptabilité mandants est tenue dans le logiciel de gestion locative ; la comptabilité de l'agence enregistre ses propres opérations et un compte de liaison **467MAND « Fonds mandants – liaison »**. TVA sur les débits non optée : TVA exigible à l'encaissement des honoraires.

## Les pièces

**Pièce 1 — Relevé du compte séquestre « ImmoPlus – Fonds mandants » au 30/09/2026 (Banque Rhône-Alpes)**
```
Compte n° 30004 01234 00078945612 — Compte réglementé loi Hoguet
Solde au 31/08/2026 ................................................. 214 905,60 €
[...] mouvements de septembre [...]
29/09  PRLV FRAIS TENUE COMPTE SEQUESTRE T3                              - 18,50
30/09  ........................................................................
SOLDE CRÉDITEUR AU 30/09/2026 ....................................... 298 702,25 €
Solde le plus élevé du mois : 405 860,12 € (le 08/09/2026, après encaissement des loyers)
```

**Pièce 2 — Balance de la comptabilité mandants au 30/09/2026 (logiciel de gestion)**

| Compte | Solde |
|---|---|
| Propriétaires – soldes à reverser (créditeurs) | 186 420,35 € C |
| Dépôts de garantie détenus pour le compte des bailleurs | 96 300,00 € C |
| Locataires créditeurs (loyers payés d'avance) | 2 180,00 € C |
| Honoraires de gestion de septembre dus à l'agence (prélevés sur les comptes propriétaires, non encore virés) | 9 612,00 € C |
| Fournisseurs – travaux à payer pour le compte des propriétaires | 3 248,40 € C |
| **Banque séquestre (solde comptable)** | **297 760,75 € D** |
| Locataire Mme Petitjean (lot 42 – propriétaire M. Vasseur) : loyer de septembre non encaissé | 1 150,00 € D (loyer appelé, propriétaire non crédité) |

Suspens notés par la gestionnaire avant son départ :
- chèque de dépôt de garantie (locataire M. Haddad), remis en banque le 30/09 : 1 900,00 € — non encore crédité ;
- virement au propriétaire Mme Roche émis le 30/09 : 2 860,00 € — non encore débité.

**Pièce 3 — Relevé du compte courant de l'agence (Banque Rhône-Alpes) — extrait**
```
10/09/2026  VIR SEPA MME PETITJEAN CLAIRE LOYER SEPT LOT 42            + 1 150,00
```

**Pièce 4 — Extrait du grand livre de l'agence, compte 706 « Honoraires » (septembre 2026)**

| Date | Libellé | Crédit |
|---|---|---|
| 10/09/2026 | Encaissement virement Petitjean (affectation automatique « honoraires ») | 958,33 € (+ TVA 191,67 € en 44571) |
| 15/09/2026 | Honoraires vente Lambertin / Morel – compromis signé ce jour (acte authentique prévu le 20/11/2026) – facture n° T-2026-031 au vendeur | 10 000,00 € (+ TVA 2 000,00 € en 44571) |
| 30/09/2026 | Honoraires de gestion septembre (relevé mandants) | 8 010,00 € (+ TVA 1 602,00 € en 44571) |
| 30/09/2026 | Autres honoraires de location et de gestion du mois | 31 240,00 € |
| | **Total septembre** | **50 208,33 €** |

**Pièce 5 — Attestation de garantie financière**
```
CAISSE DE GARANTIE DE L'IMMOBILIER [fictive] — Attestation n° G-2026-0877
ImmoPlus SARL — SIREN 822 555 666 — Carte professionnelle CPI 6901 2018 000 012 345
Activité « Gestion immobilière » : garantie financière accordée pour un montant de 350 000,00 €
Activité « Transactions » : sans détention de fonds (déclaration du titulaire)
Valable du 01/01/2026 au 31/12/2026.
```

## Travail à faire

1. Établissez le rapprochement bancaire du compte séquestre au 30/09/2026 (solde du relevé / solde de la comptabilité mandants).
2. Établissez l'état de **représentation des fonds** : les fonds disponibles couvrent-ils toutes les sommes dues aux mandants ? Chiffrez l'éventuel déficit, en tenant compte du loyer de Mme Petitjean.
3. Analysez les écritures du compte 706 de septembre : quelles sont les erreurs ? Quel est le chiffre d'affaires correct ?
4. Passez les écritures de correction dans la comptabilité de l'agence, ainsi que les virements nécessaires entre le compte agence et le compte séquestre. Quelles corrections dans la comptabilité mandants ?
5. Quelles conséquences sur la CA3 de septembre ?
6. La garantie financière est-elle suffisante ? Que faites-vous ?
7. Rédigez le message à Frédéric Blanc.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E13-05_corrige.md)
