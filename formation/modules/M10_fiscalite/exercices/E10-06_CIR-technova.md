# E10-06 — Le crédit d'impôt recherche de TechNova : calcul et comptabilisation
**Client :** C08 — TechNova SAS | **Difficulté :** ★★★ | **Durée estimée :** 1 h | **Thèmes :** CIR, dépenses éligibles, forfait de fonctionnement, subventions, CII, comptabilisation (diminution d'IS ou subvention), 2058-A

**Corner case :** oui — confusion R&D / innovation et subvention Bpifrance oubliée.

## La mise en situation

Mardi 2 février 2027. Émilie Roux (DAF) envoie son projet de 2069-A :

> « Bonjour, voici mon calcul de CIR 2026 : 115 351 €. J'ai mis tout le monde de l'équipe tech, avec les pourcentages des feuilles de temps. Yanis voudrait que le CIR apparaisse en subvention pour améliorer l'EBITDA dans le reporting aux investisseurs ; l'an dernier le cabinet l'avait passé en diminution de l'IS. On fait quoi ? Émilie »

## Les pièces

**Pièce 1 — Tableau des temps et coûts 2026 (extrait du fichier RH, validé par les feuilles de temps mensuelles)**

| Salarié | Fonction / diplôme | Salaire brut annuel | Charges patronales effectivement supportées (JEI) | Temps sur le projet « Moteur d'optimisation sous contraintes » (R&D) | Temps sur « Nouvelle interface mobile » | Autres tâches |
|---|---|---|---|---|---|---|
| Yanis Haddad | Président, docteur en informatique | 72 000 € | 30 240 € | 40 % | — | 60 % (direction, commercial) |
| Amine Kaci | Ingénieur R&D | 58 000 € | 13 920 € | 80 % | — | 20 % (support) |
| Julie Perret | Ingénieure logiciel | 52 000 € | 12 480 € | 60 % | 20 % | 20 % |
| Hugo Tran | Data scientist | 55 000 € | 13 200 € | 100 % | — | — |
| Lisa Moreno | Développeuse front-end | 45 000 € | 10 800 € | — | 50 % | 50 % (maintenance) |

**Pièce 2 — Note technique (extrait du dossier justificatif)**

```
Projet "Moteur d'optimisation sous contraintes" : état de l'art réalisé (publications 2019-2025),
verrou identifié = résolution en temps réel de plannings > 5 000 contraintes hétérogènes ;
approche par heuristiques hybrides + apprentissage ; incertitude scientifique documentée,
journal de bord des essais, 2 échecs documentés.
Projet "Nouvelle interface mobile" : refonte UX, nouvelle application mobile de planification
(fonctionnalités inédites sur le marché des PME), pas d'incertitude scientifique.
```

**Pièce 3 — Autres données 2026**

```
- Serveur de calcul GPU acquis le 02/01/2026, affecté exclusivement au projet de recherche :
  dotation aux amortissements 2026 = 12 000 €.
- Sous-traitance au laboratoire privé agréé CIR "Optima Lab" (SIREN 843 112 790) : 30 000 € HT.
- Subvention Bpifrance "Aide pour projet d'innovation" encaissée le 15/04/2026 : 40 000 €,
  affectée au projet "Moteur d'optimisation" (comptabilisée en 74).
- IS brut 2026 (exercice E10-05) : 75 750 €.
- TechNova est une PME au sens communautaire.
```

**Pièce 4 — Paramètres retenus (valeurs à vérifier chaque année)**

```
Taux du CIR : 30 % des dépenses éligibles (jusqu'à 100 M€).
Dépenses de fonctionnement forfaitaires : 40 % des dépenses de personnel éligibles
+ 75 % des dotations aux amortissements des immobilisations affectées à la recherche.
(Émilie a utilisé l'ancien taux de 43 %.)
Subventions publiques reçues pour les opérations éligibles : déduites de la base l'année d'encaissement.
CII : 20 % (PME), dépenses plafonnées à 400 000 € — non calculé dans cet exercice.
```

## Travail à faire

1. Identifiez les erreurs du projet d'Émilie.
2. Calculez la base et le montant du CIR 2026 (tableau détaillé).
3. Quelles dépenses pourraient relever du CII ? (Identification seulement.)
4. Imputation sur l'IS 2026 et sort de l'excédent.
5. Comptabilisation : présentez les deux méthodes admises, leurs effets, et passez les écritures selon la méthode qui répond au souhait de Yanis. Que faut-il faire vis-à-vis de la méthode de l'an dernier ?
6. Indiquez le retraitement sur le 2058-A.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E10-06_corrige.md)
