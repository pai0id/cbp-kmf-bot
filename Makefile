# docker & docker compose plugin are needed to run

build:
	mkdir -p deployment/db-data/
	cd deployment && sudo docker compose up --build -d
