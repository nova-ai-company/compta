# M01 — Les fondamentaux du métier et la chaîne documentaire

> **Objectif du module.** Vous savez déjà saisir. L'objectif ici est de savoir **pourquoi** on saisit ainsi, de **refuser une pièce** qui ne tient pas, de reconstituer une opération à partir de documents incomplets et de garantir que le dossier résisterait à un contrôle fiscal. C'est la base de tout le reste de la formation : un senior se reconnaît d'abord à la qualité de ses pièces et de sa piste d'audit.

!!! abstract "En clair — ce module en 5 idées"
    1. Chaque écriture s'appuie sur une **pièce** : en général une facture adressée à l'entreprise. Un simple relevé de banque ou un ticket de carte ne suffit pas à récupérer la TVA.
    2. Les **principes comptables** servent à trancher les cas difficiles. Exemple : le fonds de commerce de C01 Boulangerie Dupain reste à 150 000 € dans les comptes, même si le gérant pense qu'il en vaut 250 000 €.
    3. Le **plan de comptes** classe tout en 8 familles. Le numéro du compte dit ce que c'est : 401 = fournisseurs, 411 = clients, 512 = banque, 6 = charges, 7 = produits.
    4. On range les écritures dans des **journaux** (achats, ventes, banque…), puis on **lettre** : on relie chaque facture à son paiement pour savoir ce qui reste dû.
    5. Une **facture** doit contenir des mentions précises et se corriger par un **avoir**, jamais en la supprimant. Depuis le 01/09/2026, toutes les entreprises doivent pouvoir recevoir des factures électroniques via une plateforme agréée. Exemple : C09 Mode & Co, la boutique en ligne, reçoit ses factures de grands fournisseurs par ce canal.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Pièce justificative | Le document qui prouve une opération : facture, contrat, relevé. | La facture du boulanger pour sa farine. |
    | Écriture | Une ligne (ou plusieurs) qui enregistre une opération dans les comptes, avec un débit et un crédit égaux. | Achat de farine : charge au débit, fournisseur au crédit. |
    | PCG | Le plan comptable général : la liste officielle des comptes et des règles. | Le compte 607 « Achats de marchandises » vient du PCG. |
    | Compte | Une « case » numérotée qui regroupe les opérations de même nature. | 512 = la banque. |
    | Journal | Un cahier où l'on range les écritures par type. | Journal des achats (AC), de banque (BQ). |
    | Lettrage | Relier une facture et son paiement avec un même code. | Facture de 1 860 € lettrée avec le virement de 1 860 €. |
    | Contre-passation | Annuler une écriture en passant la même à l'envers. | Pour supprimer un doublon proprement. |
    | FEC | Le fichier de toutes les écritures de l'année, à remettre aux impôts en cas de contrôle. | Exporté depuis le logiciel du cabinet. |
    | Piste d'audit fiable | Pouvoir relier la facture à la commande, à la livraison et au paiement. | Devis → bon de commande → bon de livraison → facture. |
    | Avoir | Un document qui réduit ou annule une facture. | Retour de 10 articles abîmés. |
    | HT / TTC | HT : prix sans la TVA. TTC : prix avec la TVA. | 100 € HT + 20 % = 120 € TTC. |
    | TVA déductible / collectée | Déductible : la TVA payée sur les achats, que l'on récupère. Collectée : la TVA facturée aux clients, que l'on reverse. | 44566 pour la déductible, 44571 pour la collectée. |
    | Facture électronique / PA | Une facture sous forme de données structurées, transmise par une plateforme agréée. Un PDF par e-mail n'en est pas une. | Format Factur-X. |
    | OCR | Le logiciel qui lit les pièces et propose l'écriture. | Il peut confondre date de facture et date d'échéance. |
    | Immobilisation | Un bien qui sert plusieurs années ; son coût est étalé (amortissement). | Un four de boulangerie. |

---

## 1. Les principes comptables : à quoi ils servent concrètement

> 🟢 **En clair :** les principes sont les grandes règles du jeu. Ils vous aident quand aucune règle précise ne répond à votre question. Exemple : un gain seulement espéré ne s'enregistre pas, une perte probable s'enregistre tout de suite.

Le Code de commerce (art. L. 123-12 et suivants) et le PCG posent des principes. Un junior les récite, un senior s'en sert pour **trancher un cas qui n'est écrit nulle part**.

| Principe | Ce qu'il dit | Exemple concret dans le portefeuille |
|---|---|---|
| **Image fidèle** (C. com. L. 123-14) | Les comptes doivent être réguliers, sincères et donner une image fidèle du patrimoine, de la situation financière et du résultat. Si l'application d'une règle ne suffit pas, on donne une information complémentaire en annexe. | Menuiserie Bois & Création (C24) : la continuité d'exploitation est incertaine → information obligatoire en annexe, même si chaque écriture est « juste ». |
| **Prudence** | On ne comptabilise pas un profit incertain ; on constate une perte probable dès qu'elle est connue. | Un litige client de Bâtisseurs du Sud (C02) → provision ; une ristourne fournisseur simplement « espérée » → rien. |
| **Indépendance des exercices** (rattachement) | Chaque exercice supporte les charges et produits qui le concernent, et seulement eux. | Abonnement annuel payé d'avance → charge constatée d'avance ; livraison du 29/09 facturée le 05/10 chez Garage Martin (C03, clôture 30/09) → facture non parvenue. |
| **Permanence des méthodes** | Les méthodes d'évaluation et de présentation ne changent pas d'un exercice à l'autre, sauf changement justifié (et alors expliqué en annexe). | Mode & Co (C09) valorise son stock au CMUP : impossible de passer au FIFO « parce que ça arrange le résultat ». |
| **Coût historique** | Les biens sont enregistrés à leur coût d'entrée (prix d'achat + frais accessoires directement attribuables), sans réévaluation (sauf réévaluation libre, encadrée). | Le fonds de commerce de la Boulangerie Dupain (C01) reste à 150 000 € même si le gérant estime qu'il en vaut 250 000 €. |
| **Non-compensation** | Pas de compensation entre actif et passif, ni entre charges et produits (sauf exceptions prévues). | Un fournisseur qui est aussi client : on garde 401 et 411 distincts ; la compensation se fait par une écriture explicite, appuyée sur un accord. |
| **Continuité d'exploitation** | Les comptes sont établis en supposant que l'entreprise poursuit son activité. | C24 encore : si la continuité est compromise, les règles d'évaluation changent. |
| **Importance relative** | Une information non significative peut être simplifiée. | C'est elle qui justifie de passer en charge un petit équipement de 289 € HT. |

> 💡 **Réflexe senior :** face à un cas inédit, demandez-vous : « Quelle écriture donne l'image la plus fidèle, sans anticiper un gain et sans masquer une perte ? » Puis documentez votre raisonnement dans le dossier (note de travail). Un raisonnement écrit vaut mieux qu'une écriture « évidente » qu'on ne sait plus justifier deux ans plus tard.

---

## 2. Les obligations comptables

> 🟢 **En clair :** la loi impose de tenir certains registres, de garder les documents longtemps (en pratique 10 ans) et d'avoir une pièce pour chaque écriture. C'est ce que l'administration vérifie en premier lors d'un contrôle fiscal.

### 2.1 Les documents obligatoires

| Document | Contenu | Point de vigilance |
|---|---|---|
| **Livre-journal** | Enregistrement chronologique de toutes les opérations, pièce par pièce (ou par récapitulation au moins mensuelle des totaux, si les pièces permettent de vérifier jour par jour). | En pratique : les **journaux auxiliaires** (achats, ventes, banque, caisse, OD) + leur centralisation. |
| **Grand livre** | Les écritures du journal ventilées par compte. | Doit être cohérent avec la balance au centime près. |
| **Livre d'inventaire** | Les données d'inventaire (stocks, créances, dettes, bilan et compte de résultat). | Souvent remplacé par le dossier de travail de clôture + les états financiers — à conserver. |
| **FEC** (fichier des écritures comptables) | Export normé de toutes les écritures de l'exercice (LPF art. L. 47 A ; format fixé à l'art. A. 47 A-1 du LPF). | À remettre dès le début d'un contrôle fiscal pour une comptabilité informatisée. Non-conformité ou défaut de remise : amende prévue à l'art. 1729 D du CGI. |

**Caractère définitif des écritures.** Une écriture validée (clôture de période) ne se supprime plus et ne se modifie plus : on corrige par **contre-passation** puis nouvelle écriture. Un logiciel qui permet de modifier une écriture validée n'est pas conforme.

> 🟢 **En clair :** une fois une période validée, on ne gomme plus. Pour corriger, on passe une écriture « à l'envers » qui annule l'erreur, puis la bonne écriture. Ainsi, on garde la trace de tout ce qui s'est passé.

### 2.2 Conservation

| Durée | Fondement | Ce qui est concerné |
|---|---|---|
| **10 ans** | Code de commerce (art. L. 123-22) | Documents comptables et pièces justificatives. |
| **6 ans** | Livre des procédures fiscales (art. L. 102 B) | Délai de conservation fiscal ; à partir de la dernière opération mentionnée. |

> En pratique : **10 ans** pour tout. Les factures sous forme électronique doivent être conservées **sous leur forme originale électronique** (une facture électronique imprimée n'est pas l'original).

### 2.3 La pièce justificative

Toute écriture doit s'appuyer sur une **pièce justificative** datée, qui permet d'en vérifier la réalité, le montant et le bénéficiaire. Le libellé de l'écriture doit permettre de **retrouver la pièce** (numéro de facture, nom du tiers).

Hiérarchie de la preuve, du plus solide au plus fragile :
1. facture originale (électronique via PA ou papier) adressée **à l'entreprise** ;
2. copie fiable d'une facture papier numérisée selon le processus réglementaire (CGI art. 289 VII et arrêté du 22 mars 2017 fixant les modalités de numérisation) ;
3. contrat, relevé, avis d'échéance, quittance ;
4. ticket de caisse détaillé ;
5. ticket de carte bancaire seul → **ne justifie ni la nature de la dépense, ni la TVA**.

> ⚠️ **Erreur classique :** saisir une dépense sur la base du relevé bancaire « parce que le client n'a pas envoyé la facture ». Le relevé prouve le paiement, pas la nature ni la TVA. Saisissez en compte d'attente, réclamez la pièce, et si elle ne vient jamais : TVA non déductible, et déductibilité fiscale de la charge à apprécier.

### 2.4 La piste d'audit fiable (PAF)

Pour la TVA, l'entreprise doit pouvoir établir un **lien entre une facture et la livraison de biens ou la prestation** qui en est le fondement (CGI art. 289 VII). Concrètement, pour un achat : **devis → bon de commande → bon de livraison / procès-verbal de réception → facture → règlement**. Les contrôles doivent être **documentés et permanents** (BOFiP, TVA – Facturation).

> 🟢 **En clair :** l'entreprise doit pouvoir prouver que chaque facture correspond à un vrai achat : quelqu'un a commandé, quelqu'un a reçu la marchandise, puis on a payé. Si cette chaîne de documents manque, le dossier est fragile en cas de contrôle fiscal.

> 💡 **Réflexe senior :** chez un client avec un service achats (Bâtisseurs du Sud, Imprimerie Graphique Rhône), demandez une fois par an la description de leur procédure : qui commande, qui réceptionne, qui « bon à payer ». C'est votre PAF, et c'est aussi la première question du commissaire aux comptes.

---

## 3. Le PCG « 2025 » : ce qui change avec le règlement ANC n° 2022-06

> 🟢 **En clair :** les règles comptables ont changé pour les exercices ouverts depuis le 01/01/2025. Deux réflexes à prendre : ne plus utiliser les comptes 791, 796 et 797, et ne plus mettre les amendes, pénalités et dons courants en « exceptionnel » (classe 67) mais en classe 65.

Le règlement ANC n° 2022-06 modernise le règlement n° 2014-03. Il est applicable aux **exercices ouverts à compter du 1er janvier 2025**. Pour les clôtures décalées du portefeuille (C03, C12, C13 au 30/09 ; C16 au 31/10 ; C21 au 31/08 ; C04 au 30/06), le premier exercice concerné est donc celui **ouvert en 2025** et clos en 2026.

| Thème | Avant | Depuis le règlement 2022-06 |
|---|---|---|
| **Transferts de charges** (791, 796, 797) | Très utilisés (IJSS, remboursements d'assurance, avantages en nature…). | **Supprimés.** Remboursement → en diminution de la charge concernée, ou en produit par nature selon le cas. **Ne jamais les utiliser.** |
| **Résultat exceptionnel** | Fourre-tout : amendes, dons, pénalités, régularisations… | **Restreint** aux produits et charges liés à un **événement majeur et inhabituel**. Amendes, pénalités, dons courants → **charges d'exploitation (classe 65)** : compte 658 (*subdivision selon la nomenclature 2025 du PCG*). Les cessions d'immobilisations restent en **675 / 775**. |
| **Changements comptables** | Définitions éparses. | Distinction clarifiée entre changement de méthode, changement d'estimation et correction d'erreur, avec traitement associé. |
| **États financiers et annexe** | Modèles anciens. | Modèles de bilan et de compte de résultat révisés, annexe refondue. |
| **Nomenclature** | — | Plusieurs comptes renumérotés ou créés (emprunts, frais d'émission, etc.). |

> ⚠️ **Erreur classique :** reprendre les « tables de correspondance » de l'an dernier dans le logiciel sans vérifier qu'il a bien été mis à jour. Contrôlez à chaque premier exercice concerné que les comptes 79x n'apparaissent plus et que les amendes ne remontent plus en 67.

> 💡 **Réflexe senior :** quand vous n'êtes pas sûr du numéro exact d'un compte de la nomenclature 2025, utilisez le compte à 3 chiffres (« 658 ») et notez *« subdivision à confirmer selon la nomenclature 2025 »*. Un compte à 3 chiffres juste vaut mieux qu'un compte à 6 chiffres inventé.

---

## 4. Structure du plan de comptes

> 🟢 **En clair :** tous les comptes sont rangés en 8 classes. Le premier chiffre suffit à savoir de quoi on parle : 2 = ce que l'entreprise garde longtemps, 4 = ce qu'elle doit ou ce qu'on lui doit, 5 = banque et caisse, 6 = dépenses, 7 = recettes. Apprenez aussi les comptes de TVA du tableau : vous les utiliserez chaque jour.

| Classe | Contenu | Comptes que vous utiliserez tous les jours |
|---|---|---|
| **1** Capitaux | Capital, réserves, résultat, provisions pour risques, emprunts. | 101, 106, 108 (exploitant), 120/129, 151, 164, 165 (dépôts reçus) |
| **2** Immobilisations | Incorporelles, corporelles, financières, amortissements, dépréciations. | 205 (logiciels), 207 (fonds), 213, 215, 218, 28x |
| **3** Stocks et en-cours | Matières, marchandises, en-cours, produits finis. | 31, 37, 39 |
| **4** Tiers | Fournisseurs, clients, personnel, organismes sociaux, État, associés, régularisations. | 401, 404, 408, 409x, 411, 418, 419x, 421, 431, 445x, 455, 467, 471, 486, 487 |
| **5** Financiers | Banques, caisse, virements internes, VMP. | 512, 53, 58 |
| **6** Charges | Par nature. | 60 achats, 61/62 services extérieurs, 63 impôts, 64 personnel, 65 autres charges, 66 financières, 67 exceptionnelles (restreintes), 68 dotations, 69 IS |
| **7** Produits | Par nature. | 70 ventes, 709 RRR accordés, 74 subventions, 75, 76, 77 (restreints), 78 reprises |
| **8** Comptes spéciaux | Engagements hors bilan, contributions volontaires en nature (associations : 86/87). | Les Jardins Solidaires (C14) |

**Comptes de TVA à maîtriser dès maintenant**

| Compte | Usage |
|---|---|
| 44562 | TVA déductible sur immobilisations |
| 44566 | TVA déductible sur autres biens et services |
| 445662 | TVA déductible intracommunautaire / autoliquidée (sous-compte usuel) |
| 4452 | TVA due intracommunautaire (autoliquidation) |
| 44571 | TVA collectée |
| 44574x (sous-compte usuel) | TVA collectée en attente d'encaissement (prestations de services) |
| 44586 | Taxes sur factures non parvenues |
| 44587 | Taxes sur factures à établir |
| 44551 | TVA à décaisser |
| 44567 | Crédit de TVA à reporter |

---

## 5. Les journaux et le lettrage

> 🟢 **En clair :** les journaux sont des « tiroirs » où l'on range les écritures par type (achats, ventes, banque, caisse, divers). Le lettrage consiste à relier une facture à son paiement. Un compte bien lettré montre tout de suite ce qui reste à payer ou à encaisser.

### 5.1 Les journaux auxiliaires

| Code usuel | Journal | Ce qu'on y passe | Ce qu'on n'y passe **pas** |
|---|---|---|---|
| **AC** | Achats | Factures et avoirs fournisseurs (y compris immobilisations, avec 404) | Les règlements |
| **VT** | Ventes | Factures et avoirs clients, Z de caisse si le cabinet les traite en ventes | Les encaissements |
| **BQ** (un par compte) | Banque | Tout ce qui figure sur le relevé : règlements, prélèvements, virements, frais | Une facture non payée |
| **CA** | Caisse | Mouvements d'espèces (recettes, dépenses, remises en banque via 58) | Les paiements CB |
| **OD** | Opérations diverses | Paie (si pas de journal dédié), régularisations, inventaire, amortissements, corrections | Ce qui a un journal spécifique |
| **AN** | À-nouveaux | Reprise des soldes de bilan | — |

> 💡 **Réflexe senior :** chaque mouvement entre banque et caisse transite par **58 « Virements internes »** : le retrait est saisi en BQ (58 / 512) et l'alimentation de la caisse en CA (530 / 58). Le 58 doit être **soldé** en fin de mois. Un 58 non soldé révèle un retrait dont on ignore la destination… souvent la poche du gérant.

### 5.2 Le lettrage

Lettrer, c'est rapprocher dans un compte de tiers les écritures qui se compensent (facture ↔ règlement ↔ avoir) en leur attribuant un même code. Un compte bien lettré permet :
- de connaître le **solde réel** de chaque tiers (ce qui reste dû, pièce par pièce) ;
- de détecter les **doublons**, les **factures manquantes**, les **règlements non affectés** ;
- de justifier la balance âgée au commissaire aux comptes ou au banquier.

Règles :
1. On lettre des **montants qui se soldent exactement** (une facture avec un règlement, ou une facture avec plusieurs règlements partiels, ou facture + avoir + règlement).
2. Un **règlement partiel** se lettre partiellement (lettrage partiel si le logiciel le permet) ou attend le solde.
3. Un **doublon** ne se « lettre » pas avec un règlement : il se **contre-passe**, et l'écriture d'origine est lettrée avec son extourne.
4. Un compte fournisseur **débiteur** est anormal (paiement en double, avoir non imputé, acompte) : on l'analyse, et à la clôture on reclasse en 409x.
5. Le lettrage se fait **au fil de l'eau**, pas en mai pour la liasse.

> ⚠️ **Erreur classique :** lettrer « au montant » sans regarder la référence. Deux factures de 1 860 € d'un même fournisseur peuvent coexister ; lettrer la mauvaise fausse la balance âgée et masque une facture impayée.

> 💡 **Réflexe senior :** demandez à chaque fournisseur important un **relevé de compte** à la clôture et rapprochez-le du grand livre. C'est la seule manière de découvrir les factures que le client n'a jamais transmises.

---

## 6. La chaîne commerciale

> 🟢 **En clair :** un achat laisse une suite de documents, du devis jusqu'au paiement. Votre travail : vérifier qu'ils racontent la même histoire (même quantité, même prix). Si ce n'est pas le cas, on demande un avoir avant de payer.

```
Devis ──► Bon de commande ──► Bon de livraison ──► Facture ──► (Avoir) ──► Règlement
(offre)    (engagement)        (preuve de la         (créance /    (correction)  (extinction
                                livraison / PV de     dette, TVA)                 de la dette)
                                réception)
```

| Document | Valeur | Ce que vous vérifiez |
|---|---|---|
| **Devis** | Offre de prix ; une fois signé (« bon pour accord »), il vaut contrat. | Prix unitaires, remises, conditions de livraison. |
| **Bon de commande** | Engagement de l'acheteur. Son numéro doit figurer sur la facture lorsqu'il a été émis par l'acheteur. | Quantités et prix = devis. |
| **Bon de livraison** / **PV de réception** | Preuve de la livraison effective ; les **réserves** y figurent. | Quantités réellement reçues, réserves (casse, manquants). |
| **Facture** | Fait générateur de la dette, justificatif de la TVA déductible. | Quantités = BL, prix = devis/BC, calculs, mentions. |
| **Avoir** | Document rectificatif qui réduit ou annule une facture (retour, rabais, remise, annulation). | Référence précise à la facture d'origine. |
| **Règlement** | Éteint la dette. | Montant = facture – avoirs (– escompte). |

> 💡 **Réflexe senior (le rapprochement « 3 voies ») :** **commande = livraison = facture**. Une facture ne se « bon à payer » que si les trois concordent. Un écart de quantité ou de prix se règle par un **avoir**, pas par un paiement partiel non documenté.

---

## 7. La facture

> 🟢 **En clair :** une facture doit contenir des informations précises (numéro, SIREN, TVA, dates, conditions de paiement…). S'il en manque, votre client peut perdre la TVA qu'il voulait récupérer. Une facture ne se supprime jamais : on la corrige par un avoir ou une facture rectificative.

### 7.1 Les mentions obligatoires (factures entre professionnels)

Sources : CGI art. 242 nonies A de l'annexe II (mentions fiscales) et Code de commerce art. L. 441-9 (mentions commerciales) ; Code de commerce art. R. 123-237 (identification de la société).

| Bloc | Mentions |
|---|---|
| **Identification** | Numéro unique, basé sur une séquence chronologique et continue ; date d'émission. |
| **Vendeur** | Nom/dénomination, adresse, **SIREN** (ou SIRET), n° de TVA intracommunautaire ; pour une société : forme juridique, capital social, RCS + ville. |
| **Client** | Nom/dénomination et adresse ; n° de TVA intracom du client pour les opérations intracommunautaires / autoliquidées ; adresse de facturation si différente. |
| **Opération** | Date de la livraison ou de la prestation (si différente de la date de facture) ; désignation précise, quantité, prix unitaire HT ; numéro du bon de commande s'il a été émis par l'acheteur. |
| **Montants** | Taux et montant de TVA par taux ; total HT ; réductions de prix acquises à la date de l'opération (remises, rabais, ristournes) ; total TTC. |
| **Paiement** | Date d'échéance ; conditions d'escompte (ou « pas d'escompte pour paiement anticipé ») ; **taux des pénalités de retard** ; **indemnité forfaitaire pour frais de recouvrement de 40 €** (C. com. art. D. 441-5). |
| **Mentions spéciales** | « Autoliquidation » (sous-traitance BTP, prestations intracom…) ; motif d'exonération (ex. « Exonération de TVA, art. 262 ter I du CGI » pour une livraison intracommunautaire) ; « TVA non applicable, art. 293 B du CGI » (franchise en base) ; « Régime particulier – biens d'occasion » (TVA sur la marge) ; option pour le paiement de la TVA d'après les débits. |

**Les nouvelles mentions liées à la réforme de la facturation électronique**

| Nouvelle mention | Pourquoi |
|---|---|
| **SIREN du client** | Adressage de la facture via l'annuaire de la réforme ; contrôle. |
| **Adresse de livraison** des biens si elle diffère de l'adresse du client | Localisation de l'opération. |
| **Nature de l'opération** : livraison de biens / prestation de services / mixte | La TVA n'est pas exigible au même moment (livraison vs encaissement). |
| **Option pour le paiement de la TVA d'après les débits**, le cas échéant | Indique au client à quel moment il peut déduire la TVA sur une prestation de services. |

> ⚠️ **Point à suivre :** ces mentions accompagnent le calendrier de la réforme. Le moment exact à partir duquel elles sont exigées sur les factures papier ou PDF encore émises par les PME entre le 01/09/2026 et le 01/09/2027 est à vérifier dans la doctrine en vigueur (elle a évolué). **Position du cabinet :** demandez-les dès maintenant à tous les fournisseurs et faites-les figurer sur toutes les factures émises par nos clients.

**Sanctions.** Amende fiscale par mention manquante ou inexacte (CGI art. 1737, plafonnée par facture) ; amende administrative prévue par le Code de commerce pour les manquements aux règles de facturation. Côté acheteur : une facture irrégulière peut faire **perdre le droit à déduction** de la TVA.

### 7.2 Factures spécifiques

| Type | Règles clés |
|---|---|
| **Facture d'acompte** | Obligatoire pour un acompte reçu d'un professionnel. Depuis 2023, la TVA est exigible à l'encaissement de l'acompte **aussi bien pour les livraisons de biens que pour les prestations de services**. La facture définitive reprend le total et **déduit** l'acompte déjà facturé (HT et TVA). |
| **Facture rectificative** | Corrige une mention (nom, adresse, SIREN, n° TVA…) ou un montant. Elle doit faire **référence à la facture initiale de manière précise et non équivoque** (numéro et date). Elle porte son propre numéro. |
| **Avoir** | Document rectificatif qui **diminue** une facture (retour, rabais, remise, annulation). Il réduit la base de TVA : le fournisseur récupère la TVA collectée, le client **reverse** la TVA déduite. |
| **Facture récapitulative** | Possible pour des livraisons multiples à un même client au cours d'un mois civil ; émise au plus tard à la fin du mois. |

**Numérotation.** Séquence **unique, chronologique et continue**, sans trou ; plusieurs séries sont admises si elles sont justifiées (par établissement, par type de document : FA / AV) et chacune continue. Une facture émise **ne se supprime jamais** : elle s'annule par un avoir.

> ⚠️ **Erreur classique :** « Je supprime la facture n° 87 dans le logiciel et je la refais. » Cela crée un trou dans la numérotation et casse la piste d'audit. On émet un avoir AV-xxx référençant la n° 87, puis une nouvelle facture.

### 7.3 Facture électronique ≠ facture PDF

**Calendrier de la réforme (CGI art. 289 bis et 290, dans leur rédaction issue des lois de finances successives) :**

| Date | Obligation | Qui |
|---|---|---|
| **01/09/2026** | **Réception** des factures électroniques | **Toutes** les entreprises assujetties à la TVA établies en France |
| **01/09/2026** | **Émission** de factures électroniques + **e-reporting** | Grandes entreprises (GE) et ETI |
| **01/09/2027** | **Émission** + **e-reporting** | PME, TPE, micro-entreprises |

Concepts :
- **Facture électronique** = facture émise, transmise et reçue sous **forme électronique structurée** (formats du socle : **UBL**, **CII**, **Factur-X** — PDF auquel est attaché un fichier XML structuré) via une **plateforme agréée (PA)**, anciennement appelée PDP.
- Un **PDF envoyé par e-mail n'est pas une facture électronique** au sens de la réforme.
- Le **cycle de vie** de la facture est suivi par des **statuts** transmis via les plateformes (déposée, rejetée, refusée, approuvée, encaissée…). Le statut **« encaissée »** est indispensable pour les prestations de services dont la TVA est exigible à l'encaissement.
- **E-reporting** : transmission à l'administration des données des opérations non couvertes par la facturation électronique domestique (B2C, international : ventes et achats avec des non-établis) et des données de paiement.
- **Annuaire** : il permet de savoir sur quelle PA adresser la facture d'un client identifié par son SIREN.

> 💡 **Réflexe senior :** depuis le 01/09/2026, pour chaque client du portefeuille, vous devez savoir : (1) quelle PA il a choisie pour recevoir ses factures ; (2) quels fournisseurs **GE/ETI** lui facturent désormais obligatoirement via PA ; (3) ce qui reste en papier/PDF (fournisseurs PME jusqu'au 01/09/2027, fournisseurs étrangers). Un PDF reçu d'une ETI après le 01/09/2026 est un signal d'alerte : soit l'original existe dans la PA (le PDF est une simple copie → risque de **doublon**), soit le fournisseur n'est pas en règle.

> ⚠️ **Erreur classique :** la photo WhatsApp d'une facture papier n'est **ni** une facture électronique, **ni** une copie fiable au sens de l'arrêté du 22 mars 2017. L'original papier doit être conservé.

---

## 8. OCR et pré-comptabilisation : gagner du temps sans perdre la maîtrise

> 🟢 **En clair :** le logiciel lit les factures et propose l'écriture à votre place. Il va vite, mais il se trompe toujours de la même façon si personne ne vérifie. Votre rôle passe de « saisir » à « contrôler » : dates, taux de TVA, avoirs, doublons.

L'outil de pré-comptabilisation du cabinet lit les pièces (OCR), propose un tiers, un compte, une ventilation de TVA, et « apprend » des validations précédentes. Il fait gagner un temps considérable… et produit des erreurs **systématiques** si personne ne contrôle.

| Piège | Exemple | Contrôle |
|---|---|---|
| **Mauvaise date** | L'outil lit la date d'échéance ou la date de livraison au lieu de la date de facture → mauvaise période, voire mauvais exercice. | Toutes les pièces datées autour de la clôture : contrôle visuel systématique. |
| **Ventilation de TVA multi-taux** | Une facture à 5,5 % / 10 % / 20 % lue avec un seul taux ; l'outil « équilibre » en gonflant le HT. | Recalculer TVA / HT pour chaque taux. |
| **Avoir lu comme une facture** | Sens inversé : la charge augmente au lieu de diminuer. | Filtrer les pièces portant « AVOIR » / montants négatifs. |
| **Autoliquidation non détectée** | Facture étrangère ou de sous-traitant BTP sans TVA → saisie « TVA 0 ». | Tout fournisseur étranger ou BTP : vérifier la mention et passer l'autoliquidation. |
| **Mémorisation abusive** | Le fournisseur « Amazon » est toujours imputé en 6063 → un téléviseur à 549 € HT part en charge. | Seuil d'alerte au-delà de 500 € HT sur les comptes de petit équipement. |
| **Doublons** | Même facture reçue en PDF par e-mail et via la PA ; ou fournisseur créé deux fois (« EDF » et « Électricité de France »). | Contrôle des doublons (n° de facture + tiers + montant) ; nettoyage du fichier tiers. |
| **Pièces non probantes** | Ticket CB, devis, bon de livraison saisis comme des factures. | Typologie de la pièce vérifiée avant validation. |

> 💡 **Réflexe senior :** l'OCR déplace votre travail de la **saisie** vers le **contrôle**. Gardez une liste de contrôles par dossier (fournisseurs étrangers, multi-taux, seuil immobilisation, période de clôture) et revoyez les règles de mémorisation au moins une fois par an.

---

## 9. Immobilisation ou charge ?

> 🟢 **En clair :** un bien qui sert plusieurs années et coûte plus de 500 € HT est une immobilisation : son coût est étalé sur sa durée d'utilisation. Un petit équipement ou une réparation courante est une charge de l'année. Exemple : un four pour C01 Boulangerie Dupain = immobilisation ; le remplacement d'un joint = charge.

Un bien est une **immobilisation corporelle** s'il est destiné à servir de façon durable à l'activité (plus d'un exercice), si l'entreprise en attend des avantages économiques futurs et si son coût est évaluable de façon fiable. Le coût d'entrée comprend le prix d'achat net de remises, les **frais directement attribuables** (transport, installation, montage, honoraires directement liés). La **formation** du personnel n'est pas incorporable.

> 🟢 **En clair :** trois questions. Le bien sert-il plus d'un an ? Va-t-il rapporter quelque chose à l'entreprise ? Connaît-on son prix ? Si oui, c'est une immobilisation. Son coût comprend le prix et les frais pour le mettre en service (livraison, installation), mais pas la formation des salariés.

**Tolérance administrative des 500 € HT** (BOFiP, BIC – Charges – immobilisations de faible valeur) : le petit matériel et outillage, le matériel et mobilier de bureau et les logiciels dont la **valeur unitaire HT n'excède pas 500 €** peuvent être comptabilisés en charges. Ne s'applique pas aux biens dont l'utilisation constitue l'objet même de l'activité, ni, selon l'administration, à un renouvellement complet d'un ensemble de mobilier (point d'appréciation — à vérifier au cas par cas).

> 🟢 **En clair :** un petit bien de bureau ou un petit outil qui coûte 500 € HT ou moins (prix d'un seul objet) peut aller directement en charge. Attention : cela ne marche pas si l'entreprise renouvelle tout son mobilier d'un coup, ni pour les biens qui sont le cœur de son activité.

| Dépense | Traitement |
|---|---|
| Bien durable > 500 € HT | Immobilisation (classe 2) + amortissement |
| Petit équipement ≤ 500 € HT unitaire | Charge possible (6063 / 6064) |
| Entretien, réparation qui maintient le bien en état | Charge (615x) |
| Dépense qui prolonge significativement la durée d'utilisation ou remplace un composant | Immobilisation |
| Abonnement (SaaS, maintenance, garantie) | Charge, avec **charge constatée d'avance** pour la part postérieure à la clôture |

---

## 10. Checklist de fin de module

- [ ] Je sais justifier une écriture par un principe comptable (et l'écrire dans une note de travail).
- [ ] Je connais les durées de conservation (10 ans C. com. / 6 ans LPF) et la règle de l'original électronique.
- [ ] Je sais ce que le PCG 2025 supprime (791/796/797) et ce qu'il déplace (amendes, dons → classe 65).
- [ ] Je contrôle une facture sur **toutes** ses mentions, y compris les 4 nouvelles (SIREN client, adresse de livraison, nature de l'opération, option débits).
- [ ] Je connais le calendrier : réception 01/09/2026 pour tous ; émission GE/ETI 01/09/2026, PME/TPE 01/09/2027.
- [ ] Je fais la différence entre facture rectificative et avoir, et je ne supprime jamais une facture.
- [ ] Je rapproche devis / BC / BL / facture avant tout « bon à payer ».
- [ ] Je lettre au fil de l'eau, je contre-passe les doublons, je rapproche les relevés fournisseurs.
- [ ] Je sais lire un FEC et repérer ses anomalies.
- [ ] Je contrôle l'OCR sur les points à risque (dates de clôture, multi-taux, avoirs, autoliquidation, seuil de 500 €, doublons).

## À retenir en 30 secondes

- Pas d'écriture sans pièce : une facture au nom de l'entreprise, pas un simple relevé de banque.
- Face à un cas inédit, choisissez l'écriture la plus fidèle : on n'anticipe pas un gain, on ne cache pas une perte.
- On garde tout 10 ans, et une facture électronique se garde sous sa forme électronique.
- Le premier chiffre du compte dit sa famille : 2 immobilisations, 4 tiers, 5 banque, 6 charges, 7 produits.
- On lettre au fil de l'eau : chaque facture reliée à son paiement.
- Une facture ne se supprime jamais : on la corrige par un avoir.
- L'OCR propose, vous contrôlez.
