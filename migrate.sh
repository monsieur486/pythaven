#!/bin/bash


python manage.py collectstatic -v 0 && python manage.py makemigrations && python manage.py migrate