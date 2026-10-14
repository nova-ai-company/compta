# E07-08 — Gérante majoritaire de SELARL : rémunération TNS et dividendes au-delà de 10 %
**Client :** C12 — Pharmacie Centrale SELARL | **Difficulté :** ★★★ | **Durée estimée :** 70 min | **Thèmes :** gérance majoritaire, statut TNS, comptes 644 / 646, charge à payer de régularisation SSI à une clôture décalée, dividendes et règle des 10 % (article L. 131-6 du CSS), prélèvements à la source sur dividendes, arbitrage rémunération / dividendes

**Corner case :** oui — prélèvements sociaux retenus à tort sur la fraction des dividendes soumise aux cotisations TNS

## La mise en situation

Vendredi 9 octobre 2026. La Pharmacie Centrale clôture au **30/09/2026** ; vous préparez la révision. Hélène Ferrand vous transmet un mail du Dr Anne Petit :

> « Bonjour, pour l'exercice prochain je voudrais me verser moins de salaire et plus de dividendes, on m'a dit que c'était moins taxé. Au passage, le comptable de mon ancien associé dit qu'on aurait mal calculé la retenue sur les dividendes de mars. Pouvez-vous regarder ? Cordialement, Dr Anne Petit »

Note d'Hélène : *« Trois sujets : (1) les charges à payer TNS au 30/09, (2) la retenue sur les dividendes de mars, (3) une réponse argumentée à Anne. Vous avez les taux simplifiés dans le dossier. »*

## Les pièces

### Pièce 1 — Fiche juridique (extrait du dossier permanent)

```
PHARMACIE CENTRALE SELARL — 1 place Bellecour, 69002 Lyon — SIREN 820 444 555
Capital social : 150 000 € — 15 000 parts de 10 € entièrement libérées — Pas de prime d'émission
Associés : Dr Anne PETIT, gérante — 12 000 parts (80 %)
           Dr Luc VIDAL, pharmacien adjoint salarié, non gérant — 3 000 parts (20 %)
Anne Petit : mariée sous le régime de la séparation de biens, son conjoint ne détient aucune part ; pas d'enfant mineur associé.
Compte courant d'associée d'Anne Petit : montant moyen 2026 : 50 000 €
AGO du 15/03/2026 (comptes clos le 30/09/2025) : dividende de 150 000 €, mis en paiement le 31/03/2026
AGO du 15/03/2026 : rémunération de la gérante maintenue à 8 000 € nets par mois ; « la société prend en charge les cotisations sociales personnelles afférentes à la rémunération de la gérante ».
```

### Pièce 2 — Écriture de distribution passée par l'assistante de la pharmacie (31/03/2026)

| Compte | Libellé | Débit | Crédit |
|---|---|---|---|
| 457 | Associés – dividendes à payer | 150 000,00 | |
| 442 | État – prélèvements sur dividendes (PFNL 12,8 % × 150 000) | | 19 200,00 |
| 442 | État – prélèvements sociaux (18,6 % × 150 000) | | 27 900,00 |
| 512 | Virements A. Petit 82 320,00 et L. Vidal 20 580,00 | | 102 900,00 |

Formulaire 2777 déposé et payé le 14/04/2026 : 47 100,00 €.

### Pièce 3 — Grand livre au 30/09/2026 (comptes de la gérante)

| Compte | Intitulé | Solde débiteur |
|---|---|---|
| 644 | Rémunération du travail de l'exploitant | 96 000,00 |
| 646 | Cotisations sociales personnelles de l'exploitant | 36 000,00 (prélèvements SSI d'octobre 2025 à septembre 2026) |

### Pièce 4 — Note de calcul SSI (simulateur, valeurs simplifiées — *à vérifier*)

```
Cotisations de l'année civile 2026 de la gérante :
 - sur la rémunération seule (assiette estimée)      : 41 000 € (provisionnelles 2026 appelées : 34 800 €)
 - supplément lié aux dividendes > 10 % perçus en 2026 : taux moyen retenu 28 % de la fraction concernée
La régularisation 2025 a été provisionnée au 30/09/2025 et s'est révélée exacte (aucun écart).
```

### Pièce 5 — Paramètres retenus (*valeurs à vérifier chaque année*)

| Paramètre | Valeur |
|---|---|
| Prélèvement forfaitaire non libératoire (PFNL) d'IR sur dividendes | 12,8 % |
| Prélèvements sociaux sur revenus de capitaux mobiliers | **18,6 %** (*taux 2026 à vérifier : relèvement de la CSG sur les revenus du capital*) |
| IS (taux marginal de la pharmacie) | 25 % |
| Taux marginal d'imposition à l'IR du foyer d'Anne Petit | 41 % |
| Abattement forfaitaire de 10 % sur rémunérations article 62 du CGI | applicable |
| Coût des cotisations TNS sur la rémunération (simplification) | 40 % de la rémunération nette |

## Travail à faire

1. Qualifiez le statut social d'Anne Petit et de Luc Vidal. Justifiez l'utilisation des comptes 644 et 646.
2. Calculez et comptabilisez la charge à payer de cotisations SSI au 30/09/2026.
3. Calculez la fraction des dividendes d'Anne Petit soumise aux cotisations sociales TNS.
4. Recalculez les retenues à la source correctes sur les dividendes de mars, chiffrez l'erreur et passez l'écriture de correction. Que faut-il faire vis-à-vis de l'administration et d'Anne ?
5. Les cotisations TNS dues sur les dividendes sont-elles une charge de la pharmacie ?
6. Pour 10 000 € de bénéfice avant IS et avant rémunération, comparez (ordre de grandeur) ce qu'il reste à Anne en rémunération et en dividende (fraction > 10 %). Rédigez la réponse à Anne.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E07-08_corrige.md)
