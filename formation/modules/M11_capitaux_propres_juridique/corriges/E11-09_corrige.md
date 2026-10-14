# Corrigé E11-09 — Mode & Co : une distribution votée supérieure au bénéfice distribuable

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-09](../exercices/E11-09_distribution-illegale-mode-and-co.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Le réflexe** : avant de comptabiliser (et a fortiori de payer) un dividende, on refait **soi-même** le calcul du bénéfice distribuable. Un PV signé et déposé ne rend pas légale une distribution qui ne l'est pas.

**Ce que la plateforme a oublié** :
1. Le **report à nouveau débiteur** (– 48 500 €) doit être **apuré en priorité** : le bénéfice distribuable est le bénéfice **diminué des pertes antérieures** (art. L. 232-11 C. com.). On ne peut pas distribuer tant que les pertes passées ne sont pas couvertes.
2. La **réserve légale** : 5 % du bénéfice **diminué des pertes antérieures** (art. L. 232-10), soit 5 % × (61 800 – 48 500). La réserve (1 200 €) n'a pas atteint le dixième du capital (3 000 €) : la dotation est obligatoire.
3. Il n'existe **aucune réserve distribuable** (1068 = 0) qui pourrait compléter.

**Le « quitus »** de la première résolution : clause usuelle mais **sans effet** sur la responsabilité de la gérance (une décision de l'assemblée ne peut éteindre l'action en responsabilité contre le gérant, art. L. 223-22 C. com.) — à supprimer des modèles du cabinet.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Bénéfice 2025 | | 61 800,00 |
| – Pertes antérieures (report à nouveau débiteur) | | – 48 500,00 |
| = Bénéfice après imputation des pertes | | 13 300,00 |
| – Réserve légale | 5 % × 13 300 = 665 (plafond restant : 3 000 – 1 200 = 1 800 → non atteint) | – 665,00 |
| + Report à nouveau bénéficiaire | aucun | 0,00 |
| **= Bénéfice distribuable** | | **12 635,00** |
| + Réserves disponibles | aucune | 0,00 |
| **= Maximum distribuable** | | **12 635,00** |
| Distribution votée | | 30 000,00 |
| **Excédent irrégulier (dividende fictif)** | 30 000 – 12 635 | **17 365,00** |

Dividende maximal par part : 12 635 / 3 000 = 4,2117 € → arrondi **4,20 € par part = 12 600,00 €** ; solde au report à nouveau : 12 635 – 12 600 = **35,00 €**.

Contrôle du second verrou : capitaux propres après distribution = 30 000 + 1 200 + 665 + 35 = **31 900 €** ≥ capital + réserve légale (31 865 €) ✓.

**Affectation régulière**

| Affectation du bénéfice 2025 (61 800 €) | Montant |
|---|---|
| Apurement du report à nouveau débiteur | 48 500,00 |
| Réserve légale | 665,00 |
| Dividendes (4,20 € × 3 000 parts) | 12 600,00 |
| Report à nouveau (créditeur) | 35,00 |
| **Total** | **61 800,00** |

**Retenues sur le dividende de 12 600 €** (paiement le 16/11/2026)

| | Inès (2 100 parts, gérante majoritaire) | Théo (900 parts) | Total |
|---|---|---|---|
| Brut | 8 820,00 | 3 780,00 | 12 600,00 |
| Seuil 10 % (capital détenu 21 000 €, pas de prime ni de compte courant) | 2 100,00 | sans objet | |
| PFNL 12,8 % sur le brut | 1 128,96 | 483,84 | 1 612,80 |
| Prélèvements sociaux 18,6 % | 2 100 × 18,6 % = 390,60 | 3 780 × 18,6 % = 703,08 | 1 093,68 |
| **Net versé** | **7 300,44** | **2 593,08** | **9 893,52** |
| Fraction soumise aux cotisations TNS (déclarée par Inès) | 6 720,00 | — | |

Contrôle : 12 600 – 1 612,80 – 1 093,68 = 9 893,52 ✓.

## 3. Écritures comptables

**Correction de l'affectation** (à la date de la nouvelle assemblée, le 26/10/2026)

L'écriture du junior a laissé 457 = 30 000 € et 119 = 16 700 € débiteur. La situation correcte est : 457 = 12 600 € ; 119 soldé ; 1061 + 665 € ; 110 = 35 €.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 26/10/2026 | OD | 457 | Associés – dividendes à payer | Rectif. affectation 2025 – AGO 26/10/2026 (30 000 → 12 600) | 17 400,00 | |
| 26/10/2026 | OD | 119 | Report à nouveau débiteur | Apurement total des pertes antérieures | | 16 700,00 |
| 26/10/2026 | OD | 1061 | Réserve légale | Dotation 5 % × (61 800 – 48 500) | | 665,00 |
| 26/10/2026 | OD | 110 | Report à nouveau créditeur | Solde bénéfice 2025 | | 35,00 |
| 16/11/2026 | BQ | 457 | Associés – dividendes à payer | Paiement dividendes 2025 (4,20 €/part) | 12 600,00 | |
| 16/11/2026 | BQ | 4422 | Prélèvements forfaitaires non libératoires | PFNL 12,8 % (I. 1 128,96 / T. 483,84) | | 1 612,80 |
| 16/11/2026 | BQ | 4423 | Retenues et prélèvements sur distributions | Prélèvements sociaux (I. 390,60 / T. 703,08) | | 1 093,68 |
| 16/11/2026 | BQ | 512 | Banque | Vir. dividendes nets (I. 7 300,44 / T. 2 593,08) | | 9 893,52 |
| 15/12/2026 | BQ | 4422 | Prélèvements forfaitaires non libératoires | 2777 – novembre 2026 | 1 612,80 | |
| 15/12/2026 | BQ | 4423 | Retenues et prélèvements sur distributions | 2777 – novembre 2026 | 1 093,68 | |
| 15/12/2026 | BQ | 512 | Banque | Télérèglement 2777 – novembre 2026 | | 2 706,48 |
| | | | | **Totaux** | **32 706,48** | **32 706,48** |

Contrôle des soldes après correction : 119 = 48 500 – 31 800 – 16 700 = 0 ✓ ; 1061 = 1 865 € ; 110 = 35 € ; 457 = 30 000 – 17 400 – 12 600 = 0 ✓ après paiement.

## 4. Points d'attention / pièges

- **Report à nouveau débiteur = priorité absolue** : « on affecte le solde au report à nouveau » n'est correct qu'**après** avoir couvert les pertes antérieures.
- **Base de la réserve légale** : bénéfice **diminué des pertes antérieures** (13 300 €), et non le bénéfice brut (5 % × 61 800 = 3 090 € serait faux).
- **Un PV déposé au greffe n'est pas une garantie de légalité** : il faut un **dépôt rectificatif** de la décision d'affectation.
- **Ne pas payer avant régularisation** : une fois versé, le dividende fictif expose les associés à la répétition et la gérante au risque pénal.
- **Date de paiement** : le 15/11/2026 est un dimanche → paiement le lundi 16/11/2026, 2777 au **15/12/2026** au plus tard.
- **Dividendes d'Inès** : gérante majoritaire de SARL → règle des 10 % (seuil 2 100 €) ; ne pas retenir de prélèvements sociaux sur les 6 720 € soumis aux cotisations.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 2 — Si les 30 000 € avaient été versés**
- **Civil** : distribution contraire à l'art. L. 232-11 → la société peut exiger la **répétition** des sommes indûment versées (art. L. 232-17 C. com. ; action prescrite par 3 ans à compter de la mise en paiement). Ici, Inès et Théo, associés et signataires, ne pourraient prétendre ignorer l'irrégularité.
- **Pénal** : la **répartition de dividendes fictifs** est un délit pour le gérant de SARL (art. L. 241-3 C. com. — *éléments constitutifs, notamment l'absence d'inventaire ou l'inventaire frauduleux, à apprécier au cas par cas*). Le cabinet n'a pas à s'exposer à une complicité : on alerte **par écrit**.
- **Fiscal** : les sommes versées restent des **revenus distribués** imposables (art. 109 CGI) au moment du paiement ; une restitution ultérieure ne fait pas disparaître automatiquement l'imposition (*traitement de la restitution à vérifier*). Les retenues (PFNL, prélèvements sociaux) seraient dues sur 30 000 €.
- **Banque, investisseurs, repreneurs** : capitaux propres affaiblis de 17 365 € de façon irrégulière.

**Question 3 — Régularisation (rien n'a été payé)**
- La décision de distribution a créé une **créance** des associés (457) ; elle ne peut être modifiée unilatéralement. Comme **les deux associés** sont d'accord et que la décision est **contraire à la loi**, on réunit une **nouvelle assemblée** (ou, si les statuts le permettent, une **décision unanime par acte sous seing privé**) qui **rapporte** la deuxième résolution du 29/06/2026 et adopte une affectation régulière. Les associés **renoncent expressément** au surplus. Majorité : celle des décisions ordinaires, mais l'**unanimité** est recherchée (renonciation individuelle à une créance).
- Délai : avant la date de paiement (16/11/2026), idéalement fin octobre ; les comptes 2025 restent approuvés (la première résolution n'est pas en cause).
- Formalités : **dépôt rectificatif** au greffe de la décision d'affectation (dans le mois) ; mise à jour de la mention de l'art. 243 bis pour les exercices suivants.
- Délai de paiement des dividendes : 9 mois après la clôture → **30/09/2026**, déjà dépassé ! La mise en paiement au 30/11 votée en juin nécessitait une **prolongation** par ordonnance du président du tribunal de commerce, sur requête **avant** l'expiration du délai. Le dépassement n'annule pas la distribution, mais le cabinet le signale à Inès (*sanctions éventuelles à vérifier*).

**Question 4 — Projets de résolutions**

> **MODE & CO — SARL au capital de 30 000 € — RCS Lyon 851 777 890**
> **Assemblée générale ordinaire réunie extraordinairement le 26 octobre 2026**
>
> **Première résolution — Retrait de la deuxième résolution de l'assemblée du 29 juin 2026.** L'assemblée générale, après avoir pris connaissance du rapport de la gérance exposant que la deuxième résolution adoptée par l'assemblée générale ordinaire du 29 juin 2026 a décidé une distribution de dividendes de 30 000 € excédant le bénéfice distribuable de l'exercice clos le 31 décembre 2025, qui s'élève à 12 635 €, et constatant qu'aucune somme n'a été mise en paiement, décide de rapporter ladite résolution. Chacun des associés déclare renoncer à toute créance née de cette résolution.
>
> **Deuxième résolution — Affectation du résultat de l'exercice clos le 31 décembre 2025.** L'assemblée générale, constatant que le bénéfice de l'exercice s'élève à 61 800,00 € et que le report à nouveau antérieur est débiteur de 48 500,00 €, décide d'affecter le bénéfice comme suit :
> - imputation sur le report à nouveau débiteur, qui est ainsi intégralement apuré : 48 500,00 € ;
> - dotation à la réserve légale (5 % du bénéfice diminué des pertes antérieures) : 665,00 €, portant celle-ci à 1 865,00 € ;
> - distribution aux associés à titre de dividendes : 12 600,00 €, soit 4,20 € par part ;
> - report à nouveau : 35,00 €.
>
> Les dividendes seront mis en paiement le 16 novembre 2026. Il est rappelé que les dividendes versés aux associés personnes physiques sont soumis, lors de leur paiement, au prélèvement forfaitaire non libératoire et aux prélèvements sociaux, sous réserve de l'article L. 131-6 du Code de la sécurité sociale, et qu'ils sont éligibles, en cas d'option pour le barème progressif, à l'abattement de 40 % (art. 158, 3-2° du CGI). Conformément à l'article 243 bis du CGI, l'assemblée prend acte qu'aucun dividende n'a été distribué au titre des exercices 2022, 2023 et 2024 [*à vérifier sur les PV antérieurs*].
>
> **Troisième résolution — Pouvoirs.** L'assemblée générale confère tous pouvoirs au porteur d'une copie ou d'un extrait du présent procès-verbal pour effectuer le dépôt rectificatif de la décision d'affectation au greffe du tribunal de commerce de Lyon et toutes autres formalités.
>
> *Chaque résolution est adoptée à l'unanimité des associés (3 000 parts).*

**Réponse à Inès (question 6)**

> Bonjour Inès,
>
> Avant de préparer le paiement, nous avons vérifié la décision du 29 juin : **elle ne peut pas être exécutée en l'état**. Les pertes de 2023-2024 (48 500 €) devaient être compensées en priorité par le bénéfice 2025, et une part du bénéfice devait aller à la réserve légale. Le montant maximum distribuable est de **12 635 €**, et non 30 000 €. Verser 30 000 € reviendrait à distribuer 17 365 € de « dividendes fictifs » : vous et Théo pourriez être tenus de les rembourser, et la responsabilité pénale de la gérante pourrait être engagée.
>
> Bonne nouvelle : rien n'a été payé. Nous vous proposons une nouvelle décision, que nous pouvons rédiger (lettre de mission complémentaire jointe), d'ici le 26 octobre : dividende de **4,20 € par part (12 600 €)**, versé le 16 novembre. Vous recevrez **7 300,44 €** net (sur 8 820 € brut ; une partie, 6 720 €, sera soumise à vos cotisations sociales de gérante majoritaire), Théo **2 593,08 €** net (sur 3 780 €). Nous déclarerons les 2 706,48 € de prélèvements sur la 2777 avant le 15 décembre.
>
> Si vous souhaitez percevoir davantage en 2026, parlons d'une **rémunération** de gérance, qui serait déductible du résultat 2026. Et pour l'avenir, nous vous conseillons de nous confier la préparation des assemblées.

**Contrôles / dossier** :
- Note au dossier signée d'Hélène Ferrand sur l'irrégularité constatée et l'alerte donnée (traçabilité de la diligence du cabinet).
- Revue de la **lettre de mission** (juridique hors mission → avenant).
- Contrôle de la balance 2026 : 120 soldé, 457 cohérent avec les PV, 119 apuré.
- Mise en place d'une **checklist « distribution »** obligatoire pour toute écriture au crédit du 457.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. **L. 232-10** (réserve légale, base après pertes antérieures), art. **L. 232-11** (bénéfice distribuable, pertes antérieures), art. L. 232-12 al. 3 (dividendes fictifs), art. **L. 232-13** (mise en paiement dans les 9 mois, prolongation judiciaire), art. **L. 232-17** (répétition, prescription de 3 ans), art. **L. 241-3** (délits des gérants de SARL), art. L. 223-22 (responsabilité des gérants, inefficacité du quitus), art. L. 232-22 (dépôt au greffe).
- CGI : art. 109 et suivants (revenus distribués), art. 117 quater, 200 A, 158-3-2°, 243 bis.
- Code de la sécurité sociale : art. L. 131-6.
- PCG : comptes 1061, 110, 119, 120, 457, 442.
