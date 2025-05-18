# Django Boilerplate Code

## Setup and Run Django Project
```bash
git clone https://github.com/amplify-tech/django-boilerplate.git
cd django-boilerplate

# Create Virtual Environment (venv)
python -m venv venv
source venv/bin/activate

# Install Django and Dependencies
cd backend
pip install -r requirements.txt

# Apply Migrations - Database Setup :
python manage.py makemigrations
python manage.py migrate

# Run the Development Server:
python manage.py runserver
```
Visit: http://127.0.0.1:8000/

For Admin Dashboard: http://127.0.0.1:8000/admin

## Django Useful Commands
```bash
# Create a Django project:
django-admin startproject projectname

# Create a Django app:
python manage.py startapp appname

# Run the development server:
python manage.py runserver

# Make and apply migrations:
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin login):
python manage.py createsuperuser

# Shell access (interactive):
python manage.py shell

# Check for issues:
python manage.py check
```
