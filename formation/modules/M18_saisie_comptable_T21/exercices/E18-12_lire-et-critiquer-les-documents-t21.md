# E18-12 — Lire et critiquer les documents comptables de Trisomie 21 France
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 30 | **Thèmes :** lecture critique d'une procédure interne, sens des comptes, coquilles et incohérences du plan comptable, TVA et taxe sur les salaires, 6419000, report à nouveau sous gestion contrôlée, réserves 10685xx, gestion contrôlée et non contrôlée, communication avec la direction
**Corner case :** oui — il faut appliquer une procédure de la Fédération **tout en** signalant ses erreurs, sans froisser personne et sans corriger de sa propre autorité

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **BFR** | Besoin en fonds de roulement. Argent immobilisé dans le cycle d'exploitation (stocks + créances clients − dettes fournisseurs). Plus il est élevé, plus l'entreprise a besoin de trésorerie. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CME** | Crédit Mutuel (abréviation du plan T21). Banque coopérative : pour ouvrir un compte, on souscrit des parts sociales. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **DK** | Abréviation d'un lieu dans le plan T21. « SESSAD DK », « SAVS DK » : vraisemblablement Dunkerque. À faire confirmer. |
    | **ESMS** | Établissement ou service médico-social. Autre façon d'écrire ESSMS : une structure autorisée et financée par l'ARS et/ou le Département. |
    | **ESSMS** | Établissement ou service social et médico-social. Structure autorisée par l'ARS et/ou le Département (SESSAD, SAVS, IME, ESAT…). Elle a son propre budget et rend des comptes à son financeur. |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **N+1** | L'exercice suivant. L'année comptable d'après (ex. : si N = 2026, N+1 = 2027). Une charge « de N+1 » ne doit pas peser sur le résultat de N. |
    | **PSB** | Parts sociales (abréviation du plan T21). Dans « PSB CME T21 France (parts sociales) », compte 5040000 : parts sociales détenues au Crédit Mutuel. |
    | **RAN** | Report à nouveau. Résultat d'un exercice pas encore affecté (comptes 115xxxx créditeurs, 1159xxx débiteurs dans le plan T21). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 4671XXX** | Comptes débiteurs et produits à recevoir (plan T21). Créances diverses et produits à recevoir (un sous-compte par débiteur). Libellé identique à 4676000 : à clarifier. |
    | **Compte 1032000** | Fonds propres sattutaires avec droits de reprise (plan T21). Fonds propres de départ qu'un financeur peut reprendre si le service ferme. Le plan écrit « sattutaires » (coquille pour « statutaires »). |
    | **Compte 1068522** | Res invest - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve d'investissement : excédent d'un ESSMS mis de côté, sur décision du financeur, pour financer un investissement. |
    | **Compte 1068552** | Res tréso - Autres éts relevant du I art L.312-1 du CASF (plan T21). Réserve de trésorerie : excédent affecté pour renforcer la trésorerie du service. |
    | **Compte 1068562** | Res compens déficits- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des déficits : couvre un futur déficit. Le document T21 indique qu'elle doit atteindre au moins 5 % de la dotation annuelle. |
    | **Compte 1068572** | Res compens amort- Autres éts relevant  art L.312-1 du CASF (plan T21). Réserve de compensation des charges d'amortissement : couvre les surcoûts d'amortissement d'un investissement. |
    | **Compte 1150120** | RAN ESMS sous gestion contrôlée (créditeur) (plan T21). Report à nouveau excédentaire d'un ESSMS financé par une autorité de tarification (« gestion contrôlée ») : excédent pas encore affecté. |
    | **Compte 1159020** | RAN ESMS sous gestion contrôlée (débiteur) (plan T21). Report à nouveau déficitaire d'un ESSMS sous gestion contrôlée : déficit en attente de reprise. |
    | **Compte 1159220** | Dépenses pour congés payés (plan T21). Congés payés acquis non financés lors du passage à la provision (écriture de transition). À voir avec l'expert-comptable. |
    | **Compte 1202000** | Excédent de l'exercice ESMS sous gestion non contrôlée (plan T21). Excédent de l'exercice d'une activité non tarifée (ex. : vie associative). |
    | **Compte 1205000** | Excédent de l'exercice ESMS sous gestion contrôlée (plan T21). Excédent de l'exercice d'un ESSMS tarifé (SESSAD, SAVS), en attente de décision d'affectation. |
    | **Compte 1292000** | Déficit de l'exercice ESMS sous gestion non contrôlée (plan T21). Déficit de l'exercice d'une activité non tarifée. |
    | **Compte 1295000** | Déficit de l'exercice ESMS sous gestion contrôlée (plan T21). Déficit de l'exercice d'un ESSMS tarifé. |
    | **Compte 1841100** | SIA - Compte liaison exploit° courante BFR (plan T21). Liaison avec la structure « SIA » de la Fédération (code interne : à faire préciser). |
    | **Compte 1842000** | SESSAD DK - Compte liaison exploit° courante BFR (plan T21). Liaison avec le SESSAD « DK » (vraisemblablement Dunkerque : à faire confirmer). |
    | **Compte 1843000** | SAVS DK - Compte liaison exploit° courante BFR (plan T21). Liaison avec le SAVS « DK ». |
    | **Compte 1848000** | 91 - Compte liaison exploit° courante BFR (plan T21). Liaison avec la structure « 91 » (Essonne ; à faire confirmer). |
    | **Compte 2710000** | Titres immobilisés (droit de propriété) (plan T21). Titres détenus durablement (le document T21 y range les parts sociales du Crédit Mutuel ; le plan, lui, a aussi 5040000 : à clarifier). |
    | **Compte 2750000** | Dépôts et cautionnements versés (plan T21). Dépôt de garantie versé (loyer, compteur) : on le récupère à la fin du contrat. |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 4676000** | Comptes débiteurs et Produits à recevoir (plan T21). Produit acquis en N mais pas encore reçu (ex. : remboursement d'assurance accordé). |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 4730000** | Comptes d’attente (plan T21). Second compte d'attente (même libellé que 4710000 : à clarifier). Même règle : soldé au 31/12. |
    | **Compte 5040000** | PSB CME T21 France (parts sociales) (plan T21). Parts sociales du Crédit Mutuel détenues par T21 France (« PSB CME »). Le document range les parts sociales en 27 : à clarifier. |
    | **Compte 6419000** | Remboursements sur rémunération du personnel - IJSS ancien compte 6491000 (plan T21). IJSS versées par la CPAM à l'association (subrogation) : saisies au crédit, en banque. « Charge négative ». Ancien compte 6491000. |
    | **Compte 6479000** | Remboursement aur autres charges sociales (plan T21). Remboursements d'autres charges sociales (le plan écrit « aur » pour « aux »). |
    | **Compte 6611000** | Intêrets des emprunts (plan T21). Intérêts des emprunts (exemple du document T21 : prélevés par la banque). |
    | **Compte 7312130** | ESSMS relevant du 2° du I de l’article L. 312-1 du CASF (plan T21). Dotation de l'autorité de tarification pour un ESSMS du 2° du I de l'article L. 312-1 du CASF (services pour mineurs et jeunes handicapés, ex. : SESSAD). Seule subdivision 731 du plan. |
    | **Compte 7488000** | Autres Subventions et participations (plan T21). Autres subventions (tout financeur sans sous-compte dédié). |
    | **Compte 7541100** | Dons T21 France (plan T21). Dons à T21 France. |
    | **Compte 7556000** | Siège social du gestionnaire (plan T21). Frais de siège reçus par le siège des structures (contrepartie du 6556000). |
    | **Compte 7557000** | Siège social interassociatif (plan T21). Frais de siège interassociatif reçus. |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **facture non parvenue** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **produits à recevoir** | Recette acquise mais pas encore reçue. Ex. : solde d'une subvention AGEFIPH dû au 31/12, versé en mars. |
    | **report à nouveau** | Résultat gardé en attente. Excédent (110) ou déficit (119) reporté sur un budget suivant. |
    | **réserve de compensation** | Excédent mis de côté pour un futur déficit. Compte 10686 : si le service est en déficit plus tard, on puise dans cette réserve. |
    | **subvention affectée** | Subvention donnée pour un projet précis. Elle ne peut servir qu'à ce projet ; ce qui n'est pas dépensé va en fonds dédiés ou est remboursé. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

*Fiche de référence : [les 5 structures et les règles de saisie](../fiche_dossier_5_structures.md).*

## La mise en situation

Lors de votre deuxième semaine, Mme Berthier vous remet trois documents de la Fédération Trisomie 21 France :

1. « **La comptabilité chez Trisomie 21 France** » (8 pages, créé et mis à jour le 30/04/2026) ;
2. « **Les journaux comptables chez Trisomie 21 France** » (3 pages, 30/04/2026) ;
3. le « **Plan comptable général T21 France** » (6 pages, « MAJ le 13/10/2025 – Applicable au 1/01/2025 »).

> « Lisez-les attentivement : c'est notre référence, et l'expert-comptable s'y appuie aussi. Si quelque chose vous paraît faux ou pas clair, notez-le, on en parlera. Je préfère qu'on le voie maintenant plutôt qu'au moment de la clôture. »

Vous avez les trois documents sous les yeux (ce sont de **vrais** documents internes du réseau ; les extraits ci-dessous en sont tirés mot pour mot).

## Les pièces (extraits)

**Extrait 1 — Document 1, § 3.a (classe 40)**
```
Le compte 4081000 sera débité en exercice N, puis crédité en exercice N+1
quand la facture sera reçue et saisie en FO ou LI.
```

**Extrait 2 — Document 1, § 4.a (classe 50)**
```
Se trouvent ici tous les placements réalisés par une structure : Livret
d'épargne, comptes à terme.
Lors de la souscription du placement, le compte est débité, lors de la
libération des fonds, le compte est débité.
```

**Extrait 3 — Document 1, § 3.d (classe 43)**
```
Dans les comptes 43, on retrouve les charges sociales à reverser à l'Etat
(parts patronales et salariales).
```

**Extrait 4 — Document 1, § 2.d (classe 27)**
```
Dans la classe 27, on retrouve les parts sociales du crédit mutuel et les
dépôts et cautionnements versés (loyer, EDF, ...).
```
Et dans le plan comptable (document 3) : `2710000 Titres immobilisés (droit de propriété)` · `2750000 Dépôts et cautionnements versés` · `5040000 PSB CME T21 France (parts sociales)`.

**Extrait 5 — Document 1, § 1.a (classe 10)**
```
Les réserves sont de 3 types : d'investissement, de compensation des déficits
et de trésorerie.
La norme est que la réserve de compensation des déficits doit être d'au moins
5% de la dotation annuelle.
```
Et dans le plan : `1068522 Res invest` · `1068552 Res tréso` · `1068562 Res compens déficits` · `1068572 Res compens amort`.

**Extrait 6 — Plan comptable (document 3), quelques lignes**
```
1032000  Fonds propres sattutaires avec droits de reprise
1150120  RAN ESMS sous gestion contrôlée (créditeur)
1159020  RAN ESMS sous gestion contrôlée (débiteur)
1159220  Dépenses pour congés payés
1202000  Excédent de l'exercice ESMS sous gestion non contrôlée
1205000  Excédent de l'exercice ESMS sous gestion contrôlée
1292000  Déficit de l'exercice ESMS sous gestion non contrôlée
1295000  Déficit de l'exercice ESMS sous gestion contrôlée
1842000  SESSAD DK - Compte liaison exploit° courante BFR
1843000  SAVS DK - Compte liaison exploit° courante BFR
4671XXX  Comptes débiteurs et produits à recevoir
4676000  Comptes débiteurs et Produits à recevoir
4710000  Comptes d'attente
4730000  Comptes d'attente
6419000  Remboursements sur rémunération du personnel - IJSS ancien compte 6491000
6479000  Remboursement aur autres charges sociales
6611000  Intêrets des emprunts
7312130  ESSMS relevant du 2° du I de l'article L. 312-1 du CASF
7488000  Autres Subventions et participations
7556000  Siège social du gestionnaire
7557000  Siège social interassociatif
7541100  Dons T21 France
```

**Extrait 7 — Document 1, introduction**
```
La dernière version est celle de l'arrêté du 19 décembre 2025 applicable
à compter du 1er janvier 2026.
```

## Travail à faire

**Partie A — « Dans quel compte et à quel sens ? »** Pour chaque opération, donnez le compte du plan T21, le sens (débit ou crédit) et le journal, en vous appuyant sur les documents :

1. La CPAM verse 642,18 € d'IJSS au SESSAD.
2. Au 31/12, une facture de psychomotricien de décembre n'est pas arrivée.
3. EDF envoie un avoir de 54,00 € au siège.
4. L'autorité de tarification décide d'affecter 20 000,00 € d'excédent du SESSAD à la réserve de compensation des déficits.
5. Au 31/12, des intérêts sont acquis sur le compte à terme du siège mais ne seront versés qu'en N+1.
6. Au 31/12, 8 000,00 € d'une subvention affectée à un projet n'ont pas été utilisés.
7. Le siège place 50 000,00 € sur son compte à terme (deux journaux).
8. Au 01/01/2027, on extourne une facture non parvenue d'électricité de 1 860,00 €.

**Partie B — Lecture critique**

9. Trouvez **au moins huit** incohérences, erreurs ou coquilles dans les documents (extraits ci-dessus et documents complets). Classez-les : **erreur qui peut fausser une écriture** / **incohérence entre documents** / **simple coquille**.
10. Pourquoi le plan T21 ne contient-il **aucun compte 445** (TVA) ? Quelle conséquence pour la saisie ? Quel compte du plan est un indice que les structures ne sont pas soumises à la TVA ?
11. Pourquoi le compte **6419000** (une charge) fonctionne-t-il **au crédit** ? Que signifie « ancien compte 6491000 » ?
12. Expliquez la différence entre **1150120** et **1159020**. Pourquoi ne pas tout mettre dans un seul compte de report à nouveau ? À quoi peut servir **1159220** « Dépenses pour congés payés » ?
13. Les **réserves 10685xx** : combien de types le document décrit-il, combien le plan en contient-il ? Application de la « norme » des 5 % : la dotation 2026 du SESSAD est de **1 296 000,00 €** et le compte 1068562 du SESSAD présente un solde de **41 300,00 €**. La norme est-elle respectée ? Quelles précautions de langage prendre ?
14. Expliquez simplement « ESMS **sous gestion contrôlée** » et « **sous gestion non contrôlée** ». Dans laquelle rangeriez-vous chacune des 5 structures de Cap Horizons 21 ? Soyez prudente.
15. Le compte **7312130** est la seule subdivision des dotations dans le plan. Est-ce suffisant pour Cap Horizons 21 ?
16. Les comptes **1841100 à 1848000** portent des noms comme « SESSAD DK », « SAVS DK », « 56 », « 93 ». Que vous apprennent-ils sur ce plan comptable ?

**Partie C — Communication**

17. Rédigez le **mail à Mme Berthier** qui présente vos remarques de façon **diplomatique** et **utile** (ce qui change pour la saisie, ce qui peut attendre, ce que vous proposez).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-12_corrige.md)
