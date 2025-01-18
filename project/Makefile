# Variables
PYTHON = python3
PIP = pip3

# Cibles principales
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
