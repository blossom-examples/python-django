# Django Jokes App

A ready-to-deploy Django application for managing and displaying jokes. This app is designed to be deployed on [Blossom](https://blossom-cloud.com).

## Features

- View a list of all jokes
- Add, edit, and delete jokes
- Get a random joke
- Categorize jokes

## Quick Start

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or `venv/Scripts/activate` on Windows
source venv/bin/activate.fish  # fish shell

# Install dependencies
pip install -r requirements.txt

# Set up the database
createdb jokes_dev  # Create PostgreSQL database

# Run migrations
python manage.py migrate

# Load initial data
python manage.py loaddata initial_data

# Run the development server
python manage.py runserver
```

Visit `http://localhost:8000` in your browser to see the application.

## Database Configuration

The application uses PostgreSQL by default. You can configure the database connection using environment variables:

```bash
export DB_NAME=jokes_dev
export DB_USER=your_postgres_user
export DB_PASSWORD=your_postgres_password
# Optional: DB_HOST and DB_PORT if different from defaults
```

Or use a `.env` file:
```
DB_NAME=jokes_dev
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
```

For production deployment on Blossom, the `DATABASE_URL` environment variable will be automatically set.

## Deployment

This application is configured for deployment on Blossom. The Procfile includes:

- Web process: Runs the Gunicorn server
- Release process: Runs migrations and loads initial data

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string (for production)
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`: PostgreSQL connection details
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
