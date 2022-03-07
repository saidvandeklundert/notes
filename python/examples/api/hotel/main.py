from fastapi import FastAPI
from src.db.models import DBRoom
from src.db.engine import DBSession, init_db

from src.routers import rooms, customers, bookings

app = FastAPI()

DB_FILE = "sqlite:///hotel.db"


@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)


@app.get("/")
def read_root():
    return "the server is running"


app.include_router(rooms.router)
app.include_router(customers.router)
app.include_router(bookings.router)
