# E04-12 — Crédit de TVA remboursable et erreur sur une CA3 antérieure
**Client :** C25 — Studio Pixel SAS | **Difficulté :** ★★★ | **Durée estimée :** 1 h | **Thèmes :** crédit de TVA, report, demande de remboursement (formulaire 3519), régularisation d'une omission de TVA collectée sur une déclaration antérieure, chaîne des crédits reportés, intérêt de retard, contrôle de cohérence 44574

**Corner case :** oui — une omission de TVA collectée dans un mois « en crédit » qui provoque pourtant un retard de paiement le mois suivant, et une erreur de report de crédit

## La mise en situation

Studio Pixel (premier exercice de 16 mois, du 01/09/2025 au 31/12/2026) a opté pour le **réel normal** (CA3 mensuelles). Léo Martin, président, vous écrit le 9 octobre 2026 :

> Bonjour, on vient d'acheter le drone et les caméras, on a un gros crédit de TVA. Sarah dit qu'on peut se le faire rembourser, c'est vrai ? On en aurait bien besoin pour la trésorerie. Au fait, en préparant le dossier, Sarah s'est rendu compte que la facture Kanal Prod de juin n'apparaît pas dans la TVA de juin. Est-ce grave ?

On retient (*valeurs à vérifier chaque année*) : remboursement possible en cours d'année pour les redevables au réel normal lorsque le crédit de la période est au moins égal à **760 €** ; demande annuelle possible si le crédit au 31/12 est au moins égal à **150 €**.

## Les pièces

### Pièce 1 — Historique des CA3 déposées (extrait)

| Période | TVA brute (ligne 16) | TVA déductible (ligne 23, report inclus) | Crédit (ligne 25) | Remboursement demandé | Crédit reporté (ligne 27) |
|---|---|---|---|---|---|
| Juin 2026 | 1 400,00 | 4 000,00 | 2 600,00 | non | 2 600,00 |
| Juillet 2026 | 2 900,00 | 3 340,00 (dont report 2 600,00) | 440,00 | non | 440,00 |
| Août 2026 | 800,00 | 2 740,00 (dont report 440,00) | 1 940,00 | non | **2 380,00** ← *voir note* |

*Note : en août, le montant reporté a été saisi à 2 380,00 € ; vous vérifiez : 2 740,00 – 800,00 = 1 940,00. L'écart de 440,00 € provient d'un double report du crédit de juillet (déjà inclus dans la ligne 23).*

### Pièce 2 — Facture omise

```
STUDIO PIXEL SAS – 21 rue Mercière – 69002 Lyon – SIREN 952 777 888 – TVA FR 58 952777888
FACTURE N° SP-2026-014 du 05/06/2026 – Client : SAS KANAL PROD – SIREN 911 450 238
Réalisation de 4 vidéos et cession des droits d'exploitation pour une chaîne en ligne
HT 8 000,00 – TVA 20 % 1 600,00 – TTC 9 600,00 – payée par virement le 20/06/2026
```
En comptabilité : facture enregistrée (411 / 706 / 44574) et encaissement enregistré (512 / 411), mais **le transfert de la TVA de 44574 vers 44571 n'a pas été passé** : le 44574 présente encore 1 600,00 € pour cette facture.

### Pièce 3 — Données de septembre 2026

| Élément | HT | TVA |
|---|---|---|
| Prestations encaissées en septembre (TVA déjà transférée en 44571) | 11 000,00 | 2 200,00 |
| Drone professionnel (facture du 08/09/2026, payée) | 18 000,00 | 3 600,00 |
| Caméras et optiques (facture du 15/09/2026, payée) | 10 000,00 | 2 000,00 |
| Frais généraux (logiciels, loyer, téléphone) | 5 600,00 | 1 120,00 |

## Travail à faire

1. Analysez l'erreur de juin et l'erreur de report d'août : quelles conséquences sur la chaîne des crédits ? Y a-t-il un intérêt de retard ?
2. Indiquez comment régulariser (déclaration rectificative ou CA3 suivante, lignes concernées).
3. Établissez la CA3 de septembre 2026 corrigée (lignes 08 ou régularisation, 16, 19, 20, 22, 23, 25, 26, 27, 28).
4. Studio Pixel peut-elle demander le remboursement de son crédit ? Quel montant, quelle procédure, quels risques ?
5. Passez les écritures : facture des immobilisations, correction du 44574, liquidation de la CA3 de septembre avec demande de remboursement, encaissement du remboursement.
6. Que faut-il préparer pour le contrôle qui accompagnera probablement la demande ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E04-12_corrige.md)
