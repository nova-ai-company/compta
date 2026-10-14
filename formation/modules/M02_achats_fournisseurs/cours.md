# M02 — Le cycle achats et fournisseurs

> **Objectif du module.** Comptabiliser n'importe quelle facture d'achat — française, européenne, américaine, de sous-traitant BTP, de carte carburant, de note de frais — avec le bon compte, la bonne TVA (récupérable ou non, autoliquidée ou non) et au bon moment. C'est le cycle où le junior fait le plus d'erreurs « silencieuses » : une TVA déduite à tort ou une autoliquidation oubliée ne se voit pas dans la balance, mais se voit très bien en contrôle fiscal.

!!! abstract "En clair — ce module en 5 idées"
    1. Chaque achat va dans le compte qui décrit sa nature. Ce qui est transformé va en 601 (la farine de C01 Boulangerie Dupain), ce qui est revendu tel quel va en 607 (les vêtements de C09 Mode & Co), les consommations courantes vont en 606.
    2. Une réduction de prix écrite **sur** la facture ne s'enregistre pas : on saisit directement le prix réduit. Une réduction accordée **plus tard** par un avoir va en 609. Une réduction pour paiement rapide (escompte) est un produit financier (765).
    3. Facture d'un fournisseur étranger sans TVA ? Réflexe : **autoliquidation**. Vous déclarez vous-même la TVA due et vous la déduisez en même temps. Exemple : C19 Asia Trading, qui importe des luminaires de Chine.
    4. Toute la TVA payée ne se récupère pas : rien sur l'achat d'une voiture de tourisme, 80 % sur son carburant, rien sur l'hôtel ou le train, rien sur un cadeau de plus de 73 € TTC.
    5. À la fin de l'exercice, chaque charge doit tomber dans la bonne année (factures non parvenues, avoirs à recevoir, charges payées d'avance). Et depuis le 01/09/2026, la facture reçue par la plateforme est l'original : le PDF reçu en plus par e-mail est une copie, à ne pas saisir une deuxième fois.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | 401 Fournisseurs | Le compte de ce que l'entreprise doit à ses fournisseurs. | Facture de farine pas encore payée. |
    | 60x Achats | Les comptes où l'on enregistre ce que l'entreprise achète. | 607 pour les marchandises revendues. |
    | TVA déductible (44566) | La TVA payée sur les achats, que l'entreprise récupère. | 20 € de TVA sur un achat de 100 € HT. |
    | Remise / rabais / ristourne | Remise : réduction pour grosse commande. Rabais : pour un défaut. Ristourne : sur tous les achats de l'année. | Ristourne de fin d'année de C12 Pharmacie Centrale. |
    | Escompte | Une réduction accordée parce qu'on paie plus tôt que prévu. | 2 % si paiement sous 10 jours. |
    | Avoir | Le document du fournisseur qui réduit ou annule une facture. | Avoir pour un retour de marchandises. |
    | Acompte (4091) | Une somme payée d'avance au fournisseur, avant la facture finale. | 30 % versés à la commande d'une machine. |
    | Consignation | Un emballage facturé mais à rendre (palette, fût). Ce n'est pas un achat. | Fûts de bière d'un restaurant. |
    | Autoliquidation | C'est l'acheteur qui déclare la TVA à la place du fournisseur, et la déduit en même temps. | Sous-traitant du BTP pour C02 Bâtisseurs du Sud. |
    | Acquisition intracommunautaire | Un achat de biens à un fournisseur d'un autre pays de l'Union européenne. | Tissus achetés en Italie. |
    | Importation / DAU | Un achat de biens hors Union européenne ; le DAU est le document de douane. | Luminaires chinois de C19 Asia Trading. |
    | VP / VU | VP : voiture de tourisme (transport de personnes). VU : utilitaire (transport de marchandises). | Camionnette « CTTE » = VU. |
    | FNP (408) | Facture non parvenue : le bien est reçu avant la clôture, la facture arrive après. | Livraison du 29/09 facturée le 05/10 chez C03 Garage Martin. |
    | CCA (486) | Charge constatée d'avance : la part d'une facture qui concerne l'année suivante. | Assurance payée pour 12 mois à cheval sur deux exercices. |
    | LCR | Une traite : le fournisseur se fait payer via la banque à une date convenue. | Comptes 401 → 403 → 512. |
    | PA | La plateforme agréée qui transmet les factures électroniques. | Source de l'original depuis le 01/09/2026. |

---

## 1. Les comptes d'achats : où va quoi ?

> 🟢 **En clair :** le numéro du compte dit ce qu'on a acheté. La bonne question à se poser : « est-ce transformé, revendu tel quel, consommé, ou est-ce un service ? ». Un mauvais compte fausse les marges et le calcul des stocks.

| Compte | Contenu | Exemple du portefeuille |
|---|---|---|
| **601** Achats stockés – matières premières (et fournitures) | Ce qui est transformé | Farine de la Boulangerie Dupain (C01), bois de la Menuiserie (C24) |
| **602** Achats stockés – autres approvisionnements (6021 matières consommables, 6022 fournitures consommables, 6026 emballages) | Ce qui est consommé ou incorporé sans être la matière principale | Quincaillerie, colle, vernis ; emballages |
| **604** Achats d'études et prestations de services | Prestations **incorporées directement** aux ouvrages ou produits | Hébergement cloud d'un éditeur SaaS (C08), études incorporées à un ouvrage |
| **606** Achats non stockés de matières et fournitures (6061 énergie, eau, carburant ; 6063 petit équipement ; 6064 fournitures administratives ; 6068 autres) | Consommations courantes | Électricité, carburant, petit outillage < 500 € HT |
| **607** Achats de marchandises | Ce qui est **revendu en l'état** | Vêtements de Mode & Co (C09), boissons revendues |
| **608** | Compte de récapitulation des frais accessoires incorporés aux achats (si l'entreprise choisit de les y suivre) | Droits de douane, transport |
| **609** RRR obtenus sur achats (6091 à 6098 selon la nature de l'achat) | Rabais, remises, ristournes **obtenus hors facture** (avoirs ultérieurs) | Ristourne de fin d'année de la Pharmacie Centrale (C12) |
| **61 / 62** Services extérieurs | Sous-traitance (611), locations (613), entretien (615), assurances (616), honoraires et commissions (622), publicité et cadeaux (623), transports (624), déplacements, missions, réceptions (625), télécom (626), services bancaires (627) | |

**Frais accessoires d'achat** (transport, droits de douane, commissions, assurance transport) : deux méthodes admises — les **incorporer** au coût d'achat (601/607, éventuellement via 608), ou les comptabiliser **par nature** (6241 Transports sur achats, etc.). Le choix doit être **permanent** et cohérent avec la valorisation des stocks (le coût d'acquisition des stocks inclut les frais accessoires dans tous les cas).

> 🟢 **En clair :** les frais payés en plus du prix (transport, douane…) peuvent soit être ajoutés au compte d'achat, soit être enregistrés à part dans leur propre compte. Les deux sont permis, mais il faut garder le même choix chaque année. Et pour calculer la valeur du stock, on les compte toujours.

---

## 2. Réductions de prix : remises, rabais, ristournes, escompte

> 🟢 **En clair :** il existe quatre sortes de réductions de prix, et elles ne s'enregistrent pas de la même façon. Retenez la règle simple : réduction sur la facture → on saisit le prix net ; réduction plus tard par avoir → 609 ; réduction pour paiement rapide → 765.

| Réduction | Définition | Si elle figure **sur la facture d'origine** | Si elle est accordée **après** (avoir) |
|---|---|---|---|
| **Remise** | Réduction pour importance de la commande, qualité de client | On comptabilise le **net** (la remise ne s'enregistre pas) | 609x |
| **Rabais** | Réduction pour défaut de qualité, retard de livraison | Net | 609x |
| **Ristourne** | Réduction calculée sur l'ensemble des achats d'une période (fin d'année) | Net (rare) | 609x ; si non encore reçue à la clôture → **avoir à recevoir 4098** |
| **Escompte** | Réduction **financière** pour paiement anticipé | Produit financier **765 Escomptes obtenus** | 765 |

**Retour de marchandises** : l'avoir annule tout ou partie de l'achat → **crédit du compte d'achat** (601/607), pas du 609.

**TVA** : toute réduction de prix diminue la base imposable ; sur un avoir, le client **reverse** la TVA déduite (crédit 44566). Pour l'escompte, la facture doit indiquer la TVA réduite, ou le fournisseur doit émettre un avoir : sans cela, le client garde en principe la TVA déduite sur le prix initial et le fournisseur la TVA collectée correspondante (point à vérifier sur chaque facture).

> 🟢 **En clair :** quand le prix baisse, la TVA baisse aussi. Si un avoir arrive, votre client doit rendre la part de TVA qu'il avait récupérée en trop. Pour l'escompte, regardez si la facture ou un avoir montre bien la TVA réduite.

> ⚠️ **Erreur classique :** passer une remise figurant sur la facture en 609. Elle n'apparaît pas du tout : on enregistre le net commercial.

**Écritures types**

| Opération | Débit | Crédit |
|---|---|---|
| Facture avec remise et escompte | 601/607 (net commercial) ; 44566 (TVA sur net financier) | 765 (escompte) ; 401 (net à payer) |
| Avoir pour retour | 401 | 601/607 ; 44566 |
| Avoir pour rabais / ristourne | 401 | 609x ; 44566 |
| Avoir à recevoir à la clôture | 4098 | 609x ; 44586 |

---

## 3. Acomptes versés, emballages, transport

> 🟢 **En clair :** trois cas fréquents. Une somme payée d'avance au fournisseur reste une avance (4091) jusqu'à la facture finale. Un emballage à rendre (palette, fût) n'est pas un achat tant qu'il n'est pas gardé. Le transport suit des règles de TVA différentes selon qui le facture.

**Acompte versé** : 4091 « Fournisseurs – avances et acomptes versés sur commandes ». La TVA est exigible chez le fournisseur à l'encaissement de l'acompte (biens comme services) ; le client la déduit sur la base de la **facture d'acompte**.

| Opération | Débit | Crédit |
|---|---|---|
| Facture d'acompte reçue et payée | 4091 (HT) ; 44566 (TVA) | 512 (ou 401 puis 512) |
| Facture définitive | 6xx (total HT) ; 44566 (TVA sur le solde) | 4091 (acompte HT) ; 401 (net à payer) |

> 💡 **Réflexe senior :** quand le fournisseur est un **prestataire de services sans option pour les débits**, sa TVA n'est exigible qu'à l'encaissement : vous ne la déduisez **qu'au paiement**. C'est précisément l'information que donne la nouvelle mention obligatoire « option pour le paiement de la TVA d'après les débits ».

**Emballages consignés** (palettes, fûts, caisses) : la consignation n'est pas un achat.

| Opération | Débit | Crédit |
|---|---|---|
| Consignation facturée | 4096 Fournisseurs – créances pour emballages et matériel à rendre | 401 |
| Retour des emballages (déconsignation) | 401 | 4096 |
| Emballages conservés (non rendus) | 6026 Emballages (+ TVA) | 4096 |

**Transport** : facturé par le vendeur → suit le taux de TVA de la marchandise (frais accessoires de la livraison) ; facturé par un transporteur → 20 %, compte 6241.

---

## 4. Les achats à l'international et l'autoliquidation

> 🟢 **En clair :** quand le fournisseur est à l'étranger (ou dans certains cas comme la sous-traitance BTP), il ne facture pas de TVA. C'est votre client qui la déclare lui-même, puis la déduit aussitôt : le plus souvent, cela ne coûte rien, mais l'oublier est sanctionné. Exemple : C19 Asia Trading pour ses luminaires importés de Chine.

**Règle générale** : quand le fournisseur n'est pas établi en France (ou dans les cas prévus par la loi : sous-traitance BTP, etc.), c'est **l'acheteur assujetti qui « autoliquide » la TVA** : il la déclare comme due et, dans le même temps, la déduit (si ses droits à déduction sont complets). L'opération est neutre en trésorerie mais **doit être déclarée** ; l'omission est sanctionnée (CGI art. 1788 A).

| Situation | Fondement | TVA due (crédit) | TVA déductible (débit) | Ce qu'on vérifie |
|---|---|---|---|---|
| **Acquisition intracommunautaire de biens** (fournisseur UE) | CGI art. 256 bis | 4452 TVA due intracommunautaire | 445662 | N° TVA du fournisseur et le nôtre sur la facture ; mention d'exonération ; transport réel entre deux États |
| **Prestation de services d'un prestataire UE** (règle générale B2B) | CGI art. 259 et 283-2 | 4452 (sous-compte services) | 445662 (sous-compte) | Mention « autoliquidation » |
| **Prestation de services d'un prestataire hors UE** | CGI art. 259 et 283-2 | 4452 (ou sous-compte « TVA autoliquidée hors UE ») | 445662 (sous-compte) | Conversion en euros au taux du jour d'exigibilité |
| **Importation de biens** (hors UE) | Autoliquidation **obligatoire** depuis le 01/01/2022 pour les assujettis identifiés en France | Sous-compte de 4452 « TVA import autoliquidée » | Sous-compte de 44566 | DAU, valeur en douane, droits de douane (non récupérables → coût d'achat) |
| **Sous-traitance BTP** | CGI art. 283-2 nonies | Sous-compte de 4457 « TVA autoliquidée » | Sous-compte de 44566 | Contrat de sous-traitance, travaux immobiliers, mention « Autoliquidation » |

**Exigibilité** :
- acquisition intracommunautaire de biens : le 15 du mois suivant la livraison, ou à la date de la facture si elle est émise avant ;
- services : à l'achèvement de la prestation (ou au paiement d'un acompte), et pour les prestations continues, à chaque période ;
- importation : à la mise à la consommation (DAU).

Les opérations autoliquidées figurent sur des **lignes dédiées** de la CA3 (vérifiez la ligne sur le formulaire en vigueur ; la ligne « acquisitions intracommunautaires » n'est pas celle des services, ni celle des importations).

**Importation — écriture type**

| Débit | Crédit |
|---|---|
| 607 (valeur facturée au cours du jour) ; 607/608 ou 6xx (droits de douane, non récupérables) ; sous-compte 44566 TVA import | 401 fournisseur étranger ; 401/411 transitaire ou administration des douanes (droits) ; sous-compte 4452 TVA import |

Base de la TVA à l'importation = **valeur en douane** + droits de douane + frais accessoires jusqu'au premier lieu de destination en France.

> 🟢 **En clair :** pour une marchandise venue hors d'Europe, la TVA se calcule sur la valeur déclarée en douane, plus les droits de douane, plus les frais pour l'acheminer en France. Les droits de douane ne se récupèrent pas : ils augmentent le coût d'achat.

> ⚠️ **Erreur classique :** une facture étrangère sans TVA saisie « TVA 0 ». Toute facture d'un fournisseur non établi en France doit déclencher la question « autoliquidation ? ».

> ⚠️ **Erreur classique (inverse) :** un fournisseur établi en France ou à l'étranger qui **facture la TVA à tort** sur une opération autoliquidée (ex. sous-traitant BTP). Cette TVA n'est **pas déductible** par le client (elle est due par celui qui l'a facturée, CGI art. 283-3) : on exige une facture rectificative et on autoliquide.

**Dettes en devises** (renvoi M09) : la facture est convertie au **cours du jour de l'opération** ; l'écart au paiement est une perte (666) ou un gain (766) de change ; à la clôture, les dettes non réglées sont réévaluées (écarts de conversion 476/477 et provision pour perte de change).

> 🟢 **En clair :** une facture en dollars est convertie en euros au cours du jour. Si le dollar a bougé au moment du paiement, la différence est une perte ou un gain de change. Le détail de la clôture est vu au module M09.

---

## 5. Carburant, véhicules, frais de déplacement : la TVA récupérable

> 🟢 **En clair :** sur certaines dépenses, l'entreprise ne récupère pas (ou pas toute) la TVA. Tout dépend du type de véhicule (tourisme ou utilitaire) et de la nature de la dépense (repas, hôtel, train, cadeau). Regardez la carte grise et la facture avant de saisir la TVA.

### 5.1 Véhicules et carburants

| Dépense | Véhicule de tourisme (VP) | Véhicule utilitaire (VU) / poids lourd |
|---|---|---|
| Achat, location, entretien, réparations, pièces | **Non déductible** | Déductible |
| Gazole | **80 %** | 100 % |
| Essence (SP95, SP98, E10) | **80 %** (alignement achevé en 2022) | 100 % |
| Superéthanol E85, GPL, GNV, électricité | Règles spécifiques — **à vérifier** dans le BOFiP en vigueur | 100 % |
| Lavage, parking lié au véhicule | Non déductible (services afférents à un bien exclu) | Déductible |
| Péages autoroutiers | En principe déductible (dépense de déplacement de l'entreprise) — **à confirmer** pour les VP | Déductible |

Un **VP** est un véhicule conçu pour le transport de personnes ou à usage mixte (y compris une berline de société). Un **VU** est conçu pour le transport de marchandises (carte grise : genre « CTTE », camionnette ; poids lourds). Les pick-up et véhicules « société » dérivés de VP ont des règles particulières : consultez la carte grise.

**Remboursement partiel de TICPE** pour les transporteurs (véhicules ≥ 7,5 t) : créance sur l'État, demande périodique ; à traiter en fin de période (taux à vérifier chaque année).

### 5.2 Frais de déplacement, réception, cadeaux

| Dépense | TVA déductible ? | Compte |
|---|---|---|
| Restaurant (repas d'affaires, repas en déplacement), facture **au nom de l'entreprise** | **Oui** si engagé dans l'intérêt de l'exploitation | 6257 Réceptions / 6256 Missions |
| **Hébergement** (hôtel) des dirigeants et salariés | **Non** (logement du personnel et des dirigeants exclu) | 6251 Voyages et déplacements |
| **Transport de personnes** (train, avion, taxi, VTC) | **Non** (exclu) | 6251 |
| Cadeaux ≤ **73 € TTC** par bénéficiaire et par an (*valeur à vérifier chaque année*) | **Oui** | 6234 Cadeaux à la clientèle |
| Cadeaux > 73 € TTC | **Non** (pour la totalité de la TVA) | 6234 |
| Ticket CB sans facture | **Non** | selon nature, et justification à obtenir |

**Fiscalement** (IS/IR) : les frais de réception et cadeaux sont déductibles s'ils sont engagés dans l'intérêt de l'entreprise et justifiés (nom des bénéficiaires, objet) ; certains frais généraux doivent figurer sur le **relevé détaillé** prévu par le CGI au-delà de seuils (à vérifier chaque année).

**Note de frais** : la note du salarié ou du dirigeant récapitule les dépenses ; elle doit être accompagnée des **justificatifs** (factures). La dette envers le salarié se constate en 421 / 4286 (ou en 467 pour un mandataire selon l'organisation du dossier) ; un dirigeant associé peut aussi être crédité en compte courant (455).

> 💡 **Réflexe senior :** chez une **holding animatrice** ou toute société **assujettie partielle** (Delta Invest, C10), la TVA déductible sur les frais généraux est en outre limitée par le **coefficient de déduction** de l'entreprise. Deux filtres successifs : (1) la dépense ouvre-t-elle droit à déduction ? (2) dans quelle proportion (coefficient) ?

---

## 6. Les opérations de fin de période

> 🟢 **En clair :** à la clôture, chaque dépense doit être dans la bonne année. Bien reçu mais facture pas encore arrivée : on l'enregistre quand même (FNP). Facture payée pour l'année suivante : on retire la part concernée (CCA). Ces écritures sont annulées le premier jour de l'exercice suivant.

| Opération | Quand | Écriture | Extourne |
|---|---|---|---|
| **Facture non parvenue (FNP)** | Bien livré / service rendu avant la clôture, facture reçue après | D 6xx (HT) ; D 44586 (TVA) / C 408 | À l'ouverture |
| **Avoir à recevoir** (ristourne, retour) | Réduction acquise avant la clôture, avoir non reçu | D 4098 / C 609x (ou 6xx) ; C 44586 | À l'ouverture |
| **Charge constatée d'avance** | Facture reçue pour une période postérieure | D 486 / C 6xx | À l'ouverture |
| **Fournisseurs débiteurs** | Solde débiteur d'un compte 401 (avoir non imputé, paiement en double) | Reclassement en 409x | — |

**Effets à payer (LCR)** : quand le fournisseur tire une lettre de change relevé que l'entreprise accepte (« bon à payer » via la banque) :

| Opération | Débit | Crédit |
|---|---|---|
| Acceptation de la LCR | 401 | 403 Fournisseurs – effets à payer |
| Paiement à l'échéance | 403 | 512 |

À la clôture, une LCR acceptée non échue reste en **403** (dette fournisseur, rubrique « dettes fournisseurs » du bilan).

---

## 7. La réception des factures électroniques via la PA (depuis le 01/09/2026)

> 🟢 **En clair :** les grandes entreprises et les ETI envoient désormais leurs factures par une plateforme agréée. Pour ces fournisseurs, c'est la facture de la plateforme qui compte. Si le client vous transfère aussi le PDF par e-mail, ne le saisissez pas : vous auriez la même facture en double.

Depuis le **01/09/2026**, **toutes** les entreprises assujetties doivent pouvoir **recevoir** des factures électroniques via une **plateforme agréée** ; les **GE et ETI** doivent **émettre** électroniquement depuis la même date ; les PME, TPE et micro-entreprises émettront au **01/09/2027**. Conséquences pour le cycle achats :

| Point | Ce que vous faites |
|---|---|
| **Source de vérité** | Pour un fournisseur qui facture via PA, l'**original** est le flux électronique ; un PDF reçu par e-mail est une copie → **ne pas l'intégrer** (risque de doublon). |
| **Statuts** | Le client peut **refuser** une facture (statut transmis au fournisseur via les plateformes) : utile pour une facture erronée (mauvais taux, mauvais destinataire). Une facture refusée devra être annulée par le fournisseur (avoir) avant réémission. |
| **Données structurées** | SIREN, taux, montants par taux, nature de l'opération (biens / services), option pour les débits : la pré-comptabilisation est plus fiable… à condition que le paramétrage des comptes soit juste. |
| **Transition** | Jusqu'au 01/09/2027, cohabitent : flux PA (GE/ETI), PDF et papier (PME), factures étrangères (hors réforme, mais **e-reporting** des achats auprès de non-établis). |

> 💡 **Réflexe senior :** tenez, pour chaque client, une **liste des fournisseurs « PA »** et paramétrez l'outil pour bloquer les PDF de ces fournisseurs. Et vérifiez, sur les factures reçues, la **mention de l'option pour les débits** : elle conditionne le mois de déduction de la TVA sur les services.

---

## 8. Checklist de fin de module

- [ ] Je choisis entre 601 / 602 / 604 / 606 / 607 / 61-62 sans hésiter, et je sais où vont les frais accessoires.
- [ ] Je ne comptabilise pas une remise sur facture ; je distingue retour (crédit 60x) et rabais/ristourne (609).
- [ ] Je passe l'escompte obtenu en 765 et je calcule la TVA sur le net financier.
- [ ] Je traite un acompte versé (4091) et la facture définitive qui l'impute.
- [ ] Je sais traiter une consignation d'emballages (4096).
- [ ] Je passe l'autoliquidation pour : acquisition intracom de biens, services UE, services hors UE, importation, sous-traitance BTP.
- [ ] Je refuse de déduire une TVA facturée à tort sur une opération autoliquidée.
- [ ] Je sais appliquer 80 % / 100 % sur le carburant selon le véhicule, et exclure hébergement, transport de personnes, cadeaux > 73 € TTC.
- [ ] Je combine exclusions et coefficient de déduction chez un assujetti partiel.
- [ ] Je passe FNP, avoirs à recevoir, CCA, et je reclasse les fournisseurs débiteurs.
- [ ] Je traite une LCR (401 → 403 → 512).
- [ ] Je sais quelle est la pièce originale (flux PA, papier, PDF) et j'élimine les doublons.

## À retenir en 30 secondes

- Le compte d'achat dépend de ce qu'on fait du bien : transformé (601), revendu tel quel (607), consommé (606), service (61/62).
- Remise sur la facture : on saisit le net. Avoir reçu plus tard : 609. Escompte : 765.
- Facture étrangère sans TVA : pensez tout de suite « autoliquidation ».
- Une TVA facturée à tort ne se déduit pas : on demande une facture rectificative.
- Voiture de tourisme : pas de TVA sur l'achat ni l'entretien, 80 % sur le carburant. Hôtel, train, taxi : pas de TVA.
- À la clôture : factures non parvenues, avoirs à recevoir et charges payées d'avance, pour que chaque charge tombe dans la bonne année.
- La facture reçue par la plateforme est l'original : le PDF en plus est un doublon.
