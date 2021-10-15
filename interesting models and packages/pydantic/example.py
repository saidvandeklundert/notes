from pydantic import BaseModel


class Human(BaseModel):
    name: str
    age: int

    class Config:
        """make it 'immutable'"""

        allow_mutation = False


marie_d = {"name": "marie", "age": 2}

marie = Human(**marie_d)

marie.dict()
marie.schema_json()
print(marie.schema_json(indent=2))