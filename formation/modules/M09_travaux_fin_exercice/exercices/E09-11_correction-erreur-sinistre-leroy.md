# E09-11 — Transports Leroy : erreurs de 2025 découvertes en 2026 et camion détruit
**Client :** C11 — Transports Leroy SAS | **Difficulté :** ★★★ | **Durée estimée :** 1 h 15 | **Thèmes :** correction d'erreurs (vs changement de méthode et changement d'estimation), traitement fiscal sur l'exercice d'origine, réclamation, sinistre d'une immobilisation, indemnité d'assurance à recevoir, sortie d'actif, TVA

**Corner case :** oui — Bruno veut passer les erreurs « en report à nouveau » ; l'indemnité d'assurance n'est pas encore encaissée à la clôture.

## La mise en situation

Nous sommes le 9 octobre 2026. En reprenant le dossier (voir E09-01), vous avez découvert deux erreurs dans les comptes 2025, **approuvés en juin 2026**. Par ailleurs, un tracteur a été détruit dans un accident fin septembre.

Bruno Leroy, président, vous répond au téléphone :

> « Des erreurs de 2025 ? Je ne veux pas que ça plombe 2026, les banques regardent mes comptes. Mettez ça en report à nouveau, c'est fait pour ça, non ? Et pour le camion, l'assureur a dit oui mais on n'a rien touché : on ne peut rien mettre tant que ce n'est pas payé, si ? »

Données : exercice civil ; résultat 2025 approuvé : **186 400 €** (avant IS) ; Transports Leroy est imposée au taux de **25 %** sur la totalité de son bénéfice marginal (les 42 500 premiers euros ne sont pas concernés par les corrections). IS 2025 payé (solde) le 15/05/2026.

## Les pièces

**Pièce 1 — Relance fournisseur reçue le 14/09/2026**
```
CARROSSERIE INDUSTRIELLE DU RHÔNE SAS — SIREN 618 330 204 — FR39618330204
RELANCE — Facture n° F-2025-1188 du 28/11/2025 — échue le 31/12/2025
Réparation carrosserie semi-remorque SR-14 suite à accrochage — travaux réalisés du
17/11/2025 au 26/11/2025 — HT 11 800,00 € — TVA 20 % 2 360,00 € — TTC 14 160,00 €
Nous constatons que cette facture, transmise par courriel le 28/11/2025, reste impayée.
Pénalités de retard : 3 fois le taux d'intérêt légal ; indemnité forfaitaire : 40 €.
```
*Recherche : la facture n'a jamais été enregistrée (courriel classé en indésirable). Elle est réglée le 30/09/2026 (duplicata reçu).*

**Pièce 2 — Justification du compte 4181 au 30/09/2026**

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 31/12/2025 | FAE Fromageries de l'Ain – transport du 22/12/2025 | 11 340,00 | |
| | **Solde** | **11 340,00** | |

*La facture n° 2025-1290 du 29/12/2025 (Fromageries de l'Ain, 9 450,00 € HT, TVA 1 890,00 €) a été enregistrée au journal des ventes de décembre 2025, puis encaissée le 28/01/2026. La FAE de Julien porte sur la même prestation. Aucune extourne n'a été passée.*

**Pièce 3 — Constat et rapport d'expertise**
```
Accident du 28/09/2026 sur l'A43 — Tracteur Renault T 480 immat. FR-221-PL (sans tiers responsable)
Rapport d'expertise du 22/10/2026 : véhicule économiquement irréparable (VEI).
Valeur de remplacement à dire d'expert (VRADE) : 58 000,00 €.
```
*Fiche immobilisation : acquis et mis en service le 01/04/2022, coût 118 000,00 € HT, amortissement linéaire sur 5 ans (prorata temporis, année de 360 jours). Amortissement 2026 non encore comptabilisé.*

**Pièce 4 — Lettre de l'assureur**
```
MUTUELLE DES TRANSPORTEURS — Lyon, le 20/11/2026
Sinistre n° SIN-26-44871 — Tracteur FR-221-PL
Nous vous confirmons la prise en charge du sinistre au titre de la garantie dommages tous
accidents : indemnité = VRADE 58 000,00 € – franchise contractuelle 1 500,00 €,
soit 56 500,00 €, payable sous 60 jours après remise de la carte grise barrée et de la
cession de l'épave à notre partenaire.
```
*Carte grise et épave remises le 10/12/2026. Paiement reçu le 12/01/2027.*

**Pièce 5 — Facture de remorquage**
```
DÉPANNAGE ALPES RHÔNE — Facture n° DR-2609-077 du 30/09/2026
Remorquage poids lourd A43 → Vénissieux — HT 1 200,00 € — TVA 240,00 € — TTC 1 440,00 €
(non pris en charge par l'assureur)
```

## Travail à faire
1. Qualifiez les deux anomalies 2025 : correction d'erreur, changement de méthode ou changement d'estimation ? Répondez à Bruno sur le report à nouveau.
2. Passez les écritures de correction dans les comptes 2026 et précisez l'information en annexe.
3. Indiquez le traitement fiscal : sur quel exercice ces charges et produits sont-ils imposables ? Quelle démarche faire, avant quelle date ? Chiffrez.
4. Pour comparaison : l'omission de la provision prud'homale de 8 000 € au 31/12/2025 (voir E09-01) peut-elle être corrigée fiscalement de la même manière ?
5. Traitez le sinistre du tracteur dans les comptes 2026 : amortissement, sortie, indemnité, remorquage, TVA. Répondez à Bruno sur l'indemnité non encaissée.
6. Calculez le résultat de cession (plus ou moins-value) et son traitement fiscal.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E09-11_corrige.md)
