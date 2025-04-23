# Django Jokes App

A ready-to-deploy Django application for managing and displaying jokes. This app is designed to be deployed on [Blossom](https://blossom-cloud.com).

## Quick Start

```bash
# Create and activate virtual environment
# Note: Only if you're using venv
python -m venv venv
source venv/bin/activate  # or `venv/Scripts/activate` on Windows
source venv/bin/activate.fish  # fish shell

# Install dependencies
pip install -r requirements.txt

# Set up the database
createdb jokes_dev  # Create PostgreSQL database
# createdb python_django -h 127.0.0.1 -U postgres # Another example
# You can configure .env

# Run migrations
python manage.py migrate

# Load initial data
python manage.py loaddata initial_data

# Run the development server
python manage.py runserver
```

Visit `http://localhost:8000` in your browser to see the application.

## Database Configuration

The application uses PostgreSQL by default. You can configure the database connection using environment variables or with .env:

For production deployment on Blossom, the `DATABASE_URL` environment variable will be automatically set.

## Environment Variables

- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: PostgreSQL connection string (for production)
- `DEBUG`: Set to False in production
- `SECRET_KEY`: Django secret key
