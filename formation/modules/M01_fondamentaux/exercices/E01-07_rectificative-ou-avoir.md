# E01-07 — Facture rectificative ou avoir ?
**Client :** C13 — Atelier Ligne | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** facture rectificative, avoir, numérotation, taux de TVA des prestations d'architecte, TVA sur les encaissements

**Corner case :** oui — une cogérante qui veut « supprimer » une facture dans le logiciel, et une erreur de taux en faveur du client particulier

## La mise en situation

Atelier Ligne a ouvert son nouvel exercice le 01/10/2026. Le cabinet tient la comptabilité, mais la facturation est faite par les associés dans un logiciel de facturation relié au logiciel comptable. Lundi 12 octobre 2026, Camille Fabre, cogérante, vous appelle :

> « J'ai fait plusieurs bêtises sur mes factures de la semaine dernière. Un : j'ai mis le mauvais SIREN et "SARL" au lieu de "SAS" pour Promotion Saône, leur service compta me l'a renvoyée. Deux : pour les Chevalier, j'ai mis 10 % de TVA parce que c'est une rénovation… Nicolas me dit que c'est faux. Trois : Promotion Saône râle parce qu'on a rendu l'APD avec trois semaines de retard, Nicolas leur a promis une remise de 5 % sur la facture. Et quatre : le projet de la SCM des Brotteaux est abandonné, la facture DET n'a pas lieu d'être. Celle-là, je ne l'ai même pas envoyée, je peux la supprimer du logiciel ? Ce serait plus simple. »

Hélène Ferrand : « Traitez les quatre cas, avec les documents à émettre, la numérotation et les écritures. Rappel : Atelier Ligne est en TVA sur les encaissements (prestations de services, pas d'option pour les débits). Aucune de ces factures n'a été payée. »

Données : dernière facture émise : **FA-2026-0417** ; dernier avoir émis : **AV-2026-0030** (deux séries distinctes, chacune continue). Comptes utilisés par le cabinet : 706 Prestations de services ; 709 Rabais, remises et ristournes accordés ; 44574 TVA collectée en attente d'encaissement ; 411xxx comptes clients.

## Les pièces

**Facture 1**
```
ATELIER LIGNE SARL — Architectes DPLG — 17 rue Duguesclin, 69006 Lyon
SARL au capital de 10 000 € — RCS Lyon 839 222 017 — TVA FR23 839222017
Inscrite au tableau de l'Ordre des architectes Auvergne-Rhône-Alpes
Assurance décennale : Mutuelle des Architectes Français — contrat n° 2026-AL-7781

FACTURE N° FA-2026-0412                              Date : 02/10/2026
Client : PROMOTION SAÔNE SARL — SIREN 512 334 807
         45 quai Saint-Vincent, 69001 Lyon
Nature de l'opération : prestation de services
Opération : Immeuble « Les Terrasses de Saône » — marché du 14/03/2026

Phase APD (avant-projet définitif) — 100 %          HT    18 000,00 €
                                                 TVA 20 %   3 600,00 €
                                                 TTC       21 600,00 €
Échéance : 01/11/2026 — Pénalités : 3 x taux d'intérêt légal — Indemnité forfaitaire : 40 €
Pas d'escompte pour paiement anticipé.
```
*Information du client : la dénomination exacte est « PROMOTION SAÔNE SAS », SIREN 512 334 870.*

**Facture 2**
```
ATELIER LIGNE SARL — [en-tête identique]
FACTURE N° FA-2026-0413                              Date : 05/10/2026
Client : M. et Mme CHEVALIER — 8 chemin de la Croix, 69130 Écully
Nature de l'opération : prestation de services
Mission de maîtrise d'œuvre — rénovation de leur maison (construite en 1978)
Contrat d'architecte du 02/06/2026 : honoraires forfaitaires 4 500,00 € HT (phase conception)

Honoraires phase conception                         HT     4 500,00 €
                              TVA 10 % (travaux de rénovation)   450,00 €
                                                    TTC     4 950,00 €
Échéance : à réception.
```

**Facture 3**
```
ATELIER LIGNE SARL — [en-tête identique]
FACTURE N° FA-2026-0414                              Date : 06/10/2026
Client : SCM CABINET MÉDICAL DES BROTTEAUX — SIREN 448 120 556
         60 boulevard des Brotteaux, 69006 Lyon
Nature de l'opération : prestation de services
Aménagement du cabinet — phase DET (direction de l'exécution des travaux), acompte

Honoraires phase DET — 1re situation                HT     3 000,00 €
                                                 TVA 20 %     600,00 €
                                                    TTC     3 600,00 €
Échéance : 05/11/2026 — Pénalités : 3 x taux d'intérêt légal — Indemnité forfaitaire : 40 €
```
*La facture 3 a été validée dans le logiciel (numéro attribué, écriture générée dans le journal des ventes) mais n'a pas été envoyée.*

## Travail à faire

1. Pour chacun des quatre cas, indiquez le **document à émettre** (facture rectificative, avoir partiel, avoir total + nouvelle facture), son **numéro**, sa date et les **mentions particulières** qu'il doit porter.
2. Justifiez le taux de TVA applicable aux honoraires de l'architecte pour les Chevalier. Qui supporte la différence de TVA ?
3. Répondez à la question de Camille sur la « suppression » de la facture FA-2026-0414.
4. Passez les écritures comptables des documents émis.
5. Que changera la facturation électronique (émission obligatoire pour Atelier Ligne au 01/09/2027) pour ce type d'erreurs ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E01-07_corrige.md)
