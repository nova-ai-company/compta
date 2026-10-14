# E14-11 — Fraude au changement de RIB : détecter, réagir, comptabiliser quand le virement est déjà parti
**Client :** GSF Riviera SAS (filiale régionale **fictive**, dossier tenu au siège) | **Difficulté :** ★★★ | **Durée estimée :** 50 min | **Thèmes :** fraude au faux fournisseur, contrôle des modifications du fichier tiers, procédure d'urgence (banque, plainte, assurance), maintien de la dette fournisseur, créance sur fonds détournés, dépréciation, PCG 2025 (pas d'exceptionnel par défaut)

**Corner case :** oui — payer « le fournisseur » sur un IBAN frauduleux n'éteint pas la dette envers le vrai fournisseur

> *Cadre de formation : sociétés, adresses électroniques, IBAN et personnes fictifs. Les IBAN sont volontairement incomplets.*

## La mise en situation

Lundi 05/10/2026, 9 h 10. Le service relation fournisseurs d'Hygiène Pro Distribution appelle sur le numéro du standard : trois factures échues fin septembre ne sont pas payées. Or le run de paiement du 01/10 les a réglées : 18 642,30 €. En remontant l'historique, vous retrouvez un e-mail du 28/09, traité le 29/09 par un collègue intérimaire au service fournisseurs, qui a modifié l'IBAN dans la fiche tiers.

Sophie Garnier (personnage fictif) : « On déclenche la procédure tout de suite. Dites-moi dans l'ordre ce qu'on fait dans l'heure, puis ce qu'on passe en compta. Et en entretien, c'est une question qu'on vous posera : "que faites-vous si vous recevez un changement de RIB ?" »

Comptes : 401HPD ; 512 ; 467FR Débiteurs divers – fonds détournés ; 4967 Dépréciation des comptes de débiteurs divers ; 6817 Dotations aux dépréciations des actifs circulants ; 658 Charges diverses de gestion courante (*subdivision selon la nomenclature 2025 du PCG*) ; 758 Produits divers de gestion courante.

## Les pièces

**Pièce 1 — E-mail reçu le 28/09/2026 à 18 h 52**
```
De : Service Comptabilité <comptabilite@hygienepro-distributlon.fr>
À : fournisseurs@gsf-riviera.example
Objet : URGENT – Changement de coordonnées bancaires

Bonjour,
Suite à un audit interne, nos comptes ont été transférés vers notre nouvel
établissement bancaire. Merci de mettre à jour nos coordonnées AVANT votre
prochain règlement et de ne plus utiliser l'ancien RIB, qui sera clôturé le 30/09.
Pour toute question, merci de me contacter uniquement par e-mail ou au
+44 7xxx xxx xxx (je suis en déplacement).
Cordialement,
Mme Claire Martin – Responsable comptable (nouvelle dans le service)
PJ : RIB_HPD_2026.pdf
```

**Pièce 2 — RIB joint**
```
Titulaire : HPD DISTRIBUTION LTD
IBAN : LT12 3250 0xxx xxxx xxxx – BIC : RVUALT2V (fictif)
```

**Pièce 3 — Fiche tiers 401HPD (historique des modifications)**

| Date | Utilisateur | Champ | Ancienne valeur | Nouvelle valeur | Validation 2e personne |
|---|---|---|---|---|---|
| 29/09/2026 09:14 | interim.fournisseurs | IBAN | FR76 1xxx … (Banque fictive, Nice) | LT12 3250 0xxx … | **aucune** |
| 29/09/2026 09:15 | interim.fournisseurs | E-mail de contact | compta@hygienepro-distribution.fr | comptabilite@hygienepro-distributlon.fr | aucune |

Contact habituel dans la fiche : M. Lucas Ferrand, comptable fournisseurs HPD, 04 93 xx xx xx.

**Pièce 4 — Run de paiement du 01/10/2026 (extrait)**

| Facture | Échéance | Montant |
|---|---|---|
| F26-7650 | 30/09/2026 | 9 870,00 |
| F26-7688 | 30/09/2026 | 5 412,30 |
| F26-7702 | 30/09/2026 | 3 360,00 |
| **Total viré vers LT12 3250 …** | | **18 642,30** |

**Pièce 5 — Suites**
- 05/10 : demande de rappel des fonds transmise à la banque à 9 h 40 ; dépôt de plainte le 05/10 après-midi ; déclaration de sinistre à l'assureur (contrat fraude fictif, franchise 5 000 €).
- 07/10 : après contre-appel au numéro connu de M. Ferrand et validation par deux personnes, GSF Riviera paie HPD sur son IBAN historique (18 642,30 €).
- 14/10 : la banque obtient le retour partiel de **6 210,00 €**.
- 31/10 : clôture d'octobre ; la banque indique que le reste des fonds a été retiré du compte bénéficiaire. L'assureur n'a pas encore pris position.

## Travail à faire

1. Relevez tous les indices de fraude dans les pièces 1 à 3.
2. Décrivez, dans l'ordre, les actions à mener dans l'heure qui suit la découverte (05/10), et qui prévenir.
3. Expliquez pourquoi la dette envers HPD subsiste et passez les écritures du 01/10 (déjà passée), du 05/10, du 07/10, du 14/10 et du 31/10.
4. Quel traitement si, en décembre, l'assureur notifie une indemnisation de 7 432,30 € ? Pourquoi ne pas la constater au 31/10 ?
5. Rédigez la procédure de changement de coordonnées bancaires que vous proposeriez (5 règles), et votre réponse en entretien.

---

<!-- lien-corrige -->
> ✅ **Exercice terminé ?** [Voir le corrigé →](../corriges/E14-11_corrige.md)
