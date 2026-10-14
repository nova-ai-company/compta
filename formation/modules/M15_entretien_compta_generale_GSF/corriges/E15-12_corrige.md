# Corrigé E15-12 — Test Excel : doublons, totaux par établissement et rapprochement avec la balance fournisseurs

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-12](../exercices/E15-12_test-excel-doublons-rapprochement-balance.md)

*Rappel : société, tiers et montants fictifs. Excel en français : séparateur « ; », fonctions en français.*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Doublons exacts (colonne I)
Un doublon = **même fournisseur + même numéro de facture**. Le montant seul ne suffit pas (deux factures peuvent avoir le même montant), le numéro seul non plus (deux fournisseurs peuvent utiliser le même numéro).

Formule en **I2**, recopiée jusqu'en I26 :

```
=NB.SI.ENS($C$2:$C$26;C2;$D$2:$D$26;D2)
```

Les `$` figent les plages quand on recopie la formule vers le bas ; seule la cellule testée (C2, D2) change. Un résultat **> 1** signale un doublon.
Variante avec NB.SI (une seule condition) : créer une clé en colonne L `=C2&"|"&D2`, puis `=NB.SI($L$2:$L$26;L2)`.

**Résultat** : lignes **3 et 11** (401ACS, facture ACS-7712, 1 158,60 € TTC) → valeur 2. Même facture, déposée deux fois (le 02/10 puis le 09/10) : **vrai doublon**.

### Question 2 — Doublon déguisé (colonne J)
Formule en **J2** : même fournisseur + même montant TTC :

```
=NB.SI.ENS($C$2:$C$26;C2;$H$2:$H$26;H2)
```

Lignes signalées et analyse :

| Lignes | Fournisseur | N° facture | TTC | Verdict |
|---|---|---|---|---|
| 3 et 11 | Azur Consommables Sanitaires | ACS-7712 / ACS-7712 | 1 158,60 | **Vrai doublon** (déjà vu en question 1) |
| 6 et 15 | Hygiène Pro Méditerranée | HPM-26-10412 / HPM2610412 | 2 730,00 | **Vrai doublon déguisé** : même numéro sans les tirets, même établissement (Nice), même montant. NB.SI ne le voit pas car le texte est différent |
| 5, 12, 18, 21 | Textiles Pro Sud | 4 numéros différents | 734,40 | **Pas des doublons** : location mensuelle de 612,00 € HT par établissement ; la ligne 5 (TPS-0926-118) est la facture de **septembre** de Nice reçue en octobre, la ligne 21 celle d'octobre |

Pour repérer automatiquement le doublon déguisé, on peut « nettoyer » le numéro en colonne M : `=SUBSTITUE(D2;"-";"")`, puis compter `=NB.SI.ENS($C$2:$C$26;C2;$M$2:$M$26;M2)`.

**À retenir** : une formule **signale**, c'est la comptable qui **décide** en regardant les pièces.

### Question 3 — Totaux par établissement
Colonne K « Doublon ? » : « Oui » en **K11** et **K15** (on garde la première occurrence), « Non » partout ailleurs.

Total TTC de Nice, tous enregistrements :

```
=SOMME.SI.ENS($H$2:$H$26;$A$2:$A$26;"Nice")
```

Total TTC de Nice hors doublons :

```
=SOMME.SI.ENS($H$2:$H$26;$A$2:$A$26;"Nice";$K$2:$K$26;"Non")
```

(Dans SOMME.SI.ENS, la **plage à additionner vient en premier**, puis les couples plage de critère / critère. Mieux : mettre « Nice » dans une cellule et y faire référence plutôt que de l'écrire en dur.)

### Question 4 — Rapprochement
Onglet « Rappro », ligne 2 (recopiée jusqu'à la ligne 7) :

- **B2** (export hors doublons) : `=SOMME.SI.ENS(Export!$H$2:$H$26;Export!$C$2:$C$26;A2;Export!$K$2:$K$26;"Non")`
- **C2** (balance) avec RECHERCHEX : `=RECHERCHEX(A2;Balance!$A$2:$A$6;Balance!$C$2:$C$6;"Absent")`
- **C2** en version ancienne avec RECHERCHEV : `=SIERREUR(RECHERCHEV(A2;Balance!$A$2:$C$6;3;FAUX);"Absent")` — le **FAUX** (correspondance exacte) est indispensable ; sans lui, Excel peut renvoyer le montant d'un autre fournisseur.
- **D2** (écart = balance − export) : `=SI(ESTNUM(C2);C2-B2;-B2)`

**Lecture des écarts** :
- **401ACS : + 1 158,60** → la comptabilité contient une facture de plus que l'export « propre » : le doublon ACS-7712 a été **saisi deux fois** en comptabilité (à confirmer dans le grand livre 401ACS : deux lignes ACS-7712). Il faut l'annuler, sinon on risque de **payer deux fois**.
- **401HPM : 0** → le doublon déguisé n'a été saisi qu'une fois en comptabilité ; il faut seulement le supprimer / rejeter dans l'outil de dématérialisation.
- **401SEV : « Absent »** → nouveau fournisseur sans compte en comptabilité : la facture SEV-26-0457 **n'a pas été saisie**. Créer le tiers (après contrôle du RIB et du SIREN) et saisir la facture.

## 2. Calculs (détaillés, chaque montant justifié)

**Totaux par établissement (question 3)**

| Établissement | Nb lignes | TTC tous enregistrements | Doublon retiré | TTC hors doublons |
|---|---|---|---|---|
| Nice | 11 | 24 636,96 | ligne 15 : − 2 730,00 | 21 906,96 |
| Antibes | 8 | 13 695,60 | ligne 11 : − 1 158,60 | 12 537,00 |
| Cannes | 6 | 11 031,24 | — | 11 031,24 |
| **Total** | **25** | **49 363,80** | **− 3 888,60** | **45 475,20** |

Contrôle HT / TVA hors doublons : HT 37 896,00 + TVA 7 579,20 = 45 475,20 ✓.

**Rapprochement (question 4)**

| Code tiers | B — Export hors doublons | C — Balance | D — Écart | Explication |
|---|---|---|---|---|
| 401ACS | 4 327,44 | 5 486,04 | + 1 158,60 | ACS-7712 saisie deux fois en compta |
| 401HPM | 10 314,00 | 10 314,00 | 0,00 | Doublon déguisé présent seulement dans l'export |
| 401IRV | 21 888,00 | 21 888,00 | 0,00 | — |
| 401MNC | 5 484,00 | 5 484,00 | 0,00 | — |
| 401TPS | 2 937,60 | 2 937,60 | 0,00 | — |
| 401SEV | 524,16 | Absent | − 524,16 | Facture non saisie, tiers à créer |
| **Total** | **45 475,20** | **46 109,64** | **+ 634,44** | 1 158,60 − 524,16 = 634,44 ✓ |

Détail ACS hors doublons : 1 158,60 + 890,76 + 1 572,00 + 706,08 = 4 327,44 € (lignes 3, 8, 19, 24).

## 3. Écritures comptables

Annulation de la facture saisie en double : on fait **l'inverse** de l'écriture d'achat (débit du fournisseur, crédit de la charge et de la TVA). Saisie de la facture manquante : écriture d'achat classique.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | HA | 401ACS | Fournisseur Azur Consommables Sanitaires | Annulation doublon F ACS-7712 | 1 158,60 | |
| 31/10/2026 | HA | 6068 | Autres matières et fournitures | Annulation doublon F ACS-7712 | | 965,50 |
| 31/10/2026 | HA | 44566 | TVA déductible sur autres biens et services | Annulation doublon F ACS-7712 TVA | | 193,10 |
| 31/10/2026 | HA | 6068 | Autres matières et fournitures | F SEV-26-0457 sacs et emballages Nice | 436,80 | |
| 31/10/2026 | HA | 44566 | TVA déductible sur autres biens et services | F SEV-26-0457 TVA 20 % | 87,36 | |
| 31/10/2026 | HA | 401SEV | Fournisseur Sacs et Emballages du Var | F SEV-26-0457 sacs et emballages Nice | | 524,16 |
| | | | | **Totaux** | **1 682,76** | **1 682,76** |

Après correction : balance 46 109,64 − 1 158,60 + 524,16 = **45 475,20 €** = export hors doublons ✓.

### Question 6 — Le TCD
1. **Avant** : vérifier que les données forment un tableau propre (une ligne d'en-tête, pas de ligne vide ni de sous-total, montants au format nombre et non texte), puis le transformer en **tableau** (Ctrl + L) pour que le TCD suive les ajouts.
2. Insertion > Tableau croisé dynamique, source = le tableau.
3. **Lignes** : Établissement ; **Colonnes** : Fournisseur ; **Valeurs** : Somme de TTC ; **Filtre** : Doublon ? = « Non ».
4. Actualiser le TCD (clic droit > Actualiser) à chaque modification des données : il ne se met pas à jour tout seul. Les totaux par établissement doivent redonner 21 906,96 / 12 537,00 / 11 031,24.

## 4. Points d'attention / pièges

- **Oublier les `$`** : la plage glisse en recopiant et les comptages deviennent faux.
- **RECHERCHEV sans FAUX** : recherche approximative, résultat faux sans message d'erreur.
- **Montants « texte »** dans un export (ex. « 1 158,60 » avec espace insécable) : SOMME.SI.ENS les ignore. Contrôler avec `=ESTNUM(H2)` ou une somme simple.
- **Conclure trop vite** : quatre factures Textiles Pro Sud au même montant ne sont pas des doublons ; deux numéros différents peuvent être la même facture.
- **Annuler un doublon sans preuve** : on regarde le grand livre et les deux PDF avant de contre-passer.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Ce que le recruteur attend** : des formules qui fonctionnent du premier coup (syntaxe française, `;`, `$`), un **contrôle de total** (le rapprochement doit « tomber » : l'écart de 634,44 € est entièrement expliqué), et du jugement sur les faux doublons. Annoncer « je vérifierais d'abord que le doublon n'a pas été payé » est un plus.

**Actions** : bloquer le paiement de la seconde ACS-7712 ; signaler à l'équipe de l'outil de dématérialisation le doublon HPM (règle de normalisation des numéros) ; demander au référent achats le dossier de création du fournisseur SEV (Kbis, RIB, SIREN) avant tout paiement ; conserver le fichier de rapprochement dans le dossier de clôture d'octobre.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 401, 6068, 44566 ; principe de régularité (justification des soldes de tiers).
- CGI : droit à déduction de la TVA subordonné à la détention d'une facture conforme (une facture saisie deux fois ne donne droit qu'à une seule déduction).
- Aide Microsoft Excel : fonctions NB.SI.ENS, SOMME.SI.ENS, RECHERCHEX, RECHERCHEV, SIERREUR, SUBSTITUE.
