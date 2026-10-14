# M10 — La fiscalité de l'entreprise : du résultat comptable au résultat fiscal

> **Objectif du module.** À la fin de ce module, vous savez passer seule du résultat comptable au résultat fiscal (2058-A), calculer et comptabiliser l'IS, gérer déficits, acomptes et crédits d'impôt, traiter les impôts locaux et les taxes annexes, établir une 2031, une 2035 ou une 2072, conseiller un micro-entrepreneur, et accompagner un client pendant un contrôle fiscal.
>
> **Prérequis :** M09 (travaux de fin d'exercice). **Renvois :** M13 (intégration fiscale détaillée, bénéfice agricole), M11 (dividendes, capitaux propres), M04 (TVA), M07 (paie).

> ⚠️ **Avertissement « chiffres de l'année ».** Les taux, seuils et barèmes de ce module sont ceux retenus pour l'exercice 2026 **à la date de rédaction**. Chaque fois qu'une valeur est susceptible d'évoluer, elle porte la mention *« valeur à vérifier chaque année »*. Le réflexe senior : **chaque mois de janvier, mettre à jour la fiche « chiffres clés » du cabinet** après lecture de la loi de finances et de la LFSS.

!!! abstract "En clair — ce module en 5 idées"
    1. **L'impôt part du résultat comptable, puis on l'ajuste.** On ajoute ce que l'impôt refuse de déduire, on retire ce qu'il n'impose pas. Ces ajustements se font sur un tableau à part, sans écriture comptable. Exemple : une amende pour excès de vitesse d'un camion de C11 Transports Leroy, le transporteur, reste en charge dans les comptes, mais on la rajoute pour calculer l'impôt.
    2. **L'impôt sur les sociétés (IS) a deux taux.** 15 % sur le début du bénéfice pour les PME qui remplissent les conditions, 25 % au-delà. Il se paie en 4 acomptes puis un solde. Exemple : C25 Studio Pixel a un premier exercice de 16 mois, donc la tranche à 15 % est allongée en proportion.
    3. **Une perte n'est pas perdue pour l'impôt.** Elle peut réduire l'impôt des années suivantes, ou, sur option, celui de l'année précédente. Vous devez la suivre d'une année sur l'autre.
    4. **L'IS n'est pas le seul impôt.** Il y a aussi la CFE, la CVAE, les taxes sur les salaires et sur les voitures de tourisme. Exemple : C10 Delta Invest, la holding, paie la taxe sur les salaires, car elle ne récupère qu'une partie de sa TVA.
    5. **Tous les clients ne sont pas à l'IS.** C20 Style & Vous, le salon de coiffure, est imposé à l'impôt sur le revenu (2031) ; C05 Dr Lambert, médecin, remplit une 2035 ; C06 SCI Les Tilleuls, une 2072. Et en cas de contrôle fiscal, ce sont les délais qui protègent le client.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | Résultat comptable | Le bénéfice ou la perte qui sort des comptes : produits moins charges. | 214 860 € de bénéfice dans l'exemple du § 2.4 |
    | Résultat fiscal | Le bénéfice sur lequel on calcule l'impôt, après ajustements. | Résultat comptable + amendes – dividendes exonérés |
    | Réintégration | Une somme que l'on rajoute au résultat pour calculer l'impôt, car l'impôt ne l'accepte pas en charge. | Une amende, l'IS lui-même |
    | Déduction | Une somme que l'on retire du résultat pour calculer l'impôt, car elle n'est pas imposable. | Un crédit d'impôt recherche enregistré en produit |
    | Extra-comptable | Fait sur le tableau de l'impôt, sans passer d'écriture dans la comptabilité. | Rajouter une amende sur la 2058-A |
    | Liasse fiscale | L'ensemble des formulaires annuels envoyés aux impôts avec les comptes. | 2065 + 2050 à 2059 pour une société au réel normal |
    | 2058-A | Le formulaire qui fait passer du résultat comptable au résultat fiscal. | Une ligne par ajustement |
    | Retraitement temporaire | Un ajustement qui s'inverse plus tard : rajouté une année, retiré une autre. | Une provision non déductible, retirée l'année de sa reprise |
    | Déficit reportable | Une perte fiscale gardée « en réserve » pour réduire l'impôt des années suivantes. | Une start-up qui perd de l'argent pendant 3 ans |
    | Carry-back | L'option qui permet d'utiliser une perte de cette année contre le bénéfice de l'année précédente. | L'État reconnaît alors une créance à l'entreprise |
    | Acompte d'IS | Un paiement d'avance de l'IS, versé en cours d'année. | Le 15/03, le 15/06, le 15/09 et le 15/12 pour une clôture au 31/12 |
    | Crédit d'impôt | Une somme qui diminue directement l'impôt à payer, voire se rembourse. | Le CIR de C08 TechNova pour ses travaux de recherche |
    | Régime mère-fille | Une règle qui exonère presque entièrement les dividendes reçus d'une filiale. | Les dividendes reçus par C10 Delta Invest de ses filiales |
    | CFE | Un impôt local payé par les entreprises, calculé sur la valeur des locaux utilisés. | L'avis arrive en ligne début novembre |
    | Proposition de rectification | Le courrier par lequel l'administration annonce un redressement après un contrôle. | Le client a 30 jours pour répondre |

---

## 1. Le principe : la fiscalité « part » de la comptabilité

> 🟢 **En clair :** l'impôt ne se calcule pas sur une autre comptabilité. On part du résultat comptable et on l'ajuste sur un tableau à part, sans passer d'écriture. Exemple : une amende payée reste en charge dans les comptes, mais on la rajoute pour calculer l'impôt.

Le résultat fiscal est le **résultat comptable corrigé** de retraitements **extra-comptables** (on ne passe **aucune écriture** pour réintégrer une amende) :

```
Résultat comptable (bénéfice ou perte, après IS comptabilisé)
+ Réintégrations  (charges comptabilisées mais non déductibles ; produits imposables non comptabilisés)
– Déductions      (produits comptabilisés mais non imposables ; charges déductibles non comptabilisées)
= Résultat fiscal avant imputation des déficits
– Déficits antérieurs imputés (plafonnés)
= Résultat fiscal imposable (ou déficit de l'exercice)
```

Le support est l'imprimé **2058-A** (régime réel normal) ou le cadre équivalent du **2033-B** (régime simplifié). Le **2058-B** suit les déficits et les provisions non déductibles, le **2058-C** l'affectation du résultat.

> 🟢 **En clair :** chaque régime a son formulaire de calcul : la 2058-A pour le réel normal, la 2033-B pour le simplifié. La 2058-B sert à suivre les pertes et les provisions d'une année sur l'autre ; la 2058-C indique ce que l'on fait du bénéfice.

> 💡 **Réflexe senior :** tenez pour chaque dossier un **tableau de passage** (feuille de travail) : une ligne par retraitement, montant, compte d'origine, justification, référence CGI, et si le retraitement est **définitif** (amende) ou **temporaire** (provision non déductible qui sera déduite lors de sa reprise). Les retraitements temporaires doivent être suivis d'une année sur l'autre — c'est là que les juniors oublient des déductions.

> ⚠️ **Erreur classique :** déduire une charge « parce qu'elle est en 6 ». Une charge n'est déductible que si elle est engagée **dans l'intérêt de l'entreprise**, **justifiée**, **non excessive**, **rattachée au bon exercice**, et **non exclue par un texte** (art. 39 CGI).

---

## 2. Le tableau 2058-A : les retraitements à connaître par cœur

> 🟢 **En clair :** la 2058-A est la « feuille de calcul officielle » du résultat fiscal. Ce sont presque toujours les mêmes ajustements qui reviennent (IS, amendes, voitures, dividendes, provisions). Apprenez-les une fois : vous les retrouverez dans la plupart de vos dossiers.

> Les **codes de lignes** du 2058-A changent parfois d'une année à l'autre : reportez-vous toujours à la notice de l'année. Ci-dessous, on raisonne sur les **libellés**.

### 2.1 Réintégrations courantes

| Retraitement | Règle | Référence |
|---|---|---|
| **IS lui-même** (compte 695, y compris contribution sociale) | L'IS n'est pas déductible de sa propre base | Art. 213 CGI |
| **Amendes, pénalités, majorations** liées à une obligation **légale** (PV, majorations URSSAF, majorations fiscales, amende de non-désignation du conducteur) | Non déductibles. **Attention** : les pénalités **contractuelles** (retard de chantier, de livraison) restent déductibles | Art. 39-2 CGI |
| **Amortissements excédentaires des véhicules de tourisme** | Base amortissable fiscale plafonnée selon le taux de CO₂ (voir § 2.3) ; même logique pour la fraction des loyers de crédit-bail / LLD > 3 mois | Art. 39-4 CGI |
| **Taxes annuelles sur les véhicules de tourisme** (ex-TVS : taxe CO₂ + taxe polluants) | Non déductibles | CGI (art. relatif à la non-déductibilité de ces taxes) — CIBS L. 421-93 s. |
| **Charges somptuaires** : chasse, pêche, yachts, résidences de plaisance | Non déductibles, sauf si c'est l'objet même de l'activité (loueur de bateaux) | Art. 39-4 CGI |
| **Dépenses personnelles du dirigeant** prises en charge (restaurant familial, vacances…) | Non engagées dans l'intérêt de l'entreprise → réintégration ; risque de **revenus distribués** pour le bénéficiaire | Art. 39-1, 109 et 111 CGI |
| **Provisions non déductibles** : risques généraux, indemnités de départ en retraite, provision pour amende, provision pour impôt sur les bénéfices, provision pour perte de change (en tenant compte des écarts de conversion) | Réintégrées (retraitement **temporaire** : déduction lors de la reprise) | Art. 39-1-5° CGI |
| **Intérêts de comptes courants d'associés excédentaires** | Déductibles seulement si le capital est **entièrement libéré** et dans la limite d'un **taux maximum** publié chaque année (sauf preuve d'un taux de marché entre entreprises liées) | Art. 39-1-3° et 212 CGI |
| **Quote-part de frais et charges (QPFC)** sur dividendes du régime mère-fille | 5 % du dividende brut ; **1 %** si la distributrice est membre du même groupe intégré | Art. 145 et 216 CGI |
| **Dons (mécénat)** | Le don est réintégré ; il ouvre droit à une **réduction d'impôt** | Art. 238 bis CGI |
| **Écarts de valeur liquidative** sur certains OPC, **quote-part de bénéfices de sociétés de personnes** non comptabilisée… | Réintégrations « techniques » | Art. 209-0 A, 238 bis K CGI |

### 2.2 Déductions courantes

| Retraitement | Règle | Référence |
|---|---|---|
| **Dividendes du régime mère-fille** | Déduits pour leur montant brut (titres nominatifs, ≥ 5 % du capital, conservés ≥ 2 ans), puis QPFC réintégrée | Art. 145 et 216 CGI |
| **Reprises de provisions** qui avaient été réintégrées à leur dotation | Déduites (sinon double imposition) | — |
| **Plus-values nettes à long terme** sur titres de participation | Déduites (taux 0 %) ; réintégration d'une QPFC de 12 % de la plus-value brute | Art. 219 I a quinquies CGI |
| **Crédit d'impôt recherche (CIR)**, crédit d'impôt innovation, créance de **carry-back** comptabilisés en produit | Non imposables → déduits | Art. 244 quater B, 220 quinquies CGI |
| **Régimes de faveur** : exonérations zonées (entreprises nouvelles en ZFRR…), plus-values de fusion/apport sous régime spécial, abattements spécifiques | Déduction de la fraction exonérée | Art. 44 sexies s., 210 A CGI |

> 💡 **Réflexe senior :** à l'IS, la distinction plus-value **court terme / long terme** n'a quasiment plus d'intérêt **sauf pour les titres de participation** (et le régime des brevets / logiciels — art. 238 CGI). La plus-value de cession d'un camion, d'une machine ou d'un terrain est taxée au **taux de droit commun**. À l'**IR** (BIC, BNC), au contraire, la distinction est essentielle (voir § 9).

### 2.3 Véhicules de tourisme : plafond d'amortissement

Plafond de la base amortissable (prix **TTC**, la TVA n'étant pas récupérable sur un véhicule de tourisme) — véhicules acquis depuis 2021, valeurs *à vérifier chaque année* :

| Émissions de CO₂ (WLTP) | Plafond |
|---|---|
| < 20 g/km | 30 000 € |
| 20 à 49 g/km | 20 300 € |
| 50 à 160 g/km | 18 300 € |
| > 160 g/km | 9 900 € |

> Note : le seuil de 130 g/km pour le plafond de 9 900 € était celui des véhicules mesurés en norme **NEDC** (ancienne norme) ; pour les véhicules mesurés en **WLTP** (immatriculés depuis 2021), le seuil est de **160 g/km**. Vérifiez la norme indiquée sur le certificat d'immatriculation.

```
Amortissement non déductible = dotation comptable × (prix TTC – plafond) / prix TTC
```

> ⚠️ **Erreur classique :** appliquer l'ancien seuil NEDC de 130 g à un véhicule WLTP. Un SUV à 158 g/km (WLTP) relève du plafond de **18 300 €**, pas de 9 900 €.

> ⚠️ **Erreur classique :** appliquer le plafond à un **véhicule utilitaire** (fourgon 3 places, N1) — il n'est pas concerné. À l'inverse, un **pick-up à double cabine (5 places)** est en principe un véhicule de tourisme au sens du CIBS : analysez la carte grise (genre, carrosserie, nombre de places), pas le libellé de la facture.

### 2.4 Exemple d'écriture du 2058-A (fil rouge)

| Ligne | Montant |
|---|---|
| Résultat comptable | 214 860 € |
| + IS comptabilisé | 39 400 € |
| + Amendes | 1 240 € |
| + Amortissement excédentaire véhicule | 3 450 € |
| – Dividendes mère-fille | – 12 000 € |
| + QPFC 5 % | 600 € |
| = … | … |

(Le cas complet est l'exercice E10-01.)

---

## 3. Les déficits

> 🟢 **En clair :** une perte fiscale peut réduire l'impôt des années suivantes (report en avant) ou, sur option, donner une créance sur l'impôt de l'année précédente (carry-back). Vous devez suivre ces pertes d'une année sur l'autre, sinon le client paie trop d'impôt.

### 3.1 Report en avant (art. 209 I CGI)

- **Sans limitation de durée.**
- **Plafond annuel d'imputation** : **1 000 000 €**, majoré de **50 %** de la fraction du bénéfice qui excède 1 000 000 €.
- La fraction non imputée reste reportable.

```
Exemple : bénéfice 1 640 000 €, déficits antérieurs 2 300 000 €
Imputation max = 1 000 000 + 50 % × (1 640 000 – 1 000 000) = 1 320 000 €
Bénéfice imposable = 320 000 € ; déficits restant à reporter = 980 000 €
```

- Perte du droit au report en cas de **changement d'activité réelle** (art. 221-5 CGI), notamment après une restructuration ; un simple changement d'actionnaires (levée de fonds) ne fait pas perdre les déficits.

### 3.2 Report en arrière — carry-back (art. 220 quinquies CGI)

- **Option** : le déficit de l'exercice N est imputé sur le bénéfice de **N-1 uniquement**.
- **Limite** : le plus faible entre (i) le bénéfice de N-1 et (ii) un **plafond légal** — **1 000 000 €** dans la rédaction de l'article que nous connaissons (*valeur à vérifier chaque année* : le plafond du carry-back a été modifié par le passé et fait régulièrement l'objet de projets de réduction ; certains supports de formation citent 200 000 €, contrôlez la version en vigueur avant tout conseil).
- Le bénéfice d'imputation **exclut** : la fraction distribuée, la fraction exonérée ou taxée à taux réduit spécifique, et la fraction ayant donné lieu à un IS **payé au moyen de crédits d'impôt** (CIR notamment).
- Effet : naissance d'une **créance** sur le Trésor = déficit reporté × taux de l'IS, **non imposable**, imputable sur l'IS des 5 exercices suivants puis remboursable, mobilisable auprès d'une banque.
- Option exercée sur la liasse de l'exercice déficitaire (imprimé 2039).

> 🟢 **En clair :** avec le carry-back, la perte de cette année est utilisée contre le bénéfice de l'année précédente. L'État ne rembourse pas tout de suite : il reconnaît une créance, que l'entreprise utilise pour payer son IS des 5 années suivantes, puis se fait rembourser.

| Compte | Débit | Crédit |
|---|---|---|
| 444 État — impôt sur les bénéfices (sous-compte « créance de carry-back ») | X | |
| 699 Produits — Reports en arrière des déficits | | X |

Puis **déduction extra-comptable** du produit sur le 2058-A.

> 💡 **Réflexe senior :** le carry-back ne « rembourse » pas un IS **payé avec du CIR** — c'est le piège classique des start-up (exercice E10-05).

---

## 4. Le calcul de l'IS

> 🟢 **En clair :** ici, on calcule l'impôt sur les sociétés : quel taux appliquer, quand le payer (4 acomptes puis un solde), et comment l'enregistrer. Exemple : quand C01 Boulangerie Dupain verse un acompte d'IS, il va en 444 (une avance à l'État), pas en charge.

### 4.1 Taux (art. 219 CGI)

| Tranche de bénéfice (par période de 12 mois) | Taux |
|---|---|
| 0 → 42 500 € (PME éligibles) | 15 % |
| Au-delà | 25 % |

**Conditions du taux réduit** (cumulatives) :
1. **CA HT < 10 M€** (ramené à 12 mois si l'exercice n'a pas 12 mois ; pour un groupe intégré : somme des CA des membres) ;
2. **capital entièrement libéré** ;
3. capital détenu de manière continue **à 75 % au moins par des personnes physiques** (ou par une société remplissant elle-même ces conditions).

**Exercice ≠ 12 mois** : le plafond de 42 500 € est **proratisé** : `42 500 × nombre de mois / 12`. Pour Studio Pixel (16 mois) : 56 666,67 €.

> ⚠️ **Erreur classique :** pour un premier exercice de 16 mois, appliquer 15 % sur 42 500 € « parce que c'est le plafond ». Le plafond suit la durée de l'exercice (dans les deux sens : 9 mois → 31 875 €).

### 4.2 Contribution sociale sur l'IS (art. 235 ter ZC CGI)

- **3,3 %** de l'IS (calculé au taux normal et réduit) **diminué d'un abattement de 763 000 €**.
- Seules les entreprises dont le CA ≥ 7 630 000 € sont concernées (les PME remplissant les conditions du taux réduit en sont exonérées). En pratique : IS > 763 000 €, donc bénéfice > ≈ 3 M€.
- Pour les très grandes entreprises (CA ≥ 1 Md€), une **contribution exceptionnelle sur les bénéfices** a été instituée par la loi de finances 2025 : *périmètre, taux et durée à vérifier chaque année*.

### 4.3 Acomptes et solde (art. 1668 CGI)

| Élément | Règle |
|---|---|
| Nombre | 4 acomptes |
| Dates (clôture 31/12) | **15/03, 15/06, 15/09, 15/12** (en général : le 15 du 3e, 6e, 9e et 12e mois de l'exercice) |
| Montant | ¼ de l'IS calculé sur le **bénéfice de référence** (dernier exercice clos), **avant imputation des crédits et réductions d'impôt** ; bénéfice ramené à 12 mois si l'exercice de référence n'a pas 12 mois |
| Acompte du 15/03 | Calculé sur l'**avant-dernier** exercice (la liasse du dernier n'est pas encore déposée) ; **régularisé** avec l'acompte du 15/06 |
| Dispense | IS de référence **≤ 3 000 €** ; **premier exercice** d'une société nouvelle |
| Formulaire | Relevé d'acompte **2571** (télérèglement obligatoire) |
| Modulation | Possible si l'entreprise estime que les acomptes versés couvrent l'IS final ; en cas d'erreur : majoration et intérêt de retard (art. 1731 A CGI) |
| Solde | **15 du 4e mois** suivant la clôture (15/05 pour une clôture au 31/12), relevé de solde **2572** ; excédent d'acomptes remboursé dans les 30 jours |

```
Acompte n° 2 (15/06/N+1) = 2 × ¼ IS(N) – acompte n° 1 déjà versé (calculé sur N-1)
```

### 4.4 Comptabilisation de l'IS

| Opération | Débit | Crédit |
|---|---|---|
| Versement d'un acompte | 444 État — IS | 512 Banque |
| Constatation de l'IS de l'exercice | 695 Impôts sur les bénéfices | 444 État — IS |
| Réduction d'impôt mécénat / crédit d'impôt imputé | 444 État — IS | 695 (sous-compte) ou 699 / 74 selon le cas |
| Paiement du solde | 444 | 512 |

> ⚠️ **Erreur classique :** passer les acomptes en 695 au fil de l'eau « parce que c'est de l'IS ». En cours d'année, l'acompte est une **avance** (444). Si le client l'a fait, on corrige à la clôture, sinon la charge d'IS est faussée.

> 💡 **Réflexe senior :** dans un **groupe intégré**, la filiale ne paie pas l'IS au Trésor : elle verse sa contribution à la **société mère** selon la **convention d'intégration**. La contrepartie de 695 est alors un compte de groupe (451) et non 444 — la mère seule dépose le 2571/2572 du groupe.

---

## 5. Crédits et réductions d'impôt

> 🟢 **En clair :** certaines dépenses font baisser directement l'impôt : la recherche (CIR), l'innovation (CII), les dons (mécénat). Exemple : C08 TechNova, l'éditeur de logiciel, en bénéficie. Point clé : un crédit d'impôt n'est pas imposable, on le retire du résultat fiscal.

| Dispositif | Base | Taux (*à vérifier chaque année*) | Points clés |
|---|---|---|---|
| **CIR** (art. 244 quater B) | Dépenses de **recherche** (personnel chercheurs/techniciens au prorata du temps, amortissements des matériels de recherche, forfait de fonctionnement, sous-traitance agréée), **moins les subventions** reçues pour ces opérations | 30 % jusqu'à 100 M€ ; forfait de fonctionnement retenu : 40 % des dépenses de personnel + 75 % des dotations aux amortissements | Imputé sur l'IS de l'année ; excédent remboursable après 3 ans ou **immédiatement** pour les PME (définition UE), JEI, entreprises nouvelles ou en difficulté ; déclaration **2069-A** ; **dossier justificatif** (état de l'art, verrous, temps passés) |
| **CII** (crédit d'impôt innovation) | Conception de prototypes / installations pilotes de produits nouveaux, PME uniquement, plafond de dépenses 400 000 € | 20 % (réduit par la LF 2025 ; *à vérifier*) | Ne pas confondre R&D (lever une incertitude scientifique) et innovation (produit nouveau sur le marché) |
| **Mécénat** (art. 238 bis) | Dons à des organismes d'intérêt général | 60 % (40 % au-delà de 2 M€) | Plafond : 20 000 € ou 5 ‰ du CA HT si plus élevé ; excédent reportable 5 ans ; reçu fiscal ; don **réintégré** sur le 2058-A |

**Comptabilisation du CIR — deux présentations admises :**

| Option | Écriture | Effet |
|---|---|---|
| **Diminution de l'IS** | 444 / 699 (sous-compte « crédits d'impôt ») ou 444 / 695 | Le résultat d'exploitation n'est pas modifié ; présentation fiscale « pure » |
| **Subvention** | 444 / 74 (subvention d'exploitation) | Améliore le résultat d'exploitation et l'EBE (présentation proche des IFRS, appréciée des investisseurs) |

Dans les deux cas le CIR est **non imposable** : s'il est en produit (74 ou 699), on le **déduit** sur le 2058-A ; s'il est porté au crédit du 695, la réintégration de l'IS se fait pour le montant net. **Choisissez une méthode, appliquez-la de façon permanente et décrivez-la en annexe.**

> 🟢 **En clair :** le CIR n'est jamais imposé, quelle que soit la façon de l'enregistrer. Choisissez une seule présentation, gardez-la chaque année et expliquez-la dans l'annexe.

---

## 6. Les impôts locaux et taxes annexes

> 🟢 **En clair :** en plus de l'IS, l'entreprise paie des impôts locaux et des taxes : CFE, CVAE, taxes sur les salaires, taxes sur les voitures de tourisme. Ce sont souvent eux que l'on oublie dans les charges à payer à la clôture.

### 6.1 CFE (cotisation foncière des entreprises)

- **Base** : valeur locative des biens passibles de taxe foncière utilisés pour l'activité au cours de **N-2** (abattement de 50 % pour les établissements industriels).
- **Cotisation minimum** : base minimum fixée par la commune selon des tranches de CA (*barème indexé chaque année — à vérifier*) ; **exonération** de la cotisation minimum si CA ≤ 5 000 €.
- **Création** : **exonération l'année de création** ; l'année suivante, base = biens au **31/12 de l'année de création**, **réduite de moitié** ; la 2e année suivant la création, même base sans réduction (art. 1478 II CGI). Déclaration **1447-C** avant le 31/12 de l'année de création.
- **Paiement** : 15/12 (acompte au 15/06 si la CFE N-1 ≥ 3 000 €) ; avis en ligne dans l'espace professionnel début novembre.
- **Plafonnement** CFE + CVAE en fonction de la valeur ajoutée (taux *à vérifier*), sur demande.
- Charge **déductible** (compte 635 — subdivision selon la nomenclature 2025 du PCG).

> 🟢 **En clair :** la CFE dépend des locaux utilisés deux ans plus tôt. Une société nouvelle ne la paie pas l'année de sa création, puis paie sur une base réduite de moitié l'année suivante. Pensez-y pour une société récente comme C25 Studio Pixel.

### 6.2 CVAE

- Due par les entreprises dont le CA HT > 500 000 € (déclaration 1330-CVAE dès 152 500 €).
- **Suppression progressive** : le calendrier a été modifié par les lois de finances successives. **Taux maximal retenu pour 2026 dans ce module : 0,19 %** de la valeur ajoutée (*valeur à vérifier chaque année*), plus taxe additionnelle et frais.
- Acomptes 15/06 et 15/09 si CVAE N-1 > 1 500 € ; charge déductible.

### 6.3 Taxes et participations assises sur les salaires

| Taxe | Taux / seuil (*à vérifier*) | Modalités |
|---|---|---|
| Taxe d'apprentissage | 0,68 % (0,59 % part principale mensuelle + 0,09 % solde annuel) | DSN, collectée par l'URSSAF |
| Contribution à la formation professionnelle (CFP) | 0,55 % (< 11 salariés) / 1 % (≥ 11) | DSN |
| Contribution supplémentaire à l'apprentissage (CSA) | Entreprises ≥ 250 salariés sous quota d'alternants | DSN |
| CPF-CDD | 1 % des salaires des CDD | DSN |
| PEEC (« 1 % logement ») | 0,45 % — entreprises ≥ 50 salariés | DSN |
| **Taxe sur les salaires** | Barème progressif | Employeurs **non assujettis à la TVA** ou assujettis partiels (médecin employeur, association, holding à prorata faible — Delta Invest) |

### 6.4 Taxes annuelles sur les véhicules de tourisme (ex-TVS)

Depuis 2022 (CIBS, art. L. 421-93 s.), deux taxes pour les véhicules de tourisme utilisés à des fins économiques :
1. **Taxe annuelle sur les émissions de CO₂** — barème progressif par gramme (WLTP) ;
2. **Taxe annuelle sur les émissions de polluants atmosphériques** — selon la catégorie (électrique/hydrogène : 0 € ; essence, gaz, hybrides récents : 100 € ; autres dont diesel : 500 € — *valeurs à vérifier*).

- **Prorata** : nombre de jours d'affectation / nombre de jours de l'année.
- Déclaration et paiement **en janvier N+1** (annexe 3310-A de la CA3 ; CA12 pour le réel simplifié).
- **Non déductibles** du résultat imposable → réintégration.
- Charge de l'exercice d'utilisation (charge à payer au 31/12).

---

## 7. La liasse fiscale et le calendrier

> 🟢 **En clair :** la liasse fiscale, c'est le paquet de formulaires envoyé chaque année aux impôts. Le formulaire dépend du régime du client, et les dates limites sont fixes. Exemple : C04 Le Petit Zinc clôture au 30/06, sa liasse est due 3 mois après, au 30/09.

| Régime | Imprimés |
|---|---|
| IS réel normal | 2065 + **2050 à 2059** (2050-2051 bilan, 2052-2053 compte de résultat, 2054-2056 immobilisations/amortissements/provisions, 2057 échéances, **2058-A/B/C**, 2059-A à G : plus-values, filiales, capital) |
| IS réel simplifié | 2065 + **2033-A à G** |
| BIC à l'IR (EURL non optante, LMNP) | **2031** + 2050s ou 2033s |
| BNC | **2035** + 2035-A/B |
| SCI à l'IR | **2072** (puis 2044 de chaque associé) |
| Bénéfice agricole | **2139** (simplifié) / 2143 (normal) — voir M13 |
| Intégration fiscale | Liasse de groupe (2058-A-bis, 2058-ES…) — voir M13 |

**Échéances** : clôture au 31/12 → **2e jour ouvré suivant le 1er mai** (+ 15 jours en télétransmission EDI, *à vérifier*) ; autres clôtures → **3 mois après la clôture**. Solde d'IS au 15 du 4e mois.

> 💡 **Réflexe senior :** les seuils réel simplifié / réel normal (CA) sont revalorisés tous les trois ans — vérifiez-les et documentez le régime de chaque client dans sa fiche permanente.

---

## 8. Intégration fiscale (principes — détail en M13)

> 🟢 **En clair :** dans un groupe, la société mère peut payer un seul IS pour elle et ses filiales détenues à 95 % ou plus. Les pertes de l'une compensent les bénéfices de l'autre. Exemple : C10 Delta Invest avec C02 Bâtisseurs du Sud et C24 Menuiserie Bois & Création.

- Société mère détenant **≥ 95 %** des filiales (directement ou indirectement), **même date de clôture**, exercices de 12 mois, **option pour 5 ans**.
- Chaque société calcule son **résultat individuel** (2058-A) comme si elle était seule ; la mère calcule le **résultat d'ensemble** (somme algébrique) après **neutralisations** (provisions intra-groupe, cessions d'immobilisations intra-groupe, abandons de créances, subventions, etc.).
- La **mère est seule redevable** de l'IS du groupe (acomptes, solde, contribution sociale), des crédits d'impôt imputés et du taux réduit (CA = somme des CA du groupe).
- **QPFC à 1 %** sur les dividendes intra-groupe.
- **Convention d'intégration** : fixe ce que chaque filiale verse à la mère (le plus souvent : convention de **neutralité**, la filiale verse l'IS qu'elle aurait payé seule ; l'économie liée aux déficits reste chez la mère).

Dans le portefeuille : **Delta Invest (C10)**, tête de groupe avec **Bâtisseurs du Sud (C02)** et **Menuiserie Bois & Création (C24)**.

---

## 9. Les autres régimes d'imposition

> 🟢 **En clair :** tous vos clients ne paient pas l'IS. Les entrepreneurs individuels, certaines EURL, les SCI et les micro-entrepreneurs sont imposés à l'impôt sur le revenu, au nom de la personne. Chaque cas a son formulaire : 2031, 2035, 2072, ou la déclaration simplifiée du micro-entrepreneur (C17 Paul Durand).

### 9.1 BIC à l'IR (2031) — EURL non optante, entreprise individuelle, LMNP

- Le résultat est imposé **au nom de l'exploitant** (2042-C-PRO), au barème de l'IR, et soumis aux cotisations sociales.
- **Non déductibles** : la **rémunération de l'exploitant** (ses prélèvements → compte 108), sa **CSG non déductible (2,4 %) et CRDS (0,5 %)**, l'IR.
- **Déductibles** : cotisations sociales obligatoires (SSI) **versées** dans l'année ; contrats « Madelin » / PER dans les limites légales (art. 154 bis CGI).
- **Plus-values professionnelles** : court terme (≤ 2 ans de détention ou à hauteur des amortissements déduits) taxées au barème, avec étalement possible sur 3 ans ; long terme taxées à **12,8 %** (+ prélèvements sociaux) ; exonérations art. 151 septies, 238 quindecies…
- **LMNP au réel** : l'amortissement ne peut pas **créer ni augmenter un déficit** (art. 39 C CGI) → excédent = **amortissements réputés différés (ARD)**, reportables sans limite de durée. Depuis la LF 2025, les amortissements déduits sont **réintégrés dans le calcul de la plus-value privée** de cession (hors exceptions — *modalités à vérifier*). Statut LMP si recettes > 23 000 € **et** > autres revenus d'activité du foyer.

> 🟢 **En clair :** en location meublée au réel (C23 M. et Mme Bernard), l'amortissement ne peut pas créer de perte. La part non utilisée est mise de côté (ARD) et servira les années suivantes.

### 9.2 BNC — déclaration contrôlée (2035)

- **Comptabilité de trésorerie** : recettes **encaissées** / dépenses **payées** dans l'année civile (option possible pour les créances-dettes).
- Exception : les immobilisations sont **amorties** (pas de déduction du prix payé).
- Médecin : recettes = télétransmissions CPAM + tiers payant complémentaire + paiements patients + forfaits (ROSP, forfait patientèle) ; **contrôle par le relevé SNIR** (actes de l'année, en date de soins → rapprochement avec les encaissements).
- **SCM** : on déduit la **quote-part réelle** des frais de la SCM (selon la 2036), pas les appels de fonds.
- **Véhicule** : frais réels **ou** barème kilométrique (qui couvre carburant, entretien, assurance, amortissement ; on y ajoute péages, parking, intérêts d'emprunt au prorata professionnel).
- **Cotisations** : CARMF, URSSAF déductibles, sauf CSG non déductible et CRDS.

### 9.3 Revenus fonciers (2072 — SCI à l'IR)

- Pas d'amortissement ; recettes et dépenses **payées**.
- **Déductibles** : travaux d'**entretien, de réparation et d'amélioration** (locaux d'habitation), intérêts et assurance emprunteur, taxe foncière (hors TEOM récupérée), assurance PNO, frais de gestion (réels + forfait de 20 € par local), provisions de copropriété (avec régularisation N+1).
- **Non déductibles** : travaux de **construction, reconstruction, agrandissement** (création de surface habitable).
- **Déficit foncier** : la part issue des charges **autres que les intérêts** s'impute sur le revenu global de chaque associé dans la limite de **10 700 €** par an (plafond majoré de 21 400 € pour certains travaux de rénovation énergétique sur une période limitée — *à vérifier*) ; le surplus et la part issue des intérêts s'imputent sur les revenus fonciers des **10 années** suivantes. Condition : maintien de la location jusqu'au 31/12 de la 3e année suivant l'imputation.

> 🟢 **En clair :** quand les charges d'une SCI dépassent ses loyers (déficit foncier), une partie de ce déficit réduit les autres revenus de chaque associé, dans une limite annuelle. Le reste attend les loyers des 10 années suivantes.

### 9.4 Micro-entreprise

| Activité | Plafond de CA 2026 (*à vérifier*) | Abattement forfaitaire |
|---|---|---|
| Vente de marchandises, hébergement (hors meublés de tourisme non classés) | 203 100 € | 71 % |
| Prestations de services BIC | 83 600 € | 50 % |
| BNC | 83 600 € | 34 % |
| Meublés de tourisme **non classés** | 15 000 € | 30 % |
| Location meublée longue durée et meublés de tourisme classés | 77 700 € (ou montant revalorisé) | 50 % |

- Abattement minimum de 305 €. Sortie du régime après **deux années consécutives** de dépassement (au 1er janvier suivant).
- Cotisations sociales en % du CA encaissé (BNC relevant de la SSI : **26,1 %** en 2026 — *à vérifier*), option possible pour le **versement libératoire** de l'IR (sous condition de revenu fiscal de référence).
- La franchise en base de TVA est un régime **distinct** (seuils propres — voir M04).

### 9.5 Bénéfice agricole

Régime micro-BA, réel simplifié (2139) ou normal (2143) ; stocks vivants, DEP, aides PAC → **voir M13** (EARL Ferme du Val).

---

## 10. Le contrôle fiscal

> 🟢 **En clair :** quand l'administration fiscale contrôle un client, les délais sont stricts et les pénalités peuvent être lourdes. Votre rôle : noter les dates, vérifier que la procédure est respectée, puis seulement discuter le fond.

### 10.1 Les procédures

| Procédure | Où | Caractéristiques |
|---|---|---|
| Contrôle sur pièces | Au bureau de l'administration | Demandes de renseignements, de justifications |
| **Examen de comptabilité** | À distance, sur le **FEC** | Pas de déplacement du vérificateur |
| **Vérification de comptabilité** | Dans l'entreprise | **Avis de vérification** + **charte des droits et obligations du contribuable vérifié** ; assistance d'un conseil ; débat oral et contradictoire ; durée sur place limitée à **3 mois** pour les petites entreprises (CA sous les seuils de l'art. L. 52 LPF), **sauf** notamment en cas de **graves irrégularités privant la comptabilité de valeur probante**, qui doivent alors être notifiées dans la proposition de rectification |

### 10.2 Délai de reprise (art. L. 169 et L. 176 LPF)

- **IS / IR (BIC, BNC)** : jusqu'au **31/12 de la 3e année** suivant celle au titre de laquelle l'imposition est due (année de clôture). Exercice clos le 30/06/2023 → reprise possible jusqu'au 31/12/2026.
- **TVA** : jusqu'au **31/12 de la 3e année** suivant celle au cours de laquelle la taxe est **devenue exigible**. TVA de juillet-décembre 2022 → prescrite au 31/12/2025, **même si l'exercice comptable chevauche 2023**.
- Délai porté à 10 ans en cas d'activité occulte ; la proposition de rectification **interrompt** la prescription.

### 10.3 La procédure de rectification contradictoire

```
Avis de vérification → interventions sur place → débat oral
→ PROPOSITION DE RECTIFICATION (motivée, art. L. 57 LPF)
   └─ 30 jours pour répondre (+ 30 jours sur demande avant l'expiration du premier délai)
→ Observations du contribuable
→ Réponse de l'administration (PME : 60 jours, sinon observations réputées acceptées — art. L. 57 A LPF)
→ Recours : supérieur hiérarchique, puis interlocuteur départemental
→ Commission départementale des impôts (questions de FAIT : reconstitution de recettes, montant d'une charge…)
→ Mise en recouvrement → réclamation contentieuse → tribunal administratif
```

### 10.4 Pénalités et intérêts

| Sanction | Taux | Référence |
|---|---|---|
| Intérêt de retard | **0,20 % par mois** (2,4 % par an) | Art. 1727 CGI |
| Retard de déclaration | 10 % (40 % / 80 % après mise en demeure) | Art. 1728 CGI |
| **Manquement délibéré** | **40 %** (charge de la preuve : administration) | Art. 1729 CGI |
| Abus de droit / manœuvres frauduleuses | 80 % | Art. 1729 CGI |
| Défaut de paiement / acompte insuffisant | 5 % | Art. 1731 CGI |

> 💡 **Réflexe senior :** le jour où un client reçoit une proposition de rectification, notez **la date de réception** (pas la date du courrier), calculez immédiatement le **délai de 30 jours**, demandez la **prorogation** par écrit si le dossier est lourd, et vérifiez d'abord la **régularité de la procédure** (avis, charte, durée, prescription, motivation) avant le fond.

---

## 11. Le dirigeant : rémunération ou dividendes ?

> 🟢 **En clair :** question fréquente des dirigeants : vaut-il mieux se verser un salaire ou des dividendes ? Il n'y a pas de réponse unique. Il faut comparer l'impôt de la société, les charges sociales, l'impôt personnel et la protection sociale.

| Critère | Rémunération (président SAS, gérant) | Dividendes |
|---|---|---|
| Effet sur l'IS | **Déductible** | Payés après IS (non déductibles) |
| Charges sociales | Oui (assimilé salarié ≈ 75-80 % du net ; TNS ≈ 40-45 % du revenu) | Non en SAS ; **oui en SARL/SELARL** pour le gérant majoritaire au-delà de 10 % du capital + primes + CCA |
| Imposition personnelle | Barème IR après abattement de 10 % | **PFU** : 12,8 % IR + prélèvements sociaux (**18,6 %** après la hausse de CSG de la LFSS 2026 — *à vérifier*), ou option globale pour le barème avec abattement de 40 % |
| Droits sociaux | Retraite, prévoyance, (pas de chômage pour un mandataire) | Aucun |

> ⚠️ **Erreur classique :** conseiller « tout en dividendes » sans parler de la protection sociale, ni du fait que la société paie d'abord l'IS.

---

## Checklist de fin de module

- [ ] Je tiens un tableau de passage avec retraitements définitifs / temporaires et je suis les provisions non déductibles d'une année sur l'autre.
- [ ] Je vérifie les trois conditions du taux réduit et je proratise le plafond si l'exercice ≠ 12 mois.
- [ ] J'applique le plafond « 1 M€ + 50 % » aux déficits et je mets à jour le 2058-B.
- [ ] Je sais calculer l'échéancier des acomptes (y compris la régularisation du 15/06) et le solde 2572.
- [ ] Je contrôle que les acomptes sont en 444 (ou 451 en groupe intégré) et non en 695.
- [ ] Je déduis le CIR, la créance de carry-back et les dividendes mère-fille ; je réintègre la QPFC (5 % / 1 %).
- [ ] Je calcule l'amortissement excédentaire et les taxes annuelles des véhicules de tourisme.
- [ ] Je sais contrôler un avis de CFE (année de création, réduction de moitié, base minimum).
- [ ] Je sais établir une 2035, une 2072, une 2031 et gérer les ARD d'un LMNP.
- [ ] Je sais comparer micro / réel / société pour un client.
- [ ] Face à une proposition de rectification : date de réception, délais, prescription, régularité, puis fond.
- [ ] J'ai mis à jour la fiche « chiffres clés » de l'année et toutes mes valeurs « à vérifier ».

## À retenir en 30 secondes

- Résultat fiscal = résultat comptable + réintégrations – déductions, calculé sur la 2058-A (ou la 2033-B), sans écriture comptable.
- Suivez d'une année sur l'autre les ajustements temporaires (provisions non déductibles) : c'est là que l'on oublie des déductions.
- IS : 15 % jusqu'à 42 500 € de bénéfice pour les PME qui remplissent les conditions, 25 % au-delà ; la tranche à 15 % suit la durée de l'exercice.
- En cours d'année, les acomptes d'IS vont en 444 (une avance), jamais en 695.
- Une perte se reporte sur les bénéfices futurs (avec un plafond), ou sur l'année précédente sur option (carry-back).
- N'oubliez pas les autres impôts : CFE, CVAE, taxes sur les salaires, taxes sur les voitures de tourisme.
- Contrôle fiscal : notez la date de réception, comptez les 30 jours, vérifiez la procédure avant le fond. Et revérifiez chaque année les chiffres « à vérifier ».
