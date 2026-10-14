# E02-10 — Clôture du garage : doublon PDF / PA, facture au nom du gérant, LCR et livraison sans facture
**Client :** C03 — Garage Martin | **Difficulté :** ★★★ | **Durée estimée :** 50 min | **Thèmes :** réception des factures électroniques via la PA, doublons, facture adressée au gérant, compte courant d'associé, effets à payer (LCR), factures non parvenues, cut-off

**Corner case :** oui — trois en un : même facture reçue en flux PA et en PDF, pneus facturés au nom personnel de Thierry Martin, livraison du 29/09 sans facture

## La mise en situation

Garage Martin (EURL à l'IS, associé unique Thierry Martin) clôture le **30/09/2026** ; vous préparez les écritures d'inventaire du cycle achats. Thierry vous appelle :

> « Je ne comprends pas, mon fournisseur de pièces AutoDistrib me dit que je n'ai qu'une facture de 3 415,80 € en septembre, mais dans ma compta il y en a deux. Ma secrétaire dit qu'elle a saisi celle qu'elle a reçue par mail. Et autre chose : j'ai payé les pneus de la dépanneuse avec ma carte perso chez Pneus Express, ils ont mis la facture à mon nom, vous pouvez me les rembourser ? Pour Huiles & Lubrifiants, j'ai validé la LCR sur le site de la banque, et ils m'ont livré de l'huile hier, mais pas encore de facture. »

Hélène Ferrand : « Garage Martin a basculé sur sa PA de réception en août. Réglez les quatre sujets avec les écritures au 30/09, et préparez une procédure pour la secrétaire. »

Rappels : réel normal, CA3 mensuelle. Compte courant de Thierry Martin : 455TMAR. La dépanneuse (immatriculée en « VASP – dépanneuse », véhicule utilitaire) figure à l'actif. L'outil de pré-comptabilisation intègre **automatiquement** les flux reçus de la PA au journal AC.

## Les pièces

**Pièce 1 — Journal AC, extrait du compte 401AUTO (septembre 2026)**

| Date | Pièce | Origine | Libellé | Débit | Crédit |
|---|---|---|---|---|---|
| 25/09/2026 | AC-0947 | Flux PA (Factur-X, statut « Mise à disposition ») | AutoDistrib F FA-88412 pièces | | 3 415,80 |
| 26/09/2026 | AC-0952 | Saisie manuelle (PDF reçu par e-mail le 26/09) | AutoDistrib facture du 24/09 | | 3 415,80 |

Détail de la facture FA-88412 du 24/09/2026 : pièces détachées 2 846,50 € HT ; TVA 20 % 569,30 € ; TTC 3 415,80 €. AutoDistrib Rhône SAS (RCS Lyon 512 664 093, TVA FR61 512664093) est une ETI (1 100 salariés).

**Pièce 2 — Facture Pneus Express**
```
PNEUS EXPRESS SARL — 88 avenue Berthelot, 69007 Lyon
SARL au capital de 30 000 € — RCS Lyon 338 920 114 — TVA FR49 338920114

FACTURE N° PE-26-07731                             Date : 15/09/2026
Client : M. Thierry MARTIN — 14 chemin des Vignes, 69110 Sainte-Foy-lès-Lyon
Véhicule : Renault Master dépanneuse — GH-417-TM

4 pneus 225/65 R16 C            4 x 95,00 €          380,00 €
Montage + équilibrage           4 x 12,00 €           48,00 €
                                   Total HT          428,00 €
                                   TVA 20 %           85,60 €
                                   Total TTC         513,60 €
Acquittée par carte bancaire le 15/09/2026
```

**Pièce 3 — Relevé LCR à payer (banque du garage)**
```
RELEVÉ DES LCR À PAYER — édité le 22/09/2026 — Garage Martin
Tireur : HUILES & LUBRIFIANTS DU RHÔNE SAS (TVA FR01 451330876)
Réf. : facture HL-2026-0831 du 31/08/2026 — Montant : 1 932,00 € — Échéance : 10/10/2026
Bon à payer donné en ligne le 25/09/2026
```
La facture HL-2026-0831 (1 610,00 € HT ; TVA 322,00 € ; TTC 1 932,00 €) est comptabilisée au 401HUIL en août.

**Pièce 4 — Bon de livraison**
```
HUILES & LUBRIFIANTS DU RHÔNE — BL n° BLH-26-4410 du 29/09/2026
Garage Martin — 45 avenue Jean Jaurès, 69007 Lyon
Huile moteur 5W30 (fût 60 L) ............ 60 L x 6,20 € HT
Filtres à huile réf. FH-220 ............. 10 x 8,40 € HT
Facture mensuelle à suivre (émise le 31/10/2026)
```
Les produits ont été comptés dans l'inventaire des pièces et lubrifiants du 30/09/2026.

## Travail à faire

1. AutoDistrib : identifiez l'original de la facture, corrigez la comptabilité et expliquez les conséquences de l'erreur si elle n'avait pas été détectée (résultat, TVA, paiement).
2. Pneus Express : la dépense peut-elle être prise en charge par le garage, avec quelle TVA ? Que faut-il obtenir, et quelles écritures passez-vous au 30/09/2026 (hypothèse : Pneus Express émettra en octobre un avoir et une facture au nom de l'EURL) ?
3. LCR : passez les écritures de l'acceptation et de l'échéance. Comment apparaît cette dette au bilan du 30/09/2026 ?
4. Livraison du 29/09 : passez l'écriture nécessaire au 30/09/2026.
5. Rédigez une procédure courte (5 points) pour la secrétaire du garage sur la réception des factures depuis la mise en place de la PA.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E02-10_corrige.md)
