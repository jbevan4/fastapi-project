.PHONY: test test-with-coverage

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov=fastapi_project --cov-report xml --cov-report html