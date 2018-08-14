#!/bin/bash


# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create default admin
echo "Create default admin"
python manage.py initadmin

# Start server
echo "Starting server"
uwsgi --ini /app/iban_manager/wsgi/uwsgi.ini