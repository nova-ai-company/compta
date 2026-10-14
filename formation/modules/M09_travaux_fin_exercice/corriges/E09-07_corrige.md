# Corrigé E09-07 — Asia Trading : dettes et créances en dollars au 31/12/2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-07](../exercices/E09-07_devises-asia-trading.md)

## 1. Analyse

**Principe.** Les créances et dettes en devises sont des éléments **monétaires** : leur valeur en euros dépend du cours du jour. À la clôture, on les convertit **au cours du 31/12**. L'écart avec la valeur historique n'est **pas réalisé** (la dette n'est pas encore payée), donc :
- une **perte latente** (dette qui augmente, créance qui diminue) va au compte **476 Écart de conversion – Actif**. Par **prudence**, elle est couverte par une **provision pour perte de change (1515)** ;
- un **gain latent** (dette qui diminue, créance qui augmente) va au compte **477 Écart de conversion – Passif**, et n'est **jamais** constaté en résultat (art. L. 123-21 C. com. : seuls les bénéfices réalisés).

**Réponses à Kevin :**
1. « Je dois montrer une grosse perte ? » → Il y a une perte latente sur les dettes. Elle ne passe pas directement en charge : elle est inscrite au bilan (476) et une **provision** est constatée. Grâce à la position globale, cette provision est limitée à la perte nette.
2. « Je peux compter le gain sur Dubaï ? » → **Non** en tant que produit. Le gain latent reste au passif (477). En revanche, comme les échéances sont voisines, il **réduit la provision** nécessaire (position globale).

**Position globale de change :** les trois éléments sont en USD, avec des échéances au 14/01, au 31/01 et au 10/02/2027, soit moins de 2 mois d'écart. La pratique constante de la société permet de considérer qu'ils forment une position globale : la provision est limitée à la **perte nette**. C'est un choix de méthode, à appliquer de façon **permanente** et à mentionner en annexe.

**Compte bancaire USD :** les disponibilités en devises sont converties au cours de clôture, et l'écart va **directement en résultat financier** (766 ou 666), sans passer par 476/477.

**Stock (corner case) :**
- Les lampes NH-T12 ont été achetées **FOB Ningbo** : le transfert des risques et de la propriété intervient au chargement à bord (02/12/2026). Elles **appartiennent à Asia Trading au 31/12**, même si elles sont sur un bateau. La dette est comptabilisée, mais le stock physique ne les inclut pas. Il faut donc **ajouter les marchandises en transit au stock final**. Sinon, le résultat serait minoré de 33 953,49 €, puisque l'achat est passé en charge sans stock final correspondant.
- Le stock est un élément **non monétaire** : il reste au **coût historique en euros** (33 953,49 €, cours du 02/12). On ne le réévalue **pas** au cours de clôture, contrairement à la dette correspondante.
- Les droits de douane et les frais d'approche ne seront engagés qu'à l'arrivée en 2027. Ils ne font pas partie du coût au 31/12/2026.

## 2. Calculs

| Élément | USD | Valeur historique | Cours 31/12 | Valeur au 31/12 | Écart | Nature |
|---|---|---|---|---|---|---|
| Dette Shenzhen | 84 000,00 | 77 064,22 € (1,0900) | 1,0600 | 79 245,28 € | + 2 181,06 € | Perte latente → 476 |
| Dette Ningbo | 36 500,00 | 33 953,49 € (1,0750) | 1,0600 | 34 433,96 € | + 480,47 € | Perte latente → 476 |
| Créance Lumière Emirates | 52 000,00 | 48 059,15 € (1,0820) | 1,0600 | 49 056,60 € | + 997,45 € | Gain latent → 477 |

Détail : 84 000 / 1,06 = 79 245,28 € ; 36 500 / 1,06 = 34 433,96 € ; 52 000 / 1,06 = 49 056,60 €.

- **Écarts de conversion actif (476)** : 2 181,06 + 480,47 = **2 661,53 €**
- **Écarts de conversion passif (477)** : **997,45 €**

**Provision pour perte de change :**
- (a) élément par élément : 2 661,53 € ;
- (b) position globale : 2 661,53 – 997,45 = **1 664,08 €** → **retenue**, conformément à la méthode constante de la société.

**Banque USD :** 15 000 / 1,06 = 14 150,94 € ; solde comptable 13 950,00 € → **gain de change réalisé (financier) 200,94 €**.

**Stock en transit :** **33 953,49 €** au coût historique. Stock final total : 412 600,00 + 33 953,49 = **446 553,49 €**.

**Impact sur le résultat 2026 :** – 1 664,08 (provision) + 200,94 (banque) + 33 953,49 (stock en transit) = **+ 32 490,35 €**.

## 3. Écritures comptables

**Au 31/12/2026 :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 476 | Différences de conversion – Actif | Conversion dette Shenzhen 84 000 USD | 2 181,06 | |
| 31/12/2026 | OD | 401 | Fournisseurs | Conversion dette Shenzhen | | 2 181,06 |
| 31/12/2026 | OD | 476 | Différences de conversion – Actif | Conversion dette Ningbo 36 500 USD | 480,47 | |
| 31/12/2026 | OD | 401 | Fournisseurs | Conversion dette Ningbo | | 480,47 |
| 31/12/2026 | OD | 411 | Clients | Conversion créance Lumière Emirates 52 000 USD | 997,45 | |
| 31/12/2026 | OD | 477 | Différences de conversion – Passif | Conversion créance Lumière Emirates | | 997,45 |
| 31/12/2026 | OD | 6865 | Dotations aux provisions financières (*voir note*) | Provision perte de change – position globale | 1 664,08 | |
| 31/12/2026 | OD | 1515 | Provisions pour pertes de change | Provision perte de change | | 1 664,08 |
| 31/12/2026 | OD | 5124 | Banque – compte USD | Conversion solde 15 000 USD au cours de clôture | 200,94 | |
| 31/12/2026 | OD | 766 | Gains de change financiers | Conversion solde 15 000 USD | | 200,94 |
| 31/12/2026 | OD | 37 | Stocks de marchandises | Marchandises en transit NH-T12 (FOB 02/12) | 33 953,49 | |
| 31/12/2026 | OD | 6037 | Variation des stocks de marchandises | Marchandises en transit NH-T12 | | 33 953,49 |
| | | | | **Totaux** | **39 477,49** | **39 477,49** |

*Note sur le classement de la dotation : les gains et pertes de change **réalisés** sur opérations commerciales sont en résultat d'exploitation (656/756) depuis le règlement ANC n° 2015-05. Pour la **dotation** à la provision pour perte de change sur opérations commerciales, une présentation en exploitation (6815) est cohérente avec ce classement, mais beaucoup d'entités conservent 6865. Choisissez une présentation, documentez-la et appliquez-la de façon permanente — subdivision selon la nomenclature 2025 du PCG à vérifier dans votre logiciel.*

*Le stock en transit est souvent suivi dans un sous-compte dédié (ex. 3701 « Marchandises en transit »).*

**Au 01/01/2027 — extourne des écarts de conversion :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/01/2027 | OD | 401 | Fournisseurs | Extourne conversion Shenzhen | 2 181,06 | |
| 01/01/2027 | OD | 476 | Différences de conversion – Actif | Extourne conversion Shenzhen | | 2 181,06 |
| 01/01/2027 | OD | 401 | Fournisseurs | Extourne conversion Ningbo | 480,47 | |
| 01/01/2027 | OD | 476 | Différences de conversion – Actif | Extourne conversion Ningbo | | 480,47 |
| 01/01/2027 | OD | 477 | Différences de conversion – Passif | Extourne conversion Lumière Emirates | 997,45 | |
| 01/01/2027 | OD | 411 | Clients | Extourne conversion Lumière Emirates | | 997,45 |
| | | | | **Totaux** | **3 658,98** | **3 658,98** |

La **provision** (1515) n'est pas extournée : elle est reprise au fur et à mesure des dénouements, ou au plus tard à la clôture 2027. Le gain sur la banque USD est réalisé et n'est pas extourné.

**Règlement Shenzhen le 15/01/2027 :** 84 000 / 1,0650 = 78 873,24 €. Après l'extourne, la dette est revenue à sa valeur historique (77 064,22 €). La perte de change **réalisée**, commerciale, est de 1 809,02 €.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/01/2027 | BQ | 401 | Fournisseurs | Règlement Shenzhen 84 000 USD | 77 064,22 | |
| 15/01/2027 | BQ | 656 | Pertes de change sur créances et dettes commerciales | Perte de change réalisée | 1 809,02 | |
| 15/01/2027 | BQ | 512 | Banque | Règlement Shenzhen (cours 1,0650) | | 78 873,24 |
| | | | | **Totaux** | **78 873,24** | **78 873,24** |

*Le dollar a légèrement reculé entre le 31/12 et le 15/01 : la perte réalisée (1 809,02 €) est inférieure à l'écart latent constaté sur cette dette (2 181,06 €).*

## 4. Points d'attention / pièges

**Retraitements fiscaux (art. 38, 4 CGI) — 2058-A :**

| Ligne | Montant |
|---|---|
| Réintégration de la provision pour perte de change (non déductible) | + 1 664,08 € |
| Réintégration de l'écart de conversion passif (gain latent imposable) | + 997,45 € |
| Déduction de l'écart de conversion actif (perte latente déductible) | – 2 661,53 € |
| **Total des retraitements** | **0,00 €** |

Comptablement, la charge nette constatée est de 1 664,08 € (la provision). Fiscalement, la charge nette retenue est de 2 661,53 – 997,45 = 1 664,08 €. Les deux coïncident parce que la position globale égalise provision et écart net. **Sans** position globale, la provision serait de 2 661,53 € et le retraitement net de + 997,45 € : fiscalement, le gain latent est imposé, même si on ne le constate pas en comptabilité. Un **état de suivi des écarts de conversion** doit être joint à la liasse.

**Pièges :**
- Ne **jamais** passer le gain latent (477) en produit.
- Ne **jamais** réévaluer le **stock** au cours de clôture : il reste au coût historique.
- Les **marchandises en transit** achetées FOB, CFR ou CIF appartiennent à l'acheteur dès le chargement. Achetées DAP ou DDP, elles appartiennent encore au vendeur. Vérifiez **l'Incoterm et la date du connaissement (B/L)**.
- Le compte bancaire en devises : écart **directement en résultat** (pas de 476/477).
- Les **acomptes versés** sur commandes en devises sont en pratique maintenus au cours historique (élément non monétaire assimilé).
- **Permanence des méthodes** : choisir la position globale engage la société pour les exercices suivants.

## 5. Ce qu'un senior ferait en plus

- **Annexe** : mentionner la méthode de conversion, le montant des écarts de conversion actif et passif, et le choix de la position globale.
- **Conseil à Kevin** : avec environ 2,9 M€ de CA dont une grande partie des achats en USD, l'exposition au change est structurelle. Proposez-lui d'en parler à sa banque : **achats à terme** sur les échéances fournisseurs, ou compte en USD alimenté par les ventes export, pour une couverture naturelle. Une couverture qualifiée permettrait de ne plus provisionner la partie couverte (règlement ANC n° 2015-05).
- **Contrôle de cut-off des achats import** : rapprocher les connaissements (B/L) de décembre des factures et des entrées en stock, pour identifier tous les biens en transit.
- **Mail à Kevin :**
> « Bonjour Kevin, la hausse du dollar crée une perte latente de 2 661,53 € sur vos dettes chinoises et un gain latent de 997,45 € sur la créance de Dubaï. Comme les échéances sont proches, nous ne provisionnons que la perte nette (1 664,08 €). Le gain n'est jamais comptabilisé en produit tant qu'il n'est pas encaissé. Attention : les lampes de Ningbo, sur le bateau au 31/12, vous appartiennent déjà (FOB). Nous les avons ajoutées au stock (33 953,49 €) : votre inventaire de l'entrepôt ne suffit pas. »

## 6. Références

- PCG (règlement ANC n° 2014-03 modifié) : opérations en devises (conversion au cours de clôture, comptes 476/477, provision pour perte de change, position globale de change).
- Règlement ANC n° 2015-05 (instruments financiers à terme et opérations de couverture ; classement des écarts de change commerciaux en 656/756).
- Code de commerce, art. L. 123-21 (seuls les bénéfices réalisés peuvent être inscrits).
- CGI, art. 38, 4 (prise en compte fiscale des écarts de conversion) ; art. 39, 1-5° (provisions) ; art. 262 I (exonération des exportations).
- Incoterms® 2020 (ICC) : transfert des risques FOB au chargement à bord.
