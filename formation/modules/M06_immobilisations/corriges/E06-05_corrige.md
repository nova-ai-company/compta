# Corrigé E06-05 — Le tracteur détruit en novembre, l'indemnité payée en février

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-05](../exercices/E06-05_sinistre-tracteur-transports-leroy.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — Le bien n'existe plus au 31/12/2026.** Un actif détruit ne procure plus d'avantages économiques : il **sort** du bilan à la date du sinistre, quelle que soit la date d'indemnisation. Continuer à l'amortir sur toute l'année (proposition de Théo) laisse à l'actif un camion qui est à la casse.

**Étape 2 — Le rattachement de l'indemnité (question 2).** On se pose trois questions :

| Question | Réponse au 31/12/2026 | Pièce |
|---|---|---|
| Le **fait générateur** est-il antérieur à la clôture ? | Oui : accident du 14/11/2026 | Constat, déclaration |
| Le **principe** de l'indemnisation est-il acquis à la clôture ? | Oui : l'assureur a reconnu le 05/12/2026 que le sinistre relève de la garantie « dommages tous accidents » | Pièce 2 |
| Le **montant** peut-il être estimé de façon fiable ? | Oui : rapport d'expert du 10/12/2026 (VRADE 78 000 €) et franchise contractuelle de 2 000 € connue | Pièces 3 et contrat |

Le courrier du 22/01/2027 est un **événement postérieur à la clôture** qui **confirme** une situation existant au 31/12/2026 (droit à indemnité déjà né, montant déjà déterminable) : il doit être pris en compte dans les comptes 2026. Le paiement du 15/02/2027 n'est qu'un **dénouement de trésorerie**. Conclusion : **produit à recevoir de 76 000 € en 2026**, présenté comme un produit de cession (775) puisqu'il compense la disparition de l'immobilisation (position retenue par le cabinet).

**Étape 3 — Les frais de remorquage (question 3).** La facture est une **charge** de 2026 (TVA déductible : elle est au nom de Transports Leroy). Le remboursement par l'assureur (1 850 €, hors taxes) ne passe plus par un compte de transfert de charges (791 supprimé par le règlement ANC n° 2022-06) : on le comptabilise **en diminution de la charge** concernée (produit à recevoir en contrepartie). Résultat : charge nette nulle.

**Étape 4 — La Laiterie (question 3).** Leroy a reconnu sa responsabilité avant la clôture : l'obligation existe au 31/12/2026. L'assureur indemnise **directement** le client de 5 400 € et Leroy ne doit que la **franchise de 1 000 €** → **charge à payer** de 1 000 € en 2026. (Si l'assureur avait payé Leroy, qui aurait indemnisé le client, on aurait constaté une dette de 6 400 € et une créance de 5 400 € **sans compensation** au bilan.)

**Étape 5 — TVA.** L'indemnité d'assurance n'est la contrepartie d'aucune livraison ou prestation : elle est **hors champ** de la TVA. L'assureur l'a calculée **hors taxes** car Leroy récupère la TVA (il rachètera un tracteur avec TVA déductible). La remise de l'épave à l'assureur est intégrée à l'indemnité ; elle ne donne pas lieu à une facture de cession distincte dans ce schéma (épave = sauvetage abandonné à l'assureur).

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---:|
| Annuité | 132 000 / 6 | 22 000,00 |
| Cumul au 31/12/2025 | 2023 : 6 mois = 11 000 ; 2024 et 2025 : 44 000 | 55 000,00 |
| Durée 2026 jusqu'au sinistre | 10 mois × 30 j + 14 j = 314 jours | |
| **Dotation 2026** | 22 000 × 314/360 | **19 188,89** |
| Cumul au 14/11/2026 | 55 000 + 19 188,89 | 74 188,89 |
| **VNC** | 132 000 – 74 188,89 | **57 811,11** |
| Indemnité (775) | 78 000 – 2 000 | **76 000,00** |
| **Résultat de la sortie** | 76 000 – 57 811,11 | **+ 18 188,89** |

Fiscalement (IS), la plus-value de 18 188,89 € est imposable en 2026 au taux de droit commun, au même titre qu'une plus-value de cession (l'indemnité d'assurance est assimilée à un prix de cession). Des dispositifs d'étalement ciblés existent pour certaines indemnités : *à vérifier, non appliqués ici*.

**Question 5 — Écart avec la proposition de Théo (résultat 2026)**

| Poste | Théo | Correct |
|---|---:|---:|
| Dotation 2026 du tracteur | 22 000,00 | 19 188,89 |
| VNC sortie (675) | 0,00 | 57 811,11 |
| Indemnité (775) | 0,00 | – 76 000,00 |
| Remorquage (net du remboursement) | 1 850,00 | 0,00 |
| Franchise marchandises | 0,00 | 1 000,00 |
| **Charges nettes 2026** | **23 850,00** | **2 000,00** |

→ La proposition de Théo **sous-évalue le résultat 2026 de 21 850,00 €**, laisse à l'actif un bien détruit (VNC 55 000 € au bilan de Théo) et reporterait en 2027 un produit de 77 850 € qui appartient à 2026. Le coût économique réel du sinistre pour Leroy est bien de **2 000 € de franchise dommages + 1 000 € de franchise marchandises**, le « gain » comptable de 18 188,89 € traduisant simplement le fait que le camion valait plus sur le marché que sa VNC.

Contrôle : 19 188,89 + 57 811,11 – 76 000 + 1 000 = 2 000,00 ✓.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 14/11/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | GK-731-LR dotation 2026 (314 j) | 19 188,89 | |
| 14/11/2026 | OD | 28182 | Amortissements du matériel de transport | GK-731-LR | | 19 188,89 |
| 14/11/2026 | OD | 28182 | Amortissements du matériel de transport | Sortie GK-731-LR (sinistre 26-11-03977) | 74 188,89 | |
| 14/11/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | Sortie GK-731-LR — VNC | 57 811,11 | |
| 14/11/2026 | OD | 2182 | Matériel de transport | Sortie GK-731-LR | | 132 000,00 |
| 20/11/2026 | AC | 6248 | Transports divers (remorquage) | DAPL-26-0912 remorquage + gardiennage | 1 850,00 | |
| 20/11/2026 | AC | 44566 | TVA sur autres biens et services | DAPL-26-0912 | 370,00 | |
| 20/11/2026 | AC | 401 | Fournisseur Dépannage Alpes PL | DAPL-26-0912 | | 2 220,00 |
| 15/12/2026 | BQ | 401 | Fournisseur Dépannage Alpes PL | Règlement DAPL-26-0912 | 2 220,00 | |
| 15/12/2026 | BQ | 512 | Banque | Règlement DAPL-26-0912 | | 2 220,00 |
| 31/12/2026 | OD | 658 | Charges diverses de gestion courante – litiges clients (subdivision selon la nomenclature 2025 du PCG) | Franchise marchandises LV-26-44107 | 1 000,00 | |
| 31/12/2026 | OD | 4686 | Charges à payer | Franchise due à la Laiterie des Monts du Lyonnais | | 1 000,00 |
| 31/12/2026 | OD | 4687 | Produits à recevoir | Mutuelle des Transporteurs — sinistre 26-11-03977 | 77 850,00 | |
| 31/12/2026 | OD | 775 | Produits des cessions d'éléments d'actif | Indemnité VRADE 78 000 – franchise 2 000 | | 76 000,00 |
| 31/12/2026 | OD | 6248 | Transports divers (remorquage) | Remboursement remorquage par l'assureur | | 1 850,00 |
| 10/02/2027 | BQ | 4686 | Charges à payer | Règlement franchise Laiterie | 1 000,00 | |
| 10/02/2027 | BQ | 512 | Banque | Règlement franchise Laiterie | | 1 000,00 |
| 15/02/2027 | BQ | 512 | Banque | Virement Mutuelle des Transporteurs | 77 850,00 | |
| 15/02/2027 | BQ | 4687 | Produits à recevoir | Encaissement indemnité sinistre 26-11-03977 | | 77 850,00 |
| | | | | **Totaux** | **313 328,89** | **313 328,89** |

En 2027, à la réouverture, on n'extourne **pas** le 4687 (ce n'est pas une estimation reprise d'office) : il est soldé par l'encaissement. Si l'on utilise un sous-compte « créance sur assureur » (468x), même logique.

## 4. Points d'attention / pièges

- **Ne pas compenser** la VNC (675) et l'indemnité (775) en une seule ligne de « résultat de sinistre » : le PCG impose la présentation brute (et le 2054 / tableau des immobilisations doit montrer la sortie).
- **Courrier de l'assureur après la clôture** : il **confirme** une situation existante → on ajuste. À l'inverse, un événement **nouveau** postérieur (nouveau sinistre en janvier 2027) ne s'ajuste pas : information en annexe s'il est significatif.
- **Indemnité inférieure à la VNC** : la perte apparaît naturellement (675 > 775) ; aucune dépréciation préalable n'est à constater pour un bien déjà sorti.
- **Question 6 — garantie contestée** : si l'assureur conteste le principe même de sa garantie, l'indemnité est un **actif éventuel** : **aucun produit** n'est comptabilisé en 2026. La sortie du bien (VNC en 675) reste obligatoire. On mentionne en annexe le litige si son issue favorable est probable et significative ; on ne constate le produit que lorsque le droit est acquis (accord, décision de justice définitive). En parallèle, si des pénalités ou un refus de prise en charge des marchandises exposent Leroy à payer l'intégralité du préjudice de la Laiterie (6 400 €), la charge ou provision correspondante doit être constatée (prudence : asymétrie entre actif éventuel et passif probable).
- **Véhicule en crédit-bail** : si le tracteur avait été financé en crédit-bail, il ne figurerait pas à l'actif ; l'indemnité serait en principe versée au crédit-bailleur (propriétaire), et Leroy devrait analyser l'indemnité de résiliation du contrat — schéma très différent (module M05).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Documentation du dossier de révision** : conserver dans la feuille de travail « immobilisations » la chronologie (accident, reconnaissance de garantie, rapport d'expert, proposition, accord, encaissement) avec les copies : c'est ce qui justifie le rattachement à 2026 auprès du commissaire aux comptes éventuel ou d'un vérificateur.

**Contrôles complémentaires**
- Vérifier que la **carte carburant** et le **badge télépéage** du GK-731-LR sont désactivés et que le véhicule est retiré de la liste **TICPE** et de la déclaration de **taxe à l'essieu**.
- Vérifier la date de fin de la garantie et le **remplacement** du véhicule : location courte durée de remplacement (charge), commande d'un nouveau tracteur (acompte en 238).
- Contrôler que le contrat flotte n'est plus facturé pour ce véhicule (prime à régulariser).

**Mail à Bruno Leroy**

> Bonjour Monsieur Leroy,
>
> Nous avons finalisé le traitement du sinistre du tracteur GK-731-LR. Le camion sort du bilan au 14 novembre 2026 et l'indemnité de 76 000 € est rattachée à 2026, l'assureur ayant reconnu sa garantie et l'expert ayant chiffré la perte avant la clôture. Comptablement, l'opération fait apparaître un gain de 18 189 €, car le camion valait davantage que sa valeur dans les comptes : ce gain est imposable à l'IS en 2026. Le coût réel du sinistre se limite aux franchises (2 000 € sur le véhicule, 1 000 € sur la marchandise de la Laiterie).
>
> Pour le remplacement du tracteur, merci de nous transmettre le bon de commande dès sa signature, en particulier si vous versez un acompte.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : sortie des immobilisations ; produits à recevoir ; événements postérieurs à la clôture (ajustement si la situation existait à la clôture) ; suppression des comptes de transfert de charges (règlement ANC n° 2022-06).
- Code de commerce, art. L. 123-21 (seuls les bénéfices réalisés peuvent être inscrits) et principe de prudence (art. L. 123-20) ; distinction actif éventuel / passif probable.
- CGI, art. 38-2 (rattachement des créances acquises), art. 39 duodecies et s. (plus-values, l'indemnité d'assurance étant assimilée à un prix de cession).
- CGI, art. 256 : champ d'application de la TVA (indemnités sans contrepartie hors champ).
