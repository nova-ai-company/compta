# E14-01 — Facture mensuelle forfaitaire multi-sites (Riviera Mall) : TVA sur les encaissements ou option pour les débits ?
**Client :** GSF Riviera SAS (filiale régionale **fictive** du groupe GSF, dossier tenu à la comptabilité du siège) | **Difficulté :** ★★☆ | **Durée estimée :** 40 min | **Thèmes :** facturation d'un forfait de propreté multi-sites, mentions obligatoires de la facture électronique 2026, exigibilité de la TVA sur les prestations de services, option pour les débits, compte 44574, encaissement partiel, CA3

**Corner case :** oui — le modèle de facture de l'ERP porte la mention « option pour les débits » alors que la société n'a jamais opté

> *Cadre de formation : GSF Riviera SAS (SIREN fictif 999 100 206), ses établissements de Nice, Antibes et Cannes, ses clients et ses fournisseurs sont fictifs. Les personnes citées sont des personnages fictifs. Aucun chiffre réel du groupe GSF n'est utilisé.*

## La mise en situation

Vous êtes en poste depuis trois semaines à la comptabilité du siège de Sophia Antipolis. Le 30/09/2026, l'ERP a généré le brouillon de la facture mensuelle du contrat Riviera Mall avant son envoi à la plateforme agréée (PA). Sophie Garnier, responsable comptable (personnage fictif), vous transmet le brouillon :

> « Avant qu'on la pousse sur la PA, contrôlez-la. Depuis le 1er septembre, on émet tout en électronique, et la PA rejette les factures incomplètes. Au passage, j'ai un doute : je vois "TVA acquittée d'après les débits" en pied de facture. À ma connaissance, GSF Riviera n'a jamais opté. Dites-moi ce que ça change, passez les écritures de septembre et d'octobre pour ce client, et préparez-moi ce qui ira sur la CA3 de septembre. »

Informations du dossier :
- GSF Riviera SAS : régime réel normal, CA3 mensuelle, exercice du 01/01 au 31/12. Activité : prestations de nettoyage (NAF 81.21Z). **Aucune option pour le paiement de la TVA d'après les débits n'a été formulée** auprès du service des impôts.
- Comptes du dossier : 411RIVM Client Riviera Mall ; 706 Prestations de services (analytique par établissement : NIC, ANT, CAN) ; 44571 TVA collectée ; 44574 TVA collectée en attente d'encaissement ; 512 Banque.
- La facture d'août (n° FR-2026-08-0412, HT 40 620,00 €, TVA 8 124,00 €, TTC 48 744,00 €) a été émise le 31/08/2026 et **payée par virement le 22/09/2026**. Elle est correctement enregistrée en 411RIVM / 706 / 44574.
- Le 15/10/2026, Riviera Mall vire **25 000,00 €** avec le libellé « acompte sur facture septembre ».

## Les pièces

**Pièce 1 — Extrait du contrat de prestations (avenant n° 3 du 15/12/2025)**
```
Contrat RM-2024-017 – Nettoyage des parties communes des centres commerciaux
Article 3 – Prix forfaitaires mensuels HT (après révision du 01/01/2026)
   Riviera Mall Nice-Ouest .......................... 18 450,00 €
   Riviera Mall Antibes-Les Pins .................... 12 300,00 €
   Riviera Mall Cannes-La Bocca .....................  9 870,00 €
Article 4 – Prestations périodiques : vitrerie trimestrielle Nice-Ouest
   (mars, juin, septembre, décembre) ................  1 240,00 € HT par passage
Article 6 – Facturation : une facture mensuelle unique adressée au siège de
   Riviera Mall SAS, émise le dernier jour du mois, détaillant chaque site.
Article 7 – Paiement : 30 jours date de facture, par virement.
```

**Pièce 2 — Brouillon de facture généré par l'ERP (avant transmission à la PA)**
```
GSF RIVIERA SAS – Société par actions simplifiée au capital de 200 000 €
Siège : Immeuble Le Riviera (adresse fictive), 06200 Nice
RCS Nice 999 100 206 – SIREN 999 100 206 – TVA intracommunautaire FR48999100206

FACTURE N° FR-2026-09-0457                      Date d'émission : 30/09/2026
Client : RIVIERA MALL SAS – Direction administrative, 06000 Nice
         SIREN 999 200 642 – TVA FR74999200642
Nature de l'opération : prestation de services
Période : septembre 2026 – Contrat RM-2024-017

Site (adresse de réalisation)                     Qté    PU HT        Montant HT
Riviera Mall Nice-Ouest – forfait mensuel          1    18 450,00      18 450,00
Riviera Mall Nice-Ouest – vitrerie trimestrielle   1     1 240,00       1 240,00
Riviera Mall Antibes-Les Pins – forfait mensuel    1    12 300,00      12 300,00
Riviera Mall Cannes-La Bocca – forfait mensuel     1     9 870,00       9 870,00
                                                       TOTAL HT          41 860,00
                                                       TVA 20 %           8 327,00
                                                       TOTAL TTC         50 187,00

Échéance : 30/10/2026 – Paiement par virement – IBAN FR76 3000 4000 0000 0000 0000 000 (fictif)
Pas d'escompte pour paiement anticipé.
En cas de retard : pénalités au taux de 3 fois le taux d'intérêt légal ;
indemnité forfaitaire pour frais de recouvrement : 40 €.
TVA acquittée d'après les débits.
```

**Pièce 3 — Relevé bancaire GSF Riviera (extrait)**

| Date | Libellé | Débit | Crédit |
|---|---|---|---|
| 22/09/2026 | VIR RIVIERA MALL SAS FACT FR-2026-08-0412 | | 48 744,00 |
| 15/10/2026 | VIR RIVIERA MALL SAS ACOMPTE FACT SEPT | | 25 000,00 |

## Travail à faire

1. Contrôlez le brouillon de facture (pièce 2) : calculs et mentions obligatoires, y compris les mentions propres à la facture électronique depuis le 01/09/2026. Listez les corrections à apporter avant transmission à la PA.
2. Expliquez la règle d'exigibilité de la TVA applicable aux prestations de GSF Riviera, et ce qu'implique la mention « TVA acquittée d'après les débits » si elle est maintenue alors qu'aucune option n'a été exercée.
3. Passez les écritures : facture de septembre, encaissement de la facture d'août (22/09), encaissement partiel du 15/10.
4. Indiquez, pour ce client, la base et la TVA à déclarer sur la CA3 de septembre (déposée en octobre), puis celles qui iront sur la CA3 d'octobre au titre de l'encaissement du 15/10.
5. Comparez avec la situation où GSF Riviera aurait opté pour les débits : écriture de la facture de septembre et montant déclaré en septembre.
6. Préparez la réponse que vous feriez en entretien si l'on vous demandait : « Quelle est la différence entre TVA sur les débits et TVA sur les encaissements, et pourquoi c'est important en propreté ? »

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-01_corrige.md)
