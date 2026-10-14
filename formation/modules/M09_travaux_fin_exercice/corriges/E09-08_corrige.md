# Corrigé E09-08 — SCI Horizon Pro : provision pour gros entretien ou composant ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-08](../exercices/E09-08_gros-entretien-horizon-pro.md)

## 1. Analyse

**Ce que dit le PCG.** Les dépenses de **gros entretien ou de grandes révisions** sont celles qui ont pour seul objet de **vérifier le bon état de fonctionnement** des installations et d'y **apporter un entretien**, sans prolonger leur durée de vie au-delà de celle prévue. Lorsqu'elles font l'objet de **programmes pluriannuels** établis en application de **lois, de règlements ou de pratiques constantes** de l'entité, deux méthodes sont possibles :
1. **la provision pour gros entretien** (compte 1572), constituée progressivement sur la période qui précède les travaux ;
2. **le composant « gros entretien »** : la dépense est immobilisée lors de sa réalisation et amortie jusqu'à la révision suivante (un composant est identifié dès l'origine).

La SCI a retenu la provision en 2025 : par **permanence des méthodes**, elle la conserve.

**Analyse des postes :**

| Poste | Nature | Provisionnable ? |
|---|---|---|
| A — Grande révision des ascenseurs | Entretien imposé par la réglementation, **sans prolongation** de la durée d'utilisation | **Oui** |
| B — Peintures et sols des parties communes | Entretien cyclique (10 ans), pratique constante du bailleur | **Oui** |
| C — Remplacement du groupe froid | **Remplacement d'un composant** en fin de vie : la dépense sera **immobilisée** en 2029 et l'ancien composant sorti. Un investissement futur ne se provisionne jamais | **Non** |

**Traitement correct du poste C :** l'enjeu est le **plan d'amortissement de l'ancien composant**. Il était prévu sur 20 ans (fin en 2031), mais il sera remplacé fin 2029. Sa durée d'utilisation est donc **raccourcie** : c'est un **changement d'estimation**, traité de façon **prospective**. On amortit la VNC au 01/01/2026 sur la durée résiduelle révisée (4 ans : 2026 à 2029).

**Hausse des devis (A et B : 44 000 € → 48 000 €) :** c'est aussi un **changement d'estimation**. On recalcule la provision nécessaire à la clôture sur la base du coût réestimé et de la quote-part de la période écoulée (2 ans sur 5). La dotation de l'exercice absorbe l'écart : on ne corrige pas 2025.

## 2. Calculs

**Provision pour gros entretien :**

| Élément | Montant |
|---|---|
| Coût réestimé des postes A + B : 22 000 + 26 000 | 48 000,00 € |
| Quote-part de la période écoulée (2025 et 2026) : 2/5 | |
| Provision nécessaire au 31/12/2026 : 48 000 × 2/5 | **19 200,00 €** |
| Provision existante | 8 800,00 € |
| **Dotation 2026** | **10 400,00 €** |

*Proposition du DAF : 78 000 × 2/5 = 31 200 €, soit une dotation de 22 400 €. Le surplus de 12 000 € (30 000 × 2/5) correspond au groupe froid et n'est pas justifié.*

**Groupe froid :**
- Amortissement annuel initial : 24 000 / 20 = 1 200 € ; cumul au 31/12/2025 (14 ans) = 16 800 € ; **VNC au 01/01/2026 = 7 200 €**.
- Durée résiduelle révisée : 4 ans (2026, 2027, 2028, 2029).
- **Nouvelle dotation annuelle : 7 200 / 4 = 1 800,00 €** (au lieu de 1 200 €), soit 600 € de plus par an.
- En 2029, la VNC sera nulle au moment du remplacement : aucune moins-value de sortie.

**Impact sur le résultat 2026 :** – 10 400 – 1 800 = **– 12 200,00 €** (dont 600 € liés à la révision du plan).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Provision gros entretien (ascenseurs + parties communes) 2/5 | 10 400,00 | |
| 31/12/2026 | OD | 1572 | Provisions pour gros entretien ou grandes révisions | Provision gros entretien | | 10 400,00 |
| 31/12/2026 | OD | 6811 | Dotations aux amortissements des immobilisations | Groupe froid CTA – durée révisée (VNC 7 200 / 4) | 1 800,00 | |
| 31/12/2026 | OD | 28135 | Amortissements des installations générales, agencements | Groupe froid CTA | | 1 800,00 |
| | | | | **Totaux** | **12 200,00** | **12 200,00** |

**En 2029 (pour mémoire) :**
- travaux A et B réalisés : charges par nature (615) pour le coût réel, et **reprise** de la provision (D 1572 / C 7815) ;
- groupe froid : sortie de l'ancien composant (VNC nulle) et immobilisation du nouveau (D 2135 / C 404).

## 4. Points d'attention / pièges

- **Le remplacement d'un composant ne se provisionne pas.** C'est l'erreur du DAF : la provision ne finance pas un investissement futur. Son vrai sujet comptable, c'est le **raccourcissement du plan d'amortissement** de l'ancien composant.
- **Pas de prolongation de la durée de vie** : si la révision des ascenseurs était en réalité une **modernisation** qui prolonge leur durée d'utilisation ou améliore leurs performances, la dépense serait immobilisable et non provisionnable. Il faut lire le devis.
- **Changement d'estimation ≠ correction d'erreur** : la hausse des devis et la révision de durée sont traitées en résultat de l'exercice, de façon prospective.
- **Refacturation aux locataires** : si les baux permettaient de refacturer ces dépenses (dans les limites de l'article R. 145-35 du Code de commerce pour les baux commerciaux), la charge nette pour la SCI serait moindre et il faudrait en tenir compte.
- **Ne pas mélanger les deux méthodes** pour une même catégorie de dépenses.

**Fiscalité :**
- La provision pour gros entretien est **déductible** si les dépenses sont **précisément évaluées** (devis), relèvent d'un **programme** imposé par la réglementation ou la pratique, et **ne sont pas immobilisables**. Les postes A et B remplissent ces conditions : **pas de réintégration**.
- La dotation complémentaire au groupe froid est **déductible**, puisque la révision de la durée d'utilisation est justifiée par un élément objectif (plan de travaux, état de l'équipement).
- La partie « groupe froid » proposée par le DAF (12 000 €) aurait été **non déductible** et aurait exposé la SCI à un redressement.

## 5. Ce qu'un senior ferait en plus

- **Dossier permanent** : conserver le plan pluriannuel, les devis et la justification réglementaire (ascenseurs). Mettre à jour la provision chaque année avec un tableau « coût estimé / années écoulées / provision ».
- **Annexe** : méthode retenue pour le gros entretien (provision), changement d'estimation de la durée du groupe froid.
- **Gouvernance** : la SCI a deux associés (dont Delta Invest à 40 %). Une écriture qui « arrange tout le monde » fiscalement mais n'est pas justifiée comptablement engage le cabinet. On répond par écrit, avec copie aux deux associés.

**Réponse au DAF (copie à Jean Delmas) :**
> « Bonjour, merci pour la mise à jour du plan. Nous retenons une provision de 19 200 € au 31/12/2026 (dotation de 10 400 €), calculée sur la grande révision des ascenseurs et la réfection des parties communes réestimées à 48 000 €. Le remplacement du groupe froid (30 000 €) est un renouvellement de composant : il sera immobilisé en 2029 et ne peut pas être provisionné (PCG, règles sur les composants ; une telle provision ne serait pas déductible). En contrepartie, nous accélérons l'amortissement de l'équipement actuel sur sa durée résiduelle réelle : 1 800 € par an au lieu de 1 200 €, ce qui est déductible. La charge totale de 2026 sur ces postes est donc de 12 200 €. »

## 6. Références

- PCG (règlement ANC n° 2014-03 modifié) : dépenses de gros entretien et grandes révisions (provision ou composant), approche par composants, révision du plan d'amortissement (changement d'estimation, traitement prospectif).
- CGI, art. 39, 1-5° (provisions) ; art. 39, 1-2° (amortissements) ; doctrine administrative sur les provisions pour grosses réparations et gros entretien (BOFiP, série BIC-PROV).
- Code de la construction et de l'habitation : obligations d'entretien et de contrôle technique des ascenseurs.
- Code de commerce, art. R. 145-35 (charges non imputables au locataire dans un bail commercial).
