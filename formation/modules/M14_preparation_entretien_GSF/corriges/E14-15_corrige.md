# Corrigé E14-15 — Journal de paie mensuel d'un établissement : comptabiliser et contrôler 421, 425, 431 avec la DSN

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-15](../exercices/E14-15_journal-paie-etablissement-controle-421-431.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Cohérence du journal
- Brut : 52 480,00 + 3 260,00 + 1 120,00 + 1 940,00 − 4 860,00 + 1 580,00 = **55 520,00 €** ✓.
- Cotisations salariales : 8 994,24 + 2 442,88 + 777,28 = 12 214,40 €.
- Net avant impôt : 55 520,00 − 12 214,40 + 1 360,00 + 980,00 + 2 870,40 = **48 516,00 €** ✓.
- Net à payer : 48 516,00 − 1 410,30 − 3 200,00 = **43 905,70 €** ✓.
- Écriture d'interface : débits 76 109,44 € = crédits 76 109,44 € ✓ ; 6411 = brut hors prime de salissure (55 520,00 − 1 120,00 = 54 400,00) ; 6414 = panier + transport (2 340,00).

### Question 2 — IJSS subrogées
En subrogation, l'employeur **maintient** le salaire et **avance** au salarié les IJSS ; la CPAM les lui rembourse ensuite. Le brut comprend seulement la part employeur (salaire − absence + complément) ; les IJSS nettes sont ajoutées après le net : elles ne sont **pas une charge** de GSF Riviera mais une **créance sur la CPAM** → **D 4387** (et non 6411). À l'encaissement : D 512 / C 4387. Depuis le PCG modifié par le règlement ANC n° 2022-06, les comptes de transfert de charges (791) sont supprimés : si des IJSS sont reçues **après** que le salaire maintenu a été entièrement passé en charge, on les porte **en diminution de la charge de personnel** (6411 ou une subdivision), jamais en 791.
Contrôle utile : le 4387 doit se solder au fil des paiements de la CPAM ; un solde ancien = IJSS non perçues (arrêt non transmis, attestation de salaire manquante) → relance du service paie.

### Questions 3 à 5 — Les trois contrôles
- **421** : il doit être soldé par les virements, sauf rejets identifiés.
- **425** : il doit retomber à zéro après déduction des acomptes ; un reliquat = acompte non récupéré.
- **431 / DSN** : le crédit 431 de la paie doit être égal au montant URSSAF déclaré en DSN. Ici 18 432,64 € vs 19 543,04 € : écart **1 110,40 €** = **versement mobilité**, que l'interface a crédité en 447 alors qu'il est déclaré et payé à l'URSSAF via la DSN. Erreur de **paramétrage** du compte de tiers, pas de calcul.

## 2. Calculs (détaillés, chaque montant justifié)

| Contrôle | Calcul | Résultat |
|---|---|---|
| 421 au 30/09 après virement | 43 905,70 − 43 905,70 | 0,00 |
| 421 au 02/10 après rejet | + 612,35 (retour) | 612,35 créditeur (dette envers Mme Costa) |
| 421 au 05/10 | 612,35 − 612,35 | 0,00 ✓ |
| 425 avant paie | 150,00 (août) + 3 200,00 (15/09) | 3 350,00 débiteur |
| 425 après paie | 3 350,00 − 3 200,00 | **150,00 débiteur** ✗ |
| 431 paie | 8 994,24 + 9 438,40 | 18 432,64 |
| 431 DSN | | 19 543,04 |
| Écart | 19 543,04 − 18 432,64 | **1 110,40** = versement mobilité (55 520,00 × 2 %) |
| 4371 retraite | 2 442,88 + 3 664,32 | 6 107,20 |
| 4372 mutuelle / prévoyance | 777,28 + 1 165,92 | 1 943,20 |
| **Coût employeur** | brut 55 520,00 + indemnités 2 340,00 + patronal 9 438,40 + 3 664,32 + 1 165,92 + VM 1 110,40 | **73 239,04 €** |
| Coût moyen par salarié | 73 239,04 / 40 | 1 830,98 € |
| Coût horaire moyen | 73 239,04 / 4 286 h | 17,09 € |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/09/2026 | BQ | 425 | Personnel – avances et acomptes | Acomptes 09/2026 Nice | 3 200,00 | |
| 15/09/2026 | BQ | 512 | Banque | Acomptes 09/2026 Nice | | 3 200,00 |
| 30/09/2026 | OD-PAIE | 6411 | Salaires, appointements | Paie 09/2026 Nice – brut hors primes | 54 400,00 | |
| 30/09/2026 | OD-PAIE | 6413 | Primes et gratifications | Paie 09/2026 Nice – prime de salissure | 1 120,00 | |
| 30/09/2026 | OD-PAIE | 6414 | Indemnités et avantages divers | Paie 09/2026 Nice – paniers + transport | 2 340,00 | |
| 30/09/2026 | OD-PAIE | 4387 | Organismes sociaux – produits à recevoir (IJSS subrogation) | IJSS nettes avancées 09/2026 (7 salariés) | 2 870,40 | |
| 30/09/2026 | OD-PAIE | 6451 | Cotisations à l'URSSAF | Paie 09/2026 Nice – patronal URSSAF | 9 438,40 | |
| 30/09/2026 | OD-PAIE | 6453 | Cotisations aux caisses de retraite | Paie 09/2026 Nice – patronal retraite | 3 664,32 | |
| 30/09/2026 | OD-PAIE | 6452 | Cotisations aux mutuelles et à la prévoyance | Paie 09/2026 Nice – patronal mutuelle/prév. | 1 165,92 | |
| 30/09/2026 | OD-PAIE | 6331 | Versement mobilité | Paie 09/2026 Nice – VM | 1 110,40 | |
| 30/09/2026 | OD-PAIE | 431 | Sécurité sociale (URSSAF) | Paie 09/2026 Nice – sal. + pat. URSSAF | | 18 432,64 |
| 30/09/2026 | OD-PAIE | 4371 | Caisses de retraite complémentaire | Paie 09/2026 Nice – retraite | | 6 107,20 |
| 30/09/2026 | OD-PAIE | 4372 | Mutuelle / prévoyance | Paie 09/2026 Nice – mutuelle/prév. | | 1 943,20 |
| 30/09/2026 | OD-PAIE | 4421 | État – prélèvement à la source | Paie 09/2026 Nice – PAS | | 1 410,30 |
| 30/09/2026 | OD-PAIE | 425 | Personnel – avances et acomptes | Paie 09/2026 Nice – reprise acomptes | | 3 200,00 |
| 30/09/2026 | OD-PAIE | 421 | Personnel – rémunérations dues | Paie 09/2026 Nice – net à payer | | 43 905,70 |
| 30/09/2026 | OD-PAIE | 447 | Autres impôts, taxes et versements assimilés | Paie 09/2026 Nice – VM (paramétrage) | | 1 110,40 |
| 30/09/2026 | OD | 447 | Autres impôts, taxes et versements assimilés | Reclass. VM 09/2026 Nice – déclaré en DSN URSSAF | 1 110,40 | |
| 30/09/2026 | OD | 431 | Sécurité sociale (URSSAF) | Reclass. VM 09/2026 Nice – déclaré en DSN URSSAF | | 1 110,40 |
| 30/09/2026 | BQ | 421 | Personnel – rémunérations dues | Virement salaires 09/2026 Nice | 43 905,70 | |
| 30/09/2026 | BQ | 512 | Banque | Virement salaires 09/2026 Nice | | 43 905,70 |
| 02/10/2026 | BQ | 512 | Banque | Retour virement salaire A. Costa (compte clos) | 612,35 | |
| 02/10/2026 | BQ | 421 | Personnel – rémunérations dues | Retour virement salaire A. Costa (compte clos) | | 612,35 |
| 05/10/2026 | BQ | 421 | Personnel – rémunérations dues | Virement salaire 09/2026 A. Costa nouvel IBAN | 612,35 | |
| 05/10/2026 | BQ | 512 | Banque | Virement salaire 09/2026 A. Costa nouvel IBAN | | 612,35 |
| | | | | **Totaux** | **125 550,24** | **125 550,24** |

> En pratique, la correction 447 → 431 se fait **dans le paramétrage de l'interface** (pour les mois suivants) **et** par une écriture pour septembre, avant le paiement de la DSN le 05/10 (ou le 15/10 selon l'échéance de l'établissement) : le prélèvement URSSAF de 19 543,04 € soldera alors exactement le 431.

## 4. Points d'attention / pièges

- **Question 4 — 425** : solde de **150,00 €** = acompte d'août de M. Silva jamais repris. Ce n'est pas une charge : c'est une créance sur le salarié. On demande au service paie de le **retenir sur la paie d'octobre** (avec information du salarié) ; si le salarié a quitté l'entreprise, on le réclame et, à défaut, la perte relève d'une décision du responsable. Ne pas solder le 425 en 6411.
- **Ne pas confondre** indemnités de frais (panier, transport, exonérées dans les limites) et primes (salissure, ancienneté, soumises) : leur traitement social et comptable diffère, et les primes conventionnelles de la propreté sont un sujet classique de contrôle URSSAF.
- **Rejet de virement** : le 421 redevient créditeur ; on ne repaie qu'après **contrôle** du nouvel IBAN (fraude au changement de RIB salarié — même logique que E14-11).
- **IJSS** : jamais en 791 (supprimé depuis 2025) ; jamais en produit 7xx.
- **Heures complémentaires des temps partiels** : un volume important et récurrent (3 260,00 € ici) peut entraîner une requalification de l'horaire contractuel ; c'est un signal à remonter à l'établissement et aux RH.
- **Provision congés payés** : en clôture mensuelle, la variation de la dette de congés payés (et des charges sociales afférentes) est souvent comptabilisée par le service paie ou la comptabilité ; à vérifier dans la procédure du groupe.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Indicateurs de contrôle de gestion (question 6)** : **coût horaire moyen** (17,09 €) comparé au prix de vente horaire des contrats ; **taux d'heures complémentaires** et **taux d'absentéisme** (absences maladie 4 860,00 € de déductions, 7 salariés en arrêt) ; ratio **intérim / masse salariale** ; **masse salariale / chiffre d'affaires** de l'établissement (le ratio clé de la propreté, activité de main-d'œuvre).

**Tableau de contrôle mensuel paie → comptabilité** (une ligne par établissement) : brut journal = 641x ; 421 soldé (ou rejets listés) ; 425 = 0 ; 431 = DSN URSSAF ; 437x = DSN retraite/prévoyance ; 4421 = PAS déclaré ; 4387 : ancienneté des IJSS à recevoir.

**Message au service paie** : « Paie de septembre Nice : écriture validée. Deux points : (1) le versement mobilité (1 110,40 €) est paramétré vers le 447 dans l'interface alors qu'il est déclaré et payé à l'URSSAF via la DSN : merci de corriger le mapping (je l'ai reclassé pour septembre) ; (2) l'acompte d'août de M. Silva (150,00 €) n'a pas été repris : à retenir en octobre. Le salaire de Mme Costa a été re-viré le 05/10 après contrôle du nouvel IBAN. »

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 641x, 645x, 6331, 421, 425, 431, 437, 4387, 4421 ; règlement ANC n° 2022-06 (suppression des comptes 79).
- Code de la sécurité sociale art. L. 133-5-3 (DSN), R. 323-11 (subrogation de l'employeur dans les IJSS) (*à vérifier*).
- Code du travail art. L. 3245-1 (prescription des salaires), L. 3251-3 (avances en espèces et retenues sur salaire), L. 3123-1 et suivants (temps partiel, heures complémentaires).
- Code général des collectivités territoriales : versement mobilité (taux fixé par l'autorité organisatrice — *à vérifier*).
- Convention collective nationale des entreprises de propreté et services associés (IDCC 3043) : primes et indemnités.
