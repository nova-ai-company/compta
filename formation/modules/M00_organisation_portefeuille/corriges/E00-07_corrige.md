# Corrigé E00-07 — Checklist de clôture adaptée à trois clients

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E00-07](../exercices/E00-07_checklist-cloture-3-clients.md)

## 1. Analyse

Adapter une checklist, c'est répondre à trois questions pour chaque ligne :
1. **Le cycle existe-t-il chez ce client ?** Le Dr Lambert n'a ni stock, ni TVA, ni créances clients au sens comptable.
2. **Le référentiel est-il le même ?** Le Dr Lambert tient une comptabilité de **trésorerie** (recettes encaissées / dépenses payées) : les notions de cut-off, de FNP, de CCA et de FAE ne s'appliquent pas, sauf option pour les créances-dettes.
3. **Quels sont les risques propres au secteur ?** TVA sur la marge et stock de VO pour le garage ; fonds des mandants et fait générateur des honoraires pour l'agence ; SCM et frais mixtes pour le médecin.

Une checklist adaptée est **plus courte** sur ce qui est sans objet et **plus précise** sur ce qui compte.

## 2. Calculs

Pas de calcul. Le volume indicatif des checklists adaptées est le suivant :

| Client | Lignes de la checklist type (27) | Supprimées | Modifiées | Ajoutées | Total adapté |
|---|---|---|---|---|---|
| C03 Garage Martin | 27 | 1 (A3) | 6 | 6 | 32 |
| C05 Dr Lambert | 27 | 15 | 6 | 6 | 18 |
| C22 ImmoPlus | 27 | 2 (A3, D1) | 4 | 5 | 30 |

## 3. Écritures comptables

Sans objet : il s'agit d'outils de méthode. Les écritures correspondant à chaque point sont traitées dans les modules techniques (stocks M08, révision M12, cas particuliers M13).

### 3.1 C03 — Garage Martin (clôture au 30/09/2026)

| Réf. | Statut | Contenu adapté | Justification |
|---|---|---|---|
| A2 | Modifiée | PV de caisse au 30/09 **+ contrôle des encaissements en espèces sur les ventes de VO** (plafonds légaux, identité de l'acheteur) | Activité VO : ventes à des particuliers, risque espèces / LCB-FT |
| A3 | **Supprimée** | — | Pas de VMP |
| C3 | Modifiée | FAE : réparations terminées non facturées au 30/09 (ordres de réparation clos) ; **débours cartes grises** en comptes de tiers, hors CA | Cut-off atelier ; les cartes grises ne sont pas du CA |
| C5 | Modifiée | Rapprochement du CA et des CA3 **en distinguant** : atelier (TVA 20 % sur le prix), VO achetés à des pros (TVA sur le prix), VO achetés à des **particuliers** (TVA **sur la marge**) | Risque principal de TVA du dossier |
| D1 | Modifiée | Inventaire des **pièces détachées** (inventaire tournant : contrôle de la dernière valorisation, pièces obsolètes) **et des VO** (liste par VIN, prix d'achat + frais de remise en état, **dépréciation des VO en stock depuis plus de 6 mois** selon la cote) | Deux stocks, deux méthodes |
| D2 | **Ajoutée** | Véhicules de démonstration : immobilisation (utilisés durablement) ou stock (destinés à la vente) ; cohérence avec l'usage réel | Corner case du dossier |
| E1 | Modifiée | Immobilisations : pont élévateur, valises de diagnostic ; vérifier qu'aucun VO destiné à la vente n'est immobilisé | — |
| H4 | **Ajoutée** | Registre de police des VO (livre d'achat-vente) rapproché du stock | Obligation réglementaire + preuve des achats à des particuliers |
| H5 | **Ajoutée** | Factures VO sur la marge : mention obligatoire « régime particulier – biens d'occasion », **pas de TVA apparente** | Mention obligatoire |
| I1 | Modifiée | Provision pour **garanties** (VO vendus avec garantie, statistiques de retours) et litiges clients | Corner case |
| I3 | **Ajoutée** | Taxe sur les véhicules de démonstration ou de prêt, si applicable (à vérifier) | — |
| J4 | **Ajoutée** | Dossier servant de base au cas de synthèse : **note de synthèse détaillée** pour Hélène | Organisation du cabinet |
| J5 | **Ajoutée** | Échéances : liasse avant le **31/12/2026**, solde IS au **15/01/2027**, AG au plus tard le **31/03/2027** | Calendrier |

**3 points à plus fort risque :**
1. **TVA sur la marge** : contrôle par sondage de 10 dossiers VO (achat à un particulier : certificat de cession + facture de vente ; marge = prix de vente TTC − prix d'achat, TVA = marge × 20/120). Pièce : fichier de calcul de la marge par véhicule, rapproché des CA3.
2. **Stock de VO** : liste des véhicules au 30/09 rapprochée du livre de police et de la balance ; dépréciation des VO de plus de 6 mois sur la base de la **cote professionnelle** à la date de clôture. Pièce : liste signée et cotes imprimées.
3. **Cut-off atelier** : ordres de réparation ouverts ou clos autour du 30/09. Pièce : extraction du logiciel atelier.

### 3.2 C05 — Dr Sophie Lambert (2035, comptabilité de trésorerie)

| Réf. | Statut | Contenu adapté | Justification |
|---|---|---|---|
| A1 | Modifiée | Rapprochement bancaire au 31/12 **+ contrôle que toutes les recettes sont sur le compte professionnel** ; recettes rapprochées des **relevés SNIR / relevés de tiers payant** de la CPAM | En BNC, la recette est l'encaissement : le rapprochement avec les relevés de l'Assurance maladie est le contrôle d'exhaustivité |
| A2 | Modifiée | Recettes en espèces : cahier de recettes journalier | — |
| A3, B1, B2, B3, C1, C2, C3, C4, D1, F1, F3, G1, G2, H1, H2 | **Supprimées** | — | Trésorerie, pas de stock, pas de salarié, **exonérée de TVA**, pas d'IS |
| C5 | Modifiée | Rapprochement des recettes déclarées (2035) avec les relevés CPAM, les ROSP et les forfaits, et avec la déclaration de l'AGA | — |
| E1 | Modifiée | Immobilisations : **échographe** (amortissement sur la base TTC, puisque la TVA n'est pas récupérable) ; véhicule : option barème kilométrique **ou** frais réels (pas de cumul) | TVA non récupérable → coût TTC |
| F2 | Modifiée | Emprunt : seuls les **intérêts** et l'assurance sont déductibles ; le capital ne l'est pas | Erreur fréquente en trésorerie |
| H3 | Modifiée | CFE, cotisations **URSSAF et CARMF** (part obligatoire déductible ; Madelin dans les limites) | — |
| K1 | **Ajoutée** | **Quote-part SCM** (1/3) : rapprochement des appels de fonds versés avec la **2036** de la SCM ; ventilation des frais par nature | Corner case |
| K2 | **Ajoutée** | **Dépenses mixtes** (téléphone, domicile, véhicule) : quote-part professionnelle justifiée | Risque fiscal |
| K3 | **Ajoutée** | Frais de repas : seule la fraction excédant le seuil forfaitaire est déductible (seuils à vérifier chaque année) ; blanchissage | — |
| K4 | **Ajoutée** | Prélèvements personnels identifiés (non déductibles) | — |
| K5 | **Ajoutée** | Transmission à l'**AGA** et visa ; échéance de la 2035 en mai 2027 | — |
| K6 | **Ajoutée** | Option éventuelle pour les **créances-dettes** : vérifier qu'elle n'a pas été exercée (sinon, la checklist redevient d'engagement) | — |

**3 points à plus fort risque :**
1. **Exhaustivité des recettes** : relevés CPAM et mutuelles (tiers payant), règlements directs et espèces, rapprochés des encaissements bancaires. Pièce : relevé annuel de l'Assurance maladie + tableau de rapprochement.
2. **Quote-part SCM** : déduction de la **quote-part des frais réels**, et non des appels de fonds. Pièce : 2036 de la SCM et état de répartition.
3. **Dépenses mixtes et véhicule** : choix entre barème et frais réels, puis justificatif de la quote-part professionnelle. Pièce : carte grise, kilométrage, note de calcul.

### 3.3 C22 — ImmoPlus (clôture au 31/12/2026)

| Réf. | Statut | Contenu adapté | Justification |
|---|---|---|---|
| A1 | Modifiée | Rapprochement des comptes **propres** de l'agence **et**, séparément, du **compte séquestre** | Deux trésoreries à ne jamais mélanger |
| A3 | **Supprimée** | — | Pas de VMP |
| A4 | **Ajoutée** | **Rapprochement fonds mandants** au 31/12 : solde du compte séquestre = total des comptes mandants (propriétaires, locataires, dépôts de garantie) ± suspens justifiés ; **tout écart négatif** (fonds manquants) est remonté immédiatement | Obligation légale + garantie financière ; oubli en 2025 |
| C3 | Modifiée | **Honoraires de transaction** : produit à l'**acte authentique**, jamais au compromis ; liste des compromis signés au 31/12 sans acte = pas de produit | Erreur de 18 000 € HT en 2025 |
| C5 | Modifiée | Rapprochement CA / TVA **en excluant** les loyers encaissés pour les mandants (jamais du CA) | — |
| C6 | **Ajoutée** | Honoraires de gestion : rapprochés des encaissements de loyers du logiciel de gestion (taux du mandat × loyers) | Contrôle de vraisemblance |
| D1 | **Supprimée** | — | Pas de stock |
| B4 | **Ajoutée** | **Commissions des agents commerciaux** : charges rattachées aux actes de l'exercice ; DAS2 | Rattachement + obligation déclarative |
| H4 | **Ajoutée** | Carte professionnelle (T et G) et attestation de **garantie financière** en cours de validité | Condition d'exercice |
| I1 | Modifiée | Litiges (mandants, locataires, acquéreurs), et sinistres couverts par la RC professionnelle | — |
| J5 | **Ajoutée** | Dépôts de garantie : reçus pour le compte des bailleurs → en comptes de tiers (mandants), pas en dettes de l'agence | Classement |

**3 points à plus fort risque :**
1. **Fonds des mandants** : rapprochement au 31/12, signé par le gérant. Pièces : relevé séquestre, balance mandants du logiciel, état des suspens.
2. **Fait générateur des honoraires de transaction** : rapprocher les honoraires comptabilisés de la liste des **actes authentiques** de l'exercice (attestations du notaire). Pièce : listing des actes.
3. **Commissions des agents commerciaux** : rattachement à l'acte et DAS2. Pièce : contrats d'agents et décomptes.

## 4. Points d'attention / pièges

- Cocher « N/A » sans réfléchir est **pire** que supprimer la ligne : on croit avoir contrôlé.
- Chez le Dr Lambert, appliquer des réflexes d'engagement (FNP, CCA) dans une 2035 en trésorerie **fausse** le résultat.
- Chez ImmoPlus, le rapprochement des fonds mandants n'est pas une simple ligne de checklist : un **écart négatif** (argent manquant) est une alerte grave, à remonter le jour même à Hélène.
- Chaque ligne cochée doit renvoyer à une **feuille de travail** référencée (ex. « D1 → WP D-02 »).

## 5. Ce qu'un senior ferait en plus

- **Classement** : la checklist **adaptée** (le « modèle client ») va dans le **dossier permanent**, pour être réutilisée chaque année. La checklist **remplie** de l'exercice va dans le **dossier annuel**.
- **Nommage** : `2026-09-30_C03_GarageMartin_Checklist-cloture_v1.xlsx`, `2026-12-31_C05_Lambert_Checklist-2035_v1.xlsx`, `2026-12-31_C22_ImmoPlus_Checklist-cloture_v1.xlsx`.
- **Revue** : Hélène commence par les **3 points à risque** de chaque client, avec les pièces justificatives. Chaque point de revue est soldé par écrit dans la checklist (colonne « réponse »).
- Mettre à jour le modèle client après chaque clôture, en y intégrant les erreurs de l'année (ex. compromis / acte chez ImmoPlus).

## 6. Références
- CGI, art. 297 A (TVA sur la marge des biens d'occasion) ; CGI, art. 93 (BNC : dépenses nécessitées par l'exercice de la profession) ; règles de la comptabilité de trésorerie des titulaires de BNC (recettes encaissées / dépenses payées, option possible pour les créances-dettes).
- Loi n° 70-9 du 2 janvier 1970 (« loi Hoguet ») et son décret d'application : carte professionnelle, garantie financière, maniement des fonds des mandants.
- PCG : cut-off, dépréciations, provisions ; cours M00 § 11 (méthodes de travail).
