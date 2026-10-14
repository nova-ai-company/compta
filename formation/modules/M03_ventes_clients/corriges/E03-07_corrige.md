# Corrigé E03-07 — Un client en redressement, puis en liquidation judiciaire

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-07](../exercices/E03-07_client-redressement-liquidation.md)

## 1. Analyse

**a) La déclaration de créance est régulière.**
- **Délai** : 2 mois à compter de la publication du jugement d'ouverture au BODACC (art. L. 622-24 et R. 622-24 C. com.), soit jusqu'au **19/05/2026**. Envoi par LRAR le 28/04/2026 : dans les délais. (Hors délai, il aurait fallu une action en relevé de forclusion, possible dans les 6 mois de la publication — art. L. 622-26.)
- **Montant** : la créance se déclare **TTC** (le débiteur doit le TTC) : 24 000 + 10 800 = **34 800 €** ✔. Antoine aurait pu ajouter les pénalités de retard échues avant le jugement et les indemnités forfaitaires de 40 € (2 × 40 €) : enjeu faible.
- **Nature** : chirographaire (pas de sûreté, pas de clause de réserve de propriété — à vérifier dans les CGV : une **clause de réserve de propriété** aurait permis de **revendiquer** les meubles dans les 3 mois de la publication du jugement).
- La créance a été **admise** (pièce 4) ✔.

**b) TVA : les deux factures ne sont pas dans la même situation.**

| Facture | Nature | Exigibilité de la TVA | TVA déjà reversée ? | Traitement |
|---|---|---|---|---|
| F-2025-118 (mobilier sur mesure livré) | **Livraison de biens meubles** | À la livraison (26/11/2025) | **Oui**, déclarée en novembre 2025 | TVA sur le solde impayé **récupérable** (art. 272-1 CGI) |
| F-2026-021 (pose et fixation d'agencements) | **Travaux immobiliers** (prestation de services) | À l'**encaissement** | **Non** : rien n'a été encaissé, la TVA dort en 44574 | Rien à récupérer : **solder le 44574** |

TVA récupérable sur F-2025-118 : le paiement partiel de 6 000 € TTC est imputé sur cette facture ; reste **24 000 € TTC**, dont TVA 24 000 × 20/120 = **4 000 €**.

**Conditions de la récupération** (art. 272-1 CGI) :
1. la créance doit être **définitivement irrécouvrable** : en cas de **liquidation judiciaire**, la créance est considérée comme irrécouvrable à compter du **jugement de liquidation** (22/09/2026), sans attendre la clôture de la procédure (position administrative à vérifier au BOFiP lors de chaque mise à jour — une créance seulement « douteuse » en redressement ne suffit pas) ;
2. la créance doit avoir été **déclarée** au passif ;
3. le créancier doit **rectifier la facture initiale** : émission d'une **facture rectificative (avoir de TVA)** référençant F-2025-118, adressée au débiteur en la personne du **liquidateur**.

La TVA est imputée sur la CA3 de la période au cours de laquelle l'avoir est émis (ici octobre 2026, CA3 déposée en novembre), en ligne **21 « Autre TVA à déduire »** avec la mention prévue par la notice (*numérotation de la CA3 à contrôler sur le formulaire millésimé*).

**c) Comptabilisation de la créance.**
- Dès le jugement de redressement (connu par la publication du 19/03/2026) : reclassement **411 → 416** (TTC).
- La dépréciation porte sur le **HT** : la TVA est récupérable (F-118) ou n'a jamais été due (F-021). Après les régularisations de TVA, le 416 ne contient plus que du HT : 20 000 + 9 000 = **29 000 €**.
- Au 31/12/2026, la procédure n'est pas clôturée : la créance n'est pas juridiquement éteinte, mais le liquidateur annonce **aucune répartition** → **dépréciation à 100 %** du HT (perte probable, nettement précisée : déductible fiscalement, art. 39-1-5° CGI).
- À la **clôture de la liquidation pour insuffisance d'actif** (certificat d'irrécouvrabilité) : passage en **perte (654)** et **reprise** de la dépréciation (7817). L'effet net sur le résultat de l'exercice de la perte est nul.

*Variante admise* : si le certificat d'irrécouvrabilité était obtenu avant le 31/12/2026, on passerait directement la perte en 654 en 2026, sans dépréciation.

**d) Fallait-il déprécier dès 2025 ?** Le jugement d'ouverture (10/03/2026) fixe la **date de cessation des paiements au 01/12/2025** : la situation qui rend la créance douteuse **existait à la clôture du 31/12/2025**. Le jugement est un **événement postérieur à la clôture** qui apporte une information sur une situation existant à cette date : il devait être pris en compte dans les comptes 2025 **s'il était connu avant leur arrêté**. Or les comptes ont été arrêtés le **27/03/2026**, après la publication du 19/03/2026 : la créance F-2025-118 (24 000 € TTC restant dus, soit 20 000 € HT) aurait dû être **dépréciée dans les comptes 2025** (à hauteur du risque estimé à cette date : en redressement, la dépréciation se fonde sur l'estimation du dividende prévisible — souvent 50 % à 100 % du HT pour une créance chirographaire). La facture F-2026-021, elle, est née en 2026.

Les comptes 2025 étant approuvés, on ne les rouvre pas : la dépréciation est constatée en 2026. Il s'agit d'une **omission** : si elle est significative, une information est donnée dans l'annexe 2026 (correction d'erreur constatée dans le résultat de l'exercice). Fiscalement, une dépréciation omise en 2025 ne peut pas être « rattrapée » en 2026 si elle aurait dû être constatée en 2025 (théorie des provisions irrégulièrement omises) — en pratique, l'enjeu se limite ici au décalage d'un exercice, mais le point est à documenter au dossier. À retenir pour l'avenir : **consulter le BODACC des principaux clients avant tout arrêté des comptes.**

**e) Le paiement de 6 000 € en période suspecte.** Payé le 15/01/2026, après la date de cessation des paiements (01/12/2025) : le liquidateur peut en demander l'**annulation** s'il prouve que Menuiserie Bois & Création **connaissait la cessation des paiements** (nullité facultative, art. L. 632-2 C. com.). Le courrier annonce un examen, pas une action. À la clôture :
- si aucune action n'est engagée : **pas de provision**, simple mention dans le dossier (passif éventuel, éventuellement en annexe si significatif) ;
- si le liquidateur assigne : **provision pour risques** (compte 151) à hauteur du montant probable (6 000 €), et la créance correspondante serait à redéclarer.

## 2. Calculs

| Élément | F-2025-118 | F-2026-021 | Total |
|---|---|---|---|
| TTC facturé | 30 000,00 | 10 800,00 | 40 800,00 |
| Encaissé | 6 000,00 | 0,00 | 6 000,00 |
| **Restant dû TTC (416)** | **24 000,00** | **10 800,00** | **34 800,00** |
| TVA incluse dans le restant dû | 4 000,00 | 1 800,00 | 5 800,00 |
| Traitement de la TVA | Récupérée (avoir de TVA, ligne 21) | Solde du 44574 (jamais déclarée) | |
| **HT restant (base de la dépréciation et de la perte)** | **20 000,00** | **9 000,00** | **29 000,00** |

**Perte définitive pour Menuiserie Bois & Création** : **29 000 € HT** (le montant TTC non payé de 34 800 € diminué de 5 800 € de TVA, dont 4 000 € récupérés auprès de l'État et 1 800 € jamais reversés). Effet sur la trésorerie : – 34 800 € non encaissés + 4 000 € de TVA récupérée = – 30 800 € (les 1 800 € de TVA sur travaux n'ont jamais été décaissés). Effet sur le résultat avant impôt : – 29 000 €.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 19/03/2026 | OD | 416 | Clients douteux ou litigieux | Vallon – RJ du 10/03/2026 | 34 800,00 | |
| 19/03/2026 | OD | 411VAL | Client Boutiques Vallon | Vallon – reclassement en douteux | | 34 800,00 |
| 09/10/2026 | VT | 44571 | TVA collectée (régularisation – ligne 21 CA3) | Avoir de TVA AV-2026-014 sur F-2025-118 – LJ du 22/09/2026 | 4 000,00 | |
| 09/10/2026 | VT | 416 | Clients douteux ou litigieux | Avoir de TVA AV-2026-014 | | 4 000,00 |
| 09/10/2026 | OD | 44574 | TVA collectée en attente (encaissements) | F-2026-021 – TVA jamais exigible (LJ) | 1 800,00 | |
| 09/10/2026 | OD | 416 | Clients douteux ou litigieux | F-2026-021 – annulation TVA en attente | | 1 800,00 |
| 31/12/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Vallon – dépréciation 100 % du HT (aucune répartition) | 29 000,00 | |
| 31/12/2026 | OD | 491 | Dépréciation des comptes clients | Vallon – dépréciation 100 % du HT | | 29 000,00 |
| *Clôture de la LJ (N+x)* | OD | 654 | Pertes sur créances irrécouvrables (*subdivision 6541/6544 selon la nomenclature 2025*) | Vallon – certificat d'irrécouvrabilité | 29 000,00 | |
| *Clôture de la LJ (N+x)* | OD | 416 | Clients douteux ou litigieux | Vallon – solde | | 29 000,00 |
| *Clôture de la LJ (N+x)* | OD | 491 | Dépréciation des comptes clients | Vallon – reprise | 29 000,00 | |
| *Clôture de la LJ (N+x)* | OD | 7817 | Reprises sur dépréciations des actifs circulants | Vallon – reprise | | 29 000,00 |
| | | | | **Totaux** | **127 600,00** | **127 600,00** |

Contrôle du 416 après les régularisations de TVA : 34 800 – 4 000 – 1 800 = **29 000 €** = 20 000 + 9 000 ✔. Le 44574 de F-2026-021 est soldé ✔.

## 4. Points d'attention / pièges

- **Ne jamais déprécier le TTC** : la TVA n'est pas une perte (récupérable ou jamais versée).
- **Ne pas « récupérer » une TVA jamais reversée** : sur F-2026-021 (travaux, TVA sur encaissements), porter 1 800 € en ligne 21 ferait déduire une TVA qui n'a jamais été payée — redressement assuré.
- **Pas de récupération de TVA au stade du redressement** : la créance n'est pas définitivement irrécouvrable (un plan peut prévoir un remboursement). La récupération intervient en liquidation (ou, dans un plan, à hauteur de la part abandonnée).
- **L'avoir de TVA** se borne à annuler la TVA (il ne réduit pas la créance déclarée au passif, qui reste de 34 800 € TTC dans la procédure) ; il doit référencer la facture d'origine et être adressé au liquidateur. Si, contre toute attente, un dividende était versé, la TVA correspondante serait à reverser.
- **Clause de réserve de propriété** : à vérifier pour les prochains contrats (elle permet la revendication des biens non payés).
- **Intégration fiscale** : la perte et la dépréciation affectent le résultat de Menuiserie Bois & Création, qui fait partie du périmètre d'intégration de Delta Invest — elles diminuent le résultat d'ensemble.

## 5. Ce qu'un senior ferait en plus

**Réponse à Antoine (et copie à Jean Delmas, Delta Invest) :**
> Bonjour Antoine, votre déclaration de créance était dans les délais et pour le bon montant : elle a été admise pour 34 800 €. Le liquidateur ne prévoit malheureusement aucune répartition. La perte comptable sera de 29 000 € HT. Nous récupérons 4 000 € de TVA sur la facture de mobilier : je vous envoie l'avoir de TVA à adresser à Me Ravel, et nous l'imputerons sur la déclaration d'octobre. Sur la facture de pose, la TVA n'a jamais été payée (travaux taxés à l'encaissement) : il n'y a rien à récupérer, mais rien n'a été perdu non plus. Attention : le liquidateur examine votre paiement de 6 000 € reçu en janvier ; si vous recevez une assignation, transmettez-la-nous immédiatement.

**Conséquences sur le dossier Menuiserie** (continuité d'exploitation déjà fragile) :
- intégrer la perte dans le **prévisionnel de trésorerie** et le suivi des **capitaux propres** (seuil de la moitié du capital, art. L. 223-42 C. com.) ;
- recommander une **assurance-crédit** ou, a minima, une vérification systématique de la solvabilité des gros clients et des **acomptes** à la commande ;
- **mettre en place une veille BODACC** sur les 20 premiers clients du portefeuille, avant chaque arrêté des comptes.

## 6. Références

- Code de commerce : art. L. 622-24, L. 622-26 et R. 622-24 (déclaration de créances, relevé de forclusion), art. L. 624-9 (revendication), art. L. 632-2 (nullités facultatives de la période suspecte), art. L. 223-42 (capitaux propres inférieurs à la moitié du capital).
- CGI : art. 269-2 (exigibilité : livraisons de biens / prestations), art. 272-1 (TVA sur créances devenues irrécouvrables), art. 39-1-5° (dépréciations).
- BOFiP : TVA-DED (régularisation de la TVA en cas d'impayés et de procédures collectives) ; BIC-PROV (dépréciation des créances douteuses).
- PCG : comptes 416, 491, 654, 6817, 7817, 151 ; traitement des événements postérieurs à la clôture.
