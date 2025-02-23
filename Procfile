web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn loja.wsgi:application --bind 0.0.0.0:$PORT

web: gunicorn loja.wsgi --bind 0.0.0.0:$PORT