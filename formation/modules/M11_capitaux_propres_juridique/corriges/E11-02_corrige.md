# Corrigé E11-02 — Studio Pixel : l'appel et la libération du solde du capital

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E11-02](../exercices/E11-02_liberation-solde-studio-pixel.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

**Le fil logique d'un appel de capital** : (1) une **décision** du président fixe le montant et la date limite (création d'une créance de la société sur chaque associé, compte 4562) ; (2) les **versements** éteignent cette créance ; (3) le capital passe de « non appelé » (1011) à « appelé versé » (1013). Aucun de ces mouvements ne touche le résultat ni la TVA : ce sont des opérations **en capital**, hors champ de la TVA.

**Anomalie 1 — Décision non comptabilisée.** Le 109 (2 000 € débiteur) et le 1011 (2 000 € créditeur) n'ont pas bougé : l'appel du 02/06/2026 n'a jamais été saisi. La balance laisse croire que le capital n'est toujours pas entièrement libéré — ce qui serait faux et coûteux (taux réduit d'IS, voir question 5).

**Anomalie 2 — Versement de Léo en compte courant.** Le libellé dit pourtant « SOLDE CAPITAL ». Conséquence : le compte courant de Léo est **surévalué** de 1 000 € (3 230,80 € au lieu de 2 230,80 €) — la société semble lui devoir 1 000 € de trop, qu'il pourrait se faire « rembourser » : ce serait un **remboursement d'apport en capital** déguisé.

**Anomalie 3 — Versement de Sarah enregistré comme une vente.** La règle automatique « VIR … PIXEL = client » a transformé un apport en capital en chiffre d'affaires :
- **résultat** surévalué de 833,33 € ;
- **TVA collectée à tort** de 166,67 €, **déjà déclarée et payée** sur la CA3 de juin ;
- capital libéré sous-évalué.

**Régularisation de la TVA.** Une TVA déclarée à tort n'est pas « perdue » : elle se régularise sur une déclaration ultérieure (dans le délai de réclamation), en la portant en **TVA déductible / régularisation** sur la CA3 du mois de la correction (ou en minorant la TVA brute selon la ligne prévue par le formulaire). On la régularise ici sur la **CA3 d'octobre 2026** (déposée en novembre), avec une note au dossier. Comme il n'y a **pas eu de facture** émise avec TVA, aucune facture rectificative n'est nécessaire.

## 2. Calculs (détaillés, chaque montant justifié)

- Appel : 100 actions × 10 € × 2 associés = **2 000,00 €**.
- Montant mal enregistré chez Sarah : 1 000,00 € TTC décomposé par l'outil en 1 000 / 1,20 = **833,33 €** HT + **166,67 €** de TVA.
- Compte courant de Léo corrigé : 3 230,80 – 1 000,00 = **2 230,80 €** (= solde issu de E11-01 ✓).
- Délai : décision du 02/06, versements le 15/06, avant la date limite du 20/06 → **pas de retard**, pas d'intérêts de retard.

## 3. Écritures comptables

**Écritures de l'appel et de la libération (à leur date)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 02/06/2026 | OD | 45625 | Associés – capital appelé non versé | Appel solde capital – décision du président du 02/06/2026 | 2 000,00 | |
| 02/06/2026 | OD | 109 | Actionnaires : capital souscrit non appelé | Appel solde capital | | 2 000,00 |
| 02/06/2026 | OD | 1011 | Capital souscrit – non appelé | Appel solde capital | 2 000,00 | |
| 02/06/2026 | OD | 1012 | Capital souscrit – appelé non versé | Appel solde capital | | 2 000,00 |
| 15/06/2026 | OD | 1012 | Capital souscrit – appelé non versé | Libération intégrale du capital | 2 000,00 | |
| 15/06/2026 | OD | 1013 | Capital souscrit – appelé versé | Libération intégrale du capital | | 2 000,00 |

**Écritures de correction (30/09/2026)**

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/09/2026 | OD | 4551 | Compte courant L. Martin | Reclass. vir. 15/06 = libération capital (pas un apport en CC) | 1 000,00 | |
| 30/09/2026 | OD | 45625 | Associés – capital appelé non versé | Vir. L. Martin 15/06 – solde capital | | 1 000,00 |
| 30/09/2026 | OD | 706 | Prestations de services | Annul. encaissement S. Cohen 15/06 enregistré à tort en vente | 833,33 | |
| 30/09/2026 | OD | 44571 | TVA collectée | Annul. TVA collectée à tort (CA3 06/2026) – à régulariser CA3 10/2026 | 166,67 | |
| 30/09/2026 | OD | 45625 | Associés – capital appelé non versé | Vir. S. Cohen 15/06 – solde capital | | 1 000,00 |
| | | | | **Totaux (appel + libération + corrections)** | **8 000,00** | **8 000,00** |

> Le débit de 44571 diminue la TVA collectée du mois d'octobre ; sur la CA3 d'octobre 2026, le cabinet porte la régularisation de 166,67 € sur la ligne de régularisation de TVA prévue par le formulaire (ou en « autre TVA à déduire »), avec une mention dans le dossier de TVA. Contrôle : le compte 45625 est soldé (2 000 D – 1 000 C – 1 000 C).

## 4. Points d'attention / pièges

- **Un apport en capital n'est jamais un produit** et n'est jamais soumis à la TVA. Un libellé contenant le nom de la société ou d'un associé doit être **exclu des règles automatiques** de l'outil OCR.
- **Ne pas confondre libération du capital et apport en compte courant** : le capital est bloqué (il ne se rembourse que par une réduction de capital) ; le compte courant est remboursable. Une erreur de compte peut mener à un remboursement d'apport irrégulier.
- **Une TVA déclarée à tort se régularise**, elle ne se « contre-passe » pas silencieusement : la correction comptable doit être reportée sur une CA3.
- **Décision écrite et notifiée** : sans décision du président (et sans le respect du préavis prévu par les statuts), l'appel n'a pas de base juridique.
- Aucune **formalité de publicité** n'est en principe nécessaire (le montant du capital ne change pas) ; si les statuts mentionnent la fraction libérée, les mettre à jour lors de la prochaine modification (*à vérifier selon la rédaction des statuts*).

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Question 3 — Capitaux au 31/12/2026** : Capital social **10 000 €, entièrement libéré** (1013 = 10 000 € ; 1011 = 0 ; 109 = 0). L'annexe n'a plus à mentionner de capital non appelé.

**Question 4 — La compensation** : oui, juridiquement, un associé peut libérer ses actions **par compensation** avec une créance **certaine, liquide et exigible** qu'il détient sur la société (son compte courant de 2 230,80 €). Il aurait fallu : une décision du président constatant la compensation, la mention de la créance compensée (pour une augmentation de capital dans une société par actions, un **arrêté de compte certifié** est exigé ; pour la simple libération d'un capital déjà souscrit, le cabinet recommande au minimum un arrêté de compte signé et conservé — *formalisme à vérifier selon les statuts*). Écriture : D 4551 / C 45625. L'effet économique est identique (le compte courant aurait baissé de 1 000 €). Puisque Léo a viré l'argent, rien à refaire : il pourra se faire rembourser son compte courant quand la trésorerie le permettra.

**Question 5 — Intérêts de compte courant et libération intégrale** :
- La déduction fiscale des intérêts versés aux associés suppose notamment que **le capital soit entièrement libéré** et que le taux n'excède pas le **taux maximum** publié (art. 39-1-3° et 212 CGI). Cette condition est remplie depuis le 15/06/2026 ; pour une rémunération à venir, elle est donc satisfaite (*modalités d'appréciation de la condition sur la période d'intérêts à vérifier*).
- Il faut une **convention** écrite (taux, modalités) ; elle relève des **conventions réglementées** de la SAS (art. L. 227-10 C. com. : convention avec le président / un associé disposant de plus de 10 % des voix) → rapport aux associés lors de l'approbation des comptes.
- Les intérêts versés à Léo subiront le **PFNL de 12,8 %** et les **prélèvements sociaux** (retenus par la société et déclarés sur la 2777), et figureront sur l'IFU.
- Conseil : avec un compte courant de 2 230,80 €, la rémunération serait symbolique (à 4 %, moins de 90 € par an) et générerait des formalités : à déconseiller tant que le compte courant reste modeste.
- **Taux réduit d'IS** : la condition « capital entièrement libéré » (art. 219-I-b CGI) est remplie à la clôture du 31/12/2026 : Studio Pixel pourra bénéficier du taux de 15 % sur la fraction de bénéfice éligible du premier exercice (voir E10-03 pour le calcul du plafond proratisé).

**Question 6 — Si Sarah n'avait pas payé** : à l'expiration du délai, les sommes non versées portent **intérêt de retard de plein droit** au taux légal (sans formalité) ; après mise en demeure restée sans effet (délai d'au moins un mois), la société peut faire **vendre les actions** de l'associée défaillante et, dans les sociétés par actions, les actions non libérées cessent de donner droit de vote et aux dividendes jusqu'au paiement (*modalités à vérifier dans les statuts et le Code de commerce, art. L. 228-27 à L. 228-29*). Comptablement : D 4566 Actionnaires défaillants / C 45625 pour 1 000 €. Et pour la fiscalité : capital non entièrement libéré à la clôture → **perte du taux réduit** de 15 %.

**Mail type à Léo (extrait)**

> Bonjour Léo,
> La libération du solde du capital est bien faite (décision du 02/06, versements du 15/06) — le capital de Studio Pixel est désormais **entièrement libéré**, ce qui permet à la société de bénéficier du taux réduit d'impôt sur les sociétés à la clôture du 31/12/2026. Votre virement avait été enregistré sur votre compte courant : nous l'avons corrigé, la société vous doit donc 2 230,80 € (et non 3 230,80 €). Le virement de Sarah avait été pris pour une vente : nous récupérons les 166,67 € de TVA payés à tort sur la déclaration d'octobre.
> Pour la compensation : c'était possible, mais votre virement aboutit au même résultat. Pour les intérêts sur votre compte courant : c'est faisable (convention à signer, retenues fiscales à chaque versement), mais pour 2 230 € cela ne vaut pas les formalités. Nous en reparlerons si votre compte courant augmente.

**Documentation / contrôle** :
- Classer la décision du 02/06/2026, les AR de notification et l'extrait bancaire au dossier juridique.
- Modifier la **règle OCR** (exclure les libellés contenant « PIXEL », « CAPITAL », « APPORT », les noms des associés) et le signaler à Sarah.
- Ajouter la régularisation de TVA de 166,67 € à la **liste des points de la CA3 d'octobre**.
- Revue analytique : contrôler qu'aucun autre « encaissement client » ne provient d'un associé.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code de commerce : art. L. 225-3 (libération du solde dans les 5 ans, applicable à la SAS via L. 227-1), art. L. 228-27 à L. 228-29 (actionnaire défaillant — *à vérifier*), art. L. 227-10 (conventions réglementées de la SAS).
- PCG : comptes 1011, 1012, 1013, 109, 4562, 4566, 455.
- CGI : art. 219-I-b (taux réduit, capital entièrement libéré), art. 39-1-3° et 212 (intérêts des comptes courants), art. 125 A et 200 A (PFNL et imposition des intérêts), art. 256 (champ de la TVA — les apports en capital n'en relèvent pas).
- BOFiP : TVA – régularisations ; BIC – charges financières – intérêts des comptes courants d'associés.
