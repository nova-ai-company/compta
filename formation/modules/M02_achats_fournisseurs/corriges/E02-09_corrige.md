# Corrigé E02-09 — Clôture de la pharmacie : ristourne de fin d'année, coopération commerciale et livraison du 30 septembre

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-09](../exercices/E02-09_ristourne-a-recevoir-pharmacie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### La ristourne (question 1)
Le principe d'**indépendance des exercices** impose de rattacher à l'exercice les produits et réductions de charges **acquis** à la clôture, même si le document n'est pas encore reçu. Au 30/09/2026 :
- la période de référence du contrat (01/10/2025 – 30/09/2026) est **achevée** ;
- le palier de 400 000 € est **atteint** (412 000 €), le grossiste l'a confirmé (pièce 2) ;
- le montant est **déterminable** avec précision.

La ristourne est donc **acquise** : on constate un **avoir à recevoir** au 30/09/2026. L'attendre en novembre, « comme d'habitude », c'est minorer le résultat de l'exercice clos et le reporter sur l'exercice suivant — un décalage qui se répète chaque année, mais qui fausse chaque exercice (et pose un problème en cas de variation de la ristourne, de cession de l'officine ou de changement de taux d'IS).

> Si le palier n'avait pas été atteint de façon certaine à la clôture (période en cours, volumes incertains), on ne constaterait rien (prudence) ou seulement le palier certain.

### Coopération commerciale vs ristourne (question 3)

| | Ristourne du grossiste | Rémunération Alpina |
|---|---|---|
| Nature | **Réduction du prix** des achats (avantage financier lié au volume) | **Prix d'un service** rendu par la pharmacie (mise en avant, animations) |
| Qui émet le document ? | Le **fournisseur** (avoir) | La **pharmacie** (facture) |
| Compte | **609x** (diminution des achats) | **706** Prestations de services (chiffre d'affaires) |
| TVA | Régularisation de la TVA **déduite**, aux taux des achats (2,1 % et 10 %) | TVA **collectée** à **20 %** (prestation de services) |
| Incidence stocks | Diminue le **coût d'achat** des marchandises (et donc potentiellement la valeur du stock) | Aucune |
| À la clôture | **Avoir à recevoir** (4098) | **Facture à établir** (4181) |

La requalification d'une « remise » en coopération commerciale (ou l'inverse) est un sujet sensible : TVA (2,1 % vs 20 %), et réglementation des remises sur les médicaments remboursables (plafonds). On s'en tient à ce que prévoient les contrats **et** à la réalité des services rendus (justificatifs).

### La livraison du 30/09 (question 4)
Les produits ont été **livrés** le 30/09 et **comptés dans l'inventaire** : ils figurent dans le stock final. Si l'achat correspondant n'est pas comptabilisé, le résultat est **surévalué** de 6 240,00 € (stock final augmenté sans achat correspondant). → **Facture non parvenue** au 30/09/2026.

## 2. Calculs (détaillés, chaque montant justifié)

**Ristourne de fin d'année** : achats 412 000,00 € > 400 000 € ⇒ taux 2,5 % sur la totalité.

| Taux de TVA des achats | Base achats | Ristourne 2,5 % | TVA sur ristourne |
|---|---|---|---|
| 2,1 % | 371 000,00 € | 9 275,00 € | 9 275,00 × 2,1 % = 194,775 → **194,78 €** |
| 10 % | 41 000,00 € | 1 025,00 € | 1 025,00 × 10 % = **102,50 €** |
| **Total** | **412 000,00 €** | **10 300,00 €** | **297,28 €** |

Avoir à recevoir TTC : 10 300,00 + 297,28 = **10 597,28 €**.

**Coopération commerciale Alpina** : 4 800,00 € HT ; TVA 20 % = **960,00 €** ; TTC **5 760,00 €**.

**Livraison du 30/09** :

| Taux | HT | TVA |
|---|---|---|
| 2,1 % | 5 100,00 € | 5 100,00 × 2,1 % = 107,10 € |
| 20 % | 1 140,00 € | 1 140,00 × 20 % = 228,00 € |
| **Total** | **6 240,00 €** | **335,10 €** |

FNP TTC : **6 575,10 €**.

**Incidence sur le résultat de l'exercice clos le 30/09/2026** : + 10 300,00 (ristourne) + 4 800,00 (coopération) – 6 240,00 (FNP) = **+ 8 860,00 €** avant IS.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 4098 | RRR à obtenir et autres avoirs non encore reçus | RFA Répartition Pharma Rhône 2025-2026 (2,5 % s/ 412 000) | 10 597,28 | |
| 30/09/2026 | OD | 6097 | RRR obtenus sur achats de marchandises | RFA génériques 2,1 % (9 275,00) + 10 % (1 025,00) | | 10 300,00 |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues (avoirs à recevoir) | TVA s/ RFA : 194,78 (2,1 %) + 102,50 (10 %) | | 297,28 |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | Coopération commerciale Alpina 2025-2026 à facturer | 5 760,00 | |
| 30/09/2026 | OD | 706 | Prestations de services | Coopération commerciale Alpina 2025-2026 | | 4 800,00 |
| 30/09/2026 | OD | 44587 | TVA sur factures à établir | Coopération commerciale Alpina 2025-2026 TVA 20 % | | 960,00 |
| 30/09/2026 | OD | 607 | Achats de marchandises | FNP Répartition Pharma BL 26-0930-55871 du 30/09 | 6 240,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP BL 26-0930-55871 : 107,10 (2,1 %) + 228,00 (20 %) | 335,10 | |
| 30/09/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Répartition Pharma BL 26-0930-55871 | | 6 575,10 |
| | | | | **Totaux** | **22 932,38** | **22 932,38** |

**Question 5 — au 01/10/2026** : les trois écritures sont **extournées** (contre-passées à l'identique, sens inverse). Puis :
- à réception de la **facture** du grossiste (05/10) : saisie normale 607 / 44566 / 401 — l'extourne et la facture se compensent en 607 ;
- à l'émission de la **facture Alpina** (octobre) : 411 / 706 / 44571 — compensée par l'extourne ;
- à réception de l'**avoir** de ristourne (novembre) : 401 / 6097 / 44566 — compensé par l'extourne.
Si les montants définitifs diffèrent des estimations, l'écart affecte l'exercice 2026-2027 (changement d'estimation).

> Note sur 44586 : ce compte sert aux FNP (débit) ; on l'utilise aussi au crédit pour la TVA des avoirs à recevoir — le solde du compte est alors net. Certains dossiers préfèrent un sous-compte distinct (par exemple 445861 « TVA sur avoirs à recevoir ») pour la lisibilité : c'est recommandé.

## 4. Points d'attention / pièges

- **« Comme d'habitude »** : vérifier si l'exercice précédent avait la même omission. Si oui, l'exercice 2025-2026 supporte l'avoir de novembre 2025 (ristourne 2024-2025) **et** la ristourne 2025-2026 : le résultat de cet exercice-ci est « gonflé » d'une ristourne en plus — à expliquer au Dr Petit et à documenter (correction d'erreur de l'exercice antérieur selon le règlement ANC 2022-06, à arbitrer avec Hélène Ferrand selon le caractère significatif).
- **Ventilation par taux** : l'avoir de ristourne régularise la TVA **aux taux des achats** (2,1 % et 10 %), pas à 20 %.
- **Coopération commerciale = prestation à 20 %** : ne pas la traiter comme une remise (TVA différente, compte différent) ; elle doit correspondre à des **services réels** et justifiés (photos, plannings), sinon risque de requalification.
- **FNP et inventaire** : le test « les produits sont-ils dans le stock ? » est le meilleur contrôle de cut-off. Une livraison du 30 au soir comptée dans le stock appelle **toujours** sa FNP.
- **Plafonds réglementaires des remises** sur les médicaments remboursables (génériques, princeps) : vérifier que le cumul remises sur facture + ristourne respecte le plafond en vigueur (taux à vérifier) — sujet de conformité pour la pharmacie et pour le grossiste.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — incidence sur le stock.** Le coût d'acquisition des stocks s'entend **net des rabais, remises et ristournes** obtenus. Une ristourne de 2,5 % sur les génériques réduit le coût des génériques encore en stock au 30/09. Si le stock de génériques à la clôture représente, par exemple, 60 000 € au prix facturé, le coût net serait inférieur d'environ 2,5 % × 60 000 = 1 500 €. Ce montant n'est pas négligeable : selon le caractère significatif et la permanence de la méthode suivie les années précédentes, on valorise le stock de génériques net de la ristourne estimée (méthode la plus correcte) — point à documenter et à arbitrer avec Hélène Ferrand.

**Message au Dr Petit :**

> Bonjour Docteur,
>
> Pour la clôture au 30/09 :
> - **Remise de fin d'année** : elle est acquise au 30/09 (vous avez dépassé 400 000 € d'achats de génériques), elle doit donc être rattachée à l'exercice qui se termine, même si l'avoir n'arrive qu'en novembre : 10 300 € HT ;
> - **Laboratoires Alpina** : ce n'est pas une remise mais la rémunération d'un service que vous leur rendez ; nous constatons la facture à établir (4 800 € HT + TVA 20 %). Merci de l'émettre en octobre avec les justificatifs (photos, planning des animations) ;
> - **Livraison du 30/09** : comme les produits sont dans votre inventaire, nous enregistrons l'achat dès maintenant (6 240 € HT).
>
> Ces trois points améliorent le résultat de l'exercice d'environ 8 860 € avant impôt. Nous vérifions aussi le traitement de l'an dernier.

**Documentation** : contrat grossiste et relevé du portail (pièce justificative de l'avoir à recevoir), contrat Alpina et justificatifs des services, BL du 30/09 ; feuille de cut-off « achats » listant toutes les FNP et avoirs à recevoir ; note sur la distinction remise / coopération commerciale.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce art. L. 123-21 et PCG : rattachement des produits et charges à l'exercice (indépendance des exercices).
- PCG : comptes 4098 « RRR à obtenir et autres avoirs non encore reçus », 408, 4181, 44586, 44587, 6097, 706 ; coût d'acquisition des stocks net des RRR.
- Règlement ANC 2022-06 : changements d'estimation et corrections d'erreurs.
- CGI art. 272 : régularisation de la TVA en cas de réduction de prix ; CGI art. 278 et suivants : taux applicables aux médicaments et à la parapharmacie.
- Code de commerce art. L. 441-3 et suivants : conventions et coopération commerciale ; Code de la sécurité sociale : plafonnement des remises sur les médicaments remboursables (taux à vérifier).
