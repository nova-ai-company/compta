# Corrigé E00-04 — « Vous ne pourriez pas antidater la facture ? »

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E00-04](../exercices/E00-04_Karim-antidater-facture.md)

## 1. Analyse

### Demande 1 — antidater la facture du Ford Ranger
- **Comptablement** : une immobilisation entre au bilan au **transfert de contrôle**, en pratique à la livraison (le 08/01/2027), et s'amortit à compter de sa **mise en service**. La date de la facture ne change ni l'un ni l'autre. Le bon de livraison signé par Karim lui-même prouve la date réelle.
- **Fiscalement** : un amortissement pratiqué sur 2026 pour un bien mis en service en 2027 n'est **pas déductible**. Une facture de date fausse est une **facture de complaisance**. La TVA déduite sur une facture comportant des mentions inexactes peut être remise en cause, et l'amende pour facture fictive ou de complaisance peut s'appliquer.
- **Pénalement** : établir ou faire établir un document daté faussement constitue un **faux** (Code pénal, art. 441-1). Utilisé pour minorer l'impôt, il peut caractériser une **fraude fiscale** (CGI, art. 1741). Le concessionnaire, Nadia et le cabinet s'exposeraient à des poursuites en tant que **complices**.
- **Facturation électronique** : depuis le 01/09/2026, Bâtisseurs **reçoit** ses factures par une **PA**. La facture est horodatée à sa transmission : une facture « du 28/12 » émise le 10/01 laisserait une trace contradictoire.

### Demande 2 — retarder la facturation des Acacias
- **Comptablement** : le chantier est **achevé** (PV de réception sans réserve du 18/12/2026). Avec la méthode à l'achèvement, **tout** le chiffre d'affaires du marché est rattaché à **2026**, quelle que soit la date de facture. Le reste à facturer est constaté en **factures à établir (FAE)**. Retarder la facture ne déplace pas le produit.
- **Fiscalement** : pour les travaux, le produit est rattaché à l'exercice de **réception** (CGI, art. 38-2 bis : achèvement des prestations). Le report de la facture ne change donc pas l'IS 2026.
- **Facturation** : la facture doit être émise dès la réalisation de la prestation (Code de commerce et CGI fixent les délais d'émission). Un retard volontaire est une **infraction aux règles de facturation**, sanctionnée par une amende.
- **TVA** : sur des travaux immobiliers, la TVA est exigible à l'**encaissement**. Le report de facturation ne la décale donc pas non plus.

**Conclusion** : les deux demandes sont **illégales**, et en plus **inefficaces**. Le cabinet refuse par écrit, propose des leviers légaux et informe Hélène.

## 2. Calculs

### 2.1 Gain d'IS espéré par l'antidatage du véhicule

| Élément | Calcul | Montant |
|---|---|---|
| Base amortissable | Prix HT (TVA récupérable sur un pick-up utilitaire, sous réserve de sa qualification de véhicule utilitaire) | 42 000,00 € |
| Durée | 5 ans, linéaire | — |
| Prorata si mis en service le 28/12/2026 | 4 jours (28 au 31/12), base de 360 jours | 4/360 |
| Dotation 2026 « espérée » | 42 000 / 5 × 4/360 | **93,33 €** |
| Économie d'IS (taux de 25 %) | 93,33 × 25 % | **23,33 €** |

Karim pensait sans doute que l'achat entier était déductible. Ce n'est pas le cas : c'est une **immobilisation**, déduite par l'amortissement sur la durée d'utilisation. La fraude lui ferait risquer un redressement, des pénalités et des poursuites pénales **pour 23 €**.

### 2.2 Le chantier des Acacias

| Élément | Calcul | Montant |
|---|---|---|
| Reste à facturer HT | 520 000 − 436 000 | 84 000,00 € |
| TVA 20 % (logements neufs) | 84 000 × 20 % | 16 800,00 € |
| TTC | | 100 800,00 € |
| Impact sur le résultat 2026 | Rattaché à 2026 quelle que soit la date de facture | + 84 000,00 € |
| IS 2026 correspondant (taux de 25 %, la tranche à 15 % étant déjà absorbée) | 84 000 × 25 % | 21 000,00 € |
| Retenue de garantie de 5 % (sur le TTC du décompte, selon le marché) | 100 800 × 5 % | 5 040,00 € (à suivre dans un sous-compte 4117) |

## 3. Écritures comptables

**Au 31/12/2026 : facture à établir sur le chantier achevé**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 4181 | Clients – factures à établir | Acacias – DGD lot GO, réception 18/12/2026 | 100 800,00 | |
| 31/12/2026 | OD | 704 | Travaux | Acacias – solde marché | | 84 000,00 |
| 31/12/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | Acacias – TVA 20 % (exigible à l'encaissement) | | 16 800,00 |
| | | | | **Totaux** | **100 800,00** | **100 800,00** |

Extourne au 01/01/2027, puis facture définitive émise **sans délai** en janvier 2027, si elle ne l'a pas été en décembre comme elle aurait dû l'être.

**Le 08/01/2027 : réception de la facture du véhicule (datée du jour de la livraison)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 08/01/2027 | HA | 2182 | Matériel de transport | Ford Ranger GK-418-RT | 42 000,00 | |
| 08/01/2027 | HA | 44562 | TVA déductible sur immobilisations | Ford Ranger | 8 400,00 | |
| 08/01/2027 | HA | 404 | Fournisseurs d'immobilisations | Garage des Alpes – fact. du 08/01/2027 | | 50 400,00 |
| | | | | **Totaux** | **50 400,00** | **50 400,00** |

Aucune écriture d'amortissement en 2026. L'amortissement court à partir du 08/01/2027.

## 4. Points d'attention / pièges

- **La TVA sur le pick-up** : elle n'est récupérable que si le véhicule est bien **utilitaire** (pick-up de 4 ou 5 places à benne : sa qualification fiscale pour la TVA et pour les taxes sur véhicules est **à vérifier** au regard de la carte grise et des règles en vigueur). Ne pas récupérer la TVA d'un véhicule de tourisme.
- **La retenue de garantie** : la retenue de 5 % ne réduit pas le chiffre d'affaires. C'est une créance à plus long terme, à isoler.
- **Groupe intégré** : Bâtisseurs est dans le périmètre de Delta Invest (C10). Son IS est versé à la holding selon la convention d'intégration, et le résultat d'ensemble intègre ce produit. Le président de Delta, Jean Delmas, doit pouvoir compter sur des comptes sincères.
- Ne jamais répondre au téléphone « on va voir ce qu'on peut faire » : la réponse est **écrite**.
- Nadia est salariée et sous la pression de son employeur. Ne la mettez pas en porte-à-faux : la réponse vient **du cabinet**.

## 5. Ce qu'un senior ferait en plus

**Réponse à Karim (copie Nadia, validée par Hélène)** :

> Objet : Clôture 2026 — Ford Ranger et chantier des Acacias
>
> Bonjour Monsieur Benali,
>
> Nadia m'a transmis vos deux demandes. Nous ne pouvons pas y donner suite, et ce ne serait de toute façon pas dans votre intérêt :
>
> 1. **Ford Ranger** : la date d'entrée et d'amortissement d'un véhicule est celle de sa **livraison** (08/01/2027, bon signé de votre main), pas celle de la facture. Une facture antidatée serait un faux. L'économie d'IS serait de l'ordre de **23 €** (4 jours d'amortissement), pour un risque fiscal et pénal pour vous, pour le concessionnaire et pour Nadia.
> 2. **Les Acacias** : le chantier a été réceptionné le 18/12/2026. Comptablement et fiscalement, les 84 000 € HT appartiennent à **2026**, même facturés en janvier. Nous les enregistrons en « facture à établir ». En revanche, la facture doit être émise **sans attendre** : un retard de facturation est sanctionné par une amende.
>
> Pour réduire **légalement** votre IS, nous vous proposons d'étudier avant la clôture 2027, lors d'un rendez-vous en septembre :
> - un calendrier d'investissements avec **mise en service** avant la clôture (amortissement dégressif si les conditions sont remplies) ;
> - la **revue des risques** chantiers au 31/12/2026 (litiges, pénalités de retard, pertes à terminaison) : ce sont des provisions déductibles si elles sont justifiées ;
> - un dispositif d'**épargne salariale** (intéressement), déductible ;
> - l'arbitrage rémunération / dividendes au niveau du groupe, avec Delta Invest.
>
> Je reste à votre disposition.
> Cordialement,

**Suites internes** :
- Note datée à Hélène (fait, réponse, pièces). La demande d'un faux visant à minorer l'impôt est un **signal LCB-FT** (fraude fiscale) : l'appréciation d'une éventuelle déclaration revient au déclarant du cabinet. Ne rien en dire au client.
- Mise à jour de la fiche de vigilance de C02. **Lettre d'affirmation** de fin d'exercice signée par le président, mentionnant l'exhaustivité du chiffre d'affaires et des chantiers réceptionnés.
- Vérification, lors de la révision, de **tous** les PV de réception de décembre 2026 contre les factures : y a-t-il d'autres chantiers « décalés » ?

## 6. Références
- PCG : règles de comptabilisation des immobilisations (entrée au transfert de contrôle, amortissement à compter de la mise en service) et des contrats à long terme (méthode à l'achèvement / à l'avancement).
- CGI, art. 38-2 bis (rattachement des produits : achèvement des prestations) ; art. 39-1-2° (amortissements) ; art. 39 A (amortissement dégressif) ; art. 1737 (sanctions des manquements aux règles de facturation) ; art. 1741 (fraude fiscale).
- CGI, art. 242 nonies A, annexe II (mentions des factures) ; art. 289 (émission des factures).
- Code pénal, art. 441-1 (faux) et art. 121-7 (complicité).
- Code de déontologie des professionnels de l'expertise comptable (indépendance, refus de concourir à des actes illicites).
