#!/bin/bash

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Optional: Create superuser if needed (this is just an example)
# Uncomment the following line to create a superuser automatically. 
# You might want to handle this more securely in production.
# python manage.py createsuperuser --noinput --username admin --email admin@example.com

echo "Running Server..."
python manage.py runserver
