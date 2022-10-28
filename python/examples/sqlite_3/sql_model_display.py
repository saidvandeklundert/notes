from sqlmodel import Field, SQLModel, create_engine, Session, select
from typing import Optional


class Human(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int


sqlite_file_name = "humans.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


humans: list[Human] = []


with Session(engine) as session:
    statement = select(Human)
    results = session.exec(statement)
    for human in results:
        print(human)
        print(type(human))
        humans.append(human)
