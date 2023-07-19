.PHONY: test test-with-coverage open-html-coverage ruff black

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov=fastapi_project --cov-report xml --cov-report html

open-html-coverage:
	open htmlcov/index.html

ruff:
	ruff . --fix

black:
	black .

serve:
	poetry run uvicorn main:app --reload