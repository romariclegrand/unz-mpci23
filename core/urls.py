from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('actualites/', views.actualites, name='actualites'),
    path('bibliotheque/', views.bibliotheque, name='bibliotheque'),
    path('images/', views.images, name='images'),
    path('apropos/', views.apropos, name='apropos'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reset-admin/', views.reset_admin, name='reset_admin'),
]