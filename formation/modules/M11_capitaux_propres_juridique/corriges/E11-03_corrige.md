# Corrigé E11-03 — TechNova : augmentation de capital avec prime d'émission et frais

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-03](../exercices/E11-03_augmentation-capital-technova.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Le prix d'émission se décompose en deux** : la **valeur nominale** (1 €), qui augmente le capital, et la **prime d'émission** (49 €), qui rémunère la valeur créée par l'entreprise depuis sa création (les nouveaux investisseurs « achètent » une part des réserves, des déficits passés et du potentiel). La prime va en **1041**.

**Libération en augmentation de capital (SA/SAS)** : à la souscription, **au moins ¼ du nominal** et **la totalité de la prime**. Claire Vasseur a versé 150 € de nominal (¼ de 600 €) et 29 400 € de prime : c'est le minimum légal. Il reste **450 €** de capital **souscrit non appelé**, à appeler dans les 5 ans.

**Question 2** : oui, Émilie a eu raison. La prime d'émission doit être **intégralement libérée à la souscription** (art. L. 225-144 C. com., applicable aux SAS) ; une libération de la moitié de la prime aurait rendu la souscription irrégulière, et le dépositaire n'aurait pas pu certifier la libération conforme à la résolution d'AGE.

**Le compte 4563** : les fonds arrivent sur un compte **indisponible** avant que l'augmentation soit réalisée. Tant que le certificat du dépositaire n'est pas établi, l'augmentation n'existe pas : on constate une dette envers les souscripteurs (**4563 Associés – versements reçus sur augmentation de capital**). L'augmentation est **réalisée à la date du certificat du dépositaire** (24/03/2027) : on passe alors les écritures de capital.

**Les frais** : seuls les **coûts externes directement attribuables** à l'émission sont imputables sur la prime :

| Frais | HT | Imputable ? | Raison |
|---|---|---|---|
| Lex Rhône – opération (rapport, PV, bulletins, formalités) | 9 500,00 | **Oui** | Coût direct de l'émission |
| Lex Rhône – pacte d'associés | 2 500,00 | **Oui** (jugement documenté) | Exigé par le FPCI comme **condition** de la souscription, signé le jour de la réalisation |
| Lex Rhône – règlement BSPCE 2027 | 2 500,00 | **Non** | Sans lien direct avec l'émission → charge (6226) |
| Capital Bridge – commission de succès 3 % | 9 000,00 | **Oui** | Directement liée au montant levé (3 % × 300 000 = 9 000 ✓) |
| Annonce et dépôt greffe | 250,00 | **Oui** | Formalités de l'opération |
| Certificat du dépositaire | 300,00 | **Oui** | Formalité de l'opération |

**Erreurs du projet d'Émilie (question 3)** :
1. **Banque débitée de 300 000 €** alors que 299 550 € ont été versés : la fraction **non appelée de 450 €** est ignorée (109 / 1011), et le rapprochement bancaire est faux de 450 €.
2. **Tout le nominal en 1013** (6 000 €) : seuls 5 550 € sont appelés et versés ; 450 € doivent figurer en **1011**.
3. **Pas de passage par 4563** à la réception des fonds (19/03) : sans gravité si l'arrêté est postérieur au 24/03, mais à corriger pour la piste d'audit — à une date d'arrêté intermédiaire, les fonds reçus avant le certificat ne sont pas encore du capital.
4. **Compte 791 « transfert de charges »** : **supprimé** depuis le règlement ANC n° 2022-06 (exercices ouverts depuis le 01/01/2025). L'imputation sur la prime se fait **directement** au débit du 1041, sans transiter par les charges.
5. **Imputation de 24 050 €** : elle inclut les 2 500 € du règlement BSPCE, qui ne sont pas imputables.
6. **Montant du 401** (28 500 €) : 17 400 + 10 800 + 300 = **28 500 €** ✓ — correct ; la banque (300 €) est bien créditée séparément.

## 2. Calculs (détaillés, chaque montant justifié)

**Émission**

| Élément | Calcul | Montant |
|---|---|---|
| Actions émises | 5 400 + 600 | 6 000 |
| Augmentation du capital (nominal) | 6 000 × 1 € | 6 000,00 € |
| Prime d'émission | 6 000 × 49 € | 294 000,00 € |
| Prix total | 6 000 × 50 € | 300 000,00 € |
| Versé par le FPCI | 5 400 × 50 € | 270 000,00 € |
| Versé par C. Vasseur | 600 × 1 € × ¼ + 600 × 49 € = 150 + 29 400 | 29 550,00 € |
| **Total versé** | | **299 550,00 €** |
| Nominal appelé et versé | 5 400 + 150 | 5 550,00 € |
| Nominal **non appelé** (C. Vasseur) | 600 – 150 | **450,00 €** |

**Capitaux après l'opération**
- Capital : 54 000 + 6 000 = **60 000 €** (60 000 actions), dont **450 € non appelés**.
- Prime d'émission : 1 196 000 + 294 000 – 21 550 (frais imputés) = **1 468 450,00 €**.

**Frais**
- Imputables (HT) : 9 500 + 2 500 + 9 000 + 250 + 300 = **21 550,00 €**.
- En charges : **2 500,00 €** (BSPCE).
- TVA déductible : 14 500 × 20 % + 9 000 × 20 % + 250 × 20 % = 2 900 + 1 800 + 50 = **4 750,00 €** (TechNova, redevable sur la totalité de son CA, déduit intégralement la TVA sur ces frais généraux ; les frais bancaires sont exonérés).
- Contrôle : 21 550 + 2 500 + 4 750 = 28 800 = 17 400 + 10 800 + 300 + 300 ✓.

**Répartition du capital après l'opération (60 000 actions)**

| Associé | Actions | % |
|---|---|---|
| Yanis Haddad | 62 % × 54 000 = 33 480 | 55,80 % |
| Cofondateurs | 18 % × 54 000 = 9 720 | 16,20 % |
| Business angels (anciens 6 480 + C. Vasseur 600) | 7 080 | 11,80 % |
| FCPI | 4 320 | 7,20 % |
| FPCI Rhône Capital Seed II | 5 400 | 9,00 % |
| **Total** | **60 000** | **100,00 %** |

Personnes physiques : 55,80 + 16,20 + 11,80 = **83,80 %**. Valorisation : pré-money 54 000 × 50 = 2 700 000 € ; post-money 60 000 × 50 = 3 000 000 €.

## 3. Écritures comptables

**Réception des fonds et réalisation de l'augmentation (schéma complet)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 19/03/2027 | BQ | 5124 | Banque – compte indisponible augmentation de capital | Vir. FPCI Rhône Capital Seed II + C. Vasseur | 299 550,00 | |
| 19/03/2027 | BQ | 4563 | Associés – versements reçus sur augmentation de capital | Souscriptions reçues avant réalisation | | 299 550,00 |
| 24/03/2027 | OD | 45615 | Associés – apports en numéraire | Souscription 6 000 actions à 50 € – AGE 12/03/2027 | 300 000,00 | |
| 24/03/2027 | OD | 1011 | Capital souscrit – non appelé | Souscription – nominal | | 6 000,00 |
| 24/03/2027 | OD | 1041 | Primes d'émission | Souscription – prime 6 000 × 49 € | | 294 000,00 |
| 24/03/2027 | OD | 45621 | Actionnaires – capital appelé non versé | Appel : nominal 5 550 + prime 294 000 | 299 550,00 | |
| 24/03/2027 | OD | 109 | Actionnaires : capital souscrit non appelé | ¾ du nominal C. Vasseur non appelé | 450,00 | |
| 24/03/2027 | OD | 45615 | Associés – apports en numéraire | Solde promesse | | 300 000,00 |
| 24/03/2027 | OD | 1011 | Capital souscrit – non appelé | Fraction appelée | 5 550,00 | |
| 24/03/2027 | OD | 1012 | Capital souscrit – appelé non versé | Fraction appelée | | 5 550,00 |
| 24/03/2027 | OD | 4563 | Associés – versements reçus sur augmentation de capital | Imputation des versements – certificat du dépositaire | 299 550,00 | |
| 24/03/2027 | OD | 45621 | Actionnaires – capital appelé non versé | Libération constatée | | 299 550,00 |
| 24/03/2027 | OD | 1012 | Capital souscrit – appelé non versé | Capital libéré | 5 550,00 | |
| 24/03/2027 | OD | 1013 | Capital souscrit – appelé versé | Capital libéré | | 5 550,00 |
| 24/03/2027 | BQ | 512 | Banque Rhodanienne – compte courant | Déblocage des fonds | 299 550,00 | |
| 24/03/2027 | BQ | 5124 | Banque – compte indisponible augmentation de capital | Déblocage des fonds | | 299 550,00 |
| | | | | **Totaux** | **1 509 750,00** | **1 509 750,00** |

(Hors mouvements de trésorerie 5124/512, les écritures de capital totalisent 910 650,00 € au débit et au crédit.)

Soldes : 1013 + 5 550 ; 1011 + 450 ; 109 + 450 (actif) ; 1041 + 294 000 ; 4561x, 4562x, 4563, 1012 soldés ✓.

**Frais (31/03/2027, à la réception des factures)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/03/2027 | AC | 1041 | Primes d'émission | Frais d'augm. de capital imputés : Lex Rhône (opération + pacte) 12 000 | 12 000,00 | |
| 31/03/2027 | AC | 6226 | Honoraires | Lex Rhône LR-27-0331 – règlement BSPCE 2027 | 2 500,00 | |
| 31/03/2027 | AC | 44566 | TVA déductible sur ABS | Lex Rhône LR-27-0331 | 2 900,00 | |
| 31/03/2027 | AC | 401 | Fournisseurs – Lex Rhône Avocats | F LR-27-0331 | | 17 400,00 |
| 31/03/2027 | AC | 1041 | Primes d'émission | Frais d'augm. de capital imputés : Capital Bridge commission 3 % | 9 000,00 | |
| 31/03/2027 | AC | 44566 | TVA déductible sur ABS | Capital Bridge CB-2027-014 | 1 800,00 | |
| 31/03/2027 | AC | 401 | Fournisseurs – Capital Bridge Conseil | F CB-2027-014 | | 10 800,00 |
| 31/03/2027 | AC | 1041 | Primes d'émission | Frais d'augm. de capital imputés : annonce + greffe | 250,00 | |
| 31/03/2027 | AC | 44566 | TVA déductible sur ABS | Annonces & Formalités AF-5521 | 50,00 | |
| 31/03/2027 | AC | 401 | Fournisseurs – Annonces & Formalités Rhône | F AF-5521 | | 300,00 |
| 24/03/2027 | BQ | 1041 | Primes d'émission | Frais d'augm. de capital imputés : certificat du dépositaire | 300,00 | |
| 24/03/2027 | BQ | 512 | Banque Rhodanienne | Frais certificat du dépositaire | | 300,00 |
| | | | | **Totaux** | **28 800,00** | **28 800,00** |

Le projet d'Émilie (pièce 5) est **supprimé** (contre-passation des trois écritures) et remplacé par les écritures ci-dessus.

## 4. Points d'attention / pièges

- **Plus de compte 791** : toute imputation de frais sur la prime se fait **directement**. Un 791 dans une balance 2025 ou postérieure est une anomalie à corriger.
- **Capital ≠ prime** : le 1013 ne reçoit que le **nominal** libéré.
- **Prime toujours libérée intégralement**, le nominal au moins au quart.
- **Date de réalisation** = certificat du dépositaire : un arrêté intermédiaire au 20/03/2027 aurait montré 299 550 € en 4563 (dette), pas en capitaux propres.
- **Tri des frais** : documenter le jugement sur le pacte d'associés (condition suspensive du term sheet) ; le règlement BSPCE reste en charges. Le temps de la DAF n'est jamais imputable.
- **Prime d'émission et bénéfice distribuable** : la prime est une réserve **distribuable** sur décision expresse de l'AGO (sauf clause contraire), mais en pratique les investisseurs l'encadrent dans le pacte.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 5 — Fiscalité des frais imputés sur la prime**
- Les frais imputés sur la prime **restent déductibles fiscalement** : on les déduit **extra-comptablement** sur la 2058-A 2027 (déductions diverses) pour **21 550 €**. Les 2 500 € passés en charges sont déduits normalement.
- **« Net d'impôt »** : le PCG prévoit l'imputation des frais nets de l'économie d'impôt qu'ils génèrent. En 2027, TechNova prévoit une **perte fiscale** : la déduction ne produit **aucune économie d'impôt** immédiate (elle augmente le déficit reportable, dont l'utilisation future est incertaine et plafonnée). On impute donc le **montant brut** (21 550 €), sans écriture d'effet d'impôt — choix à mentionner en annexe.
- Pour une société imposée à 25 % : effet d'impôt = 21 550 × 25 % = **5 387,50 €**. On aurait passé : D 1041 21 550 (frais) puis D 695 5 387,50 / C 1041 5 387,50, de sorte que la prime ne soit diminuée que de 16 162,50 € et que la charge d'IS du compte de résultat ne bénéficie pas d'une économie liée à une opération en capital.

**Question 6 — Réponse à Yanis : la libération partielle pose-t-elle un problème fiscal ?** Oui, potentiellement deux :
1. **Intérêts du compte courant de Yanis** (80 000 € à 4 % = 3 200 € par an) : leur déduction suppose que le **capital soit entièrement libéré** (art. 39-1-3° CGI). Avec 450 € non appelés depuis le 24/03/2027, les intérêts courus à compter de cette date risquent d'être **non déductibles** (*modalités d'appréciation à vérifier*). Enjeu : environ 3 200 × 9/12 = 2 400 € d'intérêts pour 2027, soit une base d'IS (ou de déficit) de 2 400 €.
2. **Taux réduit d'IS de 15 %** : condition de capital **entièrement libéré** (art. 219-I-b CGI). Sans effet en 2027 (perte prévue), mais à surveiller pour les exercices bénéficiaires.

Le seuil de 75 % de détention par des personnes physiques n'est pas en cause (83,80 % ; de plus, les participations de certains fonds de capital-risque ne sont pas prises en compte pour ce calcul — *à vérifier*).

**Conseil** : faire **appeler immédiatement les 450 €** par décision du président (Claire Vasseur a les moyens de les verser) : D 45621 / C 109 et D 1011 / C 1012, puis D 512 / C 45621 et D 1012 / C 1013. Coût : nul ; gain : sécurité fiscale.

**Question 7 — Formalités post-opération**
- Mise à jour des **statuts** (capital 60 000 €, 60 000 actions) ; **dépôt au greffe** (PV d'AGE, statuts à jour, certificat du dépositaire, rapports) et **avis dans un journal d'annonces légales** dans le mois ; inscription modificative au RCS via le guichet unique.
- **Registre des mouvements de titres** : inscription des 6 000 actions nouvelles ; mise à jour de la **table de capitalisation** (cap table) et des **bénéficiaires effectifs** si un seuil de 25 % est franchi (ce n'est pas le cas ici).
- **Enregistrement** de l'acte d'augmentation de capital (*droit applicable — exonération ou droit fixe — à vérifier*).
- Rapport complémentaire du président et du commissaire aux comptes sur les conditions définitives de l'opération, le cas échéant.
- Pacte d'associés : calendrier des obligations d'information des investisseurs (reporting).
- Information de Bpifrance et des prêteurs si les contrats de financement contiennent une clause de changement de contrôle ou d'information.

**Note à Émilie (extrait)**
> Émilie, trois corrections : (1) les 450 € non versés par Claire sont du capital **non appelé** (1011/109) — la banque n'a reçu que 299 550 € ; (2) le compte 791 n'existe plus depuis 2025 : on impute directement les frais au débit du 1041 ; (3) le règlement BSPCE (2 500 € HT) n'est pas un frais de l'augmentation de capital, il reste en honoraires. N'oubliez pas la déduction extra-comptable de 21 550 € sur la 2058-A 2027. Et pour Claire : vous avez eu parfaitement raison, la prime doit être versée en totalité.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. L. 225-129 et suivants (augmentation de capital), art. L. 225-135 et L. 225-138 (suppression du DPS au profit de personnes dénommées), art. L. 225-144 (libération du quart du nominal et de la totalité de la prime), art. L. 225-146 (certificat du dépositaire), art. L. 227-1 (application aux SAS).
- PCG : comptes 1011, 1012, 1013, 1041, 109, 4561, 4562, 4563 ; règles sur les frais d'augmentation de capital (imputation sur la prime nette d'impôt, ou charges) ; règlement ANC n° 2022-06 (suppression des comptes de transfert de charges).
- CGI : art. 39-1-3° (intérêts des comptes courants), art. 219-I-b (taux réduit), art. 209-I (report des déficits).
- BOFiP : BIC – frais d'augmentation de capital (déductibilité) ; TVA – droit à déduction des frais liés à l'émission de titres (jurisprudence CJCE, Kretztechnik, 2005).
