# Corrigé E05-01 — Rapprochement bancaire de septembre et écart introuvable

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E05-01](../exercices/E05-01_rapprochement-bancaire-dupain.md)

## 1. Analyse

Un rapprochement se fait **toujours en partant du précédent**. On vérifie d'abord que les suspens d'ouverture se sont dénoués, puis on pointe le mois, puis on établit l'état. S'il reste un écart après prise en compte de tous les suspens identifiés, ce n'est **pas un suspens** : c'est une **erreur**, et elle se cherche.

**Étape 1 — Suspens d'août :**
- chèque n° 4402 (1 860,00 €) : débité le 03/09 → dénoué ;
- remise espèces du 31/08 (2 340,00 €) : créditée le 01/09 → dénouée.
Aucun suspens ancien ne traîne. Bon point.

**Étape 2 — Pointage.**

Lignes du relevé **sans contrepartie** au 512 (à comptabiliser chez nous) :

| Date | Libellé | Montant | Nature |
|---|---|---|---|
| 10/09 | Edenred | écart 46,60 (1 175,00 saisi / 1 128,40 reçu) | Commission Edenred non saisie : la remise a été saisie **brute** |
| 28/09 | Frais tenue de compte | 38,50 | Frais bancaires |
| 28/09 | Commissions CB | 96,42 | Frais bancaires |
| 29/09 | Cotisation carte | 12,00 | Frais bancaires |
| 30/09 | Orange | 54,99 | Prélèvement non saisi (facture reçue : pièce 5) |

Lignes du 512 **sans contrepartie** sur le relevé (suspens normaux, rien à passer) :

| Date | Libellé | Montant | Sens |
|---|---|---|---|
| 16/09 | Chèque 4404 Emballages Lyonnais | 412,80 | Chèque émis non encaissé |
| 29/09 | Chèque 4406 Pâtisserie Supply | 834,00 | Chèque émis non encaissé |
| 30/09 | Remise espèces bord. 0930 | 2 115,00 | Remise non créditée |
| 30/09 | Remise CB 18-30/09 | 1 887,40 | Remise CB non créditée |

**Lignes pointées mais à montants différents :** le chèque 4405 est à **1 524,00 €** sur le relevé et à **1 254,00 €** au 512. Si le pointage automatique s'est fait « par numéro de chèque », il a masqué l'écart. C'est exactement l'erreur que l'on va retrouver à l'étape 4.

## 2. Calculs

### 2.1 Contrôle des soldes
- Relevé : 18 245,37 + 20 336,80 – 19 497,44 = **19 084,73 €** ✔
- 512 : 18 725,37 + 22 045,80 – 18 412,33 = **22 358,84 €** ✔

### 2.2 État de rapprochement provisoire (avant recherche de l'écart)

| Relevé | Montant | Compte 512 | Montant |
|---|---|---|---|
| Solde créditeur au 30/09 | 19 084,73 | Solde débiteur au 30/09 | 22 358,84 |
| – Ch. 4404 non débité | – 412,80 | – Commission Edenred | – 46,60 |
| – Ch. 4406 non débité | – 834,00 | – Frais tenue de compte | – 38,50 |
| + Remise espèces 30/09 | + 2 115,00 | – Commissions CB | – 96,42 |
| + Remise CB 18-30/09 | + 1 887,40 | – Cotisation carte | – 12,00 |
| | | – Prélèvement Orange | – 54,99 |
| **Solde bancaire rectifié** | **21 840,33** | **Solde comptable rectifié** | **22 110,33** |

**Écart résiduel : 22 110,33 – 21 840,33 = 270,00 €** (le 512 est trop élevé de 270 €).

### 2.3 Recherche de l'écart (méthode)
1. 270 est-il égal à une ligne du relevé ? Non.
2. 270 est-il le double d'une ligne (inversion de sens → écart = 2 × montant) ? 135,00 : aucune ligne.
3. **270 est-il divisible par 9 ?** 270 / 9 = 30 → **oui** : signe typique d'une **inversion de deux chiffres** (transposition).
4. On cherche deux montants proches qui ne diffèrent que par l'ordre des chiffres : chèque 4405, **1 524,00** sur le relevé et sur le talon (pièce 6), **1 254,00** au 512. 1 524 – 1 254 = 270 ✔.

Le chèque a été saisi pour 1 254,00 € au lieu de 1 524,00 € : le 512 n'a pas été crédité de 270 € et le compte fournisseur Grands Moulins du Rhône reste à tort créditeur de 270 € (la facture GM-26-0877 n'est pas soldée).

### 2.4 Écritures à passer (total des corrections au 512)
46,60 + 38,50 + 96,42 + 12,00 + 54,99 + 270,00 = **518,51 €**
22 358,84 – 518,51 = **21 840,33 €** = solde bancaire rectifié ✔

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 10/09/2026 | BQ | 627 | Services bancaires et assimilés | Commission Edenred TR août | 38,83 | |
| 10/09/2026 | BQ | 44566 | TVA déductible sur autres biens et services | Commission Edenred TR août | 7,77 | |
| 10/09/2026 | BQ | 512 | Banque BPAURA | Commission Edenred TR août | | 46,60 |
| 28/09/2026 | BQ | 627 | Services bancaires et assimilés | Frais tenue de compte 09/2026 | 38,50 | |
| 28/09/2026 | BQ | 512 | Banque BPAURA | Frais tenue de compte 09/2026 | | 38,50 |
| 28/09/2026 | BQ | 627 | Services bancaires et assimilés | Commissions encaissement CB 09/2026 | 96,42 | |
| 28/09/2026 | BQ | 512 | Banque BPAURA | Commissions encaissement CB 09/2026 | | 96,42 |
| 29/09/2026 | BQ | 627 | Services bancaires et assimilés | Cotisation carte business | 12,00 | |
| 29/09/2026 | BQ | 512 | Banque BPAURA | Cotisation carte business | | 12,00 |
| 30/09/2026 | BQ | 626 | Frais postaux et de télécommunications | Orange FO-2026-09-7781 | 45,83 | |
| 30/09/2026 | BQ | 44566 | TVA déductible sur autres biens et services | Orange FO-2026-09-7781 | 9,16 | |
| 30/09/2026 | BQ | 512 | Banque BPAURA | Orange FO-2026-09-7781 | | 54,99 |
| 30/09/2026 | BQ | 401GMR | Fournisseur Grands Moulins du Rhône | Correction saisie ch. 4405 (1 524,00 et non 1 254,00) | 270,00 | |
| 30/09/2026 | BQ | 512 | Banque BPAURA | Correction saisie ch. 4405 | | 270,00 |
| | | | | **Totaux** | **518,51** | **518,51** |

> Variante possible pour l'écriture n° 4 de la saisie initiale : contre-passer la ligne du chèque 4405 à 1 254,00 € et la ressaisir à 1 524,00 €. Les deux méthodes sont correctes ; la contre-passation + ressaisie laisse une piste d'audit plus lisible dans un logiciel qui lettre ligne à ligne. **Ne modifiez jamais** une écriture d'une période validée.

> Remarque Orange : la facture porte sur la période d'octobre. Pour un montant de 45,83 € HT, on ne passe pas de charge constatée d'avance en situation mensuelle (importance relative) ; à la clôture du 31/12, la question ne se posera pas (période de janvier facturée en décembre : à apprécier, montant non significatif).

### État de rapprochement définitif au 30/09/2026

| Relevé | Montant | Compte 512 (après écritures) | Montant |
|---|---|---|---|
| Solde créditeur au 30/09/2026 | 19 084,73 | Solde débiteur au 30/09/2026 | 21 840,33 |
| – Ch. 4404 du 16/09 (Emballages Lyonnais) | – 412,80 | | |
| – Ch. 4406 du 29/09 (Pâtisserie Supply) | – 834,00 | | |
| + Remise espèces bord. 0930 | + 2 115,00 | | |
| + Remise CB 18-30/09 | + 1 887,40 | | |
| **Solde rectifié** | **21 840,33** | **Solde rectifié** | **21 840,33** |

Écart : **0,00 €**.

## 4. Points d'attention / pièges

- **Le pointage automatique « par numéro de chèque »** valide des lignes dont les montants diffèrent. Contrôlez toujours le montant.
- **Remise saisie brute (Edenred)** : le bordereau donne le net viré et la commission. Saisir la remise pour sa valeur faciale crée un écart égal à la commission — et fait perdre 7,77 € de TVA déductible.
- **Le 471 n'est pas un compte d'écart** : y mettre 270 € aurait laissé au bilan un compte sans signification et au fournisseur un faux solde créditeur (la facture aurait été relancée par le fournisseur… ou payée deux fois).
- **Chèque 4404 du 16/09** : non débité au 30/09. Rien d'anormal à 14 jours, mais à surveiller : s'il n'est pas débité en octobre, demandez à Marc si le chèque a bien été remis à Emballages Lyonnais.
- **Ordre de saisie** : les dates au 512 ne sont pas chronologiques (saisie du 05/09 avant celle du 04/09). Sans conséquence comptable, mais le rapprochement s'en trouve compliqué ; un logiciel qui trie par date de valeur facilite le pointage.

## 5. Ce qu'un senior ferait en plus

- **Réponse à Inès** (mail interne) :
  > « Inès, j'ai trouvé l'écart : 270 € = 9 × 30, c'est une inversion de chiffres sur le chèque 4405 (1 524 saisi 1 254). Corrigé au 30/09 contre le compte Grands Moulins. Pour la suite : on ne solde jamais un rapprochement en 471, on cherche (montant exact, double, divisible par 9). Bonne fin de congés ! »
- **Paramétrer la saisie Edenred** : créer un modèle d'écriture « remise TR » avec trois lignes (512 net, 627 + 44566 commission, 467 Edenred brut), pour que la commission ne soit plus oubliée.
- **Contrôle croisé CB** : rapprocher les remises CB du relevé (4 215,60 + 6 512,80 + 1 887,40 = 12 615,80 €) avec le cumul CB des Z de caisse de septembre. Un écart signalerait des encaissements CB non déclarés en caisse ou une remise manquante.
- **Contrôle du ratio espèces** : remises espèces de septembre = 3 180 + 2 960 + 2 115 = 8 255 € (hors remise du 31/08 rattachée à août). Comparez au CA espèces des Z : la différence correspond au fond de caisse et aux dépenses payées en espèces — et doit être justifiée.
- **Archiver** l'état de rapprochement signé (préparé par / revu par / date) dans le dossier permanent de l'exercice.

## 6. Références

- PCG : comptes 512, 627, 626, 44566, 401, 471 (compte d'attente à solder).
- Code de commerce, art. L. 123-14 (image fidèle), principe de non-compensation.
- CGI, art. 261 C (exonération de certaines opérations bancaires et financières).
- Code monétaire et financier : délai de présentation d'un chèque (1 an et 8 jours) — utile pour l'analyse des suspens anciens.
