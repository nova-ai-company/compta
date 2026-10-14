# E14-04 — Client public : facture déposée sur Chorus Pro, paiement à 75 jours, intérêts moratoires et indemnité de 40 €
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Cannes | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** facturation des entités publiques via Chorus Pro, délai global de paiement de la commande publique, point de départ du délai, intérêts moratoires, indemnité forfaitaire pour frais de recouvrement, TVA sur les encaissements

**Corner case :** oui — la facture a été rejetée une première fois par Chorus Pro par la faute de GSF Riviera : le délai ne court pas de la date du premier dépôt

> *Cadre de formation : le « Centre hospitalier de Grasse » est utilisé ici comme client fictif ; ses identifiants, le marché et les montants sont inventés. Les autres sociétés et personnes sont fictives.*

## La mise en situation

Vendredi 09/10/2026. Julien Roux, chef de l'établissement de Cannes (personnage fictif), passe au service comptable :

> « Le centre hospitalier nous a payé la facture de juin au bout de 75 jours. C'est un marché public : ils nous doivent des intérêts, non ? Combien, et comment on les réclame ? Je voudrais aussi comprendre pourquoi on ne les a pas reçus automatiquement. »

Informations :
- Délai global de paiement retenu pour un **établissement public de santé** : **50 jours** (Code de la commande publique — *valeur à vérifier* ; la fiche interne du service mentionnait 60 jours, ce qui doit être vérifié avant toute réclamation).
- Taux des intérêts moratoires : taux de la principale opération de refinancement de la BCE en vigueur au 1er jour du semestre civil au cours duquel les intérêts ont commencé à courir, **majoré de 8 points**. On retient un taux BCE de **2,15 % au 01/07/2026** (*valeur à vérifier*), soit **10,15 %**.
- Indemnité forfaitaire pour frais de recouvrement : **40 €** (*à vérifier*).
- Intérêts calculés sur le montant TTC resté impayé, jours exacts, base 365.
- TVA exigible sur les encaissements. Comptes : 411CHGR, 44574, 44571, 512, 4687 Divers – produits à recevoir, 763 Revenus des autres créances, 758 Produits divers de gestion courante (*subdivisions selon la nomenclature 2025 du PCG*).

## Les pièces

**Pièce 1 — Facture FR-2026-06-0301 (données de dépôt sur Chorus Pro)**
```
Émetteur : GSF RIVIERA SAS – SIRET 999 100 206 00034 (établissement de Cannes, fictif)
Destinataire : CENTRE HOSPITALIER DE GRASSE (fictif) – SIRET 999 200 311 00018
Code service exécutant : SERV-LOG-06 (fictif)
Numéro d'engagement juridique (bon de commande) : ................ (champ vide)
Marché n° 2024-CHG-PROP-03 – Lot 2 : bionettoyage des services de soins
Facture n° FR-2026-06-0301 du 30/06/2026 – période : juin 2026
Montant HT 46 250,00 € – TVA 20 % 9 250,00 € – TTC 55 500,00 €
Nature : prestation de services
Mode de paiement : virement – délai : conformément au CCP
```

**Pièce 2 — Historique Chorus Pro**

| Date | Événement |
|---|---|
| 01/07/2026 | Dépôt FR-2026-06-0301 |
| 02/07/2026 | Statut « Rejetée » — motif : numéro d'engagement juridique absent |
| 06/07/2026 | Nouveau dépôt avec engagement n° EJ-2026-0458 (fictif) — statut « Déposée » |
| 07/07/2026 | Statut « Mise à disposition du destinataire » |
| 28/07/2026 | Statut « Service fait » |
| 11/09/2026 | Statut « Mandatée » |
| 14/09/2026 | Statut « Mise en paiement » |

**Pièce 3 — Relevé bancaire**

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 14/09/2026 | VIR DGFIP TRESORERIE HOSPITALIERE FR-2026-06-0301 | | 55 500,00 |

## Travail à faire

1. Déterminez le point de départ du délai de paiement, la date limite de paiement et le nombre de jours de retard. Justifiez pourquoi le premier dépôt du 01/07 ne compte pas.
2. Calculez les intérêts moratoires et l'indemnité forfaitaire. Comparez avec ce que Julien Roux aurait obtenu en partant du 01/07.
3. Expliquez le régime TVA des intérêts moratoires et de l'indemnité.
4. Passez les écritures : encaissement du 14/09 (avec la TVA), constatation de la créance d'intérêts et d'indemnité le 09/10 (demande déposée sur Chorus Pro), encaissement le 30/10/2026.
5. Listez les contrôles à mettre en place pour que les factures publiques de GSF Riviera ne soient plus rejetées.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-04_corrige.md)
