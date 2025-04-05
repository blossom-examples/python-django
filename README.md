# Django Jokes App

A simple Django application for managing and displaying jokes. This app is designed to be deployed on [Blossom](https://blossom-cloud.com).

## Features

- View a list of all jokes
- Add, edit, and delete jokes
- Get a random joke
- Categorize jokes

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up the database
python manage.py migrate

# Load initial data
python manage.py loaddata initial_data

# Run the development server
python manage.py runserver
```

Visit `http://localhost:8000` in your browser to see the application.

## Deployment

This application is configured for deployment on Blossom. The Procfile includes:

- Web process: Runs the Gunicorn server
- Release process: Runs migrations and loads initial data

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
