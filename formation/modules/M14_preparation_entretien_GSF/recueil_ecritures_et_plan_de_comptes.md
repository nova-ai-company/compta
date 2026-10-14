# M14 — Recueil d'écritures types et plan de comptes d'un groupe de propreté

> **À quoi sert ce document.** C'est votre « bible de poche » pour l'entretien d'aide-comptable chez GSF, puis pour vos premières semaines au poste. Un recruteur de groupe de propreté ne vous demandera pas de réciter le PCG : il vous montrera une facture (sous-traitant, intérim, LLD, marché public…) et vous demandera « vous la passez comment ? », puis « et qu'est-ce que vous contrôlez ? ». Chaque écriture ci-dessous répond aux deux questions.
>
> **Mode d'emploi :** lisez d'abord la partie 2 (plan de comptes), puis travaillez le recueil cycle par cycle en cachant les tableaux : essayez de trouver vous-même débit / crédit à partir du contexte et de la pièce, puis comparez. Terminez par le tableau récapitulatif (partie 4) et les 20 contrôles mensuels (partie 5), qui sont exactement ce qu'on attend d'une assistante comptable fournisseurs ou clients dans un groupe qui clôture **tous les mois**.

---

## 1. Avertissement

1. **Le plan de comptes réel de GSF n'est pas public.** Ni les numéros de comptes, ni les sous-comptes, ni les sections analytiques, ni l'ERP du groupe ne sont publiés (voir la fiche de recherche du module). Ce document présente un **plan de comptes type** d'un groupe de propreté et services associés, **conforme au PCG en vigueur pour les exercices ouverts depuis le 01/01/2025** (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06), avec des subdivisions réalistes telles qu'on les rencontre dans les groupes multi-sociétés et multi-établissements.
2. **Toutes les données chiffrées sont fictives** : montants, numéros de factures, codes tiers, noms de clients et de fournisseurs, sociétés du groupe. Les entités utilisées sont imaginaires :
   - **PROPRETÉ AZUR SAS** (« la filiale ») — société régionale fictive, 3 établissements : **ETB061** (Nice), **ETB062** (Cannes), **ETB083** (Toulon) ; exercice civil ; TVA au réel normal, **CA3 mensuelle**, **TVA sur les encaissements** (pas d'option pour les débits, sauf variante signalée) ;
   - **SIÈGE SERVICES SAS** (« la société tête » ou « la mère ») — holding animatrice fictive qui centralise la trésorerie (cash pooling), facture des management fees et est tête d'un groupe d'intégration fiscale (*hypothèse de travail : l'existence d'une intégration fiscale chez GSF est à vérifier*).
3. **Le PCG 2025 est appliqué strictement** dans tout le recueil :
   - **aucun compte 79** (les comptes de transferts de charges 791, 796 et 797 sont supprimés) : les IJSS en subrogation, remboursements d'assurance, etc. viennent **en diminution de la charge concernée** ou en produit par nature ;
   - **résultat exceptionnel restreint** aux événements majeurs et inhabituels : pénalités, amendes, écarts de règlement, créances irrécouvrables courantes restent en **exploitation** ; seules les **cessions d'immobilisations** restent en **675 / 775** ;
   - la quote-part de subvention d'investissement virée au résultat est en **747** ;
   - pénalités et amendes : **658** (*subdivision selon la nomenclature 2025 du PCG*) ;
   - gains et pertes de change sur opérations **commerciales** : **656 / 756** ; **666 / 766** réservés aux opérations financières.
4. **Chiffres qui changent chaque année** (taux d'intérêts moratoires, seuil des cadeaux, taux de cotisations, taux de CVAE, taux d'intérêt fiscalement déductible des comptes courants, etc.) : ils sont donnés « on retient… » — *valeur à vérifier chaque année*.
5. Les montants sont au format français **12 345,67** (en euros sauf mention contraire). **Chaque écriture a été contrôlée : total débit = total crédit.**

> 💡 **Réflexe senior :** en entretien, si l'on vous demande « quel compte utilisez-vous pour… ? », répondez d'abord par la **logique** (nature de la charge, tiers concerné, TVA, période) puis par le compte à 3 ou 4 chiffres du PCG, et terminez par « … et je vérifie le sous-compte prévu dans votre plan de comptes groupe ». C'est exactement ce que fait une professionnelle qui arrive dans un groupe dont le plan est paramétré dans l'ERP.

---

## 2. Plan de comptes type commenté

### 2.1 Architecture d'un plan de comptes de groupe de propreté

| Élément | Convention retenue dans ce document | Pourquoi |
|---|---|---|
| **Comptes généraux** | Numéro PCG complété à droite jusqu'à 6 chiffres dans l'ERP (ex. `706100`, `445740`). Dans les tableaux, on écrit le compte au niveau utile (ex. `44566`, `6022`, `706100`). | Le groupe impose un plan unique à toutes les filiales pour pouvoir consolider (« mapping » vers la liasse de consolidation). |
| **Comptes de tiers** | Comptes collectifs `401000`, `404000`, `411000`… + **comptes auxiliaires** par tiers : `F00412` (fournisseur), `C00218` (client). Les tiers groupe ont des collectifs dédiés (`4011`, `4112`, `451x`). | Le lettrage, les relances, la balance âgée et la réconciliation intragroupe se font sur l'auxiliaire. |
| **Sections analytiques** | Axe 1 **Établissement** (`ETB061`, `ETB062`, `ETB083`, `SIEGE`) ; axe 2 **Activité** (`PROP` propreté courante, `VITR` vitrerie, `REM` remise en état, `MULTI` multiservices, `3D` dératisation-désinsectisation-désinfection, `GDD` gestion déléguée des déchets) ; axe 3 **Contrat / site client** (`CT-2026-0418`…). | Chaque établissement est un centre de profit : le compte de résultat par établissement et la marge par contrat sont les indicateurs que suivent les chefs d'établissement. |
| **Journaux** | `VT` ventes, `AC` achats, `ACI` achats d'immobilisations, `BQ1`/`BQ2` banques, `PAIE` paie, `OD` opérations diverses, `ODG` opérations groupe, `EXT` extournes, `AN` à-nouveaux. | Séparer les flux pour les contrôles et les droits d'accès (l'assistante fournisseurs saisit en `AC`, pas en `PAIE`). |

> ⚠️ **Erreur classique :** croire que le numéro de sous-compte « est » le PCG. Le PCG fixe les comptes jusqu'à un certain niveau (souvent 4 ou 5 chiffres) ; les subdivisions au-delà appartiennent à chaque groupe. Exemple : le PCG définit **4011** comme « Fournisseurs – Achats de biens et prestations de services » et **4111** comme « Clients – Ventes de biens ou de prestations de services » ; dans le plan type ci-dessous, le groupe a **réaffecté** 4011 aux fournisseurs groupe et 4111 aux clients publics, ce qui est fréquent. L'important : la cohérence dans toutes les filiales et un mapping propre vers les comptes de la liasse.

### 2.2 Classe 1 — Capitaux, provisions, emprunts

| Compte | Intitulé | Usage dans une société de propreté |
|---|---|---|
| 101 | Capital | Filiales régionales : capital souvent modeste (ex. 200 000), détenu par la société tête. |
| 1061 / 1068 | Réserve légale / Autres réserves | Affectation du résultat en AG (voir écriture G05a). |
| 110 / 119 | Report à nouveau créditeur / débiteur | |
| 120 / 129 | Résultat de l'exercice (bénéfice / perte) | |
| 131 | Subventions d'équipement | Aides régionales ou ADEME pour véhicules électriques, matériel à batteries. |
| 139 | Subventions d'investissement inscrites au compte de résultat | Contrepartie de la reprise en **747**. |
| 145 | Amortissements dérogatoires | Si amortissement fiscal plus rapide (rare sur ce type d'actifs). |
| 1511 | Provisions pour litiges | **Prud'hommes** (fréquents dans un secteur à fort effectif), litiges clients. |
| 1518 | Autres provisions pour risques | Pénalités contractuelles probables mais non chiffrées, garanties. |
| 153 | Provisions pour pensions et obligations similaires | Indemnités de fin de carrière (IFC) si l'entité opte pour leur comptabilisation (méthode de référence). |
| 164 | Emprunts auprès des établissements de crédit | Financement de matériel ou de flotte. |
| 1688 | Intérêts courus sur emprunts | Régularisation de clôture. |

### 2.3 Classe 2 — Immobilisations

| Compte | Intitulé | Usage / seuil |
|---|---|---|
| 205 | Concessions, brevets, licences, logiciels | Licences **acquises** (ERP, logiciel de planification on-premise). Un abonnement **SaaS** n'est pas une immobilisation (charge). |
| 2154 | Matériel industriel — **matériel de nettoyage** | Autolaveuses, monobrosses, nettoyeurs haute pression, autolaveuses autoportées, robots. Approche par **composants** possible (batteries lithium). |
| 2181 | Installations générales, agencements | Aménagement des agences et dépôts. |
| 2182 | Matériel de transport | Véhicules **achetés** (les véhicules en LLD ne sont pas à l'actif). |
| 2183 | Matériel de bureau et informatique | PC des établissements, terminaux de pointage, smartphones des chefs d'équipe. |
| 2184 | Mobilier | |
| 238 | Avances et acomptes versés sur commandes d'immobilisations corporelles | **Pas en 4091** (piège, voir A15a). |
| 261 | Titres de participation | Chez la société tête : titres des filiales régionales. |
| 275 | Dépôts et cautionnements versés | Dépôts de garantie des baux d'agences, cautions. |
| 2805 / 28154 / 28182 / 28183 / 28184 | Amortissements | |
| 2961 | Dépréciation des titres de participation | Chez la mère, si une filiale perd durablement de la valeur. |

> 💡 **Réflexe senior :** le **seuil de 500 € HT** est une **tolérance fiscale** (matériels et outillages de faible valeur, mobilier de bureau) qui permet de passer en charge ; elle ne s'applique pas à un bien qui fait partie d'un ensemble (ex. 20 aspirateurs livrés pour équiper un nouveau marché : analysez l'ensemble). Dans un groupe, la **procédure d'immobilisation** fixe le seuil comptable : demandez-la.

### 2.4 Classe 3 — Stocks

| Compte | Intitulé | Usage |
|---|---|---|
| 3222 | Fournitures consommables | Produits d'entretien, papier, sacs, consommables détenus dans un **dépôt** (stock significatif et suivi). |
| 6032 | Variation des stocks des autres approvisionnements | Contrepartie de 3222 à l'inventaire. |

Une société de propreté n'a en général **pas** de stock de marchandises : les consommables livrés directement sur les sites sont souvent consommés immédiatement et passés en charge (voir A02/A03).

### 2.5 Classe 4 — Tiers (le cœur du poste)

**Fournisseurs**

| Compte | Intitulé | Usage |
|---|---|---|
| 401000 + aux. `Fxxxxx` | Fournisseurs (biens et services) | Produits d'entretien, sous-traitants, intérim, loueurs, énergie, télécoms. |
| 4011 | Fournisseurs groupe | Factures des sociétés du groupe (management fees, mise à disposition de personnel). À réconcilier chaque mois avec le 4112 de l'entité émettrice. |
| 4017 | Fournisseurs — retenues de garantie | Retenues sur sous-traitants de travaux (A25). |
| 403 | Fournisseurs — effets à payer | LCR fournisseurs acceptées. |
| 404000 | Fournisseurs d'immobilisations | Autolaveuses, véhicules achetés, informatique, logiciels. |
| 408 | Fournisseurs — factures non parvenues (FNP) | Clôtures mensuelles ; **doit être extourné** le mois suivant. |
| 4081 | Fournisseurs groupe — factures non parvenues | Pour les réconciliations intragroupe. |
| 4091 | Fournisseurs — avances et acomptes versés sur commandes | Acomptes sur **charges** (pas sur immobilisations → 238). |
| 4096 | Fournisseurs — créances pour emballages et matériel à rendre | Fûts, conteneurs, bonbonnes consignés. |
| 4098 | Rabais, remises, ristournes à obtenir et autres avoirs non encore reçus | Avoirs à recevoir, **RFA** de fin d'année. |

**Clients**

| Compte | Intitulé | Usage |
|---|---|---|
| 411000 + aux. `Cxxxxx` | Clients privés | Contrats de propreté, prestations ponctuelles. |
| 4111 | Clients publics | Hôpitaux, collectivités, aéroports : factures déposées sur **Chorus Pro**, délais de paiement réglementés (30 j, 60 j pour les établissements publics de santé). |
| 4112 | Clients groupe | Chez la mère : management fees, refacturations aux filiales. |
| 413 | Clients — effets à recevoir | LCR acceptées. |
| 416 | Clients douteux ou litigieux | Procédure collective, litige sérieux, retard anormal. |
| 418 | Clients — produits non encore facturés (FAE) | Prestations réalisées non facturées à la clôture. |
| 4191 | Clients — avances et acomptes reçus sur commandes | Acomptes de démarrage de contrat. |
| 4196 | Clients — dettes pour emballages et matériel consignés | Distributeurs (savon, essuie-mains) mis à disposition contre consigne. |
| 4198 | Rabais, remises, ristournes à accorder et autres avoirs à établir | Avoirs à établir (pénalités qualité notifiées, remises de fin d'année). |
| 491 | Dépréciations des comptes clients | Dotation **HT**. |

**Personnel, organismes sociaux**

| Compte | Intitulé | Usage |
|---|---|---|
| 421 | Personnel — rémunérations dues | Net à payer ; sous-compte `421800` notes de frais à rembourser. |
| 4246 | Participation — réserve spéciale | Participation obligatoire (≥ 50 salariés). |
| 425 | Personnel — avances et acomptes | Acomptes sur salaire, très fréquents avec des temps partiels. |
| 427 | Personnel — oppositions | Saisies sur salaire, pensions alimentaires (versées au créancier). |
| 4282 | Dettes provisionnées pour congés à payer | Provision CP (mensuelle dans un groupe). |
| 4286 | Personnel — autres charges à payer | Primes d'objectif, 13e mois proratisé. |
| 431 | Sécurité sociale (URSSAF) | Cotisations URSSAF, contribution formation et apprentissage collectées via la DSN. |
| 437 (4372 / 4373) | Autres organismes sociaux | 4372 mutuelle / prévoyance de branche ; 4373 retraite complémentaire (Agirc-Arrco). |
| 4382 | Charges sociales sur congés à payer | Pendant de 4282. |
| 4386 | Organismes sociaux — autres charges à payer | Charges sur primes provisionnées, forfait social sur participation. |
| 4387 | Organismes sociaux — produits à recevoir | **IJSS en subrogation** à recevoir de la CPAM. |

**État**

| Compte | Intitulé | Usage |
|---|---|---|
| 441 | État — subventions à recevoir | Subvention notifiée non encaissée. |
| 4421 | Prélèvement à la source (PAS) | Retenu sur les salaires, reversé via la DSN. |
| 444 | État — impôt sur les bénéfices | Acomptes d'IS et solde (hors intégration ; en intégration fiscale, la filiale règle la mère via 451). |
| 44551 | TVA à décaisser | Solde de la CA3. |
| 44562 | TVA déductible sur immobilisations | |
| 44566 | TVA déductible sur autres biens et services | |
| 445662 | TVA déductible — autoliquidation (sous-compte interne) | Contrepartie **symétrique** de 4452 (intracom, hors UE, sous-traitance BTP). |
| 445668 | TVA déductible en attente — prestations non payées (sous-compte interne) | TVA sur **services** achetés à un prestataire qui n'a **pas** opté pour les débits : déductible seulement au **paiement**. |
| 44567 | Crédit de TVA à reporter | |
| 44571 | TVA collectée | TVA **exigible** (encaissée, ou facturée si option débits / livraison de biens). |
| 44574 | TVA collectée sur encaissements à régulariser — « TVA en attente » (sous-compte interne) | TVA facturée sur prestations **non encore encaissées** : basculée en 44571 à l'encaissement. Son solde doit correspondre à la TVA incluse dans l'encours clients « prestations ». |
| 4452 (44521 / 44522 / 44523) | TVA due intracommunautaire et autres autoliquidations | 44521 acquisitions intracom de biens ; 44522 services UE / hors UE ; 44523 sous-traitance BTP. |
| 44583 | Remboursement de taxes sur le chiffre d'affaires demandé | Demande de remboursement de crédit de TVA. |
| 44584 | TVA récupérée d'avance | Cas particuliers (régularisations). |
| 44586 | Taxes sur le CA sur factures non parvenues | TVA des FNP et des avoirs à recevoir. |
| 44587 | Taxes sur le CA sur factures à établir | TVA des FAE et des avoirs à établir. |
| 447 | Autres impôts, taxes et versements assimilés | CFE, taxe sur les véhicules, à payer. |
| 4486 | État — charges à payer | CVAE (solde), taxes annuelles sur les véhicules à payer. |

**Groupe, associés, divers, régularisation**

| Compte | Intitulé | Usage |
|---|---|---|
| 451 (4511 / 4512 / 4518) | Groupe | 4511 compte courant de **cash pooling** ; 4512 compte courant d'**intégration fiscale** ; 4518 intérêts courus groupe. |
| 455 / 4551 | Associés — comptes courants (principal) | Comptes courants d'associés hors convention de trésorerie. |
| 457 | Associés — dividendes à payer | Après décision d'AG. |
| 462 | Créances sur cessions d'immobilisations | Prix de vente d'un véhicule cédé. |
| 4671 | Autres comptes débiteurs — factor (compte courant d'affacturage) | Créances cédées au factor. |
| 4672 | Autres comptes débiteurs — factor, retenue de garantie / fonds de garantie | |
| 4686 / 4687 | Divers — charges à payer / produits à recevoir | Ce qui n'a pas de compte de tiers plus précis. |
| 471 | Compte d'attente | **Doit être vide** à chaque clôture mensuelle. |
| 472 | Compte d'attente — opérations à classer (dépenses carte, écarts) | Idem. |
| 486 / 487 | Charges / produits constatés d'avance | Assurances, loyers d'avance / forfaits facturés d'avance. |

### 2.6 Classe 5 — Trésorerie

| Compte | Intitulé | Usage |
|---|---|---|
| 5113 | Effets à l'encaissement | LCR clients remises en banque. |
| 5121 / 5122 | Banque A / Banque B (un sous-compte par compte bancaire) | Rapprochement **par compte**. |
| 517 | Autres organismes financiers | Comptes de paiement, cartes carburant prépayées le cas échéant. |
| 58 | Virements internes | Transit entre deux banques : **solde nul** en fin de mois. |

### 2.7 Classe 6 — Charges

| Compte | Intitulé | Usage dans la propreté |
|---|---|---|
| 601 / 602 | Achats stockés — matières / autres approvisionnements | Rare en direct. |
| 6022 | Fournitures consommables — **produits d'entretien** | Détergents, désinfectants, microfibres, papier, sacs. |
| 6032 | Variation des stocks d'approvisionnements | |
| 6061 | Fournitures non stockables (eau, énergie) | Électricité des agences, **carburant** (sous-compte `606110`). |
| 6063 | Fournitures d'entretien et de petit équipement | **EPI**, petit matériel < 500 € HT, chariots. |
| 6064 | Fournitures administratives | |
| 6068 | Autres matières et fournitures | |
| 609 / 6092 | Rabais, remises, ristournes obtenus sur achats | RFA, remises hors facture. |
| 611 | Sous-traitance générale | **Sous-traitants de propreté**, nettoyage de fin de chantier. |
| 6122 | Redevances de crédit-bail mobilier | Matériel en crédit-bail. |
| 6132 | Locations immobilières | Loyers d'agences, dépôts. |
| 6135 | Locations mobilières | **LLD véhicules**, location de matériel, abonnements SaaS (selon plan groupe). |
| 614 | Charges locatives et de copropriété | |
| 6152 / 6155 | Entretien et réparations sur biens immobiliers / mobiliers | Réparation des autolaveuses, entretien de la flotte. |
| 6156 | Maintenance | Contrats de maintenance informatique. |
| 616 | Primes d'assurance | Flotte, RC exploitation, multirisque (exonérées de TVA). |
| 618 | Divers (documentation, colloques) | |
| 6211 | Personnel intérimaire | Remplacements, renforts saisonniers. |
| 6214 | Personnel détaché ou prêté à l'entreprise | Mise à disposition de personnel par une société du groupe. |
| 6225 | Rémunérations d'affacturage | Commission d'affacturage. |
| 6226 / 6227 / 6228 | Honoraires / frais d'actes et de contentieux / divers | CAC, avocats (prud'hommes), recouvrement. |
| 623 / 6234 | Publicité, relations publiques / cadeaux à la clientèle | |
| 6251 / 6256 / 6257 | Voyages et déplacements / missions / réceptions | Notes de frais des chefs d'établissement et inspecteurs. |
| 626 | Frais postaux et de télécommunications | Flotte mobile des chefs d'équipe. |
| 627 | Services bancaires et assimilés | Frais de tenue de compte, commissions. |
| 628 (`628800`) | Divers — **management fees / frais de siège** (sous-compte groupe) | Selon plan groupe (certains utilisent 6228 ou 611). |
| 631 (6312) | Impôts, taxes sur rémunérations (administration des impôts) — taxe d'apprentissage | Collectée via la DSN par l'URSSAF ; certains plans la classent en 633. |
| 633 (6333) | Impôts, taxes sur rémunérations (autres organismes) — participation des employeurs à la formation professionnelle continue | |
| 63511 | Contribution économique territoriale (**CFE, CVAE**) | CFE par établissement. |
| 63514 | Taxes sur les véhicules | Taxes annuelles sur les véhicules de tourisme utilisés à des fins économiques (CO2, polluants). |
| 6411 | Salaires, appointements | Base, **heures complémentaires** (temps partiels), préavis ; sous-compte `641190` **IJSS subrogées** (en diminution). |
| 6412 | Congés payés | CP pris, indemnité compensatrice, variation de la provision. |
| 6413 | Primes et gratifications | Prime de salissure, ancienneté, 13e mois, objectifs. |
| 6414 | Indemnités et avantages divers | Paniers, transport, indemnités de licenciement / rupture conventionnelle. |
| 6451 / 6452 / 6453 / 6458 | Cotisations URSSAF / mutuelles / retraite / autres organismes | Part patronale. |
| 647 (6478) | Autres charges sociales | Titres-restaurant (part patronale), médecine du travail (6475). |
| 648 | Autres charges de personnel | |
| 651 | Redevances pour concessions, brevets, licences, logiciels | Licences d'utilisation. |
| 654 | Pertes sur créances irrécouvrables | 6541 créances de l'exercice / 6544 créances des exercices antérieurs. |
| 656 | Pertes de change sur créances et dettes commerciales | Fournisseur en USD. |
| 658 | Charges diverses de gestion courante | **Pénalités contractuelles**, amendes, écarts de règlement débiteurs (*subdivision selon la nomenclature 2025 du PCG*). |
| 661 (6611 / 6615 / 6618) | Charges d'intérêts | Emprunts / comptes courants et cash pooling / autres (intérêts d'affacturage). |
| 665 | Escomptes accordés | |
| 666 | Pertes de change financières | Opérations financières en devises. |
| 671 | Charges exceptionnelles (*subdivisions selon la nomenclature 2025*) | Uniquement événement **majeur et inhabituel** (ex. sinistre majeur). |
| 675 | Valeurs comptables des éléments d'actif cédés | Cession / mise au rebut d'immobilisations. |
| 6811 (68111 / 68112) | Dotations aux amortissements incorporels / corporels | |
| 6815 | Dotations aux provisions d'exploitation | Prud'hommes, pénalités probables. |
| 6817 | Dotations aux dépréciations des actifs circulants | Clients douteux. |
| 691 | Participation des salariés aux résultats | |
| 695 | Impôts sur les bénéfices | IS et contribution sociale sur l'IS (sous-compte selon plan groupe). |
| 696 | Suppléments d'impôt sur les sociétés liés aux distributions | Rare. |
| 698 (6981 / 6989) | Intégration fiscale — charges / produits | Chez la tête de groupe : produits d'intégration reçus des filiales. |

### 2.8 Classe 7 — Produits

| Compte | Intitulé | Usage |
|---|---|---|
| 706100 | Prestations — **propreté forfait** (contrats mensuels) | Cœur du chiffre d'affaires. |
| 706200 | Prestations **ponctuelles** (vitrerie, remise en état, travaux exceptionnels) | |
| 706300 | Prestations **multiservices** (accueil, 3D, GDD, espaces verts) | |
| 706400 | **Refacturations** aux clients (consommables, frais) | |
| 706800 | Prestations intragroupe (management fees) | Chez la mère. |
| 7084 | Mise à disposition de personnel facturée | Chez la mère ou la filiale qui prête. |
| 7088 | Autres produits d'activités annexes | Locations de matériel, prestations diverses. |
| 7096 | RRR accordés sur prestations de services | **Attention :** 7091 vise les ventes de **produits finis** ; une société de services utilise **7096**. |
| 74 / 747 | Subventions d'exploitation / **quote-part des subventions d'investissement virée au résultat** | 747 depuis le PCG 2025 (ex-777). |
| 752 | Revenus des immeubles non affectés aux activités professionnelles | Rare. |
| 756 | Gains de change sur créances et dettes commerciales | |
| 758 | Produits divers de gestion courante | **Indemnité forfaitaire de 40 €**, écarts de règlement créditeurs (*subdivision selon la nomenclature 2025*). |
| 761 (7611) | Produits de participations — revenus des titres de participation | Dividendes des filiales (chez la mère). |
| 763 (7631) | Revenus des autres créances — créances commerciales | **Intérêts moratoires** facturés. |
| 764 | Revenus des valeurs mobilières de placement | |
| 765 | Escomptes obtenus | |
| 766 | Gains de change financiers | |
| 768 | Autres produits financiers | Intérêts facturés aux filiales sur la convention de trésorerie (certains plans : 763). |
| 775 | Produits des cessions d'éléments d'actif | |
| 7811 / 7815 / 7817 | Reprises sur amortissements / provisions d'exploitation / dépréciations des actifs circulants | |

---

## 3. Le recueil d'écritures types

Présentation de chaque écriture : **contexte** (une ligne), **pièce**, **tableau d'écriture** (équilibré), **piège / contrôle**. Les codes analytiques sont indiqués dans le libellé entre crochets. Taux de TVA : 20 % sauf mention contraire.

### 3.1 Cycle ventes / clients

#### V01 — Facture de forfait mensuel multi-sites (TVA sur les encaissements)
**Contexte :** contrat pluriannuel de propreté avec Résidences Horizon SA, trois immeubles de bureaux suivis par trois établissements, facturés sur une facture unique.
**Pièce :** facture électronique FV26-10-0458 du 31/10/2026, émise via la plateforme agréée, échéance 30 jours fin de mois. Site Nice 8 450,00 HT, site Cannes 5 230,00 HT, site Toulon 3 120,00 HT ; TVA 3 360,00 ; TTC 20 160,00. Pas de mention d'option pour les débits.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 411000 | Clients – Résidences Horizon (C00218) | FV26-10-0458 forfait oct. | 20 160,00 | |
| 31/10/2026 | VT | 706100 | Prestations propreté forfait | FV26-10-0458 [ETB061/PROP/CT-0418] | | 8 450,00 |
| 31/10/2026 | VT | 706100 | Prestations propreté forfait | FV26-10-0458 [ETB062/PROP/CT-0418] | | 5 230,00 |
| 31/10/2026 | VT | 706100 | Prestations propreté forfait | FV26-10-0458 [ETB083/PROP/CT-0418] | | 3 120,00 |
| 31/10/2026 | VT | 44574 | TVA collectée en attente (encaissements) | FV26-10-0458 | | 3 360,00 |
| | | | | **Total** | **20 160,00** | **20 160,00** |

> **Piège / contrôle :** une prestation de services est soumise à la TVA **à l'encaissement** : la TVA ne va **pas** en 44571 à la facturation. Ventilez le chiffre d'affaires **par établissement** (c'est la base du compte de résultat par centre de profit). Depuis le 01/09/2026, une grande entreprise émet ses factures sous forme électronique : vérifiez la présence du **SIREN du client**, de la **nature de l'opération** (« prestation de services ») et, le cas échéant, de la mention d'option pour les débits.

#### V02 — Encaissement de la facture V01 et bascule de la TVA
**Contexte :** Résidences Horizon règle la facture par virement.
**Pièce :** relevé bancaire Banque A du 30/11/2026, virement reçu 20 160,00 « REF FV26-10-0458 ».

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | BQ1 | 5121 | Banque A | Vir. Résidences Horizon FV26-10-0458 | 20 160,00 | |
| 30/11/2026 | BQ1 | 411000 | Clients – Résidences Horizon (C00218) | Vir. Résidences Horizon FV26-10-0458 | | 20 160,00 |
| 30/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | TVA exigible FV26-10-0458 | 3 360,00 | |
| 30/11/2026 | OD | 44571 | TVA collectée | TVA exigible FV26-10-0458 | | 3 360,00 |
| | | | | **Total** | **23 520,00** | **23 520,00** |

> **Piège / contrôle :** sans la deuxième écriture, la TVA n'est jamais déclarée (risque de rappel + intérêts de retard). La plupart des ERP génèrent la bascule automatiquement **au lettrage** : un encaissement **non lettré** = TVA non basculée. D'où le contrôle mensuel n° 6 (partie 5). En cas de paiement partiel, on ne bascule que la TVA **incluse dans le montant encaissé**.

#### V03 — Variante : société ayant opté pour le paiement de la TVA d'après les débits
**Contexte :** même type de facture, mais chez une société du groupe qui a opté pour les débits (option globale, mentionnée sur chaque facture).
**Pièce :** facture FV26-10-0512 du 31/10/2026 à Hypermarché Lumière SAS, forfait 9 600,00 HT, TVA 1 920,00, TTC 11 520,00, mention « Option pour le paiement de la taxe d'après les débits ».

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 411000 | Clients – Hypermarché Lumière (C00377) | FV26-10-0512 forfait oct. | 11 520,00 | |
| 31/10/2026 | VT | 706100 | Prestations propreté forfait | FV26-10-0512 [ETB083/PROP/CT-0533] | | 9 600,00 |
| 31/10/2026 | VT | 44571 | TVA collectée | FV26-10-0512 | | 1 920,00 |
| | | | | **Total** | **11 520,00** | **11 520,00** |

> **Piège / contrôle :** avec l'option, la TVA est exigible dès la facturation (44571) ; le client, lui, peut la déduire dès réception de la facture. Avantage commercial pour les clients, coût de trésorerie pour le prestataire. En entretien : savoir expliquer que le régime « encaissements » est le régime **de droit commun** des services.

#### V04 — Prestations ponctuelles (vitrerie, remise en état)
**Contexte :** vitrerie trimestrielle hors forfait et remise en état après un dégât des eaux, réalisées en octobre pour Résidences Horizon.
**Pièce :** facture FV26-10-0461 du 31/10/2026 : vitrerie 2 450,00 HT ; remise en état 3 800,00 HT ; TVA 1 250,00 ; TTC 7 500,00. Bons d'intervention signés par le client joints.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 411000 | Clients – Résidences Horizon (C00218) | FV26-10-0461 ponctuel oct. | 7 500,00 | |
| 31/10/2026 | VT | 706200 | Prestations ponctuelles | Vitrerie T4 [ETB061/VITR] | | 2 450,00 |
| 31/10/2026 | VT | 706200 | Prestations ponctuelles | Remise en état dégât des eaux [ETB061/REM] | | 3 800,00 |
| 31/10/2026 | VT | 44574 | TVA collectée en attente (encaissements) | FV26-10-0461 | | 1 250,00 |
| | | | | **Total** | **7 500,00** | **7 500,00** |

> **Piège / contrôle :** les prestations ponctuelles sont la principale source d'**oubli de facturation** : rapprochez chaque mois les **bons d'intervention** (outil de traçabilité client) et les factures émises ; ce qui est réalisé et non facturé à la clôture part en FAE (V13).

#### V05 — Facture de révision de prix rétroactive
**Contexte :** la clause de révision (indice de la branche propreté) donne +2,35 % à compter du 01/07/2026 ; l'indice n'a été publié qu'en octobre.
**Pièce :** facture FV26-10-0470 du 31/10/2026 : rappel de révision juillet à septembre : 16 800,00 × 3 mois × 2,35 % = 1 184,40 HT ; TVA 236,88 ; TTC 1 421,28.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 411000 | Clients – Résidences Horizon (C00218) | FV26-10-0470 révision prix 07-09 | 1 421,28 | |
| 31/10/2026 | VT | 706100 | Prestations propreté forfait | Révision +2,35 % 07-09/2026 [ETB061] | | 1 184,40 |
| 31/10/2026 | VT | 44574 | TVA collectée en attente (encaissements) | FV26-10-0470 | | 236,88 |
| | | | | **Total** | **1 421,28** | **1 421,28** |

> **Piège / contrôle :** même si la révision porte sur des mois passés, elle reste du **chiffre d'affaires d'exploitation** (pas de résultat exceptionnel). À la clôture annuelle, une révision **certaine** mais pas encore facturée donne lieu à une **FAE** (C04). Vérifiez que le forfait d'octobre a lui aussi été facturé au nouveau prix.

#### V06a — Avoir pour pénalité qualité analysée comme une réfaction de prix
**Contexte :** le contrôle qualité contradictoire du site de Cannes relève des prestations non réalisées ; le contrat prévoit une **réduction du prix** proportionnelle aux heures non effectuées.
**Pièce :** avoir AV26-10-0031 du 31/10/2026 sur la facture FV26-10-0458 : 640,00 HT ; TVA 128,00 ; TTC 768,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 7096 | RRR accordés sur prestations de services | AV26-10-0031 réfaction qualité [ETB062/PROP] | 640,00 | |
| 31/10/2026 | VT | 44574 | TVA collectée en attente (encaissements) | AV26-10-0031 | 128,00 | |
| 31/10/2026 | VT | 411000 | Clients – Résidences Horizon (C00218) | AV26-10-0031 | | 768,00 |
| | | | | **Total** | **768,00** | **768,00** |

> **Piège / contrôle :** la facture d'origine n'étant pas encaissée, on diminue la TVA **en attente** (44574), pas la TVA collectée. Une réfaction de prix **réduit la base de TVA** et exige un **avoir** (facture rectificative) faisant référence à la facture initiale.

#### V06b — Pénalité contractuelle forfaitaire (indemnité) retenue par le client
**Contexte :** autre client, marché avec pénalité forfaitaire de 500,00 par retard d'intervention, **sans lien avec le prix** de la prestation ; le client paie la facture TTC diminuée de la pénalité.
**Pièce :** courrier de notification de pénalité du 12/11/2026 + avis de paiement du client (facture 6 000,00 TTC, payé 5 500,00).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/11/2026 | BQ1 | 5121 | Banque A | Règlt Hypermarché Lumière net pénalité | 5 500,00 | |
| 15/11/2026 | BQ1 | 658 | Charges diverses de gestion courante – pénalités | Pénalité retard intervention [ETB083] | 500,00 | |
| 15/11/2026 | BQ1 | 411000 | Clients – Hypermarché Lumière (C00377) | Règlt FV26-10-0498 | | 6 000,00 |
| 15/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | TVA exigible FV26-10-0498 | 1 000,00 | |
| 15/11/2026 | OD | 44571 | TVA collectée | TVA exigible FV26-10-0498 | | 1 000,00 |
| | | | | **Total** | **7 000,00** | **7 000,00** |

> **Piège / contrôle :** une indemnité qui sanctionne un manquement, **sans réduire le prix**, n'est pas soumise à la TVA et ne diminue pas la base : la compensation vaut paiement, la TVA exigible est celle de **toute** la facture (1 000,00). Compte **658** (*subdivision selon la nomenclature 2025 du PCG*), en exploitation : **jamais en 67**. La qualification (réfaction de prix ou indemnité) dépend du **contrat** : faites-la valider par le contrôle de gestion ou le juridique.

#### V07 — Avoir commercial (geste commercial)
**Contexte :** geste commercial accordé par le chef d'établissement après une réclamation, sur une facture déjà réglée.
**Pièce :** avoir AV26-11-0004 du 05/11/2026 : 300,00 HT ; TVA 60,00 ; TTC 360,00 ; à imputer sur la prochaine facture.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/11/2026 | VT | 7096 | RRR accordés sur prestations de services | AV26-11-0004 geste commercial [ETB061] | 300,00 | |
| 05/11/2026 | VT | 44571 | TVA collectée | AV26-11-0004 (facture d'origine encaissée) | 60,00 | |
| 05/11/2026 | VT | 411000 | Clients – Résidences Horizon (C00218) | AV26-11-0004 | | 360,00 |
| | | | | **Total** | **360,00** | **360,00** |

> **Piège / contrôle :** la facture d'origine ayant été **encaissée**, sa TVA est déjà en 44571 : l'avoir la diminue en 44571. Si elle n'avait pas été encaissée, on passerait par 44574 (V06a). Et l'on n'utilise pas 7091 (produits finis) dans une société de services : **7096**. Vérifiez la **délégation de signature** du chef d'établissement (un avoir est une perte de marge).

#### V08a — Encaissement d'un acompte client au démarrage d'un contrat
**Contexte :** nouveau client exigeant un démarrage rapide ; acompte de 6 000,00 TTC demandé à la signature.
**Pièce :** facture d'acompte FA26-10-0007 du 02/10/2026 ; virement reçu le 06/10/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 06/10/2026 | BQ1 | 5121 | Banque A | Acompte FA26-10-0007 Clinique des Pins | 6 000,00 | |
| 06/10/2026 | BQ1 | 4191 | Clients – avances et acomptes reçus | Acompte HT FA26-10-0007 | | 5 000,00 |
| 06/10/2026 | BQ1 | 44571 | TVA collectée | TVA exigible sur acompte encaissé | | 1 000,00 |
| | | | | **Total** | **6 000,00** | **6 000,00** |

> **Piège / contrôle :** pour une **prestation de services**, l'encaissement d'un acompte rend la TVA **exigible immédiatement**. (Pour une livraison de biens, au contraire, l'acompte n'entraîne pas l'exigibilité.)

#### V08b — Facture finale avec imputation de l'acompte
**Contexte :** facturation du premier mois (forfait + mise en place) et imputation de l'acompte.
**Pièce :** facture FV26-10-0499 du 31/10/2026 : 15 000,00 HT ; TVA 3 000,00 ; TTC 18 000,00 ; acompte déduit 6 000,00 TTC ; net à payer 12 000,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 411000 | Clients – Clinique des Pins (C00402) | FV26-10-0499 net à payer | 12 000,00 | |
| 31/10/2026 | VT | 4191 | Clients – avances et acomptes reçus | Imputation acompte FA26-10-0007 | 5 000,00 | |
| 31/10/2026 | VT | 706100 | Prestations propreté forfait | FV26-10-0499 [ETB061/PROP/CT-0561] | | 15 000,00 |
| 31/10/2026 | VT | 44574 | TVA collectée en attente (encaissements) | TVA sur solde non encaissé (10 000,00 HT) | | 2 000,00 |
| | | | | **Total** | **17 000,00** | **17 000,00** |

> **Piège / contrôle :** ne collectez pas deux fois la TVA de l'acompte : seule la TVA du **solde** (2 000,00) est mise en attente. Le compte 4191 doit être soldé : un 4191 qui traîne = acompte non imputé (facture finale émise sans déduction, risque de double paiement par le client).

#### V09 — Marché public : facture déposée sur Chorus Pro, encaissement à 60 jours
**Contexte :** marché de bionettoyage du Centre hospitalier de Valmont (établissement public de santé : délai de paiement **60 jours**).
**Pièce :** facture FV26-08-0377 du 31/08/2026 déposée sur Chorus Pro (statut « mise à disposition » puis « mise en paiement ») : 24 500,00 HT ; TVA 4 900,00 ; TTC 29 400,00. Encaissement le 15/11/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/08/2026 | VT | 4111 | Clients publics – CH Valmont (C00091) | FV26-08-0377 bionettoyage août | 29 400,00 | |
| 31/08/2026 | VT | 706100 | Prestations propreté forfait | FV26-08-0377 [ETB061/PROP/CT-0099] | | 24 500,00 |
| 31/08/2026 | VT | 44574 | TVA collectée en attente (encaissements) | FV26-08-0377 | | 4 900,00 |
| 15/11/2026 | BQ1 | 5121 | Banque A | Vir. DGFiP/comptable public FV26-08-0377 | 29 400,00 | |
| 15/11/2026 | BQ1 | 4111 | Clients publics – CH Valmont (C00091) | Règlt FV26-08-0377 | | 29 400,00 |
| 15/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | TVA exigible FV26-08-0377 | 4 900,00 | |
| 15/11/2026 | OD | 44571 | TVA collectée | TVA exigible FV26-08-0377 | | 4 900,00 |
| | | | | **Total** | **63 700,00** | **63 700,00** |

> **Piège / contrôle :** une facture publique non déposée sur Chorus Pro (ou rejetée pour un **numéro d'engagement juridique** / **code service** absent) **ne court pas** : le délai de paiement ne démarre qu'à la réception conforme. Suivez les statuts Chorus Pro chaque semaine. Le paiement est ici arrivé avec **16 jours de retard** (échéance au 30/10/2026) → V10.

#### V10 — Intérêts moratoires et indemnité forfaitaire de 40 €
**Contexte :** le retard de paiement du CH Valmont fait courir de plein droit des intérêts moratoires et l'indemnité forfaitaire pour frais de recouvrement.
**Pièce :** note de calcul et demande de paiement du 16/11/2026. On retient un taux d'intérêts moratoires de 10,15 % (taux BCE + 8 points — *valeur à vérifier chaque semestre*) : 29 400,00 × 10,15 % × 16 / 365 = **130,81** ; indemnité forfaitaire **40,00**. Non soumis à la TVA.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 16/11/2026 | VT | 4111 | Clients publics – CH Valmont (C00091) | Intérêts moratoires + indemnité FV26-08-0377 | 170,81 | |
| 16/11/2026 | VT | 7631 | Revenus des créances commerciales | Intérêts moratoires 16 j | | 130,81 |
| 16/11/2026 | VT | 758 | Produits divers de gestion courante | Indemnité forfaitaire recouvrement | | 40,00 |
| | | | | **Total** | **170,81** | **170,81** |

> **Piège / contrôle :** pas de TVA sur les intérêts moratoires ni sur l'indemnité (ce sont des sommes réparant un préjudice, pas la contrepartie d'un service). Dans la commande publique, ils sont **dus de plein droit** ; dans un groupe, la politique de réclamation (systématique ou non, selon la relation client) est fixée par la direction : ne facturez pas sans validation. Comptes : *subdivisions selon la nomenclature 2025 du PCG*.

#### V11 — Client douteux : transfert en 416 et dépréciation
**Contexte :** Hypermarché Lumière (V03, option débits) est placé en redressement judiciaire ; la facture de 11 520,00 TTC est impayée. Estimation du risque de perte : 60 %.
**Pièce :** annonce BODACC du 20/11/2026 ; déclaration de créance envoyée au mandataire judiciaire.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | OD | 416 | Clients douteux ou litigieux | Transfert Hypermarché Lumière RJ | 11 520,00 | |
| 30/11/2026 | OD | 411000 | Clients – Hypermarché Lumière (C00377) | Transfert en 416 | | 11 520,00 |
| 30/11/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation 60 % × 9 600,00 HT | 5 760,00 | |
| 30/11/2026 | OD | 491 | Dépréciations des comptes clients | Dépréciation Hypermarché Lumière | | 5 760,00 |
| | | | | **Total** | **17 280,00** | **17 280,00** |

> **Piège / contrôle :** la dépréciation se calcule sur le **HT** (la TVA sera récupérée en cas de perte définitive). **Déclarez la créance** au mandataire dans le délai légal (deux mois à compter de la publication au BODACC) : sans déclaration, la créance est inopposable. Ne facturez plus de nouvelles prestations sur ce compte sans garantie : les prestations postérieures au jugement suivent un autre régime (créances « postérieures » payables à l'échéance).

#### V12 — Créance irrécouvrable avec récupération de la TVA
**Contexte :** clôture de la liquidation pour insuffisance d'actif ; la créance de V11 est définitivement perdue.
**Pièce :** certificat d'irrecouvrabilité du mandataire du 10/12/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 10/12/2026 | OD | 6541 | Pertes sur créances irrécouvrables de l'exercice | Hypermarché Lumière – perte définitive | 9 600,00 | |
| 10/12/2026 | OD | 44571 | TVA collectée | Récupération TVA FV26-10-0512 | 1 920,00 | |
| 10/12/2026 | OD | 416 | Clients douteux ou litigieux | Solde Hypermarché Lumière | | 11 520,00 |
| 10/12/2026 | OD | 491 | Dépréciations des comptes clients | Reprise dépréciation | 5 760,00 | |
| 10/12/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise dépréciation | | 5 760,00 |
| | | | | **Total** | **17 280,00** | **17 280,00** |

> **Piège / contrôle :** on récupère la TVA **en 44571** ici parce que la société avait opté pour les **débits** (la TVA avait été reversée à la facturation). **Sous le régime des encaissements, il n'y a rien à « récupérer » : on annule simplement la TVA en attente (débit 44574)** — erreur fréquente qui fait déduire une TVA jamais payée. La récupération suppose l'émission d'une facture rectificative (avoir) et le certificat d'irrecouvrabilité. 6541 si la créance est née dans l'exercice, 6544 sinon.

#### V13 — Facture à établir en fin de mois (prestations réalisées non facturées)
**Contexte :** remise en état exceptionnelle réalisée du 26 au 30/10 sur un site de Toulon ; le bon d'intervention signé arrive après la clôture de facturation.
**Pièce :** bon d'intervention BI-083-2026-1188 ; devis accepté 4 200,00 HT.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 418 | Clients – produits non encore facturés | FAE remise en état BI-1188 | 5 040,00 | |
| 31/10/2026 | OD | 706200 | Prestations ponctuelles | FAE BI-1188 [ETB083/REM] | | 4 200,00 |
| 31/10/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | FAE BI-1188 | | 840,00 |
| | | | | **Total** | **5 040,00** | **5 040,00** |

> **Piège / contrôle :** **extourne au 01/11/2026** (journal EXT), puis vraie facture en novembre. La TVA de la FAE ne figure pas sur la CA3 : elle n'est ni exigible (pas facturée, pas encaissée). Contrôle : le 418 d'un mois doit être soldé le mois suivant.

#### V14 — Produit constaté d'avance (forfait facturé à terme à échoir)
**Contexte :** certains contrats sont facturés **d'avance** : le forfait de novembre a été facturé le 25/10/2026.
**Pièce :** facture FV26-10-0440 du 25/10/2026 : forfait novembre 7 000,00 HT.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 706100 | Prestations propreté forfait | PCA forfait nov. FV26-10-0440 [ETB062] | 7 000,00 | |
| 31/10/2026 | OD | 487 | Produits constatés d'avance | PCA forfait nov. FV26-10-0440 | | 7 000,00 |
| | | | | **Total** | **7 000,00** | **7 000,00** |

> **Piège / contrôle :** le PCA se calcule **HT** (la TVA suit sa propre règle d'exigibilité). Extourne au 01/11. Une clôture mensuelle sans PCA sur les contrats « à échoir » gonfle le chiffre d'affaires d'un mois et creuse le suivant : le contrôle de gestion le verra immédiatement.

#### V15 — Refacturation de consommables au client
**Contexte :** le contrat prévoit que les consommables sanitaires (papier, savon) sont refacturés au coût majoré de 10 %.
**Pièce :** facture FV26-10-0476 du 31/10/2026 : consommables octobre 1 380,00 HT ; TVA 276,00 ; TTC 1 656,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 411000 | Clients – Résidences Horizon (C00218) | FV26-10-0476 consommables oct. | 1 656,00 | |
| 31/10/2026 | VT | 706400 | Refacturations aux clients | Consommables sanitaires [ETB061/PROP] | | 1 380,00 |
| 31/10/2026 | VT | 44574 | TVA collectée en attente (encaissements) | FV26-10-0476 | | 276,00 |
| | | | | **Total** | **1 656,00** | **1 656,00** |

> **Piège / contrôle :** une refacturation est un **produit**, jamais une diminution de 6022 (on compenserait charges et produits et la marge analytique serait faussée). Si les consommables sont fournis comme accessoire de la prestation, ils suivent le régime TVA de la prestation (encaissements) ; s'il s'agit d'une vente distincte de biens, l'exigibilité est la livraison → 44571 : analysez le contrat.

#### V16 — Affacturage : cession de créances au factor
**Contexte :** pour financer le BFR, la filiale cède au factor un bordereau de factures clients.
**Pièce :** bordereau de cession n° 2026-44 du 05/11/2026 : 120 000,00 TTC.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/11/2026 | OD | 4671 | Factor – compte courant d'affacturage | Bordereau 2026-44 | 120 000,00 | |
| 05/11/2026 | OD | 411000 | Clients (détail par auxiliaire) | Cession bordereau 2026-44 | | 120 000,00 |
| | | | | **Total** | **120 000,00** | **120 000,00** |

#### V17 — Affacturage : financement, commissions et retenue de garantie
**Contexte :** le factor met les fonds à disposition sous déduction de ses commissions et d'un fonds de garantie de 10 %.
**Pièce :** relevé du factor du 06/11/2026 : commission d'affacturage 0,30 % = 360,00 HT + TVA 72,00 ; commission de financement (intérêts) 450,00 ; fonds de garantie 12 000,00 ; net versé 107 118,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 06/11/2026 | BQ1 | 5121 | Banque A | Financement factor bordereau 2026-44 | 107 118,00 | |
| 06/11/2026 | BQ1 | 6225 | Rémunérations d'affacturage | Commission 0,30 % | 360,00 | |
| 06/11/2026 | BQ1 | 44566 | TVA déductible sur ABS | TVA commission factor | 72,00 | |
| 06/11/2026 | BQ1 | 6618 | Intérêts des autres dettes | Commission de financement | 450,00 | |
| 06/11/2026 | BQ1 | 4672 | Factor – fonds de garantie | Retenue 10 % bordereau 2026-44 | 12 000,00 | |
| 06/11/2026 | BQ1 | 4671 | Factor – compte courant d'affacturage | Bordereau 2026-44 | | 120 000,00 |
| | | | | **Total** | **120 000,00** | **120 000,00** |

> **Piège / contrôle (V16-V17) :** la commission d'affacturage (service, TVA) se distingue de la commission de financement (intérêts, charge financière, pas de TVA). Le **4672** est une créance à suivre et à récupérer quand les clients ont payé le factor. Côté TVA sur encaissements, la **date d'exigibilité** de la TVA des créances cédées (paiement par le factor ou par le client final) doit être tranchée avec le responsable fiscal et appliquée de manière constante ; ne laissez pas dormir la TVA en 44574 sur des créances sorties du 411. Information en annexe sur les créances cédées non échues selon le type de contrat.

#### V18 — Encaissement par LCR (acceptation, remise, encaissement)
**Contexte :** un client industriel règle par lettre de change-relevé (LCR) à 45 jours.
**Pièce :** facture 8 400,00 TTC (7 000,00 HT ; TVA 1 400,00) ; LCR acceptée le 10/10 ; remise à l'encaissement le 20/11 ; relevé du 25/11 : crédit 8 395,68 (frais 3,60 HT + TVA 0,72).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 10/10/2026 | OD | 413 | Clients – effets à recevoir | LCR acceptée Agroalim Sud | 8 400,00 | |
| 10/10/2026 | OD | 411000 | Clients – Agroalim Sud (C00512) | LCR acceptée | | 8 400,00 |
| 20/11/2026 | BQ1 | 5113 | Effets à l'encaissement | Remise LCR n° 4471 | 8 400,00 | |
| 20/11/2026 | BQ1 | 413 | Clients – effets à recevoir | Remise LCR n° 4471 | | 8 400,00 |
| 25/11/2026 | BQ1 | 5121 | Banque A | Encaissement LCR n° 4471 | 8 395,68 | |
| 25/11/2026 | BQ1 | 627 | Services bancaires | Frais remise LCR | 3,60 | |
| 25/11/2026 | BQ1 | 44566 | TVA déductible sur ABS | TVA frais bancaires | 0,72 | |
| 25/11/2026 | BQ1 | 5113 | Effets à l'encaissement | Encaissement LCR n° 4471 | | 8 400,00 |
| 25/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | TVA exigible LCR n° 4471 | 1 400,00 | |
| 25/11/2026 | OD | 44571 | TVA collectée | TVA exigible LCR n° 4471 | | 1 400,00 |
| | | | | **Total** | **26 600,00** | **26 600,00** |

> **Piège / contrôle :** l'acceptation d'une LCR **n'est pas** un encaissement : la TVA ne devient exigible qu'à l'**échéance** (encaissement effectif), pas au passage en 413. En cas d'impayé, on contre-passe (voir T07).

#### V19 — Escompte pour paiement anticipé accordé au client
**Contexte :** le client paie à 10 jours et applique l'escompte de 1 % prévu aux conditions générales.
**Pièce :** facture 12 000,00 TTC (10 000,00 HT ; TVA 2 000,00) ; escompte 1 % du HT = 100,00 HT + TVA 20,00 ; virement reçu 11 880,00 ; avoir d'escompte AV26-11-0011 émis.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 18/11/2026 | BQ1 | 5121 | Banque A | Vir. Logistique Var FV26-11-0102 | 11 880,00 | |
| 18/11/2026 | BQ1 | 665 | Escomptes accordés | Escompte 1 % AV26-11-0011 | 100,00 | |
| 18/11/2026 | BQ1 | 44574 | TVA collectée en attente (encaissements) | TVA sur escompte | 20,00 | |
| 18/11/2026 | BQ1 | 411000 | Clients – Logistique Var (C00588) | Règlt FV26-11-0102 | | 12 000,00 |
| 18/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | TVA exigible nette d'escompte | 1 980,00 | |
| 18/11/2026 | OD | 44571 | TVA collectée | TVA exigible nette d'escompte | | 1 980,00 |
| | | | | **Total** | **13 980,00** | **13 980,00** |

> **Piège / contrôle :** l'escompte est une charge **financière** (665), pas un RRR (709). Il réduit la base de TVA à condition d'émettre un **avoir** (ou que la facture d'origine mentionne la TVA nette d'escompte).

#### V20 — Écart de règlement minime
**Contexte :** un client règle 4 799,85 pour une facture de 4 800,00 TTC (frais bancaires du client) ; la politique groupe autorise le passage en charge des écarts inférieurs à 5,00.
**Pièce :** relevé Banque A du 20/11/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 20/11/2026 | BQ1 | 5121 | Banque A | Vir. Pharma Côte FV26-10-0455 | 4 799,85 | |
| 20/11/2026 | BQ1 | 658 | Charges diverses de gestion courante – écarts de règlement | Écart de règlement < 5 € | 0,15 | |
| 20/11/2026 | BQ1 | 411000 | Clients – Pharma Côte (C00611) | Règlt FV26-10-0455 | | 4 800,00 |
| 20/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | TVA exigible FV26-10-0455 | 800,00 | |
| 20/11/2026 | OD | 44571 | TVA collectée | TVA exigible FV26-10-0455 | | 800,00 |
| | | | | **Total** | **5 600,00** | **5 600,00** |

> **Piège / contrôle :** l'écart de règlement n'est pas une remise : il ne réduit pas la TVA (on bascule toute la TVA de la facture). Écarts créditeurs en **758**. Au-delà du seuil fixé par la procédure, on relance le client au lieu de passer en charge.

### 3.2 Cycle achats / fournisseurs

> 💡 **Réflexe senior (avant toute saisie d'une facture fournisseur) :** 1) la facture est-elle bien **adressée à la bonne société du groupe** (SIREN, adresse de facturation) ? 2) existe-t-il une **commande** et une **réception** (rapprochement à trois voies) ? 3) les **mentions obligatoires** sont-elles présentes (sinon TVA non déductible) ? 4) **doublon** (même fournisseur, même numéro, même montant) ? 5) **nature** (charge, immobilisation, stock) et **TVA** (taux, exigibilité, autoliquidation, exclusion) ? 6) **imputation analytique** (établissement, contrat) ?

#### A01 — Produits d'entretien avec remise sur facture
**Contexte :** commande mensuelle de détergents et désinfectants pour l'établissement de Nice.
**Pièce :** facture Hygiène Pro Distribution n° HP-88412 du 08/10/2026 : brut 3 250,00 HT ; remise 8 % 260,00 ; net 2 990,00 HT ; TVA 598,00 ; TTC 3 588,00 ; paiement 45 jours fin de mois, escompte 1 % pour paiement à 10 jours.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 08/10/2026 | AC | 6022 | Fournitures consommables – produits d'entretien | HP-88412 détergents [ETB061/PROP] | 2 990,00 | |
| 08/10/2026 | AC | 44566 | TVA déductible sur ABS | HP-88412 | 598,00 | |
| 08/10/2026 | AC | 401000 | Fournisseurs – Hygiène Pro Distribution (F00412) | HP-88412 | | 3 588,00 |
| | | | | **Total** | **3 588,00** | **3 588,00** |

> **Piège / contrôle :** une remise **sur facture** se comptabilise **nette** (on ne passe pas 609). Comparez les prix unitaires avec le **contrat cadre** des Achats : un écart de prix est un motif de litige (blocage) avant comptabilisation, pas après. La TVA sur **livraison de biens** est déductible dès la facture (pas d'attente du paiement).

#### A02 — Consommables stockés : variation de stock du dépôt
**Contexte :** l'établissement de Nice gère un dépôt central de consommables (stock significatif, inventorié chaque fin de mois).
**Pièce :** état d'inventaire au 31/10/2026 : 21 150,00 ; stock comptabilisé au 30/09/2026 : 18 400,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6032 | Variation des stocks d'approvisionnements | Annulation stock initial dépôt Nice | 18 400,00 | |
| 31/10/2026 | OD | 3222 | Fournitures consommables | Annulation stock initial dépôt Nice | | 18 400,00 |
| 31/10/2026 | OD | 3222 | Fournitures consommables | Stock final 31/10 dépôt Nice | 21 150,00 | |
| 31/10/2026 | OD | 6032 | Variation des stocks d'approvisionnements | Stock final 31/10 dépôt Nice [ETB061] | | 21 150,00 |
| | | | | **Total** | **39 550,00** | **39 550,00** |

> **Piège / contrôle :** les achats restent en 6022 ; c'est la **variation** (6032, ici créditrice de 2 750,00) qui corrige la consommation. Contrôlez la valorisation (coût d'achat, pas prix de revente) et les articles périmés ou obsolètes (dépréciation 3922 si nécessaire).

#### A03 — Fournitures non stockées (EPI, fournitures de bureau, divers)
**Contexte :** achats livrés directement sur les sites et consommés immédiatement.
**Pièce :** facture Équip'Pro n° EP-20931 du 12/10/2026 : EPI (gants, chaussures de sécurité) 640,00 ; fournitures de bureau 180,00 ; divers 95,00 ; HT 915,00 ; TVA 183,00 ; TTC 1 098,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 12/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | EP-20931 EPI [ETB062] | 640,00 | |
| 12/10/2026 | AC | 6064 | Fournitures administratives | EP-20931 bureau [ETB062] | 180,00 | |
| 12/10/2026 | AC | 6068 | Autres matières et fournitures | EP-20931 divers [ETB062] | 95,00 | |
| 12/10/2026 | AC | 44566 | TVA déductible sur ABS | EP-20931 | 183,00 | |
| 12/10/2026 | AC | 401000 | Fournisseurs – Équip'Pro (F00519) | EP-20931 | | 1 098,00 |
| | | | | **Total** | **1 098,00** | **1 098,00** |

> **Piège / contrôle :** les EPI sont une obligation de l'employeur : ne les refacturez jamais aux salariés. Une facture « multi-natures » se ventile ligne par ligne, y compris en analytique.

#### A04 — Matériel de faible valeur (< 500 € HT) passé en charge
**Contexte :** remplacement d'un aspirateur dorsal sur un site.
**Pièce :** facture Matériel Nettoyage Sud n° MNS-7710 du 14/10/2026 : 389,00 HT ; TVA 77,80 ; TTC 466,80.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 14/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | MNS-7710 aspirateur dorsal [ETB061] | 389,00 | |
| 14/10/2026 | AC | 44566 | TVA déductible sur ABS | MNS-7710 | 77,80 | |
| 14/10/2026 | AC | 401000 | Fournisseurs – Matériel Nettoyage Sud (F00233) | MNS-7710 | | 466,80 |
| | | | | **Total** | **466,80** | **466,80** |

#### A05 — Autolaveuse immobilisée (approche par composants)
**Contexte :** achat d'une autolaveuse autoportée pour un nouveau marché de centre commercial ; les batteries lithium seront remplacées au bout de 3 ans.
**Pièce :** facture Matériel Nettoyage Sud n° MNS-7745 du 20/10/2026 : machine 7 500,00 HT ; pack batteries 1 400,00 HT ; TVA 1 780,00 ; TTC 10 680,00 ; procès-verbal de mise en service du 21/10/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 21/10/2026 | ACI | 2154 | Matériel de nettoyage – structure | MNS-7745 autolaveuse (5 ans) [ETB062] | 7 500,00 | |
| 21/10/2026 | ACI | 2154 | Matériel de nettoyage – composant batteries | MNS-7745 batteries (3 ans) [ETB062] | 1 400,00 | |
| 21/10/2026 | ACI | 44562 | TVA déductible sur immobilisations | MNS-7745 | 1 780,00 | |
| 21/10/2026 | ACI | 404000 | Fournisseurs d'immobilisations – Matériel Nettoyage Sud | MNS-7745 | | 10 680,00 |
| | | | | **Total** | **10 680,00** | **10 680,00** |

> **Piège / contrôle (A04-A05) :** 404 et 44562 pour une immobilisation (la CA3 distingue la TVA sur immobilisations). Date de début d'amortissement = **mise en service** (21/10), pas date de facture. Créez la fiche dans le **fichier des immobilisations** avec le numéro de série : c'est lui qui permettra la sortie propre en cas de rebut (I04).

#### A06 — Sous-traitant de propreté (TVA de droit commun, déductible au paiement)
**Contexte :** un sous-traitant assure le nettoyage d'un site éloigné ; il n'a pas opté pour les débits.
**Pièce :** facture Net'Sous-Traitance n° NST-2026-301 du 31/10/2026 : 5 600,00 HT ; TVA 1 120,00 ; TTC 6 720,00 ; payée le 30/11/2026. Attestation de vigilance URSSAF de moins de 6 mois au dossier.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | AC | 611 | Sous-traitance générale | NST-2026-301 site Antibes [ETB061/PROP/CT-0472] | 5 600,00 | |
| 31/10/2026 | AC | 445668 | TVA déductible en attente (services non payés) | NST-2026-301 | 1 120,00 | |
| 31/10/2026 | AC | 401000 | Fournisseurs – Net'Sous-Traitance (F00688) | NST-2026-301 | | 6 720,00 |
| 30/11/2026 | BQ1 | 401000 | Fournisseurs – Net'Sous-Traitance (F00688) | Règlt NST-2026-301 | 6 720,00 | |
| 30/11/2026 | BQ1 | 5121 | Banque A | Règlt NST-2026-301 | | 6 720,00 |
| 30/11/2026 | OD | 44566 | TVA déductible sur ABS | TVA déductible au paiement NST-2026-301 | 1 120,00 | |
| 30/11/2026 | OD | 445668 | TVA déductible en attente (services non payés) | TVA déductible au paiement NST-2026-301 | | 1 120,00 |
| | | | | **Total** | **14 560,00** | **14 560,00** |

> **Piège / contrôle :** symétrie avec V01 : quand le prestataire est « aux encaissements », **le client ne déduit la TVA qu'au paiement**. Déduire la TVA d'un sous-traitant dès la facture = déduction anticipée (rappel en cas de contrôle). **Obligation de vigilance** : pour tout contrat ≥ 5 000 € HT, l'attestation URSSAF doit être obtenue à la conclusion puis **tous les 6 mois** ; à défaut, solidarité financière du donneur d'ordre. Le nettoyage courant de locaux reste en TVA de droit commun (pas d'autoliquidation BTP).

#### A07 — Sous-traitant de nettoyage de fin de chantier (autoliquidation BTP)
**Contexte :** la filiale, elle-même sous-traitante d'une entreprise de construction pour le nettoyage de fin de chantier d'un immeuble neuf, fait appel à un sous-traitant de second rang.
**Pièce :** facture Fin de Chantier Express n° FCE-118 du 31/10/2026 : 3 400,00 HT, mention « Autoliquidation » (pas de TVA facturée) ; payée le 30/11/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | AC | 611 | Sous-traitance générale | FCE-118 fin de chantier [ETB083/REM/CT-0590] | 3 400,00 | |
| 31/10/2026 | AC | 401000 | Fournisseurs – Fin de Chantier Express (F00702) | FCE-118 | | 3 400,00 |
| 30/11/2026 | BQ1 | 401000 | Fournisseurs – Fin de Chantier Express (F00702) | Règlt FCE-118 | 3 400,00 | |
| 30/11/2026 | BQ1 | 5121 | Banque A | Règlt FCE-118 | | 3 400,00 |
| 30/11/2026 | OD | 445662 | TVA déductible – autoliquidation | TVA autoliquidée BTP FCE-118 | 680,00 | |
| 30/11/2026 | OD | 44523 | TVA due – autoliquidation sous-traitance BTP | TVA autoliquidée BTP FCE-118 | | 680,00 |
| | | | | **Total** | **7 480,00** | **7 480,00** |

> **Piège / contrôle :** l'autoliquidation BTP ne s'applique qu'au nettoyage **lié à des travaux immobiliers** réalisé en **sous-traitance** d'un preneur assujetti ; le nettoyage de locaux en exploitation reste en droit commun. La TVA autoliquidée sur des travaux est exigible **au paiement** (sauf option du sous-traitant pour les débits). Côté ventes, la facture de la filiale à l'entreprise de construction est elle aussi émise **HT** avec la mention « Autoliquidation ». Contrôle : 44523 = 445662 (sous-compte BTP).

#### A08 — Facture d'intérim
**Contexte :** renforts pendant les congés d'automne sur l'établissement de Cannes.
**Pièce :** facture Intérim Côte n° IC-55120 du 31/10/2026 (relevés d'heures signés joints) : 6 850,00 HT ; TVA 1 370,00 ; TTC 8 220,00 ; mention « Option pour le paiement de la taxe d'après les débits ».

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | AC | 6211 | Personnel intérimaire | IC-55120 renforts oct. [ETB062/PROP] | 6 850,00 | |
| 31/10/2026 | AC | 44566 | TVA déductible sur ABS | IC-55120 (option débits) | 1 370,00 | |
| 31/10/2026 | AC | 401000 | Fournisseurs – Intérim Côte (F00145) | IC-55120 | | 8 220,00 |
| | | | | **Total** | **8 220,00** | **8 220,00** |

> **Piège / contrôle :** c'est **la mention d'option pour les débits** sur la facture qui permet la déduction immédiate (comparez avec A06). Rapprochez les heures facturées avec les **relevés d'heures validés** par le chef d'équipe : l'intérim est un poste de litige fréquent (heures majorées, coefficient).

#### A09 — Location longue durée (LLD) de véhicules : VU et VP
**Contexte :** facture mensuelle du loueur pour 3 véhicules utilitaires d'équipes (VU) et 1 véhicule de tourisme du chef d'établissement (VP).
**Pièce :** facture Flotte Leasing n° FL-10-26-8841 du 01/11/2026 : VU loyer 3 × 390,00 = 1 170,00 + entretien 3 × 45,00 = 135,00 ; VP loyer 520,00 + entretien 60,00 ; HT 1 885,00 ; TVA 377,00 ; TTC 2 262,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/11/2026 | AC | 6135 | Locations mobilières – LLD véhicules | FL-8841 loyers VU [ETB061] | 1 170,00 | |
| 01/11/2026 | AC | 6135 | Locations mobilières – LLD véhicules | FL-8841 loyer VP TTC (TVA non récupérable) [ETB061] | 624,00 | |
| 01/11/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | FL-8841 entretien VU [ETB061] | 135,00 | |
| 01/11/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | FL-8841 entretien VP TTC [ETB061] | 72,00 | |
| 01/11/2026 | AC | 44566 | TVA déductible sur ABS | FL-8841 TVA VU uniquement | 261,00 | |
| 01/11/2026 | AC | 401000 | Fournisseurs – Flotte Leasing (F00301) | FL-8841 | | 2 262,00 |
| | | | | **Total** | **2 262,00** | **2 262,00** |

> **Piège / contrôle :** la TVA sur la location **et l'entretien** d'un **véhicule de tourisme** est exclue du droit à déduction (elle s'ajoute à la charge) ; elle est déductible pour un véhicule **utilitaire** (vérifiez la carte grise : genre « CTTE », « VP »…). Pour le VP, une fraction du loyer peut être **non déductible fiscalement** (plafond d'amortissement du bailleur selon le taux de CO2) et le véhicule entre dans les **taxes annuelles sur les véhicules** (C13). La LLD n'est pas inscrite à l'actif en comptes sociaux : engagement à mentionner en annexe.

#### A10 — Carte carburant
**Contexte :** relevé mensuel de cartes carburant (VU au gazole, VP à l'essence).
**Pièce :** relevé CarbuCard n° CC-2610-004 du 31/10/2026 : gazole VU 1 240,00 HT + TVA 248,00 ; essence VP 180,00 HT + TVA 36,00 ; TTC 1 704,00. On retient la règle de déductibilité : 100 % pour les VU, **80 %** pour les VP (gazole et essence) — *à vérifier*.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | AC | 6061 | Fournitures non stockables – carburants | CC-2610-004 gazole VU [ETB061] | 1 240,00 | |
| 31/10/2026 | AC | 6061 | Fournitures non stockables – carburants | CC-2610-004 essence VP + 20 % TVA non récup. [ETB061] | 187,20 | |
| 31/10/2026 | AC | 44566 | TVA déductible sur ABS | CC-2610-004 (248,00 + 80 % × 36,00) | 276,80 | |
| 31/10/2026 | AC | 401000 | Fournisseurs – CarbuCard (F00410) | CC-2610-004 | | 1 704,00 |
| | | | | **Total** | **1 704,00** | **1 704,00** |

> **Piège / contrôle :** analysez le relevé **par carte / immatriculation** : une carte affectée à un VP utilisée pour un VU (ou l'inverse) fausse la TVA. Contrôlez les anomalies (plein le week-end, volumes supérieurs au réservoir) : c'est un vrai sujet de contrôle interne dans un groupe à grande flotte.

#### A11 — Service acheté à un prestataire de l'Union européenne (autoliquidation)
**Contexte :** réparation d'un robot de nettoyage par son fabricant allemand.
**Pièce :** facture Reinigung Technik GmbH n° RT-2026-0918 du 22/10/2026 : 1 850,00 € HT, n° TVA DE et FR mentionnés, « Reverse charge – art. 196 directive 2006/112/CE ».

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 22/10/2026 | AC | 6155 | Entretien et réparations sur biens mobiliers | RT-0918 réparation robot [ETB061] | 1 850,00 | |
| 22/10/2026 | AC | 401000 | Fournisseurs – Reinigung Technik GmbH (F00811) | RT-0918 | | 1 850,00 |
| 22/10/2026 | AC | 445662 | TVA déductible – autoliquidation | TVA autoliquidée service UE RT-0918 | 370,00 | |
| 22/10/2026 | AC | 44522 | TVA due – services UE / hors UE | TVA autoliquidée service UE RT-0918 | | 370,00 |
| | | | | **Total** | **2 220,00** | **2 220,00** |

> **Piège / contrôle :** prestation B2B : lieu d'imposition en France (siège du preneur) → c'est la filiale qui **autoliquide**. La TVA due et la TVA déductible apparaissent toutes deux sur la CA3 (lignes distinctes). Erreur classique : payer une facture étrangère « TTC » avec une TVA allemande (non récupérable par la CA3 : demande de remboursement spécifique).

#### A12 — Acquisition intracommunautaire de biens
**Contexte :** achat de lavettes microfibres à un fabricant italien, livrées au dépôt de Nice.
**Pièce :** facture Microfibre Italia Srl n° MI-4471 du 15/10/2026 : 4 200,00 € HT, « Exempt – art. 138 directive 2006/112/CE », n° TVA IT et FR.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | AC | 6022 | Fournitures consommables – produits d'entretien | MI-4471 microfibres [ETB061] | 4 200,00 | |
| 15/10/2026 | AC | 401000 | Fournisseurs – Microfibre Italia Srl (F00822) | MI-4471 | | 4 200,00 |
| 15/10/2026 | AC | 445662 | TVA déductible – autoliquidation | TVA AIC MI-4471 | 840,00 | |
| 15/10/2026 | AC | 44521 | TVA due – acquisitions intracommunautaires | TVA AIC MI-4471 | | 840,00 |
| | | | | **Total** | **5 040,00** | **5 040,00** |

> **Piège / contrôle :** vérifiez le **numéro de TVA intracommunautaire** du fournisseur (VIES) ; l'exigibilité intervient le 15 du mois suivant le fait générateur ou à la date de la facture si elle est antérieure. Selon les volumes, l'enquête statistique sur les échanges de biens (EMEBI) peut être obligatoire.

#### A13 — Logiciel SaaS facturé par un prestataire hors UE (en dollars)
**Contexte :** abonnement mensuel à un logiciel de planification des équipes, éditeur américain.
**Pièce :** facture CloudPlan Inc. n° INV-77812 du 01/10/2026 : 1 200,00 USD, sans TVA. Cours retenu à la date de facture : 1 € = 1,0800 USD → 1 111,11 €. Paiement le 31/10/2026 au cours de 1,0750 → 1 116,28 €.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/10/2026 | AC | 6135 | Locations mobilières – abonnements SaaS | INV-77812 planification oct. [SIEGE] | 1 111,11 | |
| 01/10/2026 | AC | 401000 | Fournisseurs – CloudPlan Inc. (F00905) | INV-77812 (1 200,00 USD) | | 1 111,11 |
| 01/10/2026 | AC | 445662 | TVA déductible – autoliquidation | TVA autoliquidée service hors UE | 222,22 | |
| 01/10/2026 | AC | 44522 | TVA due – services UE / hors UE | TVA autoliquidée service hors UE | | 222,22 |
| 31/10/2026 | BQ1 | 401000 | Fournisseurs – CloudPlan Inc. (F00905) | Règlt INV-77812 | 1 111,11 | |
| 31/10/2026 | BQ1 | 656 | Pertes de change sur créances et dettes commerciales | Perte de change INV-77812 | 5,17 | |
| 31/10/2026 | BQ1 | 5121 | Banque A | Règlt 1 200,00 USD | | 1 116,28 |
| | | | | **Total** | **2 449,61** | **2 449,61** |

> **Piège / contrôle :** un abonnement SaaS est une **charge** (pas de 205 : on n'acquiert aucun droit durable). Le prestataire hors UE ne facture pas de TVA : la filiale autoliquide. La perte de change sur une **dette fournisseur** est désormais en **656** (exploitation), pas en 666.

#### A14 — Avoir fournisseur (retour de produits non conformes)
**Contexte :** retour d'un lot de désinfectant non conforme à la fiche technique.
**Pièce :** avoir Hygiène Pro Distribution n° HP-AV-2290 du 25/10/2026 : 420,00 HT ; TVA 84,00 ; TTC 504,00, référencé à la facture HP-88412.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 25/10/2026 | AC | 401000 | Fournisseurs – Hygiène Pro Distribution (F00412) | HP-AV-2290 | 504,00 | |
| 25/10/2026 | AC | 6022 | Fournitures consommables – produits d'entretien | HP-AV-2290 retour désinfectant [ETB061] | | 420,00 |
| 25/10/2026 | AC | 44566 | TVA déductible sur ABS | HP-AV-2290 | | 84,00 |
| | | | | **Total** | **504,00** | **504,00** |

> **Piège / contrôle :** un **retour** annule l'achat (crédit 6022) ; une **remise hors facture** ou une ristourne va en **609** (A18). Lettrez immédiatement l'avoir avec la facture d'origine pour ne pas payer celle-ci en totalité.

#### A15a — Acompte versé sur commande d'immobilisations
**Contexte :** commande de 3 autolaveuses (26 700,00 HT) ; le fournisseur exige 30 % à la commande.
**Pièce :** bon de commande n° BC-062-2026-114 signé ; demande d'acompte de 8 010,00 (livraison de biens : pas de TVA exigible sur l'acompte).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 26/10/2026 | BQ1 | 238 | Avances et acomptes versés sur immobilisations corporelles | Acompte 30 % BC-062-114 autolaveuses | 8 010,00 | |
| 26/10/2026 | BQ1 | 5121 | Banque A | Acompte Matériel Nettoyage Sud | | 8 010,00 |
| | | | | **Total** | **8 010,00** | **8 010,00** |

#### A15b — Acompte versé sur une prestation de services
**Contexte :** réservation d'un séminaire des chefs d'établissement ; le prestataire facture un acompte avec TVA.
**Pièce :** facture d'acompte Séminaires Riviera n° SR-A-0091 du 27/10/2026 : 2 000,00 HT ; TVA 400,00 ; TTC 2 400,00 ; payée le jour même.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 27/10/2026 | BQ1 | 4091 | Fournisseurs – avances et acomptes versés | Acompte SR-A-0091 séminaire | 2 000,00 | |
| 27/10/2026 | BQ1 | 44566 | TVA déductible sur ABS | TVA sur acompte payé SR-A-0091 | 400,00 | |
| 27/10/2026 | BQ1 | 5121 | Banque A | Acompte Séminaires Riviera | | 2 400,00 |
| | | | | **Total** | **2 400,00** | **2 400,00** |

> **Piège / contrôle (A15) :** acompte sur **immobilisation → 238**, sur charge → **4091**. Pour des **biens**, l'acompte n'ouvre pas droit à déduction (exigibilité à la livraison) ; pour des **services**, la TVA de l'acompte payé est déductible s'il existe une facture d'acompte. À la facture finale, soldez 238 / 4091.

#### A16 — Facture non parvenue (FNP) en fin de mois
**Contexte :** réparation de la porte sectionnelle du dépôt réalisée le 28/10, facture attendue.
**Pièce :** bon de réception / attachement signé du 28/10/2026 ; devis 1 750,00 HT.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6152 | Entretien et réparations sur biens immobiliers | FNP réparation porte dépôt [ETB061] | 1 750,00 | |
| 31/10/2026 | OD | 44586 | TVA sur factures non parvenues | FNP réparation porte dépôt | 350,00 | |
| 31/10/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Portes Azur (F00733) | | 2 100,00 |
| | | | | **Total** | **2 100,00** | **2 100,00** |

> **Piège / contrôle :** la FNP se justifie par une **pièce** (bon de réception, commande réceptionnée dans l'ERP, attachement). Extourne au 1er du mois suivant ; si la facture n'arrive pas, la FNP est **reconduite**, jamais oubliée. Un 408 de plus de 3 mois est un signal d'alerte (contrôle n° 4).

#### A17 — Avoir à recevoir
**Contexte :** livraison partiellement endommagée ; le fournisseur a accepté par écrit un avoir, non encore reçu au 31/10.
**Pièce :** e-mail d'accord du fournisseur du 29/10/2026 : avoir 600,00 HT + TVA 120,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 4098 | RRR à obtenir et autres avoirs non encore reçus | Avoir à recevoir Hygiène Pro | 720,00 | |
| 31/10/2026 | OD | 6022 | Fournitures consommables – produits d'entretien | Avoir à recevoir livraison endommagée [ETB062] | | 600,00 |
| 31/10/2026 | OD | 44586 | TVA sur factures non parvenues | TVA avoir à recevoir | | 120,00 |
| | | | | **Total** | **720,00** | **720,00** |

#### A18 — Ristourne de fin d'année (RFA) à recevoir
**Contexte :** le contrat cadre avec Hygiène Pro prévoit une RFA de 2 % au-delà de 150 000,00 HT d'achats annuels ; achats 2026 : 186 500,00 HT. RFA = 186 500,00 × 2 % = 3 730,00 (palier atteint : taux sur la totalité des achats selon le contrat).
**Pièce :** contrat cadre 2026 et état des achats annuels extrait de l'ERP.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 4098 | RRR à obtenir et autres avoirs non encore reçus | RFA 2026 Hygiène Pro | 4 476,00 | |
| 31/12/2026 | OD | 6092 | RRR obtenus sur achats d'approvisionnements | RFA 2026 Hygiène Pro [SIEGE] | | 3 730,00 |
| 31/12/2026 | OD | 44586 | TVA sur factures non parvenues | TVA RFA 2026 | | 746,00 |
| | | | | **Total** | **4 476,00** | **4 476,00** |

> **Piège / contrôle (A17-A18) :** une RFA réglée par **avoir** réduit la TVA déductible. Si le fournisseur verse une rémunération pour un **service de coopération commerciale** (mise en avant, référencement), c'est une **prestation facturée par la filiale** (produit en 7088 + TVA collectée), pas une RFA : lisez le contrat. Ne comptabilisez une RFA à recevoir que si le seuil est **atteint** (pas « probable »).

#### A19 — Note de frais d'un chef d'établissement
**Contexte :** déplacement pour une visite client et une soutenance d'appel d'offres.
**Pièce :** note de frais NDF-2026-10-118 avec justificatifs : repas d'affaires 86,40 TTC (TVA 10 % : 7,85) ; hôtel 132,00 TTC ; billet de train 64,00 TTC ; parking 18,00 TTC (TVA 3,00). Total 300,40.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6256 | Missions | NDF-118 repas d'affaires HT [ETB062] | 78,55 | |
| 31/10/2026 | OD | 6256 | Missions | NDF-118 hôtel TTC (TVA exclue) [ETB062] | 132,00 | |
| 31/10/2026 | OD | 6251 | Voyages et déplacements | NDF-118 train TTC (TVA exclue) [ETB062] | 64,00 | |
| 31/10/2026 | OD | 6251 | Voyages et déplacements | NDF-118 parking HT [ETB062] | 15,00 | |
| 31/10/2026 | OD | 44566 | TVA déductible sur ABS | NDF-118 TVA repas + parking | 10,85 | |
| 31/10/2026 | OD | 421800 | Personnel – notes de frais à rembourser | NDF-118 M. Ruiz | | 300,40 |
| | | | | **Total** | **300,40** | **300,40** |

> **Piège / contrôle :** TVA **non déductible** sur l'**hébergement** des salariés et dirigeants et sur le **transport de personnes** ; déductible sur les repas et le parking **si** le justificatif est une facture comportant les mentions (un simple ticket de carte bancaire ne suffit pas). Contrôlez le respect de la **politique voyages** du groupe et l'approbation hiérarchique.

#### A20 — Cadeaux à la clientèle
**Contexte :** coffrets de fin d'année pour 45 interlocuteurs clients.
**Pièce :** facture Délices du Sud n° DS-3381 du 01/12/2026 : 45 coffrets × 60,00 HT = 2 700,00 ; TVA 540,00 ; TTC 3 240,00 ; liste nominative des bénéficiaires jointe.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/12/2026 | AC | 6234 | Cadeaux à la clientèle | DS-3381 coffrets fin d'année [ETB061] | 2 700,00 | |
| 01/12/2026 | AC | 44566 | TVA déductible sur ABS | DS-3381 (72,00 TTC/bénéficiaire ≤ seuil) | 540,00 | |
| 01/12/2026 | AC | 401000 | Fournisseurs – Délices du Sud (F00940) | DS-3381 | | 3 240,00 |
| | | | | **Total** | **3 240,00** | **3 240,00** |

> **Piège / contrôle :** la TVA sur cadeaux n'est déductible que si la valeur unitaire ne dépasse pas un seuil **par bénéficiaire et par an** (on retient **73,00 € TTC** — *valeur à vérifier chaque année*). À 62,00 HT (74,40 TTC), la TVA serait **entièrement** non déductible. Conservez la liste des bénéficiaires (relevé des frais généraux selon les seuils).

#### A21a — Loyer trimestriel d'agence (bail commercial avec option TVA du bailleur)
**Contexte :** loyer de l'agence de Cannes, payable trimestriellement d'avance.
**Pièce :** avis d'échéance SCI Croisette du 01/10/2026 : loyer T4 7 500,00 HT ; provisions sur charges 900,00 HT ; TVA 1 680,00 ; TTC 10 080,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/10/2026 | AC | 6132 | Locations immobilières | Loyer T4 2026 agence Cannes [ETB062] | 7 500,00 | |
| 01/10/2026 | AC | 614 | Charges locatives et de copropriété | Provisions charges T4 [ETB062] | 900,00 | |
| 01/10/2026 | AC | 44566 | TVA déductible sur ABS | Avis d'échéance T4 | 1 680,00 | |
| 01/10/2026 | AC | 401000 | Fournisseurs – SCI Croisette (F00120) | Avis d'échéance T4 | | 10 080,00 |
| | | | | **Total** | **10 080,00** | **10 080,00** |

#### A21b — Dépôt de garantie versé à la signature d'un nouveau bail
**Contexte :** ouverture d'une antenne à Toulon ; dépôt de garantie de deux trimestres de loyer hors charges.
**Pièce :** bail commercial signé le 15/10/2026, dépôt de garantie 15 000,00 (hors champ de la TVA).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | BQ1 | 275 | Dépôts et cautionnements versés | Dépôt de garantie bail antenne Toulon [ETB083] | 15 000,00 | |
| 15/10/2026 | BQ1 | 5121 | Banque A | Dépôt de garantie SCI Mourillon | | 15 000,00 |
| | | | | **Total** | **15 000,00** | **15 000,00** |

> **Piège / contrôle (A21) :** un avis d'échéance n'est une **facture** que s'il en comporte les mentions (sinon, TVA déductible seulement sur la quittance / la facture). Le dépôt de garantie est une **créance** (275), jamais une charge ; la **régularisation annuelle des charges** donne lieu à une facture complémentaire ou à un avoir. Un loyer facturé en décembre pour le 1er trimestre suivant → **CCA**.

#### A22 — Prime d'assurance flotte (exonérée de TVA)
**Contexte :** prime annuelle d'assurance de la flotte, période du 01/04/2026 au 31/03/2027.
**Pièce :** avis d'échéance Assur'Flotte n° AF-2026-221 du 01/04/2026 : 18 000,00 taxes d'assurance comprises.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/04/2026 | AC | 616 | Primes d'assurance | AF-2026-221 flotte 04/2026-03/2027 [SIEGE] | 18 000,00 | |
| 01/04/2026 | AC | 401000 | Fournisseurs – Assur'Flotte (F00055) | AF-2026-221 | | 18 000,00 |
| | | | | **Total** | **18 000,00** | **18 000,00** |

> **Piège / contrôle :** pas de TVA sur les primes d'assurance (taxe spéciale incluse dans le prix). Au 31/12, 3 mois sur 12 concernent 2027 → **CCA** de 4 500,00 (C01). En clôture **mensuelle**, beaucoup de groupes étalent la prime (1/12 par mois via 486) pour lisser le résultat.

#### A23 — Facture fournisseur en litige (quantité facturée non livrée)
**Contexte :** trois monobrosses facturées, deux livrées ; le fournisseur reconnaît l'erreur mais l'avoir n'est pas émis à la clôture du mois.
**Pièce :** facture Matériel Nettoyage Sud n° MNS-7790 du 28/10/2026 : 3 × 1 450,00 = 4 350,00 HT ; TVA 870,00 ; TTC 5 220,00 ; bon de livraison : 2 unités ; statut « litige » transmis via la plateforme.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | ACI | 2154 | Matériel de nettoyage | MNS-7790 2 monobrosses livrées [ETB083] | 2 900,00 | |
| 31/10/2026 | ACI | 44562 | TVA déductible sur immobilisations | MNS-7790 TVA sur 2 unités livrées | 580,00 | |
| 31/10/2026 | ACI | 4098 | RRR à obtenir et autres avoirs non encore reçus | MNS-7790 unité non livrée (TTC) – litige | 1 740,00 | |
| 31/10/2026 | ACI | 404000 | Fournisseurs d'immobilisations – Matériel Nettoyage Sud | MNS-7790 – BLOQUÉE litige | | 5 220,00 |
| | | | | **Total** | **5 220,00** | **5 220,00** |

> **Piège / contrôle :** la dette est constatée pour son montant **facturé** (le fournisseur la réclamera) mais le **paiement est bloqué** (code blocage dans l'ERP) ; on n'immobilise que ce qui est **livré** et l'on ne déduit que la TVA afférente. À réception de l'avoir : débit 404000 1 740,00 / crédit 4098 1 740,00. Avec la facturation électronique, signalez le litige par le **statut du cycle de vie** (« en litige », ou « refusée » si la facture est entièrement à reprendre). Tenez un **tableau de suivi des litiges** (date, motif, interlocuteur Achats, relance) : c'est le cœur du poste d'assistante comptable fournisseurs.

#### A24 — Règlement par virement SEPA avec escompte obtenu
**Contexte :** paiement anticipé à 10 jours de la facture A01 pour bénéficier de l'escompte de 1 %.
**Pièce :** ordre de virement SEPA du 17/10/2026 : 3 588,00 − escompte (29,90 HT + TVA 5,98) = 3 552,12 ; avoir d'escompte demandé au fournisseur.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 17/10/2026 | BQ1 | 401000 | Fournisseurs – Hygiène Pro Distribution (F00412) | Règlt HP-88412 | 3 588,00 | |
| 17/10/2026 | BQ1 | 5121 | Banque A | Vir. SEPA HP-88412 escompte déduit | | 3 552,12 |
| 17/10/2026 | BQ1 | 765 | Escomptes obtenus | Escompte 1 % HP-88412 | | 29,90 |
| 17/10/2026 | BQ1 | 44566 | TVA déductible sur ABS | Régularisation TVA sur escompte | | 5,98 |
| | | | | **Total** | **3 588,00** | **3 588,00** |

> **Piège / contrôle :** l'escompte obtenu est un **produit financier** (765). La TVA déductible doit être réduite à hauteur de l'escompte. Avant tout virement : **contrôle du RIB** (procédure anti-fraude au faux fournisseur : tout changement de coordonnées bancaires se vérifie par contre-appel à un numéro connu, jamais celui du courriel).

#### A25 — Retenue de garantie sur sous-traitant de travaux
**Contexte :** deuxième lot de nettoyage de fin de chantier (autoliquidation BTP) ; le contrat prévoit une retenue de garantie de 5 % libérable au bout d'un an.
**Pièce :** facture Fin de Chantier Express n° FCE-131 du 30/11/2026 : 6 000,00 HT, « Autoliquidation » ; paiement le 15/12/2026 de 95 %.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | AC | 611 | Sous-traitance générale | FCE-131 fin de chantier lot 2 [ETB083/REM/CT-0590] | 6 000,00 | |
| 30/11/2026 | AC | 401000 | Fournisseurs – Fin de Chantier Express (F00702) | FCE-131 | | 6 000,00 |
| 15/12/2026 | BQ1 | 401000 | Fournisseurs – Fin de Chantier Express (F00702) | Règlt FCE-131 | 6 000,00 | |
| 15/12/2026 | BQ1 | 5121 | Banque A | Règlt FCE-131 (95 %) | | 5 700,00 |
| 15/12/2026 | BQ1 | 4017 | Fournisseurs – retenues de garantie | Retenue 5 % FCE-131 | | 300,00 |
| 15/12/2026 | OD | 445662 | TVA déductible – autoliquidation | TVA autoliquidée sur 5 700,00 payés | 1 140,00 | |
| 15/12/2026 | OD | 44523 | TVA due – autoliquidation sous-traitance BTP | TVA autoliquidée sur 5 700,00 payés | | 1 140,00 |
| | | | | **Total** | **13 140,00** | **13 140,00** |

> **Piège / contrôle :** la retenue reste une **dette** envers le sous-traitant (4017), à suivre dans un échéancier. La TVA autoliquidée sur travaux étant exigible au paiement, les 60,00 restant (20 % × 300,00) seront autoliquidés à la **libération** de la retenue. Une retenue de garantie peut être remplacée par une **caution bancaire** du sous-traitant : vérifiez le contrat.

### 3.3 Cycle trésorerie

#### T01 — Frais bancaires du relevé mensuel
**Contexte :** prélèvement des frais de tenue de compte et des commissions du mois.
**Pièce :** relevé Banque A d'octobre 2026 + facture récapitulative des frais : tenue de compte 45,00 HT + TVA 9,00 ; commissions d'intervention et de virements 28,00 (non soumises) ; total 82,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | BQ1 | 627 | Services bancaires | Tenue de compte oct. | 45,00 | |
| 31/10/2026 | BQ1 | 44566 | TVA déductible sur ABS | TVA frais bancaires (facture banque) | 9,00 | |
| 31/10/2026 | BQ1 | 627 | Services bancaires | Commissions oct. (non soumises) | 28,00 | |
| 31/10/2026 | BQ1 | 5121 | Banque A | Frais bancaires oct. | | 82,00 |
| | | | | **Total** | **82,00** | **82,00** |

> **Piège / contrôle :** on ne déduit la TVA bancaire que si la banque a émis une **facture** la faisant apparaître (beaucoup de commissions sont exonérées). Les **agios** (intérêts débiteurs) vont en **6615**, pas en 627.

#### T02 — Virement interne entre deux banques
**Contexte :** équilibrage de trésorerie de la Banque A vers la Banque B (prélèvements de loyers à venir).
**Pièce :** relevés Banque A (débit le 12/10) et Banque B (crédit le 13/10) : 50 000,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 12/10/2026 | BQ1 | 58 | Virements internes | Vir. Banque A → Banque B | 50 000,00 | |
| 12/10/2026 | BQ1 | 5121 | Banque A | Vir. Banque A → Banque B | | 50 000,00 |
| 13/10/2026 | BQ2 | 5122 | Banque B | Vir. reçu de Banque A | 50 000,00 | |
| 13/10/2026 | BQ2 | 58 | Virements internes | Vir. reçu de Banque A | | 50 000,00 |
| | | | | **Total** | **100 000,00** | **100 000,00** |

> **Piège / contrôle :** chaque journal de banque ne saisit que **son** relevé ; le 58 fait le lien. Un solde en 58 en fin de mois = virement saisi d'un seul côté (ou en double).

#### T03 — Cash pooling (remontée et redescente de trésorerie)
**Contexte :** convention de trésorerie avec mise à zéro quotidienne (*zero balancing*) : le solde du compte de la filiale est remonté chaque soir vers le compte centralisateur de la société tête.
**Pièce :** relevés Banque A des 14 et 15/10/2026 : remontée de 237 450,00 le 14 ; couverture d'un solde débiteur de 62 300,00 le 15.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 14/10/2026 | BQ1 | 4511 | Groupe – compte courant cash pooling | Remontée zero balancing 14/10 | 237 450,00 | |
| 14/10/2026 | BQ1 | 5121 | Banque A | Remontée zero balancing 14/10 | | 237 450,00 |
| 15/10/2026 | BQ1 | 5121 | Banque A | Redescente zero balancing 15/10 | 62 300,00 | |
| 15/10/2026 | BQ1 | 4511 | Groupe – compte courant cash pooling | Redescente zero balancing 15/10 | | 62 300,00 |
| | | | | **Total** | **299 750,00** | **299 750,00** |

> **Piège / contrôle :** un 4511 **débiteur** = la filiale **prête** au groupe ; **créditeur** = elle **emprunte**. Chaque mois, rapprochez le solde de 4511 avec l'**extrait de compte courant** envoyé par la trésorerie groupe (contrôle n° 13) : c'est la base des éliminations en consolidation. Au bilan, le solde est classé en créance ou dette financière groupe, pas en trésorerie.

#### T04 — Encaissement d'un emprunt bancaire
**Contexte :** financement du renouvellement du parc d'autolaveuses.
**Pièce :** contrat de prêt du 02/11/2026 : 300 000,00, 5 ans, taux fixe 3,50 %, frais de dossier 750,00 prélevés au déblocage ; tableau d'amortissement joint.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/11/2026 | BQ1 | 5121 | Banque A | Déblocage prêt n° 88-2026 | 299 250,00 | |
| 02/11/2026 | BQ1 | 627 | Services bancaires | Frais de dossier prêt n° 88-2026 | 750,00 | |
| 02/11/2026 | BQ1 | 164 | Emprunts auprès des établissements de crédit | Prêt n° 88-2026 | | 300 000,00 |
| | | | | **Total** | **300 000,00** | **300 000,00** |

> **Piège / contrôle :** l'emprunt s'inscrit pour son **nominal** (300 000,00), pas pour le net reçu. Les frais d'émission peuvent être passés en charge (retenu ici) ou étalés sur la durée du prêt (*compte selon la nomenclature 2025 du PCG*) : c'est un choix de méthode du groupe, à appliquer de façon permanente.

#### T05 — Échéance mensuelle d'emprunt
**Contexte :** première échéance selon le tableau d'amortissement.
**Pièce :** avis d'échéance du 02/12/2026 : capital 4 875,32 ; intérêts 875,00 ; total 5 750,32.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/12/2026 | BQ1 | 164 | Emprunts auprès des établissements de crédit | Échéance 1/60 capital | 4 875,32 | |
| 02/12/2026 | BQ1 | 6611 | Intérêts des emprunts et dettes | Échéance 1/60 intérêts | 875,00 | |
| 02/12/2026 | BQ1 | 5121 | Banque A | Échéance prêt n° 88-2026 | | 5 750,32 |
| | | | | **Total** | **5 750,32** | **5 750,32** |

> **Piège / contrôle :** seul le capital diminue la dette. Contrôle annuel : solde du 164 = capital restant dû au tableau d'amortissement au 31/12.

#### T06 — Intérêts courus non échus à la clôture
**Contexte :** autre emprunt dont l'échéance tombe le 15 de chaque mois ; au 31/12, 16 jours d'intérêts sont courus.
**Pièce :** tableau d'amortissement : capital restant dû 271 480,00, taux 3,50 %, base 360 jours : 271 480,00 × 3,50 % × 16 / 360 = 422,30.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6611 | Intérêts des emprunts et dettes | ICNE prêt n° 51-2024 (16 j) | 422,30 | |
| 31/12/2026 | OD | 1688 | Intérêts courus sur emprunts | ICNE prêt n° 51-2024 | | 422,30 |
| | | | | **Total** | **422,30** | **422,30** |

#### T07 — Rapprochement bancaire : écritures de régularisation
**Contexte :** le rapprochement d'octobre fait apparaître des opérations du relevé non comptabilisées.
**Pièce :** état de rapprochement Banque A au 31/10/2026 : prélèvement télécom 156,00 (facture déjà saisie) ; agios 37,20 ; virement reçu non identifié 1 980,00 ; **LCR impayée** 8 400,00 (V18) + frais d'impayé 15,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | BQ1 | 401000 | Fournisseurs – Télécom Pro (F00077) | Prlv SEPA facture oct. | 156,00 | |
| 31/10/2026 | BQ1 | 5121 | Banque A | Prlv SEPA Télécom Pro | | 156,00 |
| 31/10/2026 | BQ1 | 6615 | Intérêts des comptes courants et dépôts créditeurs | Agios oct. | 37,20 | |
| 31/10/2026 | BQ1 | 5121 | Banque A | Agios oct. | | 37,20 |
| 31/10/2026 | BQ1 | 5121 | Banque A | Vir. reçu « REGLT FACT » non identifié | 1 980,00 | |
| 31/10/2026 | BQ1 | 471 | Compte d'attente | Vir. non identifié – à analyser | | 1 980,00 |
| 31/10/2026 | BQ1 | 411000 | Clients – Agroalim Sud (C00512) | Impayé LCR n° 4471 | 8 400,00 | |
| 31/10/2026 | BQ1 | 5121 | Banque A | Impayé LCR n° 4471 | | 8 400,00 |
| 31/10/2026 | BQ1 | 627 | Services bancaires | Frais d'impayé LCR n° 4471 | 15,00 | |
| 31/10/2026 | BQ1 | 5121 | Banque A | Frais d'impayé | | 15,00 |
| 31/10/2026 | OD | 44571 | TVA collectée | Annulation exigibilité LCR impayée | 1 400,00 | |
| 31/10/2026 | OD | 44574 | TVA collectée en attente (encaissements) | Annulation exigibilité LCR impayée | | 1 400,00 |
| | | | | **Total** | **11 988,20** | **11 988,20** |

> **Piège / contrôle :** l'impayé **annule l'encaissement** : la TVA qui avait été rendue exigible repasse « en attente » (sinon elle sera déclarée sans avoir été encaissée). Le rapprochement est fini quand il ne reste que des **suspens explicables** (chèques émis non débités, remises en cours) ; tout suspens de plus d'un mois doit être analysé.

#### T08 — Identification du virement en compte d'attente
**Contexte :** la relance du service recouvrement permet d'identifier le virement de 1 980,00 : règlement d'une facture de vitrerie de Pharma Côte.
**Pièce :** avis de paiement transmis par le client le 04/11/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 04/11/2026 | OD | 471 | Compte d'attente | Identification vir. du 30/10 | 1 980,00 | |
| 04/11/2026 | OD | 411000 | Clients – Pharma Côte (C00611) | Règlt FV26-09-0388 | | 1 980,00 |
| 04/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | TVA exigible FV26-09-0388 | 330,00 | |
| 04/11/2026 | OD | 44571 | TVA collectée | TVA exigible FV26-09-0388 | | 330,00 |
| | | | | **Total** | **2 310,00** | **2 310,00** |

> **Piège / contrôle :** la TVA est exigible à la date d'**encaissement** (30/10, donc sur la CA3 d'**octobre**) même si l'identification intervient en novembre : si la CA3 d'octobre n'est pas encore déposée, intégrez-la ; sinon, régularisez sur la suivante. Le 471 doit être **vide** à chaque clôture mensuelle.

### 3.4 Cycle paie (secteur de la propreté)

> 💡 **Contexte sectoriel :** convention collective des entreprises de propreté et services associés (**IDCC 3043**) ; beaucoup de **temps partiels** (heures complémentaires), horaires décalés, **primes de panier et de salissure**, multi-sites, fort taux d'accidents du travail (IJSS), **reprise du personnel** en cas de changement de prestataire. La paie est produite par le service paie ; la comptabilité intègre le **journal de paie** et contrôle les comptes de tiers sociaux. Les taux ci-dessous sont des agrégats fictifs (*valeurs à vérifier chaque année*).

#### P01 — Journal de paie mensuel : rémunérations et part salariale
**Contexte :** paie d'octobre de l'établissement de Nice (environ 120 salariés, majoritairement à temps partiel).
**Pièce :** journal de paie octobre 2026 : salaires de base 210 000,00 ; heures complémentaires 12 500,00 ; congés payés pris 18 000,00 ; primes de salissure et d'ancienneté 6 800,00 ; primes de panier 4 200,00 et indemnités de transport 1 500,00 ; cotisations salariales URSSAF 30 000,00, retraite complémentaire 15 500,00, mutuelle/prévoyance 6 500,00 ; PAS 6 300,00 ; acomptes déjà versés 8 000,00 ; saisies sur salaire 1 250,00 ; net à payer 185 450,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | PAIE | 6411 | Salaires, appointements | Salaires de base oct. [ETB061] | 210 000,00 | |
| 31/10/2026 | PAIE | 6411 | Salaires, appointements | Heures complémentaires oct. [ETB061] | 12 500,00 | |
| 31/10/2026 | PAIE | 6412 | Congés payés | CP pris oct. [ETB061] | 18 000,00 | |
| 31/10/2026 | PAIE | 6413 | Primes et gratifications | Primes salissure / ancienneté [ETB061] | 6 800,00 | |
| 31/10/2026 | PAIE | 6414 | Indemnités et avantages divers | Paniers et transport [ETB061] | 5 700,00 | |
| 31/10/2026 | PAIE | 431 | Sécurité sociale (URSSAF) | Cotisations salariales URSSAF | | 30 000,00 |
| 31/10/2026 | PAIE | 4373 | Caisses de retraite complémentaire | Cotisations salariales retraite | | 15 500,00 |
| 31/10/2026 | PAIE | 4372 | Mutuelle / prévoyance | Cotisations salariales mutuelle-prévoyance | | 6 500,00 |
| 31/10/2026 | PAIE | 4421 | Prélèvement à la source | PAS oct. | | 6 300,00 |
| 31/10/2026 | PAIE | 425 | Personnel – avances et acomptes | Imputation acomptes du 15/10 | | 8 000,00 |
| 31/10/2026 | PAIE | 427 | Personnel – oppositions | Saisies sur salaire oct. | | 1 250,00 |
| 31/10/2026 | PAIE | 421 | Personnel – rémunérations dues | Net à payer oct. | | 185 450,00 |
| | | | | **Total** | **253 000,00** | **253 000,00** |

#### P02 — Journal de paie mensuel : charges patronales
**Pièce :** même journal de paie : URSSAF patronales (après réduction générale) 42 000,00 ; retraite complémentaire 21 000,00 ; mutuelle/prévoyance de branche 7 500,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | PAIE | 6451 | Cotisations à l'URSSAF | Charges patronales URSSAF oct. [ETB061] | 42 000,00 | |
| 31/10/2026 | PAIE | 6453 | Cotisations aux caisses de retraite | Retraite patronale oct. [ETB061] | 21 000,00 | |
| 31/10/2026 | PAIE | 6452 | Cotisations aux mutuelles | Mutuelle-prévoyance patronale oct. [ETB061] | 7 500,00 | |
| 31/10/2026 | PAIE | 431 | Sécurité sociale (URSSAF) | Charges patronales URSSAF | | 42 000,00 |
| 31/10/2026 | PAIE | 4373 | Caisses de retraite complémentaire | Retraite patronale | | 21 000,00 |
| 31/10/2026 | PAIE | 4372 | Mutuelle / prévoyance | Mutuelle-prévoyance patronale | | 7 500,00 |
| | | | | **Total** | **70 500,00** | **70 500,00** |

> **Piège / contrôle (P01-P02) :** contrôlez que **brut − retenues = net** et que le total des crédits 431/437 correspond aux montants de la **DSN** (contrôle n° 10). Les heures complémentaires des temps partiels sont majorées (10 % puis 25 % selon le volume, accords à vérifier) et bénéficient d'une réduction de cotisations salariales et d'une exonération d'impôt sur le revenu dans une limite annuelle. Les **primes de panier** sont des frais professionnels (non soumis dans les limites) : elles restent en **6414**. Les **saisies** (427) sont reversées au créancier ou au greffe, pas au salarié.

#### P03 — Règlement des salaires et des organismes sociaux
**Pièce :** virement des nets le 31/10 ; prélèvements URSSAF (dont PAS), retraite et prévoyance le 15/11 ; virement des saisies au créancier.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | BQ1 | 421 | Personnel – rémunérations dues | Virement des nets oct. | 185 450,00 | |
| 15/11/2026 | BQ1 | 431 | Sécurité sociale (URSSAF) | Prlv DSN URSSAF oct. | 72 000,00 | |
| 15/11/2026 | BQ1 | 4421 | Prélèvement à la source | Prlv DSN PAS oct. | 6 300,00 | |
| 15/11/2026 | BQ1 | 4373 | Caisses de retraite complémentaire | Prlv retraite oct. | 36 500,00 | |
| 15/11/2026 | BQ1 | 4372 | Mutuelle / prévoyance | Prlv mutuelle-prévoyance oct. | 14 000,00 | |
| 15/11/2026 | BQ1 | 427 | Personnel – oppositions | Reversement saisies oct. | 1 250,00 | |
| 15/11/2026 | BQ1 | 5121 | Banque A | Règlements sociaux oct. | | 315 500,00 |
| | | | | **Total** | **315 500,00** | **315 500,00** |

> **Piège / contrôle :** après ces règlements, 421, 431, 437, 4421 et 427 doivent être **soldés** pour le mois concerné. Un 421 résiduel = net non versé (salarié sans RIB, virement rejeté) à traiter avec la paie.

#### P04 — Acompte sur salaire versé en cours de mois
**Pièce :** liste des acomptes demandés validée par le chef d'établissement, virés le 15/10/2026 : 8 000,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | BQ1 | 425 | Personnel – avances et acomptes | Acomptes oct. (liste n° 061-10) | 8 000,00 | |
| 15/10/2026 | BQ1 | 5121 | Banque A | Acomptes oct. | | 8 000,00 |
| | | | | **Total** | **8 000,00** | **8 000,00** |

> **Piège / contrôle :** le 425 est soldé par la paie (P01). Une **avance** (somme supérieure au salaire acquis, remboursable en plusieurs fois) se suit par salarié et se rembourse dans les limites de la quotité saisissable.

#### P05 — IJSS en subrogation (sans compte de transfert de charges)
**Contexte :** une salariée en arrêt maladie : l'employeur maintient le salaire (inclus dans P01) et perçoit les IJSS à sa place.
**Pièce :** attestation de salaire transmise ; décompte CPAM du 20/11/2026 : IJSS subrogées octobre 2 346,80, virées le 25/11/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | PAIE | 4387 | Organismes sociaux – produits à recevoir | IJSS subrogées oct. à recevoir | 2 346,80 | |
| 31/10/2026 | PAIE | 641190 | Salaires – IJSS subrogées (en diminution) | IJSS subrogées oct. [ETB061] | | 2 346,80 |
| 25/11/2026 | BQ1 | 5121 | Banque A | Vir. CPAM IJSS | 2 346,80 | |
| 25/11/2026 | BQ1 | 4387 | Organismes sociaux – produits à recevoir | Encaissement IJSS oct. | | 2 346,80 |
| | | | | **Total** | **4 693,60** | **4 693,60** |

> **Piège / contrôle :** **plus de compte 791** depuis le PCG 2025 : les IJSS viennent **en diminution de la charge de salaires** (sous-compte de 6411). Rapprochez chaque mois le 4387 avec les décomptes CPAM : un 4387 qui grossit = IJSS jamais versées (attestation de salaire manquante, arrêt non transmis) — fréquent dans un secteur à fort taux d'AT.

#### P06 — Provision mensuelle pour congés payés et charges sociales
**Contexte :** clôture mensuelle : mise à jour de la dette de congés payés acquis et non pris.
**Pièce :** état des droits CP au 31/10/2026 : 412 000,00 (contre 398 500,00 au 30/09) ; taux de charges patronales retenu sur CP : 42 %.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 6412 | Congés payés | Variation provision CP oct. [ETB061] | 13 500,00 | |
| 31/10/2026 | OD | 4282 | Dettes provisionnées pour congés à payer | Variation provision CP oct. | | 13 500,00 |
| 31/10/2026 | OD | 6451 | Cotisations à l'URSSAF | Charges sur variation CP (42 %) [ETB061] | 5 670,00 | |
| 31/10/2026 | OD | 4382 | Charges sociales sur congés à payer | Charges sur variation CP | | 5 670,00 |
| | | | | **Total** | **19 170,00** | **19 170,00** |

> **Piège / contrôle :** on comptabilise la **variation** (ici + 13 500,00), pas le stock. Le secteur de la propreté n'a pas de caisse de congés payés (contrairement au BTP) : la dette est chez l'employeur. Vérifiez la cohérence avec les règles d'acquisition de CP pendant les arrêts maladie.

#### P07 — Indemnités de rupture (licenciement)
**Contexte :** licenciement d'une agente de service ; solde de tout compte.
**Pièce :** bulletin de sortie du 30/11/2026 : indemnité compensatrice de préavis 2 100,00 ; indemnité compensatrice de CP 1 150,00 ; indemnité légale de licenciement 8 640,00 (exonérée dans les limites légales) ; cotisations salariales URSSAF 500,00, retraite 215,00 ; PAS 120,00 ; net 11 055,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | PAIE | 6411 | Salaires, appointements | Préavis payé non effectué [ETB062] | 2 100,00 | |
| 30/11/2026 | PAIE | 6412 | Congés payés | Indemnité compensatrice de CP [ETB062] | 1 150,00 | |
| 30/11/2026 | PAIE | 6414 | Indemnités et avantages divers | Indemnité légale de licenciement [ETB062] | 8 640,00 | |
| 30/11/2026 | PAIE | 431 | Sécurité sociale (URSSAF) | Cotisations salariales sortie | | 500,00 |
| 30/11/2026 | PAIE | 4373 | Caisses de retraite complémentaire | Cotisations salariales sortie | | 215,00 |
| 30/11/2026 | PAIE | 4421 | Prélèvement à la source | PAS sortie | | 120,00 |
| 30/11/2026 | PAIE | 421 | Personnel – rémunérations dues | Solde de tout compte | | 11 055,00 |
| | | | | **Total** | **11 890,00** | **11 890,00** |

> **Piège / contrôle :** l'indemnité de licenciement reste en **charges de personnel** (6414) et donc en résultat d'exploitation : jamais en exceptionnel. Si un litige prud'homal est ouvert ensuite, il donne lieu à une **provision** (C05). Pensez à la reprise de la provision CP correspondant aux droits soldés.

#### P08 — Reprise de personnel (article 7 de la CCN propreté) : ce qu'il faut — et ne faut pas — comptabiliser
**Contexte :** la filiale **perd** le marché d'un client ; 18 salariés affectés au site sont **transférés** au nouveau prestataire au 01/11/2026 en application de l'article 7 de la convention collective.

**Ce que passe l'entreprise ENTRANTE : rien de spécifique.** Les salariés repris entrent dans la paie (P01) avec leur ancienneté. Selon le dispositif conventionnel, les congés payés acquis chez l'ancien employeur sont **réglés par l'entreprise sortante** : l'entrante ne reprend donc **pas** de provision CP et n'enregistre ni dette ni créance envers le sortant (*modalités exactes à vérifier dans le texte conventionnel en vigueur et l'accord éventuel entre les deux entreprises*). En revanche, l'**ancienneté reprise** augmente l'engagement d'indemnités de fin de carrière et les futures indemnités de rupture.

**Ce que passe l'entreprise SORTANTE :** paiement des indemnités compensatrices de CP aux salariés transférés, puis reprise de la provision devenue sans objet.
**Pièce :** bulletins de sortie du 31/10/2026 : ICCP 23 400,00 ; cotisations salariales 3 744,00 (URSSAF) et 1 404,00 (retraite) ; net 18 252,00 ; charges patronales 9 828,00 (42 %) ; provision CP correspondante au 30/09 : 23 400,00 + charges 9 828,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | PAIE | 6412 | Congés payés | ICCP salariés transférés art. 7 [ETB083] | 23 400,00 | |
| 31/10/2026 | PAIE | 431 | Sécurité sociale (URSSAF) | Cotisations salariales ICCP | | 3 744,00 |
| 31/10/2026 | PAIE | 4373 | Caisses de retraite complémentaire | Cotisations salariales ICCP | | 1 404,00 |
| 31/10/2026 | PAIE | 421 | Personnel – rémunérations dues | Net ICCP salariés transférés | | 18 252,00 |
| 31/10/2026 | PAIE | 6451 | Cotisations à l'URSSAF | Charges patronales ICCP [ETB083] | 9 828,00 | |
| 31/10/2026 | PAIE | 431 | Sécurité sociale (URSSAF) | Charges patronales ICCP | | 9 828,00 |
| 31/10/2026 | OD | 4282 | Dettes provisionnées pour congés à payer | Reprise provision CP salariés transférés | 23 400,00 | |
| 31/10/2026 | OD | 6412 | Congés payés | Reprise provision CP [ETB083] | | 23 400,00 |
| 31/10/2026 | OD | 4382 | Charges sociales sur congés à payer | Reprise charges sur CP transférés | 9 828,00 | |
| 31/10/2026 | OD | 6451 | Cotisations à l'URSSAF | Reprise charges sur CP [ETB083] | | 9 828,00 |
| | | | | **Total** | **66 456,00** | **66 456,00** |

> **Piège / contrôle :** en entretien, la bonne réponse à « la reprise de personnel, vous passez quoi ? » est : **« côté entrant, aucune écriture de transfert : ce n'est pas une acquisition d'activité, il n'y a ni prix ni actif ; les salariés entrent simplement en paie. Côté sortant, on solde les CP et l'on reprend la provision. »** Puis : impacts à surveiller — ancienneté (IFC), éventuels **matériels** rachetés au sortant (écriture d'immobilisation classique), et fin des **charges** du site perdu (sous-traitants, LLD à réaffecter).

#### P09 — Participation des salariés (clôture annuelle)
**Contexte :** calcul de la réserve spéciale de participation selon la formule légale.
**Pièce :** calcul de la RSP 2026 : 186 000,00 ; forfait social retenu 20 % (*valeur à vérifier*) : 37 200,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 691 | Participation des salariés aux résultats | RSP 2026 | 186 000,00 | |
| 31/12/2026 | OD | 4246 | Participation – réserve spéciale | RSP 2026 | | 186 000,00 |
| 31/12/2026 | OD | 6458 | Cotisations aux autres organismes sociaux | Forfait social sur RSP 2026 | 37 200,00 | |
| 31/12/2026 | OD | 4386 | Organismes sociaux – autres charges à payer | Forfait social sur RSP 2026 | | 37 200,00 |
| | | | | **Total** | **223 200,00** | **223 200,00** |

> **Piège / contrôle :** la participation est en **691** (rubrique spécifique du compte de résultat), le forfait social en charges sociales. Le calcul utilise le bénéfice fiscal, les capitaux propres, la valeur ajoutée et les salaires : dans un groupe, il peut exister un **accord de groupe** répartissant une RSP globale.

#### P10 — Titres-restaurant : achat et retenue de la part salariale
**Contexte :** salariés de l'établissement sans restauration sur site.
**Pièce :** facture Titres Repas Services n° TRS-26-10-551 du 05/10/2026 : 2 160 titres × 9,00 = 19 440,00 (valeur faciale, hors champ de la TVA) ; commission 1,5 % = 291,60 HT + TVA 58,32 ; TTC 19 789,92. Part patronale 60 %, part salariale 40 % retenue sur la paie (7 776,00).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/10/2026 | AC | 6478 | Autres charges sociales – titres-restaurant | TRS-551 valeur faciale [ETB061] | 19 440,00 | |
| 05/10/2026 | AC | 6228 | Rémunérations d'intermédiaires – divers | TRS-551 commission émetteur | 291,60 | |
| 05/10/2026 | AC | 44566 | TVA déductible sur ABS | TRS-551 TVA commission | 58,32 | |
| 05/10/2026 | AC | 401000 | Fournisseurs – Titres Repas Services (F00500) | TRS-551 | | 19 789,92 |
| 31/10/2026 | PAIE | 421 | Personnel – rémunérations dues | Retenue part salariale TR oct. | 7 776,00 | |
| 31/10/2026 | PAIE | 6478 | Autres charges sociales – titres-restaurant | Retenue part salariale TR oct. | | 7 776,00 |
| | | | | **Total** | **27 565,92** | **27 565,92** |

> **Piège / contrôle :** pas de TVA sur la valeur faciale (seule la commission de l'émetteur en supporte). Charge nette en 6478 = 11 664,00 (part patronale). Exonération de la part patronale dans une limite par titre et sous condition de participation entre 50 % et 60 % (*valeurs à vérifier chaque année*).

#### P11 — Mutuelle et prévoyance de branche : appel de régularisation annuel
**Contexte :** les cotisations courantes passent dans P01/P02 ; l'organisme assureur adresse en fin d'année un appel de régularisation (effectifs et assiettes réels).
**Pièce :** appel de régularisation du 10/12/2026 : 1 260,00 à la charge de l'employeur.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 10/12/2026 | OD | 6452 | Cotisations aux mutuelles | Régularisation annuelle prévoyance 2026 [ETB061] | 1 260,00 | |
| 10/12/2026 | OD | 4372 | Mutuelle / prévoyance | Régularisation annuelle 2026 | | 1 260,00 |
| | | | | **Total** | **1 260,00** | **1 260,00** |

> **Piège / contrôle :** les **dispenses d'adhésion** de salariés (temps partiels avec mutuelle du conjoint, CDD courts…) doivent être justifiées par écrit : sans justificatif, l'exonération sociale de la part patronale peut être remise en cause lors d'un contrôle URSSAF.

#### P12 — Contribution à la formation professionnelle et taxe d'apprentissage (via la DSN)
**Contexte :** contributions recouvrées mensuellement par l'URSSAF avec la DSN.
**Pièce :** DSN d'octobre : masse salariale soumise 247 300,00 ; taxe d'apprentissage 0,59 % = 1 459,07 ; contribution formation 1 % = 2 473,00 (*taux à vérifier*).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | PAIE | 6312 | Taxe d'apprentissage | Taxe d'apprentissage oct. [ETB061] | 1 459,07 | |
| 31/10/2026 | PAIE | 6333 | Participation à la formation professionnelle continue | Contribution formation oct. [ETB061] | 2 473,00 | |
| 31/10/2026 | PAIE | 431 | Sécurité sociale (URSSAF) | CUFPA oct. | | 3 932,07 |
| | | | | **Total** | **3 932,07** | **3 932,07** |

> **Piège / contrôle :** le solde de la taxe d'apprentissage et la **contribution supplémentaire à l'apprentissage** (entreprises d'au moins 250 salariés n'atteignant pas le quota d'alternants) sont déclarés annuellement : provisionnez-les à la clôture. Ces contributions ne sont pas des « cotisations sociales » : elles relèvent des comptes 631/633.

### 3.5 Cycle immobilisations

#### I01 — Acquisition d'un véhicule utilitaire
**Contexte :** achat (et non LLD) d'un fourgon pour une équipe de remise en état.
**Pièce :** facture Garage Riviera n° GR-2026-411 du 05/10/2026 : véhicule 24 000,00 HT ; TVA 4 800,00 ; certificat d'immatriculation 330,00 (taxe, sans TVA) ; TTC 29 130,00 ; mise en service le 05/10/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/10/2026 | ACI | 2182 | Matériel de transport | GR-411 fourgon AB-123-CD (5 ans) [ETB083] | 24 330,00 | |
| 05/10/2026 | ACI | 44562 | TVA déductible sur immobilisations | GR-411 | 4 800,00 | |
| 05/10/2026 | ACI | 404000 | Fournisseurs d'immobilisations – Garage Riviera | GR-411 | | 29 130,00 |
| | | | | **Total** | **29 130,00** | **29 130,00** |

> **Piège / contrôle :** les frais d'acquisition (immatriculation) peuvent être incorporés au coût ou passés en charge : c'est une **option** globale du groupe (appliquée ici : incorporation). Un VU ouvre droit à déduction ; un VP non.

#### I02 — Dotation mensuelle aux amortissements
**Contexte :** clôture mensuelle de novembre.
**Pièce :** tableau des amortissements : autolaveuse A05 structure 7 500,00 / 60 mois = 125,00 ; batteries 1 400,00 / 36 mois = 38,89 ; fourgon I01 24 330,00 / 60 mois = 405,50. Total 569,39.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | OD | 68112 | Dotations aux amortissements des immobilisations corporelles | Dotation nov. [ETB062/ETB083] | 569,39 | |
| 30/11/2026 | OD | 28154 | Amortissements du matériel de nettoyage | Dotation nov. autolaveuse + batteries | | 163,89 |
| 30/11/2026 | OD | 28182 | Amortissements du matériel de transport | Dotation nov. fourgon | | 405,50 |
| | | | | **Total** | **569,39** | **569,39** |

> **Piège / contrôle :** le prorata temporis démarre à la **mise en service** (21/10 pour l'autolaveuse, 05/10 pour le fourgon : la dotation d'octobre est donc partielle). Contrôle : total des amortissements au fichier des immobilisations = solde des comptes 28.

#### I03 — Cession d'un véhicule utilitaire
**Contexte :** revente d'un ancien fourgon.
**Pièce :** facture de vente FV26-09-0001 du 30/09/2026 : 6 500,00 HT + TVA 1 300,00 = 7 800,00 ; fiche d'immobilisation : acquis le 01/03/2022 pour 22 000,00, linéaire 5 ans ; amortissements au 31/12/2025 : 16 866,67 ; dotation 2026 jusqu'à la cession (9 mois) : 3 300,00 ; cumul 20 166,67 ; VNC 1 833,33.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 68112 | Dotations aux amortissements des immobilisations corporelles | Complément dotation 01-09/2026 fourgon EF-456-GH | 3 300,00 | |
| 30/09/2026 | OD | 28182 | Amortissements du matériel de transport | Complément dotation fourgon EF-456-GH | | 3 300,00 |
| 30/09/2026 | OD | 28182 | Amortissements du matériel de transport | Sortie amortissements cumulés | 20 166,67 | |
| 30/09/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | VNC fourgon EF-456-GH | 1 833,33 | |
| 30/09/2026 | OD | 2182 | Matériel de transport | Sortie fourgon EF-456-GH | | 22 000,00 |
| 30/09/2026 | VT | 462 | Créances sur cessions d'immobilisations | FV26-09-0001 cession fourgon | 7 800,00 | |
| 30/09/2026 | VT | 775 | Produits des cessions d'éléments d'actif | FV26-09-0001 | | 6 500,00 |
| 30/09/2026 | VT | 44571 | TVA collectée | FV26-09-0001 (livraison de bien) | | 1 300,00 |
| | | | | **Total** | **33 100,00** | **33 100,00** |

> **Piège / contrôle :** 675 / 775 restent les comptes de cession dans le PCG 2025 ; plus-value = 6 500,00 − 1 833,33 = 4 666,67. Une cession de bien est une **livraison** : TVA exigible à la livraison (44571), pas « en attente ». Vente d'un véhicule dont la TVA avait été déduite → cession **taxable**. Pensez à la déclaration de cession du véhicule (certificat).

#### I04 — Mise au rebut d'une autolaveuse
**Contexte :** autolaveuse détruite (moteur hors d'usage, réparation non rentable).
**Pièce :** procès-verbal de mise au rebut du 30/06/2026 signé par le chef d'établissement + bordereau de la filière de recyclage ; acquise le 01/10/2022 pour 7 200,00, linéaire 5 ans ; amortissements au 31/12/2025 : 4 680,00 ; dotation 2026 (6 mois) : 720,00 ; VNC 1 800,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/06/2026 | OD | 68112 | Dotations aux amortissements des immobilisations corporelles | Complément dotation 01-06/2026 autolaveuse n° S-2291 | 720,00 | |
| 30/06/2026 | OD | 28154 | Amortissements du matériel de nettoyage | Complément dotation n° S-2291 | | 720,00 |
| 30/06/2026 | OD | 28154 | Amortissements du matériel de nettoyage | Sortie amortissements n° S-2291 | 5 400,00 | |
| 30/06/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés | VNC autolaveuse rebutée n° S-2291 | 1 800,00 | |
| 30/06/2026 | OD | 2154 | Matériel de nettoyage | Sortie autolaveuse n° S-2291 | | 7 200,00 |
| | | | | **Total** | **7 920,00** | **7 920,00** |

> **Piège / contrôle :** pas de régularisation de TVA pour un bien **détruit** dont la destruction est **justifiée** (PV, bordereau de recyclage) : d'où l'importance de la pièce. Si une indemnité d'assurance est perçue, elle est comptabilisée en produit (*compte selon la nomenclature 2025 du PCG*).

#### I05 — Subvention d'investissement (véhicule électrique)
**Contexte :** la Région subventionne l'achat d'un VU électrique (35 000,00 HT, mis en service le 01/07/2026, amorti sur 5 ans).
**Pièce :** arrêté d'attribution du 20/06/2026 : 6 000,00 ; versement le 15/09/2026. Reprise 2026 : 6 000,00 / 5 × 6 / 12 = 600,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 20/06/2026 | OD | 441 | État et collectivités – subventions à recevoir | Arrêté Région VU électrique | 6 000,00 | |
| 20/06/2026 | OD | 131 | Subventions d'équipement | Subvention Région VU électrique | | 6 000,00 |
| 15/09/2026 | BQ1 | 5121 | Banque A | Versement subvention Région | 6 000,00 | |
| 15/09/2026 | BQ1 | 441 | État et collectivités – subventions à recevoir | Versement subvention Région | | 6 000,00 |
| 31/12/2026 | OD | 139 | Subventions inscrites au compte de résultat | Quote-part 2026 | 600,00 | |
| 31/12/2026 | OD | 747 | Quote-part des subventions d'investissement virée au résultat | Quote-part 2026 [ETB061] | | 600,00 |
| | | | | **Total** | **12 600,00** | **12 600,00** |

> **Piège / contrôle :** **747** depuis le PCG 2025 (et non plus 777). La reprise suit le **rythme de l'amortissement** du bien financé. Option possible : imposer immédiatement la subvention en produit (rare).

#### I06 — Logiciel acquis et matériel informatique
**Contexte :** licence perpétuelle d'un logiciel de gestion des interventions et renouvellement de 10 PC d'établissement.
**Pièce :** facture Éditeur Planif'Net n° PN-2026-77 du 16/11/2026 : licence + paramétrage 12 000,00 HT + TVA 2 400,00 ; facture Info Azur n° IA-9912 du 18/11/2026 : 10 PC × 850,00 = 8 500,00 HT + TVA 1 700,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 16/11/2026 | ACI | 205 | Concessions, brevets, licences, logiciels | PN-2026-77 licence + paramétrage [SIEGE] | 12 000,00 | |
| 16/11/2026 | ACI | 44562 | TVA déductible sur immobilisations | PN-2026-77 | 2 400,00 | |
| 16/11/2026 | ACI | 404000 | Fournisseurs d'immobilisations – Planif'Net | PN-2026-77 | | 14 400,00 |
| 18/11/2026 | ACI | 2183 | Matériel de bureau et informatique | IA-9912 10 PC (3 ans) [ETB061] | 8 500,00 | |
| 18/11/2026 | ACI | 44562 | TVA déductible sur immobilisations | IA-9912 | 1 700,00 | |
| 18/11/2026 | ACI | 404000 | Fournisseurs d'immobilisations – Info Azur | IA-9912 | | 10 200,00 |
| | | | | **Total** | **24 600,00** | **24 600,00** |

> **Piège / contrôle :** le **paramétrage** nécessaire à la mise en service s'immobilise avec la licence ; la **formation** des utilisateurs et la **maintenance** sont des charges. Un SaaS (A13) n'est jamais en 205. Les PC à 850,00 HT dépassent le seuil de 500,00 HT : immobilisation.

### 3.6 Cycle intra-groupe

> 💡 **Règle d'or :** toute écriture intragroupe a un **miroir** dans l'autre société. Chaque mois, les deux comptables (ou le service de consolidation) **réconcilient** les soldes : 4112 de la mère = 4011 de la filiale ; 4511 de la mère (créance sur filiale) = 4511 de la filiale (dette envers la mère), etc. Un écart non expliqué bloque la consolidation.

#### G01 — Management fees du siège : chez la filiale
**Contexte :** la convention de prestations de services du groupe prévoit des frais de siège égaux à 3 % du chiffre d'affaires trimestriel (direction générale, finance, paie, achats, juridique, informatique).
**Pièce :** facture SIÈGE SERVICES n° SS-2026-T3-014 du 30/09/2026 : CA T3 de la filiale 4 850 000,00 × 3 % = 145 500,00 HT ; TVA 29 100,00 (option débits) ; TTC 174 600,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 628800 | Management fees groupe | SS-2026-T3-014 frais de siège T3 [SIEGE] | 145 500,00 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | SS-2026-T3-014 (option débits) | 29 100,00 | |
| 30/09/2026 | AC | 4011 | Fournisseurs groupe – Siège Services | SS-2026-T3-014 | | 174 600,00 |
| | | | | **Total** | **174 600,00** | **174 600,00** |

#### G02 — Management fees du siège : chez la mère

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | VT | 4112 | Clients groupe – Propreté Azur | SS-2026-T3-014 | 174 600,00 | |
| 30/09/2026 | VT | 706800 | Prestations intragroupe – management fees | Frais de siège T3 Propreté Azur | | 145 500,00 |
| 30/09/2026 | VT | 44571 | TVA collectée | SS-2026-T3-014 (option débits) | | 29 100,00 |
| | | | | **Total** | **174 600,00** | **174 600,00** |

> **Piège / contrôle (G01-G02) :** les management fees doivent correspondre à des **services réels** et documentés (convention, clés de répartition, prix de pleine concurrence) : à défaut, l'administration fiscale peut refuser la déduction chez la filiale. Si le groupe a constitué un **groupe TVA** (assujetti unique), les flux internes sont **hors champ** : pas de TVA facturée. Réconciliation : 4011 filiale = 4112 mère.

#### G03a — Refacturation de frais de personnel : chez la mère (qui prête)
**Contexte :** un contrôleur de gestion salarié de la mère est mis à disposition de la filiale à mi-temps ; refacturation au coût réel (salaire + charges), sans marge.
**Pièce :** facture SS-2026-10-022 du 31/10/2026 : 12 000,00 HT ; TVA 2 400,00 ; TTC 14 400,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | VT | 4112 | Clients groupe – Propreté Azur | SS-2026-10-022 | 14 400,00 | |
| 31/10/2026 | VT | 7084 | Mise à disposition de personnel facturée | MAD contrôleur de gestion oct. | | 12 000,00 |
| 31/10/2026 | VT | 44571 | TVA collectée | SS-2026-10-022 | | 2 400,00 |
| | | | | **Total** | **14 400,00** | **14 400,00** |

#### G03b — Refacturation de frais de personnel : chez la filiale (qui bénéficie)

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | AC | 6214 | Personnel détaché ou prêté à l'entreprise | SS-2026-10-022 MAD contrôleur [SIEGE] | 12 000,00 | |
| 31/10/2026 | AC | 44566 | TVA déductible sur ABS | SS-2026-10-022 | 2 400,00 | |
| 31/10/2026 | AC | 4011 | Fournisseurs groupe – Siège Services | SS-2026-10-022 | | 14 400,00 |
| | | | | **Total** | **14 400,00** | **14 400,00** |

> **Piège / contrôle (G03) :** chez la mère, la refacturation est un **produit** (7084), pas une diminution de 641 ; chez la filiale, c'est une charge **externe** (6214), pas une charge de personnel (le salarié n'est pas dans sa paie). La mise à disposition **à but non lucratif** suppose une refacturation au coût exact (salaire, charges, frais professionnels).

#### G04a — Intérêts de la convention de trésorerie : chez la filiale (emprunteuse)
**Contexte :** la filiale a été en moyenne débitrice de 500 000,00 sur la convention de cash pooling au 3e trimestre.
**Pièce :** relevé d'intérêts de la trésorerie groupe du 30/09/2026 : 500 000,00 × 3,95 % × 92 / 365 = 4 978,08 (taux retenu dans la limite du taux fiscalement déductible — *valeur à vérifier*). Non soumis à la TVA.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | ODG | 6615 | Intérêts des comptes courants | Intérêts cash pooling T3 | 4 978,08 | |
| 30/09/2026 | ODG | 4511 | Groupe – compte courant cash pooling | Intérêts cash pooling T3 | | 4 978,08 |
| | | | | **Total** | **4 978,08** | **4 978,08** |

#### G04b — Intérêts de la convention de trésorerie : chez la mère (prêteuse)

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | ODG | 4511 | Groupe – compte courant Propreté Azur | Intérêts cash pooling T3 | 4 978,08 | |
| 30/09/2026 | ODG | 768 | Autres produits financiers – intérêts groupe | Intérêts cash pooling T3 Propreté Azur | | 4 978,08 |
| | | | | **Total** | **4 978,08** | **4 978,08** |

> **Piège / contrôle (G04) :** les intérêts servis à une société liée ne sont déductibles que dans la limite d'un **taux maximum** (taux moyen publié ou taux de marché démontré) et sous réserve des règles de limitation des charges financières : la fraction excédentaire est **réintégrée** extra-comptablement. Opération financière exonérée de TVA.

#### G05a — Dividendes : chez la filiale (affectation du résultat 2025)
**Contexte :** l'associé unique (la mère) approuve les comptes 2025 et décide une distribution ; la réserve légale a déjà atteint 10 % du capital.
**Pièce :** décision de l'associé unique du 30/04/2026 : résultat 1 250 000,00 ; dividende 800 000,00 ; solde en autres réserves 450 000,00 ; paiement le 31/05/2026 par le compte de cash pooling.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/04/2026 | OD | 120 | Résultat de l'exercice (bénéfice) | Affectation résultat 2025 | 1 250 000,00 | |
| 30/04/2026 | OD | 1068 | Autres réserves | Affectation résultat 2025 | | 450 000,00 |
| 30/04/2026 | OD | 457 | Associés – dividendes à payer | Dividende 2025 Siège Services | | 800 000,00 |
| 31/05/2026 | ODG | 457 | Associés – dividendes à payer | Paiement dividende 2025 | 800 000,00 | |
| 31/05/2026 | ODG | 4511 | Groupe – compte courant cash pooling | Paiement dividende 2025 | | 800 000,00 |
| | | | | **Total** | **2 050 000,00** | **2 050 000,00** |

#### G05b — Dividendes : chez la mère (régime mère-fille)

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/04/2026 | ODG | 4511 | Groupe – compte courant Propreté Azur | Dividende 2025 décidé | 800 000,00 | |
| 30/04/2026 | ODG | 7611 | Revenus des titres de participation | Dividende 2025 Propreté Azur | | 800 000,00 |
| | | | | **Total** | **800 000,00** | **800 000,00** |

> **Piège / contrôle (G05) :** chez la mère, le produit est constaté à la **date de la décision** de distribution. Le **régime mère-fille** exonère le dividende, sauf une **quote-part de frais et charges** (5 %, réduite à 1 % pour les dividendes reçus d'une filiale membre du même groupe d'intégration fiscale depuis plus d'un exercice — *conditions à vérifier*) : retraitement **extra-comptable** (déduction puis réintégration de la quote-part), aucune écriture comptable spécifique. Pas de prélèvement à la source entre sociétés françaises éligibles.

#### G06 — IS en intégration fiscale : chez la filiale
**Contexte :** convention d'intégration « de neutralité » : la filiale verse à la mère l'IS qu'elle aurait payé si elle n'était pas intégrée (acomptes puis solde), au lieu de le payer au Trésor.
**Pièce :** convention d'intégration fiscale ; versements d'acomptes à la mère : 4 × 80 000,00 = 320 000,00 (débités sur le compte courant) ; IS théorique 2026 : 1 400 000,00 × 25 % = 350 000,00 (pas de contribution sociale : IS inférieur à l'abattement de 763 000,00).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/12/2026 | ODG | 4512 | Groupe – compte courant intégration fiscale | Cumul acomptes IS 2026 versés à la mère | 320 000,00 | |
| 15/12/2026 | ODG | 4511 | Groupe – compte courant cash pooling | Cumul acomptes IS 2026 versés à la mère | | 320 000,00 |
| 31/12/2026 | OD | 695 | Impôts sur les bénéfices | IS 2026 dû à la mère (convention) | 350 000,00 | |
| 31/12/2026 | OD | 4512 | Groupe – compte courant intégration fiscale | IS 2026 dû à la mère | | 350 000,00 |
| | | | | **Total** | **670 000,00** | **670 000,00** |

> **Piège / contrôle :** en intégration, la filiale n'a **pas** de compte 444 actif : sa dette d'IS est envers **la mère** (451). Solde dû à la mère au 31/12 : 30 000,00. Le crédit d'impôt et les réintégrations de la filiale sont calculés comme si elle était imposée seule (selon la convention).

#### G07 — IS en intégration fiscale : chez la mère (tête de groupe)
**Pièce :** IS du groupe sur le résultat d'ensemble : 6 200 000,00 × 25 % = 1 550 000,00 ; contribution sociale 3,3 % × (1 550 000,00 − 763 000,00) = 25 971,00 ; contributions dues par les filiales intégrées selon les conventions : 1 720 000,00 (dont la filiale : 350 000,00).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 695 | Impôts sur les bénéfices | IS du groupe intégré 2026 | 1 550 000,00 | |
| 31/12/2026 | OD | 695 | Impôts sur les bénéfices – contribution sociale | Contribution sociale 3,3 % groupe | 25 971,00 | |
| 31/12/2026 | OD | 444 | État – impôt sur les bénéfices | IS + contribution sociale groupe 2026 | | 1 575 971,00 |
| 31/12/2026 | OD | 4512 | Groupe – comptes courants intégration fiscale (filiales) | IS dû par les filiales intégrées | 1 720 000,00 | |
| 31/12/2026 | OD | 698 | Intégration fiscale – produits (6989) | Contributions des filiales 2026 | | 1 720 000,00 |
| | | | | **Total** | **3 295 971,00** | **3 295 971,00** |

> **Piège / contrôle :** la mère est **seule redevable** de l'IS du groupe (444) ; le compte **698** enregistre l'économie ou la charge d'intégration (ici, les contributions des filiales). La contribution sociale peut être logée dans un sous-compte de 695 ou en 696 selon le plan groupe. Les **grandes entreprises** (CA ≥ 1 Md€) peuvent être redevables d'une **contribution exceptionnelle sur les bénéfices** (*périmètre, taux et prorogation à vérifier*) et suivent des règles renforcées pour le dernier acompte.

#### G08 — Facture groupe non parvenue à la clôture (réconciliation intragroupe)
**Contexte :** la mère a émis le 31/12 sa facture de prestations informatiques de décembre ; la filiale ne l'a pas reçue au moment de clôturer.
**Pièce :** état de réconciliation intragroupe envoyé par la consolidation : écart 11 760,00 (facture SS-2026-12-031 : 9 800,00 HT + TVA 1 960,00).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 628800 | Management fees groupe | FNP SS-2026-12-031 informatique déc. [SIEGE] | 9 800,00 | |
| 31/12/2026 | OD | 44586 | TVA sur factures non parvenues | FNP SS-2026-12-031 | 1 960,00 | |
| 31/12/2026 | OD | 4081 | Fournisseurs groupe – factures non parvenues | FNP SS-2026-12-031 | | 11 760,00 |
| | | | | **Total** | **11 760,00** | **11 760,00** |

> **Piège / contrôle :** la consolidation exige que la charge chez la filiale = le produit chez la mère **sur la même période**. Les écarts de réconciliation proviennent presque toujours de **décalages** (facture en transit, avoir non saisi, taux de change) : documentez-les dans l'état de réconciliation.

### 3.7 TVA

#### TV01 — Liquidation de la CA3 mensuelle (TVA à payer)
**Contexte :** déclaration de TVA d'octobre 2026 de la filiale (montants agrégés du mois).
**Pièce :** balance des comptes de TVA au 31/10/2026 après bascules d'encaissements : 44571 312 480,00 C ; 4452 (44521 + 44522 + 44523) 3 252,22 C ; 44562 18 640,00 D ; 44566 96 315,40 D ; 445662 3 252,22 D. TVA nette due : 197 524,60, payée par télérèglement le 20/11/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 44571 | TVA collectée | Liquidation CA3 oct. 2026 | 312 480,00 | |
| 31/10/2026 | OD | 4452 | TVA due intracommunautaire et autoliquidations | Liquidation CA3 oct. 2026 | 3 252,22 | |
| 31/10/2026 | OD | 44562 | TVA déductible sur immobilisations | Liquidation CA3 oct. 2026 | | 18 640,00 |
| 31/10/2026 | OD | 44566 | TVA déductible sur ABS | Liquidation CA3 oct. 2026 | | 96 315,40 |
| 31/10/2026 | OD | 445662 | TVA déductible – autoliquidation | Liquidation CA3 oct. 2026 | | 3 252,22 |
| 31/10/2026 | OD | 44551 | TVA à décaisser | CA3 oct. 2026 | | 197 524,60 |
| 20/11/2026 | BQ1 | 44551 | TVA à décaisser | Télérèglement CA3 oct. 2026 | 197 524,60 | |
| 20/11/2026 | BQ1 | 5121 | Banque A | Télérèglement CA3 oct. 2026 | | 197 524,60 |
| | | | | **Total** | **513 256,82** | **513 256,82** |

> **Piège / contrôle :** **44574 n'est jamais liquidé** (TVA non exigible) ; 44586 / 44587 non plus. Avant de liquider : contrôlez que **4452 = 445662** (autoliquidations symétriques), que les bascules d'encaissements sont faites et que le **CA déclaré** (base HT des encaissements) est cohérent avec les mouvements créditeurs des 411. La CA3 se déclare **en euros** : l'écart d'arrondi éventuel se solde en 658 / 758.

#### TV02 — CA3 créditrice (mois de forts investissements)
**Pièce :** balance des comptes de TVA de novembre : 44571 82 400,00 C ; 4452 2 100,00 C ; 44562 96 000,00 D ; 44566 41 300,00 D ; 445662 2 100,00 D → crédit de 54 900,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | OD | 44571 | TVA collectée | Liquidation CA3 nov. 2026 | 82 400,00 | |
| 30/11/2026 | OD | 4452 | TVA due intracommunautaire et autoliquidations | Liquidation CA3 nov. 2026 | 2 100,00 | |
| 30/11/2026 | OD | 44567 | Crédit de TVA à reporter | Crédit CA3 nov. 2026 | 54 900,00 | |
| 30/11/2026 | OD | 44562 | TVA déductible sur immobilisations | Liquidation CA3 nov. 2026 | | 96 000,00 |
| 30/11/2026 | OD | 44566 | TVA déductible sur ABS | Liquidation CA3 nov. 2026 | | 41 300,00 |
| 30/11/2026 | OD | 445662 | TVA déductible – autoliquidation | Liquidation CA3 nov. 2026 | | 2 100,00 |
| | | | | **Total** | **139 400,00** | **139 400,00** |

#### TV03 — Demande de remboursement du crédit de TVA et encaissement
**Pièce :** demande de remboursement (formulaire n° 3519) déposée avec la CA3 de novembre ; remboursement reçu le 18/01/2027.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/12/2026 | OD | 44583 | Remboursement de taxes sur le CA demandé | Demande remboursement crédit nov. | 54 900,00 | |
| 15/12/2026 | OD | 44567 | Crédit de TVA à reporter | Demande remboursement crédit nov. | | 54 900,00 |
| 18/01/2027 | BQ1 | 5121 | Banque A | Remboursement crédit TVA | 54 900,00 | |
| 18/01/2027 | BQ1 | 44583 | Remboursement de taxes sur le CA demandé | Remboursement crédit TVA | | 54 900,00 |
| | | | | **Total** | **109 800,00** | **109 800,00** |

> **Piège / contrôle (TV02-TV03) :** sans demande de remboursement, le crédit s'impute sur la CA3 suivante (44567 diminue lors de la liquidation suivante). Une demande de remboursement déclenche souvent un **contrôle** : préparez les factures d'immobilisations du mois.

#### TV04 — Régularisation de la TVA sur encaissements (rapprochement 44574 / encours clients)
**Contexte :** contrôle mensuel : le solde de 44574 doit égaler la TVA incluse dans l'encours clients « prestations » non encaissé.
**Pièce :** balance âgée clients au 30/11/2026 : encours TTC prestations 2 459 160,00 → TVA incluse 2 459 160,00 / 6 = 409 860,00 ; solde 44574 : 412 300,00 ; écart 2 440,00 expliqué par des encaissements de novembre non lettrés (liste jointe).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | OD | 44574 | TVA collectée en attente (encaissements) | Régul. bascule encaissements non lettrés nov. | 2 440,00 | |
| 30/11/2026 | OD | 44571 | TVA collectée | Régul. bascule encaissements non lettrés nov. | | 2 440,00 |
| | | | | **Total** | **2 440,00** | **2 440,00** |

> **Piège / contrôle :** la cause racine est presque toujours un **lettrage manquant** : lettrez d'abord, la bascule suit. Excluez du calcul les créances **non soumises** (intérêts moratoires, débours), les factures en **option débits** et les cessions de biens. Un 44574 **inférieur** à la TVA de l'encours signale au contraire une TVA déclarée trop tôt.

### 3.8 Clôture (mensuelle et annuelle)

#### C01 — Charge constatée d'avance (assurance)
**Pièce :** prime A22 de 18 000,00 pour la période du 01/04/2026 au 31/03/2027 ; part 2027 : 18 000,00 × 3 / 12 = 4 500,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 486 | Charges constatées d'avance | CCA assurance flotte 01-03/2027 | 4 500,00 | |
| 31/12/2026 | OD | 616 | Primes d'assurance | CCA assurance flotte 01-03/2027 [SIEGE] | | 4 500,00 |
| | | | | **Total** | **4 500,00** | **4 500,00** |

#### C02 — Produit constaté d'avance (forfait de janvier facturé en décembre)
**Pièce :** facture FV26-12-0702 du 20/12/2026 : forfait janvier 2027 Résidences Horizon 16 800,00 HT.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 706100 | Prestations propreté forfait | PCA forfait janv. 2027 [ETB061/062/083] | 16 800,00 | |
| 31/12/2026 | OD | 487 | Produits constatés d'avance | PCA forfait janv. 2027 | | 16 800,00 |
| | | | | **Total** | **16 800,00** | **16 800,00** |

#### C03 — Factures non parvenues (sous-traitance et intérim de décembre)
**Pièce :** état des commandes réceptionnées non facturées au 31/12/2026 : sous-traitant 4 200,00 HT ; intérim 3 150,00 HT (relevés d'heures signés) ; TVA 1 470,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 611 | Sous-traitance générale | FNP Net'Sous-Traitance déc. [ETB061] | 4 200,00 | |
| 31/12/2026 | OD | 6211 | Personnel intérimaire | FNP Intérim Côte déc. [ETB062] | 3 150,00 | |
| 31/12/2026 | OD | 44586 | TVA sur factures non parvenues | FNP déc. | 1 470,00 | |
| 31/12/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP déc. | | 8 820,00 |
| | | | | **Total** | **8 820,00** | **8 820,00** |

#### C04 — Facture à établir (révision de prix connue non facturée)
**Pièce :** indice de révision publié le 20/12/2026 ; révision due sur le 4e trimestre : 2 360,00 HT ; facture émise en janvier 2027.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 418 | Clients – produits non encore facturés | FAE révision prix T4 | 2 832,00 | |
| 31/12/2026 | OD | 706100 | Prestations propreté forfait | FAE révision prix T4 [ETB061] | | 2 360,00 |
| 31/12/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | FAE révision prix T4 | | 472,00 |
| | | | | **Total** | **2 832,00** | **2 832,00** |

#### C05 — Provisions pour litiges prud'homaux
**Contexte :** revue des dossiers prud'homaux avec le service juridique social.
**Pièce :** note de l'avocat du 15/12/2026 : nouveau dossier (contestation de licenciement) : risque estimé 9 000,00 ; dossier clos par une transaction réglée en 2026 : provision devenue sans objet 6 000,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Prud'hommes dossier 2026-07 [ETB062] | 9 000,00 | |
| 31/12/2026 | OD | 1511 | Provisions pour litiges | Prud'hommes dossier 2026-07 | | 9 000,00 |
| 31/12/2026 | OD | 1511 | Provisions pour litiges | Reprise dossier 2024-11 (transaction) | 6 000,00 | |
| 31/12/2026 | OD | 7815 | Reprises sur provisions d'exploitation | Reprise dossier 2024-11 [ETB061] | | 6 000,00 |
| | | | | **Total** | **15 000,00** | **15 000,00** |

> **Piège / contrôle :** provision **dossier par dossier**, sur la base d'une **estimation documentée** (avocat), en exploitation (pas en exceptionnel). La transaction réglée en 2026 a été passée en charge (6414 / 6226) : la reprise de 6 000,00 la compense, elle ne se « consomme » pas autrement.

#### C06 — Pénalités client : provision ou avoir à établir ?
**Contexte :** deux situations au 31/12 : (a) audit qualité défavorable sur le marché du CH Valmont, pénalités **probables** mais non encore chiffrées par le client (estimation 7 800,00) ; (b) réfaction de prix **notifiée et chiffrée** sur un autre contrat : 2 400,00 HT, avoir non émis.
**Pièce :** rapport d'audit du 12/12/2026 ; courrier de notification de réfaction du 22/12/2026.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Pénalités probables CH Valmont [ETB061] | 7 800,00 | |
| 31/12/2026 | OD | 1518 | Autres provisions pour risques | Pénalités probables CH Valmont | | 7 800,00 |
| 31/12/2026 | OD | 7096 | RRR accordés sur prestations de services | Avoir à établir réfaction T4 [ETB062] | 2 400,00 | |
| 31/12/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | TVA avoir à établir | 480,00 | |
| 31/12/2026 | OD | 4198 | RRR à accorder et autres avoirs à établir | Avoir à établir réfaction T4 | | 2 880,00 |
| | | | | **Total** | **10 680,00** | **10 680,00** |

> **Piège / contrôle :** **montant certain → dette** (avoir à établir, 4198) ; **montant incertain → provision** (1518). Une pénalité de nature indemnitaire probable se provisionne aussi en 6815 ; une fois notifiée, elle passe en 658 (V06b).

#### C07 — Dépréciation des créances clients
**Pièce :** revue de la balance âgée avec le credit manager : nouvelles dépréciations individuelles 14 250,00 (HT des créances à risque) ; créance dépréciée en 2025 finalement encaissée : reprise 3 100,00.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciations clients 2026 (état joint) | 14 250,00 | |
| 31/12/2026 | OD | 491 | Dépréciations des comptes clients | Dépréciations clients 2026 | | 14 250,00 |
| 31/12/2026 | OD | 491 | Dépréciations des comptes clients | Reprise créance Logis Est encaissée | 3 100,00 | |
| 31/12/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise créance Logis Est | | 3 100,00 |
| | | | | **Total** | **17 350,00** | **17 350,00** |

> **Piège / contrôle :** une dépréciation **forfaitaire** (« 50 % de tout ce qui a plus de 6 mois ») est admise en comptabilité si elle est justifiée par l'historique, mais **non déductible** fiscalement : seule la dépréciation individualisée l'est. Les créances sur **clients publics** sont rarement irrécouvrables : un retard n'est pas un risque de non-paiement.

#### C08 — IS et acomptes (société du groupe hors périmètre d'intégration)
**Pièce :** acomptes versés en 2026 : 4 × 95 000,00 = 380 000,00 ; IS 2026 calculé : 412 000,00 ; solde 32 000,00 à verser avec le relevé de solde.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/12/2026 | BQ1 | 444 | État – impôt sur les bénéfices | Cumul acomptes IS 2026 (03, 06, 09, 12) | 380 000,00 | |
| 15/12/2026 | BQ1 | 5121 | Banque A | Cumul acomptes IS 2026 | | 380 000,00 |
| 31/12/2026 | OD | 695 | Impôts sur les bénéfices | IS 2026 | 412 000,00 | |
| 31/12/2026 | OD | 444 | État – impôt sur les bénéfices | IS 2026 | | 412 000,00 |
| | | | | **Total** | **792 000,00** | **792 000,00** |

> **Piège / contrôle :** le 444 créditeur de 32 000,00 = solde à payer. Pour les grandes entreprises, le **dernier acompte** est calculé à partir d'une **estimation** du résultat de l'exercice en cours (*seuils et pourcentages à vérifier*) : une sous-estimation entraîne majoration. En **clôture mensuelle**, beaucoup de groupes passent un IS estimé chaque mois (taux effectif prévisionnel).

#### C09 — CFE et CVAE
**Pièce :** avis de CFE 2026 par établissement (Nice 4 820,00 ; Cannes 3 140,00 ; Toulon 2 610,00 = 10 570,00), payés le 15/12/2026 ; CVAE 2026 estimée 18 400,00, acomptes versés 17 200,00 → solde à payer 1 200,00 (*taux de CVAE 2026 à vérifier*).

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | OD | 63511 | Contribution économique territoriale | CFE 2026 Nice [ETB061] | 4 820,00 | |
| 30/11/2026 | OD | 63511 | Contribution économique territoriale | CFE 2026 Cannes [ETB062] | 3 140,00 | |
| 30/11/2026 | OD | 63511 | Contribution économique territoriale | CFE 2026 Toulon [ETB083] | 2 610,00 | |
| 30/11/2026 | OD | 447 | Autres impôts, taxes et versements assimilés | Avis CFE 2026 | | 10 570,00 |
| 15/12/2026 | BQ1 | 447 | Autres impôts, taxes et versements assimilés | Paiement CFE 2026 | 10 570,00 | |
| 15/12/2026 | BQ1 | 5121 | Banque A | Paiement CFE 2026 | | 10 570,00 |
| 31/12/2026 | OD | 63511 | Contribution économique territoriale | Solde CVAE 2026 estimé [SIEGE] | 1 200,00 | |
| 31/12/2026 | OD | 4486 | État – charges à payer | Solde CVAE 2026 | | 1 200,00 |
| | | | | **Total** | **22 340,00** | **22 340,00** |

> **Piège / contrôle :** la CFE est due **par établissement** (lieu des biens passibles de taxe foncière) : vérifiez que chaque agence ouverte ou fermée dans l'année est correctement déclarée. La CVAE est en voie de suppression progressive : vérifiez le taux applicable à l'exercice.

#### C10 — Intérêts courus sur compte courant groupe (convention de trésorerie)
**Pièce :** convention : intérêts débités trimestriellement à terme échu le 10 du mois suivant ; position moyenne débitrice T4 : 450 000,00 × 3,95 % × 92 / 365 = 4 480,27.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | ODG | 6615 | Intérêts des comptes courants | Intérêts courus cash pooling T4 | 4 480,27 | |
| 31/12/2026 | ODG | 4518 | Groupe – intérêts courus | Intérêts courus cash pooling T4 | | 4 480,27 |
| | | | | **Total** | **4 480,27** | **4 480,27** |

#### C11 — Extournes au 1er jour de la période suivante
**Contexte :** les régularisations C01 à C04 sont contre-passées le 01/01/2027 (le même mécanisme s'applique chaque 1er du mois en clôture mensuelle) ; les vraies factures s'imputeront normalement.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/01/2027 | EXT | 408 | Fournisseurs – factures non parvenues | Extourne FNP déc. | 8 820,00 | |
| 01/01/2027 | EXT | 611 | Sous-traitance générale | Extourne FNP déc. [ETB061] | | 4 200,00 |
| 01/01/2027 | EXT | 6211 | Personnel intérimaire | Extourne FNP déc. [ETB062] | | 3 150,00 |
| 01/01/2027 | EXT | 44586 | TVA sur factures non parvenues | Extourne FNP déc. | | 1 470,00 |
| 01/01/2027 | EXT | 706100 | Prestations propreté forfait | Extourne FAE révision T4 [ETB061] | 2 360,00 | |
| 01/01/2027 | EXT | 44587 | Taxes sur le CA sur factures à établir | Extourne FAE révision T4 | 472,00 | |
| 01/01/2027 | EXT | 418 | Clients – produits non encore facturés | Extourne FAE révision T4 | | 2 832,00 |
| 01/01/2027 | EXT | 487 | Produits constatés d'avance | Extourne PCA forfait janv. | 16 800,00 | |
| 01/01/2027 | EXT | 706100 | Prestations propreté forfait | Extourne PCA forfait janv. | | 16 800,00 |
| 01/01/2027 | EXT | 616 | Primes d'assurance | Extourne CCA assurance [SIEGE] | 4 500,00 | |
| 01/01/2027 | EXT | 486 | Charges constatées d'avance | Extourne CCA assurance | | 4 500,00 |
| | | | | **Total** | **32 952,00** | **32 952,00** |

> **Piège / contrôle :** sans extourne, la facture réelle de janvier **double** la charge. Si l'ERP gère l'extourne automatiquement, vérifiez qu'elle a bien été générée (et pas deux fois). Ne pas extourner les provisions (C05-C07), qui s'ajustent par dotation / reprise.

#### C12 — Prime d'objectif annuelle à payer et charges sociales
**Pièce :** accord d'intéressement managérial : primes d'objectifs 2026 des chefs d'établissement estimées 42 000,00, versées en mars 2027 ; charges patronales retenues 45 %.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6413 | Primes et gratifications | Primes d'objectifs 2026 à payer | 42 000,00 | |
| 31/12/2026 | OD | 4286 | Personnel – autres charges à payer | Primes d'objectifs 2026 | | 42 000,00 |
| 31/12/2026 | OD | 6451 | Cotisations à l'URSSAF | Charges sur primes d'objectifs (45 %) | 18 900,00 | |
| 31/12/2026 | OD | 4386 | Organismes sociaux – autres charges à payer | Charges sur primes d'objectifs | | 18 900,00 |
| | | | | **Total** | **60 900,00** | **60 900,00** |

#### C13 — Taxes annuelles sur les véhicules de tourisme
**Pièce :** état de la flotte : 2 VP utilisés en 2026 ; taxes annuelles (CO2 et polluants) calculées : 3 860,00 (*barèmes à vérifier*) ; déclaration et paiement en janvier 2027.

| Date | Journal | Compte | Intitulé | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 63514 | Taxes sur les véhicules | Taxes annuelles VP 2026 [SIEGE] | 3 860,00 | |
| 31/12/2026 | OD | 4486 | État – charges à payer | Taxes annuelles VP 2026 | | 3 860,00 |
| | | | | **Total** | **3 860,00** | **3 860,00** |

> **Piège / contrôle :** les VP en **LLD** utilisés par l'entreprise sont taxables comme les véhicules achetés ; les **VU** ne le sont pas. Les véhicules personnels des salariés remboursés en indemnités kilométriques peuvent aussi entrer dans l'assiette au-delà d'un seuil (*à vérifier*). Taxes non déductibles du résultat fiscal (*à vérifier*).

---

## 4. Tableau récapitulatif : « Je reconnais l'opération → je passe l'écriture »

*(HT = montant hors taxes ; TVA ded. = 44566, ou 44562 pour une immobilisation ; « en attente » = 44574 côté ventes, 445668 côté achats de services non payés.)*

| # | Opération reconnue | Débit | Crédit | Réf. |
|---|---|---|---|---|
| 1 | Facture de prestation, TVA sur encaissements | 411 (TTC) | 706x (HT) + 44574 (TVA) | V01 |
| 2 | Encaissement d'une facture de prestation | 512 / 44574 | 411 / 44571 | V02 |
| 3 | Facture de prestation avec option débits | 411 | 706x + 44571 | V03 |
| 4 | Révision de prix rétroactive | 411 | 706100 + 44574 | V05 |
| 5 | Avoir de réfaction de prix (facture non encaissée) | 7096 + 44574 | 411 | V06a |
| 6 | Pénalité indemnitaire retenue par le client | 512 + 658 | 411 (puis bascule de toute la TVA) | V06b |
| 7 | Avoir commercial (facture déjà encaissée) | 7096 + 44571 | 411 | V07 |
| 8 | Acompte client reçu (services) | 512 | 4191 (HT) + 44571 | V08a |
| 9 | Facture finale avec imputation de l'acompte | 411 + 4191 | 706x + 44574 (sur le solde) | V08b |
| 10 | Facture marché public (Chorus Pro) | 4111 | 706x + 44574 | V09 |
| 11 | Intérêts moratoires + indemnité 40 € | 4111 | 7631 + 758 | V10 |
| 12 | Client en procédure collective | 416 / 6817 | 411 / 491 (sur HT) | V11 |
| 13 | Créance irrécouvrable | 654 + 44571 (option débits) ou 44574 (encaissements) | 416 ; puis 491 → 7817 | V12 |
| 14 | Prestation réalisée non facturée | 418 | 706x + 44587 | V13, C04 |
| 15 | Prestation facturée d'avance | 706x | 487 | V14, C02 |
| 16 | Refacturation de consommables | 411 | 706400 + 44574 | V15 |
| 17 | Cession de créances au factor | 4671 | 411 | V16 |
| 18 | Financement par le factor | 512 + 6225 + 44566 + 6618 + 4672 | 4671 | V17 |
| 19 | LCR client : acceptation / remise / encaissement | 413 / 5113 / 512 + 627 | 411 / 413 / 5113 | V18 |
| 20 | Escompte accordé | 665 + 44574 | 411 | V19 |
| 21 | Écart de règlement débiteur / créditeur | 658 | 758 | V20 |
| 22 | Achat de produits d'entretien | 6022 + 44566 | 401 | A01 |
| 23 | Inventaire du dépôt de consommables | 6032 / 3222 | 3222 / 6032 | A02 |
| 24 | EPI, petit matériel < 500 € HT | 6063 + 44566 | 401 | A03, A04 |
| 25 | Autolaveuse, monobrosse, PC | 2154 / 2183 + 44562 | 404 | A05, I06 |
| 26 | Sous-traitant de propreté (fournisseur aux encaissements) | 611 + 445668 | 401 ; au paiement 44566 / 445668 | A06 |
| 27 | Sous-traitant de fin de chantier (autoliquidation BTP) | 611 ; au paiement 445662 | 401 ; au paiement 44523 | A07 |
| 28 | Intérim (option débits) | 6211 + 44566 | 401 | A08 |
| 29 | LLD : VU / VP | 6135 + 6155 + 44566 (VU seulement) | 401 | A09 |
| 30 | Carburant VU / VP | 6061 + 44566 (100 % / 80 %) | 401 | A10 |
| 31 | Service acheté dans l'UE ou hors UE | 6xxx + 445662 | 401 + 44522 | A11, A13 |
| 32 | Achat de biens dans l'UE | 6022 + 445662 | 401 + 44521 | A12 |
| 33 | Perte / gain de change sur dette fournisseur | 656 | 756 | A13 |
| 34 | Avoir fournisseur (retour) | 401 | 6022 + 44566 | A14 |
| 35 | Acompte sur immobilisation / sur service | 238 / 4091 + 44566 | 512 | A15 |
| 36 | Facture non parvenue | 6xxx + 44586 | 408 | A16, C03 |
| 37 | Avoir à recevoir / RFA | 4098 | 6022 ou 6092 + 44586 | A17, A18 |
| 38 | Note de frais | 6251 / 6256 + 44566 (si déductible) | 421800 | A19 |
| 39 | Cadeaux clients (≤ seuil) | 6234 + 44566 | 401 | A20 |
| 40 | Loyer d'agence / dépôt de garantie | 6132 + 614 + 44566 / 275 | 401 / 512 | A21 |
| 41 | Prime d'assurance | 616 | 401 | A22 |
| 42 | Facture en litige (quantité non livrée) | 2154 + 44562 + 4098 | 404 (paiement bloqué) | A23 |
| 43 | Paiement avec escompte obtenu | 401 | 512 + 765 + 44566 | A24 |
| 44 | Retenue de garantie sous-traitant | 401 | 512 + 4017 | A25 |
| 45 | Frais bancaires / agios | 627 (+ 44566 si facture) / 6615 | 512 | T01, T07 |
| 46 | Virement interne | 58 puis 512 (B) | 512 (A) puis 58 | T02 |
| 47 | Cash pooling : remontée / redescente | 4511 / 512 | 512 / 4511 | T03 |
| 48 | Emprunt reçu / échéance | 512 + 627 / 164 + 6611 | 164 / 512 | T04, T05 |
| 49 | Intérêts courus | 6611 / 6615 | 1688 / 4518 | T06, C10 |
| 50 | Virement non identifié / identifié | 512 / 471 | 471 / 411 | T07, T08 |
| 51 | LCR impayée | 411 + 44571 | 512 + 44574 | T07 |
| 52 | Journal de paie (part salariale) | 6411 / 6412 / 6413 / 6414 | 431, 437x, 4421, 425, 427, 421 | P01 |
| 53 | Charges patronales | 6451 / 6452 / 6453 | 431 / 437x | P02 |
| 54 | Acompte sur salaire | 425 | 512 | P04 |
| 55 | IJSS subrogées | 4387 | 641190 (jamais 791) | P05 |
| 56 | Provision congés payés | 6412 / 645x | 4282 / 4382 | P06 |
| 57 | Indemnité de licenciement | 6414 | 421 (+ 431, 437, 4421) | P07 |
| 58 | Reprise de personnel art. 7 (entrant) | rien de spécifique | — | P08 |
| 59 | Participation | 691 / 6458 | 4246 / 4386 | P09 |
| 60 | Titres-restaurant | 6478 + 6228 + 44566 ; retenue 421 | 401 ; 6478 | P10 |
| 61 | Formation / apprentissage (DSN) | 6312 / 6333 | 431 | P12 |
| 62 | Dotation aux amortissements | 68112 | 28xx | I02 |
| 63 | Cession d'immobilisation | 28xx + 675 / 462 | 2xxx / 775 + 44571 | I03 |
| 64 | Mise au rebut | 28xx + 675 | 2xxx | I04 |
| 65 | Subvention d'investissement | 441 → 512 ; 139 | 131 ; 747 | I05 |
| 66 | Management fees reçus (filiale) / émis (mère) | 628800 + 44566 / 4112 | 4011 / 706800 + 44571 | G01, G02 |
| 67 | Mise à disposition de personnel (filiale / mère) | 6214 + 44566 / 4112 | 4011 / 7084 + 44571 | G03 |
| 68 | Intérêts de convention de trésorerie (filiale / mère) | 6615 / 4511 | 4511 / 768 | G04 |
| 69 | Dividende (filiale / mère) | Filiale : 120 à la décision, 457 au paiement / mère : 4511 | Filiale : 1068 + 457, puis 4511 / mère : 7611 | G05 |
| 70 | IS intégré (filiale / mère) | 695 / 695 + 4512 | 4512 / 444 + 698 | G06, G07 |
| 71 | Liquidation CA3 à payer | 44571 + 4452 | 44562 + 44566 + 445662 + 44551 | TV01 |
| 72 | CA3 créditrice / remboursement | 44571 + 4452 + 44567 / 44583 | 4456x / 44567 | TV02, TV03 |
| 73 | Régularisation 44574 | 44574 | 44571 | TV04 |
| 74 | Charge constatée d'avance | 486 | 6xxx | C01 |
| 75 | Provision prud'hommes / pénalités probables | 6815 | 1511 / 1518 | C05, C06 |
| 76 | Avoir à établir | 7096 + 44587 | 4198 | C06 |
| 77 | Dépréciation clients | 6817 / 491 | 491 / 7817 | C07 |
| 78 | IS hors intégration | 444 (acomptes) / 695 | 512 / 444 | C08 |
| 79 | CFE / CVAE | 63511 | 447 / 4486 | C09 |
| 80 | Extournes du 1er du mois | sens inverse | sens inverse | C11 |
| 81 | Primes à payer + charges | 6413 / 6451 | 4286 / 4386 | C12 |
| 82 | Taxes annuelles véhicules | 63514 | 4486 | C13 |

---

## 5. Les 20 contrôles de comptes à faire chaque mois

Ce sont les contrôles qu'un responsable comptable attend d'une assistante autonome **avant** la remontée du reporting mensuel. En entretien, en citer cinq ou six avec la logique (« ce que je regarde / ce que ça révèle ») fait une forte impression.

| # | Contrôle | Ce que vous regardez | Ce que cela révèle / action |
|---|---|---|---|
| 1 | **Fournisseurs débiteurs** | Comptes 401 / 404 auxiliaires à solde débiteur | Double paiement, avoir non imputé, acompte non soldé, facture non saisie → demander le remboursement ou l'avoir, lettrer. |
| 2 | **Clients créditeurs** | Comptes 411 auxiliaires à solde créditeur | Double encaissement, avoir non imputé, règlement mal affecté → rembourser ou réimputer. |
| 3 | **Lettrage** des 401 et 411 | Taux de lettrage, écritures non lettrées de plus de 60 jours | Sans lettrage : balance âgée fausse, bascule de TVA non faite, relances inutiles. |
| 4 | **408 / 418 anciens** | FNP et FAE de plus de 3 mois | Facture jamais reçue (doublon de FNP ?), prestation jamais facturée (perte de chiffre d'affaires) → relancer ou annuler. |
| 5 | **4098 / 4198** | Avoirs à recevoir / à établir en suspens | Avoirs fournisseurs jamais obtenus (litiges A23), avoirs clients non émis. |
| 6 | **44574 vs encours clients** | Solde 44574 = TVA incluse dans l'encours « prestations » non encaissé | Écart = bascules non faites (TVA non déclarée) ou faites à tort → TV04. |
| 7 | **4452 = 445662** (par sous-compte) | Symétrie des autoliquidations (intracom, hors UE, BTP) | Une autoliquidation saisie d'un seul côté = TVA due non déclarée ou déduction sans TVA due. |
| 8 | **Rapprochement CA3 / comptabilité** | Lignes de la CA3 vs soldes des 445 ; 44551 / 44567 après liquidation | Une TVA collectée qui ne « tombe » pas = erreur de déclaration. 44586 / 44587 / 44574 jamais liquidés. |
| 9 | **421 soldé** | Net à payer après virements | Salaire non versé, RIB erroné, virement rejeté. |
| 10 | **431 / 437 / 4421 = DSN** | Soldes après prélèvements vs montants de la DSN | Écart de paramétrage paie / compta, cotisation non payée (majorations). |
| 11 | **425 et 427** | Acomptes non imputés, saisies non reversées | Acompte versé deux fois, saisie conservée à tort (responsabilité de l'employeur). |
| 12 | **4387 IJSS** | IJSS à recevoir de plus de 2 mois | Attestations de salaire non transmises : perte de trésorerie et de produit. |
| 13 | **Réconciliation intragroupe** | 4011 / 4112 / 4511 / 4512 / 4081 vs comptes miroirs des autres sociétés | Écarts bloquants pour la consolidation → G08. |
| 14 | **471 / 472 vides** | Comptes d'attente | Tout montant doit être identifié et reclassé avant clôture. |
| 15 | **58 virements internes à zéro** | Solde du compte 58 | Virement saisi d'un seul côté ou en double. |
| 16 | **Rapprochements bancaires** | Un état par compte bancaire, suspens datés | Suspens de plus d'un mois = erreur ou fraude potentielle ; contrôle des changements de RIB. |
| 17 | **4091 / 4191 / 238** | Acomptes versés et reçus | Acompte non imputé sur la facture finale (risque de double paiement ou de double facturation). |
| 18 | **Balance âgée clients + 416 / 491** | Créances > 90 jours, clients en procédure | Transfert en 416, déclaration de créance, dépréciation HT. Clients publics : statut Chorus Pro. |
| 19 | **Revue analytique** | Charges et produits par établissement / contrat vs mois précédent et budget | Imputation analytique erronée, facture oubliée, doublon (charge doublée), forfait non facturé. |
| 20 | **Cut-off et extournes** | FNP / FAE / CCA / PCA passées et **extournées** au 1er du mois suivant ; immobilisations vs comptes de charges (> 500 € HT) | Charges doublées faute d'extourne ; immobilisations passées en charges (ou l'inverse). |

> 💡 **Réflexe senior — la phrase à placer en entretien :** « Chaque fin de mois, avant de transmettre, je vérifie mes comptes de tiers dans les deux sens (fournisseurs débiteurs, clients créditeurs), mes comptes d'attente à zéro, mes FNP anciennes, la symétrie de mes comptes d'autoliquidation et le rapprochement 44574 / encours clients ; je documente chaque écart restant dans un fichier de justification. »

> ⚠️ **Erreur classique :** considérer la clôture mensuelle comme « une petite clôture ». Dans un groupe détenu en partie par un fonds d'investissement, le reporting mensuel alimente les **covenants bancaires** et le pilotage : une FNP oubliée en octobre fausse la marge d'un établissement et déclenche des questions de la direction. Le niveau d'exigence est le même qu'à la clôture annuelle, en plus rapide.

---

### Auto-évaluation express (à faire la veille de l'entretien)

- [ ] Je sais expliquer **pourquoi** la TVA d'une facture de propreté va en 44574 et quand elle passe en 44571.
- [ ] Je sais dire **quand** la TVA d'un sous-traitant est déductible (à la facture ou au paiement) et ce que change la mention « option pour les débits ».
- [ ] Je distingue nettoyage courant (TVA de droit commun) et nettoyage de fin de chantier en sous-traitance (autoliquidation BTP).
- [ ] Je sais traiter une facture **en litige** sans bloquer la clôture (comptabilisation, blocage du paiement, suivi, avoir).
- [ ] Je connais les comptes **PCG 2025** : pas de 791, pénalités en 658, cessions en 675 / 775, subvention en 747, change commercial en 656 / 756.
- [ ] Je sais expliquer la **reprise de personnel** (article 7) côté comptable : rien à passer chez l'entrant, solde des CP chez le sortant.
- [ ] Je sais décrire un **cash pooling**, des **management fees** et une **réconciliation intragroupe**.
- [ ] Je peux citer au moins **cinq** des 20 contrôles mensuels et ce qu'ils révèlent.

