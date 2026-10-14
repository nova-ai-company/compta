# E08-05 — Stock de véhicules d'occasion du Garage Martin au 30/09/2026
**Client :** C03 — Garage Martin | **Difficulté :** ★★★ | **Durée estimée :** 60 min | **Thèmes :** biens identifiables (coût individuel), frais de remise en état (pièces + main-d'œuvre au coût de revient), VNR avec TVA sur la marge, véhicule invendu depuis plus de 6 mois, véhicule endommagé (coûts d'achèvement), vente aux enchères, véhicule en dépôt-vente, acompte reçu sur un véhicule non livré, variation de stock créditrice

**Corner case :** oui — la TVA sur la marge vient réduire la VNR (sauf si la marge est négative), et un véhicule « au stock » n'appartient pas au garage

## La mise en situation

Garage Martin EURL (IS, réel normal) clôture son exercice le **30/09/2026**. Nous sommes le **12 octobre 2026**. Thierry Martin, gérant, a déposé au cabinet la liste des véhicules d'occasion (VO) présents sur le parc le 30/09 au soir, le livre de police et les ordres de réparation internes.

Son mot :

> « Stock VO au 30/09 : 95 970 €, j'ai mis les prix affichés sur les pare-brise, c'est ce qu'ils valent. Pour le 3008 qui ne part pas, on verra l'an prochain. J'ai déjà encaissé 1 000 € d'acompte sur la C3, je l'ai passé en vente VO. Thierry »

Hélène Ferrand : « Valorisez chaque véhicule à son coût réel, testez la VNR véhicule par véhicule — attention à la TVA sur la marge — et passez les écritures. Ce garage sert de base au cas de synthèse : je veux un dossier impeccable. »

Données :
- **coût horaire de revient** de la main-d'œuvre de l'atelier (salaires chargés + charges de l'atelier, hors frais administratifs et commerciaux), calculé par le cabinet : **42,00 €/h** ; taux horaire facturé aux clients : 78,00 € HT ;
- coûts de vente estimés pour une vente au détail d'un VO : **garantie commerciale 3 mois** (coût statistique) **180 €** + **préparation esthétique** **60 €**, soit **240 €** par véhicule ;
- la TVA sur la marge d'un VO acheté à un particulier se calcule sur (prix de vente TTC – prix d'achat) × 20/120 ; si la marge est négative, la TVA est nulle (pas d'imputation sur les autres ventes) ; les frais de remise en état ne sont **pas** déductibles de la marge (leur TVA est récupérée normalement) ;
- balance avant inventaire : **37 Stocks de marchandises – VO : 58 700,00 €** (stock au 30/09/2025) ; **397 Dépréciations – VO : 2 150,00 €** (constituée au 30/09/2025 sur deux véhicules vendus depuis) ;
- le stock de pièces détachées est traité séparément (hors exercice).

## Les pièces

**Pièce 1 — Liste du parc VO établie par Thierry Martin (30/09/2026, 19 h)**
```
GARAGE MARTIN — VO SUR LE PARC AU 30/09/2026
Véhicule                         Immat.       Prix affiché TTC
Peugeot 3008 BlueHDi 2018         FG-***-KL        16 900
Renault Clio V TCe 2020           FK-***-PB        11 990
Dacia Sandero 2021                GA-***-ZT         6 490
Peugeot 308 PureTech 2021         GB-***-MC        15 900
Volkswagen Golf 8 2022            GE-***-RA        19 200
Citroën C3 PureTech 2019          FH-***-DS         8 990
BMW Série 1 118i 2020             FL-***-VN        16 500
TOTAL                                              95 970
```

**Pièce 2 — Extrait du livre de police (registre des véhicules d'occasion)**
```
N° ordre    Date entrée   Véhicule              Vendeur                                   Prix d'achat   Régime TVA à la revente
P-2025-118  20/10/2025    Peugeot 3008 2018     particulier (M. A. Ferrer)                 13 800,00     marge
P-2025-131  08/12/2025    Renault Clio V 2020   particulier (Mme S. Kaya)                  10 900,00     marge
P-2026-022  03/03/2026    Dacia Sandero 2021    particulier (M. D. Royer)                   5 200,00     marge
P-2026-061  12/06/2026    Peugeot 308 2021      particulier (Mme L. Chassagne)             11 500,00     marge
P-2026-074  22/07/2026    VW Golf 8 2022        Rhône Location Courte Durée SAS            14 200,00 HT  normal (TVA 20 % sur le prix total)
                                                (facture n° RLCD-26-0712, TVA 2 840,00 € déduite)
P-2026-089  15/09/2026    Citroën C3 2019       particulier (M. J. Petitjean)               6 900,00     marge
```

**Pièce 3 — Ordres de réparation internes (remise en état avant vente)**
```
OR interne   Véhicule          Pièces (coût d'achat HT)   Main-d'œuvre (heures)
OI-26-014    Peugeot 3008             1 150,00                 10 h
OI-26-002    Renault Clio V             420,00                  4 h
OI-26-041    Peugeot 308                640,00                  6 h
OI-26-055    Citroën C3                 380,00                  3 h
(Golf et Sandero : aucune remise en état)
```

**Pièce 4 — Mandat de dépôt-vente**
```
MANDAT DE DÉPÔT-VENTE du 02/09/2026
Mandant : M. Bruno Lacroix, 14 rue Cavenne, 69007 Lyon — Mandataire : Garage Martin EURL
Véhicule : BMW Série 1 118i 2020 — Prix de vente minimum souhaité : 16 000 € TTC
Le véhicule reste la propriété du mandant jusqu'à sa vente. Commission du mandataire : 8 % du prix de vente.
```

**Pièce 5 — Bon de commande et reçu d'acompte**
```
BON DE COMMANDE VO n° BC-26-0177 du 28/09/2026 — Client : Mme Nora Benhamou
Citroën C3 PureTech 2019 — Prix 8 990,00 € TTC (régime de la marge — art. 297 A du CGI)
Acompte versé ce jour par CB : 1 000,00 € — Livraison prévue après immatriculation : 05/10/2026
```
Comptabilisation par Thierry : D 512 1 000,00 / C 707 1 000,00. Le véhicule a été livré le 05/10/2026.

**Pièce 6 — Notes du dossier VO (préparées avec Thierry le 09/10/2026)**
```
- Clio V : en stock depuis 10 mois. Prix affiché baissé deux fois. Cote professionnelle : 10 600 €.
  Deux offres fermes reçues en septembre : 10 200 € et 10 400 € TTC. Prix de vente retenu : 10 400 € TTC.
- Sandero : grêle du 14/08/2026 sur le parc (franchise d'assurance supérieure au dommage, pas d'indemnité).
  Débosselage sans peinture à faire avant la vente : devis Débosselage Express 600,00 € HT.
  Prix de vente estimé après réparation : 4 800 € TTC.
- 308 : prix de vente probable après négociation : 15 400 € TTC.
- Golf : prix de vente probable 19 200 € TTC (régime normal).
- 3008 diesel 2018 : aucun acheteur depuis 11 mois (restrictions ZFE à Lyon). Décision du gérant
  du 25/09/2026 : vente aux enchères professionnelles (VPA Enchères Auto, vacation du 22/10/2026).
  Estimation de la maison d'enchères : adjudication 11 200 € (régime de la marge).
  Frais vendeur : 6 % HT du prix d'adjudication + convoyage 150 € HT.
```

## Travail à faire

1. Analysez la liste de Thierry : quelles erreurs de principe contient-elle ?
2. Déterminez le coût d'entrée de chaque véhicule appartenant au garage au 30/09/2026.
3. Calculez la VNR de chaque véhicule et la dépréciation nécessaire. Justifiez le traitement de la TVA sur la marge dans la VNR.
4. Traitez l'acompte de la C3.
5. Passez les écritures d'inventaire au 30/09/2026 et commentez le sens du compte 6037.
6. Répondez à Thierry, notamment sur le 3008 (« on verra l'an prochain »).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E08-05_corrige.md)
