# Corrigé E11-06 — Menuiserie Bois & Création : capitaux propres inférieurs à la moitié du capital et abandon de créance de Delta Invest

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-06](../exercices/E11-06_capitaux-propres-menuiserie-abandon-creance.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Ce qu'on compare** : les **capitaux propres comptables** (tout le bloc « capitaux propres » du bilan, y compris subventions d'investissement et provisions réglementées) et la **moitié du capital social** (50 000 / 2 = 25 000 €). Si CP < 25 000 €, la gérance doit consulter les associés sur la dissolution anticipée dans les 4 mois de l'approbation des comptes.

**Le compte courant (question 2)** : un compte courant d'associé, même **bloqué**, est une **dette** de la société. La convention de blocage le rend « quasi-fonds propres » **aux yeux du banquier** (analyse financière), mais il n'entre **jamais** dans les capitaux propres comptables ni dans le calcul de l'art. L. 223-42. L'argument de M. Delmas ne tient pas.

**L'abandon de créance** : Delta Invest renonce à une partie de sa créance → la dette de la Menuiserie disparaît → **produit** chez la Menuiserie (qui améliore son résultat, donc ses capitaux propres) et **charge** chez Delta. La **clause de retour à meilleure fortune** fait renaître la créance si la situation de la Menuiserie s'améliore : tant que la condition n'est pas réalisée, c'est un **engagement hors bilan** (donné chez la Menuiserie, reçu chez Delta).

**La date (question 3)** : un abandon signé le **5 janvier 2027** prend effet en 2027 : il n'a **aucun effet sur les comptes 2026** (au mieux, une information en annexe au titre des événements postérieurs à la clôture). Les capitaux propres au 31/12/2026 resteraient à – 102 000 € : la procédure de l'art. L. 223-42 serait déclenchée à l'approbation des comptes 2026. Il faut **signer (et rendre effective) la convention avant le 31/12/2026**, après décision des organes compétents des deux sociétés.

## 2. Calculs (détaillés, chaque montant justifié)

**Question 1 — Capitaux propres au 31/12/2026**

| Élément | (a) Sans abandon | (b) Abandon 120 000 € | Abandon retenu 130 000 € |
|---|---|---|---|
| Capital | 50 000,00 | 50 000,00 | 50 000,00 |
| Réserve légale | 5 000,00 | 5 000,00 | 5 000,00 |
| Autres réserves | 12 000,00 | 12 000,00 | 12 000,00 |
| Report à nouveau | 3 400,00 | 3 400,00 | 3 400,00 |
| Résultat 2026 | – 182 600,00 | – 62 600,00 | – 52 600,00 |
| Subvention d'investissement | 6 000,00 | 6 000,00 | 6 000,00 |
| Amortissements dérogatoires | 4 200,00 | 4 200,00 | 4 200,00 |
| **Capitaux propres** | **– 102 000,00** | **18 000,00** | **28 000,00** |
| Moitié du capital | 25 000,00 | 25 000,00 | 25 000,00 |
| CP < ½ capital ? | **Oui** | **Oui** | **Non** |

(c) Abandon minimum : 25 000 – (– 102 000) = **127 000 €** (les capitaux propres doivent être **au moins égaux** à la moitié du capital). **120 000 € ne suffisent pas** (il manque 7 000 €). Un abandon de **130 000 €** laisse une marge de 3 000 € — mince : le résultat 2026 n'est encore que **prévisionnel**. Un senior recommande de retenir une marge plus confortable ou de prévoir que le montant soit ajusté au vu de l'arrêté définitif (dans le respect de la date d'effet avant clôture), ou de combiner avec une autre mesure en 2027.

Après abandon de 130 000 €, le compte courant de Delta passe de 260 000 € à **130 000 €**.

## 3. Écritures comptables

**Chez la Menuiserie Bois & Création**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 21/12/2026 | OD | 455100 | Compte courant Delta Invest | Abandon de créance avec clause de retour à meilleure fortune – convention du 21/12/2026 | 130 000,00 | |
| 21/12/2026 | OD | 768 | Autres produits financiers | Abandon de créance financier reçu de Delta Invest | | 130 000,00 |

**Chez Delta Invest**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 21/12/2026 | OD | 668 | Autres charges financières | Abandon de créance à caractère financier – Menuiserie (clause RMF) | 130 000,00 | |
| 21/12/2026 | OD | 4514 | Groupe – compte courant Menuiserie | Abandon partiel du compte courant | | 130 000,00 |

**En cas de retour à meilleure fortune (exemple : exercice N où la clause joue pour 20 000 €)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/N | OD | 668 | Autres charges financières | Menuiserie – retour à meilleure fortune (clause du 21/12/2026) | 20 000,00 | |
| 31/12/N | OD | 455100 | Compte courant Delta Invest | Renaissance de la créance | | 20 000,00 |
| 31/12/N | OD | 4514 | Groupe – compte courant Menuiserie | Delta – renaissance de la créance abandonnée | 20 000,00 | |
| 31/12/N | OD | 768 | Autres produits financiers | Delta – retour à meilleure fortune Menuiserie | | 20 000,00 |
| | | | | **Totaux (abandon + exemple de retour, deux sociétés)** | **300 000,00** | **300 000,00** |

> **Classement** : l'abandon d'un compte courant (avance de trésorerie) a un **caractère financier** → charges et produits financiers (668 / 768, *subdivisions selon la nomenclature 2025 du PCG*). Depuis le règlement ANC n° 2022-06, le résultat exceptionnel est réservé aux événements majeurs et inhabituels : certains praticiens maintiennent l'abandon en exceptionnel lorsqu'il s'inscrit dans un plan de restructuration d'ampleur — choix à **justifier et documenter**, et à appliquer de façon cohérente dans les deux sociétés.

**Annexe (les deux sociétés)**
- **Menuiserie** : engagement **donné** — « Dans le cadre d'un abandon de créance consenti le 21/12/2026 par Delta Invest (130 000 €), la société s'est engagée à reconstituer la créance en cas de retour à meilleure fortune : si, à la clôture de l'un des huit exercices suivants, les capitaux propres excèdent le capital social, à hauteur de 50 % du bénéfice net, dans la limite de l'excédent et du montant restant à recouvrer. Montant maximal : 130 000 €. » + mention de l'événement dans la note sur la **continuité d'exploitation**.
- **Delta Invest** : engagement **reçu** du même montant ; information sur les entreprises liées (charge de 130 000 €, compte courant résiduel de 130 000 €).

## 4. Points d'attention / pièges

- **Compte courant ≠ capitaux propres**, même bloqué.
- **Date d'effet avant la clôture**, sinon l'abandon ne joue pas pour l'exercice 2026. Antidater une convention serait un faux : on la signe réellement avant le 31/12.
- **Montant calculé sur un résultat prévisionnel** : refaire le calcul sur l'arrêté définitif (stocks de bois, dépréciation de la créance du client en redressement judiciaire, provision pour licenciement économique…) — tout ajustement négatif peut faire repasser les CP sous 25 000 €.
- **Subventions et provisions réglementées** font partie des capitaux propres : les oublier fausse le test (ici 10 200 €).
- **Clause de retour à meilleure fortune** : chez la Menuiserie, tant que la condition n'est pas remplie, **pas de dette ni de provision** — seulement un engagement hors bilan. Si la condition devient probable à la clôture d'un exercice, on comptabilise la charge **de cet exercice**.
- **Dépréciation des titres chez Delta** : les titres de la Menuiserie (47 500 €) doivent être testés à la clôture (valeur d'utilité). L'abandon améliore la situation nette de la filiale, mais il est la conséquence de pertes ; le test reste à faire, de même que celui du compte courant résiduel (130 000 €).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 4 — La procédure si les capitaux propres restent < ½ capital**

| Étape | Délai | Détail |
|---|---|---|
| Approbation des comptes 2026 | Au plus tard le 30/06/2027 | Les comptes font apparaître CP < ½ capital |
| Consultation des associés (AGE) sur la **dissolution anticipée** | Dans les **4 mois** suivant l'approbation (ex. AGO le 15/06/2027 → AGE au plus tard le 15/10/2027) | Majorité des modifications statutaires |
| Si pas de dissolution : **publicité** | Après la décision | Avis dans un journal d'annonces légales, dépôt au greffe, inscription au RCS |
| **Régularisation** | Au plus tard à la clôture du **2e exercice suivant** celui de la constatation des pertes (constatation en 2027 → **31/12/2029**) | Reconstituer les CP à hauteur d'au moins ½ capital, ou réduire le capital du montant des pertes non imputées sur les réserves (dans le respect du minimum légal) |
| À défaut | — | Tout intéressé peut demander la dissolution judiciaire ; publicité de la situation, signal négatif pour les fournisseurs, assureurs-crédit et la Banque de France |

> La procédure a été modifiée à plusieurs reprises (notamment par la loi PACTE de 2019) : vérifiez la rédaction en vigueur de l'art. L. 223-42 au moment d'agir.

Et Antoine Girard a raison : il ne s'agit pas de « dissoudre », mais de **consulter** les associés sur la dissolution — ils votent normalement la **poursuite** de l'activité.

**Question 6 — Fiscalité**
- **Delta Invest** : abandon à **caractère financier** (soutien d'une filiale, sans contrepartie commerciale) → charge **non déductible** (art. 39-13 CGI), sauf s'il était consenti dans le cadre d'une procédure de sauvegarde, de redressement, de liquidation judiciaire ou de **conciliation** — *exceptions à vérifier*. Réintégration de 130 000 € sur la 2058-A de Delta. La charge réduit cependant le résultat comptable et donc le bénéfice distribuable de Delta (voir E11-08 : impact sur un acompte sur dividendes).
- **Menuiserie** : le produit de 130 000 € est **imposable** individuellement ; il s'impute en pratique sur la perte de l'exercice (résultat fiscal moins déficitaire).
- **Intégration fiscale** : les abandons de créances entre sociétés du groupe sont **neutralisés** pour la détermination du résultat d'ensemble (art. 223 B CGI) : le produit de la Menuiserie est déduit au niveau du groupe ; la charge de Delta, non déductible individuellement, n'a pas d'effet. Résultat : l'opération est **neutre** pour l'IS du groupe — *mécanisme et tableaux de suivi des neutralisations à vérifier*.
- **Retour à meilleure fortune** : produit imposable chez Delta, charge déductible chez la Menuiserie (dans la limite de ce qui avait été imposé), avec neutralisation si les deux sociétés sont toujours dans le groupe.
- **Associé minoritaire** : Antoine Girard (5 %) profite indirectement de l'abandon (5 % × 130 000 = 6 500 € de situation nette). L'intérêt propre de Delta (préserver une filiale, ses management fees, sa réputation de groupe) doit être documenté dans la décision du président.

**Question 7 — Formalités et alternatives**
- **Menuiserie (SARL)** : convention entre la société et un **associé** (Delta) → **convention réglementée** (art. L. 223-19 C. com.) : rapport du gérant à l'AGO qui statue sur les comptes 2026 ; **Delta ne prend pas part au vote** — seul Antoine Girard vote. Elle n'est ni courante ni conclue à des conditions normales : la procédure s'applique.
- **Delta (SAS)** : décision du président (selon les statuts, autorisation préalable éventuelle d'un comité) ; pas de convention réglementée au sens de l'art. L. 227-10 chez Delta (la Menuiserie n'est ni dirigeant ni associé de Delta) — *à vérifier au regard des dirigeants communs*.
- **Augmentation de capital par compensation** (130 000 €) : elle transforme la dette en capital **sans produit imposable**, mais elle **augmente le capital** à 180 000 € → la moitié du capital passe à 90 000 € ; les CP (28 000 €) resteraient **inférieurs** à la moitié. D'où le « **coup d'accordéon** » : réduire d'abord le capital pour absorber les pertes (sous condition suspensive de l'augmentation), puis augmenter par compensation. Plus lourd juridiquement (AGE, rapports), mais durable — et il fait jouer la dilution d'Antoine Girard s'il ne suit pas.

**Réponse à M. Delmas (extrait)**

> Monsieur le Président,
>
> 1. **Montant** : avec la perte prévisionnelle, les capitaux propres de la Menuiserie au 31/12/2026 seraient de – 102 000 €. Il faut au moins 127 000 € d'abandon pour les ramener à la moitié du capital (25 000 €). Avec 120 000 €, ils seraient de 18 000 € : la procédure de l'article L. 223-42 resterait obligatoire. Nous recommandons **130 000 €**, montant à confirmer au vu de l'arrêté définitif.
> 2. **Date** : la convention doit être **signée avant le 31/12/2026** ; signée le 5 janvier, elle ne modifierait pas les comptes 2026.
> 3. **Compte courant bloqué** : il reste une dette ; il n'est pas pris en compte dans les capitaux propres au sens du Code de commerce.
> 4. **Chez Delta** : charge financière de 130 000 € non déductible, mais neutralisée dans le résultat du groupe intégré ; engagement hors bilan à mentionner ; dépréciation des titres et du compte courant résiduel à examiner.
> 5. **Formalités** : décision de votre part pour Delta ; à la Menuiserie, convention réglementée soumise à l'AGO (vote d'Antoine Girard seul).

**Documentation** : convention signée et datée, décision du président de Delta, rapport du gérant de la Menuiserie, calcul des CP (avec et sans abandon) archivé, mention hors bilan dans les deux annexes, alerte « suivi de la clause RMF » sur 8 exercices dans les deux dossiers.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. **L. 223-42** (SARL : capitaux propres < ½ capital), art. L. 225-248 (SA, applicable aux SAS), art. L. 223-19 (conventions réglementées SARL), art. L. 227-10 (SAS).
- PCG : définition des capitaux propres (classe 1, y compris subventions d'investissement et provisions réglementées) ; engagements hors bilan en annexe ; règlement ANC n° 2022-06 (résultat exceptionnel restreint).
- CGI : art. 39-13 (abandons de créances à caractère financier), art. 223 B (neutralisation des abandons intra-groupe en intégration fiscale), art. 38 (produit imposable chez le bénéficiaire).
- BOFiP : BIC – aides et abandons de créances entre entreprises ; IS – régime de groupe – neutralisations.
