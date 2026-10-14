# E06-01 — L'immeuble du Gerland : coût d'entrée et plan d'amortissement par composants
**Client :** C07 — SCI Horizon Pro | **Difficulté :** ★★☆ | **Durée estimée :** 1 h | **Thèmes :** coût d'acquisition d'un immeuble, option frais d'acquisition, terrain, approche par composants, durées résiduelles, prorata temporis, dépôts de garantie repris, frais d'emprunt

**Corner case :** oui — un décompte de notaire qui mélange prix, frais du prêt et dépôts de garantie des locataires.

## La mise en situation

Lundi 12 octobre 2026. La SCI Horizon Pro (IS sur option, TVA sur les loyers par option) a acquis le 1er avril 2026 un second immeuble de bureaux à Lyon 7e, déjà loué à trois sociétés. La comptabilité courante est préparée par la comptable de Delta Invest (associée à 40 %), qui a créé la fiche d'immobilisation et vous l'envoie « pour validation rapide ».

Note d'Hélène Ferrand :

> « Je ne valide pas une fiche à 1,9 M€ en cinq minutes. Reprenez le décompte du notaire, isolez ce qui fait partie du coût, ventilez avec le rapport de l'expert et faites-moi le plan par composants. Les associés veulent savoir ce que change l'option "frais d'acquisition en charges" sur le résultat 2026 : chiffrez-moi les deux. Rappel : nous retenons l'année de 360 jours. »

## Les pièces

**Pièce 1 — Décompte de l'office notarial (extrait)**

```
SCP MARCHAND & VIAL — Notaires associés — 18 quai Saint-Antoine, 69002 Lyon
DÉCOMPTE ACQUÉREUR — Dossier 2026-0412 — Acte de vente signé le 01/04/2026
Acquéreur : SCI HORIZON PRO — SIREN 798 333 120 — 120 rue Garibaldi, 69006 Lyon
Vendeur   : FONCIÈRE DU CONFLUENT SAS — SIREN 509 774 218
Bien : immeuble de bureaux R+3, 7 rue Marcel-Mérieux, 69007 Lyon — 1 420 m² utiles —
       construit en 1998 — cadastre section BK n° 112 (terrain 1 150 m²)
Régime : vente d'un immeuble achevé depuis plus de 5 ans, sans option du vendeur pour la TVA

                                                                     DÉBIT          CRÉDIT
Prix de vente                                                    1 800 000,00
Droits d'enregistrement et taxe de publicité foncière (*)          104 520,00
Contribution de sécurité immobilière                                  1 800,00
Émoluments du notaire (vente) HT                                     18 400,00
TVA 20 % sur émoluments                                               3 680,00
Débours et formalités (vente)                                         1 200,00
Frais de l'acte de prêt et inscription du privilège de prêteur
  de deniers (Banque Rhône-Alpes Entreprises)                         9 600,00
Dépôts de garantie des locataires en place, repris par
  l'acquéreur (art. 7 de l'acte)                                                      45 000,00
Fonds versés par la Banque Rhône-Alpes Entreprises (prêt)                         1 400 000,00
Provision versée par l'acquéreur le 25/03/2026                                      494 200,00
                                                                 ----------------------------
TOTAUX                                                           1 939 200,00      1 939 200,00
(*) taux départemental applicable à la date de l'acte — à vérifier
```

**Pièce 2 — Facture de l'agence**

```
LYON TERTIAIRE CONSEIL SARL — Transaction en immobilier d'entreprise
5 place des Jacobins, 69002 Lyon — SIREN 834 102 556 — TVA FR 41 834 102 556
Carte professionnelle CPI 6901 2019 000 041 xxx — Garantie financière : Galian
FACTURE N° LTC-2026-031                                    Date : 01/04/2026
Client : SCI HORIZON PRO — SIREN 798 333 120 — 120 rue Garibaldi, 69006 Lyon
Nature de l'opération : prestation de services
Honoraires de négociation — acquisition 7 rue Marcel-Mérieux (mandat de recherche
du 12/11/2025, à la charge de l'acquéreur)                   HT    54 000,00
                                                           TVA 20 % 10 800,00
                                                           TTC     64 800,00
Échéance : 30/04/2026. Pénalités de retard : 3 × taux d'intérêt légal ; indemnité forfaitaire 40 €.
```

**Pièce 3 — Rapport d'évaluation (extrait) — Cabinet Expertim, expert près la cour d'appel**

```
Répartition de la valeur globale de l'ensemble immobilier (à appliquer au coût total d'acquisition) :
  Terrain ......................................................  20 %
  Constructions ................................................  80 %
     dont (en % des constructions) :
       Structure / gros œuvre ..................................  50 %   durée résiduelle 40 ans
       Façades et menuiseries extérieures ......................  15 %   durée résiduelle 20 ans
       Toiture et étanchéité (réfection 2011) ..................  10 %   durée résiduelle 15 ans
       Installations techniques (CVC, électricité, ascenseur) ..  15 %   durée résiduelle 15 ans
       Agencements intérieurs (plateaux, sanitaires) ...........  10 %   durée résiduelle 10 ans
Valeur résiduelle des composants en fin de durée : non significative.
```

**Pièce 4 — Fiche d'immobilisation préparée par la comptable de Delta Invest**

```
N° IMM-2026-01 — Immeuble Mérieux — Compte 2131 — Date de mise en service : 01/04/2026
Valeur d'origine : 1 944 520,00 € (total décompte notaire hors TVA + honoraires agence HT)
Mode : linéaire 30 ans — Dotation 2026 : 48 613,00 €
Commentaire : "durée des bureaux dans le logiciel"
```

**Pièce 5 — Informations complémentaires**
- Les trois baux en cours sont repris par la SCI ; les loyers sont soumis à la TVA (option).
- L'emprunt de 1 400 000 € est amortissable sur 15 ans (module M05 pour les échéances).
- La SCI a retenu, pour son premier immeuble, l'**incorporation des frais d'acquisition au coût** des immobilisations.
- Résultat 2026 prévisionnel de la SCI avant prise en compte de ce nouvel immeuble (amortissements et frais) : 96 000 €.

## Travail à faire

1. Analysez le décompte du notaire : pour chaque ligne, indiquez si elle fait partie du coût d'acquisition de l'immeuble, et justifiez. Calculez le coût d'acquisition total.
2. L'option « frais d'acquisition en charges » est-elle encore ouverte pour cet immeuble ? Chiffrez néanmoins, pour éclairer les associés, l'impact sur le résultat 2026 des deux traitements (coût / charges).
3. Ventilez le coût entre le terrain et les composants ; établissez le **plan d'amortissement** (dotation annuelle, dotation 2026, et tableau 2026 → 2030).
4. Passez les écritures : versement de la provision, déblocage du prêt, acquisition (acte et facture d'agence), dotation au 31/12/2026.
5. Listez les erreurs de la fiche préparée par la comptable de Delta Invest et chiffrez l'écart de dotation 2026.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E06-01_corrige.md)
