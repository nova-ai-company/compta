# M08 — Stocks, en-cours et contrats à long terme

> **Objectif du module.** Savoir **compter**, **valoriser**, **déprécier** et **comptabiliser** les stocks et en-cours d'un client, quelle que soit son activité : matières premières d'une boulangerie, marchandises importées de Chine, véhicules d'occasion, médicaments, produits fabriqués par une imprimerie, études d'un architecte en cours, chantier de BTP à cheval sur deux exercices. Le stock est le poste où une erreur, même petite, passe **directement** dans le résultat — à l'euro près — et où les erreurs volontaires (« on gonfle un peu le stock cette année ») sont les plus faciles à commettre et les plus difficiles à voir.
>
> **Prérequis :** M01 (principes), M02 (achats, frais accessoires, FNP), M03 (ventes, factures à établir), M04 (TVA, notamment importations et TVA sur la marge).

!!! abstract "En clair — ce module en 5 idées"
    1. Le **stock**, c'est ce que l'entreprise a encore en réserve le jour de la clôture : farine, vêtements, pièces, médicaments. Exemple : la farine et le beurre de C01 Boulangerie Dupain au 31/12.
    2. Le stock final change **directement** le résultat : 1 € de stock en trop, c'est 1 € de bénéfice en trop. C'est pour cela qu'on le contrôle de près.
    3. On compte le stock **physiquement**, puis on lui donne une valeur : son coût d'achat ou de fabrication, **jamais** son prix de vente.
    4. Si un article ne pourra plus être vendu à son coût (périmé, démodé, abîmé), on enregistre une **dépréciation**, article par article. Exemple : les collections démodées de C09 Mode & Co, l'e-commerce de vêtements.
    5. Un travail commencé mais pas fini à la clôture (une étude, un chantier) se compte aussi : c'est un **en-cours**. Exemple : les chantiers de C02 Bâtisseurs du Sud ou les études de C13 Atelier Ligne.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Stock | Ce que l'entreprise possède pour le vendre ou le transformer | Luminaires de C19 Asia Trading |
    | Inventaire physique | Le comptage réel, sur place, de ce qui est en stock | Comptage du 31/12 |
    | Inventaire intermittent | On ne compte le stock qu'à la clôture ; les achats vont en charges toute l'année | C01 Boulangerie Dupain |
    | Inventaire permanent | Un logiciel suit le stock à chaque entrée et sortie | C12 Pharmacie Centrale |
    | Cut-off | Vérifier que chaque marchandise est rattachée au bon exercice (achat et vente) | Livraison du 31/12 facturée le 05/01 |
    | Coût d'acquisition | Prix d'achat + frais pour amener la marchandise (transport, douane) | Lampe 10 € + 2 € de frais |
    | Coût de production | Ce que coûte la fabrication : matières + main-d'œuvre + frais d'atelier | Agendas de C18 Imprimerie Graphique Rhône |
    | CMUP | Coût moyen : on fait la moyenne des prix d'achat | Lots achetés 8 € et 10 € |
    | FIFO (PEPS) | « Premier entré, premier sorti » : on vend d'abord les plus anciens | Les yaourts du fond d'abord |
    | Variation de stock | Écriture qui ajuste les charges ou les produits selon que le stock monte ou baisse | Compte 603 ou 713 |
    | VNR (valeur nette de réalisation) | Ce qu'on peut espérer tirer de la vente, moins les frais pour vendre | Prix soldé – frais de port |
    | Dépréciation | Perte de valeur constatée quand la VNR est inférieure au coût | Collection démodée |
    | En-cours | Travail commencé et pas terminé à la clôture, compté à son coût | Étude d'architecte à moitié faite |
    | Incoterm | Règle internationale qui dit à quel moment le risque passe du vendeur à l'acheteur | FOB, DAP, EXW |
    | Méthode à l'avancement | Pour un long chantier, on reconnaît le chiffre d'affaires au fur et à mesure | Chantier fait à 40 % |

---

## 1. Pourquoi le stock est un poste « à risque »

> 🟢 **En clair :** chez la plupart des clients, le stock n'est enregistré qu'une fois par an, à la clôture. Son montant fait donc monter ou baisser le bénéfice à l'euro près. C'est aussi le poste le plus facile à « arranger » : soyez vigilante.

Avec un **inventaire intermittent** (le cas de la quasi-totalité des PME du portefeuille), les achats de l'exercice sont passés **en charges** (601, 602, 607) et le stock n'est constaté qu'**à la clôture**. Le résultat dépend donc mécaniquement du stock final :

> **Consommation de l'exercice = Stock initial + Achats – Stock final**
>
> **Production stockée = Stock final de produits / en-cours – Stock initial**

Conséquences :
- **1 € de stock final en trop = 1 € de résultat en trop** (et de l'IS en plus, et un stock initial gonflé l'an prochain) ;
- une erreur de stock **s'inverse automatiquement l'exercice suivant** (le stock final N devient le stock initial N+1) : elle **déplace** du résultat entre deux exercices ;
- le stock est l'outil favori des « arrangements » : un dirigeant qui veut afficher un bénéfice à sa banque surévalue ; un dirigeant qui veut « payer moins d'impôt » sous-évalue ou déprécie à tort. Les deux sont des **inexactitudes** (art. L. 123-14 C. com., image fidèle) et la seconde est une cause classique de redressement.

> 💡 **Réflexe senior :** avant même d'ouvrir l'inventaire, calculez le **taux de marge** (ou le ratio matières / CA) de l'exercice et comparez-le aux exercices précédents et au secteur. Un taux de marge qui bondit de 4 points « sans raison » signale presque toujours un stock final surévalué (ou des achats manquants).

---

## 2. L'inventaire physique

> 🟢 **En clair :** une fois par an au moins, le client doit compter réellement son stock. Votre rôle : exiger un comptage bien organisé et vérifier que les achats et les ventes autour de la date de clôture sont rattachés au bon exercice. Exemple : un carton reçu le 31/12 chez C19 Asia Trading dont la facture n'arrive qu'en janvier.

### 2.1 L'obligation

Tout commerçant doit, **au moins une fois tous les douze mois**, contrôler par inventaire l'existence et la valeur des éléments de son patrimoine (Code de commerce, art. L. 123-12). Pour les stocks, cela signifie un **comptage physique** (quantités) puis une **valorisation** (prix unitaire × quantité), documentés, datés et **signés par le dirigeant**.

| Système | Principe | Exemples du portefeuille |
|---|---|---|
| **Inventaire intermittent** | Comptage à la clôture ; achats en charges ; stock constaté par variation de stock | Boulangerie Dupain (C01), Mode & Co (C09), Asia Trading (C19) |
| **Inventaire permanent** (logiciel de gestion de stock) | Le stock est suivi en quantités et en valeur à chaque mouvement ; le comptage physique **contrôle** le stock théorique | Pharmacie Centrale (C12) via son logiciel d'officine |
| **Inventaire tournant** | Comptage par familles tout au long de l'année, chaque article au moins une fois par an ; admis si l'inventaire permanent est fiable | Pièces détachées du Garage Martin (C03) |

### 2.2 L'organisation d'un inventaire (ce que le cabinet doit exiger)

1. **Avant** : instruction écrite (date, heure, équipes, zones), rangement, mise à l'écart et étiquetage des articles **n'appartenant pas** à l'entreprise (dépôt de tiers, biens de clients en réparation, marchandises déjà vendues non enlevées) et des articles **abîmés / périmés / obsolètes**.
2. **Pendant** : **gel des mouvements** (ou enregistrement des entrées/sorties pendant le comptage), équipes de deux (un compteur, un contrôleur), **feuilles de comptage pré-numérotées** (on les rend toutes, même vierges), unité de compte précisée (sac, carton, pièce, kg), recomptage par sondage.
3. **Le cut-off (séparation des exercices)** : noter le **numéro du dernier bon de réception** (entrées) et du **dernier bon de livraison** (sorties) avant le comptage. Ce sont eux qui permettent ensuite de vérifier que :
   - tout ce qui est **dans le stock compté** a son **achat** comptabilisé (facture ou FNP) ;
   - tout ce qui est **sorti** du stock a sa **vente** comptabilisée (facture ou facture à établir) ;
   - rien n'est compté deux fois (en stock **et** déjà vendu).
4. **Après** : valorisation, rapprochement stock physique / stock théorique (si inventaire permanent), analyse des **écarts** (démarque), signature du dirigeant, conservation des feuilles de comptage (pièces justificatives).

| Situation au cut-off | Stock | Achat / vente | Écriture de régularisation |
|---|---|---|---|
| Marchandise **reçue et comptée**, facture fournisseur **non reçue** | Inclus | Achat manquant | **FNP** : D 60x + 44586 / C 408 |
| Facture fournisseur **reçue et comptabilisée**, marchandise **non reçue** (et pas encore à nos risques) | Exclu | Achat en trop | **CCA** : D 486 / C 60x |
| Marchandise **livrée au client** (sortie du stock), facture **non émise** | Exclu | Vente manquante | **Facture à établir** : D 4181 / C 70x + 44587 |
| Facture client **émise et comptabilisée**, marchandise **non livrée** (encore à nos risques) | **Inclus** (si comptée ; à ajouter sinon) | Vente en trop | **PCA** : D 70x / C 487 |

> ⚠️ **Erreur classique :** traiter le cut-off « par les factures ». C'est **le mouvement physique** (et le transfert du contrôle et des risques) qui commande, pas la date de la facture. La date de la facture n'est qu'un indice.

> 💡 **Réflexe senior :** assistez (ou faites assister un collaborateur) à l'inventaire physique des clients à stock significatif (Pharmacie, Garage, Asia Trading, Imprimerie). Dix minutes dans l'entrepôt valent dix heures de révision : on voit les palettes de « fins de séries » au fond, les véhicules en dépôt-vente sur le parc, les produits périmés dans le bac.

---

## 3. Le coût d'entrée des stocks

> 🟢 **En clair :** un stock se valorise à ce qu'il a coûté, pas à ce qu'il rapportera. Pour un bien acheté : prix + transport + douane. Pour un bien fabriqué : matières + main-d'œuvre + frais d'atelier, sans les frais de bureau ni de vente.

### 3.1 Coût d'acquisition (biens achetés : marchandises, matières, approvisionnements)

| Inclus | Exclus |
|---|---|
| Prix d'achat **net** des remises, rabais, ristournes (et des escomptes de règlement obtenus, en principe) | TVA récupérable |
| **Droits de douane** et autres taxes non récupérables | **Frais de stockage** postérieurs à la réception (sauf s'ils sont nécessaires au processus de production) |
| **Frais de transport**, d'assurance transport, de manutention jusqu'à l'entrepôt | **Frais administratifs** généraux, frais commerciaux |
| Commissions d'achat, honoraires du transitaire (dédouanement) | **Frais financiers** (agios, intérêts du crédit documentaire) — sauf option pour les coûts d'emprunt sur les stocks à cycle de production long |
| Autres coûts **directement attribuables** à l'acquisition | **Écarts de change** constatés au paiement (666 / 766) ou à la clôture (476 / 477) |

Les achats en devises sont convertis au **cours du jour de l'opération** ; ce coût historique en euros n'est **jamais** réévalué ensuite (les stocks sont des éléments non monétaires).

> 💡 **Réflexe senior :** que l'entreprise comptabilise ses frais accessoires **par nature** (6241 transports sur achats, droits de douane en 607/608…) ou **incorporés** au compte d'achat, **le coût du stock les inclut toujours**. C'est la valorisation de l'inventaire qui doit les intégrer, pas seulement la comptabilité générale.

### 3.2 Coût de production (biens produits : produits finis, en-cours, produits intermédiaires)

> **Coût de production = coût d'acquisition des matières consommées + charges directes de production + quote-part des charges indirectes de production « raisonnablement » rattachables**

| Inclus | Exclus |
|---|---|
| Matières et fournitures consommées (valorisées au CMUP ou FIFO) | **Coût de la sous-activité** (charges fixes non absorbées par une activité inférieure à la normale) |
| Main-d'œuvre directe (salaires **chargés**) | **Gaspillages anormaux** (matières, main-d'œuvre, rebuts anormaux) |
| Sous-traitance directe (façonnage, études incorporées) | **Frais d'administration générale** (direction, comptabilité, siège) non liés à la production |
| Charges indirectes de **production** : amortissements des machines, redevances de crédit-bail de production, énergie, maintenance, encadrement de l'atelier, contrôle qualité | **Frais commerciaux** et de distribution (publicité, représentants, transport de livraison) |
| | **Frais de stockage** des produits finis |
| | **Frais financiers** (sauf option, cycle long) |

**L'imputation rationnelle des charges fixes.** Les charges fixes de production sont incorporées sur la base de la **capacité normale** de production :

> Taux d'imputation = Charges fixes de production ÷ **Activité normale** (et non activité réelle)
>
> **Sous-activité** = Charges fixes × (1 – activité réelle ÷ activité normale) → **reste en charges** de l'exercice, n'entre pas dans le stock.
>
> En cas de **suractivité**, on retient l'activité réelle (le coût unitaire ne doit pas être gonflé, mais pas non plus artificiellement réduit en dessous du coût réel).

> ⚠️ **Erreur classique :** calculer le coût de production en divisant **toutes les charges de l'atelier** par la production réelle d'une période creuse. On « stocke » la sous-activité : le stock est surévalué et la perte de l'exercice est reportée sur le suivant.

**Coûts simplifiés admis** : coût standard ou méthode du prix de détail (commerce de détail), à condition que les résultats soient proches du coût réel et révisés régulièrement.

---

## 4. Les méthodes de valorisation des sorties et du stock final

> 🟢 **En clair :** quand on achète le même article à des prix différents, il faut choisir quel prix retenir pour le stock. Deux méthodes sont permises : le coût moyen (CMUP) ou « premier entré, premier sorti » (FIFO). Pour des biens uniques, comme les voitures de C03 Garage Martin, on garde le coût réel de chacun.

Pour des **biens fongibles** (interchangeables), on ne peut pas identifier le coût de chaque unité. Deux méthodes sont admises (PCG, règles d'évaluation des biens fongibles ; CGI art. 38-3 pour l'évaluation fiscale) :

| Méthode | Principe | Effet en période de hausse des prix |
|---|---|---|
| **CMUP après chaque entrée** | Après chaque entrée : (valeur du stock + valeur de l'entrée) ÷ (quantités) ; les sorties sont valorisées à ce coût jusqu'à l'entrée suivante | Stock final intermédiaire |
| **CMUP de période** (mois, trimestre, exercice) | (Stock initial + entrées de la période) ÷ quantités totales | Plus simple, mais les sorties ne sont valorisées qu'en fin de période |
| **FIFO / PEPS** (premier entré, premier sorti) | Les sorties consomment les lots les plus anciens ; le stock final est valorisé aux **derniers** coûts | Stock final le plus élevé (proche des prix récents) |
| ~~**LIFO / DEPS**~~ (dernier entré, premier sorti) | **Interdit** en comptes individuels en France (et fiscalement) | — |

- Les **biens identifiables** (véhicules d'occasion, œuvres, chantiers) sont valorisés à leur **coût réel individuel** (pas de CMUP sur des voitures !).
- Le « **dernier prix d'achat** » utilisé par beaucoup de petits commerces n'est qu'une **approximation du FIFO**, acceptable si la rotation est rapide et les prix stables — à documenter.
- **Permanence des méthodes** (M01) : on ne change pas de méthode pour « arranger » le résultat ; un changement doit être justifié (meilleure information) et expliqué en annexe.

> 💡 **Réflexe senior :** le CMUP se calcule **par référence** (par article). Un CMUP « global » du stock d'un importeur qui vend des lampes à 8 € et à 80 € ne veut rien dire.

---

## 5. La variation de stock : les écritures (et leur sens)

> 🟢 **En clair :** à la clôture, on retire l'ancien stock et on inscrit le nouveau. Pour les biens achetés, l'écart passe en 603 (dans les charges) ; pour les biens produits, en 713 (dans les produits). Si le stock augmente, le résultat augmente.

### 5.1 Biens achetés (matières, approvisionnements, marchandises)

| Écriture | Débit | Crédit |
|---|---|---|
| Annulation du **stock initial** | **603x** Variation des stocks | **31 / 32 / 37** |
| Constatation du **stock final** | **31 / 32 / 37** | **603x** Variation des stocks |

Comptes : **6031** (matières premières), **6032** (autres approvisionnements), **6037** (marchandises).

> **Solde du 603x = Stock initial – Stock final.** Solde **débiteur** si le stock **baisse** (on a consommé plus qu'on n'a acheté → charge supplémentaire) ; solde **créditeur** si le stock **augmente** (une partie des achats n'est pas consommée → diminution des charges). Le 603 reste **dans les charges** (en négatif s'il est créditeur), il ne passe jamais en produits.

### 5.2 Biens et services produits (en-cours, produits finis)

| Écriture | Débit | Crédit |
|---|---|---|
| Annulation du **stock initial** | **713x** Variation des stocks (en-cours, produits) | **33 / 34 / 35** |
| Constatation du **stock final** | **33 / 34 / 35** | **713x** |

Comptes : **7133** (en-cours de production de biens), **7134** (en-cours de production de services), **7135** (produits finis et intermédiaires).

> **Solde du 713x = Stock final – Stock initial.** Solde **créditeur** si le stock **augmente** (production stockée positive) ; **débiteur** s'il baisse. Le 713 reste **dans les produits** (« production stockée »), même négatif.

> ⚠️ **Erreur classique :** inverser la logique entre 603 et 713. Retenez : **603 = charges = SI – SF** ; **713 = produits = SF – SI**. Une augmentation de stock **diminue les charges** (603 créditeur) ou **augmente les produits** (713 créditeur) — dans les deux cas, elle **augmente le résultat**.

### 5.3 Récapitulatif des comptes

| Stock | Compte de stock | Variation | Dépréciation |
|---|---|---|---|
| Matières premières | 31 | 6031 | 391 |
| Autres approvisionnements (matières et fournitures consommables, emballages) | 32 (321, 322, 326) | 6032 | 392 |
| En-cours de production de biens (produits en cours, travaux en cours) | 33 (331, 335) | 7133 | 393 |
| En-cours de production de services (études en cours, prestations en cours) | 34 (341, 345) | 7134 | 394 |
| Produits (intermédiaires, finis, résiduels) | 35 (351, 355, 358) | 7135 | 395 |
| Marchandises | 37 | 6037 | 397 |
| Stocks en voie d'acheminement, mis en dépôt ou donnés en consignation | 38 (ou sous-comptes des 31 à 37) | selon la nature | selon la nature |

---

## 6. La dépréciation des stocks

> 🟢 **En clair :** si un article ne pourra plus être vendu au moins à son coût, on constate la perte. On le fait article par article, avec des preuves, jamais par un pourcentage « au jugé ». Exemple : des médicaments bientôt périmés chez C12 Pharmacie Centrale.

### 6.1 Principe

À la clôture, on compare **coût d'entrée** et **valeur actuelle** — pour un stock, la **valeur nette de réalisation (VNR)** :

> **VNR = prix de vente estimé dans le cours normal de l'activité – coûts estimés pour achever le bien – coûts estimés nécessaires pour réaliser la vente** (commissions, frais de port non refacturés, préparation, garantie, frais d'enchères, **TVA sur la marge** pour un bien vendu sous ce régime…)

Si **VNR < coût** → **dépréciation** de la différence, **article par article** (ou par catégorie homogène), jamais globalement « par prudence ». Pour des matières destinées à être incorporées dans des produits dont la vente reste rentable, on ne déprécie pas la matière du seul fait de la baisse de son cours.

> 🟢 **En clair :** demandez-vous « combien va-t-on vraiment récupérer en vendant cet article, une fois les frais de vente payés ? ». Si c'est moins que ce qu'il a coûté, la différence est une dépréciation.

| Écriture | Débit | Crédit |
|---|---|---|
| Reprise de la dépréciation N-1 | **39x** | **7817** Reprises sur dépréciations des actifs circulants |
| Dotation de la dépréciation N | **6817** Dotations aux dépréciations des actifs circulants | **39x** |

(Le cabinet peut aussi ne passer que la **différence** nette ; la présentation « reprise totale + dotation totale » est plus lisible et facilite le relevé des provisions.)

Les informations **postérieures à la clôture** qui **confirment** une situation existant à la clôture (prix des soldes de janvier, offre d'un soldeur, vente à perte en octobre) **doivent** être utilisées (M09, événements postérieurs).

### 6.2 Quand déprécier ? Indices à rechercher

- articles **périmés** ou à péremption courte (Pharmacie Centrale, C12 ; Boulangerie, C01) ;
- **collections démodées**, fins de séries (Mode & Co, C09) ;
- **rotation lente** : véhicule d'occasion invendu depuis plus de 6 mois (Garage Martin, C03), diesel ancien face aux ZFE ;
- articles abîmés, retournés défectueux ;
- **baisse du prix de vente** (concurrence, soldes, offre d'un destockeur) ;
- coût de revient gonflé (sous-activité « stockée » par erreur — à corriger dans le coût, pas par une dépréciation).

> ⚠️ **Erreur classique :** une dépréciation **forfaitaire** (« 30 % sur tout le stock de plus d'un an ») sans justification statistique propre à l'entreprise. Comptablement, c'est une provision « pour lisser » ; fiscalement, elle est **réintégrée** (une dépréciation n'est déductible que si elle est justifiée, chiffrée avec une précision suffisante et constatée en comptabilité — CGI art. 39-1-5°). Une méthode statistique fondée sur **l'historique réel des ventes de l'entreprise** est en revanche admise.

### 6.3 Produits à détruire et loi AGEC

- Un produit **périmé, à détruire** n'a plus de valeur : on le **sort** de l'inventaire (valeur nulle) ou on le déprécie à 100 %, et l'on conserve la **preuve de destruction** (procès-verbal, bon d'enlèvement) — c'est elle que demandera un vérificateur.
- Depuis la loi « anti-gaspillage pour une économie circulaire » (AGEC), la **destruction des invendus non alimentaires neufs** est en principe interdite : ils doivent être donnés, réemployés ou recyclés. Les **dons** de stocks à des associations éligibles peuvent ouvrir droit à la réduction d'impôt mécénat (CGI art. 238 bis), calculée sur le **coût de revient** du stock donné.

---

## 7. Biens qui ne sont pas « là où ils devraient être »

> 🟢 **En clair :** ce qui compte, c'est à qui appartient la marchandise, pas où elle se trouve. Une voiture déposée par un particulier sur le parc de C03 Garage Martin n'est pas au garage. Un conteneur sur un bateau peut déjà appartenir à C19 Asia Trading.

### 7.1 Stocks en dépôt, en consignation, en dépôt-vente

**Règle** : le stock appartient à celui qui en a la **propriété** (et en pratique le contrôle et les risques), **peu importe où il se trouve physiquement**.

| Situation | Chez le propriétaire (déposant) | Chez le dépositaire |
|---|---|---|
| Marchandises **mises en dépôt** chez un revendeur, un client (dépôt-vente, consignation) | **Dans son stock** (compte 38 ou sous-compte), sur la base d'une **attestation** du dépositaire à la clôture | **Hors stock** (information éventuelle en engagements) |
| Biens d'un **client** confiés pour transformation ou réparation | Dans le stock du client | **Hors stock** (à isoler lors du comptage) |
| Véhicule d'un particulier en **dépôt-vente** sur le parc d'un garage | Patrimoine du particulier | **Hors stock** du garage (la commission seule est un produit) |

> 💡 **Réflexe senior :** dans la lettre de demande de documents de clôture, ajoutez systématiquement : « Avez-vous des marchandises chez des tiers ? Détenez-vous des biens appartenant à des tiers ? ». Et exigez une **attestation de stock** des dépositaires au jour de la clôture.

### 7.2 Marchandises en transit et Incoterms

Les **Incoterms** (règles ICC, version 2020) fixent le point de **transfert des risques** et la **répartition des frais** entre vendeur et acheteur. Ils ne règlent **pas** à eux seuls le transfert de **propriété**, qui dépend du contrat (clause expresse, réserve de propriété) et du droit applicable. En pratique, on lit **le contrat** (conditions générales d'achat / de vente) et, s'il est muet, on retient le **transfert des risques** comme indice du transfert du contrôle — en le documentant.

> 🟢 **En clair :** pour une marchandise en route au 31/12, lisez d'abord le contrat. S'il ne dit rien, regardez l'Incoterm : celui qui supporte le risque si le bateau coule est, en pratique, celui qui a la marchandise dans son stock.

| Groupe | Incoterms | Risques transférés à l'acheteur… | Marchandise en transit au 31/12 : chez qui en stock ? |
|---|---|---|---|
| **E** | EXW (à l'usine) | dès la mise à disposition chez le vendeur | **Acheteur** |
| **F** | FCA, FAS, **FOB** | à la remise au transporteur / **à bord du navire** au port d'embarquement | **Acheteur** dès le chargement |
| **C** | CFR, **CIF**, CPT, CIP | à bord / à la remise au premier transporteur (le vendeur paie le fret, mais les risques sont déjà transférés) | **Acheteur** dès le chargement |
| **D** | **DAP**, DPU, **DDP** | à l'arrivée au lieu convenu | **Vendeur** jusqu'à l'arrivée |

> ⚠️ **Erreur classique :** croire que « CIF » veut dire « le vendeur supporte le risque jusqu'à destination ». En CIF, le vendeur paie le fret et l'assurance, **mais les risques passent à l'acheteur au chargement**.

Le coût d'une marchandise en transit appartenant à l'acheteur comprend le prix d'achat et les frais **déjà engagés** (fret payé en FOB…). Les droits de douane et la TVA à l'importation (autoliquidée) ne naîtront qu'au dédouanement.

**Clause de réserve de propriété** : elle ne retarde **pas** la comptabilisation de la vente ni l'entrée en stock chez l'acheteur : le bien est inscrit chez l'**acheteur** dès la livraison (information en annexe pour les montants significatifs).

### 7.3 Stocks agricoles

Animaux, avances aux cultures, produits de la récolte, option pour la valorisation des animaux reproducteurs : règles propres au secteur agricole → **voir le module M13** (EARL Ferme du Val, C15).

---

## 8. Les en-cours de production de services

> 🟢 **En clair :** une mission commencée mais pas finie à la clôture a de la valeur : on l'inscrit en stock, au coût du temps passé, sans marge. Une phase terminée mais pas encore facturée, elle, se traite en facture à établir, au prix de vente. Exemple : les études de C13 Atelier Ligne au 30/09.

Une prestation **commencée mais non achevée** à la clôture (et non facturable) est un **en-cours de production de services** (compte **34** : 341 Études en cours, 345 Prestations de services en cours ; variation **7134**). C'est le cas typique d'un cabinet d'architecture (Atelier Ligne, C13) qui facture par phases.

| Situation à la clôture | Traitement |
|---|---|
| Phase **achevée** (livrée, acceptée), **non facturée** | **Facture à établir** au prix de vente : D 4181 / C 706 + 44587 |
| Phase **commencée**, non achevée, non facturable | **En-cours** au **coût de production** (temps passé × coût horaire de revient de production) : D 34 / C 7134 |
| Phase **non commencée** | Rien |
| **Acompte** reçu sur une phase en cours | Reste en **4191** (dette) ; **jamais compensé** avec l'en-cours (principe de non-compensation) |

- Le coût horaire de revient = rémunérations **chargées** des intervenants (y compris celle des dirigeants rémunérés dans une société à l'IS) + quote-part des charges **de production** (logiciels métier, matériel, locaux de production) ; **sans** les frais administratifs et commerciaux. On ne valorise **jamais** un en-cours au **taux facturé** (ce serait constater une marge non réalisée).
- **Plafond** : l'en-cours est déprécié (394) si **coût engagé > honoraires attendus de la phase – coûts restant à engager** (ou si le client a suspendu / contesté la mission).
- Pour un **entrepreneur individuel** à l'IR, le temps de l'exploitant n'est pas une charge : il ne se valorise pas dans l'en-cours.

> ⚠️ **Erreur classique :** confondre « phase terminée non facturée » (facture à établir, **avec marge**, au prix de vente) et « phase commencée » (en-cours, **sans marge**, au coût).

---

## 9. Les contrats à long terme

> 🟢 **En clair :** un chantier qui dure plus d'un exercice ne doit pas faire apparaître tout son bénéfice d'un coup à la fin. Avec la méthode à l'avancement, on reconnaît le chiffre d'affaires et la marge au fur et à mesure. Et si le chantier va perdre de l'argent, on enregistre toute la perte dès qu'on le sait. Exemple : les chantiers de C02 Bâtisseurs du Sud.

### 9.1 Définition et méthodes

Un **contrat à long terme** est un contrat d'une durée généralement longue, **spécifiquement négocié** pour la réalisation d'un bien, d'un service ou d'un ensemble (un ouvrage de BTP, un logiciel sur mesure, une étude importante), dont l'exécution **s'étend sur au moins deux exercices**. Deux méthodes :

| | **Méthode à l'avancement** (préférentielle) | **Méthode à l'achèvement** |
|---|---|---|
| Chiffre d'affaires | Constaté au fur et à mesure : **prix total × % d'avancement** | Constaté **à la réception** (livraison) seulement |
| Charges | En charges au fur et à mesure | Stockées en **en-cours** (335) au coût de production jusqu'à l'achèvement |
| Marge | Dégagée **au prorata de l'avancement** | Dégagée **entièrement à la fin** |
| Condition | Le **résultat à terminaison** doit pouvoir être estimé de façon **fiable** (prix, coûts totaux, avancement) | Utilisable si l'avancement n'est pas choisi, ou si l'estimation fiable est impossible |
| Changement | **Achèvement → avancement** : possible (méthode préférentielle) | **Avancement → achèvement** : **interdit** (on ne quitte pas une méthode préférentielle) |

**Mesure de l'avancement** : rapport **coûts engagés / coûts totaux estimés** (le plus courant), mesures physiques (m³ coulés, étages), jalons contractuels. Avec la méthode des coûts, on **exclut** des coûts engagés ceux qui ne représentent pas du travail exécuté : **matériaux livrés sur chantier mais non mis en œuvre** (ils restent en **stock**), acomptes versés aux sous-traitants pour des travaux non réalisés.

> 🟢 **En clair :** le plus souvent, on mesure l'avancement en comparant ce qu'on a déjà dépensé au coût total prévu. Mais des matériaux livrés sur le chantier et pas encore posés ne comptent pas : ils n'ont pas fait avancer le travail.

**Prix total** = prix contractuel + **avenants signés** + réclamations ou révisions de prix dont l'acceptation est **probable** ; une réclamation contestée par le client n'entre **pas** dans le prix (prudence).

### 9.2 Écritures à la clôture (méthode à l'avancement)

Les situations de travaux facturées en cours d'année sont en 704 / 706. À la clôture, on **ajuste** le chiffre d'affaires facturé au chiffre d'affaires à l'avancement :

| Situation | Écriture |
|---|---|
| CA à l'avancement **>** CA facturé | **Facture à établir** : D 4181 / C 704 (+ C 44587 pour la TVA) |
| CA à l'avancement **<** CA facturé | **Produit constaté d'avance** : D 704 / C 487 |

### 9.3 La perte à terminaison

Dès qu'il est **probable** que le coût total du contrat dépassera le prix total, la **perte à terminaison est constatée en totalité, immédiatement** (prudence), quelle que soit la méthode :

> **Provision pour perte à terminaison = perte totale prévue – perte déjà constatée par l'avancement**
>
> (À l'avancement, la perte déjà constatée = perte totale × % d'avancement ; à l'achèvement, la perte s'impute d'abord en **dépréciation des en-cours** (393), le surplus en provision.)

| Écriture | Débit | Crédit |
|---|---|---|
| Dotation | **6815** Dotations aux provisions d'exploitation | **151** Provisions pour risques — sous-compte « pertes sur contrats » (*subdivision selon la nomenclature 2025 du PCG*) |
| Reprise (à l'avancement suivant ou à l'achèvement) | 151 | **7815** |

> 💡 **Réflexe senior :** le budget de chantier **révisé à la date de clôture** est la pièce maîtresse. Exigez-le signé par le conducteur de travaux ou le dirigeant, avec les coûts engagés rapprochés de la comptabilité analytique. Sans budget fiable, pas d'avancement fiable.

### 9.4 Fiscalement

Les travaux en cours sont évalués au **coût de revient** (CGI art. 38-3) et les produits sont en principe rattachés à l'**achèvement** des prestations (CGI art. 38-2 bis) ; la méthode à l'avancement retenue en comptabilité est **admise fiscalement** pour les contrats à long terme (vérifiez la doctrine BOFiP en vigueur, série BIC – base imposable / stocks). La **provision pour perte à terminaison** est en principe **déductible** si la perte est probable et nettement précisée à la clôture (CGI art. 39-1-5°) — point à documenter et à valider avec Hélène Ferrand avant la liasse.

> 🟢 **En clair :** côté impôt, la méthode à l'avancement est en principe acceptée, et la perte prévue sur un chantier est en principe déductible si elle est probable et chiffrée. Dans tous les cas, gardez les justificatifs et faites valider avant la liasse.

---

## 10. Les factures à établir (418 / 4181)

> 🟢 **En clair :** quand une vente est faite (bien livré, service rendu) mais que la facture n'est pas encore émise, on l'enregistre quand même à la clôture. On l'annule au début de l'exercice suivant, quand la vraie facture arrive.

Le compte **4181 « Clients – factures à établir »** enregistre, à la clôture, les ventes de biens **livrés** ou de services **rendus** dont la facture n'est pas encore émise (y compris l'ajustement à l'avancement d'un contrat à long terme). La TVA est créditée en **44587 « TVA sur factures à établir »**.

- Écriture **extournée** à l'ouverture de l'exercice suivant ; la facture définitive est ensuite saisie normalement.
- **TVA sur les encaissements** (prestations de services, travaux immobiliers sans option pour les débits) : la TVA n'est pas exigible tant que le prix n'est pas encaissé ; le 44587 la « met en attente » et ne doit pas être reporté sur la CA3 de décembre.
- **Ne pas confondre** : 4181 (vente acquise, facture à émettre) ≠ **34 / 33** (prestation ou travaux en cours, valorisés au coût) ≠ **487** (facturé d'avance).

---

## 11. Erreurs d'inventaire découvertes après la clôture

> 🟢 **En clair :** si l'erreur est trouvée avant que les comptes soient arrêtés, on corrige simplement. Si elle est trouvée plus tard, on la corrige dans l'exercice où on la découvre, et on l'explique en annexe si elle est importante.

| Moment de la découverte | Traitement |
|---|---|
| **Avant l'arrêté des comptes** de l'exercice concerné | On **corrige** l'inventaire et l'écriture de stock de cet exercice |
| **Après l'approbation** des comptes (exercice suivant) | **Correction d'erreur** : impact dans le **résultat de l'exercice de découverte** (le stock initial erroné se « corrige » mécaniquement par la variation de stock), **information en annexe** si significatif (règles du PCG sur les changements comptables et corrections d'erreurs, modifiées par le règlement ANC n° 2022-06 — le classement en résultat exceptionnel n'est plus le réflexe : à apprécier selon la définition restreinte) |

Fiscalement, si l'exercice erroné n'est pas prescrit, l'entreprise peut **corriger sa déclaration** (réclamation pour un stock surévalué ; déclaration rectificative spontanée pour un stock sous-évalué). Si l'erreur affecte le bilan d'ouverture du **premier exercice non prescrit**, joue la règle de **correction symétrique des bilans** (CGI art. 38-4 bis).

> 🟢 **En clair :** pour l'impôt, une erreur de stock sur une année encore contrôlable peut être corrigée en déposant une déclaration corrigée. Pour les erreurs plus anciennes, une règle spéciale s'applique : signalez-la à votre responsable.

---

## 12. Checklist de fin de module

- [ ] J'exige une instruction d'inventaire, des feuilles numérotées, signées, et les numéros des derniers BL d'entrée et de sortie.
- [ ] Je fais le cut-off par les **mouvements physiques** : FNP, CCA, facture à établir, PCA.
- [ ] Je valorise au **coût d'acquisition** (prix net + douane + transport + transitaire), sans stockage, frais financiers ni écart de change.
- [ ] Je calcule un **CMUP après chaque entrée** et un **FIFO**, et je sais que le **LIFO est interdit**.
- [ ] Je calcule un **coût de production** en excluant **sous-activité**, gaspillage anormal, frais administratifs, commerciaux, de stockage et financiers.
- [ ] Je passe la variation de stock **dans le bon sens** : 603 = SI – SF ; 713 = SF – SI.
- [ ] Je calcule une **VNR** (prix de vente – coûts d'achèvement – coûts de vente, y compris TVA sur la marge) et je déprécie article par article (391 à 397, 6817 / 7817).
- [ ] Je refuse une dépréciation forfaitaire non justifiée.
- [ ] J'inclus les stocks **en dépôt chez des tiers** (attestation) et j'exclus les biens **de tiers**.
- [ ] Je détermine, selon le **contrat et l'Incoterm**, qui détient une marchandise en transit au 31/12.
- [ ] Je valorise un **en-cours de services** au coût (jamais au taux facturé) et je le distingue d'une facture à établir.
- [ ] J'applique la **méthode à l'avancement**, j'exclus les matériaux non mis en œuvre, je constate la **perte à terminaison en totalité**.
- [ ] Je sais traiter une **erreur d'inventaire** découverte après la clôture (comptable et fiscal).

---

## 13. Exercices du module

| N° | Client | Thème | Difficulté |
|---|---|---|---|
| E08-01 | C01 Boulangerie Dupain | Inventaire des matières premières, fiche d'inventaire erronée, variation de stock, FNP | ★☆☆ |
| E08-02 | C19 Asia Trading | Coût d'acquisition d'importations (douane, transport, transitaire) et CMUP des luminaires | ★★☆ |
| E08-03 | C19 Asia Trading | Marchandises en transit au 31/12 : FOB, DAP, EXW ; cut-off ; écarts de conversion | ★★★ |
| E08-04 | C09 Mode & Co | Dépréciation des collections démodées, VNR, refus du forfait | ★★☆ |
| E08-05 | C03 Garage Martin | Stock de VO au 30/09 : coût, VNR avec TVA sur la marge, dépôt-vente, acompte | ★★★ |
| E08-06 | C12 Pharmacie Centrale | Inventaire au 30/09 : démarque, périmés, péremption courte, dépréciation | ★★☆ |
| E08-07 | C18 Imprimerie Graphique Rhône | Coût de production des agendas : sous-activité, gâche anormale, charges exclues | ★★★ |
| E08-08 | C13 Atelier Ligne | En-cours de production de services au 30/09, facture à établir, mission suspendue | ★★☆ |
| E08-09 | C02 Bâtisseurs du Sud | Chantiers à cheval : avancement, perte à terminaison, refus de passer à l'achèvement | ★★★ |
| E08-10 | C24 Menuiserie Bois & Création | Corner cases : erreur d'inventaire N-1, stock en dépôt, bois confié, cut-off BL / factures | ★★★ |

---

## À retenir en 30 secondes

- 1 € de stock final en trop = 1 € de bénéfice en trop : le stock se contrôle toujours de près.
- Le stock se compte physiquement au moins une fois par an, et chaque achat ou vente est rattaché au bon exercice.
- On valorise au **coût** (achat ou fabrication), jamais au prix de vente ; le LIFO est interdit.
- 603 = stock initial – stock final (charges) ; 713 = stock final – stock initial (produits).
- On déprécie article par article quand la valeur de revente nette est inférieure au coût, jamais au forfait.
- Ce qui compte, c'est à qui appartient la marchandise, pas l'endroit où elle se trouve.
- En-cours = au coût, sans marge ; phase finie non facturée = facture à établir ; perte prévue sur un chantier = constatée tout de suite.
