## Start server

```
python -m pipenv shell      
uvicorn web.app:app --reload

python -m pipenv run uvicorn web.app:app --reload
```

## Tests

```
python -m pytest .\test\
```