# Corrigé E17-03 — Remonter les variables de paie d'octobre au service paie

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **BOFiP** | Bulletin officiel des finances publiques. La doctrine officielle de l'administration fiscale : elle explique comment l'administration applique la loi. |
    | **BQ** | Journal de banque. Journal qui reprend les mouvements du relevé bancaire. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CCN** | Convention collective nationale. Accord de branche qui complète le Code du travail (salaires minimaux, primes, congés…). |
    | **CCN 66** | Convention collective nationale du 15 mars 1966. Convention collective très répandue dans le secteur social et médico-social (établissements pour personnes inadaptées et handicapées). |
    | **CDD** | Contrat à durée déterminée. Contrat de travail avec une date de fin ; donne souvent droit à une indemnité de fin de contrat. |
    | **CDI** | Contrat à durée indéterminée. Contrat de travail sans date de fin. |
    | **CGI** | Code général des impôts. Le code qui contient toutes les règles fiscales (TVA, IS, IR…). « art. 39 CGI » = article 39 de ce code. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **DPAE** | Déclaration préalable à l'embauche. Déclaration à l'URSSAF obligatoire AVANT l'arrivée de tout nouveau salarié. |
    | **DSN** | Déclaration sociale nominative. Déclaration mensuelle de la paie envoyée par l'entreprise : elle remplace la plupart des déclarations sociales. Due le 5 ou le 15 du mois suivant selon l'effectif. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **PCG** | Plan comptable général. Le référentiel comptable français : liste des comptes (classes 1 à 7) et règles d'enregistrement. Version applicable : règlement ANC 2014-03 modifié par l'ANC 2022-06. |
    | **RIB** | Relevé d'identité bancaire. Document qui donne les coordonnées bancaires (IBAN, BIC) d'un compte. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **URSSAF** | Organisme de recouvrement des cotisations sociales. Collecte les cotisations sociales (maladie, famille, CSG…) des salariés et des indépendants. |
    | **Compte 425** | Personnel. Avances et acomptes : argent avancé à un salarié avant la paie. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E17-03](../exercices/E17-03_variables-paie-octobre.md)

!!! abstract "En clair"
    Vous n'avez pas à tout savoir, mais vous devez **tout transmettre** et **dire clairement ce qui est incertain**. Une ligne « à confirmer » protège le salarié et l'association. Un oubli, lui, se découvre trop tard, sur le bulletin.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### La méthode

1. Lire **toutes** les pièces avant d'écrire la moindre ligne : une même personne apparaît souvent dans deux mails (Hugo Petit est cité par Karim **et** par Sophie).
2. Faire **une ligne par événement** et par salarié.
3. Pour chaque ligne, se demander : **ai-je le justificatif ?** Si non, la ligne part quand même, marquée « à confirmer », et le manque va dans la liste des relances.
4. Repérer ce qui ne concerne **pas** le mois d'octobre (événement après le 20/10, prise d'effet en novembre) et le dire.

### Question 2 — Les heures complémentaires d'Inès Roche

Un salarié à **temps partiel** ne fait pas des « heures supplémentaires » mais des **heures complémentaires** : ce sont les heures faites au-delà de son contrat, sans atteindre 35 h.

- Durée du contrat : 28 h par semaine. Le **dixième** : 28 × 10 % = **2,8 h** par semaine.
- Jusqu'à 2,8 h de plus dans la semaine : majoration de **10 %**. Au-delà : **25 %**.

| Semaine | Heures en plus | à 10 % | à 25 % | Transmise en octobre ? |
|---|---|---|---|---|
| 41 | 32 − 28 = 4 h | 2,8 h | 1,2 h | Oui (réalisée, visée) |
| 42 | 30 − 28 = 2 h | 2,0 h | 0,0 h | Oui (réalisée, visée) |
| 43 | 34 − 28 = 6 h | 2,8 h | 3,2 h | **Non** : semaine pas encore faite au 20/10 → **paie de novembre**, sur le planning réalisé |
| **Octobre** | **6 h** | **4,8 h** | **1,2 h** | |

On ne transmet jamais des heures **prévues** : on paie des heures **faites et visées** par la cheffe de service.

Deux alertes pour le service paie :
- En semaine 41 (et en semaine 43), Inès a dépassé le dixième de son contrat. C'est possible seulement si un **accord collectif** le permet *(à vérifier pour la CCN 66)*.
- Si, pendant **12 semaines**, Inès fait en moyenne **2 h ou plus** au-delà de son contrat, son horaire contractuel doit en principe être revu *(règle du Code du travail, à vérifier)*. Il faut surveiller le cumul sur les prochains mois.

### Question 3 — La sortie d'Hugo Petit

Ce qu'on transmet :
- **Date de fin du CDD** : 23/10/2026 (CDD de remplacement de M. Royer, congé parental), service SAVS.
- **Congés acquis non pris** : 4,5 jours → **indemnité compensatrice de congés payés**, calculée par le service paie.
- **Documents de fin de contrat** à préparer par le service paie : certificat de travail, attestation pour France Travail, reçu pour solde de tout compte.
- **L'indemnité de fin de contrat** (souvent appelée « prime de précarité », en principe **10 %** de la rémunération brute totale du CDD) : **à confirmer**.

Pourquoi « à confirmer » ? En principe, cette indemnité **n'est pas due** lorsque le CDD se poursuit **par un CDI** chez le même employeur. Mais ici :
- il y a **9 jours** sans contrat entre les deux (du 24/10 au 01/11) ;
- le CDI est sur **un autre poste**, dans **un autre service** (SESSAD au lieu de SAVS).

Ce n'est pas à l'agent comptable de trancher. La **directrice** décide, avec l'avis du **service paie** (et de leur juriste si besoin). Votre rôle : poser la question **par écrit**, avec les dates.

Autres points à signaler :
- Le **taux** de l'indemnité peut être réduit (6 %) si un accord de branche prévoit des contreparties de formation *(à vérifier pour la CCN 66)*.
- Dans le secteur médico-social, les CDD sont surtout des **CDD de remplacement**. Ils ouvrent droit en principe à l'indemnité de fin de contrat, contrairement aux « CDD d'usage » réservés à certains secteurs *(liste des secteurs à vérifier)*.
- Pour le CDI du 02/11 : **nouvelle DPAE** (déclaration préalable à l'embauche) à faire **avant** le 02/11, et nouvelle ligne « entrée » dans les variables de **novembre**.

### Les autres points délicats

- **Claire Dumas** : l'arrêt reçu va du 05/10 au 16/10. Le planning la dit « absente » du 19/10 au 23/10 **sans motif**. Est-ce une **prolongation** d'arrêt (il faut l'avis), des **congés** (il faut la demande validée) ou autre chose ? Tant qu'on ne sait pas, le service paie ne peut ni maintenir le salaire ni faire la déclaration à la CPAM.
- **Amandine Faure** : la directrice confirme le remplacement **à l'oral**. Pour une indemnité, il faut **un écrit** : une note de la directrice avec les dates et les fonctions remplacées. Le service paie vérifie ensuite si les conditions de la CCN 66 sont remplies (durée minimale, montant) *(à vérifier dans la convention)*.
- **Malik Benoît** : une absence non justifiée n'est **pas payée**, mais on ne retient pas le salaire « à l'aveugle ». On transmet « absence non rémunérée, 1 jour, **à confirmer** », et la directrice confirme le 21/10 au matin si aucun justificatif n'est arrivé. Une **retenue sur salaire** pour absence est autorisée. En revanche, l'éventuelle **sanction** relève de la directrice, pas de la paie.
- **Léa Moulin** : sans **RIB**, on ne peut pas lui virer son salaire le 28/10. Sans **attestation de Sécurité sociale**, la DSN sera en anomalie. Sans **certificats de travail**, le service paie applique une ancienneté provisoire (régularisation ensuite). Sans **demande écrite de dispense** avec justificatif, elle est affiliée **d'office** à la mutuelle de l'association.
- **Rachid Haddad** : passer en formule « famille » demande l'**acte de naissance** (ou le livret de famille) et le **bulletin de modification** de l'organisme. La date d'effet dépend du contrat de mutuelle (souvent le 1er du mois suivant) : **paie de novembre** probablement.
- **Thomas Girard** : le logiciel de paie applique en général les avancements d'échelon seul. On le signale quand même **pour contrôle**, c'est une source d'erreur fréquente.

## 2. Calculs (détaillés, chaque montant justifié)

**Question 1 — Fichier des variables d'octobre 2026**

| Salarié | Service (code) | Rubrique | Dates / quantité | Justificatif reçu | Remarque |
|---|---|---|---|---|---|
| Léa Moulin | SESSAD (10-SESSAD) | **Entrée** CDI, psychomotricienne, 17 h 30/semaine (0,5 ETP) | Depuis le 19/10/2026 | Contrat oui, DPAE oui (14/10), diplôme oui | **Manquent** : attestation Sécurité sociale, RIB, certificats de travail (ancienneté CCN), dispense de mutuelle |
| Léa Moulin | SESSAD (10-SESSAD) | Mutuelle | — | **Non** | Dispense demandée oralement : **sans document, affiliation** |
| Hugo Petit | SAVS (20-SAVS) | **Sortie** – fin de CDD de remplacement | 23/10/2026 | Contrat oui | Congés non pris : **4,5 jours** (indemnité compensatrice). Documents de fin de contrat à établir |
| Hugo Petit | SAVS (20-SAVS) | Indemnité de fin de contrat | — | — | **À CONFIRMER** : CDI au SESSAD le 02/11 (9 jours d'écart, autre poste). Décision : directrice + service paie |
| Claire Dumas | SESSAD (10-SESSAD) | Arrêt maladie non professionnelle, **subrogation** | 05/10 → 16/10/2026 (12 jours) | Oui (avis d'arrêt) | Signalement d'arrêt et attestation de salaire par le service paie |
| Claire Dumas | SESSAD (10-SESSAD) | Absence | 19/10 → 23/10/2026 | **Non** | **Motif inconnu** : prolongation d'arrêt ? congés ? À CONFIRMER |
| Inès Roche | SAVS (20-SAVS) | Heures complémentaires à 10 % | **4,8 h** | Oui (planning visé S41-S42) | Taux horaire 16,20 €. Semaine 43 → paie de novembre |
| Inès Roche | SAVS (20-SAVS) | Heures complémentaires à 25 % | **1,2 h** | Oui | Dépassement du dixième : **accord collectif** à vérifier |
| Thomas Girard | SESSAD (10-SESSAD) | Avancement d'échelon (ancienneté) | Au 01/10/2026 | Oui (tableau de la directrice) | À contrôler sur le bulletin |
| Thomas Girard | SESSAD (10-SESSAD) | Congés payés | 26/10 → 30/10/2026 | Oui (mail du chef de service) | Congés posés après le 20/10, déjà validés |
| Rachid Haddad | SAVS 70 % / Habitat 30 % (20-SAVS / 40-HABITAT) | Congés payés | 19/10 → 23/10/2026 | Oui | — |
| Rachid Haddad | SAVS / Habitat | Mutuelle : passage en formule « famille » | Naissance le 02/10/2026 | **Non** | Acte de naissance + bulletin de modification à fournir. Date d'effet selon contrat (sans doute **novembre**) |
| Julie Marchetti | Emploi accompagné (30-EMPLOI) | Congés trimestriels (CCN 66) | 29/10 et 30/10/2026 (2 jours) | Oui (mail de la cheffe de service) | *Droit conventionnel à vérifier selon le poste* |
| Amandine Faure | SESSAD (10-SESSAD) | Indemnité de remplacement du chef de service | 05/10 → 16/10/2026 | **Non** (accord oral) | **À CONFIRMER** : note écrite de la directrice ; conditions CCN 66 à vérifier par le service paie |
| Malik Benoît | Siège (01-SIEGE) | Absence non rémunérée | 13/10/2026 : 1 jour (7 h) | **Non** (pas de justificatif) | **À CONFIRMER** le 21/10 au matin par la directrice |
| Malik Benoît | Siège (01-SIEGE) | **Acompte** à déduire | 400,00 € versés le 15/10/2026 | Oui (virement) | — |

**Montant indicatif des heures complémentaires d'Inès** (pour contrôler le bulletin, pas pour le calculer à la place du service paie) :
- 4,8 h × 16,20 € × 1,10 = **85,54 €**
- 1,2 h × 16,20 € × 1,25 = **24,30 €**
- Total : **109,84 €** brut.

**Question 4 — Les informations manquantes**

| N° | Ce qui manque | À qui le demander | Pour quand |
|---|---|---|---|
| 1 | Attestation de Sécurité sociale et **RIB** de Léa Moulin | Léa Moulin (copie : Karim Belkacem) | **21/10 matin** (salaire viré le 28/10) |
| 2 | Certificats de travail de Léa Moulin | Léa Moulin | Fin octobre (sinon régularisation en novembre) |
| 3 | Demande écrite de dispense de mutuelle + attestation de la mutuelle du conjoint | Léa Moulin | Fin octobre (sinon affiliation) |
| 4 | Motif de l'absence de Claire Dumas du 19 au 23/10 | Karim Belkacem, puis Claire Dumas | **21/10 matin** |
| 5 | Note écrite sur le remplacement d'Amandine Faure (dates, fonctions) | Nathalie Berthier | 21/10 matin |
| 6 | Justificatif de l'absence du 13/10 (ou confirmation de la retenue) | Nathalie Berthier | 21/10 matin |
| 7 | Décision sur l'indemnité de fin de contrat d'Hugo Petit | Nathalie Berthier, avec le service paie | Avant le 23/10 |
| 8 | DPAE d'Hugo Petit pour le CDI du 02/11 | Nathalie Berthier | Avant le 02/11 |
| 9 | Acte de naissance et bulletin de modification mutuelle | Rachid Haddad | Pour la paie de novembre |
| 10 | Planning réalisé de la semaine 43 d'Inès Roche | Sophie Laurent | Variables de novembre |

## 3. Écritures comptables

Les variables ne donnent pas d'écriture : c'est le **journal de paie** du service paie qui sera comptabilisé (voir E17-04). La seule écriture du mois à ce stade est l'**acompte** versé à Malik Benoît le 15/10 (question 7).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | BQ | 425 | Personnel – avances et acomptes | Acompte sur salaire d'octobre – M. Benoît | 400,00 | |
| 15/10/2026 | BQ | 512 | Banque | Acompte sur salaire d'octobre – M. Benoît | | 400,00 |
| | | | | **Totaux** | **400,00** | **400,00** |

Le compte 425 sera **soldé** par l'écriture de paie d'octobre, quand l'acompte sera retenu sur le net (crédit 425). Un 425 qui ne se solde pas, c'est un acompte **oublié** dans les variables.

## 4. Points d'attention / pièges

- **Oublier une entrée ou une sortie** parce que l'information est arrivée par un autre canal (le mail de Karim parle d'Hugo, qui dépend de Sophie).
- **Transmettre des heures prévues** comme des heures faites (semaine 43 d'Inès).
- **Décider seul de l'indemnité de fin de contrat**. Ce n'est pas une question de comptabilité, c'est une question de **droit du travail** : on la pose, on ne la tranche pas.
- **Accepter une dispense de mutuelle « orale »** : sans demande écrite et justificatif, la dispense n'est pas valable, et l'association risque un redressement sur la part patronale *(règles des dispenses à vérifier)*.
- **Retenir une absence sans vérifier** : si le salarié avait envoyé un arrêt maladie, la retenue serait fausse et le climat social abîmé.
- **Payer une indemnité promise à l'oral** : sans écrit, rien ne prouve le droit, et le CAC ou un contrôle URSSAF peut le relever.
- **Oublier l'acompte** : le salarié serait payé deux fois 400,00 €, et le compte 425 resterait débiteur.
- **Mettre les frais de déplacement dans les variables** : chez Cap Horizons 21, ils passent par les états de frais (E17-05), pas par la paie.

> 💡 Réflexe senior : gardez **une copie datée** de chaque envoi de variables et des réponses. Quand un salarié conteste son bulletin trois mois plus tard, c'est le seul moyen de savoir si l'erreur vient de l'information transmise ou du calcul.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail au service paie (question 5) :**

> Objet : Cap Horizons 21 — variables de paie d'octobre 2026 (1 entrée, 1 sortie, 4 points à confirmer)
>
> Bonjour Hélène,
>
> Vous trouverez ci-joint le fichier des variables d'octobre (arrêtées au 20/10) et les justificatifs reçus.
>
> **Mouvements** : entrée de Léa Moulin le 19/10 (CDI mi-temps, SESSAD) ; sortie d'Hugo Petit le 23/10 (fin de CDD de remplacement, 4,5 jours de congés non pris). Hugo Petit signe un CDI au SESSAD le 02/11 : **pouvez-vous nous dire si l'indemnité de fin de contrat est due**, compte tenu des 9 jours d'écart et du changement de poste ? La directrice tranchera avec votre avis.
>
> **À confirmer d'ici demain midi** : motif de l'absence de Claire Dumas du 19 au 23/10 ; absence de Malik Benoît le 13/10 ; indemnité de remplacement d'Amandine Faure (note écrite en cours).
>
> **Pièces manquantes pour Léa Moulin** : attestation de Sécurité sociale et RIB (relancés), certificats de travail (ancienneté provisoire en attendant), dispense de mutuelle non documentée (affiliation à défaut).
>
> **Pour novembre** : semaine 43 d'Inès Roche (heures complémentaires sur le réalisé) ; passage de Rachid Haddad en mutuelle « famille ».
>
> Je reste disponible. Bonne journée,
> [Prénom Nom], agent comptable — Cap Horizons 21

**Question 6 — Check-list mensuelle des variables**

1. Entrées du mois : contrat, DPAE, Sécurité sociale, RIB, diplôme, mutuelle (adhésion ou dispense écrite).
2. Sorties du mois : date, motif, congés non pris, indemnités, documents de fin de contrat.
3. Arrêts de travail : avis reçu, dates, prolongations, subrogation.
4. Absences autres (congés, congés trimestriels, absences non rémunérées, événements familiaux) : demande validée.
5. Heures complémentaires et supplémentaires : planning **réalisé** et visé.
6. Primes et indemnités : décision **écrite** de la directrice.
7. Changements de situation : échelon, coefficient, temps de travail, service (et donc **code analytique**).
8. Mutuelle et prévoyance : adhésions, changements de formule, dispenses.
9. Acomptes et avances versés dans le mois (compte 425).
10. Envoi avant la date limite, copie datée, liste des points « à confirmer » relancée le lendemain.

**Pour aller plus loin :** demander au service paie un **état des écarts** entre le mois précédent et le mois en cours (salarié par salarié). C'est le meilleur contrôle de cohérence avant la validation des bulletins par la directrice.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code du travail : heures complémentaires des salariés à temps partiel (majorations de 10 % et 25 %, limite du dixième ou du tiers par accord), indemnité de fin de contrat du CDD et ses exceptions, DPAE, acompte sur salaire (*articles à citer selon le texte en vigueur*).
- Code de la sécurité sociale : indemnités journalières et subrogation de l'employeur (*références à vérifier*).
- Convention collective nationale du 15 mars 1966 : classification, avancement d'échelon, congés trimestriels, indemnités de remplacement (*hypothèse de l'association ; articles à vérifier dans la convention*).
- PCG : compte 425 « Personnel – avances et acomptes ».
- Fiche de l'association Cap Horizons 21 : paie établie par le service paie de l'expert-comptable.
