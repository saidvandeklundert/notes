

### Install the requirements from the Pipfile:

```
python -m pipenv check
python -m pipenv update
python -m pipenv shell
```

To leave the pipenv environment, enter 'exit'.

### Start the container:

```
docker start batfish
docker exec -it batfish bash
```





## Play with the allinone container:

```
docker pull batfish/allinone
docker run --name batfish -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone
docker cp example/. batfish:/var/tmp
docker exec -it batfish bash
apt-get update
apt-get install vim
ipython
```

Now you are in the repl and you can run the below code by pasting it in


Copy the example config from the example dir:

docker cp example batfish:var/tmp/config


Pulling files stuff from the container:
```
docker cp batfish:<filename> <filename>
docker cp batfish:bgp_process_configuration.csv bgp_process_configuration.csv
```






```
python -m pipenv pipenv install

python -m pipenv run
python -m pytest .\test\
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


