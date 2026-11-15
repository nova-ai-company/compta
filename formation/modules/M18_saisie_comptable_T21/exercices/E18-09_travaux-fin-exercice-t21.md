# E18-09 — Les travaux de fin d'exercice au 31/12/2026, structure par structure
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★★ | **Durée estimée :** 2 h 30 | **Thèmes :** factures non parvenues (4081000), charges constatées d'avance (4860000), produits constatés d'avance sur subvention (4878000), produits à recevoir (4676000), charges à payer (4686000), intérêts courus (1648000 / 6618000), fonds dédiés (6892200 / 1940000 ou 1950000 / 7892200), congés payés (4282000 / 4382000), comptes 47, 58 et 18 à zéro, extournes du 01/01/2027
**Corner case :** oui — le document interne T21 donne le **mauvais sens** pour le compte 4081000 ; et une charge commune régularisée à la clôture doit l'être **dans chaque structure**, pas seulement au siège

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **EIG** | Suite de logiciels de gestion utilisée par Trisomie 21 France. Logiciels qui alimentent la comptabilité : EIG RH (paie), EIG IMMOS (immobilisations), EIG Gestion commerciale (factures de vente). Leurs journaux sont automatiques : on ne les saisit pas à la main. |
    | **EMP** | Structure Emploi accompagné (dossier M18). Dispositif d'emploi accompagné (ARS, AGEFIPH, FIPHFP). |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **N+1** | L'exercice suivant. L'année comptable d'après (ex. : si N = 2026, N+1 = 2027). Une charge « de N+1 » ne doit pas peser sur le résultat de N. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **OPCO** | Opérateur de compétences. Organisme qui finance la formation professionnelle des salariés de la branche. |
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
    | **Compte 1648000** | Intérêts courus sur emprunts auprès des Ets de crédit (plan T21). Intérêts courus non échus (ICNE) : intérêts de l'exercice qui seront payés l'an prochain. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 1849200** | Liaison SAVS (dossier M18, fictif). Dans les livres du siège : compte de liaison avec le SAVS. Solde opposé au 1840000 chez le SAVS. |
    | **Compte 1849300** | Liaison Emploi accompagné (dossier M18, fictif). Dans les livres du siège : compte de liaison avec l'emploi accompagné. Solde opposé au 1840000 chez l'Emploi. |
    | **Compte 1849400** | Liaison Association (dossier M18, fictif). Dans les livres du siège : compte de liaison avec la structure Association et projets. Solde opposé au 1840000 chez l'Association. |
    | **Compte 1940000** | Fonds dédiés sur subventions d'exploitation (plan T21). Subvention d'exploitation affectée à un projet et non dépensée au 31/12 (ex. : fondation pour le projet Pairs). |
    | **Compte 1950000** | Fonds dédiés sur contribution financières d'autres organismes (plan T21). Contributions financières d'autres organismes (ex. : fondation d'entreprise) non utilisées. |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4282000** | Dettes provisionnées pour congés à payer (plan T21). Congés payés acquis et non pris à la clôture (dette envers les salariés). |
    | **Compte 4382000** | Charges sociales sur congés à payer (plan T21). Charges sociales sur les congés payés provisionnés. |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4686000** | Comptes créditeurs et Charges à payer (plan T21). Charge de N à payer qui n'est ni un fournisseur, ni une dette sociale ou fiscale. |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4860000** | Charges constatées d’avance (plan T21). Charge constatée d'avance : facturée en N mais concernant N+1 (ex. : assurance avril N – mars N+1). |
    | **Compte 4878000** | Produits constatés d’avance - Subventions (plan T21). Subvention reçue en N pour une période de N+1 (ex. : année scolaire). |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 6161000** | Assurance Multirisques (plan T21). Assurance multirisque des locaux. |
    | **Compte 6618000** | Autres charges d'intérêt - intérêts courus (plan T21). Intérêts courus à la clôture (ICNE). |
    | **Compte 6892200** | Report en fonds dédiés à l'exploitation (plan T21). Mise en fonds dédiés de la part non dépensée d'une subvention d'exploitation affectée. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7892200** | Fonds dédiés - Exploitation (plan T21). Utilisation, l'année suivante, des fonds dédiés d'exploitation (quand on dépense enfin la subvention). |
    | **FOFERRAND** | Compte fournisseur expert-comptable (dossier M18). Honoraires de comptabilité et de paie (6226010), répartis en IS. |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOMAAF** | Compte fournisseur assurances (dossier M18). Mutuelle d'assurance : multirisque, flotte automobile, responsabilité civile. |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **charge commune** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **charges constatées d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **clés de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **extourner** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **habitat inclusif** | Logement partagé en milieu ordinaire. Des personnes handicapées vivent ensemble chez elles, avec un projet de vie partagé animé par l'association. |
    | **produits à recevoir** | Recette acquise mais pas encore reçue. Ex. : solde d'une subvention AGEFIPH dû au 31/12, versé en mars. |
    | **subvention affectée** | Subvention donnée pour un projet précis. Elle ne peut servir qu'à ce projet ; ce qui n'est pas dépensé va en fonds dédiés ou est remboursé. |
<!-- /glossaire-page -->

*Avant de commencer, relisez la [fiche du dossier](../fiche_dossier_5_structures.md) : les 5 structures (SIE, SES, SAV, EMP, ASS), les comptes de liaison 184xxxx, les clés de répartition et les règles maison.*

## La mise en situation

Nous sommes le **8 janvier 2027**. Vous êtes agent comptable de Cap Horizons 21 depuis six mois. La directrice, **Mme Nathalie Berthier**, vous écrit :

> « Bonjour, Hélène Ferrand (notre expert-comptable) vient réviser le **2 février**. Elle veut trouver les écritures d'inventaire passées dans **les cinq structures**, les comptes d'attente soldés et les comptes de liaison concordants. Vous trouverez ci-dessous tout ce que j'ai pu rassembler. Le document de la Fédération sur la comptabilité dit quelque chose sur le compte 4081000 qui me paraît bizarre : pouvez-vous vérifier ? Merci, N. Berthier »

Rappels utiles :

- Exercice du **01/01 au 31/12**. Chaque structure a sa propre balance (voir la fiche).
- **Pas de TVA récupérable** : tous les montants sont **TTC** et vont en charge TTC.
- Les écritures d'inventaire passent au journal **OD** (opérations diverses), le seul journal manuel « avec contrepartie » où tous les comptes sont permis.
- Les écritures d'inventaire 2025 ont été **extournées le 01/01/2026** (extourner = passer au premier jour de l'exercice suivant l'écriture inverse, pour l'annuler).
- Clés de répartition (fiche, § 5) : **m²** = SIE 15 % · SES 45 % · SAV 25 % · EMP 10 % · ASS 5 % ; **ETP** = 9 % · 48 % · 27 % · 12 % · 4 % ; **forfait** honoraires = 20 % · 40 % · 20 % · 10 % · 10 %.

## Les pièces

**Information 1 — Électricité des locaux de Valence (EDF, contrat unique au siège)**
```
Facture bimestrielle novembre-décembre 2026 attendue fin janvier 2027.
Estimation faite à partir des relevés du compteur : 1 860,00 € TTC.
Les factures EDF sont saisies au siège et réparties en IS selon la clé m².
```

**Information 2 — Cabinet Hélène Ferrand (FOFERRAND)**
```
Honoraires de paie de décembre 2026 et d'assistance à la clôture
(travaux faits en décembre) : 2 280,00 € TTC.
La facture sera émise le 15/01/2027. Clé : forfait honoraires.
```

**Information 3 — Orthophonie du SESSAD (LIDUPONT)**
```
Relevé de séances de Claire Dupont, orthophoniste libérale conventionnée :
décembre 2026 = 18 séances × 34,00 € (tarif de la convention, valeur fictive).
Sa facture de décembre arrive toujours vers le 10 du mois suivant.
```

**Information 4 — Assurance multirisque des locaux (FOMAAF)**
```
Prime annuelle du 01/04/2026 au 31/03/2027 : 7 200,00 € (taxes comprises).
Saisie en avril 2026 au siège, compte 6161000, et répartie en IS selon la clé m²
(chaque structure a donc sa part dans SON compte 6161000).
```

**Information 5 — Emprunt du SESSAD (Crédit Mutuel)**
```
Emprunt de 60 000,00 € souscrit en 2024 pour l'aménagement des locaux du SESSAD.
Échéances trimestrielles : 31/01, 30/04, 31/07, 31/10.
Échéance du 31/01/2027 : capital 2 912,00 € + intérêts 438,00 €.
Les intérêts de cette échéance couvrent la période du 01/11/2026 au 31/01/2027.
```

**Information 6 — AGEFIPH, emploi accompagné (structure EMP)**
```
Convention n° 2026-EA-26-117 (fictive) : 24 000,00 € pour la période du
01/07/2026 au 30/06/2027 (12 mois d'accompagnement, dépenses réparties
régulièrement sur la période).
Versements reçus en 2026 : 12 000,00 € en juillet, 12 000,00 € en novembre,
comptabilisés au crédit du compte 7488000 Autres subventions et participations.
```

**Information 7 — Formation d'une monitrice-éducatrice du SAVS**
```
OPCO (opérateur de compétences) : accord de prise en charge du 14/10/2026,
1 450,00 € pour la formation « Accompagner la vie affective » suivie
du 16 au 20/11/2026 (facture de l'organisme payée en novembre par le SAVS).
L'OPCO rembourse sur justificatifs : versement attendu en février 2027.
```

**Information 8 — Frais des bénévoles (structure ASS)**
```
Conseil d'administration du 12/12/2026 : les administrateurs bénévoles
demandent le remboursement de leurs frais de déplacement.
État récapitulatif signé par la trésorière, remis le 06/01/2027 : 386,40 €.
(Les bénévoles ne sont pas salariés : ils n'ont pas de compte SA.)
```

**Information 9 — Projet « Pairs et voix » (structure ASS, code analytique 50-PAIRS)**
```
Fondation Lumen (fondation privée, fictive) : subvention affectée au projet,
40 000,00 € versés en mars 2026, comptabilisés au crédit du compte 7488000.
La convention couvre les dépenses du projet jusqu'au 30/06/2027 ; la part
non utilisée à cette date est à restituer.
Dépenses du projet en 2026 (état analytique 50-PAIRS) : 27 350,00 €.
Pas de fonds dédiés au 31/12/2025 (projet démarré en 2026).
Prévision : les dépenses restantes seront faites en totalité avant le 30/06/2027.
```

**Information 10 — Congés payés acquis et non pris au 31/12/2026**

État « Provision congés payés » édité par **EIG RH** (le logiciel de paie) le 05/01/2027 :

| Structure | Congés payés bruts restant dus | Charges patronales (taux moyen retenu : 42 %, *valeur à vérifier chaque année*) |
|---|---|---|
| SIE | 10 250,00 € | à calculer |
| SES | 61 300,00 € | à calculer |
| SAV | 32 480,00 € | à calculer |
| EMP | 13 120,00 € | à calculer |
| ASS (habitat inclusif, 40-HABITAT) | 4 150,00 € | à calculer |
| **Total** | **121 300,00 €** | |

*EIG RH, chez Cap Horizons 21, édite l'état mais ne déverse pas l'écriture de provision dans le journal de paie (hypothèse : à vérifier dans le paramétrage).*

**Information 11 — Extrait des balances des 5 structures au 31/12/2026, avant écritures d'inventaire**

| Structure | Compte | Intitulé | Solde débiteur | Solde créditeur |
|---|---|---|---|---|
| SIE | 1849100 | Liaison SESSAD | 18 640,20 | |
| SIE | 1849200 | Liaison SAVS | 9 875,40 | |
| SIE | 1849300 | Liaison Emploi | 3 214,60 | |
| SIE | 1849400 | Liaison Association | | 1 120,00 |
| SES | 1840000 | Liaison Siège | | 18 640,20 |
| SAV | 1840000 | Liaison Siège | | 9 443,40 |
| EMP | 1840000 | Liaison Siège | | 3 214,60 |
| ASS | 1840000 | Liaison Siège | 1 120,00 | |
| SES | 4710000 | Comptes d'attente | 214,80 | |
| ASS | 5800000 | Virements internes | 300,00 | |

Notes jointes par Mme Berthier :

- **SES, 4710000** : prélèvement du 18/12/2026 « LUDIK EDUCATION 214,80 » mis en attente. Vérification faite, c'est le règlement de la facture n° LE-2026-1187 de 214,80 € du 02/12/2026, **déjà saisie** au journal des achats sur FOLUDIK.
- **ASS, 5800000** : retrait de 300,00 € au distributeur le 11/12/2026 pour la caisse du marché de Noël. La sortie de banque a été saisie (BQASS : 5800000 au débit). Le carnet de caisse indique bien l'entrée de 300,00 € le 11/12/2026, mais **rien n'a été saisi** dans le journal de caisse CAASS.
- **SIE / SAV** : le siège a saisi le 30/12/2026 la facture Orange de décembre (1 600,00 €) avec l'IS vers le SAVS (27 % = 432,00 €). Dans le SAVS, l'écriture « miroir » n'a pas été générée.

**Information 12 — Extrait du document « La comptabilité chez Trisomie 21 France » (30/04/2026), § 3.a**
```
« Ceci se fera par l'intermédiaire du compte 4081000 qui vient ici
« remplacer » le compte FO ou LI.
Le compte 4081000 sera débité en exercice N, puis crédité en exercice N+1
quand la facture sera reçue et saisie en FO ou LI. »
```

## Travail à faire

1. **Information 12** : la phrase du document T21 est-elle juste ? Expliquez avec un raisonnement simple (« la facture n'est pas arrivée, mais on doit quand même… ») et donnez la bonne écriture au 31/12/2026 et au 01/01/2027.
2. Pour chaque information 1 à 10, indiquez dans un tableau : la (ou les) **structure(s)** concernée(s), le **principe** (rattacher la charge ou le produit au bon exercice), les **comptes** et le **montant**.
3. Passez toutes les **écritures d'inventaire au 31/12/2026**, en indiquant pour chaque ligne **dans quels livres** (SIE, SES, SAV, EMP, ASS) elle est passée et le **code analytique**. N'oubliez pas les écritures « miroir » des IS.
4. **Information 4** : expliquez pourquoi la charge constatée d'avance ne se passe pas seulement au siège.
5. **Information 6 et information 9** : l'une donne un **produit constaté d'avance**, l'autre des **fonds dédiés**. Expliquez la différence. Pour les fonds dédiés, choisissez entre **1940000** et **1950000** en vous appuyant sur les intitulés du plan comptable T21, et passez l'écriture de **reprise** que l'on fera en 2027.
6. **Information 10** : qui calcule les congés payés ? Dans quel journal passe l'écriture ? Que faut-il vérifier avant de la passer ?
7. **Information 11** : passez les écritures qui soldent le 4710000 et le 5800000 et qui rendent les comptes de liaison concordants. Présentez le tableau de contrôle des comptes 18 après correction.
8. Listez les écritures à **extourner le 01/01/2027** et montrez, sur une écriture, que la charge est alors **saisie au crédit** (l'« exception » du document T21).
9. Calculez l'**impact** de vos écritures sur le résultat de **chaque structure**.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-09_corrige.md)
