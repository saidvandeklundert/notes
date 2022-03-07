from fastapi import APIRouter
from src.operations.bookings import (
    read_all_bookings,
    read_booking,
    create_booking,
    delete_booking,
    BookingCreateData,
    BookingUpdateData,
)


router = APIRouter()


@router.get("/bookings")
def api_read_all_bookins():
    return read_all_bookings()


@router.get("/booking/{booking_id}")
def api_read_booking(booking_id: int):
    return read_booking(booking_id)


@router.post("/booking")
def api_create_booking(booking: BookingCreateData) -> BookingCreateData:
    return create_booking(booking)


@router.delete("/booking/{booking_id}")
def api_delete_booking(
    booking_id: int, booking: BookingUpdateData
) -> BookingUpdateData:
    return delete_booking(booking_id, booking)
