# Corrigé E11-07 — SCI Les Tilleuls : répartition du résultat entre associés et parts démembrées

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-07](../exercices/E11-07_repartition-resultat-sci-tilleuls-demembrement.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Une SCI n'est pas une SARL** : pas de réserve légale, pas de dividendes au sens fiscal (la SCI à l'IR est **translucide** : chaque associé est imposé sur sa quote-part du résultat **fiscal**, qu'il soit distribué ou non), pas de PFNL ni de 2777. Juridiquement, en revanche, les bénéfices n'appartiennent aux associés qu'après **approbation des comptes** et décision d'affectation.

**Le démembrement** : sur 50 parts, Julien est **usufruitier** et Léa **nue-propriétaire** depuis le 15/11/2026.
- **Bénéfice de l'exercice** = « fruit » de la part → revient à l'**usufruitier** (statuts art. 20, conforme à la règle civile). Peu importe que le démembrement date de novembre : Julien était plein propriétaire avant, usufruitier après ; dans les deux cas le bénéfice courant lui revient.
- **Réserves** = bénéfices antérieurs mis en réserve, ils ont accru la **substance** de la part → ils reviennent en principe au **nu-propriétaire** ; mais lorsqu'ils sont **distribués**, l'usufruitier exerce son droit de jouissance sous forme de **quasi-usufruit** : il reçoit les sommes et devra en **restituer la valeur** au nu-propriétaire à la fin de l'usufruit (jurisprudence de la Cour de cassation, chambre commerciale, 2015 ; reprise ici par l'article 20 des statuts), **sauf convention contraire** entre eux notifiée à la société — il n'y en a pas.

**Question 1 — Convocation et vote** : le nu-propriétaire et l'usufruitier ont tous deux le **droit de participer** aux décisions collectives (art. 1844 C. civ., et art. 14 des statuts) → **Léa doit être convoquée**, tout comme Paul, Emma et Julien. Le **vote** sur les résolutions ordinaires (approbation, affectation, distribution de réserves, pouvoirs) appartient à l'**usufruitier** pour les parts 151 à 200 (art. 14) : Julien vote, Léa assiste et peut s'exprimer.

| Résolution | Paul (100 voix) | Emma (50 voix) | Parts 151-200 (50 voix) |
|---|---|---|---|
| 1. Approbation des comptes | Vote | Vote | **Julien** vote ; Léa participe sans voter |
| 2. Affectation du résultat | Vote | Vote | **Julien** |
| 3. Distribution de réserves | Vote | Vote | **Julien** (décision ordinaire selon art. 14) |
| 4. Pouvoirs | Vote | Vote | **Julien** |

> Une distribution de réserves touche aux droits du nu-propriétaire : même si les statuts confèrent le vote à l'usufruitier, la jurisprudence sanctionne une décision qui priverait le nu-propriétaire de la substance de ses droits. Ici, le quasi-usufruit préserve la créance de restitution de Léa : la décision est régulière.

## 2. Calculs (détaillés, chaque montant justifié)

**(a) Bénéfice 2026 : 5 020,00 €** — réparti au prorata des parts (200 parts → 25,10 € par part)

| Bénéficiaire | Parts | Calcul | Montant |
|---|---|---|---|
| Paul Garnier | 100 | 5 020 × 100/200 | 2 510,00 |
| Emma Garnier | 50 | 5 020 × 50/200 | 1 255,00 |
| Julien Garnier (usufruitier des parts 151-200) | 50 | 5 020 × 50/200 | 1 255,00 |
| **Total** | **200** | | **5 020,00** |

**(b) Distribution de réserves : 12 000,00 €** (60 € par part)

| Bénéficiaire | Parts | Montant | Observation |
|---|---|---|---|
| Paul Garnier | 100 | 6 000,00 | Pleine propriété |
| Emma Garnier | 50 | 3 000,00 | Pleine propriété |
| Julien Garnier, **quasi-usufruitier** | 50 | 3 000,00 | Créance de restitution de **3 000,00 €** au profit de Léa à l'extinction de l'usufruit |
| **Total** | **200** | **12 000,00** | |

Réserves après distribution : 36 000 – 12 000 = **24 000,00 €**. Trésorerie : 21 400 € disponibles le 20/05/2027 → la distribution de 12 000 € est payable ; les 5 020 € restent en comptes courants (retirables ultérieurement selon la trésorerie : échéances d'emprunt, taxe foncière d'octobre, provisions de copropriété).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 10/06/2027 | OD | 120 | Résultat de l'exercice (bénéfice) | Affectation résultat 2026 – AG du 10/06/2027 | 5 020,00 | |
| 10/06/2027 | OD | 4551 | Compte courant Paul Garnier | Quote-part résultat 2026 (100 parts) | | 2 510,00 |
| 10/06/2027 | OD | 4552 | Compte courant Emma Garnier | Quote-part résultat 2026 (50 parts) | | 1 255,00 |
| 10/06/2027 | OD | 4553 | Compte courant Julien Garnier | Quote-part résultat 2026 – usufruit parts 151-200 | | 1 255,00 |
| 10/06/2027 | OD | 1068 | Réserves | Distribution de réserves – 3e résolution AG 10/06/2027 | 12 000,00 | |
| 10/06/2027 | OD | 4551 | Compte courant Paul Garnier | Distribution de réserves (100 parts) | | 6 000,00 |
| 10/06/2027 | OD | 4552 | Compte courant Emma Garnier | Distribution de réserves (50 parts) | | 3 000,00 |
| 10/06/2027 | OD | 4553 | Compte courant Julien Garnier | Distribution de réserves – quasi-usufruit (parts 151-200, NP Léa Garnier) | | 3 000,00 |
| 30/06/2027 | BQ | 4551 | Compte courant Paul Garnier | Paiement distribution de réserves | 6 000,00 | |
| 30/06/2027 | BQ | 4552 | Compte courant Emma Garnier | Paiement distribution de réserves | 3 000,00 | |
| 30/06/2027 | BQ | 4553 | Compte courant Julien Garnier | Paiement distribution de réserves (quasi-usufruit) | 3 000,00 | |
| 30/06/2027 | BQ | 512 | Banque | Vir. distribution de réserves | | 12 000,00 |
| | | | | **Totaux** | **29 020,00** | **29 020,00** |

> La créance de restitution de Léa sur Julien (3 000 €) est une affaire **entre eux** : elle n'apparaît pas dans les comptes de la SCI. Le cabinet en garde trace dans le dossier juridique (PV, tableau de suivi des sommes soumises à quasi-usufruit).

## 4. Points d'attention / pièges

- **Pas de 2777, pas de PFNL, pas d'IFU** : la SCI à l'IR ne verse pas de revenus de capitaux mobiliers ; ses associés sont imposés via la 2072, que l'argent soit distribué ou non.
- **Ne pas imposer deux fois** : la distribution de réserves (résultats antérieurs déjà déclarés sur les 2072 des années concernées) n'est **pas** un revenu imposable.
- **Résultat comptable ≠ résultat fiscal** : 5 020 € de bénéfice comptable en 2026, mais un **déficit foncier** sur la 2072 (E10-10 : travaux, pas d'amortissement fiscal, régime des revenus fonciers). L'imposition des associés suit la **2072**, pas l'affectation comptable.
- **Démembrement et 2072** : la quote-part du résultat **fiscal** courant afférente aux parts démembrées est imposée chez l'**usufruitier** (Julien), y compris l'imputation de sa quote-part de déficit foncier ; Léa figure sur l'annexe de la 2072 comme nue-propriétaire, sans quote-part de résultat courant (*présentation de l'annexe 2072-S à vérifier*).
- **Convocation de la nue-propriétaire** : l'oublier expose la décision à une contestation.
- **Quasi-usufruit** : il est de droit (statuts + jurisprudence) sauf convention contraire **notifiée** à la société ; la société paie donc **l'usufruitier**, et non le nu-propriétaire.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Projets de résolutions (question 4)**

> **Première résolution — Approbation des comptes.** L'assemblée générale, après avoir entendu la lecture du rapport de la gérance, approuve les comptes de l'exercice clos le 31 décembre 2026 tels qu'ils lui ont été présentés, se soldant par un bénéfice de 5 020,00 €, ainsi que les opérations traduites dans ces comptes.
>
> **Deuxième résolution — Affectation du résultat.** L'assemblée générale décide, conformément à l'article 20 des statuts, de répartir le bénéfice de l'exercice, soit 5 020,00 €, entre les associés proportionnellement à leurs droits, soit 25,10 € par part, et de le porter au crédit de leurs comptes courants : M. Paul Garnier 2 510,00 € ; Mme Emma Garnier 1 255,00 € ; M. Julien Garnier, usufruitier des parts n° 151 à 200, 1 255,00 €.
>
> **Troisième résolution — Distribution de réserves.** L'assemblée générale décide de distribuer une somme de 12 000,00 €, soit 60,00 € par part, prélevée sur le poste « Réserves », qui est ainsi ramené de 36 000,00 € à 24 000,00 €. Conformément à l'article 20 des statuts, la quote-part afférente aux parts n° 151 à 200, soit 3 000,00 €, est versée à M. Julien Garnier, usufruitier, qui en a la jouissance sous forme de quasi-usufruit, à charge d'en restituer la valeur à Mme Léa Garnier, nue-propriétaire, à l'extinction de l'usufruit. La distribution sera mise en paiement le 30 juin 2027.
>
> **Quatrième résolution — Pouvoirs.** L'assemblée générale confère tous pouvoirs au porteur d'un original, d'une copie ou d'un extrait du présent procès-verbal pour accomplir toutes formalités.
>
> *Pour chaque résolution, les voix attachées aux parts n° 151 à 200 sont exprimées par M. Julien Garnier, usufruitier ; Mme Léa Garnier, nue-propriétaire, régulièrement convoquée, a assisté à l'assemblée.*

**Réponse à Léa (question 3)**

> Madame,
> Vous serez bien convoquée à l'assemblée du 10 juin 2027 : en qualité de nue-propriétaire, vous avez le droit d'y participer. En revanche, les statuts (articles 14 et 20) réservent le vote des décisions ordinaires à l'usufruitier et prévoient que les réserves distribuées sont versées à l'usufruitier, qui en a la jouissance sous forme de **quasi-usufruit** : la société versera donc 3 000 € à M. Julien Garnier, qui vous en devra la **restitution** à la fin de l'usufruit. Cette créance vous est acquise. Si vous convenez avec votre père d'une autre répartition (par exemple un versement direct à votre profit), il vous suffit de nous notifier une convention signée par vous deux avant la mise en paiement.
> Nous vous conseillons, avec votre père, de **formaliser la créance de restitution par un acte** (convention de quasi-usufruit), utile notamment au plan civil et successoral — votre notaire pourra vous conseiller.

**Réponse à Paul (question 6)** : « Pas de 2777 : elle concerne les dividendes des sociétés soumises à l'IS. La SCI étant à l'IR, chacun d'entre vous est imposé sur sa part du résultat **fiscal** de la 2072 (en 2026, un déficit foncier grâce aux travaux), que l'argent soit distribué ou non ; les 12 000 € de réserves distribués ne sont pas imposés une seconde fois. »

**Contrôles et dossier** :
- Copie de l'acte de donation et de sa **signification** à la SCI dans le dossier juridique ; mise à jour du registre des associés (parts 151-200 : US Julien / NP Léa) et des **bénéficiaires effectifs** (le nu-propriétaire et l'usufruitier peuvent devoir y figurer selon leurs droits — *à vérifier*).
- Vérifier la **trésorerie** après paiement (21 400 – 12 000 = 9 400 €) au regard des échéances d'emprunt et de la taxe foncière.
- Dépôt des comptes : **non requis** pour une SCI (société civile) ; PV signé et conservé au registre des décisions.
- Mettre à jour le tableau de suivi des comptes courants (Paul 2 510 €, Emma 1 255 €, Julien 1 255 € après paiement).

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code civil : art. 578 et suivants (usufruit), art. 587 (quasi-usufruit sur les choses consomptibles, dont les sommes d'argent), art. 1844 (participation et droit de vote de l'usufruitier et du nu-propriétaire), art. 1844-1 (répartition des bénéfices au prorata des apports, sauf clause contraire), art. 1855-1856 (approbation des comptes des sociétés civiles).
- Jurisprudence : Cour de cassation, chambre commerciale, 27 mai 2015 (quasi-usufruit de l'usufruitier sur les réserves distribuées) — *référence à vérifier*.
- CGI : art. 8 (translucidité des sociétés de personnes), art. 28 et suivants (revenus fonciers), art. 156-I-3° (déficit foncier) ; déclaration 2072.
- BOFiP : RFPI – sociétés immobilières non soumises à l'IS – démembrement des parts.
