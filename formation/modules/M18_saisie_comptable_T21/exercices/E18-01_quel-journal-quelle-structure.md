# E18-01 — Quel journal, quelle structure ? 20 opérations à aiguiller

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQEMP** | Journal de banque de l'emploi accompagné. Contrepartie automatique 5124000. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IMMOS** | EIG IMMOS : le fichier des immobilisations. Calcule les amortissements et les sorties d'actif, puis les déverse dans le journal des immobilisations (automatique). |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PA** | Plateforme agréée — ou, dans le M18, journal de paie. Opérateur agréé par l'État (anciennement « PDP ») qui transmet les factures électroniques entre entreprises et envoie les données à l'administration. Dans le module M18, PA est le code du journal des salaires, alimenté automatiquement par EIG RH. |
    | **PLSIE** | Journal de banque « placement » du siège. Un journal par placement : versements, retraits, intérêts du compte à terme 5081100. |
    | **RH** | Ressources humaines. Service ou personne qui gère le personnel. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **VT** | Journal des ventes. Journal où l'on enregistre les factures clients (et les Z de caisse). |
    | **Compte 4010000** | Fournisseurs (comptes de tiers FO…) (plan T21). Compte de centralisation des fournisseurs. Interdit d'y saisir : on saisit dans le compte de tiers FO… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
<!-- /glossaire-page -->

**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★☆☆ | **Durée estimée :** 45 min | **Thèmes :** journaux manuels et automatiques, choix de la structure, comptes de tiers FO / LI / SA / CL, sens débit / crédit, journal de banque à contrepartie automatique, IJSS et prévoyance, virements internes (58), comptes de liaison (18), factures non parvenues (4081000)

**Corner case :** oui — trois demandes « pour aller plus vite » sont interdites par les règles T21 (saisir la paie à la main, passer un amortissement en OD, saisir directement dans le compte 4010000), et un virement entre deux structures n'est **pas** un virement interne en 58.

> *Cadre de formation : association, personnes, montants et documents fictifs. Les règles de saisie viennent des documents internes de Trisomie 21 France (voir la fiche du dossier).*

!!! abstract "En clair"
    Avant de saisir quoi que ce soit, il faut **aiguiller** la pièce : dans quel **journal** (le « cahier » où l'on écrit l'opération), dans quelle **structure** (laquelle des cinq comptabilités de l'association), sur quel **compte**, avec quel **tiers** (la personne ou l'entreprise concernée), et dans quel **sens** (débit ou crédit). Si l'aiguillage est faux, tout ce qui suit est faux. Cet exercice ne demande **aucun calcul** : seulement de bons réflexes.

## La mise en situation

Lundi 16 novembre 2026. C'est votre deuxième semaine comme agent comptable de **Cap Horizons 21**. Nathalie Berthier, la directrice, a déposé sur votre bureau une bannette de pièces et une liste de questions des collègues. Elle vous demande : « Avant de saisir, dites-moi pour chaque ligne où elle va. Je veux être sûre que vous avez compris notre organisation. »

Gardez sous les yeux la **fiche du dossier** (5 structures, journaux, tiers). Rappel des mots utilisés :

- **Structure** : une des cinq comptabilités de l'association : **SIE** (siège), **SES** (SESSAD, enfants), **SAV** (SAVS, adultes), **EMP** (emploi accompagné), **ASS** (vie associative et projets).
- **Journal manuel** : vous saisissez vous-même. **Journal automatique** : les écritures arrivent seules depuis un autre logiciel (**EIG RH** pour la paie, **EIG IMMOS** pour les immobilisations, **EIG Gestion commerciale** pour les ventes). On n'y saisit **jamais** à la main.
- **Tiers** : le compte individuel d'un fournisseur (**FO**…), d'un libéral conventionné (**LI**…, par exemple une orthophoniste qui travaille pour l'association sans en être salariée), d'un salarié pour ses notes de frais (**SA**…) ou d'un client (**CL**…).
- **TTC** : toutes taxes comprises. L'association ne récupère pas la TVA : elle comptabilise ses achats TTC.

## Les pièces et les questions

| N° | Date | Pièce ou demande |
|---|---|---|
| 1 | 03/11/2026 | Facture **EDF** n° 10 284 556 712, électricité des locaux de Valence (septembre–octobre), **2 093,87 € TTC**, adressée au siège. Les locaux sont partagés par les cinq structures. |
| 2 | 02/11/2026 | **Note de frais** d'octobre de Nathalie Durand, éducatrice spécialisée au SESSAD : 286 km avec sa voiture et un achat de stylos et carnets (23,70 €). Total **205,60 €**, visée par le chef de service. |
| 3 | 04/11/2026 | Relevé bancaire du **SAVS** : virement « CPAM DROME IJSS » de **612,48 €** pour Inès Roche, monitrice-éducatrice du SAVS, en arrêt maladie (la paie maintient son salaire). |
| 4 | 05/11/2026 | Relevé bancaire du **SESSAD** : virement « ARS ARA DOTATION GLOBALE 11/2026 » de **118 450,00 €**. |
| 5 | 06/11/2026 | Ticket de caisse d'une station-service + ticket de carte bancaire du compte **SAVS** : plein du véhicule de service du SAVS, **58,40 €**. Pas de facture. |
| 6 | 06/11/2026 | La paie d'octobre du service emploi accompagné n'est pas arrivée en comptabilité. La cheffe de service vous dit : « Saisissez-la à la main dans le journal de paie à partir du PDF du journal de paie, c'est urgent. » |
| 7 | 09/11/2026 | En relisant la balance du SESSAD, vous voyez qu'il manque la **dotation aux amortissements** d'octobre de l'ordinateur acheté en septembre. Une collègue : « Passe-la en OD, ça ira plus vite. » |
| 8 | 09/11/2026 | Une collègue de la **Fédération Trisomie 21 France** vous demande comment, chez elle, on enregistre la facture de formation que la Fédération émet pour une association du réseau. |
| 9 | 10/11/2026 | Retrait de **150,00 €** au distributeur avec la carte du compte **ASS**, pour alimenter la **petite caisse** du marché de Noël. |
| 10 | 10/11/2026 | **Avoir** Bureau Vallée 26 n° AV-26-0412 de **37,80 € TTC** : cartouches d'encre défectueuses rendues par le SAVS (elles avaient été facturées en octobre). |
| 11 | 16/11/2026 | Vous préparez la clôture : la facture EDF de **novembre–décembre 2026** n'arrivera qu'en janvier 2027. Estimation d'après la facture précédente : **2 150,00 € TTC**. |
| 12 | 12/11/2026 | Facture de **Claire Dupont, orthophoniste libérale** conventionnée avec le SESSAD : séances d'octobre, **675,00 €**. |
| 13 | 12/11/2026 | Vous payez par virement la facture du **Garage Martin** (réparation du véhicule du SAVS, 494,28 €), déjà saisie au journal des achats. |
| 14 | 13/11/2026 | Relevé bancaire du **SESSAD** : prélèvement « COMMISSIONS ET FRAIS » de **18,60 €**. |
| 15 | 13/11/2026 | Remise en banque, sur le compte **ASS**, d'un chèque de **200,00 €** : don d'une famille à l'association. |
| 16 | 13/11/2026 | Relevé bancaire **ASS** : virement de **6 000,00 €** de la Fondation de France, subvention du projet « Pairs et voix ». |
| 17 | 14/11/2026 | Facture **Info Rhône Services** : un ordinateur portable **899,00 € TTC** et une souris 24,90 € TTC, livrés au service **emploi accompagné**. |
| 18 | 14/11/2026 | Facture d'un **nouveau fournisseur**, « Sécuri Feu 26 », vérification annuelle des extincteurs des locaux de Valence. Une collègue : « Le tiers n'existe pas, mets-la directement sur le 4010000, on verra plus tard. » |
| 19 | 16/11/2026 | Le SESSAD **rembourse au siège** 4 800,00 € (sa part des factures communes d'octobre) : virement du compte bancaire du SESSAD vers celui du siège. Une collègue : « C'est un virement de banque à banque, donc en 58. » |
| 20 | 16/11/2026 | Relevé bancaire du **SAVS** : virement de **1 245,30 €** de l'organisme de **prévoyance**, pour un salarié du SAVS en arrêt de longue durée. |

## Travail à faire

1. Pour chacune des 20 lignes, indiquez :
    - le **journal** (code de la fiche : AC, VT, BQSIE / BQSES / BQSAV / BQEMP / BQASS, PLSIE, CAASS, PA, IM, OD) ;
    - si ce journal est **manuel** ou **automatique** ;
    - la **structure** dans les livres de laquelle on saisit (SIE, SES, SAV, EMP, ASS, ou « pas chez nous ») ;
    - le **compte général** et, s'il y a lieu, le **compte de tiers** ;
    - le **sens** (débit ou crédit) de la ligne que **vous** saisissez. Pour les journaux de banque, précisez aussi la ligne que le logiciel ajoute seul.
2. Pour les lignes 6, 7, 18 et 19, expliquez en deux ou trois phrases ce que vous répondez à votre collègue.
3. Pour la ligne 1, quelles écritures apparaissent dans les livres **du SESSAD** ?
4. Pour la ligne 9, pourquoi faut-il **deux** écritures et un compte 58 ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-01_corrige.md)
