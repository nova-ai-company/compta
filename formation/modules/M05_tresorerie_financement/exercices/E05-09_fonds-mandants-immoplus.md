# E05-09 — Le compte séquestre d'ImmoPlus : fonds des mandants et honoraires
**Client :** C22 — ImmoPlus SARL | **Difficulté :** ★★★ | **Durée estimée :** 60 min | **Thèmes :** fonds de tiers, compte séquestre, loi Hoguet, honoraires de gestion, dépôts de garantie, représentation des fonds, virements internes

**Corner case :** oui — des fonds des mandants ont servi à payer une dette de l'agence.

## La mise en situation

Une nouvelle assistante du cabinet, Lou, a repris la tenue d'ImmoPlus en septembre 2026. Pour « être exhaustive », elle a importé dans la comptabilité de l'agence le relevé du **compte séquestre** (compte « fonds mandants ») en plus du compte courant de l'agence. Résultat : le chiffre d'affaires de septembre est passé de 50 000 € environ à plus de 200 000 €.

Frédéric Blanc, gérant, ravi :
> « Super mois ! Au fait, j'ai fait un petit virement de 6 000 € du compte mandants vers le compte de l'agence le 21, pour payer l'URSSAF à temps. Je remets ça début octobre, les propriétaires n'ont rien vu. »

Hélène Ferrand : « Stop. On remet tout d'aplomb, et on parle à Frédéric aujourd'hui. Le garant financier ne rigole pas avec ça. »

## Les pièces

### Pièce 1 — Relevé du compte séquestre, septembre 2026 (résumé par nature)

```
BANQUE RHÔNE GESTION — Compte spécial « Fonds de tiers — Mandants » — Loi n° 70-9 du 2 janvier 1970
Titulaire : SARL IMMOPLUS — Gestion locative — Carte professionnelle G n° CPI 6901 2019 000 041 221
IBAN FR76 1009 6180 0400 0412 3456 789
```

| Date | Libellé | Débit | Crédit | Solde |
|---|---|---|---|---|
| 01/09 | Solde créditeur | | | 214 380,00 |
| 02/09 → 10/09 | Encaissements loyers et charges des locataires (prélèvements SEPA et virements, 178 lots) | | 186 400,00 | 400 780,00 |
| 04/09 → 18/09 | Dépôts de garantie reçus — 3 nouveaux baux | | 4 800,00 | 405 580,00 |
| 11/09 | Restitution dépôt de garantie — sortie locataire M. Akkari (lot 112, propriétaire M. Vidal) | 2 200,00 | | 403 380,00 |
| 14/09 | Règlement Hydro Services SARL — fuite lot 47 (propriétaire Mme Roux), ordre de service du 03/09 | 640,00 | | 402 740,00 |
| 15/09 | Reversements aux propriétaires (comptes rendus de gérance de septembre) | 162 300,00 | | 240 440,00 |
| 15/09 | Virement vers compte agence — honoraires de gestion septembre | 15 657,60 | | 224 782,40 |
| 21/09 | Virement vers compte agence — « URSSAF agence » | 6 000,00 | | 218 782,40 |
| 30/09 | **Solde créditeur** | | | **218 782,40** |

### Pièce 2 — Mandat de gestion type (extrait)
> « Rémunération du mandataire : 7 % HT des sommes encaissées (loyers et charges) pour le compte du mandant, TVA au taux en vigueur en sus, prélevée lors de chaque reddition de compte. »

### Pièce 3 — Saisie de Lou dans la comptabilité de l'agence (septembre 2026)

| Compte débité | Compte crédité | Libellé | Montant |
|---|---|---|---|
| 512SEQ Banque séquestre | 706200 Loyers encaissés | Loyers locataires septembre | 186 400,00 |
| 512SEQ | 165 Dépôts et cautionnements reçus | DG reçus 3 baux | 4 800,00 |
| 165 | 512SEQ | Restitution DG Akkari | 2 200,00 |
| 615 Entretien et réparations | 512SEQ | Hydro Services fuite lot 47 | 640,00 |
| 6228 Rémunérations d'intermédiaires | 512SEQ | Reversements propriétaires | 162 300,00 |
| 580 Virements internes | 512SEQ | Virement honoraires vers agence | 15 657,60 |
| 580 | 512SEQ | Virement URSSAF | 6 000,00 |
| 512AG Banque agence | 580 | Virement reçu du séquestre (honoraires) | 15 657,60 |
| 512AG | 580 | Virement reçu du séquestre | 6 000,00 |

Le solde d'ouverture du séquestre (214 380,00 €) n'a pas été repris. Aucune facture d'honoraires de gestion n'a été comptabilisée pour septembre.

### Pièce 4 — État de la comptabilité mandants (logiciel de gestion locative) au 30/09/2026

| Rubrique | Montant |
|---|---|
| Soldes créditeurs des comptes propriétaires (loyers encaissés non encore reversés) | 151 912,40 |
| Dépôts de garantie détenus pour le compte des bailleurs | 70 470,00 |
| Locataires créditeurs (trop-perçus) | 2 400,00 |
| **Total des fonds dus aux mandants et aux tiers** | **224 782,40** |

## Travail à faire
1. Expliquez pourquoi les loyers encaissés pour le compte des propriétaires ne sont pas le chiffre d'affaires d'ImmoPlus, et quel est le seul produit de l'agence dans ces flux.
2. Contrôlez le montant des honoraires de gestion prélevés en septembre.
3. Comparez le solde du compte séquestre avec l'état de la comptabilité mandants : que constatez-vous ?
4. Passez les écritures de correction dans la comptabilité de l'agence (méthode retenue : la comptabilité mandants est tenue séparément dans le logiciel de gestion ; la comptabilité générale de l'agence n'enregistre que ses propres opérations).
5. Analysez le virement de 6 000 € (réglementation, risques) et comptabilisez sa restitution le 02/10/2026.
6. Préparez les points de l'entretien avec Frédéric Blanc et les contrôles à mettre en place.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E05-09_corrige.md)
