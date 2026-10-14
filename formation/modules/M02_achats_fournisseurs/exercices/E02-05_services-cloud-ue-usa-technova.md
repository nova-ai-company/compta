# E02-05 — Services numériques achetés en Allemagne et aux États-Unis
**Client :** C08 — TechNova | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** autoliquidation des services (prestataire UE et hors UE), conversion des devises, perte de change, frais bancaires, choix du compte

**Corner case :** oui — facture en USD payée par carte à un cours différent, et question récurrente de la DAF « pourquoi déclarer une TVA qui n'est pas sur la facture ? »

## La mise en situation

TechNova tient sa comptabilité en interne ; le cabinet révise et prépare les déclarations de TVA. Émilie Roux, DAF à temps partagé, vous envoie le 7 octobre 2026 :

> « Bonjour, pour la CA3 de septembre, je vous mets les deux factures "tech" du mois : l'outil de monitoring allemand et l'hébergement NimbusCloud. Ni l'une ni l'autre n'a de TVA. Je les ai passées en 6228 sans TVA, ça vous va ? Pour NimbusCloud, j'ai pris le montant en euros débité sur la carte. »

Hélène Ferrand : « Ça ne va pas du tout. Reprenez les deux factures : comptes, autoliquidation, devise. Et expliquez à Émilie, elle doit pouvoir le faire seule le mois prochain. »

Rappels : SAS, réel normal, CA3 mensuelle, droits à déduction complets. TVA FR84 879654321. L'hébergement cloud est le cœur de la production du service SaaS vendu aux clients. Hypothèse de cours de change (BCE) : **30/09/2026 : 1 € = 1,1650 USD**. Paiement de NimbusCloud par carte bancaire le **03/10/2026** : la banque convertit au cours de **1,1580** et prélève une **commission de change de 1,5 %** sur le montant converti. Le fournisseur allemand est prélevé par SEPA le **05/10/2026**.

## Les pièces

**Pièce 1 — Facture allemande**
```
DATENWERK GmbH — Monitoring & Observability Software
Torstraße 140, 10119 Berlin, Deutschland
Handelsregister: Amtsgericht Charlottenburg HRB 198765 — USt-IdNr.: DE298765431

RECHNUNG / INVOICE Nr. DW-2026-09-1188              Datum / Date: 30.09.2026
Kunde / Customer: TechNova SAS, 30 quai Perrache, 69002 Lyon, France
                  USt-IdNr. / VAT: FR84879654321
Leistungszeitraum / Service period: 01.09.2026 – 30.09.2026

Beschreibung / Description                                    Betrag / Amount
Subscription "Observa Pro" – 25 hosts – September 2026            1.250,00 EUR
                                         Netto / Net              1.250,00 EUR
                                         USt / VAT 0 %                0,00 EUR
                                         Gesamt / Total           1.250,00 EUR
Steuerschuldnerschaft des Leistungsempfängers / Reverse charge –
VAT to be accounted for by the recipient (Art. 196 Directive 2006/112/EC)
Zahlung: SEPA-Lastschrift / Direct debit on 05.10.2026
```

**Pièce 2 — Facture américaine**
```
NIMBUSCLOUD INC.
1200 Fifth Avenue, Suite 900, Seattle, WA 98101, USA — EIN 91-1234567

INVOICE INV-NC-2026-09-77351                          Invoice date: Sep 30, 2026
Bill to: TechNova SAS — 30 quai Perrache, 69002 Lyon, France — VAT FR84879654321
Account ID: 4471-2290-1183 — Billing period: Sep 1 – Sep 30, 2026

Service                                           Usage                 Amount (USD)
Compute instances (production cluster)            21 600 hrs              11 880.00
Managed database (PostgreSQL, multi-AZ)           720 hrs                  4 320.00
Object storage                                    48 TB-month               1 680.00
Data transfer out                                  9.5 TB                    760.00
                                                         Subtotal         18 640.00
                                                         Tax                  0.00
                                                         TOTAL USD        18 640.00
Tax note: Customer to self-assess VAT where applicable (reverse charge).
Payment: charged to card ending 8812 on Oct 3, 2026.
```

**Pièce 3 — Relevé de la carte bancaire (débit différé, compte 512)**
```
03/10/2026  NIMBUSCLOUD INC SEATTLE  USD 18 640,00  cours 1,1580   16 096,72 EUR
03/10/2026  COMMISSION PAIEMENT DEVISE 1,5 %                           241,45 EUR
```

## Travail à faire

1. Expliquez pourquoi ces deux factures sont sans TVA et pourquoi TechNova doit néanmoins déclarer de la TVA. Quelle différence de traitement déclaratif entre la facture allemande et la facture américaine ?
2. Quand la TVA est-elle exigible pour chacune ? Sur quelle CA3 ?
3. Quel compte de charge retenez-vous (justifiez) ? Pourquoi le 6228 d'Émilie n'est-il pas adapté ?
4. Convertissez la facture américaine : à quel cours, pour la comptabilité et pour la TVA ?
5. Passez les écritures des deux factures et des deux règlements.
6. Si la facture NimbusCloud n'avait pas été payée au 31/12, que faudrait-il faire ?
7. Rédigez une fiche « mode d'emploi » de 6 lignes pour Émilie.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E02-05_corrige.md)
