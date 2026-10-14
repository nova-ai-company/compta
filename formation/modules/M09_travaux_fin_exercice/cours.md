# M09 — Les travaux d'inventaire et le cut-off

> **Objectif du module.** À la fin de ce module, vous savez construire seule le dossier d'inventaire d'un client : rattacher chaque produit et chaque charge au bon exercice, constater les provisions et dépréciations justifiées (et refuser celles qui ne le sont pas), traiter les opérations en devises, analyser les événements postérieurs à la clôture, corriger une erreur d'un exercice antérieur et enchaîner les écritures d'inventaire dans un ordre qui ne vous oblige pas à tout refaire.
>
> **Prérequis :** M01 à M08 (saisie courante, TVA, immobilisations, stocks, paie).
> **Référentiel :** PCG (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06, exercices ouverts depuis le 01/01/2025) — **pas de comptes de transfert de charges (79)**, résultat exceptionnel restreint aux événements majeurs et inhabituels (les cessions d'immobilisations restent en 675/775).

!!! abstract "En clair — ce module en 5 idées"
    1. **Chaque année ne garde que ce qui la concerne.** Une charge ou une vente appartient à l'année où le travail a été fait ou la marchandise livrée. La date de la facture ou du paiement ne compte pas. Exemple : C11 Transports Leroy, le transporteur, reçoit en janvier la facture d'une réparation de camion faite en décembre → c'est une charge de décembre.
    2. **On remet chaque montant dans la bonne année avec des écritures de régularisation.** Facture pas encore reçue, dépense payée d'avance, salaire dû mais pas encore versé… On passe l'écriture à la clôture, puis on l'annule le 1er jour de l'année suivante. Exemple : C04 Le Petit Zinc, le restaurant, clôture au 30/06 : ce qu'il a payé d'avance pour juillet n'est pas une charge de l'année close.
    3. **Une provision, c'est mettre de côté pour un risque réel, probable et chiffrable.** Jamais pour « lisser » le résultat. Exemple : C03 Garage Martin, le garage, est attaqué aux prud'hommes par un ancien salarié.
    4. **Une dépréciation, c'est reconnaître qu'un bien vaut moins que dans les comptes.** Un client qui ne paiera sans doute pas, un stock invendable, des titres qui ont perdu de la valeur. Pour les achats en dollars (C19 Asia Trading, l'importateur de luminaires), on recalcule aussi les dettes au cours du jour de clôture.
    5. **Ce qui se passe après la clôture compte aussi.** Si l'événement éclaire une situation qui existait déjà à la clôture, on corrige les comptes. Sinon, on l'explique dans l'annexe. Exemple : C24 Menuiserie Bois & Création, la menuiserie en difficulté.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Clôture | Le dernier jour de l'année comptable du client. On « arrête » les comptes à cette date. | 31/12 pour C11, 30/06 pour C04 |
    | Exercice | L'année comptable, souvent 12 mois, pas toujours du 1er janvier au 31 décembre. | Du 01/07 au 30/06 pour C04 Le Petit Zinc |
    | Cut-off | Le tri, autour de la clôture, entre ce qui appartient à l'année qui se termine et ce qui appartient à la suivante. | Une livraison du 30/12 facturée le 05/01 |
    | Fait générateur | Le moment où la chose se passe vraiment : livraison, travail terminé, service rendu. | Le jour où le camion est réparé |
    | FNP (facture non parvenue) | Une dépense de l'année dont la facture n'est pas encore arrivée à la clôture. | Électricité de décembre facturée en janvier |
    | FAE (facture à établir) | Une vente de l'année que le client n'a pas encore facturée à la clôture. | Un transport fait le 31/12, facturé en janvier |
    | Extourne | L'annulation, le 1er jour de l'année suivante, d'une écriture passée à la clôture, pour ne pas compter deux fois. | On annule la FNP le 01/01, puis on saisit la vraie facture |
    | CCA (charge constatée d'avance) | Une dépense déjà payée ou facturée, mais qui concerne en partie l'année suivante. | Une assurance payée pour 12 mois à cheval sur deux années |
    | PCA (produit constaté d'avance) | Une vente déjà facturée, mais dont le service sera rendu l'année suivante. | Un abonnement de salle de sport vendu chez C21 FitClub |
    | Charge à payer | Une somme due à la clôture mais pas encore payée, sans facture à attendre. | Les congés payés acquis par les salariés |
    | Provision pour risque | Une somme mise de côté pour une dette probable dont le montant ou la date n'est pas encore sûr. | Un procès aux prud'hommes chez C03 Garage Martin |
    | Dépréciation | La constatation qu'un bien vaut moins que sa valeur dans les comptes. | Une facture client impayée depuis un an |
    | Écart de conversion | La différence de valeur d'une dette ou d'une créance en devises entre le jour de l'achat et le jour de la clôture. | Une facture en dollars chez C19 Asia Trading |
    | Événement postérieur | Un fait qui arrive entre la clôture et le jour où les comptes sont arrêtés. | Un client qui fait faillite en février |
    | Revue analytique | La comparaison des chiffres d'une année sur l'autre pour repérer ce qui est bizarre. | Les frais de carburant baissent de 30 % sans raison |

---

## 1. Le principe : l'indépendance des exercices

> 🟢 **En clair :** une charge ou un produit appartient à l'année où la chose s'est réellement passée (livraison, travail fait), pas à l'année de la facture ou du paiement. C'est la base de tout le travail de clôture : si vous comprenez cette idée, le reste du module en découle.

Le Code de commerce (art. L. 123-21 et règles d'évaluation du PCG) et le CGI (art. 38, 2 — notion de « créances acquises » et de « dettes certaines dans leur principe et leur montant ») imposent la même chose : **chaque exercice supporte les charges et produits qui le concernent, et seulement eux**, indépendamment de leur date de paiement ou de facturation.

> 🟢 **En clair :** la loi comptable et la loi fiscale disent la même chose. Chaque année ne porte que ses propres charges et ses propres produits. Peu importe quand la facture arrive ou quand on paie.

Les trois questions à se poser devant chaque pièce autour de la clôture :

1. **Le fait générateur** (livraison du bien, exécution de la prestation, service fait, obligation née) est-il **avant ou après** la date de clôture ?
2. Le document (facture, avoir) est-il arrivé **avant ou après** ?
3. Si fait générateur et document sont de part et d'autre de la clôture → **régularisation**.

| Situation à la clôture | Charges | Produits |
|---|---|---|
| Service fait / livré, document pas encore reçu ou émis | **Facture non parvenue** (408) / **charge à payer** (428x, 438x, 448x, 4686) | **Facture à établir** (418) / **produit à recevoir** (4287, 4387, 4487, 4687) |
| Document reçu ou émis, service pas encore fait | **Charge constatée d'avance** (486) | **Produit constaté d'avance** (487) |
| Réduction de prix acquise mais document pas encore établi | **Avoir à recevoir** (4098) | **Avoir à établir** (4198) |

> 💡 Réflexe senior : le cut-off ne se fait pas « de mémoire ». Il se fait **à partir des pièces du mois suivant la clôture** (factures d'achat et de vente datées de janvier pour une clôture au 31/12, relevés bancaires, avis d'échéance, bulletins de paie) et du **dernier bon de livraison / dernier bon d'expédition** de l'exercice. Demandez systématiquement au client l'export de son journal d'achats et de ventes du mois N+1 et ses derniers numéros de BL.

---

## 2. Les régularisations de charges et de produits

> 🟢 **En clair :** voici les écritures qui « remettent chaque montant dans la bonne année » : factures pas encore reçues ou pas encore envoyées, dépenses payées d'avance, salaires et taxes dus mais pas encore payés, intérêts qui courent. Exemple : un loyer de janvier payé en décembre n'est pas une charge de décembre.

### 2.1 Factures non parvenues (FNP) et factures à établir (FAE)

On enregistre **le HT en charge/produit** et **la TVA dans un compte d'attente** : la TVA n'est ni déductible ni collectée tant que la facture n'existe pas (ou, pour les prestations de services, tant que le prix n'est pas payé, sauf option pour les débits).

> 🟢 **En clair :** quand la facture n'existe pas encore, on enregistre le montant hors taxe en charge (ou en vente) de l'année. La TVA est mise « en attente » dans un compte spécial : sans facture, on ne peut ni la récupérer ni la déclarer.

| Écriture | Débit | Crédit |
|---|---|---|
| **FNP** au 31/12 | 6xx (HT) + 44586 *TVA sur factures non parvenues* | 4081 *Fournisseurs – factures non parvenues* (TTC) |
| **FAE** au 31/12 | 4181 *Clients – factures à établir* (TTC) | 7xx (HT) + 44587 *TVA sur factures à établir* |
| **Avoir à recevoir** | 4098 *Fournisseurs – avoirs à recevoir* (TTC) | 6xx ou 609 (HT) + 44586 |
| **Avoir à établir** | 7xx ou 709 (HT) + 44587 | 4198 *Clients – avoirs à établir* (TTC) |

Au **1er jour de l'exercice suivant**, ces écritures sont **contrepassées** (extournées) ; la facture réelle sera saisie normalement à sa réception.

> ⚠️ Erreur classique : oublier l'extourne au 1er jour de l'exercice suivant. Résultat : la charge est comptée deux fois (une fois en FNP N, une fois à la réception de la facture en N+1), et le 4081 traîne pendant des années au bilan. **Au début de chaque révision, contrôlez que les 408, 418, 486, 487, 4686, 4687 d'ouverture ont bien été soldés.**

> ⚠️ Erreur classique : passer la FNP **TTC en charge** ou déduire la TVA de la FNP sur la CA3 de décembre. La TVA ne se déduit que sur facture (art. 271 CGI).

**Avoirs : réduction de prix ou indemnité ?** Une remise, un rabais ou une ristourne de fin d'année (RFA) est une **réduction du prix** → avoir avec TVA. En revanche, une **indemnité** qui répare un préjudice (marchandise abîmée pendant un transport, pénalité contractuelle de retard…) est **hors champ de la TVA** → charge à payer (4686) ou produit à recevoir (4687) sans TVA.

### 2.2 Charges et produits constatés d'avance (CCA / PCA)

| Écriture | Débit | Crédit |
|---|---|---|
| **CCA** | 486 *Charges constatées d'avance* | 6xx (**HT**) |
| **PCA** | 7xx (**HT**) | 487 *Produits constatés d'avance* |

- Calcul **au prorata temporis** (en mois si les périodes commencent au 1er du mois, en jours sinon) ou **à l'avancement** (prestation partiellement réalisée, séances non consommées…).
- **Jamais de TVA** dans une CCA/PCA : la TVA a été traitée à la facture.
- Les achats de **biens stockables** non consommés ne sont pas des CCA : ce sont des **stocks** (variation de stock).
- Les **abonnements payés d'avance** (SaaS, salles de sport, presse) génèrent des PCA ; ventilez dans l'annexe la part à plus d'un an.

> 💡 Réflexe senior : chez un client à abonnements (TechNova, FitClub), ne recalculez pas les PCA à la main ligne à ligne : demandez l'**état des produits différés** (deferred revenue) au logiciel de facturation, puis **testez-le** par sondage sur 5 à 10 contrats (date de début, durée, montant HT, résiliations, suspensions). Le logiciel ne connaît pas les avenants ni les gestes commerciaux.

### 2.3 Charges à payer sociales et fiscales

| Nature | Compte de dette | Exemple |
|---|---|---|
| Rémunérations dues au personnel | **4282** dettes provisionnées pour congés à payer ; **4286** autres charges à payer | Congés payés acquis non pris, prime décidée en N payée en N+1, heures supplémentaires de décembre payées en janvier |
| Charges sociales correspondantes | **4382** charges sociales sur congés à payer ; **4386** autres charges à payer | Cotisations patronales sur ces sommes |
| Impôts et taxes | **4486** *État – charges à payer* | C3S, taxe d'apprentissage solde, taxe sur les véhicules, CFE si non encore réglée, CVAE selon l'année (vérifier le calendrier de suppression) |
| Divers | **4686** *Divers – charges à payer* | Indemnité due à un client, note de frais du mois de décembre non remboursée |

**Produits à recevoir** : 4287 (personnel), 4387 (organismes sociaux : IJSS à recevoir…), **4487** (*État – produits à recevoir* : remboursement partiel de TICPE, crédit d'impôt non encore déclaré…), **4687** (*Divers – produits à recevoir* : indemnité d'assurance acquise…).

> ⚠️ Erreur classique : comptabiliser le remboursement d'IJSS ou d'assurance en « transfert de charges » (791). **Ce compte n'existe plus** depuis le PCG 2025 : le remboursement vient **en diminution de la charge** concernée (ex. 641/645 pour les IJSS subrogées) ou en produit par nature.

### 2.4 Intérêts courus

- **Sur emprunts** : intérêts de la période écoulée entre la dernière échéance et la clôture → **D 661 / C 1688** *Intérêts courus sur emprunts*.
- **Sur placements** (DAT, comptes à terme) : **D 2768** ou **5088** *Intérêts courus* / **C 7xx** (produits financiers).
- Calcul au jour près : intérêts de la prochaine échéance × (jours courus jusqu'à la clôture / jours de la période).

---

## 3. Les provisions pour risques et charges (comptes 151x)

> 🟢 **En clair :** une provision, c'est une dette probable dont on ne connaît pas encore exactement le montant ou la date. Vous en passerez surtout pour des litiges (prud'hommes, client mécontent). Le point clé : on ne provisionne que des risques réels, prouvés par des documents, jamais « au cas où ».

### 3.1 Les trois conditions cumulatives (PCG, règles relatives aux passifs)

Une provision est un **passif dont l'échéance ou le montant est incertain**. On ne la constate que si, **à la clôture** :

1. il existe une **obligation** envers un tiers (légale, réglementaire, contractuelle ou **implicite** — pratique passée, engagement public) **résultant d'un événement passé** ;
2. il est **probable ou certain** qu'elle provoquera une **sortie de ressources sans contrepartie au moins équivalente** ;
3. son montant peut être **estimé de manière fiable**.

Si l'une des conditions manque → **pas de provision**, éventuellement une information en annexe (**passif éventuel**).

| Provision | Compte | Fait générateur à la clôture |
|---|---|---|
| Litiges (prud'homal, commercial) | **1511** | Assignation, saisine, réclamation écrite ; ou événement fautif connu |
| Garanties données aux clients | **1512** | Ventes réalisées sous garantie (estimation statistique) |
| Pertes de change | **1515** | Écart de conversion actif non couvert |
| Amendes et pénalités | **1516** | Infraction commise, contrôle en cours (redressement probable) |
| Pertes sur contrats (perte à terminaison) | **1517** | Contrat signé dont les coûts estimés dépassent les produits |
| Autres risques | **1518** | Caution donnée, risque filiale… (toujours **nommé** et documenté) |
| Pensions et obligations similaires (IDR) | **153** | Méthode préférentielle (sinon engagement hors bilan) |
| Restructuration | **154** | Plan **décidé ET annoncé** avant la clôture aux personnes concernées |
| Impôts | **155** | Redressement probable |
| Gros entretien / grandes révisions | **1572** | Programme pluriannuel imposé par la loi, un règlement ou la pratique constante |

**Écritures :** dotation **D 6815** (exploitation) / **6865** (financière) / **687x** (exceptionnelle, désormais rare) → **C 151x**. Reprise : **D 151x** → **C 7815 / 7865 / 787x**. Une provision **utilisée** est reprise et la charge réelle est comptabilisée dans son compte par nature ; une provision **devenue sans objet** est reprise.

> 💡 Réflexe senior : la provision se mesure à la **meilleure estimation** de la sortie de ressources (le scénario le plus probable, ou la moyenne pondérée s'il existe une population nombreuse comme les garanties). Pour un litige, **exigez une lettre de l'avocat** qui donne la probabilité et la fourchette. Pas de lettre = pas de documentation = point de révision ouvert.

**Ce qui n'est JAMAIS une provision :**
- les **pertes d'exploitation futures** (« l'an prochain sera mauvais ») ;
- les **dépenses futures liées à l'activité** (formation, recrutement, déménagement non contractualisé, achat d'un équipement) ;
- les « **risques divers** » non identifiés destinés à **lisser le résultat** : c'est une **inexactitude volontaire des comptes**, contraire au principe d'image fidèle (art. L. 123-14 C. com.), non déductible fiscalement et engageant la responsabilité de l'expert-comptable ;
- les **honoraires futurs** d'avocat pour la suite d'une procédure (prestation non encore rendue) — pratique divergente, à documenter si vous les incluez.

### 3.2 Traitement fiscal (art. 39, 1-5° CGI)

Une provision comptable est **déductible** si : elle est destinée à faire face à des pertes ou charges **nettement précisées**, que des **événements en cours** rendent **probables**, elle est **effectivement constatée en comptabilité** et figure sur le **relevé des provisions** (tableau 2056 / 2033-D). La charge provisionnée doit elle-même être déductible.

> 🟢 **En clair :** pour que l'impôt accepte la provision, il faut un risque précis et probable, une écriture passée dans les comptes, et une ligne dans le tableau des provisions de la liasse. Sinon, on rajoute la provision au résultat fiscal.

| Provision | Fiscalement |
|---|---|
| Litiges, garanties (si statistiques fiables), pénalités contractuelles, perte à terminaison, gros entretien (programme précis) | Déductible |
| **Amendes et pénalités** fiscales ou pénales (art. 39, 2 CGI), contraventions | **Non déductible** (la charge ne l'est pas) |
| **Indemnités de départ à la retraite** (153) | **Non déductible** (art. 39, 1-5°) — déduite au paiement |
| **Perte de change** (1515) | **Non déductible** (l'écart de conversion actif est déjà déduit, art. 38, 4 CGI) |
| **Dépréciation des titres de participation** relevant du régime des plus-values à long terme exonérées | **Non déductible** |
| Provision « pour risques divers » non justifiée | **Non déductible** + risque de majoration pour manquement délibéré |

Les provisions non déductibles sont **réintégrées** extra-comptablement (2058-A / 2033-B) l'année de la dotation et **déduites** l'année de leur reprise.

---

## 4. Les dépréciations d'actifs

> 🟢 **En clair :** une dépréciation constate qu'un bien de l'entreprise vaut moins que sa valeur dans les comptes : une créance client qui ne sera sans doute pas payée, un stock démodé, des titres qui ont perdu de la valeur. On ne touche pas au compte du bien lui-même : on enregistre la perte probable dans un compte à côté.

Une dépréciation constate une **perte de valeur probable et non irréversible** d'un actif : **valeur actuelle < valeur nette comptable**.

| Actif | Valeur actuelle à retenir | Dotation / compte de dépréciation |
|---|---|---|
| Créances clients | Montant **HT** jugé irrécouvrable (la TVA sera récupérée si la créance devient définitivement irrécouvrable) | D 6817 / C 491 (après transfert en 416 *clients douteux*) |
| Stocks | Valeur nette de réalisation (prix de vente estimé – coûts de commercialisation) ou cours du jour | D 6817 / C 39x |
| Titres de participation | **Valeur d'utilité** (quote-part de capitaux propres, rentabilité, perspectives, valeur de marché… approche multicritère) | D 6866 / C 2961 |
| Titres de placement (VMP) | Cours moyen du dernier mois (titres cotés) | D 6866 / C 590 |
| Immobilisations corporelles / incorporelles | Max (valeur vénale, valeur d'usage), test si indice de perte de valeur | D 6816 / C 29x |

> ⚠️ Erreur classique : déprécier une créance **TTC**. La TVA collectée n'est pas une perte : elle sera imputée sur la CA3 quand la créance sera définitivement irrécouvrable (art. 272-1 CGI). On déprécie le **HT**.

> 💡 Réflexe senior : pour chaque dépréciation, gardez la **pièce probante** dans le dossier (jugement d'ouverture, lettre du mandataire, relances, état des ventes après clôture, rapport d'évaluation). Le contrôleur fiscal demandera ce qui rendait la perte « probable » **à la clôture**.

---

## 5. Les opérations en devises

> 🟢 **En clair :** quand un client achète ou vend en dollars (par exemple C19 Asia Trading, qui importe de Chine), le montant en euros change avec le cours. À la clôture, on recalcule les dettes et les créances au cours du jour. Les pertes probables sont prises en compte, les gains probables non (prudence).

### 5.1 Principe

Les créances et dettes en devises sont enregistrées au **cours du jour de l'opération** (cours BCE en pratique). À la clôture, les éléments **monétaires** (créances, dettes, emprunts, prêts) sont **convertis au cours de clôture** ; l'écart n'est **pas** passé en résultat, il est porté au bilan :

> 🟢 **En clair :** on enregistre d'abord la facture en devises au cours du jour. À la clôture, on recalcule ce qui reste à payer ou à recevoir au cours du dernier jour. La différence ne va pas dans le résultat : elle est rangée au bilan, dans un compte d'écart.

| Situation à la clôture | Écart | Compte | Traitement |
|---|---|---|---|
| Dette qui augmente / créance qui diminue | **Perte latente** | **476** *Écarts de conversion – Actif* | **Provision pour perte de change** (D 6865 / C 1515) |
| Dette qui diminue / créance qui augmente | **Gain latent** | **477** *Écarts de conversion – Passif* | **Rien en résultat** (prudence) |

Écriture type (dette fournisseur qui augmente) : **D 476 / C 401**. Créance qui augmente : **D 411 / C 477**. Extourne au 1er jour de l'exercice suivant.

- **Position globale de change** : si des créances et dettes dans la même devise ont des **échéances voisines**, la provision peut être limitée à la **perte nette** (et doit l'être si c'est la pratique de l'entité, de façon permanente).
- **Opérations couvertes** (achat à terme, option) : la perte n'est pas provisionnée à hauteur de la couverture (règlement ANC n° 2015-05 sur les instruments financiers à terme).
- **Disponibilités en devises** (compte bancaire USD) : converties au cours de clôture, l'écart va **directement en résultat** (666 / 766).
- **Éléments non monétaires** (stocks, immobilisations, acomptes sur commandes en pratique) : **restent au coût historique**, jamais réévalués.
- **Gains et pertes de change réalisés** : sur opérations **commerciales** en **656 / 756** ; sur opérations **financières** en **666 / 766** (règlement ANC n° 2015-05).

### 5.2 Fiscalement (art. 38, 4 CGI)

Les écarts de conversion **sont pris en compte dans le résultat fiscal** : l'écart **passif** (gain latent) est **réintégré**, l'écart **actif** (perte latente) est **déduit**, et la **provision pour perte de change est réintégrée** (sinon la perte serait déduite deux fois). Ces retraitements figurent sur la 2058-A ; un état de suivi des écarts est joint.

> 🟢 **En clair :** pour l'impôt, l'écart de change compte tout de suite, qu'il soit un gain ou une perte. On fait donc des ajustements sur la 2058-A. Et on rajoute la provision pour perte de change, pour ne pas déduire la même perte deux fois.

---

## 6. Les événements postérieurs à la clôture

> 🟢 **En clair :** entre la date de clôture et le jour où le dirigeant arrête les comptes, il se passe des choses. Une seule question à vous poser : l'événement concerne-t-il une situation qui existait déjà à la clôture ? Si oui, on corrige les comptes. Si non, on l'explique dans l'annexe.

Période : **entre la date de clôture et la date d'arrêté des comptes** par l'organe compétent (gérant, président, conseil).

| Type | Définition | Traitement |
|---|---|---|
| **Événement ajustant** | Il **précise une situation qui existait à la clôture** (liquidation d'un client déjà en difficulté, jugement d'un litige déjà né, vente d'un stock à perte confirmant une valeur nette de réalisation, accord d'un assureur sur un sinistre antérieur) | **Ajuster les comptes** de l'exercice clos |
| **Événement non ajustant** | Il **trouve son origine après la clôture** (incendie en janvier, perte d'un client sain, acquisition, litige né en N+1) | **Pas d'ajustement** ; **information en annexe** s'il est significatif (art. L. 123-13 et R. 123-196 C. com. — information sur les événements significatifs postérieurs) |
| Événement remettant en cause la **continuité d'exploitation** | Quelle que soit son origine | Si la continuité est compromise, les comptes ne peuvent plus être établis en valeurs de continuation |

> 💡 Réflexe senior : avant de signer la plaquette, faites une **revue des événements postérieurs** : relevés bancaires de N+1, factures et avoirs de N+1, courriers d'avocat et de mandataire, procès-verbaux, et **une question écrite au dirigeant** (« Avez-vous connaissance d'un événement survenu depuis la clôture qui pourrait affecter les comptes ? »). Gardez sa réponse : elle alimente la **lettre d'affirmation**.

---

## 7. Changements comptables et corrections d'erreurs

> 🟢 **En clair :** trois situations différentes : on change de méthode (rare), on révise une estimation (courant), ou on corrige une erreur (oubli, doublon). Chacune a son traitement. Retenez surtout ceci : une erreur se corrige dans le résultat, pas dans le report à nouveau.

| Nature | Exemple | Traitement comptable | Fiscalement |
|---|---|---|---|
| **Changement de méthode** | Passage à la méthode préférentielle (IDR provisionnées, coûts d'emprunt…), changement de méthode de valorisation des stocks justifié | Effet calculé à l'ouverture, **imputé en capitaux propres (report à nouveau)** ; information en annexe (PCG, règles sur les changements comptables, art. 122-1 s.) | L'impact n'est **pas** fiscalement neutralisé : il est **réintégré ou déduit** sur la déclaration de l'exercice du changement |
| **Changement d'estimation** | Révision de la durée d'utilisation, du taux de garantie, du coût du gros entretien | **Prospectif**, en **résultat** de l'exercice | Suit le traitement comptable |
| **Correction d'erreur** | Facture oubliée, double comptabilisation, omission d'une provision alors que l'information existait | Comptabilisée **en résultat de l'exercice de découverte**, dans le compte par nature concerné, avec **information en annexe** si significative | La charge ou le produit se rattache à l'exercice **d'origine** : **réintégration/déduction** sur l'exercice de découverte et **réclamation** ou **déclaration rectificative** sur l'exercice d'origine (s'il n'est pas prescrit). Voir aussi le mécanisme de **correction symétrique des bilans** (art. 38, 4 bis CGI) |

> ⚠️ Erreur classique : faire passer une erreur en report à nouveau « pour ne pas abîmer le résultat ». En PCG, **seul le changement de méthode** passe en capitaux propres ; l'erreur passe en résultat.

> ⚠️ Erreur classique : continuer à utiliser les comptes 672 / 772 « charges/produits sur exercices antérieurs » comme réflexe. Avec la restriction du résultat exceptionnel, comptabilisez la correction **dans le compte par nature** (achat, vente…) et expliquez-la en annexe — *subdivision selon la nomenclature 2025 du PCG à vérifier dans votre logiciel*.

---

## 8. La procédure de clôture et la revue analytique

> 🟢 **En clair :** c'est la « recette » de la clôture. Dans quel ordre passer les écritures pour ne pas tout refaire, puis comment vérifier que les chiffres sont cohérents d'une année sur l'autre. L'impôt sur les sociétés se calcule toujours en dernier.

### 8.1 L'ordre logique des écritures d'inventaire

L'ordre compte : chaque étape alimente la suivante.

1. **Rapprochements** : banque, caisse, comptes de tiers lettrés, comptes d'attente (471-475) soldés.
2. **Extournes d'ouverture vérifiées** (408, 418, 486, 487, 428x, 438x, 4486, 4686, 4687, 476/477).
3. **Cut-off achats/ventes** : FNP, FAE, avoirs à recevoir/établir.
4. **CCA / PCA**.
5. **Charges de personnel** : congés payés, primes, charges sociales à payer.
6. **Stocks et en-cours** : inventaire, valorisation, variation de stock.
7. **Immobilisations** : acquisitions/cessions, dotations aux amortissements (comptables et dérogatoires).
8. **Devises** : conversion des créances et dettes, écarts 476/477, bancaire en devises.
9. **Dépréciations** (créances, stocks, titres, immobilisations).
10. **Provisions pour risques et charges** (dont perte de change, perte à terminaison).
11. **Intérêts courus**, produits à recevoir divers.
12. **Événements postérieurs** (ajustements).
13. **Impôts et taxes** (CFE, C3S, taxe sur les véhicules…), **participation** le cas échéant.
14. **Impôt sur les sociétés** (en dernier : il dépend de tout le reste).
15. **Revue analytique finale**, annexe, liasse.

### 8.2 La revue analytique

Comparez N et N-1 (et budget) : CA, taux de marge, charges externes, masse salariale, ratios clients (DSO) et fournisseurs (DPO), BFR. **Toute variation de plus de 10 % ou d'un montant significatif doit avoir une explication écrite** dans le dossier. Un compte de charge qui baisse sans raison signale souvent une **FNP oubliée** ; un délai client qui s'allonge signale une **créance douteuse** non dépréciée.

> 💡 Réflexe senior : le seuil de signification se fixe **avant** de réviser (souvent 1 à 2 % du CA ou 5 à 10 % du résultat courant). En dessous, on documente et on simplifie ; au-dessus, on corrige et on prouve.

---

## 9. Checklist de fin de module

- [ ] Je contrôle que toutes les régularisations de l'exercice précédent ont été extournées.
- [ ] Je sais construire un cut-off à partir des pièces du mois N+1 et des derniers BL.
- [ ] Je passe FNP/FAE/avoirs **HT + TVA en attente** (44586/44587), CCA/PCA **en HT**.
- [ ] Je distingue avoir (réduction de prix, avec TVA) et indemnité (hors champ).
- [ ] Je ne constate une provision que si les **trois conditions** sont réunies et je la mesure à la meilleure estimation, documentée.
- [ ] Je connais les provisions **non déductibles** (amendes, IDR, perte de change, titres de participation, provisions non justifiées).
- [ ] Je déprécie les créances **HT**, les stocks à la **valeur nette de réalisation**, les titres à la **valeur d'utilité**.
- [ ] Je convertis les éléments **monétaires** en devises, j'enregistre 476/477, la provision 1515, et je retraite fiscalement.
- [ ] Je classe chaque événement postérieur : **ajustant** (on corrige) ou **non ajustant** (annexe).
- [ ] Je distingue changement de méthode (capitaux propres), d'estimation (prospectif) et correction d'erreur (résultat + traitement fiscal sur l'exercice d'origine).
- [ ] Je refuse, par écrit et avec arguments, toute provision de « lissage ».
- [ ] J'enchaîne les écritures d'inventaire dans l'ordre et je termine par l'IS et la revue analytique.

### Exercices du module

| N° | Client | Thème | Difficulté |
|---|---|---|---|
| E09-01 | C11 Transports Leroy | Cut-off : 15 pièces de janvier | ★★★ |
| E09-02 | C04 Le Petit Zinc | Charges constatées d'avance au 30/06 | ★☆☆ |
| E09-03 | C08 TechNova | PCA sur abonnements SaaS | ★★☆ |
| E09-04 | C21 FitClub Villeurbanne | PCA abonnements, séances, redevance au 31/08 | ★★☆ |
| E09-05 | C13 Atelier Ligne | FNP, FAE, en-cours, PCA au 30/09 (TVA sur encaissements) | ★★☆ |
| E09-06 | C03 Garage Martin | Provisions litige prud'homal et garantie, fiscalité | ★★☆ |
| E09-07 | C19 Asia Trading | Dettes et créances en USD, écarts, provision | ★★★ |
| E09-08 | C07 SCI Horizon Pro | Provision pour gros entretien vs composant | ★★☆ |
| E09-09 | C24 Menuiserie Bois & Création | Événements postérieurs à la clôture | ★★★ |
| E09-10 | C10 Delta Invest | Dépréciation des titres de la Menuiserie | ★★★ |
| E09-11 | C11 Transports Leroy | Correction d'erreurs 2025 + indemnité d'assurance sinistre | ★★★ |
| E09-12 | C02 Bâtisseurs du Sud | Corner case : provision de « lissage » refusée, perte à terminaison | ★★☆ |

## À retenir en 30 secondes

- Chaque année porte ses propres charges et produits, quelle que soit la date de la facture ou du paiement.
- Facture pas reçue, facture pas encore émise, avoir attendu : le hors taxe va en charge ou en produit, la TVA dans un compte d'attente. Et vous annulez (extournez) le 1er jour de l'année suivante.
- Charges et produits constatés d'avance : toujours en hors taxe, jamais de TVA.
- Une provision seulement si les trois conditions sont réunies (obligation, sortie d'argent probable, montant estimable), avec une preuve écrite au dossier.
- On déprécie une créance sur le hors taxe, jamais sur le TTC.
- Devises : les pertes probables sont provisionnées, les gains probables ne vont pas en résultat.
- Après la clôture : situation qui existait déjà → on corrige ; situation nouvelle → on l'explique en annexe. L'IS se calcule en dernier.
