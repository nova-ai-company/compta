# Corrigé E18-08 — Petite caisse, virements internes et compte à terme

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **ANC** | Autorité des normes comptables. L'organisme qui écrit les règles comptables françaises (le PCG). |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CAT** | Compte à terme. Placement bloqué pour une durée fixée, avec intérêts. Comptes 5081XXX dans le plan T21. |
    | **CME** | Crédit Mutuel (abréviation du plan T21). Banque coopérative : pour ouvrir un compte, on souscrit des parts sociales. |
    | **ICNE** | Intérêts courus non échus. À la clôture : intérêts d'emprunt qui concernent l'année mais qui seront payés à la prochaine échéance. On les enregistre en charge de N. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **PLSIE** | Journal de banque « placement » du siège. Un journal par placement : versements, retraits, intérêts du compte à terme 5081100. |
    | **PSB** | Parts sociales (abréviation du plan T21). Dans « PSB CME T21 France (parts sociales) », compte 5040000 : parts sociales détenues au Crédit Mutuel. |
    | **PV** | Procès-verbal — ou plus-value. Deux sens selon le contexte : (1) PV d'assemblée générale, de réception de travaux, d'inventaire ; (2) plus-value de cession. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 5081XXX** | CAT détaillés (plan T21). Comptes à terme (CAT), un sous-compte par placement. |
    | **Compte 2710000** | Titres immobilisés (droit de propriété) (plan T21). Titres détenus durablement (le document T21 y range les parts sociales du Crédit Mutuel ; le plan, lui, a aussi 5040000 : à clarifier). |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 5040000** | PSB CME T21 France (parts sociales) (plan T21). Parts sociales du Crédit Mutuel détenues par T21 France (« PSB CME »). Le document range les parts sociales en 27 : à clarifier. |
    | **Compte 5081100** | Compte à terme du siège (dossier M18, fictif). Placement du siège, sous-compte du 5081XXX du plan T21 ; journal PLSIE. |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 5188000** | Intérêts courus à recevoir (plan T21). Intérêts des placements acquis au 31/12 mais versés plus tard. |
    | **Compte 5300000** | Caisse (plan T21). Caisse (espèces). Le solde doit être égal au comptage physique. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6062500** | Fournitures scolaires, éducatives et de loisirs (plan T21). Jeux, matériel éducatif, fournitures de loisirs pour les personnes accompagnées. |
    | **Compte 6063000** | Alimentation (plan T21). Alimentation (goûters, repas d'activités, événements). |
    | **Compte 6270000** | Services bancaires et assimilés (plan T21). Frais bancaires (prélevés directement sur le relevé). |
    | **Compte 6588000** | Charges diverses de gestion courante - autres (plan T21). Autres charges de gestion courante (ex. : arrondis, petits écarts justifiés). |
    | **Compte 6720000** | Charges sur exercices antérieurs (plan T21). Charge oubliée d'un exercice antérieur. |
    | **Compte 7541200** | Dons Autres projets (plan T21). Dons pour d'autres projets. |
    | **Compte 7640000** | Revenus des valeurs mobilières de placement (plan T21). Intérêts des placements (comptes à terme, livrets). |
    | **autorités de tarification** | Le financeur qui fixe le budget d'un ESSMS. L'ARS (pour le SESSAD) ou le Conseil départemental (pour le SAVS). |
    | **compte administratif** | Compte rendu annuel d'un service hors CPOM. Le réalisé de l'année, remis au financeur (ex. : le Département pour le SAVS) en général avant le 30 avril N+1. |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **fonds de roulement** | Ressources stables moins biens durables. L'argent « d'avance » qui finance le fonctionnement courant. |
    | **plan de trésorerie** | Prévoir l'argent en banque mois par mois. Solde de début + encaissements − décaissements = solde de fin, sur 6 à 12 mois. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-08](../exercices/E18-08_caisse-virements-internes-placements.md)

> *Cadre de formation : association, personnes, sociétés et documents fictifs.*

!!! abstract "En clair"
    Trois idées suffisent. **1.** Entre deux comptes de trésorerie d'une même structure, on passe toujours par le **5800000**, en deux écritures (une dans chaque journal), et le 58 revient à zéro. **2.** La caisse comptable doit être égale, au centime, à l'argent **compté** dans la boîte ; un écart se **cherche** d'abord, et ne se passe en charge qu'en dernier recours, avec un procès-verbal. **3.** Les intérêts d'un placement appartiennent à l'année où ils **courent**, pas à celle où ils sont versés : au 31/12, on enregistre ceux qui ont couru depuis le 01/10.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Pourquoi deux écritures pour un retrait d'espèces

Le journal **BQASS** a pour contrepartie automatique **5125000** (la banque) ; le journal **CAASS** a pour contrepartie automatique **5300000** (la caisse). Un journal de banque ne peut pas mouvementer la caisse, et inversement. Le retrait se découpe donc en deux moitiés :

- dans **BQASS** : l'argent **sort** de la banque. Vous tapez **5800000 au débit** 300,00 (une « dépense » pour ce journal) ; le logiciel crédite 5125000.
- dans **CAASS** : l'argent **entre** dans la caisse. Vous tapez **5800000 au crédit** 300,00 (une « recette » pour ce journal) ; le logiciel débite 5300000.

Écrire « 5300000 / 5125000 » directement en OD est interdit par le document T21 (« il n'est pas possible de comptabiliser la sortie de banque (512) avec une contrepartie de compte caisse (53) ») et, surtout, cela casserait le **rapprochement** : chaque journal doit refléter **son** relevé (le relevé bancaire pour BQASS, le brouillard de caisse pour CAASS). Le 58 permet aussi un contrôle : si une des deux moitiés est oubliée, il ne revient pas à zéro.

### Question 2 — Les achats et les dons du goûter

| Opération | Compte tapé | Sens de la ligne tapée | Analytique | Pourquoi |
|---|---|---|---|---|
| Boissons, gâteaux, fruits | **6063000** Alimentation | Débit | 90-ASSO | Achat non stocké (pas de stocks chez T21) |
| Jeux et crayons du stand | **6062500** Fournitures scolaires, éducatives et de loisirs | Débit | 90-ASSO | Fournitures de loisirs, consommées le jour même |
| Dons de l'urne | **7541200** Dons Autres projets | Crédit | 90-ASSO | Dons en espèces ; même remarque qu'en E18-05 sur le libellé du plan T21, à faire valider |

Un ticket de caisse suffit comme justificatif pour un achat en espèces de faible montant (comme pour la carte bancaire sans facture). On ne mélange **jamais** les dons et les dépenses : les 412,50 € de dons sont enregistrés en **brut**, et les achats séparément. On ne fait pas « dons nets des achats = 283,15 € ».

**Reçus fiscaux** : impossible pour les dons de l'urne. Ils sont **anonymes** : on ne sait pas qui a donné combien. Un reçu fiscal suppose un donateur identifié et un montant prouvé. Si une famille veut un reçu, elle doit donner par chèque, virement ou en espèces **contre un reçu nominatif** remis sur place.

### Question 4 — Le solde théorique et l'écart

| Élément | Montant |
|---|---|
| Solde au 31/10 | 84,30 |
| + Retrait du 03/11 | 300,00 |
| − Supermarché | − 86,45 |
| − Bazar | − 42,90 |
| + Dons de l'urne | 412,50 |
| − Versement en banque | − 400,00 |
| **= Solde théorique au 16/11** | **267,45** |
| Comptage réel | 263,95 |
| **Écart (manquant)** | **− 3,50** |

**Avant toute écriture, on cherche** (dans cet ordre) :

1. **Recompter à deux** (vous et R. Haddad), billets et pièces, et refaire l'addition du comptage : 263,95 € confirmé.
2. **Rechercher un ticket oublié** : un achat de 3,50 € (pain, glaçons, timbre, parking) payé en espèces le jour du goûter et dont le ticket est resté dans une poche.
3. **Revoir le PV des dons** : l'urne a-t-elle été comptée **avant** que quelqu'un y prenne de la monnaie ? Le PV est-il signé par deux personnes et l'addition juste ?
4. **Clarifier la phrase de R. Haddad sur les crayons** : si des objets ont été **vendus** au stand, ce n'étaient pas des dons, et il y a eu des échanges de monnaie non tracés. Une vente se trace (liste ou ticket), et ne s'enregistre pas en dons. C'est la piste la plus probable de l'écart, et un point de procédure à corriger pour le prochain événement.

**Si l'écart reste inexpliqué**, on aligne la comptabilité sur la réalité (la caisse comptable doit toujours être égale à la caisse physique, dit le document T21) :

- **compte retenu : 6588000 « Charges diverses de gestion courante – autres »**. C'est le compte du plan T21 qui correspond à une **perte courante de faible montant** sans nature identifiée. Depuis le règlement ANC n° 2022-06, le résultat exceptionnel est réservé aux événements majeurs et inhabituels : un écart de caisse de 3,50 € n'en est pas un ;
- **pas** 6720000 « Charges sur exercices antérieurs » (l'écart est de novembre 2026) ;
- **pas** 6270000 (ce ne sont pas des frais bancaires), ni 6063000 (on n'invente pas un achat) ;
- **pas** 4710000 « Comptes d'attente » sans suite : ce serait cacher le problème jusqu'au 31/12. Le 4710000 ne se justifie que pour quelques jours, si une recherche concrète est en cours (ticket attendu) ;
- **pas** en diminution des dons (7541200 au débit) sans preuve que l'erreur vient du comptage de l'urne.

L'écriture est appuyée par un **procès-verbal de caisse** daté et signé par deux personnes (comptage, solde théorique, écart, recherches faites), visé par la directrice.

> ⚠️ Erreur classique : « compléter » la caisse avec 3,50 € de sa poche pour que le compte tombe juste. C'est sympathique et c'est **faux** : la comptabilité ne reflète plus ce qui s'est passé, et un écart répété (signe d'un problème de procédure, voire d'un vol) devient invisible.

### Question 7 — Le retrait partiel et l'erreur du document T21

Dans **PLSIE** (contrepartie automatique 5081100), l'argent **sort** du placement : vous tapez **5800000 au débit** 20 000,00 ; le logiciel **crédite** 5081100. Dans **BQSIE**, l'argent **entre** sur le compte courant : vous tapez **5800000 au crédit** 20 000,00 et **7640000 au crédit** 25,21 (intérêts versés avec le capital) ; le logiciel débite 5121000 de 20 025,21 (le montant de l'avis).

La phrase du document T21 *« lors de la libération des fonds, le compte est **débité** »* est une **coquille** : un compte d'actif augmente au débit et **diminue au crédit**. Quand les fonds sont libérés (retirés), le placement diminue : le compte 508 est **crédité**. La phrase correcte : « Lors de la souscription, le compte est débité ; lors de la libération des fonds, il est crédité. » Réflexe senior : signaler la coquille à l'auteur du document (le service comptable de la Fédération), par un mail court et factuel, pour que la prochaine personne formée avec ce document ne l'apprenne pas de travers.

### Question 8 — Les intérêts courus au 31/12/2026

Au 31/12, 40 000,00 € sont placés depuis le 01/10 à 2,00 %. Les intérêts de cette somme ne seront versés qu'à l'échéance (01/10/2027), mais ceux qui ont couru **du 01/10 au 31/12/2026** appartiennent à **2026** : c'est le principe d'indépendance des exercices (le même qui impose les factures non parvenues en 4081000).

Calcul : 40 000,00 × 2,00 % × 92 / 365 = **201,64 €** (92 jours : 31 en octobre + 30 en novembre + 31 en décembre). Les intérêts des 20 000,00 € retirés ont déjà été versés le 16/11 : ils sont déjà en 7640000, on ne les compte pas une seconde fois.

Écriture au 31/12 (journal **OD**, pas PLSIE : aucun argent ne bouge, et le journal PLSIE mouvementerait automatiquement 5081100) : **5188000 Intérêts courus à recevoir** au débit, **7640000** au crédit. Le 01/01/2027, on **extourne** (écriture inverse) : à l'échéance d'octobre 2027, la banque versera la totalité des intérêts de l'année de placement, et 2027 ne gardera ainsi que sa part.

**Pour la trésorière, en trois phrases** : « Le placement a rapporté environ 200 € entre octobre et décembre, même si la banque ne les versera qu'en octobre 2027. Les comptes 2026 doivent montrer ce que l'année 2026 a réellement rapporté. On les inscrit donc au 31/12 comme une somme à recevoir, et on annule cette écriture le 1er janvier pour ne pas les compter deux fois en 2027. »

### Question 10 — Les parts sociales : classe 27 ou 5040000 ?

**Ce que fait un senior** : il ne tranche pas seul et ne reclasse rien sans accord. Il **pose la question**, par écrit, à la directrice et à l'expert-comptable (et, à travers eux, au CAC), en présentant les deux options et leurs conséquences. Il vérifie aussi ce qui a été fait les années précédentes (permanence des méthodes) et dans les autres structures.

**La classification la plus défendable** : les parts sociales d'une banque mutualiste ne sont ni cotées ni négociables ; elles sont détenues **durablement**, comme condition pour être sociétaire de la banque, et ne sont remboursées qu'à leur valeur nominale, au départ. Elles ne sont pas un placement de trésorerie. La pratique la plus répandue les classe donc en **titres immobilisés**, compte **2710000** (actif immobilisé), ce qui correspond au document T21. Le compte **5040000** du plan, libellé « PSB CME T21 France », semble propre à une entité (sans doute la Fédération) : à faire confirmer.

**Conséquences si l'on reclasse** (OD 2710000 au débit / 5040000 au crédit, 500,00 €, sur décision écrite) : la trésorerie du siège diminue de 500,00 € et l'actif immobilisé augmente d'autant. Dans le médico-social, cela change le calcul du **fonds de roulement** et de la **trésorerie** présentés dans l'ERRD et le compte administratif. D'où la nécessité de décider **avant** la clôture, et de le faire de la même façon dans toutes les structures.

## 2. Calculs (détaillés, chaque montant justifié)

| Calcul | Détail | Résultat |
|---|---|---|
| Solde théorique de la caisse au 16/11 | 84,30 + 300,00 − 86,45 − 42,90 + 412,50 − 400,00 | 267,45 |
| Comptage | 100,00 + 100,00 + 30,00 + 20,00 + 8,00 + 3,50 + 1,80 + 0,40 + 0,25 | 263,95 |
| Écart | 263,95 − 267,45 | − 3,50 |
| Solde de la caisse après l'écriture d'écart | 267,45 − 3,50 | 263,95 (= comptage) ✓ |
| Nombre de jours du 01/10 au 16/11 | 31 jours d'octobre + 15 jours de novembre | 46 |
| Intérêts du retrait partiel | 20 000,00 × 1,00 % × 46 / 365 = 25,205… | 25,21 ✓ (avis B2) |
| Capital restant | 60 000,00 − 20 000,00 | 40 000,00 |
| ICNE au 31/12 | 40 000,00 × 2,00 % × 92 / 365 = 201,643… | 201,64 |
| Intérêts du CAT dans le résultat 2026 | 25,21 + 201,64 | 226,85 |

## 3. Écritures comptables

### 3.1 Livres de l'ASS — banque et caisse (questions 1 à 4)

*« (tapé) » = ligne saisie ; « (auto) » = ligne de contrepartie générée par le journal (5125000 pour BQASS, 5300000 pour CAASS).*

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| BQASS | 03/11/2026 | 5800000 Virements internes |  | Retrait espèces guichet pour caisse – goûter solidaire 14/11 *(tapé)* |  | 300,00 |  |
| BQASS | 03/11/2026 | 5125000 Banque CM Association |  | Retrait espèces guichet pour caisse – goûter solidaire 14/11 *(auto)* |  |  | 300,00 |
| CAASS | 03/11/2026 | 5800000 Virements internes |  | Alimentation caisse – retrait banque du 03/11 *(tapé)* |  |  | 300,00 |
| CAASS | 03/11/2026 | 5300000 Caisse |  | Alimentation caisse – retrait banque du 03/11 *(auto)* |  | 300,00 |  |
| CAASS | 13/11/2026 | 6063000 Alimentation |  | Supermarché – boissons et goûter – ticket 13/11 *(tapé)* | 90-ASSO | 86,45 |  |
| CAASS | 13/11/2026 | 5300000 Caisse |  | Supermarché – boissons et goûter – ticket 13/11 *(auto)* |  |  | 86,45 |
| CAASS | 13/11/2026 | 6062500 Fournitures scolaires, éducatives et de loisirs |  | Bazar – jeux stand enfants – ticket 13/11 *(tapé)* | 90-ASSO | 42,90 |  |
| CAASS | 13/11/2026 | 5300000 Caisse |  | Bazar – jeux stand enfants – ticket 13/11 *(auto)* |  |  | 42,90 |
| CAASS | 14/11/2026 | 7541200 Dons Autres projets |  | Urne dons – goûter solidaire 14/11 – PV de comptage *(tapé)* | 90-ASSO |  | 412,50 |
| CAASS | 14/11/2026 | 5300000 Caisse |  | Urne dons – goûter solidaire 14/11 – PV de comptage *(auto)* |  | 412,50 |  |
| CAASS | 16/11/2026 | 5800000 Virements internes |  | Versement espèces en banque – bordereau n° 0042 *(tapé)* |  | 400,00 |  |
| CAASS | 16/11/2026 | 5300000 Caisse |  | Versement espèces en banque – bordereau n° 0042 *(auto)* |  |  | 400,00 |
| BQASS | 16/11/2026 | 5800000 Virements internes |  | Versement espèces en banque – bordereau n° 0042 *(tapé)* |  |  | 400,00 |
| BQASS | 16/11/2026 | 5125000 Banque CM Association |  | Versement espèces en banque – bordereau n° 0042 *(auto)* |  | 400,00 |  |
| CAASS | 16/11/2026 | 6588000 Charges diverses de gestion courante – autres |  | Écart de caisse inexpliqué – PV de caisse du 16/11 *(tapé)* | 90-ASSO | 3,50 |  |
| CAASS | 16/11/2026 | 5300000 Caisse |  | Écart de caisse inexpliqué – PV de caisse du 16/11 *(auto)* |  |  | 3,50 |
| | | | | | **Total** | **1 945,35** | **1 945,35** |
**Contrôle du 5800000 de l'ASS (question 5)**

| Date | Journal | Opération | Débit | Crédit | Solde |
|---|---|---|---|---|---|
| 03/11 | BQASS | Retrait banque | 300,00 | | D 300,00 |
| 03/11 | CAASS | Entrée en caisse | | 300,00 | 0,00 |
| 16/11 | CAASS | Sortie de caisse | 400,00 | | D 400,00 |
| 16/11 | BQASS | Versement en banque | | 400,00 | **0,00 ✓** |

**Contrôle du 5300000 Caisse** : 84,30 + 300,00 − 86,45 − 42,90 + 412,50 − 400,00 − 3,50 = **263,95** = comptage ✓.

### 3.2 Livres du siège — compte à terme (questions 6 et 7)

*Contreparties automatiques : 5121000 pour BQSIE, 5081100 pour PLSIE. Le 16/11, les deux lignes tapées de BQSIE donnent une seule ligne de banque de 20 025,21, comme sur le relevé.*

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| BQSIE | 01/10/2026 | 5800000 Virements internes |  | Versement sur CAT n° 0081 – 60 000 à 2,00 % *(tapé)* |  | 60 000,00 |  |
| BQSIE | 01/10/2026 | 5121000 Banque CM Siège |  | Versement sur CAT n° 0081 – 60 000 à 2,00 % *(auto)* |  |  | 60 000,00 |
| PLSIE | 01/10/2026 | 5800000 Virements internes |  | Souscription CAT n° 0081 – versement depuis 5121000 *(tapé)* |  |  | 60 000,00 |
| PLSIE | 01/10/2026 | 5081100 CAT Siège |  | Souscription CAT n° 0081 – versement depuis 5121000 *(auto)* |  | 60 000,00 |  |
| PLSIE | 16/11/2026 | 5800000 Virements internes |  | Retrait partiel CAT n° 0081 – capital *(tapé)* |  | 20 000,00 |  |
| PLSIE | 16/11/2026 | 5081100 CAT Siège |  | Retrait partiel CAT n° 0081 – capital *(auto)* |  |  | 20 000,00 |
| BQSIE | 16/11/2026 | 5800000 Virements internes |  | Retrait partiel CAT n° 0081 – capital *(tapé)* |  |  | 20 000,00 |
| BQSIE | 16/11/2026 | 7640000 Revenus des valeurs mobilières de placement |  | CAT n° 0081 – intérêts sur 20 000 retirés – 1,00 % × 46 j *(tapé)* | 01-SIEGE |  | 25,21 |
| BQSIE | 16/11/2026 | 5121000 Banque CM Siège |  | Retrait partiel CAT n° 0081 – capital + intérêts *(auto)* |  | 20 025,21 |  |
| | | | | | **Total** | **160 025,21** | **160 025,21** |
**Contrôle du 5800000 du siège (question 9)** : débit 60 000,00 (BQSIE 01/10) et 20 000,00 (PLSIE 16/11) ; crédit 60 000,00 (PLSIE 01/10) et 20 000,00 (BQSIE 16/11). Solde **0,00 ✓**.

**Solde du 5081100 au 16/11** : 60 000,00 − 20 000,00 = **débiteur 40 000,00**, égal au « capital restant » de l'avis B2 ✓.

### 3.3 À préparer pour le 31/12/2026 — intérêts courus et extourne (question 8)

| Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| OD | 31/12/2026 | 5188000 Intérêts courus à recevoir |  | CAT n° 0081 – ICNE 01/10-31/12 – 40 000 × 2,00 % × 92/365 |  | 201,64 |  |
| OD | 31/12/2026 | 7640000 Revenus des valeurs mobilières de placement |  | CAT n° 0081 – ICNE 01/10-31/12 | 01-SIEGE |  | 201,64 |
| OD | 01/01/2027 | 7640000 Revenus des valeurs mobilières de placement |  | Extourne ICNE CAT n° 0081 au 31/12/2026 | 01-SIEGE | 201,64 |  |
| OD | 01/01/2027 | 5188000 Intérêts courus à recevoir |  | Extourne ICNE CAT n° 0081 au 31/12/2026 |  |  | 201,64 |
| | | | | | **Total** | **403,28** | **403,28** |
## 4. Points d'attention / pièges

- **Une seule écriture 5300000 / 5125000** pour un retrait : interdit par le document T21, et le rapprochement de chaque journal devient impossible.
- **Passer par le 58 entre deux structures** : le 58 ne sert qu'à l'intérieur d'une même comptabilité. Entre structures, c'est la liaison 18 (voir E18-07).
- **Oublier une moitié** du mouvement (ex. : le versement saisi en caisse mais pas en banque) : le 58 reste débiteur. Contrôle : solde du 58 à zéro **chaque mois**, pas seulement au 31/12.
- **Enregistrer les dons nets des dépenses** du goûter, ou émettre des reçus fiscaux pour des dons anonymes.
- **Masquer l'écart de caisse** (en le compensant de sa poche, en le laissant en 4710000, ou en réduisant les dons sans preuve).
- **Suivre le document T21 à la lettre** sur la libération des fonds (« débité ») : le CAT deviendrait 80 000,00 € au lieu de 40 000,00 €.
- **Passer l'ICNE dans PLSIE** : le journal générerait une ligne 5081100, comme si de l'argent avait été versé sur le CAT.
- **Oublier l'extourne** du 01/01/2027 : en octobre 2027, les intérêts du 01/10 au 31/12/2026 seraient comptés une seconde fois.

## 5. Ce qu'un senior ferait en plus

**Procédure de caisse :**

- **Brouillard de caisse** tenu au jour le jour par le responsable (date, objet, entrée, sortie, solde), et comptage **signé à deux** à chaque fin de mois et après chaque événement.
- **Plafond de caisse** (par exemple 300 €, montant à fixer par la direction) : au-delà, versement en banque. Les espèces sont le moyen de paiement le plus exposé au vol et à l'erreur.
- **Pour les événements** : deux personnes au comptage de l'urne, PV signé immédiatement, urne fermée ; **pas de vente** mêlée aux dons, ou, s'il y a des ventes, une liste séparée. Une petite **fiche d'événement** (recettes, dépenses, bénévoles présents) facilite le bilan pour le conseil d'administration.
- **Paiements en espèces** : ils sont plafonnés par la réglementation pour les paiements à des professionnels (*plafond à vérifier chaque année*). Les achats importants se paient par carte ou virement.

**Placements :**

- Tenir un **tableau des placements** (n° de contrat, montant, taux, dates, intérêts courus) : il sert au calcul des ICNE, à l'annexe des comptes et au plan de trésorerie.
- **Coût du retrait anticipé** : le retrait du 16/11 a rapporté 25,21 € au lieu des 50,41 € que les 20 000,00 € auraient produits à 2,00 % sur la même durée. C'est un petit coût, mais le plan de trésorerie (voir E17-06) aurait peut-être permis de placer seulement 40 000,00 € dès le départ.
- **Affectation des produits financiers** : le CAT est au siège, mais la trésorerie placée provient en partie des dotations des services. Les autorités de tarification peuvent demander comment les produits financiers sont répartis ou pris en compte dans les budgets : question à poser à la directrice avant l'ERRD et le compte administratif.

**Documentation** : mail à la Fédération signalant la coquille (classe 50), note écrite sur la question des parts sociales avec la décision prise, PV de caisse du 16/11 signé, classés dans le dossier de clôture.

## 6. Références

- Document interne T21 France « La comptabilité » (30/04/2026) : classe 27 (parts sociales du Crédit Mutuel), classe 50 (placements, avec la coquille sur la libération des fonds), classe 51 (5188 intérêts courus), classe 53 (caisse égale à l'inventaire physique), classe 58 (virements internes, solde nul en fin d'exercice), classe 76 (intérêts sur placements).
- Document interne T21 France « Les journaux comptables » : journaux de banque « placement » et de caisse.
- Plan comptable T21 France (MAJ 13/10/2025) : 2710000, 5040000, 5081XXX, 5188000, 5300000, 5800000, 6062500, 6063000, 6588000, 7541200, 7640000.
- Règlement ANC n° 2022-06 : résultat exceptionnel restreint aux événements majeurs et inhabituels.
- PCG : principe d'indépendance des exercices (rattachement des produits à l'exercice).
