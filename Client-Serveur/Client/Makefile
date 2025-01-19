# Variables
PYTHON = python3
PIP = pip3

# Cibles principales
.PHONY: setup
setup: install
	echo "Setup Terminer"

.PHONY: install
install:
	$(PIP) install -r requirements.txt

.PHONY: run
run:
	$(PYTHON) -m app.main

.PHONY: test
test:
	$(PYTHON) -m pytest tests/

.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache

.PHONY: ufw
ufw:
	sudo ufw allow OpenSSH
	sudo ufw allow 'Nginx Full'  # Ou remplacez par votre serveur web
	sudo ufw enable
	sudo ufw status