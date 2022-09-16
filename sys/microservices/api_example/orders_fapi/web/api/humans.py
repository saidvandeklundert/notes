import uuid
from datetime import datetime
from uuid import UUID

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from web.app import app


from humans.humans_service.humans import Human, Humans

humans: list[Human] = []
humans.append(Human(id=uuid.uuid4(), name="Said van de Klundert", age=38))


@app.get("/humans", response_model=Humans)
def get_humans():
    """Returns all the Humans found in the database."""
    return {"humans": humans}


@app.post("/humans", status_code=status.HTTP_201_CREATED, response_model=Human)
def add_human(human: Human):

    humans.append(human)
    return human


@app.put("/humans/{order_id}", response_model=Human)
def update_human(human_id: UUID, human_update: Human):
    for idx, human in enumerate(humans):
        if human.id == human_id:
            update_data = human_update.dict(exclude_unset=True)
            updated_human = human.copy(update=update_data)
            humans[idx] = updated_human
            return human
    raise HTTPException(status_code=404, detail=f"Human with ID {human_id} not found")
