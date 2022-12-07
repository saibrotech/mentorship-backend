# mentorship-backend

## DEV

### Configurations

Copy the file `.env.sample` to `.env`.
Edit this file if necessary.
### Docker

No terminal:

`cd docker/dev`

`docker compose up`

This will run only once in the PostgreSQL database

### Create environment

`python3 -m venv venv`

Select the interpreter before:

`pip install -r requirements.txt`


### Run server

`cd docker/dev`

`docker-compose up`

`python manage.py migrate`

`python manage.py createsuperuser` (First time only)

`python manage.py runserver`

Access: http://127.0.0.1:8000/job


### Run fixtures

`python manage.py loaddata category`

`python manage.py loaddata company`

`python manage.py loaddata job`


### Admin

Access: http://127.0.0.1:8000/admin
    
After create or edit a model:

`python manage.py makemigrations` to create migration files

`python manage.py migrate` to apply to data base

### Documentation

The models, views and tags documentation can be found in:

http://127.0.0.1:8000/admin/doc
### Run Pylinter

Looks for "errors" in the code (see `setup.cfg`).

> Example:  `flake8` This line of code will run the pylinter on all the python files inside the project excluding the .git venv and migration folders.

To check violation documentation:
https://flake8.codes/wemake-python-styleguide/0.15.3/index.html

### Run Auto-Formatter

Tries to automatically fix some of the code "errors" that would show up on the pylinter.

> Example:  `autopep8 --in-place --aggressive --recursive .`  This line of code will run the auto-formatter on all the python files inside the project folder except .git, venv and migrations.

### Figma Prototype

https://www.figma.com/file/EMwv4Gxa2o9mj1uZ1jj111/Vagas-para-J%C3%BAnior-(Novo)?node-id=991%3A8629


## Produção

Na pastar `docker` existe um docker compose para rodar o docker de Django e a base de dados juntos.

`docker-compose up`
