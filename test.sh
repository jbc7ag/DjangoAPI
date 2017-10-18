#!/usr/bin/env bash
python manage.py migrate personas zero
python magane.py migrate lugares zero
python manage.py migrate User zero
python manage.py makemigrations
python manage.py migrate
python manage.py test