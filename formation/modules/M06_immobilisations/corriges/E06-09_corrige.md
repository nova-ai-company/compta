# Corrigé E06-09 — Le tracteur subventionné par la Région

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-09](../exercices/E06-09_subvention-tracteur-jardins-solidaires.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — Coût d'entrée (question 1).** L'association n'est **pas assujettie** à la TVA : elle ne récupère rien, la TVA fait partie du coût. On distingue deux biens (durées différentes) :
- **tracteur** : 40 000 HT + 8 000 TVA = **48 000,00 €** TTC ;
- **broyeur** : 5 000 HT + 1 000 TVA = **6 000,00 €** TTC.
La reprise de l'ancien tracteur (2 000 €) est une **cession** distincte, elle ne diminue pas le coût du nouveau (même logique qu'en E06-03).

**Étape 2 — Nature de la subvention.** Elle finance **l'acquisition d'un bien durable** déterminé : c'est une **subvention d'investissement** (d'équipement), qui va en **capitaux propres** (fonds propres de l'association) au compte **131**, et non en produit d'exploitation (74). Elle est ensuite « reprise » au résultat **au rythme de l'amortissement** du bien qu'elle finance (139 / 747), ce qui neutralise progressivement la charge d'amortissement.

**Date de comptabilisation** : à la **signature de la convention** (15/02/2026), qui rend la subvention **acquise** dans son principe et son montant (24 000 €) — l'association remplit les conditions (le tracteur est acheté). La part non encore versée est une **créance** (441). Le versement en deux temps n'est qu'une modalité de trésorerie.

**Étape 3 — Quote-part de reprise.** La subvention ne finance que le **tracteur** (pas le broyeur, autofinancé). Elle couvre 24 000 / 48 000 = **50 %** du coût du tracteur : on reprend chaque année 50 % de la dotation du tracteur.

**Étape 4 — L'ancien tracteur (question 3).** Totalement amorti depuis le 31/03/2024 et cédé 2 000 € : VNC nulle, produit de cession 2 000 € (775), sans TVA (association non assujettie). Sa subvention de 11 000 € a été **entièrement reprise** (139 = 131 = 11 000) : on **solde** les deux comptes l'un par l'autre — ils n'ont plus d'objet. La clause d'inaliénabilité du Département (si elle existait) est expirée depuis longtemps.

**Étape 5 — Clause de reversement.** L'article 6 crée un **engagement** sur 5 ans : à mentionner en annexe. Il ne justifie aucune provision tant que l'association n'a pas l'intention de céder le tracteur.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---:|
| Dotation tracteur 2026 | 48 000 / 8 × 9/12 | **4 500,00** |
| Dotation broyeur 2026 | 6 000 / 5 × 9/12 | **900,00** |
| Total dotations 2026 | | **5 400,00** |
| Quote-part de subvention virée au résultat | 24 000 × 4 500 / 48 000 (= 24 000 / 8 × 9/12) | **2 250,00** |
| Subvention nette au bilan 31/12/2026 | 24 000 – 2 250 | **21 750,00** |
| Créance sur la Région au 31/12/2026 | 24 000 – 12 000 | **12 000,00** |

Rythme futur de reprise : 3 000 €/an de 2027 à 2033, puis 750 € en 2034 (fin d'amortissement du tracteur le 31/03/2034).

**Question 5 — Écart de résultat 2026**

| Poste | Samuel | Correct |
|---|---:|---:|
| Subvention en produit (7441) | + 12 000,00 | 0,00 |
| Quote-part de subvention (747) | 0,00 | + 2 250,00 |
| Produit de cession ancien tracteur (775) | 0,00 | + 2 000,00 |
| Dotations (52 000 / 8 × 9/12 chez Samuel) | – 4 875,00 | – 5 400,00 |
| **Résultat** | **+ 7 125,00** | **– 1 150,00** |

→ Les saisies de Samuel **surévaluent le résultat 2026 de 8 275,00 €** (et sous-évaluent les fonds propres « subventions d'investissement » de 21 750 €, tout en oubliant la créance de 12 000 € sur la Région).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/02/2026 | OD | 441 | État et autres collectivités – subventions à recevoir | Convention Région ESS-2026-0418 | 24 000,00 | |
| 15/02/2026 | OD | 131 | Subventions d'équipement | Région — tracteur maraîcher | | 24 000,00 |
| 20/03/2026 | OD | 7441 | Subventions d'exploitation – Région | Annulation saisie de Samuel (encaissement 1er versement) | 12 000,00 | |
| 20/03/2026 | OD | 441 | État et autres collectivités – subventions à recevoir | Imputation 1er versement Région (50 %) | | 12 000,00 |
| 28/03/2026 | AC | 2154 | Matériel industriel – tracteur T75-26-0912 | AER-26-0356 tracteur TTC (correction de la saisie nette) | 48 000,00 | |
| 28/03/2026 | AC | 2154 | Matériel industriel – broyeur | AER-26-0356 broyeur TTC | 6 000,00 | |
| 28/03/2026 | AC | 404 | Fournisseurs d'immobilisations – Agri Équipement Rhône | AER-26-0356 (brut, avant reprise) | | 54 000,00 |
| 28/03/2026 | OD | 462 | Créances sur cessions d'immobilisations | Reprise tracteur 2014 | 2 000,00 | |
| 28/03/2026 | OD | 775 | Produits des cessions d'éléments d'actif | Cession tracteur 2014 (sans TVA) | | 2 000,00 |
| 28/03/2026 | OD | 404 | Fournisseurs d'immobilisations – Agri Équipement Rhône | Compensation reprise | 2 000,00 | |
| 28/03/2026 | OD | 462 | Créances sur cessions d'immobilisations | Compensation reprise | | 2 000,00 |
| 28/03/2026 | OD | 28154 | Amortissements du matériel industriel | Sortie tracteur 2014 (totalement amorti, VNC 0) | 22 000,00 | |
| 28/03/2026 | OD | 2154 | Matériel industriel | Sortie tracteur 2014 | | 22 000,00 |
| 28/03/2026 | OD | 139 | Subventions d'investissement inscrites au compte de résultat | Solde subvention Département tracteur 2014 | 11 000,00 | |
| 28/03/2026 | OD | 131 | Subventions d'équipement | Solde subvention Département tracteur 2014 | | 11 000,00 |
| 10/04/2026 | BQ | 404 | Fournisseurs d'immobilisations – Agri Équipement Rhône | Règlement AER-26-0356 | 52 000,00 | |
| 10/04/2026 | BQ | 512 | Banque | Règlement AER-26-0356 | | 52 000,00 |
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations corporelles | Tracteur 4 500 + broyeur 900 (9 mois) | 5 400,00 | |
| 31/12/2026 | OD | 28154 | Amortissements du matériel industriel | Tracteur T75-26-0912 | | 4 500,00 |
| 31/12/2026 | OD | 28154 | Amortissements du matériel industriel | Broyeur | | 900,00 |
| 31/12/2026 | OD | 139 | Subventions d'investissement inscrites au compte de résultat | Reprise subvention Région 2026 | 2 250,00 | |
| 31/12/2026 | OD | 747 | Quote-part des subventions d'investissement virée au résultat | Reprise subvention Région 2026 (50 % de la dotation tracteur) | | 2 250,00 |
| | | | | **Totaux** | **186 650,00** | **186 650,00** |

Note : la saisie de la facture par Samuel (D 2154 52 000 / C 404 52 000) est **contre-passée** et remplacée par les écritures du 28/03 ci-dessus. L'encaissement du 20/03 au débit du 512 est conservé ; seule la contrepartie passe de 7441 à 441.

Contrôles : 441 = 24 000 – 12 000 = **12 000 D** ; 131 = 11 000 (ouverture) + 24 000 – 11 000 = **24 000 C** ; 139 = 11 000 (ouverture) – 11 000 + 2 250 = **2 250 D** ; 404 soldé ; 2154 = 22 000 (ouverture) + 54 000 – 22 000 = **54 000 D**.

## 4. Points d'attention / pièges

- **Subvention d'investissement ≠ subvention d'exploitation** : le critère est l'**objet** financé (bien durable) défini par la convention, pas le compte où « on met d'habitude les subventions ».
- **Comptabiliser à l'attribution**, pas à l'encaissement : sinon la créance de 12 000 € disparaît du bilan et la reprise est faussée.
- **Reprise limitée au bien financé** : ne pas reprendre sur la dotation du broyeur.
- **Coût TTC** pour une entité non assujettie (et la subvention, elle, est calculée sur le TTC éligible : cohérent).
- **Ne pas compenser** la subvention avec le coût du bien (inscrire le tracteur pour 24 000 € « net de subvention ») : interdit, la subvention figure en fonds propres.
- **Cession anticipée** : si le tracteur était vendu avant 5 ans, il faudrait (1) virer au résultat le solde non repris de la subvention et (2) constater la **dette de reversement** exigée par la Région (charge correspondante) — les deux mouvements se compensent partiellement.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Tableau des subventions d'investissement pour le CAC (question 6)**

| Financeur | Bien | Date d'octroi | Montant (131) | Repris au 01/01/2026 | Reprise 2026 (747) | Sorties 2026 | Solde au 31/12/2026 (131 – 139) | Reste à encaisser |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Département | Tracteur 2014 | 2014 | 11 000,00 | 11 000,00 | 0,00 | – 11 000,00 / – 11 000,00 | 0,00 | 0,00 |
| Région AURA (ESS-2026-0418) | Tracteur T75-26-0912 | 15/02/2026 | 24 000,00 | 0,00 | 2 250,00 | — | 21 750,00 | 12 000,00 |

**Annexe (règlement ANC n° 2018-06)** : méthode de comptabilisation des subventions d'investissement et rythme de reprise ; tableau ci-dessus ; **engagement** d'inaliénabilité de 5 ans (jusqu'au 28/03/2031) avec reversement prorata en cas de cession ; ressources par origine (le compte de résultat par origine et destination le cas échéant).

**Question 7 — Biens renouvelables (règlement ANC n° 2018-06)** : lorsqu'une subvention finance un bien que l'association **s'engage à renouveler par ses propres moyens** (financement du remplacement à l'identique, sur ressources propres), elle peut être inscrite en **fonds propres sans droit de reprise** (non reprise au résultat), le renouvellement étant alors assuré par les fonds propres. Ici, rien dans la convention ni dans les décisions du conseil d'administration n'établit un tel engagement de renouvellement : on retient le traitement **131 / 139 / 747**. Point à valider avec le CAC et à documenter dans le dossier.

**Message à Samuel Okafor**

> Bonjour Samuel,
>
> La subvention de la Région finance un investissement : elle n'est pas un produit de l'année mais des fonds propres, que nous reprenons au résultat au même rythme que l'amortissement du tracteur (2 250 € en 2026, puis 3 000 € par an). Le second versement de 12 000 € est inscrit comme une créance sur la Région ; merci de nous prévenir dès qu'il arrive.
>
> Le tracteur et le broyeur sont inscrits pour leur prix TTC (l'association ne récupère pas la TVA), sans déduire la reprise : l'ancien tracteur sort du bilan et la reprise apparaît en produit de cession. Enfin, attention : la Région interdit de revendre le nouveau tracteur avant mars 2031 sous peine de reversement.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Règlement ANC n° 2018-06 (comptes annuels des personnes morales de droit privé à but non lucratif) : subventions d'investissement, biens renouvelables, annexe.
- PCG : comptes 131, 139, 441 ; quote-part de subvention virée au résultat (compte 747 dans la nomenclature applicable depuis 2025) ; rythme de reprise (au rythme des amortissements pour un bien amortissable).
- Code de commerce, art. L. 612-4 : associations recevant des subventions publiques au-delà du seuil légal (153 000 €) — comptes annuels et commissaire aux comptes.
