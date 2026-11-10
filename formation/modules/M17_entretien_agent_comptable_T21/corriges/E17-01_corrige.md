# Corrigé E17-01 — Le circuit des factures : huit factures arrivées lundi matin

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E17-01](../exercices/E17-01_circuit-factures-huit-factures-lundi.md)

!!! abstract "En clair"
    Sur huit factures, **trois seulement** sont saisies ce lundi. Les cinq autres ne sont pas « mauvaises » : elles attendent une réponse (un avoir, un bon de commande, une facture au bon nom). Le travail de l'agent comptable, ici, c'est surtout **de savoir à qui parler**.

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### La grille de contrôle (la même pour chaque facture)

Pour chaque pièce, posez-vous cinq questions, dans cet ordre :

1. **Est-ce pour nous ?** Nom, adresse et SIREN de l'association.
2. **L'avons-nous déjà ?** Même fournisseur, même numéro, même montant dans le compte 401 (ou dans le 4081).
3. **L'avons-nous commandé ?** Bon de commande, devis signé ou contrat.
4. **Le montant est-il juste ?** Quantités × prix, taux et calcul de la TVA, total TTC, comparaison avec le devis.
5. **Peut-on payer sans risque ?** Coordonnées bancaires connues, pas de demande inhabituelle.

Si une seule réponse est « non » ou « je ne sais pas », la facture est **bloquée**.

### Questions 1 et 2 — Pièce par pièce

| Pièce | Fournisseur | Décision | Pourquoi | Qui contacter, pour demander quoi |
|---|---|---|---|---|
| 1 | Bureau Plus Valence | **Bloquée : doublon** — pas de saisie | La même facture (n° BPV-26-2231, 223,80 €) a déjà été saisie le 28/10 à partir de la PA. Le papier est un **duplicata**. | Personne en urgence. Tamponner « DOUBLON – déjà saisie le 28/10 » et classer. Mail au fournisseur : ne plus envoyer de papier en plus de la PA. |
| 2 | MédiaTech Valence | **Bloquée : pas au nom de l'association** | La facture est au nom de **Thomas Girard**, à son adresse personnelle. Pour l'association, ce n'est pas une dette fournisseur : MédiaTech est déjà payé. Et 329,00 € > 150 € : il fallait un bon de commande. | **Karim Belkacem** : l'achat était-il prévu, et qui l'a autorisé ? **Directrice** : accepte-t-elle l'achat a posteriori ? **Thomas Girard** : demander au magasin une facture au nom de l'association (ticket à l'appui), puis déposer une **note de frais**. |
| 3 | Formations Inclusives Sud | **Bloquée : pas de bon de commande** | 1 200,00 € de formation, sans devis ni bon de commande. On ne sait pas qui a commandé, ni si la formation a eu lieu. | **Sophie Laurent** à son retour le 12/11 : a-t-elle commandé ? feuille d'émargement ? Était-ce prévu au plan de formation ? Une prise en charge par l'**OPCO** (opérateur de compétences de la branche) est-elle possible ? |
| 4 | Peinture Rhodanienne | **Bloquée : montant supérieur au devis** | Devis signé : 2 400,00 € TTC. Facture : 3 120,00 € TTC. Les 600,00 € HT de « travaux supplémentaires » n'ont jamais été acceptés par écrit. | **Karim Belkacem** : a-t-il accepté le rebouchage, à quel prix ? Puis le **fournisseur** : soit un **avoir** de 720,00 € TTC, soit un devis complémentaire signé par la directrice. |
| 5 | Ateliers Drôme Impression | **Acceptée** — saisie **sur le 4081**, pas en charge | Facture réelle (bon de livraison de décembre 2025), jamais reçue jusqu'ici, et une **charge à payer** de 1 080,00 € existe déjà dans le 4081 depuis le 31/12/2025. | **Directrice** pour le BAP. Prévenir le fournisseur que le paiement suivra. |
| 6 | Sign'Alpes | **Bloquée : TVA mal calculée** | 650,00 € × 20 % = **130,00 €**, pas 150,00 €. Le TTC juste est **780,00 €**, pas 800,00 €. Vous ne pouvez pas corriger vous-même la facture d'un fournisseur. | **Fournisseur** : un **avoir** qui annule la facture et une nouvelle facture juste (ou une facture rectificative). Le refus peut aussi être signalé par la PA. |
| 7 | Alpes Copie Services | **Acceptée** — saisie | Prestation prévue au contrat, montant juste. Il manque le **SIREN du client** : c'est une anomalie de forme. Elle ne change ni la dette, ni le montant. | **Fournisseur** : ajouter le SIREN 999 210 021 sur les prochaines factures. **Directrice** pour le BAP. |
| 8 | Rhône Mobilité Location | **Facture acceptée — paiement sur l'ancien RIB uniquement** | La facture arrive par la PA, avec le **même IBAN que le contrat**. Le **mail** est une tentative de **fraude au changement de RIB** : domaine en « .co » au lieu de « .fr », urgence, banque étrangère, refus du téléphone, réclamation d'une facture d'octobre **déjà payée**. | **Le fournisseur, au numéro du contrat** (jamais celui du mail). **La directrice et la trésorière**, qui signent les virements. |

> 💡 Réflexe senior : bloquer une facture ne veut pas dire la refuser. Une facture bloquée a toujours **un nom** (la personne qui doit répondre) et **une date de relance**. Notez-les dans le registre des factures en attente.

### Question 3 — La facture de 2025 (pièce 5)

Au 31/12/2025, le cabinet a vu un bon de livraison sans facture. Il a donc passé une **charge à payer** (facture non parvenue, FNP) :

- en 2025 : débit 6237 Publications (ou le compte d'impression utilisé), crédit **4081** : 1 080,00 €.

La charge **est déjà dans les comptes de 2025**. Si vous passez aujourd'hui « 6237 / 401 », vous comptez la dépense **deux fois** :
- une fois en 2025 (déjà fait) ;
- une fois en 2026, dans le service 90-ASSO, qui n'a rien acheté cette année.

Et le 4081 resterait créditeur pour toujours. La bonne écriture **solde le 4081** et crée la dette envers le fournisseur : débit 4081, crédit 401ADI.

Deux vérifications avant de saisir :
- le compte 401ADI n'a aucun mouvement : la facture n'a pas été payée « en douce » ;
- le montant de la facture est **égal** à la FNP (1 080,00 €). S'il y avait un écart, il irait en charge de 2026, sur le code 90-ASSO.

### Question 4 — Pièce 8 : ce que vous faites dans l'heure

1. **Ne pas répondre** au mail. **Ne pas cliquer**. **Ne pas modifier** le fichier des fournisseurs.
2. Appeler Rhône Mobilité Location **au numéro du contrat** ou des factures précédentes. Demander si leur banque a changé.
3. Transférer le mail (sans le supprimer) à la **directrice** et à la **trésorière**, avec un mot court : « tentative de fraude, aucun paiement fait ».
4. Vérifier qu'aucun autre fournisseur n'a reçu de demande du même genre, et prévenir la banque si un virement a été préparé.
5. Saisir la facture normalement : elle est juste. Elle sera payée sur l'**IBAN habituel**, après le bon à payer.

La directrice décidera d'un **signalement** (plainte ou plateforme officielle de signalement des escroqueries).

> ⚠️ Erreur classique : penser que la double signature protège de tout. Ici, la facture fait 540,00 € : en dessous de 1 500 €, **une seule** signature suffit. Le contrôle du RIB est donc **la seule** barrière.

## 2. Calculs (détaillés, chaque montant justifié)

| Pièce | Contrôle | Résultat |
|---|---|---|
| 1 | 186,50 × 20 % = 37,30 ; 186,50 + 37,30 = 223,80 | Facture juste, mais **déjà saisie** le 28/10 |
| 2 | 274,17 × 20 % = 54,83 ; 274,17 + 54,83 = 329,00 | Juste, mais au nom d'un salarié |
| 4 | Devis 2 000,00 + 400,00 = 2 400,00 TTC ; facture 2 600,00 + 520,00 = 3 120,00 TTC | Écart **720,00 € TTC** (600,00 HT + 120,00 TVA), soit **+30 %** |
| 5 | 900,00 × 20 % = 180,00 ; 900,00 + 180,00 = 1 080,00 | Égal à la FNP de 1 080,00 € ✓ |
| 6 | 5 × 130,00 = 650,00 HT ; 650,00 × 20 % = **130,00** (facture : 150,00) | TTC juste **780,00 €** (facture : 800,00 €) → 20,00 € facturés en trop |
| 7 | 375,00 × 20 % = 75,00 ; 375,00 + 75,00 = 450,00 ; contrat : 375,00 HT/trimestre | Juste ✓ |
| 8 | 450,00 × 20 % = 90,00 ; 450,00 + 90,00 = 540,00 | Juste ✓, IBAN identique au contrat ✓ |

**Pourquoi la TVA est « dans la charge »** : Cap Horizons 21 ne récupère pas la TVA. Le coût réel d'une facture, c'est le **TTC**. Pour la pièce 6, les 20,00 € de TVA en trop seraient donc une **vraie perte** pour l'association. Ce n'est pas une petite erreur sans conséquence.

**Total saisi ce lundi** : 1 080,00 + 450,00 + 540,00 = **2 070,00 €**, dont **990,00 €** de charges 2026 (450,00 + 540,00).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| 09/11/2026 | AC | 4081 | Fournisseurs – factures non parvenues | ADI-2025-0412 du 18/12/2025 – reprise FNP 2025 | — | 1 080,00 | |
| 09/11/2026 | AC | 401ADI | Fournisseur Ateliers Drôme Impression | ADI-2025-0412 du 18/12/2025 – plaquettes | — | | 1 080,00 |
| 09/11/2026 | AC | 6156 | Maintenance | ACS-26-1093 du 31/10/2026 – maintenance copieur siège T4 (TTC) | 01-SIEGE | 450,00 | |
| 09/11/2026 | AC | 401ACS | Fournisseur Alpes Copie Services | ACS-26-1093 du 31/10/2026 | — | | 450,00 |
| 09/11/2026 | AC | 6135 | Locations mobilières | RML-2611-0207 du 01/11/2026 – LLD Clio SAVS novembre (TTC) | 20-SAVS | 540,00 | |
| 09/11/2026 | AC | 401RML | Fournisseur Rhône Mobilité Location | RML-2611-0207 du 01/11/2026 | — | | 540,00 |
| | | | | **Totaux** | | **2 070,00** | **2 070,00** |

Remarques :
- **Pas de code analytique sur les comptes de bilan** (4081, 401) : l'analytique sert à répartir les **charges et les produits** entre les services.
- **Pas de compte 4456x** : la TVA n'est pas récupérable. Elle reste dans le montant de la charge.
- La location du véhicule va au **SAVS** : la Clio est affectée à ce service. Le copieur du siège va en **01-SIEGE** ; il sera refacturé aux services avec les frais de siège.

## 4. Points d'attention / pièges

- **Le doublon « papier + PA »** : avec la facturation électronique, le même document arrive souvent deux fois pendant la transition. Avant de saisir, cherchez toujours **le numéro de facture** dans le compte du fournisseur.
- **Saisir puis contrepasser un doublon** : c'est du bruit dans les comptes et un risque de double paiement. On ne saisit pas, on classe.
- **La facture au nom du salarié** : la passer en 401MédiaTech créerait une dette fausse (MédiaTech est déjà payé). Si l'achat est validé, la dette est envers **Thomas**, par note de frais. La tablette devient alors un bien de l'association : notez-la dans l'inventaire du petit matériel. Elle contiendra des données sur des enfants : prévenez aussi le référent informatique.
- **La facture sans bon de commande** : la formation a peut-être bien eu lieu. Mais sans bon de commande, personne n'a vérifié le budget. Et une partie aurait peut-être pu être prise en charge par l'OPCO.
- **Payer le devis et « laisser en attente » le reste** : on ne paie pas une partie de facture sans accord écrit. On obtient un avoir ou un accord signé, puis on paie le tout.
- **La facture 2025 passée en charge 2026** : double comptabilisation de la charge, 4081 jamais soldé, et un compte de service 2026 faux. Ce point est vu par le commissaire aux comptes (CAC).
- **La TVA « qui ne compte pas »** : une comptable venue d'une entreprise commerciale pense parfois que la TVA ne coûte rien. Dans une association qui ne récupère pas la TVA, **chaque euro de TVA est une charge**.
- **Le SIREN manquant** : l'anomalie est réelle, mais elle n'empêche pas de reconnaître une dette juste et prévue au contrat. Les PME peuvent encore émettre des factures papier ou PDF jusqu'au **01/09/2027**. L'association, elle, doit pouvoir **recevoir** des factures électroniques depuis le 01/09/2026 *(dès lors qu'elle est assujettie à la TVA, même pour des opérations exonérées : point à confirmer avec l'expert-comptable)*. Une autre organisation pourrait choisir de bloquer : l'important est de **justifier** son choix et de demander la correction.
- **La fraude au RIB** : les signes sont presque toujours les mêmes. Domaine de mail proche, urgence, banque étrangère, refus du téléphone, demande de payer des factures déjà réglées.

> 💡 Réflexe senior : un changement de RIB se traite **uniquement** avec trois preuves. Un courrier ou une attestation sur papier à en-tête avec un **RIB original**. Un **contre-appel** à un numéro déjà connu. Et une **double validation** interne (agent comptable + directrice) avant de modifier le fichier des fournisseurs.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à la directrice (question 6) :**

> Objet : Factures reçues le 9/11 — 3 à valider, 5 en attente, 1 tentative de fraude
>
> Bonjour Nathalie,
>
> **À valider (bon à payer jeudi)** : Ateliers Drôme Impression 1 080,00 € (facture de décembre 2025, déjà provisionnée dans les comptes 2025, 2e relance) ; Alpes Copie Services 450,00 € (contrat copieur, SIREN manquant signalé au fournisseur) ; Rhône Mobilité Location 540,00 € (loyer de novembre de la Clio du SAVS).
>
> **En attente** : MédiaTech 329,00 € (tablette du SESSAD, facture au nom de Thomas Girard : j'en parle avec Karim) ; Formations Inclusives Sud 1 200,00 € (pas de bon de commande, je vois Sophie jeudi à son retour) ; Peinture Rhodanienne 3 120,00 € (720,00 € de plus que le devis signé, je vois Karim) ; Sign'Alpes 800,00 € (erreur de TVA de 20,00 €, avoir demandé). Bureau Plus : doublon papier d'une facture déjà saisie, classé.
>
> **Alerte** : ce matin, mail frauduleux « changement de RIB » au nom de Rhône Mobilité Location (banque en Lituanie, adresse en .co). Le fournisseur a confirmé par téléphone qu'il n'a pas changé de banque. Aucun paiement n'a été fait. Je vous transfère le mail pour un éventuel signalement.
>
> Bonne journée,
> [Prénom Nom], agent comptable

**Autres bonnes pratiques :**
- Tenir le **registre des factures en attente** : fournisseur, montant, motif, personne relancée, date de relance. À la clôture, il sert à repérer les **charges à payer**.
- En fin de mois, comparer ce registre avec les **bons de livraison** reçus : une prestation faite mais une facture bloquée reste une **charge de l'exercice**.
- Proposer un rappel en réunion de cadres : « pas de bon de commande, pas de paiement » et « on ne paie rien avec sa carte personnelle sans accord ».

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Règlement ANC n° 2018-06 (comptes annuels des personnes morales de droit privé à but non lucratif) et PCG : compte 408 « Fournisseurs – factures non parvenues », comptes 401, 61, 62.
- CGI, art. 289 et annexe II (mentions obligatoires des factures), et textes de la réforme de la facturation électronique : réception obligatoire depuis le 01/09/2026, émission obligatoire pour les PME au 01/09/2027, nouvelles mentions (SIREN du client, nature de l'opération…).
- Code de commerce : mentions obligatoires des factures et délais de paiement, pénalités de retard et indemnité forfaitaire de 40 € pour frais de recouvrement (*articles à citer selon le texte en vigueur*).
- CGI : exonération de TVA de la formation professionnelle continue (*article à vérifier*).
- Fiche de l'association Cap Horizons 21 : § 3.7 (chaîne de validation des factures) et § 3.8 (TVA non récupérable).
