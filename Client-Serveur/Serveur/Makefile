# Variables
PYTHON = python3
DOCKER = docker
DOCKER_COMPOSE = docker-compose

# Commandes
build:
    $(DOCKER_COMPOSE) build

up:
    $(DOCKER_COMPOSE) up -d

down:
    $(DOCKER_COMPOSE) down

tests:
    $(PYTHON) -m unittest discover tests/

migrate:
    $(PYTHON) manage.py migrate

.PHONY: ufw
ufw:
	sudo ufw allow OpenSSH
	sudo ufw allow 'Nginx Full'  # Ou remplacez par votre serveur web
	sudo ufw enable
	sudo ufw status