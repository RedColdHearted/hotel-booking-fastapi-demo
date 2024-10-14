import datetime

import pydantic


class ReservationBase(pydantic.BaseModel):
    """Base `Reservation` schema."""
    client_name: str
    client_phone: str
    client_whishes: str
    hotel_address: str
    room_number: int
    check_in: datetime.datetime
    check_out: datetime.datetime


class ReservationCreate(ReservationBase):
    "`Reservation` schema to create instance."
    pass


class Reservation(ReservationBase):
    "`Reservation` schema for db instance."
    id: int

    class Config:
        orm_mode = True
