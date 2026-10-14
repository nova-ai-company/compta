# Corrigé E14-12 — Rapprochement bancaire de fin de mois au siège : suspens, régularisations et chèque périmé

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-12](../exercices/E14-12_rapprochement-bancaire-siege.md)

*Rappel : montants fictifs.*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Pointage et classement
**En banque, pas (ou mal) en comptabilité → écritures à passer en septembre :**

| Opération | Montant | Écriture |
|---|---|---|
| Virement Machines Nett' : saisi 2 485,60 au lieu de 2 845,60 | écart 360,00 au débit en banque | Complément de 360,00 (D 401MNE / C 512) |
| Prélèvement télécom | 1 872,00 | Règlement de la dette 401TEL |
| Remontée cash pooling GSF Riviera | 45 000,00 | Mouvement du compte courant groupe 451GSFR |
| Virement non identifié REF 88412 | 3 240,00 | Compte d'attente 471 (question 4) |
| LCR n° 4471 échue | 12 600,00 | Solde de 403 |
| Commissions T3 | 516,00 TTC | 627 : 430,00 + TVA 86,00 |

**En comptabilité, pas en banque → suspens normaux de l'état de rapprochement :**

| Opération | Montant | Commentaire |
|---|---|---|
| CHQ 0045781 (24/09) | 2 400,00 | Chèque émis non encaissé, récent : normal |
| CHQ 0045783 (28/09) | 1 180,00 | Idem |
| Remise de chèques du 30/09 | 8 650,40 | Créditée en principe le 01/10 |
| Run fournisseurs du 30/09 | 46 912,55 | Débité en principe le 01/10 |
| CHQ 0044102 (12/08/2025) | 350,00 | **Anormal** : plus de 13 mois (question 5) |

### Question 5 — Le chèque de 2025
Un chèque doit être présenté dans un délai de **8 jours** (en France métropolitaine) ; passé **un an et huit jours** à compter de l'émission, l'action du porteur contre la banque est prescrite et la banque peut refuser de le payer. Mais la **dette envers le fournisseur**, elle, n'est pas éteinte par la prescription du chèque : elle suit la prescription commerciale (5 ans). Donc :
- on **annule le chèque en comptabilité** (il ne sera plus encaissé) : D 512 / C 401IAG — la dette réapparaît au compte fournisseur ;
- on **contacte le fournisseur** (chèque perdu ? jamais reçu ? adresse ?) et on le paie par virement après vérification de ses coordonnées (cf. procédure anti-fraude) ; on fait **opposition** sur le chèque pour éviter un double paiement s'il réapparaît.
Laisser le chèque en suspens « parce que ça a toujours été là » fausse la trésorerie et masque une dette.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Écart de saisie Machines Nett' | 2 845,60 − 2 485,60 | 360,00 € |
| Commissions HT / TVA | 516,00 / 1,20 = 430,00 ; TVA 86,00 | 430,00 / 86,00 € |
| Encaissements en banque non comptabilisés | 45 000,00 + 3 240,00 | 48 240,00 € |
| Décaissements en banque non comptabilisés | 360,00 + 1 872,00 + 12 600,00 + 516,00 | 15 348,00 € |
| Annulation chèque 2025 | | + 350,00 € |
| Solde comptable corrigé | 1 209 478,03 + 48 240,00 − 15 348,00 + 350,00 | **1 242 720,03 €** |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | BQA | 401MNE | Fournisseur Machines Nett' | Correction saisie vir. 24/09 MN-4390 (2 845,60 et non 2 485,60) | 360,00 | |
| 30/09/2026 | BQA | 512100 | Banque A | Correction saisie vir. 24/09 MN-4390 | | 360,00 |
| 30/09/2026 | BQA | 401TEL | Fournisseur opérateur télécom | Prlv télécom fact. 09-2026 | 1 872,00 | |
| 30/09/2026 | BQA | 512100 | Banque A | Prlv télécom fact. 09-2026 | | 1 872,00 |
| 30/09/2026 | BQA | 512100 | Banque A | Remontée cash pooling GSF Riviera 28/09 | 45 000,00 | |
| 30/09/2026 | BQA | 451GSFR | Groupe – compte courant GSF Riviera | Remontée cash pooling GSF Riviera 28/09 | | 45 000,00 |
| 30/09/2026 | BQA | 512100 | Banque A | Vir. non identifié REF 88412 | 3 240,00 | |
| 30/09/2026 | BQA | 471 | Compte d'attente | Vir. non identifié REF 88412 – à identifier | | 3 240,00 |
| 30/09/2026 | BQA | 403 | Fournisseurs – effets à payer | LCR n° 4471 échue 30/09 | 12 600,00 | |
| 30/09/2026 | BQA | 512100 | Banque A | LCR n° 4471 échue 30/09 | | 12 600,00 |
| 30/09/2026 | BQA | 627 | Services bancaires et assimilés | Commissions et frais T3 2026 | 430,00 | |
| 30/09/2026 | BQA | 44566 | TVA déductible sur ABS | Commissions T3 2026 TVA | 86,00 | |
| 30/09/2026 | BQA | 512100 | Banque A | Commissions et frais T3 2026 | | 516,00 |
| 30/09/2026 | BQA | 512100 | Banque A | Annulation CHQ 0044102 du 12/08/2025 non présenté | 350,00 | |
| 30/09/2026 | BQA | 401IAG | Fournisseur Imprimerie Azur Graphic | Annulation CHQ 0044102 – dette F IAG-2025-311 rétablie | | 350,00 |
| | | | | **Totaux** | **63 938,00** | **63 938,00** |

**État de rapprochement au 30/09/2026 (question 3)**

| Côté banque | Montant | Côté comptabilité | Montant |
|---|---|---|---|
| Solde du relevé (créditeur) | 1 284 562,18 | Solde du 512100 avant régularisations (débiteur) | 1 209 478,03 |
| − CHQ 0045781 non présenté | − 2 400,00 | + Remontée cash pooling | + 45 000,00 |
| − CHQ 0045783 non présenté | − 1 180,00 | + Virement non identifié (471) | + 3 240,00 |
| − Run fournisseurs du 30/09 non débité | − 46 912,55 | − Correction Machines Nett' | − 360,00 |
| + Remise de chèques du 30/09 non créditée | + 8 650,40 | − Prélèvement télécom | − 1 872,00 |
| | | − LCR n° 4471 | − 12 600,00 |
| | | − Commissions T3 | − 516,00 |
| | | + Annulation CHQ 0044102 | + 350,00 |
| **Solde rapproché** | **1 242 720,03** | **Solde corrigé** | **1 242 720,03** ✓ |

## 4. Points d'attention / pièges

- **Ne jamais « équilibrer » un rapprochement avec un écart en 471 ou en 658** : chaque euro doit être expliqué. Ici, l'écart Machines Nett' (360,00 €, chiffres inversés : écart divisible par 9) est typique d'une erreur de frappe.
- **Les suspens « comptabilité non banque » doivent se dénouer dans les premiers jours du mois suivant** : on vérifie le 01/10 et le 02/10 que la remise et le run sont bien passés. Un suspens de plus d'un mois est une anomalie à analyser.
- **Cash pooling** : la remontée de 45 000,00 € doit aussi être comptabilisée chez GSF Riviera (compte courant 451 côté filiale, en sens inverse) ; c'est un point de rapprochement des comptes réciproques (voir E14-17).
- **Frais bancaires** : la TVA n'est déductible que si la banque a opté et la facture la mentionne ; certaines commissions restent exonérées.
- **LCR** : l'échéance solde le 403 (et non le 401, déjà soldé à l'acceptation de l'effet).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Virement non identifié (question 4)** : en 471 au 30/09 (jamais en produit), puis recherche le jour même : demande à la banque du détail du donneur d'ordre (IBAN émetteur, nom complet), recherche dans la balance âgée **de toutes les sociétés du groupe** (un client a pu payer la mauvaise entité : dans ce cas, on le reverse ou on le refacture via le compte courant de l'entité concernée), recherche des combinaisons de factures (3 240,00 = plusieurs factures ? facture moins un avoir ?). Le 471 doit être **à zéro** à chaque clôture annuelle et justifié à chaque clôture mensuelle.

**Message à Isabelle Marchetti (question 5)** :
> Le chèque 0044102 de 350,00 € (Imprimerie Azur Graphic, août 2025) est annulé au 30/09 : il ne sera plus présenté (délai de présentation dépassé). Attention, la facture reste due : je contacte le fournisseur pour vérifier ce qu'il en est, et nous la réglerons par virement après contrôle de ses coordonnées. Je demande en parallèle une opposition sur le chèque à la banque. L'état de rapprochement est équilibré à 1 242 720,03 € ; trois écritures de septembre relèvent d'oublis de saisie (LCR, prélèvement télécom, cash pooling) que je propose d'automatiser par des règles d'affectation bancaire.

**Documentation** : état de rapprochement signé (préparé par / revu par), relevé joint, justificatif de chaque suspens de plus de 30 jours.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code monétaire et financier art. L. 131-32 (délai de présentation du chèque) et L. 131-59 (prescription d'un an et huit jours de l'action contre le tiré) (*à vérifier*).
- Code de commerce art. L. 110-4 : prescription quinquennale des obligations entre commerçants.
- PCG : comptes 512, 403, 451, 471, 627 ; obligation de justification des soldes (principe de régularité).
- CGI art. 260 B : option pour la TVA sur certaines opérations bancaires.
