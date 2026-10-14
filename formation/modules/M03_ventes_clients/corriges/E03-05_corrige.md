# Corrigé E03-05 — Arrhes, acomptes, no-show, Booking et taxe de séjour

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-05](../exercices/E03-05_arrhes-no-show-hotel.md)

## 1. Analyse

**a) Trois sommes versées d'avance, trois natures différentes**

| Pièce | Qualification | Conséquence civile |
|---|---|---|
| P1 Kinetic | **Acompte** (expressément stipulé, engagement ferme) | Le client doit le prix ; l'hôtel doit la prestation |
| P2 Lefort | **Arrhes** (art. 1590 C. civ. ; et en B2C, toute somme versée d'avance est présumée arrhes sauf stipulation contraire, art. L. 214-1 C. consom.) | Le client peut se dédire en perdant les arrhes |
| P3 Kowalska | **Prix d'un tarif non remboursable** payé d'avance | La cliente a acquis le droit à la prestation ; elle ne l'a pas utilisé |

**b) TVA à l'encaissement.** L'hébergement est une **prestation de services** : la TVA (10 %) est exigible **à l'encaissement**, y compris pour les acomptes et les arrhes (ce sont des paiements relatifs à une prestation déterminée). Les trois sommes génèrent donc de la TVA collectée le jour de leur encaissement.

**c) Après l'annulation ou le no-show.**
- **Arrhes conservées après dédit (P2)** : selon la jurisprudence européenne *Société thermale d'Eugénie-les-Bains* (CJCE, 18 juillet 2007, C-277/05) et la doctrine administrative qui en a tiré les conséquences, les arrhes conservées en cas de dédit du client sont une **indemnité forfaitaire** réparant le préjudice de l'hôtelier, sans lien direct avec un service rendu : **hors champ de la TVA**. La TVA acquittée à l'encaissement est **régularisée** (récupérée).
- **Tarif non remboursable non utilisé (P3)** : la CJUE (*Air France-KLM et Hop!-Brit Air*, 23 décembre 2015, C-250/14 et C-289/14) juge que le prix d'un billet non utilisé reste la **contrepartie** du droit de bénéficier du service : **TVA due**. De même, la CJUE (*MEO*, 22 novembre 2018, C-295/17) considère que les sommes dues en cas de rupture anticipée d'un contrat peuvent constituer la contrepartie de la prestation. Le no-show sur un tarif non remboursable est donc traité comme une **vente** : TVA maintenue, produit en 706.
- **Acompte Kinetic (P1)** : la prestation aura lieu en novembre ; aucune annulation à ce jour.

> **Note de position (à valider avec Hélène).** L'Hôtel Belle Vue distingue (1) les **arrhes** au sens de l'art. 1590 C. civ., conservées en cas de dédit du client, analysées comme une indemnité hors champ de TVA conformément à la jurisprudence Eugénie-les-Bains et à la doctrine administrative ; la TVA acquittée lors de l'encaissement est régularisée le mois de l'annulation ; (2) les **tarifs non remboursables** et no-shows sur réservations garanties, dont le prix rémunère le droit au service (jurisprudence Air France-KLM, MEO) : TVA maintenue. Compte tenu de l'évolution de la jurisprudence européenne sur les sommes conservées en cas d'annulation, cette position est documentée (CGV, contrats types) et **réexaminée chaque année** ; en cas de doute sur une catégorie de réservations, l'option prudente consiste à maintenir la TVA. Montants en jeu sur l'exercice : à chiffrer à partir du PMS (arrhes conservées).

**d) Booking.** Booking.com B.V. est établi aux Pays-Bas et facture une prestation de services à un assujetti français : le lieu de la prestation est en France (art. 259-1° CGI, règle générale B2B) et c'est le **preneur (l'hôtel) qui autoliquide** la TVA française à 20 % (art. 283-2 CGI). La facture sans TVA est normale. L'hôtel déclare la base (ligne **A3**), la TVA due (ligne **08**) et la déduit simultanément (ligne **20**) : opération neutre en trésorerie, mais obligatoire.

**e) Taxe de séjour.** Collectée par l'hôtel **pour le compte de la commune** : ce n'est ni un produit, ni une base de TVA. Elle va dans un **compte de tiers** jusqu'à son reversement. Le paramétrage du PMS (taxe de séjour soumise à TVA 10 % et comptée en CA) est faux : il fait payer de la TVA indue et gonfle le CA.

## 2. Calculs

| Opération | TTC | HT | TVA |
|---|---|---|---|
| Acompte Kinetic (10 %) | 810,00 | 736,36 | 73,64 |
| Séjour Kinetic complet | 2 700,00 | 2 454,55 | 245,45 |
| TVA restant due en novembre sur le solde | | | 245,45 – 73,64 = **171,81** |
| Arrhes Lefort (10 %) | 240,00 | 218,18 | 21,82 |
| Tarif non remboursable Kowalska (10 %) | 236,00 | 214,55 | 21,45 |
| Commission Booking 18 % × 14 160,00 | | 2 548,80 | autoliquidée 20 % : **509,76** |

**Facture Durieux corrigée**

| Ligne | TTC | HT | TVA |
|---|---|---|---|
| Chambre (10 %) | 270,00 | 245,45 | 24,55 |
| Petits-déjeuners (10 %) | 56,00 | 50,91 | 5,09 |
| Minibar bières (20 %) | 12,00 | 10,00 | 2,00 |
| Taxe de séjour : 2 adultes × 2 nuits × 2,10 € (l'enfant est exonéré) — **hors TVA** | 8,40 | — | — |
| **Total** | **346,40** | **306,36** | **31,64** |

Avec le paramétrage erroné, le PMS calcule une « TVA » de 0,76 € sur la taxe de séjour (8,40 × 10/110) : TVA indue, et 7,64 € de faux CA.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/09/2026 | BQ | 512 | Banque | Arrhes R-26-1187 Lefort | 240,00 | |
| 02/09/2026 | BQ | 4191 | Clients – avances et acomptes reçus | Arrhes Lefort | | 218,18 |
| 02/09/2026 | BQ | 44571 | TVA collectée 10 % | Arrhes Lefort (exigible à l'encaissement) | | 21,82 |
| 10/09/2026 | BQ | 512 | Banque | Acompte GRP-2026-031 Kinetic | 810,00 | |
| 10/09/2026 | BQ | 4191 | Clients – avances et acomptes reçus | Acompte Kinetic | | 736,36 |
| 10/09/2026 | BQ | 44571 | TVA collectée 10 % | Acompte Kinetic | | 73,64 |
| 14/09/2026 | VT | 512 | Banque (CB) | Facture H-26-09-2215 Durieux | 346,40 | |
| 14/09/2026 | VT | 706 | Prestations de services – hébergement | Chambre | | 245,45 |
| 14/09/2026 | VT | 706 | Prestations de services – petits-déjeuners | Petits-déjeuners | | 50,91 |
| 14/09/2026 | VT | 707 | Ventes de marchandises – minibar | Minibar | | 10,00 |
| 14/09/2026 | VT | 44571 | TVA collectée | 24,55 + 5,09 + 2,00 | | 31,64 |
| 14/09/2026 | VT | 467 | Commune de Lyon – taxe de séjour collectée | Taxe de séjour Durieux | | 8,40 |
| 15/09/2026 | BQ | 512 | Banque | Booking 4021778116 tarif NR Kowalska | 236,00 | |
| 15/09/2026 | BQ | 4191 | Clients – avances et acomptes reçus | Tarif NR Kowalska | | 214,55 |
| 15/09/2026 | BQ | 44571 | TVA collectée 10 % | Tarif NR Kowalska | | 21,45 |
| 20/09/2026 | OD | 4191 | Clients – avances et acomptes reçus | Arrhes Lefort conservées (dédit) | 218,18 | |
| 20/09/2026 | OD | 44571 | TVA collectée 10 % | Régularisation TVA – indemnité hors champ | 21,82 | |
| 20/09/2026 | OD | 758 | Produits divers de gestion courante (*subdivision selon la nomenclature 2025 du PCG*) | Indemnité de dédit Lefort | | 240,00 |
| 24/09/2026 | OD | 4191 | Clients – avances et acomptes reçus | No-show Kowalska – tarif NR | 214,55 | |
| 24/09/2026 | OD | 706 | Prestations de services – hébergement | No-show Kowalska – tarif NR | | 214,55 |
| 01/10/2026 | AC | 622 | Rémunérations d'intermédiaires (commissions) | Booking commission 09/2026 | 2 548,80 | |
| 01/10/2026 | AC | 401BOOK | Fournisseur Booking.com | Booking commission 09/2026 | | 2 548,80 |
| 01/10/2026 | AC | 44566 | TVA déductible sur ABS (autoliquidation) | Autoliquidation Booking 20 % | 509,76 | |
| 01/10/2026 | AC | 4452 | TVA due intracommunautaire (autoliquidation) | Autoliquidation Booking 20 % | | 509,76 |
| | | | | **Totaux** | **5 145,51** | **5 145,51** |

Remarques :
- La facture Booking est datée du 01/10 mais porte sur des séjours de septembre : la charge et la TVA autoliquidée sont rattachées à **septembre** (date de la prestation : les commissions sont dues séjour par séjour). En pratique, saisir la facture au 30/09 ou passer une **charge à payer** : la base figure sur la CA3 de **septembre**. Pour les services B2B continus, l'exigibilité de l'autoliquidation intervient à l'achèvement de la prestation (ou à l'encaissement d'un acompte).
- Le no-show est porté en 706 car la TVA est maintenue ; l'arrhes conservée en 758 car c'est une indemnité.

**Clôture du 31/10/2026 — acompte Kinetic** : aucune écriture. Le 4191 de 736,36 € figure au **passif** (avances reçues) ; la TVA de 73,64 € a déjà été déclarée en septembre. Le séjour, réalisé en novembre, appartient à l'exercice suivant.

**Par anticipation — facture de novembre (07/11/2026)** :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 07/11/2026 | VT | 411KIN | Client Kinetic Conseil | Facture séjour GRP-2026-031 (solde) | 1 890,00 | |
| 07/11/2026 | VT | 4191 | Clients – avances et acomptes reçus | Imputation acompte | 736,36 | |
| 07/11/2026 | VT | 706 | Prestations de services – hébergement | Séjour GRP-2026-031 | | 2 454,55 |
| 07/11/2026 | VT | 44574 | TVA collectée en attente (encaissement) | TVA sur solde | | 171,81 |
| | | | | **Totaux** | **2 626,36** | **2 626,36** |

(Taxe de séjour : 20 personnes majeures × 2 nuits × 2,10 € = 84,00 € à ajouter en 467 si les participants sont tous majeurs.)

## 4. Points d'attention / pièges

- **CA3 de septembre** : commission Booking en ligne **A3** (achats de prestations de services auprès d'un assujetti non établi en France, art. 283-2) pour 2 548,80 € ; TVA de 509,76 € incluse dans la ligne **08** (taux normal) et déduite en ligne **20** (autres biens et services). La régularisation des arrhes Lefort (21,82 €) se fait en ligne **21** « Autre TVA à déduire » (ou en minoration de la TVA collectée du mois, selon la méthode du cabinet) — *numérotation de la CA3 à contrôler sur le formulaire millésimé*.
- **Ne pas confondre** : arrhes conservées (indemnité, 758, hors champ) ≠ no-show sur tarif non remboursable (prix, 706, TVA).
- **Taxe de séjour** : compte de tiers, reversement selon le calendrier fixé par la collectivité, registre du logeur à tenir ; si une plateforme collecte elle-même la taxe pour le compte de l'hôtel, ne pas la compter deux fois.
- **Acomptes au 31/10** : faire l'inventaire de **toutes** les réservations payées d'avance pour des séjours postérieurs à la clôture : elles restent en 4191 (et non en CA).
- **Booking** : vérifier que la base de commission (14 160 €) correspond aux séjours Booking du mois dans le PMS.

## 5. Ce qu'un senior ferait en plus

- Faire **corriger le paramétrage du PMS** (taxe de séjour hors TVA, compte 467) et chiffrer la TVA indûment versée depuis la mise en place du paramétrage (réclamation possible).
- **Revoir les CGV** et les contrats types : vocabulaire « arrhes » / « acompte » cohérent avec l'intention commerciale (en B2C, sans précision, ce sont des arrhes ; avec des arrhes, le client peut annuler en les perdant — un acompte l'engage sur la totalité du prix).
- Mettre en place un **état mensuel des réservations prépayées** (date d'encaissement, date de séjour, statut) pour justifier le 4191 à la clôture et régulariser la TVA des annulations.
- Mail à Olivier : « La facture Booking sans TVA est normale : c'est à l'hôtel d'autoliquider la TVA, opération neutre pour votre trésorerie. En revanche, la taxe de séjour ne doit jamais être dans le CA : nous corrigeons avec votre éditeur. »

## 6. Références

- Code civil : art. 1590 (arrhes) ; Code de la consommation : art. L. 214-1 (sommes versées d'avance réputées arrhes).
- CGI : art. 256 et 269-2-c (prestations de services, exigibilité à l'encaissement), art. 259-1° et 283-2 (services B2B rendus par un prestataire non établi : autoliquidation), art. 279 (taux de 10 % pour l'hébergement hôtelier).
- CGCT : art. L. 2333-26 et suivants (taxe de séjour).
- Jurisprudence : CJCE, 18/07/2007, *Société thermale d'Eugénie-les-Bains*, C-277/05 ; CJUE, 23/12/2015, *Air France-KLM et Hop!-Brit Air*, C-250/14 et C-289/14 ; CJUE, 22/11/2018, *MEO*, C-295/17.
- BOFiP : TVA-BASE (indemnités et sommes versées en cas d'annulation) — position à vérifier lors de chaque mise à jour.
