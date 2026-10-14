# Corrigé E15-09 — Test technique : emprunt à annuités constantes, intérêts courus, crédit-bail et LCR fournisseur

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-09](../exercices/E15-09_emprunt-credit-bail-lcr.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### L'emprunt : capital et intérêts, deux natures différentes
- Le **capital** reçu de la banque est une **dette** (164). Le rembourser **diminue la dette** : ce n'est pas une charge.
- Les **intérêts** sont le prix de l'argent emprunté : c'est une **charge financière** (6611).
- Chaque annuité = **intérêts** (calculés sur le capital restant dû) + **remboursement du capital** (le reste). Avec des annuités constantes, les intérêts baissent chaque année (le capital dû baisse) et la part de capital augmente.

### Le déblocage
La banque prête 60 000,00 € mais retient 300,00 € de frais de dossier : le compte bancaire ne reçoit que 59 700,00 €. La dette, elle, est bien de **60 000,00 €** (c'est ce qu'on remboursera). Les frais vont en charge (option retenue par le groupe ; le PCG permet aussi de les étaler sur la durée de l'emprunt).

### Les intérêts courus au 31/12/2026
La première échéance tombe le 30/06/2027 et paiera 12 mois d'intérêts (du 01/07/2026 au 30/06/2027). Six de ces mois (juillet à décembre 2026) concernent **2026** : on les rattache à 2026 par une écriture d'**intérêts courus non échus** (6611 au débit, 1688 au crédit). On extourne au 01/01/2027 : quand l'échéance de juin 2027 passera 2 400,00 € en 6611, l'extourne (−1 200,00 €) laissera en 2027 seulement les 6 mois qui la concernent.

### Le crédit-bail : on loue, on n'est pas propriétaire
Pendant le contrat, le véhicule appartient à **Azur Leasing**. Dans les **comptes sociaux** de GSF Riviera, on enregistre seulement les **loyers en charge** (6122), et on informe le lecteur des comptes par une mention en **annexe** (engagements de crédit-bail). Le retraitement « comme un achat financé par emprunt » ne se fait qu'en comptes consolidés (non demandé ici). Si l'option d'achat est levée à la fin, le véhicule entrera alors à l'actif pour 2 000,00 € HT.

### La LCR : la dette change de forme
Une LCR (lettre de change relevé) est un effet de commerce : quand GSF Riviera donne son « bon à payer », la dette **fournisseur ordinaire** (401) devient une **dette sous forme d'effet** (403). Le montant ne change pas ; seul le compte change. À l'échéance, la banque paie : 403 est soldé par 512.

## 2. Calculs (détaillés, chaque montant justifié)

**Annuité constante (question 1)**

| Étape | Calcul | Résultat |
|---|---|---|
| (1 + i)^−n | 1,04^−5 | 0,821927 |
| 1 − (1 + i)^−n | 1 − 0,821927 | 0,178073 |
| C × i | 60 000,00 × 4 % | 2 400,00 |
| Annuité | 2 400,00 / 0,178073 | **13 477,63 €** (13 477,6268… arrondi au centime) |

**Tableau d'amortissement (question 2)**

| Échéance | Capital début | Intérêts (4 %) | Amortissement du capital | Annuité | Capital fin |
|---|---|---|---|---|---|
| 30/06/2027 | 60 000,00 | 2 400,00 | 11 077,63 | 13 477,63 | 48 922,37 |
| 30/06/2028 | 48 922,37 | 1 956,89 | 11 520,74 | 13 477,63 | 37 401,63 |
| 30/06/2029 | 37 401,63 | 1 496,07 | 11 981,56 | 13 477,63 | 25 420,07 |
| 30/06/2030 | 25 420,07 | 1 016,80 | 12 460,83 | 13 477,63 | 12 959,24 |
| 30/06/2031 | 12 959,24 | 518,37 | 12 959,24 | **13 477,61** | 0,00 |
| **Total** | | **7 388,13** | **60 000,00** | **67 388,13** | |

Méthode pour chaque ligne : intérêts = capital début × 4 % ; amortissement = annuité − intérêts ; capital fin = capital début − amortissement. **Écart d'arrondi** : l'annuité arrondie au centime fait rembourser un peu trop chaque année ; la dernière annuité est **ajustée** pour solder exactement le capital (13 477,61 € au lieu de 13 477,63 €). C'est la banque qui fixe le chiffre définitif : on recopie **son** tableau, après l'avoir contrôlé.

| Élément | Calcul | Montant |
|---|---|---|
| Fonds reçus en banque | 60 000,00 − 300,00 | 59 700,00 € |
| ICNE au 31/12/2026 (question 4) | 60 000,00 × 4 % × 6/12 | **1 200,00 €** |
| Charge d'intérêts 2027 sur l'échéance de juin | 2 400,00 − 1 200,00 (extourne) | 1 200,00 € |

**Dette au bilan du 31/12/2026 (question 6)**

| Élément | Calcul | Montant |
|---|---|---|
| Emprunt (164) | aucun remboursement en 2026 | 60 000,00 € |
| Intérêts courus (1688) | ICNE | 1 200,00 € |
| **Total dette financière** | | **61 200,00 €** |
| Dont à moins d'un an | capital remboursé le 30/06/2027 (11 077,63) + ICNE (1 200,00) | **12 277,63 €** |
| Dont à plus d'un an | 60 000,00 − 11 077,63 | **48 922,37 €** (aucune part à plus de 5 ans) |

**Crédit-bail (question 7)**

| Élément | Calcul | Montant |
|---|---|---|
| Loyer mensuel TTC | 690,00 × 1,20 | 828,00 € |
| Charge 2026 | 3 loyers (octobre, novembre, décembre) × 690,00 | 2 070,00 € HT |
| Loyers restant à payer au 31/12/2026 | (48 − 3) × 690,00 = 45 × 690,00 | 31 050,00 € HT |
| Prix de l'option d'achat | contrat | 2 000,00 € HT |
| Engagement à mentionner en annexe | 31 050,00 + 2 000,00 | **33 050,00 € HT** |

**LCR (question 8)** : TTC 7 200,00 + 1 440,00 = 8 640,00 €.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/07/2026 | BQ | 512 | Banque | Déblocage prêt Banque du Comté – autolaveuses | 59 700,00 | |
| 01/07/2026 | BQ | 627 | Services bancaires et assimilés | Frais de dossier prêt Banque du Comté | 300,00 | |
| 01/07/2026 | BQ | 164 | Emprunts auprès des établissements de crédit | Prêt Banque du Comté 60 000 € 4 % 5 ans | | 60 000,00 |
| 01/10/2026 | AC | 6122 | Redevances de crédit-bail mobilier | Azur Leasing – loyer 10/2026 fourgon électrique | 690,00 | |
| 01/10/2026 | AC | 44566 | TVA déductible sur autres biens et services | Azur Leasing – TVA loyer 10/2026 | 138,00 | |
| 01/10/2026 | AC | 401 | Fournisseurs | Azur Leasing – loyer 10/2026 | | 828,00 |
| 15/10/2026 | AC | 6022 | Fournitures consommables | Hygiène Pro Méditerranée HPM-26-2290 | 7 200,00 | |
| 15/10/2026 | AC | 44566 | TVA déductible sur autres biens et services | HPM-26-2290 TVA 20 % | 1 440,00 | |
| 15/10/2026 | AC | 401 | Fournisseurs | Hygiène Pro Méditerranée HPM-26-2290 | | 8 640,00 |
| 22/11/2026 | OD | 401 | Fournisseurs | Bon à payer LCR HPM-26-2290 éch. 30/11/2026 | 8 640,00 | |
| 22/11/2026 | OD | 403 | Fournisseurs – effets à payer | LCR HPM-26-2290 éch. 30/11/2026 | | 8 640,00 |
| 30/11/2026 | BQ | 403 | Fournisseurs – effets à payer | Paiement LCR HPM-26-2290 | 8 640,00 | |
| 30/11/2026 | BQ | 512 | Banque | Paiement LCR HPM-26-2290 | | 8 640,00 |
| 31/12/2026 | OD | 6611 | Intérêts des emprunts et dettes | ICNE prêt Banque du Comté 01/07-31/12/2026 | 1 200,00 | |
| 31/12/2026 | OD | 1688 | Intérêts courus | ICNE prêt Banque du Comté | | 1 200,00 |
| 01/01/2027 | OD | 1688 | Intérêts courus | Extourne ICNE prêt Banque du Comté | 1 200,00 | |
| 01/01/2027 | OD | 6611 | Intérêts des emprunts et dettes | Extourne ICNE prêt Banque du Comté | | 1 200,00 |
| 30/06/2027 | BQ | 164 | Emprunts auprès des établissements de crédit | Échéance 1/5 prêt Banque du Comté – capital | 11 077,63 | |
| 30/06/2027 | BQ | 6611 | Intérêts des emprunts et dettes | Échéance 1/5 prêt Banque du Comté – intérêts | 2 400,00 | |
| 30/06/2027 | BQ | 512 | Banque | Échéance 1/5 prêt Banque du Comté | | 13 477,63 |
| | | | | **Totaux** | **102 625,63** | **102 625,63** |

> Les loyers de novembre et décembre 2026 se passent comme celui d'octobre (690,00 € en 6122, 138,00 € de TVA, 828,00 € en 401), suivis de leur règlement (401 / 512).

**Pourquoi ce sens ?**
- Déblocage : la banque **reçoit** de l'argent → 512 au débit ; la dette **naît** → 164 au crédit.
- Échéance : la dette **diminue** → 164 au débit ; la charge d'intérêts **augmente** → 6611 au débit ; l'argent **sort** → 512 au crédit.
- LCR : la dette 401 **disparaît** (débit) et une dette 403 **apparaît** (crédit) pour le même montant.

## 4. Points d'attention / pièges

- **Brouillon pièce 4, ligne 1** : passer les 13 477,63 € en 6611 gonfle les charges de 11 077,63 € et laisse au bilan une dette 164 qui ne baisse jamais. Seuls les **intérêts** sont une charge.
- **Brouillon pièce 4, ligne 2** : immobiliser le véhicule en crédit-bail est faux dans les comptes sociaux français : GSF Riviera n'en est pas propriétaire. On passe les loyers en 6122 et on mentionne l'engagement en annexe. En plus, le brouillon créerait une dette de 34 500,00 € qui n'existe pas en 401.
- **Dette au déblocage** : c'est 60 000,00 €, pas 59 700,00 € (les frais ne réduisent pas ce qu'on doit à la banque).
- **ICNE** : penser à l'**extourne** au 01/01, sinon les 1 200,00 € d'intérêts de 2026 seraient comptés deux fois (en 2026 et dans l'échéance de 2027).
- **Moins d'un an / plus d'un an** : l'échéancier des dettes de l'annexe se fait à partir du tableau d'amortissement, pas « au feeling ». Les intérêts courus sont à moins d'un an.
- **LCR** : ne pas débiter 512 dès le bon à payer ; la banque ne paie qu'à l'échéance. Entre les deux, la dette est en 403.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Phrase d'entretien (30 secondes) :**
> « Pour un emprunt, je récupère le tableau d'amortissement de la banque et je le contrôle. À chaque échéance, le capital diminue le 164 et seuls les intérêts vont en 6611. À la clôture, je calcule les intérêts courus depuis la dernière échéance et je les extourne au 1er janvier. Et je vérifie que le solde du 164 égale le capital restant dû du tableau. Pour un crédit-bail, je passe les loyers en charges et je prépare l'engagement pour l'annexe. »

**Contrôle mensuel / annuel** : rapprochement du solde 164 avec le capital restant dû du tableau de la banque ; contrôle que le compte 403 ne contient que des LCR à échéance future (un 403 ancien = paiement non comptabilisé) ; liste des contrats de crédit-bail avec loyers restants pour l'annexe.

**Dossier** : offre de prêt signée, tableau d'amortissement de la banque, contrat de crédit-bail, relevés LCR avec bon à payer.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 164, 1688, 403, 6122, 6611, 627 ; règles relatives aux contrats de location et de crédit-bail dans les comptes individuels (loyers en charges, pas d'inscription à l'actif).
- PCG, règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06 : nomenclature des comptes de frais d'émission d'emprunt et de services bancaires (*subdivision à vérifier dans la nomenclature 2025*).
- Code de commerce : informations à fournir en annexe (engagements financiers, dont crédit-bail ; échéances des dettes) — *articles à citer selon la taille de l'entreprise*.
- Code de commerce : régime de la lettre de change (effets de commerce).
