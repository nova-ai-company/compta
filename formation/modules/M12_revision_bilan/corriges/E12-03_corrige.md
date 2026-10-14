# Corrigé E12-03 — Contrôles de cohérence sur la balance de Transports Leroy

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E12-03](../exercices/E12-03_controles-coherence-leroy.md)

## 1. Analyse (raisonnement pas à pas)

Une balance qui « tombe juste » (totaux débit = crédit) ne prouve rien : toutes les anomalies ci-dessous sont **équilibrées**. Le senior déroule mécaniquement la grille de contrôles du cours, **dans l'ordre**, sans se laisser influencer par « Kevin a tout passé ». Il distingue :
- les anomalies qu'il peut **corriger seul** sur pièce (421, 471, emprunt, affectation, capital, reclassements PCG 2025) ;
- celles qui exigent une **réponse ou une action du client** (fournisseur payé deux fois, client ayant payé deux fois, caisse, compte courant débiteur) ;
- celles qui ont une conséquence **déclarative** (TVA de mai).

## 2. Calculs — grille de contrôles

| # | Contrôle | Constat | Anomalie | Montant |
|---|---|---|---|---:|
| 1 | 421 soldé | 3 850 € créditeur : le salaire net de M. Diallo a été payé par un virement imputé en 6251 | **Oui** | 3 850,00 |
| 2 | 471 vide | 12 400 € débiteur : prélèvement DKV (relevé carte carburant de septembre) non imputé | **Oui** | 12 400,00 |
| 3 | Caisse jamais créditrice | 640 € **créditeur** : dépense « payée en caisse » alors que la caisse était vide → en réalité payée par quelqu'un (Bruno ?) de sa poche | **Oui** | 640,00 |
| 4 | Fournisseurs débiteurs | F-TOTAL débiteur de 2 980 € : facture TMF-0826-4471 **payée deux fois** (14/08 et 21/08) | **Oui** | 2 980,00 |
| 5 | Clients créditeurs | C-CARREF créditeur de 4 560 € : facture 2026-0731 **encaissée deux fois** (28/08 et 02/09) | **Oui** | 4 560,00 |
| 6 | 455 débiteur | 6 200 € : location d'une villa à Sète (vacances du président) payée avec la CB de la société | **Oui (grave)** | 6 200,00 |
| 7 | TVA collectée / CA | Mai : CA comptable 221 000 / base déclarée 194 000 → **27 000 € HT non déclarés**, TVA 5 400 € ; le 44571 (49 400 €) ≠ TVA de septembre (220 000 × 20 % = 44 000 €) : l'écart de 5 400 € est le reliquat de mai | **Oui** | 5 400,00 de TVA |
| 8 | Charges sociales / salaires | 190 000 / 560 000 = **33,9 %** (2025 : 33,5 %) | Non — cohérent | — |
| 9 | Immobilisations / fichier | 2182 : balance 2 330 000 / fichier 2 258 000 → écart **72 000 €** = semi-remorque Krone du 08/07/2026 absente du fichier (donc non amortie) | **Oui** | 72 000,00 |
| 10 | Emprunts / tableau | 1641 = 640 000 ; attestation : 612 400 → **27 600 €** = capital de juillet à septembre (3 × 9 200) passé en 6611 | **Oui** | 27 600,00 |
| 11 | Capital / statuts | 101 = 80 000 ; Kbis = **120 000** (incorporation de réserves du 15/06/2026 non comptabilisée) | **Oui** | 40 000,00 |
| 12 | Affectation N-1 passée | 120 = 142 000 € toujours présent au 30/09/2026 → affectation non comptabilisée (dividendes 60 000 non constatés en dette) | **Oui** | 142 000,00 |
| 13 | Nomenclature PCG 2025 | **6712** (amendes en exceptionnel) et **791** (transfert de charges) : comptes **supprimés / à ne plus utiliser** depuis les exercices ouverts au 01/01/2025 | **Oui** | 3 400,00 et 2 400,00 |
| 14 | Banque | 512 débiteur 38 870 € : à rapprocher du relevé au 30/09 (non fourni) | À contrôler | — |
| 15 | TICPE à recevoir | 19 400 € : à rapprocher de la demande de remboursement déposée (1er semestre) | À contrôler | — |
| 16 | Stock de gazole | 21 000 € : jauge de la cuve au 30/09 × dernier prix d'achat | À contrôler | — |

## 3. Écritures comptables de correction

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 421 | Personnel – rémunérations dues | Salaire sept. M. Diallo imputé en 6251 | 3 850,00 | |
| 30/09/2026 | OD | 6251 | Voyages et déplacements | Salaire sept. M. Diallo imputé en 6251 | | 3 850,00 |
| 30/09/2026 | OD | 6061 | Carburant (gazole) | Relevé DKV sept. 2026 (sur facture DKV) | 10 333,33 | |
| 30/09/2026 | OD | 44566 | TVA déductible sur ABS | Relevé DKV sept. 2026 | 2 066,67 | |
| 30/09/2026 | OD | 471 | Compte d'attente | Relevé DKV sept. 2026 | | 12 400,00 |
| 30/09/2026 | OD | 1641 | Emprunts auprès des établissements de crédit | Capital échéances juil.-sept. passé en intérêts | 27 600,00 | |
| 30/09/2026 | OD | 6611 | Intérêts des emprunts | Capital échéances juil.-sept. passé en intérêts | | 27 600,00 |
| 15/06/2026 | OD | 120 | Résultat de l'exercice (bénéfice) | Affectation résultat 2025 (AGO 15/06/2026) | 142 000,00 | |
| 15/06/2026 | OD | 457 | Associés – dividendes à payer | Affectation résultat 2025 | | 60 000,00 |
| 15/06/2026 | OD | 1068 | Autres réserves | Affectation résultat 2025 | | 82 000,00 |
| 15/06/2026 | OD | 1068 | Autres réserves | Augmentation de capital par incorporation (AGE 15/06/2026) | 40 000,00 | |
| 15/06/2026 | OD | 101 | Capital social | Augmentation de capital par incorporation | | 40 000,00 |
| 30/09/2026 | OD | 530 | Caisse | Dépense Norauto payée personnellement par B. Leroy (après confirmation) | 640,00 | |
| 30/09/2026 | OD | 455 | Associé – compte courant Bruno Leroy | Dépense Norauto payée personnellement | | 640,00 |
| 30/09/2026 | OD | 658 | Pénalités et amendes (*subdivision selon la nomenclature 2025 du PCG*) | Reclassement PCG 2025 des amendes | 3 400,00 | |
| 30/09/2026 | OD | 6712 | Pénalités, amendes fiscales et pénales | Reclassement PCG 2025 des amendes | | 3 400,00 |
| 30/09/2026 | OD | 791 | Transferts de charges d'exploitation | Reclassement PCG 2025 des IJSS subrogées | 2 400,00 | |
| 30/09/2026 | OD | 641 | Rémunérations du personnel (*subdivision « IJSS » selon la nomenclature 2025 du PCG / plan du cabinet*) | IJSS en diminution de la charge de personnel | | 2 400,00 |
| | | | | **Totaux** | **232 290,00** | **232 290,00** |

Remarques :
- **Caisse** : l'écriture 530 / 455 n'est passée **qu'après confirmation écrite** de Bruno qu'il a réglé lui-même la dépense (sinon, la question est : qui a payé ?). La caisse revient à zéro.
- **F-TOTAL** (2 980 € débiteur) : pas d'écriture, mais **demande de remboursement** au fournisseur (ou imputation sur la prochaine facture). Au bilan, le solde débiteur est présenté en « Autres créances » (fournisseurs débiteurs), **pas compensé** avec les autres fournisseurs.
- **C-CARREF** (4 560 € créditeur) : rembourser le client ou obtenir son accord pour imputation ; au bilan, présentation au passif (clients créditeurs / autres dettes).
- **Compte courant débiteur** : après l'écriture de caisse, il reste **5 560 € débiteur**. Aucune écriture ne « règle » le problème : Bruno doit **rembourser** (ou la dépense doit lui être refacturée et réglée). À défaut : risque pénal (abus de biens sociaux), interdiction des prêts aux dirigeants de SAS (art. L. 227-12 C. com.), revenus distribués (art. 111 a CGI) et le cas échéant avantage en nature.
- **Semi-remorque** : pas d'écriture d'origine à corriger, mais **création de la fiche immobilisation** (date de mise en service, durée, éventuels composants) pour calculer la dotation de la situation (prorata depuis juillet).
- **TVA de mai** : pas d'écriture (la TVA est déjà au 44571) ; régularisation de **5 400 €** sur la **CA3 de septembre** (déposée en octobre) ; un intérêt de retard peut être dû (*modalités à vérifier ; une régularisation spontanée est toujours préférable*).
- **Amendes** : non déductibles fiscalement (réintégration en fin d'exercice). Pour les deux contraventions où un conducteur a été **désigné**, l'amende est personnelle au conducteur : si l'entreprise la paie quand même, c'est un **avantage** pour le salarié (soumis à cotisations) — à voir avec la paie.

## 4. Impact sur le résultat provisoire

| Correction | Impact |
|---|---:|
| Salaire Diallo sorti des frais de déplacement (déjà dans la paie) | + 3 850,00 |
| Carburant DKV de septembre | – 10 333,33 |
| Capital d'emprunt sorti des intérêts | + 27 600,00 |
| Reclassements PCG 2025, affectation, capital, caisse | 0,00 |
| **Impact net** | **+ 21 116,67** |

(Avant amortissements, dont celui de la semi-remorque, et avant régularisations de la situation.)

## 5. Points d'attention / pièges

- **Ne jamais passer d'écriture « de solde »** pour vider un 471 ou un 421 : chaque correction s'appuie sur une pièce (facture DKV, virement Diallo, attestation bancaire).
- **Le taux de charges sociales est normal** : un contrôle qui ne révèle rien doit aussi être documenté (« contrôle effectué, pas d'anomalie »).
- **PCG 2025** : un junior laisse 6712 et 791 « parce que c'était comme ça l'an dernier ». Depuis les exercices ouverts au 01/01/2025, il n'y a plus de transferts de charges et les amendes ne sont plus en exceptionnel. Pensez aussi à **retraiter les comparatifs N-1** dans les états de synthèse (ou à l'expliquer en annexe).
- **Réserve légale** : après l'augmentation de capital à 120 000 €, le plafond de 10 % passe à 12 000 € ; la réserve légale (8 000 €) devra de nouveau être dotée de 5 % des bénéfices jusqu'à 12 000 € lors des prochaines affectations.
- Une situation intermédiaire destinée à une **banque** engage le cabinet : elle doit être établie avec le même sérieux qu'un bilan (et accompagnée d'un document précisant la nature de l'intervention).

## 6. Ce qu'un senior ferait en plus

**Mail à Bruno Leroy :**
> « Bonjour Bruno,
> Nous avons terminé les contrôles de la balance au 30/09. Plusieurs points sont à régulariser avant d'envoyer la situation à la banque :
> 1. **TotalEnergies** : la facture TMF-0826-4471 (2 980 €) a été payée deux fois (14/08 et 21/08). Pouvez-vous demander un remboursement ou un avoir ?
> 2. **Carrefour Supply Chain** a réglé deux fois la facture 2026-0731 (4 560 €) : il faut le rembourser ou convenir d'une imputation sur la prochaine facture.
> 3. **Ticket Norauto de 640 €** du 21/09 : l'avez-vous réglé personnellement ? Si oui, nous l'inscrivons à votre crédit en compte courant.
> 4. **Location de la villa à Sète (6 200 €)** payée avec la carte de la société : il s'agit d'une dépense personnelle. La loi interdit à une SAS de faire des avances à son président ; nous vous demandons de **rembourser** la société au plus vite (5 560 € après le point 3). Nous pouvons en parler de vive voix.
> 5. **TVA** : une facture de mai (Rhône Logistique, 27 000 € HT) n'a pas été déclarée ; nous la régularisons sur la déclaration de septembre (5 400 € de TVA en plus).
> 6. Merci de nous transmettre le **relevé bancaire au 30/09**, la **jauge de la cuve** au 30/09 et la copie de la **demande de remboursement de TICPE**.
> Le reste (capital, affectation 2025, emprunt, carburant) est corrigé de notre côté. Bien cordialement. »

**Réponse à « envoyez sans tout ça » :**
> « Je comprends l'urgence, mais une situation remise à votre banque porte le nom du cabinet. Une partie des corrections **améliore** d'ailleurs votre résultat (+ 21 000 € environ). En revanche, je ne peux pas transmettre un document avec un capital erroné, un emprunt surévalué ou une avance au dirigeant non signalée : la banque les verrait au bilan définitif. Nous pouvons vous envoyer la situation corrigée **jeudi**. »

- Documenter la grille dans le dossier (section A — points en suspens) et mettre en place une **revue mensuelle** du 471, du 421 et des comptes de tiers à solde inversé pour l'alternant.

## 7. Références

- PCG (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06) : suppression des comptes de transfert de charges, résultat exceptionnel restreint.
- Code de commerce : art. L. 227-12 (interdiction des emprunts / avances aux dirigeants de SAS) ; art. L. 232-10 (réserve légale : 5 % du bénéfice jusqu'à 10 % du capital) ; art. L. 225-130 (augmentation de capital par incorporation de réserves, applicable aux SAS par renvoi).
- CGI : art. 39-2 (amendes non déductibles) ; art. 111 a (avances aux associés) ; art. 287 (obligations déclaratives TVA).
