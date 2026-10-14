# E15-02 — Rapprochement bancaire complet du mois de septembre
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — compte bancaire de l'établissement de Nice (ETB061) | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** test technique d'entretien, pointage relevé / compte 512, suspens bancaires et comptables, frais bancaires, intérêts débiteurs, prélèvement et virement non comptabilisés, chèque émis non encaissé, remise de chèques non créditée, erreur de sens à la saisie, état de rapprochement

**Corner case :** oui — un règlement fournisseur a été saisi dans le mauvais sens : il faut le corriger pour le **double** de son montant

> *Cadre de formation : sociétés, banques, montants et personnes fictifs.*

## La mise en situation

Mercredi 14/10/2026, 14 h. Deuxième partie de votre entretien chez GSF Riviera. Laurent Vidal, chef comptable (personnage fictif), vous tend deux feuilles :

> « Rapprochement bancaire de septembre du compte de Nice. Au 31/08, le relevé et le compte 512 étaient d'accord, sans aucun suspens. Je veux l'état de rapprochement et les écritures à passer en septembre. Vous avez 40 minutes. »

Informations données :
- Compte comptable : **512100 Banque – Nice** (noté 512 ci-dessous). Journal **BQ**.
- La facture Énergie Sud de septembre (612,00 € TTC) est **déjà enregistrée** au journal des achats, au compte 401ENS.
- Les factures du client Syndic Promenade Gestion (compte 411SPG) totalisant 4 560,00 € TTC sont ouvertes dans le compte client.
- Le règlement du 07/09 à Azur Hygiène Distribution (401AZH) solde une facture de 875,00 € TTC.
- Comptes utiles : 401 (par tiers), 411 (par tiers), 44566 TVA déductible sur autres biens et services, 627 Services bancaires et assimilés, 6616 Intérêts bancaires et sur opérations de financement.

## Les pièces

**Pièce 1 — Relevé de compte de la banque (septembre 2026)**

Rappel : sur un relevé, la banque écrit de **son** point de vue. « Débit » = argent qui **sort** du compte de GSF Riviera ; « Crédit » = argent qui **entre**.

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 01/09 | Solde créditeur au 31/08/2026 | | 41 200,00 |
| 03/09 | VIR SEPA CABINET AZUR SYNDIC – RESIDENCE LES MIMOSAS | | 12 600,00 |
| 07/09 | VIR SEPA EMIS AZUR HYGIENE DISTRIBUTION | 875,00 | |
| 15/09 | VIR SEPA CLINIQUE DES OLIVIERS | | 9 120,00 |
| 18/09 | CHEQUE N° 0001243 | 2 150,00 | |
| 25/09 | PRLV SEPA LOCAZUR LLD VEHICULES 09-2026 | 1 845,60 | |
| 26/09 | PRLV SEPA ENERGIE SUD FACT 09-2026 | 612,00 | |
| 28/09 | VIR SEPA EMIS EQUIP PRO RIVIERA | 4 212,00 | |
| 29/09 | VIR SEPA SYNDIC PROMENADE GESTION | | 4 560,00 |
| 30/09 | FRAIS TENUE DE COMPTE ET COMMISSIONS T3 DONT TVA 6,00 | 36,00 | |
| 30/09 | INTERETS DEBITEURS (facilité de caisse août) | 124,57 | |
| 30/09 | **Solde créditeur au 30/09/2026** | | **57 624,83** |

**Pièce 2 — Extrait du grand livre, compte 512 (septembre 2026)**

Ici, c'est **le point de vue de GSF Riviera** : « Débit » = argent qui entre ; « Crédit » = argent qui sort.

| Date | Pièce | Libellé | Débit | Crédit |
|---|---|---|---|---|
| 01/09 | — | Solde débiteur au 31/08/2026 | 41 200,00 | |
| 03/09 | BQ-0901 | Cabinet Azur Syndic – règlement | 12 600,00 | |
| 07/09 | BQ-0904 | Azur Hygiène – règlement facture | 875,00 | |
| 15/09 | BQ-0911 | Clinique des Oliviers – règlement | 9 120,00 | |
| 16/09 | BQ-0913 | Chèque n° 0001243 Laverie Industrielle Azur | | 2 150,00 |
| 25/09 | BQ-0920 | Locazur – loyer LLD 09/2026 | | 1 845,60 |
| 28/09 | BQ-0924 | Équip'Pro Riviera – règlement | | 4 212,00 |
| 29/09 | BQ-0926 | Chèque n° 0001245 Laverie Industrielle Azur | | 1 980,00 |
| 30/09 | BQ-0928 | Remise de chèques n° 0098 (2 chèques clients) | 2 340,00 | |
| 30/09 | | **Solde débiteur au 30/09/2026** | **55 947,40** | |

*Information complémentaire :* la remise de chèques n° 0098 a été déposée en agence le 30/09 à 17 h ; elle figure sur le relevé d'octobre, au 02/10.

## Travail à faire

1. Pointez le relevé et le compte 512 : listez les opérations présentes **des deux côtés**, puis celles présentes **d'un seul côté**.
2. Pour l'opération du 07/09, expliquez ce qui ne va pas et calculez le montant de la correction.
3. Classez chaque opération non pointée : faut-il passer une écriture en comptabilité, ou s'agit-il d'un décalage qui se régularisera tout seul ?
4. Établissez l'**état de rapprochement** au 30/09/2026 et vérifiez que les deux soldes corrigés sont égaux.
5. Passez les écritures de régularisation au 30/09/2026.
6. Le chèque n° 0001245 n'est pas encore encaissé : que surveillez-vous dans les semaines qui viennent ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-02_corrige.md)
