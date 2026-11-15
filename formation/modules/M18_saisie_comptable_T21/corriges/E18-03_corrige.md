# Corrigé E18-03 — Les factures des libéraux : convention, planning et avoirs

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **10-SESSAD** | Section analytique du SESSAD. Le service pour enfants (45 places), financé par l'ARS. Toute charge du SESSAD porte ce code. |
    | **20-SAVS** | Section analytique du SAVS. Le service pour adultes (60 places), financé par le Département. Toute charge du SAVS porte ce code. |
    | **AC** | Journal des achats. Journal où l'on enregistre les factures fournisseurs. |
    | **BQSAV** | Journal de banque du SAVS. Contrepartie automatique 5123000. |
    | **BQSES** | Journal de banque du SESSAD. Contrepartie automatique 5122000. |
    | **CGI** | Code général des impôts. Le code qui contient toutes les règles fiscales (TVA, IS, IR…). « art. 39 CGI » = article 39 de ce code. |
    | **IME** | Institut médico-éducatif. Établissement qui accueille des enfants et adolescents avec une déficience intellectuelle. |
    | **RGPD** | Règlement général sur la protection des données. Règles européennes sur les données personnelles. |
    | **SAV** | Structure SAVS (dossier M18). Code de la structure SAVS : sa propre comptabilité (financeur Département, BP/CA). |
    | **SAVS** | Service d'accompagnement à la vie sociale. Service qui accompagne des adultes en situation de handicap dans leur vie quotidienne (logement, budget, loisirs). Financé par le Département. |
    | **SES** | Structure SESSAD (dossier M18). Code de la structure SESSAD : sa propre comptabilité (financeur ARS, EPRD/ERRD). |
    | **SESSAD** | Service d'éducation spéciale et de soins à domicile. Service qui accompagne des enfants et jeunes en situation de handicap là où ils vivent (école, domicile, crèche). Financé par l'ARS. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **TTC** | Toutes taxes comprises. Montant TVA incluse : c'est ce que le client paie réellement. TTC = HT + TVA. |
    | **TVA** | Taxe sur la valeur ajoutée. Impôt payé par le consommateur final, collecté par les entreprises. L'entreprise reverse à l'État la TVA collectée sur ses ventes moins la TVA déductible sur ses achats. |
    | **Compte 512** | Banque. Le compte bancaire de l'association. |
    | **Compte 4011000** | Libéraux (comptes de tiers LI…) (plan T21). Centralisation des libéraux (orthophonistes, psychomotriciens…). On saisit dans les comptes LI… |
    | **Compte 4081000** | Fournisseurs  factures non parvenues (plan T21). Facture non parvenue : charge de N dont la facture arrivera en N+1. Crédité en N, débité en N+1 (extourne). |
    | **Compte 5122000** | Banque du SESSAD (dossier M18, fictif). Compte bancaire du SESSAD, journal BQSES. |
    | **Compte 5123000** | Banque du SAVS (dossier M18, fictif). Compte bancaire du SAVS, journal BQSAV. |
    | **Compte 6223221** | Honoraires Orthophonistes (plan T21). Honoraires d'orthophonistes (exemple du document T21 : orthophoniste Dupont, compte LIDUPONT). |
    | **Compte 6223222** | Honoraires Psycho-motriciens (plan T21). Honoraires de psychomotriciens. |
    | **Compte 6223224** | Honoraires Psychologues (plan T21). Honoraires de psychologues. |
    | **Compte 6223226** | Honoraires Educateurs (plan T21). Honoraires d'éducateurs libéraux. |
    | **LI** | Compte de tiers Libéral (Trisomie 21). Préfixe des comptes des professionnels libéraux conventionnés (orthophoniste, psychomotricien…), ex. : LIDUPONT. Regroupés dans 4011000. Crédité à la facture, débité au paiement. |
    | **LIBENALI** | Compte libéral : psychologue (dossier M18). Groupes de parole du SAVS (6223224). |
    | **LIDUPONT** | Compte libéral : orthophoniste Dupont. Exemple du document T21 : LIDUPONT crédité, 6223221 Honoraires orthophonistes débité. |
    | **LIMOREAUPSY** | Compte libéral : psychomotricien (dossier M18). Séances de psychomotricité du SESSAD (6223222). |
    | **factures non parvenues** | Charge sans facture au 31/12 (FNP). Le service est fait mais la facture n'est pas arrivée : on enregistre la charge quand même (compte 408). |
    | **lettrage** | Relier une facture et son paiement. Dans un compte de tiers, la facture et le virement reçoivent la même lettre (A, B…) : ils s'annulent. |
<!-- /glossaire-page -->

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E18-03](../exercices/E18-03_factures-liberaux-avoirs.md)

!!! abstract "En clair"
    Sur 1 785,00 € facturés en octobre, **1 614,00 €** sont dus : 630,00 € à Claire Dupont, 504,00 € à Julien Moreau et 480,00 € à Samira Benali. Les 171,00 € écartés correspondent à une séance non réalisée (enfant hospitalisé, absence prévenue) et à trois séances pour un enfant qui n'était plus accompagné par le SESSAD. Côté paiement, on vire le 20/11 : 630,00 €, 504,00 € et 360,00 € (480,00 € moins l'avoir de 120,00 € sur septembre).

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

Pour chaque ligne d'un relevé de libéral, trois questions :

1. **L'enfant (ou l'adulte) est-il accompagné par le service à cette date ?** → liste des personnes accompagnées, dates d'admission et de sortie.
2. **La séance a-t-elle eu lieu ?** → planning du service, absences signalées, règle d'absence de la convention.
3. **Le tarif est-il celui de la convention ?** → tarif de la séance, du bilan, du groupe.

Et deux questions pour la facture entière : **les calculs** sont-ils justes, et la facture est-elle **déjà payée** en tout ou partie (avoir sur un mois précédent) ?

### Question 1 — Contrôle ligne par ligne

**Claire Dupont (orthophonie, SESSAD)**

| Enfant | Facturé | Contrôle | Décision |
|---|---|---|---|
| A.R. | 4 séances × 45,00 = 180,00 | Aucune absence | Accepté |
| L.M. | 3 séances × 45,00 = 135,00 | Le **14/10**, L.M. était **hospitalisé** (du 13 au 16/10). La famille a prévenu le 12/10, donc plus de 24 h avant : séance **non réalisée et non facturable** | **45,00 refusés** ; 2 séances acceptées = 90,00 |
| N.K. | 4 séances × 45,00 = 180,00 | Aucune absence | Accepté |
| E.P. | Bilan 90,00 + 2 séances × 45,00 = 180,00 | Admis le 01/10, prescription du bilan au dossier, tarif du bilan conforme | Accepté |
| **Total** | **675,00** | | **630,00 acceptés** |

**Julien Moreau (psychomotricité, SESSAD)**

| Enfant | Facturé | Contrôle | Décision |
|---|---|---|---|
| T.B. | 3 séances × 42,00 = 126,00 | **Sorti du SESSAD le 30/09/2026** (orientation IME). La convention ne couvre que les enfants accompagnés. M. Moreau a été informé par courrier le 16/09 | **126,00 refusés** |
| J.D. | 4 × 42,00 = 168,00 | Conforme | Accepté |
| M.S. | 4 × 42,00 = 168,00 | Conforme | Accepté |
| C.F. | 4 × 42,00 = 168,00 | Conforme | Accepté |
| **Total** | **630,00** | | **504,00 acceptés** |

**Samira Benali (groupes de parole, SAVS)**

| Élément | Montant | Contrôle | Décision |
|---|---|---|---|
| 4 groupes d'octobre × 120,00 | 480,00 | Conforme au relevé des groupes visé par la cheffe de service | Accepté |
| Avoir sur septembre (groupe du 24/09 annulé) | − 120,00 | La facture de septembre (480,00) a **déjà été payée** le 20/10 (lettrage B). L'avoir est une **créance** sur Mme Benali : il vient en déduction du paiement d'octobre | À déduire |

> ⚠️ Erreur classique : penser que le visa du chef de service suffit. Le chef de service vise que les séances correspondent à des enfants qu'il connaît ; il ne revérifie pas toujours le planning des absences ni les sorties. Le contrôle croisé facture / planning / liste des accompagnés est **le** travail de l'agent comptable sur les libéraux.

### Question 5 — Pourquoi pas de TVA ?

- **Pièces 1 et 2** : les actes de soins dispensés par les professions de santé réglementées (orthophonistes, psychomotriciens, comme les autres auxiliaires médicaux) sont **en général exonérés de TVA** par le Code général des impôts. L'exonération tient à **la nature de l'acte**.
- **Pièce 3** : la mention « article 293 B du CGI » renvoie à la **franchise en base** de TVA : la professionnelle ne facture pas de TVA parce que son chiffre d'affaires est **sous un seuil**. L'exonération tient à **sa situation** (montant de son activité), pas à l'acte. Si elle dépasse un jour le seuil, ses factures pourraient comporter de la TVA (*seuils à vérifier chaque année*).
- Pour l'association, la conséquence pratique est la même : on saisit le **montant facturé**, en charge. Si une facture de libéral comportait un jour de la TVA, l'agent comptable n'a pas à décider à la place du professionnel ; il le **signale** et saisit le TTC.

## 2. Calculs (détaillés, chaque montant justifié)

| Libéral | Facturé | Écarté | Accepté | Avoir déjà reçu | **À payer le 20/11** | Avoir attendu |
|---|---|---|---|---|---|---|
| Claire Dupont | 675,00 | 1 × 45,00 = 45,00 | 630,00 | — | **630,00** | 45,00 |
| Julien Moreau | 630,00 | 3 × 42,00 = 126,00 | 504,00 | — | **504,00** | 126,00 |
| Samira Benali | 480,00 | 0,00 | 480,00 | 120,00 | **360,00** | — |
| **Total** | **1 785,00** | **171,00** | **1 614,00** | **120,00** | **1 494,00** | **171,00** |

Le SESSAD paiera 630,00 + 504,00 = 1 134,00 € (BQSES) ; le SAVS paiera 360,00 € (BQSAV).

**Pourquoi saisir la facture entière et non le montant accepté ?** Une facture émise ne se modifie pas : la seule correction possible est un **avoir** du professionnel. On saisit donc la pièce **telle qu'elle est** (675,00 € et 630,00 €), on ne paie que la partie acceptée, et le reliquat reste ouvert sur le compte du libéral jusqu'à l'avoir. Le compte de tiers montre ainsi, à tout moment, le **désaccord en cours**.

## 3. Écritures comptables

### Claire Dupont — facture du 31/10/2026, paiement du 20/11/2026, avoir attendu

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 6223221 Honoraires orthophonistes | | Dupont – orthophonie – CD-2026-10 – 10/2026 | 10-SESSAD | 675,00 | |
| SES | AC | 4011000 Libéraux | LIDUPONT | Dupont – orthophonie – CD-2026-10 – 10/2026 | | | 675,00 |
| SES | BQSES | 4011000 Libéraux | LIDUPONT | Virement Dupont – CD-2026-10 – partiel (1 séance contestée) | | 630,00 | |
| SES | BQSES | 5122000 Crédit Mutuel – SESSAD *(ligne automatique)* | | Virement Dupont – CD-2026-10 – partiel | | | 630,00 |
| SES | AC | 4011000 Libéraux | LIDUPONT | Dupont – avoir séance 14/10 L.M. non due – *à saisir à réception* | | 45,00 | |
| SES | AC | 6223221 Honoraires orthophonistes | | Dupont – avoir séance 14/10 – *à saisir à réception* | 10-SESSAD | | 45,00 |

### Julien Moreau — facture du 31/10/2026, paiement du 20/11/2026, avoir attendu

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SES | AC | 6223222 Honoraires psychomotriciens | | Moreau – psychomotricité – JM-2026-10 – 10/2026 | 10-SESSAD | 630,00 | |
| SES | AC | 4011000 Libéraux | LIMOREAUPSY | Moreau – psychomotricité – JM-2026-10 – 10/2026 | | | 630,00 |
| SES | BQSES | 4011000 Libéraux | LIMOREAUPSY | Virement Moreau – JM-2026-10 – partiel (enfant sorti) | | 504,00 | |
| SES | BQSES | 5122000 Crédit Mutuel – SESSAD *(ligne automatique)* | | Virement Moreau – JM-2026-10 – partiel | | | 504,00 |
| SES | AC | 4011000 Libéraux | LIMOREAUPSY | Moreau – avoir 3 séances dossier S-2022-008 – *à saisir à réception* | | 126,00 | |
| SES | AC | 6223222 Honoraires psychomotriciens | | Moreau – avoir 3 séances – *à saisir à réception* | 10-SESSAD | | 126,00 |

### Samira Benali — facture du 31/10/2026, avoir du 05/11/2026, paiement du 20/11/2026

| Livres de | Journal | Compte | Tiers | Libellé | Analytique | Débit | Crédit |
|---|---|---|---|---|---|---|---|
| SAV | AC | 6223224 Honoraires psychologues | | Benali – groupes de parole – SB-2026-10 – 10/2026 | 20-SAVS | 480,00 | |
| SAV | AC | 4011000 Libéraux | LIBENALI | Benali – groupes de parole – SB-2026-10 – 10/2026 | | | 480,00 |
| SAV | AC | 4011000 Libéraux | LIBENALI | Benali – avoir groupe 24/09 annulé – SB-AV-2026-01 sur SB-2026-09 | | 120,00 | |
| SAV | AC | 6223224 Honoraires psychologues | | Benali – avoir groupe 24/09 annulé – SB-AV-2026-01 | 20-SAVS | | 120,00 |
| SAV | BQSAV | 4011000 Libéraux | LIBENALI | Virement Benali – SB-2026-10 moins avoir SB-AV-2026-01 | | 360,00 | |
| SAV | BQSAV | 5123000 Crédit Mutuel – SAVS *(ligne automatique)* | | Virement Benali – SB-2026-10 moins avoir | | | 360,00 |

*Rappel : dans le journal de banque, vous saisissez seulement la ligne du tiers (LIBENALI au débit) ; le logiciel génère la ligne 512. Le compte 4011000 est alimenté automatiquement par le compte de tiers : on « saisit dans » LIBENALI, jamais dans 4011000.*

### Question 4 — Le lettrage

**Lettrer**, c'est relier dans le compte du tiers les lignes qui se compensent (une facture et son paiement), en leur donnant la même lettre. Une ligne non lettrée est une ligne **en attente** : c'est elle qu'il faut expliquer.

**LIDUPONT après le 20/11 :**

| Pièce | Débit | Crédit | Lettrage |
|---|---|---|---|
| CD-2026-10 facture | | 675,00 | *non lettrée* |
| Virement du 20/11 | 630,00 | | *non lettrée* |
| **Solde créditeur** | | **45,00** | |

La facture et le virement ne s'équilibrent pas : on **ne les lettre pas encore** (certains logiciels permettent un lettrage partiel, à n'utiliser que si la procédure le prévoit). Le solde de 45,00 € correspond exactement à la séance contestée. À réception de l'avoir de 45,00 €, on lettre les **trois** lignes ensemble : 675,00 = 630,00 + 45,00.

**LIBENALI après le 20/11 :**

| Pièce | Débit | Crédit | Lettrage |
|---|---|---|---|
| SB-2026-09 facture (05/10) | | 480,00 | B |
| Virement du 20/10 | 480,00 | | B |
| SB-2026-10 facture | | 480,00 | C |
| SB-AV-2026-01 avoir | 120,00 | | C |
| Virement du 20/11 | 360,00 | | C |
| **Solde** | | **0,00** | |

Septembre reste lettré B (la facture a bien été payée en entier). L'avoir est lettré avec la facture d'octobre et le virement de novembre : 480,00 = 120,00 + 360,00. Compte soldé.

## 4. Points d'attention / pièges

- **Payer 675,00 € « parce que le chef de service a visé »** : le visa ne remplace pas le contrôle du planning. La séance du 14/10 n'a pas eu lieu.
- **Imputer les 126,00 € de T.B. en charge « en attendant »** et les payer : ces séances ne relèvent plus du SESSAD. Si M. Moreau a continué à suivre l'enfant, il doit facturer **la famille** ou la nouvelle structure (l'IME), selon ce qui a été organisé. Ce n'est ni à l'association de payer, ni à l'agent comptable de régler ce point avec la famille : on informe le professionnel et le chef de service.
- **Saisir l'avoir Benali en produit** (classe 7) : non. Il réduit la charge **6223224**, comme le dit le document T21 : « LIDUPONT au débit et 6223221 au crédit ».
- **Oublier que la facture de septembre est déjà payée** : on pourrait demander à Mme Benali un remboursement de 120,00 € par chèque. C'est inutile et lourd : la déduction sur le paiement suivant est la règle (« à déduire de votre prochain règlement »).
- **Écrire le nom de l'enfant dans le libellé** : interdit (voir plus bas). Le numéro de dossier suffit, et seulement si c'est utile.
- **Se tromper de compte d'honoraires** : orthophoniste 6223221, psychomotricien 6223222, psychologue 6223224. Le plan T21 a un compte par profession, pour que le service puisse suivre ses dépenses par type de soin.

### Question 6 — Message à Julien Moreau

> Objet : votre facture JM-2026-10 – séances d'octobre 2026
>
> Bonjour Monsieur Moreau,
>
> Nous avons bien reçu votre facture n° JM-2026-10 de 630,00 €. Les séances facturées pour le dossier S-2022-008 (3 séances, 126,00 €) concernent un enfant dont l'accompagnement par le SESSAD a pris fin le 30/09/2026, comme indiqué dans le courrier du 16/09/2026. La convention ne nous permet pas de les prendre en charge.
>
> Nous vous réglons donc 504,00 € le 20/11/2026, et nous vous remercions de nous adresser un **avoir de 126,00 €** sur cette facture. Pour la suite de la prise en charge de cet enfant, Karim Belkacem, chef de service, reste à votre disposition.
>
> Bien cordialement,
> L'agent comptable – Association Cap Horizons 21

*(Message de même nature à Claire Dupont, plus court : séance du 14/10 pour le dossier S-2025-004, absence prévenue le 12/10, avoir de 45,00 € demandé, paiement de 630,00 € le 20/11.)*

### Question 7 — Confidentialité

- Les relevés de séances contiennent des **données de santé** sur des mineurs : ce sont des données particulièrement protégées (RGPD).
- **Dans la saisie** : libellés sans nom ni initiales d'enfant (« Dupont – orthophonie – CD-2026-10 – 10/2026 ») ; le détail reste sur la pièce.
- **Dans le classement** : pièces dans un classeur ou un dossier numérique à accès limité (comptabilité, direction) ; pas d'envoi des relevés par mail non sécurisé, ni à des personnes qui n'en ont pas besoin. Si le commissaire aux comptes demande la pièce, on la lui montre ; on ne la fait pas circuler.
- **Demander aux libéraux** de n'indiquer que les initiales et le numéro de dossier (c'est déjà dans la convention : rappeler la règle si un nom apparaît un jour).

## 5. Ce qu'un senior ferait en plus

**Bonnes pratiques**

- Tenir un **tableau de suivi mensuel** par libéral : séances prévues au planning, séances facturées, écart, avoir demandé, avoir reçu. Il sert aussi pour le budget : les honoraires de libéraux sont un poste suivi de près par l'ARS.
- Demander au chef de service de transmettre **chaque mois**, en même temps que le planning, la liste des **entrées et sorties** d'enfants. C'est le contrôle le plus efficace contre les séances « hors convention ».
- **Relancer les avoirs attendus** à chaque fin de mois : un avoir oublié laisse un solde créditeur sur le compte LI, que l'on finit par payer par erreur ou que le commissaire aux comptes relève.
- À la clôture, provisionner en **4081000** (factures non parvenues, **sans** tiers LI) les séances de décembre réalisées mais facturées en janvier, d'après le planning.
- Si la même erreur revient plusieurs mois, proposer à la directrice d'**ajouter à la convention** une clause de transmission du relevé au chef de service **avant** facturation.

**Le raisonnement d'analyse**

- Les libéraux sont un des rares postes où la charge dépend directement de l'**activité** (nombre de séances). C'est pour cela que le contrôle se fait contre le **planning** et non seulement contre la convention : un tarif juste appliqué à une séance qui n'a pas eu lieu reste une dépense injustifiée.
- Payer la partie non contestée **à temps** est aussi important que contester le reste : ces professionnels sont des partenaires du service, et un paiement bloqué pour 45,00 € sur 675,00 € abîme la relation pour rien.

## 6. Références

- Document interne « Les journaux comptables chez Trisomie 21 France » : facturation d'un libéral (LIDUPONT, 6223221) et avoir « à l'envers ».
- Plan comptable T21 : 4011000 Libéraux, 6223221 à 6223226 Honoraires par profession, 4081000 Factures non parvenues.
- CGI : exonération de TVA des soins dispensés par les membres des professions médicales et paramédicales réglementées ; article 293 B (franchise en base).
- RGPD : données de santé, catégorie particulière de données.
