# Variables
PYTHON = python3
PIP = pip3
PROTOC = python -m grpc_tools.protoc
PROTO_FILES = central_sync.proto
OUT_DIR = .



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

.PHONY: generate
generate:
        $(PROTOC) -I. --python_out=$(OUT_DIR) --grpc_python_out=$(OUT_DIR) $(PROTO_FILES)
