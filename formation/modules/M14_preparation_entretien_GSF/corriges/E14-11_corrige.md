# Corrigé E14-11 — Fraude au changement de RIB : détecter, réagir, comptabiliser quand le virement est déjà parti

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E14-11](../exercices/E14-11_fraude-changement-rib.md)

## 1. Analyse (raisonnement pas à pas, comme un senior l'expliquerait)

### Question 1 — Les indices
- **Nom de domaine** : « hygienepro-distribut**l**on.fr » (un « l » à la place du « i ») ≠ « hygienepro-distribution.fr » du fichier tiers.
- **Urgence et pression** (« URGENT », « AVANT votre prochain règlement », ancien RIB « clôturé le 30/09 ») ; envoi un **vendredi/soir de fin de mois**, juste avant le run de paiement.
- **Contact exclusif par e-mail ou par un mobile étranger**, interlocutrice « nouvelle dans le service », inconnue du fichier.
- **Banque étrangère** (IBAN lituanien) pour un fournisseur français de produits d'entretien, sans raison commerciale.
- **Titulaire du compte différent** de la raison sociale (« HPD DISTRIBUTION LTD » ≠ « Hygiène Pro Distribution SAS »).
- **Contrôle interne défaillant** : modification de l'IBAN **et** de l'adresse e-mail de contact (ce qui aurait détourné les futures confirmations) par une seule personne, **sans validation par une deuxième personne ni contre-appel**.

### Question 2 — Dans l'heure
1. **Banque** (immédiatement, par téléphone puis écrit) : demande de **rappel des fonds** / blocage chez la banque bénéficiaire. Chaque heure compte : les fonds sont généralement retirés en quelques jours.
2. **Bloquer le tiers** 401HPD (paiements suspendus), **remettre l'IBAN historique** seulement après contre-appel du contact connu, au numéro du fichier (pas celui de l'e-mail).
3. **Alerter** : responsable comptable, DAF / trésorerie groupe, **sécurité informatique** (la messagerie a peut-être été ciblée, d'autres filiales aussi), direction juridique.
4. **Conserver les preuves** : e-mail original avec en-têtes, PJ, logs de modification, ordre de virement.
5. **Plainte** (police / gendarmerie) — pièce exigée par la banque et l'assureur — et **déclaration à l'assureur** dans les délais du contrat.
6. **Revue des autres modifications** de fichiers tiers des 30 derniers jours (toutes filiales gérées par le service).
7. Informer HPD (son domaine est usurpé) et lui confirmer un paiement rapide.

### Question 3 — La dette subsiste
Un paiement libère le débiteur s'il est fait **au créancier** (ou à une personne habilitée par lui). Un virement sur le compte d'un fraudeur n'est pas un paiement à HPD : **la dette envers HPD reste entière**. Comptablement, on « rouvre » le 401HPD et on constate à la place une **créance sur les fonds détournés** (467), qui sera recouvrée en tout ou partie (rappel bancaire, assurance) ou dépréciée.

Sous le PCG modifié par le règlement ANC n° 2022-06, une perte de fraude de ce montant, dans un groupe de cette taille, n'est pas un événement « majeur et inhabituel » : la **charge** est d'exploitation (dépréciation en 6817, perte définitive en 658), pas en résultat exceptionnel.

## 2. Calculs (détaillés, chaque montant justifié)

| Élément | Calcul | Montant |
|---|---|---|
| Fonds détournés | 9 870,00 + 5 412,30 + 3 360,00 | 18 642,30 € |
| Retour bancaire du 14/10 | | 6 210,00 € |
| Créance résiduelle au 31/10 | 18 642,30 − 6 210,00 | **12 432,30 €** |
| Dépréciation au 31/10 | 100 % (fonds retirés, assurance non acquise) | **12 432,30 €** |
| Indemnisation assureur (décembre) | 12 432,30 − franchise 5 000,00 | 7 432,30 € |
| Perte nette finale | 12 432,30 − 7 432,30 | **5 000,00 €** (= franchise) |

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 01/10/2026 | BQ | 401HPD | Fournisseur Hygiène Pro Distribution | Run 01/10 F26-7650/7688/7702 (IBAN frauduleux) | 18 642,30 | |
| 01/10/2026 | BQ | 512 | Banque | Run 01/10 HPD | | 18 642,30 |
| 05/10/2026 | OD | 467FR | Débiteurs divers – fonds détournés | Fraude RIB HPD – vir. 01/10 vers LT12… | 18 642,30 | |
| 05/10/2026 | OD | 401HPD | Fournisseur Hygiène Pro Distribution | Réouverture dette HPD – paiement non libératoire | | 18 642,30 |
| 07/10/2026 | BQ | 401HPD | Fournisseur Hygiène Pro Distribution | Vir. HPD IBAN historique F26-7650/7688/7702 | 18 642,30 | |
| 07/10/2026 | BQ | 512 | Banque | Vir. HPD IBAN historique | | 18 642,30 |
| 14/10/2026 | BQ | 512 | Banque | Retour partiel fonds (rappel bancaire) | 6 210,00 | |
| 14/10/2026 | BQ | 467FR | Débiteurs divers – fonds détournés | Retour partiel fonds (rappel bancaire) | | 6 210,00 |
| 31/10/2026 | OD | 6817 | Dotations aux dépréciations des actifs circulants | Dépréciation créance fraude RIB HPD | 12 432,30 | |
| 31/10/2026 | OD | 4967 | Dépréciation des comptes de débiteurs divers | Dépréciation créance fraude RIB HPD | | 12 432,30 |
| | | | | **Totaux** | **74 569,20** | **74 569,20** |

**Question 4 — Indemnisation notifiée en décembre** (accord écrit de l'assureur) puis constat de la perte définitive :

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 15/12/2026 | OD | 4687 | Divers – produits à recevoir | Indemnité assurance fraude RIB HPD (accord du 15/12) | 7 432,30 | |
| 15/12/2026 | OD | 758 | Produits divers de gestion courante | Indemnité assurance fraude RIB HPD | | 7 432,30 |
| 15/12/2026 | OD | 658 | Charges diverses de gestion courante – pertes sur fraudes | Perte définitive fonds détournés HPD | 12 432,30 | |
| 15/12/2026 | OD | 467FR | Débiteurs divers – fonds détournés | Perte définitive fonds détournés HPD | | 12 432,30 |
| 15/12/2026 | OD | 4967 | Dépréciation des comptes de débiteurs divers | Reprise dépréciation fraude RIB HPD | 12 432,30 | |
| 15/12/2026 | OD | 7817 | Reprises sur dépréciations des actifs circulants | Reprise dépréciation fraude RIB HPD | | 12 432,30 |
| | | | | **Totaux** | **32 296,90** | **32 296,90** |

Effet net sur le résultat de l'exercice : − 12 432,30 (dotation) + 12 432,30 (reprise) − 12 432,30 (perte) + 7 432,30 (indemnité) = **− 5 000,00 €**, la franchise.
Pourquoi pas au 31/10 ? Au 31/10, l'assureur n'a pas pris position : l'indemnité est un **produit éventuel**, non acquis ; le principe de prudence interdit de la constater (on peut la mentionner dans le reporting comme « recouvrement potentiel »).

## 4. Points d'attention / pièges

- **Ne pas laisser 401HPD soldé** : la balance fournisseurs serait fausse, HPD relancerait, et la perte serait cachée.
- **Ne pas passer la perte directement en charge le 05/10** : à cette date, la récupération est possible (rappel bancaire) ; on constate une créance, puis on la déprécie à la clôture selon les informations disponibles.
- **Ne pas compenser** avec l'indemnité d'assurance avant son acquisition.
- **Ne pas re-payer HPD sur un simple appel entrant** : l'appel du 05/10 pourrait lui aussi être une manœuvre ; on rappelle soi-même le numéro **du fichier** et on vérifie les factures.
- **TVA** : aucune incidence (les factures HPD restent dues et leur TVA déduite ; la fraude n'est pas une opération imposable).
- **Responsabilité** : l'intérimaire a appliqué une procédure absente ou mal connue ; la correction porte sur le contrôle interne, pas sur une sanction individuelle à décider par la comptabilité.

## 5. Ce qu'un senior ferait en plus (conseil client, mail type, contrôle, documentation du dossier)

**Procédure de changement de coordonnées bancaires (question 5)** :
1. **Aucune modification sur la base d'un e-mail** : la demande doit être confirmée par **contre-appel** au numéro **déjà connu** du fichier (jamais celui fourni dans la demande).
2. **RIB à l'en-tête et au nom exact** du fournisseur (titulaire = raison sociale), **cohérence pays** (banque étrangère = alerte), et si possible service de vérification de bénéficiaire de la banque.
3. **Séparation des tâches** : saisie par une personne, **validation par une seconde** (workflow ERP), tracée.
4. **Gel** : un IBAN modifié n'est pas utilisable pendant X jours, et le premier paiement est contrôlé spécifiquement (« premier paiement sur nouvel IBAN »).
5. **Revue mensuelle** du journal des modifications de fichiers tiers par le responsable, et sensibilisation régulière (intérimaires compris).

**Réponse d'entretien** : « Je ne modifie jamais un RIB sur la foi d'un e-mail, même s'il paraît venir d'un fournisseur connu. Je rappelle le fournisseur au numéro que nous avons déjà dans notre fichier, je vérifie que le titulaire du compte correspond à la société, et la modification est validée par une deuxième personne. Si quelque chose me paraît bizarre — urgence, banque à l'étranger, nouvel interlocuteur —, j'alerte mon responsable. Et si un virement est déjà parti, j'appelle la banque immédiatement pour tenter un rappel des fonds : chaque heure compte. »

**Documentation** : dossier « incident » (chronologie, preuves, plainte, déclaration de sinistre, échanges bancaires), suivi du compte 467FR jusqu'à son solde.

## 6. Références (PCG, CGI, Code de commerce, BOFiP…)

- Code civil art. 1342-2 : le paiement doit être fait au créancier ou à la personne qu'il a désignée pour le recevoir.
- PCG : comptes 467, 4967, 6817, 7817, 658, 758, 4687 ; principe de prudence ; règlement ANC n° 2022-06 (résultat exceptionnel restreint).
- Code monétaire et financier : règles relatives aux opérations de paiement (rappel de fonds, responsabilités) (*articles à vérifier*).
