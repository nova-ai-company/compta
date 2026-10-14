# Conventions de rédaction (usage interne — pour tous les rédacteurs de modules)

## Public
Une comptable **junior** (BTS/DCG, 1 an d'expérience) que l'on veut amener au niveau **senior** (autonome sur un portefeuille, de la saisie au bilan et à la liasse, capable de conseiller le client et de gérer les cas atypiques). Tutoiement interdit : on vouvoie l'apprenante (« vous »). **Tout en français.**

## Référentiel (exercice 2026, date du jour 09/10/2026)
- **PCG** : règlement ANC n° 2014-03 **modifié par le règlement ANC n° 2022-06**, applicable aux exercices ouverts à compter du **01/01/2025**. Conséquences à respecter :
  - **Suppression des comptes de transfert de charges (791, 796, 797)** : ne jamais les utiliser. Les remboursements (IJSS, assurance…) se comptabilisent en diminution de la charge concernée ou en produit par nature selon le cas.
  - **Résultat exceptionnel restreint** aux éléments liés à un événement majeur et inhabituel. Pénalités, amendes, dons, libéralités courants ne sont plus en exceptionnel par défaut → comptes de charges d'exploitation de la classe 65 (pénalités et amendes : 658x selon la nouvelle nomenclature ; dons : 6586/6587 selon nomenclature). **Les cessions d'immobilisations restent en 675 / 775.** Quand un numéro de compte de la nomenclature 2025 est incertain, indiquez le compte à 3 chiffres (ex. « 658 ») et précisez « *subdivision selon la nomenclature 2025 du PCG* ».
  - Comptes de primes de remboursement / frais d'émission d'emprunt : selon nouvelle nomenclature.
- **Taux TVA** : 20 % / 10 % / 5,5 % / 2,1 %.
- **IS** : 15 % jusqu'à 42 500 € de bénéfice (PME : CA HT < 10 M€, capital entièrement libéré, détenu ≥ 75 % par des personnes physiques ou sociétés remplissant ces conditions), 25 % au-delà.
- **Facturation électronique** : obligation de **réception** pour toutes les entreprises assujetties depuis le **01/09/2026** ; obligation d'**émission** + **e-reporting** : GE et ETI depuis le 01/09/2026, PME/TPE/micro au **01/09/2027**. Plateformes agréées (**PA**, anciennement PDP). Nouvelles mentions obligatoires : **SIREN du client**, **adresse de livraison** si différente, **nature de l'opération** (livraison de biens / prestation de services / mixte), **option pour le paiement de la TVA d'après les débits** le cas échéant.
- **Chiffres qui changent chaque année** (PASS, SMIC, plafonds, barèmes kilométriques, taux de cotisations, seuils micro/franchise TVA, CVAE…) : **donnez les valeurs nécessaires dans l'énoncé** (« on retient… ») et ajoutez la mention *« valeur à vérifier chaque année »*. Ne jamais affirmer une valeur précise incertaine comme vérité absolue.
- Citer les références quand c'est utile : article du CGI, du Code de commerce, du PCG, BOFiP, CSS — **sans inventer de numéro** : si vous n'êtes pas sûr du numéro exact, citez le texte de façon générique.

## Clients
Utiliser **exclusivement** les clients de `01_PORTEFEUILLE_CLIENTS.md` (codes C01 à C25) et respecter leurs caractéristiques (forme, régime, date de clôture, personnes). Les fournisseurs/clients tiers sont inventés (SIREN fictifs à 9 chiffres, noms crédibles).

## Format de fichiers (Markdown)
Chaque module vit dans `formation/modules/MXX_nom_court/` :
- `cours.md` — l'essentiel théorique **orienté pratique** : règles, schémas d'écritures types (tableaux), pièges, **« Réflexe senior »** (encadrés `> 💡 Réflexe senior :`), **« Erreur classique de junior »** (`> ⚠️ Erreur classique :`), checklist de fin de module. Longueur visée : 4 à 10 pages.
- `exercices/EXX-NN_titre-court.md` — un fichier par exercice (XX = n° de module, NN = n° d'exercice).
- `corriges/EXX-NN_corrige.md` — **un fichier (une « page ») par corrigé**, avec TOUS les détails.

### Gabarit d'exercice
```
# EXX-NN — Titre
**Client :** C0X — Nom | **Difficulté :** ★☆☆ / ★★☆ / ★★★ | **Durée estimée :** 30 min | **Thèmes :** …
**Corner case :** oui/non (si oui, lequel en une ligne)

## La mise en situation
(Scène réaliste : e-mail du client, appel téléphonique, note de la cheffe de mission Hélène Ferrand, pièces arrivées en vrac, échéance qui approche…)

## Les pièces
(Reproduire les documents : facture, devis, bon de commande, bon de livraison, avoir, relevé bancaire, bulletin de paie, tableau d'amortissement, extrait de grand livre, balance, contrat, échéancier, Z de caisse, DAU, relevé marketplace… sous forme de blocs de texte ``` ou de tableaux Markdown, avec TOUTES les mentions réalistes : numéro, date, SIREN, n° TVA intracom, conditions de paiement, pénalités de retard, indemnité forfaitaire de 40 €, etc.)
Certaines pièces doivent volontairement contenir des **anomalies** à détecter (mention manquante, erreur de calcul, mauvais taux, facture au nom du gérant, doublon, date hors exercice…).

## Travail à faire
1. …
2. …
```

### Gabarit de corrigé (une page, complet)
```
# Corrigé EXX-NN — Titre
## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)
## 2. Calculs (détaillés, chaque montant justifié)
## 3. Écritures comptables
| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
(totaux équilibrés)
## 4. Points d'attention / pièges
## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)
## 6. Références (PCG, CGI, Code de commerce, BOFiP…)
```

## Qualité
- **Tous les calculs doivent être exacts et les écritures équilibrées.** Vérifiez vos chiffres (vous pouvez utiliser `python3` en ligne de commande pour recalculer).
- Montants au format français : `12 345,67 €`.
- Réalisme : les clients ont des personnalités, oublient des pièces, posent de « mauvaises » questions, le cabinet a des délais.
- Couvrir les cas « normaux » ET les **corner cases**.
- Pas de lien hypertexte inventé.
