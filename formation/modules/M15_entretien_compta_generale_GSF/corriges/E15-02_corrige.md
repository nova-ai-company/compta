# Corrigé E15-02 — Rapprochement bancaire complet du mois de septembre

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E15-02](../exercices/E15-02_rapprochement-bancaire-septembre.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Le principe en une phrase

Le relevé et le compte 512 décrivent **le même argent**, vu de deux côtés : un **crédit** sur le relevé correspond à un **débit** au 512, et inversement. Les deux soldes ne sont presque jamais égaux en fin de mois, à cause :
- d'opérations que **la banque a passées et pas encore la comptabilité** (frais, prélèvements, virements reçus) → **on passe une écriture** ;
- d'opérations que **la comptabilité a passées et pas encore la banque** (chèque émis non encaissé, remise déposée tard) → **aucune écriture**, simple décalage de date ;
- d'**erreurs** → on corrige.

### Question 1 — Pointage

**Opérations présentes des deux côtés (pointées, même montant, même sens) :**

| Date relevé | Opération | Montant |
|---|---|---|
| 03/09 | Cabinet Azur Syndic | + 12 600,00 |
| 15/09 | Clinique des Oliviers | + 9 120,00 |
| 18/09 | Chèque n° 0001243 (saisi le 16/09) | − 2 150,00 |
| 25/09 | Locazur LLD | − 1 845,60 |
| 28/09 | Équip'Pro Riviera | − 4 212,00 |

**Opérations non pointées :**

| Côté | Date | Opération | Montant | Nature | Écriture ? |
|---|---|---|---|---|---|
| Relevé seul | 26/09 | Prélèvement Énergie Sud | − 612,00 | non comptabilisé | **Oui** |
| Relevé seul | 29/09 | Virement reçu Syndic Promenade | + 4 560,00 | non comptabilisé | **Oui** |
| Relevé seul | 30/09 | Frais bancaires dont TVA 6,00 | − 36,00 | non comptabilisé | **Oui** |
| Relevé seul | 30/09 | Intérêts débiteurs | − 124,57 | non comptabilisé | **Oui** |
| Les deux, sens opposés | 07/09 | Azur Hygiène 875,00 | relevé : sortie ; 512 : entrée | **erreur de sens** | **Oui** |
| 512 seul | 29/09 | Chèque n° 0001245 émis | − 1 980,00 | pas encore présenté par le fournisseur | Non (décalage) |
| 512 seul | 30/09 | Remise de chèques n° 0098 | + 2 340,00 | créditée le 02/10 | Non (décalage) |

### Question 2 — L'erreur de sens du 07/09

Le 07/09, GSF Riviera a **payé** 875,00 € à son fournisseur : l'argent **sort**, il fallait **créditer** le 512 (et débiter le 401AZH). La saisie a fait l'inverse : 512 au débit, 401AZH au crédit.

Conséquence : le 512 est trop élevé de **2 × 875,00 = 1 750,00 €** — 875,00 € pour annuler l'entrée fictive, plus 875,00 € pour enregistrer la vraie sortie. Même chose côté fournisseur : le 401AZH est trop créditeur de 1 750,00 € (on croit devoir encore la facture, et même plus).

Deux façons de corriger, toutes deux justes :
- **contrepasser** l'écriture fausse (875,00) puis **ressaisir** la bonne (875,00) — c'est la méthode la plus lisible pour un auditeur ;
- passer **une seule écriture de 1 750,00 €** (401AZH au débit, 512 au crédit) — c'est celle retenue ci-dessous, avec un libellé explicite.

### Question 3 — Pourquoi passer une écriture pour certaines opérations et pas pour d'autres ?

On ne passe une écriture que si **la comptabilité a oublié** quelque chose qui s'est réellement produit. Le chèque n° 0001245 et la remise n° 0098 sont **déjà bien comptabilisés** : c'est la banque qui « n'est pas encore au courant ». Si l'on passait une écriture, on compterait l'opération deux fois.

## 2. Calculs (détaillés, chaque montant justifié)

### Question 4 — État de rapprochement au 30/09/2026

**Côté comptabilité (compte 512)**

| Libellé | Montant |
|---|---|
| Solde débiteur du 512 au 30/09 | 55 947,40 |
| − Frais bancaires non comptabilisés | − 36,00 |
| − Intérêts débiteurs non comptabilisés | − 124,57 |
| + Virement Syndic Promenade non comptabilisé | + 4 560,00 |
| − Prélèvement Énergie Sud non comptabilisé | − 612,00 |
| − Correction de l'erreur de sens du 07/09 (2 × 875,00) | − 1 750,00 |
| **Solde comptable corrigé** | **57 984,83** |

**Côté banque (relevé)**

| Libellé | Montant |
|---|---|
| Solde créditeur du relevé au 30/09 | 57 624,83 |
| − Chèque n° 0001245 émis, non encore débité | − 1 980,00 |
| + Remise de chèques n° 0098, créditée le 02/10 | + 2 340,00 |
| **Solde bancaire corrigé** | **57 984,83** |

Les deux soldes corrigés sont **égaux : 57 984,83 €** ✓.

Contrôles :
- 55 947,40 − 36,00 − 124,57 + 4 560,00 − 612,00 − 1 750,00 = 57 984,83.
- 57 624,83 − 1 980,00 + 2 340,00 = 57 984,83.
- Contrôle du relevé : 41 200,00 + 12 600,00 + 9 120,00 + 4 560,00 − 875,00 − 2 150,00 − 1 845,60 − 612,00 − 4 212,00 − 36,00 − 124,57 = 57 624,83 ✓.

**Frais bancaires** : 36,00 € TTC dont 6,00 € de TVA → 30,00 € HT en 627 et 6,00 € en 44566 (le relevé mentionne la TVA ; *conditions de déduction à vérifier selon le justificatif de la banque*).

## 3. Écritures comptables

Question 5 — écritures datées du 30/09/2026 (date du relevé).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | BQ | 627 | Services bancaires et assimilés | Frais tenue de compte et commissions T3 | 30,00 | |
| 30/09/2026 | BQ | 44566 | TVA déductible sur autres biens et services | TVA sur frais bancaires T3 | 6,00 | |
| 30/09/2026 | BQ | 512100 | Banque – Nice | Frais bancaires T3 (relevé 30/09) | | 36,00 |
| 30/09/2026 | BQ | 6616 | Intérêts bancaires et sur opérations de financement | Intérêts débiteurs facilité de caisse août | 124,57 | |
| 30/09/2026 | BQ | 512100 | Banque – Nice | Intérêts débiteurs (relevé 30/09) | | 124,57 |
| 30/09/2026 | BQ | 512100 | Banque – Nice | VIR reçu Syndic Promenade Gestion 29/09 | 4 560,00 | |
| 30/09/2026 | BQ | 411SPG | Client Syndic Promenade Gestion | Règlement factures – VIR 29/09 | | 4 560,00 |
| 30/09/2026 | BQ | 401ENS | Fournisseur Énergie Sud | Prélèvement facture 09/2026 | 612,00 | |
| 30/09/2026 | BQ | 512100 | Banque – Nice | PRLV Énergie Sud 26/09 | | 612,00 |
| 30/09/2026 | BQ | 401AZH | Fournisseur Azur Hygiène Distribution | Correction erreur de sens règlement 07/09 (2 × 875,00) | 1 750,00 | |
| 30/09/2026 | BQ | 512100 | Banque – Nice | Correction erreur de sens règlement 07/09 (2 × 875,00) | | 1 750,00 |
| | | | | **Totaux** | **7 082,57** | **7 082,57** |

**Pourquoi ces sens ?**
- Frais, intérêts, prélèvement, paiement fournisseur : l'argent **sort** → 512 au **crédit**. La contrepartie est une charge (627, 6616) ou la diminution d'une dette (401 au débit).
- Virement reçu : l'argent **entre** → 512 au **débit** ; la créance client diminue → 411 au **crédit**.

Après ces écritures, le 512 présente un solde de **57 984,83 €**, égal au solde bancaire corrigé. Les comptes 401AZH (facture de 875,00 € réglée) et 411SPG (factures de 4 560,00 € réglées) peuvent être **lettrés**.

## 4. Points d'attention / pièges

- **Ne pas confondre les sens** : le débit du relevé est un crédit du 512. C'est l'erreur n° 1 en test.
- **Erreur de sens = double du montant** : corriger de 875,00 € seulement laisse un écart de 875,00 €.
- **Ne rien passer pour les suspens « côté 512 »** (chèque émis, remise tardive) : ce sont des décalages.
- **Les intérêts débiteurs** sont une charge financière (66), pas un frais bancaire (627). Selon le plan de comptes, on trouve 6615 ou 6616 : suivez la règle interne.
- **Date des écritures** : celle du relevé (30/09), pour que le rapprochement de septembre « tombe juste » sur septembre.

## 5. Ce que le recruteur attend / ce qu'un senior ferait en plus

- **Question 6 — Chèque n° 0001245** : vérifier en octobre qu'il est bien débité. S'il ne l'est toujours pas au bout de quelques semaines, appeler le fournisseur (chèque perdu ? jamais reçu ?) **avant** d'en émettre un autre, et faire opposition sur l'ancien si on le remplace. Un suspens ne doit jamais rester des mois sans explication.
- **Remise n° 0098** : vérifier sur le relevé d'octobre qu'elle est créditée le 02/10 pour **exactement** 2 340,00 € (un chèque rejeté apparaîtrait ensuite en débit).
- **Signaler l'origine de l'erreur du 07/09** : si c'est un modèle de saisie mal paramétré, la même erreur se reproduira.
- **Prélèvement et virement** : demander à la personne qui saisit la banque de traiter le relevé **au fil de l'eau** (idéalement chaque jour), pas en fin de mois.
- **Documenter** : l'état de rapprochement est daté, signé, et accompagné du relevé et de l'extrait du 512 pointés.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG : comptes 512, 401, 411, 44566, 627, 661 (6615 / 6616) ; principe de correction des erreurs par écriture de contrepassation ou d'extourne.
- Code de commerce art. L. 123-12 et suivants : obligation de tenir une comptabilité régulière, sincère et donnant une image fidèle.
- CGI art. 271 : conditions de déduction de la TVA (justificatif mentionnant la TVA).
