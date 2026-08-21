.PHONY: up down build logs restart clean status

up:
	docker-compose up -d

build:
	docker-compose up --build -d

down:
	docker-compose down

clean:
	docker-compose down -v
	
logs:
	docker-compose logs -f

restart:
	docker-compose restart

status:
	docker-compose ps