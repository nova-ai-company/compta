# E16-08 — La balance analytique ne tombe pas juste : retrouver et corriger les erreurs d'imputation
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** balance analytique par service, rapprochement analytique / comptabilité générale, section d'attente, erreurs d'imputation, clé de répartition des m², frais de siège en double, erreur de transposition (divisible par 9), mutation d'un salarié, OD analytiques de correction, contrôle avant reporting

**Corner case :** oui — deux erreurs ne se voient pas dans les totaux (les frais de siège passés deux fois s'annulent entre le siège et les services ; un salaire imputé au mauvais service ne change pas le total) : seul un contrôle de vraisemblance service par service les révèle

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **99-ATTENTE** | Section d'attente. Charges dont on ne connaît pas encore le service. Elle doit être vide à la clôture. |
    | **IK** | Indemnités kilométriques. Remboursement des kilomètres faits avec sa voiture personnelle pour le travail, selon un barème (prix par km). Compte 6251. |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **SARL** | Société à responsabilité limitée. Société classique des PME ; le gérant majoritaire est TNS. Ex. : C01 Boulangerie Dupain. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIREN** | Numéro d'identification de l'entreprise (9 chiffres). Identifiant unique de chaque entreprise en France. Mention obligatoire sur les factures, y compris celui du client depuis la facturation électronique. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 613** | Locations. Loyers (sous-comptes 6132 immobilier, 6135 mobilier et véhicules). |
    | **Compte 641** | Rémunérations du personnel. Salaires bruts. |
    | **Compte 645** | Charges de sécurité sociale et de prévoyance. Cotisations patronales. |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6063** | Fournitures d'entretien et de petit équipement. Petit matériel (moins de 500 € environ), produits d'entretien. |
    | **Compte 6226** | Honoraires. Expert-comptable, commissaire aux comptes, avocat. |
    | **Compte 6251** | Voyages et déplacements. Indemnités kilométriques, péages, parking, train. |
    | **Bon à payer** | Accord écrit de la direction pour payer. Sans bon à payer de la directrice, la facture ne part pas en paiement. |
    | **clé de répartition** | Règle de partage d'une charge commune. Ex. : le loyer partagé selon les m² occupés par chaque service, la téléphonie selon les ETP. |
    | **Code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **OD analytiques** | Écriture de reclassement entre services. Elle change seulement le code analytique d'une charge, pas le compte général. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **section d'attente** | Section analytique provisoire. Pour les charges dont on ne connaît pas encore le service. Elle doit être vide à la clôture. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes, fournisseurs et chiffres fictifs. Relisez la [fiche de l'association](../fiche_association_Cap_Horizons_21.md) avant de commencer.*

!!! abstract "En clair"
    La comptabilité **générale** dit **combien** l'association a dépensé (par compte). La comptabilité **analytique** dit **pour quel service** (par section). Les deux doivent donner **le même total** : chaque euro de charge doit être affecté à un service, une fois et une seule. Si les totaux diffèrent, il y a une erreur. Mais des totaux égaux ne prouvent **pas** que tout est juste : un euro peut être dans le mauvais service.

## La mise en situation

Lundi 12/10/2026, 8 h 45. Vous éditez la **balance analytique de septembre 2026** (charges uniquement) pour préparer le tableau de bord de la direction. Le total ne correspond pas au grand livre. Hélène Ferrand, au cabinet, vous répond au téléphone :

> « Classique. Ne corrigez pas au hasard : comparez d'abord compte par compte avec la générale, videz la section d'attente, puis regardez chaque service avec les pièces. Et faites-moi la liste des OD analytiques avant de les passer, je veux la relire. »

Rappels utiles :

- Sections analytiques : 01-SIEGE, 10-SESSAD, 20-SAVS, 30-EMPLOI, 40-HABITAT, 50-PAIRS, 90-ASSO. La section **99-ATTENTE** reçoit les lignes saisies **sans code** : elle doit être **à zéro** avant tout reporting.
- **Loyer** : clé des m² (SESSAD 280, SAVS 160, Emploi 60, Siège 90 ; la salle commune de 30 m² est répartie comme le reste, donc on divise par 590 m²).
- **Honoraires de l'expert-comptable** : forfait par service : Siège 10 %, SESSAD 40 %, SAVS 25 %, Emploi 15 %, Habitat 5 %, Pairs 5 %.
- **Frais de siège** : une OD analytique **trimestrielle**, passée en fin de trimestre (crédit de la section siège, débit des services). La ligne « quote-part frais de siège » doit donc être à **zéro au total**.
- Dans le logiciel, une ligne analytique « Quote-part frais de siège » positive = charge pour le service ; négative = refacturation par le siège.

## Les pièces

**Pièce 1 — Balance analytique des charges, septembre 2026 (édition du 12/10/2026)**

| Compte | 01-SIEGE | 10-SESSAD | 20-SAVS | 30-EMPLOI | 40-HABITAT | 50-PAIRS | 90-ASSO | 99-ATTENTE | **Total analytique** |
|---|---|---|---|---|---|---|---|---|---|
| 6061 Carburant | — | 1 720,00 | 780,00 | 720,00 | 260,00 | — | — | — | **3 480,00** |
| 6063 Fournitures et petit matériel | 310,00 | 500,00 | 1 060,00 | 120,00 | 160,00 | — | — | — | **2 150,00** |
| 613 Locations (loyer de Valence) | 8 932,20 | 3 677,97 | 2 101,69 | 788,14 | — | — | — | — | **15 500,00** |
| 6226 Honoraires | — | — | — | — | — | — | — | 1 800,00 | **1 800,00** |
| 6251 Voyages et déplacements (IK) | — | 1 175,00 | 690,00 | 400,00 | — | 185,00 | — | 410,00 | **2 860,00** |
| 641 Rémunérations du personnel | 7 300,00 | 42 280,00 | 19 420,00 | 10 150,00 | 2 450,00 | 800,00 | — | — | **82 400,00** |
| 645 Charges de sécurité sociale | 3 200,00 | 18 610,00 | 8 520,00 | 4 640,00 | 1 060,00 | 350,00 | — | — | **36 380,00** |
| Quote-part frais de siège (OD interne) | − 48 658,10 | 25 406,50 | 13 780,00 | 6 456,00 | 1 896,00 | 1 119,60 | — | — | **0,00** |
| **Total** | **− 28 915,90** | **93 369,47** | **46 351,69** | **23 274,14** | **5 826,00** | **2 454,60** | — | **2 210,00** | **144 570,00** |

**Pièce 2 — Balance générale, comptes de charges, septembre 2026**

| Compte | Intitulé | Solde débiteur |
|---|---|---|
| 6061 | Carburant | 3 480,00 |
| 6063 | Fournitures et petit matériel | 2 150,00 |
| 613 | Locations | 7 750,00 |
| 6226 | Honoraires | 1 800,00 |
| 6251 | Voyages et déplacements | 2 860,00 |
| 641 | Rémunérations du personnel | 82 400,00 |
| 645 | Charges de sécurité sociale et de prévoyance | 36 200,00 |
| | **Total** | **136 640,00** |

**Pièce 3 — Extraits des pièces et des journaux de septembre**

```
(a) Facture Ludiclasse SARL (fictive) — SIREN 512 874 309
    N° LC-26-0918 du 14/09/2026 — Jeux et matériel pédagogique adapté
    Montant : 640,00 € TTC (TVA non récupérable pour l'association)
    Bon de commande n° BC-SESSAD-2026-041 signé par Karim Belkacem
    Bon à payer : Nathalie Berthier, 18/09/2026
    Code analytique saisi : 20-SAVS

(b) Relevé mensuel des cartes carburant (fournisseur de cartes), septembre 2026
    Carte n° 1 à 4 — véhicules 1 à 4 — affectés 10-SESSAD ......... 1 720,00 €
    Carte n° 5 et 6 — véhicules 5 et 6 — affectés 20-SAVS .......... 1 040,00 €
        dont carte n° 5 : 260,00 € — saisie avec le code 40-HABITAT
    Carte n° 7 et 8 — véhicules 7 et 8 — affectés 30-EMPLOI ......... 720,00 €
    Note : la Maison partagée (40-HABITAT) n'a aucun véhicule de service.

(c) Récapitulatif analytique du journal de paie de septembre (service paie du cabinet)
    Section         641 brut       645 charges patronales
    01-SIEGE        7 300,00       3 200,00
    10-SESSAD      42 280,00      18 610,00
    20-SAVS        19 420,00       8 520,00
    30-EMPLOI      10 150,00       4 460,00
    40-HABITAT      2 450,00       1 060,00
    50-PAIRS          800,00         350,00
    Total          82 400,00      36 200,00
    (La ventilation de l'OD de paie a été ressaisie à la main dans le logiciel
    comptable à partir de ce récapitulatif.)

(d) Avenant au contrat de travail de Clara Vidal, éducatrice spécialisée
    « À compter du 01/09/2026, Mme Vidal est affectée au SAVS (20-SAVS). »
    Bulletin de septembre : brut 2 180,00 € ; charges patronales 960,00 €.
    Le paramétrage analytique de la paie indique toujours : 10-SESSAD.

(e) Journal des OD — 30/09/2026
    OD-2026-0931  Quote-part frais de siège T3 2026 ........ 24 329,05 €
    OD-2026-0937  Quote-part frais de siège T3 2026 ........ 24 329,05 €
    Ventilation de chaque OD : SESSAD 12 703,25 ; SAVS 6 890,00 ;
    EMPLOI 3 228,00 ; HABITAT 948,00 ; PAIRS 559,80 ; SIEGE − 24 329,05

(f) Loyer de septembre — facture du bailleur : 7 750,00 € (620 m²)
    Saisie le 01/09 avec le code par défaut 01-SIEGE pour 7 750,00 €.
    Le 30/09, OD de répartition aux m² saisie en ajoutant des lignes :
    SIEGE 1 182,20 ; SESSAD 3 677,97 ; SAVS 2 101,69 ; EMPLOI 788,14.

(g) États de frais de septembre (indemnités kilométriques, compte 6251)
    - Lucas Moreno, job coach de l'emploi accompagné : 410,00 €
      → importé sans code analytique.
    - Mme Fabre, parent bénévole : déplacement pour tenir le stand de
      l'association au forum des associations de Valence (12/09) : 185,00 €
      → codé 50-PAIRS (« elle participe aussi au projet Pairs »).
      Le stand relève de la vie associative (sensibilisation).

(h) Honoraires du cabinet d'expertise comptable, septembre : 1 800,00 €
    → saisis sans code analytique.
```

## Travail à faire

1. Comparez la balance analytique et la balance générale **compte par compte**. Quels comptes présentent un écart ? Que vous suggère chaque écart (pensez à la règle de la division par 9) ?
2. Listez **toutes** les anomalies (il y en a 9), avec la pièce qui les prouve et la conséquence sur chaque service.
3. Rédigez les **OD analytiques de correction** (débit = on ajoute à la section, crédit = on retire de la section). Distinguez les corrections qui **déplacent** un montant d'une section à l'autre de celles qui **suppriment** une ligne analytique en trop.
4. Présentez la **balance analytique corrigée** et vérifiez qu'elle tombe sur le total du grand livre.
5. Pourquoi la section 01-SIEGE reste-t-elle négative en septembre après correction ? Est-ce une anomalie ?
6. Proposez **cinq contrôles** à faire chaque mois pour éviter ces erreurs.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E16-08_corrige.md)
