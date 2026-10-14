# E11-03 — TechNova : augmentation de capital avec prime d'émission et frais
**Client :** C08 — TechNova SAS | **Difficulté :** ★★★ | **Durée estimée :** 1 h | **Thèmes :** augmentation de capital en numéraire, prime d'émission, libération partielle (¼ du nominal + totalité de la prime), compte 4563, certificat du dépositaire, frais d'augmentation de capital imputés sur la prime, suppression des comptes de transfert de charges, effets fiscaux

**Corner case :** oui — une souscription libérée du quart seulement du nominal (le capital n'est plus « entièrement libéré ») et des frais dont une partie n'est pas imputable.

## La mise en situation

Mardi 30 mars 2027. TechNova vient de boucler sa levée de fonds « seed+ ». Émilie Roux, DAF à temps partagé, vous envoie son projet d'écritures :

> « Bonjour, voici ce que j'ai passé pour l'augmentation de capital. J'ai mis tous les frais en honoraires puis en transfert de charges vers la prime, comme on faisait chez mon ancien employeur. Petite question : Claire Vasseur voulait ne verser que la moitié de la prime d'émission, comme pour le nominal. J'ai refusé, j'ai bien fait ? Et Yanis demande si le fait que Claire n'ait pas tout versé pose un problème "fiscal". Merci ! Émilie »

Hélène Ferrand : « Corrigez le projet d'Émilie et faites-lui une note claire. Pensez à la fiscalité : TechNova prévoit une perte fiscale en 2027 (voir E10-05), et Yanis a un compte courant rémunéré. »

## Les pièces

**Pièce 1 — Procès-verbal de l'AGE du 12/03/2027 (extraits)**

```
TECHNOVA — SAS au capital de 54 000 € — 30 quai Perrache, 69002 Lyon — RCS Lyon 879 654 321
ASSEMBLÉE GÉNÉRALE EXTRAORDINAIRE DU 12 MARS 2027

Deuxième résolution — Augmentation de capital en numéraire avec suppression du droit
préférentiel de souscription au profit de personnes dénommées
L'assemblée générale, après avoir pris connaissance du rapport du Président et du rapport
du commissaire aux comptes désigné à cet effet, décide d'augmenter le capital social d'un
montant nominal de 6 000 € par l'émission de 6 000 actions ordinaires nouvelles de 1 € de
valeur nominale, émises au prix unitaire de 50 €, soit avec une prime d'émission de 49 €
par action (prime totale : 294 000 €).
Les actions nouvelles devront être libérées, lors de la souscription, du quart au moins de
leur valeur nominale et de la totalité de la prime d'émission.
Souscripteurs : FPCI RHÔNE CAPITAL SEED II (5 400 actions) ; Mme Claire VASSEUR (600 actions).

Troisième résolution — Modification corrélative des statuts (sous condition de réalisation)
```

**Pièce 2 — Bulletins de souscription (synthèse)**

| Souscripteur | Actions | Prix total | Libération déclarée au bulletin | Montant versé |
|---|---|---|---|---|
| FPCI Rhône Capital Seed II (représenté par sa société de gestion, SIREN 834 220 916) | 5 400 | 270 000,00 € | Intégrale | 270 000,00 € |
| Mme Claire Vasseur (business angel) | 600 | 30 000,00 € | ¼ du nominal + totalité de la prime | 29 550,00 € |

**Pièce 3 — Relevé du compte bloqué et certificat du dépositaire**

```
BANQUE RHODANIENNE — Compte « augmentation de capital TechNova » (indisponible)
19/03/2027  VIR FPCI RHONE CAPITAL SEED II  SOUSCRIPTION TECHNOVA     + 270 000,00
19/03/2027  VIR VASSEUR CLAIRE  SOUSCRIPTION TECHNOVA                 +  29 550,00

CERTIFICAT DU DÉPOSITAIRE du 24/03/2027
La banque certifie avoir reçu la somme de 299 550,00 € représentant la libération de
6 000 actions nouvelles de la société TechNova, à savoir 5 550 € au titre du nominal et
294 000 € au titre de la prime d'émission. Les fonds sont mis à la disposition de la société.
Frais de délivrance du certificat : 300,00 € (exonérés de TVA), prélevés le 24/03/2027.
```

**Pièce 4 — Factures de frais**

```
LEX RHÔNE AVOCATS — SIREN 812 667 340 — TVA FR 23 812667340
Facture n° LR-27-0331 du 26/03/2027 — Client : TechNova SAS (SIREN 879 654 321)
1. Opération d'augmentation de capital : rapport du Président, PV d'AGE,
   bulletins, formalités                                          9 500,00 €
2. Pacte d'associés (exigé par le FPCI comme condition de la souscription,
   signé le 24/03/2027)                                            2 500,00 €
3. Mise à jour du règlement du plan de BSPCE 2027                  2 500,00 €
Total HT 14 500,00 € — TVA 20 % 2 900,00 € — TTC 17 400,00 €
Échéance : 25/04/2027. Indemnité forfaitaire pour frais de recouvrement : 40 €.

CAPITAL BRIDGE CONSEIL — SIREN 901 455 208 — TVA FR 68 901455208
Facture n° CB-2027-014 du 25/03/2027 — Client : TechNova SAS
Commission de succès : 3 % × 300 000 € levés                       9 000,00 €
TVA 20 % 1 800,00 € — TTC 10 800,00 € — Échéance : 24/04/2027

ANNONCES & FORMALITÉS RHÔNE — SIREN 529 870 114
Facture n° AF-5521 du 27/03/2027 — Avis de modification du capital + dépôt au greffe
HT 250,00 € — TVA 20 % 50,00 € — TTC 300,00 €
```

**Pièce 5 — Projet d'écritures d'Émilie**

```
24/03/2027  512   Banque                                  300 000,00
            1013  Capital souscrit appelé versé                         6 000,00
            1041  Prime d'émission                                    294 000,00

31/03/2027  6226  Honoraires (Lex Rhône + Capital Bridge + formalités + banque) 24 050,00
            44566 TVA déductible                                 4 750,00
            401   Fournisseurs                                             28 500,00
            512   Banque                                                      300,00
31/03/2027  1041  Prime d'émission                             24 050,00
            791   Transfert de charges d'exploitation                      24 050,00
```

**Pièce 6 — Informations complémentaires (valeurs à vérifier chaque année)**

```
- Capitaux propres avant l'opération : capital 54 000 € (54 000 actions de 1 €, entièrement
  libéré) ; prime d'émission 1 196 000 € (levées antérieures).
- Répartition du capital avant l'opération : Yanis Haddad 62 %, deux cofondateurs 18 %,
  business angels personnes physiques 12 %, FCPI 8 %.
- Compte courant de Yanis Haddad : 80 000 €, rémunéré au taux de 4 %.
- Prévision 2027 : perte fiscale (environ – 180 000 €) ; déficits reportables importants.
- Taux normal de l'IS : 25 %.
- TechNova est redevable de la TVA sur la totalité de son chiffre d'affaires.
```

## Travail à faire

1. Calculez le nombre et le montant des actions, la prime d'émission, le capital appelé et non appelé après l'opération, et la nouvelle répartition du capital.
2. Émilie a-t-elle eu raison de refuser que Claire Vasseur ne verse que la moitié de la prime ?
3. Relevez les erreurs du projet d'écritures d'Émilie.
4. Passez les écritures correctes : réception des fonds (19/03/2027), réalisation de l'augmentation (24/03/2027, schéma complet), frais (31/03/2027).
5. Quel traitement fiscal pour les frais imputés sur la prime ? Pourquoi n'y a-t-il pas lieu de les imputer « nets d'impôt » ici ? Chiffrez ce qu'aurait été l'effet d'impôt pour une société imposée à 25 %.
6. Répondez à la question de Yanis : la libération partielle de Claire pose-t-elle un problème fiscal ? Que conseillez-vous ?
7. Listez les formalités juridiques post-opération.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E11-03_corrige.md)
