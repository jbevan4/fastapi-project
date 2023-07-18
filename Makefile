.PHONY: test test-with-coverage open-html-coverage

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov=fastapi_project --cov-report xml --cov-report html

open-html-coverage:
	open htmlcov/index.html