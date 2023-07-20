.PHONY: test test-with-coverage open-html-coverage lint format adr

test:
	poetry run pytest

test-with-coverage:
	poetry run pytest --cov=fastapi_project --cov-report xml --cov-report html

open-html-coverage:
	open htmlcov/index.html

lint:
	ruff . --fix

format:
	black .

serve:
	poetry run uvicorn main:app --reload

adr:
	@echo "Enter ADR title: "; \
	read title; \
	title=`echo $$title | tr ' ' '_'`; \
	filename=docs/adrs/`date +%Y_%m_%d`_$$title.md; \
	cp docs/adrs/TEMPLATE.md $$filename; \
	sed -i '' "s/short title of solved problem and solution/$$title/g" $$filename; \
	sed -i '' "s/Status: \[proposed | rejected | accepted | deprecated | … | superseded by \[ADR-0005\]()\]/Status: proposed/g" $$filename; \
	sed -i '' "s/Date: \[YYYY-MM-DD when the decision was last updated\]/Date: `date +%Y-%m-%d`/g" $$filename;