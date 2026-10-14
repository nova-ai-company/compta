# E03-04 — Le relevé de reversement de la marketplace
**Client :** C09 — Mode & Co SARL | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** ventes via marketplace, comptabilisation au brut, commissions, retours, frais de port refacturés, réserve de sécurité, rapprochement du compte de tiers plateforme, ventes à distance UE

**Corner case :** oui — la marketplace applique la TVA française à des ventes livrées en Belgique alors que Mode & Co a dépassé le seuil des ventes à distance

## La mise en situation

Inès Moreau, gérante de Mode & Co, vous transfère le relevé mensuel de la marketplace **Vestali** avec ce commentaire :

> Bonjour ! Comme d'habitude, j'ai reçu 13 836,64 € sur le compte le 5 octobre, c'est ça notre CA de septembre sur Vestali non ? L'ancien comptable passait juste le virement en ventes. Bises, Inès

Hélène Ferrand a noté sur le dossier : *« Attention, Mode & Co a franchi le seuil de 10 000 € de ventes à distance UE le 08/07/2026 (voir dossier OSS). Depuis cette date, les ventes livrées à des particuliers dans un autre État membre sont taxables dans le pays de destination. Vérifiez si Vestali en tient compte. »*

## Les pièces

### Pièce 1 — Relevé de reversement Vestali

```
VESTALI SAS – Place de marché en ligne
45 rue de Turbigo – 75003 Paris – SIREN 893 410 562 – TVA FR 52 893410562

RELEVÉ DE REVERSEMENT VENDEUR N° RV-2026-09-04471
Vendeur : MODE & CO SARL – ID vendeur 77120 – SIREN 851 777 890
Période : 01/09/2026 – 30/09/2026        Date de versement : 05/10/2026

A. VENTES (montants TTC payés par les acheteurs)
   Commandes livrées en France (212 commandes)                   17 160,00
   Commandes livrées en Belgique (14 commandes) – TVA FR 20 %     1 320,00
   Sous-total articles                                           18 480,00
   Frais de port facturés aux acheteurs (France)                    672,00
   TOTAL ENCAISSÉ POUR VOTRE COMPTE                              19 152,00

B. REMBOURSEMENTS ACHETEURS (retours acceptés – France)          – 2 160,00

C. FRAIS VESTALI (voir facture FV-2026-09-77120)
   Commission 15 % sur total encaissé (19 152,00) HT              2 872,80
   TVA 20 %                                                         574,56
   Commission TTC                                               – 3 447,36
   Remboursement de commission sur retours (15 % × 2 160,00) HT    324,00
   TVA 20 %                                                          64,80
   Remboursement TTC                                              + 388,80
   Abonnement « Vendeur Pro » septembre HT 39,00 + TVA 7,80       – 46,80

D. RÉSERVE DE SÉCURITÉ
   Constitution réserve septembre                                  – 500,00
   Libération réserve d'août                                       + 450,00

NET VERSÉ LE 05/10/2026                                          13 836,64
```

### Pièce 2 — Paramétrage fiscal de la boutique Vestali (capture d'écran, extrait)

```
Pays d'expédition : France   |   Taux de TVA appliqué à toutes les commandes : 20 %
Option « TVA du pays de destination (OSS) » : désactivée
```

### Pièce 3 — Information sur les taux
Taux normal belge applicable aux vêtements : **21 %**. Les prix affichés aux acheteurs sont des prix TTC identiques quel que soit le pays de livraison.

## Travail à faire

1. Expliquez à Inès pourquoi le virement de 13 836,64 € n'est pas son chiffre d'affaires de septembre. Quel est le CA HT réel du mois sur Vestali ?
2. Traitez la TVA des 14 commandes livrées en Belgique. Quelle est la TVA belge due ? Quelles conséquences pour la marge de Mode & Co et pour le paramétrage ?
3. Passez les écritures du relevé (période de septembre, versement du 05/10) en utilisant un compte de tiers dédié à la plateforme.
4. Contrôlez que le compte de tiers Vestali est soldé après le versement (hors réserve) et indiquez le solde du compte de réserve.
5. Listez les contrôles mensuels à mettre en place sur ce flux.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E03-04_corrige.md)
