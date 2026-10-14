# E05-07 — Vider le compte d'attente de TechNova avant la levée de fonds
**Client :** C08 — TechNova SAS | **Difficulté :** ★★☆ | **Durée estimée :** 60 min | **Thèmes :** compte d'attente 471, identification d'opérations bancaires, avance remboursable, Stripe, autoliquidation, CIR, avance au dirigeant

**Corner case :** oui — parmi les 15 lignes, une avance au président et une dépense personnelle.

## La mise en situation

TechNova prépare une levée de fonds de série A. Le fonds d'investissement demande une **situation intermédiaire au 30/09/2026** révisée par le cabinet. La comptabilité est tenue en interne par Émilie Roux (DAF à temps partagé, deux jours par semaine), qui a tout importé depuis la banque mais n'a pas eu le temps d'affecter certaines lignes.

Hélène Ferrand : « Un 471 de 132 000 € dans une situation envoyée à un investisseur, c'est exclu. Je veux un 471 à zéro, chaque ligne justifiée, et la liste des questions qui restent. Attention à ce que vous trouvez sur Yanis. »

## Les pièces

### Pièce 1 — Grand livre du compte 471 au 30/09/2026

| N° | Date | Libellé bancaire | Débit 471 (décaissement) | Crédit 471 (encaissement) | Solde 471 |
|---|---|---|---|---|---|
| 1 | 03/02/2026 | VIR BPIFRANCE FINANCEMENT REF AR-2025-0412 |  | 12 000,00 | 12 000,00 C |
| 2 | 11/02/2026 | PRLV SEPA AWS EMEA SARL INV EUINFR26-118842 | 1 249,00 |  | 10 751,00 C |
| 3 | 28/02/2026 | VIR SEPA M HADDAD YANIS AVANCE | 3 600,00 |  | 7 151,00 C |
| 4 | 16/03/2026 | VIR STRIPE PAYMENTS EUROPE PO_1Q8x7Z |  | 45 000,00 | 52 151,00 C |
| 5 | 02/04/2026 | PRLV INPI DEPOT 2026-4412 | 270,00 |  | 51 881,00 C |
| 6 | 18/04/2026 | VIR SEPA SOFTDEV CONSULTING | 18 000,00 |  | 33 881,00 C |
| 7 | 30/04/2026 | PRLV DGFIP 0026 TVA | 2 400,00 |  | 31 481,00 C |
| 8 | 12/05/2026 | VIR LOGISTIK PLAN GMBH INV 0142 |  | 8 400,00 | 39 881,00 C |
| 9 | 20/05/2026 | VIR LOGISTIK PLAN GMBH INV 0142 |  | 8 400,00 | 48 281,00 C |
| 10 | 05/06/2026 | CB APPLE.COM/BILL 04/06 | 89,90 |  | 48 191,10 C |
| 11 | 30/06/2026 | VIR M HADDAD YANIS |  | 3 600,00 | 51 791,10 C |
| 12 | 15/07/2026 | PRLV URSSAF RHONE ALPES | 4 830,00 |  | 46 961,10 C |
| 13 | 03/08/2026 | VIR SEPA SCI GERLAND BUREAUX DG | 1 200,00 |  | 45 761,10 C |
| 14 | 25/09/2026 | VIR DGFIP REMBT CREANCE CIR |  | 86 420,00 | 132 181,10 C |
| 15 | 30/09/2026 | FRAIS VIREMENT INTERNATIONAL | 36,00 |  | 132 145,10 C |
| | | **Totaux / solde au 30/09/2026** | **31 674,90** | **163 820,00** | **132 145,10 C** |

### Pièce 2 — Réponses d'Émilie Roux à vos questions (e-mail du 07/10/2026)

> 1. Bpifrance : c'est le solde de l'aide pour projet d'innovation (avance remboursable de 40 000 €, 28 000 € reçus en 2025 et comptabilisés en 1674). Remboursable à partir de 2028 en cas de succès.
> 2. AWS : la facture de février est arrivée dans la boîte mail de Yanis, je vous la transfère. AWS EMEA SARL, Luxembourg, montant 1 249,00 € HT, « VAT reverse charge — Article 196 Directive 2006/112/EC ».
> 3 et 11. Yanis avait besoin d'une avance pour l'achat de son appartement, il a remboursé fin juin. Pas de contrat.
> 4. Stripe : je vous joins le rapport du payout (pièce 3).
> 5. Dépôt de notre marque « TechNova Plan » à l'INPI (3 classes).
> 6. SoftDev : c'est le règlement de leur facture SD-2026-031 du 31/03 (15 000 € HT + TVA), déjà saisie en achats.
> 7. TVA de mars (CA3 déposée, montant à payer 2 400 €, déjà comptabilisée en 44551).
> 8 et 9. Logistik Plan a payé deux fois la facture 0142. Je leur ai écrit, ils m'ont répondu de garder le second paiement pour la facture de juillet (F-2026-0218, 8 400 € HT, autoliquidation, saisie le 01/07).
> 10. Je ne sais pas, c'est la carte de Yanis.
> 12. URSSAF : cotisations de juin (déclarées en DSN, comptabilisées en 431 par la paie : 4 830,00 €).
> 13. Dépôt de garantie du petit bureau qu'on loue à Gerland depuis août (bail de 12 mois).
> 14. Remboursement du CIR 2025 (créance comptabilisée au 31/12/2025 : 86 420 €).
> 15. Frais de la banque sur le virement vers notre freelance au Canada.

### Pièce 3 — Rapport de virement Stripe (extrait)

```
Stripe Payments Europe, Ltd — Payout PO_1Q8x7Z — Date d'arrivée : 16/03/2026
Compte : TechNova SAS — EUR
Paiements (charges) ........................................ 46 452,00
Remboursements .............................................      0,00
Frais Stripe ............................................... - 1 452,00
Montant net viré ........................................... 45 000,00
Période couverte : 01/03/2026 – 14/03/2026
```

Les ventes de la période ont été importées en comptabilité depuis Stripe : débit 4672 « Stripe – transit » 46 452,00 / crédit 706 et TVA collectée. Les frais Stripe n'ont pas été comptabilisés.

### Pièce 4 — Réponse de Yanis Haddad (SMS transféré par Émilie)
> « Le 89,90 Apple c'est l'abonnement Apple One de ma famille, la carte de la boîte était enregistrée par erreur. Je rembourse ! »

## Travail à faire
1. Pour chacune des 15 lignes, identifiez la nature de l'opération et le compte de contrepartie, en justifiant.
2. Passez les écritures permettant de solder le 471 au 30/09/2026, y compris les écritures complémentaires nécessaires (TVA, commissions).
3. Analysez juridiquement et fiscalement les lignes 3, 10 et 11.
4. Listez ce qui reste à obtenir ou à faire après le solde du 471.
5. Expliquez à Émilie pourquoi le 471 doit être vide à chaque arrêté, et proposez une organisation pour éviter la répétition.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E05-07_corrige.md)
