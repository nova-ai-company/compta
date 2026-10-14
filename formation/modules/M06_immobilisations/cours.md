# M06 — Les immobilisations, de l'acquisition à la sortie

> **Objectif du module.** Les immobilisations pèsent souvent plus de la moitié du bilan de vos clients, et chaque erreur sur une immobilisation se répète **pendant toute sa durée d'amortissement** : une facture passée en charge à tort, un composant oublié, une durée mal choisie, une sortie jamais constatée… et ce sont cinq, dix ou cinquante ans de comptes faux. Un senior sait (1) **qualifier** une dépense (charge ou actif ?), (2) **mesurer** le coût d'entrée, (3) **construire un plan d'amortissement** défendable comptablement et fiscalement, (4) **tester** la valeur à la clôture, (5) **sortir** proprement un bien (cession, rebut, sinistre), et (6) tenir un **fichier des immobilisations** qui colle à la balance au centime.

**Référentiel.** PCG (règlement ANC n° 2014-03 modifié, notamment par le règlement ANC n° 2022-06 applicable aux exercices ouverts depuis le 01/01/2025), CGI (art. 38 et s., 39, 39 A, 39 B, 39 duodecies et s., 42 septies…), BOFiP. Les associations appliquent le règlement ANC n° 2018-06, qui renvoie au PCG pour les immobilisations.

!!! abstract "En clair — ce module en 5 idées"
    1. Une **immobilisation**, c'est un bien que l'entreprise garde et utilise plus d'un an : un four, un camion, un ordinateur, un logiciel. Exemple : le nouveau four de C01 Boulangerie Dupain.
    2. On ne met pas tout son prix en charge l'année de l'achat. On l'**étale** sur sa durée d'utilisation : c'est l'**amortissement**. Chaque année, une part du prix devient une charge.
    3. Le prix à inscrire, c'est le prix d'achat hors TVA récupérable, **plus** les frais pour l'installer (livraison, montage). La formation ou la garantie, elles, restent des charges.
    4. À chaque clôture, vous vérifiez que le bien vaut encore au moins ce qui reste au bilan. Sinon, on constate une **dépréciation**. Exemple : le fonds de commerce de C04 Le Petit Zinc, le restaurant, si l'activité s'effondre.
    5. Quand un bien sort (vendu, jeté, détruit), il faut le **sortir des comptes** et du fichier des immobilisations. Le fichier doit toujours correspondre à la balance, au centime près.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Immobilisation | Bien ou droit que l'entreprise garde et utilise plus d'un an | Le camion de C11 Transports Leroy |
    | Charge | Dépense « consommée » tout de suite, qui réduit le résultat de l'année | Une réparation de peinture |
    | Coût d'entrée | Le montant total inscrit à l'actif au départ : prix + frais d'installation | Four 20 000 € + livraison 500 € |
    | Amortissement | Étalement du coût du bien sur les années où on l'utilise | 10 000 € sur 5 ans = 2 000 € par an |
    | Dotation | La part d'amortissement passée en charge pour une année | 2 000 € en 2026 |
    | VNC (valeur nette comptable) | Ce qui reste au bilan : coût d'entrée moins amortissements déjà passés | 10 000 – 4 000 = 6 000 € |
    | Mise en service | Le jour où le bien commence vraiment à servir ; l'amortissement démarre là | Machine installée le 12/11 |
    | Prorata temporis | On ne compte que la partie de l'année où le bien a servi | 1,5 mois sur 12 la 1re année |
    | Linéaire / dégressif | Linéaire : même montant chaque année. Dégressif : plus au début, moins à la fin | — |
    | Composant | Partie d'un bien qu'on remplace plus souvent que le reste, amortie à part | La toiture d'un immeuble |
    | Dérogatoire | Amortissement en plus, permis par le fisc, qui baisse l'impôt aujourd'hui et le remonte plus tard | Dégressif fiscal sur une machine |
    | Dépréciation | Constat que le bien vaut moins que sa VNC à la clôture | Fonds de commerce en perte |
    | Cession | Vente d'une immobilisation | Revente d'un véhicule de C03 Garage Martin |
    | Subvention d'investissement | Aide publique reçue pour acheter un bien, étalée au même rythme que lui | Aide régionale pour un équipement |
    | Fichier des immobilisations | Liste détaillée de tous les biens, qui doit coller à la balance | Logiciel d'immobilisations du cabinet |

---

## 1. Qu'est-ce qu'une immobilisation ?

> 🟢 **En clair :** devant chaque facture d'achat, vous devez trancher : charge de l'année ou bien durable à l'actif ? C'est la première décision, et une erreur ici fausse les comptes pendant des années. Exemple : un four neuf pour C01 Boulangerie Dupain est une immobilisation ; son nettoyage annuel est une charge.

### 1.1 Les trois conditions (PCG, définition d'un actif)

Un élément est inscrit à l'actif en immobilisation si :

1. c'est un **élément identifiable** (séparable ou issu d'un droit légal ou contractuel) ;
2. il a une **valeur économique positive** : il génère des **avantages économiques futurs** que l'entité **contrôle** (elle en a la maîtrise et en supporte les risques) ;
3. son **coût peut être évalué de façon fiable** ;

… et il est destiné à servir de façon **durable** (plus d'un exercice) à l'activité. Un bien destiné à être vendu est un **stock**, même s'il est cher (véhicule d'occasion du Garage Martin) ; un bien utilisé durablement est une immobilisation, même s'il est petit (outillage).

> 💡 **Réflexe senior :** « Qui contrôle ? » avant « Qui est propriétaire ? ». Des agencements faits par FitClub dans un local loué sont des immobilisations **de FitClub** (elle les contrôle pendant le bail) alors qu'ils deviendront la propriété du bailleur à la fin du bail. À l'inverse, un bien en **crédit-bail** n'est pas à l'actif en comptes individuels français (il l'est en IFRS 16) — il figure dans les engagements hors bilan (module M05).

### 1.2 Charge ou immobilisation : la grille de décision

| Question | Si oui | Si non |
|---|---|---|
| La dépense crée-t-elle un **nouvel actif** (bien, droit, logiciel) utilisé plus d'un an ? | Immobilisation | ↓ |
| Remplace-t-elle un **composant** identifié (toiture, moteur, agencements d'une chambre) ? | Immobilisation du nouveau composant + **sortie** de l'ancien | ↓ |
| **Augmente-t-elle la valeur** ou **prolonge-t-elle de façon significative la durée d'utilisation** d'un bien existant, au-delà de son état d'origine ? | Immobilisation (dépense ultérieure activée) | ↓ |
| Maintient-elle simplement le bien **en état** (entretien, réparation, peinture) ? | **Charge** (615) | — |

Les **dépenses de gros entretien ou de grandes révisions** faisant l'objet de programmes pluriannuels peuvent être traitées soit comme un **composant** (méthode préférentielle), soit par une **provision pour gros entretien** (PCG, provisions pour gros entretien ou grandes révisions) — jamais les deux pour la même dépense.

### 1.3 Le seuil de 500 € HT

- **Comptablement**, le PCG ne fixe pas de seuil : il autorise à ne pas immobiliser les éléments **non significatifs** (principe d'importance relative).
- **Fiscalement**, une **tolérance administrative** (BOFiP, frais et charges — dépenses de faible valeur) admet la déduction immédiate des **matériels et outillages, matériels et mobiliers de bureau et logiciels** dont la valeur unitaire **n'excède pas 500 € HT**.
- Le seuil s'apprécie **par bien** (unité), pas par facture : 6 chaises à 380 € HT = 6 biens de faible valeur.
- La tolérance est écartée pour les biens qui constituent **l'objet même de l'activité** (matériel destiné à la location) ; la doctrine l'écarte aussi, selon les cas, pour un **équipement d'ensemble** (équipement complet ou renouvellement complet d'un mobilier) — *à apprécier au cas par cas et à vérifier dans le BOFiP en vigueur*.
- C'est une **faculté** : on peut toujours immobiliser un bien de 450 € (cohérence : appliquez la même règle chaque année).

> ⚠️ **Erreur classique :** passer en 6063 une station de travail à 2 850 € HT « parce que c'est du petit matériel informatique », ou au contraire immobiliser un écran à 420 € HT et le perdre de vue dans le fichier. Le compte 6063 doit être **balayé** à chaque révision (cf. exercice E06-11).

---

## 2. Le coût d'entrée

> 🟢 **En clair :** une fois le bien reconnu, il faut savoir pour quel montant l'inscrire. On additionne le prix (hors TVA récupérable) et les frais nécessaires pour le faire fonctionner. Ce qui sert « autour » du bien (formation, garantie) reste en charge.

### 2.1 Coût d'acquisition (bien acheté)

**Coût d'acquisition = prix d'achat** (après remises, rabais, escomptes de règlement, **hors TVA récupérable**) **+ coûts directement attribuables** engagés pour mettre le bien en place et en état de fonctionner :

| Inclus dans le coût | Exclu (charge) |
|---|---|
| Transport, livraison, manutention | Frais de **formation** du personnel |
| Installation, montage, raccordement | **Extension de garantie**, contrat de maintenance |
| Frais de préparation du site, essais de bon fonctionnement (nets des produits des essais) | Frais **administratifs et généraux** non directement attribuables |
| Honoraires d'architecte, de maîtrise d'œuvre | Coûts de **démontage / évacuation de l'ancien bien** (ils concernent la sortie de l'ancien, pas l'entrée du nouveau) |
| **TVA non récupérable** (véhicule de tourisme, association non assujettie, médecin exonéré) | **Pertes d'exploitation** pendant les travaux, salaires pendant la fermeture |
| Coût estimé de **démantèlement** imposé par une obligation (provision en contrepartie) | **Frais d'emprunt** liés au financement (sauf option d'incorporation des coûts d'emprunt pour les actifs éligibles) |

### 2.2 Droits de mutation, honoraires, commissions et frais d'actes : l'option

Ces frais d'acquisition peuvent, **sur option** (PCG ; CGI, ann. III, art. 38 quinquies), être :
- **incorporés au coût** de l'immobilisation (et amortis avec elle — ou jamais, pour la quote-part afférente au terrain) ;
- ou comptabilisés **en charges**.

L'option est **globale** : elle s'applique à toutes les immobilisations corporelles et incorporelles (une option distincte existe pour les titres). Elle doit être appliquée de façon **permanente** et mentionnée en annexe.

**Cas particulier des titres de participation** : fiscalement, les frais d'acquisition des titres doivent être incorporés au prix de revient puis **amortis sur 5 ans** par voie d'**amortissement dérogatoire** (CGI, art. 209-VII) — même si l'entreprise les a passés en charges en comptabilité (alors réintégration extra-comptable puis déduction sur 5 ans).

> 🟢 **En clair :** quand une société achète des parts d'une autre société, le fisc veut que les frais d'achat soient étalés sur 5 ans. Si la comptabilité les a mis en charge d'un coup, on corrige sur la déclaration fiscale.

> 💡 **Réflexe senior :** l'option « charges » réduit le résultat de l'année d'acquisition (souvent créant une perte), l'option « coût » le lisse. Le bon choix dépend du client : IS à 15 % ou 25 %, déficits reportables existants, besoin d'afficher des capitaux propres (banque, levée de fonds), distribution prévue. On **chiffre les deux** avant de choisir (cf. E06-01).

### 2.3 Autres modes d'entrée

| Mode d'entrée | Valeur d'entrée | Compte de contrepartie |
|---|---|---|
| Production par l'entreprise | **Coût de production** (matières + main-d'œuvre directe + charges indirectes de production attribuables) | 72 Production immobilisée (721 incorporelle, 722 corporelle) |
| **Apport en nature** | **Valeur d'apport** fixée aux statuts (ou dans le traité d'apport) | 4561 / 456x (associés, comptes d'apport) |
| Acquisition à titre gratuit | Valeur vénale | Selon le cas (subvention, produit) |
| Échange | Valeur vénale du bien reçu (en règle générale) | 775 pour le bien remis |

### 2.4 Acomptes et immobilisations en cours

| Situation | Compte |
|---|---|
| Acompte versé sur commande d'une immobilisation **corporelle** | **238** Avances et acomptes versés sur commandes d'immobilisations corporelles |
| Acompte versé sur immobilisation **incorporelle** | 237 |
| Bien en cours de construction / de développement, pas encore en service | **231** (corporelle) / **232** (incorporelle) — **non amortis** |
| Mise en service | 21x / 20x par le crédit de 23x ; l'amortissement commence |

> ⚠️ **Erreur classique :** amortir un 231 ou un 232 « parce que les dépenses ont été engagées ». Pas de mise en service = pas d'amortissement (mais une **dépréciation** est possible si le projet est compromis). Et un 238 qui traîne depuis 2 ans au bilan alors que le bien est livré et facturé : l'acompte n'a jamais été imputé sur la facture définitive → actif gonflé, 404 surévalué.

**TVA sur acomptes** : pour une **livraison de biens** (machine, four, véhicule), la TVA est exigible à la **livraison**, pas à l'encaissement de l'acompte ; pour une **prestation de services** ou des **travaux immobiliers**, elle est exigible à l'encaissement (sauf option pour les débits) — l'acompte versé ouvre donc droit à déduction dès qu'il est payé (sur facture).

---

## 3. Immobilisations incorporelles

> 🟢 **En clair :** ce sont des biens qu'on ne peut pas toucher : un fonds de commerce, un logiciel, un droit au bail, une licence. Certains s'amortissent, d'autres non. Exemple : le logiciel développé par C08 TechNova peut, sous conditions, devenir un actif.

| Élément | Compte | Amortissable ? | Points clés |
|---|---|---|---|
| **Fonds commercial** (clientèle, achalandage non identifiés séparément) | 207 | **Présumé à durée non limitée → non amorti** ; les **petites entreprises** (au sens des seuils du Code de commerce) peuvent l'amortir sur **10 ans** (option du PCG) | **Test de dépréciation** obligatoire pour les fonds non amortis (au moins à chaque clôture selon le PCG ; à défaut, dès qu'il existe un indice) ; dépréciation **irréversible** (jamais reprise). Fiscalement : amortissement en principe **non déductible** (une mesure temporaire a visé les fonds acquis entre 2022 et 2025 — *à vérifier*) |
| **Droit au bail** | 206 | En général non (droit au renouvellement du bail commercial) | Amorti seulement si durée limitée (bail non renouvelable) |
| **Licence IV** (débit de boissons) | 208 / 207 selon pratique | Non (durée illimitée sous réserve d'exploitation) | Test de dépréciation ; péremption si non exploitée (délai légal à vérifier) |
| **Logiciels acquis** | 205 | Oui, durée d'utilisation (souvent 1 à 3 ans) | Fiscal : **amortissement exceptionnel sur 12 mois** possible pour les logiciels acquis (CGI, art. 236-II) → dérogatoire |
| **Logiciels créés** | 205 / 232 | Oui | Activation à partir de la phase de conception détaillée/programmation si les conditions sont remplies |
| **Abonnement SaaS** | — (charge 6xx) | — | On ne contrôle pas le logiciel : c'est un **service**. Abonnement annuel payé d'avance → **CCA** |
| **Frais de développement** | 203 (232 en cours) | Oui, durée d'utilisation (en principe ≤ 5 ans) | **Activation = méthode de référence** si les 6 critères sont remplis ; **recherche = toujours en charges** |
| **Droit d'entrée de franchise** | 205 (ou 208) | Oui, sur la durée du contrat | Distinguer : formation initiale, kit d'ouverture = charges ; redevances = charges (651) |
| Frais d'établissement | 201 | Oui, ≤ 5 ans | Option : charges (méthode préférentielle) ou actif |

### 3.1 Frais de développement : les 6 critères (PCG)

Les frais de **développement** peuvent être activés si l'entreprise démontre **cumulativement** :
1. la **faisabilité technique** nécessaire à l'achèvement du projet ;
2. son **intention** d'achever le projet et de l'utiliser ou de le vendre ;
3. sa **capacité** à l'utiliser ou à le vendre ;
4. la façon dont il générera des **avantages économiques futurs probables** (marché, clients) ;
5. la **disponibilité des ressources** (techniques, financières) pour l'achever ;
6. sa capacité à **évaluer de façon fiable** les dépenses attribuables (feuilles de temps, suivi par projet).

Seules les dépenses engagées **à partir du moment où tous les critères sont remplis** sont activables ; les dépenses antérieures passées en charges **ne sont jamais réactivées**. Les frais de **recherche** (lever une incertitude scientifique, état de l'art, preuve de concept exploratoire) sont **toujours** des charges.

Conséquences juridiques : tant que les frais de développement inscrits à l'actif ne sont pas totalement amortis, **aucune distribution de dividendes** n'est possible, sauf si les réserves libres sont au moins égales aux frais non amortis (Code de commerce, partie réglementaire, dispositions sur les frais d'établissement et de développement).

Fiscalement, les dépenses de recherche au sens fiscal peuvent, sur option, être **déduites immédiatement** même si elles sont immobilisées (CGI, art. 236-I) → mécanisme d'amortissement dérogatoire.

---

## 4. Immobilisations corporelles et approche par composants

> 🟢 **En clair :** les biens physiques (bâtiment, machine, véhicule, mobilier) ont chacun leur compte. Quand un bien a des parties qui s'usent à des vitesses différentes, on les découpe et on amortit chaque partie à son rythme. Exemple : les chambres de C16 Hôtel Belle Vue sont refaites plus souvent que les murs.

### 4.1 Les comptes

| Compte | Contenu |
|---|---|
| 211 | Terrains (**jamais amortis**, sauf gisements/carrières) |
| 212 | Agencements et aménagements de terrains |
| 213 (2131, 2135) | Constructions ; 2135 : installations générales, agencements, aménagements **des constructions** (bâtiment dont l'entreprise est propriétaire) |
| 214 | Constructions sur sol d'autrui |
| 215 (2154, 2155) | Installations techniques, matériel et outillage industriels |
| 2181 | Installations générales, agencements, aménagements **divers** (notamment dans des **locaux loués**) |
| 2182 | Matériel de transport |
| 2183 | Matériel de bureau et informatique |
| 2184 | Mobilier |

### 4.2 L'approche par composants (PCG)

Lorsque des éléments d'un actif ont des **durées d'utilisation différentes** (ou procurent des avantages selon un rythme différent), chacun est comptabilisé et amorti **séparément** dès l'origine. On distingue :
- la **structure** (élément principal), amortie sur sa propre durée ;
- les **composants**, destinés à être remplacés à intervalles réguliers (toiture, façade, installations techniques, agencements ; moteur d'un avion ; réfection des chambres d'un hôtel…).

Durées indicatives couramment retenues pour un **immeuble de bureaux** (à adapter à l'état réel, à justifier par un rapport d'expert ou un diagnostic technique) :

| Composant | Quote-part indicative | Durée neuve |
|---|---|---|
| Terrain | 10 à 30 % du total selon la localisation | Non amorti |
| Structure / gros œuvre | 40 à 60 % des constructions | 40 à 80 ans |
| Façades, menuiseries extérieures | 10 à 20 % | 20 à 40 ans |
| Toiture, étanchéité | 5 à 15 % | 15 à 30 ans |
| Installations générales techniques (CVC, électricité, ascenseurs) | 10 à 20 % | 15 à 25 ans |
| Agencements intérieurs | 5 à 15 % | 8 à 15 ans |

Pour un **immeuble d'occasion**, on retient les **durées résiduelles** estimées à la date d'acquisition, pas les durées « neuves ».

**Remplacement d'un composant** :
1. on amortit l'ancien composant **jusqu'à la date de sortie** ;
2. on le **sort** : VNC en 675 (contrepartie : annulation du brut 21x et des amortissements 28x) ;
3. on immobilise le **nouveau** composant à son coût ;
4. si l'ancien composant n'avait pas été identifié à l'origine, on estime sa valeur (coût du nouveau actualisé à rebours, ou quote-part) pour le sortir.

> ⚠️ **Erreur classique :** immobiliser la rénovation des chambres **sans sortir** les anciens agencements → le même mur figure deux fois à l'actif, les dotations sont surévaluées pendant des années et la VNC de l'ancien ne sera jamais passée en charge.

> 💡 **Réflexe senior :** pour les **PME**, le PCG admet des mesures de simplification (notamment retenir la **durée d'usage** pour les biens non décomposés et ne pas décomposer certains composants). Pour un immeuble, la décomposition reste incontournable : elle est attendue par l'administration fiscale et par tout auditeur.

---

## 5. L'amortissement

> 🟢 **En clair :** l'amortissement répartit le coût du bien sur ses années d'utilisation. Vous devez choisir une durée, un mode (linéaire ou dégressif) et une date de départ. Si le fisc permet d'aller plus vite que la comptabilité, l'écart s'appelle « dérogatoire ».

### 5.1 Vocabulaire

| Notion | Définition |
|---|---|
| **Base amortissable** | Coût d'entrée – **valeur résiduelle** (prise en compte seulement si elle est **significative et mesurable** ; rare en pratique, sauf flottes de véhicules revendus à date fixe) |
| **Durée d'utilisation** (comptable) | Durée pendant laquelle **l'entreprise** prévoit d'utiliser le bien (elle peut le revendre avant la fin de sa vie physique) |
| **Durée d'usage** (fiscale) | Durée admise par les **usages de la profession** (BOFiP, tables indicatives) ; sert de référence fiscale (amortissement minimal, dégressif) |
| **Mode** | Linéaire, dégressif (fiscal), unités d'œuvre (km, heures, copies) — doit refléter le **rythme de consommation** des avantages |
| **Point de départ** | Linéaire : **date de mise en service** ; dégressif fiscal : **1er jour du mois d'acquisition** |

**Prorata temporis.** En linéaire, la première annuité est calculée au jour près à partir de la mise en service. **Convention de cette formation (usage courant des logiciels) : année de 360 jours, mois de 30 jours.** Exemple : mise en service le 12/11 → 19 jours en novembre (30 – 12 + 1) + 10 mois → 319/360.

### 5.2 L'amortissement dégressif (CGI, art. 39 A)

- **Biens éligibles** : biens **neufs**, durée d'usage **≥ 3 ans**, figurant dans la liste réglementaire (matériels et outillages industriels, matériels de manutention, installations de production, matériels informatiques, certains bâtiments industriels légers…). Exclus notamment : biens d'occasion, biens dont la durée < 3 ans, la plupart des immeubles et le mobilier de bureau non industriel.
- **Taux dégressif = taux linéaire × coefficient** :

| Durée d'usage | Coefficient |
|---|---|
| 3 ou 4 ans | **1,25** |
| 5 ou 6 ans | **1,75** |
| Plus de 6 ans | **2,25** |

*(Coefficients de droit commun ; des coefficients majorés temporaires ont existé par le passé — vérifiez qu'aucune mesure temporaire n'est en vigueur pour l'exercice.)*

- **Prorata** : en **mois**, à compter du **premier jour du mois d'acquisition** (même si la mise en service est postérieure).
- **Passage au linéaire** : dès que l'annuité dégressive (VNC × taux) devient **inférieure** à l'annuité linéaire calculée sur la **durée restant à courir** (VNC ÷ durée restante), on retient cette dernière jusqu'au terme.

### 5.3 Amortissement fiscal et amortissement comptable : les dérogatoires

Le plan comptable doit refléter la consommation réelle (souvent linéaire). Si la fiscalité autorise **plus** (dégressif, durée d'usage plus courte, amortissement exceptionnel), l'écart est constaté en **amortissements dérogatoires**, une **provision réglementée** inscrite dans les **capitaux propres** :

> 🟢 **En clair :** la comptabilité amortit au rythme réel d'usure. Le fisc permet parfois d'aller plus vite pour payer moins d'impôt tout de suite. La différence est notée à part, dans un compte de capitaux propres (145), pour ne pas fausser l'amortissement « réel ».

| Situation | Écriture |
|---|---|
| Annuité fiscale > annuité comptable | **D 6872** Dotations aux provisions réglementées (immobilisations) / **C 145** Amortissements dérogatoires |
| Annuité fiscale < annuité comptable (fin de plan) | **D 145** / **C 7872** Reprises sur provisions réglementées (immobilisations) |
| Cession du bien | **Reprise du solde** de 145 en 7872 |

Les dérogatoires ne se déduisent fiscalement **que s'ils sont comptabilisés** (connexion fiscalo-comptable). Ils sont symétriques sur la durée : ils **décalent** l'impôt, ils ne l'effacent pas.

**Amortissement minimal (CGI, art. 39 B)** : à la clôture de chaque exercice, le cumul des amortissements pratiqués doit être au moins égal au cumul des amortissements **linéaires** calculés sur la durée d'usage. À défaut, la fraction non pratiquée est **définitivement perdue** fiscalement (« amortissements irrégulièrement différés »).

> 🟢 **En clair :** chaque année, il faut avoir amorti au moins autant qu'en linéaire. Un amortissement « oublié » une année ne pourra jamais être déduit plus tard.

> ⚠️ **Erreur classique :** « ne pas passer la dotation cette année pour améliorer le résultat ». C'est interdit en comptabilité (principe de prudence : l'amortissement est constaté même en cas d'absence ou d'insuffisance de bénéfice) et fiscalement pénalisant (art. 39 B).

### 5.4 Le plan d'amortissement (modèle)

| Exercice | Base | Taux / prorata | Dotation | Cumul | VNC fin |
|---|---|---|---|---|---|
| 2026 (mise en service 01/04) | 100 000 | 10 % × 270/360 | 7 500 | 7 500 | 92 500 |
| 2027 | 100 000 | 10 % | 10 000 | 17 500 | 82 500 |
| … | | | | | |
| 2036 (fin au 31/03) | 100 000 | 10 % × 90/360 | 2 500 | 100 000 | 0 |

Le plan est **révisé de façon prospective** si la durée ou le mode d'utilisation change significativement, ou après une dépréciation (nouvelle base = VNC dépréciée, sur la durée résiduelle).

---

## 6. Dépréciation des immobilisations

> 🟢 **En clair :** à la clôture, vous vous demandez si le bien vaut encore ce qui reste au bilan. S'il vaut moins (bien abîmé, activité en baisse), on enregistre la perte de valeur. Pour le fonds commercial, cette perte n'est jamais reprise.

### 6.1 Le test

À chaque clôture, on recherche s'il existe un **indice de perte de valeur** (externe : baisse de la valeur de marché, concurrence nouvelle, changement réglementaire, hausse des taux ; interne : obsolescence, dégradation physique, baisse de performance, projet d'arrêt). Les **fonds commerciaux et autres incorporels non amortis** font l'objet d'un test **systématique**.

**Valeur actuelle = la plus élevée** de :
- la **valeur vénale** (prix de cession, net des coûts de sortie, dans une transaction normale) ;
- la **valeur d'usage** (valeur des avantages économiques futurs attendus de l'utilisation et de la sortie — en pratique, flux de trésorerie futurs actualisés).

Si **valeur actuelle < VNC** → dépréciation = VNC – valeur actuelle.

Lorsque l'actif ne génère pas de flux indépendants (un fonds de commerce, ses agencements et son matériel), le test se fait au niveau du **groupe d'actifs** : on compare la VNC du groupe à sa valeur actuelle ; la perte s'impute en priorité sur le fonds commercial, les autres actifs n'étant pas ramenés sous leur propre valeur actuelle.

### 6.2 Écritures

| Opération | Débit | Crédit |
|---|---|---|
| Dotation | 6816 Dotations aux dépréciations des immobilisations incorporelles et corporelles | 29x (2907 fonds commercial, 2931…) |
| Reprise (sauf fonds commercial) | 29x | 7816 Reprises sur dépréciations des immobilisations incorporelles et corporelles |

Après dépréciation d'un bien amortissable, le **plan est révisé** (base = VNC dépréciée). **Fiscalement**, la dépréciation d'un bien amortissable n'est pas déductible en tant que telle mais se traduit par des amortissements futurs plus faibles (mécanisme de réintégration/déduction étalée) ; la dépréciation d'un bien non amortissable (fonds) suit les conditions de droit commun des provisions (perte probable, évaluée avec précision) — *point technique à documenter avec soin*.

> 🟢 **En clair :** après une dépréciation, on recalcule les amortissements futurs sur la nouvelle valeur, plus basse. Côté impôt, le traitement est différent selon que le bien s'amortit ou non : notez toujours votre raisonnement dans le dossier.

---

## 7. Les sorties d'actif

> 🟢 **En clair :** un bien vendu, jeté ou détruit doit disparaître du bilan et du fichier. On passe d'abord l'amortissement jusqu'au jour de la sortie, puis on enregistre d'un côté ce qui restait au bilan, de l'autre le prix reçu. Exemple : C03 Garage Martin revend sa dépanneuse.

### 7.1 Schéma général (cession, mise au rebut, sinistre)

| Étape | Débit | Crédit |
|---|---|---|
| 1. **Dotation complémentaire** jusqu'à la date de sortie | 6811 | 28x |
| 2. **Sortie** du bien : on solde amortissements et brut | 28x (cumul) + **675** Valeurs comptables des éléments d'actif cédés (VNC) | 21x / 20x (brut) |
| 3. **Prix de cession** / indemnité | 462 Créances sur cessions d'immobilisations (ou 512) | **775** Produits des cessions d'éléments d'actif + 44571 (TVA si taxable) |
| 4. Dépréciations éventuelles | 29x | 7816 |
| 5. Amortissements dérogatoires restants | 145 | 7872 |

Le règlement ANC n° 2022-06 a restreint le résultat exceptionnel, mais les **cessions d'immobilisations restent en 675 / 775**. Pour une **mise au rebut** (VNC sans prix) ou une **sortie sans contrepartie**, nous retenons également 675 (valeur comptable des actifs sortis) ; *vérifiez la subdivision retenue par la nomenclature 2025 et la position du cabinet*.

> ⚠️ **Erreur classique :** créditer 775 du prix de vente… et oublier de sortir le bien. Le fichier des immobilisations continue de l'amortir, la balance et le fichier divergent, le 2054 est faux. Autre classique : créditer le compte 2182 du prix de vente (« le camion est parti »).

### 7.2 TVA sur cession

- La cession d'un **bien meuble** dont la TVA a été déduite est **taxable** au taux normal sur le prix total (pas de régime de la marge pour l'entreprise qui cède son propre matériel).
- Bien acquis **sans droit à déduction** (véhicule de tourisme) : cession en principe exonérée.
- **Immeubles** : régime propre (neufs / plus de 5 ans, option, régularisations sur 20 ans).
- Les **indemnités d'assurance** sont **hors champ** de la TVA.

### 7.3 Régime fiscal des plus-values professionnelles

**Entreprises à l'IS** : la plus ou moins-value (prix – VNC fiscale) est comprise dans le **résultat imposable au taux de droit commun**, quelle que soit la durée de détention. Le régime du long terme ne subsiste que pour certains **titres** (titres de participation : exonération sous réserve d'une quote-part de frais et charges — *taux à vérifier*).

**Entreprises à l'IR** (BIC, BNC, BA) : régime court terme / long terme (CGI, art. 39 duodecies et s.) :

| | Bien détenu **< 2 ans** | Bien détenu **≥ 2 ans** |
|---|---|---|
| **Plus-value**, bien amortissable | **Court terme** en totalité | **Court terme** à hauteur des **amortissements déduits** ; **long terme** pour l'excédent (prix > coût d'origine) |
| **Plus-value**, bien non amortissable (terrain, fonds) | Court terme | **Long terme** |
| **Moins-value**, bien amortissable | Court terme | **Court terme** |
| **Moins-value**, bien non amortissable | Court terme | Long terme |

- **Court terme net** : imposé au barème avec le résultat (étalement sur 3 ans possible pour la plus-value nette à court terme).
- **Long terme net** : imposé à un **taux proportionnel** (on retient 12,8 % + prélèvements sociaux — *taux à vérifier*).
- Exonérations possibles selon les recettes (CGI, art. 151 septies), départ à la retraite, transmission… (module M10).

**Point technique** : la plus-value **fiscale** se calcule sur la **VNC fiscale** = coût – (amortissements comptables + amortissements dérogatoires). La reprise des dérogatoires à la cession (7872) fait donc partie du résultat de cession fiscal.

> 🟢 **En clair :** pour l'impôt, la plus-value se calcule sur la valeur restante après **tous** les amortissements, y compris les dérogatoires. C'est pourquoi on solde le compte 145 au moment de la vente.

### 7.4 Sinistres

- Le bien détruit **sort de l'actif** à la date du sinistre (dotation jusqu'à cette date, VNC en 675).
- L'**indemnité d'assurance** est traitée comme un **produit de cession** (775) — position retenue dans ce module pour un bien détruit ; *certains cabinets la présentent en autres produits : harmonisez avec la position du cabinet*.
- **Rattachement** : l'indemnité est constatée en **produit à recevoir** (4687 ou 468x) à la clôture si, à cette date, le **principe** de l'indemnisation est acquis (garantie non contestée) et le montant **estimable de façon fiable** (rapport d'expert). Un courrier de l'assureur reçu **après la clôture** mais avant l'arrêté des comptes, qui **confirme** une situation existant à la clôture, est un événement post-clôture à prendre en compte. Si l'assureur **conteste** sa garantie : rien en produit (actif éventuel), information en annexe si significatif.
- Les remboursements de **frais** (remorquage, expertise) ne passent **plus en 791** (comptes de transfert de charges supprimés) : ils viennent **en diminution de la charge** concernée.

---

## 8. Subventions d'investissement

> 🟢 **En clair :** quand l'entreprise reçoit une aide publique pour acheter un bien, on ne la met pas en produit d'un coup. On la garde dans les capitaux propres et on la fait passer en résultat petit à petit, au même rythme que l'amortissement du bien.

| Opération | Débit | Crédit |
|---|---|---|
| Notification (droit acquis, conditions remplies) | 441 État et autres collectivités – subventions à recevoir | **131** Subventions d'équipement |
| Encaissement | 512 | 441 |
| Chaque clôture : quote-part virée au résultat | **139** Subventions d'investissement inscrites au compte de résultat | **747** Quote-part des subventions d'investissement virée au résultat de l'exercice (*nomenclature PCG 2025 ; anciennement 777*) |
| Fin (bien totalement amorti ou sorti) | 139 | 131 (on solde les deux comptes) |

- **Rythme de reprise** : bien **amortissable** → au rythme des amortissements (même proportion) ; bien **non amortissable** → sur la durée d'inaliénabilité prévue par la convention, à défaut par 1/10e.
- La subvention reste en capitaux propres (bilan) pour son montant non repris.
- **Fiscalement** : par défaut imposable l'année d'octroi ; **étalement** possible au rythme des amortissements (CGI, art. 42 septies) — l'option comptable de reprise rend en pratique le traitement fiscal identique.
- Clause de **reversement** en cas de cession anticipée : engagement à suivre (annexe) ; en cas de cession, le solde non repris est viré au résultat (ou une dette constatée si le reversement est exigé).
- **Associations** (règlement ANC n° 2018-06) : même mécanisme pour les biens non renouvelables par l'association ; une subvention finançant un bien **renouvelable par l'entité** peut être inscrite en **fonds propres sans droit de reprise** (non reprise) — *analyse à faire au cas par cas avec la convention et le CAC*.

---

## 9. Véhicules de tourisme

> 🟢 **En clair :** les voitures particulières ont des règles à part : TVA non récupérable, amortissement fiscal plafonné, taxes annuelles. Le client pense souvent faire une bonne affaire fiscale en achetant une voiture : vous devez savoir chiffrer la réalité.

| Conséquence | Règle | Valeurs (à vérifier chaque année) |
|---|---|---|
| **TVA** | Non déductible sur le véhicule (VP, carte grise « VP », pick-up 5 places…) | Coût d'entrée **TTC** |
| **Plafond d'amortissement fiscal** (CGI, art. 39-4) | La fraction de la dotation correspondant au prix TTC **excédant le plafond** est **réintégrée** (extra-comptable, 2058-A) | On retient : 30 000 € (< 20 g CO₂/km), 20 300 € (20 à 50 g), 18 300 € (50 à 160 g), **9 900 €** au-delà de 160 g/km (véhicules homologués **WLTP**, soit tous ceux immatriculés depuis 2021 ; l'ancien seuil NEDC était 130 g) — *valeurs à vérifier chaque année* |
| **Taxes annuelles** (ex-TVS) | Taxe annuelle sur les émissions de CO₂ + taxe annuelle sur les polluants atmosphériques, au **prorata des jours d'affectation** ; **non déductibles** | Barèmes CIBS de l'année (module M10) |
| **Avantage en nature** | Si usage privé du dirigeant/salarié | Module M07 |

Calcul : `réintégration = dotation comptable × (coût TTC – plafond) / coût TTC`.

> 💡 **Réflexe senior :** « acheter une voiture en décembre pour payer moins d'impôt » est un mythe : la dotation de décembre porte sur quelques jours, l'essentiel est réintégré, la TVA est perdue et les taxes annuelles démarrent. On chiffre et on l'écrit au client (cf. E06-06).

---

## 10. Immobilisations financières

> 🟢 **En clair :** ce sont des placements ou des sommes bloquées à long terme : titres d'une filiale, prêts, dépôts de garantie. Exemple : le dépôt de garantie versé par C21 FitClub Villeurbanne à son bailleur n'est pas un loyer, c'est une somme qu'elle récupérera.

| Compte | Contenu | Points clés |
|---|---|---|
| 261 | **Titres de participation** (détention durable utile à l'activité, en principe ≥ 10 %) | Coût d'acquisition (+ frais : option ; fiscal art. 209-VII) ; dépréciation si **valeur d'utilité** < coût (actif net réévalué, rentabilité, perspectives) |
| 271/272 | Titres immobilisés | Placements durables sans influence |
| 274 | Prêts | |
| **275** | **Dépôts et cautionnements versés** (dépôt de garantie d'un bail, caution EDF) | **Non amortis, non actualisés** ; remboursables en fin de contrat ; retenue éventuelle du bailleur → charge |
| 165 | *(passif)* Dépôts et cautionnements **reçus** | Chez le bailleur (SCI Horizon Pro) — jamais en produit |

> ⚠️ **Erreur classique :** passer le dépôt de garantie du bail en charge de loyer (6132) ou, chez le bailleur, en produit (706). C'est une **créance** (275) / une **dette** (165).

---

## 11. Le fichier des immobilisations et son contrôle avec la balance

> 🟢 **En clair :** le fichier des immobilisations est la liste détaillée de tous les biens. À chaque clôture, ses totaux doivent être égaux aux soldes de la balance. S'il y a un écart, vous cherchez la cause ligne par ligne, sans écriture « pour équilibrer ».

Le fichier (ou « registre ») des immobilisations est la **comptabilité auxiliaire** des classes 20-21-23-28-29 et 145. Il doit, pour chaque bien : désignation précise (n° de série, immatriculation), compte, date d'acquisition et de mise en service, coût, mode et durée (comptable / fiscale), dotations, cumul, VNC, sortie.

**Contrôle de clôture (systématique) :**

| Contrôle | Égalité attendue |
|---|---|
| Brut | Σ valeurs brutes du fichier par compte = soldes 20x / 21x / 23x |
| Amortissements | Σ cumuls du fichier = soldes 28x |
| Dotations | Σ dotations du fichier = 6811 (+ 6871) ; dérogatoires = 6872 / 7872 ; 145 |
| Dépréciations | 29x / 6816 / 7816 |
| Cessions | Σ VNC des biens sortis = 675 ; prix = 775 |
| Tableau de variation | Brut ouverture + acquisitions – sorties = brut clôture (alimente le 2054 / 2055) |

**Causes d'écart typiques** : acquisition saisie en comptabilité mais pas créée dans le fichier (ou l'inverse) ; sortie passée d'un côté seulement ; dotation saisie « à la main » (situation intermédiaire, estimation) et non contre-passée ; bien imputé sur le mauvais compte ; réimputation des 6063/615 à la révision non reportée dans le fichier.

> 💡 **Réflexe senior :** l'écart se **justifie ligne par ligne** dans une feuille de travail (rapprochement fichier / balance), jamais par une écriture d'« ajustement » sans pièce. Une fois par an, faites **l'inventaire physique** des biens significatifs avec le client (les biens disparus ou hors d'usage sont à sortir).

---

## 12. Schémas d'écritures types (récapitulatif)

> 🟢 **En clair :** ce tableau résume les écritures du module. Gardez-le sous la main pendant vos saisies et vos révisions.

| Opération | Débit | Crédit |
|---|---|---|
| Acompte versé sur machine | 238 | 512 |
| Facture de la machine (acompte imputé) | 2154 + 44562 | 404 (puis 404 / 238 pour imputer l'acompte) |
| Frais d'acquisition — option coût | 21x | 404 / 467 |
| Production immobilisée (logiciel, travaux faits soi-même) | 232 / 231 | 721 / 722 |
| Mise en service d'un en-cours | 20x / 21x | 232 / 231 |
| Dotation | 6811 | 28x |
| Dérogatoire | 6872 | 145 |
| Dépréciation | 6816 | 29x |
| Cession | 462 ; 28x + 675 | 775 + 44571 ; 21x |
| Subvention d'investissement | 441 → 131 ; 139 → 747 | |
| Apport en nature | 21x | 4561 |
| Dépôt de garantie versé | 275 | 512 |

---

## Checklist de fin de module

- [ ] Je sais appliquer les 3 conditions de l'actif et la grille charge / immobilisation, y compris le seuil de 500 € HT et ses limites.
- [ ] Je détermine un coût d'entrée complet et j'exclus formation, garantie, démontage de l'ancien bien, frais d'emprunt.
- [ ] Je connais l'option frais d'acquisition (charge / coût) et je chiffre son impact avant de conseiller.
- [ ] Je ventile un immeuble en terrain + structure + composants avec des durées justifiées (résiduelles si occasion).
- [ ] Je calcule un prorata temporis (linéaire : mise en service, au jour ; dégressif : 1er jour du mois d'acquisition).
- [ ] Je construis un plan dégressif avec passage au linéaire et je calcule les dérogatoires (6872 / 145 / 7872).
- [ ] Je traite un remplacement de composant avec sortie de la VNC de l'ancien.
- [ ] Je comptabilise une cession (dotation complémentaire, sortie, 675/775, TVA, reprise des dérogatoires) et je détermine CT/LT pour un client à l'IR.
- [ ] Je traite un sinistre et je sais quand constater l'indemnité en produit à recevoir.
- [ ] Je comptabilise une subvention d'investissement et sa reprise (131 / 139 / **747**).
- [ ] Je calcule la réintégration de l'amortissement d'un véhicule de tourisme et les taxes annuelles.
- [ ] Je réalise un test de dépréciation (valeur vénale vs valeur d'usage) et je sais qu'une dépréciation du fonds commercial est irréversible.
- [ ] Je rapproche le fichier des immobilisations de la balance et j'explique chaque écart.

---

## À retenir en 30 secondes

- Un bien utilisé plus d'un an va à l'actif ; l'entretien courant reste une charge.
- Le coût d'entrée = prix hors TVA récupérable + frais pour le faire fonctionner (pas la formation ni la garantie).
- L'amortissement démarre à la mise en service, jamais avant ; les terrains ne s'amortissent pas.
- Si le fisc permet d'amortir plus vite, l'écart va en dérogatoire (6872 / 145 / 7872).
- À chaque clôture, vérifiez que le bien vaut encore sa VNC ; sinon, dépréciation.
- Un bien vendu ou jeté doit sortir des comptes **et** du fichier (675 / 775).
- Le fichier des immobilisations doit toujours être égal à la balance.
