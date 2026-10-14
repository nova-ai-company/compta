# Corrigé E14-03 — Avoir pour pénalités qualité en salles propres (Laboratoires Pharmabel)

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-03](../exercices/E14-03_avoir-penalites-qualite-pharmabel.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Deux natures différentes
**Article 11 — passages non exécutés (840,00 €).** Le contrat dit « réduction du prix forfaitaire » : la prestation facturée (27 400,00 € pour 22 passages en zone C) n'a été que partiellement rendue. C'est une **réfaction de prix** : elle **réduit la base d'imposition** à la TVA. GSF Riviera émet un **avoir avec TVA** (840,00 € HT + 168,00 € de TVA), comptabilisé en **709** (ou en diminution du 706 selon le paramétrage du groupe).

**Article 12 — non-conformités (1 050,00 €).** La pénalité forfaitaire est stipulée « en réparation du préjudice subi » : elle ne rémunère aucune prestation et ne réduit pas un prix, elle **indemnise** le client. Selon la doctrine administrative, une indemnité qui répare un préjudice et ne constitue pas la contrepartie d'une prestation est **hors du champ de la TVA**. Chez GSF Riviera, c'est une **charge** (658, pénalités sur marchés — *subdivision selon la nomenclature 2025 du PCG* ; depuis le règlement ANC n° 2022-06, ces pénalités courantes ne sont plus en résultat exceptionnel). Pas d'avoir avec TVA : la somme est simplement **compensée** sur le règlement (article 13), le document support étant l'avis de pénalités du client (ou une note de débit sans TVA).

> La frontière « réduction de prix / indemnité » est un sujet sur lequel la jurisprudence a évolué ; la qualification dépend de la rédaction du contrat. Dans un groupe, la position retenue doit être validée par le service fiscal **et appliquée uniformément** à tous les contrats similaires.

**Rattachement** : les manquements datent de septembre, l'avis est reçu le 05/10, avant l'arrêté des comptes de septembre → on constate au 30/09 un **avoir à établir** (réfaction) et une **charge à payer** (pénalités).

### Question 2 — Montants
Avoir : 840,00 € HT + TVA 168,00 € = **1 008,00 € TTC**.
Paiement dû : 32 880,00 − 1 008,00 (avoir) − 1 050,00 (pénalités, sans TVA) = **30 822,00 €**.
Virement reçu : 30 612,00 € → écart **210,00 €** = TVA de 20 % que Pharmabel a appliquée à tort sur les pénalités (1 050,00 × 20 %).

### Question 3 — TVA sur les encaissements
Le règlement du 20/10 éteint la créance à hauteur de 30 612,00 € (virement) + 1 050,00 € (compensation, qui vaut paiement) = 31 662,00 € TTC. La TVA devient exigible sur ce montant : 31 662,00 × 20/120 = **5 277,00 €**.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Réfaction (art. 11) HT | 2 × 420,00 | 840,00 € |
| TVA sur réfaction | 840,00 × 20 % | 168,00 € |
| Avoir TTC | | **1 008,00 €** |
| Pénalités (art. 12), hors champ | 3 × 350,00 | **1 050,00 €** |
| Facture de septembre TTC | 27 400,00 + 5 480,00 | 32 880,00 € |
| Montant dû par Pharmabel | 32 880,00 − 1 008,00 − 1 050,00 | **30 822,00 €** |
| Virement reçu | | 30 612,00 € |
| Écart (TVA réclamée à tort sur pénalités) | 30 822,00 − 30 612,00 = 1 050,00 × 20 % | **210,00 €** |
| Créance éteinte le 20/10 | 30 612,00 + 1 050,00 | 31 662,00 € |
| TVA exigible le 20/10 | 31 662,00 / 6 | 5 277,00 € |
| 44574 restant (facture) | 5 480,00 − 168,00 − 5 277,00 | **35,00 €** (= 210,00 / 6) |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 709 | Rabais, remises et ristournes accordés | AAE Pharmabel réfaction 2 passages zone C 09/2026 | 840,00 | |
| 30/09/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | AAE Pharmabel TVA réfaction | 168,00 | |
| 30/09/2026 | OD | 4198 | Clients – avoirs à établir | AAE Pharmabel réfaction 09/2026 | | 1 008,00 |
| 30/09/2026 | OD | 658 | Charges diverses de gestion courante – pénalités sur marchés | CAP pénalités qualité Pharmabel QA-2026-09 | 1 050,00 | |
| 30/09/2026 | OD | 4686 | Divers – charges à payer | CAP pénalités qualité Pharmabel QA-2026-09 | | 1 050,00 |
| 01/10/2026 | OD | 4198 | Clients – avoirs à établir | Extourne AAE Pharmabel | 1 008,00 | |
| 01/10/2026 | OD | 709 | Rabais, remises et ristournes accordés | Extourne AAE Pharmabel | | 840,00 |
| 01/10/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | Extourne AAE Pharmabel | | 168,00 |
| 01/10/2026 | OD | 4686 | Divers – charges à payer | Extourne CAP pénalités Pharmabel | 1 050,00 | |
| 01/10/2026 | OD | 658 | Charges diverses de gestion courante – pénalités sur marchés | Extourne CAP pénalités Pharmabel | | 1 050,00 |
| 15/10/2026 | VT | 709 | Rabais, remises et ristournes accordés | AV AV-2026-10-0007 réfaction art. 11 (F FR-2026-09-0480) | 840,00 | |
| 15/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | AV AV-2026-10-0007 TVA 20 % | 168,00 | |
| 15/10/2026 | VT | 411PHAR | Client Laboratoires Pharmabel | AV AV-2026-10-0007 réfaction art. 11 | | 1 008,00 |
| 20/10/2026 | BQ | 512 | Banque | Vir. Pharmabel F FR-2026-09-0480 | 30 612,00 | |
| 20/10/2026 | BQ | 658 | Charges diverses de gestion courante – pénalités sur marchés | Compensation pénalités QA-2026-09 (art. 12-13) | 1 050,00 | |
| 20/10/2026 | BQ | 411PHAR | Client Laboratoires Pharmabel | Règlement + compensation F FR-2026-09-0480 | | 31 662,00 |
| 20/10/2026 | OD | 44574 | TVA collectée en attente d'encaissement | TVA exigible encaiss. F FR-2026-09-0480 | 5 277,00 | |
| 20/10/2026 | OD | 44571 | TVA collectée | TVA exigible encaiss. F FR-2026-09-0480 | | 5 277,00 |
| | | | | **Totaux** | **42 063,00** | **42 063,00** |

## 4. Points d'attention / pièges

- **Solde après le 20/10 (question 4)** : 411PHAR = 32 880,00 − 1 008,00 − 31 662,00 = **210,00 € débiteur** ; 44574 = **35,00 €** créditeur. Ce n'est pas un écart à passer en perte : c'est une **créance réelle** (Pharmabel a retenu une TVA qui n'existe pas). On la réclame (question 5). Si Pharmabel maintenait sa position après échange, la décision (abandon commercial ou non) appartient au responsable, pas à la comptabilité — et un éventuel abandon serait une charge, pas un avoir avec TVA.
- **Un avoir avec TVA sur les pénalités** (ce que demandait le client) aurait minoré à tort la TVA collectée de 210,00 € : chez Pharmabel, la TVA « reversée » serait indûment déduite de sa TVA déductible… et chez GSF Riviera, elle aurait été réduite sans base. Risque de redressement des deux côtés.
- **Compensation = encaissement** pour l'exigibilité de la TVA : ne pas oublier de virer la TVA correspondant aux 1 050,00 € compensés.
- **Ne pas compenser sans écriture** : saisir seulement le virement de 30 612,00 € et laisser le 411 ouvert de 2 268,00 € fausse la balance âgée et le DSO.
- **Contrôler les clauses d'exclusion** avant d'accepter une pénalité (non-conformité due à une panne de la centrale de traitement d'air du client, par exemple) : c'est l'établissement qui juge, mais la comptabilité demande l'accord écrit du chef d'établissement.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à Pharmabel (question 5)**, après accord de Laure Pellegrino :
> Madame, Monsieur,
> Nous accusons réception de votre avis de pénalités QA-2026-09. Conformément au contrat PH-2025-002 :
> – la réduction de prix de l'article 11 (2 passages non réalisés, 840,00 € HT) fait l'objet de notre avoir AV-2026-10-0007 de 1 008,00 € TTC, ci-joint ;
> – les pénalités de l'article 12 (1 050,00 €) réparent un préjudice et ne sont pas soumises à la TVA : elles sont compensées pour leur montant net de 1 050,00 €, sans TVA.
> Votre règlement du 20/10 de 30 612,00 € laisse donc un solde de 210,00 € sur la facture FR-2026-09-0480, correspondant à la TVA appliquée sur les pénalités. Nous vous remercions de bien vouloir le régler.
> Nous restons à votre disposition. Cordialement, Comptabilité clients – GSF Riviera.

**Reporting** : distinguer dans le reporting de l'établissement la réfaction (baisse de chiffre d'affaires) et les pénalités (charge qualité) : le contrôle de gestion suit les pénalités comme un indicateur de qualité.
**Dossier** : conserver l'avis de pénalités, l'accord écrit de la cheffe d'établissement et l'analyse TVA validée.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 256 et 266-1-a : base d'imposition = contrepartie de la prestation ; CGI art. 267 : réductions de prix exclues de la base.
- BOFiP, TVA – Base d'imposition – sommes ne constituant pas la contrepartie d'une opération (indemnités) (*référence précise à vérifier*).
- CGI art. 269-2-c : exigibilité à l'encaissement des prestations de services.
- Code civil art. 1347 et suivants : compensation.
- PCG : comptes 709, 4198, 4686 ; règlement ANC n° 2022-06 (résultat exceptionnel restreint).
