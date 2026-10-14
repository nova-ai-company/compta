# E14-13 — Balance âgée fournisseurs, fournisseurs débiteurs et délais de paiement (LME) : analyser avant le comité
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) | **Difficulté :** ★★☆ | **Durée estimée :** 50 min | **Thèmes :** balance âgée, lecture des soldes anormaux, acompte mal classé, double paiement, avoir non imputé, paiement par carte non lettré, délais de paiement légaux, pénalités de retard et indemnité de 40 €, amende administrative, DPO

**Corner case :** oui — un solde « échu à plus de 90 jours » qui n'est pas une dette (facture déjà payée par carte, paiement resté en compte d'attente)

> *Cadre de formation : sociétés, montants et personnes fictifs.*

## La mise en situation

Vendredi 02/10/2026. Le comité mensuel « BFR » de GSF Riviera se tient mardi. Sophie Garnier (personnage fictif) :

> « Le directeur financier régional veut une lecture de la balance âgée fournisseurs au 30/09 : ce qui est vraiment en retard, pourquoi, quel risque au regard des délais de paiement, et les soldes anormaux corrigés. Une page, pas plus, plus les écritures. »

Informations :
- Conditions de paiement négociées : produits et matériel : **45 jours fin de mois** ; intérim : **30 jours date de facture** ; sous-traitance : 45 jours fin de mois ; LLD : prélèvement à réception ; loyers : terme à échoir le 1er du trimestre ; SaaS : paiement par carte à réception.
- Délai légal maximal (Code de commerce) : **60 jours à compter de la date d'émission de la facture**, ou par dérogation **45 jours fin de mois** si convenu ; à défaut de convention, 30 jours (*à vérifier*).
- Pénalités de retard prévues dans les CGV des fournisseurs : **taux BCE + 10 points**, soit **12,15 %** retenu (*à vérifier*) ; indemnité forfaitaire **40 € par facture**.
- Amende administrative pour non-respect des délais de paiement : jusqu'à **2 000 000 € pour une personne morale**, doublée en cas de réitération, avec publication de la sanction (*montants à vérifier*).
- Achats TTC des 12 derniers mois : **1 520 000,00 €**.
- Comptes : 401 (par tiers), 4091 Fournisseurs – avances et acomptes versés sur commandes, 4097 Fournisseurs – autres avoirs (créances), 471 Compte d'attente.

## Les pièces

**Pièce 1 — Balance âgée fournisseurs au 30/09/2026 (TTC, en €, soldes créditeurs positifs)**

| Fournisseur | Non échu | Échu 1-30 j | Échu 31-60 j | Échu 61-90 j | Échu > 90 j | Total |
|---|---|---|---|---|---|---|
| Hygiène Pro Distribution | 48 200,00 | 6 300,00 | | | − 3 000,00 | 51 500,00 |
| Interim Azur | 31 400,00 | 12 850,00 | 9 640,00 | | | 53 890,00 |
| Clean Sous-Traitance | 8 440,00 | | | | | 8 440,00 |
| Machines Nett' | 3 120,00 | | | | − 1 250,00 | 1 870,00 |
| AutoLease France | | − 2 512,00 | | | | − 2 512,00 |
| CloudLedger Inc. (SaaS, États-Unis) | | | | | 4 860,00 | 4 860,00 |
| SCI Les Oliviers (loyer agence de Cannes, fictive) | | | | 6 600,00 | | 6 600,00 |
| **Total** | **91 160,00** | **16 638,00** | **9 640,00** | **6 600,00** | **610,00** | **124 648,00** |

**Pièce 2 — Commentaires recueillis**
- HPD : les 6 300,00 € échus correspondent à trois factures **en litige documenté** (quantités, prix). Le − 3 000,00 € est un **acompte** versé le 12/05/2026 sur la commande d'un stock d'EPI pour le démarrage d'un marché, livraison prévue en novembre ; il a été saisi au crédit… du 401HPD.
- Interim Azur : les 22 490,00 € échus (12 850,00 + 9 640,00) attendent la **validation des relevés d'heures** par les établissements ; aucune contestation. Les 9 640,00 € concernent 2 factures émises il y a 70 jours en moyenne.
- Machines Nett' : avoir de 1 250,00 € reçu en juin, jamais déduit d'un paiement.
- AutoLease : la facture de loyers d'août (2 512,00 €) a été **prélevée** le 10/09 et **payée aussi par virement** le 08/09 par un collègue qui ne savait pas qu'un mandat SEPA existait.
- CloudLedger : facture de 4 860,00 € de janvier 2026 (abonnement annuel), **payée par carte bancaire** le jour même ; la dépense carte a été comptabilisée en 471 faute de justificatif à l'époque, la facture a été saisie en 401 depuis.
- SCI Les Oliviers : loyer du T3 non payé ; l'établissement de Cannes conteste la régularisation des charges 2025 (facturée séparément, 1 140,00 €, non comprise dans les 6 600,00 €).

## Travail à faire

1. Identifiez et corrigez les soldes anormaux (écritures au 30/09/2026). Recalculez le total des dettes fournisseurs.
2. Analysez l'échu « réel » : montant, causes, caractère justifié ou non du retard.
3. Évaluez le risque au regard des délais de paiement : pénalités et indemnités dues aux fournisseurs (exemple chiffré sur les factures Interim Azur à 31-60 jours), risque d'amende administrative. Faut-il comptabiliser les pénalités ?
4. Calculez le DPO (délai moyen de paiement) après corrections.
5. Rédigez la page de synthèse pour le comité (5 à 7 puces) avec les actions.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-13_corrige.md)
