# Corrigé E08-10 — Menuiserie Bois & Création : erreur d'inventaire N-1, stock en dépôt, bois confié et cut-off

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E08-10](../exercices/E08-10_corner-cases-menuiserie.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Partie A — L'erreur d'inventaire au 31/12/2025

**Question 1 — Chiffrage.** Le lot n° 14 a été compté deux fois : stock au 31/12/2025 surévalué de 3,6 m³ × 1 450 € = **5 220,00 €**. Un stock final surévalué **diminue** la consommation de l'exercice : le résultat 2025 est surévalué d'autant.

| 2025 | Publié | Corrigé | Écart |
|---|---|---|---|
| Résultat fiscal (avant IS) | 12 400,00 € | 12 400,00 – 5 220,00 = 7 180,00 € | – 5 220,00 € |
| IS à 15 % | 1 860,00 € | 7 180,00 × 15 % = 1 077,00 € | – 783,00 € |
| Bénéfice net | 10 540,00 € | 6 103,00 € | – 4 437,00 € |
| Capitaux propres au 31/12/2025 | — | — | **– 4 437,00 €** (5 220,00 – 783,00) |

**Question 2 — Correction comptable.** Les comptes 2025 sont **approuvés** : on ne les modifie pas (pas de « réouverture » de l'exercice). Selon les règles du PCG sur les corrections d'erreurs (dans leur rédaction issue du règlement ANC n° 2022-06), la correction d'une erreur est comptabilisée **dans le résultat de l'exercice au cours duquel elle est découverte**, avec une **information en annexe** si elle est significative. Le classement de l'impact en résultat exceptionnel n'est plus le réflexe (définition restreinte de l'exceptionnel) : il reste dans le poste concerné, ici la variation de stock.

En pratique, **aucune écriture spécifique** n'est nécessaire : le compte 31 porte encore le stock du 31/12/2025 (41 870,00 €, dont 5 220,00 € fictifs). Lorsqu'on annule ce stock initial (D 6031 / C 31) et qu'on constate le stock réel au 30/09/2026, la variation de stock 2026 absorbe automatiquement les 5 220,00 € : la consommation 2026 est majorée d'autant. **L'erreur se corrige d'elle-même en 2026** — elle a simplement « déplacé » 5 220 € de charges de 2025 vers 2026. Le senior doit **l'identifier et la documenter** pour expliquer la variation de stock et la marge de la situation au 30/09, et pour l'annexe 2026.

**Question 3 — Options fiscales.**

| Option | Mécanisme | Effet 2025 | Effet 2026 |
|---|---|---|---|
| **a. Ne rien faire** | La correction passe dans le résultat 2026 | IS 2025 payé en trop : 783 € (perdu) | Déficit 2026 majoré de 5 220 € (reportable) |
| **b. Réclamation sur 2025** (exercice non prescrit) | Rectification du résultat fiscal 2025 (stock de clôture corrigé) — délai : jusqu'au 31 décembre de la 2e année suivant le paiement de l'impôt (LPF art. R*196-1) | **Restitution de 783 €** (trésorerie immédiate) | Le stock d'ouverture fiscal 2026 étant corrigé, il faut **réintégrer extra-comptablement 5 220 €** sur la déclaration 2026 (sinon la charge serait déduite deux fois) : le déficit 2026 est réduit d'autant |

La règle de **correction symétrique des bilans** (CGI art. 38-4 bis) ne s'applique qu'aux erreurs affectant le bilan d'ouverture du **premier exercice non prescrit** ; ici l'exercice 2025 lui-même n'est pas prescrit : on corrige directement 2025.

**Recommandation** : pour une entreprise en conciliation, **783 € de trésorerie immédiate** valent mieux qu'un déficit supplémentaire de 5 220 € dont l'utilisation future est incertaine. Option **b**, avec réintégration de 5 220 € en 2026. *Piste à étudier avec Hélène Ferrand : le report en arrière (carry-back) du déficit 2026 sur le bénéfice 2025 — sa base serait le bénéfice corrigé, et la créance qui en résulte n'est en principe remboursable qu'au terme de cinq ans, sauf ouverture d'une procédure collective.*

### Partie B — La situation au 30/09/2026

**Question 4 — Analyse des pièces.**

| Élément | Constat | Traitement |
|---|---|---|
| Lot de chêne « Dufresne » (6 080 €) | Fourni par **le client** (pièce 2) : il n'appartient pas à la menuiserie, qui le façonne pour lui | **Exclu** du stock (bien de tiers). L'en-cours de l'escalier ne comprend que les heures et fournitures de la menuiserie : correct |
| 6 portes chez Déco Bois (attestation au 30/09) | Dépôt : la menuiserie **reste propriétaire** jusqu'à la revente | **Ajoutées** au stock de produits finis : 6 × 490 = 2 940 € |
| 4 portes vendues par Déco Bois en septembre | Le dépositaire les a revendues : à cet instant, il les achète à la menuiserie (585 € HT) | **Vente de septembre** non facturée → **facture à établir** 4 × 585 = 2 340 € HT. Les portes ne sont plus en stock (l'attestation n'en compte que 6) : cohérent |
| a) Panneaux Scierie du Pilat (BL 28/09) | Reçus et **comptés**, facture d'octobre non saisie | **FNP** 4 260 € HT |
| b) Quincaillerie Pro Lyon (facture 29/09) | Facture **saisie**, marchandise **livrée le 03/10** (non comptée) | **CCA** 1 180 € HT (achat facturé non livré). Côté TVA : pour une livraison de biens, la TVA devient exigible chez le fournisseur à la **livraison** (03/10) ; le droit à déduction naît à ce moment — la déduction de 236 € sur la CA3 de septembre était prématurée (régularisation à prévoir, voir M04) |
| c) Agencement Optique Verdier (réception le 30/09) | Travaux **achevés et réceptionnés** le 30/09, facture du 05/10 | **Facture à établir** 8 600 € HT |
| d) Agencement Saint-Just (facture 29/09) | Facturé mais **pas encore posé** au 30/09 (réception le 07/10) ; il est à l'atelier et compté en produits finis (5 400 €) | **PCA** 7 800 € HT ; il reste en stock à son coût |

### Inventaire corrigé par compte

| Compte | Inventaire d'Antoine | Corrections | **Inventaire corrigé** |
|---|---|---|---|
| 31 Matières premières (bois + panneaux) | 28 640 + 9 420 = 38 060,00 | – 6 080,00 (chêne Dufresne) | **31 980,00** |
| 32 Autres approvisionnements | 3 180,00 | — (la quincaillerie du 03/10 n'est ni comptée ni à ajouter) | **3 180,00** |
| 33 En-cours de production (escalier Dufresne) | 6 300,00 | — | **6 300,00** |
| 355 Produits finis | 5 400,00 | + 2 940,00 (6 portes chez Déco Bois) | **8 340,00** |
| **Total** | **52 940,00** | **– 3 140,00** | **49 800,00** |

## 2. Calculs (détaillés, chaque montant justifié)

### Variations de stock au 30/09/2026

| Compte | Stock initial (31/12/2025) | Stock au 30/09/2026 | Variation | Sens |
|---|---|---|---|---|
| 6031 (matières) | 41 870,00 | 31 980,00 | SI – SF = **9 890,00** | Débitrice (charge), **dont 5 220,00 € de correction de l'erreur 2025** |
| 6032 (autres approvisionnements) | 2 950,00 | 3 180,00 | SI – SF = **– 230,00** | Créditrice (diminution de charge) |
| 7133 (en-cours de biens) | 4 100,00 | 6 300,00 | SF – SI = **2 200,00** | Créditrice (production stockée) |
| 7135 (produits finis) | 3 600,00 | 8 340,00 | SF – SI = **4 740,00** | Créditrice (production stockée) |

Incidence nette des variations sur le résultat de la situation : – 9 890 + 230 + 2 200 + 4 740 = **– 2 720,00 €**, dont **– 5 220,00 €** liés à l'erreur de 2025 (hors erreur : + 2 500,00 €).

### Régularisations de cut-off

| Élément | HT | TVA 20 % | TTC |
|---|---|---|---|
| FNP Scierie du Pilat | 4 260,00 | 852,00 | 5 112,00 |
| CCA Quincaillerie Pro Lyon | 1 180,00 | — | — |
| Facture à établir Optique Verdier | 8 600,00 | 1 720,00 | 10 320,00 |
| Facture à établir Déco Bois (4 × 585,00) | 2 340,00 | 468,00 | 2 808,00 |
| PCA Saint-Just | 7 800,00 | — | — |

Incidence des régularisations sur le résultat : – 4 260 + 1 180 + 8 600 + 2 340 – 7 800 = **+ 60,00 €**.

## 3. Écritures comptables

Écritures de la situation intermédiaire au 30/09/2026 (journal OD de situation ; elles seront contre-passées ou reprises selon l'organisation du dossier avant la clôture du 31/12/2026).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 6031 | Variation des stocks de matières premières | Annulation stock MP au 31/12/2025 (dont erreur lot n° 14 : 5 220,00) | 41 870,00 | |
| 30/09/2026 | OD | 31 | Matières premières | Annulation stock MP au 31/12/2025 | | 41 870,00 |
| 30/09/2026 | OD | 31 | Matières premières | Stock MP au 30/09/2026 (hors chêne Dufresne, bien de tiers) | 31 980,00 | |
| 30/09/2026 | OD | 6031 | Variation des stocks de matières premières | Stock MP au 30/09/2026 | | 31 980,00 |
| 30/09/2026 | OD | 6032 | Variation des stocks des autres approvisionnements | Annulation stock au 31/12/2025 | 2 950,00 | |
| 30/09/2026 | OD | 32 | Autres approvisionnements | Annulation stock au 31/12/2025 | | 2 950,00 |
| 30/09/2026 | OD | 32 | Autres approvisionnements | Stock au 30/09/2026 | 3 180,00 | |
| 30/09/2026 | OD | 6032 | Variation des stocks des autres approvisionnements | Stock au 30/09/2026 | | 3 180,00 |
| 30/09/2026 | OD | 7133 | Variation des en-cours de production de biens | Annulation en-cours au 31/12/2025 | 4 100,00 | |
| 30/09/2026 | OD | 33 | En-cours de production de biens | Annulation en-cours au 31/12/2025 | | 4 100,00 |
| 30/09/2026 | OD | 33 | En-cours de production de biens | En-cours escalier Dufresne au 30/09/2026 | 6 300,00 | |
| 30/09/2026 | OD | 7133 | Variation des en-cours de production de biens | En-cours au 30/09/2026 | | 6 300,00 |
| 30/09/2026 | OD | 7135 | Variation des stocks de produits | Annulation produits finis au 31/12/2025 | 3 600,00 | |
| 30/09/2026 | OD | 355 | Produits finis | Annulation produits finis au 31/12/2025 | | 3 600,00 |
| 30/09/2026 | OD | 355 | Produits finis | PF au 30/09/2026 : agencement Saint-Just 5 400 + 6 portes en dépôt Déco Bois 2 940 | 8 340,00 | |
| 30/09/2026 | OD | 7135 | Variation des stocks de produits | Produits finis au 30/09/2026 | | 8 340,00 |
| 30/09/2026 | OD | 601 | Achats stockés – matières premières | FNP Scierie du Pilat BL 26-3307 du 28/09 | 4 260,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP Scierie du Pilat — TVA 20 % | 852,00 | |
| 30/09/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Scierie du Pilat BL 26-3307 | | 5 112,00 |
| 30/09/2026 | OD | 486 | Charges constatées d'avance | Quincaillerie Pro Lyon QPL-26-9915 — livrée le 03/10 | 1 180,00 | |
| 30/09/2026 | OD | 602 | Achats stockés – autres approvisionnements | Quincaillerie facturée non livrée au 30/09 | | 1 180,00 |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | Optique Verdier — agencement réceptionné le 30/09 | 10 320,00 | |
| 30/09/2026 | OD | 704 | Travaux | Optique Verdier — agencement magasin | | 8 600,00 |
| 30/09/2026 | OD | 44587 | TVA sur factures à établir | Optique Verdier — TVA 20 % (exigible à l'encaissement) | | 1 720,00 |
| 30/09/2026 | OD | 4181 | Clients – factures à établir | Déco Bois — 4 portes revendues en septembre | 2 808,00 | |
| 30/09/2026 | OD | 701 | Ventes de produits finis | Déco Bois — 4 portes × 585,00 | | 2 340,00 |
| 30/09/2026 | OD | 44587 | TVA sur factures à établir | Déco Bois — TVA 20 % | | 468,00 |
| 30/09/2026 | OD | 704 | Travaux | Saint-Just FA-26-0398 — pose le 07/10/2026 | 7 800,00 | |
| 30/09/2026 | OD | 487 | Produits constatés d'avance | Saint-Just — agencement non posé au 30/09 | | 7 800,00 |
| | | | | **Totaux** | **129 540,00** | **129 540,00** |

Les 6 portes en dépôt peuvent aussi être suivies dans un sous-compte dédié (ou au compte 38 « stocks mis en dépôt ») : leur identification facilite le rapprochement avec l'attestation du dépositaire.

## 4. Points d'attention / pièges

- **Erreur N-1** : ne pas « corriger » par une écriture supplémentaire dans le compte 31 : le stock initial erroné est soldé par l'écriture d'annulation du stock initial ; ajouter une écriture de 5 220 € ferait compter la correction **deux fois**.
- **Fiscalité de la correction** : si la réclamation 2025 est déposée, ne pas oublier la **réintégration de 5 220 €** en 2026 ; à défaut, double déduction (risque de redressement).
- **Bien de tiers** : le chêne de M. Dufresne est physiquement à l'atelier, rangé à part, et Antoine l'a valorisé (il « vaut » 6 080 €). Il n'est pas à la menuiserie. Si un incendie le détruisait, la menuiserie en répondrait vis-à-vis du client : vérifier l'assurance des **biens confiés**.
- **Stock en dépôt** : il n'est pas dans l'atelier, mais il est à la menuiserie. Sans **attestation** du dépositaire, pas de stock justifiable.
- **Ventes du dépositaire** : la vente est réalisée quand Déco Bois revend la porte, pas quand la menuiserie reçoit le relevé : facture à établir sur septembre.
- **Cut-off par les mouvements physiques** : la facture du 29/09 (quincaillerie) n'est pas un achat consommé de septembre ; celle du 02/10 (panneaux) en est un.
- **Agencement Saint-Just** : facturé n'est pas vendu. Il reste au stock à son **coût** (5 400 €), le CA de 7 800 € est neutralisé.
- **Capitaux propres** : la correction réduit les capitaux propres de 4 437 € (après IS). Avec la perte prévisionnelle de 180 000 €, le seuil de la moitié du capital social (art. L. 223-42 C. com.) est un sujet majeur : chaque euro compte dans le calcul, il faut des chiffres justes.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — Incidence des corrections d'inventaire** : stock corrigé 49 800,00 € contre 52 940,00 € dans l'inventaire d'Antoine, soit **– 3 140,00 €** de résultat de situation (– 6 080 de bois de tiers + 2 940 de portes en dépôt). Avec les régularisations de cut-off (+ 60,00 €), l'incidence totale de nos travaux par rapport aux chiffres bruts est de **– 3 080,00 €**. À cela s'ajoute la correction de l'erreur 2025 (– 5 220,00 €), déjà incluse mécaniquement dans la variation de stock.

**Paragraphe destiné au conciliateur (à valider par Hélène Ferrand) :**

> *Situation intermédiaire au 30/09/2026 — Stocks et en-cours. Les stocks et en-cours au 30/09/2026 (49 800 €) résultent d'un inventaire physique réalisé le 30/09/2026 en présence d'un collaborateur du cabinet. Ils excluent les biens confiés par des clients et incluent les produits finis détenus en dépôt par un revendeur, sur la base de son attestation. Les opérations de fin de période (factures non parvenues, factures à établir, produits et charges constatés d'avance) ont été régularisées. Les travaux ont mis en évidence une erreur de l'inventaire au 31/12/2025 (lot de bois compté deux fois, 5 220 €) : le résultat de l'exercice 2025 était surévalué de ce montant ; la correction est prise en compte dans le résultat de la période (variation de stock) et fera l'objet d'une information dans l'annexe des comptes 2026. Une réclamation sera déposée pour obtenir la restitution de l'IS correspondant (783 €).*

**Message à Antoine Girard (extrait)** : expliquer l'erreur du lot n° 14 sans dramatiser (erreur matérielle, sans intention), annoncer la réclamation d'IS, et proposer pour le 31/12/2026 : feuilles de comptage numérotées par zone, **étiquetage des lots** (n° de lot unique), zone « biens de clients » séparée et listée, demande d'attestation à Déco Bois au 31/12.

**Contrôles et documentation :**
- note de correction d'erreur (constat, chiffrage, feuilles 3 et 5 de l'inventaire 2025, confirmation écrite d'Antoine) ;
- préparation de la réclamation 2025 (avec Hélène Ferrand) et mention de la réintégration de 5 220 € dans le dossier fiscal 2026 ;
- attestation Déco Bois, contrat de dépôt, relevé des ventes de septembre ;
- devis Dufresne (preuve que le bois appartient au client) ;
- feuille de cut-off (derniers BL d'entrée et de sortie, factures autour du 30/09) ;
- à la clôture du 31/12/2026 : refaire l'ensemble de ces contrôles, et tester la **dépréciation** du stock de bois (rotation lente en période de baisse d'activité).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- PCG (règlement ANC n° 2014-03 modifié par le règlement ANC n° 2022-06) : changements de méthodes, changements d'estimations et corrections d'erreurs (correction dans le résultat de l'exercice de découverte, information en annexe) ; résultat exceptionnel restreint ; comptes 31, 32, 33, 355, 38, 4181, 44586, 44587, 486, 487, 6031, 6032, 7133, 7135.
- Code de commerce art. L. 123-12 (inventaire), L. 123-14 (image fidèle), L. 223-42 (capitaux propres inférieurs à la moitié du capital social), L. 611-4 et suivants (conciliation).
- CGI art. 38-4 bis (correction symétrique des bilans), art. 220 quinquies (report en arrière des déficits) ; LPF art. R*196-1 (délai de réclamation).
- CGI art. 269 (exigibilité de la TVA : livraison de biens, encaissement pour les travaux immobiliers).
