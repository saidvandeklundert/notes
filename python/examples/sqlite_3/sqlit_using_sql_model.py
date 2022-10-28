from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional


class Human(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int


sqlite_file_name = "humans.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

"""
The SQLModel class has a metadata attribute. 
Whenever you create a class that inherits from SQLModel and 
 is configured with table = True, it is registered in this metadata attribute.

when 'SQLModel.metadata.create_all(engine)' is called, tables are created
 for all known models that have 'table=True'.
"""
engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)

humans = [Human(name="Jan", age=7), Human(name="Marie", age=4)]

with Session(engine) as session:
    for human in humans:
        session.add(human)
    session.commit()
with Session(engine) as session:
    statement = select(Human).where(Human.name == "Marie")
    human = session.exec(statement).first()
    print(human)
