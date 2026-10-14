# Corrigé E04-12 — Crédit de TVA remboursable et erreur sur une CA3 antérieure

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-12](../exercices/E04-12_credit-tva-erreur-ca3.md)

## 1. Analyse

**a) Deux erreurs distinctes.**
1. **Omission de TVA collectée en juin** : la facture Kanal Prod (prestation de services) a été **encaissée le 20/06** : la TVA de 1 600 € était exigible en juin (art. 269-2-c CGI). Le transfert 44574 → 44571 n'ayant pas été passé, elle n'a pas été déclarée. (La cession de droits est facturée à 20 % : le taux réduit applicable à certaines cessions de droits d'auteur ne vise que les auteurs personnes physiques, pas une société de production.)
2. **Double report en août** : le crédit de juillet (440 €) a été inclus dans la ligne 23 **et** ajouté une seconde fois au crédit à reporter : le crédit reporté en septembre (2 380 €) est surévalué de 440 €.

**b) La chaîne des crédits.** Corriger juin ne se limite pas à juin : le crédit de juin se reporte en juillet, et ainsi de suite. Il faut **reconstituer** chaque mois :

| Mois | Déclaré | Correct | Commentaire |
|---|---|---|---|
| Juin | crédit 2 600 | **crédit 1 000** (4 000 – 1 400 – 1 600) | |
| Juillet | crédit 440 | **TVA nette due 1 160** (2 900 – 740 de déductions propres – 1 000 de report) | **Retard de paiement de 1 160 €** |
| Août | crédit reporté 2 380 | **crédit 1 500** (2 300 de déductions propres – 800) | Pas de report de juillet (juillet était débiteur) |

Bien que juin soit resté créditeur, l'erreur a fait **disparaître une TVA due en juillet** : il y a donc bien un **retard de paiement** de 1 160 € et un **intérêt de retard** (art. 1727 CGI, 0,20 % par mois), réduit en cas de régularisation spontanée (*réduction à vérifier*). Si tous les mois étaient restés créditeurs après correction, il n'y aurait eu aucun intérêt (pas de retard de paiement), seulement un crédit reporté à rectifier.

**c) Comment régulariser.** Deux voies :
- déposer des **déclarations rectificatives** de juin, juillet et août (procédure la plus exacte, plus lourde) ;
- ou, en pratique courante, régulariser sur la **CA3 de septembre** : la ligne 22 reprend le crédit tel que déclaré en août (2 380 €, pour garder la cohérence avec la déclaration précédente), et les rappels sont portés en **ligne 5B « Sommes à ajouter »** (1 600 € de TVA omise en juin + 440 € de crédit reporté à tort), avec une **mention expresse** dans la zone de commentaires (période d'origine, nature de l'erreur). *Numérotation à contrôler sur le formulaire millésimé.*

**d) Le remboursement.** Après régularisation, la CA3 de septembre fait apparaître un crédit de 4 860 € ≥ 760 € : Studio Pixel, au réel normal, peut en demander le **remboursement** via le formulaire **3519** déposé avec la CA3 (ligne 26). Le crédit provient d'**investissements** (drone, caméras) : c'est la situation type du démarrage d'activité. Une demande de remboursement d'une jeune société déclenche fréquemment un **contrôle sur pièces** (demande de factures, de justificatifs de paiement et d'utilisation) — d'où l'intérêt d'avoir corrigé spontanément les erreurs **avant** la demande : l'agent aurait vu l'écart dans la chaîne des crédits.

## 2. Calculs

**CA3 de septembre 2026 corrigée**

| Ligne | Libellé | Montant |
|---|---|---|
| A1 / 08 | Prestations encaissées en septembre : base 11 000 / TVA 20 % | 2 200,00 |
| 5B | Sommes à ajouter : TVA omise juin (1 600) + crédit reporté à tort en août (440) | 2 040,00 |
| **16** | **Total TVA brute** | **4 240,00** |
| 19 | Biens constituant des immobilisations (3 600 + 2 000) | 5 600,00 |
| 20 | Autres biens et services | 1 120,00 |
| 22 | Report du crédit de la déclaration précédente | 2 380,00 |
| **23** | **Total TVA déductible** | **9 100,00** |
| **25** | **Crédit de TVA (23 – 16)** | **4 860,00** |
| 26 | Remboursement demandé (formulaire 3519 joint) | 4 860,00 |
| 27 | Crédit à reporter | 0,00 |
| 28 | TVA nette due | 0,00 |

**Contrôle par la chaîne corrigée** : crédit d'août correct 1 500 € + crédit propre de septembre (5 600 + 1 120 – 2 200 = 4 520 €) – TVA de juillet non payée 1 160 € = **4 860 €** ✔.

**Intérêt de retard (décompte indicatif)** : 1 160 € dus avec la CA3 de juillet (échéance août 2026), régularisés en octobre 2026 : 2 mois (septembre, octobre) × 0,20 % × 1 160 = **4,64 €**, avant réduction éventuelle. L'intérêt ne s'impute pas sur le crédit remboursable ; il sera acquitté selon les modalités indiquées par l'administration (*à vérifier*).

## 3. Écritures comptables

Hypothèse : en comptabilité, les liquidations de TVA de juin à août ont été passées sans l'erreur de double report (le 44567 présente 1 940 € au 31/08, soit le crédit d'août hors omission de juin).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/09/2026 | AC | 2154 | Matériel industriel (matériel de prise de vue) | Drone + caméras | 28 000,00 | |
| 15/09/2026 | AC | 44562 | TVA déductible sur immobilisations | Drone + caméras | 5 600,00 | |
| 15/09/2026 | AC | 404 | Fournisseurs d'immobilisations | Drone + caméras | | 33 600,00 |
| 30/09/2026 | OD | 44574 | TVA collectée en attente | SP-2026-014 Kanal Prod – TVA exigible au 20/06 non transférée | 1 600,00 | |
| 30/09/2026 | OD | 44571 | TVA collectée | SP-2026-014 – régularisation (ligne 5B) | | 1 600,00 |
| 30/09/2026 | OD | 44571 | TVA collectée | Liquidation CA3 09/2026 (2 200 + 1 600) | 3 800,00 | |
| 30/09/2026 | OD | 44583 | Remboursement de taxes sur le CA demandé | Demande 3519 – CA3 09/2026 | 4 860,00 | |
| 30/09/2026 | OD | 44562 | TVA déductible sur immobilisations | Liquidation CA3 09/2026 | | 5 600,00 |
| 30/09/2026 | OD | 44566 | TVA déductible sur ABS | Liquidation CA3 09/2026 | | 1 120,00 |
| 30/09/2026 | OD | 44567 | Crédit de TVA à reporter | Imputation du crédit d'août (comptable) | | 1 940,00 |
| 30/09/2026 | OD | 658 | Charges diverses de gestion courante – intérêts de retard (*subdivision selon la nomenclature 2025 du PCG*) | Intérêt de retard TVA juillet | 4,64 | |
| 30/09/2026 | OD | 4486 | État – charges à payer | Intérêt de retard TVA juillet | | 4,64 |
| (date de réception) | BQ | 512 | Banque | Remboursement crédit de TVA | 4 860,00 | |
| (date de réception) | BQ | 44583 | Remboursement de taxes sur le CA demandé | Remboursement crédit de TVA | | 4 860,00 |
| | | | | **Totaux** | **48 724,64** | **48 724,64** |

Rapprochement : la liquidation comptable (3 800 + 4 860 = 5 600 + 1 120 + 1 940 = 8 660) concorde avec la CA3, l'écart de 440 € entre le report déclaré (2 380) et le report comptable (1 940) étant exactement la somme ajoutée en ligne 5B ✔.

## 4. Points d'attention / pièges

- **Contrôle mensuel du 44574** : un solde correspondant à une facture **encaissée** est une TVA exigible oubliée. Rapprocher chaque mois 44574 et factures non encaissées (voir E04-07).
- **Ligne 22** : elle doit être égale à la ligne 27 de la déclaration précédente ; on corrige par des lignes de régularisation, pas en modifiant le report.
- **Une omission dans un mois créditeur n'est pas « sans conséquence »** : il faut dérouler la chaîne des crédits ; le retard apparaît dès qu'un mois corrigé devient débiteur.
- **Remboursement** : seuil de 760 € pour une demande en cours d'année (150 € pour la demande annuelle) ; le crédit remboursé est imputé sur le crédit de la période, la ligne 27 tombe à zéro.
- **Avant de demander un remboursement**, vérifier que les déclarations antérieures sont exactes : la demande attire l'attention de l'administration.

## 5. Ce qu'un senior ferait en plus

**Dossier de remboursement** (prêt à transmettre au SIE) : factures du drone et des caméras, preuves de paiement, fiche d'immobilisation, explication du crédit (investissements de démarrage, CA encore modeste), Kbis, statuts, option pour le réel normal, chaîne des crédits juin–septembre avec la note de régularisation.

**Mail à Léo et Sarah :**
> Bonjour, bonne nouvelle : le crédit de TVA est remboursable. Après correction de deux erreurs (la TVA de la facture Kanal Prod de juin, non déclarée, et un crédit reporté deux fois en août), le montant à demander est de 4 860 €, au lieu des 7 000 € environ que vous espériez. Nous régularisons spontanément sur la déclaration de septembre, ce qui limite les intérêts à moins de 5 €. Attendez-vous à une demande de justificatifs du service des impôts : nous avons préparé le dossier.

**Process** : écriture automatique 44574 → 44571 à l'encaissement (paramétrage du logiciel), contrôle de la ligne 22 avant chaque dépôt, tableau de suivi de la chaîne des crédits.

## 6. Références

- CGI : art. 269-2-c (exigibilité), art. 271 IV (imputation et remboursement des crédits), art. 1727 (intérêt de retard).
- Annexe II au CGI : art. 242-0 A et suivants (conditions et seuils des remboursements de crédits — *valeurs à vérifier*).
- LPF : régularisation spontanée et droit à l'erreur (loi n° 2018-727 du 10 août 2018, dite ESSOC).
- Notice des formulaires 3310-CA3 et 3519.
- PCG : comptes 44562, 44566, 44567, 44571, 44574, 44583.
