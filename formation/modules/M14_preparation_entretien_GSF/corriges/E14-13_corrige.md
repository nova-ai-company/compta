# Corrigé E14-13 — Balance âgée fournisseurs, fournisseurs débiteurs et délais de paiement (LME) : analyser avant le comité

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-13](../exercices/E14-13_balance-agee-fournisseurs-delais-paiement.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Une balance âgée fournisseurs se lit en deux temps : **d'abord les soldes anormaux** (débiteurs, très anciens), qui faussent tout le reste ; **ensuite l'échu**, en distinguant le retard **justifié** (litige documenté sur une facture non conforme) du retard **subi** (processus interne défaillant).

### Question 1 — Les soldes anormaux

| Tiers | Solde anormal | Nature réelle | Traitement |
|---|---|---|---|
| HPD − 3 000,00 | acompte sur commande non livrée | créance (avance) | Reclassement **4091** ; s'imputera sur la facture de novembre |
| Machines Nett' − 1 250,00 | avoir non imputé | réduction de dette | Pas de reclassement (le tiers reste créditeur net de 1 870,00 €) ; **imputer l'avoir au prochain paiement** et lettrer |
| AutoLease − 2 512,00 | double paiement | créance sur le fournisseur | Reclassement **4097** et **demande de remboursement** (ou imputation sur la facture suivante, par accord écrit) |
| CloudLedger 4 860,00 à > 90 j | facture **déjà payée** par carte | pas une dette | Imputer le paiement carte : D 401 / C 471 ; lettrer |

### Question 2 — L'échu réel
Après corrections, l'échu créditeur est de 6 300,00 (HPD) + 12 850,00 + 9 640,00 (Interim Azur) + 6 600,00 (SCI) = **35 390,00 €**.
- **HPD 6 300,00 €** : litige documenté sur factures non conformes → retard **justifié** (la dette n'est pas exigible en l'état), à condition que les litiges soient formalisés et suivis.
- **Interim Azur 22 490,00 €** : **aucune contestation** ; le retard vient de la non-validation des heures par les établissements → retard **non justifié**, imputable à GSF Riviera. Les 9 640,00 € ont environ 70 jours d'âge : ils dépassent non seulement le délai convenu (30 jours) mais aussi le **plafond légal de 60 jours**.
- **SCI 6 600,00 €** : le désaccord porte sur la régularisation de charges (1 140,00 €, facture distincte), **pas sur le loyer** : retenir le loyer est injustifié et expose à un commandement de payer (clause résolutoire du bail). On paie le loyer, on conteste la régularisation séparément.

### Question 3 — Risque « délais de paiement »
- **Pénalités et indemnités** : dues **de plein droit** au fournisseur dès le lendemain de l'échéance, sans rappel. Exemple Interim Azur (2 factures âgées de 70 jours en moyenne, échéance à 30 jours, soit **40 jours de retard**) : 9 640,00 × 12,15 % × 40/365 = **128,36 €** + 2 × 40 € = **80,00 €**.
- **Comptabilisation** : en pratique, les fournisseurs les réclament rarement ; on ne constate une charge à payer que si la réclamation est **probable** (fournisseur qui les facture habituellement, réclamation reçue). Les pénalités sont une charge (658 — *subdivision selon la nomenclature 2025 du PCG*), hors champ de TVA.
- **Amende administrative** (DGCCRF) : le non-respect des délais **convenus** ou **légaux** est sanctionné, quel que soit le motif interne, jusqu'à 2 M€ pour une personne morale, avec publication (*à vérifier*). Pour un groupe engagé sur un label « relations fournisseurs et achats responsables », le risque d'image est aussi important que l'amende.
- **Rapport de gestion / CAC** : les sociétés dont les comptes sont certifiés publient la décomposition des factures reçues et émises non réglées et échues par tranche de retard ; le commissaire aux comptes atteste (et signale les manquements significatifs) (*modalités à vérifier*).

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Total 401 avant corrections | balance âgée | 124 648,00 € |
| + reclassement acompte HPD (sortie du débit 401) | | + 3 000,00 € |
| + reclassement trop-payé AutoLease | | + 2 512,00 € |
| − imputation paiement carte CloudLedger | | − 4 860,00 € |
| **Total 401 après corrections** | | **125 300,00 €** |
| Créances à l'actif : 4091 / 4097 | | 3 000,00 € / 2 512,00 € |
| Échu créditeur réel | 6 300,00 + 12 850,00 + 9 640,00 + 6 600,00 | **35 390,00 €** |
| dont justifié (litiges HPD) | | 6 300,00 € |
| dont non justifié | 22 490,00 + 6 600,00 | **29 090,00 €** |
| Pénalités illustratives Interim Azur | 9 640,00 × 12,15 % × 40/365 | 128,36 € |
| Indemnités forfaitaires | 2 × 40,00 | 80,00 € |
| **DPO** | 125 300,00 / 1 520 000,00 × 365 | **30,1 jours** |

Le DPO moyen de 30 jours est **bon** (bien en deçà des délais convenus) : le problème n'est pas global, il est concentré sur deux fournisseurs et un processus (validation des heures d'intérim).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 4091 | Fournisseurs – avances et acomptes versés sur commandes | Reclass. acompte HPD 12/05/2026 commande EPI | 3 000,00 | |
| 30/09/2026 | OD | 401HPD | Fournisseur Hygiène Pro Distribution | Reclass. acompte HPD 12/05/2026 commande EPI | | 3 000,00 |
| 30/09/2026 | OD | 4097 | Fournisseurs – autres avoirs (créances) | Trop-payé AutoLease loyers 08/2026 (vir. 08/09 + prlv 10/09) | 2 512,00 | |
| 30/09/2026 | OD | 401ALF | Fournisseur AutoLease France | Trop-payé AutoLease loyers 08/2026 | | 2 512,00 |
| 30/09/2026 | OD | 401CLD | Fournisseur CloudLedger Inc. | Imputation paiement CB 01/2026 abonnement annuel | 4 860,00 | |
| 30/09/2026 | OD | 471 | Compte d'attente | Imputation paiement CB 01/2026 CloudLedger | | 4 860,00 |
| | | | | **Totaux** | **10 372,00** | **10 372,00** |

> Variante admise : laisser l'acompte en 401 en cours de mois et reclasser seulement à la clôture annuelle. Dans un groupe qui publie un BFR mensuel, on reclasse à chaque clôture (ou on saisit directement en 4091, ce qui est mieux).

## 4. Points d'attention / pièges

- **Un solde débiteur fournisseur n'est jamais « bon signe »** : c'est soit une avance (4091), soit une créance (trop-payé, avoir), soit une erreur. Il doit être justifié tiers par tiers.
- **Compenser des tiers différents** (net du 401 global) masque les problèmes : la présentation au bilan suppose un examen **par fournisseur**.
- **Le retard « parce que l'établissement n'a pas validé »** n'est pas opposable au fournisseur ni à l'administration : seul un litige réel sur la facture suspend légitimement le paiement de la partie contestée.
- **Ne pas retenir un loyer** pour une contestation de charges distincte.
- **Le paiement carte en 471 depuis janvier** révèle un compte d'attente non suivi : le 471 doit être justifié à chaque clôture mensuelle.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Page de synthèse pour le comité (question 5)** :
- Dettes fournisseurs au 30/09 après corrections : **125 300 €** ; DPO **30 jours**, conforme aux délais négociés.
- Soldes anormaux corrigés : acompte HPD (3 000 €) reclassé, trop-payé AutoLease (2 512 €) — **remboursement demandé**, paiement carte CloudLedger (4 860 €) imputé ; avoir Machines Nett' (1 250 €) à déduire du prochain paiement.
- Échu réel **35 390 €**, dont **6 300 € justifiés** (litiges HPD documentés) et **29 090 € non justifiés**.
- **Interim Azur 22 490 €** : retard dû à la non-validation des heures par les établissements ; 9 640 € dépassent le plafond légal de 60 jours → **paiement cette semaine** et mise en place d'une validation hebdomadaire avec délégation (adjoint) dans chaque établissement.
- **Loyer Cannes 6 600 €** : à payer immédiatement ; la contestation de la régularisation de charges (1 140 €) est traitée séparément avec le bailleur.
- Risque : pénalités et indemnités dues de plein droit (ordre de grandeur : quelques centaines d'euros), **risque d'amende administrative** et d'image en cas de contrôle ; aucune réclamation reçue à ce jour, pas de provision.
- Action process : interdire les paiements manuels sur un tiers sous mandat SEPA (blocage ERP) ; revue mensuelle du 471.

**Mail à AutoLease** : demande de remboursement du double paiement de 2 512,00 € (virement du 08/09 et prélèvement du 10/09, facture de loyers d'août), par virement sur l'IBAN de GSF Riviera, ou à défaut accord écrit pour imputation sur la facture d'octobre.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce art. L. 441-10 (délais de paiement, pénalités, indemnité forfaitaire de 40 €), D. 441-5 (indemnité), L. 441-16 (amende administrative), D. 441-6 (informations sur les délais de paiement dans le rapport de gestion) (*à vérifier*).
- PCG : comptes 4091, 4097, 471 ; présentation des soldes débiteurs des comptes fournisseurs en créances.
- Code civil (bail) et clause résolutoire : non-paiement du loyer.
