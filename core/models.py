from django.db import models
from django.contrib.auth.models import User

class Actualite(models.Model):
    CATEGORIES = [
        ('General', 'Général'),
        ('Evenement', 'Événement'),
        ('Assemblee', 'Assemblée'),
        ('Universite', 'Université'),
        ('Organisation', 'Organisation'),
        ('Cours', 'Cours'),
    ]
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='General')

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Actualité'
        verbose_name_plural = 'Actualités'
        ordering = ['-date']


class Document(models.Model):
    MATIERES = [
        ('Informatique', 'Informatique'),
        ('Physique', 'Physique'),
        ('Mathematiques', 'Mathématiques'),
        ('Droit', 'Droit'),
        ('Autre', 'Autre'),
    ]
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='documents/')
    matiere = models.CharField(max_length=100, choices=MATIERES, default='Autre')
    description = models.TextField(blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    ajoute_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['-date_ajout']


class Image(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    categorie = models.CharField(max_length=100, default='Général')
    date_ajout = models.DateTimeField(auto_now_add=True)
    ajoute_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['-date_ajout']


class Video(models.Model):
    titre = models.CharField(max_length=200)
    url_youtube = models.URLField(blank=True, null=True)
    fichier = models.FileField(upload_to='videos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    ajoute_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Vidéo'
        verbose_name_plural = 'Vidéos'
        ordering = ['-date_ajout']


class MembrePromotion(models.Model):
    ROLES = [
        ('Delegue', 'Délégué'),
        ('Delegue_adjoint', 'Délégué adjoint'),
        ('Etudiant', 'Étudiant'),
    ]
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLES, default='Etudiant')
    photo = models.ImageField(upload_to='membres/', blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = 'Membre'
        verbose_name_plural = 'Membres'