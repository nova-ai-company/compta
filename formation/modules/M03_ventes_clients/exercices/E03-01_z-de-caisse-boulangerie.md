# E03-01 — Le Z de caisse du samedi
**Client :** C01 — Boulangerie Dupain SARL | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** ventes en caisse, multi-taux, écart de caisse, prélèvement du gérant, logiciel certifié

**Corner case :** oui — taux de TVA mal paramétré dans la caisse et sortie d'espèces « Marc » sans justificatif

## La mise en situation

Lundi 5 octobre 2026, 14 h 10. Marc Dupain a déposé sa boîte à chaussures de septembre… et, cette fois, aussi le Z du samedi 3 octobre avec un Post-it : *« Il manque 7,50 € dans la caisse samedi, encore. Et j'ai pris 100 € pour payer le plombier en liquide, il m'a pas fait de facture. »*

Hélène Ferrand vous transmet le tout :

> « Saisissez-moi le Z du 03/10 comme modèle pour Julie (qui fera les autres). Regardez bien le paramétrage des taux : je trouve bizarre ce qu'on voit sur la ligne boissons. Et sortez-moi les écarts de caisse de la semaine, je veux en parler à Marc. Attestation du logiciel de caisse : elle est dans le dossier permanent, éditeur "CaissePro 7", attestation individuelle du 14/02/2024. »

## Les pièces

### Pièce 1 — Ticket Z n° 0274

```
================================================
        BOULANGERIE DUPAIN SARL
   12 rue de la Charité – 69002 LYON
   SIREN 912 345 001 – TVA FR 41 912345001
   Logiciel : CaissePro 7 v7.4.2 (certifié NF525)
================================================
 TICKET Z N° 0274        CLÔTURE JOURNALIÈRE
 Date : 03/10/2026   Ouverture 06:30  Clôture 19:42
 Nb tickets : 612       Caissier(e)s : JD / MD
------------------------------------------------
 VENTES PAR FAMILLE                         TTC
 Pain / baguettes (5,5 %)             1 018,60
 Viennoiseries (5,5 %)                  412,30
 Pâtisseries à emporter (5,5 %)         196,50
 Eaux, jus à emporter (5,5 %)            60,00
 Sandwichs / formules (10 %)            612,50
 Boissons chaudes sur place (10 %)      130,00
 Sodas sur place (20 %)                  54,00
 Bières / cidres sur place (20 %)        42,00
------------------------------------------------
 RÉCAPITULATIF TVA       HT        TVA       TTC
 5,5 %             1 599,43      87,97  1 687,40
 10 %                675,00      67,50    742,50
 20 %                 80,00      16,00     96,00
 TOTAL             2 354,43     171,47  2 525,90
------------------------------------------------
 RÈGLEMENTS
 Espèces                                  884,30
 Carte bancaire                         1 412,60
 Titres-restaurant (papier + carte)       229,00
 TOTAL ENCAISSÉ                         2 525,90
------------------------------------------------
 Annulations : 3 (total 11,40)  Remises : 0,00
 GT perpétuel : 1 284 512,77
 Signature : 7F3A-91C2-0D44-B8E1
================================================
```

### Pièce 2 — Feuille de caisse manuscrite (cahier de caisse)

| Libellé | Montant |
|---|---|
| Fond de caisse au matin | 150,00 |
| + Espèces encaissées (Z) | 884,30 |
| – Achat levure au marché (ticket de caisse sans mention de TVA joint) | 12,00 |
| – « Marc – plombier » (pas de justificatif) | 100,00 |
| = Espèces théoriques | ? |
| Espèces comptées le soir (billets + pièces) | 914,80 |
| Remise en banque prévue lundi 05/10 (on laisse 150,00 de fond de caisse) | ? |

### Pièce 3 — Écarts de caisse de la semaine (relevés sur le cahier)

| Jour | Écart constaté |
|---|---|
| Lundi 28/09 | – 12,00 |
| Mardi 29/09 | + 3,20 |
| Mercredi 30/09 | – 9,80 |
| Jeudi 01/10 | – 15,40 |
| Vendredi 02/10 | – 6,10 |
| Samedi 03/10 | à calculer |

### Pièce 4 — Extrait du grand livre 455 « Associé – Marc Dupain » au 30/09/2026

| Date | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|
| 01/01/2026 | À-nouveau | | 2 400,00 | 2 400,00 C |
| 30/06/2026 | Prélèvements espèces S1 | 1 850,00 | | 550,00 C |
| 31/08/2026 | Prélèvement espèces | 600,00 | | 50,00 D |

## Travail à faire

1. Contrôlez la cohérence interne du Z (ventilation par taux, règlements). Le paramétrage des taux vous paraît-il correct ? Chiffrez l'éventuelle incidence sur la journée et indiquez ce que vous recommandez.
2. Calculez les espèces théoriques, l'écart de caisse du 03/10 et le montant de la remise en banque.
3. Passez les écritures du 03/10 et de la remise en banque du 05/10 (comptes de ventes par taux, comptes de trésorerie adaptés).
4. Que faites-vous de la sortie de 100 € « Marc – plombier » ? Analysez la pièce 4.
5. Analysez les écarts de la semaine et préparez les points à aborder avec Marc.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E03-01_corrige.md)
