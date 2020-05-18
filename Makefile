run:
	python ./src/start.py

test:
	nose2 -c nose2.cfg

run-coverage:
	coverage run -m nose2

coverage-report:
	coverage report --omit="*/test*,*/env/*"
