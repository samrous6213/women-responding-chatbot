# Importation de la fonction path depuis le module django.urls et des vues de l'application chatbot
from django.urls import path
from . import views

# Définition des URLs de l'application Django "chatbot"
urlpatterns = [
    # URL pour afficher la page du chatbot et gérer les interactions
    path('', views.chatbot, name='chatbot'),
    # URL pour afficher la page de connexion
    path('login', views.login, name='login'),
    # URL pour afficher la page d'inscription
    path('register', views.register, name='register'),
    # URL pour gérer la déconnexion de l'utilisateur
    path('logout', views.logout, name='logout'),
]
