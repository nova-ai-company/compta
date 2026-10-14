# Corrigé E09-12 — Bâtisseurs du Sud : « Mettez 100 000 € de provisions, on a fait une trop belle année »

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-12](../exercices/E09-12_lissage-batisseurs-du-sud.md)

## 1. Analyse

### 1.1 Les trois provisions demandées par Karim

Rappel des conditions : **(1)** une obligation envers un tiers née d'un **événement passé**, **(2)** une sortie de ressources **probable** sans contrepartie, **(3)** une estimation **fiable**.

| Demande | (1) Obligation / événement passé | (2) Probable | (3) Fiable | Conclusion |
|---|---|---|---|---|
| « Risques divers » 60 000 € | **Aucune** obligation identifiée ; « on ne sait jamais » n'est pas un événement passé | — | Montant arbitraire | **Refus** |
| « Baisse d'activité 2027 » 40 000 € | **Aucune** : des pertes d'exploitation **futures** ne sont pas une obligation envers un tiers. Le PCG interdit expressément de provisionner les pertes opérationnelles futures | — | — | **Refus** |
| « Congés payés » 35 000 € | Dans le BTP, les salariés sont indemnisés par la **caisse de congés payés**, à laquelle l'entreprise verse des **cotisations**. L'obligation de l'employeur est éteinte par le paiement de ces cotisations. Seules les cotisations dues sur les salaires de la période et non encore payées constituent une **charge à payer** (déjà traitée par la paie) | — | — | **Refus** de la provision ; contrôle des cotisations à payer à la caisse |

### 1.2 Les dossiers de Nadia (provisions justifiées)

**Chantier Les Acacias — perte à terminaison.** Le contrat est **déficitaire** : coût total estimé de 512 000 € pour un prix de 480 000 €, soit une perte de 32 000 €. Le PCG impose de **provisionner la totalité de la perte à terminaison** dès qu'elle est **probable**, quel que soit l'avancement. Avec la méthode à l'avancement, une partie de la perte est déjà dans le résultat : CA reconnu 288 000 € – coûts engagés 307 200 € = – 19 200 €, soit 60 % × 32 000 €. On ne provisionne que le **solde non encore constaté**.

**Litige Résidence du Parc.** La réception de 2025 et l'exécution défectueuse sont l'**événement passé**. L'assignation est délivrée et l'expertise judiciaire **retient la responsabilité** : la sortie est **hautement probable**, et le montant de 18 000 € est **chiffré par l'expert**. Le désordre n'est pas couvert par l'assurance, donc il n'y a pas de remboursement à attendre. Provision **justifiée**.

Ironie de la situation : Karim voulait 135 000 € de provisions injustifiées, alors que le dossier contenait **30 800 € de provisions parfaitement justifiées**, que personne n'avait comptabilisées.

## 2. Calculs

**Perte à terminaison :**

| Élément | Montant |
|---|---|
| Prix du marché | 480 000,00 € |
| Coût total estimé | 512 000,00 € |
| **Perte à terminaison** | **– 32 000,00 €** |
| Perte déjà constatée via l'avancement : 288 000 – 307 200 | – 19 200,00 € |
| **Provision pour perte à terminaison (solde)** | **12 800,00 €** |

Contrôle : 32 000 × (1 – 60 %) = 12 800 €.

**Litige :** **18 000,00 €**.

**Effet sur le résultat :** – 30 800,00 € → résultat avant IS d'environ 279 200 € (310 000 – 30 800).

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/12/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Perte à terminaison chantier Les Acacias (solde 40 %) | 12 800,00 | |
| 31/12/2026 | OD | 1517 | Provisions pour pertes sur contrats | Perte à terminaison Les Acacias | | 12 800,00 |
| 31/12/2026 | OD | 6815 | Dotations aux provisions d'exploitation | Litige Synd. copro. Résidence du Parc (expertise judiciaire) | 18 000,00 | |
| 31/12/2026 | OD | 1511 | Provisions pour litiges | Litige Résidence du Parc | | 18 000,00 |
| | | | | **Totaux** | **30 800,00** | **30 800,00** |

Fiscalement, les deux provisions sont **déductibles** : pertes nettement précisées, probables, chiffrées, et charges futures déductibles. La provision pour perte à terminaison est admise pour la perte afférente aux travaux restant à exécuter.

## 4. Points d'attention / pièges

**Les risques d'une provision de « lissage » :**

| Domaine | Conséquence |
|---|---|
| **Comptable** | Comptes **ni réguliers ni sincères**, qui ne donnent pas une image fidèle (art. L. 123-14 C. com.). Le résultat 2026 serait minoré, puis le résultat 2027 artificiellement gonflé par la reprise : c'est précisément ce que l'image fidèle interdit |
| **Pénal** | Pour les dirigeants de SAS, la **présentation de comptes annuels ne donnant pas une image fidèle** en vue de dissimuler la véritable situation est un **délit** (art. L. 242-6, 2° C. com., applicable aux SAS par renvoi de l'art. L. 244-1) |
| **Fiscal** | Provisions **non déductibles** (art. 39, 1-5° CGI : pas de perte nettement précisée ni probable) → **réintégration**, **intérêts de retard** et, s'agissant d'une démarche délibérée, **majoration de 40 % pour manquement délibéré** (art. 1729 CGI). Si on les réintègre spontanément, elles n'ont plus aucun intérêt fiscal |
| **Groupe et partenaires** | Comptes faussés transmis aux banques, aux assureurs crédit et à l'organisme de qualification ; incohérence avec les comptes de Delta Invest |
| **Déontologique** | L'expert-comptable doit refuser de passer des écritures qu'il sait contraires aux règles ; sa responsabilité civile et disciplinaire est engagée. Sa mission de présentation ne peut pas aboutir à une attestation de cohérence et de vraisemblance sur des comptes qu'il sait inexacts |

**Pourquoi le lissage n'a pas l'intérêt fiscal imaginé (question 5) :** Bâtisseurs du Sud est dans le **groupe intégré** de Delta Invest. L'IS est calculé sur le **résultat d'ensemble**, où le bénéfice de Bâtisseurs est déjà **compensé par le déficit de la Menuiserie** (perte 2026). Selon la convention d'intégration, Bâtisseurs verse en général à Delta l'IS qu'elle aurait payé seule, mais l'économie de groupe existe déjà. Surtout, le taux d'IS est le même en 2026 et en 2027 : un décalage d'une année n'économise **rien**, il ne fait que déplacer l'impôt, au prix des risques ci-dessus.

**Autres pièges :**
- **Congés payés BTP** : ne jamais provisionner les congés payés d'une entreprise affiliée à une caisse de congés payés. Vérifier en revanche les **cotisations dues à la caisse** sur les salaires de décembre (charge à payer).
- **Perte à terminaison** : provisionner **la totalité** de la perte, mais déduire ce que la méthode à l'avancement a déjà fait passer en résultat. Sinon, la perte est comptée deux fois.
- **Retenues de garantie de 5 %** : ce sont des créances, pas des provisions. On les déprécie seulement si une levée de réserves est contestée.
- **Garantie décennale** : les désordres décennaux sont couverts par l'assurance. On ne provisionne que la **franchise** ou les désordres non couverts, comme ici.

## 5. Ce qu'un senior ferait en plus

**Leviers légaux à proposer à Karim** (chaque dispositif est à vérifier dans ses conditions et plafonds de l'année) :
- **Épargne salariale** : un accord d'**intéressement** pour 2027 doit être conclu **avant le premier jour de la seconde moitié** de la période de calcul ; abondement à un plan d'épargne ; **prime de partage de la valeur** selon les règles en vigueur. Ces dispositifs sont déductibles et fidélisent les équipes ;
- **Investissements utiles** (matériel de chantier), à décider pour leur intérêt économique et non pour l'IS. Un achat le 20 décembre ne génère que quelques jours d'amortissement ;
- **Rémunération du président et politique de dividendes** à arbitrer au niveau du groupe avec Delta Invest ;
- **Revue des vraies provisions** : litiges, pertes à terminaison, dépréciations de créances (retenues de garantie contestées, clients en difficulté), avec pièces justificatives. C'est ce qu'on vient de faire, et cela représente 30 800 €.

**Documentation du dossier :** conserver le courriel de Karim et la réponse écrite du cabinet. En cas de contrôle ou de litige, la trace du refus protège le cabinet.

**Réponse écrite d'Hélène (à Karim, copie Nadia) :**
> « Bonjour Karim,
> Nous comprenons votre souci d'anticiper une année 2027 plus difficile, mais nous ne pouvons pas comptabiliser les trois provisions demandées. Une provision n'est possible que pour une obligation déjà née, envers un tiers, et dont le coût est probable et chiffrable (règles du Plan comptable général). Ce n'est le cas ni des "risques divers", ni d'une baisse d'activité future. Quant aux congés payés, ils sont pris en charge par la caisse de congés payés du BTP, à laquelle vous cotisez déjà.
> Comptabiliser ces provisions rendrait les comptes inexacts, ce qui engagerait votre responsabilité de président (présentation de comptes infidèles) et la nôtre. Elles seraient en outre réintégrées par l'administration, avec intérêts de retard et une majoration de 40 %. Enfin, votre société est intégrée fiscalement avec Delta Invest : les pertes de la Menuiserie réduisent déjà l'impôt du groupe, et décaler du résultat d'une année n'économise rien.
> En revanche, la revue des dossiers de Nadia fait apparaître 30 800 € de provisions justifiées, que nous comptabilisons : la perte prévisible sur le chantier Les Acacias (12 800 €) et le litige de la Résidence du Parc (18 000 €). Nous vous proposons aussi un rendez-vous en janvier pour étudier la mise en place d'un accord d'intéressement pour 2027.
> Bien cordialement, Hélène Ferrand »

## 6. Références

- Code de commerce, art. L. 123-14 (régularité, sincérité, image fidèle), L. 123-20 (prudence), L. 242-6, 2° et L. 244-1 (présentation de comptes infidèles par les dirigeants de SAS).
- PCG (règlement ANC n° 2014-03 modifié) : définition des passifs, interdiction de provisionner les pertes opérationnelles futures, contrats à long terme (méthode à l'avancement, provision pour perte à terminaison).
- CGI, art. 39, 1-5° (provisions), art. 1727 et 1729 (intérêts de retard, majoration pour manquement délibéré), art. 223 A et suivants (intégration fiscale).
- Code du travail : caisses de congés payés du BTP ; Code du travail, livre III de la 3e partie (intéressement, participation, épargne salariale).
- Ordonnance n° 45-2138 du 19 septembre 1945 et code de déontologie des professionnels de l'expertise comptable.
