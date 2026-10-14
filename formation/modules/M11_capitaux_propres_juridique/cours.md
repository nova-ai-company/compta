# M11 — Capitaux propres, associés et vie juridique

> **Objectif du module.** Comptabiliser sans hésiter tout ce qui touche aux **capitaux propres** (capital, primes, réserves, report à nouveau, résultat, subventions, provisions réglementées) et aux **associés** (apports, libération, comptes courants, dividendes), et piloter le **juridique annuel** d'un dossier : approbation des comptes, affectation du résultat, dépôt au greffe, conventions réglementées, procédure des capitaux propres inférieurs à la moitié du capital.
>
> C'est un module où le junior est souvent « exécutant » (« le client a voté ça, je le passe »). Le senior, lui, **vérifie que la décision est légale avant de la comptabiliser** : une distribution supérieure au bénéfice distribuable, une réserve légale oubliée ou un acompte sur dividendes sans bilan certifié engagent la responsabilité du dirigeant… et celle du cabinet qui a rédigé le procès-verbal.

!!! abstract "En clair — ce module en 5 idées"
    1. **Les capitaux propres, c'est ce qui appartient aux associés dans l'entreprise.** L'argent qu'ils ont apporté (le capital) et les bénéfices laissés dans la société (les réserves). Exemple : C01 Boulangerie Dupain, la boulangerie, accumule des réserves année après année. Attention : l'argent qu'un associé prête à sa société (compte courant) est une dette, pas des capitaux propres.
    2. **Le capital n'est pas toujours versé d'un coup.** Les associés s'engagent sur un montant, puis le versent en une ou plusieurs fois. Exemple : C25 Studio Pixel a un capital de 10 000 €, dont une partie n'a pas encore été demandée aux associés.
    3. **Le bénéfice ne se distribue pas librement.** Il faut d'abord combler les pertes passées et alimenter la réserve légale. Exemple : C09 Mode & Co, l'e-commerce, a un report à nouveau débiteur (des pertes passées) : ces pertes passent avant tout dividende.
    4. **Verser un dividende, c'est aussi retenir et déclarer des impôts.** La société retient l'impôt et les prélèvements sociaux, puis les reverse à l'État. Cas piège : le gérant majoritaire de SARL et l'associé d'une SELARL comme C12 Pharmacie Centrale, la pharmacie.
    5. **Chaque année, il y a un calendrier juridique.** Approuver les comptes dans les 6 mois, les déposer au greffe, traiter les conventions entre la société et ses dirigeants. Exemple : C03 Garage Martin, dont le gérant loue le local à sa propre société.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Capitaux propres | Tout ce qui appartient aux associés dans la société : capital, réserves, résultat, etc. | Le haut du passif du bilan |
    | Capital social | La somme que les associés se sont engagés à apporter, inscrite dans les statuts. | 10 000 € pour C25 Studio Pixel |
    | Souscription | La promesse d'un associé d'apporter une somme ou un bien à la société. | Un associé signe pour 5 000 € |
    | Appel de fonds | La demande faite par le dirigeant aux associés de verser tout ou partie de ce qu'ils ont promis. | Le président demande le solde du capital |
    | Libération | Le versement réel, par l'associé, de ce qu'il a promis. | Le virement arrive sur le compte de la société |
    | Apport en nature | Un apport d'un bien (machine, fonds de commerce) au lieu d'argent. | Un associé apporte son matériel informatique |
    | Prime d'émission | Le supplément payé par un nouvel associé au-dessus de la valeur de base de la part ou de l'action. | Les investisseurs de C08 TechNova |
    | Réserve légale | Une partie du bénéfice que la loi oblige à garder dans la société, jusqu'à un plafond. | 5 % du bénéfice chaque année, jusqu'à 10 % du capital |
    | Report à nouveau | Le bénéfice laissé « en attente » ou les pertes pas encore effacées. | Le report débiteur de C09 Mode & Co |
    | Affectation du résultat | La décision des associés sur ce que devient le bénéfice ou la perte de l'année. | Réserve, dividendes, report à nouveau |
    | Bénéfice distribuable | Le montant maximum que la loi permet de verser en dividendes. | Bénéfice – pertes passées – réserve légale |
    | Dividende | La part du bénéfice versée aux associés. | Le dividende décidé par l'AGO de C01 |
    | Compte courant d'associé | De l'argent qu'un associé prête à sa société. C'est une dette de la société. | Le gérant avance 20 000 € pour payer un fournisseur |
    | AGO / AGE | L'assemblée des associés : ordinaire (comptes annuels) ou extraordinaire (modifier les statuts, le capital). | L'AGO approuve les comptes ; l'AGE augmente le capital |
    | Convention réglementée | Un contrat entre la société et l'un de ses dirigeants ou associés, qui doit être signalé aux associés. | Le bail du local du gérant de C03 Garage Martin |

---

## 1. La structure des capitaux propres (classe 1)

> 🟢 **En clair :** les capitaux propres, c'est ce qui appartient aux associés : l'argent qu'ils ont apporté (capital) et les bénéfices laissés dans la société (réserves, report à nouveau). Attention aux comptes qui leur ressemblent mais sont des dettes ou des créances, comme le compte courant d'associé.

| Compte | Intitulé | Ce qu'on y trouve | Exemple du portefeuille |
|---|---|---|---|
| **101** | Capital | **1011** souscrit non appelé ; **1012** souscrit appelé non versé ; **1013** souscrit appelé versé | Studio Pixel (C25) : 10 000 € dont une partie non appelée |
| **104** | Primes liées au capital | **1041** primes d'émission ; 1042 de fusion ; 1043 d'apport ; 1044 de conversion d'obligations | TechNova (C08) : levées de fonds avec prime |
| **105** | Écarts de réévaluation | Réévaluation libre (rare, fiscalement coûteuse) | — |
| **106** | Réserves | **1061** réserve légale ; 1062 indisponibles ; **1063** statutaires ou contractuelles ; 1064 réglementées ; **1068** autres réserves (facultatives) | Boulangerie Dupain (C01) |
| **108** | Compte de l'exploitant | Apports et prélèvements de l'**entrepreneur individuel** pendant l'exercice | Dr Lambert (C05), à défaut de société |
| **110 / 119** | Report à nouveau créditeur / débiteur | Bénéfices non affectés / pertes non apurées | Mode & Co (C09) : report à nouveau débiteur |
| **120 / 129** | Résultat de l'exercice (bénéfice / perte) | Solde des classes 6 et 7 en attente d'affectation | Tous |
| **13** | Subventions d'investissement | 131 subventions reçues ; **139** subventions inscrites au compte de résultat (reprises) | TechNova (Bpifrance), Les Jardins Solidaires (C14) |
| **14** | Provisions réglementées | **145** amortissements dérogatoires ; 143 hausse des prix ; 148 autres | Garage Martin (C03), Transports Leroy (C11) |

**Comptes d'actif et de tiers associés** (à ne jamais confondre avec les capitaux propres) :

| Compte | Intitulé | Rôle |
|---|---|---|
| **109** | Actionnaires : capital souscrit non appelé | **Actif** (en tête du bilan) : contrepartie du 1011 |
| **4561** | Associés – comptes d'apport en société (45611 apports en nature, 45615 apports en numéraire) | Promesse d'apport |
| **4562** | Apporteurs – capital appelé, non versé (45621 actionnaires, 45625 associés) | Créance sur les associés pour la fraction appelée |
| **4563** | Associés – versements reçus sur augmentation de capital | Fonds reçus avant la réalisation définitive de l'augmentation |
| **4564** | Associés – versements anticipés | Versement avant l'appel |
| **4566** | Actionnaires défaillants | Associé qui ne paie pas après appel |
| **4567** | Associés – capital à rembourser | Réduction de capital non motivée par des pertes |
| **455** | Associés – comptes courants (4551 principal, 4558 intérêts courus) | **Dette** de la société envers l'associé |
| **457** | Associés – dividendes à payer | Dette née de la décision de distribution |
| **4422 / 4423** | Prélèvements forfaitaires non libératoires / retenues et prélèvements sur distributions | Retenues à la source sur dividendes reversées à l'État (*subdivisions à adapter au plan de comptes du cabinet*) |

> 💡 **Réflexe senior :** « capitaux propres » au sens du Code de commerce (test de la moitié du capital, art. L. 223-42 / L. 225-248) = **total de la rubrique « Capitaux propres » du bilan**, y compris subventions d'investissement et provisions réglementées. Les **comptes courants d'associés** n'en font **pas** partie (ce sont des dettes), pas plus que les avances conditionnées (« autres fonds propres »).

> 🟢 **En clair :** pour savoir si une société a « perdu la moitié de son capital », on prend tout le bloc « Capitaux propres » du bilan. Les comptes courants d'associés n'en font jamais partie : ce sont des dettes.

---

## 2. La constitution : souscription, apports, libération

> 🟢 **En clair :** quand une société naît, les associés promettent un apport (souscription), puis le versent, parfois en plusieurs fois (libération). Exemple : C25 Studio Pixel a un capital de 10 000 €, dont une partie n'a pas encore été demandée aux associés.

### 2.1 Les règles de libération à connaître par cœur

| Forme | Apports en numéraire : libération minimale à la constitution | Solde | Apports en nature |
|---|---|---|---|
| **SARL / EURL / SELARL** | **1/5** du montant | Dans les **5 ans** de l'immatriculation, sur décision du gérant | Libérés **intégralement** dès l'émission |
| **SAS / SA** | **1/2** du montant | Dans les **5 ans** (sur décision du président / du conseil) | Libérés intégralement |
| **Augmentation de capital SA / SAS** | **1/4 du nominal** + **totalité de la prime d'émission** | 5 ans | Intégralement |
| **SCI, SNC** | Libre (statuts) | Statuts | — |

- Les fonds sont **déposés sur un compte bloqué** (banque, notaire ou Caisse des dépôts) au nom de la société en formation ; le **certificat du dépositaire** (« attestation de dépôt des fonds ») accompagne le dossier d'immatriculation. Ils sont débloqués sur présentation du Kbis.
- **Commissaire aux apports** : désigné en principe pour évaluer les apports en nature. Les associés peuvent décider **à l'unanimité** de s'en dispenser si **aucun apport en nature n'excède 30 000 €** et si **le total des apports en nature n'excède pas la moitié du capital** (SARL : art. L. 223-9 C. com. ; régime transposé aux SAS). Sans commissaire, les associés sont **solidairement responsables pendant 5 ans** de la valeur attribuée aux apports.
- **Capital minimum** : 1 € pour SARL et SAS (37 000 € pour une SA).

> 🟢 **En clair :** quand un associé apporte un bien (et non de l'argent), un expert l'évalue en principe : le commissaire aux apports. Les associés peuvent s'en passer, s'ils sont tous d'accord et si les apports en nature restent limités. Mais ils répondent alors eux-mêmes de la valeur annoncée pendant 5 ans.

### 2.2 Les écritures de constitution (schéma complet)

| Étape | Débit | Crédit |
|---|---|---|
| 1. Souscription (promesse d'apport) | 4561 (45611 nature / 45615 numéraire) | 1011 Capital souscrit non appelé |
| 2. Appel de la fraction exigible | 4562 (appelé) ; 109 (non appelé) | 4561 |
| | 1011 (pour la fraction appelée) | 1012 Capital souscrit appelé non versé |
| 3. Réalisation des apports | 512 (fonds) ; 2xx (biens apportés) | 4562 |
| | 1012 | 1013 Capital souscrit appelé versé |

Au final : **1013** = capital libéré ; **1011** = capital non appelé, avec sa contrepartie **109** à l'actif. En pratique, de nombreux logiciels passent une écriture **simplifiée** directe (D 512 / 2xx / 109 – C 1013 / 1011) : acceptable si les comptes de détail sont soldés et si la ventilation 1011/1013 est juste.

**Apport en nature** : le bien entre à l'actif pour sa **valeur d'apport** (valeur figurant aux statuts), qui devient sa base amortissable. Pas de TVA si l'apporteur est un particulier.

### 2.3 Les frais de constitution

| Option | Traitement comptable | Conséquence |
|---|---|---|
| **Charges** (méthode préférentielle) | 6226 honoraires, 6231 annonces légales, 6227 frais d'actes, 627 frais bancaires… | Perte du premier exercice plus forte, rien à suivre |
| **Actif** (frais d'établissement, 201) | Amortis sur **5 ans au plus** | **Aucune distribution** tant que les réserves libres ne couvrent pas le montant non amorti (art. L. 232-9 C. com.) |

**Dépenses engagées avant l'immatriculation** : reprises par la société si elles figurent sur l'**état des actes accomplis pour le compte de la société en formation** annexé aux statuts (ou sont reprises ensuite par une décision des associés). Payées par un associé → **crédit de son compte courant 455**.

> ⚠️ **Erreur classique :** saisir la facture d'avocat libellée au nom personnel du fondateur avec récupération de TVA. Pour déduire la TVA, la facture doit être établie au nom de la **société (en formation)**. On demande une facture rectificative.

---

## 3. Libération ultérieure, défaillance, compensation

> 🟢 **En clair :** cette section traite la suite : le dirigeant demande le reste du capital, un associé ne paie pas, ou un associé paie en avance. Enjeu concret : tant que le capital n'est pas entièrement versé, la société n'a pas droit au taux réduit d'IS de 15 %.

| Opération | Débit | Crédit |
|---|---|---|
| Appel du solde (décision du dirigeant) | 4562 | 109 |
| | 1011 | 1012 |
| Versement | 512 | 4562 |
| | 1012 | 1013 |
| Associé qui ne paie pas à l'échéance | 4566 Actionnaires défaillants | 4562 |
| Versement anticipé (avant l'appel) | 512 | 4564 |

- À défaut de libération dans le délai, les sommes portent **intérêt de retard de plein droit** et la société peut, après mise en demeure, faire vendre les titres du défaillant (procédure propre aux sociétés par actions).
- La **libération intégrale du capital** conditionne : le **taux réduit d'IS** de 15 % (art. 219-I-b CGI) et la **déductibilité des intérêts de comptes courants** (art. 39-1-3° CGI). Un capital non libéré de quelques centaines d'euros peut coûter des milliers d'euros d'impôt.

> 💡 **Réflexe senior :** au moment de la révision, comparez la **balance** (1011/109/4562) aux **statuts et au Kbis** : un 109 « oublié » depuis des années signifie soit un appel jamais fait, soit une libération jamais comptabilisée.

---

## 4. Augmentation de capital

> 🟢 **En clair :** augmenter le capital, c'est faire entrer de l'argent ou un bien, ou transformer des sommes déjà présentes (réserves, compte courant) en capital. Exemple : C08 TechNova lève des fonds auprès d'investisseurs, qui paient une prime en plus de la valeur de base des actions.

### 4.1 Les modalités

| Modalité | Écriture type | Remarque |
|---|---|---|
| **Apport en numéraire** avec prime | 4561 / 1011 + 1041, puis schéma d'appel et de versement | Fonds reçus avant la réalisation → **4563**, soldé à la date du **certificat du dépositaire** |
| **Incorporation de réserves** | 106x (ou 110, 1041) / 1013 | Pas de flux de trésorerie ; actions gratuites ou hausse du nominal |
| **Compensation avec un compte courant** | 455 / 1013 (+ 1041) | Créance **liquide et exigible** ; arrêté de compte certifié (CAC ou commissaire désigné) dans les sociétés par actions |
| **Apport en nature** | 2xx / 1013 (+ 1043 prime d'apport) | Commissaire aux apports en principe |

**Prime d'émission** = (prix d'émission – nominal) × nombre de titres. Elle protège les anciens associés de la dilution de la valeur des réserves accumulées. Le **droit préférentiel de souscription** (DPS) peut être supprimé au profit de personnes dénommées (rapport du dirigeant, et du CAC s'il existe).

### 4.2 Les frais d'augmentation de capital (PCG)

Trois traitements possibles :
1. **Imputation sur la prime d'émission**, **nette d'impôt** (méthode largement retenue dans les levées de fonds) : **D 1041 / C 401**, TVA déductible en 44566. Si l'économie d'impôt existe, elle est rattachée aux capitaux propres (D 695 / C 1041 pour l'effet d'impôt).
2. **Charges** de l'exercice (622x, 623x…).
3. **Frais d'établissement** (201) amortis sur 5 ans au plus.

Seuls les **coûts externes directement attribuables** à l'opération sont imputables (avocats, conseils, certificat du dépositaire, formalités, commission de levée). Le temps passé en interne, la refonte d'un plan de BSPCE ou les travaux juridiques sans lien direct avec l'émission restent en charges (un pacte d'associés exigé par l'investisseur comme condition de la souscription peut, sur justification, être rattaché à l'opération).

> 🟢 **En clair :** seuls les frais payés à des prestataires extérieurs et liés directement à l'augmentation de capital peuvent être imputés sur la prime. Le reste va en charges.

> ⚠️ **Erreur classique :** passer les frais en charges puis les « transférer » via le compte **791**. **Les comptes de transfert de charges sont supprimés** depuis le règlement ANC n° 2022-06 (exercices ouverts depuis le 01/01/2025) : l'imputation sur la prime se fait **directement** au débit du 1041.

**Fiscalement**, les frais imputés sur la prime restent **déductibles** du résultat imposable : on les déduit **extra-comptablement** (2058-A, déductions diverses). La TVA sur ces frais est **déductible** dans les conditions de droit commun (frais généraux de l'entreprise).

---

## 5. Réduction de capital et « coup d'accordéon »

> 🟢 **En clair :** on peut aussi diminuer le capital : pour effacer des pertes, ou pour rendre de l'argent aux associés. Le « coup d'accordéon » consiste à réduire le capital puis à l'augmenter aussitôt, souvent pour remettre à flot une société en difficulté.

| Cas | Écriture | Formalités |
|---|---|---|
| **Réduction motivée par des pertes** (apurement) | D 1013 / C 119 (ou 129) | AGE ; pas d'opposition des créanciers |
| **Réduction non motivée par des pertes** (remboursement) | D 1013 / C 4567, puis D 4567 / C 512 | AGE ; **droit d'opposition des créanciers** ; CAC s'il existe |
| **Coup d'accordéon** (réduction à zéro puis augmentation) | Réduction : D 1013 / C 119 ; augmentation : schéma du § 4 | Réduction **sous condition suspensive** de l'augmentation ; capital minimum à respecter |

Le capital ne peut être réduit en dessous du minimum légal que sous condition d'une augmentation qui le porte au moins à ce minimum.

---

## 6. Le résultat, les réserves, le report à nouveau

> 🟢 **En clair :** chaque année, l'assemblée décide de ce que devient le bénéfice : réserve obligatoire, réserves libres, dividendes ou report à nouveau. Votre rôle : vérifier que la décision respecte la loi avant de l'enregistrer.

### 6.1 La réserve légale (art. L. 232-10 C. com.)

- **SARL, SELARL, EURL, SAS, SA** (pas les SCI, SNC, ni les associations).
- Dotation : **5 %** du **bénéfice de l'exercice diminué, le cas échéant, des pertes antérieures** (report à nouveau débiteur).
- Jusqu'à ce que la réserve atteigne **10 % du capital** ; la dotation est donc **plafonnée** au montant manquant. Si la réserve redescend sous 10 % (par exemple après une augmentation de capital), la dotation reprend.

> ⚠️ **Erreur classique :** doter 5 % du bénéfice alors que la réserve légale est déjà (presque) à 10 % du capital. On ne dote que ce qui manque.

### 6.2 Réserves statutaires, facultatives, report à nouveau

- **Réserve statutaire (1063)** : imposée par les statuts (dotation obligatoire, déduite du bénéfice distribuable).
- **Autres réserves (1068)** : décidées librement par l'AGO ; **distribuables** ultérieurement (la résolution doit alors indiquer **expressément** les postes de réserves prélevés).
- **Report à nouveau** : bénéfice non affecté (110) ou perte non apurée (119). Un 119 doit être **apuré en priorité** par les bénéfices suivants avant toute distribution.

### 6.3 Le bénéfice distribuable (art. L. 232-11 C. com.)

```
  Bénéfice de l'exercice
– Pertes antérieures (report à nouveau débiteur)
– Dotation à la réserve légale et aux réserves statutaires
+ Report à nouveau bénéficiaire
= BÉNÉFICE DISTRIBUABLE
+ Réserves disponibles (sur décision expresse de l'AGO)
= MONTANT MAXIMUM DISTRIBUABLE
```

**Deux verrous supplémentaires :**
1. Aucune distribution si les capitaux propres **sont ou deviendraient** inférieurs au capital augmenté des réserves non distribuables.
2. Frais d'établissement ou frais de développement **non amortis** à l'actif : pas de distribution si les réserves libres ne les couvrent pas.

**Distribution irrégulière** = **dividende fictif** : répétition auprès des associés (art. L. 232-17 C. com., si la distribution viole les règles ci-dessus ou si les bénéficiaires en connaissaient le caractère irrégulier ; prescription de 3 ans), et **délit** de répartition de dividendes fictifs pour les dirigeants (SARL : art. L. 241-3 ; SA/SAS : art. L. 242-6 C. com. — éléments constitutifs à vérifier au cas par cas).

> 🟢 **En clair :** distribuer plus que ce que la loi permet, c'est verser un « dividende fictif ». Les associés peuvent devoir le rembourser, et le dirigeant risque une sanction pénale.

### 6.4 L'affectation du résultat (écritures)

| Opération | Débit | Crédit |
|---|---|---|
| Affectation d'un bénéfice | 120 | 1061 / 1063 / 1068 ; **457** (dividendes) ; 110 (solde) ; ou **119** (apurement d'une perte antérieure) |
| Affectation d'une perte | 119 (report à nouveau débiteur) | 129 |
| Imputation d'une perte sur les réserves | 1068 | 129 ou 119 |
| Distribution de réserves | 1068 (ou 110) | 457 |
| Paiement des dividendes (associés personnes physiques) | 457 (brut) | 512 (net) ; 4422 (PFNL 12,8 %) ; 4423 (prélèvements sociaux) |
| Reversement à l'État avec l'imprimé 2777 | 4422 ; 4423 | 512 |

> 💡 **Réflexe senior :** le compte 120 de l'exercice N-1 doit être **soldé** à la date de l'AGO. Un 120 ou un 129 « N-1 » qui traîne dans la balance de l'exercice N, c'est une affectation oubliée — et souvent un PV jamais rédigé.

---

## 7. Les dividendes : fiscalité et obligations déclaratives

> 🟢 **En clair :** verser un dividende à une personne déclenche des retenues (impôt et prélèvements sociaux). La société doit les reverser à l'État dans des délais précis. Cas piège : le gérant majoritaire de SARL et l'associé d'une SELARL, comme C12 Pharmacie Centrale.

### 7.1 Associé personne physique (résident fiscal français)

| Étape | Règle (valeurs **à vérifier chaque année**) |
|---|---|
| **Au paiement** : prélèvement forfaitaire non libératoire (PFNL) | **12,8 %** du brut, acompte d'IR retenu par la société |
| **Au paiement** : prélèvements sociaux | **18,6 %** selon nos informations pour 2026 (hausse de la CSG sur les revenus du capital prévue par la LFSS 2026 ; 17,2 % auparavant) — **taux à vérifier** |
| **Taux global (PFU / « flat tax »)** | **31,4 %** (12,8 % + 18,6 %) selon nos informations — *à présenter avec prudence et à vérifier* ; option globale possible pour le **barème progressif** avec abattement de 40 % |
| **Dispense de PFNL** | Sur demande de l'associé (attestation sur l'honneur remise **avant le 30 novembre de l'année précédant le paiement**) si son revenu fiscal de référence N-2 est inférieur à **50 000 €** (célibataire) / **75 000 €** (couple) — *seuils à vérifier*. Les prélèvements sociaux restent dus. |
| **Déclaration et paiement** | Imprimé **2777** (télédéclaration et télépaiement) **au plus tard le 15 du mois suivant** le paiement des dividendes |
| **IFU** (imprimé fiscal unique, 2561) | Avant le **15 février de l'année suivante** : la société déclare les revenus distribués et les prélèvements opérés par bénéficiaire |

**Associé société** soumise à l'IS : aucune retenue ; si elle détient ≥ 5 %, **régime mère-fille** chez elle (cf. M10). Associé non-résident : retenue à la source (taux selon convention fiscale).

### 7.2 Le piège des gérants majoritaires et des associés de SEL (art. L. 131-6 CSS)

Pour un **gérant majoritaire de SARL/EURL à l'IS** et pour les **travailleurs indépendants exerçant dans une société d'exercice libéral** (SELARL, SELAS…), la fraction des dividendes qui excède **10 % du capital social, des primes d'émission et des sommes versées en compte courant** — **détenus par l'intéressé, son conjoint ou partenaire de PACS et leurs enfants mineurs** — est soumise aux **cotisations sociales des indépendants**, et non aux prélèvements sociaux.

> 🟢 **En clair :** pour ces dirigeants, la partie des dividendes qui dépasse 10 % de leur mise (capital, primes et compte courant détenus par eux et leur famille proche) est traitée comme un revenu d'activité. Elle supporte donc des cotisations sociales.

| Fraction | PFNL 12,8 % (retenu par la société) | Prélèvements sociaux (retenus par la société) | Cotisations sociales TNS |
|---|---|---|---|
| ≤ 10 % (capital + primes + CCA détenus) | Oui | Oui | Non |
| > 10 % | Oui | **Non** | **Oui** (déclarées par le dirigeant sur sa déclaration de revenus d'indépendant) |

> ⚠️ **Erreur classique :** calculer le seuil de 10 % sur **le capital total** de la société. C'est 10 % de la **quote-part détenue** par le dirigeant et sa famille proche (+ primes + comptes courants qu'ils détiennent).

Le **président de SAS** (assimilé salarié) n'est **pas** concerné : ses dividendes restent soumis au PFU / prélèvements sociaux, quel que soit le montant.

### 7.3 Délais

- **Mise en paiement** des dividendes : au plus tard **9 mois après la clôture** (prolongation possible par le président du tribunal de commerce).
- La décision de distribution crée une **créance** de l'associé sur la société (457) : elle ne peut plus être retirée unilatéralement.

---

## 8. Les acomptes sur dividendes (art. L. 232-12 C. com.)

> 🟢 **En clair :** un acompte sur dividendes, c'est verser une partie du dividende avant l'approbation des comptes. C'est permis, mais seulement avec un bilan intermédiaire certifié par un commissaire aux comptes.

Conditions **cumulatives** :
1. Un **bilan établi en cours ou en fin d'exercice**, **certifié par un commissaire aux comptes** (désigné à cet effet si la société n'en a pas) ;
2. Il fait apparaître un **bénéfice** — après amortissements et provisions, déduction des pertes antérieures et des dotations aux réserves légale et statutaires, augmenté du report bénéficiaire ;
3. Le montant de l'acompte **ne peut excéder** ce bénéfice ;
4. Décision de l'organe compétent (président de SAS selon les statuts, conseil d'administration, gérance) **après** la certification.

| Opération | Débit | Crédit |
|---|---|---|
| Décision de l'acompte | 4578 Associés – acomptes sur dividendes (subdivision interne) | 457 Dividendes à payer |
| Paiement | 457 | 512 ; 4422 ; 4423 |
| AGO suivante : affectation du résultat | 120 | 457 (dividende total) … |
| Imputation de l'acompte | 457 | 4578 |

Les retenues à la source (PFNL, prélèvements sociaux, 2777) s'appliquent **dès le paiement de l'acompte**. À la clôture, le solde débiteur du 4578 est présenté en **autres créances** (présentation usuelle) et commenté en annexe, jusqu'à la décision de l'AGO.

---

## 9. Les comptes courants d'associés

> 🟢 **En clair :** le compte courant d'associé, c'est de l'argent que l'associé prête à sa société. C'est une dette de la société, pas du capital. L'inverse (la société qui prête à son dirigeant) est en principe interdit.

- **Nature** : dette de la société (prêt de l'associé), remboursable **à tout moment** sauf convention de blocage. Une convention de blocage peut le faire assimiler à des quasi-fonds propres pour le banquier — mais jamais en comptabilité.
- **Intérêts** : déductibles si le **capital est entièrement libéré** et dans la limite d'un **taux maximum** publié chaque année (art. 39-1-3° et 212 CGI) ; l'excédent est réintégré et peut être requalifié en **revenu distribué**. Chez l'associé personne physique : PFNL 12,8 % + prélèvements sociaux retenus par la société (2777).
- **Compte courant débiteur** d'un gérant de SARL ou d'un dirigeant de SA/SAS personne physique : **interdit** (prêt au dirigeant prohibé, art. L. 223-21 et L. 225-43 C. com.) ; risque d'abus de biens sociaux et réintégration fiscale (art. 111-a CGI : avance présumée distribuée).
- **Abandon de créance** par un associé : produit chez la société débitrice ; souvent assorti d'une **clause de retour à meilleure fortune** (la créance renaît si la situation s'améliore — engagement hors bilan des deux côtés). Fiscalité chez l'associé société : les abandons **à caractère financier** sont en principe **non déductibles** (art. 39-13 CGI, sauf procédures collectives et conciliation) ; neutralisation en intégration fiscale.

> 🟢 **En clair :** un associé peut renoncer à se faire rembourser son compte courant (abandon de créance) pour aider la société. Souvent, il prévoit que la dette renaîtra si la société va mieux : c'est la clause de retour à meilleure fortune.

> 💡 **Réflexe senior :** un compte courant créditeur important + des capitaux propres négatifs = proposez au client une **augmentation de capital par compensation** ou un **abandon de créance** pour reconstituer les capitaux propres. Comparez les conséquences fiscales (l'abandon est un produit imposable chez la filiale, l'incorporation ne l'est pas).

---

## 10. Capitaux propres inférieurs à la moitié du capital social

> 🟢 **En clair :** quand les pertes ont « mangé » plus de la moitié du capital, la loi oblige les associés à se prononcer sur l'avenir de la société, dans des délais précis. Un point à surveiller chez un client en difficulté, comme C24 Menuiserie Bois & Création.

**Textes** : SARL art. **L. 223-42** C. com. ; SA art. **L. 225-248** (applicable aux SAS par renvoi).

```
Approbation des comptes faisant apparaître CP < ½ capital
   │
   └─► dans les 4 MOIS : consultation des associés (AGE) sur la DISSOLUTION ANTICIPÉE
          │
          ├─ dissolution votée → liquidation amiable
          │
          └─ pas de dissolution → publicité (journal d'annonces légales, greffe, RCS)
                 │
                 └─► au plus tard à la clôture du 2e exercice suivant celui de la constatation des pertes :
                       reconstituer les CP à hauteur d'au moins ½ capital
                       OU réduire le capital du montant des pertes non imputées sur les réserves
```

- Calcul : capitaux propres **comptables** (capital + primes + réserves + report à nouveau + résultat + subventions d'investissement + provisions réglementées) comparés à **½ du capital social** (capital souscrit, appelé ou non).
- À défaut de consultation ou de régularisation, **tout intéressé** peut demander au tribunal la dissolution. La procédure a été **assouplie et modifiée à plusieurs reprises** (notamment par la loi PACTE de 2019) : vérifiez toujours la rédaction en vigueur et l'articulation avec le minimum légal de capital.
- Moyens de reconstitution : bénéfices futurs, augmentation de capital (en numéraire ou par compensation de compte courant), abandon de créance, réduction de capital, coup d'accordéon.

> ⚠️ **Erreur classique :** inclure les comptes courants d'associés dans les capitaux propres pour « éviter » la procédure. Un compte courant, même bloqué, reste une **dette**.

---

## 11. Le juridique annuel

> 🟢 **En clair :** chaque année, un calendrier juridique s'impose : approuver les comptes, les déposer au greffe, payer les dividendes, traiter les conventions entre la société et ses dirigeants. Exemple : C03 Garage Martin, dont le gérant loue le local à sa propre société.

### 11.1 Calendrier type (clôture au 31/12)

| Échéance | Acte | Texte |
|---|---|---|
| Avant l'AGO | Arrêté des comptes par le dirigeant ; rapport de gestion (sauf dispense) ; rapport spécial sur les conventions réglementées ; convocation (15 jours avant pour une SARL, documents joints) | C. com. |
| **Dans les 6 mois** de la clôture | **Approbation des comptes** par l'AGO (ou décision de l'associé unique) ; affectation du résultat | L. 223-26 (SARL), L. 225-100 (SA), statuts (SAS, dans la même limite) |
| Si dépassement prévisible | Demande de **prorogation** au président du tribunal de commerce **avant** l'expiration du délai | |
| **1 mois** après l'approbation (**2 mois** par voie électronique) | **Dépôt** des comptes annuels et de la décision d'affectation au greffe | L. 232-22 / L. 232-23 |
| **9 mois** après la clôture | Mise en paiement des dividendes au plus tard | L. 232-13 |

**Dispense de rapport de gestion** : les SARL, SAS et SA qui sont des **petites entreprises** (au sens de l'art. L. 123-16 C. com.) en sont dispensées (sauf exceptions) — les informations sur le rachat d'actions éventuel restent à fournir en annexe.

**EURL dont l'associé unique personne physique est gérant** : le **dépôt au greffe**, dans les 6 mois, de l'inventaire et des comptes annuels signés **vaut approbation** ; la décision d'affectation doit tout de même être **répertoriée dans le registre des décisions**.

### 11.2 Confidentialité des comptes déposés

| Catégorie (seuils relevés en 2024 — *à vérifier*) | Option |
|---|---|
| **Micro-entreprise** (2 des 3 seuils non dépassés : total bilan 450 000 €, CA net 900 000 €, 10 salariés) | Les comptes annuels **ne sont pas rendus publics** (déclaration de confidentialité jointe au dépôt) |
| **Petite entreprise** (total bilan 7,5 M€, CA net 15 M€, 50 salariés) | Le **compte de résultat** n'est pas rendu public |
| Exclusions | Notamment sociétés appartenant à un groupe (selon les cas), établissements de crédit, sociétés dont l'activité consiste à gérer des titres (holdings) — *liste à vérifier* |

Le défaut de dépôt expose le dirigeant à une **injonction** de déposer sous astreinte et à une contravention.

### 11.3 Conventions réglementées

| Forme | Conventions visées | Procédure |
|---|---|---|
| **SARL** (L. 223-19) | Entre la société et un **gérant** ou un **associé** (ou une société dirigée par l'un d'eux) | **Rapport** du gérant (ou du CAC) à l'AGO ; l'intéressé ne vote pas. EURL : associé unique gérant → simple **mention au registre** des décisions |
| **SAS** (L. 227-10) | Avec le président, un dirigeant, un associé disposant de plus de 10 % des droits de vote (ou la société qui le contrôle) | Rapport du président (ou du CAC) aux associés ; SAS à associé unique : mention au registre |
| **SA** (L. 225-38) | Administrateurs, DG, actionnaire > 10 % | **Autorisation préalable** du conseil + rapport du CAC + approbation de l'AGO |
| Toutes | **Conventions courantes conclues à des conditions normales** | Hors procédure |

Exemples du portefeuille : bail du local consenti par le gérant à sa société (Garage Martin), compte courant rémunéré, convention de trésorerie et d'animation (Delta Invest et ses filiales), abandon de créance de la holding à une filiale.

### 11.4 Le dossier juridique du cabinet (checklist annuelle)

- Registre des décisions (côté et paraphé ou dématérialisé) à jour ; PV signés.
- Statuts à jour (capital, siège, dirigeants) ; Kbis de moins de 3 mois au dossier.
- Bénéficiaires effectifs à jour (RBE) après toute cession de titres.
- Tableau des titres / registre des mouvements de titres (SAS) à jour.
- Rapport sur les conventions réglementées ; tableau des comptes courants et taux.
- Récépissé de dépôt des comptes, option de confidentialité.
- Suivi : capitaux propres < ½ capital ; libération du capital ; mandats (CAC, dirigeants) arrivant à échéance.

---

## 12. Subventions d'investissement et provisions réglementées

> 🟢 **En clair :** deux postes particuliers des capitaux propres. La subvention d'investissement (une aide pour acheter un bien) passe en résultat petit à petit, au rythme du bien financé. Les provisions réglementées (surtout les amortissements dérogatoires) existent pour un avantage fiscal.

**Subventions d'investissement (13)** : inscrites en capitaux propres (131), puis **reprises** au compte de résultat (D 139 / C 777 dans l'ancienne nomenclature — *compte de reprise à vérifier dans la nomenclature 2025 du PCG*) au rythme des amortissements du bien financé (bien amortissable) ou sur 10 ans / durée d'inaliénabilité (bien non amortissable). Option fiscale pour l'étalement (art. 42 septies CGI) ; à défaut, la subvention peut être comptabilisée directement en produit.

**Provisions réglementées (14)** : comptabilisées pour bénéficier d'un avantage fiscal (principalement **amortissements dérogatoires 145** : D 6872 / C 145 ; reprise D 145 / C 7872 — *subdivisions à vérifier dans la nomenclature 2025*). Elles figurent en capitaux propres mais comportent un **impôt latent** : un banquier ou un repreneur les retraite.

---

## 13. Les capitaux propres hors sociétés commerciales

> 🟢 **En clair :** hors sociétés commerciales, les règles changent : entrepreneur individuel, EURL à l'IR, SCI, associations. Exemple : C05 Dr Lambert, médecin en entreprise individuelle, ne verse pas de dividendes : ce qu'elle prend pour elle passe au compte 108 de l'exploitant.

- **Entreprise individuelle** (Dr Lambert C05, Paul Durand C17 s'il tient une comptabilité) : **101 capital individuel** + **108 compte de l'exploitant** (apports et prélèvements de l'année, D 108 / C 512 pour un prélèvement). À l'ouverture de l'exercice suivant, 108 et le résultat sont virés au **101**. La rémunération de l'exploitant **n'est pas une charge**.
- **EURL à l'IR** (Style & Vous C20) : la société a la personnalité morale ; les prélèvements de la gérante passent par son **compte courant** (455) ou sont comptabilisés en rémunération (644) **réintégrée** fiscalement ; le bénéfice est imposé à l'IR au nom de l'associée.
- **SCI à l'IR** (Les Tilleuls C06) : pas de réserve légale ; le résultat est affecté aux associés selon les statuts (comptes courants 455 individuels) ; le résultat **fiscal** (revenus fonciers, 2072) est imposé chez les associés qu'il soit distribué ou non. En cas de **démembrement**, le bénéfice courant revient à l'**usufruitier**, les distributions de réserves au **nu-propriétaire** (l'usufruitier exerçant en principe un **quasi-usufruit** sur les sommes distribuées).
- **Associations** (Les Jardins Solidaires C14) : fonds propres sans droit de reprise / avec droit de reprise, réserves, report à nouveau, fonds dédiés hors fonds propres — règlement ANC n° 2018-06 → **voir module M13**.

---

## 14. Checklist de fin de module

- [ ] Je sais passer la constitution d'une SAS au capital partiellement libéré avec un apport en nature (1011, 1012, 1013, 109, 4561, 4562).
- [ ] Je connais les seuils de libération (1/5 SARL, 1/2 SAS/SA, 1/4 + prime en augmentation) et la dispense de commissaire aux apports (30 000 € / ½ capital, unanimité).
- [ ] Je sais imputer des frais d'augmentation de capital sur la prime **sans compte 791**, et je distingue les frais imputables des autres.
- [ ] Je calcule la dotation à la réserve légale avec le **plafond de 10 %** et la base « bénéfice – pertes antérieures ».
- [ ] Je calcule le **bénéfice distribuable** et je refuse de comptabiliser une distribution qui le dépasse.
- [ ] Je sais passer l'affectation (120 → 1061/1068/457/110/119) et le paiement des dividendes avec PFNL, prélèvements sociaux et 2777 (15 du mois suivant).
- [ ] J'applique la règle des **10 %** aux gérants majoritaires et aux TNS de SEL, sur la **quote-part détenue** + primes + comptes courants.
- [ ] Je connais les conditions de l'**acompte sur dividendes** (bilan certifié **avant** la décision, plafond).
- [ ] Je calcule les capitaux propres au sens de L. 223-42 / L. 225-248 et je sais dérouler la procédure et son calendrier.
- [ ] Je sais comptabiliser un **abandon de créance avec clause de retour à meilleure fortune** chez les deux sociétés et l'annoncer en engagements hors bilan.
- [ ] Je tiens le calendrier : AGO dans les 6 mois, dépôt dans le mois (2 mois en ligne), confidentialité, conventions réglementées.

## À retenir en 30 secondes

- Capitaux propres = capital + primes + réserves + report à nouveau + résultat + subventions d'investissement + provisions réglementées. Le compte courant d'associé est une dette.
- Libération minimale à la création : 1/5 en SARL, 1/2 en SAS/SA. Tant que le capital n'est pas entièrement versé, pas de taux réduit d'IS.
- Avant d'enregistrer un dividende, calculez le bénéfice distribuable et la réserve légale (5 % du bénéfice, jusqu'à 10 % du capital).
- Dividendes versés à une personne : retenues à la source, imprimé 2777 au plus tard le 15 du mois suivant, puis IFU.
- Gérant majoritaire de SARL ou associé de SEL : règle des 10 % sur sa propre mise.
- Calendrier : comptes approuvés dans les 6 mois, déposés au greffe dans le mois (2 mois en ligne), dividendes payés dans les 9 mois.
- Capitaux propres sous la moitié du capital : consultez les associés dans les 4 mois qui suivent l'approbation des comptes.
