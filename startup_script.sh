#! /usr/bin/bash

echo 'Running startup script'

cd /home/jamie/site

source venv/bin/activate


python3 main.py

#prod
#uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
