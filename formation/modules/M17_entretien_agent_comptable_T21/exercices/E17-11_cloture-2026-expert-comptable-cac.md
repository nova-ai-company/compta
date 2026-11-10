# E17-11 — Clôture au 31/12/2026 avec l'expert-comptable et le commissaire aux comptes
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★☆ | **Durée estimée :** 60 min | **Thèmes :** factures non parvenues, charges constatées d'avance, subvention à recevoir, congés payés par service, indemnités de départ à la retraite, subvention d'investissement et quote-part virée au résultat, fonds dédiés, dossier de travail, justificatifs pour le commissaire aux comptes

**Corner case :** oui — l'indemnité de départ de Mme Roux n'est plus un simple « engagement » mais une **dette certaine**, alors que l'engagement de retraite des autres salariés reste en annexe

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **30-EMPLOI** | Section analytique de l'emploi accompagné. Le dispositif qui aide 40 personnes à trouver et garder un emploi. Financé par l'ARS, l'AGEFIPH et le FIPHFP. |
    | **40-HABITAT** | Section analytique de l'habitat inclusif. « La Maison partagée » (6 habitants), financée par le Département (aide à la vie partagée). |
    | **50-PAIRS** | Section analytique du projet « Pairs et voix ». Projet expérimental de pair-aidance et d'autoreprésentation, financé par une fondation et la Région. |
    | **AGEFIPH** | Association de gestion du fonds pour l'insertion professionnelle des personnes handicapées. Finance l'emploi des personnes handicapées dans le secteur privé (ex. : cofinance le dispositif d'emploi accompagné). |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CCA** | Charges constatées d'avance — ou compte courant d'associé. Deux sens selon le contexte : (1) clôture : charge payée en N mais qui concerne N+1 (compte 486) ; (2) financement : argent prêté par un associé à sa société (compte 455). |
    | **CNR** | Crédits non reconductibles. Financement ponctuel accordé par l'ARS pour une dépense exceptionnelle (remplacement, véhicule). Il n'est pas renouvelé l'année suivante. |
    | **FNP** | Factures non parvenues. À la clôture : charges de l'année dont la facture n'est pas encore arrivée. On les enregistre quand même (compte 408) pour que l'année supporte ses vraies charges. |
    | **HT** | Hors taxes. Montant sans la TVA. C'est le montant HT qui va en charge ou en produit (sauf si la TVA n'est pas récupérable). |
    | **IDR** | Indemnités de départ à la retraite. Indemnités dues aux salariés partant en retraite ; un engagement que l'on peut provisionner. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 131** | Subventions d'investissement reçues. Subvention qui finance un bien durable (véhicule, ordinateur). |
    | **Compte 194** | Fonds dédiés sur subventions. Subvention reçue pour un projet précis, pas encore dépensée à la clôture (numéro à vérifier dans le plan de l'association). |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 616** | Primes d'assurances. Assurance des locaux, des véhicules, responsabilité civile. Pas de TVA. |
    | **charges constatées d'avance** | Dépense payée d'avance (CCA). Payée cette année mais concerne l'année suivante : on la retire des charges au 31/12 (compte 486). |
    | **code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **crédits non reconductibles** | Financement ponctuel (CNR). Somme accordée une seule fois par l'ARS pour une dépense exceptionnelle ; elle n'est pas renouvelée l'année suivante. |
    | **emploi accompagné** | Dispositif d'aide vers et dans l'emploi. Un conseiller accompagne la personne et l'employeur, dans une entreprise ordinaire, aussi longtemps que nécessaire. |
    | **extourner** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **fonds dédiés** | Subvention affectée pas encore dépensée. Argent reçu pour un projet précis et pas encore utilisé au 31/12. On le met de côté (compte 689 → 19x) pour le dépenser l'année suivante sur ce projet. |
    | **quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes et chiffres fictifs. Relisez la [fiche de l'association](../../M16_comptabilite_analytique_association/fiche_association_Cap_Horizons_21.md), § 1 (les personnes) et § 3.1 (comptes propres au secteur).*

!!! abstract "En clair"
    La clôture, c'est faire en sorte que les comptes de 2026 contiennent **toutes** les charges et **tous** les produits de 2026, et **seulement** eux. Dans une association médico-sociale, on ajoute deux sujets propres au secteur : les **subventions** (à recevoir, à étaler, à reporter en fonds dédiés) et l'**analytique** (chaque écriture doit aller dans le bon service, car chaque financeur lira ses propres chiffres). Vous préparez le travail ; Hélène Ferrand (expert-comptable) le révise ; M. Garnier (commissaire aux comptes, CAC) le contrôle et certifie les comptes.

## La mise en situation

On se place le **15 janvier 2027**. Hélène Ferrand vous a envoyé son planning : « Je passe le **2 février** pour la révision. M. Garnier commence son audit final le **1er mars**. Merci de me préparer les écritures d'inventaire et le **dossier de travail**, et de préparer pour M. Garnier la liste des justificatifs qu'il demande chaque année. »

Rappels : exercice du 01/01 au 31/12 ; l'association **ne récupère pas la TVA** (toutes les charges sont comptées TTC) ; les écritures d'inventaire 2025 (FNP, CCA, congés payés) ont été **extournées le 01/01/2026**.

## Les pièces

**Information 1 — Commissaire aux comptes**
```
Lettre de mission – Audit Rhodanien (fictif) – exercice 2026
Honoraires : 8 000,00 € HT + TVA 20 % = 9 600,00 € TTC
Acompte facturé et comptabilisé en octobre 2026 : 3 840,00 € TTC
Le solde sera facturé à la remise du rapport (juin 2027).
```

**Information 2 — Électricité des locaux de Valence**
```
Facture bimestrielle novembre-décembre 2026 attendue fin janvier 2027.
Estimation à partir des relevés : 1 860,00 € TTC.
```

**Information 3 — Assurance multirisque des locaux**
```
Prime annuelle du 01/04/2026 au 31/03/2027 : 7 200,00 € (taxe comprise),
comptabilisée en totalité en 616 en avril 2026.
```

**Information 4 — Loyer**
```
Loyer et charges de janvier 2027 des locaux de Valence : 6 200,00 €,
facture reçue et payée le 28/12/2026, comptabilisée en 6132 en décembre 2026.
```

**Information 5 — AGEFIPH, emploi accompagné**
```
Convention 2026 : 36 000,00 €. Versé en 2026 : 28 800,00 € (80 %).
Solde de 7 200,00 € versé après réception du bilan de l'action.
L'objectif (40 personnes accompagnées) est atteint au 31/12/2026.
Mme Roux comptabilisait cette subvention en 74 à chaque encaissement
(débit 512 / crédit 74), seulement.
```

**Information 6 — Congés payés acquis et non pris au 31/12/2026 (état du service paie de l'expert-comptable)**

| Service | Congés payés bruts restant dus |
|---|---|
| 01-SIEGE | 9 800,00 € |
| 10-SESSAD | 58 400,00 € |
| 20-SAVS | 31 200,00 € |
| 30-EMPLOI | 12 600,00 € |
| 40-HABITAT | 3 800,00 € |
| **Total** | **115 800,00 €** |

Taux de charges patronales à appliquer : **42 %** (*valeur à vérifier chaque année*). Au 31/12/2025, la dette de congés payés était de 109 400,00 € (charges comprises : 155 348,00 €), extournée le 01/01/2026.

**Information 7 — Départs à la retraite**
```
a) Attestation de l'actuaire (fictive) : engagement de l'association en
   indemnités de départ à la retraite (IDR) au 31/12/2026 : 186 000,00 €
   (171 500,00 € au 31/12/2025). Méthode suivie depuis toujours par
   l'association : engagement mentionné en annexe, non provisionné.
b) Mme Roux (comptable, section 01-SIEGE) part à la retraite le 31/12/2026.
   Indemnité de départ volontaire à la retraite calculée par le service paie :
   7 850,00 € brut ; cotisations patronales : 3 297,00 €.
   Elle sera payée avec la paie de janvier 2027.
```

**Information 8 — Véhicule d'occasion du SESSAD**
```
Acheté le 01/07/2026 : 12 500,00 € TTC, durée d'amortissement 5 ans (linéaire).
Financé en totalité par des crédits non reconductibles (CNR) de l'ARS
notifiés « pour l'acquisition d'un véhicule ». Encaissés en septembre 2026
et comptabilisés : débit 512 / crédit 131 « Subventions d'investissement ».
Aucune écriture d'amortissement n'a encore été passée.
```

**Information 9 — Projet « Pairs et voix » (section 50-PAIRS)**
```
Subvention affectée de la Fondation Lumen (fictive), tranche 2026 : 40 000,00 €,
comptabilisée en 74.
Fonds dédiés au 31/12/2025 (compte 194) : 6 200,00 €, pas encore repris.
Dépenses du projet en 2026 : 31 500,00 €.
```

## Travail à faire

1. Pour chaque information, dites en une phrase **quel principe** s'applique et **quel service** (code analytique) est concerné.
2. Calculez les montants et passez toutes les **écritures d'inventaire au 31/12/2026** (avec le code analytique).
3. Information 7 : expliquez simplement la différence entre une **provision**, une **dette** et un **engagement mentionné en annexe**. Faut-il une écriture pour les 186 000,00 € ? Pour Mme Roux ?
4. Information 8 : expliquez pourquoi on « étale » la subvention d'investissement. Quelle question faut-il poser à l'expert-comptable et à l'ARS sur le traitement des CNR ?
5. Calculez l'**impact** de ces écritures sur le résultat 2026.
6. Listez les écritures à **extourner** au 01/01/2027.
7. Préparez le sommaire du **dossier de travail** pour Hélène Ferrand.
8. Préparez la **liste des justificatifs** à remettre à M. Garnier (CAC).

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E17-11_corrige.md)
