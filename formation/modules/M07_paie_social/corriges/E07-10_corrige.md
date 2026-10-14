# Corrigé E07-10 — Trois corner cases sociaux : coach « indépendant », dirigeants non rémunérés, erreur de paie découverte trois mois après

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-10](../exercices/E07-10_corner-cases-social.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Cas A — Le coach de FitClub
1. **Critère du contrat de travail** : une prestation, une rémunération et surtout un **lien de subordination** — exécution d'un travail sous l'autorité d'un employeur qui a le pouvoir de donner des ordres, d'en contrôler l'exécution et de sanctionner les manquements (jurisprudence constante de la Cour de cassation, arrêt *Société Générale* de 1996). Le **travail au sein d'un service organisé** est un indice lorsque l'employeur en fixe unilatéralement les conditions.
2. **Présomption de non-salariat** : l'immatriculation comme micro-entrepreneur fait présumer l'absence de contrat de travail (article L. 8221-6 du Code du travail), mais la présomption **tombe** si la subordination juridique permanente est établie.
3. **Indices ici** : planning imposé, tarif fixé par FitClub, tenue FitClub, matériel du club, obligation de prévenir et de se faire remplacer **par le club**, **client unique**, aucune clientèle propre, rémunération horaire fixe depuis 3 ans. Le faisceau est **défavorable** : le risque de requalification est élevé.
4. **Conséquences** : rappel de cotisations (sommes versées réintégrées dans l'assiette, le cas échéant après reconstitution d'un brut), majorations de retard, perte de réductions de cotisations sur la période, risque de qualification de **travail dissimulé** (prescription allongée, annulation des exonérations, sanctions pénales) si l'intention est retenue ; côté prud'hommes, Samir pourrait demander la requalification (rappels de CP, indemnités de rupture…).
5. **Comptes au 31/08/2026** : l'avis de contrôle reçu le 15/09/2026 est un **événement postérieur à la clôture** qui **éclaire une situation existant à la clôture** (la relation litigieuse existait depuis 2023). Les comptes n'étant pas arrêtés, il faut en tenir compte : la sortie de ressources est **probable** et **estimable** → **provision pour risques**.

### Cas B — Studio Pixel
1. **Président et DG de SAS non rémunérés** : ils seraient assimilés salariés **s'ils étaient rémunérés** ; sans rémunération, **pas d'affiliation, pas de bulletin, pas de cotisations** — et pas de droits (retraite, indemnités journalières). Ils peuvent cumuler leur ARE avec leur mandat non rémunéré (sous les conditions de France Travail).
2. **ACRE** : exonération partielle de cotisations sur les **revenus d'activité** pendant 12 mois à compter de la création, réservée à certains publics (dont les demandeurs d'emploi indemnisés) et conditionnée à une demande — *conditions, taux et délais à vérifier, le dispositif ayant été modifié à plusieurs reprises*. Elle n'a d'intérêt **que s'il y a une rémunération**. Ici, la société a été immatriculée le 01/09/2025 : la période de 12 mois **a expiré le 31/08/2026**. Sans rémunération versée, l'ACRE n'a rien exonéré et il n'y a plus rien à demander.
3. **Dépenses personnelles payées par la société** : ce ne sont pas des charges. Si elles ne sont ni remboursées ni imputées sur un compte courant créditeur, elles constituent pour un dirigeant une **rémunération de fait** (assujettissement au régime général, cotisations, bulletin) et fiscalement un **revenu distribué**. Imputer sur le compte courant de Sarah est possible **tant qu'il reste créditeur** : un compte courant **débiteur** d'un dirigeant de SAS personne physique est une **avance interdite** (article L. 227-12 du Code de commerce, qui renvoie à l'interdiction applicable aux SA — sanctions possibles, abus de biens sociaux).

### Cas C — Atelier Ligne
1. L'avenant du 28/05 rend le salaire de 3 100 € **dû** dès juin. Au 30/09/2026, la société doit 3 × 300 = 900 € brut : c'est une **dette certaine** de l'exercice → **charge à payer** (avec les charges sociales).
2. **Paie / DSN** : le rappel est versé avec la paie d'octobre et déclaré dans la DSN d'octobre en **rappel de salaire rattaché aux périodes d'emploi d'origine** (juin à août) pour l'application des plafonds et des taux ; le PAS s'applique sur le net imposable du mois de **versement**.

## 2. Calculs (détaillés, chaque montant justifié)

### Cas A
- Provision : rappel de cotisations 34 000 € + majorations de retard 1 700 € = **35 700 €**.
- Fiscalité : la fraction correspondant aux **majorations** (pénalités) n'est pas déductible → réintégration de 1 700 € ; la fraction « cotisations » est déductible si la provision répond aux conditions générales.
- Exposition résiduelle hors période contrôlée : janvier → août 2026, 8 × 1 800 = 14 400 € versés, sur lesquels le même risque existe ; à mentionner et à intégrer dans la provision si la requalification est jugée probable pour la période postérieure (ici, on la signale et on recommande de régulariser la situation immédiatement).

### Cas B
On suppose que Sarah confirme le 09/10/2026, par écrit, que les quatre dépenses sont personnelles (aucun client invité, aucune facture au nom de la société).
- Dépenses personnelles : 98,40 + 112,00 + 76,00 + 143,92 = **430,32 €** (TTC ; aucune TVA récupérable).
- Compte courant de Sarah après imputation : 1 240,00 − 430,32 = **809,68 € créditeur** ✔ (pas d'avance interdite).

### Cas C
- Rappel brut : 3 × (3 100 − 2 800) = **900,00 €**.
- Charges patronales estimées : 900,00 × 42 % = **378,00 €**.
- Dette de CP : déjà calculée sur 3 100 € → rien à ajouter (si la méthode du 1/10e était retenue pour Manon, l'incidence serait de 90 € × 42 % de charges, négligeable).

## 3. Écritures comptables

**Cas A — FitClub, au 31/08/2026**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/08/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Risque redressement URSSAF – requalification coach | 35 700,00 | |
| 31/08/2026 | OD | 151 | Provisions pour risques (*subdivision selon la nomenclature 2025 du PCG*) | Risque redressement URSSAF 2023-2025 | | 35 700,00 |
| | | | | **Totaux** | **35 700,00** | **35 700,00** |

> Lors du redressement effectif, la provision sera reprise et les cotisations comptabilisées par nature (645x), les majorations en charges d'exploitation (658, *subdivision selon la nomenclature 2025 du PCG*) — et non plus en charges exceptionnelles.

**Cas B — Studio Pixel, au 30/09/2026**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 455200 | Associés – compte courant Sarah Cohen | Dépenses personnelles payées par CB société | 430,32 | |
| 30/09/2026 | OD | 471000 | Compte d'attente | Apurement dépenses personnelles S. Cohen | | 430,32 |
| | | | | **Totaux** | **430,32** | **430,32** |

**Cas C — Atelier Ligne, au 30/09/2026**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6411 | Salaires, appointements | Rappel salaire M. Lefèvre 06-08/2026 | 900,00 | |
| 30/09/2026 | OD | 4286 | Personnel – autres charges à payer | Rappel salaire M. Lefèvre à verser 10/2026 | | 900,00 |
| 30/09/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance (*subdivision selon la nomenclature 2025 du PCG*) | Charges sociales sur rappel (42 %) | 378,00 | |
| 30/09/2026 | OD | 4386 | Organismes sociaux – autres charges à payer | Charges sociales sur rappel | | 378,00 |
| | | | | **Totaux** | **1 278,00** | **1 278,00** |

Ces écritures sont **extournées au 01/10/2026** ; la paie d'octobre comptabilisera le rappel réel.

## 4. Points d'attention / pièges

- **Cas A** : ne pas se contenter du SIRET et de la facture « conforme » : c'est la **réalité de la relation** qui compte. Ne pas oublier les **événements post-clôture** tant que les comptes ne sont pas arrêtés. Une provision n'est pas un aveu : elle est évaluée prudemment et documentée ; l'annexe peut rester sobre si l'information porte préjudice à la société dans un litige (dans le respect des règles de l'annexe).
- **Cas B** : l'ACRE n'est pas un « droit » général ni un crédit ; sans rémunération, elle n'a aucun effet. Ne jamais laisser des dépenses personnelles en compte d'attente : à la clôture, elles seraient requalifiées. Surveiller le **compte courant débiteur** à chaque arrêté (relevés CB mensuels).
- **Cas C** : une erreur de paie se corrige **en paie** (rappel ou retenue) et **en DSN** (régularisation rattachée à la bonne période) — jamais par une simple OD comptable. À la clôture, la dette existe dès que le salaire était dû.
- **Trop-perçu (cas inverse)** : l'employeur peut réclamer les sommes indûment versées (action en répétition de l'indu, prescription de 3 ans) mais la retenue sur salaire est limitée à la **fraction saisissable** (compensation encadrée par le Code du travail) ; un échéancier écrit est recommandé ; les cotisations et le PAS sont régularisés négativement en DSN. Une créance sur le salarié au 4287/425 à la clôture doit être justifiée et, si elle est douteuse, dépréciée.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- **FitClub** : conseiller à Romain Faure de **régulariser sans attendre** (CDI à temps partiel ou CDD d'usage selon l'activité, ou au contraire rendre l'indépendance réelle : tarifs fixés par le coach, clientèle propre, liberté d'organisation) ; préparer le contrôle (liste des prestataires, contrats, factures) ; prévenir l'assureur protection juridique ; documenter l'estimation de la provision.
- **Studio Pixel** : envoyer aux fondateurs une note sur les coûts d'une future rémunération (assimilés salariés : pas de cotisation chômage, mais charges élevées) et l'alternative dividendes (prélèvements sociaux uniquement en SAS) ; rappeler la règle « carte société = dépenses de la société uniquement ».
- **Atelier Ligne** : contrôler toutes les augmentations et avenants de l'année (procédure : tout avenant signé est transmis le jour même au gestionnaire paie), et rapprocher contrat / bulletin pour chaque salarié lors de la révision.
- **Mail à Léo Martin (cas B)** :

> Bonjour Léo,
> Tant que Sarah et vous ne vous versez aucune rémunération, vous ne payez aucune cotisation sociale en tant que dirigeants — mais vous n'acquérez pas non plus de droits (retraite, indemnités en cas d'arrêt). L'ACRE ne réduit que des cotisations sur une rémunération : sans rémunération, elle ne vous apportait rien, et sa période de 12 mois s'est achevée le 31 août 2026.
> Les dépenses personnelles de Sarah (430,32 €) ont été imputées sur son compte courant, qui reste créditeur (809,68 €). Attention : ce compte ne doit jamais devenir débiteur — la loi interdit à une SAS de faire des avances à ses dirigeants. Le plus simple est de réserver la carte de la société aux seules dépenses professionnelles.
> Bien cordialement,

## 6. Références

- Code du travail : article L. 8221-6 (présomption de non-salariat des personnes immatriculées), articles L. 8221-5 et suivants (travail dissimulé) ; Cass. soc., 13 novembre 1996, *Société Générale* (définition du lien de subordination).
- Code de la sécurité sociale : article L. 311-3 (président et DG de SAS assimilés salariés), article L. 131-6-4 (ACRE) — *conditions à vérifier* ; article L. 243-7 et suivants (contrôle URSSAF).
- Code de commerce : article L. 227-12 (interdiction des avances aux dirigeants de SAS, renvoi à l'article L. 225-43) ; articles L. 123-12 et suivants ; PCG (événements postérieurs à la clôture).
- Code du travail : article L. 3251-3 (limitation des retenues sur salaire), article L. 3245-1 (prescription triennale des salaires).
- PCG : comptes 151, 6815, 455, 471, 6411, 4286, 645, 4386 ; règlement ANC n° 2022-06 (pénalités et amendes en charges d'exploitation).
