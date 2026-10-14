# Corrigé E02-10 — Clôture du garage : doublon PDF / PA, facture au nom du gérant, LCR et livraison sans facture

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E02-10](../exercices/E02-10_doublon-pa-gerant-lcr-garage.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### AutoDistrib : le doublon PA / PDF (question 1)
AutoDistrib est une **ETI** : depuis le **01/09/2026**, elle émet ses factures sous forme **électronique** via une plateforme agréée. Garage Martin reçoit l'**original** — le flux Factur-X — dans sa PA ; il a été intégré automatiquement le 25/09 (AC-0947). Le PDF envoyé par e-mail le 26/09 n'est qu'une **copie de courtoisie** : sa saisie (AC-0952) crée un **doublon**.

Conséquences si l'erreur n'avait pas été vue :
- **résultat** minoré de **2 846,50 €** (charge en double) ;
- **TVA** déductible majorée de **569,30 €** sur la CA3 de septembre → rappel + intérêts de retard en cas de contrôle ;
- **dette fournisseur** surévaluée de 3 415,80 € → risque de **double paiement** (la secrétaire paie « ce qui est dans la compta ») ;
- **stock** : aucune incidence (le stock est inventorié physiquement), mais le coût d'achat consommé est faussé.

Correction : **contre-passer AC-0952** (et non AC-0947, qui est l'original) avec un libellé explicite.

### Pneus Express : facture au nom du gérant (question 2)
La dépense est **professionnelle** (pneus de la dépanneuse, véhicule utilitaire inscrit à l'actif). Mais la facture est adressée à **M. Thierry Martin, à son domicile** : la TVA n'est **pas déductible** par l'EURL sur ce document (la déduction suppose une facture au nom de l'assujetti). Thierry l'a payée personnellement : l'EURL lui doit 513,60 € (via son compte courant).

Solution : obtenir de Pneus Express un **avoir** annulant la facture PE-26-07731 et une **nouvelle facture au nom de Garage Martin EURL** (dénomination, adresse du siège, SIREN), mentionnant qu'elle est acquittée. La TVA de 85,60 € devient alors déductible (véhicule utilitaire : pas d'exclusion).

**Au 30/09/2026**, la nouvelle facture n'est pas encore émise. La charge (entretien de la dépanneuse en septembre) appartient à l'exercice → on constate une **facture non parvenue** pour la facture à recevoir au nom de l'EURL (montant certain, bien reçu). À réception de la facture en octobre : extourne de la FNP, saisie de la facture, puis constatation de la dette envers Thierry (le fournisseur ayant déjà été payé par lui).

> Variante : si Pneus Express refuse de refacturer, la dépense peut être remboursée à Thierry sur la base de la facture à son nom, comptabilisée en charge **TTC** (sans déduction de TVA), à condition de démontrer son caractère professionnel (immatriculation de la dépanneuse sur la facture : c'est le cas).

### LCR (question 3)
Le « bon à payer » donné le 25/09 sur la LCR transforme la dette fournisseur ordinaire en **effet à payer** : on vire le montant de 401HUIL en **403 « Fournisseurs – effets à payer »**. À l'échéance du 10/10, la banque débite le compte : 403 / 512. Au bilan du 30/09/2026, les 1 932,00 € figurent toujours dans les **dettes fournisseurs et comptes rattachés** (403 est un compte de dette fournisseur), avec une échéance à moins d'un an.

### Livraison du 29/09 (question 4)
Les huiles et filtres sont **livrés** et **inventoriés** au 30/09 : sans FNP, le stock final les inclurait sans achat correspondant → résultat surévalué de 456,00 €. → **FNP**.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | HT | TVA 20 % | TTC |
|---|---|---|---|
| AutoDistrib FA-88412 (doublon à annuler) | 2 846,50 € | 569,30 € | 3 415,80 € |
| Pneus Express : 4 × 95,00 + 4 × 12,00 | 380,00 + 48,00 = 428,00 € | 85,60 € | 513,60 € |
| LCR Huiles & Lubrifiants | 1 610,00 € | 322,00 € | 1 932,00 € |
| Livraison 29/09 : 60 × 6,20 + 10 × 8,40 | 372,00 + 84,00 = 456,00 € | 91,20 € | 547,20 € |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | AC | 401AUTO | Fournisseur AutoDistrib Rhône | Extourne doublon AC-0952 (PDF de FA-88412, original = flux PA AC-0947) | 3 415,80 | |
| 30/09/2026 | AC | 607 | Achats de marchandises (pièces détachées) | Extourne doublon AC-0952 FA-88412 | | 2 846,50 |
| 30/09/2026 | AC | 44566 | TVA déductible sur ABS | Extourne doublon AC-0952 FA-88412 | | 569,30 |
| 25/09/2026 | OD | 401HUIL | Fournisseur Huiles & Lubrifiants du Rhône | Acceptation LCR HL-2026-0831 éch. 10/10/2026 | 1 932,00 | |
| 25/09/2026 | OD | 403 | Fournisseurs – effets à payer | Acceptation LCR HL-2026-0831 éch. 10/10/2026 | | 1 932,00 |
| 30/09/2026 | OD | 6155 | Entretien et réparations sur biens mobiliers | FNP Pneus Express – pneus dépanneuse GH-417-TM (refacturation EURL) | 428,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP Pneus Express – pneus dépanneuse | 85,60 | |
| 30/09/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Pneus Express – pneus dépanneuse | | 513,60 |
| 30/09/2026 | OD | 607 | Achats de marchandises (lubrifiants, filtres) | FNP Huiles & Lubrifiants BL BLH-26-4410 du 29/09 | 456,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP Huiles & Lubrifiants BL BLH-26-4410 | 91,20 | |
| 30/09/2026 | OD | 408 | Fournisseurs – factures non parvenues | FNP Huiles & Lubrifiants BL BLH-26-4410 | | 547,20 |
| 10/10/2026 | BQ | 403 | Fournisseurs – effets à payer | Échéance LCR HL-2026-0831 | 1 932,00 | |
| 10/10/2026 | BQ | 512 | Banque | Échéance LCR HL-2026-0831 | | 1 932,00 |
| | | | | **Totaux** | **8 340,60** | **8 340,60** |

**Suite en octobre pour Pneus Express** (après extourne de la FNP au 01/10/2026) :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| (date facture) | AC | 6155 | Entretien et réparations sur biens mobiliers | Pneus Express F (refacturation EURL) pneus dépanneuse | 428,00 | |
| (date facture) | AC | 44566 | TVA déductible sur ABS | Pneus Express F (refacturation EURL) | 85,60 | |
| (date facture) | AC | 401PNEU | Fournisseur Pneus Express | Pneus Express F (refacturation EURL) | | 513,60 |
| (date facture) | OD | 401PNEU | Fournisseur Pneus Express | Facture acquittée par T. Martin (CB perso 15/09) | 513,60 | |
| (date facture) | OD | 455TMAR | Associé – compte courant T. Martin | Facture acquittée par T. Martin (CB perso 15/09) | | 513,60 |
| | | | | **Totaux** | **1 027,20** | **1 027,20** |

Puis remboursement de Thierry : 455TMAR / 512 (ou maintien en compte courant).

## 4. Points d'attention / pièges

- **Ne pas extourner le mauvais côté** : c'est le **PDF** (AC-0952) qui est le doublon ; le flux PA (AC-0947) est l'original. Lettrer ensuite AC-0952 avec son extourne.
- **Le fournisseur avait raison** : un relevé fournisseur ou un simple appel aurait évité le doublon. Avec la PA, la question « quel est l'original ? » a une réponse simple : **le flux**.
- **TVA de la FNP** (44586) : **non déductible** tant que la facture n'est pas reçue ; elle est extournée au 01/10 et déduite sur la CA3 du mois de réception de la facture.
- **Facture au nom du gérant** : le caractère professionnel ne suffit pas à déduire la TVA ; c'est le **destinataire** de la facture qui compte. Mais la **charge** peut être professionnelle → on régularise la facture plutôt que de perdre la TVA.
- **LCR** : le 403 reste une dette fournisseur. Ne pas l'oublier dans la balance âgée et le rapprochement bancaire (la sortie de trésorerie est à l'échéance, pas à l'acceptation).
- **Garage Martin vend aussi des VO** : si les pneus avaient été montés sur un VO en stock destiné à la revente, la dépense serait un coût de remise en état à incorporer au **coût du VO en stock** — et pour un VO relevant de la TVA sur la marge, la TVA sur les frais de remise en état reste déductible dans les conditions de droit commun (point à approfondir dans le module TVA).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Procédure pour la secrétaire (question 5) :**
1. **Ne plus saisir aucune facture** : les factures des fournisseurs reliés à la PA (AutoDistrib, et tous les grands fournisseurs) arrivent **automatiquement** dans la comptabilité.
2. **Les PDF reçus par e-mail** de ces fournisseurs sont des **copies** : les classer, ne pas les transmettre au cabinet comme pièces à saisir.
3. **Les factures papier/PDF des petits fournisseurs** (jusqu'en septembre 2027) : les déposer sur la plateforme de dématérialisation du cabinet, une fois par semaine.
4. **Toute facture doit être au nom de « Garage Martin EURL »** avec l'adresse du garage et le SIREN 824 112 309 : vérifier à la caisse du fournisseur avant de payer ; jamais au nom de M. Martin.
5. **Avant chaque paiement ou bon à payer de LCR** : vérifier que la facture n'a pas déjà été payée (rechercher le numéro de facture dans la liste des règlements) et que la livraison est conforme au BL.

**Message à Thierry Martin :**

> Bonjour Thierry,
>
> - **AutoDistrib** : votre fournisseur a raison, il n'y a qu'une facture. La version reçue via la plateforme était déjà enregistrée ; le PDF saisi par votre secrétaire faisait doublon. C'est corrigé — surtout, ne la payez qu'une fois (3 415,80 €).
> - **Pneus de la dépanneuse** : la facture est à votre nom, le garage ne peut pas en récupérer la TVA. Pouvez-vous demander à Pneus Express de la refaire au nom de Garage Martin EURL ? Nous vous rembourserons ensuite 513,60 € via votre compte courant.
> - **Huiles & Lubrifiants** : la LCR de 1 932 € sera débitée le 10/10 ; la livraison du 29/09 est enregistrée dans les comptes de l'exercice.
>
> Je joins une petite procédure pour votre secrétaire, liée à la nouvelle plateforme de factures.

**Contrôles de clôture** : recherche systématique des doublons sur l'exercice (même fournisseur + même n° de facture, ou même montant à quelques jours d'intervalle) depuis la mise en place de la PA en août ; circularisation des 5 principaux fournisseurs ; liste exhaustive des BL de fin septembre sans facture (cut-off) rapprochée de l'inventaire.

**Documentation** : feuille de cut-off achats au 30/09/2026 (FNP Pneus Express, FNP Huiles & Lubrifiants), justificatif de l'extourne du doublon (capture du flux PA), procédure remise au client (date).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 289 bis : facturation électronique (réception obligatoire au 01/09/2026, émission par les ETI au 01/09/2026) ; la facture électronique est l'original.
- CGI art. 271 : déduction de la TVA subordonnée à une facture adressée à l'assujetti.
- CGI, annexe II, art. 206-IV : exclusions (les véhicules utilitaires n'en relèvent pas).
- PCG : comptes 403 « Fournisseurs – effets à payer », 408, 44586, 455 ; rattachement des charges à l'exercice.
- Code de commerce art. L. 511-1 et suivants : lettre de change (la LCR en est la forme dématérialisée).
