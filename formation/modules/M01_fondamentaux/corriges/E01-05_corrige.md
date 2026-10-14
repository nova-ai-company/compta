# Corrigé E01-05 — « Je vous ai tout envoyé par WhatsApp »

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-05](../exercices/E01-05_photo-whatsapp-petit-zinc.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

La question centrale est : **où est l'original de la facture ?** Le droit à déduction de la TVA et la valeur probante de la comptabilité reposent sur l'original (ou sur une copie qui a légalement la même valeur).

| Pièce | Nature de l'original | Valeur de ce que Clara a envoyé |
|---|---|---|
| **Primeurs Croix-Rousse** | Facture **papier** remise par un fournisseur PME (qui peut encore facturer sur papier ou en PDF jusqu'au 01/09/2027). L'original est **le papier** détenu au restaurant. | La photo est une **simple copie de travail**. Ce n'est **ni** une facture électronique (pas de flux structuré via PA), **ni** une copie fiable au sens de l'arrêté du 22 mars 2017 (pas de processus de numérisation garantissant l'intégrité, pas de cachet/horodatage, image incomplète et partiellement illisible). |
| **CHR Distribution** | CHR est une ETI (1 800 salariés) → depuis le 01/09/2026, elle **émet obligatoirement** ses factures sous forme électronique via PA. L'original est le **flux électronique structuré** reçu par la PA du Petit Zinc le 30/09 (déjà présent dans l'outil). | Le PDF est la **représentation lisible** du flux : une copie, sans valeur d'original. L'intégrer créerait un **doublon**. |
| **Reçu du marché** | Il n'existe pas de facture : un maraîcher de marché vendant à un professionnel devrait en principe établir une facture, mais en pratique on n'a qu'un reçu. Le reçu papier est la seule pièce. | Justifie la **dépense** (avec le brouillard de caisse) ; **aucune TVA** n'est mentionnée → rien à déduire. |

**TVA de la facture Primeurs (question 2).** Le droit à déduction suppose de **détenir** une facture conforme. On ne déduit pas sur une photo illisible : la date est masquée (impossible de vérifier la période de déduction), et l'image ne garantit pas l'intégrité. **Démarche :** demander à Clara de déposer l'original papier (ou de le numériser selon une procédure conforme) ; à défaut, demander un **duplicata** au fournisseur. En attendant, la facture peut être comptabilisée **sous condition** — on préfère attendre l'original avant déduction.

**PDF CHR (question 3).** Ne **pas** l'intégrer : le flux PA est déjà dans l'outil et sera comptabilisé automatiquement. Intégrer aussi le PDF doublerait la charge (1 700,00 €) et la TVA (160,20 €). Le statut « Mise à disposition » signifie que la facture est à disposition du destinataire ; c'est sur ce flux que l'on travaille.

> 💡 La facture électronique a une conséquence pratique : pour les fournisseurs GE/ETI, **le client n'a plus besoin de vous envoyer quoi que ce soit** — vous récupérez l'original dans le flux de la PA. Ce qu'il faut demander à Clara, ce sont uniquement les pièces des petits fournisseurs (papier/PDF) et les pièces non facturées (reçus, contrats).

## 2. Calculs (détaillés, chaque montant justifié)

**Primeurs Croix-Rousse** : 40 × 1,85 = 74,00 ; 18 × 4,50 = 81,00 ; 6 × 9,00 = 54,00 ; 5 × 15,00 = 75,00 → **284,00 € HT** ✓. TVA 5,5 % : 284,00 × 5,5 % = 15,62 € ✓. TTC **299,62 €** ✓.

**CHR Distribution** :
- 1 240,00 × 5,5 % = **68,20 €** ✓
- 460,00 × 20 % = **92,00 €** ✓
- Total HT 1 700,00 € ; TVA 160,20 € ; TTC **1 860,20 €** ✓.

Ventilation : les produits frais sont des **matières premières** transformées en cuisine (601) ; les vins et spiritueux servis en l'état sont des **marchandises** (607) — distinction utile pour le calcul des ratios matière (coût matière / CA nourriture ; coût boissons / CA boissons).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 29/09/2026 | AC | 601 | Achats de matières premières (denrées) | CHR Distribution F CHR-26-0929-77412 (flux PA) | 1 240,00 | |
| 29/09/2026 | AC | 607 | Achats de marchandises (vins, spiritueux) | CHR Distribution F CHR-26-0929-77412 (flux PA) | 460,00 | |
| 29/09/2026 | AC | 44566 | TVA déductible sur ABS | CHR Distribution F CHR-26-0929-77412 (68,20 + 92,00) | 160,20 | |
| 29/09/2026 | AC | 401CHRD | Fournisseur CHR Distribution | CHR Distribution F CHR-26-0929-77412 (flux PA) | | 1 860,20 |
| 2x/09/2026 | AC | 601 | Achats de matières premières (denrées) | Primeurs Croix-Rousse F 2026-0918 (sur original) | 284,00 | |
| 2x/09/2026 | AC | 44566 | TVA déductible sur ABS | Primeurs Croix-Rousse F 2026-0918 (sur original) | 15,62 | |
| 2x/09/2026 | AC | 401PRIM | Fournisseur Primeurs Croix-Rousse | Primeurs Croix-Rousse F 2026-0918 (sur original) | | 299,62 |
| 26/09/2026 | CA | 601 | Achats de matières premières (denrées) | Herbes aromatiques marché St-Antoine (reçu R. Moulin) | 45,00 | |
| 26/09/2026 | CA | 530 | Caisse | Herbes aromatiques marché St-Antoine (reçu R. Moulin) | | 45,00 |
| | | | | **Totaux** | **2 204,82** | **2 204,82** |

Conditions :
- **CHR** : l'écriture est générée **à partir du flux PA**, pas du PDF. Si l'outil l'a déjà intégrée, il n'y a rien à saisir : on vérifie seulement la ventilation 601 / 607.
- **Primeurs** : date exacte (« 2x/09 ») à compléter à réception de l'original ou du duplicata ; la TVA de 15,62 € n'est déduite qu'une fois l'original en main. Si l'original est perdu, le fournisseur peut délivrer un **duplicata** portant la mention « duplicata ».
- **Reçu du marché** : charge justifiée par le reçu et le brouillard de caisse ; pas de TVA. Pour un montant récurrent, demander au maraîcher une facture.

## 4. Points d'attention / pièges

- **« Une photo, c'est une copie numérique, donc c'est bon. »** Non. La numérisation ne permet de détruire l'original papier que si elle respecte les conditions réglementaires (copie **fidèle** à l'original, format PDF ou PDF/A, procédé garantissant **l'intégrité** — cachet serveur, empreinte numérique, signature électronique ou horodatage —, **conservation** dans des conditions préservant l'intégrité, procédure documentée). Une photo WhatsApp compressée, recadrée, tachée ne remplit aucune de ces conditions.
- **Facture électronique ≠ PDF.** Le PDF « représentation lisible » d'un Factur-X n'a pas valeur d'original ; l'original est conservé dans sa forme électronique d'origine (le flux).
- **Doublons** : le risque principal de la période de transition 2026-2027 est d'avoir la même facture en flux PA **et** en PDF/photo.
- **WhatsApp et confidentialité** : les pièces d'un client sur la messagerie d'un téléphone de collaborateur posent un problème de sécurité et de traçabilité (le cabinet ne peut pas démontrer la date de réception ni garantir la conservation). Rediriger vers la plateforme de dématérialisation.
- **Durées** : conservation 10 ans (Code de commerce) ; 6 ans au titre du droit de contrôle fiscal (LPF art. L. 102 B), sous la forme d'origine (papier pour le papier, électronique pour l'électronique).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse à Clara (par e-mail, pas par WhatsApp) :**

> Bonjour Clara,
>
> Merci pour les pièces. Quelques règles importantes, pour vous protéger en cas de contrôle :
>
> 1. **Ne jetez pas les originaux papier.** Une photo de facture n'a pas la valeur d'une facture : en cas de contrôle, la TVA correspondante pourrait être refusée. Il faut conserver les originaux **10 ans**.
> 2. **Vos gros fournisseurs (CHR Distribution, etc.) vous facturent désormais électroniquement via votre plateforme.** Nous recevons ces factures directement : inutile de nous les transférer — cela crée même des doublons.
> 3. **Pour les petits fournisseurs (primeurs, marché…)**, qui facturent encore sur papier jusqu'en septembre 2027 : déposez les originaux dans la bannette mensuelle ou numérisez-les depuis l'application de notre plateforme de dématérialisation (pas WhatsApp), une fois par semaine.
> 4. **Pour libérer votre placard** : il est possible de détruire les originaux papier après une **numérisation conforme** (procédé qui garantit l'intégrité de la copie, avec horodatage et conservation sécurisée). Notre plateforme propose ce service ; nous pouvons vous le présenter lors de notre prochain rendez-vous. D'ici là, archivez les cartons à la cave plutôt que de jeter.
>
> Dernier point : pouvez-vous déposer l'original de la facture Primeurs Croix-Rousse n° 2026-0918 ? La date est illisible sur la photo.
>
> Belle soirée,

**Contrôles et documentation :**
- vérifier dans l'outil qu'aucun PDF CHR n'a déjà été intégré à côté du flux PA (recherche par n° de facture sur juillet-septembre) ;
- créer une règle « fournisseurs facturant via PA » pour le Petit Zinc et bloquer l'intégration de PDF de ces fournisseurs ;
- note au dossier permanent : « canal de transmission des pièces : plateforme, pas WhatsApp — client informé le … ».

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 289 (règles de facturation, forme et conservation des factures) et art. 289 VII (copie fiable, piste d'audit, numérisation).
- Arrêté du 22 mars 2017 fixant les modalités de numérisation des factures papier (CGI, annexe IV) — conditions de la copie fiable.
- CGI art. 289 bis : facturation électronique et calendrier (réception 01/09/2026 ; émission ETI 01/09/2026, PME 01/09/2027).
- LPF art. L. 102 B : durée et forme de conservation (6 ans, forme originale).
- Code de commerce art. L. 123-22 : conservation 10 ans des pièces justificatives.
- CGI art. 271 : déduction subordonnée à la détention d'une facture.
