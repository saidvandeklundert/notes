

### Install the app:

```
python -m pipenv check
python -m pipenv update
python -m pipenv shell
python -m pipenv run
```

### start the app:

```
python -m pipenv shell
uvicorn orders.app:app --reload
```

After this, go to http://127.0.0.1:8000/docs to see the Swagger UI.

Alternatively, check http://127.0.0.1:8000/redoc to check the Redoc visualization.

## structure:

`orders/app.py`: instance of the FastAPI class that represents the API we are implementing
`orders/api/api/py`: the implementation of the API
`orders/api/schema.py`: the schemas and models


## Notes:

Use the ``response_model` parameter to ensure FastApi validates the API response before letting it leave the server. The effect of the below is that the response for the 'orders' API endpoint is first run through the GetOrdersSchema Pydantic model.
```python
@app.get("/orders", response_model=GetOrdersSchema)
def get_orders():
    return [order]
```

