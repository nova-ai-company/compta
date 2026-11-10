# E16-03 — Un salarié pour deux services : ventiler les salaires au temps passé
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** salaire chargé, temps passé, feuilles de temps, ventilation analytique des salaires, OD de reclassement, régularisation, subvention affectée, dépenses éligibles

**Corner case :** oui — un financeur refuse des frais de personnel non justifiés par des feuilles de temps, et la tentation est de « basculer » la charge sur un autre service

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **Compte 6411** | Salaires, appointements. Salaire brut de base. Les IJSS reçues en subrogation viennent en diminution. |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **OD analytique** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **subvention affectée** | Subvention donnée pour un projet précis. Elle ne peut servir qu'à ce projet ; ce qui n'est pas dépensé va en fonds dédiés ou est remboursé. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes et chiffres fictifs.*

!!! abstract "En clair"
    Un salarié qui travaille pour deux services doit être payé **par les deux**, au prorata du **temps réellement passé**. La preuve de ce temps, c'est la **feuille de temps** (ou le planning réalisé), signée par le salarié et par son responsable. Pas de feuille de temps = pas de preuve = le financeur peut refuser la dépense.

## La mise en situation

Mardi 10/11/2026. Vous recevez l'OD de paie d'octobre préparée par le service paie du cabinet d'expertise comptable. Hélène Ferrand a ajouté une note :

> « Attention, le logiciel de paie impute chaque salarié sur **une seule section** : celle de son contrat. Pour les trois salariés partagés, il faut les ventiler vous-même, à partir des feuilles de temps. Et je crois que rien n'a été fait depuis janvier pour la psychologue et le secrétaire. »

Le même jour, un courriel de la Fondation Lumen (financeur du projet expérimental « Pairs et voix ») :

> « Madame, à l'occasion du contrôle du compte rendu intermédiaire 2026, nous constatons que les frais de personnel de Mme Inès Moulin imputés au projet de **janvier à mai 2026** ne sont accompagnés d'**aucune feuille de temps**. Conformément à la convention, nous ne pouvons pas les retenir. Merci de nous adresser un compte rendu corrigé avant le 30/11/2026. »

Sophie Laurent, cheffe de service SAVS et emploi accompagné, passe dans votre bureau :

> « Le plus simple, c'est de remettre ces cinq mois sur l'emploi accompagné, non ? Il nous reste du budget sur la convention. »

## Les pièces

**Pièce 1 — Les trois salariés partagés (paie d'octobre 2026)**

| Salarié | Poste | Temps de travail | Section du contrat (imputation par la paie) | Salaire brut d'octobre |
|---|---|---|---|---|
| Claire Vidal | Psychologue | Temps plein (1 ETP) | 10-SESSAD | 3 250,00 € |
| Julien Pereira | Secrétaire | 0,8 ETP | 10-SESSAD | 1 920,00 € |
| Inès Moulin | Conseillère en emploi accompagné | Temps plein (1 ETP) | 30-EMPLOI | 2 450,00 € |

Hypothèse de l'exercice : on retient un **taux global de charges patronales de 42 % du brut** (cotisations de sécurité sociale, retraite complémentaire, prévoyance, formation, après réductions) — *taux moyen fictif, valeur à vérifier chaque année*. Le salaire **chargé** = brut + charges patronales. On ignore la taxe sur les salaires et les provisions pour congés payés. Les salaires bruts sont identiques chaque mois de janvier à octobre.

L'OD de paie d'octobre enregistre les salaires bruts au compte **6411** (Salaires) et les charges patronales au compte **645** (Charges de sécurité sociale et de prévoyance), sur la section du contrat.

**Pièce 2 — Feuilles de temps d'octobre 2026 (signées par le salarié et le chef de service)**

| Salarié | 10-SESSAD | 20-SAVS | 30-EMPLOI | 50-PAIRS | Total |
|---|---|---|---|---|---|
| Claire Vidal | 92,40 h | 61,60 h | — | — | 154,00 h |
| Julien Pereira | 61,60 h | 36,96 h | 24,64 h | — | 123,20 h |
| Inès Moulin | — | — | 123,20 h | 30,80 h | 154,00 h |

**Pièce 3 — Cumul des feuilles de temps de janvier à septembre 2026 (signées)**

| Salarié | 10-SESSAD | 20-SAVS | 30-EMPLOI | Total |
|---|---|---|---|---|
| Claire Vidal | 806 h | 434 h | — | 1 240 h |
| Julien Pereira | 520 h | 300 h | 180 h | 1 000 h |

De janvier à septembre, leurs salaires sont restés **entièrement** sur 10-SESSAD.

**Pièce 4 — Inès Moulin : ce qui a été fait de janvier à septembre**

- Chaque mois, Mme Roux a passé une OD qui transférait **20 %** du salaire chargé d'Inès Moulin de 30-EMPLOI vers 50-PAIRS, « selon le budget du projet » (0,2 ETP).
- Les **feuilles de temps** n'existent qu'à partir de **juin 2026** ; elles confirment 20 % de juin à septembre.
- Pour janvier à mai, il existe : l'agenda électronique d'Inès Moulin et les **feuilles d'émargement** de 9 séances de formation des autoreprésentants qu'elle a animées.
- Extrait de la convention avec la Fondation Lumen : « Les frais de personnel ne sont éligibles que s'ils sont justifiés par des **feuilles de temps mensuelles** signées par le salarié et son responsable. »

## Travail à faire

1. Calculez le salaire **chargé** mensuel de chacun des trois salariés.
2. Calculez les pourcentages de temps d'octobre et ventilez le salaire chargé d'octobre (brut et charges séparément) entre les sections.
3. Passez l'**OD analytique de reclassement** d'octobre (31/10/2026).
4. Calculez et passez la **régularisation** de janvier à septembre pour Claire Vidal et Julien Pereira (les périodes jusqu'à septembre étant clôturées dans le logiciel, datez-la du 31/10/2026).
5. Inès Moulin : quel montant est contesté par la Fondation Lumen ? Que répondez-vous à Sophie Laurent ? Que proposez-vous ?
6. Que demandez-vous au service paie pour que le problème ne se reproduise pas ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E16-03_corrige.md)
