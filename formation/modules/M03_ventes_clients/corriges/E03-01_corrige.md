# Corrigé E03-01 — Le Z de caisse du samedi

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-01](../exercices/E03-01_z-de-caisse-boulangerie.md)

## 1. Analyse

**a) La pièce comptable, c'est le Z.** La boulangerie vend à des particuliers sans facture : la pièce justificative des recettes est le ticket Z journalier issu d'un logiciel de caisse sécurisé. Avant toute saisie, un senior vérifie trois choses :
- **le logiciel est couvert** par un certificat (NF525 mentionné sur le Z) ou une attestation individuelle de l'éditeur (présente au dossier permanent, datée du 14/02/2024 : à faire renouveler en cas de changement de version majeure ou d'éditeur) ;
- **la continuité** : numéro de Z (0274 — vérifier que le 0273 est bien celui du 02/10) et grand total perpétuel croissant ;
- **la cohérence interne** : somme des familles = total TTC = total des règlements.

Contrôle des familles : 1 018,60 + 412,30 + 196,50 + 60,00 = **1 687,40 €** (5,5 %) ; 612,50 + 130,00 = **742,50 €** (10 %) ; 54,00 + 42,00 = **96,00 €** (20 %). Total 2 525,90 € = total des règlements (884,30 + 1 412,60 + 229,00 = 2 525,90 €). Le Z est cohérent.

**b) Le paramétrage des taux est faux sur une ligne.** Les **boissons non alcoolisées consommées sur place** relèvent de la restauration : taux de **10 %** (art. 279 CGI). Seules les **boissons alcoolisées** sont à 20 %. La ligne « Sodas sur place (20 %) » est donc mal paramétrée. (La fiche permanente du client reprend d'ailleurs cette erreur : « boissons alcoolisées et sodas consommés sur place 20 % » — elle est à corriger.)

Rappel de la grille pour une boulangerie :

| Produit | Taux |
|---|---|
| Pain, viennoiseries, pâtisseries, boissons non alcoolisées **à emporter** (consommation différée) | 5,5 % |
| Sandwichs, formules, produits destinés à une **consommation immédiate**, boissons non alcoolisées **sur place** | 10 % |
| Boissons **alcoolisées** (sur place ou à emporter) | 20 % |

**c) Que faire du Z erroné ?** Le ticket remis au client fait apparaître un taux de 20 % : on ne réécrit pas un Z certifié. La méthode recommandée :
1. comptabiliser le Z **tel qu'il est** (la comptabilité doit concorder avec les Z archivés et le FEC) ;
2. faire **corriger le paramétrage immédiatement** par l'éditeur (ou par Marc, avec notre aide) ;
3. chiffrer la TVA versée en trop sur la période passée et décider, avec Hélène, d'une éventuelle **réclamation** (délai : jusqu'au 31/12 de la 2e année suivant celle du versement). L'enjeu doit être mis en regard du risque de discussion sur la valeur des tickets mentionnant la TVA.

**d) Les 100 € « Marc – plombier ».** Sortie d'espèces sans justificatif : ce n'est **pas une charge déductible** en l'état (pas de facture) et la TVA n'est pas récupérable. Deux possibilités :
- le plombier a travaillé pour la boulangerie : il **doit** émettre une facture (opération entre professionnels) → on la réclame, on attend en **471** ;
- à défaut de facture dans le mois, la dépense est imputée au **compte courant de Marc** (455).

Or la pièce 4 montre que le compte courant de Marc est **déjà débiteur de 50 €** au 31/08. Ajouter 100 € le porterait à 150 € débiteur. **En SARL, il est interdit à un associé personne physique (et a fortiori au gérant) de se faire consentir un découvert en compte courant** (art. L. 223-21 C. com.) : c'est pénalement sanctionnable (abus de biens sociaux possible) et fiscalement, les sommes peuvent être requalifiées en revenus distribués (art. 111-a CGI). Il faut régulariser vite (remboursement par Marc ou rémunération/dividende décidé régulièrement).

**e) Les écarts de caisse sont systématiquement négatifs.** Un écart ponctuel de quelques euros est normal (rendu de monnaie). Mais 5 écarts négatifs sur 6 jours, pour un total de – 47,60 € sur la semaine, soit environ **– 2 400 € par an** extrapolés, n'est pas « du rendu de monnaie ». Causes possibles : prélèvements non notés, ventes encaissées sans ticket, erreurs de comptage, vol. Pour l'administration, une caisse aux écarts répétés est un indice de **comptabilité non probante**.

## 2. Calculs

**Espèces théoriques du 03/10**

| | Montant |
|---|---|
| Fond de caisse | 150,00 |
| + Espèces du Z | 884,30 |
| – Levure | – 12,00 |
| – Sortie « Marc » | – 100,00 |
| **= Espèces théoriques** | **922,30** |
| Espèces comptées | 914,80 |
| **Écart** | **– 7,50** |
| Remise en banque (914,80 – 150,00 de fond) | **764,80** |

**Incidence du mauvais taux sur la journée**

| | Paramétrage actuel | Correct |
|---|---|---|
| Sodas sur place 54,00 TTC | 20 % : HT 45,00 / TVA 9,00 | 10 % : HT 49,09 / TVA 4,91 |
| Total base 10 % | 742,50 TTC → HT 675,00 / TVA 67,50 | 796,50 TTC → HT 724,09 / TVA 72,41 |
| Total base 20 % | 96,00 TTC → HT 80,00 / TVA 16,00 | 42,00 TTC → HT 35,00 / TVA 7,00 |
| **TVA totale du jour** | **171,47** | **167,38** |

TVA versée en trop : **4,09 € pour la journée**, soit de l'ordre de **1 270 € par an** (4,09 € × environ 310 jours d'ouverture) — à affiner avec les Z mensuels.

**Écarts de la semaine** : – 12,00 + 3,20 – 9,80 – 15,40 – 6,10 – 7,50 = **– 47,60 €**.

**Levure** : ticket sans mention de TVA → pas de déduction ; charge de 12,00 € en 601.

## 3. Écritures comptables

Comptes de ventes ventilés par taux (pratique du cabinet pour faciliter la CA12 ; une ventilation plus fine 701 / 707 par famille est possible si le Z la fournit).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 03/10/2026 | VC (ventes caisse) | 531 | Caisse | Z 0274 – espèces | 884,30 | |
| 03/10/2026 | VC | 5115 | CB à encaisser | Z 0274 – CB | 1 412,60 | |
| 03/10/2026 | VC | 5116 | Titres-restaurant à encaisser | Z 0274 – TR | 229,00 | |
| 03/10/2026 | VC | 7011 | Ventes produits 5,5 % | Z 0274 | | 1 599,43 |
| 03/10/2026 | VC | 7012 | Ventes produits 10 % | Z 0274 | | 675,00 |
| 03/10/2026 | VC | 7071 | Ventes boissons 20 % | Z 0274 | | 80,00 |
| 03/10/2026 | VC | 445715 | TVA collectée 5,5 % | Z 0274 | | 87,97 |
| 03/10/2026 | VC | 445710 | TVA collectée 10 % | Z 0274 | | 67,50 |
| 03/10/2026 | VC | 445720 | TVA collectée 20 % | Z 0274 | | 16,00 |
| 03/10/2026 | CA (caisse) | 601 | Achats de matières premières | Levure – marché | 12,00 | |
| 03/10/2026 | CA | 531 | Caisse | Levure – marché | | 12,00 |
| 03/10/2026 | CA | 471 | Compte d'attente | Sortie espèces « Marc – plombier » – facture demandée | 100,00 | |
| 03/10/2026 | CA | 531 | Caisse | Sortie espèces | | 100,00 |
| 03/10/2026 | CA | 658 | Charges diverses de gestion courante (*subdivision selon la nomenclature 2025 du PCG*) | Écart de caisse 03/10 | 7,50 | |
| 03/10/2026 | CA | 531 | Caisse | Écart de caisse 03/10 | | 7,50 |
| 05/10/2026 | CA | 580 | Virements internes | Remise espèces | 764,80 | |
| 05/10/2026 | CA | 531 | Caisse | Remise espèces | | 764,80 |
| 05/10/2026 | BQ | 512 | Banque | Remise espèces | 764,80 | |
| 05/10/2026 | BQ | 580 | Virements internes | Remise espèces | | 764,80 |
| | | | | **Totaux** | **4 175,00** | **4 175,00** |

Contrôle du compte 531 : 150,00 + 884,30 – 12,00 – 100,00 – 7,50 – 764,80 = **150,00 €** = fond de caisse. ✔

Si aucune facture du plombier n'est obtenue avant la fin du mois : 455 Marc Dupain / 471 pour 100,00 € — **mais** seulement après avoir réglé la question du compte courant débiteur (voir § 5).

## 4. Points d'attention / pièges

- **Ne pas recalculer le HT « à la main » différemment du Z** : on reprend la ventilation HT/TVA du Z (arrondis du logiciel) pour que la TVA collectée comptable corresponde au Z archivé.
- **Taux** : boissons non alcoolisées sur place = 10 %, pas 20 % ; à emporter = 5,5 % (sauf si vendues dans une formule à consommation immédiate → 10 %).
- **Écart de caisse** : il ne modifie pas la TVA collectée (la TVA est due sur les ventes du Z).
- **Caisse créditrice interdite** : contrôler le solde du 531 jour par jour, pas seulement en fin de mois.
- **Compte courant débiteur de l'associé gérant de SARL** : interdit (art. L. 223-21 C. com.) ; à signaler à Hélène.
- **Titres-restaurant** : le 5116 se solde lors du remboursement par la centrale de règlement, net d'une commission (627 + TVA déductible si facturée avec TVA). Rapprocher le 5116 chaque mois.

## 5. Ce qu'un senior ferait en plus

**Mail à Marc (à envoyer après 14 h, il ne lit pas ses mails le matin — l'appeler serait encore mieux) :**

> Bonjour Monsieur Dupain,
>
> Merci pour le Z du 3 octobre. Trois points importants :
> 1. **Paramétrage de la caisse** : les sodas consommés sur place sont taxés à 20 % alors que le taux légal est de 10 %. Vous payez environ 4 € de TVA en trop chaque jour (de l'ordre de 1 300 € par an). Pouvez-vous demander à CaissePro de corriger la famille « Sodas sur place » dès cette semaine ? Nous chiffrerons ensuite ce qui peut être récupéré.
> 2. **Les 100 € du plombier** : sans facture, cette dépense n'est ni déductible ni récupérable en TVA. Merci de demander une facture au plombier (il est tenu de vous en remettre une). Sinon, la somme sera mise à votre compte personnel, qui est déjà débiteur : or la loi interdit qu'un associé de SARL doive de l'argent à sa société. Nous devons en parler.
> 3. **Écarts de caisse** : 47,60 € manquent sur la semaine. Pouvez-vous noter **chaque** sortie d'espèces avec un justificatif, et compter la caisse à deux (vous et Julie) le soir pendant un mois ?
>
> Bien cordialement.

**Contrôles complémentaires à prévoir :**
- tableau mensuel des écarts de caisse (montant, jour, caissier) ;
- rapprochement mensuel des CB télécollectées (relevé bancaire) avec les Z ;
- test de **marge** : CA 5,5 % / achats de farine et beurre comparé aux années précédentes (un taux de marge anormal confirme ou infirme des ventes non enregistrées) ;
- mise à jour de la **fiche permanente** (taux des sodas sur place).

## 6. Références

- CGI : art. 278-0 bis et 279 (taux de 5,5 % et 10 %), art. 286-I-3° bis (logiciels et systèmes de caisse sécurisés) ; BOFiP TVA-DECLA (obligations des logiciels de caisse) et TVA-LIQ (taux en restauration et vente à emporter).
- Code de commerce : art. L. 223-21 (interdiction des comptes courants débiteurs des associés de SARL).
- CGI : art. 111-a (avances aux associés réputées distribuées).
- PCG : comptes 511, 531, 580, 658 / 758 (subdivisions selon la nomenclature 2025).
