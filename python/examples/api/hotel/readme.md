
This API demonstrates several layers:
- database/lower layer, `src/db`: database specific code and models/orm
- operations/middle layer, `src/operations`: defines the methods that can perform operations. Imports the database layer models and database operations.
- routers layer, `src/routers`: access operations to perform tasks


Open a terminal in this directory and:
```
uvicorn main:app --reload
python -m uvicorn main:app --reload
```


Open another terminal and run the tests: 

```
python -m pytest .\tests.py
```



pip install fastapi  
pip install uvicorn
pip install sqlalchemy
pip install pydantic