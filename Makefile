build:
	poetry install

run: static
	poetry run python squad_game/manage.py runserver

export:
	poetry export -f requirements.txt --output requirements.txt

migrate:
	poetry run python squad_game/manage.py migrate

static:
	poetry run python squad_game/manage.py collectstatic --noinput
