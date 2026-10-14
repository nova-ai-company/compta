# Corrigé E05-09 — Le compte séquestre d'ImmoPlus : fonds des mandants et honoraires

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-09](../exercices/E05-09_fonds-mandants-immoplus.md)

## 1. Analyse

### 1.1 Mandataire, pas propriétaire des fonds
ImmoPlus agit comme **mandataire** des propriétaires (mandat de gestion). Les loyers qu'elle encaisse appartiennent aux **mandants** dès l'encaissement ; les dépôts de garantie appartiennent aux bailleurs (et sont dus, à terme, aux locataires). L'agence ne fait que **détenir** ces fonds sur un compte spécial, couvert par sa **garantie financière** (loi n° 70-9 du 2 janvier 1970, dite loi Hoguet, et son décret d'application n° 72-678 du 20 juillet 1972).

Conséquences :
- **aucun** loyer, charge locative ou dépôt ne transite par le compte de résultat de l'agence ;
- les dépenses réglées pour le compte d'un propriétaire (plombier du lot 47) sont **à la charge du propriétaire** ;
- le **seul produit** de l'agence dans ces flux est l'**honoraire de gestion** (7 % HT des sommes encaissées), soumis à TVA.

### 1.2 Méthode de tenue
La méthode retenue (et la plus répandue) : la **comptabilité mandants** est tenue dans le logiciel de gestion (comptes individuels propriétaires et locataires, registre des fonds) ; la comptabilité générale d'ImmoPlus n'enregistre que les **honoraires** et ses propres opérations. Certaines agences intègrent le compte séquestre à leur bilan avec une dette symétrique envers les mandants (compte de tiers 467) : cette présentation est admise si elle est permanente et décrite en annexe ; elle ne doit **jamais** faire passer ces fonds par le compte de résultat.

### 1.3 Représentation des fonds
À tout moment, la trésorerie du compte séquestre doit être **au moins égale** au total des fonds dus aux mandants et aux tiers (pièce 4). C'est le contrôle n° 1 du garant financier et de la commission de contrôle.

## 2. Calculs

### 2.1 Honoraires de septembre
- 186 400,00 × 7 % = **13 048,00 € HT**
- TVA 20 % : 2 609,60 €
- TTC : **15 657,60 €** = montant viré le 15/09 ✔

(L'assiette retenue par le mandat est « loyers et charges encaissés » ; les dépôts de garantie ne sont pas des sommes rémunérant le mandant et sont exclus.)

### 2.2 Représentation des fonds au 30/09/2026

| | Montant |
|---|---|
| Fonds dus aux mandants et aux tiers (pièce 4) | 224 782,40 |
| Solde du compte séquestre | 218 782,40 |
| **Insuffisance de représentation** | **6 000,00** |

L'écart correspond exactement au virement « URSSAF agence » du 21/09. Contrôle : 224 782,40 = solde séquestre **avant** ce virement ✔. Le séquestre est donc juste à l'euro près, hors l'utilisation irrégulière.

### 2.3 Impact de la saisie de Lou sur le résultat de l'agence

| Compte | Effet sur le résultat |
|---|---|
| 706200 Loyers | + 186 400,00 |
| 615 Entretien | – 640,00 |
| 6228 Reversements | – 162 300,00 |
| Honoraires de gestion non comptabilisés | – 13 048,00 (manquant) |
| **Résultat faussé de** | **+ 23 460,00 – 13 048,00 = + 10 412,00** et chiffre d'affaires surévalué de **173 352,00 €** (186 400 au lieu de 13 048) |

## 3. Écritures comptables

**Étape 1 — Contre-passation de toutes les écritures de Lou sur le compte séquestre :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 706200 | Loyers encaissés (compte ouvert à tort) | Contre-passation loyers mandants sept. | 186 400,00 |  |
| 30/09/2026 | OD | 512SEQ | Banque — compte séquestre (à sortir de la compta agence) | Contre-passation loyers mandants |  | 186 400,00 |
| 30/09/2026 | OD | 165 | Dépôts et cautionnements reçus | Contre-passation DG reçus pour compte des bailleurs | 4 800,00 |  |
| 30/09/2026 | OD | 512SEQ | Banque — compte séquestre | Contre-passation DG reçus |  | 4 800,00 |
| 30/09/2026 | OD | 512SEQ | Banque — compte séquestre | Contre-passation restitution DG | 2 200,00 |  |
| 30/09/2026 | OD | 165 | Dépôts et cautionnements reçus | Contre-passation restitution DG |  | 2 200,00 |
| 30/09/2026 | OD | 512SEQ | Banque — compte séquestre | Contre-passation facture plombier lot Roux | 640,00 |  |
| 30/09/2026 | OD | 615 | Entretien et réparations | Contre-passation facture plombier (charge du propriétaire) |  | 640,00 |
| 30/09/2026 | OD | 512SEQ | Banque — compte séquestre | Contre-passation reversements propriétaires | 162 300,00 |  |
| 30/09/2026 | OD | 6228 | Rémunérations d'intermédiaires — divers | Contre-passation reversements propriétaires |  | 162 300,00 |
| 30/09/2026 | OD | 512SEQ | Banque — compte séquestre | Contre-passation virement honoraires (côté séquestre) | 15 657,60 |  |
| 30/09/2026 | OD | 580 | Virements internes | Contre-passation virement honoraires |  | 15 657,60 |
| 30/09/2026 | OD | 512SEQ | Banque — compte séquestre | Contre-passation virement « URSSAF agence » (côté séquestre) | 6 000,00 |  |
| 30/09/2026 | OD | 580 | Virements internes | Contre-passation virement 6 000 |  | 6 000,00 |
| | | | | **Totaux** | **377 997,60** | **377 997,60** |

Après cette étape : 512SEQ, 706200, 165, 615 (pour ce montant) et 6228 sont à zéro. Il reste au 580 un **solde créditeur** de 21 657,60 € : ce sont les deux virements **reçus sur le compte de l'agence**, qui, eux, sont bien des opérations de l'agence et doivent être qualifiés.

**Étape 2 — Qualification des sommes reçues sur le compte de l'agence :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 580 | Virements internes | Honoraires de gestion sept. reçus du séquestre | 15 657,60 |  |
| 30/09/2026 | OD | 706100 | Honoraires de gestion locative | Honoraires de gestion sept. (7 % HT des loyers encaissés) |  | 13 048,00 |
| 30/09/2026 | OD | 44571 | TVA collectée | Honoraires de gestion sept. |  | 2 609,60 |
| 30/09/2026 | OD | 580 | Virements internes | Fonds mandants virés à tort sur le compte agence | 6 000,00 |  |
| 30/09/2026 | OD | 4678 | Mandants — fonds à restituer au compte séquestre | Fonds mandants utilisés pour l'URSSAF agence |  | 6 000,00 |
| | | | | **Totaux** | **21 657,60** | **21 657,60** |

> En pratique, les honoraires sont justifiés par les **comptes rendus de gérance** (une facture/note d'honoraires par mandant, édités par le logiciel) : la comptabilité de l'agence peut enregistrer une écriture récapitulative mensuelle appuyée sur l'état des honoraires du logiciel. Au 30/09, le 580 est soldé ✔.

**Étape 3 — Restitution le 02/10/2026 :**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/10/2026 | BQ | 4678 | Mandants — fonds à restituer au compte séquestre | Restitution des 6 000 € au compte séquestre | 6 000,00 |  |
| 02/10/2026 | BQ | 512AG | Banque — compte courant agence | Restitution au compte séquestre |  | 6 000,00 |
| | | | | **Totaux** | **6 000,00** | **6 000,00** |

Si la clôture intervenait avant la restitution, la dette de 6 000 € envers les mandants (4678) figurerait au bilan de l'agence, et la situation serait à décrire dans le dossier de révision.

## 4. Points d'attention / pièges

### Le virement de 6 000 €
- **Ce n'est pas un « prêt » de trésorerie** : ce sont les fonds des propriétaires et des locataires. Leur utilisation pour les besoins propres de l'agence est interdite par la réglementation Hoguet (les fonds détenus pour le compte de tiers ne peuvent servir qu'à l'exécution des mandats).
- **Risques** :
  - **garant financier** : l'insuffisance de représentation des fonds, même temporaire, peut conduire à la **suspension ou au retrait de la garantie**, et donc à l'impossibilité d'exercer (la carte professionnelle G suppose une garantie) ;
  - **disciplinaire** : sanctions par la commission de contrôle des activités de transaction et de gestion immobilières ;
  - **pénal** : l'utilisation de fonds remis à titre précaire peut caractériser un **abus de confiance** (art. 314-1 du Code pénal), indépendamment de la restitution ultérieure ;
  - **responsabilité du gérant** à l'égard des mandants.
- « Les propriétaires n'ont rien vu » n'est pas un argument : le registre et le rapprochement mandants le montrent immédiatement, et un contrôle du garant aussi.

### Les autres pièges
- **Ne jamais intégrer un relevé de compte de tiers dans le journal de banque de l'agence** sans méthode : c'est l'erreur de Lou, qui a gonflé le CA de 173 352 €.
- **Dépense pour un propriétaire** (plombier) : imputée au compte du propriétaire dans la comptabilité mandants, jamais en 615 chez l'agence.
- **Dépôts de garantie** : ils ne sont pas au passif de l'agence (165) lorsqu'ils sont détenus pour le compte des bailleurs ; ils figurent dans la comptabilité mandants.
- **Honoraires oubliés** : en revanche, l'agence **doit** comptabiliser ses honoraires, avec la TVA — la confusion de Lou les avait fait disparaître.
- **Autres fonds de tiers** à surveiller chez ImmoPlus : séquestres de transaction (dépôts reçus à la signature d'un compromis), si l'agence est habilitée à les recevoir.

## 5. Ce qu'un senior ferait en plus

**Entretien avec Frédéric Blanc (Hélène Ferrand et vous) — points à aborder :**
1. Le virement du 21/09 est **interdit** et crée une insuffisance de représentation des fonds de 6 000 € : restitution **immédiate** (prévue le 02/10 : obtenir l'avis d'opéré).
2. Risques : garant, carte professionnelle, abus de confiance. Ne pas recommencer, même « pour 3 jours ».
3. La vraie question est la **trésorerie de l'agence** : si l'URSSAF ne peut être payée sans les fonds des mandants, il faut un prévisionnel de trésorerie, une demande de délai à l'URSSAF, ou une ligne de crédit — le cabinet peut aider.
4. Les honoraires de gestion doivent être prélevés **uniquement** sur la base des comptes rendus de gérance, au taux du mandat.
5. Remerciement pour le « super mois » : le vrai CA de septembre est de 13 048 € d'honoraires de gestion (+ transactions éventuelles), pas 186 400 €.

**Contrôles à mettre en place :**
- **Rapprochement mensuel** : solde du compte séquestre ↔ total des fonds dus (état du logiciel) → écart = 0, documenté et signé. À conserver pour le garant.
- Contrôle de cohérence : honoraires = 7 % HT × encaissements de la période.
- Règle d'import : le relevé du séquestre ne s'importe **jamais** dans le journal de banque de l'agence ; seuls les virements reçus sur le compte agence sont comptabilisés (580 / 706100 + 44571).
- Formation de Lou sur les fonds de tiers (et inscription de ce point dans la fiche permanente du dossier).

**Documentation** : note au dossier sur l'incident du 21/09 (constat, entretien, restitution). Selon la gravité et la répétition, Hélène Ferrand appréciera les suites à donner dans le cadre de la mission (obligations de vigilance du cabinet, notamment au titre de la lutte contre le blanchiment).

## 6. Références
- Loi n° 70-9 du 2 janvier 1970 (loi Hoguet) et décret n° 72-678 du 20 juillet 1972 : garantie financière, compte spécial, registres, représentation des fonds.
- Code pénal, art. 314-1 (abus de confiance).
- CGI, art. 256 et 266 (honoraires de gestion soumis à la TVA sur leur montant).
- PCG : comptes 580, 706, 44571, 467 ; principe de non-compensation et image fidèle (C. com., art. L. 123-14).
