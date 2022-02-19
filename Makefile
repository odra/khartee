SHELL := /bin/bash

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

.PHONY: test/code test/unit test docs/clean docs/build docs
