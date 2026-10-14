# Corrigé E04-01 — La CA3 de septembre d'Asia Trading

<!-- lien-enonce -->
> ↩️ [Revenir à l'énoncé de l'exercice E04-01](../exercices/E04-01_ca3-asia-trading.md)

## 1. Analyse

**a) L'importation.** Depuis le 01/01/2022, la TVA à l'importation est **obligatoirement autoliquidée** sur la CA3 par tout importateur identifié à la TVA en France (art. 1695 II CGI) : elle n'est pas payée en douane, elle est **déclarée** (TVA brute) et **déduite** simultanément sur la même CA3.

Sa **base** n'est pas le prix facturé par le fournisseur (art. 292 CGI) : c'est la **valeur en douane** (CIF : prix FOB + fret + assurance jusqu'à l'entrée dans l'UE) **augmentée des droits de douane** (et des frais accessoires jusqu'au premier lieu de destination s'ils sont inclus). La valeur de référence est celle du **DAU**, avec le taux de change douanier. Kevin a pris la valeur FOB convertie au taux du jour et oublié fret et droits : base sous-évaluée de 7 816,05 €.

**b) La livraison en Belgique** est une **livraison intracommunautaire exonérée** (art. 262 ter I CGI) : client assujetti avec un numéro de TVA valide vérifié sur VIES ✔, transport vers la Belgique prouvé (CMR + facture du transporteur, à compléter par l'accusé de réception du client) ✔. **Anomalie** : la facture indique « TVA 0 % » au lieu de la mention obligatoire **« Exonération de TVA, article 262 ter I du CGI »**. Il faut émettre une facture rectificative (ou un document rectificatif) portant la mention.

**c) TVA déductible : les exclusions.**
- **Essence du véhicule de tourisme** : déductible à **80 %** (40 € sur 50 €).
- **Gazole du fourgon utilitaire** : 100 % déductible.
- **Coffrets cadeaux à 90 € TTC** : au-delà du seuil de **73 € TTC** par bénéficiaire et par an (*valeur à vérifier chaque année*) → **TVA non déductible** (450 €). Ce n'est pas une question de « bon pour le business » : la dépense reste une charge déductible du résultat (si elle est dans l'intérêt de l'entreprise), mais la TVA est exclue.
- **Rayonnages** : immobilisation → ligne 19.
- **Transitaire** : le fret maritime est exonéré (transport international) ; les honoraires de dédouanement ouvrent droit à déduction (76 €) ; les droits de douane refacturés en **débours** ne portent pas de TVA (et sont inclus dans la base de la TVA à l'importation).

## 2. Calculs

**TVA à l'importation**

| Élément | Montant |
|---|---|
| Valeur en douane CIF (DAU) | 62 000,00 |
| + Droits de douane 4,7 % | 2 914,00 |
| **= Base TVA importation** | **64 914,00** |
| **TVA 20 %** | **12 982,80** |
| *Calcul de Kevin* | *57 097,95 × 20 % = 11 419,59 (erroné)* |

**TVA collectée**

| Opération | Base | TVA |
|---|---|---|
| Ventes France (A1) | 186 400,00 | 37 280,00 |
| Importation (A4) | 64 914,00 | 12 982,80 |
| **Ligne 08 (20 %)** | **251 314,00** | **50 262,80** |
| LIC Belgique (F2) | 42 600,00 | exonérée |

**TVA déductible**

| Nature | TVA facturée | Taux de déduction | TVA déductible | Ligne |
|---|---|---|---|---|
| Rayonnages (immobilisation) | 1 900,00 | 100 % | 1 900,00 | 19 |
| Emballages | 640,00 | 100 % | 640,00 | 20 |
| Loyer entrepôt | 1 200,00 | 100 % | 1 200,00 | 20 |
| Énergie, télécom | 280,00 | 100 % | 280,00 | 20 |
| Honoraires | 520,00 | 100 % | 520,00 | 20 |
| Marketing | 320,00 | 100 % | 320,00 | 20 |
| Honoraires de dédouanement | 76,00 | 100 % | 76,00 | 20 |
| Gazole utilitaire | 120,00 | 100 % | 120,00 | 20 |
| Essence VP | 50,00 | 80 % | 40,00 | 20 |
| Coffrets cadeaux (> 73 € TTC) | 450,00 | 0 % | 0,00 | — |
| TVA à l'importation autoliquidée | 12 982,80 | 100 % | 12 982,80 | 20 (et 24) |
| **Total** | | | **18 078,80** | |

Ligne 20 = 640 + 1 200 + 280 + 520 + 320 + 76 + 120 + 40 + 12 982,80 = **16 178,80 €**.

**CA3 de septembre 2026**

| Ligne | Libellé | Montant |
|---|---|---|
| A1 | Ventes, prestations de services | 186 400 |
| A4 | Importations (autres que produits pétroliers) | 64 914 |
| F2 | Livraisons intracommunautaires à destination d'un assujetti | 42 600 |
| 08 | Taux normal 20 % — base / taxe due | 251 314 / 50 262,80 |
| 16 | Total de la TVA brute due | 50 262,80 |
| 19 | Biens constituant des immobilisations | 1 900,00 |
| 20 | Autres biens et services | 16 178,80 |
| 22 | Report du crédit de la déclaration précédente | 0 |
| 23 | Total TVA déductible | 18 078,80 |
| 24 | dont TVA déductible sur importations | 12 982,80 |
| **28** | **TVA nette due (16 – 23)** | **32 184,00** |
| **32** | **Total à payer** | **32 184,00** |

*(Les bases sont déclarées en euros arrondis ; la CA3 se télédéclare au plus tard à la date limite propre à l'entreprise — ici le 19/10/2026 selon Kevin, à confirmer dans l'espace professionnel. Numérotation à contrôler sur le formulaire millésimé.)*

Contrôle : 50 262,80 – 18 078,80 = 32 184,00 ✔.

## 3. Écritures comptables

| Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
|---|---|---|---|---|---|---|
| 08/09/2026 | OD | 445663 | TVA déductible sur importations | DAU 26FR6900IM0447213 – autoliquidation | 12 982,80 | |
| 08/09/2026 | OD | 4452 | TVA due autoliquidée (importations) | DAU 26FR6900IM0447213 – autoliquidation | | 12 982,80 |
| 30/09/2026 | OD | 44571 | TVA collectée | Liquidation TVA 09/2026 | 37 280,00 | |
| 30/09/2026 | OD | 4452 | TVA due autoliquidée (importations) | Liquidation TVA 09/2026 | 12 982,80 | |
| 30/09/2026 | OD | 44562 | TVA déductible sur immobilisations | Liquidation TVA 09/2026 | | 1 900,00 |
| 30/09/2026 | OD | 44566 | TVA déductible sur ABS | Liquidation TVA 09/2026 | | 3 196,00 |
| 30/09/2026 | OD | 445663 | TVA déductible sur importations | Liquidation TVA 09/2026 | | 12 982,80 |
| 30/09/2026 | OD | 44551 | TVA à décaisser | CA3 09/2026 | | 32 184,00 |
| | | | | **Totaux** | **63 245,60** | **63 245,60** |

Remarques :
- 44566 = 640 + 1 200 + 280 + 520 + 320 + 76 + 120 + 40 = **3 196,00 €**. Les 10 € de TVA non déductible sur l'essence et les 450 € sur les cadeaux sont comptabilisés **en charge** (TTC) avec la dépense (6061 carburants ; 6234 cadeaux), jamais en 44566.
- Les droits de douane (2 914 €) sont un élément du coût d'achat des marchandises (607 ou 6087 « frais accessoires d'achat »), comme le fret maritime (4 900 €) et les honoraires de dédouanement (380 €).

## 4. Points d'attention / pièges

- **Rapprocher la ligne A4 des données douanières** mises à disposition dans l'espace professionnel (montants d'importation de la période) : un écart sera relevé par l'administration.
- **Taux de change** : celui du DAU (taux douanier) pour la base de TVA ; le taux du jour (ou un taux moyen) pour la comptabilisation de l'achat en devises ; l'écart de règlement va en 666 / 766 et, à la clôture, la dette fournisseur en USD est réévaluée (476 / 477).
- **Cadeaux** : vérifier la valeur **unitaire TTC** par bénéficiaire et le cumul annuel ; un cadeau à 70 € suivi d'un second à 30 € au même client dépasse 73 € dans l'année.
- **Facture de LIC** : la mention d'exonération et le numéro de TVA du client sont des conditions de forme ; sans numéro valide, l'exonération tombe (voir E04-11).
- **Liquidation** : l'autoliquidation est neutre (12 982,80 en brute et en déductible) ; son oubli fausse la CA3 et peut être sanctionné même sans perte de recettes.

## 5. Ce qu'un senior ferait en plus

**Autres obligations liées à la vente en Belgique** :
- déposer l'**état récapitulatif des clients** (livraisons intracommunautaires) de septembre, au plus tard le 10e jour ouvrable d'octobre (*délai à vérifier*) : client BE 0712.554.390, 42 600 € ;
- répondre, si Asia Trading y est soumise, à l'**enquête statistique EMEBI** ;
- conserver le **dossier de preuve du transport** (CMR signé à la livraison, facture de Transports Leroy, attestation de réception du client).

**Mail à Kevin :**
> Bonjour Kevin, merci pour le pré-remplissage ! Trois corrections : (1) la TVA à l'importation se calcule sur la valeur du DAU (CIF) plus les droits de douane, soit 64 914 € de base et 12 982,80 € de TVA, autoliquidée (déclarée et déduite sur la même déclaration, donc sans coût) ; (2) la TVA des coffrets à 90 € n'est pas récupérable (seuil de 73 € TTC par bénéficiaire) ; (3) l'essence de votre véhicule n'est récupérable qu'à 80 %. TVA à payer : 32 184 €. Pour la facture belge, je vous envoie le modèle avec la mention d'exonération obligatoire.

**Dossier** : archiver la CA3, le DAU, la consultation VIES, le tableau de calcul de la TVA déductible et le rapprochement 44571 / journal des ventes.

## 6. Références

- CGI : art. 262 ter I (LIC), art. 292 (base de la TVA à l'importation), art. 1695 II (autoliquidation à l'importation), art. 298-4-1° (carburants : 80 % pour les VP), art. 242 nonies A ann. II (mentions), art. 206 IV-2-3° ann. II (cadeaux de faible valeur — seuil à vérifier), art. 262 II-14° (transports internationaux exonérés).
- Règlement d'exécution (UE) n° 282/2011, art. 45 bis (présomption de transport intracommunautaire).
- BOFiP : TVA-DECLA (autoliquidation de la TVA à l'importation), TVA-CHAMP (échanges intracommunautaires), TVA-DED (exclusions).
- Notice de la déclaration 3310-CA3 (millésime de l'année).
