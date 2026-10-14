# Corrigé E11-01 — La constitution de Studio Pixel : capital partiellement libéré et apport en nature

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-01](../exercices/E11-01_constitution-studio-pixel.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**a) Le capital n'est pas égal à l'argent en banque.** Le capital social (10 000 €) est la somme des **souscriptions** : 7 000 € de numéraire + 3 000 € de nature. Ce qui est entré en banque (5 000 €) n'est que la **fraction libérée du numéraire**. L'apport en nature (3 000 €) est un actif (ordinateur, logiciel), pas de la trésorerie. Et 2 000 € restent **à libérer** : c'est du capital **souscrit non appelé**.

**b) Contrôle de la libération minimale (SAS : la moitié des apports en numéraire à la souscription).**

| Associé | Numéraire souscrit | Minimum ½ | Libéré | Conforme ? |
|---|---|---|---|---|
| Léo Martin | 5 000,00 | 2 500,00 | 4 000,00 | Oui |
| Sarah Cohen | 2 000,00 | 1 000,00 | 1 000,00 | Oui (juste au minimum) |
| **Total** | **7 000,00** | **3 500,00** | **5 000,00** | Oui |

Le minimum s'apprécie **pour chaque souscripteur**, pas seulement globalement. Le solde (2 000 €) doit être appelé par le président dans les **5 ans** de l'immatriculation (avant le 01/09/2030).

**c) Apport en nature.** Il est **intégralement libéré** dès l'émission (300 actions entièrement libérées) : c'est la règle. Dispense de commissaire aux apports : décision **unanime** (prévue à l'article 6), aucun apport > 30 000 € (2 200 € et 800 €) et total (3 000 €) ≤ ½ capital (5 000 €) → **dispense valable**. Contrepartie : responsabilité solidaire des associés pendant 5 ans. La valorisation paraît raisonnable (ordinateur acheté 2 899 € TTC 17 mois plus tôt, valorisé 2 200 € ; licence à 800 € pour un coût de 1 040 €) — on garde au dossier les factures d'origine.

**d) Anomalies relevées.**

| Pièce | Anomalie | Conséquence | Action |
|---|---|---|---|
| 2 — Certificat du dépositaire | Libellé « STUDIO PIXEL **SARL** » alors que la société est une SAS | Erreur matérielle ; l'immatriculation a été obtenue, mais le dossier juridique comporte une pièce incohérente | Demander à la banque une attestation rectifiée pour le dossier permanent |
| 3 — Facture d'avocat | Établie au nom de **M. Léo Martin** personnellement, et non de « Studio Pixel SAS en formation » | La société n'est pas titulaire d'une facture à son nom : **TVA de 360 € non déductible en l'état** (CGI art. 271-II) ; la dépense reste une charge de la société, reprise via l'état des actes annexé aux statuts | Demander à l'avocat une **facture rectificative** au nom de la société en formation ; déduire la TVA à réception |
| 4 — Frais de formalités et annonce | Factures au nom de la société en formation, payées par cartes personnelles | Rien d'anormal : dépenses reprises (état annexé), dette envers chaque associé | Créditer les comptes courants |

**e) Les frais avant immatriculation.** Ils figurent sur l'état des actes accomplis pour le compte de la société en formation : la signature des statuts emporte leur reprise à l'immatriculation. La société devient débitrice des associés qui les ont avancés → **comptes courants 455**. Ils appartiennent au **premier exercice** (qui commence le 01/09/2025, date d'immatriculation) et sont comptabilisés à cette date.

## 2. Calculs (détaillés, chaque montant justifié)

**Capital**
- Capital souscrit : 5 000 + 2 000 + 3 000 = **10 000,00 €** (1 000 actions × 10 €).
- Appelé à la constitution : numéraire libéré 4 000 + 1 000 = 5 000,00 + nature 3 000,00 = **8 000,00 €**.
- Non appelé : 10 000 – 8 000 = **2 000,00 €** (Léo 1 000 €, Sarah 1 000 €).

**Apport en nature** : 2 200,00 € (2183 Matériel informatique) + 800,00 € (205 Logiciel) = 3 000,00 €. Pas de TVA : l'apporteuse est un particulier. Base amortissable = valeur d'apport.

**Frais de constitution**

| Dépense | HT | TVA | TTC | Compte | Payé par |
|---|---|---|---|---|---|
| Avocat (statuts, formalités) | 1 800,00 | 360,00 | 2 160,00 | 6226 Honoraires | L. Martin |
| Frais de formalités (greffe, RBE) | 59,00 | 11,80 | 70,80 | 6227 Frais d'actes et de contentieux | L. Martin |
| Annonce légale | 196,00 | 39,20 | 235,20 | 6231 Annonces et insertions | S. Cohen |
| Frais bancaires de dépôt de capital | 125,00 | — | 125,00 | 627 Services bancaires | Banque |
| **Total** | **2 180,00** | **411,00** | **2 591,00** | | |

- Compte courant Léo : 2 160,00 + 70,80 = **2 230,80 €**.
- Compte courant Sarah : **235,20 €**.
- **TVA de l'avocat (360 €)** : tant que la facture rectificative n'est pas reçue, on la comptabilise en **4458 / compte d'attente** « TVA à régulariser » plutôt qu'en 44566 — ou, si la facture ne peut être obtenue avant la déclaration, en charge. On retient ci-dessous la comptabilisation en attente (subdivision 44568 « TVA déductible en attente de facture conforme », *subdivision interne*), à basculer en 44566 à réception de la facture rectificative. La TVA réellement déductible à ce stade est donc 11,80 + 39,20 = **51,00 €**.

## 3. Écritures comptables

**Question 2 — Pourquoi l'écriture de l'outil est fausse** : elle porte 10 000 € en banque alors que seuls 5 000 € ont été versés ; elle ignore l'apport en nature (3 000 € d'immobilisations) et la fraction non appelée (2 000 €) ; et elle crédite un compte 101 « global » au lieu de distinguer 1013 (appelé versé) et 1011 (non appelé). La balance afficherait une trésorerie fictive de 5 000 €, et le rapprochement bancaire ne tomberait jamais juste.

**Question 3 — Schéma complet (01/09/2025, journal OD)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/09/2025 | OD | 45615 | Associés – apports en numéraire | Souscription numéraire (L. Martin 5 000, S. Cohen 2 000) | 7 000,00 | |
| 01/09/2025 | OD | 45611 | Associés – apports en nature | Souscription apport en nature S. Cohen | 3 000,00 | |
| 01/09/2025 | OD | 1011 | Capital souscrit – non appelé | Souscription du capital – statuts du 18/08/2025 | | 10 000,00 |
| 01/09/2025 | OD | 45625 | Associés – capital appelé non versé | Appel numéraire 5 000 + nature 3 000 | 8 000,00 | |
| 01/09/2025 | OD | 109 | Actionnaires : capital souscrit non appelé | Numéraire non appelé (L. Martin 1 000, S. Cohen 1 000) | 2 000,00 | |
| 01/09/2025 | OD | 45615 | Associés – apports en numéraire | Appel / solde promesse numéraire | | 7 000,00 |
| 01/09/2025 | OD | 45611 | Associés – apports en nature | Appel / solde promesse nature | | 3 000,00 |
| 01/09/2025 | OD | 1011 | Capital souscrit – non appelé | Fraction appelée | 8 000,00 | |
| 01/09/2025 | OD | 1012 | Capital souscrit – appelé non versé | Fraction appelée | | 8 000,00 |
| 01/09/2025 | OD | 512 | Banque Rhodanienne | Fonds déposés le 05/08/2025 (certificat du dépositaire) | 5 000,00 | |
| 01/09/2025 | OD | 2183 | Matériel de bureau et informatique | Apport S. Cohen – station de montage | 2 200,00 | |
| 01/09/2025 | OD | 205 | Concessions, brevets, licences, logiciels | Apport S. Cohen – licence logiciel de montage | 800,00 | |
| 01/09/2025 | OD | 45625 | Associés – capital appelé non versé | Réalisation des apports | | 8 000,00 |
| 01/09/2025 | OD | 1012 | Capital souscrit – appelé non versé | Capital libéré | 8 000,00 | |
| 01/09/2025 | OD | 1013 | Capital souscrit – appelé versé | Capital libéré | | 8 000,00 |
| | | | | **Totaux** | **44 000,00** | **44 000,00** |

Soldes après écritures : 1013 = 8 000 (C) ; 1011 = 2 000 (C) ; 109 = 2 000 (D) ; 512 = 5 000 (D) ; 2183 = 2 200 ; 205 = 800 ; 4561x, 4562x, 1012 soldés. ✓

> Les fonds étaient indisponibles jusqu'au 03/09/2025 : si le cabinet suit un compte bancaire distinct pour le compte bloqué, on utilise un sous-compte 512 « compte de dépôt du capital » et on le vire au compte courant par 580 au déblocage. Ici, la banque a conservé le même numéro de compte : aucune écriture au déblocage.

**Écriture simplifiée équivalente**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/09/2025 | OD | 512 | Banque Rhodanienne | Constitution – numéraire libéré | 5 000,00 | |
| 01/09/2025 | OD | 2183 | Matériel de bureau et informatique | Apport en nature S. Cohen | 2 200,00 | |
| 01/09/2025 | OD | 205 | Concessions, brevets, licences, logiciels | Apport en nature S. Cohen | 800,00 | |
| 01/09/2025 | OD | 109 | Actionnaires : capital souscrit non appelé | Numéraire non appelé | 2 000,00 | |
| 01/09/2025 | OD | 1013 | Capital souscrit – appelé versé | Capital libéré | | 8 000,00 |
| 01/09/2025 | OD | 1011 | Capital souscrit – non appelé | Capital non appelé | | 2 000,00 |
| | | | | **Totaux** | **10 000,00** | **10 000,00** |

**Question 4 — Frais de constitution**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/09/2025 | OD | 6226 | Honoraires | Altea Avocats F 2025-0812 – statuts (repris, état annexé) | 1 800,00 | |
| 01/09/2025 | OD | 44568 | TVA déductible en attente de facture conforme | Altea F 2025-0812 – facture au nom de L. Martin | 360,00 | |
| 01/09/2025 | OD | 6227 | Frais d'actes et de contentieux | Guichet unique – immatriculation | 59,00 | |
| 01/09/2025 | OD | 6231 | Annonces et insertions | Avis de constitution | 196,00 | |
| 01/09/2025 | OD | 44566 | TVA déductible sur ABS | Formalités + annonce légale | 51,00 | |
| 01/09/2025 | OD | 4551 | Compte courant L. Martin | Frais avancés (avocat 2 160,00 + formalités 70,80) | | 2 230,80 |
| 01/09/2025 | OD | 4552 | Compte courant S. Cohen | Annonce légale avancée | | 235,20 |
| 03/09/2025 | BQ | 627 | Services bancaires | Frais de dépôt de capital | 125,00 | |
| 03/09/2025 | BQ | 512 | Banque Rhodanienne | Frais de dépôt de capital | | 125,00 |
| | | | | **Totaux** | **2 591,00** | **2 591,00** |

À réception de la facture rectificative : D 44566 / C 44568 pour 360,00 €. Si elle n'est jamais obtenue : D 6226 / C 44568 pour 360,00 € (la TVA devient une charge).

> TVA « sur les encaissements » : l'avocat étant prestataire de services sans option pour les débits, la TVA est exigible chez lui au paiement (20/08/2025), donc déductible chez Studio Pixel dès que la facture conforme est détenue — sur la première déclaration de TVA de la société.

**Question 5 — Présentation au bilan (avant tout appel du solde)**

| ACTIF | | PASSIF | |
|---|---|---|---|
| **Capital souscrit non appelé** (en tête de l'actif) | 2 000,00 | Capital social (dont versé 8 000) | 10 000,00 |
| Immobilisations incorporelles (logiciel) | 800,00 | Résultat de l'exercice (frais de constitution) | – 2 180,00 |
| Immobilisations corporelles (matériel) | 2 200,00 | **Capitaux propres** | **7 820,00** |
| TVA déductible (44566 + 44568) | 411,00 | Comptes courants d'associés | 2 466,00 |
| Banque | 4 875,00 | | |
| **Total** | **10 286,00** | **Total** | **10 286,00** |

(Bilan théorique au 03/09/2025, avant toute autre opération et avant amortissements, pour visualiser les postes.) Le capital figure **en totalité** (10 000 €) au passif ; le non appelé apparaît **à l'actif**, et l'annexe indique « capital de 10 000 € dont 2 000 € non appelés ».

## 4. Points d'attention / pièges

- **Capital ≠ trésorerie** : un Kbis à 10 000 € ne dit rien du montant libéré. Toujours partir des statuts et du certificat du dépositaire.
- **Libération minimale par souscripteur** : Sarah est exactement au minimum (50 %) ; à 900 €, sa souscription aurait été irrégulière.
- **Apport en nature toujours intégralement libéré** : jamais de « nature non appelée ».
- **Facture au nom du fondateur** : charge reprise par la société (état des actes) mais TVA non déductible tant que la facture n'est pas au nom de la société en formation.
- **Les dépenses avant immatriculation** appartiennent au premier exercice : ne pas les « perdre » parce qu'elles sont antérieures au 01/09/2025.
- **Comptes courants** : les avances des associés sont des **dettes** de la société (pas des apports en capital). Leur remboursement n'est soumis à aucune formalité, mais il doit être cohérent avec la trésorerie.
- **Capital non entièrement libéré** : tant que les 2 000 € ne sont pas versés, Studio Pixel **ne remplit pas** la condition de libération intégrale du taux réduit d'IS (appréciée à la clôture — voir E11-02 et E10-03) ni celle de déductibilité des intérêts de comptes courants.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à Léo Martin (question 7)**

> Objet : Studio Pixel — reprise de la comptabilité de création : 3 points à régulariser
>
> Bonjour Léo,
>
> Nous avons repris les écritures de création de Studio Pixel. Trois points :
>
> 1. **Capital** : le capital est bien de 10 000 €, mais seuls 8 000 € sont libérés (5 000 € versés en banque + 3 000 € d'apport en matériel par Sarah). Les 2 000 € restants (1 000 € chacun) devront être appelés par vous, en tant que président, d'ici le 01/09/2030 au plus tard. **Nous vous conseillons de les appeler avant le 31/12/2026** : tant que le capital n'est pas entièrement libéré à la clôture, la société ne peut pas bénéficier du taux réduit d'impôt sur les sociétés de 15 %.
> 2. **Facture de l'avocat** : elle est à votre nom personnel. La société ne peut donc pas récupérer les 360 € de TVA. Pouvez-vous demander au cabinet Altea une facture rectificative au nom de « Studio Pixel SAS en formation, représentée par M. Léo Martin » ? Les 2 160 € (+ 70,80 € de frais de greffe) sont inscrits sur votre compte courant d'associé : la société vous doit 2 230,80 €, que vous pourrez vous faire rembourser quand la trésorerie le permettra.
> 3. **Attestation de la banque** : elle mentionne « SARL » au lieu de « SAS ». Merci de demander à la Banque Rhodanienne une attestation rectifiée, que nous conserverons dans le dossier juridique.
>
> Sarah dispose de son côté d'un compte courant de 235,20 € (annonce légale).
>
> Bien cordialement,
> [Prénom Nom] — Cabinet Ferrand & Associés

**Question 6 — Option « frais de constitution à l'actif »** : on aurait inscrit 2 180 € en **201 Frais d'établissement**, amortis sur 5 ans au plus. Effet : perte du premier exercice moins forte (meilleure image pour le banquier), mais :
- **aucune distribution** possible tant que les réserves libres ne couvrent pas les frais non amortis (art. L. 232-9 C. com.) ;
- le poste est retraité (« non-valeur ») par tous les analystes financiers ;
- c'est la méthode **non préférentielle** ; les frais sont de toute façon fiscalement déductibles.
Pour 2 180 €, le jeu n'en vaut pas la chandelle : charges.

**Contrôles et dossier permanent** :
- Classer : statuts signés, état des actes annexé, certificat du dépositaire (rectifié), Kbis, factures d'origine du matériel apporté (preuve de la valeur), décision unanime de dispense de commissaire aux apports.
- Créer le **tableau des immobilisations** avec date de mise en service 01/09/2025 et base = valeur d'apport (2 200 € et 800 €), durées à arrêter avec Sarah (3 ans pour le matériel informatique, 1 à 3 ans pour le logiciel — à justifier selon l'usage).
- Ouvrir un **suivi des comptes courants** par associé (4551 Léo, 4552 Sarah).
- Créer une alerte « appel du solde du capital » dans le planning du dossier.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. L. 227-1 (renvoi aux règles de la SA pour la SAS), art. L. 225-3 (libération de la moitié du numéraire, solde dans les 5 ans), dispositions transposant à la SAS la dispense de commissaire aux apports (conditions identiques à l'art. L. 223-9 pour la SARL : 30 000 € et ½ capital, unanimité), art. L. 210-6 (reprise des actes accomplis pour le compte de la société en formation), art. L. 232-9 (frais d'établissement non amortis et distributions).
- PCG : comptes 1011, 1012, 1013, 109, 4561, 4562, 455 ; frais d'établissement (méthode préférentielle : charges) ; coût d'entrée des biens apportés = valeur d'apport.
- CGI : art. 271-II (facture au nom de l'assujetti), art. 219-I-b (condition de capital entièrement libéré pour le taux réduit).
- BOFiP : TVA – Droits à déduction – dépenses engagées avant le début de l'activité taxable.
