# E14-17 — Intra-groupe : management fees, convention de trésorerie (cash pooling) et rapprochement des comptes réciproques
**Client :** GSF Riviera SAS (filiale **fictive**) et comptabilité du **siège** (société tête GSF, SIREN 775 675 291 — **montants fictifs**) | **Difficulté :** ★★★ | **Durée estimée :** 55 min | **Thèmes :** refacturation de frais de siège, TVA intra-groupe (hors groupe TVA), compte courant de trésorerie, intérêts de cash pooling (base de calcul), comptes réciproques, écarts temporels et écarts de calcul, préparation de la consolidation

**Corner case :** oui — trois écarts de natures différentes se superposent : facture en transit, opération enregistrée à une date différente, erreur de base de calcul des intérêts

> *Cadre de formation : la société tête est réelle mais **toutes les conventions, tous les taux et tous les montants sont fictifs**. On suppose qu'il n'existe **pas** de groupe TVA (assujetti unique) entre les deux sociétés — hypothèse à vérifier dans la réalité.*

## La mise en situation

Mercredi 07/10/2026 (J+5). Le service consolidation du siège envoie à chaque filiale l'état des **comptes réciproques** au 30/09/2026 : tout écart doit être expliqué et corrigé avant le 09/10. Pour GSF Riviera, l'outil de consolidation affiche deux écarts. Sophie Garnier (personnage fictif) :

> « Vous tenez les deux côtés, siège et Riviera : c'est l'occasion. Trouvez l'origine de chaque écart, dites qui corrige, et passez les écritures. »

Comptes chez **GSF Riviera** : 451GSF Groupe – compte courant de trésorerie (siège) ; 401GSF Fournisseur groupe – GSF ; 6228 Rémunérations d'intermédiaires et honoraires – frais de siège (*subdivision selon le plan du groupe*) ; 44566 ; 763 Revenus des autres créances ; 512.
Comptes au **siège** : 451GSFR Groupe – compte courant GSF Riviera ; 411GSFR Client groupe – GSF Riviera ; 706 ; 44571 ; 6615 Intérêts des comptes courants et des dépôts créditeurs ; 512100.

## Les pièces

**Pièce 1 — Convention de prestations de services (extraits, fictive)**
```
Le siège fournit à GSF Riviera des prestations de direction générale,
comptabilité, paie, achats, juridique, informatique.
Rémunération : 2,5 % du chiffre d'affaires HT trimestriel de GSF Riviera,
facturée le dernier jour du trimestre. TVA au taux normal.
Paiement : 30 jours fin de mois.
```

**Pièce 2 — Convention de trésorerie (cash pooling, extraits, fictive)**
```
Remontée quotidienne des soldes bancaires (zero balancing) sur le compte
centralisateur du siège. Les positions sont inscrites en compte courant.
Rémunération des positions prêteuses de la filiale : taux de référence
retenu pour le T3 2026 + marge = 3,10 % l'an (taux fictif, à vérifier au regard
des limites fiscales de déductibilité), calculé sur le solde moyen
du trimestre, base exact/365, inscrit en compte courant le dernier jour
du trimestre.
```

**Pièce 3 — Données du T3 2026**
- Chiffre d'affaires HT de GSF Riviera au T3 2026 : **4 812 000,00 €**.
- Solde moyen prêteur de GSF Riviera dans le cash pooling du 01/07 au 30/09 (92 jours) : **1 850 000,00 €**.
- Facture du siège n° GSF-MF-2026-T3-021 du 30/09/2026 (management fees T3), transmise via la PA le **30/09** ; GSF Riviera l'a reçue le **05/10** et ne l'a pas encore saisie.
- Remontée de trésorerie du 28/09/2026 (45 000,00 €) : comptabilisée par le siège le 28/09 ; comptabilisée par GSF Riviera le **01/10**, date de l'avis d'opéré du cash pooling.

**Pièce 4 — État des comptes réciproques au 30/09/2026 (outil de consolidation)**

| Flux | Siège (vu du siège) | GSF Riviera (vu de la filiale) | Écart |
|---|---|---|---|
| Compte courant cash pooling | 451GSFR : **1 927 106,11 créditeur** (dette envers Riviera) | 451GSF : **1 881 905,34 débiteur** (créance sur le siège) | **45 200,77** |
| Management fees | 411GSFR : **144 360,00 débiteur** | 401GSF : **0,00** | **144 360,00** |

Détail du 451 au siège : principal 1 912 450,00 € + intérêts T3 14 656,11 €. Détail du 451 chez Riviera : principal 1 867 450,00 € + intérêts T3 14 455,34 €.

## Travail à faire

1. Recalculez les management fees du T3 et les intérêts du T3 selon la convention. Qui a raison sur les intérêts ?
2. Expliquez chacun des écarts (nature : temporel / erreur ; qui corrige).
3. Passez les écritures de correction et de rattrapage dans chacune des deux sociétés au 30/09/2026 (et la contre-passation de la saisie du 01/10 chez Riviera).
4. Vérifiez qu'après corrections les comptes réciproques sont égaux.
5. Citez les points de vigilance fiscale et juridique des flux intra-groupe (management fees, intérêts), et l'incidence d'un éventuel groupe TVA.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-17_corrige.md)
