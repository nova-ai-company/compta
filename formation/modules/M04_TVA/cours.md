# M04 — La TVA de A à Z

> **Objectif du module.** À la fin de ce module, vous savez déterminer si une opération est taxable, où, quand et à quel taux ; calculer la TVA déductible (y compris avec un coefficient de déduction) ; remplir une CA3 et une CA12 ; traiter l'autoliquidation, les échanges intracommunautaires, l'OSS, la TVA sur la marge et la TVA immobilière ; rapprocher le CA déclaré du CA comptable et corriger une erreur. C'est le module où une junior devient « fiable » aux yeux d'un associé.
>
> **Prérequis :** M02 (achats) et M03 (ventes).

> ⚠️ **Valeurs chiffrées.** Les seuils de franchise et de régimes ont fait l'objet de réformes et de débats en 2025 (projet de seuil unique de franchise finalement non appliqué). Dans ce module, on **retient** les valeurs ci-dessous, à **vérifier chaque année** (loi de finances, BOFiP) :
>
> | Seuil | Valeur retenue |
> |---|---|
> | Franchise en base — ventes / hébergement : seuil de base / seuil majoré | 85 000 € / 93 500 € |
> | Franchise en base — prestations de services : seuil de base / seuil majoré | 37 500 € / 41 250 € |
> | Réel simplifié (RSI) — ventes / services (plafonds de CA HT) | 840 000 € / 254 000 € |
> | RSI — TVA exigible annuelle au-delà de laquelle le réel normal s'impose | 15 000 € |
> | Dispense d'acomptes RSI (TVA due N-1 avant déduction sur immobilisations) | < 1 000 € |
> | Ventes à distance intra-UE (seuil communautaire unique) | 10 000 € HT |
> | Cadeaux : TVA déductible si valeur unitaire ≤ | 73 € TTC par bénéficiaire et par an |
> | Remboursement de crédit : demande annuelle / mensuelle ou trimestrielle | ≥ 150 € / ≥ 760 € |
>
> *Valeurs à vérifier chaque année.*

!!! abstract "En clair — ce module en 5 idées"
    1. **La TVA n'est pas une charge de l'entreprise.** L'entreprise l'ajoute à ses prix, la récupère sur ses achats, et reverse la différence à l'État. Elle sert d'intermédiaire.
    2. **Avant de calculer, on se pose trois questions dans l'ordre.** L'opération est-elle concernée par la TVA ? Est-elle taxée en France ? Est-elle exonérée ? Exemple : les consultations du Dr Lambert (C05) sont exonérées, elle ne facture donc pas de TVA.
    3. **Le moment compte autant que le montant.** Pour une vente de biens, la TVA est due à la livraison. Pour un service, elle est due quand le client paie. C13 Atelier Ligne, le cabinet d'architectes, déclare donc la TVA de ce qu'il a encaissé, pas de ce qu'il a facturé.
    4. **On ne récupère pas toute la TVA de ses achats.** Certaines dépenses sont exclues (voiture de tourisme, cadeaux trop chers…). Une entreprise qui a aussi des activités sans TVA, comme la holding C10 Delta Invest, ne récupère qu'une partie.
    5. **À la fin, tout doit coller.** Les ventes en comptabilité, les ventes déclarées et la TVA déclarée doivent se rapprocher. Chaque écart s'explique et s'écrit dans le dossier.

??? info "Les mots à connaître avant de commencer (cliquez pour ouvrir)"
    | Mot / sigle | Ce que ça veut dire, simplement | Exemple |
    |---|---|---|
    | TVA collectée | La TVA que l'entreprise ajoute sur ses ventes et qu'elle doit reverser | C04 Le Petit Zinc ajoute 10 % sur un repas |
    | TVA déductible | La TVA payée sur les achats, que l'entreprise peut retirer de ce qu'elle doit | La TVA sur le four acheté par C01 Boulangerie Dupain |
    | Assujetti | Une personne ou une entreprise qui exerce une activité économique et entre dans le système de la TVA | Une SARL commerciale est assujettie |
    | Hors champ | L'opération n'est pas concernée du tout par la TVA | Les dividendes reçus par C10 Delta Invest |
    | Exonérée | L'opération est concernée par la TVA, mais la loi dit qu'on n'en facture pas | Les soins du Dr Lambert (C05) |
    | Exigibilité | Le moment où la TVA doit être déclarée et payée | À l'encaissement pour un service |
    | Option pour les débits | Choix de payer la TVA d'un service dès la facture, sans attendre le paiement | Mention obligatoire sur la facture |
    | Franchise en base | Petite entreprise qui ne facture pas de TVA tant qu'elle reste sous un seuil | C17 Paul Durand, qui dépasse le seuil en 2026 |
    | CA3 / CA12 | Les formulaires de déclaration de TVA : CA3 chaque mois, CA12 une fois par an | C01 au réel simplifié dépose une CA12 |
    | Crédit de TVA | Quand la TVA récupérable dépasse la TVA due : l'État vous doit de l'argent | Un gros investissement dans le mois |
    | Coefficient de déduction | Le pourcentage de TVA sur achats que l'entreprise a le droit de récupérer | 0,90 → on récupère 90 % |
    | Autoliquidation | C'est le client, et non le vendeur, qui déclare la TVA | Un service acheté à un prestataire étranger |
    | Intracommunautaire (LIC / AIC) | Une vente (LIC) ou un achat (AIC) de biens entre deux pays de l'Union européenne | C19 Asia Trading livre un client professionnel dans un autre pays de l'UE |
    | OSS | Un guichet en ligne unique pour déclarer la TVA des ventes à des particuliers d'autres pays de l'UE | C09 Mode & Co vend à des particuliers d'autres pays de l'UE |
    | TVA sur la marge | Pour certains biens d'occasion, on taxe seulement le bénéfice, pas tout le prix | Une voiture d'occasion vendue par C03 Garage Martin |

---

## 1. Le champ d'application : trois questions dans l'ordre

> 🟢 **En clair :** avant tout calcul, demandez-vous si l'opération est concernée par la TVA. Trois questions, toujours dans le même ordre, vous donnent la réponse. Exemple : la taxe de séjour de l'hôtel C16 ne porte pas de TVA, car elle est « hors champ ».

```
1. L'opération est-elle DANS LE CHAMP ?   (livraison de bien / prestation de services à titre onéreux
                                            par un assujetti agissant en tant que tel)
      non → hors champ (dividendes, subventions non liées au prix, indemnités, cessions de titres…)
      oui ↓
2. Est-elle IMPOSABLE EN FRANCE ?          (règles de territorialité : lieu de livraison / lieu de prestation)
      non → hors champ territorial (ex. service B2B à un client UE → taxable chez le client)
      oui ↓
3. Est-elle EXONÉRÉE ?                     (médical, enseignement, locations nues, opérations financières,
                                            exportations, livraisons intracommunautaires…)
      oui → exonérée (avec ou sans droit à déduction selon les cas) ; option parfois possible
      non → TAXABLE : à quel taux ? qui est redevable ? quand ?
```

| Catégorie | Exemples du portefeuille | Droit à déduction des achats liés |
|---|---|---|
| Hors champ | Dividendes reçus (C10), taxe de séjour (C16), indemnité d'arrhes conservées (C16) | Non (sauf frais généraux selon le coefficient d'assujettissement) |
| Exonérée sans droit à déduction | Soins médicaux (C05), location nue d'habitation (C06), intérêts de prêts (C10) | **Non** → TVA sur achats = charge |
| Exonérée avec droit à déduction | Exportations (C18, C19), livraisons intracommunautaires (C19) | **Oui** |
| Taxable | Presque tout le reste | Oui |

> 💡 **Réflexe senior :** « exonéré » et « hors champ » ne sont pas synonymes. L'un et l'autre ne génèrent pas de TVA collectée, mais ils n'ont pas le même effet sur le coefficient de taxation (les opérations hors champ ne figurent pas dans le calcul) ni sur la CA3 (lignes différentes).

---

## 2. Fait générateur et exigibilité

> 🟢 **En clair :** cette section répond à la question « sur quel mois je déclare cette TVA ? ». Pour des biens, c'est en général le mois de la livraison. Pour des services, c'est le mois où le client paie.

Le **fait générateur** est l'événement qui fait naître la dette fiscale ; l'**exigibilité** est le moment où l'administration peut en réclamer le paiement — c'est elle qui détermine **sur quelle déclaration** la TVA est portée (art. 269 CGI).

> 🟢 **En clair :** le fait générateur, c'est « la dette de TVA existe ». L'exigibilité, c'est « l'État peut la demander maintenant ». C'est l'exigibilité qui décide du mois de déclaration.

| Opération | Exigibilité | Acomptes |
|---|---|---|
| **Livraisons de biens** | À la livraison (transfert du pouvoir de disposer) | **Depuis le 01/01/2023, l'encaissement d'un acompte rend la TVA exigible** à hauteur de l'acompte |
| **Prestations de services** (y compris travaux immobiliers) | À l'**encaissement** du prix (acomptes inclus) | TVA exigible à l'encaissement de l'acompte |
| Prestations de services avec **option pour les débits** | À la facturation (débit en compte) | — |
| Prestations continues avec décomptes (B2B intra-UE, autoliquidation) | À l'achèvement / à chaque échéance ou paiement selon le cas | — |
| Livraisons intracommunautaires | Le 15 du mois suivant la livraison ou à la facture si antérieure | — |

**Option pour les débits** : demandée au SIE ; elle simplifie la gestion (TVA = facture) mais oblige à reverser une TVA non encaissée. Elle doit être **mentionnée sur les factures** (« Option pour le paiement de la taxe d'après les débits ») — mention reprise dans les nouvelles mentions de la facture électronique.

> ⚠️ **Erreur classique :** déclarer la TVA des prestations de services sur la base des **factures émises** du mois. Pour un cabinet d'architectes (C13) ou un consultant (C17), c'est le **relevé des encaissements** du mois qui fait la TVA collectée. En comptabilité, on utilise un compte **44574 « TVA collectée en attente »** (subdivision usuelle de 4457) entre la facture et l'encaissement.

---

## 3. Les régimes d'imposition

> 🟢 **En clair :** selon sa taille, une entreprise ne facture pas de TVA (franchise), la déclare une fois par an (réel simplifié, CA12) ou tous les mois (réel normal, CA3). Connaître le régime de chaque client vous dit quelle déclaration préparer et quand.

### 3.1 Franchise en base (art. 293 B CGI)

- Pas de TVA facturée (mention **« TVA non applicable, art. 293 B du CGI »**), pas de TVA déductible.
- Bénéficie de la franchise en N l'entreprise dont le CA N-1 n'excède pas le **seuil de base**, ou le **seuil majoré** si le CA N-2 n'excédait pas le seuil de base.
- **Dépassement du seuil de base** en cours d'année (sans dépasser le seuil majoré) : la franchise est maintenue pour l'année en cours, perdue au 1er janvier suivant.
- **Dépassement du seuil majoré** : depuis le 01/01/2025, la TVA est due **à compter de l'opération qui entraîne le dépassement** (incluse). Avant 2025, c'était à compter du premier jour du mois du dépassement.
- Les factures déjà émises en franchise **restent valables** : on ne refacture pas de TVA a posteriori sur des opérations antérieures au dépassement.
- Le CA s'apprécie **HT** et sur l'**année civile**, en distinguant ventes / services pour les entreprises mixtes.

### 3.2 Réel simplifié (RSI)

- Déclaration **annuelle CA12** (formulaire 3517-S), déposée au plus tard le **2e jour ouvré suivant le 1er mai** (exercice = année civile) ; dans les 3 mois de la clôture pour un exercice décalé (CA12E).
- **Deux acomptes semestriels** : **juillet (55 %)** et **décembre (40 %)** de la TVA due au titre de l'année précédente **avant déduction de la TVA sur immobilisations**. Pas d'acompte si cette base est inférieure à 1 000 €. Possibilité de **moduler** (réduire) les acomptes sous sa responsabilité (majoration si l'estimation est inexacte de plus de 20 %).

> 🟢 **En clair :** au réel simplifié, on paie deux avances dans l'année (en juillet et en décembre), calculées sur la TVA de l'année d'avant. On fait le compte exact une fois par an, sur la CA12.
- Le RSI cesse de s'appliquer si le CA dépasse les plafonds ou si la **TVA exigible annuelle dépasse 15 000 €** : passage au réel normal (à compter de l'année suivante — *modalités à vérifier*).
- Option possible pour le réel normal (CA3), utile pour un remboursement rapide de crédit.

### 3.3 Réel normal (CA3)

- Déclaration **mensuelle CA3** (formulaire 3310-CA3), déposée entre le 15 et le 24 du mois suivant selon le calendrier propre à l'entreprise (consulter l'espace professionnel).
- **Trimestrielle** possible si la TVA annuelle est inférieure à 4 000 € (*valeur à vérifier*).
- Télédéclaration et télépaiement obligatoires (EDI ou espace professionnel).

### 3.4 Les grandes lignes de la CA3 (3310-CA3)

*Numérotation à contrôler sur le formulaire millésimé de l'année.*

| Cadre / ligne | Contenu |
|---|---|
| **A1** | Ventes, prestations de services (HT) taxables en France |
| **A2** | Autres opérations imposables (livraisons à soi-même, cessions d'immobilisations…) |
| **A3** | Achats de **prestations de services** auprès d'un assujetti non établi en France (autoliquidation, art. 283-2) |
| **A4** | **Importations** (autres que produits pétroliers) — autoliquidation |
| **B2** | **Acquisitions intracommunautaires** |
| **B4** | Achats de biens / services auprès d'un assujetti non établi (art. 283-1) |
| **E1** | Exportations hors UE |
| **E2** | Autres opérations non imposables (dont services B2B UE, sous-traitance BTP autoliquidée par le client) |
| **E3** | Ventes à distance taxables dans un autre État membre (B2C) — déclarées via l'OSS |
| **F2** | **Livraisons intracommunautaires** à un assujetti |
| **08 / 09 / 9B** | Bases et TVA due à **20 % / 5,5 % / 10 %** (ligne dédiée pour le **2,1 %**) |
| **15** | TVA antérieurement déduite à **reverser** |
| **16** | Total TVA brute |
| **17** | dont TVA sur acquisitions intracommunautaires |
| **19** | TVA déductible sur **immobilisations** |
| **20** | TVA déductible sur **autres biens et services** |
| **21** | **Autre TVA à déduire** (régularisations, impayés…) |
| **22** | Report du crédit de la déclaration précédente |
| **23** | Total TVA déductible ; **24** dont TVA déductible sur importations |
| **25** | Crédit de TVA ; **26** remboursement demandé (formulaire **3519**) ; **27** crédit à reporter |
| **28** | TVA nette due ; **32** total à payer |

> 💡 **Réflexe senior :** l'autoliquidation (import, AIC, services B2B étrangers, sous-traitance BTP côté preneur) apparaît **deux fois** : en TVA brute (ligne 08) et en TVA déductible (lignes 19/20). Elle est neutre en trésorerie si le droit à déduction est total — mais **son omission est sanctionnée** (amende de 5 % des sommes non déclarées, art. 1788 A CGI, *à vérifier*), même sans enjeu de droits.

---

## 4. Les taux

> 🟢 **En clair :** il existe quatre taux de TVA. Le bon taux dépend de ce qui est vendu, et parfois de la façon dont c'est vendu. Exemple : un repas servi par C04 Le Petit Zinc est à 10 %, mais un verre de vin servi avec ce repas est à 20 %.

| Taux | Principales opérations |
|---|---|
| **20 %** | Taux normal : la majorité des biens et services ; boissons alcoolisées ; parapharmacie ; véhicules |
| **10 %** | Restauration et ventes à consommer immédiatement ; hébergement hôtelier ; transport de voyageurs ; médicaments non remboursables ; travaux d'amélioration, de transformation, d'aménagement et d'entretien de **logements achevés depuis plus de 2 ans** |
| **5,5 %** | Produits alimentaires (consommation différée) ; boissons non alcoolisées à emporter ; livres ; équipements pour personnes handicapées ; travaux de **rénovation énergétique** de logements de plus de 2 ans ; certaines protections hygiéniques |
| **2,1 %** | Médicaments **remboursables** ; publications de presse ; certains spectacles (premières représentations) |

**Travaux dans les logements (10 % / 5,5 %)** : conditions cumulatives (local à usage d'habitation, achevé depuis plus de 2 ans, travaux ne concourant pas à une production d'immeuble neuf, fourniture et pose par l'entreprise). Le preneur certifie que ces conditions sont remplies : historiquement par une **attestation** (formulaires 1300-SD / 1301-SD) ; depuis 2025, la justification peut prendre la forme d'une **mention** portée sur le devis ou la facture et signée par le client (*modalités à vérifier au BOFiP*). L'entreprise doit conserver cette justification : sans elle, le taux réduit est remis en cause chez **elle**.

---

## 5. Le droit à déduction

> 🟢 **En clair :** « déduire » la TVA, c'est récupérer la TVA payée sur ses achats. Ce n'est possible que si la facture est correcte, si l'achat sert à une activité soumise à la TVA, et si la dépense n'est pas exclue par la loi.

### 5.1 Conditions

- **Fond** : la dépense est engagée pour les besoins d'opérations **ouvrant droit à déduction** (taxables ou exonérées avec droit à déduction), et n'est pas exclue.
- **Forme** : détention d'une **facture** régulière (mentions obligatoires, TVA correctement calculée, au nom de l'entreprise) ou d'une déclaration d'importation ; et TVA **exigible chez le fournisseur** (pour un service sans option débits : au paiement du fournisseur).
- **Délai** : la déduction s'exerce sur la déclaration du mois où le droit naît ; une omission peut être réparée sur une déclaration ultérieure jusqu'au **31 décembre de la 2e année** suivant celle de l'omission.

### 5.2 Exclusions principales (art. 206 IV ann. II CGI)

| Dépense | Règle |
|---|---|
| **Véhicules de tourisme** (VP, véhicules conçus pour transporter des personnes ou à usage mixte) : achat, location, entretien, pièces | **Non déductible** (sauf véhicules affectés à un usage d'enseignement de la conduite, de taxi, de location, de transport public de personnes…) |
| Véhicules utilitaires (camionnettes, camions) | Déductible |
| Gazole / supercarburant (essence, E85) des **VP** | **80 %** déductible |
| Gazole / essence des **véhicules utilitaires** | 100 % déductible |
| **Logement** des dirigeants et du personnel | Non déductible (sauf gardiennage / sécurité sur le lieu de travail) |
| **Cadeaux** | Déductible seulement si valeur unitaire ≤ 73 € TTC par bénéficiaire et par an |
| Transport de personnes (billets) | Non déductible (sauf transport collectif du personnel sur le lieu de travail) |
| Services liés à un bien exclu (entretien d'un VP) | Non déductible |

### 5.3 Le coefficient de déduction (art. 206 ann. II CGI)

**Coefficient de déduction = coefficient d'assujettissement × coefficient de taxation × coefficient d'admission**

| Coefficient | Ce qu'il mesure | Exemple Delta Invest (C10) |
|---|---|---|
| **Assujettissement** | Part d'utilisation du bien/service pour des opérations **dans le champ** de la TVA | Frais généraux d'une holding qui facture des management fees (dans le champ) mais gère aussi un portefeuille de titres (hors champ, dividendes) : clé d'utilisation documentée |
| **Taxation** | Part des opérations **ouvrant droit à déduction** parmi les opérations dans le champ | Management fees (taxables) / (management fees + intérêts de prêts aux filiales exonérés) |
| **Admission** | Exclusions légales | 0 pour un VP, 1 sinon |

- Calcul de chaque coefficient **arrondi par excès** au centième (ex. 0,8955 → 0,90 ; 0,675 → 0,68).
- Coefficient de taxation : ratio CA ouvrant droit à déduction / CA total (opérations dans le champ), en excluant les **cessions de biens d'investissement**, les **subventions d'équipement** et les **opérations financières ou immobilières accessoires**.
- **Coefficients provisoires** en N (sur la base de N-1 ou d'estimations), **définitifs** arrêtés au plus tard le **25 avril N+1** : la régularisation (positive ou négative) est portée sur la déclaration déposée avant cette date (ligne 15 « TVA à reverser » ou ligne 21 « autre TVA à déduire »).
- **Immobilisations** : après l'année d'acquisition, régularisation annuelle **si le coefficient varie de plus de 10 points** par rapport au coefficient définitif de l'année d'acquisition : montant = TVA initiale × (coefficient de l'année – coefficient d'origine) / 5 (biens meubles) ou / 20 (immeubles).
- Pas de coefficient « à la louche » : la holding qui déduit 100 % de sa TVA sur frais généraux est une cible classique de contrôle.

> 🟢 **En clair :** le coefficient de déduction est un pourcentage obtenu en multipliant trois chiffres entre 0 et 1. Il dit quelle part de la TVA d'un achat vous pouvez récupérer. On l'estime en début d'année, puis on le corrige avec les chiffres réels avant le 25 avril de l'année suivante.

### 5.4 Régularisations (art. 207 ann. II CGI)

| Événement | Régularisation |
|---|---|
| Bien affecté à une opération qui n'ouvre plus droit à déduction | Reversement (immobilisation : au prorata de la période restante, 1/5 ou 1/20 par année) |
| Cession d'une immobilisation **sans TVA** dans la période de régularisation | Reversement de la fraction non encore « consommée » |
| Assujetti qui **devient redevable** (sortie de franchise, option) | **Régularisation positive** : déduction de la TVA des immobilisations détenues, diminuée d'1/5 (ou 1/20) par année civile ou fraction d'année écoulée depuis l'acquisition |
| Vol, destruction (non justifiés) de biens | Reversement |

---

## 6. L'autoliquidation

> 🟢 **En clair :** dans certains cas, c'est l'acheteur qui déclare la TVA à la place du vendeur, puis la récupère sur la même déclaration. C'est souvent sans coût, mais l'oublier est sanctionné. Exemple : les luminaires importés de Chine par C19 Asia Trading.

C'est le **client** qui déclare et (le cas échéant) déduit la TVA, à la place du fournisseur.

| Situation | Base légale | Qui autoliquide | Lignes CA3 du preneur |
|---|---|---|---|
| Services B2B rendus par un prestataire établi hors de France | Art. 283-2 CGI | Le preneur français | A3 + 08 / 20 |
| Acquisition intracommunautaire de biens | Art. 256 bis | L'acquéreur | B2 + 08 + 17 / 20 (ou 19) |
| **Importation** (depuis le 01/01/2022, obligatoire pour tous les assujettis identifiés en France) | Art. 1695 II | L'importateur, sur la CA3 | A4 + 08 / 20 + 24 |
| **Sous-traitance BTP** | Art. 283-2 nonies | L'entreprise principale | Le sous-traitant facture HT (ligne E2) ; l'entreprise principale autoliquide |
| Livraisons de biens par un fournisseur non établi (installés en France…) | Art. 283-1 | Le client assujetti | B4 |

**Base de la TVA à l'importation** (art. 292 CGI) : valeur en douane (en général **CIF** : prix + transport + assurance jusqu'à la frontière de l'UE) + **droits de douane** + frais accessoires jusqu'au premier lieu de destination en France (s'ils sont connus à l'importation). Les données douanières de la période sont mises à disposition dans l'espace professionnel : **rapprochez-les** de la CA3.

> ⚠️ **Erreur classique :** calculer la TVA à l'importation sur le prix facturé par le fournisseur chinois (FOB) en oubliant le fret, l'assurance et les droits de douane.

---

## 7. Les échanges intracommunautaires

> 🟢 **En clair :** quand on vend ou achète dans un autre pays de l'Union européenne, la TVA suit des règles spéciales. Entre professionnels, la vente part souvent sans TVA. Vers des particuliers, au-delà d'un seuil, on applique la TVA du pays du client.

### 7.1 Livraison intracommunautaire (LIC) exonérée (art. 262 ter I CGI)

Conditions **cumulatives** :
1. le bien est **expédié ou transporté** dans un autre État membre (preuves : CMR, facture du transporteur, attestation de réception de l'acquéreur — présomption à partir de deux documents non contradictoires) ;
2. l'acquéreur est un **assujetti** identifié dans un autre État membre, qui a **communiqué un numéro de TVA valide** (vérifier sur **VIES** et archiver la preuve de la consultation) ;
3. la livraison est déclarée dans l'**état récapitulatif des clients** (ex-volet fiscal de la DEB), déposé mensuellement (au plus tard le 10e jour ouvrable du mois suivant — *à vérifier*). Le volet statistique est désormais une enquête distincte (EMEBI) pour les entreprises interrogées.

Mention sur la facture : **« Exonération de TVA, article 262 ter I du CGI »**, avec les numéros de TVA du vendeur et de l'acquéreur. Déclaration : ligne **F2**.

### 7.2 Acquisition intracommunautaire (AIC)

Taxable en France chez l'acquéreur (autoliquidation), lignes B2 / 08 / 17 et déduction 19 ou 20. Exigibilité : le 15 du mois suivant ou à la facture si antérieure.

### 7.3 Services B2B intra-UE

Règle générale : taxables chez le **preneur** (art. 259-1°). Le prestataire français facture HT avec la mention « Autoliquidation », déclare en **E2** et dépose une **déclaration européenne de services (DES)**.

### 7.4 Ventes à distance B2C et guichet unique (OSS / IOSS)

- Ventes de biens expédiés par un vendeur français à des **particuliers** d'autres États membres : taxables **en France** tant que le total annuel de ces ventes (et des services électroniques B2C UE) ne dépasse pas **10 000 € HT** (année en cours et année précédente) ; au-delà, taxables **dans l'État de destination** **à compter de la vente qui fait franchir le seuil** (art. 258 A, 259 D CGI). Option possible pour la taxation à destination dès le premier euro.

> 🟢 **En clair :** tant que les ventes à des particuliers des autres pays de l'UE restent sous 10 000 € HT par an, on applique la TVA française. Dès la vente qui fait passer ce seuil, on applique la TVA du pays du client.
- Plutôt que de s'immatriculer dans chaque pays, le vendeur utilise le **guichet unique OSS** (One-Stop-Shop) via son espace professionnel français : **déclaration trimestrielle** (au plus tard le dernier jour du mois suivant le trimestre), en euros, par pays et par taux, paiement unique. Les ventes sont reportées en **ligne E3** de la CA3.
- **IOSS** (Import One-Stop-Shop) : ventes à distance de biens **importés** d'une valeur ≤ 150 € ; la TVA est collectée à la vente et l'importation est exonérée.
- **Plateformes** : une marketplace qui facilite des ventes de vendeurs **non établis dans l'UE** est réputée fournisseur (elle collecte la TVA) ; un vendeur français comme Mode & Co reste redevable de sa TVA.

---

## 8. Régimes particuliers

> 🟢 **En clair :** deux cas sortent de la règle habituelle. Les biens d'occasion, où l'on taxe seulement la marge (les voitures de C03 Garage Martin). Et l'immobilier, où une location peut être avec ou sans TVA (les bureaux loués par C07 SCI Horizon Pro sont avec TVA, sur option).

### 8.1 TVA sur la marge — biens d'occasion (art. 297 A CGI)

- S'applique aux **assujettis-revendeurs** sur les biens acquis **sans TVA déductible** (achats à des particuliers, à des assujettis exonérés, à des revendeurs sous le régime de la marge).
- **Marge = prix de vente TTC – prix d'achat** ; TVA = marge × 20/120. Les frais de remise en état ne s'ajoutent **pas** au prix d'achat (leur TVA est déductible).
- **Pièce par pièce** pour les véhicules ; **marge globale** (compensation des marges positives et négatives sur la période) réservée aux biens dont le prix d'achat unitaire **n'excède pas 300 €**.
- Pas de TVA apparente sur la facture ; mention « Régime particulier – Biens d'occasion ».
- Véhicule acquis auprès d'un professionnel avec une facture de TVA : **régime normal** (TVA sur le prix total, TVA d'achat déductible).
- Ligne de la CA3 : la **marge HT** constitue la base imposable (*voir la notice de la CA3 pour la présentation exacte*).

### 8.2 TVA immobilière

- **Locations nues** de locaux professionnels : **exonérées** (art. 261 D 2° CGI) avec **option possible** (art. 260-2° CGI) lorsque le preneur est assujetti (ou non assujetti si le bail fait mention de l'option). L'option ouvre droit à déduction de la TVA sur la construction, l'acquisition et les travaux ; elle se gère par immeuble / local selon les règles de l'article 260-2° et de l'annexe II.
- **Locations d'habitation nues** : exonérées sans option (C06) ; **locations meublées** : exonérées sauf para-hôtellerie (3 des 4 services : petit-déjeuner, nettoyage régulier, linge, accueil — C23).
- Les **refacturations** au locataire (taxe foncière, charges) sont un **complément de loyer** : elles suivent le régime du loyer (TVA 20 % si option). Ce ne sont pas des débours, car le bailleur est le **redevable légal** de la taxe foncière.
- Cessions d'immeubles : neufs (moins de 5 ans) taxables ; anciens exonérés avec option ; terrains à bâtir taxables ; TVA sur la marge dans certains cas — hors du périmètre de ce module.

---

## 9. Crédit de TVA et remboursement

> 🟢 **En clair :** si, sur une période, l'entreprise a payé plus de TVA sur ses achats qu'elle n'en a facturé, l'État lui doit la différence. Elle peut la garder pour plus tard ou en demander le remboursement.

- Un crédit apparaît quand la TVA déductible dépasse la TVA collectée (investissements, exportations, démarrage d'activité).
- Il est **reporté** (ligne 27) ou fait l'objet d'une **demande de remboursement** (formulaire **3519**, déposé avec la CA3 — ligne 26) :
  - **annuelle** : crédit constaté au 31/12 au moins égal à 150 € ;
  - **mensuelle ou trimestrielle** (réel normal) : crédit au moins égal à 760 € ;
  - au RSI : sur la CA12, et en cours d'année sous conditions (investissements, montant ≥ 760 €).
- Comptablement : 44583 « Remboursement de taxes sur le CA demandé » / 44567 « Crédit de TVA à reporter » ; à l'encaissement : 512 / 44583.
- Une demande de remboursement déclenche souvent un **contrôle sur pièces** : préparez un dossier (factures d'immobilisations, explication du crédit).

---

## 10. Contrôle de cohérence : CA comptable / CA déclaré / TVA collectée

> 🟢 **En clair :** c'est la vérification la plus importante en TVA. On compare les ventes de la comptabilité avec les ventes déclarées sur l'année. Si les deux ne collent pas, on doit pouvoir expliquer pourquoi, chiffres à l'appui.

C'est **le** contrôle de révision TVA. Formule de rapprochement (à adapter à chaque dossier) :

```
CA comptable HT (comptes 70x, net des 709)
 + produits taxables hors 70 (cessions d'immobilisations 775 si TVA, refacturations en 708…)
 + variation des PCA (services encaissés d'avance : TVA déjà exigible)
 – variation des créances clients sur services (TVA sur encaissements : facturé non encaissé)
 + bons à usage unique vendus non utilisés (TVA à l'émission, CA différé)
 – opérations exonérées / hors champ / autoliquidées par le client (déclarées en E1, E2, F2…)
 = Base taxable théorique → à comparer aux bases cumulées des CA3 (lignes 08, 09, 9B…)
```

Puis : **TVA collectée théorique** (base × taux) = **mouvements créditeurs du 44571** = **TVA brute des CA3**. Et pour la TVA déductible : 44562 + 44566 = lignes 19 + 20 (+ 21). Enfin : solde du 44551 au 31/12 = TVA due de décembre.

> 🟢 **En clair :** trois choses doivent donner le même montant : la TVA calculée sur les ventes, la TVA enregistrée en comptabilité et la TVA déclarée. Même logique pour la TVA récupérée. Et la TVA restant à payer au 31/12 doit être celle de la déclaration de décembre.

> 💡 **Réflexe senior :** un écart de rapprochement n'est pas forcément une erreur (PCA, encaissements, bons, cessions) — mais **tout écart doit être expliqué** et documenté dans le dossier, chiffré, avec un résidu inexpliqué non significatif.

---

## 11. Erreurs, rectifications et sanctions

> 🟢 **En clair :** une erreur de TVA se corrige, en général sur une déclaration suivante. Plus on la corrige tôt et de soi-même, moins elle coûte. Ce tableau vous dit quoi faire selon le type d'erreur.

| Situation | Que faire |
|---|---|
| TVA collectée omise / sous-déclarée | Régulariser sur la **déclaration suivante** (en mentionnant la période d'origine) ou par **déclaration rectificative** ; intérêt de retard **0,20 % par mois** (art. 1727 CGI), réduit en cas de régularisation spontanée (droit à l'erreur, loi ESSOC — *taux de réduction à vérifier*) |
| TVA déduite à tort (VP, facture irrégulière) | **Reversement** (ligne 15) + intérêt de retard |
| TVA déductible omise | Déduction sur une déclaration ultérieure jusqu'au 31/12 de la 2e année suivant l'omission ; au-delà, **réclamation** |
| TVA facturée à tort | Due du seul fait de sa facturation (art. 283-3) jusqu'à rectification de la facture |
| Retard de dépôt | Majoration de **10 %** (art. 1728 CGI), 40 % après mise en demeure restée sans effet |
| Manquement délibéré | Majoration de **40 %** (art. 1729) |
| Défaut d'autoliquidation (sans perte de recettes) | Amende de 5 % des droits (art. 1788 A — *à vérifier*) |

Crédit de TVA et erreur : si l'entreprise est restée créditrice sur toute la période, une sous-déclaration n'a pas causé de **retard de paiement** — pas d'intérêt de retard, mais correction du crédit reporté.

---

## 12. Facturation électronique et TVA (2026-2027)

> 🟢 **En clair :** avec la facture électronique, l'administration verra passer les factures et les paiements presque en direct. Les incohérences entre factures et déclarations de TVA seront repérées tout de suite : la rigueur devient indispensable.

- **Réception** obligatoire pour tous depuis le **01/09/2026** ; **émission** et **e-reporting** pour les PME/TPE au **01/09/2027** (GE et ETI depuis le 01/09/2026).
- L'administration recevra les données de facturation (B2B), de transaction (B2C, international) et de **paiement** (services) : à terme, elle pré-remplira la CA3. Toute incohérence entre factures émises/reçues, encaissements et déclarations sera immédiatement visible.
- Nouvelles mentions : SIREN du client, adresse de livraison, nature de l'opération (biens / services / mixte), option pour les débits.

---

## 13. Checklist de fin de module

- [ ] Je sais dire si une opération est hors champ, exonérée ou taxable, et où elle est taxable.
- [ ] Je maîtrise l'exigibilité : biens (livraison, acomptes depuis 2023), services (encaissement, option débits).
- [ ] Je connais les régimes (franchise, RSI, réel normal), leurs seuils (à vérifier chaque année) et le mécanisme de dépassement de la franchise depuis 2025.
- [ ] Je remplis une CA3 complète (A1, A3, A4, B2, E1, E2, E3, F2, 08, 09, 9B, 15, 16, 19, 20, 21, 22, 23, 24, 25-28) et une CA12 avec acomptes.
- [ ] Je connais les exclusions du droit à déduction (VP, carburants, logement, cadeaux).
- [ ] Je calcule un coefficient de déduction (assujettissement × taxation × admission) et la régularisation définitive.
- [ ] Je traite l'autoliquidation (import, AIC, services, sous-traitance BTP) et ses lignes CA3.
- [ ] Je vérifie les conditions d'une LIC (n° TVA valide, preuve du transport, état récapitulatif).
- [ ] Je sais quand basculer en OSS et remplir une déclaration OSS trimestrielle.
- [ ] Je calcule une TVA sur la marge pièce par pièce.
- [ ] Je traite l'option TVA sur loyers et la refacturation de la taxe foncière.
- [ ] Je demande un remboursement de crédit (3519) et je corrige une erreur sur une CA3 passée.
- [ ] Je fais un rapprochement CA comptable / CA déclaré / TVA collectée et j'explique les écarts.

## Références

- CGI : art. 256 à 260 (champ, territorialité, options), 261 et 262 (exonérations), 262 ter I (LIC), 266 à 267 (base), 269 (fait générateur et exigibilité), 271 à 273 (déductions), 278 à 281 (taux), 283 (redevables, autoliquidation), 287 (déclarations), 289 (factures), 292 (base à l'importation), 293 B (franchise), 297 A et 297 E (biens d'occasion), 298 sexdecies F et suivants (guichets OSS / IOSS), 302 septies A (RSI), 1695 II (autoliquidation à l'importation), 1727 à 1729 et 1788 A (sanctions).
- Annexe II au CGI : art. 205 à 207 (coefficient de déduction, régularisations), art. 242-0 A et suivants (remboursement de crédits), art. 242 nonies A (mentions des factures).
- Directive 2006/112/CE (directive TVA) ; règlement d'exécution (UE) n° 282/2011 (preuve du transport intracommunautaire).
- BOFiP : séries TVA-CHAMP, TVA-BASE, TVA-LIQ, TVA-DED, TVA-DECLA, TVA-SECT, TVA-IMM.

## À retenir en 30 secondes

- L'entreprise collecte la TVA sur ses ventes, récupère celle de ses achats et reverse la différence.
- Toujours trois questions dans l'ordre : concernée ? taxée en France ? exonérée ?
- Biens : TVA due à la livraison. Services : TVA due au paiement du client (sauf option pour les débits).
- Chaque client a un régime : franchise, réel simplifié (CA12) ou réel normal (CA3).
- Certaines TVA sur achats ne se récupèrent pas (voiture de tourisme, logement, cadeaux trop chers).
- Autoliquidation : le client déclare la TVA à la place du vendeur ; l'oublier est sanctionné.
- À chaque bilan, rapprochez CA comptable, CA déclaré et TVA collectée, et expliquez chaque écart.
