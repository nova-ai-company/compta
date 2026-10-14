# E03-06 — Vente d'un véhicule d'occasion et carte grise en débours
**Client :** C03 — Garage Martin EURL | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** vente de VO sous le régime de la marge, mentions de facture, frais accessoires, débours (art. 267-II-2° CGI), compte 467, frais de remise en état

**Corner case :** oui — facture faisant apparaître de la TVA sur la totalité du prix d'un VO acheté à un particulier et taxes de carte grise soumises à TVA

## La mise en situation

Garage Martin clôture au **30/09/2026** et la révision a commencé. En pointant le journal des ventes de septembre, vous tombez sur la facture d'un SUV d'occasion. Thierry Martin, interrogé, répond :

> « Celle-là, c'est mon nouveau stagiaire qui l'a faite sur le modèle de facture atelier. Le client a payé, il est content, c'est l'essentiel non ? Pour les cartes grises, je fais comme d'habitude, je paie l'ANTS avec ma carte pro et je refacture. »

Le garage est **habilité SIV** (système d'immatriculation des véhicules) et fait signer à chaque acheteur un **mandat d'immatriculation** (formulaire officiel). Le dossier contient le mandat signé de M. Faure.

## Les pièces

### Pièce 1 — Livre de police (extrait)

| N° | Date d'achat | Véhicule | Immatriculation | Vendeur | Prix d'achat | Justificatif |
|---|---|---|---|---|---|---|
| VO-26-041 | 02/07/2026 | SUV diesel, 1re mise en circulation 03/2021, 68 400 km, 7 CV | FG-218-KL | M. Henri Lacroix, particulier, Villeurbanne | 14 500,00 | Certificat de cession, copie CNI, carte grise barrée |

### Pièce 2 — Facture de pièces pour remise en état

```
AUTO-PIÈCES RHÔNE SAS – SIREN 507 220 413 – facture n° AP-77810 du 28/07/2026
Client : Garage Martin – Plaquettes, disques, kit distribution pour VO FG-218-KL
Total HT 620,00 – TVA 20 % 124,00 – TTC 744,00 – payée à 30 jours
```

### Pièce 3 — Facture de vente établie par le stagiaire

```
GARAGE MARTIN EURL – 45 avenue Jean Jaurès – 69007 Lyon
SIREN 824 112 309 – TVA FR 70 824112309 – Capital 15 000 €

FACTURE N° V-2026-0093                                   Date : 18/09/2026
Client : M. Stéphane FAURE – 11 rue Sala – 69002 Lyon

Véhicule d'occasion SUV diesel FG-218-KL (68 400 km)    18 900,00 TTC   dont TVA 20 % 3 150,00
Frais de mise à la route (préparation, contrôle, plein)     290,00 TTC   dont TVA 20 %    48,33
Carte grise (taxes Y1 à Y5)                                 314,76 TTC   dont TVA 20 %    52,46
Frais de démarche carte grise                                36,00 TTC   dont TVA 20 %     6,00
TOTAL TTC                                                19 540,76      dont TVA      3 256,79
Réglé par virement le 18/09/2026
```

### Pièce 4 — Récapitulatif ANTS de la demande d'immatriculation (payée le 16/09/2026 par la carte bancaire professionnelle du garage)

| Code | Taxe | Montant |
|---|---|---|
| Y1 | Taxe régionale : 7 CV × 43,00 € (tarif régional indicatif, *valeur à vérifier*) | 301,00 |
| Y4 | Taxe fixe | 11,00 |
| Y5 | Redevance d'acheminement | 2,76 |
| Y6 | **Total** | **314,76** |

### Pièce 5 — Écriture passée en septembre (journal VT)

| Compte | Libellé | Débit | Crédit |
|---|---|---|---|
| 411 FAURE | V-2026-0093 | 19 540,76 | |
| 707 | V-2026-0093 | | 16 283,97 |
| 44571 | V-2026-0093 | | 3 256,79 |

## Travail à faire

1. Le véhicule relève-t-il du régime de la TVA sur la marge ? Justifiez. Quelles sont les mentions obligatoires d'une facture sous ce régime ?
2. Calculez la marge imposable et la TVA due sur cette vente. Les pièces de remise en état (pièce 2) entrent-elles dans le calcul ? Les frais de mise à la route ?
3. Les taxes de carte grise remplissent-elles les conditions des débours ? Et les frais de démarche ?
4. Rédigez le corps de la facture correcte et indiquez la procédure pour remplacer la facture V-2026-0093.
5. Passez les écritures correctes (achat, pièces, paiement ANTS, vente, encaissement) et l'écriture de correction de la pièce 5.
6. Quelle est l'incidence de l'erreur sur la TVA de septembre ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E03-06_corrige.md)
