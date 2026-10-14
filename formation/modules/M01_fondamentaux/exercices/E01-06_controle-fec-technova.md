# E01-06 — Contrôler un FEC avant de le remettre au vérificateur
**Client :** C08 — TechNova | **Difficulté :** ★★★ | **Durée estimée :** 50 min | **Thèmes :** FEC, format A. 47 A-1, intégrité des écritures, compte d'attente, produits constatés d'avance

**Corner case :** oui — FEC produit par l'ERP du client (et non par le logiciel du cabinet) à remettre lors d'un contrôle fiscal

## La mise en situation

TechNova a reçu un **avis de vérification de comptabilité** portant sur les exercices 2024 et 2025. Première intervention du vérificateur dans 15 jours : il demandera le FEC dès la première intervention. Émilie Roux, DAF à temps partagé, a extrait le FEC 2025 de l'ERP de TechNova (la tenue est faite en interne ; le cabinet assure la révision et la liasse) :

> « Bonjour, voici le FEC 2025, je l'ai généré hier. Vous pouvez y jeter un œil avant qu'on le donne ? Le fichier fait 48 000 lignes, je vous mets un extrait des écritures de décembre où j'ai eu des doutes. Merci ! Émilie »

Hélène Ferrand : « On ne remet **rien** au vérificateur sans l'avoir passé au contrôle. Analysez cet extrait comme si c'était le fichier complet : anomalies de format, anomalies d'intégrité, anomalies de fond. Et dites-moi ce qu'on risque. »

Exercice de TechNova : 01/01/2025 – 31/12/2025.

## Les pièces

**Pièce 1 — Extrait du fichier `879654321FEC20251231.txt`** (séparateur « | », en-tête puis 18 lignes)

```
JournalCode|JournalLib|EcritureNum|EcritureDate|CompteNum|CompteLib|CompAuxNum|CompAuxLib|PieceRef|PieceDate|EcritureLib|Debit|Credit|EcritureLet|DateLet|ValidDate|Montantdevise|Idevise
VE|Ventes|VE000122|20251215|411000|Clients|C0042|Batiplan SAS|FA25-1201|20251215|Batiplan abonnement annuel 2026|14400,00|0,00|AA|20260110|20251231||
VE|Ventes|VE000122|20251215|706100|Abonnements SaaS|||FA25-1201|20251215|Batiplan abonnement annuel 2026|0,00|12000,00|||20251231||
VE|Ventes|VE000122|20251215|445710|TVA collectée|||FA25-1201|20251215|Batiplan abonnement annuel 2026|0,00|2400,00|||20251231||
VE|Ventes|VE000123|20251218|411000|Clients|C0051|Optima Conseil|FA25-1202|20251218|Optima abonnement 12/2025|1200,00|0,00|||20251231||
VE|Ventes|VE000123|20251218|706100|Abonnements SaaS|||FA25-1202|20251218|Optima abonnement 12/2025|0,00|1000,00|||20251231||
VE|Ventes|VE000123|20251218|445710|TVA collectée|||FA25-1202|20251218|Optima abonnement 12/2025|0,00|180,00|||20251231||
VE|Ventes|VE000125|20251220|411000|Clients|C0012|Logistik Alpes|FA25-1204|20251220|Logistik Alpes abonnement 12/2025|2160,00|0,00|||20251231||
VE|Ventes|VE000125|20251220|706100|Abonnements SaaS|||FA25-1204|20251220|Logistik Alpes abonnement 12/2025|0,00|1800,00|||20251231||
VE|Ventes|VE000125|20251220|445710|TVA collectée|||FA25-1204|20251220|Logistik Alpes abonnement 12/2025|0,00|360,00|||20251231||
AC|Achats|AC000310|20251130|401000|Fournisseurs|||F-88213|20251128|Facture fournisseur|0,00|540,00|||20251231||
AC|Achats|AC000310|20251130|626000|Frais postaux et télécom|||F-88213|20251128|Facture fournisseur|450,00|0,00|||20251231||
AC|Achats|AC000310|20251130|445660|TVA déductible ABS|||F-88213|20251128|Facture fournisseur|90,00|0,00|||20251231||
AC|Achats|AC000311|20251210|604000|Achats prestations hébergement|||AV-NC-1177|20251210|NimbusCloud avoir SLA|-320,00|0,00|||20251201||
AC|Achats|AC000311|20251210|401000|Fournisseurs|F0007|NimbusCloud Inc|AV-NC-1177|20251210|NimbusCloud avoir SLA|0,00|-320,00|||20251201||
AC|Achats|AC000312|15-12-2025|604000|Achats prestations hébergement|||INV-NC-2025-12|20251201|NimbusCloud hébergement 12/2025|4291,85|0,00|||20251231|5000,00|
AC|Achats|AC000312|15-12-2025|401000|Fournisseurs|F0007|NimbusCloud Inc|INV-NC-2025-12|20251201|NimbusCloud hébergement 12/2025|0,00|4291,85|||20251231|5000,00|
BQ|Banque|BQ000845|20251231|512000|Banque BNP|||||Virement reçu|8500,00|0,00|||20260115||
BQ|Banque|BQ000845|20251231|471000|Compte d'attente|||||Virement reçu|0,00|8500,00|||20260115||
OD|Opérations diverses|OD000077|20260105|681120|Dotations amort. immo. corporelles|||AMORT25|20251231|Dotations 2025|18640,00|0,00|||20260105||
OD|Opérations diverses|OD000077|20260105|281830|Amort. matériel informatique|||AMORT25|20251231|Dotations 2025|0,00|18640,00|||20260105||
```

**Pièce 2 — Informations complémentaires obtenues d'Émilie Roux**
- La numérotation VE000124 correspond à une facture « annulée » par un commercial dans l'ERP avant validation (« elle avait une erreur, on l'a supprimée »).
- Le virement de 8 500,00 € du 31/12/2025 est le règlement par Logistik Alpes de sa facture FA25-1150 du 15/11/2025 (8 500,00 € TTC), toujours ouverte au 411.
- La facture Batiplan FA25-1201 couvre l'abonnement du **01/01/2026 au 31/12/2026**.
- Dans l'ERP, la facture FA25-1202 d'Optima affiche une TVA de 200,00 € à l'écran.

## Travail à faire

1. Rappelez les règles essentielles de forme du FEC (nom du fichier, colonnes, formats de date et de montant, numérotation, dates).
2. Dressez la liste de **toutes** les anomalies de l'extrait, classées en : (a) anomalies de format ; (b) anomalies d'intégrité / de piste d'audit ; (c) anomalies de fond comptable révélées par le fichier.
3. Pour chaque anomalie, indiquez le correctif (paramétrage de l'export, correction dans l'ERP, écriture comptable).
4. Présentez les écritures de fond qui **auraient dû** être passées au 31/12/2025, puis expliquez ce que l'on fait **aujourd'hui**, sachant que les comptes 2025 ont été approuvés en juin 2026 (peut-on « corriger » le FEC ? que passe-t-on en 2026 ?).
5. Quels sont les risques pour TechNova si le FEC est remis en l'état ? Que conseillez-vous à Émilie Roux ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E01-06_corrige.md)
