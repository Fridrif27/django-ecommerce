#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py loaddata fixtures/goods/categories.json
python manage.py loaddata fixtures/goods/products.json

python manage.py runserver 0.0.0.0:${PORT:-8000}