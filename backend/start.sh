#!/bin/sh

echo "Waiting for DB to become operational"
until psql postgresql://example:example@db/ecommerce_cart -c "\q" ; do
    >&2 echo "Waiting for postgres"
    sleep 1
done

python manage.py migrate && python manage.py runserver 0.0.0.0:8000