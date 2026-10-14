# Corrigé E03-09 — Trois anomalies sur le compte clients

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-09](../exercices/E03-09_corner-cases-clients.md)

## 1. Analyse

### a) Double paiement (Éditions du Confluent)

Le second encaissement n'est **pas un produit** : c'est une **dette envers le client**, matérialisée par un solde **créditeur** du compte 411 (6 330 €). Deux solutions, au choix du client :
- **remboursement** (choix retenu, 06/10/2026) : 411 au débit / 512 au crédit ;
- **imputation** sur une prochaine facture, uniquement avec l'**accord écrit** du client (pour éviter un litige et sécuriser le lettrage).

Si le remboursement n'avait pas eu lieu avant une clôture, le solde créditeur serait **reclassé au passif** (compte **4191** « avances et acomptes reçus » ou une subdivision **419 « clients créditeurs »**) : on ne compense pas un client créditeur avec les autres clients débiteurs au bilan. Une somme jamais réclamée ne devient un produit (758) qu'à l'expiration de la **prescription commerciale de 5 ans** (art. L. 110-4 C. com.), et seulement après tentative de remboursement documentée.

Point de contrôle : le prélèvement SEPA B2B est passé alors que la facture était déjà soldée → le **mandat SEPA** et le paramétrage des échéances doivent être revus (risque de répétition).

### b) Client suisse (frais bancaires déduits)

- **TVA** : livraison de biens expédiés hors de l'UE → **exportation exonérée** (art. 262 I CGI) à condition de **justifier la sortie** des biens de l'UE (déclaration d'exportation avec confirmation de sortie : présente ✔) et de mentionner l'exonération sur la facture ✔. Le montant est déclaré en ligne **E1 « Exportations hors UE »** de la CA3 du mois de la livraison (septembre 2026). (*Pour les livres, la TVA aurait été de 5,5 % en France — sans incidence ici puisque l'opération est exonérée.*)
- **Écart de 18 €** : frais d'une banque intermédiaire, la facture prévoyant des frais **partagés (SHA)** : chaque partie supporte les frais de sa banque, mais les frais d'un intermédiaire sont fréquemment prélevés sur le montant. Relancer pour 18 € coûterait plus cher que l'écart (temps, frais de virement) et dégraderait la relation : on **constate une charge financière** en **627** (services bancaires). Si l'écart avait été significatif ou répétitif, on aurait demandé au client de passer ses virements en option **OUR** (tous frais à sa charge) ou facturé en conséquence.
- Pas d'écart de change : facture et paiement en euros. (Si la facture avait été en CHF, l'écart de change aurait été comptabilisé en 666 / 766.)

### c) Avoir Hexa Com (facture d'un exercice clos)

**L'écriture de février 2026 est correcte pour 2026** : l'avoir est un document de 2026, il est comptabilisé en 2026 en **7091** (RRR accordés sur ventes de produits finis) avec la TVA correspondante. La **TVA** se régularise sur la déclaration de la **période d'émission de l'avoir** (CA3 de février 2026, déposée en mars), pas sur celle de décembre 2025 : on ne dépose pas de déclaration rectificative.

**Mais les comptes 2025 étaient incomplets.** Le défaut d'impression existait **à la livraison (17/12/2025)**. La réclamation (08/01/2026) et l'accord commercial (13/02/2026) sont des **événements postérieurs à la clôture** qui apportent des informations sur une situation **existant au 31/12/2025**. Ils étaient connus **avant l'arrêté des comptes** (20/03/2026). Il aurait donc fallu comptabiliser au 31/12/2025 un **avoir à établir** :

| Débit | Crédit |
|---|---|
| 7091 RRR accordés 1 800,00 + 44587 TVA sur avoirs à établir 360,00 | **4198** Clients – RRR à accorder et autres avoirs à établir 2 160,00 |

Conséquence : le **résultat 2025 est surévalué de 1 800 €** avant impôt et le résultat 2026 sous-évalué d'autant. L'omission est **non significative** à l'échelle de l'Imprimerie (CA de 6,8 M€) : pas de correction d'erreur à présenter en annexe ; l'écriture de 2026 reste en résultat 2026. Fiscalement, la charge est déductible en 2026 (l'écart temporaire n'a pas d'incidence sur le taux d'IS, 25 % les deux années).

## 2. Calculs

| Cas | Élément | Montant |
|---|---|---|
| Confluent | Trop-perçu = 2e paiement | 6 330,00 |
| Alpenblick | Facture 4 250,00 – reçu 4 232,00 | 18,00 (frais bancaires) |
| Hexa Com | Remise 15 % × 12 000,00 HT | 1 800,00 HT |
| | TVA 20 % | 360,00 |
| | Avoir TTC | 2 160,00 |
| | Incidence sur le résultat 2025 (omission) | + 1 800,00 (surévaluation) |
| | Incidence sur le résultat 2026 | – 1 800,00 |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 13/02/2026 | VT | 7091 | RRR accordés sur ventes de produits finis | AV-26-007 Hexa Com (FA-25-1190) | 1 800,00 | |
| 13/02/2026 | VT | 44571 | TVA collectée | AV-26-007 Hexa Com | 360,00 | |
| 13/02/2026 | VT | 411HEX | Client Agence Hexa Com | AV-26-007 Hexa Com | | 2 160,00 |
| 20/02/2026 | BQ | 411HEX | Client Agence Hexa Com | Remboursement AV-26-007 | 2 160,00 | |
| 20/02/2026 | BQ | 512 | Banque | Remboursement AV-26-007 | | 2 160,00 |
| 12/09/2026 | BQ | 512 | Banque | VIR Confluent FA-26-0812 | 6 330,00 | |
| 12/09/2026 | BQ | 411CON | Client Éditions du Confluent | VIR Confluent FA-26-0812 | | 6 330,00 |
| 15/09/2026 | BQ | 512 | Banque | PRLV SEPA Confluent FA-26-0812 (doublon) | 6 330,00 | |
| 15/09/2026 | BQ | 411CON | Client Éditions du Confluent | PRLV SEPA – doublon (solde créditeur) | | 6 330,00 |
| 02/10/2026 | BQ | 512 | Banque | Encaissement Alpenblick FA-26-0870 | 4 232,00 | |
| 02/10/2026 | BQ | 627 | Services bancaires et assimilés | Frais banque intermédiaire Alpenblick | 18,00 | |
| 02/10/2026 | BQ | 411ALP | Client Verlag Alpenblick | Règlement FA-26-0870 | | 4 250,00 |
| 06/10/2026 | BQ | 411CON | Client Éditions du Confluent | Remboursement trop-perçu FA-26-0812 | 6 330,00 | |
| 06/10/2026 | BQ | 512 | Banque | Remboursement trop-perçu FA-26-0812 | | 6 330,00 |
| | | | | **Totaux** | **27 560,00** | **27 560,00** |

**Si le doublon n'avait pas été remboursé avant la clôture** (écriture d'inventaire, extournée à l'ouverture) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/N | OD | 411CON | Client Éditions du Confluent | Reclassement client créditeur | 6 330,00 | |
| 31/12/N | OD | 4191 | Clients – avances reçues / clients créditeurs | Reclassement client créditeur | | 6 330,00 |
| | | | | **Totaux** | **6 330,00** | **6 330,00** |

## 4. Points d'attention / pièges

- **Ne jamais passer un trop-perçu en produit** pour « solder » un compte.
- **Clients créditeurs** : à lister à chaque clôture (doublons, avoirs non imputés, acomptes) ; ce sont des dettes.
- **Exportation** : sans preuve de sortie (déclaration d'export apurée), l'exonération peut être remise en cause → TVA française due. Classer la preuve avec la facture.
- **Avoir sur exercice clos** : comptabilisé dans l'exercice de son émission ; la TVA se régularise sur la déclaration de la période de l'avoir. Mais la question à se poser est toujours : **le fait générateur de la réduction existait-il à la clôture et était-il connu avant l'arrêté ?** Si oui → 4198 à la clôture précédente.
- **Petits écarts de paiement** : définir avec le client un **seuil de tolérance** documenté (par exemple 20 €) en deçà duquel l'écart est passé en charge sans relance — à valider par la DAF.

## 5. Ce qu'un senior ferait en plus

**Réponse au commissaire aux comptes (projet pour Sabine) :**
> L'avoir AV-26-007 du 13/02/2026 (1 800 € HT) a été comptabilisé en 2026 en diminution du chiffre d'affaires (compte 7091), la TVA étant régularisée sur la déclaration de février 2026. Il se rapporte à une non-conformité d'une livraison du 17/12/2025, réclamée le 08/01/2026, soit avant l'arrêté des comptes 2025 : un avoir à établir aurait dû être constaté au 31/12/2025. Compte tenu de son montant (1 800 €, soit 0,03 % du CA), cette omission est non significative ; l'écriture est maintenue en 2026. Pour la clôture 2026, nous avons mis en place une revue systématique des réclamations clients reçues entre la clôture et l'arrêté des comptes.

**Réponse aux Éditions du Confluent** : confirmation écrite du remboursement de 6 330 € effectué le 06/10/2026, avec la référence du virement — et vérification que le mandat SEPA ne déclenchera pas un nouveau prélèvement.

**Procédure** : ajouter à la PBC list (*Prepared By Client*) du CAC un état des **clients créditeurs**, des **avoirs émis après la clôture** et des **réclamations ouvertes** à la date d'arrêté.

## 6. Références

- PCG : comptes 4191, 4198, 44587, 7091, 627 ; traitement des événements postérieurs à la clôture.
- Code de commerce : art. L. 110-4 (prescription de 5 ans), art. L. 123-21 (rattachement des produits et charges à l'exercice), art. L. 441-9 (factures rectificatives).
- CGI : art. 262 I (exportations), art. 272-1 (régularisation de la TVA en cas de réduction de prix), art. 289 (factures rectificatives).
- Directive 2006/112/CE : art. 90 (réduction de la base d'imposition après l'opération).
