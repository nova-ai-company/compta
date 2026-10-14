# Corrigé E12-06 — Correspondance balance → liasse 2050 à 2053 (TechNova)

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E12-06](../exercices/E12-06_correspondance-liasse-technova.md)

> ⚠️ Les **codes de cases** indiqués sont ceux des liasses 2050 à 2053 en usage depuis de nombreuses années. Le millésime de la liasse peut être adapté (notamment à la suite du PCG 2025 : intitulés « transferts de charges », résultat exceptionnel) : **vérifiez toujours les codes sur la notice du millésime en vigueur** avant de figer un paramétrage.

## 1. Analyse (raisonnement pas à pas)

Un mapping se fait **au niveau du compte de détail**, jamais au niveau de la classe : 512 peut aller à l'actif (disponibilités) ou au passif (concours bancaires), 467 en « autres créances » ou « autres dettes », 444 en créance ou en dette selon son sens. Trois règles :
1. **Non-compensation** des soldes de sens contraire (art. L. 123-19 C. com. et PCG) : chaque compte auxiliaire / chaque banque est classé selon **son** solde.
2. **Brut / amortissements / net** à l'actif : les comptes 28 et 49 vont dans la colonne « amortissements, provisions » de la ligne de l'actif concerné, jamais au passif.
3. **Rubriques spécifiques** : avances conditionnées (« autres fonds propres »), production immobilisée, écarts de conversion.

## 2. Calculs — tableau de correspondance

### 2.1 Formulaire 2050 (actif)

| Compte(s) | Rubrique | Case brut | Case amort./dépréc. | Brut | Amort. | Net |
|---|---|---|---|---:|---:|---:|
| 203 / 2803 | Frais de développement | CX | CQ | 380 000 | 140 000 | 240 000 |
| 205 / 2805 | Concessions, brevets et droits similaires | AF | AG | 24 000 | 16 000 | 8 000 |
| 232 | Autres immobilisations incorporelles (dont en cours) | AJ | AK | 95 000 | – | 95 000 |
| 2183 / 28183 | Autres immobilisations corporelles | AT | AU | 68 000 | 41 000 | 27 000 |
| 275 | Autres immobilisations financières | BF | BG | 12 000 | – | 12 000 |
| 4091 | Avances et acomptes versés sur commandes | BV | BW | 3 000 | – | 3 000 |
| 411 + 4181 / 491 | Clients et comptes rattachés | BX | BY | 224 000 | 8 000 | 216 000 |
| 444 + 44566 + 467-D | Autres créances | BZ | CA | 134 500 | – | 134 500 |
| 512-BNP | Disponibilités | CF | — | 640 000 | – | 640 000 |
| 486 | Charges constatées d'avance | CH | — | 11 000 | – | 11 000 |
| 476 | Écarts de conversion actif | ligne dédiée en bas d'actif (code à vérifier sur le millésime) | — | 1 200 | – | 1 200 |

Autres créances : 126 000 (CIR) + 6 000 (TVA) + 2 500 = 134 500.

### 2.2 Formulaire 2051 (passif)

| Compte(s) | Rubrique | Case | Montant |
|---|---|---|---:|
| 1013 | Capital social ou individuel (dont versé) | DA | 54 000 |
| 1041 | Primes d'émission, de fusion, d'apport | DB | 446 000 |
| 131 – 139 | Subventions d'investissement (montant net) | DJ | 28 000 |
| 1674 | **Avances conditionnées** (rubrique « Autres fonds propres ») | DN | 120 000 |
| 1515 | Provisions pour risques | DP | 1 200 |
| 1641 + 1688 + 512-CC | Emprunts et dettes auprès des établissements de crédit | DU | 88 810 |
| 455 | Emprunts et dettes financières divers | DV | 30 000 |
| 4191 | Avances et acomptes reçus sur commandes en cours | DW | 9 000 |
| 401 + 4081 | Dettes fournisseurs et comptes rattachés | DX | 71 500 |
| 4282 + 431 + 437 + 44551 | Dettes fiscales et sociales | DY | 110 000 |
| 404 | Dettes sur immobilisations et comptes rattachés | DZ | 5 000 |
| 467-C | Autres dettes | EA | 1 800 |
| 487 | Produits constatés d'avance | EB | 182 000 |

DU : 85 000 + 310 + 3 500 = 88 810 (dont concours bancaires courants et soldes créditeurs de banque : 3 500 — information demandée en bas du 2051). DY : 38 000 + 41 000 + 9 000 + 22 000 = 110 000.

### 2.3 Formulaire 2052 (compte de résultat – exploitation)

| Compte(s) | Rubrique | Case(s) | Montant |
|---|---|---|---:|
| 706-FR | Production vendue – services – France | FG | 1 450 000 |
| 706-UE | Production vendue – services – Exportations et livraisons intracommunautaires | FH | 270 000 |
| | Production vendue – services – Total | FI | 1 720 000 |
| | Chiffre d'affaires net (total) | FL | 1 720 000 |
| 721 | Production immobilisée | FN | 140 000 |
| 74 | Subventions d'exploitation | FO | 25 000 |
| 747 | Quote-part de subvention d'investissement : **en exploitation** si la nomenclature 2025 la classe en 74x (sinon en produits exceptionnels sur opérations en capital, HB) — *point à valider* | FQ / FO selon paramétrage, ou HB | 8 000 |
| 604 + 621 | Autres achats et charges externes | FW | 126 000 |
| 6411 | Salaires et traitements | FY | 1 150 000 |
| 645 | Charges sociales | FZ | 380 000 |
| 6811 | Dotations aux amortissements sur immobilisations | GA | 98 000 |
| 6817 | Dotations aux dépréciations sur actif circulant | GC | 8 000 |
| 658 | Autres charges | GE | 1 200 |

### 2.4 Formulaire 2053 (financier, exceptionnel, impôt)

| Compte(s) | Rubrique | Case | Montant |
|---|---|---|---:|
| 766 | Différences positives de change | GN | 400 |
| 6865 | Dotations financières aux amortissements, dépréciations et provisions | GQ | 1 200 |
| 6611 | Intérêts et charges assimilées | GR | 3 100 |
| 666 | Différences négatives de change | GS | 900 |
| 775 | Produits exceptionnels sur opérations en capital | HB | 1 000 |
| 675 | Charges exceptionnelles sur opérations en capital | HF | 600 |
| 695 (créditeur) | Impôts sur les bénéfices | HK | **– 126 000** |

## 3. Écritures comptables

Aucune écriture : il s'agit de **présentation**. Pour mémoire, l'écriture de constatation du CIR telle que passée par TechNova :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2025 | OD | 444 | État – impôt sur les bénéfices | CIR 2025 (déclaration 2069-A) | 126 000,00 | |
| 31/12/2025 | OD | 695 | Impôts sur les bénéfices | CIR 2025 imputé sur l'IS | | 126 000,00 |
| | | | | **Totaux** | **126 000,00** | **126 000,00** |

## 4. Points d'attention / pièges de mapping

| Piège | Conséquence si mal paramétré | Bon traitement |
|---|---|---|
| **512-CC créditeur** compensé avec BNP | Disponibilités 636 500 au lieu de 640 000, dette bancaire minorée | Actif CF 640 000 ; passif DU (+ 3 500, mention « concours bancaires courants ») |
| **467** mappé globalement | 700 € net en autres créances, 1 800 € de dette disparus | 467-D en BZ, 467-C en EA |
| **1674 avance conditionnée** mappée en dettes financières (DV) | Capitaux propres et endettement faussés | Rubrique « Autres fonds propres » (DN). *Selon les conditions de remboursement, certains la présentent en dettes : être cohérent avec l'annexe.* |
| **139** au débit | Si mappée seule à l'actif : erreur grossière | Net 131 – 139 en DJ |
| **232 (en cours)** | Oubliée car non amortie | AJ (autres immobilisations incorporelles) — certaines versions de la liasse ont une ligne spécifique : vérifier |
| **721 production immobilisée** | Comptée dans le CA | FN, hors CA ; elle « neutralise » les salaires des développeurs activés |
| **706-UE** | Tout en « France » | FH (exportations et livraisons intracommunautaires) : recoupé par l'administration avec les CA3 (prestations B2B UE : autoliquidation par le preneur) |
| **476 / 1515** | 476 oublié (pas de classe « bilan » reconnue) | Écart de conversion actif en bas d'actif ; provision pour perte de change en DP et dotation en GQ |
| **695 créditeur** | Case IS négative refusée par certains logiciels → mapping « forcé » en produit exceptionnel | HK négatif admis. **Alternative comptable** : le CIR peut être présenté en subvention d'exploitation (74), choix de méthode à appliquer de façon permanente et à expliquer en annexe. |
| **658 / 747** | Restés mappés en exceptionnel (ancienne nomenclature 6712 / 777) | Nomenclature 2025 : pénalités en exploitation ; vérifier la place de la quote-part de subvention dans le millésime |
| **Comptes non mappés** | Total liasse ≠ total balance | Contrôle bloquant (voir § 5) |

**Contrôle de cohérence sur l'extrait** : la somme des montants classés (actif net + passif + charges – produits) doit se retrouver à l'identique dans la balance ; ici chaque compte de l'extrait est affecté à **une et une seule** rubrique.

## 5. Ce qu'un senior ferait en plus

**Réponse à Émilie Roux :**
> « Bonjour Émilie, nous ne pouvons pas compenser les deux banques : le principe de non-compensation impose de présenter le solde BNP en disponibilités (640 000 €) et le découvert Crédit Coopératif en dettes auprès des établissements de crédit (3 500 €). L'impact est nul sur les capitaux propres mais il est visible pour un lecteur des comptes (et un investisseur dans une prochaine levée regardera ce poste). Pour le CIR, la présentation en diminution de l'IS est admise et c'est celle retenue depuis l'origine : on la conserve par permanence des méthodes, avec une mention en annexe. Bien cordialement. »

**Contrôles automatiques à paramétrer :**
1. **Comptes non affectés** : alerte bloquante si un compte de la balance n'a pas de rubrique.
2. **Équilibres** : total actif net = total passif ; résultat 2051 (DI) = résultat 2053 (HN) = solde des classes 6 et 7.
3. **Sens des soldes** : mapping conditionnel au sens (512, 467, 444, 455, 4456/4457, comptes de tiers auxiliaires).
4. **Recoupements** : CA 2052 / CA déclaré sur les CA3 de l'année ; dotations 2052 = 2055 ; capital 2051 = Kbis ; résultat fiscal 2058-A cohérent avec la 2572.
5. **Variations N/N-1** par rubrique au-delà d'un seuil → justification obligatoire.

## 6. Références

- Code de commerce, art. L. 123-19 (non-compensation) ; modèles de bilan et de compte de résultat du PCG.
- PCG : avances conditionnées (« autres fonds propres »), subventions d'investissement, frais de développement (option d'activation), écarts de conversion.
- CGI, art. 244 quater B (crédit d'impôt recherche) ; art. 53 A et art. 223 (obligations déclaratives : déclaration de résultat et tableaux annexes).
- Notice de la liasse fiscale du régime réel normal (2050 à 2059) du millésime en vigueur.
