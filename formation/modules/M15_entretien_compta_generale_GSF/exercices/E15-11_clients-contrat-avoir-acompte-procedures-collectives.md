# E15-11 — Test technique « clients » : facture mensuelle, avoir, acompte, client en difficulté et pénalités de retard
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Nice | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** facturation d'un contrat de nettoyage, avoir pour prestation non réalisée, acompte reçu, délais de paiement, client en redressement judiciaire (416, dépréciation sur le HT), créance irrécouvrable (654) et récupération de la TVA, pénalités de retard et indemnité forfaitaire de 40 €

**Corner case :** oui — la TVA d'une créance douteuse n'est **pas** dépréciée et ne se récupère **qu'au moment où la créance devient définitivement irrécouvrable**

> *Cadre de formation : le groupe GSF est réel, mais **GSF Riviera SAS, les clients, les personnes et tous les montants sont fictifs**.*

## La mise en situation

Vous passez l'entretien pour le poste d'assistante comptable. Après l'échange avec la RH, Laurent Vidal, chef comptable (personnage fictif), vous installe dans une petite salle avec un PCG papier et une calculatrice :

> « On va faire un petit test sur la partie clients, c'est 45 minutes. Je ne cherche pas la perfection, je veux voir **comment vous raisonnez** : pour chaque écriture, dites-moi pourquoi vous débitez ou créditez tel compte. Une précision : pour ce test, GSF Riviera a **opté pour le paiement de la TVA d'après les débits** (la mention figure sur ses factures), donc la TVA collectée est due dès la facture, en 44571. »

Plan de comptes simplifié : 411 (un sous-compte par client), 416 Clients douteux ou litigieux, 4191 Clients – avances et acomptes reçus, 44571 TVA collectée, 491 Dépréciation des comptes clients, 512 Banque, 654 Pertes sur créances irrécouvrables, 6817 Dotations aux dépréciations des actifs circulants, 7817 Reprises sur dépréciations des actifs circulants, 706 Prestations de services, 758 Produits divers de gestion courante, 763 Revenus des autres créances.

## Les pièces

**Pièce 1 — Facture mensuelle du contrat de nettoyage**

```
GSF RIVIERA SAS — Établissement de Nice                 FACTURE N° F-2026-10-0215
SIREN 999 100 206 — TVA FR 48 999100206                  Date : 31/10/2026
Option pour le paiement de la TVA d'après les débits

Client : Hôtel Baie des Anges SAS — Promenade des Anglais, 06000 Nice
SIREN client : 512 348 907
Nature de l'opération : prestation de services

Contrat n° CN-2024-031 — Nettoyage des parties communes et des chambres
Forfait mensuel octobre 2026 ..................................... 8 450,00 € HT
TVA 20 % .......................................................... 1 690,00 €
Total TTC ......................................................... 10 140,00 €

Conditions de paiement : 60 jours fin de mois
Pénalités de retard : taux BCE + 10 points — indemnité forfaitaire pour frais de recouvrement : 40 €
```

**Pièce 2 — Fiche d'intervention et avoir**

> Fiche du chef d'équipe : « Vitrerie des 14/10 et 21/10 non réalisée (nacelle en panne). 2 passages × 180,00 € HT à déduire. »

```
AVOIR N° A-2026-10-0031 du 31/10/2026 — Hôtel Baie des Anges SAS (SIREN 512 348 907)
Réf. facture F-2026-10-0215 — Vitrerie non réalisée les 14/10 et 21/10 (2 × 180,00)
Montant HT ....... 360,00 € — TVA 20 % ....... 72,00 € — Total TTC ....... 432,00 €
```

**Pièce 3 — Acompte reçu puis facture finale (prestation ponctuelle)**

- Devis accepté par la SELARL Dentaire Masséna (SIREN 834 562 019) : remise en état d'un cabinet après travaux, **6 000,00 € HT**, acompte de **30 %** à la commande.
- Relevé bancaire du 12/10/2026 : « VIR SELARL DENTAIRE MASSENA ACOMPTE DEVIS D-26-118 » **+ 2 160,00 €**.
- Facture F-2026-10-0342 du 28/10/2026 : 6 000,00 € HT + TVA 1 200,00 € = 7 200,00 € TTC ; « acompte reçu le 12/10 : − 2 160,00 € » ; **net à payer : 5 040,00 €**.

**Pièce 4 — Jugement d'ouverture d'un redressement judiciaire**

```
Annonce BODACC — Restaurant Le Galet SARL (SIREN 798 214 336), Nice
Jugement du 07/10/2026 : ouverture d'une procédure de redressement judiciaire.
Mandataire judiciaire : Me Dalmasso (fictif). Les créanciers doivent déclarer leurs
créances dans un délai de deux mois à compter de la publication au BODACC.
```

Factures impayées de Restaurant Le Galet au 411GAL : 4 320,00 € TTC (soit 3 600,00 € HT + 720,00 € de TVA). Après échange avec le mandataire, le chef comptable estime le risque de perte à **60 %**.

**Pièce 5 — Clôture d'une liquidation judiciaire**

> Courrier du liquidateur du 20/10/2026 : « La liquidation judiciaire de la société Boulangerie Les Arcades SAS (SIREN 851 907 243) a été clôturée pour insuffisance d'actif. Aucun dividende ne sera versé aux créanciers chirographaires. »

Situation dans les comptes : créance au 416ARC de **1 920,00 € TTC** (1 600,00 € HT + 320,00 € de TVA, facture de 2025), dépréciée à 100 % du HT en 2025 (491 : **1 600,00 €**).

**Pièce 6 — Règlement tardif d'un client**

- Facture F-2026-07-0144 du 31/07/2026 adressée à SCI Promenade Bureaux (SIREN 789 033 115) : **12 000,00 € TTC**, échéance **30/08/2026**.
- Relevé bancaire du 29/10/2026 : « VIR SCI PROMENADE BUREAUX F-2026-07-0144 » **+ 12 000,00 €**.
- Le responsable d'établissement est d'accord pour facturer les pénalités de retard et l'indemnité forfaitaire.
- Taux des pénalités : on retient **12,15 %** (taux BCE + 10 points — *valeur à vérifier chaque semestre*), calcul sur **365 jours**.

## Travail à faire

1. **Facture mensuelle (pièce 1)** : passez l'écriture. Relevez l'**anomalie** sur les conditions de paiement et dites ce que vous faites.
2. **Avoir (pièce 2)** : passez l'écriture. Pourquoi faut-il un avoir et non une simple correction de la facture ?
3. **Acompte (pièce 3)** : passez les trois écritures (réception de l'acompte, facture finale, imputation de l'acompte) et vérifiez que le compte client est bien à 5 040,00 € après imputation.
4. **Redressement judiciaire (pièce 4)** : passez les écritures au 31/10/2026 (reclassement et dépréciation). Expliquez pourquoi la dépréciation se calcule sur le **HT**. Quelle démarche ne faut-il surtout pas oublier ?
5. **Liquidation clôturée (pièce 5)** : passez les écritures au 31/10/2026 (perte, TVA, reprise de la dépréciation).
6. **Retard de paiement (pièce 6)** : enregistrez l'encaissement, calculez les pénalités et passez l'écriture de facturation des pénalités et de l'indemnité. Faut-il appliquer de la TVA ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-11_corrige.md)
