# E08-07 — Coût de production des agendas de l'Imprimerie Graphique Rhône
**Client :** C18 — Imprimerie Graphique Rhône | **Difficulté :** ★★★ | **Durée estimée :** 60 min | **Thèmes :** coût de production (matières, main-d'œuvre directe, sous-traitance, charges indirectes de production), imputation rationnelle des charges fixes, sous-activité exclue, gâche anormale exclue, frais administratifs, commerciaux, financiers et de stockage exclus, VNR, produits obsolètes, variation de stock 7135, relation avec le commissaire aux comptes

**Corner case :** oui — en période creuse, le coût « réel » de l'atelier inclut la sous-activité, que la DAF a stockée

## La mise en situation

L'Imprimerie Graphique Rhône SAS (52 salariés, CAC : Audit Rhône-Alpes) imprime pour des éditeurs et des agences, mais fabrique aussi, chaque fin d'année, sa propre gamme d'**agendas de marque « Rhône Agenda »** vendus aux librairies et papeteries. Clôture au 31/12, IS.

Nous sommes le **18 janvier 2027**. Sabine Morel, directrice administrative et financière, a transmis le calcul du coût des agendas 2027 encore en stock au 31/12/2026, avec ce commentaire :

> « J'ai pris toutes les charges du lot, sans rien oublier, divisées par les 12 000 agendas bons. Coût unitaire 6,78 €, stock de 4 500 agendas = 30 510 €. Le CAC va tester le coût de production, je préfère qu'on soit exhaustifs. »

Hélène Ferrand : « Exhaustif n'est pas le mot. Un coût de production n'est pas un coût complet. Reprenez le calcul, poste par poste. Et vérifiez le taux horaire de l'atelier : novembre et décembre ont été très creux, la presse n° 2 était arrêtée trois semaines faute de commandes. »

Données :
- lot « Rhône Agenda 2027 » : **12 600 agendas imprimés** en novembre-décembre 2026, dont **600 défectueux** (erreur de plaque sur un tirage complet, pilonnés et réimprimés) : **12 000 agendas bons** ;
- au 31/12/2026 : **7 500 agendas vendus et livrés**, **4 500 en stock** ;
- prix de vente aux librairies : **9,90 € HT** l'unité ; commission des représentants : 8 % du prix HT ; transport de livraison : 0,10 € par agenda ; retours et invendus historiques des agendas : moins de 5 % ;
- stock de produits finis **355** au 31/12/2025 : **46 800,00 €**, dont 2 900 agendas 2026 à 5,10 € (14 790,00 €) ; au 31/12/2026, il reste **300 agendas 2026**, invendables (date dépassée), envoyés au pilon avec recyclage du papier le 08/01/2027 ;
- autres produits finis en stock au 31/12/2026 (papeterie de marque), valorisés et vérifiés par vos soins : **38 150,00 €** ;
- aucune dépréciation n'existait au 31/12/2025.

## Les pièces

**Pièce 1 — Calcul de Sabine Morel (fichier « coût agendas 2027.xlsx »)**
```
IMPRIMERIE GRAPHIQUE RHÔNE — Coût de revient lot Rhône Agenda 2027 (12 000 bons)
Poste                                                         Montant      Remarque
1  Papier intérieur et carton de couverture (CMUP)           19 940,00    dont tirage défectueux : 880,00
2  Encres, plaques, consommables d'impression                 2 265,00    dont tirage défectueux : 105,00
3  Façonnage sous-traité (reliure spirale) — Façonnage
   Lyonnais, facture FL-26-1290                               7 200,00    12 000 agendas
4  Conception graphique de la gamme 2027 (studio externe)    3 600,00    spécifique à la gamme 2027
5  Main-d'œuvre directe atelier : 538 h x 38,50 €/h         20 713,00    dont tirage défectueux : 18 h
6  Charges indirectes atelier offset : 220 h machine
   x 80,00 €/h (taux réel nov.-déc.)                         17 600,00    dont tirage défectueux : 10 h
7  Quote-part frais de direction, comptabilité, RH           4 500,00
8  Campagne de promotion auprès des libraires                 2 800,00
9  Intérêts de l'emprunt de la presse n° 2 (quote-part)        640,00
10 Location de l'entrepôt de stockage des produits finis        900,00
11 Transport de livraison aux libraires (7 500 livrés)        1 150,00
TOTAL                                                        81 308,00
Coût unitaire : 81 308 / 12 000 = 6,78 €  — Stock : 4 500 x 6,78 = 30 510,00 €
```

**Pièce 2 — Fiche de l'atelier offset (contrôle de gestion)**
```
ATELIER OFFSET — Novembre-décembre 2026
Charges fixes de l'atelier (amortissements presses, redevances de crédit-bail de la presse n° 1,
maintenance, énergie hors consommation proportionnelle, encadrement d'atelier)        84 000,00 €
Capacité normale (moyenne des 3 dernières années, même période, maintenance prévue
déduite)                                                                               1 400 h machine
Activité réelle nov.-déc. 2026 (presse n° 2 arrêtée 3 semaines faute de commandes)    1 050 h machine
Taux réel = 84 000 / 1 050 = 80,00 €/h
```

**Pièce 3 — Taux horaire de la main-d'œuvre directe**
```
Conducteurs offset et aides : salaire brut + charges patronales + congés payés + 13e mois,
divisés par les heures productives : 38,50 €/h (taux validé par le CAC lors de l'audit 2025).
```

## Travail à faire

1. Pour chacun des 11 postes du calcul de Sabine, indiquez s'il entre dans le coût de production des agendas, pour quel montant, et pourquoi.
2. Calculez le taux d'imputation des charges fixes de l'atelier et le coût de la sous-activité de la période.
3. Déterminez le coût de production du lot, le coût unitaire et la valeur des 4 500 agendas en stock au 31/12/2026.
4. Vérifiez la VNR des agendas 2027 et traitez les agendas 2026 restants.
5. Passez l'écriture de variation des stocks de produits finis au 31/12/2026 et commentez le sens du 7135.
6. Chiffrez l'incidence de la correction sur le résultat et rédigez la note destinée à Sabine Morel (et au CAC).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E08-07_corrige.md)
