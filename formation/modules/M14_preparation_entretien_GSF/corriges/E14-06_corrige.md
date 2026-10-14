# Corrigé E14-06 — Gérer un litige fournisseur de bout en bout : analyse, mail type, avoir reçu incomplet

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-06](../exercices/E14-06_litige-fournisseur-avoir-hygiene-pro.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Trois écarts
1. **Marchandises refusées** : 12 bidons percés ont été refusés avec **réserves écrites** sur le BL (art. 6 respecté) → ils ne doivent pas être payés : 12 × 14,20 = **170,40 € HT**.
2. **Remise contractuelle** : la commande brute (852,00 € HT) dépasse 800,00 € → remise de 5 % due. Appliquée sur les marchandises effectivement conservées (48 bidons, 681,60 € HT) : **34,08 € HT**. (Si la facture avait été correcte : 852,00 − 5 % = 809,40 € ; avoir des 12 bidons au prix net 161,88 € ; net 647,52 € HT : on retrouve bien 681,60 − 34,08.)
3. **Frais de port** : commande ≥ 500,00 € HT → franco : **35,00 € HT** indûment facturés.

Avoir attendu : 170,40 + 34,08 + 35,00 = **239,48 € HT**, TVA 47,90 €, **287,38 € TTC**. Montant net dû : 1 064,40 − 287,38 = **777,02 €**.

### Question 3 — L'argument du fournisseur
Le contrat dit « commande d'un montant brut ≥ 800,00 € HT » : le seuil s'apprécie sur la **commande**, pas sur le montant livré et conservé. Le refus des 12 bidons est dû à un défaut **du fournisseur** ; il ne peut pas s'en prévaloir pour supprimer la remise. L'argument ne tient pas : on maintient la demande de 34,08 € HT (40,90 € TTC), sur un ton ferme mais cordial, en citant l'article.

### Question 5 — Suivi
- La facture est **comptabilisée** (dette réelle) mais **bloquée** au paiement avec un code litige ; le statut « En litige » est transmis via la PA.
- À la clôture d'octobre (31/10), l'avoir AV26-0431 étant reçu le 28/10, il n'y a plus d'avoir à recevoir. Si le second avoir n'était pas arrivé, on n'aurait **pas** constaté d'avoir à recevoir (4098) sans accord du fournisseur… sauf si l'on considère la remise comme certaine au regard du contrat — décision du responsable, avec documentation.
- Dans la balance fournisseurs, la facture et les avoirs sont **lettrés ensemble** dès que le solde est réglé ; avant, le lettrage partiel (facture + avoir 1) permet de voir le reste à payer contesté.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | HT | TVA | TTC |
|---|---|---|---|---|
| Facture F26-7830 | 60 × 14,20 + 35,00 | 887,00 | 177,40 | 1 064,40 |
| Bidons refusés | 12 × 14,20 | 170,40 | | |
| Remise 5 % sur conservé | 48 × 14,20 = 681,60 × 5 % | 34,08 | | |
| Port (franco) | | 35,00 | | |
| **Avoir attendu** | | **239,48** | 47,90 | **287,38** |
| Avoir AV26-0412 | 170,40 + 35,00 | 205,40 | 41,08 | 246,48 |
| Avoir AV26-0431 | remise | 34,08 | 6,82 | 40,90 |
| **Net à payer** | 1 064,40 − 246,48 − 40,90 | | | **777,02** |
| Contrôle | (681,60 − 34,08) × 1,20 = 647,52 × 1,20 | | | 777,02 ✓ |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | HPD F26-7830 décapant (CAN) | 852,00 | |
| 30/09/2026 | AC | 6241 | Transports sur achats | HPD F26-7830 port | 35,00 | |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | HPD F26-7830 TVA 20 % | 177,40 | |
| 30/09/2026 | AC | 401HPD | Fournisseur Hygiène Pro Distribution | HPD F26-7830 – LITIGE | | 1 064,40 |
| 19/10/2026 | AC | 401HPD | Fournisseur Hygiène Pro Distribution | HPD AV26-0412 sur F26-7830 | 246,48 | |
| 19/10/2026 | AC | 6063 | Fournitures d'entretien et de petit équipement | HPD AV26-0412 12 bidons refusés | | 170,40 |
| 19/10/2026 | AC | 6241 | Transports sur achats | HPD AV26-0412 annulation port | | 35,00 |
| 19/10/2026 | AC | 44566 | TVA déductible sur ABS | HPD AV26-0412 TVA 20 % | | 41,08 |
| 27/10/2026 | AC | 401HPD | Fournisseur Hygiène Pro Distribution | HPD AV26-0431 remise 5 % F26-7830 | 40,90 | |
| 27/10/2026 | AC | 6096 | RRR obtenus sur achats non stockés | HPD AV26-0431 remise contractuelle 5 % | | 34,08 |
| 27/10/2026 | AC | 44566 | TVA déductible sur ABS | HPD AV26-0431 TVA 20 % | | 6,82 |
| 15/11/2026 | BQ | 401HPD | Fournisseur Hygiène Pro Distribution | Vir. HPD F26-7830 net avoirs | 777,02 | |
| 15/11/2026 | BQ | 512 | Banque | Vir. HPD F26-7830 net avoirs | | 777,02 |
| | | | | **Totaux** | **2 128,80** | **2 128,80** |

Après paiement, 401HPD pour ce dossier : 1 064,40 − 246,48 − 40,90 − 777,02 = **0** → lettrage F26-7830 / AV26-0412 / AV26-0431 / virement.

## 4. Points d'attention / pièges

- **Sans réserves écrites sur le BL**, la position de GSF Riviera aurait été beaucoup plus faible : c'est la pièce maîtresse. Rappeler aux établissements de les porter **sur le BL, devant le chauffeur**, avec le nombre d'unités.
- **Régulariser la TVA** : les avoirs réduisent la TVA déductible (art. 272 CGI) ; ne pas saisir l'avoir « HT seulement ».
- **Remise vs retour** : le retour de marchandises se crédite au compte d'achat ; la remise accordée après facture se crédite en 609 (6096 ici). Les deux sont acceptables tant que la méthode est constante, mais le 609 permet de suivre les remises obtenues.
- **Ne pas payer « net de ce que l'on pense dû »** sans avoir : un paiement de 777,02 € sans avoir laisserait 287,38 € ouverts chez le fournisseur et déclencherait des relances (voire des pénalités de retard et l'indemnité de 40 €).
- **Délai de paiement** : le litige n'arrête pas l'échéance de la partie non contestée ; ici, tout est réglé le 15/11 à l'échéance.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail d'ouverture de litige (question 2), 01/10/2026 :**
> Objet : Facture F26-7830 du 30/09/2026 – BC-2026-0931 – demande d'avoir
> Madame, Monsieur,
> Nous avons bien reçu votre facture F26-7830 (1 064,40 € TTC). Avant mise en paiement, nous relevons :
> 1. 12 bidons de décapant ont été refusés à la livraison (BL-77120, réserves écrites contresignées par votre chauffeur) : 170,40 € HT ;
> 2. la remise de 5 % prévue à l'article 4 du contrat-cadre n'a pas été appliquée (commande de 852,00 € HT) : 34,08 € HT sur les marchandises conservées ;
> 3. la commande ouvre droit au franco de port (article 5) : 35,00 € HT.
> Nous vous remercions de nous adresser via la plateforme un avoir de 239,48 € HT, soit 287,38 € TTC. La facture est en statut « en litige » ; le solde de 777,02 € sera réglé à l'échéance du 15/11/2026 dès réception de l'avoir.
> Cordialement, Comptabilité fournisseurs – GSF Riviera (siège, Sophia Antipolis).

**Réponse à l'avoir AV26-0412 (question 3), 20/10/2026 :**
> Merci pour l'avoir AV26-0412 (246,48 € TTC). Concernant la remise, l'article 4 du contrat-cadre apprécie le seuil sur le **montant brut de la commande**, soit 852,00 € HT pour BC-2026-0931 ; le refus des 12 bidons résulte de leur état à la livraison et ne peut priver GSF de la remise. Nous restons donc dans l'attente d'un avoir complémentaire de 34,08 € HT (40,90 € TTC). Le règlement du solde interviendra à l'échéance.

**Contrôles** : registre des litiges (date d'ouverture, montant, interlocuteur, relances, date de clôture), revue hebdomadaire avec les Achats ; remontée des fournisseurs à litiges récurrents (évaluation fournisseurs, label « relations fournisseurs et achats responsables » : on traite vite et on paie à l'heure ce qui n'est pas contesté).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce art. L. 133-3 (réserves au transporteur — délai de protestation de 3 jours, à vérifier selon le mode de transport) et L. 441-10 (délais de paiement).
- CGI art. 271 et 272 : droit à déduction et régularisation en cas de réduction de prix.
- PCG : comptes 6063, 6096, 6241, 401 ; règles d'enregistrement des RRR obtenus.
