# Corrigé E14-04 — Client public : facture déposée sur Chorus Pro, paiement à 75 jours, intérêts moratoires et indemnité de 40 €

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-04](../exercices/E14-04_chorus-pro-interets-moratoires-ch-grasse.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Point de départ du délai
Dans la commande publique, le délai global de paiement court à compter de la **date de réception de la demande de paiement** par le pouvoir adjudicateur (ou de la date d'exécution des prestations si elle est postérieure). Une facture **rejetée** pour une mention obligatoire manquante n'est pas une demande de paiement recevable : le délai ne court qu'à partir du **dépôt conforme**.
Ici, l'absence du **numéro d'engagement juridique** est imputable à GSF Riviera → départ du délai le **06/07/2026** (dépôt conforme). Les prestations de juin étant achevées le 30/06, la date de réception de la facture est bien la plus tardive.
- Date limite : 06/07/2026 + 50 jours = **25/08/2026**.
- Paiement le 14/09/2026 → **20 jours de retard**.
Le « service fait » du 28/07 ne décale pas le point de départ : la constatation du service fait est un acte interne de l'acheteur, compris dans le délai global.

### Question 2 — Pourquoi rien n'a été versé automatiquement ?
Les intérêts moratoires et l'indemnité sont dus **de plein droit**, sans formalité, et l'acheteur public doit les mandater en même temps que le principal. En pratique, ils sont souvent oubliés : le créancier doit les **réclamer**, ici en déposant sur Chorus Pro une demande de paiement complémentaire (ou par courrier au comptable public), avec le calcul.

### Question 3 — TVA
Intérêts moratoires et indemnité forfaitaire **réparent un préjudice** (retard) : ils ne sont la contrepartie d'aucune prestation → **hors du champ de la TVA**. On les réclame pour leur montant brut, sans TVA, et on ne les facture pas comme une prestation.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Point de départ | dépôt conforme sur Chorus Pro | 06/07/2026 |
| Date limite | 06/07 + 50 j | 25/08/2026 |
| Jours de retard | du 25/08 au 14/09 | **20 jours** |
| Taux | 2,15 % + 8 points | 10,15 % |
| Intérêts moratoires | 55 500,00 × 10,15 % × 20 / 365 | **308,67 €** |
| Indemnité forfaitaire | forfait | **40,00 €** |
| Total à réclamer | 308,67 + 40,00 | **348,67 €** |
| Hypothèse « départ 01/07 » | limite 20/08, 25 j : 55 500,00 × 10,15 % × 25 / 365 | 385,84 € |
| TVA exigible le 14/09 | 55 500,00 × 20/120 | 9 250,00 € |

La réclamation calculée depuis le 01/07 (385,84 €) serait **rejetée** par le comptable public, avec un échange inutile : on réclame 308,67 € + 40,00 €.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 14/09/2026 | BQ | 512 | Banque | Vir. CH Grasse F FR-2026-06-0301 | 55 500,00 | |
| 14/09/2026 | BQ | 411CHGR | Client Centre hospitalier de Grasse | Vir. CH Grasse F FR-2026-06-0301 | | 55 500,00 |
| 14/09/2026 | OD | 44574 | TVA collectée en attente d'encaissement | TVA exigible encaiss. F FR-2026-06-0301 | 9 250,00 | |
| 14/09/2026 | OD | 44571 | TVA collectée | TVA exigible encaiss. F FR-2026-06-0301 | | 9 250,00 |
| 09/10/2026 | OD | 4687 | Divers – produits à recevoir | Intérêts moratoires + IF 40 € F FR-2026-06-0301 | 348,67 | |
| 09/10/2026 | OD | 763 | Revenus des autres créances – intérêts moratoires | IM 20 j à 10,15 % F FR-2026-06-0301 | | 308,67 |
| 09/10/2026 | OD | 758 | Produits divers de gestion courante – indemnités de recouvrement | IF frais de recouvrement F FR-2026-06-0301 | | 40,00 |
| 30/10/2026 | BQ | 512 | Banque | Vir. CH Grasse IM + IF F FR-2026-06-0301 | 348,67 | |
| 30/10/2026 | BQ | 4687 | Divers – produits à recevoir | Vir. CH Grasse IM + IF F FR-2026-06-0301 | | 348,67 |
| | | | | **Totaux** | **65 447,34** | **65 447,34** |

> Variante de prudence fréquente dans les groupes : ne constater les intérêts moratoires qu'à l'encaissement (D 512 / C 763 et 758). La créance étant légale et chiffrable, la constatation à la demande est défendable ; l'essentiel est d'appliquer **une méthode constante** dans tout le groupe.

## 4. Points d'attention / pièges

- **Délai applicable** : 30 jours pour l'État et les collectivités territoriales, **50 jours pour les établissements publics de santé**, 60 jours pour les entreprises publiques (*à vérifier dans le Code de la commande publique en vigueur*). Le fichier interne indiquant 60 jours était faux pour un hôpital : on vérifie la source avant de réclamer.
- **Pas de pénalités « 3 fois le taux légal »** du Code de commerce avec un acheteur public : le régime est celui de la commande publique (BCE + 8 points).
- **Pas de TVA, pas de facture « de vente »** : ne pas saisir la demande en journal des ventes avec TVA.
- **TVA sur les encaissements** : un client public qui paie à 75 jours ne coûte pas de trésorerie de TVA à GSF Riviera (TVA exigible au 14/09 seulement) ; avec une option pour les débits, la TVA de juin aurait été avancée au Trésor dès juillet.
- **Suspension du délai** : l'acheteur peut suspendre le délai une fois, par une notification motivée (pièce manquante). Aucune suspension ici, mais on la vérifie dans Chorus Pro avant tout calcul.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Contrôles à mettre en place (question 5)** :
1. Fiche client « entité publique » dans l'ERP avec **SIRET**, **code service**, obligation ou non d'un **numéro d'engagement juridique**, et blocage de l'émission si le champ est vide.
2. Rapprochement mensuel des **bons de commande publics** (EJ) avec les factures à émettre ; demande du nouvel EJ avant la fin d'un exercice budgétaire du client (les hôpitaux en émettent souvent un par an ou par trimestre).
3. Suivi hebdomadaire des **statuts Chorus Pro** (rejet, suspension, mise en paiement) : un rejet non traité, c'est un mois de trésorerie perdu.
4. Tableau de calcul automatique des intérêts moratoires sur les paiements publics reçus hors délai, et réclamation systématique (c'est un droit, et l'acheteur public y est habitué).

**Mail à Julien Roux :**
> Bonjour Julien,
> Le centre hospitalier nous doit 308,67 € d'intérêts moratoires (20 jours à 10,15 %) et 40 € d'indemnité forfaitaire. Le retard n'est que de 20 jours, et non 25 : notre premier dépôt du 01/07 a été rejeté parce que le numéro d'engagement juridique manquait, le délai ne court donc que depuis le 06/07. Je dépose la demande sur Chorus Pro aujourd'hui. Pour les prochaines factures, pouvez-vous nous transmettre chaque nouveau bon de commande de l'hôpital dès réception ?

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de la commande publique, art. L. 2192-10 et suivants et R. 2192-10 et suivants : délais de paiement, intérêts moratoires (taux BCE + 8 points), indemnité forfaitaire pour frais de recouvrement (*numéros précis à vérifier*).
- Ordonnance n° 2014-697 et textes relatifs à la facturation électronique dans la commande publique (Chorus Pro).
- CGI art. 256 : champ d'application de la TVA (indemnités hors champ).
- CGI art. 269-2-c : exigibilité à l'encaissement des prestations de services.
- PCG : comptes 4687, 763, 758.
