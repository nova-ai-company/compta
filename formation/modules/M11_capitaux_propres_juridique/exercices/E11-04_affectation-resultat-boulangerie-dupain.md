# E11-04 — Boulangerie Dupain : affectation du résultat, dividendes et 2777
**Client :** C01 — Boulangerie Dupain SARL | **Difficulté :** ★★☆ | **Durée estimée :** 1 h | **Thèmes :** réserve légale plafonnée, bénéfice distribuable, affectation du résultat, dividendes, PFNL et prélèvements sociaux, dispense de PFNL, règle des 10 % du gérant majoritaire, imprimé 2777, IFU

**Corner case :** oui — réserve légale presque complète (dotation plafonnée) et dividendes d'un gérant majoritaire partiellement soumis aux cotisations sociales.

## La mise en situation

Lundi 3 mai 2027. Les comptes 2026 de la Boulangerie Dupain sont arrêtés. Marc Dupain passe au cabinet (après 14 h, comme toujours) avec un projet de procès-verbal qu'il a préparé à partir d'un modèle trouvé sur internet :

> « J'ai tout préparé, vous n'avez plus qu'à mettre au propre. On se verse 45 000 € de dividendes avec Julie, comme ça elle aussi en profite. Ce qui m'arrange, c'est que c'est "flat tax" à 30 %, donc pas de charges sociales comme sur mon salaire. Et la banque, je lui vire combien à l'État, et quand ? »

Hélène Ferrand : « On a la mission juridique. Vérifiez son projet, refaites l'affectation, préparez les écritures et le calendrier des déclarations. Julie nous a déposé une demande de dispense de prélèvement en novembre, elle est au dossier. Et expliquez à Marc, gentiment, que la "flat tax" n'est pas tout à fait ce qu'il croit. »

## Les pièces

**Pièce 1 — Extrait de la balance au 31/12/2026 (après inventaire, avant affectation)**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 1013 | Capital souscrit, appelé, versé (2 000 parts de 10 €) | | 20 000,00 |
| 1061 | Réserve légale | | 1 650,00 |
| 1068 | Autres réserves | | 100 000,00 |
| 110 | Report à nouveau (créditeur) | | 10 350,00 |
| 120 | Résultat de l'exercice 2026 (bénéfice) | | 71 380,00 |
| 455 | Associés – comptes courants | | 0,00 |
| 512 | Banque (solde au 30/04/2027 : 104 600 €) | | |

**Pièce 2 — Répartition du capital**

```
Marc DUPAIN — gérant majoritaire (TNS) — 1 200 parts (60 %)
Julie DUPAIN — sœur de Marc, vendeuse salariée — 800 parts (40 %)
Marc n'est ni marié ni pacsé ; il n'a pas d'enfant mineur associé. Aucune prime d'émission.
Aucun compte courant d'associé en 2026 ni en 2027.
```

**Pièce 3 — Projet de PV préparé par Marc**

```
SARL BOULANGERIE DUPAIN — au capital de 20 000 € — 12 rue de la Charité, 69002 Lyon
RCS Lyon 912 345 001
PROCÈS-VERBAL DE L'ASSEMBLÉE GÉNÉRALE ORDINAIRE DU 27 MAI 2027

Deuxième résolution — Affectation du résultat
L'assemblée décide d'affecter le bénéfice de l'exercice, soit 71 380 €, comme suit :
   - à la réserve légale (5 %)                       3 569,00 €
   - à la réserve facultative                       20 000,00 €
   - aux associés à titre de dividendes            45 000,00 €
   - au report à nouveau                             2 811,00 €
Les dividendes seront versés nets du prélèvement forfaitaire unique de 30 %, soit
31 500 € nets, le 10 juin 2027.
Conformément à la loi, l'assemblée rappelle qu'aucun dividende n'a été distribué
au titre des trois exercices précédents.
```

**Pièce 4 — Demande de dispense de prélèvement forfaitaire non libératoire**

```
Je soussignée Julie DUPAIN, demeurant 7 rue Mercière, 69002 Lyon, atteste sur l'honneur
que le revenu fiscal de référence de mon foyer fiscal figurant sur mon avis d'impôt sur
les revenus de l'année 2025 est inférieur à 50 000 € (personne seule), et demande à être
dispensée du prélèvement prévu à l'article 117 quater du CGI sur les revenus distribués
qui me seront versés en 2027.
Fait à Lyon, le 20/11/2026 — Signature
```

Marc n'a déposé aucune demande de dispense (son revenu fiscal de référence dépasse le seuil).

**Pièce 5 — Paramètres retenus (valeurs à vérifier chaque année)**

```
- Prélèvement forfaitaire non libératoire (PFNL) : 12,8 %.
- Prélèvements sociaux sur les revenus du capital : 18,6 % (selon nos informations, après la
  hausse de CSG prévue par la LFSS 2026 — taux à vérifier ; 17,2 % auparavant).
- Soit un « PFU » global de 31,4 % (à vérifier).
- Seuil de dispense de PFNL : RFR N-2 < 50 000 € (personne seule) / 75 000 € (couple).
- Cotisations sociales du gérant majoritaire sur la fraction des dividendes > 10 % :
  on retient, pour une estimation, un taux global de 40 % (à vérifier).
```

## Travail à faire

1. Relevez les erreurs du projet de PV de Marc.
2. Calculez la dotation à la réserve légale, le bénéfice distribuable et le montant maximum distribuable.
3. Proposez une rédaction corrigée de la résolution d'affectation (en conservant les choix de Marc : 20 000 € en réserve facultative et 45 000 € de dividendes).
4. Calculez, pour chaque associé, le dividende brut, les retenues opérées par la société et le net versé.
5. Passez les écritures d'affectation (27/05/2027), de paiement (10/06/2027) et de reversement des prélèvements.
6. Établissez le calendrier déclaratif (2777, IFU) et expliquez la situation sociale de Marc.
7. Répondez à Marc sur la « flat tax à 30 % ».

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E11-04_corrige.md)
