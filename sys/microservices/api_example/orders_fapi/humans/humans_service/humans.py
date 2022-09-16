from pydantic import BaseModel
import uuid


class Human(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    age: int


class Humans(BaseModel):
    humans: list[Human]
