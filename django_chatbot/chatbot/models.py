
# Importation des modules nécessaires depuis Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Définition des modèles de données de l'application Django "chatbot"
class Chat(models.Model):
    # Champ pour lier chaque message à un utilisateur (utilisation d'une clé étrangère)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Champ pour stocker le message envoyé par l'utilisateur
    message = models.TextField()
    # Champ pour stocker la réponse générée par le chatbot
    response = models.TextField()
    # Champ pour stocker la date et l'heure de création du message
    created_at = models.DateTimeField(auto_now_add=True)

    # Méthode spéciale pour afficher une représentation lisible de l'objet Chat
    def __str__(self):
        return f'{self.user.username}: {self.message}'
