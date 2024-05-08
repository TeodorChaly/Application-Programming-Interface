# pip install fastapi[all]
from typing import Optional
from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

app = FastAPI()


# endpoint
@app.get("/hotels/{hotel_id}")  # hotel_id - variable
def get_hotels(hotel_id: int):  # hotel_id - int validation, date to and from - queries
    return hotel_id


@app.get("/hotels_search")
def get_hotels(
        location,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,  # Optional param
        stars: Optional[int] = Query(None, ge=1, le=5),  # Double validation

):
    return date_from, date_to


class SBooking(BaseModel):  # S - schema
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass

# Command to start web server:
# uvicorn API-Learn.Fast_API_course.main:app --reload
