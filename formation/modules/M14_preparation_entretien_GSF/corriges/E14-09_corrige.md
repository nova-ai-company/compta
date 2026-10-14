# Corrigé E14-09 — Intérim : relevé d'heures non validé, facture d'Interim Azur et facture non parvenue de fin de mois

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-09](../exercices/E14-09_interim-releve-heures-fnp.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Rapprochement de la facture
Pour l'intérim, le « 3-way match » est : **contrat de mise à disposition** (commande, taux) / **heures validées** (réception) / **facture**. Ici :
- Diallo et Petrova : 70 h et 64 h facturées = validées = pointées ✓.
- Benali : 38 h facturées, 30 h validées et pointées. Les 8 h du dimanche 20/09 ne sont étayées par rien (site fermé, aucun badge) → **contestées**.
Décision : la facture est **comptabilisée** (elle est recevable, l'essentiel est dû) mais **bloquée** au paiement ; statut « En litige » via la PA ; demande d'avoir de 8 h × 24,85 = **198,80 € HT** (238,56 € TTC).

### Question 2 — Taux
12,30 × 2,02 = 24,846 € → arrondi contractuel **24,85 €** ✓. Le coefficient inclut les indemnités de fin de mission et de congés payés, que l'agence verse à l'intérimaire : elles ne sont donc **pas** à provisionner chez GSF Riviera.

### Question 3 — Charge de septembre et FNP
La charge de septembre comprend toutes les heures **effectivement travaillées en septembre**, facturées ou non. Pour 21-30/09, aucune facture et pas de validation sur le portail : il faut une FNP, sur la **meilleure estimation fiable** disponible au moment de la clôture.
- Les 126 h déclarées par l'agence ne sont pas validées et dépassent le planning et le pointage.
- Les **120 h** sont corroborées par **deux sources internes indépendantes** (pointage badgeuse et planning) → base retenue : 120 h × 24,85 = **2 982,00 € HT**.
- Les 6 h d'écart ne sont ni certaines ni probables à ce stade : on les documente en commentaire de la FNP (elles seront contestées par Julien Roux le 05/10, ce qui confirme le choix).
L'absence du chef d'établissement n'est pas une raison de ne rien provisionner : une charge de septembre non constatée fausse le reporting de marge de l'établissement.

### Avoir à recevoir au 30/09
Les 8 h contestées sont **certaines** dans leur principe au 30/09 (aucune preuve de travail, pointage négatif) : on peut constater un **avoir à recevoir** de 198,80 € HT pour que la charge de septembre soit exacte (« sans les heures contestées », demande de Thomas Vidal). C'est un jugement : si la contestation était plus fragile, on aurait laissé la charge et signalé le litige.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | HT | TVA | TTC |
|---|---|---|---|---|
| Facture IA-26-09-1187 | 172 h × 24,85 | 4 274,20 | 854,84 | 5 129,04 |
| Heures validées 07-20/09 | 164 h × 24,85 | 4 075,40 | 815,08 | 4 890,48 |
| Heures contestées | 8 h × 24,85 | 198,80 | 39,76 | 238,56 |
| FNP 21-30/09 | 120 h × 24,85 | 2 982,00 | 596,40 | 3 578,40 |
| (pour mémoire, base agence) | 126 h × 24,85 | 3 131,10 | | |
| **Charge d'intérim de septembre (Cannes)** | 4 274,20 − 198,80 + 2 982,00 | **7 057,40** | | |
| Virement du 21/10 | 5 129,04 − 238,56 | | | **4 890,48** |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 21/09/2026 | AC | 6211 | Personnel intérimaire | IAZ IA-26-09-1187 07-20/09 (CAN) | 4 274,20 | |
| 21/09/2026 | AC | 44566 | TVA déductible sur ABS | IAZ IA-26-09-1187 TVA 20 % | 854,84 | |
| 21/09/2026 | AC | 401IAZ | Fournisseur Interim Azur | IAZ IA-26-09-1187 – LITIGE 8 h Benali | | 5 129,04 |
| 30/09/2026 | OD | 4098 | Fournisseurs – avoirs à recevoir | AAR IAZ 8 h Benali 20/09 contestées | 238,56 | |
| 30/09/2026 | OD | 6211 | Personnel intérimaire | AAR IAZ 8 h Benali 20/09 contestées | | 198,80 |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | AAR IAZ TVA 8 h contestées | | 39,76 |
| 30/09/2026 | OD | 6211 | Personnel intérimaire | FNP IAZ 21-30/09 120 h (pointage) (CAN) | 2 982,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP IAZ 21-30/09 TVA | 596,40 | |
| 30/09/2026 | OD | 4081 | Fournisseurs – factures non parvenues | FNP IAZ 21-30/09 120 h | | 3 578,40 |
| 01/10/2026 | OD | 6211 | Personnel intérimaire | Extourne AAR IAZ 8 h Benali | 198,80 | |
| 01/10/2026 | OD | 44586 | TVA sur factures non parvenues | Extourne AAR IAZ 8 h Benali | 39,76 | |
| 01/10/2026 | OD | 4098 | Fournisseurs – avoirs à recevoir | Extourne AAR IAZ 8 h Benali | | 238,56 |
| 01/10/2026 | OD | 4081 | Fournisseurs – factures non parvenues | Extourne FNP IAZ 21-30/09 | 3 578,40 | |
| 01/10/2026 | OD | 6211 | Personnel intérimaire | Extourne FNP IAZ 21-30/09 | | 2 982,00 |
| 01/10/2026 | OD | 44586 | TVA sur factures non parvenues | Extourne FNP IAZ 21-30/09 | | 596,40 |
| 14/10/2026 | AC | 401IAZ | Fournisseur Interim Azur | IAZ IA-AV-26-0212 8 h Benali | 238,56 | |
| 14/10/2026 | AC | 6211 | Personnel intérimaire | IAZ IA-AV-26-0212 8 h Benali | | 198,80 |
| 14/10/2026 | AC | 44566 | TVA déductible sur ABS | IAZ IA-AV-26-0212 TVA 20 % | | 39,76 |
| 21/10/2026 | BQ | 401IAZ | Fournisseur Interim Azur | Vir. IAZ IA-26-09-1187 net avoir | 4 890,48 | |
| 21/10/2026 | BQ | 512 | Banque | Vir. IAZ IA-26-09-1187 net avoir | | 4 890,48 |
| | | | | **Totaux** | **17 892,00** | **17 892,00** |

> La facture de la quinzaine 21/09-04/10, quand elle arrivera, sera saisie normalement en octobre ; l'extourne de la FNP neutralise la part de septembre. Si elle porte 126 h sur 21-30/09, elle sera bloquée pour 6 h (contestation du 05/10).

## 4. Points d'attention / pièges

- **Payer « la facture telle qu'elle est »** parce que le chef d'établissement est absent : non. Mais **ne pas la saisir** non plus : la dette existe pour 4 890,48 €.
- **FNP à zéro faute de validation** : c'est l'erreur la plus fréquente en clôture J+5 ; la charge de septembre serait sous-estimée de près de 3 000 € et réapparaîtrait en octobre.
- **Ne pas provisionner les IFM/ICCP** : ils sont inclus dans le coefficient et payés par l'agence, pas par GSF.
- **TVA déductible sur une prestation de services** : le droit à déduction naît quand la TVA devient exigible chez le prestataire, c'est-à-dire à l'**encaissement**, sauf si le prestataire a **opté pour les débits**. Interim Azur porte la mention de l'option sur sa facture : la TVA est donc déductible dès la réception de la facture. Sans cette mention, il aurait fallu attendre le paiement (21/10) pour déduire les 815,08 €.
- **Délai de paiement** : 30 jours date de facture, conforme à la limite légale ; le blocage partiel ne doit pas retarder le paiement de la partie non contestée au-delà de l'échéance (ici réglée le 21/10, à l'échéance).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Contrôles sur une agence d'intérim (question 5)** :
1. **Obligation de vigilance** (attestation URSSAF tous les 6 mois, Kbis) et **attestation de garantie financière** de l'entreprise de travail temporaire (à défaut, l'entreprise utilisatrice peut être substituée pour les salaires et cotisations).
2. Concordance contrat de mise à disposition / motif de recours / durée : un contrat sans motif ou expiré expose à une requalification (sujet RH, mais la comptabilité voit passer les factures).
3. Rapprochement mensuel **heures facturées / heures validées / pointage** par site, et suivi des **délégations de validation** (un adjoint doit pouvoir valider en l'absence du chef d'établissement).
4. Contrôle du **coefficient** et du **taux** à chaque facture (une hausse de taux brut doit correspondre à un avenant).
5. Suivi du **coût d'intérim par établissement** vs heures d'absence : indicateur de pilotage de la marge.

**Mail à Interim Azur (02/10/2026)** :
> Bonjour, la facture IA-26-09-1187 est en litige pour 8 heures déclarées le 20/09 pour Mme Benali (CMD-26-4415) : le site était fermé et aucun pointage n'a été enregistré. Merci de nous adresser un avoir de 198,80 € HT (238,56 € TTC). Le solde (4 890,48 €) sera réglé à l'échéance du 21/10 dès réception. Les heures du 21 au 30/09 seront validées sur votre portail le 05/10.

**Message à Thomas Vidal** : coût d'intérim de septembre Cannes = **7 057,40 € HT** (dont 2 982,00 € de FNP sur 120 h pointées), 8 h contestées exclues ; 6 h en cours d'analyse sur la dernière décade, non provisionnées.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code du travail art. L. 1251-1 et suivants (travail temporaire), L. 1251-42 et suivants (contrat de mise à disposition), L. 1251-49 et suivants (garantie financière, substitution de l'utilisateur).
- Code du travail art. L. 8222-1 ; Code de la sécurité sociale art. L. 243-15 : obligation de vigilance.
- CGI art. 269-2-c et 271 : exigibilité et déduction de la TVA sur prestations de services.
- PCG : comptes 6211, 4081, 4098, 44586 ; principe d'indépendance des exercices (appliqué au mois).
- Code de commerce art. L. 441-10 : délais de paiement.
