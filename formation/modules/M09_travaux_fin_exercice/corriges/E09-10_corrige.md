# Corrigé E09-10 — Delta Invest : faut-il encore déprécier les titres de la Menuiserie ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-10](../exercices/E09-10_depreciation-titres-delta-invest.md)

## 1. Analyse

**Évaluation des titres de participation.** À la clôture, on compare la **valeur d'entrée** (coût d'acquisition, frais d'acquisition compris le cas échéant) à la **valeur d'inventaire**, c'est-à-dire la **valeur d'utilité**. La valeur d'utilité représente ce que l'entreprise accepterait de décaisser pour obtenir la participation si elle avait à l'acquérir. Elle s'apprécie selon une **approche multicritère** :
- critères **patrimoniaux** : quote-part des capitaux propres, éventuellement réévalués (plus-values latentes sur actifs) ;
- critères de **rentabilité et de perspectives** : flux de trésorerie actualisés, rentabilité future ;
- critères de **marché** : transactions récentes, multiples ;
- **intention** et **utilité** pour la détentrice (participation stratégique, synergies de groupe).

On ne déprécie que si la valeur d'utilité est **inférieure** au coût. La **quote-part de capitaux propres** est souvent le premier indicateur, mais elle **ne suffit pas**. Une société en redressement avec un plan crédible peut avoir une valeur d'utilité positive malgré des capitaux propres négatifs. À l'inverse, des capitaux propres positifs peuvent masquer une activité sans avenir.

**Application :**
- quote-part des capitaux propres : 95 % × (– 15 100 €) → **négative** (on retient 0) ;
- flux actualisés : 40 000 € pour 100 %, soit **38 000 € pour 95 %**. Le plan est revu, les hypothèses sont « raisonnables mais exigeantes », et la sensibilité va de 22 000 € à 61 000 € ;
- utilité pour Delta : la filiale fait partie du groupe intégré et du projet du dirigeant.

On retient la valeur issue des **flux actualisés** (38 000 €), parce que le plan d'affaires est documenté et revu, et que la continuité d'exploitation est soutenue par l'associé. On écarte la quote-part de capitaux propres, qui ne reflète pas les perspectives. La **prudence** impose de ne pas retenir l'hypothèse haute (10 %). On garde l'hypothèse centrale et on documente la sensibilité. Si le CAC jugeait le plan insuffisamment étayé, il faudrait retenir une valeur plus basse.

**Le compte courant (60 000 €).** La valeur des capitaux propres de 40 000 € est calculée **après** remboursement de tout l'endettement net, **y compris** le compte courant de Delta. Le plan prévoit donc implicitement le remboursement du compte courant : **pas de dépréciation**. En revanche, si la valeur des capitaux propres devenait négative, il faudrait d'abord déprécier totalement les titres, puis le compte courant (D 6866 / C 2967 ou 496 selon le classement), puis envisager une provision pour risque.

**La lettre de soutien.** C'est une **intention** de soutien et d'augmentation de capital (« confirme son intention », « envisage »). Elle ne crée **pas une obligation** de couvrir les pertes de la filiale au profit d'un tiers. Il n'y a donc pas de provision pour risque filiale (1518). Une lettre d'**engagement ferme** (garantie de passif au profit d'une banque, obligation de combler un passif) pourrait justifier une provision, si une sortie de ressources devenait probable au-delà de la valeur des titres et du compte courant. La lettre est en revanche un **engagement hors bilan** à mentionner en annexe.

## 2. Calculs

| Élément | Montant |
|---|---|
| Valeur brute des titres | 197 600,00 € |
| Valeur d'utilité retenue : 40 000 × 95 % | 38 000,00 € |
| Dépréciation nécessaire au 31/12/2026 | 159 600,00 € |
| Dépréciation existante | 120 000,00 € |
| **Dotation complémentaire 2026** | **39 600,00 €** |

Valeur nette des titres au bilan après dotation : 197 600 – 159 600 = **38 000,00 €**.

*Sensibilité (à documenter dans le dossier) : à 14 %, valeur d'utilité 22 000 × 95 % = 20 900 €, soit une dotation de 56 700 € ; à 10 %, valeur 61 000 × 95 % = 57 950 €, soit une dotation de 19 650 €.*

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6866 | Dotations aux dépréciations des éléments financiers | Dépréciation complémentaire titres Menuiserie (VU 38 000) | 39 600,00 | |
| 31/12/2026 | OD | 2961 | Dépréciations des titres de participation | Dépréciation complémentaire titres Menuiserie | | 39 600,00 |
| | | | | **Totaux** | **39 600,00** | **39 600,00** |

**Abandon de créance du 15/10/2026 (déjà comptabilisé, à valider) :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | OD | 668 | Autres charges financières (*subdivision selon nomenclature 2025*) | Abandon de créance à caractère financier – Menuiserie (clause RMF) | 200 000,00 | |
| 15/10/2026 | OD | 4511 | Comptes courants – groupe | Abandon de créance Menuiserie | | 200 000,00 |
| | | | | **Totaux** | **200 000,00** | **200 000,00** |

## 4. Points d'attention / pièges

**Réponse sur l'abandon de créance :**
- **Comptablement**, l'abandon est une **charge**. Il ne s'ajoute **pas** au coût des titres : il ne donne aucun droit supplémentaire sur la filiale, contrairement à une augmentation de capital. L'ajouter aux titres reviendrait à immobiliser une perte. Il s'agit d'un abandon à **caractère financier** (soutien d'une filiale, sans lien avec des relations commerciales) : on le classe en **charges financières (668)**. Il ne relèverait du résultat exceptionnel que s'il résultait d'un événement majeur et inhabituel (règles du PCG 2025). *La subdivision du compte est à vérifier dans la nomenclature 2025.*
- **Clause de retour à meilleure fortune** : tant que la condition n'est pas réalisée, c'est un **engagement reçu** (hors bilan) chez Delta. Si la Menuiserie revient à meilleure fortune, Delta constatera un **produit**, et la Menuiserie une charge.
- **Fiscalement**, un abandon de créance à caractère financier consenti à une filiale **n'est pas déductible** chez la mère (art. 39, 13 CGI), sauf si la filiale fait l'objet d'une procédure de sauvegarde, de redressement ou de liquidation judiciaire, ou d'un accord de conciliation (dans certaines limites). La Menuiserie n'étant pas en procédure collective, les 200 000 € sont à **réintégrer**.
- **Intégration fiscale** : les abandons de créances entre sociétés du groupe sont **neutralisés** pour le résultat d'ensemble (art. 223 B CGI). La charge n'est pas déduite et le produit constaté chez la Menuiserie n'est pas imposé au niveau du groupe. Il faut tenir les états de suivi correspondants. *Le retour à meilleure fortune ne sera imposable chez Delta que dans la mesure où l'abandon avait été déduit : point à vérifier au BOFiP le moment venu.*

**Fiscalité de la dépréciation des titres :**
- Les dépréciations de **titres de participation** relevant du régime des plus-values à long terme exonérées (sous réserve d'une quote-part de frais et charges) **ne sont pas déductibles**. La dotation de 39 600 € est **réintégrée** sur la 2058-A ; la reprise future sera déduite.
- En intégration fiscale, cette dotation n'étant pas déduite, elle n'appelle aucune neutralisation supplémentaire.

**Autres pièges :**
- **Ne pas déprécier « tout »** par réflexe (« mon CAC va me demander… ») : une dépréciation totale non justifiée serait aussi inexacte qu'une absence de dépréciation.
- **Ne pas tenir compte de l'augmentation de capital future** dans la valeur d'utilité au 31/12/2026, sauf à travers les flux du plan. Les 100 000 € qui seront versés augmenteront le coût des titres et la valeur de la filiale **à due concurrence**, sans créer de valeur au 31/12/2026.
- **Ordre de dépréciation** : titres d'abord, puis compte courant, puis provision pour risque si une obligation existe.

**Annexe de Delta Invest :**
- tableau des **filiales et participations** (capital, capitaux propres, quote-part détenue, valeur brute et nette des titres, prêts et avances, chiffre d'affaires et résultat du dernier exercice) ;
- méthode d'évaluation des titres (flux actualisés, hypothèses clés et sensibilité) ;
- **engagements** : lettre de soutien à la Menuiserie, clause de retour à meilleure fortune (200 000 €), projet d'augmentation de capital ;
- l'abandon de créance consenti dans l'exercice.

## 5. Ce qu'un senior ferait en plus

- **Préparer le dossier pour le CAC** : note d'évaluation, plan d'affaires signé par le gérant, comparaison entre le plan de l'an dernier et le réel (pour tester la fiabilité des prévisions), analyse de sensibilité.
- **Faire signer la lettre de soutien** par le président de Delta, avec une rédaction maîtrisée : la différence entre « intention » et « engagement » change le traitement comptable chez les deux sociétés. Prévoir l'autorisation par l'organe compétent si les statuts l'exigent.
- **Conventions réglementées** : l'abandon de créance et la convention de compte courant entre Delta et sa filiale doivent être examinés au regard des règles applicables aux conventions entre la SAS et ses dirigeants et associés, et figurer dans le rapport aux associés.
- **Cohérence de groupe** : vérifier que l'économie d'impôt liée au déficit de la Menuiserie est traitée conformément à la convention d'intégration (réallocation ou non à la filiale).

**Réponse à Jean Delmas :**
> « Monsieur Delmas, nous ne déprécions pas tout. Le plan de redressement de la Menuiserie, revu par nos soins, valorise vos 95 % à 38 000 €. La dépréciation est donc portée à 159 600 € (dotation de 39 600 € cette année), non déductible fiscalement. Le compte courant restant (60 000 €) est couvert par le plan et n'est pas déprécié. L'abandon de 200 000 € est bien une charge : on ne l'ajoute pas au prix des titres. Il n'est pas déductible pour Delta, mais il est neutralisé dans le résultat du groupe intégré, et la clause de retour à meilleure fortune sera mentionnée en annexe. Votre future augmentation de capital de 100 000 € viendra, elle, augmenter le coût des titres en 2027. »

## 6. Références

- PCG (règlement ANC n° 2014-03 modifié) : évaluation des titres de participation à la valeur d'utilité, dépréciations (comptes 2961, 6866), engagements hors bilan.
- Code de commerce, art. L. 123-18 (évaluation à la valeur actuelle à la clôture) ; art. L. 233-15 et R. 123-197 (tableau des filiales et participations en annexe).
- CGI, art. 39, 1-5° (dépréciation des titres de participation) ; art. 219, I-a quinquies (plus-values à long terme sur titres de participation) ; art. 39, 13 (abandons de créances) ; art. 223 A et 223 B (intégration fiscale, neutralisations).
