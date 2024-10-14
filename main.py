from http import HTTPStatus

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

from booking import crud, models, schemas
from database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/reservations/", response_model=schemas.Reservation)
def create_reservation(
    reservation: schemas.ReservationCreate,
    db: Session = Depends(get_db),
):
    return crud.create_reservation(db=db, reservation=reservation)


@app.get(
    "/reservations/{reservation_id}/",
    response_model=schemas.Reservation,
)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = crud.get_reservation(db=db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Item not found",
        )
    return db_reservation


@app.get("/reservations/", response_model=list[schemas.Reservation])
def read_reservations(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    reservations = crud.get_reservations(db=db, skip=skip, limit=limit)
    return reservations