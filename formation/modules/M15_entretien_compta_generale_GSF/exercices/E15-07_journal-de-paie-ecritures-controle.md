# E15-07 — Test technique : du journal de paie aux écritures de salaires et de charges sociales
**Client :** GSF Riviera SAS (filiale régionale **fictive**, siège à Nice) — établissement de Nice | **Difficulté :** ★★☆ | **Durée estimée :** 40 min (test chronométré) | **Thèmes :** écriture de paie à partir d'un journal récapitulatif, cotisations salariales et patronales, prélèvement à la source, acompte, saisie sur salaire, IJSS en subrogation, titres-restaurant, règlements, contrôle des comptes 421 / 431 / 437 / 4421

**Corner case :** oui — le total des cotisations patronales du récapitulatif est mal additionné, et les IJSS subrogées s'ajoutent au net à payer

> *Cadre de formation : sociétés, documents et personnes fictifs.*

## La mise en situation

Deuxième partie de votre entretien chez GSF Riviera SAS. Laurent Vidal, chef comptable (personnage fictif), pose devant vous le journal de paie d'octobre 2026 de l'établissement de Nice, tel qu'il sort du logiciel de paie.

« Chez nous, la paie est faite par le service paie du siège, mais **c'est la comptabilité qui passe et contrôle les écritures**. Vous avez **40 minutes**. Je veux une écriture de paie juste, les règlements, et surtout que vous me disiez comment vous vérifiez que les comptes 421, 431, 437 et 4421 sont bien soldés. Ne vous fiez pas aveuglément aux totaux du logiciel. »

Plan de comptes de GSF Riviera pour la paie (fictif, proche du PCG) :
- 6411 Salaires, appointements ; 6451 Cotisations à l'URSSAF ; 6452 Cotisations aux mutuelles et à la prévoyance ; 6453 Cotisations aux caisses de retraite ; 647 Autres charges sociales (part patronale des titres-restaurant — *subdivision selon le plan du groupe*) ;
- 421 Personnel – rémunérations dues ; 425 Personnel – avances et acomptes ; 427 Personnel – oppositions ; 431 Sécurité sociale (URSSAF) ; 437ARR Caisse de retraite AGIRC-ARRCO ; 437PRV Organisme de prévoyance et mutuelle ; 4387 Organismes sociaux – produits à recevoir (IJSS de la CPAM) ; 4421 Prélèvements à la source (impôt sur le revenu) ; 467TR Titres-restaurant (compte de tiers du groupe) ; 401TRA Fournisseur Titres Azur ; 512 Banque.

## Les pièces

**Pièce 1 — Journal de paie récapitulatif — Établissement de Nice — Octobre 2026 (42 salariés)**

| Rubrique | Base / info | Part salariale | Part patronale |
|---|---|---|---|
| Salaires de base | | 89 420,00 | |
| Heures complémentaires et supplémentaires | | 3 860,00 | |
| Prime d'ancienneté | | 2 150,00 | |
| Prime de salissure | | 1 640,00 | |
| Maintien de salaire maladie (complément employeur) | 3 salariés | 1 690,00 | |
| **SALAIRE BRUT** | | **98 760,00** | |
| URSSAF (sécurité sociale, CSG/CRDS, chômage, après réduction générale) | | 13 450,20 | 22 870,15 |
| Retraite complémentaire AGIRC-ARRCO | | 3 950,40 | 5 925,60 |
| Prévoyance et mutuelle | | 1 205,30 | 1 807,95 |
| **TOTAL COTISATIONS** | | **18 605,90** | **30 630,70** |
| **NET À PAYER AVANT IMPÔT** | | **80 154,10** | |
| Prélèvement à la source | | −2 318,47 | |
| Acompte versé le 15/10/2026 | 2 salariés | −1 500,00 | |
| Saisie sur salaire (versée au commissaire de justice répartiteur) | 1 salarié | −420,00 | |
| Titres-restaurant (360 titres de 9,00 €, part salariale 40 %) | 360 × 3,60 | −1 296,00 | 1 944,00 |
| IJSS nettes en subrogation (avancées par l'employeur) | 3 salariés | +1 284,60 | |
| **NET À PAYER** | | **75 904,23** | |

**Pièce 2 — Informations complémentaires**
```
- Acompte du 15/10/2026 : 1 500,00 € payés par virement, déjà comptabilisés (425 / 512).
- Titres-restaurant : facture TITRES AZUR SAS (SIREN 999 640 118, fictif) n° TA-26-10-0457
  du 20/10/2026, 360 titres × 9,00 € = 3 240,00 € (valeur faciale, hors champ TVA),
  payée par prélèvement le 20/10/2026.
- Virement des salaires nets : 30/10/2026.
- Échéances (on retient) : DSN d'octobre payée le 05/11/2026 (URSSAF, AGIRC-ARRCO, prévoyance,
  prélèvement à la source reversé à la DGFiP) – valeurs et dates à vérifier selon l'effectif.
- Saisie sur salaire : reversée au commissaire de justice le 10/11/2026.
- IJSS : la CPAM verse 1 284,60 € à GSF Riviera le 18/11/2026 (subrogation).
- Méthode de paie : les IJSS ne sont PAS incluses dans le brut ; elles sont ajoutées au net
  car l'employeur les avance au salarié puis les récupère auprès de la CPAM.
```

**Pièce 3 — Note de l'ancienne assistante (trouvée dans le dossier)**
```
« Pour les IJSS, je passais toujours : 512 au débit / 791 Transferts de charges au crédit. »
```

## Travail à faire

1. Vérifiez les totaux du journal de paie (brut, total des cotisations salariales, total des cotisations patronales, net avant impôt, net à payer). Signalez toute erreur.
2. Passez **l'écriture de paie** du 31/10/2026 (salaires et retenues), puis **l'écriture des charges patronales**. Pour chaque compte, dites en quelques mots pourquoi il est au débit ou au crédit.
3. Passez l'achat des titres-restaurant (20/10/2026) et vérifiez que le compte 467TR est soldé.
4. Passez les **règlements** : salaires nets, organismes sociaux, prélèvement à la source, saisie sur salaire, et l'encaissement des IJSS.
5. Après toutes les écritures, montrez que **421, 425, 427, 431, 437ARR, 437PRV, 4387, 4421 et 467TR sont soldés** (tableau de contrôle).
6. Que répondez-vous à la note de la pièce 3 ?
7. Calculez le **coût total employeur** du mois pour l'établissement.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-07_corrige.md)
