# E03-09 — Trois anomalies sur le compte clients
**Client :** C18 — Imprimerie Graphique Rhône SAS | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** double paiement, client créditeur, client hors UE et frais bancaires déduits, export, avoir sur une facture d'un exercice clos, événements postérieurs à la clôture, cut-off

**Corner case :** oui — trois cas atypiques à traiter, dont un qui révèle une omission dans les comptes de l'exercice précédent

## La mise en situation

Sabine Morel, DAF de l'Imprimerie Graphique Rhône, prépare la revue intermédiaire du commissaire aux comptes (cabinet Audit Rhône-Alpes) prévue fin octobre. Elle vous envoie le 9 octobre 2026 une liste de trois points « bizarres » sur lesquels son équipe bloque :

> Bonjour,
> 1) Les Éditions du Confluent nous ont payé deux fois la même facture en septembre. Leur compta nous demande quoi faire.
> 2) Notre client suisse a payé 18 € de moins que la facture. On relance pour 18 € ?
> 3) En février, on a fait un avoir à l'agence Hexa Com pour une facture de décembre 2025 (défaut d'impression). Le CAC veut savoir comment il a été traité et si ça concerne 2025.
> Pouvez-vous me proposer les écritures et une réponse à chacun ? Merci, Sabine

Les comptes 2025 ont été **arrêtés par le président le 20/03/2026** et approuvés le 25/06/2026.

## Les pièces

### Pièce 1 — Compte client 411 CONFLUENT (extrait)

| Date | Pièce | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|---|
| 31/07/2026 | FA-26-0812 | Impression 3 000 ex. « Les Quais du Rhône » (livres) — HT 6 000,00, TVA 5,5 % 330,00 | 6 330,00 | | 6 330,00 D |
| 12/09/2026 | BQ | VIR ÉDITIONS DU CONFLUENT FA-26-0812 | | 6 330,00 | 0,00 |
| 15/09/2026 | BQ | PRLV SEPA B2B ÉDITIONS DU CONFLUENT FA-26-0812 | | 6 330,00 | 6 330,00 C |

Mail du service comptable des Éditions du Confluent (01/10/2026) : *« Suite à une erreur de notre part, la facture FA-26-0812 a été réglée deux fois. Merci de nous rembourser par virement (RIB joint) ou de nous confirmer par écrit l'imputation sur votre prochaine facture. »* Le remboursement par virement a été effectué le **06/10/2026**.

### Pièce 2 — Facture et avis de crédit du client suisse

```
FACTURE N° FA-26-0870 du 08/09/2026
Client : VERLAG ALPENBLICK AG – Bahnhofstrasse 112 – 8001 Zürich – Suisse – UID CHE-114.552.807
Impression et livraison de 1 500 ex. « Wandern im Jura » – Incoterm DAP Zürich
Montant HT 4 250,00 € – « Exonération de TVA – art. 262 I du CGI (exportation) »
Échéance : 30 jours date de facture. Paiement en euros. Frais bancaires : partagés (SHA).
Document d'export : déclaration d'exportation n° 26FR690000EX112874, sortie UE confirmée le 11/09/2026.
```
```
AVIS DE CRÉDIT – 02/10/2026 – Donneur d'ordre : Verlag Alpenblick AG
Montant transféré : 4 250,00 EUR – Frais de la banque intermédiaire : 18,00 EUR
Montant crédité : 4 232,00 EUR – Réf. FA-26-0870
```

### Pièce 3 — Dossier Hexa Com

```
FACTURE N° FA-25-1190 du 18/12/2025 – AGENCE HEXA COM SARL – SIREN 803 667 201
20 000 brochures publicitaires 24 pages, livrées le 17/12/2025
HT 12 000,00 – TVA 20 % 2 400,00 – TTC 14 400,00 – payée le 15/01/2026
```
- 08/01/2026 : réclamation écrite d'Hexa Com (dérive des couleurs sur une partie du tirage), photos jointes.
- 13/02/2026 : accord commercial — remise de 15 % → **avoir AV-26-007** : HT 1 800,00, TVA 360,00, TTC 2 160,00, remboursé par virement le 20/02/2026.
- Comptes 2025 : aucune écriture de provision ni de « RRR à accorder » relative à Hexa Com (vérifié dans le grand livre 2025).
- Écriture passée en février 2026 par l'équipe de Sabine : 411 HEXA au crédit 2 160,00 / 7091 au débit 1 800,00 / 44571 au débit 360,00.

## Travail à faire

1. **Double paiement** : écritures de septembre et d'octobre ; traitement si le remboursement n'avait pas eu lieu avant une clôture ; que répondre aux Éditions du Confluent ?
2. **Client suisse** : écriture de l'encaissement ; faut-il relancer pour 18 € ? Vérifiez les conditions de l'exonération à l'export et la ligne de CA3.
3. **Avoir Hexa Com** :
   a) L'écriture de février 2026 est-elle correcte ? Sur quelle déclaration de TVA l'avoir est-il pris en compte ?
   b) Les comptes 2025 auraient-ils dû enregistrer quelque chose ? Rédigez la réponse au commissaire aux comptes.
4. Présentez l'ensemble des écritures dans un tableau unique.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E03-09_corrige.md)
