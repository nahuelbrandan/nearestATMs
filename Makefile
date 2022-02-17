init:
	pip install -r requirements.txt

install:
	python setup.py install

run:
	nearestATMs

test:
	pytest -v --cov=nearest_atms tests/

help:
	python setup.py --help-commands

uninstall:
	python setup.py uninstall
