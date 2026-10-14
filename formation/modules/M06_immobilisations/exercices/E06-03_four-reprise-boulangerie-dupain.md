# E06-03 — Le nouveau four à sole et la reprise de l'ancien
**Client :** C01 — Boulangerie Dupain SARL | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** coût d'acquisition (frais accessoires inclus / exclus), acompte sur immobilisation (238), reprise d'un bien usagé (cession + TVA), sortie d'actif, prorata, extension de garantie, option dégressif

**Corner case :** oui — une reprise « déduite » sur la facture du fournisseur, qui masque une cession taxable.

## La mise en situation

Lundi 5 octobre 2026, 14 h 30 (Marc Dupain ne répond pas le matin). Dans la boîte à chaussures de septembre, vous trouvez la facture du nouveau four à sole. Le four ventilé, financé en crédit-bail depuis 2024, n'est pas concerné : c'est l'**ancien four à sole**, acheté en 2019, qui a été remplacé.

Au téléphone, Marc vous explique :

> « Ils ont livré le 28 septembre, installé le 29 et 30, on cuit dedans depuis le 1er octobre. Ils m'ont repris le vieux four 2 400 €, c'est déduit sur la facture. J'avais versé un acompte en juin. Et la garantie trois ans, je l'ai prise, on ne sait jamais. »

Le stagiaire du cabinet a préparé une proposition de saisie, que vous devez contrôler avant validation.

## Les pièces

**Pièce 1 — Facture du fournisseur** (reçue en PDF par e-mail)

```
THERMO-FOURNIL SAS — Équipements de boulangerie-pâtisserie
ZI Les Ruires, 38070 Saint-Quentin-Fallavier — SAS au capital de 300 000 €
SIREN 448 902 337 — RCS Vienne — TVA FR 70 448 902 337

FACTURE N° TF-26-1187                                          Date : 28/09/2026
Client : BOULANGERIE DUPAIN SARL — SIREN 912 345 001
         12 rue de la Charité, 69002 Lyon (adresse de livraison identique)
Nature de l'opération : mixte (livraison de biens et prestations de services)
Bon de commande BC-0614 du 13/06/2026

Réf.       Désignation                                              Qté    PU HT       Total HT
FS-5E      Four à sole électrique 5 étages, 10 m², n° série 26-4471   1   41 500,00    41 500,00
CP-20      Chambre de pousse contrôlée 20 chariots                    1    6 200,00     6 200,00
LIV        Livraison et manutention (grue)                            1      650,00       650,00
INST       Installation, raccordement électrique et hotte             1    1 400,00     1 400,00
DEM        Démontage et évacuation de l'ancien four                   1      750,00       750,00
FORM       Formation des boulangers (1 journée sur site)              1      480,00       480,00
GAR3       Extension de garantie 3 ans (01/10/2026 - 30/09/2029)      1    1 140,00     1 140,00
                                                                          Sous-total  52 120,00
REP        Reprise ancien four à sole (Bongrand 4 étages, 2019)       1   -2 400,00    -2 400,00
                                                                        TOTAL HT     49 720,00
                                                                        TVA 20 %      9 944,00
                                                                        TOTAL TTC    59 664,00
                                               Acompte reçu le 13/06/2026         - 15 000,00
                                                                        NET À PAYER  44 664,00
Échéance : 15/10/2026 par virement. Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €. Pas d'escompte pour paiement anticipé.
```

**Pièce 2 — Relevé bancaire de juin (extrait)**

```
13/06/2026   VIR SEPA THERMO-FOURNIL ACOMPTE BC-0614              débit 15 000,00
```
(L'acompte a été saisi au débit du compte 401 Thermo-Fournil. Aucune facture d'acompte n'a été émise.)

**Pièce 3 — Fiche d'immobilisation de l'ancien four**

```
N° 2019-03 — Four à sole Bongrand 4 étages — compte 2154
Mise en service : 01/07/2019 — Valeur d'origine : 32 000,00 € HT — Linéaire 10 ans
Amortissements cumulés au 31/12/2025 : 20 800,00 €
```

**Pièce 4 — Proposition de saisie du stagiaire**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2154 Four à sole | 49 720,00 | |
| 44562 TVA sur immobilisations | 9 944,00 | |
| 404 Thermo-Fournil | | 59 664,00 |

Commentaire du stagiaire : « Amortissement 10 ans à partir du 28/09. L'ancien four est amorti à 65 %, je n'y touche pas. »

**Pièce 5 — Paramètres**
- Durées d'utilisation retenues : four 10 ans ; chambre de pousse 8 ans. Convention : année de 360 jours.
- La société est à l'IS (taux réduit de 15 % sur son résultat) et au régime simplifié de TVA.

## Travail à faire

1. Analysez chaque ligne de la facture : coût de l'immobilisation ou charge ? Déterminez le coût d'entrée du four et celui de la chambre de pousse.
2. Analysez la ligne « Reprise » : quelle est la réalité juridique et fiscale de l'opération ? Quelles pièces faut-il ?
3. Traitez l'ancien four jusqu'à sa sortie et calculez le résultat de cession.
4. Passez toutes les écritures de 2026 (acompte, facture, reprise, sortie, règlement, inventaire du 31/12/2026).
5. Marc demande s'il peut « amortir plus vite » le nouveau matériel. Calculez la dotation 2026 en dégressif et donnez votre avis.
6. Listez les erreurs du stagiaire.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E06-03_corrige.md)
