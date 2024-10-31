.PHONY: up down lint


up:
	docker compose build
	docker compose up -d

down:
	docker compose down

lint:
	pylint ./cms/src --recursive=true
