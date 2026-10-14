# E03-07 — Un client en redressement, puis en liquidation judiciaire
**Client :** C24 — Menuiserie Bois & Création SARL | **Difficulté :** ★★★ | **Durée estimée :** 1 h 15 | **Thèmes :** créances douteuses, déclaration de créance, dépréciation, récupération de TVA sur créance irrécouvrable, TVA sur encaissements des travaux, perte définitive, événement post-clôture

**Corner case :** oui — une des deux factures porte sur des travaux immobiliers (TVA jamais exigible), et un paiement a été reçu en période suspecte

## La mise en situation

Menuiserie Bois & Création traverse une période difficile (CA en baisse de 25 %). Son plus gros client, la SAS **Boutiques Vallon**, chaîne de magasins de décoration, a été placé en redressement judiciaire en mars, puis en liquidation judiciaire en septembre. Antoine Girard, gérant, vous écrit le 9 octobre 2026 :

> Bonjour, je vous transmets le courrier du liquidateur reçu cette semaine. J'avais fait la déclaration de créance moi-même en avril, j'espère que c'était bon. Delta Invest (la holding) me demande combien on va perdre exactement et si on peut au moins récupérer la TVA. Merci, Antoine

Hélène Ferrand : *« Faites le point complet. Et regardez les dates : les comptes 2025 ont été arrêtés le 27 mars, je veux savoir si on aurait dû déprécier dès 2025. »*

## Les pièces

### Pièce 1 — Extrait du compte client 411 VALLON au 09/10/2026

| Date | Pièce | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|---|
| 28/11/2025 | F-2025-118 | Fourniture et livraison de 4 comptoirs et 12 meubles d'exposition sur mesure (livraison le 26/11/2025) — HT 25 000,00, TVA 20 % 5 000,00 | 30 000,00 | | 30 000,00 D |
| 15/01/2026 | VIR | Règlement partiel F-2025-118 | | 6 000,00 | 24 000,00 D |
| 20/02/2026 | F-2026-021 | Travaux de pose et fixation d'agencements au magasin de Vienne (travaux immobiliers) — HT 9 000,00, TVA 20 % 1 800,00 | 10 800,00 | | 34 800,00 D |

La TVA de F-2025-118 a été déclarée en novembre 2025. Celle de F-2026-021 est en **44574** (TVA sur encaissements, pas d'option pour les débits). Aucune autre écriture n'a été passée sur ce client en 2026.

### Pièce 2 — Annonce BODACC (extrait)

```
BODACC A – n° 20260055 – publié le 19/03/2026 – Procédures collectives
SAS BOUTIQUES VALLON – SIREN 789 004 512 – 40 rue Président Édouard Herriot – 69002 Lyon
Jugement du Tribunal des activités économiques de Lyon du 10/03/2026 prononçant l'ouverture
d'une procédure de REDRESSEMENT JUDICIAIRE – Date de cessation des paiements : 01/12/2025
Mandataire judiciaire : SELARL MJ Confluence, Me Ravel – Les créances sont à déclarer
auprès du mandataire dans les deux mois de la présente publication.
```

### Pièce 3 — Copie de la déclaration de créance envoyée par Antoine (LRAR du 28/04/2026)

```
Déclaration de créance – Débiteur : SAS Boutiques Vallon – Mandataire : Me Ravel
Créancier : Menuiserie Bois & Création SARL – SIREN 811 010 202
Nature : créance chirographaire, échue
  Facture F-2025-118 du 28/11/2025 – solde                          24 000,00 € TTC
  Facture F-2026-021 du 20/02/2026                                  10 800,00 € TTC
  TOTAL DÉCLARÉ                                                     34 800,00 € TTC
Pièces jointes : copies des factures, relevé de compte. Signé : A. Girard, gérant.
```

### Pièce 4 — Courrier du liquidateur du 02/10/2026

```
SELARL MJ Confluence – Me Ravel, liquidateur judiciaire
Objet : SAS Boutiques Vallon – conversion en liquidation judiciaire
Par jugement du 22/09/2026, le Tribunal a converti la procédure en LIQUIDATION JUDICIAIRE.
Votre créance a été admise au passif à titre chirographaire pour 34 800,00 €.
En l'état, l'actif réalisable ne permet d'envisager AUCUNE répartition au profit des créanciers
chirographaires. Un certificat d'irrécouvrabilité pourra vous être délivré à la clôture de la procédure.
Par ailleurs, j'examine les paiements intervenus depuis la date de cessation des paiements (01/12/2025).
```

## Travail à faire

1. Vérifiez la déclaration de créance (délai, montant, nature).
2. Analysez les deux factures au regard de la TVA : quel montant de TVA peut être « récupéré », à quelle date, à quelles conditions et sur quelle ligne de la CA3 ?
3. Passez toutes les écritures nécessaires : en mars 2026, à la date de la régularisation de TVA, au 31/12/2026, puis, par anticipation, à la clôture de la liquidation.
4. Répondez à Hélène : aurait-on dû déprécier la créance dans les comptes 2025 ?
5. Quel risque présente le paiement de 6 000 € du 15/01/2026 ? Faut-il le traduire dans les comptes ?
6. Répondez à Delta Invest : quelle est la perte définitive pour Menuiserie Bois & Création ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E03-07_corrige.md)
