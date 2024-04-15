# Importation de la classe AppConfig depuis le module django.apps
from django.apps import AppConfig

# Définition de la configuration de l'application Django "chatbot"
class ChatbotConfig(AppConfig):
    # Définition du champ automatique par défaut pour les modèles de base de données
    default_auto_field = "django.db.models.BigAutoField"
    # Définition du nom de l'application
    name = "chatbot"
