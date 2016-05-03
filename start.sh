#!/bin/bash
cd todoapp-flask
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python todoapp/apps.py & python todoapp/api.py
