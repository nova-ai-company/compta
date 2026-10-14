# Corrigé E01-02 — Reconstituer la chaîne devis → BC → BL → facture

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-02](../exercices/E01-02_chaine-documentaire-batisseurs.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Le principe est le **rapprochement « 3 voies »** : ce qui a été **commandé** (devis signé + BC), ce qui a été **reçu** (BL, avec ses réserves) et ce qui est **facturé** doivent concorder. La référence de prix est le **devis signé** (il vaut contrat), la référence de quantité est le **BL** (ce qui a été effectivement accepté sur le chantier).

**Tableau de rapprochement**

| Élément | Devis D-2026-417 | BC-ACA-0812 | BL-77310 (21/08) + BL-77802 (02/09) | Facture F-2026-08-2291 | Écart |
|---|---|---|---|---|---|
| Parpaings | 2 400 u à 1,28 € | 2 400 u | 2 400 livrés – **60 cassés repris** = **2 340 acceptés** | 2 400 u | **+ 60 u facturés à tort** |
| Ciment | 120 sacs à 8,90 € | 120 | 120 | 120 | — |
| Treillis | 60 pan. à 24,50 € | 60 | 40 + 20 = 60 | 60 | Quantité OK, mais 20 panneaux **facturés le 31/08, livrés le 02/09** |
| Remise | **4 %** sur matériaux | « selon devis » | — | **3 %** | **– 1 point de remise** |
| Livraison | **Forfait unique 180 €** « quel que soit le nombre de rotations » | « forfait 180 € » | 2 rotations (la 2e due à la rupture de stock du fournisseur) | 2 × 180 € | **+ 180 € facturés à tort** |

**Trois écarts financiers** et **une anomalie de procédure** :
1. Les **60 parpaings cassés** au déchargement, repris par le chauffeur (réserve écrite et contresignée sur le BL), ne sont pas dus.
2. La **remise contractuelle est de 4 %**, pas 3 %.
3. La **2e livraison** résulte de la rupture de stock du fournisseur ; le devis prévoit un forfait unique.
4. La facture est datée du 31/08 alors que 20 treillis ont été livrés le 02/09 : elle ne précise pas les dates de livraison de chaque lot. Ce n'est pas ici un enjeu de montant (même exercice), mais c'est un défaut de piste d'audit — à la clôture, ce même décalage pourrait faire comptabiliser une charge sur le mauvais exercice.

**Faut-il laisser la facture en comptabilité ?** Oui. La facture a été reçue, elle est au nom de la société, elle a été intégrée : c'est une dette apparente. On ne la supprime pas ; on **bloque le paiement** et on **obtient un avoir**. Si l'avoir n'était pas reçu à la clôture du 31/12, on constaterait un **avoir à recevoir** (compte 4098) pour ne pas surévaluer la charge.

**La saisie de Nadia** est juste dans son principe (601, TVA, fournisseur) mais elle a noyé **360 € de transport dans le 601**. Incorporer les frais accessoires au coût d'achat est admis ; mais le plan de comptes de Bâtisseurs du Sud suit les transports sur achats en **6241** pour l'analyse par chantier. On reclasse.

## 2. Calculs (détaillés, chaque montant justifié)

**Ce qui est réellement dû**

| Ligne | Calcul | Montant |
|---|---|---|
| Parpaings | 2 340 × 1,28 | 2 995,20 € |
| Ciment | 120 × 8,90 | 1 068,00 € |
| Treillis | 60 × 24,50 | 1 470,00 € |
| Sous-total matériaux | | 5 533,20 € |
| Remise 4 % | 5 533,20 × 4 % = 221,328 | – 221,33 € |
| Matériaux nets | | 5 311,87 € |
| Livraison (forfait unique) | | 180,00 € |
| **Total HT dû** | | **5 491,87 €** |
| TVA 20 % | 5 491,87 × 20 % = 1 098,374 | **1 098,37 €** |
| **Total TTC dû** | | **6 590,24 €** |

**Ce qui est facturé** : HT 5 801,70 € ; TVA 1 160,34 € ; TTC 6 962,04 €.

**Avoir à réclamer**

| Composante | Calcul | HT |
|---|---|---|
| Matériaux (quantité + remise) | 5 441,70 – 5 311,87 | 129,83 € |
| dont 60 parpaings | 60 × 1,28 × 96 % = 73,73 € | |
| dont point de remise manquant | (5 441,70 – 5 311,87) – 73,73 = 56,10 € | |
| Livraison facturée à tort | | 180,00 € |
| **Total HT** | | **309,83 €** |
| TVA 20 % | 1 160,34 – 1 098,37 | **61,97 €** |
| **Total TTC** | | **371,80 €** |

Contrôle : 6 962,04 – 371,80 = **6 590,24 €** ✓.

> Pourquoi la décomposition de la remise ne fait pas « 1 % de 5 610 » (56,10 €) pile ? Parce que la remise s'applique sur une base qui a elle-même changé (60 parpaings en moins). La décomposition ci-dessus est cohérente : 73,73 + 56,10 = 129,83 €. Pour la réclamation, présentez simplement le recalcul complet de la facture, plus lisible qu'une décomposition d'écarts.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 08/10/2026 | AC | 401NEGO | Fournisseur Négoce BTP Lyonnais | Négoce BTP AV s/ F-2026-08-2291 (casse, remise, livraison) | 371,80 | |
| 08/10/2026 | AC | 601 | Achats de matières premières (matériaux) | Négoce BTP AV s/ F-2026-08-2291 | | 129,83 |
| 08/10/2026 | AC | 6241 | Transports sur achats | Négoce BTP AV s/ F-2026-08-2291 | | 180,00 |
| 08/10/2026 | AC | 44566 | TVA déductible sur ABS | Négoce BTP AV s/ F-2026-08-2291 | | 61,97 |
| 09/10/2026 | OD | 6241 | Transports sur achats | Reclassement transport F-2026-08-2291 | 360,00 | |
| 09/10/2026 | OD | 601 | Achats de matières premières (matériaux) | Reclassement transport F-2026-08-2291 | | 360,00 |
| 12/10/2026 | BQ | 401NEGO | Fournisseur Négoce BTP Lyonnais | Vir. Négoce BTP solde F-2026-08-2291 / AV | 6 590,24 | |
| 12/10/2026 | BQ | 512 | Banque | Vir. Négoce BTP solde F-2026-08-2291 / AV | | 6 590,24 |
| | | | | **Totaux** | **7 322,04** | **7 322,04** |

Après ces écritures, le compte 401NEGO se lettre : facture 6 962,04 (crédit) = avoir 371,80 + virement 6 590,24 (débits). Le 6241 porte 180,00 € (360,00 – 180,00) : le forfait de livraison réellement dû.

## 4. Points d'attention / pièges

- **Les réserves sur le BL sont la preuve.** Sans la mention « 60 parpaings cassés – repris par le chauffeur » contresignée, la réclamation serait très difficile. Le BL est aussi important que la facture.
- **Le devis signé fait foi** sur les prix et les conditions (remise, forfait). Le fournisseur ne peut pas modifier unilatéralement la remise.
- **Ne pas payer partiellement « au feeling »** (ex. payer 6 600 €) : le compte fournisseur resterait non lettrable et le litige ne serait pas documenté.
- **Pénalités de retard** : l'échéance (30/09) est dépassée. Les pénalités ne sont pas dues sur la partie contestée à juste titre ; mais tant que la réclamation n'a pas été envoyée, le fournisseur peut les réclamer sur la totalité. D'où l'urgence de formaliser la contestation.
- **TVA** : la TVA de 1 160,34 € a été déduite en août. L'avoir impose de **reverser** 61,97 € de TVA déductible sur la déclaration du mois de réception de l'avoir (octobre).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Message de réclamation (à faire signer par Karim Benali) :**

> Objet : Votre facture F-2026-08-2291 du 31/08/2026 — demande d'avoir
>
> Madame, Monsieur,
>
> Après rapprochement de votre facture avec votre devis D-2026-417 signé le 13/08/2026, notre bon de commande BC-ACA-0812 et vos bons de livraison BL-77310 et BL-77802, nous relevons les écarts suivants :
> 1. 60 parpaings cassés au déchargement et repris par votre chauffeur (réserve portée sur le BL-77310) ont été facturés ;
> 2. la remise appliquée est de 3 % au lieu des 4 % prévus au devis ;
> 3. la seconde livraison, rendue nécessaire par votre rupture de stock, a été facturée alors que le devis prévoit un forfait unique de 180 € HT.
>
> Le montant dû s'établit à 5 491,87 € HT, soit 6 590,24 € TTC. Nous vous remercions de nous adresser un avoir de 309,83 € HT (371,80 € TTC). Dès sa réception, nous procéderons au règlement du solde.
>
> Copies jointes : devis signé, BC, BL-77310 et BL-77802.

**Procédure interne (question 6).** Le défaut : **personne ne fait le rapprochement BL ↔ facture**. Karim « trouve que c'est trop cher » mais rien n'est formalisé ; Nadia saisit sans contrôle ; le chef de chantier signe les BL mais ne les transmet pas à la comptabilité de façon systématique. Recommandation écrite au client :
- le chef de chantier transmet chaque BL signé (photo ou scan) à Nadia dans les 48 h ;
- Nadia ne met en paiement qu'après rapprochement BC / BL / facture (case « bon à payer » datée et visée) ;
- tout écart déclenche une réclamation écrite sous 8 jours.

C'est la **piste d'audit fiable** exigée pour la TVA, et un vrai gain de marge sur un chantier : 309,83 € sur une seule facture de matériaux.

**Documentation du dossier** : classer la réclamation et l'avoir dans le dossier du chantier Les Acacias ; noter dans la feuille de révision du cycle achats « PAF : défaut de rapprochement BL/facture constaté — recommandation envoyée le … ».

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 289 VII : piste d'audit fiable entre la facture et la livraison de biens / prestation.
- BOFiP, TVA – Facturation – piste d'audit fiable (contrôles documentés et permanents).
- CGI, annexe II, art. 242 nonies A : la facture mentionne la date de la livraison si elle diffère de la date d'émission ; tout document rectificatif fait référence à la facture initiale.
- CGI art. 272-1 : régularisation de la TVA déduite en cas de réduction de prix (avoir).
- Code de commerce art. L. 441-9 : mentions de la facture, numéro de bon de commande.
- PCG : frais accessoires d'achat (incorporation au coût ou comptabilisation par nature).
