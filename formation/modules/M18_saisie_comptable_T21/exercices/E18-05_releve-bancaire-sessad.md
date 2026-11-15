# E18-05 — Saisir le relevé bancaire d'octobre du SESSAD et faire le rapprochement
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 15 | **Thèmes :** journal de banque à contrepartie automatique, convention « débit pour les dépenses », FO / LI / SA, dotation ARS, IJSS et prévoyance (6419xxx), carte bancaire sans facture, compte d'attente 4710000, prélèvement rejeté, comptes de liaison, lettrage, état de rapprochement bancaire

**Corner case :** oui — un prélèvement qui appartient au siège est passé sur le compte du SESSAD, un virement de 150,00 € arrive sans que personne sache de qui, et un prélèvement revient impayé

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **ARS** | Agence régionale de santé. Organisme de l'État qui autorise et finance les soins et le médico-social (ex. : la dotation du SESSAD). |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **CAC** | Commissaire aux comptes. Auditeur indépendant qui certifie les comptes de certaines entreprises (au-delà de seuils) et associations. |
    | **CB** | Carte bancaire. Paiement par carte. Les encaissements CB arrivent en banque nets de commission. |
    | **CPAM** | Caisse primaire d'assurance maladie. Verse notamment les indemnités journalières en cas d'arrêt maladie. |
    | **ETP** | Équivalent temps plein. Mesure de l'effectif : un salarié à temps plein = 1 ETP, un mi-temps = 0,5 ETP. Sert souvent de clé de répartition (téléphonie, informatique). |
    | **IBAN** | Numéro de compte bancaire international. Identifiant unique d'un compte bancaire, nécessaire pour un virement. |
    | **IJ** | Indemnités journalières. Voir IJSS : sommes versées par la CPAM pendant un arrêt de travail. |
    | **IJSS** | Indemnités journalières de la Sécurité sociale. Somme versée par la CPAM au salarié en arrêt. Si l'employeur maintient le salaire (subrogation), il les reçoit à sa place. |
    | **IS** | Impôt sur les sociétés — ou, chez Trisomie 21, inter-structures. Impôt sur le bénéfice des sociétés (SAS, SARL…). Taux réduit de 15 % jusqu'à 42 500 € de bénéfice pour les PME, 25 % au-delà. Chez Trisomie 21 France (M18), IS veut dire inter-structures : une opération faite par une structure pour une autre (ex. : facture EDF du siège répartie entre les services), passée par les comptes de liaison 18. |
    | **NDF** | Note de frais. Remboursement à un salarié des dépenses qu'il a avancées pour l'entreprise, avec justificatifs. |
    | **PRLV** | Prélèvement. Abréviation utilisée sur les relevés bancaires. |
    | **RIB** | Relevé d'identité bancaire. Document qui donne les coordonnées bancaires (IBAN, BIC) d'un compte. |
    | **SA** | Société anonyme — ou, chez Trisomie 21, compte de tiers Salarié. Société plus lourde (conseil d'administration), plutôt pour les grandes entreprises. Chez Trisomie 21 France (M18), SA est aussi le préfixe des comptes de tiers des salariés pour leurs notes de frais (ex. : SADURAND), regroupés dans le compte 4248000. |
    | **SEPA** | Espace unique de paiement en euros. Normes européennes de virements et prélèvements en euros. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **VIR** | Virement. Abréviation utilisée sur les relevés bancaires. |
    | **Compte 1840000** | Compte liaison exploit° courante (besoin fonds de roulement) (plan T21). Compte de liaison générique. Dans le dossier M18 : la « Liaison Siège » dans les livres de chaque structure. |
    | **Compte 1849100** | Liaison SESSAD (dossier M18, fictif). Dans les livres du siège : ce que le SESSAD doit au siège (ou l'inverse). Son solde est l'opposé du 1840000 chez le SESSAD. |
    | **Compte 4710000** | Comptes d’attente (plan T21). Compte d'attente : opération non identifiée. À utiliser rarement et à solder avant la clôture. |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 6262000** | Frais de télécommunication (plan T21). Téléphone, internet. |
    | **FOBUREAU26** | Compte fournisseur fournitures de bureau (dossier M18). Fournitures administratives (6062400). |
    | **FOLUDIK** | Compte fournisseur matériel éducatif (dossier M18). Jeux et matériel éducatif du SESSAD (6062500). |
    | **FOORANGE** | Compte fournisseur télécom (dossier M18). Contrat unique de téléphonie et internet facturé au siège, réparti en IS selon les ETP. |
    | **FOTOTALCARTE** | Compte fournisseur carte carburant (dossier M18). Relevé mensuel des cartes carburant des véhicules de service (6062100). |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **LIMOREAUPSY** | Compte libéral : psychomotricien (dossier M18). Séances de psychomotricité du SESSAD (6223222). |
    | **SADURAND** | Compte salarié : Nathalie Durand. Exemple du document T21 : note de frais (kilomètres en 6251000, stylos en 6062400), SADURAND crédité du total. |
    | **SAGIRARD** | Compte salarié : Thomas Girard (dossier M18). Notes de frais d'un éducateur du SESSAD. |
    | **Code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **comptes de liaison** | Compte qui relie le siège et les services. Compte 181 : utilisé quand chaque service a sa propre comptabilité. |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
    | **subrogation** | L'employeur touche les IJSS à la place du salarié. L'association maintient le salaire pendant l'arrêt maladie et reçoit directement les indemnités de la CPAM. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes, sociétés et documents fictifs. Les numéros de comptes viennent du plan comptable T21 France ; les numéros de structures, de banques et de journaux sont ceux de la fiche du dossier M18.*

!!! abstract "En clair"
    Chaque mois, la banque envoie un **relevé** : la liste de tout ce qui est entré et sorti du compte. Votre travail consiste à **recopier chaque ligne dans la comptabilité**, avec le bon compte, puis à vérifier que le solde de la comptabilité et celui de la banque « se parlent ». Ils ne sont presque jamais égaux, et c'est normal : un chèque que vous avez donné n'est pas encore encaissé, un virement est parti le vendredi et arrive le lundi. Le document qui explique la différence s'appelle l'**état de rapprochement bancaire**.

## La mise en situation

Lundi 16 novembre 2026. Vous êtes agente comptable de Cap Horizons 21 depuis quinze jours. Le relevé d'octobre du compte du **SESSAD** est arrivé (export PDF de la banque en ligne). Personne n'a saisi la banque du SESSAD depuis le 30/09 : seules deux opérations d'octobre ont été passées par Mme Roux, votre prédécesseure, avant son départ.

Nathalie Berthier, la directrice, passe la tête par la porte :

> « Le CAC (commissaire aux comptes) vient fin novembre pour l'intérim. Il demandera les rapprochements bancaires de septembre et d'octobre, structure par structure. Commencez par le SESSAD, c'est le plus gros compte. Et regardez ce virement de 150 € : une maman m'a dit qu'elle avait fait un don, je ne sais pas si c'est lié. »

Rappels de la fiche du dossier :

- **Structure** : SES (SESSAD). **Compte bancaire** : **5122000** Crédit Mutuel – SESSAD. **Journal** : **BQSES**, journal de banque « compte courant » à **contrepartie automatique** (le logiciel ajoute seul la ligne 5122000).
- **Code analytique** du SESSAD : **10-SESSAD** (sur les comptes de charges et de produits seulement).
- **Compte de liaison** dans les livres du SESSAD : **1840000** Liaison Siège. Dans les livres du siège, le SESSAD est suivi en **1849100** Liaison SESSAD.
- Le contrat télécom (FOORANGE) est **au nom du siège** : la facture est saisie au siège (SIE), puis répartie entre les structures selon les ETP (équivalents temps plein).

## Les pièces

**Pièce 1 — Relevé de compte n° 10 (extrait reproduit)**

```
CRÉDIT MUTUEL – Agence Valence Victor-Hugo (coordonnées fictives)
Titulaire : ASSOCIATION CAP HORIZONS 21 – SESSAD
IBAN : FR76 1027 8089 0000 0212 2000 0xx (fictif)
Relevé n° 10 – du 01/10/2026 au 31/10/2026
```

| N° | Date opé. | Libellé banque | Débit | Crédit |
|---|---|---|---|---|
| | 30/09 | **Solde créditeur au 30/09/2026** | | **63 214,57** |
| 1 | 01/10 | VIR CAP HORIZONS 21 SIEGE – AVANCE TRESO DOTATION 10/2026 | | 20 000,00 |
| 2 | 02/10 | CHEQUE N° 0004518 | 420,00 | |
| 3 | 05/10 | PRLV SEPA ORANGE – CONTRAT FLOTTE 0148 77 – FACT 09/2026 – RUM CH21-SIE-0007 | 312,48 | |
| 4 | 06/10 | VIR SEPA DUPONT CLAIRE – FACT 2026-09 ORTHOPHONIE | 1 245,00 | |
| 5 | 08/10 | VIR SEPA GIRARD THOMAS – NDF 09/2026 | 86,70 | |
| 6 | 09/10 | CB TOTAL ENERGIES VALENCE SUD 08/10 – CARTE 4970 xxxx 2231 | 62,35 | |
| 7 | 12/10 | VIR CPAM DE LA DROME – IJ SUBROGATION – ASSURE 2 85 xx – DU 07/09 AU 30/09 | | 1 184,62 |
| 8 | 14/10 | VIR ARS AUVERGNE-RHONE-ALPES – DOTATION GLOBALE SESSAD 10/2026 | | 98 000,00 |
| 9 | 15/10 | VIR PREVOYANCE ALPES-RHONE – IJ COMPLEMENTAIRES DOSSIER 2026-0415 | | 2 316,40 |
| 10 | 16/10 | VIR SEPA MOREAU JULIEN – FACT 09/2026 PSYCHOMOTRICITE | 960,00 | |
| 11 | 19/10 | PRLV SEPA TOTALCARTE – RELEVE 09/2026 – RUM TC-55871 | 418,92 | |
| 12 | 20/10 | VIR M OU MME LEROY MARIE-CLAUDE – (sans référence) | | 150,00 |
| 13 | 22/10 | RETOUR PRLV SEPA TOTALCARTE – MOTIF MD01 MANDAT NON VALIDE | | 418,92 |
| 14 | 22/10 | VIR CAP HORIZONS 21 SIEGE – REMB AVANCE + IS 09/2026 | 34 380,00 | |
| 15 | 27/10 | VIR SEPA LUDIK EDUCATION – FACT LE-2026-311 | 537,60 | |
| 16 | 30/10 | FRAIS TENUE DE COMPTE + COTISATION CARTE T4 | 38,50 | |
| | | **Total des mouvements** | **38 461,55** | **122 069,94** |
| | 31/10 | **Solde créditeur au 31/10/2026** | | **146 822,96** |

*Attention au vocabulaire de la banque : sur un relevé, « solde créditeur » veut dire que **la banque vous doit** de l'argent, c'est-à-dire que le compte est positif. Dans **votre** comptabilité, le même compte 5122000 est **débiteur** (c'est un avoir de l'association). Chacun regarde le compte depuis sa place.*

**Pièce 2 — État de rapprochement au 30/09/2026 (fait par Mme Roux)**

```
Compte 5122000 – SESSAD – Rapprochement au 30/09/2026
Solde du relevé au 30/09 (créditeur)                    63 214,57
– Chèque n° 0004518 émis le 28/09 à LIMOREAUPSY,
  non encore débité                                       – 420,00
= Solde comptable 5122000 au 30/09 (débiteur)           62 794,57   ✓
```

**Pièce 3 — Opérations d'octobre déjà saisies dans BQSES (par Mme Roux, avant son départ)**

| Date | Pièce | Compte saisi | Libellé | Montant |
|---|---|---|---|---|
| 29/10 | Chèque n° 0004524 | FOBUREAU26 | Bureau Vallée 26 – fournitures SESSAD – BV-26-8812 – 10/2026 | 64,90 (dépense) |
| 30/10 | Virement émis | SADURAND | Durand – NDF 10/2026 | 142,30 (dépense) |

**Pièce 4 — Factures et notes non lettrées au 30/09/2026 dans les livres du SESSAD**

| Compte de tiers | Pièce | Date | Montant dû |
|---|---|---|---|
| LIDUPONT | Facture 2026-09 orthophonie | 30/09/2026 | 1 245,00 |
| LIMOREAUPSY | Facture 08/2026 psychomotricité (payée par chèque 0004518, chèque non encore encaissé) | 31/08/2026 | 420,00 *(soldée par le chèque en septembre, lettrage à faire quand le chèque est débité)* |
| LIMOREAUPSY | Facture 09/2026 psychomotricité | 30/09/2026 | 960,00 |
| SAGIRARD | NDF 09/2026 | 30/09/2026 | 86,70 |
| FOTOTALCARTE | Relevé carte carburant 09/2026 | 05/10/2026 | 418,92 |
| FOLUDIK | Facture LE-2026-311 jeux éducatifs | 12/10/2026 | 537,60 |
| FOBUREAU26 | Facture BV-26-8812 | 28/10/2026 | 64,90 |
| SADURAND | NDF 10/2026 | 29/10/2026 | 142,30 |

**Pièce 5 — Ce que vous avez appris en posant des questions**

- Ligne 3 (Orange) : la facture de septembre a été **saisie au siège** (FOORANGE, crédit 312,48, au journal des achats de SIE). En regardant le mandat (la **RUM**, référence unique de mandat, se termine par « SIE »), la secrétaire du siège découvre que l'opérateur a, depuis septembre, prélevé sur **le mauvais IBAN** : celui du SESSAD, donné par erreur lors d'un changement de contrat.
- Ligne 6 : ticket de caisse et ticket CB agrafés, plein du véhicule de service du SESSAD (Kangoo). Pas de facture.
- Ligne 7 : IJSS (indemnités journalières de la sécurité sociale) d'une éducatrice en arrêt maladie, dont le salaire a été **maintenu** par l'association (subrogation : la CPAM rembourse l'employeur).
- Ligne 9 : la prévoyance complète le salaire d'un salarié en arrêt long.
- Ligne 12 : personne ne connaît Mme Leroy. Il n'y a ni facture, ni convention, ni courrier.
- Ligne 13 : TotalCarte a envoyé un mail le 23/10 : « Votre banque a rejeté notre prélèvement : le mandat signé en 2024 porte l'ancien IBAN. Merci de nous retourner un nouveau mandat signé. Le relevé de septembre reste dû. »
- Lignes 1 et 14 : le siège a avancé 20 000,00 € au SESSAD le 01/10, car la dotation de l'ARS (agence régionale de santé) arrive en général vers le 10 et le compte du SESSAD était bas avant la paie. Le 22/10, le SESSAD a rendu l'avance et payé en plus sa part des factures communes de septembre (**IS**, inter-structures) : 14 380,00 €.

**Pièce 6 — Courrier reçu le 16/11/2026 (arrivé au siège)**

> « Madame, le 20 octobre j'ai fait un virement de 150 euros pour soutenir votre association, après la fête de l'école de mon petit-fils Hugo. J'ai pris le RIB sur un papier du SESSAD que ma fille avait à la maison. Pouvez-vous m'envoyer un reçu pour les impôts ? Bien cordialement, Marie-Claude Leroy, 4 allée des Cèdres, 26500 Bourg-lès-Valence. »

## Travail à faire

1. Expliquez en cinq lignes, avec l'exemple de la ligne 4, ce que veut dire la phrase du document T21 : *« Les opérations seront saisies au débit pour les dépenses, et au crédit pour les recettes. »* Qu'est-ce que vous tapez, et qu'est-ce que le logiciel génère ?
2. Pour chaque ligne du relevé, indiquez **le compte que vous saisissez** (compte de tiers ou compte général), le sens, et le code analytique s'il y en a un. Une ligne ne doit **pas** être saisie : laquelle, et pourquoi ?
3. Passez les écritures d'octobre du journal **BQSES**. Montrez, pour chaque opération, **la ligne que vous tapez et la ligne 5122000 générée par le logiciel** (colonnes : Journal | Date | Compte | Tiers | Libellé | Analytique | Débit | Crédit).
4. **Ligne 3 (Orange)** : pourquoi ne faut-il surtout pas la passer en 6262000 Frais de télécommunication dans le SESSAD ? Passez l'écriture du SESSAD **et** l'écriture correspondante dans les livres du **siège**. Quelles actions non comptables faut-il lancer ?
5. **Ligne 12 (150,00 €)** : quelle écriture au 20/10 ? Puis, avec le courrier du 16/11, quelles écritures dans les trois livres concernés (SESSAD, siège, association) ? À qui revient le reçu fiscal ?
6. **Ligne 13** : comment traitez-vous le retour du prélèvement ? Que devient la facture de TotalCarte ?
7. **Lettrez** les comptes LIDUPONT, LIMOREAUPSY, SAGIRARD, FOTOTALCARTE et FOLUDIK après saisie. Que reste-t-il de non lettré, et pourquoi ?
8. Établissez l'**état de rapprochement bancaire** du compte 5122000 au 31/10/2026.
9. Calculez le **solde du compte 1840000** Liaison Siège dans les livres du SESSAD pour les seuls mouvements d'octobre. Quel solde devez-vous retrouver dans le compte 1849100 chez le siège pour ces mêmes mouvements ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-05_corrige.md)
