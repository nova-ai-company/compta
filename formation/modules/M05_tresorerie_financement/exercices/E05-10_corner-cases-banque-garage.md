# E05-10 — Trois incidents bancaires à la clôture du Garage Martin
**Client :** C03 — Garage Martin EURL | **Difficulté :** ★★★ | **Durée estimée :** 75 min | **Thèmes :** virement sans référence, acompte sur vente de VO, chèque impayé, créance douteuse, fraude au faux fournisseur (changement de RIB), dépréciation

**Corner case :** oui — trois cas atypiques sur le relevé de septembre, à traiter pour la clôture du 30/09/2026.

## La mise en situation

Clôture du 30/09/2026 du Garage Martin, qui sert de base au cas de synthèse. En faisant le rapprochement de septembre, vous isolez trois opérations. Thierry Martin vous appelle, très énervé :

> « Je viens d'avoir AutoPièces au téléphone, ils me relancent pour 18 000 € de factures que j'ai PAYÉES le 5 septembre ! Ma secrétaire a reçu un mail qui disait qu'ils changeaient de banque. Et le chèque du client de la 208, il est revenu impayé, alors que la voiture est partie. Et il y a aussi un virement de 4 380 € d'un M. Lefebvre, je ne sais pas à quoi il correspond. Dites-moi ce que je fais ! »

Hélène Ferrand : « Pour la fraude, l'urgence c'est la banque et la plainte, aujourd'hui même. Ensuite on traite les trois sujets pour la clôture. »

## Les pièces

### Pièce 1 — Extrait du relevé bancaire de septembre 2026

```
CRÉDIT MUTUEL LYON GERLAND — Compte professionnel EURL GARAGE MARTIN — n° 00020 451 877 01
```

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 05/09 | VIR SEPA EMIS AUTOPIECES DISTRIBUTION FA-88412 FA-88467 — IBAN LT62 3250 0412 8877 1023 | 18 420,60 | |
| 16/09 | REMISE CHEQUES BORD. 0916 (1 chèque) | | 9 800,00 |
| 22/09 | VIR SEPA RECU M OU MME LEFEBVRE JEAN | | 4 380,00 |
| 25/09 | CHEQUE IMPAYE N° 2245871 — MOTIF : DEFAUT DE PROVISION | 9 800,00 | |
| 25/09 | FRAIS REJET CHEQUE | 25,00 | |

Le virement du 22/09 est en 471. Le chèque impayé et les frais ne sont pas encore saisis. Le virement du 05/09 a été saisi et **lettré** avec les factures FA-88412 (11 240,40 € TTC) et FA-88467 (7 180,20 € TTC) au compte 401 AutoPièces Distribution, qui est donc soldé.

### Pièce 2 — E-mail reçu par la secrétaire le 02/09/2026

```
De : Service Comptabilité AutoPièces <comptabilite@autopieces-distrib.com>
À : contact@garage-martin-lyon.fr
Objet : URGENT — Changement de coordonnées bancaires
Bonjour,
Suite à un changement d'établissement bancaire lié à notre audit annuel, merci de bien vouloir
effectuer vos prochains règlements sur notre nouveau compte (RIB en pièce jointe).
IBAN : LT62 3250 0412 8877 1023 — BIC : REVOLT21
Nous vous remercions de procéder au règlement des factures FA-88412 et FA-88467 avant le 05/09
afin d'éviter la suspension de vos livraisons.
Cordialement, Sandrine Morel — Service Comptabilité
AUTOPIÈCES DISTRIBUTION SAS — 14 rue de l'Industrie 69200 Vénissieux
```

Les factures habituelles d'AutoPièces mentionnent l'adresse `compta@autopieces-distribution.fr` et un IBAN français FR76 1027 8073 ….

### Pièce 3 — Suites données (informations au 08/10/2026)
- 29/09/2026 : demande de rappel de fonds (recall) adressée au Crédit Mutuel ; réponse de la banque du 06/10 : « fonds non récupérables, le compte bénéficiaire a été vidé le 05/09 ».
- 30/09/2026 : plainte déposée au commissariat de Lyon 7e (récépissé joint).
- Le Garage n'a pas d'assurance « fraude / cyber ». AutoPièces confirme n'avoir jamais changé de banque et maintient sa créance.

### Pièce 4 — Vente du véhicule Peugeot 208 et chèque impayé
```
BON DE COMMANDE VO n° VO-26-109 du 12/09/2026 — Client : M. Kévin Petitjean, 18 rue Marietton 69009 Lyon
Peugeot 208 1.2 PureTech 2020 — Prix TTC : 9 800,00 € — Régime : TVA sur la marge (art. 297 A CGI)
Livraison et remise des clés : 15/09/2026 — Règlement : chèque n° 2245871 (Banque Postale)
Clause de réserve de propriété : le véhicule reste la propriété du vendeur jusqu'au paiement intégral du prix.
```
- Prix d'achat du véhicule à un particulier (juin 2026) : 7 600,00 €.
- 30/09 : certificat de non-paiement demandé à la banque du tireur. 05/10 : M. Petitjean, joint par téléphone, dit être « en attente d'un prêt » ; il a viré **1 000,00 €** le 07/10/2026 et promet le solde « d'ici fin novembre », sans garantie.

### Pièce 5 — Compte client Lefebvre et carnet de commandes
- 411 M. Jean Lefebvre : facture atelier A-26-0912 du 08/09/2026 (révision + freins), **1 380,00 € TTC**, non réglée.
- Bon de commande VO-26-118 du 20/09/2026 : Renault Clio 2019, prix 8 900,00 € TTC (TVA sur la marge), client M. Jean Lefebvre, **acompte demandé 3 000,00 €**, livraison prévue le **06/10/2026**.

## Travail à faire
1. **Virement Lefebvre** : identifiez-le, passez l'écriture et justifiez le traitement de TVA.
2. **Chèque impayé** : passez les écritures du 25/09, puis analysez la créance à la clôture (classement, dépréciation chiffrée, TVA sur la marge). Quel parti peut-on tirer de la clause de réserve de propriété ?
3. **Fraude au faux fournisseur** : expliquez pourquoi le paiement n'a pas éteint la dette ; listez les indices qui auraient dû alerter ; passez les écritures au 30/09/2026 ; traitez la question de la déductibilité fiscale et de la TVA déduite sur les factures.
4. Indiquez l'impact total de ces trois sujets sur le résultat de l'exercice.
5. Rédigez les consignes à transmettre à Thierry Martin (urgence et prévention).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E05-10_corrige.md)
