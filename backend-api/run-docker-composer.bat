docker-compose build
docker-compose run web bash -c "python manage.py makemigrations herokuapp && python manage.py migrate && python manage.py createsuperuser --email admin@example.com --username admin"
docker-compose up
docker-compose up -d