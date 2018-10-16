.PHONY: collectstatics isort isort-check run install test

collectstatics: compile-scss
	./manage.py collectstatic --noinput

isort:
	isort */*.py

isort-check:
	isort -c */*.py

run:
	python manage.py runserver 0.0.0.0:8000

install:
	pip install -r requirements/dev.txt

test:
	@coverage run --source=. manage.py test -v2
