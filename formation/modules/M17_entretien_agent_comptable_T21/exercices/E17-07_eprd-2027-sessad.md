# E17-07 — Préparer l'EPRD 2027 du SESSAD à partir de la dotation notifiée
**Client :** Cap Horizons 21 (association fictive) | **Difficulté :** ★★★ | **Durée estimée :** 60 min | **Thèmes :** EPRD, dotation globale, taux d'actualisation, crédits non reconductibles, groupes fonctionnels, GVT, frais de siège, équilibre « par la recette », CAF, plan de financement, trésorerie

**Corner case :** oui — le premier projet de budget dépasse la dotation : il faut trouver des leviers **sans toucher** aux crédits non reconductibles, qui sont « fléchés »

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **BFR** | Besoin en fonds de roulement. Argent immobilisé dans le cycle d'exploitation (stocks + créances clients − dettes fournisseurs). Plus il est élevé, plus l'entreprise a besoin de trésorerie. |
    | **CAF** | Capacité d'autofinancement. Trésorerie dégagée par l'activité (résultat + amortissements et provisions). Sert à rembourser les emprunts et investir. |
    | **CASF** | Code de l'action sociale et des familles. Le code qui encadre les ESSMS : autorisation, tarification, budgets, frais de siège. |
    | **CDD** | Contrat à durée déterminée. Contrat de travail avec une date de fin ; donne souvent droit à une indemnité de fin de contrat. |
    | **CNR** | Crédits non reconductibles. Financement ponctuel accordé par l'ARS pour une dépense exceptionnelle (remplacement, véhicule). Il n'est pas renouvelé l'année suivante. |
    | **CPOM** | Contrat pluriannuel d'objectifs et de moyens. Contrat de 5 ans entre une association et l'ARS et/ou le Département : objectifs, moyens, et budget présenté en EPRD. |
    | **EPRD** | État des prévisions de recettes et de dépenses. Budget prévisionnel des gestionnaires sous CPOM. Il part de la ressource notifiée par le financeur (« budget par la recette »). Dépôt en général au 30 avril (à vérifier chaque année). |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **FINESS** | Fichier national des établissements sanitaires et sociaux. Numéro d'identification de chaque établissement ou service médico-social (SESSAD, SAVS…). Il figure sur l'EPRD, l'ERRD et les notifications de l'ARS. |
    | **GVT** | Glissement vieillesse technicité. Hausse « automatique » de la masse salariale due à l'ancienneté et aux promotions. À prévoir dans tout budget de personnel. |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **Compte 777** | Quote-part des subventions d'investissement virée au résultat. Chaque année, la même part que l'amortissement du bien financé. |
    | **Compte 10682** | Excédents affectés à l'investissement. Excédent d'un service mis de côté pour financer un investissement (véhicule, travaux). Plan des ESSMS. |
    | **besoin en fonds de roulement** | Argent bloqué par le décalage des paiements. Créances (subventions à recevoir) moins dettes à court terme. |
    | **crédits non reconductibles** | Financement ponctuel (CNR). Somme accordée une seule fois par l'ARS pour une dépense exceptionnelle ; elle n'est pas renouvelée l'année suivante. |
    | **dotation globale** | Somme annuelle fixée par le financeur. L'ARS ou le Département verse au service un montant pour l'année, souvent par douzièmes (1/12 chaque mois). |
    | **frais de siège** | La part du coût du siège payée par chaque service. Le siège (direction, compta, RH) n'a pas de financement propre : chaque service en paie une part, au taux autorisé par le financeur (ex. : 4,5 %). |
    | **groupes fonctionnels** | Les 3 familles de dépenses d'un ESSMS. Groupe I : exploitation courante. Groupe II : personnel. Groupe III : structure (loyers, amortissements, frais de siège). |
    | **Indemnités kilométriques** | Remboursement des km faits avec sa voiture. Barème en € par km, selon la puissance du véhicule (CV). Compte 6251. |
    | **Quote-part** | La part qui revient à chacun. Ex. : la quote-part de loyer du SAVS = loyer × m² du SAVS ÷ m² total. |
    | **taxe sur les salaires** | Impôt des employeurs sans TVA. L'association, non soumise à la TVA, paie cet impôt sur les salaires bruts ; un abattement annuel s'applique aux associations. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes et chiffres fictifs. Relisez la [fiche de l'association](../../M16_comptabilite_analytique_association/fiche_association_Cap_Horizons_21.md) avant de commencer.*

!!! abstract "En clair"
    L'**EPRD** (état des prévisions de recettes et de dépenses) est le budget d'un établissement médico-social sous **CPOM** (contrat pluriannuel d'objectifs et de moyens). Sa logique est simple : **l'ARS (Agence régionale de santé) annonce d'abord combien elle donne**, puis l'association construit des dépenses qui tiennent dans cette enveloppe. On parle de budget « **par la recette** ». Dans cet exercice, vous construisez la partie « compte de résultat » du SESSAD, puis la CAF (capacité d'autofinancement), le plan de financement et un résumé de trésorerie.

## La mise en situation

Lors de votre entretien, Nathalie Berthier, directrice générale, vous propose un cas pratique : « Imaginez que nous sommes le **18 mai 2027**. L'ARS vient de nous notifier la dotation 2027 du SESSAD. Nous avons **30 jours** pour déposer l'EPRD (*délai à vérifier chaque année dans la notification et dans le CASF*). Karim Belkacem, le chef de service, m'a envoyé ses besoins. Pouvez-vous me préparer le compte de résultat prévisionnel du SESSAD, me dire s'il est équilibré et, sinon, me proposer des solutions ? »

Elle ajoute : « Je ne vous demande pas de remplir le fichier officiel de l'ARS. Je veux voir si vous comprenez la logique. »

## Les pièces

**Pièce 1 — Extrait de la notification de l'ARS (fictive)**
```
ARS – Direction de l'autonomie – Délégation départementale de la Drôme
Objet : notification de la dotation globale 2027
Établissement : SESSAD Cap Horizons 21 – 45 places – FINESS (fictif) 26 000 2121

Base reconductible 2026 ............................ 1 148 000,00 €
Taux d'actualisation 2027 .......................... 1,10 %
Crédits non reconductibles (CNR) 2027 :
  - formation des équipes à la communication alternative et
    augmentée (action ponctuelle, non reconductible) .. 12 000,00 €
Les CNR sont fléchés : ils ne peuvent financer que l'action indiquée.
Versement : par fractions mensuelles.
```
*Le taux d'actualisation est fictif : il change chaque année (valeur à vérifier chaque année).*

**Pièce 2 — Autres recettes prévues pour 2027 (estimation de Mme Roux, l'ancienne comptable)**

| Recette | Groupe | Montant |
|---|---|---|
| Interventions de sensibilisation facturées à des écoles et crèches | II | 4 800,00 € |
| Intérêts du livret de trésorerie | III | 1 200,00 € |
| Quote-part de subvention d'investissement virée au résultat (compte 777, produit non encaissé) | III | 2 500,00 € |

**Pièce 3 — Tableau des effectifs du SESSAD (14,2 ETP) et coûts moyens chargés 2026**

*ETP : équivalent temps plein. Coût moyen chargé : salaire brut + cotisations patronales + taxe sur les salaires, pour 1 ETP sur un an.*

| Fonction | ETP | Coût moyen chargé 2026 par ETP |
|---|---|---|
| Chef de service | 1,0 | 84 000,00 € |
| Psychologue | 1,0 | 70 000,00 € |
| Éducateurs spécialisés | 6,0 | 60 000,00 € |
| Paramédicaux (orthophoniste, psychomotricienne) | 2,2 | 64 000,00 € |
| Secrétaire | 1,0 | 47 000,00 € |
| Médecin | 0,2 | 150 000,00 € |
| Assistante sociale | 0,8 | 58 000,00 € |
| Moniteurs-éducateurs | 2,0 | 52 000,00 € |

Hypothèse de l'expert-comptable : **GVT 2027 = + 1,3 %** sur la masse salariale (*GVT : glissement vieillesse technicité, c'est-à-dire la hausse automatique des salaires due à l'ancienneté et aux promotions ; valeur à vérifier chaque année*).

**Pièce 4 — Mail de Karim Belkacem, chef de service SESSAD**
```
De : Karim Belkacem
À : Nathalie Berthier ; agent comptable
Objet : besoins 2027

- Remplacements (congés maladie, maternité) : prévoir 28 000 € de personnel
  extérieur / CDD de remplacement, comme en 2026.
- Formation communication alternative : 12 000 € (c'est le CNR).
- Je demande la création d'un demi-poste d'éducateur spécialisé
  (0,5 ETP) dès le 1er janvier : la liste d'attente atteint 19 enfants.
- Achat d'un véhicule pour remplacer la Clio de 2016 :
  24 000 € TTC, livraison le 1er avril 2027, durée d'amortissement 5 ans.
```

**Pièce 5 — Autres charges prévues pour 2027**

| Charge | Groupe | Montant |
|---|---|---|
| Carburant (cartes carburant) | I | 25 000,00 € |
| Fournitures et matériel éducatifs | I | 10 000,00 € |
| Fournitures administratives | I | 4 000,00 € |
| Alimentation des ateliers | I | 2 000,00 € |
| Indemnités kilométriques des professionnels | I | 37 500,00 € |
| Téléphone, internet | I | 7 500,00 € |
| Loyers et charges (quote-part de Valence + antenne de Romans-sur-Isère) | III | 54 000,00 € |
| Entretien et maintenance | III | 8 500,00 € |
| Assurances | III | 9 800,00 € |
| Dotations aux amortissements des biens existants | III | 18 400,00 € |
| Honoraires (quote-part expert-comptable et commissaire aux comptes) | III | 9 200,00 € |
| Intérêts de l'emprunt (travaux 2022) | III | 900,00 € |

Autres données :
- Frais de siège autorisés : **4,5 %** des charges brutes du SESSAD **hors frais de siège** (taux fictif, fixé par l'autorité).
- Remboursement du capital de l'emprunt en 2027 : **7 500,00 €**.
- Trésorerie du SESSAD au 01/01/2027 : **185 000,00 €**. Le BFR (besoin en fonds de roulement) devrait augmenter de **3 000,00 €** en 2027.
- Au bilan, le compte **10682** « Excédents affectés à l'investissement » du SESSAD s'élève à **13 750,00 €** (affectation du résultat 2025, voir E17-08).

## Travail à faire

1. Expliquez en quatre ou cinq phrases simples ce que veut dire « un budget **par la recette** » et pourquoi l'EPRD fonctionne ainsi.
2. Calculez la dotation 2027 et le **total des recettes** du SESSAD, classées par groupe fonctionnel.
3. Calculez la **masse salariale 2027** (effectif actuel) avec le GVT, puis le coût en année pleine du demi-poste demandé.
4. Construisez le **premier projet** de compte de résultat prévisionnel par groupes fonctionnels (avec le demi-poste au 1er janvier et l'amortissement du nouveau véhicule). Calculez les frais de siège. Le budget est-il équilibré ?
5. Proposez des **leviers** pour revenir à l'équilibre. Dites lesquels sont interdits ou risqués. Présentez le **projet final** et son résultat, en retenant : demi-poste créé au **1er septembre 2027** et remplacements ramenés à **24 000,00 €**.
6. Calculez la **CAF** prévisionnelle (méthode simplifiée), puis présentez le **plan de financement** 2027 (véhicule + remboursement d'emprunt).
7. Présentez un **résumé du tableau de trésorerie** 2027 et le nombre de **jours de charges** couverts par la trésorerie de fin d'année.
8. Y a-t-il une écriture comptable à passer ? Expliquez.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E17-07_corrige.md)
