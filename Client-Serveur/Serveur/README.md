# Système de gestion sécurisé avec HSM et gRPC

Ce projet est une application sécurisée utilisant un HSM (Hardware Security Module) pour gérer des clés sensibles, gRPC pour la communication entre magasins et serveurs, et FastAPI pour l'API REST.

## Prérequis

- Python 3.9 ou supérieur
- Docker et Docker Compose (facultatif, pour exécuter dans des conteneurs)

## Installation

1. Clonez ce répertoire sur votre machine locale.

    ```bash
    git clone https://votre-repository.git
    cd votre-repository
    ```

2. Créez un environnement virtuel et activez-le.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    ```

3. Installez les dépendances.

    ```bash
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement dans `.env` (voir plus haut).

5. Lancez l'application.

    ```bash
    uvicorn app.main:app --reload
    ```

## Docker

Si vous préférez utiliser Docker, vous pouvez construire et démarrer les services avec Docker Compose.

```bash
docker-compose up --build
