# Corrigé E01-07 — Facture rectificative ou avoir ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-07](../exercices/E01-07_rectificative-ou-avoir.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Le principe directeur : une facture émise ne se modifie pas et ne se supprime pas.** Elle se corrige par un **document rectificatif** qui fait référence à la facture initiale « de manière précise et non équivoque » (CGI, annexe II, art. 242 nonies A). Deux outils :

| Outil | Quand | Effet |
|---|---|---|
| **Facture rectificative** | Erreur sur une **mention** (identité, adresse, SIREN, n° TVA, libellé), ou correction de montant (elle peut aussi porter un montant) | Remplace les informations erronées en citant la facture initiale |
| **Avoir** | **Diminution** du montant dû : remise accordée après coup, retour, annulation totale ou partielle | Réduit la base imposable et la TVA (CGI art. 272) |

En pratique, quand le montant change, la solution la plus lisible (et la mieux gérée par les logiciels) est **avoir total + nouvelle facture**.

### Cas 1 — Promotion Saône : mauvaise dénomination et mauvais SIREN
Seules des **mentions** sont erronées ; les montants sont justes. → **Facture rectificative FA-2026-0418 du 12/10/2026**, portant :
- la mention « **Facture rectificative de la facture n° FA-2026-0412 du 02/10/2026** » ;
- la dénomination et le SIREN corrects (PROMOTION SAÔNE SAS — 512 334 870) ;
- les montants inchangés (18 000,00 € HT ; 3 600,00 € TVA ; 21 600,00 € TTC).

Comptablement, **aucune écriture** si le logiciel permet de rattacher la rectificative à la créance existante (le client 411 est le même) ; si le logiciel génère une écriture, elle doit être neutralisée (ou bien on procède par avoir total + nouvelle facture, ce qui est aussi correct).
**Le SIREN client est une mention à part entière** (nouvelle mention de la réforme) : erroné, il empêchera demain l'acheminement de la facture électronique via l'annuaire.

### Cas 2 — Chevalier : taux de TVA erroné
Le taux de 10 % s'applique aux **travaux** d'amélioration, de transformation, d'aménagement et d'entretien portant sur des logements achevés depuis plus de deux ans. La doctrine administrative exclut en principe du taux réduit les **prestations intellectuelles** — dont les honoraires d'architecte et de maîtrise d'œuvre — lorsqu'elles sont facturées distinctement des travaux par un prestataire qui ne les réalise pas. → **Taux normal de 20 %** (point à vérifier dans le BOFiP en vigueur — taux réduit dans les logements, prestations exclues).

Le contrat prévoit des honoraires **HT** de 4 500,00 € → la TVA de 900,00 € est due par le client : le TTC passe de 4 950,00 € à **5 400,00 €**. Commercialement, c'est désagréable (450,00 € de plus pour un particulier) : il faut **l'expliquer** au client. Si Atelier Ligne refuse de réclamer le complément, elle devra absorber la différence en considérant le prix comme TTC (HT = 4 950,00 / 1,20 = 4 125,00 €, TVA 825,00 €) — décision commerciale, pas comptable.

Hypothèse retenue (contrat HT) : **avoir total AV-2026-0031** annulant FA-2026-0413 + **nouvelle facture FA-2026-0419** à 20 %.

### Cas 3 — Remise de 5 % accordée à Promotion Saône
Réduction de prix accordée **après** la facturation → **avoir partiel AV-2026-0032**, faisant référence à FA-2026-0412 (et à sa rectificative FA-2026-0418), motif « remise commerciale pour retard de livraison de la phase APD ». Comptablement : **709 Rabais, remises et ristournes accordés** (et non une diminution directe du 706), ce qui conserve l'information du chiffre d'affaires brut et des remises.

### Cas 4 — Facture DET annulée
La facture FA-2026-0414 a été **validée** : elle a un numéro et une écriture. Peu importe qu'elle n'ait pas été envoyée : la supprimer créerait un **trou dans la numérotation** et casserait la piste d'audit (et, après le 01/09/2027, elle aurait de toute façon été transmise via la PA dès sa validation). → **Avoir total AV-2026-0033**, référençant FA-2026-0414, motif « annulation – projet abandonné par le client ». On envoie les deux documents au client pour qu'il dispose d'un dossier cohérent.

**Réponse à Camille (question 3) :** « Non, une facture validée ne se supprime jamais, même non envoyée. On l'annule par un avoir. Si une facture est en cours de saisie et **pas encore validée** (pas de numéro définitif), on peut l'abandonner : c'est pour cela qu'il faut relire avant de valider. »

### Numérotation retenue

| Série factures | Série avoirs |
|---|---|
| FA-2026-0418 — 12/10 — rectificative de FA-0412 (Promotion Saône) | AV-2026-0031 — 12/10 — annule FA-0413 (Chevalier) |
| FA-2026-0419 — 12/10 — nouvelle facture Chevalier à 20 % | AV-2026-0032 — 12/10 — remise 5 % s/ FA-0412 (Promotion Saône) |
| | AV-2026-0033 — 12/10 — annule FA-0414 (SCM Brotteaux) |

## 2. Calculs (détaillés, chaque montant justifié)

| Document | HT | TVA | TTC |
|---|---|---|---|
| AV-2026-0031 (annulation FA-0413) | 4 500,00 € | 4 500,00 × 10 % = 450,00 € | 4 950,00 € |
| FA-2026-0419 (Chevalier à 20 %) | 4 500,00 € | 4 500,00 × 20 % = 900,00 € | 5 400,00 € |
| AV-2026-0032 (remise 5 %) | 18 000,00 × 5 % = 900,00 € | 900,00 × 20 % = 180,00 € | 1 080,00 € |
| AV-2026-0033 (annulation FA-0414) | 3 000,00 € | 600,00 € | 3 600,00 € |

Solde client Promotion Saône après avoir : 21 600,00 – 1 080,00 = **20 520,00 €** (17 100,00 € HT + 3 420,00 € TVA).
Solde client Chevalier : 4 950,00 – 4 950,00 + 5 400,00 = **5 400,00 €**.
Solde client SCM Brotteaux : 3 600,00 – 3 600,00 = **0,00 €**.

## 3. Écritures comptables

TVA sur les encaissements : la TVA des factures et avoirs reste en **44574 (TVA en attente)** tant qu'il n'y a pas d'encaissement ; elle sera virée en 44571 à l'encaissement.

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 12/10/2026 | VT | 706 | Prestations de services | AV-2026-0031 annul. FA-2026-0413 Chevalier (taux erroné) | 4 500,00 | |
| 12/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | AV-2026-0031 annul. FA-2026-0413 Chevalier | 450,00 | |
| 12/10/2026 | VT | 411CHEV | Client M. et Mme Chevalier | AV-2026-0031 annul. FA-2026-0413 Chevalier | | 4 950,00 |
| 12/10/2026 | VT | 411CHEV | Client M. et Mme Chevalier | FA-2026-0419 Chevalier honoraires conception TVA 20 % | 5 400,00 | |
| 12/10/2026 | VT | 706 | Prestations de services | FA-2026-0419 Chevalier honoraires conception | | 4 500,00 |
| 12/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | FA-2026-0419 Chevalier TVA 20 % | | 900,00 |
| 12/10/2026 | VT | 709 | Rabais, remises et ristournes accordés | AV-2026-0032 remise 5 % retard APD s/ FA-2026-0412 | 900,00 | |
| 12/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | AV-2026-0032 remise 5 % s/ FA-2026-0412 | 180,00 | |
| 12/10/2026 | VT | 411PROM | Client Promotion Saône SAS | AV-2026-0032 remise 5 % s/ FA-2026-0412 | | 1 080,00 |
| 12/10/2026 | VT | 706 | Prestations de services | AV-2026-0033 annul. FA-2026-0414 SCM Brotteaux (projet abandonné) | 3 000,00 | |
| 12/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | AV-2026-0033 annul. FA-2026-0414 SCM Brotteaux | 600,00 | |
| 12/10/2026 | VT | 411SCMB | Client SCM Cabinet médical des Brotteaux | AV-2026-0033 annul. FA-2026-0414 SCM Brotteaux | | 3 600,00 |
| | | | | **Totaux** | **15 030,00** | **15 030,00** |

FA-2026-0418 (rectificative de mentions) : **pas d'écriture** (montants inchangés, même compte client) — vérifier toutefois que le compte 411 porte la bonne dénomination et le bon SIREN dans la fiche tiers.

## 4. Points d'attention / pièges

- **Ne jamais réutiliser un numéro** ni « remplacer » une facture dans le logiciel en gardant le même numéro.
- **Toujours citer la facture d'origine** (numéro + date) sur l'avoir ou la rectificative. Un avoir sans référence ne permet pas de régulariser la TVA de manière probante.
- **TVA sur les encaissements** : un avoir sur une facture non encaissée ne modifie pas la TVA déclarée (elle n'était pas encore exigible). Si la facture avait déjà été payée et la TVA déclarée, l'avoir donnerait lieu à une régularisation de TVA collectée (et à un remboursement au client).
- **Le taux réduit n'est pas « contagieux »** : c'est la nature de la prestation facturée (honoraires intellectuels) qui compte, pas la nature du chantier.
- **709 vs 706** : une remise commerciale accordée après coup se suit en 709 ; une annulation de prestation (erreur, projet abandonné) annule le 706.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 5 — la facturation électronique.** À partir du 01/09/2027, Atelier Ligne émettra ses factures B2B **via sa PA** : la facture partira **dès sa validation**. Une erreur de **SIREN** client empêchera l'acheminement (rejet technique par la plateforme) ; une erreur de fond sera visible par le client et devra être corrigée par un avoir, lui-même transmis via la PA. Le client pourra **refuser** la facture (statut « refusée »), ce qui imposera d'émettre un avoir et une nouvelle facture. Pour les clients particuliers (Chevalier), pas de facture électronique : l'opération relèvera de l'**e-reporting**. Enfin, la mention « option pour le paiement de la TVA d'après les débits » n'ayant pas été choisie, le **statut « encaissée »** devra être transmis à chaque paiement reçu.

**Mail type à Camille Fabre :**

> Bonjour Camille,
>
> Voici comment traiter vos quatre factures (les documents sont prêts dans le logiciel, il ne reste qu'à les valider) :
> 1. Promotion Saône : facture rectificative FA-2026-0418 avec la bonne dénomination (SAS) et le bon SIREN — montants inchangés.
> 2. Chevalier : les honoraires d'architecte relèvent du taux de 20 %, même pour une rénovation. Avoir AV-2026-0031 puis nouvelle facture FA-2026-0419 de 5 400 € TTC. Votre contrat étant en HT, le complément de 450 € est dû par vos clients ; je vous suggère de les appeler avant l'envoi.
> 3. Remise de 5 % à Promotion Saône : avoir AV-2026-0032 de 1 080 € TTC.
> 4. SCM des Brotteaux : une facture validée ne peut pas être supprimée, même non envoyée. Avoir AV-2026-0033 qui l'annule ; envoyez les deux au client.
>
> Conseil : relisez la fiche client (dénomination, SIREN) avant chaque première facture — à partir de septembre 2027, une erreur de SIREN bloquera l'envoi de la facture électronique.

**Contrôles** : vérifier la continuité des deux séries (FA et AV) dans le journal des ventes ; vérifier les autres factures de particuliers émises à 10 % depuis l'ouverture du dossier (risque de rappel de TVA sur les exercices non prescrits).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI, annexe II, art. 242 nonies A : mentions des factures ; document rectificatif faisant référence à la facture initiale.
- CGI art. 272-1 : réduction de la base imposable en cas d'annulation, de rabais ou de remise après facturation.
- CGI art. 269-2-c : exigibilité de la TVA sur les prestations de services à l'encaissement (sauf option pour les débits).
- CGI art. 279-0 bis et BOFiP TVA – taux réduit de 10 % – travaux dans les logements de plus de deux ans (prestations exclues) — à vérifier dans la version en vigueur.
- CGI art. 289 bis et 290 : facturation électronique et e-reporting.
- PCG : compte 709 « Rabais, remises et ristournes accordés par l'entreprise ».
