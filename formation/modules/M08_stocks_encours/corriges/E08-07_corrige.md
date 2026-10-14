# Corrigé E08-07 — Coût de production des agendas de l'Imprimerie Graphique Rhône

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-07](../exercices/E08-07_cout-production-imprimerie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Le **coût de production** d'un stock n'est pas le « coût de revient complet » du contrôle de gestion. Il comprend ce qu'il a fallu dépenser pour **fabriquer** le produit et l'amener **dans son état actuel**, dans des conditions **normales** d'activité :

> coût d'acquisition des matières consommées + charges directes de production + quote-part des charges indirectes **de production**, imputées sur la base de la **capacité normale**

Il exclut tout ce qui relève de l'**administration générale**, de la **vente**, du **financement**, du **stockage** des produits finis, des **gaspillages anormaux** et de la **sous-activité**.

### Question 1 — Les 11 postes

| # | Poste | Retenu | Montant retenu | Justification |
|---|---|---|---|---|
| 1 | Papier et carton | **Oui, hors tirage défectueux** | 19 940,00 – 880,00 = **19 060,00** | Matière consommée (CMUP). La gâche **normale** de calage reste incluse ; le tirage défectueux (erreur de plaque, tirage complet à refaire) est un **gaspillage anormal** |
| 2 | Encres, plaques, consommables | **Oui, hors tirage défectueux** | 2 265,00 – 105,00 = **2 160,00** | Idem |
| 3 | Façonnage sous-traité | **Oui** | **7 200,00** | Sous-traitance directe de production |
| 4 | Conception graphique de la gamme 2027 | **Oui** | **3 600,00** | Coût **directement attribuable** à la fabrication de ce lot (spécifique à la gamme 2027, sans usage au-delà) |
| 5 | Main-d'œuvre directe | **Oui, hors heures du tirage défectueux** | (538 – 18) × 38,50 = 520 × 38,50 = **20 020,00** | Charge directe ; les 18 h de réimpression relèvent du gaspillage anormal |
| 6 | Charges indirectes de l'atelier | **Oui, au taux normal et hors heures défectueuses** | (220 – 10) × 60,00 = 210 × 60,00 = **12 600,00** | Charges fixes de production imputées sur la base de la **capacité normale** (voir question 2) |
| 7 | Frais de direction, comptabilité, RH | **Non** | 0 | Frais d'administration générale, non liés à la production |
| 8 | Promotion auprès des libraires | **Non** | 0 | Frais commerciaux |
| 9 | Intérêts de l'emprunt de la presse | **Non** | 0 | Frais financiers (l'option d'incorporation ne vise que les stocks à cycle de production long ; un lot d'agendas fabriqué en deux mois n'est pas concerné) |
| 10 | Entrepôt de stockage des produits finis | **Non** | 0 | Stockage **après** l'achèvement de la production |
| 11 | Transport de livraison aux libraires | **Non** | 0 | Frais de distribution (coût de vente) — et il concerne des agendas **déjà vendus** |

### Question 2 — Imputation rationnelle et sous-activité

Les charges fixes de l'atelier (84 000 €) sont engagées quelle que soit l'activité. Si on les divise par l'activité **réelle** d'une période creuse (1 050 h), on obtient 80 €/h : chaque agenda « porte » une part des heures où la presse n° 2 était arrêtée faute de commandes. Ce coût de l'inactivité ne correspond à aucune valeur du produit : il doit rester en **charges de la période**.

> **Taux d'imputation rationnelle** = 84 000 / 1 400 h (capacité normale) = **60,00 €/h**
>
> **Charges fixes imputées aux productions** = 1 050 h × 60,00 = 63 000,00 €
>
> **Coût de la sous-activité** = 84 000,00 – 63 000,00 = **21 000,00 €** (soit 84 000 × (1 – 1 050 / 1 400) = 84 000 × 25 %) → **charge de l'exercice**, non stockée

Pour le lot d'agendas : 210 h × (80,00 – 60,00) = **4 200,00 €** de sous-activité que le calcul de Sabine avait incorporés.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 3 — Coût de production du lot

| Poste | Montant |
|---|---|
| Papier et carton (hors tirage défectueux) | 19 060,00 € |
| Encres, plaques, consommables (hors tirage défectueux) | 2 160,00 € |
| Façonnage sous-traité | 7 200,00 € |
| Conception graphique gamme 2027 | 3 600,00 € |
| Main-d'œuvre directe : 520 h × 38,50 € | 20 020,00 € |
| Charges indirectes atelier : 210 h × 60,00 € | 12 600,00 € |
| **Coût de production des 12 000 agendas bons** | **64 640,00 €** |

- Coût unitaire : 64 640,00 / 12 000 = **5,3867 €** (5,386666…) ;
- **Stock des 4 500 agendas** : 64 640,00 × 4 500 / 12 000 = **24 240,00 €** (on applique la proportion pour éviter l'arrondi du coût unitaire : 4 500 × 5,3867 = 24 240,15 €).

### Rapprochement avec le calcul de Sabine

| | Montant total du lot |
|---|---|
| Calcul de Sabine | 81 308,00 € |
| – Tirage défectueux : papier 880,00 + encres 105,00 + MO 18 h × 38,50 = 693,00 + charges atelier 10 h × 80,00 = 800,00 | – 2 478,00 € |
| – Sous-activité sur les heures bonnes : 210 h × (80,00 – 60,00) | – 4 200,00 € |
| – Frais administratifs | – 4 500,00 € |
| – Promotion | – 2 800,00 € |
| – Intérêts | – 640,00 € |
| – Stockage | – 900,00 € |
| – Transport de livraison | – 1 150,00 € |
| **= Coût de production retenu** | **64 640,00 €** |

Contrôle : 81 308,00 – 2 478,00 – 4 200,00 – 4 500,00 – 2 800,00 – 640,00 – 900,00 – 1 150,00 = 64 640,00 € ✔

### Question 4 — VNR et agendas 2026

**Agendas 2027** : VNR unitaire = 9,90 – 8 % × 9,90 (0,79) – 0,10 = **9,01 €** > 5,3867 € → **pas de dépréciation**. Les retours historiques (< 5 %) ne remettent pas en cause cette conclusion à l'échelle du lot : même si 5 % des 4 500 agendas restaient invendus, la VNR moyenne du lot resterait très supérieure à son coût. À revoir si les ventes de janvier-février 2027 décrochaient.

**Agendas 2026** : les 300 agendas restants n'ont **plus aucune valeur** au 31/12/2026 (année écoulée), pilonnés le 08/01/2027 : **valeur nulle**, ils ne figurent pas au stock final (pas de dépréciation à constater : ils sont exclus, avec la preuve du pilon et du recyclage du papier).

### Stock de produits finis et variation

| | Montant |
|---|---|
| Autres produits finis (papeterie de marque) | 38 150,00 € |
| Agendas 2027 (4 500) | 24 240,00 € |
| Agendas 2026 (300, pilonnés) | 0,00 € |
| **Stock final 355 au 31/12/2026** | **62 390,00 €** |
| Stock initial 355 au 31/12/2025 | 46 800,00 € |
| **Variation 7135 = SF – SI** | **+ 15 590,00 €** (créditrice) |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 7135 | Variation des stocks de produits | Annulation stock initial produits finis au 31/12/2025 | 46 800,00 | |
| 31/12/2026 | OD | 355 | Produits finis | Annulation stock initial produits finis au 31/12/2025 | | 46 800,00 |
| 31/12/2026 | OD | 355 | Produits finis | Stock final au 31/12/2026 : papeterie 38 150,00 + agendas 2027 24 240,00 | 62 390,00 | |
| 31/12/2026 | OD | 7135 | Variation des stocks de produits | Stock final produits finis au 31/12/2026 | | 62 390,00 |
| | | | | **Totaux** | **109 190,00** | **109 190,00** |

**Sens du 7135 (question 5)** : solde **créditeur** de 15 590,00 € = **production stockée** positive. L'imprimerie a produit en 2026 des biens qu'elle n'a pas encore vendus : leur coût (déjà en charges : papier, salaires, amortissements…) est neutralisé par ce produit, pour que les charges de production des agendas non vendus ne pèsent pas sur 2026. Le 7135 reste dans les **produits d'exploitation** (rubrique « production stockée »), même s'il était débiteur.

**Incidence de la correction (question 6)** : stock retenu 24 240,00 € au lieu de 30 510,00 € → production stockée et résultat inférieurs de **6 270,00 €** par rapport au calcul de Sabine. Ces 6 270,00 € ne sont pas « perdus » : ce sont des charges de 2026 (sous-activité, gâche anormale, frais administratifs, commerciaux, financiers) que le calcul initial reportait sur 2027.

## 4. Points d'attention / pièges

- **« Exhaustif » ≠ juste** : un coût de production complet « tout compris » surévalue le stock. Ce que le CAC teste, c'est précisément l'**exclusion** des frais non incorporables et le traitement de la **sous-activité**.
- **Capacité normale** : moyenne de plusieurs périodes, compte tenu de la maintenance prévue ; elle se **documente** (historique d'heures machine) et ne se fixe pas au gré du résultat recherché. En cas de **suractivité**, on retient l'activité réelle (taux plus bas), pour ne pas valoriser le stock au-dessus du coût réel.
- **Gaspillage anormal vs gâche normale** : la gâche de calage habituelle fait partie du coût ; un tirage entier raté et refait est anormal (le coût du tirage défectueux, 2 478,00 €, reste en charges).
- **Crédit-bail** : les redevances de la presse n° 1 sont une charge indirecte de production (location d'un outil de production) : elles entrent dans les 84 000 € et donc, au taux normal, dans le coût.
- **Agendas 2026** : produit **daté** → valeur nulle dès l'année écoulée ; la loi AGEC impose le réemploi ou le recyclage (pilon avec recyclage du papier : conforme).
- **Coût unitaire arrondi** : appliquez la proportion au coût total plutôt qu'un coût unitaire arrondi.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Note à Sabine Morel (copie au dossier CAC) :**

> Objet : coût de production des agendas Rhône Agenda 2027 en stock au 31/12/2026
>
> Bonjour Sabine,
>
> Nous avons repris le calcul du coût des agendas. Le coût de production retenu pour les stocks ne comprend que les coûts de **fabrication** dans des conditions **normales** d'activité :
> - **exclus** : frais de direction et de structure (4 500 €), promotion (2 800 €), intérêts (640 €), stockage (900 €), transport de livraison (1 150 €), ainsi que le tirage défectueux (2 478 €) ;
> - **charges de l'atelier** : imputées au taux de **60 €/h**, calculé sur la capacité normale de 1 400 h, et non au taux réel de 80 €/h. L'écart (sous-activité de novembre-décembre : 21 000 € pour l'atelier, dont 4 200 € sur ce lot) reste en charges de 2026.
>
> Coût de production du lot : 64 640 € (5,39 € par agenda) ; **stock des 4 500 agendas : 24 240 €** (au lieu de 30 510 €). Les 300 agendas 2026 pilonnés sont sortis à valeur nulle. La VNR (9,01 €) couvre largement le coût : pas de dépréciation.
>
> Pour l'audit, nous joignons le tableau de rapprochement, la fiche de l'atelier (capacité normale sur 3 ans) et le détail du tirage défectueux. Pourriez-vous nous transmettre l'historique des heures machine 2023-2025 qui justifie les 1 400 h ?
>
> Bien cordialement,

**Contrôles complémentaires :**
- appliquer la même méthode (taux normal, exclusions) aux **en-cours** de travaux d'impression pour les éditeurs au 31/12, s'il y en a ;
- vérifier la **permanence** : le coût des agendas 2026 (5,10 €) a-t-il été calculé de la même façon en 2025 ? Si la méthode change, information en annexe ;
- mentionner en annexe la méthode d'évaluation des stocks de produits finis (coût de production, imputation rationnelle).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié) : coût de production des stocks (charges directes et indirectes de production) ; exclusion des coûts de sous-activité, des gaspillages anormaux, des frais d'administration générale, des frais de stockage et des frais de commercialisation ; option pour l'incorporation des coûts d'emprunt aux actifs éligibles ; comptes 355, 7135.
- Code de commerce art. L. 123-18 (évaluation au coût de production) ; informations de l'annexe sur les méthodes d'évaluation (partie réglementaire du Code de commerce et PCG).
- CGI art. 38-3 (stocks au prix de revient) ; BOFiP, série BIC – produits et stocks : prix de revient des produits fabriqués et charges à exclure.
- Loi AGEC (n° 2020-105) : interdiction de l'élimination des invendus non alimentaires neufs, réemploi ou recyclage.
