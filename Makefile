SHELL := /bin/bash
BOOTSTRAP_JS_URL := https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js
BOOTSTRAP_CSS_URL := https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css

web/static/clean:
	@rm -rf  src/khartee/web/static

web/static/prepare:
	@mkdir -p src/khartee/web/static/js
	@mkdir -p src/khartee/web/static/css

web/static/download: web/static/prepare
	$(shell curl '${BOOTSTRAP_JS_URL}' > src/khartee/web/static/js/bootstrap.bundle.min.js) 
	$(shell curl '${BOOTSTRAP_CSS_URL}' > src/khartee/web/static/css/bootstrap.min.css)

web/static: web/static/clean web/static/prepare web/static/download

docs/clean:
	@rm -rf ./docs/build

docs/build:
	@poetry run sphinx-build -M html ./docs/source ./docs/build

docs: docs/build

test/code:
	@poetry run mypy --strict ./src

test/unit:
	@poetry run python -m pytest ./test/unit

test: test/code test/unit

.PHONY: test/code test/unit test
.PHONY: docs/clean docs/build docs
.PHONY: web/static/prepare web/static/download web/static/clean web/static
