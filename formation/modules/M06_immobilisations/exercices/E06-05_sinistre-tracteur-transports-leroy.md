# E06-05 — Le tracteur détruit en novembre, l'indemnité payée en février
**Client :** C11 — Transports Leroy SAS | **Difficulté :** ★★★ | **Durée estimée :** 1 h | **Thèmes :** sinistre, sortie d'actif, indemnité d'assurance (produit à recevoir), événements postérieurs à la clôture, remboursement de frais sans compte de transfert de charges, franchise, TVA hors champ

**Corner case :** oui — l'indemnité n'est chiffrée définitivement qu'après la clôture, et la proposition de saisie la rattache à 2027.

## La mise en situation

Lundi 1er février 2027. Révision des comptes 2026 de Transports Leroy (clôture 31/12/2026, arrêté des comptes prévu le 15/03/2027).

Le 14/11/2026, le tracteur Scania GK-731-LR a été détruit dans un accident sur l'A43 (chaussée verglacée, aucun tiers en cause). Le chauffeur est indemne ; la marchandise transportée (produits laitiers) a été en partie perdue.

Votre collègue Théo, junior lui aussi, a préparé la note suivante :

> « Le camion figure toujours dans le fichier, je l'ai amorti sur toute l'année 2026 (22 000 €). L'assurance a payé le 15/02/2027… enfin elle va payer, c'est annoncé dans le courrier du 22/01 : on comptabilisera l'indemnité en 2027 quand on la recevra. Le remorquage, je l'ai mis en charge. Pour le client laitier, on attend. »

Hélène Ferrand : « Reprenez tout. Je veux l'analyse du rattachement de l'indemnité, les écritures 2026, et l'impact sur le résultat par rapport à la proposition de Théo. »

## Les pièces

**Pièce 1 — Fiche d'immobilisation**

```
N° V-2023-07 — Tracteur routier Scania R450 4x2 — immatriculation GK-731-LR — compte 2182
Mise en service : 01/07/2023 — Valeur d'origine : 132 000,00 € HT (TVA déduite)
Linéaire 6 ans — Amortissements cumulés au 31/12/2025 : 55 000,00 €
```

**Pièce 2 — Courrier de l'assureur du 05/12/2026**

```
MUTUELLE DES TRANSPORTEURS DU RHÔNE — Service sinistres flotte
Contrat flotte n° FL-2019-88412 — Garanties : responsabilité civile, dommages tous accidents
(franchise 2 000 € par sinistre), frais de remorquage et de gardiennage, marchandises
transportées (franchise 1 000 € par sinistre).
Objet : sinistre n° 26-11-03977 du 14/11/2026 — véhicule GK-731-LR
Madame, Monsieur, nous accusons réception de votre déclaration. Les circonstances relevées
(perte de contrôle sur chaussée verglacée) relèvent de la garantie « dommages tous accidents ».
Un expert a été missionné. Nous vous ferons connaître notre proposition d'indemnisation à
réception de son rapport.
```

**Pièce 3 — Rapport d'expertise du 10/12/2026 (extrait)**

```
Cabinet EXPERTS AUTO POIDS LOURDS RHÔNE-ALPES — Rapport n° 26-PL-1121
Véhicule : Scania R450 GK-731-LR — 3 ans et 4 mois — 398 000 km
Conclusion : véhicule économiquement irréparable (coût de remise en état 112 400 € HT
supérieur à la valeur de remplacement).
Valeur de remplacement à dire d'expert (VRADE) HT : 78 000 €
Épave : cession à l'assureur (valeur de sauvetage intégrée à la proposition).
```

**Pièce 4 — Courrier de l'assureur du 22/01/2027**

```
Proposition d'indemnisation — sinistre n° 26-11-03977
  Garantie dommages : VRADE HT 78 000,00 € – franchise 2 000,00 €        76 000,00 €
  Frais de remorquage et de gardiennage (facture Dépannage Alpes Poids Lourds) 1 850,00 €
  Total (assuré récupérant la TVA : indemnité calculée hors taxes)         77 850,00 €
Règlement par virement sous 15 jours à réception de votre accord et du certificat
d'immatriculation barré.
Marchandises transportées : nous indemnisons directement votre client, la Laiterie des Monts
du Lyonnais, à hauteur de son préjudice (6 400 €) sous déduction de votre franchise (1 000 €),
que vous lui réglerez directement.
```
Accord de Transports Leroy envoyé le 25/01/2027. Virement de 77 850,00 € reçu le 15/02/2027.

**Pièce 5 — Facture de remorquage**

```
DÉPANNAGE ALPES POIDS LOURDS SARL — 73000 Chambéry — SIREN 489 220 731 — TVA FR 38 489 220 731
FACTURE N° DAPL-26-0912 du 20/11/2026 — Client : TRANSPORTS LEROY SAS (SIREN 803 909 101)
Nature : prestation de services
Remorquage poids lourd A43 + gardiennage 10 jours                      HT 1 850,00
                                                                     TVA 20 %  370,00
                                                                         TTC 2 220,00
Payée par virement le 15/12/2026.
```

**Pièce 6 — Courrier de la Laiterie des Monts du Lyonnais (28/11/2026)**

```
Réclamation pour perte de marchandises — lettre de voiture LV-26-44107 du 14/11/2026 :
préjudice chiffré à 6 400 € (32 palettes de yaourts). Nous vous tenons pour responsable
en votre qualité de transporteur.
```
Transports Leroy a reconnu sa responsabilité le 02/12/2026. La franchise de 1 000 € a été payée à la Laiterie le 10/02/2027.

**Paramètres** : convention du cabinet — mois de 30 jours ; le bien est amorti jusqu'au jour du sinistre inclus.

## Travail à faire

1. Calculez la dotation 2026 du tracteur, sa VNC à la date du sinistre et le résultat de la sortie.
2. L'indemnité doit-elle être rattachée à 2026 ou à 2027 ? Raisonnez à partir des pièces (dates, nature des événements) et des principes comptables.
3. Comment traiter le remboursement des frais de remorquage, sachant que le compte 791 n'existe plus ? Et la réclamation de la Laiterie ?
4. Passez toutes les écritures de 2026 (et l'encaissement de 2027).
5. Chiffrez l'écart de résultat 2026 entre la proposition de Théo et la vôtre.
6. Que feriez-vous si l'assureur avait contesté sa garantie (par exemple pour non-conformité du chronotachygraphe) ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E06-05_corrige.md)
