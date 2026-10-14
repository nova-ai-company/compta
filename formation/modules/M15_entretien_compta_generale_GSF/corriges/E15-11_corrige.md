# Corrigé E15-11 — Test technique « clients » : facture mensuelle, avoir, acompte, client en difficulté et pénalités de retard

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-11](../exercices/E15-11_clients-contrat-avoir-acompte-procedures-collectives.md)

*Rappel : société, tiers et montants fictifs. Hypothèse du test : GSF Riviera a opté pour la TVA d'après les débits (TVA collectée en 44571 dès la facture).*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**La règle de base à dire à voix haute pendant le test** : une **facture de vente** crée une **créance** sur le client (actif → on **débite** 411) et un **produit** (on **crédite** 706) ; la TVA facturée est une **dette** envers l'État (on **crédite** 44571). Un **avoir** fait exactement l'inverse.

### Question 1 — Facture mensuelle
- Écriture classique : D 411HBA 10 140,00 / C 706 8 450,00 / C 44571 1 690,00.
- **Anomalie** : « 60 jours **fin de mois** » dépasse les plafonds légaux. Entre professionnels, le délai ne peut pas dépasser **60 jours à compter de la date de la facture**, ou **45 jours fin de mois** si le contrat le prévoit. On saisit quand même la facture (la prestation a eu lieu), mais on **signale** l'anomalie au chef comptable : le modèle de facture ou la fiche client doit être corrigé (conditions alignées sur le contrat, dans les limites légales). Ce n'est pas à la comptable de modifier seule une condition commerciale.

### Question 2 — Avoir
- Une facture émise **ne se modifie pas et ne se supprime pas** (numérotation continue, chronologique, et, avec la facturation électronique, la facture est transmise via la plateforme). Pour réduire le montant facturé, on émet un **avoir** qui fait référence à la facture d'origine.
- Écriture : on annule une partie du produit (**débit** 706 360,00) et de la TVA (**débit** 44571 72,00) ; le client nous doit moins (**crédit** 411HBA 432,00).
- Solde dû par l'hôtel : 10 140,00 − 432,00 = **9 708,00 €**.

### Question 3 — Acompte
- **Réception de l'acompte (12/10)** : l'argent arrive (D 512) mais aucune prestation n'est encore faite : ce n'est **pas un produit**. On constate une **dette** envers le client (C 4191). Pour une **prestation de services**, la TVA est exigible à l'encaissement de l'acompte : 2 160,00 / 1,20 = 1 800,00 HT et 360,00 de TVA (C 44571).
- **Facture finale (28/10)** : on enregistre la **totalité** de la prestation (7 200,00 TTC), comme une facture normale.
- **Imputation** : on solde le 4191 (débit 1 800,00) et on enlève la TVA déjà déclarée sur l'acompte (débit 44571 360,00), en contrepartie du client (crédit 411DMA 2 160,00). Sans cette annulation, la TVA de l'acompte serait comptée deux fois.
- **Contrôle** : 411DMA = 7 200,00 − 2 160,00 = **5 040,00 €** = le « net à payer » de la facture ✓ ; 4191 soldé ✓ ; TVA nette collectée = 360,00 + 1 200,00 − 360,00 = **1 200,00 €** = 20 % de 6 000,00 ✓.

### Question 4 — Redressement judiciaire
- **Reclassement** : dès qu'un client est en procédure collective (ou que le recouvrement devient douteux), on transfère la créance de 411 vers **416 Clients douteux** : D 416GAL / C 411GAL 4 320,00. On voit ainsi d'un coup d'œil les créances à risque.
- **Dépréciation** : on constate la perte **probable** (principe de prudence) par une charge (D 6817) et une diminution de la valeur de l'actif (C 491).
- **Pourquoi le HT** : la TVA (720,00 €) n'est **pas** une perte pour GSF Riviera : si la créance devient irrécouvrable, cette TVA pourra être **récupérée** auprès de l'État. La seule perte possible est le HT : 3 600,00 × 60 % = **2 160,00 €**.
- **À ne surtout pas oublier** : **déclarer la créance** au mandataire judiciaire dans les **2 mois** de la publication au BODACC (soit 4 320,00 € TTC, montant total dû). Sans déclaration dans le délai, la créance n'est pas prise en compte dans la procédure. Et on **bloque** le compte client (plus de prestations à crédit sans accord du responsable).

### Question 5 — Liquidation clôturée pour insuffisance d'actif
La créance est maintenant **définitivement irrécouvrable** (perte certaine) :
- **Perte HT** : D 654 1 600,00.
- **TVA** : GSF Riviera a reversé 320,00 € à l'État en 2025 (option débits). La créance étant définitivement irrécouvrable, cette TVA est **récupérable** : on la porte en diminution de la TVA collectée (D 44571 320,00), sur la CA3 du mois, à condition d'adresser au débiteur (au liquidateur) une **facture rectificative** de la TVA (*modalités à vérifier au BOFiP*).
- On solde le 416 (C 416ARC 1 920,00).
- **Reprise** de la dépréciation devenue sans objet : D 491 / C 7817 1 600,00. Résultat net de l'année 2026 : − 1 600,00 + 1 600,00 = **0** : la perte avait déjà été « prise » en 2025.

### Question 6 — Retard de paiement
- Encaissement : D 512 / C 411SPB 12 000,00.
- Retard : du 30/08/2026 (échéance) au 29/10/2026 (paiement) = **60 jours**.
- Pénalités et indemnité de 40 € (due de plein droit **par facture** payée en retard) : ce sont des **indemnités** qui réparent un préjudice, pas le prix d'une prestation → **pas de TVA**.
- Comptes : pénalités = intérêts → **763** (produit financier) ; indemnité forfaitaire → **758** (produit de gestion courante). Depuis le règlement ANC n° 2022-06, on ne passe plus ces sommes en produits exceptionnels.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| TVA facture mensuelle | 8 450,00 × 20 % | 1 690,00 € |
| Avoir | 2 × 180,00 = 360,00 HT ; TVA 72,00 | 432,00 € TTC |
| Acompte HT / TVA | 6 000,00 × 30 % = 1 800,00 ; × 20 % = 360,00 | 2 160,00 € TTC |
| Solde client Dentaire Masséna | 7 200,00 − 2 160,00 | 5 040,00 € |
| Dépréciation Le Galet | 3 600,00 HT × 60 % | 2 160,00 € |
| Jours de retard SCI Promenade | 1 jour (31/08) + 30 (septembre) + 29 (octobre) | 60 jours |
| Pénalités de retard | 12 000,00 × 12,15 % × 60 / 365 = 239,671… | 239,67 € |
| Note de débit SCI Promenade | 239,67 + 40,00 | 279,67 € |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 12/10/2026 | BQ | 512 | Banque | Acompte SELARL Dentaire Masséna devis D-26-118 | 2 160,00 | |
| 12/10/2026 | BQ | 4191 | Clients – avances et acomptes reçus | Acompte Dentaire Masséna HT | | 1 800,00 |
| 12/10/2026 | BQ | 44571 | TVA collectée | Acompte Dentaire Masséna TVA 20 % | | 360,00 |
| 28/10/2026 | VT | 411DMA | Client SELARL Dentaire Masséna | F F-2026-10-0342 remise en état | 7 200,00 | |
| 28/10/2026 | VT | 706 | Prestations de services | F F-2026-10-0342 remise en état | | 6 000,00 |
| 28/10/2026 | VT | 44571 | TVA collectée | F F-2026-10-0342 TVA 20 % | | 1 200,00 |
| 28/10/2026 | OD | 4191 | Clients – avances et acomptes reçus | Imputation acompte sur F-2026-10-0342 | 1 800,00 | |
| 28/10/2026 | OD | 44571 | TVA collectée | Imputation acompte – TVA déjà déclarée | 360,00 | |
| 28/10/2026 | OD | 411DMA | Client SELARL Dentaire Masséna | Imputation acompte sur F-2026-10-0342 | | 2 160,00 |
| 29/10/2026 | BQ | 512 | Banque | Règlement SCI Promenade F-2026-07-0144 | 12 000,00 | |
| 29/10/2026 | BQ | 411SPB | Client SCI Promenade Bureaux | Règlement F-2026-07-0144 | | 12 000,00 |
| 31/10/2026 | VT | 411HBA | Client Hôtel Baie des Anges | F F-2026-10-0215 forfait octobre | 10 140,00 | |
| 31/10/2026 | VT | 706 | Prestations de services | F F-2026-10-0215 forfait octobre | | 8 450,00 |
| 31/10/2026 | VT | 44571 | TVA collectée | F F-2026-10-0215 TVA 20 % | | 1 690,00 |
| 31/10/2026 | VT | 706 | Prestations de services | AV A-2026-10-0031 vitrerie non réalisée | 360,00 | |
| 31/10/2026 | VT | 44571 | TVA collectée | AV A-2026-10-0031 TVA 20 % | 72,00 | |
| 31/10/2026 | VT | 411HBA | Client Hôtel Baie des Anges | AV A-2026-10-0031 vitrerie non réalisée | | 432,00 |
| 31/10/2026 | OD | 416GAL | Client douteux Restaurant Le Galet | Reclassement – RJ du 07/10/2026 | 4 320,00 | |
| 31/10/2026 | OD | 411GAL | Client Restaurant Le Galet | Reclassement – RJ du 07/10/2026 | | 4 320,00 |
| 31/10/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation Le Galet 60 % du HT | 2 160,00 | |
| 31/10/2026 | OD | 491 | Dépréciation des comptes clients | Dépréciation Le Galet 60 % du HT | | 2 160,00 |
| 31/10/2026 | OD | 654 | Pertes sur créances irrécouvrables | Les Arcades – LJ clôturée insuffisance d'actif | 1 600,00 | |
| 31/10/2026 | OD | 44571 | TVA collectée | Les Arcades – TVA récupérée créance irrécouvrable | 320,00 | |
| 31/10/2026 | OD | 416ARC | Client douteux Boulangerie Les Arcades | Les Arcades – solde créance irrécouvrable | | 1 920,00 |
| 31/10/2026 | OD | 491 | Dépréciation des comptes clients | Reprise dépréciation Les Arcades | 1 600,00 | |
| 31/10/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise dépréciation Les Arcades | | 1 600,00 |
| 31/10/2026 | VT | 411SPB | Client SCI Promenade Bureaux | ND pénalités + indemnité F-2026-07-0144 | 279,67 | |
| 31/10/2026 | VT | 763 | Revenus des autres créances | Pénalités de retard 60 j à 12,15 % | | 239,67 |
| 31/10/2026 | VT | 758 | Produits divers de gestion courante | Indemnité forfaitaire de recouvrement | | 40,00 |
| | | | | **Totaux** | **44 371,67** | **44 371,67** |

## 4. Points d'attention / pièges

- **Dépréciation sur le TTC** : erreur la plus fréquente en entretien. On déprécie le **HT** ; la TVA est récupérable en cas de perte définitive.
- **Récupérer la TVA trop tôt** : en redressement judiciaire, la créance n'est que **douteuse** ; la TVA ne se récupère qu'à l'irrécouvrabilité **définitive** (ici, clôture de la liquidation).
- **Oublier la reprise** de la dépréciation : sans elle, la perte serait comptée deux fois (6817 en 2025 + 654 en 2026).
- **Si GSF Riviera était sous le régime des encaissements** (cas par défaut pour les prestations de services), la TVA d'une facture impayée n'aurait **jamais été déclarée** (elle serait restée en 44574 « TVA en attente ») : à l'irrécouvrabilité, on solderait simplement ce 44574, il n'y aurait rien à « récupérer » sur la CA3. Posez toujours la question du régime.
- **Acompte en produit (706)** : non, aucune prestation n'est réalisée au 12/10 ; c'est une dette (4191).
- **TVA sur les pénalités** : non, ce sont des indemnités. Et l'indemnité de 40 € est **par facture**, pas par relance.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Ce que le recruteur attend** : des écritures justes, mais surtout que vous **expliquiez** chaque sens (débit/crédit), que vous repériez l'anomalie de délai, que vous pensiez à la **déclaration de créance** et que vous sachiez que la TVA ne se déprécie pas. Dire « je vérifierais avec vous avant de facturer des pénalités à un client important » montre du recul commercial.

**Mail type au chef comptable (question 1)** :
> Bonjour Laurent, la facture F-2026-10-0215 (Hôtel Baie des Anges) indique « 60 jours fin de mois », ce qui dépasse le plafond légal (60 jours date de facture ou 45 jours fin de mois). Je l'ai saisie, mais pouvez-vous me confirmer le délai prévu au contrat CN-2024-031 pour que je fasse corriger la fiche client ? Merci.

**Contrôles** : 4191 soldé après chaque facture finale ; 416 et 491 revus chaque mois avec la balance âgée ; dossier « procédures collectives » avec copie du BODACC, de la déclaration de créance et des courriers du mandataire.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 411, 416, 4191, 44571, 491, 654, 6817, 7817, 706, 758, 763 ; principe de prudence ; règlement ANC n° 2022-06 (résultat exceptionnel restreint).
- Code de commerce art. L. 441-10 (délais de paiement, pénalités de retard, indemnité forfaitaire) et D. 441-5 (montant de 40 €) (*à vérifier*).
- Code de commerce, livre VI : déclaration des créances au mandataire judiciaire (délai de 2 mois à compter de la publication au BODACC).
- CGI art. 269 (exigibilité de la TVA, option pour les débits) et art. 272 (récupération de la TVA sur créances définitivement irrécouvrables) ; BOFiP TVA (régularisations, facture rectificative).
- CGI art. 39-1-5° : déductibilité des dépréciations de créances.
