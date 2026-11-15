# E18-08 — Petite caisse, virements internes et compte à terme
**Dossier :** Cap Horizons 21 (5 structures, modèle T21 France) | **Difficulté :** ★★☆ | **Durée estimée :** 1 h 15 | **Thèmes :** journal de caisse, compte 5300000, virements internes 5800000, dons en espèces, comptage et écart de caisse, journal de placement, compte à terme 5081100, intérêts 7640000, intérêts courus 5188000, extourne, lecture critique d'une procédure interne

**Corner case :** oui — il manque 3,50 € dans la caisse après l'événement ; le document interne T21 contient une erreur de sens sur les placements, et classe les parts sociales du Crédit Mutuel autrement que le plan comptable

<!-- glossaire-page -->
??? tip glossaire-page "📖 Les mots et codes de cette page — cliquez pour ouvrir"
    Sur le site, vous pouvez aussi **cliquer sur un mot souligné en pointillés** dans le texte.

    | Mot / code | Ce que ça veut dire |
    |---|---|
    | **01-SIEGE** | Section analytique du siège. Direction générale, comptabilité, RH. Son coût est refacturé aux services sous forme de frais de siège. |
    | **90-ASSO** | Section analytique de la vie associative. Adhésions, dons, événements : ce qui n'appartient à aucun service financé. |
    | **ASS** | Structure Association et projets (dossier M18). Vie associative, dons, habitat inclusif, projet Pairs et voix. |
    | **BQASS** | Journal de banque de l'association. Contrepartie automatique 5125000. |
    | **BQSIE** | Journal de banque du siège. Contrepartie automatique 5121000 : vous saisissez seulement la ligne d'en face. |
    | **CAASS** | Journal de caisse de l'association. Petite caisse des événements, compte 5300000. Se tient comme une banque. |
    | **CAT** | Compte à terme. Placement bloqué pour une durée fixée, avec intérêts. Comptes 5081XXX dans le plan T21. |
    | **CESF** | Conseiller (ou conseillère) en économie sociale et familiale. Travailleur social qui aide les personnes à gérer leur budget, leur logement, leur vie quotidienne. Métier fréquent dans un SAVS. |
    | **CME** | Crédit Mutuel (abréviation du plan T21). Banque coopérative : pour ouvrir un compte, on souscrit des parts sociales. |
    | **ICNE** | Intérêts courus non échus. À la clôture : intérêts d'emprunt qui concernent l'année mais qui seront payés à la prochaine échéance. On les enregistre en charge de N. |
    | **PLSIE** | Journal de banque « placement » du siège. Un journal par placement : versements, retraits, intérêts du compte à terme 5081100. |
    | **PSB** | Parts sociales (abréviation du plan T21). Dans « PSB CME T21 France (parts sociales) », compte 5040000 : parts sociales détenues au Crédit Mutuel. |
    | **PV** | Procès-verbal — ou plus-value. Deux sens selon le contexte : (1) PV d'assemblée générale, de réception de travaux, d'inventaire ; (2) plus-value de cession. |
    | **SIE** | Service des impôts des entreprises — ou, dans le M18, la structure Siège. Le centre des impôts dont dépend l'entreprise : interlocuteur pour la TVA, l'IS, la CFE. Dans le module M18, SIE est aussi le code de la structure « Siège social » de l'association. |
    | **T21** | Trisomie 21 (France). Abréviation utilisée dans les documents internes : « T21 France » = la Fédération Trisomie 21 France. |
    | **Compte 2710000** | Titres immobilisés (droit de propriété) (plan T21). Titres détenus durablement (le document T21 y range les parts sociales du Crédit Mutuel ; le plan, lui, a aussi 5040000 : à clarifier). |
    | **Compte 5040000** | PSB CME T21 France (parts sociales) (plan T21). Parts sociales du Crédit Mutuel détenues par T21 France (« PSB CME »). Le document range les parts sociales en 27 : à clarifier. |
    | **Compte 5081100** | Compte à terme du siège (dossier M18, fictif). Placement du siège, sous-compte du 5081XXX du plan T21 ; journal PLSIE. |
    | **Compte 5121000** | Banque du siège (dossier M18, fictif). Compte bancaire du siège, journal BQSIE. |
    | **Compte 5125000** | Banque de l'association (dossier M18, fictif). Compte bancaire de la structure Association et projets, journal BQASS. |
    | **Compte 5188000** | Intérêts courus à recevoir (plan T21). Intérêts des placements acquis au 31/12 mais versés plus tard. |
    | **Compte 5300000** | Caisse (plan T21). Caisse (espèces). Le solde doit être égal au comptage physique. |
    | **Compte 5800000** | Virements internes (plan T21). Virements internes : passage obligé entre deux comptes de trésorerie (banque → caisse, banque → placement). Solde nul au 31/12. |
    | **Compte 7640000** | Revenus des valeurs mobilières de placement (plan T21). Intérêts des placements (comptes à terme, livrets). |
    | **Code analytique** | Le code du service saisi sur chaque ligne. Il dit « pour qui » est la charge (ex. : 10-SESSAD). |
    | **extourne** | Annuler une écriture au 1er jour de l'exercice suivant. On passe l'écriture inverse (ex. : d'une FNP) pour ne pas compter la charge deux fois quand la facture arrive. |
<!-- /glossaire-page -->

> *Cadre de formation : association, personnes, sociétés et documents fictifs. Les numéros de comptes viennent du plan comptable T21 France ; les numéros de banque, de placement et de journaux sont ceux de la fiche du dossier M18.*

!!! abstract "En clair"
    Quand de l'argent passe d'une « poche » de trésorerie à une autre **de la même structure** (de la banque à la caisse, du compte courant au compte à terme), l'association ne gagne ni ne perd rien. On fait passer le mouvement par un compte « couloir », le **5800000 Virements internes** : il est mouvementé une fois à la sortie, une fois à l'entrée, et revient à **zéro**. S'il ne revient pas à zéro, une des deux moitiés manque.

## La mise en situation

Lundi 16 novembre 2026, 9 h. Samedi 14/11, l'association a organisé un **goûter solidaire** dans la salle commune, pour présenter le projet d'habitat inclusif aux familles. Rachid Haddad (CESF, conseiller en économie sociale et familiale, qui tient la petite caisse de l'ASS) dépose sur votre bureau une enveloppe et une boîte en métal :

> « Voilà les tickets, le PV des dons et la caisse. J'ai déposé 400 € à la banque ce matin en arrivant. J'ai recompté la caisse ensuite… il me manque quelque chose, je crois. »

Ensuite, Odile Marchand, la trésorière, vous appelle au sujet du **compte à terme** du siège : elle a fait un retrait partiel ce matin pour passer le creux de trésorerie de fin novembre, et veut savoir « combien d'intérêts il faudra mettre dans les comptes au 31 décembre ».

Rappels de la fiche du dossier :

- **Petite caisse** : structure **ASS**, compte **5300000** Caisse, journal **CAASS** (fonctionne comme un journal de banque, contrepartie automatique 5300000). Banque de l'ASS : **5125000**, journal **BQASS**.
- **Compte à terme** : structure **SIE**, compte **5081100**, journal **PLSIE** (contrepartie automatique 5081100). Banque du siège : **5121000**, journal **BQSIE**.
- Code analytique de la vie associative : **90-ASSO** ; du siège : **01-SIEGE**.

## Les pièces

### Partie A — La petite caisse de l'ASS

**Pièce A1 — Solde de la caisse au 31/10/2026** : 84,30 € (comptage du 31/10 conforme, signé par R. Haddad et par vous).

**Pièce A2 — Les mouvements de novembre**

| Date | Opération | Justificatif | Montant |
|---|---|---|---|
| 03/11 | Retrait d'espèces au guichet du Crédit Mutuel, compte de l'ASS, pour alimenter la caisse avant le goûter | Avis de retrait + relevé BQASS | 300,00 |
| 13/11 | Supermarché : boissons, gâteaux, fruits pour le goûter | Ticket de caisse | 86,45 |
| 13/11 | Bazar : petits jeux et crayons pour le stand des enfants | Ticket de caisse | 42,90 |
| 14/11 | Dons déposés dans l'urne pendant le goûter (dons anonymes en espèces) | PV de comptage signé par deux bénévoles | 412,50 |
| 16/11 | Versement d'espèces au guichet sur le compte de l'ASS (crédité le jour même) | Bordereau de versement n° 0042 | 400,00 |

**Pièce A3 — Comptage de la caisse du 16/11/2026, à 9 h 30 (après le versement)**

| Billets et pièces | Nombre | Montant |
|---|---|---|
| Billets de 20 € | 5 | 100,00 |
| Billets de 10 € | 10 | 100,00 |
| Billets de 5 € | 6 | 30,00 |
| Pièces de 2 € | 10 | 20,00 |
| Pièces de 1 € | 8 | 8,00 |
| Pièces de 0,50 € | 7 | 3,50 |
| Pièces de 0,20 € | 9 | 1,80 |
| Pièces de 0,10 € | 4 | 0,40 |
| Pièces de 0,05 € | 5 | 0,25 |
| **Total compté** | | **263,95** |

*R. Haddad : « J'ai rendu la monnaie à des enfants qui achetaient des crayons au stand… enfin, je crois qu'on ne vendait rien. Je ne sais plus. »*

### Partie B — Le compte à terme du siège

**Pièce B1 — Conditions du compte à terme n° 0081 (extrait du contrat, fictif)**

```
Souscripteur : Association Cap Horizons 21 – Siège
Compte à terme n° 0081 – durée 12 mois – du 01/10/2026 au 01/10/2027
Montant initial : 60 000,00 € – versé le 01/10/2026 par le débit du compte courant
Taux : 2,00 % par an, fixe (valeur contractuelle, propre à ce contrat)
Intérêts : calculés au jour le jour, base 365 jours, versés à l'échéance
Retrait partiel : possible à tout moment, par tranches de 5 000 €. Les intérêts
de la somme retirée sont versés le jour du retrait, au taux réduit de 1,00 %
par an, sur le compte courant, avec le capital retiré.
```

**Pièce B2 — Avis d'opération du 16/11/2026**

```
Retrait partiel sur CAT n° 0081
Capital retiré :                                  20 000,00
Intérêts (20 000,00 × 1,00 % × 46 jours / 365) :      25,21
Montant crédité sur le compte courant 5121000 :   20 025,21
Capital restant sur le CAT :                      40 000,00
```

**Pièce B3 — Ce qu'écrit le document interne « La comptabilité chez Trisomie 21 France » (30/04/2026)**

> *Classe 50* : « Se trouvent ici tous les placements réalisés par une structure : Livret d'épargne, comptes à terme. Lors de la souscription du placement, le compte est débité, lors de la libération des fonds, le compte est **débité**. »
>
> *Classe 27* : « Dans la classe 27, on retrouve les **parts sociales du crédit mutuel** et les dépôts et cautionnements versés (loyer, EDF, ...). »
>
> *Classe 58* : « C'est via ce compte que doivent transiter toutes les opérations réalisées entre les comptes de classe 5. […] Les comptes 58 doivent présenter un solde nul à la fin de l'exercice. »

Et dans le **plan comptable T21** : 2710000 « Titres immobilisés (droit de propriété) », mais aussi **5040000 « PSB CME T21 France (parts sociales) »**. Dans la balance du siège, les parts sociales du Crédit Mutuel (500,00 €, souscrites à l'ouverture des comptes) figurent en **5040000**.

## Travail à faire

**Partie A — Caisse**

1. Passez le retrait d'espèces du 03/11. Pourquoi faut-il **deux** écritures, dans **deux** journaux ? Pourquoi est-il interdit d'écrire directement « 5300000 au débit / 5125000 au crédit » ?
2. Passez les achats et les dons du goûter dans le journal CAASS (compte, sens, code analytique). Peut-on délivrer des reçus fiscaux pour les dons de l'urne ?
3. Passez le versement d'espèces du 16/11.
4. Calculez le **solde théorique** de la caisse au 16/11, comparez-le au comptage, et dites **comment vous traitez l'écart** : ce que vous faites **avant** de passer une écriture, puis l'écriture si l'écart reste inexpliqué. Justifiez le compte choisi à partir du plan T21, et dites quels comptes seraient faux.
5. Vérifiez que le compte **5800000** de l'ASS est soldé.

**Partie B — Compte à terme**

6. Passez la souscription du 01/10 (journaux BQSIE et PLSIE).
7. Passez le retrait partiel du 16/11, avec ses intérêts. Que pensez-vous de la phrase du document T21 « lors de la libération des fonds, le compte est débité » ?
8. **À préparer pour le 31/12/2026** : calculez les **intérêts courus non échus** (ICNE) du CAT et passez l'écriture du 31/12, puis son **extourne** du 01/01/2027. Expliquez à la trésorière, en trois phrases, pourquoi on les comptabilise alors qu'ils ne seront versés qu'en octobre 2027.
9. Vérifiez que le compte **5800000** du siège est soldé, et donnez le solde du compte 5081100 au 16/11.
10. **Parts sociales** : le document T21 et le plan T21 ne disent pas la même chose. Que fait un senior ? Quelle est, selon vous, la classification la plus défendable, et pourquoi ?

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E18-08_corrige.md)
