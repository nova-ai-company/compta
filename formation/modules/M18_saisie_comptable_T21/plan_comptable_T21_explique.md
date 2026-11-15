# Le plan comptable T21 France, compte par compte
<!-- sans-glossaire-page -->

*Les **268 comptes** du « Plan comptable général T21 France » (mis à jour le 13/10/2025), recopiés à l'identique avec, pour chacun, une explication simple et le journal où on le rencontre le plus souvent. Gardez cette page ouverte pendant les exercices du module M18.*

!!! abstract "En clair : comment lire un numéro de compte T21"
    Les comptes T21 ont **7 chiffres**. On les lit de gauche à droite, du général au précis :

    - **6** : classe 6, une charge ;
    - **62** : autres services extérieurs ;
    - **622** : honoraires ;
    - **6223** : honoraires médicaux et paramédicaux ;
    - **6223221** : honoraires des **orthophonistes**.

    Les comptes de **tiers** n'ont pas de numéro mais un **code** : **FO** + nom pour un fournisseur, **LI** + nom pour un libéral, **SA** + nom pour un salarié (notes de frais), **CL** + nom pour un client. Ils sont regroupés automatiquement dans les comptes de centralisation 4010000, 4011000, 4248000 et 4110000.

!!! tip "Trois remarques de senior sur ce plan"
    1. **Aucun compte 445 (TVA).** Les structures ne récupèrent pas la TVA : toutes les factures se saisissent **TTC**.
    2. **Pas de comptes 601 ou 603 (stocks).** Le document T21 le confirme : « il n'y a pas de notion de stocks », on utilise les **606**.
    3. **Le plan est daté du 13/10/2025** (« applicable au 1/01/2025 ») alors que le document T21 s'appuie sur l'arrêté du 19/12/2025, applicable au 1er janvier 2026. Avant la clôture 2026, demandez si le plan a été mis à jour.

Les colonnes « En clair » et « Journal habituel » sont des explications de formation. Les codes de journaux sont ceux du dossier M18 :

| Code | Journal |
|---|---|
| AC | Achats |
| VT | Ventes |
| BQ | Banque |
| PL | Banque placement |
| CA | Caisse |
| PA | Paie |
| IM | Immobilisations |
| OD | Opérations diverses |

Quand une explication dit « à clarifier » ou « à faire confirmer », c'est une question à poser à votre arrivée : le document ne permet pas de trancher.

## Classe 1 — Capitaux (fonds propres, réserves, résultat, provisions, emprunts, liaisons, fonds dédiés)

| Compte | Libellé du plan T21 | En clair / exemple | Journal habituel |
|---|---|---|---|
| **1023100** | Dotations non consomptibles initiales | Biens ou fonds apportés à l'origine et qui ne doivent pas être dépensés. Rare. | OD |
| **1032000** | Fonds propres sattutaires avec droits de reprise | Fonds propres de départ qu'un financeur peut reprendre si le service ferme. Le plan écrit « sattutaires » (coquille pour « statutaires »). | OD |
| **1068522** | Res invest - Autres éts relevant du I art L.312-1 du CASF | Réserve d'investissement : excédent d'un ESSMS mis de côté, sur décision du financeur, pour financer un investissement. | OD (affectation du résultat) |
| **1068552** | Res tréso - Autres éts relevant du I art L.312-1 du CASF | Réserve de trésorerie : excédent affecté pour renforcer la trésorerie du service. | OD |
| **1068562** | Res compens déficits- Autres éts relevant  art L.312-1 du CASF | Réserve de compensation des déficits : couvre un futur déficit. Le document T21 indique qu'elle doit atteindre au moins 5 % de la dotation annuelle. | OD |
| **1068572** | Res compens amort- Autres éts relevant  art L.312-1 du CASF | Réserve de compensation des charges d'amortissement : couvre les surcoûts d'amortissement d'un investissement. | OD |
| **1150120** | RAN ESMS sous gestion contrôlée (créditeur) | Report à nouveau **excédentaire** d'un ESSMS financé par une autorité de tarification (« gestion contrôlée ») : excédent pas encore affecté. | OD |
| **1150300** | RAN affecté au financement de mesures d’exploitation | Excédent reporté pour financer des mesures d'exploitation (dépenses de fonctionnement) d'un budget suivant. | OD |
| **1159020** | RAN ESMS sous gestion contrôlée (débiteur) | Report à nouveau **déficitaire** d'un ESSMS sous gestion contrôlée : déficit en attente de reprise. | OD |
| **1159120** | RAN charges rejetées des activités sociales et médico-soc. | Charges que le financeur a refusé de financer (« rejetées ») : elles restent à la charge de l'association. | OD |
| **1159220** | Dépenses pour congés payés | Congés payés acquis non financés lors du passage à la provision (écriture de transition). À voir avec l'expert-comptable. | OD |
| **1159230** | Autres droits acquis par les salariés non provisionnés | Autres droits des salariés (ex. : indemnités de départ) non provisionnés, constatés en report à nouveau. | OD |
| **1195000** | RAN des activités ESSMS hors gestion ctlée (débiteur) | Report à nouveau déficitaire d'activités **hors** gestion contrôlée (non tarifées). | OD |
| **1202000** | Excédent de l'exercice ESMS sous gestion non contrôlée | Excédent de l'exercice d'une activité **non** tarifée (ex. : vie associative). | OD (clôture) |
| **1205000** | Excédent de l'exercice ESMS sous gestion contrôlée | Excédent de l'exercice d'un ESSMS tarifé (SESSAD, SAVS), en attente de décision d'affectation. | OD (clôture) |
| **1292000** | Déficit de l'exercice ESMS sous gestion non contrôlée | Déficit de l'exercice d'une activité non tarifée. | OD (clôture) |
| **1295000** | Déficit de l'exercice ESMS sous gestion contrôlée | Déficit de l'exercice d'un ESSMS tarifé. | OD (clôture) |
| **1412000** | Prov destinées à la couverture du BRR | Provision réglementée liée au besoin en fonds de roulement (BFR). **Jamais** sans accord du financeur. | OD |
| **1421000** | Prov réglem : renouvellement des immobilisations | Provision réglementée pour renouveler les immobilisations, accordée par le financeur. | OD |
| **1486100** | Prov réglem : réserves des plus-values nettes d'actif immo | Plus-values de cession d'immobilisations mises en réserve, sur décision réglementaire. | OD |
| **1518000** | Autres provisions pour risques | Provision pour un risque identifié (ex. : litige prud'homal). | OD (clôture) |
| **1523000** | Provisions pour impôts | Provision pour un impôt probable à payer. | OD (clôture) |
| **1526000** | Provisions pour remise en état | Provision pour remettre en état des locaux loués à la fin du bail. | OD (clôture) |
| **1640000** | Emprunts auprès des Ets de crédit | Capital restant dû des emprunts bancaires. Crédité au déblocage, débité à chaque remboursement de capital. | BQ (échéance), OD |
| **1648000** | Intérêts courus sur emprunts auprès des Ets de crédit | Intérêts courus non échus (ICNE) : intérêts de l'exercice qui seront payés l'an prochain. | OD (clôture) |
| **1840000** | Compte liaison exploit° courante (besoin fonds de roulement) | Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. | OD, AC (IS) |
| **1841100** | SIA - Compte liaison exploit° courante BFR | Liaison avec la structure « SIA » de la Fédération (code interne : à faire préciser). | OD (IS) |
| **1841200** | CFF - Compte liaison exploit° courante BFR | Liaison avec la structure « CFF » de la Fédération (code interne : à faire préciser). | OD (IS) |
| **1841300** | AF - Compte liaison exploit° courante BFR | Liaison avec la structure « AF » de la Fédération (code interne : à faire préciser). | OD (IS) |
| **1842000** | SESSAD DK - Compte liaison exploit° courante BFR | Liaison avec le SESSAD « DK » (vraisemblablement Dunkerque : à faire confirmer). | OD (IS) |
| **1843000** | SAVS DK - Compte liaison exploit° courante BFR | Liaison avec le SAVS « DK ». | OD (IS) |
| **1844000** | SESSAD Lille - Compte liaison exploit° courante BFR | Liaison avec le SESSAD de Lille. | OD (IS) |
| **1844050** | Compte de liaison des établissements | Liaison des établissements (compte générique). | OD (IS) |
| **1845000** | 56 - Compte liaison exploit° courante BFR | Liaison avec la structure « 56 » (numéro de département : Morbihan ; à faire confirmer). | OD (IS) |
| **1846000** | 28 - Compte liaison exploit° courante BFR | Liaison avec la structure « 28 » (Eure-et-Loir ; à faire confirmer). | OD (IS) |
| **1847000** | 93 - Compte liaison exploit° courante BFR | Liaison avec la structure « 93 » (Seine-Saint-Denis ; à faire confirmer). | OD (IS) |
| **1848000** | 91 - Compte liaison exploit° courante BFR | Liaison avec la structure « 91 » (Essonne ; à faire confirmer). | OD (IS) |
| **1921000** | Fonds dédiés à l'investissement | Subvention reçue pour un investissement, pas encore utilisée. | OD (clôture) |
| **1922000** | Fonds dédiés à l'exploitation | Fonds reçus pour l'exploitation d'un projet, pas encore utilisés. | OD (clôture) |
| **1940000** | Fonds dédiés sur subventions d'exploitation | Subvention d'exploitation **affectée** à un projet et non dépensée au 31/12 (ex. : fondation pour le projet Pairs). | OD (clôture) |
| **1950000** | Fonds dédiés sur contribution financières d'autres organismes | Contributions financières d'autres organismes (ex. : fondation d'entreprise) non utilisées. | OD (clôture) |
| **1960000** | Fonds dédiés sur ressources liées à la générosité du public | Dons du public affectés à un projet et non utilisés. | OD (clôture) |

## Classe 2 — Immobilisations

| Compte | Libellé du plan T21 | En clair / exemple | Journal habituel |
|---|---|---|---|
| **2050000** | Concessions et droits similaires, brevets, licences | Logiciel ou licence **achetés** (propriété durable). Un abonnement mensuel n'est pas une immobilisation. | AC |
| **2110000** | Terrains | Terrain (jamais amorti). | AC |
| **2131000** | Bâtiments | Bâtiment appartenant à l'association. | AC |
| **2135000** | Installations générales, agencements, aménagements des constructions | Agencements et installations dans un bâtiment **dont on est propriétaire**. | AC |
| **2154000** | Matériel et outillage | Matériel et outillage. | AC |
| **2181000** | Installations générales, agencements, aménagements divers | Agencements dans des locaux **loués** (ex. : cloisons, électricité refaite). | AC |
| **2182000** | Matériel de transport | Véhicule acheté (exemple du document T21 : véhicule acheté au garage Martin). | AC |
| **2183000** | Matériel de bureau et matériel informatique | Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. | AC |
| **2184000** | Mobilier | Mobilier (bureaux, armoires, tables). | AC |
| **2315000** | Immobilisations en cours - Inst, mat et outillage | Travaux commencés mais pas terminés au 31/12. Soldé vers la classe 21 à la fin des travaux. | AC, OD |
| **2710000** | Titres immobilisés (droit de propriété) | Titres détenus durablement (le document T21 y range les parts sociales du Crédit Mutuel ; le plan, lui, a aussi 5040000 : à clarifier). | BQ |
| **2750000** | Dépôts et cautionnements versés | Dépôt de garantie versé (loyer, compteur) : on le récupère à la fin du contrat. | BQ |
| **2805000** | Amort concessions et droits similaires, brevets, licences | Amortissements cumulés des logiciels. | IM (automatique) |
| **2813100** | Amort bâtiments | Amortissements cumulés des bâtiments. | IM |
| **2813500** | Amort installations générales, agencements, aménagements IGAAC | Amortissements cumulés des agencements dans les bâtiments. | IM |
| **2815400** | Amort Matériel et outillage | Amortissements cumulés du matériel. | IM |
| **2818100** | Amort Installations générales : agencements, aménagements divers | Amortissements cumulés des agencements divers. | IM |
| **2818200** | Amort Matériel de transport | Amortissements cumulés des véhicules. | IM |
| **2818300** | Amort Matériel de bureau et matériel informatique | Amortissements cumulés du matériel informatique. | IM |
| **2818400** | Amort Mobilier | Amortissements cumulés du mobilier. | IM |

## Classe 4 — Tiers

| Compte | Libellé du plan T21 | En clair / exemple | Journal habituel |
|---|---|---|---|
| **4010000** | Fournisseurs — tiers **FO** | Compte de **centralisation** des fournisseurs. **Interdit** d'y saisir : on saisit dans le compte de tiers FO… | — (alimenté automatiquement) |
| **4011000** | Libéraux — tiers **LI** | Centralisation des **libéraux** (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… | — |
| **4081000** | Fournisseurs  factures non parvenues | Facture **non parvenue** : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). | OD (clôture) |
| **4110000** | Clients — tiers **CL** | Centralisation des clients. On saisit dans les comptes CL… | — |
| **4181000** | Clients - factures à établir | Facture à établir : prestation faite en N, facturée en N+1. | OD (clôture) |
| **4210000** | Personnel - Rémunérations dues | Salaires **nets** à payer. Crédité par la paie, débité au virement des salaires. | PA (automatique), BQ |
| **4220000** | Comités d’entreprises, d’établissement, … | Sommes dues au CSE (comité social et économique). | PA, BQ |
| **4248000** | Salariés - NDF — tiers **SA** | Centralisation des **notes de frais** des salariés. On saisit dans les comptes SA… | — |
| **4250000** | Personnel - Avances et acomptes | Avance ou acompte versé à un salarié, récupéré sur la paie. | BQ, PA |
| **4270000** | Personnel - Oppositions | Sommes retenues sur salaire pour un tiers (saisie sur salaire, avis à tiers détenteur). | PA, BQ |
| **4282000** | Dettes provisionnées pour congés à payer | Congés payés acquis et non pris à la clôture (dette envers les salariés). | OD (clôture) |
| **4310000** | Sécurité sociale | URSSAF : cotisations à payer. Crédité par la paie, débité au paiement. | PA, BQ |
| **4372000** | Mutuelles | Cotisations mutuelle à payer. | PA, BQ |
| **4373100** | Caisse de retraite | Cotisations retraite complémentaire à payer. | PA, BQ |
| **4373200** | Caisse de prévoyance | Cotisations prévoyance à payer. | PA, BQ |
| **4374000** | Taxe d'apprentissage | Taxe d'apprentissage à payer. | PA, BQ |
| **4382000** | Charges sociales sur congés à payer | Charges sociales sur les congés payés provisionnés. | OD (clôture) |
| **4417000** | Subventions d'exploitation | Subvention d'exploitation accordée mais pas encore reçue (créance sur le financeur). | OD |
| **4421000** | Prélèvements à la source (Impôt sur le revenu) | Prélèvement à la source de l'impôt sur le revenu retenu sur les salaires, à reverser. | PA, BQ |
| **4471100** | Taxe sur les salaires | Taxe sur les salaires à payer (les associations non soumises à la TVA la paient). | PA, BQ |
| **4471300** | Participation employeurs à la formation profession continue | Contribution formation professionnelle à payer. | PA, BQ |
| **4611000** | Transfert T21 France | Opérations de transfert avec la Fédération T21 France. | OD |
| **4671XXX** | Comptes débiteurs et produits à recevoir | Créances diverses et produits à recevoir (un sous-compte par débiteur). Libellé identique à 4676000 : à clarifier. | OD |
| **4676000** | Comptes débiteurs et Produits à recevoir | Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). | OD (clôture) |
| **4686000** | Comptes créditeurs et Charges à payer | Charge de N à payer qui n'est ni un fournisseur, ni une dette sociale ou fiscale. | OD (clôture) |
| **4710000** | Comptes d’attente | Compte d'attente : opération non identifiée. À utiliser **rarement** et à **solder** avant la clôture. | BQ, OD |
| **4730000** | Comptes d’attente | Second compte d'attente (même libellé que 4710000 : à clarifier). Même règle : soldé au 31/12. | BQ, OD |
| **4860000** | Charges constatées d’avance | Charge constatée d'avance : facturée en N mais concernant N+1 (ex. : assurance avril N – mars N+1). | OD (clôture) |
| **4870000** | Produits constatés d’avance | Produit constaté d'avance : encaissé en N mais concernant N+1. | OD (clôture) |
| **4878000** | Produits constatés d’avance - Subventions | Subvention reçue en N pour une période de N+1 (ex. : année scolaire). | OD (clôture) |
| **4910000** | Dépréciations des comptes de clients | Dépréciation d'une créance client douteuse. | OD (clôture) |

## Classe 5 — Financiers

| Compte | Libellé du plan T21 | En clair / exemple | Journal habituel |
|---|---|---|---|
| **5040000** | PSB CME T21 France (parts sociales) | Parts sociales du Crédit Mutuel détenues par T21 France (« PSB CME »). Le document range les parts sociales en 27 : à clarifier. | BQ |
| **5081XXX** | CAT détaillés | Comptes à terme (CAT), un sous-compte par placement. | PL (banque placement) |
| **512XXX** | Banques | Comptes bancaires courants, un sous-compte et un journal par compte. | BQ (contrepartie automatique) |
| **5181000** | Intérêts courus à payer | Intérêts bancaires courus à payer au 31/12. | OD (clôture) |
| **5188000** | Intérêts courus à recevoir | Intérêts des placements acquis au 31/12 mais versés plus tard. | OD (clôture) |
| **5300000** | Caisse | Caisse (espèces). Le solde doit être égal au comptage physique. | CA (caisse) |
| **5800000** | Virements internes | Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. | BQ, CA, PL |

## Classe 6 — Charges

| Compte | Libellé du plan T21 | En clair / exemple | Journal habituel |
|---|---|---|---|
| **6061100** | Eau et assainissement | Facture d'eau. | AC |
| **6061200** | Energie, électricité | Facture d'électricité (exemple du document T21 : EDF). | AC |
| **6061210** | Electricité pour véhicules électriques | Recharge des véhicules électriques. | AC, BQ |
| **6061300** | Chauffage | Chauffage (gaz, fioul, réseau de chaleur). | AC |
| **6061800** | Autres fournitures non stockables | Autres fournitures non stockables. | AC |
| **6062100** | Combustibles et carburants | Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). | AC, BQ |
| **6062200** | Produits d’entretien | Produits d'entretien et d'hygiène. | AC |
| **6062300** | Fournitures d'atelier | Petites fournitures d'atelier. | AC |
| **6062400** | Fournitures administratives | Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). | AC |
| **6062410** | Relevés d'imprimante | Relevés de compteur des imprimantes (copies facturées). | AC |
| **6062500** | Fournitures scolaires, éducatives et de loisirs | Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. | AC |
| **6062800** | Autres fournitures non stockées | Autres petites fournitures. | AC |
| **6063000** | Alimentation | Alimentation (goûters, repas d'activités, événements). | AC, CA |
| **6066000** | Fournitures médicales | Fournitures médicales (trousses de secours…). | AC |
| **6068000** | Autres achats non stockés de matières et fournitures | Autres petits achats non stockés. | AC |
| **6112000** | Prestations à caractère médico-social | Prestation médico-sociale achetée à un autre établissement. | AC |
| **6122000** | Crédit-bail mobilier 1 sous-compte par contrat (véhicule) | Loyer de crédit-bail (leasing avec option d'achat), un sous-compte par contrat. | AC, BQ |
| **6132000** | Locations immobilières | Loyer des locaux. | AC |
| **6135200** | Location équipements | Location de matériel (photocopieur…). | AC |
| **6135300** | Location matériel de transport | Location de véhicule (location longue durée sans option d'achat). | AC |
| **6140000** | Charges locatives et de copropriété | Charges locatives et de copropriété refacturées par le bailleur. | AC |
| **6152100** | Maintenance et contrôle obligatoire immobilier | Contrôles obligatoires des locaux (extincteurs, électricité, ascenseur). | AC |
| **6152800** | Autres entretiens et réparations  immobiliers | Petites réparations des locaux. | AC |
| **6155800** | Entretien et réparations des autres matériel et outillages | Entretien et réparation des véhicules et du matériel. | AC |
| **6156100** | Maintenance informatique | Maintenance informatique, abonnements logiciels. | AC |
| **6156800** | Maintenance non informatique | Autres contrats de maintenance. | AC |
| **6161000** | Assurance Multirisques | Assurance multirisque des locaux. | AC |
| **6162000** | Assurance obligatoire dommage-construction | Assurance dommage-ouvrage (travaux). | AC |
| **6163000** | Assurance transport | Assurance des véhicules (flotte). | AC |
| **6165000** | Assurance Responsabilité civile | Assurance responsabilité civile. | AC |
| **6166000** | Assurance Matériels | Assurance du matériel. | AC |
| **6168800** | Assurance Autres risques | Autres assurances. | AC |
| **6170000** | Etudes et recherches | Études et recherches confiées à un tiers. | AC |
| **6182000** | Documentation générale et technique | Abonnements, revues, documentation. | AC |
| **6184000** | Concours divers (cotisations) | Cotisations à des organismes (ex. : cotisation à la Fédération, à l'URIOPSS). | AC, BQ |
| **6185000** | Frais de colloques, séminaires, conférences | Inscriptions à des colloques et séminaires. | AC |
| **6188000** | Autres frais divers | Autres frais divers. | AC |
| **6211800** | Autres personnels intérimaires - Formateurs | Formateurs intérimaires. | AC |
| **6215000** | Personnel affecté à l'établissement | Personnel mis à disposition par un autre organisme. | AC |
| **6218000** | Autres personnels extérieurs | Autre personnel extérieur (intérim). | AC |
| **6221000** | Frais de recrutement du personnel | Frais de recrutement (cabinet, annonces). | AC |
| **6223120** | Honoraires Médecin | Honoraires d'un médecin libéral. | AC (tiers LI) |
| **6223210** | Honoraires Infirmiers | Honoraires d'infirmiers libéraux. | AC (tiers LI) |
| **6223221** | Honoraires Orthophonistes | Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). | AC (tiers LI) |
| **6223222** | Honoraires Psycho-motriciens | Honoraires de psychomotriciens. | AC (tiers LI) |
| **6223223** | Honoraires Ergothérapeutes | Honoraires d'ergothérapeutes. | AC (tiers LI) |
| **6223224** | Honoraires Psychologues | Honoraires de psychologues. | AC (tiers LI) |
| **6223225** | Honoraires Kinésithérapeutes | Honoraires de kinésithérapeutes. | AC (tiers LI) |
| **6223226** | Honoraires Educateurs | Honoraires d'éducateurs libéraux. | AC (tiers LI) |
| **6226010** | Honoraires comptabilité | Honoraires de l'expert-comptable (et du commissaire aux comptes, faute de compte dédié dans le plan : à vérifier). | AC |
| **6226020** | Honoraires juridiques | Honoraires d'avocat. | AC |
| **6228000** | Autres honoraires | Autres honoraires. | AC |
| **6230000** | Publicité, publications, relations publiques | Publicité, impression de plaquettes, site internet. | AC |
| **6242800** | Transports des usagers | Transport des personnes accompagnées (taxi, transporteur). | AC |
| **6251000** | Voyages et déplacements | Indemnités kilométriques, train, péages, parkings (notes de frais). | AC (tiers SA) |
| **6255000** | Frais de déménagement | Frais de déménagement. | AC |
| **6256000** | Missions | Repas et hébergement en mission. | AC (tiers SA) |
| **6256100** | Frais Conseil d'Administration, Bénévoles, Mission CA/Représ | Frais des administrateurs bénévoles (conseil d'administration, représentation). | AC (tiers SA ou FO) |
| **6256200** | Frais formateurs | Frais de déplacement des formateurs. | AC |
| **6256300** | Missions nationales (projets) | Missions nationales liées à des projets. | AC |
| **6256700** | Missions - Journées Fédérales | Déplacements pour les journées fédérales. | AC |
| **6257000** | Réceptions | Réceptions (pot, accueil de partenaires). | AC, CA |
| **6261000** | Frais d’affranchissements | Timbres, envois postaux. | AC, BQ |
| **6262000** | Frais de télécommunication | Téléphone, internet. | AC |
| **6270000** | Services bancaires et assimilés | Frais bancaires (prélevés directement sur le relevé). | BQ |
| **6287000** | Remboursement de frais | Remboursements de frais à un autre organisme. | AC |
| **6288000** | Autres services extérieurs | Autres services extérieurs. | AC |
| **6311000** | Taxe sur les salaires | Taxe sur les salaires (calculée par la paie). | PA (automatique) |
| **6331000** | Versement de mobilité | Versement mobilité (transport), calculé par la paie. | PA |
| **6332000** | Allocation logement | Contribution au FNAL (« allocation logement »), calculée par la paie. | PA |
| **6333000** | Participation des employeurs à la formation prof. continue | Contribution à la formation professionnelle continue. | PA |
| **6335000** | Taxe d'apprentissage | Taxe d'apprentissage. | PA |
| **6351200** | Taxes foncières | Taxe foncière (si l'association est propriétaire). | AC, BQ |
| **6351300** | Autres impôts locaux | Autres impôts locaux. | AC, BQ |
| **6354000** | Droits d’enregistrement et de timbre | Droits d'enregistrement et de timbre. | BQ |
| **6358000** | Autres impôts et taxes | Autres impôts et taxes (ex. : certificat d'immatriculation). | BQ |
| **6411100** | Personnel titulaire et stagiaires - Rémunération principale | Salaires bruts des salariés en CDI (« titulaires »). | PA |
| **6411600** | Indemnités de préavis et de licenciement | Indemnités de préavis et de licenciement. | PA |
| **6411810** | Gratification des stagiaires | Gratification des stagiaires. | PA |
| **6412000** | Congés payés | Congés payés (et variation de la provision). | PA, OD |
| **6413100** | Personnel non titulaire - Rémunération principale | Salaires bruts des CDD. | PA |
| **6415200** | Personnel non médical de remplacement-Remunération principale | Salaires des remplaçants. | PA |
| **6416000** | Emplois d’insertion | Salaires des contrats aidés (emplois d'insertion). | PA |
| **6417000** | Apprentis | Salaires des apprentis. | PA |
| **6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 | **IJSS** versées par la CPAM à l'association (subrogation) : saisies au **crédit**, en banque. « Charge négative ». Ancien compte 6491000. | BQ |
| **6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 | Remboursements de la **prévoyance** pour les arrêts longs : au **crédit**, en banque. Ancien compte 6492000. | BQ |
| **6421000** | Rémunérations du personnel médical | Salaires du personnel médical salarié. | PA |
| **6451100** | Cotisations à l’URSSAF | Cotisations URSSAF (part employeur). | PA |
| **6451200** | Cotisations aux mutuelles | Cotisations mutuelle (part employeur). | PA |
| **6451210** | Cotisations aux caisses de prévoyance | Cotisations prévoyance (part employeur). | PA |
| **6451300** | Cotisations aux caisses de retraite - pers non médical | Cotisations retraite complémentaire (part employeur). | PA |
| **6451800** | Provision sur charges Congés Payés | Charges sociales sur la provision pour congés payés. | OD (clôture) |
| **6451810** | Provision sur charges Modif valeur du point | Charges sociales liées à la revalorisation de la valeur du point (convention collective). | OD |
| **6475000** | Médecine du travail | Médecine du travail. | AC |
| **6478400** | Oeuvres sociales | Œuvres sociales (chèques cadeaux, activités du personnel). | AC |
| **6479000** | Remboursement aur autres charges sociales | Remboursements d'autres charges sociales (le plan écrit « aur » pour « aux »). | BQ |
| **6488000** | Autres charges diverses de personnel | Autres charges de personnel. | AC, PA |
| **6510000** | Redevances pour concessions, brevets, licences | Redevances de licences et logiciels. | AC |
| **6524000** | Valeurs comptables des éléments d'actif cédés | Valeur restant à amortir d'une immobilisation vendue ou jetée. | IM (automatique) |
| **6544000** | Pertes sur créances irrécouvrables - exo antérieurs | Créance devenue définitivement irrécouvrable. | OD |
| **6551000** | QP de résultat sur opé groupement de coop° sociale | Quote-part de résultat dans un groupement de coopération sociale (GCSMS). | OD |
| **6556000** | Frais de siège social du gestionnaire | **Frais de siège** facturés par le siège à la structure (taux autorisé par le financeur). | OD (IS) |
| **6557000** | Frais de siège social interassociatif | Frais de siège interassociatif (siège commun à plusieurs associations). | OD |
| **6571000** | Aides financières octroyées - Conseil scientifique | Aides financières octroyées (Fédération : conseil scientifique, recherche). | AC, BQ |
| **6582000** | Pénalités, amendes fiscales et pénales | Pénalités, amendes (ex. : majoration de retard URSSAF). | BQ, OD |
| **6588000** | Charges diverses de gestion courante - autres | Autres charges de gestion courante (ex. : arrondis, petits écarts justifiés). | OD |
| **6611000** | Intêrets des emprunts | Intérêts des emprunts (exemple du document T21 : prélevés par la banque). | BQ |
| **6618000** | Autres charges d'intérêt - intérêts courus | Intérêts courus à la clôture (ICNE). | OD (clôture) |
| **6720000** | Charges sur exercices antérieurs | Charge oubliée d'un exercice antérieur. | AC, OD |
| **6811100** | Dot Amorts Immobilisations incorporelles | Amortissement de l'année des logiciels. | IM (automatique) |
| **6811200** | Dot Amorts Immobilisations corporelles | Amortissement de l'année des biens corporels. | IM (automatique) |
| **6815000** | Dotation aux provisions d'exploitation | Dotation aux provisions (risques, charges). | OD (clôture) |
| **6891000** | Report en fonds reportés | Mise en réserve de fonds reportés en fin d'année. | OD (clôture) |
| **6892100** | Report en fonds dédiés à l'investissement | Mise en fonds dédiés d'une subvention d'investissement non utilisée. | OD (clôture) |
| **6892200** | Report en fonds dédiés à l'exploitation | Mise en fonds dédiés de la part **non dépensée** d'une subvention d'exploitation affectée. | OD (clôture) |

## Classe 7 — Produits

| Compte | Libellé du plan T21 | En clair / exemple | Journal habituel |
|---|---|---|---|
| **7060000** | Prestations de services | Prestations de services vendues. | VT (automatique) |
| **7060001** | Quote-Part SIA | Quote-part SIA facturée (Fédération). | VT |
| **7060002** | Abonnement annuel OGIRYS | Abonnement annuel OGIRYS facturé (Fédération). | VT |
| **7060003** | Prestations de services Mandats de Gestion | Prestations de mandats de gestion (Fédération). | VT |
| **7060004** | Prestations de FORMATION | Prestations de formation vendues (Fédération). | VT |
| **7060005** | Prestations de services - Bulletins de paie | Bulletins de paie réalisés pour d'autres associations (Fédération). | VT |
| **7060006** | Prestations de services - Frais de gestion | Frais de gestion facturés (Fédération). | VT |
| **7060007** | Prestations de services - Campagnes de communication | Campagnes de communication facturées (Fédération). | VT |
| **7068300** | Prestations de services exterieures | Autres prestations de services. | VT |
| **7085200** | Frais pédagogiques de formation | Frais pédagogiques de formation facturés. | VT |
| **7085300** | Inscription événements | Inscriptions à des événements. | VT |
| **7085800** | Prestations délivrées usagers, accompagnant & autres tiers | Prestations facturées aux personnes accompagnées ou à des tiers. | VT |
| **7085900** | Participation frais postaux et routages | Participation aux frais d'envoi. | VT |
| **7088000** | Autres produits d'activité annexe - DOCUMENTATION | Vente de documentation. | VT |
| **7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF | **Dotation** de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. | BQ |
| **7410001** | Subvention Education Nationale | Subvention de l'Éducation nationale. | BQ |
| **7410002** | Subvention Fondation de France | Subvention de la Fondation de France. | BQ |
| **7410003** | Subvention FDVA | Subvention FDVA (fonds pour le développement de la vie associative). | BQ |
| **7410004** | Subventions OETH | Subventions OETH (emploi des travailleurs handicapés). | BQ |
| **7410005** | Subventions Malakoff | Subventions Malakoff. | BQ |
| **7410006** | Subventions Crédit Mutuel | Subventions Crédit Mutuel. | BQ |
| **7410007** | Subventions René Fournier | Subventions René Fournier. | BQ |
| **7410008** | Subvention CNSA | Subvention CNSA. | BQ |
| **7410009** | Subventions Agir sa vie | Subventions Agir sa vie. | BQ |
| **7410010** | Subventions La France s'engage | Subventions La France s'engage. | BQ |
| **7410011** | Subventions Fondation RATP | Subventions Fondation RATP. | BQ |
| **7410012** | Subventions Crédit Agricole | Subventions Crédit Agricole. | BQ |
| **7410013** | Subventions INDOSUEZ | Subventions Indosuez. | BQ |
| **7412000** | Subventions Virage Numérique | Subventions Virage Numérique. | BQ |
| **7470000** | QP des subventions d'investissement virées au résultat de l'exercice | Part de la subvention d'investissement reprise chaque année au rythme de l'amortissement du bien. | OD (clôture) |
| **7484000** | Aide forfaitaire à l’apprentissage | Aide de l'État à l'embauche d'apprentis. | BQ |
| **7488000** | Autres Subventions et participations | Autres subventions (tout financeur sans sous-compte dédié). | BQ |
| **7556000** | Siège social du gestionnaire | **Frais de siège** reçus par le siège des structures (contrepartie du 6556000). | OD (IS) |
| **7557000** | Siège social interassociatif | Frais de siège interassociatif reçus. | OD |
| **7541100** | Dons T21 France | Dons à T21 France. | BQ |
| **7541110** | Dons T21 France - Internet | Dons à T21 France reçus par internet. | BQ |
| **7541200** | Dons Autres projets | Dons pour d'autres projets. | BQ, CA |
| **7541300** | Dons recherche | Dons pour la recherche. | BQ |
| **7541400** | Dons Projet DIAE | Dons pour le projet DIAE. | BQ |
| **7541500** | Dotation Régine Clément | Dotation Régine Clément. | BQ |
| **7562100** | Cotisations fédérales | Cotisations fédérales (cotisations des associations membres à la Fédération). | VT, BQ |
| **7574000** | Produits de cessions d'immobilisations incorp et corp | Prix de vente d'une immobilisation cédée. | BQ |
| **7584000** | Remboursements de frais | Remboursements de frais reçus. | BQ |
| **7584100** | Remboursements sur frais de formation ancien compte 6498000 | Remboursement de frais de formation (OPCO). Ancien compte 6498000. | BQ |
| **7587000** | Indemnités d'assurance | Indemnité versée par l'assurance après un sinistre. | BQ |
| **7588000** | Autres produits divers de gestion courante | Autres produits divers (ex. : arrondis créditeurs). | BQ, OD |
| **7640000** | Revenus des valeurs mobilières de placement | Intérêts des placements (comptes à terme, livrets). | PL, OD |
| **7720000** | Produits sur exercices antérieurs | Produit oublié d'un exercice antérieur. | OD |
| **7780000** | Autres produits exceptionnels | Produit réellement exceptionnel (rare). | OD |
| **7817400** | Reprises sur dépréciation des créances | Reprise d'une dépréciation de créance devenue inutile. | OD (clôture) |
| **7891000** | Fonds reportés | Utilisation de fonds reportés. | OD |
| **7892100** | Fonds dédiés - Investissements | Utilisation de fonds dédiés à l'investissement. | OD |
| **7892200** | Fonds dédiés - Exploitation | Utilisation, l'année suivante, des fonds dédiés d'exploitation (quand on dépense enfin la subvention). | OD |

*Voir aussi : [la fiche du dossier](fiche_dossier_5_structures.md) et [le cours M18](cours.md).*
