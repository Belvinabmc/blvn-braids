from django.db import models
from django.contrib.auth.models import AbstractUser


# ============================================================
# UTILISATEUR
# ============================================================

class Utilisateur(AbstractUser):

    class Role(models.TextChoices):
        CLIENT = "client", "Client"
        ADMIN = "admin", "Administrateur"

    email = models.EmailField(
        unique=True
    )

    telephone = models.CharField(
        max_length=20,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT
    )

    def __str__(self):
        return self.email


# ============================================================
# UNIVERS
# ============================================================

class Univers(models.Model):

    nom = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=120,
        unique=True
    )

    description = models.TextField(
        max_length=500,
        blank=True
    )

    image = models.ImageField(
        upload_to="univers/",
        blank=True,
        null=True
    )

    ordre_affichage = models.PositiveIntegerField(
        default=0
    )

    actif = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nom


# ============================================================
# CATEGORIE
# ============================================================

class Categorie(models.Model):

    univers = models.ForeignKey(
        Univers,
        on_delete=models.PROTECT,
        related_name="categories"
    )

    nom = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        max_length=120
    )

    description = models.TextField(
        max_length=500,
        blank=True
    )

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    ordre_affichage = models.PositiveIntegerField(
        default=0
    )

    actif = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nom


# ============================================================
# PRESTATION
# ============================================================

class Prestation(models.Model):

    class PublicCible(models.TextChoices):
        FEMME = "femme", "Femme"
        HOMME = "homme", "Homme"
        UNISEXE = "unisexe", "Unisexe"

    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.PROTECT,
        related_name="prestations"
    )

    nom = models.CharField(
        max_length=150
    )

    description = models.TextField(
        max_length=500,
        blank=True
    )

    prix = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    duree = models.PositiveIntegerField(
        help_text="Durée en minutes"
    )

    image = models.ImageField(
        upload_to="prestations/",
        blank=True,
        null=True
    )

    public_cible = models.CharField(
        max_length=20,
        choices=PublicCible.choices,
        default=PublicCible.UNISEXE
    )

    ordre_affichage = models.PositiveIntegerField(
        default=0
    )

    actif = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nom


# ============================================================
# RESERVATION
# ============================================================

class Reservation(models.Model):

    class Statut(models.TextChoices):
        EN_ATTENTE = "en_attente", "En attente"
        CONFIRMEE = "confirmee", "Confirmée"
        ANNULEE = "annulee", "Annulée"
        TERMINEE = "terminee", "Terminée"

    utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.PROTECT,
        related_name="reservations"
    )

    prestation = models.ForeignKey(
        Prestation,
        on_delete=models.PROTECT,
        related_name="reservations"
    )

    creneau = models.OneToOneField(
        "Creneau",
        on_delete=models.PROTECT,
        related_name="reservation"
    )

    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    reservation_pour_soi = models.BooleanField(
        default=True
    )

    nom_beneficiaire = models.CharField(
        max_length=100,
        blank=True
    )

    prenom_beneficiaire = models.CharField(
        max_length=100,
        blank=True
    )

    telephone_beneficiaire = models.CharField(
        max_length=20,
        blank=True
    )

    commentaire_client = models.TextField(
        max_length=500,
        blank=True
    )

    def __str__(self):
        return f"Réservation #{self.id} - {self.prestation.nom}"


# ============================================================
# CRENEAU
# ============================================================

class Creneau(models.Model):

    date = models.DateField()

    heure_debut = models.TimeField()

    heure_fin = models.TimeField()

    disponible = models.BooleanField(
        default=True
    )

    horaire_ouverture = models.ForeignKey(
        "HoraireOuverture",
        on_delete=models.PROTECT,
        related_name="creneaux"
    )

    fermeture = models.ForeignKey(
        "Fermeture",
        on_delete=models.SET_NULL,
        related_name="creneaux_bloques",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.date} - {self.heure_debut} à {self.heure_fin}"


# ============================================================
# HORAIRE D'OUVERTURE
# ============================================================

class HoraireOuverture(models.Model):

    class JourSemaine(models.TextChoices):
        LUNDI = "lundi", "Lundi"
        MARDI = "mardi", "Mardi"
        MERCREDI = "mercredi", "Mercredi"
        JEUDI = "jeudi", "Jeudi"
        VENDREDI = "vendredi", "Vendredi"
        SAMEDI = "samedi", "Samedi"
        DIMANCHE = "dimanche", "Dimanche"

    jour_semaine = models.CharField(
        max_length=10,
        choices=JourSemaine.choices
    )

    heure_ouverture = models.TimeField()

    heure_fermeture = models.TimeField()

    actif = models.BooleanField(
        default=True
    )

    def __str__(self):
        return (
            f"{self.get_jour_semaine_display()} : "
            f"{self.heure_ouverture} - {self.heure_fermeture}"
        )


# ============================================================
# FERMETURE
# ============================================================

class Fermeture(models.Model):

    date_debut = models.DateField()

    date_fin = models.DateField()

    motif = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f"Fermeture du {self.date_debut} au {self.date_fin}"

    
# ============================================================
# PAIEMENT
# ============================================================

class Paiement(models.Model):

    class StatutPaiement(models.TextChoices):
        EN_ATTENTE = "en_attente", "En attente"
        REUSSI = "reussi", "Réussi"
        ECHOUE = "echoue", "Échoué"
        REMBOURSE = "rembourse", "Remboursé"

    reservation = models.OneToOneField(
        Reservation,
        on_delete=models.PROTECT,
        related_name="paiement"
    )

    montant = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    date_paiement = models.DateTimeField(
        blank=True,
        null=True
    )

    statut_paiement = models.CharField(
        max_length=20,
        choices=StatutPaiement.choices,
        default=StatutPaiement.EN_ATTENTE
    )

    reference_stripe = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        unique=True
    )

    def __str__(self):
        return f"Paiement #{self.id} - {self.statut_paiement}"



    # ============================================================
# IMAGE GALERIE
# ============================================================

class ImageGalerie(models.Model):

    prestation = models.ForeignKey(
        Prestation,
        on_delete=models.SET_NULL,
        related_name="images_galerie",
        blank=True,
        null=True
    )

    url_image = models.ImageField(
        upload_to="galerie/"
    )

    titre = models.CharField(
        max_length=150,
        blank=True
    )

    description = models.TextField(
        max_length=500,
        blank=True
    )

    date_ajout = models.DateTimeField(
        auto_now_add=True
    )

    ordre_affichage = models.PositiveIntegerField(
        default=0
    )

    actif = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.titre or f"Image #{self.id}"