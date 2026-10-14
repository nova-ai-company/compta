# Corrigé E10-06 — Le crédit d'impôt recherche de TechNova : calcul et comptabilisation

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E10-06](../exercices/E10-06_CIR-technova.md)

## 1. Analyse

Le CIR finance la **recherche** (lever une incertitude scientifique ou technique au-delà de l'état de l'art), pas le développement de produits nouveaux. Le senior vérifie trois choses :

1. **Le périmètre** : seul le projet « Moteur d'optimisation » est de la R&D (état de l'art, verrou, incertitude, échecs documentés). La « Nouvelle interface mobile » est de l'**innovation** (CII éventuel), pas de la recherche.
2. **Les paramètres de l'année** : forfait de fonctionnement à 40 % (et non 43 %), plus 75 % des amortissements.
3. **Les déductions obligatoires** : la subvention Bpifrance affectée au projet de recherche **diminue la base** l'année de son encaissement.

**Erreurs d'Émilie** : (1) Lisa Moreno incluse (50 % interface mobile = innovation) ; (2) taux de fonctionnement de 43 % ; (3) subvention de 40 000 € non déduite. Résultat : 115 351 € au lieu de **89 534 €** (surestimation de 25 817 €, qui aurait été redressée en cas de contrôle, avec intérêts de retard).

## 2. Calculs

**Dépenses de personnel R&D** (salaire + charges patronales effectivement supportées) × temps R&D :

| Salarié | Coût total | % R&D | Dépenses éligibles |
|---|---|---|---|
| Yanis Haddad | 72 000 + 30 240 = 102 240 | 40 % | 40 896,00 |
| Amine Kaci | 58 000 + 13 920 = 71 920 | 80 % | 57 536,00 |
| Julie Perret | 52 000 + 12 480 = 64 480 | 60 % | 38 688,00 |
| Hugo Tran | 55 000 + 13 200 = 68 200 | 100 % | 68 200,00 |
| Lisa Moreno | 45 000 + 10 800 = 55 800 | 0 % | 0,00 |
| **Total** | | | **205 320,00** |

**Base et CIR**

| Poste | Calcul | Montant |
|---|---|---|
| Dépenses de personnel | | 205 320,00 |
| Dotations aux amortissements (serveur GPU) | | 12 000,00 |
| Fonctionnement forfaitaire | 40 % × 205 320 + 75 % × 12 000 = 82 128 + 9 000 | 91 128,00 |
| Sous-traitance agréée (Optima Lab) | | 30 000,00 |
| **Base brute** | | **338 448,00** |
| – Subvention Bpifrance affectée | | – 40 000,00 |
| **Base nette** | | **298 448,00** |
| **CIR** | 30 % × 298 448 = 89 534,40 | **89 534 €** |

Contrôle du calcul d'Émilie : personnel 233 220 € (avec Lisa 27 900 €) ; fonctionnement 43 % × 233 220 + 9 000 = 109 284,60 € ; base 384 504,60 € ; CIR 115 351 €.

**3) CII potentiel** (non calculé ici) : temps sur « Nouvelle interface mobile » : Julie Perret 20 % (12 896 €) et Lisa Moreno 50 % (27 900 €), soit 40 796 € de dépenses de personnel à analyser au titre du CII (prototype d'un produit nouveau sur le marché), sous réserve d'un dossier démontrant la nouveauté et des subventions éventuelles affectées.

**4) Imputation**

- IS brut 2026 : 75 750 € → imputation du CIR à hauteur de 75 750 € → IS net 0 €.
- Excédent : 89 534 – 75 750 = **13 784 €** → **remboursement immédiat** (PME au sens communautaire), demandé avec le 2572 + 2069-A.

## 3. Écritures comptables

**Les deux méthodes admises**

| | Méthode 1 : diminution de l'IS | Méthode 2 : subvention d'exploitation |
|---|---|---|
| Compte crédité | 699 (sous-compte « Crédits d'impôt ») ou 695 | 74 (subdivision « CIR ») |
| Résultat d'exploitation / EBITDA | Inchangé | **Augmenté de 89 534 €** |
| Résultat net | Identique | Identique |
| Logique | Le CIR est juridiquement un crédit d'**impôt** | Le CIR finance des dépenses d'exploitation (approche IAS 20) |

Yanis souhaite la méthode 2. **Mais** l'an dernier, le cabinet a retenu la méthode 1 : changer de présentation est un **changement de méthode** qui doit être justifié (meilleure information), appliqué de manière permanente et **décrit en annexe** avec l'information comparative. Ce n'est pas un choix « au coup par coup ». Le senior soumet la décision à Hélène, puis documente.

Écritures selon la méthode 2 (subvention), au 31/12/2026 :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 444200 | État — CIR à recevoir | CIR 2026 (2069-A) | 89 534,00 | |
| 31/12/2026 | OD | 74xxxx | Subventions d'exploitation — CIR (subdivision selon nomenclature 2025) | CIR 2026 (2069-A) | | 89 534,00 |
| 31/12/2026 | OD | 444000 | État — impôt sur les bénéfices | Imputation du CIR sur l'IS 2026 | 75 750,00 | |
| 31/12/2026 | OD | 444200 | État — CIR à recevoir | Imputation du CIR sur l'IS 2026 | | 75 750,00 |
| | | | | **Totaux** | **165 284,00** | **165 284,00** |

(L'IS de 75 750 € a été constaté en E10-05 : 695 / 444.) Solde du 444200 : **13 784 € débiteur** = créance remboursable. Au remboursement (mai-juin 2027 en général) : 512 / 444200 pour 13 784 €.

Variante méthode 1 : même écriture en remplaçant le 74 par le **699** (sous-compte « Crédits d'impôt »), ou par un crédit du **695**.

## 4. Points d'attention / pièges

- **Retraitement 2058-A** : le CIR est **non imposable**. Comptabilisé en 74 (ou 699), il est **déduit** pour 89 534 €. S'il est porté au crédit du 695, la réintégration de l'IS se fait pour le montant net et aucune déduction séparée n'est nécessaire. Dans tous les cas, le résultat fiscal est identique (1 640 000 € avant déficits — cf. E10-05).
- **Subvention Bpifrance** : déduite de la base **l'année de l'encaissement**. Une **avance remboursable** est aussi déduite l'année de son versement, puis rajoutée à la base l'année de son remboursement.
- **JEI** : seules les charges sociales **effectivement supportées** entrent dans la base.
- **Président** : sa rémunération n'est retenue que s'il exerce réellement une activité de chercheur, prouvée par des feuilles de temps et sa qualification.
- **Sous-traitance** : prestataire **agréé** (vérifier l'agrément de l'année), plafonds spécifiques ; un sous-traitant non agréé est exclu.
- **Dossier justificatif** : sans état de l'art, description du verrou, journal des travaux et temps passés, le CIR ne tiendra pas en cas de contrôle (le délai de reprise du CIR est allongé — *à vérifier*).

## 5. Ce qu'un senior ferait en plus

- **Mail type à Émilie** :

> « Bonjour Émilie, après revue, le CIR 2026 s'élève à 89 534 € (et non 115 351 €) : 1) le projet "interface mobile" relève de l'innovation, pas de la recherche — on regarde séparément le CII sur 40 796 € de dépenses de personnel ; 2) le forfait de fonctionnement est désormais de 40 % ; 3) la subvention Bpifrance de 40 000 € vient en déduction de la base. Le CIR couvre tout l'IS 2026 (75 750 €) et 13 784 € vous seront remboursés. Sur la présentation en subvention : c'est possible, mais c'est un changement de méthode par rapport à 2025 ; nous le décrirons dans l'annexe avec le comparatif. Je vous propose un point avec Hélène pour valider. Bien à vous. »

- Proposer un **rescrit** CIR (art. L. 80 B LPF) ou un audit externe du dossier justificatif si les montants augmentent.
- Mettre en place un suivi des temps **mensuel** signé par les salariés.
- Archiver : 2069-A, dossier technique, contrat Optima Lab + agrément, convention Bpifrance.

## 6. Références

- CGI : art. 244 quater B (CIR : dépenses éligibles, forfait de fonctionnement, sous-traitance, subventions), art. 244 quater B II k (CII), art. 199 ter B (imputation et remboursement immédiat), art. 220 B.
- LPF : art. L. 80 B (rescrit CIR).
- PCG / ANC : présentation du CIR (diminution de l'impôt ou subvention), règles de changement de méthode et information en annexe.
- BOFiP : série BIC-RICI (crédits et réductions d'impôt, CIR/CII).
