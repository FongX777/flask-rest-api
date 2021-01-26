dev:
	docker-compose up -d --build
dev_hot_reload:
	docker-compose up -d --build
	watchmedo shell-command \                                                                                                    main     11:29
    --patterns="*.py" \
    --recursive \
		--timeout=2\
    --command='docker-compose stop flask && docker-compose up --build flask' \
    flask

unit-tests:
	docker-compose run --rm --no-deps --entrypoint=pytest flask /web/tests