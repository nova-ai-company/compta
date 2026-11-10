# E17-04 — Journal de paie, charges sociales par salarié et paiement des salaires
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★★ | **Durée estimée :** 60 min | **Thèmes :** contrôle du journal de paie salarié par salarié, taux de cotisations, prélèvement à la source, acompte, écritures de paie (641, 645, 421, 425, 431, 437, 4421), ventilation analytique par service, salarié partagé entre deux services, paiement des salaires, paiement des organismes sociaux, IJSS en subrogation (PCG 2025)

**Corner case :** oui — une erreur de base de calcul cachée dans la ligne d'un seul salarié ; un salarié travaille pour deux services ; et les IJSS reçues de la CPAM viennent en diminution de la charge (le compte 791 n'existe plus)

> *Cadre de formation : association, personnes et documents fictifs.*

!!! abstract "En clair"
    Le service paie envoie le **journal de paie** : un tableau qui résume tous les bulletins du mois. L'agent comptable **ne le recopie pas** : il le **contrôle** (salarié par salarié), le **comptabilise** (avec le bon service pour chaque salarié), puis **paie** les salaires et les organismes sociaux à la bonne date. Enfin, il suit les **IJSS** que la CPAM doit à l'association.

## La mise en situation

Lundi 2 novembre 2026. Le service paie du Cabinet Ferrand & Associés vous a envoyé le journal de paie d'octobre. Pour l'exercice, on n'en garde qu'un **extrait de 6 salariés** (ceux dont vous avez remonté les variables en E17-03). Les salaires nets ont été virés le **28/10/2026**.

Hélène Ferrand vous écrit :

> « Avant que j'envoie la DSN (déclaration sociale nominative), pouvez-vous contrôler les cotisations salarié par salarié ? Les taux simplifiés sont dans le tableau. Ensuite, passez les écritures avec la ventilation par service : la directrice veut le coût de la paie de chaque service pour le suivi budgétaire. La DSN d'octobre sera prélevée le 16/11. »

**Taux simplifiés retenus pour l'exercice** (taux globaux, réduction générale et cas particuliers ignorés — *valeurs à vérifier chaque année*) :

| Cotisation | Part salariale | Part patronale | Organisme | Compte de tiers |
|---|---|---|---|---|
| URSSAF (Sécurité sociale, CSG/CRDS, chômage, etc.) | 16,80 % du brut | 28,00 % du brut | URSSAF | 431 |
| Retraite complémentaire AGIRC-ARRCO | 4,01 % du brut | 6,01 % du brut | Caisse de retraite | 437ARR |
| Prévoyance | 0,80 % du brut | 1,50 % du brut | Organisme de prévoyance | 437PRV |
| Mutuelle (sauf dispense) | 35,00 € par mois | 35,00 € par mois | Organisme de prévoyance (même contrat) | 437PRV |

Plan de comptes de la paie (fictif, proche du PCG) : 6411 Salaires, appointements ; 6451 Cotisations à l'URSSAF ; 6452 Cotisations aux mutuelles et à la prévoyance ; 6453 Cotisations aux caisses de retraite ; 421 Personnel – rémunérations dues ; 425 Personnel – avances et acomptes ; 431 Sécurité sociale ; 437ARR Caisse de retraite AGIRC-ARRCO ; 437PRV Organisme de prévoyance et mutuelle ; 4387 Organismes sociaux – produits à recevoir ; 4421 Prélèvements à la source ; 512 Banque. Les charges de personnel reçoivent un **code analytique** ; les comptes de tiers, non.

## Les pièces

**Pièce 1 — Journal de paie d'octobre 2026 (extrait) — part salariale et net**

| Salarié | Service | Brut | URSSAF | Retraite | Prévoyance | Mutuelle | Total salarial | Net avant PAS | Net imposable | Taux PAS | PAS | Acompte | Net à payer |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Thomas Girard | 10-SESSAD | 2 712,40 | 455,68 | 108,77 | 21,70 | 35,00 | 621,15 | 2 091,25 | 2 203,53 | 4,1 % | 90,34 | 0,00 | 2 000,91 |
| Claire Dumas | 10-SESSAD | 2 486,00 | 417,65 | 99,69 | 19,89 | 35,00 | 572,23 | 1 913,77 | 2 019,60 | 2,3 % | 46,45 | 0,00 | 1 867,32 |
| Inès Roche | 20-SAVS | 2 075,39 | 348,67 | 83,22 | 16,60 | 35,00 | 483,49 | 1 591,90 | 1 686,03 | 0,0 % | 0,00 | 0,00 | 1 591,90 |
| Rachid Haddad | 20-SAVS / 40-HABITAT | 2 438,20 | 409,62 | 97,77 | 19,51 | 35,00 | 561,90 | 1 876,30 | 1 980,77 | 3,6 % | 71,31 | 0,00 | 1 804,99 |
| Julie Marchetti | 30-EMPLOI | 2 590,00 | 435,12 | 103,86 | 20,72 | 0,00 | 559,70 | 2 030,30 | 2 104,10 | 5,2 % | 109,41 | 0,00 | 1 920,89 |
| Malik Benoît | 01-SIEGE | 1 955,40 | 328,51 | 78,41 | 15,64 | 35,00 | 457,56 | 1 497,84 | 1 588,55 | 1,5 % | 23,83 | 400,00 | 1 074,01 |
| **Total** | | **14 257,39** | **2 395,25** | **571,72** | **114,06** | **175,00** | **3 256,03** | **11 001,36** | **11 582,58** | | **341,34** | **400,00** | **10 260,02** |

**Pièce 2 — Journal de paie d'octobre 2026 (extrait) — part patronale**

| Salarié | URSSAF | Retraite | Prévoyance | Mutuelle | Total patronal |
|---|---|---|---|---|---|
| Thomas Girard | 759,47 | 163,02 | 40,69 | 35,00 | 998,18 |
| Claire Dumas | 696,08 | 149,41 | 37,29 | 35,00 | 917,78 |
| Inès Roche | 581,11 | 124,73 | 31,13 | 35,00 | 771,97 |
| Rachid Haddad | 657,50 | 146,54 | 36,57 | 35,00 | 875,61 |
| Julie Marchetti | 725,20 | 155,66 | 38,85 | 0,00 | 919,71 |
| Malik Benoît | 547,51 | 117,52 | 29,33 | 35,00 | 729,36 |
| **Total** | **3 966,87** | **856,88** | **213,86** | **175,00** | **5 212,61** |

**Pièce 3 — Informations complémentaires**
```
- Thomas Girard : brut avec le nouvel échelon au 01/10/2026.
- Claire Dumas : arrêt maladie du 05/10 au 16/10 (12 jours), subrogation. Méthode retenue
  par le service paie pour l'association (simplifiée pour l'exercice) : le salaire est
  maintenu en entier dans le brut ; les IJSS reçues par l'association viendront en
  diminution des salaires du mois où elles sont versées. Du 19 au 23/10 : congés payés
  (confirmé le 21/10).
  La CPAM verse les IJSS le 18/11/2026 : 3 jours de carence, puis 38,13 € net par jour
  (montant fictif).
- Inès Roche : brut = salaire de base 1 965,55 + heures complémentaires 109,84 (voir E17-03).
  Taux PAS de 0,0 % transmis par l'administration fiscale.
- Rachid Haddad : temps partagé 70 % SAVS (20-SAVS) / 30 % habitat inclusif (40-HABITAT),
  selon son planning.
- Julie Marchetti : dispense de mutuelle (couverte par le contrat obligatoire de son
  conjoint), demande écrite et justificatif reçus le 12/01/2026.
- Malik Benoît : brut = 2 050,00 − absence non rémunérée du 13/10 (94,60) ; acompte de
  400,00 € versé le 15/10 (déjà comptabilisé : débit 425 / crédit 512).
- Salaires nets virés le 28/10/2026.
- DSN d'octobre (URSSAF, retraite, prévoyance-mutuelle, PAS) prélevée le 16/11/2026
  (échéance du 15 reportée, le 15 étant un dimanche).
```

## Travail à faire

1. Recalculez, **pour chaque salarié**, les cotisations salariales et patronales à partir des taux, ainsi que le net à payer. Signalez toute anomalie et dites ce que vous faites. Commentez aussi la mutuelle de Julie Marchetti et le taux PAS d'Inès Roche.
2. Calculez le **coût employeur** de chaque service (brut + charges patronales), en répartissant Rachid Haddad à 70 % / 30 %.
3. Passez l'**écriture de paie** du 28/10/2026 (salaires et retenues) puis l'écriture des **charges patronales**, ventilées par code analytique. Utilisez les montants **corrigés**.
4. Passez le **paiement des salaires nets** (28/10) et le **paiement des organismes sociaux** et du PAS (16/11).
5. Calculez les IJSS de Claire Dumas et passez leur encaissement du 18/11. Pourquoi pas de compte 791 ? Que feriez-vous si les IJSS n'étaient pas encore arrivées au 31/12 ?
6. Montrez que les comptes 421, 425, 431, 437ARR, 437PRV et 4421 sont soldés après ces écritures.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E17-04_corrige.md)
