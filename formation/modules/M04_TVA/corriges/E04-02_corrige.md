# Corrigé E04-02 — La CA12 de la boulangerie et ses acomptes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-02](../exercices/E04-02_ca12-boulangerie.md)

## 1. Analyse

**a) Le régime réel simplifié (RSI)** : une seule déclaration annuelle (CA12, formulaire 3517-S) déposée au plus tard le 2e jour ouvré suivant le 1er mai pour un exercice clos au 31/12, et deux **acomptes** :
- **juillet** : 55 % de la TVA due au titre de l'année précédente ;
- **décembre** : 40 % de cette même base ;
- la base des acomptes est la TVA due N-1 **avant déduction de la TVA sur immobilisations** (pour ne pas faire dépendre les acomptes d'un investissement ponctuel).

**b) L'erreur.** Le compte 44562 n'a pas été soldé : la TVA de la vitrine réfrigérée (facture d'octobre 2025, payée, au nom de la société, bien utilisé pour l'activité taxable) a été **oubliée** sur la CA12. La TVA déductible sur immobilisations est donc sous-déclarée de 3 600 €, et la TVA due surévaluée d'autant.

**c) Pourquoi c'est grave.** Le RSI n'est applicable que si la **TVA exigible de l'année précédente n'excède pas 15 000 €** (art. 302 septies A CGI, *seuil à vérifier*). La CA12 erronée affiche **16 980 €** de TVA due : au vu de la déclaration, la boulangerie paraît sortir du régime simplifié et basculer au **réel normal** (CA3 mensuelles) — avec plus de charge administrative et de coût d'honoraires. La TVA réellement due est de **13 380 €**, sous le seuil : le régime simplifié reste applicable. Il faut donc **rectifier officiellement** la situation, pas seulement « récupérer » les 3 600 € discrètement sur la prochaine CA12.

**d) Comment récupérer.** Deux voies :
- **réclamation contentieuse** auprès du SIE (art. L. 190 LPF) pour obtenir le **remboursement** de 3 600 € et la rectification de la CA12 2025 (et donc du montant de TVA due de référence) — délai : jusqu'au 31/12 de la 2e année suivant le paiement, soit le **31/12/2028** ;
- ou **déduction de la TVA omise** sur une déclaration ultérieure (CA12 2026, déposée en mai 2027), possible jusqu'au **31/12 de la 2e année suivant celle de l'omission**, soit le **31/12/2027** (art. 208 et 224 ann. II CGI).

Ici, la **réclamation** est préférable : elle corrige la TVA due 2025 (13 380 €) et sécurise le maintien au régime simplifié. En pratique, accompagner la réclamation d'un courrier explicatif et de la facture de la vitrine.

**e) Les acomptes 2026.** La base (TVA due 2025 avant déduction de la TVA sur immobilisations) vaut **16 980 €** **que l'erreur soit corrigée ou non** (13 380 + 3 600 = 16 980). L'acompte de juillet (9 339 €) est donc correct.

**f) Modulation de l'acompte de décembre.** L'entreprise peut réduire (voire supprimer) un acompte si elle estime que les acomptes déjà versés atteignent la TVA due de l'année en cours, en le signalant au SIE (mention sur le relevé d'acompte). Si la TVA finalement due excède de **plus de 20 %** le montant estimé, l'intérêt de retard et la majoration de 5 % s'appliquent sur la différence. Avec une estimation prudente de 14 500 €, l'acompte de décembre peut être ramené à 14 500 – 9 339 = **5 161 €** au lieu de 6 792 €. Opportun, car la trésorerie de la boulangerie est tendue en fin d'année — mais à condition que l'estimation soit documentée (simulation sur 9 mois + extrapolation). Marge de sécurité : 14 500 × 1,20 = 17 400 € ; un dépassement de la TVA réelle au-delà déclencherait des pénalités.

## 2. Calculs

**CA12 2025 correcte**

| Rubrique | Base HT | TVA |
|---|---|---|
| Opérations imposables à 5,5 % | 560 000 | 30 800,00 |
| Opérations imposables à 10 % | 110 000 | 11 000,00 |
| Opérations imposables à 20 % | 20 000 | 4 000,00 |
| **Total TVA brute** | **690 000** | **45 800,00** |
| TVA déductible — biens constituant des immobilisations | | 3 600,00 |
| TVA déductible — autres biens et services (9 900 + 17 000 + 1 920) | | 28 820,00 |
| **Total TVA déductible** | | **32 420,00** |
| **TVA due** | | **13 380,00** |
| Acomptes versés (7 040 + 5 120) | | 12 160,00 |
| **Solde à payer** | | **1 220,00** |
| Base des acomptes 2026 (13 380 + 3 600) | | 16 980,00 |

*Présentation par cadres du formulaire 3517-S ; numéros de lignes à reprendre sur le formulaire millésimé.*

**Erreur** : solde payé 4 820 € au lieu de 1 220 € → **3 600 € payés en trop**. TVA due affichée 16 980 € au lieu de 13 380 €.

**Contrôle des acomptes 2025** : base 2024 = 12 800 € → juillet 55 % = 7 040 € ; décembre 40 % = 5 120 € ✔.

**Acomptes 2026**

| | Calcul | Montant |
|---|---|---|
| Juillet 2026 | 16 980 × 55 % | 9 339,00 ✔ (payé) |
| Décembre 2026 (normal) | 16 980 × 40 % | 6 792,00 |
| Décembre 2026 (modulé) | 14 500 – 9 339 | 5 161,00 |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/05/2026 | BQ | 445715/0/20 | TVA collectée (5,5 / 10 / 20 %) | CA12 2025 – solde des comptes de TVA collectée | 45 800,00 | |
| 05/05/2026 | BQ | 44566 | TVA déductible sur ABS | CA12 2025 | | 28 820,00 |
| 05/05/2026 | BQ | 44581 | Acomptes – régime simplifié | CA12 2025 – imputation des acomptes | | 12 160,00 |
| 05/05/2026 | BQ | 512 | Banque | CA12 2025 – solde payé (tel que déclaré) | | 4 820,00 |
| 15/07/2026 | BQ | 44581 | Acomptes – régime simplifié | Acompte TVA juillet 2026 | 9 339,00 | |
| 15/07/2026 | BQ | 512 | Banque | Acompte TVA juillet 2026 | | 9 339,00 |
| 09/10/2026 | OD | 4458 | TVA à régulariser – déduction omise (réclamation en cours) | Vitrine FRIGOLYON 2025-882 – TVA non déduite sur CA12 2025 | 3 600,00 | |
| 09/10/2026 | OD | 44562 | TVA déductible sur immobilisations | Reclassement TVA vitrine | | 3 600,00 |
| 12/2026 | BQ | 44581 | Acomptes – régime simplifié | Acompte TVA décembre 2026 (non modulé) | 6 792,00 | |
| 12/2026 | BQ | 512 | Banque | Acompte TVA décembre 2026 | | 6 792,00 |
| | | | | **Totaux** | **65 531,00** | **65 531,00** |

(Si l'acompte de décembre est modulé, remplacer 6 792,00 par 5 161,00.)

À l'encaissement du remboursement : 512 / 4458 pour 3 600 €. Si l'on choisissait plutôt l'imputation sur la CA12 2026, le 4458 serait soldé lors de la liquidation de la CA12 2026 (TVA déductible supplémentaire).

## 4. Points d'attention / pièges

- **Un compte de TVA déductible non soldé** après une déclaration est toujours le signe d'un oubli : à chaque CA12/CA3, tous les comptes 4456x doivent revenir à zéro (sauf crédit reporté en 44567, acomptes en 44581, TVA en attente justifiée).
- **Base des acomptes** = TVA due N-1 **avant** déduction de la TVA sur immobilisations : ne pas recalculer les acomptes sur la TVA nette après investissement.
- **Seuil de 15 000 €** : il porte sur la TVA exigible de l'année ; un investissement important une année (forte TVA déductible) ou une erreur peut faire basculer artificiellement le régime. Surveillez ce seuil chaque année pour la boulangerie (13 380 € en 2025 : marge faible).
- **Modulation** : elle se fait sous la responsabilité de l'entreprise ; documenter l'estimation.
- **Paiement** : acomptes et solde sont télépayés ; la CA12 est télédéclarée (EDI par le cabinet).

## 5. Ce qu'un senior ferait en plus

**Mail à Marc Dupain :**
> Bonjour Monsieur Dupain, en reprenant votre dossier, nous avons constaté que la TVA de votre vitrine réfrigérée (3 600 €) n'a pas été déduite sur la déclaration annuelle 2025. Vous avez donc payé 3 600 € de trop en mai. Nous déposons une réclamation pour vous les faire rembourser et pour que votre TVA 2025 soit ramenée à 13 380 € : c'est important car au-delà de 15 000 €, vous passeriez à des déclarations mensuelles. Pour l'acompte de décembre, nous vous proposons de le réduire à 5 161 € au lieu de 6 792 €, compte tenu de votre activité 2026. Nous nous occupons de tout.

**Contrôles mis en place** : check-list de la CA12 (soldes des 4456x, rapprochement CA par taux / CA comptable / Z de caisse, fichier des immobilisations de l'année) ; tableau de suivi pluriannuel de la TVA due vs seuil de 15 000 €.

**Information d'Hélène** : l'erreur provient du cabinet (ancien collaborateur). Le cabinet doit en informer le client (devoir de transparence) et vérifier l'absence d'autre préjudice (pénalités, frais).

## 6. Références

- CGI : art. 287-3 (régime simplifié, déclaration annuelle et acomptes), art. 302 septies A (seuils du régime simplifié), art. 271 (droit à déduction).
- Annexe II au CGI : art. 208 et 224 (exercice du droit à déduction et réparation des omissions) ; dispositions relatives aux acomptes et à leur modulation (à vérifier au BOFiP TVA-DECLA).
- LPF : art. L. 190 (réclamations), art. R. 196-1 (délai de réclamation).
- CGI : art. 1727 et 1731 (intérêt de retard, majoration de 5 % en cas de modulation excessive).
- BOFiP : TVA-DECLA (régime simplifié d'imposition).
