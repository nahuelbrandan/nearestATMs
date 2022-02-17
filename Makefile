init:
	pip install -r requirements.txt

install:
	python setup.py install

run:
	nearestATMs

test:
	pytest -v

coverage:
	coverage run -m pytest

help:
	python setup.py --help-commands

uninstall:
	python setup.py uninstall
