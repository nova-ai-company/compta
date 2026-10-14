# Corrigé E07-05 — Rupture conventionnelle : indemnité légale, régime social et solde de tout compte

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E07-05](../exercices/E07-05_rupture-conventionnelle-immoplus.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

1. **Plancher** : l'indemnité spécifique de rupture conventionnelle ne peut pas être inférieure à l'indemnité **légale** de licenciement (ou conventionnelle si plus favorable — écartée ici par l'énoncé). À défaut, la DREETS refuse l'homologation.
2. **Salaire de référence** : le plus favorable entre (a) la moyenne mensuelle des 12 derniers mois et (b) la moyenne des 3 derniers mois, dans laquelle **toute prime annuelle ou exceptionnelle n'est retenue qu'au prorata** (article R. 1234-4 du Code du travail). L'augmentation de juillet 2026 rend la méthode des 3 mois plus favorable.
3. **Ancienneté** : appréciée à la date de **fin du contrat** (30/11/2026), années incomplètes comprises au prorata.
4. **Régime social** : on part de la fraction exonérée d'IR, puis on plafonne à 2 PASS pour les cotisations ; la CSG/CRDS frappe la fraction **supra-légale** ; l'employeur paie une **contribution patronale spécifique** sur la part exonérée de cotisations — c'est le « forfait » dont parle M. Blanc (l'ancien forfait social a été remplacé par cette contribution en 2023).
5. **Comptabilité** : l'indemnité est une charge de personnel (6414), la contribution patronale une charge sociale (645), la CSG/CRDS une retenue sur le net.

## 2. Calculs (détaillés, chaque montant justifié)

### 2.1 Ancienneté
Du 01/03/2013 au 30/11/2026 : 13 ans (au 28/02/2026) + 9 mois = **13 ans 9 mois = 13,75 années**.

### 2.2 Salaire de référence

| Méthode | Calcul | Moyenne |
|---|---|---|
| 12 derniers mois (oct. 2025 → sept. 2026) | 9 × 2 450 + 3 × 2 600 + 13e mois 2 450 + 4 primes × 300 = 22 050 + 7 800 + 2 450 + 1 200 = 33 500,00 / 12 | 2 791,67 € |
| 3 derniers mois (juil. → sept. 2026) | 3 × 2 600 + 13e mois **au prorata** (2 600 × 3/12 = 650,00) + prime trimestrielle de septembre (qui couvre le trimestre : 300,00) = 8 750,00 / 3 | **2 916,67 €** |

> Piège : intégrer le 13e mois **en totalité** dans les 3 mois (il est versé en décembre et couvre l'année) ou l'oublier. Le prorata s'applique aux primes annuelles ; la prime trimestrielle versée en septembre couvre exactement la période de 3 mois, elle est retenue en totalité.

### 2.3 Indemnité légale minimale
- 1/4 de mois par année jusqu'à 10 ans : 10 × 1/4 = 2,5 mois ;
- 1/3 de mois par année au-delà : 3,75 × 1/3 = 1,25 mois ;
- total 3,75 mois × 2 916,67 = **10 937,50 €**.

**14 000 € ≥ 10 937,50 €** ✔ : l'indemnité est homologable. Supra-légal : 14 000,00 − 10 937,50 = **3 062,50 €**.

### 2.4 Régime fiscal et social

| Étape | Calcul | Résultat |
|---|---|---|
| Limite d'exonération IR | max(10 937,50 ; 2 × 33 050 = 66 100 ; 50 % × 14 000 = 7 000) = 66 100, plafonnée à 6 PASS (288 360) | 66 100 € → **14 000 € entièrement exonérés d'IR** |
| Part exonérée de cotisations | min(part exonérée d'IR 14 000 ; 2 PASS = 96 120) | **14 000 € exonérés de cotisations** |
| CSG/CRDS (salariée) | fraction supra-légale 3 062,50 × 9,70 % | **297,06 €** |
| Contribution patronale spécifique | 14 000 × 30 % (*taux à vérifier*) | **4 200,00 €** |

### 2.5 Calendrier
- Signature : 06/10/2026 → rétractation de 15 jours **calendaires** : du 07/10 au **21/10/2026** inclus.
- Envoi de la demande d'homologation (téléservice TéléRC) : au plus tôt le **22/10/2026**.
- Instruction : 15 jours **ouvrables** à compter du lendemain de la réception. Si la demande est reçue le 22/10 : 23, 24, 26, 27, 28, 29, 30, 31/10, 2, 3, 4, 5, 6, 7 et **9/11/2026** (le 1er novembre est un dimanche, férié) → homologation tacite acquise le **09/11/2026**.
- Rupture possible **au plus tôt le 10/11/2026** : le 30/11/2026 est compatible ✔ (marge de 3 semaines en cas de retard d'envoi ou de demande de pièces).

### 2.6 Solde de tout compte

| Élément | Montant |
|---|---|
| Brut soumis (salaire, 13e mois prorata, ICCP) | 6 503,33 |
| − cotisations salariales (926,03 + 403,44 + 40,00) | − 1 369,47 |
| + indemnité de rupture conventionnelle | + 14 000,00 |
| − CSG/CRDS sur indemnité | − 297,06 |
| **Net avant PAS** | **18 836,80** |
| − PAS : 5 360,32 × 5,2 % (l'indemnité, exonérée d'IR, n'entre pas dans l'assiette) | − 278,74 |
| **Net payé** | **18 558,06** |

### 2.7 Coût pour ImmoPlus

| Élément | Montant |
|---|---|
| Brut du solde | 6 503,33 |
| Charges patronales sur le solde (2 373,72 + 604,71 + 40,00) | 3 018,43 |
| Indemnité de rupture | 14 000,00 |
| Contribution patronale spécifique | 4 200,00 |
| **Coût total du dernier mois** | **27 721,76** |
| dont **coût propre de la rupture** (indemnité + contribution) | **18 200,00** |

Le salaire, le 13e mois et les congés auraient été dus de toute façon (le 13e mois et les congés sont déjà en partie provisionnés si la clôture est intervenue entre-temps).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/11/2026 | OD-PAIE | 6411 | Salaires, appointements | STC S. Lopez – salaire novembre | 2 600,00 | |
| 30/11/2026 | OD-PAIE | 6413 | Primes et gratifications | STC S. Lopez – 13e mois prorata | 2 383,33 | |
| 30/11/2026 | OD-PAIE | 6412 | Congés payés | STC S. Lopez – indemnité compensatrice CP | 1 520,00 | |
| 30/11/2026 | OD-PAIE | 6414 | Indemnités et avantages divers | Indemnité spécifique de rupture conventionnelle | 14 000,00 | |
| 30/11/2026 | OD-PAIE | 6451 | Cotisations à l'URSSAF | Patronal URSSAF STC | 2 373,72 | |
| 30/11/2026 | OD-PAIE | 6451 | Cotisations à l'URSSAF | Contribution patronale spécifique RC 30 % | 4 200,00 | |
| 30/11/2026 | OD-PAIE | 6453 | Cotisations aux caisses de retraite | Patronal AGIRC-ARRCO STC | 604,71 | |
| 30/11/2026 | OD-PAIE | 6452 | Cotisations aux mutuelles | Mutuelle patronale | 40,00 | |
| 30/11/2026 | OD-PAIE | 431 | Sécurité sociale (URSSAF) | 926,03 + 297,06 + 2 373,72 + 4 200,00 | | 7 796,81 |
| 30/11/2026 | OD-PAIE | 4371 | AGIRC-ARRCO | 403,44 + 604,71 | | 1 008,15 |
| 30/11/2026 | OD-PAIE | 4372 | Mutuelle | 40,00 + 40,00 | | 80,00 |
| 30/11/2026 | OD-PAIE | 4421 | État – prélèvement à la source | PAS STC | | 278,74 |
| 30/11/2026 | OD-PAIE | 421 | Personnel – rémunérations dues | Net payé STC S. Lopez | | 18 558,06 |
| | | | | **Totaux** | **27 721,76** | **27 721,76** |

> Si une dette de CP (4282/4382) a été constatée pour Sandrine Lopez au 31/12/2025 et n'a pas été extournée, l'indemnité compensatrice versée vient la solder (débit 4282 au lieu de 6412 pour la part correspondante) : vérifiez la méthode du dossier (extourne ou ajustement global).

## 4. Points d'attention / pièges

- **Ne pas confondre** indemnité légale et indemnité négociée : seul le supra-légal supporte la CSG/CRDS, mais **toute** la part exonérée de cotisations supporte la contribution patronale.
- **Taux de la contribution patronale** : il a déjà changé (remplacement du forfait social de 20 % par une contribution de 30 % au 01/09/2023) et un nouveau relèvement a été discuté — **vérifiez le taux à la date de la rupture**.
- **Salariée en droit de partir à la retraite** : régime totalement différent (indemnité entièrement soumise). À vérifier systématiquement pour les salariés âgés.
- **Clôture** : si la convention était signée avant une clôture et l'homologation obtenue après, l'indemnité serait une **charge à payer** (4286 / 4386) à la clôture si l'homologation est quasi certaine ; une simple négociation en cours ne justifie aucune écriture.
- **DSN** : signalement de fin de contrat de travail (FCTU) dans les 5 jours ; l'indemnité et la contribution patronale figurent dans la DSN mensuelle de novembre.
- **Délai de carence France Travail** : une indemnité supra-légale élevée allonge le différé d'indemnisation de la salariée — argument fréquent de négociation, sans incidence pour l'employeur.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

- Vérifier la **date d'envoi** effective de la demande d'homologation et conserver l'accusé de réception TéléRC dans le dossier social.
- Vérifier l'absence de **litige** en cours avec la salariée (une rupture conventionnelle signée dans un contexte conflictuel reste valable sauf vice du consentement — risque prud'homal à apprécier).
- Préparer les **documents de fin de contrat** : certificat de travail, attestation France Travail (via la DSN), reçu pour solde de tout compte (dénonçable dans les 6 mois), état récapitulatif de l'épargne salariale le cas échéant ; portabilité de la mutuelle et de la prévoyance à mentionner.
- **Mail à Frédéric Blanc** :

> Bonjour Monsieur Blanc,
> Le minimum légal pour Mme Lopez est de 10 937,50 € (13 ans et 9 mois d'ancienneté, salaire de référence de 2 916,67 € compte tenu de son augmentation de juillet) : les 14 000 € convenus sont donc homologables.
> Le coût propre de la rupture sera de 18 200 € : 14 000 € d'indemnité, exonérée de cotisations, plus une contribution patronale de 30 % (4 200 €) payée à l'URSSAF. Mme Lopez supportera la CSG/CRDS sur la part au-delà du minimum légal (297,06 €).
> Calendrier : fin du délai de rétractation le 21 octobre ; la demande d'homologation pourra partir le 22, et un départ au 30 novembre est compatible avec les délais.
> Bien cordialement,

## 6. Références

- Code du travail : articles L. 1237-11 à L. 1237-16 (rupture conventionnelle, rétractation, homologation) ; L. 1234-9 et R. 1234-1 à R. 1234-4 (indemnité légale et salaire de référence) ; L. 1234-20 (reçu pour solde de tout compte).
- Code de la sécurité sociale : article L. 242-1 (exclusion d'assiette dans la limite de 2 PASS) ; article L. 137-12 (contribution patronale spécifique sur les indemnités de rupture conventionnelle) — *taux à vérifier*.
- CGI, article 80 duodecies (exonération d'IR des indemnités de rupture).
- PCG : comptes 6411 à 6414, 6451, 431, 437, 4421, 421.
