# Corrigé E13-11 — Le Petit Zinc : détournement d'espèces par un salarié découvert après l'arrêté des comptes

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E13-11](../exercices/E13-11_petit-zinc-detournement-caisse.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Question 1 — Le mécanisme.** Le client consomme et paie en espèces ; le barman encaisse puis **annule** le ticket et garde les espèces. Le **Z de caisse** du jour ne comprend donc pas ces ventes : le chiffre d'affaires comptabilisé (issu des Z), la TVA collectée déclarée et les espèces remises en banque sont **tous minorés du même montant**. Rien ne « détonne » en comptabilité : la caisse est juste… par rapport à un Z faux. Seuls les **journaux d'annulation** du logiciel certifié (qui doit tracer toute annulation) et les indicateurs (part des espèces, marge) trahissent la fraude.

**La TVA est-elle due ?** Oui. Les prestations de restauration ont **réellement été rendues** par la société, et le prix a été **payé** par les clients à son **préposé**, qui agissait pour elle. Le fait générateur et l'exigibilité sont intervenus ; le détournement est un événement **postérieur**, interne, qui ne réduit pas la base d'imposition. La société doit la TVA sur 13 200 € TTC de ventes, et subit une perte de 13 200 € (le prix TTC détourné).

**Question 3 — L'exercice clos.**
- **Comptablement** : le détournement a commencé avant le 30/06/2026, mais il a été **découvert après l'arrêté** des comptes (24/09). Les événements postérieurs à l'arrêté peuvent conduire la présidente à **arrêter de nouveaux comptes** avant l'assemblée si leur incidence est significative. Ici, l'effet net sur le résultat 2025/2026 est **faible** : + 7 100 € de ventes et − 7 920 € de perte, soit − 820 € (la TVA), à comparer à un résultat de 41 200 €. On **ne rouvre pas** les comptes ; on **informe** l'assemblée (rapport de gestion / communication aux associés : événement postérieur à la clôture) et on traite l'ensemble dans les comptes 2026/2027 (correction d'erreur comptabilisée dans le résultat de l'exercice de découverte, par nature — la nomenclature 2025 du PCG ne prévoyant plus de comptes de produits sur exercices antérieurs en exceptionnel ; *à vérifier dans le plan de comptes*).
- **Fiscalement** : la règle comptable n'efface pas la règle fiscale. Les **recettes** de mars à juin 2026 sont des créances acquises de l'exercice 2025/2026 : elles doivent être **imposées sur cet exercice** → **déclaration rectificative** (2065 et 2033/2050 rectificatives). La **perte** n'était pas connue à la clôture : selon la jurisprudence du Conseil d'État, la perte résultant d'un détournement est déductible au titre de l'exercice au cours duquel il est **découvert** (position retenue ici, prudente — *à valider avec Hélène au vu de la jurisprudence la plus récente*). D'où une asymétrie temporaire : produits imposés en 2025/2026, perte déduite en 2026/2027.
- **TVA** : régularisation spontanée sur une **CA3 ultérieure** (octobre 2026), en distinguant les périodes d'origine, ou par déclarations rectificatives ; l'intérêt de retard (CGI art. 1727) est dû sur la TVA omise de mars à septembre (*réduction possible en cas de régularisation spontanée selon les conditions légales — à vérifier*).

**Question 5 — Déductibilité.** Les pertes résultant de détournements commis par des **salariés** sont déductibles, **sauf** si elles résultent d'une **carence manifeste** des dirigeants dans l'organisation des contrôles, ou s'ils y ont participé ou en ont profité (jurisprudence constante du Conseil d'État). Ici : un seul salarié, une fraude découverte par la direction elle-même au bout de 7 mois, un logiciel certifié en place. On peut soutenir l'absence de carence manifeste, mais l'administration pourrait objecter qu'aucune revue des annulations n'était faite : **documenter** les contrôles existants et les mesures prises.

**Question 4 — L'assurance.** L'indemnité ne pourra être comptabilisée en produit que lorsqu'elle sera **acquise** (accord de l'assureur sur le principe et le montant) ; à la date de l'écriture, ce n'est pas le cas (déclaration en cours, plainte à déposer). Estimation : min(13 200 ; 10 000) − 1 500 = **8 500 €** (*sous réserve des conditions du contrat et de l'appréciation de l'assureur — par sinistre et par année d'assurance*). On la mentionne en annexe 2026/2027 si elle n'est pas acquise à la clôture.

## 2. Calculs (détaillés, chaque montant justifié)

| | Exercice 2025/2026 (mars-juin) | Exercice 2026/2027 (juillet-septembre) | Total |
|---|---|---|---|
| Ventes à 10 % TTC | 6 600,00 | 4 400,00 | 11 000,00 |
| → HT / TVA | 6 000,00 / 600,00 | 4 000,00 / 400,00 | 10 000,00 / 1 000,00 |
| Ventes à 20 % TTC | 1 320,00 | 880,00 | 2 200,00 |
| → HT / TVA | 1 100,00 / 220,00 | 733,33 / 146,67 | 1 833,33 / 366,67 |
| **CA HT omis** | **7 100,00** | **4 733,33** | **11 833,33** |
| **TVA omise** | **820,00** | **546,67** | **1 366,67** |
| **Montant détourné (TTC)** | **7 920,00** | **5 280,00** | **13 200,00** |

Ordre de grandeur : 13 200 € sur 7 mois de CA (≈ 820 000 × 7/12 × 1,1 TTC moyen) ≈ 2,5 % des encaissements — c'est le seuil typique où une revue des annulations doit alerter.

**IS supplémentaire 2025/2026** (résultat fiscal 38 400 € + 7 100 € = 45 500 €) :
- part restant dans la tranche à 15 % : 42 500 − 38 400 = 4 100 € × 15 % = 615,00 € ;
- part au-delà : 45 500 − 42 500 = 3 000 € × 25 % = 750,00 € ;
- **IS supplémentaire : 1 365,00 €** (plus intérêt de retard).

**Effet sur le résultat comptable 2026/2027** : 4 733,33 + 7 100,00 − 13 200,00 = **− 1 366,67 €** (= la TVA, coût définitif de la fraude avant assurance).

**Retraitement fiscal 2026/2027** : déduction extra-comptable des **7 100,00 €** de ventes 2025/2026 comptabilisées en 2026/2027 mais déjà imposées en 2025/2026 (sinon double imposition). Effet fiscal 2026/2027 : − 1 366,67 − 7 100,00 = **− 8 466,67 €** ; sur les deux exercices : + 7 100,00 − 8 466,67 = **− 1 366,67 €** ✓.

## 3. Écritures comptables

*Exercice 2026/2027 (écritures passées en octobre 2026)*

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 05/10/2026 | OD | 4678 | Débiteurs divers – D. Ferrière (détournement) | Ventes espèces détournées juil.-sept. 2026 | 5 280,00 | |
| 05/10/2026 | OD | 7061 | Ventes restauration (10 %) | Ventes annulées frauduleusement juil.-sept. 2026 | | 4 000,00 |
| 05/10/2026 | OD | 7062 | Ventes boissons (20 %) | Ventes annulées frauduleusement juil.-sept. 2026 | | 733,33 |
| 05/10/2026 | OD | 44571 | TVA collectée | TVA sur ventes détournées juil.-sept. 2026 | | 546,67 |
| 05/10/2026 | OD | 4678 | Débiteurs divers – D. Ferrière (détournement) | Ventes espèces détournées mars-juin 2026 (exercice clos) | 7 920,00 | |
| 05/10/2026 | OD | 7061 | Ventes restauration (10 %) | Correction d'erreur – ventes mars-juin 2026 | | 6 000,00 |
| 05/10/2026 | OD | 7062 | Ventes boissons (20 %) | Correction d'erreur – ventes mars-juin 2026 | | 1 100,00 |
| 05/10/2026 | OD | 44571 | TVA collectée | TVA sur ventes détournées mars-juin 2026 | | 820,00 |
| 05/10/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation créance détournement D. Ferrière | 13 200,00 | |
| 05/10/2026 | OD | 496 | Dépréciations des comptes de débiteurs divers | Dépréciation créance détournement D. Ferrière | | 13 200,00 |
| | | | | **Totaux** | **26 400,00** | **26 400,00** |

*Les ventes 2025/2026 peuvent être isolées dans des sous-comptes « correction d'erreur – exercice antérieur » pour faciliter le retraitement fiscal et l'information en annexe. La TVA de 1 366,67 € figure sur la CA3 d'octobre 2026 (régularisation, avec détail par période en note). Quand l'assureur aura donné son accord : D 4687 Produits à recevoir / C 7588 Indemnités d'assurance (*subdivision selon la nomenclature 2025*) ; à l'encaissement D 512 / C 4687. Toute somme récupérée auprès de D. Ferrière : D 512 / C 4678 et reprise de la dépréciation à due concurrence. La créance sera passée en perte (654 / reprise de la dépréciation) lorsque le recouvrement sera définitivement impossible.*

*Exercice 2025/2026* : pas d'écriture (comptes arrêtés, non rouverts) ; liasse et 2065 rectificatives intégrant 7 100,00 € de recettes ; information des associés à l'assemblée du 15/12/2026.

## 4. Points d'attention / pièges

- **« Le client n'a rien encaissé, donc pas de TVA »** : faux. La société a encaissé par l'intermédiaire de son salarié ; la TVA est due.
- **Ne pas compenser** vente omise et perte en une seule écriture « nette » : on perdrait la traçabilité (CA, TVA, créance, dépréciation, assurance, recouvrement).
- **Double imposition** des ventes 2025/2026 si l'on oublie la déduction extra-comptable en 2026/2027 après la rectificative.
- **Délai de déclaration à l'assureur** : 5 jours ouvrés après la découverte (05/10) → au plus tard le **12/10/2026**. Urgent.
- **Pas de retenue sur salaire** : les sanctions pécuniaires sont interdites (C. trav. art. L. 1331-2) ; et la responsabilité pécuniaire du salarié envers l'employeur, devant le juge prud'homal, suppose une **faute lourde** (intention de nuire). La voie de récupération est la **constitution de partie civile** dans le cadre de la plainte pour **abus de confiance** (C. pén. art. 314-1), ou une reconnaissance de dette librement signée.
- **Mise à pied conservatoire et procédure** : la faute grave doit être sanctionnée dans un délai restreint ; convocation à entretien préalable rapide ; ne pas accuser publiquement le salarié (diffamation), s'appuyer sur les faits (rapports de caisse, vidéos — sous réserve de la licéité du dispositif de vidéosurveillance : information des salariés et du CSE le cas échéant).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 6 — Plan d'action pour Clara Rossi et Hugo Lemoine :**
1. **Aujourd'hui** : conserver les preuves (export horodaté et signé des journaux de caisse, sauvegarde des vidéos avant leur effacement automatique) ; ne pas modifier le paramétrage de la caisse avant l'export.
2. **Plainte** pour abus de confiance (commissariat ou procureur), indispensable pour l'assureur et la constitution de partie civile.
3. **Déclaration de sinistre** à l'assureur avant le 12/10/2026.
4. **Procédure disciplinaire** avec l'avocat en droit social (faute grave ; faute lourde si l'intention de nuire est établie).
5. **Contrôle interne** : annulation après encaissement possible uniquement avec le badge d'un responsable ; rapport quotidien des annulations par opérateur revu par Hugo ; comptage de caisse « à l'aveugle » en fin de service ; suivi mensuel de la part des espèces et du ticket moyen par serveur ; rotation des postes.

**Question 7 — Le cabinet (réponse préparée pour Hélène) :** la mission de présentation des comptes n'a **pas pour objet** de détecter les fraudes (assurance modérée, contrôles de cohérence) ; la lettre de mission le précise. Le dossier montre pourtant un indice : la baisse de la part des espèces (31 % vs 35 %), acceptée sur une explication orale. Bonne pratique désormais : (a) **documenter** que la revue analytique a été faite et l'explication obtenue ; (b) ajouter au programme de travail des clients à forte part d'espèces une **revue des annulations** et des tickets en attente ; (c) **informer par écrit** les dirigeants des faiblesses de contrôle interne relevées (lettre de recommandations) ; (d) prévenir l'**assureur RC professionnelle** du cabinet si le client met en cause le cabinet (déclaration de circonstance, selon le contrat). Le cabinet n'a pas d'obligation de déclaration à Tracfin dans cette situation (la société est **victime** ; pas de soupçon de blanchiment par le client), mais il reste vigilant.

**Mail de synthèse au client (extrait) :**

> Le préjudice chiffré à partir de la caisse est de **13 200 €** (mars à septembre 2026). Les ventes correspondantes restent imposables : **1 366,67 €** de TVA et environ **1 365 €** d'IS sur l'exercice clos sont à régulariser ; la perte est en revanche déductible sur l'exercice en cours. Votre assurance pourrait couvrir jusqu'à **8 500 €** (plafond 10 000 €, franchise 1 500 €) : la déclaration doit partir **avant le 12 octobre** et suppose une plainte. Nous préparons les déclarations rectificatives ; nous vous proposons un rendez-vous jeudi pour les mesures de contrôle de la caisse.

**Documentation du dossier** : exports de caisse signés, tableau de chiffrage, copie de la plainte, déclaration de sinistre, PV de l'assemblée mentionnant l'événement postérieur, déclarations rectificatives (TVA, IS) et justification de la déduction de la perte (absence de carence manifeste : description des contrôles existants), lettre de recommandations.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- CGI art. 256, 266 et 269 (base et exigibilité de la TVA) ; art. 38 et 39 (rattachement des produits, déduction des pertes) ; art. 1727 (intérêt de retard) ; art. 286, I-3° bis (logiciels de caisse sécurisés).
- Jurisprudence du Conseil d'État : déductibilité des pertes résultant de détournements commis par des salariés, sauf carence manifeste des dirigeants ; rattachement à l'exercice de découverte (*à vérifier au vu des décisions les plus récentes*).
- PCG : événements postérieurs à la clôture, corrections d'erreurs (comptabilisées dans le résultat de l'exercice de découverte), dépréciation des créances.
- Code de commerce art. L. 232-1 (rapport de gestion : événements importants survenus depuis la clôture).
- Code du travail art. L. 1331-2 (interdiction des sanctions pécuniaires), L. 1332-2 et suivants (procédure disciplinaire) ; Code pénal art. 314-1 (abus de confiance).
- Norme professionnelle de l'Ordre relative à la mission de présentation des comptes (NP 2300).
