from src.db.engine import DBSession
from src.db.models import DBRoom, to_dict


def read_all_rooms():
    session = DBSession()
    rooms = session.query(DBRoom).all()
    return [to_dict(r) for r in rooms]


def read_room(room_id: int):
    session = DBSession()
    room = session.query(DBRoom).get(room_id)
    return to_dict(room)
