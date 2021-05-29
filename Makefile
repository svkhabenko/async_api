compose_file = docker-compose.yml

init:
	cp .env.local .env
	pip install pre-commit
	pre-commit install

start:
	docker-compose -f $(compose_file) up

infra:
	docker-compose -f $(compose_file) up -d --build postgres redis