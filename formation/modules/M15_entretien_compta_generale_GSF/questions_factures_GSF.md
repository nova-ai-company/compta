# Les factures du quotidien chez GSF : questions et pièges

*Module M15 — complément de la banque de questions. Une entreprise de propreté comme GSF reçoit et émet toujours les **mêmes familles de factures** : produits d'entretien, intérim, sous-traitance, location de matériel, carburant, contrats de nettoyage mensuels… En entretien, le recruteur vous en montre une et demande : « **Vous la passez comment ?** ». Puis il ajoute le détail qui piège.*

*Exemples chiffrés sur la filiale **fictive** « **GSF Riviera SAS** » (Nice). Les questions déjà traitées dans la banque principale sont signalées par leur numéro (Q09, Q18…) : relisez-les en complément.*

> 🟢 **En clair :** chaque réponse est cachée. Lisez la facture, **dites à voix haute le compte de charge (ou de produit), le compte de TVA et le compte de tiers**, puis le piège. Ensuite, cliquez pour comparer.

## Le tableau à connaître par cœur

| Facture | Compte | TVA déductible / collectée | Tiers |
|---|---|---|---|
| Produits d'entretien, sacs, consommables | 6063 | 44566 (bien : à la facture) | 401 |
| Vêtements de travail, EPI | 6063 *(ou 6068 selon le plan)* | 44566 | 401 |
| Carburant (cartes carburant) | 6061 | 44566, **100 % utilitaire / 80 % voiture particulière** | 401 |
| Personnel intérimaire | 6211 | 4456x en attente (service : au paiement) | 401 |
| Sous-traitance de nettoyage | 611 | 4456x en attente, ou **autoliquidation** si fin de chantier | 401 |
| Location de matériel, LLD de véhicules | 6135 | 4456x en attente (rien sur une voiture particulière) | 401 |
| Contrat de maintenance | 6156 | 4456x en attente | 401 |
| Loyer de l'agence / charges locatives | 6132 / 614 | 4456x en attente (si le bailleur a opté) | 401 |
| Assurances | 616 | **aucune TVA** | 401 |
| Honoraires (avocat, expert) | 6226 | 4456x en attente | 401 |
| Matériel durable > 500 € HT | 2154 / 2182 / 2183 | **44562** | **404** |
| Contrat de nettoyage, prestation ponctuelle | 706 | **44574** en attente d'encaissement | 411 |
| Revente de fournitures au client | 707 *(ou 708 selon le plan)* | **44571** directement (bien) | 411 |

> 💡 Réflexe senior : avant le compte, posez-vous **deux questions** : « C'est un **bien** ou un **service** ? » (cela décide du moment de la TVA) et « Ça sert **plus d'un an** ? » (charge ou immobilisation). La moitié des pièges tombe avec ces deux questions.

---

## 1. Factures fournisseurs (F01-F12)

### F01 — ⭐ Facture de produits d'entretien avec remise et frais de port
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** Azur Hygiène Distribution, produits d'entretien 2 400,00 € HT, remise 10 % (− 240,00 €), frais de port 60,00 €. Total HT 2 220,00 € ; TVA 20 % 444,00 € ; TTC 2 664,00 €.

    **En 30 secondes :** ce sont des **biens consommés** dans le mois : compte **6063**. La remise est sur la facture : je saisis **directement le net** (2 160,00 €). Le port va en 6241 (ou dans le 6063, selon le plan de comptes du groupe). C'est un bien : TVA déductible **tout de suite** en 44566.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6063 Fournitures d'entretien et de petit équipement | 2 160,00 | |
    | 6241 Transports sur achats | 60,00 | |
    | 44566 TVA déductible sur autres biens et services | 444,00 | |
    | 401 Fournisseurs | | 2 664,00 |

    **Le piège :** comptabiliser la remise à part (en produit). Une remise **sur la facture** se déduit directement. Et ne pas oublier l'**établissement** (ETB061 Nice) en analytique. *(Voir Q09, Q11.)*

### F02 — ⭐ Facture d'intérim
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** agence d'intérim, 160 heures × 24,80 € = 3 968,00 € HT ; TVA 793,60 € ; TTC 4 761,60 €. Agent de propreté en remplacement d'un salarié en arrêt.

    **En 30 secondes :** compte **6211 Personnel intérimaire**. C'est un **service** : la TVA est déductible au **paiement** (compte de TVA en attente).

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6211 Personnel intérimaire | 3 968,00 | |
    | 4456x TVA déductible en attente *(sous-compte selon le plan de comptes)* | 793,60 | |
    | 401 Fournisseurs | | 4 761,60 |

    **Les pièges :**

    - la mettre en **641** : l'intérimaire n'est **pas** salarié de GSF ;
    - saisir sans contrôler les **heures** sur le relevé validé par le chef d'établissement (160 h facturées pour 152 h faites = 198,40 € HT payés en trop) ;
    - oublier l'**attestation de vigilance URSSAF** : obligatoire dès 5 000 € HT par contrat, à redemander tous les six mois. *(Voir Q16.)*

### F03 — ⭐ Facture de sous-traitance de nettoyage : normale ou autoliquidée ?
??? success "Réponse modèle (cliquez pour afficher)"
    **Cas 1, nettoyage courant :** un sous-traitant nettoie un site client pour le compte de GSF : 6 500,00 € HT + TVA 1 300,00 € = 7 800,00 €.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 611 Sous-traitance générale | 6 500,00 | |
    | 4456x TVA déductible en attente | 1 300,00 | |
    | 401 Fournisseurs | | 7 800,00 |

    **Cas 2, nettoyage de fin de chantier :** le sous-traitant intervient sur un chantier de construction. Sa facture est **HT**, avec la mention « Autoliquidation » : 4 000,00 € HT. C'est **GSF** qui déclare la TVA, et la déduit en même temps.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 611 Sous-traitance générale | 4 000,00 | |
    | 44566 TVA déductible autoliquidée *(sous-compte selon le plan de comptes)* | 800,00 | |
    | 401 Fournisseurs | | 4 000,00 |
    | 4457x TVA due autoliquidée *(sous-compte selon le plan de comptes)* | | 800,00 |

    **Les pièges :**

    - « La facture n'a pas de TVA, donc je ne passe pas de TVA » : **faux**, il faut l'autoliquider (et la déclarer sur la CA3) ;
    - appliquer l'autoliquidation à du **nettoyage courant** de bureaux : elle ne vise que le nettoyage **lié à des travaux immobiliers** (position à suivre, *à vérifier*) ;
    - payer un sous-traitant sans **attestation de vigilance** à jour (au-delà de 5 000 € HT) : GSF peut être tenue **solidairement** de ses dettes sociales. *(Voir Q32.)*

### F04 — Location d'une autolaveuse pour un mois
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** loueur de matériel, autolaveuse du 01/10 au 31/10/2026, 380,00 € HT + TVA 76,00 € = 456,00 €.

    **En 30 secondes :** c'est une **location**, pas un achat : compte **6135 Locations mobilières**. Service : TVA en attente jusqu'au paiement.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6135 Locations mobilières | 380,00 | |
    | 4456x TVA déductible en attente | 76,00 | |
    | 401 Fournisseurs | | 456,00 |

    **Les pièges :**

    - l'**immobiliser** parce que « c'est une autolaveuse » : GSF n'en est pas propriétaire ;
    - une location facturée **à cheval sur deux exercices** (15/12 au 15/01) : à la clôture, la moitié de janvier passe en **charge constatée d'avance** (486).

### F05 — ⭐ Relevé de cartes carburant : utilitaires et voiture de fonction
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** relevé mensuel des cartes carburant (gazole) : utilitaires 900,00 € HT + TVA 180,00 € ; voiture particulière du responsable d'agence 200,00 € HT + TVA 40,00 €. Total TTC 1 320,00 €.

    **En 30 secondes :** compte **6061 Fournitures non stockables**. La TVA sur le gazole est déductible à **100 % pour un utilitaire** et à **80 % pour une voiture particulière** (*taux à vérifier chaque année*). Les 20 % non déductibles restent en **charge**.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6061 Fournitures non stockables (carburant) | 1 108,00 | |
    | 44566 TVA déductible sur autres biens et services | 212,00 | |
    | 401 Fournisseurs | | 1 320,00 |

    Calcul : TVA déductible = 180,00 + 40,00 × 80 % = 212,00 € ; charge = 900,00 + 200,00 + 8,00 (TVA non récupérable) = 1 108,00 €.

    **Les pièges :**

    - tout déduire à 100 % (ou à 0 %) **sans séparer** les véhicules ;
    - confondre avec le **véhicule lui-même** : l'achat ou la location d'une voiture particulière n'ouvre **aucun** droit à déduction, même si son carburant est déductible à 80 %. *(Voir Q30.)*

### F06 — Loyer de LLD : utilitaire ou voiture particulière ?
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** loyer mensuel d'un utilitaire en LLD, 520,00 € HT + TVA 104,00 € = 624,00 €.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6135 Locations mobilières | 520,00 | |
    | 4456x TVA déductible en attente | 104,00 | |
    | 401 Fournisseurs | | 624,00 |

    Si c'était une **voiture particulière** : 6135 au débit **624,00 €** (TTC), sans TVA déductible.

    **Les pièges :**

    - l'**immobiliser** : en comptes sociaux, la LLD reste une location ;
    - récupérer la TVA sur le loyer d'une voiture particulière « par habitude ». *(Voir Q49.)*

### F07 — Facture de 60 tenues de travail : 1 920 € HT, on immobilise ?
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** 60 tenues (blouse + pantalon) × 32,00 € HT = 1 920,00 € HT ; TVA 384,00 € ; TTC 2 304,00 €.

    **En 30 secondes :** **non**. Le seuil de 500 € HT s'apprécie **par bien**, pas par facture : une tenue vaut 32,00 €. Ce sont des fournitures, et elles s'usent vite : **charge** (6063).

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6063 Fournitures d'entretien et de petit équipement | 1 920,00 | |
    | 44566 TVA déductible sur autres biens et services | 384,00 | |
    | 401 Fournisseurs | | 2 304,00 |

    **Le piège :** se laisser impressionner par le **total** de la facture. C'est la **valeur unitaire** et la **durée d'utilisation** qui décident. *(Voir Q01.)*

### F08 — Une facture avec une machine et des accessoires
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** autolaveuse 8 500,00 € HT + 2 jeux de brosses de rechange 180,00 € HT + livraison 150,00 € HT. Total HT 8 830,00 € ; TVA 1 766,00 € ; TTC 10 596,00 €.

    **En 30 secondes :** je **découpe** la facture. La machine **et sa livraison** (frais nécessaires à la mise en service) sont une immobilisation : 8 650,00 € en **2154**. Les brosses de rechange sont des consommables : 180,00 € en **6063**.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 2154 Matériel industriel | 8 650,00 | |
    | 6063 Fournitures d'entretien et de petit équipement | 180,00 | |
    | 44562 TVA déductible sur immobilisations | 1 730,00 | |
    | 44566 TVA déductible sur autres biens et services | 36,00 | |
    | 404 Fournisseurs d'immobilisations | | 10 380,00 |
    | 401 Fournisseurs | | 216,00 |

    **Les pièges :**

    - tout immobiliser, ou tout passer en charge, sans découper ;
    - mettre la livraison en 624 : elle fait partie du **coût** de la machine ;
    - utiliser 401 / 44566 pour la machine au lieu de **404 / 44562** ;
    - oublier de créer la fiche dans le **fichier des immobilisations** (date de mise en service, durée, établissement). *(Voir Q43.)*

### F09 — Contrat de maintenance annuel facturé d'avance
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** maintenance du parc d'autolaveuses du 01/10/2026 au 30/09/2027, 1 200,00 € HT + TVA 240,00 € = 1 440,00 €, reçue en octobre.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6156 Maintenance | 1 200,00 | |
    | 4456x TVA déductible en attente | 240,00 | |
    | 401 Fournisseurs | | 1 440,00 |

    Au 31/12/2026, seuls 3 mois sur 12 concernent 2026 : 9/12 × 1 200,00 = **900,00 €** de charge constatée d'avance.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 486 Charges constatées d'avance | 900,00 | |
    | 6156 Maintenance | | 900,00 |

    **Le piège :** laisser les 1 200,00 € en charge 2026. Autre piège : la confondre avec une **réparation** (6155), qui remet un bien en état ponctuellement. *(Voir Q61.)*

### F10 — Avis d'échéance du loyer de l'agence
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** loyer du 1er trimestre 2027 des locaux de l'agence, payable d'avance, reçu le 15/12/2026 : loyer 4 500,00 € HT + provision sur charges 600,00 € HT ; TVA 20 % 1 020,00 € (le bailleur a **opté** pour la TVA) ; TTC 6 120,00 €.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6132 Locations immobilières | 4 500,00 | |
    | 614 Charges locatives et de copropriété | 600,00 | |
    | 4456x TVA déductible en attente | 1 020,00 | |
    | 401 Fournisseurs | | 6 120,00 |

    Au 31/12/2026 : tout le trimestre concerne 2027 → 486 au débit 5 100,00 € / 6132 au crédit 4 500,00 € et 614 au crédit 600,00 €.

    **Les pièges :**

    - déduire une TVA alors que le bailleur **n'a pas opté** : sans mention de TVA sur l'avis, il n'y a rien à déduire ;
    - passer le **dépôt de garantie** (première facture du bail) en charge : c'est une **créance**, compte **275** ;
    - un « avis d'échéance » n'est pas toujours une facture : vérifiez qu'il comporte les **mentions** d'une facture avant de déduire la TVA.

### F11 — Facture d'assurance de la flotte de véhicules
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** prime annuelle du 01/04/2026 au 31/03/2027, 4 800,00 € (dont taxe sur les conventions d'assurance).

    | Compte | Débit | Crédit |
    |---|---|---|
    | 616 Primes d'assurances | 4 800,00 | |
    | 401 Fournisseurs | | 4 800,00 |

    Au 31/12/2026 : 3 mois concernent 2027 → 3/12 × 4 800,00 = **1 200,00 €** en charge constatée d'avance (486 / 616).

    **Les pièges :**

    - chercher de la **TVA** : l'assurance en est **exonérée**. La taxe d'assurance n'est **pas** récupérable, elle reste en charge ;
    - oublier la CCA sur une prime à cheval sur deux exercices.

### F12 — Note d'honoraires d'avocat (recouvrement d'un client)
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** cabinet d'avocats, honoraires 1 500,00 € HT + TVA 300,00 € = 1 800,00 € ; débours (frais d'huissier avancés) 85,00 € sans TVA. Total 1 885,00 €.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 6226 Honoraires | 1 500,00 | |
    | 6227 Frais d'actes et de contentieux | 85,00 | |
    | 4456x TVA déductible en attente | 300,00 | |
    | 401 Fournisseurs | | 1 885,00 |

    **Les pièges :**

    - calculer de la TVA sur les **débours** : ils sont refacturés à l'euro près, sans TVA ;
    - oublier que les honoraires versés sont à déclarer en fin d'année (**DAS2**) au-delà d'un seuil par bénéficiaire (on retient 1 200 € TTC par an, *valeur à vérifier chaque année*) : le compte 6226 doit donc être **bien alimenté**, sans y mélanger d'autres frais.

---

## 2. Factures clients (F13-F19)

### F13 — ⭐ La facture mensuelle d'un contrat de nettoyage
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** nettoyage des bureaux d'un client, octobre 2026, forfait 9 600,00 € HT + TVA 1 920,00 € = 11 520,00 €. GSF Riviera **n'a pas opté** pour les débits.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 411 Clients | 11 520,00 | |
    | 706 Prestations de services | | 9 600,00 |
    | 44574 TVA collectée en attente d'encaissement | | 1 920,00 |

    À l'encaissement : 512 au débit / 411 au crédit 11 520,00 €, **et** 44574 au débit / 44571 au crédit 1 920,00 €.

    **Les pièges :**

    - créditer **44571** dès la facture : sur une prestation de services, la TVA est due à l'**encaissement** ;
    - oublier le **virement** 44574 → 44571 à l'encaissement : la CA3 sera fausse ;
    - octobre facturé début novembre : à la clôture du mois d'octobre, il faut une **FAE** (voir F19). *(Voir Q18.)*

### F14 — Facture à un hôpital public via Chorus Pro
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** même écriture que F13 (411 / 706 / 44574). La différence est dans le **dépôt** : la facture est déposée sur **Chorus Pro** avec les références exigées par l'acheteur public (numéro d'engagement, code service).

    **En 30 secondes :** le délai de paiement court à partir de la **réception** de la facture conforme par l'acheteur public (on retient 30 jours pour l'État et les collectivités, 50 jours pour les établissements publics de santé, *à vérifier*). En cas de retard : **intérêts moratoires** + indemnité forfaitaire de **40 €**, dus automatiquement.

    **Les pièges :**

    - une facture **rejetée** sur Chorus Pro (code service manquant) n'est **pas reçue** : le délai ne court pas. Le client « ne paie pas », mais c'est GSF qui doit corriger ;
    - relancer le client sans **regarder le statut** de la facture dans Chorus Pro ;
    - annuler la facture rejetée en la supprimant : si elle a été émise avec un numéro, on l'annule par un **avoir** puis on réémet (la numérotation doit rester continue). *(Voir Q24.)*

### F15 — ⭐ Nettoyage de fin de chantier pour un constructeur
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** GSF Riviera, sous-traitante d'une entreprise du BTP, facture le nettoyage de fin de chantier d'un immeuble neuf : 4 000,00 € HT, **sans TVA**, mention « **Autoliquidation** ».

    | Compte | Débit | Crédit |
    |---|---|---|
    | 411 Clients | 4 000,00 | |
    | 706 Prestations de services | | 4 000,00 |

    **En 30 secondes :** c'est le **client** (le constructeur) qui déclare la TVA. GSF ne collecte rien, mais doit porter ce chiffre d'affaires sur la **CA3** dans la ligne des opérations autoliquidées.

    **Les pièges :**

    - facturer **avec TVA** « parce que c'est du nettoyage » : le client refusera la facture ;
    - à l'inverse, appliquer l'autoliquidation au nettoyage **courant** des bureaux d'un client du BTP : son activité ne change rien, c'est la **nature de la prestation** qui compte (*à vérifier selon la position en vigueur*) ;
    - oublier la **mention** « Autoliquidation » sur la facture.

### F16 — Une facture mixte : prestation + fournitures revendues
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** nettoyage du mois 3 000,00 € HT + fournitures sanitaires fournies au client (papier, savon) 400,00 € HT ; TVA 20 % 680,00 € ; TTC 4 080,00 €.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 411 Clients | 4 080,00 | |
    | 706 Prestations de services | | 3 000,00 |
    | 707 Ventes de marchandises *(ou 708 selon le plan)* | | 400,00 |
    | 44574 TVA collectée en attente d'encaissement (service) | | 600,00 |
    | 44571 TVA collectée (bien) | | 80,00 |

    **En 30 secondes :** deux natures, donc **deux moments** de TVA. Pour la prestation, la TVA est due à l'encaissement. Pour les fournitures (des **biens**), elle est due à la **livraison** : 44571 tout de suite.

    **Les pièges :**

    - tout mettre en 706 et en 44574 : la TVA sur les fournitures est déclarée trop tard ;
    - enregistrer la refacturation **en diminution de l'achat** (crédit 6063) : c'est une **vente**.

### F17 — Un avoir sur une facture déjà payée
??? success "Réponse modèle (cliquez pour afficher)"
    **La situation :** le client a payé sa facture de septembre. On découvre qu'une vitrerie de 500,00 € HT n'a pas été réalisée → avoir de 600,00 € TTC.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 709 Rabais, remises et ristournes accordés *(ou 706)* | 500,00 | |
    | 44571 TVA collectée | 100,00 | |
    | 411 Clients | | 600,00 |

    **En 30 secondes :** la facture est **encaissée**, donc sa TVA est déjà passée en 44571 : l'avoir la diminue en **44571** (et pas en 44574). Le client devient **créditeur** de 600,00 € : on l'impute sur sa prochaine facture ou on le rembourse.

    **Les pièges :**

    - régulariser la TVA dans le **mauvais compte** (44574 alors que la facture est payée) ;
    - laisser un client **créditeur** à la clôture : c'est une **dette**, reclassée en **4191** au passif. *(Voir Q24, Q25.)*

### F18 — ⭐ Facture d'acompte au démarrage d'un contrat
??? success "Réponse modèle (cliquez pour afficher)"
    **La situation :** remise en état d'un site après travaux, 10 000,00 € HT. Le client verse 30 % à la commande : 3 000,00 € HT + 600,00 € TVA = 3 600,00 €.

    | Étape | Compte | Débit | Crédit |
    |---|---|---|---|
    | Encaissement de l'acompte | 512 Banque | 3 600,00 | |
    | | 4191 Clients – avances et acomptes reçus | | 3 000,00 |
    | | 44571 TVA collectée | | 600,00 |
    | Facture finale | 411 Clients | 8 400,00 | |
    | | 4191 Clients – avances et acomptes reçus | 3 000,00 | |
    | | 706 Prestations de services | | 10 000,00 |
    | | 44574 TVA collectée en attente d'encaissement | | 1 400,00 |

    **En 30 secondes :** pour un service, la TVA de l'acompte est due **à l'encaissement**. Sur la facture finale, je ne collecte la TVA que sur le **solde** : 7 000,00 € × 20 % = 1 400,00 €.

    **Les pièges :**

    - collecter **2 000,00 €** de TVA sur la facture finale : la TVA de l'acompte serait payée deux fois ;
    - réclamer 12 000,00 € au client en oubliant de **déduire l'acompte**. *(Voir Q22.)*

### F19 — La prestation d'octobre sera facturée en novembre
??? success "Réponse modèle (cliquez pour afficher)"
    **La situation :** le forfait d'octobre (9 600,00 € HT) n'est facturé que le 03/11. On clôture le mois d'octobre.

    | Compte | Débit | Crédit |
    |---|---|---|
    | 4181 Clients – factures à établir | 11 520,00 | |
    | 706 Prestations de services | | 9 600,00 |
    | 44587 TVA sur factures à établir | | 1 920,00 |

    Extourne le 01/11, puis saisie de la vraie facture.

    **Les pièges :**

    - oublier l'**extourne** : le chiffre d'affaires d'octobre est compté deux fois ;
    - mettre la TVA en 44571 : elle n'est pas encore due, la facture n'existe pas. *(Voir Q20.)*

---

## 3. Les pièges « sur la pièce elle-même » (F20-F26)

*Ici, le recruteur ne teste pas le compte : il teste votre **contrôle**. La bonne réponse commence souvent par « **Je ne la saisis pas telle quelle** ».*

### F20 — ⭐ Un petit fournisseur envoie sa facture en PDF par mail en octobre 2026. Vous l'acceptez ?
??? success "Réponse modèle (cliquez pour afficher)"
    **En 30 secondes :** **oui, si c'est une PME**. Depuis le **01/09/2026**, toutes les entreprises doivent pouvoir **recevoir** des factures électroniques via une **plateforme agréée (PA)**. Mais l'obligation d'**émettre** ne s'applique qu'aux grandes entreprises et aux ETI : les PME et TPE ont jusqu'au **01/09/2027**. Une PME peut donc encore envoyer un PDF.

    **Le piège :** l'inverse pour GSF. Le groupe est une **grande entreprise** : **ses** factures de vente doivent être émises en format électronique via une PA **depuis le 01/09/2026**, avec les nouvelles mentions (SIREN du client, nature de l'opération, option pour les débits le cas échéant). Un PDF envoyé par mail n'est plus une facture valable pour GSF.

### F21 — La facture est adressée à « GSF Méditerranée » au lieu de « GSF Riviera »
??? success "Réponse modèle (cliquez pour afficher)"
    **En 30 secondes :** je ne la saisis pas chez GSF Riviera. La TVA n'est déductible que par la société **au nom de laquelle** la facture est établie. Je demande au fournisseur un **avoir** et une **nouvelle facture** au bon nom (avec le bon SIREN).

    **Le piège :** « C'est le même groupe, ce n'est pas grave. » Chaque filiale est une **société distincte**, avec sa propre comptabilité et sa propre CA3. *(Voir Q31.)*

### F22 — Le TTC de la facture est faux
??? success "Réponse modèle (cliquez pour afficher)"
    **La facture :** HT 1 232,50 € ; TVA 20 % 246,50 € ; TTC indiqué **1 497,00 €** (au lieu de 1 479,00 €).

    **En 30 secondes :** je ne la saisis pas, et je ne la corrige pas moi-même. Je la **bloque** et je demande une **facture rectificative**. Je vérifie toujours HT × taux = TVA, et HT + TVA = TTC.

    **Le piège :** saisir le TTC indiqué « parce que c'est ce que le fournisseur réclame » : on paierait 18,00 € de trop. *(Voir E15-01.)*

### F23 — Une facture de nettoyage avec une TVA à 10 %
??? success "Réponse modèle (cliquez pour afficher)"
    **En 30 secondes :** le nettoyage de locaux relève du taux **normal de 20 %**. Je bloque la facture et je demande une **rectificative**. Je ne déduis pas 20 % « parce que c'est le bon taux » : on ne déduit que la TVA **correctement facturée**.

    **Le piège :** se dire « ça m'arrange, je déduis moins ». Une TVA mal facturée est une anomalie à **tracer**, pas à arranger. *(Voir Q34.)*

### F24 — ⭐ Deux factures identiques du même fournisseur
??? success "Réponse modèle (cliquez pour afficher)"
    **La situation :** deux factures Azur Hygiène de 2 664,00 € TTC, l'une reçue via la PA, l'autre par courrier : même numéro F26-1214.

    **En 30 secondes :** c'est un **doublon** (même numéro, même fournisseur, même montant). Je n'en saisis qu'une. Pour les repérer, je contrôle la **clé fournisseur + numéro de facture** (l'ERP bloque souvent les doublons) et, dans Excel, un **NB.SI** sur cette clé.

    **Le piège :** deux factures **différentes** au même montant (deux livraisons identiques dans le mois) : ce n'est pas un doublon. Je vérifie le **numéro** et le **bon de livraison**, pas seulement le montant. *(Voir Q87, E15-12.)*

### F25 — Une facture d'intérim sans relevé d'heures validé
??? success "Réponse modèle (cliquez pour afficher)"
    **En 30 secondes :** je peux l'enregistrer (la dette existe), mais je **bloque le paiement** tant que le chef d'établissement n'a pas validé le **service fait**. C'est le principe du **rapprochement à trois** : commande, preuve du service fait (relevé d'heures, bon de livraison), facture.

    **Le piège :** payer à l'échéance « pour ne pas être en retard » sans validation : si les heures sont fausses, il faudra courir après un avoir.

### F26 — ⭐ En janvier, vous recevez une facture d'électricité de décembre
??? success "Réponse modèle (cliquez pour afficher)"
    **En 30 secondes :** si les comptes de décembre sont **ouverts**, je la saisis sur décembre. S'ils sont **clôturés**, la charge aurait dû être provisionnée en **facture non parvenue** (408) au 31/12. Je la saisis en janvier, et l'extourne de la FNP annule la charge provisionnée.

    **Écriture au 31/12 (FNP) :** 6061 au débit 850,00 € ; 44586 TVA sur factures non parvenues au débit 170,00 € ; 4081 au crédit 1 020,00 €. Extourne le 01/01.

    **Le piège :** passer la facture en charge sur janvier **sans FNP** : décembre est sous-évalué et janvier surévalué. Et ne pas la jeter parce qu'elle est « en retard » : la TVA reste déductible dans les délais. *(Voir Q60, Q85.)*

---

## À retenir en 30 secondes

- **Bien ou service ?** Bien → TVA tout de suite (44566 / 44571). Service → TVA au **paiement** (en attente : 4456x / 44574), sauf option pour les débits.
- **Plus d'un an et plus de 500 € HT par bien ?** → immobilisation, **404 / 44562**, et la livraison est dans le coût.
- **Pas de TVA sur la facture ?** → assurance (exonérée), débours, ou **autoliquidation** à passer soi-même.
- **Voiture particulière** : aucune TVA sur l'achat ou le loyer, **80 %** sur le carburant (*à vérifier chaque année*).
- **À cheval sur deux exercices** (loyer, assurance, maintenance) → **charge constatée d'avance** à la clôture.
- **Une anomalie sur la pièce** (mauvais nom, mauvais taux, TTC faux, doublon) → je **bloque**, je demande une **rectificative**, je ne corrige jamais moi-même.
