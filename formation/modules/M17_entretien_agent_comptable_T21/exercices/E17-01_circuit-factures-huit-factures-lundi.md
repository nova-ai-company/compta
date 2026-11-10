# E17-01 — Le circuit des factures : huit factures arrivées lundi matin
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★☆☆ | **Durée estimée :** 35 min | **Thèmes :** réception des factures, contrôle avant saisie, doublon, facture au nom d'un salarié, bon de commande, devis, facture d'un exercice clos, erreur de TVA, mentions obligatoires et facturation électronique, fraude au changement de RIB, saisie TTC, code analytique

**Corner case :** oui — une facture de 2025 arrive en novembre 2026 alors qu'une charge à payer avait été passée à la clôture ; et un « changement de RIB » arrive par mail le même jour qu'une facture parfaitement conforme

> *Cadre de formation : association, personnes, sociétés et documents fictifs.*

!!! abstract "En clair"
    Avant de saisir une facture, on vérifie **qu'elle est pour nous**, **qu'elle est juste**, **qu'elle correspond à une commande** et **qu'on ne l'a pas déjà**. Une facture douteuse n'est **pas** saisie « pour voir » : on la bloque et on appelle la bonne personne. Et on ne change **jamais** un RIB fournisseur sur la foi d'un simple mail.

## La mise en situation

Lundi 9 novembre 2026, 8 h 45. C'est votre deuxième semaine comme agent comptable chez Cap Horizons 21. Le week-end a été long : la bannette « Factures » déborde, la boîte mail aussi, et la plateforme agréée (**PA** : plateforme de facturation électronique choisie par l'association) a déposé plusieurs factures.

Nathalie Berthier, la directrice, passe la tête par la porte :

> « Bonjour ! Mme Roux faisait le tri des factures le lundi matin. Je vous laisse faire pareil : vous me dites lesquelles je peux valider, lesquelles posent problème et à qui il faut parler. Je signe les bons à payer jeudi. »

Rappels de la procédure interne (voir la fiche de l'association) :

- Les factures doivent être **au nom de l'association** : *Association Cap Horizons 21, 14 rue des Alpes, 26000 Valence — SIREN 999 210 021*.
- Toute dépense passe par un **bon de commande** signé par le chef de service (au-delà de 150 € TTC) ou par un **devis signé**.
- L'association **ne récupère pas la TVA** : les charges sont enregistrées **TTC**.
- Chaque charge reçoit un **code analytique** (01-SIEGE, 10-SESSAD, 20-SAVS, 30-EMPLOI, 40-HABITAT, 50-PAIRS, 90-ASSO).
- Les factures conformes sont **saisies dès réception** (journal AC, date du jour de saisie, avec la date de la facture en libellé) ; le **paiement** n'a lieu qu'après le **bon à payer** (BAP) de la directrice. Une facture non conforme n'est pas saisie : elle est notée dans le **registre des factures en attente**.
- Comptes utiles : 401xxx Fournisseurs (un compte par fournisseur) ; 4081 Fournisseurs – factures non parvenues ; 6063 Fournitures d'entretien et de petit équipement ; 6064 Fournitures administratives ; 6135 Locations mobilières ; 6152 Entretien et réparations sur biens immobiliers ; 6156 Maintenance ; 6228 Honoraires et prestations diverses *(subdivisions selon le plan de comptes de l'association)*.

## Les pièces

**Pièce 1 — Facture papier reçue par La Poste**
```
BUREAU PLUS VALENCE — SAS au capital de 40 000 € — SIREN 999 318 204 (fictif)
Facture n° BPV-26-2231 du 27/10/2026                         « DUPLICATA »
Client : Association Cap Horizons 21 – SAVS – 14 rue des Alpes, 26000 Valence
SIREN client : 999 210 021
Nature de l'opération : livraison de biens
Ramettes papier A4 (20), classeurs, enveloppes – BC n° SAVS-26-087
Total HT 186,50 € — TVA 20 % 37,30 € — Total TTC 223,80 €
Échéance : 30 jours date de facture. Pénalités de retard : 3 fois le taux d'intérêt
légal. Indemnité forfaitaire pour frais de recouvrement : 40 €.
```
*Extrait du grand livre, compte 401BPV au 09/11/2026 :*

| Date | Journal | Pièce | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|---|---|
| 28/10/2026 | AC | BPV-26-2231 | Bureau Plus – fournitures SAVS (reçue via PA) | | 223,80 | 223,80 C |

**Pièce 2 — Facture remise par Karim Belkacem (chef de service SESSAD), avec un post-it**
```
MÉDIATECH VALENCE — SIREN 999 507 336 (fictif)
Facture n° MT-884512 du 30/10/2026
Client : M. Thomas GIRARD, 8 allée des Tilleuls, 26500 Bourg-lès-Valence
Tablette tactile 10 pouces + coque renforcée              Total TTC 329,00 €
dont TVA 20 % 54,83 €          Payé par carte bancaire le 30/10/2026
```
> Post-it de Karim : « Tablette pour les ateliers du SESSAD. Thomas l'a payée avec sa carte, il faut le rembourser. Merci ! K. »

**Pièce 3 — Facture PDF reçue par mail**
```
FORMATIONS INCLUSIVES SUD — SARL — SIREN 999 604 552 (fictif)
Facture n° FIS-2026-118 du 03/11/2026
Client : Association Cap Horizons 21 – 14 rue des Alpes, 26000 Valence – SIREN 999 210 021
Nature : prestation de services
« Intervention de sensibilisation à la communication FALC (facile à lire et à comprendre)
auprès de l'équipe de l'emploi accompagné – 1 journée – 22/10/2026 »
Montant net : 1 200,00 € — Exonération de TVA : formation professionnelle continue
Échéance : 30 jours.
```
*Aucun bon de commande ni devis dans le classeur « Commandes ». Sophie Laurent (cheffe de service emploi accompagné) est en congés ; elle revient le jeudi 12/11 (le 11/11 est férié).*

**Pièce 4 — Facture reçue via la PA, et le devis retrouvé dans le classeur « Commandes »**
```
PEINTURE RHODANIENNE — EURL — SIREN 999 711 029 (fictif)
Facture n° PR-26-0457 du 04/11/2026
Client : Association Cap Horizons 21 – SESSAD – SIREN 999 210 021
Réf. devis D-26-112
Peinture de la salle d'attente du SESSAD (murs et plafond) ......... 2 000,00 € HT
Travaux supplémentaires : rebouchage de fissures .................... 600,00 € HT
Total HT 2 600,00 € — TVA 20 % 520,00 € — Total TTC 3 120,00 €
```
```
DEVIS D-26-112 du 15/09/2026 – Peinture de la salle d'attente du SESSAD
Total HT 2 000,00 € — TVA 20 % 400,00 € — Total TTC 2 400,00 €
« Bon pour accord » – signé K. Belkacem le 18/09/2026
```

**Pièce 5 — Facture reçue par La Poste, avec une lettre de relance**
```
ATELIERS DRÔME IMPRESSION — SIREN 999 452 117 (fictif)
Facture n° ADI-2025-0412 du 18/12/2025
Client : Association Cap Horizons 21 – Vie associative – SIREN 999 210 021
1 500 plaquettes « Changeons de regard » (journée mondiale de la trisomie 21)
Total HT 900,00 € — TVA 20 % 180,00 € — Total TTC 1 080,00 € — Payable à réception
« 2e relance : sauf erreur de notre part, cette facture reste impayée. »
```
*Extrait du compte 4081 au 09/11/2026 :*

| Date | Journal | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|---|
| 31/12/2025 | OD | FNP Ateliers Drôme Impression – plaquettes déc. 2025 (BL du 16/12/2025) | | 1 080,00 | 1 080,00 C |

*Le compte 401ADI n'a aucun mouvement. Les comptes 2025 ont été approuvés en juin 2026.*

**Pièce 6 — Facture reçue via la PA**
```
SIGN'ALPES — SAS — SIREN 999 803 640 (fictif)
Facture n° SA-26-0311 du 05/11/2026
Client : Association Cap Horizons 21 – SAVS – SIREN 999 210 021
5 panneaux de signalétique en FALC pour l'accueil du SAVS × 130,00 € HT
Total HT 650,00 € — TVA 20 % 150,00 € — Total TTC 800,00 €
Bon de commande SAVS-26-091 signé S. Laurent
```

**Pièce 7 — Facture PDF reçue par mail**
```
ALPES COPIE SERVICES — SARL — SIREN 999 615 090 (fictif)
Facture n° ACS-26-1093 du 31/10/2026
Client : Association Cap Horizons 21, 14 rue des Alpes, 26000 Valence
Contrat de maintenance n° CM-2024-017 – copieur du siège – 4e trimestre 2026
Total HT 375,00 € — TVA 20 % 75,00 € — Total TTC 450,00 €
Nature : prestation de services — Échéance : 30/11/2026
```
*Le contrat CM-2024-017, signé par la directrice, prévoit bien 375,00 € HT par trimestre. Le numéro SIREN du client n'apparaît nulle part sur la facture.*

**Pièce 8 — Facture reçue via la PA, puis un mail reçu à 7 h 52**
```
RHÔNE MOBILITÉ LOCATION — SAS — SIREN 999 902 418 (fictif)
Facture n° RML-2611-0207 du 01/11/2026
Client : Association Cap Horizons 21 – SAVS – SIREN 999 210 021
Location longue durée – Clio immatriculée GH-412-KT – loyer de novembre 2026
Total HT 450,00 € — TVA 20 % 90,00 € — Total TTC 540,00 €
Échéance : 10/11/2026 – Règlement par virement sur IBAN FR76 XXXX XXXX XXXX 4471
(IBAN identique au contrat de location du 01/03/2024)
```
```
De : Service comptabilité <compta@rhone-mobilite-location.co>
Objet : URGENT – changement de domiciliation bancaire
Bonjour, suite à un changement de banque, merci de régler dès aujourd'hui nos factures
d'octobre et de novembre sur notre nouveau compte : IBAN LT12 3250 0000 1234 5678.
Nos lignes téléphoniques sont coupées pendant notre déménagement, merci de répondre
uniquement par mail. Cordialement, La comptabilité.
```
*Dans le fichier des fournisseurs, l'adresse mail de Rhône Mobilité Location se termine par « @rhone-mobilite-location.fr ». La facture d'octobre (RML-2610-0198, 540,00 €) a été payée le 12/10/2026.*

## Travail à faire

1. Pour chacune des huit pièces, dites si vous **acceptez** la facture (saisie) ou si vous la **bloquez** (pas de saisie, registre des factures en attente). Justifiez en une ou deux phrases.
2. Pour chaque facture bloquée, dites **qui vous contactez** (fournisseur, chef de service, salarié, directrice) et **ce que vous demandez**.
3. Pour la pièce 5, expliquez pourquoi la facture ne doit pas être passée en charge de 2026.
4. Pour la pièce 8, listez ce que vous faites **dans l'heure**.
5. Passez les écritures des factures acceptées au 09/11/2026 (journal AC), avec le code analytique de chaque ligne de charge. Vérifiez que votre écriture est équilibrée.
6. Rédigez le court mail que vous envoyez à la directrice pour lui présenter le tri du lundi.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E17-01_corrige.md)
