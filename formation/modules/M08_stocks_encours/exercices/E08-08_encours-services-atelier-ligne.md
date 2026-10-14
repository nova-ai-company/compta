# E08-08 — En-cours de production de services de l'Atelier Ligne au 30/09
**Client :** C13 — Atelier Ligne | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** en-cours de production de services (341 / 7134), coût horaire de revient de production, exclusion des frais administratifs et commerciaux, plafonnement à la valeur recouvrable (mission suspendue), phase achevée non facturée (facture à établir, TVA sur les encaissements), acompte reçu non compensé, dépréciation 394

**Corner case :** oui — une mission suspendue par le client trois jours avant la clôture

## La mise en situation

Atelier Ligne SARL, cabinet d'architecture (IS, TVA sur les encaissements, clôture au **30/09**). Nous sommes le **16 octobre 2026**. Les missions sont facturées **par phases** (ESQ, APS, APD, PRO, DCE, DET, AOR), chaque phase étant facturable à sa remise au client.

Courriel de Camille Fabre, cogérante :

> « Bonjour, voici les feuilles de temps au 30/09 sur les phases en cours. Pour les en-cours, je propose de prendre nos heures au taux facturé de 95 €/h, c'est ce qu'elles valent vraiment. Pour Gerland, le client a mis le projet en pause, mais on a bien travaillé dessus, ça compte. Ah, et on a oublié de facturer le DCE des Quais, je le fais cette semaine. Camille »

Hélène Ferrand : « Les en-cours, c'est le poste clé de ce dossier. Je veux un tableau mission par mission : en-cours au coût, test de la valeur recouvrable, facture à établir. Et ne me compensez pas l'acompte Perrin avec l'en-cours. »

Données de la balance avant inventaire :
- **341 Études en cours : 9 450,00 €** (en-cours au 30/09/2025 ; toutes les phases correspondantes ont été achevées et facturées pendant l'exercice) ;
- **4191 Clients – avances et acomptes reçus** : 2 500,00 € (acompte HT de M. et Mme Perrin, reçu le 15/09/2026, 3 000,00 € TTC, TVA de 500,00 € déclarée) ;
- aucune dépréciation des en-cours au 30/09/2025.

## Les pièces

**Pièce 1 — Calcul du coût horaire (dossier de travail du cabinet, exercice 2025-2026)**
```
ATELIER LIGNE — Coût horaire de revient
Intervenant                     Rémunération chargée annuelle   Heures productives (missions)   Coût direct / h
Camille Fabre (cogérante)                  78 000,00 €                   1 300 h                    60,00 €
Nicolas Brun (cogérant)                    78 000,00 €                   1 300 h                    60,00 €
Léa Moulin (architecte salariée)           56 000,00 €                   1 400 h                    40,00 €
Hugo Petit (dessinateur-projeteur)         42 000,00 €                   1 500 h                    28,00 €
Total heures productives                                                  5 500 h

Charges de production (logiciels CAO/BIM, traceur, postes de travail,
quote-part des locaux de l'atelier de conception) : 38 500,00 € / 5 500 h = 7,00 €/h
Frais administratifs et commerciaux (secrétariat, comptabilité, honoraires,
concours, site internet, prospection) : 49 500,00 € / 5 500 h = 9,00 €/h
Taux horaire moyen facturé aux clients : 95,00 € HT
```

**Pièce 2 — Extrait des contrats de maîtrise d'œuvre et état des phases au 30/09/2026**
```
Mission A — Maison individuelle Perrin (particuliers) — Honoraires 36 000,00 € HT
  Répartition : ESQ 5 % — APS 10 % — APD 15 % — PRO 20 % — DCE 10 % — DET 35 % — AOR 5 %
  ESQ, APS, APD : achevées et facturées. PRO : commencée le 01/09/2026, remise prévue le 15/11/2026.
  Acompte reçu le 15/09/2026 sur la phase PRO : 3 000,00 € TTC.

Mission B — Restaurant « Les Quais » — SCI Les Quais de Saône (SIREN 853 210 774) — Honoraires 54 000,00 € HT
  DCE (10 %) : remis au client le 25/09/2026 (accusé de réception par e-mail du 25/09). Non facturé au 30/09.
  DET : non commencée (début du chantier prévu en novembre).

Mission C — Bureaux Gerland — Gerland Office SAS (SIREN 901 456 220) — Honoraires 80 000,00 € HT
  APS (10 %) : commencé le 10/07/2026. Art. 9 du contrat : « En cas de suspension supérieure à trois mois
  ou d'abandon du projet par le maître d'ouvrage, les honoraires de la phase en cours sont dus au
  prorata des prestations réalisées. »

Mission D — Rénovation maison Vasseur (particulier) — Honoraires 24 000,00 € HT
  ESQ (5 %) : commencée le 22/09/2026.
```

**Pièce 3 — Feuilles de temps au 30/09/2026 sur les phases en cours (heures) et estimations à terminaison**
```
Mission / phase      Camille   Nicolas   Léa    Hugo   |  Reste à faire estimé (h)
A — PRO                 22        —       30      64    |  Camille 6 — Léa 10 — Hugo 30
C — APS                 40       35       60      30    |  (mission suspendue)
D — ESQ                  —        6        —      10    |  Hugo 4
```

**Pièce 4 — Courrier de Gerland Office SAS**
```
GERLAND OFFICE SAS — Lyon, le 27/09/2026 — LRAR
Objet : suspension du projet de bureaux — avenue Tony Garnier
Madame, Monsieur, notre financement bancaire ayant été refusé, nous vous informons de la suspension
du projet à compter de ce jour. Nous reviendrons vers vous d'ici la fin de l'année pour vous indiquer
si le projet est relancé ou abandonné. Veuillez agréer…   Le Président
```
Note de Nicolas Brun (09/10/2026) : « Avancement réel de l'APS Gerland : environ 70 %. Gerland Office est une filiale d'un groupe immobilier solide, aucun doute sur sa solvabilité. »

## Travail à faire

1. Distinguez, pour chaque mission, ce qui relève d'un en-cours, d'une facture à établir ou d'aucune écriture.
2. Calculez le coût horaire de revient **de production** de chaque intervenant. Pourquoi ne pas retenir le taux de 95 €/h proposé par Camille ?
3. Valorisez les en-cours au 30/09/2026 et testez, mission par mission, leur valeur recouvrable. Calculez la dépréciation éventuelle.
4. Passez les écritures d'inventaire au 30/09/2026 (en-cours, dépréciation, facture à établir) et commentez le traitement de la TVA.
5. Expliquez pourquoi l'acompte Perrin n'est pas déduit de l'en-cours.
6. Chiffrez l'écart entre la proposition de Camille et votre calcul et rédigez la réponse.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E08-08_corrige.md)
