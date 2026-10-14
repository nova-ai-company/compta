# M05 — Banque, caisse et financements

> **Objectif du module.** La trésorerie est le seul compte du bilan que l'on peut **prouver au centime** par un document externe (le relevé bancaire). Un senior s'en sert comme d'une ancre : si la banque est juste, une bonne partie du reste l'est aussi. Inversement, une caisse créditrice, un compte d'attente plein ou un rapprochement « à peu près » sont les premiers signaux qu'un vérificateur ou un commissaire aux comptes repère. Ce module couvre la banque et la caisse au quotidien, puis tous les modes de financement que vous rencontrerez dans le portefeuille : emprunt, PGE, crédit-bail, LLD, comptes courants d'associés, affacturage, Dailly, placements, prélèvements de l'exploitant.

!!! abstract "En clair — ce module en 5 idées"
    1. **La banque, c'est le compte qu'on peut vérifier au centime.** Chaque mois, on compare la comptabilité avec le relevé de la banque. Les deux doivent finir par donner le même solde.
    2. **Une caisse ne peut jamais être « dans le rouge ».** On ne peut pas sortir des billets qu'on n'a pas. Si la caisse de C04 Le Petit Zinc, le restaurant, devient négative, il y a forcément une erreur ou une recette oubliée.
    3. **Une mensualité d'emprunt contient deux choses.** Une partie rembourse la dette, l'autre paie les intérêts. Seul le tableau de la banque (tableau d'amortissement) donne le partage.
    4. **L'argent des associés et celui de la société sont séparés.** Un associé peut prêter à sa société, mais dans une SARL ou une SAS, la société ne doit pas lui avancer d'argent. Et l'argent des propriétaires encaissé par l'agence C22 ImmoPlus n'est pas du chiffre d'affaires.
    5. **Rien ne reste « en attente ».** Une opération inconnue peut aller un moment dans un compte d'attente (471), mais ce compte doit être vide à chaque arrêté. Chaque ligne en attente est une question à poser au client.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Compte 512 « Banque » | Le compte où l'on suit, dans la comptabilité, l'argent sur le compte bancaire | Un virement client reçu s'inscrit au débit du 512 |
    | Rapprochement bancaire | La comparaison, ligne à ligne, entre la comptabilité et le relevé de la banque | Fait chaque mois pour C01 Boulangerie Dupain |
    | Suspens | Une opération déjà enregistrée d'un côté, pas encore de l'autre | Un chèque envoyé le 30/06, pas encore encaissé par le fournisseur |
    | Pointer | Cocher une ligne du relevé qui correspond à une ligne de la comptabilité | Le prélèvement EDF de 245 € pointé des deux côtés |
    | Caisse (530) | Le compte qui suit les espèces de l'entreprise | Les billets dans le tiroir-caisse du salon C20 Style & Vous |
    | Billetage | Le comptage physique des billets et pièces de la caisse | Fait le soir de la clôture |
    | Virement interne (580) | Un compte « de passage » pour les transferts entre deux comptes de la même entreprise | Les espèces de la caisse déposées à la banque |
    | Tableau d'amortissement (emprunt) | Le tableau de la banque qui détaille chaque mensualité : capital, intérêts, assurance | Indispensable pour saisir les échéances du PGE de C24 |
    | Intérêts courus | Les intérêts déjà « gagnés » par la banque à la date du bilan, mais pas encore prélevés | Intérêts du 5 au 30/09 à la clôture |
    | PGE | Un prêt bancaire classique, mais dont le remboursement est garanti par l'État | C24 Menuiserie Bois & Création en rembourse encore un |
    | Crédit-bail | Une location avec possibilité d'acheter le bien à la fin du contrat | Une machine louée en crédit-bail avec option d'achat finale |
    | LLD | Une location longue durée, sans intention d'acheter le bien | Les camions de C11 Transports Leroy |
    | Compte courant d'associé (455) | L'argent qu'un associé prête à sa société | Le gérant laisse 10 000 € à disposition de sa SARL |
    | Compte de l'exploitant (108) | Le compte où l'on suit les retraits et apports personnels d'un entrepreneur individuel | Les prélèvements personnels d'un exploitant en entreprise individuelle |
    | Compte d'attente (471) | Un compte provisoire pour une opération dont on ignore encore la nature | Un virement reçu sans libellé |

---

## 1. La banque : relevés, saisie et rapprochement

> 🟢 **En clair :** chaque mois, vous comparez la banque dans la comptabilité avec le relevé de la banque. Les différences viennent soit d'un simple décalage de dates, soit d'une erreur à trouver. C'est la base du travail de tenue.

### 1.1 Le principe des comptes réciproques

La banque tient **votre compte chez elle** ; vous tenez **le compte de la banque chez vous** (512). Les deux enregistrent les mêmes opérations, mais **en sens inverse** :

| Opération | Chez vous (512) | Sur le relevé |
|---|---|---|
| Encaissement (remise de chèques, virement reçu) | **Débit** | **Crédit** |
| Décaissement (chèque émis, prélèvement, virement émis) | **Crédit** | **Débit** |
| Solde « positif » | Solde **débiteur** | Solde **créditeur** |

> 🟢 **En clair :** la banque voit les choses « dans l'autre sens ». Quand vous avez de l'argent, la banque vous le doit : votre relevé affiche « créditeur », alors que votre 512 est « débiteur ». Ce n'est pas une erreur, c'est normal.

Les deux soldes diffèrent à une date donnée pour deux raisons seulement :
1. **décalages temporels** (une opération est déjà chez l'un, pas encore chez l'autre) ;
2. **erreurs** (de l'entreprise, du cabinet… très rarement de la banque).

### 1.2 Les suspens classiques

| Côté | Suspens | Traitement |
|---|---|---|
| Comptabilisé chez nous, pas encore en banque | Chèque émis non encaissé par le fournisseur ; remise de chèques/espèces du dernier jour ; remise CB du dernier jour (créditée J+1/J+2) | **Rien à comptabiliser** : on attend, et on vérifie le relevé suivant. |
| En banque, pas encore chez nous | Frais bancaires, agios, commissions CB, prélèvements non annoncés, virements reçus non identifiés, rejets de prélèvement, chèques impayés | **À comptabiliser** (avec la bonne pièce) ou, si non identifié, en **471** provisoirement. |

### 1.3 La méthode de rapprochement (pas à pas)

1. Partir de l'**état de rapprochement du mois précédent** : les suspens d'ouverture doivent se dénouer (vérifiez qu'ils apparaissent bien sur le relevé du mois).
2. **Pointer** chaque ligne du relevé avec une ligne du 512 (même montant, date cohérente). Les logiciels font du pointage automatique : vérifiez toujours les pointages « à 1 centime près » ou sur montants ronds identiques.
3. Lister les lignes **non pointées** de chaque côté.
4. Établir l'état :

| Solde du relevé (créditeur) | | Solde du 512 (débiteur) | |
|---|---|---|---|
| – chèques émis non débités | | – frais/agios/prélèvements non saisis | |
| + remises non créditées | | + virements reçus non saisis | |
| **= solde bancaire rectifié** | X | **= solde comptable rectifié** | X |

5. Les deux soldes rectifiés **doivent être égaux**. S'il reste un écart : il y a une **erreur**, pas un suspens.
6. Passer les écritures côté entreprise ; archiver l'état signé dans le dossier.

> 💡 **Réflexe senior — chercher un écart :**
> - écart **divisible par 9** → inversion de chiffres (1 524 saisi 1 254 : écart 270 = 9 × 30) ;
> - écart égal à **un montant du relevé** → opération oubliée ;
> - écart égal au **double** d'un montant → opération saisie dans le mauvais sens ;
> - écart rond (100, 1 000) → erreur de frappe ou addition ;
> - écart égal à une **commission** → encaissement saisi brut au lieu de net (titres-restaurant, Stripe, marketplace).

> ⚠️ **Erreur classique :** « équilibrer » le rapprochement par une écriture en 471 ou en 658 du montant de l'écart. Un écart inexpliqué se **cherche** ; il ne se solde pas.

**Suspens anciens.** Un chèque émis non encaissé depuis plus d'un an (délai de présentation d'un chèque : 1 an et 8 jours) doit être analysé : fournisseur toujours créancier ? On contre-passe le chèque (512 / 401) et la dette fournisseur réapparaît ; si elle est définitivement éteinte (prescription, renonciation), elle devient un produit. Un chèque **reçu** jamais crédité est une créance client à relancer.

### 1.4 Frais, agios, cartes bancaires

| Nature | Compte | TVA |
|---|---|---|
| Frais de tenue de compte, commissions de virement, cotisations carte | 627 Services bancaires et assimilés | En principe exonérés (art. 261 C CGI) sauf certaines prestations taxées — se fier à la mention « dont TVA » du relevé |
| Commissions sur encaissements CB (commerçant) | 627 | Généralement exonérées |
| Agios (intérêts débiteurs du découvert) | 6615 Intérêts des comptes courants et des dépôts créditeurs / 661 | Hors champ |
| Commissions d'engagement, de plus fort découvert | 627 (ou 6618 selon la nature) | — |

Les **encaissements CB** arrivent par remises (J+1 ou J+2) : à la clôture, la remise du dernier jour est un suspens. Si l'entreprise utilise un TPE et un logiciel de caisse, rapprochez le **total CB du Z** de la **remise bancaire** : un écart récurrent révèle souvent des encaissements CB non déclarés en caisse ou des commissions mal saisies.

### 1.5 Virements internes : le compte 580

Quand une entreprise a deux comptes bancaires (ou une caisse et une banque), un transfert est enregistré **deux fois** (relevé A et relevé B, ou caisse et banque). Pour éviter le doublon, on passe par **580 Virements internes** :

| Écriture | Débit | Crédit |
|---|---|---|
| Journal banque A (sortie) | 580 | 512 A |
| Journal banque B (entrée) | 512 B | 580 |

Le 580 doit être **soldé** à chaque fin de mois. Un solde résiduel = un virement saisi d'un seul côté ou en double. Même principe pour la **remise d'espèces** : 580 / 530 dans le journal de caisse, 512 / 580 dans le journal de banque.

---

## 2. La caisse

> 🟢 **En clair :** la caisse, ce sont les espèces. Le solde de la comptabilité doit correspondre aux billets réellement comptés, et il ne peut jamais être négatif. Chez les clients qui encaissent beaucoup d'espèces (boulangerie C01, restaurant C04, salon de coiffure C20), c'est un point que le fisc regarde de près.

### 2.1 Les règles d'or

- **Une caisse ne peut jamais être créditrice.** On ne peut pas sortir des billets qu'on n'a pas. Un solde créditeur, même un seul jour, prouve une erreur de saisie ou une recette non enregistrée. En contrôle fiscal, c'est un motif classique de **rejet de comptabilité** (comptabilité non probante) et de **reconstitution du chiffre d'affaires**.
- Le solde comptable doit correspondre au **comptage physique** (billetage) à la clôture et, idéalement, régulièrement.
- Les recettes sont justifiées par les **Z** (tickets de clôture journalière) d'un logiciel de caisse **certifié** (art. 286, I-3° bis CGI ; amende de 7 500 € par système non conforme — art. 1770 duodecies CGI).

### 2.2 Les écarts de caisse

| Situation | Écriture |
|---|---|
| Comptage < solde comptable (manquant) | 658 Charges diverses de gestion courante / 530 (*subdivision selon la nomenclature 2025 du PCG*) |
| Comptage > solde comptable (excédent) | 530 / 758 Produits divers de gestion courante |

Un manquant **récurrent** n'est pas un « écart » : c'est un symptôme (vol, prélèvements du dirigeant non déclarés, recettes non enregistrées).

### 2.3 Les paiements en espèces

- **Plafond entre professionnels et vers un particulier non commerçant résidant fiscalement en France : 1 000 €** (art. L. 112-6 et D. 112-3 du Code monétaire et financier), pour une **même dette** (on ne fractionne pas une facture pour passer sous le plafond). Sanction : amende pouvant aller jusqu'à 5 % des sommes payées en violation, **solidaire** entre débiteur et créancier (art. 1840 J CGI).
- Les **salaires** au-delà d'un seuil (1 500 € par mois, valeur à vérifier) doivent être payés par chèque ou virement (art. L. 3241-1 C. trav.).
- Les **prélèvements en espèces du dirigeant** sans pièce sont l'angle mort de la caisse (voir § 6).

> 💡 **Réflexe senior :** dans les commerces à forte proportion d'espèces (Boulangerie Dupain, Le Petit Zinc, Style & Vous), comparez chaque mois le **ratio espèces / CA total** au mois précédent et à l'année précédente. Une chute brutale du ratio sans raison commerciale doit déclencher une question au client.

---

## 3. Les emprunts

> 🟢 **En clair :** un emprunt se suit avec le tableau d'amortissement fourni par la banque. Chaque mensualité se découpe en capital remboursé, intérêts et assurance. À la clôture, on vérifie que la dette en comptabilité est égale à ce qui reste dû selon le tableau.

### 3.1 Le tableau d'amortissement

Pour un emprunt à **mensualités constantes** de capital C, taux annuel t, n mensualités :

- taux mensuel i = t / 12 ;
- mensualité a = C × i / (1 – (1 + i)^–n) ;
- intérêts du mois = capital restant dû × i ;
- capital remboursé = a – intérêts.

S'ajoutent souvent l'**assurance emprunteur** (fixe ou sur capital restant dû) et des **frais de dossier**.

### 3.2 Les écritures

| Événement | Débit | Crédit |
|---|---|---|
| Déblocage des fonds | 512 | 164 Emprunts auprès des établissements de crédit |
| Frais de dossier | 627 (ou étalement selon l'option retenue et la nomenclature 2025) | 512 |
| Échéance | 164 (capital) + 661 (intérêts, subdivision 6611) + 616 (assurance) | 512 |
| Clôture : intérêts courus non échus | 661 | **1688 Intérêts courus** |
| Réouverture N+1 | Contre-passation (ou extourne) de l'écriture de 1688 | |

**Intérêts courus à la clôture** : de la date de la dernière échéance à la date de clôture. Usage bancaire : base **exact/360** (nombre de jours réels / 360). Exemple : capital restant dû 100 000 €, taux 3,6 %, échéance le 5, clôture le 30/09 → 25 jours → 100 000 × 3,6 % × 25 / 360 = 250,00 €.

> 🟢 **En clair :** entre la dernière mensualité et la date du bilan, la banque a « gagné » des intérêts qu'elle n'a pas encore prélevés. On les ajoute aux charges de l'année, avec une dette en face (1688), car ils concernent bien cette année.

> ⚠️ **Erreur classique :** passer toute la mensualité en 661, ou toute en 164. Le relevé ne détaille pas le partage : **seul le tableau d'amortissement** le donne. Exigez-le du client dès le déblocage, et contrôlez à la clôture que le **solde du 164 = capital restant dû** du tableau à la date de clôture.

### 3.3 Présentation et annexe
Le bilan présente l'emprunt en dettes financières ; l'annexe (état des échéances) distingue la part **à moins d'un an**, **de un à cinq ans** et **à plus de cinq ans**. Les **garanties** données (nantissement du fonds, caution du dirigeant, hypothèque) sont des engagements à mentionner.

### 3.4 Le prêt garanti par l'État (PGE)
- Emprunt bancaire classique (164), garanti par l'État via Bpifrance. Première année sans amortissement (différé), puis possibilité d'amortir sur 1 à 5 ans supplémentaires (durée totale maximale de 6 ans), avec parfois un différé supplémentaire d'un an accordé en 2021-2022.
- Le **coût de la garantie** (commission prélevée par la banque et reversée à l'État) est **progressif** selon l'année et la taille de l'entreprise : à lire **dans le contrat** (pour une PME, barème usuel de 0,25 % la 1re année, 0,50 % les 2e et 3e, 1 % les 4e à 6e — valeurs à vérifier sur chaque contrat). Comptabilisation : 627 (commission de garantie) ou 661 si le contrat l'intègre au taux — soyez cohérent d'une année à l'autre.
- Entreprise en difficulté (Menuiserie Bois & Création) : restructuration possible via la **Médiation du crédit** ou une procédure amiable ; ne jamais laisser le client « arrêter de payer » sans démarche.

### 3.5 Le découvert
Un découvert au 31/12 n'est pas une trésorerie négative à « compenser » : le 512 créditeur se reclasse au bilan en **concours bancaires courants** (dettes financières). Ne compensez pas un compte créditeur avec un compte débiteur d'une autre banque (non-compensation), sauf convention de fusion de comptes.

---

## 4. Crédit-bail, location financière, LLD

> 🟢 **En clair :** quand l'entreprise loue un bien au lieu de l'acheter, elle enregistre des loyers en charges, et le bien n'apparaît pas dans son bilan. Mais il faut quand même informer le lecteur des comptes (dans l'annexe) des loyers qui restent à payer.

### 4.1 Le crédit-bail en comptes sociaux
En comptes individuels français, le **crédit-bail n'est pas inscrit à l'actif** du preneur : l'entreprise n'est pas propriétaire tant qu'elle n'a pas levé l'option.

| Événement | Débit | Crédit |
|---|---|---|
| Redevance (mobilier) | 6122 Redevances de crédit-bail mobilier + 44566 | 512 / 401 |
| Redevance (immobilier) | 6125 Redevances de crédit-bail immobilier + 44566 | 512 / 401 |
| Premier loyer majoré | 6122, puis à la clôture étalement de la fraction non consommée en **486 Charges constatées d'avance** | |
| Dépôt de garantie versé | 275 | 512 |
| Levée de l'option | 218x (prix de levée) + 44562 | 512 / 404 |

Après la levée d'option, le bien est amorti sur sa **durée d'utilisation résiduelle** à partir de son prix de levée (souvent symbolique : 1 % de la valeur d'origine).

### 4.2 L'information en annexe (engagement hors bilan)
L'annexe doit donner, pour les biens en crédit-bail : la **valeur d'origine**, les **amortissements** qui auraient été pratiqués si le bien avait été acheté (cumul et dotation de l'exercice), les **redevances payées** (exercice et cumul), les **redevances restant à payer** (à moins d'un an, de 1 à 5 ans, à plus de 5 ans) et le **prix d'achat résiduel**. Le niveau de détail dépend de la taille de l'entreprise (annexe abrégée des petites entreprises) — vérifiez les exigences applicables.

### 4.3 Points fiscaux
- **Véhicule de tourisme en crédit-bail ou en location > 3 mois** : la fraction des loyers correspondant à l'amortissement pratiqué par le bailleur au-delà du **plafond** de l'art. 39-4 CGI est **réintégrée** (le bailleur communique chaque année le montant). Voir M06 pour les plafonds.
- **Levée d'option** : régime particulier pour les immeubles (art. 239 sexies et suivants CGI) ; pour les biens mobiliers, attention à la plus-value ultérieure en cas de revente rapide (régime de l'art. 39 duodecies, 10 CGI).

### 4.4 La location financière et la LLD
- **Location financière** (équipements de FitClub, photocopieurs) et **LLD** (camions de Transports Leroy, véhicules) : simples loyers en **6122/6135** (selon la nature), pas d'option d'achat (ou option non déterminante). Pas d'actif, pas d'emprunt.
- Annexe : les engagements de loyers futurs peuvent constituer des engagements hors bilan significatifs.
- Fiscalement, même réintégration que ci-dessus pour les véhicules de tourisme.

> 💡 **Réflexe senior :** à chaque nouveau dossier, demandez la **liste des contrats de financement** (emprunts, crédit-bail, LLD, location financière) avec leurs échéanciers. C'est la base des engagements hors bilan, des intérêts courus, du prévisionnel et des réintégrations fiscales.

---

## 5. Les comptes courants d'associés

> 🟢 **En clair :** un associé peut prêter de l'argent à sa société : c'est son « compte courant ». L'inverse (la société qui avance de l'argent à son dirigeant) est interdit dans la plupart des sociétés. Surveillez donc que ce compte ne passe jamais du mauvais côté.

### 5.1 Principe
Un associé qui laisse des sommes à disposition de la société (apport de trésorerie, rémunération non prélevée, dépenses payées pour la société) détient une **créance** sur elle : compte **455 Associés – comptes courants** (subdivisé par associé : 4551 Léo Martin, 4552 Sarah Cohen…).

| Opération | Débit | Crédit |
|---|---|---|
| Apport en compte courant | 512 | 455x |
| Dépense de la société payée par l'associé | Compte de charge / d'immobilisation + 4456x (si facture au nom de la société) | 455x |
| Intérêts dus à l'associé | 6615 Intérêts des comptes courants | 455x (ou 4426 pour la retenue à la source) |
| Remboursement | 455x | 512 |

### 5.2 Intérêts : limite de déduction
Les intérêts servis aux associés ne sont déductibles que si (art. 39-1-3° et 212 CGI) :
- le **capital est entièrement libéré** ;
- le taux n'excède pas le **taux moyen des prêts à taux variable aux entreprises d'une durée initiale supérieure à 2 ans** (taux publié chaque trimestre ; on retient la moyenne des taux des trimestres couverts par l'exercice — **valeur à vérifier chaque année**), sauf à justifier d'un taux de marché supérieur obtenu d'un tiers (art. 212 CGI) ;
- s'ajoutent les règles de sous-capitalisation pour les entreprises liées.

> 🟢 **En clair :** la société peut verser des intérêts à l'associé qui lui prête de l'argent. Mais le fisc n'accepte de les déduire que si le capital a été entièrement versé et si le taux ne dépasse pas un plafond publié chaque trimestre.

Les intérêts perçus par l'associé personne physique supportent le **prélèvement forfaitaire non libératoire** et les **prélèvements sociaux**, retenus à la source par la société et déclarés (imprimé 2777) — taux à vérifier pour 2026.

### 5.3 Le compte courant débiteur : interdit dans la plupart des sociétés
- **SARL / EURL** : interdiction pour les **gérants et associés personnes physiques** (et leurs conjoints, ascendants, descendants) de se faire consentir un découvert en compte courant par la société (art. L. 223-21 C. com.). Sanction : nullité du contrat ; en pratique, le risque pénal est l'**abus de biens sociaux** (art. L. 241-3 C. com.).
- **SA / SAS** : même interdiction pour les administrateurs, directeurs généraux, président de SAS (art. L. 225-43 et L. 227-12 C. com.).
- **Fiscalement** : les sommes mises à disposition des associés à titre d'avances ou de prêts sont **présumées revenus distribués** (art. 111 a CGI), sauf remboursement.

> ⚠️ **Erreur classique :** imputer en 455 toutes les dépenses personnelles du gérant « pour faire simple ». Le 455 devient débiteur, et vous venez de **documenter vous-même** une infraction. Le senior régularise *avant* la clôture : remboursement, imputation sur une rémunération décidée, distribution votée — et prévient le client par écrit.

---

## 6. L'entreprise individuelle et le compte de l'exploitant

> 🟢 **En clair :** un entrepreneur individuel ne se paie pas de salaire : il retire de l'argent quand il en a besoin. Ces retraits ne sont pas des charges. On les suit dans un compte à part (108), remis à zéro chaque année.

En **entreprise individuelle** (et, par extension de pratique, pour certaines EURL à l'IR — voir E05-08), l'exploitant ne se verse pas un salaire : il **prélève**.

| Opération | Débit | Crédit |
|---|---|---|
| Prélèvement de trésorerie | 108 Compte de l'exploitant | 512 / 530 |
| Dépense personnelle payée par l'entreprise | 108 | 512 |
| Apport personnel de trésorerie | 512 | 108 |
| Clôture : virement du solde du 108 au capital individuel | 101 | 108 (ou inversement) |

Le 108 est **soldé chaque année** contre le capital individuel (101). Les prélèvements ne sont **pas des charges** : le résultat fiscal (BIC/BNC) est taxé chez l'exploitant, quel que soit le montant prélevé.

**EURL à l'IR** : la société reste une personne morale distincte. La rémunération de la gérante associée unique n'est pas déductible du résultat imposable (elle fait partie de son bénéfice BIC). La pratique du cabinet (fiche C20) l'enregistre en 108 ; une approche plus rigoureuse l'enregistre en **644 Rémunération du travail de l'exploitant** puis la réintègre extra-comptablement. Les deux aboutissent au même résultat fiscal ; l'important est la **permanence** et qu'aucune dépense personnelle ne reste en charges.

> 🟢 **En clair :** pour l'EURL C20 Style & Vous, la rémunération de la gérante n'est pas déductible de l'impôt. On peut l'enregistrer de deux façons ; les deux donnent le même impôt. Ce qui compte : garder la même méthode chaque année et ne laisser aucune dépense personnelle dans les charges.

---

## 7. Placements de trésorerie

> 🟢 **En clair :** quand une entreprise a de l'argent qui dort, elle peut le placer (compte à terme, SICAV…). On enregistre les intérêts déjà acquis à la clôture, et on constate une perte si le placement vaut moins cher qu'à l'achat. Un gain non encore réalisé, lui, ne s'enregistre pas.

| Placement | Compte | Points clés |
|---|---|---|
| Compte à terme (CAT) | 508 Autres valeurs mobilières et créances assimilées (ou 5181/compte de dépôt à terme selon nomenclature) | Intérêts courus à la clôture : 5188 / 7682 (intérêts courus sur placements) |
| VMP (SICAV monétaires, actions cotées détenues à court terme) | 503 / 504 / 506 | Évaluées au coût ; **dépréciation** si la valeur à la clôture est inférieure (pas de constatation des plus-values latentes en comptes sociaux) |
| Livret / compte rémunéré | 512 dédié | Intérêts crédités annuellement → produit à recevoir si significatif |

Fiscalement, les plus-values latentes sur certains OPCVM détenus par une société à l'IS peuvent être imposables (art. 209-0 A CGI) : point à signaler quand le portefeuille est significatif.

---

## 8. Mobiliser ses créances : escompte, Dailly, affacturage

> 🟢 **En clair :** « mobiliser ses créances », c'est se faire avancer par la banque ou un factor l'argent que les clients doivent, sans attendre l'échéance. C'est payant, et l'entreprise garde souvent le risque si le client ne paie pas : il faut le signaler dans l'annexe.

| Technique | Principe | Écriture clé | Bilan |
|---|---|---|---|
| **Escompte d'effets** | La banque avance le montant d'une LCR avant l'échéance | 5114 effets à l'escompte / 513 | Engagement hors bilan tant que l'échéance n'est pas passée |
| **Cession Dailly** | Cession de créances professionnelles à la banque par bordereau (art. L. 313-23 CMF) | 512 + 661/627 / 519 Concours bancaires courants (ou maintien en 411 avec dette financière) | La créance reste souvent à l'actif ; **engagement en annexe** |
| **Affacturage** | Le factor achète les créances (avec ou sans recours), finance une partie, retient un fonds de garantie | 467 Factor / 411 ; 512 / 467 ; 627/661 (commission d'affacturage, commission de financement) ; 275 ou 467 (retenue de garantie) | Avec recours : risque conservé → information en annexe |

> 💡 **Réflexe senior :** un relevé d'affacturage mélange tout (financement, commissions, retenues, encaissements). Ouvrez un compte **467 Factor** dédié et rapprochez-le chaque mois avec le relevé du factor, comme une banque.

---

## 9. Le compte d'attente 471

> 🟢 **En clair :** le 471 est une « boîte provisoire » pour les opérations qu'on ne sait pas encore classer. Elle doit être vide à chaque arrêté. Chaque ligne qui y reste est une question à poser au client.

- Sert à **stocker provisoirement** une opération dont on ne connaît pas encore la nature (virement sans libellé, prélèvement inconnu).
- Doit être **vidé à chaque arrêté** (mensuel au cabinet, obligatoirement à la clôture) : un 471 au bilan n'a **aucune signification** comptable (ni actif, ni passif identifiable), il n'apparaît pas dans les postes du bilan publié et le CAC le relève systématiquement.
- Chaque ligne en attente = une **question au client**, datée, tracée. Au-delà d'un délai raisonnable, le senior **tranche** avec le client : à défaut d'identification, un encaissement inexpliqué peut être requalifié en recette (risque fiscal) et un décaissement inexpliqué n'est pas une charge déductible.

> ⚠️ **Erreur classique :** imputer l'écart de rapprochement en 471 « pour boucler ». Le 471 n'est pas un compte d'écart.

---

## 10. Fonds de tiers : séquestre et mandants

> 🟢 **En clair :** certaines entreprises encaissent de l'argent pour quelqu'un d'autre. Les loyers que C22 ImmoPlus encaisse pour les propriétaires ne sont pas à elle : seule sa commission est du chiffre d'affaires. Cet argent ne doit jamais servir à payer les frais de l'agence.

Certaines entreprises encaissent de l'argent qui **ne leur appartient pas** :
- agences immobilières (ImmoPlus) : loyers et dépôts de garantie encaissés pour les propriétaires (loi Hoguet du 2 janvier 1970 et son décret d'application) ;
- hôtels : taxe de séjour ;
- marketplaces, notaires, avocats…

Règles : **compte bancaire séparé** (séquestre/mandants), **comptabilité mandants distincte**, **jamais de chiffre d'affaires** sur ces sommes : seul l'**honoraire** de l'agence est un produit. Utiliser les fonds des mandants pour payer les charges de l'agence est une faute grave (sanctions disciplinaires, mise en jeu de la garantie financière, pénal).

---

## 11. Le prévisionnel de trésorerie

> 🟢 **En clair :** le prévisionnel, c'est un tableau qui prévoit, mois par mois, l'argent qui va entrer et sortir. Il sert à savoir si l'entreprise pourra payer ses factures. Pour C24 Menuiserie Bois & Création, en difficulté, c'est la pièce clé du dossier.

Outil indispensable pour un client en difficulté (Menuiserie Bois & Création) ou en croissance (TechNova, Studio Pixel) :

| Ligne | Mois 1 | Mois 2 | … |
|---|---|---|---|
| Trésorerie d'ouverture | | | |
| + Encaissements clients **TTC** (selon délais réels de paiement) | | | |
| + Autres encaissements (subventions, apports, emprunts, CIR) | | | |
| – Décaissements fournisseurs TTC | | | |
| – Salaires nets, charges sociales (échéances URSSAF) | | | |
| – TVA à décaisser (décalage d'un mois), IS (acomptes) | | | |
| – Échéances d'emprunt, crédit-bail | | | |
| = Trésorerie de clôture | | | |

Règles : raisonner en **TTC** et en **dates de flux** (pas en dates de facture) ; intégrer les échéances fiscales et sociales (dates exactes) ; prévoir au moins 12 mois ; faire un **scénario dégradé**. Pour la continuité d'exploitation (annexe), c'est la pièce que le CAC ou le banquier demandera.

---

## 12. Fraudes et incidents : ce qu'un senior a vu

> 🟢 **En clair :** chèque impayé, virement sans nom, faux changement de RIB d'un fournisseur… Ce tableau vous dit quelle écriture passer, et surtout quoi faire en plus pour protéger le client. Un paiement détourné ne fait pas disparaître la dette envers le vrai fournisseur.

| Incident | Écriture | Ce qu'il faut faire en plus |
|---|---|---|
| **Chèque client impayé** | 411 / 512 (contre-passation) + 627 / 512 (frais) | Relancer, certificat de non-paiement, injonction de payer ; si risque : 416 + dépréciation |
| **Rejet de prélèvement** (client) | 411 / 512 | Idem |
| **Virement reçu sans référence** | 512 / 471 en attendant | Rechercher dans les encours clients (montant exact, cumul de factures, acompte), interroger le client |
| **Fraude au faux fournisseur / changement de RIB** | Le paiement n'éteint **pas** la dette envers le vrai fournisseur : reclasser le décaissement en **467** (créance sur fonds détournés), puis déprécier selon les chances de récupération | Rappel de fonds immédiat auprès de la banque, plainte, déclaration à l'assureur, procédure de contre-appel des changements de RIB |
| **Fraude au président** | Idem | Idem + sensibilisation des équipes |

---

## Checklist de fin de module

- [ ] Je sais établir un état de rapprochement à partir du rapprochement précédent, et chercher un écart (÷ 9, double, montant exact).
- [ ] Je contrôle qu'une caisse n'est **jamais créditrice** et je sais en diagnostiquer les causes.
- [ ] Je connais le plafond de paiement en espèces (1 000 €) et sa sanction (art. 1840 J CGI).
- [ ] J'utilise le 580 pour les virements internes et je vérifie qu'il est soldé.
- [ ] Je découpe une échéance d'emprunt avec le tableau d'amortissement, et je calcule les intérêts courus (1688).
- [ ] Je contrôle 164 = capital restant dû et je ventile les échéances (< 1 an / 1-5 ans / > 5 ans).
- [ ] Je comptabilise un crédit-bail (redevances, premier loyer majoré, levée d'option) et je prépare l'information en annexe.
- [ ] Je connais les conditions de déduction des intérêts de comptes courants (capital libéré, taux plafond).
- [ ] Je sais pourquoi un compte courant débiteur est interdit en SARL/SAS et ce que l'on risque (ABS, art. 111 a CGI).
- [ ] Je solde le 108 en EI et je ne laisse aucune dépense personnelle en charges.
- [ ] Le 471 est à zéro à chaque arrêté.
- [ ] Je ne mélange jamais les fonds de tiers (mandants, taxe de séjour) avec le chiffre d'affaires.
- [ ] Je sais réagir à une fraude au changement de RIB (comptablement et pratiquement).

## À retenir en 30 secondes

- Chaque mois, rapprochez la banque de la comptabilité : un écart inexpliqué est une erreur à chercher, jamais à « boucher ».
- Une caisse n'est jamais négative, et son solde doit correspondre aux espèces comptées.
- Pas de paiement en espèces au-delà de 1 000 € pour une même dette entre professionnels.
- Une mensualité d'emprunt se découpe avec le tableau d'amortissement : capital, intérêts, assurance.
- Un associé peut prêter à sa société ; la société ne doit pas avancer d'argent à son dirigeant.
- L'argent encaissé pour le compte d'autrui (loyers des propriétaires, taxe de séjour) n'est pas du chiffre d'affaires.
- Le compte d'attente 471 est vide à chaque arrêté.
