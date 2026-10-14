# Corrigé E01-06 — Contrôler un FEC avant de le remettre au vérificateur

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-06](../exercices/E01-06_controle-fec-technova.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### 1.1 Les règles de forme (question 1)

Le FEC (LPF art. L. 47 A-I ; format fixé par l'art. A. 47 A-1 du LPF ; commentaires BOFiP, contrôle fiscal – FEC) :

| Élément | Règle |
|---|---|
| Nom du fichier | `SIRENFECAAAAMMJJ` (date de clôture) → `879654321FEC20251231` ✓ |
| Contenu | **Toutes** les écritures de l'exercice, y compris les à-nouveaux, **après** les opérations d'inventaire, classées par ordre chronologique de validation |
| Colonnes | 18 champs dans l'ordre : JournalCode, JournalLib, EcritureNum, EcritureDate, CompteNum, CompteLib, CompAuxNum, CompAuxLib, PieceRef, PieceDate, EcritureLib, Debit, Credit, EcritureLet, DateLet, ValidDate, Montantdevise, Idevise |
| Dates | Format **AAAAMMJJ**, sans séparateur |
| Montants | Séparateur décimal virgule, pas de séparateur de milliers |
| Numérotation | **EcritureNum** continu et chronologique par journal (ou global), sans rupture |
| Écritures | Chaque écriture **équilibrée** ; EcritureDate et ValidDate **dans l'exercice ou à la clôture**, ValidDate ≥ EcritureDate |
| Tiers | Les comptes collectifs (401, 411) doivent comporter le compte auxiliaire (CompAuxNum / CompAuxLib) |
| Pièce | PieceRef et PieceDate renseignés (lien avec la pièce justificative) |
| Libellé | EcritureLib suffisamment explicite pour identifier l'opération |
| Devises | Montantdevise renseigné ⇒ Idevise renseigné (code ISO : USD) |

L'administration met à disposition un outil gratuit de test de conformité du FEC (« Test Compta Demat ») : à passer **systématiquement** avant remise.

### 1.2 Les anomalies (questions 2 et 3)

**(a) Anomalies de format**

| # | Ligne(s) | Anomalie | Correctif |
|---|---|---|---|
| F1 | AC000312 | EcritureDate au format `15-12-2025` au lieu de `20251215` | Paramétrage de l'export (format de date du champ) |
| F2 | AC000312 | Montantdevise = 5000,00 **sans Idevise** | Renseigner « USD » dans la fiche fournisseur / paramétrage de l'export |
| F3 | AC000311 | **Montants négatifs** (– 320,00 au débit du 604 et au crédit du 401) : un avoir saisi « en négatif » | Paramétrer l'export pour inverser le sens des montants négatifs (débit ↔ crédit) et proscrire la saisie en négatif ; à défaut, les outils de contrôle signalent l'anomalie et la lecture du fichier est faussée |

**(b) Anomalies d'intégrité / de piste d'audit**

| # | Ligne(s) | Anomalie | Gravité | Correctif |
|---|---|---|---|---|
| I1 | VE000123 | Écriture **déséquilibrée** : débit 1 200,00 ; crédits 1 000,00 + 180,00 = 1 180,00. L'ERP affiche 200,00 € de TVA → le fichier exporté ne reflète pas la comptabilité | **Très grave** : un FEC déséquilibré est rejeté ; il fait douter de toute la comptabilité | Remonter à l'éditeur ; régénérer l'export ; contrôler que le total des débits = total des crédits = balance |
| I2 | VE000124 absent | **Rupture de numérotation** : une facture a été « supprimée » dans l'ERP | **Grave** : en matière de facturation, une facture émise ne se supprime pas ; si elle avait été envoyée au client, il fallait un avoir | Vérifier si la facture a été transmise au client. Si elle n'a jamais été validée/émise et que l'ERP numérote les écritures à la validation, documenter l'explication (note écrite pour le vérificateur). Corriger la procédure : annulation par avoir uniquement |
| I3 | AC000311 | **ValidDate (01/12/2025) antérieure à EcritureDate (10/12/2025)** et à PieceDate | Grave : une écriture ne peut être validée avant d'exister ; suggère une manipulation de dates | Analyser le paramétrage des dates de validation de l'ERP |
| I4 | AC000310 | **CompAuxNum / CompAuxLib vides** sur le 401 : fournisseur non identifiable | Moyenne | Affecter le compte auxiliaire ; contrôler toutes les lignes 401/411 sans auxiliaire |
| I5 | AC000310 | EcritureLib « Facture fournisseur » : libellé non explicite | Faible à moyenne | Libellé type : « [Fournisseur] F n° [x] [objet] » |
| I6 | BQ000845 | **PieceRef et PieceDate vides** | Moyenne : pas de lien avec un justificatif | Référencer le relevé bancaire (ex. RB-2025-12) |
| I7 | OD000077 | **EcritureDate 05/01/2026**, hors exercice, pour les dotations 2025 ; ValidDate 05/01/2026 | Moyenne : les écritures d'inventaire doivent être datées au plus tard de la clôture (31/12/2025) | Les écritures d'inventaire se datent au 31/12 ; la ValidDate peut être postérieure à la clôture (validation lors des travaux de clôture) mais l'EcritureDate doit appartenir à l'exercice |
| I8 | BQ000845 | ValidDate 15/01/2026 > clôture : acceptable en soi (validation pendant la clôture), à condition que l'EcritureDate soit dans l'exercice ✓ | Aucune | — |

**(c) Anomalies de fond révélées par le fichier**

| # | Ligne(s) | Anomalie | Conséquence |
|---|---|---|---|
| C1 | VE000122 | Abonnement **01/01/2026 – 31/12/2026** facturé le 15/12/2025 et intégralement en produit 2025 | **Produit constaté d'avance** de 12 000,00 € omis → résultat 2025 surévalué de 12 000,00 € |
| C2 | BQ000845 | Virement de 8 500,00 € laissé en **471 compte d'attente** à la clôture, alors qu'il solde la facture FA25-1150 de Logistik Alpes | Bilan 2025 faux (411 et 471 surévalués de 8 500,00 €) ; un 471 non soldé à la clôture est un **signal d'alerte** pour un vérificateur |
| C3 | VE000123 | Si l'ERP a bien 200,00 € de TVA (1 000,00 × 20 %), c'est l'export qui est faux ; sinon la TVA collectée a été minorée de 20,00 € | À vérifier dans le logiciel source et la CA3 de décembre |
| C4 | AC000312 | Facture NimbusCloud en USD : **contrôler l'autoliquidation de la TVA** (prestation de services d'un prestataire hors UE) : aucune ligne 4452 / 445662 dans l'écriture | Vérifier que l'autoliquidation a été passée (éventuellement par une OD) et déclarée — sinon rappel de TVA (en principe neutre, mais sanctionnable) |

## 2. Calculs (détaillés, chaque montant justifié)

- VE000123 : 1 000,00 × 20 % = **200,00 €** ; débit 1 200,00 – crédits (1 000,00 + 180,00) = **20,00 € d'écart**.
- VE000122 : 12 000,00 € HT pour 12 mois de 2026 ; part 2025 = 0 mois ⇒ **PCA = 12 000,00 €** (le PCA ne porte que sur le HT ; la TVA de 2 400,00 € suit ses propres règles : prestation de services ⇒ TVA exigible à l'**encaissement**, ici le 10/01/2026 d'après le lettrage, sauf option pour les débits — à vérifier sur la CA3 de janvier 2026).
- AC000312 : 5 000,00 USD → 4 291,85 € ⇒ taux implicite 5 000,00 / 4 291,85 = **1,1650 USD pour 1 €**.
- Total des écritures de l'extrait : débits 49 411,85 € ; crédits 49 391,85 € → **écart de 20,00 €**, qui provient uniquement de VE000123 (les montants négatifs se compensent).

## 3. Écritures comptables

**A. Écritures qui auraient dû être passées au 31/12/2025** (pour comprendre l'erreur)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2025 | BQ | 471000 | Compte d'attente | Affectation vir. Logistik Alpes – FA25-1150 | 8 500,00 | |
| 31/12/2025 | BQ | 411000 (C0012) | Clients – Logistik Alpes | Affectation vir. Logistik Alpes – FA25-1150 | | 8 500,00 |
| 31/12/2025 | OD | 706100 | Abonnements SaaS | PCA Batiplan FA25-1201 abonnement 2026 | 12 000,00 | |
| 31/12/2025 | OD | 487000 | Produits constatés d'avance | PCA Batiplan FA25-1201 abonnement 2026 | | 12 000,00 |
| | | | | **Totaux** | **20 500,00** | **20 500,00** |

**B. Ce que l'on fait aujourd'hui (comptes 2025 approuvés)**

- **On ne modifie pas le FEC sur le fond.** Le FEC doit être le reflet exact de la comptabilité telle qu'elle a été arrêtée et approuvée. On corrige **uniquement les défauts d'export** (formats, Idevise, sens des montants, équilibre de VE000123 si l'ERP est juste) en **régénérant** le fichier depuis l'ERP. « Retoucher » à la main un FEC remis à l'administration serait une faute grave.
- **Le 471 a été repris en à-nouveau 2026** : on l'affecte dans la comptabilité 2026 (écriture de bilan, sans impact sur le résultat) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 09/10/2026 | OD | 471000 | Compte d'attente | Affectation vir. 31/12/2025 Logistik Alpes – FA25-1150 | 8 500,00 | |
| 09/10/2026 | OD | 411000 (C0012) | Clients – Logistik Alpes | Affectation vir. 31/12/2025 Logistik Alpes – FA25-1150 | | 8 500,00 |
| | | | | **Totaux** | **8 500,00** | **8 500,00** |

- **Le PCA omis** : l'erreur « se retourne » d'elle-même — le résultat 2025 est surévalué de 12 000,00 €, le résultat 2026 sera sous-évalué d'autant (le produit 2026 a déjà été comptabilisé en 2025). Aucune écriture n'est à passer en 2026, mais le point doit être **documenté** : (1) information du vérificateur si la question est posée (TechNova a payé « trop tôt », ce qui n'est pas une insuffisance de déclaration) ; (2) incidence sur le **déficit reportable** ou l'IS 2025 — à chiffrer avec Hélène Ferrand ; (3) correction de la procédure de clôture pour 2026 (tableau des abonnements annuels à étaler).

## 4. Points d'attention / pièges

- **Un FEC qui « passe » à l'outil de test peut quand même être faux sur le fond** (C1, C2). Le test de conformité ne remplace pas la révision.
- **ValidDate** : l'administration s'en sert pour repérer les écritures passées tardivement ou modifiées. Une ValidDate antérieure à l'EcritureDate est incohérente.
- **Les ruptures de numérotation** sont l'une des premières choses que regarde un vérificateur ; chaque trou doit pouvoir être expliqué par écrit.
- **Le compte 471 à la clôture** : doit être à zéro. C'est un indicateur de qualité de la tenue.
- **Facture en devise** : l'écriture doit aussi permettre de vérifier l'autoliquidation (M02).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Risques (question 5).** Défaut de présentation d'un FEC conforme : **amende** prévue à l'art. 1729 D du CGI (forfait par exercice ou, si plus élevée, majoration proportionnelle aux droits rappelés — montants à vérifier) ; en cas de comptabilité jugée **non probante** (écritures déséquilibrées, ruptures de séquence, dates incohérentes), le vérificateur peut l'écarter et **reconstituer** le chiffre d'affaires ; mauvaise impression dès la première intervention, qui oriente tout le contrôle.

**Message à Émilie Roux :**

> Bonjour Émilie,
>
> Merci pour l'extrait. Avant toute remise, il faut régénérer le FEC : nous avons relevé des défauts d'export (une date au format JJ-MM-AAAA, une devise sans code, des montants négatifs) et surtout **une écriture déséquilibrée** dans le fichier (VE000123) alors qu'elle est juste à l'écran : c'est un problème d'export à remonter en urgence à l'éditeur.
>
> D'autres points sont de fond et seront discutés avec Hélène : la rupture VE000124 (pouvez-vous nous confirmer par écrit que la facture n'a jamais été émise ?), les dotations datées du 05/01/2026, le virement de 8 500 € resté en compte d'attente, et l'abonnement Batiplan 2026 comptabilisé en totalité en 2025.
>
> Merci de nous renvoyer le fichier complet régénéré : nous le passerons à l'outil de test de l'administration et nous ferons nos contrôles (équilibre, continuité, balance) avant la première intervention.

**Contrôles complémentaires sur le fichier complet** : équilibre global et par écriture ; total du FEC = balance de clôture ; continuité des EcritureNum ; recherche des EcritureDate hors exercice ; comptes 401/411 sans auxiliaire ; lignes sans PieceRef ; comptes d'attente non soldés ; écritures passées après la clôture (ValidDate tardives) sur des comptes de résultat.

**Documentation** : conserver dans le dossier « Contrôle fiscal TechNova » le FEC remis (empreinte du fichier, date de remise), le rapport de l'outil de test et la note d'explication des anomalies.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- LPF art. L. 47 A-I : obligation de remettre le FEC en cas de vérification d'une comptabilité informatisée.
- LPF art. A. 47 A-1 : format et contenu du FEC.
- BOFiP, contrôle fiscal – vérification des comptabilités informatisées (FEC).
- CGI art. 1729 D : sanction du défaut de présentation conforme.
- Code de commerce art. L. 123-14 et R. 123-172 et suivants : régularité, caractère définitif des écritures, chronologie.
- PCG : comptes 471 (à solder à la clôture) et 487 (produits constatés d'avance) ; correction d'erreurs (règlement ANC 2022-06).
