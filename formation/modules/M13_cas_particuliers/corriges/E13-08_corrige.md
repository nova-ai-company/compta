# Corrigé E13-08 — Hôtel Belle Vue : taxe de séjour mal paramétrée et arrhes à la clôture du 31/10

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E13-08](../exercices/E13-08_hotel-belle-vue-taxe-sejour-arrhes.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Question 1 — Taxe de séjour.** L'hôtelier est un **collecteur** : il perçoit la taxe auprès des clients **pour le compte de la collectivité** et la lui reverse (CGCT art. L. 2333-29 et suivants). Ce n'est ni sa recette, ni le prix de sa prestation → **compte de tiers**, **hors base de TVA**. Le night auditor a tort : « tout est sur la facture » ne veut pas dire « tout est chiffre d'affaires ». Conséquences de l'erreur : CA surévalué de 4 100 € et **TVA collectée indûment** de 410 € (qui, en l'état, serait reversée au Trésor alors que la collectivité attend 4 510 €).

Contrôle de cohérence : 1 640 nuitées taxables × 2,75 € = **4 510,00 €** ✓ (le registre et la facturation concordent ; seul le paramétrage comptable est faux).

**Question 2 — Plateformes.** Les plateformes intermédiaires de paiement sont tenues de collecter la taxe de séjour pour le compte des loueurs **non professionnels** ; pour les hébergeurs professionnels comme un hôtel, c'est l'**hôtel** qui collecte, sauf si la plateforme a été habilitée à le faire pour lui (*modalités à vérifier*). Contrôlez les relevés : si une plateforme a collecté pour certaines réservations prépayées, ne pas la recollecter ni la reverser deux fois.

**Question 3 — Arrhes et acomptes.**
- **Juridiquement** (C. consom. art. L. 214-1) : sauf stipulation contraire, les sommes versées d'avance sont des **arrhes** ; chaque partie peut se dédire : le client en perdant les arrhes, le professionnel en **restituant le double**. Un **acompte** engage ferme : le client doit le solde. Les CGV de l'hôtel parlent bien d'arrhes.
- **En TVA**, la distinction juridique ne commande pas tout : une somme encaissée d'avance pour une **prestation déterminée** (chambre, dates) constitue un **acompte au sens fiscal** → TVA **exigible à l'encaissement** (CGI art. 269, 2-c), au taux de la prestation (10 %). C'est la pratique de l'hôtel, conforme.
- **Arrhes conservées après annulation par le client (R4)** : l'administration, tirant les conséquences de la jurisprudence européenne (CJUE *Air France-KLM*, 23/12/2015 ; *MEO*, 22/11/2018), considère que les sommes conservées par le prestataire lorsque le client renonce à la prestation sont la **contrepartie du droit** de bénéficier de la prestation → **TVA maintenue**, pas de régularisation (*position à vérifier au BOFiP — elle a évolué*). Comptablement : produit de l'exercice de l'**annulation** (25/09/2026, exercice clos le 31/10/2026), en 706 (contrepartie de la prestation réservée).
- **Annulation par l'hôtel (R5)** : la prestation n'aura jamais lieu → la restitution des 300 € **annule l'acompte** : la TVA collectée de 27,27 € est **récupérable** (régularisation). Les 300 € supplémentaires (le « double ») sont une **indemnité** de dédit : **hors champ de la TVA**, **charge** de l'hôtel.

**Séjour à cheval (R6).** Le groupe a passé 2 nuits sur 3 avant la clôture. La prestation des nuits du 30 et du 31/10 est **réalisée** : produit de l'exercice 2025/2026 → **facture à établir** (le PMS ne facture qu'au départ). Les arrhes de 900 € restent en 4191 jusqu'à la facture du 02/11. La TVA de la facture à établir n'est pas encore exigible (prestation de services : exigible à l'encaissement ; le solde sera encaissé le 02/11) → 44587.

**R1 et R2** : séjours futurs → les arrhes restent en **4191** (dette envers le client). Aucune écriture.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Taxe de séjour d'octobre | 1 640 × 2,75 | 4 510,00 € |
| Comptabilisée à tort en 706 / 44571 | 4 510,00 / 1,10 ; 4 510,00 − 4 100,00 | 4 100,00 € / 410,00 € |
| R4 – arrhes conservées (HT) | 240,00 / 1,10 | 218,18 € (TVA 21,82 € déjà collectée) |
| R5 – arrhes restituées (HT / TVA) | 300,00 / 1,10 | 272,73 € / 27,27 € |
| R5 – indemnité (double) | | 300,00 € |
| R6 – nuits réalisées au 31/10 | 2 × 990,00 TTC | 1 980,00 € TTC |
| R6 – HT / TVA | 1 980,00 / 1,10 | 1 800,00 € / 180,00 € |

**Solde du 4191 au 31/10/2026** (question 5)

| Réf. | Séjour | Solde HT |
|---|---|---|
| R1 | 12-14/11/2026 | 1 800,00 € |
| R2 | 19-20/06/2027 | 2 272,73 € |
| R6 | arrhes à imputer sur la facture du 02/11 | 818,18 € |
| **Total** | | **4 890,91 €** |

(soit 5 380,00 € TTC encaissés d'avance, dont 489,09 € de TVA déjà déclarée).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD | 706100 | Prestations de services – hébergement | Taxe de séjour octobre déversée à tort en CA | 4 100,00 | |
| 31/10/2026 | OD | 44571 | TVA collectée | Taxe de séjour octobre – TVA indue | 410,00 | |
| 31/10/2026 | OD | 467TS | Collectivité – taxe de séjour collectée | Taxe de séjour octobre 1 640 nuitées × 2,75 € | | 4 510,00 |
| 31/10/2026 | OD | 4191 | Clients – arrhes reçues | R4 Laurent – arrhes conservées (annulation 25/09) | 218,18 | |
| 31/10/2026 | OD | 706100 | Prestations de services – hébergement | R4 Laurent – arrhes conservées | | 218,18 |
| 23/10/2026 | BQ | 4191 | Clients – arrhes reçues | R5 Novak – restitution des arrhes | 272,73 | |
| 23/10/2026 | BQ | 44571 | TVA collectée | R5 Novak – régularisation TVA sur arrhes restituées | 27,27 | |
| 23/10/2026 | BQ | 658 | Charges diverses de gestion courante (indemnités) | R5 Novak – indemnité de dédit (double des arrhes) | 300,00 | |
| 23/10/2026 | BQ | 512 | Banque | R5 Novak – virement du 23/10 | | 600,00 |
| 31/10/2026 | OD | 4181 | Clients – factures à établir | R6 Club Rando – nuits des 30 et 31/10 | 1 980,00 | |
| 31/10/2026 | OD | 706100 | Prestations de services – hébergement | R6 Club Rando – nuits des 30 et 31/10 | | 1 800,00 |
| 31/10/2026 | OD | 44587 | TVA sur factures à établir | R6 Club Rando – nuits des 30 et 31/10 | | 180,00 |
| | | | | **Totaux** | **7 308,18** | **7 308,18** |

*658 : subdivision selon la nomenclature 2025 du PCG (indemnités versées). L'écriture R6 est extournée le 01/11/2026, puis la facture du 02/11 est comptabilisée normalement (avec imputation des arrhes de R6).*

## 4. Points d'attention / pièges

- **Taxe de séjour en CA** : double erreur (CA et TVA). Après une mise à jour du PMS, contrôlez **toujours** la table de correspondance « familles de produits → comptes / codes TVA ».
- **Taxe de séjour : responsabilité de l'hôtel** : il est redevable des sommes qu'il aurait dû collecter (la taxe est due sur les nuitées, même s'il a oublié de la facturer). Rapprochez chaque mois **registre du logement / taxe facturée / compte 467TS / reversements**.
- **Arrhes ≠ produit à l'encaissement** : elles restent en 4191 jusqu'à la prestation ou l'annulation. Un 4191 qui contient des arrhes de séjours **passés** est le signe d'annulations ou d'imputations non traitées (R4, R5).
- **Annulation par le client vs par l'hôtel** : TVA maintenue dans le premier cas (position actuelle), régularisée dans le second ; le « double » est une indemnité hors champ.
- **Séjour à cheval** : ne pas attendre la facture du 02/11 ; les nuits du 30 et 31/10 appartiennent à l'exercice clos (séparation des exercices). Les nuitées de ce groupe entrent aussi dans le registre de la taxe de séjour d'octobre.
- **No-shows** (client qui ne vient pas sans annuler) : même logique que les arrhes conservées.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 1 (suite) et 6 — Déclarations :**
- **Taxe de séjour** : les 4 510 € d'octobre seront reversés avec ceux de novembre et décembre au plus tard le **20/01/2027**, avec l'état récapitulatif (nuitées, tarif, exonérations) prévu par la délibération ; le compte 467TS est soldé au reversement (D 467TS / C 512).
- **CA3 d'octobre 2026** : TVA collectée diminuée de 410,00 € (taxe de séjour) et de 27,27 € (arrhes restituées à M. Novak) ; la TVA de la facture à établir R6 (180,00 €) n'est pas déclarée en octobre (exigible à l'encaissement du 02/11). Le CA hébergement déclaré exclut la taxe de séjour.

**Message à Olivier Garnier :**

> Bonjour Olivier,
>
> 1. **Taxe de séjour** : votre night auditor a raison sur un point (elle figure bien sur la facture du client), mais pas sur l'essentiel : elle n'est **pas** à vous. Le logiciel la traite désormais comme de l'hébergement avec de la TVA ; nous avons corrigé octobre (4 510 € à reverser à la collectivité, 410 € de TVA en moins à payer). Merci de demander à l'éditeur du PMS de rétablir le paramétrage (famille « taxe de séjour » : compte 467, sans TVA) **avant le 1er novembre**.
> 2. **Arrhes** : trois cas réglés à la clôture : Mme Laurent (arrhes acquises à l'hôtel), M. Novak (le double que vous lui avez versé est une charge, la TVA sur ses arrhes est récupérée), et le Club Rando (les deux premières nuits sont comptées dans votre chiffre d'affaires d'octobre).
> 3. À l'avenir, chaque fin de mois, la réception pourrait nous transmettre la liste des arrhes avec la date du séjour et le statut (réalisé / annulé client / annulé hôtel).

**Documentation** : export du registre du logement d'octobre, extrait de la délibération en vigueur, CGV, tableau de suivi des arrhes au 31/10 (justificatif du solde 4191), preuve du virement Novak, rapprochement taxe de séjour annuelle (collectée / reversée).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code général des collectivités territoriales : art. L. 2333-26 et suivants (taxe de séjour : assiette, tarifs, exonérations, collecte par les logeurs et plateformes, reversement), et dispositions relatives à la taxe additionnelle départementale.
- Code de la consommation : art. L. 214-1 (arrhes, dédit, restitution du double).
- CGI art. 269, 2-c (exigibilité à l'encaissement des prestations de services), art. 279-a (taux de 10 % pour l'hébergement), art. 267 (base d'imposition : exclusion des sommes perçues pour le compte de tiers — débours).
- CJUE 23/12/2015, *Air France-KLM et Hop!-Brit Air*, aff. C-250/14 et C-289/14 ; CJUE 22/11/2018, *MEO*, aff. C-295/17 ; BOFiP BOI-TVA-BASE-10-10-10 (sommes conservées en cas d'annulation — à vérifier dans sa version en vigueur).
- PCG : comptes 4191, 4181, 44587, 467 ; séparation des exercices.
