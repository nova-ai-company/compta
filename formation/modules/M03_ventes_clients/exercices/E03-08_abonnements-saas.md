# E03-08 — Abonnements SaaS facturés d'avance
**Client :** C08 — TechNova SAS | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** abonnements annuels payés d'avance, produits constatés d'avance, frais de mise en service, mois offert, facturation anticipée, TVA sur encaissements des services, client UE en autoliquidation

**Corner case :** oui — abonnement de 13 mois pour le prix de 12 et facture émise en décembre pour une période entièrement en N+1

## La mise en situation

Émilie Roux, DAF à temps partagé de TechNova, prépare la clôture du 31/12/2026 en avance car une levée de fonds est prévue en février 2027. Elle vous écrit le 9 octobre :

> Bonjour, les investisseurs regardent notre ARR (revenu récurrent annuel). Yanis voudrait qu'on reconnaisse en CA les contrats annuels dès la signature, « puisque le client est engagé ». Pouvez-vous me confirmer le traitement et me préparer les écritures types sur les cinq contrats ci-dessous ? Les factures de novembre et décembre sont déjà programmées dans notre outil d'abonnement (Stripe Billing), je vous les mets aussi. Merci ! Émilie

TechNova n'a **pas** opté pour le paiement de la TVA d'après les débits.

## Les pièces

### Pièce 1 — Export Stripe Billing (factures 2026 et factures programmées)

| Facture | Date | Client | Période de service | Objet | HT | TVA | TTC | Paiement |
|---|---|---|---|---|---|---|---|---|
| TN-2026-0611 | 01/07/2026 | Bauplan Software GmbH, Berlin — USt-IdNr DE 298 114 556 (validé VIES) | 01/07/2026 – 30/06/2027 | Abonnement annuel « Pro » | 9 600,00 | 0,00 — « Autoliquidation » | 9 600,00 | 10/07/2026 |
| TN-2026-0802 | 01/10/2026 | SAS Logis Plan — SIREN 902 331 740 | 01/10/2026 – 30/09/2027 | Abonnement annuel « Business » | 14 400,00 | 2 880,00 | 17 280,00 | 05/10/2026 |
| (même facture) | | | octobre 2026 | Mise en service : paramétrage + 2 jours de formation des utilisateurs (réalisés les 6 et 7/10/2026) | 1 500,00 | 300,00 | 1 800,00 | 05/10/2026 |
| TN-2026-0890 *(programmée)* | 01/11/2026 | SAS Atelier Mobile — SIREN 918 004 225 | 01/11/2026 – 30/11/2027 (**13 mois** : offre « 1er mois offert ») | Abonnement « Pro » 13 mois | 12 000,00 | 2 400,00 | 14 400,00 | prélèvement SEPA prévu 10/11/2026 |
| TN-2026-0955 *(programmée)* | 15/12/2026 | SAS Frigo Logistique — SIREN 831 557 090 | 01/01/2027 – 31/12/2027 | Renouvellement annuel « Pro » | 6 000,00 | 1 200,00 | 7 200,00 | échéance 15/01/2027 |
| Mensuelles | le 1er de chaque mois | SARL Optima RH | mois civil | Abonnement mensuel | 390,00 | 78,00 | 468,00 | SEPA le 5 du mois |

### Pièce 2 — Extrait des CGV TechNova

```
Art. 5 – Les abonnements sont conclus pour la durée indiquée sur le bon de commande et facturés
d'avance. Ils ne sont pas remboursables, sauf manquement de TechNova à ses obligations de service (SLA).
Art. 6 – Les prestations de mise en service (paramétrage, formation) sont des prestations distinctes,
facturées à leur réalisation, et ne conditionnent pas l'accès à la plateforme.
```

## Travail à faire

1. Répondez à la question de Yanis (reconnaissance en CA à la signature) en quelques lignes argumentées, et précisez la différence entre l'indicateur ARR et le chiffre d'affaires comptable.
2. Pour chaque contrat, déterminez le CA de l'exercice 2026 et le produit constaté d'avance au 31/12/2026. Justifiez le traitement des frais de mise en service et du mois offert.
3. Indiquez, pour chaque facture, le mois au cours duquel la TVA est exigible et la ligne de la CA3 concernée pour la facture allemande.
4. Passez les écritures 2026 (factures, encaissements, régularisation de TVA sur encaissement, PCA au 31/12). Les abonnements mensuels Optima RH ne sont pas à détailler.
5. Que se passe-t-il au 01/01/2027 ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E03-08_corrige.md)
