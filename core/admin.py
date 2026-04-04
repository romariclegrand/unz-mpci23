from django.contrib import admin
from .models import Actualite, Document, Image, Video, MembrePromotion

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date')
    list_filter = ('categorie', 'date')
    search_fields = ('titre', 'contenu')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('titre', 'matiere', 'ajoute_par', 'date_ajout')
    list_filter = ('matiere',)
    search_fields = ('titre',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'ajoute_par', 'date_ajout')
    list_filter = ('categorie',)
    search_fields = ('titre',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'ajoute_par', 'date_ajout')
    search_fields = ('titre',)

@admin.register(MembrePromotion)
class MembrePromotionAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'role', 'whatsapp')
    list_filter = ('role',)
    search_fields = ('nom', 'prenom')
