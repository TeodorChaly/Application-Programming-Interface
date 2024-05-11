# pip install fastapi[all]
from typing import Optional
from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel
from API_Learn.Fast_API_course.hotels.router import router as hotels_router

app = FastAPI()
app.include_router(hotels_router)


# endpoint
@app.get("/hotels/{hotel_id}")  # hotel_id - variable
def get_hotels(hotel_id: int):  # hotel_id - int validation, date to and from - queries
    return hotel_id


class SHotel(BaseModel):  # For frontend developers to know what to expect
    address: str
    name: str
    stars: int


@app.get("/hotels_search", response_model=list[SHotel])  # Or use -> list[SHotel] to show expected response
def get_hotels(
        location,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        has_spa: Optional[bool] = None,  # Optional param
        stars: Optional[int] = Query(None, ge=1, le=5),  # Double validation
) -> list[SHotel]:
    hotels = [
        {"address": "West York 1", "name": "Hotel A", "stars": 2},
    ]
    return hotels


class SBooking(BaseModel):  # S - schema, request model
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass

# Command to start web server:
# uvicorn API_Learn-Learn.Fast_API_course.main:app --reload
