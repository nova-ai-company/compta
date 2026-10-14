# Corrigé E09-03 — Les produits constatés d'avance de TechNova (situation au 30/06/2026)

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E09-03](../exercices/E09-03_pca-saas-technova.md)

## 1. Analyse

Un abonnement SaaS est une **prestation de services continue** : le produit est **acquis au fur et à mesure de la mise à disposition du service**, et non à la signature ni à la facturation. La facture émise d'avance pour toute la période est comptabilisée en 706 au moment de son émission, puis la part qui correspond à la période postérieure à l'arrêté est **neutralisée en PCA (487)**, pour son montant **HT**.

| Réf. | Mois restant à courir après le 30/06/2026 | Analyse |
|---|---|---|
| A | 2 (juillet, août) | PCA 2/12 |
| B | 6 (juillet à décembre) | PCA 6/12 |
| C | 9 (juillet 2026 à mars 2027) | PCA 9/12 |
| D | 11 (juillet 2026 à mai 2027) | PCA 11/12. Client allemand en autoliquidation : sans incidence sur le PCA, qui est toujours HT |
| E | 24 (juillet 2026 à juin 2028) sur 36 | PCA 24/36, **dont 12 mois à plus d'un an** |
| F | 12 sur 12 | Facture émise le 28/06 pour une période qui n'a pas commencé → **PCA à 100 %** |
| G | 1 sur 1 | Mensuels de juillet facturés en juin → **PCA à 100 %** |
| H | 7 mois remboursables | Contrat **résilié** au 30/06 : les 7 mois ne seront jamais réalisés et donneront lieu à un **avoir**. On ne constate pas de PCA, on constate un **avoir à établir** (4198) |
| I | 0 | La mise en service est une **prestation distincte, entièrement réalisée** en juin (paramétrage, reprise des données, formation livrés) → produit acquis, pas de PCA |

**La facture F (question 3) :** la facture a été émise, elle crée une créance juridique, et TechNova l'a enregistrée dans son journal des ventes. On la comptabilise (D 411 / C 7061 / C 44571, ou un compte de TVA en attente puisque la TVA sur services n'est exigible qu'à l'encaissement), **puis on la neutralise intégralement en PCA**. L'effet net sur le résultat est nul. Autre approche admise : ne pas comptabiliser une facture émise pour une période future et non encore payée. Mais il est plus simple et plus traçable de suivre le journal des ventes et de neutraliser par PCA. Ce qui est **interdit**, c'est de laisser 7 200 € en chiffre d'affaires du semestre.

**Le contrat H (question 2) :** la résiliation est notifiée et acceptée avant le 30/06, avec un remboursement contractuel (article 9 des CGV). L'obligation de rembourser existe à la clôture, et son montant est certain : 12 000 € × 7/12 = 7 000 € HT. On passe donc un **avoir à établir**, avec TVA puisque c'est une réduction du prix facturé. Il ne faut **pas** constater en plus un PCA sur H, sinon les 7 000 € seraient retirés deux fois du produit.

## 2. Calculs

| Réf. | Montant HT | Calcul | PCA |
|---|---|---|---|
| A | 14 400,00 € | 14 400 × 2/12 | 2 400,00 € |
| B | 9 600,00 € | 9 600 × 6/12 | 4 800,00 € |
| C | 18 000,00 € | 18 000 × 9/12 | 13 500,00 € |
| D | 24 000,00 € | 24 000 × 11/12 | 22 000,00 € |
| E | 50 400,00 € | 50 400 × 24/36 | 33 600,00 € |
| F | 7 200,00 € | 100 % | 7 200,00 € |
| G | 21 350,00 € | 100 % | 21 350,00 € |
| H | — | voir avoir à établir | 0,00 € |
| I | — | prestation réalisée | 0,00 € |
| **Total PCA** | | | **104 850,00 €** |

**Avoir à établir H :** HT 12 000 × 7/12 = **7 000,00 €** ; TVA 20 % = **1 400,00 €** ; TTC **8 400,00 €**.

**Part des PCA à plus d'un an (après le 30/06/2027) :** seul le contrat E est concerné, de juillet 2027 à juin 2028, soit 12 mois × 1 400 € = **16 800,00 €**. Pour le contrat D, le dernier mois est mai 2027 : il reste à moins d'un an.

**Effet sur le CA du semestre :** le 7061 passe de 812 400 € à 812 400 – 104 850 – 7 000 = **700 550,00 €**. Le 7062 (41 500 €) est inchangé.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 30/06/2026 | OD | 7061 | Abonnements SaaS | PCA abonnements au 30/06/2026 | 104 850,00 | |
| 30/06/2026 | OD | 487 | Produits constatés d'avance | PCA abonnements au 30/06/2026 | | 104 850,00 |
| 30/06/2026 | OD | 7061 | Abonnements SaaS (*ou 709 RRR accordés*) | Avoir à établir Fromageries Alpines 7/12 | 7 000,00 | |
| 30/06/2026 | OD | 44587 | TVA sur factures à établir | Avoir à établir Fromageries Alpines | 1 400,00 | |
| 30/06/2026 | OD | 4198 | Clients – avoirs à établir | Avoir à établir Fromageries Alpines | | 8 400,00 |
| | | | | **Totaux** | **113 250,00** | **113 250,00** |

Au **01/07/2026** : extourne du PCA et de l'avoir à établir. L'avoir réel émis en juillet viendra ensuite en diminution du chiffre d'affaires de juillet et compensera l'extourne.

*La facture F est supposée déjà enregistrée au journal des ventes du 28/06. Si elle ne l'était pas, on peut ne pas l'enregistrer et retirer 7 200 € du PCA. Le résultat est identique ; seule la présentation du bilan change (créance et PCA de 7 200 € en moins).*

## 4. Points d'attention / pièges

- **PCA toujours HT**, y compris pour le client allemand en autoliquidation (aucune TVA facturée).
- **Ne pas confondre facturation et réalisation :** facturer 50 400 € en juillet 2025 pour 36 mois ne donne que 1 400 € de CA par mois.
- **Double neutralisation (contrat H) :** il faut choisir entre PCA et avoir à établir. Ici, l'avoir est la bonne réponse, puisque le service ne sera jamais rendu.
- **Frais de mise en service :** le PCG ne contient pas de règle détaillée. On les reconnaît immédiatement **s'ils rémunèrent une prestation distincte, réalisée et utile au client par elle-même** (ici, formation et reprise de données livrées). S'il s'agissait d'un simple « droit d'entrée » sans prestation distincte, on les étalerait sur la durée de l'abonnement. Documentez votre choix et appliquez-le de façon permanente.
- **TVA sur les services :** TechNova n'a pas opté pour les débits, donc la TVA est exigible à **l'encaissement**. La facture F (non payée) ne génère pas encore de TVA à reverser. Vérifiez le paramétrage du logiciel : compte de TVA « en attente » (4457x) pour les factures non encaissées.
- **Situation intermédiaire :** les mêmes principes s'appliquent qu'à la clôture (cut-off, PCA, provisions), puisque les investisseurs s'en serviront pour leurs décisions.

## 5. Ce qu'un senior ferait en plus

- **Rapprochement registre ↔ comptabilité :** le total facturé au registre doit correspondre au 7061 du semestre (extourne du PCA d'ouverture comprise). Tout écart signale des avoirs ou des factures hors registre.
- **Test du « deferred revenue » du logiciel de facturation :** comparez le PCA calculé (104 850 €) à l'état généré par l'outil, puis sondez 5 contrats (bons de commande signés, CGV, avenants, résiliations).
- **Indicateurs pour les investisseurs :** proposez à Émilie de présenter **à côté** des comptes un tableau de bord des **ventes signées (bookings)**, de l'**ARR/MRR** et du **carnet de PCA**. Ce sont les indicateurs que Yanis cherche, et ils ne se confondent pas avec le chiffre d'affaires comptable.

**Réponse à Yanis :**
> « Yanis, les contrats signés en juin sont une excellente nouvelle, et ils apparaîtront clairement : ils figurent au bilan en "produits constatés d'avance" (104 850 €), c'est-à-dire du chiffre d'affaires déjà facturé et sécurisé, qui sera reconnu au fil des mois de service. Le chiffre d'affaires comptable du semestre ne peut retenir que le service effectivement rendu (principe d'indépendance des exercices, art. L. 123-21 C. com.). Pour vos investisseurs, je vous propose d'ajouter un tableau "bookings / ARR / carnet de commandes" : c'est l'indicateur qu'ils attendent d'un éditeur SaaS, et il valorise mieux vos ventes de juin qu'un CA gonflé qu'un auditeur corrigerait. »

## 6. Références

- Code de commerce, art. L. 123-21 (seuls les bénéfices réalisés à la date de clôture peuvent être inscrits) ; art. L. 123-13 (inventaire).
- CGI, art. 38, 2 bis : les produits des prestations continues rémunérées notamment par des intérêts ou des loyers et des prestations discontinues à échéances successives sont rattachés **au fur et à mesure de l'exécution**.
- CGI, art. 269, 2-c (exigibilité de la TVA sur services à l'encaissement) ; directive 2006/112/CE, art. 44 et 196 (prestations B2B intra-UE, autoliquidation par le preneur).
- PCG : compte 487 « Produits constatés d'avance » ; compte 4198 « Clients – avoirs à établir ».
