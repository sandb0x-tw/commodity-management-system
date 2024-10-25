.PHONY: up down lint


up:
	docker compose up -d

down:
	docker compose down

lint:
	pylint ./ --recursive=true
