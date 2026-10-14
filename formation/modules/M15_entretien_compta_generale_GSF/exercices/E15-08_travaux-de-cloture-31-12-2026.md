# E15-08 — Test technique : sept travaux de clôture au 31/12/2026 et leurs extournes
**Client :** GSF Riviera SAS (filiale régionale **fictive**, siège à Nice) — service comptable | **Difficulté :** ★★☆ | **Durée estimée :** 45 min (test chronométré) | **Thèmes :** factures non parvenues, factures à établir, charges constatées d'avance, intérêts courus, provision pour litige, créance douteuse et dépréciation sur le HT, variation de stock, écritures d'extourne au 01/01

**Corner case :** oui — l'établissement propose de déprécier la créance douteuse sur le TTC, et il faut savoir quelles écritures **ne s'extournent pas**

> *Cadre de formation : sociétés, documents et personnes fictifs.*

## La mise en situation

Dernière partie de l'entretien chez GSF Riviera SAS. Laurent Vidal, chef comptable (personnage fictif), vous tend une feuille : « On se place en **janvier 2027**, pendant la clôture de l'exercice 2026. Voici sept informations remontées par les établissements. Pour chacune, je veux l'écriture au 31/12/2026, et me dire si on l'extourne au 01/01/2027. Vous avez **45 minutes**. C'est exactement ce que vous ferez chaque année en janvier chez nous. »

Rappels (fictifs) : exercice du 01/01 au 31/12 ; TVA sur les prestations de services de GSF Riviera exigible **à l'encaissement** (pas d'option pour les débits) ; plan de comptes conforme au PCG : 4081 Fournisseurs – factures non parvenues, 4181 Clients – factures à établir, 44586 TVA sur factures non parvenues, 44587 TVA sur factures à établir, 486 Charges constatées d'avance, 1688 Intérêts courus, 1511 Provisions pour litiges, 416 Clients douteux, 491 Dépréciations des comptes clients, 322 Stocks de fournitures consommables (produits d'entretien), 6032 Variation des stocks des autres approvisionnements, 611 Sous-traitance générale, 616 Primes d'assurances, 706 Prestations de services, 6611 Intérêts des emprunts, 6815 Dotations aux provisions d'exploitation, 6817 Dotations aux dépréciations des actifs circulants.

## Les pièces

**Information 1 — Sous-traitance de décembre non facturée (établissement de Nice)**
```
ATTACHEMENT DE TRAVAUX signé le 22/12/2026
VITRES CÔTE D'AZUR SARL – SIREN 999 733 052 (fictif)
Nettoyage des vitres en hauteur – Centre d'affaires Arenas, décembre 2026
Montant convenu : 6 800,00 € HT – TVA 20 %
La facture arrivera via la plateforme agréée le 12/01/2027.
```

**Information 2 — Prestation réalisée en décembre, facturée en janvier (établissement de Cannes)**
```
Remise en état après travaux – Résidence Les Oliviers (syndic fictif)
Prestation terminée et réceptionnée le 18/12/2026
Facture qui sera émise le 08/01/2027 : 4 250,00 € HT + TVA 20 %
```

**Information 3 — Assurance de la flotte de véhicules**
```
Avis d'échéance ASSURANCES DU LITTORAL (fictif)
Contrat flotte automobile – période du 01/10/2026 au 30/09/2027
Prime annuelle : 14 400,00 € (taxe sur les conventions d'assurance comprise, pas de TVA)
Comptabilisée en totalité en 616 le 01/10/2026 et payée.
```

**Information 4 — Emprunt bancaire (prêt matériel)**
```
Capital restant dû après l'échéance du 30/11/2026 : 84 000,00 €
Taux nominal annuel : 3,60 % – échéances TRIMESTRIELLES (intérêts payés à terme échu)
Dernière échéance payée : 30/11/2026 – prochaine échéance : 28/02/2027
```

**Information 5 — Litige prud'homal**
```
Ancien chef d'équipe (licencié en juin 2026) : demande de 28 000,00 € devant le conseil
de prud'hommes. Lettre de l'avocat de GSF Riviera du 08/01/2027 :
« Le risque de condamnation est probable ; nous l'estimons à 12 000,00 €. »
```

**Information 6 — Client en difficulté (établissement de Nice)**
```
SYNDIC AZUR GESTION SAS – SIREN 999 281 640 (fictif) – placé en redressement judiciaire
le 03/12/2026.
Créance au 31/12/2026 : facture VT-26-1187 du 15/10/2026 : 6 000,00 € HT + 1 200,00 € TVA
= 7 200,00 € TTC, non réglée.
Risque de perte estimé par le directeur d'agence : 60 %.
Proposition de l'établissement : « dépréciation 7 200 × 60 % = 4 320,00 € ».
```

**Information 7 — Inventaire des produits d'entretien**
```
Stock de produits d'entretien au 01/01/2026 (compte 322) : 23 450,00 €
Inventaire physique valorisé au 31/12/2026 (coût d'achat) : 19 870,00 €
```

## Travail à faire

1. Pour chaque information, dites en une phrase **quel principe** s'applique (rattacher la charge ou le produit au bon exercice, prudence…).
2. Calculez les montants (montrez le calcul) et **corrigez la proposition** de l'information 6 si nécessaire.
3. Passez toutes les écritures d'inventaire au **31/12/2026**.
4. Passez les écritures d'**extourne** au **01/01/2027**, et expliquez pourquoi certaines écritures **ne s'extournent pas**.
5. Calculez l'**impact net** de ces sept écritures sur le résultat 2026 (en plus ou en moins).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-08_corrige.md)
