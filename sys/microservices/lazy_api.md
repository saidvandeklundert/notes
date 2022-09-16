

### Install the app:

```
# create venv for python 3:
python -m pipenv --three 
python -m pipenv check
python -m pipenv update
python -m pipenv shell
python -m pipenv run
```

### start the app:

```
python -m pipenv shell
uvicorn orders.app:app --reload
# or
uvicorn orders.web.app:app --reload

# or
flask run --reload
```

Swagger:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/docs/orders


## Docker

```
# build it
docker build -t orders:1.0 .
# run it
docker run --name='api' --hostname='api' --env DB_URL=sqlite:///orders.db -v C:\dev\notes\sys\microservices\docker_app\orders.db:\orders\orders.db -p 8000:8000 -it orders:1.0 
# enter container
docker exec -it -u root api bash


# use compose:
docker-compose up --build
docker-compose down
docker exec -it docker_app_api_1 bash
#
PYTHONPATH=`pwd` DB_URL=postgresql://postgres:postgres@localhost:5432/postgres alembic upgrade heads


```

## Postgress:

```
psql -d postgres -U  postgres -W 
# list databases
\l
# list tables
\dt

CREATE DATABASE database;

CREATE TABLE orders (
  id VARCHAR PRIMARY KEY,
  status VARCHAR,
  created TIMESTAMP,
  schedule_id VARCHAR,
  delivery_id VARCHAR
);

CREATE TABLE order_item (
  id VARCHAR PRIMARY KEY,
  order_id VARCHAR,
  product VARCHAR,
  size VARCHAR,
  quantity VARCHAR
);
```

Alternatively, check http://127.0.0.1:8000/redoc to check the Redoc visualization.

## structure:

`orders/app.py`: instance of the FastAPI class that represents the API we are implementing
`orders/api/api/py`: the implementation of the API
`orders/api/schema.py`: the schemas and models


