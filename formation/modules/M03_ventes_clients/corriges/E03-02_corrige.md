# Corrigé E03-02 — Situations de travaux, retenue de garantie et sous-traitance

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E03-02](../exercices/E03-02_situation-travaux-btp.md)

## 1. Analyse

**a) Ce qu'est une situation de travaux.** C'est une facture d'acompte sur le prix du marché, calculée sur l'avancement cumulé : cumul exécuté – cumul déjà facturé. Le produit (704) est le **montant HT des travaux exécutés sur la période**, soit 186 000 € pour la situation n° 4, quelle que soit la retenue de garantie.

**b) La retenue de garantie n'est pas une réduction de prix.** Le maître d'ouvrage conserve 5 % du TTC jusqu'à la levée des réserves (au plus tard un an après la réception), sauf caution bancaire. Pour l'entreprise, c'est une **créance** (compte **4117**), payable plus tard. Nadia a comptabilisé le **net à payer** en 411 et l'a « reconstitué » en HT + TVA : elle a donc **sous-évalué le CA** (176 700 € au lieu de 186 000 €) et oublié la créance de retenue.

**c) Les travaux immobiliers sont des prestations de services : TVA exigible à l'encaissement** (art. 269-2-c CGI), faute d'option pour les débits. À la facturation, la TVA va en **44574 « TVA collectée en attente »** ; elle ne passe en 44571 (et sur la CA3) qu'au moment du paiement, au prorata de ce qui est encaissé. La TVA afférente à la retenue de garantie ne sera exigible qu'à l'encaissement de la retenue.

**d) La sous-traitance relève de l'autoliquidation** (art. 283-2 nonies CGI). Lorsque Bâtisseurs du Sud intervient comme **sous-traitant** d'une entreprise principale pour des travaux de construction (contrat de sous-traitance au sens de la loi de 1975), c'est l'**entreprise principale qui autoliquide** la TVA. Le sous-traitant facture **HT, sans TVA**, avec la mention « Autoliquidation ». Le client a raison de refuser de payer la TVA.

**Anomalies relevées :**

| N° | Pièce | Anomalie | Conséquence |
|---|---|---|---|
| 1 | P2 | TVA 20 % facturée en sous-traitance | Facture irrégulière ; et la TVA mentionnée à tort sur une facture est due **du seul fait de sa facturation** (art. 283-3 CGI) tant que la facture n'est pas rectifiée |
| 2 | P2 | Mention « Autoliquidation » absente | Mention obligatoire |
| 3 | P2 | Pas d'indemnité de 40 € ni de taux de pénalités de retard | Mentions obligatoires B2B (art. L. 441-9 C. com.) |
| 4 | P2 | Nature de l'opération non précisée | Nouvelle mention (facturation électronique) — à intégrer dès maintenant |
| 5 | P3 | 704 = net après retenue, pour les deux factures | CA minoré de 9 300 € (A) + 2 425 € (B) |
| 6 | P3 | Retenue de garantie non comptabilisée (4117) | Créance absente du bilan |
| 7 | P3 | TVA des travaux en 44571 au lieu de 44574 | TVA déclarée avant son exigibilité (paiement anticipé de 35 340 € à l'État) |
| 8 | P3 | TVA collectée sur la sous-traitance | TVA non due (après rectification) |

## 2. Calculs

**Situation n° 4 (marché principal)**

| Élément | Calcul | Montant |
|---|---|---|
| Cumul exécuté HT | 1 240 000 × 46 % | 570 400,00 |
| Cumul déjà facturé | 1 240 000 × 31 % | 384 400,00 |
| HT de la situation | 570 400 – 384 400 | **186 000,00** |
| TVA 20 % | 186 000 × 20 % | 37 200,00 |
| TTC | | 223 200,00 |
| Retenue de garantie | 223 200 × 5 % | **11 160,00** |
| Net à payer | | 212 040,00 |
| TVA exigible au paiement du net | 212 040 × 20/120 | **35 340,00** |
| TVA restant en attente (sur la retenue) | 11 160 × 20/120 | **1 860,00** |

Contrôle : 35 340 + 1 860 = 37 200. ✔

**Sous-traitance (facture correcte)**

| Élément | Montant |
|---|---|
| Travaux HT | 48 500,00 |
| TVA | néant (autoliquidation) |
| Retenue de garantie 5 % (sur le montant facturé, soit le HT) | 2 425,00 |
| Net à payer | **46 075,00** |

**Explication pour Karim (écart de CA)** : Nadia a enregistré 176 700 + 46 075 = 222 775 € de CA ; le CA réel est 186 000 + 48 500 = **234 500 €**. Écart : **11 725 €** = les retenues de garantie hors taxes (9 300 + 2 425). Le CA n'est pas plus bas : il a été mal comptabilisé.

**Reste à facturer sur le marché principal** : 1 240 000 – 570 400 = **669 600 € HT** (54 %).

## 3. Écritures comptables

**a) Extourne des écritures de Nadia (30/09/2026)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 704 | Travaux | Extourne SIT-0412 erronée | 176 700,00 | |
| 30/09/2026 | OD | 44571 | TVA collectée | Extourne SIT-0412 erronée | 35 340,00 | |
| 30/09/2026 | OD | 411SCCV | Client SCCV Les Terrasses | Extourne SIT-0412 erronée | | 212 040,00 |
| 30/09/2026 | OD | 704 | Travaux | Extourne SIT-0413 erronée | 46 075,00 | |
| 30/09/2026 | OD | 44571 | TVA collectée | Extourne SIT-0413 erronée | 9 215,00 | |
| 30/09/2026 | OD | 411RCG | Client Rhône Constructions | Extourne SIT-0413 erronée | | 55 290,00 |
| | | | | **Totaux (a)** | **267 330,00** | **267 330,00** |

**b) Écritures correctes**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | VT | 411SCCV | Client SCCV Les Terrasses | SIT-2026-0412 – net à payer | 212 040,00 | |
| 30/09/2026 | VT | 4117 | Clients – retenues de garantie | SIT-2026-0412 – RG 5 % | 11 160,00 | |
| 30/09/2026 | VT | 704 | Travaux | SIT-2026-0412 – situation 4 | | 186 000,00 |
| 30/09/2026 | VT | 44574 | TVA collectée en attente (encaissements) | SIT-2026-0412 | | 37 200,00 |
| 30/09/2026 | VT | 411RCG | Client Rhône Constructions | Facture rectificative SIT-0413 (autoliquidation) | 46 075,00 | |
| 30/09/2026 | VT | 4117 | Clients – retenues de garantie | RG 5 % sous-traitance | 2 425,00 | |
| 30/09/2026 | VT | 704 | Travaux | Sous-traitance situation 2 | | 48 500,00 |
| 20/10/2026 | BQ | 512 | Banque | Encaissement SIT-2026-0412 | 212 040,00 | |
| 20/10/2026 | BQ | 411SCCV | Client SCCV Les Terrasses | Encaissement SIT-2026-0412 | | 212 040,00 |
| 20/10/2026 | OD | 44574 | TVA collectée en attente | TVA exigible sur encaissement | 35 340,00 | |
| 20/10/2026 | OD | 44571 | TVA collectée | TVA exigible sur encaissement | | 35 340,00 |
| | | | | **Totaux (b)** | **519 080,00** | **519 080,00** |

En pratique, le logiciel de Nadia passera l'avoir n° AV-2026-xxx (annulation de SIT-0413) puis la nouvelle facture ; l'effet comptable net est celui présenté ci-dessus.

## 4. Points d'attention / pièges

- **Facture déjà envoyée** : on ne la modifie pas, on émet un **avoir d'annulation total** (référençant SIT-2026-0413) puis une **nouvelle facture** HT avec la mention « **Autoliquidation – TVA due par le preneur (art. 283-2 nonies du CGI)** ». Tant que l'avoir n'est pas émis, la TVA de 9 700 € facturée à tort reste due par Bâtisseurs du Sud (art. 283-3 CGI).
- **Mentions de la facture correcte** : numéro, date, SIREN et n° TVA des deux parties, nature « prestation de services – travaux immobiliers », référence du contrat de sous-traitance, montant HT, mention d'autoliquidation, retenue de garantie, échéance, pénalités et indemnité de 40 €.
- **CA3** :
  - situation n° 4 : rien sur la CA3 de **septembre** (TVA non exigible) ; sur la CA3 d'**octobre** (déposée en novembre) : base 176 700 € en ligne A1 et en ligne 08 (TVA 35 340 €) ;
  - retenue de garantie : TVA de 1 860 € déclarée **le mois de son encaissement** (fin 2027 au plus tard si la réception a lieu fin 2026) — base 9 300 € ;
  - sous-traitance : aucune TVA ; le montant HT est déclaré en ligne **E2 « Autres opérations non imposables »** (période de l'encaissement, en cohérence avec l'exigibilité des travaux).
- **Ne pas déduire la retenue du CA** et ne pas la déprécier par principe : elle est encaissée dans la grande majorité des cas. À la clôture, une RG de plus d'un an sans réception signée = point à analyser (litige, réserves non levées).
- **Caution bancaire** : si l'entreprise fournit une caution de la banque, il n'y a pas de retenue (et la commission de caution est une charge financière 627/661).

## 5. Ce qu'un senior ferait en plus

**Pour la clôture du 31/12/2026 (chantier à cheval sur deux exercices)** :
- obtenir de Karim un **état d'avancement technique** au 31/12 (métré, heures, coûts engagés) et le **budget à terminaison** du chantier de Corbas ;
- appliquer la méthode retenue par l'entreprise (avancement ou achèvement — permanence des méthodes) ; avec la méthode à l'avancement, comparer le CA facturé à l'avancement réel → **4181** (facturé en retard) ou **487** (facturé en avance) ;
- si le budget fait apparaître une **perte à terminaison**, la provisionner intégralement (voir M08).

**Contrôle de cohérence 44574** : au 31/12, le solde du 44574 doit correspondre à la TVA incluse dans les créances clients de travaux (411 + 4117) non encaissées. Mettre en place ce contrôle mensuel avec Nadia.

**Mail à Nadia :**
> Bonjour Nadia, merci pour l'envoi. Trois corrections avant la CA3 : (1) la retenue de garantie va en 4117, le CA est le HT de la situation (186 000 €) ; (2) les travaux sont soumis à la TVA à l'encaissement : la TVA va en 44574 et ne sera déclarée qu'en octobre, au paiement ; (3) en sous-traitance, pas de TVA : merci d'émettre un avoir total de SIT-0413 et une nouvelle facture HT avec la mention « Autoliquidation ». Je vous envoie les écritures corrigées. Pour la CA3 de septembre, aucune de ces deux factures ne génère de TVA.

## 6. Références

- CGI : art. 269-2-c (exigibilité à l'encaissement des prestations de services), art. 283-2 nonies (autoliquidation en sous-traitance BTP), art. 283-3 (TVA facturée à tort), art. 242 nonies A ann. II (mentions).
- Loi n° 71-584 du 16 juillet 1971 (retenue de garantie) ; loi n° 75-1334 du 31 décembre 1975 (sous-traitance).
- Code de commerce : art. L. 441-9 et L. 441-10.
- PCG : comptes 704, 4117, 44571, 44574 (subdivision usuelle de 4457 pour la TVA en attente).
- BOFiP : TVA-DECLA (autoliquidation dans le secteur de la construction).
