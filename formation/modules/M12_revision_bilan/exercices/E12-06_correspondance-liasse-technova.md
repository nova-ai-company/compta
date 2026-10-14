# E12-06 — Correspondance balance → liasse 2050 à 2053 (TechNova)
**Client :** C08 — TechNova SAS | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 15 | **Thèmes :** liasse fiscale du régime réel normal, mapping des comptes, non-compensation, autres fonds propres, CIR, frais de développement, écarts de conversion

**Corner case :** oui — comptes « inhabituels » d'une start-up (avance conditionnée, production immobilisée, CIR, banque créditrice, écart de conversion).

## La mise en situation

Lundi 12 octobre 2026. Le cabinet migre vers un nouveau logiciel de production ; le **paramétrage du passage balance → liasse** (« mapping ») doit être revu compte par compte avant la saison fiscale. Hélène Ferrand :

> « Testez le nouveau mapping sur la balance **2025** de TechNova (liasse déposée en mai) : c'est le dossier qui a les comptes les plus atypiques. Pour chaque compte de l'extrait, indiquez le formulaire, la rubrique et le code de case. Signalez-moi tout compte que le logiciel risque de mal classer. »

Émilie Roux (DAF à temps partagé) a ajouté en commentaire : « Pour le CIR, on l'a passé en moins de l'IS comme d'habitude. La banque Crédit Coopératif est à découvert au 31/12, c'est juste technique, on peut compenser avec BNP, non ? »

## Les pièces

### Extrait de la balance après inventaire au 31/12/2025 (comptes atypiques ou à risque de classement)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 1013 | Capital souscrit, appelé, versé | | 54 000,00 |
| 1041 | Primes d'émission | | 446 000,00 |
| 131 | Subventions d'équipement (Région) | | 40 000,00 |
| 139 | Subventions d'investissement inscrites au compte de résultat | 12 000,00 | |
| 1674 | Avances conditionnées de l'État (avance remboursable Bpifrance) | | 120 000,00 |
| 1641 | Emprunts auprès des établissements de crédit | | 85 000,00 |
| 1688 | Intérêts courus sur emprunts | | 310,00 |
| 1515 | Provisions pour pertes de change | | 1 200,00 |
| 203 | Frais de développement | 380 000,00 | |
| 2803 | Amortissements des frais de développement | | 140 000,00 |
| 205 | Concessions, logiciels, licences | 24 000,00 | |
| 2805 | Amortissements des logiciels | | 16 000,00 |
| 232 | Immobilisations incorporelles en cours (version 4 du logiciel) | 95 000,00 | |
| 2183 | Matériel informatique | 68 000,00 | |
| 28183 | Amortissements du matériel informatique | | 41 000,00 |
| 275 | Dépôts et cautionnements versés | 12 000,00 | |
| 4091 | Fournisseurs – avances et acomptes versés | 3 000,00 | |
| 411 | Clients | 210 000,00 | |
| 4181 | Clients – factures à établir | 14 000,00 | |
| 491 | Dépréciation des comptes clients | | 8 000,00 |
| 4191 | Clients – avances et acomptes reçus | | 9 000,00 |
| 401 | Fournisseurs | | 64 000,00 |
| 4081 | Fournisseurs – factures non parvenues | | 7 500,00 |
| 404 | Fournisseurs d'immobilisations | | 5 000,00 |
| 4282 | Dettes provisionnées pour congés payés | | 38 000,00 |
| 431 | Sécurité sociale | | 41 000,00 |
| 437 | Autres organismes sociaux | | 9 000,00 |
| 444 | État – impôt sur les bénéfices (créance de CIR 2025) | 126 000,00 | |
| 44551 | TVA à décaisser | | 22 000,00 |
| 44566 | TVA déductible sur ABS (factures de décembre non encore déclarées) | 6 000,00 | |
| 455 | Associés – comptes courants | | 30 000,00 |
| 467-D | Débiteurs divers | 2 500,00 | |
| 467-C | Créditeurs divers | | 1 800,00 |
| 476 | Différences de conversion – actif | 1 200,00 | |
| 486 | Charges constatées d'avance | 11 000,00 | |
| 487 | Produits constatés d'avance (abonnements annuels) | | 182 000,00 |
| 512-BNP | Banque BNP | 640 000,00 | |
| 512-CC | Banque Crédit Coopératif | | 3 500,00 |
| 706-FR | Abonnements SaaS – France | | 1 450 000,00 |
| 706-UE | Abonnements SaaS – clients professionnels UE | | 270 000,00 |
| 721 | Production immobilisée – immobilisations incorporelles | | 140 000,00 |
| 74 | Subventions d'exploitation | | 25 000,00 |
| 747 | Quote-part des subventions d'investissement virée au résultat (*numéro selon la nomenclature 2025 du PCG — à vérifier*) | | 8 000,00 |
| 604 | Achats d'études et prestations de services (hébergement cloud) | 96 000,00 | |
| 621 | Personnel extérieur à l'entreprise | 30 000,00 | |
| 6411 | Salaires | 1 150 000,00 | |
| 645 | Charges de sécurité sociale et de prévoyance | 380 000,00 | |
| 6811 | Dotations aux amortissements des immobilisations | 98 000,00 | |
| 6817 | Dotations aux dépréciations des actifs circulants | 8 000,00 | |
| 658 | Pénalités et amendes (*subdivision selon la nomenclature 2025 du PCG*) | 1 200,00 | |
| 6611 | Intérêts des emprunts | 3 100,00 | |
| 666 | Pertes de change financières | 900,00 | |
| 766 | Gains de change financiers | | 400,00 |
| 6865 | Dotations aux provisions financières (perte de change) | 1 200,00 | |
| 675 | Valeurs comptables des éléments d'actif cédés | 600,00 | |
| 775 | Produits des cessions d'éléments d'actif | | 1 000,00 |
| 695 | Impôts sur les bénéfices (CIR imputé) | | 126 000,00 |

## Travail à faire

1. Pour chaque compte, indiquez le **formulaire** (2050, 2051, 2052, 2053), la **rubrique** et le **code de case** (colonne brut / amortissements le cas échéant).
2. Calculez le montant de chaque rubrique concernée (sur le seul périmètre de l'extrait).
3. Identifiez les **pièges de mapping** (comptes de sens inverse, non-compensation, rubriques peu connues).
4. Répondez à Émilie Roux sur la compensation des deux banques et sur la présentation du CIR.
5. Quels **contrôles automatiques** mettez-vous en place dans le nouveau logiciel pour sécuriser la liasse ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E12-06_corrige.md)
