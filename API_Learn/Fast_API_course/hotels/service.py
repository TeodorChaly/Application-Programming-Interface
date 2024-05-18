# service
import random
from datetime import date
from operator import or_

from sqlalchemy import select, and_

from API_Learn.Fast_API_course.database import new_session
from API_Learn.Fast_API_course.hotels.models import Hotels
from API_Learn.Fast_API_course.service.base import BaseDAO


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def add(
            cls,
            user_id: str,
            room_id: int,
            date_from: date,
            date_to: date,
    ):
        # booked_room = select(Hotels).where(  # SQLAlchemy query
        #     and_(
        #         Hotels.id == 1,
        #         Hotels.rooms_quantity > 0
        #     )).cte("booked_room")

        # print(booked_room) SQL query

        # Logic of booking
        if_booked = random.randint(0, 1)
        if if_booked:
            return {"message": "Room is booked"}
        return {"message": "Room is not available"}
