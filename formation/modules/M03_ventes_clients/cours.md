# M03 — Le cycle ventes et clients

> **Objectif du module.** À la fin de ce module, vous savez comptabiliser toutes les formes de ventes rencontrées dans le portefeuille (caisse, marketplace, situations de travaux, phases d'honoraires, abonnements, débours…), suivre le poste clients comme un senior (lettrage, balance âgée, relances, dépréciations, procédures collectives) et conseiller le client sur sa facturation (mentions, délais, facture électronique).
>
> **Prérequis :** M01 (fondamentaux), M02 (achats). Le module M04 (TVA) prolonge directement celui-ci : on y renvoie dès qu'une question de TVA devient technique.

!!! abstract "En clair — ce module en 5 idées"
    1. **Une vente compte quand le client est servi, pas quand on facture.** Le pain vendu le 31/12 par C01 Boulangerie Dupain est une vente de l'année, même si l'argent arrive en janvier.
    2. **Une facture doit être complète.** Il y a une liste de mentions obligatoires. Si une mention manque, la facture est irrégulière. Avec la facture électronique, cette liste s'allonge un peu.
    3. **Chaque façon de vendre a son écriture.** Le ticket de caisse de C01, le relevé de marketplace de C09 Mode & Co, la situation de chantier de C02 Bâtisseurs du Sud : la logique est la même, mais les comptes changent.
    4. **On enregistre toujours le montant brut.** Si une plateforme verse 900 € après avoir gardé 100 € de commission, la vente est de 1 000 €, et la commission est une charge.
    5. **Un client qui ne paie pas se suit étape par étape.** Relance, client « douteux », provision (dépréciation), puis perte définitive. C24 Menuiserie Bois & Création, dont un client est en liquidation, en est l'exemple type.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Chiffre d'affaires (CA) | Le total des ventes de l'entreprise, sans la TVA | C04 Le Petit Zinc vend environ 820 000 € par an |
    | HT / TTC | HT = prix sans la taxe. TTC = prix que le client paie vraiment, taxe comprise | 100 € HT + 20 € de TVA = 120 € TTC |
    | Compte 411 « Clients » | Le compte qui garde la trace de ce que les clients doivent encore | Facture de 1 200 € non payée → 1 200 € au débit du 411 |
    | Comptes 70x | Les comptes où l'on range les ventes, selon leur nature | 707 pour des vêtements revendus par C09 |
    | Avoir | Une « facture à l'envers » qui annule ou réduit une facture déjà envoyée | Un client renvoie une robe : Mode & Co lui fait un avoir |
    | Acompte | Une avance payée par le client sur une commande ferme | Un client de C13 Atelier Ligne verse 30 % au démarrage |
    | Arrhes | Une avance qui permet de renoncer à la commande, en la perdant | Un client réserve une chambre à C16 Hôtel Belle Vue puis annule |
    | Débours | Une somme payée pour le client, en son nom, et refacturée au centime près, sans TVA | Les taxes de carte grise payées par C03 Garage Martin |
    | Z de caisse | Le ticket de fin de journée qui résume toutes les ventes de la caisse | Le Z quotidien de la boulangerie C01 |
    | Marketplace / PSP | Un site qui vend pour vous (Amazon…) ou un service qui encaisse pour vous (Stripe, PayPal) | C09 vend via une marketplace et encaisse par Stripe |
    | Lettrage | Relier une facture et son paiement pour montrer qu'ils « vont ensemble » | Facture n° 45 lettrée avec le virement du 12/03 |
    | Balance âgée | Le tableau des sommes dues par les clients, classées par ancienneté du retard | C11 Transports Leroy : qui doit depuis plus de 90 jours ? |
    | Client douteux (416) | Un client dont on craint qu'il ne paie pas | Un client en redressement judiciaire |
    | Dépréciation | Une perte probable qu'on enregistre avant qu'elle soit sûre | On prévoit de ne récupérer que la moitié d'une créance |
    | Procédure collective | Une procédure au tribunal pour une entreprise en difficulté (sauvegarde, redressement, liquidation) | Un client de C24 placé en liquidation |

---

## 1. Le cycle commercial : de la demande du client à l'encaissement

> 🟢 **En clair :** une vente passe par plusieurs étapes : devis, commande, livraison, facture, paiement. Chaque étape laisse un papier. Votre travail est de savoir à quelle étape on enregistre quoi, et dans quel compte.

### 1.1 Les étapes et les documents

| Étape | Document | Effet juridique | Effet comptable |
|---|---|---|---|
| Demande de prix | Devis (proposition commerciale) | Offre ; devient contrat quand il est signé « bon pour accord » | Aucun |
| Accord | Bon de commande / devis signé / contrat | Contrat formé | Aucun (sauf acompte versé) |
| Acompte ou arrhes | Facture d'acompte (obligatoire en B2B dès qu'un acompte est encaissé) | Avance sur le prix | 4191 + TVA selon exigibilité |
| Exécution | Bon de livraison, PV de réception, relevé d'heures, situation de travaux | Transfert de propriété / service rendu | **Fait générateur du produit** |
| Facturation | Facture (et, dès 2026-2027, facture électronique via une PA) | Créance exigible | 411 / 70x / 4457x |
| Encaissement | Relevé bancaire, Z de caisse, relevé PSP, relevé marketplace | Extinction de la créance | 512 / 411 (et TVA sur encaissements) |
| Incident | Relance, mise en demeure, avoir, procédure collective | — | 416, 491, 654, 709… |

> 💡 **Réflexe senior :** le produit se rattache à l'exercice où la **livraison** (biens) ou l'**exécution** (services) a eu lieu, pas à la date de la facture ni à celle de l'encaissement. La facture n'est qu'une **preuve**. D'où les comptes de régularisation : **4181** (factures à établir) quand on a livré sans facturer, **487** (produits constatés d'avance) quand on a facturé sans avoir livré.

> 🟢 **En clair :** livré mais pas encore facturé → on ajoute la vente quand même (4181). Facturé mais pas encore livré → on retire la vente de l'année (487). Ce qui compte, c'est la date du service rendu.

### 1.2 Les comptes de produits

| Compte | Contenu | Exemples dans le portefeuille |
|---|---|---|
| 701 | Ventes de produits finis (fabriqués par l'entreprise) | Pain (C01), meubles sur mesure (C24), imprimés (C18) |
| 704 | Travaux | Gros œuvre (C02), pose de menuiseries (C24) |
| 706 | Prestations de services | Honoraires (C13), abonnements SaaS (C08), nuitées (C16), transport (C11) |
| 707 | Ventes de marchandises (achetées pour être revendues en l'état) | Luminaires (C19), VO (C03), vêtements (C09), parapharmacie (C12) |
| 708 | Produits des activités annexes (dont **7085 ports et frais accessoires facturés**, refacturations diverses) | Frais de port (C09), refacturation de taxe foncière (C07) |
| 709 | Rabais, remises et ristournes **accordés** (7091 sur 701… **7097 sur 707**) | Ristourne de fin d'année, avoir commercial |

> ⚠️ **Erreur classique :** comptabiliser une **remise figurant sur la facture** en 709. Les réductions qui figurent sur la facture initiale (remise, rabais) ne se comptabilisent pas : on enregistre directement le **net commercial**. Le 709 ne sert qu'aux réductions accordées **après** la facture (avoir) ou aux ristournes de fin de période.

> ⚠️ **Erreur classique :** utiliser le 791 « transfert de charges » pour une refacturation. **Les comptes de transfert de charges ont été supprimés** par le règlement ANC n° 2022-06 (exercices ouverts depuis le 01/01/2025). Une refacturation de frais au client est un **produit** (706 ou 708 selon la nature).

---

## 2. La facture : mentions et délais

> 🟢 **En clair :** une facture n'est pas un simple papier libre : la loi fixe ce qu'elle doit contenir et le délai pour la payer. Au cabinet, vous vérifiez les factures de vos clients et vous les conseillez pour qu'elles soient conformes, surtout avant le passage à la facture électronique.

### 2.1 Mentions obligatoires (art. L. 441-9 C. com., art. 242 nonies A ann. II CGI)

- Date d'émission ; **numéro unique** basé sur une séquence chronologique et continue (des séries distinctes sont possibles si justifiées).
- Identité du vendeur et du client (dénomination, adresse, **SIREN** du vendeur ; **SIREN du client** devient obligatoire avec la facture électronique) ; **n° de TVA intracommunautaire** du vendeur et, pour les opérations intracommunautaires B2B, celui du client.
- Adresse de facturation et, si différente, **adresse de livraison** (nouvelle mention).
- **Nature de l'opération** : livraison de biens / prestation de services / mixte (nouvelle mention).
- Désignation, quantité, prix unitaire HT, taux et montant de TVA par taux, total HT et TTC, réductions de prix acquises.
- Date de la livraison ou de l'exécution (ou de l'acompte), **date d'échéance** du paiement, conditions d'escompte (ou « pas d'escompte pour paiement anticipé »).
- **Taux des pénalités de retard** et **indemnité forfaitaire pour frais de recouvrement de 40 €** (uniquement entre professionnels).
- Mentions spéciales : « Autoliquidation » (sous-traitance BTP, B2B intra-UE), « Exonération de TVA, art. 262 ter I du CGI » (livraison intracommunautaire), « TVA non applicable, art. 293 B du CGI » (franchise), « Régime particulier – Biens d'occasion » (TVA sur la marge), « **Option pour le paiement de la taxe d'après les débits** » si option.

### 2.2 Délais de paiement (art. L. 441-10 C. com. — loi LME)

| Règle | Contenu |
|---|---|
| Délai supplétif | 30 jours après la réception des marchandises ou l'exécution de la prestation |
| Délai convenu maximum | **60 jours à compter de la date d'émission de la facture**, ou, si convenu et sans abus, **45 jours fin de mois** |
| Pénalités de retard | Taux fixé aux CGV ; à défaut, taux de refinancement BCE + 10 points ; minimum 3 fois le taux d'intérêt légal. Exigibles **sans rappel** |
| Indemnité forfaitaire | **40 €** par facture payée en retard (art. D. 441-5), entre professionnels |
| Sanction | Amende administrative (DGCCRF) pouvant atteindre 2 M€ pour une personne morale |

Calcul des « 45 jours fin de mois » : deux méthodes admises par la pratique — (a) fin du mois d'émission + 45 jours, ou (b) date de facture + 45 jours puis fin de ce mois. Facture du 10/03 : (a) 31/03 + 45 j = 15/05 ; (b) 24/04 → 30/04. **Retenez la méthode écrite dans les CGV.**

> 💡 **Réflexe senior :** les pénalités de retard et l'indemnité de 40 € sont **hors champ de TVA** (ce sont des indemnités, pas la contrepartie d'un service). Si le client les facture, il les comptabilise en produits financiers (**763**, revenus des autres créances) pour les intérêts de retard et en produits de gestion courante (**758**, *subdivision selon la nomenclature 2025 du PCG*) pour l'indemnité de 40 €. Ne les comptabilisez **que si elles sont réellement réclamées et recouvrables** (prudence).

### 2.3 Relances : la procédure type d'un cabinet sérieux

1. J+1 après échéance : relance amiable (e-mail + copie de la facture).
2. J+15 : relance téléphonique, puis courrier rappelant les pénalités et les 40 €.
3. J+30 : **mise en demeure** par LRAR (point de départ des intérêts au taux légal si les CGV sont muettes).
4. J+45 : injonction de payer (tribunal de commerce, procédure peu coûteuse) ou commissaire de justice.
5. À tout moment : vérifier au **BODACC** que le client n'est pas en procédure collective (si oui → **déclaration de créance**, voir § 7).

### 2.4 La facturation électronique (calendrier à connaître par cœur)

| Obligation | Qui | Depuis / à partir du |
|---|---|---|
| **Réception** des factures électroniques | Toutes les entreprises assujetties | **01/09/2026** |
| **Émission** + **e-reporting** (B2C, international, données de paiement des services) | Grandes entreprises et ETI | **01/09/2026** |
| Émission + e-reporting | PME, TPE, micro-entreprises | **01/09/2027** |

Les factures transitent par une **plateforme agréée (PA)** (anciennement PDP). Un PDF envoyé par e-mail ou une photo WhatsApp **n'est pas** une facture électronique. Dans le portefeuille, tous les clients sont des PME/TPE : ils **reçoivent** déjà en électronique et **émettront** au 01/09/2027 — c'est maintenant qu'il faut auditer leurs mentions, leur numérotation et leurs fichiers clients (SIREN de chaque client !).

> 💡 **Réflexe senior :** l'e-reporting des **données de paiement** concerne les prestations de services (TVA exigible à l'encaissement). Pour Atelier Ligne (C13) ou TechNova (C08), il faudra transmettre la date et le montant de chaque encaissement : un lettrage clients propre devient une obligation fiscale, plus seulement une bonne pratique.

---

## 3. Les schémas d'écritures de vente

> 🟢 **En clair :** cette section est votre « boîte à modèles ». Pour chaque type de vente (simple, avec acompte, en caisse, sur une plateforme, avec bon cadeau, sur un chantier), vous trouvez l'écriture type à reproduire.

### 3.1 Vente simple, frais de port, escompte

| Opération | Débit | Crédit |
|---|---|---|
| Facture de marchandises avec port refacturé | 411 (TTC) | 707 (HT net de remises), 7085 (port HT), 44571 (TVA) |
| Escompte **accordé** pour paiement comptant (avoir d'escompte) | 665 (HT de l'escompte), 44571 (TVA correspondante) | 411 |
| Avoir commercial postérieur à la facture | 709x (HT), 44571 | 411 |
| Retour de marchandises | 707 (HT), 44571 | 411 |

Les frais de port refacturés suivent le **taux de TVA de la marchandise** (l'accessoire suit le principal). L'escompte réduit la base de TVA : sans avoir rectificatif (ou sans mention sur la facture initiale du montant de TVA réduit), le vendeur reste redevable de la TVA sur le prix plein.

> 🟢 **En clair :** les frais de port prennent le même taux de TVA que l'objet vendu. Et si vous accordez une réduction pour paiement rapide (escompte), vous ne payez moins de TVA que si un avoir (ou la facture) le dit noir sur blanc.

### 3.2 Acomptes, arrhes et factures d'acompte

| | Acompte | Arrhes |
|---|---|---|
| Nature juridique | Premier versement d'un prix ; **engagement ferme** des deux parties | Faculté de dédit (art. 1590 C. civ.) : l'acheteur perd les arrhes, le vendeur qui se dédit rend le double |
| Présomption en B2C | — | **Sauf stipulation contraire, les sommes versées d'avance sont des arrhes** (art. L. 214-1 C. consom.) |
| Comptabilisation à la réception | 512 / **4191** (HT) + TVA si exigible | Idem |
| TVA à l'encaissement | **Services** : TVA exigible à l'encaissement de l'acompte. **Biens** : depuis le 01/01/2023, l'acompte sur une livraison de biens rend aussi la TVA exigible | Idem à l'encaissement ; si les arrhes sont **conservées** après désistement, elles deviennent une indemnité (hors champ selon la doctrine traditionnelle — voir E03-05) |
| À la facture finale | 411 (solde TTC) + 4191 (HT de l'acompte) / 70x (HT total) + TVA restant due | — |

> ⚠️ **Erreur classique :** porter l'acompte au crédit du 411. Un acompte reçu est une **dette** envers le client (4191, au passif) tant que la livraison n'a pas eu lieu. À la clôture, un 4191 qui « traîne » doit être justifié (livraison faite mais non facturée ? acompte à rembourser ?).

### 3.3 Débours (art. 267-II-2° CGI)

Les débours sont des sommes payées **au nom et pour le compte du client** et refacturées **à l'euro près**. Ils sont **exclus de la base de TVA** si trois conditions sont réunies :

1. le prestataire agit en vertu d'un **mandat explicite** (même verbal, mais prouvable : un mandat d'immatriculation signé pour une carte grise) ;
2. les sommes sont comptabilisées dans des **comptes de passage** (**467**), jamais en charges / produits ;
3. le prestataire **rend compte** au client (refacturation au montant exact, justificatif à l'appui).

| Opération | Débit | Crédit |
|---|---|---|
| Paiement du débours (ex. taxes de carte grise à l'ANTS) | 467 Débours clients | 512 |
| Refacturation | 411 | 467 (montant exact, sans TVA) |
| Frais de dossier facturés en plus | 411 | 706 + 44571 |

> ⚠️ **Erreur classique :** traiter en débours des **frais engagés pour son propre compte** (frais de déplacement de l'architecte, reprographie, transport refacturé). Ce sont des frais accessoires de la prestation : produit + TVA.

### 3.4 Ventes en caisse (commerce de détail)

- Le **Z de caisse** (ticket de clôture journalière) est la pièce comptable. Depuis 2018, les assujettis qui encaissent des particuliers doivent utiliser un **logiciel de caisse sécurisé** (inaltérabilité, sécurisation, conservation, archivage) justifié par un **certificat ou une attestation individuelle de l'éditeur** (art. 286-I-3° bis CGI ; amende de 7 500 € par logiciel non conforme).
- Comptabilisation journalière (ou mensuelle récapitulative si les Z sont conservés et détaillés) :

| Débit | Crédit |
|---|---|
| 531 Caisse (espèces) | 701 / 707 par taux (HT) |
| 511x CB à encaisser | 44571 par taux |
| 511x Titres-restaurant à encaisser | |

- Ensuite : remise d'espèces en banque (**580** virements internes), télécollecte CB (commission bancaire en 627), remboursement des titres-restaurant (commission de la centrale en 627 ou 622 selon la facture).
- **Écart de caisse** = espèces comptées – espèces théoriques. Un écart négatif est une charge (**658**), un écart positif un produit (**758**) — *subdivisions selon la nomenclature 2025 du PCG*. La TVA collectée reste celle du Z.

> 💡 **Réflexe senior :** une caisse ne peut **jamais être créditrice** (sinon la comptabilité est irrégulière et peut être rejetée en contrôle). Des écarts négatifs **systématiques** révèlent soit des prélèvements non justifiés, soit des ventes non enregistrées : dans les deux cas, risque de redressement (et pour un gérant de SARL qui se sert dans la caisse, compte courant débiteur interdit, art. L. 223-21 C. com.).

### 3.5 Marketplaces et prestataires de paiement (PSP : Stripe, PayPal…)

Principe : **on comptabilise le brut**, jamais le net versé.

| Élément du relevé | Écriture |
|---|---|
| Ventes TTC encaissées par la plateforme | 467 Plateforme / 707 + 7085 + 4457x |
| Remboursements clients | 707 (ou 709) + 4457x / 467 |
| Commissions de la plateforme (facture de la plateforme) | 622 (ou 627 pour les frais de paiement) + 44566 / 467 (ou 401) |
| Réserve de sécurité retenue | 467 « réserve » / 467 plateforme |
| Virement reçu | 512 / 467 |

Le compte 467 de chaque plateforme doit être **rapproché chaque mois** avec le solde du relevé (comme un compte bancaire). Les relevés Stripe et PayPal fonctionnent de la même façon (un 512 « PayPal » est également admis si le compte est un véritable compte de paiement).

> ⚠️ **Erreur classique :** comptabiliser le virement net de la marketplace en chiffre d'affaires. Conséquences : CA minoré, commissions et TVA déductible oubliées, TVA collectée fausse — et une incohérence immédiate entre le CA déclaré et les données de la plateforme (qui transmet ses informations à l'administration).

### 3.6 Cartes et bons cadeaux

| Type de bon | Exemple | TVA | Comptabilisation à la vente du bon | À l'utilisation |
|---|---|---|---|---|
| **Bon à usage unique** (lieu et taux de TVA connus à l'émission) | Carte « abonnement 3 mois » de FitClub | Exigible **à la vente du bon** | 512 / 4191 (HT) + 44571 | 4191 / 706 |
| **Bon à usages multiples** (taux inconnu à l'émission) | Carte cadeau Mode & Co utilisable sur tout le site (vêtements en France ou livraison UE) | Exigible **à l'utilisation** | 512 / 4191 (montant TTC du bon) | 4191 / 707 + 4457x |
| Bon expiré non utilisé | — | Usage multiple : hors champ | 4191 / 758 | — |

### 3.7 Abonnements, prestations continues, chantiers

- Abonnement facturé d'avance : produit en 706 à la facture, puis **PCA (487)** à la clôture pour la fraction non courue (calcul au prorata temporis de la **période de service**).
- Prestation continue facturée à terme échu : **4181** pour la part exécutée non facturée.
- Contrats à long terme (BTP, ingénierie) : méthode à l'avancement (préférentielle) ou à l'achèvement — voir M08. Les **situations de travaux** sont des factures d'acomptes sur le prix ; seul l'**avancement réel** détermine le produit.

### 3.8 Retenues de garantie (BTP)

La loi n° 71-584 du 16 juillet 1971 autorise le maître d'ouvrage à retenir **au maximum 5 %** du montant des travaux jusqu'à la levée des réserves (au plus tard **un an** après la réception), sauf si l'entreprise fournit une **caution bancaire**.

| Débit | Crédit |
|---|---|
| 411 (net à payer) + **4117 Clients – retenues de garantie** | 704 (HT total de la situation) + 44574 TVA en attente (travaux = TVA à l'encaissement) |

> ⚠️ **Erreur classique :** déduire la retenue de garantie du chiffre d'affaires. La retenue est une **créance** à plus d'un an possible, pas une réduction de prix.

---

## 4. Effets de commerce, affacturage

> 🟢 **En clair :** certaines entreprises n'attendent pas que le client paie : elles confient leurs factures à la banque (effet de commerce) ou à une société spécialisée (factor) pour être payées plus tôt. Cela coûte des frais, et la facture ne disparaît pas toujours du risque de l'entreprise.

### 4.1 Effets à recevoir (LCR)

| Opération | Débit | Crédit |
|---|---|---|
| Acceptation de la LCR | 413 Effets à recevoir | 411 |
| Remise à l'encaissement | 5113 Effets à l'encaissement | 413 |
| Remise à l'escompte | 5114 Effets à l'escompte | 413 |
| Crédit de l'escompte | 512 + 661 (intérêts) + 627 (commissions) | 5114 |

Les effets escomptés non échus sont un **engagement hors bilan** à mentionner en annexe (risque de recours si le tiré ne paie pas).

### 4.2 Affacturage (subrogation)

| Opération | Débit | Crédit |
|---|---|---|
| Cession des factures au factor | 467 Factor | 411 |
| Financement reçu (net de la réserve / fonds de garantie) | 512 + 467 Factor – fonds de garantie | 467 Factor |
| Commission d'affacturage + TVA | 622 + 44566 | 467 Factor |
| Commission de financement (intérêts, exonérée de TVA) | 661 | 467 Factor |

Point de révision : en affacturage **avec recours**, le risque d'impayé reste chez le client — la dépréciation des créances cédées doit toujours être analysée.

---

## 5. Les cas sectoriels du portefeuille

> 🟢 **En clair :** chaque métier vend à sa façon. Ce tableau vous dit, client par client, quelle particularité surveiller et quel exercice la travaille. Par exemple, l'hôtel C16 encaisse une taxe de séjour qui ne lui appartient pas.

| Client | Spécificité vente | Où l'approfondir |
|---|---|---|
| C01 Boulangerie Dupain | Z de caisse multi-taux, espèces, titres-restaurant | E03-01 |
| C02 Bâtisseurs du Sud | Situations de travaux, retenue de garantie, autoliquidation sous-traitance | E03-02 |
| C13 Atelier Ligne | Honoraires par phases, acompte, en-cours de services, TVA sur encaissements | E03-03, E04-07 |
| C09 Mode & Co | Marketplace, PSP, retours, ventes UE | E03-04, E04-06 |
| C16 Hôtel Belle Vue | Arrhes / acomptes, no-show, Booking, taxe de séjour | E03-05 |
| C03 Garage Martin | VO (TVA sur la marge), cartes grises en débours | E03-06, E04-03 |
| C24 Menuiserie Bois & Création | Client en redressement puis liquidation | E03-07 |
| C08 TechNova | Abonnements SaaS, PCA | E03-08 |
| C18 Imprimerie Graphique Rhône | Doublons, client étranger, avoir sur exercice clos | E03-09 |
| C11 Transports Leroy | Balance âgée, dépréciations | E03-10 |

**Taxe de séjour (hôtels) :** collectée pour le compte de la commune (art. L. 2333-26 et s. CGCT), elle n'est **ni du CA ni dans la base de TVA** : compte de tiers (467 « Commune – taxe de séjour ») jusqu'au reversement.

**Plateformes de réservation (Booking…) :** l'hôtel facture le client au prix plein et enregistre la commission de la plateforme en charge. Une plateforme établie dans un autre État membre facture sa commission **sans TVA** : l'hôtel **autoliquide** la TVA (art. 283-2 CGI) — voir M04.

---

## 6. Le poste clients en révision

> 🟢 **En clair :** « réviser le poste clients », c'est vérifier que les sommes dues par les clients sont réelles et seront bien payées. Si un client risque de ne pas payer, on le signale dans les comptes. C'est un contrôle que vous ferez à chaque bilan.

### 6.1 Contrôles de base (à chaque situation)

1. **Lettrage** à jour ; aucun solde ancien non lettré sans explication.
2. **Balance âgée** (par tranches : non échu, 0-30, 31-60, 61-90, 91-180, > 180 j, > 1 an).
3. **Clients créditeurs** : doublons de paiement, avoirs non imputés, acomptes mal affectés → à reclasser au passif (4191 / 4198 / 419 « clients créditeurs ») à la clôture ; jamais de produit tant que la dette envers le client existe (prescription commerciale de **5 ans**, art. L. 110-4 C. com.).
4. **Circularisation** des principaux clients (audit légal ou révision approfondie).
5. **Cut-off** : dernières livraisons / premières factures de l'exercice suivant ; avoirs émis après la clôture portant sur des ventes de l'exercice (→ **4198 RRR à accorder** ou avoir à établir).
6. Rapprochement **CA comptable / CA déclaré en TVA** (voir M04, E04-10).

### 6.2 Créances douteuses et dépréciation

| Étape | Débit | Crédit |
|---|---|---|
| Reclassement (retard significatif, litige, procédure) | **416** Clients douteux (TTC) | 411 |
| Dépréciation à la clôture (**sur le HT** : la TVA est récupérable en cas de perte) | **6817** Dotations aux dépréciations des actifs circulants | **491** Dépréciation des comptes clients |
| Ajustement N+1 | 491 / 7817 (reprise) ou 6817 / 491 (complément) | |
| Perte définitive | **654** Pertes sur créances irrécouvrables (HT) + 44571 (TVA récupérée) | 416 (TTC) |
| Reprise de la dépréciation devenue sans objet | 491 | 7817 |

Fiscalement (art. 39-1-5° CGI), la dépréciation n'est déductible que si la perte est **nettement précisée** et **probable** à la clôture, du fait d'événements en cours : la dépréciation doit être **individualisée** (créance par créance, motif documenté). Une dépréciation **forfaitaire ou statistique** (« 50 % des créances de plus de 6 mois ») est **réintégrée** extra-comptablement ; la jurisprudence n'admet de méthode statistique qu'à titre exceptionnel, pour des créances nombreuses et de faible montant, sur la base d'une expérience passée précise et documentée.

> 🟢 **En clair :** pour que l'impôt accepte la dépréciation, il faut viser chaque client un par un, avec une raison écrite (retard, litige, procédure). Un pourcentage appliqué « à la louche » sur toutes les vieilles factures est refusé par le fisc.

> 💡 **Réflexe senior :** si le client a une **assurance-crédit**, la perte probable n'est que la part **non couverte** (franchise, quotité non garantie). Documentez la police, la date de déclaration du sinistre et l'accord de l'assureur.

### 6.3 Procédures collectives : le chemin complet

```
Jugement d'ouverture (sauvegarde / redressement / liquidation)
   │  publication au BODACC
   ▼
Déclaration de créance au mandataire judiciaire (ou liquidateur)
   délai : 2 MOIS à compter de la publication au BODACC (art. L. 622-24 et R. 622-24 C. com.)
   montant : TTC, créances antérieures au jugement (+ pénalités échues avant le jugement)
   hors délai : action en relevé de forclusion dans les 6 mois (art. L. 622-26)
   ▼
Comptablement : 411 → 416, dépréciation du HT selon la probabilité de dividende
   ▼
TVA : récupération quand la créance est définitivement irrécouvrable (art. 272-1 CGI),
   en pratique dès le jugement de LIQUIDATION judiciaire (ou à hauteur de l'abandon dans un plan),
   sous réserve d'une facture rectificative (avoir de TVA) adressée au débiteur / liquidateur
   ▼
Perte définitive (clôture pour insuffisance d'actif, certificat d'irrécouvrabilité) : 654 + reprise 491
```

> ⚠️ **Erreur classique :** « récupérer » la TVA sur une facture de **prestations de services ou de travaux** impayée. Pour ces opérations, la TVA n'est exigible qu'à l'**encaissement** (sauf option débits) : sur une facture jamais payée, elle n'a jamais été reversée — elle est simplement en 44574 (TVA en attente). Il suffit de solder ce compte, sans rien « récupérer » sur la CA3.

> 🟢 **En clair :** pour un service ou des travaux, la TVA n'est due que quand le client paie. Si le client ne paie jamais, vous n'avez jamais versé cette TVA à l'État : il n'y a donc rien à vous faire rembourser.

### 6.4 Créances irrécouvrables hors procédure

Une créance peut être passée en perte sans procédure collective si son irrécouvrabilité est **prouvée** : procès-verbal de carence d'un commissaire de justice, débiteur disparu, créance prescrite, coût de recouvrement disproportionné (petites créances, documenté). La TVA est alors récupérable dans les mêmes conditions (facture rectificative).

---

## 7. Les opérations atypiques à repérer

> 🟢 **En clair :** voici les situations « bizarres » qui reviennent souvent : client qui paie deux fois, frais bancaires retenus, avoir qui arrive après la clôture… Quand vous en voyez une, ce tableau vous donne la bonne réponse.

| Situation | Traitement |
|---|---|
| Client qui paie deux fois | 411 créditeur → remboursement (512) ou imputation sur une prochaine facture avec accord écrit ; à la clôture, reclassement au passif |
| Client étranger, frais bancaires déduits | Différence en **627** (si non récupérable) ; si l'écart provient d'un taux de change → 666 / 766 |
| Avoir sur une facture d'un exercice clos | Comptabilisé dans l'exercice de l'avoir (709 / 44571) ; la TVA se régularise sur la déclaration de la **période de l'avoir**. Si le litige était connu avant l'arrêté des comptes de l'exercice précédent, il aurait fallu un **4198** (RRR à accorder) à la clôture |
| Escompte déduit sans accord | Ce n'est pas un escompte : c'est un **impayé partiel** à relancer |
| Vente au nom du gérant | Facture irrégulière : à refaire au nom de la société |
| Vente d'une immobilisation | **775** (produit de cession), jamais en 70x — mais TVA collectée si le bien avait ouvert droit à déduction (attention au rapprochement CA / TVA) |

---

## 8. Checklist de fin de module

- [ ] Je sais rattacher un produit à son exercice (livraison / exécution) et passer 4181 / 487 à la clôture.
- [ ] Je distingue acompte et arrhes, et je sais quand la TVA est exigible sur une avance (biens depuis 2023, services).
- [ ] Je comptabilise un Z de caisse multi-taux, un écart de caisse et une remise d'espèces.
- [ ] Je comptabilise un relevé de marketplace / PSP **au brut** et je rapproche le 467.
- [ ] Je connais les trois conditions des débours (art. 267-II-2° CGI) et je les applique aux cartes grises.
- [ ] Je comptabilise une situation de travaux avec retenue de garantie (4117) et autoliquidation.
- [ ] Je connais les délais LME (60 j date de facture / 45 j fin de mois), les pénalités et l'indemnité de 40 €.
- [ ] Je sais conduire une créance de la relance à la perte : 416, dépréciation sur le HT, déclaration de créance dans les 2 mois, récupération de TVA, 654.
- [ ] Je sais pourquoi une dépréciation statistique est réintégrée fiscalement et comment documenter une dépréciation individuelle.
- [ ] Je connais le calendrier de la facture électronique (réception 01/09/2026 ; émission PME 01/09/2027) et les nouvelles mentions.

## Références

- PCG (règlement ANC n° 2014-03 modifié par le règlement n° 2022-06) : classes 4 et 7, comptes 4117, 416, 4191, 4198, 467, 487, 491, 654, 6817, 7817.
- Code de commerce : art. L. 441-9 (factures), L. 441-10 et D. 441-5 (délais, pénalités, indemnité de 40 €), L. 110-4 (prescription), L. 622-24 à L. 622-26 et R. 622-24 (déclaration de créances), L. 223-21 (interdiction des comptes courants débiteurs en SARL).
- Code civil : art. 1590 (arrhes) ; Code de la consommation : art. L. 214-1.
- CGI : art. 39-1-5° (dépréciations), 267-II-2° (débours), 269 (exigibilité), 272-1 (TVA sur créances irrécouvrables), 283-2 et 283-2 nonies (autoliquidation), 286-I-3° bis (logiciels de caisse), 289 et 242 nonies A ann. II (factures).
- Loi n° 71-584 du 16 juillet 1971 (retenue de garantie).
- BOFiP : séries TVA-BASE (base d'imposition, débours, indemnités), TVA-DED (régularisation pour impayés), BIC-PROV (dépréciation des créances).

## À retenir en 30 secondes

- Une vente appartient à l'année où le client a été livré ou servi, pas à la date de la facture.
- Une facture doit porter toutes les mentions obligatoires ; vérifiez-les avant la facture électronique de 2027.
- Un acompte reçu est une dette envers le client (4191), pas une vente, tant que rien n'est livré.
- Ventes par plateforme ou par Stripe : on enregistre toujours le montant brut, et la commission à part.
- Les débours (payés au nom du client, refacturés au centime) n'ont pas de TVA, à trois conditions.
- Un client qui ne paie pas suit un chemin : relance, 416, dépréciation sur le HT, déclaration de créance en 2 mois, puis perte (654).
- Une dépréciation se justifie client par client, avec une raison écrite.
