from django.shortcuts import render
from django.http import JsonResponse
import openai 

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from django.shortcuts import redirect

from django.utils import timezone

# Clé API d'OpenAI pour accéder à l'API
openai_api_key = ""

# Configuration de la clé API d'OpenAI
openai.api_key = openai_api_key

# Fonction pour interroger OpenAI avec un message et obtenir une réponse
def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-4", # Modèle utilisé pour la génération de texte 
        messages=[
            {"role": "system", "content": "You are a helpful and empathetic assistant, focusing on providing information, resources, and support regarding issues such as abuse, violence, legal rights, and more. Your responses should be tailored to address the user's needs, ensuring their safety and well-being are prioritized. Always adhere to privacy and safety guidelines."},
            {"role": "user", "content": message}, # Message de l'utilisateur
            
        ]
    )
    
    answer = response.choices[0].message.content.strip()# Extraction de la réponse générée par OpenAI
    return answer

# Create your views here.

# Vue pour la page principale du chatbot
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)# Récupération des messages de chat précédents pour l'utilisateur

    if request.method == 'POST':
        message = request.POST.get('message')# Récupération du message envoyé par l'utilisateur
        response = ask_openai(message)# Appel à la fonction ask_openai pour obtenir une réponse

        # Enregistrement du message de l'utilisateur et de la réponse dans la base de données
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})# Renvoi de la réponse au format JSON
    return render(request, 'chatbot.html', {'chats': chats})# Renvoi du template de chatbot avec les messages précédents

# Vue pour la page de connexion
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')# Redirection vers la page principale du chatbot après la connexion
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})# Renvoi de la page de connexion avec un message d'erreur
    else:
        return render(request, 'login.html')# Renvoi de la page de connexion


# Vue pour la page d'inscription
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')# Redirection vers la page principale du chatbot après l'inscription
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})# Renvoi de la page d'inscription avec un message d'erreur
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})# Renvoi de la page d'inscription avec un message d'erreur
    return render(request, 'register.html')# Renvoi de la page d'inscription

# Vue pour la déconnexion de l'utilisateur
def logout(request):
    auth.logout(request)# Déconnexion de l'utilisateur
    return redirect('login')# Redirection vers la page de connexion
