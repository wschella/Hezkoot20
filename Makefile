zip:
	zip -r code.zip hashcode Pipfile

module:
	pipenv run python -m hashcode

main:
	pipenv run python hashcode/main.py