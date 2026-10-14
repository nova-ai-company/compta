# Corrigé E09-02 — Les charges constatées d'avance du Petit Zinc au 30/06/2026

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-02](../exercices/E09-02_cca-le-petit-zinc.md)

## 1. Analyse

**Le compte 486 « figé » :** le solde de 4 210 € correspond **exactement** aux CCA constatées au 30/06/2025. Une CCA doit être **extournée au 1er jour de l'exercice suivant** (01/07/2025) : la charge revient alors dans l'exercice qu'elle concerne. Comme rien n'a été fait, **4 210 € de charges de l'exercice 2025-2026 n'ont jamais été comptabilisées**, et l'actif est surévalué d'autant. C'est un oubli d'extourne de l'exercice en cours, pas une erreur d'un exercice antérieur : on le corrige simplement dans l'exercice.

**Les pièces :**

| Pièce | Période couverte | Part après le 30/06/2026 | CCA ? |
|---|---|---|---|
| 1 Assurance | 01/04/2026 – 31/03/2027 | 9 mois sur 12 | **Oui**, sur le **montant total payé** (taxe d'assurance non récupérable incluse : c'est le coût de la charge) |
| 2 Loyer | 01/06/2026 – 31/08/2026 | 2 mois sur 3 | **Oui**, sur le **HT** (la TVA a été déduite à la facture) |
| 3 Logiciel | 01/02/2026 – 31/01/2027 | 7 mois sur 12 | **Oui**, sur le HT |
| 4 Terrasse | 01/01/2026 – 31/12/2026 | 6 mois sur 12 | **Oui** (pas de TVA : redevance publique) |
| 5 Entretien hottes | 01/01 – 30/06/2026 (terme échu) | 0 | **Non** : la prestation est entièrement réalisée sur l'exercice |
| 6 Vins | Biens livrés, stockables | — | **Non** : ce n'est pas une CCA, c'est du **stock** |

**La question de Clara sur le vin :** des marchandises achetées et non vendues à la clôture ne sont pas une charge « d'avance » : elles figurent dans le **stock final** (inventaire de 7 850 €), via la variation de stock (6037). Les passer en CCA ferait doublon avec l'inventaire, puisque la livraison du 26/06 y figure déjà.

## 2. Calculs

| Pièce | Base | Prorata | CCA |
|---|---|---|---|
| 1 Assurance | 4 860,00 € (TTC = coût) | 9/12 | **3 645,00 €** |
| 2 Loyer | 9 600,00 € HT | 2/3 | **6 400,00 €** |
| 3 Logiciel | 1 440,00 € HT | 7/12 | **840,00 €** |
| 4 Terrasse | 2 880,00 € | 6/12 | **1 440,00 €** |
| **Total** | | | **12 325,00 €** |

Vérification : 4 860 × 9/12 = 3 645 ; 9 600 × 2/3 = 6 400 ; 1 440 × 7/12 = 840 ; 2 880 × 6/12 = 1 440 ; total 12 325,00 €.

**Impact sur le résultat 2025-2026 :**
- extourne oubliée : **– 4 210,00 €** ;
- CCA au 30/06/2026 : **+ 12 325,00 €** ;
- **impact net : + 8 115,00 €** (par rapport à la balance avant inventaire).

**Solde du 486 après inventaire :** 4 210 – 4 210 + 12 325 = **12 325,00 €**.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/06/2026 | OD | 616 | Primes d'assurance | Extourne CCA 30/06/2025 oubliée | 3 240,00 | |
| 30/06/2026 | OD | 651 | Redevances pour logiciels | Extourne CCA 30/06/2025 oubliée | 970,00 | |
| 30/06/2026 | OD | 486 | Charges constatées d'avance | Extourne CCA 30/06/2025 oubliée | | 4 210,00 |
| 30/06/2026 | OD | 486 | Charges constatées d'avance | CCA au 30/06/2026 | 12 325,00 | |
| 30/06/2026 | OD | 616 | Primes d'assurance | CCA assurance MRP 9/12 | | 3 645,00 |
| 30/06/2026 | OD | 6132 | Locations immobilières | CCA loyer juillet-août | | 6 400,00 |
| 30/06/2026 | OD | 651 | Redevances pour logiciels | CCA CaissePro 7/12 | | 840,00 |
| 30/06/2026 | OD | 6132 | Locations immobilières (*redevance d'occupation du domaine public*) | CCA terrasse 6/12 | | 1 440,00 |
| | | | | **Totaux** | **16 535,00** | **16 535,00** |

Au **01/07/2026**, il faut extourner la CCA de 12 325 € (D 616 3 645 / D 6132 7 840 / D 651 840 / C 486 12 325). Paramétrez l'extourne automatique dans le logiciel pour que l'oubli ne se reproduise pas.

*La redevance de terrasse peut aussi être suivie dans un sous-compte dédié (ex. 6132x « redevance domaine public ») pour la lisibilité ; ce n'est pas un impôt (pas de 63x).*

## 4. Points d'attention / pièges

- **Ne jamais mettre de TVA dans une CCA.** Pour le loyer, la base est le HT (9 600 €). Pour l'assurance, en revanche, la taxe sur les conventions d'assurance n'est pas récupérable : elle fait partie du coût, donc la base est le montant total.
- **Prorata en mois** lorsque les périodes commencent le 1er du mois ; en jours sinon.
- **Pièce 5 (terme échu) :** la facture du 30/06 couvre le semestre écoulé. Il n'y a ni CCA ni FNP. Si la facture était arrivée en juillet, il aurait fallu une **FNP**.
- **Le vin n'est pas une CCA :** c'est un bien stockable. Il passe par l'inventaire. Inscrire 4 200 € en CCA **et** dans le stock surévaluerait le résultat de 4 200 €.
- **Contrôle d'ouverture :** une CCA qui a exactement le montant de l'an dernier est le signe d'une extourne oubliée. C'est le premier contrôle à faire en révision.
- **Seuil de signification :** au Petit Zinc (820 k€ de CA), on ne passe pas de CCA pour un abonnement de 9,90 €/mois. On se concentre sur les montants significatifs et récurrents.

## 5. Ce qu'un senior ferait en plus

- **Feuille de travail CCA permanente** dans le dossier : liste des contrats récurrents (assurance, loyer, logiciel, terrasse, licence IV si redevance, abonnements plateformes de réservation) avec leurs dates d'échéance. L'an prochain, il suffira de la mettre à jour.
- **Contrôle de cohérence :** le loyer annuel attendu est de 9 600 × 4 = 38 400 € HT. Or le 6132 affiche 47 040 € avant inventaire, soit après CCA 47 040 – 7 840 = 39 200 €. L'écart de 800 € s'explique-t-il par une indexation (ILC), par des charges locatives ou par la terrasse ? À justifier par le **bail et ses avenants**.
- **Rappel à Clara sur la facturation électronique :** depuis le 01/09/2026, la société doit **recevoir** ses factures fournisseurs au format électronique via une plateforme agréée. Une photo WhatsApp n'est pas une facture électronique. Il faut vérifier que les fournisseurs (cave, CaissePro) adressent bien leurs factures via la PA.

**Réponse écrite à Clara :**
> « Bonjour Clara, merci pour les factures. Pour le vin : non, ce n'est pas une charge "d'avance". Les bouteilles non vendues au 30 juin font partie de votre stock, et elles sont déjà dans l'inventaire de Hugo (7 850 €). Elles ne pèsent donc pas sur le résultat de l'exercice. En revanche, nous avons isolé 12 325 € de dépenses payées pour la période postérieure au 30 juin (assurance, loyer d'été, logiciel de caisse, terrasse), qui seront imputées sur l'exercice 2026-2027. Nous avons aussi corrigé une écriture de l'an dernier qui n'avait pas été soldée. Bonne soirée ! »

## 6. Références

- Code de commerce, art. L. 123-13 (inventaire) et principe d'indépendance des exercices.
- CGI, art. 38, 2 et 39, 1 (rattachement des charges à l'exercice) ; art. 271 (TVA déductible sur facture).
- PCG : compte 486 « Charges constatées d'avance » ; comptes 603x (variation des stocks).
- CGI, art. 289 bis et textes sur la généralisation de la facturation électronique (réception obligatoire au 01/09/2026).
