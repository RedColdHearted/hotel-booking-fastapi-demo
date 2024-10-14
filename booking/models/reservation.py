from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base

class Reservation(Base):
    """Represent `Reservation` in db."""
    __tablename__ = "reservations"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    client_name = Column(
        String(120),
    )
    client_phone = Column(
        String(30),
    )
    client_whishes = Column(
        Text,
    )
    hotel_address = Column(
        String(120),
    )
    room_number = Column(
        Integer,
    )
    check_in = Column(
        DateTime,
    )
    check_out = Column(
        DateTime,
    )