# E13-09 — SCI Horizon Pro : franchise de loyer d'un nouveau locataire et locataire en liquidation
**Client :** C07 — SCI Horizon Pro | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** SCI à l'IS, option TVA sur les loyers, franchise de loyer (étalement sur la durée ferme), liquidation judiciaire d'un locataire, déclaration de créance, compensation avec le dépôt de garantie, TVA sur encaissements, dépréciation HT

**Corner case :** oui — le dépôt de garantie compense une partie de la créance, ce qui rend la TVA exigible sur cette partie

## La mise en situation

Mail de Jean Delmas (Delta Invest, associée à 40 % de la SCI, qui en assure la gérance administrative), le 9 octobre 2026 :

> « Deux sujets pour la SCI. Le nouveau locataire du lot 2, Orféo Conseil, ne paie rien pendant 6 mois, c'est ce qu'on a négocié pour le faire venir : donc pas de loyer en 2026 avant octobre, c'est bien ça ? Et le locataire du lot 3, Studio Archi Plus, a été mis en liquidation ; il nous doit 4 mois, mais on a son dépôt de garantie, donc on est tranquilles, non ? »

Hélène Ferrand : « Préparez les écritures au 31/12/2026 en supposant qu'il n'y aura pas d'autre événement d'ici là, et vérifiez la TVA. »

Rappels : SCI à l'IS, **option pour la TVA sur les loyers** (CGI art. 260-2°), loyers facturés mensuellement d'avance le 1er du mois. La SCI **n'a pas opté pour les débits** : la TVA sur les loyers est exigible à l'**encaissement** (les avis d'échéance sont comptabilisés D 411 / C 706 / C 44574 « TVA collectée en attente d'encaissement » ; le 44574 est viré en 44571 à l'encaissement).

## Les pièces

**Pièce 1 — Bail commercial du lot 2 (extraits)**
```
BAIL COMMERCIAL — Entre SCI HORIZON PRO (SIREN 798 333 120), bailleur,
et ORFÉO CONSEIL SAS (SIREN 921 448 305), preneur
Locaux : lot 2, 2e étage, 120 rue Garibaldi, 69006 Lyon — usage exclusif de bureaux
Durée : 9 années entières et consécutives à compter du 01/04/2026.
Art. 4 — Par dérogation à l'article L. 145-4 du Code de commerce, s'agissant de locaux à usage
exclusif de bureaux, le preneur renonce à la faculté de donner congé à l'expiration de la
première période triennale : le bail est conclu pour une durée ferme de 6 ans.
Art. 5 — Loyer annuel hors taxes et hors charges : 60 000,00 € HT, payable mensuellement et
d'avance (5 000,00 € HT par mois), TVA en sus au taux en vigueur.
Art. 6 — Mesure d'accompagnement : franchise de loyer de 6 mois, du 01/04/2026 au 30/09/2026,
consentie sans contrepartie de travaux par le preneur. Premier loyer exigible le 01/10/2026.
```

**Pièce 2 — Grand livre 411 Orféo Conseil (au 09/10/2026)**
```
01/10/2026  Avis d'échéance octobre 2026   D 6 000,00   (706 : 5 000,00 ; 44574 : 1 000,00)
05/10/2026  Virement Orféo Conseil          C 6 000,00
```
> Les avis d'échéance de novembre et décembre seront émis aux mêmes conditions.

**Pièce 3 — Jugement concernant le locataire du lot 3**
```
BODACC — Publication du 25/09/2026
Tribunal des activités économiques de Lyon — Jugement du 15/09/2026
STUDIO ARCHI PLUS SARL (RCS Lyon 833 610 457) — Liquidation judiciaire simplifiée
Liquidateur : Me Paul Rivière, 6 rue de la Bourse, 69002 Lyon
Les créances sont à déclarer auprès du liquidateur dans les deux mois de la publication.
```
> Le liquidateur a renoncé à la poursuite du bail ; les clés ont été restituées le 30/09/2026 ; état des lieux de sortie conforme (aucune dégradation). Il a indiqué qu'aucun dividende n'est à attendre pour les créanciers chirographaires.

**Pièce 4 — Compte 411 Studio Archi Plus et dépôt de garantie**

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 01/06/2026 | Avis d'échéance juin (3 000,00 HT + 600,00 TVA) | 3 600,00 | |
| 01/07/2026 | Avis d'échéance juillet | 3 600,00 | |
| 01/08/2026 | Avis d'échéance août | 3 600,00 | |
| 01/09/2026 | Avis d'échéance septembre | 3 600,00 | |
| | **Solde débiteur** | **14 400,00** | |

Compte 165 « Dépôts et cautionnements reçus » — Studio Archi Plus : **9 000,00 €** créditeur (3 mois de loyer HT, versé à l'entrée en 2021).

## Travail à faire

1. Répondez à la première question de Jean : quel est le produit de loyer du lot 2 à comptabiliser en 2026 ? Justifiez la méthode et calculez. Quelle est la conséquence en TVA ? Signalez le point fiscal à documenter.
2. Que se serait-il passé si la franchise avait été la contrepartie de travaux d'aménagement réalisés par le preneur ?
3. Studio Archi Plus : quelles démarches, dans quel délai ? La compensation avec le dépôt de garantie est-elle possible ?
4. Calculez la perte probable et la dépréciation ; analysez la TVA (part compensée / part impayée).
5. Passez les écritures au 31/12/2026.
6. Répondez à Jean (« on est tranquilles, non ? »).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E13-09_corrige.md)
