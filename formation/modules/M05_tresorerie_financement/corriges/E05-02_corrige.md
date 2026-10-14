# Corrigé E05-02 — La caisse du Petit Zinc est créditrice

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-02](../exercices/E05-02_caisse-creditrice-petit-zinc.md)

## 1. Analyse

**Pourquoi c'est impossible.** La caisse représente des billets et des pièces physiquement présents. On ne peut pas sortir plus d'espèces qu'il n'y en a : un solde **créditeur**, même un seul jour, prouve que la comptabilité ne reflète pas la réalité — soit une recette n'a pas été enregistrée, soit une sortie a été enregistrée à tort (en double, ou alors qu'elle a été payée par un autre moyen).

**Conséquences en contrôle fiscal.** Une caisse créditrice est l'argument classique pour déclarer la comptabilité **non probante** (irrégulière et non sincère) : le vérificateur peut alors **écarter la comptabilité** et **reconstituer le chiffre d'affaires** (méthode des vins, des couverts, des achats revendus…), avec charge de la preuve inversée en pratique. Pour un restaurant, c'est un risque majeur.

**Méthode de diagnostic.** On remonte au **premier jour créditeur** (15/09) et on examine tout ce qui précède, puis chaque sortie de caisse : était-elle réellement payée en espèces ? était-elle déjà enregistrée ailleurs ? Puis on vérifie que **chaque jour d'ouverture a son Z** (mardi → samedi).

### Anomalies identifiées

| # | Anomalie | Preuve | Effet sur le 530 |
|---|---|---|---|
| 1 | **Z n° 2440 du samedi 12/09 non saisi** (la numérotation passe de 2439 à 2441) | Pièce 3 ; le samedi 12/09 est un jour d'ouverture | Recette espèces manquante : **+ 698,40** |
| 2 | **Remise du 15/09 enregistrée deux fois** : une fois depuis le bordereau (580/530) et une fois lors de l'import bancaire, où le stagiaire a affecté la contrepartie en 530 au lieu de 580 | Pièce 2 (ligne du 16/09) | Sortie en double : **+ 1 500,00** ; le 580 reste débiteur de 1 500,00 |
| 3 | **Facture Metro payée par CB**, saisie en sortie de caisse | Pièce 5 (ticket CB), pièce 2 (import du 09/09 : 401 / 512) | Sortie inexistante : **+ 342,18** ; le fournisseur Metro est soldé deux fois (401 débiteur de 342,18) |
| 4 | **Paiement en espèces de 1 440,58 € à la Cave des Canuts** (1 450 € remis, 9,42 € rendus) | Pièce 4 | Pas d'erreur de saisie sur le principe, mais montant à vérifier (voir § 4) et **infraction au plafond de 1 000 €** |
| 5 | **Avance de 200 € à un extra** | Grand livre | Sortie réelle, mais à régulariser en paie (§ 5) |

Les anomalies 1 à 3 suffisent à expliquer la caisse créditrice ; l'anomalie 4 est un sujet réglementaire.

> Point fin sur l'anomalie 4 : le grand livre enregistre une sortie de 1 450,00 €, alors que la dette réglée est de 1 440,58 € (9,42 € de monnaie rendue). La sortie de caisse **nette** est 1 440,58 € ; la saisie à 1 450,00 € crée un faux manquant de 9,42 € et laisse le fournisseur débiteur de 9,42 €. À corriger.

## 2. Calculs

### 2.1 Solde corrigé

| Élément | Montant |
|---|---|
| Solde comptable au 30/09 (pièce 1) | 1 158,82 |
| + Z n° 2440 espèces | + 698,40 |
| + Annulation du doublon de remise du 15/09 | + 1 500,00 |
| + Annulation de la sortie Metro (payée par CB) | + 342,18 |
| + Monnaie rendue Cave des Canuts | + 9,42 |
| **Solde corrigé au 30/09/2026** | **3 708,82** |

### 2.2 Vérification : le solde corrigé n'est jamais créditeur
En réintégrant les corrections à leur date, le point bas du mois devient le **15/09 après la remise : 395,90 € débiteur** (855,32 + 698,40 + 342,18 + 9,42 – 1 500,00 = 405,32 avec la correction Canuts ; 395,90 sans elle). Tous les soldes journaliers sont désormais débiteurs ✔.

### 2.3 Comparaison avec le comptage

| | Montant |
|---|---|
| Solde comptable corrigé | 3 708,82 |
| Comptage physique du 30/09 (Hugo) | 3 687,00 |
| **Manquant** | **21,82** |

Un manquant de 21,82 € sur un mois de recettes espèces d'environ 10 000 € reste dans l'ordre de grandeur d'erreurs de rendu de monnaie : on le constate en charge, mais on le **signale** (s'il devient récurrent, ce n'est plus un écart, c'est un problème).

### 2.4 TVA et CA du Z n° 2440
- TVA 10 % : 2 214,30 / 1,10 = 2 013,00 HT ; TVA 201,30.
- TVA 20 % : 632,00 / 1,20 = 526,67 HT ; TVA 105,33.
- Contrôle : 2 013,00 + 201,30 + 526,67 + 105,33 = 2 846,30 ✔ = 698,40 + 1 973,90 + 174,00 ✔.

Le Z manquant n'était pas seulement un problème de caisse : **2 539,67 € de CA HT et 306,63 € de TVA collectée** manquaient dans la comptabilité (et donc potentiellement dans la CA3 de septembre, à vérifier avant dépôt).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 12/09/2026 | VT | 530 | Caisse | Z n° 2440 du 12/09 — espèces | 698,40 | |
| 12/09/2026 | VT | 4672 | Transit encaissements CB (compte du dossier) | Z n° 2440 — CB | 1 973,90 | |
| 12/09/2026 | VT | 4673 | Titres-restaurant à rembourser (compte du dossier) | Z n° 2440 — TR | 174,00 | |
| 12/09/2026 | VT | 7061 | Prestations restauration — TVA 10 % | Z n° 2440 | | 2 013,00 |
| 12/09/2026 | VT | 7062 | Ventes boissons alcoolisées — TVA 20 % | Z n° 2440 | | 526,67 |
| 12/09/2026 | VT | 445712 | TVA collectée 10 % | Z n° 2440 | | 201,30 |
| 12/09/2026 | VT | 445711 | TVA collectée 20 % | Z n° 2440 | | 105,33 |
| 16/09/2026 | OD | 530 | Caisse | Annulation doublon remise bord. 0915 (affectation import erronée) | 1 500,00 | |
| 16/09/2026 | OD | 580 | Virements internes | Annulation doublon remise bord. 0915 | | 1 500,00 |
| 08/09/2026 | OD | 530 | Caisse | Annulation sortie Metro 0189-4456 réglée par CB | 342,18 | |
| 08/09/2026 | OD | 401METRO | Fournisseur Metro | Annulation sortie Metro (double règlement) | | 342,18 |
| 05/09/2026 | OD | 530 | Caisse | Monnaie rendue Cave des Canuts CV-2611 | 9,42 | |
| 05/09/2026 | OD | 401CANUTS | Fournisseur Cave des Canuts | Monnaie rendue CV-2611 | | 9,42 |
| 30/09/2026 | CA | 658 | Charges diverses de gestion courante (écart de caisse — *subdivision selon la nomenclature 2025 du PCG*) | Manquant de caisse au comptage du 30/09 | 21,82 | |
| 30/09/2026 | CA | 530 | Caisse | Manquant de caisse au comptage du 30/09 | | 21,82 |
| | | | | **Totaux** | **4 719,72** | **4 719,72** |

Contrôles après écritures :
- 530 : 1 158,82 + 698,40 + 1 500,00 + 342,18 + 9,42 – 21,82 = **3 687,00 €** = comptage ✔
- 580 : soldé (le débit de 1 500,00 laissé par le bordereau 0915 est compensé) ✔
- 401 Metro : soldé ✔ ; 401 Cave des Canuts : soldé à 1 440,58 ✔

> Les comptes 4672/4673 sont des comptes de transit du plan du dossier : la remise CB du 12/09 (qui figure dans la remise globale du relevé) et le remboursement des titres viendront les solder. Vérifiez au passage que la remise CB correspondante a bien été lettrée.

## 4. Points d'attention / pièges

### Le paiement de la Cave des Canuts : infraction au plafond
- Entre professionnels, le paiement en espèces d'une **même dette** est plafonné à **1 000 €** (C. mon. fin., art. L. 112-6 et D. 112-3). Ici : 1 440,58 €.
- Sanction : amende fiscale pouvant aller jusqu'à **5 % des sommes indûment réglées en espèces**, dont le débiteur et le créancier sont **solidairement** responsables (CGI, art. 1840 J) — soit jusqu'à environ 72 € ici. Le montant est faible, le **signal** ne l'est pas : un fournisseur de vins qui propose une remise « pour paiement en liquide » doit alerter (risque de minoration de recettes chez le fournisseur, et suspicion sur la traçabilité des achats de boissons du restaurant — précisément la base de la « méthode des vins » de reconstitution du CA).
- On ne fractionne pas la facture en deux paiements pour passer sous le plafond.

### Les autres pièges
- **L'import bancaire affecté en 530** : l'erreur classique. Toute remise d'espèces passe par le **580** des deux côtés ; un 580 non soldé en fin de mois signale exactement ce type de doublon.
- **Tickets CB saisis en caisse** : c'est le moyen de paiement qui détermine le journal, pas le fait que la facture a été « donnée à la caisse ».
- **Monnaie rendue** : on enregistre la sortie nette.
- **Z manquant** : contrôlez la **continuité de numérotation** des Z et le **grand total perpétuel** du logiciel certifié. Un Z manquant = du CA et de la TVA manquants.

### L'avance à l'extra
L'avance de 200 € à M. Diallo est une **avance sur salaire** (425 Personnel – avances et acomptes) : elle doit apparaître sur son bulletin de paie (retenue « acompte »), avec un reçu signé. Vérifiez en paie : un extra payé « en partie en espèces hors bulletin » est un risque de travail dissimulé. À noter aussi : le paiement des salaires en espèces est limité (art. L. 3241-1 C. trav., seuil à vérifier) ; une avance ponctuelle de 200 € reste admissible si elle est tracée.

## 5. Ce qu'un senior ferait en plus

**Message à Clara (WhatsApp, puis confirmé par e-mail) :**
> « Bonjour Clara, la caisse est réglée : il manquait le Z du samedi 12/09 (photo reçue, merci), une remise d'espèces avait été enregistrée deux fois et un ticket Metro payé par carte avait été passé en caisse. Après corrections, l'écart avec le comptage d'Hugo n'est que de 21,82 €.
> En revanche, pour la Cave des Canuts : la loi interdit de payer en espèces plus de 1 000 € à un professionnel pour une même facture. L'amende (jusqu'à 5 % du montant) peut viser le Petit Zinc comme le fournisseur. Merci de régler désormais leurs factures par virement ou carte — la remise de 3 % n'en vaut pas la peine. Et pensez à nous envoyer la photo de **chaque** Z, même le samedi. Bonne soirée ! »

**Contrôles à mettre en place :**
- Contrôle mensuel automatique : séquence des Z sans trou + caisse jamais créditrice + 580 soldé.
- Billetage signé **chaque fin de mois** (pas seulement quand le cabinet le demande).
- Rapprochement trimestriel achats de boissons / ventes de boissons (ratio de marge) : c'est le premier contrôle d'un vérificateur dans la restauration.
- Rappel à l'équipe (stagiaire) sur l'affectation des imports « VERSEMENT ESPECES » → 580.

**Documentation** : note dans le dossier de travail (anomalies, corrections, échange avec Clara) — utile si un contrôle porte un jour sur cet exercice.

## 6. Références
- CGI, art. 286, I-3° bis (logiciels de caisse sécurisés) et art. 1770 duodecies (amende).
- Code monétaire et financier, art. L. 112-6 et D. 112-3 (plafond de paiement en espèces) ; CGI, art. 1840 J (sanction).
- Code du travail, art. L. 3241-1 (paiement des salaires).
- LPF : procédure de rectification et reconstitution du chiffre d'affaires en cas de comptabilité non probante (principe général).
- PCG : comptes 530, 580, 425, 658/758 (*nomenclature 2025*).
