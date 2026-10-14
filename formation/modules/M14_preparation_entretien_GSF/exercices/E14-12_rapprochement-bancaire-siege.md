# E14-12 — Rapprochement bancaire de fin de mois au siège : suspens, régularisations et chèque périmé
**Client :** Comptabilité du **siège** — société tête GSF (SIREN 775 675 291) — **montants fictifs** | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** état de rapprochement, suspens bancaires et comptables, frais bancaires, prélèvements, LCR, erreur de saisie, virement intra-groupe, encaissement non identifié, chèque émis non présenté depuis plus d'un an

**Corner case :** oui — un chèque émis il y a plus d'un an n'a jamais été encaissé : il ne doit plus figurer en suspens indéfiniment, mais la dette envers le fournisseur ne disparaît pas pour autant

> *Cadre de formation : la société tête du groupe GSF est réelle, mais **tous les montants, comptes bancaires, opérations et personnes sont fictifs** et ne reflètent en rien ses comptes.*

## La mise en situation

Jeudi 01/10/2026, J+1 de la clôture de septembre. Isabelle Marchetti, trésorière du siège (personnage fictif), vous confie le rapprochement du compte « Banque A » (compte 512100) :

> « J'ai besoin de l'état de rapprochement signé ce soir pour le reporting trésorerie. Tous les suspens doivent être expliqués, et ce qui doit être passé en compta doit l'être sur septembre. Le vieux chèque de 2025 qui traîne, je ne veux plus le voir. »

Comptes : 512100 Banque A ; 401 (fournisseurs, par tiers) ; 403 Fournisseurs – effets à payer ; 451GSFR Groupe – compte courant GSF Riviera (cash pooling) ; 471 Compte d'attente ; 627 Services bancaires et assimilés ; 44566 ; 411 (clients).

## Les pièces

**Pièce 1 — Relevé de la Banque A au 30/09/2026 (opérations du 24/09 au 30/09)**

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 24/09 | VIR SEPA MACHINES NETT SARL REF PAY-0924 | 2 845,60 | |
| 25/09 | PRLV SEPA OPERATEUR TELECOM FACT 09-2026 | 1 872,00 | |
| 28/09 | VIR GSF RIVIERA SAS REMONTEE CASH POOLING | | 45 000,00 |
| 29/09 | VIR SEPA REF 88412 REGLEMENT CLIENT | | 3 240,00 |
| 30/09 | LCR ECHUE N° 4471 FOURNISSEUR PAPIER ESSUYAGE (fictif) | 12 600,00 | |
| 30/09 | COMMISSIONS ET FRAIS T3 2026 DONT TVA 86,00 | 516,00 | |
| | **Solde créditeur au 30/09/2026** | | **1 284 562,18** |

**Pièce 2 — Extrait du grand livre 512100 (opérations non pointées au relevé)**

| Date | Pièce | Libellé | Débit | Crédit |
|---|---|---|---|---|
| 12/08/2025 | CHQ 0044102 | Imprimerie Azur Graphic (fictif) – F IAG-2025-311 | | 350,00 |
| 24/09/2026 | VIR | Machines Nett' – F MN-4390 | | 2 485,60 |
| 24/09/2026 | CHQ 0045781 | Fédération professionnelle (fictive) – cotisation | | 2 400,00 |
| 28/09/2026 | CHQ 0045783 | Location salle séminaire (fictif) | | 1 180,00 |
| 30/09/2026 | REM CHQ | Remise de chèques clients n° 2026-118 | 8 650,40 | |
| 30/09/2026 | VIR | Run fournisseurs du 30/09 (fichier SEPA 2026-09-30-01) | | 46 912,55 |
| | | **Solde débiteur au 30/09/2026** | **1 209 478,03** | |

**Pièce 3 — Informations complémentaires**
- Facture Machines Nett' MN-4390 : TTC **2 845,60 €** (le virement a été correctement exécuté ; la saisie comptable du 24/09 est erronée).
- La facture télécom de septembre (1 872,00 € TTC) est déjà enregistrée au compte fournisseur 401TEL.
- LCR n° 4471 : effet accepté, enregistré en 403 lors de l'acceptation (12 600,00 €) ; l'échéance n'a pas été comptabilisée.
- Commissions T3 : la banque a opté pour la TVA sur ces services ; facture de frais disponible sur l'espace client.
- Le virement « REF 88412 » ne mentionne ni nom ni facture ; aucune facture client ouverte de 3 240,00 €.
- Chèque 0044102 du 12/08/2025 : jamais présenté. La facture IAG-2025-311 n'a pas été payée par un autre moyen.

## Travail à faire

1. Pointez les deux documents et classez chaque suspens (en banque non en compta / en compta non en banque).
2. Passez au 30/09/2026 les écritures de régularisation nécessaires, y compris pour le chèque de 2025.
3. Établissez l'état de rapprochement au 30/09/2026 et vérifiez qu'il s'équilibre.
4. Que faites-vous du virement non identifié de 3 240,00 € (traitement immédiat et suivi) ?
5. Que dites-vous à Isabelle Marchetti à propos du vieux chèque, et quelle action concrète engagez-vous ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-12_corrige.md)
