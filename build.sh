#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='romaric').exists() or User.objects.create_superuser('romaric', 'romaricyelkouni1@gmail.com', 'unzmpci2025')" | python manage.py shell
