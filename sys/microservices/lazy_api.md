

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
flask run --reload
```

After this, go to http://127.0.0.1:8000/docs to see the Swagger UI.

Alternatively, check http://127.0.0.1:8000/redoc to check the Redoc visualization.

## structure:

`orders/app.py`: instance of the FastAPI class that represents the API we are implementing
`orders/api/api/py`: the implementation of the API
`orders/api/schema.py`: the schemas and models


