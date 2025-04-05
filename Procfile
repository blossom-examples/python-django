web: gunicorn jokes.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate && python manage.py loaddata initial_data