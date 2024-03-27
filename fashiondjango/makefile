.PHONY: build up down shell logs migrate makemigrations createsuperuser

build:
	docker-compose build

up:
	docker-compose up -d && docker-compose logs -f

down:
	docker-compose down

shell:
	docker-compose exec web bash

logs:
	docker-compose logs -f

migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

createsuperuser:
	docker-compose exec web python manage.py createsuperuser
