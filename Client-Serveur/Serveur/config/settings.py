import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class Settings:
    # Variables de configuration sensibles chargées depuis .env
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/mydatabase")
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecretkey")
    HSM_URL = os.getenv("HSM_URL", "localhost:5000")
    API_KEY = os.getenv("API_KEY", "default-api-key")

settings = Settings()
