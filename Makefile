dev:
	docker-compose up -d --build
dev_hot_reload:
	docker-compose up -d --build
	watchmedo shell-command \
    --patterns="*.py" \
    --recursive \
		--timeout=2\
    --command='docker-compose stop flask && docker-compose up --build flask' \
    flask

ci-unit-tests:
	docker-compose build flask
	docker-compose run --rm --no-deps --entrypoint="python -m pytest" flask tests