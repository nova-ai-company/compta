# Corrigé E14-08 — Sous-traitance : nettoyage courant (TVA de droit commun) ou nettoyage de fin de chantier (autoliquidation) ? Et l'attestation URSSAF manquante

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-08](../exercices/E14-08_sous-traitance-nettoyage-autoliquidation-vigilance.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Qui est redevable ?
L'autoliquidation de l'article 283-2 nonies du CGI s'applique aux **travaux de construction** (y compris réparation, **nettoyage**, entretien, transformation, démolition) **en relation avec un bien immobilier**, réalisés par un **sous-traitant** pour un preneur assujetti qui est lui-même entrepreneur principal ou sous-traitant. Le mot « nettoyage » ne vise que le nettoyage **lié à des travaux immobiliers** (typiquement le nettoyage de fin de chantier) ; le **nettoyage courant de locaux en exploitation** n'est pas un travail immobilier et reste soumis à la TVA de droit commun, même s'il est sous-traité (doctrine BOFiP, confirmée selon la fiche interne par une décision du Conseil d'État de février 2026 — *à vérifier*).

| Opération | Nature | Contrat de sous-traitance de travaux immobiliers ? | Redevable de la TVA |
|---|---|---|---|
| GSF Riviera → Bâti Azur (9 800,00 €) | Nettoyage de fin de chantier d'un immeuble neuf | Oui : GSF Riviera sous-traitant de 1er rang de l'entreprise principale | **Bâti Azur** (autoliquidation) ; GSF Riviera facture **HT** |
| Clean → GSF Riviera, CST-0922 (4 600,00 €) | Vitrerie de fin de chantier, même chantier | Oui : sous-traitance de 2e rang | **GSF Riviera** (autoliquidation) ✓ facture correcte |
| Clean → GSF Riviera, CST-0921 (3 200,00 €) | Nettoyage courant des bureaux d'un client industriel | Non : prestation de services de droit commun | **Clean** : facture à 20 % obligatoire ; **CST-0921 est erronée** |

**À Karim Haddad** : « Ce n'est pas moins cher : la TVA est simplement absente d'une facture qui devait en comporter. Nous ne pouvons pas autoliquider nous-mêmes une TVA qui n'entre pas dans le dispositif, ni déduire une TVA non facturée. Si on la laisse passer, Clean ne déclare pas la TVA, et nous, nous n'avons pas de TVA déductible : en cas de contrôle de Clean, il y aura un rappel et une facture rectificative qui nous arrivera tardivement. On la refuse et on demande une facture à 20 % (3 840,00 € TTC, TVA récupérable). »

**À Laure Pellegrino** : « Sans TVA, avec la mention "Autoliquidation" : c'est Bâti Azur qui déclare la TVA. Et de notre côté, nous autoliquidons la vitrerie de Clean. »

### Question 2 — Mentions de la facture GSF Riviera → Bâti Azur
Mentions habituelles + **« Autoliquidation »** (art. 242 nonies A, annexe II CGI) ; montant **HT** seulement (pas de TVA) ; SIREN et n° TVA de Bâti Azur ; **nature : prestation de services** ; adresse du chantier (adresse de réalisation, différente du siège de Bâti Azur) ; référence du contrat de sous-traitance et du chantier.

### Exigibilité de la TVA autoliquidée (CST-0922)
Les travaux immobiliers sont des prestations de services : la TVA autoliquidée devient exigible chez le preneur au moment du **paiement** (encaissement chez le sous-traitant), sauf option pour les débits du sous-traitant (*modalités à vérifier au BOFiP*). Paiement le 22/10 → **CA3 d'octobre**.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Facture GSF → Bâti Azur | HT, sans TVA | 9 800,00 € |
| CST-0922 HT | | 4 600,00 € |
| TVA autoliquidée (20 %, immeuble neuf) | 4 600,00 × 20 % | 920,00 € |
| CST-0921R | 3 200,00 + 640,00 | 3 840,00 € TTC |
| Virement du 22/10 | 3 840,00 + 4 600,00 | **8 440,00 €** |
| Marge brute du chantier (hors main-d'œuvre propre) | 9 800,00 − 4 600,00 | 5 200,00 € |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | VT | 411BATI | Client Bâti Azur Construction | F FR-2026-09-0492 fin de chantier Terrasses du Port – autoliquidation | 9 800,00 | |
| 30/09/2026 | VT | 706 | Prestations de services (ANT) | F FR-2026-09-0492 fin de chantier – autoliquidation | | 9 800,00 |
| 30/09/2026 | AC | 611 | Sous-traitance générale | CST CST-0922 vitrerie fin de chantier (ANT) | 4 600,00 | |
| 30/09/2026 | AC | 401CST | Fournisseur Clean Sous-Traitance | CST CST-0922 – BLOQUÉE vigilance | | 4 600,00 |
| 30/09/2026 | OD | 611 | Sous-traitance générale | FNP CST nettoyage Agrodélices 09/2026 (NIC) | 3 200,00 | |
| 30/09/2026 | OD | 44586 | TVA sur factures non parvenues | FNP CST nettoyage Agrodélices 09/2026 | 640,00 | |
| 30/09/2026 | OD | 4081 | Fournisseurs – factures non parvenues | FNP CST nettoyage Agrodélices 09/2026 | | 3 840,00 |
| 01/10/2026 | OD | 4081 | Fournisseurs – factures non parvenues | Extourne FNP CST 09/2026 | 3 840,00 | |
| 01/10/2026 | OD | 611 | Sous-traitance générale | Extourne FNP CST 09/2026 | | 3 200,00 |
| 01/10/2026 | OD | 44586 | TVA sur factures non parvenues | Extourne FNP CST 09/2026 | | 640,00 |
| 08/10/2026 | AC | 611 | Sous-traitance générale | CST CST-0921R nettoyage Agrodélices 09/2026 (NIC) | 3 200,00 | |
| 08/10/2026 | AC | 44566 | TVA déductible sur ABS | CST CST-0921R TVA 20 % | 640,00 | |
| 08/10/2026 | AC | 401CST | Fournisseur Clean Sous-Traitance | CST CST-0921R – BLOQUÉE vigilance | | 3 840,00 |
| 22/10/2026 | BQ | 401CST | Fournisseur Clean Sous-Traitance | Vir. CST CST-0921R + CST-0922 | 8 440,00 | |
| 22/10/2026 | BQ | 512 | Banque | Vir. CST CST-0921R + CST-0922 | | 8 440,00 |
| 22/10/2026 | OD | 445661 | TVA déductible autoliquidée – sous-traitance BTP | Autoliq. CST-0922 exigible au paiement | 920,00 | |
| 22/10/2026 | OD | 445711 | TVA due autoliquidée – sous-traitance BTP | Autoliq. CST-0922 exigible au paiement | | 920,00 |
| | | | | **Totaux** | **35 280,00** | **35 280,00** |

Remarques :
- **CST-0921** refusée via la PA n'est pas comptabilisée ; la prestation de septembre étant réalisée, on constate une **FNP** au 30/09 pour le montant **correct** (avec TVA).
- **L'avoir CST-AV-0031** n'est pas à saisir chez GSF Riviera puisque la facture CST-0921 n'a jamais été enregistrée (il régularise la comptabilité de Clean) ; on le classe avec la facture refusée.

## 4. Points d'attention / pièges

**CA3 (question 4)** — *libellés et numéros de lignes à vérifier sur le formulaire 3310-CA3 en vigueur* :
- **Septembre** : la facture FR-2026-09-0492 (9 800,00 €) relève, pour GSF Riviera, des **opérations non imposables** chez elle (ligne « autres opérations non imposables », E2), puisque c'est Bâti Azur qui déclare la TVA ; elle n'est pas portée en base taxable. (Si GSF Riviera déclare ses opérations à l'encaissement, on la déclare au mois de l'encaissement, en pratique : point à harmoniser avec la méthode du dossier.)
- **Octobre** : CST-0922 : base 4 600,00 € sur la ligne « autres opérations imposables » (ligne 02) et TVA due 920,00 € au taux normal ; même montant en TVA déductible « autres biens et services » (ligne 20). CST-0921R : 640,00 € en TVA déductible (ligne 20), dans le mois de réception de la facture.
- **Taux de l'autoliquidation** : construction neuve → 20 % ; en rénovation de locaux d'habitation, un taux réduit pourrait s'appliquer.
- **Contrôle de cohérence** : 445661 = 445711 (même montant, même mois) : un écart signale une saisie incomplète.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Obligation de vigilance (question 5).**
- **Constat** : contrat Agrodélices de 38 400 € HT par an (> **5 000 € HT**) et sous-traitance de chantier de 4 600 € HT avec le même cocontractant ; l'attestation URSSAF date du **10/03/2026** → **plus de six mois** au 01/10/2026 : elle n'est plus valable.
- **Règle** : le donneur d'ordre doit obtenir, à la conclusion puis **tous les six mois** jusqu'à la fin du contrat, une attestation de vigilance (et vérifier son authenticité en ligne), un Kbis et, le cas échéant, la liste des salariés étrangers.
- **Risque** : à défaut, **solidarité financière** de GSF Riviera pour les impôts, cotisations, pénalités et rémunérations dues par Clean en cas de travail dissimulé (et, en sous-traitance de chantier, responsabilités spécifiques à l'égard du maître d'ouvrage). Pour un groupe labellisé « achats responsables », c'est aussi un risque d'image.
- **Décision** : **paiement bloqué** jusqu'à réception d'une attestation à jour et vérifiée → reçue le 16/10, paiement le 22/10 ; l'échéance (15/11) est respectée, le blocage n'a donc rien coûté au fournisseur.
- **Sous-traitance de 2e rang** : vérifier que Clean a été **acceptée** par le maître d'ouvrage et que ses conditions de paiement ont été agréées, et que GSF Riviera lui a fourni une garantie de paiement (caution ou délégation) — loi de 1975 sur la sous-traitance. À défaut, Clean pourrait agir directement contre le maître d'ouvrage et le contrat peut être fragilisé.

**Mail à Clean Sous-Traitance (01/10/2026) :**
> Bonjour,
> Votre facture CST-0921 (nettoyage courant des bureaux Agrodélices, septembre) a été refusée sur la plateforme : il s'agit d'une prestation de nettoyage de locaux en exploitation, soumise à la TVA de droit commun (20 %) et non à l'autoliquidation, réservée aux travaux immobiliers. Merci d'émettre un avoir et une facture rectifiée de 3 200,00 € HT + 640,00 € de TVA. La facture CST-0922 (vitrerie de fin de chantier) est correcte. Par ailleurs, votre attestation de vigilance URSSAF date de mars : merci de nous adresser une attestation de moins de six mois ; les règlements sont suspendus dans l'attente.

**Contrôle** : paramétrer dans l'ERP un code TVA par **contrat** (et non par fournisseur), car un même sous-traitant peut relever des deux régimes ; tableau de bord vigilance avec alerte à 5 mois.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 283-2 nonies : autoliquidation dans la sous-traitance de travaux de construction ; CGI art. 242 nonies A de l'annexe II : mention « Autoliquidation ».
- BOFiP, TVA – Redevable – autoliquidation dans le secteur de la sous-traitance du BTP (champ des travaux, exclusion du nettoyage courant, exigibilité) (*référence précise à vérifier*).
- CE, 24/02/2026, n° 497507 (*selon la fiche de recherche ; à vérifier*).
- Code du travail art. L. 8222-1 et suivants, D. 8222-5 ; Code de la sécurité sociale art. L. 243-15 : obligation de vigilance, seuil de 5 000 € HT.
- Loi n° 75-1334 du 31 décembre 1975 relative à la sous-traitance.
- CGI art. 289 : facture électronique, refus via la plateforme.
