## SETUP

#### Create virtual environment
```bash
cd robots_analyzer
pipenv install
```

#### Create sqlite3 database
```bash
pipenv shell
python manage.py makemigrations robots_scraper
python manage.py migrate
```
or
```bash
pipenv run python manage.py makemigrations robots_scraper
pipenv run python manage.py migrate
```

#### Create admin user
```bash
pipenv run python manage.py createsuperuser
```

## START APPLICATION

#### Start server
```bash
pipenv run python manage.py runserver
```

visit to view login page `http://127.0.0.1:8000/`

