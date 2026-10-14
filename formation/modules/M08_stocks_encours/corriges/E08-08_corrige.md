# Corrigé E08-08 — En-cours de production de services de l'Atelier Ligne au 30/09

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-08](../exercices/E08-08_encours-services-atelier-ligne.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Qualifier chaque situation

La facturation par phases fixe la règle : une phase est **facturable** quand elle est **achevée et remise** au client. À la clôture :

| Mission / phase | Situation au 30/09/2026 | Qualification | Valorisation |
|---|---|---|---|
| A — Perrin, PRO | Commencée le 01/09, remise prévue le 15/11 | **En-cours** de production de services | Au **coût** |
| A — Perrin, ESQ / APS / APD | Achevées et facturées | Rien (déjà en CA) | — |
| B — Les Quais, DCE | **Achevée et remise** le 25/09, non facturée | **Facture à établir** | Au **prix de vente** (10 % × 54 000 = 5 400 € HT) |
| B — Les Quais, DET | Non commencée | Rien | — |
| C — Gerland, APS | Commencée, **suspendue** le 27/09 par le client | **En-cours**, à tester (valeur recouvrable) | Au coût, plafonné |
| D — Vasseur, ESQ | Commencée le 22/09 | **En-cours** | Au coût |

> ⚠️ La différence est essentielle : la phase **achevée** (DCE des Quais) a été **gagnée** : on constate le produit **avec sa marge**. La phase **commencée** n'a rien rapporté tant qu'elle n'est pas remise : on « met en stock » **ses coûts**, sans marge.

### Question 2 — Le coût horaire de revient de production

Un en-cours se valorise au **coût de production** : coûts directs (rémunérations chargées des intervenants) + quote-part des charges **de production** (logiciels, matériel, locaux de conception). On exclut les **frais administratifs et commerciaux** (9,00 €/h), comme pour tout stock.

| Intervenant | Coût direct / h | Charges de production / h | **Coût de revient de production / h** |
|---|---|---|---|
| Camille Fabre (cogérante) | 60,00 | 7,00 | **67,00 €** |
| Nicolas Brun (cogérant) | 60,00 | 7,00 | **67,00 €** |
| Léa Moulin (architecte) | 40,00 | 7,00 | **47,00 €** |
| Hugo Petit (dessinateur) | 28,00 | 7,00 | **35,00 €** |

La rémunération des cogérants est une charge de la SARL à l'IS (quel que soit leur statut social) : leur temps entre dans le coût. *(Chez un architecte en entreprise individuelle à l'IR, le temps de l'exploitant ne serait pas valorisé.)*

**Pourquoi pas 95 €/h ?** Le taux facturé contient la **marge** du cabinet et la couverture des frais administratifs et commerciaux. Valoriser un en-cours au prix de vente revient à constater un bénéfice sur une prestation **non achevée et non acceptée** : c'est contraire au principe de prudence et au principe de réalisation (un produit n'est acquis qu'à l'achèvement de la prestation).

### Question 3 — Le test de valeur recouvrable

L'en-cours ne peut pas être maintenu à une valeur supérieure à ce que la phase rapportera **net des coûts restant à engager** :

> Valeur recouvrable = honoraires de la phase – coût de revient des heures restant à faire

**Mission C — Gerland** : le client a suspendu le projet le 27/09 ; au 30/09, la suspension n'a pas encore 3 mois, mais l'issue la plus probable est soit l'abandon (honoraires au prorata, art. 9), soit une relance incertaine. On retient le scénario **recouvrable de façon certaine** : le prorata de 70 % de l'APS, soit 70 % × 8 000 = **5 600 € HT**, le client étant solvable. Remarque : même en cas de relance, la phase serait déficitaire — 8 895 € de coûts déjà engagés pour 8 000 € d'honoraires. La dépréciation est donc **certaine** dans son principe ; seul son montant dépend du scénario.

## 2. Calculs (détaillés, chaque montant justifié)

### En-cours au coût

**Mission A — Perrin, PRO (honoraires de la phase : 20 % × 36 000 = 7 200 € HT)**

| Intervenant | Heures | Taux | Coût |
|---|---|---|---|
| Camille | 22 | 67,00 | 1 474,00 |
| Léa | 30 | 47,00 | 1 410,00 |
| Hugo | 64 | 35,00 | 2 240,00 |
| **En-cours** | 116 h | | **5 124,00 €** |

Reste à faire : 6 × 67 + 10 × 47 + 30 × 35 = 402 + 470 + 1 050 = 1 922,00 € → valeur recouvrable = 7 200,00 – 1 922,00 = **5 278,00 €** ≥ 5 124,00 € → **pas de dépréciation** (marge attendue sur la phase : 7 200 – 5 124 – 1 922 = 154 € : très faible, à surveiller).

**Mission C — Gerland, APS (honoraires de la phase : 10 % × 80 000 = 8 000 € HT)**

| Intervenant | Heures | Taux | Coût |
|---|---|---|---|
| Camille | 40 | 67,00 | 2 680,00 |
| Nicolas | 35 | 67,00 | 2 345,00 |
| Léa | 60 | 47,00 | 2 820,00 |
| Hugo | 30 | 35,00 | 1 050,00 |
| **En-cours** | 165 h | | **8 895,00 €** |

Valeur recouvrable : 70 % × 8 000 = 5 600,00 € → **dépréciation = 8 895,00 – 5 600,00 = 3 295,00 €**.

**Mission D — Vasseur, ESQ (honoraires de la phase : 5 % × 24 000 = 1 200 € HT)**

| Intervenant | Heures | Taux | Coût |
|---|---|---|---|
| Nicolas | 6 | 67,00 | 402,00 |
| Hugo | 10 | 35,00 | 350,00 |
| **En-cours** | 16 h | | **752,00 €** |

Reste à faire : 4 × 35 = 140,00 € → valeur recouvrable = 1 200,00 – 140,00 = 1 060,00 € ≥ 752,00 € → pas de dépréciation.

### Synthèse

| Mission | En-cours brut | Dépréciation | En-cours net |
|---|---|---|---|
| A — Perrin PRO | 5 124,00 | — | 5 124,00 |
| C — Gerland APS | 8 895,00 | 3 295,00 | 5 600,00 |
| D — Vasseur ESQ | 752,00 | — | 752,00 |
| **Total** | **14 771,00** | **3 295,00** | **11 476,00** |

**Variation 7134** = SF – SI = 14 771,00 – 9 450,00 = **+ 5 321,00 €** (créditrice).

**Facture à établir — DCE des Quais** : 10 % × 54 000 = 5 400,00 € HT ; TVA 20 % = 1 080,00 € ; TTC **6 480,00 €**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 7134 | Variation des en-cours de production de services | Annulation en-cours au 30/09/2025 | 9 450,00 | |
| 30/09/2026 | OD | 341 | Études en cours | Annulation en-cours au 30/09/2025 | | 9 450,00 |
| 30/09/2026 | OD | 341 | Études en cours | En-cours au 30/09/2026 : Perrin PRO 5 124 / Gerland APS 8 895 / Vasseur ESQ 752 | 14 771,00 | |
| 30/09/2026 | OD | 7134 | Variation des en-cours de production de services | En-cours au 30/09/2026 (au coût de production) | | 14 771,00 |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation en-cours Gerland APS (mission suspendue) | 3 295,00 | |
| 30/09/2026 | OD | 394 | Dépréciations des en-cours de production de services | Dépréciation en-cours Gerland APS | | 3 295,00 |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | SCI Les Quais de Saône — DCE remis le 25/09/2026 | 6 480,00 | |
| 30/09/2026 | OD | 706 | Prestations de services | DCE Les Quais (10 % de 54 000) | | 5 400,00 |
| 30/09/2026 | OD | 44587 | TVA sur factures à établir | TVA 20 % DCE Les Quais — exigible à l'encaissement | | 1 080,00 |
| | | | | **Totaux** | **33 996,00** | **33 996,00** |

Au 01/10/2026 : extourne de la facture à établir ; la facture émise en octobre sera saisie normalement. Les écritures d'en-cours ne s'extournent pas : elles seront reprises par la variation de stock du 30/09/2027.

**TVA (question 4)** : Atelier Ligne acquitte la TVA **sur les encaissements** (prestations de services, pas d'option pour les débits). La TVA de la facture à établir n'est donc **pas exigible** au 30/09 : elle est « en attente » en 44587 et ne figure pas sur la CA3 de septembre ; elle sera exigible lors de l'encaissement de la facture. Les en-cours, valorisés au coût, ne portent **aucune TVA**.

## 4. Points d'attention / pièges

- **Question 5 — Acompte Perrin** : l'acompte de 2 500 € HT reçu sur la phase PRO est une **dette** envers le client (4191) tant que la phase n'est pas remise ; l'en-cours (5 124 €) est un **actif**. Le **principe de non-compensation** (Code de commerce art. L. 123-19) interdit de les compenser : au bilan, l'en-cours figure à l'actif, l'acompte au passif (« avances et acomptes reçus sur commandes en cours »). La TVA de 500 € a été justement acquittée à l'encaissement.
- **En-cours ≠ facture à établir** : le DCE des Quais, achevé, ne doit pas être valorisé au coût en en-cours (on perdrait la marge acquise) ; la PRO Perrin, non achevée, ne doit pas être en facture à établir (on anticiperait une marge non acquise).
- **Mission suspendue** : la suspension est connue avant la clôture (27/09) : la perte de valeur existe au 30/09 → dépréciation. Si le client confirme l'abandon avant l'arrêté des comptes, la facturation du prorata (5 600 €) deviendra une créance ; s'il relance le projet, on réexaminera la dépréciation.
- **Feuilles de temps** : sans feuilles de temps fiables par mission et par phase, il n'y a pas d'en-cours justifiable. C'est la première pièce à exiger.
- **Fiscalement**, les en-cours sont évalués au coût de revient (CGI art. 38-3) ; la dépréciation de l'en-cours Gerland est déductible si elle est justifiée (courrier du client, contrat, estimation de l'avancement).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — Écart avec la proposition de Camille** : 297 h (116 + 165 + 16) × 95 € = **28 215,00 €**, contre un en-cours net retenu de **11 476,00 €** : écart de **16 739,00 €** de résultat (et d'IS) anticipé à tort.

**Réponse à Camille :**

> Bonjour Camille,
>
> Merci pour les feuilles de temps, elles sont très claires.
> - **En-cours** : nous devons les valoriser à ce que les heures vous **coûtent** (rémunérations chargées et frais de l'atelier de conception, soit 67 €/h pour vous et Nicolas, 47 €/h pour Léa, 35 €/h pour Hugo), et non au taux facturé : la marge ne se constate que lorsque la phase est remise. Vos en-cours au 30/09 s'élèvent à 14 771 €.
> - **Gerland** : la suspension du 27/09 nous oblige à limiter l'en-cours à ce que le client vous devra au minimum (70 % de l'APS, soit 5 600 €). Nous constatons une dépréciation de 3 295 €. Si le projet repart, nous la reprendrons. Pensez à adresser dès maintenant à Gerland Office un courrier rappelant l'article 9 du contrat et l'état d'avancement (70 %).
> - **DCE des Quais** : remis le 25/09, il est acquis sur cet exercice : nous l'enregistrons en facture à établir (5 400 € HT). Merci d'émettre la facture rapidement — la TVA ne sera due qu'à l'encaissement.
>
> Au passage, la phase PRO Perrin ne dégagera qu'environ 150 € de marge si le reste à faire est respecté : à suivre de près.
>
> Bien cordialement,

**Contrôles et documentation :**
- tableau de suivi des missions (honoraires par phase, état d'avancement, temps passé, reste à faire) rapproché des feuilles de temps et de la facturation ;
- vérifier que **toutes** les phases remises avant le 30/09 sont facturées ou en facture à établir (balayage des e-mails de remise de documents) ;
- conserver : contrat Gerland (art. 9), courrier de suspension, note d'avancement de Nicolas ;
- calcul du coût horaire de revient à **mettre à jour chaque année** (rémunérations, heures productives réelles) et à appliquer de manière permanente.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié) : coût de production (exclusion des frais d'administration générale et de commercialisation) ; comptes 341, 394, 4181, 44587, 4191, 7134 ; dépréciation des actifs circulants (6817).
- Code de commerce art. L. 123-19 (non-compensation) et L. 123-21 (seuls les bénéfices réalisés peuvent être inscrits).
- CGI art. 38-2 bis (rattachement des produits de prestations de services à l'achèvement) et 38-3 (évaluation des travaux en cours au prix de revient) ; art. 269-2-c (exigibilité de la TVA sur les prestations de services à l'encaissement).
