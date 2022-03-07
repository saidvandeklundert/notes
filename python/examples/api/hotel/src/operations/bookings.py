from src.routers import customers
from src.db.engine import DBSession
from src.db.models import DBBooking, DBCustomer, DBRoom, to_dict
from pydantic import BaseModel
from typing import Optional
from datetime import date


class InvalidDateError(Exception):
    pass


class BookingCreateData(BaseModel):
    room_id: int
    customer_id: int
    from_date: date
    to_date: date


class BookingUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]


def read_all_bookings():
    session = DBSession()
    bookings = session.query(DBBooking).all()
    return [to_dict(c) for c in bookings]


def read_booking(customer_id: int):
    session = DBSession()
    booking = session.query(DBBooking).get(customer_id)
    return to_dict(booking)


def create_booking(data: BookingCreateData):
    session = DBSession()
    # retrieve room
    room = session.query(DBRoom).get(data.room_id)
    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid dates.")

    booking_dict = data.dict()
    booking_dict["price"] = room.price * days

    booking = DBBooking(**booking_dict)
    session.add(booking)
    session.commit()
    return to_dict(booking)


def delete_booking(booking_id: int, data: BookingUpdateData):
    session = DBSession()
    booking = session.query(DBBooking).get(booking_id)
    session.delete(booking)
    session.commit()
    return to_dict(booking)
