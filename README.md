# mentorship-backend

### Docker

`docker compose up`

- docker/dev <br>
    - Para rodar o docker apenas da base da dados PostgreSQL.

- /dev <br>
    - Para rodar o docker de Django e a base de dados juntos.

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


## Run fixtures
`python manage.py loaddata category`

`python manage.py loaddata company`

`python manage.py loaddata job`

## Admin

http://127.0.0.1:8000/admin

After create or edit a model:

`python manage.py makemigrations` to create migration files

`python manage.py migrate` to apply to data base


### Figma Prototype

https://www.figma.com/file/Qg08r5xH2nlWXmAao32k0I/Vagas-para-J%C3%BAnior?node-id=105%3A466