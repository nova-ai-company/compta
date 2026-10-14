# Corrigé E01-01 — Quatre factures, combien d'anomalies ?

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E01-01](../exercices/E01-01_anomalies-4-factures.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

On contrôle chaque facture dans le même ordre, toujours : **(1) qui facture à qui ? (2) quoi, quand, combien ? (3) les calculs ; (4) le taux de TVA ; (5) les mentions de paiement ; (6) la forme (papier, PDF, électronique via PA).** Ce qui compte ensuite, c'est la **gravité** : toutes les anomalies ne se valent pas.

| Gravité | Signification | Exemples |
|---|---|---|
| **Bloquante TVA** | La TVA ne peut pas être déduite en l'état | Facture adressée à une autre personne que l'entreprise ; TVA facturée au-delà de ce qui est légalement dû |
| **Bloquante paiement** | Le montant à payer est faux | Erreur de calcul, mauvais taux |
| **Mise en conformité** | Le fournisseur doit corriger ses modèles, sans remettre en cause la déduction de cette facture | Mentions commerciales manquantes (pénalités, 40 €), nouvelle mention absente |

### Pièce 1 — Bois du Lyonnais (4 507,92 €)

Calculs justes (24 × 86,40 = 2 073,60 ; 0,85 × 1 980 = 1 683,00 ; TVA 20 % = 751,32). Taux de 20 % correct (vente de bois à un professionnel).

| Anomalie | Gravité |
|---|---|
| **SIREN du client absent** (nouvelle mention liée à la réforme) | Mise en conformité — à exiger pour la suite |
| **Nature de l'opération** non indiquée (livraison de biens) | Mise en conformité |
| **Taux des pénalités de retard** absent | Mise en conformité (mention commerciale obligatoire, C. com. L. 441-9) |
| **Indemnité forfaitaire de 40 €** absente | Mise en conformité |
| **Conditions d'escompte** (ou mention « pas d'escompte ») absentes | Mise en conformité |

→ **Bon à payer**, la TVA est déductible. Courriel au fournisseur pour mise à jour de ses modèles de facture.

### Pièce 2 — Quincaillerie Pro (1 504,96 €)

Facture la plus complète en mentions (elle comporte même le SIREN client et la nature de l'opération). Mais **le calcul est faux** :
- Total HT : 470,00 + 267,00 + 172,80 + 336,00 = **1 245,80 €** ✓
- TVA 20 % : 1 245,80 × 20 % = **249,16 €**, et non 259,16 € (erreur de 10,00 €, probablement une faute de frappe)
- TTC correct : **1 494,96 €**, et non 1 504,96 €

| Anomalie | Gravité |
|---|---|
| TVA surévaluée de 10,00 € | **Bloquante TVA** pour 10,00 € : seule la TVA légalement due est déductible ; la TVA facturée en trop reste due par le fournisseur (CGI art. 283-3) mais n'ouvre pas droit à déduction chez le client |
| TTC faux | **Bloquante paiement** : on ne paie pas 1 504,96 € |

→ Demander un **avoir de rectification** (ou une facture rectificative) de 10,00 € de TVA, ou payer 1 494,96 € en joignant l'explication **et** obtenir le document rectificatif (sinon le compte fournisseur restera avec 10,00 € non lettrés).

### Pièce 3 — Outillage Direct (982,80 €)

La facture est adressée à **M. Antoine Girard, à son adresse personnelle**, et payée avec sa carte personnelle. Pour le fournisseur, c'est une vente à un particulier.

| Anomalie | Gravité |
|---|---|
| **Destinataire = le gérant à titre personnel**, pas la société | **Bloquante TVA** : la TVA n'est déductible que par l'assujetti à qui la facture est adressée. La société ne peut pas déduire 163,80 € sur une facture au nom d'un tiers. |
| SIREN client absent | Conséquence du point précédent |
| Dépense > 500 € HT (819,00 € HT) | Ce n'est pas une anomalie de facture, mais un point de comptabilisation : **immobilisation** (matériel et outillage), pas une charge |

→ Demander à Outillage Direct d'**annuler la facture par un avoir et de refacturer la société** (dénomination, adresse du siège, SIREN), avec mention que la facture est déjà acquittée. La société remboursera ensuite Antoine Girard (via son compte courant d'associé, puis virement).

### Pièce 4 — MRAD (2 079,00 €)

Trois problèmes, dont deux graves :

1. **Mauvais taux de TVA.** Le taux de 10 % « travaux de rénovation » ne concerne que les **travaux** réalisés dans des logements de plus de deux ans, facturés par l'entreprise qui les exécute au client final. Une **vente de matériaux** à un professionnel (la Menuiserie, qui les incorpore à son ouvrage) relève du **taux normal de 20 %**. C'est éventuellement la Menuiserie qui appliquera 10 % à son client final, si les conditions sont remplies.
   - TVA due : 1 890,00 × 20 % = **378,00 €** (et non 189,00 €) ; TTC : **2 268,00 €**.
   - **Gravité :** bloquante paiement (le montant change) ; la Menuiserie ne peut pas déduire plus que ce qui est facturé, et la facture est irrégulière.
2. **Forme de la facture.** MRAD est une ETI (groupe de 2 300 salariés). Depuis le **01/09/2026**, elle doit **émettre ses factures sous forme électronique via une PA**. Un PDF reçu par e-mail le 23/09/2026 est soit une **copie** d'une facture électronique déjà déposée dans la PA de la Menuiserie (risque de **doublon**), soit le signe que MRAD n'est pas en règle. Dans les deux cas, **on ne comptabilise pas le PDF** : on cherche l'original dans la PA.
3. **Numéro de bon de commande absent** alors que la Menuiserie en a émis un (BC-2026-118) — mention obligatoire lorsque l'acheteur a émis un bon de commande ; il manque aussi les conditions d'escompte.

L'adresse de livraison (chantier) est bien mentionnée, ce qui est correct puisqu'elle diffère de l'adresse du client.

→ **Ne pas payer.** Vérifier dans la PA ; demander à MRAD un avoir total et une nouvelle facture à 20 %, via la PA.

## 2. Calculs (détaillés, chaque montant justifié)

| Pièce | HT | TVA facturée | TVA légalement due | TTC facturé | TTC correct | Écart |
|---|---|---|---|---|---|---|
| 1 Bois du Lyonnais | 3 756,60 € | 751,32 € | 751,32 € | 4 507,92 € | 4 507,92 € | 0,00 € |
| 2 Quincaillerie Pro | 1 245,80 € | 259,16 € | 249,16 € | 1 504,96 € | 1 494,96 € | **– 10,00 €** |
| 3 Outillage Direct | 819,00 € | 163,80 € | 163,80 € (déductible seulement après refacturation à la société) | 982,80 € | 982,80 € | 0,00 € |
| 4 MRAD | 1 890,00 € | 189,00 € | 378,00 € | 2 079,00 € | 2 268,00 € | **+ 189,00 €** |

Ce qu'Antoine Girard voulait payer vendredi : 4 507,92 + 1 504,96 + 2 079,00 = **8 091,88 €** (+ 982,80 € de remboursement personnel).
Ce qui peut être payé vendredi : pièce 1 (**4 507,92 €**) et pièce 2 **corrigée** (**1 494,96 €**), soit **6 002,88 €**. La pièce 4 sera payée à réception de la facture rectifiée (**2 268,00 €**, échéance 21/10) ; le remboursement d'Antoine (**982,80 €**) après refacturation.

## 3. Écritures comptables

Comptes retenus : bois et panneaux = **601** (matières premières) ; quincaillerie, colle, vernis = **6021** (matières consommables) ; scie et rails = **2154** (matériel industriel / outillage, valeur unitaire > 500 € HT).

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 18/09/2026 | AC | 601 | Achats de matières premières | Bois du Lyonnais F BL-F-2026-04417 | 3 756,60 | |
| 18/09/2026 | AC | 44566 | TVA déductible sur ABS | Bois du Lyonnais F BL-F-2026-04417 | 751,32 | |
| 18/09/2026 | AC | 401BOIS | Fournisseur Bois du Lyonnais | Bois du Lyonnais F BL-F-2026-04417 | | 4 507,92 |
| 22/09/2026 | AC | 6021 | Matières consommables | Quincaillerie Pro F 2026-1187 | 1 245,80 | |
| 22/09/2026 | AC | 44566 | TVA déductible sur ABS | Quincaillerie Pro F 2026-1187 | 259,16 | |
| 22/09/2026 | AC | 401QUIN | Fournisseur Quincaillerie Pro | Quincaillerie Pro F 2026-1187 | | 1 504,96 |
| 12/10/2026 | AC | 401QUIN | Fournisseur Quincaillerie Pro | Quincaillerie Pro AV rectif. TVA s/ F 2026-1187 | 10,00 | |
| 12/10/2026 | AC | 44566 | TVA déductible sur ABS | Quincaillerie Pro AV rectif. TVA s/ F 2026-1187 | | 10,00 |
| 09/10/2026 | AC | 2154 | Matériel industriel (outillage) | Outillage Direct F (refacturation société) scie plongeante + rails | 819,00 | |
| 09/10/2026 | AC | 44562 | TVA déductible sur immobilisations | Outillage Direct F (refacturation société) | 163,80 | |
| 09/10/2026 | AC | 404OUTI | Fournisseur d'immobilisations Outillage Direct | Outillage Direct F (refacturation société) | | 982,80 |
| 09/10/2026 | OD | 404OUTI | Fournisseur d'immobilisations Outillage Direct | Facture acquittée par A. Girard (CB perso) | 982,80 | |
| 09/10/2026 | OD | 455GIRA | Associé – compte courant A. Girard | Facture acquittée par A. Girard (CB perso) | | 982,80 |
| 21/09/2026 | AC | 601 | Achats de matières premières | MRAD F MRAD-0926-558214 (flux PA) | 1 260,00 | |
| 21/09/2026 | AC | 6021 | Matières consommables | MRAD F MRAD-0926-558214 (flux PA) | 630,00 | |
| 21/09/2026 | AC | 44566 | TVA déductible sur ABS | MRAD F MRAD-0926-558214 (flux PA) | 189,00 | |
| 21/09/2026 | AC | 401MRAD | Fournisseur MRAD | MRAD F MRAD-0926-558214 (flux PA) | | 2 079,00 |
| 14/10/2026 | AC | 401MRAD | Fournisseur MRAD | MRAD AV total s/ F MRAD-0926-558214 | 2 079,00 | |
| 14/10/2026 | AC | 601 | Achats de matières premières | MRAD AV total s/ F MRAD-0926-558214 | | 1 260,00 |
| 14/10/2026 | AC | 6021 | Matières consommables | MRAD AV total s/ F MRAD-0926-558214 | | 630,00 |
| 14/10/2026 | AC | 44566 | TVA déductible sur ABS | MRAD AV total s/ F MRAD-0926-558214 | | 189,00 |
| 14/10/2026 | AC | 601 | Achats de matières premières | MRAD F rectifiée TVA 20 % | 1 260,00 | |
| 14/10/2026 | AC | 6021 | Matières consommables | MRAD F rectifiée TVA 20 % | 630,00 | |
| 14/10/2026 | AC | 44566 | TVA déductible sur ABS | MRAD F rectifiée TVA 20 % | 378,00 | |
| 14/10/2026 | AC | 401MRAD | Fournisseur MRAD | MRAD F rectifiée TVA 20 % | | 2 268,00 |
| | | | | **Totaux** | **14 414,48** | **14 414,48** |

Remarques sur les écritures :
- La pièce MRAD du 21/09 est passée **d'après le flux reçu dans la PA** (s'il existe), pas d'après le PDF. Si aucune facture n'existe dans la PA, on ne passe que la facture rectifiée.
- L'écriture « avoir + nouvelle facture » conserve une **piste d'audit** complète : on ne modifie jamais la facture d'origine.
- Si Outillage Direct refuse de refacturer, la dépense ne peut pas être prise en charge par la société avec déduction de TVA : à défaut, la scie reste un bien personnel d'Antoine Girard (ou fait l'objet d'un apport/cession formalisé), et la TVA est perdue.
- Les remboursements (paiement de 4 507,92 € et 1 494,96 €, virement de 982,80 € à Antoine Girard) se passent au journal de banque à leur date.

## 4. Points d'attention / pièges

- **La facture la plus « propre » en apparence (pièce 2) contient une erreur de calcul.** Toujours recalculer la TVA, même quand la mise en page est impeccable.
- **Un taux réduit n'est jamais « contagieux »** du client final vers le fournisseur de matériaux.
- **Facture au nom du gérant** : ce n'est pas un détail de forme, c'est l'identité du **titulaire du droit à déduction**. Même chose pour une facture à l'adresse personnelle d'un associé de SCI ou au nom d'un salarié.
- **PDF d'une ETI après le 01/09/2026** : réflexe « doublon + conformité ». Si la Menuiserie comptabilise le PDF puis que le flux PA est intégré automatiquement, la charge et la TVA sont doublées.
- Une mention commerciale manquante (pénalités, 40 €) **ne remet pas en cause** la déduction de la TVA, mais expose le **fournisseur** à une amende : c'est un service à lui rendre que de le signaler, pas une raison de bloquer le paiement.
- L'outillage à 819 € HT ne bénéficie pas de la tolérance des 500 € HT : c'est une **immobilisation**.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Mail à Antoine Girard :**

> Bonjour Monsieur Girard,
>
> Nous avons contrôlé les quatre factures de septembre :
> - **Bois du Lyonnais (4 507,92 €)** : vous pouvez la régler.
> - **Quincaillerie Pro** : la TVA est mal calculée (259,16 € au lieu de 249,16 €). Merci de régler **1 494,96 €** et non 1 504,96 € ; nous leur demandons un avoir de 10 €.
> - **MRAD** : le taux de TVA appliqué (10 %) est erroné, la vente de matériaux à votre entreprise relève de 20 %. Le montant correct est **2 268,00 €**. Par ailleurs, MRAD doit désormais vous facturer via la plateforme agréée : nous vérifions si la facture y figure. **Merci de ne pas la payer** avant réception de la facture rectifiée (échéance 21/10, nous avons le temps).
> - **Scie plongeante** : la facture est à votre nom personnel, la société ne peut pas en déduire la TVA. Nous demandons à Outillage Direct de la refaire au nom de la Menuiserie (SIREN 811 010 202) ; nous vous rembourserons ensuite 982,80 € via votre compte courant. À l'avenir, pensez à donner la raison sociale et le SIREN de la société au moment de l'achat.
>
> Bien cordialement,

**Contrôles et documentation :**
- Note dans le dossier permanent : liste des fournisseurs GE/ETI de la Menuiserie, qui doivent facturer via PA depuis le 01/09/2026 (MRAD en fait partie).
- Paramétrer dans l'outil de pré-comptabilisation une règle « fournisseur MRAD : ne pas intégrer les PDF reçus par e-mail ».
- Vu la situation de trésorerie (C24 en difficulté) : vérifier que les échéances fournisseurs payées « d'un coup » ne mettent pas en péril les échéances URSSAF / SIE, et intégrer ces sorties dans le prévisionnel de trésorerie.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI, annexe II, art. 242 nonies A : mentions obligatoires des factures.
- CGI art. 283-3 : la TVA facturée à tort est due par celui qui la facture.
- CGI art. 271 et suivants : droit à déduction (facture conforme, adressée à l'assujetti).
- CGI art. 289 bis et calendrier de la facturation électronique (réception 01/09/2026 pour tous ; émission GE/ETI 01/09/2026, PME 01/09/2027).
- CGI art. 1737 : amendes pour manquements à la facturation.
- Code de commerce art. L. 441-9 (mentions commerciales) et D. 441-5 (indemnité forfaitaire de 40 €).
- BOFiP : TVA – Taux réduit de 10 % pour les travaux dans les logements ; BIC – Charges – immobilisations de faible valeur (seuil de 500 € HT).
