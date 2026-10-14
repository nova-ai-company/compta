# E08-06 — Inventaire de la Pharmacie Centrale au 30/09 : démarque, périmés et péremption courte
**Client :** C12 — Pharmacie Centrale | **Difficulté :** ★★☆ | **Durée estimée :** 45 min | **Thèmes :** inventaire permanent (logiciel d'officine) vs inventaire physique, démarque inconnue, valorisation au prix d'achat HT net (et non au prix de vente TTC), produits périmés (sortie du stock, preuve de destruction), reprise partielle par un laboratoire, dépréciation des produits à péremption courte et des références arrêtées, variation de stock créditrice

**Corner case :** oui — le chiffre de stock donné par la titulaire est le stock au prix de vente TTC

## La mise en situation

La Pharmacie Centrale SELARL clôture au **30/09/2026**. Le cabinet assure la révision et la liasse. Nous sommes le **14 octobre 2026**.

Courriel du Dr Anne Petit, pharmacienne titulaire :

> « Bonjour, d'après le logiciel, mon stock au 30/09 vaut 412 380 €. Une société d'inventaire est passée le 30 au soir, je vous joins son rapport, mais le logiciel est plus précis. J'ai aussi un bac de périmés et quelques produits qui vont périmer, je vous mets la liste. Ce sont des broutilles, non ? Anne Petit »

Hélène Ferrand : « Le logiciel d'officine donne deux valeurs : au prix d'achat et au prix de vente. Devinez laquelle Anne a recopiée. Faites-moi l'inventaire, la dépréciation et les écritures. Et regardez la démarque : en pharmacie, une démarque se commente toujours. »

Données de la balance avant inventaire :
- **37 Stocks de marchandises : 268 450,00 €** (stock au 30/09/2025) ;
- **397 Dépréciations des stocks de marchandises : 3 900,00 €** (constituée au 30/09/2025 ; les produits concernés ont tous été vendus ou détruits pendant l'exercice).

## Les pièces

**Pièce 1 — Édition du logiciel d'officine au 30/09/2026, 20 h (stock théorique)**
```
PHARMACIE CENTRALE — État du stock valorisé au 30/09/2026 — Stock théorique
Famille                                  Nb réf.   Valeur PAMP HT*   Valeur prix public TTC
Médicaments remboursables                 2 914        158 220,00            214 650,00
Médicaments non remboursables (OTC)         986         41 380,00             68 920,00
Parapharmacie / dermocosmétique            2 460         72 640,00            115 870,00
Orthopédie, matériel, divers                 412          9 400,00             12 940,00
TOTAL                                      6 772        281 640,00            412 380,00
* PAMP : prix d'achat moyen pondéré, net des remises figurant sur facture.
```

**Pièce 2 — Rapport de la société d'inventaire**
```
INVENTAIRES PRO RHÔNE SARL — SIREN 489 335 201 — Rapport d'inventaire du 30/09/2026 (20 h - 23 h 40)
Client : Pharmacie Centrale, 1 place Bellecour, 69002 Lyon
Méthode : comptage exhaustif par lecture des codes produits, 2 compteurs par zone, recomptage de 5 % des zones.
Valorisation : PAMP HT du logiciel de l'officine.
Stock physique compté (y compris le bac « périmés » de la réserve) :   279 120,00 € HT
Écart avec le stock théorique :                                         – 2 520,00 € HT (– 0,89 %)
  dont stupéfiants : écart nul (rapproché du registre des stupéfiants).
Rapport signé par le chef d'équipe et par le Dr A. Petit.
```

**Pièce 3 — Liste des périmés et des produits « à risque » préparée par le Dr Petit (valeurs PAMP HT, comprises dans le stock physique)**
```
A. Bac des périmés (péremption dépassée au 30/09/2026)
   - Médicaments remboursables périmés .................. 2 140,00 €  (non repris)
   - Médicaments non remboursables périmés ................  860,00 €  (non repris)
   - Dermocosmétique Laboratoires Alpina périmée .......... 1 520,00 €  (reprise par Alpina
     à 50 % du prix d'achat, par avoir, selon l'accord de reprise des périmés)
   Enlèvement des périmés non repris par le prestataire de collecte de l'officine le 07/10/2026
   (bordereau d'enlèvement n° DO-26-4471). Retour Alpina prévu fin octobre.

B. Péremption courte et références à risque
   - Lait infantile 1er âge (péremption 11/2026) ............  640,00 €
     Historique de l'officine sur ce type de lot : 40 % vendu avant péremption.
   - Solaires « formule 2026 » arrêtée par le laboratoire ... 1 150,00 €
     Péremption 2028 ; seront vendus en promotion à 50 % du prix de vente HT habituel.
     Prix de vente HT habituel = 1,75 x PAMP HT.
   - Tests antigéniques : 180 boîtes x 1,90 € ..............  342,00 €
     Péremption 28/02/2027 ; ventes moyennes : 10 boîtes par mois.
```

## Travail à faire

1. Quelle valeur de stock retenir : 412 380 €, 281 640 € ou 279 120 € ? Justifiez.
2. Analysez l'écart d'inventaire (démarque) : traitement comptable et diligences.
3. Traitez les produits périmés (bac A) : faut-il les sortir du stock ou les déprécier ?
4. Calculez la dépréciation au 30/09/2026 sur les produits de la liste B et sur les dermocosmétiques Alpina.
5. Passez les écritures d'inventaire au 30/09/2026.
6. Répondez au Dr Petit (« des broutilles, non ? ») et indiquez les justificatifs à conserver.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E08-06_corrige.md)
