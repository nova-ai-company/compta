# E15-15 — Cas de synthèse « Votre première semaine » : saisie, rapprochement, clôture du mois, TVA et mail
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) — établissement de Nice | **Difficulté :** ★★☆ | **Durée estimée :** 1 h | **Thèmes :** saisie de factures d'achat et d'une note de frais, seuil des 500 € HT, rapprochement bancaire court, TVA sur les encaissements, compte d'attente, facture non parvenue, charge constatée d'avance, TVA sur cadeaux d'affaires, mail pour pièce manquante

**Corner case :** oui — une dépense par carte bancaire sans justificatif : on ne la passe ni en charge ni en TVA déductible tant que la pièce n'est pas reçue

> *Cadre de formation : le groupe GSF est réel, mais **GSF Riviera SAS, les tiers, les personnes et tous les montants sont fictifs**.*

## La mise en situation

Dernière étape du recrutement : un test écrit d'une heure qui reproduit « votre première semaine ». Laurent Vidal, chef comptable (personnage fictif), vous laisse la consigne :

> « Imaginez qu'on est le lundi 02/11/2026 et que vous êtes arrivée la semaine dernière. Vous clôturez **octobre** pour l'établissement de Nice. Ne cherchez pas à tout faire parfaitement : faites les choses **dans l'ordre**, justifiez vos comptes, et signalez ce qui vous gêne. »

Rappels donnés avec le sujet :
- GSF Riviera facture des **prestations de services** **sans option pour les débits** : la TVA collectée est exigible à l'**encaissement**. Les factures de vente sont enregistrées avec la TVA en 44574 « TVA collectée en attente d'encaissement », virée en 44571 lors du paiement du client.
- Comptes : 401 (par fournisseur), 408, 411 (par client), 421 Personnel – rémunérations dues (sous-compte notes de frais), 44566, 44571, 44574, 44586, 471, 486, 512, 6063 Fournitures d'entretien et de petit équipement, 6068, 6211 Personnel intérimaire, 616 Primes d'assurances, 6251 Voyages et déplacements, 6256 Missions, 627 Services bancaires.

## Les pièces

**Pièce 1 — Facture d'achat de produits d'entretien**

```
HYGIÈNE PRO MÉDITERRANÉE SAS — SIREN 438 920 615 — TVA FR 49 438920615
FACTURE N° HPM-26-10877 du 27/10/2026
Client : GSF Riviera SAS — SIREN 999 100 206 — Établissement de Nice
Nature de l'opération : livraison de biens
Produits détergents et désinfectants (bons de livraison BL-5512 et BL-5530)
Total HT ........ 2 340,00 €   TVA 20 % ........ 468,00 €   Total TTC ........ 2 808,00 €
Échéance : 30/11/2026 — Pénalités de retard : 3 fois le taux d'intérêt légal — indemnité forfaitaire 40 €
```

**Pièce 2 — Facture d'un petit matériel**

```
OUTILLAGE PRO AZUR SARL — SIREN 520 731 448
FACTURE N° OPA-5521 du 21/10/2026 — Client : GSF Riviera SAS, établissement de Nice
1 aspirateur dorsal professionnel ........ 420,00 € HT
TVA 20 % ................................. 84,00 €
Total TTC ................................ 504,00 €   — Paiement à 30 jours
```

**Pièce 3 — Note de frais de Karim B., chef d'équipe (déplacement chantier Menton, 29/10/2026)**

| Dépense | TTC | dont TVA | Justificatif |
|---|---|---|---|
| Péage autoroute | 18,00 | 3,00 | ticket |
| Repas du midi (seul) | 27,50 | 2,50 | ticket de restaurant |
| Parking | 12,00 | 2,00 | ticket |
| **Total à rembourser** | **57,50** | **7,50** | Validée par le chef d'établissement le 30/10 |

**Pièce 4 — Rapprochement bancaire : relevé et grand livre au 31/10/2026**

Relevé bancaire (opérations non encore pointées) :

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 28/10 | VIR SYNDIC COPRO LE CAP BLEU F-2026-09-0301 | | 3 840,00 |
| 29/10 | CB BRICO RIVIERA NICE 27/10 | 186,00 | |
| 30/10 | FRAIS TENUE DE COMPTE OCTOBRE | 32,00 | |
| | **Solde créditeur au 31/10/2026** | | **53 487,30** |

Grand livre 512 (opérations non pointées) : chèque n° 0001245 du 29/10/2026 à la Serrurerie Niçoise (fictive), **1 250,00 €**. **Solde débiteur au 31/10/2026 : 48 615,30 €.**

Informations : la facture F-2026-09-0301 (Copropriété Le Cap Bleu, 3 200,00 € HT + 640,00 € TVA) est en compte 411CAP. Personne au siège ne sait à quoi correspond la dépense « Brico Riviera » ; aucun ticket n'a été transmis. Les frais de tenue de compte ne sont pas soumis à TVA.

**Pièce 5 — Éléments pour la clôture d'octobre**
- Intérim : relevé d'heures d'octobre validé par l'établissement pour Intérim Riviera (401IRV) : **3 150,00 € HT** (TVA 20 %) ; la facture arrivera vers le 10/11.
- Assurance : prime annuelle multirisque de **3 600,00 €** (pas de TVA) payée le 01/10/2026 pour la période du **01/10/2026 au 30/09/2027**, enregistrée **en totalité** en 616 en octobre.

**Pièce 6 — Question du chef d'établissement**

> « Pour Noël, je voudrais offrir à notre principal client un coffret de vins à **85,00 € TTC**. On pourra récupérer la TVA ? »

## Travail à faire

1. **Saisie (pièces 1 à 3)** : passez les trois écritures. Pour la pièce 2, justifiez le choix charge / immobilisation.
2. **Rapprochement (pièce 4)** : pointez, passez les écritures nécessaires au 31/10/2026 (sans oublier la TVA de l'encaissement Cap Bleu), puis présentez un état de rapprochement qui s'équilibre.
3. **Clôture (pièce 5)** : passez les deux écritures de fin de mois.
4. **TVA (pièce 6)** : répondez au chef d'établissement en deux ou trois phrases. On retient un seuil de **73 € TTC** par bénéficiaire et par an pour les cadeaux de faible valeur (*valeur à vérifier chaque année*).
5. **Mail** : rédigez le mail au chef d'établissement pour obtenir le justificatif de la dépense Brico Riviera (ton cordial, demande précise, délai).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E15-15_corrige.md)
