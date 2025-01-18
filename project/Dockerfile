# Utiliser l'image officielle Python comme base
FROM python:3.8-slim

# Définir un répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de configuration nécessaires
COPY requirements.txt .

# Installer les dépendances définies dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source dans le conteneur
COPY . .

# Exposer les ports nécessaires
EXPOSE 5000

# Définir la commande pour exécuter l'application
CMD ["python", "app/main.py"]
