# mentorship-backend

## DEV

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


### Run Pylinter

Looks for "errors" in the code.

`flake8 --format=wemake your_module.py`

> Example:  `flake8 --format=wemake job/` This line of code will run the pylinter on all the python files inside the job folder and it's children.

### Run Auto-Formatter

Tries to automatically fix some of the code "errors" that would show up on the pylinter.

`autopep8 --in-place --aggressive --aggressive <filename>`

> Example:  `autopep8 --in-place --aggressive --aggressive job/`  This line of code will run the auto-formatter on all the python files inside the job folder and it's children.

### Figma Prototype

https://www.figma.com/file/Qg08r5xH2nlWXmAao32k0I/Vagas-para-J%C3%BAnior?node-id=105%3A466



## Produção

Na pastar `docker` existe um docker compose para rodar o docker de Django e a base de dados juntos.

`docker-compose up`
