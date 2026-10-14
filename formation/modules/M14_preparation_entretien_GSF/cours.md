# M14 — Cours : connaître GSF et sa comptabilité

*Module de préparation à l'entretien d'aide-comptable / assistante comptable au siège de GSF (Sophia Antipolis, Biot). Public : candidate avec 2 à 3 ans d'expérience. Référentiel au 09/10/2026 (PCG modifié par le règlement ANC n° 2022-06, sans comptes 79 ; facturation électronique en vigueur depuis le 01/09/2026).*

> **Avertissement de méthode.** Les faits sur GSF proviennent exclusivement de la fiche de recherche du module (sources publiques consultées le 09/10/2026). Tout ce qui concerne l'organisation **interne** de la comptabilité de GSF (ERP, calendrier de clôture, intégration fiscale, date de clôture, etc.) est une **déduction raisonnable de formateur**, signalée « *à vérifier* ». En entretien, présentez ces points comme des hypothèses (« j'imagine que… », « est-ce que… ? »), jamais comme des certitudes.

!!! tip "Vous avez environ 2 ans d'expérience ? Suivez ce parcours"
    Ce module va loin : certains sujets (intra-groupe, liasse, reprise du personnel) **ne sont pas attendus** d'une assistante comptable avec 2 ans d'expérience. Pour ne pas vous décourager :

    1. **Commencez par le module M15** (questions de comptabilité générale en entretien GSF) : c'est le socle que le recruteur testera en priorité.
    2. **Dans ce module M14, lisez d'abord** la Partie 1 (GSF en deux pages), la Partie 3 (circuit fournisseurs P2P) et les sections 5.1 à 5.3 (TVA).
    3. **Faites ces exercices en priorité** (★★☆) : E14-05 (3-way match), E14-06 (litige fournisseur), E14-07 (immobilisation ou charge), E14-09 (intérim et FNP), E14-12 (rapprochement bancaire), E14-13 (balance âgée), E14-14 (clôture mensuelle).
    4. **Les exercices ★★★ sont de l'approfondissement** (E14-03, E14-08, E14-11, E14-15 à E14-20) : utiles si vous avez le temps, mais on ne vous reprochera pas de ne pas les maîtriser en entretien.

!!! abstract "En clair — ce module en 5 idées"
    1. **GSF est un très grand groupe de nettoyage.** Environ 43 000 salariés, autour de 160 établissements, et une comptabilité centralisée au siège de Sophia Antipolis. Ce n'est pas une PME.
    2. **Beaucoup de sociétés, un seul siège.** Chaque société du groupe a sa propre comptabilité. Votre premier réflexe : vérifier sur quelle société vous saisissez. C'est la même logique, en beaucoup plus grand, que C10 Delta Invest et ses filiales au cabinet.
    3. **Le poste visé tourne autour des factures fournisseurs.** De la commande au paiement : on vérifie que la facture correspond à ce qui a été commandé et reçu, puis on paie dans les délais légaux.
    4. **La TVA a ses pièges dans la propreté.** Le nettoyage courant de bureaux se facture avec TVA. Le nettoyage de fin de chantier, fait en sous-traitance pour un constructeur comme C02 Bâtisseurs du Sud, se facture sans TVA : c'est le client qui la déclare (autoliquidation).
    5. **En entretien, montrez que vous comprenez la logique.** Vous ne connaissez pas leur logiciel ni leur organisation interne : présentez-les comme des hypothèses et posez des questions.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Centre de profit | Une unité qui suit son propre chiffre d'affaires et sa propre marge | Un établissement GSF de Lyon Est |
    | Analytique | Un code ajouté à chaque écriture pour savoir à quel établissement ou contrat elle se rapporte | Une facture de produits d'entretien imputée à « Lyon Est » |
    | Intercos (intra-groupe) | Les opérations entre deux sociétés du même groupe | Le siège refacture ses frais aux filiales régionales |
    | Consolidation | Additionner les comptes de toutes les sociétés du groupe comme s'il n'y en avait qu'une | Les comptes du groupe GSF |
    | ERP | Le grand logiciel de gestion qui regroupe compta, achats, ventes… | SAP, Oracle, Sage X3 |
    | P2P (Purchase-to-Pay) | Tout le circuit d'un achat, de la demande jusqu'au paiement | Commande de produits → réception → facture → paiement |
    | O2C (Order-to-Cash) | Tout le circuit d'une vente, du contrat jusqu'à l'encaissement | Contrat de nettoyage → facture mensuelle → encaissement |
    | Bon à payer (BAP) | L'accord donné par un responsable pour qu'une facture soit payée | Le chef d'établissement valide la facture d'intérim |
    | 3-way match | La vérification croisée commande / livraison / facture | 100 cartons commandés, 80 reçus, 100 facturés : on bloque |
    | Balance âgée | La liste des dettes fournisseurs classées par ancienneté | Les factures en retard de plus de 60 jours ressortent |
    | Plateforme agréée (PA) | Le service officiel par lequel passent les factures électroniques | Les factures fournisseurs de GSF arrivent par la PA |
    | Autoliquidation | Le client déclare lui-même la TVA à la place du fournisseur | Nettoyage de fin de chantier en sous-traitance |
    | Chorus Pro | Le site public où l'on dépose les factures destinées à l'État, aux hôpitaux… | Une facture pour un hôpital public |
    | Attestation de vigilance | Le document URSSAF qui prouve qu'un sous-traitant paie bien ses cotisations | À demander tous les six mois |
    | FNP | Une facture pas encore reçue mais dont la dépense concerne déjà le mois | Des produits livrés le 28, facturés le mois suivant |

---

## Partie 1 — GSF en deux pages

> 🟢 **En clair :** cette partie vous donne la carte d'identité de GSF : son histoire, sa taille, son organisation et ses clients. Le recruteur attend que vous sachiez en parler en deux minutes, avec trois chiffres clés, sans réciter.

### 1.1 Identité et histoire

| Élément | Ce qu'il faut retenir |
|---|---|
| Nom | GROUPE SERVICES FRANCE (GSF), marque « GSF Propreté & Services » |
| Création | **1963, à Paris**, par **Jean Louis Noisiez** (décédé en 2022) |
| Siège | **1625 route des Lucioles, Sophia Antipolis 2, 06410 Biot** — siège administratif à Sophia Antipolis **depuis 1978** |
| SIREN | 775 675 291 |
| Forme | **SAS à directoire** ; président du directoire : **Christophe Cognée**, dans le groupe depuis environ 35 ans, promu en interne |
| Actionnariat | Famille Noisiez + **TowerBrook Capital Partners** (fonds d'investissement transatlantique), **environ 51 % depuis 2022** (communiqué de mars 2022) |
| Rang | **N° 2 français de la propreté** |
| Fonctions support | Regroupées à **Sophia Antipolis** : comptabilité, finance, paie, achats, juridique, RH… |

### 1.2 Chiffres clés (groupe)

| Année | Chiffre d'affaires | Salariés | Établissements |
|---|---|---|---|
| 2015 | 740 M€ | 31 000 | 118 |
| 2021 | ≈ 1,1 Md€ | 41 100 | 141 |
| 2022 | 1,183 Md€ (dont 91 M€ à l'international) ; résultat net 51,4 M€ | 41 109 | 152 établissements, 29 filiales |
| 2023 | 1,272 Md€ | > 42 000 | 159 à 162 |
| 2024 | **1,386 Md€** | ≈ 43 000 | 162 |
| 2025 | Acquisition du **groupe Ithaque / Pénélope** (accueil, hospitalité, événementiel ; ≈ 4 000 salariés, 22 sites) → CA combiné ≈ **1,6 Md€** | ≈ 43 000 + ≈ 4 000 (total *à vérifier*) | — |

Autres chiffres à pouvoir citer : **96 % de fidélisation clients**, **150 nationalités** parmi les salariés, **≈ 78 à 80 % des chefs d'établissement issus de la promotion interne**.

> 💡 Réflexe senior : retenez **trois** chiffres seulement pour l'oral — « près de 1,4 milliard d'euros de CA en 2024, environ 43 000 salariés, autour de 160 établissements », plus l'acquisition d'Ithaque/Pénélope en 2025. Trop de chiffres récités donnent un effet « par cœur ».

### 1.3 Organisation

- Environ **160 établissements** en France : chaque établissement est un **centre de profit de proximité**, dirigé par un **chef d'établissement**.
- Les établissements sont **regroupés dans des sociétés régionales** (SAS filiales) : par exemple GSF Trévise (Paris), GSF Mercure (Lyon), GSF Saturne (Strasbourg), GSF Atlantis (Pessac), GSF Ariane (Nancy), GSF Auriga (Cholet), GSF Celtus, GSF Grande Arche (Rueil), GSF Energia (Biot)… Capital souvent ≈ 200 000 €, présidence assurée par une société du groupe, **commissaires aux comptes**.
- **International** : Royaume-Uni, Canada, États-Unis, Monaco (Espagne historiquement) ; membre du réseau européen ECS (European Customers Synergy).

### 1.4 Activités et clients

- **Propreté** : bureaux et tertiaire, commerces et centres commerciaux, ERP (établissements recevant du public), transports publics, **aéroports**, **santé** (hôpitaux, cliniques, salles propres, laboratoires pharmaceutiques), **agroalimentaire** (nettoyage industriel, décontamination des allergènes — brevet déposé en 2018), **industrie**, **nucléaire** (centrales, radioprotection).
- **Services associés (« soft FM »)** : logistique interne, manutention, gestion déléguée des déchets, 3D (dératisation, désinsectisation, désinfection), espaces verts, petite maintenance, **accueil**, conciergerie, courrier, événementiel (Pénélope).
- **Clients** : privés (historiquement Thomson, Galeries Lafayette) et **publics** via des **marchés publics** (hôpitaux, aéroports, transports).
- Outil client « **Optima** » (espace client, traçabilité des prestations).

### 1.5 Certifications et RSE

**MASE**, **QUALIANOR**, **EcoVadis Platinum** (top 1 %), **B Corp** (certification obtenue en octobre 2024, annoncée par communiqué en janvier 2025), adhérent au **Pacte mondial de l'ONU**, label **Relations fournisseurs et achats responsables**.

> 💡 Réflexe senior : le label « Relations fournisseurs et achats responsables » est **votre** argument d'aide-comptable fournisseurs. Un tel label implique notamment de **payer les fournisseurs dans les délais**. Phrase utile : « Le respect des délais de paiement, c'est aussi la traduction concrète du label achats responsables : la comptabilité fournisseurs y contribue directement. »

### 1.6 Ce qu'il faut savoir citer en entretien (fiche mémo)

1. Fondée en 1963 par Jean Louis Noisiez ; siège administratif à Sophia Antipolis depuis 1978.
2. N° 2 français de la propreté ; ≈ 1,4 Md€ de CA en 2024 ; ≈ 43 000 salariés ; ≈ 160 établissements.
3. TowerBrook majoritaire (≈ 51 %) depuis 2022, aux côtés de la famille ; SAS à directoire présidé par Christophe Cognée.
4. Organisation décentralisée : établissements = centres de profit, regroupés en sociétés régionales ; fonctions support centralisées à Sophia.
5. Diversification : santé, agroalimentaire, nucléaire, aéroports ; services associés ; acquisition d'Ithaque/Pénélope en 2025 (accueil).
6. RSE forte : B Corp, EcoVadis Platinum, label achats responsables ; forte promotion interne.

> ⚠️ Erreur classique : dire « GSF est une PME familiale ». C'est un **grand groupe** détenu majoritairement par un fonds d'investissement depuis 2022, même si l'ADN familial reste revendiqué. Autre erreur : confondre le siège administratif (Biot) et l'ancienne adresse parisienne (49 rue de Trévise, encore citée dans le rapport 2022).

---

## Partie 2 — Ce que cette organisation implique pour la comptabilité

> 🟢 **En clair :** un groupe avec des dizaines de sociétés et 160 établissements, cela veut dire : beaucoup de comptabilités en parallèle, un code analytique sur chaque écriture, des opérations entre sociétés du groupe à réconcilier, et une clôture chaque mois en quelques jours.

### 2.1 Multi-sociétés

Une vingtaine à une trentaine de sociétés (29 filiales en 2022) = **autant de comptabilités** (journaux, balances, liasses, déclarations de TVA, comptes annuels, mandats de CAC). Au siège, une même équipe traite souvent **plusieurs sociétés** dans le même ERP : le premier réflexe est de **vérifier la société** sur laquelle on saisit (code société), car une facture adressée à « GSF Mercure » ne doit pas être comptabilisée chez « GSF Atlantis ».

> ⚠️ Erreur classique : saisir une facture sur la mauvaise société parce que le fournisseur est commun à tout le groupe. Contrôlez la **dénomination et le SIREN du destinataire** (mention obligatoire de la facture électronique) avant la saisie.

### 2.2 Analytique : l'établissement, centre de profit

Chaque établissement suit sa marge. Toute charge ou tout produit doit donc porter un **axe analytique** (code établissement, voire code chantier / contrat / client). Une facture de produits d'entretien imputée au mauvais établissement fausse la marge d'un chef d'établissement — qui s'en apercevra et appellera la comptabilité.

| Axe analytique type | Exemple |
|---|---|
| Société | GSF Mercure |
| Établissement (centre de profit) | Lyon Est |
| Contrat / site client | Hôpital X – bâtiment B |
| Nature d'activité | Propreté / 3D / accueil |

### 2.3 Intra-groupe (« intercos »)

Flux typiques (*schémas probables, à vérifier*) :
- **Refacturation des frais de siège / management fees** (comptabilité, paie, informatique, achats centralisés) de la société tête vers les filiales ;
- **Convention de trésorerie / cash pooling** (comptes courants intra-groupe, compte 451 « Groupe » et sous-comptes) ;
- **Refacturations entre filiales** (personnel mis à disposition, sous-traitance entre établissements de sociétés différentes, matériel prêté).

Règle d'or : **ce que A comptabilise en charge, B doit le comptabiliser en produit, au même montant et sur la même période**. Chaque mois, on **réconcilie les soldes intra-groupe** (matrice des intercos) avant le reporting ; un écart non expliqué bloque la consolidation.

> 🟢 **En clair :** quand une société du groupe facture une autre société du groupe, les deux comptabilités doivent dire la même chose. Si l'une a enregistré 5 000 € et l'autre rien, il faut trouver pourquoi avant de faire les comptes du groupe.

### 2.4 Consolidation, CAC, reporting au fonds

- Un groupe détenu par un fonds d'investissement produit un **reporting mensuel** (CA, marge par établissement, EBITDA, BFR, trésorerie, DSO/DPO) et des **comptes consolidés** annuels (voire semestriels) audités.
- Les **commissaires aux comptes** interviennent dans les sociétés (fiche : CAC relevés dans les filiales). Pour l'aide-comptable : préparer les **justificatifs de solde**, les **confirmations fournisseurs/clients** (circularisation), les **rapprochements bancaires**, répondre aux demandes de pièces.
- Un fonds suit de près le **BFR** : le **DPO** (délai moyen de paiement fournisseurs) et le **DSO** (délai moyen de recouvrement clients) sont des indicateurs surveillés.

### 2.5 Clôtures mensuelles — calendrier type J+5 (*exemple pédagogique, à vérifier*)

> 🟢 **En clair :** dans un grand groupe, on « arrête » les comptes chaque mois, en cinq jours ouvrés environ. J-1 = la veille de la fin du mois ; J+5 = le 5e jour après. Chaque jour a ses tâches.

| Jour | Tâches de l'équipe | Rôle de l'aide-comptable fournisseurs |
|---|---|---|
| J-3 à J-1 | Pré-clôture : relance des bons à payer (BAP), réceptions non saisies | Relancer les valideurs, saisir toutes les factures reçues |
| J+1 | Relevés bancaires, rapprochements | Rapprochement bancaire, lettrage des paiements |
| J+2 | Cut-off : FNP, FAE, CCA, PCA | Liste des **réceptions non facturées** → FNP (408) ; avoirs à recevoir (4098) |
| J+3 | Paie et charges sociales, immobilisations, intercos | Réconciliation des comptes intra-groupe fournisseurs ; contrôle des immobilisations saisies |
| J+4 | Revue analytique, justification des comptes | Justification des comptes 401/408/4098, balance âgée, analyse des débiteurs fournisseurs |
| J+5 | Reporting groupe / consolidation | Commentaires d'écarts sur les postes fournisseurs |

> 💡 Réflexe senior : en clôture mensuelle on accepte des **estimations** (FNP sur la base des commandes réceptionnées), à condition qu'elles soient **documentées** et **extournées** le mois suivant.

### 2.6 L'ERP : inconnu, mais les compétences sont transférables

L'outil n'est pas communiqué publiquement (question à poser). Les grands groupes utilisent souvent SAP, Oracle, Sage X3, Microsoft Dynamics, Cegid… associés à une **solution de dématérialisation** (OCR, workflow de validation) et désormais à une **plateforme agréée (PA)** pour la facture électronique.

Ce qu'il faut savoir faire **quel que soit l'outil** :

| Compétence | Exemple de mots-clés si l'outil est SAP (pour information) |
|---|---|
| Créer/consulter un tiers fournisseur (sans modifier le RIB seule) | Fiche fournisseur (données de base) |
| Consulter une commande et une réception | Commande d'achat, entrée de marchandises |
| Saisir/contrôler une facture rapprochée d'une commande | Contrôle facture (rapprochement commande) |
| Saisir une facture hors commande | Saisie facture directe |
| Proposer un paiement / un fichier de virement | Programme de paiement |
| Lettrer / délettrer | Compensation |
| Éditer une balance âgée, un grand livre tiers | États de postes ouverts |
| Extraire vers Excel | Export de listes |

En entretien : « Je n'ai pas encore utilisé votre ERP, mais la logique est la même partout : référentiel tiers, rapprochement commande-réception-facture, workflow de validation, propositions de paiement, lettrage. Je me forme vite sur un nouvel outil — j'ai changé d'outil [à personnaliser] en X semaines. »

---

## Partie 3 — Le processus Purchase-to-Pay (P2P)

> 🟢 **En clair :** c'est le cœur du poste : le circuit d'un achat, de la demande jusqu'au paiement. À chaque étape, un contrôle évite de payer trop, deux fois ou à un fraudeur. Exemple : on ne paie que ce qui a été commandé **et** reçu.

### 3.1 Les étapes

| # | Étape | Acteur | Pièce / trace | Contrôle clé |
|---|---|---|---|---|
| 1 | **Demande d'achat** (DA) | Établissement | DA dans l'outil | Budget, besoin réel |
| 2 | **Bon de commande** (BC) | Achats / établissement habilité | BC numéroté | Fournisseur **référencé**, prix du **contrat-cadre** |
| 3 | **Réception** | Établissement | Bon de livraison, PV de réception, relevé d'heures (intérim) | Quantités, conformité |
| 4 | **Réception de la facture** | Comptabilité fournisseurs | Facture électronique via PA (depuis le 01/09/2026) | Mentions obligatoires, SIREN, doublon |
| 5 | **Rapprochement à 3 voies (3-way match)** | Comptabilité / outil | BC ↔ réception ↔ facture | Prix, quantités, tolérances |
| 6 | **Bon à payer (BAP)** | Valideur habilité (délégation) | Workflow | Pas de BAP par la personne qui a commandé **et** payé |
| 7 | **Paiement** | Trésorerie | Proposition de paiement, fichier de virements | Échéance, **RIB vérifié**, double signature |
| 8 | **Lettrage** | Comptabilité | Lettrage facture/règlement | Compte fournisseur soldé, pas de solde débiteur anormal |

### 3.2 Le 3-way match en pratique

- **Prix** : prix facturé = prix de la commande (ou du contrat-cadre) ; tolérance éventuelle (par ex. ± 2 % ou ± 50 € — *paramètre propre à chaque entreprise*).
- **Quantités** : quantité facturée ≤ quantité réceptionnée.
- **2-way match** (BC ↔ facture) pour les services sans réception physique (abonnements, loyers) ; **facture hors commande** pour certaines dépenses autorisées (énergie, télécoms, loyers) avec validation par le budgétaire.
- En cas d'écart : la facture est **bloquée** (blocage au paiement) et un **litige** est ouvert.

Écriture type à la saisie (facture de produits d'entretien, 1 000 € HT, TVA 20 %) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6022 | Fournitures consommables (produits d'entretien) — axe : établissement | 1 000,00 € | |
| 44566 | TVA déductible sur autres biens et services | 200,00 € | |
| 401 | Fournisseurs | | 1 200,00 € |

### 3.3 Les litiges fournisseurs

| Type de litige | Exemple | Traitement |
|---|---|---|
| **Écart de prix** | Prix facturé ≠ prix contrat-cadre | Blocage, demande d'avoir au fournisseur, information des Achats |
| **Écart de quantités** | 100 cartons facturés, 80 réceptionnés | Payer 80 ou bloquer, demander un avoir de 20 |
| **Doublon** | Même facture reçue via la PA et en PDF par e-mail ; ou même n° de facture saisi deux fois | Contrôle automatique n° facture + fournisseur + montant ; ne comptabiliser **que** la facture de la PA |
| **Facture sans commande** | Établissement qui achète en direct | Retour vers l'établissement, régularisation de la commande ou validation hors procédure par la hiérarchie |
| **Prestation non conforme** | Intérim facturé sur des heures non validées | Rapprochement avec les relevés d'heures validés, avoir |
| **RIB modifié / fraude** | « Notre banque a changé » reçu par e-mail | **Procédure anti-fraude** (cf. 3.8) |
| **Facture non conforme** | Mention manquante, mauvais destinataire, mauvaise société | Refus / rejet via la PA avec motif (statut de cycle de vie) |

### 3.4 Relances et balance âgée fournisseurs

- La **balance âgée** ventile les dettes par antériorité : non échues / échues 0-30 j / 31-60 j / 61-90 j / > 90 j.
- Elle sert à : prioriser les paiements, détecter les **litiges anciens**, repérer les **soldes débiteurs** (avoirs non imputés, acomptes, doublons de paiement → à récupérer), préparer le reporting **DPO**.
- Les fournisseurs relancent la comptabilité : il faut répondre vite, avec la **cause précise** (facture non reçue, en litige, en attente de BAP, programmée au paiement le…).

### 3.5 Délais de paiement LME et sanctions

- **Article L. 441-10 du Code de commerce** : délai convenu ≤ **60 jours à compter de la date d'émission de la facture** ou, si convenu, **45 jours fin de mois** ; à défaut de convention : 30 jours après la réception des marchandises ou l'exécution de la prestation.
- Pénalités de retard exigibles de plein droit (taux minimal : trois fois le taux d'intérêt légal ; à défaut de stipulation, taux BCE + 10 points) + **indemnité forfaitaire de 40 €** pour frais de recouvrement.
- **Contrôles de la DGCCRF** : amende administrative pouvant aller jusqu'à **2 M€ pour une personne morale** (doublée en cas de réitération), avec **publication** de la sanction (« name and shame ») — *montants à vérifier, texte : Code de commerce, L. 441-16*. Les grands groupes sont régulièrement cités dans ces publications.
- Les **commissaires aux comptes** attestent des délais de paiement dans le rapport de gestion (tableau des factures reçues et émises non réglées échues).

> 🟢 **En clair :** la loi limite le délai de paiement des fournisseurs : 60 jours après la date de la facture, ou 45 jours fin de mois si c'est prévu. Payer en retard coûte des pénalités et peut entraîner une amende publique.

> 💡 Réflexe senior : le retard de paiement n'est pas qu'un sujet fournisseur ; c'est un **risque d'amende et d'image**, contradictoire avec le label « achats responsables ». Une facture bloquée en litige doit être **documentée** (motif, date de contestation) pour justifier le retard.

### 3.6 Obligation de vigilance (sous-traitants et intérim)

- **Code du travail, L. 8222-1 et D. 8222-5** : pour tout contrat d'au moins **5 000 € HT**, le donneur d'ordre doit obtenir du cocontractant, **à la conclusion puis tous les six mois** jusqu'à la fin de l'exécution, l'**attestation de vigilance URSSAF** (et un extrait Kbis ou équivalent). L'authenticité de l'attestation se vérifie en ligne (code de sécurité).
- À défaut : **solidarité financière** du donneur d'ordre (impôts, cotisations, rémunérations) en cas de travail dissimulé du sous-traitant.
- Pour l'aide-comptable : ne pas mettre en paiement un sous-traitant dont l'attestation est **expirée** sans alerte (procédure interne à connaître) ; tenir un tableau de suivi des échéances.

> 🟢 **En clair :** avant de travailler avec un sous-traitant (pour 5 000 € HT ou plus), il faut lui demander tous les six mois un document de l'URSSAF prouvant qu'il est en règle. Sinon, si le sous-traitant fraude, l'entreprise peut devoir payer ses dettes à sa place.

### 3.7 Facture électronique : réception via PA depuis le 01/09/2026

- Depuis le **01/09/2026**, toutes les entreprises assujetties doivent pouvoir **recevoir** des factures électroniques ; les **grandes entreprises et ETI** (GSF en est une) doivent aussi les **émettre** et procéder à l'**e-reporting**. Les PME/TPE émettront au 01/09/2027.
- Les factures transitent par une **plateforme agréée (PA)** (anciennement PDP), dans un format structuré (Factur-X, UBL, CII).
- **Nouvelles mentions** à contrôler : **SIREN du client**, **adresse de livraison** si différente, **nature de l'opération** (livraison de biens / prestation de services / mixte), **option pour le paiement de la TVA d'après les débits** le cas échéant.
- **Statuts de cycle de vie** : certains sont obligatoires (notamment *déposée*, *rejetée*, *refusée*, *encaissée*) ; d'autres facultatifs (*approuvée*, *en litige*, *suspendue*…). Le refus d'une facture se fait **dans la PA** avec un motif, plus par simple e-mail.
- **Transition** : des fournisseurs PME qui ne sont pas encore tenus d'émettre en électronique jusqu'au 01/09/2027 peuvent encore envoyer du PDF — attention aux **doublons** si le même fournisseur envoie aussi par PA.

### 3.8 Fraude au changement de RIB — procédure

1. Aucune modification de RIB sur simple e-mail, même d'une adresse connue (compromission possible).
2. **Contre-appel** au fournisseur sur un **numéro déjà connu** (contrat, ancienne facture), jamais celui de l'e-mail.
3. Obtention d'un RIB **signé** + attestation bancaire ; **séparation des tâches** (la personne qui saisit les factures ne valide pas seule la modification du référentiel) ; double validation.
4. Contrôle des **premiers paiements** vers le nouveau RIB ; alerte en cas d'urgence inhabituelle ou de pression (« faux président »).

---

## Partie 4 — Le processus Order-to-Cash (O2C)

> 🟢 **En clair :** c'est le circuit inverse : facturer les clients de GSF et récupérer l'argent. Les clients publics (hôpitaux, aéroports) ont leurs propres règles : dépôt sur Chorus Pro et délais de paiement fixés par la loi.

### 4.1 Contrats et facturation

| Type | Caractéristiques | Point d'attention |
|---|---|---|
| **Forfait mensuel multi-sites** | Contrat pluriannuel, une facture par mois (parfois une par site) | Facturation automatique, révision de prix, ventilation analytique par établissement |
| **Prestations ponctuelles** | Vitrerie, remise en état, nettoyage après sinistre, travaux exceptionnels | Bon d'intervention signé, devis accepté, facturation rapide |
| **Révision de prix** | Indexation annuelle selon une formule contractuelle (indice de la propreté, coût de la main-d'œuvre) | Rappel de révision si l'indice est publié après la facturation |
| **Pénalités** | Pénalités qualité / retard prévues au contrat | Avoir ou compensation par le client — cf. 4.4 |

Écriture type (forfait mensuel 10 000 € HT, TVA sur les encaissements) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 411 | Clients | 12 000,00 € | |
| 706 | Prestations de services — axe : établissement / contrat | | 10 000,00 € |
| 44587 | TVA sur factures à encaisser | | 2 000,00 € |

À l'encaissement : 512 à 411 (12 000 €) puis 44587 à 44571 (2 000 €). Avec l'**option pour les débits**, la TVA est directement portée en 44571 à la facturation.

### 4.2 Marchés publics et Chorus Pro

- Les factures aux **acheteurs publics** (hôpitaux, collectivités, établissements publics) sont déposées sur **Chorus Pro**, avec le **numéro d'engagement** / bon de commande et le **code service** fournis par l'acheteur ; à défaut, rejet.
- **Délai global de paiement** : **30 jours** (État, collectivités) et **50 jours pour les établissements publics de santé** (*à vérifier*).
- Retard → **intérêts moratoires de plein droit** (taux BCE + 8 points — *à vérifier*) + **indemnité forfaitaire de 40 €** ; ils sont dus sans demande, mais il faut contrôler qu'ils ont bien été versés et les réclamer sinon.

Écriture des intérêts moratoires constatés : 411 (ou 4181) à **763** (revenus des créances — *subdivision selon la nomenclature 2025 du PCG*). Ils sont **hors champ de TVA** (indemnité).

### 4.3 Relances, créances douteuses, affacturage

- **Relances** graduées : J+5 après échéance (rappel courtois), J+15 (relance avec relevé), J+30 (mise en demeure), puis contentieux. Avec un client public : vérifier d'abord le statut Chorus Pro (facture rejetée ? en attente de service fait ?).
- **Créance douteuse** : transfert 411 → **416** ; dépréciation sur le **HT** : 6817 à 491. La TVA ne se récupère qu'en cas d'irrécouvrabilité certaine (procédure collective, jugement) et pour les prestations dont la TVA a été acquittée (débits) ou encaissée partiellement.
- **Affacturage** (*possible, non confirmé*) : cession des créances à un factor ; comptes de tiers dédiés (467 « Factor » ou sous-comptes 411 cédés), retenue de garantie, commission en charge financière/de service.

### 4.4 Pénalités facturées par le client

Deux traitements selon la **nature** :
- **Réfaction de prix** (prestation partiellement non rendue) → **avoir avec TVA**, réduction du chiffre d'affaires (709 « Rabais, remises et ristournes accordés » ou 706 directement).
- **Pénalité indemnitaire** (sanction d'un manquement, sans lien direct avec le prix) → **hors champ de TVA**, comptabilisée en charge **658** (*subdivision selon la nomenclature 2025 du PCG* — jamais en exceptionnel par défaut depuis le PCG 2025). Le client émet une **note de débit** (ou procède par compensation), pas un avoir avec TVA.

> 🟢 **En clair :** si le client réduit le prix parce que la prestation n'a pas été entièrement faite, c'est un avoir avec TVA. S'il inflige une amende pour un manquement, c'est une indemnité sans TVA, enregistrée en charge.

> ⚠️ Erreur classique : accepter un « avoir » client pour pénalité avec TVA alors qu'il s'agit d'une indemnité → TVA collectée à tort réduite.

---

## Partie 5 — La TVA d'une entreprise de propreté

> 🟢 **En clair :** GSF déclare sa TVA chaque mois. Pour les prestations de services, la TVA est due en principe quand le client paie, pas quand on facture. Le grand piège du secteur : le nettoyage de fin de chantier en sous-traitance, facturé sans TVA.

### 5.1 Régime

- **Réel normal**, déclaration **CA3 mensuelle** (formulaire 3310-CA3), **télédéclarée et télépayée**, à une date limite fixée par le calendrier fiscal (en général entre le 15 et le 24 du mois suivant selon l'entreprise — *à vérifier sur l'espace professionnel*).
- Taux normal **20 %** pour l'essentiel des prestations (taux en vigueur : 20 / 10 / 5,5 / 2,1 %).

### 5.2 Exigibilité des prestations de services

- Prestations de services : TVA exigible **à l'encaissement**, sauf **option pour les débits** (exigibilité à la facturation). Depuis la réforme, la mention « **option pour le paiement de la taxe d'après les débits** » doit figurer sur la facture le cas échéant.
- Conséquences pratiques en régime encaissements : suivre le compte **44587 « TVA sur factures à encaisser »** et ne collecter qu'aux encaissements ; c'est aussi la raison du statut obligatoire « **encaissée** » dans la PA.
- Côté **achats de services**, la TVA n'est **déductible** qu'au **paiement** du fournisseur (sauf fournisseur ayant opté pour les débits) → compte d'attente **44586 / 4458x « TVA déductible sur factures non parvenues ou à payer »** selon le plan de comptes.

### 5.3 Autoliquidation BTP : le corner case du nettoyage

- **Article 283, 2 nonies du CGI** : la TVA est autoliquidée par le **preneur** (donneur d'ordre) pour les **travaux de construction** (y compris réparation, nettoyage, entretien, transformation et démolition) **effectués par un sous-traitant** pour un preneur assujetti.
- Doctrine (BOFiP) : le **nettoyage courant** de locaux en exploitation n'est **pas** un travail immobilier → TVA de droit commun. En revanche, le **nettoyage lié à des travaux immobiliers** (nettoyage de fin de chantier, de livraison, réalisé en sous-traitance d'une entreprise de BTP) entre dans l'autoliquidation.
- Une décision du **Conseil d'État du 24/02/2026, n° 497507**, citée dans la fiche, porterait sur cette frontière — **référence et portée à vérifier** avant d'en parler en entretien.

> 🟢 **En clair :** nettoyer des bureaux tous les jours = TVA normale. Nettoyer un bâtiment en fin de travaux pour le compte d'un constructeur = facture sans TVA, et c'est le constructeur qui déclare la TVA. Le tableau ci-dessous reprend les cas.

| Situation | TVA |
|---|---|
| GSF nettoie les bureaux d'un client (contrat d'entretien) | Droit commun : GSF facture TVA 20 % |
| GSF réalise un nettoyage de fin de chantier **en sous-traitance** d'un constructeur | Autoliquidation : facture **HT** avec mention « Autoliquidation » ; le constructeur autoliquide |
| GSF réalise le nettoyage de fin de chantier **directement pour le maître d'ouvrage** (pas de sous-traitance) | Droit commun |
| GSF sous-traite à son tour un nettoyage de fin de chantier qu'elle réalise elle-même en sous-traitance | GSF autoliquide la TVA sur la facture de son sous-traitant |

Écriture chez le donneur d'ordre (sous-traitance autoliquidée, 5 000 € HT) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 611 | Sous-traitance générale | 5 000,00 € | |
| 401 | Fournisseurs | | 5 000,00 € |
| 44566 | TVA déductible sur autres biens et services | 1 000,00 € | |
| 4452 (ou 44571x dédié) | TVA due autoliquidée | | 1 000,00 € |

### 5.4 Autres sujets TVA du secteur

| Sujet | Règle |
|---|---|
| **Sous-traitance de nettoyage courant** | TVA de droit commun, déductible au paiement (service) |
| **Véhicules** | Voitures particulières : TVA **non déductible** sur l'achat/la LLD ; utilitaires (camionnettes d'intervention) : déductible. Carburants : déductibilité partielle ou totale selon le véhicule et le carburant (*pourcentages à vérifier*) |
| **Cadeaux** | TVA déductible seulement si valeur unitaire ≤ **73 € TTC** par bénéficiaire et par an (*valeur à vérifier chaque année*) |
| **Intra-groupe** | Les refacturations entre sociétés du groupe sont des opérations soumises à TVA (sauf **groupe TVA**) |
| **Groupe TVA** (art. 256 C CGI, depuis 2023) | Assujetti unique : opérations internes hors champ, une déclaration unique — *option de GSF inconnue, à vérifier* |
| **Crédit de TVA** | Report sur la déclaration suivante ou **demande de remboursement** (formulaire 3519) selon seuils (*à vérifier*) |
| **Immobilisations** | TVA sur immobilisation déclarée ligne distincte (ligne 19) |

### 5.5 Préparer la CA3 : méthode

1. **Clôturer les saisies** du mois (ventes, achats, encaissements, décaissements, OD).
2. **TVA collectée** : extraire les soldes 44571 (par taux) ; en régime encaissements, vérifier le passage 44587 → 44571 sur les encaissements du mois.
3. **Rapprochement CA / TVA collectée** : CA HT (comptes 70x) × taux = TVA théorique ; expliquer les écarts (encaissements ≠ facturation, opérations autoliquidées, exonérées, débours, avoirs).
4. **TVA déductible** : 44562 (immobilisations), 44566 (biens et services) ; contrôler qu'aucune TVA sur VP ou cadeaux > seuil n'y figure ; pour les services, que la TVA n'est déduite qu'après paiement.
5. **Autoliquidation** : vérifier la symétrie TVA due / TVA déductible.
6. **Report** du crédit antérieur.
7. **Remplir le formulaire** puis **contrôler** : solde du compte 44551 (TVA à décaisser) ou 44567 (crédit) = montant de la déclaration.
8. **Écriture de liquidation** (44571 et 4452 au débit ; 44562, 44566 au crédit ; solde en 44551 ou 44567).
9. **Archiver** : tableau de préparation, extraits, justificatif de télédéclaration.

Lignes principales du 3310-CA3 (*numérotation à vérifier sur le formulaire en vigueur*) :

| Ligne | Contenu |
|---|---|
| A1 | Ventes, prestations de services (base HT) |
| A2 | Autres opérations imposables |
| E1 / E2 | Exportations / autres opérations non imposables (ex. ventes en autoliquidation BTP chez le sous-traitant) |
| 08 / 9B / 09 | Bases et TVA au taux de 20 % / 10 % / 5,5 % |
| 16 | Total de la TVA brute due |
| 19 | TVA déductible sur immobilisations |
| 20 | TVA déductible sur autres biens et services |
| 22 | Report du crédit apparaissant ligne 27 de la précédente déclaration |
| 23 | Total TVA déductible |
| 25 / 28 | Crédit de TVA / TVA nette due |

La ligne exacte pour la base des **achats autoliquidés en sous-traitance BTP** est à vérifier sur la notice du formulaire en vigueur.

> ⚠️ Erreur classique : déclarer la TVA collectée sur la **facturation** du mois alors que l'entreprise est en régime des **encaissements** — ou l'inverse. Toujours savoir quel régime s'applique et vérifier les factures (mention « option débits »).

---

## Partie 6 — La fiscalité d'une grande entreprise

> 🟢 **En clair :** une grande entreprise paie l'impôt sur les sociétés au taux plein, avec des contributions en plus. Elle paie aussi une taxe locale (CFE) pour chacun de ses établissements. Votre rôle d'aide-comptable : fournir des comptes propres et justifiés pour préparer la liasse fiscale.

### 6.1 Impôt sur les sociétés

| Élément | Règle (exercice 2026) |
|---|---|
| Taux | **25 %** (le taux réduit de 15 % est réservé aux PME : CA < 10 M€ et détention ≥ 75 % par des personnes physiques — GSF n'y a pas droit) |
| Contribution sociale | **3,3 %** de l'IS excédant un abattement de 763 000 € (entreprises dont le CA ≥ 7,63 M€) |
| Contribution exceptionnelle grandes entreprises | Créée par la loi de finances pour 2025 pour les entreprises dont le CA ≥ **1 Md€** ; taux et prorogation pour 2026 — ***à vérifier*** (GSF, avec ≈ 1,4 Md€ de CA groupe, peut être concernée selon l'appréciation du seuil, notamment en intégration fiscale) |
| Acomptes | Quatre acomptes (15/03, 15/06, 15/09, 15/12 pour un exercice civil) ; pour un CA > **250 M€**, le **dernier acompte** est calculé sur une **estimation de l'IS de l'exercice en cours** (pourcentage croissant avec le CA — ***à vérifier***) ; solde au 15 du 4e mois suivant la clôture (15/05 pour une clôture au 31/12) |
| Intégration fiscale | Société mère détenant ≥ **95 %** de filiales → résultat d'ensemble, IS payé par la tête de groupe ; **convention d'intégration** fixant la charge d'impôt de chaque filiale — ***probable, à vérifier*** |
| Interlocuteur | Rattachement possible à la **DGE** (Direction des grandes entreprises) |

### 6.2 Impôts locaux

- **CFE** : due **par établissement** (commune par commune) → avec ≈ 160 établissements, beaucoup d'avis à contrôler, payer et répartir analytiquement (dégrèvements éventuels, plafonnement en fonction de la valeur ajoutée).
- **CVAE** : en voie de suppression progressive (calendrier repoussé par les lois de finances successives) — **taux 2026 à vérifier**. Acomptes en juin et septembre, déclaration 1330-CVAE.

### 6.3 Préparer la liasse fiscale (régime réel normal, 2050 à 2059)

| Tableau | Contenu |
|---|---|
| 2050 / 2051 | Bilan actif / passif |
| 2052 / 2053 | Compte de résultat (charges et produits — sans comptes 79 depuis le PCG 2025) |
| 2054 | Immobilisations (mouvements) |
| 2055 | Amortissements |
| 2056 | Provisions et dépréciations |
| 2057 | État des échéances des créances et des dettes |
| **2058-A** | **Détermination du résultat fiscal** : réintégrations (amendes et pénalités, taxes annuelles sur les véhicules de tourisme, amortissements excédentaires des VP, provisions non déductibles, charges non déductibles…) et déductions |
| **2058-B** | Déficits reportables, provisions non déductibles |
| 2058-C | Affectation du résultat |
| 2059-A à 2059-D | Plus/moins-values, réserve spéciale |
| 2059-F / 2059-G | Composition du capital, filiales et participations |
| Groupe | Tableaux spécifiques à l'intégration fiscale (2058-A-bis, 2058-ER, etc. — *à vérifier*) |

**Étapes** :
1. Balance définitive après écritures d'inventaire.
2. **Justification de chaque compte** (dossier de travail : relevés, lettrages, tableaux).
3. **Tableaux annexes** : variation des immobilisations, amortissements, provisions, échéancier créances/dettes.
4. **Analyse des charges non déductibles** : grand livre des comptes 658 (pénalités), 6234 (cadeaux), véhicules, amendes.
5. Remplissage via l'outil de liasse (souvent alimenté par la balance avec une **table de correspondance** comptes → cases).
6. **Contrôles de cohérence** : total actif = total passif, résultat comptable 2053 = résultat repris en 2058-A, capitaux propres N = N-1 + résultat − distributions.
7. Revue par le responsable / CAC ; télétransmission (EDI-TDFC).

**Rôle de l'aide-comptable** : fournir une **balance propre**, **justifier les comptes de tiers** (401, 408, 4098, 411, 418, 419), produire le **tableau des immobilisations**, lister les **charges à réintégrer**, préparer l'**état des échéances** (2057) et l'**état des délais de paiement**.

---

## Partie 7 — Le social dans la propreté (pour comptabiliser la paie)

> 🟢 **En clair :** le secteur a ses règles de paie : beaucoup de temps partiel, des primes spécifiques, et surtout la reprise des salariés quand un contrat de nettoyage change de prestataire. Pour la comptabilité, le contrôle clé est que la paie, la comptabilité et la DSN donnent les mêmes chiffres.

| Thème | Ce qu'il faut savoir |
|---|---|
| Convention collective | **Entreprises de propreté et services associés — IDCC 3043** |
| **Reprise du personnel** (annexe 7 / ancien article 7) | En cas de **changement de prestataire** sur un marché, l'**entreprise entrante** reprend les salariés affectés au marché qui remplissent les conditions (ancienneté d'affectation, présence — *conditions précises à vérifier*). Le contrat est transféré : l'entreprise **sortante** solde certains droits (notamment **congés payés acquis** — *à vérifier*), l'entrante reprend l'ancienneté |
| **Temps partiel** | Très fréquent (horaires décalés, tôt le matin / le soir) ; durée minimale conventionnelle inférieure à la règle légale de 24 h (*à vérifier*) ; avenants de complément d'heures |
| **Heures complémentaires** | Majorées (10 % puis 25 % au-delà de 1/10e de la durée contractuelle, règles conventionnelles à vérifier) |
| **Primes** | Panier, salissure, transport, ancienneté, 13e mois selon accords |
| **IJSS / subrogation** | L'employeur maintient le salaire et perçoit les IJSS : 4387 (organismes sociaux — produits à recevoir) à **641** (diminution de la charge) — **jamais de 791** depuis le PCG 2025 |
| **Accidents du travail** | Taux AT élevé dans le secteur → cotisation AT significative ; suivi des arrêts |
| **Intérim** | Charge externe (621 « Personnel extérieur ») ; contrôle des **relevés d'heures validés** avant BAP |
| **Provision congés payés** | 6412 / 4282 (dettes CP) et 645 / 4382 (charges sociales sur CP) — recalcul mensuel en reporting |
| **Participation** | Obligatoire (> 50 salariés) : charge 691 / dette 4246 (réserve spéciale de participation) — *numéros selon nomenclature 2025* |
| **Mutuelle / prévoyance de branche** | Charges patronales 645/647 ; dettes 437 |
| **DSN** | Des dizaines de milliers de salariés : le **rapprochement paie/comptabilité** (journal de paie ↔ 421, 431, 437 ↔ DSN) est un contrôle mensuel clé |

Écriture IJSS subrogées (1 200 € à recevoir) :

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 4387 | Organismes sociaux — produits à recevoir | 1 200,00 € | |
| 641 | Rémunérations du personnel | | 1 200,00 € |

À réception : 512 à 4387 (1 200 €).

---

## Partie 8 — Corner cases du secteur (20 cas)

> 🟢 **En clair :** voici 20 situations concrètes que l'on peut vous poser en entretien. Pour chacune, demandez-vous : de quelle opération s'agit-il ? Quelle règle s'applique ? Qui doit valider ?

| # | Situation | Analyse / bon réflexe |
|---|---|---|
| 1 | **Perte d'un marché et transfert de personnel** (annexe 7) | Fin de la facturation au terme du contrat ; salariés transférés à l'entrant ; soldes de tout compte partiels / CP à régler selon la convention (*à vérifier*) ; arrêter les **FAE** et revoir les FNP liés au site ; matériel sur site à récupérer ou céder |
| 2 | **Gain d'un marché avec reprise de personnel** | Reprise d'ancienneté : impact sur la provision CP et les primes ; dossiers paie à créer ; centre de coût analytique à créer avant la première facture |
| 3 | **Client hôpital public qui paie à 60 jours** | Le délai légal d’un établissement public de santé est de **50 jours** : au-delà, **intérêts moratoires** + 40 € dus de plein droit ; vérifier le statut Chorus Pro avant de relancer |
| 4 | **Facture d'autolaveuse 2 800 € HT** | Bien durable utilisé sur plusieurs exercices, au-delà du seuil de tolérance de 500 € HT → **immobilisation** (2154 « Matériel industriel »), amortie sur sa durée d'utilisation (≈ 5 ans à apprécier) ; TVA en 44562 |
| 5 | **Aspirateur à 180 € HT** | Sous le seuil de tolérance de 500 € HT → **charge** (6063 « Fournitures d'entretien et de petit équipement ») |
| 6 | **Sous-traitant sans attestation URSSAF à jour** (contrat ≥ 5 000 € HT) | Risque de **solidarité financière** ; ne pas payer sans alerte ; relancer, suivre l'échéance semestrielle |
| 7 | **Nettoyage de fin de chantier** en sous-traitance d'un constructeur | **Autoliquidation BTP** : facturer HT avec mention ; corner case du CE 24/02/2026 n° 497507 (*à vérifier*) |
| 8 | **Avoir client pour pénalité qualité** | Réfaction de prix (avoir avec TVA) **ou** indemnité hors champ (658, sans TVA) selon la clause |
| 9 | **Double facturation PA + PDF** | Seule la facture de la PA fait foi ; contrôle doublon (n°, fournisseur, montant, date) ; le PDF est classé comme copie |
| 10 | **Fraude au changement de RIB** | Contre-appel sur numéro connu, double validation, aucune urgence acceptée |
| 11 | **Intérim facturé sur heures non validées** | Rapprochement avec relevés signés par le chef d'établissement ; blocage du BAP ; avoir |
| 12 | **Facture sans bon de commande** d'un chef d'établissement | Ne pas saisir « pour arranger » sans validation ; renvoyer vers la procédure (commande de régularisation ou validation hiérarchique), imputer analytiquement |
| 13 | **Fournisseur facturant au mauvais SIREN / à la mauvaise société** | Refus via la PA (statut *refusée*, motif) ; demande de refacturation à la bonne entité |
| 14 | **Révision de prix calculée sur un indice publié tardivement** | Facturation au prix N-1 puis **facture complémentaire** de rappel ; en clôture, **FAE** (418) estimée |
| 15 | **Acheteur public qui rejette la facture Chorus Pro** (n° d'engagement manquant) | La facture n'a pas été « reçue » : le délai de paiement ne court pas ; redéposer immédiatement |
| 16 | **Matériel de nettoyage sinistré, indemnité d'assurance** | Indemnité en produit (selon nature, **pas de 791**) ; sortie de l'immobilisation (675 / 775 restent pour les cessions) |
| 17 | **Solde débiteur sur un compte fournisseur** | Avoir non imputé, doublon de paiement ou acompte : demander le remboursement ou imputer ; reclasser en créance à l'inventaire (4091/4098) |
| 18 | **Refacturation intra-groupe non comptabilisée en symétrique** | Écart dans la matrice des intercos ; identifier la facture manquante, régulariser avant le reporting |
| 19 | **Facture d'un fournisseur PME reçue en PDF en octobre 2026** | Admis jusqu'au 01/09/2027 pour l'émetteur PME ; GSF doit malgré tout la traiter (et la recevoir via PA si l'émetteur l'y dépose) |
| 20 | **Pénalité de retard réclamée par un fournisseur** | Due de plein droit si le retard est avéré (L. 441-10) ; analyser la cause (litige documenté ?) ; charge financière/658 selon nature, pas d'exceptionnel |

> 💡 Réflexe senior : pour chaque corner case, raisonnez en trois temps : **nature de l'opération** (quoi ?), **règle** (comptable, fiscale, sociale), **contrôle interne** (qui valide, quelle trace ?). C'est exactement ce que le recruteur veut entendre.

---

## Partie 9 — Checklist « la veille de l'entretien »

**Connaître GSF**
- [ ] Je cite sans hésiter : 1963, Jean Louis Noisiez, n° 2 de la propreté, ≈ 1,4 Md€ (2024), ≈ 43 000 salariés, ≈ 160 établissements, TowerBrook depuis 2022, Ithaque/Pénélope 2025.
- [ ] Je sais expliquer l'organisation : établissements = centres de profit, sociétés régionales, siège à Sophia.
- [ ] Je connais 2 certifications RSE (B Corp, EcoVadis Platinum) et le label achats responsables.

**Technique**
- [ ] Je sais dérouler le P2P en 8 étapes et expliquer le 3-way match.
- [ ] Je connais les délais LME (60 j date de facture / 45 j fin de mois) et l'indemnité de 40 €.
- [ ] Je sais expliquer encaissements vs débits et l'autoliquidation BTP (nettoyage courant ≠ fin de chantier).
- [ ] Je sais ce qu'est un FNP, une CCA, une FAE, un avoir à recevoir, et les comptes associés.
- [ ] Je connais la facture électronique : PA, réception obligatoire depuis le 01/09/2026, émission GE, statuts.
- [ ] Je sais comptabiliser IJSS sans compte 79.
- [ ] Je révise RECHERCHEX, SOMME.SI.ENS, TCD, NB.SI pour les doublons.

**Pratique**
- [ ] CV imprimé ×2, pièce d'identité, convocation, carnet + stylo.
- [ ] Itinéraire vers **1625 route des Lucioles, Sophia Antipolis 2, Biot** (bouchons fréquents aux heures de pointe sur la technopole : prévoir une marge), téléphone du standard : 04 93 95 50 83.
- [ ] Mes 3 exemples STAR (litige résolu, clôture tenue, amélioration d'un process).
- [ ] Mes 5 questions prioritaires pour le recruteur.
- [ ] Ma fourchette de salaire et ma date de disponibilité.

## À retenir en 30 secondes

- GSF : n° 2 français de la propreté, ≈ 1,4 Md€ de CA en 2024, ≈ 43 000 salariés, ≈ 160 établissements.
- Toujours vérifier la société et le code établissement avant de saisir une facture.
- On ne paie que ce qui a été commandé, reçu et validé (bon à payer).
- Payer les fournisseurs dans les délais légaux, c'est éviter pénalités et amendes.
- Nettoyage courant = TVA normale ; nettoyage de fin de chantier en sous-traitance = autoliquidation.
- Jamais de changement de RIB sur simple e-mail : contre-appel sur un numéro connu.
- En entretien, présentez ce que vous ne savez pas de GSF comme des hypothèses et posez des questions.
