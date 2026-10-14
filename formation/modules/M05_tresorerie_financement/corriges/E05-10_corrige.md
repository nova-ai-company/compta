# Corrigé E05-10 — Trois incidents bancaires à la clôture du Garage Martin

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-10](../exercices/E05-10_corner-cases-banque-garage.md)

## 1. Analyse

### 1.1 Le virement Lefebvre (4 380 €)
Méthode de recherche d'un virement sans référence : (1) un montant identique dans les encours clients ? (2) une **combinaison** de factures ? (3) un **acompte** sur commande en cours ? Ici : 1 380,00 (facture atelier impayée) + 3 000,00 (acompte demandé sur le bon de commande de la Clio) = **4 380,00 €** ✔. Le nom du donneur d'ordre (M. ou Mme Lefebvre Jean) confirme.

- 1 380,00 € → règlement de la facture A-26-0912 (lettrage 411).
- 3 000,00 € → **acompte** sur une vente de véhicule non encore livré → **4191 Avances et acomptes reçus sur commandes**. Ce n'est pas du chiffre d'affaires 2025-2026 : la vente sera constatée à la livraison (06/10/2026, exercice suivant).
- **TVA** : pour une **livraison de biens**, la TVA est exigible à la livraison, pas à l'encaissement d'un acompte (art. 269 CGI). De plus, la Clio relève de la **TVA sur la marge** : la TVA sera calculée sur la marge lors de la vente. Aucune TVA sur l'acompte.

### 1.2 Le chèque impayé (9 800 €)
- Le chèque remis le 16/09 a été crédité « sauf bonne fin » ; son rejet le 25/09 fait **renaître la créance** : contre-passation 411 / 512 et frais de rejet en 627.
- À la clôture : la créance est **douteuse** (impayé, promesse sans garantie) → reclassement en **416** et **dépréciation** à hauteur du risque, calculée sur le **montant hors TVA** (la TVA ne serait récupérable qu'en cas d'irrécouvrabilité définitive).
- **TVA sur la marge** : marge = 9 800 – 7 600 = 2 200 € TTC ; TVA = 2 200 × 20/120 = 366,67 € ; montant « HT » de la créance = 9 800 – 366,67 = 9 433,33 €.
- **Informations postérieures à la clôture** : le virement de 1 000 € du 07/10 est un événement **postérieur** qui **éclaire** une situation existant au 30/09 (la solvabilité du client) : on en tient compte pour évaluer la dépréciation.
- **Réserve de propriété** : le véhicule appartient encore au garage tant que le prix n'est pas payé. En cas de défaillance, le garage peut **revendiquer** le véhicule — c'est une garantie qui limite le risque de perte. On retient néanmoins une dépréciation de 50 % du HT restant dû : la récupération supposerait une procédure, le véhicule aura perdu de la valeur et le client est en difficulté. (Si le véhicule était localisé et récupérable rapidement, une dépréciation plus faible, limitée à la décote attendue, serait défendable.)

### 1.3 La fraude au faux fournisseur
- **Le paiement n'éteint pas la dette** : un paiement libère le débiteur seulement s'il est fait **au créancier** (ou à une personne qu'il a habilitée). Payer un escroc qui usurpe l'identité d'AutoPièces n'éteint rien : le Garage doit toujours **18 420,60 €** à AutoPièces (art. 1342-2 du Code civil).
- Comptablement : on **rétablit la dette** au 401 et on constate une **créance** sur les fonds détournés (467), aussitôt **dépréciée** car le rappel de fonds a échoué et l'auteur est inconnu. Les chances de récupération (plainte, éventuelle responsabilité de la banque) sont trop faibles pour maintenir un actif.
- **Présentation** : depuis le règlement ANC n° 2022-06, le résultat exceptionnel est réservé aux événements majeurs et inhabituels. Une fraude de 18 k€ pour une entreprise de 1,15 M€ de CA reste ici présentée en **exploitation** (dotation aux dépréciations des actifs circulants) ; si elle était d'une ampleur telle qu'elle constitue un événement majeur pour l'entreprise, le classement en exceptionnel serait à discuter — choix à documenter.
- **Fiscalité** : les pertes résultant de détournements commis par des **tiers** sont déductibles (elles ne le sont pas lorsqu'elles résultent d'agissements du dirigeant ou d'une carence grave et répétée de ce dernier). La dépréciation est déductible car la perte est **probable**, **précisément évaluée** et résulte d'un événement survenu dans l'exercice (art. 39-1-5° CGI). Si des fonds étaient récupérés plus tard : reprise de dépréciation, imposable.
- **TVA** : les factures FA-88412 et FA-88467 correspondent à des **pièces réellement livrées** ; la TVA déduite reste acquise (le droit à déduction naît de la livraison et de la facture, pas du paiement). La fraude n'a aucun effet TVA.

### Indices qui auraient dû alerter (pièce 2)
1. **Domaine d'expéditeur différent** : `autopieces-distrib.com` au lieu de `autopieces-distribution.fr`.
2. **IBAN étranger** (Lituanie, néobanque) pour un fournisseur établi à Vénissieux.
3. **Urgence** et menace (« éviter la suspension de vos livraisons ») ; paiement anticipé demandé.
4. Motif vague (« audit annuel »), signataire inconnu.
5. Aucune **confirmation par un autre canal** (appel au numéro habituel du fournisseur).

## 2. Calculs

### Chèque impayé

| | Montant |
|---|---|
| Créance TTC initiale | 9 800,00 |
| Encaissé après clôture (07/10) | 1 000,00 |
| Reste dû TTC | 8 800,00 |
| Reste dû hors TVA : 8 800 × 9 433,33 / 9 800 | 8 470,75 |
| **Dépréciation 50 %** | **4 235,38** |

### Fraude
Créance sur fonds détournés : 11 240,40 + 7 180,20 = **18 420,60 €**, dépréciée à 100 %.

### Impact total sur le résultat de l'exercice clos le 30/09/2026

| Élément | Impact |
|---|---|
| Frais de rejet de chèque | – 25,00 |
| Dépréciation créance Petitjean | – 4 235,38 |
| Dépréciation fonds détournés | – 18 420,60 |
| Virement Lefebvre | 0 (lettrage + acompte au bilan) |
| **Total** | **– 22 680,98** |

## 3. Écritures comptables

**Virement Lefebvre :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 471 | Compte d'attente | Identification virement Lefebvre du 22/09 | 4 380,00 |  |
| 30/09/2026 | OD | 411LEF | Client Lefebvre | Règlement facture atelier A-26-0912 |  | 1 380,00 |
| 30/09/2026 | OD | 4191 | Clients — avances et acomptes reçus sur commandes | Acompte BC VO-26-118 Clio (livraison prévue 06/10) |  | 3 000,00 |
| | | | | **Totaux** | **4 380,00** | **4 380,00** |

**Chèque impayé et dépréciation :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 25/09/2026 | BQ | 411PJ | Client Petitjean | Chèque n° 2245871 impayé (sans provision) | 9 800,00 |  |
| 25/09/2026 | BQ | 512 | Banque | Chèque n° 2245871 impayé |  | 9 800,00 |
| 25/09/2026 | BQ | 627 | Services bancaires et assimilés | Frais de rejet chèque Petitjean | 25,00 |  |
| 25/09/2026 | BQ | 512 | Banque | Frais de rejet chèque |  | 25,00 |
| 30/09/2026 | OD | 416 | Clients douteux ou litigieux | Reclassement créance Petitjean (impayé) | 9 800,00 |  |
| 30/09/2026 | OD | 411PJ | Client Petitjean | Reclassement en clients douteux |  | 9 800,00 |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation créance Petitjean (50 % du HT restant dû) | 4 235,38 |  |
| 30/09/2026 | OD | 491 | Dépréciations des comptes de clients | Dépréciation créance Petitjean |  | 4 235,38 |
| | | | | **Totaux** | **23 860,38** | **23 860,38** |

(Le 07/10/2026, l'encaissement de 1 000 € sera porté au crédit du 416.)

**Fraude au changement de RIB :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 4678 | Débiteurs divers — fonds détournés (fraude RIB du 05/09) | Reclassement paiement frauduleux FA-88412 + FA-88467 | 18 420,60 |  |
| 30/09/2026 | OD | 401APD | Fournisseur AutoPièces Distribution | Rétablissement de la dette (paiement à un tiers non libératoire) |  | 18 420,60 |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation créance fraude RIB (recouvrement improbable) | 18 420,60 |  |
| 30/09/2026 | OD | 496 | Dépréciations des comptes de débiteurs divers | Dépréciation créance fraude RIB |  | 18 420,60 |
| | | | | **Totaux** | **36 841,20** | **36 841,20** |

> Délettrer d'abord le 401 AutoPièces (le paiement du 05/09 ne doit plus être lettré avec les factures). Le 401 affiche ensuite 18 420,60 € créditeur : c'est la dette réelle, à payer **sur le RIB habituel vérifié**.

## 4. Points d'attention / pièges

- **Acompte sur VO ≠ chiffre d'affaires** : la vente sera rattachée à l'exercice 2026-2027 (livraison du 06/10). Ne pas déstocker la Clio au 30/09 : elle est toujours en stock.
- **Pas de TVA sur l'acompte** d'une livraison de biens (ni sur la marge avant la vente).
- **Chèque crédité ≠ chèque payé** : le crédit bancaire est « sauf bonne fin ».
- **Dépréciation sur le HT** et non sur le TTC ; en régime de marge, le « HT » se calcule en retirant la TVA sur la marge.
- **Fraude** : l'erreur classique est de laisser le 401 soldé (« on a payé ») → dette omise de 18 420,60 € au bilan et fournisseur qui finira par assigner. Autre erreur : passer la perte sans rétablir la dette.
- **Ne pas annuler la TVA déduite** sur les factures AutoPièces : les pièces ont été livrées.
- **Événements postérieurs** : le virement de 1 000 € du 07/10 sert à évaluer la créance au 30/09 ; il ne remet pas en cause le caractère douteux du solde.

## 5. Ce qu'un senior ferait en plus

**Consignes à Thierry Martin (appel immédiat puis e-mail) :**
> « Bonjour Thierry,
> **Aujourd'hui** : (1) la plainte est déposée, très bien — transmettez le récépissé au Crédit Mutuel et demandez par écrit à votre conseiller si la banque du bénéficiaire a pu bloquer une partie des fonds ; (2) réglez AutoPièces sur leur **RIB habituel**, après avoir appelé leur comptabilité au numéro figurant sur vos anciennes factures — la dette est toujours due, mieux vaut négocier un échéancier que subir une suspension de livraisons ; (3) vérifiez qu'aucun autre fournisseur n'a reçu un mail du même type.
> **Pour l'avenir** : tout changement de RIB doit être confirmé par **téléphone**, à un numéro connu (pas celui du mail), et validé par vous ; la secrétaire ne modifie aucun RIB seule. Je vous conseille aussi de vous renseigner sur une assurance « fraude/cyber ».
> **Pour M. Petitjean** : envoyez-lui une mise en demeure par lettre recommandée rappelant la clause de réserve de propriété ; sans paiement fin novembre, nous lancerons une injonction de payer ou la revendication du véhicule.
> **Pour M. Lefebvre** : rien à faire, son virement correspond à la facture d'atelier et à l'acompte de la Clio.
> Impact sur le résultat de l'exercice : environ – 22 700 € avant impôt. Bien cordialement. »

**Contrôles à ajouter au dossier permanent** : procédure écrite de changement de RIB ; revue mensuelle des **nouveaux IBAN** apparaissant dans les virements émis (le logiciel bancaire peut l'éditer) ; double validation des virements > 5 000 €.

**Documentation** : récépissé de plainte, échanges avec la banque, réponse d'AutoPièces, mise en demeure Petitjean → au dossier de clôture (justification des dépréciations en cas de contrôle). Mention éventuelle en annexe si l'incident est significatif.

## 6. Références
- Code civil, art. 1342-2 (le paiement doit être fait au créancier ou à la personne qu'il a désignée) ; art. 2367 et suivants (réserve de propriété).
- CGI, art. 269 (exigibilité de la TVA sur les livraisons de biens), art. 297 A (régime de la marge pour les biens d'occasion), art. 39-1-5° (provisions et dépréciations), art. 272 (récupération de la TVA en cas de créance irrécouvrable).
- Code monétaire et financier : délai de présentation et rejet du chèque ; certificat de non-paiement.
- PCG (règlement ANC n° 2014-03 modifié par le règlement n° 2022-06) : comptes 416, 491, 4678, 496, 4191, 6817 ; définition restreinte du résultat exceptionnel.
