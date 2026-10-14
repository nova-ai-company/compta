# Corrigé E07-07 — Cotisations SSI de la gérante d'une EURL à l'IR : provisionnelles, régularisation, prélèvements

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-07](../exercices/E07-07_cotisations-ssi-style-vous.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **Statut fiscal** : Style & Vous est une EURL **non optante à l'IS**. Le bénéfice est imposé au nom de Nadia dans la catégorie BIC (2031). Juridiquement, la « rémunération » de la gérante associée unique **n'est pas une charge déductible** : c'est un prélèvement sur un bénéfice qui lui appartient déjà fiscalement → **compte 108 « Compte de l'exploitant »**.
2. **Impôt sur le revenu personnel** : les acomptes de prélèvement à la source sur ses BIC sont l'impôt **personnel** de Nadia → 108 également (jamais en 63x : l'IR n'est pas une charge de l'entreprise).
3. **Cotisations sociales personnelles obligatoires** : elles sont des **charges** de l'entreprise (646), déductibles du BIC, **sauf la CSG non déductible et la CRDS** (2,9 points), à **réintégrer** extra-comptablement.
4. **Mécanisme SSI** : en année N, l'URSSAF appelle des **provisionnelles** sur la dernière assiette connue (N-2 en début d'année, puis N-1 après la déclaration de revenus du printemps) ; en N+1, elle **régularise** sur le revenu définitif de N. Les revenus de Nadia augmentant (37 000 € → 46 000 € → ~52 000 €), elle subit une double hausse en 2026 : complément 2025 + provisionnelles 2026 recalculées.
5. **Engagement** : le cabinet tient la comptabilité en droits constatés : la régularisation prévisible de l'exercice est une **charge à payer** à la clôture (déjà fait au 31/12/2025 pour 3 000 €, à refaire au 31/12/2026).

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 Régularisation 2025 dans les comptes 2026
- Complément définitif notifié : 3 500,00 €.
- Charge à payer constatée au 31/12/2025 : 3 000,00 €.
- **Complément de charge 2026** (insuffisance d'estimation) : **500,00 €**.

### 2.2 Provisionnelles 2026
19 800,00 € (12 150,00 déjà payés + 3 × 2 550,00).

### 2.3 Charge à payer au 31/12/2026
22 600,00 (estimation définitive 2026) − 19 800,00 (provisionnelles) = **2 800,00 €**, dont :
- cotisations sociales : 17 556 − 15 338 = 2 218,00 € ;
- CSG déductible : 3 536 − 3 128 = 408,00 € ;
- CSG non déductible + CRDS : 1 508 − 1 334 = **174,00 €**.

### 2.4 Total en charges 2026 (compte 646)

| Élément | Montant |
|---|---|
| Provisionnelles 2026 | 19 800,00 |
| Complément régularisation 2025 | 500,00 |
| Charge à payer régularisation 2026 | 2 800,00 |
| **Total 646** | **23 100,00** |

### 2.5 Réintégration fiscale 2026 (CSG non déductible + CRDS)

| Origine | Montant |
|---|---|
| Provisionnelles 2026 | 1 334,00 |
| Régularisation 2025 (non isolée dans l'estimation de 2025, donc jamais réintégrée) | 261,00 |
| Charge à payer 2026 | 174,00 |
| **Total à réintégrer** | **1 769,00** |

> Variante : on peut comptabiliser directement la CSG non déductible et la CRDS au **débit du 108** (et non en 646) : elle n'est alors ni en charge, ni à réintégrer. Les deux méthodes sont admises ; l'essentiel est la **constance** et la **traçabilité** dans le dossier.

### 2.6 Corrections
- 644 → 108 : 9 × 2 500 = **22 500,00 €**.
- 6354 → 108 : 9 × 420 = **3 780,00 €**.
- Impact : le bénéfice comptable 2026 **augmente** de 26 280,00 € par rapport au provisoire. Ce n'est pas une « hausse d'impôt » : de toute façon, ces sommes n'étaient pas déductibles et le bénéfice fiscal aurait dû être corrigé.

## 3. Écritures comptables

**Corrections des prélèvements de la gérante (cumul janvier → septembre)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 108 | Compte de l'exploitant | Reclassement prélèvements N. Belkacem 01-09/2026 | 22 500,00 | |
| 30/09/2026 | OD | 644 | Rémunération du travail de l'exploitant | Reclassement prélèvements N. Belkacem 01-09/2026 | | 22 500,00 |
| 30/09/2026 | OD | 108 | Compte de l'exploitant | Reclassement acomptes PAS BIC (IR personnel) | 3 780,00 | |
| 30/09/2026 | OD | 6354 | Droits d'enregistrement et de timbre | Reclassement acomptes PAS BIC (IR personnel) | | 3 780,00 |
| | | | | **Totaux** | **26 280,00** | **26 280,00** |

**Avis URSSAF du 18/06/2026 (régularisation 2025)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 18/06/2026 | OD | 4386 | Organismes sociaux – autres charges à payer | Solde estimation régul. 2025 | 3 000,00 | |
| 18/06/2026 | OD | 646 | Cotisations sociales personnelles de l'exploitant | Complément régul. 2025 | 500,00 | |
| 18/06/2026 | OD | 437 | URSSAF – cotisations personnelles de l'exploitant (*subdivision du dossier*) | Régularisation 2025 à payer | | 3 500,00 |
| | | | | **Totaux** | **3 500,00** | **3 500,00** |

**Prélèvements URSSAF du 05/10/2026** (même écriture les 05/11 et 05/12, la dernière fraction de régularisation étant de 1 166,66 €)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/10/2026 | BQ | 646 | Cotisations sociales personnelles de l'exploitant | Provisionnelle SSI 10/2026 | 2 550,00 | |
| 05/10/2026 | BQ | 437 | URSSAF – cotisations personnelles de l'exploitant | Régularisation 2025 – 1re fraction | 1 166,67 | |
| 05/10/2026 | BQ | 512 | Banque | Prélèvement URSSAF 05/10/2026 | | 3 716,67 |
| | | | | **Totaux** | **3 716,67** | **3 716,67** |

**Clôture au 31/12/2026**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 646 | Cotisations sociales personnelles de l'exploitant | Estimation régularisation SSI 2026 | 2 800,00 | |
| 31/12/2026 | OD | 4386 | Organismes sociaux – autres charges à payer | Estimation régularisation SSI 2026 | | 2 800,00 |
| | | | | **Totaux** | **2 800,00** | **2 800,00** |

Contrôle au 31/12/2026 : 437 soldé (3 500,00 − 3 × 1 166,67/1 166,67/1 166,66) ; 646 = 12 150 + 3 × 2 550 + 500 + 2 800 = **23 100,00 €** ✔.

## 4. Points d'attention / pièges

- **Ne jamais passer en charges** les prélèvements de l'exploitant, son IR, ses dépenses personnelles : tout va au 108. Le 644 n'est utilisé qu'en **société à l'IS** pour un gérant majoritaire.
- **Réintégration CSG/CRDS** : elle se fait sur la ligne prévue du tableau de détermination du résultat fiscal (2033-B / 2031) — à ne pas oublier, c'est un point de contrôle classique en cas d'examen de la liasse.
- **Contrat Madelin / cotisations facultatives** : déductibles dans des plafonds spécifiques (article 154 bis du CGI) ; à suivre sur un sous-compte distinct de 646 et à vérifier chaque année.
- **Réforme de l'assiette** des cotisations des indépendants (revenus 2025 et suivants) : les simulations « de tête » sont devenues risquées ; utilisez le simulateur officiel et documentez l'hypothèse de revenu retenue.
- **Modulation** : Nadia peut demander à moduler ses provisionnelles si elle anticipe une baisse ; inversement, si son revenu grimpe, elle s'expose à une forte régularisation l'année suivante : prévoir la **trésorerie**.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- Mettre en place un **virement mensuel fixe** vers le compte personnel (108) et un **compte épargne de précaution** pour les régularisations.
- Paramétrer le dossier : comptes 644 et 6354 **interdits** pour cette EURL ; libellés bancaires « DGFIP PAS BIC » affectés automatiquement au 108.
- Documenter dans le dossier permanent : statut fiscal (IR), statut social (TNS), méthode CSG/CRDS retenue.
- **Réponse à Nadia** :

> Bonjour Nadia,
> L'URSSAF fonctionne en deux temps : elle vous fait payer chaque année des acomptes calculés sur vos revenus passés, puis elle régularise lorsqu'elle connaît le revenu réel. Votre revenu 2025 (46 000 €) étant plus élevé que celui qui avait servi aux acomptes, elle vous demande 3 500 € de complément et relève vos mensualités 2026. Ces cotisations sont bien déductibles de votre bénéfice (sauf une petite part de CSG/CRDS). Avec un revenu 2026 estimé à 52 000 €, prévoyez environ 2 800 € de complément l'an prochain.
> Pour l'IS : votre rémunération deviendrait effectivement déductible, mais le bénéfice restant serait soumis à l'IS, puis à l'imposition des dividendes, et une partie des dividendes supporterait des cotisations sociales. Le choix (en principe irrévocable passé un délai) dépend de votre niveau de revenus et de vos besoins : nous vous proposons une simulation chiffrée lors du bilan.
> Bien cordialement,

## 6. Références

- CGI : article 8 (EURL à l'IR, transparence), article 154 bis (déductibilité des cotisations sociales personnelles et des contrats Madelin), article 154 quinquies (CSG déductible).
- Code de la sécurité sociale : articles L. 131-6 et suivants (assiette des cotisations des travailleurs indépendants), L. 131-6-2 (provisionnelles et régularisation), réforme de l'assiette issue de la LFSS pour 2024 — *paramètres à vérifier*.
- PCG : comptes 108, 437, 4386, 646.
