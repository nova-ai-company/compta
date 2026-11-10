# E16-01 — Codifier douze factures : compte de charge, code analytique, groupe fonctionnel
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★☆☆ | **Durée estimée :** 40 min | **Thèmes :** réception des factures, codification, TVA non récupérable, code analytique, groupes fonctionnels, immobilisation, note de frais, facture d'un exercice antérieur, charges constatées d'avance, double signature

**Corner case :** oui — une facture au nom d'une salariée, une facture qui concerne l'exercice 2025, une facture commune à plusieurs services adressée à un seul service

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **00-COMMUN** | Section des charges communes à répartir. Section « de passage » : on y saisit les charges partagées (loyer, téléphone…), puis on la vide vers les services avec une clé. Elle doit revenir à zéro. |
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **FALC** | Facile à lire et à comprendre. Méthode d'écriture simple, illustrée, pensée pour les personnes avec une déficience intellectuelle. Très utilisée dans le réseau Trisomie 21. |
    | **FNP** | Factures non parvenues. À la clôture : charges de l'année dont la facture n'est pas encore arrivée. On les enregistre quand même (compte 408) pour que l'année supporte ses vraies charges. |
    | **HA** | Journal des achats. Autre code fréquent pour le journal des achats (équivalent de AC). |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **OD** | Opérations diverses. Journal des écritures qui ne sont ni des achats, ni des ventes, ni de la banque : paie, amortissements, provisions, corrections, régularisations de clôture. |
    | **SARL** | Société à responsabilité limitée. Société classique des PME ; le gérant majoritaire est TNS. Ex. : C01 Boulangerie Dupain. |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SCI** | Société civile immobilière. Société qui détient et loue des biens immobiliers. Ex. : C06 SCI Les Tilleuls, C07 SCI Horizon Pro. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIREN** | Numéro d'identification de l'entreprise (9 chiffres). Identifiant unique de chaque entreprise en France. Mention obligatoire sur les factures, y compris celui du client depuis la facturation électronique. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 401** | Fournisseurs. Ce que l'association doit à ses fournisseurs (factures reçues, pas encore payées). |
    | **Compte 404** | Fournisseurs d'immobilisations. Dettes envers un fournisseur pour un bien durable (véhicule, ordinateur). |
    | **Compte 421** | Personnel. Rémunérations dues : les salaires nets à verser. |
    | **Compte 486** | Charges constatées d'avance (CCA). Dépense payée cette année qui concerne l'année suivante (assurance, loyer d'avance). |
    | **Compte 614** | Charges locatives et de copropriété. |
    | **Compte 616** | Primes d'assurances. Assurance des locaux, des véhicules, responsabilité civile. Pas de TVA. |
    | **Compte 626** | Frais postaux et de télécommunications. Téléphone, internet, timbres. |
    | **Compte 2183** | Matériel de bureau et informatique. Ordinateurs, imprimantes : un bien durable, amorti sur plusieurs années. |
    | **Compte 4081** | Fournisseurs. Factures non parvenues (sous-compte du 408). |
    | **Compte 6061** | Fournitures non stockables. Carburant, eau, électricité. |
    | **Compte 6063** | Fournitures d'entretien et de petit équipement. Petit matériel (moins de 500 € environ), produits d'entretien. |
    | **Compte 6064** | Fournitures administratives. Papier, stylos, cartouches. |
    | **Compte 6068** | Autres matières et fournitures. Matériel pédagogique, jeux, fournitures d'activités. |
    | **Compte 6132** | Locations immobilières. Loyer des locaux, location de salle. |
    | **Compte 6185** | Frais de colloques, séminaires, conférences. |
    | **Compte 6226** | Honoraires. Expert-comptable, commissaire aux comptes, avocat. |
    | **Compte 6288** | Autres services extérieurs divers. Ex. : sorties et activités des personnes accompagnées (selon le plan interne). |
    | **Compte 6811** | Dotations aux amortissements. L'usure annuelle des biens durables (véhicules, ordinateurs). |
    | **Autodétermination** | Décider pour soi-même. Principe central du réseau Trisomie 21 : la personne fait ses propres choix de vie, avec du soutien si besoin. |
    | **charges communes** | Charge partagée entre plusieurs services. Elle est répartie avec une clé (ex. : le loyer des locaux de Valence). |
    | **charges constatées d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **double signature** | Deux personnes valident le paiement. Au-dessus d'un seuil, la directrice ET la trésorière signent le virement : c'est un contrôle anti-fraude. |
    | **Emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **groupe fonctionnel** | Les 3 familles de dépenses d'un ESSMS. Groupe I : exploitation courante. Groupe II : personnel. Groupe III : structure (loyers, amortissements, frais de siège). |
    | **groupe III** | Dépenses de structure. Loyers, assurances, entretien, amortissements, frais de siège, intérêts. |
    | **habitat inclusif** | Logement partagé en milieu ordinaire. Des personnes handicapées vivent ensemble chez elles, avec un projet de vie partagé animé par l'association. |
    | **section d'attente** | Section analytique provisoire. Pour les charges dont on ne connaît pas encore le service. Elle doit être vide à la clôture. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes, fournisseurs et documents fictifs.*

!!! abstract "En clair"
    **Codifier** une facture, c'est écrire dessus trois informations avant la saisie : **le compte** (quelle dépense ?), **le code analytique** (quel service la paie ?) et **le groupe fonctionnel** (dans quelle case du budget de l'ESSMS — établissement ou service social et médico-social — elle tombe). Une erreur de code analytique fait payer une dépense par le mauvais financeur.

## La mise en situation

Mardi 10/11/2026, 9 h. C'est votre deuxième semaine chez Cap Horizons 21. Mme Roux, l'ancienne comptable, est partie en retraite vendredi. Elle vous laisse un parapheur avec douze pièces et un post-it :

> « Bonjour ! Voici les factures d'octobre et du début de novembre. Elles sont toutes **validées par Nathalie (la directrice)**. Il reste à les codifier et à les saisir. Attention, il y a deux ou trois "pièges" que je n'ai pas eu le temps de traiter. Bon courage ! — Mme Roux »

Rappels utiles (voir la fiche de l'association) :

- L'association **ne récupère pas la TVA** : toutes les charges sont enregistrées **TTC** (toutes taxes comprises).
- **Procédure interne (fictive)** : une facture commune à plusieurs services est saisie sur le code **00-COMMUN** (section d'attente « charges communes à répartir »). Elle est ensuite répartie avec les clés de la fiche par une **OD** (opération diverse) analytique. La section 00-COMMUN doit être à zéro après la répartition.
- **Seuil d'immobilisation (règle interne fictive)** : un bien durable dont la valeur unitaire dépasse **500 € TTC** est immobilisé (compte 2183) et amorti. En dessous, il va en charge.
- **Double signature** (directrice + trésorière) pour tout paiement supérieur à **1 500 €**.
- Au 31/12/2025, la comptabilité contenait les **factures non parvenues** (FNP) suivantes (extrait du compte 4081) :

| Fournisseur | Objet | Montant TTC |
|---|---|---|
| Rhône Auto Services | Révision véhicule de service AB-123-CD, intervention du 15/12/2025 | 384,00 € |
| Imprimerie du Vivarais | Plaquettes de présentation (facture reçue le 12/01/2026, FNP soldée) | 0,00 € |

Mme Roux ne pratique **pas** l'extourne des FNP au 01/01 : le compte 4081 présente toujours un solde créditeur de 384,00 € au 10/11/2026.

### Extrait du plan de comptes de Cap Horizons 21 (plan interne, *à vérifier sur le plan réel de l'association*)

| Compte | Intitulé | Groupe fonctionnel |
|---|---|---|
| 2183 | Matériel de bureau et matériel informatique | — (immobilisation ; son amortissement 6811 ira en groupe III) |
| 401 | Fournisseurs | — |
| 404 | Fournisseurs d'immobilisations | — |
| 4081 | Fournisseurs – factures non parvenues | — |
| 421 | Personnel – rémunérations dues (notes de frais) | — |
| 486 | Charges constatées d'avance | — |
| 6061 | Fournitures non stockables (énergie, carburant) | I |
| 6063 | Fournitures d'entretien et de petit équipement | I |
| 6064 | Fournitures administratives | I |
| 6068 | Autres fournitures (matériel éducatif et pédagogique) | I |
| 6132 | Locations immobilières | III |
| 614 | Charges locatives et de copropriété | III |
| 616 | Primes d'assurance | III |
| 6185 | Frais de formation du personnel (organismes extérieurs) | II *(classement interne)* |
| 6226 | Honoraires (commissaire aux comptes, expert-comptable) | III |
| 626 | Frais postaux et de télécommunications | I |
| 6288 | Activités et sorties des personnes accompagnées | I |

Codes analytiques : 00-COMMUN · 01-SIEGE · 10-SESSAD · 20-SAVS · 30-EMPLOI · 40-HABITAT · 50-PAIRS · 90-ASSO.

## Les pièces

**Pièce 1 — Facture Éveil & Apprendre SARL** (SIREN 512 487 903), n° EA-26-1187 du 15/10/2026

```
Livré à : Cap Horizons 21 – SESSAD, 14 rue des Alpes, 26000 Valence
Commande n° 2026-SESSAD-041 signée par K. Belkacem
3 kits de manipulation « Je compte, je trie »   3 × 64,00  = 192,00 HT  TVA 20 %
1 lot de pictogrammes plastifiés (200 pièces)              88,00 HT  TVA 20 %
4 livres « Lire en FALC » (facile à lire et à comprendre)
                                                4 × 16,00  =  64,00 HT  TVA 5,5 %
Total HT 344,00 — TVA 20 % 56,00 — TVA 5,5 % 3,52 — Total TTC 403,52 €
Paiement à 30 jours. Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €.
```

**Pièce 2 — Relevé mensuel cartes carburant Carbu'Pro Services**, octobre 2026, daté du 31/10/2026

| Véhicule | Affectation | Litres | TTC |
|---|---|---|---|
| AB-123-CD | SESSAD | 112,4 | 205,90 |
| AC-456-EF | SESSAD | 98,1 | 179,70 |
| AD-789-GH | SESSAD | 104,6 | 191,60 |
| AE-012-IJ | SESSAD | 87,3 | 159,90 |
| AF-345-KL | SAVS | 95,2 | 174,40 |
| AG-678-MN | SAVS | 61,0 | 111,70 |
| AH-901-OP | Emploi accompagné | 72,5 | 132,80 |
| AJ-234-QR | Véhicule partagé (pool) | 50,1 | 92,00 |
| **Total** | | | **1 248,00 € TTC dont TVA 208,00 €** |

Note : chez Cap Horizons 21, **tous** les frais des 8 véhicules sont répartis entre services au kilomètre (carnets de bord), en fin de période.

**Pièce 3 — Avis d'échéance SCI Les Terrasses du Rhône** du 25/10/2026, échéance du **01/11/2026**

```
Locataire : CAP HORIZONS 21 – SESSAD   (bail signé le 01/09/2009)
Locaux : 14 rue des Alpes, 26000 Valence — 620 m² (plateau complet)
Loyer de novembre 2026 ............................ 6 200,00
Provision sur charges (chauffage, ménage, eau) ..... 1 000,00
Total à payer ...................................... 7 200,00 €
Le bailleur n'a pas opté pour la TVA.
```

**Pièce 4 — Avis de cotisation Mutuelle Alpine des Associations** du 20/10/2026

```
Contrat multirisque n° MAA-40-2231 — « La Maison partagée » (habitat inclusif)
Période garantie : du 01/11/2026 au 31/10/2027
Cotisation annuelle TTC (taxe sur les conventions d'assurance incluse) : 1 140,00 €
Prélèvement le 05/11/2026.
```

**Pièce 5 — Facture Audit Rhodanien** (commissaire aux comptes, M. Garnier), n° AR-2026-317 du 30/10/2026

```
Mission de certification des comptes de l'exercice 2026 — acompte n° 1 sur 2
Honoraires HT 4 800,00 — TVA 20 % 960,00 — Total TTC 5 760,00 €
Règlement à réception.
```

**Pièce 6 — Facture Rhône Bureautique** (SIREN 438 902 117), n° RB-77812 du 28/10/2026

```
Livré à : Cap Horizons 21 – SAVS
2 ordinateurs portables 15"            2 × 790,00 = 1 580,00 HT
2 souris sans fil                      2 ×  19,90 =    39,80 HT
Total HT 1 619,80 — TVA 20 % 323,96 — Total TTC 1 943,76 €
Garantie constructeur 3 ans. Paiement à 30 jours.
```

**Pièce 7 — Facture Restaurant La Table du Parc**, Valence, n° 2026-1042 du 17/10/2026

```
Client : Association Cap Horizons 21 – SAVS
Sortie « restaurant et budget » : 6 personnes accompagnées + 2 accompagnants
8 menus du jour × 18,50 TTC = 148,00 € TTC (dont TVA 10 % : 13,45)
Paiement par virement à réception.
```

**Pièce 8 — Facture Institut Formation Handicap Rhône-Alpes (IFHRA)**, n° F-26-0904 du 23/10/2026

```
Formation « Autodétermination : accompagner le pouvoir d'agir » — 2 jours (19 et 20/10/2026)
Stagiaires : Léa Fontaine (SESSAD), Marc Rivière (SAVS), Inès Moulin (Emploi accompagné)
3 stagiaires × 420,00 = 1 260,00 €
TVA non applicable : formation professionnelle continue exonérée.
```

**Pièce 9 — Facture Espace Rencontres du Plateau** (association), n° 26-118 du 05/11/2026

```
Location de la grande salle — 3 demi-journées (14/10, 21/10, 28/10/2026)
Groupe « Pairs et voix » — formation des autoreprésentants
3 × 75,00 = 225,00 € — Association non assujettie à la TVA.
```

**Pièce 10 — Facture Teleo Pro** (téléphonie et internet), n° TP-1026-55841 du 31/10/2026

```
Client : Cap Horizons 21 (compte entreprise unique)
Fibre + standard du siège ............................ 189,00 HT
30 lignes mobiles (forfaits professionnels) .......... 571,50 HT
Options et hors forfait .............................. 51,90 HT
Total HT 812,40 — TVA 20 % 162,48 — Total TTC 974,88 €
Prélèvement le 15/11/2026.
```

**Pièce 11 — Ticket-facture La Boîte à Jeux**, Valence, du 08/10/2026, joint à une note de frais

```
Facture au nom de : Mme Léa Fontaine, 8 allée des Tilleuls, 26500 Bourg-lès-Valence
2 jeux de société « émotions » et 1 jeu de mémoire illustré
Total TTC 86,40 € (dont TVA 20 % : 14,40) — payé par carte bancaire
```
Note de frais d'octobre de Léa Fontaine (éducatrice spécialisée, SESSAD), signée par elle et **validée par Karim Belkacem** : « Jeux pour les séances à l'école Jean-Moulin, achat urgent, payé avec ma carte personnelle ». Pas d'autre ligne sur la note.

**Pièce 12 — Facture Rhône Auto Services**, n° RAS-11-0093 du **03/11/2026**

```
Véhicule AB-123-CD — révision des 60 000 km — intervention du 15/12/2025
Total HT 320,00 — TVA 20 % 64,00 — Total TTC 384,00 €
« Facture émise avec retard suite au changement de notre logiciel. Veuillez nous en excuser. »
```

## Travail à faire

1. Pour chacune des 12 pièces, remplissez un tableau : **pièce / compte / montant TTC / code analytique / groupe fonctionnel / remarque**. Quand une pièce doit être découpée sur plusieurs comptes ou plusieurs codes, faites une ligne par morceau.
2. Expliquez en une phrase pourquoi l'association enregistre ses charges **TTC**.
3. Repérez les trois « pièges » annoncés par Mme Roux (facture au nom d'une salariée, facture de 2025, facture commune adressée à un seul service) et dites comment vous les traitez.
4. Passez les écritures de saisie (journal des achats HA, et journal des opérations diverses OD pour la note de frais), avec une colonne « code analytique ».
5. La pièce 4 couvre une période à cheval sur 2026 et 2027 : quelle écriture faudra-t-il passer au 31/12/2026 ?
6. Quelles factures demandent la **double signature** au moment du paiement ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E16-01_corrige.md)
