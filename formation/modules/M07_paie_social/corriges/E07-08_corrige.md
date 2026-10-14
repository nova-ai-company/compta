# Corrigé E07-08 — Gérante majoritaire de SELARL : rémunération TNS et dividendes au-delà de 10 %

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-08](../exercices/E07-08_remuneration-gerante-pharmacie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **Statuts** :
   - **Anne Petit** détient 80 % des parts (son conjoint et ses enfants mineurs n'en détiennent pas) et est gérante → **gérante majoritaire** → **travailleuse non salariée** (TNS), affiliée à la sécurité sociale des indépendants (recouvrement URSSAF ; retraite auprès de la caisse des pharmaciens). Fiscalement, sa rémunération relève de l'**article 62 du CGI**.
   - **Luc Vidal** est associé minoritaire **non gérant** et pharmacien adjoint **salarié** : bulletin de paie, régime général. Ses dividendes suivent le régime normal des revenus de capitaux mobiliers.
2. **Comptes** : en société à l'IS, la rémunération du gérant majoritaire est une **charge déductible** ; l'usage est de l'isoler au **644** (rémunération du travail de l'exploitant) et ses cotisations au **646**, pour ne pas la mélanger avec la paie (641/645) — elle n'apparaît pas en DSN.
3. **Clôture décalée** : les cotisations TNS sont calculées par **année civile**. Au 30/09/2026, la régularisation à venir sur 2026 doit être rattachée à l'exercice **pour la fraction de l'année civile comprise dans l'exercice** (janvier → septembre).
4. **Dividendes et règle des 10 %** : pour les gérants majoritaires de SARL/SELARL, la fraction des dividendes qui excède **10 % du capital social détenu, des primes d'émission et des sommes versées en compte courant** est soumise aux **cotisations sociales TNS** et **pas** aux prélèvements sociaux sur revenus du capital (article L. 131-6 du CSS). L'assistante a retenu les prélèvements sociaux sur la totalité : double imposition sociale.

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 Charge à payer SSI au 30/09/2026
- Régularisation estimée 2026 (rémunération) : 41 000 − 34 800 = 6 200 € pour l'année civile.
- Fraction rattachable à l'exercice (janvier → septembre 2026) : 6 200 × 9/12 = **4 650,00 €**.
- La régularisation 2025 ayant été exactement provisionnée au 30/09/2025, aucun autre ajustement.

### 2.2 Fraction des dividendes d'Anne soumise aux cotisations

| Élément | Calcul | Montant |
|---|---|---|
| Dividende revenant à Anne | 150 000 × 80 % | 120 000,00 € |
| Capital détenu | 12 000 parts × 10 € | 120 000,00 € |
| Primes d'émission | néant | 0,00 € |
| Compte courant (montant moyen) | | 50 000,00 € |
| Base | | 170 000,00 € |
| Seuil de 10 % | 170 000 × 10 % | **17 000,00 €** |
| **Fraction soumise aux cotisations TNS** | 120 000 − 17 000 | **103 000,00 €** |

### 2.3 Retenues à la source correctes

| Bénéficiaire / fraction | Base | PFNL 12,8 % | PS 18,6 % | Total retenu | Net versé |
|---|---|---|---|---|---|
| Luc Vidal | 30 000,00 | 3 840,00 | 5 580,00 | 9 420,00 | 20 580,00 |
| Anne — fraction ≤ 10 % | 17 000,00 | 2 176,00 | 3 162,00 | 5 338,00 | |
| Anne — fraction > 10 % | 103 000,00 | 13 184,00 | **0,00** | 13 184,00 | |
| Anne — total | 120 000,00 | 15 360,00 | 3 162,00 | 18 522,00 | **101 478,00** |
| **Total** | **150 000,00** | **19 200,00** | **8 742,00** | **27 942,00** | **122 058,00** |

Erreur : prélèvements sociaux retenus 27 900,00 au lieu de 8 742,00 → **trop-retenu de 19 158,00 €** (= 103 000 × 18,6 %), au détriment d'Anne (versé 82 320,00 au lieu de 101 478,00). Le PFNL (12,8 %) reste dû sur toute la distribution (sauf dispense demandée dans les délais, ici sans objet).

### 2.4 Cotisations TNS sur les dividendes
103 000 × 28 % ≈ **28 840 €** (estimation), appelés par l'URSSAF au titre des revenus 2026 (provisionnelles puis régularisation en 2027). La décision d'AG ne met à la charge de la société que les cotisations **afférentes à la rémunération** : ces cotisations sont **personnelles** à Anne. Si la pharmacie les paie (appel unique de l'URSSAF), la part « dividendes » est **débitée au compte courant d'Anne (455)** — sinon, ce serait un complément de rémunération non autorisé par l'AG, à requalifier.

### 2.5 Simulation 10 000 € (ordre de grandeur, hypothèses de la pièce 5)

| | Rémunération | Dividende (fraction > 10 %) |
|---|---|---|
| Bénéfice disponible | 10 000,00 | 10 000,00 |
| IS 25 % | 0 (rémunération + cotisations déductibles) | − 2 500,00 |
| Cotisations TNS | R + 40 % R = 10 000 → R = 7 142,86 ; cotisations 2 857,14 | 7 500 × 28 % = − 2 100,00 |
| Revenu brut perçu | 7 142,86 | 7 500,00 |
| IR | 7 142,86 × 90 % × 41 % = − 2 635,71 | PFU 12,8 % : − 960,00 (pas de prélèvements sociaux sur cette fraction) |
| **Reste à Anne** | **≈ 4 507 €** | **≈ 4 440 €** |

Conclusion : au-delà du seuil de 10 %, **le dividende n'est pas moins taxé** ; il est même légèrement moins favorable dans ces hypothèses et n'améliore pas la protection sociale autant qu'une rémunération (les cotisations sur dividendes ouvrent des droits mais l'assiette est plus irrégulière). Le seul « dividende avantageux » est la fraction ≤ 10 % (17 000 €), déjà utilisée.

## 3. Écritures comptables

**Charge à payer SSI au 30/09/2026**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 646 | Cotisations sociales personnelles de l'exploitant | Régul. SSI 2026 estimée (9/12 × 6 200) | 4 650,00 | |
| 30/09/2026 | OD | 4386 | Organismes sociaux – autres charges à payer | Régul. SSI 2026 gérante | | 4 650,00 |
| | | | | **Totaux** | **4 650,00** | **4 650,00** |

**Correction de la retenue sur dividendes** (constatation de la créance sur l'État et de la dette envers Anne)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 442 | État – impôts et taxes recouvrables sur des tiers (prélèvements sur dividendes — *subdivision selon la nomenclature 2025 du PCG*) | PS trop versés 2777 du 14/04/2026 | 19 158,00 | |
| 30/09/2026 | OD | 457 | Associés – dividendes à payer | Complément dividende net A. Petit | | 19 158,00 |
| | | | | **Totaux** | **19 158,00** | **19 158,00** |

**Versement du complément à Anne** (dès validation)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/10/2026 | BQ | 457 | Associés – dividendes à payer | Complément dividende A. Petit | 19 158,00 | |
| 15/10/2026 | BQ | 512 | Banque | Complément dividende A. Petit | | 19 158,00 |
| | | | | **Totaux** | **19 158,00** | **19 158,00** |

> Le compte 442 (subdivision prélèvements sur dividendes) présente ainsi un solde débiteur de 19 158,00 € au 30/09/2026 : créance sur l'État, à apurer par imputation sur une prochaine déclaration 2777 ou par réclamation auprès du SIE (*procédure à vérifier*). Si la pharmacie préfère attendre le remboursement avant de payer Anne, le 457 reste créditeur à la clôture.

## 4. Points d'attention / pièges

- **Seuil de 10 %** : il s'apprécie sur le capital **détenu** par le gérant (et son conjoint / partenaire de PACS / enfants mineurs), pas sur le capital total ; on y ajoute les primes d'émission et le **montant moyen** du compte courant. Un compte courant important augmente la fraction « légère ».
- **Ne pas retenir les prélèvements sociaux** sur la fraction soumise aux cotisations ; l'**IFU** doit isoler cette fraction.
- La règle ne concerne **pas** Luc Vidal (non gérant) ni les dirigeants de SAS.
- **Gérance majoritaire** : en cas de cogérance, on additionne les parts de tous les gérants ; un gérant égalitaire (50 %) n'est pas majoritaire.
- **Clôture décalée** : la charge à payer TNS se calcule au prorata de l'année civile ; un junior oublie souvent le décalage et provisionne l'année entière, ou rien.
- Les cotisations sur dividendes ne sont pas déductibles du résultat de la société si elles sont personnelles ; si l'AG décidait de les prendre en charge, elles deviendraient un élément de rémunération (644/646) imposable chez Anne.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- Vérifier l'**IFU 2026** qui sera déposé en février 2027 (fraction > 10 % déclarée à part).
- Vérifier que la **décision d'AG** sur la rémunération est bien au registre (sinon, rémunération contestable).
- Proposer pour l'exercice suivant une **simulation complète** (retraite, prévoyance, IS à 15 % sur la première tranche, CSG déductible, option barème vs PFU) avant toute modification de la politique de rémunération.
- **Mail à Anne Petit** :

> Bonjour Docteur,
> Vos dividendes de mars ont été mal traités : 19 158 € de prélèvements sociaux ont été retenus à tort sur la part qui supporte déjà des cotisations sociales (au-delà de 17 000 €, soit 10 % de votre capital et de votre compte courant). Nous vous reversons ce montant et régularisons auprès de l'administration.
> Sur votre projet : au-delà de ce seuil de 17 000 €, un dividende supporte à la fois l'impôt sur les sociétés et des cotisations sociales d'environ 28 %. Pour 10 000 € de bénéfice, il vous resterait environ 4 440 € en dividende contre 4 500 € en rémunération, qui en outre améliore votre retraite et votre prévoyance. Nous ne recommandons donc pas de basculer de la rémunération vers les dividendes ; nous vous proposerons une simulation complète lors de la présentation des comptes.
> Bien cordialement,

## 6. Références

- Code de la sécurité sociale : article L. 131-6 (assiette des cotisations des travailleurs indépendants, intégration des dividendes excédant 10 % du capital, des primes d'émission et des comptes courants).
- CGI : article 62 (rémunération des gérants majoritaires), article 117 quater (prélèvement forfaitaire non libératoire de 12,8 %), article 200 A (PFU), article 242 ter (IFU).
- Code de la sécurité sociale, article L. 136-7 et Code général des impôts, article 1600-0 S (prélèvements sociaux sur revenus de placement) — *taux à vérifier*.
- PCG : comptes 644, 646, 4386, 442, 455, 457.
