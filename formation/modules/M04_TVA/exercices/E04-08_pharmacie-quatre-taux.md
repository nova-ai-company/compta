# E04-08 — Quatre taux de TVA à l'officine
**Client :** C12 — Pharmacie Centrale SELARL | **Difficulté :** ★★☆ | **Durée estimée :** 1 h | **Thèmes :** taux de 2,1 %, 5,5 %, 10 % et 20 %, changement de taux d'un médicament déremboursé, remises arrière (ristournes) vs coopération commerciale, ventilation de la TVA par taux sur les avoirs, CA3

**Corner case :** oui — avoir de ristourne d'un laboratoire avec TVA à 20 % sur des produits à 2,1 % et 10 %

## La mise en situation

La Pharmacie Centrale clôture au **30/09/2026** ; la révision est en cours et la CA3 de septembre doit être déposée en octobre. Le Dr Anne Petit, titulaire, vous transmet le récapitulatif mensuel de son logiciel de gestion d'officine (LGO) et les pièces du mois :

> « Tout est dans le LGO, vous n'avez qu'à recopier. Par contre j'ai reçu un avoir de fin d'année du laboratoire Alpin Santé, je ne sais pas où le mettre. Et on a facturé au labo notre opération vitrine de septembre. »

En pointant les mises à jour de la base de données des médicaments, vous constatez que la spécialité « DOLORYX 400 mg » a été **déremboursée à compter du 01/09/2026** : elle relève désormais du taux de **10 %**, mais le LGO l'a laissée à 2,1 % en septembre (ventes : 1 230,00 € TTC).

## Les pièces

### Pièce 1 — Récapitulatif LGO des ventes de septembre 2026 (TTC)

| Taux | Catégorie | Ventes TTC |
|---|---|---|
| 2,1 % | Médicaments remboursables | 142 380,00 (dont DOLORYX 1 230,00) |
| 5,5 % | Dispositifs pour personnes handicapées, protections hygiéniques, produits alimentaires | 9 917,00 |
| 10 % | Médicaments non remboursables | 21 120,00 |
| 20 % | Parapharmacie, cosmétiques | 26 280,00 |
| **Total** | | **199 697,00** |
Règlements : tiers payant (CPAM et mutuelles) 118 400,00 ; CB 70 297,00 ; espèces 11 000,00.

### Pièce 2 — Achats de septembre (factures du grossiste-répartiteur et des laboratoires, HT)

| Taux | HT | TVA |
|---|---|---|
| 2,1 % | 101 400,00 | 2 129,40 |
| 5,5 % | 6 100,00 | 335,50 |
| 10 % | 11 300,00 | 1 130,00 |
| 20 % | 12 800,00 | 2 560,00 |
| Frais généraux à 20 % (loyer avec option TVA, énergie, maintenance, honoraires) | 5 600,00 | 1 120,00 |

### Pièce 3 — Avoir du laboratoire

```
LABORATOIRES ALPIN SANTÉ SAS – 18 avenue des Alpes – 38000 Grenoble – SIREN 534 901 662
AVOIR N° AS-RFA-2026-0412 du 15/09/2026 – Client : Pharmacie Centrale SELARL
Remise de fin d'année (ristourne contractuelle 2026, 4 % du CA HT réalisé avec le laboratoire)
  sur produits remboursables (CA HT 75 000,00)                          3 000,00
  sur produits non remboursables (CA HT 21 000,00)                        840,00
Total HT                                                               3 840,00
TVA 20 %                                                                 768,00
Total TTC                                                              4 608,00 – à déduire de vos prochains règlements
```

### Pièce 4 — Facture émise par la pharmacie

```
PHARMACIE CENTRALE SELARL – 1 place Bellecour – 69002 Lyon – SIREN 820 444 555
FACTURE N° PC-2026-031 du 30/09/2026 – Client : Laboratoires Alpin Santé
Contrat de coopération commerciale du 05/01/2026 – Mise en avant de la gamme « Alpin Soleil »
en vitrine et sur le comptoir du 01/09 au 30/09/2026 (service distinct)
HT 1 500,00 – TVA 20 % 300,00 – TTC 1 800,00 – paiement à 30 jours
```

## Travail à faire

1. Rappelez le champ de chacun des quatre taux à l'officine.
2. Corrigez la ventilation des ventes du LGO et calculez, par taux, les bases HT et la TVA collectée de septembre. Quelle est l'incidence de l'erreur DOLORYX ?
3. Analysez l'avoir du laboratoire : nature, traitement comptable, taux de TVA à appliquer, conséquence pour la pharmacie si elle le comptabilise tel quel.
4. Analysez la facture PC-2026-031 : en quoi diffère-t-elle d'une remise ?
5. Calculez la TVA déductible et la TVA nette due de septembre ; présentez les lignes utiles de la CA3.
6. Passez les écritures de septembre (ventes récapitulatives, facture de coopération commerciale, avoir corrigé).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E04-08_corrige.md)
