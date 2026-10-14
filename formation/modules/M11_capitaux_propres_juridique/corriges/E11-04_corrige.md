# Corrigé E11-04 — Boulangerie Dupain : affectation du résultat, dividendes et 2777

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-04](../exercices/E11-04_affectation-resultat-boulangerie-dupain.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Ordre de travail d'une affectation** : (1) réserve légale (et statutaire) ; (2) apurement des pertes antérieures s'il y en a ; (3) bénéfice distribuable ; (4) choix des associés (dividendes, réserves facultatives, report à nouveau) ; (5) fiscalité et social des dividendes ; (6) déclarations.

**Erreurs du projet de PV (question 1)**

| # | Erreur | Correction |
|---|---|---|
| 1 | Réserve légale dotée de **5 % du bénéfice (3 569 €)** | La réserve légale est **plafonnée à 10 % du capital** (2 000 €). Elle est déjà de 1 650 € : la dotation est limitée à **350 €**. Doter 3 569 € n'est pas illégal, mais au-delà de 350 € ce n'est plus de la réserve « légale » : l'excédent doit aller en réserve facultative ou en report à nouveau, sinon il est rendu indisponible sans raison. |
| 2 | « Versés **nets du prélèvement forfaitaire unique de 30 %**, soit 31 500 € » | Le PFU n'est pas « retenu » en bloc par la société : la société retient le **PFNL de 12,8 %** (acompte d'IR, sauf dispense) et les **prélèvements sociaux** (18,6 % selon nos informations — *à vérifier*) ; la fraction des dividendes de Marc excédant 10 % de sa quote-part de capital n'est **pas** soumise aux prélèvements sociaux mais aux **cotisations sociales des indépendants**. Julie est dispensée de PFNL. Le net versé n'est donc pas de 31 500 €. Le montant des retenues n'a d'ailleurs pas à figurer dans la résolution. |
| 3 | Report à nouveau **2 811 €** | Conséquence de l'erreur 1 : avec une dotation de 350 €, le solde affecté au report à nouveau est de **6 030 €**. |
| 4 | Le report à nouveau antérieur (10 350 €) n'est pas mentionné | La résolution doit présenter l'**origine** des sommes (bénéfice + report antérieur) pour justifier que la distribution est couverte par le bénéfice distribuable. |
| 5 | Mention des dividendes antérieurs | La mention des distributions des **trois exercices précédents** est obligatoire (art. 243 bis CGI) : elle doit être **exacte** (montants et éligibilité à l'abattement de 40 %). Le cabinet vérifie dans les PV antérieurs ; si des dividendes ont été versés, la mention « aucun dividende » est fausse. |

**Pourquoi Julie et Marc ne sont pas traités de la même façon** :
- **Julie** (40 %, salariée, sœur de Marc — ni conjointe ni partenaire de PACS) : dividendes « ordinaires » → prélèvements sociaux retenus par la société ; **PFNL non retenu** grâce à sa dispense déposée **avant le 30/11/2026** pour les revenus versés en 2027.
- **Marc** (60 %, **gérant majoritaire** de SARL → travailleur indépendant) : règle de l'art. L. 131-6 CSS. La fraction de ses dividendes qui dépasse **10 % du capital social, des primes et des comptes courants qu'il détient** (lui, son conjoint/partenaire de PACS, ses enfants mineurs) est soumise aux **cotisations sociales TNS**. Le seuil se calcule sur **sa** quote-part : 10 % × 12 000 € = **1 200 €** (et non 10 % × 20 000 €). Julie, sa sœur, n'entre pas dans le calcul.

## 2. Calculs (détaillés, chaque montant justifié)

**Réserve légale**
- 5 % × 71 380,00 = 3 569,00 € (dotation théorique).
- Plafond : 10 % × 20 000 = 2 000,00 € ; déjà constituée : 1 650,00 € ; manquant : **350,00 €**.
- Dotation retenue : min(3 569,00 ; 350,00) = **350,00 €**. Après dotation, la réserve légale est complète (2 000 €) : plus de dotation obligatoire les années suivantes tant que le capital ne change pas.

**Bénéfice distribuable**

| Élément | Montant |
|---|---|
| Bénéfice 2026 | 71 380,00 |
| – Pertes antérieures | 0,00 |
| – Dotation à la réserve légale | – 350,00 |
| + Report à nouveau créditeur antérieur | + 10 350,00 |
| **= Bénéfice distribuable** | **81 380,00** |
| + Réserves disponibles (autres réserves, sur décision expresse) | + 100 000,00 |
| **= Maximum distribuable** | **181 380,00** |

45 000 € ≤ 81 380 € : la distribution est couverte par le **bénéfice distribuable** (sans prélèvement sur les réserves). Contrôle complémentaire : après distribution, capitaux propres = 203 380 – 45 000 = 158 380 € > capital + réserve légale (22 000 €) ✓.

**Affectation proposée (en conservant les choix de Marc)**

| Affectation | Montant |
|---|---|
| Réserve légale | 350,00 |
| Autres réserves (réserve facultative) | 20 000,00 |
| Dividendes | 45 000,00 |
| Report à nouveau (solde du bénéfice) | 6 030,00 |
| **Total = bénéfice 2026** | **71 380,00** |

Report à nouveau après affectation : 10 350 + 6 030 = **16 380,00 €**.

**Dividendes par associé** (2 000 parts → 22,50 € par part)

| | Marc (1 200 parts) | Julie (800 parts) | Total |
|---|---|---|---|
| Dividende brut | 27 000,00 | 18 000,00 | 45 000,00 |
| Seuil 10 % (quote-part de capital détenue) | 10 % × 12 000 = 1 200,00 | sans objet | |
| Fraction soumise aux prélèvements sociaux | 1 200,00 | 18 000,00 | |
| Fraction soumise aux cotisations TNS | 25 800,00 | — | |
| PFNL 12,8 % (retenu) | 27 000 × 12,8 % = 3 456,00 | 0,00 (dispense) | 3 456,00 |
| Prélèvements sociaux 18,6 % (retenus) | 1 200 × 18,6 % = 223,20 | 18 000 × 18,6 % = 3 348,00 | 3 571,20 |
| **Net versé** | **23 320,80** | **14 652,00** | **37 972,80** |

Contrôle : 45 000,00 – 3 456,00 – 3 571,20 = 37 972,80 ✓.

**Cotisations sociales de Marc sur la fraction > 10 %** (non retenues par la société, déclarées par Marc sur sa déclaration de revenus d'indépendant au printemps 2028 au titre de 2027) : estimation 25 800 × 40 % = **10 320,00 €** (*taux global retenu pour l'estimation, à vérifier*).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 27/05/2027 | OD | 120 | Résultat de l'exercice (bénéfice) | Affectation résultat 2026 – AGO 27/05/2027 | 71 380,00 | |
| 27/05/2027 | OD | 1061 | Réserve légale | Dotation (plafond 10 % du capital) | | 350,00 |
| 27/05/2027 | OD | 1068 | Autres réserves | Réserve facultative | | 20 000,00 |
| 27/05/2027 | OD | 457 | Associés – dividendes à payer | Dividendes 22,50 €/part (M. 27 000 / J. 18 000) | | 45 000,00 |
| 27/05/2027 | OD | 110 | Report à nouveau (solde créditeur) | Solde du bénéfice | | 6 030,00 |
| 10/06/2027 | BQ | 457 | Associés – dividendes à payer | Paiement dividendes 2026 | 45 000,00 | |
| 10/06/2027 | BQ | 4422 | Prélèvements forfaitaires non libératoires | PFNL 12,8 % M. Dupain (J. Dupain dispensée) | | 3 456,00 |
| 10/06/2027 | BQ | 4423 | Retenues et prélèvements sur distributions | Prélèvements sociaux 18,6 % (M. 223,20 / J. 3 348,00) | | 3 571,20 |
| 10/06/2027 | BQ | 512 | Banque | Vir. dividendes nets M. Dupain 23 320,80 / J. Dupain 14 652,00 | | 37 972,80 |
| 15/07/2027 | BQ | 4422 | Prélèvements forfaitaires non libératoires | 2777 – juin 2027 | 3 456,00 | |
| 15/07/2027 | BQ | 4423 | Retenues et prélèvements sur distributions | 2777 – juin 2027 | 3 571,20 | |
| 15/07/2027 | BQ | 512 | Banque | Télérèglement 2777 – juin 2027 | | 7 027,20 |
| | | | | **Totaux** | **123 407,20** | **123 407,20** |

> Subdivisions 4422 / 4423 à adapter au plan de comptes du cabinet. Les cotisations TNS de Marc sur la fraction > 10 % ne donnent lieu à **aucune écriture** au moment du paiement des dividendes ; elles seront appelées par l'URSSAF sur la base de sa déclaration de revenus. Si la société les prend en charge (pratique fréquente pour les cotisations du gérant), elles constituent un élément de sa rémunération, à traiter comme tel.

**Résolution corrigée (question 3)**

> **Deuxième résolution — Affectation du résultat.** L'assemblée générale, sur proposition de la gérance, constatant que le bénéfice de l'exercice clos le 31 décembre 2026 s'élève à 71 380,00 € et que le report à nouveau antérieur créditeur est de 10 350,00 €, décide d'affecter le bénéfice de l'exercice de la manière suivante :
> - à la réserve légale : 350,00 €, portant celle-ci à 2 000,00 €, soit le dixième du capital social ;
> - au poste « autres réserves » : 20 000,00 € ;
> - à titre de dividendes aux associés : 45 000,00 €, soit 22,50 € par part sociale ;
> - au report à nouveau : 6 030,00 €, portant celui-ci à 16 380,00 €.
>
> Les dividendes seront mis en paiement le 10 juin 2027. Il est rappelé que les dividendes perçus par les associés personnes physiques sont, lors de leur paiement, soumis au prélèvement forfaitaire non libératoire prévu à l'article 117 quater du CGI, sauf dispense, et aux prélèvements sociaux, sous réserve des dispositions de l'article L. 131-6 du Code de la sécurité sociale, et qu'ils sont éligibles, en cas d'option pour le barème progressif, à l'abattement de 40 % prévu à l'article 158, 3-2° du CGI.
>
> Conformément à l'article 243 bis du CGI, l'assemblée prend acte des dividendes distribués au titre des trois exercices précédents : [à compléter d'après les PV des exercices 2023, 2024 et 2025].
>
> *Cette résolution est adoptée à l'unanimité.*

## 4. Points d'attention / pièges

- **Réserve légale plafonnée** : vérifiez toujours le solde existant avant de calculer 5 %.
- **Seuil de 10 % = quote-part détenue** par le gérant et sa famille proche (capital + primes + comptes courants), pas le capital total. Si Marc avait un compte courant, le seuil augmenterait (10 % du compte courant détenu) — *modalité d'appréciation du compte courant (solde ou moyenne) à vérifier*.
- **La fraction > 10 %** : PFNL 12,8 % **oui** (c'est de l'IR), prélèvements sociaux **non** (remplacés par les cotisations TNS). Erreur fréquente : appliquer 31,4 % sur tout, ce qui fait payer deux fois les cotisations sociales.
- **Dispense de PFNL** : valable seulement si la demande a été faite **avant le 30 novembre** de l'année précédant le paiement ; elle ne dispense **jamais** des prélèvements sociaux.
- **2777** : à déposer **au plus tard le 15 du mois suivant le paiement** (ici le 15/07/2027), même si aucune somme n'était due au titre du PFNL.
- **« PFU 30 % »** : taux 2018-2025. Pour les revenus de 2026 et suivants, le taux global serait de 31,4 % selon nos informations (CSG relevée par la LFSS 2026) — *à vérifier avant tout chiffrage communiqué au client*.
- **Trésorerie** : 104 600 € en banque au 30/04/2027 ; décaissement total 45 000 € (37 972,80 € le 10/06 + 7 027,20 € le 15/07) : compatible, mais vérifier les échéances de mai-juillet (solde d'IS au 15/05, emprunt, crédit-bail).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Calendrier (question 6)**

| Date | Action | Qui |
|---|---|---|
| Au plus tard le 12/05/2027 | Envoi de la convocation et des documents (comptes, texte des résolutions) 15 jours avant l'AGO | Cabinet / gérant |
| 27/05/2027 | AGO (dans le délai de 6 mois : avant le 30/06/2027) | Associés |
| Avant le 27/06/2027 (ou 27/07 en ligne) | Dépôt des comptes et du PV d'affectation au greffe (option de confidentialité du compte de résultat si petite entreprise) | Cabinet |
| 10/06/2027 | Paiement des dividendes (≤ 9 mois après la clôture : avant le 30/09/2027) | Société |
| **15/07/2027** | **2777** : déclaration et télépaiement de 3 456,00 € (PFNL) + 3 571,20 € (prélèvements sociaux) | Cabinet |
| Avant le 15/02/2028 | **IFU** (2561) : déclaration par bénéficiaire des revenus distribués 2027 et des prélèvements | Cabinet |
| Printemps 2028 | Déclaration des revenus 2027 : Marc déclare ses dividendes (dont la fraction de 25 800 € soumise aux cotisations sur sa déclaration de revenus d'indépendant) ; Julie déclare ses 18 000 € (le PFU s'applique à l'IR, sauf option globale pour le barème) | Associés |

**Réponse à Marc (question 7)**

> Bonjour Marc,
>
> Bonne nouvelle : la société peut verser les 45 000 € prévus (22,50 € par part). Trois précisions :
> 1. **La « flat tax » ne vous concerne que pour une petite partie.** Comme gérant majoritaire, la part de vos dividendes qui dépasse 10 % de votre part du capital (soit 1 200 €) est soumise aux **cotisations sociales** des indépendants, comme votre rémunération. Sur vos 27 000 €, environ 25 800 € supporteront des cotisations de l'ordre de 10 000 € (estimation à 40 %), à payer à l'URSSAF l'année prochaine — prévoyez-les. Ce n'est donc pas « sans charges sociales ».
> 2. **La société retient à la source** : pour vous, 3 456,00 € d'acompte d'impôt (12,8 %) et 223,20 € de prélèvements sociaux → vous recevrez **23 320,80 €** ; pour Julie, dispensée de l'acompte d'impôt, 3 348,00 € de prélèvements sociaux → elle recevra **14 652,00 €**.
> 3. **L'État** : 7 027,20 € à verser au plus tard le 15 juillet 2027 avec la déclaration 2777 ; nous nous en chargeons.
>
> Par ailleurs, la réserve légale est désormais complète : il ne fallait doter que 350 €, et non 3 569 €. Pour l'année prochaine, nous pourrons comparer avec vous rémunération et dividendes : avec la règle des 10 %, une rémunération complémentaire est souvent plus intéressante pour un gérant majoritaire (elle est déductible de l'IS et ouvre des droits à la retraite).

**Contrôles et documentation** :
- Récupérer les PV 2023-2025 pour compléter la mention de l'art. 243 bis.
- Classer la demande de dispense de Julie (valable pour 2027 uniquement — la renouveler chaque année avant le 30/11).
- Créer l'échéance « 2777 au 15/07/2027 » et « IFU 2027 avant le 15/02/2028 » dans le planning.
- Vérifier, lors de la révision 2027, que 457, 4422 et 4423 sont soldés.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. L. 232-10 (réserve légale : 5 %, plafond 10 % du capital), art. L. 232-11 (bénéfice distribuable), art. L. 232-13 (paiement dans les 9 mois), art. L. 223-26 (approbation dans les 6 mois, SARL), art. L. 232-22 (dépôt au greffe).
- CGI : art. 117 quater (PFNL 12,8 % et dispense), art. 200 A (PFU / option pour le barème), art. 158-3-2° (abattement de 40 %), art. 243 bis (mention des distributions antérieures), art. 242 ter (IFU).
- Code de la sécurité sociale : art. L. 131-6 (fraction des dividendes > 10 % soumise aux cotisations des travailleurs indépendants) ; art. L. 136-6 / L. 136-7 et LFSS 2026 (CSG sur les revenus du capital — *taux à vérifier*).
- PCG : comptes 1061, 1068, 110, 120, 457, 442.
- BOFiP : RPPM – Revenus de capitaux mobiliers – prélèvement forfaitaire non libératoire, dispense.
