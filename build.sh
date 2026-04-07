#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='romaric').exists():
    User.objects.create_superuser('romaric', 'romaricyelkouni1@gmail.com', 'unzmpci2025')
    print('Superuser created')
else:
    print('Superuser exists')
"
