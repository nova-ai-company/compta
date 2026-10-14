# M15 — Entretien GSF : les questions de comptabilité générale

*Module de préparation à l'entretien d'assistante comptable / aide-comptable au siège de GSF (Sophia Antipolis, Biot). Public : candidate avec **2 ans d'expérience**. Référentiel au 14/10/2026 (PCG = règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06 : plus de comptes 79, résultat exceptionnel restreint ; facturation électronique en vigueur depuis le 01/09/2026).*

**Objectif du module.** À la fin, vous savez répondre calmement aux questions techniques qu'un chef ou une cheffe comptable pose à une assistante comptable : « Comment passez-vous une facture d'achat ? », « C'est quoi un FNP ? », « Comment faites-vous un rapprochement bancaire ? ». Vous savez aussi réussir un petit test écrit (écritures + Excel).

> **Par où commencer ?** M15 est le **point de départ recommandé**. Il couvre les bases de la comptabilité générale, celles qu'on vous demandera à coup sûr. Faites-le **avant** M14, qui parle de GSF, de son organisation et des processus achats/ventes en plus de détail. Les passages notés « *pour aller plus loin* » sont facultatifs pour un premier passage.

> **Avertissement de méthode.** Les exemples utilisent **GSF Riviera SAS**, une filiale régionale **fictive** (SIREN fictif 999 100 206, capital 200 000 €), avec ses établissements de **Nice (ETB061)**, **Cannes (ETB062)** et Antibes. Les faits sur le groupe GSF viennent de la fiche de recherche de M14. Tout ce qui concerne l'organisation **interne** de GSF (logiciel, calendrier de clôture, plan de comptes exact) est une **hypothèse**, à présenter comme telle en entretien.

!!! abstract "En clair — ce module en 5 idées"
    1. **Le recruteur teste vos réflexes, pas votre mémoire.** Il veut voir que vous savez quel compte débiter, quel compte créditer, et pourquoi.
    2. **Répondez toujours en 3 temps.** La règle en une phrase, l'écriture, un exemple concret. Puis, si vous en connaissez un, le piège.
    3. **Le quotidien compte plus que le bilan.** Saisie des factures, lettrage, rapprochement bancaire, TVA du mois, notes de frais : c'est 80 % des questions.
    4. **La clôture, c'est « remettre chaque charge dans le bon mois ».** FNP, FAE, CCA, PCA : quatre écritures qui reviennent à chaque entretien.
    5. **Dire « je ne sais pas, mais voici comment je chercherais » est une bonne réponse.** Inventer est la pire.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Partie double | Chaque écriture a un débit et un crédit de même montant | Achat de 100 € : charge au débit, fournisseur au crédit |
    | PCG | Plan comptable général : la liste officielle des comptes | 401 = fournisseurs, 512 = banque |
    | Pièce justificative | Le document qui prouve l'opération | Facture, relevé bancaire, bulletin de paie |
    | Journal | Le « cahier » où l'on saisit un type d'opération | Journal des achats (AC), des ventes (VT), de banque (BQ) |
    | Lettrage | Relier une facture et son paiement dans un compte de tiers | La facture de 1 200 € et le virement de 1 200 € reçoivent la lettre « A » |
    | Rapprochement bancaire | Comparer le compte 512 et le relevé de la banque | Expliquer pourquoi il y a 2 500 € d'écart |
    | HT / TVA / TTC | Hors taxes, taxe, toutes taxes comprises | 1 000 € HT + 200 € TVA = 1 200 € TTC |
    | Avoir | Une « facture négative » qui annule ou réduit une facture | Remboursement d'un produit retourné |
    | FNP | Facture non parvenue : charge du mois, facture pas encore reçue | Intérim de septembre facturé en octobre |
    | FAE | Facture à établir : prestation faite, pas encore facturée | Vitrerie faite le 30/09, facturée le 05/10 |
    | CCA / PCA | Charge / produit constaté d'avance : concerne le mois ou l'exercice suivant | Assurance payée pour 12 mois |
    | Amortissement | Étaler le coût d'un matériel sur sa durée d'utilisation | Autolaveuse amortie sur 5 ans |
    | Balance | Le tableau de tous les comptes avec leurs totaux et soldes | Total débit = total crédit |
    | Grand livre | Le détail de toutes les écritures, compte par compte | Toutes les lignes du compte 401 |
    | FEC | Fichier des écritures comptables, à remettre au fisc en cas de contrôle | Un export du logiciel comptable |
    | ERP | Le grand logiciel de gestion de l'entreprise | SAP, Oracle, Sage X3, Cegid… |
    | PA | Plateforme agréée : le service qui transmet les factures électroniques | Les factures fournisseurs arrivent par la PA |

---

## Partie 1 — Ce que le recruteur teste vraiment

> 🟢 **En clair :** pour un poste d'assistante comptable, on ne vous demandera pas de faire une consolidation. On veut savoir si vous pouvez saisir juste, contrôler, et prévenir quand quelque chose cloche.

### 1.1 Le déroulé type

Le processus exact de GSF pour les postes comptables n'est pas connu (*à vérifier*). Les retours publics décrivent un processus rapide (environ une semaine) et jugé plutôt facile. Le schéma classique dans un grand groupe :

| Étape | Avec qui | Ce qu'on teste | Durée indicative |
|---|---|---|---|
| 1. Appel de qualification | RH ou cabinet | Disponibilité, salaire, motivation | 15 min |
| 2. Entretien RH | Chargé(e) de recrutement | Parcours, savoir-être, « pourquoi GSF ? » | 30 à 45 min |
| 3. Entretien technique | Chef(fe) comptable, parfois responsable comptable | **Questions de compta générale** (ce module) | 45 min à 1 h |
| 4. Test écrit (fréquent) | Seule, sur papier ou sur PC | 5 à 10 écritures + un petit exercice Excel | 30 min à 1 h |

> 💡 Réflexe senior : à l'entretien technique, la cheffe comptable se demande une seule chose : « Est-ce que je pourrai lui confier les factures fournisseurs dès la deuxième semaine, sans tout revérifier ? » Chaque réponse doit la rassurer sur ce point.

### 1.2 Ce qu'on regarde dans vos réponses

1. **La justesse** : bon compte, bon sens (débit ou crédit), bon montant.
2. **La logique** : vous savez expliquer *pourquoi*.
3. **Le réflexe de contrôle** : vous pensez à vérifier (la TVA, le doublon, le bon établissement).
4. **L'honnêteté** : vous dites ce que vous ne savez pas.
5. **Le concret** : vous donnez un exemple tiré de votre expérience.

### 1.3 La méthode pour répondre à une question technique

Répondez en **3 temps**, plus un bonus :

| Temps | Ce que vous dites | Exemple : « C'est quoi une FNP ? » |
|---|---|---|
| 1. Définition | La règle en une phrase | « Une charge du mois dont la facture n'est pas encore arrivée. » |
| 2. Écriture | Les comptes, débit puis crédit | « Je débite la charge et la TVA sur FNP, 44586, et je crédite 408. » |
| 3. Exemple GSF | Un cas concret de propreté | « Par exemple l'intérim de septembre pour l'établissement de Nice, facturé début octobre. » |
| Bonus : le piège | Ce qu'il ne faut pas oublier | « Et je l'extourne le 1er du mois suivant pour ne pas compter la charge deux fois. » |

Une réponse de 30 secondes suffit. Si la recruteuse veut plus, elle relancera.

### 1.4 Quand vous ne savez pas

Ne restez pas muette, n'inventez pas. Trois phrases utiles :

- « Je ne l'ai pas encore pratiqué, mais voici comment je raisonnerais : … »
- « Je ne suis pas sûre du numéro de compte exact, mais c'est un compte de charge de classe 6 ; je vérifierais dans votre plan de comptes. »
- « Dans ce cas, je demanderais à ma responsable avant de saisir, et je noterais la réponse pour la prochaine fois. »

> ⚠️ Erreur classique : donner un numéro de compte au hasard avec assurance. Une recruteuse pardonne « je vérifierais », elle ne pardonne pas une erreur affirmée.

---

## Partie 2 — Les principes de base et le PCG

> 🟢 **En clair :** c'est la grammaire de la comptabilité. Chaque opération s'écrit deux fois (débit et crédit), dans un journal, à partir d'une pièce. Les comptes sont rangés en 7 classes.

### 2.1 Les règles à connaître

**La partie double.** Toute écriture a au moins un débit et un crédit, et **total débit = total crédit**. Moyen mnémotechnique : *ce que je reçois* (une charge, un bien, de l'argent) va au **débit** ; *ce que je dois ou ce qui part* va au **crédit**.

**Les 7 classes du PCG :**

| Classe | Contenu | Exemples GSF Riviera | Va dans… |
|---|---|---|---|
| 1 | Capitaux, emprunts, provisions | 101 capital, 164 emprunt | Bilan (passif) |
| 2 | Immobilisations | 2154 autolaveuse, 2182 camionnette | Bilan (actif) |
| 3 | Stocks | 322 stock de produits d'entretien | Bilan (actif) |
| 4 | Tiers | 401 fournisseurs, 411 clients, 445 TVA, 421 salaires | Bilan |
| 5 | Financiers | 512 banque, 530 caisse | Bilan |
| 6 | Charges | 6022 produits d'entretien, 641 salaires | Compte de résultat |
| 7 | Produits | 706 prestations de services | Compte de résultat |

**Bilan et compte de résultat.** Le **bilan** est une photo à une date : ce que l'entreprise possède (actif) et ce qu'elle doit (passif). Le **compte de résultat** est le film de l'année : produits moins charges = résultat.

**Les principes comptables à citer** (Code de commerce et PCG) :

| Principe | En une phrase | Exemple |
|---|---|---|
| Prudence | On enregistre les pertes probables, pas les gains probables | On déprécie un client en difficulté |
| Indépendance des exercices | Chaque charge dans l'exercice (ou le mois) qu'elle concerne | FNP, CCA |
| Permanence des méthodes | On garde les mêmes méthodes d'une année sur l'autre | Même durée d'amortissement des autolaveuses |
| Coût historique | On enregistre au prix payé | Une autolaveuse reste à son prix d'achat |
| Non-compensation | On ne mélange pas une dette et une créance | Un client qui est aussi fournisseur : 411 et 401 séparés |
| Continuité d'exploitation | On suppose que l'entreprise continue | Base de l'amortissement |

**La pièce justificative.** Pas d'écriture sans pièce (facture, relevé, contrat, bulletin). Les livres comptables et les pièces se conservent **10 ans** (Code de commerce). Le fisc peut contrôler en principe sur 3 ans, mais les documents se gardent plus longtemps (*durées à vérifier selon les documents*).

**Les journaux usuels :** AC (achats), VT (ventes), BQ (banque, un par compte), CA (caisse), OD (opérations diverses : paie, clôture, TVA), AN (à-nouveaux).

**Le FEC.** Fichier de toutes les écritures de l'exercice, au format imposé par l'administration (CGI, livre des procédures fiscales). Il est remis en cas de contrôle fiscal. Conséquence pratique : chaque écriture doit avoir une date, un numéro de pièce et un libellé clair.

**Le lettrage.** Dans un compte de tiers (401, 411), on relie la facture et son règlement par une même lettre. Ce qui reste **non lettré** = ce qui reste à payer ou à encaisser.

### 2.2 Les écritures de base

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Apport en capital (création) | 512 Banque | 101 Capital | 200 000,00 € |
| Achat de produits d'entretien | 6022 + 44566 | 401 | 1 000,00 + 200,00 / 1 200,00 € |
| Paiement du fournisseur | 401 | 512 | 1 200,00 € |
| Facture de prestation au client | 411 | 706 + 44574 (TVA en attente) | 1 200,00 / 1 000,00 + 200,00 € |

### 2.3 Questions qu'on vous posera

1. **« Expliquez la partie double. »** — Chaque opération touche au moins deux comptes, un au débit, un au crédit, pour le même total. Exemple : un achat de 1 200 € TTC, c'est 1 000 € de charge et 200 € de TVA au débit, 1 200 € de dette fournisseur au crédit.
2. **« Quelle différence entre bilan et compte de résultat ? »** — Le bilan, c'est le patrimoine à une date ; le compte de résultat, c'est l'activité de l'année et le bénéfice ou la perte.
3. **« Un compte 401, il est normalement débiteur ou créditeur ? »** — Créditeur : c'est une dette. Un 401 débiteur veut dire qu'on a trop payé, payé en double, ou qu'un avoir n'est pas utilisé : à analyser.
4. **« À quoi sert le lettrage ? »** — À savoir ce qui reste dû, facture par facture. Sans lettrage, on peut payer deux fois ou oublier une facture.
5. **« Combien de temps garde-t-on les pièces ? »** — 10 ans pour les pièces comptables (Code de commerce).
6. **« C'est quoi le FEC ? »** — Le fichier de toutes les écritures, remis à l'administration fiscale lors d'un contrôle.
7. **« Qu'est-ce que le principe de prudence ? »** — Prendre en compte les pertes probables tout de suite, et les gains seulement quand ils sont réalisés.

> 💡 Réflexe senior : dans un groupe, le plan de comptes est commun à toutes les filiales (souvent sur 6 chiffres, ex. 706100). Dites : « J'appliquerai votre plan de comptes groupe ; les comptes que je cite sont ceux du PCG. »

> ⚠️ Erreur classique : citer le compte 791 « transfert de charges ». Il **n'existe plus** depuis le PCG applicable aux exercices ouverts à compter du 01/01/2025. Un remboursement réduit directement la charge concernée.

---

## Partie 3 — Achats et fournisseurs

> 🟢 **En clair :** c'est le cœur du poste. Une facture arrive, vous vérifiez qu'elle est juste, vous la saisissez sur la bonne société et le bon établissement, puis vous la payez à l'échéance.

### 3.1 Les règles à connaître

- **Contrôler avant de saisir :** destinataire (bonne société, SIREN), mentions obligatoires, calcul HT/TVA/TTC, taux de TVA, doublon, bon de commande et bon à payer.
- **Avoir :** il annule ou réduit une facture. Il se saisit à l'inverse de la facture et se lettre avec elle.
- **RRR (rabais, remises, ristournes)** : sur la facture → on saisit le **net** ; reçus plus tard par avoir → compte **609** (RRR obtenus).
- **Escompte** (réduction pour paiement rapide) : c'est un **produit financier**, compte **765**.
- **Acompte versé** : avance au fournisseur, compte **4091**, soldé à la réception de la facture.
- **Frais accessoires** (port, emballage) : ils suivent l'achat (ou compte 6241 transport sur achats selon le plan de l'entreprise). Pour une immobilisation, ils font partie de son coût.
- **Immobilisation ou charge ?** Un bien durable qui sert plus d'un an est une immobilisation. Par tolérance fiscale, le **petit matériel de moins de 500 € HT** peut aller en charge (6063) (*seuil à vérifier chaque année*).
- **Achat intracommunautaire** (fournisseur d'un autre pays de l'UE) : facture sans TVA ; GSF Riviera calcule elle-même la TVA, la **déclare et la déduit** en même temps.
- **Sous-traitance BTP** : quand GSF Riviera fait appel à un sous-traitant pour du nettoyage **lié à des travaux** (fin de chantier), le sous-traitant facture **sans TVA** et GSF Riviera l'autoliquide. Le nettoyage courant de bureaux reste en TVA normale.

### 3.2 Les écritures types (GSF Riviera, établissement de Nice ETB061)

**a) Facture de produits d'entretien : 1 250,00 € HT, TVA 20 %**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 6022 | Fournitures consommables — produits d'entretien [ETB061] | 1 250,00 € | |
| 44566 | TVA déductible sur ABS | 250,00 € | |
| 401 | Fournisseur | | 1 500,00 € |

**b) Avoir pour retour de marchandise : 150,00 € HT**

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 401 | Fournisseur | 180,00 € | |
| 6022 | Produits d'entretien | | 150,00 € |
| 44566 | TVA déductible | | 30,00 € |

**c) Remise de 10 % sur la facture : brut 2 000,00 € HT, net 1 800,00 € HT**

| Compte | Débit | Crédit |
|---|---|---|
| 6022 | 1 800,00 € | |
| 44566 | 360,00 € | |
| 401 | | 2 160,00 € |

On ne fait pas apparaître la remise : on saisit le net.

**d) Escompte de 2 % sur facture : 1 000,00 € HT, escompte 20,00 €, net financier 980,00 €, TVA 196,00 €**

| Compte | Débit | Crédit |
|---|---|---|
| 6022 | 1 000,00 € | |
| 44566 | 196,00 € | |
| 765 Escomptes obtenus | | 20,00 € |
| 401 | | 1 176,00 € |
| **Total** | **1 196,00 €** | **1 196,00 €** |

La TVA se calcule sur le montant **après escompte** (980,00 × 20 % = 196,00 €).

**e) Acompte versé, puis facture (livraison de biens)**

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Acompte versé à la commande | 4091 Fournisseurs — avances versées | 512 | 2 000,00 € |
| Facture à la livraison (5 000,00 HT) | 6022 5 000,00 + 44566 1 000,00 | 401 | 6 000,00 € |
| Imputation de l'acompte | 401 | 4091 | 2 000,00 € |
| Paiement du solde | 401 | 512 | 4 000,00 € |

**f) Immobilisation : autolaveuse 4 200,00 € HT pour Cannes (ETB062)**

| Compte | Débit | Crédit |
|---|---|---|
| 2154 Matériel industriel — matériel de nettoyage | 4 200,00 € | |
| 44562 TVA déductible sur immobilisations | 840,00 € | |
| 404 Fournisseurs d'immobilisations | | 5 040,00 € |

À l'inverse, un aspirateur dorsal à 389,00 € HT va en **6063** (petit équipement), TVA en 44566.

**g) Achat intracommunautaire de biens : 3 000,00 € HT (fournisseur allemand)**

| Compte | Débit | Crédit |
|---|---|---|
| 6022 | 3 000,00 € | |
| 401 | | 3 000,00 € |
| 445662 TVA déductible intracommunautaire | 600,00 € | |
| 4452 TVA due intracommunautaire | | 600,00 € |

Effet net sur la TVA à payer : zéro. Mais les deux lignes doivent figurer sur la CA3.

**h) Sous-traitance de nettoyage de fin de chantier : 4 000,00 € HT (autoliquidation)**

| Compte | Débit | Crédit |
|---|---|---|
| 611 Sous-traitance générale | 4 000,00 € | |
| 401 | | 4 000,00 € |
| 445661 TVA déductible autoliquidée (sous-compte interne) | 800,00 € | |
| 445711 TVA due autoliquidée (sous-compte interne) | | 800,00 € |

### 3.3 Questions qu'on vous posera

1. **« Que vérifiez-vous sur une facture fournisseur avant de la saisir ? »** — Qu'elle est adressée à la bonne société, que les mentions obligatoires sont là, que les calculs et le taux de TVA sont justes, qu'elle n'a pas déjà été saisie, et qu'elle correspond à la commande et à la livraison, avec un bon à payer.
2. **« Différence entre un rabais, une remise et une ristourne ? »** — Rabais : pour un défaut de qualité. Remise : pour une quantité. Ristourne : calculée sur le chiffre d'affaires d'une période. Les trois sont commerciaux ; l'escompte, lui, est financier (765).
3. **« Une autolaveuse à 4 200 € HT, vous la passez où ? »** — En immobilisation, 2154, car elle sert plusieurs années et dépasse 500 € HT. Puis on l'amortit.
4. **« Comment saisissez-vous un avoir ? »** — À l'inverse de la facture : 401 au débit, charge et TVA au crédit. Puis je le lettre avec la facture pour ne payer que la différence.
5. **« Un fournisseur italien vous facture sans TVA, c'est normal ? »** — Oui, si c'est un achat intracommunautaire et que nos deux numéros de TVA sont sur la facture. C'est nous qui autoliquidons la TVA.
6. **« Le compte 401 d'un fournisseur est débiteur, que faites-vous ? »** — J'analyse : paiement en double, avoir non utilisé, acompte. Selon le cas, je demande un remboursement ou j'impute l'avoir sur la prochaine facture.
7. **« Que faites-vous si une facture arrive sans bon de commande ? »** — Je ne la paie pas. Je cherche le demandeur (souvent le chef d'établissement) pour obtenir sa validation.

> 💡 Réflexe senior : avant de saisir, regardez toujours le **code établissement**. Une facture de 1 250 € imputée à Cannes au lieu de Nice fausse la marge des deux chefs d'établissement.

> ⚠️ Erreur classique : payer une facture reçue deux fois (une par e-mail, une par la plateforme). Contrôlez le numéro de facture et le montant dans le compte fournisseur avant toute saisie.

---

## Partie 4 — Ventes et clients

> 🟢 **En clair :** GSF Riviera facture ses clients chaque mois (forfait de nettoyage) puis encaisse. Votre rôle : facture juste, encaissement bien lettré, et alerte quand un client ne paie pas.

### 4.1 Les règles à connaître

- **Prestations de services** (le nettoyage) : la TVA devient due **à l'encaissement**, sauf option pour les débits. En attendant, de nombreux groupes la placent dans un **sous-compte de TVA « en attente »** (ici **44574**, sous-compte interne), puis la basculent en 44571 quand le client paie.
- **Avoir client** : annule ou réduit une facture. Une réduction de prix (pénalité contractuelle qui réduit le prix, geste commercial) va en **709** (RRR accordés, sous-compte prestations de services 7096).
- **Acompte reçu** : compte **4191**. Pour une prestation de services, la TVA est due dès l'encaissement de l'acompte.
- **Client douteux** : quand un client risque de ne pas payer (retards répétés, redressement judiciaire), on transfère la créance en **416**, puis on la **déprécie** sur la base **HT** (6817 / 491).
- **Créance irrécouvrable** : perte définitive (liquidation judiciaire, par exemple). On passe la perte en **654**, on récupère la TVA, et on reprend la dépréciation (491 / 7817).
- **Retard de paiement** : entre professionnels, les **pénalités de retard** sont dues de plein droit (Code de commerce), plus une **indemnité forfaitaire de 40 €** pour frais de recouvrement. Pas de TVA sur ces sommes.

### 4.2 Les écritures types

**a) Facture du forfait mensuel : 5 000,00 € HT (TVA sur les encaissements)**

| Compte | Débit | Crédit |
|---|---|---|
| 411 Client | 6 000,00 € | |
| 706 Prestations de services [ETB061] | | 5 000,00 € |
| 44574 TVA collectée en attente | | 1 000,00 € |

**b) Encaissement du client**

| Compte | Débit | Crédit |
|---|---|---|
| 512 Banque | 6 000,00 € | |
| 411 Client | | 6 000,00 € |
| 44574 TVA collectée en attente | 1 000,00 € | |
| 44571 TVA collectée | | 1 000,00 € |

**c) Avoir pour pénalité contractuelle réduisant le prix : 300,00 € HT (facture pas encore encaissée)**

| Compte | Débit | Crédit |
|---|---|---|
| 7096 RRR accordés — prestations | 300,00 € | |
| 44574 TVA collectée en attente | 60,00 € | |
| 411 Client | | 360,00 € |

**d) Acompte reçu sur une remise en état : 3 000,00 € HT**

| Compte | Débit | Crédit |
|---|---|---|
| 512 | 3 600,00 € | |
| 4191 Clients — avances reçues | | 3 000,00 € |
| 44571 TVA collectée | | 600,00 € |

**e) Client douteux : facture de 2 400,00 € TTC (2 000,00 € HT), risque de perte 50 %**

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Transfert en douteux | 416 Clients douteux | 411 | 2 400,00 € |
| Dépréciation (50 % du HT) | 6817 Dotations aux dépréciations des actifs circulants | 491 Dépréciation des comptes clients | 1 000,00 € |

**f) L'année suivante, le client est liquidé : la créance est perdue**

| Compte | Débit | Crédit |
|---|---|---|
| 654 Pertes sur créances irrécouvrables | 2 000,00 € | |
| 44574 TVA collectée en attente | 400,00 € | |
| 416 Clients douteux | | 2 400,00 € |
| 491 Dépréciation des comptes clients | 1 000,00 € | |
| 7817 Reprises sur dépréciations des actifs circulants | | 1 000,00 € |

Ici la facture n'a jamais été encaissée : avec la TVA sur les encaissements, la TVA n'a jamais été due, on solde simplement le compte « en attente ». Si la TVA avait déjà été versée (option débits), on diminuerait 44571, avec une facture rectificative.

**g) Pénalités de retard facturées au client : 130,00 € + indemnité forfaitaire 40,00 €**

| Compte | Débit | Crédit |
|---|---|---|
| 411 | 170,00 € | |
| 763 Revenus des créances commerciales | | 130,00 € |
| 758 Produits divers de gestion courante (*subdivision selon la nomenclature 2025 du PCG*) | | 40,00 € |

### 4.3 Questions qu'on vous posera

1. **« Quand la TVA sur une prestation de nettoyage est-elle due ? »** — À l'encaissement, sauf si l'entreprise a opté pour les débits ; dans ce cas, à la facturation.
2. **« Un client ne paie pas depuis 6 mois, que faites-vous ? »** — Je relance (mail, téléphone, lettre recommandée) en lien avec l'établissement. À la clôture, je le passe en 416 et je propose une dépréciation sur le HT.
3. **« Pourquoi déprécie-t-on le HT et pas le TTC ? »** — Parce que la TVA sera récupérée si la créance est perdue. La vraie perte, c'est le HT.
4. **« Différence entre dépréciation et perte ? »** — La dépréciation constate un risque (6817 / 491). La perte constate une créance définitivement perdue (654).
5. **« Que doit-on facturer à un client en retard ? »** — Des pénalités de retard au taux prévu dans les conditions de paiement, et l'indemnité forfaitaire de 40 €, sans TVA.
6. **« Comment comptabilisez-vous un acompte client ? »** — En 4191. Pour une prestation de services, la TVA est due dès l'encaissement de l'acompte.

> 💡 Réflexe senior : à chaque fin de mois, comparez le solde de 44574 (TVA en attente) à la TVA contenue dans les factures clients non encaissées. Les deux doivent être égaux.

> ⚠️ Erreur classique : passer la perte sur un client en charge exceptionnelle (67). Depuis le PCG 2025, l'exceptionnel est réservé aux événements majeurs et inhabituels : une créance perdue reste en **654**.

---

## Partie 5 — La TVA

> 🟢 **En clair :** l'entreprise collecte la TVA sur ses ventes, récupère celle de ses achats, et verse la différence à l'État chaque mois (déclaration CA3). Si elle a plus récupéré que collecté, elle a un crédit.

### 5.1 Les règles à connaître

**Les taux :** 20 % (taux normal, le nettoyage), 10 %, 5,5 %, 2,1 %.

**Exigibilité (le moment où la TVA est due) :**

| Opération | TVA collectée due… |
|---|---|
| Vente de biens | À la **livraison** |
| Prestation de services | À l'**encaissement** (sauf option pour les débits) |
| Acompte sur prestation | À l'encaissement de l'acompte |
| Acquisition intracommunautaire | À la livraison (au plus tard le 15 du mois suivant) |

**Côté achats :** la TVA est déductible quand elle est devenue exigible chez le fournisseur, et si la facture est conforme. Pour un service payé à un fournisseur sous le régime des encaissements, vous ne déduisez qu'**après paiement**.

**Déclaration :** GSF Riviera est au **réel normal**, **CA3 mensuelle**.

**TVA non déductible (les plus fréquentes) :**

| Dépense | Règle |
|---|---|
| Véhicule de tourisme (achat, location, entretien) | TVA non déductible ; un véhicule utilitaire, oui |
| Carburant d'un véhicule de tourisme | Déductible à 80 % (gazole et essence) ; 100 % pour un utilitaire (*à vérifier chaque année*) |
| Cadeaux à des tiers | Non déductible sauf objets de faible valeur : **73 € TTC** par bénéficiaire et par an (*valeur à vérifier chaque année*) |
| Logement (hôtel) du personnel et des dirigeants | Non déductible |
| Transport de personnes (train, avion, taxi) | Non déductible en principe |
| Facture non conforme ou au nom d'une autre personne | Non déductible |

### 5.2 Les écritures types

**a) Liquidation de la CA3 d'octobre (TVA à payer)**

TVA collectée 48 000,00 € ; TVA déductible sur ABS 30 000,00 € ; TVA déductible sur immobilisations 2 000,00 € ; TVA à payer = 48 000,00 − 30 000,00 − 2 000,00 = **16 000,00 €**.

| Compte | Débit | Crédit |
|---|---|---|
| 44571 TVA collectée | 48 000,00 € | |
| 44566 TVA déductible sur ABS | | 30 000,00 € |
| 44562 TVA déductible sur immobilisations | | 2 000,00 € |
| 44551 TVA à décaisser | | 16 000,00 € |

Paiement : 44551 au débit / 512 au crédit, 16 000,00 €.

**b) Crédit de TVA : collectée 10 000,00 €, déductible 14 000,00 €**

| Compte | Débit | Crédit |
|---|---|---|
| 44571 | 10 000,00 € | |
| 44567 Crédit de TVA à reporter | 4 000,00 € | |
| 44566 | | 14 000,00 € |

Le crédit s'impute sur la CA3 suivante, ou fait l'objet d'une demande de remboursement.

**c) Hôtel lors d'une mission : 110,00 € TTC (TVA 10,00 €)**

| Compte | Débit | Crédit |
|---|---|---|
| 6256 Missions | 110,00 € | |
| 421 (ou 467 / sous-compte « notes de frais ») | | 110,00 € |

Toute la somme va en charge : la TVA sur le logement du personnel n'est pas récupérable.

### 5.3 Questions qu'on vous posera

1. **« Comment calculez-vous la TVA à payer ? »** — TVA collectée exigible du mois moins TVA déductible du mois, plus ou moins les régularisations et le crédit antérieur.
2. **« Différence entre 44566 et 44562 ? »** — 44566 pour les achats de biens et services courants ; 44562 pour les immobilisations. Ils sont sur des lignes différentes de la CA3.
3. **« Qu'est-ce qu'un crédit de TVA ? »** — Plus de TVA déductible que collectée. On le reporte (44567) ou on demande le remboursement.
4. **« Peut-on récupérer la TVA sur une voiture de fonction ? »** — Non, pas sur un véhicule de tourisme. Oui sur une camionnette utilitaire.
5. **« Un cadeau client à 90 € TTC, TVA récupérable ? »** — Non, il dépasse le seuil de 73 € TTC par bénéficiaire et par an (*à vérifier chaque année*).
6. **« Comment contrôlez-vous votre CA3 ? »** — Je rapproche la TVA collectée des comptes 706, la TVA déductible du journal des achats, et je vérifie que les comptes 4457 et 4456 sont soldés après liquidation.

> 💡 Réflexe senior : après chaque liquidation, les comptes 44571, 44566 et 44562 doivent être à **zéro** (sauf TVA en attente et TVA sur FNP/FAE). Un solde qui reste est une anomalie à expliquer.

> ⚠️ Erreur classique : déduire la TVA d'une facture adressée à une autre société du groupe. La TVA n'est déductible que pour l'entreprise qui figure sur la facture.

---

## Partie 6 — La trésorerie

> 🟢 **En clair :** la banque, la caisse, les emprunts. La question presque certaine : « Comment faites-vous un rapprochement bancaire ? ». Préparez-la à fond.

### 6.1 Le rapprochement bancaire, pas à pas

**Le principe.** Le compte 512 (votre comptabilité) et le relevé de la banque doivent dire la même chose. Ils diffèrent à cause d'opérations enregistrées d'un seul côté. Attention au sens : votre compte 512 débiteur = de l'argent en banque ; sur le relevé, ce même solde apparaît **créditeur** (vu de la banque, c'est sa dette envers vous).

**La méthode en 4 étapes :**

1. Pointer chaque ligne du relevé avec les lignes du 512.
2. Lister ce qui n'est pointé que d'un côté.
3. Corriger la comptabilité pour ce qui est **en banque mais pas en compta** (frais, virements reçus, prélèvements).
4. Justifier ce qui est **en compta mais pas en banque** (chèques pas encore encaissés, remises pas encore créditées) : ce sont des décalages normaux, qui disparaîtront le mois suivant.

**Exemple GSF Riviera au 31/10/2026 :**

- Solde du 512 : **18 450,00 € débiteur**.
- Solde du relevé : **21 780,00 € créditeur**.
- Chèque n° 4512 émis à un fournisseur, pas encore débité par la banque : 2 500,00 €.
- Remise de chèques clients du 31/10, pas encore créditée : 1 200,00 €.
- Frais bancaires sur le relevé, pas en compta : 36,00 €.
- Virement d'un client sur le relevé, pas en compta : 2 066,00 €.

| Côté comptabilité | Montant | Côté banque | Montant |
|---|---|---|---|
| Solde du 512 | 18 450,00 € | Solde du relevé | 21 780,00 € |
| − Frais bancaires | − 36,00 € | − Chèque fournisseur non débité | − 2 500,00 € |
| + Virement client reçu | + 2 066,00 € | + Remise de chèques non créditée | + 1 200,00 € |
| **Solde rectifié** | **20 480,00 €** | **Solde rectifié** | **20 480,00 €** |

Les deux soldes rectifiés sont égaux : le rapprochement est bon. On passe en comptabilité uniquement les écritures de la colonne de gauche :

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Frais bancaires | 627 Services bancaires | 512 | 36,00 € |
| Virement client | 512 | 411 | 2 066,00 € |

### 6.2 Les autres règles de trésorerie

- **Caisse (530)** : jamais créditrice (on ne peut pas avoir moins de zéro euro en caisse).
- **Virements internes (580)** : pour passer de la caisse à la banque, ou d'une banque à l'autre, sans compter deux fois. Chaque journal passe par 580, qui doit revenir à zéro.
- **Prélèvements SEPA** (énergie, télécoms, loyers) : 401 au débit / 512 au crédit, à la date du prélèvement, une fois la facture saisie.
- **Effets de commerce / LCR** : le client accepte une lettre de change. Créance en 413 (effets à recevoir), dette en 403 (effets à payer).
- **Emprunt** : le capital reçu va en 164 ; à chaque échéance, le capital remboursé diminue 164 et les intérêts sont une charge financière (6611).
- **ICNE** (intérêts courus non échus) : à la clôture, les intérêts déjà courus mais pas encore payés sont une charge de l'exercice (6611 / 1688).

### 6.3 Les écritures types

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Dépôt d'espèces en banque (1) | 580 Virements internes | 530 Caisse | 500,00 € |
| Dépôt d'espèces en banque (2) | 512 | 580 | 500,00 € |
| Réception d'un emprunt le 01/10/2026 (60 000,00 € à 3 %, 5 ans, remboursement annuel de 12 000,00 € le 30/09) | 512 | 164 Emprunts | 60 000,00 € |
| ICNE au 31/12/2026 : 60 000,00 × 3 % × 3/12 | 6611 Intérêts des emprunts | 1688 Intérêts courus | 450,00 € |
| Extourne des ICNE au 01/01/2027 | 1688 | 6611 | 450,00 € |
| Échéance du 30/09/2027 : capital | 164 | 512 | 12 000,00 € |
| Échéance du 30/09/2027 : intérêts (60 000,00 × 3 %) | 6611 | 512 | 1 800,00 € |
| Client accepte une LCR | 413 Effets à recevoir | 411 | 3 000,00 € |
| Remise de la LCR à l'encaissement | 5113 Effets à l'encaissement | 413 | 3 000,00 € |
| Encaissement de la LCR | 512 | 5113 | 3 000,00 € |

### 6.4 Questions qu'on vous posera

1. **« Comment faites-vous un rapprochement bancaire ? »** — Je pointe relevé et 512, je liste les écarts, je passe en compta ce que la banque a enregistré et pas moi (frais, virements), et je justifie les décalages (chèques non encaissés). Les deux soldes rectifiés doivent être égaux.
2. **« Un chèque émis il y a 6 mois n'est toujours pas encaissé, que faites-vous ? »** — Je contacte le fournisseur. Un chèque n'est plus encaissable au-delà d'un an et 8 jours : il faut l'annuler et régler autrement.
3. **« À quoi sert le compte 580 ? »** — À enregistrer un mouvement entre deux comptes de trésorerie sans le compter deux fois.
4. **« Que se passe-t-il à l'échéance d'un emprunt ? »** — Le capital diminue la dette (164), les intérêts sont une charge (6611).
5. **« C'est quoi les ICNE ? »** — Les intérêts courus depuis la dernière échéance jusqu'à la clôture, pas encore payés. On les constate en charge pour respecter l'indépendance des exercices.
6. **« La caisse peut-elle être créditrice ? »** — Non, jamais. Si c'est le cas, une recette a été oubliée ou une dépense saisie deux fois.

> 💡 Réflexe senior : un rapprochement se fait **chaque mois**, et les écarts de plus de deux mois doivent être expliqués par écrit. Un vieux chèque non encaissé, c'est souvent une dette que le fournisseur réclamera plus tard.

> ⚠️ Erreur classique : comptabiliser le chèque fournisseur non encaissé une deuxième fois pour « faire coller » le rapprochement. Le décalage est normal : il ne se corrige pas dans la comptabilité.

---

## Partie 7 — Les immobilisations

> 🟢 **En clair :** une autolaveuse sert 5 ans ; on ne passe pas tout son prix en charge la première année. On l'enregistre à l'actif, puis on en passe une part en charge chaque année : c'est l'amortissement.

### 7.1 Les règles à connaître

- **Coût d'acquisition** = prix d'achat net de remises + frais nécessaires à la mise en service (livraison, installation). La TVA récupérable n'en fait pas partie.
- **Amortissement linéaire** : la même charge chaque année. Il commence à la **date de mise en service**, au prorata (en jours, souvent sur une base de 360 jours).
- **Amortissement dégressif** (fiscal, *pour aller plus loin*) : plus fort au début. Il commence le **1er jour du mois** d'acquisition. Taux = taux linéaire × coefficient (1,25 pour 3 ou 4 ans, 1,75 pour 5 ou 6 ans, 2,25 au-delà de 6 ans).
- **Composants** : si une pièce importante a une durée différente (batteries d'une autolaveuse, 3 ans), on l'amortit séparément.
- **Cession** : on constate la vente en produit (775) et la sortie de la valeur nette comptable en charge (675). La différence est la plus ou moins-value. Les cessions restent en 675/775 dans le PCG 2025.
- **Dépréciation** : si la valeur réelle d'un bien tombe sous sa valeur nette comptable (matériel cassé, obsolète), on la constate (6816 / 29x).

### 7.2 Calcul : autolaveuse de 12 000,00 € HT, mise en service le 15/03/2026, 5 ans

**Linéaire.** Taux 20 %. Du 15/03 au 31/12/2026 = 9 mois et 15 jours = 285 jours (base 360).
Dotation 2026 = 12 000,00 × 20 % × 285/360 = **1 900,00 €**. Puis 2 400,00 € par an.

| Année | Dotation | Cumul | Valeur nette comptable |
|---|---|---|---|
| 2026 | 1 900,00 € | 1 900,00 € | 10 100,00 € |
| 2027 | 2 400,00 € | 4 300,00 € | 7 700,00 € |
| 2028 | 2 400,00 € | 6 700,00 € | 5 300,00 € |
| 2029 | 2 400,00 € | 9 100,00 € | 2 900,00 € |
| 2030 | 2 400,00 € | 11 500,00 € | 500,00 € |
| 2031 | 500,00 € | 12 000,00 € | 0,00 € |

**Dégressif (*pour aller plus loin*).** Taux 20 % × 1,75 = 35 %. Point de départ : 01/03/2026, soit 10 mois.
2026 = 12 000,00 × 35 % × 10/12 = **3 500,00 €** ; 2027 = (12 000,00 − 3 500,00) × 35 % = **2 975,00 €**.

Écriture de dotation (linéaire, 2026) :

| Compte | Débit | Crédit |
|---|---|---|
| 6811 Dotations aux amortissements des immobilisations | 1 900,00 € | |
| 28154 Amortissements du matériel industriel | | 1 900,00 € |

### 7.3 Cession d'une camionnette

Camionnette (utilitaire) achetée 20 000,00 € HT le 01/01/2023, amortie en linéaire sur 5 ans (4 000,00 € par an), vendue 9 000,00 € HT le 30/06/2026.

- Amortissements au 31/12/2025 : 3 × 4 000,00 = 12 000,00 €.
- Dotation complémentaire 2026 (6 mois) : 4 000,00 × 6/12 = 2 000,00 €. Cumul : 14 000,00 €.
- Valeur nette comptable : 20 000,00 − 14 000,00 = 6 000,00 €. Plus-value : 9 000,00 − 6 000,00 = **3 000,00 €**.

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Dotation complémentaire | 6811 | 28182 | 2 000,00 € |
| Vente (TVA 20 %) | 462 Créances sur cessions d'immobilisations : 10 800,00 | 775 Produits des cessions : 9 000,00 ; 44571 : 1 800,00 | 10 800,00 € |
| Sortie du bien | 28182 : 14 000,00 ; 675 Valeurs comptables des éléments cédés : 6 000,00 | 2182 Matériel de transport : 20 000,00 | 20 000,00 € |

### 7.4 Questions qu'on vous posera

1. **« Qu'est-ce qu'un amortissement ? »** — La constatation de l'usure d'un bien, en étalant son coût sur sa durée d'utilisation.
2. **« Quand commence l'amortissement linéaire ? »** — À la date de mise en service, au prorata.
3. **« Qu'est-ce qui entre dans le coût d'une immobilisation ? »** — Le prix net de remises et les frais pour la mettre en état de marche (livraison, installation). Pas la TVA récupérable.
4. **« Comment comptabilisez-vous une cession ? »** — Trois temps : dotation jusqu'à la date de vente, vente en 775, sortie de la valeur nette en 675 avec annulation de l'immobilisation et des amortissements.
5. **« Une monobrosse à 450 € HT ? »** — Sous 500 € HT, on peut la passer en charge, compte 6063, selon la politique du groupe.
6. **« C'est quoi l'approche par composants ? »** — Amortir séparément une pièce importante qui a une durée différente, par exemple les batteries d'une autolaveuse.

> 💡 Réflexe senior : quand un matériel est mis au rebut sur un chantier, prévenez la comptabilité des immobilisations. Sinon, il reste à l'actif et continue d'être amorti alors qu'il n'existe plus.

> ⚠️ Erreur classique : oublier la dotation de l'année de cession, ou passer la vente d'un bien en 707 ou 706. La vente d'une immobilisation va en **775**.

---

## Partie 8 — La paie (côté comptabilité)

> 🟢 **En clair :** vous ne faites pas la paie, mais vous la comptabilisez et vous la contrôlez. Le salaire brut est une charge ; ce qu'on retient au salarié est versé aux organismes ; le reste est le net payé au salarié.

### 8.1 Les règles à connaître

| Compte | Ce qu'il contient |
|---|---|
| 641 | Salaires bruts (charge) |
| 645 | Charges sociales patronales (charge) |
| 421 | Net à payer aux salariés (dette) |
| 425 | Avances et acomptes versés aux salariés |
| 431 | Sécurité sociale (URSSAF) : parts salariale et patronale |
| 437 | Autres organismes (retraite complémentaire, mutuelle, prévoyance) |
| 4421 | Prélèvement à la source de l'impôt sur le revenu, reversé à l'État |
| 6412 / 4282 | Congés payés : charge / dette provisionnée |
| 645 / 4382 | Charges sociales sur congés payés |
| 625 | Déplacements, missions, réceptions (notes de frais) |

Rappel PCG 2025 : les **IJSS** perçues en cas de subrogation réduisent directement le 641 (4387 / 641), **jamais** de compte 791.

### 8.2 L'écriture de paie type (un salarié, montants simplifiés)

On retient : brut 2 000,00 € ; cotisations salariales URSSAF 180,00 €, retraite 160,00 €, mutuelle/prévoyance 30,00 € ; prélèvement à la source 40,00 € ; acompte déjà versé 300,00 € ; charges patronales URSSAF 500,00 €, retraite 240,00 €, mutuelle/prévoyance 50,00 € (*montants pédagogiques, taux réels à vérifier chaque année*).

Net à payer = 2 000,00 − 180,00 − 160,00 − 30,00 − 40,00 − 300,00 = **1 290,00 €**.

| Compte | Intitulé | Débit | Crédit |
|---|---|---|---|
| 641 | Rémunérations du personnel | 2 000,00 € | |
| 645 | Charges de sécurité sociale et de prévoyance | 790,00 € | |
| 431 | URSSAF (180,00 + 500,00) | | 680,00 € |
| 437 | Autres organismes (160,00 + 30,00 + 240,00 + 50,00) | | 480,00 € |
| 4421 | Prélèvement à la source | | 40,00 € |
| 425 | Acompte déjà versé | | 300,00 € |
| 421 | Net à payer | | 1 290,00 € |
| **Total** | | **2 790,00 €** | **2 790,00 €** |

Le versement de l'acompte, plus tôt dans le mois, avait été passé : 425 au débit / 512 au crédit, 300,00 €.

### 8.3 Congés payés et notes de frais

**Provision congés payés à la clôture** : congés acquis non pris 3 000,00 € ; charges sociales estimées à 42 % (*taux pédagogique*) = 1 260,00 €.

| Compte | Débit | Crédit |
|---|---|---|
| 6412 Congés payés | 3 000,00 € | |
| 4282 Dettes provisionnées pour congés à payer | | 3 000,00 € |
| 645 Charges sociales | 1 260,00 € | |
| 4382 Charges sociales sur congés à payer | | 1 260,00 € |

**Note de frais d'un chef d'équipe** : restaurant en mission 66,00 € TTC (60,00 € HT + TVA 10 % 6,00 €) et hôtel 110,00 € TTC (TVA non récupérable).

| Compte | Débit | Crédit |
|---|---|---|
| 6256 Missions (60,00 + 110,00) | 170,00 € | |
| 44566 TVA déductible (restaurant) | 6,00 € | |
| 421 (ou sous-compte « notes de frais ») | | 176,00 € |

### 8.4 Questions qu'on vous posera

1. **« Décrivez une écriture de paie. »** — 641 et 645 au débit ; 431, 437, 4421, 425 et 421 au crédit. Total débit = brut + charges patronales.
2. **« Quelle différence entre 421 et 425 ? »** — 421 : ce qu'on doit au salarié. 425 : ce qu'on lui a déjà avancé ; on le déduit de la paie.
3. **« Comment contrôlez-vous la paie en comptabilité ? »** — Je rapproche le journal de paie des comptes 641/645, je vérifie que 421 est soldé après virement des salaires, et que 431/437 correspondent aux déclarations (DSN).
4. **« C'est quoi la provision pour congés payés ? »** — La dette envers les salariés pour les congés acquis et pas encore pris, plus les charges sociales dessus.
5. **« Que vérifiez-vous sur une note de frais ? »** — Les justificatifs, la validation du responsable, le motif professionnel, et la TVA récupérable (oui pour un repas en mission avec facture, non pour l'hôtel).
6. **« Comment comptabilisez-vous les IJSS en subrogation ? »** — 4387 au débit, 641 au crédit à la réception de l'attestation ; puis 512 / 4387 à l'encaissement.

> 💡 Réflexe senior : dans la propreté, beaucoup de salariés, de temps partiels et d'arrêts de travail. Un compte 421 qui ne revient pas à zéro chaque mois cache souvent un salaire non versé ou un virement rejeté : à surveiller.

> ⚠️ Erreur classique : récupérer la TVA sur une nuit d'hôtel. Le logement du personnel n'ouvre pas droit à déduction.

---

## Partie 9 — Clôture et inventaire

> 🟢 **En clair :** à la fin du mois ou de l'année, on remet chaque charge et chaque produit dans la bonne période. Quatre mots-clés : FNP, FAE, CCA, PCA. Puis on extourne (on annule) le 1er jour de la période suivante.

### 9.1 Les règles à connaître

| Situation | Ce qu'on fait | Comptes |
|---|---|---|
| Charge du mois, facture pas reçue | FNP | 6x + 44586 / 408 |
| Prestation faite, pas facturée | FAE | 418 / 706 + 44587 |
| Charge payée pour une période future | CCA | 486 / 6x |
| Produit facturé pour une période future | PCA | 706 / 487 |
| Avoir attendu d'un fournisseur | AAR (avoir à recevoir) | 4098 / 609 + 44586 |
| Avoir à faire à un client | AAE (avoir à établir) | 7096 + 44587 / 4198 |
| Risque probable (litige, prud'hommes) | Provision pour risques | 6815 / 151 |
| Stock de produits en fin de période | Variation de stock | 6032 / 322 (puis 322 / 6032) |

**L'extourne** : le 1er jour de la période suivante, on passe l'écriture inverse. Quand la vraie facture arrive, on la saisit normalement : la charge n'est comptée qu'une fois.

### 9.2 Les écritures types (clôture du 31/12/2026)

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| FNP : intérim de décembre 2 000,00 € HT | 621 Personnel extérieur 2 000,00 + 44586 TVA sur factures non parvenues 400,00 | 408 Fournisseurs — factures non parvenues | 2 400,00 € |
| FAE : vitrerie faite le 30/12, 1 500,00 € HT | 418 Clients — factures à établir | 706 1 500,00 + 44587 TVA sur factures à établir 300,00 | 1 800,00 € |
| CCA : assurance de 3 600,00 € payée le 01/10/2026 pour un an → 9 mois sur 2027 | 486 Charges constatées d'avance | 616 Primes d'assurance | 2 700,00 € |
| PCA : forfait de janvier 2027 facturé en décembre, 5 000,00 € HT | 706 | 487 Produits constatés d'avance | 5 000,00 € |
| AAR : ristourne de fin d'année attendue, 500,00 € HT | 4098 Avoirs à recevoir 600,00 | 609 RRR obtenus 500,00 + 44586 100,00 | 600,00 € |
| AAE : avoir promis à un client, 400,00 € HT | 7096 400,00 + 44587 80,00 | 4198 Avoirs à établir | 480,00 € |
| Provision pour litige prud'homal | 6815 Dotations aux provisions d'exploitation | 151 Provisions pour risques | 8 000,00 € |
| Annulation du stock initial | 6032 Variation des stocks | 322 Stock de produits d'entretien | 4 000,00 € |
| Constatation du stock final | 322 | 6032 | 5 200,00 € |
| Extourne de la FNP au 01/01/2027 | 408 2 400,00 | 621 2 000,00 + 44586 400,00 | 2 400,00 € |

Calcul de la CCA : 3 600,00 × 9/12 = 2 700,00 €. Variation de stock : 4 000,00 − 5 200,00 = − 1 200,00 € (le stock a augmenté, la consommation diminue d'autant).

> Le compte 713 « variation des stocks de production » concerne les entreprises qui fabriquent. Pour des produits d'entretien achetés, c'est **6032**.

### 9.3 Pour aller plus loin : écarts de conversion et impôt sur les sociétés

**Écart de conversion.** Une dette en dollars se réévalue au cours de clôture. Facture fournisseur de 6 600,00 USD, enregistrée au cours de 1 € = 1,10 USD, soit 6 000,00 €. Au 31/12, cours 1 € = 1,0560 USD : la dette vaut 6 250,00 €. Perte latente de 250,00 €.

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Écart de conversion | 476 Différences de conversion — actif | 401 | 250,00 € |
| Provision pour perte de change | 6865 Dotations aux provisions financières | 1515 Provisions pour pertes de change | 250,00 € |

**Impôt sur les sociétés.** Les acomptes versés en cours d'année vont au débit de 444. À la clôture, on constate l'impôt de l'année. Exemple : IS 2026 de 50 000,00 € (25 % × 200 000,00 €), acomptes versés 48 000,00 €.

| Opération | Débit | Crédit | Montant |
|---|---|---|---|
| Acomptes versés (total de l'année) | 444 État — impôt sur les bénéfices | 512 | 48 000,00 € |
| IS de l'exercice | 695 Impôts sur les bénéfices | 444 | 50 000,00 € |
| Solde à payer en 2027 | 444 | 512 | 2 000,00 € |

Dans un groupe comme GSF, l'IS est souvent traité par la société tête (intégration fiscale probable, *à vérifier*) : l'assistante comptable n'en a en général que la préparation des pièces.

### 9.4 Questions qu'on vous posera

1. **« C'est quoi une FNP, et comment la passez-vous ? »** — Une charge de la période dont la facture n'est pas arrivée. 6x et 44586 au débit, 408 au crédit. Extourne le 1er jour de la période suivante.
2. **« Comment trouvez-vous les FNP ? »** — Commandes réceptionnées non facturées, contrats récurrents (loyers, intérim, énergie), relevés d'heures validés, questions aux chefs d'établissement.
3. **« Différence entre CCA et FNP ? »** — FNP : charge de la période, facture pas reçue. CCA : facture reçue, mais elle concerne la période suivante.
4. **« Pourquoi extourne-t-on ? »** — Pour ne pas compter la charge deux fois quand la vraie facture arrive.
5. **« Un salarié attaque l'entreprise aux prud'hommes, que fait-on à la clôture ? »** — Une provision pour risques (6815 / 151) du montant probable, d'après l'avocat ou le service juridique.
6. **« Comment comptabilise-t-on les stocks ? »** — On annule le stock initial et on constate le stock final, par le compte 6032 pour des fournitures achetées.
7. **« Que faites-vous en clôture mensuelle ? »** — FNP, FAE, CCA/PCA récurrentes, rapprochements bancaires, lettrage, justification des comptes de tiers et de TVA, provision congés payés.

> 💡 Réflexe senior : gardez un **fichier de suivi des FNP** (fournisseur, montant, justification, établissement). Le mois suivant, vérifiez que chaque FNP extournée a bien été remplacée par une vraie facture.

> ⚠️ Erreur classique : oublier l'extourne. La charge apparaît deux fois : une fois par la FNP, une fois par la facture.

---

## Partie 10 — États financiers et contrôle des comptes

> 🟢 **En clair :** à la fin, il faut prouver que chaque solde est juste. On regarde la balance, on ouvre le grand livre, et on justifie chaque compte avec une pièce ou un tableau.

### 10.1 Les règles à connaître

- **Balance** : total des débits = total des crédits. Elle sert à repérer les soldes anormaux.
- **Grand livre** : le détail d'un compte. On l'ouvre pour comprendre un solde.
- **Justification de compte** : pour chaque compte de bilan, un tableau qui explique le solde (liste des factures non lettrées, relevé de la banque, déclaration de TVA, état des dettes sociales).
- **Compte d'attente 471** : on y met provisoirement une opération qu'on ne sait pas encore affecter (virement sans référence). Il doit être **vidé** avant la clôture.
- **Soldes anormaux** à repérer : 401 débiteur, 411 créditeur, 530 créditeur, 421 non soldé, 4456/4457 non soldés après la CA3.
- **Cohérence TVA / chiffre d'affaires** : chiffre d'affaires du mois × 20 % doit être proche de la TVA facturée (collectée + en attente). Un écart s'explique (avoirs, opérations exonérées, autoliquidation).

### 10.2 Les SIG et l'EBE (les bases)

Les soldes intermédiaires de gestion découpent le résultat en étapes. Exemple simplifié pour GSF Riviera (montants fictifs) :

| Poste | Montant |
|---|---|
| Chiffre d'affaires (706) | 1 000 000,00 € |
| − Achats consommés (produits d'entretien) | − 120 000,00 € |
| − Charges externes (intérim, sous-traitance, loyers) | − 180 000,00 € |
| **= Valeur ajoutée** | **700 000,00 €** |
| − Impôts et taxes | − 20 000,00 € |
| − Charges de personnel | − 620 000,00 € |
| **= EBE (excédent brut d'exploitation)** | **60 000,00 €** |

Dans la propreté, les charges de personnel sont de loin la plus grosse charge : l'EBE dépend surtout de la maîtrise des heures travaillées.

### 10.3 Écriture type : régularisation d'un compte d'attente

Un virement de 1 440,00 € reçu sans référence a été passé en 471. On découvre qu'il s'agit d'un client de l'établissement de Cannes.

| Compte | Débit | Crédit |
|---|---|---|
| 471 Compte d'attente | 1 440,00 € | |
| 411 Client [ETB062] | | 1 440,00 € |

### 10.4 Questions qu'on vous posera

1. **« Comment justifiez-vous un compte fournisseur ? »** — Par la liste des factures non lettrées, chacune vérifiable avec sa pièce. Je vérifie qu'il n'y a pas de vieux soldes ni de soldes débiteurs inexpliqués.
2. **« Que regardez-vous en premier sur une balance ? »** — Qu'elle est équilibrée, puis les soldes anormaux et les comptes d'attente.
3. **« C'est quoi le compte 471 ? »** — Un compte d'attente, provisoire. Il doit être à zéro à la clôture.
4. **« Qu'est-ce que l'EBE ? »** — Ce que l'activité courante dégage avant amortissements, frais financiers et impôt. C'est un indicateur suivi par les actionnaires.
5. **« Comment contrôlez-vous la cohérence de la TVA ? »** — Je compare le chiffre d'affaires × taux à la TVA facturée, et la TVA déclarée aux soldes des comptes.

> 💡 Réflexe senior : un dossier de justification bien tenu (un onglet par compte, la pièce en lien) fait gagner des jours lors de la venue des commissaires aux comptes.

> ⚠️ Erreur classique : laisser des sommes en 471 « en attendant ». À la clôture, un compte d'attente non soldé est une anomalie que les auditeurs relèvent.

---

## Partie 11 — Les outils : Excel, ERP, facture électronique

> 🟢 **En clair :** on vous demandera presque toujours votre niveau sur Excel. Quatre fonctions suffisent pour impressionner : RECHERCHEV (ou RECHERCHEX), SOMME.SI.ENS, le tableau croisé dynamique, et NB.SI pour trouver les doublons.

### 11.1 Excel : les fonctions à savoir expliquer

| Besoin | Fonction (Excel en français) | Exemple |
|---|---|---|
| Retrouver le nom d'un fournisseur à partir de son code | RECHERCHEV | `=RECHERCHEV(A2;Fournisseurs!A:C;3;FAUX)` |
| Même chose, plus souple | RECHERCHEX | `=RECHERCHEX(A2;Fournisseurs!A:A;Fournisseurs!C:C;"Introuvable")` |
| Total des factures d'un établissement sur un compte | SOMME.SI.ENS | `=SOMME.SI.ENS(D:D;B:B;"ETB061";C:C;"6022")` |
| Repérer les doublons (même fournisseur + même n° de facture) | NB.SI.ENS | `=NB.SI.ENS(A:A;A2;E:E;E2)>1` renvoie VRAI si doublon |
| Compter les factures non lettrées | NB.SI | `=NB.SI(F:F;"")` |
| Synthèse par fournisseur ou par mois | Tableau croisé dynamique (TCD) | Lignes : fournisseur ; colonnes : mois ; valeurs : somme des montants |

Le `FAUX` de RECHERCHEV demande une correspondance **exacte** : sans lui, Excel peut renvoyer un mauvais fournisseur.

### 11.2 ERP et dématérialisation

Le logiciel de GSF n'est pas connu publiquement (*question à poser*). Les grands groupes utilisent SAP, Oracle, Sage X3, Cegid, Microsoft Dynamics… La logique est la même partout : fiche tiers, saisie ou validation de facture, workflow de bon à payer, proposition de paiement, lettrage, éditions (balance âgée, grand livre).

### 11.3 Facture électronique (2026)

- Depuis le **01/09/2026**, toutes les entreprises doivent pouvoir **recevoir** des factures électroniques via une **plateforme agréée (PA)**.
- Les **grandes entreprises et ETI** doivent aussi les **émettre** depuis le 01/09/2026 (GSF est une grande entreprise). Les PME et TPE émettront à partir du **01/09/2027**.
- Nouvelles mentions : **SIREN du client**, adresse de livraison si différente, **nature de l'opération** (biens, services ou mixte), option pour les débits le cas échéant.
- Pour vous : moins de saisie manuelle, plus de **contrôle** (rejets, statuts de la facture, rapprochement avec les commandes).

### 11.4 Questions qu'on vous posera

1. **« Quel est votre niveau sur Excel ? »** — Donnez des faits : « J'utilise RECHERCHEV et SOMME.SI.ENS chaque semaine, je fais des TCD pour mes balances âgées, et je repère les doublons avec NB.SI.ENS. »
2. **« Comment trouveriez-vous des factures en double dans un export de 5 000 lignes ? »** — Colonne avec NB.SI.ENS sur fournisseur + numéro de facture, filtre sur VRAI, puis vérification des pièces.
3. **« Vous connaissez la facture électronique ? »** — Oui : réception obligatoire depuis le 01/09/2026 via une plateforme agréée ; émission obligatoire pour les grandes entreprises comme GSF depuis la même date.
4. **« Quels logiciels avez-vous utilisés ? »** — Citez les vôtres, puis : « Je ne connais pas encore le vôtre, mais la logique est la même, et je me forme vite. »

> 💡 Réflexe senior : au test Excel, nommez vos onglets, figez les en-têtes, et ajoutez une ligne de contrôle (total = total de la balance). On note autant la méthode que le résultat.

> ⚠️ Erreur classique : dire « Excel, je maîtrise » sans exemple. La recruteuse demandera aussitôt « Expliquez-moi un TCD ».

---

## Partie 12 — Les 30 écritures à savoir par cœur

> 🟢 **En clair :** si vous ne révisez qu'une page, c'est celle-ci. Cachez les colonnes Débit et Crédit et récitez.

| N° | Opération | Débit | Crédit |
|---|---|---|---|
| 1 | Facture d'achat de produits | 6022 + 44566 | 401 |
| 2 | Avoir fournisseur | 401 | 6022 (ou 609) + 44566 |
| 3 | Paiement fournisseur | 401 | 512 |
| 4 | Facture avec escompte obtenu | 6022 + 44566 (sur le net) | 765 + 401 |
| 5 | Acompte versé | 4091 | 512 |
| 6 | Achat d'immobilisation | 2xx + 44562 | 404 |
| 7 | Achat intracommunautaire | 6xx ; 445662 | 401 ; 4452 |
| 8 | Sous-traitance BTP autoliquidée | 611 ; 445661 | 401 ; 445711 |
| 9 | Facture client (services, encaissements) | 411 | 706 + 44574 |
| 10 | Encaissement client | 512 ; 44574 | 411 ; 44571 |
| 11 | Avoir client (réduction de prix) | 7096 + TVA | 411 |
| 12 | Acompte reçu (services) | 512 | 4191 + 44571 |
| 13 | Client douteux | 416 | 411 |
| 14 | Dépréciation client (sur HT) | 6817 | 491 |
| 15 | Créance irrécouvrable | 654 + TVA | 416 |
| 16 | Reprise de dépréciation | 491 | 7817 |
| 17 | Liquidation de TVA à payer | 44571 | 44566 + 44562 + 44551 |
| 18 | Crédit de TVA | 44571 + 44567 | 44566 |
| 19 | Frais bancaires | 627 | 512 |
| 20 | Virement interne | 580 puis 512 | 530 puis 580 |
| 21 | Réception d'un emprunt | 512 | 164 |
| 22 | Échéance d'emprunt | 164 + 6611 | 512 |
| 23 | ICNE | 6611 | 1688 |
| 24 | Dotation aux amortissements | 6811 | 28xx |
| 25 | Cession d'immobilisation | 462 ; 28xx + 675 | 775 + 44571 ; 2xx |
| 26 | Paie | 641 + 645 | 431 + 437 + 4421 + 425 + 421 |
| 27 | Provision congés payés | 6412 ; 645 | 4282 ; 4382 |
| 28 | FNP | 6xx + 44586 | 408 |
| 29 | FAE | 418 | 706 + 44587 |
| 30 | CCA / PCA | 486 / 706 | 6xx / 487 |

---

## Partie 13 — Les 10 pièges qui font perdre des points

> 🟢 **En clair :** ce sont les erreurs que les recruteurs entendent le plus souvent. Les éviter suffit à se démarquer.

| N° | Le piège | La bonne réponse |
|---|---|---|
| 1 | Citer un compte 791 (transfert de charges) | Supprimé depuis le PCG 2025 : on diminue la charge |
| 2 | Mettre une pénalité ou une créance perdue en 67 | Exceptionnel restreint : 658 pour une pénalité, 654 pour une créance perdue |
| 3 | Déprécier un client sur le TTC | Sur le **HT** |
| 4 | Oublier l'extourne des FNP | Charge comptée deux fois |
| 5 | Déduire la TVA d'une nuit d'hôtel ou d'une voiture de tourisme | Non déductible |
| 6 | Dire que la TVA du nettoyage est due à la facturation | À l'**encaissement**, sauf option pour les débits |
| 7 | Passer une autolaveuse en charge | Immobilisation (2154) au-delà de 500 € HT |
| 8 | « Corriger » un chèque non encaissé dans le rapprochement | Décalage normal, on ne passe rien |
| 9 | Laisser des sommes en 471 | Compte vidé avant la clôture |
| 10 | Affirmer un numéro de compte ou un taux au hasard | « Je vérifierais dans votre plan de comptes » |

---

## Partie 14 — Checklist de révision

**Les bases**

- [ ] Je sais expliquer la partie double avec un exemple chiffré.
- [ ] Je connais les 7 classes du PCG et je sais ce qui va au bilan ou au compte de résultat.
- [ ] Je cite 4 principes comptables avec un exemple.

**Le quotidien**

- [ ] Je sais passer une facture, un avoir, un acompte et un paiement fournisseur.
- [ ] Je sais lettrer et expliquer un 401 débiteur.
- [ ] Je sais faire un rapprochement bancaire de tête sur un exemple à 4 écarts.
- [ ] Je sais calculer une CA3 simple et expliquer encaissements / débits.
- [ ] Je sais comptabiliser une note de frais et dire quelle TVA est récupérable.
- [ ] Je sais lire une écriture de paie.

**La clôture**

- [ ] Je sais passer et extourner une FNP, une FAE, une CCA et une PCA.
- [ ] Je sais calculer une dotation linéaire au prorata.
- [ ] Je sais passer une cession d'immobilisation en 3 écritures.
- [ ] Je sais déprécier un client douteux sur le HT.

**Le test et l'oral**

- [ ] J'ai refait les 30 écritures en cachant les colonnes, sans erreur.
- [ ] Je sais écrire RECHERCHEV, SOMME.SI.ENS et NB.SI.ENS sans les chercher.
- [ ] J'ai préparé 2 exemples tirés de mon expérience (une erreur trouvée, une clôture tenue).
- [ ] Je sais répondre en 3 temps : définition, écriture, exemple.

## À retenir en 30 secondes

- Répondez en 3 temps : la règle, l'écriture, un exemple GSF ; ajoutez le piège si vous le connaissez.
- Avant de saisir : bonne société, bon établissement, facture conforme, pas de doublon.
- Nettoyage = TVA à 20 %, due à l'encaissement sauf option pour les débits.
- Rapprochement bancaire : on corrige la compta pour ce que la banque a vu, on justifie les décalages.
- Clôture : FNP, FAE, CCA, PCA, puis extourne le 1er jour suivant.
- Client douteux : 416, dépréciation sur le HT ; perte définitive en 654.
- Plus de comptes 79, exceptionnel réservé aux événements majeurs ; les cessions restent en 675/775.
- Si vous ne savez pas : dites comment vous chercheriez, n'inventez jamais.
