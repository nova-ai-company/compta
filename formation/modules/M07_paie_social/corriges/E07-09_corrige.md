# Corrigé E07-09 — Réserve spéciale de participation : calcul, comptabilisation, fiscalité et correction

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-09](../exercices/E07-09_participation-imprimerie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **Obligation** : avec 52 salariés (seuil de 50 franchi pendant 5 années civiles consécutives selon les règles du CSS), l'Imprimerie doit appliquer au minimum la **formule légale** : **RSP = ½ × (B − 5 % C) × S / VA**.
2. **Les quatre termes** se lisent dans la liasse, mais avec des pièges :
   - **B** = bénéfice **fiscal** (pas comptable) imposable au taux de droit commun, **diminué de l'IS correspondant** ;
   - **C** = capitaux propres : capital, primes, réserves, report à nouveau, provisions réglementées… **sans le résultat de l'exercice** pour lequel on calcule la participation (c'est précisément ce bénéfice que l'on partage) ;
   - **S** = salaires bruts au sens de l'assiette des cotisations de sécurité sociale ;
   - **VA** = charges de personnel + impôts et taxes (hors taxes sur le CA) + charges financières + dotations aux amortissements et provisions + **résultat courant avant impôts**, ce dernier pris **avant** participation.
3. **Erreur de Sabine** : elle a pris les capitaux propres « avant répartition » **y compris le résultat 2025** (500 000 €). C augmente, 5 % C augmente, la RSP diminue : les salariés ont été lésés.
4. **Conséquence** : la RSP est un **droit des salariés** ; un complément est dû. L'erreur est découverte après approbation des comptes 2025 : elle se corrige **dans les comptes 2026** (pas de retraitement du bilan d'ouverture en règles françaises), par nature (691), et non en résultat exceptionnel.

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 B — bénéfice net
- Résultat fiscal 2025 : 820 000 €.
- IS : 42 500 × 15 % = 6 375 ; (820 000 − 42 500) × 25 % = 194 375 ; total **200 750 €**.
- **B = 820 000 − 200 750 = 619 250 €**.

### 2.2 C — capitaux propres

| Élément | Retenu |
|---|---|
| Capital | 400 000 |
| Réserves | 1 100 000 |
| Report à nouveau | 85 000 |
| Provisions réglementées | 120 000 |
| Résultat de l'exercice 2025 | **exclu** |
| **C** | **1 705 000** |

5 % × C = **85 250 €**.

### 2.3 S et VA
- **S = 2 540 000 €** (rémunérations DSN ; personne au-dessus de 4 PASS).
- **VA** = 2 540 000 + 980 000 (charges de personnel, hors participation) + 145 000 (impôts et taxes hors TVA) + 62 000 (charges financières) + 410 000 (dotations) + 790 000 (RCAI avant participation) = **4 927 000 €**.
- S / VA = 0,515527.

### 2.4 RSP et forfait social
- B − 5 % C = 619 250 − 85 250 = 534 000 €.
- RSP = ½ × 534 000 × 2 540 000 / 4 927 000 = **137 645,63 €**.
- Forfait social 20 % = **27 529,13 €**.

### 2.5 Écart avec le calcul de Sabine

| | Sabine | Correct | Complément |
|---|---|---|---|
| C | 2 205 000 | 1 705 000 | |
| 5 % C | 110 250 | 85 250 | |
| RSP | 131 201,54 | 137 645,63 | **6 444,09** |
| Forfait social | 26 240,31 | 27 529,13 | **1 288,82** |
| Quote-part de Paul Roche (RSP × 34 800 / 2 540 000) | 1 797,56 | 1 885,85 | **88,29** |

Le plafond individuel (75 % du PASS de l'année — *à vérifier*) n'est pas atteint pour Paul Roche.

## 3. Écritures comptables

### 3.1 Pour mémoire : écritures correctes au 31/12/2025

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2025 | OD | 691 | Participation des salariés aux résultats | RSP 2025 | 137 645,63 | |
| 31/12/2025 | OD | 4246 | Réserve spéciale de participation (*intitulé selon la nomenclature du PCG*) | RSP 2025 | | 137 645,63 |
| 31/12/2025 | OD | 645 | Charges de sécurité sociale – forfait social (*subdivision selon la nomenclature 2025 du PCG*) | Forfait social 20 % sur RSP 2025 | 27 529,13 | |
| 31/12/2025 | OD | 4386 | Organismes sociaux – autres charges à payer | Forfait social sur RSP 2025 | | 27 529,13 |
| | | | | **Totaux** | **165 174,76** | **165 174,76** |

**Traitement fiscal** :
- 2025 : la RSP est **réintégrée** (elle n'est déductible que de l'exercice au cours duquel les sommes sont portées à la réserve spéciale, soit 2026) — c'est d'ailleurs pourquoi le résultat fiscal 2025 est « après réintégration de la RSP 2025 ».
- 2026 : **déduction** extra-comptable de la RSP 2025 (affectée en mai 2026).
- Forfait social : charge à payer certaine dans son principe et son montant au 31/12/2025, en principe déductible en 2025 ; certaines pratiques le rattachent à l'exercice de versement de la participation — *point à vérifier au BOFiP et à traiter avec constance*.

### 3.2 Corrections dans les comptes 2026

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 691 | Participation des salariés aux résultats | Complément RSP 2025 (correction calcul C) | 6 444,09 | |
| 31/10/2026 | OD | 4246 | Réserve spéciale de participation | Complément RSP 2025 | | 6 444,09 |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale – forfait social (*subdivision selon la nomenclature 2025*) | Forfait social sur complément RSP | 1 288,82 | |
| 31/10/2026 | OD | 4386 | Organismes sociaux – autres charges à payer | Forfait social sur complément RSP | | 1 288,82 |
| | | | | **Totaux** | **7 732,91** | **7 732,91** |

Puis, lors de l'affectation aux salariés (PEE / PERECO ou versement immédiat) : débit 4246 (6 444,09), crédit 512 et crédit 431 pour la CSG/CRDS précomptée (6 444,09 × 9,70 % = 625,08 €) ; paiement du forfait social via la DSN (débit 4386 / crédit 431 puis 512). Les **intérêts de retard** dus sur le complément (versé après le dernier jour du 5e mois suivant la clôture) sont une charge financière (661) et s'ajoutent aux droits des salariés — à calculer par le teneur de registre selon le taux légal applicable.

**Traitement fiscal du complément** : il est déductible de l'exercice au cours duquel il est porté à la réserve spéciale ; s'il est affecté avant le 31/12/2026, déduction en 2026 (aucune réintégration) ; sinon réintégration en 2026 et déduction en 2027. Les intérêts de retard sont déductibles dans les conditions de droit commun.

**Présentation** : correction d'erreur comptabilisée en résultat de l'exercice 2026, **par nature** (691 / 645) ; depuis le règlement ANC n° 2022-06, elle n'a pas vocation à être classée en exceptionnel. Si elle était significative, une information en annexe serait donnée.

## 4. Points d'attention / pièges

- **C sans le résultat de l'exercice** : c'est l'erreur la plus fréquente ; elle minore la RSP.
- **B est fiscal** : partir du résultat comptable est faux (réintégrations, déductions).
- **VA avant participation** : ne pas retrancher la participation du RCAI.
- **IS « correspondant »** : calculé sur le bénéfice retenu, au taux de droit commun (taux réduit PME inclus le cas échéant), sans imputer les crédits d'impôt.
- **Attestation** : le montant du bénéfice net et des capitaux propres est établi par une attestation de l'inspecteur des impôts ou du **commissaire aux comptes** ; ces montants ne peuvent ensuite être remis en cause dans un litige — d'où l'intérêt que le CAC détecte l'erreur maintenant.
- **Forfait social** : nul pour les entreprises de moins de 50 salariés (participation volontaire), 20 % au-delà, taux réduits selon le support (certains plans d'épargne retraite) — *à vérifier*.
- **Plafonds** : salaire retenu plafonné à 4 PASS, plafond individuel annuel, éventuel plafond global de l'accord.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- Faire établir un **tableau de répartition rectificatif** par salarié (complément, CSG/CRDS, intérêts), y compris pour les **salariés partis** (droits à leur verser ou à conserver selon les règles de l'accord).
- Informer le **CSE** de l'erreur et de sa régularisation ; remettre à chaque salarié une fiche distincte du bulletin de paie pour le complément.
- Mettre à jour le **modèle de calcul** du cabinet (contrôle automatique « C hors résultat de l'exercice »).
- Documenter dans le dossier de révision 2026 et dans les échanges avec le CAC (PBC list).
- **Note à Sabine Morel (copie CAC)** :

> Bonjour Sabine,
> Le calcul de la participation 2025 retenait les capitaux propres y compris le résultat 2025 (2 205 000 €) ; la formule légale les retient hors résultat de l'exercice (1 705 000 €). La réserve spéciale correcte est de 137 645,63 €, soit un complément de 6 444,09 € pour les salariés et de 1 288,82 € de forfait social.
> Proposition : (1) comptabiliser le complément dans les comptes 2026 ; (2) faire établir par le teneur de registre la répartition individuelle (par exemple + 88,29 € pour Paul Roche), avec les intérêts de retard ; (3) informer le CSE et les salariés, qui pourront à nouveau choisir entre PEE, PERECO et versement ; (4) verser avant le 31/12/2026 pour que le complément soit déductible dès 2026.
> Bien cordialement,

## 6. Références

- Code du travail : articles L. 3322-1 et suivants (obligation, seuil de 50 salariés), L. 3324-1 (formule de la RSP), D. 3324-1 et suivants (définition de B, C, S, VA ; attestation), L. 3324-5 et D. 3324-10 et suivants (répartition et plafonds), D. 3324-21-2 et D. 3324-25 (délais de versement et intérêts de retard) — *numéros à vérifier selon la codification en vigueur*.
- CGI, article 237 bis A (déductibilité de la RSP).
- Code de la sécurité sociale, article L. 137-15 et suivants (forfait social).
- PCG : comptes 691, 4246, 645, 4386, 661.
