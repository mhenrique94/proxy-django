#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

postgres://proxy_django_user:Y5qmJKRYyimBSTcvIlx2Pbgshdc5bfo9@dpg-ciunpmtgkuvoig948t3g-a/proxy_django