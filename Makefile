SHELL := /bin/bash
FILES=$(shell docker ps -a -q --filter "name=ordermanager*")

# Verifica versao do docker compose.
COMPOSE_COMMAND=$(shell command -v docker-compose >/dev/null 2>&1 && echo "docker compose" || echo "docker compose")

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .pytest_cache
	rm -rf backend/src/db.sqlite3
	rm -rf backend/.pytest_cache

create-requirements:
	poetry export --without-hashes -f requirements.txt --output requirements.txt

setup:
	@if [ ! -f backend/.env ]; then \
		cp ./contrib/.env-exemple backend/.env; \
		echo "Arquivo .env criado na pasta backend/"; \
	fi

build:
	docker build -t ordermanager-api:latest .

up: build
	$(COMPOSE_COMMAND) up -d

up-log: up
	docker logs -f ordermanager-api


down:
	$(COMPOSE_COMMAND) down

up-localy:
	python backend/manage.py runserver

bash:
	docker exec -ti ordermanager-api bash

logs-api:
	docker logs -f ordermanager-api

test:
	docker exec -it ordermanager-api poetry run pytest

test-coverage:
	docker exec -it ordermanager-api poetry run pytest --cov=.

test-cov-report:
	docker exec -it ordermanager-api poetry run pytest -vvv --cov-report html --cov=.

isort:
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa  backend/. --verbose --diff

style:
	@isort -m 3 --trailing-comma --use-parentheses --honor-noqa  backend/.
	@black -S -t py37 -l 120 backend/. --exclude '/(\.git|\.venv|env|venv|build|dist)/'

lint:
	pylint backend/

pre-commit:
	@echo "Executando verificação de estilo e testes de cobertura..."
	@{ \
		make style && \
		make test-coverage; \
	} || { \
		echo "Erro ao validar o código ou testes"; \
		exit 1; \
	}
	@echo "Validação efetuada com sucesso"

.PHONY: all clean install test
