# Corrigé E01-03 — La boîte à chaussures de septembre

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-03](../exercices/E01-03_boite-a-chaussures-dupain.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Pour chaque pièce, trois questions dans l'ordre :
1. **Quelle est la nature de la pièce ?** Facture (→ AC ou VT), mouvement bancaire (→ BQ), mouvement d'espèces (→ CA), régularisation (→ OD).
2. **Quelle est la nature de la dépense ?** Elle détermine le compte de charge (ou d'immobilisation, ou de tiers si elle n'est pas professionnelle).
3. **Quelle TVA, et est-elle récupérable ?** Taux appliqué par le fournisseur, conditions de déduction (facture au nom de l'entreprise, dépense dans l'intérêt de l'exploitation, absence d'exclusion).

| N° | Pièce | Journal | Débit | Crédit | TVA / récupérable ? |
|---|---|---|---|---|---|
| 1 | Minoterie | AC | 601 Matières premières | 401 | 5,5 % – oui |
| 2 | Laiterie | AC | 601 Matières premières | 401 | 5,5 % – oui |
| 3 | Boissons | AC | 607 Marchandises (revendues en l'état) | 401 | 5,5 % et 20 % – oui |
| 4 | Électricité | AC | 6061 Fournitures non stockables | 401 | 20 % – oui |
| 5 | Loyer | AC | 6132 Locations immobilières | 401 | 20 % – oui (le bailleur a opté) |
| 6 | Assurance | BQ (prélèvement, avis d'échéance = pièce) | 616 Primes d'assurance | 512 | Pas de TVA (taxe sur les conventions d'assurance, non récupérable) |
| 7 | Z de caisse | VT | 530 / 5115 / 5118 | 701 / 707 / 44571 | Collectée 5,5 % / 10 % / 20 % |
| 8 | Titres-restaurant | BQ | 512 + 6278 + 44566 | 5118 | Commission à 20 % – oui |
| 9 | Madelin du gérant | BQ | 646 Cotisations sociales personnelles du gérant | 512 | Pas de TVA |
| 10 | URSSAF | BQ | 431 Sécurité sociale | 512 | Pas de TVA |
| 11 | Batteur 420 € HT | AC | 6063 Petit équipement | 401 | 20 % – oui |
| 12 | Vitrine 3 430 € HT | AC | 2154 Matériel (+ 44562) | 404 | 20 % – oui, sur immobilisation |
| 13 | Restaurant samedi soir | BQ | **4551 Compte courant Marc Dupain** (en l'état) | 512 | **Non** (dépense non justifiée comme professionnelle ; ticket sans facture) |
| 14 | Contravention | BQ | 658 Charges diverses de gestion courante (*subdivision selon la nomenclature 2025 du PCG*) | 512 | Hors champ ; **non déductible fiscalement** |
| 15 | Retrait DAB pour la caisse | BQ puis CA | 581 puis 530 | 512 puis 581 | — |

Points de raisonnement à retenir :
- **Pièce 3** : les boissons sont **revendues en l'état** → **607 Marchandises**, pas 601. Deux taux : sodas et jus 5,5 %, bières 20 %.
- **Pièce 7** : le pain, les viennoiseries et sandwichs fabriqués sont des **produits finis** (701), les boissons revendues des **marchandises** (707). Les CB et titres-restaurant ne sont pas encore « en banque » le soir du Z : on les passe en **comptes d'attente d'encaissement** (5115 CB à encaisser ; 5118 titres-restaurant à encaisser — sous-comptes de 511 « Valeurs à l'encaissement »), soldés à l'arrivée des fonds.
- **Pièce 8** : la commission de la centrale est un **service bancaire/financier facturé avec TVA** → 6278 « Autres frais et commissions sur prestations de services », TVA déductible.
- **Pièce 9** : les cotisations Madelin de Marc, gérant majoritaire (TNS), payées par la SARL constituent un élément de sa rémunération ; elles se comptabilisent dans le compte des cotisations personnelles du dirigeant (646) ; leur déductibilité **chez Marc** est encadrée par des plafonds (à vérifier lors de la déclaration de rémunération). Elles doivent être prévues par une décision de rémunération.
- **Pièce 13** : un samedi à 21 h 47, deux couverts, pas de nom de convive. Le post-it « c'est pour le boulot » n'est pas un justificatif. En l'état : débit du **compte courant de Marc** (la société a payé pour lui). Si Marc établit qu'il s'agissait d'un repas d'affaires (nom de l'invité, objet) et obtient une **facture** au nom de la SARL, on reclassera en 6257 « Réceptions » avec TVA déductible.
- **Pièce 14** : depuis le PCG 2025 (règlement ANC 2022-06), les amendes ne vont plus en charges exceptionnelles (ancien 6712) mais en **charges d'exploitation, classe 65**. Fiscalement, les amendes et pénalités sont **non déductibles** (CGI art. 39-2) → réintégration extra-comptable.
- **Pièce 15** : un retrait pour alimenter la caisse transite par **58 Virements internes** ; la contrepartie dans le journal de caisse est justifiée par le brouillard de caisse. Le 581 doit être soldé.

## 2. Calculs (détaillés, chaque montant justifié)

**Z de caisse (pièce 7)** — le Z donne des montants TTC par taux ; on extrait HT et TVA :

| Taux | TTC | HT = TTC / (1 + taux) | TVA |
|---|---|---|---|
| 5,5 % | 1 412,30 € | 1 412,30 / 1,055 = 1 338,67 € | 73,63 € |
| 10 % | 386,10 € | 386,10 / 1,10 = 351,00 € | 35,10 € |
| 20 % | 92,40 € | 92,40 / 1,20 = 77,00 € | 15,40 € |
| **Total** | **1 890,80 €** | **1 766,67 €** | **124,13 €** |

Contrôle des règlements : 650,00 + 1 040,80 + 200,00 = **1 890,80 €** ✓.

**Titres-restaurant (pièce 8)** : commission 1 860,00 × 4,5 % = 83,70 € HT ; TVA 83,70 × 20 % = 16,74 € ; net 1 860,00 – 83,70 – 16,74 = **1 759,56 €** ✓.

**Boissons (pièce 3)** : 210,00 × 5,5 % = 11,55 € ; 178,00 × 20 % = 35,60 € ; TTC 388,00 + 47,15 = **435,15 €** ✓.

**Vitrine (pièce 12)** : coût d'entrée = prix + frais de livraison et d'installation (frais directement attribuables) = 3 250,00 + 180,00 = **3 430,00 € HT** ; TVA 686,00 € ; TTC 4 116,00 €.

**Assurance (question 3)** : prime annuelle 1 386,00 € pour la période 01/09/2026 – 31/08/2027. Part de 2026 : 4 mois (septembre à décembre) ; part de 2027 : 8 mois.
Charge constatée d'avance au 31/12/2026 = 1 386,00 × 8 / 12 = **924,00 €**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/09/2026 | AC | 601 | Achats de matières premières | Minoterie MMO-26-1841 | 1 480,00 | |
| 02/09/2026 | AC | 44566 | TVA déductible sur ABS | Minoterie MMO-26-1841 | 81,40 | |
| 02/09/2026 | AC | 401MINO | Fournisseur Minoterie des Monts d'Or | Minoterie MMO-26-1841 | | 1 561,40 |
| 05/09/2026 | AC | 601 | Achats de matières premières | Laiterie du Pilat LP-9921 | 642,00 | |
| 05/09/2026 | AC | 44566 | TVA déductible sur ABS | Laiterie du Pilat LP-9921 | 35,31 | |
| 05/09/2026 | AC | 401LAIT | Fournisseur Laiterie du Pilat | Laiterie du Pilat LP-9921 | | 677,31 |
| 08/09/2026 | AC | 607 | Achats de marchandises | Boissons du Rhône BR-2026-3307 sodas/jus | 210,00 | |
| 08/09/2026 | AC | 607 | Achats de marchandises | Boissons du Rhône BR-2026-3307 bières | 178,00 | |
| 08/09/2026 | AC | 44566 | TVA déductible sur ABS | Boissons du Rhône BR-2026-3307 (11,55 + 35,60) | 47,15 | |
| 08/09/2026 | AC | 401BOIS | Fournisseur Boissons du Rhône | Boissons du Rhône BR-2026-3307 | | 435,15 |
| 10/09/2026 | AC | 6061 | Fournitures non stockables (énergie) | Énergie Lyon Métropole élec. août | 1 120,00 | |
| 10/09/2026 | AC | 44566 | TVA déductible sur ABS | Énergie Lyon Métropole élec. août | 224,00 | |
| 10/09/2026 | AC | 401ENER | Fournisseur Énergie Lyon Métropole | Énergie Lyon Métropole élec. août | | 1 344,00 |
| 01/09/2026 | AC | 6132 | Locations immobilières | SCI du Vieux Lyon loyer 09/2026 | 2 400,00 | |
| 01/09/2026 | AC | 44566 | TVA déductible sur ABS | SCI du Vieux Lyon loyer 09/2026 | 480,00 | |
| 01/09/2026 | AC | 401SCIV | Fournisseur SCI du Vieux Lyon | SCI du Vieux Lyon loyer 09/2026 | | 2 880,00 |
| 05/09/2026 | BQ | 616 | Primes d'assurance | Prlv AMC multirisque 09/2026-08/2027 | 1 386,00 | |
| 05/09/2026 | BQ | 512 | Banque | Prlv AMC multirisque 09/2026-08/2027 | | 1 386,00 |
| 30/09/2026 | VT | 530 | Caisse | Z 2026-0273 espèces | 650,00 | |
| 30/09/2026 | VT | 5115 | CB à encaisser | Z 2026-0273 CB | 1 040,80 | |
| 30/09/2026 | VT | 5118 | Titres-restaurant à encaisser | Z 2026-0273 titres-restaurant | 200,00 | |
| 30/09/2026 | VT | 701 | Ventes de produits finis (5,5 %) | Z 2026-0273 ventes 5,5 % | | 1 338,67 |
| 30/09/2026 | VT | 701 | Ventes de produits finis (10 %) | Z 2026-0273 ventes 10 % | | 351,00 |
| 30/09/2026 | VT | 707 | Ventes de marchandises (20 %) | Z 2026-0273 boissons 20 % | | 77,00 |
| 30/09/2026 | VT | 44571 | TVA collectée 5,5 % | Z 2026-0273 | | 73,63 |
| 30/09/2026 | VT | 44571 | TVA collectée 10 % | Z 2026-0273 | | 35,10 |
| 30/09/2026 | VT | 44571 | TVA collectée 20 % | Z 2026-0273 | | 15,40 |
| 18/09/2026 | BQ | 512 | Banque | Remb. titres-restaurant du 18/09 | 1 759,56 | |
| 18/09/2026 | BQ | 6278 | Autres frais et commissions | Commission titres-restaurant 4,5 % | 83,70 | |
| 18/09/2026 | BQ | 44566 | TVA déductible sur ABS | Commission titres-restaurant | 16,74 | |
| 18/09/2026 | BQ | 5118 | Titres-restaurant à encaisser | Remb. titres-restaurant du 18/09 | | 1 860,00 |
| 10/09/2026 | BQ | 646 | Cotisations sociales personnelles du gérant | Prlv Prévoyance Artisans Madelin M. Dupain 09/2026 | 96,00 | |
| 10/09/2026 | BQ | 512 | Banque | Prlv Prévoyance Artisans Madelin M. Dupain 09/2026 | | 96,00 |
| 15/09/2026 | BQ | 431 | Sécurité sociale | Prlv URSSAF cotisations 08/2026 | 3 412,00 | |
| 15/09/2026 | BQ | 512 | Banque | Prlv URSSAF cotisations 08/2026 | | 3 412,00 |
| 14/09/2026 | AC | 6063 | Fournitures d'entretien et petit équipement | Équip'Fournil EF-0577 batteur 5 L | 420,00 | |
| 14/09/2026 | AC | 44566 | TVA déductible sur ABS | Équip'Fournil EF-0577 | 84,00 | |
| 14/09/2026 | AC | 401EQUI | Fournisseur Équip'Fournil | Équip'Fournil EF-0577 | | 504,00 |
| 19/09/2026 | AC | 2154 | Matériel (vitrine réfrigérée) | Vitrines Lyonnaises VL-26-118 (dont install. 180) | 3 430,00 | |
| 19/09/2026 | AC | 44562 | TVA déductible sur immobilisations | Vitrines Lyonnaises VL-26-118 | 686,00 | |
| 19/09/2026 | AC | 404VITR | Fournisseur d'immobilisations Vitrines Lyonnaises | Vitrines Lyonnaises VL-26-118 | | 4 116,00 |
| 28/09/2026 | BQ | 4551 | Associé – compte courant Marc Dupain | CB Bouchon des Halles 26/09 (en attente justif.) | 78,00 | |
| 28/09/2026 | BQ | 512 | Banque | CB Bouchon des Halles 26/09 | | 78,00 |
| 21/09/2026 | BQ | 658 | Charges diverses de gestion courante (amendes) | Contravention stationnement fourgonnette 17/09 | 35,00 | |
| 21/09/2026 | BQ | 512 | Banque | Contravention stationnement fourgonnette 17/09 | | 35,00 |
| 28/09/2026 | BQ | 581 | Virements internes | Retrait DAB pour fonds de caisse | 300,00 | |
| 28/09/2026 | BQ | 512 | Banque | Retrait DAB pour fonds de caisse | | 300,00 |
| 28/09/2026 | CA | 530 | Caisse | Apport fonds de caisse (retrait DAB) | 300,00 | |
| 28/09/2026 | CA | 581 | Virements internes | Apport fonds de caisse (retrait DAB) | | 300,00 |
| 31/12/2026 | OD | 486 | Charges constatées d'avance | CCA assurance AMC 01-08/2027 (8/12) | 924,00 | |
| 31/12/2026 | OD | 616 | Primes d'assurance | CCA assurance AMC 01-08/2027 (8/12) | | 924,00 |
| | | | | **Totaux** | **21 799,66** | **21 799,66** |

> Le 44571 est ventilé par taux (sous-comptes 445711, 445712, 445713 selon le plan du dossier) : indispensable pour remplir la déclaration de TVA multi-taux. La date du loyer est celle de la quittance (terme d'avance, 1er du mois).

## 4. Points d'attention / pièges

- **Pièce 11 vs pièce 12 (question 4)** : le batteur (420 € HT) entre dans la **tolérance des 500 € HT** pour le petit matériel → charge (6063). La vitrine (3 430 € HT, durable) est une **immobilisation**, frais d'installation inclus. Ne pas oublier **44562** (et non 44566) et **404** (et non 401) : ces comptes alimentent des lignes spécifiques de la liasse et de la déclaration de TVA.
- **Le relevé bancaire n'est pas une pièce** pour une dépense : pour la pièce 13, c'est l'absence de facture qui oblige à imputer au compte courant.
- **Pièce 6** : l'assurance porte sur 12 mois à cheval sur 2026 et 2027 → **charge constatée d'avance** de 924,00 € au 31/12 (indépendance des exercices). Pas de TVA : la taxe sur les conventions d'assurance n'est pas de la TVA.
- **Pièce 14** : ne pas utiliser l'ancien compte 6712 ; et ne pas oublier la **réintégration fiscale** de l'amende sur le tableau 2033-B (régime simplifié d'imposition).
- **5118 / 5115** : ces comptes doivent se solder au fil des remboursements. Un solde ancien sur 5118 = titres perdus ou non remis.
- **58** : vérifiez qu'il est soldé en fin de mois ; un retrait sans apport correspondant en caisse est un prélèvement du gérant à imputer en 4551.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Questions à poser à Marc Dupain (par téléphone, après 14 h) :**
1. Le dîner du samedi 26/09 au Bouchon des Halles : avec qui, pour quel objet professionnel ? Pouvez-vous obtenir une **facture** au nom de la SARL ? À défaut, il reste à votre charge (compte courant).
2. La contravention : qui conduisait ? (Information utile pour la politique de désignation du conducteur ; dans tous les cas, l'amende reste non déductible.)
3. Le contrat Madelin : avez-vous la décision fixant votre rémunération qui prévoit sa prise en charge par la SARL ?
4. Il manque le **relevé du terminal CB** (remises de septembre) : pouvez-vous le déposer pour solder le 5115 ?
5. La vitrine : l'ancienne vitrine a-t-elle été mise au rebut ou vendue ? (Sortie d'actif à passer si elle figurait à l'immobilisé.)

**Contrôles :**
- rapprocher le total des Z du mois avec les remises en banque (espèces + CB + titres) ;
- vérifier que le fonds de caisse théorique correspond au comptage ;
- mettre à jour le tableau des immobilisations (vitrine, mise en service le 19/09/2026).

**Documentation du dossier** : noter la position retenue sur le ticket de restaurant et la conserver dans la feuille « Points en suspens » ; si Marc ne fournit rien, l'imputation au compte courant devient définitive.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC 2014-03 modifié par ANC 2022-06) : fonctionnement des comptes 511, 58, 486, 60x ; suppression du résultat exceptionnel « fourre-tout » (amendes en classe 65).
- CGI art. 39-2 : non-déductibilité des amendes et pénalités.
- CGI art. 271 et annexe II art. 230 : conditions de déduction de la TVA (dépense nécessaire à l'exploitation, facture).
- CGI art. 154 bis : déductibilité des cotisations Madelin chez le TNS (plafonds à vérifier chaque année).
- BOFiP BIC – Charges – immobilisations de faible valeur (tolérance 500 € HT).
- CGI art. 278-0 bis (taux de 5,5 % sur les produits alimentaires) et 279 (taux de 10 % sur la vente à consommer immédiatement) — taux selon la nature des produits.
