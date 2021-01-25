dev:
	docker-compose up -d --build
dev_hot_reload:
	docker-compose up -d --build
	nodemon --delay 80ms --exec 'docker-compose stop flask && docker-compose up --build flask' flask