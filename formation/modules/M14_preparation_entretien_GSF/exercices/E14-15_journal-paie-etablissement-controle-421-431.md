# E14-15 — Journal de paie mensuel d'un établissement : comptabiliser et contrôler 421, 425, 431 avec la DSN
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Nice | **Difficulté :** ★★★ | **Durée estimée :** 60 min | **Thèmes :** paie dans la propreté (temps partiels, heures complémentaires, primes conventionnelles et indemnités de frais), IJSS en subrogation, acomptes, prélèvement à la source, versement mobilité, écriture de paie centralisée, contrôles 421 / 425 / 431 / DSN

**Corner case :** oui — le compte 431 ne correspond pas à la DSN : l'écart vient d'un paramétrage comptable, pas d'une erreur de paie

> *Cadre de formation : sociétés, salariés, montants et personnes fictifs. Les taux ne sont pas à recalculer : les montants sont donnés par le logiciel de paie.*

## La mise en situation

Vendredi 02/10/2026. La paie de septembre de l'établissement de Nice (40 salariés, dont 34 à temps partiel, horaires décalés sur 11 sites) a été calculée et versée le 30/09 par le service paie du siège. L'interface paie → comptabilité a généré l'écriture centralisée. Sophie Garnier (personnage fictif) vous demande :

> « Avant de valider l'écriture de paie de Nice, faites les trois contrôles habituels : le 421 doit être soldé par les virements, le 425 doit retomber à zéro, et le 431 doit correspondre à la DSN. S'il y a des écarts, je veux leur explication, pas un "écart de paie" en 658. »

Comptes : 6411 Salaires, appointements ; 6413 Primes et gratifications ; 6414 Indemnités et avantages divers ; 6451 Cotisations à l'URSSAF ; 6452 Cotisations aux mutuelles et à la prévoyance ; 6453 Cotisations aux caisses de retraite ; 6331 Versement mobilité ; 421 Personnel – rémunérations dues ; 425 Personnel – avances et acomptes ; 431 Sécurité sociale (URSSAF) ; 4371 Caisses de retraite complémentaire ; 4372 Mutuelle / prévoyance ; 4387 Organismes sociaux – produits à recevoir (IJSS subrogation) ; 4421 État – prélèvement à la source ; 447 Autres impôts, taxes et versements assimilés ; 512.

## Les pièces

**Pièce 1 — Journal de paie récapitulatif, établissement de Nice, septembre 2026**
```
Effectif payé : 40 (dont 34 temps partiels) – Heures payées : 4 286 h
                                                                    Montant
Salaire de base (heures contractuelles)                            52 480,00
Heures complémentaires (majorées 10 % et 25 %)                      3 260,00
Prime de salissure (conventionnelle)                                1 120,00
Prime d'ancienneté                                                  1 940,00
Absences maladie (déduction)                                       -4 860,00
Complément employeur de maintien de salaire                         1 580,00
SALAIRE BRUT                                                       55 520,00
Cotisations salariales URSSAF (y c. CSG/CRDS)                      -8 994,24
Cotisations salariales retraite complémentaire                     -2 442,88
Cotisations salariales mutuelle / prévoyance                         -777,28
Indemnités de panier (frais professionnels, non soumises)           1 360,00
Prise en charge frais de transport (non soumise)                      980,00
IJSS nettes avancées (subrogation, 7 salariés)                      2 870,40
NET À PAYER AVANT IMPÔT                                            48 516,00
Prélèvement à la source                                            -1 410,30
Acomptes versés le 15/09                                           -3 200,00
NET À PAYER                                                        43 905,70

Charges patronales : URSSAF (après réduction générale) 9 438,40 ;
retraite complémentaire 3 664,32 ; mutuelle / prévoyance 1 165,92 ;
versement mobilité 1 110,40
```

**Pièce 2 — Écriture générée par l'interface paie (journal OD-PAIE, 30/09/2026)**

| Compte | Débit | Crédit |
|---|---|---|
| 6411 | 54 400,00 | |
| 6413 | 1 120,00 | |
| 6414 | 2 340,00 | |
| 4387 | 2 870,40 | |
| 6451 | 9 438,40 | |
| 6453 | 3 664,32 | |
| 6452 | 1 165,92 | |
| 6331 | 1 110,40 | |
| 431 | | 18 432,64 |
| 4371 | | 6 107,20 |
| 4372 | | 1 943,20 |
| 4421 | | 1 410,30 |
| 425 | | 3 200,00 |
| 421 | | 43 905,70 |
| 447 | | 1 110,40 |

**Pièce 3 — Extraits bancaires et grand livre**
- 15/09 : virement des acomptes de septembre : 3 200,00 €.
- Grand livre 425 au 31/08/2026 : solde débiteur **150,00 €** (acompte d'août de M. R. Silva, non repris sur la paie d'août).
- 30/09 : virement des salaires (fichier SEPA) : **43 905,70 €**.
- 02/10 : retour de virement « compte clos » : **612,35 €** (Mme A. Costa). Nouvelle domiciliation reçue et contrôlée le 02/10 ; virement le 05/10.

**Pièce 4 — DSN de septembre (établissement de Nice), bordereau URSSAF** : total des cotisations dues à l'URSSAF : **19 543,04 €**, dont versement mobilité 1 110,40 € (taux retenu 2 % — *à vérifier selon l'autorité organisatrice de la mobilité*).

## Travail à faire

1. Vérifiez la cohérence arithmétique du journal de paie (brut, net avant impôt, net à payer) et l'équilibre de l'écriture d'interface.
2. Expliquez le traitement des IJSS subrogées (pourquoi 4387 et non un produit, et pourquoi pas de compte 791).
3. Contrôle 421 : passez les écritures de paiement (30/09, 02/10, 05/10) et justifiez le solde du 421 au 30/09.
4. Contrôle 425 : quel est le solde après la paie ? Que faites-vous ?
5. Contrôle 431 / DSN : expliquez l'écart et passez l'écriture de correction.
6. Calculez le coût employeur total du mois et le coût moyen par salarié ; citez deux indicateurs que le contrôle de gestion suivra pour un établissement de propreté.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-15_corrige.md)
