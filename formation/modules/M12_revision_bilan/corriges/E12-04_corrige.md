# Corrigé E12-04 — Feuille maîtresse et feuilles de travail du cycle clients de l'Hôtel Belle Vue

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E12-04](../exercices/E12-04_feuille-maitresse-clients-hotel.md)

## 1. Analyse (raisonnement pas à pas)

Le cycle ventes / clients répond à quatre questions (les **assertions**) :
- **Existence / réalité** : les créances existent-elles ? → balance âgée, encaissements post-clôture (E1).
- **Évaluation** : seront-elles encaissées ? → créances anciennes, litiges, procédures (E2).
- **Séparation des exercices** : le CA de l'exercice correspond-il aux prestations **réalisées** entre le 01/11/2025 et le 31/10/2026 ? → FAE et PCA (E3).
- **Classement / présentation** : arrhes, clients créditeurs, sommes collectées pour le compte de tiers (E4).

La feuille maîtresse est le **sommaire** du cycle : chaque montant y renvoie à la feuille de travail qui le prouve et à l'OD qui le corrige.

## 2. Calculs — les feuilles de travail

### E1 — Balance âgée et encaissements post-clôture
**Objectif** : justifier l'existence des créances du compte 411 (86 400 €) et identifier les créances à risque.
**Travail** : rapprochement balance âgée PMS / balance générale ; pointage des encaissements du 01/11 au 05/11.

| Client | Solde 31/10 | Encaissé post-clôture | Reste | Conclusion |
|---|---:|---:|---:|---|
| Booking.com | 18 600,00 | 18 600,00 ✔ | 0,00 | Justifié |
| Expedia | 7 200,00 | 7 200,00 ✔ | 0,00 | Justifié |
| Agence Lyon Congrès | 22 800,00 | 10 800,00 ✔ | 12 000,00 | Client régulier, paiement à 60 jours habituel : pas de risque |
| Biotech Gerland | 13 200,00 | 0,00 | 13 200,00 | Facture d'avance d'un séminaire de novembre → **E3 (PCA)** |
| Cabinet Rivière Avocats | 3 200,00 | 0,00 | 3 200,00 | Litige → **E2** |
| Pharmalab Rhône | 13 800,00 | 13 800,00 ✔ | 0,00 | Justifié (61-90 j mais réglé le 05/11) |
| Particuliers débiteurs | 8 700,00 | 6 900,00 ✔ | 1 800,00 | Séjours récents, montant non significatif |
| Groupe scolaire Saint-Paul | – 1 100,00 | — | – 1 100,00 | Client **créditeur** = arrhes → **E4** |
| **Total** | **86 400,00** Σ ↔ | **57 300,00** | **29 100,00** | |

**Conclusion E1** : 66 % du solde est encaissé à J+5 ; le solde 411 est justifié sous réserve des ajustements E2, E3 et E4. → E

### E2 — Créances douteuses et irrécouvrables
**Objectif** : évaluer les créances à risque.

| Créance | Situation | Traitement | Calcul |
|---|---|---|---|
| Voyages Horizon (416, 2 900 TTC) | Liquidation clôturée pour **insuffisance d'actif** le 18/06/2026 | **Perte définitive** : sortie de la créance, reprise de la dépréciation | HT 2 900 / 1,10 = **2 636,36** en 654 ; TVA **263,64** ; reprise 491 **1 450,00** |
| Cabinet Rivière (3 200 TTC, > 90 j) | Litige écrit, client propose 50 % | **Créance litigieuse** : reclassement en 416, dépréciation du risque sur le **HT** | 3 200 / 1,10 = 2 909,09 HT × 50 % = **1 454,55** |

Remarque : la dépréciation N-1 de Voyages Horizon (1 450 € = 50 % du **TTC**) avait été calculée sur une base erronée ; sans incidence aujourd'hui puisque la créance sort, mais **à signaler** dans le dossier (bonne pratique pour les prochaines clôtures).
**Conclusion E2** : perte 2 636,36 €, reprise 1 450,00 €, dotation 1 454,55 €. → OD 1 à 4 → E

### E3 — Séparation des exercices

| Élément | Analyse | Ajustement |
|---|---|---|
| Nuitées du 29 au 31/10 de clients partis après la clôture | Prestations **réalisées** en N, facturées en N+1 | **FAE** 4 400 HT + TVA 440 = **4 840** |
| Séminaire Biotech du 15 au 17/11/2026, facturé le 25/10 | Prestation **non réalisée** au 31/10 | **PCA** 12 000 HT (la créance reste au 411 : la facture est émise et due) |

**Conclusion E3** : + 4 400 € et – 12 000 € de CA. → OD 5 et 6 → E

### E4 — Arrhes et taxe de séjour
- **Arrhes** : liste PMS 25 700 € vs 4191 = 24 600 € → écart 1 100 € = virement du Groupe scolaire lettré à tort sur le compte client. Reclassement 411 → 4191. Après correction : 4191 = **25 700 €** ✔ = PMS.
- **Taxe de séjour** : l'hôtel la **collecte pour le compte de la commune** ; ce n'est ni un produit ni une base de TVA. 4 980 € enregistrés en 706 depuis la mise à jour du PMS (septembre-octobre) → reclassement en compte de tiers. Contrôle : la déclaration / le reversement à la commune doit porter sur ces 4 980 €.
- **Conclusion E4** : reclassements 1 100 € et 4 980 €. Paramétrage PMS à corriger. → OD 7 et 8 → E

## 3. Écritures comptables (OD d'ajustement au 31/10/2026)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 654 | Pertes sur créances irrécouvrables | (1) Voyages Horizon – LJ clôturée | 2 636,36 | |
| 31/10/2026 | OD | 44571 | TVA collectée | (1) Voyages Horizon – récupération TVA | 263,64 | |
| 31/10/2026 | OD | 416 | Clients douteux | (1) Voyages Horizon – sortie | | 2 900,00 |
| 31/10/2026 | OD | 491 | Dépréciation des comptes clients | (2) Reprise dépréciation Voyages Horizon | 1 450,00 | |
| 31/10/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | (2) Reprise dépréciation Voyages Horizon | | 1 450,00 |
| 31/10/2026 | OD | 416 | Clients douteux | (3) Cabinet Rivière – litige | 3 200,00 | |
| 31/10/2026 | OD | 411 | Clients | (3) Cabinet Rivière – litige | | 3 200,00 |
| 31/10/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | (4) Dépréciation 50 % HT Rivière | 1 454,55 | |
| 31/10/2026 | OD | 491 | Dépréciation des comptes clients | (4) Dépréciation 50 % HT Rivière | | 1 454,55 |
| 31/10/2026 | OD | 418 | Clients – factures à établir | (5) Nuitées 29-31/10 non facturées | 4 840,00 | |
| 31/10/2026 | OD | 706 | Prestations de services | (5) Nuitées 29-31/10 non facturées | | 4 400,00 |
| 31/10/2026 | OD | 44587 | TVA sur factures à établir | (5) Nuitées 29-31/10 non facturées | | 440,00 |
| 31/10/2026 | OD | 706 | Prestations de services | (6) Séminaire Biotech 15-17/11/2026 | 12 000,00 | |
| 31/10/2026 | OD | 487 | Produits constatés d'avance | (6) Séminaire Biotech 15-17/11/2026 | | 12 000,00 |
| 31/10/2026 | OD | 411 | Clients | (7) Arrhes Groupe scolaire Saint-Paul | 1 100,00 | |
| 31/10/2026 | OD | 4191 | Clients – avances et acomptes reçus | (7) Arrhes Groupe scolaire Saint-Paul | | 1 100,00 |
| 31/10/2026 | OD | 706 | Prestations de services | (8) Taxe de séjour sept.-oct. en CA | 4 980,00 | |
| 31/10/2026 | OD | 447 | Autres impôts, taxes et versements assimilés – taxe de séjour à reverser (*ou compte de tiers dédié selon le plan du cabinet*) | (8) Taxe de séjour sept.-oct. | | 4 980,00 |
| | | | | **Totaux** | **31 924,55** | **31 924,55** |

> **TVA de la créance irrécouvrable** : l'écriture ci-dessus suppose que la TVA a été déclarée lors de la facturation (option pour les débits). Si l'hôtel acquitte la TVA **sur les encaissements** (régime de droit commun des prestations de services), la TVA d'une facture jamais encaissée n'a jamais été exigible : on solde alors le compte de TVA « en attente d'encaissement » où elle figure, sans régularisation sur la CA3. À vérifier sur le paramétrage du dossier.

## 4. Feuille maîtresse E — Cycle ventes / clients — Clôture 31/10/2026

| Compte | Intitulé | N-1 | N avant ajust. | Ajustements | N définitif | Variation N/N-1 | Réf. |
|---|---|---:|---:|---:|---:|---:|---|
| 411 | Clients | 71 200,00 | 86 400,00 | – 2 100,00 (OD 3, 7) | 84 300,00 | + 18,4 % | E1 |
| 416 | Clients douteux | 2 900,00 | 2 900,00 | + 300,00 (OD 1, 3) | 3 200,00 | + 10,3 % | E2 |
| 418 | Factures à établir | 3 300,00 | 0,00 | + 4 840,00 (OD 5) | 4 840,00 | + 46,7 % | E3 |
| 491 | Dépréciation clients | – 1 450,00 | – 1 450,00 | – 4,55 (OD 2, 4) | – 1 454,55 | + 0,3 % | E2 |
| **Créances clients nettes (actif)** | | **75 950,00** | **87 850,00** | | **90 885,45** | **+ 19,7 %** | |
| 4191 | Arrhes et acomptes reçus | – 19 800,00 | – 24 600,00 | – 1 100,00 (OD 7) | – 25 700,00 | + 29,8 % | E4 |
| 487 | Produits constatés d'avance | 0,00 | 0,00 | – 12 000,00 (OD 6) | – 12 000,00 | n.s. | E3 |
| 706 | Prestations de services | – 1 140 000,00 | – 1 180 000,00 | + 12 580,00 (OD 5, 6, 8) | – 1 167 420,00 | + 2,4 % | E3/E4 |
| 654 / 6817 / 7817 | Pertes, dotations, reprises | | | 2 636,36 + 1 454,55 – 1 450,00 | 2 640,91 (charge nette) | | E2 |

(Convention : soldes débiteurs positifs, soldes créditeurs négatifs.)

**Impact sur le résultat** : + 4 400,00 – 12 000,00 – 4 980,00 – 2 636,36 + 1 450,00 – 1 454,55 = **– 15 220,91 €** (supérieur au seuil de remontée → communiqué à Hélène Ferrand ; inférieur au seuil de signification).

**DSO** (clients TTC 84 300 + 3 200 + 4 840 = 92 340 / CA TTC approché 1 167 420 × 1,10) × 365 = **26,2 jours** (N-1 : 77 400 / (1 140 000 × 1,10) × 365 = 22,5 jours). Hausse expliquée par la facture Biotech émise d'avance (13 200 €) et par le litige Rivière.

**Conclusion du cycle** : « Sur la base des travaux E1 à E4, et après prise en compte des OD 1 à 8 (impact – 15 220,91 €), les comptes du cycle ventes / clients au 31/10/2026 n'appellent pas d'autre remarque. Points à suivre : litige Rivière (relance / transaction), paramétrage de la taxe de séjour dans le PMS. » — Préparé par : [initiales], le 06/11/2026 — Revu par : H.F., le …

## 5. Points d'attention / pièges

- **La facture Biotech reste en 411** : la PCA ne touche que le produit ; la créance existe juridiquement (facture émise et exigible à 30 jours).
- **Dépréciation sur le HT**, jamais sur le TTC (l'erreur N-1 le montre).
- **Arrhes ≠ CA** : les sommes reçues pour des séjours futurs restent en 4191 jusqu'à la prestation. Sur le plan de la TVA, les acomptes sur prestations de services rendent la TVA exigible à l'encaissement ; le sort des arrhes conservées en cas d'annulation ou de no-show (indemnité ou contrepartie d'un service ?) a évolué avec la jurisprudence européenne : *vérifier la doctrine administrative en vigueur* avant de conclure.
- **Compenser un client créditeur** avec les autres clients masque une erreur de classement.
- Les **4 980 € de taxe de séjour** gonflaient aussi le CA servant au calcul des ratios et, le cas échéant, de la CVAE.

## 6. Ce qu'un senior ferait en plus

**Réponse à Olivier Garnier :**
> « Non, la taxe de séjour n'est pas du chiffre d'affaires : vous la collectez **pour le compte de la commune** (ou de la métropole) et vous la reversez selon le calendrier fixé. Elle ne supporte pas la TVA et ne doit pas apparaître dans vos ventes. Depuis la mise à jour du logiciel du 1er septembre, elle était enregistrée en ventes : nous avons corrigé 4 980 €. Pouvez-vous demander à l'éditeur du PMS de rétablir le paramétrage, et nous transmettre votre dernière déclaration de taxe de séjour pour que nous vérifiions la concordance ? »

- Relancer le litige Rivière par un courrier proposant une **transaction** (geste commercial de 30 % ?) : un avoir de 960 € TTC vaut mieux que 3 200 € de créance dépréciée pendant deux ans.
- Archiver dans le dossier permanent la **procédure de clôture** du PMS (export des séjours en cours, des arrhes, de la taxe de séjour au dernier jour de l'exercice).

## 7. Références

- PCG : séparation des exercices (FAE 418, PCA 487), dépréciation des créances (491), pertes sur créances irrécouvrables (654).
- CGI : art. 269-2-c (exigibilité de la TVA sur les prestations de services à l'encaissement, option pour les débits) ; art. 272 (récupération de la TVA sur créances irrécouvrables).
- Code général des collectivités territoriales : dispositions relatives à la taxe de séjour (collecte par les hébergeurs pour le compte de la collectivité).
- Norme professionnelle de l'Ordre relative à la mission de présentation : documentation des travaux.
