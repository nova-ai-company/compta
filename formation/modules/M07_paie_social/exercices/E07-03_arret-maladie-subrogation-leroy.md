# E07-03 — Arrêt maladie avec subrogation et IJSS
**Client :** C11 — Transports Leroy SAS | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** absence maladie, carence, maintien de salaire, IJSS, subrogation, PAS sur IJSS, suppression du compte 791

**Corner case :** oui — IJSS d'un accident du travail comptabilisées en « transfert de charges » (compte supprimé depuis 2025)

## La mise en situation

Mardi 6 octobre 2026. Bruno Leroy appelle le cabinet :

> « Benoît Garcia, un de mes chauffeurs, a été arrêté en septembre, deux semaines, une bronchite. On a l'accord d'entreprise qui maintient le salaire, et on est en subrogation. La CPAM vient de nous verser des sous. Et puis votre collègue qui a remplacé Yasmine cet été a passé les IJ de l'accident de Jordan en "transfert de charges", c'est normal ? Le commissaire aux comptes de mon client principal m'a dit que ce compte n'existait plus. »

Hélène Ferrand vous confie le dossier : *« Établissez le bulletin de Benoît, passez les écritures, et corrigez l'été. »*

## Les pièces

### Pièce 1 — Avis d'arrêt de travail (volet 3 employeur) — extrait

```
Assuré : GARCIA Benoît — N° SS 1 82 11 69 ••• ••• ••
Employeur : TRANSPORTS LEROY SAS — SIRET 803 909 101 00024
Arrêt de travail initial — Maladie
Du 08/09/2026 au 21/09/2026 inclus (14 jours calendaires) — Sorties autorisées
Date de prescription : 08/09/2026 — Reçu par l'employeur le 09/09/2026
```

### Pièce 2 — Accord d'entreprise du 15/03/2021 (article 7 — extrait)

> « En cas d'arrêt maladie dûment justifié, les salariés comptant au moins un an d'ancienneté bénéficient, **à compter du 4e jour d'arrêt**, du maintien de leur **salaire brut**, sous déduction des indemnités journalières de sécurité sociale **brutes**. L'employeur pratique la **subrogation** : il perçoit directement les IJSS de la CPAM. Les trois premiers jours d'arrêt ne sont pas rémunérés. »

### Pièce 3 — Éléments de paie de Benoît Garcia (septembre 2026)

```
Chauffeur poids lourd, groupe 7 coeff. 150M — CDI — Entrée le 02/05/2020
Salaire mensuel brut : 2 400,00 € (horaire et heures d'équivalence inclus) — même salaire en juin, juillet, août
Retenue d'absence : méthode des jours calendaires (salaire / 30 jours de septembre × jours d'absence)
Taux PAS : 3,8 %
```

### Pièce 4 — Paramètres (valeurs simplifiées — *à vérifier chaque année*)

| Élément | Valeur retenue |
|---|---|
| Délai de carence maladie | 3 jours |
| Salaire journalier de base (SJB) | salaires bruts des 3 mois précédant l'arrêt / 91,25 (plafonnement à 1,4 SMIC non atteint) |
| IJSS maladie | 50 % du SJB par jour calendaire indemnisé |
| CSG + CRDS sur IJSS (précomptées par la CPAM) | 6,20 % + 0,50 % = 6,70 % (dont CSG déductible 3,80 %) |
| Cotisations salariales | Sécu vieillesse 7,30 % ; AGIRC-ARRCO 4,01 % ; mutuelle 30,00 € ; CSG déd. 6,80 % et CSG/CRDS non déd. 2,90 % sur 98,25 % du brut + part patronale mutuelle |
| Cotisations patronales | URSSAF 36,50 % ; AGIRC-ARRCO 6,01 % ; mutuelle 30,00 € |
| Réduction générale (calcul logiciel, septembre) | 332,89 € (URSSAF 282,62 € ; AGIRC-ARRCO 50,27 €) |

### Pièce 5 — Extrait du relevé bancaire BNP Paribas (fictif) — octobre 2026

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 02/10/2026 | VIR CPAM DU RHONE IJ GARCIA B 11/09-21/09 SUBROG | | 404,88 |

### Pièce 6 — Extrait du grand livre 2026 (saisies de l'été)

| Date | Journal | Compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|
| 31/07/2026 | OD-PAIE | 6411 | Paie 07/2026 – salaire maintenu J. Petit (AT) | 2 150,00 | |
| 21/08/2026 | BQ | 512 | CPAM IJ AT J. PETIT 07/2026 subrogation | 1 186,50 | |
| 21/08/2026 | BQ | 791 | Transfert de charges – IJ AT J. Petit | | 1 186,50 |

## Travail à faire

1. Calculez le salaire journalier de base, le nombre de jours indemnisés par la CPAM et le montant des IJSS brutes et nettes.
2. Établissez le bulletin de septembre de Benoît Garcia (retenue d'absence, complément employeur, brut, cotisations, IJSS, net imposable, PAS, net payé).
3. Passez l'écriture de paie de Benoît et l'écriture d'encaissement des IJSS du 02/10.
4. Analysez et corrigez les écritures de l'été (pièce 6).
5. Que faudra-t-il vérifier sur ce compte d'IJSS au 31/12/2026 ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E07-03_corrige.md)
