from fastapi import APIRouter
from src.operations.rooms import read_all_rooms, read_room

router = APIRouter()


@router.get("/rooms")
def api_read_all_rooms():
    return read_all_rooms()


@router.get("/room/{room_id}")
def api_read_room(room_id: int):
    return read_room(room_id)
