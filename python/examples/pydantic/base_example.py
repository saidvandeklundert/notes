from pydantic import BaseModel


class Human(BaseModel):
    name: str
    age: int


jan = Human(name="Jan", age=6)

"""
>>> jan.json()
'{"name": "Jan", "age": 6}'
>>> jan.json(exclude={"age"})  
'{"name": "Jan"}'

>>> jan.dict()
{'name': 'Jan', 'age': 6}
>>> jan.dict(include={"name"}) 
{'name': 'Jan'}
"""
