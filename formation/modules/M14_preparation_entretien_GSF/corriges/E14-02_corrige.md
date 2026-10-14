# Corrigé E14-02 — Prestation ponctuelle et révision de prix rétroactive par indice : facture complémentaire (Aéroport Côte d'Azur Services)

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-02](../exercices/E14-02_prestation-ponctuelle-revision-prix-aeroport.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — La révision
La formule est contractuelle : on l'applique **exactement** (pondération, indice du bon mois, arrondi à 4 décimales). La partie fixe (0,125) représente la part du prix non indexée ; seule la part de 87,5 % suit l'indice. L'indice a progressé de 3,63 % mais le prix ne progresse que de 3,18 % : c'est normal.
Hausse de 3,18 % < 5 % : la **clause de sauvegarde ne joue pas**, la révision s'applique de plein droit.

### Question 2 — Rattachement à septembre
Le principe d'indépendance des exercices (et, pour le reporting mensuel du groupe, des périodes) impose de rattacher un produit à la période où la prestation est **exécutée** et où le droit à rémunération est **certain dans son principe et déterminable dans son montant**.
- **Rappel de révision** : la prestation de juillet à septembre est exécutée ; le contrat prévoit expressément l'application rétroactive ; l'indice est connu au 25/09 → le montant est certain → **FAE au 30/09** pour les trois mois (le rappel de juillet et d'août n'a pas été constaté dans leurs mois respectifs faute d'indice : il passe en septembre, et le contrôle de gestion doit le savoir pour ne pas interpréter une « hausse » de marge de septembre).
- **Heures complémentaires** : exécutées le 19-20/09, acceptées par écrit (BC complémentaire du 02/10, reçu **avant** l'arrêté des comptes de septembre) → **FAE au 30/09**. L'accord écrit postérieur confirme une situation existant au 30/09 (prestation réalisée à la demande du client).
- **Facture FR-2026-09-0471** : déjà émise, à enregistrer normalement.

### Question 3 — Mécanique FAE / extourne
À la clôture : D 4181 (TTC) / C 706 (HT) / C 44587 (TVA). Le 01/10, extourne automatique. Le 08/10, les factures réelles sont saisies en 411 / 706 / 44574 (TVA en attente d'encaissement). L'effet net sur octobre est nul, le produit est bien en septembre.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Rapport d'indices | 122,7 / 118,4 | 1,036318 |
| Coefficient | 0,125 + 0,875 × 1,036318 = 1,031778 → arrondi 4 déc. | **1,0318** |
| Nouveau prix mensuel | 32 600,00 × 1,0318 | **33 636,68 €** |
| Rappel mensuel | 33 636,68 − 32 600,00 | 1 036,68 € |
| Rappel juillet-septembre HT | 1 036,68 × 3 | **3 110,04 €** |
| TVA 20 % | 3 110,04 × 20 % | 622,01 € |
| TTC | | **3 732,05 €** |
| Hausse annuelle (clause de sauvegarde) | 1,0318 − 1 | 3,18 % < 5 % |
| Heures complémentaires HT | 6 h × 38,00 € | **228,00 €** |
| TVA | 228,00 × 20 % | 45,60 € |
| TTC | | 273,60 € |
| Facture FR-2026-09-0471 | 4 850,00 + 970,00 | 5 820,00 € |

Chiffre d'affaires additionnel de septembre au titre de ce client : 3 110,04 + 228,00 + 4 850,00 = **8 188,04 € HT** (en plus du forfait de 32 600,00 €).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | VT | 411ACAS | Client Aéroport Côte d'Azur Services | F FR-2026-09-0471 salon 19/09 BC-ACAS-26-0912 | 5 820,00 | |
| 30/09/2026 | VT | 706 | Prestations de services (NIC) | F FR-2026-09-0471 salon 19/09 | | 4 850,00 |
| 30/09/2026 | VT | 44574 | TVA collectée en attente d'encaissement | F FR-2026-09-0471 TVA 20 % | | 970,00 |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | FAE rappel révision 07-09/2026 ACAS | 3 732,05 | |
| 30/09/2026 | OD | 706 | Prestations de services (NIC) | FAE rappel révision 07-09/2026 ACAS | | 3 110,04 |
| 30/09/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | FAE rappel révision 07-09/2026 ACAS | | 622,01 |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | FAE 6 h compl. salon BC-ACAS-26-0987 | 273,60 | |
| 30/09/2026 | OD | 706 | Prestations de services (NIC) | FAE 6 h compl. salon BC-ACAS-26-0987 | | 228,00 |
| 30/09/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | FAE 6 h compl. salon BC-ACAS-26-0987 | | 45,60 |
| 01/10/2026 | OD | 706 | Prestations de services (NIC) | Extourne FAE rappel révision | 3 110,04 | |
| 01/10/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | Extourne FAE rappel révision | 622,01 | |
| 01/10/2026 | OD | 4181 | Clients – factures à établir | Extourne FAE rappel révision | | 3 732,05 |
| 01/10/2026 | OD | 706 | Prestations de services (NIC) | Extourne FAE heures compl. | 228,00 | |
| 01/10/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | Extourne FAE heures compl. | 45,60 | |
| 01/10/2026 | OD | 4181 | Clients – factures à établir | Extourne FAE heures compl. | | 273,60 |
| 08/10/2026 | VT | 411ACAS | Client Aéroport Côte d'Azur Services | F FR-2026-10-0012 rappel révision 07-09/2026 | 3 732,05 | |
| 08/10/2026 | VT | 706 | Prestations de services (NIC) | F FR-2026-10-0012 rappel révision 07-09/2026 | | 3 110,04 |
| 08/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | F FR-2026-10-0012 TVA 20 % | | 622,01 |
| 08/10/2026 | VT | 411ACAS | Client Aéroport Côte d'Azur Services | F FR-2026-10-0013 heures compl. BC-ACAS-26-0987 | 273,60 | |
| 08/10/2026 | VT | 706 | Prestations de services (NIC) | F FR-2026-10-0013 heures compl. | | 228,00 |
| 08/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | F FR-2026-10-0013 TVA 20 % | | 45,60 |
| | | | | **Totaux** | **17 836,95** | **17 836,95** |

## 4. Points d'attention / pièges

- **Ne pas annuler et refaire les trois factures** : une révision de prix se traite par une **facture complémentaire** (ou rectificative) référencée aux factures initiales ; refacturer les trois mois en totalité créerait un doublon chez le client.
- **Coefficient non arrondi** : 32 600,00 × 1,031778 = 33 635,95 € ; la différence (0,73 €/mois) paraît dérisoire mais le client recalculera et rejettera la facture.
- **Mauvais indice** : prendre l'indice de septembre (dernier publié) au lieu de celui de juin prévu au contrat est l'erreur classique.
- **TVA de la FAE** : sur les encaissements, elle n'est **pas** exigible au 30/09 ; elle va en 44587 (et non en 44571) et ne figure pas sur la CA3.
- **Prestation ponctuelle sans BC** (question 5) : sans bon de commande complémentaire, la facture de 228,00 € aurait été rejetée par le client (article 9). Au 30/09, le droit à rémunération aurait été **incertain** : pas de FAE (ou FAE assortie d'une analyse de risque), heures supportées en charge sans produit en face. Commercialement, l'établissement aurait dû obtenir l'accord écrit **avant** d'exécuter les heures. En revanche, la paie des salariés ayant fait les heures reste due quoi qu'il arrive.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mentions de la facture complémentaire (question 4)** : « Facture complémentaire – révision de prix au 01/07/2026 – article 6 du contrat AC-2023-004 » ; formule et valeurs d'indices (I0 = 118,4 ; I = 122,7 ; coefficient 1,0318) ; références des factures initiales FR-2026-07-0388, FR-2026-08-0405, FR-2026-09-0466 ; détail par mois (1 036,68 € HT × 3) ; mentions habituelles (SIREN client, nature : prestation de services, adresse de réalisation, échéance, pénalités, 40 €).

**Mail à Thomas Vidal :**
> Bonjour Thomas,
> Oui, les deux éléments entrent en septembre : rappel de révision 3 110,04 € HT (coefficient 1,0318, nouveau forfait 33 636,68 € HT dès octobre) et heures complémentaires 228,00 € HT (BC-ACAS-26-0987 reçu le 02/10). Je les passe en factures à établir au 30/09 ; les factures partent le 08/10. Attention pour le reporting : septembre porte 3 mois de rappel (2 073,36 € concernent juillet-août). Merci de mettre à jour le forfait dans l'ERP pour la facturation d'octobre.

**Contrôles** : tableau de suivi des révisions par contrat (date anniversaire, indice, date de publication, statut) ; revue mensuelle des FAE de plus de 60 jours (une FAE qui ne se transforme pas en facture est un produit douteux).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié) : principe d'indépendance des exercices ; comptes 4181 et 44587.
- Code de commerce art. L. 123-21 (seuls les bénéfices réalisés peuvent être inscrits) et L. 441-9 (mentions de facture).
- CGI art. 269-2-c (exigibilité de la TVA sur les prestations de services) ; CGI art. 242 nonies A de l'annexe II (mentions, factures rectificatives).
- Code monétaire et financier art. L. 112-2 : validité des clauses d'indexation (indice en relation avec l'objet du contrat).
