# Corrigé E12-09 — Le client conteste la provision et refuse de signer ; une erreur découverte après le dépôt de la liasse

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E12-09](../exercices/E12-09_refus-affirmation-liasse-rectificative.md)

## 1. Analyse (raisonnement pas à pas)

### Partie A — la contestation de Thierry Martin
Le senior sépare **l'émotion** (« je veux un beau bilan pour la banque ») des **faits**. Une estimation comptable se modifie quand on apporte une **preuve**, jamais parce que le résultat déplaît. Pour chaque poste :

| Poste | Argument de Thierry | Preuve disponible | Décision |
|---|---|---|---|
| **C3** (dépréciation 1 700 €) | « Je l'ai vendue » | Facture du 20/10/2026 : **6 200 € TTC**, vendue en l'état, TVA sur marge nulle | **Ajustement** : la vente postérieure à la clôture **éclaire la valeur à la clôture** (événement postérieur donnant une information sur une situation existant au 30/09). VNR = 6 200 € (pas de remise en état). Dépréciation = 6 400 – 6 200 = **200 €** au lieu de 1 700 € → – 1 500 € |
| **Golf** (1 800 €) | « Je la vendrai au prix affiché » | Aucune offre ; sa propre estimation écrite du 30/09 (9 500 € – 400 €) ; 8,5 mois de stock | **Maintien** : une intention n'est pas une preuve ; l'estimation vient de lui |
| **Vidal** (2 800 €) | « Vidal va s'en sortir » | Redressement judiciaire ouvert, mandataire : dividende ≈ 30 % | **Maintien** : la dépréciation reflète l'information du mandataire ; à revoir si le plan de redressement est adopté avec un meilleur taux |
| **Garanties** (3 540 €) | « Je n'ai jamais de retour » | Statistique sur 3 ans : 1,5 % des ventes VO | **Maintien** : obligation contractuelle de garantie de 6 mois, coûts historiquement constatés (ils sont dans ses charges d'atelier !) |

### Partie B — l'erreur 2025 de Transports Leroy
L'accord de l'assureur du **18/12/2025** rendait la créance **certaine dans son principe et son montant** à la clôture du 31/12/2025 : il fallait constater un **produit à recevoir** de 48 000 € en 2025. C'est une **erreur** (omission) de l'exercice 2025, significative (48 000 € ≈ 34 % du résultat 2025).
- **Comptablement** : les comptes 2025, approuvés, ne sont pas modifiés. Selon le PCG, la correction d'une erreur est comptabilisée **dans le résultat de l'exercice au cours duquel elle est constatée** (2026), avec une **information en annexe**. Ici, le produit est déjà dans le résultat 2026 (775) : aucune écriture de reclassement n'est nécessaire.
- **Fiscalement** : le principe des **créances acquises** (art. 38-2 bis CGI) rattache le produit à **2025**. Il faut donc **rectifier la déclaration 2025** (+ 48 000 €) et **déduire** extra-comptablement ces 48 000 € du résultat fiscal 2026 pour éviter une double imposition.

## 2. Calculs

### Partie A — nouveau résultat du Garage Martin

| | Avant | Ajustement | Après |
|---|---:|---:|---:|
| Résultat avant IS | 86 852 | + 1 500 | 88 352 |
| Réintégration amende | 450 | | 450 |
| Résultat fiscal | 87 302 | + 1 500 | 88 802 |
| IS : 42 500 × 15 % + (88 802 – 42 500) × 25 % = 6 375 + 11 575,50 | 17 576 | + 375 | **17 951** (arrondi) |
| **Résultat net** | 69 276 | + 1 125 | **70 401** |
| Solde d'IS à payer (– 15 000 d'acomptes) | 2 576 | | **2 951** |

Montants toujours contestés : Golf 1 800 + Vidal 2 800 + garanties 3 540 (suppression totale de la provision) = **8 140 €** > seuil de signification (8 000 €) → leur suppression rendrait les comptes **significativement** incorrects : le cabinet ne peut pas l'accepter.

### Partie B — IS 2025 et intérêt de retard

| | Montant |
|---|---:|
| Produit omis (rattachable à 2025) | 48 000,00 |
| IS supplémentaire 2025 (taux marginal 25 %, le bénéfice dépassant 42 500 €) | 12 000,00 |
| Intérêt de retard : du 01/06/2026 au 30/11/2026 = 6 mois × 0,20 % × 12 000 | 144,00 |
| **Total à verser** (avant éventuelle réduction de l'intérêt en cas de régularisation spontanée — *dispositif et taux à vérifier*) | **12 144,00** |

## 3. Écritures comptables

### Partie A — Garage Martin (OD d'inventaire complémentaires au 30/09/2026)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 3972 | Dépréciation du stock de VO | C3 vendue 6 200 € le 20/10 – ajustement | 1 500,00 | |
| 30/09/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | C3 vendue 6 200 € le 20/10 – ajustement | | 1 500,00 |
| 30/09/2026 | OD | 695 | Impôts sur les bénéfices | Complément d'IS | 375,00 | |
| 30/09/2026 | OD | 444 | État – impôt sur les bénéfices | Complément d'IS | | 375,00 |
| | | | | **Totaux** | **1 875,00** | **1 875,00** |

(En pratique, on corrige directement l'écriture n° 6 de dépréciation : 4 400 € au lieu de 5 900 €.)

### Partie B — Transports Leroy (exercice 2026)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | OD | 695 | Impôts sur les bénéfices | IS 2025 supplémentaire – déclaration rectificative | 12 000,00 | |
| 30/11/2026 | OD | 658 | Pénalités et amendes (*subdivision selon la nomenclature 2025 du PCG*) | Intérêt de retard IS 2025 | 144,00 | |
| 30/11/2026 | OD | 444 | État – impôt sur les bénéfices | IS 2025 rectificatif et intérêt de retard | | 12 144,00 |
| 30/11/2026 | BQ | 444 | État – impôt sur les bénéfices | Paiement 2572 rectificatif | 12 144,00 | |
| 30/11/2026 | BQ | 512 | Banque | Paiement 2572 rectificatif | | 12 144,00 |
| | | | | **Totaux** | **24 288,00** | **24 288,00** |

**Traitement extra-comptable** :
- Liasse 2025 rectificative : résultat fiscal 2025 + 48 000 € (réintégration sur le 2058-A rectificatif ou rectification des postes concernés).
- Liasse 2026 : **déduction** de 48 000 € (produit déjà imposé en 2025) ; l'IS (695) est réintégré comme chaque année ; l'intérêt de retard afférent à l'IS suit le régime de l'impôt auquel il se rapporte → **non déductible** (réintégration de 144 €).
- **Annexe 2026** : mention de la correction d'erreur (nature, montant, incidence sur le résultat 2026).

## 4. Points d'attention / pièges

- **Ne jamais « négocier » une provision** : on modifie une estimation sur **preuve** (la vente de la C3), pas sur pression. Le refus d'un client n'est pas une preuve.
- **Événements postérieurs** : la vente de la C3 en octobre est un événement qui **confirme une situation existant à la clôture** → ajustement des comptes. Un incendie du parc en octobre serait au contraire un événement **nouveau** → information en annexe sans ajustement.
- **Pas de lettre d'affirmation → pas d'attestation** en l'état. Mais la **liasse fiscale** reste due au **31/12/2026** : c'est une obligation de la société, distincte de l'attestation. Les comptes sont **arrêtés par le gérant**, sous sa responsabilité ; si le gérant arrête des comptes sans ces provisions, le cabinet n'y associe pas son nom (refus d'attestation ou attestation assortie d'une réserve selon la norme professionnelle) et peut être amené à **mettre fin à la mission** dans les conditions prévues par la lettre de mission et le code de déontologie.
- **Risque pénal** pour Thierry : présenter à l'associé unique des comptes ne donnant pas une image fidèle **en vue de dissimuler la véritable situation** de la société est un délit pour le gérant de SARL (art. L. 241-3 C. com.) ; remettre sciemment à une banque des comptes inexacts pour obtenir un crédit peut en outre caractériser une escroquerie.
- **Partie B** : ne pas « refaire » les comptes 2025 approuvés ; ne pas oublier la **déduction 2026** (sinon double imposition) ; distinguer **déclaration rectificative** (le contribuable augmente spontanément son impôt) et **réclamation contentieuse** (s'il demandait une diminution, art. L. 190 LPF, dans le délai de réclamation).
- Une déclaration rectificative **spontanée**, avant tout contrôle, limite les conséquences : intérêt de retard seul, pas de majoration pour manquement délibéré.

## 5. Ce qu'un senior ferait en plus

**Mail d'Hélène Ferrand à Thierry Martin (partie A) :**
> « Bonjour Thierry,
> Suite à notre échange, nous avons tenu compte de la vente de la C3 du 20/10 : la dépréciation passe de 1 700 € à 200 €, et votre résultat de 69 276 € à **70 401 €**.
> En revanche, nous maintenons la dépréciation de la Golf (fondée sur votre estimation écrite du 30/09 : 9 500 € moins 400 € de frais), celle de la créance Vidal (information du mandataire judiciaire) et la provision pour garanties (calculée sur vos propres coûts de garantie des trois dernières années). Ces éléments, d'un montant total de 8 140 €, sont significatifs : les supprimer rendrait les comptes inexacts.
> Votre banquier lira d'abord votre EBE (113 762 €), votre trésorerie (140 896 €) et vos capitaux propres (61 % du bilan) : des comptes prudents et attestés sont un atout dans votre demande de financement, pas un handicap.
> Si vous apportez des éléments nouveaux (offre écrite sur la Golf, plan de redressement de Vidal), nous les examinerons avant le 13/11. À défaut de lettre d'affirmation signée, nous ne pourrons pas délivrer notre attestation sur les comptes ; la liasse fiscale devra néanmoins être déposée avant le 31/12.
> Je vous propose d'en parler de vive voix jeudi à 17 h. Bien cordialement, Hélène Ferrand »

**Mail à Bruno Leroy (partie B) :**
> « Bonjour Bruno,
> En révisant la situation au 30/09, nous avons constaté que l'indemnité d'assurance de 48 000 € du tracteur FX-218-KL, accordée par l'assureur le 18/12/2025, aurait dû être rattachée à l'exercice 2025 (elle a été enregistrée en 2026). Fiscalement, cela augmente le bénéfice 2025 de 48 000 € et l'impôt 2025 de **12 000 €**, majoré d'un intérêt de retard d'environ **144 €** (calculé à fin novembre). En contrepartie, ces 48 000 € seront déduits du résultat fiscal 2026 : l'impôt 2026 sera réduit d'autant (sur la base du taux de 25 %, environ 12 000 €). L'effet est donc essentiellement un **décalage de trésorerie** et un coût de 144 €.
> Nous vous proposons de déposer une **déclaration rectificative** spontanée avant fin novembre, ce qui limite les pénalités. Les comptes 2025 approuvés ne sont pas modifiés ; une mention figurera dans l'annexe 2026. Pouvez-vous nous donner votre accord par retour ? Bien cordialement. »

- **Qualité interne** : consigner l'incident (cause : sinistre en cours non suivi au questionnaire de fin de mission ; procédure : ajouter la question « sinistres et indemnités d'assurance en cours » à la check-list des événements postérieurs). Informer l'assureur RC du cabinet si la procédure interne l'exige.

## 6. Références

- PCG : définition et évaluation des provisions et dépréciations ; événements postérieurs à la clôture ; correction d'erreurs comptabilisée dans le résultat de l'exercice de constatation, avec information en annexe.
- Code de commerce : art. L. 123-14 (image fidèle), art. L. 241-3 (sanctions pénales des gérants de SARL, présentation de comptes infidèles).
- CGI : art. 38-2 bis (rattachement des créances acquises), art. 1727 (intérêt de retard), art. 1729 (majorations, non applicables en cas de régularisation spontanée de bonne foi).
- LPF : art. L. 190 (réclamations) ; délai de reprise de l'administration (art. L. 169).
- Norme professionnelle de l'Ordre relative à la mission de présentation (déclarations de la direction, attestation, refus d'attestation) ; code de déontologie des professionnels de l'expertise comptable (indépendance, fin de mission).
