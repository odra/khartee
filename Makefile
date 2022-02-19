SHELL := /bin/bash

test/code:
	@poetry run mypy --strict ./src

test/unit:
	@poetry run python -m pytest ./test/unit

test: test/code test/unit

.PHONY: test/code test/unit test
