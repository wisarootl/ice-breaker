lint:
	poetry run black .
	poetry run isort .
	poetry run ruff check .
	poetry run mypy .
	

gen_requirements:
	poetry export -f requirements.txt --output requirements/requirements.txt

gen_dev_requirements:
	poetry export --format requirements.txt --output requirements/dev-requirements.txt --dev