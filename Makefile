run:
	python -m src.start.py

gunicorn:
	gunicorn src.server:app

test:
	nose2 -c nose2.cfg

run-coverage:
	coverage run -m nose2

coverage-report:
	coverage report --omit="*/test*,*/env/*"
