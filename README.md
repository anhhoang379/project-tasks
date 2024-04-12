# The hoanglb_baitest Project

This is a template for easily and quickly initing a new Project.

## Prepare environment

### Create a virtual environment

```bash
pyenv virtualenv hoanglb_baitest
pyenv shell hoanglb_baitest

# or

python -m venv venv
source venv/bin/activate
```

### Install dependency packages

```bash
pip install -r requirements.txt

# for development
pip install -r requirements.dev.txt

# for testing
pip install -r requirements.test.txt
```

### Create Database

If using sqlite, you can pass this step.
This guide intends to help create PostgreSQL db

```sql
DROP DATABASE IF EXISTS hoanglb_baitest;

CREATE DATABASE hoanglb_baitest;

CREATE ROLE hoanglb_baitest WITH LOGIN PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE hoanglb_baitest TO hoanglb_baitest;
```

### Create environment file

``` bash
cp settings/.env.tpl settings/.env

# Update the environment varables as needed
```

### Run migrate to init database for the app

```bash
python manage.py migrate
```

## Create superuser

```bash
python manage.py createsuperuser
```

### Install pre-commit

```bash
# cd <TO REPO's root directory>
pre-commit install
```

### Install redis if needed

```bash
# For Ubuntu
## Install redis
sudo apt-get install redis-server
## Start service
sudo service redis-server

# For Mac
## Install redis
brew install redis
## Start service
brew services start redis
```


## Run celery

```bash
ENVIRONMENT=local celery -A celery_tasks worker -l info -Q default
ENVIRONMENT=local celery -A celery_tasks beat -l info
```

## Run flower to easily manage celery in browsers

```bash
# Run flower to manage celery
ENVIRONMENT=local celery -A celery_tasks flower
```

Then navigate to http://localhost:5555/
