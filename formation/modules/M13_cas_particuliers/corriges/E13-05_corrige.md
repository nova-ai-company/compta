# Corrigé E13-05 — ImmoPlus : rapprochement des fonds mandants et honoraires passés à tort en chiffre d'affaires

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E13-05](../exercices/E13-05_immoplus-fonds-mandants.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Deux contrôles différents, à ne pas confondre :**
1. le **rapprochement bancaire** : le solde du relevé du compte séquestre et le solde comptable de la banque dans la comptabilité mandants s'expliquent-ils par des suspens normaux ?
2. la **représentation des fonds** : l'argent réellement disponible sur le séquestre (relevé ajusté des suspens) couvre-t-il **toutes les sommes dues** aux mandants (propriétaires, dépôts de garantie, locataires, fournisseurs, honoraires non prélevés) ? C'est ce que vérifie le garant ; un déficit signifie que l'agence a utilisé, ou n'a pas reversé, l'argent de ses clients.

**Les anomalies :**
- **Frais de tenue du compte séquestre (18,50 €)** : prélevés sur le séquestre, donc payés avec l'argent des mandants. Sauf stipulation contraire des mandats, ils sont à la **charge de l'agence** → l'agence doit les rembourser au séquestre et les comptabiliser en charge (627).
- **Loyer de Mme Petitjean (1 150 €)** : la locataire a viré son loyer sur le compte **de l'agence**. L'outil de pré-comptabilisation l'a affecté en honoraires. Or c'est l'argent de M. Vasseur, le propriétaire : il n'est **pas** du chiffre d'affaires, et il **manque** sur le séquestre. L'agence doit le **virer sans délai** sur le compte séquestre ; la comptabilité mandants enregistre alors l'encaissement (crédit du locataire, crédit du propriétaire).
- **Honoraires de transaction Lambertin / Morel (12 000 € TTC)** : loi Hoguet, art. 6 — **aucune rémunération n'est due** à l'agent immobilier avant que l'opération ait été **effectivement conclue**, c'est-à-dire constatée par l'**acte authentique** (prévu le 20/11/2026). Le compromis ne fait naître aucune créance : la facture et le produit doivent être **annulés** (facture d'annulation / avoir ; nouvelle facture à l'acte). Comme ImmoPlus déclare sa TVA d'après les encaissements, la TVA n'était de toute façon pas exigible en septembre.
- **Honoraires de gestion de septembre (9 612 € TTC)** : correctement comptabilisés en 706 ; ils sont dus à l'agence mais encore sur le séquestre → simple virement à opérer (ce n'est pas une anomalie, c'est un suspens à apurer rapidement).

**Garantie financière.** Elle doit couvrir au moins le **montant maximal des fonds détenus** pour le compte des mandants au cours de la période (décret n° 72-678 du 20 juillet 1972 — *modalités et minimum légal à vérifier*). Le séquestre a atteint **405 860,12 €** le 08/09, pour une garantie de **350 000 €** → **insuffisante**.

## 2. Calculs (détaillés, chaque montant justifié)

**Total des sommes dues aux mandants selon la comptabilité mandants**

| Poste | Montant |
|---|---|
| Propriétaires créditeurs | 186 420,35 € |
| Dépôts de garantie | 96 300,00 € |
| Locataires créditeurs | 2 180,00 € |
| Honoraires de gestion non virés (dus à l'agence) | 9 612,00 € |
| Fournisseurs – travaux à payer | 3 248,40 € |
| **Total = solde comptable banque séquestre** | **297 760,75 €** ✓ |

**Question 1 — Rapprochement bancaire au 30/09/2026**

| | Montant |
|---|---|
| Solde du relevé bancaire | 298 702,25 € |
| + Remise de chèque non créditée (dépôt de garantie Haddad) | + 1 900,00 € |
| − Virement émis non débité (Mme Roche) | − 2 860,00 € |
| **Solde bancaire rectifié** | **297 742,25 €** |
| Solde de la comptabilité mandants | 297 760,75 € |
| − Frais de tenue de compte non comptabilisés | − 18,50 € |
| **Solde comptable rectifié** | **297 742,25 €** ✓ |

**Question 2 — Représentation des fonds**

| | Montant |
|---|---|
| Fonds disponibles (solde bancaire rectifié) | 297 742,25 € |
| Sommes dues selon la comptabilité mandants | 297 760,75 € |
| + Loyer Petitjean dû au propriétaire Vasseur (encaissé par l'agence) | + 1 150,00 € |
| **Sommes réellement dues** | **298 910,75 €** |
| **Déficit de représentation** | **− 1 168,50 €** (1 150,00 + 18,50) |

→ L'agence doit virer **1 168,50 €** de son compte courant vers le séquestre **immédiatement**.

**Question 3 — Chiffre d'affaires de septembre**

| | Montant HT |
|---|---|
| CA comptabilisé | 50 208,33 € |
| − Loyer Petitjean (1 150 / 1,20) | − 958,33 € |
| − Honoraires de transaction Lambertin / Morel (acte non signé) | − 10 000,00 € |
| **CA réel de septembre** | **39 250,00 €** |

Soit une surévaluation de 10 958,33 € (≈ 22 %) : l'« excellent mois » de Frédéric est un mois normal.

## 3. Écritures comptables

*Comptabilité de l'agence*

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 706 | Honoraires | Annulation : loyer Petitjean lot 42 affecté à tort | 958,33 | |
| 30/09/2026 | OD | 44571 | TVA collectée | Annulation : loyer Petitjean lot 42 affecté à tort | 191,67 | |
| 30/09/2026 | OD | 467MAND | Fonds mandants – liaison | Loyer Petitjean à reverser au séquestre | | 1 150,00 |
| 30/09/2026 | OD | 627 | Services bancaires | Frais tenue compte séquestre T3 à charge agence | 18,50 | |
| 30/09/2026 | OD | 467MAND | Fonds mandants – liaison | Frais tenue compte séquestre T3 à rembourser | | 18,50 |
| 30/09/2026 | VT | 706 | Honoraires | Annulation F T-2026-031 – acte authentique non signé | 10 000,00 | |
| 30/09/2026 | VT | 44571 | TVA collectée | Annulation F T-2026-031 – acte authentique non signé | 2 000,00 | |
| 30/09/2026 | VT | 411LAMB | Client Lambertin (vendeur) | Annulation F T-2026-031 – avoir n° T-2026-031A | | 12 000,00 |
| 09/10/2026 | BQ | 467MAND | Fonds mandants – liaison | Virement de couverture agence → séquestre | 1 168,50 | |
| 09/10/2026 | BQ | 512 | Banque – compte courant agence | Virement de couverture agence → séquestre | | 1 168,50 |
| 09/10/2026 | BQ | 512 | Banque – compte courant agence | Virement honoraires de gestion septembre depuis le séquestre | 9 612,00 | |
| 09/10/2026 | BQ | 467MAND | Fonds mandants – liaison | Virement honoraires de gestion septembre depuis le séquestre | | 9 612,00 |
| | | | | **Totaux** | **23 949,00** | **23 949,00** |

*Le 467MAND avait été débité de 9 612,00 € le 30/09 lors de la constatation des honoraires de gestion (D 467MAND / C 706 8 010,00 / C 44571 1 602,00) : après ces écritures, il est soldé. Si la TVA des honoraires est suivie en 44574 « TVA collectée en attente d'encaissement », adapter les comptes ; l'important est que ces montants ne figurent pas dans la TVA exigible de septembre.*

*Comptabilité mandants (logiciel de gestion)* : encaissement de 1 150,00 € au crédit du compte locataire Petitjean et au crédit du compte propriétaire Vasseur (date de valeur du virement de couverture) ; enregistrement des frais de 18,50 € en débit banque séquestre / crédit compte « agence – remboursement de frais » (le remboursement de l'agence venant le compenser) ; virement des honoraires de 9 612,00 € à l'agence.

## 4. Points d'attention / pièges

- **Un rapprochement bancaire « qui tombe juste » ne suffit pas** : ici, le rapprochement bancaire est équilibré après correction des frais, mais la **représentation des fonds** fait apparaître un déficit dû à un encaissement… sur le mauvais compte.
- **Jamais de loyer en chiffre d'affaires** : seuls les honoraires sont du CA. Paramétrez l'outil de pré-comptabilisation pour qu'aucun virement de locataire ne soit affecté automatiquement en 706.
- **Honoraires de transaction** : fait générateur à l'**acte authentique**, pas au compromis, même si le vendeur « est d'accord ». Aucun acompte sur honoraires ne peut être perçu avant (loi Hoguet art. 6).
- **Frais du séquestre** : à la charge de l'agence, sauf clause expresse des mandats.
- **TVA** : régime des encaissements pour des prestations de services → la TVA de la facture T-2026-031 n'était pas exigible ; et le loyer n'est pas une recette de l'agence (la location nue d'habitation est d'ailleurs exonérée chez le propriétaire).
- **Garantie** : on la compare au **solde le plus élevé** du séquestre (début de mois, après encaissement des loyers), pas au solde de fin de mois.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 5 — CA3 de septembre** : la déclaration n'étant pas déposée, on la corrige **avant dépôt** : la TVA collectée de septembre exclut 191,67 € (loyer) et les 2 000,00 € de la facture de transaction annulée. Aucune régularisation ultérieure n'est alors nécessaire. (Si elle avait été déposée, régularisation sur la CA3 d'octobre.)

**Question 6 — Garantie financière** : demander **sans délai** à la caisse de garantie une **augmentation** du plafond (au moins 410 000 €, et plutôt 450 000 € pour absorber la croissance du portefeuille) ; dans l'attente, organiser les reversements aux propriétaires plus tôt dans le mois (par exemple le 10 au lieu du 25) pour réduire le pic. Vérifier également que l'activité transaction ne détient réellement **aucun fonds** (acomptes des acquéreurs séquestrés chez le notaire) : sinon, une garantie « transaction » est nécessaire.

**Question 7 — Message à Frédéric Blanc :**

> Bonjour Frédéric,
>
> Le rapprochement du compte séquestre au 30/09 est fait. Trois points importants :
> 1. **Mme Petitjean** a viré son loyer de septembre (1 150 €) sur le compte de l'agence au lieu du compte mandants, et il a été enregistré comme honoraires. Il faut virer **1 168,50 €** du compte agence vers le compte séquestre **aujourd'hui** (le loyer + 18,50 € de frais bancaires du séquestre, qui sont à la charge de l'agence). Le garant considère tout manque sur le séquestre comme un incident grave.
> 2. **Les honoraires de la vente Lambertin / Morel** (12 000 € TTC) ne peuvent être facturés qu'à la signature de l'acte authentique (20/11). J'ai annulé la facture ; nous la referons après l'acte. Votre CA réel de septembre est donc de **39 250 € HT** (et non 50 208 €). La CA3 de septembre est corrigée avant son dépôt.
> 3. **Votre garantie financière (350 000 €) est insuffisante** : le compte séquestre a atteint 405 860 € le 8 septembre. Il faut demander dès maintenant une augmentation à votre caisse de garantie ; je peux vous préparer les chiffres.
>
> Pensez aussi à rappeler à vos locataires le RIB du compte mandants (quittances, avis d'échéance).

**Contrôles et documentation** : état de rapprochement signé et transmis au garant ; preuve du virement de couverture ; avoir T-2026-031A ; contrôle mensuel (et non trimestriel) de la représentation des fonds ; revue des **soldes débiteurs de propriétaires** (un propriétaire débiteur signifie que l'agence a payé pour lui avec l'argent des autres) ; vérification de la **non-compensation** entre comptes de propriétaires ; registre des mandats et carte professionnelle à jour au dossier permanent.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Loi n° 70-9 du 2 janvier 1970 (loi Hoguet), notamment art. 3 (garantie financière) et art. 6 (rémunération subordonnée à la conclusion effective de l'opération) ; décret n° 72-678 du 20 juillet 1972 (garantie financière, compte séquestre, registres).
- PCG : comptes de tiers (467) pour les fonds détenus pour le compte de tiers ; reconnaissance du chiffre d'affaires.
- CGI art. 269, 2-c (exigibilité de la TVA sur les prestations de services à l'encaissement) ; art. 261 D (exonération de la location nue de locaux d'habitation).
