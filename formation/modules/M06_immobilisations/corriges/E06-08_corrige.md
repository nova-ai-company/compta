# Corrigé E06-08 — Frais de développement : ce qui s'active, ce qui ne s'active pas

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E06-08](../exercices/E06-08_frais-developpement-technova.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Étape 1 — Recherche ou développement ?**
- **Recherche** : travaux originaux pour acquérir des connaissances nouvelles, lever une **incertitude scientifique ou technique** ; on ne sait pas encore si cela débouchera sur un produit. → **Toujours en charges**, même si un prototype « marche ».
- **Développement** : application des connaissances à un **projet défini** (produit, version, module), dont la faisabilité est établie. → **Activable** (méthode de référence, appliquée par TechNova depuis 2023) dès que les **six critères** sont réunis : (1) faisabilité technique, (2) intention d'achever, (3) capacité d'utiliser ou de vendre, (4) avantages économiques futurs probables, (5) ressources disponibles, (6) évaluation fiable des dépenses.

**Étape 2 — Projet par projet (question 1)**

| Critère | V4 | Module paie | Moteur d'optimisation | Interface mobile |
|---|---|---|---|---|
| Nature | Développement | Développement | **Recherche** (verrou scientifique, échecs, incertitude) | Développement (technologie connue) |
| 1. Faisabilité technique | ✔ (techno maîtrisée) | ✔ à l'origine | ✘ verrou non levé ; un prototype expérimental ≠ faisabilité industrielle | ✔ prototype UX validé (déc. 2025) |
| 2. Intention d'achever | ✔ | **✘ depuis le 12/05/2026** | ✘ « aucune décision d'industrialisation » | ✔ PV du 15/01/2026 |
| 3. Capacité à utiliser / vendre | ✔ | ✘ | — | ✔ offre « Mobile+ » |
| 4. Avantages futurs probables | ✔ clients existants | ✘ (concurrence) | non démontré | ✔ 41 lettres d'intention, prix défini |
| 5. Ressources disponibles | ✔ | — | — | ✔ budget 55 000 €, trésorerie 1,1 M€ |
| 6. Évaluation fiable | ✔ factures ESN | — | ✔ (temps) | ✔ Jira + feuilles mensuelles |
| **Conclusion** | **Activable** | **Sortie de l'actif** | **Charges** | **Activable** (en cours au 31/12) |

Le moteur d'optimisation est d'ailleurs déclaré en **CIR** comme projet de **recherche** (E10-06) : le qualifier de « développement » pour l'activer serait incohérent — et un vérificateur ou un auditeur le relèverait immédiatement.

**Étape 3 — Le coût incorporable (question 2).** Seules les dépenses **directement attribuables** à la création, à la production et à la préparation de l'actif, engagées **après** la réunion des critères :

| Dépense (interface mobile) | Incorporable ? | Justification |
|---|---|---|
| Lisa 50 % (27 900) | **Oui** | Coût salarial chargé effectivement supporté, temps documenté |
| Julie 20 % (12 896) | **Oui** | Idem |
| Designer UI freelance (9 000) | **Oui** | Prestation directement affectée |
| Formation Flutter (2 400) | **Non** | Formation du personnel : toujours exclue |
| Campagne de pré-lancement (7 500) | **Non** | Coûts de commercialisation et de publicité |
| Quote-part de loyer et frais généraux (6 000) | **Non** | Frais administratifs et généraux non directement attribuables |
| **Total activable** | **49 796,00** | |

V4 : ESN 48 000 + outils de tests dédiés 3 200 = **51 200,00 €** activables (engagés avant la mise en production du 01/03/2026 ; tout ce qui suit la mise en production — maintenance, corrections — est en charges).

**Étape 4 — L'abandon (question 3).** Le 12/05/2026, le critère « intention d'achever » disparaît pour le module paie : les 18 000 € inclus dans le 232 ne correspondent plus à aucun actif. On les **sort** (VNC = 18 000 €, aucun prix). Ils ne peuvent pas être transférés en 203 avec la V4, ni « dilués » dans le coût de la V4.

**Étape 5 — Mise en service et amortissement.** La V4 passe de 232 à 203 le 01/03/2026 et s'amortit sur 3 ans à compter de cette date. L'interface mobile, non mise en service au 31/12/2026, reste en **232 et n'est pas amortie** (mais devra faire l'objet d'un test de dépréciation si un indice apparaît).

## 2. Calculs (détaillés, chaque montant justifié)

**V4 — coût à transférer en 203**

| Élément | Montant |
|---|---:|
| 232 V4 au 31/12/2025 | 95 000,00 |
| – module paie abandonné | – 18 000,00 |
| + dépenses 2026 activables (ESN + tests) | + 51 200,00 |
| **= Coût de la V4 au 01/03/2026** | **128 200,00** |

Amortissement 2026 : 128 200 / 3 × 10/12 = **35 611,11 €** ; annuité pleine : 42 733,33 €.

**Solde du 232 au 31/12/2026** : 95 000 – 18 000 + 51 200 – 128 200 + 49 796 = **49 796,00 €** (interface mobile).

**Question 5 — impact sur le résultat 2026**

| Élément | Montant |
|---|---:|
| Production immobilisée V4 (721) | + 51 200,00 |
| Production immobilisée interface mobile (721) | + 49 796,00 |
| Sortie du module paie (675) | – 18 000,00 |
| Amortissement V4 (6811) | – 35 611,11 |
| **Impact net par rapport à « tout en charges »** | **+ 47 384,89** |

**Demande de Yanis** (activer en plus le moteur et les frais exclus) : + 205 320 + 30 000 (moteur, hors dotation GPU qui est déjà un amortissement) + 2 400 + 7 500 + 6 000 = **+ 251 220,00 €** de résultat et de capitaux propres **fictifs**. C'est une **irrégularité** (comptes ne donnant pas une image fidèle) que le cabinet ne peut pas présenter.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 28/02/2026 | OD | 232 | Immobilisations incorporelles en cours | V4 — dépenses 2026 ESN + outils de tests | 51 200,00 | |
| 28/02/2026 | OD | 721 | Production immobilisée – immobilisations incorporelles | V4 — production immobilisée 2026 | | 51 200,00 |
| 01/03/2026 | OD | 203 | Frais de développement | Mise en production V4 | 128 200,00 | |
| 01/03/2026 | OD | 232 | Immobilisations incorporelles en cours | Transfert V4 en 203 | | 128 200,00 |
| 12/05/2026 | OD | 675 | Valeurs comptables des éléments d'actif cédés (sortie sans prix) | Abandon module paie intégrée — CODIR 12/05/2026 | 18 000,00 | |
| 12/05/2026 | OD | 232 | Immobilisations incorporelles en cours | Abandon module paie intégrée | | 18 000,00 |
| 31/12/2026 | OD | 232 | Immobilisations incorporelles en cours | Interface mobile — coûts activables 2026 | 49 796,00 | |
| 31/12/2026 | OD | 721 | Production immobilisée – immobilisations incorporelles | Interface mobile — production immobilisée 2026 | | 49 796,00 |
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations incorporelles | V4 — 10 mois | 35 611,11 | |
| 31/12/2026 | OD | 2803 | Amortissements des frais de développement | V4 — 10 mois | | 35 611,11 |
| | | | | **Totaux** | **282 807,11** | **282 807,11** |

Remarques :
- La chronologie compte : le transfert 232 → 203 du 01/03 suppose que les 51 200 € de 2026 aient été portés au 232 avant (écriture du 28/02). En pratique, beaucoup de cabinets passent la production immobilisée à la clôture : le résultat est identique, mais le **fichier** doit porter la bonne date de mise en service.
- Sortie du module abandonné : certains cabinets constatent d'abord une **dépréciation** à 100 % (6816 / 2932) puis la sortie ; l'effet sur le résultat est le même. *Le compte de sortie (675) est celui retenu par le cabinet ; vérifiez la subdivision de la nomenclature 2025 pour les mises au rebut.*
- Les charges par nature (salaires, sous-traitance) restent en classe 6 : la production immobilisée **ne les annule pas**, elle les compense par un produit d'exploitation (721).

## 4. Points d'attention / pièges

- **« Le prototype marche »** n'est pas un critère : la faisabilité technique s'apprécie pour le **produit final** et doit être documentée (note technique, décision d'industrialisation). Les dépenses du moteur engagées en 2026 resteront **définitivement** en charges, même si les critères sont remplis en 2027 : **pas de réactivation rétroactive**.
- **Personnel** : retenir le coût **effectivement supporté** (TechNova est JEI : charges patronales réduites) et seulement le temps **documenté** ; pas de « forfait » de frais de structure.
- **Mise en service** : la V4 est amortie à partir de sa **mise en production** (01/03), pas à partir du 01/01 ni de la date de la dernière facture.
- **Dépréciation** : le 232 « interface mobile » doit être testé si le lancement d'avril 2027 est compromis (perte de clients pilotes, abandon de la fonctionnalité).
- **Cohérence avec le CIR / CII** (E10-06) : l'activation ne modifie pas la base du crédit d'impôt, qui porte sur les **dépenses exposées** (personnel, sous-traitance, dotations aux amortissements des immobilisations affectées à la recherche) ; le moteur relève du CIR, l'interface mobile éventuellement du **CII** (innovation). Veillez à ne pas compter deux fois une même dépense (dépense de personnel dans le CII **et** dotation aux amortissements de l'actif créé).
- **Option fiscale (CGI, art. 236-I)** : les dépenses de recherche **scientifique ou technique** peuvent être déduites immédiatement même si elles sont immobilisées (via amortissement dérogatoire). Elle vise la recherche au sens fiscal ; la V4 et l'interface mobile, développements sans incertitude scientifique, n'en relèvent pas en principe — *à valider avant toute option*.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Conséquences juridiques (question 6)** : tant que les frais de développement inscrits à l'actif ne sont pas totalement amortis, **aucune distribution de dividendes** n'est possible, sauf si les réserves libres sont au moins égales au montant des frais non amortis (Code de commerce, partie réglementaire). Au 31/12/2026, la VNC des frais de développement et des développements en cours se chiffre en centaines de milliers d'euros : sujet à anticiper si les fondateurs ou les investisseurs envisagent une distribution.

**Mail à Yanis Haddad (copie Émilie Roux)**

> Bonjour Yanis,
>
> Nous avons analysé les quatre projets 2026. La V4 (128 200 €) et l'interface mobile (49 796 €) répondent aux critères d'activation et sont inscrites à l'actif ; le module « paie intégrée » abandonné en mai sort de l'actif (18 000 €). Au total, le résultat 2026 est amélioré de 47 385 € par rapport à un traitement tout en charges.
>
> En revanche, le moteur d'optimisation relève de la recherche (incertitude scientifique non levée, pas de décision d'industrialisation) : les règles comptables interdisent de l'activer, quel que soit le succès du prototype. C'est d'ailleurs à ce titre qu'il ouvre droit au crédit d'impôt recherche. De même, la formation, la campagne de pré-lancement et la quote-part de loyer ne peuvent pas être incorporées. Les activer augmenterait artificiellement les capitaux propres de 251 220 € : un auditeur mandaté par les investisseurs le corrigerait, avec un effet très négatif sur la négociation.
>
> Pour valoriser le moteur auprès des investisseurs, le bon vecteur est la documentation (brevet éventuel, rapport technique, dossier CIR) et l'annexe des comptes, pas le bilan.

**Documentation du dossier** : note d'activation par projet (critères, preuves, date de réunion des critères), extraction des temps validés, PV du comité de direction, calcul du coût, mise à jour de l'annexe (méthode, montants activés, durée d'amortissement).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : définition des frais de recherche et de développement ; conditions d'activation des frais de développement (méthode de référence) ; coût de production des immobilisations incorporelles ; logiciels créés.
- Code de commerce, partie réglementaire : interdiction de distribution tant que les frais de développement ne sont pas amortis, sauf réserves libres suffisantes.
- CGI, art. 236-I : option de déduction immédiate des dépenses de recherche ; art. 244 quater B : crédit d'impôt recherche et innovation (module M10, exercice E10-06).
