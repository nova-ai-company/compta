# Corrigé E18-05 — Saisir le relevé bancaire d'octobre du SESSAD et faire le rapprochement

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CB** | Carte bancaire. Paiement par carte. Les encaissements CB arrivent en banque nets de commission. |
    | **CGI** | Code général des impôts. Le code qui contient toutes les règles fiscales (TVA, IS, IR…). « art. 39 CGI » = article 39 de ce code. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IBAN** | Numéro de compte bancaire international. Identifiant unique d'un compte bancaire, nécessaire pour un virement. |
    | **IJ** | Indemnités journalières. Voir IJSS : sommes versées par la CPAM pendant un arrêt de travail. |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SEPA** | Espace unique de paiement en euros. Normes européennes de virements et prélèvements en euros. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **VIR** | Virement. Abréviation utilisée sur les relevés bancaires. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 1640000** | Emprunts auprès des Ets de crédit (plan T21). Capital restant dû des emprunts bancaires. Crédité au déblocage, débité à chaque remboursement de capital. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4248000** | Salariés - NDF (comptes de tiers SA…) (plan T21). Centralisation des notes de frais des salariés. On saisit dans les comptes SA… |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 6062100** | Combustibles et carburants (plan T21). Carburant (carte carburant, ou ticket CB sans facture saisi directement en banque). |
    | **Compte 6262000** | Frais de télécommunication (plan T21). Téléphone, internet. |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6419100** | Remboursements sur rémunération du personnel - Prévoyance ancien compte 6492000 (plan T21). Remboursements de la prévoyance pour les arrêts longs : au crédit, en banque. Ancien compte 6492000. |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7541100** | Dons T21 France (plan T21). Dons à T21 France. |
    | **Compte 7541110** | Dons T21 France - Internet (plan T21). Dons à T21 France reçus par internet. |
    | **Compte 7541200** | Dons Autres projets (plan T21). Dons pour d'autres projets. |
    | **Compte 7588000** | Autres produits divers de gestion courante (plan T21). Autres produits divers (ex. : arrondis créditeurs). |
    | **FOBUREAU26** | Compte fournisseur fournitures de bureau (dossier M18). Fournitures administratives (6062400). |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOORANGE** | Compte fournisseur télécom (dossier M18). Contrat unique de téléphonie et internet facturé au siège, réparti en IS selon les ETP. |
    | **FOTOTALCARTE** | Compte fournisseur carte carburant (dossier M18). Relevé mensuel des cartes carburant des véhicules de service (6062100). |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **LIMOREAUPSY** | Compte libéral : psychomotricien (dossier M18). Séances de psychomotricité du SESSAD (6223222). |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **SAGIRARD** | Compte salarié : Thomas Girard (dossier M18). Notes de frais d'un éducateur du SESSAD. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **Lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-05](../exercices/E18-05_releve-bancaire-sessad.md)

> *Cadre de formation : association, personnes, sociétés et documents fictifs.*

!!! abstract "En clair"
    Dans le journal de banque, vous ne tapez **qu'une seule ligne par opération** : celle de « l'autre côté » (le fournisseur, la charge, la dotation…). Le logiciel ajoute tout seul la ligne de banque 5122000. Avant de taper, vous posez toujours la question : **cette opération appartient-elle vraiment au SESSAD ?** Ici, deux lignes n'appartiennent pas au SESSAD (Orange et le don de Mme Leroy) : on ne les met pas en charge ou en produit du SESSAD, on les fait passer par les comptes de liaison ou par un compte d'attente.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — « Débit pour les dépenses » : ce que vous tapez, ce que le logiciel génère

Le journal **BQSES** est un journal à **contrepartie automatique** : son compte de banque (5122000) est fixé dans le paramétrage. Vous ne saisissez que la ligne de **contrepartie**.

Ligne 4 du relevé : virement de 1 245,00 € à l'orthophoniste Claire Dupont.

- Vous tapez : **LIDUPONT au débit 1 245,00**. La dette envers la libérale disparaît (elle était au crédit depuis la saisie de sa facture en AC).
- Le logiciel génère : **5122000 au crédit 1 245,00**. L'argent sort de la banque.

La phrase du document T21 parle donc de **la ligne que vous tapez**. Une dépense = ligne tapée au **débit** (la banque, elle, est créditée). Une recette = ligne tapée au **crédit** (la banque est débitée). Si vous pensez « banque », vous inversez tout.

### Question 2 — Le compte de chaque ligne

| N° | Opération | Ce que vous tapez | Sens de la ligne tapée | Analytique | Pourquoi |
|---|---|---|---|---|---|
| 1 | Avance du siège | **1840000** Liaison Siège | Crédit | — | Argent venu d'une autre structure de la même association : ce n'est **ni un produit, ni un emprunt**. Le SESSAD doit cette somme au siège. |
| 2 | Chèque 0004518 | **Rien** | — | — | Le chèque a été **saisi en septembre**, le jour où il a été émis (pièce 2). Le saisir à nouveau paierait deux fois LIMOREAUPSY. On le **pointe** seulement. |
| 3 | Orange | **1840000** Liaison Siège | Débit | — | La facture appartient au siège (voir question 4). |
| 4 | Dupont | **LIDUPONT** (centralisé en 4011000) | Débit | — | Paiement d'une facture déjà saisie en AC. L'analytique est sur la facture, pas sur le paiement. |
| 5 | Girard | **SAGIRARD** (centralisé en 4248000) | Débit | — | Remboursement d'une note de frais déjà saisie. |
| 6 | Carburant CB | **6062100** Combustibles et carburants | Débit | 10-SESSAD | Ticket CB + ticket de caisse, **sans facture** : saisie directe en charge (règle du document T21). |
| 7 | CPAM | **6419000** Remboursements IJSS | Crédit | 10-SESSAD | « Charge négative » : elle diminue les charges de personnel du SESSAD. |
| 8 | ARS | **7312130** ESSMS relevant du 2° du I de l'article L. 312-1 du CASF | Crédit | 10-SESSAD | Dotation de l'autorité de tarification (le 2° vise les services pour enfants et jeunes handicapés, comme le SESSAD). |
| 9 | Prévoyance | **6419100** Remboursements prévoyance | Crédit | 10-SESSAD | Même logique que les IJSS, compte distinct pour la prévoyance. |
| 10 | Moreau | **LIMOREAUPSY** (4011000) | Débit | — | Paiement de la facture de septembre. |
| 11 | TotalCarte | **FOTOTALCARTE** (4010000) | Débit | — | Paiement du relevé de septembre, saisi en AC le 05/10. |
| 12 | Leroy | **4710000** Comptes d'attente | Crédit | — | Origine inconnue au moment de la saisie : on ne devine pas. |
| 13 | Retour TotalCarte | **FOTOTALCARTE** | Crédit | — | Le paiement de la ligne 11 est annulé : la dette revient. |
| 14 | Remboursement au siège | **1840000** Liaison Siège | Débit | — | Le SESSAD rembourse le siège : on solde la dette de liaison. Jamais de 58 entre deux structures. |
| 15 | Ludik | **FOLUDIK** (4010000) | Débit | — | Paiement de facture. |
| 16 | Frais bancaires | **6270000** Services bancaires et assimilés | Débit | 10-SESSAD | Frais prélevés directement par la banque, sans facture séparée. |

> ⚠️ Erreur classique : taper le compte de centralisation **4011000** ou **4010000** au lieu du compte de tiers (LIDUPONT, FOTOTALCARTE). Le document T21 l'interdit : le compte de centralisation se remplit tout seul. Saisi directement, le paiement n'est rattaché à aucun fournisseur et ne pourra jamais être lettré.

### Question 4 — Orange : la charge d'une autre structure payée par le mauvais compte

Si vous passez la ligne 3 en **6262000** dans le SESSAD :

- la facture est **déjà** en charge au siège (saisie en AC de SIE, puis répartie en IS selon les ETP, dont 48 % pour le SESSAD) ;
- le SESSAD supporterait donc la charge **deux fois** : 100 % par la banque et 48 % par l'IS ;
- et chez le siège, la dette FOORANGE resterait ouverte : quelqu'un finirait par **payer Orange une deuxième fois**.

La bonne lecture : le SESSAD a **payé pour le compte du siège**. Il a une **créance** sur le siège → **1840000 au débit**. Chez le siège, la dette envers Orange est éteinte, et le siège doit cette somme au SESSAD → **FOORANGE au débit, 1849100 au crédit**.

Actions non comptables (aussi importantes que l'écriture) :

1. Envoyer à l'opérateur un **nouveau mandat SEPA** signé avec l'IBAN du **siège** (5121000) et demander l'annulation de l'ancien.
2. Vérifier les **relevés de septembre** du SESSAD : la note dit « depuis septembre » ; s'il y a un autre prélèvement Orange, même traitement.
3. Prévenir la secrétaire du siège de **ne pas** mettre la facture d'octobre en paiement par virement si elle est aussi prélevée.

### Question 5 — Le virement de 150,00 € sans référence

**Au 20/10** : on ne sait pas ce que c'est. On le met en **4710000 Comptes d'attente**, avec un libellé qui dit tout (nom de l'émetteur, date, « à identifier »). Le document T21 rappelle que les comptes d'attente s'utilisent « avec parcimonie » et doivent être **soldés à chaque fin d'exercice**. En pratique : liste des sommes en attente revue **chaque mois**.

**Au 16/11**, le courrier règle la question : c'est un **don à l'association**, pas une recette du SESSAD. Le don doit aller dans la structure **ASS** (vie associative, code 90-ASSO). Or les structures ne se parlent **qu'à travers le siège** : le SESSAD n'a qu'un compte de liaison (1840000, vers le siège), et l'association aussi. Il faut donc **trois écritures** :

- **SESSAD** : on solde l'attente, et le SESSAD doit 150,00 € au siège (1840000 au crédit) ;
- **Siège** : le siège a une créance sur le SESSAD (1849100 au débit) et une dette envers l'association (1849400 au crédit) ;
- **Association** : elle a une créance sur le siège (1840000 au débit) et constate le don (7541200 au crédit).

Le compte **7541200 « Dons Autres projets »** est retenu parce que le plan T21 ne contient que des comptes de dons libellés pour la Fédération (7541100 « Dons T21 France », 7541110 « – Internet »…). **À faire valider** : le plan de l'association a peut-être une subdivision « Dons de particuliers » ; sinon, demander laquelle utiliser et s'y tenir toute l'année.

Le **reçu fiscal** est émis par l'**association** (Cap Horizons 21, personne morale unique) au nom de Mme Leroy, pour 150,00 €, à la date du versement (20/10/2026). Il est rattaché à la structure ASS, qui tient le registre des reçus. Il faut vérifier au préalable que l'association remplit bien les conditions pour délivrer des reçus (intérêt général) : c'est une question pour la directrice, pas une évidence.

L'argent, lui, est resté sur le compte du SESSAD. Il remontera au siège avec le prochain remboursement mensuel, puis le siège le reversera à l'association : la liaison garde la trace de chaque étape.

### Question 6 — Le prélèvement revenu impayé

La ligne 13 annule la ligne 11. On saisit le retour **en sens inverse** sur le même compte de tiers : **FOTOTALCARTE au crédit 418,92**. Résultat : la dette envers TotalCarte **réapparaît** dans le compte du fournisseur, ce qui est la vérité (le relevé de septembre n'est pas payé).

On ne supprime **pas** la ligne 11 de la comptabilité : le relevé bancaire montre bien les deux mouvements, la comptabilité doit les montrer aussi, sinon le rapprochement ne tombe plus.

Ensuite : faire signer un **nouveau mandat** par la directrice avec l'IBAN du SESSAD, l'envoyer à TotalCarte, et payer le relevé de septembre par **virement** à la prochaine campagne (418,92 €, sous le seuil de 1 500 € : une seule signature). Vérifier aussi si TotalCarte facture des **frais de rejet**. S'ils arrivent, ce sont des charges du SESSAD (sur la facture TotalCarte, au compte de la nature facturée). Avant de les accepter, regardez **qui** a communiqué l'ancien IBAN : si c'est l'association, les frais sont justifiés ; si c'est une erreur du fournisseur, on les conteste.

## 2. Calculs (détaillés, chaque montant justifié)

| Calcul | Détail | Résultat |
|---|---|---|
| Contrôle du relevé : total des débits | 420,00 + 312,48 + 1 245,00 + 86,70 + 62,35 + 960,00 + 418,92 + 34 380,00 + 537,60 + 38,50 | 38 461,55 ✓ |
| Contrôle du relevé : total des crédits | 20 000,00 + 1 184,62 + 98 000,00 + 2 316,40 + 150,00 + 418,92 | 122 069,94 ✓ |
| Contrôle du solde du relevé | 63 214,57 − 38 461,55 + 122 069,94 | 146 822,96 ✓ |
| Dépenses saisies en BQSES à partir du relevé | 38 461,55 − 420,00 (chèque déjà saisi en septembre) | 38 041,55 |
| Recettes saisies | toutes les lignes créditrices | 122 069,94 |
| Solde comptable 5122000 au 30/09 | pièce 2 | 62 794,57 |
| Opérations déjà saisies (pièce 3) | 64,90 + 142,30 | 207,20 |
| Solde comptable 5122000 au 31/10 | 62 794,57 + 122 069,94 − 38 041,55 − 207,20 | 146 615,76 |
| Écart relevé / comptabilité au 31/10 | 146 822,96 − 146 615,76 | 207,20 (= pièce 3, à justifier) |
| Liaison 1840000 (mouvements d'octobre) | débits 312,48 + 34 380,00 = 34 692,48 ; crédit 20 000,00 | **débiteur 14 692,48** |

## 3. Écritures comptables

### 3.1 Journal BQSES — octobre 2026 (livres du SESSAD)

*« (tapé) » = la ligne que vous saisissez ; « (auto) » = la ligne 5122000 que le logiciel génère. Le chèque n° 0004518 (ligne 2) n'apparaît pas : il a été saisi en septembre.*

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| BQSES | 01/10 | 1840000 Liaison Siège |  | Siège – avance trésorerie dotation – VIR – 10/2026 *(tapé)* |  |  | 20 000,00 |
| BQSES | 01/10 | 5122000 Banque CM SESSAD |  | Siège – avance trésorerie dotation – VIR – 10/2026 *(auto)* |  | 20 000,00 |  |
| BQSES | 05/10 | 1840000 Liaison Siège |  | Orange – fact. 09/2026 contrat siège prélevée à tort sur SESSAD – à reprendre au siège *(tapé)* |  | 312,48 |  |
| BQSES | 05/10 | 5122000 Banque CM SESSAD |  | Orange – fact. 09/2026 contrat siège prélevée à tort sur SESSAD – à reprendre au siège *(auto)* |  |  | 312,48 |
| BQSES | 06/10 | 4011000 Libéraux | LIDUPONT | Dupont – orthophonie – 2026-09 – 09/2026 *(tapé)* |  | 1 245,00 |  |
| BQSES | 06/10 | 5122000 Banque CM SESSAD |  | Dupont – orthophonie – 2026-09 – 09/2026 *(auto)* |  |  | 1 245,00 |
| BQSES | 08/10 | 4248000 Salariés NDF | SAGIRARD | Girard – NDF – 09/2026 *(tapé)* |  | 86,70 |  |
| BQSES | 08/10 | 5122000 Banque CM SESSAD |  | Girard – NDF – 09/2026 *(auto)* |  |  | 86,70 |
| BQSES | 09/10 | 6062100 Combustibles et carburants |  | Total Valence – carburant Kangoo SESSAD – ticket CB 08/10 *(tapé)* | 10-SESSAD | 62,35 |  |
| BQSES | 09/10 | 5122000 Banque CM SESSAD |  | Total Valence – carburant Kangoo SESSAD – ticket CB 08/10 *(auto)* |  |  | 62,35 |
| BQSES | 12/10 | 6419000 Remb. rémunérations IJSS |  | CPAM Drôme – IJSS subrogation – 07/09 au 30/09 *(tapé)* | 10-SESSAD |  | 1 184,62 |
| BQSES | 12/10 | 5122000 Banque CM SESSAD |  | CPAM Drôme – IJSS subrogation – 07/09 au 30/09 *(auto)* |  | 1 184,62 |  |
| BQSES | 14/10 | 7312130 ESSMS 2° du I L.312-1 CASF |  | ARS ARA – dotation globale SESSAD – douzième 10/2026 *(tapé)* | 10-SESSAD |  | 98 000,00 |
| BQSES | 14/10 | 5122000 Banque CM SESSAD |  | ARS ARA – dotation globale SESSAD – douzième 10/2026 *(auto)* |  | 98 000,00 |  |
| BQSES | 15/10 | 6419100 Remb. rémunérations prévoyance |  | Prévoyance Alpes-Rhône – IJ complémentaires – dossier 2026-0415 *(tapé)* | 10-SESSAD |  | 2 316,40 |
| BQSES | 15/10 | 5122000 Banque CM SESSAD |  | Prévoyance Alpes-Rhône – IJ complémentaires – dossier 2026-0415 *(auto)* |  | 2 316,40 |  |
| BQSES | 16/10 | 4011000 Libéraux | LIMOREAUPSY | Moreau – psychomotricité – 09/2026 *(tapé)* |  | 960,00 |  |
| BQSES | 16/10 | 5122000 Banque CM SESSAD |  | Moreau – psychomotricité – 09/2026 *(auto)* |  |  | 960,00 |
| BQSES | 19/10 | 4010000 Fournisseurs | FOTOTALCARTE | TotalCarte – carburant – relevé 09/2026 *(tapé)* |  | 418,92 |  |
| BQSES | 19/10 | 5122000 Banque CM SESSAD |  | TotalCarte – carburant – relevé 09/2026 *(auto)* |  |  | 418,92 |
| BQSES | 20/10 | 4710000 Comptes d'attente |  | VIR Leroy Marie-Claude sans référence – à identifier *(tapé)* |  |  | 150,00 |
| BQSES | 20/10 | 5122000 Banque CM SESSAD |  | VIR Leroy Marie-Claude sans référence – à identifier *(auto)* |  | 150,00 |  |
| BQSES | 22/10 | 4010000 Fournisseurs | FOTOTALCARTE | TotalCarte – retour prlv motif MD01 – relevé 09/2026 *(tapé)* |  |  | 418,92 |
| BQSES | 22/10 | 5122000 Banque CM SESSAD |  | TotalCarte – retour prlv motif MD01 – relevé 09/2026 *(auto)* |  | 418,92 |  |
| BQSES | 22/10 | 1840000 Liaison Siège |  | Siège – remb. avance 20 000 + IS 09/2026 14 380 *(tapé)* |  | 34 380,00 |  |
| BQSES | 22/10 | 5122000 Banque CM SESSAD |  | Siège – remb. avance 20 000 + IS 09/2026 14 380 *(auto)* |  |  | 34 380,00 |
| BQSES | 27/10 | 4010000 Fournisseurs | FOLUDIK | Ludik Éducation – jeux éducatifs – LE-2026-311 *(tapé)* |  | 537,60 |  |
| BQSES | 27/10 | 5122000 Banque CM SESSAD |  | Ludik Éducation – jeux éducatifs – LE-2026-311 *(auto)* |  |  | 537,60 |
| BQSES | 30/10 | 6270000 Services bancaires |  | Crédit Mutuel – tenue de compte + carte – T4 2026 *(tapé)* | 10-SESSAD | 38,50 |  |
| BQSES | 30/10 | 5122000 Banque CM SESSAD |  | Crédit Mutuel – tenue de compte + carte – T4 2026 *(auto)* |  |  | 38,50 |
| | | | | | **Total** | **160 111,49** | **160 111,49** |

Contrôle : les dépenses tapées au débit (38 041,55) + les recettes tapées au crédit (122 069,94) = 160 111,49 de chaque côté ✓.

### 3.2 Ligne 3 — l'écriture miroir chez le siège (livres de SIE)

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 31/10/2026 | 4010000 Fournisseurs | FOORANGE | Orange – fact. 09/2026 – payée par le compte du SESSAD le 05/10 | | 312,48 | |
| OD | 31/10/2026 | 1849100 Liaison SESSAD | | Orange – fact. 09/2026 – payée par le SESSAD pour le siège | | | 312,48 |
| | | | | | **Total** | **312,48** | **312,48** |

Cette OD **lettre** la facture Orange de septembre dans le compte FOORANGE du siège : elle ne sera pas payée une deuxième fois.

### 3.3 Le don de Mme Leroy, au 16/11/2026 (trois livres)

**Livres du SESSAD (SES)**

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 16/11/2026 | 4710000 Comptes d'attente | | Leroy – VIR 20/10 identifié : don à l'association – courrier 16/11 | | 150,00 | |
| OD | 16/11/2026 | 1840000 Liaison Siège | | Leroy – don reçu sur compte SESSAD, à transférer à ASS via siège | | | 150,00 |
| | | | | | **Total** | **150,00** | **150,00** |

**Livres du siège (SIE)**

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 16/11/2026 | 1849100 Liaison SESSAD | | Leroy – don reçu par le SESSAD pour ASS | | 150,00 | |
| OD | 16/11/2026 | 1849400 Liaison Association | | Leroy – don à reverser à ASS | | | 150,00 |
| | | | | | **Total** | **150,00** | **150,00** |

**Livres de l'association (ASS)**

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 16/11/2026 | 1840000 Liaison Siège | | Leroy – don reçu sur compte SESSAD le 20/10 | | 150,00 | |
| OD | 16/11/2026 | 7541200 Dons Autres projets | | Leroy Marie-Claude – don – VIR 20/10/2026 – reçu fiscal n° … | 90-ASSO | | 150,00 |
| | | | | | **Total** | **150,00** | **150,00** |

Contrôle des liaisons : SES 1840000 crédit 150,00 ↔ SIE 1849100 débit 150,00 ✓ ; SIE 1849400 crédit 150,00 ↔ ASS 1840000 débit 150,00 ✓. Somme de tous les comptes 18 de l'association pour cette opération : 0 ✓.

*Date du don* : on peut dater l'OD de l'association au 20/10 si octobre n'est pas encore clôturé, pour que le produit soit dans le bon mois. Le reçu fiscal porte, lui, la date du versement (20/10/2026) quoi qu'il arrive.

### 3.4 Lettrage (question 7)

*Compte LIMOREAUPSY (livres du SESSAD)*

| Date | Journal | Pièce | Débit | Crédit | Lettre |
|---|---|---|---|---|---|
| 31/08/2026 | AC | Facture 08/2026 | | 420,00 | A |
| 28/09/2026 | BQSES | Chèque 0004518 (débité le 02/10) | 420,00 | | A |
| 30/09/2026 | AC | Facture 09/2026 | | 960,00 | B |
| 16/10/2026 | BQSES | Virement | 960,00 | | B |

*Compte FOTOTALCARTE (livres du SESSAD)*

| Date | Journal | Pièce | Débit | Crédit | Lettre |
|---|---|---|---|---|---|
| 05/10/2026 | AC | Relevé carburant 09/2026 | | 418,92 | *(non lettré)* |
| 19/10/2026 | BQSES | Prélèvement | 418,92 | | C |
| 22/10/2026 | BQSES | Retour prélèvement MD01 | | 418,92 | C |

Le prélèvement et son retour sont lettrés **ensemble** (ils s'annulent) ; la facture reste **ouverte** : 418,92 € toujours dus. C'est exactement ce que doit montrer le compte.

*Autres comptes* : LIDUPONT (facture 2026-09 / virement 06/10, 1 245,00), SAGIRARD (NDF 09/2026 / virement 08/10, 86,70) et FOLUDIK (LE-2026-311 / virement 27/10, 537,60) sont **lettrés et soldés**.

*Ce qui reste non lettré au 31/10* : FOTOTALCARTE 418,92 (impayé, voir question 6) ; FOBUREAU26 64,90 et SADURAND 142,30 sont **lettrés** dans les comptes de tiers (le paiement est saisi), mais leurs paiements ne sont pas encore passés en banque : c'est le rapprochement qui les suit, pas le lettrage.

### 3.5 État de rapprochement bancaire au 31/10/2026 (question 8)

```
CAP HORIZONS 21 – Structure SES – Compte 5122000 Crédit Mutuel SESSAD
ÉTAT DE RAPPROCHEMENT AU 31/10/2026

Solde du relevé n° 10 au 31/10/2026 (créditeur)                   146 822,96
Moins : opérations saisies en comptabilité, pas encore passées en banque
  – Chèque n° 0004524 émis le 29/10 à FOBUREAU26                    –  64,90
  – Virement émis le 30/10 à SADURAND (débité le 02/11)            – 142,30
= Solde rapproché                                                 146 615,76

Solde comptable 5122000 au 31/10/2026 (débiteur)                  146 615,76
Écart                                                                   0,00  ✓

Opérations de la banque non saisies en comptabilité : aucune (toutes saisies le 16/11).
Établi le 16/11/2026 par : [agente comptable]     Visé par : N. Berthier
Pièces jointes : relevé n° 10, extrait du grand livre 5122000, mail TotalCarte, courrier Leroy
```

Au **30/11**, il faudra vérifier que le chèque 0004524 et le virement Durand apparaissent bien sur le relevé de novembre. Un chèque non encaissé depuis plus de deux ou trois mois doit faire l'objet d'un appel au bénéficiaire (perdu ? oublié ?).

### 3.6 Solde de liaison d'octobre (question 9)

| Date | Opération | Débit | Crédit | Solde |
|---|---|---|---|---|
| 01/10 | Avance du siège | | 20 000,00 | créditeur 20 000,00 |
| 05/10 | Orange payé pour le siège | 312,48 | | créditeur 19 687,52 |
| 22/10 | Remboursement avance + IS septembre | 34 380,00 | | **débiteur 14 692,48** |

Chez le siège, le compte **1849100** doit montrer, pour les mêmes opérations, un solde **créditeur de 14 692,48** : avance (débit 20 000,00 au BQSIE le 01/10), remboursement reçu (crédit 34 380,00 au BQSIE le 22/10), OD Orange (crédit 312,48). Exactement l'opposé ✓.

*(Le débit net d'octobre s'explique : les 14 380,00 € d'IS de septembre remboursés ce mois-ci éteignent un crédit qui figurait déjà dans le compte au 30/09.)*

## 4. Points d'attention / pièges

- **Saisir le chèque 0004518 une seconde fois** : il a été comptabilisé en septembre, à l'émission. Sur le relevé d'octobre, on le **pointe**, on ne le saisit pas.
- **Penser « banque » au lieu de « contrepartie »** : en BQSES, une dépense se tape au **débit** de la contrepartie.
- **Mettre Orange en charge au SESSAD** : double charge, et dette jamais soldée au siège (risque de double paiement).
- **Mettre le virement Leroy en produit du SESSAD** (7312130 ou 7588000) parce que « c'est arrivé sur son compte » : on fausserait le compte de résultat que l'ARS contrôle. Une somme dont on ignore l'origine va en **4710000**, et on cherche.
- **Effacer le prélèvement TotalCarte rejeté** au lieu de saisir le retour : le relevé montre deux lignes, la comptabilité doit en montrer deux.
- **Passer l'avance du siège en 58 ou en 1640000** : entre deux structures de la même association, c'est **toujours** la liaison 18. Le 58 sert entre deux comptes de trésorerie **d'une même structure**, et un emprunt suppose un prêteur extérieur.
- **Mettre de l'analytique sur les comptes de tiers, de liaison ou de banque** : l'analytique va sur les classes 6 et 7, là où se lit le coût du service.
- **IJSS en 7xx** : le document T21 est clair, c'est **6419000**, au crédit. Plus de compte de transfert de charges (supprimés par le règlement ANC n° 2022-06).

## 5. Ce qu'un senior ferait en plus

**Bonnes pratiques de saisie bancaire :**

- **Saisir la banque toutes les semaines**, pas une fois par mois (et encore moins un mois et demi après) : un retour de prélèvement repéré le 22/10 se règle en un appel ; repéré le 16/11, le fournisseur a déjà relancé.
- **Partir du rapprochement précédent** : la première chose à faire en ouvrant un relevé, c'est reprendre l'état du mois d'avant et cocher ce qui « tombe » (ici le chèque 0004518).
- **Contrôler le relevé lui-même** (solde de début + crédits − débits = solde de fin) avant de saisir : un PDF mal exporté ou une page manquante se voit tout de suite.
- **Une pièce pour chaque ligne** : ticket CB agrafé au ticket de caisse, avis de virement de la CPAM (il détaille la période et le salarié, indispensable pour vérifier que la paie a bien maintenu le salaire), courrier de la prévoyance, mail de TotalCarte.

**Contrôles à lancer à partir de ce relevé :**

- **IJSS** : rapprocher les 1 184,62 € de l'attestation de la CPAM et du bulletin de paie de septembre de la salariée. En subrogation, l'employeur maintient le salaire et la CPAM le rembourse : si le montant reçu ne correspond pas au montant attendu, c'est le service paie (EIG RH) qui doit régulariser.
- **Mandats SEPA** : faire la liste de **tous** les prélèvements de chaque compte (opérateur, énergie, carte carburant, assurance) et vérifier que chacun est sur le compte de la **structure qui supporte le contrat**. L'erreur Orange en cache peut-être d'autres.
- **Compte 4710000** : tenir une liste des sommes en attente, structure par structure, avec la date d'entrée et les relances. Objectif : **zéro** au 31/12.
- **Liaisons** : chaque fin de mois, comparer 1849100 (siège) et 1840000 (SESSAD). L'OD Orange chez le siège est **la** ligne qu'on oublie, et l'écart sautera aux yeux au contrôle croisé.

**Mail type à la secrétaire du siège (Orange) :**

> « Bonjour, le prélèvement Orange de la facture de septembre (312,48 €) est passé sur le compte du SESSAD, à cause d'un ancien mandat. J'ai passé les écritures de liaison : la facture est soldée chez le siège, ne la mettez pas en paiement. Pouvez-vous faire signer un nouveau mandat avec l'IBAN du siège à Mme Berthier et l'envoyer à Orange cette semaine ? Je vérifie de mon côté le relevé de novembre. Merci ! »

**Documentation du dossier :** classer l'état de rapprochement signé, le relevé, l'extrait du grand livre 5122000 et les justificatifs des lignes « anormales » (Orange, Leroy, TotalCarte) dans le dossier de clôture mensuelle. C'est ce que le CAC demandera fin novembre.

## 6. Références

- Documents internes T21 France (30/04/2026) : « Les journaux comptables » (journaux de banque à contrepartie automatique, saisie au débit des dépenses, CB sans facture en 60621, IJSS en 6419, prévoyance en 64191, dotations en 731) ; « La comptabilité » (comptes de liaison 18 de solde nul au niveau de l'organisme gestionnaire, comptes d'attente 47 à solder à chaque fin d'exercice).
- Plan comptable T21 France (MAJ 13/10/2025) : 1840000, 4010000, 4011000, 4248000, 4710000, 5122000 (subdivision de 512 propre à la structure — fiche du dossier), 6062100, 6270000, 6419000, 6419100, 7312130, 7541200.
- Arrêté du 19 décembre 2025 relatif au plan comptable des ESSMS privés relevant du I de l'article L. 312-1 du CASF, applicable à compter du 1er janvier 2026.
- Règlement ANC n° 2022-06 : suppression des comptes de transfert de charges.
- Reçus fiscaux pour dons : conditions fixées par le CGI pour les organismes d'intérêt général (*vérifier l'éligibilité de l'association avant d'émettre un reçu*).
