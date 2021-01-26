dev:
	docker-compose up -d --build
dev_hot_reload:
	docker-compose up -d --build
	watchmedo shell-command \                                                                                                    main     11:29
    --patterns="*.py" \
    --recursive \
		--event-delay=500ms\
    --command='docker-compose stop flask && docker-compose up --build flask' \
    flask
	nodemon --delay 80ms --exec 'docker-compose stop flask && docker-compose up --build flask' flask