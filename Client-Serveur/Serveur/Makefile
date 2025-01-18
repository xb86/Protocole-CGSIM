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
