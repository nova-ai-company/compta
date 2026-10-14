# Corrigé E01-10 — Rédiger une facture d'acompte (et la facture finale) dans les règles

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-10](../exercices/E01-10_facture-acompte-studio-pixel.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Anomalies du modèle actuel (question 1)

| Manque / erreur | Règle |
|---|---|
| Numéro « 41 » sans série ni continuité visible avec SP-2026-0040 | Numérotation unique, chronologique et continue → **SP-2026-0041** |
| Pas de **date** d'émission | Mention obligatoire |
| Vendeur : ni forme juridique, ni capital, ni **SIREN**, ni RCS, ni **n° TVA intracom**, adresse incomplète (code postal) | CGI annexe II art. 242 nonies A ; C. com. R. 123-237 |
| Client : dénomination incomplète (« Cuisine Facile »), pas d'adresse, pas de **SIREN** | Identification du client ; SIREN client = nouvelle mention |
| Désignation vague (« Acompte vidéos ») ; pas de référence au contrat | Désignation précise de la prestation |
| Pas de **taux** de TVA, pas de total HT explicite | Taux et montant de TVA par taux, total HT |
| Pas de **nature de l'opération** (prestation de services) | Nouvelle mention |
| Pas de date d'échéance, pas de pénalités de retard, pas d'**indemnité forfaitaire de 40 €**, pas de mention sur l'escompte | C. com. L. 441-9 et D. 441-5 |
| Pas d'indication que la TVA est acquittée sur les encaissements | Utile ; la mention obligatoire est l'**option pour les débits** quand elle existe (ici : pas d'option, donc pas de mention obligatoire, mais la précision évite les erreurs du client) |

### Taux de TVA
Studio Pixel est une **société** qui réalise une prestation de production audiovisuelle incluant la cession de droits d'exploitation : l'ensemble constitue une **prestation de services unique** au **taux normal de 20 %** (les taux réduits applicables à certaines cessions de droits d'auteur visent en principe les cessions consenties par les auteurs eux-mêmes — à vérifier si un associé facturait personnellement des droits).

### Exigibilité (question 5)
Prestation de services, pas d'option pour les débits ⇒ **TVA exigible à l'encaissement** (CGI art. 269-2-c).
- Acompte encaissé le 22/09/2026 → TVA de **768,00 €** exigible en **septembre 2026** (CA3 de septembre, déposée en octobre).
- Solde : TVA de **1 152,00 €** exigible à l'encaissement du solde (prévu début novembre 2026 → CA3 de novembre). Tant qu'il n'est pas encaissé, la TVA reste en 44574.

La facture d'acompte est **obligatoire** dès lors que l'acompte est versé par un professionnel (CGI art. 289-I-1-c). Le contrat prévoyant un paiement à réception, on l'émet avant l'encaissement.

## 2. Calculs (détaillés, chaque montant justifié)

| | HT | TVA 20 % | TTC |
|---|---|---|---|
| Prix total du contrat | 9 600,00 € | 1 920,00 € | 11 520,00 € |
| Acompte 40 % | 9 600,00 × 40 % = **3 840,00 €** | 3 840,00 × 20 % = **768,00 €** | **4 608,00 €** |
| Solde | 9 600,00 – 3 840,00 = **5 760,00 €** | 5 760,00 × 20 % = **1 152,00 €** | **6 912,00 €** |

Contrôle : 4 608,00 + 6 912,00 = 11 520,00 € ✓.

## 3. Écritures comptables

### Modèle de facture d'acompte (question 2)

```
STUDIO PIXEL SAS — Studio de création graphique et vidéo
21 rue Mercière, 69002 Lyon
SAS au capital de 10 000 € — RCS Lyon 952 777 888 — SIREN 952 777 888
N° TVA intracommunautaire : FR47 952777888

FACTURE D'ACOMPTE N° SP-2026-0041                     Date d'émission : 15/09/2026

Client : CUISINE FACILE MÉDIA SAS
         14 rue de Brest, 69002 Lyon
         SIREN 887 412 305 — TVA FR50 887412305
Nature de l'opération : prestation de services
Référence : contrat de production audiovisuelle du 14/09/2026

Désignation                                                         Montant HT
Acompte de 40 % sur la réalisation de 6 vidéos de recettes
(tournage, montage, étalonnage, habillage) et cession des droits
d'exploitation YouTube / réseaux sociaux pour 5 ans
— prix forfaitaire total du contrat : 9 600,00 € HT                  3 840,00 €

                                               Total HT              3 840,00 €
                                               TVA 20 %                768,00 €
                                               Total TTC             4 608,00 €

Date d'échéance : à réception (15/09/2026)
Pas d'escompte pour paiement anticipé.
Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 € (art. D. 441-5 C. com.).
TVA acquittée sur les encaissements.
Règlement par virement : IBAN FR76 XXXX XXXX XXXX XXXX XXXX XXX — BIC XXXXXXXX
```

### Modèle de facture de solde (question 3)

```
STUDIO PIXEL SAS — [en-tête identique]

FACTURE N° SP-2026-0047                               Date d'émission : 06/10/2026
Client : CUISINE FACILE MÉDIA SAS — [identification identique, SIREN 887 412 305]
Nature de l'opération : prestation de services
Référence : contrat du 14/09/2026 — prestation achevée le 05/10/2026
(livraison des 6 vidéos par lien de téléchargement)

Désignation                                                         Montant HT
Réalisation de 6 vidéos de recettes et cession des droits
d'exploitation (5 ans) — prix forfaitaire                            9 600,00 €
                                               Total HT              9 600,00 €
                                               TVA 20 %              1 920,00 €
                                               Total TTC            11 520,00 €
À déduire : facture d'acompte n° SP-2026-0041 du 15/09/2026
            HT 3 840,00 € — TVA 768,00 € — TTC                     - 4 608,00 €
                                               NET À PAYER           6 912,00 €
                                   dont HT 5 760,00 € — TVA 20 % 1 152,00 €

Date d'échéance : 05/11/2026 (30 jours)
Pas d'escompte pour paiement anticipé. Pénalités de retard : 3 fois le taux d'intérêt légal.
Indemnité forfaitaire pour frais de recouvrement : 40 €. TVA acquittée sur les encaissements.
```
(Numéro SP-2026-0047 : hypothèse de cinq factures émises entre le 15/09 et le 06/10 — en pratique, le numéro suivant dans la séquence.)

### Écritures (question 4)

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/09/2026 | VT | 411CUIS | Client Cuisine Facile Média | F acompte SP-2026-0041 Cuisine Facile 40 % | 4 608,00 | |
| 15/09/2026 | VT | 4191 | Clients – avances et acomptes reçus sur commandes | F acompte SP-2026-0041 Cuisine Facile 40 % | | 3 840,00 |
| 15/09/2026 | VT | 44574 | TVA collectée en attente d'encaissement | F acompte SP-2026-0041 Cuisine Facile 40 % | | 768,00 |
| 22/09/2026 | BQ | 512 | Banque | Vir. Cuisine Facile acompte SP-2026-0041 | 4 608,00 | |
| 22/09/2026 | BQ | 411CUIS | Client Cuisine Facile Média | Vir. Cuisine Facile acompte SP-2026-0041 | | 4 608,00 |
| 22/09/2026 | OD | 44574 | TVA collectée en attente d'encaissement | TVA exigible encaissement acompte SP-2026-0041 | 768,00 | |
| 22/09/2026 | OD | 44571 | TVA collectée | TVA exigible encaissement acompte SP-2026-0041 | | 768,00 |
| 06/10/2026 | VT | 411CUIS | Client Cuisine Facile Média | F SP-2026-0047 Cuisine Facile solde 6 vidéos | 6 912,00 | |
| 06/10/2026 | VT | 4191 | Clients – avances et acomptes reçus sur commandes | F SP-2026-0047 imputation acompte SP-2026-0041 | 3 840,00 | |
| 06/10/2026 | VT | 706 | Prestations de services | F SP-2026-0047 Cuisine Facile 6 vidéos + droits | | 9 600,00 |
| 06/10/2026 | VT | 44574 | TVA collectée en attente d'encaissement | F SP-2026-0047 TVA sur solde | | 1 152,00 |
| | | | | **Totaux** | **20 736,00** | **20 736,00** |

Après ces écritures : 4191 soldé ; 411CUIS = 6 912,00 € (solde à encaisser) ; 44574 = 1 152,00 € (TVA qui deviendra exigible à l'encaissement) ; 706 = 9 600,00 € (le chiffre d'affaires est constaté à l'achèvement de la prestation, le 05/10/2026, et non à la facture d'acompte).

## 4. Points d'attention / pièges

- **L'acompte n'est pas du chiffre d'affaires** : il est crédité en **4191** jusqu'à la réalisation de la prestation. Si la prestation n'était pas achevée à la clôture du 31/12/2026, le 4191 resterait au passif.
- **La facture de solde reprend le prix total** puis **déduit** l'acompte (HT et TVA) : ne pas facturer seulement « 60 % » sans référence à l'acompte, sinon le client ne peut pas rapprocher ses pièces et la piste d'audit est rompue.
- **Ne pas re-collecter la TVA de l'acompte** sur la facture de solde : 768,00 € ont déjà été collectés.
- **Numérotation** : les factures d'acompte et les factures définitives suivent la même séquence (ou des séries distinctes, chacune continue).
- **Exigibilité ≠ facturation** : en TVA sur les encaissements, c'est la date du paiement qui compte. Si Studio Pixel optait pour les débits, la mention « option pour le paiement de la TVA d'après les débits » deviendrait obligatoire sur ses factures.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse à Sarah sur la plateforme (question 6) :**

> Bonjour Sarah,
>
> Ci-joint vos deux modèles (facture d'acompte et facture de solde), à paramétrer dans votre logiciel. Quelques règles : un numéro qui suit toujours le précédent (SP-2026-0041, 0042…), jamais de facture supprimée (on annule par un avoir), et toujours le SIREN de votre client.
>
> Concernant la facturation électronique, votre question n'est pas bête du tout, elle est même urgente :
> - **depuis le 1er septembre 2026, toutes les entreprises doivent être en mesure de recevoir des factures électroniques.** Studio Pixel doit donc choisir dès maintenant une **plateforme agréée (PA)** pour recevoir ses factures fournisseurs (vos gros fournisseurs — opérateur télécom, loueur de matériel, éditeurs de logiciels — vous factureront par ce canal) ;
> - **pour émettre vos factures**, Studio Pixel étant une petite entreprise, l'obligation commencera le **1er septembre 2027** ; d'ici là, vos factures PDF restent valables. Autant choisir une PA qui fera aussi l'émission, et commencer à l'utiliser avant l'échéance.
>
> Nous vous proposons un rendez-vous de 30 minutes pour choisir la plateforme (le cabinet travaille avec une solution reliée à notre outil de production).

**Contrôles** : vérifier à la clôture du 31/12/2026 (premier exercice de 16 mois) que tous les acomptes reçus correspondent à des prestations achevées ou figurent en 4191 ; vérifier sur les CA3 que la TVA a bien été déclarée au mois d'encaissement ; noter au dossier permanent : « TVA sur encaissements, pas d'option débits ; PA de réception à mettre en place — relance le … ».

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 289-I : obligation de facturation, y compris pour les acomptes.
- CGI, annexe II, art. 242 nonies A : mentions obligatoires des factures.
- CGI art. 269-2-c : exigibilité de la TVA sur les prestations de services (encaissement, sauf option pour les débits).
- CGI art. 289 bis : facturation électronique — réception obligatoire au 01/09/2026 pour toutes les entreprises ; émission au 01/09/2027 pour les PME et micro-entreprises.
- Code de commerce art. L. 441-9, L. 441-10 et D. 441-5 : mentions commerciales, pénalités, indemnité de 40 €.
- Code de commerce art. R. 123-237 : mentions d'identification de la société sur ses documents.
- PCG : compte 4191 « Clients – Avances et acomptes reçus sur commandes ».
