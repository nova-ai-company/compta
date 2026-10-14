# E01-04 — Lettrer un compte fournisseur qui « ne tombe pas juste »
**Client :** C16 — Hôtel Belle Vue | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** lettrage, paiements partiels, doublon, rapprochement avec le relevé fournisseur, facture manquante

**Corner case :** oui — une facture saisie deux fois (OCR + saisie manuelle) et une facture jamais transmise par le client

## La mise en situation

L'Hôtel Belle Vue clôture le **31/10/2026**. Pour préparer la révision, Hélène Ferrand vous demande de « nettoyer » les comptes fournisseurs. Le compte de la Blanchisserie du Gourguillon présente un solde créditeur de 4 620,00 € au 05/10/2026, alors qu'Olivier Garnier, le président, affirme : « On est à jour avec la blanchisserie, je paie tout ce qu'ils m'envoient. »

Le même jour, la Blanchisserie envoie par e-mail un relevé de compte avec ce mot : « Merci de bien vouloir régulariser le solde de 2 676,00 € dont une facture de banquet échue depuis le 16/09. »

Rappels : SAS, réel normal (CA3 mensuelle), toutes les factures de la blanchisserie sont soumises à la TVA à 20 %. Saisie des factures fournisseurs par l'outil de pré-comptabilisation (OCR) ; la réceptionniste saisit parfois « à la main » quand l'OCR tarde.

## Les pièces

**Pièce 1 — Extrait du grand livre (logiciel du cabinet)**

```
HÔTEL BELLE VUE SAS — Grand livre du 01/07/2026 au 05/10/2026
Compte 401BLAN — Blanchisserie du Gourguillon

Date        Jal  Pièce        Libellé                               Débit      Crédit    Let.
05/07/2026  AC   AC-0712      Blanchisserie F 2026-311 linge juin              1 860,00
10/07/2026  BQ   BQ-0731      Vir. Blanchisserie                1 860,00
04/08/2026  AC   AC-0803      Blanchisserie F 2026-352 linge juillet           2 340,00
06/08/2026  AC   AC-0821      Blanchisserie F 2026-352                         2 340,00
20/08/2026  BQ   BQ-0846      Vir. Blanchisserie acompte          1 500,00
03/09/2026  AC   AC-0904      Blanchisserie F 2026-398 linge août              2 610,00
08/09/2026  AC   AC-0919      Blanchisserie AV 2026-021 linge abîmé  210,00
15/09/2026  BQ   BQ-0938      Vir. Blanchisserie                    840,00
25/09/2026  BQ   BQ-0955      Vir. Blanchisserie                  2 400,00
02/10/2026  AC   AC-1004      Blanchisserie F 2026-441 linge sept.             2 280,00
                                                    Totaux       6 810,00   11 430,00
                                                    Solde créditeur          4 620,00
```

Note : l'écriture AC-0803 a été générée par l'OCR (pièce jointe : PDF de la facture) ; l'écriture AC-0821 a été saisie manuellement par la réceptionniste (pièce jointe : la même facture, scannée depuis l'exemplaire papier).

**Pièce 2 — Relevé de compte du fournisseur**

```
BLANCHISSERIE DU GOURGUILLON SARL — 27 rue du Bœuf, 69005 Lyon
SARL au capital de 15 000 € — RCS Lyon 612 448 390 — TVA FR88 612448390

RELEVÉ DE COMPTE CLIENT au 05/10/2026 — Client : HÔTEL BELLE VUE SAS (code C-0117)

Date        Référence       Libellé                          Débit       Crédit      Solde
05/07/2026  F 2026-311      Linge juin                     1 860,00                 1 860,00
10/07/2026  REG             Virement reçu                              1 860,00         0,00
04/08/2026  F 2026-352      Linge juillet                  2 340,00                 2 340,00
17/08/2026  F 2026-372      Nappes et serviettes banquet     396,00                 2 736,00
                            mariage 15/08 (échéance 16/09)
20/08/2026  REG             Virement reçu                              1 500,00     1 236,00
03/09/2026  F 2026-398      Linge août                     2 610,00                 3 846,00
08/09/2026  AV 2026-021     Avoir linge abîmé                            210,00     3 636,00
15/09/2026  REG             Virement reçu                                840,00     2 796,00
25/09/2026  REG             Virement reçu                              2 400,00       396,00
02/10/2026  F 2026-441      Linge septembre                2 280,00                 2 676,00
                                                        SOLDE DÛ AU 05/10/2026      2 676,00
```

**Pièce 3 — Ventilation HT/TVA des factures (facture 2026-352)** : 1 950,00 € HT + TVA 20 % 390,00 € = 2 340,00 € TTC.

## Travail à faire

1. Lettrez le compte 401BLAN : attribuez un code de lettrage à chaque groupe d'écritures qui se solde, et identifiez les écritures non lettrables.
2. Établissez le **rapprochement** entre le solde comptable (4 620,00 €) et le solde du fournisseur (2 676,00 €).
3. Passez les écritures de correction nécessaires (comptes de charge : 6155 « Entretien et réparations sur biens mobiliers — blanchissage » ; HT/TVA de la facture manquante : 330,00 € + 66,00 €). La facture 2026-372 sera reçue en copie le 12/10/2026.
4. Quelles conséquences sur la TVA ? Sur quelle déclaration régularisez-vous ?
5. Que faut-il faire si la copie de la facture 2026-372 n'est **pas** reçue avant la clôture du 31/10/2026 ?
6. Quelles mesures proposez-vous pour éviter que cela se reproduise ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E01-04_corrige.md)
