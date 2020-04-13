VENV_NAME=.venv
BIN=$(VENV_NAME)/bin/

install:
	rm -rf $(VENV_NAME)
	virtualenv $(VENV_NAME) -p python3
	poetry install

test:
	$(BIN)pytest

build:
	poetry build

publish: build
	poetry publish -u __token__ -p $(POETRY_PYPI_TOKEN_PYPI)