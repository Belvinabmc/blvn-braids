# DATA-03 — Modèles Django BLVN Braids

## Objectif

Transformer le MCD BLVN Braids en modèles Django et créer les tables correspondantes dans MySQL.

---

## Modèles créés

### 1. Utilisateur

Représente les utilisateurs de la plateforme.

Principaux champs :

- username
- first_name
- last_name
- email
- telephone
- role
- password

Le modèle hérite de `AbstractUser`.

Rôles disponibles :

- Client
- Administrateur

---

### 2. Univers

Représente les grands domaines de services.

Exemples :

- Coiffure
- Onglerie
- Regard
- Maquillage
- Soins

Principaux champs :

- nom
- slug
- description
- image
- ordre_affichage
- actif

---

### 3. Categorie

Représente une catégorie appartenant à un univers.

Exemples :

- Tresses
- Locks
- Perruques
- Barber

Relation :

Univers → Categorie

Une catégorie appartient à un seul univers.

---

### 4. Prestation

Représente un service réservable.

Exemples :

- Knotless Braids
- Box Braids
- Pose de perruque
- Retwist

Principaux champs :

- nom
- description
- prix
- duree
- image
- public_cible
- ordre_affichage
- actif

Public cible :

- Femme
- Homme
- Unisexe

Relation :

Categorie → Prestation

---

### 5. Reservation

Représente une réservation effectuée par un utilisateur.

Principaux champs :

- utilisateur
- prestation
- creneau
- statut
- date_creation
- reservation_pour_soi
- nom_beneficiaire
- prenom_beneficiaire
- telephone_beneficiaire
- commentaire_client

Statuts disponibles :

- En attente
- Confirmée
- Annulée
- Terminée

Règle métier :

Une réservation correspond à une personne coiffée, une prestation et un créneau.

---

### 6. Creneau

Représente un créneau disponible pour une réservation.

Principaux champs :

- date
- heure_debut
- heure_fin
- disponible
- horaire_ouverture
- fermeture

Un créneau ne peut être utilisé que par une seule réservation.

---

### 7. HoraireOuverture

Représente les horaires habituels d'ouverture.

Principaux champs :

- jour_semaine
- heure_ouverture
- heure_fermeture
- actif

Jours disponibles :

- Lundi
- Mardi
- Mercredi
- Jeudi
- Vendredi
- Samedi
- Dimanche

---

### 8. Fermeture

Représente les périodes d'indisponibilité.

Principaux champs :

- date_debut
- date_fin
- motif

Exemples :

- congés
- jour férié
- absence
- formation

---

### 9. Paiement

Représente le paiement associé à une réservation.

Principaux champs :

- reservation
- montant
- date_paiement
- statut_paiement
- reference_stripe

Statuts disponibles :

- En attente
- Réussi
- Échoué
- Remboursé

---

### 10. ImageGalerie

Représente les images affichées dans la galerie.

Principaux champs :

- prestation
- url_image
- titre
- description
- date_ajout
- ordre_affichage
- actif

Une image peut être liée à une prestation ou être utilisée comme image générale de galerie.

---

## Relations principales

- Univers → Categorie
- Categorie → Prestation
- Utilisateur → Reservation
- Prestation → Reservation
- Reservation → Creneau
- Reservation → Paiement
- HoraireOuverture → Creneau
- Fermeture → Creneau
- Prestation → ImageGalerie

---

## Base de données

SGBD :

MySQL

Moteur utilisé :

InnoDB

Base :

blvn_braids

---

## Migrations Django

Première migration :

`core/migrations/0001_initial.py`

Modèles concernés :

- Utilisateur
- Univers
- Categorie
- Prestation

Deuxième migration :

`core/migrations/0002_fermeture_horaireouverture_creneau_imagegalerie_and_more.py`

Modèles concernés :

- Fermeture
- HoraireOuverture
- Creneau
- ImageGalerie
- Reservation
- Paiement

---

## Vérification

Commande :

```bash
python manage.py check