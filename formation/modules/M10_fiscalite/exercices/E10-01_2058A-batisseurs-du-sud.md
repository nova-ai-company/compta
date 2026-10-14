# E10-01 — Le 2058-A complet de Bâtisseurs du Sud, l'IS 2026 et les acomptes 2027
**Client :** C02 — Bâtisseurs du Sud SAS | **Difficulté :** ★★★ | **Durée estimée :** 1 h 30 | **Thèmes :** 2058-A, réintégrations/déductions, IS 15 %/25 %, mécénat, acomptes, groupe intégré

**Corner case :** oui — la société est membre du groupe intégré Delta Invest : l'IS ne se paie pas au Trésor mais à la société mère.

## La mise en situation

Lundi 1er février 2027, 8 h 40. Nadia, la comptable interne de Bâtisseurs du Sud, vous transmet la balance provisoire 2026 et un fichier Excel intitulé « trucs fiscaux 2026 ». Elle écrit :

> « Bonjour, voici la liste des points que j'ai notés pendant l'année. Je ne sais pas lesquels sont à réintégrer, j'ai tout mis en vrac. J'ai passé les acomptes d'IS en 695 comme d'habitude. Karim veut connaître le montant d'IS 2026 et ce qu'il faudra verser en 2027 pour préparer son plan de trésorerie. Merci ! Nadia »

Note d'Hélène Ferrand jointe au dossier :

> « Rappel : Bâtisseurs est intégrée fiscalement chez Delta Invest (C10) depuis 2019. Convention d'intégration de **neutralité** : la filiale verse à la mère, aux échéances légales, l'IS (et les acomptes) qu'elle aurait payés en l'absence d'intégration, réductions d'impôt comprises. Faites le 2058-A individuel, calculez l'IS "théorique", passez les écritures et préparez l'échéancier 2027 pour Karim. H.F. »

## Les pièces

**Pièce 1 — Extrait de la balance provisoire au 31/12/2026 (après écritures d'inventaire, avant IS)**

```
BÂTISSEURS DU SUD SAS — SIREN 812 450 776 — Balance provisoire au 31/12/2026
Compte   Intitulé                                         Débit         Crédit
451000   Groupe — Delta Invest (compte d'intégration)          0,00          0,00
455100   Compte courant Delta Invest (prêt d'associé)                  210 000,00
658xxx   Pénalités, amendes et dons (cf. détail)           13 120,00
6615     Intérêts des comptes courants                     12 000,00
681xxx   Dotations aux amortissements                     148 300,00
6815     Dotations aux provisions pour risques            37 000,00
695000   Impôt sur les bénéfices                          39 400,00
7615     Revenus des titres de participation                           12 000,00
7815     Reprises sur provisions pour risques                           8 000,00
...
RÉSULTAT PROVISOIRE (bénéfice, après le 695 ci-dessus)                214 860,00
Chiffre d'affaires HT 2026 : 3 420 000,00 €
```

**Pièce 2 — Le fichier « trucs fiscaux 2026 » de Nadia (reproduit tel quel)**

| N° | Ce que Nadia a noté | Montant | Compte |
|---|---|---|---|
| 1 | Acomptes IS 2026 versés à Delta Invest (15/03, 15/06, 15/09, 15/12 : 4 × 9 850 €) | 39 400,00 | 695 |
| 2 | PV de stationnement et amendes de non-désignation du conducteur (camionnettes) | 1 240,00 | 658 |
| 3 | Majorations de retard URSSAF (paiement tardif cotisations de mars) | 380,00 | 658 |
| 4 | Pénalités de retard de livraison versées à la SCCV Les Terrasses du Parc (art. 9 du marché : 1/1000e par jour) | 6 500,00 | 658 |
| 5 | Amortissement non déductible du SUV de Karim (calcul Nadia — voir E10-02) | 4 290,00 | 681 |
| 6 | Taxes annuelles CO₂ + polluants du SUV, charge à payer 2026 (calcul Nadia — voir E10-02) | 1 065,00 | 635 |
| 7 | Provision « aléas chantiers 2027 » (pas de chantier ni de risque identifié, « par prudence » dit Karim) | 15 000,00 | 6815 |
| 8 | Reprise de la provision « aléas » 2025 (elle avait été réintégrée sur la liasse 2025) | 8 000,00 | 7815 |
| 9 | Provision litige SCI Valfleuri (malfaçons dalle, rapport d'expert du 14/11/2026 chiffrant les reprises à 22 000 €) | 22 000,00 | 6815 |
| 10 | Journée de chasse en Sologne offerte à 6 clients promoteurs (location du territoire + traiteur) | 4 800,00 | 625 |
| 11 | Don à l'association « Les Restos du Cœur » (reçu fiscal Cerfa reçu) | 5 000,00 | 658 |
| 12 | Parrainage du club de rugby de Saint-Priest : logo Bâtisseurs sur les maillots et panneau au stade (facture avec TVA) | 3 000,00 | 623 |
| 13 | Intérêts du compte courant Delta Invest : 6 % sur un solde moyen de 200 000 € | 12 000,00 | 6615 |
| 14 | Dividendes reçus de la SA Béton Rhône (Bâtisseurs détient 12 % du capital, titres nominatifs achetés en 2018) | 12 000,00 | 7615 |
| 15 | Restaurants du week-end de Karim avec sa famille (notes « L'Auberge du Lac », samedis et dimanches) | 1 860,00 | 625 |

**Pièce 3 — Informations complémentaires**

```
- Capital social de Bâtisseurs du Sud : 100 000 €, entièrement libéré ; détenu à 100 % par Delta Invest,
  elle-même détenue à 100 % par Jean Delmas (personne physique).
- CA HT 2026 du groupe intégré (Delta + Bâtisseurs + Menuiserie) : 4 690 000 €.
- Taux maximum des intérêts de comptes courants déductibles (art. 39-1-3° CGI) pour un exercice
  de 12 mois clos le 31/12/2026 : on retient 4,79 % (valeur à vérifier chaque année).
  La société n'est pas en mesure de justifier qu'un établissement bancaire lui aurait prêté à 6 %.
- Béton Rhône n'est pas membre du groupe intégré.
- Résultat fiscal 2025 de Bâtisseurs du Sud : 174 600 € (IS 2025 : 39 400 €).
- Mécénat : réduction d'impôt de 60 % ; plafond = 20 000 € ou 5 ‰ du CA HT si ce montant est plus élevé
  (valeurs à vérifier chaque année).
- Taux d'IS : 15 % jusqu'à 42 500 €, 25 % au-delà.
```

## Travail à faire

1. Classez les 15 éléments : réintégration, déduction ou aucun retraitement. Justifiez chacun (une ligne + référence).
2. Établissez le tableau 2058-A et le résultat fiscal 2026.
3. Calculez l'IS 2026 « théorique » (convention de neutralité), la réduction d'impôt mécénat et le solde à verser à Delta Invest.
4. Passez les écritures de régularisation et de constatation de l'IS chez Bâtisseurs du Sud. Quel est le résultat comptable définitif ?
5. Établissez l'échéancier des acomptes 2027 à verser à Delta Invest (dates et montants).
6. Rédigez la réponse à Nadia sur la comptabilisation des acomptes.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E10-01_corrige.md)
