# Corrigé E03-08 — Abonnements SaaS facturés d'avance

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-08](../exercices/E03-08_abonnements-saas.md)

## 1. Analyse

**a) Réponse à Yanis.** Un abonnement SaaS est une **prestation de services continue** : le produit est acquis **au fur et à mesure de la période de service** (principe d'indépendance des exercices, art. L. 123-21 C. com. : « seuls les bénéfices réalisés à la date de clôture peuvent être inscrits dans les comptes »). L'engagement du client et la facturation d'avance ne rendent pas le service exécuté : la part non courue au 31/12 est un **produit constaté d'avance (487)**, au passif. Reconnaître le contrat entier à la signature gonflerait artificiellement le résultat et les capitaux propres — exactement ce que les auditeurs des investisseurs (due diligence) vont vérifier en premier.

L'**ARR** (*Annual Recurring Revenue*) est un **indicateur de gestion** (valeur annualisée des abonnements actifs à une date) : il peut être présenté aux investisseurs dans le dossier de levée, à côté des comptes, mais **ce n'est pas le chiffre d'affaires comptable**. Les deux doivent pouvoir être réconciliés (CA comptable + variation des PCA ≈ facturation de la période).

**b) Les cas particuliers.**
- **Frais de mise en service** : selon les CGV (art. 6), il s'agit d'une prestation **distincte**, réalisée en octobre et qui ne conditionne pas l'accès au service : produit **reconnu à sa réalisation** (octobre 2026). Si, au contraire, la mise en service n'avait pas de valeur propre pour le client (simple activation technique indissociable de l'abonnement), elle aurait dû être étalée sur la durée de l'abonnement. Le traitement retenu doit être **documenté** et appliqué de façon permanente.
- **Mois offert** : le client paie 12 000 € pour **13 mois** de service. Le produit se répartit **linéairement sur 13 mois** (923,08 € par mois), et non 1 000 € par mois sur 12 mois avec un mois à zéro.
- **Facture émise en décembre pour 2027** (Frigo Logistique) : la facture existe juridiquement (créance), mais aucun service n'est rendu en 2026 → **PCA à 100 %**. Comme elle n'est pas payée, la TVA reste **en attente (44574)**.
- **Client allemand** : prestation B2B à un assujetti établi dans un autre État membre (numéro validé VIES) → lieu de taxation en Allemagne (art. 259-1° CGI), **facture HT avec la mention « Autoliquidation »**, le preneur autoliquide la TVA allemande. Le traitement comptable du produit est identique (PCA).

**c) TVA.** Prestations de services → TVA exigible **à l'encaissement** (pas d'option débits). D'où le passage par 44574 à la facturation, puis 44571 à l'encaissement. La TVA ne suit **pas** le rythme des PCA : une fois encaissé, l'abonnement annuel a supporté toute sa TVA, même si 9/12 du produit est reporté.

## 2. Calculs

| Contrat | HT facturé | Période | Mois 2026 / total | CA 2026 | PCA au 31/12/2026 |
|---|---|---|---|---|---|
| Bauplan GmbH (DE) | 9 600,00 | 07/2026 – 06/2027 | 6 / 12 | 4 800,00 | **4 800,00** |
| Logis Plan — abonnement | 14 400,00 | 10/2026 – 09/2027 | 3 / 12 | 3 600,00 | **10 800,00** |
| Logis Plan — mise en service | 1 500,00 | réalisée en 10/2026 | — | 1 500,00 | 0,00 |
| Atelier Mobile (13 mois) | 12 000,00 | 11/2026 – 11/2027 | 2 / 13 | 1 846,15 | **10 153,85** |
| Frigo Logistique | 6 000,00 | 01/2027 – 12/2027 | 0 / 12 | 0,00 | **6 000,00** |
| **Total** | **43 500,00** | | | **11 746,15** | **31 753,85** |

Détail Atelier Mobile : 12 000 / 13 = 923,08 € par mois ; 2 mois en 2026 = 1 846,15 € ; PCA = 12 000 × 11/13 = 10 153,85 €.

Contrôle : 43 500,00 – 31 753,85 = 11 746,15 € ✔.

**Exigibilité de la TVA**

| Facture | TVA | Encaissement | Mois d'exigibilité / CA3 |
|---|---|---|---|
| TN-2026-0611 (DE) | néant (autoliquidation par le preneur) | 10/07/2026 | Base 9 600 € en ligne **E2** « Autres opérations non imposables » de la CA3 de **juillet** 2026 (période d'exécution/paiement selon la règle d'exigibilité applicable aux services continus facturés d'avance) + **déclaration européenne de services (DES)** du mois |
| TN-2026-0802 | 3 180,00 | 05/10/2026 | Octobre 2026 (ligne A1 / 08) |
| TN-2026-0890 | 2 400,00 | 10/11/2026 | Novembre 2026 |
| TN-2026-0955 | 1 200,00 | 15/01/2027 (prévu) | Janvier 2027 → en 44574 au 31/12/2026 |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/07/2026 | VT | 411BAU | Client Bauplan GmbH | TN-2026-0611 abonnement annuel – autoliquidation | 9 600,00 | |
| 01/07/2026 | VT | 7062 | Prestations – abonnements UE | TN-2026-0611 | | 9 600,00 |
| 10/07/2026 | BQ | 512 | Banque | Encaissement TN-2026-0611 | 9 600,00 | |
| 10/07/2026 | BQ | 411BAU | Client Bauplan GmbH | Encaissement TN-2026-0611 | | 9 600,00 |
| 01/10/2026 | VT | 411LOG | Client Logis Plan | TN-2026-0802 | 19 080,00 | |
| 01/10/2026 | VT | 7061 | Prestations – abonnements France | TN-2026-0802 abonnement annuel | | 14 400,00 |
| 01/10/2026 | VT | 7063 | Prestations – mise en service | TN-2026-0802 mise en service | | 1 500,00 |
| 01/10/2026 | VT | 44574 | TVA collectée en attente | TN-2026-0802 | | 3 180,00 |
| 05/10/2026 | BQ | 512 | Banque | Encaissement TN-2026-0802 | 19 080,00 | |
| 05/10/2026 | BQ | 411LOG | Client Logis Plan | Encaissement TN-2026-0802 | | 19 080,00 |
| 05/10/2026 | OD | 44574 | TVA collectée en attente | TVA exigible TN-2026-0802 | 3 180,00 | |
| 05/10/2026 | OD | 44571 | TVA collectée | TVA exigible TN-2026-0802 | | 3 180,00 |
| 01/11/2026 | VT | 411ATM | Client Atelier Mobile | TN-2026-0890 – 13 mois | 14 400,00 | |
| 01/11/2026 | VT | 7061 | Prestations – abonnements France | TN-2026-0890 | | 12 000,00 |
| 01/11/2026 | VT | 44574 | TVA collectée en attente | TN-2026-0890 | | 2 400,00 |
| 10/11/2026 | BQ | 512 | Banque | Prélèvement TN-2026-0890 | 14 400,00 | |
| 10/11/2026 | BQ | 411ATM | Client Atelier Mobile | Prélèvement TN-2026-0890 | | 14 400,00 |
| 10/11/2026 | OD | 44574 | TVA collectée en attente | TVA exigible TN-2026-0890 | 2 400,00 | |
| 10/11/2026 | OD | 44571 | TVA collectée | TVA exigible TN-2026-0890 | | 2 400,00 |
| 15/12/2026 | VT | 411FRI | Client Frigo Logistique | TN-2026-0955 – période 2027 | 7 200,00 | |
| 15/12/2026 | VT | 7061 | Prestations – abonnements France | TN-2026-0955 | | 6 000,00 |
| 15/12/2026 | VT | 44574 | TVA collectée en attente | TN-2026-0955 | | 1 200,00 |
| 31/12/2026 | OD | 7062 | Prestations – abonnements UE | PCA Bauplan 6/12 | 4 800,00 | |
| 31/12/2026 | OD | 7061 | Prestations – abonnements France | PCA Logis Plan 9/12 | 10 800,00 | |
| 31/12/2026 | OD | 7061 | Prestations – abonnements France | PCA Atelier Mobile 11/13 | 10 153,85 | |
| 31/12/2026 | OD | 7061 | Prestations – abonnements France | PCA Frigo Logistique 12/12 | 6 000,00 | |
| 31/12/2026 | OD | 487 | Produits constatés d'avance | PCA abonnements au 31/12/2026 | | 31 753,85 |
| | | | | **Totaux** | **130 693,85** | **130 693,85** |

## 4. Points d'attention / pièges

- **Au 01/01/2027** : **extourne** (contre-passation) de l'écriture de PCA : 487 / 706 pour 31 753,85 €. Le produit est ainsi « réinjecté » en 2027, puis un nouveau calcul de PCA est fait au 31/12/2027 (les contrats Logis Plan, Bauplan, Atelier Mobile se terminent en 2027 ; Frigo Logistique aussi).
- **PCA ≠ TVA** : la TVA des abonnements payés est déjà déclarée ; elle ne se régularise pas avec les PCA.
- **Facture Frigo Logistique impayée** au 31/12 : au bilan, une créance client de 7 200 € TTC face à un PCA de 6 000 € et une TVA en attente de 1 200 €. Certains cabinets préfèrent ne pas comptabiliser les factures émises par anticipation ; l'essentiel est de **ne reconnaître aucun produit** en 2026 et de rester cohérent d'un exercice à l'autre.
- **Prorata temporis** : on calcule au mois si la facturation est mensuelle et les périodes calées sur des mois civils ; au jour près sinon (365e).
- **Remboursements / SLA** : si un client résilie pour manquement, le PCA correspondant devient une dette à rembourser (ou un avoir) : vérifier les litiges ouverts à la clôture.
- **Client UE** : contrôler à chaque facture la validité du numéro de TVA (VIES) et la mention « Autoliquidation » ; sans numéro valide, la prestation serait taxable en France (TVA française à 20 %).

## 5. Ce qu'un senior ferait en plus

**Message à Émilie :**
> Bonjour Émilie, le CA d'un abonnement se reconnaît au prorata de la période de service : sur ces cinq contrats, 11 746 € en 2026 et 31 754 € de produits constatés d'avance au 31/12. L'ARR peut évidemment être présenté aux investisseurs, mais comme indicateur, réconcilié avec le CA comptable. Je vous propose un fichier de calcul automatique des PCA à partir de l'export Stripe Billing (date de début, date de fin, montant HT), que nous figerons au 31/12 et qui servira de justificatif pour la due diligence.

**Mise en place d'un contrôle permanent** : export mensuel Stripe Billing → tableau des **revenus différés** (*deferred revenue*) par contrat, rapproché du compte 487 à chaque situation ; rapprochement trimestriel du 44574 avec les factures non encaissées ; DES mensuelle pour les clients UE.

**Facture électronique** : TechNova (PME) **reçoit** les factures électroniques depuis le 01/09/2026 et **émettra** au 01/09/2027 ; ses ventes de services exigeront l'e-reporting des **données de paiement** : la synchronisation Stripe / PA est à prévoir dès 2027.

## 6. Références

- Code de commerce : art. L. 123-21 (seuls les bénéfices réalisés sont inscrits), art. L. 123-14 (image fidèle).
- PCG : compte 487 (produits constatés d'avance) ; principes de rattachement des produits à l'exercice.
- CGI : art. 259-1° (lieu des prestations B2B), art. 269-2-c (exigibilité à l'encaissement), art. 283-2 et 289 (mention « Autoliquidation »).
- BOFiP : TVA-CHAMP (lieu des prestations de services) ; TVA-DECLA (déclaration européenne de services).
