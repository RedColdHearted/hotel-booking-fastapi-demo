from sqlalchemy.orm import Session, Query

from .. import models, schemas

def get_reservation(
    db: Session,
    reservation_id: int,
) -> models.Reservation | None:
    """Return `Reservation` db instance by id."""
    return (
        db.query(
            models.Reservation
        ).filter(
            models.Reservation.id == reservation_id
        ).first()
    )

def get_reservations(
    db: Session,
    skip: int = 0,
    limit: int = 10,
) -> Query[models.Reservation]:
    """Return `Reservation` query of db instances by skip and limit."""
    return db.query(models.Reservation).offset(skip).limit(limit).all()

def create_reservation(
    db: Session,
    reservation: schemas.ReservationCreate,
) -> models.Reservation:
    """Create and return `Reservation` db instance."""
    db_reservation = models.Reservation(
        client_name=reservation.client_name,
        client_phone=reservation.client_phone,
        client_whishes=reservation.client_whishes,
        hotel_address=reservation.hotel_address,
        room_number=reservation.room_number,
        check_in=reservation.check_in,
        check_out=reservation.check_out,

    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation