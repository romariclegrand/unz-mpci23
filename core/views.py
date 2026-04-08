from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Actualite, Document, Image, Video, MembrePromotion
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(request, 'Identifiant ou mot de passe incorrect.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def accueil(request):
    actualites = Actualite.objects.order_by('-date')[:5]
    return render(request, 'fichier.html', {'actualites': actualites})

@login_required
def actualites(request):
    actu = Actualite.objects.order_by('-date')
    return render(request, 'actualite.html', {'actualites': actu})

@login_required
def bibliotheque(request):
    docs = Document.objects.order_by('-date_ajout')
    return render(request, 'document.html', {'documents': docs})

@login_required
def images(request):
    imgs = Image.objects.order_by('-date_ajout')
    return render(request, 'images.html', {'images': imgs})

@login_required
def videos(request):
    vids = Video.objects.order_by('-date_ajout')
    return render(request, 'video.html', {'videos': vids})

@login_required
def apropos(request):
    membres = MembrePromotion.objects.all()
    return render(request, 'apropos.html', {'membres': membres})


def reset_admin(request):
    from django.contrib.auth.models import User
    from django.http import HttpResponse
    user, created = User.objects.get_or_create(username='romaric')
    user.set_password('unzmpci2025')
    user.is_superuser = True
    user.is_staff = True
    user.email = 'romaricyelkouni1@gmail.com'
    user.save()
    if created:
        return HttpResponse('Superutilisateur créé !')
    return HttpResponse('Mot de passe réinitialisé !')



def register(request):
    if request.user.is_authenticated:
        return redirect('accueil')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})