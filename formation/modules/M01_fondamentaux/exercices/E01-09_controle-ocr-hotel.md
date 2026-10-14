# E01-09 — Six propositions de l'OCR à valider… ou pas
**Client :** C16 — Hôtel Belle Vue | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** pré-comptabilisation, contrôle des propositions OCR, multi-taux, avoir, autoliquidation, seuil d'immobilisation, fichier tiers, date de pièce et clôture

**Corner case :** oui — date d'échéance lue comme date de facture à trois semaines de la clôture du 31/10

## La mise en situation

L'Hôtel Belle Vue clôture le **31/10/2026**. L'outil de pré-comptabilisation a traité le lot de pièces déposé le 08/10/2026 et propose six écritures « prêtes à valider ». Votre collègue Julien, en poste depuis trois mois, vous dit : « L'outil a un taux de confiance de 97 % sur ce lot, je valide tout d'un clic ? »

Hélène Ferrand, passant derrière vous : « 97 % de confiance sur la **lecture des caractères**, pas sur la **comptabilité**. Vous contrôlez les six avant validation, et vous expliquez à Julien ce que vous corrigez. »

Rappels : SAS, réel normal, CA3 mensuelle ; hébergement et petit-déjeuner à 10 %, minibar alcool à 20 %. Fichier tiers du dossier : le fournisseur d'électricité est enregistré sous le compte **401ENRH « Énergies du Rhône »**.

## Les pièces

**Pièce A — Facture StayBooker B.V.** (plateforme de réservation)
```
StayBooker B.V. — Herengracht 500, 1017 CB Amsterdam, Nederland
KvK 61234567 — VAT NL859012345B01
INVOICE / FACTURE N° SB-FR-2026-0927-11834          Date : 30/09/2026
Hotel Belle Vue SAS — 3 montée du Gourguillon, 69005 Lyon, France
VAT FR06 815678333
Commission on stays checked-out in September 2026 (148 reservations)   EUR 3 420,00
VAT : Reverse charge — Article 196 Council Directive 2006/112/EC     EUR     0,00
Total due                                                            EUR 3 420,00
Payment : deducted from guest payments collected by StayBooker (virtual cards)
```
Proposition OCR : `622 Commissions 3 420,00 D / 401STAY 3 420,00 C` — TVA : 0,00 — date 30/09/2026.

**Pièce B — Facture CashPro Lyon** (cash & carry)
```
CASHPRO LYON SAS — 220 route de Vienne, 69008 Lyon — RCS Lyon 433 210 912
FACTURE N° CP-26-114820              Date : 03/10/2026
Client : HÔTEL BELLE VUE SAS — SIREN 815 678 333
Récapitulatif TVA       Base HT      TVA
  5,5 %                 412,00 €    22,66 €   (denrées petit-déjeuner)
  10 %                  238,00 €    23,80 €   (viennoiseries prêtes à consommer)
  20 %                  517,00 €   103,40 €   (vins, bières, spiritueux minibar)
Total HT 1 167,00 €   Total TVA 149,86 €   TOTAL TTC 1 316,86 €
```
Proposition OCR : `601 Achats 1 294,20 D / 44566 22,66 D / 401CASH 1 316,86 C`.

**Pièce C — Hygiène Pro**
```
HYGIÈNE PRO SARL — AVOIR N° AV-26-0071 du 01/10/2026
sur facture n° F-26-0988 du 15/09/2026 — retour de 12 cartons de produits d'accueil (gel douche) non conformes
Montant HT 180,00 € — TVA 20 % 36,00 € — TOTAL AVOIR TTC 216,00 €
```
Proposition OCR : `6063 Fournitures 180,00 D / 44566 36,00 D / 401HYGI 216,00 C` — libellé « Hygiène Pro F AV-26-0071 ».

**Pièce D — Chauffage Service Rhône**
```
CHAUFFAGE SERVICE RHÔNE SAS — FACTURE N° CSR-2026-1477
Date de facture : 30/09/2026 — Date d'échéance : 30/11/2026
Intervention du 24/09/2026 : entretien annuel de la chaudière collective et remplacement d'un circulateur
Montant HT 1 450,00 € — TVA 20 % 290,00 € — TTC 1 740,00 €
```
Proposition OCR : `6152 Entretien biens immobiliers 1 450,00 D / 44566 290,00 D / 401CHSR 1 740,00 C` — **date 30/11/2026**.

**Pièce E — MarketPro**
```
MARKETPRO FRANCE SAS — commande n° 405-7781123 — FACTURE N° MPF-26-55102 du 02/10/2026
Client : Hôtel Belle Vue SAS — SIREN 815 678 333
10 x Téléviseur 43" Smart TV (mode hôtel)  PU HT 549,00 €   Total HT 5 490,00 €
TVA 20 % 1 098,00 € — TOTAL TTC 6 588,00 € — Payé par carte le 02/10/2026
```
Proposition OCR (règle mémorisée « MarketPro → 6063 ») : `6063 Petit équipement 5 490,00 D / 44566 1 098,00 D / 401MARK 6 588,00 C`.

**Pièce F — Énergies du Rhône**
```
ENERGIES DU RHONE SAS — FACTURE N° EDR-0926-778120 du 05/10/2026
Électricité septembre 2026 — HT 2 840,00 € — TVA 20 % 568,00 € — TTC 3 408,00 €
```
Proposition OCR : création d'un **nouveau tiers 401ENER « ENERGIES DU RHONE SAS »** ; `6061 2 840,00 D / 44566 568,00 D / 401ENER 3 408,00 C`.

## Travail à faire

1. Pour chacune des six propositions, dites si elle est **valable** ; sinon, identifiez l'erreur et sa conséquence (résultat, TVA, bilan, exercice).
2. Présentez les écritures correctes.
3. Calculez l'incidence cumulée des erreurs sur le **résultat de l'exercice clos le 31/10/2026** et sur la **TVA** si Julien avait tout validé.
4. Proposez à Julien une **liste de contrôles** à faire systématiquement sur ce dossier avant validation d'un lot OCR, et les paramétrages à modifier dans l'outil.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E01-09_corrige.md)
