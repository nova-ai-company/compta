# E15-06 — Test technique : acquisition d'une autolaveuse, plan d'amortissement et cession d'un véhicule utilitaire
**Client :** GSF Riviera SAS (filiale régionale **fictive**, siège à Nice) — service comptable | **Difficulté :** ★★☆ | **Durée estimée :** 45 min (test chronométré) | **Thèmes :** coût d'acquisition d'une immobilisation (frais inclus / exclus), amortissement linéaire prorata temporis, cession d'immobilisation (dotation complémentaire, sortie de l'actif, 675 / 775), TVA sur cession ; *pour aller plus loin :* amortissement dégressif

**Corner case :** oui — la facture d'achat mélange coût de l'immobilisation et formation (à exclure), et le projet de facture de cession du véhicule oublie la TVA

> *Cadre de formation : sociétés, documents et personnes fictifs.*

## La mise en situation

Vous passez l'entretien pour le poste d'assistante comptable de GSF Riviera SAS. Après l'échange avec la responsable RH, Laurent Vidal, chef comptable (personnage fictif), vous installe dans une petite salle avec une calculatrice, le plan comptable et trois pièces.

« Voici un test que je donne à tous les candidats. Vous avez **45 minutes**. Je ne cherche pas la vitesse : je veux voir si vous savez **ce qu'on met dans le coût d'une machine**, calculer un **amortissement** et passer une **cession** sans vous perdre dans les comptes. Écrivez vos calculs, même simples. »

Règles de GSF Riviera pour ce test (fictives) :
- exercice comptable du 01/01 au 31/12 ; pour simplifier, les **dotations sont calculées une fois par an** au 31/12 (et à la date de sortie pour un bien cédé) ;
- amortissement **linéaire** ; prorata temporis **en jours, année de 360 jours** (mois de 30 jours) à compter de la **mise en service** ;
- autolaveuses : **5 ans** ; véhicules utilitaires : **5 ans** ;
- comptes : 2154 Matériel industriel, 2182 Matériel de transport, 28154, 28182, 404 Fournisseurs d'immobilisations, 401 Fournisseurs, 44562 TVA déductible sur immobilisations, 44566 TVA déductible sur autres biens et services, 44571 TVA collectée, 462 Créances sur cessions d'immobilisations, 512 Banque, 6228 Divers (formations externes — *compte selon le plan du groupe*), 675 Valeurs comptables des éléments d'actif cédés, 775 Produits des cessions d'éléments d'actif, 6811 Dotations aux amortissements.

## Les pièces

**Pièce 1 — Facture d'achat (reçue via la plateforme agréée)**
```
PROPRETÉ ÉQUIPEMENT SUD SAS – SIREN 999 412 538 – TVA FR41999412538 – RCS Nice (fictif)
FACTURE PES-26-0311 du 10/03/2026
Client : GSF RIVIERA SAS – SIREN 999 100 206 – TVA FR12999100206
Adresse de livraison : établissement GSF Riviera de Cagnes-sur-Mer (adresse fictive)
Nature de l'opération : mixte (livraison de biens et prestations de services)
Réf. commande : BC-2026-0217

Désignation                                                        HT
Autolaveuse autoportée AL-80 (n° série AL80-26-00452)          18 500,00
Remise commerciale 5 %                                            -925,00
Transport et livraison sur site                                     350,00
Installation et raccordement de la borne de charge                  480,00
Formation de 3 agents à la conduite de l'autolaveuse               600,00
                                                    TOTAL HT    19 005,00
                                                    TVA 20 %     3 801,00
                                                    TOTAL TTC   22 806,00
Échéance : 30/04/2026 – pénalités de retard : 3 fois le taux d'intérêt légal
Indemnité forfaitaire pour frais de recouvrement : 40 €
```

**Pièce 2 — Procès-verbal de mise en service**
```
PV n° MS-CAG-2026-04 – Autolaveuse AL-80 n° série AL80-26-00452
Mise en service le 01/04/2026 sur le site Polygone Riviera (Cagnes-sur-Mer)
Signé : chef de site GSF Riviera / technicien Propreté Équipement Sud
```

**Pièce 3 — Fiche d'immobilisation et projet de facture de cession du véhicule utilitaire**
```
FICHE IMMOBILISATION n° 2182-0457
Véhicule utilitaire Fourgon 3 places – immatriculé GS-457-RV (fictif)
Date d'acquisition et de mise en service : 01/10/2023
Valeur d'origine : 28 000,00 € HT (TVA déduite à l'achat)
Mode : linéaire 5 ans
Amortissements cumulés au 31/12/2025 : 12 600,00 €
```
```
PROJET DE FACTURE (préparé par l'établissement de Nice, non encore émis)
GSF RIVIERA SAS – SIREN 999 100 206
Facture CES-2026-003 du 30/06/2026
Client : GARAGE DES BAOUS SARL – SIREN 999 587 214 – Saint-Laurent-du-Var (fictif)
Vente du véhicule utilitaire GS-457-RV en l'état                 13 500,00
« TVA non applicable – vente de véhicule d'occasion »
NET À PAYER                                                     13 500,00
Règlement par virement à réception
```
Le Garage des Baous a réglé la somme facturée par virement le **15/07/2026**.

## Travail à faire

1. **Pièce 1** : pour chaque ligne de la facture, dites si elle entre dans le **coût de l'autolaveuse** ou si c'est une **charge**, en une phrase. Calculez le coût d'entrée (montant à porter en 2154).
2. Passez l'écriture d'achat du 10/03/2026 (attention aux deux comptes de TVA déductible).
3. Établissez le **plan d'amortissement linéaire** complet de l'autolaveuse (une ligne par exercice, de 2026 à 2031) et passez la dotation au 31/12/2026.
4. **Pièce 3** : repérez l'erreur du projet de facture de cession et corrigez les montants (HT, TVA, TTC).
5. Pour la cession du 30/06/2026 : calculez la **dotation complémentaire** 2026, la **valeur nette comptable** à la date de cession et le **résultat de cession**. Passez les trois écritures (dotation, sortie de l'actif, facture de cession), puis l'encaissement du 15/07/2026.
6. Question orale : « Pourquoi la formation n'est-elle pas dans le coût de l'autolaveuse, alors que l'installation l'est ? »

**Pour aller plus loin (facultatif — si vous avez le temps) :** le 05/07/2026, GSF Riviera achète une balayeuse aspiratrice industrielle neuve à 24 000,00 € HT (TVA 20 %), durée 5 ans, amortie en **dégressif**. On retient : coefficient **1,75** pour une durée de 5 ans (*valeur à vérifier chaque année*), soit un taux de 35 % ; prorata à partir du **premier jour du mois d'acquisition** ; la première annuité, même réduite, compte pour une année (5 annuités de 2026 à 2030) ; passage au linéaire lorsque le taux linéaire calculé sur les années restantes (année en cours comprise) dépasse 35 %. Établissez le plan et la dotation 2026.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-06_corrige.md)
