# E05-03 — Emprunt de la Pharmacie Centrale : tableau d'amortissement et intérêts courus au 30/09
**Client :** C12 — Pharmacie Centrale SELARL | **Difficulté :** ★★☆ | **Durée estimée :** 60 min | **Thèmes :** emprunt, tableau d'amortissement, 164 / 661 / 616, frais de dossier, intérêts courus 1688, état des échéances

**Corner case :** non (mais une saisie erronée toute l'année à corriger)

## La mise en situation

Clôture du 30/09/2026 de la Pharmacie Centrale. Le cabinet assure la révision ; la saisie est faite par l'assistante de la pharmacie, Mme Gauthier, qui vous écrit :

> « Bonjour, pour le prêt des travaux je n'ai pas le tableau d'amortissement, le Dr Petit l'a reçu par courrier et ne le retrouve pas. J'ai tout passé au compte d'emprunt, je pense que c'est bon puisque c'est le prêt qu'on rembourse. Cordialement, Sylvie Gauthier »

Hélène Ferrand : « Reconstituez le tableau avec l'offre de prêt, corrigez, et contrôlez que le 164 colle au capital restant dû. N'oubliez pas les courus et l'état des échéances pour l'annexe. »

## Les pièces

### Pièce 1 — Offre de prêt (extrait des conditions particulières)

```
CRÉDIT AGRICOLE CENTRE-EST — Agence Lyon Bellecour
OFFRE DE PRÊT PROFESSIONNEL n° 0071-2025-PRO — émise le 14/10/2025, acceptée le 28/10/2025
Emprunteur : SELARL PHARMACIE CENTRALE — 1 place Bellecour 69002 Lyon — SIREN 820 444 555
Objet : financement de travaux d'agencement de l'officine et d'un robot de dispensation
Montant : 240 000,00 EUR
Durée : 60 mois — Amortissement : échéances mensuelles constantes (hors assurance)
Taux nominal annuel fixe : 3,90 % — Taux périodique mensuel : 0,325 %
Date de déblocage : 05/11/2025 — Première échéance : 05/12/2025 — Dernière échéance : 05/11/2030
Frais de dossier : 1 200,00 EUR, prélevés sur le montant débloqué
Assurance décès-invalidité (tête assurée : Dr Anne Petit, bénéficiaire : la banque à hauteur
du capital restant dû) : 0,30 % l'an du capital initial, soit 60,00 EUR par mois, prélevée avec l'échéance
Garanties : nantissement du fonds de commerce en 2e rang ; caution personnelle et solidaire
du Dr Anne Petit à hauteur de 120 000,00 EUR
Calcul des intérêts : sur la base du taux périodique appliqué au capital restant dû
```

### Pièce 2 — Extraits du relevé bancaire
```
06/11/2025  DEBLOCAGE PRET 0071-2025-PRO NET DE FRAIS          + 238 800,00
05/12/2025  ECHEANCE PRET 0071-2025-PRO N° 001                   - 4 469,14
05/01/2026  ECHEANCE PRET 0071-2025-PRO N° 002                   - 4 469,14
...  (une échéance identique chaque 5 du mois)
05/09/2026  ECHEANCE PRET 0071-2025-PRO N° 010                   - 4 469,14
```

### Pièce 3 — Grand livre du compte 164 au 30/09/2026 (avant révision)

| Date | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|
| 06/11/2025 | Déblocage prêt CA 0071 | | 238 800,00 | 238 800,00 C |
| 05/12/2025 → 05/09/2026 | Échéances n° 1 à 10 (10 × 4 469,14) | 44 691,40 | | 194 108,60 C |
| | **Solde au 30/09/2026** | | | **194 108,60 C** |

Les comptes 661 et 616 ne contiennent aucune écriture relative à ce prêt.

## Travail à faire
1. Calculez la mensualité hors assurance et vérifiez-la avec le montant prélevé.
2. Établissez le tableau d'amortissement de l'échéance n° 1 à l'échéance n° 22 (05/09/2027).
3. Déterminez, pour l'exercice du 01/10/2025 au 30/09/2026 : les intérêts, le capital remboursé, l'assurance, et le capital restant dû au 30/09/2026.
4. Analysez les erreurs de saisie et passez les écritures de correction.
5. Calculez et comptabilisez les intérêts courus au 30/09/2026 (convention bancaire exact/360 ; vérifiez par une seconde méthode) et indiquez l'écriture du 01/10/2026.
6. Préparez l'état des échéances de l'emprunt pour l'annexe et listez les engagements hors bilan liés à ce prêt.
7. Passez l'écriture de l'échéance du 05/10/2026.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E05-03_corrige.md)
