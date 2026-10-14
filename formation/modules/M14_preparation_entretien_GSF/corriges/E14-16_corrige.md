# Corrigé E14-16 — Perte d'un marché et reprise du personnel (article 7 de la CCN propreté) ; gain d'un marché avec reprise de salariés

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-16](../exercices/E14-16_perte-gain-marche-reprise-personnel-article7.md)

*Rappel : règles de l'article 7 résumées et simplifiées pour l'exercice — texte en vigueur à vérifier.*

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Qui part, qui reste, que paie-t-on ?
- **Les 8 salariés A à H** remplissent les conditions (affectés depuis plus de 6 mois, en poste) : leurs contrats sont **transférés** à NetAzur Services au 01/11/2026. Ce transfert conventionnel n'est pas un licenciement : **pas d'indemnité de licenciement**, pas de préavis. GSF Riviera verse avec la paie d'octobre le **salaire d'octobre** (paie normale) et l'**indemnité compensatrice des congés payés acquis et non pris** (9 640,00 € brut), puis établit les documents de fin de relation avec GSF Riviera (bulletin, attestation, certificat).
- **I. Durand**, absente depuis plus de 4 mois à la date du transfert, ne remplit pas les conditions : son contrat **reste chez GSF Riviera**. À son retour, il faudra lui proposer une affectation sur un autre site (sujet RH). Comptablement, ses congés acquis restent dans la provision 4282 de GSF Riviera.
- La **provision pour congés payés** des 8 salariés (déjà constatée) est **reprise** au moment où l'indemnité est versée : la charge réelle remplace l'estimation, seul l'écart affecte le résultat.

### Question 3 — Autres conséquences de la perte du marché
- **Chiffre d'affaires** : dernière facture forfaitaire au 31/10 (9 870,00 € HT) ; plus de facturation à compter de novembre → mise à jour du **budget / reporting** de l'établissement de Cannes.
- **Remise en état du 30/10** (1 450,00 € HT) : réalisée en octobre sur devis accepté → **FAE au 31/10** (D 4181 / C 706 / C 44587), facture en novembre.
- **Matériel** (VNC 4 200,00 €) : réaffecté à Carros → **pas de dépréciation** ; mise à jour du fichier des immobilisations (établissement et site de rattachement, analytique). S'il n'était pas réutilisable, il faudrait examiner une dépréciation ou une cession.
- **Produits stockés** : déjà en charges (pas de suivi de stock) → rapatriement physique, pas d'écriture ; s'ils étaient abandonnés au client, rien non plus (sauf refacturation prévue au contrat).
- **Contrats fournisseurs liés au site** (location de bennes, contrat déchets, ligne téléphonique, badges) : à **résilier** pour éviter des FNP orphelines après le 31/10.
- **Créances** : surveiller le paiement des dernières factures de Riviera Mall (un client qui part paie parfois moins vite) ; lettrer les avoirs éventuels de fin de contrat (pénalités).

### Question 4 — Côté entrant (Agrodélices Carros)
- **Congés payés** : les 6 salariés arrivent avec **0 jour de congé acquis chez GSF Riviera** (le sortant les a indemnisés) → **pas de dette de CP à reprendre** ; la provision 4282 se constituera progressivement à partir de novembre. Point RH : ces salariés ne pourront pas prendre de congés payés rémunérés avant d'en avoir acquis (souvent source de demandes de congés sans solde).
- **Ancienneté reprise** (9 ans en moyenne) : effet sur la **prime d'ancienneté** dès la première paie (à intégrer au chiffrage du marché) et sur l'**engagement d'indemnités de départ à la retraite** : si le groupe comptabilise une provision pour IDR (méthode préférentielle) ou la mentionne en engagement hors bilan, l'engagement augmente immédiatement, sans contrepartie → à signaler au service consolidation / actuariat.
- **Frais de démarrage** (visites médicales, badges, EPI et tenues, formation : 4 100,00 € HT) : **charges** de la période (pas d'activation de frais de démarrage d'un contrat de services dans les comptes individuels, sauf éléments répondant à la définition d'une immobilisation — par exemple du matériel durable).
- **Pas d'écriture « d'entrée » des salariés** : un transfert conventionnel n'est pas une acquisition, rien n'est payé au sortant.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Indemnité compensatrice CP (brut) | calcul paie | 9 640,00 € |
| Cotisations salariales | 9 640,00 × 22 % | 2 120,80 € |
| Net versé (hors PAS, ignoré ici) | 9 640,00 − 2 120,80 | 7 519,20 € |
| Cotisations patronales | 9 640,00 × 42 % | 4 048,80 € |
| Provision CP reprise | | 9 480,00 € |
| Provision charges sociales reprise | 9 480,00 × 42 % | 3 981,60 € |
| **Impact net sur le résultat d'octobre** | (9 640,00 − 9 480,00) + (4 048,80 − 3 981,60) | **227,20 €** de charge |
| URSSAF (sal. + pat., hypothèse : tout à l'URSSAF pour simplifier) | 2 120,80 + 4 048,80 | 6 169,60 € |
| FAE remise en état | 1 450,00 + TVA 290,00 | 1 740,00 € TTC |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 31/10/2026 | OD-PAIE | 6412 | Congés payés | ICCP 8 salariés transférés art. 7 – Cannes-La Bocca | 9 640,00 | |
| 31/10/2026 | OD-PAIE | 6451 | Cotisations à l'URSSAF | Patronal sur ICCP transférés (42 %) | 4 048,80 | |
| 31/10/2026 | OD-PAIE | 431 | Sécurité sociale (URSSAF) | Sal. + pat. sur ICCP transférés | | 6 169,60 |
| 31/10/2026 | OD-PAIE | 421 | Personnel – rémunérations dues | Net ICCP 8 salariés transférés | | 7 519,20 |
| 31/10/2026 | OD | 4282 | Dettes provisionnées pour congés payés | Reprise provision CP 8 salariés transférés | 9 480,00 | |
| 31/10/2026 | OD | 6412 | Congés payés | Reprise provision CP 8 salariés transférés | | 9 480,00 |
| 31/10/2026 | OD | 4382 | Charges sociales sur congés à payer | Reprise provision charges CP transférés | 3 981,60 | |
| 31/10/2026 | OD | 645 | Charges de sécurité sociale et de prévoyance | Reprise provision charges CP transférés | | 3 981,60 |
| 31/10/2026 | OD | 4181 | Clients – factures à établir | FAE remise en état fin de contrat Cannes-La Bocca | 1 740,00 | |
| 31/10/2026 | OD | 706 | Prestations de services (CAN) | FAE remise en état fin de contrat Cannes-La Bocca | | 1 450,00 |
| 31/10/2026 | OD | 44587 | Taxes sur le CA sur factures à établir | FAE remise en état – TVA | | 290,00 |
| | | | | **Totaux** | **28 890,40** | **28 890,40** |

> Les salaires d'octobre suivent l'écriture de paie habituelle (voir E14-15). L'écriture d'ICCP est ici isolée pour la lisibilité ; dans l'ERP, elle fait partie de la paie d'octobre. Dans la réalité, les cotisations se répartissent entre URSSAF, retraite complémentaire, prévoyance, et le PAS est retenu sur l'indemnité.

## 4. Points d'attention / pièges

- **Provisionner une indemnité de licenciement** pour les salariés transférés : erreur, il n'y a pas de licenciement.
- **Oublier de reprendre la provision CP** : la charge serait comptée deux fois (provision + indemnité versée), soit ici 13 461,60 € de charge en trop.
- **Garder dans la provision CP des salariés partis** : la provision doit être recalculée nominativement ; I. Durand y reste.
- **Côté entrant, constater une dette de CP** « reprise » : non, le sortant a payé.
- **Ancienneté reprise et IDR** : ce n'est pas l'aide-comptable qui calcule l'engagement, mais c'est elle qui alerte (liste des salariés repris avec dates d'ancienneté transmise au service en charge).
- **Calendrier** : la paie d'octobre des transférés doit être **définitive** (soldes) ; une erreur découverte après le transfert oblige à des régularisations sur des salariés sortis.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Réponse d'entretien (question 5)** :
> « En propreté, quand un client change de prestataire, l'article 7 de la convention collective organise la reprise par l'entreprise entrante des salariés affectés au marché, s'ils remplissent les conditions d'ancienneté sur le site et de présence. Pour l'entreprise sortante, ce n'est pas un licenciement : elle verse le salaire jusqu'au transfert et une indemnité compensatrice des congés acquis, et je pense à reprendre la provision congés payés correspondante. Pour l'entrante, les salariés arrivent avec leur ancienneté mais sans congés acquis, donc sans dette de congés, et l'ancienneté a un coût : primes, engagements de retraite. Comptablement, il faut aussi gérer la fin du marché : dernière facture, FAE, matériel réaffecté, contrats fournisseurs à résilier. »

**Check-list « fin de marché » pour l'établissement** : liste du personnel transmise dans les délais ; paie de sortie ; dernière facture + FAE ; restitution des badges et clés ; inventaire du matériel et réaffectation ; résiliation des contrats fournisseurs liés ; suivi du dernier encaissement. **Check-list « nouveau marché »** : création du site en analytique, du client et de ses exigences de facturation (BC, plateforme), paramétrage des primes conventionnelles du site, budget de démarrage.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Convention collective nationale des entreprises de propreté et services associés (IDCC 3043), **article 7** « Conditions de garantie de l'emploi et continuité du contrat de travail du personnel en cas de changement de prestataire » (*texte en vigueur et avenants à vérifier*).
- Code du travail art. L. 1224-1 (transfert légal, non applicable en principe à une simple perte de marché, d'où le dispositif conventionnel), L. 3141-28 (indemnité compensatrice de congés payés).
- PCG : comptes 4282, 4382, 6412, 645 ; recommandation ANC n° 2013-02 relative aux engagements de retraite (*à vérifier*).
