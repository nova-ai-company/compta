# Corrigé E15-15 — Cas de synthèse « Votre première semaine » : saisie, rapprochement, clôture du mois, TVA et mail

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-15](../exercices/E15-15_synthese-premiere-semaine.md)

*Rappel : société, tiers et montants fictifs.*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Ordre de travail conseillé (1 h)** : saisie des pièces (15 min) → rapprochement (15 min) → clôture (10 min) → TVA et mail (10 min) → relecture des totaux (10 min). Faire la saisie **avant** le rapprochement évite de chercher des écarts qui n'en sont pas.

### Question 1 — Saisie
- **Pièce 1** : achat de produits consommés dans le mois → **charge** (6068), TVA déductible (44566), dette fournisseur (crédit 401HPM 2 808,00). La facture est complète (SIREN du client, nature de l'opération, pénalités, indemnité de 40 €) : rien à signaler.
- **Pièce 2** : 420,00 € HT < **500 € HT** → on peut, par tolérance, passer ce petit matériel **en charge** (6063) au lieu de l'immobiliser. C'est la pratique la plus simple et la plus courante.
- **Pièce 3** : la note de frais est une **dette envers le salarié** (crédit 421, sous-compte notes de frais) ; chaque dépense va dans sa charge : péage et parking en 6251 (déplacements), repas en 6256 (missions). La TVA figurant sur les tickets est déductible (dépenses engagées pour l'entreprise ; tickets acceptés pour ces petits montants).

### Question 2 — Rapprochement
**En banque, pas en comptabilité** → à comptabiliser :
- **Virement Cap Bleu 3 840,00** : règlement d'une facture → D 512 / C 411CAP. Comme la TVA est due **à l'encaissement**, on vire aussi 640,00 € de 44574 (en attente) vers 44571 (exigible) : cette TVA sera déclarée sur la CA3 d'octobre.
- **Frais de tenue de compte 32,00** : charge bancaire sans TVA → D 627 / C 512.
- **CB Brico Riviera 186,00** : l'argent est sorti, il faut l'enregistrer, mais **sans justificatif on ne sait ni quelle charge ni quelle TVA** passer. On l'enregistre en **compte d'attente 471** et on réclame la pièce (question 5). Pas de TVA déductible sans facture.

**En comptabilité, pas en banque** → suspens normal, pas d'écriture : **chèque 0001245 de 1 250,00** émis le 29/10 et pas encore encaissé par la Serrurerie Niçoise.

### Question 3 — Clôture d'octobre
- **Intérim** : le travail a été fait en octobre (heures validées) mais la facture n'est pas arrivée → **facture non parvenue** : charge 6211 3 150,00, TVA 44586 630,00, dette 408 3 780,00. Elle sera contre-passée le 01/11 et remplacée par la vraie facture.
- **Assurance** : 3 600,00 € passés en charge en octobre alors qu'ils couvrent 12 mois. Seul **1 mois** concerne octobre : 300,00 €. Les 11 mois restants (novembre 2026 à septembre 2027) sont une **charge constatée d'avance** : D 486 / C 616 3 300,00. Sans cette écriture, octobre serait surchargé de 3 300,00 €.

### Question 4 — Cadeau
La TVA d'un cadeau n'est récupérable que s'il est de **faible valeur** : on retient **73 € TTC** par bénéficiaire et par an (*valeur à vérifier chaque année*). 85,00 € TTC > 73 € → **TVA non récupérable** : on passera 85,00 € TTC en charge (6234 Cadeaux), sans TVA déductible.

**Réponse au chef d'établissement** :
> Bonjour, le coffret à 85 € dépasse le plafond des cadeaux de faible valeur (on retient 73 € TTC par bénéficiaire et par an) : la TVA ne sera pas récupérable, le coût réel sera donc de 85 €. Un coffret à 73 € TTC maximum permettrait de récupérer la TVA. Pensez à me transmettre la facture au nom de GSF Riviera avec le nom du client bénéficiaire.

### Question 5 — Mail pour la pièce manquante

> **Objet : Justificatif CB du 27/10 — Brico Riviera Nice — 186,00 €**
>
> Bonjour Monsieur Rossi,
>
> En faisant le rapprochement bancaire d'octobre, je trouve un paiement par carte de **186,00 €** chez **Brico Riviera Nice** le **27/10/2026** (débité le 29/10), pour lequel je n'ai pas reçu de justificatif.
>
> Pourriez-vous me transmettre la **facture** (au nom de GSF Riviera SAS, établissement de Nice) et me préciser en une ligne **l'objet de l'achat** (chantier ou usage) ? Je l'ai provisoirement enregistré en compte d'attente.
>
> Si possible **avant le vendredi 06/11**, pour que je puisse le classer dans les comptes d'octobre. Si la facture a été perdue, dites-le-moi : je demanderai un duplicata au magasin.
>
> Merci d'avance et bonne journée,
> [Prénom Nom] — Assistante comptable, GSF Riviera

*(Le nom du chef d'établissement est fictif.)* Ce qu'on attend d'un tel mail : **montant, date, fournisseur**, ce dont on a besoin, **pourquoi** et **pour quand**, ton neutre (pas de reproche).

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Pièce 1 — TVA | 2 340,00 × 20 % | 468,00 € |
| Pièce 3 — HT déplacements (6251) | (18,00 − 3,00) + (12,00 − 2,00) | 25,00 € |
| Pièce 3 — HT repas (6256) | 27,50 − 2,50 | 25,00 € |
| Pièce 3 — TVA | 3,00 + 2,50 + 2,00 | 7,50 € |
| TVA Cap Bleu exigible | 3 840,00 / 1,20 × 20 % | 640,00 € |
| FNP intérim | 3 150,00 × 20 % = 630,00 | 3 780,00 € TTC |
| CCA assurance | 3 600,00 × 11/12 | 3 300,00 € |
| Solde 512 corrigé | 48 615,30 + 3 840,00 − 186,00 − 32,00 | **52 237,30 €** |
| Solde banque rapproché | 53 487,30 − 1 250,00 | **52 237,30 €** ✓ |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 21/10/2026 | HA | 6063 | Fournitures d'entretien et de petit équipement | F OPA-5521 aspirateur dorsal | 420,00 | |
| 21/10/2026 | HA | 44566 | TVA déductible sur autres biens et services | F OPA-5521 TVA 20 % | 84,00 | |
| 21/10/2026 | HA | 401OPA | Fournisseur Outillage Pro Azur | F OPA-5521 aspirateur dorsal | | 504,00 |
| 27/10/2026 | HA | 6068 | Autres matières et fournitures | F HPM-26-10877 produits d'entretien | 2 340,00 | |
| 27/10/2026 | HA | 44566 | TVA déductible sur autres biens et services | F HPM-26-10877 TVA 20 % | 468,00 | |
| 27/10/2026 | HA | 401HPM | Fournisseur Hygiène Pro Méditerranée | F HPM-26-10877 produits d'entretien | | 2 808,00 |
| 30/10/2026 | OD | 6251 | Voyages et déplacements | NDF Karim B. 29/10 péage + parking | 25,00 | |
| 30/10/2026 | OD | 6256 | Missions | NDF Karim B. 29/10 repas | 25,00 | |
| 30/10/2026 | OD | 44566 | TVA déductible sur autres biens et services | NDF Karim B. 29/10 TVA | 7,50 | |
| 30/10/2026 | OD | 421NDF | Personnel – notes de frais à rembourser | NDF Karim B. 29/10 | | 57,50 |
| 31/10/2026 | BQ | 512 | Banque | Vir. Copro Le Cap Bleu F-2026-09-0301 | 3 840,00 | |
| 31/10/2026 | BQ | 411CAP | Client Copropriété Le Cap Bleu | Vir. Copro Le Cap Bleu F-2026-09-0301 | | 3 840,00 |
| 31/10/2026 | OD | 44574 | TVA collectée en attente d'encaissement | TVA exigible encaiss. F-2026-09-0301 | 640,00 | |
| 31/10/2026 | OD | 44571 | TVA collectée | TVA exigible encaiss. F-2026-09-0301 | | 640,00 |
| 31/10/2026 | BQ | 471 | Compte d'attente | CB Brico Riviera 27/10 – justificatif demandé | 186,00 | |
| 31/10/2026 | BQ | 512 | Banque | CB Brico Riviera 27/10 | | 186,00 |
| 31/10/2026 | BQ | 627 | Services bancaires et assimilés | Frais tenue de compte octobre | 32,00 | |
| 31/10/2026 | BQ | 512 | Banque | Frais tenue de compte octobre | | 32,00 |
| 31/10/2026 | OD | 6211 | Personnel intérimaire | FNP Intérim Riviera heures octobre | 3 150,00 | |
| 31/10/2026 | OD | 44586 | TVA sur factures non parvenues | FNP Intérim Riviera TVA | 630,00 | |
| 31/10/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Intérim Riviera heures octobre | | 3 780,00 |
| 31/10/2026 | OD | 486 | Charges constatées d'avance | CCA assurance 11 mois (11/2026 à 09/2027) | 3 300,00 | |
| 31/10/2026 | OD | 616 | Primes d'assurances | CCA assurance 11 mois (11/2026 à 09/2027) | | 3 300,00 |
| | | | | **Totaux** | **15 147,50** | **15 147,50** |

**État de rapprochement au 31/10/2026**

| Côté banque | Montant | Côté comptabilité | Montant |
|---|---|---|---|
| Solde du relevé (créditeur) | 53 487,30 | Solde du 512 avant corrections (débiteur) | 48 615,30 |
| − Chèque 0001245 non encaissé | − 1 250,00 | + Virement Copro Le Cap Bleu | + 3 840,00 |
| | | − CB Brico Riviera (471) | − 186,00 |
| | | − Frais de tenue de compte | − 32,00 |
| **Solde rapproché** | **52 237,30** | **Solde corrigé** | **52 237,30** ✓ |

## 4. Points d'attention / pièges

- **Oublier la TVA à l'encaissement** : avec la TVA sur les encaissements, chaque règlement client déclenche le virement 44574 → 44571, sinon la TVA d'octobre est sous-déclarée.
- **Passer la CB sans pièce en charge avec TVA** : pas de facture, pas de TVA déductible ; le 471 doit être soldé dès réception du justificatif (ou, à défaut, passé en charge sans TVA après validation du chef comptable).
- **Passer une écriture pour le chèque non encaissé** : non, c'est un décalage normal ; on vérifie seulement qu'il passe dans les jours suivants.
- **Charge constatée d'avance** : 11 mois et non 9 (on ne raisonne pas sur l'année civile mais sur la période couverte après octobre).
- **FNP sans TVA** : la TVA va en 44586 ; elle ne sera déductible qu'à réception de la facture.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Ce que le recruteur attend** : une méthode (ordre de travail), un rapprochement qui **tombe juste**, deux écritures de clôture expliquées simplement, une réponse TVA claire pour un non-comptable et un mail **poli, précis et daté**. Signaler ce qu'on n'a pas pu finir (« le 471 reste à solder ») vaut mieux que de le cacher.

**Pour la suite** : programmer la contre-passation de la FNP au 01/11 ; mettre un rappel au 06/11 pour la pièce Brico Riviera ; vérifier en novembre que le chèque 0001245 est bien débité ; classer l'état de rapprochement signé dans le dossier de clôture d'octobre.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : principe d'indépendance des exercices (factures non parvenues, charges constatées d'avance) ; comptes 408, 421, 44574, 44586, 471, 486, 6063, 6211, 616, 6251, 6256, 627.
- CGI art. 269 (exigibilité de la TVA sur les prestations de services à l'encaissement) ; art. 271 (droit à déduction, détention d'une facture) ; annexe II (exclusion des cadeaux, sauf biens de très faible valeur) (*à vérifier*).
- BOFiP : tolérance de passage en charge des biens de faible valeur (seuil de 500 € HT — *valeur à vérifier*) ; seuil des cadeaux de faible valeur (*valeur à vérifier chaque année*).
