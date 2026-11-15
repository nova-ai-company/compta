# Corrigé E18-10 — Réviser la balance du SAVS au 30/11/2026 comme une senior

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **FNP** | Factures non parvenues. À la clôture : charges de l'année dont la facture n'est pas encore arrivée. On les enregistre quand même (compte 408) pour que l'année supporte ses vraies charges. |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N-1** | L'exercice précédent. L'année comptable d'avant (ex. : si N = 2026, N-1 = 2025). On compare souvent N et N-1 pour repérer les écarts anormaux. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PA** | Plateforme agréée — ou, dans le M18, journal de paie. Opérateur agréé par l'État (anciennement « PDP ») qui transmet les factures électroniques entre entreprises et envoie les données à l'administration. Dans le module M18, PA est le code du journal des salaires, alimenté automatiquement par EIG RH. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 1150120** | RAN ESMS sous gestion contrôlée (créditeur) (plan T21). Report à nouveau excédentaire d'un ESSMS financé par une autorité de tarification (« gestion contrôlée ») : excédent pas encore affecté. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 2183000** | Matériel de bureau et matériel informatique (plan T21). Ordinateurs, imprimantes, téléphones durables au-dessus du seuil d'immobilisation. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4110000** | Clients (comptes de tiers CL…) (plan T21). Centralisation des clients. On saisit dans les comptes CL… |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4310000** | Sécurité sociale (plan T21). URSSAF : cotisations à payer. Crédité par la paie, débité au paiement. |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4730000** | Comptes d’attente (plan T21). Second compte d'attente (même libellé que 4710000 : à clarifier). Même règle : soldé au 31/12. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6062400** | Fournitures administratives (plan T21). Fournitures de bureau : stylos, carnets, papier (exemple du document T21 : note de frais Durand). |
    | **Compte 6062800** | Autres fournitures non stockées (plan T21). Autres petites fournitures. |
    | **Compte 6132000** | Locations immobilières (plan T21). Loyer des locaux. |
    | **Compte 6156100** | Maintenance informatique (plan T21). Maintenance informatique, abonnements logiciels. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6223224** | Honoraires Psychologues (plan T21). Honoraires de psychologues. |
    | **Compte 6411100** | Personnel titulaire et stagiaires - Rémunération principale (plan T21). Salaires bruts des salariés en CDI (« titulaires »). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6556000** | Frais de siège social du gestionnaire (plan T21). Frais de siège facturés par le siège à la structure (taux autorisé par le financeur). |
    | **Compte 7312170** | Dotation du SAVS (dossier M18, numéro fictif). Le plan T21 ne prévoit que 7312130 (services pour enfants). Pour le SAVS, une autre subdivision 7312xxx est nécessaire : à vérifier dans le plan de l'association. |
    | **FOBUREAU26** | Compte fournisseur fournitures de bureau (dossier M18). Fournitures administratives (6062400). |
    | **FOGARAGEMARTIN** | Compte fournisseur Garage Martin (dossier M18). Garage de Valence : entretien et achat des véhicules. Regroupé dans 4010000. |
    | **FOINFORHONE** | Compte fournisseur informatique (dossier M18). Maintenance informatique (6156100) et matériel (2183000 si immobilisé). |
    | **FOTOTALCARTE** | Compte fournisseur carte carburant (dossier M18). Relevé mensuel des cartes carburant des véhicules de service (6062100). |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIBENALI** | Compte libéral : psychologue (dossier M18). Groupes de parole du SAVS (6223224). |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
    | **Report à nouveau** | Résultat gardé en attente. Excédent (110) ou déficit (119) reporté sur un budget suivant. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-10](../exercices/E18-10_revision-balance-analyse-senior.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

!!! abstract "En clair"
    Une balance ne se lit pas ligne à ligne de haut en bas. On la **questionne** : chaque solde est-il dans le **bon sens** ? Est-il **cohérent** avec l'an dernier et avec le budget ? Les comptes de **tiers** sont-ils justifiés par les comptes individuels ? Les comptes qui doivent être **à zéro** le sont-ils ? Les **liaisons** avec le siège concordent-elles ? Ce n'est qu'ensuite qu'on « descend » dans le grand livre pour trouver la cause.

### Question 1 — La méthode d'une senior, en 8 étapes

1. **Vérifier que la balance est complète** : toute la paie de novembre déversée (journal PA), toutes les banques saisies jusqu'au 30/11, les IS du siège reçues (frais de siège, loyer, télécom). Une balance incomplète donne de faux écarts.
2. **Rapprocher la trésorerie** : 5123000 = relevé bancaire, ou écart entièrement expliqué par des opérations en suspens. Tant que la banque n'est pas rapprochée, rien n'est fiable.
3. **Contrôler le sens normal de chaque solde** (tableau ci-dessous) et les comptes qui doivent être **à zéro** (4710000, 4730000, 5800000) ou **ne pas exister** (aucun 445 dans le plan T21).
4. **Rapprocher les tiers** : chaque compte de centralisation (4010000, 4011000, 4248000) = somme de sa balance auxiliaire ; aucune ligne « sans compte de tiers » ; pas de compte FO, LI ou SA débiteur sans explication ; lettrage à jour.
5. **Rapprocher les comptes de liaison** : 1840000 du SAVS = opposé exact du 1849200 du siège.
6. **Revue analytique des charges et produits** : comparer N et N-1, réalisé et budget proratisé (ici × 11/12). Fixer un **seuil** d'investigation (par exemple 10 % **et** 500 €) pour ne pas se noyer.
7. **Calculer quelques ratios** simples : charges sociales / salaires, coût mensuel moyen, dotation reçue / dotation notifiée.
8. **Descendre dans le grand livre** pour chaque alerte, trouver la pièce, écrire la cause, proposer l'écriture corrective, et **documenter** (feuille de révision).

### Question 2 — Sens normal des comptes

| Famille | Sens normal | Ce qu'on voit au SAVS | Verdict |
|---|---|---|---|
| Report à nouveau créditeur 1150120 | Créditeur (excédent antérieur non affecté) | C 12 400,00 | Normal |
| Liaison 1840000 | Libre, mais **opposé** du 1849200 du siège | C 41 210,30 contre D 42 297,80 au siège | **Écart** (question 5) |
| Immobilisations 21xxxxx / amortissements 28xxxxx | Débiteur / créditeur | D 8 750,00 / C 4 120,00 | Sens normal, mais **contenu** à vérifier (350,00 € de destructeur) |
| Fournisseurs, libéraux, NDF (401x, 4248000) | Créditeur (dettes) | Créditeurs **en total**, mais la balance auxiliaire montre deux FO **débiteurs** | **Alerte** |
| Sécurité sociale 4310000 | Créditeur (cotisations à payer) | C 18 450,00 | Normal (cotisations de novembre payées en décembre) |
| TVA 4456600 | **N'existe pas** dans le plan T21 | D 186,40 | **Anomalie** |
| Attente 4710000, virements internes 5800000 | **Zéro** | D 742,00 et D 1 500,00 | **Anomalies** |
| Banque 5123000 | Débiteur (argent disponible) | D 64 380,55 | Sens normal, mais **non rapprochée** |
| Charges 6xxxxxx | Débiteur | Débiteurs, **sauf** 6419000 qui doit être créditeur | **Anomalie** sur 6419000 |
| 6419000 IJSS | **Créditeur** (« charge négative », document T21) | **D** 1 860,00 (N-1 : C 4 210,00) | **Anomalie** |
| Dotation 7312170 | Créditeur | C 632 500,00 = 11 × 57 500,00 | Normal |

### Question 3 — Comparaisons N / N-1 / budget et ratios

| Compte | Réalisé N | N-1 | Budget × 11/12 | Écart / budget | Lecture |
|---|---|---|---|---|---|
| 7312170 Dotation | 632 500,00 | 618 750,00 | 632 500,00 | 0,00 | 11 douzièmes reçus : **conforme** |
| 6132000 Loyer (IS) | 14 850,00 | 14 520,00 | 14 850,00 | 0,00 | 11 × 1 350,00 (25 % de 5 400,00) : **conforme** |
| 6556000 Frais de siège | 25 875,00 | 27 225,00 | 28 462,50 | **− 2 587,50** | Exactement **un mois** de moins : alerte |
| 6223221 Orthophonie | 1 224,00 | 0,00 | 0,00 | **+ 1 224,00** | Le SAVS (adultes) n'a **pas** d'orthophoniste conventionné : alerte |
| 6062400 Fournitures administratives | 2 184,60 | 1 412,30 | 1 375,00 | **+ 809,60** (+ 58,9 %) | Alerte → grand livre : une ligne de TVA a été sortie de la facture d'octobre |
| 6062100 Carburants | 12 846,30 | 11 920,10 | 12 375,00 | + 471,30 (+ 3,8 %) | Sous le seuil ; + 7,8 % sur N-1 : à commenter (prix, kilomètres) |
| 6223224 Psychologues | 9 600,00 | 8 640,00 | 10 560,00 | − 960,00 | 10 factures de 960,00 € : celle de **novembre** n'est pas arrivée. Décalage normal (FNP si toujours absente au 31/12) |
| 6419000 IJSS | **D** 1 860,00 | C 4 210,00 | C 2 750,00 | − 4 610,00 | Sens inversé : alerte |
| 6411100 Salaires | 318 640,00 | 309 815,00 | 322 300,00 | − 3 660,00 (− 1,1 %) | Normal |

**Ratio charges sociales / salaires** : 98 420,00 / 318 640,00 = **30,9 %** (N-1 : 95 640,00 / 309 815,00 = 30,9 %). Stable : la paie déversée est cohérente. *Un ratio qui saute de plusieurs points signale souvent un déversement de paie incomplet ou une régularisation de cotisations.*

**Ratio dotation** : 632 500,00 / 690 000,00 = 91,7 % = 11/12 ✓.

### Question 4 — Les tiers

- **Total de la pièce 2** : 3 589,20 − 1 872,00 = 1 717,20 € créditeur = solde du 4010000 ✓ (la balance auxiliaire « tombe » sur la générale), **mais** elle contient une ligne « **écritures sans compte de tiers** » de 1 248,00 €. C'est une saisie **directement sur le compte de centralisation 4010000**, ce qui est **interdit** (document T21, classe 40). Le grand livre le confirme : la facture Info Rhône F-IRS-0612 du 18/06 a été saisie sur 4010000, puis payée le 30/06 sur **FOINFORHONE**. D'où un FOINFORHONE **débiteur** de 1 248,00 € qui n'est **pas** un trop-payé : la facture est simplement « ailleurs ».
- **FOGARAGEMARTIN débiteur de 624,00 €** : la facture F-GM-2026-388 a été payée **deux fois** (12/09 et 03/10). Ici, c'est un vrai trop-payé : de l'argent à récupérer.
- **FOTOTALCARTE créditeur de 1 928,40 €** = relevé de septembre (742,00) + relevé d'octobre (1 186,40). Or le prélèvement de septembre de 742,00 € est parti… en **4710000** (attente). Les deux anomalies se corrigent par **une seule** écriture.
- **LIDUPONT dans le SAVS** : Claire Dupont est l'orthophoniste conventionnée du **SESSAD** (enfants). Sa facture d'octobre (36 séances × 34,00 = 1 224,00 €) a été saisie dans la **mauvaise structure**. Conséquence : le SAVS paierait une charge du SESSAD, et le Département financerait une dépense de l'ARS.

### Question 5 — Le compte de liaison, au centime

Écart : 42 297,80 (siège, D) − 41 210,30 (SAVS, C) = **1 087,50 €**.

Deux causes, de sens contraires :

| Cause | Effet au siège (1849200) | Effet au SAVS (1840000) | Effet sur l'écart |
|---|---|---|---|
| Frais de siège de novembre saisis au siège le 30/11, miroir absent au SAVS | + 2 587,50 au débit | rien | + 2 587,50 |
| Virement du 16/10 : saisi en 1849200 au siège, mais en **5800000** au SAVS | − 1 500,00 (crédit) | rien (le 1840000 n'a pas été débité) | − 1 500,00 |
| **Total** | | | **+ 1 087,50** ✓ |

> 💡 Réflexe senior : un écart de liaison n'est presque jamais « une » erreur. Cherchez d'abord les **montants ronds et récurrents** (frais de siège mensuels, remboursements de trésorerie) dans les deux grands livres, mois par mois.

## 2. Calculs (détaillés, chaque montant justifié)

| Contrôle | Calcul | Résultat |
|---|---|---|
| Frais de siège attendus au 30/11 | 2 587,50 × 11 | 28 462,50 € (comptabilisés : 25 875,00 € = 10 mois) |
| Orthophonie | 36 séances × 34,00 | 1 224,00 € |
| Facture Bureau Vallée F-BV-26-4471 | 932,00 + 186,40 | 1 118,40 € TTC (la charge réelle, puisque la TVA n'est pas récupérable) |
| Écart bancaire | 68 100,55 − 64 380,55 | 3 720,00 € = 2 × 1 860,00 (une recette de 1 860,00 € saisie comme une dépense) |
| Destructeur de documents | 350,00 € TTC < seuil de 500,00 € TTC | Charge, pas immobilisation |
| Liaison après correction | 41 210,30 − 1 500,00 + 2 587,50 | 42 297,80 € = 1849200 du siège ✓ |

## 3. Écritures comptables

*Les comptes de tiers sont indiqués entre parenthèses derrière le compte de centralisation. Dans les journaux de banque, la ligne 5123000 est générée automatiquement par le logiciel ; elle est reproduite pour montrer l'équilibre.*

**Anomalie 1 — Facture saisie directement sur 4010000 (interdit) ; FOINFORHONE débiteur en apparence**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | OD | 4010000 | Fournisseurs FO (ligne sans compte de tiers) | Reclassement F-IRS-0612 saisie sans tiers le 18/06 | | 1 248,00 | |
| 30/11/2026 | SAV | OD | 4010000 | Fournisseurs FO (tiers FOINFORHONE) | FOINFORHONE – maintenance logiciels – F-IRS-0612 – 06/2026 | | | 1 248,00 |
| | | | | | **Total** | | **1 248,00** | **1 248,00** |

Puis **lettrer** FOINFORHONE (facture 1 248,00 au crédit avec virement du 30/06 au débit). Le compte 6156100 était juste : seule la contrepartie était mal saisie. *Demander que le logiciel **bloque** la saisie directe sur 4010000, 4011000, 4248000 et 4110000.*

**Anomalie 2 — FOGARAGEMARTIN débiteur : facture payée deux fois**

Pas d'écriture au 30/11 : la créance sur le garage est **réelle** et le compte FO débiteur la montre. Action : demander au garage Martin le remboursement (ou un avoir à imputer sur la prochaine facture). Écriture au remboursement (exemple au 10/12/2026) :

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 10/12/2026 | SAV | BQSAV | 5123000 | Crédit Mutuel – SAVS | Remboursement double paiement F-GM-2026-388 (ligne automatique) | | 624,00 | |
| 10/12/2026 | SAV | BQSAV | 4010000 | Fournisseurs FO (tiers FOGARAGEMARTIN) | FOGARAGEMARTIN – remb. double paiement F-GM-2026-388 | | | 624,00 |
| | | | | | **Total** | | **624,00** | **624,00** |

*Si rien n'est récupéré à la clôture, on garde la créance (en la reclassant en 4676000 « Comptes débiteurs » si l'expert-comptable le souhaite) ; on ne la passe **pas** en charge sans décision.*

**Anomalie 3 — 4710000 non soldé (prélèvement carte carburant de septembre)**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | OD | 4010000 | Fournisseurs FO (tiers FOTOTALCARTE) | FOTOTALCARTE – prélèvement 22/09 – relevé 09/2026 | | 742,00 | |
| 30/11/2026 | SAV | OD | 4710000 | Comptes d'attente | Reclassement prélèvement 22/09 TOTALENERGIES | | | 742,00 |
| | | | | | **Total** | | **742,00** | **742,00** |

Puis lettrer FOTOTALCARTE (relevé de septembre 742,00 / prélèvement 742,00). Il reste C 1 186,40 (relevé d'octobre, prélevé en novembre ? à vérifier sur le relevé de décembre).

**Anomalie 4 — 5800000 non nul : remboursement au siège passé par 58 au lieu de la liaison**

Le 58 sert aux mouvements entre comptes de trésorerie **d'une même structure** ; un virement entre le SAVS et le siège passe **toujours** par les comptes de liaison (fiche, § 5).

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | OD | 1840000 | Liaison Siège | Reclassement virement 16/10 vers siège – remb. IS T3 | | 1 500,00 | |
| 30/11/2026 | SAV | OD | 5800000 | Virements internes | Reclassement virement 16/10 vers siège | | | 1 500,00 |
| | | | | | **Total** | | **1 500,00** | **1 500,00** |

**Anomalie 5 — 6419000 débiteur : IJSS saisie comme une dépense**

Le 14/10, la CPAM a **versé** 1 860,00 € ; la ligne a été saisie au **débit** de 6419000, donc le logiciel a **crédité** la banque : la banque en comptabilité est trop basse de 2 × 1 860,00 = 3 720,00 €, exactement l'écart du rapprochement. Correction dans le journal de banque (pour que le rapprochement retrouve ses lignes) :

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | BQSAV | 6419000 | Remboursements sur rémunération du personnel - IJSS | Annulation saisie erronée du 14/10 – IJSS Mme Roche | 20-SAVS | | 1 860,00 |
| 30/11/2026 | SAV | BQSAV | 5123000 | Crédit Mutuel – SAVS | Annulation saisie erronée du 14/10 (ligne automatique) | | 1 860,00 | |
| 30/11/2026 | SAV | BQSAV | 6419000 | Remboursements sur rémunération du personnel - IJSS | CPAM – IJSS Mme Roche – arrêt 09/2026 – reçu 14/10 | 20-SAVS | | 1 860,00 |
| 30/11/2026 | SAV | BQSAV | 5123000 | Crédit Mutuel – SAVS | CPAM – IJSS Mme Roche (ligne automatique) | | 1 860,00 | |
| | | | | | **Total** | | **3 720,00** | **3 720,00** |

*Selon les habitudes du logiciel, on peut aussi modifier directement la ligne du 14/10 si la période n'est pas clôturée. Garder une trace (pièce de correction) dans tous les cas.*

**Anomalie 6 — 2183000 : un destructeur de 350,00 € immobilisé sous le seuil**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | OD | 6062800 | Autres fournitures non stockées | FOBUREAU26 – destructeur – F-BV-26-4502 – sous seuil 500 € | 20-SAVS | 350,00 | |
| 30/11/2026 | SAV | OD | 2183000 | Matériel de bureau et matériel informatique | Reclassement destructeur F-BV-26-4502 en charge | | | 350,00 |
| | | | | | **Total** | | **350,00** | **350,00** |

**Et supprimer la fiche dans EIG IMMOS**, sinon le journal IM générera une dotation aux amortissements à la clôture sur un bien qui n'est plus à l'actif (la comptabilité et la base des immobilisations doivent toujours concorder).

**Anomalie 7 — Un compte 4456600 apparaît : la TVA a été séparée à tort**

L'association ne récupère pas la TVA : la facture F-BV-26-4471 va en charge pour **1 118,40 € TTC**. De plus, le compte 4456600 **n'existe pas** dans le plan T21 : quelqu'un l'a créé « à la volée ».

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | OD | 6062400 | Fournitures administratives | FOBUREAU26 – TVA non récupérable – F-BV-26-4471 | 20-SAVS | 186,40 | |
| 30/11/2026 | SAV | OD | 4456600 | TVA déductible (compte hors plan T21) | Reclassement TVA F-BV-26-4471 en charge | | | 186,40 |
| | | | | | **Total** | | **186,40** | **186,40** |

Puis **supprimer ou bloquer** le compte 4456600 et vérifier les autres structures (une même personne a pu faire la même erreur ailleurs).

**Anomalie 8 — Une charge du SESSAD (orthophonie) dans le SAVS**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | AC | 4011000 | Libéraux LI (tiers LIDUPONT) | Annulation LIDUPONT F2026-10 saisie dans le SAVS par erreur | | 1 224,00 | |
| 30/11/2026 | SAV | AC | 6223221 | Honoraires Orthophonistes | Annulation LIDUPONT F2026-10 saisie dans le SAVS par erreur | 20-SAVS | | 1 224,00 |
| 30/11/2026 | SES | AC | 6223221 | Honoraires Orthophonistes | LIDUPONT – orthophonie – 36 séances – F2026-10 – 10/2026 | 10-SESSAD | 1 224,00 | |
| 30/11/2026 | SES | AC | 4011000 | Libéraux LI (tiers LIDUPONT) | LIDUPONT – orthophonie – 36 séances – F2026-10 – 10/2026 | | | 1 224,00 |
| | | | | | **Total** | | **2 448,00** | **2 448,00** |

*La facture n'avait pas été payée (LIDUPONT créditeur dans le SAVS) : on la sort du SAVS et on la saisit dans le SESSAD, qui la paiera. Si elle avait été payée par la banque du SAVS, il aurait fallu une IS entre SAVS et SESSAD (via le siège) en plus. Vérifier aussi que la facture n'a pas **déjà** été saisie dans le SESSAD (doublon).*

**Anomalies 9 et 10 — Frais de siège de novembre absents et liaison non concordante**

| Date | Livres | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|---|
| 30/11/2026 | SAV | OD | 6556000 | Frais de siège social du gestionnaire | Frais de siège 11/2026 – IS reçue du siège | 20-SAVS | 2 587,50 | |
| 30/11/2026 | SAV | OD | 1840000 | Liaison Siège | Frais de siège 11/2026 – IS reçue du siège | | | 2 587,50 |
| | | | | | **Total** | | **2 587,50** | **2 587,50** |

Avec l'écriture de l'anomalie 4, le 1840000 du SAVS passe à 41 210,30 − 1 500,00 + 2 587,50 = **42 297,80 € créditeur** = 1849200 du siège ✓.

### Question 7 — Soldes corrigés et rapprochement

| Compte | Intitulé | Solde débiteur | Solde créditeur | Commentaire |
|---|---|---|---|---|
| 1840000 | Liaison Siège | | 42 297,80 | = 1849200 du siège |
| 2183000 | Matériel de bureau et informatique | 8 400,00 | | Sans le destructeur |
| 4010000 | Fournisseurs FO | | 975,20 | FOBUREAU26 C 412,80 + FOTOTALCARTE C 1 186,40 − FOGARAGEMARTIN D 624,00 |
| 4011000 | Libéraux LI | | 960,00 | LIBENALI seul |
| 4456600 | (compte à supprimer) | 0,00 | | |
| 4710000 | Comptes d'attente | 0,00 | | |
| 5123000 | Crédit Mutuel – SAVS | 68 100,55 | | = relevé : rapprochement **sans écart** |
| 5800000 | Virements internes | 0,00 | | |
| 6062400 | Fournitures administratives | 2 371,00 | | Commande importante d'octobre : à commenter |
| 6062800 | Autres fournitures non stockées | 350,00 | | Destructeur |
| 6223221 | Honoraires Orthophonistes | 0,00 | | Charge transférée au SESSAD |
| 6419000 | Remboursements IJSS | | 1 860,00 | Sens normal |
| 6556000 | Frais de siège social du gestionnaire | 28 462,50 | | = budget × 11/12 |

## 4. Points d'attention / pièges

- **Se contenter du total** de la balance auxiliaire : elle « tombe » sur le 4010000 et pourtant elle cache une saisie interdite et un double paiement. Il faut lire **chaque ligne**.
- **Corriger FOINFORHONE par un remboursement fictif** : non, le fournisseur ne doit rien. Il faut reclasser la facture sur le bon tiers.
- **Solder le 4710000 vers une charge** « pour faire propre » : interdit tant qu'on n'a pas identifié la pièce. Ici, la charge carburant était **déjà** comptabilisée par le relevé : la passer en charge aurait créé un **doublon**.
- **Passer l'écart de liaison en charge ou en produit** : jamais. Un écart de liaison a **toujours** une cause précise à trouver dans les deux comptabilités.
- **Oublier EIG IMMOS** après avoir sorti un bien de la classe 2 : la dotation de fin d'année le remettrait dans les comptes.
- **6419000 « charge négative »** : son solde normal est **créditeur**. Un débit est presque toujours une erreur de sens, ou une reprise par la paie à analyser avec le service paie.
- **Comparer au budget sans proratiser** : la balance est à 11 mois, le budget est annuel ; ici on compare au budget × 11/12. Pour une charge **non linéaire** (assurance payée en avril), le prorata n'a pas de sens : on compare au montant annuel.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Feuille de révision** (une ligne par anomalie) conservée dans le dossier de clôture : compte, montant, cause, pièce, écriture, date, qui a corrigé, qui a validé.

**Actions de fond** (éviter que cela recommence) :

1. Demander à l'éditeur ou à l'administrateur d'EIG de **bloquer la saisie directe** sur les comptes de centralisation et de **verrouiller la création de comptes** (le 4456600 n'aurait jamais dû pouvoir être créé).
2. Faire le **lettrage** des fournisseurs **chaque mois** : un double paiement se voit tout de suite.
3. Faire le **rapprochement des liaisons** chaque mois avec le siège, avant de lancer les remboursements de trésorerie.
4. Rappeler aux personnes qui saisissent les banques : **recette = crédit** de la ligne saisie (IJSS, dotations), et un virement vers une autre structure = **1840000**, jamais 5800000.
5. Ajouter au contrôle mensuel : « 6556000 = 2 587,50 × nombre de mois » et « 7312170 = 57 500,00 × nombre de mois ».

**Mail à Hélène Ferrand :**

> « Bonjour Madame Ferrand, voici la revue de la balance du SAVS au 30/11/2026. J'ai relevé 10 anomalies, toutes corrigées ou en cours (tableau joint, avec les écritures et les pièces). Les principales : (1) une IJSS de 1 860,00 € saisie en dépense, qui expliquait tout l'écart de rapprochement bancaire (3 720,00 €) ; (2) un écart de liaison de 1 087,50 € avec le siège, dû aux frais de siège de novembre non reçus (2 587,50 €) et à un remboursement au siège passé en 5800000 (1 500,00 €) ; (3) une facture d'orthophonie du SESSAD (1 224,00 €) saisie dans le SAVS, transférée au SESSAD ; (4) une facture saisie directement sur le 4010000 et une TVA séparée sur un compte 4456600 créé hors plan. Un point reste ouvert : le double paiement de 624,00 € au garage Martin, dont j'ai demandé le remboursement. Je propose aussi de bloquer dans EIG la saisie sur les comptes de centralisation et la création de comptes. Bien cordialement. »

## 6. Références

- Documents internes Trisomie 21 France (30/04/2026) : comptes de centralisation 401XXXX (saisie interdite), classe 47 et 58 (soldés en fin d'exercice), classe 18 (IS), 6419 (« charges négatives » au crédit), journaux de banque (IJSS en 6419 au crédit) ; plan comptable T21 (aucun compte 445).
- Fiche du dossier M18 : seuil d'immobilisation de 500,00 € TTC (hypothèse), frais de siège (taux fictif), règle « jamais de 58 entre structures ».
- Plan comptable général (règlement ANC n° 2014-03 modifié) : définition des immobilisations corporelles et possibilité de comptabiliser en charges les biens de faible valeur, selon la politique de l'entité.
