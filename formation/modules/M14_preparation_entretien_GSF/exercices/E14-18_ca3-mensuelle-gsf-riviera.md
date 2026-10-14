# E14-18 — Préparer la CA3 mensuelle de GSF Riviera à partir de la balance des comptes de TVA
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) | **Difficulté :** ★★★ | **Durée estimée :** 60 min | **Thèmes :** déclaration 3310-CA3, TVA sur les encaissements, autoliquidations (sous-traitance BTP, services d'un prestataire hors UE, acquisitions intracommunautaires), opérations non imposables, TVA sur immobilisations, cadeaux, créance irrécouvrable sous le régime des encaissements, écriture de liquidation

**Corner case :** oui — une créance devenue irrécouvrable sur une prestation de services n'ouvre aucune « récupération » de TVA quand la TVA n'a jamais été exigible (régime des encaissements)

> *Cadre de formation : sociétés, montants et personnes fictifs. La numérotation et les libellés des lignes du formulaire 3310-CA3 sont donnés à titre indicatif : **à vérifier sur le formulaire en vigueur**.*

## La mise en situation

Lundi 12/10/2026. La CA3 de septembre de GSF Riviera doit être télédéclarée et payée avant l'échéance fixée par le calendrier du service des impôts (on retient le **19/10/2026**, *à vérifier*). Sophie Garnier (personnage fictif) vous confie sa préparation :

> « Je veux le brouillon de CA3, les contrôles de cohérence, et l'écriture de liquidation. Attention aux pièges : on est sur les encaissements, il y a des autoliquidations, et un collègue a mis des choses bizarres dans les comptes de TVA ce mois-ci. »

Rappels : GSF Riviera déclare la TVA sur ses prestations **à l'encaissement** (pas d'option pour les débits) ; toutes ses prestations sont au taux de 20 %. Aucun crédit de TVA antérieur à reporter.

## Les pièces

**Pièce 1 — Balance des comptes de TVA, mouvements de septembre 2026 (soldes au 30/09)**

| Compte | Intitulé | Solde au 30/09 | Commentaire du collègue |
|---|---|---|---|
| 44571 | TVA collectée (exigible) | 312 486,40 C | TVA virée de 44574 lors des encaissements de septembre |
| 44574 | TVA collectée en attente d'encaissement | 248 902,16 C | Factures émises non encaissées |
| 445711 | TVA due autoliquidée – sous-traitance BTP | 630,00 C | Sous-traitant de 2e rang, base 3 150,00 €, payé en septembre |
| 4452 | TVA due intracommunautaire / autoliquidée | 790,53 C | Abonnement SaaS CloudLedger Inc. (États-Unis) 1 572,65 € (TVA 314,53) + pièces détachées achetées en Allemagne 2 380,00 € (TVA 476,00) |
| 44562 | TVA déductible sur immobilisations | 4 218,40 D | Dont autolaveuse MN-4377 |
| 44566 | TVA déductible sur ABS | 96 412,18 D | Dont 180,00 € de TVA sur 9 coffrets cadeaux clients à 120,00 € TTC l'un |
| 445661 | TVA déductible autoliquidée – sous-traitance BTP | 630,00 D | |
| 445662 | TVA déductible intracommunautaire / autoliquidée | 790,53 D | |
| 44586 | TVA sur factures non parvenues | 3 412,00 D | « Je l'ajoute à la TVA déductible ? » |
| 44587 | TVA sur factures à établir | 5 240,00 C | |

**Pièce 2 — Autres informations**
- Encaissements de septembre (prestations) : **1 562 432,00 € HT** (TVA 312 486,40 €) — concorde avec 44571.
- Facture à Bâti Azur Construction du 30/09/2026 en **autoliquidation** (GSF Riviera sous-traitant) : **9 800,00 € HT**.
- Client « Boutique Mistral » (fictif), placé en liquidation judiciaire, clôturée pour insuffisance d'actif le 25/09/2026 : facture FR-2026-03-0144 de 2 160,00 € TTC (HT 1 800,00 € ; TVA 360,00 €) **jamais encaissée**, toujours en 411BMIS et en 44574. Le collègue propose de « récupérer les 360 € de TVA sur la ligne des régularisations de la CA3 ».
- Les coffrets cadeaux (120,00 € TTC l'un, 9 clients différents, un seul cadeau par client sur l'année) ont été comptabilisés en 6234 Cadeaux (100,00 € HT) et 44566 (20,00 €). Seuil retenu de déductibilité des cadeaux : **73 € TTC par bénéficiaire et par an** (*valeur à vérifier*).

## Travail à faire

1. Indiquez, pour chaque compte de la pièce 1, s'il alimente la CA3 de septembre et sur quelle ligne. Traitez les deux questions du collègue (44586 et Boutique Mistral) et les cadeaux.
2. Remplissez le brouillon de la CA3 de septembre (lignes des opérations, TVA brute, TVA déductible, TVA nette due).
3. Passez les écritures préalables (cadeaux, créance irrécouvrable) puis l'écriture de liquidation au 30/09/2026 et le paiement au 19/10/2026.
4. Listez les contrôles de cohérence que vous faites avant de transmettre la CA3 à Sophie Garnier.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-18_corrige.md)
